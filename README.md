# ovarian-aging-biomarkers

Python-first research repository for ovarian aging biomarker discovery.

## Aim

`ovarian-aging-biomarkers` is an early-stage research codebase for discovering, prioritizing, and validating biomarkers of ovarian aging from clinical, laboratory, and multi-omics data.

The project is organized to support reproducible analysis from raw data registration through feature engineering, modeling, validation, and reporting.

## Repository Layout

```text
config/                  Dataset registry and analysis configuration
data/
  raw/                   Immutable source files, excluded from git
  interim/               Intermediate cleaned extracts, excluded from git
  processed/             Analysis-ready datasets, excluded from git
  external/              Public reference data and annotations, excluded from git
docs/                    Analysis plan, data dictionary, and research notes
results/
  figures/               Generated plots and visual outputs
  tables/                Generated summary tables
  models/                Serialized model artifacts
  reports/               Rendered analysis reports
  logs/                  Pipeline logs
scripts/                 Command-line entry points for data and analysis tasks
src/ovarian_aging_biomarkers/
                         Reusable project package code
src/predicteve/          Backward-compatible import alias
tests/                   Unit and regression tests
```

## Getting Started

Create the conda environment:

```bash
conda env create -f environment.yml
conda activate ovarian-aging-biomarkers
```

Install the local package in editable mode:

```bash
python -m pip install -e .
```

Validate the setup:

```bash
python scripts/run_analysis.py --help
pytest
```

## Data Management

Raw and derived data are intentionally excluded from git. Register datasets in `config/datasets.yaml` with their provenance, access status, schema notes, and expected local path. Keep raw files immutable and write cleaned outputs to `data/interim/` or `data/processed/`.

## Research Workflow

1. Register each candidate dataset in `config/datasets.yaml`.
2. Document variables and harmonization decisions in `docs/data_dictionary.md`.
3. Keep statistical assumptions, endpoints, and validation decisions in `docs/analysis_plan.md`.
4. Put reusable logic in `src/ovarian_aging_biomarkers/`.
5. Use `scripts/` for repeatable command-line workflows.
6. Save generated artifacts under `results/`.

## Package Naming

The canonical Python package is `ovarian_aging_biomarkers`. The old `predicteve` package name is kept as a compatibility alias while the repository is renamed.
