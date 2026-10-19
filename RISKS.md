# Risk Register

Ranked by expected cost. Each entry: the risk, why it bites, the mitigation, and the owner.

---

## 1. Regulatory / criminal — the risk that ends the business

**Risk.** Corrections that are not supported by source documents amount to falsification of records of duty status required under 49 U.S.C. § 31502, criminal under 18 U.S.C. § 1001 and 49 U.S.C. § 5215, and a "falsifying records" violation rated critical under 49 CFR 385.3. ELD edit histories are permanent and retrievable by FMCSA. It also voids the carrier's insurance for any loss tied to the falsified hours, and the carrier — also a criminal actor in that scenario — is the least likely party to complain, which is exactly what makes it a business that can grow until one inspection, one claim, or one criminal referral unwinds it.

**Why it bites.** "Only what documents support" is a *practice*, not a *policy*. It erodes under deadline pressure, under a loud carrier owner, and under a commission structure that rewards outcomes rather than process. A single fabrication discovered in an ELD edit history is exhibit A.

**Mitigation.**
- The 4-class correction SOP in `PLAN.md` §2, with Class 4 (unsupported reconstruction) as a mandatory logged refusal.
- We never edit the ELD; the driver does. We prepare and document.
- The refusal log is retained and auditable. Review it monthly. A rising refusal count is a healthy sign, not a problem.
- US transportation attorney's written opinion on the SOP before the first commercial contract.
- The E&O underwriter reads the SOP. A carrier that declines to write because of the SOP is the most valuable feedback available.
- If a carrier asks us to break the rule: end the relationship, not just the contract. Never renegotiate it.

**Owner.** Partner #1 (SOP) + US attorney (opinion) + owner (logged refusals, reviewed monthly).

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

**Owner.** Owner (report templates) + delivery lead (QA).
