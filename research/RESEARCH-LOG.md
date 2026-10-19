# Research Log — ELD Managed Compliance

Every claim, with source grade, pull date, and what it changed.

**Grades:** A = primary regulatory text or official data · B = contemporaneous trade press or named-party documents · C = vendor marketing or unattributed · D = forum/social anecdote.
**Rule applied:** only A and B go into customer-facing material. Every number carries unit, geography, as-of date, sample.

Sprint window: 2026-10-19. Raw pulls in `raw/2026-10-19/`.

---

## Section 1 — Legal foundation (Gate 0.5)

### 1.1 ⚠️ CORRECTION — 395.8(e)(4)(ii) does not exist in the current CFR

**Claim:** `49 CFR 395.8(e)(4)(ii)` is cited across `PLAN.md`, `RISKS.md` and `assets/hos-rods-reconciliation-checklist.md` as the operative rule on log correction and 14-day reconstruction. **It does not exist in the current Code of Federal Regulations.**

**Source (A):** current 49 CFR 395.8, eCFR (up to date as of 2026-10-15; title last amended 2026-10-13), read in full at https://www.ecfr.gov/current/title-49/part-395/section-395.8 and cross-read at Cornell LII. Paragraph (e) contains only (e)(1), (e)(2), (e)(3). Paragraph (b)(1) is the duty-status category list, not a 14-day rule.

**What changed:** every citation to 395.8(e)(4)(ii) is replaced with the anchors actually verified in Section 1.2. The "14-day reconstruction" framing is withdrawn entirely — it was based on a pre-2016 rule structure.

**Status:** corrected in all venture documents.

---

### 1.2 The real operative rules (Grade A)

All from current 49 CFR Part 395, read in full 2026-10-19.

| Provision | Substance | Why it matters to us |
|---|---|---|
| **395.30(d)(1)** | "On review of a driver's submitted records, the motor carrier may request edits to a driver's records of duty status to ensure accuracy. A driver must confirm or reject any proposed change, implement the appropriate edits on the driver's record of duty status, and recertify and resubmit the records in order for any motor carrier-proposed changes to take effect." | **The regulation expressly contemplates a third party proposing edits with driver confirmation.** Our model is not a workaround; it is the sanctioned workflow. |
| **395.30(d)(2)** | Carrier may not request edits before the driver has submitted the records. | Timing rule: corrections are a review of *submitted* records, not real-time remote steering. |
| **395.30(d)(3)** | "Edits requested by any system or by any person other than the driver must require the driver's electronic confirmation or rejection." | Direct statutory basis for our service existing at all. |
| **395.30(c)(2)** | The driver or support personnel must annotate each change or addition. | Every correction needs a written reason attached. |
| **395.30(e)** | Carrier may not coerce a driver to make a false certification. | Asks the driver a question, never instructs one. |
| **395.30(f)** | Carrier must not alter or erase original information, source data streams, or information in any ELD that uses the original information. | The original record is untouchable. Any change is additive. |
| **395.8(f)(2)** | "Entries made by driver only. All entries relating to a driver's duty status must be legible and made by the driver." | Core of "we do not touch the ELD." |
| **395.8(e)(1)** | No driver or motor carrier may make a false report in connection with a duty status. | The criminal anchor. |
| **395.8(a)(2)(ii)** | Driver must submit the certified RODS to the carrier within **13 days** of the 24-hour period. | Our correction window is 13 days, not 14. |
| **395.8(k)(1)** | Carrier must retain RODS and supporting documents **not less than 6 months** from receipt. | Retention obligation we serve. |
| **395.8(k)(2)** | Driver must retain a copy of each RODS for the previous **7 consecutive days**, in possession and available for inspection while on duty. | The in-cab document rule. |
| **395.22(b)(1)** | Applies to "the motor carrier's support personnel who have been authorized by the motor carrier to access ELD records and make or suggest authorized edits." | Establishes a legally recognised role we can be contracted into. |
| **395.22(d)** | Support personnel account requires the individual's name from government-issued ID and a unique username. | **Operational:** named accounts per operator, or operate under the carrier's own account. |
| **395.22(e)** | Proper log-in required for drivers and support personnel. | No shared logins. |
| **395.32(c)** | Carrier must ensure records of unidentified driving are reviewed and either annotated (explaining why the time is unassigned) or assigned to the correct driver. Retain 6 months; produce on inspection. | A discrete, high-frequency, currently-underserved task with a named regulation. |
| **395.36** | Driver must be able to access their own ELD records; carrier must not force a driver through the carrier to get copies. | Our service may not create a process that obstructs driver access. |
| **Appendix A 4.3.2.8(b)** | ELD must not permit alteration or erasure of the original information collected, or of the source data streams. | Device-level guarantee behind Rule 1. |
| **Appendix A 4.3.2.8.2(b)** | An ELD must not allow automatically recorded driving time to be shortened, except in stated circumstances. | **The device itself blocks the classic "shorten the driving time" evasion.** |
| **Appendix A 4.3.3** | Motor carrier entries are restricted to authenticated "support personnel" account holders. | Access-control basis. |

