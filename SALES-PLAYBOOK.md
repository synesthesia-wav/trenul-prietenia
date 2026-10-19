# Sales Playbook

Companion to `PLAN.md`. Written for the person making the owner-level calls.

---

> **Revised 2026-10-20 after the strategy panel.** The previous opening line was "You will never get a call about a logbook again" - the panel's judgement was that it positions us as nuisance removal, a virtual assistant, which is a $29 comparison and a bookkeeper comparison. The buyer's problem is not calls; it is exposure. The 24/7 claim is gone from the pitch entirely. See `research/strategy-memo.md`.

## 1. The offer, by who is in the room

Use the version that matches who's in the room.

**Owner / decision maker (the carrier in trouble, with a date on his calendar):**
> When somebody with authority asks about your records, you want a file behind you, not an excuse. We are the hours-of-service desk for fleets like yours. We check every log against the bill of lading and the rate con, we prepare each correction with the document that supports it, and your driver certifies it. We never touch the log. Hand the inspector a file.

**The same buyer, one line, if he pushes for the summary:**
> Every correction comes with the document behind it. That is the whole promise.

**Driver (referral content, not a pitch):**
> Free cheat-sheet for phone ELD: duty status, the 30-minute break, the 8/12 splits in California, the 34-hour reset. Send it to a driver who just got a ticket. No signup, no sales call. (Retain the phone number in the footer - a driver who sends this to five other drivers is worth more than an ad.) Produce English first, then translated versions on request from the fleet; the driver-facing card is the referral engine, and it works in any language.

**Insurance agent (channel - the referral source that substitutes for a track record we do not have):**
> Your carrier clients get a file, not a report: every hours-of-service correction backed by its source document, so a roadside stop does not become a claim. Send me one of your insured fleets that is worried about its safety score. I will do the review free, with your name on it. You are the only person in this who can say "and I checked it myself."

**New Entrant carrier with a safety audit in the next 90 days (Tier 0 - our first sale):**
> You have 45 days to give FMCSA a corrective action plan or lose your registration. This is not a training course and it is not a monitoring service. We assemble the file FMCSA asks for, from the records you already have, and we stand behind the paperwork. [Price quoted as a flat fee for the event, not per truck.]

**ELD reseller (introducing only, never white-label):**
> [A one-page sell sheet that never contains a per-truck number. The reseller introduces; we contract directly with the carrier. Their real money is the ELD subscription, and we make it stickier.]

---

## 2. The HOS Health Check — now a pre-qualification filter, not a magnet

> **Repositioned 2026-10-20 by the strategy panel.** The Health Check is built on free public data the buyer can pull in ten minutes, so handing it to the market announces that we hold nothing proprietary. It is also aimed at a population whose public record is *empty by design* - FMCSA will not assign a percentile without three driver inspections with violations, so for our target segment the honest output is often "we can't tell you." That is a fine filter and it is not a magnet.
>
> **What it becomes:** (a) a **pre-qualification filter** we use before spending time on a carrier, and (b) a **cover page inside the file**, which is the actual product. It is also, for an insurance agent, a free loss-prevention tool with their name on it - which is how the channel gets built.
>
> **And the new first instrument: the "open the glovebox" self-score.** Twenty minutes in which the buyer scores his own ten driver-days and his own cab, with us present. The checklist is built from 49 CFR 395.22(h) (the in-vehicle packet: the data-transfer instruction sheet, the **ELD malfunction reporting sheet**, and eight days of blank graph grids) and 395.34(a) (the driver must note a malfunction in writing within 24 hours, and reconstruct the current 24-hour period and the previous seven days on graph-grid paper). **The first cab audit is free, needs no ELD integration, no API, no NDA and no E&O - which is why we can run 20 of them before a single contract exists.** It is also the only thing FMCSA's free layer cannot do, because FMCSA's free layer is *knowledge* and this is *observation*.

**What the Health Check still is:** a one-page report built from public FMCSA data for one carrier.

