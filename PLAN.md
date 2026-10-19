# ELD Support Services — Go-To-Market Plan

**Status:** draft for partner review
**Price:** $130 / truck / month (confirmed)
**Delivery model:** human, document-based corrections; 24/7 via Moldova shift roster
**Position:** legitimate managed compliance — corrections only where source documents support them

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

**One line:** *The compliance desk for small fleets — we answer the driver at 2am, we reconcile the paperwork, and every correction we handle is backed by a document and written down.*

**Owner-facing version (the actual ad):**

> You will never get a call about a logbook again. We answer your drivers at any hour, we reconcile every trip against the BOL, and if an inspector asks, you hand them a file instead of an excuse.

**What we sell:** service levels we control.
**What we report:** outcomes we observe.
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

**The strongest asset the research found, and it is not a price argument.** *United States v. Sisic* (D.R.I. 2020): the owner of an **11-tractor** carrier altered thousands of ELD entries for ~20 drivers to conceal driving and on-duty time; one driver died; the owner pleaded guilty to conspiracy to falsify records (18 U.S.C. § 371), 18 months' imprisonment and a $50,000 fine, and the company is defunct. That is our target customer — small fleet, owner-operated, an ELD and no compliance function — doing precisely what an unmanaged fleet does. The alternative to paying for a service is that the owner does it himself, and the consequence is not a fine. Full enforcement history, including a 126-count Virginia indictment that added **wire fraud** (the reason our documented-correction standard is not optional), is in `research/RESEARCH-LOG.md` §1.4.

---

## 4. Segments — ranked by profitability per unit of selling effort

### Tier 1 — Beachhead: fleets that already got hurt
- **15–75 power units**, active authority, one or more HOS/RODS violations or citations in 24 months, or a documented paperwork deficiency. (Raised from 5–50 and narrowed at the bottom after research: below ~10 trucks, the free FMCSA training plus a $29 bundle serves the owner better than a 24/7 desk.)
- **Why:** they have a budget line and a deadline, the health-check report is directly actionable, and the sales conversation is about *their* problem, not our product.
- **Our offer:** free HOS Health Check → paid pilot → monthly.
- **Note on metric naming (corrected 2026-10-19):** hours violations sit in the **Unsafe Driving** category; record-of-duty-status violations sit in the **HOS Compliance** category. FMCSA is reorganising BASICs into "compliance categories" (Controlled Substances/Alcohol and operating-while-OOS move into Unsafe Driving; HOS is unchanged) — and **a carrier needs at least three driver inspections with violations to be assigned a percentile above zero**, so for small fleets the percentile is frequently unassignable. The Health Check therefore leads with counts and violation codes, not percentiles. See `assets/health-check-build-guide.md`.
- **Also confirmed by the data:** FMCSA's own SMS profiles show documentation violations (form and manner, certification, blank graph grids, shipping-document number, trailer number) outnumber driving violations by count, and the weight-5 codes (395.8A1, 395.8F01, 395.8K2, 395.32B, 395.34A1) are all documentation defects. **A small fleet's score is damaged mostly by paperwork — which is exactly what a staffed desk fixes.** This is now a demonstrated claim, not a hypothesis.

### Tier 2 — Non-English-speaking owner and driver populations (a reach segment, not a language wedge)
- Chicago, Houston, Dallas–Fort Worth, New Jersey/New York, Atlanta, Detroit–Dearborn, and metros with large immigrant-owned trucking communities (Arabic, Spanish, Russian, Romanian, and others). The team works in RO/RU/EN, so the differentiator here must be **document verification and the inspection file, not language**.
- **What is possible without native-speaker staff:**
  - Serving a non-English owner is fully possible: the owner-facing conversation is document- and outcome-driven, and the correction is prepared in writing for the driver to sign, so the driver needs no language to comply with it.
  - Coaching a driver well in a language we do not speak is not possible. That caps the violation-prevention half of the value for non-English crews, and means our own outcome data for this segment will be weaker than for English-speaking crews. **Know this internally, and do not over-promise prevention in the sales pitch for this segment.**
- **⚠️ Language is not a differentiator here — the incumbent already has it.** Turbo ELD (the $60/month offshore provider) advertises support in **English, Russian, Uzbek and Arabic** with 100+ employees and 500+ clients. We cannot out-resource them on language. What we can out-perform them on is the *documented, inspection-ready correction file* and a 24/7 response line with a named accountable human.
- **The cheap fix:** translated driver-facing material (HOS cheat-sheet, certification reminders, break-discipline card) is a translation task, not a staffing decision. English first; translated versions on request from the fleet; use them as the referral engine. Near-zero cost, real benefit. **Do not hire on the back of a language thesis.**
- **Quantify before betting on it:** build the segment from FMCSA census data (§7) before treating it as a beachhead.

