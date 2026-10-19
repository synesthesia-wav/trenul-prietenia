# HOS COMPLIANCE REVIEW — CUSTOMER-FACING TEMPLATE

> **How to use this file.** Everything in `{{ }}` is a placeholder. Section headings and the order are fixed — the report must fit on **one page**, with the checklist as a separate second page (which it should be, so it can be forwarded on its own). Delete this instruction block before sending. See `health-check-build-guide.md` for sources, computation rules, and QA.
>
> **Note on percentiles:** only include the percentile block **if a percentile is assignable**. FMCSA requires at least three driver inspections with violations before a percentile above zero is assigned in the HOS category. For a small fleet there often is no percentile. If there is not, delete the block and replace it with the "not enough data to score" line. **Never report a percentile of 0 for a carrier who has not been scored.**

---

## PAGE 1

```
{{CARRIER LEGAL NAME}}
USDOT {{DOT_NUMBER}} · {{CITY, STATE}} · {{POWER_UNITS}} power units · {{DRIVER_COUNT}} drivers
Prepared {{DATE}} · Data source: FMCSA public records, retrieved {{PULL_DATE}}

────────────────────────────────────────────────────────────
AT A GLANCE
────────────────────────────────────────────────────────────
Authority status:        {{ACTIVE / SUSPENDED / INACTIVE}} ({{AUTHORITY_TYPE}})
Out-of-service rate:     {{X.XX}}% ({{N}} inspections, 24 months, retrieved {{PULL_DATE}})
24-month inspections:    {{N}} total — {{N_driver}} driver, {{N_vehicle}} vehicle
24-month violations:     {{N}} total ({{N_driver}} driver, {{N_vehicle}} vehicle)
Crashes (24 months):     {{N_fatal}} fatal · {{N_injury}} injury · {{N_towaway}} towaway

────────────────────────────────────────────────────────────
HOW MUCH OF YOUR RECORD WE COULD ACTUALLY SEE
────────────────────────────────────────────────────────────
Driver inspections in 24 months:        {{N}}
  of which resulted in a violation:    {{N}}
Violations per driver inspection:       {{N.N}}
{{IF N_driver_with_violations < 3:
  FMCSA does not assign a safety percentile to a carrier until it has
  at least three driver inspections with violations. You have {{N}},
  so there is no score for you — not a good one, not a bad one.
  No score means your record is largely unexamined, which is a
  different problem from a poor one, and it is the one you can fix
  this month.}}
{{ELSE:
  Safety percentile, Hours of Service:  {{P}}/100
  (FMCSA ranks 0 as best and 100 as worst, against carriers of
  similar size and type)                {{PLAIN READING}}}}

────────────────────────────────────────────────────────────
WHAT IS IN YOUR VIOLATIONS
────────────────────────────────────────────────────────────
{{N}} violations in 24 months. Grouped by what they actually are,
because most of them are paperwork, not driving.

  Paperwork and certification                    {{N}} violations
    - Log not certified by the driver             {{N}}
    - Form and manner of the ELD record           {{N}}
    - Shipping document / trailer number missing  {{N}}
    - No blank log grids in the cab                {{N}}
    - Records not produced on request              {{N}}

  Records the carrier must manage                  {{N}} violations
    - Unassigned driving time not explained        {{N}}
    - ELD malfunction not reported within 24h      {{N}}
    - Logbook not current                         {{N}}
    - Seven days of logs not kept in the cab       {{N}}

  Hours of service                                  {{N}} violations
    - Beyond 11 hours / 14-hour window / break     {{N}}

  (Weights in brackets are FMCSA's own severity weights. A weight of
   1 is a paperwork error. A weight of 5 or 7 is the kind of finding
   that lands on your safety score and can put a driver out of
   service for the rest of the day.)

────────────────────────────────────────────────────────────
WHAT WE FOUND ({{N}} items)
────────────────────────────────────────────────────────────

1. [ACT THIS WEEK] {{One-sentence finding: what we found.}}
   Why it matters: {{in risk or money terms, no rule citations}}
   Do this: {{the specific action}}

2. [ACT THIS WEEK] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

3. [ACT THIS MONTH] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

4. [GOOD PRACTICE] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

────────────────────────────────────────────────────────────
TWO THINGS TO DO THIS WEEK
────────────────────────────────────────────────────────────
1. {{the single highest-value action}}
2. {{the second}}

────────────────────────────────────────────────────────────
NEXT
────────────────────────────────────────────────────────────
{{ONE QUESTION — e.g. "Do you know who signs the certification
when a driver is on vacation?"}}

Two options:
  a) A 90-day pilot on 5–10 trucks: we handle the paperwork, the
     driver questions and the correction files, business hours, flat
     fee, credited in full against the contract.
  b) Just the paperwork checklist on the next page, and we talk
     in a month if it is useful.

{{PHONE}} · {{EMAIL}}
```

---

## PAGE 2 — the checklist (separate, so it can be forwarded on its own)

