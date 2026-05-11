<!-- Page 1 -->

Special Issue: Critical Technical Practice(s) in Digital Research
Convergence: The International
Journal of Research into
New Media Technologies
2024, Vol. 30(1) 94–115
© The Author(s) 2023
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/13548565221144260
journals.sagepub.com/home/con
Digital methods as ‘experimental a
priori’ – how to navigate vague
empirical situations as an
operationalist pragmatist
Anders Koed Madsen
Culture and Learning, Aalborg University, Copenhagen, Denmark
Abstract
Digitalisation and computation presents us with a vague empirical world that unsettles established
links between measurements and values. As more and more actors use digital media to produce
data about aspects of the world they deem important, new possibilities for inscribing their lives
emerge. The practical work with digital methods thus often involves the production of social
visibilities that are misﬁts in the context of established data practices. In this paper I argue that this
dissonance carries the distinct critical potential to design data experiments that (a) uses the act of
operationalisation as an engine for creating intersubjective clarity about the meaning of existing
concepts and (b) takes advantage of algorithmic techniques to provoke a reassessment of some of
the core assumptions that shape the way we pose empirical problems are normally framed. Drawing
on the work of Kant, Peirce, Dewey and C.I. Lewis I propose to think of this critical potential as the
possibility to practice what I term ’experimental a priori’ and I use qualitative vignettes from two
years of data experiments with GEHL architects to illustrate what this entails in practice. Faced with
the task of using traces from Facebook as an empirical source to produce a map of urban political
diversity, the architects found themselves in a need to revisit inherited assumptions about the
ontology of urban space and the way it can even be formulated as a problem of diversity. While I
describe this as a form of obstructive data practice that is afforded by digital methods, I also argue
that it cannot be realised without deliberate design interventions. I therefore end the paper by
outlining ﬁve design principles that can productively guide collective work with digital methods.
These principles contribute to recent work within digital STS on the recalibration of problem spaces
and the design of data sprints. However, the concept of ‘experimental a priori’ can also serve as a
philosophical foundation for knowledge production within computational humanities more broadly.
Keywords
Critical data practice, Charles Sanders Peirce, digital methods, machine learning, political diversity,
practical epistemology, urban design, pragmatism
Received 6 August 2021; Revised 28 September 2022; Accepted 10 August 2021
Corresponding author:
Anders Koed Madsen, Culture and Learning, Aalborg University, A.C. Meyers Vænge 15, 2450 Copenhagen 2450,
Denmark.
Email: akma@hum.aau.dk

---

<!-- Page 2 -->

The resolution of objects […] into facts stated exclusively in terms of quantities which may be handled in
calculation […] seem strange and puzzling only when we fail to appreciate what it signiﬁes [...] this is the
effective way to think things; the effective mode in which to frame ideas of them, to formulate their
meanings.
John Dewey – The Quest for Certainty (p. 108)
Introduction
Jeff and Alex are sitting around a digital map of Copenhagen ﬁlled with dots in different colours. The
map is built on digital traces of 300,000 Facebook users’ interactions with politics and urban events.
Each dot represents an urban venue, and its colour indicates whether it attracts a politically diverse
audience. The green ones do, and the red ones do not. Jeff is a partner and CIO of GEHL architects. Alex
is an associate on the company’s innovation team. Between them, they have years of experience
measuring urban life in public spaces. Yet, they are unsure how to translate the cacophony of coloured
dots into a relevant narrative about the political geography of Copenhagen. Part of their troubles stem
from the fact that they are looking at a map that does not quite resemble the ones they are used to
interpreting. It is built on an alien data source. Its meaning is underdetermined. As they discuss which
mapping strategies would indeed create a sense of meaning in the seemingly disorganised data, Alex
suggests transforming the dots into an aggregated ‘heatmap’. A map that highlights the average political
diversity of larger geographical areas instead of foregrounding the urban venues at single dots. He points
to the map and explains: ‘This heatmap shows [that] this area over here is generally more diverse than
any of these two’. Jeff intervenes: ‘But that’s not really true spatially […]’ (Figure 1).
Figure 1. Screenshot fromone oftheﬁrstiterationsofthe diversity map with whichJeffand Alexwork inthe opening
vignette. You can explore a ﬁnal interactive version of the datascape here: https://www.tantlab.gehlpeople.com.
Koed Madsen
95

---

<!-- Page 3 -->

This conversation stems from the project ‘Do You Live in a Bubble?’ (DYLIAB), which involved
two years of collaborative data experiments between TANTLab and GEHL architects. The aim of the
project was to use traces from Facebook as an empirical foundation for cartographies that could
provide new insights into the problem of urban political diversity and perhaps even new ways of
phrasing this problem. The most tangible outcome of the project is the publication of an interactive
datascape that enables users to explore the issue of political diversity in new ways. It offers a map on
which each venue in Copenhagen is assigned a diversity index between 0 and 100, depending on how
its users engage with politics. This is this datascape that Jeff and Alex are in the process of building
above (the full method and the speciﬁc ﬁndings about diversity are described in Madsen (2022)). In
this paper, I will use selected qualitative vignettes from DYLIAB to illustrate how the decision to use
digital methods on alien data stimulated speciﬁc forms of thinking and reasoning among the people
tasked with building a diversity map. More speciﬁcally, I will argue that one of the most exciting
critical potentials in ‘thinking with digital methods’ is the possibility of practicing a mode of enquiry
that I propose to call experimental a priori. A form of technologically assisted enquiry that allows for
re-composing the way empirical problems are framed by unsettling established modes of measuring.
Throughout the paper, I draw on the philosophies of Kant, Peirce, Dewey and C.I. Lewis to
sketch a philosophical foundation for this speciﬁc form of obstructive data practice. First, I use
Dewey’s work to argue that the decision to work with native digital data (such as data from
Facebook) almost always positions the analyst in a vague empirical situation where the analytical
components and their internal relations are unclear. Given that digital traces are produced under
constantly changing conditions, it is impossible to work from clear and durable methodological
standards. Each new project needs to reassess how digital traces make sense as inscriptions of the
speciﬁc empirical phenomenon one is trying to produce knowledge about. Although this is po-
tentially frustrating, it is also liberating in the sense that it allows revisiting the elements that make
up a problematic situation (such as urban diversity). Second, I draw on Peirce to argue that the best
way out of this vagueness is to decide on a set of formal operationalisations that stabilise the
connections between measurement, enquiry, and problematisation (such as the heatmap proposed
by Alex). Decisions on operationalizations afford a distinct form of intersubjective sensemaking that
requires participants to clearly explicate what they mean when they use speciﬁc concepts in their
problem formulations (such as space). Third, I argue that the availability of a wide variety of
explorative algorithmic techniques to identify patterns in unstructured and granular digital traces
means that this stabilisation can be achieved in many ways. Drawing on C. I. Lewis, I argue that
there is no shared a priori baseline around which the empirical must be ordered. To the contrary,
digital analysis requires the active production of such a baseline (see also Madsen 2015; Madsen and
Munk, 2019). The fact that this can be done in an iterative fashion is what I propose to discuss as the
opportunity to practice the mode of enquiry I call experimental a priori. Fourth, I argue that this
speciﬁc mode of enquiry carries distinct potential as a critical data practice. However, I also argue
that this opportunity does not arise by itself. The critical situation has to be intentionally designed
and I end by providing criteria for such a design.
The theoretical framework of experimental a priori takes inspiration from – and further
elaborates – important work within digital Science and Technology Studies (STS) during the last
decade. First, it contributes to the discussion of how digital methods and the rise of computation
allow for new modes of empirical experimentation (Marres and Stark, 2020; Moats and Seaver,
2019). More speciﬁcally, the suggestion to work with digital methods with an outset in speciﬁc
design principles adds to the growing literature on data sprints (Madsen and Munk, 2019; Munk
et al., 2019) and participatory data design (Jensen et al., 2021) The arguments in this paper can
furthermore be read as an addition to Lury’s (2020) recent work on how the increasingly digital
96
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 4 -->

