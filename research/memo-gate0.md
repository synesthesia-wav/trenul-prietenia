# Gate 0 Memo — Go / No-Go

**Date:** 2026-10-19
**Scope:** six blocking questions from `plan/eld-research-sprint.md`
**Verdict: CONDITIONAL GO — with one mandatory re-pricing decision before any selling starts.**

Two of the six gates failed in ways that change the business. One of those changes is good news about the legality of the product; the other is bad news about the price. Everything else passes with caveats.

---

## The short version

1. **The product is legally sound, and the regulation actually blesses the exact model we designed.** The rule I had been citing (395.8(e)(4)(ii)) does not exist. The rule that does exist (395.30(d)) is *better for us*: it expressly permits a motor carrier — or a system acting for one — to propose edits to a driver's records, provided the driver confirms or rejects, implements, recertifies and resubmits. That is our workflow, sanctioned in the CFR rather than improvised around it. Our "we never touch the ELD" rule is now anchored in 395.8(f)(2), 395.30(f) and Appendix A 4.3.2.8(b).

2. **$130/truck/month is roughly twice the automation tier and about 2.2x the real offshore anchor.** Published US managed-compliance prices run $25–65 per truck per month (Trucking Hub $29, Trucking Comply from $25, TruckingMBA $50–65, TenFour $38–99/driver). The genuine offshore competitor is Turbo ELD at **$60/month** ($2/day/truck) with 100+ employees, 500+ clients, 7 years, and **already native in Arabic, Uzbek, Russian and English**. $130 only makes sense in the *staffed-HOS-desk* band (Prime Fleet, $60–250/truck), where the buyer is comparing us to a full outsourced compliance department, not to a $29 software bundle.

3. **The strongest sales asset in the whole research is a criminal case.** *United States v. Sisic* (D.R.I. 2020): the owner of an **11-tractor** carrier altered thousands of ELD entries for ~20 drivers to conceal driving time; one driver died; he pleaded guilty to conspiracy to falsify records, 18 months, $50,000, and the company is defunct. That is our target customer, in our target fleet-size band, doing exactly what an unmanaged fleet does. The alternative to paying for a service is that the owner does it himself and goes to prison.

4. **Our core positioning is now proven by FMCSA's own violation data.** In live SMS profiles, the documentation codes (form and manner, certification, blank graph grids, shipping document number, trailer number) outnumber the driving codes by count, and the weight-5 paperwork codes are all documentation defects. A small fleet's HOS score is damaged mostly by paperwork — which is exactly what a staffed desk fixes. This is no longer a hypothesis.

5. **Two risks we did not know about:** the SMS methodology now reports "compliance categories" and **percentiles are often not assignable for small fleets** (three driver inspections with violations are required for a percentile above zero), so the Health Check must be rebuilt on counts and violation codes, not percentiles. And **Moldova's IT Park 7% turnover tax** — if this service qualifies as an accredited IT activity, it replaces corporate tax, payroll withholding and the 24% social contribution, and the entire staffing economics change.

---

## Gate results

| Gate | Question | Verdict | Note |
|---|---|---|---|
| 0.1 | E&O for a Moldova-domiciled provider | ⚠️ **PARTIAL** | Cost band is fine ($500–1,735/yr US baseline; ≤5% of revenue at 100 trucks). **Placement for a non-US domicile is unresearchable** — it is a broker conversation, not a search. |
| 0.2 | Market size | ✅ **PASS** | ~160,000–195,000 active carriers in the 5–75 PU band. 200–300 trucks = 0.11–0.19%. Not a market-size problem. |
| 0.3 | Free alternatives | ✅ **PASS** (with a commercial consequence) | Nothing free is staffed and continuous. But training and guidance *are* free — so we cannot sell training or advice. |
| 0.4 | Price | ❌ **FAIL — re-price before selling** | $130 sits 2x above the automation tier and 2.2x above the offshore anchor. Defensible only against the staffed-HOS band. |
| 0.5 | Legal | ✅ **PASS, strengthened** | Product design confirmed against 395.30(d). One citation withdrawn, two flagged unverified. |
| 0.6 | Request volume | ⚠️ **PARTIAL** | ~6 exceptions/truck/month (single grade-C source). Consistent with our labour model. Verify by instrumenting the pilot. |

---

## What must happen before we sell anything

### 1. Decide the price and the segment together (blocking)

The research forces a choice. We cannot be a cheaper general compliance desk, because $25–65 providers already are. Our defensible position is:

