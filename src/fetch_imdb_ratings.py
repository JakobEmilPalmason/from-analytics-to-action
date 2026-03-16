"""Fetch per-star rating distributions from IMDb's GraphQL API.

Usage:
    python -m src.fetch_imdb_ratings

Outputs: 03-data/imdb_rating_distributions.csv

Each row has: titleId, rating_1, rating_2, ..., rating_10 (vote counts per star)
"""

import os
import sys
import time

import pandas as pd
import requests

BASE_URL = "https://caching.graphql.imdb.com/"
INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "03-data", "European_data_2000.xlsx")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "03-data", "imdb_rating_distributions.csv")

HEADERS = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
}

QUERY = """
query RatingsDist($id: ID!) {
  title(id: $id) {
    ratingsSummary {
      aggregateRating
      voteCount
    }
    aggregateRatingsBreakdown {
      histogram {
        histogramValues {
          rating
          voteCount
        }
      }
    }
  }
}
"""

REQUEST_DELAY = 0.1  # 100ms between requests to be respectful


def fetch_ratings(imdb_id: str, session: requests.Session) -> dict | None:
    """Fetch rating histogram for a single title."""
    payload = {"query": QUERY, "variables": {"id": imdb_id}}
    try:
        resp = session.post(BASE_URL, json=payload, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json().get("data", {}).get("title")
        if not data:
            return None

        result = {"titleId": imdb_id}

        summary = data.get("ratingsSummary") or {}
        result["aggregateRating"] = summary.get("aggregateRating")
        result["totalVotes"] = summary.get("voteCount")

        breakdown = data.get("aggregateRatingsBreakdown") or {}
        histogram = (breakdown.get("histogram") or {}).get("histogramValues") or []
        for entry in histogram:
            result[f"rating_{entry['rating']}"] = entry["voteCount"]

        return result
    except requests.RequestException:
        return None


def main() -> None:
    df = pd.read_excel(INPUT_PATH)
    print(f"Loaded {len(df)} films from dataset")

    # Resume support
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

        result = fetch_ratings(imdb_id, session)
        time.sleep(REQUEST_DELAY)

        if result is None:
            results.append({"titleId": imdb_id})
            print(f"  [{i+1}/{total}] {imdb_id} — failed")
            continue

        results.append(result)
        r10 = result.get("rating_10", 0)
        r1 = result.get("rating_1", 0)
        total_v = result.get("totalVotes", 0)
        print(f"  [{i+1}/{total}] {imdb_id} — {total_v:,} votes (10s: {r10:,}, 1s: {r1:,})")

        # Save every 100 films
        if len(results) % 100 == 0:
            _save(results, already_done)

    _save(results, already_done)
    _print_report()


def _save(new_results: list[dict], already_done: set) -> None:
    new_df = pd.DataFrame(new_results)
    if os.path.exists(OUTPUT_PATH) and already_done:
        existing = pd.read_csv(OUTPUT_PATH)
        combined = pd.concat([existing, new_df], ignore_index=True)
    else:
        combined = new_df
    # Ensure consistent column order
    cols = ["titleId", "aggregateRating", "totalVotes"] + [f"rating_{i}" for i in range(1, 11)]
    for c in cols:
        if c not in combined.columns:
            combined[c] = None
    combined = combined[cols]
    combined.to_csv(OUTPUT_PATH, index=False)


def _print_report() -> None:
    df = pd.read_csv(OUTPUT_PATH)
    total = len(df)
    has_data = df["totalVotes"].notna().sum()
    print("\n" + "=" * 50)
    print("IMDb RATING DISTRIBUTION REPORT")
    print("=" * 50)
    print(f"Total films:          {total}")
    print(f"Has rating data:      {has_data} ({has_data/total:.1%})")

    # Show most polarizing films (high % of 1s and 10s)
    df["pct_extreme"] = (df["rating_1"].fillna(0) + df["rating_10"].fillna(0)) / df["totalVotes"].fillna(1)
    top = df.nlargest(5, "pct_extreme")
    print("\nMost polarizing films (highest % of 1s + 10s):")
    for _, r in top.iterrows():
        print(f"  {r['titleId']}: {r['pct_extreme']:.1%} extreme votes ({int(r.get('totalVotes', 0)):,} total)")
    print("=" * 50)


if __name__ == "__main__":
    main()
