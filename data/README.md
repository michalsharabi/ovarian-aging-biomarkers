# Data

This folder is for local data organization only. Do not commit raw human-subject data, private clinical metadata, credentials, or large derived matrices.

Suggested local layout:

```text
data/raw/        Original files from controlled sources
data/interim/    Cleaned modality-specific intermediates
data/processed/  Analysis-ready feature matrices and labels
```

Only README files and `.gitkeep` placeholders should be committed here.
