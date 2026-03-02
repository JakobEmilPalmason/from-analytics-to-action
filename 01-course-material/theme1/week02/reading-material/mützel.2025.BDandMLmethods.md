<!-- Page 1 -->

Big Data and Machine Learning Methods
Sophie Mu¨tzel
Contents
1
Introduction ...................................................................................
2
2
Innovation .....................................................................................
2
3
New and Old Large-Scale Data ..............................................................
4
4
Methods of Data Analysis ....................................................................
5
4.1
Topic Modeling .........................................................................
6
4.2
Word Embeddings ......................................................................
8
4.3
Outlook and Trends: Contextual Embeddings and Generative Large Language
Models ..................................................................................
9
5
Conclusion ....................................................................................
11
References ........................................................................................
12
Abstract
This chapter delineates big data and machine learning (ML) methods in innova-
tion research. Large-scale data and computational methods are currently being
used to advance innovation research on sources and processes. The chapter
covers three oft-used computational methods: topic modeling for identifying
latent themes, word embeddings for assessing semantic linkages, and generative
large language models for text annotation and coding. Combined with large-scale
data sets, these methods allow for nuanced and systematic analysis of innovation
processes. The chapter also addresses the limitations of employing big data and
ML methods in empirical studies, such as data quality and ethical considerations.
It emphasizes the importance of human expertise and the potential of ML to aid as
research assistants and interlocutors in social science innovation research.
Keywords
Big data · Innovation · Topic modeling · Word embedding · LLMs · Data quality
S. Mützel (✉)
University of Lucerne, Lucerne, Switzerland
© Springer Nature Switzerland AG 2025
I. Schulz-Schaeffer et al. (eds.), Handbook of Innovation,
https://doi.org/10.1007/978-3-031-25143-6_56-1
1

---

<!-- Page 2 -->

2
S. Mu¨tzel
1
Introduction
This chapter addresses the evolving landscape of innovation studies, driven by the
increasing availability of big data and the application of machine learning
(ML) methods. The emergence of large-scale digitized and “born-digital” data
sources has opened new avenues for examining enduring questions in innovation
studies, such as how newness emerges. This abundance of textual data, alongside
advancements in computational analysis, allows researchers to study innovation
processes with unprecedented breadth and depth. Foundational principles of inno-
vation, such as recombination of existing elements, the temporal unfolding of ideas,
processes of recognition, the interpretation of newness by diverse actors, and the
categorization of new concepts, are now being investigated using computational
tools. This shift enables a more nuanced understanding of the complexities inherent
in innovation processes, which are often nonlinear and involve uncertainties and
diverse interpretations.
First, the chapter introduces its notions of innovation and discusses challenges
and advantages of old and new types of large-scale data. It proceeds to focus on the
application of speciﬁc computational methods to the study of innovation: it intro-
duces and discusses topic modeling, word embeddings, and generative language
models as key analytical tools that leverage big data to provide new insights into
innovation processes. These methods offer distinct approaches to analyzing large
textual corpora, ranging from identifying latent thematic structures to mapping
semantic relationships, and even generating text that mimics “understanding.” By
exploring the capabilities and limitations of these methods, this chapter is aimed at
delineating how they contribute to and transform the study of innovation.
2
Innovation
Research on innovation studies innovative breakthroughs as they are the foundation
for change in scientiﬁc and technological ideas, and potential increases in social and
economic value. The focus of innovation research includes the sources and the
effects of such breakthroughs. Research also addresses how organizations can
innovate and, for example, change their business models.
This chapter focuses on the study of sources of innovation, for which research has
identiﬁed several foundational principles and mechanisms. Innovations are based on
some sort of recombination of actors, objects, or knowledge; new ideas emerge over
time, and novel ideas must be recognized (for an overview see, for example, Cattani
et al. 2023).
New actors, organizational forms, and objects, collectively referred to as new-
ness, do not arise spontaneously. Instead, newness results “from combinations and
permutations of what was there before. Transformations are what make them novel”
(Padgett and Powell 2012, p. 2). Structurally, innovations emerge from the recom-
bination of people, practices, and relations across multiple social network domains
and “improve on existing ways of doing things” (Padgett and Powell 2012, p. 5) or

---

<!-- Page 3 -->

even “change the ways things are done” (Padgett and Powell 2012, p. 5). Cogni-
tively, recombination of different kinds of knowledge—deep, local, and bridging—
is necessary to create breakthroughs (de Vaan et al. 2015).
Big Data and Machine Learning Methods
3
Other works in organizational studies have picked up on the complexities of
innovation processes as journeys over time and organizational spaces (e.g., Garud
et al. 2015). These studies examine innovation processes by observing the sequences
of events that unfold over time, “events that unfold as ideas emerge, are developed,
and are implemented within ﬁrms, across multi-party networks and within commu-
nities” (Garud et al. 2013, p. 776). Innovation processes are often not linear and may
entail failures, so an empirical perspective over time as the process evolves is
necessary.
Research also shows that to cope with uncertainties in innovation processes,
interpretations of diverse sets of actors are involved. For example, in the history
of biotechnology, entrepreneurs contested interpretations of “what biotechnology
meant at any one point” (Kaplan and Murray 2010, p. 108) and constructed different
economic logics of the ﬁeld in which they operated. Similarly, industry analysts
contested what a new breast cancer treatment was a case of (Mützel 2022).
The concept of “reﬂexive cognition” (Stark 2009, p. 4) analytically breaks down
such interpretive processes, in which actors collaboratively create meaning, into
three moments. First, actors must be able to recognize and identify something, such
as a new product or practice, by making previously uncommon associations across
various networks or knowledge domains. Second, the new thing requires a label and
a category to belong to, and to which others may attach their interpretation and
meaning. And third, others need to be convinced of the new thing so that they can
value and support it and its categorization.
Categories seemingly reduce the cognitive complexities of social reality and
provide a “conceptual system” (Rosa et al. 1999). Meaningful categories only
stick over time when a ﬁrst label is adopted and used by different actors (Grodal
et al. 2015). Labels may stem from attempts to self-categorize (e.g., Vergne 2012),
although such labeling is often contested (e.g., Slavich et al. 2020) as it needs to
resonate with audiences or other intermediaries. Moreover, labels may serve as
supportive vocabularies in communicating a new category (e.g., Hsu and Grodal
2021). In particular, new combinations of words and concepts help to signal a new
category while also allowing for common ground to understand the meaning of that
new category.
To coordinate amid uncertainty and ambiguity, actors use stories to temporarily
settle on categories about what the situation is about. “Category emergence” and
“category creation” are two possible avenues through which category formation can
take place (Durand and Khaire 2017). In the process of “category creation,” actors—
in mostly cognitive moves—redeﬁne and reinterpret preexisting attributes and
features to elaborate how a new category is different from and normatively superior
to an existing category (e.g., Rao et al. 2003). Instead, processes of “category
emergence” involve labeling after a material innovation has been identiﬁed by actors
involved in the market. In category emergence, the category acquires its legitimacy
through the explication of the meaning of the category—most notably from third-