society stimulates a form of ontological disturbance that opens up the possibility to critically
recompose the problem spaces that guide our existing epistemic habits. The suggestion to view
some of these questions through the works of Kant, Peirce, Dewey and Lewis, hopefully, helps
strengthen the attempt for digital STS to work actively with quantiﬁcation and algorithmic
techniques from its own distinct philosophical ground. This ground would also have relevance for
broader discussions about digital data experiments (Blok 2020) and the epistemology of com-
putational social sciences and humanities more broadly (see e.g. Nelson 2020 and Benthall 2016).
The computational turn as a generator of vague empirical situations
Digital methods were born in tandem with the so-called computational turn (Berry, 2011) in the
early 2000s. As people moved their social lives online, new types of digital data and techniques for
analysing them became available to researchers in the social sciences and humanities. The fact that
most of these data and techniques were shaped by owners of online platforms changed the way
empirical phenomena could be observed. The platforms brought forth a multiplicity of data authors
and inscriptions that, by far, outnumbered everything seen before. Furthermore, their data were
granular, unstructured and messy (Kitchin, 2014). No matter which phenomenon is of interest to
study, no single actor would be in control of the conditions under which data about it would be
produced. The unsurprising result is that data after the computational turn rarely follow established
classiﬁcatory standards. When the state and other public institutions were the main producers of
data, their scope and details had a natural limit. Since one had to be strategic about what to count and
inscribe, data would often be aggregated into categories and data models agreed upon by these
institutions. As digitalisation expands the number of data authors, this limit erodes. The world can
be inscribed in various ways by various actors, depending on what they ﬁnd important.
This is what Dewey (1938) would describe as a vague empirical situation, in which existing
concepts and classiﬁcatory schemes lose their heuristic value as guides of thought and action. This
creates a need to (re)establish the analytical components of the situation one is interested in
studying. Which objects are present? How do we distinguish between them? What are they called?
How do they relate to each other? Only by answering such questions can we return to a situation in
which it is possible to think and act. To Dewey, this form of reconstructive work is the core of critical
thinking. Although arguably frustrating, vague situations are valuable because they stimulate a form
of suspended judgement that the human mind normally prefers to skip (Dewey, 2007). Dewey thus
concluded that good enquiry involves an attempt to deliberately provoke such situations. If we fail
to do so, our analytical schemes will ultimately be unﬁt for the constantly changing empirical world.
One of Dewey’s proposed strategies for provoking vagueness was to invent tools and instruments
that fundamentally change the way empirical phenomena can be observed (Dewey, 1929). A task
that is now routinely done by people within and around academia.
The last decades of work with digital methods in STS can be seen as driven by a desire to take
advantage of the vagueness introduced by the computational turn. For instance, Rogers’ (2013) early
work with natively digital objects was precisely driven by a curiosity about what we could learn from
‘following the web’ and the ontologies of digital media. This led to the rise of ‘post-demographic’
analyses that differed from most quantitative social sciences by not automatically clustering people
based on demographic traits. Similarly, Marres (2005) used the relational structure of the web to trace the
composition of issue publics rather than conceptualising ‘the public’ as an entity that had to do with
voting intentions and party sympathies. Although these early studies enabled new representations of
empirical phenomena, such as groups and publics, they also required analysts to interface with alien
methodological traditions. The provenance of digital data was often unknown, and working with it
Koed Madsen
97

---

<!-- Page 5 -->

meant relying on infrastructures and analytical techniques developed by people with speciﬁc interests in
and around Silicon Valley (Marres, 2012). Against this backdrop, I agree with Lury’s (2020) statement
that the rise of the digital society means that ‘[…] linkages between measure and value are [...] being
recalibrated’ (ibid:87). This is what I refer to as the rise of empirical vagueness.
Returning to the ofﬁces at GEHL, I propose that it is exactly the need to engage in such a vague
process of recalibration that troubles Jeff and Alex in the opening vignette. Working at GEHL, they
are employees of a company with an empirical toolkit that has been developed over decades to make
standardised representations of public life in public spaces. This toolkit is called PSPL (Public life/
Public Space) and it uses surveys, interviews and observations to map people’s behaviour in pre-
selected public spaces. Typically, the spaces observed are identiﬁed in conversation with local
municipalities, and they have recognisable forms, such as a square, a street segment or a block.
GEHL analysts are then sent to the selected spaces with a structured observation guide that enables
them to inscribe urban life in these spaces. For instance, if the topic of interest is urban diversity, this
guide could include a task to count the number of men and women and to note the extent to which
they interact in conversations. This methodological approach is sometimes internally referred to as
part of the ‘GEHL lens’ and has been documented in various publications, creating the company’s
trademark gaze on the urban (Gehl, 2011; Gehl and Svarre, 2013) (Figures 2 and 3).
Figure 2. Central elements in the GEHL lens. To the left, employees ready to observe urban life in pre-
selected spaces. In the middle, the survey guide structuring their gaze on gender distribution is a predeﬁned
street segment. To the right is a visualisation of gender composition in a speciﬁc public space.
Figure 3. Central elements in the Facebook lens. To the right are traces of anonymous users’ engagement
with a political post. In the middle are traces of anonymous users’ interest in a speciﬁc concert. To the right is
a visualisation of the political composition of the crowd at a speciﬁc event.
98
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 6 -->

When tasked with mapping urban diversity through traces from Facebook, Jeff and Alex ﬁnd
themselves working with an alien data source that inscribes public life and public space from a
quite different outset. This naturally prompts questions about its provenance and validity. What
are we looking at when we examine the way people engage with politics and urban events on
Facebook? Who leaves traces such as likes on this medium, and why do they do it? Can we even
think of these users as an urban public? Are these traces reliable signals, or are they inﬂuenced
by platform algorithms? Do we know whether people have been to the events they indicate that
they attend? Is this even important for understanding urban life? These were questions that
popped up early in our project, and it was questions that GEHL team members had already asked
themselves in prior attempts to work with exhaust data from social media (GEHL Studio SF,
2015). The diversity project brought them back to renewed strength. Viewing the problem of
urban diversity through the lens of Facebook (Figure 3) rather than through the GEHL lens blurs
what counts as public life and public space. The empirical situation is vague compared to a
situation in which the established PSPL method is the main empirical tool. This creates
frustration but also critical opportunities.
Operationalisation as intersubjective semantics
Vague empirical situations provide an opportunity to engage in what Dewey (1929) termed
operational thinking. As long as the empirical components of a situation are unclear, a
community of enquires can only move productively forward by agreeing on a procedure to
identify them. As argued above, the digital is ripe with vagueness. For instance, it is not obvious
how to deﬁne and recognise something as fundamental as a person in unstructured traces from
Facebook. Individuals can have many accounts that are often deliberately created to distinguish
between a private and a professional self. Should these count as two persons or one? What if half
of the posts of the professional account are written with the help of a robot, does that make the
account less human? This kind of ontological indeterminacy allows for explicating what is
meant by the concept of a person. It confronts analysts with the task of creating shared signiﬁers
that can function as referential evidence for a speciﬁc analytical object (Dewey, 1910). Big
digital datasets require such signiﬁers to be formalised because their scale makes it necessary to
delegate the task of identifying objects (such as persons among thousands of proﬁles) to an
algorithm. A decision on such formal operationalisation is a bottleneck for proceeding.
Thinking about conceptual ideas as items that are put to work by sets of operations offers a
promising way forward for critical digital enquiry. What counts as a person in our example is
deﬁned according to the way we choose to recognise it rather than by reference to some
metaphysical truth about what a person really is. What is interesting about the vagueness of the
computational turn is that it allows ideas to be put to work in multiple ways.
This connection between operationalisation and meaning owes much to Peirce’s (1878)
original formulation of the pragmatic maxim, which stipulated that the meaning of concepts
must lie in their tangible1 effects. The semantic test of a concept is to explicate which pro-
cedures to follow to obtain perceptual acquaintance with the objects falling under it. For
instance, Peirce argued that the meaning of calling an object ‘hard’ lies in the operational test
that it would not be scratched if it were to be rubbed against other objects. Similarly, if one
decided that a Facebook proﬁle could only be labelled a person if it made no use of bots, the
operational test could be that it would sometimes have periods of inactivity. It would sleep like a
human does. To Peirce, it was of utmost importance for meaningful enquiry that the results of
such operational tests could be assessed by an intersubjective community of enquirers. Only
Koed Madsen
99

