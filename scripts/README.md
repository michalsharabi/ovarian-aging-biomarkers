# Scripts

Command-line entry points for reproducible data preparation and analysis workflows.

Keep reusable logic in `src/ovarian_aging_biomarkers/` and use scripts as thin orchestration layers.

Sprint 0 entry points:

- `audit_donor_metadata.py`: writes `results/tables/donor_characteristics.tsv`.
- `audit_celltype_coverage.py`: writes `results/tables/donor_celltype_coverage.tsv` and `results/figures/donor_celltype_coverage_heatmap.png`.
- `prepare_data.py`: placeholder for dataset-specific preparation.
- `run_analysis.py`: project utility commands.