**FMCSA guidance (A):** "Editing and Annotations" (fmcsa.dot.gov/hours-service/elds/editing-and-annotations), read 2026-10-19:
- Q4: "Both the driver and authorized carrier staff can make limited edits to an ELD record to correct mistakes or add missing information. All edits must include a note (annotation) to explain the reason for the edit. In addition, the driver must confirm (certify) that any carrier edit is accurate, and resubmit the records."
- Q5: if the driver is unavailable or unwilling to recertify, the carrier's proposed edit and annotation remain part of the record. **Risk to disclose.**
- Q6: original records are retained alongside edits; driver access limited to the six-month retention period.
- Q7: "Can a user edit or change driving time that has been recorded by an ELD to non-driving time? No."

**FMCSA ELD Accounts FAQ (A):** support personnel accounts are for those "authorized by the motor carrier to create, remove, and manage user accounts; configure allowed ELD parameters; and access, review, and manage drivers' ELD records on behalf of the motor carrier."

**What changed:** the product design in `PLAN.md` §2 was **confirmed and strengthened**, but the citation was wrong. `PLAN.md` §2 is rewritten around 395.30(d). The 13-day window replaces 14. The seven-day in-cab rule replaces 14. 395.32(c) unidentified driving is added as a service line. The "we do not touch the ELD" rule is now anchored in 395.8(f)(2), 395.30(f) and Appendix A 4.3.2.8(b) rather than a repealed paragraph.

**New risk surfaced:** FMCSA FAQ Q5 — an unconfirmed proposed edit stays in the record. We must design so that a rejected or ignored edit is harmless, because the carrier may not be able to remove it.

---

### 1.3 ⚠️ UNVERIFIED — two citations could not be confirmed

Recorded so they are not carried forward on my word.

| Claim in earlier drafts | Status |
|---|---|
| "14 calendar days of records must be available in the ELD before driving" (cited to 395.8(b)(1)) | **Not found in current 395.8.** Current (b)(1) is the duty-status category list. The 14-day availability requirement exists in FMCSA guidance and in pre-2016 CFR text, but I could not locate its current paragraph. **Do not cite a paragraph number. Confirm with counsel and cite the guidance.** |
| 395.3(e)(4)(ii) driver out-of-service criterion | Text not cleanly retrieved. Confirmed only that the section exists and that 395.8(e)(1) false report and 395.8(a) RODS violations carry OOS consequences in SMS data. **Confirm before use.** |

**What changed:** both removed from customer-facing and attorney-facing drafts until verified. A verification task added to the Gate 0 exit checklist.

---

### 1.4 Enforcement history — the risk and the pitch (Grades A/B)

Federal prosecutions of falsified hours-of-service records, DOT Office of Inspector General and federal court records, pulled 2026-10-19:

