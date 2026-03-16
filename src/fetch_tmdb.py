"""Fetch budget, revenue, and metadata from TMDb for our European film dataset.

Usage:
    export TMDB_API_KEY="your_key_here"
    python -m src.fetch_tmdb

Get a free API key at: https://www.themoviedb.org/settings/api

Outputs: 03-data/tmdb_enrichment.csv
"""

import os
import sys
import time

import pandas as pd
import requests

API_KEY = os.environ.get("TMDB_API_KEY", "")
BASE_URL = "https://api.themoviedb.org/3"
INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "03-data", "European_data_2000.xlsx")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "03-data", "tmdb_enrichment.csv")

# TMDb rate limit: ~40 req/s — we stay conservative
REQUEST_DELAY = 0.05  # 50ms between requests


def find_tmdb_id(imdb_id: str, session: requests.Session) -> int | None:
    """Look up TMDb movie ID from an IMDb titleId."""
    resp = session.get(
        f"{BASE_URL}/find/{imdb_id}",
        params={"api_key": API_KEY, "external_source": "imdb_id"},
    )
    if resp.status_code != 200:
        return None
    results = resp.json().get("movie_results", [])
    return results[0]["id"] if results else None


def get_movie_details(tmdb_id: int, session: requests.Session) -> dict | None:
    """Fetch movie details from TMDb."""
    resp = session.get(
        f"{BASE_URL}/movie/{tmdb_id}",
        params={"api_key": API_KEY},
    )
    if resp.status_code != 200:
        return None
    data = resp.json()
    return {
        "tmdb_id": tmdb_id,
        "budget": data.get("budget", 0),
        "revenue": data.get("revenue", 0),
        "tmdb_popularity": data.get("popularity"),
        "tmdb_vote_average": data.get("vote_average"),
        "tmdb_vote_count": data.get("vote_count"),
        "original_language": data.get("original_language"),
        "tagline": data.get("tagline"),
        "status": data.get("status"),
        "spoken_languages": ", ".join(
            lang.get("english_name", "") for lang in data.get("spoken_languages", [])
        ),
        "production_countries": ", ".join(
            c.get("iso_3166_1", "") for c in data.get("production_countries", [])
        ),
    }


def main() -> None:
    if not API_KEY:
        print("Error: Set TMDB_API_KEY environment variable.")
        print("Get a free key at: https://www.themoviedb.org/settings/api")
        sys.exit(1)

    df = pd.read_excel(INPUT_PATH)
    print(f"Loaded {len(df)} films from dataset")

    # Resume support: if output file exists, skip already-fetched films
    already_done = set()
    if os.path.exists(OUTPUT_PATH):
        existing = pd.read_csv(OUTPUT_PATH)
        already_done = set(existing["titleId"].tolist())
        print(f"Resuming — {len(already_done)} films already fetched")

    session = requests.Session()
    results = []
    total = len(df)

    for i, row in df.iterrows():
        imdb_id = row["titleId"]
        if imdb_id in already_done:
            continue

        # Step 1: Find TMDb ID
        tmdb_id = find_tmdb_id(imdb_id, session)
        time.sleep(REQUEST_DELAY)

        if tmdb_id is None:
            results.append({"titleId": imdb_id, "tmdb_id": None})
            print(f"  [{i+1}/{total}] {imdb_id} — not found on TMDb")
            continue

        # Step 2: Get details
        details = get_movie_details(tmdb_id, session)
        time.sleep(REQUEST_DELAY)

        if details is None:
            results.append({"titleId": imdb_id, "tmdb_id": tmdb_id})
            print(f"  [{i+1}/{total}] {imdb_id} — found but details failed")
            continue

        details["titleId"] = imdb_id
        results.append(details)

        budget = details.get("budget", 0)
        revenue = details.get("revenue", 0)
        status = "has financials" if (budget > 0 or revenue > 0) else "no financials"
        print(f"  [{i+1}/{total}] {imdb_id} — {status} (budget=${budget:,}, revenue=${revenue:,})")

        # Save progress every 100 films
        if len(results) % 100 == 0:
            _save(results, already_done)

    _save(results, already_done)
    _print_coverage_report()


def _save(new_results: list[dict], already_done: set) -> None:
    """Append new results to output CSV."""
    new_df = pd.DataFrame(new_results)
    if os.path.exists(OUTPUT_PATH) and already_done:
        existing = pd.read_csv(OUTPUT_PATH)
        combined = pd.concat([existing, new_df], ignore_index=True)
    else:
        combined = new_df
    combined.to_csv(OUTPUT_PATH, index=False)


def _print_coverage_report() -> None:
    """Print summary of what we got."""
    df = pd.read_csv(OUTPUT_PATH)
    total = len(df)
    found = df["tmdb_id"].notna().sum()
    has_budget = (df["budget"].fillna(0) > 0).sum()
    has_revenue = (df["revenue"].fillna(0) > 0).sum()
    has_either = ((df["budget"].fillna(0) > 0) | (df["revenue"].fillna(0) > 0)).sum()

    print("\n" + "=" * 50)
    print("TMDb COVERAGE REPORT")
    print("=" * 50)
    print(f"Total films:          {total}")
    print(f"Found on TMDb:        {found} ({found/total:.1%})")
    print(f"Has budget data:      {has_budget} ({has_budget/total:.1%})")
    print(f"Has revenue data:     {has_revenue} ({has_revenue/total:.1%})")
    print(f"Has budget OR revenue: {has_either} ({has_either/total:.1%})")
    print("=" * 50)


if __name__ == "__main__":
    main()
