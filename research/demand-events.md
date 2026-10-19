# Demand map: the four dated, document-driven events

Written 2026-10-19, during the strategy panel on demand and deal-making. Grade A regulatory sources, pulled and read in full. This page exists because the question was "how might we create demand in other ways," and the answer turned out to be that **FMCSA already creates the demand, on dates, and specifies the evidence standard.**

## The short version

We had been treating the New Entrant safety audit as *the* beachhead. It is one of four. All four are the same shape: a federal deadline, a specific list of documents, and a carrier with no staff. The difference is how fresh the deadline is, how much money hangs on it, and how reachable the carrier is.

| # | Event | Clock | Evidence required | Reach | Money |
|---|---|---|---|---|---|
| 1 | **Driver gets an HOS violation** | short (to verify) | supporting documents, 49 CFR 395.11 categories | every carrier with a driver who gets cited | small per event, high volume |
| 2 | **Carrier gets a Conditional safety rating** | 45/60 days for the rating to go final; rating-change request (385.17) at any time, FMCSA reviews within 45 days | written description of corrective actions + documentation | 4,497 carriers in the 3–12 PU band, ~200–300 newly rated per year | high — it is an insurance and broker problem |
| 3 | **New entrant safety audit** | 45 or 60 days to file a CAP, or registration revoked | the full Safety Audit Resource Guide document set | ~58,600 audits a year, 8.7% fail | total, but the population churns |
| 4 | **Insurance renewal** | none | — | everyone | where the money actually is |

**Every one of them is resolved by a document package.** That is the product, and it is defined by regulation rather than invented by us.

## The evidence standard: 49 CFR 395.11, "Supporting documents"

Effective 2017-12-18. This is the half of the retention obligation we had missed, and it specifies the deliverable precisely.

**What a carrier must retain** (395.11(c)(1)), for each driver, for each 24-hour period, to verify on-duty not driving time:

1. Each bill of lading, itinerary, schedule, or equivalent document showing origin and destination of each trip;
2. Each dispatch record, trip record, or equivalent;
3. Each expense receipt related to any on-duty not driving time;
4. Each electronic mobile communication record reflecting communications through a fleet management system;
5. Each payroll record, settlement sheet, or equivalent indicating payment to a driver.

**Data elements required on each document** (395.11(c)(2)): the driver's name or PIN (or a unit number that can be associated with the driver), and the time, convertible to local time at the location where it was recorded.

**Other operative rules:**
- 395.11(b): the driver must submit supporting documents to the employer within **13 days** of the 24-hour period, or of coming into possession, whichever is later.
- 395.11(d)(1): a carrier need not retain more than **eight** supporting documents per driver per 24-hour period; if it holds more, it must retain the ones with the earliest and latest time indications.
- 395.11(f)(1): on request during a roadside inspection, the driver must make available any supporting document in his possession.
- 395.11(h): a carrier may apply to FMCSA under 49 CFR Part 381 subpart C to use a **self-compliance system** instead of the default retention method.

**Why this matters commercially.** Before this, our deliverable was "a source-documented correction file," which is a description. Now it is *a specified list of five document categories, with named data elements, a retention cap, and a production obligation at the roadside*. We are not selling a judgement about paperwork; we are selling compliance with a regulation that names its own evidence.

**And the corollary that hurts the current pitch.** FMCSA publishes the Safety Audit Resource Guide and the New Entrant training material **free**. Knowledge is not scarce. The scarce thing is the assembly, the retention discipline, and the production readiness. Anything we say that sounds like "here is what you need to know" is competing with a free PDF. Anything that says "we have it assembled and produced on demand" is not.

## Event 2 in detail: the Conditional safety rating

**The regulation (49 CFR 385.11, notification):** FMCSA gives a carrier written notice of a safety rating resulting from a compliance review, within 30 days of the review. The notice "will include **a list of FMCSR and HMR compliance deficiencies which the motor carrier must correct**." A proposed Conditional or Unsatisfactory rating becomes final after 45 days (HM/passenger) or **60 days (all other carriers)**.