**Contents:**
1. Header: carrier name, DOT number, power units, drivers, operating radius, authority status.
2. Their inspection history: count by type, date, and violation code over 24 months, split into *hours of service* (395.3(a)), *records of duty status* (395.8/395.30/395.32/395.34) and *vehicle/driver qualification*.
3. **Their percentiles — only if assignable.** FMCSA requires at least three driver inspections with violations before it assigns a percentile above zero in the HOS category, so for a small fleet there frequently is none. **If there is no percentile, say so plainly: "you have no safety score, and that is not good news - it means nobody has looked." A score of 0 for an unscored carrier would be a false reassurance and a credibility failure.**
4. Out-of-service rate, with the pull date.
5. A one-page checklist: the documentation items most likely to fail an inspection for a fleet their size, **ordered by FMCSA's own violation data** (certification, form and manner, blank graph grids, shipping-document and trailer numbers, unassigned driving time, ELD malfunction reports, records not current, production on request, retention and possession, the 13-day submission window, driver access to records, state rules). See `assets/health-check-build-guide.md` section 3.
6. Footer: the offer, and one question.

**Rules:**
- It is **free**, and it must be **automated** if we are to send it at volume. The funnel arithmetic says ~1,160 reports per 100 trucks; at 45 minutes each, no person can produce that. If it is not automated, it is a ceiling, not a target.
- Every number comes from the carrier's own public record. Say so: *"we didn't ask you for anything, this is your own FMCSA data."*
- **Never** quote a percentile or a benchmark from memory - pull it, and put the pull date on the report.
- **We have no publishable track record of our own**, so this report *is* the credibility. Every number pulled on the day it is printed, dated, and correct.
- If the record is clean, say so, and still deliver the checklist. A clean report that hands over something useful wins the referral; a manufactured problem loses the account and the referral.
- **No number in it without a source URL and a pull date.** We got the Sisic sentence wrong once already; the rule now applies to every document we produce.

---

## 3. Call structure — 20 minutes, not 40

**Never open with the service. Open with their finding, and open with the date on their calendar.**

1. **Opening (2 min).** "I pulled your FMCSA record for [company] - no charge, it takes two minutes. There's [X] in there. Do you have 20 minutes now or later this week?"
   - If they say "send it to me," send it and ask for a 15-minute call after they read it. Do not push.
2. **Find the date (3 min).** "What's coming up for you - an insurance renewal, a renewal notice, a new authority letter, a broker asking you for something?" **The trigger is a date on his calendar, not a violation in his history.** A fleet with a deadline and a bad record does not need our references; it needs us to fix it by a date.
3. **Permission and baseline (5 min).** "Before I say anything about us - who actually touches the logs when something goes wrong?" Listen for the gap. That gap *is* the product.
4. **Quantify the pain in his units (5 min).** "What did the last one cost you - in the fine, in the down time, in the argument with your insurance company?" Never lead with the fine; lead with the renewal and the personal exposure. The statutory maximum is a ceiling that a smart buyer will discount to expected value.
5. **The bridge (3 min).** "We check every log against the bill of lading, we prepare each correction with the document that supports it, and your driver certifies it. We never touch the log. When somebody asks about your records, you hand over a file."
6. **The close (3 min).** Every close ends with **a date on a clock he owns** - not "send me an email and we talk in a month," which converts doubt into delay. "Two ways to test it: [the paid pilot] - or I send you the checklist and we talk after your [renewal / audit / response date]. Which is more useful?"
7. **If the close fails (2 min).** "What's the one thing that would have to be true for you to consider this?" - write the answer down verbatim. That is the next 20 calls.

**Call notes that go in the CRM (mandatory):** trucks, lanes/states, ELD platform, current compliance provider, **the dated event and its date**, what happens today when a driver has a log problem, the exact objection, and the exact next step with a date.

---

## 4. Qualification — five questions, and the disqualifiers

**Qualify on:**
1. How many power units, and how many are active right now?
2. Which ELD platform?
3. Who handles a driver's log question today - you, your office manager, a bookkeeper, or nobody?
4. **What is the dated event?** An insurance renewal, a citation, a new authority, a broker's qualification request, a new-entrant safety audit. *(This replaces "last violation" as the primary filter.)*
5. Do you know how many driver inspections with violations you have had in 24 months? *(FMCSA needs at least three before it assigns a percentile above zero, so for a small fleet there usually is no score. That absence is the pitch: you have no score because almost nobody has looked.)*

