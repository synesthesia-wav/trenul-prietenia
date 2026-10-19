# Risk Register

Ranked by expected cost. Each entry: the risk, why it bites, the mitigation, and the owner.

---

## 1. Regulatory / criminal — the risk that ends the business

**Risk.** Corrections that are not supported by source documents amount to falsification of records of duty status required under 49 U.S.C. § 31502, and can be criminal under 18 U.S.C. § 1001. Under 49 U.S.C. § 521(h), anyone who "knowingly and willfully violates" the hours-of-service and recordkeeping provisions is, upon conviction, subject for each offense to a fine not to exceed $25,000 or imprisonment not to exceed one year (doubled for a subsequent offense). Separately, FMCSA rates 49 CFR 390.35 — "Making, or causing to make fraudulent or intentionally false statements or records and/or reproducing fraudulent records" — as an **acute** violation in the safety rating process (49 CFR Part 385, Appendix B), meaning it can drive an unsatisfactory safety rating on its own. ELD edit histories are permanent and retrievable by FMCSA. It also voids the carrier's insurance for any loss tied to the falsified hours, and the carrier — also a criminal actor in that scenario — is the least likely party to complain, which is exactly what makes it a business that can grow until one inspection, one claim, or one criminal referral unwinds it.

**Why it bites.** "Only what documents support" is a *practice*, not a *policy*. It erodes under deadline pressure, under a loud carrier owner, and under a commission structure that rewards outcomes rather than process. A single fabrication discovered in an ELD edit history is exhibit A.

**Mitigation.**
- The 4-class correction SOP in `PLAN.md` §2 and `assets/hos-rods-reconciliation-checklist.md` §0, with Class 4 (unsupported reconstruction) as a mandatory logged refusal.
- **We never edit the ELD.** 395.8(f)(2): "All entries relating to a driver's duty status must be legible and made by the driver." 395.30(f) forbids altering or erasing originals. Appendix A § 4.3.2.8(b) requires the device to prevent it. We propose in the carrier's support-personnel account (395.22(b)); the driver confirms, enters and recertifies (395.30(d)(1)).
- **Never instruct, only ask.** 395.30(e) prohibits coercing a false certification. We request; the driver decides.
- **A proposed edit is not a draft.** Per FMCSA Q5, if the driver is unavailable or unwilling to recertify, the proposed edit and annotation *remain part of the record*. Every correction we propose must be one we would defend on its merits. This is a design constraint, not a footnote.
- The refusal log is retained and auditable. Review it monthly. A rising refusal count is a healthy sign, not a problem.
- US transportation attorney's written opinion on the SOP before the first commercial contract.
- The E&O underwriter reads the SOP. A carrier that declines to write because of the SOP is the most valuable feedback available.
- If a carrier asks us to break the rule: end the relationship, not just the contract. Never renegotiate it.

**Owner.** Partner #1 (SOP) + US attorney (opinion) + owner (logged refusals, reviewed monthly).

**What the research changed (2026-10-19) — three material updates, all verified against the current CFR:**

