"""Synthetic tests: the validator must find exactly the errors planted in the data."""
from pathlib import Path

import pandas as pd
import pytest
import yaml

from dril import Instrument, labels_to_codes
from dril.validate import validate_evidence, validate_records

SPEC = {
    "id": "toy", "version": "T1", "unit_id": "uid", "prefilled": ["uid", "country"],
    "status_suffix": "_status",
    "special_codes": {"not_applicable": "-88", "not_found": "-99"},
    "statuses": ["answered", "inferred", "proxy_used", "partial_answer",
                 "not_found_after_search", "not_applicable", "conflict_unresolved"],
    "status_for_code": {"-88": ["not_applicable"], "-99": ["not_found_after_search", "conflict_unresolved"]},
    "evidence_required_statuses": ["answered", "inferred", "proxy_used", "partial_answer"],
    "multivalue_separator": "|",
    "evidence_fields": ["uid", "variable", "source_url", "access_date", "source_locator", "evidence_quote"],
    "evidence_required_fields": ["source_url", "access_date", "source_locator", "evidence_quote"],
    "variables": [
        {"name": "subsidy", "kind": "categorical", "codes": {"1": "Yes", "2": "No", "-99": "No info"}},
        {"name": "amount", "kind": "numeric"},
        {"name": "currency", "kind": "currency"},
        {"name": "start", "kind": "year"},
        {"name": "eval_type", "kind": "multicategorical",
         "codes": {"1": "Monitoring", "2": "Impact", "-88": "NA", "-99": "No info"}},
    ],
    "dependencies": [{"if": "subsidy", "equals": "2", "then_not_applicable": ["amount", "currency"], "source": "t"}],
}

COLS = ["uid", "country", "subsidy", "subsidy_status", "amount", "amount_status",
        "currency", "currency_status", "start", "start_status", "eval_type", "eval_type_status"]
CLEAN = [
    ["U1", "CHL", "1", "answered", "1000", "answered", "CLP", "answered", "2019", "answered", "1|2", "answered"],
    ["U2", "PER", "2", "answered", "-88", "not_applicable", "-88", "not_applicable", "-99", "not_found_after_search", "-99", "not_found_after_search"],
    ["U3", "MEX", "-99", "not_found_after_search", "-99", "not_found_after_search", "-99", "not_found_after_search", "2021", "inferred", "1", "proxy_used"],
]
EVIDENCE_KEYS = [("U1", "subsidy"), ("U1", "amount"), ("U1", "currency"), ("U1", "start"), ("U1", "eval_type"),
                 ("U2", "subsidy"), ("U3", "start"), ("U3", "eval_type")]


@pytest.fixture
def inst(tmp_path: Path) -> Instrument:
    p = tmp_path / "toy.yaml"
    p.write_text(yaml.safe_dump(SPEC), encoding="utf-8")
    return Instrument.load(p)


def records(rows=CLEAN):
    return pd.DataFrame([list(r) for r in rows], columns=COLS)


def evidence(keys=EVIDENCE_KEYS):
    return pd.DataFrame([{"uid": u, "variable": v, "source_url": "https://x.gob/p", "access_date": "2026-07-21",
                          "source_locator": "sec. 2", "evidence_quote": "texto"} for u, v in keys])


def test_clean_data_pass(inst):
    assert validate_records(records(), inst).empty
    assert validate_evidence(records(), evidence(), inst).empty


@pytest.mark.parametrize("row,col,value,check", [
    (0, "subsidy", "7", "value_domain"),
    (0, "amount", "mil", "value_domain"),
    (0, "currency", "pesos", "value_domain"),
    (0, "start", "19", "value_domain"),
    (0, "eval_type", "1|9", "value_domain"),
    (0, "eval_type", "1|-88", "value_domain"),
    (1, "amount_status", "not_found_after_search", "code_status_agreement"),  # -88 must be not_applicable
    (2, "amount_status", "answered", "code_status_agreement"),                # -99 with answered
    (0, "start_status", "not_found_after_search", "code_status_agreement"),   # substantive with not found
    (0, "amount", "", "no_empty_value"),
    (0, "amount_status", "", "no_empty_status"),
    (0, "amount_status", "guessed", "status_domain"),
])
def test_planted_error_found_once(inst, row, col, value, check):
    rows = [list(r) for r in CLEAN]
    rows[row][COLS.index(col)] = value
    f = validate_records(records(rows), inst)
    assert list(f["check"]) == [check], f.to_string()
    assert f["unit"].iloc[0] == CLEAN[row][0]


def test_dependency(inst):
    rows = [list(r) for r in CLEAN]
    rows[1][COLS.index("amount")] = "500"            # subsidy = 2 but amount filled, consistently answered
    rows[1][COLS.index("amount_status")] = "answered"
    f = validate_records(records(rows), inst)
    assert list(f["check"]) == ["dependency"] and f["variable"].iloc[0] == "amount"


def test_duplicate_unit(inst):
    rows = [list(r) for r in CLEAN] + [list(CLEAN[0])]
    f = validate_records(records(rows), inst)
    assert set(f["check"]) == {"unique_unit"}


def test_missing_column_stops(inst):
    f = validate_records(records().drop(columns=["start_status"]), inst)
    assert list(f["check"]) == ["column_present"]


def test_evidence_missing_and_contract(inst):
    ev = evidence(EVIDENCE_KEYS[1:])          # drop evidence for U1 subsidy
    ev.loc[0, "evidence_quote"] = ""          # break the citation contract on one row
    ev.loc[len(ev)] = {"uid": "U9", "variable": "colour", "source_url": "https://a", "access_date": "x",
                       "source_locator": "y", "evidence_quote": "z"}
    f = validate_evidence(records(), ev, inst)
    assert sorted(f["check"]) == ["citation_contract", "evidence_for_answer",
                                  "evidence_unit_known", "evidence_variable_known"]
    assert f.loc[f.check == "evidence_for_answer", "variable"].tolist() == ["subsidy"]


def test_labels_to_codes(inst):
    df = records()
    df.loc[0, "subsidy"] = "Yes"
    df.loc[0, "eval_type"] = "Monitoring|Impact"
    df.loc[2, "subsidy"] = "No info"
    out, unmapped = labels_to_codes(df, inst)
    assert out.loc[0, "subsidy"] == "1" and out.loc[0, "eval_type"] == "1|2" and out.loc[2, "subsidy"] == "-99"
    assert unmapped == []
    df.loc[1, "subsidy"] = "Maybe"
    _, unmapped = labels_to_codes(df, inst)
    assert unmapped == [("U2", "subsidy", "Maybe")]
