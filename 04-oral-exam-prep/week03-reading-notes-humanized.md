# Week 03 — Reading Notes for the Oral Exam

*From Analytics to Action, DTU Spring 2026 — Theme 1: The value of data, and what gets hidden when we talk about it.*

Long-form study notes on the two week 3 readings. Xu et al. (2024) on the four roles of data in organizations, and Birch (2023) on data enclaves and parasitic innovation. Built for the individual oral exam.

## How to use this file

This is a study document, not a summary. Read each section slowly. If an examiner asks *"what does Xu et al. mean by data as a commodity?"*, the answer is in §1.3. If they ask *"how would Birch criticise the way your group is using IMDb data?"*, look at §2.5 and §3. For cross-reading questions, jump to §3 and §4.

The file is structured around the three skill levels the oral exam tests: **explain** (recall the concept), **apply** (map it onto Publikum / arthouse / IMDb), and **reflect critically** (where the concept breaks).

## Navigation

| Section | What it covers |
|---|---|
| §1 — Xu et al. (2024) | The four-faces typology in full depth: tool, commodity, practice, algorithmic intelligence |
| §1.6 — Apply Xu to my case | Mapping our Publikum / arthouse / IMDb work onto the four roles |
| §1.7 — Critical view of Xu | Where the typology smooths over real friction |
| §1.8 — Quotes worth knowing | Three quotable lines from Xu et al. |
| §1.9 — Likely examiner questions on Xu | Q&A in my voice |
| §2 — Birch (2023) | Data enclaves, techcraft, assetization, parasitic innovation |
| §2.5 — Apply Birch to my case | What Birch lets me say critically about Publikum and IMDb |
| §2.6 — Critical view of Birch | Where Birch overreaches |
| §2.7 — Quotes worth knowing | Three quotable lines from Birch |
| §2.8 — Likely examiner questions on Birch | Q&A in my voice |
| §3 — Connecting Xu and Birch | Where they agree, where they tension, what they together let me say |
| §4 — Cross-reading exam questions | Questions an examiner can build that span both readings |

---

# §1. Xu, Indulska, Asadi Someh & Shanks (2024) — *Time to reassess data value: The many faces of data in organizations*

## 1.1 One-paragraph elevator summary

Xu and her co-authors argue that the way Information Systems research has talked about data, as a single thing, valued in a single way, fitting into a single resource-based-view story about competitive advantage, has fallen behind what data is actually doing in organizations today. They run a structured literature review of 142 papers and find that data plays not one role but four, each with its own purpose, value-creation mechanism, and configuration of people, technology, and organization. **Data as a tool** supports human decision-making. **Data as a commodity** is sold or traded between organizations. **Data as a practice** is embedded in repeatable routines that produce continuous learning and innovation. **Data as algorithmic intelligence** sits inside AI/ML systems that make decisions with little or no human in the loop. The contribution is a typology that lets researchers and practitioners ask the more grounded question: *for this specific use, which role is data playing, and therefore which value-creation pathway and which management capability does it require?* Generic claims about "data as a strategic asset" don't survive contact with this typology.

## 1.2 The big argument

The paper's central claim is that the purpose and context of data use determine the role data plays. Role determines value, the way value is created, and the management capabilities the organization needs to extract that value. There is no general theory of "data value" that holds across contexts. Different uses of data create value through different mechanisms, with different actors at the centre, requiring different organizational capabilities. Treating all data the same way, as one big strategic resource, is a category error.

Two background frames hold the argument together.

The first is Orlikowski and Iacono's (2001) *views* framework, originally a typology of five common stances toward IT artifacts in IS research (the tool view, proxy view, ensemble view, computational view, nominal view). Xu et al. borrow four of these views and pin each to one of their data roles. The point is to anchor each role in an existing theoretical tradition rather than invent four categories from scratch.

The second is the move from "data as resource" to "data as multifaceted artifact." The old IS canon treats data like raw material: something you have, that produces value through resource allocation and decision support. Xu et al. say that worked when most organizations used data only for managerial decision support. It now misses three other things data does (gets sold, gets practiced into routines, gets baked into algorithms), and each of those has its own logic.

## 1.3 The four roles in depth

### 1.3.1 Data as a Tool (Orlikowski's "tool view")

**Plain-English version:** data is a calculator. A human picks it up, uses it to think more clearly, and puts it down. The calculator doesn't decide; the person does.

**Purpose:** informing managerial decision-making. Forecasts, dashboards, KPI reports, customer-insight reports.

**Value-creation pathway:** data improves the *quality* of human decisions. Better planning, better resource allocation, better strategic alignment. The benefit is captured at firm level (sales, market value, customer satisfaction) but it flows from people thinking better with data than without it.

**Interplay between people, technology, organization:** human-centred. The user is the key enabler. Without a human asking a useful question and interpreting the output, the data sits there inert. Data in this role is, in Orlikowski's words, "definable, unchanging, and independent." Separable from the organizational setting.

**Characteristics of data in this role:** subjective in value (depends on what the user is trying to do), situated, contextualized, instrumental.

**The lecture's examples:** retail demand forecasting (a supermarket reads dashboards and orders inventory) and hospital resource allocation (administrators use patient-flow data to staff wards). In both cases, the data does not "decide." It informs a human decision.

### 1.3.2 Data as a Commodity (Orlikowski's "proxy view")

**Plain-English version:** data is a thing you can sell. Like grain or oil, it has a price, it changes hands, and it sits in a market.

**Purpose:** data trading. Direct sale, exchange for other resources, or bundling into a paid service. Most often inter-organizational rather than within a single firm.

**Value-creation pathway:** revenue. Data marketplaces (Dawex, Narrative, Data & Sons), data brokers (Acxiom, Experian), and bundled data products. The chain is: generate, prepare, package, broker, price, transmit, consume.

**Interplay:** the relationship is between buyer and seller in a two-sided market. Data here is *decontextualizable*. You have to strip it from its original setting and make it portable so that someone else, who never collected it, can use it.

**Characteristics:** monetizable, modular (atomic data points that can be repurposed and recombined), editable, reprogrammable, distributable, exchangeable. Crucially *non-rival*. Jones and Tonetti's (2020) point that data, unlike grain, can be sold to many buyers at once without diminishing it. This is what Xu et al. mean when they say data trading produces *increasing returns* rather than the usual diminishing returns.

**The lecture's examples:** consumer-data marketplaces (selling aggregated behavioural data to advertisers) and weather-data services (logistics or agriculture firms buying climate data).

**Why this matters for the exam:** the commodity role is where I can pivot to Birch. Xu et al. say data is a commodity if it's traded; Birch will say data is *not* a commodity at all because it isn't fungible, and that this is exactly why Big Tech can hoard it in enclaves. More on that in §3.

### 1.3.3 Data as a Practice (Orlikowski's "ensemble view")

**Plain-English version:** data is a habit, not a thing. The value sits not in the dataset but in the *repeated routine of using* the dataset. The daily standup that looks at the numbers, the recommendation engine that retrains itself, the team that has internalised "we always check the data first."

**Purpose:** enabling innovation and organizational learning. Continuous improvement of products, services, and processes.

**Value-creation pathway:** data participates in a designed business process. Through repetition, the organization builds capabilities that competitors cannot easily copy because they're embedded in routines, culture, and tacit know-how. Grover et al. (2018)'s "three gears" — data, insights, actions — work together to produce sustained competitive advantage.

