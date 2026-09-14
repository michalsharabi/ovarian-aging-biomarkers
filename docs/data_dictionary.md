# Data Dictionary

Use this document to track harmonized variables across datasets. Add dataset-specific aliases as new sources are registered.

| Field | Type | Domain | Description | Units / Coding | Source Aliases | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| participant_id | string | identifiers | De-identified participant identifier. | Stable unique ID | subject_id, patient_id | Required for joins and splits. |
| sample_id | string | identifiers | Biospecimen or assay sample identifier. | Stable unique ID | specimen_id | Optional when one participant has multiple samples. |
| collection_date | date | timing | Date of sample or clinical measure collection. | ISO 8601 | visit_date, draw_date | Use only when permitted by governance. |
| age | numeric | demographics | Chronological age at measurement. | years | age_years | Prefer age at sample collection. |
| bmi | numeric | anthropometrics | Body mass index. | kg/m^2 | body_mass_index | Track pregnancy status where relevant. |
| cycle_day | numeric | timing | Menstrual cycle day at collection. | day number | menstrual_day | Define day 1 consistently. |
| menopause_status | category | reproductive | Reproductive or menopause transition status. | premenopause, perimenopause, postmenopause, unknown | stage | Align to STRAW+10 where possible. |
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