1. **The rule I had been citing is wrong, and the correct rule is better for us.** `395.8(e)(4)(ii)` does not exist in the current CFR — it was withdrawn by the November 2023 technical-corrections rule (89 FR 712, eff. 2024-01-05). The operative provisions are **395.30(d)**, which expressly permits the motor carrier to request edits with the driver confirming, rejecting, entering and recertifying, and 395.30(d)(3), which requires exactly that for "any system or any person other than the driver." **Our product is the regulation's own model.** This turns the risk section from a defence into a selling point: we are not hiding from the rule, we are the rule's workflow, and an attorney packet can say so in one paragraph.
2. **The criminal exposure lands on the carrier owner, not on us** — provided we do not alter the record. *United States v. Sisic* (D.R.I., Crim. No. 20-63MSM): the owner of an **11-truck** carrier altered thousands of ELD entries for ~20 drivers to conceal driving and on-duty time; one driver died in an April 22, 2018 Oklahoma crash; guilty plea to conspiracy to falsify records (18 U.S.C. § 371) on Oct 14, 2020; **sentenced Jan 25, 2021 to three years' probation including six months' home incarceration with electronic monitoring, 50 hours' community service, a $1,000 fine and a $100 special assessment**; **FMCSA suspended and proposed a three-year debarment on Apr 29, 2021 and debarred him on Aug 19, 2021**; company defunct. *(Corrected 2026-10-20 — earlier drafts said "18 months, $50,000", which was the prosecution's sentencing recommendation, not the judgment. See `research/RESEARCH-LOG.md` §1.4.)* Also: *Belovs* (E.D. Pa. 2012, 15 counts, fatal crash, 18 months), *McClafferty* (E.D. Pa. 2003, 10 counts; six drivers plus the dispatcher and the company indicted), Nijjar Brothers (Cal., 13 drivers), and a 126-count Virginia indictment that added **wire fraud** (which is why our documented-correction standard is not optional). **Sisic is our target customer** — small fleet, owner-operated, an ELD and no compliance function. That is the strongest available evidence that the problem is real and that the current "solution" is to lie.
3. **The device blocks part of the evasion.** Appendix A § 4.3.2.8.2(b) bars shortening automatically recorded driving time, and FMCSA's Q7 confirms driving time "cannot be edited or changed to non-driving time." The classic hours-shortening evasion is not merely illegal, it is technically blocked. Class 4 is therefore aligned with the regulation rather than stricter than it, and we can say so.

**Open verification items — do not cite until confirmed.** The current paragraph for the 14-day ELD records-availability requirement, and the text of 395.3(e)(4). Both appeared in earlier drafts; neither could be located in the current CFR text during the 2026-10-19 research. See `research/RESEARCH-LOG.md` §1.3.

---

## 2. No publishable track record (confirmed constraint)

**Risk.** The partners' 18-month, zero-negative-inspection record is under NDA: it cannot be opened, quoted, or published. **We therefore have no track record of our own to show a buyer.** This is not a risk to mitigate — it is a condition to plan around, and it shapes the first six months more than any other factor in this register.

**Why it bites.** In a first sales conversation, a proven track record is the shortest route to trust. Without one, the entire burden of proof falls on the Health Check (our credibility), the SLA (our commitment), and the evidence pack (our process). It also raises CAC and lengthens the cycle, and it means the first three pilots are not revenue — they are the reference base the whole company will be sold on.

