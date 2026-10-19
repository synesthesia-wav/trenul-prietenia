# Week One — How To Start

**The three gates are now assumed yes** (E&O placeable; IT Park 7% applicable). That assumption has one consequence we must respect: **we can talk, and we can run a paid pilot. We cannot sign an annual managed-services contract until the E&O policy is bound.** Which is why the first thing we sell is an *event* (New Entrant audit preparation), not a retainer — an event is a smaller liability, most buyers do not require a COI for it, and it proves the file.

**The target list already exists.** `research/data/new-entrant-targets.csv` — 44,959 US carriers, built from the public FMCSA Company Census File, updated daily, reproducible with `python3 research/build_new_entrant_list.py`.

---

## 1. The list, and why it is the right one

| | |
|---|---|
| **Source** | FMCSA Company Census File (Socrata `az4n-8mr2`), public, daily refresh, no key, no cost |
| **Filter** | added in the last 10 months · status Active · operating authority Active · motor carrier (not broker) · 1–25 power units · ≥1 driver · US address · 10-digit phone |
| **Result** | **44,959 carriers** |
| **Why** | A New Entrant must pass a Safety Audit within 12 months (49 CFR 385.307). Failure to file an acceptable corrective action plan in 45 or 60 days = **loss of USDOT registration** (385.321). The audit can be conducted **electronically, by submitting documents** — so the deliverable is a file, and the deadline belongs to the buyer. FMCSA ran 58,600 of these audits in 2023 at an 8.7% first-attempt failure rate — about 5,100 carriers a year who fail and have 45 days to respond. |

**Sanity check that it is the right population:** 44,959 over 10 months annualises to ~54,000/year, against FMCSA's 58,600 audits in 2023. The list and the audit count agree.

### But read the size distribution before you dial

| Band | Carriers | Read |
|---|---|---|
| 1 power unit | 34,246 (76%) | Owner-operators. The paperwork burden is real but the budget is small. **Not the first call.** |
| 2 power units | 7,215 (16%) | Same problem, less severe. |
| **3–12 power units** | **3,304 (7%)** | **The sweet spot.** Real HOS exposure, no in-house compliance function, enough revenue to pay for an audit. |
| 13–25 power units | 194 | Almost too small a pool; but the best payers. |

**3,304 carriers with 3–12 trucks is the entire market for our first product.** We need 2 sales from it in 90 days. That is 0.06% of a list we can hold in a spreadsheet.

### The first 100

`research/data/first-100.csv` — priority 1 and 2, 3–12 power units, ordered by call priority.
`research/data/state-campaign.csv` — all 3,304, **sorted by state**. Call one state at a time. Calling 20 states in a day means 20 time zones; calling Texas on one day means one. Top states: TX 438, FL 213, CA 187, OH 148, IL 138, PA 129, GA 127, NC 125, NJ 103.

---

## 2. Two ways in, and you do both — in this order

### Route A — the reseller or agent (do this first, it is faster)

One conversation with one ELD reseller or one truck-insurance agent is worth 5–10 introductions. This is the single highest-yield hour in the plan, and the panel was unanimous that the agent is the channel that substitutes for the track record we cannot show.

**Who to call:** commercial-truck insurance agents and ELD installers/resellers in the states above. Their book *is* our list — they already talk to these owners every month.

**The ask, in their language (Hormozi):** *"Send me one of your insured fleets that is worried about its safety score. I will do the review free, with your name on it."* Not a referral fee. A free file for one of their clients.

**For the interview programme specifically, the ask is:** *"I am trying to reach ten small fleet owners who have had a compliance scare, to understand what the paperwork actually costs them. I will do their paperwork review for free. Will you introduce me to two?"*

### Route B — the list (do it in parallel, day 2 onward)

Cold-call the first 100. Expect a **5–13% connect rate** (industry benchmark: 5.4% average, 13.3% top quartile) and **~400 dials per meeting**. Ten interviews from cold alone is 4,000 calls. That is not the plan. **Route A gets us the ten. Route B starts the campaign that produces sales.**

---

## 3. The instrument — the glovebox session IS the interview

Do not run "research interviews" and then separately run "cab audits." They are the same 30 minutes, and the audit version is the one that works, because it gives the owner something real.

**What it is:** a 20-minute session where **the owner scores his own ten driver-days and his own cab, with us present.** The checklist is built from 49 CFR 395.22(h) and 395.34(a):

- Is the **ELD malfunction reporting instruction sheet** in the cab? (395.22(h)(2))
- Are there **8 days of blank graph grids**? (395.22(h)(3))
- Is the **data-transfer instruction sheet** there? (395.22(h)(1))
- Does each driver have their **last 7 days of records in the cab**? (395.8(k)(2))
- Are the logbooks **certified**? (395.30(b))
- Is the **shipping document number** in the log? (395.24(c)(iii))
- Is **unassigned driving time** explained or assigned? (395.32(c))
- Was the last **ELD malfunction reported in writing within 24 hours**? (395.34(a)(1))

**Why this beats a pitch:** it is a five-minute check the owner can do with no ELD integration, no API, no NDA and no E&O — which is why we can run 20 of them before a single contract exists. And it is the one thing FMCSA's free layer cannot do, because FMCSA's free layer is *knowledge* and this is *observation*.

**What we are measuring, and why it matters more than the answers:**

