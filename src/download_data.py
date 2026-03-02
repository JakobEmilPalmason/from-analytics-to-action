"""Download IMDb non-commercial datasets.

IMDb provides gzipped TSV files at:
https://datasets.imdbws.com/

Available datasets:
- title.basics.tsv.gz
- title.ratings.tsv.gz
- title.crew.tsv.gz
- title.episode.tsv.gz
- title.principals.tsv.gz
- title.akas.tsv.gz
- name.basics.tsv.gz

Usage:
    python -m src.download_data
"""

import os
import requests

BASE_URL = "https://datasets.imdbws.com"
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

DATASETS = [
    "title.basics.tsv.gz",
    "title.ratings.tsv.gz",
    "title.akas.tsv.gz",
]


def download_file(filename: str) -> None:
    url = f"{BASE_URL}/{filename}"
    dest = os.path.join(DATA_DIR, filename)

    if os.path.exists(dest):
        print(f"Already exists: {dest}")
        return

    print(f"Downloading {url} ...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Saved to {dest}")


def main() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    for dataset in DATASETS:
        download_file(dataset)


if __name__ == "__main__":
    main()
