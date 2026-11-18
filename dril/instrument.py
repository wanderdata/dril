"""Research instruments: loading, and converting between stored labels and codes.

An instrument is a YAML file with the fields used below (see
projects/proveedores/instrument/stage2_V260721.yaml for an example). It is the
authoritative specification of a DRIL run: the validator, the coverage tables and
the derived data all read it, so that they cannot drift apart.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
import yaml

CODED_KINDS = ("categorical", "multicategorical")


@dataclass
class Variable:
    name: str
    kind: str
    question: str = ""
    block: str = ""
    codes: dict[str, str] = field(default_factory=dict)

    @property
    def label_to_code(self) -> dict[str, str]:
        return {label: code for code, label in self.codes.items()}


@dataclass
class Instrument:
    id: str
    version: str
    unit_id: str
    prefilled: list[str]
    variables: list[Variable]
    statuses: list[str]
    status_for_code: dict[str, list[str]]
    evidence_required_statuses: list[str]
    special_codes: dict[str, str]
    dependencies: list[dict]
    status_suffix: str = "_status"
    multivalue_separator: str = "|"
    evidence_fields: list[str] = field(default_factory=list)
    evidence_required_fields: list[str] = field(default_factory=list)

    @classmethod
    def load(cls, path: str | Path) -> "Instrument":
        with open(path, encoding="utf-8") as fh:
            raw = yaml.safe_load(fh)
        raw = dict(raw)
        raw.pop("description", None)
        raw["variables"] = [Variable(**{k: (({str(a): str(b) for a, b in v.items()}) if k == "codes" else v)
                                        for k, v in var.items()})
                            for var in raw["variables"]]
        raw["status_for_code"] = {str(k): v for k, v in raw["status_for_code"].items()}
        raw["special_codes"] = {k: str(v) for k, v in raw["special_codes"].items()}
        return cls(**raw)

    @property
    def names(self) -> list[str]:
        return [v.name for v in self.variables]

    def var(self, name: str) -> Variable:
        for v in self.variables:
            if v.name == name:
                return v
        raise KeyError(name)

    def status_col(self, name: str) -> str:
        return name + self.status_suffix

    @property
    def special(self) -> set[str]:
        return set(self.special_codes.values())


def labels_to_codes(records: pd.DataFrame, instrument: Instrument) -> tuple[pd.DataFrame, list[tuple]]:
    """Replace value labels by codes in categorical variables.

    Values that are already codes are kept. Returns the converted frame and a list of
    (unit, variable, value) for values that are neither a code nor a label, which the
    caller should treat as errors.
    """
    out = records.copy()
    unmapped = []
    sep = instrument.multivalue_separator
    for var in instrument.variables:
        if var.kind not in CODED_KINDS:
            continue
        l2c = var.label_to_code

        def conv(value, unit):
            parts = [p.strip() for p in str(value).split(sep)] if var.kind == "multicategorical" else [str(value).strip()]
            res = []
            for p in parts:
                if p in var.codes:
                    res.append(p)
                elif p in l2c:
                    res.append(l2c[p])
                else:
                    unmapped.append((unit, var.name, p))
                    res.append(p)
            return sep.join(res)

        out[var.name] = [conv(val, unit) for val, unit in zip(out[var.name], out[instrument.unit_id])]
    return out, unmapped
