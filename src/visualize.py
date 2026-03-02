"""Visualization helpers for reports and presentations.

Usage:
    python -m src.visualize
"""

import matplotlib.pyplot as plt
import seaborn as sns

REPORTS_DIR = "reports/figures"


def set_style() -> None:
    """Apply a clean default style for all plots."""
    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams.update({"figure.figsize": (10, 6), "figure.dpi": 150})


def save_figure(fig: plt.Figure, name: str) -> None:
    """Save a figure to the reports/figures directory."""
    path = f"{REPORTS_DIR}/{name}.png"
    fig.savefig(path, bbox_inches="tight")
    print(f"Saved {path}")


def main() -> None:
    print("Import visualization helpers: from src.visualize import set_style, save_figure")


if __name__ == "__main__":
    main()