**Disqualify or de-prioritize:**
- **Under 10 trucks** (excluding New Entrant carriers, who are buying an event rather than a retainer) - the account cannot carry a staffed desk against, and the free FMCSA training plus a $29 software bundle serves the owner better. **Say no rather than discount.** (Research 2026-10-19: the automation band is $25-65/truck/month, and FMCSA provides training and guidance free.)
- **Fleets that want filings** - DQ files, Clearinghouse, drug and alcohol, IFTA/UCR, MCS-150. That is TenFour ($99 first truck / $59 each additional) and DotFleet Compliance ($75 per driver one-time, $30/driver/month): cheaper, US-domiciled, and explicitly good at it. **Refuse and refer.** This is the most valuable refusal we have, and DotFleet's own FAQ points its buyers at us.
- A large fleet (100+ power units) with a compliance department - wrong process, six-month procurement.
- "We already have this covered" - unless the incumbent is the ELD app's own tier-1 support with no human behind it. That is the most winnable "we have it" objection; see section 6.
- **A carrier whose hours-of-service record is already clean.** We have no published track record, so we cannot beat a clean record on results.
- Anyone who wants us to *edit* the ELD for them or to "make the hours work." Decline, politely, and permanently. See section 8.

**Pricing ladder (reconciled 2026-10-20 - identical to `PLAN.md` section 5.2, which previously contradicted this table):**
| Active power units | Price | Floor |
|---|---|---|
| 1-14 | $150 / truck / mo | $1,500 / mo |
| 15-49 | $130 / truck / mo | $1,950 / mo |
| 50+ | $130 / truck / mo | $6,500 / mo |
| 24/7 live desk | +$55 / truck / mo, at 75+ trucks only | |
| New Entrant audit prep | $1,500-4,000 per event | |

**The old $110 tier at 50+ trucks is deleted** - at 50 trucks it made the account negative by roughly $31,800 a year. We were paying our best reference candidates to leave us in the hole.

**Why these tiers exist (research 2026-10-19/20):** published US managed-compliance prices run $25-65 per truck per month for the automation tier (Trucking Hub $29, Trucking Comply from $25, TruckingMBA $50-65, TenFour $38-99 per driver, DotFleet $30 per driver), $60-80 for the offshore ELD-monitoring tier (Turbo ELD, from $2/day per truck, 100+ employees, 500+ clients, already native in Arabic, Uzbek and Russian), and $60-250 for the staffed-HOS tier (Prime Fleet Management: from $500/month, and "most fleets in our 6-25 truck range invest $1,500-$6,000/month" - their own FAQ puts 15 trucks at $6,000/month, i.e. $400 per truck). **$130 only defends against the tier we are in.** It must never be compared to the $29 tier, and we should say so out loud when a buyer raises it: *"If you only want the paperwork done, they are cheaper and you should buy them."*

**Present the price per fleet, not per truck.** Quote "$1,950 a month for your 25 trucks" on the offer sheet and per-truck on the invoice. "$130 a truck" invites "the ELD is $29 a truck." "$1,950 a month" invites "what do I spend on compliance today?" - where the honest answer is $725-1,625 of software, $0 of people, and his office manager's time.

---

## 5. The pilot and the first sale

**Two different entry offers, for two different buyers.**

**A. New Entrant audit prep (Tier 0 - our first sale).**
- **Flat fee, $1,500-4,000 for the event.** Not per truck. A 2-truck carrier facing revocation cannot pay a retainer, but a business facing revocation can pay for a professional to assemble the file.
- **30 days**, and the deliverable is the file FMCSA asks for: driver list, licences, RODS plus supporting documentation, MVRs, medical certificates, vehicle list, maintenance files, accident register, insurance proof, BOC-3, IRP/IFTA - plus the **corrective action plan** if the audit has already failed.
- **Credited in full** against the first three months of any continuing engagement.
- **The deadline is his, not ours:** 45 days (passenger/HM) or 60 days (all other) from the failure notice, or his USDOT registration is revoked. Lead with that, not with our process.
- **Success metric:** the file assembles cleanly and he passes. There is no other metric that matters.

