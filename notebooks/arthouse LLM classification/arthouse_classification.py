"""
Arthouse Film Classifier — Anthropic Message Batches API Workflow
=================================================================
Classifies films on an "arthouse-ness" scale of 1-10 using Claude via
the Batch API (50% cost reduction, results within 24h).

Requirements:
    pip install anthropic pandas

Pre-processing:
    If your CSV has IMDb name IDs (nm0000001), run decode_imdb_names.py first.

Usage (three steps):

    1. SUBMIT — send all batches and exit:
       python arthouse_batch_classifier.py submit --input films.csv

    2. CHECK — see if batches are done yet:
       python arthouse_batch_classifier.py check

    3. RETRIEVE — pull results and produce the scored CSV:
       python arthouse_batch_classifier.py retrieve --input films.csv --output films_scored.csv

EXPECTED INPUT FORMAT (CSV):
    - titleId      : unique film identifier (IMDb title ID)
    - originalTitle: film title
    - releaseYear  : release year
    - numberOfVotes: number of votes on IMDb
    - allCountries : production countries
    - allLanguages : spoken language(s)
    - directors    : director name(s)
    - writers      : writer name(s)
    - genres       : genre(s), comma-separated
    - plotShort    : plot summary / description
"""

import anthropic
import pandas as pd
import json
import argparse
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------
BATCH_DIR = "batch_runs"
BATCH_IDS_FILE = Path(BATCH_DIR) / "batch_ids.json"
RAW_RESULTS_FILE = Path(BATCH_DIR) / "raw_results.json"
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 150
MAX_REQUESTS_PER_BATCH = 10_000

# ---------------------------------------------------------------------------
# SYSTEM PROMPT
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a film classification assistant. Your task is to rate how "arthouse" a film is on a scale of 1 to 10, based on this definition:

Arthouse cinema refers to films that prioritize artistic expression, formal experimentation, or thematic depth over commercial appeal. They tend to feature non-linear or ambiguous narratives, a strong directorial voice, and subjects rooted in psychological, philosophical, or social themes rather than genre formulas. They are typically independently produced, circulated through festival circuits, and aimed at an engaged audience seeking provocation or reflection rather than conventional entertainment.

Scoring guide:
- 1-2: Purely mainstream/commercial (blockbusters, franchise films, broad comedies)
- 3-4: Mainstream with some artistic ambition (prestige studio films, Oscar-bait)
- 5-6: Crossover films (indie spirit with mainstream accessibility, e.g. Moonlight, Parasite)
- 7-8: Clearly arthouse (festival circuit regulars, strong auteur vision)
- 9-10: Deeply experimental or avant-garde (minimal commercial concessions)

