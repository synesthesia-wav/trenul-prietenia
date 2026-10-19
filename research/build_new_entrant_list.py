#!/usr/bin/env python3
"""
Build the New Entrant safety-audit target list from the FMCSA Company Census File.

Source: https://data.transportation.gov/Trucking-and-Motorcoaches/Company-Census-File/az4n-8mr2
Public, updated daily, 4.5M rows, 147 columns, Socrata/SODA API. No API key, no paid data.

WHY THIS LIST
-------------
A New Entrant carrier must pass a Safety Audit within 12 months of operating
(49 CFR 385.307). Failure to submit an acceptable corrective action plan within
45 days (passenger/HM) or 60 days (all other) results in LOSS OF USDOT
REGISTRATION (49 CFR 385.321). The audit may be conducted ELECTRONICALLY, by
submitting documents (ai.fmcsa.dot.gov/NewEntrant/SafetyAudits.aspx) - so the
deliverable is a document package and the deadline belongs to the buyer.

FMCSA published 58,600 New Entrant Safety Audits in 2023 (2024 Safety Research
Forum p.11) at an 8.7% first-attempt failure rate. The list below is the
matching population: carriers added in the last N months, active, holding
operating authority, 1-25 power units, with a reachable US phone number.

The census file has no NEW_ENTRANT flag, so ADD_DATE is the proxy: a carrier
added within the last ~12 months is inside its first 12 months, which is the
window in which the audit is scheduled or approaching.

SOCRATA QUIRKS (learned 2026-10-20, do not "fix" these)
---------------------------------------------------------
- add_date, power_units, total_drivers and phone are TEXT columns. SoQL does
  not allow >= / <= / BETWEEN on text. Use `like` for date prefixes and `in`
  for numeric ranges.
- add_date is a text column of the form YYYYMMDD, so a year prefix like
  '2026%' is the practical range filter.

USAGE
-----
  python3 research/build_new_entrant_list.py
  python3 research/build_new_entrant_list.py --months 10 --max-units 25
  python3 research/build_new_entrant_list.py --out research/data/list.csv
"""

import argparse
import csv
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://data.transportation.gov/resource/az4n-8mr2.json"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.join(HERE, "data", "new-entrant-targets.csv")

FIELDS = [
    "dot_number", "legal_name", "dba_name", "add_date", "status_code",
    "carrier_operation", "classdef", "power_units", "total_drivers",
    "phone", "cell_phone", "phy_city", "phy_state", "phy_zip", "phy_country",
    "docket1_status_code", "safety_rating", "mcs150_date",
    "crgo_genfreight", "crgo_cargoothr_desc",
]

US_STATES = {
    "AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN",
    "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH",
    "NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT",
    "VT","VA","WA","WV","WI","WY","PR","VI","GU","AS","MP",
}


def soql(**params):
    url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                return json.load(r)
        except Exception as exc:  # noqa: BLE001
            last = exc
            wait = 2 ** attempt
            print(f"  retry in {wait}s ({exc})", file=sys.stderr)
            time.sleep(wait)
    raise last


def month_prefixes(months):
    """['2026%', '202512%', ...] covering the last `months` months, newest first."""
    today = datetime.date.today()
    out = []
    y, m = today.year, today.month
    for _ in range(months):
        out.append(f"{y}{m:02d}%")
        m -= 1
        if m == 0:
            m, y = 12, y - 1
    return out