**Interplay:** people are *one part of an ensemble* that also includes processes, infrastructure, management support, and corporate culture. The repeating pattern is what binds them. Data here is *organizationally embedded* and not easily separable from the firm. You can copy a dataset; you cannot easily copy the practice.

**Characteristics:** organizationally embedded, context-situated, exhibits *data-enabled learning* and *data network effects* (Hagiu & Wright, 2020. The more users use the platform, the better the data gets, the better the platform gets, the more users it attracts.) Adaptable, integrable, complex, and possessing a *social identity* within the community that produces it.

**The lecture's examples:** Netflix recommendation systems (continuously learning from user interactions) and Uber trip-data refinement (pricing and routing improving through repeated feedback cycles). Both are cases where the data isn't valuable on its own. It becomes valuable through the routine of being acted upon and looped back in.

### 1.3.4 Data as Algorithmic Intelligence (Orlikowski's "computational view")

**Plain-English version:** data is engine fuel for machines that *act*. Not just inform a decision but make the decision, take the action, and possibly do so without telling a human.

**Purpose:** automating tasks, processing decisions, and modelling outcomes through AI and machine learning.

**Value-creation pathway:** computational capabilities. Process automation (RPA, robotic decision-making) and algorithmic decision-making (ADM). Value creation happens through *substitution* of human labour (Zuboff's "automate") and through the generation of new information about automated processes (Zuboff's "informate"). LLMs like ChatGPT, fraud-detection models in banking, predictive-maintenance triggers in factories.

**Interplay:** machine-centred. With increasing autonomy, the algorithm acts on behalf of (and sometimes against) humans. Berente et al. (2021) and Baird & Maruping (2021) describe this as a shift in the "primacy of human agency." The algorithm is no longer a passive tool. Murray et al. (2021) call this "conjoined agency." Different configurations of who-controls-what between human and machine.