| Case | Year | Facts | Outcome |
|---|---|---|---|
| **US v. Sisic**, D.R.I., Crim. No. 20-63 (18 USC 371 conspiracy to falsify records) | 2020 | Owner of an 11-tractor Rhode Island carrier altered thousands of ELD entries for ~20 drivers to conceal driving and on-duty time, using the carrier's own Omnitracs system. One driver died in an April 2018 crash. | Pleaded guilty. 18 months; $50,000 fine. Company defunct. |
| **US v. Belovs**, E.D. Pa. | 2012 | 15 false-statement counts. Falsified FMCSA logbooks to conceal driving beyond lawful hours; fatal crash, one killed, five injured. | 18 months; 36 months supervised release; $2,500 fines. |
| **US v. McClafferty**, E.D. Pa. | 2003 | Pleaded guilty to 10 counts of falsifying HOS logs; 6 other drivers, the dispatcher and the company were indicted. | Guilty plea. |
| Nijjar Brothers Trucking (Madera, CA) | 2006 | 13 drivers pleaded guilty to false logbooks. | 4 sentenced: 15 months, 3 months, 3 months, 135 days. |
| Virginia carriers and executives | 2017 | 126-count indictment: conspiracy, falsifying records, false statements, **wire fraud**, wire fraud conspiracy. | Indictment. |
| DOT OIG "Truck drivers charged with lying to DOT about required rest time" (oig.dot.gov/hos1.pdf) | — | Indictments of drivers, one dispatcher and one trucking company on 18 USC 1001, alleging systematic falsification of daily logbooks to exceed lawful driving and on-duty hours. | Multiple prosecutions; OIG notes seven prior trucker cases. |

**What changed, and this is the most important finding in the research:**
1. **Sisic is our exact target customer.** 11 tractors. 7–10 drivers. A small fleet whose owner did the falsification himself. This is not a story about criminals; it is a story about a small carrier owner with an ELD and no compliance function, which is the precise profile of the fleets we intend to sell to. It is the strongest possible evidence that the problem is real and that the current "solution" is to lie.
2. **The criminal exposure lands on the carrier owner, not on us** — *provided* we do not alter the record. Every case above involved the owner or driver editing the record. If we prepare corrections and the driver confirms, the falsifying act is the carrier's, not ours.
3. It supplies the **pitch**: the alternative to paying for a service is that your company does it itself and you go to prison, lose the company, and void the insurance. That is a far stronger sales argument than any dollar value-stack.
4. Note the **wire fraud** count in the Virginia case. If a vendor is paid to produce false records, that is a fraud claim on us and the carrier. It is the legal reason our "documented, source-backed corrections" standard is not optional.

**Honest limitation:** none of these cases involves a *vendor* being prosecuted for selling falsification. That is consistent with the low visibility of this market, not evidence of legal safety. The vendor exposure is real but untested; our Rule 2 refusal log is the defence.

### 1.5 The criminal and regulatory penalties, verified (Grade A)

Pulled 2026-10-19 from Cornell LII (uscode) and eCFR.

| Provision | Substance |
|---|---|
| **49 U.S.C. § 521(h)** | "Any person who knowingly and willfully violates any provision of subchapter III of chapter 311 (except sections 31138 and 31139) or section 31502 of this title, or a regulation issued under any of those provisions shall, upon conviction, be subject for each offense to a fine not to exceed $25,000 or imprisonment for a term not to exceed one year" — **doubled for a subsequent offense.** |
| **49 U.S.C. § 521(a)** | Civil penalty up to $10,000 per offense for violations of § 31502 and its regulations. |
| **49 U.S.C. § 521(b)** | Recordkeeping and reporting violations: up to $1,000 per offense, each day a separate offence, capped at $10,000 for all offences related to a single violation. |
| **49 U.S.C. § 521(b)(ii)** | Knowingly falsifying, destroying, mutilating or changing a required report or record: up to $10,000 per violation, where the action misrepresents a fact constituting a violation other than a reporting or recordkeeping violation. |
| **49 CFR 386, Appendix B** (penalty schedule) | Recordkeeping: max civil penalty $1,584 per day, up to $15,846. Knowing falsification of records: max civil penalty $15,846. |
| **49 CFR Part 385, Appendix B** (safety rating) | § 390.35 — "Making, or causing to make fraudulent or intentionally false statements or records and/or reproducing fraudulent records" — is rated **acute**, not merely critical. An acute violation can produce an unsatisfactory safety rating on its own, independently of frequency. |
| **18 U.S.C. § 1001** | The charging statute in every DOT OIG prosecution of falsified hours-of-service logs. |

