# Week 5 — Exploratory Data Visualization · Oral exam prep

> Note on sources: the `week05-description.md` text actually describes the datafication session (Mejias & Couldry; Flyverbom & Madsen). The header, lecture file (`ExploratoryDataViz_A2A-2026.md`), and reading folder make clear that **Week 5 is Exploratory Data Visualization**, with readings by Sapienza & Lehmann (2021) and Venturini, Jacomy & Jensen (2021). This prep follows the lecture and readings.

## 1. Week overview

This week reframes the analyst's first move from confirmation to exploration. The central question is: **what work does visualization do when we have not yet decided what question to ask?** Sapienza & Lehmann (2021) argue from a data-science perspective that exploration of large datasets — searching for the *right variables* before the *right hypothesis* — is a legitimate and necessary research mode, complementary to hypothesis-driven social science. Venturini et al. (2021) anchor this argument in a concrete technique, Visual Network Analysis (VNA) with force-directed layouts, and defend the *visual ambiguity* of network maps as an asset for exploratory data analysis (EDA) rather than a flaw to engineer away. Together, the readings and Madsen's lecture position EDA — and especially VNA — as the bridge between raw relational traces and the formulation of useful, testable questions about a case.

## 2. Key concepts (define on the spot)

- **Exploratory Data Analysis (EDA)** — Examining data to surface patterns, anomalies, and variables *before* committing to a hypothesis (Tukey, 1977; cited in lecture and Venturini et al., 2021).
- **Hypothesis-driven research** — Deductive paradigm where questions, variables, and tests are pre-specified (sometimes pre-registered); contrasted with EDA in Sapienza & Lehmann (2021).
- **Variable identification** — Sapienza & Lehmann's "secret trick": alongside questions, the data scientist *searches for the variables* that define them, in the manner of natural scientists (Sapienza & Lehmann, 2021, citing Milner 2018).
- **Generalizability vs. immediate usefulness** — A trade-off Sapienza & Lehmann (2021) sketch: exploratory DS findings are general but may have no immediate application; SS/policy work is immediately useful but variables are pre-fixed.
- **Force-directed layout** — Layout algorithm (e.g., ForceAtlas2, Fruchterman–Reingold) where nodes repel each other and edges attract them; equilibrium produces a position where related nodes are closer (Venturini et al., 2021).
- **Spatialization (vs. visualization)** — Force-directed layouts do not project a network into a pre-existing space — they *create* a space whose axes are an emergent property of the relations (Venturini et al., 2021, p. 4).
- **Topological vs. diagrammatic perspective** — Diagrammatic reading follows individual paths between nodes (suited to small networks); topological reading scans for clusters, centres, bridges (suited to medium/large networks). VNA is topological (Venturini et al., 2021).
- **Visual Network Analysis (VNA)** — A practice of analysing a network by (1) positioning nodes via a force-directed layout, (2) sizing them by importance, (3) colouring them by category (Venturini et al., 2021).
- **Relational ambiguity** — The genuine vagueness of empirical relations (e.g., overlapping musical genres). Force-directed layouts *preserve* it; community-detection algorithms hide it behind clean partitions (Venturini et al., 2021).
- **Structural holes** — Sparse zones between dense clusters; in VNA they appear as visual emptiness (Venturini et al., 2021, citing Burt, 1995).
- **Anscombe's quartet** — Four datasets with identical summary statistics but radically different distributions; a canonical argument for visualisation over metrics (lecture).
- **Anscombe / Tukey rationale** — *"The greatest value of a picture is when it forces us to notice what we never expected to see"* (Tukey, 1977; lecture slide 6).
- **Explanatory vs. exploratory visualization** — Explanatory viz (Minard's Napoleon map) is curated to convey a known point; exploratory viz is for noticing the unknown (lecture slide 19).
- **Spatialization quality** — An open problem: there is no settled metric for how faithfully a 2-D layout represents a multidimensional graph; Noack's *normalised edge length* is the current empirical gold standard, equivalent under conditions to Newman's modularity (Venturini et al., 2021).
- **Social Data Science (SDS)** — A still-forming transdisciplinary field that aims to fuse data-science methods with social-theoretic interpretation, requiring new questions, new evaluation criteria, and patient long-term collaboration (Sapienza & Lehmann, 2021).
- **The "invisible gorilla" of hypothesis testing** — When researchers focus on a specific hypothesis they may go *psychologically blind* to other patterns in the data (lecture slide 18, after Yanai & Lercher 2020).

## 3. Per-paper notes

### Sapienza, A., & Lehmann, S. (2021). *A view from data science.* Big Data & Society.

**(a) Core argument.** Working at the boundary of social and data science, the authors argue that data scientists do not arrive with hypotheses — they explore large datasets to identify *what variables matter*, much as Newton identified *force* and *momentum*. Building Social Data Science therefore requires social and data scientists to recognise this asymmetry of method and audience and to build long-term, patient collaborations whose findings are evaluated by new, transdisciplinary criteria.

**(b) Method/empirical basis.** A reflective commentary, not an empirical study, drawing on the authors' joint experience at the Copenhagen Center for Social Data Science (SODAS) and DTU. They use illustrative examples — Brockmann et al. (2006) on dollar-bill mobility; Sekara et al. (2016) on dynamic social networks — and a sketched 2×2 trade-off (Figure 1) between research strategy and immediate applicability.

**(c) Quotable passages.**

- *"As we explore the data, we form informal theories of what might be driving the patterns we see. We learn what the right questions (and variables) are."* (p. 2)
- *"The secret trick (we believe) is that alongside the questions, we search for the variables defining the questions."* (p. 2)
- *"As long as the separation between 'information' and 'noise' (or 'measure' and 'errors', if you prefer) remains unclear, efforts to clean up the picture risk to cut observation along precise but fallacious lines."* (cited in Venturini et al., 2021, but the spirit echoes Sapienza & Lehmann's whole argument; their own line: *"large datasets … cannot be adequately understood from a single disciplinary perspective"*, p. 5, citing Chang et al. 2014.)
- *"A clear example of this experimental design is the practice of preregistration … not only the questions/hypotheses need to be specified but also the variables and tests"* (p. 2–3) — used to mark the *contrast* with EDA.

**(d) Connection to the week.** This paper is the *epistemological licence* for everything else in the week. It explains why EDA is not sloppy science but a different mode of science — one whose first task is to find the variables a hypothesis would later need. It motivates VNA (Venturini et al.) as a paradigmatic EDA technique and grounds the lecture's contrast between hypothesis-driven and exploratory analytics.

---

### Venturini, T., Jacomy, M., & Jensen, P. (2021). *What do we see when we look at networks: Visual network analysis, relational ambiguity, and force-directed layouts.* Big Data & Society.

**(a) Core argument.** Force-directed network layouts have become a de facto tool of digital social and natural sciences, but practitioners read them by intuition; their epistemic basis is implicit. The paper makes the practice of *Visual Network Analysis* explicit: a force-directed layout *spatialises* a graph, producing an emergent space whose readable features (clusters, holes, bridges, polarisation) are valuable precisely *because* they preserve the empirical ambiguity of relational phenomena rather than collapsing it into a single partition or ranking.

**(b) Method/empirical basis.** A methodological/conceptual paper grounded in a worked example: an updated jazz network, scraped from Wikipedia/Wikidata (6,381 nodes — humans, bands, record labels, subgenres — 85,826 edges; pp. 4–5). The authors compare layouts (Fruchterman–Reingold, default ForceAtlas2, ForceAtlas2 with LinLog & gravity = 0), demonstrate node sizing by in-degree vs. Wikipedia page views, and colour by year, nationality, ethnicity, and gender. They then test two attempts to formalise *layout quality* — Euclidean vs. relational distance (geodesic, mean commuting time) and k-means vs. Louvain modularity — and show both partially fail, motivating Noack's *normalised edge length* as the current best heuristic.

**(c) Quotable passages.**

- *"Force-directed layouts do not just project networks in space — they create a space that would not exist without them. This is why this process is better called 'spatialization' rather than 'visualization.'"* (p. 4)
- *"The same ambiguity that makes network charts unfit for hypothesis confirmation, we contend, makes them invaluable for exploratory data analysis."* (p. 2)
- *"In early stages, researchers should respect the inherent ambiguity of their subjects rather than imposing a premature and artificial ordering."* (p. 8)
- *"'Far better an approximate answer to the right question, which is often vague, than an exact answer to the wrong question, which can always be made precise.'"* (Tukey, 1962, quoted on p. 8)
- *"Tools such as Gephi have made network analysis accessible to broad audiences that happily produce network diagrams without having acquired a robust understanding of the concepts and techniques the software mobilizes."* (p. 12, quoting Rieder & Röhle 2017)
- The three "unwritten principles" of point-and-line charts: *"nodes are (1) positioned according to their connectivity; (2) sized proportionally to their importance; and (3) coloured or shaped by their category"* (p. 3).

**(d) Connection to the week.** This paper *operationalises* Sapienza & Lehmann's general argument. If the data-science move is to find the right variables before fixing the question, VNA is a concrete technique for doing that on relational data: spatialise, scan for shapes, hypothesise, recolour, iterate. It is also the paper that backs the lecture's chef-network exercise, where students enact the same EDA loop on Facebook posts about famous chefs.

## 4. Lecture connections (Madsen, 2026)

- **Theme positioning.** The lecture sits in Theme 2 — *Making Data Valuable* — between datafication (week 4) and participatory data design (week 6). The arc is: how data is produced (datafication) → how analysts interrogate it (EDA) → how it is co-shaped with stakeholders (participatory).
- **Tukey is foregrounded.** Madsen opens with John Tukey (1977) and frames EDA as a "reaction to hypothesis-driven statistics" (slides 5–7). He uses pre-registration as the foil — exactly the example Sapienza & Lehmann use — to show what exploration is *not*.
- **Why visualisation, not just metrics.** Anscombe's quartet (1973, slides 14–16): four datasets share descriptive statistics yet look entirely different — visualisation is the quickest route to the structure. He pairs this with Yanai & Lercher's (2020) "hypothesis is a liability" study (slide 17) and the *invisible gorilla* analogy (slide 18): focusing on a hypothesis can blind you to unexpected features.
- **Explanatory vs. exploratory.** Madsen separates Minard's Napoleon map (curated, explanatory) from EDA (slide 19). Useful for the exam: the same chart type can serve different epistemic functions.
- **VNA as a paradigm case.** Slides 21–31 walk through VNA's recipe (force layout → size by centrality → colour by category → name clusters) using Venturini et al.'s techniques.
- **Hands-on exercise — chefs on Facebook.** A 242,000-page Facebook corpus (2010–2018) plus 670 chefs scraped from Wikipedia, with co-mention edges (slides 32–34). Students load `chef_overlap_full.gexf` into Gephi Lite and form hypotheses (e.g., is there a "Nordic" cluster? a Redzepi/Nilsson axis?). This is EDA enacted: variables on nodes (country, mention count, modularity class) and edges (raw vs. normalised overlap) are *available*, not pre-fixed.
- **Practitioner interview.** Madsen brings in Johan from *Will & Agency* on EDA in industry — anchoring the academic argument in consulting practice.
- **Prompts for case work.** *To what extent are your hypotheses testable? What exploratory visualisations would lead you toward better, data-driven hypotheses? Is your data relational — what would the nodes and edges be?* (slide 38). Expect the examiner to map exam discussion onto your case.

## 5. Cross-paper synthesis

- **Both papers privilege variable discovery over hypothesis confirmation.** Sapienza & Lehmann make the general argument; Venturini et al. instantiate it in network space (e.g., the jazz layout *reveals* that time and "genre purity" are the structuring axes — neither was hypothesised in advance).
- **Both quote Tukey.** Tukey's "approximate answer to the right question" (1962) appears explicitly in Venturini et al. (p. 8) and is the spiritual basis of Sapienza & Lehmann's stance and the lecture's framing — a useful single thread that ties the readings together.
- **Both treat ambiguity as productive.** Sapienza & Lehmann frame DS findings as legitimately *generalisable but not immediately useful* — a kind of useful imprecision. Venturini et al. argue the same about visual ambiguity in force-directed layouts: it mirrors the ambiguity of social phenomena.
- **They differ in object and audience.** Sapienza & Lehmann is meta-disciplinary commentary on collaboration; Venturini et al. is methodological documentation. Sapienza & Lehmann worry about *publishing* across fields; Venturini et al. worry about *reading* across dimensions. Read together, one supplies the why, the other the how.
- **Both flag the risk of premature closure.** Pre-registration (Sapienza & Lehmann) and hard community-detection partitions (Venturini et al.) are the same vice in different clothing — fixing the question before the data has been allowed to speak. EDA and VNA are antidotes.

## 6. Likely exam questions (with model answers)

### Q1. What is exploratory data analysis, and why has it become more important with large datasets?

EDA, as Tukey (1977) framed it, is the practice of examining data before committing to a hypothesis — looking for patterns, anomalies, and the right variables. Sapienza & Lehmann (2021) argue that with big behavioural datasets, this is not a methodological convenience but a necessity: when data are abundant, the binding constraint is no longer hypothesis power but *variable identification* — knowing what to measure. Their example of Brockmann et al.'s (2006) dollar-bill mobility study shows how new variables (scale-free jumps, long waiting times) only emerged from exploration. Hypothesis-driven, pre-registered work — common in psychology and economics — locks in variables and questions early and risks "p-hacking" or, worse, asking precisely the wrong question. EDA is the corrective: an "approximate answer to the right question," in Tukey's phrase quoted by Venturini et al. (2021).

### Q2. Sapienza & Lehmann describe a trade-off between research strategy and immediate usefulness. Explain it.

They sketch a 2-D space (Figure 1) where one axis is freedom in choosing questions and variables and the other is immediacy of practical impact. Mathematics and physics live at one extreme — total freedom, often no immediate application; conic sections waited centuries before Kepler used them for orbits. Engineering, parts of social science, and policy-driven economics live at the other — variables are dictated by the question of the day, but findings have direct uptake. Data science currently sits between: it picks its variables (so it generalises) but pays for that with a delay between insight and application. The paper does not romanticise one pole — instead, it argues that interdisciplinary infrastructure (journals, funding, joint training) is needed precisely so that DS exploration and SS theory can together optimise this trade-off rather than each side accusing the other of irrelevance or imprecision.

### Q3. Why do Venturini et al. call force-directed layouts "spatialisation" rather than "visualisation"?

Most charts (bar, scatter) project data into an axis system that exists *before* the data is plotted. A force-directed layout has no pre-existing axes: nodes start randomly, repel each other, are pulled by edges, and settle into an equilibrium where related nodes end up close. The space, in other words, is an emergent property of the relations — *"force-directed layouts do not just project networks in space — they create a space that would not exist without them"* (Venturini et al., 2021, p. 4). This matters for interpretation: distance between two nodes is meaningful in aggregate (clusters, centres) but not in pairwise terms (the Euclidean–geodesic correlation is weak; p. 11). The London tube map (Beck, 1933) is the analogy the authors use — a chart whose proximity encodes connectivity, not geographic distance.

### Q4. What is "relational ambiguity" and why do Venturini et al. defend it?

Many empirical relations are genuinely vague — jazz subgenres overlap, social communities have fuzzy borders, *"the community structure of networks is, for instance, notoriously ambiguous"* (Venturini et al., 2021, p. 9). Community-detection algorithms (e.g., Louvain modularity) impose hard, non-overlapping partitions and can be unstable: small changes in parameters yield very different "best" partitions (citing Calatayud et al., 2019). A force-directed layout instead *renders* this ambiguity — denser zones with blurry edges, polarisations without strict axes. In an exploratory phase, this is a feature: the analyst stays appropriately uncertain. The argument echoes Drucker (2011): a clean statistical chart of "gender distribution" claims more precision than the social category warrants. Tying this to Sapienza & Lehmann (2021): if the goal is to *find* the right variables, a method that hides ambiguity will hide candidates.

### Q5. Walk me through the three steps of VNA using a concrete example.

I'll use the jazz network from Venturini et al. (2021). **Step 1, position:** apply a force-directed layout — they show that ForceAtlas2 with LinLog mode and gravity = 0 reveals clustering that Fruchterman–Reingold collapses. The first read of the resulting shape (vertical stretch, slight horizontal stretch) is itself a finding. **Step 2, size:** size nodes and labels by an importance variable; in-degree and Wikipedia page-views give different stories — in-degree foregrounds Gillespie, Ellington, Davis (jazz canon); page views foreground George Michael, Alicia Keys (pop celebrity). The contrast already suggests a left–right "purity" axis. **Step 3, colour:** by year of birth/inception, nationality, ethnicity, gender. Colour confirms the vertical axis is *time* and the horizontal is *jazz lineage / national origin*; gender produces no fracture, so it is not a structuring variable. The same recipe is what Madsen's chef-network exercise asks students to perform on the Facebook corpus.

### Q6. Sapienza & Lehmann claim data scientists "are not hypothesis-driven in the sense of many social scientists." How do Venturini et al. illustrate this?

The jazz analysis in Venturini et al. (2021) is a textbook instance. The authors do not begin with "hypothesis: nationality structures jazz networks." They begin with a layout, *observe* a vertical stretch, *guess* time, recolour and confirm; observe a horizontal stretch, guess "jazz purity," recolour and confirm. The variables that explain the structure are produced *during* the exploration, not before it. This matches Sapienza & Lehmann's claim that *"as we explore the data, we form informal theories of what might be driving the patterns we see. We learn what the right questions (and variables) are"* (Sapienza & Lehmann, 2021, p. 2). The jazz example is therefore an existence proof for their epistemological argument.

### Q7. Why is there no settled metric for "spatialisation quality," and what is the closest current candidate?

Venturini et al. (2021) try two metrics. First, correlate Euclidean distance in the layout with relational distances (geodesic, mean commuting time): the correlation is weak because force-directed layouts are not designed to be read pairwise. Second, compare geometric clustering (k-means on the layout) with relational clustering (Louvain modularity): correspondence is good in highly clustered networks (the Karate club) but poor in polarised ones (jazz) — and this is *expected*, because if the layout's value is preserving ambiguity, no clustering metric can capture it. The current best candidate is Andreas Noack's *normalised edge length* — total edge length divided by total inter-node distance and graph density — which Noack proved is mathematically equivalent to Newman's modularity for simple cases. Minimising it is likely NP-complete (like maximising modularity), suggesting force-directed iteration is hard to outperform deterministically. The honest answer at the exam: *we don't have one yet; LinLog is the empirical gold standard*.

### Q8. The lecture used Anscombe's quartet. Why?

Anscombe (1973) constructed four datasets with identical means, variances, correlations, and regression lines — yet plotted, they look completely different (one is linear with noise, one curved, one a clear outlier driving the fit, one a single high-leverage point). The quartet shows that summary statistics under-determine data structure: numbers can mislead in ways that a simple scatter cannot. In Tukey's (1977) words quoted in the lecture, *"the greatest value of a picture is when it forces us to notice what we never expected to see."* It is therefore the simplest possible motivation for EDA: even when a metric appears trustworthy, visualisation may surface anomalies the metric is structurally blind to — the same logic Venturini et al. (2021) extend to relational data, where centrality rankings can be more misleading than a force-layout map.

### Q9. How might VNA apply to your own case-company data?

[Adapt to your case.] As a template: identify a relational structure in the data — co-occurrences, co-purchases, co-citations, co-mentions, communications. Define nodes and edges (e.g., for a hospital no-show case, nodes = clinics, edges = shared patients). Spatialise in Gephi Lite, size by traffic, colour by speciality. The point is not to test a hypothesis but to use the resulting map to *generate* better hypotheses than the ones the company currently holds, then state explicitly what the layout's ambiguity is concealing vs. revealing. This directly answers Madsen's slide-38 prompts.

### Q10. What does it mean — for analytics practice — to take Sapienza & Lehmann's "interdisciplinarity is necessary" claim seriously?

It means three things. First, *staffing*: an exploratory analysis on behavioural data needs both a data scientist (to find variables) and a social scientist (to interpret motivations) — *"large datasets … cannot be adequately understood from a single disciplinary perspective"* (Sapienza & Lehmann, 2021, p. 5). Second, *patience*: the authors stress that interdisciplinary collaborations need long timelines because evaluation criteria, journals, and incentives still favour disciplinary work. Third, *practice*: bring in the other discipline at the *exploration* stage, not as a post-hoc reviewer — Venturini et al.'s jazz analysis worked because a jazz expert (Emiliano Neri, in their footnote) helped name the clusters. For an industry analytics team, the implication is that the EDA loop should already include the domain expert, not just hand them final dashboards.

## 7. One-minute elevator answer

Week 5 was about exploratory data visualization — the analytic move you make *before* you have a hypothesis. Sapienza and Lehmann argue that data scientists do not start from questions but from large datasets, and that their genuinely original contribution is identifying the *variables* that any later hypothesis will need. That mode is in tension with hypothesis-driven social science, which pre-fixes both questions and variables. Venturini, Jacomy and Jensen take this argument into a concrete technique: visual network analysis with force-directed layouts. They show, with a 6,000-node jazz network, that you can spatialise a graph, scan it for clusters and polarisations, and let those visual features — including their inherent ambiguity — generate hypotheses, rather than confirm them. Madsen's lecture stitched this together with Tukey, Anscombe's quartet, and a hands-on Gephi Lite exercise on chefs in Facebook posts. The case prompt is to ask, of your own data: are my hypotheses really testable, and would an exploratory map of the relations get me to a better question first?
