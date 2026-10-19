#!/usr/bin/env python3
"""
Fill the two customer-facing documents: the cab review and the agent one-pager.

Usage:
    # 1. The cab review (2 pages: review letter + printable checklist)
    python3 assets/merge_cab_review.py results.json --dot 9099205 --out out.html
    python3 assets/merge_cab_review.py results.json --dot 9099205 --pdf

    # 2. The agent one-pager
    python3 assets/merge_cab_review.py --agent config.json --out agent.html

    # 3. A blank cab-review form, to print and fill by hand
    python3 assets/merge_cab_review.py --print-template

THE SESSION RESULTS FILE
------------------------
A JSON object. Everything except "cab" and "file" is optional and will be
rendered as a visible MISSING rather than silently blank, so a broken merge is
obvious instead of shipping a document with holes in it.

    {
      "session_date": "2026-10-21",
      "reviewer": "V. Vanica",
      "source_date": "2026-10-19",
      "event_price_line": "fixed fee, quoted before we start",
      "cab":  { "dtransfer": "y", "malfsheet": "n", "grids": "n" },
      "file": { "driverslist": "y", "licenses": "y", "rods": "n" }
    }

Values: "y" (in place), "n" (missing), "p" (not checked). Anything not
recorded defaults to "p" (not checked), never silently counted as present.

The "five things to do first" are derived from the worst cab gaps and the worst
file gaps. Override with "top_five": ["...", "...", "...", "...", "..."].

THE AGENT CONFIG FILE
---------------------
    { "our_name": "", "our_title": "", "our_phone": "", "our_email": "",
      "agency_name": "" }
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "cab-review-template.html")
AGENT_TEMPLATE = os.path.join(HERE, "agent-onepager.html")
CENSUS = "https://data.transportation.gov/resource/az4n-8mr2.json"

CAB_ORDER = [
    ("dtransfer", "ELD data-transfer instruction sheet is not in the cab",
     "395.22(h)(1) requires the carrier to ensure every driver has the sheet telling him how to produce and hand over his records to an officer. Without it, the driver cannot hand over a clean record even when his logs are perfect."),
    ("malfsheet", "ELD malfunction reporting instruction sheet is not in the cab",
     "395.22(h)(2) and 395.34(a)(1): the driver must notify you in writing within 24 hours of a malfunction. He cannot do what he does not know he should do, and a missed notice is a weight-5 finding against the carrier."),
    ("grids", "No blank graph grids in the cab",
     "395.22(h)(3) requires 8 days of blank grids, and 395.34(a)(2) requires a driver to reconstruct 24 hours plus the previous 7 days on paper after a malfunction. No paper means no compliant reconstruction."),
    ("rods7", "Drivers do not have their last 7 days of records in the cab",
     "395.8(k)(2): the driver must have his copy and be able to produce it while on duty. If it is at the office, it is not in his possession."),
    ("certified", "Logbooks are not all signed and certified",
     "395.30(b) and 395.8(f)(2): the driver certifies his own record. An uncertified log is treated as no log, which is a violation in the driver's hand and counts against the carrier."),
    ("shipdoc", "Shipping document numbers are not going into the logs",
     "395.24(c)(iii): the number that ties the log to the bill of lading. Missing it is a form-and-manner finding on every affected day, and it is the document an inspector uses to test whether the log is real."),
    ("unassigned", "Unassigned driving time is not being explained or assigned",
     "395.32(c) is a carrier duty, not a driver duty: every record of unidentified driving must be annotated to explain why, or assigned to the right driver. Left alone it is a weight-5 finding, and it is entirely mechanical to clear."),
    ("malfnote", "ELD malfunctions are not being reported to you in writing within 24 hours",
     "395.34(a)(1): failure to give written notice within 24 hours is a weight-5 violation. This is a phone call and a form."),
    ("insp", "Current annual vehicle inspection report is not in the cab",
     "396.17 and Part 396 Appendix G: every commercial vehicle inspected every 12 months, with the documentation on the vehicle."),
]

FILE_ORDER = [
    ("driverslist", "Drivers list", "FMCSA asks for every currently employed driver, to work out which rules apply to each of them."),
    ("licenses", "Driver's licence copies", "Part of each driver qualification file."),
    ("rods", "Records of duty status and supporting documentation", "6 months retained, with the supporting documents - toll receipts, fuel receipts, bills of lading, trip reports - that let an auditor verify the log is real."),
    ("mvr", "Motor vehicle records", "For every driver."),
    ("medical", "Medical certificates", "Every driver medically qualified."),
    ("vehlist", "Vehicle list", "Unit number, VIN, plate number and state, for every vehicle and trailer."),
    ("vehinsp", "Vehicle inspection reports", "Within the preceding 12 months."),
    ("insurance", "Proof of insurance", "Sufficient to meet the minimum public liability requirement."),
    ("drug", "Drug and alcohol programme", "Periodic testing for CDL drivers."),
    ("accident", "Accident register", "FMCSA-reportable crashes for the past 3 years."),
    ("authority", "Operating authority, BOC-3, IRP and IFTA", "Proof the carrier is registered to run."),
    ("submission", "Signed logbooks submitted to the carrier", "395.8(a)(2)(ii): the driver submits the certified record to the carrier within 13 days of the 24-hour period. If it never arrives, the file has a hole in it that nobody sees until an audit."),
]

MISSING = "MISSING"


def fetch_census(dot):
    url = CENSUS + "?" + urllib.parse.urlencode({
        "$where": f"dot_number = {int(dot)}",
        "$limit": 1,
    })
    with urllib.request.urlopen(url, timeout=60) as r:
        rows = json.load(r)
    if not rows:
        raise SystemExit(f"No census row for USDOT {dot}")
    return rows[0]


def month_year(add_date):
    """'20260731' -> 'July 2026'."""
    months = ["January","February","March","April","May","June","July",
              "August","September","October","November","December"]
    try:
        return f"{months[int(add_date[4:6]) - 1]} {add_date[:4]}"
    except Exception:
        return add_date


def mark(value):
    """'y' -> filled, 'n' -> empty, 'p' -> dashed."""
    return {"y": "y", "n": "n"}.get((value or "").strip().lower(), "p")


def build_results(session, census):
    cab = {k: mark(v) for k, v in (session.get("cab") or {}).items()}
    fil = {k: mark(v) for k, v in (session.get("file") or {}).items()}

    cab_ok = sum(1 for v in cab.values() if v == "y")
    cab_missing = sum(1 for v in cab.values() if v == "n")
    file_ok = sum(1 for v in fil.values() if v == "y")
    file_missing = sum(1 for v in fil.values() if v == "n")

    # Top five: worst missing cab items first, then worst missing file items.
    worst_cab = [c for c in CAB_ORDER if cab.get(c[0]) == "n"]
    worst_file = [f for f in FILE_ORDER if fil.get(f[0]) == "n"]
    picked = []
    for key, title, body in worst_cab:
        picked.append((title, body))
    for key, title, body in worst_file:
        picked.append((title, body))

    top = session.get("top_five")
    if top:
        items = list(zip(top, [""] * len(top)))
    else:
        items = [(t, b) for t, b in picked[:5]]
    while len(items) < 5:
        items.append(("Everything else on the checklist is in place.",
                       "Keep it that way - the cab list takes five minutes and it is the cheapest "
                       "protection you have."))

    out = {
        "LEGAL_NAME": census.get("legal_name", MISSING),
        "DOT_NUMBER": census.get("dot_number", MISSING),
        "PHY_CITY": census.get("phy_city", ""),
        "PHY_STATE": census.get("phy_state", ""),
        "POWER_UNITS": census.get("power_units", MISSING),
        "TOTAL_DRIVERS": census.get("total_drivers", MISSING),
        "ADD_MONTH_YEAR": month_year(census.get("add_date", "")),
        "SESSION_DATE": session.get("session_date", MISSING),
        "REVIEWER": session.get("reviewer", MISSING),
        "SOURCE_DATE": session.get("source_date", MISSING),
        "EVENT_PRICE_LINE": session.get("event_price_line", "a fixed fee, quoted before we start"),
        "N_CAB_OK": str(cab_ok), "N_CAB_MISSING": str(cab_missing),
        "N_FILE_OK": str(file_ok), "N_FILE_MISSING": str(file_missing),
    }
    for i, (t, b) in enumerate(items[:5], start=1):
        out[f"F{i}_TITLE"] = t
        out[f"F{i}_BODY"] = b
    for key, _, _ in CAB_ORDER:
        out[f"CAB:{key}"] = cab.get(key, "p")
    for key, _, _ in FILE_ORDER:
        out[f"FILE:{key}"] = fil.get(key, "p")
    return out


def render(html, values):
    def sub(m):
        key = m.group(1)
        if key in values:
            return str(values[key])
        if ":" in key:
            return MISSING
        return "MISSING"
    return re.sub(r"\{\{([A-Za-z0-9_:\-]+)\}\}", sub, html)


AGENT_FIELDS = {
    "our_name": "OUR_NAME", "our_title": "OUR_TITLE", "our_phone": "OUR_PHONE",
    "our_email": "OUR_EMAIL", "agency_name": "AGENCY_NAME",
}


def build_agent(config):
    """The agent one-pager carries no price and no client data - only who we are."""
    out = {}
    for key, value in config.items():
        out[AGENT_FIELDS.get(key, key.upper())] = value
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results", nargs="?", help="session results JSON")
    ap.add_argument("--dot", help="USDOT number of the carrier")
    ap.add_argument("--agent", metavar="CONFIG", help="agent one-pager config JSON")
    ap.add_argument("--out", help="output HTML path")
    ap.add_argument("--pdf", action="store_true", help="also print to PDF")
    ap.add_argument("--print-template", action="store_true",
                    help="print a blank template with every field marked")
    args = ap.parse_args()

    if args.agent:
        cfg = json.load(open(args.agent, encoding="utf-8"))
        html = open(AGENT_TEMPLATE, encoding="utf-8").read()
        out = render(html, build_agent(cfg))
        path = args.out or os.path.join(HERE, "agent-onepager.html")
        open(path, "w", encoding="utf-8").write(out)
        print(f"wrote {path}")
        if "MISSING" in out:
            print("  WARNING: unresolved fields in the agent one-pager", file=sys.stderr)
        return

    html = open(TEMPLATE, encoding="utf-8").read()

    if args.print_template:
        out = render(html, {})
        path = args.out or os.path.join(HERE, "cab-review-blank.html")
        open(path, "w", encoding="utf-8").write(out)
        print(f"blank template -> {path}  (open in a browser, print to PDF)")
        return

    if not args.results or not args.dot:
        ap.error("need a results JSON and --dot (or use --print-template)")

    session = json.load(open(args.results, encoding="utf-8"))
    census = fetch_census(args.dot)
    values = build_results(session, census)
    out = render(html, values)

    path = args.out or os.path.join(HERE, "cab-review.html")
    open(path, "w", encoding="utf-8").write(out)
    print(f"wrote {path}")

    missing = sorted({m for m in re.findall(r"MISSING", out)})
    if missing:
        print(f"  WARNING: {len(missing)} unresolved field(s): {missing}", file=sys.stderr)

    if args.pdf:
        try:
            subprocess.run(["/System/Library/Printers/Libraries/convert",
                            "-s", "letter", "-o", path.replace(".html", ".pdf"), out],
                           check=True, capture_output=True)
            print(f"  pdf -> {path.replace('.html', '.pdf')}")
        except Exception as exc:  # noqa: BLE001
            print(f"  (PDF conversion needs macOS 'cupsfilter' or Chrome: {exc})", file=sys.stderr)


if __name__ == "__main__":
    main()
