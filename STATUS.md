# Status and next steps

Parked on 2026-11-19. This file is the starting point when work resumes: it says what exists, what is unfinished, and what each next step needs. Update it whenever work is parked again.

## How to resume

Open a session with this repository attached and say, for example: "Resume DRIL from STATUS.md, starting with step 1." The repository's `CLAUDE.md` carries the working conventions (branches, registers, checks). Before starting, run `pytest` and `python run_all.py` to confirm the committed state reproduces.

## State

| Component | State |
|---|---|
| Repository skeleton, registers, CI | Done. CI rebuilds every project from source and fails if outputs change (D-012). |
| `dril/` shared tools | Instrument loader, validator (synthetic tests), country table. No verification, archiving or ledger tools yet. |
| `projects/proveedores` | Archived, validated and described (coverage, gaps, sources, diagnostics). Not verified; no second run. |
| Other projects (GTED update, technological extension, STI evaluations) | Not started; no materials received. |
| Method notes (`docs/method/`) | Empty. |

The main findings so far, the correction of the entity count (D-006) and the open questions OQ-06 to OQ-12 are in `projects/proveedores/README.md` and `docs/register/`.

## Next steps for proveedores, in order

1. Pre-analysis plan for verification (`projects/proveedores/plan/verification_plan.md`), committed before any verification outcome is computed. To specify:
   - Sample: about 40 initiatives, stratified by subregion and by the dominant source type of their evidence, drawn with a fixed seed; all evidence rows of the sampled initiatives (roughly 900). Oversample the cells flagged in OQ-06 (edition cells resting only on shared quotes) and OQ-07 (quotes of three words or fewer), with weights to recover population shares.
   - Test A, quote presence: share of evidence quotes found verbatim (after normalising whitespace, case and accents) in the archived text of the cited page; with a fuzzy-match threshold fixed in advance for PDFs. Report the share with a confidence interval, by source type.
   - Test B, support: a reviewer that sees the source passage and the question but not the coded value answers the question; agreement with the coded value by variable, with Cohen's kappa for categorical variables. The reviewer should be a different model family from the original run, which is unknown (OQ-12), so record which model is used.
   - Reviewer error: Paul (or a research assistant) hand-codes a subsample of about 100 cells blind to both the original value and the reviewer's answer.
   - Decision thresholds for "supported", "rejected" and "inconclusive", set before seeing results, and minimum detectable differences given the sample size.
2. Archiving script for the user's machine (`scripts/archive_sources.py`, repository level): reads a list of URLs, saves each page (HTML or PDF) with its SHA-256 and retrieval time, records failures, and writes a manifest. Paul runs it locally on the sampled URLs and attaches the output folder. The workspace cannot reach government sites, and WebFetch returns summaries, not page text, so it cannot be used for Test A.
3. Run the verification, log every post-result choice as a decision, write a short results section in the project README.
4. Independent Stage 1 rerun on a sample of entities, including those reviewed externally in Chile and Colombia, under a frozen copy of V260714 amended only to require a search log and to record the model and host. Measure how many initiatives each run finds that the other misses. Needs its own pre-analysis plan.
5. Update run (later): re-code variables likely to have changed since July 2026, starting with `vigencia`, with an append-only ledger so earlier values are superseded, not overwritten.

## What is needed from Paul

| Item | Needed for | Status |
|---|---|---|
| Review of `projects/proveedores/data/manual/source_domains.csv` (12 domains marked uncertain; the rest classified from memory) | Source-type tables, sample stratification | Open |
| Confirmation that the 1,102-entity count (D-006) is right, and correction of slides 16–17 and CEPAL (2026c) if so | Published figures | Open |
| Running the archiving script locally and attaching the output | Verification, Test A | After step 2 |
| Hand-coding about 100 cells | Measuring the reviewer's error | After step 1 |
| Model and host of the original run, if it can be found | OQ-12 | Unknown at present |
| Materials for the next projects (protocols, outputs, earlier hand-coded data) | New projects | When available |
| Licence for the repository (none set) | Reuse by others | Open |

## Not to forget

- The GitHub Actions runner warns that Node.js 20 actions are deprecated (`actions/checkout@v4`, `actions/setup-python@v5`); bump the versions when they are next touched.
- Source PDFs of copyrighted papers are not committed (D-003); the NBER paper and the CEPAL presentation were read from attachments in the session of 2026-11-18.