```
PAPERWORK CHECKLIST
{{CARRIER LEGAL NAME}} · prepared {{DATE}} · in the order that matters

1. Driver certification
   The driver reviews, corrects and certifies the record, and certifies
   again right after the last change of the day. An uncertified log is
   treated as no log.
   Status: {{VERIFIED / NEEDS CHECK / UNKNOWN}}

2. Form and manner
   Correct status selections, correct entries, correct record structure.
   Status: {{...}}

3. Blank log grids in the cab
   A supply of blank paper graph grids for at least 8 days.
   Status: {{...}}

4. Shipping document and trailer number
   The number on the paperwork is entered or verified in the log.
   Status: {{...}}

5. Unassigned driving time
   Every record of driving with no driver assigned is either explained
   or assigned to the right driver. Kept 6 months, produced on request.
   Status: {{...}}

6. ELD malfunctions
   The driver notes the fault and the carrier gets written notice
   within 24 hours.
   Status: {{...}}

7. Records current
   The log is up to date to the last change of duty status.
   Status: {{...}}

8. Records on request
   The driver can produce and hand over their records to an inspector
   on demand.
   Status: {{...}}

9. Retain and possess
   You keep the records 6 months. The driver keeps the last 7 days in
   the cab, available for inspection while on duty.
   Status: {{...}}

10. Submission
   The driver hands the certified record to you within 13 days.
   Status: {{...}}

11. Driver access
   Drivers can get their own records without having to ask you first.
   Status: {{...}}

12. State rules
   The rules for each state you run in, and any that changed recently.
   Status: {{...}}

13. Hours of service
   11 hours driving, 14-hour window, 30-minute break, 60/70 hours.
   Status: {{...}}

Prepared from FMCSA public records and information provided by the carrier.
Not legal advice. {{PHONE}} · {{EMAIL}}
```

---

## SAMPLE (fictional carrier, for training only — delete before use)

```
MIDWAY HAULING LLC
USDOT 0000000 · Houston, TX · 14 power units · 11 drivers
Prepared Mar 14 · Data source: FMCSA public records, retrieved Mar 14

AT A GLANCE
Authority status:        ACTIVE (Property)
Out-of-service rate:     8.33% (12 inspections, 24 months, retrieved Mar 14)
24-month inspections:    12 total — 9 driver, 3 vehicle
24-month violations:     3 total (3 driver, 0 vehicle)
Crashes (24 months):     0 fatal · 1 injury · 0 towaway

HOW MUCH OF YOUR RECORD WE COULD ACTUALLY SEE
Driver inspections in 24 months:        9
  of which resulted in a violation:    3
Violations per driver inspection:       0.33
FMCSA does not assign a safety percentile to a carrier until it has
at least three driver inspections with violations. You have 3, so there
is no score for you — not a good one, not a bad one. No score means
your record is largely unexamined, which is a different problem from a
poor one, and it is the one you can fix this month.

WHAT IS IN YOUR VIOLATIONS
3 violations in 24 months.

  Paperwork and certification                     2 violations
    - Log not certified by the driver              1
    - Form and manner of the ELD record            1

  Records the carrier must manage                  1 violation
    - Unassigned driving time not explained         1

  Hours of service                                 0 violations

  (Weights in brackets are FMCSA's own severity weights. A weight of
   1 is a paperwork error. A weight of 5 or 7 is the kind of finding
   that lands on your safety score and can put a driver out of
   service for the rest of the day.)

WHAT WE FOUND (4 items)

1. [ACT THIS WEEK] 11 of your 14 trucks show at least one hours-of-service
   violation in the last 24 months, and 3 of those are out-of-service
   violations.
   Why it matters: an hours violation on a driver's record is counted
   against the carrier, and the 3 out-of-service results are what your
   insurance renewal is priced on.
   Do this: we will pull the 3 drivers' records and show you exactly which
   days and which rule — most of these are paperwork defects, not driving
   problems.

2. [ACT THIS WEEK] 4 drivers' logbooks are missing the driver's certification.
   Why it matters: at a roadside inspection an uncertified log is treated
   as no log, which turns a paperwork gap into a violation in the driver's
   hand.
   Do this: a one-page daily certification reminder for your drivers.

3. [ACT THIS MONTH] You have 3 records of driving with no driver assigned,
   and nothing in your file explains them.
   Why it matters: this is your obligation, not your driver's, and it is
   the kind of finding that turns into a question you cannot answer at
   the roadside.
   Do this: pull the last 90 days of unidentified driving and either
   explain the time or assign it to the right driver.

4. [GOOD PRACTICE] Your vehicle maintenance record is in the best part of
   your peer group, and the driver files we can see are current.
   Why it matters: this is the part most small fleets lose, and you have
   not. It also means your risk is concentrated in hours and paperwork,
   not in the truck — so this is a narrow problem, not a broad one.

TWO THINGS TO DO THIS WEEK
1. Let us pull the 3 out-of-service violations and show you the cause of each.
2. Check that 4 drivers are certifying their logbooks every day.

NEXT
Do you know who signs the certification when a driver is on vacation?

  a) A 90-day pilot on 5–10 trucks: we handle the paperwork, the driver
     questions and the correction files, business hours, flat fee, credited
     in full against the contract.
  b) Just the paperwork checklist on the next page, and we talk in a month
     if it is useful.
```

---

## CHECKLIST OF THINGS THAT MUST NOT BE IN THE TEMPLATE

- Any fine amount, legal conclusion, or prediction of an inspection outcome.
- Any reference to the partners' prior 18-month record (under NDA).
- Any competitor name.
- Any claim that we edit, adjust, or reconstruct hours.
- Any percentile or benchmark not pulled today, and any percentile shown for a carrier who does not have one assigned.
- Any number without a denominator beside it.
