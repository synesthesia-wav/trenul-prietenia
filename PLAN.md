# ELD Support Services — Go-To-Market Plan

**Status:** revised 2026-10-20 after the strategy panel (eight frameworks, applied in parallel) — see `research/strategy-memo.md`
**Price:** $130 / truck / month (a hypothesis until the owner interviews; see §11)
**Delivery model:** human, document-based corrections; **the product is the file**, not the desk
**Position:** managed hours-of-service compliance — a specialist desk inside outsourced compliance
**Legal basis:** 49 CFR 395.30(d) — we propose, the driver confirms, enters and recertifies

> **Three changes from the strategy panel that rewrite this plan:**
> 1. **The product is the file.** Not monitoring, not a hotline, not a monthly report — a source-documented, driver-certified correction record the carrier can hand to an inspector, an insurer, a broker or their own attorney. Eight independent frameworks reached this conclusion. Details in `research/strategy-memo.md` §1.1.
> 2. **24/7 is removed from all positioning.** It is ~50% of our fixed cost, table stakes (Turbo ELD: 100+ staff, four languages), and under 395.30(d)(2) most correction work is asynchronous and driver-certified anyway. It survives as an SLA attribute and a measured question, never as a headline.
> 3. **A new beachhead with a deadline: the New Entrant safety audit.** ~58,600 audits a year, 8.7% fail (~5,100 carriers/year), 45–60 days to produce a corrective action plan or **lose USDOT registration**, and the audit can be conducted **electronically by submitting documents**. The deliverable is a document package — which is what we are proposing to build — bought by a buyer with a hard external deadline and a total downside. See §4.
>
> **And one correction to our own record:** the Sisic sentence published in earlier drafts ("18 months, $50,000") was the prosecution's sentencing recommendation, not the judgment. The judgment was three years' probation including six months' home incarceration, a $1,000 fine and a $100 special assessment, plus a three-year FMCSA debarment. Corrected everywhere; sources in `research/RESEARCH-LOG.md` §1.4.

---

## 1. The core problem this business actually solves

Fleets do not get cited for driving hours as often as they get cited for **paperwork**.

A negative logbook inspection usually traces to one of:

| Failure | Who fixes it | Cost to fix |
|---|---|---|
| Missing / unsigned driver certification on the record of duty status | Driver + reminders | ~$0 |
| RODS doesn't reconcile to the BOL (pickup/delivery times don't line up) | Human review of documents | 15 min |
| 14 days of records not available in the ELD | Administrative | ~$0 |
| Edit without an annotation explaining it (395.30(c)(2)) | Documentation | 20 min |
| HOS violation (11-hr / 14-hr / 60-hr) | Driver behavior + planning | Coaching |
| Pre-trip / DVIR and vehicle maintenance gaps | Carrier, not us | — |

**Only the fifth is behavior.** The first four are documentation hygiene, and they are the bulk of what produces a bad `HOS Compliance BASIC` percentile. This matters: a service that sells only "we stop HOS violations" is selling something that depends on driver honesty. A service that sells "your paperwork is defensible and your certification is current" is selling something the vendor controls.

**Consequence for the pitch:** lead with audit-defensibility and paperwork integrity, not with "fewer violations." Violation prevention is the *outcome evidence*; paperwork is the *deliverable*.

---

## 2. Product design — the "we do not touch your ELD" principle

**The single most important structural decision in this business — and now a verified one.**

> **Correction (2026-10-19, research Gate 0.5):** earlier drafts cited `395.8(e)(4)(ii)` for this. **That paragraph does not exist in the current CFR.** The rule was withdrawn in a November 2023 technical-corrections rule (89 FR 712, eff. 2024-01-05) and the current 395.8(e) contains only (e)(1) false report, (e)(2) ELD tampering, (e)(3) permitting another to tamper. Everything below is anchored to the rule that actually governs. Full citations: `research/RESEARCH-LOG.md` §1.2.

**The regulation expressly permits what we do.** 49 CFR 395.30(d):

> "(1) On review of a driver's submitted records, the motor carrier may request edits to a driver's records of duty status to ensure accuracy. **A driver must confirm or reject any proposed change, implement the appropriate edits** on the driver's record of duty status, and recertify and resubmit the records in order for any motor carrier-proposed changes to take effect. ... (3) **Edits requested by any system or by any person other than the driver must require the driver's electronic confirmation or rejection.**"

That is our workflow, in the CFR, in one sentence: a third party proposes, the driver decides, the driver certifies. We are not building a workaround. We are building the process the rule describes.

Supporting anchors, all verified against the current CFR on 2026-10-19:

- **395.8(f)(2)** — "All entries relating to a driver's duty status must be legible and **made by the driver**."
- **395.30(f)** — the carrier "must not alter or erase ... the original information collected concerning the driver's hours of service, the source data streams ... or information contained in any ELD that uses the original information."
- **395.30(c)(2)** — every change or addition must be annotated with a reason.
- **395.30(e)** — the carrier may not coerce a driver into a false certification. So: we ask the driver, we never instruct.
- **395.30(d)(2)** — no edits may be requested before the driver has submitted the records. Corrections are a *review of submitted records*.
- **Appendix A 4.3.2.8(b)** — the ELD itself must not permit alteration or erasure of the original information or source data streams.
- **Appendix A 4.3.2.8.2(b)** — an ELD must not allow automatically recorded driving time to be shortened. **The device blocks the classic evasion.**
- **395.22(b)(1), (d), (e)** — establishes the legally recognised role of "support personnel who have been authorized by the motor carrier to access ELD records and make or suggest authorized edits," with named accounts and proper log-in.
- **395.32(c)** — the carrier must review records of unidentified driving and either annotate them or assign them to the right driver. A discrete, weight-5, recurring task.
- **395.36** — a driver must be able to access their own records; we may not create a process that obstructs that.
- **FMCSA, Editing and Annotations (Q4):** "Both the driver and authorized carrier staff can make limited edits ... All edits must include a note (annotation) ... the driver must confirm (certify) that any carrier edit is accurate, and resubmit the records."

So the model is:

