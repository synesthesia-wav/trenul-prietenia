# Sales Playbook

Companion to `PLAN.md`. Written for the person making the owner-level calls.

---

## 1. The offer in three versions

Use the version that matches who's in the room.

**Owner / decision maker:**
> You will never get a call about a logbook again. We answer your drivers at any hour, we reconcile every trip against the BOL, and if an inspector asks, you hand them a file instead of an excuse. $130 per truck per month, per truck, no surprises.

**Driver (referral content, not a pitch):**
> Free cheat-sheet for phone ELD: duty status, the 30-minute break, the 8/12 splits in California, the 34-hour reset. Send it to a driver who just got a ticket. No signup, no sales call. (Retain the phone number in the footer — a driver who sends this to five other drivers is worth more than an ad.) Produce English first, then translated versions on request from the fleet; the driver-facing card is the referral engine, and it works in any language.

**Insurance agent / ELD reseller (channel):**
> Your carrier clients get an HOS Compliance review of their own FMCSA record, and a documented correction file for every fix — so an inspection doesn't become a claim. You get a free risk review for the carrier; we get the work. 20% of year one.

---

## 2. The HOS Health Check — the door opener

**What it is:** a one-page report built from public FMCSA data for one carrier.

**Contents:**
1. Header: carrier name, DOT number, power units, drivers, operating radius, authority status.
2. Their inspection history: count by type, date, and violation code over 24 months, split into *hours of service* (395.3(a)) vs. *records of duty status* (395.3(e)) vs. *vehicle/driver qualification*.
3. Their `HOS Compliance` and `Unsafe Driving` BASIC percentiles, current, with the date pulled, plus a plain-language "what this percentile means for your next renewal" line.
4. Out-of-service rate vs. the size-band benchmark.
5. A one-page checklist: the documentation items most likely to fail an inspection for a fleet their size, **ordered by FMCSA's own violation data** (certification, form and manner, blank graph grids, shipping-document and trailer numbers, unassigned driving time, ELD malfunction reports, records not current, production on request, retention and possession, the 13-day submission window, driver access to records, state rules). See `assets/health-check-build-guide.md` §3.
6. Footer: our offer, and one question — "want us to walk you through what we found?"

**Rules:**
- It is **free** and it takes 20–30 minutes to produce. Price of the report is the disqualifying factor, not the labor.
- Every number in it comes from the carrier's own public record. Say so explicitly: *"we didn't ask you for anything, this is your own FMCSA data."*
- **Never** quote a percentile or a benchmark from memory — pull it, and put the pull date on the report. FMCSA methodology changes; a wrong number destroys the only credibility the report has.
- **We have no publishable track record of our own** (the partners prior record is under NDA), so this report *is* the credibility. Every number pulled on the day it is printed, dated, and correct.
- If the record is clean, say so, and still deliver the checklist. A clean report that hands over something useful wins the referral; a manufactured problem loses the account and the referral.

---

## 3. Call structure — 20 minutes, not 40

**Never open with the service. Open with their finding.**

1. **Opening (2 min).** "I pulled your FMCSA record for [company] — no charge, it takes two minutes. There's [X] in there. Do you have 20 minutes now or later this week?"
   - If they say "send it to me," send it and ask for a 15-minute call after they read it. Do not push.
2. **Permission and baseline (5 min).** "Before I say anything about us — what happens today when a driver has a problem with his log? Who calls him?"
   - Listen for the gap. That gap *is* the product.
3. **Quantify their pain (5 min).** "Has a driver been cited in the last 24 months?" / "When your insurance renews, do you know what your safety score is?" / "What did the last inspection cost you?"
4. **The bridge (3 min).** "We handle that part — the paperwork, the driver questions, the 2am calls, and the file an inspector sees. It's $130 per truck per month."
5. **The close (3 min).** "Two ways to test it: a paid pilot on 5 of your trucks, business hours, flat fee, credited in full against the contract. Or I send you the checklist and we talk in a month. Which is more useful?"
6. **If the close fails (2 min).** "What's the one thing that would have to be true for you to consider this?" — write the answer down verbatim. That is the next 20 calls.

**Call notes that go in the CRM (mandatory):** trucks, lanes/states, ELD platform, current compliance provider, last violation date, what happens today when a driver has a log problem, the exact objection, and the exact next step with a date.

---

## 4. Qualification — five questions, and the disqualifiers

**Qualify on:**
1. How many power units, and how many are active right now?
2. Which ELD platform?
3. Who handles a driver's log question today — you, your office manager, a bookkeeper, or nobody?
4. Last HOS or record-of-duty-status violation or citation, and how long ago?
5. Do you know your current `HOS Compliance` percentile? *(Better: do you know how many driver inspections with violations you have had in 24 months? FMCSA needs at least three driver inspections with violations before it assigns a percentile above zero, so for a small fleet there usually is no score. That absence is itself the pitch: you have no score because almost nobody has looked.)*

