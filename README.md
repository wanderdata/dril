# DRIL: Deep Research on a Loop

This repository holds replications, extensions and applications of Deep Research on a Loop (DRIL), a method for building datasets from published sources with AI agents. An agent applies a fixed research instrument to every unit in a defined set (for example, countries by years) and returns, for each unit, coded answers with a verbatim quote and locator for every value, explicit records of what could not be found, and a log of the searches it ran (Afonso, Galiani, Gálvez and Sosa, 2026, NBER Working Paper 35188).

The repository is maintained by Paul Wander (UN-ECLAC). The views expressed are the author's and do not necessarily reflect those of ECLAC or its member States.

## Structure

| Path | Content |
|---|---|
| `dril/` | Shared components used by every project: schemas for the research instrument, unit space, evidence policy and records; validators; verification and coverage tools. To be built once the first projects define what they need. |
| `projects/<name>/` | One folder per application. Each holds its frozen protocol (instrument, unit roster, evidence policy, run parameters), the records produced, verification results and a short paper or note. |
| `docs/method/` | Notes on the method, including changes made to the procedure in the original paper and the reasons for them. |
| `docs/register/` | Research log, decision log and open questions. |
| `references/` | Literature register. Source documents under copyright are not committed. |

## Status

Set-up. Projects will be added as their references and protocols are prepared.

## Reference

Afonso, S., Galiani, S., Gálvez, R. H. and Sosa, R. A. (2026). Deep Research on a Loop: Using AI Agents to Construct Economic Datasets. NBER Working Paper 35188. https://www.nber.org/papers/w35188