**Correction to earlier drafts:** these documents cited "49 U.S.C. § 5215" for the criminal penalty. **The correct provision is § 521(h).** The "acute" rating for fraudulent records is also sharper than the "critical" characterisation used earlier, and is the more persuasive fact for a carrier owner: a single acute violation is enough to sink the safety rating.

**What changed:** the penalty framework in `RISKS.md` §1 and the attorney packet is now cited correctly and more strongly. The acute rating under 385 Appendix B is a better argument than a fine schedule, because it is about the carrier's operating authority, which is the thing an owner actually fears losing.

---

## Section 2 — Market and price (Gates 0.2, 0.3, 0.4)

### 2.1 ⚠️ THE PRICE IS THE PROBLEM — $130/truck/month sits 2x above the automation tier

Published US prices, all read directly from vendor pricing pages on 2026-10-19. Normalised to USD per truck per month.

| Provider | What it is | Published price | Normalised /truck/mo | Grade |
|---|---|---|---|---|
| **Trucking Hub** | Complete DOT compliance incl. ELD compliance + nationwide random drug testing, 24,000+ locations | $29/month **per truck** (press release, Aug 2025) | **$29** | B |
| **Trucking Comply** | Managed compliance: DQ files, drug & alcohol pool, renewals; "run by humans who actually know carrier operations" | From **$25 a unit, a month** | **$25** | C |
| **TruckingMBA** | Beyond Compliance $50/mo: automated FMCSA filing reminders, DQ file audits, **HOS compliance review**, insurance certificate tracking, email & chat support. Complete Compliance $65/mo: adds dedicated compliance manager, DOT audit prep + mock audits, CSA score monitoring + improvement plan, quarterly reports, **phone support with same-day response**. Pricing by truck count: 1 truck $50; 2–5 +$10 each; 6–10 +$7 each. | **$50–65 per truck/mo** | **$50–65** | C |
| **TenFour** | Flat tiers, every price published, no quote: Solo $99 (1 truck), Small Fleet $159 (2–3), Fleet $229 (4–6) — "about $38 a driver at six trucks". Includes compliance monitoring, DQ files, drug program, CSA monitoring, human review, unlimited text/email questions. | $99–229 flat | **$38–99** | C |
| **Lili Safety** | Owner-Op $199/mo (1 driver + PU); Small Fleet Managed $499 (≤5); Growth Fleet $899 (≤15); Outsourced Safety Department $1,499 (≤30). Includes weekly CSA/SMS KPI summary, expanded ELD/HOS review, weekly management reporting. | $199–1,499 flat | **$50–100** | C |
| **Fleet Regulators** cost index | "Ongoing compliance management — per-truck monthly scope (roughly 50 to 150 dollars per truck per month per our cost guide)" | $50–150 | **$50–150** | C |
| **Moving Authority** | Full-service packages including audits, training, records management | $100–250 **per driver per month**; basic $50–100 | **$50–250** (driver-based) | C |
| **Prime Fleet Management** ⭐ | **The closest true comparable.** A named "HOS Specialist" doing daily ELD monitoring inside the carrier's Samsara or Motive account, HOS violations flagged before they become citations, **logbook review and correction**, direct driver coaching on HOS, roadside inspection data review. Plus a Compliance Manager, Safety Specialist, Admin, monthly report, quarterly review, annual mock audit, regulatory alerts. Free DOT assessment as lead magnet. | "Starting at $500/month"; **"Most fleets in our 6–25 truck range invest $1,500–$6,000/month"**; in-house equivalent quoted at $180,000–$350,000+/yr | **~$60–250** (6 trucks @ $1,500 = $250; 25 @ $6,000 = $240) | C |
| **Turbo ELD** ⭐ | **The real offshore anchor.** ELD monitoring from **$2/day per truck**; real-time log monitoring, auto-certify logbooks, 24/7 support, weekly performance/violation reports, 500+ audits passed, 100+ employees, 7+ years, 500+ clients, **support in English, Russian, Uzbek and Arabic** | $2/day = $60/mo; $80/mo ≈ $2.67/day | **$60–80** | C |

