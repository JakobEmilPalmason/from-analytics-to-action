"""Extract MovieLens 32M data for our European film dataset.

Usage:
    python -m src.fetch_movielens

Expects: 03-data/ml-32m.zip (downloaded from https://grouplens.org/datasets/movielens/32m/)
Outputs: 03-data/movielens_enrichment.csv

For each film in our dataset, extracts:
- Number of MovieLens ratings
- Average MovieLens rating (0.5-5.0 scale)
- Rating distribution (count per star: 0.5, 1.0, ..., 5.0)
- User tags (comma-separated)
"""

import os
import zipfile

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "03-data")
ZIP_PATH = os.path.join(DATA_DIR, "ml-32m.zip")
INPUT_PATH = os.path.join(DATA_DIR, "European_data_2000.xlsx")
OUTPUT_PATH = os.path.join(DATA_DIR, "movielens_enrichment.csv")


def main() -> None:
    if not os.path.exists(ZIP_PATH):
        print(f"Error: Download ml-32m.zip first to {ZIP_PATH}")
        print("https://grouplens.org/datasets/movielens/32m/")
        return

    # Load our film dataset
    our_films = pd.read_excel(INPUT_PATH)
    # Extract numeric IMDb IDs (strip 'tt' prefix and leading zeros)
    our_films["imdbIdNum"] = our_films["titleId"].str.replace("tt", "").astype(int)
    print(f"Our dataset: {len(our_films)} films")

    # Read links.csv from zip to map MovieLens movieId -> imdbId
    print("Reading MovieLens links...")
    with zipfile.ZipFile(ZIP_PATH) as zf:
        links = pd.read_csv(zf.open("ml-32m/links.csv"))

    # Filter to only our films
    our_imdb_ids = set(our_films["imdbIdNum"])
    links_matched = links[links["imdbId"].isin(our_imdb_ids)]
    matched_movie_ids = set(links_matched["movieId"])
    print(f"Found {len(links_matched)} of our films in MovieLens")

    # Read ratings for matched films only
    print("Reading MovieLens ratings (this may take a moment)...")
    with zipfile.ZipFile(ZIP_PATH) as zf:
        chunks = pd.read_csv(zf.open("ml-32m/ratings.csv"), chunksize=1_000_000)
        ratings_list = []
        for i, chunk in enumerate(chunks):
            filtered = chunk[chunk["movieId"].isin(matched_movie_ids)]
            if len(filtered) > 0:
                ratings_list.append(filtered)
            print(f"  Processed {(i+1):,}M ratings...", end="\r")

    print()
    if not ratings_list:
        print("No ratings found for our films.")
        return

    ratings = pd.concat(ratings_list, ignore_index=True)
    print(f"Total ratings for our films: {len(ratings):,}")

    # Compute per-film stats
    stats = ratings.groupby("movieId").agg(
        ml_rating_count=("rating", "count"),
        ml_rating_mean=("rating", "mean"),
        ml_rating_std=("rating", "std"),
        ml_rating_median=("rating", "median"),
    ).reset_index()

    # Rating distribution per film
    dist = ratings.groupby(["movieId", "rating"]).size().unstack(fill_value=0)
    dist.columns = [f"ml_rating_{str(c).replace('.', '_')}" for c in dist.columns]
    dist = dist.reset_index()

    stats = stats.merge(dist, on="movieId", how="left")

    # Read tags for matched films
    print("Reading MovieLens tags...")
    with zipfile.ZipFile(ZIP_PATH) as zf:
        tags = pd.read_csv(zf.open("ml-32m/tags.csv"))

    tags_matched = tags[tags["movieId"].isin(matched_movie_ids)]
    tags_agg = (
        tags_matched.groupby("movieId")["tag"]
        .apply(lambda x: ", ".join(x.dropna().unique()))
        .reset_index()
        .rename(columns={"tag": "ml_tags"})
    )
    print(f"Films with tags: {len(tags_agg)}")

    stats = stats.merge(tags_agg, on="movieId", how="left")

    # Map back to IMDb titleIds
    id_map = links_matched[["movieId", "imdbId"]].copy()
    id_map["titleId"] = "tt" + id_map["imdbId"].astype(str).str.zfill(7)
    stats = stats.merge(id_map[["movieId", "titleId"]], on="movieId", how="left")

    # Reorder columns
    cols = ["titleId"] + [c for c in stats.columns if c not in ("titleId", "movieId")]
    stats = stats[cols]

    stats.to_csv(OUTPUT_PATH, index=False)
    print(f"\nSaved to {OUTPUT_PATH}")

    # Coverage report
    total = len(our_films)
    matched = len(stats)
    has_tags = stats["ml_tags"].notna().sum()

    print("\n" + "=" * 50)
    print("MOVIELENS COVERAGE REPORT")
    print("=" * 50)
    print(f"Our films:            {total}")
    print(f"Found in MovieLens:   {matched} ({matched/total:.1%})")
    print(f"Have tags:            {has_tags} ({has_tags/total:.1%})")
    print(f"Total ratings:        {len(ratings):,}")
    print(f"Avg ratings/film:     {len(ratings)/matched:,.0f}")

    # Most polarizing by std deviation
    top_polar = stats.nlargest(5, "ml_rating_std")
    print("\nMost polarizing films (highest rating std dev):")
    for _, r in top_polar.iterrows():
        print(f"  {r['titleId']}: std={r['ml_rating_std']:.2f}, mean={r['ml_rating_mean']:.2f} ({int(r['ml_rating_count']):,} ratings)")
    print("=" * 50)


if __name__ == "__main__":
    main()
