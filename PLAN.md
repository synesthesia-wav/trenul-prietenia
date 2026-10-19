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
| 14 days of records not available in the ELD (395.8(b)(1)) | Administrative | ~$0 |
| No documented explanation for an edit (395.8(e)(4)(ii)) | Documentation | 20 min |
| HOS violation (11-hr / 14-hr / 60-hr) | Driver behavior + planning | Coaching |
| Pre-trip / DVIR and vehicle maintenance gaps | Carrier, not us | — |

**Only the fifth is behavior.** The first four are documentation hygiene, and they are the bulk of what produces a bad `HOS Compliance BASIC` percentile. This matters: a service that sells only "we stop HOS violations" is selling something that depends on driver honesty. A service that sells "your paperwork is defensible and your certification is current" is selling something the vendor controls.

**Consequence for the pitch:** lead with audit-defensibility and paperwork integrity, not with "fewer violations." Violation prevention is the *outcome evidence*; paperwork is the *deliverable*.

---

## 2. Product design — the "we do not touch your ELD" principle

**The single most important structural decision in this business.**

Under 49 CFR 395.8(e)(4)(ii), the driver — not a vendor — makes entries in the ELD, and every edit is recorded in an edit history that FMCSA can retrieve. A vendor editing a driver's ELD creates a permanent record in the driver's file of a third party touching federal records, and the carrier's insurance does not care who had good intentions.

So the model is:

1. **Driver or carrier requests** a correction.
2. **We** research source documents (BOL, rate con, GPS/stop trace, dispatch record, fuel-card, scale tickets) and prepare the proposed correction, each one attached to its source document.
3. **The driver (or an authorized carrier official) makes the actual entry** and signs off — a 30-second action in the ELD app or on the paper RODS.
4. **We** retain the evidence pack and the audit trail, and produce it on demand to FMCSA, the carrier, or the carrier's insurance company.

Result: we never edit a federal record. We produce the *documented, defensible* basis for a correction the driver is entitled to make. This is the lawful version of the service, it is insurable, and — as a sales point — it is stronger than a competitor's, because a competitor who edits for you cannot hand an inspector a clean trail.

**Rule of construction for the SOP:** every correction is classified before it is proposed.

| Class | Definition | Action |
|---|---|---|
| Typographical | Genuine typo (395.8(e)(4)(ii) exception) | Driver corrects; logged |
| Document-supported | Reconstructable from shipping papers / actual events within 14 days | We prepare the evidence pack; driver enters |
| Disputed | Documents and driver account conflict | We do **not** propose a correction; escalate to the carrier |
| Out of scope | Requires reconstruction of hours not actually driven | **Refuse, always, and log the refusal** |

Class 4 is written into the SOP, the training, and the contract. It is a control, not a formality — it is also the answer to the E&O underwriter and to any carrier's risk manager.

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

### The $80 anchor — and why we do not fight it on price

The competing offshore price is confirmed at **$80 per truck per month**. Ours is $130. On a 25-truck fleet that is a **$15,000 annual gap**, and the buyer will frame it as a $15,000 question.

**Never answer that gap by defending the price.** Answer it by pricing the *alternatives the owner already has*: an in-house compliance manager ($70–100k/yr), an annual FMCSA compliance audit ($2–6k/fleet), a lawyer for a violation ($1.5–4k), and one HOS out-of-service citation with its insurance consequence. Then let three questions do the work against the incumbent: *who is accountable for a correction, what is the response time at 2am on a Sunday, and can they hand an inspector a document for every change they made?*

**Structurally, $80 is the right number for a monitoring desk and $130 is the right number for a staffed compliance desk.** We are not trying to be cheaper than an $80 provider. We are a different product: a named accountable human on 24/7, document-verified corrections with an evidence pack, an inspection-ready file, and a monthly report on the carrier's own numbers. If a carrier can get all of that at $80, we should not have won the deal.

---

## 4. Segments — ranked by profitability per unit of selling effort