**Also confirmed:** ELD platform software itself runs **$15–60 per truck per month** (FleetOpsClub $15–50; technbrains $20–60; Motive ~$40). A carrier already pays $25–50/truck/mo for the platform before paying us.

**Disconfirming pass (mandatory, run):** searched specifically for evidence that higher-priced managed compliance delivers measurably better outcomes, and for any published effect size. **Null result: no citable study of outcome effect size for outsourced ELD/log compliance services was found.** The only quantitative claim located is a vendor calculator's internal assumption (ZenduELD) that clearing an unverified log "removes roughly 70% of its violation risk" — grade C, a model assumption, not evidence. **Consequence: we may not promise violation reduction. Process and documentation outcomes only.** This reinforces the existing no-outcome-guarantee rule.

**What changed — the central strategic finding:**
- **$130/truck/month is roughly 2x the automation tier** ($25–65) and **2.2x the true offshore anchor** ($60–80). It is *inside* the staffed-HOS band (Prime Fleet, $60–250).
- **We cannot sell against TruckingMBA ($65, includes HOS compliance review) or Trucking Hub ($29).** They are cheaper and their scope is broader.
- **We can sell against the $60–80 offshore tier and against Prime Fleet.** Against Turbo ELD we must beat a firm with 100+ employees, 500+ clients, 7 years and *already native Arabic, Uzbek, Russian and English*. **The partners' "no Arabic" constraint removes the single most obvious differentiator against the incumbent.**
- **The defensible position is the middle band: above filing automation, below a full outsourced compliance department, with 24/7 driver response and a document-backed correction file.** That is a narrower and more specific position than the current documents assume, and it requires re-tiering the price and the segment.
- **Prime Fleet proves the category exists, defines our product in their own words, and has already built the same free-assessment lead magnet.** It is the benchmark to beat on substance.

**Also confirmed:** ELD platform software itself runs **$15–60 per truck per month** (FleetOpsClub $15–50; technbrains $20–60; Motive ~$40). A carrier already pays $25–50/truck/mo for the platform before paying us.

### 2.2 Market size (Gate 0.2) — PASS

Source: FMCSA Pocket Guide 2024 (published 2025-09), via secondary citation (maxdispatchservice.com, grade C) — **primary PDF not yet read directly.**

- 787,189 active carriers (Dec 2023), down from 813,844 in 2022 — **the market is contracting ~3%/yr**; ~10,000 carriers exited in 1H 2024.
- By fleet size: 1 truck 418,526 (53.1%); 2 trucks 123,353 (15.7%); 3–10 trucks 168,507 (21.4%); 11–100 trucks 56,715 (7.2%); >100 trucks 5,062 (0.64%).
- **Derived 5–75 power-unit band ≈ 160,000–195,000 carriers** (derivation in `raw/2026-10-19/manifest.md`; 5–10 trucks ≈ 105k–147k, 11–75 ≈ 41k–46k). 200–300 trucks is **0.11–0.19% of that band.**
- Inspection volume by fleet size, FMCSA Pocket Guide (Grade A, 2023 data): Very Small (1–6 PU) 1,008,803 inspections; Small (7–20) ~501,000 (2022) — **our band generates the overwhelming majority of all inspections.**

**What changed:** 200–300 trucks is comfortably reachable; the constraint is demand generation and sales capacity, not market size. The contracting market is a new fact worth monitoring. **Primary Pocket Guide PDF still to be read** — the size-band split is grade C until then.

### 2.3 Free alternatives (Gate 0.3) — PASS with a caveat

