# HOS COMPLIANCE REVIEW — CUSTOMER-FACING TEMPLATE

> **How to use this file.** Everything in `{{ }}` is a placeholder. Section headings and the order are fixed — the report must fit on **one page** (or two if the checklist is a separate page, which it should be). Delete this instruction block before sending. See `health-check-build-guide.md` for sources, computation rules, and QA.

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
SAFETY PERCENTILE RANKINGS (FMCSA)
────────────────────────────────────────────────────────────
0 = best, 100 = worst. Calculated against a peer group of similar
carriers. FMCSA methodology current as of {{VERSION/DATE}}.

  Unsafe Driving ................ {{P1}}/100   {{PLAIN READING}}
  HOS Compliance ................ {{P2}}/100   {{PLAIN READING}}
  Vehicle Maintenance ........... {{P3}}/100   {{PLAIN READING}}
  Driver Fitness ................ {{P4}}/100   {{PLAIN READING}}
  Controlled Substances/Alcohol . {{P5}}/100   {{PLAIN READING}}

────────────────────────────────────────────────────────────
WHAT WE FOUND ({{N}} items)
────────────────────────────────────────────────────────────

1. [ACT THIS WEEK] {{One-sentence finding: what we found.}}
   Why it matters: {{in risk or money terms, no rule citations}}
   Do this: {{the specific action}}

2. [ACT THIS MONTH] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

3. [ACT THIS MONTH] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

4. [GOOD PRACTICE] {{...}}
   Why it matters: {{...}}
   Do this: {{...}}

5. [GOOD PRACTICE] {{...}}
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
  a) A 90-day pilot on 5–10 trucks: we handle the paperwork,
     the driver questions and the correction files, business hours,
     flat fee, credited in full against the contract.
  b) Just the paperwork checklist on the next page, and we talk
     in a month if it is useful.

{{PHONE}} · {{EMAIL}}
```

---

## PAGE 2 — the checklist (separate, so it can be forwarded on its own)

```
PAPERWORK CHECKLIST
{{CARRIER LEGAL NAME}} · prepared {{DATE}} · all 8 items

1. Driver certification of the logbook
   Every driver signs the certification for every day, including
   days off. An unsigned log is treated as no log.
   Status: {{VERIFIED / NEEDS CHECK / UNKNOWN}}

2. 14 days of records available before driving
   A driver with fewer than 14 days of records in the ELD cannot
   drive. Watch drivers returning from leave or after a device repair.
   Status: {{...}}

3. Edits annotated and justified
   Every edit needs a reason. Reconstructing past records is limited
   to 14 days and must rest on the driver's own records and shipping
   papers. The device keeps the edit history permanently.
   Status: {{...}}

4. Duty status continuity
   No gaps, no overlapping duty periods, the 30-minute break logged,
   and the 60/70-hour limit and 34-hour reset calculated correctly.
   Status: {{...}}

5. Logbook reconciled to the bill of lading
   Pickup and delivery times on the rate con match the ELD, and the
   time between them is real. This is the most common reason a record
   is said not to reflect actual operations.
   Status: {{...}}

6. State and lane rules
   The rules for the states you run in differ from each other and
   change. One fleet, three states, three rulebooks.
   Status: {{...}}

7. Retention and production
   Six-month retention, and the ability to produce the last 14 days of
   logbooks on demand, to law enforcement, within 48 hours. Retention
   only helps if the retrieval works.
   Status: {{...}}

8. Roadside document readiness
   Medical card, license, registration and insurance, correct ELD
   status, and logbooks available in the cab.
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

SAFETY PERCENTILE RANKINGS (FMCSA)
0 = best, 100 = worst. Calculated against a peer group of similar carriers.
FMCSA methodology current as of {{VERSION/DATE}}.

  Unsafe Driving ................ 42/100   Better than most peers your size
  HOS Compliance ................ 88/100   In the worse part of your peer group
  Vehicle Maintenance ........... 11/100   Among the better
  Driver Fitness ................ 35/100   Better than most
  Controlled Substances/Alcohol . 0/100    No violations of this type

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

3. [ACT THIS MONTH] Your records are stored and produced by the ELD only.
   Why it matters: if an officer asks for the last 14 days of logbooks and
   the retrieval is not instant, the inspection goes badly regardless of
   how clean the driving was.
   Do this: test the retrieval once this month, on a truck you do not
   need.

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
- Any percentile or benchmark not pulled today.