---

<!-- Page 4 -->

party intermediaries in discursive contestations (e.g., Grodal and Kahl 2017; Mützel
2022).
4
S. Mu¨tzel
These principles of recombination, processes over time, cognition and interpre-
tation, and processes of categorization and institutional logics are expressed in
stories on innovations.
3
New and Old Large-Scale Data
As this brief review of innovation research has shown, actors involved in innovative
processes talk and dispute over meaning and interpretation, leave written traces of
such meaning-making processes, e.g., in meeting minutes and other documents, and
can be observed and interviewed about how innovative breakthroughs failed or came
about. Involved actors ﬁle patents, publish academic papers, and third-party
observers and analysts produce special reports and articles on how to evaluate the
claimed innovative breakthroughs. Accordingly, studies of innovation processes
have employed various qualitative research methods to gather data on how novel
ideas emerge, including ethnographic ﬁeldwork, interviews, and document analysis.
For instance, patent data have long been used to study the recombination of ideas
and their potential economic value using citation counts to patents (e.g., Griliches
1990). Researchers have followed innovation journeys over time based on ethno-
graphic ﬁeld work, interviews, and document analysis (e.g., Van de Ven et al. 1999).
Over the past two decades, libraries and archives have digitized old textual data
sources, e.g., newspapers, organizational documents, and new “born-digital” data
sources, e.g., online social media platforms, webpages, and digital-only text
archives, have appeared (e.g., Gregoire et al. 2024). Characteristically, such data
are large in size, unstructured, diverse—they include, for example, texts, images,
administrative data, transactional data—and about an array of phenomena. Both old
and new types of textual data have increased the variety and breadth of data sources
used to study innovation processes—and they both come with caveats.
Trace data sourced from social networking sites have their own advantages and
challenges. Such big data on communications are exciting for research because,
contrary to scarce and expensive data sources of surveys and interviews, they are
large, always on, and nonreactive. However, they are collected and further used by
social media platforms for their proﬁts (e.g., Zuboff 2019). Research must carefully
consider the repurposing of such data, especially since they are incomplete and
algorithmically confounded (Salganik 2017). Moreover, access to proprietary data
from social media platforms is limited; indeed, at the time of writing, most social
media platforms cannot or can no longer be accessed or web scraped for research.
Moreover, both digitized and digital data need further processing and curation
before they can be analyzed. The transformation from analog documents to machine-
readable text data takes several steps. It includes computer-assisted digitalization
using algorithms such as optical character recognition or manual digitalization,
transcribing the source material. The resulting machine-readable documents are
rarely ready to use but must be further processed and curated as they may contain

---

<!-- Page 5 -->

errors or superﬂuous information. Whereas collections of digital text data allow for
swift downloads of machine-readable ﬁles, they too need further curation and
processing, such as nontextual information.
Big Data and Machine Learning Methods
5
The growing literature on data quality (e.g., Hurtado Bodell et al. 2022) and
pre-processing of unstructured, textual data (e.g., Hickman et al. 2022) points to the
many consequential decisions during data curation that affect later data analyses and
the validity of insights. Additionally, the selection of datasets on which algorithmic
procedures are trained proves consequential as they may propagate unwanted yet
encoded societal biases, stereotypical associations, and negative sentiment toward
speciﬁc groups. To mitigate such effects and to increase transparency and account-
ability, researchers in academia and industry have emphasized the need to document
the characteristics of datasets used in training and analyses (e.g., Whittaker et al.
2018). They suggest providing each dataset with information on its motivation,
composition, collection process, and recommended uses (e.g., Gebru et al. 2021).
4
Methods of Data Analysis
Before looking in detail at current methods, it is helpful to brieﬂy point to earlier
methods of textual, network, and other relational analyses, as texts as data have long
been used for social inquiries. For instance, using dictionaries and coding schemes,
researchers have used content analysis to systematically ﬁnd and measure speciﬁc
constructs of interest (Krippendorff 2012). Word counts and frequency analysis in a
given corpus have been used to describe and quantify “the manifest content of
communication” (Berelson 1952, p. 18). Co-word analyses have helped to describe
ﬁelds of knowledge (Callon et al. 1991).
Others have long been interested in identifying latent patterns in how individuals,
groups, organizations, or ﬁelds make meaning. Many have studied discourses and
narratives using qualitative analyses to trace meaning-making processes. Other
research has employed formal methods that can capture the relationality of actors,
events, objects, or terms, including network analysis, correspondence analysis, and
Galois lattices, to detect how meaning is made. Such research has utilized various
data types, including newspaper reports, directories, observations, and interviews.
Studies of innovation have been particularly interested in identifying latent
patterns in texts of how innovative breakthroughs or novelty emerge. Research has
used keywords, co-word analyses of keywords, and network analyses. For example,
Sarah Kaplan et al. (2003) use word counts from letters to shareholders to measure
ﬁrms’ innovativeness. Mark Kennedy (2005) analyzes the co-mentioning of com-
pany names in newspaper data to analyze rivalries in the emerging market of
computer workstations. Andrei Mogoutov et al. (2008) use a combination of publi-
cations, US patents, and abstracts of funded research projects to study the emergence
of biomedical innovations. Using natural language processing (NLP), they extract
semantically meaningful multi-term keywords from texts and plot their relations in
semantic network analyses. Candace Jones et al. (2016) use network analysis of

