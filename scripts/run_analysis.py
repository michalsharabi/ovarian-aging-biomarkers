"""Command-line entry point for project analysis workflows."""

from pathlib import Path

import typer

from ovarian_aging_biomarkers.config import load_dataset_registry

app = typer.Typer(help="Run ovarian aging biomarker analysis workflows.")


@app.command()
def registry(path: Path = Path("config/datasets.yaml")) -> None:
    """Print the dataset IDs currently registered for analysis."""
    registry_data = load_dataset_registry(path)
    datasets = registry_data.get("datasets", [])
    if not datasets:
        typer.echo("No datasets registered.")
        raise typer.Exit()

    for dataset in datasets:
        typer.echo(dataset.get("id", "<missing id>"))


if __name__ == "__main__":
    app()
