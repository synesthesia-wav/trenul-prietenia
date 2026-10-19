# HOS Health Check — Internal Build Guide

The single most important sales asset we have, because we have no publishable track record of our own. The report must be **impeccable, dated, and specific to the carrier**, and it must be the thing the owner can verify themselves without trusting us.

**Who produces it:** the person running the outbound motion. **Time to produce:** 25–30 minutes once the process is smooth; 45 minutes for the first ten. **Cost:** effectively free, and it is the reason a cold conversation is not a cold call.

**Success criteria:** the report is good enough that an owner forwards it to his dispatcher or his insurance agent. That forwarding is the whole point.

---

## 1. Sources — what to pull, from where

| # | Source | What you get | Access |
|---|---|---|---|
| 1 | **SAFER Company Snapshot** (safer.fmcsa.dot.gov) — search by USDOT | Legal name, SAFER tier, physical address, phone, power units, drivers, authority type, status, **out-of-service rate**, **24-month inspection counts by type** (driver / vehicle / hazmat) with violations per inspection, **24-month crash counts** (fatal, injury, towaway), and the **BASIC percentile rankings** currently displayed | Free, public, per-carrier |
| 2 | **SAFER Licensing & Insurance** (same DOT number) | Operating authority status (broker authority, factoring), insurance filings on record (cargo, liability, UM, workers comp) with dates | Free, public |
| 3 | **FMCSA Carrier Census / bulk registration data** (FMCSA data download) | Full carrier universe with power units, drivers, status, class, and 24-month inspection / OOS / crash and BASIC-violation counts | Free bulk download; use for **list building**, not for the report |
| 4 | **Current SMS Methodology** (FMCSA Safety Measurement System) | Definitions of the BASICs, percentile ranking, severity weights, how the percentiles are calculated | Free PDF; **re-download before each campaign** |
| 5 | **Third-party carrier-data API** (CarrierReports, ATLAS, CarrierAPI, or similar) | Automated pull + nicer violation breakdown | Paid; verify terms before using a carrier's data |
| 6 | **The carrier itself** (only after they engage) | ELD export, BOLs, rate cons, RODS, driver roster, authority documents | Under a signed authorization |

**Rules for sources 1–5:** everything in sections 1–3 of the report is public information the carrier can pull themselves. Say so on the report. That is what makes it credible.

---

## 2. How to read what SAFER gives you

**Do not hard-code any structure.** BASIC names, components, and percentile methodology have been revised more than once, and carriers themselves are confused about it. Read the labels off the current SAFER page and cite the methodology version you used.

**Percentile ranking:** FMCSA's percentile ranking runs **0 = best, 100 = worst**, computed against a peer group of similar carriers (size and type). Say this in plain language on the report, because owners routinely misread it. Practical reading: anything above roughly 80 is in the worse part of its peer group — treat that as a working heuristic, not an official threshold, and do not present it as FMCSA language.

**The denominator problem — this is the most important thing in the report.** For a 5–20 truck carrier, the inspection count over 24 months may be a single digit. A carrier with "zero violations" may simply have had two inspections. **Always show the denominator next to the numerator.** A report that says "0 violations" without "across N inspections" is worse than no report, because it teaches the owner the wrong lesson.

**The OOS rate** (out-of-service rate) is the share of inspections resulting in an out-of-service violation. State the carrier's figure and the pull date. If you compare it to a national average, pull that from FMCSA's own published data and date it, or leave it out.

**Inspections by type** (driver / vehicle / hazmat) with violations per inspection tells you something valuable and often overlooked: the ratio of vehicle violations to driver violations tells the owner where their actual exposure is. A fleet with clean driver records and repeated vehicle violations does not need an ELD service at all — it needs a maintenance program. **Saying that is a trust move, and it prevents us from selling the wrong thing.**

---

## 3. The eight-item paperwork checklist

This is the substance of the report — the part the owner cannot get anywhere else without hiring a consultant. Assess each item from public information and from what the carrier tells you; mark status as **Verified / Needs check / Unknown**.

1. **Driver certification of the record of duty status (395.8(e)(6)(i)).** Every driver certifies every day, including non-driving days. A missing certification is the most common RODS defect and it is free to fix.
2. **14 days of records available in the ELD before driving (395.8(b)(1)).** A driver returning from extended leave, or whose device was repaired, can be legally unable to drive. Pair this with a written check that drivers log off correctly at the end of a trip.
3. **Edits annotated and justified (395.8(e)(4)(ii)).** Every edit carries a reason; reconstruction is limited to the last 14 days and must rest on the driver's personal records and shipping papers. The ELD keeps the edit history permanently, and FMCSA can retrieve it.
4. **Duty status continuity.** No gaps, no overlapping duty periods, the 30-minute break (395.3(d)(3)) actually logged, and the 60/70-hour limit and 34-hour reset computed correctly.
5. **BOL / RODS reconciliation.** Pickup and delivery times on the rate con match the ELD, and the off-duty time between them is real. This is the single most common source of a "records do not reflect actual operation" finding.
6. **State and lane rules.** The state-specific rules for the lanes the fleet actually runs (for example: California 8/12-hour splits and the 34-hour reset; Texas 30-hour restart; short-haul exceptions). Rules differ by state and change; a fleet running in three states is running three rulebooks.
7. **Retention and production (395.8(j)).** Six-month retention, and the ability to produce the driver copy of the RODS for the last 14 days on demand, to law enforcement, within 48 hours. Retention only helps if the retrieval actually works.
8. **Roadside document readiness.** Medical card, license, registration and proof of insurance, correct ELD status (no unassigned driving time, no device malfunctions, correct time zone), and a printed or downloadable RODS available in the cab.

