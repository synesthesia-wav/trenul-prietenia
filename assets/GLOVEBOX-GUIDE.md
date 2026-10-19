# The Glovebox Session — 20 minutes

This replaces the research interview. It is not a softer version of it. It is a different and better instrument, because it gives the owner something real in 20 minutes and measures the thing that decides the thesis.

**What you are doing:** letting a fleet owner discover, in his own truck, what an inspector can ask for — and then showing him that FMCSA audits every new carrier within 12 months.

**The order matters, and it is the opposite of what feels natural.**

> **Do not lead with the audit.** Lead with the glovebox. Let him find a gap first, *then* tell him about the deadline. A deadline he has not felt is noise. A deadline right after he has found four things in his own truck is the reason he buys.

---

## Before the call

- [ ] You have the carrier's row from the census file: name, USDOT, city, state, power units, drivers, authority date.
- [ ] You have the **session sheet** open (`assets/session-sheet.html`), and the **cab review template** ready to merge the moment you hang up.
- [ ] You have a quiet 25 minutes. The first ten are the cab check and cannot be compressed.
- [ ] You know the two dates: their 12-month audit mark (authority date + 12 months) and the 45-or-60-day corrective action plan window.

---

## Minute 0–2 — The frame

Say close to this, and nothing more:

> "Hi, this is [name] with [company]. I'm not selling you anything today, and I want you to know that up front.
>
> I pull public FMCSA records, and yours says you got your operating authority in [month]. I would like twenty minutes to walk you through what an inspector can actually ask for in a truck — the paperwork that has to be in the cab, the stuff that is easy to get wrong — and I will tell you what I find.
>
> It takes five minutes. We will do it together, because I am not going to tell you what is missing in your truck when I can just ask you to open the glovebox."

**Permission, not a pitch.** If he says he is busy, ask for twenty minutes later in the day, and only then ask the qualifying questions. If he refuses, log it and move on — a no today is a data point.

**Do not say:** "we are an ELD compliance service" (that is the $29 shelf), "we offer 24/7 support" (the incumbent has it at $60 with 100 staff), "we prevent violations" (we cannot promise it and cannot measure it).

---

## Minute 2–12 — The cab check, live

He opens things. You watch and tick. Nine items, in this order — **the order is the pitch**:

| # | Ask him to | Why here |
|---|---|---|
| 1 | "Show me where the driver keeps his paperwork" | Opens the glovebox. Once it is open, everything after this is easy. |
| 2 | "Is there a sheet that tells the driver how to hand over his hours to an officer?" | 395.22(h)(1) |
| 3 | "Is there a sheet that tells him what to do if the ELD breaks down?" | 395.22(h)(2). **The highest-value item.** Without it he cannot report a malfunction in writing within 24 hours — a weight-5 violation. |
| 4 | "Are there eight days of blank graph grids?" | 395.22(h)(3). This is the paper he needs to rebuild 24 hours plus the previous 7 days. |
| 5 | "Does each driver have his last seven days of records with him?" | 395.8(k)(2) |
| 6 | "Are the logbooks signed and certified by the driver?" | 395.30(b). |
| 7 | "Is the shipping document number going into the log?" | 395.24(c)(iii). This is the number that ties the log to the bill of lading. |
| 8 | "What about driving time with no driver on it — is that explained anywhere?" | 395.32(c). **A carrier duty, not a driver duty** — most owners have never been told that. |
| 9 | "When the ELD malfunctioned last, were you told in writing within 24 hours?" | 395.34(a)(1). |
| — | "Is the annual inspection report in the cab?" | 396.17. |

**Do not correct him. Do not explain the regulation.** You are not there to teach. You are there to find out what is in his truck, and the explanation comes later, in writing, in the review you send him.

**If he has everything:** say so, mean it, and move on. "You are in better shape than most fleets I look at. Let me ask you two questions about deadlines." A clean bill is a good outcome, not a failure — and if most fleets are clean, we need to know that in week one, not month six.

