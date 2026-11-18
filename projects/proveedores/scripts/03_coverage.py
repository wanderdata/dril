"""Coverage, gap and source tables for the supplier-development application. Descriptive only.

Writes to output/:
  funnel_total.csv          entities searched -> candidates -> initiatives characterised
  funnel_by_country.csv     the same by country, with M49 subregion
  funnel_by_level.csv       the same by level of government of the entity
  status_by_variable.csv    status of each Stage 2 variable across the 265 initiatives
  status_by_group.csv       status shares of all cells by subregion and by entity level
  source_types.csv          evidence rows and domains by source type, total and by subregion
  diagnostics.csv           checks beyond the protocol's checklist (D-010)
"""
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dril import Instrument  # noqa: E402
from dril.countries import COUNTRIES  # noqa: E402

OUT = HERE / "output"
STATUSES = ["answered", "inferred", "proxy_used", "partial_answer",
            "not_found_after_search", "not_applicable", "conflict_unresolved"]
GOV = re.compile(r"(\.|^)(gob|gov|gub|gouv|govt|go|gc|mil|leg|jus)\.[a-z]{2}$|\.gov$|\.gob$")
SUB = COUNTRIES.set_index("iso3")["subregion"]


def load():
    inst = Instrument.load(HERE / "instrument/stage2_V260721.yaml")
    ent = pd.read_csv(HERE / "data/derived/entities.csv", dtype=str, keep_default_na=False)
    for c in ["n_stage1_rows", "n_stage2_initiatives", "existe_programa_proveeduria"]:
        ent[c] = ent[c].astype(int)
    rec = pd.read_csv(HERE / "data/derived/records.csv", dtype=str, keep_default_na=False)
    ev = pd.read_csv(HERE / "data/derived/evidence.csv", dtype=str, keep_default_na=False)
    return inst, ent, rec, ev


