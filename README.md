# ELD Support Services — working documents

Managed hours-of-service compliance for US trucking fleets. $130/truck/month, delivered from Moldova.

**The product is the file** — a source-documented, driver-certified correction record the carrier can hand to an inspector, an insurer, a broker or their own attorney. Not monitoring. Not a hotline. Not a monthly report.

**Read in this order:**

| File | What it is | Read it when |
|---|---|---|
| [`PLAN.md`](PLAN.md) | Strategy: the kernel, segments, product design, unit economics, channel mix, 90-day plan, metrics | First — it is the business |
| [`research/strategy-memo.md`](research/strategy-memo.md) | The synthesis of eight advisor lenses: what they agreed on, where they split, what changed, what was rejected | Now — this is the decision record |
| [`research/strategy-panel.md`](research/strategy-panel.md) | The eight briefs unabridged, each with the evidence it cited | When you want to argue with the recommendation |
| [`SALES-PLAYBOOK.md`](SALES-PLAYBOOK.md) | The pitch by audience, the call structure, qualification, the price ladder, objection handling, retention | Before every owner conversation |
| [`RISKS.md`](RISKS.md) | 19 risks ranked by expected cost, each with why it bites, mitigation, and an owner | Before each new channel, contract, or hire |
| [`research/RESEARCH-LOG.md`](research/RESEARCH-LOG.md) | Every researched claim with source grade, pull date, and what it changed — including what could not be verified | Before relying on any number or citation |
| [`research/memo-gate0.md`](research/memo-gate0.md) | The market-research go/no-go: which gates passed, which failed | For the original evidence trail |
| [`research/interview-guides.md`](research/interview-guides.md) | Four interview scripts (fleet owner, insurance agent, ELD reseller, dispatcher) | Before the first interview |
| [`research/raw/2026-10-19/manifest.md`](research/raw/2026-10-19/manifest.md) | Every source opened, with dates and what it was relied on for | When checking a citation |
| [`assets/health-check-build-guide.md`](assets/health-check-build-guide.md) | How to produce the HOS Health Check: sources, denominator rules, the checklist ordered by FMCSA's own violation data, QA, prohibited language | Before producing the first report |
| [`assets/health-check-template.md`](assets/health-check-template.md) | The customer-facing one-page report and the forwardable checklist, with a worked example | Every time you produce a report |
| [`assets/hos-rods-reconciliation-checklist.md`](assets/hos-rods-reconciliation-checklist.md) | The operating procedure: 4-class decision tree, intake, evidence packs, correction log, weekly routine, monthly report, SLA, QC, onboarding | Before the first driver request |

**Two rules that everything else serves** (see `PLAN.md` §2 and the reconciliation checklist §0):

1. **We never edit a driver's ELD.** 49 CFR 395.8(f)(2) requires all entries relating to duty status to be made by the driver; 395.30(d) expressly permits a carrier — or a system acting for one — to *propose* edits, and 395.30(d)(3) requires the driver's electronic confirmation or rejection. We propose with the source document attached; the driver confirms, enters and recertifies.
2. **We never propose a correction the documents do not support.** Disputes escalate to the carrier; requests to create or erase driving time are refused in writing and logged. The refusal log is our moat — and our biggest legal exposure, so it is counsel-gated before publication.

**The facts that decide the business** (all verified; see the research log for sources and pull dates):

- **$130/truck/month is ~2x the automation tier** ($25–65 published) and **~2.2x the offshore anchor** (Turbo ELD, from $2/day/truck, 100+ staff, already native in Arabic, Uzbek and Russian). It defends only against the staffed-HOS tier. **Never compare on price; refuse the comparison.**
- **Most small fleets have no safety score at all** — FMCSA needs three driver inspections with violations before assigning a percentile above zero. "No score because nobody has looked" is the finding, and it is the opening.
- **The documentation codes outnumber the driving codes** in FMCSA's own violation data, and every weight-5 code is a paperwork defect. A small fleet's score is damaged mostly by paperwork, which is what a staffed desk fixes.
- **The first thing we sell is New Entrant safety-audit preparation**: ~58,600 audits a year, 8.7% fail (~5,100 carriers), 45–60 days to a corrective action plan or loss of USDOT registration, and the audit can be conducted **electronically by submitting documents**. The deliverable is a file. The buyer has a hard deadline and a total downside.
- **We have no publishable track record** (the partners' 18-month record is under NDA). We sell on process proof and generate our own evidence from account one.
- **The strongest sales asset is a criminal case** — *United States v. Sisic* (D.R.I.): an 11-truck carrier's owner altered thousands of ELD entries; one driver died in Oklahoma; three years' probation including six months' home incarceration, a $1,000 fine, and a three-year FMCSA debarment; the company is defunct. What ended it was not the messy log but the false second copy he handed to the trooper.
- **No number in a customer-facing document without a source URL and a pull date.** We got the Sisic sentence wrong once, and that rule exists because of it.

**Status:** Gate 0 research and the strategy panel are complete. Blocked on three things only a human can close: the **E&O broker call** (can a Moldova-domiciled provider write E&O with US claims handling?), the **Moldovan accountant** (does the IT Park 7% turnover regime apply?), and **ten owner interviews** (will they pay above $100/truck/month for a document-backed file?). The kill criterion is written down in `PLAN.md` §11 so it cannot be moved later.
