"""Configuration helpers."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = Path(os.getenv("OVARIAN_AGING_DATA_DIR", os.getenv("PREDICTEVE_DATA_DIR", PROJECT_ROOT / "data")))
RESULTS_DIR = Path(
    os.getenv("OVARIAN_AGING_RESULTS_DIR", os.getenv("PREDICTEVE_RESULTS_DIR", PROJECT_ROOT / "results"))
)


def load_dataset_registry(path: str | Path = "config/datasets.yaml") -> dict[str, Any]:
    """Load the dataset registry YAML file."""
    registry_path = Path(path)
    with registry_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    return data


def ensure_project_dirs() -> None:
    """Create local data and result directories used by analysis scripts."""
    for path in (
        DATA_DIR / "raw",
        DATA_DIR / "external",
        DATA_DIR / "interim",
        DATA_DIR / "processed",
        RESULTS_DIR / "figures",
        RESULTS_DIR / "tables",
        RESULTS_DIR / "models",
        RESULTS_DIR / "reports",
        RESULTS_DIR / "logs",
    ):
        path.mkdir(parents=True, exist_ok=True)