---

<!-- Page 6 -->

actors’ vocabulary to identify their institutional logics and how these logics shaped
the creation of a new category called modern architecture.
6
S. Mu¨tzel
The availability of large-scale digitized or digital data promises research to study
processes with all their complexities and nuances over longer periods of time.
Instead of scarce and expensively collected data points, digitized and digital data
are now abundant. Instead of drawing samples, researchers can now work with “all
the data” and obtain large-scale perspectives of the social.
No longer small or sampled, such large-scale data demand new methods of
analysis. Research has pointed out that we are at “a watershed moment” (McFarland
et al. 2016): The combination of available large-scale digitized corpora as well as
novel tools from ﬁelds such as NLP and ML have elevated computational text
analysis in empirical studies of the social world (for overviews, see, for example,
Evans and Aceves 2016; Kobayashi et al. 2018; Borch and Pardo-Guerra 2025).
Computational tools allow formally modeled insights into numerous social phenom-
ena, events, situations, and relations by analyzing vast amounts of digitized text data.
The interdisciplinary ﬁeld of computational social science (e.g., Edelmann et al.
2020) has paved the way in how to combine powerful computation with careful
social science and to propel automated text analysis (e.g., Grimmer et al. 2022).
The following sections introduce the current state of computational methods used
on large-scale data sets in the study of innovation and discuss pertinent examples.
Focus is placed on topic modeling, word embeddings, and generative language
models. In this order, the methods also address the shift from models based on
pattern recognition to those that can generate texts.
4.1
Topic Modeling
One of the methods that studies of innovation have used over the past decade is the
unsupervised ML approach of topic modeling based on Latent Dirichlet Allocation,
or LDA (e.g., Blei et al. 2003). Topic modeling yields groups of words that
frequently co-occur and collectively represent themes or latent topics. This is
based on a statistical model of language—that is, on a probabilistic model of how
words are distributed in a corpus, which does not require a priori dictionaries or
coding guidelines. Another advantage over hand-coding, frequency counts, and
keyword analyses is that individual words may appear in different topics, reﬂecting
their use in different contexts and various meanings. The amount of human involve-
ment in topic modeling algorithms is minimal: researchers must tell the algorithm
how many topics to ﬁnd in the corpus; the algorithm then produces that number of
topics, the words that make up each topic, and the distribution of those topics across
the entire corpus.
The unsupervised method of topic modeling follows an inductive logic; it detects
patterns in texts for explorative analyses—the idea is “to identify a number of
substantively meaningful and analytically useful topics” (DiMaggio et al. 2013,
p. 583). Fittingly, topic modeling has been likened to grounded theory approaches
(Baumer et al. 2017), which identify themes based on close readings. Identiﬁed

---

<!-- Page 7 -->

topics present “the lens through which one can see the data more clearly” (DiMaggio
et al. 2013, p. 582), whereas contextual knowledge is needed to interpret the patterns.
Big Data and Machine Learning Methods
7
Several reviews and instructive discussions have introduced organizational
scholars to the unsupervised ML method of topic modeling (e.g., Hannigan et al.
2019; Goldenstein and Poschmann 2019; Schmiedel et al. 2019). Sarah Kaplan and
Keyvan Vakili (2015) make a compelling case for topic modeling as “a fruitful
approach to measuring interpretations in the emergence of a new technological ﬁeld”
(p. 1441). They use topic modeling to measure the novelty of ideas as expressed in
patents (“topic-originating patents”). Working with a large corpus of abstracts of US
patents on nanotubes, they show the intricate relation of how innovative break-
throughs can but do not have to yield economic value. David Antons and Christoph
Breidbach (2018) analyze the topical landscape in service innovation and service
design based on scientiﬁc journal articles. Using topic modeling to identify topics of
research, they map the connections between topics based on their level of distribu-
tion in articles as a topic network. Antons et al. (2019) use topic modeling together
with rhetorical measures to study how the thematic substance and argumentative
style of scientiﬁc articles impact their future use.
Another strand of research on innovation using topic modeling focuses on
cultural dynamics, including categories, institutional logics, and styles. Analyzing
restaurant reviews, Sophie Mützel (2015) shows the emergence and diminishing of
culinary styles. Harsh Jha and Christine Beckman (2017) analyze the emergence of
new organizational forms based on a corpus of charter school founding applications
using topic modeling to show frames, organizational identities, and institutional
logics. Richard Haans (2019) shows how distinctiveness affects performance and
uses data from company websites to identify topics on how companies present
themselves. Karl Taeuscher et al. (2021) also address the distinctiveness of entre-
preneurial stories and market categories on a dataset of crowdfunding campaigns. In
a study of the emergence of new breast cancer therapeutics, Mützel (2022) traces
how science, industry analysts, companies, and journalists discuss and evaluate
ﬁndings and failures of molecules and research strategies as topics. The analyses
show the emergence of a new category (“targeted therapeutics”) across the studied
domains. Jessica Santana and Seonghoon Kim (2025) show how contested values
shift and converge in codes of ethics in semantic network analysis and topic
modeling.
Over the last decade, after the initial excitement, research has identiﬁed several
problems with such unsupervised approaches. In general, unsupervised learning
tools are data driven. This is useful for exploring a corpus, yet these tools cannot
identify a priori speciﬁed theoretical concepts. Topic modeling is based on a
statistical estimation of language and may not yield semantically meaningful topics.
Indeed, as a generative model, it remains a black box with occasionally cryptic
output. Moreover, topic models treat each document as a “bag of words,” thus
disregarding the syntax, grammar, or order of words within the document. Instead
of statistical validity, research relies on semantic (are the topics produced semanti-
cally meaningful?) and external validity (do the topics and their distribution reﬂect
external relevant events?). Overall, the unsupervised ML method of topic modeling

---

<!-- Page 8 -->

