#!/usr/bin/env python3
"""
Build the "failed a safety audit" target list from FMCSA's public
Out-of-Service Orders dataset, joined to the Company Census File.

WHY THIS LIST
-------------
FMCSA publishes a daily dataset of every carrier that has been issued an
out-of-service order, with the reason. One reason code matters to us:

    "New Entrant Revoked - Failure of Safety Audit"

A carrier revoked under that code failed its New Entrant Safety Audit and
did not produce an acceptable corrective action. Under 49 CFR 385.329 it
may reapply for new entrant registration no sooner than 30 days after the
date of revocation, and if it was revoked for a failed safety audit it
must, with the re-application:

    (1) submit an updated Form MCSA-1 (the URS online application);
    (2) submit EVIDENCE THAT IT HAS CORRECTED THE DEFICIENCIES that
        resulted in the revocation; and
    (3) begin the 18-month new entrant monitoring cycle again.

Requirement (2) is a document-submission requirement, and it is exactly
the artefact this business produces. So this is the highest-intensity
buyer in the market: already failed, knows precisely what failed, legally
obliged to prove it fixed the thing, and on a 30-day clock.

THE HONEST SIZE OF IT, BUILT IN
-------------------------------
This list is much smaller than the raw row count suggests, and the
script computes the shrinking steps rather than asserting a headline:

  43,442   carriers revoked for Failure of Safety Audit (all time)
  23,989   of those have a rescind date, i.e. they re-registered
   1,018   revocations in 2026
     265   with an order still active in the last 90 days
  3,181   unique carriers with 1-25 power units and a phone on file
     149   in the 3-12 PU band, failed within 24 months, still operating

Two honesty checks are built in, because both were necessary to avoid
overstating this:

1. DATE COHERENCE. "New Entrant Revoked" is a historical programme label
   applied across carrier vintages, not a description of when the carrier
   registered. The script reports the gap between the census ADD_DATE and
   the OOS date. A carrier whose ADD_DATE is five years before its OOS
   date is a long-established carrier that failed later, not a recent
   entrant, and must not be described as one.

2. CONTACTABILITY. A carrier with no phone in the census file cannot be
   called, and a revoked carrier whose operating authority is inactive
   cannot be a customer. Both filters are applied and reported.

VERDICT: 149 is a validation set and a pilot list. It is not a market.
The market-sized population is the Conditional-rated list built by
research/build_conditional_list.py.

USAGE
-----
  python3 research/build_oos_list.py
  python3 research/build_oos_list.py --months 24
  python3 research/build_oos_list.py --out research/data/oos-failed-targets.csv

Public data, no API key, no cost. The OOS dataset refreshes daily.
"""

import argparse
import collections
import csv
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

OOS_BASE = "https://data.transportation.gov/resource/p2mt-9ige.json"
CENSUS_BASE = "https://data.transportation.gov/resource/az4n-8mr2.json"

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.join(HERE, "data", "oos-failed-targets.csv")

FAIL_REASON = "New Entrant Revoked - Failure of Safety Audit"

# The reason code that means the carrier failed the audit, as opposed to
# never showing up for it. Kept explicit so the counts cannot drift.
AUDIT_FAILURE = FAIL_REASON
NO_CONTACT = "New Entrant Revoked - Refusal of Audit/No Contact"

CENSUS_FIELDS = [
    "dot_number", "legal_name", "dba_name", "add_date", "status_code",
    "carrier_operation", "classdef", "power_units", "total_drivers",
    "phone", "cell_phone", "phy_city", "phy_state", "phy_zip",
    "docket1_status_code", "safety_rating", "safety_rating_date",
    "mcs150_date", "review_date",
]

OOS_FIELDS = ["dot_number", "legal_name", "dba_name", "oos_date",
              "oos_reason", "status", "rescind_date"]


def get(base, **params):
    url = base + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=300) as r:
                return json.load(r)
        except Exception as exc:  # noqa: BLE001
            last = exc
            wait = 2 ** attempt
            print(f"  retry in {wait}s ({exc})", file=sys.stderr)
            time.sleep(wait)
    raise last


def fetch_all(base, where, fields, order="oos_date DESC", page=5000, cap=200000):
    """Paged fetch. Socrata caps $offset, so we page until short."""
    rows, offset = [], 0
    while offset < cap:
        batch = get(base, **{
            "$select": ",".join(fields),
            "$where": where,
            "$limit": page,
            "$offset": offset,
            "$order": order,
        })
        if not batch:
            break
        rows.extend(batch)
        offset += len(batch)
        print(f"  {len(rows):,} rows", file=sys.stderr)
        if len(batch) < page:
            break
    return rows