Respond ONLY with valid JSON in this exact format, no other text:
{"score": <integer 1-10>, "reasoning": "<5-8 word justification>"}"""


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def get_client() -> anthropic.Anthropic:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: Set ANTHROPIC_API_KEY environment variable first.")
        print("  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)
    return anthropic.Anthropic()


def load_batch_ids() -> list[str]:
    if not BATCH_IDS_FILE.exists():
        print(f"ERROR: No batch IDs found at {BATCH_IDS_FILE}")
        print("  Run the 'submit' step first.")
        sys.exit(1)
    with open(BATCH_IDS_FILE) as f:
        return json.load(f)


def build_user_message(film: dict) -> str:
    parts = [f"Title: {film.get('originalTitle', 'Unknown')}"]
    if film.get("releaseYear"):
        parts.append(f"Year: {film['releaseYear']}")
    if film.get("directors"):
        parts.append(f"Director: {film['directors']}")
    if film.get("writers"):
        parts.append(f"Writers: {film['writers']}")
    if film.get("genres"):
        parts.append(f"Genre: {film['genres']}")
    if film.get("allCountries"):
        parts.append(f"Countries: {film['allCountries']}")
    if film.get("allLanguages"):
        parts.append(f"Languages: {film['allLanguages']}")
    if film.get("numberOfVotes"):
        parts.append(f"IMDb votes: {film['numberOfVotes']}")
    if film.get("plotShort"):
        parts.append(f"Synopsis: {film['plotShort']}")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# STEP 1: SUBMIT
# ---------------------------------------------------------------------------

def cmd_submit(args):
    """Load films, build batch requests, submit them, save batch IDs, and exit."""
    client = get_client()
    os.makedirs(BATCH_DIR, exist_ok=True)

    print(f"Loading films from {args.input}...")
    df = pd.read_csv(args.input)
    print(f"Loaded {len(df)} films")

    if args.limit:
        df = df.head(args.limit)
        print(f"  Limited to first {args.limit} films (test mode)")

    # Build all request objects
    all_requests = []
    for _, row in df.iterrows():
        film = row.to_dict()
        all_requests.append({
            "custom_id": str(film["titleId"]),
            "params": {
                "model": MODEL,
                "max_tokens": MAX_TOKENS,
                "system": SYSTEM_PROMPT,
                "messages": [
                    {"role": "user", "content": build_user_message(film)}
                ],
            },
        })

    # Chunk into batches of 10,000
    chunks = [
        all_requests[i : i + MAX_REQUESTS_PER_BATCH]
        for i in range(0, len(all_requests), MAX_REQUESTS_PER_BATCH)
    ]
    print(f"Split into {len(chunks)} batch(es)")

    # Submit each chunk
    batch_ids = []
    for i, chunk in enumerate(chunks):
        print(f"  Submitting batch {i + 1}/{len(chunks)} ({len(chunk)} requests)...")
        batch = client.messages.batches.create(requests=chunk)
        batch_ids.append(batch.id)
        print(f"    -> {batch.id}")

    # Save batch IDs
    with open(BATCH_IDS_FILE, "w") as f:
        json.dump(batch_ids, f, indent=2)

    print(f"\nAll batches submitted. IDs saved to {BATCH_IDS_FILE}")
    print("Run 'check' to monitor progress, 'retrieve' when done.")


# ---------------------------------------------------------------------------
# STEP 2: CHECK
# ---------------------------------------------------------------------------

def cmd_check(args):
    """Check the status of all submitted batches."""
    client = get_client()
    batch_ids = load_batch_ids()

    all_done = True
    for batch_id in batch_ids:
        batch = client.messages.batches.retrieve(batch_id)
        counts = batch.request_counts
        status = batch.processing_status

        if status != "ended":
            all_done = False

        print(
            f"  {batch_id}  status={status:<12}  "
            f"succeeded={counts.succeeded}  errored={counts.errored}  "
            f"expired={counts.expired}  processing={counts.processing}"
        )

    if all_done:
        print("\nAll batches complete! Run 'retrieve' to pull results.")
    else:
        print("\nStill processing. Check again later.")


# ---------------------------------------------------------------------------
# STEP 3: RETRIEVE
# ---------------------------------------------------------------------------

def cmd_retrieve(args):
    """Download results from all batches, merge with original CSV, and save."""
    client = get_client()
    batch_ids = load_batch_ids()

    # Verify all batches are done
    for batch_id in batch_ids:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status != "ended":
            print(f"ERROR: Batch {batch_id} is still '{batch.processing_status}'.")
            print("  Run 'check' first to confirm all batches are complete.")
            sys.exit(1)

    # Stream and parse results
    print("Downloading results...")
    all_results = {}
    for batch_id in batch_ids:
        count = 0
        for result in client.messages.batches.results(batch_id):
            custom_id = result.custom_id

            if result.result.type == "succeeded":
                text = result.result.message.content[0].text
                try:
                    parsed = json.loads(text)
                except json.JSONDecodeError:
                    parsed = {"score": None, "reasoning": f"JSON parse error: {text[:100]}"}
            elif result.result.type == "errored":
                parsed = {"score": None, "reasoning": f"API error: {result.result.error}"}
            elif result.result.type == "expired":
                parsed = {"score": None, "reasoning": "Request expired"}
            elif result.result.type == "canceled":
                parsed = {"score": None, "reasoning": "Request canceled"}
            else:
                parsed = {"score": None, "reasoning": f"Unknown status: {result.result.type}"}

            all_results[custom_id] = parsed
            count += 1

        print(f"  {batch_id}: {count} results")

    # Save raw results
    with open(RAW_RESULTS_FILE, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"Raw results saved to {RAW_RESULTS_FILE}")

    # Merge with original CSV
    print(f"Merging with {args.input}...")
    df = pd.read_csv(args.input)
    df["id_str"] = df["titleId"].astype(str)
    df["arthouse_score"] = df["id_str"].map(lambda x: all_results.get(x, {}).get("score"))
    df["arthouse_reasoning"] = df["id_str"].map(lambda x: all_results.get(x, {}).get("reasoning"))
    df.drop(columns=["id_str"], inplace=True)

    df.to_csv(args.output, index=False)
    print(f"Scored CSV saved to {args.output}")

    # Summary
    scored = df["arthouse_score"].notna().sum()
    failed = len(df) - scored
    print(f"\nSummary:")
    print(f"  Total films:  {len(df)}")
    print(f"  Scored:       {scored}")
    print(f"  Failed:       {failed}")
    if scored > 0:
        print(f"  Mean score:   {df['arthouse_score'].mean():.2f}")
        print(f"\n  Score distribution:")
        print(df["arthouse_score"].value_counts().sort_index().to_string(header=False))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Classify films as arthouse using Anthropic Batch API"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # submit
    p_submit = subparsers.add_parser("submit", help="Submit batch requests")
    p_submit.add_argument("--input", default="films.csv", help="Input CSV path")
    p_submit.add_argument("--limit", type=int, default=None, help="Only submit first N films (for testing)")
    p_submit.set_defaults(func=cmd_submit)

    # check
    p_check = subparsers.add_parser("check", help="Check batch status")
    p_check.set_defaults(func=cmd_check)

    # retrieve
    p_retrieve = subparsers.add_parser("retrieve", help="Retrieve results and produce scored CSV")
    p_retrieve.add_argument("--input", default="films.csv", help="Original input CSV (for merging)")
    p_retrieve.add_argument("--output", default="films_arthouse_scored.csv", help="Output CSV path")
    p_retrieve.set_defaults(func=cmd_retrieve)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
    
# python arthouse_classification.py submit --input films_decoded.csv --limit 50
