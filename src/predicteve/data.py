"""Data loading utilities for tabular clinical and omics metadata."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

SUPPORTED_TABLE_SUFFIXES = {".csv", ".tsv", ".txt", ".parquet"}


def load_table(path: str | Path, **kwargs) -> pd.DataFrame:
    """Load a delimited or parquet table into a DataFrame."""
    table_path = Path(path)
    suffix = table_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(table_path, **kwargs)
    if suffix in {".tsv", ".txt"}:
        return pd.read_csv(table_path, sep="\t", **kwargs)
    if suffix == ".parquet":
        return pd.read_parquet(table_path, **kwargs)

    supported = ", ".join(sorted(SUPPORTED_TABLE_SUFFIXES))
    raise ValueError(f"Unsupported table format '{suffix}'. Supported: {supported}")


def require_columns(frame: pd.DataFrame, columns: list[str]) -> None:
    """Raise a clear error when expected columns are missing."""
    missing = [column for column in columns if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