**The remedy (49 CFR 385.17):** a carrier that has taken action to correct the deficiencies that resulted in a Conditional or Unsatisfactory rating **may request a rating change at any time**, on the basis of "evidence that it has taken corrective actions." The request "must include a written description of corrective actions taken, and other documentation the carrier wishes FMCSA to consider." FMCSA reviews such requests within 30 days (passenger/HM) or **45 days (all other carriers)**.

**The population, and an honest correction to my own first reading.** From the public census file, active property carriers with 3–12 power units:

- **4,497** currently carry a Conditional rating. That is the addressable stock.
- But the rating dates are spread across 1983–2026. **Only 128 were rated in 2026, 84 in 2025, 295 in 2024, 173 in 2023** — roughly **200–300 newly Conditional-rated carriers a year** in this band.
- So the stock is a **standing handicap**, not a live deadline. Most of those carriers got their letter years ago. What they still have is a Conditional rating on their record that their broker and their insurer can see, and a 385.17 path they can walk "at any time."

**This changes the pitch, and it is the second-order effect that matters.** For the recent cohort the 60-day clock is real and we should use it. For the stock, the trigger is **not a deadline — it is the renewal conversation and the broker.** The carrier's Conditional rating is a commercial problem for the agent, and the agent is the one who feels it. That is the strongest possible validation of the insurance-agent channel: the agent has a client whose rating is a liability at renewal, and the 385.17 evidence package is what fixes it.

**Also found:** 49 CFR 385.19 and 385.11(f)(i) allow FMCSA to let an Unsatisfactory carrier operate for **up to 60 additional days** where the carrier is making a good-faith effort to improve. So even the worst-rated carriers have a window, and the window is explicitly about *evidence of effort*. There are 269 Unsatisfactory-rated carriers in the 3–12 PU band.

## Event 3 in detail: the re-applicant, and the population problem

**49 CFR 385.329 (re-application):** a new entrant whose registration has been revoked may reapply **no sooner than 30 days after revocation**. If revoked for a failed safety audit, the carrier must submit an updated application, **submit evidence that it has corrected the deficiencies that resulted in the revocation**, and **begin the 18-month new entrant monitoring cycle again** as of the date the re-filed application is approved.

So the re-applicant is the highest-intensity buyer in the market: they have already failed, they know exactly what failed, they are legally required to submit remediation evidence, and their clock restarts the moment they re-apply.

**The population is far too small to build on, and the census data has a trap.** The census file carries `PRIOR_REVOKE_FLAG` and `PRIOR_REVOKE_DOT_NUMBER`. Exactly **141** carriers have the flag set — mostly 1–2 power units. And their `ADD_DATE` is the **original** registration date, not the re-application date, so our "added in the last 10 months" filter **misses re-applicants entirely**. There is no re-application date field in the census. Practical consequence: the 141 are a validation set and a pilot list, not a market.

**The bigger problem with the new-entrant beachhead, from Grade C sources with a clear signal:** new trucking businesses fail at very high rates — roughly 50% within 18 months (SBA figure, cited by truckpedia), 85–90% of new owner-operators within two years, and for auto carriers specifically "as many as 50% out of business in the first year, 70% in the first 24 months" (CarShipIO). The New Entrant programme's own exits by reason show **56% "inactive, change, no show at audit, no contact"** in 2023. A beachhead where the majority disappear before the 12-month audit, and where the minority are brand-new businesses with no revenue history, is a **churning, cash-poor, unreliable** base for a recurring retainer — even though it is the most dramatic and most document-shaped event on the map.

**One number worth keeping.** GAO-06-103 found FMCSA spent about $33M of $36.3M on education and outreach, almost all of it on the New Entrant programme, and had **no information on whether it worked** — a preliminary comparison of crash rates between audited and non-audited new entrants found "little difference." But the same report records that in 2017 FMCSA confirmed a 2015 evaluation of New Entrant training which "identified a positive impact on trained new entrants' crash performance **and business survival**." That is the only published link we have found between *document and training work* and *survival*, and it is the justification for treating this as a business-survival product rather than a paperwork product.

