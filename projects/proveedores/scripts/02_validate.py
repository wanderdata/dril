"""Validate the Stage 2 records and evidence against instrument V260721.

Writes output/validation_findings.csv (one row per finding) and
output/validation_summary.csv (findings by check). Exits with an error code if
any finding has severity "error" and --strict is given.
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from dril import Instrument  # noqa: E402
from dril.validate import summarise, validate_evidence, validate_records  # noqa: E402

CHECKS = ["unique_unit", "column_present", "no_empty_value", "no_empty_status", "status_domain",
          "code_status_agreement", "value_domain", "dependency", "evidence_column_present",
          "evidence_unit_known", "evidence_variable_known", "citation_contract", "evidence_for_answer"]


def main(strict=False):
    inst = Instrument.load(HERE / "instrument/stage2_V260721.yaml")
    rec = pd.read_csv(HERE / "data/derived/records.csv", dtype=str, keep_default_na=False)
    ev = pd.read_csv(HERE / "data/derived/evidence.csv", dtype=str, keep_default_na=False)
    f = pd.concat([validate_records(rec, inst), validate_evidence(rec, ev, inst)], ignore_index=True)
    out = HERE / "output"
    out.mkdir(exist_ok=True)
    f.to_csv(out / "validation_findings.csv", index=False)
    s = summarise(f)
    full = pd.DataFrame({"check": CHECKS}).merge(s.groupby("check")["n"].sum().reset_index(), how="left").fillna(0)
    full["n"] = full["n"].astype(int)
    full.to_csv(out / "validation_summary.csv", index=False)
    print(full.to_string(index=False))
    if strict and (f["severity"] == "error").any():
        raise SystemExit(1)


if __name__ == "__main__":
    main(strict="--strict" in sys.argv)
