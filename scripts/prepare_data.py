"""Prepare raw datasets into analysis-ready tables."""

from pathlib import Path

import typer

app = typer.Typer(help="Prepare ovarian aging biomarker datasets.")


@app.command()
def main(
    dataset_id: str = typer.Argument(..., help="Dataset ID from config/datasets.yaml."),
    output_dir: Path = Path("data/processed"),
) -> None:
    """Placeholder for dataset-specific preparation steps."""
    output_dir.mkdir(parents=True, exist_ok=True)
    typer.echo(f"Preparation workflow placeholder for {dataset_id}.")


if __name__ == "__main__":
    app()