1. **Driver or carrier requests** a correction. The records are already submitted (395.30(d)(2)).
2. **We** research source documents (BOL, rate con, GPS/stop trace, dispatch record, fuel card, scale ticket) and prepare the proposed correction with a written reason, each one attached to its source document.
3. **The driver confirms or rejects, makes the entry, and recertifies** (395.30(d)(1)). The carrier's support-personnel account is where the proposal lives (395.22(b)).
4. **We** retain the evidence pack and the audit trail, and produce it on demand to FMCSA, the carrier, or the carrier's insurance company.

Result: we never edit a federal record. We produce the *documented, defensible* basis for a correction, which is exactly what 395.30(d) contemplates. It is insurable, and it is stronger than a competitor's, because a competitor who edits for you cannot hand an inspector a clean trail.

**One risk FMCSA itself flags, which we must design around:** per the Editing and Annotations Q5, if the driver is unavailable or unwilling to recertify, **the carrier's proposed edit and annotation remain part of the record.** A proposed edit is not a harmless draft. So a correction we propose must always be one we would defend on its merits, and the driver must be asked rather than assumed. This is another reason Rule 2 is absolute.

**Rule of construction for the SOP:** every correction is classified before it is proposed.

| Class | Definition | Action |
|---|---|---|
| Typographical | Genuine clerical error — a field, a name, a trailer number, a form entry — that does not change a duty status, a timestamp, or any hours figure | Driver or carrier support personnel corrects; annotated; logged |
| Document-supported | Reconstructable from shipping papers / actual events, within the **13-day** submission window (395.8(a)(2)(ii)) | We prepare the evidence pack and the annotation; driver confirms, enters and recertifies |
| Disputed | Documents and the driver's account conflict, or the request falls outside the window | We do **not** propose a correction; we tell the driver exactly what document would support it; escalate to the carrier; log |
| Out of scope | Would require creating or erasing driving time, shortening automatically recorded driving time, or altering the original record | **Refuse, always, in writing, and log the refusal** |

Class 4 is written into the SOP, the training, and the contract. It is a control, not a formality — it is the answer to the E&O underwriter, to any carrier's risk manager, and to the record of federal prosecutions where carrier owners were charged with conspiracy to falsify records (see `research/RESEARCH-LOG.md` §1.4).

**Two citations we could not verify and must not use until we do:** the current paragraph for the 14-day ELD records-availability requirement, and the text of 395.3(e)(4). Both are on the verification list in `research/memo-gate0.md`. Until then, the SOP cites 395.8(k)(2) (driver retains the previous 7 consecutive days) and 395.8(k)(1) (carrier retains 6 months), both of which are verified.

---

## 3. Positioning

> **Rewritten 2026-10-20 by the strategy panel.** The old one-liner and ad led with 24/7, which the panel judged to be a $29 comparison in disguise — a virtual assistant, not a compliance desk — and a promise the roster cannot fund at our size. The new line leads with the file and contains no feature noun a competitor already claims (no 24/7, no multilingual, no price). Full reasoning in `research/strategy-memo.md` §1.3.

**One line:** *When somebody with authority asks about your records, you want a file behind you, not an excuse. We are the hours-of-service desk for fleets like yours: we check every log against the bill of lading and the rate con, we prepare each correction with the document that supports it, and your driver certifies it. We never touch the log.*

**The one thing we want to be known for:** *Every correction comes with the document behind it.*

**Owner-facing version (the actual ad):**

> When somebody with authority asks about your records, you want a file behind you, not an excuse. We are the hours-of-service desk for fleets like yours. We check every log against the bill of lading and the rate con, we prepare each correction with the document that supports it, and your driver certifies it. We never touch the log. Hand the inspector a file.

**The category:** *managed hours-of-service compliance* — a specialist desk inside outsourced compliance. Say the parent shelf out loud when the buyer asks for a comparison ("we are the outsourced compliance department, but only for the driver's log"), but lead with the specialism. Do not use the shelf "ELD compliance support" — it names a technology, it invites the $25–65 comparison, and it is the shelf the ELD platform vendors are winning.

**Do not claim "audit-ready."** TenFour sells an "audit-ready records vault," DXM sells "audit-ready files," and Turbo ELD claims "audit-ready" and "500+ audits passed." It is a contested adjective. "The document behind every correction" is a factual, non-copyable claim.

**What we sell:** a file — service levels we control, with a source document behind every correction and a written refusal logged for every request we declined.
**What we report:** process outcomes we observe (weight-5 paperwork defects closed per truck per month, by regulation).
**Never:** an outcome guarantee. A warranty on inspection results is uninsurable and unpriceable; an SLA on response time, coverage hours, and documentation completeness is both.

> **Proof constraint (confirmed):** the partners' 18-month, zero-negative-inspection record is under NDA and cannot be opened, quoted, or published. **We have no publishable track record of our own.** Everything below assumes that. Three consequences:
> 1. In year one the sales conversation is led by **process proof** — the Health Check on the carrier's own public data, the SLA they can measure from day one, the evidence pack behind every correction, the monthly report — never by claimed outcomes.
> 2. **Generating our own evidence becomes the top delivery priority.** Every account gets a pre-engagement baseline pulled from FMCSA data and a documented comparison at 90 days. The first three pilots are not revenue; they are the company's reference base. Design the monthly report so outcome data is collectable from day one at no extra cost.
> 3. Show the team's experience as a **system** — the 4-class SOP, the evidence-pack template, the reconciliation checklist — rather than as results. A published, rigorous process persuades a skeptical fleet owner more than an unverifiable brag, and it is the only proof we can put in a buyer's hands in month one.

### The price position — rebuilt from published prices (research 2026-10-19)

The competing offshore price is confirmed at **$80 per truck per month**. Research then found that **$80 is not the lowest anchor, and $130 is not the middle of the market.** Published US prices, read from vendor pricing pages on 2026-10-19, all normalised to USD per truck per month:

