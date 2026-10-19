# HOS / RODS Reconciliation — Operating Procedure

The product. Everything a new employee reads on day one, and everything a carrier can be shown during a pilot.

---

## 0. Two hard rules (non-negotiable, no exceptions, no verbal overrides)

**Rule 1 — We never edit a driver's ELD.** Under 49 CFR 395.8(e)(4)(ii) the driver makes entries into the ELD, and every edit is recorded in an edit history that FMCSA can retrieve. A vendor editing a driver's record leaves a third party's fingerprint in a federal record. So: **we research, prepare, and document; the driver (or an authorized carrier official) makes the entry and signs off.** This is also our best sales point — we can hand an inspector a file for every correction because we never made the changes ourselves.

**Rule 2 — We never propose a correction the source documents do not support.** Not for a large customer, not as a favor, not "just this once." If the documents and the driver's account conflict, we escalate to the carrier and log it. If the request is to reconstruct hours that were not driven, we decline in writing and log the refusal. A refusal log is a control, and it is the first thing an E&O underwriter and an investigator will want to see. A carrier that asks us to break Rule 2 ends the relationship, not just the contract.

Everything below is the machinery that makes those two rules hold at 2am on a Sunday with 200 trucks.

---

## 1. Roles

| Role | Owns |
|---|---|
| **Desk operator** (roster, 3 shifts) | Intake, triage, document research, evidence packs, correction log, driver contact |
| **Reviewer** (second person) | Second-person review per §9; may be a shift lead on the other shift |
| **Shift lead / supervisor** | Escalations, refusals, carrier contact, weekly reconciliation sign-off, QA audits |
| **Compliance lead (partner)** | SOP maintenance, state-rule matrix, monthly report, outcome evidence, carrier audits |
| **Owner** | Contract, pricing, carrier-facing escalations, channel (agents, resellers) |

**Never one person both prepares and approves a Class 2 correction that changes duty status or times.** The reviewer may be on another shift — that is what the shift overlap is for.

---

## 2. The four-class decision tree

Applied to every request, in this order, every time.

```
REQUEST RECEIVED
│
├─ Q1. Is this a true typographical error?
│      (single character or field; does NOT change a duty status,
│       a timestamp, or a driving-hours figure)
│      ├─ YES → CLASS 1 — Typographical
│      │        Driver corrects it. We log it. No documents needed.
│      │        (395.8(e)(4)(ii) exception for typographical edits)
│      └─ NO ↓
│
├─ Q2. Does the request change a duty status, a timestamp, or hours?
│      ├─ NO → CLASS 1 (if clerical) or Class 3 (if disputed) — route accordingly
│      └─ YES ↓
│
├─ Q3. Is the change supported by a source document?
│      (BOL / rate con / dispatch record / GPS or stop trace /
│       scale ticket / fuel card / proof of delivery / driver's
│       own contemporaneous personal record)
│      ├─ NO and the driver says the hours WERE worked
│      │    → CLASS 3 — Disputed / Undocumented
│      │        We do NOT propose a correction.
│      │        We tell the driver exactly what document would support it.
│      │        We log it. We notify the carrier.
│      └─ YES ↓
│
├─ Q4. Is it within 14 days of the date of the record, and does the
│      document support the specific change requested?
│      ├─ NO → CLASS 3 — Disputed / Out of window
│      │        No correction. Logged. Carrier notified.
│      └─ YES ↓
│
└─ CLASS 2 — Document-supported
         We prepare the correction + evidence pack.
         The driver (or authorized carrier official) enters it and signs.
         We log it and retain the pack.
```

**Explicit refusal trigger (Rule 2).** If the request is, in substance, *"make it look like I drove these hours"* or *"remove this violation"* — i.e. the requested change is not supported by any document, or is supported only by the driver's assertion — that is a Class 4 event:

1. Decline in writing, same shift, with a short explanation and an offer of the lawful alternative.
2. Log it as **Class 4 — Refused** with the requester's identity, the exact request, and the reason.
3. Notify the shift lead. If the same driver or the same carrier requests it again within 30 days, the supervisor notifies the owner.
4. If a carrier instructs us to proceed after a refusal, the supervisor declines on our side and the owner decides whether to end the relationship.

**Never** correct a violation to make it disappear. Correct the *record* so it is accurate — sometimes the accurate record still contains the violation, and that is the correct outcome.

---

## 3. Intake

**Channels (all tracked in one queue):** phone (24/7 line), SMS to the fleet's dedicated number, email to the fleet's address, driver portal. Every channel is timestamped on receipt. **The SLA clock starts at receipt, not at first read.**

**Intake form (minimum fields):**

| Field | Note |
|---|---|
| Carrier | Fleet name |
| Driver | Name + which truck |
| Truck | Unit number |
| Requested by | Driver / owner / dispatcher (and their authority) |
| Request type | Question / correction request / new violation / driver complaint / escalation |
| Request text | Driver's own words, verbatim — do not paraphrase the request |
| Related dates | Trip date, delivery date, timeframe involved |
| Documents supplied | BOL, rate con, POD, photos, etc. — list what arrived and what is missing |
| Triage class | 1 / 2 / 3 / 4 (filled by the operator, confirmed by the reviewer for Class 2) |
| SLA | Clock start, first response, resolution |
| Outcome | Resolved / escalated / refused / pending documents |

