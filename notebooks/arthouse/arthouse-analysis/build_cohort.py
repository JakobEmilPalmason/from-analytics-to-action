"""Build the arthouse working cohort.

Cohort definition (see ``notebooks/arthouse/deciding-method.md``):
a film is arthouse if **either**

* the rule-based ``is_arthouse()`` in ``src/arthouse.py`` flags it, **or**
* Claude Haiku scored it ``arthouse_score >= 8``.

Run from the project root:

    python notebooks/arthouse/arthouse-analysis/build_cohort.py

Reads ``notebooks/arthouse/arthouse-LLM-classification/films_arthouse_scored.csv``
(every original ``films_enriched`` column plus the LLM score and reasoning)
and writes ``notebooks/arthouse/arthouse-analysis/arthouse_cohort.csv``.

Two extra columns are added on the way out:

* ``is_arthouse_rule`` -- boolean output of the rule-based classifier.
* ``arthouse_source`` -- one of ``rule_only``, ``llm_only``, ``both``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from arthouse import is_arthouse  # noqa: E402

SCORED_CSV = (
    PROJECT_ROOT
    / "notebooks/arthouse/arthouse-LLM-classification/films_arthouse_scored.csv"
)
OUTPUT_CSV = PROJECT_ROOT / "notebooks/arthouse/arthouse-analysis/arthouse_cohort.csv"

LLM_THRESHOLD = 8


def build_cohort() -> pd.DataFrame:
    df = pd.read_csv(SCORED_CSV)

    rule_flag = is_arthouse(df)
    llm_flag = df["arthouse_score"].fillna(0).ge(LLM_THRESHOLD)
    in_cohort = rule_flag | llm_flag

    source = pd.Series("none", index=df.index, dtype="object")
    source[rule_flag & ~llm_flag] = "rule_only"
    source[llm_flag & ~rule_flag] = "llm_only"
    source[rule_flag & llm_flag] = "both"

    cohort = df.loc[in_cohort].copy()
    cohort["is_arthouse_rule"] = rule_flag.loc[in_cohort].astype(bool)
    cohort["arthouse_source"] = source.loc[in_cohort]
    return cohort


def main() -> None:
    cohort = build_cohort()
    cohort.to_csv(OUTPUT_CSV, index=False)

    counts = cohort["arthouse_source"].value_counts()
    print(f"Total scored films:    {len(pd.read_csv(SCORED_CSV)):,}")
    print(f"Arthouse cohort:       {len(cohort):,}")
    print(f"  rule only:           {int(counts.get('rule_only', 0)):,}")
    print(f"  LLM only (score>=8): {int(counts.get('llm_only', 0)):,}")
    print(f"  both:                {int(counts.get('both', 0)):,}")
    print(f"Wrote {OUTPUT_CSV.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