---

<!-- Page 7 -->

such a common point of reference would ensure that concepts such as ‘hard’ or ‘person’ were
clear enough for this community to critically assess whether an entity was meaningfully labelled
as hard or as a person. As Peirce put it, ‘We come down to what is tangible [...] as the root of
every real distinction of thought’ (Peirce, 1878): 56). Drawing on Burke (2013), I suggest that
Peirce planted the seed for a speciﬁc operationalist strand of pragmatism2 that is fruitful to
revisit when identifying the critical potentials of digital methods.
I will motivate this by returning to the dotted screen in the ofﬁce of GEHL architects. When
we left our two urbanists in the opening vignette, Jeff questioned whether the heatmap sug-
gested by Alex would actually give insights into spatial aspects of political diversity (‘Is it
really true spatially?’). Shortly after, he motivates this question by introducing an important
conceptual distinction: ‘I want to look at the place – not the event’. As described above, this
distinction has a quite straightforward empirical meaning in GEHL’s PSPL toolkit. A place
would be a speciﬁc section of the city, such as a public square, where GEHL employees can be
sent out to make their observations. An event would be whatever happens within that predeﬁned
place. However, the distinction is not as straightforward when the empirical situation involves
traces from Facebook. In Facebook’s native digital ontology, the only geolocated entities are
urban venues that own a Facebook page. As the events are announced on this same page, they
are co-located with the venues. In this inscription, the place and the venue/event are geo-
graphically synonymous. In Facebook’s ontology, there exists no well-deﬁned spatial container
in which the events occur.
Accordingly, if Jeff and Alex want to make a geographical distinction between a place and an
event, they have to translate this distinction into an operation that has a tangible consequence on the
dotted map they both have their eyes on. Following Peirce, one could say that the distinction will
only carry meaning when they decide which formalised rules an algorithm must follow to realise the
ambition of looking at places rather than events. Collectively, they embark on this task. This time,
they are looking at a map with a few more colours than the one in the opening vignette. Venues
attracting the left wing are coloured in red, venues attracting the economic liberals are coloured in
blue, and venues attracting nationalists or are coloured in yellow. The politically diverse venues are
still coloured in green.
Alex: I think we should only look at the reds, yellows, and blues, as in events, without the green
ones. Because these are polarised events, and if we can do a radius—and we have one red, one blue
and one yellow—this radius…this spatial radius would have a diversity index. It would be diverse
or not diverse.
Jeff: If that street, like Studiestræde, had the opportunity to attract […] red, yellow, and blue, that’s super
diverse. That’s potentially more diverse than here being green. [Jeff points to a street on the map with
green dots.] That’s what I want to try to do. I want to add to what Anders has done and make it a spatial
analysis.
Jeff and Alex are engaged in the task of settling the components of the vague situation and their
internal relations. The necessity of this work is sparked by a shared verdict that the dotted map they
are working on is not spatial. Geolocated events coloured by their political diversity scores do not
qualify as a relevant representation of urban space. For Jeff and Alex, an urban event/venue is
something different from an urban place/space. This is their conﬂict with the native ontology of
Facebook. To ensure that the map represents the latter, rather than the former, they brainstorm on
operationalisations that would enable them to look at a spatial map.
100
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 8 -->

In the quote above, Alex suggests two solutions that are both illustrated in Figure 4 below. One
suggestion is to ‘draw a spatial radius’ and use this as a container in which to aggregate the diversity
score of the events. Whether this spatial radius would come in the form of a hexagon or a physical
street grid is less important than the need for some sort of aerial boundary that could substitute
Facebook venues (the dots) as the geographical unit dominating the visualisation. To Jeff and Alex,
the relevant question is whether people of different political leanings are co-located in the same
physical public space – not whether they frequent the same events inside the walls of the private
venues that host Facebook events. For instance, if a book launch on identity politics for a leftist
crowd (red dot) is held right next to an afternoon update on the stock market attracting a liberal
economic crowd (blue dot) and a screening of an old Danish movie attracting a nationalist crowd
(yellow dot), ‘that street’ (as Jeff puts it in the quote above) would be an interesting place to study in
deeper detail. In fact, Jeff and Alex agree that this would be more interesting than identifying
isolated events – such as a football game – that attract a politically diverse crowd. This is also what
motivates the suggestion to reproduce the map ‘without the green ones’ (as put by Alex above). The
diversity of single events is a form of noise when one wants to identify larger urban areas that serve
the function of attracting people from across the political spectrum. It muddles the spatial ontology
when the agent of diversity can be both a venue and a street.
The work done by Jeff and Alex is an instantiation of Peirce’s idea that the decision concerning
which operations to perform on an empirical material is also a speciﬁc way of opening up concepts
for intersubjective assessment. In the process of deciding on the operationalisation, Jeff’s intuitive
Figure 4. An illustration of the two proposed solutions for ensuring that the map represents place and not
events. In the ﬁrst frame, the diverse venues are erased, which results in a map with homogenous venues
only. The second frame shows that they will each receive a diversity score of 0 because they each attract a
homogenous audience. Measured in this way, the street would have low diversity. However, if you shift the
geographical unit of analysis to the street, this street will attract a very diverse crowd and get a score of 100.
Koed Madsen
101

---

<!-- Page 9 -->

distinction between events and places becomes clearer and more tangible. By stripping the map for
accidental qualities such as the green dots, Jeff and Alex prepare the ground for focused data
explorations that they ﬁnd relevant to the problem they are trying to solve. In this rendering, private
venues can no longer be agents of diversity. This also illustrates how data explorations are never
random or free of theory. There is an intent driving which operationalisations are tried out. The
decision of a speciﬁc way of measuring is ultimately an act of selecting some qualitative aspects of a
situation as more important than others. It establishes the qualities to be compared and the means for
comparing them. Engaging in collective operationalisations is therefore also engaging in a col-
lective (re)composition of the world that highlights some aspects at the expense of others.
In the case of Jeff and Alex, their composition of the map has the consequence that the cacophony
of dots is translated into something that is manageable for architects and urban designers to act on.
Although these professions cannot change or improve events inside the walls of private venues, they
have lots of experience improving public urban areas, such as streets. According to one of their
colleagues in an interview on the project, ‘it’s natural [for urban designers] to put the physical at the
forefront, because that’s what we’re set in the world to change or to improve’. This ultimately
connects the operations of the data with the agency afforded by the resulting visualisation. The
dotted map simply carries the wrong kind of agency, whereas the proposed translation into an urban
grid ﬁts a spatial ontology that is commensurable with the PSPL methods developed inside the
company. This connection between space and agency is also reproduced in the ﬁnal published
version of the map, which includes speciﬁc stories comparing the diversity of selected urban areas
with reference to their physical traits (see Figure 5).
One lesson from the work of Jeff and Alex is that vague data situations stimulate a need to
translate conceptual distinctions into novel operationalisations, thereby explicating the assumptions
underlying them. As the computational turn provides a plethora of vague situations, it allows for
critical reﬂection on whether the operationalisations that ﬁt an old data environment can mean-
ingfully be imported to a situation with new types of data and analytical techniques. Ultimately, it
allows for the kind of recalibration between measure and value discussed by Lury (2020). Seeds of
such recalibration are, for instance, visible in a follow-up interview with Jeff, where he states that
GEHL needs to talk about ‘[…] whether the public realm includes libraries and schools and even
like, some caf´es and barbershops […]’ (Interview with Jeff Risom). His concept of space is
critically evolving with the practice of inventing new operational procedures and interpreting their
Figure 5. Screenshot of one of the stories on the published website, where we compare two areas of
Copenhagen in terms of their political diversity. This comparison shows that Folkets Park is very red and
Sundbyøster Plads is more diverse. It allows for conversations about the characteristics of the built
environment in these areas rather than the speciﬁc venues.
102
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 10 -->