requires researchers to cope with “interpretive uncertainty” (DiMaggio 2015, p. 2).
(Semi-supervised extensions of LDA, such as structural topic models (Roberts et al.
2019) and seeded topic models (Hurtado Bodell et al. 2024), have been developed to
work with both the exploratory possibilities and the elements of focus of topic
modeling.)
8
S. Mu¨tzel
Laura Nelson et al. (2021) compare hand-coded, dictionary, off-the-shelf, super-
vised ML, and unsupervised topic modeling tools used to identify inequality in a
corpus of articles. They ﬁnd that topic models can complement traditional
approaches to coding complex and multifaceted sociological concepts. However,
they cannot fully replace traditional, labor-intensive approaches. The combination of
widespread interest in topic models and their limitations paved the way for the
adoption of other ML approaches.
4.2
Word Embeddings
Developed in the 2010s, word-embedding models (e.g., Word2Vec, Mikolov et al.
2013) are tools for reducing the dimensionality of text and extract numeric repre-
sentations of concepts. Word-embedding models are unsupervised ML algorithms.
They can be derived from any corpus and use a pretrained or a custom-trained
model. Word embeddings create a vector representation of every word in a given
corpus: they calculate the proximity and distance between terms and identify
associations between these words and speciﬁc concepts. The idea is that the concept
or meaning a word represents can be deduced by the distribution of words that
surround it. The resulting semantic space thus synthesizes relationships between
words, captures those relationships, and allows for various operations on words or
concepts. Social science research views these spaces as “conceptual spaces” that are
multidimensional and “within which concepts ranging from norms and knowledge to
ideas and inventions relate to one another” (Aceves and Evans 2024, p. 789) and
refers to word-embedding models as “a means of mapping meaning space” (Stoltz
and Taylor 2021, p. 2).
To be sure, word embeddings reﬂect stereotypical racial, ethnic, and gender
biases present in the texts on which they are trained (e.g., Caliskan et al. 2017).
Some studies attempt to “de-bias” word embeddings (e.g., Bolukbasi et al. 2016),
whereas others use these associations of biases to reﬂect the contours of cultural
formations and trace changes in meaning over time (e.g., Nelson 2021).
Studies of innovation use word embeddings because of their capacity to efﬁ-
ciently extract words from a corpus that are semantically related. Jaewoo Jung et al.
(2024) use word embeddings in conjunction with additional text analytic tools, ﬁrst
to extract terms and then topics from the letters of CEOs to shareholders to better
understand what the notion “innovation” entails. Katharina Lix et al. (2022) evaluate
the discursive breadth of team members working on different stages of software
projects. The study tracks the variety of conceptual engagement at every stage of the
project, demonstrating that high-performing teams can adjust their thinking to
shifting tasks; these teams also exhibit a wider discursive breadth when generating

---

<!-- Page 9 -->

new ideas and a narrower breadth when transitioning to tasks that call for coordina-
tion. The research suggests that alternative text analytic methodologies would have
found it challenging to capture such a nuanced concept of knowledge engagement.
In a different setting, Bas Hofstra et al. (2020) analyze the innovativeness of
scientiﬁc ideas. Using word embeddings from over one million dissertation
abstracts, this study estimates the semantic location of concepts in a vast network
of interrelated concepts and compares how newer concepts are positioned with
regard to one another in that space.
Big Data and Machine Learning Methods
9
Pedro Aceves and James Evans (2024) provide an instructive roadmap, an
empirical example based on patent abstract data, and a systematic literature review
on word-embedding models. Word embeddings are particularly interesting to
scholars of innovation because they address the emergence of categories: “Catego-
ries are groups of entities with shared characteristics and attributes. As noted
previously, concepts are the mental representations of categories” (p. 791). They
show that word embeddings can “measure similarity within the conceptual space that
existed at the time the patent was published” and contend that the theoretical notion
and empirical application of conceptual space “has the potential to spur new
theoretical developments and sharpen established theories” (p. 804).
Yet, like other text analytic methods, word embeddings have limitations
(Rodriguez and Spirling 2022). The results of word embeddings may be inaccurate
and, like other unsupervised methods, provide users with little control over what
they study. Word embeddings cannot consider negation, polysemy of terms, syntax,
or word order.
4.3
Outlook and Trends: Contextual Embeddings and Generative
Large Language Models
A recent advancement in word-embedding models consists of contextual embed-
dings that rely on more complex, deep learning algorithms. They are built on
transformer models (Vaswani et al. 2017) and trained on millions of words and
thus part of the family of large language models (LLMs). Prominent transformer
models are bi-directional encoder representations from transformers (BERTs) and
generative pre-trained transformers (GPT). Both differ in their architectures, in how
they speciﬁcally process and generate language, and how they are used in research.
Because of their bidirectional architecture, BERT models (Devlin et al. 2019) take
into account the context of each occurrence of a word. Whereas previously men-
tioned embedding models are able to learn similar representations for the words that
appear more frequently close to each other in a corpus and thus can assign seman-
tically similar words a similar space, they are unable to capture the meaning of words
in different contexts—e.g., “bank” may mean different things in different contexts.
BERT can now capture the contextual variation of each word based on the sentence,
paragraph, or document. This increases BERT’s ability to generate language based
on context by suggesting meaningful strings of words and sentences. BERT is
publicly available, allowing users to train the neural network on new data and in

---

<!-- Page 10 -->