| Band | Providers and published prices |
|---|---|
| **Automation / filings** (software-led, light human review) | Trucking Hub **$29**/truck · Trucking Comply from **$25**/unit · TruckingMBA **$50–65**/truck (includes HOS compliance review, DQ file audits, mock audits, CSA monitoring, phone support with same-day response) · TenFour **$38–99**/driver (flat tiers, every price published) · Lili Safety **$50–100**/truck (flat tiers to 30 power units) |
| **Offshore / offshore-adjacent** | **Turbo ELD: from $2/day per truck ≈ $60/month** — 100+ employees, 7+ years, 500+ clients, 500+ audits passed, support in English, Russian, Uzbek **and Arabic** |
| **Staffed HOS desk** (our band) | **Prime Fleet Management: from $500/mo; "most fleets in our 6–25 truck range invest $1,500–$6,000/month"** — a named HOS Specialist doing daily ELD monitoring, logbook review and correction, driver HOS coaching, roadside inspection data review, plus a full compliance team, monthly report, quarterly review, annual mock audit, free DOT assessment as the lead magnet. ≈ **$60–250/truck** |
| **Full outsourced compliance department** | Prime Fleet quotes the in-house equivalent at **$180,000–$350,000+/yr** |

**What this changes.** $130/truck/month is **roughly 2x the automation band and ~2.2x the real offshore anchor.** It is defensible *only* against the staffed-HOS band — the buyer who is comparing us to Prime Fleet, not to a $29 bundle. We therefore:

- **Sell to the 15–75 truck fleet with a live hours-of-service problem**, not to the whole SMB market. A 5-truck owner with a clean record is served better by the free FMCSA training and a $29 bundle, and we should say so rather than discount.
- **Hold a 10-truck minimum** and re-tier the small end rather than compete on price.
- **Never lead with price and never run a price comparison.** Anchor on what the owner's actual alternative costs: an in-house compliance manager ($180–350k/yr per Prime Fleet's own published comparison), an annual compliance audit ($2–6k/fleet), a lawyer for a violation ($1.5–4k), and one hours-of-service citation with its insurance consequence. Then let three questions do the work against the incumbent: *who is accountable for a correction, what is the response time at 2am on a Sunday, and can they hand an inspector a document for every change they made?*
- **Differentiate on the audit-ready correction file and the 24/7 response line**, because neither Prime Fleet nor Turbo ELD foregrounds either. Turbo ELD's own copy claims "auto-certify logbooks," which sits uneasily with 395.30(b)(1)–(2) and 395.8(f)(2). We do not make that claim, and we can quietly be the compliant alternative.
- **Do not sell training or generic guidance as a revenue line.** FMCSA provides the Motor Carrier Safety Planner, free ELD carrier-and-driver training, and official guidance free. That free layer is real and it caps what knowledge alone can be charged for. Our value is the staffed execution and the evidence file.

**The strongest asset the research found, and it is not a price argument.** *United States v. Sisic* (D.R.I. 2020): the owner of an **11-tractor** carrier altered thousands of ELD entries for ~20 drivers to conceal driving and on-duty time; one driver died in an April 22, 2018 Oklahoma crash; he pleaded guilty to conspiracy to falsify records (18 U.S.C. § 371) and on **January 25, 2021 was sentenced to three years' probation including six months' home incarceration with electronic monitoring, 50 hours' community service, a $1,000 fine and a $100 special assessment**; FMCSA **suspended and proposed a three-year debarment on April 29, 2021, and debarred him on August 19, 2021**. The company is defunct. *(Earlier drafts of this line said "18 months and $50,000" — that was the prosecution's sentencing recommendation, not the judgment. Corrected 2026-10-20; sources in `research/RESEARCH-LOG.md` §1.4.)* That is our target customer — small fleet, owner-operated, an ELD and no compliance function — doing precisely what an unmanaged fleet does. And the mechanism is the part worth selling against: **what ended that company was not a messy log, it was the false second copy of the log he handed to the state trooper investigating the fatal crash and to the FMCSA compliance reviewer.** Full enforcement history, including a 126-count Virginia indictment that added **wire fraud** (the reason our documented-correction standard is not optional), is in `research/RESEARCH-LOG.md` §1.4.

---

## 4. Segments — ranked by profitability per unit of selling effort

> **Reordered 2026-10-20 by the strategy panel.** The beachhead is no longer "fleets with a violation" — it is **carriers with a dated event inside 90 days**, because that is the only buyer we can sell to without a track record. And the first segment is now one nobody in this business had looked at: the New Entrant safety audit.

### Tier 0 — Beachhead: the New Entrant safety audit **[NEW, recommended first]**
- **Who:** a carrier within its first 12 months of operating that has been selected for a New Entrant Safety Audit and is preparing the file FMCSA will review.
- **Why this is the best buyer we have found, and it is not close:**
  - **The deliverable is a document package.** FMCSA conducts the audit "at the carrier's place of business, **or electronically, by submitting relevant documents to FMCSA**." We are proposing to build exactly this artifact. A Moldova-based operation is structurally suited to it — no US field presence needed, because the deliverable is the file.
  - **The deadline is external, dated, and belongs to the buyer:** within 45 days (passenger/HM) or 60 days (all other) of the failure notice, a corrective action plan must be submitted — **or the carrier's USDOT registration is revoked.** That is not a $15,846 ticket; it is the end of the company.
  - **The failure mode is our exact skill.** "Failing to require drivers to make hours-of-service records" (395.8(a)) is one of the **16 automatic-fail regulations**. So is missing supporting documentation for the RODS. Both are document-assembly problems.
  - **The numbers are Grade A and large:** 58,600 New Entrant Safety Audits in 2023; **8.7% fail on the first attempt** (range 7.4–11.8% 2018–23); ~**5,100 carriers a year** fail and must produce a CAP in 45–60 days; **1% of all New Entrant exits are revocations for a failed safety audit**; 142,920 carriers exited the programme in 2023.
  - **They are unclaimed.** A new entrant has no compliance vendor, no insurance agent, no reference base and no idea what FMCSA will ask for. They do not appear on any list until they fail. **We do not need 15,000 carriers to build this business. We need 100 of them.**
