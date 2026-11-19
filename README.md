# DRIL: Deep Research on a Loop

This repository holds replications, extensions and applications of Deep Research on a Loop (DRIL), a method for building datasets from published sources with AI agents. An agent applies a fixed research instrument to every unit in a defined set (for example, countries by years) and returns, for each unit, coded answers with a verbatim quote and locator for every value, explicit records of what could not be found, and a log of the searches it ran (Afonso, Galiani, Gálvez and Sosa, 2026, NBER Working Paper 35188).

The repository is maintained by Paul Wander (UN-ECLAC). The views expressed are the author's and do not necessarily reflect those of ECLAC or its member States.

## Structure

| Path | Content |
|---|---|
| `dril/` | Shared components: loading a machine-readable instrument (`instrument.py`), validating records and evidence against it (`validate.py`), country codes and subregions (`countries.py`). Verification and ledger tools will be added as projects need them. |
| `projects/<name>/` | One folder per application. Each holds its frozen protocol (instrument, unit roster, evidence policy, run parameters), the records produced, verification results and a short paper or note. |
| `docs/method/` | Notes on the method, including changes made to the procedure in the original paper and the reasons for them. |
| `docs/register/` | Research log, decision log and open questions. |
| `references/` | Literature register. Source documents under copyright are not committed. |

## Status

Work is parked; see [`STATUS.md`](STATUS.md) for the state of each component and the next steps.

## Projects

| Project | Content |
|---|---|
| [`projects/proveedores`](projects/proveedores) | Public supplier development initiatives in 33 Latin American and Caribbean countries (ECLAC, 2026): protocols, data, validation and coverage tables |

## Reproducing

```
pip install pandas openpyxl pyyaml pytest
python run_all.py   # rebuilds every project from its source files and checks the outputs
pytest              # synthetic tests of the shared tools and checks of quoted values
```

## Reference

Afonso, S., Galiani, S., Gálvez, R. H. and Sosa, R. A. (2026). Deep Research on a Loop: Using AI Agents to Construct Economic Datasets. NBER Working Paper 35188. https://www.nber.org/papers/w35188
