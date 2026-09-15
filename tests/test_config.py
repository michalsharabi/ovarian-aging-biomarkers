import pandas as pd

from ovarian_aging_biomarkers import __version__
from ovarian_aging_biomarkers.audit import build_celltype_coverage, normalize_donor_metadata
from ovarian_aging_biomarkers.config import load_dataset_registry
from ovarian_aging_biomarkers.data import require_columns
from ovarian_aging_biomarkers.features import rank_univariate_features, zscore
from predicteve.config import load_dataset_registry as load_dataset_registry_alias


def test_version_is_defined() -> None:
    assert __version__


def test_dataset_registry_loads() -> None:
    registry = load_dataset_registry("config/datasets.yaml")

    assert "datasets" in registry
    assert registry["datasets"][0]["id"] == "GSE255690"


def test_predicteve_alias_still_loads_registry() -> None:
    registry = load_dataset_registry_alias("config/datasets.yaml")

    assert registry["datasets"][0]["id"] == "GSE255690"


def test_require_columns_accepts_existing_columns() -> None:
    frame = pd.DataFrame({"sample_id": ["s1"], "age": [42]})
    require_columns(frame, ["sample_id", "age"])


def test_zscore_standardizes_numeric_columns() -> None:
    frame = pd.DataFrame({"a": [1.0, 2.0, 3.0], "label": [0, 1, 1]})
    scaled = zscore(frame)

    assert list(scaled.columns) == ["a", "label"]
    assert round(float(scaled["a"].mean()), 7) == 0.0


def test_rank_univariate_features_returns_sorted_features() -> None:
    features = pd.DataFrame(
        {
            "weak": [1, 1, 2, 2, 3, 3],
            "strong": [0, 0, 0, 10, 10, 10],
        }
    )
    target = pd.Series([0, 0, 0, 1, 1, 1])

    ranked = rank_univariate_features(features, target)

    assert ranked.iloc[0]["feature"] == "strong"


def test_normalize_donor_metadata_adds_frozen_columns() -> None:
    frame = pd.DataFrame(
        {
            "dataset_id": ["GSE255690"],
            "donor_id": ["d1"],
            "age": [31],
            "age_group": ["young"],
            "modality": ["scRNA-seq"],
        }
    )

    normalized = normalize_donor_metadata(frame)

    assert "procurement_type" in normalized.columns
    assert normalized.loc[0, "donor_id"] == "d1"


def test_build_celltype_coverage_summarizes_by_donor_and_cell_type() -> None:
    frame = pd.DataFrame(
        {
            "dataset_id": ["GSE255690", "GSE255690", "GSE255690"],
            "donor_id": ["d1", "d1", "d2"],
            "age_group": ["young", "young", "older"],
            "cell_type": ["Granulosa", "Granulosa", "Immune"],
            "total_counts": [100, 150, 80],
            "n_genes_by_counts": [1200, 1400, 900],
        }
    )

    coverage = build_celltype_coverage(frame)

    assert coverage.loc[0, "n_cells"] == 2
    assert coverage.loc[0, "library_size"] == 250
    assert coverage.loc[0, "median_genes_per_cell"] == 1300