consequences. This is also a central point in Dewey’s writings on operational thinking, in which he
argued that the practice of establishing new standards relies on successive reﬁnements of operations.
Vague situations do not allow for operational revolutions but rather incremental tweaks.
Digital methods as ‘experimental a priori’
The concept of the ‘a priori’ can be translated into that which comes before experience in the
production of knowledge. This is a relevant concept in relation to the vignette above, where Jeff and
Alex discuss how to instruct a spatial algorithm to structure data before they become perceptually
acquainted with it in the form of a map. Their aim is to agree on formal mechanisms of aggregation
that the unstructured data must run through before they are made visible in a visual form. I propose
thinking of this as an a priori element in their subsequent enquiry and I will argue that an important
potential in digital methods to allow for a form of experimental a priori that can provoke the kind of
suspended judgment that Dewey thought to be the essence of critical reasoning. Before illustrating
this with a return to Jeff and Alex, I want to clarify how my notion of an experimental a priori builds
on – but also differs from – the way Kant, and later C.I. Lewis described the a priori element in
thinking.
Let’s start with Kant. Before him, most philosophers assumed that the goal of thinking was to
mirror a pre-existing world. For instance, empiricists argued that cognitive activity happens
after the senses have been provided with raw material from the world. Kant’s great contribution
was to ﬂip the script on this assumption. His suggestion was that the human mind provides the
scaffold of experience before the senses even enter the game. Experience begins after the mind
has imposed certain categories and structures on the world. We can thus think of Kant as the ﬁrst
constructivist philosopher. His main argument was precisely that the patterns and regularities
we end up designating as analytical ﬁndings of an empirical enquiry cannot be reduced to
empirical inputs from a pre-existing world. The mind structures the empirical and thereby sets
the boundaries for the way arguments about the world can meaningfully be formulated. Kant
used the geometry of space as one example of such a structure. According to Kant, ‘One can
never forge a representation of the absence of space, though one can quite well think that no
things are to be met within it’ (Kant, 2007/1787: 65 [B38-9]). In this example, Euclidean
geometry sets a priori boundaries within which empirical debates about the motion of objects
can be meaningful. It is possible to debate whether two objects will collide in space, but the
geometry of space itself cannot be derived from – or refuted by – experience. It is what
structures experience in the ﬁrst place. Kant named such structuring principles synthetic a priori.
It would be impossible to have meaningful intersubjective conversations without them but they
cannot be put into any empirical test. To Kant, the central concern of critical epistemology is
identifying and describing these transcendental boundaries.
Peirce found merit in the idea that experience is always already structured by some agency
outside the empirical. He proposed that there will always be elements of empirical statements that
cannot be disproven empirically. Dewey (1938) took a similar stance when he argued that certain
‘functional essences’ are necessary tools for thinking. However, the transcendental and stable
character of Kantian a priori troubled both Peirce and Dewey. Kant ends his Critique of Pure Reason
by identifying 12 universal categories, which he believed structures the cognition of all humans
across time and space. Euclidean space is one example, and the remaining 11 categories also take
inspiration from the Euclidean geometry and Newtonian physics that were taken as ground truths in
Kant’s time.
Koed Madsen
103

---

<!-- Page 11 -->

This ground truth was outdated by Einstein’s relativism at the beginning of the 19th century,
when pragmatist philosophy matured. To the pragmatists, Kant posed the right questions but arrived
at the wrong answers. As processual thinkers, they were interested in describing the ongoing
intersubjective construction of the a priori in response to concrete problems, not in arriving at ﬁnal
and universal categories. This pragmatist take on the a priori was most thoroughly developed in the
work of C. I. Lewis (1923). To escape the universalist tendencies in Kant’s proposal, he provided the
following statement about the a priori in the production of knowledge:
“What is a priori is necessary truth not because it compels the minds acceptance, but precisely because it
does not [...it...] represents an attitude in some sense freely taken, a stipulation of the mind itself, and a
stipulation which might have been in some other way if it suited our bent and need”. (ibid: 166)
Lewis’ ontological premise is that the empirical world is full of unsorted and confusing sensory
inputs that cannot meaningfully be discussed as experience in their raw form. There is no single
uniformity waiting to be uncovered. Rather, there are several possible structures and patterns that
could ﬁt this unstructured mess. Different a priori stipulations afford sifting and ordering the
empirical world in their own distinct and legitimate ways. Lewis used the logical law of con-
tradiction as an example of such a stipulation. By stating that nothing can be both X and non-X, this
law constitutes a binary world that affords formulating speciﬁc problems and conducting speciﬁc
empirical investigations. However, this law of logic does not ‘compel the mind’s acceptance’.
Lewis’ pragmatic twist on Kant’s stance is that this form of a priori stipulation is authoritative for a
community of inquirers precisely because it is freely chosen and therefore cannot be put to a decisive
empirical test. The only possible test is whether it ﬁts the problem at hand. Lewis called it a
pragmatic a priori.
I want to suggest that Jeff and Alex were engaged in stipulating such a pragmatic a priori
when we left them above. After having tried different operations on the data at hand (e.g. erasing
and keeping the green events), they end with a choice between two modes of ordering space,
each of which brings out different patterns and provokes different problem formulations. One is
the dotted map. The other is the recomposed heatmap suggested by Alex. The necessity of
making a choice between these maps subsequently sparked even more nuanced discussions
about the concept of urban space than the one reported above. For instance, the notes in Figure 6
stem from a discussion about whether it made sense to deﬁne two venues as close when they
have a short geographical distance between them, or whether it would be better to think of them
as close if they are placed on a natural walking route between two points. Although this
discussion ended with the former solution, the necessity of arriving at this operationalisation
involved formulating different ways of formalising space and thereby establishing the prag-
matic a priori that would serve as the scaffold for the empirical investigations of space.
The relational nature of the digital traces from Facebook also allowed for experimenting with the
even more radical idea of operationalising urban space as a network where two venues would be
‘close’ to each other if they shared many visitors. The images in Figure 7 below are two outcomes of
this experiment. To the left, we see a network in which each dot is a food venue in Copenhagen.
Venues of the same colour share users and thereby constitute a food cluster. One example is the
cluster to the right, which consists of coffee shops and restaurants that offer reasonably priced
vegetarian meals. This visualisation constitutes a very different ontology of urban space than the
geographical grid that usually structures GEHL’s gaze on the urban. The empirical object of a food
cluster is based on networked distances. Even though the venues in the plant-based cluster are close
104
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 12 -->

