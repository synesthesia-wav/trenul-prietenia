# The two customer-facing documents

Two documents go out from every session. They are the mechanism that makes this business work, so they are built once and merged, not written by hand each time.

| Document | Who reads it | What it does |
|---|---|---|
| `cab-review-template.html` | The fleet owner | Page 1 is the review letter — read on a phone, forwarded to an agent or attorney. Page 2 is the checklist — printed, pinned in the truck. |
| `agent-onepager.html` | The insurance agent or broker | One page. The thing that makes an agent send us one of their carriers. |

---

## 1. The cab review

### Generate it

```bash
python3 assets/merge_cab_review.py results.json --dot 9099205 --out review.html
python3 assets/merge_cab_review.py results.json --dot 9099205 --pdf   # also print to PDF
```

`--dot` pulls the carrier's own record from the public FMCSA census file, so the name, USDOT number, city, state, power units, drivers and authority date are never typed by hand and never wrong.

`--print-template` produces a blank form with every field marked, to print and fill in by hand when you have the session on paper.

### The results file

```json
{
  "session_date": "2026-10-21",
  "reviewer": "V. Vanica",
  "source_date": "2026-10-19",
  "event_price_line": "a fixed fee, quoted before we start",
  "cab":  { "dtransfer": "y", "malfsheet": "n", "grids": "n" },
  "file": { "driverslist": "y", "licenses": "y", "rods": "n" }
}
```

Values: **`y`** in place · **`n`** missing · **`p`** not checked. Anything you did not record defaults to `p`, never silently to "in place". The four cab keys and twelve file keys are in `merge_cab_review.py` (`CAB_ORDER`, `FILE_ORDER`).

### What it does for you

- **The five things to do first are derived, not written.** They are the worst missing cab items and the worst missing file gaps, in the priority order in the script, each with its regulation and a sentence saying why it matters. Override with `"top_five": [...]` when you want to write them yourself.
- **Unresolved fields render as the word `MISSING`**, not as a blank, so a broken merge is obvious rather than shipping a document with holes in it.

### Before you send it

- [ ] Every number and citation still reads correctly for this carrier.
- [ ] The event price line is filled in, or deliberately left as "quoted before we start".
- [ ] Nothing in it promises an audit outcome. It is a paperwork review, not a representation.
- [ ] The disclaimer is intact at the bottom of page 1.
- [ ] Print it, read it once yourself, then send.

### Printing

Open the HTML in a browser and print to PDF: **Letter, default margins, background graphics ON** (the checkboxes and the rules are background colours). Chrome's `--print-to-pdf` works too:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=review.pdf review.html
```

---

## 2. The agent one-pager

### Generate it

```bash
python3 assets/merge_cab_review.py --agent config.json --out agent.html
```

```json
{ "our_name": "V. Vanica", "our_title": "Founder",
  "our_phone": "+1 ...", "our_email": "...",
  "agency_name": "Joe Morten & Son" }
```

`agency_name` only appears in the browser tab title. Put the agent's name on the copy you email them — or leave it as their name in the body text when you write to them personally, and send a clean copy with your own details.

### Three rules baked into this document

1. **No per-truck price, anywhere.** A per-truck number is a software unit, and it invites the $29 comparison. The one-pager sells an outcome and an introduction.
2. **It leads with their money, not our service.** $34,116 per offence per day for operating after a final Unsatisfactory rating, $15,846 for knowing falsification, and the consequences of a revoked registration. All verified against Part 386 Appendix B and 385.13.
3. **It says what we do not do.** For an agent with a book, the sentence *"we will not touch your insured's DQ files or their drug programme"* is what makes them send it. It is also true, and it is the same rule as our reject-list in `PLAN.md` §11.

---

## 3. The rule underneath both documents

**No number in a customer-facing document without its source and a pull date.** Both documents carry the check date in the footer.

This is not a formality. We published the wrong sentence once — the Sisic sentencing recommendation instead of the judgment — in six documents, and it would have been disproved by a prospect in one search. A seller caught overstating a record has no credibility left to sell a compliance file with.

**Before every campaign, re-verify the figures in the agent one-pager.** They are regulatory maximums, and the penalty schedule is adjusted for inflation — it moves. If the date in the footer is more than a few months old, re-check it.

---

## 4. What we are not sending

- **No monthly activity report.** Twelve pages of activity is a document nobody forwards. The monthly artifact is one page: three things you did not know, and here is the file.
- **No outcome claims.** "We reduce violations" is unsupportable: no published effect size exists for outsourced ELD or compliance services, and the research log's own disconfirming pass found the null result. We sell the file and the process.
- **No price comparison** with the $25–65 automation tier or the $60 offshore desk. If a buyer raises it, refuse the comparison and say who does that work well.
- **No filings.** DQ files, drug and alcohol, clearinghouse, IFTA, UCR, permits, vehicle maintenance — refuse and refer. See `PLAN.md` §11.
