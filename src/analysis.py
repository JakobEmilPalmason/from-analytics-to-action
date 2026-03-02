"""Analysis utilities for the case project.

Add functions here for audience segmentation, comparable-title analysis,
market/country breakdowns, etc.

Usage:
    python -m src.analysis
"""

import pandas as pd


def find_comparable_titles(
    df: pd.DataFrame,
    genres: list[str],
    min_votes: int = 1000,
    top_n: int = 20,
) -> pd.DataFrame:
    """Find top-rated titles matching any of the given genres."""
    mask = df["genres"].str.contains("|".join(genres), na=False)
    mask &= df["numVotes"] >= min_votes
    return df.loc[mask].nlargest(top_n, "averageRating")


def main() -> None:
    print("Run analysis functions from notebooks or import from src.analysis")


if __name__ == "__main__":
    main()
