#!/usr/bin/env python3
"""
Aggregate session records into the evidence we need, and print the three gate
decisions.

    python3 research/aggregate_sessions.py
    python3 research/aggregate_sessions.py --dir research/sessions --out research/data/sessions.csv

WHY THIS EXISTS
---------------
The strategy panel (research/strategy-memo.md) identified the number nobody
has: the defect rate on real small fleets, per regulation. It decides the
thesis in week one - if most fleets come back clean, the paperwork thesis
is wrong and we find out before spending the fixed cost.

It also produces the price evidence, because the price was marked
"confirmed" in the plan by two people in a room with no buyer in it.

INPUT
-----
JSON files in research/sessions/, one per session, as produced by
assets/session-sheet.html. Missing fields are treated as "not recorded",
never as "in place".

OUTPUT
------
1. The defect table, by regulation.
2. The funnel: sessions -> pilots -> closed.
3. The price evidence: what they pay today, and their own ceiling.
4. The three gate decisions, each with a verdict against the threshold
   that was written down in advance.
"""

import argparse
import collections
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DEFAULT_DIR = os.path.join(HERE, "sessions")
TEMPLATE = os.path.join(ROOT, "assets", "cab-review-template.html")
FORM = os.path.join(ROOT, "assets", "session-sheet.html")

# The thresholds, as written in PLAN.md and the research memo BEFORE the data
# existed. They do not move after the fact.
GATE_DEFECT = (20, 15)      # (sessions needed to measure, non-zero count required)
                          # i.e. >= 15 of 20 sessions with a non-zero defect count
GATE_WTP = 3                # >= 3 of 10 willing to pay above $100/truck/month
GATE_PILOT = 0.25           # >= 25% of sessions convert to a pilot
GATE_CLOSE = 0.50           # >= 50% of pilots convert to a contract


def _array_keys(form, name):
    """Pull the first element of each pair from `const NAME = [ ... ];` only.

    Scoping to the named array matters: the tri-state glyph table that follows
    it is also an array of string pairs, and a naive regex picks it up.
    """
    m = re.search(r"const\s+" + name + r"\s*=\s*\[", form)
    if not m:
        return set()
    start = m.end() - 1
    depth, i = 0, start
    while i < len(form):
        if form[i] == "[":
            depth += 1
        elif form[i] == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    body = form[start + 1:i]
    return set(re.findall(r'\[\s*"([a-z0-9_]+)"\s*,', body))


def template_keys():
    """Pull the item keys straight out of the two HTML files, so the three
    files cannot silently drift apart."""
    tpl = open(TEMPLATE, encoding="utf-8").read()
    form = open(FORM, encoding="utf-8").read()
    cab_t = set(re.findall(r"\{\{CAB:([a-z0-9_]+)\}\}", tpl))
    file_t = set(re.findall(r"\{\{FILE:([a-z0-9_]+)\}\}", tpl))
    cab_f = _array_keys(form, "CAB")
    file_f = _array_keys(form, "FILE")
    problems = []
    if cab_t != cab_f:
        problems.append(f"cab keys differ: template-only={sorted(cab_t - cab_f)} "
                        f"form-only={sorted(cab_f - cab_t)}")
    if file_t != file_f:
        problems.append(f"file keys differ: template-only={sorted(file_t - file_f)} "
                        f"form-only={sorted(file_f - file_t)}")
    return cab_t, file_t, problems


CAB_LABELS = {
    "dtransfer":  ("ELD data-transfer instruction sheet",        "395.22(h)(1)"),
    "malfsheet":  ("ELD malfunction reporting instruction sheet","395.22(h)(2) / 395.34(a)"),
    "grids":      ("8 days of blank graph grids",               "395.22(h)(3) / 395.34(a)(2)"),
    "rods7":      ("Driver's last 7 days of records in the cab", "395.8(k)(2)"),
    "certified":  ("Logbooks signed and certified",              "395.30(b) / 395.8(f)(2)"),
    "shipdoc":    ("Shipping document number in the log",        "395.24(c)(iii)"),
    "unassigned": ("Unassigned driving time explained/assigned", "395.32(c)"),
    "malfnote":   ("Last malfunction reported in writing, 24h",  "395.34(a)(1)"),
    "insp":       ("Annual vehicle inspection report in the cab","396.17 / App. G"),
}
FILE_LABELS = {
    "driverslist": ("Drivers list",                 "FMCSA Resource Guide"),
    "licenses":    ("Driver's licence copies",      "Part 391"),
    "rods":        ("Records of duty status + supporting docs", "395.8(k)(1)"),
    "mvr":         ("Motor vehicle records",        "Part 391"),
    "medical":     ("Medical certificates",         "391.49"),
    "vehlist":     ("Vehicle list",                 "FMCSA Resource Guide"),
    "vehinsp":     ("Vehicle inspection reports",   "396.17"),
    "insurance":   ("Proof of insurance",           "FMCSA Resource Guide"),
    "drug":        ("Drug & alcohol programme",     "Part 382"),
    "accident":    ("Accident register",            "390.9"),
    "authority":   ("Authority, BOC-3, IRP/IFTA",  "FMCSA Resource Guide"),
    "submission":  ("Signed logbooks submitted to the carrier", "395.8(a)(2)(ii)"),
}