**Mitigation.**
- **Lead with process, never with claimed outcomes.** The Health Check on the carrier's own public data, the 4-class SOP, the evidence-pack template, the correction log, and the monthly report are the proof assets. They are demonstrable in a meeting in a way a claim is not.
- **Generate our own evidence from day one.** Every fleet gets a pre-engagement baseline pulled from FMCSA data on day 1 of onboarding, and a documented comparison at 90 days. Make the monthly report template collect it at no extra cost. Target: three fleets with a documented pre/post baseline by day 90.
- **Ask counsel** whether the partners may serve as personal references without disclosing the former employer's data, and whether the methodology can be described in general terms. Neither substitutes for our own evidence; both help in the first three conversations.
- **Do not let anyone fill the gap with a proxy.** No "we used to do this for a large provider" without a written, lawyer-cleared formulation. An implied claim that cannot be substantiated is a misrepresentation, and a carrier that discovers it is a churn event plus a bad review.
- **Budget for the slow start.** Year-one plan should assume low close rates and price accordingly; the model in `PLAN.md` §5 depends on volume, so the volume has to come from somewhere else in the early months (agents, resellers, the partners' warm network).

**Owner.** Owner (baseline capture discipline) + compliance lead (monthly report evidence).

---

## 3. Insurance and structural capacity — you cannot sell to US fleets without it

**Risk.** US carriers will require a certificate of insurance (typically $1M GL, $1M E&O, cyber), a W-9/W-8BEN-E, US-domain invoicing, and a contractual liability position. A Moldova-domiciled operation is hard to place with US carriers for E&O and may not be able to open a US business bank account without a US entity.

**Why it bites.** "We have no US entity, bank, or insurance" is not paperwork — for a *legitimate* service it is achievable, and the absence of it is a hard blocker on Tier-1 and Tier-2 carriers and on any insurance-agent channel. The broker channel cannot open without a COI.

**Mitigation.**
- US LLC (Delaware or Wyoming) used **only** for contracting, banking, and insurance — not for operations, to avoid creating US tax nexus. Confirm with a cross-border tax advisor; get the W-8BEN-E and the buyer's use-tax position settled in writing.
- E&O and cyber placement: approach US brokers; the E&O underwriting is the natural place to have the SOP reviewed (§1). If the placement requires a US entity and US-resident claims handling, budget for it.
- Liability: cap it, and separate it from the SLA. The SLA warrants *process* (response time, coverage hours, documentation completeness, source-document attachment). The service credit for a miss should be a month of fees, not the cost of a citation. Never warrant an inspection outcome.
- Data processing: the drivers' HOS data is PII and a regulated record. Encrypt at rest and in transit, role-based access, defined retention, and a documented process to produce records on legal demand.

**Owner.** Partner #2 + US broker + outside counsel.

---

## 4. Data access and ELD platform dependency

**Risk.** We need each fleet's ELD data to do anything. Options are the carrier's own account, a reseller-provided integration, or a third-party ELD. Each has a dependency, a term-of-service constraint on third-party access, and a failure mode if a vendor changes its API.

**Why it bites.** Every external dependency is a single point of failure for 100% of revenue, and API changes happen without notice.

**Mitigation.**
- Support at least two data sources from day one (own ELD + one platform integration), and design the correction log to be platform-agnostic.
- Do not depend on a white-label reseller for data access; take the customer relationship on the ELD platform directly even if the reseller owns the sale.
- Own the data: the evidence pack, the correction log, and the monthly report live in our own system, not in the ELD vendor's UI. If the ELD vendor changes, we can re-attach the fleet; if we only hold a link, we cannot.
- Contract for the access: written authorization from the carrier, and confirmation of the platform's terms on third-party monitoring.

**Owner.** Partner #1 (technical) + delivery lead.

---

## 5. Concentration — 24/7 cost with no volume

**Risk.** Breakeven is roughly 60–85 trucks against a fixed shift roster. Below that, the 24/7 promise consumes the whole company, and one lost contract or one idle month turns gross profit negative.

**Why it bites.** A shift roster is a fixed cost from the first day. The business's entire earnings are the difference between the roster and the truck count.

**Mitigation.**
- Target 200–300 trucks within 24 months; treat the truck count, not the logo count, as the primary metric.
- Minimum 10 trucks per account; tiered pricing so sub-10-truck fleets pay for the fixed cost (§ PLAN.md §5).
- The proration floor (60% of contracted power units) is non-negotiable — otherwise seasonal fleets transfer their fixed cost to us.
- Staged hiring: 3 FTE covers the first ~60 trucks; add the 4th only against contracted revenue, not forecast revenue.
- If the roster is not full 24/7 early on, publish real coverage hours in the SLA rather than over-promising. 24/7 is a differentiator at 200 trucks and a liability at 40.

**Owner.** Owner (hiring gates) + Partner #2 (roster).

---

## 6. Prior-employer obligations and the 18-month claim

**Risk.** The partners' ELD experience, SOP knowledge, and contact list may be encumbered by non-solicitation, confidentiality, or trade-secret obligations owed to their former employers. The 18-month inspection record is separately closed to us under NDA.

**Why it bites.** A prior employer who believes its client list or proprietary methodology was taken can do real damage — a claim, a demand, an injunction threat, or a letter to the carriers that poisons the pipeline. The 18-month inspection record is confirmed to be under NDA and is not publishable, so the partners' experience can only ever be demonstrated indirectly, through process and references.

**Mitigation.**
- Legal review of the partners' employment agreements **before** the first outbound call.
- Do not use a former employer's client list. Rebuild the list from FMCSA census data and from referrals the partners obtained personally.
- The 18-month record is closed to us: do not open it, do not quote it, do not describe its contents. Ask counsel instead whether the partners may serve as personal references and whether the general methodology can be described in the abstract.
- Publish only evidence we generate ourselves (see Risk 2).
- Do not publish competitor-specific comparisons in writing (see Risk 7).

**Owner.** Owner + outside counsel.

---

## 7. Legal exposure from the marketing material itself

**Risk.** The current comparison document invites a written comparison against competitors, including — given the partners' history — their former employers. Disparaging an identifiable competitor, or reproducing their internal practices, is a claim waiting to happen.

**Mitigation.**
- Rewritten as "what to ask any ELD provider" — a buyer-facing checklist with our answers, not a scorecard of named rivals' failures.
- No competitor names, no claims about what competitors do or don't do, no reproduction of anyone's internal methodology.
- Every outcome claim carries a definition, a denominator, and a date, and is drawn only from fleets we manage (e.g. "0 HOS-related violations across 14 inspections on 4 fleets, 18 months, as of March 2026"). Until we have our own evidence, there are no outcome claims to make.
- Never warrant an inspection outcome. Warranty language only for service levels we control.
- Have counsel review every customer-facing document before it goes out. This is a small cost against an uninsurable claim.

**Owner.** Owner (drafting) + counsel (review).

---

## 8. Key-person dependency

**Risk.** The partners *are* the delivery team and the domain knowledge. If one leaves, the SOP and the credibility leave with them — and in a service business, the SOP is the product.

**Mitigation.**
- The 4-class SOP, the correction log schema, and the evidence-pack template are written and versioned from day one, not held in someone's head.
- Language-specific delivery capability must not live in one person: where we serve a segment in a specific language, have two people able to handle it before relying on it.
- Document the state-rules matrix with a named owner and a monthly update cadence — it is a subscription asset, not a founder's memory.
- Key-person insurance and a written non-solicitation/retention agreement with each partner.

**Owner.** Partner #1 + delivery lead.

---

## 9. Carrier-side liability and expectation management

**Risk.** A carrier gets a citation during our engagement and blames us, or demands we cover the fine, or claims we represented that their record was clean.

**Mitigation.**
- Contracts state: we warrant *process and response*, not inspection outcomes. Service credits, not outcome warranties.
- Written scope: what is included, what is excluded (we do not do dispatch, drug/alcohol programs, DVIRs, vehicle maintenance, or legal representation — we prepare evidence, their attorney represents them).
- The monthly report shows our work continuously, so a miss is a visible process gap, not a surprise.
- Annual E&O and cyber certificates renewed and on file before renewal season, and a renewal-notification process so no client lapses uninsured.

**Owner.** Owner (contract) + delivery lead (reporting).

---

## 10. Concentration in one channel

**Risk.** An agent or reseller relationship that produces most of the trucks creates dependency on a person we do not control, who can also take the playbook to a competitor.

**Mitigation.**
- No single channel above 35% of trucks. Track by source every month.
- The Health Check, the driver-facing content, and the white-label channel are three independent engines; all three must be live by month 6.
- Channel partners get a referral or margin, not the playbook and not the accounts. The customer relationship stays ours where possible.

**Owner.** Owner.

---

## 11. Reporting inaccuracy

**Risk.** Benchmarks, percentiles, and violation rates quoted from memory rather than pulled. One wrong percentile in front of a fleet owner who knows their own record, and we lose the account and the referral.

**Mitigation.**
- Every report carries a pull date and a source. Percentiles are pulled, never recalled; FMCSA SMS methodology changes and must be re-verified before each campaign.
- The report is generated from a checklist, not from memory. Two-person check on anything quoted externally.
- When the record is clean, say so. No manufactured problems.
- **New (2026-10-19):** where a percentile is not assignable, say so rather than showing 0. FMCSA requires at least three driver inspections with violations before a carrier is assigned a percentile above zero in the HOS category, so for a small fleet there often is none. "No score because nobody has looked" is a finding; "score of 0" is a false reassurance and, if the owner checks SAFER and finds nothing assigned, it is a credibility failure.
- **New (2026-10-19):** every violation code and severity weight is read off the current SMS Appendix A at the time of the report, not recalled. The codes and weights are in `assets/health-check-build-guide.md` §3 as a working order, not as a static table.

**Owner.** Owner (report templates) + delivery lead (QA).

---

## 12. Price position — the market is denser than we assumed

**Risk.** Published research (2026-10-19) shows the market we are entering is far more crowded and far cheaper than our plan assumed. The US managed-compliance band runs **$25–65 per truck per month** (Trucking Hub $29, Trucking Comply from $25, TruckingMBA $50–65, TenFour $38–99 per driver) and the offshore ELD-monitoring band runs **$60–80** (Turbo ELD, from $2/day per truck). Our $130 is roughly 2x the automation tier and ~2.2x the offshore anchor. It only defends against the staffed-HOS-desk tier (Prime Fleet Management, $60–250 per truck), where the buyer is comparing us to a full outsourced compliance department.

**Why it bites.** A price that is 2x the cheapest credible alternative needs a reason the buyer can state to himself, and we have no published track record to supply that reason. Worse, the crowded low end could absorb our target segment: a 15-truck owner with a $29 software bundle and free FMCSA training has a perfectly reasonable cheaper answer. If we sell on price we lose; if we sell on quality and have no track record, we lose to the same buyer.

**Mitigation.**
- **Narrow the segment and hold the floor.** 15–75 truck fleets with a live hours-of-service problem. 10-truck minimum. Say no to smaller, and say no to fleets with clean records.
- **Differentiate on the two things nobody in the comparison set foregrounds:** the audit-ready source-documented correction file, and a 24/7 response line with a named accountable human. Note that Turbo ELD advertises "auto-certify logbooks" — a claim that sits uneasily with 395.30(b)(1)–(2) and 395.8(f)(2). We do not make it, and we can quietly be the compliant alternative.
- **Never run a price comparison.** Use the buyer's alternatives (in-house compliance manager at $180–350k/yr per Prime Fleet's own published comparison; an audit at $2–6k; a lawyer at $1.5–4k; one citation and its insurance consequence) and the Sisic case.
- **Do not sell training or generic guidance.** FMCSA gives it away free. That caps the knowledge component of the price and forces the value onto execution.
- **Watch the two closest competitors specifically** — Prime Fleet Management (structurally identical, same free-assessment lead magnet) and Turbo ELD (the $60 anchor, already multilingual). If either moves price materially, re-run the tiering.
- **Track this in the quarterly review.** A price ladder that has moved against us is a signal to re-tier, not to discount.

