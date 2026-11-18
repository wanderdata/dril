# DRIL repository

Replications, extensions and applications of Deep Research on a Loop (Afonso et al., 2026, NBER WP 35188). Author: Paul Wander (UN-ECLAC). See `README.md` for the map.

## Authorship and branches

- Commits are authored as `Paul Wander <pjwander@gmail.com>`; set `git config user.name/user.email` in a fresh clone.
- Work on `dev`. Merge into `main` with `--no-ff` once checks pass, and confirm GitHub Actions passes on both branches (`gh run watch <id> --exit-status`).
- Before every push: `pytest`; after any pipeline change, `python run_all.py` (which ends with `scripts/check_outputs.py`). CI fails if regenerated outputs differ from the committed ones.

## Registers (update in the same commits as the work)

- `docs/register/research_log.md`: dated entries, newest first.
- `docs/register/decision_log.md`: D-nnn; never delete, mark superseded. A changed published number is a decision with old and new values, and `tests/reference_values.yaml` is updated in the same commit.
- `docs/register/open_questions.md`: OQ-nn.
- `references/literature_register.csv`: every source read or cited, with status (verified, abstract only, from memory). Append rows; do not rewrite the file with a CSV writer.

## Projects

- One folder per application in `projects/<name>/` with `protocol/`, `instrument/`, `data/source/` (as delivered, SHA-256 in its README), `data/derived/`, `data/manual/`, `scripts/` (numbered), `output/` (D-004). Register the pipeline in `run_all.py`.
- The machine-readable instrument (YAML) is the specification the validator and tables read. Validate every set of records with `dril.validate`.
- Every number quoted in a project text has an entry in `tests/reference_values.yaml`.
- Country codes and subregions come from `dril/countries.py`; do not keep private copies.
- Protocols and source files are committed unmodified, except to remove personal information (names of reviewers or staff, account names in file metadata), which is recorded as a decision with both hashes.

## Method rules for new runs and verification

- A pre-analysis plan is committed before any verification or rerun outcome is computed, with thresholds for supported, rejected and inconclusive. Choices made after seeing results are labelled as such in the decision log.
- Verification uses a model different from the one that produced the records where possible, a reviewer blind to the coded value, and a hand-coded subsample to measure the reviewer's own error. Quotes are checked against archived copies of the sources programmatically.
- New protocols must record the model, version and host of every run, and must produce a search log.
- The workspace cannot reach most government sites; archiving pages is done on the user's machine with a script from this repository. The user prefers not to link the session to their computer; files come as attachments.

## Writing

Plain, precise English for outside readers. Argued prose, tables for numbers, no bold for emphasis, no dramatic phrasing. State units, samples and caveats; say what is descriptive. Protocols and data stay in their original language (Spanish); documentation is in English.