FMCSA free-of-charge (Grade A, verified 2026-10-19):
- **Motor Carrier Safety Planner** — free, public, online guide to the FMCSRs, with customisable checklists and forms.
- **ELD Carrier-Driver Training** — free online training for carriers and drivers.
- **ELD FAQ / guidance pages** — official answers on editing, annotations, accounts, exemptions.
- **Free RODS submission** for New Entrant programme uploads (ai.fmcsa.dot.gov).
- **SAFER / SMS public data** — the raw material for our Health Check, free.

**Verdict:** no free option provides *staffed, continuous, per-truck monitoring with document reconciliation and a 24/7 driver response line*. The free layer is education, self-service tooling and public data. **Gate passes.**

**Caveat with a commercial consequence:** the free layer covers training and self-service guidance thoroughly. **Therefore we cannot sell training or generic guidance as a revenue line** — it is free, and competing with it destroys margin and credibility. Our value has to be the *staffed execution and the evidence file*, not the knowledge.

### 2.4 The violation mix validates the positioning (Grade A — SMS data)

From live FMCSA SMS carrier profiles, read 2026-10-19, with the SMS severity weights attached to each code:

| Violation code | Description | Weight | Count (DOT 73705, a large carrier) |
|---|---|---|---|
| 395.24 | HOS (ELD) — ELD Form and Manner | 1 | 50 |
| 395.30B1-ELDDFR | Driver failing to review records and certify accuracy | 1 | 39 |
| 395.22H4-ELDBRODS | No supply of blank RODS graph-grids (min 8 days) | 1 | 30 |
| 395.3A2-HOSPD | Driving beyond the 14-hour window | 7 | 29 |
| 395.3(a)(3)(ii) | Beyond the 8-hour driving limit without a 30-min break | 7 | 26 |
| 395.3A1-HOSPD | Driving more than 11 hours after 10 off | 7 | 26 |
| 395.30B1 | Driver failed to certify accuracy of ELD information | 1 | 15 |
| 395.30B2-ELDDFC24 | Driver failed to certify immediately after final entry/correction | 1 | 10 |
| 395.24C2III | Driver failed to manually add shipping document number | 1 | 8 |
| 395.24C2II-ELDTN | Driver failed to manually input/verify trailer number | 1 | 8 |
| 395.24D-ELDPT | Failed to produce/transfer records on request | 3 | 8 |
| 395.8K2-HOSRC | Driver failed to retain 7 consecutive days of RODS in possession | 5 | — |
| 395.8F01 | Driver's record of duty status not current | 5 | — |
| 395.8A1-HOSP | Failing to have a RODS using the prescribed method | 5 | — |
| 395.32B | Driver failed to assume or decline unassigned driving time | 5 | — |
| 395.34A1-ELDDFN | Driver failed to note ELD malfunction and give written notice within 24h | 5 | — |
| 395.8(e) / 395.8E-HOSPD | False report of driver's RODS | 7 | — |
| 392.3-F | Operating while impaired through fatigue | 10 | — |

**What changed — this validates the core thesis with hard data.** In the live violation mix, the *documentation* codes (weight 1: form and manner, certification, blank graphs, shipping document number, trailer number) outnumber the *driving* codes, and the documentation codes are the ones a small fleet gets wrong constantly. The high-weight paperwork codes — 395.8A1, 395.8F01, 395.8K2, 395.32B, 395.34A1 — are all documentation defects, not unsafe driving.

**So: a fleet's HOS Compliance score is mostly damaged by paperwork, and paperwork is exactly what a staffed desk fixes.** That is now a demonstrated claim with FMCSA's own violation data behind it, not a hypothesis. It also tells us exactly what the service must do, in priority order: certification discipline → form and manner → shipping/trailer data entry → blank graph grids → production on request → unidentified driving time.

**New service line confirmed by the data:** 395.32B / 395.32(c) — unassigned driving time is a weight-5 violation that requires the *carrier* to act, and it is recurring and mechanical. It is a defensible, high-volume product.

### 2.5 SMS methodology has changed — the Health Check's centrepiece needs rebuilding (Grade A)