**Owner.** Owner (pricing and tiering) + partner #2 (competitive watch).

---

## 13. Metric obsolescence — our own reporting asset can be invalidated

**Risk.** FMCSA is actively reorganising the Safety Measurement System: BASICs are becoming "compliance categories," Controlled Substances/Alcohol and operating-while-OOS violations are moving into Unsafe Driving, and data-sufficiency standards are changing. The Health Check, the monthly report and the quarterly renewal conversation are all built on SMS outputs. If FMCSA changes or retires a metric we report, the report stops being authoritative — and a compliance report that cites a retired metric reads as amateur to exactly the audience we need to impress.

**Why it bites.** We have no track record and no brand. Our credibility is entirely "we know your record precisely." A stale methodology citation is the one error that undermines everything else we do, because the buyer can check it in five minutes.

**Mitigation.**
- The Health Check now leads with **counts and violation codes**, not percentiles. Counts survive a methodology change; percentiles and category names do not.
- Re-download the SMS Methodology and Appendix A violations list before every campaign, and record the version on the report. The report already carries a methodology-version line for this reason.
- Never hard-code a category name in customer-facing material. Read the label off the current page.
- Assign an owner to watch FMCSA's rulemaking and methodology notices, and to reissue the template when anything changes.
- The same applies to state rules (row 6 of the checklist): the matrix needs a named owner and a monthly update cadence, or it becomes a liability.

