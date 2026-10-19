#!/usr/bin/env python3
"""
Build the Conditional-rated target list from the FMCSA Company Census File.

WHY THIS LIST
-------------
A Conditional safety rating is issued after a compliance review, and 49 CFR
385.11 requires FMCSA to notify the carrier in writing with "a list of FMCSR
and HMR compliance deficiencies which the motor carrier must correct."
49 CFR 385.11(c) makes a proposed Conditional rating final 60 days after the
notice (45 for HM/passenger). 49 CFR 385.17 lets the carrier request a rating
change AT ANY TIME on "evidence that it has taken corrective actions," and
FMCSA reviews that request within 45 days.

So the carrier holds a letter naming its deficiencies and a route to fix the
rating - and the evidence for that route is a document package. That is the
product, stated by the regulation.

THE HONEST CAVEAT, BUILT INTO THE SCORING
--------------------------------------------
Most Conditional ratings are old. In the 3-12 power-unit band, only ~128
carriers were rated in 2026 and ~84 in 2025; the rest carry a rating from
decades ago. An old rating is not a live deadline - it is a STANDING
HANDICAP on the carrier's record, visible to its broker and its insurer at
renewal. So the scoring treats freshness as the difference between a deadline
hook and a renewal hook, and the output separates them.

USAGE
-----
  python3 research/build_conditional_list.py
  python3 research/build_conditional_list.py --min-power 3 --max-power 12
  python3 research/build_conditional_list.py --out research/data/conditional.csv
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
DEFAULT_OUT = os.path.join(HERE, "data", "conditional-rated-targets.csv")

FIELDS = [
    "dot_number", "legal_name", "dba_name", "add_date", "status_code",
    "carrier_operation", "classdef", "power_units", "total_drivers",
    "phone", "cell_phone", "phy_city", "phy_state", "phy_zip",
    "docket1_status_code", "safety_rating", "safety_rating_date",
    "mcs150_date", "review_date", "crgo_genfreight", "crgo_cargoothr_desc",
]

# 395.11(c)(1) categories of supporting document, for the "file status" hint.
SUPPORTING_DOC_CATEGORIES = [
    "BOL / itinerary / schedule",
    "dispatch or trip record",
    "expense receipt for on-duty not driving",
    "electronic mobile communication record",
    "payroll or settlement record",
]


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


def fetch_all(where, fields, order="add_date DESC"):
    rows, offset, page = [], 0, 5000
    while True:
        batch = soql(**{
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
        if offset > 100000:
            print("  [stopped at 100k cap]", file=sys.stderr)
            break
    return rows


def years_since(datestr):
    if not datestr or len(datestr) < 6:
        return None
    try:
        y, m = int(datestr[:4]), int(datestr[4:6])
    except ValueError:
        return None
    today = datetime.date.today()
    return (today.year - y) * 12 + (today.month - m)


def hook(r):
    """Which hook applies.

    Honest thresholds. The 60-day window in 49 CFR 385.11(c) runs from the
    NOTICE date, so a rating from two years ago had its window close two
    years ago. A rating does not expire - it stands until the carrier wins a
    rating change under 385.17 - so the old ones are a STANDING HANDICAP,
    not a live deadline. Their trigger is the renewal conversation, and
    their pain is the agent's, not the carrier's.
    """
    y = years_since(r.get("safety_rating_date"))
    if y is None:
        return "unknown"
    months = y
    if months <= 6:
        return "A: fresh"          # corrective-action window plausibly open
    if months <= 24:
        return "B: recent"         # renewal conversation now
    return "C: standing"           # live handicap, no deadline


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-power", type=int, default=3)
    ap.add_argument("--max-power", type=int, default=12)
    ap.add_argument("--rating", default="C", help="C=Conditional U=Unsatisfactory S=Satisfactory")
    ap.add_argument("--out", default=DEFAULT_OUT)
    args = ap.parse_args()

    # All census columns are TEXT: numeric ranges need an in-list, dates need a
    # like-prefix. See procedures/fmcsa-census-target-list.md.
    pu = ",".join(f"'{i}'" for i in range(args.min_power, args.max_power + 1))
    where = (
        "status_code = 'A' "
        "and carrier_operation = 'A' "
        "and docket1_status_code = 'A' "
        f"and power_units in ({pu}) "
        "and total_drivers != '0' "
        "and phone is not null and phone != '' "
        f"and safety_rating = '{args.rating}'"
    )
    print(f"Fetching {args.rating}-rated carriers, {args.min_power}-{args.max_power} power units...")
    rows = fetch_all(where, FIELDS)
    if not rows:
        print("No rows.")
        return 0

    buckets = {}
    for r in rows:
        r["hook"] = hook(r)
        r["months_since_rating"] = years_since(r.get("safety_rating_date"))
        p = (r.get("phone") or "").strip()
        r["phone_fmt"] = f"{p[:3]}-{p[3:6]}-{p[6:]}" if p.isdigit() and len(p) == 10 else p
        buckets[r["hook"]] = buckets.get(r["hook"], 0) + 1
        r["file_categories_due"] = len(SUPPORTING_DOC_CATEGORIES)

    # Hook A first (live clock), then most recent rating, then most trucks.
    order = {"A: live clock": 0, "B: recent": 1, "C: standing": 2, "unknown": 3}
    rows.sort(key=lambda r: (order.get(r["hook"], 4),
                             -(r.get("months_since_rating") or 999),
                             -int(r.get("power_units") or 0)))

    cols = FIELDS + ["phone_fmt", "months_since_rating", "hook", "file_categories_due"]
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    print(f"\n{len(rows):,} carriers  ->  {args.out}")
    for k in sorted(buckets, key=lambda x: order.get(x, 9)):
        print(f"  {k:16} {buckets[k]:6,}")
    by_state = {}
    for r in rows:
        by_state[r.get("phy_state") or "?"] = by_state.get(r.get("phy_state") or "?", 0) + 1
    print("  top states: " + ", ".join(
        f"{s} {n:,}" for s, n in sorted(by_state.items(), key=lambda x: -x[1])[:14]))
    pu_hist = {}
    for r in rows:
        pu_hist[r.get("power_units")] = pu_hist.get(r.get("power_units"), 0) + 1
    print("  by power units: " + ", ".join(f"{u}PU:{n:,}" for u, n in sorted(pu_hist.items(), key=lambda x: int(x[0] or 0))))
    print("\n  hook A: live 60-day clock -> lead with the deadline")
    print("  hook B: recent -> lead with the renewal")
    print("  hook C: standing -> the agent's problem, not the carrier's")
    return 0


if __name__ == "__main__":
    sys.exit(main())