### Tier 1 — Beachhead: fleets that already got hurt
- 5–50 power units, active authority, one or more HOS/RODS violations or citations in 24 months, or a poor `HOS Compliance BASIC` percentile.
- **Why:** they have a budget line and a deadline, the health-check report is directly actionable, and the sales conversation is about *their* problem, not our product.
- **Our offer:** free HOS Health Check → paid pilot → monthly.
- **Note on metric naming:** hours violations land in the **Unsafe Driving** BASIC; record-of-duty-status violations (395.3(e)(4)(ii)) land in the **HOS Compliance** BASIC. Use the carrier's own SAFER numbers and always pull the current methodology — SMS components have been revised more than once. Never quote a percentile from memory.

### Tier 2 — Non-English-speaking owner and driver populations (a reach segment, not a language wedge)
- Chicago, Houston, Dallas–Fort Worth, New Jersey/New York, Atlanta, Detroit–Dearborn, and metros with large immigrant-owned trucking communities (Arabic, Spanish, Russian, Romanian, and others). The team works in RO/RU/EN, so the differentiator here must be **document verification and the inspection file, not language**.
- **What is possible without native-speaker staff:**
  - Serving a non-English owner is fully possible: the owner-facing conversation is document- and outcome-driven, and the correction is prepared in writing for the driver to sign, so the driver needs no language to comply with it.
  - Coaching a driver well in a language we do not speak is not possible. That caps the violation-prevention half of the value for non-English crews, and means our own outcome data for this segment will be weaker than for English-speaking crews. **Know this internally, and do not over-promise prevention in the sales pitch for this segment.**
- **The cheap fix:** translated driver-facing material (HOS cheat-sheet, certification reminders, break-discipline card) is a translation task, not a staffing decision. English first; translated versions on request from the fleet; use them as the referral engine. Near-zero cost, real benefit.
- **Quantify before betting on it:** build the segment from FMCSA census data (§7) before treating it as a beachhead. If it is a genuine concentration of 5–50 truck fleets, it is worth a translated-material line — not a native-speaker hire.

### Tier 3 — Expansion: all SMB fleets, 5–50 trucks
- Large, contested by Motive/Samsara and offshore vendors. Enter via the ELD-vendor resellers and insurance channels, not cold calls.

### Explicit non-targets
- Fleets under 5 trucks (account too small to carry 24/7 cost against — see §5).
- Large fleets (100+ trucks): they have in-house compliance staff and will run a procurement process that will eat the team.

---

## 5. Unit economics and the 24/7 decision

Fully-loaded cost per seat in Moldova for a support specialist: budget **$900–1,300/month** (salary $700–1,000 + employer contributions). 24/7 coverage needs 3 shifts × 8h with a ~1.5 relief factor → **4.5–6 FTE**, plus 1 bilingual supervisor. For 200 trucks at 40–60 min/truck/week of monitoring and document verification, plan on **6–8 FTE**.

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
- [ ] Write the correction protocol and the 4-class SOP; have a US transportation attorney review it (this is also the E&O underwriting package).
- [ ] Fix the proration policy: add the 60% floor.
- [ ] Build the HOS Health Check (pull SAFER data, produce the 1-page report). Manual is fine at this stage.
- [ ] Hire 1 bilingual supervisor (RO/RU/EN) for the 24/7 roster; produce the English driver-facing collateral set; set up the translation pipeline for on-request languages.
- [ ] **Since we have no publishable track record:** design the monthly report and the pilot measurement so our own outcome evidence is collected from account one. The baseline is the carrier's own FMCSA record, pulled before engagement. This is the top delivery priority of the 90 days.
- [ ] Build the pilot offer, the SLA sheet, the BAA/authorization form, the pricing tiers.
- [ ] Legal checks on the partners' prior-employer obligations.
- [ ] Cross-border tax + entity advice: W-8BEN-E, US invoicing, whether a US LLC is needed for banking/insurance only, and the buyer's use-tax position. Keep the contracting entity offshore to avoid creating US nexus.

### Days 15–45 — Proof
- [ ] 3–5 friendly fleets from the partners' network, on paid pilots (business-hours SLA, flat fee).
- [ ] Baseline their SAFER numbers, response times, correction turnaround, and driver feedback **before** we touch anything.
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
