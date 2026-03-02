# WIP Presentation 1 — Publikum / Will & Agency Case Study

**Course:** From Analytics to Action, DTU Spring 2026
**Case company:** Publikum (formerly Will & Agency)
**Dataset:** `Will & Agency.csv` — ~34,840 film and TV titles with 23 columns

---

## Part 1: Datafication (Week 4)

*Drawing on Flyverbom & Madsen's (2015) four analytical moments — Production, Structuring, Distribution, Visualization — and Mejias & Couldry's (2019) framework on datafication.*

---

### Q1: How was your data made and how is it now made available to you? Could it be otherwise?

The dataset we received is a curated extract built primarily from **IMDb Non-Commercial Datasets** (title.basics, title.ratings, title.akas), enriched by Publikum with additional fields such as plot descriptions (short, medium, long), keywords, production companies, and country/language mappings.

Following Flyverbom & Madsen's (2015) typology, we can trace the data's journey through their four analytical moments:

- **Production:** The underlying data originates from IMDb — a user-contributed, Amazon-owned database where millions of users submit ratings, and editorial staff and automated systems maintain title metadata. This is not "raw" data; as Geoffrey Bowker (2008) reminds us, "raw data is an oxymoron." Every IMDb entry reflects decisions about categorization (what counts as a "genre"), geographic attribution (what is a title's "main country"), and quality thresholds (minimum votes for a rating to appear).
- **Structuring:** Publikum selected and restructured these IMDb datasets into a single flat CSV of ~34,840 rows. This involved decisions about which titles to include, how to handle multi-country productions (the `allCountries` vs. `mainCountry` split), how to represent multi-genre titles (comma-separated strings), and what metadata to carry forward (actors limited to top five, for instance).
- **Distribution:** The data was made available to us as a static CSV file — a snapshot, not a live feed. We have no access to the underlying IMDb API, Publikum's proprietary tools, or any update mechanism.
- **Visualization:** At this stage, the data has not yet been visualized by us. Publikum's own visualization layer — their PlotBounce tool and audience research dashboards — remains inaccessible to us.

**Could it be otherwise?** Yes, significantly:

- Streaming platforms (Netflix, Disney+, HBO) hold viewership data that would capture *actual audience behavior*, not just ratings from self-selected IMDb users
- Box office and ticket sales data (e.g., from The Numbers, Box Office Mojo) would add a commercial performance dimension
- Publikum's own proprietary data — their Story audience reactions (~8,000 respondents per project, video-based), Zeitgeist societal data (social media monitoring across countries), and PlotBounce's 500 expectation clusters built from 163,000 films — would provide the qualitative, anthropological layer that defines their methodology
- Wikipedia page views (as suggested in the course) could serve as an alternative popularity proxy

---

### Q2: Who made it and with what interests? Do these interests align with your interests? Could there be other interests?

The data has multiple makers, each with distinct interests:

**IMDb / Amazon** created and maintains the underlying database. Their interest is in building a comprehensive entertainment catalogue that drives traffic to Amazon's ecosystem. IMDb data is optimized for *discovery and browsing* — it is structured around individual titles, not around the analytical questions a consulting firm like Publikum would ask. Mejias & Couldry (2019) would note that this reflects a broader pattern of datafication where data is produced primarily to serve platform logics.

**Publikum** curated the dataset from IMDb's raw exports. Their interest is in *audience insight consulting* for the film and TV industry — specifically, helping producers and film funds position projects strategically across markets. As their presentation makes clear, their core value proposition is connecting "artistic ambitions and commercial strategy" through "AI-enhanced anthropology." They work across 150+ projects in 12 countries for clients including the Danish Film Institute, Norsk filminstitutt, Zentropa, Nordisk Film, DR, and many others.

**Alignment with our interests:** Partially aligned. We share an interest in understanding patterns in film/TV data — genre distributions, market dynamics, comparable titles. However, there is a fundamental gap: Publikum's methodology is built on a **three-pillar approach** (Story, Zeitgeist, References) where our dataset only covers the *References* pillar. The Story pillar (audience reactions to narrative elements via a 6-episode mobile research method yielding ~500 video responses per project) and the Zeitgeist pillar (social media monitoring of cultural conversations, e.g., "How is narcissism different in Scandinavia?" for the film *Sick of Myself*) are not represented in our data at all.

**Other interests in the company/organization:**

- **Filmmakers and directors** want to know how to position their story to reach the right audience without compromising artistic vision
- **Film funds and institutes** (public funders like DFI, NFI) want evidence-based market assessments to justify funding decisions
- **Producers** want comparable titles and market fit analysis to support pitching and distribution deals
- **Distributors** want to know which markets offer the best fit for a given project

These varied stakeholder interests mean the same dataset might need to be sliced, interpreted, and presented very differently depending on the audience.

---

### Q3: What would need to change at the level of production, structuring, and/or distribution for you to best address the challenge? How realistic are those changes?

Using Flyverbom & Madsen's (2015) framework:

**Production level:**

- Access to **audience reaction data** from Publikum's Story research would be transformative — currently we have no qualitative dimension at all. *Realism: Low — this is proprietary and project-specific.*
- **Streaming viewership data** would allow us to measure actual audience engagement rather than relying on IMDb votes as a proxy. *Realism: Very low — platforms guard this closely.*
- **Box office / admissions data** per country would add a commercial performance layer. *Realism: Medium — some of this is publicly available through industry databases.*
- **Social media / Zeitgeist data** as Publikum collects it (e.g., 1.48M mentions of "narcissism" across platforms, filtered by country) would enable cultural context analysis. *Realism: Low — requires specialized monitoring tools and domain expertise.*

**Structuring level:**

- **Separate genre and keyword columns** rather than comma-separated strings would make analysis much more straightforward. *Realism: High — we can do this ourselves through data cleaning.*
- **Normalized country data** with clear primary/secondary market designations. *Realism: High — partially already done with `mainCountry` vs. `allCountries`.*
- **Temporal engagement data** — when did a title gain traction, in which markets, and in what sequence? *Realism: Low — not captured in the current data.*
- **Plot embeddings or cluster assignments** from PlotBounce's 500 expectation clusters. *Realism: Medium — Publikum could provide these if willing, as the tool is built on the same IMDb data + DTU collaboration.*

**Distribution level:**

- **API access** rather than a static CSV would allow dynamic querying and integration with other data sources. *Realism: Low for IMDb (commercial license required), but Publikum could potentially provide access to PlotBounce.*
- **Regular data updates** to track how the landscape changes over time. *Realism: Medium — IMDb datasets are updated regularly and freely downloadable.*

---

### Q4: What can be done within the frame of the available datafication? And with what reservations vis-a-vis the results?

Within the available data, we can pursue several analytical directions:

- **Genre and market mapping:** Which genres dominate in which countries? How do genre distributions differ between, say, Scandinavian and Southern European markets?
- **Comparable title identification:** Given a new project's genre, plot keywords, and target market, which existing titles are most similar? (This is essentially what PlotBounce does, but we can build a simpler version.)
- **Rating and popularity patterns:** What characterizes highly-rated vs. highly-voted titles? Do these patterns differ by market or genre?
- **Cross-market production patterns:** Which countries frequently co-produce? What language combinations appear most often?
- **Keyword and plot analysis:** What thematic clusters emerge from keywords and plot descriptions? (Text analysis / NLP approaches.)
- **Temporal trends:** How have genre distributions, rating patterns, and production volumes shifted over time?

**Reservations — these are critical to communicate transparently:**

- **IMDb rating bias:** IMDb's user base skews male, English-speaking, and younger. Ratings may significantly underrepresent audience reception in non-English markets, for older demographics, or for genres like romance and family films (Sapienza & Lehmann, 2021, on the gap between data and the phenomena it claims to represent).
- **Popularity ≠ commercial success:** Number of IMDb votes is a proxy for visibility/engagement, not for ticket sales, streaming views, or cultural impact. A film can be commercially successful with few IMDb votes (e.g., local-language hits) or have many votes without commercial returns.
- **Missing qualitative dimension:** As Mejias & Couldry (2019) argue, datafication always involves reduction — turning complex social phenomena into quantifiable data points. Our dataset captures *what* films exist and how they are rated, but not *why* audiences respond to them, which is precisely what Publikum's Story and Zeitgeist pillars address.
- **Snapshot bias:** The data is a point-in-time extract. Ratings, vote counts, and even genre classifications change over time.
- **Keyword inconsistency:** Keywords in IMDb are user-contributed and not standardized, making systematic keyword analysis unreliable without significant cleaning.
- **The "oxymoron" problem:** Following Bowker's insight that Flyverbom & Madsen highlight — every analytical finding we produce is shaped by the datafication choices made upstream. Our "discoveries" are partly artifacts of how IMDb categorizes, how Publikum selected, and how we structure our analysis.

---

## Part 2: Exploratory Visualization & Networks (Week 5)

*Drawing on Sapienza & Lehmann (2021) on data science methodology and Venturini et al. (2021) on visual network analysis.*

---

### Q5: To what extent do you have clear hypotheses? To what extent are they testable?

At this stage, we have **preliminary hypotheses** that are more exploratory than confirmatory:

**Hypothesis 1: Genre-market fit varies systematically across countries.**
Some genres (e.g., crime/thriller in Scandinavia, comedy in France, horror in the US) may cluster more strongly in certain national markets. *Testable:* Yes — we can cross-tabulate genres and `mainCountry` and look for over-/under-representation. *Limitation:* We only see what was *produced*, not what audiences *wanted*.

**Hypothesis 2: Higher-rated titles tend to be associated with specific genre combinations.**
Multi-genre titles (e.g., drama + thriller) may systematically rate differently than single-genre titles. *Testable:* Yes — we can analyze rating distributions by genre combination. *Limitation:* Confounded by vote count (niche films may have inflated ratings from small, self-selected audiences).

**Hypothesis 3: International co-productions have different rating and visibility profiles than single-country productions.**
Titles produced across multiple countries may reach broader audiences (more votes) but receive more moderate ratings. *Testable:* Yes — we can compare titles by number of countries in `allCountries`. *Limitation:* Co-production status may correlate with budget, which we don't have.

**Hypothesis 4: Plot keywords cluster into thematic groups that map onto Publikum's "expectation clusters."**
If we apply text analysis to keywords and plot descriptions, we may be able to approximate the 500 expectation clusters that PlotBounce identifies. *Testable:* Partially — we can cluster, but cannot validate against PlotBounce's actual clusters without access to them.

**Hypothesis 5: Certain directors and actors serve as "bridges" between national film industries.**
People who work across countries may connect otherwise separate market ecosystems. *Testable:* Yes — this is directly addressable through network analysis.

These hypotheses are deliberately broad because, as Sapienza & Lehmann (2021) argue, premature hypothesis-narrowing in data science risks missing the most interesting patterns. We are still in the exploration phase.

---

### Q6: What would be good exploratory visualizations to guide you towards more data-driven hypotheses?

Following Sapienza & Lehmann's (2021) emphasis on letting data guide hypothesis formation:

- **Genre distribution bar chart by country** — to see which markets are genre-specialized vs. genre-diverse
- **Heatmap of genre co-occurrence** — which genres frequently appear together on the same title?
- **Scatter plot: IMDb rating vs. number of votes** — to identify different "quadrants" (popular & well-rated, niche & well-rated, popular & polarizing, etc.), colored by genre or country
- **Release year timeline** — production volume over time, potentially faceted by country or genre, to identify trends and inflection points
- **Box plots of ratings by main country** — are certain national cinemas systematically rated higher/lower?
- **Word cloud or frequency chart of keywords** — to identify dominant themes in the dataset
- **Keyword co-occurrence network** — a lightweight version of what PlotBounce does, showing which themes cluster together
- **Country co-production chord diagram** — which countries collaborate most frequently?
- **Runtime distribution by genre** — are there conventions being followed or broken?

These visualizations serve different purposes: some are *descriptive* (what does the data look like?), some are *comparative* (how do subgroups differ?), and some are *relational* (what connects to what?). The relational ones naturally lead into network analysis.

---

### Q7: Is your data relational? How could you explore it through visual network analysis?

Yes — our data is **deeply relational**. As Venturini et al. (2021) argue, network visualization is not just a method but a way of *seeing* that reveals structures invisible in tabular data. The "relational ambiguity" they describe — where the same data can produce very different networks depending on how nodes and edges are defined — is particularly relevant here.

**Concrete network configurations:**

| Network type | Nodes | Edges | What it reveals |
|---|---|---|---|
| **Title similarity** | Titles | Shared genres, keywords, or actors | Clusters of "comparable titles" — the core of Publikum's References pillar |
| **Collaboration** | People (actors, directors, writers) | Co-worked on same title | Industry structure, key connectors, national vs. international careers |
| **Country co-production** | Countries | Shared productions | Geopolitical patterns in film industry collaboration |
| **Genre affinity** | Genres | Co-occurrence on same title | Which genres "belong together" in the industry's mental model |
| **Keyword/theme** | Keywords | Co-occurrence on same title | Thematic landscape of the dataset — approximating PlotBounce's clusters |
| **Actor-country bipartite** | Actors + Countries | Actor appeared in title from that country | Which actors bridge national markets |

**Most promising for our case:** The **title similarity network** (nodes = titles, edges = shared genres + keywords) would most directly serve Publikum's core use case of finding comparable titles and understanding expectation clusters. This mirrors what PlotBounce does computationally with 163,000 films and 500 clusters, but at a more exploratory scale.

The **collaboration network** would be particularly interesting given Publikum's Scandinavian focus — we could visualize how the Nordic film industry connects internally and to the broader European and global market.

Following Venturini et al.'s (2021) caution about "relational ambiguity," we should be transparent that the choice of what constitutes a node and an edge is itself an analytical decision that shapes what we can see. A genre-based similarity network will surface different patterns than a keyword-based one, and both are valid but partial representations.

---

## Summary & Next Steps

We are working with a dataset that is rich in metadata but fundamentally limited to the *References* pillar of Publikum's three-pillar methodology. The data tells us what films exist and how they are categorized, but not why audiences respond to them (Story) or how they connect to cultural conversations (Zeitgeist).

**What we can do well:**
- Map the landscape of film/TV production across genres, countries, and time
- Identify comparable titles and thematic clusters through keyword/plot analysis
- Explore industry structure through network analysis of collaborations and co-productions

**What we must be transparent about:**
- IMDb data carries systematic biases (demographic, linguistic, geographic)
- Quantitative patterns in this data are not equivalent to audience insight
- Our findings are "structured reflections, not conclusions" — to borrow Publikum's own phrase about their AI-enhanced anthropology approach
