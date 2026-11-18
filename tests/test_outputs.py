"""The committed outputs must match the reference values quoted in project texts."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_check_outputs():
    r = subprocess.run([sys.executable, str(ROOT / "scripts/check_outputs.py")], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_countries_unique():
    from dril.countries import COUNTRIES, iso3
    assert COUNTRIES.iso3.is_unique and COUNTRIES.name_es.is_unique and len(COUNTRIES) == 33
    assert iso3("Trinidad y Tobago") == "TTO"