- **Our offer:** a flat-fee **New Entrant Audit Preparation** engagement, 30 days, $1,500–4,000, covering the FMCSA Safety Audit Resource Guide document set (driver list, licences, RODS + supporting documentation, MVRs, medical certificates, vehicle list, maintenance files, accident register, insurance proof, BOC-3, IRP/IFTA) and the **corrective action plan** if the audit has already failed. **Credited in full against the first three months** of any continuing engagement.
- **Price anchor exists and is published:** mock DOT audits run $549 (Motor Carrier HQ) and $999 sale / $2,500 list (The DOT Doctor, onsite mock audit); Lili Safety already lists New Entrant Safety Audit Preparation as a service. The deadline justifies the top of that range.
- **Also adjacent, and dated:** FMCSA's **English Language Proficiency** NPRM (91 FR 51422, published 2026-08-10, comment period closed 2026-10-09) would make ELP violation under 391.11(b)(2) an **out-of-service criterion** — ~9,000 additional drivers OOS annually, $800/day downtime, 2-day replacement delay, **$14.4M/year of carrier cost** (FMCSA's own estimate). The DOT's own fact sheet states **more than 20,000 truckers have been kicked out of service since June 2025**, and California only began enforcing in January 2026. This is a live, growing enforcement front that lands on the immigrant-owned segment the partners know. Treat as a *watch and product* item, not a positioning thesis.

### Tier 1 — Beachhead: fleets with a dated event inside 90 days
- **Who:** owner-operated carriers, 10–75 power units, with a dated regulatory or commercial event: an insurance renewal, a citation / NOV / out-of-service order in the last 60 days, a broker or shipper that has started screening them, or a newly granted operating authority with 10+ power units already running. **The trigger is a date on the buyer's calendar, not a violation in his history.**
- **Why:** a fleet with a deadline and a bad record does not need our references — it needs us to fix it by a date. A fleet with a clean record needs proof, and we have none.
- **Our offer:** free HOS Health Check → paid pilot → monthly.
- **The new filter is a dated event, not a violation.** Violation history selects the fleets FMCSA has already seen, i.e. the ones Prime Fleet and Turbo ELD already want. The *unexamined* fleet — no score, no citation, no dread — is where there is no competitive attention. **Test both cohorts in the interviews and let the conversion rate decide.**
- **Note on metric naming (corrected 2026-10-19):** hours violations sit in the **Unsafe Driving** category; record-of-duty-status violations sit in the **HOS Compliance** category. FMCSA is reorganising BASICs into "compliance categories" (Controlled Substances/Alcohol and operating-while-OOS move into Unsafe Driving; HOS is unchanged) — and **a carrier needs at least three driver inspections with violations to be assigned a percentile above zero**, so for small fleets the percentile is frequently unassignable. The Health Check therefore leads with counts and violation codes, not percentiles. See `assets/health-check-build-guide.md`.
- **Also confirmed by the data:** FMCSA's own SMS profiles show documentation violations (form and manner, certification, blank graph grids, shipping-document number, trailer number) outnumber driving violations by count, and the weight-5 codes (395.8A1, 395.8F01, 395.8K2, 395.32B, 395.34A1) are all documentation defects. **A small fleet's score is damaged mostly by paperwork — which is exactly what a staffed desk fixes.** This is now a demonstrated claim, not a hypothesis.

### Tier 2 — Non-English-speaking owner and driver populations (a reach segment, not a language wedge)
- Chicago, Houston, Dallas–Fort Worth, New Jersey/New York, Atlanta, Detroit–Dearborn, and metros with large immigrant-owned trucking communities (Arabic, Spanish, Russian, Romanian, and others). The team works in RO/RU/EN, so the differentiator here must be **document verification and the inspection file, not language**.
- **What is possible without native-speaker staff:**
  - Serving a non-English owner is fully possible: the owner-facing conversation is document- and outcome-driven, and the correction is prepared in writing for the driver to sign, so the driver needs no language to comply with it.
  - Coaching a driver well in a language we do not speak is not possible. That caps the violation-prevention half of the value for non-English crews, and means our own outcome data for this segment will be weaker than for English-speaking crews. **Know this internally, and do not over-promise prevention in the sales pitch for this segment.**
- **⚠️ Language is not a differentiator here — the incumbent already has it.** Turbo ELD (the $60/month offshore provider) advertises support in **English, Russian, Uzbek and Arabic** with 100+ employees and 500+ clients. We cannot out-resource them on language. What we can out-perform them on is the *documented, inspection-ready correction file*.
- **The cheap fix:** translated driver-facing material (HOS cheat-sheet, certification reminders, break-discipline card) is a translation task, not a staffing decision. English first; translated versions on request from the fleet; use them as the referral engine. Near-zero cost, real benefit. **Do not hire on the back of a language thesis.**
- **Quantify before betting on it:** build the segment from FMCSA census data (§7) before treating it as a beachhead.

### Tier 3 — Expansion: all SMB fleets, 5–50 trucks
- Large, contested by Motive/Samsara, the $25–65 automation tier, and offshore vendors. Enter via the ELD-vendor resellers and insurance channels, not cold calls. **Do not enter this band on price** — it is occupied at $25–29 per truck.

### Explicit non-targets
- **Fleets under 10 trucks** (the account is too small to carry a staffed desk against — see §5 — and is served adequately by the free layer plus a $29 bundle). **Note the exception: New Entrant carriers are frequently 1–5 trucks and are still Tier 0, because they are buying an event, not a retainer.**
- **Fleets that want filings** — DQ files, Clearinghouse, drug and alcohol, IFTA, UCR, MCS-150. That is TenFour ($99 first truck / $59 each additional) and DotFleet Compliance ($75 per driver one-time, $30/driver/month) — cheaper, US-domiciled, and explicitly good at it. **Refuse and refer.** This is the most valuable refusal we have.
- **Fleets whose real problem is driver behaviour** — speed, following distance, fatigue driving. The weight-7 and weight-10 codes are behavioural; we do not coach, do not run telematics, do not run a safety programme.
- **Fleets that want us to edit the ELD or "make the hours work"** — refuse permanently, in writing.
- **Fleets 100+ power units** (in-house compliance staff; a procurement process that will eat the team).

---

## 5. Unit economics and the roster decision

Fully-loaded cost per seat in Moldova for a support specialist: **$850–1,100/month** (research 2026-10-19: live Chisinau postings show customer support roles from 15,000 MDL ≈ $860 gross; +24% CNAS social insurance ≈ $1,065 loaded, before any IT Park relief).