> **The staffed HOS desk for fleets that have a live hours-of-service problem — 24/7 driver response, document-backed corrections, and an inspection-ready file.**

That position implies:
- **$130/truck/month is defensible against Prime Fleet ($60–250/truck), not against TruckingMBA ($65) or Trucking Hub ($29).** So we sell to the 15–75 truck fleet with a violation history, and we do not sell to a 5-truck owner with a clean record.
- **Lead with the audit-ready correction file and the 24/7 response line**, because that is what neither Prime Fleet nor Turbo ELD foregrounds. Turbo ELD's own copy claims "auto-certify logbooks" — a claim that sits uneasily with 395.30(b)(1)–(2) and 395.8(f)(2). We should not make it, and we can quietly be the compliant alternative.
- **Do not compete on price, and do not run a price comparison.** Anchor on the Sisic case and on what the owner's alternative actually costs.
- **Re-tier the small end.** Below ~10 trucks, $130/truck is a $1,300–2,600/month spend for a 24/7 desk; the free layer plus a $29 bundle serves them better. Say no rather than discount.

**Decision needed from the partners:** does $130/truck/month stand as the headline price with a 10-truck minimum and a 15-truck target band, or do we re-price? My recommendation is to keep $130, hold the minimum at 10 trucks, and narrow the target to 15–75 trucks with a violation history.

### 2. Two human items, in parallel, this week

- **E&O broker** — with the SOP and the 395.30(d) analysis attached. Four questions: can you write E&O for a Moldova-domiciled provider serving US motor carriers; what underwriting material do you need; what do US carriers typically demand (limits, claims-made, US claims handling); what does it cost against premium.
- **Moldovan accountant** — does an outsourced ELD/HOS compliance service qualify for the IT Park 7% turnover regime? This is the largest single margin lever in the model and it is a two-hour question for someone who knows the regime.

### 3. Rebuild the Health Check on counts, not percentiles

Percentiles are frequently unassignable for small fleets. The report must lead with inspection counts, violation codes with severity weights, and the specific paperwork defects, and only show a percentile when one exists. This is also *better* than the percentile report: it tells the owner something actionable instead of a number.

### 4. Verification tasks (do not skip)

- Locate the current paragraph for the **14-day ELD records availability** requirement (or confirm it lives only in guidance) and the text of **395.3(e)(4)**. Both are currently unverified in our drafts and both will appear in an attorney packet.
- Read the FMCSA Pocket Guide 2024 PDF and the census file directly to replace a grade-C carrier-count restatement with grade-A data.
- Read the 2010 FMCSA RODS regulatory guidance (2010-13900) in full.
- Download the SMS Appendix A violations list and keep the full severity-weight table on file.

### 5. Interview scripts

The four guides (fleet owner, insurance agent, ELD reseller, dispatcher) are in `research/interview-guides.md`. They are the only instrument that can validate willingness to pay at $130 and the real request volume — the two things web research could not settle.

---

## What the research did *not* change

- The 24/7 staffing model and its breakeven (60–85 trucks). Labour costs came in **better** than modelled (a loaded English-capable operator ≈ $850–1,100/month, not $1,300–1,800), which pushes breakeven down, not up.
- The channel priority. Insurance agents and ELD resellers remain the two highest-leverage channels, and Prime Fleet's free DOT assessment confirms the Health Check is the right lead magnet.
- The two hard rules. Rule 1 (we never edit the ELD) is now *more* strongly supported by the CFR. Rule 2 (no correction without source documents) is now supported by the wire-fraud count in the Virginia case.
- The need for our own evidence base. With the partners' record under NDA, the first three pilots are the reference base, and the day-1 baseline pull is now the top delivery priority.

---

## Kill criteria still in force

From the sprint plan, unchanged and re-tested against the findings:

- If the E&O path is genuinely unavailable for a Moldova-domiciled provider, the structure must change (US employing entity, or a US agency partner). That is a bigger decision than pricing, and it is the one thing research could not settle.
- If the IT Park 7% regime does **not** apply, re-cost the model: contribution per truck falls and the price floor rises, which strengthens rather than weakens the case for the $130 headline.
- If two paid pilots do not convert, the segment or the message is wrong.
- If we cannot produce a correction file that survives an inspector, the product does not exist.

**Recommendation: proceed to Gate 1 and the interview round, but hold all outbound selling until the price/segment decision (1) and the two human items (2) are closed.**
