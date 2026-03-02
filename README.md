# From Analytics to Action

DTU Spring 2026 — Translating analytics into organizational decision-making.

## Project Goal

Support a film/TV audience insights company in connecting artistic ambitions with commercial strategy. The company creates audience insights through AI-enhanced anthropology for film and TV projects across countries. Our task is to turn data into actionable recommendations while being transparent about limitations, assumptions, and the invisible work that makes data usable.

## Decision Questions

- **Project positioning:** How should a film/TV project be positioned to reach its audience?
- **Target audiences & segments:** Who are the most relevant audience groups, and what characterizes them?
- **Market & country strategy:** Which markets or countries offer the best fit for a given project?
- **Comparable-title analysis:** What existing titles serve as useful comparisons, and what can we learn from their performance?

## Expected Deliverables

1. **Explanatory visualization** — a clear, honest visual narrative that supports decision-making (not just displays data).
2. **Pitch / presentation** — communicating findings to stakeholders with attention to context, assumptions, and actionability.

## Data Sources

- [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/) — title basics, ratings, crew, episodes, etc.
- Case-specific data provided by the partner organization (not included in this repo).

## Ethical & Quality Considerations

- IMDb data is for **non-commercial use only** — respect the license.
- Audience data involves assumptions about people and culture — document and question those assumptions.
- Be explicit about what the data does **not** capture (e.g., non-English markets, niche genres, demographic blind spots).
- Distinguish between analytical findings and the interpretive/contextual work needed to make them actionable.
- Avoid presenting model outputs as ground truth — communicate uncertainty.

## Project Structure

```
lectures/           Course lecture materials (week01–week10)
reading-material/   Assigned readings (week01–week10)
data/               Raw and processed data (gitignored)
notebooks/          Jupyter notebooks for exploration and analysis
src/                Python source code
reports/            Figures and slides for deliverables
docs/               Methods documentation and assumptions log
tests/              Unit tests
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