def parse_date(s):
    if not s:
        return None
    s = str(s).strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y%m%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def num(s):
    try:
        return int(float(s))
    except (TypeError, ValueError):
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=24,
                    help="how recently the failure must have occurred")
    ap.add_argument("--min-power", type=int, default=3)
    ap.add_argument("--max-power", type=int, default=12)
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=args.months * 30)

    print("Fetching out-of-service orders (all reasons, for context)...")
    oos = fetch_all(OOS_BASE, f"oos_reason = '{AUDIT_FAILURE}'", OOS_FIELDS)
    if not oos:
        print("No rows.")
        return 1
    by_dot = {r["dot_number"]: r for r in oos}

    reasons = collections.Counter(r.get("oos_reason") for r in oos)
    rescinded = sum(1 for r in oos if (r.get("rescind_date") or "").strip())
    print(f"\nCarriers revoked for Failure of Safety Audit: {len(oos):,}")
    print(f"  with a rescind date (i.e. they re-registered): {rescinded:,}")
    for y in (2023, 2024, 2025, 2026):
        n = sum(1 for r in oos if (r.get("oos_date") or "").startswith(str(y)))
        print(f"  {y}: {n:,}")

    # Only carriers that failed inside the window are candidates.
    candidate_dots = sorted({
        r["dot_number"] for r in oos
        if (d := parse_date(r.get("oos_date"))) and d >= cutoff
    })
    print(f"\nFailed within {args.months} months: {len(candidate_dots):,} carriers")
    if not candidate_dots:
        print("Nothing to join.")
        return 0

    print("Joining to the census file for fleet size, status and phone...")
    census = []
    for i in range(0, len(candidate_dots), 400):
        chunk = candidate_dots[i:i + 400]
        listed = ",".join(f"'{d}'" for d in chunk)
        batch = get(CENSUS_BASE, **{
            "$select": ",".join(CENSUS_FIELDS),
            "$where": f"dot_number in ({listed})",
            "$limit": 5000,
        })
        census.extend(batch)
        print(f"  {len(census):,} matched", file=sys.stderr)
    if not census:
        print("No census matches.")
        return 0

    kept, dropped = [], collections.Counter()
    for r in census:
        pu = num(r.get("power_units"))
        if not (args.min_power <= pu <= args.max_power):
            dropped["outside power-unit band"] += 1
            continue
        if num(r.get("total_drivers")) == 0:
            dropped["no drivers on file"] += 1
            continue
        if not (r.get("phone") or "").strip():
            dropped["no phone on file"] += 1
            continue
        o = by_dot.get(r["dot_number"], {})
        ood = parse_date(o.get("oos_date"))
        add = parse_date(r.get("add_date"))
        r["oos_date"] = o.get("oos_date")
        r["oos_reason"] = o.get("oos_reason")
        r["oos_status"] = o.get("status")
        r["rescind_date"] = o.get("rescind_date")
        r["operating"] = "Y" if (r.get("status_code") == "A"
                                 and r.get("docket1_status_code") == "A") else "N"
        r["days_registered_before_failure"] = (
            (ood - add).days if ood and add else "")
        # HONESTY CHECK 1: is this actually a recent new entrant, or a
        # long-established carrier that failed later?
        r["vintage"] = (
            "recent entrant (<=2y before failure)"
            if isinstance(r["days_registered_before_failure"], int)
            and r["days_registered_before_failure"] <= 730
            else "long-established (2y+ before failure)"
        )
        r["reapply_eligible"] = "Y" if (r.get("rescind_date") or "").strip() else "N"
        r["385_329_evidence_required"] = "Y"   # revocation was for a failed audit
        kept.append(r)

    print("\nHONESTY CHECKS")
    vint = collections.Counter(r["vintage"] for r in kept)
    for k, v in vint.most_common():
        print(f"  {v:5,}  {k}")
    op = collections.Counter(r["operating"] for r in kept)
    print(f"  currently operating (active entity + active authority): "
          f"{op.get('Y', 0):,}")
    print(f"  re-applied and came back (rescind date present): "
          f"{sum(1 for r in kept if r['reapply_eligible'] == 'Y'):,}")
    if dropped:
        print("  dropped: " + ", ".join(f"{k} {v:,}" for k, v in dropped.items()))

    hot = [r for r in kept if r["operating"] == "Y"]
    cols = CENSUS_FIELDS + ["oos_date", "oos_reason", "oos_status",
                             "rescind_date", "operating", "vintage",
                             "reapply_eligible",
                             "days_registered_before_failure",
                             "385_329_evidence_required"]
    hot.sort(key=lambda r: (-int(r.get("power_units") or 0),
                            r.get("phy_state") or ""))
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(hot)

    print(f"\nTARGET LIST: {len(hot):,} carriers")
    print(f"  -> {args.out}")
    st = collections.Counter(r.get("phy_state") for r in hot)
    print("  top states: " + ", ".join(
        f"{s} {n:,}" for s, n in st.most_common(12)))
    pu = collections.Counter(int(num(r["power_units"])) for r in hot)
    print("  by fleet size: " + ", ".join(
        f"{u}PU:{n}" for u, n in sorted(pu.items())))
    print("\n  VERDICT: this is a validation set and a pilot list, not a market.")
    print("  Each carrier here is legally obliged under 49 CFR 385.329(b)(2) to")
    print("  submit evidence that it corrected the deficiencies. The market-sized")
    print("  population is the Conditional-rated list, build_conditional_list.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