> **⚠️ The largest margin lever in the model, and it is not a research finding — it is a question for the partners' accountant.** Moldova's IT Park residents pay a single **7% tax on turnover that replaces corporate tax, payroll withholding and social contributions, guaranteed to 31 December 2035**. If an outsourced ELD/HOS compliance service qualifies as an accredited IT activity, the marginal cost of every additional operator falls substantially. If it does not, we are on 24% contributions plus corporate tax. **Settle this before finalising the price** — it determines whether $130/truck/month is comfortable or impossible. Source and caveats: `research/RESEARCH-LOG.md` §3.2 (grade C; confirm with the accountant, do not rely on it).

**Request volume assumption, and the one number everything rests on:** ~6 unverified logs per truck per month (ZenduELD's fleet calculator, grade C — a model assumption, not evidence). At 100 trucks that is ~600 exception reviews a month, ≈30 a day, ≈200 hours of pure review — roughly 1.0–1.5 FTE per 100 trucks for review alone. **This is the number to instrument on the pilot.** No published staffing-ratio study for outsourced ELD/log desks was found (null result).

### 5.1 The roster decision — 24/7 is now a measured question, not a doctrine

The strategy panel was unanimous on removing 24/7 from positioning, and split on whether to remove it from the *roster*. Here is the resolved position:

| Roster | FTE | Fixed cost/yr | Breakeven at $112/truck contribution | When it is right |
|---|---|---|---|---|
| **Three shifts (24/7 desk)** | 6 + supervisor | ~$95k | **~60–85 trucks** | Only if out-of-hours request volume proves load-bearing |
| **Two shifts + on-call stipend (business hours 06:00–22:00 ET, on-call after)** | 3–4 + supervisor | ~$58k | **~38–52 trucks** | The default, until the data says otherwise |

**Instrument from day one:** log every request with a timestamp, the hour of day, and whether it needed a human *in shift* to resolve. If a material share of night requests must be resolved in-shift, three shifts are non-negotiable and this change fails — that is exactly what the instrument is for. **Do not decide the roster by argument; the panel disagreed and the data is cheap.**

**Also note what 24/7 was never a differentiator against:** the *specialist* competitor, DotFleet Compliance, offers Mon–Fri 8am–6pm CT with a one-business-day response, and publishes every price. It was only ever a differentiator against ELD *software* — a comparison we should refuse, not win.

**Model (at $130/truck/month, three-shift roster for comparison):**

| | per truck / month | per year |
|---|---|---|
| Revenue | $130 | $1,560 |
| Variable cost (tools, ELD/API access, comms) | ~$18 | ~$216 |
| **Contribution** | **$112** | **$1,344** |

| Fleet size | Revenue/yr | Gross profit/yr (fixed $95k at 6 FTE) | Gross profit/yr (fixed $58k at 2 shifts) |
|---|---|---|---|
| 25 | $39,000 | ~$1,000 | ~$38,000 |
| 60 | $93,600 | ~$5,000 | ~$61,000 |
| 100 | $156,000 | ~$39,000 | ~$95,000 |
| 200 | $312,000 | ~$174,000 | ~$214,000 |
| 300 | $468,000 | ~$308,000 | ~$333,000 |

**Read these two right-hand columns carefully — the panel's verdict is that the two-shift column is the one we should be planning against.** Three shifts is a business that needs 60–85 trucks before it pays for itself. Two shifts is a business that needs ~40. **And note the strategic cost of three shifts: at 25 trucks, the 24/7 promise turns a viable account into a $1,000-a-year loss.**

### 5.2 The price ladder — one ladder, in one place **[corrected 2026-10-20]**

The panel found that `PLAN.md` and `SALES-PLAYBOOK.md` carried **different tiers** (a 15-truck fleet was $1,950/mo in one and $2,250 in the other) and that the ladder was **built to lose money in exactly the two bands where we cannot win on price**. Reconciled, and the reconciliation is now binding:

| Fleet | Price | Floor | Why |
|---|---|---|---|
| 1–14 trucks | **$150**/truck/mo | $1,500/mo | At 10 trucks, $130 is a **−$6,360/yr** account. Never sell a staffed desk on it. |
| 15–49 trucks | **$130**/truck/mo | $1,950/mo | The list price. The band we sell to. |
| 50+ trucks | **$130**/truck/mo | $6,500/mo | **The old $110 tier is deleted** — at 50 trucks it made the account **−$31,800/yr**, i.e. we were paying our best reference candidates to leave us in the hole. Price big fleets *up*, not down: they create more risk exposure and cost us less per truck. |
| **Revenue floor** | — | **$1,950/mo per account** | Covers fixed cost and one seat, not one seat alone. |
| **24/7 live desk** | **+$55**/truck/mo | applies at 75+ trucks | Sold as a tier, never as the default. Never below ~75 trucks. |
| **New Entrant audit prep** | **$1,500–4,000 per event** | — | Tier 0. Benchmarked to published mock-audit prices of $549–2,500. |

**Presentation, not pricing:** quote **$1,950/month for a 25-truck fleet** on the offer sheet and per-truck on the invoice. "$130 a truck" invites "the ELD is $29 a truck." "$1,950 a month for your fleet" invites "what do I spend on compliance today?" — where the honest answer is $725–1,625 of software, $0 of people, and his office manager's time.

**Levers, in order of impact:**
1. **Fewer than 8 FTE at 200 trucks is the real constraint.** Automate the *monitoring* (exception detection off the ELD feed) so humans do the document reconciliation and the exceptions. Automation is not the product; it is the only way to hold a five-minute response at scale — and if we drop 24/7, the only way to hold a one-business-hour response at all.
2. **One ladder, one place.** The tiers above are binding; `SALES-PLAYBOOK.md` §4 mirrors them exactly.
3. **Revenue floor, not truck-count floor.** $1,950/mo per account.
4. **Proration needs a floor.** "No billing for inactive trucks" is a good sales line and a bad contract. Recommend: bill on active trucks, but with a floor of 60% of contracted power units, or a 90-day notice on reductions. Seasonal fleets will otherwise halve your revenue while your shift roster stays fixed.

**CAC:** a 25-truck account via a self-sold path costs roughly $2,000–3,500 (sales time, collateral, subsidised pilot) = $80–140/truck → payback under 2 months. A broker referral at 20% of year-one revenue = $312/truck. **CAC is not the constraint. Conversion rate, cycle time, and truck count per account are.**

**Pilot must be designed to not blow the fixed cost:** flat fee $750–1,500/month for 5–10 trucks, **business-hours SLA only** (no 24/7 during the pilot), credited in full against the first three months of the contract.

---

## 6. Channel mix — in order of expected return

Cold calling is the *last* resort, not the first. At $130/truck/month with a $39k account, a single closed fleet repays the sales cost many times over; the problem is that owner-level cold calls convert poorly, take 3 weeks, and burn the salesperson. Put effort where a single relationship produces many trucks.

**1. Insurance agents and brokers who write commercial truck — the highest-leverage channel.**
They already see claims, inspections, and CSA data, and they compete on loss prevention. Give them the Health Check as a free loss-prevention tool for their carrier clients; refer with a 20% year-one commission or a 1-month credit. One good agent relationship can carry 50+ trucks.

**2. ELD / telematics resellers and installers.**
They see every new truck and every new owner, and the reseller's captive list is exactly the 1–50 truck segment. Sell them white-label: they own the customer relationship and take the margin; we deliver. This also gets us API-level ELD access without asking a cold owner for credentials.

**3. Owner and driver communities in the languages they already use.**
Mosque and community business networks, immigrant-owned carrier associations, trucker WhatsApp/Facebook groups, and the partners' existing driver contacts (subject to the prior-employer check). Driver-facing HOS content in the driver's own language is both a marketing engine and a violation-prevention tool. Translated collateral, not native-speaker staff, is the cost-effective version.

**4. Partner network (with a legal check).**
The partners' former colleagues now running fleets are the warmest first 10 accounts. **But:** confirm no non-solicitation, confidentiality, or trade-secret obligation from their prior employers covers using those relationships, and confirm that the 18-month inspection record is under NDA and cannot be opened, quoted, or published, so it cannot be used as a sales asset. Do this before the first call, not after the first subpoena.

**5. Direct outbound — targeted, not cold.**
Not owner-cold-calls from a list. Owner-outbound with a *specific, free, personalized finding* (the Health Check on their own DOT number) and a 20-minute ask. Different from a cold call in every way that matters: they can verify the finding themselves on SAFER without trusting us.

**6. Content that ranks and gets shared.**
- "ELD/HOS Health Check" — free self-serve tool (carrier enters DOT number, gets their percentile + a checklist). This is the only marketing asset that can be built in a week and used at scale.
- Driver-facing HOS material in the driver's own language (short videos + a printable card; English first, translated versions on request). Shared in WhatsApp and driver groups; the owner hears about us from the driver, which is the highest-credibility referral in trucking.

---

## 7. Segment sizing — do this before committing

Do not guess the TAM. Build it:
- Pull the **FMCSA SAFER Company Census file** (bulk CSV) and filter: active authority, 5–75 power units, US domicile. That gives the full Tier-3 universe — a number worth knowing.
- For non-English-speaking owner populations, overlay carrier legal names and addresses; treat name-based inference as a *hypothesis generator*, not a filter, and validate against a sampled phone screen.
- Cross-reference state-level HOS enforcement activity and inspection frequency to rank states.
- Also count: how many carriers in the target size band are in states with active FMCSA HOS initiatives — those are the ones feeling pressure in the next 12 months.

**Deliverable:** a one-page market map (states × size band × priority), which then sets the outbound list and the 90-day plan.

---

## 8. Compounding loop — marketing that reduces churn

The recurring fears in SMB trucking are: (1) the driver gets pulled over, (2) the insurance renewal goes up, (3) the driver quits because he's being watched, (4) the FMCSA audit.

Our service addresses 1, 2, 4. It creates 3 — being monitored is unpleasant. **Counter it deliberately:** driver-facing training in the driver's own language, framed as protection ("this card keeps you from a $700 ticket"), turns the source of resentment into the referral engine. A driver who sends his friends the cheat-sheet because it saved him a citation is our best channel, and a fleet with trained drivers churns less. English is the first version; translated versions are cheap and additive — make translation part of the collateral pipeline, not a hiring decision.

---

## 9. 90-day plan

> **Resequenced 2026-10-20 by the strategy panel.** The panel's sharpest criticism of this plan was its sequencing: we were scheduled to sell before we were allowed to, the price was marked "confirmed" without a single buyer conversation, and the proof strategy was arithmetically incapable of producing evidence in 90 days. **The interviews and the outbound now start in week one. The entity, E&O and attorney gate *signing*, not *talking*.**

### Days 1–5 — Buy the diagnosis (do this before anything else)
- [ ] **Ten owner interviews and two dispatcher interviews, in week one.** The two load-bearing unknowns are willingness to pay at $130 and requests per truck per week, and both gate the price decision. Guides: `research/interview-guides.md`. **The panel's rule: the price is a hypothesis until these are read, and the segment is decided by the conversion rate of the dated-event cohort versus the unexamined cohort — not by argument.**
- [ ] **E&O broker call** (research cannot close this). Attach the SOP and the 395.30(d) analysis. Four questions: can you write E&O for a Moldova-domiciled provider serving US motor carriers; what underwriting material do you need; what do US carriers typically demand (limits, claims-made, US claims handling); what does it cost against premium. **Also ask in writing whether they will write a citation indemnity** — and hear a "no" as information, because it decides the offer design.
- [ ] **Moldovan accountant: does this service qualify for the IT Park 7% turnover tax?** Largest single margin lever in the model. See §5.
- [ ] **Start the outbound now.** Day 1: send 25 Health Checks and make 10 calls. A conversation needs no entity, no E&O and no contract. Waiting until day 40 wastes five weeks of the only asset we have — the requester's attention.
- [ ] **Instrument every request from call one:** timestamp, hour of day, class, whether it needed a human in shift. This decides the roster (§5.1) and the labour model.

### Days 1–20 — Foundation (parallel tracks)
- [ ] **Decide the price and segment together (blocking), after the interviews.** See §3, §5.2 and `research/memo-gate0.md`. Include the 50–200 PU question, which the panel split on and which the interviews should settle.
- [ ] Write the correction protocol and the 4-class SOP; have a US transportation attorney review it (this is also the E&O underwriting package). **Write the procedure from the public regulation, not from the partners' prior employer's playbook** — that is both the trade-secret defence and the reason it is an asset we own. Include the two unverified citations as open questions for him.
- [ ] **Ask counsel whether the refusal log is exculpatory or discoverable as an admission.** If discoverable, it must be scoped to process ("we did not propose a change because the documents did not support one") rather than to the requester's intent. This gates the single most valuable asset we have.
- [ ] Fix the proration policy: add the 60% floor.
- [ ] Build the HOS Health Check (SAFER + SMS carrier profile). **Lead with counts and violation codes, not percentiles**, and carry an explicit "no score because nobody has looked" state — see `assets/health-check-build-guide.md`.
- [ ] **Build the "open the glovebox" instrument** (Sutherland's): a one-page weighted defect checklist and a 20-minute session where **the buyer scores his own ten driver-days and his own cab, with us present**. The first cab audit is free, needs no ELD integration, no API, no NDA and no E&O — which is why it can be done 20 times before a single contract exists. The checklist is built from 395.22(h) (the in-vehicle packet: data-transfer instruction sheet, **ELD malfunction reporting sheet**, 8 days of blank graph grids) and 395.34(a) (24-hour written malfunction notice; paper reconstruction of the current 24-hour period and the previous 7 days). **Success: ≥15 of 20 sessions return a non-zero defect count** — if most fleets come back clean, the thesis is wrong and we learn it in week one, not month six.
- [ ] **Build the New Entrant audit-prep product (Tier 0).** Assemble against the FMCSA Safety Audit Resource Guide document list. Flat fee $1,500–4,000, 30 days, credited against any continuing engagement. **This is the first thing we sell.**
- [ ] **Make the refusal log and the correction SOP public** (subject to counsel's answer above), as a page a skeptic is invited to attack.
- [ ] Hire 1 bilingual supervisor (RO/RU/EN) for the desk; produce the English driver-facing collateral set; set up the translation pipeline for on-request languages.
- [ ] Build the pilot offer, the SLA sheet, the authorization form, the pricing tiers.
- [ ] **Instrument the request-volume count from day one** — requests per truck per week by class. The labour model rests on one unverified number (~6 logs/truck/month). See `RISKS.md` §14.
- [ ] Legal checks on the partners' prior-employer obligations.
- [ ] Cross-border tax + entity advice: W-8BEN-E, US invoicing, whether a US LLC is needed for banking/insurance only, and the buyer's use-tax position. Keep the contracting entity offshore to avoid creating US nexus.
- [ ] Download the FMCSA Pocket Guide 2024 PDF and the census file; build the target list; open the SMS Appendix A violations list.

### Days 15–45 — Proof
- [ ] **The first New Entrant audit-prep engagement sold and delivered** (Tier 0). This is the proof of the product, not of the funnel.
- [ ] **Run the first 20 glovebox sessions** (`assets/GLOVEBOX-GUIDE.md`). Each one ends with the cab review generated and sent within 48 hours (`assets/merge_cab_review.py`). The written review is the artefact that gets forwarded, and forwarding is the only referral engine we have.
- [ ] **Capture every session in the session sheet** (`assets/session-sheet.html`) and run `python3 research/aggregate_sessions.py` weekly. It produces the defect-rate table, the price evidence and the three gate decisions — against thresholds fixed in advance, so they cannot be moved afterwards.
- [ ] 3–5 friendly fleets from the partners' network, on paid pilots (business-hours SLA, flat fee).
- [ ] Baseline their FMCSA records, response times, correction turnaround, and driver feedback **before** we touch anything.
- [ ] **Measure what we can count ourselves, not what we cannot:** weight-5 paperwork defects found and closed per truck per month, by regulation. **Do not build a citation-count measurement programme** — a small fleet gets 1–3 roadside inspections a year and FMCSA will not assign a percentile without three driver inspections with violations, so the outcome metric cannot move in 90 days. The pre-engagement baseline is still captured, as a *byproduct of the first call*, but it is not a workstream.
- [ ] Fix the SOP from real pilot cases.

### Days 40–90 — Repeatable motion
- [ ] **Insurance agents first, and with a target attached.** Send the one-pager (`assets/agent-onepager.html`). One carrier, free, with the agent's name on it. The panel was unanimous: the agent is the channel that substitutes for the track record we cannot show, and the plan previously ranked it #1 while attaching no number to it. Target: **10 agent conversations, 3 agents with a referral in progress, 1 signed referral.** The ask is *one free file for one of their insured fleets*, not a referral fee.
- [ ] 2 ELD-reseller conversations — **introducing only, never white-label.** White-label contradicts `RISKS.md` §4 and §10, points at the $29 band, and would make 100% of revenue depend on one counterparty.
- [ ] 50–100 Health Checks sent/week — but **only if they are automated**; at 45 minutes each, 100/week is a ceiling, not a target. The funnel arithmetic says ~1,160 Health Checks per 100 trucks, which no human can produce. **Automate the pull-and-render, or the funnel cannot open.** (Cold outbound converts at roughly 1 contract per 290 sends; one agent referring three fleets at warm rates is worth ~900 cold sends. **That is why the agent target above matters more than the outbound volume.**)
- [ ] Publish the driver-facing HOS material (English, then translated on request); start the driver-group push.
- [ ] First case study written from pilot data — a **file**, not a claim.

### 90-day targets
| Metric | Target |
|---|---|
| **Owner interviews completed (week 1)** | **10 + 2 dispatchers** |
| **New Entrant audit-prep engagements sold** | **2** |
| Glovebox self-score sessions run | 20 |
| Sessions returning a non-zero defect count | ≥ 15 of 20 |
| Pilots running | 5 |
| Pilot → contract conversion | ≥ 60% |
| Trucks live | 25-40 |
| Pre-engagement baseline captured | 100% of managed fleets (day 1 of onboarding) |
| Corrections with a source document attached | 100% of Class 2 |
| Refusals logged | 100% of Class 4 |
| Requests answered inside the SLA | ≥ 95% |
| Insurance-agent conversations | 10, with ≥3 referrals in progress |
| Weight-5 paperwork defects closed per truck per month | measured from day 1 |
| Avg response time | < 10 min, 24/7 |
| Conversations/week (owner-level) | 15-20 |
| Own evidence base (managed fleets with a documented pre/post baseline) | 3 by day 90 |
| Insurance-agent relationships with a referral in progress | 2 |
| Cost per closed fleet | < $3,500 |

---

## 10. Metrics dashboard — review weekly

**Commercial:** trucks live (total and by tier) - new trucks added per month - monthly logo churn and truck churn - ARPA/truck - pipeline by stage - conversion at each stage - CAC/truck - payback months - **accounts (not trucks) as the primary count**, because 4-6 accounts of 50-100 trucks is a different business from 12-15 accounts of 20-25, and the metric should say which one we are building.

**Service:** requests per 1,000 trucks/week, **broken out by hour of day and by whether a human in shift was required** (this is the roster instrument, see 5.1) - median and p95 response time - % requests resolved within SLA - corrections by class (1 clerical / 2 document-supported / 3 disputed / 4 refused) - % RODS reconciled without driver escalation - document turnaround time - **refusals logged as a positive health metric, reviewed monthly by the owner**.

**Outcome - only what we control:** **weight-5 paperwork defects found and closed per truck per month, by regulation** (395.8A1, 395.8F01, 395.8K2, 395.32B, 395.34A1) - driver certifications obtained per correction - % of Class 2 corrections with a source document attached - repeat-violation rate. **The old outcome block (percentile movement, violations prevented) is removed from the dashboard.** A small fleet generates roughly 1-3 roadside inspections a year and FMCSA will not assign a percentile without three driver inspections with violations, so that block would read "no percentile assignable" for most of our accounts and would invite the outcome claims we have decided not to make. The pre-engagement baseline is still captured - as a byproduct of the first call - and the percentile is reported when one exists.

**Operational:** cases per FTE per day - overtime hours - staff attrition - driver certification currency %.

**One rule, now stricter:** every number in every customer-facing document carries a source URL and a pull date, and any figure that is a recommendation, estimate or projection is labelled as one. **This rule exists because we got the Sisic sentence wrong** - see `research/RESEARCH-LOG.md` section 1.4. A seller caught overstating a court record has no credibility left to sell a compliance file with.

---

## 11. The strategy, in one page

*Written by the strategy panel, 2026-10-20. Full reasoning in `research/strategy-memo.md`.*

**Diagnosis.** We are selling a product in the wrong category. The deliverable the buyer actually needs is a **source-documented, driver-certified file** that proves his operation was lawful when someone with authority comes - and no competitor claims it, because for everyone else it is a compliance control rather than a product. Meanwhile the promise we have been leading with, 24/7, is roughly half our fixed cost, is table stakes at $60, and under 395.30(d)(2) most of the work cannot be actioned until business hours anyway.

**Guiding policy.** *We are the hours-of-service recordkeeper for fleets too small to employ a compliance department and too exposed to be examined. We are bought for one reason: when a record is challenged, there is a file behind it - a source document for every correction, a driver certification for every entry, a written refusal logged for every request we declined, and a named person who answers the phone. Every choice is made to make that file defensible; none is made to make a truck count look good.* **We sell the file. We do not sell a reduction in violations, because we cannot promise one and cannot measure one.**

**What we refuse, stated as a reject-list that every new opportunity is tested against:**
1. No 24/7 promise as a default, and no 24/7 roster before the volume pays for it.
2. No lead with the criminal case; no claim that we prevent violations or citations.
3. No price comparison with the $25-65 automation tier, and no chasing of a truck count.
4. No selling training or guidance (FMCSA gives it away free), and no hiring on a language thesis.
5. No selling of DQ files, drug and alcohol, IFTA/UCR, vehicle maintenance, or legal representation - refuse and refer.
6. No white-label through a reseller.
7. No line of the prior employer's SOP. The procedure is written from the public regulation - that is both our trade-secret defence and the reason it is an asset we own.
8. No number in a customer-facing document without a source URL and a pull date.

**The three gates, in order, before we spend the $95k fixed cost:**
1. **E&O broker** - can a Moldova-domiciled provider write E&O with US claims handling? *(Research cannot close this.)*
2. **Accountant** - does the IT Park 7% turnover regime apply? It sets the cost per seat, and therefore the number of trucks the accountability model needs.
3. **Ten owner interviews** - will they pay above $100/truck/month for a document-backed file?

**The kill criterion, stated in advance so nobody moves the goalposts:** if the broker says no, **or** if fewer than 3 of 10 owners will pay above $100, then the honest conclusion is that **this is a $60-80 scale/resale business, not a $130 premium business** - and the plan gets rebuilt around the labour-cost differential and the *absence* of the accountability story, rather than a price the market will not pay. That is still a business. The one thing we may not do is keep a price the market has already refused.

---

## 12. Open items for the partners
1. Confirm which ELD platforms the team can access and how (own accounts, customer-provided API tokens, or reseller-provided) - this determines the data model.
2. Confirm the actual number of requests per truck per week in the pilot - it drives FTE count and is the single number the roster decision rests on.
3. The 18-month record is NDA-locked. Confirm with counsel whether the partners may serve as **personal references** (without disclosing the former employer's data) and whether the methodology can be described in general terms. Neither substitutes for our own evidence, but both strengthen the first three conversations.
4. Decide: do we edit the ELD or prepare corrections for the driver to make? **Recommend: prepare only** (section 2). This is a decision, not a detail.
5. Decide the invoice entity, the tax position, and who signs the E&O application.
6. **New:** the panel split on fleet size (10-40 vs 15-75 vs 50-200 PU) and the interviews should settle it. If 50-200 wins, the target becomes **4-6 accounts** rather than 12-15, and the whole sales motion changes shape.
7. **New:** counsel's answer on whether the refusal log is exculpatory or discoverable as an admission. It gates our best marketing asset.