**Disqualify or de-prioritize:**
- **Under 10 trucks** — the account cannot carry 24/7 coverage against, and the free FMCSA training plus a $29 software bundle serves the owner better. **Say no rather than discount.** (Research 2026-10-19: the automation band is $25–65/truck/month, and FMCSA provides training and guidance free.)
- A large fleet (100+ power units) with a compliance department — wrong process, six-month procurement.
- "We already have this covered" — unless the incumbent is the ELD app's own tier-1 support with no human behind it. That is the most winnable "we have it" objection; see §6.
- **A carrier whose hours-of-service record is already clean.** We have no published track record, so we cannot beat a clean record on results. Selling to a clean fleet means selling on nothing but our promise.
- Anyone who wants us to *edit* the ELD for them or to "make the hours work." Decline, politely, and permanently. See §8.

**Pricing tier to quote:**
| Active power units | Price |
|---|---|
| 10–19 | $150 / truck / mo |
| 20–49 | $130 / truck / mo |
| 50+ | $110 / truck / mo |

**Why these tiers exist (research 2026-10-19):** published US managed-compliance prices run $25–65 per truck per month for the automation tier (Trucking Hub $29, Trucking Comply from $25, TruckingMBA $50–65, TenFour $38–99 per driver) and $60–80 for the offshore ELD-monitoring tier (Turbo ELD, from $2/day per truck, 100+ employees, 500+ clients, already native in Arabic, Uzbek and Russian). The staffed-HOS-desk tier we occupy runs $60–250 per truck (Prime Fleet Management: from $500/month, and "most fleets in our 6–25 truck range invest $1,500–$6,000/month," with a named HOS Specialist doing daily ELD monitoring and logbook review and correction). **$130 only defends against the tier we are in.** It must never be compared to the $29 tier, and we should say so out loud when a buyer raises it: *"If you only want the paperwork done, they are cheaper and you should buy them."*

---

## 5. The pilot — design it to protect the 24/7 economics

- **Flat fee**, $750–1,500/month for 5–10 trucks. Not per truck.
- **Business-hours SLA only** during the pilot. 24/7 starts on the day the contract does. Say this before they ask; it reads as operational discipline, not a limitation.
- **Credited in full** against the first three months of the contract.
- **Fixed scope in writing:** monthly HOS/RODS review, driver questions during business hours, correction packs prepared and logged, one monthly report, one quarterly SAFER/BASIC review.
- **Success metric agreed in advance:** zero preventable documentation deficiencies in managed trucks; median response time < 10 min; 100% of RODS reconciliation issues caught before the weekly safety meeting; no correction proposed without a source document attached.
- **Data requirement from them:** ELD access (their own account, with their authorization), BOLs and rate cons, and a named driver-side point of contact.

---

## 6. Objection handling

