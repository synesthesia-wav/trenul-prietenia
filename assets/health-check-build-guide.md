# HOS Health Check — Internal Build Guide

The single most important sales asset we have, because we have no publishable track record of our own. The report must be **impeccable, dated, and specific to the carrier**, and it must be the thing the owner can verify themselves without trusting us.

**Who produces it:** the person running the outbound motion. **Time to produce:** 25–30 minutes once the process is smooth; 45 minutes for the first ten. **Cost:** effectively free, and it is the reason a cold conversation is not a cold call.

**Success criteria:** the report is good enough that an owner forwards it to his dispatcher or his insurance agent. That forwarding is the whole point.

> **REBUILT 2026-10-19 after Gate 0 research.** The earlier version of this guide led with BASIC percentiles. That is wrong for our target segment: FMCSA requires **at least three driver inspections with violations before a carrier is assigned a percentile above zero** in the HOS category, so for small fleets the percentile is frequently unassignable, and "0" is ambiguous between "excellent" and "we have no data." FMCSA is also reorganising BASICs into "compliance categories." **The report now leads with inspection counts, violation codes with severity weights, and the specific paperwork defects — and shows a percentile only when one exists.** A counts report is also simply more useful to an owner than a number. See `research/RESEARCH-LOG.md` §2.4 and §2.5.

---

## 1. Sources — what to pull, from where

| # | Source | What you get | Access |
|---|---|---|---|
| 1 | **SAFER Company Snapshot** (safer.fmcsa.dot.gov) — search by USDOT | Legal name, SAFER tier, physical address, phone, power units, drivers, authority type, status, **out-of-service rate**, **24-month inspection counts by type** (driver / vehicle / hazmat) with violations per inspection, **24-month crash counts** (fatal, injury, towaway), and the **percentile rankings currently displayed** | Free, public, per-carrier |
| 2 | **FMCSA SMS carrier profile** (ai.fmcsa.dot.gov/SMS/Carrier/<DOT>/Overview.aspx) | The **violation summary by code with counts, OOS counts, and SMS severity weights** — the single most valuable source. Also the "measure," the "safety event group," and the investigation results. This is where the actionable content is. | Free, public |
| 3 | **SMS Methodology** (csa.fmcsa.dot.gov/Documents/SMSMethodology.pdf) and **Appendix A violations list** (csa.fmcsa.dot.gov/documents/sms_appendixa_violationslist.xlsx) | Current definitions, severity weights 1–10, the 12-month data-sufficiency rules, time weighting, the 30-point per-inspection cap | Free. **Re-download before each campaign — the methodology has been revised and is being revised again.** |
| 4 | **SAFER Licensing & Insurance** | Operating authority status, insurance filings on record (cargo, liability, UM, workers comp) with dates | Free, public |
| 5 | **FMCSA Carrier Census / bulk registration data** (data.transportation.gov, "Motor Carrier Registrations – Census Files") | The full carrier universe with power units, drivers, status, class, and 24-month inspection / OOS / crash counts | Free bulk download; use for **list building**, not the report |
| 6 | **Third-party carrier-data API** (CarrierReports, ATLAS, CarrierAPI, or similar) | Automated pull + a cleaner violation breakdown | Paid; verify terms before using a carrier's data |
| 7 | **The carrier itself** (only after they engage) | ELD export, BOLs, rate cons, RODS, driver roster, authority documents | Under a signed authorization |

**Rules for sources 1–6:** everything in sections 1–4 of the report is public information the carrier can pull themselves. Say so on the report. That is what makes it credible.

---

## 2. How to read what FMCSA gives you

**Do not hard-code any structure.** BASICs are being reorganised into "compliance categories" (Controlled Substances/Alcohol and operating-while-OOS move into Unsafe Driving; HOS Compliance is unchanged). Names, components and percentile methodology have been revised more than once. Read the labels off the current pages and cite the methodology version you used.

**Percentile ranking:** FMCSA's ranking runs **0 = best, 100 = worst**, against a peer group of similar carriers. Say that plainly, because owners misread it constantly. Practical reading: above roughly 80 is in the worse part of its peer group — a working heuristic, not FMCSA language, and not to be presented as official.

**The denominator rules — these decide the report's design.**
- **A carrier needs at least three driver inspections with violations to be assigned a percentile above zero in the HOS category.** If they have fewer, there is no percentile. Report that fact, do not report "0."
- A carrier with no inspections in 24 months is **not** a clean record; it is an unexamined one. Say so. A carrier with "zero violations" across two inspections has told us almost nothing, and a report that implies otherwise teaches the owner the wrong lesson.
- **Always show the denominator next to the numerator.** Inspections, inspections-with-violations, and violations per inspection. This is the single most important habit in the whole report.

**The OOS rate** (out-of-service rate) is the share of inspections producing an out-of-service violation. State the carrier's figure and the pull date. Compare it to a benchmark only if you pull the benchmark from FMCSA's own published data and date it, or leave it out.

**Inspections by type** (driver / vehicle / hazmat) with violations per inspection tells the owner where their exposure actually is. The ratio of vehicle violations to driver violations is the tell: a fleet with clean driver records and repeated vehicle violations does not need an ELD service, it needs a maintenance program. **Saying that is a trust move and it stops us selling the wrong thing.**

---

## 3. The paperwork checklist, ordered by FMCSA's own violation data

This is the substance of the report — the part the owner cannot get anywhere else without hiring a consultant. Assess each item; mark **Verified / Needs check / Unknown**.

