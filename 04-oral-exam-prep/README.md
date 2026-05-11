# Oral Exam Preparation — Orientation

> **For future agents and for me:** This folder contains preparation material for the individual oral exam portion of the DTU course *From Analytics to Action* (Spring 2026). This README is the orientation document. Read it first before doing anything in this folder.

---

## What I'm preparing for

I am Jakob Emil Palmason, a student at DTU. I am preparing for the **oral exam** in *From Analytics to Action*. The exam has two parts and this folder is focused on **the second part** — the individual oral examination, which is **50% of the final grade**.

### Full exam structure (for context)

- **Duration:** 45 minutes total, 6 students per group, external examiner
- **Grading:** Danish 7-step scale (-3, 00, 02, 4, 7, 10, 12)
- **Part 1 — Group pitch (50% of grade)**
  - 12-minute pitch maximum, equal time for all 6 team members
  - Supported by an A1 hard-copy poster (≤ 450 words) submitted in advance
  - Assessed on: visualisation quality (25%) and pitch quality (25%)
- **Part 2 — Individual oral examination (50% of grade)**
  - This is what this folder is about
  - Each student is questioned individually after the group pitch
  - Examiners pull on the pitch and probe the syllabus

### What the individual portion specifically assesses

Direct from the course assessment criteria:

> - Your answers in the second part of the oral exam (individual examination) clarify questions the pitch gives rise to and **draws on the syllabus**.
> - Your answers demonstrate a **thorough understanding of the course objectives seen from the literature**.
> - You can **explain, apply and reflect** on key concepts and findings presented and discussed in the course readings.
> - Your answers are well argued and clearly reasoned.
> - Your answers demonstrate the ability to **reflect on the role of data analytics in organisational context critically and analytically**.

### What this means in practice (my framing for prep)

Three skill levels are being tested:

1. **Explain** — Recall and explain a concept clearly when named (e.g. "what is datafication?").
2. **Apply** — Map a concept onto my case work without prompting (e.g. "how does the four-moments framework describe what your group did?").
3. **Reflect critically** — Articulate where a concept breaks, what it misses, who would push back. *This is the level that separates a 7 from a 12.*

Future summary or study material produced in this folder should be calibrated to all three levels — not just description and recall.

---

## My case (so summaries can be specific)

The case company is **Publikum** (formerly Will & Agency), a film/TV audience-insights company that uses AI-enhanced anthropology to inform film and TV projects across countries. My group of 6 is working with their data to support audience and positioning decisions.

- **Dataset:** ~2,000 European films from IMDb (`03-data/European_data_2000.xlsx`), with a fuller `Will & Agency.csv` (~34,840 titles) also available. Enriched in places with TMDb (budget/revenue/popularity), IMDb GraphQL (per-star rating distributions), and MovieLens 32M (user ratings/tags).
- **My specific work:** I have been building an **arthouse cohort** definition using a **hybrid rule** — a hand-built rule **OR** an LLM score ≥ 8. Coverage and method-comparison notebooks live in `notebooks/arthouse/`.
- **Publikum's decision questions:**
  1. **Project positioning** — How should a film/TV project be positioned to reach its audience?
  2. **Target audiences & segments** — Who are the most relevant audience groups, and what characterises them?
  3. **Market & country strategy** — Which markets or countries offer the best fit?
  4. **Comparable-title analysis** — Which existing titles are useful comparisons, and what can we learn from their performance?

When agents produce summaries with an "apply to my case" section, they should refer to specifics: the arthouse hybrid rule, the IMDb data origin, the four decision questions, the ~2,000 European films, and the limitations of those data choices. Not generic film/audience hand-waving.

---

## Course structure (where readings live)

The course is organised into four themes across weeks 2–12. Materials live under `01-course-material/`. Each week folder contains `lectures/`, `reading-material/`, and a `weekNN-description.md`.