various languages. BERT models are trained on an extensive breadth of data, and
users can plug in their data sets for analysis. BERT models are pretrained for various
tasks, including text classiﬁcation and sequence labeling. Moreover, BERT models
can be ﬁne-tuned for a particular task.
10
S. Mu¨tzel
Research shows that trained BERT models are valuable tools for social science
research: Salomé Do et al. (2022) show how the use of BERT models can help
researchers in coding procedures, thus augmenting their capabilities. Moreover, ﬁne-
tuned BERT models can identify rhetorical styles (Bonikowski et al. 2022) and
detect hate speech (Davidson 2025).
Studies in innovation research, including research on patents and categories, have
also used BERT. Milan Miric et al. (2023) compare different text analytical
approaches, including word embeddings and BERT, to identify patterns in US
patents on artiﬁcial intelligence. Analyzing the “stickiness of category labels,”
Balázs Kovács et al. (2024) study genres based on books’ synopses as found on
the website goodreads.com. Using a BERT model and human labelers, they show
constraints on category positioning in a market: label expectations stick from a prior
to a next book publication, which may lead to label mismatches.
One extension of BERT models is BERTopic (Grootendorst 2022). This method
combines sentence embeddings using BERT with a clustering of documents and
yields a representation of topics. BERTopics presents topics as a distribution of
words. This allows modeling of dynamic and evolutionary aspects of topics. To
systematically review and sort the existing literature in the ﬁeld of early innovation
search that uses NLP approaches, Julian Just et al. (2024) run BERTopic. The
analysis ﬁnds 18 distinctive innovation practices, such as “patent mapping” or
“attribute recombination,” based on textual analysis methods, such as topic model-
ing or text embeddings. Just et al. (2024) also use BERTopic to sort the results of a
crowdsourced idea contest and to ﬁnd patterns.
Generative language models of the GPT family of models (Ouyang et al. 2022)
are also trained on vast corpora of texts and are already ﬁne-tuned by human
annotators (Mützel and Ollion 2025). In by now familiar conversational bots, such
as ChatGPT, Claude, or Gemini, these models generate human-like responses to
prompts, provide advice, deliver code, translate and summarize texts, generate texts
and images, draft and improve texts, and collaborate across different programs.
Technically, whereas BERT takes the context of each word to be generated into
account, GPT models generate word by word based on the previous word it
generated and the estimated probability of the next word to follow.
These conversational models are already “game-changers for science” (van Dis
et al. 2023) and will also impact innovation studies: e.g., they can summarize,
develop, evaluate, and translate knowledge (Grimes et al. 2023), formulate new
propositions (Cornelissen et al. 2024), improve survey research, experiments, agent-
based models, or vignettes with synthetic textual or image data (Bail 2024; Karell
et al. 2025; Davidson 2024). At the same time, there are various limitations and
potential dangers of these models, which can negatively impact research, including
generated texts and sources that are factually inaccurate, exhibiting human and
“machine biases” (Boelaert et al. 2025), are unethically sourced, cannot be

---

<!-- Page 11 -->

replicated, produce seemingly polished “junk science” (Bail 2024), and may in the
medium and long term also negatively impact creativity (Hsu and Bechky 2024).
Current research also points to the dangers of using closed, proprietary LLMs for
research (Ollion et al. 2024) and instead suggests open-source LLMs (Palmer et al.
2024).
Big Data and Machine Learning Methods
11
Given all these limitations, research shows that these models nevertheless open
up new possibilities for researchers interested in analyzing large-scale text corpora.
In this instance, GPT models are used as virtual research assistants that respond to
natural language instructions and can eventually augment the capabilities of social
scientists. Fabrizio Gilardi et al. (2023) demonstrate that using ChatGPT for anno-
tations of Tweets and newspaper articles produces more accurate results than from
hired workers who had received the same instructions. In their comprehensive
discussion of classifying and coding texts in the social sciences, Caleb Ziems et al.
(2024) show that instructed LLMs can reproduce human coding decisions. They
recommend integrating LLMs in the research pipeline to transform large-scale data
labeling. Yet, they also stress the need for human expert annotators who work in
tandem with these models, instructing LLMs, proving hand coding only for reﬁne-
ment, and validating outputs.
The use of LLMs thus enables social scientists “to examine corpora of unprece-
dented size with unforeseen speed” (Bail 2024, p. 5). At the same time, using LLMs
as interlocutors to interpret and categorize texts based on coding instructions deliv-
ered in prompts may also transform processes of qualitative text analysis. Research
shows that LLMs “provide a productive blend of automation and nuanced under-
standing” (Than et al. 2025, p. 880).
Recent developments in text analytical models allow research interested in the
study of innovation to work with large-scale text corpora in their analyses. All
models discussed have advantages and caveats. Although topic modeling and
word embeddings can show temporal dynamics, inductive mappings, and categori-
zation processes, the capabilities of more recent LLMs suggest the possibility of
detecting more nuanced processes of recombination and cognitive shifts.
5
Conclusion
This chapter has explored the burgeoning ﬁeld of innovation research that uses big
data and ML methodologies. It has shown how the increasing availability of
digitized and born-digital data has provided new opportunities to study the intricate
processes of innovation, from the recombination of ideas and knowledge to the
temporal unfolding of innovation journeys and the construction of meaning and
categories.
Computational methods such as topic modeling, word embeddings, and genera-
tive language models have signiﬁcantly contributed to the ﬁeld. Topic modeling
offers an inductive approach to uncovering latent themes and patterns in large textual
corpora, enabling researchers to explore the emergence of new technological ﬁelds
and cultural dynamics. Word embeddings provide a means of mapping semantic

---

<!-- Page 12 -->

relationships between concepts, allowing for the analysis of conceptual spaces and
the measurement of novelty. More recently, contextual embeddings and LLMs such
as BERT and GPT models have demonstrated the ability to understand language in
context and even generate human-like text, paving the way for advanced text
analysis tasks and the potential for LLMs to serve as virtual research assistants
and interlocutors. Moreover, these models allow for a renewed recombination of
automated and qualitative approaches (e.g., Brandt and Timmermans 2021).
12
S. Mu¨tzel
Despite the potential for novel insights outlined, it is crucial to acknowledge the
limitations and challenges associated with these computational approaches.
Unsupervised methods, such as topic modeling and word embeddings, can suffer
from interpretive uncertainty and may not always correspond to a priori theoretical
concepts. All ML models are data driven, and their outcomes can be inﬂuenced by
data quality, pre-processing decisions, and potential biases encoded in the training
data. Although generative language models are powerful, they raise concerns about
factual accuracy, ethical sourcing, reproducibility, and the possibility of “junk
science.” As a result, when using these tools, a reﬂexive approach is required,
emphasizing the ongoing need for human expertise to guide the analysis, interpret
results, and validate ﬁndings.
Looking ahead, several trends can be noted. The use of contextual embeddings
and generative language models promises nuanced and powerful analyses in the
study of innovation. The ability of LLMs to perform tasks such as coding, summa-
rizing, and formulating new propositions points to a future in which LLMs can
signiﬁcantly augment the capabilities of innovation researchers. The digitization of
historical archives and the proliferation of born-digital data will further expand the
scope and depth of inquiry in innovation studies. Analyses will also expand their
data sources to include texts, sounds, and images as data.
In conclusion, the intersection of big data and ML fundamentally contributes to
the study of innovation. These computational tools offer opportunities to investigate
long-standing questions with new data and analytical rigor, revealing intricate
patterns and dynamics in the emergence and evolution of newness. However,
realizing the full potential of these possibilities requires a thoughtful engagement
with their methodologies and limitations and a careful interplay between computa-
tional power and human expertise.
Competing Interest Declaration The author(s) has no competing interests to declare that are
relevant to the content of this manuscript.
References
Aceves, Pedro, and James Evans. 2024. Mobilizing conceptual spaces: How word embedding
models can inform measurement and theory within organization science. Organization Science
35 (3): 788–814.
Antons, David, and Christoph Breidbach. 2018. Big data, big insights? Advancing service innova-
tion and design with machine learning. Journal of Service Research 21 (1): 17–39.

