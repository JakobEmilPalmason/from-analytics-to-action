"""Operational arthouse definition for the 50k film dataset.

The project uses arthouse as a working analytical category, not as a
universal film-theory truth. The default definition combines the existing
project framing from ``notebooks/arthouse/arthouse_provocation_final.pdf``
with auditable signals available in ``03-data/films_enriched.csv``:

* high IMDb rating and niche audience reach;
* specialty/festival distribution evidence;
* foreign-language/non-Hollywood context;
* arthouse, social-political, or auteur-adjacent keywords;
* low positive budgets where TMDb budget data exists.

Import ``is_arthouse`` in downstream notebooks to apply the same definition.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

import pandas as pd


SPECIALTY_LABELS: tuple[str, ...] = (
    "a24",
    "ifc films",
    "ifc productions",
    "janus films",
    "criterion collection",
    "criterion",
    "neon",
    "mubi",
    "strand releasing",
    "kino lorber",
    "oscilloscope",
    "sony pictures classics",
    "film movement",
    "music box films",
    "magnolia pictures",
    "zeitgeist films",
    "artificial eye",
    "curzon",
    "mk2",
    "celluloid dreams",
    "films boutique",
    "the match factory",
    "wild bunch",
    "good machine",
    "new yorker films",
    "milestone films",
    "bfi",
    "british film institute",
    "cinema guild",
    "grasshopper film",
    "factory 25",
    "kimstim",
    "utopia",
    "metrograph",
    "sideshow",
    "picturehouse",
    "roadside attractions",
    "bleecker street",
    "cohen media",
    "arrow films",
    "icarus films",
    "dogwoof",
    "modern films",
    "trigon-film",
)

FESTIVAL_TERMS: tuple[str, ...] = (
    "cannes",
    "sundance",
    "venice",
    "berlinale",
    "berlin international film festival",
    "toronto international film festival",
    "tiff",
    "locarno",
    "rotterdam",
    "tribeca",
    "telluride",
    "san sebastian",
    "london film festival",
    "film festival",
    "palme d'or",
    "palme d’or",
    "golden bear",
    "golden lion",
    "jury prize",
    "festival",
)

ARTHOUSE_KEYWORDS: tuple[str, ...] = (
    "art film",
    "art documentary",
    "avant-garde",
    "avant garde",
    "experimental film",
    "experimental cinema",
    "slow cinema",
    "minimalism",
    "surrealism",
    "existentialism",
    "alienation",
    "loneliness",
    "identity",
    "human rights",
    "refugee",
    "racism",
    "holocaust",
    "genocide",
    "war crime",
    "dictatorship",
    "political repression",
    "blasphemy",
    "homosexuality",
    "lgbt",
    "lgbtq",
    "addiction",
    "suicide",
    "social realism",
    "coming of age",
    "world war ii",
    "communism",
    "poverty",
    "immigration",
)

MAINSTREAM_RISK_KEYWORDS: tuple[str, ...] = (
    "superhero",
    "marvel",
    "dc comics",
    "sequel",
    "franchise",
    "blockbuster",
    "based on comic book",
    "explosion",
    "car chase",
    "alien invasion",
    "disaster movie",
    "zombie",
    "slasher",
    "gore",
    "torture porn",
    "exploitation",
    "b-movie",
    "erotica",
)


def _text_column(df: pd.DataFrame, column: str) -> pd.Series:
    """Return a string Series aligned to ``df`` even when ``column`` is absent."""
    if column not in df:
        return pd.Series("", index=df.index, dtype="object")
    return df[column].fillna("").astype(str)


def _numeric_column(df: pd.DataFrame, column: str) -> pd.Series:
    """Return a numeric Series aligned to ``df`` even when ``column`` is absent."""
    if column not in df:
        return pd.Series(float("nan"), index=df.index)
    return pd.to_numeric(df[column], errors="coerce")


def contains_any_term(series: pd.Series, terms: Iterable[str]) -> pd.Series:
    """Case-insensitive term matching with alphanumeric boundaries.

    Boundaries keep short labels auditable: for example, ``bfi`` matches
    ``BFI`` but not a random longer word containing those letters.
    """
    text = series.fillna("").astype(str).str.lower()
    mask = pd.Series(False, index=series.index)
    for term in terms:
        pattern = rf"(?<![a-z0-9]){re.escape(term.lower())}(?![a-z0-9])"
        mask |= text.str.contains(pattern, regex=True, na=False)
    return mask


def _ids_overlap(left: object, right: object) -> bool:
    if not isinstance(left, str) or not isinstance(right, str):
        return False
    left_ids = {value.strip() for value in left.split(",") if value.strip()}
    right_ids = {value.strip() for value in right.split(",") if value.strip()}
    return bool(left_ids & right_ids)


def arthouse_signals(df: pd.DataFrame) -> pd.DataFrame:
    """Build the boolean signals used by the project arthouse definition."""
    production = _text_column(df, "production")
    keywords = _text_column(df, "keywords")
    first_language = _text_column(df, "firstLanguage")
    original_language = _text_column(df, "original_language")
    main_country = _text_column(df, "mainCountry")

    language_code = first_language.where(first_language.ne(""), original_language)
    specialty_label = contains_any_term(production, SPECIALTY_LABELS)
    festival_signal = contains_any_term(keywords, FESTIVAL_TERMS) | contains_any_term(
        production, FESTIVAL_TERMS
    )
    keyword_signal = contains_any_term(keywords, ARTHOUSE_KEYWORDS)
    mainstream_risk = contains_any_term(keywords, MAINSTREAM_RISK_KEYWORDS)

    imdb_rating = _numeric_column(df, "imdbRating")
    number_of_votes = _numeric_column(df, "numberOfVotes")
    budget = _numeric_column(df, "budget")
    tmdb_popularity = _numeric_column(df, "tmdb_popularity")

    writer_director_overlap = pd.Series(
        (
            _ids_overlap(directors, writers)
            for directors, writers in zip(
                _text_column(df, "directors"), _text_column(df, "writers"), strict=False
            )
        ),
        index=df.index,
    )

    return pd.DataFrame(
        {
            "specialty_label": specialty_label,
            "festival_signal": festival_signal,
            "keyword_signal": keyword_signal,
            "mainstream_risk": mainstream_risk,
            "non_english_non_us": language_code.str[:2].str.lower().ne("en")
            & main_country.str.upper().ne("US"),
            "high_rating": imdb_rating.ge(7.0),
            "niche_reach_pdf": number_of_votes.le(33),
            "niche_reach_broad": number_of_votes.between(20, 1000, inclusive="both"),
            "low_budget": budget.gt(0) & budget.le(5_000_000),
            "low_tmdb_popularity": tmdb_popularity.le(0.20),
            "writer_director_overlap": writer_director_overlap,
            "has_keywords": keywords.ne(""),
        },
        index=df.index,
    )


def score_arthouse(df: pd.DataFrame) -> pd.Series:
    """Return an integer arthouse evidence score for each film.

    Scoring weights:
    ``+3`` specialty label, ``+2`` festival signal, ``+2`` arthouse keyword,
    ``+1`` non-English/non-US, ``+1`` IMDb rating >= 7.0, ``+1`` 20-1000 IMDb
    votes, ``+1`` low positive budget, ``+1`` writer/director overlap,
    ``+1`` low TMDb popularity, and ``-2`` mainstream-risk keyword.
    """
    signals = arthouse_signals(df)
    return (
        signals["specialty_label"].astype(int) * 3
        + signals["festival_signal"].astype(int) * 2
        + signals["keyword_signal"].astype(int) * 2
        + signals["non_english_non_us"].astype(int)
        + signals["high_rating"].astype(int)
        + signals["niche_reach_broad"].astype(int)
        + signals["low_budget"].astype(int)
        + signals["writer_director_overlap"].astype(int)
        + signals["low_tmdb_popularity"].astype(int)
        - signals["mainstream_risk"].astype(int) * 2
    ).rename("arthouse_score")


def is_arthouse(df: pd.DataFrame, threshold: int = 6) -> pd.Series:
    """Return the project's reusable working arthouse flag.

    The default is a small ensemble:

    * refined project baseline: IMDb rating >= 7.0, <= 33 votes, keywords
      present, and either arthouse evidence or non-English/non-US context;
    * strict canon: specialty distributor/label plus festival signal;
    * composite: score >= ``threshold``, IMDb rating >= 7.0, 20-1000 votes,
      and at least one auditable evidence signal.

    Parameters
    ----------
    df:
        Film dataframe using columns from ``03-data/films_enriched.csv``.
    threshold:
        Composite score cutoff. The project default is ``6``.

    Returns
    -------
    pandas.Series
        Boolean Series aligned to ``df.index``.
    """
    signals = arthouse_signals(df)
    score = score_arthouse(df)
    evidence_signal = (
        signals["specialty_label"]
        | signals["festival_signal"]
        | signals["keyword_signal"]
        | signals["low_budget"]
    )

    refined_provocation_core = (
        signals["high_rating"]
        & signals["niche_reach_pdf"]
        & signals["has_keywords"]
        & (evidence_signal | signals["non_english_non_us"])
    )
    strict_canon = signals["specialty_label"] & signals["festival_signal"]
    composite = (
        score.ge(threshold)
        & signals["high_rating"]
        & signals["niche_reach_broad"]
        & evidence_signal
    )

    return (refined_provocation_core | strict_canon | composite).rename("is_arthouse")
