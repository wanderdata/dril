"""Check that every project's expected outputs exist, are non-empty, and that the
reference values quoted in project texts still match the outputs.

Reference values live in tests/reference_values.yaml. Changing one is a decision
(record it in docs/register/decision_log.md with the old and new value).
"""
import sys
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]


def lookup(spec):
    df = pd.read_csv(ROOT / spec["file"], keep_default_na=False)
    if "row" in spec:
        key, val = next(iter(spec["row"].items()))
        df = df[df[key].astype(str) == str(val)]
        if len(df) != 1:
            raise ValueError(f"{spec['file']}: {key}={val} matched {len(df)} rows")
    return df[spec["column"]].iloc[0]


def main():
    ref = yaml.safe_load(open(ROOT / "tests/reference_values.yaml", encoding="utf-8"))
    errors = []
    for f in ref["expected_files"]:
        p = ROOT / f
        if not p.exists() or p.stat().st_size == 0:
            errors.append(f"missing or empty: {f}")
    for name, spec in ref["values"].items():
        try:
            got = lookup(spec)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: {exc}")
            continue
        if abs(float(got) - float(spec["value"])) > spec.get("tol", 0):
            errors.append(f"{name}: output {got}, reference {spec['value']}")
    findings = pd.read_csv(ROOT / "projects/proveedores/output/validation_findings.csv")
    if (findings.get("severity", pd.Series(dtype=str)) == "error").any():
        errors.append("proveedores: validation findings with severity error")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"check_outputs: {len(ref['expected_files'])} files and {len(ref['values'])} reference values OK")


if __name__ == "__main__":
    main()