def funnel(ent: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    e = ent.assign(
        national=ent.entidad_nivel.eq("Nacional").astype(int),
        subnational=ent.entidad_nivel.eq("Subnacional").astype(int),
        stage1_candidates=ent.n_stage1_rows.where(ent.existe_programa_proveeduria == 1, 0),
        with_initiative=(ent.n_stage2_initiatives > 0).astype(int),
        positive_without_initiative=((ent.existe_programa_proveeduria == 1) & (ent.n_stage2_initiatives == 0)).astype(int),
    )
    agg = dict(entities=("entity_id", "size"), national=("national", "sum"), subnational=("subnational", "sum"),
               entities_with_candidate=("existe_programa_proveeduria", "sum"),
               stage1_candidates=("stage1_candidates", "sum"),
               entities_with_initiative=("with_initiative", "sum"),
               positive_entities_without_initiative=("positive_without_initiative", "sum"),
               initiatives=("n_stage2_initiatives", "sum"))
    g = (e.groupby(keys).agg(**agg).reset_index() if keys else
         pd.DataFrame({k: [getattr(e[c], f)()] if f != "size" else [len(e)] for k, (c, f) in agg.items()}))
    g["candidates_dropped_in_review"] = g.stage1_candidates - g.initiatives
    g["initiatives_per_100_entities"] = (100 * g.initiatives / g.entities).round(1)
    return g


def long_status(inst, rec):
    s = rec.melt(id_vars=[inst.unit_id, "iso3", "entidad_nivel", "nivel_programa"],
                 value_vars=[inst.status_col(n) for n in inst.names], var_name="variable", value_name="status")
    s["variable"] = s["variable"].str.removesuffix(inst.status_suffix)
    s["subregion"] = s["iso3"].map(SUB)
    return s


def shares(df, keys):
    t = pd.crosstab([df[k] for k in keys] if len(keys) > 1 else df[keys[0]], df["status"])
    t = t.reindex(columns=STATUSES, fill_value=0)
    n = t.sum(axis=1)
    out = t.div(n, axis=0).round(3).add_prefix("share_")
    out.insert(0, "cells", n)
    return out.reset_index()


def main():
    OUT.mkdir(exist_ok=True)
    inst, ent, rec, ev = load()

    funnel(ent, []).to_csv(OUT / "funnel_total.csv", index=False)
    fc = funnel(ent, ["iso3", "pais"])
    fc.insert(1, "subregion", fc.iso3.map(SUB))
    fc.sort_values("entities", ascending=False).to_csv(OUT / "funnel_by_country.csv", index=False)
    funnel(ent, ["entidad_nivel"]).to_csv(OUT / "funnel_by_level.csv", index=False)

    st = long_status(inst, rec)
    sv = shares(st, ["variable"])
    sv.insert(1, "block", sv.variable.map({v.name: v.block for v in inst.variables}))
    sv["share_substantive"] = (1 - sv.share_not_found_after_search - sv.share_not_applicable
                               - sv.share_conflict_unresolved).round(3)
    sv.set_index("variable").loc[inst.names].reset_index().to_csv(OUT / "status_by_variable.csv", index=False)
    sg = pd.concat([shares(st, ["subregion"]).rename(columns={"subregion": "group"}).assign(dimension="subregion"),
                    shares(st, ["entidad_nivel"]).rename(columns={"entidad_nivel": "group"}).assign(dimension="entity_level"),
                    shares(st.assign(all="all"), ["all"]).rename(columns={"all": "group"}).assign(dimension="total")])
    sg[["dimension"] + [c for c in sg if c != "dimension"]].to_csv(OUT / "status_by_group.csv", index=False)

    # Source types (D-009): government pattern on the domain, otherwise the manual table.
    man = pd.read_csv(HERE / "data/manual/source_domains.csv").set_index("source_domain")["source_type"]
    ev["source_type"] = [("government_or_public_agency" if GOV.search(d) else man.get(d, "unclassified"))
                         for d in ev.source_domain]
    ev = ev.merge(rec[[inst.unit_id, "iso3"]], on=inst.unit_id)
    ev["subregion"] = ev.iso3.map(SUB)
    tot = ev.groupby("source_type").agg(evidence_rows=("evidence_id", "size"), domains=("source_domain", "nunique"))
    tot["share_rows"] = (tot.evidence_rows / tot.evidence_rows.sum()).round(3)
    by = pd.crosstab(ev.source_type, ev.subregion, normalize="columns").round(3).add_prefix("share_rows_")
    tot.join(by).sort_values("evidence_rows", ascending=False).reset_index().to_csv(OUT / "source_types.csv", index=False)

    # Diagnostics beyond the protocol checklist (D-010).
    d = ev.merge(st[[inst.unit_id, "variable", "status", "nivel_programa"]], on=[inst.unit_id, "variable"])
    n_units = d.groupby("evidence_quote")[inst.unit_id].nunique()
    d["quote_shared"] = d.evidence_quote.map(n_units) > 1
    cell = d.groupby([inst.unit_id, "variable", "status", "nivel_programa"]).quote_shared.all().reset_index()
    shared_cells = cell[cell.quote_shared]
    edition = shared_cells[shared_cells.nivel_programa == "4"]
    words = ev.evidence_quote.str.split().str.len()
    num = lambda s: pd.to_numeric(s.where(~s.isin(inst.special)), errors="coerce")  # noqa: E731
    diag = [
        ("evidence_rows", len(ev), "Stage 2 evidence rows"),
        ("distinct_source_urls", ev.source_url.nunique(), ""),
        ("distinct_source_domains", ev.source_domain.nunique(), ""),
        ("quotes_shared_across_initiatives", int((n_units > 1).sum()), "distinct quote strings cited for more than one initiative"),
        ("cells_only_shared_quotes", len(shared_cells), "substantive cells whose every evidence row uses a quote also cited for another initiative"),
        ("edition_cells_only_shared_quotes", len(edition), "same, for initiatives coded as editions of a parent programme (nivel_programa = 4)"),
        ("edition_cells_only_shared_quotes_proxy_used", int((edition.status == "proxy_used").sum()), "of which marked proxy_used, as protocol section 13 requires for parent-programme information"),
        ("edition_cells_only_shared_quotes_not_proxy", int((edition.status != "proxy_used").sum()), "of which marked answered, inferred or partial_answer"),
        ("quotes_three_words_or_fewer", int((words <= 3).sum()), "evidence rows whose quote has at most three words"),
        ("median_quote_words", float(words.median()), ""),
        ("source_date_missing_share", round(float((ev.source_date == "-99").mean()), 3), "share of evidence rows with source_date = -99"),
        ("budget_without_currency", int((num(rec.presupuesto).notna() & (rec.p_moneda == "-99")).sum()), "presupuesto given but p_moneda = -99"),
        ("initiatives_parent_named", int((~rec.programa_madre_nombre.isin(inst.special)).sum()), "initiatives with a named parent programme"),
        ("distinct_parent_programmes", int(rec.loc[~rec.programa_madre_nombre.isin(inst.special), "programa_madre_nombre"].nunique()), ""),
        ("largest_parent_family", int(rec.loc[~rec.programa_madre_nombre.isin(inst.special)].groupby("programa_madre_nombre").size().max()), "initiatives sharing the most common parent programme"),
    ]
    pd.DataFrame(diag, columns=["diagnostic", "value", "definition"]).to_csv(OUT / "diagnostics.csv", index=False)
    print(pd.read_csv(OUT / "funnel_total.csv").T.to_string())


if __name__ == "__main__":
    main()
