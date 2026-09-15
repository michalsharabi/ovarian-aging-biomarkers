"""Create Sprint 0 donor characteristics table."""

from pathlib import Path

import typer

from ovarian_aging_biomarkers.audit import write_donor_characteristics

app = typer.Typer(help="Audit donor-level metadata before differential expression.")


@app.command()
def main(
    input_path: Path = typer.Argument(..., help="Donor metadata CSV/TSV/parquet file."),
    output_path: Path = Path("results/tables/donor_characteristics.tsv"),
) -> None:
    """Write the frozen donor characteristics table."""
    donors = write_donor_characteristics(input_path, output_path)
    typer.echo(f"Wrote {len(donors)} donor rows to {output_path}.")


if __name__ == "__main__":
    app()
