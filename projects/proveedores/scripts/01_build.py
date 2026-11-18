"""Build the derived tables from the committed source files.

Checks the SHA-256 of each source file, then writes to data/derived/:
  entities_stage1_rows.csv  the Stage 1 entity file as received, with a row number
  entities.csv              one row per distinct entity (D-006), with Stage 1 and Stage 2 counts
  records.csv               Stage 2 records with categorical labels converted to codes (D-008)
  evidence.csv              Stage 2 evidence rows, with the source domain
"""
import hashlib
import sys
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dril import Instrument, labels_to_codes  # noqa: E402
from dril.countries import iso3  # noqa: E402

SRC = HERE / "data/source"
DER = HERE / "data/derived"
HASHES = {
    "entidades_con_resultados_V260714.xlsx": "e2c7fa8996143f34ea443aa68e45970fdc45d05729deee521565808bf98353a9",
    "resultados_etapa2_compilados_V260721.xlsx": "21bce8eeef7a2447617650d40ee32a04d014903c2981c55b1a2bc8cbf42e3c67",
    "evidencias_etapa2_compiladas_V260721.xlsx": "03c7bdd839586348a521ad7c89a87657ac022789881fc70ff300140f0f55b4a1",
    "diccionario_variables_dril_etapa2_V260721.xlsx": "3323dff20682ae06f5d070018cb62e69ae3be5e95a01d62fb72eeb8767916d94",
}


def check_hashes():
    for name, expected in HASHES.items():
        got = hashlib.sha256((SRC / name).read_bytes()).hexdigest()
        if got != expected:
            raise SystemExit(f"hash mismatch for {name}: {got}")


def main():
    check_hashes()
    DER.mkdir(exist_ok=True)
    inst = Instrument.load(HERE / "instrument/stage2_V260721.yaml")

    rows = pd.read_excel(SRC / "entidades_con_resultados_V260714.xlsx", dtype=str)
    rows.insert(0, "row", range(1, len(rows) + 1))
    rows["iso3"] = rows["pais"].map(iso3)
    rows.to_csv(DER / "entities_stage1_rows.csv", index=False)

    rec = pd.read_excel(SRC / "resultados_etapa2_compilados_V260721.xlsx", dtype=str)
    rec = rec.apply(lambda c: c.str.strip())
    coded, unmapped = labels_to_codes(rec, inst)
    if unmapped:
        raise SystemExit(f"{len(unmapped)} values are neither codes nor labels, e.g. {unmapped[:3]}")
    coded.insert(coded.columns.get_loc("pais") + 1, "iso3", coded["pais"].map(iso3))
    coded.to_csv(DER / "records.csv", index=False)

    # Distinct entities. Duplicated rows in the Stage 1 file are exact copies (D-006);
    # the number of rows per entity is kept as n_stage1_rows.
    ent_cols = ["entity_id", "entidad_input", "pais", "iso3", "entidad_nivel", "tipo_entidad",
                "existe_programa_proveeduria"]
    if rows.groupby("entity_id")[ent_cols[1:]].nunique().gt(1).any().any():
        raise SystemExit("an entity_id has differing attributes across rows")
    ent = rows.drop_duplicates("entity_id")[ent_cols].copy()
    ent["n_stage1_rows"] = ent["entity_id"].map(rows["entity_id"].value_counts())
    ent["n_stage2_initiatives"] = ent["entity_id"].map(coded["entidad_id"].value_counts()).fillna(0).astype(int)
    ent.to_csv(DER / "entities.csv", index=False)

    ev = pd.read_excel(SRC / "evidencias_etapa2_compiladas_V260721.xlsx", dtype=str)
    ev = ev.apply(lambda c: c.str.strip())
    ev.insert(0, "evidence_id", [f"EV{i:05d}" for i in range(1, len(ev) + 1)])
    ev["access_date"] = ev["access_date"].str.slice(0, 10)
    ev["source_domain"] = ev["source_url"].map(lambda u: urlparse(u).netloc.lower().removeprefix("www."))
    ev.to_csv(DER / "evidence.csv", index=False)

    print(f"stage1 rows {len(rows)}, entities {len(ent)}, records {len(coded)}, evidence {len(ev)}")


if __name__ == "__main__":
    main()
