# Analysis Plan

## Research Aim

Identify and validate biomarker patterns associated with ovarian aging, with attention to reproductive stage, clinical context, measurement timing, and confounding structure.

## Candidate Biomarker Domains

- Reproductive hormones: AMH, FSH, LH, estradiol, progesterone, inhibin B.
- Metabolic markers: glucose, insulin, lipids, HbA1c.
- Inflammatory and immune markers: CRP, cytokines, immune cell profiles.
- Molecular markers: transcriptomic, proteomic, genomic, or epigenetic features when available.
- Clinical signals: cycle regularity, menopause stage, fertility history, symptoms, medication exposures.

## Primary Outcomes

- Ovarian age or reproductive stage proxy.
- Menopause transition status where available.
- Fertility-relevant endpoints where available.
- Longitudinal change in biomarker trajectories where repeated measures exist.

## Core Covariates

- Chronological age.
- BMI or body composition measures.
- Cycle day or measurement timing.
- Hormonal contraception or hormone therapy exposure.
- Relevant medication use.
- Smoking status.
- Assay platform or batch.
- Study site or cohort.

## Data Preparation

1. Register each source dataset in `config/datasets.yaml`.
2. Preserve raw inputs under `data/raw/`.
3. Standardize identifiers, units, dates, and categorical encodings.
4. Record exclusions, missingness rules, and harmonization decisions.
5. Export analysis-ready tables to `data/processed/`.

## Modeling Approach

- Start with descriptive summaries and missingness audits.
- Fit baseline statistical models with prespecified covariates.
- Compare nonlinear and multivariable models only after leakage checks.
- Evaluate calibration, discrimination, and subgroup performance where applicable.
- Prefer interpretable models for primary inference and flexible models for exploratory signal discovery.

## Validation

- Use participant-level splits for predictive analyses.
- Keep repeated measures from the same participant in the same split.
- Validate across cohorts, assay platforms, or time periods when the data permit.
- Report uncertainty intervals and sensitivity analyses.

## Outputs

- Clean tables in `results/tables/`.
- Figures in `results/figures/`.
- Model artifacts in `results/models/`.
- Reproducible reports in `results/reports/`.