---

<!-- Page 13 -->

Big Data and Machine Learning Methods
13
Antons, David, Amol Joshi, and Torsten Oliver Salge. 2019. Content, contribution, and knowledge
consumption: uncovering hidden topic structure and rhetorical signals in scientiﬁc texts. Journal
of Management 45 (7): 3035–3076.
Bail, Christopher. 2024. Can Generative AI improve social science? PNAS 121 (21): 1–10.
Baumer, Eric, David Mimno, Shion Guha, Emily Quan, and Geri Gay. 2017. Comparing grounded
theory and topic modeling: Extreme divergence or unlikely convergence? Journal of the
Association for Information Science and Technology 68 (6): 1397–1410.
Berelson, Bernard. 1952. Content analysis in communication research. Glencoe: The Free Press.
Blei, David, Andrew Ng, and Michael Jordan. 2003. Latent dirichlet allocation. Journal of Machine
Learning Research 3:993–1022.
Bodell, Hurtado, Måns Magnusson Miriam, and Sophie Mützel. 2022. From documents to data: A
framework for total corpus quality. Socius 8:1–15.
Bodell, Hurtado, Måns Magnusson Miriam, and Marc Keuschnigg. 2024. Seeded topic models in
digital archives: Analyzing interpretations of immigration in Swedish newspapers, 1945–2019.
Sociological Methods & Research. https://doi.org/10.1177/00491241241268453.
Boelaert, Julien, Samuel Coavoux, Étienne Ollion, Ivaylo Petev, and Patrick Präg. 2025. Machine
bias generative large language models have a worldview of their own. Sociological Methods and
Research 54 (3): 1156–1196.
Bolukbasi, Tolga, Kai-Wei Chang, James Zou, Venkatesh Saligrama, and Adam Kalai. 2016. Man is
to computer programmer as woman is to homemaker? Debiasing word embeddings. Advances
in Neural Information Processing Systems 29:1–9.
Bonikowski, Bart, Yuchen Luo, and Oscar Stuhler. 2022. Politics as usual? Measuring populism,
nationalism, and authoritarianism in us presidential campaigns (1952–2020) with deep neural
language models. Sociological Methods and Research 51 (4): 1721–1787.
Borch, Christian, and Juan Pablo Pardo-Guerra. 2025. In The Oxford handbook of the sociology of
machine learning, ed. Christian Borch and Juan Pablo Pardo-Guerra. Oxford: Oxford University
Press.
Brandt, Philipp, and Stefan Timmermans. 2021. Abductive logic of inquiry for quantitative research
in the digital age. Sociological Science 8:191–210.
Caliskan, Aylin, Joanna Bryson, and Arvind Narayanan. 2017. Semantics derived automatically
from language corpora contain human-like biases. Science 356 (6334): 183–186.
Callon, Michel, J. P. Courtial, and F. Laville. 1991. Co-word analysis as a tool for describing the
network of interactions between basic and technological research: The case of polymer chem-
istry. Scientometrics 22 (1): 155–205.
Cattani, Gino, Dirk Deichmann, and Simone Ferriani. 2023. Novelty: Searching for, seeing, and
sustaining it. Research in the Sociology of Organizations 77:3–23.
Cornelissen, Joep, Markus Höllerer, Eva Boxenbaum, Samer Faraj, and Joel Gehman. 2024. Large
language models and the future of organization theory. Organization Theory 5 (1):
26317877241239056.
Davidson, Thomas. 2024. Start generating: Harnessing generative artiﬁcial intelligence for socio-
logical research. Socius 10:1–17.
Davidson, Thomas. 2025. Hate speech detection and bias in supervised text classiﬁcation. In The
Oxford handbook of the sociology of machine learning, ed. Christian Borch and Juan Pablo
Pardo-Guerra, 121–140. Oxford University Press.
de Vaan, Mathijs, Balazs Vedres, and David Stark. 2015. Game changer: The topology of creativity.
American Journal of Sociology 120 (4): 1144–1194.
de Ven, Van, Douglas Polley Andrew, Raghu Garud, and Sankaran Venkataraman. 1999. The
Innovation Journey. Oxford: Oxford University Press.
Devlin, Jacob, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805:
1-16.
DiMaggio, Paul. 2015. Adapting computational text analysis to social science (and vice versa). Big
Data & Society 2 (2): 1–5.

---

<!-- Page 14 -->