in terms of shared users, they are positioned geographically far apart in the city. Proximity thus
comes to have a very different meaning in the network than in the maps sketched above.
These representations can be interpreted as examples of the kind of diagrammatic reasoning
promoted by Peirce (1906) in his later work. They constitute distinct formalised frames within
which the space can be observed and tinkered. They shape how the problem of urban diversity can
be phrased. Following Lewis, I suggest that the choice between these spatial models cannot be
determined by empirical evidence. They all ﬁt the data—albeit in different ways. The choice is a
matter of establishing the boundaries within which empirical questions – such as the one concerning
which areas of Copenhagen cater to political diversity – can even be asked. Establishing these
boundaries is decisive for the ways in which problems can be posed and answered. In the context of
urban design, this was already discussed a decade ago, when Christoph Alexander (1968) claimed
that one of the main problems of the discipline was the tendency to automatically impose
standardised spatial grids on empirical traces of urban life. More speciﬁcally, Alexander criticised
the tendency of urban designers to deﬁne spatial units as mutually exclusive and not overlapping.
Figure 6. Notes from the discussion concerning the operationalisation of urban space. In the middle of the
green note, we see an attempt to sketch an operationalisation of proximity. In the white note, this is related
to the operationalisation of space, which could vary from district level to a speciﬁc lake, such as Damhussøen.
Figure 7. Visualisations of the attempt to move from a geographical representation of data to a visualisation
that positions urban venues in a relational space.
Koed Madsen
105

---

<!-- Page 13 -->

Similar to the logical law of contradiction discussed by Lewis, this structure limited the way
problems about the city could even be formulated.
However, I suggest that the critical potentials of digital methods are best grasped by thinking of
them as enabling a form of experimental a priori that is slightly different from the pragmatic a priori
formulated by Lewis. Developments in technology and math have once again changed the way we
can talk about the role of the a priori in the production of knowledge. Whereas the physics of
Einstein demonstrated the arbitrariness of stable Kantian categories, I argue that the computational
turn prompts us to substitute Lewis’ pragmatic a priori with a more iterative and experimental
version. Whereas Lewis imagines the stipulation of a pragmatic a priori as occurring before the
empirical investigation, practitioners of digital methods often ﬁnd themselves shifting between
different structuring principles while performing the empirical analysis. This is possible for two
reasons. First, digital data come in less structured and more granular formats than most previous
data. They are a good example of Lewis’ unsorted world, which opens up the possibility for various
forms of structuring. Second, the availability of explorative algorithmic techniques and ﬂexible
visualisation tools makes it possible to iteratively experiment with such structuring on the ﬂy.
This possibility of iteratively probing the structure of empirical material is exactly what Dewey
denotes as experimental thinking. To him, the core of experimentation is the decision to translate
complex qualitative objects into data that are simple and formal enough to enable things to be
brought into relation with each other in multiple ways (Dewey, 1929: 79–80). These relations
should be so clearly deﬁned that they can be the subject of controlled interventions, of which an
intersubjective community can assess and discuss overt effects. Dewey’s point is that such
experimentation does not need to be practiced in a formal laboratory. In fact, we constantly
perform quasi-experiments in ordinary practice when, for example, we turn or shake things.
Experimentation in the context of digital methods simply allows for the continuation of this mode
of enquiry by operationalising different relations and testing their effects.
We have already seen indications of this in the vignettes with Jeff and Alex above. Their attempts
to tame the unstructured Facebook traces leave them experimenting with different spatial models
that must be critically evaluated with reference to their relevance for the process of enquiry. The
important point is that digital methods make it possible to seamlessly switch between these
structuring principles. We took advantage of this throughout the DYLIAB project, in which we
compared maps with networks and pondered the questions they each generated. It is this type of
epistemic practice that I propose to describe as experimental a priori. We are imposing structures
that cannot be disproven by empirical data, but we are doing so in ways that enable constant
comparisons between them. One could say that in the context of digital methods, Lewis’ pragmatic a
priori is permanently beta (Neff and Stark, 2004). The consequence is that established concepts –
such as space in the case of Jeff and Alex – are opened for redeﬁnition. When this works, we reach
an obstructive and critical mode of enquiry that recalibrates linkages between measure and value in
ways that slow down reasoning and ensure that problem spaces are in tune with the situation they are
meant to solve.
Why intersubjective and obstructive data practices do not emerge by themselves
However, it is by no means given that this critical potential is realised just because it is possible.
Vagueness is not always productive for critical thinking. In fact, in his original discussions of critical
technical practices, Agre (1997) explicitly suggested that the vagueness of AI models allows them to
be applied in uncritical ways. By having their inner workings black boxed, they often end up
supporting a sort of ‘anything goes’ relativism in which the underdeterminacy of data can be used to
106
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 14 -->

legitimise almost any pre-existing individual agenda or narrative. My colleagues and I have
previously described this as a docile data situation (Munk et al., 2019). Peirce (1877) similarly
warned that people’s ‘ﬁxation of belief’ can happen for various reasons, of which few are rooted in
the kind of critical operationalist semantics he put forward as the proper form of enquiry.
The fact that the digital data environment carries this risk is nicely illustrated by returning to one
of the ﬁrst data workshops in the collaboration between TANTLab and GEHL. In this workshop,
four researchers from the lab met with three GEHL employees to explore the ﬁrst prototype of the
diversity map. This map was portrayed on a large interactive touchscreen that we used to co-explore
data patterns. The intention was to use it as a shared empirical ground for selecting speciﬁc areas of
Copenhagen for further qualitative analysis. The situation was empirically vague because we had no
established rules for how to use the data to identify relevant areas. In the words of Lury (2020), we
had no procedure for linking the measurements on the map with the value of being an interesting
enough urban area to merit further exploration. The aim of the workshop was to develop such
procedures and discuss the urban ontologies motivating them.
However, the workshop did not take this desired route. Having recently been engaged in a project
on Israel’s Square – a speciﬁc area of Copenhagen – some of us approached the screen several times
to zoom in on this square and explore the political diversity of its events (see the ﬁrst image in
Figure 8). Thus, the digital traces from Facebook were translated into the role event data play in the
standardised PSPL procedure, in which the selection of an interesting place happens as a precursor
to looking at its urban life and its events. Throughout the workshop, this form of targeted exploration
became a standing joke. When somebody zoomed in on Israel’s Square, he or she was often met with
the ironic statement ‘no bias’ to indicate that we were imposing pre-existing interests on a datascape
we had not really decided how to navigate. Despite this joke, the workshop continued with us taking
turns zooming in on areas that we found relevant or interesting for personal or professional reasons.
After an hour of exploring the map in this way, Jeff suggested that each of us vote for the areas
that we found most interesting. He introduced this strategy of selection with a sarcastic statement
that moved the focus from the touchscreen to a whiteboard with post-it’s: ‘It wouldn’t be a workshop
without the sticky notes. You guys did well with the big iPad’. By aggregating our individual votes on
post-its, we ended up selecting four areas for further exploration (see the second image in Figure 8).
Although each of these areas did indeed contain interesting data, their selection was driven by our
Figure 8. Snapshots from one of the ﬁrst data workshops with GEHL. To the right, we are engaged in
exploring areas out of personal interest, and to the left, we are engaged in the post-it voting session.
Koed Madsen
107

---

<!-- Page 15 -->