**B. The retainer pilot (Tier 1).**
- **Flat fee**, $750-1,500/month for 5-10 trucks. Not per truck.
- **Business-hours SLA only** during the pilot. Say this before they ask; it reads as operational discipline, not a limitation.
- **Credited in full** against the first three months of the contract.
- **Fixed scope in writing:** monthly HOS/RODS review, driver questions during business hours, correction packs prepared and logged, one monthly report, one quarterly record review.
- **Success metric agreed in advance:** every Class 2 correction carries a source document; every request answered inside the SLA; **the carrier can produce a correction file for any managed truck without asking us anything.** That last one is the binary a client can verify without calling us, and it is the one that matters.
- **Data requirement from them:** ELD access (their own account, with their authorisation), BOLs and rate cons, and a named driver-side point of contact.
## 6. Objection handling

| Objection | Response |
|---|---|
| "The ELD app already does this." | "It does. The app tells the driver. We're the ones who reconcile the paperwork, answer the driver when he's pulled over, and hand your inspector a file. Your app sends an alert; nobody has to act on it." |
| "We are at $80 with our current provider." | "Then you are paying for a monitoring desk, and for 25 trucks the gap is $15,000 a year. Here is what that buys: a named human who is accountable for every correction, every correction backed by the source document, a file an inspector can accept, and a report on your own numbers every month. Ask your current provider three questions: who is accountable for a correction, will they hand an inspector a document for every change they made, and does the file exist if the ELD vendor shuts down? If they can answer all three, they are as good as us. If they cannot, that is the $15,000." (Never disparage a named competitor; let the three questions do the work. Anchor the $15,000 against one adverse insurance renewal, not against their invoice.) |
| "What if a driver still gets a ticket?" | "We control the paperwork and the response time — those are in the SLA with service credits. We can't control a driver who chooses to drive 12 hours. What we guarantee is that the file is clean, the correction is documented, and someone answered the driver within the window." |
| "Your competitors charge $29 a truck." | "They do, and for $29 a truck you get software and filings. What you do not get is anybody accountable for the record, or a file an inspector accepts. We are not competing with them - we are doing a different job. If all you need is the paperwork done, they are cheaper and you should buy them." **Say this with conviction. A buyer who would rather have the $29 service is not a buyer we want, and a buyer we talk out of a $29 service is a customer who churns in month three.** |
| "Why would you do this instead of just doing it ourselves?" | "Because the version where you do it yourself is the one that ends with your company gone. In 2020 the owner of an 11-truck carrier altered thousands of ELD entries to cover his drivers' hours. One of them died in a crash in Oklahoma. He pleaded guilty to conspiracy to falsify federal records and was sentenced to three years' probation, including six months in home confinement, and FMCSA debarred him from federal work for three years. The company is defunct. And it was not the messy log that did it - it was the second copy of the log he handed to the trooper. That is what we are for." **(Use the case. It is the strongest asset we have found. And get the facts right - the sentence is checkable in one search, and a seller caught overstating a court record has no credibility left to sell a compliance file with.)** |
| "My insurance company handles this." | "Your insurer cares about claims; we're the ones who can stop the citation that creates the claim. Their loss-prevention team does driver training. We assemble the file." (And: this objection often means the agent is the real buyer - ask for the agent's name.) |
| "Send me an email." | "Will do - the report goes out now. Can I call you Tuesday at 10 to go through it? I'll only call once if it's a no." (The report goes out before you hang up, always.) |
| "I have to think about it." | "Of course. What specifically do you need to think about - the price, the trust, or whether your drivers will use it?" Name the objection, then wait. |
| "My driver says he doesn't want someone editing his log." | "Good - he shouldn't. We don't edit anything. He makes every entry himself. We do the research and give him the documented correction to make. That's also why the file holds up at an inspection." |
| "What if you make a mistake?" | "Every correction we prepare is attached to its source document and logged, and the driver makes the actual entry. If we get one wrong, it's a service failure with a credit - and our E&O insurance covers professional error. You can audit our log any time." |
| "Are you an American company?" | **Answer honestly.** "Our delivery team is in Moldova; the contracting entity is a US company with US E&O insurance, so you are covered by US policy and US claims handling. The work happens overseas, which is what lets us afford a staffed desk and a documented file rather than a monitoring feed." **If that structure is not yet in place, do not sell yet** - see `RISKS.md` section 3. This is a hard dependency, not a nicety. |

---

## 7. Retention — the part that decides whether this is a company

New fleets churn on two things: the owner sells trucks, and the drivers hate being watched.

- **Day 30, 90, 180:** a written report every month, not just when something happens. Show the work: requests handled, corrections by class, the documents they sent us, and what we found that nobody asked about. **One page, not twelve.** "Three things you did not know, here is the file." A carrier that sees a monthly report with three real findings they didn't know about will not cancel.
- **The refusals belong in the report.** Every request we declined, with the reason, on the same page. It reads as rigour rather than a list of things we failed to do, it is the artefact no competitor can produce, and it is the thing a broker or an attorney will ask to see. *(Pending counsel's answer on discoverability - see `RISKS.md` section 15. Until then the report shows the refusal *count* and the rule, not the requesters' words.)*
- **Quarterly:** re-pull their FMCSA record and show the movement - violation codes, inspection counts, and the percentile **if one is assignable** (for a small fleet it usually is not; say so rather than implying a score). **We report what we control** - weight-5 paperwork defects found and closed per truck per month, by regulation - because a percentile will not move in a year at fleet sizes our buyer runs. The pre-engagement baseline is still captured as a byproduct of the first call, and it becomes the case study we can publish once we have one.
- **Driver experience:** driver-facing HOS material in the driver's language, framed as protection. Route complaints to us, not to the owner.
- **Expansion - narrower than before.** When they trust the paperwork, the next conversation is about **more of the same file**: a second location, more trucks, a quarterly examination pack, a second driver group. **Not** about their other paperwork. DQ files, drug and alcohol, IFTA/UCR, vehicle maintenance and legal representation belong to other people who are cheaper and better at them, and expanding into them is the fastest way to lose the position we have just claimed. **Refuse and refer** (see section 4).
- **Never let a fleet leave for price.** 30%+ annual logo churn is a service failure. If they say price, find the missing service first.

---

## 8. Two hard rules

**Rule 1 — We never edit a driver's ELD.** 49 CFR 395.8(f)(2) requires that all entries relating to a driver's duty status be made by the driver, and 395.30(f) forbids altering or erasing the original record. What the regulation *does* permit is a proposal: 395.30(d)(1) lets the motor carrier request edits, and 395.30(d)(3) requires the driver's electronic confirmation or rejection of anything requested by a system or a person other than the driver. So we prepare, document and propose; the driver confirms, enters and recertifies. The ELD keeps the original, unedited record alongside every edit, and that history is permanent and retrievable by FMCSA. This is also our best selling point: *we can show an inspector every document behind every change, because we never made the change ourselves.*

**Rule 2 — We never propose a correction the documents don't support.** Not for an important customer, not as a favour, not "just this once." If the documents and the driver's account conflict, we escalate to the carrier and log it. If the request is to create or erase driving time, to shorten automatically recorded driving time, or to alter the original record, we decline in writing and log the refusal. The device itself blocks part of this — Appendix A § 4.3.2.8.2(b) bars shortening automatically recorded driving time — and FMCSA's Q7 confirms driving time cannot be changed to non-driving time.

**The refusal log is our moat, and it is also our biggest legal exposure.** No competitor can ship a written record of the changes it declined to make, which is why it is the thing that makes us credible without a track record. But a logged refusal could also be read by a carrier's own attorney as a written admission that the fleet was seeking falsification. **So: get counsel's answer before publishing the log, keep the wording scoped to process ("we did not propose a change because the documents did not support one") rather than to the requester's intent, and never write down a motive.** Until that advice is in hand, publish the *rule* and keep the *log* internal. See `RISKS.md` section 15.

**And the reason this is a rule rather than a preference:** in 2020 the owner of an 11-truck carrier altered thousands of ELD entries to conceal his drivers' hours. One driver died in a crash in Oklahoma. He pleaded guilty to conspiracy to falsify federal records and was sentenced to three years' probation including six months in home confinement; FMCSA debarred him from federal contracting for three years; the company is defunct. A 126-count Virginia indictment in the same area added wire fraud. If a carrier asks us to make a correction the paperwork does not support, we are asking them to join that list — and to void their insurance at the same time.
