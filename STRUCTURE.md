# Project Structure

## Overview

```
from-analytics-to-action/
├── 00-course-description/       Course introduction and overview
├── 01-course-material/          Lectures and readings organized by theme
│   ├── theme1/                  The Organisational Context
│   │   ├── week02/
│   │   └── week03/
│   ├── theme2/                  How to Make Data Valuable?
│   │   ├── week04/
│   │   ├── week05/
│   │   └── week06/
│   ├── theme3/                  Challenges in the Data Economy
│   │   ├── week07/
│   │   ├── week08/
│   │   ├── week09/
│   │   └── week10/
│   └── theme4/                  Presentation and Communication of Data Projects
│       ├── week11/
│       └── week12/
├── 02-case-study/               Case-specific materials
├── 03-data/                     Datasets (IMDb + case data)
├── notebooks/                   Jupyter notebooks for exploration and analysis
├── src/                         Python source code
│   ├── download_data.py         Download IMDb non-commercial datasets
│   ├── process_data.py          Load and clean data
│   ├── analysis.py              Analysis utilities
│   └── visualize.py             Visualization helpers
├── reports/
│   ├── figures/                 Generated visualizations
│   └── slides/                  Presentation materials
├── docs/
│   ├── methods.md               Analytical methods documentation
│   └── assumptions.md           Assumptions log
├── tests/                       Unit tests
├── README.md                    Project overview and setup
├── STRUCTURE.md                 This file
└── requirements.txt             Python dependencies
```

## Themes

| Theme | Title | Weeks |
|-------|-------|-------|
| 1 | The Organisational Context | 2–3 |
| 2 | How to Make Data Valuable? | 4–6 |
| 3 | Challenges in the Data Economy | 7–10 |
| 4 | Presentation and Communication of Data Projects | 11–12 |

## Weekly Folder Layout

Each week folder follows the same structure:

```
weekXX/
├── lectures/           Lecture slides and notes
├── reading-material/   Assigned readings
└── weekXX-description.md   Week overview, schedule, and reading questions
```