**Delivery:** as a one-page checklist the owner can hand to his dispatcher or his driver, marked up with what we found. It is the artifact most likely to be forwarded, so it must be usable on its own, without our cover note.

---

## 4. Writing the findings

**Maximum 5 findings**, ordered by severity. Three severity levels:

| Level | Meaning | Language |
|---|---|---|
| **1 — Act this week** | Will likely produce a violation or a citation at the next inspection | "This is the finding most likely to cost you a citation." |
| **2 — Act this month** | Will show as a deficiency and compounds over a cycle | "This will surface at the next audit." |
| **3 — Good practice** | Reduces future exposure, no current deficiency | "Not a problem today; it is what a strong record looks like." |

**One sentence per finding, in this form:** *what we found* → *why it matters (in money or risk terms, not rule citations)* → *what to do*.

> **Bad:** "Violation of 395.8(e)(6)(i) — certification missing on 3 of 47 RODS for driver J. Doe, week of 03/11."
> **Good:** "Three of your driver's logbooks for the week of March 11 are missing the driver's certification. At a roadside inspection an uncertified log is treated as no log — it becomes a violation in the driver's hand and counts against the carrier."

**Never** state or imply a legal conclusion, a fine amount, or a prediction of what an inspector will do. Say "is likely to produce a violation" and "is treated as," not "you will be fined $X."

---

## 5. QA before it goes out

- [ ] Every number pulled **today**; the pull date is on the report.
- [ ] The inspection denominator is shown next to the violation count.
- [ ] Every percentile matches the current SAFER page, and the plain-language reading is right.
- [ ] No number came from memory, a previous carrier's report, or a general rule of thumb.
- [ ] Findings are written for a business owner, not an auditor.
- [ ] The eight-item checklist is complete and marked.
- [ ] The disclaimer is in place (below).
- [ ] No competitor is named.
- [ ] If the record is clean, the report says so, and the checklist is still delivered.

---

## 6. Language that must not appear

- No legal advice, no legal conclusions, no predictions of fines or citations.
- No claim that we have prevented violations, or that we will.
- No outcome guarantee, no "zero violations" promise, no reference to the partners' prior 18-month record (it is under NDA and cannot be opened or quoted).
- No naming or disparaging a competitor, no naming a former employer.
- No claim that we edit, adjust, or reconstruct a driver's hours.
- No invented problem. If the record is clean, say it is clean.

---

## 7. The disclaimer (on every report)

> This report was prepared from the carrier's own public Federal Motor Carrier Safety Administration (FMCSA) records, retrieved on [date], and from information the carrier provided. It is a compliance review for operational purposes and is not legal advice. Public FMCSA records reflect inspections that have already occurred and do not predict future inspections or results. Percentile rankings are FMCSA's, calculated against a peer group of similar carriers under FMCSA's Safety Measurement System methodology current as of [methodology version/date].

---

## 8. Delivery and follow-up

- **Send the PDF within 30 minutes of the call, before you hang up.** Never "I'll email it later."
- **Subject line:** `[Carrier] HOS compliance review — your FMCSA record, [date]`
- **Cover note (4 lines, no more):** what we found, the two most urgent items, one question, and the two options (pilot / checklist only). No paragraph about us.
- **Follow-up cadence:** day 1 (send report, ask for 15 minutes), day 4 (one-line nudge, attach the checklist), day 14 (one case line or one relevant regulatory note, not a reminder), day 30 (close the loop politely and ask for the referral).
- **Log everything in the CRM:** DOT number, power units, state, ELD platform if known, findings count and levels, the objection, the exact next step with a date, and the source of the lead.

---

## 9. Volume

| Stage | Per week | Owner |
|---|---|---|
| Health Checks produced | 25–40 | outbound |
| Reports sent | 25–40 | outbound |
| 20-minute calls booked | 8–12 | outbound |
| Reports published on the site (anonymized) | 2 | marketing |

Reports are also the *insurance-agent* channel asset: an agent can send one of these to a carrier client as free loss prevention, and it costs them nothing. That is how the channel gets built — see `PLAN.md` §6.
