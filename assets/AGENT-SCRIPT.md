# The Agent Outreach Script

Ten calls on day one: five truck insurance agents, five ELD resellers and installers. **This is where the ten interviews come from.** Cold-calling 4,000 fleet owners to find ten would take three weeks; ten agent calls takes one morning.

**Your one-line job on this call:** get one introduction — one carrier whose paperwork you will review, free, and send to the agent first.

---

## The move that makes the call easy

**Do not ask them to find a carrier. Name one yourself.**

Every agent has the same objection to a referral request: *"find me a client who needs this."* That is work, it is unpaid, and it never happens. So do it for them:

> "I already have a list. There are [N] carriers in [state] that got their operating authority in the last six months. Every one of them is inside the twelve-month window when FMCSA does the New Entrant safety audit, and I can see which ones have a paperwork gap from their own public record. Let me do one of them for free and send it to you first."

That single sentence does four things: it shows you have something they do not, it removes their work, it gives them a client who is about to have a problem, and it puts you in the position of doing them a favour.

---

## Before you dial

- [ ] **The list of 25.** `research/data/state-campaign.csv` — 3–12 power-unit carriers, sorted by state. Pick your state, take 25, and have their names and cities in front of you. You will name one on the call.
- [ ] **One sample review.** Produce a real cab review for one carrier so you can say *"here is what your client receives"* if they ask. `python3 assets/merge_cab_review.py research/sessions-example/_example-session-with-gaps.json --dot 9099205 --pdf`
- [ ] **The one-pager** ready to send afterwards: `assets/agent-onepager.html`.
- [ ] **Two facts in your head**, both verified and both checkable: a carrier that keeps operating after a final **Unsatisfactory** safety rating faces up to **$34,116 per offence, per day** (49 CFR Part 386 App. B; 49 CFR 385.13), and failure to file an acceptable corrective action plan after a failed safety audit **revokes the carrier's USDOT registration** (49 CFR 385.319(c); enforced by 385.325(b)-(c)).
- [ ] **A US entity and E&O in place.** If they are not, you are asking an agent to put their name on something unprotected. Do not make the call until they are — and if they are not yet bound, say so honestly on the call and offer to come back (see the objection table).

---

## Who to call

**Truck insurance agents and brokers** — 5 calls.
- **Fastest route to names:** the NAIC state insurance department lookup, via the NAIC's Insurance Departments page (content.naic.org/state-insurance-departments), which links each state's producer lookup. Every state publishes a licensed-agent search.
- **Fastest route to *relevant* names:** search `commercial truck insurance [city]` and `fleet insurance [city]`. The agencies that advertise for truck business are the ones with the book. Skip national brokers — you need the 5–20 person shop with 30–200 carrier clients.
- **Directory option:** truckinginsurance.org/commercial-truck-insurance-companies, and dotagencies.io (filterable by state, with a "trucking-focused" vs "generalist" split — take the focused ones). **Caveat:** these are lead-generation marketplaces. They may want a quote from you, and they may want the lead themselves. Check before you spend a morning in them.

**ELD resellers and installers** — 5 calls.
- **The best list is official and downloadable:** the FMCSA registered ELD devices list (eld.fmcsa.dot.gov/list, and the full download at eld.fmcsa.dot.gov/list/DownloadAll) carries vendor name, phone, email and address for every self-certified device. Those vendors *are* the resellers.
- **For local small installers:** search `ELD installation [city]` and `ELD service [city]`. The single-truck-shop installer is exactly our buyer.
- **What you are offering them, which is not the same offer:** your customer stops calling *them* about paperwork and starts calling *you*. Their ELD subscription gets stickier, because a fleet with a maintained file has no reason to switch devices.

**One thing to know before you dial a second agency:** some insurance agencies already bundle compliance — the UIIA intermodal directory lists agencies advertising *"insurance, bonds, compliance & IFTA."* Those are **competitors, not leads**. The pitch to them is different: *"we do the hours-of-service file only, so you can keep doing compliance and IFTA and put a specialist next to it."*