**Characteristics:** mimics human capability and skill, automated and self-trained, has a *deeper learning capacity*, *inscrutable* (the AI doesn't tell you why it decided what it decided), reusable, recombinable, and forms complex networks of technologies each with its own design objectives. Inscrutability is the key new property. It brings benefits but also genuine risk (Rinta-Kahila et al. 2021's discrimination cases, Sadiq et al. 2022's call for human oversight).

**The lecture's examples:** fraud detection (machine learning models flag suspicious transactions automatically) and predictive maintenance (industrial sensors trigger their own maintenance alerts).

## 1.4 Putting them side by side: the typology table from the paper

Worth memorizing in compressed form because an examiner can ask "what's the difference between X and Y" for any pair.

| | **Tool** | **Commodity** | **Practice** | **Algorithmic Intelligence** |
|---|---|---|---|---|
| **Purpose** | Inform decisions | Trade for revenue | Embed in routines for learning | Automate and decide |
| **Value comes from** | Better human judgment | Direct sale | Continuous improvement / network effects | Autonomous action and scale |
| **Who drives value?** | Humans | Market actors (buyer + seller) | Organization and its routines | Algorithms |
| **Separability from org** | High — data is portable and independent | High — must be decontextualized to trade | Low — embedded in routines, hard to copy | Medium — model is portable but the data + ecosystem is not |
| **Theoretical view** | Tool view | Proxy view | Ensemble view | Computational view |
| **Key author(s)** | Brynjolfsson & McElheran (2016); Knox (2007) | Birch et al. (2021); Wixom & Farrell (2019); Aaltonen et al. (2021) | Grover et al. (2018); Hagiu & Wright (2020); Gherardi (2000) | Davenport & Ronanki (2018); Berente et al. (2021); Shollo et al. (2022) |

The lecture's compressed version is even tighter: tool answers *"what should we decide?"*, commodity answers *"what can we sell?"*, practice answers *"how do we continuously improve?"*, algorithmic intelligence answers *"what can be automated?"*. I'll memorise that. It's the cleanest 30-second articulation.

## 1.5 What the lecture asks me to do with this

The Slide 16 exercise is the move the examiner is most likely to test: *take one example and show how data plays all four roles simultaneously.* This isn't optional for the exam. It's the apply-and-reflect skill the course wants. I work through this for our case in §1.6, using a recommendation system on European film data, which is essentially the kind of system Publikum's questions are reaching toward.

## 1.6 Apply Xu et al. to my case (Publikum / arthouse / IMDb)

Our group's work for Publikum is a dataset of ~2,000 European films from IMDb, enriched with TMDb (budgets, revenue, popularity), IMDb GraphQL (per-star rating distributions), and MovieLens 32M (user ratings and tags). My specific contribution is the arthouse cohort: a hybrid definition that flags a film as arthouse if a hand-built rule fires *or* an LLM scores it ≥ 8. Publikum's four decision questions are about positioning, audience segments, country-market fit, and comparable-title analysis.

Let me run the four-roles test on this work.

**Data as a tool.** This is what the IMDb dataset *is* for our group, most of the time. We pull it into a notebook, compute coverage statistics, look at how the arthouse cohort distributes across countries and genres, and use the result to inform a recommendation about how Publikum should think about the arthouse audience. The dataset doesn't decide anything; we read it and decide. The value is in the *quality of judgment* we give Publikum about positioning and comparable titles. This is the dominant role of data in our project. Question 1 (positioning) and Question 4 (comparable-title analysis) are pure tool-view questions.

**Data as a commodity.** The data we use *originated* as a commodity. IMDb has a paid API, TMDb has commercial licensing terms, MovieLens is shared under an academic license. So even though *we* don't sell data, the inputs to our analysis sit inside a commodity logic. More interestingly: the *output* of Publikum's audience-insight work is a kind of data product. Publikum sells insight to film and TV producers. That's a commodity logic, even if what's being sold is a report rather than a CSV. Worth keeping in my back pocket because it's the answer to "where in your work is data being commodified?". Publikum's *business model* is closer to commodity than tool.

**Data as a practice.** This is the role hardest to demonstrate from a 14-week student project, and I should be honest about that with the examiner. We're not running a production system that learns from continuous feedback. But the *hybrid arthouse rule* is a tiny slice of practice-view thinking. It's a repeatable artifact (rule + LLM ≥ 8) that any future analyst at Publikum could re-apply to a new dataset, and it improved through iteration. We tightened the rule and locked the definition over several commits. At Publikum's scale, *data as practice* would look like every new project applying the same enrichment pipeline, the same tagging conventions, the same comparable-title methodology. The value is that comparison and accumulation become possible across projects, not just within them. This is the role most relevant to Publikum's long-term value, and the role where they currently leave the most on the table.

**Data as algorithmic intelligence.** The LLM in the hybrid rule is a small example of this. The model scores a film for "arthouse-ness" autonomously. We don't read each plot summary; we trust the model. There's a real risk attached. The LLM is *inscrutable*, exactly as Xu et al. and Berente et al. (2021) describe. We don't know why it scores *Festen* at 9 and *Le Quattro Volte* at 7. We accepted this trade-off because we cross-validated against the rule and against human judgment, but the inscrutability concern is real and it's the right thing to flag in the exam. A more developed version of this role at Publikum would be a recommendation engine that auto-targets segments, or a generative model that drafts marketing copy. They're not there yet.

**The exercise the lecture asks for: show all four roles in one example.** Take a recommendation system Publikum could build for a streaming partner: recommend a comparable European arthouse title given a viewer's history. *Tool*: a marketing manager looks at the dashboard of recommendations and decides which to license. *Commodity*: the underlying user-rating data from MovieLens is licensed in (commodity inflow); the recommendation report is sold to the streamer (commodity outflow). *Practice*: the model retrains weekly from new viewing data and the team has a Tuesday-morning ritual of reviewing model drift. That's where a competitive moat would form. *Algorithmic intelligence*: the recommendation itself is auto-generated and auto-personalised at scale. All four roles, one system. This is the kind of integrated answer that signals exam-12 thinking.

## 1.7 Critical view of Xu et al.

The typology is useful but it has soft edges, and an examiner who's read the paper carefully will probe them.

**First, the boundaries are not as clean as the table suggests.** Xu et al. concede this themselves on the second-to-last page: *"the four types of data roles we conclude in this paper do not seem to have clear-cut boundaries in the way they are performed in practice; the context of use, and the value they represent, can be interwoven in many organizational practices."* The example they give is exactly the one I just worked through above. A repeatable data-as-tool process *becomes* data-as-practice over time. So in the cleanest cases, you can see all four roles in one system. The typology is a heuristic for asking better questions, not a partition of reality.

**Second, the paper is silent on the dark side of data.** Xu et al. acknowledge this in their limitations: they pay attention only to the *strategic* and *positive* uses of data. They explicitly defer the "nominal view" (Orlikowski's fifth view, where data is gathered for symbolic/ritual reasons rather than instrumental use, per Feldman & March 1981, Essén et al. 2022) and the "dark sides" of data (Rana et al. 2022). This is where Birch comes in. Birch is doing exactly the work Xu et al. defer.

**Third, the "data as commodity" framing imports an economic vocabulary that may not survive scrutiny.** Xu et al. cite Jones & Tonetti (2020) on data being "non-rival" and use this to argue that data trading produces increasing returns. But Birch's argument is that data is *not actually* fungible. Every dataset is an artefact of a specific collection architecture, so two datasets purporting to measure the same thing don't substitute for each other. If Birch is right, the commodity role partially evaporates. Data isn't really a commodity; it's an *asset* (capitalizable, controlled rather than owned, generating future revenue without sale). The Xu typology's commodity quadrant collapses some important political-economy distinctions.

**Fourth, the paper doesn't theorize power.** Who decides which role data plays in a given organization? Xu et al. write as though the firm chooses freely. But for most organizations the role is forced on them by the platforms they depend on. Google Analytics imposes a tool-role on data; AWS imposes an infrastructure-role; the GDPR imposes governance constraints. The "interplay between people, technology, and organization" in the typology table is bilateral. It leaves out the third party that actually sets the rules. Again, Birch fills this gap.

**Fifth, the empirical method has the usual literature-review problems.** 142 papers, 41 journals, but the search keywords ("data business value," "data monetization," etc.) front-load the strategic-resource framing the authors are trying to move beyond. The sample is biased toward IS-positive studies; it's no surprise the typology comes out optimistic. A more critical sample (HCI, STS, science studies of data, science-and-technology-policy literature) would have surfaced more friction. The paper acknowledges this implicitly when it says future research should engage adjacent disciplines.

**Sixth, the lecture's "who drives value" column glosses over a real tension.** When the lecture says practice is driven by "organization and routines" and algorithmic intelligence is driven by "algorithms," it sounds neutral. But who *built* the routines, and who *maintains* the algorithm? People did. The "shifting agency" Xu et al. note is real but it's not as clean as the table makes it look. This is a place where I should be careful in the exam. The typology doesn't say humans disappear, only that the *primacy* shifts.

## 1.8 Quotes worth knowing

> *"The purpose of data use determines the role data play in organizations and the value they create."*

The paper's thesis in a single sentence. Use it to anchor any answer about the typology.

> *"Unless data are sought, selected, extracted, and interpreted [for a purpose], they cannot inform."* (Jones, 2019, quoted on p. 2)

The paper's epistemological starting point. It rules out a naive "data has intrinsic value" framing and makes context the central variable. Useful when an examiner asks anything that sounds like "isn't more data always better?"

> *"There appears to be an interchanging value flowing between the four data roles, which needs to be further addressed by future research."* (closing section)

The authors' own admission that the typology is porous. Use this if an examiner pushes me to say which role applies to a borderline example. It's *legitimate*, per the authors, to say "more than one, and they trade off over time."

## 1.9 Likely examiner questions on Xu et al. — with model answers

**Q1. What are the four roles Xu et al. identify, and what distinguishes them?**

There are four. Data as a tool (used for managerial decision-making, value comes through better human judgment, human-centred). Data as a commodity (traded between organizations for revenue, value comes from sale, depends on data being decontextualizable). Data as a practice (embedded in repeatable routines, value comes from continuous improvement and data network effects, organization-centred). And data as algorithmic intelligence (driving AI/ML systems that act with autonomy, value comes from automation at scale, machine-centred). The four are differentiated by the purpose of use, the value-creation pathway, the interplay between people-technology-organization, and the characteristics data exhibits in each role. The deeper claim is that purpose determines role, and role determines value. There's no single answer to "what is data worth?" without specifying use.

**Q2. Apply the typology to your group's work for Publikum. Which role dominates, and why?**

The dominant role in our analysis work is data as a tool. We pull IMDb-derived data into notebooks, compute statistics about the arthouse cohort, and use the output to inform recommendations to Publikum about positioning and comparable titles. But all four roles are present at different layers. The data we use originates as a commodity (TMDb and IMDb sell access). My hybrid arthouse rule is a small instance of practice. A repeatable artifact that any future analyst could apply. And the LLM-scoring component is a small instance of algorithmic intelligence with the inscrutability that Xu et al. flag as the defining concern of that role. Publikum's *business model*, as opposed to our analysis work, is closer to commodity. They sell insight as a product. The role isn't fixed; it depends on which slice of the project you're looking at.

**Q3. The authors say their categories aren't clear-cut. Doesn't that undermine the typology?**

Not really, no. A typology isn't a partition. It's a tool for asking better questions about which forces are dominant in a given case. The fact that all four roles can co-exist in a recommendation system doesn't weaken the framework; it strengthens it, because it lets me say "this Netflix-style system creates value through *all four* mechanisms simultaneously, and managing it well requires capabilities relevant to all four." What the typology does usefully rule out is the naive "data is a strategic resource" answer that treats every data-related project as the same management problem. The blurry edges are the point. They're where interesting management questions live.

**Q4. Where does the typology fall short?**

Three places. First, it doesn't theorize power. Xu et al. write as though firms freely choose which role data plays, but in practice the role is often forced by the platforms and regulators a firm depends on. Second, it ignores the dark side of data. Symbolic data-gathering that never gets used, surveillance, exploitation. The authors acknowledge this and defer it to future work, but it matters. Third, the commodity quadrant imports an assumption (data is non-rival and tradable like a commodity) that other authors, Birch in particular, directly reject. If you treat data as a non-fungible artefact of its collection architecture, the commodity role looks much less like a real category and more like a marketing pitch.

**Q5. Take a recommendation system. Show how all four roles operate in it.**

Picture a recommendation engine that suggests comparable European arthouse titles to viewers on a streaming platform. Data is a *tool* for the marketing team that reads the dashboard and decides which titles to license. Data is a *commodity* both upstream (the platform licenses MovieLens-style ratings data in) and downstream (the platform sells the recommendation insight to producers). Data is a *practice* through the weekly retraining cycle and the team's routine of reviewing model drift and tagging conventions. That's the moat. And data is *algorithmic intelligence* in the recommendation itself, which is auto-generated, auto-personalised, and inscrutable. The four roles aren't competing here; they're stacked. Each one supports a different kind of value, and managing the system well means investing in capabilities for all four.

---

# §2. Birch (2023) — *Data Enclaves*

## 2.1 One-paragraph elevator summary

Kean Birch is a political economist at York University writing in the science-and-technology-studies (STS) tradition. *Data Enclaves* is his short, punchy 2023 book arguing that we have been thinking about data the wrong way. Personal data is not a natural resource sitting around waiting to be collected, not a commodity that gets bought and sold in real markets, and not a property right that individuals can own. It is an *asset*. Capitalizable property that can be controlled (rather than owned) and from which future revenues accrue without a sale. Big Tech corporations have built *data enclaves*. Hoarded, contractually-fenced silos of personal data that they neither own nor sell, but control through the techno-economic configuration of their ecosystems. These enclaves are not markets. They're privately-governed pseudo-markets where Big Tech sets the rules. The enclaves entrench themselves through *parasitic innovation*. Innovation deliberately designed to limit competition, exploit users, and extract rents rather than to deliver socially beneficial products. Birch argues that the standard critical response (calling this "surveillance capitalism" or "the attention economy") misses the real mechanism: Big Tech doesn't just watch us, it controls the very *information* that markets are supposed to depend on, which is why competition in their domains has effectively died. The book ends with a call to rethink data governance through data trusts, public data infrastructures, accounting reforms, and stronger regulation like the EU's Digital Markets Act and Digital Services Act.

## 2.2 The big argument

The book's spine is a chain of four linked claims.

**(1) Data is not raw; it is *made*.** Drawing on Gitelman & Jackson's slogan that *"raw data is an oxymoron"* and on James C. Scott's *Seeing Like a State*, Birch introduces the term *techcraft* to describe how Big Tech's collection architectures don't just record information about pre-existing users. They *generate* users as legible, measurable, valuable techno-economic objects. The "user" with their daily-active-user metric, their click-through rate, their viewable impression, is an artefact of the metrics and standards Big Tech has invented to monetize attention. A person's "data twin" is not a copy of them; it's a construct optimized for revenue.

**(2) Data is an asset, not a commodity.** Personal data fails the basic test for being a commodity (fungibility) because every dataset is uniquely shaped by the architecture that generated it. Two datasets that purport to measure the same behaviour don't substitute for one another. So data isn't a commodity; it's an *asset* in the technical accounting sense. Capitalizable property held for the future revenue it can produce, controlled through contractual arrangements rather than property rights. This matters because asset logic is investment logic, not market logic. Asset value is whatever investors expect future revenues to be, discounted to today.

**(3) The mechanism of control is contractual, not proprietary.** Big Tech doesn't *own* your data. Nobody legally can, since facts about a person aren't ownable. What Big Tech has is *control* via terms-of-service contracts, privacy policies, APIs, SDKs ("boundary assets"), and platform-level rules. Contracts are private law. Privately drafted, enforced by the state but not authored by the state. So Big Tech sets the rules of the game inside its ecosystem. This is why Birch prefers the word *enclave* to "platform" or "ecosystem". Enclave captures the political-economic fact that these spaces are walled off from public regulation by privately-made contractual rules.

**(4) The result is the death of markets and the rise of parasitic innovation.** Innovation in this regime isn't aimed at building better products. It's aimed at locking in users, undermining competitors, exploiting users' psychology, and extracting rent. Birch documents this with a long case study of Alphabet/Google's adtech ecosystem (the dynamic-allocation manipulation, the second-price-but-actually-third-price Project Bernanke auction, the post-2018 restrictions on data-transfer files). The deeper point is that "free markets" are supposed to depend on transparent, truthful information about supply, demand, and preferences. The very information that Big Tech now hoards inside enclaves. So the libertarian justification for letting Big Tech do what it wants ("markets work, leave them alone") is self-defeating: there *are no markets* in the relevant sense anymore.

The book doesn't argue this means we should abolish markets. It argues that the fix is *better data governance*. Collective trusts, accounting reforms forcing data onto balance sheets, ex-ante regulation like the EU's DMA/DSA. The political project is to make Big Tech *accountable* for the asset it currently controls without disclosing.

## 2.3 Key concepts (with everyday-language definitions and exam relevance)

**Techcraft.** Birch's neologism, modelled on James Scott's "statecraft." Just as a state makes its population *legible* to itself through tools like the census, the cadastral map, and standardized surnames (Scott's argument in *Seeing Like a State*), Big Tech makes individuals legible to itself through metrics like daily-active-user, viewable-impression, click-through-rate, average-revenue-per-user. The point is that the metrics don't passively observe an underlying reality; they *constitute* the reality they measure. The "user" is an artefact of techcraft; so is "engagement." *Why this matters for the exam:* whenever an examiner asks about how data gets shaped before it's analysed, techcraft is the right vocabulary. It's also the right way to push back on the lazy "data is the new oil" cliché. Oil exists in the ground; user data only exists because the architecture was built to extract it.

**Data enclave.** Big Tech's siloed, contractually-fenced reservoir of personal data, controlled through technical interoperability limits and socio-legal terms-of-service. Distinct from a "platform" (just a piece of digital infrastructure) and from an "ecosystem" (a heterogeneous assemblage of devices, users, developers, etc.). What makes an *enclave* an enclave is the *restricted access*. The wall around the ecosystem that lets Big Tech control who plays inside, on what terms, and with what data. Enclaves emerge through four steps: measurement (deploying the metrics to define users), engagement (configuring users via terms of service and ecosystem norms), enclave (using interoperability and contracts to wall off the resource), monetization (locking in users via subscriptions, ads, or platform fees). *Why this matters:* the word "enclave" is the unit of analysis for the whole book. If I can use it accurately in the exam, I've shown I've read Birch.

**Parasitic innovation.** Innovation deliberately designed to extract value rather than create it. Limiting access to resources, undermining regulations, undermining competitors, exploiting customers' psychology, locking customers in, preventing right-to-repair, weaponizing information asymmetries. Birch's examples include Tinder's age-based price discrimination, HP's printers that sabotage themselves with non-HP ink, generative AI trained on scraped copyrighted data. The contrast is with innovation that delivers a genuinely better product. *Why this matters:* parasitic innovation is the right vocabulary for criticizing dark-pattern UX, predatory pricing, and the gradual enshittification of platforms. It's also the right counterpoint to a naive "innovation is always good" framing.

**Assetization.** The process by which something (data, education, knowledge, biological material) is turned into an asset. An asset, in Birch and Muniesa's (2020) definition, is *"something that can be owned or controlled, traded, and capitalized as a revenue stream, often involving the valuation of discounted future earnings in the present."* The point of an asset is *not* to sell it. The point is to extract durable rent from it. Seven distinguishing features of assets versus commodities: they're legal constructs requiring state-enforced ownership/control; they're defined by contractual ownership/control rather than property; they're implicated in rent extraction; they have unique supply/demand logics; their value reflects discounted future expectations; their value is shaped by the actions of owners (who can transfer or transform them); and their valuation is dynamic, governed by ongoing organizational practices. *Why this matters:* whenever I can make the move from "we have data" to "we hold this data as an asset," I've made Birch's central analytical move. It's also the critical lens to apply to Xu et al.'s commodity quadrant.

**Boundary assets.** Birch and Bronson's (2022) term for the technical plug-ins (APIs, SDKs, OAuth integrations, "Sign in with Google") that let third parties connect to Big Tech's ecosystem. Boundary assets are how the enclave grows. They let Big Tech enrol other businesses (app developers, retailers, news sites) into reinforcing the ecosystem in exchange for access to its users. *Why this matters:* if an examiner asks how Big Tech grows so big, the boundary-asset answer (rather than the network-effects answer) is the one that ties back to Birch.

**Reflexivity / reflexive data.** Drawing on Lyotard and Giddens, Birch points out that personal data has a strange property: knowing about it changes it. Once users learn what data is being collected, they game it (lying about ages, faking locations, using throwaway accounts, ad-blocking). Once Big Tech knows users are gaming, they redesign the architecture. The system never settles. Reflexivity is one of three "data paradoxes" Birch identifies in Chapter 6. *Why this matters:* this is what undercuts the assumption that more data means more truth. More data also means more incentive to game.

**Emergent properties of data.** When datasets are combined and aggregated, they generate properties that none of the source datasets had on their own. This is *both* what makes data so commercially valuable (programmatic advertising depends on combining behaviour, social, location, and demographic data) *and* what makes individualistic privacy regulation inadequate (Esayas 2017, Viljoen 2020 on relational data: even if you opt out, your group's aggregated data still reveals things about you). *Why this matters:* this is the technical reason "consent-based" privacy regimes can't work. You can't meaningfully consent to a future inference that hasn't been drawn yet.

**Pseudo-markets.** Birch's term for the inside-the-enclave dynamic that *looks* like a market (there's pricing, there's bidding, there's "supply" and "demand") but is actually a privately-administered system where Big Tech sets the rules, controls the information, and rigs the outcome. Project Bernanke (Google's secret switch from second-price to third-price auctions for publishers) is the paradigmatic example. *Why this matters:* it's the precise diagnosis of why "competition policy" has been so slow to bite. What looks like a market isn't one, so the usual market-correcting tools don't apply.

**Enshittification.** Cory Doctorow's term, which Birch adopts. The lifecycle of a platform: first it's good to its users to build a base; then it abuses users to please its business customers; then it abuses the business customers to extract maximum rent for itself; then it dies. This is enclave logic playing out over time. *Why this matters:* it's quotable and it gives a useful timeline for any platform-based case (Twitter, Uber, Reddit, etc.).

## 2.4 The examples Birch uses

### 2.4.1 Alphabet/Google's adtech ecosystem (Chapter 5, the book's central case study)

Birch's main empirical case for what an enclave does. The argument unfolds in roughly five steps.

First, online advertising splits into search advertising (matching keywords with bids) and display advertising (text/image/video on websites and apps). In the early 1990s, advertisers and publishers dealt directly. As the web exploded, intermediaries emerged: ad servers, ad networks (DoubleClick, founded 1995, acquired by Google in 2008). DoubleClick aggregated "remnant" inventory, the ad slots publishers couldn't sell directly, and auctioned it.

Second, the rise of programmatic advertising in the late 2000s changed the game. Real-time bidding (RTB) replaced the older "waterfall" system. By the late 2010s, programmatic advertising was about 85% of all online ad revenues, and dependent on the collection, transfer, and analysis of personal data (user-generated, behavioural, social, locational, demographic, identifying. Every type Birch defined in Chapter 2).

Third, Google has built a dense, interlocking adtech ecosystem that touches every part of the supply chain. Google Ads (advertiser-side), Google Display & Video 360 (DSP), Google Ad Exchange (the exchange), Google Ad Manager (publisher-side ad server, formerly DoubleClick for Publishers, plus the SSP merged in 2018), and YouTube ad inventory (only accessible through DV360). It has 39% of *global* digital advertising market share. It collects personal data from over 50 consumer-facing services. In a 2011 Q1 earnings call, Google's executives explicitly call users "assets."

Fourth, and this is where parasitic innovation enters, Google designed each layer of this ecosystem to disadvantage outsiders. **Dynamic allocation (2009)** let Google's ad exchange bid in the waterfall on real-time data while competitors had to use historical performance, a structural information asymmetry. **Enhanced dynamic allocation (2014)** let Google's exchange jump ahead of even direct deals. Publishers responded with **header bidding (2015)**. Google responded with **exchange bidding (2018)**, which opened dynamic allocation to selected competitors but kept Google's privileged access to bidding data. **Project Bernanke**, alleged in the Texas state lawsuit, ran AdX as a second-price auction for advertisers but a third-price auction for publishers, and Google kept the difference. **The 2018 restriction on data-transfer files** stopped publishers from joining bid data with other Ad Manager data, claiming privacy reasons but in effect forcing publishers to use Google's own analytics and Ads Data Hub.

Fifth, the takeaway. Each of these "innovations" is parasitic. Designed to lock in publishers, lock out competitors, and exploit Google's information advantage rather than improve the ad-matching service. Together they explain how Google built and defends its enclave.

### 2.4.2 Tinder, HP printers, generative AI (small examples of parasitic innovation)

Tinder charges users 30–49 years old roughly 65% more than 18–29 year-olds for the same service, on average across six countries. It uses personal data to do this. HP designs printers that detect non-HP ink and refuse to work, charging extortionate prices for refills. Generative AI (ChatGPT, Bing Chat, Bard) is trained on massive scraped datasets including copyrighted material, with no consent from creators. Each is parasitic: each extends control over a resource through information asymmetry rather than building genuine value.

### 2.4.3 Amazon Kindle terms (Chapter 6, contractual control)

Amazon's "Buy now with 1-click" button doesn't actually let you buy an eBook. It grants you a non-exclusive license to view it on a specific device, for non-commercial use, subject to additional terms the content provider may impose. Amazon's own terms make this explicit: "Kindle Content is licensed, not sold, to you." Birch uses this to show the shift from ownership-based to contract-based control. The asset form depends on contractual rules, not property rights, which is why Big Tech can revoke access at any time.

### 2.4.4 Big Tech's balance-sheet anomaly (Chapter 3)

Birch and his colleagues looked at Big Tech corporations' asset bases. They expected to find personal data showing up as an intangible asset. They didn't. In fact, Big Tech corporations (Apple, Microsoft, Alphabet, Amazon, Meta) have a *lower* proportion of intangible assets than the average top-200 US corporation, and they have a *growing tangible* asset base (data centres, hardware, etc.). Personal data isn't on the balance sheet at all. It shows up obliquely as "users," "user base," "user engagement." This is what Birch means by the *accounting opacity* of data. It's clearly central to Big Tech's value, but it's nowhere in the financial reports, which is why the gap between book value and market capitalization for these firms is so large (sometimes 90%+).

## 2.5 How this applies to my case (Publikum / arthouse / IMDb)

Birch's framework lets me ask much sharper questions about our project than Xu et al. alone allows. Three concrete applications.

**Our IMDb data is not raw. It is *crafted*.** IMDb is itself an enclave. Every rating, every star count, every cast list is an artefact of IMDb's collection architecture: their submission rules, their deduplication policies, their voting weights (IMDb's weighted average is opaque), their audience self-selection (IMDb users are not a representative sample of cinemagoers, let alone of the European arthouse audience). When we report that a film has a 7.8 rating, we are not reporting truth about the film. We are reporting an artefact of IMDb's techcraft. This is exactly what Birch means when he says raw data is an oxymoron. The first methodological move I should make in the exam, if asked about data quality, is to name this. The IMDb dataset is shaped to serve IMDb's commercial interests (driving traffic, driving ad revenue), not to be a neutral record of cinema.

**Our enrichment chain is a stack of enclaves.** TMDb is a separate enclave with its own collection architecture and metric definitions. Popularity score on TMDb is computed differently from Box Office Mojo, which is differently again from IMDb's user-rating distribution. MovieLens is an academic dataset, but it's still an artefact of GroupLens's specific data-collection design. When we combine these and treat the combined dataset as a single object of analysis, we are doing exactly what Birch warns against: *treating cross-enclave data combination as if the resulting dataset is fungible, when it is in fact emergent*. The properties of the combined dataset (especially correlations between LLM scores, IMDb ratings, and country tags) are *emergent properties* in Birch's exact technical sense. Some of those emergent properties are genuine signal; some are artefacts of how the underlying enclaves disagree about what they're measuring.

**Publikum sits inside, and is dependent on, the very enclave economy Birch criticizes.** Their business model (selling audience-insight to streamers and producers) depends on access to enclave-controlled data: Netflix viewership, IMDb behavioural data, social media engagement. They don't *control* the underlying enclaves; they're tenants. This makes them an example of what Birch calls the small-business position in the platform economy. They survive by paying tribute to the enclave operators (paid API access, licensing fees, terms-of-service compliance) and by extracting marginal value from the access they're granted. An honest critical reading of Publikum's situation is that the data they want to leverage is mostly held by parties whose interests don't align with theirs. This is the kind of structural-political-economy point that a 12-grade answer would include.

**Arthouse is itself a constructed category.** When I score a film as arthouse using a hybrid rule (manual rule OR LLM ≥ 8), I am doing techcraft. I am defining a category that makes a population of films legible to Publikum's commercial purposes. The "arthouse film" of my dataset is not a pre-existing natural kind. It's an artefact of my measurement choices. The honest version of this, which I should be ready to say in the exam, goes like this: the arthouse cohort is a useful construct for Publikum's positioning question, and it's defensible (the rule and the LLM mostly agree, the cross-validation worked), but it's not a discovery of how films "really" partition. It's a tool for doing a specific kind of work. This is precisely the difference between Xu's tool-view and Birch's techcraft-view of the same activity. Both are right; Birch makes the politics visible.

## 2.6 Critical view of Birch

Birch is sharp, and the framework is genuinely powerful, but the book has weaknesses that an examiner might probe.

**First, the framing applies *much* better to Big Tech than to most organizations.** Birch's empirical work is on Alphabet, Meta, Apple, Amazon, Microsoft. Companies with billions of users and tens of billions in advertising revenue. The "enclave" concept stretches when applied to a mid-sized firm like Publikum. Yes, Publikum sits inside the enclave economy as a tenant, but it isn't running an enclave of its own. The political-economic critique is calibrated for a different scale than most of the cases the course actually deals with. In the exam, if I deploy Birch's vocabulary, I should be specific about which actors in my case are enclave operators and which are tenants.

**Second, the asset-vs-commodity distinction is sometimes overdrawn.** Birch insists data is not a commodity because it isn't fungible. But data brokers (Acxiom, Experian) very much do trade datasets as if they were commodities, and demand-side platforms in adtech treat data segments as priced goods that flow through markets. The picture is more mixed than Birch's clean dichotomy suggests. Xu et al.'s commodity quadrant captures something real, even if Birch is right that it doesn't capture *everything*. In the exam, the right answer is "they're both partially right." See §3.

**Third, Birch is light on what the alternative looks like.** Chapter 7 calls for data trusts, collective governance, accounting reforms, and stronger regulation (DMA, DSA, GDPR). These are good directions but the book is short on the operational details. How a data trust governs disagreements, how accounting standards for personal data would be drafted, what to do when public data infrastructures get captured by the same enclave logic. The constructive program is gestural. Not a fatal flaw (the diagnostic work is the book's main contribution), but an examiner pushing me on "okay, what should we *do*?" deserves a more grounded answer than Birch alone provides.

**Fourth, the techcraft / "raw data is an oxymoron" line is not original to Birch.** Gitelman & Jackson (2013) is the canonical source; Bowker & Star (1999) on classification systems is older still; Hoeyer's *Data Paradoxes* (2023) develops the same point in a different domain. Birch's contribution is the political-economy move (techcraft as a specific *commercial* practice in technoscientific capitalism), not the constructivist move itself. Worth knowing in the exam so that I can place Birch in a tradition rather than treat him as a singular author.

**Fifth, the book's tone is sometimes more polemical than analytic.** "Parasitic innovation" is a sharp term but it presupposes a clean line between "good" and "bad" innovation that Birch doesn't fully theorize. Some of HP's pricing tactics are obviously rent extraction; others are arguably legitimate vertical integration. Birch's own concept of rentiership is more rigorous (Birch & Cochrane 2022 on four forms of digital rentiership: enclave rents, expected-monopoly rents, engagement rents, reflexivity rents) but the book's headline language flattens it. The polemical edge sometimes does the analytical work that the careful concept should be doing. In the exam, I should reach for "rentiership" and "enclave" rather than "parasitic" if I want to sound rigorous.

**Sixth, the GDPR optimism may not survive empirical scrutiny.** Birch ends the book by celebrating the EU's regulatory turn (DMA, DSA, GDPR, the Bundeskartellamt case). It's been long enough since GDPR (2018) that we have evidence: enforcement has been slow, fines against Big Tech have been small relative to their revenues, and Big Tech has used regulatory complexity to entrench itself by absorbing compliance costs that smaller competitors can't. The DMA is too new to evaluate. Birch's conclusion that "we can find a way" may be more aspirational than the rest of his analysis warrants.

**Seventh, the book under-discusses the global South.** The data-enclave story Birch tells is a US/EU story. Indian, Chinese, African, and Latin American Big Tech firms (Tencent, Alibaba, Jio, Mercado Libre) have different political economies and different relationships to the state. The framework is not obviously portable.

## 2.7 Quotes worth knowing

> *"Raw data is an oxymoron."* — Gitelman & Jackson (2013), quoted by Birch (Chapter 2 epigraph)

The single line that sums up the constructivist starting point. Use it whenever an examiner says or implies that data is "just collected."

> *"Big Tech corporations have worked out the ways to control our personal data through the techno-economic configuration of the mass collection and hoarding of data in siloed enclaves."* (Chapter 5 introduction)

Birch's thesis statement. Worth being able to paraphrase: control without ownership, achieved through technical and contractual configuration, producing siloed enclaves rather than markets.

> *"Markets are not working anymore, or maybe they never did."* (Chapter 6 conclusion)

A quotable line that captures the death-of-markets argument. Useful for any answer about why competition policy has been ineffective against Big Tech, and any answer about why "free market" rhetoric in tech is self-defeating.

## 2.8 Likely examiner questions on Birch — with model answers

**Q1. What does Birch mean by a "data enclave," and how is it different from a "platform"?**

A platform, in the standard literature, is a piece of digital infrastructure that intermediates between two or more groups of users (Srnicek's definition). A data enclave is something more specific: a *walled-off* reservoir of personal data, controlled by Big Tech through technical interoperability limits and contractual terms-of-service. Where a platform mediates exchange, an enclave hoards and restricts. The enclave word is doing work that "platform" can't. It captures the political-economic fact that the space is privately governed by contract law rather than publicly regulated. Birch distinguishes enclaves from ecosystems too. An ecosystem is a heterogeneous assemblage of devices, users, and rules; an enclave is what an ecosystem becomes once the controlling firm restricts access to its core asset, the personal data it has aggregated.

**Q2. Birch says data is an asset, not a commodity. What's the distinction, and why does it matter?**

A commodity is fungible. One bushel of grain substitutes for another, and value comes through market exchange. An asset is unique, controlled rather than owned, and valuable because it produces future revenues without needing to be sold. Birch argues data is the second, not the first, because every dataset is an artefact of its specific collection architecture (techcraft). Two datasets purporting to measure the same behaviour aren't substitutes. The mechanism of control is contractual, not proprietary, because facts about people aren't legally ownable. This matters because asset logic is investment logic. Value is whatever investors expect future revenues to be, discounted to today. So Big Tech's market capitalization isn't about today's revenues; it's about the future revenue everyone expects them to extract from their data control. And it explains why competition policy struggles with Big Tech: the standard tools assume markets, and an enclave isn't a market.

**Q3. What is parasitic innovation, and can you give an example?**

Parasitic innovation is innovation deliberately designed to extract value rather than create it. To limit access to resources, undermine regulations, undermine competitors, exploit user psychology, or weaponize information asymmetries. Birch's central case is Google's adtech ecosystem. Google's "dynamic allocation" let its own ad exchange bid in real time on data competitors couldn't see. Project Bernanke ran the same auction as a second-price auction for advertisers and a third-price auction for publishers, with Google pocketing the difference. The 2018 data-transfer file restriction stopped publishers from joining bid data with their other Ad Manager data unless they used Google's own analytics. None of these "innovations" produced a better ad-matching service. They produced lock-in. That's the test for parasitic innovation: is the change in service quality the *consequence* or just the *cover*?

**Q4. Apply Birch's framework to your group's project. Does it work?**

Mostly, with caveats. Birch's framework is calibrated for Big Tech, and Publikum is not Big Tech. But several pieces map directly. The data we use is enclave-controlled. IMDb, TMDb, MovieLens are each their own collection architecture, their own techcraft. Our combined dataset has emergent properties that don't belong to any one source, in Birch's exact technical sense. Publikum sits in the tenant position relative to those enclaves. They pay for API access and license terms; they don't control the underlying data infrastructure. Most importantly, our arthouse cohort is itself a piece of techcraft. A category constructed to make a population of films legible to Publikum's commercial purposes. It's not a discovery of a natural kind; it's a tool. What Birch's framework lets me say, that Xu et al. doesn't, is that the *category* "arthouse film" is doing political work, not just analytical work. It's enrolling films into a marketing logic in the same way Big Tech enrols users into an advertising logic, just at a much smaller scale.

**Q5. What's wrong with Birch's argument?**

A few things. First, the framework is calibrated for Big Tech and stretches when applied to mid-size organizations like Publikum. Second, the asset-vs-commodity dichotomy is overdrawn. Data brokers really do trade data segments as commodities, even if data isn't *purely* a commodity. Third, the book is light on the operational alternatives. Data trusts and collective governance are floated but not detailed. Fourth, the constructivist starting point ("raw data is an oxymoron") isn't original to Birch. Gitelman & Jackson, Bowker & Star, Hoeyer all develop it; Birch's contribution is the political-economy move, not the constructivist insight itself. Fifth, the regulatory optimism (GDPR, DMA, DSA) may not survive empirical scrutiny. Enforcement has been slow and Big Tech has used compliance costs to entrench itself. Sixth, the framing under-discusses Big Tech outside the US/EU. None of these are fatal. The diagnostic work is genuinely powerful. But they're places an examiner can press.

---

# §3. Connecting Xu and Birch

The two readings sit on opposite sides of the same problem, and the most interesting move for the exam is to put them in dialogue rather than treat them as alternatives. They agree on more than first meets the eye. They disagree in ways that are illuminating. And taken together they give a much richer account of "data value in organizations" than either does alone.

**Where they agree.** Both readings reject the naive "data is a strategic resource" framing that dominated the 2000s and 2010s. Both insist that the value of data depends on the configuration around it. For Xu et al., the purpose of use; for Birch, the techno-economic architecture of collection. Both say data has *emergent and reflexive properties*. Xu et al. note the data network effect (Hagiu & Wright 2020) where data gets more valuable as more of it is combined, and Birch makes this central with his discussion of relational data (Viljoen 2020) and the gaming dynamics of reflexive data. Both note that data is hard to fit into existing accounting categories. Xu et al. observe that intangible-asset accounting struggles with data, and Birch builds a whole chapter around the fact that personal data isn't on Big Tech's balance sheets despite being central to their value. And both writers have moved past the notion that the data-information-knowledge-wisdom (DIKW) pyramid usefully describes how data creates value. Xu et al. see DIKW as a one-role-only model fitted to the tool view, and Birch treats DIKW as a category that obscures the political work of techcraft.

**Where they tension, round 1: on commodity status.** Xu et al. are comfortable calling data a commodity in the trading context. Birch refuses the word and insists data is an asset. This isn't pedantic. The *commodity* framing makes data look like grain. Fungible, market-priced, legibly traded. The *asset* framing makes data look like a private utility. Capitalizable, controlled by contract, valued by investor expectation rather than market clearing. The implications for policy diverge. If data is a commodity, the fix is more efficient markets (privacy markets, personal-data markets, data exchanges); if data is an asset, the fix is governance reform (data trusts, accounting standards, ex-ante regulation like the DMA). For my exam answer, the right move is *both*. Data brokers really do trade data segments in something like a commodity market, but the bulk of valuable personal data sits in enclaves where Birch's asset framing is more accurate. The two writers are looking at different ends of the same elephant.

**Where they tension, round 2: on the role of organization.** Xu et al.'s "data as a practice" quadrant is the most interesting one for thinking about competitive advantage. Value comes from organizational learning embedded in routines, not from any feature of the data itself. Birch's framework barely addresses this. The closest he comes is the discussion of "boundary assets" and how Big Tech enrols other businesses into its ecosystem. But Birch is interested in the *political* configuration; Xu et al. are interested in the *organizational* configuration. They're both right and they're both leaving the other dimension under-theorized. A good answer in the exam would say: Xu et al. tells me what kind of capability I need to build inside my organization to extract value from data; Birch tells me what kind of *power* I'm up against from the enclave operators whose data infrastructure I depend on. I need both.

**Where they tension, round 3: on AI.** Xu et al.'s "data as algorithmic intelligence" is treated relatively neutrally. A value-creation pathway with some risks (inscrutability, ethics) that need to be managed. Birch is more sceptical. His argument is that AI is just the latest layer of enclave consolidation. Training data is hoarded, model APIs are monetized, and the inscrutability is a feature for the enclave operator (they can claim "the model decided" while keeping the rules opaque). The dystopia in Birch's chapter on Google's adtech is exactly the pattern he expects to see in AI more generally. I find Birch's reading more honest, but Xu et al.'s reading is more practically useful for the firm-level "should we invest in AI" question. The exam answer is to deploy both. Xu gives me the capabilities checklist, Birch gives me the political risk-register.

**Where they tension, round 4: on the framing of value.** Xu et al. assume data value is something organizations capture for themselves through the right configuration. Birch insists data value is something that accrues *to whoever controls the enclave*, which, by definition, isn't the people whose data fed it. Xu et al. are implicitly writing for managers; Birch is explicitly writing for citizens, regulators, and policy-makers. This is why the two readings feel different even when they agree on the facts. They're calibrated for different audiences. For an exam answer about Publikum, I should remember that Publikum is a *manager* of small-scale data work (so Xu et al.'s framing is mostly the right one operationally) but also a *tenant* in larger enclaves (so Birch's framing matters for understanding their dependencies and limits).

**What they together let me say.** Put them in conversation and I get the answer to the seminar's central question, *what is the value of data in organizations?*, that neither alone supports. Data has multiple *functional* roles in any organization (Xu's typology), and each role has a corresponding *political-economic* configuration of who controls what (Birch). The four roles map roughly but not perfectly onto Birch's framework. Data-as-tool tends to be local-scale and politically uncontentious. Data-as-commodity is where Birch's "data is not a commodity" critique bites hardest. Data-as-practice is what builds organizational competitive advantage but also what the enclave operators have already monopolized. Data-as-algorithmic-intelligence is the new frontier where the political-economic dynamic Birch describes is being played out at AI scale. To assess the value of data in any specific organization, I need to ask both: *what role(s) is data playing here, and what's the configuration of control around it?* That's the integrated answer the course wants.

---

# §4. Likely cross-reading examiner questions — with model answers

**CQ1. Is data a commodity? Use Xu et al. and Birch to give a reasoned answer.**

It depends what you mean. Xu et al. identify *data as a commodity* as one of four roles. Data is a commodity when it's traded between organizations for revenue, as in data marketplaces and broker services. They cite the non-rivalry of data (Jones & Tonetti 2020) and the tradability of "data tokens." So in their framework, yes, data is sometimes a commodity. Birch flatly disagrees. He argues data fails the basic test for commodity status because it isn't fungible. Every dataset is an artefact of its collection architecture (techcraft), so two datasets aren't substitutes. He argues data is better understood as an asset: capitalizable property, controlled by contract rather than property right, valued by discounted expected future revenues rather than market clearing. My honest reading is that both are partly right. Data brokers like Acxiom and Experian really do trade data segments in markets that look like commodity markets, at the level of priced records being bought and sold. But the *core* personal-data assets of Big Tech sit in enclaves that aren't traded at all, and Birch's framework describes them better. So the answer is: data is sometimes a commodity, especially in the broker layer; but the most valuable data isn't, and treating it as one obscures the real political economy. For a project like Publikum's, the data we license in (TMDb, IMDb) sits in the commodity-trading layer; the data Publikum *would like* to access (streamer viewership, social media engagement) sits in enclaves they can't reach.

**CQ2. Apply both readings to your group's work for Publikum. What does each let you see that the other doesn't?**

Xu et al. lets me describe *what we do*. Our notebook work is mostly data-as-tool (informing decisions about positioning), the hybrid arthouse rule is a small instance of data-as-practice (a repeatable methodology), the LLM scoring is a touch of data-as-algorithmic-intelligence (autonomous scoring with the inscrutability that comes with it), and Publikum's business model lives in data-as-commodity (selling insight as a product). Without Xu, I wouldn't have a clean vocabulary for these distinctions. Birch lets me describe *what we don't control*. The IMDb dataset is enclave-shaped (techcraft optimized for IMDb's commercial purposes, not for being a neutral record of cinema); our combined dataset has emergent properties that don't belong to any source; Publikum is a tenant in enclaves they can't change; the arthouse cohort I built is itself a piece of techcraft, useful but not a discovery of a natural kind. Without Birch, I would underestimate how much of the "data quality" question is actually about whose interests shaped the data in the first place. Together: Xu gives me the operational view of what to do with the data we have; Birch gives me the political view of where that data came from and what it costs.

**CQ3. Both readings discuss data value. Whose account is more useful for an analyst working in industry?**

Xu et al. is more *operationally* useful. It gives me a checklist for thinking about which capabilities my organization needs to develop in order to extract value from data, and it lets me ask precise questions like "is this project a tool-view or a practice-view problem, and have we resourced it accordingly?" For a working analyst making decisions inside an existing organization, that's the more actionable framework. But Birch is more *strategically* useful. It tells me which dependencies I'm locked into, where the political risk is, and which competitive moats are real (organizational practice) versus illusory (data hoarding by parties more powerful than me). For a senior decision-maker thinking about long-term strategy, Birch is the framework that names the structural constraints. The honest answer is that you need both, and that they answer different questions. Xu tells me what to do; Birch tells me why it might not be enough. An organization that uses only Xu will build technically capable data teams that get out-competed by enclave operators who never appear in the analysis. An organization that uses only Birch will spend its time analyzing structural injustice while its competitors ship product. The exam-12 answer holds them in tension.

**CQ4. How does each reading help you criticize the way our pitch deck framed data value?**

The presentation we did for the case was framed around datafication and exploratory data viz. The implicit story was "data lets us see audiences clearly." Xu et al. lets me push back on that gently. Which *role* of data are we leveraging? Mostly the tool role, with some practice and some algorithmic intelligence. The pitch implicitly oversold what tool-view data can do. Improving Publikum's *decisions* about positioning, but not building a sustainable competitive advantage on its own. The advantage would come from data-as-practice (repeatable methodology) and data-as-commodity (Publikum's offer to its customers), and we under-discussed those. Birch lets me push back harder. The pitch's "data lets us see audiences clearly" is exactly the techcraft fantasy Birch warns against. We don't see audiences. We see the artefacts of IMDb's techcraft layered with TMDb's techcraft layered with MovieLens's techcraft. The audiences we describe are constructed populations made legible to Publikum's business purposes. That doesn't make them useless (constructed categories are tools), but it means we should not pretend the data is a neutral mirror. The honest version of the pitch would name this. In the individual oral, naming this without prompting is exactly the kind of move that signals critical reflection.

**CQ5. Suppose you're advising Publikum on how to build data-driven competitive advantage. What does each reading tell you?**

Xu et al. tells me: don't lean on data-as-tool alone, because tool-view value is generic. Every consultancy does it, no moat. The competitive advantage comes from data-as-practice. Building repeatable methodologies (like the arthouse cohort definition) that accumulate across projects, embedding tagging conventions, building the data network effect (the more clients we serve, the better our priors get for the next client). Investing in tooling (notebooks, dashboards) is necessary but not sufficient. The practice has to be real and the team has to keep doing it. Birch tells me: be honest about what you don't control. Publikum will never beat Netflix's recommendation engine on Netflix's home turf. The path to defensibility is not to compete on raw data volume (Publikum can't) but to compete on *interpretive judgment that the enclave operators don't have access to*. Anthropological insight into European arthouse audiences is exactly the kind of thing Big Tech can't easily replicate. It requires craft knowledge, regional networks, language fluency, and trust relationships with creators. That's the right competitive position. So combined: invest in practice (Xu); position in the territory where the enclave operators are weakest (Birch). The combination yields a more defensible strategy than either reading alone produces.

---

*End of week 03 reading notes.*