personal interests in Copenhagen. In fact, the biggest laugh of the afternoon came when someone
asked whether we could trace our selection back to some operational structure in the full dataset.
Many of us had the sense that we had done exactly what Agre had warned against. Rather than
engaging in the hard work of deciding on a shared operationalisation for identifying interesting
areas, we imposed our idiosyncratic interests on it. This was nicely captured by one of the GEHL
participants, who dryly stated that she thought we should try this method in a city that none of us
knew beforehand.
If Peirce had witnessed this workshop, he would have lamented the missed opportunity to engage
in the critical work of establishing a formal intersubjective procedure for solving the task of se-
lecting an ‘interesting place’. Instead, we allowed ourselves to fall in love with our own pet stories
and subsequently rank them based on votes. The consequence was that nobody took a critical view
of their own premises for selection. In the absence of an explicit procedure, any place could be
deemed interesting with a good enough narrative.
Experimental a priori in ﬁve steps
Throughout this paper, I have tried to establish the practice of experimental a priori as one distinct
form of critical data practice that is made possible by the rise of digital methods. However, the fact
that such critical practices do not arise on their own is also why recent scholarship in digital STS has
discussed the importance of the design of data sprints and participatory data processes (Moats and
Seaver, 2019; Munk et al., 2019; Venturini et al., 2018; Madsen and Munk, 2019). I suggest that the
operationalist strand of pragmatism offers a useful theoretical foundation for formulating criteria for
such a design. Criteria that could function as guidelines for organising data experiments, in which
the goal is to use quantiﬁcation to critically recalibrate the link between measures and values while
staying clear of the relativist trap noted by Agre. With reference to the discussion above, I end this
paper by outlining ﬁve distinct steps in such an iterative process of critical enquiry.3
Step 1. Seek alien data sources that create vague empirical situations
Figure 9. The ﬁve steps in practicing experimental a priori.
108
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 16 -->

The ﬁrst step can be conceived as a sort of self-punishment because it involves actively
seeking out data sources that trouble your native categorical schemes. In a world ﬁlled with
digital data traces, most empirical phenomena will be inscribed by actors with different cat-
egorical schemes than yourself. In our example, we saw how the decision to inscribe political
diversity and urban space through Facebook traces created classiﬁcation troubles that would not
have existed if we had used a data source, such as the voting behaviour of neighbourhoods. As
the structure of Facebook data was alien, it manifested a form of empirical vagueness that forced
us to slow down and ponder what we were looking at. According to Dewey, such vagueness is
the ﬁrst step in productive enquiry, and it is therefore a pursuit that analysts could actively seek
to produce by asking whether the empirical phenomena of interest are inscribed in data in-
frastructures that are not part of the standard scoping of data. Doing this can stimulate what
organisational scholar David Stark (2011) once called a ‘sense of dissonance’ that can help keep
analysts sensitive to changes in their environment.
Step 2. Operationalise central concepts to recalibrate the link between measure and value
Given that the decision to work with an alien data source will most likely break established links
between measures and the empirical phenomenon of interest, the second step is to insist that formal
operationalisations of central concepts are re-established in collective dialogue. This process is
important because the task of formalisation requires a form of prioritisation that brings out people’s
commitments to the concepts involved. In Peirce’s vocabulary, it is what makes theoretical dis-
tinctions tangible and thereby meaningful. In the examples with Jeff and Alex, such a process is
what led to the scribbled notes in Figure 6, but it was also what was bypassed in the workshop
depicted in Figure 8. If we were to redo this workshop with the ambition to practice experimental a
priori, we should have taken advantage of the fact that the participants from the start suggested
criteria for identifying what would count as an interesting place. For instance, several made the point
that diverse events hosted by public institutions with free access are more interesting than private
events. Instead of zooming in on areas of personal interest and investigating whether they hosted
events that met these criteria, we could have spent the time collectively discussing how this
qualitative criteria could be formalised, thereby getting closer to what we each meant with the
distinction between public and private.
Step 3. Decide on procedures for algorithmic pattern recognition and let attention follow along
After having decided on operationalisations, the third step is for the collective to delegate its
attention to the formalised system built in Step 2. The reason for this is not that algorithmic
techniques are neutral or devoid of theory, as suggested by Anderson (2008). Lewis’ discussion
of the pragmatic a priori already debunked this idea. Rather, the choice to start the conversation
from patterns found by such techniques equips data to act as a stumbling block in the dis-
cussions. It minimises the risk of the kind of conﬁrmation bias and idiosyncratic interpretation
we engaged in the workshop. This way of using algorithms in enquiry was already fore-
shadowed in Dewey’s (1910) early work, in which he argued that quantitative tools of in-
duction should be thought of as imposing useful regulations of the conditions under which
observation takes place. They halt the mind’s tendency to be caught in past experiences.
Recently, Hayles (2014) made similar important arguments about the potential of delegating
speciﬁc aspects of the interpretative process to formal technical systems.
In our reimagined workshop, we could, for instance, have used a spatial autocorrelation algorithm
(such as Moran’s I) to draw data-driven boundaries with the outset in the formalised criteria agreed on in
Step 2. This would have been an instance of delegating our initial focus to an algorithm that could have
Koed Madsen
109

---

<!-- Page 17 -->

guided us—as a group—to discuss areas that we might not have turned to by ourselves. It could have
functioned as a regulatory device for, in Dewey’s words, ‘selecting the precise facts to which weight and
signiﬁcance shall attach’ (Dewey, 1910: 43). The fact that inductive algorithms require such selection to
be formalised puts useful constraints on enquiry. After agreeing on the premises of the formalisation, one
is bound to make sense of the consequences. This mode of enquiry reminds us of Peirce’s (1906)
description of diagramming reasoning, which involves letting one’s thinking guide through rule-bound
experiments, the consequences of which can then be discussed later (see also Stjernfeldt 2014).
Step 4. Engage in abductive sensemaking
The fourth step is to insist on the need to produce qualitative interpretations of the data that
are given weight and signiﬁcance by the co-produced algorithm. Induction only facilitates the
ground from which stories can be told – the ﬁnal interpretation cannot stem from the data.
Following Peirce, we could think of algorithms and the resulting maps as a scaffold for further
abductive reasoning, which would involve controlled hypothesising about why the patterns in
the data look as they do. Peirce emphasised that the practice of guessing should play a central
role in the abductive process (Tschaepe, 2014). However, he also argued that there is a nor-
mativity to guessing. Whereas hypothesising and guessing would and should be shaped by
people’s prior experiences, the fundamental aim would be to make sense of speciﬁc tangible
empirical patterns. In the epistemology of Peirce, abduction thus involves controlled and
piecemeal guessing, not associations running wild.
In our reimagined workshop, such an abductive moment could be achieved by using the
participants’ background knowledge about urban dynamics – and Copenhagen in particular – to
elaborate on the signiﬁcance of the areas identiﬁed through spatial autocorrelation. Away to do this
would have been to give the participants the task of digging deeper into these areas and telling a
story about their political diversity. In the spirit of Peirce, we could even ask the participants to work
with areas that they found especially surprising. Two things could have happened in that process.
One could be that the areas singled out were surprising but spawned meaningful stories and
hypotheses that would otherwise not have surfaced. Another would be that the areas were surprising
and not easy to make sense of. Designing such a session would mean that personal experience would
not be eliminated as an important feature but rather that it was designated a more restricted role as an
input to sensemaking rather than place selection. It would be used in tandem with the results of
induction but never allowed to roam free, as described above. The qualitative interpretations would
serve as a complementary role to the inductive techniques.
Step 5. Backcasting as experimental a priori
The ﬁfth step would then be to insist that the outcome of this complementary strategy was
followed by a critical evaluation of the formal operations that designated certain aspects of the
empirical ground as especially salient. Regardless of which of the two mentioned outcomes ends up
being the result of the complementary strategy, there is a beneﬁt to critically assessing the road that
led there. For instance, if the result was the development of meaningful narratives about aspects of
Copenhagen that were not previously seen as signiﬁcant by the participants, it would be relevant to
backcast the choices that led there. What was the ontology we inherited from the alien data source in
Step 1? What were the assumptions behind the operationalisations in Step 2? What kind of
worldview underpinned the inductive techniques in Step 3? Why did these choices lead to another
focus than we would otherwise have had? Does the relevance of this focus warrant revisiting the
assumptions that normally guide our empirical practices?
110
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 18 -->