| Theme | Title | Weeks | Status in repo |
|---|---|---|---|
| 1 | The Organisational Context | 2–3 | Full content |
| 2 | How to Make Data Valuable? | 4–6 | Full content (weeks 4, 5, 6) |
| 3 | Challenges in the Data Economy | 7–10 | Weeks 7, 9, 10 have content; **week 8 empty** |
| 4 | Presentation & Communication of Data Projects | 11–12 | **All empty** — placeholders only |

**Important caveats agents should know:**
- `01-course-material/theme2/week05/week05-description.md` is currently a **copy of week 04's description** (incorrect). The actual week is *Exploratory data visualization*, not datafication. Don't treat that file as authoritative — use the lecture deck filename (`ExploratoryDataViz_A2A-2026`) and the readings present (Sapienza & Lehmann; Venturini et al.) to infer week 5's actual focus.
- Week descriptions for weeks 6–12 are **stub placeholders** (one-line "Week NN Description" headers). For weeks 6, 7, 9, 10 the lecture deck title and reading list are the best signal of what the week is about until the description arrives.
- Lectures are stored as **PDF + extracted Markdown + slide images**. Agents should prefer reading the `.md` extractions over the PDFs — they're faster to work with and equivalent in content.
- One file in week 06 has " - Copy" in its filename (`Jensen et. al. (2021) - Participatory Data Design - Acting in a digital world. - Copy.pdf`) — likely an accidental duplicate. Treat it as the canonical Jensen et al. (2021) reading until a clean copy replaces it.

### Generating markdown extracts

Two repo scripts handle the PDF → markdown conversion. Run them after dropping new PDFs into the right `weekNN/` folder:

```bash
cd /Users/jep/Desktop/DTU/from-analytics-to-action
source .venv/bin/activate
python src/reading_material_pdf_to_md.py     # readings (skips existing .md unless --overwrite)
python src/lecture_pdf_to_md.py              # lectures + slide images
```

### Tiered priority (which readings matter most for the oral)

**Tier 1 — must know cold (assigned readings).** Examiners can fairly probe these in detail.

| Week | Reading | File path (relative to repo root) |
|---|---|---|
| 2 | Zammuto et al. (2007) | `01-course-material/theme1/week02/reading-material/Zammuto et. al. (2007) - Information Technology and the Changing Fabric of Organization.md` |
| 2 | Justesen & Plesner (2024) | `01-course-material/theme1/week02/reading-material/Justesen and Plesner (2024) - invisible digi-work compensating connecting and cleaning in digitalized organizations.md` |
| 3 | Xu et al. (2024) | `01-course-material/theme1/week03/reading-material/Xu et al. (2024) - Time to reassess data value - The many faces of data in organizations..md` |
| 4 | Mejias & Couldry (2019) | `01-course-material/theme2/week04/reading-material/Mejias and Couldry (2019) - Datafication..md` |
| 4 | Flyverbom & Madsen (2015) | `01-course-material/theme2/week04/reading-material/Flyverbom and Madsen (2015) - Sorting data out..md` |
| 5 | Sapienza & Lehmann (2021) | `01-course-material/theme2/week05/reading-material/Sapienza and Lehmann (2021) - A view from data science..md` |
| 5 | Venturini et al. (2021) | `01-course-material/theme2/week05/reading-material/Venturini et. al. (2021) - What do we see when we look at networks - Visual network analysis, relational ambiguity, and force-directed layouts..md` |

**Tier 2 — read structured summary, skim original briefly.** General/supplementary readings, useful as critical hooks or counter-arguments.