### Tier 3 — Expansion: all SMB fleets, 5–50 trucks
- Large, contested by Motive/Samsara, the $25–65 automation tier, and offshore vendors. Enter via the ELD-vendor resellers and insurance channels, not cold calls. **Do not enter this band on price** — it is occupied at $25–29 per truck.

### Explicit non-targets
- **Fleets under 10 trucks** (the account is too small to carry 24/7 cost against — see §5 — and is served adequately by the free layer plus a $29 bundle).
- Large fleets (100+ trucks): they have in-house compliance staff and will run a procurement process that will eat the team.

---

## 5. Unit economics and the 24/7 decision

Fully-loaded cost per seat in Moldova for a support specialist: **$850–1,100/month** (research 2026-10-19: live Chisinau postings show customer support roles from 15,000 MDL ≈ $860 gross; +24% CNAS social insurance ≈ $1,065 loaded, before any IT Park relief). 24/7 coverage needs 3 shifts × 8h with a ~1.5 relief factor → **4.5–6 FTE**, plus 1 bilingual supervisor. For 200 trucks at 40–60 min/truck/week of monitoring and document verification, plan on **6–8 FTE**.

> **⚠️ The largest margin lever in the model, and it is not a research finding — it is a question for the partners' accountant.** Moldova's IT Park residents pay a single **7% tax on turnover that replaces corporate tax, payroll withholding and social contributions, guaranteed to 31 December 2035**. If an outsourced ELD/HOS compliance service qualifies as an accredited IT activity, the marginal cost of every additional operator falls substantially. If it does not, we are on 24% contributions plus corporate tax. **Settle this before finalising the price** — it determines whether $130/truck/month is comfortable or impossible. Source and caveats: `research/RESEARCH-LOG.md` §3.2 (grade C; confirm with the accountant, do not rely on it).