**Authority check on the first contact with any new fleet:** confirm in writing who is authorized to request corrections on the carrier's behalf. Requests from an unauthorized third party are declined and logged.

---

## 4. Evidence pack — one per correction

The unit of work. One folder or one record per Class 2 correction.

```
EVIDENCE PACK — EP-{{YYYY}}-{{NNNN}}
Carrier · Driver · Truck · Trip date · ELD platform

REQUEST
  Verbatim request, date/time received, requester, requester's authority

DOCUMENTS IN SUPPORT
  1. {{doc name, type, date range, where it came from}}
  2. ...
  (attach or link each; note anything that contradicts the request)

RECONCILIATION
  What the ELD shows now:      {{status / timestamp / hours}}
  What the documents show:      {{status / timestamp / hours}}
  Basis for the proposed change: {{one sentence}}
  Is the change supported?      YES / NO → if NO, this is Class 3 or 4

PROPOSED CORRECTION (for the driver or authorized carrier official to enter)
  Field: {{eld field}}  From: {{current value}}  To: {{proposed value}}
  Reason: {{short, plain language}}
  Note: this entry is made by the driver / authorized official. We do not
  edit the ELD.

PREPARED BY · REVIEWED BY · SENT TO DRIVER · DRIVER CONFIRMED · LOGGED
```

**Plain language matters.** The driver is reading this on a phone at a truck stop. "Change off-duty start from 18:42 to 18:10, supported by the signed rate con (pickup 17:55) and the fuel receipt (18:06)" beats any regulatory phrasing.

---

## 5. Correction log

One row per correction attempt, every class, including refusals. This table is the company's most valuable asset: it is the evidence trail, the QA dataset, the outcome dataset, and the E&O defense in one place.

| Column | Type |
|---|---|
| `log_id` | EP-YYYY-NNNN |
| `date_received` / `time_received` | timestamp |
| `carrier` / `driver` / `truck` | |
| `requested_by` / `authority_verified` | bool |
| `request_text` | verbatim |
| `class` | 1 / 2 / 3 / 4 |
| `source_documents` | list + link |
| `proposed_correction` | field, from, to, reason |
| `made_by` | driver name / authorized official |
| `confirmed_at` | timestamp |
| `reviewed_by` | name |
| `status` | open / resolved / escalated / refused / pending docs |
| `sla_first_response` | seconds |
| `sla_resolution` | seconds |
| `outcome` | what the carrier or driver did next |
| `notes` | anything that matters later |

**Retention:** logs and evidence packs retained **24 months** minimum. The driver's own records are subject to the 6-month retention rule (395.8(j)), but our audit trail must outlive it, because an inspection of an old trip can arrive late.

---

## 6. Weekly reconciliation routine (per fleet, per active truck)

Proactive. This is what "we don't wait for problems" means in practice, and it is the part of the service that reduces violations rather than documenting them after the fact.

| When | What | Output |
|---|---|---|
| **Daily (automated or manual sweep)** | ELD exception feed: unassigned driving time, duty-status gaps, no-break violations, unlogged off-duty periods, device faults, edits without annotation | Exception list, triaged same shift |
| **Daily** | Drivers with a certification or document gap identified overnight | Same-day driver nudge (message, not a call unless urgent) |
| **Weekly** | Reconcile a sample of at least 20% of managed trucks' trips against BOL/rate con/POD | Reconciliation log; corrections raised; disputes escalated |
| **Weekly** | Reject/verify: every Class 2 correction from the week reviewed by a second person | QA sign-off |
| **Weekly** | Expired medical certificates, expiring driver licences, MV-1/annual review dates, 6-month retention due | Compliance calendar entries, flagged to the carrier |
| **Weekly** | State/lane rule changes affecting this fleet's lanes (from the maintained matrix) | Note to the carrier if it affects them |
| **Monthly** | Full fleet reconciliation (all trucks) + report | The monthly report (§8) |
| **Quarterly** | Re-pull the carrier's FMCSA record; compare to the pre-engagement baseline | Percentile movement note — the renewal conversation |

**Coverage target:** every managed truck reconciled at least once per month; every Class 2 correction source-documented; every request answered inside the SLA.

---

## 7. Driver sign-off

The driver makes the entry. We make it easy and give them the evidence.

**Message sent to the driver (template, translate as needed):**
> We checked your log for [date] against the BOL and the pickup record. Here is the correction, with the documents we used: [link]. Please make this entry in your ELD and sign your log for that day — it takes about 30 seconds. If any of this does not match what you remember, reply and we will stop. Nobody can change your log except you.

**Driver reply handling:** if the driver disputes, the request moves to **Class 3** immediately. Do not argue, do not push for the entry, log the dispute, and notify the supervisor. A correction that a driver has not agreed to is a correction that will not survive a dispute later.