14
S. Mu¨tzel
Do, Salomé, Étienne Ollion, and Rubing Shen. 2022. The augmented social scientist: Using
sequential transfer learning to annotate millions of texts with human-level accuracy. Sociolog-
ical Methods & Research 53 (3): 1167–1200.
Durand, Rodolphe, and Mukti Khaire. 2017. Where do market categories come from and how?
Distinguishing category creation from category emergence. Journal of Management 43 (1):
87–110.
Edelmann, Achim, Tom Wolff, Danielle Montagne, and Christopher Bail. 2020. Computational
social science and sociology. Annual Review of Sociology 46:61–81.
Evans, James, and Pedro Aceves. 2016. Machine translation: Mining text for social theory. Annual
Review of Sociology 42:21–50.
Garud, Raghu, Philipp Tuertscher, and Andrew Van De Ven. 2013. Perspectives on innovation
processes. The Academy of Management Annals 7 (1): 775–819.
Garud, Raghu, Barbara Simpson, Ann Langley, and Haridimos Tsoukas. 2015. The emergence of
novelty in organizations. Oxford University Press.
Gebru, Timnit, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach,
Hal Daumé Iii, and Kate Crawford. 2021. Datasheets for datasets. Communications of the ACM
64 (12): 86–92.
Goldenstein, Jan, and Philipp Poschmann. 2019. Analyzing meaning in big data: Performing a map
analysis using grammatical parsing and topic modeling. Sociological Methodology 49 (1):
83–131.
Gregoire, Denis, Anne Ter Wal, Laura Little, Sekou Bermiss, Reddi Kotha, and Marc Gruber. 2024.
Mobilizing new sources of data: Opportunities and recommendations. Academy of Management
Journal 67 (2): 289–298.
Griliches, Zvi. 1990. Patent statistics as economic indicators: A survey. Journal of Economic
Literature 28 (4): 1661–1707.
Grimes, Matthew, Georg von Krogh, Stefan Feuerriegel, Floor Rink, and Marc Gruber. 2023. From
scarcity to abundance: scholars and scholarship in an age of generative artiﬁcial intelligence.
Academy of Management Journal 66 (6): 1617–1624.
Grimmer, Justin, Margaret Roberts, and Brandon Stewart. 2022. Text as data: A new framework for
machine learning and the social sciences. Princeton: Princeton University Press.
Grodal, Stine, and Steven Kahl. 2017. The discursive perspective of market categorization: Inter-
action, power, and context. Research in the Sociology of Organizations 51:151–184.
Grodal, Stine, Aleksios Gotsopoulos, and Fernando Suarez. 2015. The co-evolution of technologies
and categories during industry emergence. Academy of Management Review 40 (3): 423–445.
Grootendorst, Maarten. 2022. BERTopic: Neural topic modeling with a class-based TF-IDF
procedure. arXiv preprint arXi: https://doi.org/10.48550/arXiv.2203.05794.
Haans, Richard. 2019. What's the value of being different when everyone is? The effects of
distinctiveness on performance in homogeneous versus heterogeneous categories. Strategic
Management Journal 40 (1): 3–27.
Hannigan, Timothy, Richard Haans, Keyvan Vakili, Hovig Tchalian, Vern Glaser, Milo Shaoqing
Wang, Sarah Kaplan, and P. Devereaux Jennings. 2019. Topic modeling in management
research: Rendering new theory from textual data. Academy of Management Annals 13 (2):
586–632.
Hickman, Louis, Stuti Thapa, Louis Tay, Mengyang Cao, and Padmini Srinivasan. 2022. Text
preprocessing for text mining in organizational research: Review and recommendations. Orga-
nizational Research Methods 25 (1): 114–146.
Hofstra, Bas, Vivek Kulkarni, Sebastian Munoz Najar Galvez, Bryan He, Dan Jurafsky, and Daniel
A. McFarland. 2020. The diversity–innovation paradox in science. PNAS 117 (17): 9284–9291.
Hsu, Greta, and Beth Bechky. 2024. Exploring the digital undertow: How generative AI impacts
social categorizations in creative work. Organization Theory 5 (3): 1–16.
Hsu, Greta, and Stine Grodal. 2021. The double-edged Sword of oppositional category positioning:
A study of the US E-cigarette category, 2007-2017. Administrative Science Quarterly 66 (1):
86–132.

---

<!-- Page 15 -->

Big Data and Machine Learning Methods
15
Jha, Harsh, and Christine Beckman. 2017. A patchwork of identities: Emergence of charter schools
as a new organizational form. Research in the Sociology of Organizations 50:69–107.
Jones, Candace, Silviya Svejenova, Jesper Strandgaard Pedersen, and Barbara Townley. 2016.
Misﬁts, mavericks and mainstreams: Drivers of innovation in the creative industries. Organi-
zation Studies 37 (6): 751–768.
Jung, Jaewoo, Wenjun Zhou, and Anne Smith. 2024. From textual data to theoretical insights:
Introducing and applying the word-text-topic extraction approach. Organizational Research
Methods 28 (2): 182–209.
Just, Julian. 2024. Natural language processing for innovation search – Reviewing an emerging
non-human innovation intermediary. Technovation 129:1–21.
Just, Julian, Katja Hutter, and Johann Füller. 2024. Catching but a glimpse?—Navigating
crowdsourced solution spaces with transformer-based language models. Creativity and Innova-
tion Management 33 (4): 718–741.
Kaplan, Sarah, and Fiona Murray. 2010. Entrepreneurship and the construction of value in bio-
technology. Research in the Sociology of Organizations 29:107–147.
Kaplan, Sarah, and Keyvan Vakili. 2015. The double-edged sword of recombination in break-
through innovation. Strategic Management Journal 36 (10): 1435–1457.
Kaplan, Sarah, Fiona Murray, and Rebecca Henderson. 2003. Discontinuities and senior manage-
ment: assessing the role of recognition in pharmaceutical ﬁrm response to biotechnology.
Industrial and Corporate Change 12 (2): 203–233.
Karell, Daniel, Jeffrey Sachs, and Ryan Barrett. 2025. Synthetic duality: A framework for analyzing
generative artiﬁcial intelligence’s representation of social reality. Poetics 108:1–14.
Kennedy, Mark. 2005. Behind the one-way mirror: Refraction in the construction of product market
categories. Poetics 33 (3–4): 201–226.
Kobayashi, Vladimer, Stefan Mol, Hannah Berkers, Gábor Kismihók, and Deanne Den Hartog.
2018. Text mining in organizational research. Organizational Research Methods 21 (3):
733–765.
Kovács, Balázs, Greta Hsu, and Amanda Sharkey. 2024. The stickiness of category labels:
Audience perception and evaluation of producer repositioning in creative markets. Management
Science 70 (9): 6315–6335.
Krippendorff, Klaus. 2012. Content analysis: An introduction to its methodology. Thousand Oaks:
Sage.
Lix, Katharina, Amir Goldberg, Sameer Srivastava, and Melissa Valentine. 2022. Aligning differ-
ences: Discursive diversity and team performance. Management Science 68 (11): 8430–8448.
McFarland, Daniel, Kevin Lewis, and Amir Goldberg. 2016. Sociology in the era of big data: The
ascent of forensic social science. The American Sociologist 47 (1): 12–35.
Mikolov, Tomas, Kai Chen, Greg Corrado, and Jeffrey Dean. 2013. Efﬁcient estimation of word
representations in vector space. https://doi.org/10.48550/arXiv.1301.3781.
Miric, Milan, Nan Jia, and Kenneth Huang. 2023. Using supervised machine learning for large-
scale classiﬁcation in management research: The case for identifying artiﬁcial intelligence
patents. Strategic Management Journal 44 (2): 491–519.
Mogoutov, Andrei, Alberto Cambrosio, Peter Keating, and Philippe Mustar. 2008. Biomedical
innovation at the laboratory, clinical and commercial interface: A new method for mapping
research projects, publications and patents in the ﬁeld of microarrays. Journal of Informetrics
2 (4): 341–353.
Mützel, Sophie. 2015. Structures of the tasted: Restaurant reviews in Berlin between 1995 and
2012. In Moments of Valuation: Exploring Sites of Dissonance, ed. Ariane Berthoin Antal,
Michael Hutter, and David Stark, 147–167. Oxford: Oxford University Press.
Mützel, Sophie. 2022. Making sense: Markets from stories in new breast cancer therapeutics.
Stanford: Stanford University Press.
Mützel, Sophie, and Etienne Ollion. 2025. Machine learning and the analysis of culture. In The
Oxford handbook of the sociology of machine learning, ed. Christian Borch and Juan Pablo
Pardo-Guerra. Oxford: Oxford University Press.