**Owner.** Compliance lead (template and method) + delivery lead (version stamp).

---

## 14. Dependence on an unproven labour model

**Risk.** The entire 24/7 model rests on one unverified number: about **6 unverified logs per truck per month**. The only source is a vendor's fleet calculator (ZenduELD) — grade C, a model assumption, not evidence. No published staffing-ratio study for outsourced ELD/log desks was found. If the real figure is 3x higher, the labour model breaks and $130/truck/month becomes impossible; if it is 3x lower, we are badly overpriced and the whole segment changes.

**Why it bites.** The number determines FTE per 100 trucks, the 60–85 truck breakeven, the price floor and the tiering. Everything downstream inherits its error.

**Mitigation.**
- **Instrument the pilot from day one.** Count requests per truck per week by class, with the class mix. This is the first thing we measure, not a later refinement.
- Build a second, independent estimate before the pilot: what comparable services claim (Prime Fleet implies daily monitoring), and what dispatchers say the real rate is (the interview guide, §D).
- Model the business at 6, at 12 and at 18 logs/truck/month, and know which of the three we can survive.
- Staff in stages against contracted trucks, not forecast trucks, so the roster never runs ahead of the revenue.
- The cheapest structural protection is automation of the *monitoring* sweep (exception detection off the ELD feed) while keeping humans on the document reconciliation. That is not "building software" in the sense the partners object to; it is a rules engine over an existing feed, and it is the only way the 24/7 promise survives at 200 trucks.