| Reading | File path (relative to repo root) |
|---|---|
| Flyverbom & Murray (2018) — Datastructuring | `01-course-material/theme1/week02/reading-material/Flyverbom and Murray (2018) - Datastructuring - Organizing and Curating Digital Traces into Action..md` |
| Galbraith (2014) — Org design under big data | `01-course-material/theme1/week02/reading-material/Galbraith, J. R. (2014) - Organizational design challenges resulting from big data..md` |
| Mützel (2025) — Big data and ML methods | `01-course-material/theme1/week02/reading-material/mützel.2025.BDandMLmethods.md` |
| Birch (2023) — Data Enclaves | `01-course-material/theme1/week03/reading-material/Birch K. (2023) - Data Enclaves.md` |

**Tier 3 — skim summary only.**
- `01-course-material/theme1/week02/reading-material/20260208_BD_ML_SM_small.md` — looks like a reference deck, not a primary reading
- Davis (2022) affordances video (referenced in week 2 description; not in repo as a file — link only)

**Recently added — assignment status TBD (treat as Tier 1 by default).** These were added after the original tiering. Their week descriptions are still stub placeholders, so I don't yet know which are *assigned* vs *general*. Until the descriptions arrive, summarising agents should give them the same depth as Tier 1 readings.

| Week | Theme | Reading | File path (relative to repo root) |
|---|---|---|---|
| 6 | 2 — Participatory Data Design | Jensen et al. (2021) — Participatory Data Design | `01-course-material/theme2/week06/reading-material/Jensen et. al. (2021) - Participatory Data Design - Acting in a digital world. - Copy.md` |
| 6 | 2 — Participatory Data Design | Madsen (2024) | `01-course-material/theme2/week06/reading-material/Madsen (2024).md` |
| 7 | 3 — Ethics / data-driven management | Big Data Socio-Technical Infrastructures | `01-course-material/theme3/week07/reading-material/BigDataSocioTechnicalInfrastructures.md` |
| 7 | 3 — Ethics / data-driven management | Micheli et al. (2020) — Emerging models of data governance | `01-course-material/theme3/week07/reading-material/micheli-et-al-2020-emerging-models-of-data-governance-in-the-age-of-datafication.md` |
| 9 | 3 — Resistance | Hoeyer & Wadmann (2020) — *Meaningless work* (datafication of health) | `01-course-material/theme3/week09/reading-material/Hoeyer and Wadmann (2020) - ‘Meaningless work’ - How the datafication of health reconfigures knowledge about work and erodes professional judgement..md` |
| 9 | 3 — Resistance | Milan (2024) — Resistance in the data-driven society | `01-course-material/theme3/week09/reading-material/Milan S. (2024) - Resistance in the data-driven society..md` |
| 10 | 3 — Environmental impact of AI | Supply-chain capitalism of AI / algorithmic harms via environmental lens | `01-course-material/theme3/week10/reading-material/The supply chain capitalism of AI  a call to  re think algorithmic harms and resistance through environmental lens-2.md` |

**Still missing:** Week 8 (theme 3) and weeks 11–12 (theme 4) have no readings or lectures in the repo as of the last update.

**Lectures (use as context, not as readings to summarise on their own):**

| Week | Lecture | File path |
|---|---|---|
| 2 | Winthereik — Organizational Context | `01-course-material/theme1/week02/lectures/Winthereik Lecture Feb 9 2026 Organizational Context.md` |
| 3 | The value of data | `01-course-material/theme1/week03/lectures/Lecture Feb 16 The value of data_2026.md` |
| 4 | Datafication | `01-course-material/theme2/week04/lectures/Datafication_A2A_2026.md` |
| 5 | Exploratory Data Visualisation | `01-course-material/theme2/week05/lectures/ExploratoryDataViz_A2A-2026.md` |
| 6 | Participatory Data Design | `01-course-material/theme2/week06/lectures/ParticipatoryDataDesign_A2A_2026.md` |
| 7 | Ethical perspectives on data-driven management | `01-course-material/theme3/week07/lectures/Lecture March 16 Ethical perspectives on datadriven management_2026.md` |
| 9 | Resistance | `01-course-material/theme3/week09/lectures/Lecture_Resistance_13 April 2026.md` |
| 10 | Environmental impact | `01-course-material/theme3/week10/lectures/Lecture April 20 Environ Impact.md` |

