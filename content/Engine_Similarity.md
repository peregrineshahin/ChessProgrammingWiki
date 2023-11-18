---
title: Engine Similarity
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Similarity**

\[ A [dendrogram](https://en.wikipedia.org/wiki/Dendrogram) of the [Tree of Life](https://en.wikipedia.org/wiki/Tree_of_life) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Engine Similarity**,

a loosely defined relation between (two) chess engines concerning their positional playing style, therefor mostly dependent on their [evaluation](Evaluation "Evaluation") features and weights.
One approach to assess engine similarity is to [count](https://en.wikipedia.org/wiki/Similarity_measure) how often these engines agree with the same move after a shallow [search](Search "Search")
over a set of carefully selected, quiet [test positions](Test-Positions "Test-Positions") with apparently several possible best moves - another, in **k-best** mode, how often they propose the same ranking of k moves.
A relative high similarity measure between two engines <a id="cite-note-2" href="#cite-ref-2">[2]</a> could be a symptom of using similar evaluation ideas, features and weights, along with [automated tuning](Automated_Tuning "Automated Tuning") (or trainig), or even code copying aka [cloning](Category:Clone "Category:Clone").
Similarity testing is intended as first automated "[screening](<https://en.wikipedia.org/wiki/Screening_(medicine)>)" to trigger further investigations in case moves are too similar.

## Similarity Testers

In December 2010, [Don Dailey](Don_Dailey "Don Dailey") published **SIM03** to test the similary with a set of [UCI](UCI "UCI") compliant engines with **8238** in-build positions - still freely available from the [Komodo](Komodo "Komodo") site <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
A pair of different chess engines could then be compared for similarity by matching up and counting the number of positions for which each engine chose the same move.
**SIMEX** is a more user friendly successor by [Ed Schröder](Ed_Schroder "Ed Schroder") <a id="cite-note-4" href="#cite-ref-4">[4]</a> using external [EPD](Extended_Position_Description "Extended Position Description")-files.
Overall similarity of multiple engines may be visualized as [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering) [dendrogram](https://en.wikipedia.org/wiki/Dendrogram) <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## See also

- [Category:Clone](Category:Clone "Category:Clone")
- [Category:Derivative](Category:Derivative "Category:Derivative")
- [ICGA Investigations](ICGA_Investigations "ICGA Investigations")
- [Engine Testing](Engine_Testing "Engine Testing")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Playing Strength](Playing_Strength "Playing Strength")

## Publications

- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1997**). *On the k-best Mode in Computer Chess: Measuring the Similarity of Move Proposals.* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
- [Mark Levene](Mark_Levene "Mark Levene"), [Judit Bar-Ilan](Judit_Bar-Ilan "Judit Bar-Ilan") (**2005**). *[Comparing Move Choices of Chess Search Engines](https://www.researchgate.net/publication/220174440_Comparing_Move_Choices_of_Chess_Search_Engines)*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal"), [pdf](http://www.dcs.bbk.ac.uk/~mark/download/fritz_junior_icga.pdf)
- [Paolo Ciancarini](Paolo_Ciancarini "Paolo Ciancarini"), [Gian Piero Favini](index.php?title=Gian_Piero_Favini&action=edit&redlink=1 "Gian Piero Favini (page does not exist)") (**2009**). *[Detecting clones in game-playing software](https://www.sciencedirect.com/science/article/pii/S1875952109000020)*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 1, No. 1
- [Don Dailey](Don_Dailey "Don Dailey"), [Adam Hair](Adam_Hair "Adam Hair"), [Mark Watkins](Mark_Watkins "Mark Watkins") (**2014**). *[Move Similarity Analysis in Chess Programs](http://www.sciencedirect.com/science/article/pii/S1875952113000177)*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 5, No. 3, [preprint as pdf](http://magma.maths.usyd.edu.au/~watkins/papers/DHW.pdf) <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## Forum Posts

## 1999

- [Chess program similarity experiment](https://www.stmintz.com/ccc/index.php?id=40708) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), January 24, 1999
- [This test is not scientific!](https://www.stmintz.com/ccc/index.php?id=40940) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 26, 1999

## [Re: This test is not scientific!](https://www.stmintz.com/ccc/index.php?id=40948) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 26, 1999 [Comparing Bionic-Impakt vs Bionic](https://www.stmintz.com/ccc/index.php?id=41059) by [Albrecht Heeffer](Albrecht_Heeffer "Albrecht Heeffer"), [CCC](CCC "CCC"), January 27, 1999 » [Bionic Impakt](Bionic_Impakt "Bionic Impakt"), [Bionic](Bionic "Bionic") 2000 ...

- [question to vas on similarity of rybka 1.0 to fruit](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=6772) by duncan, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2008

## 2010 ...

- [Similarity Detector Available](http://www.talkchess.com/forum/viewtopic.php?t=37308) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 26, 2010
- [Cluster analysis of similarity test](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=37381) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 31, 2010
- [Similarity testing for source code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=38086) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), February 16, 2011
- [Pairwise Analysis of Chess Engine Move Selections](http://www.talkchess.com/forum/viewtopic.php?t=38772) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 17, 2011
- [Fritz and Naum shown as Rybka/Strelka clones](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=40795) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC") (Engine Origins), October 17, 2011
- [Pairwise Analysis of Chess Engine Move Selections Revisited](http://www.talkchess.com/forum/viewtopic.php?t=42737) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), March 04, 2012
- [Similarity tool myth - debunked](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=44874) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), August 23, 2012
- [Fritz 11](http://www.open-chess.org/viewtopic.php?f=5&t=2531) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 10, 2013

## 2015 ...

- [Similarity test](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=55066) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), January 24, 2015 » [Cheng](Cheng "Cheng")
- [Similarity test for Capivara > version 0.0.8 available?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60012) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 01, 2016 » [Capivara](Capivara "Capivara")
- [New Similarity Dendrogram](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=62364) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 03, 2016 (Images broken links)
- [Experiment 11 - Similarity between the top engines back then and now](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70197) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 14, 2019
- [How to measure overall similarity](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70390) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), April 02, 2019
- [Why all Lc0 runs result in such similarity of quiet moves selection?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70633) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 01, 2019
- [Similarity tester - 2nd generation - BETA](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71497) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 09, 2019
- [What the heck happens here?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71610) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 20, 2019
- [SIMEX 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71709) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 01, 2019
- [Similarity Report 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71892) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC") (Engine Origins), September 23, 2019

## 2020 ...

- [Maybe not the best diversity of strongest chess engines under development](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75797) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 14, 2020 » [NNUE](NNUE "NNUE")
- [NNUE Research Project](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76833) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 10, 2021 » [NNUE](NNUE "NNUE")
- [Simex including NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76840) by jjoshua2, [CCC](CCC "CCC"), March 11, 2021 » [NNUE](NNUE "NNUE")

## External Links

## Chess Engines

- [Komodo Chess Engine - Official Site](https://komodochess.com/downloads.htm) with Similary tester version 03 download
- [Similary tester 2nd generation](http://rebel13.nl/misc/simex.html) (SIMEX) by [Ed Schröder](Ed_Schroder "Ed Schroder")
- [Similarity Report 2019](http://rebel13.nl/misc/sim2019.html) by [Ed Schröder](Ed_Schroder "Ed Schroder")
- [nnue | Home of the Dutch Rebel](http://rebel13.nl/home/nnue.html) by [Ed Schröder](Ed_Schroder "Ed Schroder") » [NNUE](NNUE "NNUE")
- [GitHub - fsmosca/Similarity-Dendrogram: Plot dendrogram on chess engines similarity](https://github.com/fsmosca/Similarity-Dendrogram) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca")

## Misc

- [Similarity from Wikipedia](https://en.wikipedia.org/wiki/Similarity)
- [Similarity (geometry) from Wikipedia](<https://en.wikipedia.org/wiki/Similarity_(geometry)>)
- [Lexical similarity from Wikipedia](https://en.wikipedia.org/wiki/Lexical_similarity)
- [Semantic similarity from Wikipedia](https://en.wikipedia.org/wiki/Semantic_similarity)
- [Structural similarity from Wikipedia](https://en.wikipedia.org/wiki/Structural_similarity)
- [Similarity measure from Wikipedia](https://en.wikipedia.org/wiki/Similarity_measure)
- [Dendrogram from Wikipedia](https://en.wikipedia.org/wiki/Dendrogram)
- [Hierarchical clustering from Wikipedia](https://en.wikipedia.org/wiki/Hierarchical_clustering)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a>
   A [phylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree) of [living things](https://en.wikipedia.org/wiki/Life), based on [RNA](https://en.wikipedia.org/wiki/RNA) data and proposed by [Carl Woese](https://en.wikipedia.org/wiki/Carl_Woese),
   showing the separation of [bacteria](https://en.wikipedia.org/wiki/Bacteria), [archaea](https://en.wikipedia.org/wiki/Archaea), and [eukaryotes](https://en.wikipedia.org/wiki/Eukaryote).
   Trees constructed with other genes are generally similar, although they may place some early-branching groups very differently, thanks to [long branch attraction](https://en.wikipedia.org/wiki/Long_branch_attraction). The exact relationships of the three domains are still being debated, as is the position of the root of the tree. It has also been suggested that due to [lateral gene transfer](https://en.wikipedia.org/wiki/Horizontal_gene_transfer), a tree may not be the best representation of the genetic relationships of all organisms. For instance some genetic evidence suggests that eukaryotes evolved from the union of some bacteria and archaea (one becoming an [organelle](https://en.wikipedia.org/wiki/Organelle) and the other the main [cell](<https://en.wikipedia.org/wiki/Cell_(biology)>)).
   Autor: Eric Gaba, September 2006, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> i.e. > 65% in SIM03
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Komodo Chess Engine - Official Site](https://komodochess.com/downloads.htm) with Similary tester version 03 download
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [SIMEX 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71709) provided by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 01, 2019
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [How to measure overall similarity](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70390) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), April 02, 2019
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Pairwise Analysis of Chess Engine Move Selections](http://www.talkchess.com/forum/viewtopic.php?t=38772) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 17, 2011

**[Up one Level](Engines "Engines")**

