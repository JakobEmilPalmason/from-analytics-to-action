# Arthouse

We tried two methods to define what counts as an "arthouse" film. 

## The two methods

| Folder | Method |
|---|---|
| `arthouse-method-classification/` | Rule-based: an operational `is_arthouse()` definition built from auditable signals (rating, festival cues, keywords, budget, language). |
| `arthouse-LLM-classification/` | Claude Haiku 4.5 scores each film 1–10 on "arthouse-ness" using the full metadata + plot summary. |


## Two methods in a little more depth

| Method | Description |
|---|---|
| **Rule-based classification** (`arthouse-method-classification/`) | An auditable `is_arthouse()` function that flags a film as arthouse based on hard-coded signals: MPAA rating, festival/award cues, keywords, budget, and original language. Output is a binary yes/no. |
| **LLM scoring** (`arthouse-LLM-classification/`) | Claude Haiku 4.5 reads each film's full metadata plus its plot summary and assigns an "arthouse-ness" score from 1–10, capturing tone and themes the rules can't see. Output is a continuous score. |


## Method comparison

For each method, we drew **50 random films from the films it flags as arthouse** (random_state=42) and judged them by hand. "Genuine" = a recognisable auteur or canonical festival film. "Plausible" = fits the arthouse mould but no strong canonical anchor. "Borderline" = thin info or weak signal in either direction. "Misclassified" = clearly not arthouse (cooking shows, Hollywood thrillers, slasher horror, Nazi-era comedies).

| Metric | `arthouse.py` (rule) | LLM score = 7 | LLM score ≥ 8 | Original data |
|---|---|---|---|---|
| Films passing | 675 | 22,353 | 3,710 | 50,000 |
| % of dataset | 1.35% | 44.7% | 7.42% | 100% |
| Sample size | 50 | 50 | 50 | — |
| Genuine arthouse | 28 (56%) | 3 (6%) | 24 (48%) | — |
| Plausibly arthouse | 9 (18%) | 10 (20%) | 13 (26%) | — |
| Borderline / unknown | 6 (12%) | 20 (40%) | 7 (14%) | — |
| Misclassified | 7 (14%) | 17 (34%) | 6 (12%) | — |
| Est. genuine films in cohort | ≈ 378 | ≈ 1,341 | ≈ 1,781 | — |
| Est. genuine + plausible in cohort | ≈ 500 | ≈ 5,812 | ≈ 2,745 | — |

**Caveat:** n=50 gives a 95% CI of roughly ±14 percentage points around proportions near 50%, tighter for extremes. The cohort extrapolations are directional, not precise.

**What each method does well:**

- **`arthouse.py`** catches canonical auteurs through distributors and festival labels. In the 50-film sample we hit **Chabrol, Audiard (*Dheepan*, Palme d'Or 2015), Manoel de Oliveira, Fatih Akın, Raymond Depardon, Eyal Sivan, Pablo Berger, Andres Veiel, Rob Epstein**, plus a slow-cinema entry (Scott Barley's *Sleep Has Her House*). Highest precision, smallest cohort.
- **LLM ≥ 8** catches auteurs by name recognition. The 50-film sample turned up **Carl Theodor Dreyer (1919!), Theodoros Angelopoulos, Cristi Puiu, Sergey Loznitsa, Céline Sciamma, Raúl Ruiz, Gary Oldman (*Nil by Mouth*), Miklós Jancsó, Stephen Dwoskin, Reis & Cordeiro, Edgardo Cozarinsky, Claire Simon, Manthia Diawara, Noël Burch, The Otolith Group, Sahraa Karimi**, plus several lesser-known festival regulars. Largest cohort of genuine arthouse in absolute terms (~1,781).
- **LLM = 7** is mostly noise. The 50-film sample had only 3 confident hits (Stuber, Segre, Kirtadze); 40% were too thin to judge and 34% were clearly not arthouse (mountaineering docs, oil-spill journalism, 1918 silent comedies, Slovenian slashers, found-footage sci-fi sequels). Treat it as "non-mainstream foreign," not arthouse.

The rule and LLM ≥ 8 are **complementary**: they catch different canonical filmmakers (rule via distributor metadata, LLM via name recognition). Combining them — union, or LLM ≥ 8 as an extra evidence signal in the rule — is likely stronger than either alone.

**Where each method still leaks (from the 50-film samples):**

- **Rule** false positives (7): *Basic Instinct*, the *Department Q* thriller *Fasandræberne*, Corbucci's spaghetti western *Il mercenario*, the Weinstein foodie biopic *Les saveurs du Palais*, an ABC true-crime doc, a 1922 silent comedy, a 1939 Sacha Guitry ensemble comedy. All slipped through the strict-canon or composite paths via specialty distributors and festival keywords on otherwise mainstream titles.
- **LLM ≥ 8** false positives (6): a French adult/porn film, an amateur "consciousness + KungFu" sci-fi, a 1921 D'Annunzio aviation drama mistaken for avant-garde, a 1913 silent Joan of Arc, an IMDb-2.5 indie horror, and a low-budget Maltese horror. The model conflates *obscure + old + foreign* with *avant-garde*.
- **LLM = 7** false positives (17): cooking shows, mountaineering docs by Reinhold Messner, music biographies, journalistic Iraq-business docs, Mercedes/Auto-Union history, Bellman musical, Slovenian slasher, found-footage sci-fi sequels. The model uses 7 as a default-high for any foreign-language film it can't confidently dismiss.