**Owner.** Delivery lead (measurement) + owner (staffing gates).

---

## 15. The refusal log is discoverable as an admission (new, 2026-10-20)

**Risk.** The refusal log is, on the strategy panel's agreement, the single strongest asset we have: it is the only thing a competitor cannot ship, and it is the artefact that makes us credible without a track record. It is also a **written record that the carrier asked us to make a correction the paperwork did not support.** Read by a carrier's own attorney, or produced in a civil discovery, it could look like a written confession that the fleet was seeking falsification — and it would be the single most damaging document in the file.

**Why it bites.** We are simultaneously (a) planning to publish it as marketing and (b) building the business on the premise that the file is what an inspector, an insurer or a plaintiff's lawyer will read. Those two uses collide. A document that is safe to publish is not necessarily safe to produce, and vice versa. Nobody in the project has asked an attorney this question.

**Mitigation.**
- **Get the answer before we publish anything.** US counsel must advise: is a logged refusal exculpatory, or an admission? Until then, the log is internal only, and the *published* form of the SOP describes the refusal **rule** without shipping the log itself.
- **Scope the wording to process, not intent.** "We did not propose a change because the documents did not support one" is a statement about our method. "The carrier asked us to conceal hours" is a statement about the carrier's intent, and is a gift to the other side. The schema must make the first form the only easy one to write.
- **Never write down a requester's intent, a motive, or a name beyond the minimum needed.** The log records: the request, the documents reviewed, the classification, the reason for the classification, who was notified, and the date. It does not record what we think the requester wanted.
- **Retention and access controls**: the log is part of the file, produced only in response to a lawful request or an insurance/attorney request, and shared with the carrier by default so there is no hidden second copy.
- **Sequence**: publish the SOP page first (a method, which is safe), and the log format later, once counsel has cleared it. The moat is the *behaviour*, and the behaviour is what takes 90 days to build; the publication can wait.

