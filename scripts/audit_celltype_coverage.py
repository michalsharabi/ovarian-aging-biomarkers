"""Create Sprint 0 donor by cell-type coverage table and heatmap."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import typer

from ovarian_aging_biomarkers.audit import write_celltype_coverage

app = typer.Typer(help="Audit donor by cell-type coverage before pseudobulk DE.")


@app.command()
def main(
    input_path: Path = typer.Argument(..., help="Cell or nucleus metadata CSV/TSV/parquet file."),
    output_path: Path = Path("results/tables/donor_celltype_coverage.tsv"),
    figure_path: Path = Path("results/figures/donor_celltype_coverage_heatmap.png"),
) -> None:
    """Write coverage table and a donor by cell-type heatmap."""
    coverage = write_celltype_coverage(input_path, output_path)
    figure_path.parent.mkdir(parents=True, exist_ok=True)

    matrix = coverage.pivot_table(
        index=["dataset_id", "donor_id"],
        columns="cell_type",
        values="n_cells",
        fill_value=0,
        aggfunc="sum",
    )

    height = max(4, min(14, 0.35 * len(matrix) + 2))
    width = max(6, min(18, 0.45 * len(matrix.columns) + 4))
    fig, ax = plt.subplots(figsize=(width, height))
    sns.heatmap(matrix, cmap="viridis", linewidths=0.25, linecolor="white", ax=ax)
    ax.set_xlabel("Cell type")
    ax.set_ylabel("Dataset / donor")
    ax.set_title("Donor by cell-type coverage")
    fig.tight_layout()
    fig.savefig(figure_path, dpi=200)
    plt.close(fig)

    typer.echo(f"Wrote {len(coverage)} coverage rows to {output_path}.")
    typer.echo(f"Wrote coverage heatmap to {figure_path}.")


if __name__ == "__main__":
    app()