This strategy of critically pondering the coherence between personal assumptions and the
consequences of procedures allows for the experimental a priori described above. It involves
critically assessing – and perhaps changing – some of the fundamental stipulations behind the
representations. This form of backcasting is also a way to adhere to Dewey’s (1929) argument that
critique must always involve a consciousness of the principles contained in the methods applied. As
they set the boundaries of how the world can be seen, it is of utmost importance to allow them to be
part of the experimental process of enquiry. In a sense, this notion of critique can be traced all the
way back to Kant, who was concerned with identifying the conditions of possibility for making
empirical claims about the world.
These are the types of critical questions with which Jeff and Alex engaged when they allowed
surprising patterns in the data to prompt a discussion about the ontology of urban space in the ﬁrst
vignette. As we saw, this discussion involved questioning the limits of working with a geographical
conception of proximity as well as a reﬂection on what a purely public conception of space hides
regarding the question of diversity. These types of critical reﬂections were the result of an ex-
perimental setup in which backcasting was deliberately built into the exercises. Designing for such
reﬂections is also a way of avoiding the risk of mistaking the data for the world and accepting that
streams of data do not come with clear patterns. As argued by Lewis, we structure data based on
pragmatic interests, and this structuring affords fruitful discussions about the values underpinning it.
Critical data practices stimulate this form for experimental a priori, which could ultimately lead to a
redesign of the semantic engines at the heart of our epistemic practices. As we have seen in the story
of Jeff and Alex, such engines do indeed shape the way we understand our challenges and distribute
agency to speciﬁc experts to solve them.
Concluding remarks
In this paper, I have argued that the computational turn presents us with a vague empirical world.
People engaged in empirical enquiry with digital methods deal with data that are multi-authored,
granular, relational and increasingly possible to treat with inductive algorithmic techniques.
Drawing on the philosophy of Kant, Peirce, Dewey and Lewis, I have tried to argue that this
situation carries distinct critical potentials. One of these potentials is to design processes of enquiry
and data experimentation that use the act of operationalisation as an engine for creating inter-
subjective clarity about the meaning of concepts. Another is to use algorithmic techniques to
stimulate a form of experimental a priori that ultimately involves a reassessment of some of the core
assumptions that shape the way we pose empirical problems. The vagueness of the empirical
situation is an avenue for creating intersubjective indices that carry the potential for recalibrating the
concepts we use to make sense of the world – a chance to experimentally revisit the way we ascribe
meaning to the world.
I illustrate this potential with selected interviews and ethnographic material from two years of
data experiments with GEHL architects. Faced with the task of using traces from Facebook as an
empirical source to produce a map of urban political diversity, the employees found themselves in
need of revisiting core assumptions about conceptions of urban space. The dissonance between
the notions of space in the ontology of the data from Facebook and the established ‘GEHL lens’
allowed for revisiting the fundamental assumptions underpinning the ways in which the urban space
can even be phrased as a problem of diversity. Rather than evaluating the epistemic quality of the
involved operationalisations with reference to their ‘external validity’ (Adcock and Collier, 2001),
I have argued that their critical potential lies in their potential to afford this sort of intersubjective
Koed Madsen
111

---

<!-- Page 19 -->

enquiry. Their obstructive character help slow down reasoning by enforcing suspended judgment
among the participants.
I presented this as an alternative to the tendency to think about the algorithmic processing of
data as something that is free of theory. The reason why the digital data landscape is interesting
is that it comes from an alien infrastructure and has the potential to disturb established in-
frastructures. As Dewey puts it in the opening quote, measurements and operationalisations are
tools for explication and meaning making. Rather than representing an opportunity to escape
theory and realise the empiricists’ dream of a production of knowledge freed of human bias,
inductive techniques have the potential to manifest surprising patterns that can serve as the
starting point for a process of controlled abductive hypothesising. This process can ultimately
spark reﬂections on the ontological stipulations that form the basis of practices of
representation.
Drawing on the experiments with GEHL, I argue that this critical potential cannot be realised
without deliberate design interventions. Therefore, I ended the paper by outlining ﬁve steps
involved in practicing this form of experimental a priori. The ﬁrst step is to deliberately seek alien
data sources that could generate empirical vagueness. The second step is to establish formal
operational rules that recalibrate the links between measures and values. The third step is to
delegate collective attention to the algorithm. Steps 2 and 3 enable people to have a shared point
of attention that is the outcome of explicit debates about the meaning of concepts. The fourth step
is to use this shared attention to engage in abductive sensemaking with roots in personal ex-
periences. This will lead to speciﬁc qualitative stories that may lead to more or less surprising and
meaningful stories. The ﬁfth and last step is to reﬂect on how those stories came to be. By
backcasting the results to the assumptions built into the data sources, operationalisations and
algorithmic procedures – and perhaps deciding to change them – the road is opened up for the
form of experimental a priori that I argue to be a central critical potential in digital methods.
Although I have used the case of GEHL to illustrate why this is a promising critical use of digital
methods, I would argue that the approach can productively be used in most other research areas as
well. In the contemporary digitised world, there are few empirical problems that do not lend
themselves to the iterative cycle illustrated in Figure 9. One example from another recent project in
our lab is a principal of a Danish school system who needed to understand pupils’ wellbeing. The
standardised measure was a survey with a series of more or less closed questions, but she actively
sought out an alien data source in the form of more than 200 pupils’ written assignments on the
topic. Through a discussion with representatives from the pupils’ board, she arrived at a way of
operationalising the themes brought up in the texts and delegated her attention to a topic modelling
algorithm. Sensemaking of the resulting topics was then abductively conducted with the pupils, and
the whole exercise led to critical reﬂections on the assumptions behind the surveys that have served
as the original scaffold for experiencing this phenomenon. The approach of experimental a priori
could similarly be used in various other empirical contexts.
I see this work on experimental a priori as continuing important work in digital STS that has,
during the last decade, engaged in discussions about how the digital reconﬁgures problem spaces
and how to design sprints to enable people to engage with the digital. The suggestion to think
about digital methods as experimental a priori focuses on the process of enquiry that gives birth
to the representational artefacts that are later circulated. This is a quite different take on critique
than the one emphasised by theoretical approaches that focus on the circulation, uptake, and
effects of the outputs of data projects (see e.g. Latour, 1986; D’Ignasio, Klein, 2020). Whereas
such approaches often conceptualise data and visualisations as tools of persuasion that can be
used to empower or marginalise speciﬁc worldviews, the kind of critique I propose here
112
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 20 -->

