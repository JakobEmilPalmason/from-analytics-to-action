# Arthouse Definition TLDR

## Recommendation

Use the `working_ensemble` definition from `src/arthouse.py`:

```python
from src.arthouse import is_arthouse

arthouse_mask = is_arthouse(df)
```

## Definition To Use

A film counts as arthouse if it matches **any** of these paths:

1. **Refined provocation core:** IMDb rating `>= 7.0`, IMDb votes `<= 33`, keywords present, and either explicit arthouse evidence or non-English/non-US context.
2. **Strict canon:** specialty arthouse label/distributor **and** festival signal.
3. **Composite evidence:** arthouse score `>= 6`, IMDb rating `>= 7.0`, IMDb votes between `20` and `1,000`, and at least one auditable evidence signal.

Auditable evidence means at least one of:

- specialty label/distributor
- festival signal
- arthouse/provocation keyword
- positive low budget up to USD 5M

In short:

```python
is_arthouse = refined_provocation_core | strict_canon | composite
```

Where:

```python
refined_provocation_core = (
    high_rating
    & niche_reach_pdf
    & has_keywords
    & (evidence_signal | non_english_non_us)
)

strict_canon = specialty_label & festival_signal

composite = (
    arthouse_score >= 6
    & high_rating
    & niche_reach_broad
    & evidence_signal
)
```

And the score is:

```text
+3 specialty label
+2 festival signal
+2 arthouse keyword
+1 non-English/non-US
+1 IMDb rating >= 7.0
+1 IMDb votes between 20 and 1,000
+1 positive budget up to USD 5M
+1 writer/director overlap
+1 low TMDb popularity
-2 mainstream-risk keyword
```

## Why This One

- It keeps the original deck idea: arthouse is **high-rated but niche-reach**, not simply "foreign" or "independent".
- It improves the old PDF baseline by filtering out pure "tiny-vote high-rating" noise.
- It still catches clear arthouse/festival titles that are too visible to satisfy the low-vote rule.
- It uses multiple weak signals together because no single dataset column captures arthouse cinema reliably.

## Key Notebook Findings

- Original PDF baseline: `1,673` films, `3.35%` of dataset.
- Recommended working ensemble: `1,704` films, `3.41%` of dataset.
- Working ensemble profile:
  - mean IMDb rating: `7.57`
  - median IMDb votes: `20`
  - median release year: `2011`
  - high rating: `95.2%`
  - non-English/non-US: `88.7%`
  - old low-vote niche reach: `69.2%`
  - keyword signal: `26.2%`
  - specialty label: `18.0%`
  - festival signal: `13.1%`

## Do Not Use As Default

- **PDF baseline alone:** useful starting point, but too dependent on tiny IMDb vote counts.
- **Strict canon alone:** precise, but far too small at `173` films.
- **Language/country alone:** too broad; it over-includes ordinary non-US/non-English mainstream films.
- **Keyword alone:** too narrow and keyword-dependent.

## Caveat

This is a practical project definition, not a universal film-theory definition. Recalibrate if you later get hand-labeled arthouse examples from Publikum or domain experts.
