"""Sprint 0 audit helpers for donor metadata and cell-type coverage."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from ovarian_aging_biomarkers.data import load_table, require_columns

DONOR_METADATA_COLUMNS = [
    "dataset_id",
    "donor_id",
    "age",
    "age_group",
    "BMI",
    "procurement_type",
    "diagnosis_or_cause_of_death",
    "PMI",
    "cycle_phase",
    "modality",
]


def normalize_donor_metadata(frame: pd.DataFrame) -> pd.DataFrame:
    """Return a donor-level table with the frozen Sprint 0 columns."""
    require_columns(frame, ["dataset_id", "donor_id", "age", "age_group", "modality"])
    normalized = frame.copy()

    for column in DONOR_METADATA_COLUMNS:
        if column not in normalized.columns:
            normalized[column] = pd.NA

    normalized = normalized[DONOR_METADATA_COLUMNS].drop_duplicates()
    return normalized.sort_values(["dataset_id", "age_group", "donor_id"]).reset_index(drop=True)


def write_donor_characteristics(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    """Load donor metadata and write the frozen donor characteristics table."""
    donors = normalize_donor_metadata(load_table(input_path))
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    donors.to_csv(output, sep="\t", index=False)
    return donors


def build_celltype_coverage(
    frame: pd.DataFrame,
    *,
    dataset_col: str = "dataset_id",
    donor_col: str = "donor_id",
    age_group_col: str = "age_group",
    celltype_col: str = "cell_type",
    counts_col: str = "total_counts",
    genes_col: str = "n_genes_by_counts",
) -> pd.DataFrame:
    """Summarize donor by cell-type coverage from cell or nucleus metadata."""
    require_columns(frame, [dataset_col, donor_col, celltype_col])

    group_cols = [dataset_col, donor_col]
    if age_group_col in frame.columns:
        group_cols.append(age_group_col)
    group_cols.append(celltype_col)

    grouped = frame.groupby(group_cols, dropna=False)
    coverage = grouped.size().rename("n_cells").reset_index()

    if counts_col in frame.columns:
        coverage["library_size"] = grouped[counts_col].sum().to_numpy()
    else:
        coverage["library_size"] = pd.NA

    if genes_col in frame.columns:
        coverage["median_genes_per_cell"] = grouped[genes_col].median().to_numpy()
    else:
        coverage["median_genes_per_cell"] = pd.NA

    return coverage.sort_values(group_cols).reset_index(drop=True)


def write_celltype_coverage(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    """Load cell metadata and write donor by cell-type coverage."""
    coverage = build_celltype_coverage(load_table(input_path))
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    coverage.to_csv(output, sep="\t", index=False)
    return coverage