**Request volume assumption, and the one number everything rests on:** ~6 unverified logs per truck per month (ZenduELD's fleet calculator, grade C — a model assumption, not evidence). At 100 trucks that is ~600 exception reviews a month, ≈30 a day, ≈200 hours of pure review — roughly 1.0–1.5 FTE per 100 trucks for review alone, before the 24/7 question line. **This is the number to instrument on the pilot.** No published staffing-ratio study for outsourced ELD/log desks was found (null result).

**Model:**

| | per truck / month | per year |
|---|---|---|
| Revenue | $130 | $1,560 |
| Variable cost (tools, ELD/API access, comms) | ~$18 | ~$216 |
| **Contribution** | **$112** | **$1,344** |

| Fleet size | Revenue/yr | Gross profit/yr (fixed $95k at 6 FTE) |
|---|---|---|
| 25 | $39,000 | ~$1,000 |
| 60 | $93,600 | ~$5,000 |
| 100 | $156,000 | ~$39,000 |
| 200 | $312,000 | ~$174,000 |
| 300 | $468,000 | ~$308,000 |

**Read this table carefully — it is the whole strategy.**

- **Breakeven is roughly 60–85 trucks.** Below that, the 24/7 promise consumes the entire company. Every account below ~10 trucks is a net negative unless priced higher.
- **Above ~150 trucks, the 24/7 promise is nearly free per truck and becomes the strongest differentiator against offshore competitors** who cannot credibly staff US hours with a 5-minute response. The promise is a barrier to entry, not a cost center, once you are big enough.
- **This business is a volume game.** Target 200–300 trucks within 24 months; do not celebrate 15 small accounts.

**Levers, in order of impact:**
1. **Fewer than 8 FTE at 200 trucks is the real constraint.** Automate the *monitoring* (exception detection off the ELD feed) so humans do the document reconciliation and the exceptions. Automation is not the product; it is the only way to hold 5-minute response at scale.
2. **Tiered pricing** protects the small-fleet end: <10 trucks $195/truck/mo · 10–49 $130 · 50+ $110. Never sell 24/7 coverage on a 3-truck fleet.
3. **Minimum 10 trucks per account** (or $1,300/mo floor).
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

### Days 1–20 — Foundation (parallel tracks)
- [ ] **Decide the price and segment together (blocking).** $130 with a 10-truck minimum and a 15–75 truck target band, or re-price. See §3 and `research/memo-gate0.md`.
- [ ] **E&O broker call** (the research cannot close this). Attach the SOP and the 395.30(d) analysis. Four questions: can you write E&O for a Moldova-domiciled provider serving US motor carriers; what underwriting material do you need; what do US carriers typically demand; what does it cost against premium.
- [ ] **Moldovan accountant: does this service qualify for the IT Park 7% turnover tax?** Largest single margin lever in the model. See §5.
- [ ] Write the correction protocol and the 4-class SOP; have a US transportation attorney review it (this is also the E&O underwriting package). Include the two unverified citations as open questions for him.
- [ ] Fix the proration policy: add the 60% floor.
- [ ] Build the HOS Health Check (SAFER + SMS carrier profile). Manual is fine at this stage. **Lead with counts and violation codes, not percentiles** — see `assets/health-check-build-guide.md`.
- [ ] Hire 1 bilingual supervisor (RO/RU/EN) for the 24/7 roster; produce the English driver-facing collateral set; set up the translation pipeline for on-request languages.
- [ ] **Since we have no publishable track record:** design the monthly report and the pilot measurement so our own outcome evidence is collected from account one. The baseline is the carrier's own FMCSA record, pulled before engagement. This is the top delivery priority of the 90 days.
- [ ] Build the pilot offer, the SLA sheet, the authorization form, the pricing tiers.
- [ ] **Instrument the request-volume count from day one** — requests per truck per week by class. The labour model rests on one unverified number (~6 logs/truck/month). See `RISKS.md` §14.
- [ ] Legal checks on the partners' prior-employer obligations.
- [ ] Cross-border tax + entity advice: W-8BEN-E, US invoicing, whether a US LLC is needed for banking/insurance only, and the buyer's use-tax position. Keep the contracting entity offshore to avoid creating US nexus.
- [ ] Download the FMCSA Pocket Guide 2024 PDF and the census file; build the target list; open the SMS Appendix A violations list.

### Days 15–45 — Proof
- [ ] 3–5 friendly fleets from the partners' network, on paid pilots (business-hours SLA, flat fee).
- [ ] Baseline their FMCSA records, response times, correction turnaround, and driver feedback **before** we touch anything.
- [ ] Run the first 10 fleet-owner interviews and 2 dispatcher interviews (`research/interview-guides.md`). **Willingness to pay at $130 and the real request volume are the two things research could not settle.**
- [ ] Fix the SOP from real pilot cases.

### Days 40–90 — Repeatable motion
- [ ] 3 insurance-agent conversations; 2 ELD-reseller conversations.
- [ ] Publish the driver-facing HOS material (English, then translated on request); start the driver-group push.
- [ ] 50–100 Health Checks sent/week; measure conversation → meeting → pilot → close.
- [ ] First case study written from pilot data.

### 90-day targets
| Metric | Target |
|---|---|
| Pilots running | 5 |
| Pilot → contract conversion | ≥ 60% |
| Trucks live | 25-40 |
| Pre-engagement baseline captured | 100% of managed fleets (day 1 of onboarding) |
| Corrections with a source document attached | 100% of Class 2 |
| Requests answered inside the SLA | ≥ 95% |
| Avg response time | < 10 min, 24/7 |
| Conversations/week (owner-level) | 15-20 |
| Own evidence base (managed fleets with a documented pre/post baseline) | 3 by day 90 |
| Insurance-agent relationships with a referral in progress | 2 |
| Cost per closed fleet | < $3,500 |

---

## 10. Metrics dashboard — review weekly

**Commercial:** trucks live (total and by tier) · new trucks added per month · monthly logo churn and truck churn · ARPA/truck · pipeline by stage · conversion at each stage · CAC/truck · payback months.
**Service:** requests per 1,000 trucks/week · median and p95 response time · % requests resolved within SLA · corrections by class (typographical / document-supported / disputed / refused) · % RODS reconciled without driver escalation · document turnaround time.
**Outcome:** violations and citations in managed fleets vs. their own pre-engagement baseline · `HOS Compliance` and `Unsafe Driving` percentile movement · repeat-violation rate.
**Operational:** cases per FTE per day · overtime hours · staff attrition · driver certification currency %.

**One rule:** every number in the outcome block is reported per managed fleet and in aggregate, with the baseline stated. It is the sales asset, and it only stays an asset if it is accurate and consistently measured.

---

## 11. Open items for the partners
1. Confirm which ELD platforms the team can access and how (own accounts, customer-provided API tokens, or reseller-provided) — this determines the data model.
2. Confirm the actual number of requests per truck per week in the pilot — it drives FTE count and is the single number the 24/7 promise rests on.
3. The 18-month record is NDA-locked. Confirm with counsel whether the partners may serve as **personal references** (without disclosing the former employer's data) and whether the methodology can be described in general terms. Neither substitutes for our own evidence, but both strengthen the first three conversations.
4. Decide: do we edit the ELD or prepare corrections for the driver to make? **Recommend: prepare only** (§2). This is a decision, not a detail.
5. Decide the invoice entity, the tax position, and who signs the E&O application.