---

## The 15-second opener

> "Hi, this is [name] with [company]. I don't sell insurance and I'm not asking for a referral fee. I do hours-of-service paperwork for small fleets, and I'm calling because I have a list of carriers in [state] that are inside the FMCSA new-entrant audit window, and I can see from their own public record whether their paperwork has a gap.
>
> I'd like to do **one** of them free and send it to you before their agent ever sees it. Can I send you one?"

**Then stop talking.** The ask is small, the offer is free, and the first thing you said is that you are not asking for money. Let them answer.

**If they say yes:** *"Great, which carrier would you like me to look at?"* — but if they hesitate, name one yourself from your list of 25.

**If they say "tell me more first":** go to the 90-second version.

---

## The 90-second version

> "Here's the short version.
>
> Every new motor carrier has to pass a safety audit within twelve months of getting its operating authority. That's published FMCSA policy. If the carrier fails that audit, they get forty-five or sixty days to file a corrective action plan — and if they don't, **FMCSA revokes their registration.** Not a fine. The company stops.
>
> The audit can be done by submitting documents, and FMCSA publishes the exact list of documents they ask for. Most small carriers have never seen that list, and their driver qualification file and hours-of-service records are usually a shoebox.
>
> I take that list and assemble it. Every correction I prepare is backed by the document that justifies it, and the driver certifies his own record — I never write in a log. The output is a file, in the order the examiner asks for it.
>
> Here's the part that should interest you: **the carriers who are inside that twelve-month window right now are invisible in your book.** They have no citation, no score, no claim. They look fine. And a carrier that gets an Unsatisfactory rating is a carrier you cannot write for, and a carrier that loses its registration is a cancelled policy.
>
> So: pick one of your carriers inside that window, or let me pick one and show you what their file actually looks like. Either way it costs you nothing, and you get to read it before they do."

**Then ask again:** *"Can I do one for you?"*

---

## The ask, in three words

> "**One carrier.** I'll do it free. It comes to you first."

Repeat it if they push back. Do not ask for a list. Do not ask for a fee. Do not ask for a meeting. **One carrier, free, to them first** is a small enough ask that it works.

---

## Objection handling

| They say | You say |
|---|---|
| **"How much do you charge?"** | "For assembling a file it's a fixed fee, quoted before we start. For a carrier who wants it kept current it's a monthly amount per truck. I'd rather not quote you a number on a cold call — let me do one free and you can judge the work." **Never quote a per-truck number on this call.** |
| **"Who are you? I haven't heard of you."** | "We're not FMCSA and we don't represent anyone before them. We are an independent service that assembles hours-of-service files. Our delivery team is in Chisinau; the contracting entity and the professional liability cover are US, with US claims handling." |
| **"Send me a brochure."** | "I can send you a page, but it's not what will convince you. Let me do one carrier in your state and send you the actual file. That's the thing worth looking at." |
| **"I don't have a client who needs this."** | "Then let me pick one. I have [N] carriers in [state] inside the twelve-month window. If none of them has a paperwork gap, you will have lost nothing but a two-minute read." |
| **"My clients already have compliance covered."** | "By whom?" — then listen. If it is their ELD vendor, the gap is still real (no vendor assembles the FMCSA document list for a $29 subscription). If it is a compliance firm, that firm is our competitor, and we do not want that carrier. |
| **"Isn't this a legal matter?"** | "We assemble documents. Your client's attorney does law. We are careful about the line: we do not make claims about compliance, we do not represent anyone before FMCSA, and we hand over a file with a source document behind every entry." |
| **"Are you US-based?"** | "The delivery is in Moldova. The contracting entity is a US company with US-admitted errors and omissions cover and US claims handling. [If the entity is not yet in place, say so: "Not yet, and I will not sell you anything until it is — I am calling to see if the review is worth doing when it is."]" |
| **"Send me something I can show my carrier."** | "That is exactly what it is for. Give me a carrier and I will send you their own file." |
| **"Call me back next quarter."** | "When is your renewal season? I will call before then, and I will have something by then for you to look at." **Then actually call before then.** |
| **"How do I know you're not selling my clients something?"** | "You see the file before they do. And the work is a fixed fee for a document job, not a subscription you have to keep paying for. If it is not useful, you have spent nothing." |

