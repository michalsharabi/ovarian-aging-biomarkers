"""Project path helpers and runtime settings."""

from __future__ import annotations

import os
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parents[1]
DATA_DIR = Path(os.getenv("PREDICTEVE_DATA_DIR", PROJECT_ROOT / "data"))
RESULTS_DIR = Path(os.getenv("PREDICTEVE_RESULTS_DIR", PROJECT_ROOT / "results"))


def ensure_project_dirs() -> None:
    """Create local data and result directories used by analysis scripts."""
    for path in (DATA_DIR, RESULTS_DIR):
        path.mkdir(parents=True, exist_ok=True)