**One-page driver form (printable, for fleets without smartphones at the cab):** the correction details, the source documents, and a signature line for the driver and a countersignature for the shift lead.

---

## 8. Monthly report to the carrier (the product)

Sent on a fixed day, whether or not anything happened. **The report is the product** — a carrier that sees a monthly report with three real findings they did not know about will not cancel. Attach the FMCSA data pull.

```
{{CARRIER}} — COMPLIANCE REPORT, {{MONTH}}
Prepared {{DATE}} by {{TEAM}} · baseline: {{BASELINE DATE}}

1. COVERAGE
   Trucks managed: {{N}} · drivers: {{N}} · requests received: {{N}}
   Response times: median {{X}} min · 95th percentile {{X}} min · SLA met: {{X}}%
   Document requests answered: median {{X}} business hours

2. WHAT WE FOUND AND FIXED
   {{N}} corrections prepared, {{N}} confirmed by drivers, {{N}} escalated, {{N}} refused
   Top three recurring issues, and what we did about each

3. DOCUMENTED FINDINGS (per truck / per driver, no speculation)
   Table: driver, date, finding, class, status

4. OUTCOME SNAPSHOT
   Violations and out-of-service results since {{BASELINE}} vs. the pre-engagement baseline
   FMCSA percentile movement, with the pull date
   Plain-language reading — what this means for the next renewal

5. COMPLIANCE CALENDAR
   Expiring medical certificates, licences, MV-1/annual review, retention due, state rule changes

6. COACHING AND DRIVER CONTACT
   {{N}} contacts · topics: {{break discipline, certification, duty status entries, trip planning}}
   Aggregated, not attributed, unless the driver asked us to name them

7. NEXT MONTH
   {{3–5 specific commitments, with dates}}

8. ANYTHING WE COULD NOT DO
   {{requests we could not complete and why — this section builds more trust than any other}}
```

Section 8 is not optional. A report that admits what it could not do is worth more than one that claims everything.

---

## 9. Quality control

- **Second-person review** required for: any Class 2 correction that changes a duty status, a timestamp, or hours; any request that came directly from a carrier owner; any request where the driver subsequently disputed it; plus a **10% random sample** of Class 1 corrections.
- **Monthly audit:** pull 10 random drivers' RODS from 3 managed fleets, reconcile them independently against the correction log, and record every discrepancy. If the discrepancy rate is above 2%, retrain the shift and re-audit.
- **Refusal review:** the compliance lead reviews the entire Class 3 and Class 4 log monthly. A rising refusal count is healthy; a falling one is a warning sign.
- **Every monthly report** is checked by the compliance lead before it goes out. A number that has not been verified does not leave the building.

---

## 10. SLA, service credits, escalation

**What is a request:** a question or a correction request from a driver of a managed fleet, received through an agreed channel, about that driver's hours, logs, documents, or an inspection in progress.

**Response clock:** from receipt to a **substantive human reply** — either a resolution, a prepared correction with documents, or a specific statement of what we need and when we will have it. "We'll look into it" does not stop the clock. An automatic acknowledgement does not count.

| Target | Value |
|---|---|
| Median first response | under 10 minutes |
| 95th-percentile first response | under 30 minutes |
| Document-backed correction prepared | under 4 business hours (or immediately if the driver is roadside) |
| Roadside emergency (driver stopped) | immediate, at any hour, with a call, not a message |

**Not covered:** freight rates and dispatch; loads and brokers; vehicle maintenance and roadside mechanicals; drug and alcohol programs; hiring and driver onboarding paperwork beyond log forms; immigration and HR matters; anything raised by a driver who is not on a managed fleet.

**Service credits:** monthly SLA missed → 10% of that month's fee. Missed two consecutive months → 25% that month. Credits only, capped at one month's fee, and never a cash refund.

**Escalation:** driver safety or emergency → call the carrier's dispatch, then the owner. A legal demand, an FMCSA contact, or any mention of a citation or investigation → notify the owner within **1 hour**, no matter the hour. Any request that would require breaking Rule 1 or Rule 2 → supervisor immediately, owner the same shift.

---

## 11. New fleet onboarding — first ten days

| Day | Action |
|---|---|
| 0 | Contract, SLA, authorization form (who may request corrections), data access, DPA |
| 1 | ELD access live; pull the carrier's FMCRA baseline record; request BOL/rate con/POD feed |
| 2 | Driver roster with trucks and ELD devices; identify the 14-day records exposure (395.8(b)(1)) |
| 3 | Baseline reconciliation: 20% of trucks, to find the existing defects |
| 4 | First exception sweep; driver nudges; certification reminder issued |
| 5 | First weekly reconciliation; first correction evidence packs |
| 7 | First call with the owner: findings, not pitch |
| 10 | First mini-report (coverage + findings) and the first SAFER re-pull |
| 30 | Full month 1 report + full fleet reconciliation + baseline percentile captured |

**The baseline pull on day 1 is non-negotiable.** It is the only way we will ever have our own outcome evidence, and it is the input to every future renewal conversation.