**Owner.** Partner #1 (schema) + US attorney (opinion) + owner (publication decision).

---

## 16. The category is commoditising from both ends (new, 2026-10-20)

**Risk.** Two platforms are building the layer we are selling, and one of them has already shipped the workflow.

- **Samsara launched "Smart Compliance" on 2026-04-21** — "we review yesterday's, deal with them immediately, and send them straight to the driver digitally... it takes about two minutes per infringement." That is our desk, automated, with proactive pre-infringement audio alerts. **EU and UK only as of launch; US availability unconfirmed.** It is the single biggest threat to the standing SKU, and the clock on the whole strategy.
- **Motive shipped AI driver-qualification document management in February 2026**, citing FMCSA audit data on missing and outdated documents in driver files. Motive also offers "Qualification Documents Expert Services."
- **DotFleet Compliance** already occupies the adjacent specialist niche with published per-driver pricing ($75 one-time, $30/driver/month), fully remote, all 50 states — and explicitly refuses HOS and ELDs, pointing its own buyers at us.
- **AI ELD** sells a $50/vehicle/month tier with a human team that resolves events "within minutes," month-to-month, no minimum.

**Why it bites.** Our differentiator was always going to be the document. If the platforms make the document, the file becomes a feature, and a feature is a $25-65 line item on someone else's invoice. The window is measured in quarters, not years.

**Mitigation.**
- **Watch Samsara's US launch as the primary external deadline.** No public statement found; check Samsara's US product pages and investor materials quarterly and set a hard internal date at which we re-evaluate the standing SKU.
- **Do not compete on the ELD platform's own ground.** We are ELD-neutral; that is an asset, and it is also the thing a platform cannot copy without cannibalising their own ELD revenue.
- **Lead with the New Entrant audit-prep event** (Tier 0). It is a document-assembly job with an external deadline, it is not what a platform's real-time dashboard does, and it is a one-off rather than a subscription a platform can bundle.
- **Build the two assets a platform cannot copy quickly**: per-fleet exception-pattern knowledge, and the broker's renewal data. Both are outside the ELD data stream.
- **Assume the standing SKU has a 24-month shelf** and make the event SKU and the broker relationship the durable parts of the business.

**Owner.** Partner #2 (competitive watch) + owner (platform strategy).

---

## 17. The "New Entrant" beachhead may be a small, poor, and shrinking pool (new, 2026-10-20)

**Risk.** Tier 0 is the strongest-looking segment we found, and it is the newest, least validated idea in the plan. Three ways it could disappoint:
- **56% of New Entrant exits are "inactive, change, no show at the safety audit, no contact."** The population contains a large share of carriers who will not pay for anything.
- **The failures are small carriers.** A 1-3 truck carrier that fails its safety audit has a catastrophic downside and almost no budget. The two facts are in tension: the deadline is strongest where the budget is weakest.
- **FMCSA's own data says the failure rate is 7.4-11.8%, not the "one in three" that vendor blogs claim.** At 8.7% of 58,600 audits, the addressable pool is ~5,100 carriers a year, of which only a fraction will both pay and be reachable.
- And a risk nobody has checked: **the audit can be conducted electronically, which is what makes the offshore model viable — but it also means the work is document assembly, which is exactly what a $29 software bundle or a $30/driver specialist could do.**

**Why it bites.** We are making this the first thing we sell, on the basis of one research session, before a single customer conversation. If the pool is thin or the willingness to pay is near zero, we burn the first 90 days on a segment that cannot carry the business.