FMCSA "Prioritization Approved Changes to the SMS Methodology" and the SMS Methodology document, read 2026-10-19:
- BASICs are being **reorganised into "compliance categories."** Controlled Substances/Alcohol and operating-while-OOS violations move into the Unsafe Driving category. HOS Compliance remains a category (no change). Vehicle Maintenance splits into "Driver Observed" and "all other."
- **12-month data sufficiency standard:** carriers only receive percentiles in Unsafe Driving and Controlled Substances/Alcohol if they had at least one roadside violation in that category in the past 12 months.
- **A carrier must have at least three driver inspections with violations to be assigned a percentile greater than zero in the HOS category.** (Live SMS profile, DOT 2340455: "A carrier must have at least three driver inspections with violations to be assigned a percentile greater than zero in this BASIC.")

**What changed — this breaks a core reporting assumption.** For small fleets, the HOS Compliance percentile is *frequently not assignable at all* because there are fewer than three driver inspections with violations. "Your HOS percentile is 0" is therefore ambiguous: it can mean "excellent" or "we have no data."

**Consequence: the Health Check must be rebuilt on counts, not percentiles** — number of driver inspections, number with violations, violation codes with severity weights, and the specific paperwork defects — with the percentile shown only when assignable, and with an explicit "not enough data to score" state. The current template presents percentiles as the headline; that is wrong for our target segment. **This is a material rewrite of `assets/health-check-template.md` and `assets/health-check-build-guide.md`.**

### 2.6 ✨ Two competitors worth studying in detail

**Turbo ELD** — 100+ employees, 7+ years, 500+ clients, 500+ audits passed. ELD monitoring from $2/day per truck. Real-time log monitoring; **"Auto-certify logbooks"**; 24/7 support; weekly performance and violation reports; inspection alarms; support in English, Russian, Uzbek and Arabic. *"We keep a close eye on our drivers' ELD records to find infractions, mistakes, and missing information before they compromise your compliance."* Their claim: multilingual managers, "audit-ready."

**Prime Fleet Management** — the closest structural analogue. "Full outsourced compliance department" (Compliance Manager + HOS Specialist + Safety Specialist + Admin) from $500/month, with a named **HOS Specialist** whose scope is daily ELD monitoring, logbook review and correction, driver HOS coaching and roadside inspection data review. Free DOT assessment as the lead magnet. Publishes the in-house cost comparison ($180k–$350k+/yr) as its anchor.

**What changed:** our business case is now demonstrably real (Prime Fleet sells it), but it is also demonstrably **not differentiated** on features. Differentiation must come from something structural: the 24/7 driver-response line and the source-documented correction file (the audit-ready artifact), neither of which either competitor foregrounds. **The "audit-ready file" is the product.** Also note Turbo ELD's "auto-certify logbooks" claim is worth a close look: automated certification raises the 395.30(b)(1)–(2) and 395.8(f)(2) questions we have just researched. We should not make that claim ourselves.

---

## Section 3 — Insurance, labour, tax (Gate 0.1 and operating inputs)

### 3.1 E&O cost band — known; offshore placement still open (Grades B/C)

US small-business E&O baseline (2025–26, grade C, insurer/broker aggregators): Hartford ~$76/mo standalone; insureon $65/mo at $1M/$1M; Progressive median $50/mo, average $69/mo; general range $42–76/mo, ~$500–1,735/yr; 10-or-fewer-employee firms average ~$1,735/yr.

**What changed:** the cost band is not the obstacle. At 100 trucks ($156k ARR), even $8k/yr of E&O is 5% of revenue — inside the 8% gate. **The unresolved question is not price but whether a Moldova-domiciled provider can obtain US-admitted E&O (and cyber) at all, and what underwriting will demand.** No source found that answers this; it is a broker conversation. **Gate 0.1 remains partially open by design** — research can narrow it, only a broker can close it.

### 3.2 ⚠️ Moldova tax regime — potentially the single largest margin lever (Grade C, high value)