## Event 1 in detail: the driver's violation

**To verify:** the exact deadline and the documentation standard for a driver's request for administrative review of a violation, under 49 CFR 395.9, and whether a carrier may file on the driver's behalf. This is the fastest clock in the family and the highest volume — driver out-of-service violations run at roughly 6.4–7.25% of driver inspections nationally, and hours of service is the largest single share of driver OOS causes (CVSA 2025: HOS is 31.6–32.4% of driver OOS violations, and false logs/RODS is about 10% of them). **Do not quote a deadline until 395.9 is read in full.**

## The credibility risk this research surfaced

CarShipIO, writing about why new carriers fail, names one of the seven reasons: **"Every new company receives thousands of calls from people who are trying to sell them over the phone or email. Many get 'official-looking' forms with warnings urging new carriers to pay/subscribe to something they are tricked to think they need."** (Grade C, but the mechanism is obvious and the observation is specific.)

Our free cab review is a formal two-page document, on letterhead, citing CFR paragraph numbers, telling a new carrier he has a deadline and a compliance gap. **That is the description of the thing that industry warns new carriers about.** The new-entrant segment is the one segment in the country that is explicitly and repeatedly trained to distrust official-looking compliance solicitations, and it is the segment with the highest churn.

Two consequences:
1. **The free review must not read as a notice.** It should look like a peer or a service provider handing over a working checklist, not like the government writing to them. Different typography, no CFR cites on page one, no deadline language in the first line, and ideally not sent from a domain that resembles a government one.
2. **This is an argument against the New Entrant beachhead on trust grounds as well as churn grounds**, and an argument for the Conditional-rated and renewal-driven segments, where the carrier has already had a formal letter from FMCSA and therefore knows exactly what a real government document looks like — and knows the difference.

## What this changes in the plan

- The **product description** should be anchored on 395.11: five document categories, named data elements, eight-document cap, production on demand. Not on a general "compliance file".
- The **beachhead** should be the Conditional-rated population in the 3–12 PU band, reached through their **insurance agent at renewal**, with the 60-day clock used only for the recent cohort.
- The **New Entrant** segment should be retained as a secondary motion and a credibility test, not as the primary one, because of the churn and the distrust.
- The **proof standard** for what we sell is now regulatory, not promotional: we can show a customer the exact list FMCSA will ask for, and we can show him the retention and production obligation he is currently failing.

## Sources

All read 2026-10-19.

- 49 CFR 395.11 "Supporting documents" — eCFR, current as of 2026-10-05
- 49 CFR 395.8, 395.30, 395.32, 395.34, 395.36, 395.22 — eCFR, as previously recorded
- 49 CFR 385.309, 385.311, 385.319, 385.321, 385.325, 385.329, 385.329T, 385.13, 385.11, 385.17, 385.19, 385.307 — eCFR
- FMCSA "Prepare for Your Safety Audit" / Safety Audit Resource Guide — ai.fmcsa.dot.gov/NewEntrant
- FMCSA New Entrant Safety Assurance Program brochure (2023-06) and the 2015 programme booklet
- GAO-06-103, "FMCSA: Education and Outreach Programs Target Safety and Consumer Issues, but Gaps in Planning and Evaluation Remain"
- FMCSA 2024 Safety Research Forum, "Motor Carrier Industry Stats Overview" (New Entrant stats, inspections by fleet size, driver OOS rates)
- FMCSA Pocket Guide 2024 (carrier counts, inspection volume)
- CVSA 2025 International Roadcheck results (HOS share of driver OOS violations)
- CarShipIO (Grade C), truckpedia / ATOB (Grade C, new-carrier failure rates)
- FMCSA Company Census File, Socrata az4n-8mr2 (PRIOR_REVOKE_FLAG, SAFETY_RATING, SAFETY_RATING_DATE)

## Related

- procedures/fmcsa-census-target-list.md
- decisions/legal-anchors-eld-corrections.md
- notes/competitive-price-ladder.md