**Mitigation.**
- **Treat the 90-day target as a test, not a plan: 2 New Entrant engagements sold.** If we cannot sell two in 45 days, the segment is wrong and we fall back to Tier 1 (dated-event fleets) without further argument.
- **Price the event, not the fleet** ($1,500-4,000), because a 2-truck carrier cannot pay a per-truck retainer but a business facing revocation of its registration can pay for a professional to assemble the file.
- **The audit is a one-off; the retainer has to come from somewhere else.** Assume a New Entrant engagement is a customer-acquisition event whose real value is proving the file works, not a revenue engine. Do not build the plan on its recurring revenue.
- **Verify the pool from FMCSA's own data** (the census file and the New Entrant statistics) before scaling: how many carriers fail, in which states, and how many of those are in states where enforcement is active.
- **Do not repeat the "one in three fail" claim** — it is a grade-C vendor figure contradicted by FMCSA's 8.7%.

**Owner.** Partner #1 (delivery) + owner (segment test) + requester (interviews).

---

## 18. The specialist competitor is closer than we modelled (new, 2026-10-20)

**Risk.** DotFleet Compliance is not a distant competitor in a different segment. It is a **remote, single-regulation, published-price, per-driver, 100%-remote compliance desk for fleets of 1-50 trucks** — our exact operational shape — with a free file review as its magnet, Mon-Fri 8am-6pm CT coverage, and a one-business-day response promise. It also refuses HOS explicitly, which is our opening, but it demonstrates that the shape works and that a well-positioned specialist in this market publishes two prices and nothing else.

**Why it bites.** We had classified the $25-65 tier as software and the $60 tier as offshore monitoring. DotFleet is neither: it is a *human, remote, per-driver, specialist* service at $30/driver/month. If drivers ≈ trucks, that is **$30/truck against our $130** — a 4.3x gap, not the 2x we modelled, and it comes with a company that publishes every price and a reputation for doing one thing well. We cannot win on price, and we cannot win on "remote specialist" either.

**Mitigation.**
- **The wedge is what they refuse, and we must own it loudly.** Their own "what we don't do" page names Part 395 and ELDs. Their buyers are sent to us by the competitor's own FAQ. **Use that: a referral partnership with DotFleet, and quote their refusal in our positioning.**
- **Do not imitate their model without their economics.** Their price buys a narrow scope and no SLA beyond one business day. Ours has to carry a 45-60 day deadline, an E&O-backed guarantee, and source-documented corrections.
- **Watch their pricing as the true floor.** If DotFleet raises prices or adds HOS, our whole price architecture moves.
- **Their business-hours-only, one-day-response model is the model we should benchmark the roster against** - not the 24/7 promise we were about to drop for cost reasons, but the one competitor who is genuinely comparable to us.

**Owner.** Owner (competitive watch) + requester (positioning).

---

## 19. Corrections we have made to this register (audit trail)

| Date | Change |
|---|---|
| 2026-10-19 | 395.8(e)(4)(ii) withdrawn as a citation (does not exist in the current CFR); the governing rules are 395.30(d)/(c)(2)/(e)/(f), 395.8(f)(2), 395.8(k), 395.22, 395.32, 395.36 and Appendix A 4.3.2.8. Verified in full against eCFR and Cornell LII. |
| 2026-10-19 | 49 U.S.C. 5215 corrected to 49 U.S.C. 521(h) - up to $25,000 and one year per offence, doubled on a subsequent offence. |
| 2026-10-19 | 49 CFR 390.35 fraudulent records reclassified from "critical" to **acute** in 49 CFR Part 385 Appendix B. Acute violations can produce an unsatisfactory safety rating on their own. |
| 2026-10-20 | **Sisic sentence corrected.** "18 months, $50,000" was the prosecution's sentencing recommendation. The judgment of 25 January 2021 was three years' probation including six months' home incarceration, 50 hours' community service, a $1,000 fine and a $100 special assessment, plus a three-year FMCSA debarment. Corrected in six documents. |
| 2026-10-20 | Price ladders reconciled between `PLAN.md` and `SALES-PLAYBOOK.md` (a 15-truck fleet was $1,950/mo in one and $2,250 in the other). The $110 tier at 50+ trucks deleted as loss-making. |
| 2026-10-20 | Risk 2 ("no publishable track record") and the new risks 12-15 added following the strategy panel. |
