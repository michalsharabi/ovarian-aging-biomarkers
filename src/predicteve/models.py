"""Baseline modeling utilities."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import typer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from predicteve.data import load_table, require_columns

app = typer.Typer(add_completion=False)


@dataclass(frozen=True)
class BaselineResult:
    """Cross-validation summary for a baseline classifier."""

    metric: str
    scores: list[float]

    @property
    def mean(self) -> float:
        return float(pd.Series(self.scores).mean())

    @property
    def std(self) -> float:
        return float(pd.Series(self.scores).std(ddof=0))


def build_baseline_classifier() -> Pipeline:
    """Create a conservative baseline classifier for tabular biomarker features."""
    return Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced")),
        ]
    )


def cross_validate_baseline(
    features: pd.DataFrame,
    target: pd.Series,
    *,
    metric: str = "roc_auc",
    n_splits: int = 5,
) -> BaselineResult:
    """Evaluate the baseline classifier using stratified cross-validation."""
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    model = build_baseline_classifier()
    scores = cross_val_score(model, features, target, cv=cv, scoring=metric)
    return BaselineResult(metric=metric, scores=[float(score) for score in scores])


@app.command()
def baseline(
    table: str = typer.Argument(..., help="CSV/TSV/parquet table with features and target."),
    target_column: str = typer.Option(..., "--target", "-t", help="Binary target column."),
    metric: str = typer.Option("roc_auc", help="Scikit-learn scoring metric."),
) -> None:
    """Run a first-pass baseline classifier on a local tabular dataset."""
    frame = load_table(table)
    require_columns(frame, [target_column])
    y = frame[target_column]
    x = frame.drop(columns=[target_column]).select_dtypes(include="number")
    result = cross_validate_baseline(x, y, metric=metric)
    typer.echo(f"{result.metric}: mean={result.mean:.3f}, std={result.std:.3f}")


def main() -> None:
    app()
