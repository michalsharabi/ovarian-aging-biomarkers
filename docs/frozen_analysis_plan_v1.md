# Frozen Analysis Plan v1

This document freezes the Sprint 0 analysis logic before any differential-expression results are inspected.

## POC Goal

Build a computational proof of concept for whether ovarian tissue aging has a reproducible biological signature beyond reserve markers such as AMH and AFC, and whether part of that tissue-derived biology could later be translated into circulating biomarkers.

The logic is:

```text
Tissue truth -> reproducibility -> specificity -> blood feasibility -> longitudinal validation -> minimal panel -> product
```

## Hypothesis

Ovarian aging has at least two separable axes:

- Reserve axis: follicle depletion, AMH, AFC.
- Tissue-aging axis: inflammaging, fibrosis, immune remodeling, stromal or granulosa dysfunction, and altered cell-cell communication.

The POC tests whether the tissue-aging axis adds information not captured by AMH alone.

## Sprint 0 Scope

Sprint 0 is a human-first reproducibility and specificity challenge.

Primary human datasets:

- `GSE255690`: human ovarian scRNA-seq and spatial transcriptomics from young, middle, and older donors.
- `GSE202601`: human ovarian snRNA-seq and snATAC-seq from young and reproductively aged donors.

Supportive cross-species dataset:

- Stowers mouse ovarian-aging dataset, used only after a human-derived signature exists.

## Donor Metadata Audit

Before differential expression or integration, construct a donor-level table:

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

Use this table to identify confounding. If age is fully confounded with procurement, diagnosis, or another design feature, record it as a real limitation. Do not assume batch correction can solve fully confounded study design.

## Cell-Type Coverage Audit

The biological replicate is the donor, not the cell.

Before analysis, construct a donor by cell-type coverage table with:

```text
n_cells
library_size
median_genes_per_cell
```

Use broad Level 1 annotations for QC and coverage:

- Granulosa.
- Stromal/Theca.
- Immune.
- Endothelial.
- Vascular/Smooth muscle.

Use Level 2 analysis annotations only when cell types or subtypes can be matched reliably across datasets.

Do not force together non-homologous annotations, including theca with fibroblasts, macrophages with T/NK cells, or subtypes that are dataset-specific.

Primary starting heuristic:

- At least 50 cells or nuclei per donor per cell type.
- At least 3 donors per age group.

Sensitivity:

- Repeat core checks with a 100-cell threshold.

Review library depth and complexity alongside cell counts.

## Frozen Decisions Before DE

Freeze the following before viewing differential-expression results:

- Included cell types.
- QC thresholds.
- Differential-expression method.
- Ranking method.
- Replication criteria.
- Positive controls.
- Pathway databases.

## Pseudobulk DE

Run each human dataset separately.

The pseudobulk unit is:

```text
donor x cell type
```

Aggregation:

```text
counts_gene,donor = sum(counts over cells from same donor and cell type)
```

Do not run differential expression on integrated Seurat, Harmony, or other integrated objects.

Primary model:

```text
~ age_group
```

Do not include covariates with no variation or covariates fully confounded with age. Candidate methods include edgeR-QLF and DESeq2, selected based on the count structure.

## Human Replication

Do not require FDR < 0.05 in both human datasets as the primary replication endpoint because donor N is expected to be small.

Instead evaluate:

- Effect-size concordance using Spearman correlation of log2 fold changes.
- Direction concordance.
- Ranked pathway concordance using GSEA or fgsea and NES agreement.
- Gene-level meta-analysis as supportive evidence only.

## Positive Controls

The pipeline should recover known ovarian-aging biology, including:

- FOXP1 decrease.
- CDKN1A increase.
- mTOR-related changes.
- CEBPD-related regulatory changes.
- Granulosa identity loss.

If these are not recovered, pause and inspect preprocessing, annotation, and pseudobulk construction.

## Orthogonal Support

Use GSE255690 spatial transcriptomics for spatial localization and donor-level age association. Treat it as orthogonal support, not necessarily an independent cohort if donors overlap.

Use GSE202601 snATAC-seq for promoter or enhancer accessibility, DARs, TF motif changes, and regulatory support for RNA-level changes.

Use cross-species mouse evidence only after defining the human signature. Map human genes to mouse one-to-one orthologs and evaluate same-direction aging effects, pathway conservation, and cell-state conservation.

## Tissue-Aging Signature v0

The first signature is a list of genes or modules supported by multiple evidence layers:

- Human replication.
- Pathway consistency.
- Spatial support.
- ATAC support.
- Monotonic age trend.
- Mouse conservation.

This is not yet a blood test.

## Candidate Prioritization

Prioritize candidates on two axes.

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

The gold quadrant is high Axis A plus high Axis B.

## Specificity Challenge

Each candidate must be challenged against systemic aging and inflammation.

Negative controls:

- CRP.
- IL-6.
- GlycA.
- SASP markers.
- General metabolic or inflammatory markers.

The core question is whether the ovarian-derived signature adds information beyond general inflammaging.

## Olink And Nightingale

Olink is the direct protein path:

```text
ovarian tissue gene -> secreted protein -> plasma protein assay
```

Nightingale measures metabolites and lipoproteins, not proteins. Do not map genes directly to Nightingale metabolites. Use Nightingale for systemic metabolic context, negative controls, unbiased metabolomic associations, and downstream correlates.

## Longitudinal Validation

Only after a circulating candidate signature exists, test whether baseline circulating markers predict future ovarian aging.

Possible outcomes:

- Longitudinal AMH decline.
- Ovarian reserve trajectory.
- Final menstrual period timing.
- Menopause within 3-5 years.

Potential cohorts:

- SWAN.
- UK Biobank.
- Cohorts with repeated AMH and stored biospecimens.

## Discordance Phenotype

The most product-relevant group may be:

```text
age-normal AMH
+ high tissue-aging signature
```

The test is whether these women lose ovarian reserve faster over time.

## Minimal Panel

If the signature works, reduce it to a practical panel:

```text
3-10 proteins
+ optional metabolites
+ clinical variables
+ optional PRS
```

## First Go / No-Go

GO if:

- Human datasets show concordance.
- Pathways are consistent.
- Several cell types show age-related biology.
- ATAC or spatial evidence supports the signal.
- Some candidates are plausibly circulating.

NO-GO if:

- Human datasets tell contradictory stories.
- Pathway-level replication is absent.
- All replicated biology is generic inflammation.
- No candidate has a plausible path to blood.

## Sprint 0 Deliverables

Sprint 0 produces:

```text
results/tables/donor_characteristics.tsv
results/tables/donor_celltype_coverage.tsv
results/figures/donor_celltype_coverage_heatmap.png
docs/frozen_analysis_plan_v1.md
```

Do not proceed to pseudobulk differential expression until these deliverables look credible.
