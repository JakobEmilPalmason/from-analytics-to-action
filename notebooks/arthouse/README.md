# Arthouse

We tried two methods to define what counts as an "arthouse" film. 

## The two methods

| Folder | Method |
|---|---|
| `arthouse-method-classification/` | Rule-based: an operational `is_arthouse()` definition built from auditable signals (rating, festival cues, keywords, budget, language). |
| `arthouse-LLM-classification/` | Claude Haiku 4.5 scores each film 1–10 on "arthouse-ness" using the full metadata + plot summary. |

## Decision

The LLM classification wins. Its output — `arthouse-LLM-classification/films_arthouse_scored.csv` — is **the working dataset** for the rest of the project.

## Next steps

1. Decide what we want to **say** about arthouse cinema (the question / angle).
2. Decide how to **use the dataset** to support that (which signals, which cuts, which visualizations).
