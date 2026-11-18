"""Validation of DRIL records and evidence against their instrument.

Each check returns findings as rows (check, unit, variable, detail). A run passes
when no finding has severity "error". The checks generalise the end-of-run checklist
of the ECLAC supplier-development protocol (V260721, section 15) to any instrument;
the check names say which item they implement where one applies.
"""
from __future__ import annotations

import re

import pandas as pd

from .instrument import Instrument

NUMERIC = re.compile(r"-?\d+(\.\d+)?")
YEAR = re.compile(r"\d{4}")
ISO4217 = re.compile(r"[A-Z]{3}")
URL = re.compile(r"https?://\S+")

FINDING_COLUMNS = ["check", "severity", "unit", "variable", "detail"]


def _f(check, unit, variable, detail, severity="error"):
    return {"check": check, "severity": severity, "unit": unit, "variable": variable, "detail": detail}


def _blank(x) -> bool:
    return x is None or (isinstance(x, float) and pd.isna(x)) or str(x).strip() == ""


def validate_records(records: pd.DataFrame, instrument: Instrument) -> pd.DataFrame:
    """Checks on the records table alone. Values must already be codes, not labels."""
    I = instrument
    uid = I.unit_id
    out = []

    # Structure: identifiers unique (15.1), columns present (15.3), no empty cells (15.2).
    for u in records.loc[records[uid].duplicated(keep=False), uid].unique():
        out.append(_f("unique_unit", u, uid, "unit appears more than once"))
    for col in I.prefilled + I.names + [I.status_col(n) for n in I.names]:
        if col not in records.columns:
            out.append(_f("column_present", None, col, "column missing"))
    if any(f["check"] == "column_present" for f in out):
        return pd.DataFrame(out, columns=FINDING_COLUMNS)

    special = I.special
    na_code = I.special_codes["not_applicable"]
    for _, row in records.iterrows():
        u = row[uid]
        for var in I.variables:
            v, s = row[var.name], row[I.status_col(var.name)]
            if _blank(v):
                out.append(_f("no_empty_value", u, var.name, "empty value"))
                continue
            if _blank(s):
                out.append(_f("no_empty_status", u, var.name, "empty status"))
                continue
            v, s = str(v).strip(), str(s).strip()
            if s not in I.statuses:
                out.append(_f("status_domain", u, var.name, f"status {s!r} not allowed"))
            # Special codes and statuses must agree (15.5, 15.6; protocol 6.5).
            if v in I.status_for_code and s not in I.status_for_code[v]:
                out.append(_f("code_status_agreement", u, var.name, f"value {v} with status {s}"))
            if v not in special and s in ("not_applicable", "not_found_after_search"):
                out.append(_f("code_status_agreement", u, var.name, f"substantive value with status {s}"))
            if v in special:
                continue
            # Value domains (15.4, 15.13).
            if var.kind == "categorical" and v not in var.codes:
                out.append(_f("value_domain", u, var.name, f"code {v!r} not in instrument"))
            elif var.kind == "multicategorical":
                bad = [p for p in v.split(I.multivalue_separator) if p.strip() not in var.codes or p.strip() in special]
                if bad:
                    out.append(_f("value_domain", u, var.name, f"codes {bad} not allowed"))
            elif var.kind in ("numeric", "percent") and not NUMERIC.fullmatch(v):
                out.append(_f("value_domain", u, var.name, f"{v!r} is not a number"))
            elif var.kind == "percent" and not 0 <= float(v) <= 100:
                out.append(_f("value_domain", u, var.name, f"{v} outside 0-100"))
            elif var.kind == "year" and not YEAR.fullmatch(v.split(".")[0]):
                out.append(_f("value_domain", u, var.name, f"{v!r} is not a four-digit year"))
            elif var.kind == "currency" and not ISO4217.fullmatch(v):
                out.append(_f("value_domain", u, var.name, f"{v!r} is not an ISO 4217 code"))
            elif var.kind == "url" and not URL.fullmatch(v):
                out.append(_f("value_domain", u, var.name, f"{v!r} is not a URL", severity="warning"))
        # Dependencies (15.7-15.12): "if X = a then Y = -88".
        for dep in I.dependencies:
            if str(row[dep["if"]]).strip() == str(dep["equals"]):
                for y in dep["then_not_applicable"]:
                    if str(row[y]).strip() != na_code:
                        out.append(_f("dependency", u, y,
                                      f"{dep['if']} = {dep['equals']} but {y} = {row[y]} (rule {dep.get('source', '')})"))
    return pd.DataFrame(out, columns=FINDING_COLUMNS)


def validate_evidence(records: pd.DataFrame, evidence: pd.DataFrame, instrument: Instrument) -> pd.DataFrame:
    """Checks linking records and evidence (15.14 and the citation contract)."""
    I = instrument
    uid = I.unit_id
    out = []
    units = set(records[uid])
    for col in I.evidence_fields:
        if col not in evidence.columns:
            out.append(_f("evidence_column_present", None, col, "column missing"))
    if out:
        return pd.DataFrame(out, columns=FINDING_COLUMNS)
    for i, row in evidence.iterrows():
        if row[uid] not in units:
            out.append(_f("evidence_unit_known", row[uid], row["variable"], f"evidence row {i}: unit not in records"))
        if row["variable"] not in I.names:
            out.append(_f("evidence_variable_known", row[uid], row["variable"], f"evidence row {i}: variable not in instrument"))
        for col in I.evidence_required_fields:
            if _blank(row[col]) or str(row[col]).strip() in I.special:
                out.append(_f("citation_contract", row[uid], row["variable"], f"evidence row {i}: {col} missing"))
    have = set(zip(evidence[uid], evidence["variable"]))
    for _, row in records.iterrows():
        for var in I.variables:
            s = str(row[I.status_col(var.name)]).strip()
            if s in I.evidence_required_statuses and (row[uid], var.name) not in have:
                out.append(_f("evidence_for_answer", row[uid], var.name, f"status {s} without evidence"))
    return pd.DataFrame(out, columns=FINDING_COLUMNS)


def summarise(findings: pd.DataFrame) -> pd.DataFrame:
    if findings.empty:
        return pd.DataFrame(columns=["check", "severity", "n"])
    return findings.groupby(["check", "severity"]).size().rename("n").reset_index()