| Objection | Response |
|---|---|
| "The ELD app already does this." | "It does. The app tells the driver. We're the ones who reconcile the paperwork, answer the driver when he's pulled over, and hand your inspector a file. Your app sends an alert; nobody has to act on it." |
| "We are at $80 with our current provider." | "Then you are paying for a monitoring desk, and for 25 trucks the gap is $15,000 a year. Here is what that buys: a named human who answers at 2am, every correction backed by a source document, a file an inspector can accept, and a monthly report on your own safety numbers. Ask your current provider three questions: who is accountable for a correction, what is the response time at 2am on a Sunday, and can they hand an inspector a document for every change? If they can answer all three, they are as good as us. If they cannot, that is the $15,000." (Never disparage a named competitor; let the three questions do the work. Anchor the $15,000 against one HOS out-of-service on a $300k premium, not against their invoice.) |
| "What if a driver still gets a ticket?" | "We control the paperwork and the response time — those are in the SLA with service credits. We can't control a driver who chooses to drive 12 hours. What we guarantee is that the file is clean, the correction is documented, and someone answered the driver within the window." |
| "Your competitors charge $29 a truck." | "They do, and for $29 a truck you get software and filings. What you do not get is a person at 2am, or a file an inspector accepts. We are not competing with them — we are doing a different job. If all you need is the paperwork done, they are cheaper and you should buy them." **Say this with conviction. A buyer who would rather have the $29 service is not a buyer we want, and a buyer we talk out of a $29 service is a customer who churns in month three.** |
| "Why would you do this instead of just doing it ourselves?" | "Because the version where you do it yourself is the one that ends in federal court. In 2020 the owner of an 11-truck carrier altered thousands of ELD entries to cover his drivers' hours. One of them died in a crash. He pleaded guilty to conspiracy to falsify records, served 18 months, paid $50,000, and the company went out of business. That is what the alternative looks like — and your insurance does not cover it." **(Use the case. It is the strongest asset we have found.)** |
| "My insurance company handles this." | "Your insurer cares about claims; we're the ones who can stop the citation that creates the claim. Their loss-prevention team does driver training. We do the paperwork and the phone calls." (And: this objection often means the agent is the real buyer — ask for the agent's name.) |
| "Send me an email." | "Will do — the report goes out now. Can I call you Tuesday at 10 to go through it? I'll only call once if it's a no." (The report goes out before you hang up, always.) |
| "I have to think about it." | "Of course. What specifically do you need to think about — the price, the trust, or whether your drivers will use it?" Name the objection, then wait. |
| "My driver says he doesn't want someone editing his log." | "Good — he shouldn't. We don't edit anything. He makes every entry himself. We do the research and give him the documented correction to make. That's also why the file holds up at an inspection." |
| "What if you make a mistake?" | "Every correction we prepare is attached to its source document and logged, and the driver makes the actual entry. If we get one wrong, it's a service failure with a credit — and our E&O insurance covers professional error. You can audit our log any time." |
| "Are you an American company?" | **Answer honestly.** "Our delivery team is in Moldova; the contracting entity is a US company with US E&O insurance, so you are covered by US policy and US claims handling. The work happens overseas, at a cost that lets us staff 24/7." **If that structure is not yet in place, do not sell yet** — see `RISKS.md` §3. This is a hard dependency, not a nicety. |

---

## 7. Retention — the part that decides whether this is a company

New fleets churn on two things: the owner sells trucks, and the drivers hate being watched.

- **Day 30, 90, 180:** a written report every month, not just when something happens. Show the work: requests handled, response times, corrections by class, the documents they sent us, and what we found that nobody asked about. **The monthly report is the product.** A carrier that sees a monthly report with three real findings they didn't know about will not cancel.
- **Quarterly:** re-pull their FMCSA record and show the movement — violation codes, inspection counts, and the percentile **if one is assignable** (for a small fleet it usually is not; say so rather than implying a score). When it moves, quote it in the renewal conversation, and let them quote it with their agent. That is the renewal. **This is also how we build the company's own evidence base:** every account gets a pre-engagement baseline from FMCSA data, and the comparison becomes the case study we can publish once we have it.
- **Driver experience:** driver-facing HOS material in the driver's language, framed as protection. Route complaints to us, not to the owner.
- **Expansion:** when they trust the paperwork, the next conversation is about their *other* paperwork — vehicle maintenance, driver qualification files, insurance renewals, and the annual DOT audit. Those are the same desk, at the same price per truck, and they are where the margin is.
- **Never let a fleet leave for price.** 30%+ annual logo churn is a service failure. If they say price, find the missing service first.

---

## 8. Two hard rules

**Rule 1 — We never edit a driver's ELD.** 49 CFR 395.8(f)(2) requires that all entries relating to a driver's duty status be made by the driver, and 395.30(f) forbids altering or erasing the original record. What the regulation *does* permit is a proposal: 395.30(d)(1) lets the motor carrier request edits, and 395.30(d)(3) requires the driver's electronic confirmation or rejection of anything requested by a system or a person other than the driver. So we prepare, document and propose; the driver confirms, enters and recertifies. The ELD keeps the original, unedited record alongside every edit, and that history is permanent and retrievable by FMCSA. This is also our best selling point: *we can show an inspector every document behind every change, because we never made the change ourselves.*

**Rule 2 — We never propose a correction the documents don't support.** Not for an important customer, not as a favour, not "just this once." If the documents and the driver's account conflict, we escalate to the carrier and log it. If the request is to create or erase driving time, to shorten automatically recorded driving time, or to alter the original record, we decline in writing and log the refusal. The device itself blocks part of this — Appendix A § 4.3.2.8.2(b) bars shortening automatically recorded driving time — and FMCSA's Q7 confirms driving time cannot be changed to non-driving time. The refusal log is the control that makes the business insurable and defensible, and if a carrier ever asks us to break it, that is the moment to end the relationship rather than the contract.

**And the reason this is a rule rather than a preference:** in 2020 the owner of an 11-truck carrier altered thousands of ELD entries to conceal his drivers' hours. One driver died in a crash. He pleaded guilty to conspiracy to falsify records, served 18 months, paid $50,000, and the company went out of business. A 126-count Virginia indictment in the same area added wire fraud. If a carrier asks us to make a correction the paperwork does not support, we are asking them to join that list — and to void their insurance at the same time.