---

## After they say yes: the forward

Ask them to nominate a carrier, or pick one from your list of 25 and confirm the name and phone with them. Then send this, from your address, with the agent in copy:

> Subject: [Carrier name] — free HOS file review, your copy first
>
> [Agent name],
>
> As agreed, I reviewed the hours-of-service paperwork for [Carrier name] ([city], USDOT [number], [n] power units).
>
> The short version: FMCSA audits every new carrier within twelve months of operating authority, and they got theirs in [month]. If they fail that audit they have forty-five or sixty days to file a corrective action plan, and if they don't, their registration is revoked. The audit is done by submitting documents, and FMCSA publishes the list.
>
> I walked their own public record against that list. The findings are in the attached two pages — page one is the review, page two is the checklist they can print and put in the truck.
>
> It cost you nothing and you have it before they do. If you want it sent to them, say the word and I will.
>
> [Your name]
> [Phone] · [Email]

**Copy the carrier on nothing until the agent says send it.** The agent seeing it first is the entire mechanism. If the agent says "go ahead, send it to them too," then copy the carrier — never send it around the agent.

---

## The 48 hours after

1. Produce the review: `python3 assets/merge_cab_review.py research/sessions/session-<DOT>.json --dot <DOT> --pdf` — or, if the carrier has not had a cab session yet, book the 20-minute glovebox session with them first. **Do not send a review you have not actually done.**
2. Read the PDF yourself before it goes. Every number and citation must read correctly for that carrier.
3. Send it to the agent. Wait.
4. Log it: agent, agency, carrier, date, what they said, and the next step with a date.

---

## Targets for day one

| | |
|---|---|
| Calls | 10 (5 agents, 5 resellers) |
| Time | 90 seconds each, so under 20 minutes of talking |
| Outcome | **5 carriers nominated** — one from each conversation that goes well |
| Then | 5 glovebox sessions booked, 5 reviews sent, 5 agents with something in their hand |
| Follow-up | Every agent called back in seven days with the review attached |

**The number that matters is not calls made. It is agents who have read a file.** Ten calls, five reviews, five agents holding something their client needs — that is the whole of day one, and it is the highest-leverage morning in the plan.

---

## What not to say

- **Never** imply we are FMCSA, work for FMCSA, or are connected to them. We are not, and saying so would be a crime and a lie.
- **Never** promise an audit outcome, a pass, or fewer citations. We sell a file. There is no published evidence that any outsourced compliance service reduces violations — including ours.
- **Never** quote a per-truck price on a cold call. It converts a conversation about the agent's problem into a conversation about our number.
- **Never** disparage a competitor. The three questions do the work: *who is accountable for a correction, can they hand an inspector a document for every change, and does the file exist if the ELD vendor shuts down?*
- **Never** say we handle DQ files, drug and alcohol, clearinghouse, IFTA, UCR, permits or vehicle maintenance. **Refuse and refer** — and saying so out loud is what makes an agent comfortable forwarding us to a client.

---

## One caution worth internalising

The panel's verdict on the insurance channel was that the agent is the substitute for the track record we cannot show. That cuts both ways: **an agent who forwards us once and feels foolish will not forward us again, and word travels fast in a small profession.** Under-promise on the call, over-deliver on the file, and never send an agent something you have not checked. Ten agents in one state, all of whom trust us, is worth more than a hundred who heard of us once.
