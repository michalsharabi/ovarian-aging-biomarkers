"""Feature preparation helpers for biomarker discovery."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def numeric_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Return only numeric columns, preserving row order."""
    return frame.select_dtypes(include=[np.number]).copy()


def zscore(frame: pd.DataFrame) -> pd.DataFrame:
    """Standardize numeric features with zero mean and unit variance."""
    numeric = numeric_features(frame)
    std = numeric.std(axis=0, ddof=0).replace(0, np.nan)
    return (numeric - numeric.mean(axis=0)) / std


def rank_univariate_features(features: pd.DataFrame, target: pd.Series) -> pd.DataFrame:
    """Rank numeric features by absolute point-biserial correlation with a binary target."""
    clean_target = target.dropna()
    if clean_target.nunique() != 2:
        raise ValueError("target must contain exactly two classes for univariate ranking")

    aligned = features.loc[clean_target.index]
    rows: list[dict[str, float | str]] = []
    for column in numeric_features(aligned).columns:
        values = aligned[column]
        mask = values.notna()
        if mask.sum() < 3 or values[mask].nunique() < 2:
            continue
        statistic, p_value = stats.pointbiserialr(clean_target[mask], values[mask])
        rows.append(
            {
                "feature": column,
                "correlation": float(statistic),
                "abs_correlation": float(abs(statistic)),
                "p_value": float(p_value),
            }
        )

    return pd.DataFrame(rows).sort_values("abs_correlation", ascending=False).reset_index(drop=True)