---

<!-- Page 16 -->

16
S. Mu¨tzel
Nelson, Laura. 2021. Leveraging the alignment between machine learning and intersectionality:
Using word embeddings to measure intersectional experiences of the nineteenth century
U.S. South. Poetics 88:1–14.
Nelson, Laura, Derek Burk, Marcel Knudsen, and Leslie McCall. 2021. The future of coding: A
comparison of hand-coding and three types of computer-assisted text analysis methods. Socio-
logical Methods & Research 50 (1): 202–237.
Ollion, Étienne, Rubing Shen, Ana Macanovic, and Arnault Chatelain. 2024. The dangers of using
proprietary LLMs for research. Nature Machine Intelligence 6 (1): 4–5.
Ouyang, Long, Wu Jeffrey, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, and Alex Ray. 2022. Training language models to
follow instructions with human feedback. Advances in Neural Information Processing Systems
35:27730–27744.
Padgett, John, and Walter Powell. 2012. The problem of emergence. In The emergence of organi-
zations and markets, ed. John Padgett and Walter Powell, 1–29. Princeton: Princeton University
Press.
Palmer, Alexis, Noah Smith, and Arthur Spirling. 2024. Using proprietary language models in
academic research requires explicit justiﬁcation. Nature Computational Science 4 (1): 2–3.
Rao, Hayagreeva, Philippe Monin, and Rodolphe Durand. 2003. Institutional change in Toque
Ville: Nouvelle cuisine as an identity movement in French gastronomy. American Journal of
Sociology 108 (4): 795–843.
Roberts, Margaret, Brandon Stewart, and Dustin Tingley. 2019. Stm: An R package for structural
topic models. Journal of Statistical Software 91 (2):
Rodriguez, Pedro, and Arthur Spirling. 2022. Word embeddings: What works, what doesn’t, and
how to tell the difference for applied research. The Journal of Politics 84 (1): 101–115.
Rosa, José Antonio, Joseph Porac, Jelena Runser-Spanjol, and Michael Saxon. 1999. Socio-
cognitive dynamics in a product market. Journal of Marketing 63:64–77.
Salganik, Matthew. 2017. Bit by bit. Princeton: Princeton University Press.
Santana, Jessica, and Seonghoon Kim. 2025. From values to codes: A computational text analysis
of the codiﬁcation of occupational ethics. Organization Studies. https://doi.org/10.1177/
01708406251317255.
Schmiedel, Theresa, Oliver Müller, and Jan vom Brocke. 2019. Topic modeling as a strategy of
inquiry in organizational research: A tutorial with an application example on organizational
culture. Organizational Research Methods 22 (4): 941–968.
Slavich, Barbara, M. Silviya Svejenova, Pilar Opazo, and Gerardo Patriotta. 2020. Politics of
meaning in categorizing innovation: How chefs advanced molecular gastronomy by resisting
the label. Organization Studies 41 (2): 267–290.
Stark, David. 2009. The sense of dissonance: Accounts of worth in economic life. Princeton:
Princeton University Press.
Stoltz, Dustin, and Marshall Taylor. 2021. Cultural cartography with word embeddings. Poetics 88:
101567.
Taeuscher, Karl, Ricarda Bouncken, and Robin Pesch. 2021. Gaining legitimacy by being different:
Optimal distinctiveness in crowdfunding platforms. Academy of Management Journal 64 (1):
149–179.
Than, Nga, Leanne Fan, Tina Law, Laura Nelson, and Leslie McCall. 2025. Updating “The future of
coding”: Qualitative coding with generative large language models. Sociological Methods &
Research 54 (3): 849–888.
van Dis, Eva, Johan Bollen, Willem Zuidema, Robert van Rooij, and Claudi Bockting. 2023.
ChatGPT: Five priorities for research. Nature 614 (7947): 224–226.
Vaswani, Ashish, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all you need. Advances in Neural Information
Processing Systems 30:1–11.

---

<!-- Page 17 -->

Big Data and Machine Learning Methods
17
Vergne, Jean-Philippe. 2012. Stigmatized categories and public disapproval of organizations: A
mixed-methods study of the global arms industry, 1996–2007. Academy of Management
Journal 55 (5): 1027–1052.
Whittaker, Meredith, Kate Crawford, Roel Dobbe, Genevieve Fried, Elizabeth Kaziunas, Varoon
Mathur, Sarah Mysers West, Rashida Richardson, Jason Schultz, and Oscar Schwartz. 2018. AI
now report 2018. AI Now Institute at New York University New York.
Ziems, Caleb, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. 2024. Can
large language models transform computational social science? Computational Linguistics
50 (1): 237–291.
Zuboff, Shoshana. 2019. The age of surveillance capitalism: The ﬁght for a human future at the new
frontier of power. New York: PublicAffairs.