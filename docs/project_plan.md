# Ovarian Aging Biomarker Discovery Plan

## Working Goal

Build a reproducible Python-first workflow to identify biomarker candidates associated with ovarian aging, prioritize robust signals, and prepare them for validation.

## Core Questions

- Which molecular or clinical features track ovarian aging phenotypes?
- Which signals remain stable after adjustment for confounders such as chronological age, batch, treatment, and cohort?
- Can a compact biomarker panel predict ovarian aging status or trajectory in held-out data?
- Which candidates are biologically interpretable and practical for downstream validation?

## Initial Data Model

At minimum, each analysis-ready cohort should define:

- `sample_id`: stable sample identifier
- `subject_id`: stable participant identifier when repeated measures exist
- `phenotype`: ovarian aging label or continuous outcome
- `age`: chronological age when available
- `modality`: data modality such as transcriptomics, proteomics, metabolomics, imaging, or clinical labs
- `batch` and `cohort`: technical and study-source indicators when available

## Sprint 0 Checklist

- Confirm available datasets and access constraints.
- Draft a data dictionary for phenotypes, covariates, and omics feature matrices.
- Decide whether the first outcome is binary, ordinal, or continuous.
- Create a minimal analysis-ready toy dataset for pipeline testing.
- Run the baseline classifier and univariate feature ranking on non-sensitive demo data.

## Analysis Roadmap

1. Data audit and cohort definition
2. Modality-specific preprocessing and quality control
3. Covariate-aware association analysis
4. Feature ranking and stability checks
5. Baseline predictive models
6. Cross-cohort or held-out validation
7. Biological interpretation and reporting