def build(months=10, min_units=1, max_units=25, out=DEFAULT_OUT, limit=None):
    prefixes = month_prefixes(months)
    date_clause = "(" + " or ".join(f"add_date like '{p}'" for p in prefixes) + ")"
    unit_clause = "(" + ",".join(f"'{i}'" for i in range(min_units, max_units + 1)) + ")"

    where = (
        f"{date_clause} "
        "and status_code = 'A' "
        "and carrier_operation = 'A' "
        "and docket1_status_code = 'A' "
        f"and power_units in {unit_clause} "
        "and total_drivers != '0' "
        "and phone is not null and phone != ''"
    )

    print(f"Window: last {months} months ({prefixes[0]} .. {prefixes[-1]})")
    print(f"Power units: {min_units}-{max_units}")
    print("Querying (this takes a minute)...", file=sys.stderr)

    rows = []
    offset, page = 0, 5000
    while True:
        batch = soql(**{
            "$select": ",".join(FIELDS),
            "$where": where,
            "$limit": page,
            "$offset": offset,
            "$order": "add_date DESC, dot_number",
        })
        if not batch:
            break
        rows.extend(batch)
        offset += len(batch)
        if len(batch) < page:
            break
        if limit and offset >= limit:
            break
        if offset > 300000:
            print("  [stopped at 300k cap]", file=sys.stderr)
            break

    # --- filter and score -------------------------------------------------
    kept = []
    dropped = {"non_us": 0, "bad_phone": 0, "no_state": 0}
    for r in rows:
        st = (r.get("phy_state") or "").strip().upper()
        if st not in US_STATES:
            dropped["non_us"] += 1
            continue
        phone = (r.get("phone") or "").strip()
        if not (phone.isdigit() and len(phone) == 10):
            dropped["bad_phone"] += 1
            continue
        r["phone_fmt"] = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        r["months_since_add"] = (
            (datetime.date.today().year - int(r["add_date"][:4])) * 12
            + (datetime.date.today().month - int(r["add_date"][4:6]))
        )
        r["call_priority"] = priority(r)
        kept.append(r)

    kept.sort(key=lambda r: (r["call_priority"], r["months_since_add"]))

    cols = FIELDS + ["phone_fmt", "months_since_add", "call_priority"]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(kept)

    # --- summary ----------------------------------------------------------
    by_state, by_units, by_month = {}, {}, {}
    for r in kept:
        by_state[r["phy_state"]] = by_state.get(r["phy_state"], 0) + 1
        u = int(r.get("power_units") or 0)
        by_units[u] = by_units.get(u, 0) + 1
        by_month[r["add_date"][:6]] = by_month.get(r["add_date"][:6], 0) + 1

    print(f"\nFetched {len(rows):,}  ->  kept {len(kept):,} US-callable")
    print(f"  dropped: {dropped}")
    print(f"  states: {len(by_state)}  |  top: " + ", ".join(
        f"{s} {n:,}" for s, n in sorted(by_state.items(), key=lambda x: -x[1])[:12]))
    print("  power units: " + ", ".join(
        f"{u}PU:{n:,}" for u, n in sorted(by_units.items())))
    print("  by add month: " + ", ".join(
        f"{m}:{n:,}" for m, n in sorted(by_month.items(), reverse=True)[:12]))
    print(f"\nWrote {out}")
    print("\nFirst 10 by call priority:")
    for r in kept[:10]:
        print(f"  {r['call_priority']:>3}  {r['legal_name'][:34]:34} "
              f"{r['phy_city'][:14]:14} {r['phy_state']}  "
              f"{r['power_units']:>2}PU {r['total_drivers']:>2}drv  "
              f"add {r['add_date']}  {r['phone_fmt']}")
    return kept


def priority(r):
    """Call priority 1 (highest) to 5.

    Rationale: the nearer the first audit, the higher the urgency and the
    lower the chance the carrier has already hired someone. 5-25 power units
    is the sweet spot - big enough to have real HOS exposure, small enough
    that there is no in-house compliance function.
    """
    u = int(r.get("power_units") or 0)
    m = r["months_since_add"]

    if u >= 3 and u <= 12 and 3 <= m <= 9:
        return 1
    if u >= 2 and u <= 20 and 2 <= m <= 10:
        return 2
    if u >= 5 and u <= 25 and 3 <= m <= 10:
        return 3
    if 1 <= u <= 25 and 4 <= m <= 10:
        return 4
    return 5


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--months", type=int, default=10)
    ap.add_argument("--min-units", type=int, default=1)
    ap.add_argument("--max-units", type=int, default=25)
    ap.add_argument("--out", default=DEFAULT_OUT)
    a = ap.parse_args()
    build(a.months, a.min_units, a.max_units, a.out)
