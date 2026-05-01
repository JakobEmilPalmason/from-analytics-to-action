"""
IMDb Name Decoder
=================
Resolves IMDb name IDs (nm0000001 format) in a CSV to real names
using IMDb's freely available name.basics.tsv.gz dataset.

Requirements:
    pip install pandas

Setup:
    1. Download name.basics.tsv.gz from https://datasets.imdbws.com/
    2. Edit the CONFIGURATION section below with your file paths
    3. Run:  python decode_imdb_names.py
"""

import pandas as pd
import re
import sys

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these to match your setup
# ---------------------------------------------------------------------------
INPUT_CSV = "films_enriched.csv"                # Your films CSV with nm IDs
OUTPUT_CSV = "films_decoded.csv"       # Output CSV with real names
NAMES_FILE = "name.basics.tsv.gz"     # IMDb names file from https://datasets.imdbws.com/
COLUMNS = None                         # Columns to decode, e.g. ["director", "writers"]
                                       # Set to None to auto-detect

# ---------------------------------------------------------------------------

NM_PATTERN = re.compile(r"nm\d{7,}")


def build_lookup(names_path: str) -> dict[str, str]:
    """Load IMDb name.basics.tsv.gz and return a dict of nconst -> primaryName."""
    print(f"Loading IMDb names from {names_path}...")
    names_df = pd.read_csv(
        names_path,
        sep="\t",
        usecols=["nconst", "primaryName"],
        dtype=str,
        na_values=["\\N"],
    )
    lookup = dict(zip(names_df["nconst"], names_df["primaryName"]))
    print(f"  Loaded {len(lookup):,} names")
    return lookup


def detect_nm_columns(df: pd.DataFrame) -> list[str]:
    """Auto-detect columns that contain IMDb name IDs."""
    columns = []
    for col in df.columns:
        sample = df[col].dropna().head(100).astype(str)
        if sample.str.contains(NM_PATTERN).any():
            columns.append(col)
    return columns


def resolve_names(cell: str, lookup: dict[str, str]) -> str:
    """Replace all nm IDs in a cell with their real names."""
    if pd.isna(cell) or not isinstance(cell, str):
        return cell
    ids = NM_PATTERN.findall(cell)
    if not ids:
        return cell
    resolved = [lookup.get(nm_id, nm_id) for nm_id in ids]
    return ", ".join(resolved)


def main():
    # Build lookup
    lookup = build_lookup(NAMES_FILE)

    # Load films
    print(f"Loading films from {INPUT_CSV}...")
    df = pd.read_csv(INPUT_CSV, dtype=str)
    print(f"  Loaded {len(df):,} films")

    # Determine which columns to decode
    if COLUMNS:
        columns_to_decode = COLUMNS
    else:
        columns_to_decode = detect_nm_columns(df)

    if not columns_to_decode:
        print("  No columns with IMDb name IDs detected. Nothing to decode.")
        sys.exit(0)

    print(f"  Decoding columns: {columns_to_decode}")

    # Decode
    total_unresolved = 0
    for col in columns_to_decode:
        before = df[col].copy()
        df[col] = df[col].apply(lambda cell: resolve_names(cell, lookup))

        changed = (before != df[col]).sum()
        print(f"    {col}: {changed:,} cells updated")

        # Count any remaining unresolved IDs
        for val in df[col].dropna():
            remaining = NM_PATTERN.findall(str(val))
            total_unresolved += len(remaining)

    if total_unresolved > 0:
        print(f"\n  Warning: {total_unresolved} IDs could not be resolved (not in name.basics.tsv.gz)")

    # Save
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\nDecoded CSV saved to {OUTPUT_CSV}")


if __name__ == "__main__":
    main()