---

## Other useful orientation files

If an agent needs more context than this README, these are the next places to look:

- `README.md` (repo root) — Project overview, dataset description, frameworks-applied table, enrichment pipeline
- `STRUCTURE.md` (repo root) — Folder layout
- `02-case-study/presentation-1.md` — The group's first presentation (Datafication + EDA), useful for understanding how the group has framed Publikum's challenge so far
- `02-case-study/PUBLIKUM_DTU_Analytics to Action_2026.pdf` — Publikum's introductory deck to the class
- `notebooks/arthouse/` — My in-progress arthouse cohort notebooks (rule + LLM ≥ 8 method)
- `notebooks/analyses/` — General analysis notebooks
- `reports/figures/` — 60+ generated figures from analysis work
- `docs/methods.md` and `docs/assumptions.md` — Methods and assumptions log (if present)

---

## Style requirements for any study material produced in this folder

When producing summaries, study notes, or Q&A material here, follow these rules unless I say otherwise:

1. **Plain English.** Define every technical or theoretical term the first time it appears, in parentheses, in everyday language. Don't write "epistemic affordance" without immediately explaining what that means. Pretend you're explaining to a smart friend who has not read organisation theory.
2. **Long, not short.** Don't compress. Take space to explain ideas slowly with concrete examples. Better to over-explain than to leave me with a vague sense of the argument.
3. **Concrete examples first.** Walk through the author's own examples in detail before generalising. Don't skip the case studies — they're what makes ideas stick.
4. **Apply specifically.** "Apply to my case" sections must name specifics from my case (Publikum, arthouse, hybrid rule, IMDb, four decision questions). Generic application doesn't help.
5. **Critical view always included.** Every summary should include a section on the limitations of the reading — what it misses, where it doesn't quite fit, who would push back. This is what gets me from a 7 to a 12.
6. **Quotable lines preserved.** Pull 2–3 short quotes per reading that I could paraphrase or invoke in the oral. Include page or section references where the markdown shows them.
7. **Examiner-mode questions.** Every reading summary should end with 3–5 questions an external examiner could plausibly ask, each with a 3–4 sentence model answer in my voice (first person OK).
8. **No academic hedging.** Say what the author says, directly. Avoid "the author seems to suggest" — they either say it or they don't.
9. **Vary sentence length.** Short sentences for emphasis. Longer ones when an idea genuinely needs unpacking.
10. **Bullets only when listing parallel things.** Prefer prose where it reads better.

---

## Output conventions for this folder

Suggested layout for material produced under `04-oral-exam-prep/`:

```
04-oral-exam-prep/
├── README.md                          (this file — orientation)
├── week02-reading-notes.md            (long-form summaries, week 2 readings)
├── week03-reading-notes.md
├── week04-reading-notes.md
├── week05-reading-notes.md
├── concept-lookup.md                  (cross-reading concept → source table)
├── question-bank.md                   (anticipated examiner questions + model answers)
└── method-defence.md                  (justifications for our pitch's method choices)
```

These files are aspirational — agents producing material should create whichever ones the user has asked for, in the structure above, unless the user specifies otherwise.

---

## Quick prompt template for delegating to another agent

When I (or any agent acting on my behalf) wants to delegate work on this folder to another agent, the prompt should include at minimum:

1. **Pointer to this README:** "Read `/Users/jep/Desktop/DTU/from-analytics-to-action/04-oral-exam-prep/README.md` first for full context."
2. **Specific deliverable:** which week, which readings, which file to write.
3. **Output path:** absolute path under `04-oral-exam-prep/`.
4. **Length expectation:** "long-form, ~8,000–15,000 words is fine — quality over compression."
5. **Style reminder:** "Follow the style requirements in the orientation README."

The README should do most of the heavy lifting so individual prompts can stay short.
