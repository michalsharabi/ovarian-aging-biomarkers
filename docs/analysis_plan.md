# Analysis Plan

## Research Aim

Build a proof of concept that tests whether ovarian tissue aging has a reproducible biological signature beyond reserve markers such as AMH and AFC, and whether part of that tissue-derived signal can eventually be translated into circulating biomarkers.

The operating logic is:

```text
Tissue truth -> reproducibility -> specificity -> blood feasibility -> longitudinal validation -> minimal panel -> product
```

The first go/no-go is not a blood biomarker and not machine learning. It is whether human ovarian aging biology replicates across datasets at the donor, cell-type, and pathway level.

## Working Hypothesis

Ovarian aging has at least two axes:

- Reserve axis: follicle depletion, AMH, AFC.
- Tissue-aging axis: inflammaging, fibrosis, immune remodeling, stromal or granulosa dysfunction, and altered cell-cell communication.

The project asks whether the tissue-aging axis adds information that is not captured by AMH alone.

## Candidate Biomarker Domains

- Reproductive hormones: AMH, FSH, LH, estradiol, progesterone, inhibin B.
- Metabolic markers: glucose, insulin, lipids, HbA1c.
- Inflammatory and immune markers: CRP, cytokines, immune cell profiles.
- Molecular markers: transcriptomic, proteomic, genomic, epigenetic, or chromatin-accessibility features when available.
- Clinical signals: cycle regularity, menopause stage, fertility history, symptoms, medication exposures.

## Sprint 0 Datasets

- `GSE255690`: human ovarian scRNA-seq and spatial transcriptomics from young, middle, and older donors.
- `GSE202601`: human ovarian snRNA-seq and snATAC-seq from young and reproductively aged donors.
- Stowers mouse ovarian-aging dataset: cross-species mechanistic support only, after a human signature exists.

## Sprint 0 Outputs

- `results/tables/donor_characteristics.tsv`
- `results/tables/donor_celltype_coverage.tsv`
- `results/figures/donor_celltype_coverage_heatmap.png`
- `docs/frozen_analysis_plan_v1.md`

Only after these look credible should the project move to pseudobulk differential expression.

## Primary Outcomes For Later Phases

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
- Procurement type.
- Postmortem interval where relevant.
- Cycle phase where available.

## Data Preparation

1. Register each source dataset in `config/datasets.yaml`.
2. Preserve raw inputs under `data/raw/`.
3. Standardize identifiers, units, dates, and categorical encodings.
4. Record exclusions, missingness rules, and harmonization decisions.
5. Export analysis-ready tables to `data/processed/`.

## Donor Metadata Audit

Before differential expression or integration, build a donor-level table with:

```text
dataset_id
donor_id
age
age_group
BMI
procurement_type
diagnosis_or_cause_of_death
PMI
cycle_phase
modality
```

The goal is to identify confounding, especially whether age is confounded with procurement or diagnosis. Fully confounded variables should be recorded as real limitations, not treated as fixable by batch correction.

## Cell-Type Coverage Audit

The biological replicate is the donor, not the cell.

Build a donor by cell-type coverage table with:

```text
n_cells
library_size
median_genes_per_cell
```

Use two annotation levels:

- Level 1 broad annotations for QC and coverage: granulosa, stromal/theca, immune, endothelial, vascular/smooth muscle.
- Level 2 analysis annotations only for cell types or subtypes that have reliable correspondence across human datasets.

Do not force non-homologous labels together, including theca with fibroblasts, macrophages with T/NK cells, or dataset-specific subtypes that do not align.

Initial inclusion heuristic:

- At least 50 cells or nuclei per donor per cell type.
- At least 3 donors per age group.

Sensitivity analysis:

- Repeat key checks with a 100-cell threshold.

These thresholds are starting points, not biological laws. Library depth and complexity must also be reviewed.

## Frozen Plan Requirement

Before looking at differential-expression results, freeze:

- Included cell types.
- QC thresholds.
- Differential-expression method.
- Ranking method.
- Replication criteria.
- Positive controls.
- Pathway databases.

## Modeling Approach

- Start with descriptive summaries and missingness audits.
- Fit baseline statistical models with prespecified covariates.
- Compare nonlinear and multivariable models only after leakage checks.
- Evaluate calibration, discrimination, and subgroup performance where applicable.
- Prefer interpretable models for primary inference and flexible models for exploratory signal discovery.

## Pseudobulk Differential Expression

Run each human dataset separately.

The pseudobulk unit is:

```text
donor x cell type
```

Aggregate counts as:

```text
counts_gene,donor = sum(counts over cells from the same donor and cell type)
```

