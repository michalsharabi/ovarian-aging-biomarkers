# predicteve

Python-first project for ovarian aging biomarker discovery.

## Aim

`predicteve` is an early-stage research codebase for discovering, prioritizing, and validating biomarkers of ovarian aging from multi-omics and clinical data.

The project is organized to support reproducible analysis from raw data ingestion through feature engineering, modeling, validation, and reporting.

## Repository Layout

```text
src/predicteve/      Python package code
notebooks/           Exploratory notebooks and analysis narratives
scripts/             Reusable command-line entry points
data/                Local data placeholders; raw data stays out of git
docs/                Project notes, study design, and analysis plans
results/             Local output placeholders; generated results stay out of git
tests/               Automated tests
```

## Suggested First Milestones

1. Define cohorts, phenotype labels, and inclusion/exclusion criteria.
2. Create a data dictionary for clinical variables and omics matrices.
3. Build reproducible preprocessing for each data modality.
4. Establish baseline biomarker-ranking models.
5. Validate candidate biomarkers across datasets or held-out cohorts.

## Development

This repository uses a `src/` Python package layout. After cloning, create a virtual environment and install the package in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e "[dev]"
pytest
```

## Data Policy

Do not commit raw human-subject data, private clinical metadata, credentials, or large generated artifacts. Keep those files local, encrypted, or in an approved controlled storage system.