approaches them as epistemic tools that can guide thinking in critical or uncritical ways. This is a
perspective that not only has relevance for STS but also for the broader ﬁeld of digital and
computational humanities.
Declaration of conﬂicting interests
The author(s) declared no potential conﬂicts of interest with respect to the research, authorship, and/or
publication of this article.
Funding
The author(s) disclosed receipt of the following ﬁnancial support for the research, authorship, and/or pub-
lication of this article: This work was supported by the: Aalborg Universitet; Talent Funds
ORCID iD
Anders Koed Madsen https://orcid.org/0000-0003-2842-4908
Notes
1. What Peirce exactly meant by tangible is a debated issue. For instance, he entertained the idea that formal
thought-experiments could have a structure that made them clear and tangible enough for meaningful
intersubjective investigation (see e.g. Misak, C 2013 The American pragmatists. Oxford University Press).
However, a central aspect of his diagrammatical reasoning was the argument that schemata (such as formal
equations, maps or ﬂowcharts) are more accessible than mere words (Stjernfelt, F. 2014, Natural prop-
ositions: The actuality of Perices doctrine of Dicisigns, Docent Press, Boston). This makes them more
efﬁcient tools for moving thinking and inquiry critically forward.
2. Burke proposed addressing an operationalist strand of pragmatism to highlight the difference between the
version of pragmatism coined by Peirce and its subsequent development in the writings of William James.
Whereas Perice emphasised tangible effects as core to the pragmatic maxim, James promoted a more subjective
and psychological formulation of experience and effects. For instance, in ‘Varieties of Religious Experience’,
he argues for ‘the reality of the unseen’. His stance is that subjective experiences – such as religious epiphanies
and moments of hallucination – should be accepted as an indeﬁnable part of people’s inquiry that is impossible
to challenge on logical grounds. However, to those who experience them, they are convincing and prove to be
‘fertile wells’ for organising their life. This instrumentalist and coherentist test is what James sometimes
referred to as the ‘cash value’ of concepts. Pierce found that James’ version of pragmatism downplayed the
importance of tangibility and intersubjectivity to such an extent that he ultimately renamed his own position
‘pragmaticism’. A term he declared to be so ugly that James would not steal it once again. In this paper, I draw
on the Peircean version of pragmatism to emphasise the important role that operationalisation and formal
experiments play in the process of working with digital methods.
3. The steps in this ﬁgure came about through an analytic movement between the lessons learned in the experiment
with Jeff and Alex and the reading of pragmatist literature on principles of through and inquiry. It is thus a model
that has quite distinct theoretical roots while at the same time having been tested in concrete data practices.
References
Adcock R and Collier D (2001) Measurement validity: A shared standard for qualitative and quantitative
research. American Political Science Review 95: 529–546.
Agre P (1997) Toward a critical technical practice: lessons learned in trying to reform AI. In: G Bowker, S Star,
W Turner, et al. (eds), Bridging the great divide: Social Science, Technical Systems and Cooperative Work.
Koed Madsen
113

---

<!-- Page 21 -->

Alexander C (1968) A city is not a tree. Ekistics 139: 344–348.
Anderson C (2008) The end of theory: The data deluge makes the scientiﬁc method obsolete. Wired Magazine
16(7): 07–16.
Berry DM (2011) The computational turn: Thinking about the digital humanities. Culture machine, 12.
Benthall B (2016) Philosophy of computational social science. Cosmos and History: The Journal of Natural
and Social Philosophy, 12(2), 13–30.
Blok A (2020) Commentary: Why (and how to) experiment with digital social data? DASTS Engaging the Data
Moment. Special issue, 11(1).
Burke FT (2013) What Pragmatism Was. Bloomington, Indiana: Indiana University Press.
Dewey J (1910) How We Think, Lawrence, KS: Digireads. com Publishing.
Dewey J (1929) The Later Works of John Dewey, 1925 - 1953: 1929: The Quest for Certainty. Carbondale,
Illinois: Sounthern Illinois University Press.
Dewey J (1938) Logic: The Theory of Inquiry. NY USA: Henry Holt & Company, Inc.
GEHL studio SF (2015) Public Life Diversity Toolkit: A Prototype for Measuring Social Mixing and Economic
Integration in Public Space. West Bend, Wisconsin, USA: GEHL. Available August 5, 2021, at: https://
gehlinstitute.org/wp-content/uploads/2017/02/Gehl_PublicLifeDiversityToolkit_Pages-1.pdf
Gehl J (2011) Life between Buildings: Using Public Space. Washington, D.C., USA: Island press.
Gehl J and Svarre B (2013) How to Study Public Life. NY USA: Springer.
Hayles NK (2014) Cognition everywhere: The rise of the cognitive nonconscious and the costs of con-
sciousness. New Literary History 45(2): 199–220.
Jensen TE, Birkbak A, Madsen AK, et al. (2021) Participatory data design: Acting in a digital world. In: T
Zuiderent-Jerak and G Downey (eds), Making and Doing STS. Cambridge, Massachusetts: MIT Press.
Kant I (2007) Kritik Af Den Rene Fornuft. Denmark: Det lille forlag.
Kitchin R (2014) The data revolution: Big data, open data, data infrastructures and their consequences. Sage.
Lewis CI (1923) A pragmatic conception of the a priori. In: The Pragmatism Reader - from Pierce to the
Present. Princeton, New Jersey: Princeton University Press, pp. 166–173.
Lury C (2020) Problem Spaces: How and Why Methodology Matters. Hoboken, New Jersey, USA: John Wiley
& Sons.
Madsen AK (2015) Tracing Data—Paying Attention. Making Things Valuable (eds Kornberger et al.), p.
257–278, Oxford University Press.
Madsen, AK (2022) Do You Live in a Bubble? Designing Critical Diversity Metrics to Intervene in Urban
Cartography. Projections, p. 257.
Madsen AK and Munk AK (2019) Experiments with a data-public: Moving digital methods into critical
proximity with political practice. Big Data & Society 6(1): 2053951718825357.
Marres N (2005) Issues spark a public into being: A key but often forgotten point of the Lippmann-Dewey
debate. In: Making Things Public: Atmospheres of Democracy: MIT Press, pp. 208–217.
Marres N (2012) The redistribution of methods: on intervention in digital social research, broadly conceived.
The Sociological Review 60: 139–165.
Marres N and Stark D (2020) Put to the test: For a new sociology of testing. The British Journal of Sociology
71(3): 423–443.
Moats D and Seaver N (2019) You Social Scientists Love Mind Games”: Experimenting in the “divide”
between data science and critical algorithm studies. Big Data & Society 6(1): 2053951719833404.
Munk A. K., Madsen A. K., and Jacomy M. (2019) Thinking through the Databody. In: ˚A M¨akitalo, T.
Nicewonger, and M. Elam (eds), Designs for Experimentation and Inquiry: Approaching Learning and
Knowing in Digital Transformation. Oxfordshire UK: Routledge, p. 110.
114
Convergence: The International Journal of Research into New Media Technologies 30(1)

---

<!-- Page 22 -->

Munk AK, Meunier A, and Venturini T (2019) Data sprints: A collaborative format in digital controversy
mapping. Digital-STS: A Field Guide for Science & Technology Studies: 472. DOI. 10.1515/
9780691190600-032.
Nelson LK (2020) Computational grounded theory: A methodological framework: Sociological Methods &
Research, 49(1), 3–42.
Neff G and Stark D (2004) Permanently beta. Society Online: The Internet in Context 173: 188.
Peirce CS (1906) Prolegomena to an apology for pragmaticism. The Monist 16(4): 492–546.
Peirce CS (1877) The ﬁxation of belief. In: RB Talisse and SF Aikin (eds), The Pragmatism Reader: From
Pierce Through The Present. Princeton, New Jersey: Princeton University Press.
Peirce CS (1878) How to make our ideas clear. In: RB Talisse and SF Aikin (eds), The pragmatism reader:
From Pierce through the present. Princeton, New Jersey: Princeton University Press.
Rogers R (2013) Digital Methods. Cambridge, Massachusetts: MIT press.
Stark D (2011) The sense of dissonance. The Sense of Dissonance. Princeton, New Jersey: Princeton University
Press.
Stjernfelt F (2014) Natural propositions: The actuality of Perices doctrine of Dicisigns, Docent Press, Boston.
Tschaepe M (2014) Guessing and abduction. Transactions of the Charles S. Peirce Society: A Quarterly
Journal in American Philosophy 50(1): 115–138.
Koed Madsen
115