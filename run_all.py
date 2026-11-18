"""Run every project's pipeline in order, then check the outputs.

Each project lists its scripts in PIPELINES. Scripts are run as separate processes
so that projects stay independent (study scripts share names across folders).
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIPELINES = {
    "proveedores": ["01_build.py", "02_validate.py", "03_coverage.py"],
}


def main():
    for project, scripts in PIPELINES.items():
        for s in scripts:
            path = ROOT / "projects" / project / "scripts" / s
            print(f"== {project}/{s}", flush=True)
            subprocess.run([sys.executable, str(path)], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/check_outputs.py")], check=True)


if __name__ == "__main__":
    main()