**Order matters, and the order comes from the data.** In live SMS profiles the documentation codes outnumber the driving codes by count, and the weight-5 paperwork codes are the ones small fleets trip repeatedly. Work down this list.

| Priority | Item | Code | SMS weight | Why |
|---|---|---|---|---|
| 1 | **Driver certification** — the driver reviews, corrects, and certifies the record, and certifies immediately after the final entry or correction for the 24-hour period | 395.30B1-ELDDFR, 395.30B1, 395.30B2-ELDDFC24 | 1 | Highest-frequency documentation code. Free to fix, and it is the first thing an inspector asks for. |
| 2 | **Form and manner** — the ELD is used correctly: correct status selections, correct entries, correct record structure | 395.24 | 1 | Same weight, similar frequency. |
| 3 | **Blank paper graph grids** — a supply of blank RODS grids for at least 8 days must be in the cab | 395.22H4-ELDBRODS | 1 | Trivially cheap to fix, routinely missing. |
| 4 | **Shipping document number and trailer number** entered or verified | 395.24C2III, 395.24C2II-ELDTN | 1 | The exact link between the log and the paperwork. |
| 5 | **Unassigned driving time** — every unidentified-driving record annotated or assigned to the right driver; retained 6 months; producible on inspection | 395.32(c), code 395.32B | **5** | Carrier's statutory duty. Recurring, mechanical, usually unowned. |
| 6 | **ELD malfunction handling** — driver notes the malfunction and gives the carrier written notice within 24 hours | 395.34A1-ELDDFN | **5** | A phone call and a form. |
| 7 | **Records not current** — the RODS is current to the last change of duty status | 395.8F01 | **5** | |
| 8 | **Records produced on request** — the driver can produce and transfer their records to an authorised safety official on demand | 395.24D-ELDPT | 3 | |
| 9 | **Retain and possess** — carrier retains RODS and supporting documents 6 months from receipt; driver has the previous 7 consecutive days in the cab | 395.8(k)(1), 395.8(k)(2) | 5 (395.8K2-HOSRC) | Two different obligations, often conflated. |
| 10 | **Submission window** — the driver submits the certified record to the carrier within 13 days of the 24-hour period | 395.8(a)(2)(ii) | — | Determines when a correction is even reviewable (395.30(d)(2)). |
| 11 | **Records available to the driver** — a driver must be able to access their own records; the carrier may not obstruct it | 395.36 | — | Often the thing that annoys drivers most, and often broken. |
| 12 | **State and lane rules** — the rules for the states the fleet runs in differ from each other and change | — | — | One fleet, three states, three rulebooks. |
| 13 | **Hours of service itself** — 11-hour, 14-hour, 30-minute break, 60/70-hour | 395.3 | 7 | The behaviour codes. Lowest count, highest weight. Coaching, not paperwork. |

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

> **Bad:** "Violation of 395.30(b)(1) — certification missing on 3 of 47 RODS for driver J. Doe, week of 03/11."
> **Good:** "Three of your driver's logbooks for the week of March 11 are missing the driver's certification. At a roadside inspection an uncertified log is treated as no log — it becomes a violation in the driver's hand and counts against the carrier."

**Never** state or imply a legal conclusion, a fine amount, or a prediction of what an inspector will do. Say "is likely to produce a violation" and "is treated as," not "you will be fined $X."

**Use the severity weight, but translate it.** "This is a weight-5 violation" means nothing to an owner. "This is the kind of finding that lands on your safety score and can put a driver out of service" means something.

---

## 5. QA before it goes out

- [ ] Every number pulled **today**; the pull date is on the report.
- [ ] The inspection denominator is shown next to the violation count, and where a percentile is unassignable, it says so.
- [ ] Every percentile matches the current SMS page, and the plain-language reading is right.
- [ ] Every violation code and severity weight is checked against the current SMS Appendix A, not from memory.
- [ ] No number came from memory, a previous carrier's report, or a general rule of thumb.
- [ ] Findings are written for a business owner, not an auditor.
- [ ] The checklist is complete, marked, and ordered by the data above.
- [ ] The disclaimer is in place (below).
- [ ] No competitor is named.
- [ ] If the record is clean, the report says so, and the checklist is still delivered.

---

## 6. Language that must not appear

- No legal advice, no legal conclusions, no predictions of fines or citations.
- No claim that we have prevented violations, or that we will.
- No outcome guarantee, no "zero violations" promise, and no reference to the partners' prior 18-month record (under NDA; it can be neither opened nor quoted).
- No naming or disparaging a competitor, no naming a former employer.
- No claim that we edit, adjust, or reconstruct a driver's hours.
- No invented problem. If the record is clean, say it is clean.

---

## 7. The disclaimer (on every report)

> This report was prepared from the carrier's own public Federal Motor Carrier Safety Administration (FMCSA) records, retrieved on [date], and from information the carrier provided. It is a compliance review for operational purposes and is not legal advice. Public FMCSA records reflect inspections that have already occurred and do not predict future inspections or results. Violation severity weights and percentile rankings are FMCSA's, calculated under FMCSA's Safety Measurement System methodology current as of [methodology version/date].

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
| Reports published on the site (anonymised) | 2 | marketing |

Reports are also the *insurance-agent* channel asset: an agent can send one of these to a carrier client as free loss prevention, and it costs them nothing. That is how the channel gets built — see `PLAN.md` §6.

**Note on the free layer:** FMCSA provides the Motor Carrier Safety Planner, free ELD carrier-and-driver training, and official guidance free. This is why the report must be about *their specific record* and *their specific paperwork*, and why we must not sell training or generic advice — that is free, and competing with it destroys both margin and credibility.