**The sentence to listen for.** When you show him three things missing, does he say the number out loud? *"So I've got three things wrong in there."* That sentence is the whole point of the instrument, and it is the thing a report cannot do.

---

## Minute 12–15 — The file

Do not try to check twelve document sets in a truck stop. Say:

> "There is a second half of this I cannot do from a parking lot — the file itself, in the office. I will send you the exact list FMCSA asks for, in the order they ask for it, and you can tick it off yourself. If you want, I will look at it with you on a call later in the week."

That sentence is doing three jobs: it gives him the list immediately, it plants the second call, and it keeps the session inside twenty minutes.

---

## Minute 15–20 — The six questions

Ask them in this order. They are in the session sheet.

1. **"When did you get your operating authority?"** You already know. Ask it anyway — it starts the clock out loud.
2. **"Do you know when your safety audit is?"** The one that matters. If he does not know, that is the finding, and now it lands because of the glovebox.
3. **"Who actually touches the logs when something goes wrong?"** Owner, office manager, driver, or nobody. If *nobody*, that is the product, and it is worth more than the paperwork.
4. **"What did the last one cost you?"** Fine, down time, the argument with the insurance company. **Get a real number.** "A lot" is not an answer; push once, politely.
5. **"What do you pay today for anything that touches your logs, and to whom?"** The behavioural price signal. **Never offer a number first.**
6. **"If I told you it was *impossible* — not unlikely — that you would lose your operating authority for falsified records, what would it be worth per month for that to not be a thing?"** Then: *"and what is the most you would pay per month before you would rather handle it yourself?"*

**Do not ask "would you pay $130?"** It is stated preference about a price we invented. Questions 4, 5 and 6 give you the price from his side, which is the only kind worth anything.

**Question 6 needs the honest framing first:** *"I am not trying to sell you anything. I am trying to find out whether this is a real problem for you or not, because if it is not, I would rather tell you that and save you the call."*

---

## Minute 20 — The close

Every close ends on a date that belongs to him.

> "I will send you the review tonight — the list, your own answers marked on it, and the two dates. Print page two and put it in the truck.
>
> One question: when do you think your audit is?"

Then stop. Do not fill the silence.

**If the review is going to the agent as well:** ask, on the call. *"Is there someone at your insurance company you would want to see this?"* If he says yes, send it to them **with him copied** — never around him. That is the referral engine, and it only works if he is comfortable with it.

---

## Within 48 hours

1. Merge and send the cab review: `python3 assets/merge_cab_review.py research/sessions/session-<DOT>.json --dot <DOT> --pdf`
2. Check the PDF before it goes. Every number and citation must still read correctly for this carrier.
3. Send it to him. If he named someone at his insurance company, send it to them too, with him copied.
4. Log the session: outcome, whether he stated the number unprompted, and the next step with a date.

---

## What to write down even if you forget everything else

- **Did he state a number unprompted?** This is the single most predictive answer in the whole session. It measures whether the instrument works, not whether he likes us.
- **What was the last thing it cost him, in dollars?**
- **Who touches the logs today?**
- **Did he ask what we charge? If he did not, the review is doing the selling. If he did, we have a price conversation to prepare for.**
- **What was the gap in his own understanding between what he thinks the paperwork is and what the regulation actually requires?** That gap is our product, in his words, and it is the copy for the next ten calls.

---

## The three things this session is measuring

| Measurement | What it decides | Where it lands |
|---|---|---|
| Do ≥15 of 20 sessions find a gap? | Whether the paperwork thesis is real | `research/aggregate_sessions.py` §1 |
| Will ≥3 of 10 pay above $100/truck/month? | Whether $130 is a price or a wish | `research/aggregate_sessions.py` §3, §4 |
| Do ≥25% of sessions become a pilot? | Whether the instrument converts | `research/aggregate_sessions.py` §2, §4 |

**The thresholds were fixed before the first session, so they cannot be moved afterwards.** If the defect rate comes back low, the thesis is wrong and we find out in week one instead of month six — which is the only reason to run this at all.
