# From Analytics to Action

DTU Spring 2026 — Translating analytics into organizational decision-making.

## Project Goal

Support **Publikum** (formerly Will & Agency), a film/TV audience insights company, in connecting artistic ambitions with commercial strategy. Publikum creates audience insights through AI-enhanced anthropology for film and TV projects across countries. Our task is to turn data into actionable recommendations while being transparent about limitations, assumptions, and the invisible work that makes data usable.

## Team

| GitHub | Role |
|--------|------|
| [JakobEmilPalmason](https://github.com/JakobEmilPalmason) | Owner |
| [bodvarsdottirkristin](https://github.com/bodvarsdottirkristin) | Collaborator |
| [hlynurblaer](https://github.com/hlynurblaer) | Collaborator |
| [egillbjarnigislason](https://github.com/egillbjarnigislason) | Collaborator |
| [Hilmirbatman](https://github.com/Hilmirbatman) | Collaborator |
| [alessiapapa](https://github.com/alessiapapa) | Collaborator |

## Decision Questions

- **Project positioning:** How should a film/TV project be positioned to reach its audience?
- **Target audiences & segments:** Who are the most relevant audience groups, and what characterizes them?
- **Market & country strategy:** Which markets or countries offer the best fit for a given project?
- **Comparable-title analysis:** What existing titles serve as useful comparisons, and what can we learn from their performance?

## Dataset

**`03-data/European_data_2000.xlsx`** — 2,000 European movies from IMDb with 23 columns:

| Column | Description |
|--------|-------------|
| `titleId` | IMDb identifier (e.g., tt3042384) |
| `imdbUrl` | Link to IMDb page |
| `originalTitle` | Title in original language |
| `englishTitle` | English version of title |
| `titleType` | Film/TV designation |
| `releaseYear` | Year of release |
| `runtimeMinutes` | Duration in minutes |
| `isAdult` | Adult content flag |
| `imdbRating` | User rating (0–10) |
| `numberOfVotes` | Number of IMDb votes |
| `allCountries` | All countries involved (comma-separated) |
| `mainCountry` | Primary country |
| `topFiveActors` | Cast with IMDb IDs and character names |
| `directors` | Director IMDb IDs |
| `writers` | Writer IMDb IDs |
| `plotShort` / `plotMedium` / `plotLong` | Plot summaries at three lengths |
| `genres` | Genre tags (comma-separated) |
| `keywords` | User-contributed thematic tags |
| `production` | Production companies |

Source: IMDb Non-Commercial Datasets, curated by Publikum.

## Project Structure

```
from-analytics-to-action/
├── 00-course-description/       Course introduction and schedule
├── 01-course-material/          Lectures and readings by theme
│   ├── theme1/                  The Organisational Context (weeks 2–3)
│   ├── theme2/                  How to Make Data Valuable? (weeks 4–6)
│   ├── theme3/                  Challenges in the Data Economy (weeks 7–10)
│   └── theme4/                  Presentation & Communication (weeks 11–12)
├── 02-case-study/               Case study materials and presentation notes
│   └── presentation-1.md        Presentation 1: Datafication + EDA
├── 03-data/                     Datasets
│   ├── European_data_2000.xlsx  Main dataset (2,000 European movies)
│   └── Will & Agency.csv        Full dataset (~34,840 titles)
├── notebooks/
│   ├── data_analysis.ipynb           EDA notebook (clean, no outputs)
│   └── data_analysis_executed.ipynb  EDA notebook (with outputs + figures)
├── src/
│   ├── analysis.py              Analysis utilities (comparable-title search)
│   ├── visualize.py             Visualization helpers (set_style, save_figure)
│   ├── process_data.py          IMDb data loading utilities
│   └── download_data.py         IMDb dataset downloader
├── reports/
│   ├── figures/                 18 generated PNG visualizations
│   └── slides/                  Presentation materials
├── docs/                        Methods documentation and assumptions log
├── tests/                       Unit tests
├── README.md                    This file
├── STRUCTURE.md                 Detailed folder structure
└── requirements.txt             Python dependencies
```

## Notebook Overview

The main analysis notebook (`notebooks/data_analysis.ipynb`) contains 14 sections:

1. **Setup & Imports**
2. **Loading the Data** — with datafication reflection
3. **First Look** — column types, summary stats, missing values
4. **Data Cleaning** — parsing comma-separated fields, derived columns
5. **Genre Analysis** — frequencies, co-occurrence heatmap, ratings by genre
6. **Country & Market Analysis** — top countries, genre specializations, co-productions
7. **Ratings & Popularity** — distributions, four-quadrant scatter plot
8. **Temporal Trends** — production volume and genre shifts over decades
9. **Runtime Analysis** — distributions by genre
10. **Keyword & Theme Analysis** — top keywords, co-occurrence patterns
11. **Co-production Network** — country network with centrality metrics (VNA)
12. **Genre Co-occurrence Network** — genre space visualization (VNA)
13. **Comparable Title Analysis** — finding similar titles for positioning
14. **Summary & Limitations** — findings + critical reflections tied to course frameworks

## Course Frameworks Applied

| Framework | Source | Application |
|-----------|--------|-------------|
| Datafication (4 moments) | Flyverbom & Madsen (2015) | Reflecting on data production, structuring, distribution, visualization |
| Exploratory Data Analysis | Sapienza & Lehmann (2021) | Visualization-driven hypothesis formation |
| Visual Network Analysis | Venturini et al. (2021) | Co-production and genre networks |
| Critical data awareness | Mejias & Couldry (2019) | Acknowledging biases and limitations |
| Data Value Typology | Xu et al. (2024) | Understanding data's role in organizations |

## Expected Deliverables

1. **Explanatory visualization** — a clear, honest visual narrative that supports decision-making
2. **Pitch / presentation** — communicating findings to stakeholders with attention to context and actionability

## Setup

```bash
git clone git@github.com:JakobEmilPalmason/from-analytics-to-action.git
cd from-analytics-to-action
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then open the notebook:
```bash
jupyter notebook notebooks/data_analysis.ipynb
```

## Ethical & Quality Considerations

- IMDb data is for **non-commercial use only** — respect the license
- Audience data involves assumptions about people and culture — document and question those assumptions
- Be explicit about what the data does **not** capture (non-English markets, niche genres, demographic blind spots)
- Distinguish between analytical findings and the interpretive work needed to make them actionable
- Avoid presenting outputs as ground truth — communicate uncertainty
