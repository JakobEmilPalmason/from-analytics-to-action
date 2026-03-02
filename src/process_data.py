"""Load and clean IMDb datasets for analysis.

Usage:
    python -m src.process_data
"""

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_title_basics() -> pd.DataFrame:
    """Load title.basics dataset, replacing IMDb '\\N' with NaN."""
    path = os.path.join(DATA_DIR, "title.basics.tsv.gz")
    return pd.read_csv(path, sep="\t", na_values="\\N", low_memory=False)


def load_title_ratings() -> pd.DataFrame:
    """Load title.ratings dataset."""
    path = os.path.join(DATA_DIR, "title.ratings.tsv.gz")
    return pd.read_csv(path, sep="\t", na_values="\\N")


def load_title_akas() -> pd.DataFrame:
    """Load title.akas (alternative titles / regional info)."""
    path = os.path.join(DATA_DIR, "title.akas.tsv.gz")
    return pd.read_csv(path, sep="\t", na_values="\\N", low_memory=False)


def main() -> None:
    print("Loading datasets...")
    basics = load_title_basics()
    ratings = load_title_ratings()
    print(f"Titles: {len(basics):,}  |  Ratings: {len(ratings):,}")


if __name__ == "__main__":
    main()
