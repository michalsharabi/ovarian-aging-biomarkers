# Data Dictionary

Use this document to track harmonized variables across datasets. Add dataset-specific aliases as new sources are registered.

| Field | Type | Domain | Description | Units / Coding | Source Aliases | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| dataset_id | string | identifiers | Dataset accession or local dataset identifier. | controlled ID | study_id, accession | Required for multi-dataset analyses. |
| donor_id | string | identifiers | De-identified biological donor identifier. | stable unique ID within dataset | subject_id, participant_id, patient_id | Biological replicate for tissue analyses. |
| participant_id | string | identifiers | De-identified participant identifier. | Stable unique ID | subject_id, patient_id | Required for joins and splits. |
| sample_id | string | identifiers | Biospecimen or assay sample identifier. | Stable unique ID | specimen_id | Optional when one participant has multiple samples. |
| collection_date | date | timing | Date of sample or clinical measure collection. | ISO 8601 | visit_date, draw_date | Use only when permitted by governance. |
| age | numeric | demographics | Chronological age at measurement. | years | age_years | Prefer age at sample collection. |
| age_group | category | demographics | Analysis age group. | young, middle, older, reproductively_aged | age_bin, group | Define before DE and do not tune after seeing results. |
| bmi | numeric | anthropometrics | Body mass index. | kg/m^2 | body_mass_index | Track pregnancy status where relevant. |
| procurement_type | category | design | Tissue procurement context. | autopsy, BSO, donor, other, unknown | collection_type | Audit for confounding with age. |
| diagnosis_or_cause_of_death | string | design | Diagnosis, indication, or cause of death when relevant. | controlled text where possible | diagnosis, cause_of_death | Audit for confounding and exclusions. |
| pmi | numeric | design | Postmortem interval. | hours | PMI, postmortem_interval | Relevant for autopsy samples. |
| cycle_day | numeric | timing | Menstrual cycle day at collection. | day number | menstrual_day | Define day 1 consistently. |
| cycle_phase | category | timing | Menstrual cycle phase at collection. | follicular, luteal, unknown | phase | Timing-sensitive for ovarian hormones and tissue state. |
| menopause_status | category | reproductive | Reproductive or menopause transition status. | premenopause, perimenopause, postmenopause, unknown | stage | Align to STRAW+10 where possible. |
| modality | category | assay | Data modality for a sample or donor. | scRNA-seq, snRNA-seq, snATAC-seq, spatial_transcriptomics | assay, technology | Needed for modality-specific workflows. |
| cell_id | string | single_cell | Cell or nucleus barcode. | stable ID | barcode | Technical observation, not biological replicate. |
| cell_type_level1 | category | single_cell | Broad cell-type annotation used for QC and coverage. | granulosa, stromal_theca, immune, endothelial, vascular_smooth_muscle, other | broad_cell_type | Use for coverage audits only. |
| cell_type | category | single_cell | Analysis cell type or subtype. | controlled vocabulary | annotation, celltype | Use only when harmonizable across datasets. |
| n_cells | integer | coverage | Number of cells or nuclei for donor by cell type. | count | cell_count | Primary coverage metric. |
| library_size | numeric | coverage | Pseudobulk library size or summed total counts. | counts | total_counts_sum | Review alongside n_cells. |
| median_genes_per_cell | numeric | coverage | Median detected genes per cell within donor by cell type. | genes | median_n_genes | Complexity metric. |
| amh | numeric | biomarker | Anti-Mullerian hormone. | ng/mL or pmol/L | AMH | Record assay and conversion. |
| fsh | numeric | biomarker | Follicle-stimulating hormone. | IU/L | FSH | Timing-sensitive. |
| lh | numeric | biomarker | Luteinizing hormone. | IU/L | LH | Timing-sensitive. |
| estradiol | numeric | biomarker | Estradiol concentration. | pg/mL or pmol/L | E2 | Record assay lower limit. |
| progesterone | numeric | biomarker | Progesterone concentration. | ng/mL or nmol/L | P4 | Timing-sensitive. |
| contraceptive_use | category | exposure | Hormonal contraceptive exposure at measurement. | none, current, recent, unknown | birth_control | Capture formulation if available. |
| hormone_therapy_use | category | exposure | Menopausal hormone therapy exposure. | none, current, recent, unknown | hrt_use | Include route and dose if available. |
| smoking_status | category | exposure | Smoking status. | never, former, current, unknown | tobacco_use | Consider pack-years if available. |
| assay_platform | string | technical | Measurement platform or kit. | free text / controlled vocabulary | platform | Needed for batch adjustment. |
| batch_id | string | technical | Laboratory batch identifier. | stable ID | plate_id, run_id | Optional but recommended. |