def load(directory):
    sessions = []
    if not os.path.isdir(directory):
        return sessions
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".json") or name.startswith("_"):
            continue
        try:
            s = json.load(open(os.path.join(directory, name), encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print(f"  ! skipped {name}: {exc}", file=sys.stderr)
            continue
        s["_file"] = name
        sessions.append(s)
    return sessions


def num(v):
    if v is None:
        return None
    m = re.search(r"[\d,]+(?:\.\d+)?", str(v).replace("$", ""))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", ""))
    except ValueError:
        return None


def dollars(v):
    """Return the dollar figure in a free-text answer, or None."""
    if v is None:
        return None
    m = re.findall(r"\$?\s*([\d,]+(?:\.\d+)?)\s*([kK]?)", str(v))
    if not m:
        return None
    best = None
    for num_s, mult in m:
        try:
            x = float(num_s.replace(",", ""))
        except ValueError:
            continue
        if mult.lower() == "k":
            x *= 1000
        if best is None or x > best:
            best = x
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--out", default=os.path.join(HERE, "data", "sessions.csv"))
    args = ap.parse_args()

    cab_keys, file_keys, problems = template_keys()
    if problems:
        print("KEY MISMATCH between the template and the session form:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        print("  Fix before collecting any more sessions.", file=sys.stderr)
        return 2

    sessions = load(args.dir)
    print(f"Sessions found: {len(sessions)}  ({args.dir})\n")
    if not sessions:
        print("Nothing to aggregate yet. Fill in assets/session-sheet.html and save to",
              args.dir)
        return 0

    # ---------------- defect table ----------------
    def rate(items, key):
        y = sum(1 for s in sessions if (s.get(items) or {}).get(key) == "y")
        n = sum(1 for s in sessions if (s.get(items) or {}).get(key) == "n")
        p = sum(1 for s in sessions if (s.get(items) or {}).get(key) == "p")
        return y, n, p

    non_zero = 0
    for s in sessions:
        cab = s.get("cab") or {}
        fil = s.get("file") or {}
        vals = list(cab.values()) + list(fil.values())
        if any(v == "n" for v in vals):
            non_zero += 1

    print("=" * 78)
    print("1. DEFECT RATE  —  the number nobody has")
    print("=" * 78)
    print(f"Sessions with at least one missing item: {non_zero} of {len(sessions)} "
          f"({100*non_zero/len(sessions):.0f}%)\n")

    for group, keys, labels in (("PART A - IN THE CAB", sorted(cab_keys), CAB_LABELS),
                                ("PART B - IN THE FILE", sorted(file_keys), FILE_LABELS)):
        print(f"{group}")
        print(f"  {'item':46} {'cite':26} {'in place':>9} {'missing':>8} {'n/chk':>7}")
        print("  " + "-" * 98)
        for k in keys:
            label, cite = labels.get(k, (k, ""))
            y, n, p = rate("cab" if group.startswith("PART A") else "file", k)
            checked = y + n
            pct = f"{100*n/checked:.0f}%" if checked else "-"
            print(f"  {label[:46]:46} {cite[:26]:26} {y:>9} {n:>8} {pct:>7}")
        print()

    # ---------------- funnel ----------------
    outcomes = collections.Counter((s.get("outcome") or "session").strip().lower()
                                   for s in sessions)
    pilots = outcomes.get("pilot", 0) + outcomes.get("closed", 0)
    closed = outcomes.get("closed", 0)
    print("=" * 78)
    print("2. FUNNEL")
    print("=" * 78)
    for k, v in outcomes.most_common():
        print(f"  {k:12} {v}")
    print(f"  sessions {len(sessions)}  ->  pilots {pilots}  ->  closed {closed}")
    if pilots:
        print(f"  session -> pilot: {100*pilots/len(sessions):.0f}%   "
              f"pilot -> closed: {100*closed/pilots:.0f}%")

    # ---------------- price ----------------
    pays_today, ceilings, wtp_yes, wtp_no, wtp_unknown = [], [], 0, 0, 0
    for s in sessions:
        p = dollars(s.get("q5_pays_today"))
        if p:
            pays_today.append(p)
        c = dollars(s.get("q6_monthly_ceiling"))
        if c:
            ceilings.append(c)
        w = (s.get("would_pay_over_100") or "").strip().lower()
        wtp_yes += w == "y"
        wtp_no += w == "n"
        wtp_unknown += w == "unknown"
    print()
    print("=" * 78)
    print("3. PRICE EVIDENCE")
    print("=" * 78)
    if pays_today:
        pays_today.sort()
        med = pays_today[len(pays_today)//2]
        print(f"  what they pay today (monthly, fleet):  n={len(pays_today)}  "
              f"median ${med:,.0f}  range ${pays_today[0]:,.0f}-${pays_today[-1]:,.0f}")
    if ceilings:
        ceilings.sort()
        med = ceilings[len(ceilings)//2]
        print(f"  their own stated ceiling (monthly):     n={len(ceilings)}  "
              f"median ${med:,.0f}  range ${ceilings[0]:,.0f}-${ceilings[-1]:,.0f}")
    print(f"  would pay above $100/truck/month:  yes {wtp_yes} · no {wtp_no} · unknown {wtp_unknown}")

    # ---------------- gate decisions ----------------
    print()
    print("=" * 78)
    print("4. GATE DECISIONS  (thresholds were fixed in advance)")
    print("=" * 78)

    need_n, need_good = GATE_DEFECT
    if len(sessions) < need_n:
        print(f"  [ ] DEFECT RATE        not yet measurable - {len(sessions)}/{need_n} sessions run "
              f"(need {need_good} of {need_n} with a non-zero defect count)")
    else:
        ok = non_zero >= need_good
        print(f"  [{'x' if ok else ' '}] DEFECT RATE        {non_zero}/{len(sessions)} sessions "
              f"with a gap (need {need_good}/{need_n}) -> "
              f"{'THESIS HOLDS' if ok else 'THESIS IS WRONG - most fleets come back clean'}")

    if len(sessions) < 10:
        print(f"  [ ] WILLINGNESS TO PAY  not yet measurable - {len(sessions)}/10 sessions")
    else:
        ok = wtp_yes >= GATE_WTP
        print(f"  [{'x' if ok else ' '}] WILLINGNESS TO PAY  {wtp_yes}/10 will pay above $100 "
              f"(need {GATE_WTP}) -> "
              f"{'PRICE HOLDS' if ok else 'KILL CRITERION MET - rebuild as a $60-80 scale business'}")

    if len(sessions) < 4:
        print(f"  [ ] PILOT CONVERSION    not yet measurable - {len(sessions)} sessions")
    else:
        rate = pilots / len(sessions)
        ok = rate >= GATE_PILOT
        print(f"  [{'x' if ok else ' '}] PILOT CONVERSION    {100*rate:.0f}% of sessions became a "
              f"pilot (need {100*GATE_PILOT:.0f}%) -> {'on track' if ok else 'below threshold'}")
        if pilots:
            cr = closed / pilots
            ok2 = cr >= GATE_CLOSE
            print(f"  [{'x' if ok2 else ' '}] PILOT -> CONTRACT  {100*cr:.0f}% (need "
                  f"{100*GATE_CLOSE:.0f}%) -> {'on track' if ok2 else 'below threshold'}")

    # ---------------- csv ----------------
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    cols = (["_file", "session_date", "reviewer", "dot_number", "legal_name", "phy_city",
             "power_units", "total_drivers", "add_date", "outcome", "q1_authority",
             "q2_audit_known", "q3_who_touches_logs", "q4_last_event_cost", "q5_pays_today",
             "q6_monthly_ceiling", "referral_contact", "forwarded",
             "stated_number_unprompted", "would_pay_over_100", "notes"]
            + [f"cab_{k}" for k in sorted(cab_keys)]
            + [f"file_{k}" for k in sorted(file_keys)])
    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for s in sessions:
            row = {c: s.get(c, "") for c in cols if c in s}
            for k in cab_keys:
                row[f"cab_{k}"] = (s.get("cab") or {}).get(k, "")
            for k in file_keys:
                row[f"file_{k}"] = (s.get("file") or {}).get(k, "")
            w.writerow(row)
    print(f"\nWrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