| Measurement | What it decides |
|---|---|
| Do ≥15 of 20 sessions return a **non-zero defect count**? | If most fleets come back clean, the whole thesis is wrong — and we learn it in week one instead of month six. |
| The **defect rate by regulation** on real small fleets | Our first publishable evidence, and the first answer to the NDA problem. Nobody has this number. |
| **Does the owner state the number unprompted?** | Whether the finding lands. We are listening for the sentence, not the signature. |
| Session → pilot conversion | Whether the instrument converts. |

**And the price question, asked last and framed properly.** The panel was sharp about this: *"Would $130 be a decision you would make?" is stated preference about a price we invented.* So we do not ask it. We ask:

1. **"What did the last one cost you — in the fine, in the down time, in the argument with your insurance company?"**
2. **"What do you pay today for anything that touches your logs? To whom? What happened when you stopped?"**
3. **"If I told you it was *impossible* — not unlikely — that you would lose your operating authority for falsified records, what would it be worth per month for that to not be a thing?"**
4. **"What is the most you would pay per month before you'd rather handle it yourself?"**

Then we price against *his* number, not ours.

---

## 4. The opening line (and the one thing not to say)

**Do not say:** "we're an ELD compliance service" (that is the $29 shelf), "we offer 24/7 support" (the incumbent has it at $60 with 100 staff), or "we prevent violations" (we cannot promise it and cannot measure it).

**Do say — the 20-second version:**

> "Hi, this is [name] with [company]. I'm not selling you anything today.
>
> I pulled your record from FMCSA — you're [N] trucks in [city], and you got your operating authority in [month]. Here's the thing I found: **FMCSA audits every new carrier within the first 12 months, and if you don't file a corrective action plan in 45 or 60 days, you lose your registration.** That's published policy, not my opinion.
>
> The audit can be done by submitting documents. Most of the paperwork you need, you already have — you just haven't been told exactly what they ask for, or in what order.
>
> I'd like 20 minutes on the phone to walk you through what the file has to contain. It's free, and if you don't need it, I'll tell you so."

**The credibility line, if they ask how we got their number:** *"It's all public FMCSA data — your USDOT number is in a spreadsheet anyone can download. I didn't call anyone for it."*

**The one line that closes on a deadline:** *"When do you think your audit is? Because if it's before [their 12-month mark], this is a two-week job, not a scramble."*

**Then stop talking.** The panel's rule: you are buying permission, not pitching. Interruption costs whatever the customer would have done instead.

---

## 5. What to do with the answers (so the interviews are not just nice)

Record every call **with consent** — one line at the top: *"Is it OK if I record this? It saves me writing down your words wrong, and you'll get the free review either way."* Then transcribe the money and fear answers verbatim. Those become the copy.

**Log in the CRM, per call:** DOT number · trucks · state · add date · **the dated event** (audit / renewal / citation / broker request) · what happens today when a driver has a log problem · **what they pay today and to whom** · the verbatim cost of the last event · defect count found in the session · whether they stated the number unprompted · the exact objection · the next step with a date.

**Within 48 hours, send every participant the free written review** — the cab checklist with their own answers marked, and the FMCSA document list. It is the same document the agent gets, with their name on it. That is the artefact that gets forwarded, and forwarding is the only referral engine we have.

---

## 6. The week, in order

| Day | Do | Target |
|---|---|---|
| **1** | 10 calls: 5 ELD resellers/installers, 5 truck-insurance agents, in TX and FL. The ask is one introduction each. | 5 introductions |
| **2** | 25 calls: the first 25 of `first-100.csv`, all in ONE state. Record with consent. | 2–3 sessions booked |
| **3** | 10 glovebox sessions. Meanwhile 25 more calls, same state. | 10 sessions, 4 completed |
| **4** | Send the written reviews to everyone from days 2–3. 25 more calls, same state. | 3 more sessions booked |
| **5** | Complete 8 more sessions. **One broker call:** "I did the review free for [fleet]. Their file had [N] gaps. Want me to do the same for one of yours?" | 10 interviews done |
| **6–7** | Second state. Repeat. Then: **read the transcripts and decide the price.** | 10 interviews + a price decision |

**By day 7 you should have:** ten transcripts, a real defect rate on real small fleets, ten real cost figures, and a price that came from the market rather than from us. **That is what the panel said was missing: the price was marked "confirmed" without a single buyer conversation.**

---

## 7. The three decisions this week feeds

1. **The price.** Do we hold $130/truck/month, or does the market say otherwise? (Kill criterion: if fewer than 3 of 10 will pay above $100, this is a $60–80 scale business and the plan gets rebuilt around that.)
2. **The segment.** Does the dated-event cohort convert better than the unexamined cohort? Which one do we chase?
3. **The defect rate.** If ≥15 of 20 sessions come back clean, the glovebox instrument and the paperwork thesis are both wrong, and we need to know that before anyone spends a dollar of the fixed cost.

**And one thing to watch on every call:** if the owner says the problem is *driver behaviour* rather than paperwork, we are the wrong product. Note it and keep going — that is a finding, not a rejection.

---

## 8. Reproducibility

```bash
python3 research/build_new_entrant_list.py                 # rebuild the full list
python3 research/build_new_entrant_list.py --months 12      # widen the window
```

Public data, no key, no cost. Raw column dictionary saved at `research/data/census-columns.json`. The list refreshes daily, so re-run it before each state campaign.