- Employer statutory charge: a single **24% social insurance (CNAS) contribution** on gross salary; no employer-side health insurance charge. (playroll guide, Oct 2026)
- **Moldova IT Park residents pay one 7% tax on turnover that replaces corporate tax, payroll withholding and social contributions — guaranteed until 31 December 2035.** (same source)
- NBS 2025: average gross monthly earnings **15,594.5 MDL**, +11.5% YoY (≈ $890 at ~17.5 MDL/USD).
- Live market postings (Chisinau, Oct 2026): customer support specialist from 15,000 MDL (≈$860); call center operator from 12,000 MDL (≈$690); English-speaking customer support roles quoted $350–600/mo.
- Minimum wage 5,500 MDL.

**What changed:** the *cost* side of our unit economics is far better than assumed — a fully loaded English-capable support operator is plausibly **$850–1,100/month**, not the $1,300–1,800 previously modelled. But the **7% IT Park turnover tax is a very large deal**: if this service qualifies as an accredited IT activity, the marginal cost of labour collapses relative to a standard employer, and the entire 24/7 staffing economics change. **If it does not qualify, we are on 24% contributions plus corporate tax.**

**This is the highest-value open question in the whole sprint and it is the partners' own accountant's question, not a research question.** It must be settled before the pricing decision, because it determines whether $130/truck/month is comfortable or impossible.

### 3.3 Request volume (Gate 0.6) — partial

- ZenduELD's fleet calculator uses "unverified logs / month, per truck: 6" for a 50-truck fleet (grade C, model assumption).
- Prime Fleet's scope implies daily monitoring touchpoints (grade C, marketing).
- No published staffing-ratio study for outsourced ELD/log desks was found. **Null result.**

**Derived check (ours):** 6 exceptions/truck/month × 100 trucks = 600 exception reviews/month ≈ 150/week ≈ 30/day. At ~20 minutes per document-backed review that is ~200 hours/month of pure review — about 1.0–1.5 FTE per 100 trucks for reviews alone, *before* the 24/7 question-and-answer line. This is broadly consistent with the 6–8 FTE modelled for 200 trucks, so the labour model is not obviously broken, but it rests on a single grade-C assumption. **Verify by instrumenting the pilot.**

---

## Section 4 — Consolidated register

| ID | Question | Answer | Grade | Confidence | Status |
|---|---|---|---|---|---|
| 0.1 | E&O for a Moldova provider | Cost band fine ($500–1,735/yr US baseline); **offshore placement unresolved** | B/C | Medium | Open — broker |
| 0.2 | Market size | ~160–195k carriers in 5–75 PU band; 200–300 trucks = 0.11–0.19% | C | Medium | Closed pending primary PDF |
| 0.3 | Free alternatives | No staffed monitoring exists free; **training/guidance is free, so not sellable** | A | High | Closed |
| 0.4 | Price | **$130 is 2x the automation tier, 2.2x the offshore anchor; inside the staffed-HOS band** | C | Medium | **Open — repricing required** |
| 0.5 | Legal | Product design **confirmed and strengthened**; citation 395.8(e)(4)(ii) **wrong**, replaced; 2 sub-citations unverified | A | High | Closed with corrections |
| 0.6 | Request volume | ~6 exceptions/truck/month; no published staffing ratio | C | Low | Open — instrument the pilot |
| — | Violation mix | Documentation codes dominate by count; 5 paperwork codes at weight 5–7 | A | High | Closed — strong support |
| — | SMS methodology | Categories reorganised; **percentiles often not assignable for small fleets** | A | High | Closed — Health Check must be rebuilt |
| — | Enforcement | Small-fleet owners are criminally liable (Sisic: 11 tractors) | A/B | High | Closed — best sales asset found |
| — | Moldova tax | **7% IT Park turnover tax if eligible** — largest single margin lever | C | Medium | Open — accountant |

**Files changed as a result of this research:** `PLAN.md` (pricing, positioning, product design, legal anchors, segment), `SALES-PLAYBOOK.md` (price talk, objection handling, insurance-eligibility exclusions), `RISKS.md` (new risks 12–14), `assets/health-check-build-guide.md` and `assets/health-check-template.md` (rebuilt on counts and violation codes, not percentiles), `assets/hos-rods-reconciliation-checklist.md` (corrected legal anchors, 13-day window, 7-day rule, 395.32 line), `README.md`.