Do not run differential expression on integrated Seurat, Harmony, or similar integrated objects.

Primary model:

```text
~ age_group
```

Do not include covariates with no variation or covariates that are fully confounded with age. Candidate methods include edgeR-QLF and DESeq2, chosen based on data structure.

## Human Replication Criteria

Because donor N is expected to be small, do not require FDR < 0.05 in both human datasets as the primary replication definition.

Assess replication in layers:

- Effect-size concordance: Spearman correlation of log2 fold changes.
- Direction concordance: whether genes change in the same direction.
- Ranked pathway analysis: GSEA or fgsea using Wald or moderated t statistics.
- Gene-level meta-analysis: supportive only, not the primary endpoint.

## Positive Controls

The pipeline should recover previously described ovarian-aging biology, including:

- FOXP1 decrease.
- CDKN1A increase.
- mTOR-related changes.
- CEBPD-related regulatory changes.
- Granulosa identity loss.

If known signals cannot be recovered, pause and inspect preprocessing, annotation, and pseudobulk construction before proceeding.

## Validation

- Use participant-level splits for predictive analyses.
- Keep repeated measures from the same participant in the same split.
- Validate across cohorts, assay platforms, or time periods when the data permit.
- Report uncertainty intervals and sensitivity analyses.

## Orthogonal Support

Use GSE255690 spatial transcriptomics for localization and donor-level age association. Treat it as orthogonal support rather than a fully independent cohort if donors overlap.

Use GSE202601 snATAC-seq for concordant promoter or enhancer accessibility, DARs, TF motif changes, and regulatory support for RNA-level genes.

Use the Stowers mouse ovarian-aging dataset only after the human signature is defined. Map human genes to mouse one-to-one orthologs and look for same-direction aging effects, pathway conservation, and cell-state conservation.

## Tissue-Aging Signature v0

The first signature is a list of genes or modules with multi-layer evidence:

- Human replication.
- Pathway consistency.
- Spatial support.
- ATAC support.
- Monotonic age trend.
- Mouse conservation.

This is not yet a blood test.

## Candidate Prioritization

Use two axes rather than one composite score.

Axis A: ovarian aging biology evidence.

- Same-direction effect.
- Effect size.
- Rank consistency.
- Pathway support.
- Monotonicity.
- ATAC support.
- Spatial support.
- Mouse conservation.

Axis B: circulating biomarker feasibility and specificity.

- Secreted or shed protein.
- Plasma detectability.
- Olink availability.
- Tissue enrichment.
- Low liver, adipose, and blood background.
- Low dependence on generic systemic inflammation.

The gold quadrant is high Axis A and high Axis B.

## Specificity Challenge

Each candidate must be challenged against generic systemic aging and inflammation. Negative controls include CRP, IL-6, GlycA, SASP markers, and general metabolic or inflammatory markers.

The key question is whether the ovarian-derived signature adds information beyond general inflammaging. If not, there is no ovarian-specific product.

## Circulating Validation Strategy

Olink is the direct protein path:

```text
ovarian tissue gene -> secreted protein -> plasma protein assay
```

Nightingale is separate. It measures metabolites and lipoproteins, not proteins, so genes should not be mapped directly to Nightingale metabolites. Use Nightingale for systemic metabolic context, negative controls, unbiased metabolomic associations, and possible downstream correlates.

## Longitudinal Human Validation

Only after a circulating candidate signature exists, test whether baseline circulating markers predict future ovarian aging. Possible outcomes include AMH decline, ovarian reserve trajectory, final menstrual period timing, and menopause within 3-5 years.

Potential cohorts include SWAN, UK Biobank, and cohorts with repeated AMH plus stored biospecimens.

## Discordance Phenotype

The most important product-relevant group may be:

```text
age-normal AMH
+ high tissue-aging signature
```

The question is whether these women lose ovarian reserve faster over time. If yes, the signature adds information beyond an AMH snapshot.

## Minimal Biomarker Panel

If the signature works, reduce it to a practical panel:

```text
3-10 proteins
+ optional metabolites
+ clinical variables
+ optional PRS
```

## Outputs

- Clean tables in `results/tables/`.
- Figures in `results/figures/`.
- Model artifacts in `results/models/`.
- Reproducible reports in `results/reports/`.

## Go / No-Go

GO if human datasets show concordance, pathways are consistent, several cell types show age-related biology, there is ATAC or spatial support, and some candidates are plausibly circulating.

NO-GO if datasets tell contradictory stories, pathway-level replication is absent, all replicated biology is generic inflammation, or no candidates have a plausible path to blood.
