---
title: EPAM
---
**[Home](Home "Home") * [Knowledge](Knowledge "Knowledge") * [Cognition](Cognition "Cognition") * EPAM**

[](File:Epamnet.jpg) EPAM discrimination net <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**EPAM**, (Elementary Perceiver and Memorizer)

an early computer model of [rote learning](https://en.wikipedia.org/wiki/Rote_learning) by the method of [paired associates](https://en.wikipedia.org/wiki/Pair_by_association), first conceived by [Herbert Simon](Herbert_Simon "Herbert Simon") and [Allen Newell](Allen_Newell "Allen Newell") during their early conception about computer simulation of [cognitive](Cognition "Cognition") processes in the 50s <a id="cite-note-2" href="#cite-ref-2">[2]</a> , implemented as computer program by [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") in the late 50s in [IPL-V](https://en.wikipedia.org/wiki/Information_Processing_Language) for the [IBM 704](IBM_704 "IBM 704") and [IBM 7090](IBM_7090 "IBM 7090"), as topic of his Ph.D. thesis at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"). In terms of [psychology](index.php?title=Psychology&action=edit&redlink=1 "Psychology (page does not exist)") and [behaviorism](https://en.wikipedia.org/wiki/Behaviorism) EPAM associates responses with external [stimuli](https://en.wikipedia.org/wiki/Stimulus_%28psychology%29), quite similar to [classical conditioning](https://en.wikipedia.org/wiki/Classical_conditioning).

## Contents

- [1 Learning](#learning)
- [2 EPAM in Chess](#epam-in-chess)
- [3 The EPAM Simulation](#the-epam-simulation)
- [4 MAPP](#mapp)
- [5 CHREST](#chrest)
- [6 See also](#see-also)
- [7 Publicatons](#publicatons)
  - [7.1 1959](#1959)
  - [7.2 1960 ...](#1960-...)
  - [7.3 1970 ...](#1970-...)
  - [7.4 1980 ...](#1980-...)
  - [7.5 1990 ...](#1990-...)
  - [7.6 2000 ...](#2000-...)
- [8 External Links](#external-links)
- [9 References](#references)

## Learning

EPAM [learns](Learning "Learning") by growing a [discrimination](https://en.wikipedia.org/wiki/Discrimination_%28disambiguation%29#Science_and_research) [net](https://en.wikipedia.org/wiki/Net_%28mathematics%29) kept in long-term [memory](Memory "Memory"), a [tree-like structure](https://en.wikipedia.org/wiki/Tree_%28data_structure%29) whose [nodes](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29) contain tests that may be applied to objects that have been described as bundles of [perceptual](https://en.wikipedia.org/wiki/Perception) features. In EPAM III, introduced in 1964 <a id="cite-note-3" href="#cite-ref-3">[3]</a> , the test nodes were generalized as n-ary switch instead of binary of EPAM II. When a familiar object is perceived, it is recognized by being sorted through the EPAM net. At the terminal nodes of the EPAM net, partial "images" are stored, also in the form of feature bundles of the objects sorted to the respective terminals, together with other information about the objects <a id="cite-note-4" href="#cite-ref-4">[4]</a> , such as [cue](https://en.wikipedia.org/wiki/Sensory_cue) information, used to feed back into the net [recursively](Recursion "Recursion") .

## EPAM in Chess

Thus, EPAM has a recursive structure. Any object, once familiarized and incorporated into the net, can itself serve as a perceptual feature of a more complex object. For instance in the domain of chess, once the various types of chess pieces and their proximity become familiarized, these can become features of more complex configurations, i.e. a "fianchettoed castled Black King's position". Once familiarized, such a complex can, in turn, serve as a perceptual feature of a still more complex pattern, finally the entire chess position.

## The EPAM Simulation

Excerpt from *Elementary Perceiver and Memorizer: Review of Experiments* <a id="cite-note-5" href="#cite-ref-5">[5]</a> :
The EPAM processes perform the following four principal functions:

1. Recognize an external stimulus as one about which some information has already been memorized
1. Add new stimulus items to the memory by building discriminations (tests) that allow the new item to be distinguished from stimuli previously learned
1. Associate (internally) two stored items, say x and y, by storing with x some cue information about y
1. Respond to an external stimulus X with a response, Y, by retrieving the cue to the response, and then retrieving the response using the cue

Thus, EPAM has two performance processes, enabling It to respond using material already learned: the discrimination process (1), which recognizes the stimulus, and the response process (4), which finds the appropriate response associated with the stimulus and produces it. EPAM also has two learning processes: the discrimination learning process (2), which elaborates the structure of discrimination tests it applies to stimuli, and the association learning process (3), which associates response cues with stimuli.

The central "memory structure, which the performance processes use and the learning processes construct, is the discrimination net. It is a tree-like nexus of associations at whose terminal nodes are stored Images of encodings of external stimuli. At the non-terminal nodes of the net are stored tests which examine particular bits of the encodings. The image of a stimulus is retrieved by sorting the encoding of the stimulus down through the tests of the net to the appropriate terminal. In learning a set of stimuli, the net is grown to a size that is Just large enough (roughly) to discriminate among the different stimuli that have been presented to the system.

Association of a response, y, to a stimulus, x, is accomplished by storing a small amount of the information about y (an incomplete cue image of y) along with the image of x. The system determines by trial and error how much information must be stored as a cue to retrieve the response from the net when the association is made.

## MAPP

EPAM was influential in formalizing the concept of [chunking](Chunking "Chunking"). It was used in the [MAPP](MAPP "MAPP") (Memory-aided Pattern Perceiver) program by [Simon](Herbert_Simon "Herbert Simon") and [Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") <a id="cite-note-6" href="#cite-ref-6">[6]</a> to simulate the [chess board reconstruction task](William_Chase#Perception "William Chase"). An EPAM net was stimulated by the piece [fixation](https://en.wikipedia.org/wiki/Fixation_%28visual%29) of the [eye movement](Eye_Movements "Eye Movements") simulation program [Perceiver](Perceiver "Perceiver"), to recognize cluster of pieces surrounding the fixated piece as a familar chunk. In the perception phase up to seven symbols designating these chunks were stored in short-term [memory](Memory "Memory"). In the reconstruction phase, the EPAM net was used to decode the symbols held in short-term memory into locational information for each of the pieces in a chunk. In various experiments, MAPP was able to reconstruct positions with 73% accuracy <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>

[](http://snitkof.com/cg156/chesschunkingtheory.php)
A schematic representation of the principle components of MAPP shows the learning and performance

processes used to reconstruct a chess position <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## CHREST

The EPAM concept was further influential for [Fernand Gobet's](Fernand_Gobet "Fernand Gobet") [CHREST](CHREST "CHREST") (Chunk Hierarchy and REtrieval STructures) architecture, applied in Gobet's and [Jansen's](Peter_Jansen "Peter Jansen") [pattern learning](index.php?title=Pattern_Learning&action=edit&redlink=1 "Pattern Learning (page does not exist)") chess program [CHUMP](CHUMP "CHUMP") <a id="cite-note-10" href="#cite-ref-10">[10]</a> .

## See also

- [CHREST](CHREST "CHREST")
- [CHUMP](CHUMP "CHUMP")
- [Chunking](Chunking "Chunking")
- [Learning](Learning "Learning")
- [MAPP](MAPP "MAPP")
- [Neural Networks](Neural_Networks "Neural Networks")
- [Pattern Recognition](Pattern_Recognition "Pattern Recognition")

## Publicatons

## 1959

- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1959**). *[An Information Processing Theory of Verbal Learning](http://www.rand.org/pubs/papers/P1817.html)*. [RAND Paper](https://en.wikipedia.org/wiki/RAND_Corporation)

## 1960 ...

- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1960**). *Information Theories of Human Verbal Learning*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), advisor [Herbert Simon](Herbert_Simon "Herbert Simon")
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1961**). *[The Simulation of Verbal Learning Behavior](http://dl.acm.org/citation.cfm?id=1460704)*. Proceedings Western Joint Conference, Vol. 19
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1961**). *Performance of a Reading Task by an Elementary Perceiving and Memorizing Program*. [RAND Paper](https://en.wikipedia.org/wiki/RAND_Corporation), [pdf](http://www.rand.org/content/dam/rand/pubs/papers/2008/P2358.pdf)
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1961**). *[Forgetting in an association memory](http://dl.acm.org/citation.cfm?id=800029.808503&coll=DL&dl=GUIDE&CFID=111335796&CFTOKEN=62851440)*. ACM '61, [pdf](http://www.rand.org/content/dam/rand/pubs/papers/2008/P2311.pdf)
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1962**). *A Theory of the Serial Position Effect*. [British Journal of Psychology](https://en.wikipedia.org/wiki/British_Journal_of_Psychology#Journals), Vol. 53, 307-32, [pdf](http://www.rand.org/pubs/papers/2008/P2375.pdf)
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1963**). *[Elementary Perceiver and Memorizer: Review of Experiments](https://saltworks.stanford.edu/catalog/druid:sf355sf7850)*. in Symposium on Simulation Models
- [Herbert Simon](Herbert_Simon "Herbert Simon"), [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1964**). *An Information-processing Theory of Some Effects of Similarity, Familiarization, and Meaningfulness in Verbal Learning*. Journal of Verbal Learning and Verbal Behavior, Vol. 3, No. 5, [pdf](https://saltworks.stanford.edu/assets/zp668jb3733.pdf)

## 1970 ...

- [Herbert Simon](Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *A Simulation of Memory for Chess Positions*. [Cognitive Psychology](http://www.journals.elsevier.com/cognitive-psychology/), Vol. 5
- [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
- [Herbert Simon](Herbert_Simon "Herbert Simon") (**1974**). *How big is a chunk*? [Science](https://en.wikipedia.org/wiki/Science_%28journal%29), Vol. 183, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44527)

## 1980 ...

- [Lawrence W. Barsalou](https://en.wikipedia.org/wiki/Lawrence_W._Barsalou), [Gordon H. Bower](https://en.wikipedia.org/wiki/Gordon_H._Bower) (**1984**). *[Discrimination Nets as Psychological Models](http://onlinelibrary.wiley.com/doi/10.1207/s15516709cog0801_1/abstract)*. [Cognitive Science](https://en.wikipedia.org/wiki/Cognitive_Science_Society), Vol. 8, No. 1 <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1984**). *[EPAMlike models of recognition and learning](http://www.sciencedirect.com/science/article/pii/S0364021384800051)*. [Cognitive Science](https://en.wikipedia.org/wiki/Cognitive_Science_Society), Vol. 8, 305-336, [pdf](http://csjarchive.cogsci.rpi.edu/1984v08/i04/p0305p0336/MAIN.PDF)

## 1990 ...

- [Howard B. Richman](index.php?title=Howard_B._Richman&action=edit&redlink=1 "Howard B. Richman (page does not exist)"), [James J. Staszewski](index.php?title=James_J._Staszewski&action=edit&redlink=1 "James J. Staszewski (page does not exist)"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1995**). *[Simulation of Expert Memory with EPAM IV](http://psycnet.apa.org/journals/rev/102/2/305/)*. Psychological Review, Vol. 102
- [Fernand Gobet](Fernand_Gobet "Fernand Gobet"), [Howard B. Richman](index.php?title=Howard_B._Richman&action=edit&redlink=1 "Howard B. Richman (page does not exist)"), [James J. Staszewski](index.php?title=James_J._Staszewski&action=edit&redlink=1 "James J. Staszewski (page does not exist)"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1997**). *Goals, Representations, and Strategies in a Concept Attainment Task: The EPAM model*. The Psychology of Learning and Motivation, Vol. 37, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=34259)

## 2000 ...

- [Fernand Gobet](Fernand_Gobet "Fernand Gobet"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**2000**). *[Five Seconds or Sixty? Presentation Time in Expert Memory](http://onlinelibrary.wiley.com/doi/10.1207/s15516709cog2404_4/abstract)*. [Cognitive Science](https://en.wikipedia.org/wiki/Cognitive_Science_Society), Vol. 24, No. 4
- [Fernand Gobet](Fernand_Gobet "Fernand Gobet"), [Peter Lane](index.php?title=Peter_Lane&action=edit&redlink=1 "Peter Lane (page does not exist)"), [Steve Croker](http://my.ilstu.edu/~sfcroke/), [Peter C-H. Cheng](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/c/Cheng:Peter_C=_H=.html), [Gary Jones](http://www.ntu.ac.uk/apps/Profiles/53951-1-4/Dr_Gary_Jones.aspx), [Iain Oliver](http://ijosblog.blogspot.de/2012_02_01_archive.html), [Julian M. Pine](http://www.liv.ac.uk/psychology-health-and-society/staff/julian-pine/) (**2001**). *[Chunking mechanisms in human learning](http://www.sciencedirect.com/science/article/pii/S1364661300016624)*. Trends in Cognitive Sciences, Vol. 5, No. 6
- [Fernand Gobet](Fernand_Gobet "Fernand Gobet") (**2005**). *[Chunking Models of Expertise: Implications for Education](http://onlinelibrary.wiley.com/doi/10.1002/acp.1110/abstract)*. Applied Cognitive Psychology, Vol. 19, No. 2

## External Links

- [EPAM from Wikipedia](https://en.wikipedia.org/wiki/EPAM)
- [EPAM | CHREST](http://www.chrest.info/epam.html)
- [Expertise in Memory - EPAM Model](http://snitkof.com/cg156/epam.php) by [Victor Long](http://snitkof.com/cg156/contact.php), [Chandra Singh](http://snitkof.com/cg156/contact.php) and [David Snitkof](https://www.linkedin.com/in/davidsnitkof), [Brown University](https://en.wikipedia.org/wiki/Brown_University)
- [Expertise in Memory - Evidence for Chunking Theory](http://snitkof.com/cg156/chesschunkingtheory.php) by [Victor Long](http://snitkof.com/cg156/contact.php), [Chandra Singh](http://snitkof.com/cg156/contact.php) and [David Snitkof](https://www.linkedin.com/in/davidsnitkof), [Brown University](https://en.wikipedia.org/wiki/Brown_University)
- [Agnes Obel](Category:Agnes_Obel "Category:Agnes Obel") - [Familiar](https://en.wikipedia.org/wiki/Agnes_Obel#cite_ref-41), [Alcaline](<https://fr.wikipedia.org/wiki/Alcaline_(%C3%A9mission_de_t%C3%A9l%C3%A9vision)>), November 07, 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

featuring [Kristina Koropecki](https://www.couchsurfing.com/people/kriskar), [Charlotte Danhier](https://mobile.twitter.com/agnesobel_org/status/637306150413803524), [Catherine De Biasio](https://www.discogs.com/de/artist/1453695-Catherine-De-Biasio)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A typical EPAM discrimination net, Image from [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1963**). *[Elementary Perceiver and Memorizer: Review of Experiments](https://saltworks.stanford.edu/catalog/druid:sf355sf7850)*. in Symposium on Simulation Models, pp. 103
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1959**). *[An Information Processing Theory of Verbal Learning](http://www.rand.org/pubs/papers/P1817.html)*. [RAND Paper](https://en.wikipedia.org/wiki/RAND_Corporation)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") (**1964**). *An Information-processing Theory of Some Effects of Similarity, Familiarization, and Meaningfulness in Verbal Learning*. Journal of Verbal Learning and Verbal Behavior, Vol. 3, No. 5, [pdf](https://saltworks.stanford.edu/assets/zp668jb3733.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1963**). *[Elementary Perceiver and Memorizer: Review of Experiments](https://saltworks.stanford.edu/catalog/druid:sf355sf7850)*. in Symposium on Simulation Models
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *A Simulation of Memory for Chess Positions*. Cognitive Psychology, Vol. 5, pp. 29-46, reprinted in [Herbert Simon](Herbert_Simon "Herbert Simon") (**1979**). *[Models of Thought](http://yalepress.yale.edu/yupbooks/book.asp?isbn=9780300024326)*. [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Herbert Simon](Herbert_Simon "Herbert Simon"), [Kevin J. Gilmartin](Kevin_J._Gilmartin "Kevin J. Gilmartin") (**1973**). *A Simulation of Memory for Chess Positions*. Cognitive Psychology, Vol. 5, pp. 29-46
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Michael George](index.php?title=Michael_George&action=edit&redlink=1 "Michael George (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1990**). *[Chunking for Experience](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.2766)*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~jonathan/publications/ai_publications/mach.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> Image from [Expertise in Memory - Evidence for Chunking Theory](http://snitkof.com/cg156/chesschunkingtheory.php) by [Victor Long](http://snitkof.com/cg156/contact.php), [Chandra Singh](http://snitkof.com/cg156/contact.php) and [David Snitkof](https://www.linkedin.com/in/davidsnitkof), [Brown University](https://en.wikipedia.org/wiki/Brown_University), see also Figure 6 in [Herbert Simon](Herbert_Simon "Herbert Simon"), [William Chase](William_Chase "William Chase") (**1973**). *Skill in Chess*. [American Scientist](https://en.wikipedia.org/wiki/American_Scientist), Vol. 61, No. 4, pp. 401, reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**) *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, [pdf](http://digitalcollections.library.cmu.edu/awweb/awarchive?type=file&item=44582)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Fernand Gobet](Fernand_Gobet "Fernand Gobet"), [Peter Jansen](Peter_Jansen "Peter Jansen") (**1994**). *[Towards a Chess Program Based on a Model of Human Memory](http://people.brunel.ac.uk/~hsstffg/abstracts/chess_program.html).* [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Pandemonium architecture from Wikipedia](https://en.wikipedia.org/wiki/Pandemonium_architecture)

**[Up one Level](Cognition "Cognition")**

