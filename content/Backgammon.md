---
title: Backgammon
---
**[Home](Home "Home") * [Games](Games "Games") * Backgammon**

\[ A Backgammon Set <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Backgammon**,

a turn-based two-player [tables](https://en.wikipedia.org/wiki/Tables_%28board_game%29) board game of [chance](https://en.wikipedia.org/wiki/Game_of_chance) and strategy with 15 checkers each on a board of 24 spaces or points. One moves according to rolls of a pair of dice, trying to bring own checkers home and bear them off before the opponent does <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Opponent checkers can be "hit" and returned to the start.

## Computer Backgammon

Backgammon programs were pioneered in the late 70s by [Hans Berliner](Hans_Berliner "Hans Berliner") with focus on [smooth evaluation](Tapered_Eval "Tapered Eval"), and by [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") from the late 80s, who successfully applied [Neural Networks](Neural_Networks "Neural Networks") and [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning") to his Backgammon playing programs. Computer backgammon is regularly played at [Computer Olympiads](Computer_Olympiad "Computer Olympiad"), organized by the [ICGA](ICGA "ICGA") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## [Computer Olympiads](Computer_Olympiad "Computer Olympiad")

- [1st Computer Olympiad, London 1989](1st_Computer_Olympiad#Backgammon "1st Computer Olympiad")
- [2nd Computer Olympiad, London 1990](2nd_Computer_Olympiad#Backgammon "2nd Computer Olympiad")
- [4th Computer Olympiad, London 1992](4th_Computer_Olympiad#Backgammon "4th Computer Olympiad")
- [7th Computer Olympiad, Maastricht 2002](7th_Computer_Olympiad#Backgammon "7th Computer Olympiad")
- [8th Computer Olympiad, Graz 2003](8th_Computer_Olympiad#Backgammon "8th Computer Olympiad")
- [11th Computer Olympiad, Turin 2006](11th_Computer_Olympiad#Backgammon "11th Computer Olympiad")
- [12th Computer Olympiad, Amsterdam 2007](12th_Computer_Olympiad#Backgammon "12th Computer Olympiad")
- [16th Computer Olympiad, Tilburg 2011](16th_Computer_Olympiad#Backgammon "16th Computer Olympiad")
- [18th Computer Olympiad, Leiden 2015](18th_Computer_Olympiad#Backgammon "18th Computer Olympiad")
- [19th Computer Olympiad, Leiden 2016](19th_Computer_Olympiad#Backgammon "19th Computer Olympiad")

## Photos

[](https://icga.leidenuniv.nl/?page_id=1467)
[18th Computer Olympiad 2015](18th_Computer_Olympiad#Backgammon "18th Computer Olympiad"), Backgammon medalists: [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (Bronze for [BGBlitz](https://www.game-ai-forum.org/icga-tournaments/program.php?id=63)),\
[Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)") (Gold for [Palamedes](https://www.game-ai-forum.org/icga-tournaments/program.php?id=712)), and [Nardy Pillards](index.php?title=Nardy_Pillards&action=edit&redlink=1 "Nardy Pillards (page does not exist)") (Silver for [GNU Backgammon](https://www.game-ai-forum.org/icga-tournaments/program.php?id=62)) <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Evaluation

In the late 70s at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [Hans Berliner](Hans_Berliner "Hans Berliner") developed the Backgammon playing program **BKG 9.8** for the [PDP-10](PDP-10 "PDP-10") to research the principles of [evaluation](Evaluation "Evaluation") for another game than chess with a much higher [branching factor](Branching_Factor "Branching Factor") of more than 800 at every node <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Early versions of BKG played badly even against weak players, but Berliner noticed that its critical mistakes were always at transitions apparently due to [evaluation discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity"). He applied principles of [fuzzy logic](https://en.wikipedia.org/wiki/Fuzzy_logic) to [smooth out](Tapered_Eval "Tapered Eval") the transition between phases, and by July 1979, BKG 9.8 was strong enough to play against the ruling world champion [Luigi Villa](https://en.wikipedia.org/wiki/Luigi_Villa). It won the match 7–1, becoming the first computer program to defeat a world champion in any game. Berliner states that the victory was largely a matter of luck, as the computer received more favorable dice rolls <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Learning

In the late 80s, [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") researcher [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") pioneered in applying [Neural Networks](Neural_Networks "Neural Networks") to Backgammon - first within his program [Neurogammon](https://en.wikipedia.org/wiki/Neurogammon), which won the Gold medal at the [1st Computer Olympiad](1st_Computer_Olympiad#Backgammon "1st Computer Olympiad") 1989 - and further improved by *TD-Lambda* based [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning") within [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Publications

## 1977 ...

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *BKG - A Program that Plays Backgammon*. Technical Report, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *[Experiences in Evaluation with BKG, a Program That Plays Backgammon](http://www.bkgm.com/articles/Berliner/ExperiencesInEvaluationWithBKG/index.html)*. [IJCAI, 1977](Conferences#IJCAI1977 "Conferences"), hosted by [Backgammon Galore](http://www.bkgm.com/)
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1979**). *[On the Construction of Evaluation Functions for Large Domains](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/)*. [IJCAI 1979](Conferences#IJCAI1979 "Conferences"), Vol. 1, hosted by [Backgammon Galore](http://www.bkgm.com/)
- Editor (**1979**). *Computer Backgammon*. [Personal Computing, Vol. 3, No. 8](Personal_Computing#3_8 "Personal Computing"), pp. 81

## 1980 ...

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1980**). *[Backgammon Computer Program Beats World Champion](http://www.bkgm.com/articles/Berliner/BackgammonProgramBeatsWorldChamp/)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14, hosted by [Backgammon Galore](http://www.bkgm.com/)
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1980**). *[Computer Backgammon](http://www.bkgm.com/articles/Berliner/ComputerBackgammon/index.html)*. [Scientific American](Scientific_American "Scientific American"), Vol. 242, No. 6, hosted by [Backgammon Galore](http://www.bkgm.com/)

## 1985 ...

- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1987**). *A 'Neural' Network that Learns to Play Backgammon*. [NIPS 1987](http://www.informatik.uni-trier.de/~ley/db/conf/nips/nips1987.html#TesauroS87)
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1988**). *Connectionist Learning of Expert Backgammon Evaluations*. [ML, 1988](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1988.html#Tesauro88)
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1988**). *Neural network defeats creator in backgammon match*. Technical report no. CCSR-88-6, Center for Complex Systems Research, [University of Illinois at Urbana-Champaign](University_of_Illinois_at_Urbana-Champaign "University of Illinois at Urbana-Champaign")
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1989**). *NEUROGAMMON: A Neural-Network Backgammon Learning Program*. [Heuristic Programming in Artificial Intelligence 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1989**). *[Neurogammon Wins Computer Olympiad](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1989.1.3.321?journalCode=neco)*. Neural Computation Vol. 1, No. 3
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1989**). *A Parallel Network that Learns to Play Backgammon*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 39, No. 3

## 1990 ...

- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
- [Justin A. Boyan](Justin_A._Boyan "Justin A. Boyan") (**1992**). *Modular Neural Networks for Learning Context-Dependent Game Strategies*. Master's thesis, [University of Cambridge](https://en.wikipedia.org/wiki/University_of_Cambridge), [pdf](http://www.cs.cmu.edu/~jab/cv/pubs/boyan.backgammon-thesis.pdf)
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1994**). *TD-Gammon, a Self-Teaching Backgammon Program, Achieves Master-Level Play*. [Neural Computation Vol. 6, No. 2](http://www.informatik.uni-trier.de/~ley/db/journals/neco/neco6.html#Tesauro94)

## 1995 ...

- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1995**). *Temporal Difference Learning and TD-Gammon*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 38, No. 3
- [Michael Buro](Michael_Buro "Michael Buro") (**1999**). *Efficient Approximation of Backgammon Race Equities.* [ICCA Journal, Vol 22, No. 3](ICGA_Journal#22_3 "ICGA Journal"),[pdf](http://www.cs.ualberta.ca/~mburo/ps/book.pdf)

## 2000 ...

- [Michael Buro](Michael_Buro "Michael Buro") (**2001**). *Efficient Approximation of Backgammon Race Equities.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://www.cs.ualberta.ca/~mburo/ps/bgequ.pdf)
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2002**). *Programming backgammon using self-teaching neural nets*. [Artificial Intelligence Vol. 134 No. 1-2](http://www.informatik.uni-trier.de/~ley/db/journals/ai/ai134.html#Tesauro02)
- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2002**). *BGBlitz wins Backgammon tournament*. [ICGA Journal, Vol. 25, No. 3](ICGA_Journal#25_3 "ICGA Journal") » [7th Computer Olympiad](7th_Computer_Olympiad#Backgammon "7th Computer Olympiad")
- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2002**). *Backgammon at the 7th Computer Olympiad*. [ICGA Journal, Vol. 25, No. 4](ICGA_Journal#25_4 "ICGA Journal") » [7th Computer Olympiad](7th_Computer_Olympiad#Backgammon "7th Computer Olympiad")
- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2003**). *BGBlitz wins Backgammon tournament*. [ICGA Journal, Vol. 26, No. 4](ICGA_Journal#26_4 "ICGA Journal") » [8th Computer Olympiad](8th_Computer_Olympiad#Backgammon "8th Computer Olympiad")
- [Thomas Hauk](index.php?title=Thomas_Hauk&action=edit&redlink=1 "Thomas Hauk (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *[\*-Minimax Performance in Backgammon](http://link.springer.com/chapter/10.1007/11674399_4)*. [CG 2004](CG_2004 "CG 2004")

## 2005 ...

- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2006**). *GnuBG wins Backgammon tournament*. [ICGA Journal, Vol. 29, No. 3](ICGA_Journal#29_3 "ICGA Journal") » [11th Computer Olympiad](11th_Computer_Olympiad#Backgammon "11th Computer Olympiad")
- [François van Lishout](index.php?title=Fran%C3%A7ois_van_Lishout&action=edit&redlink=1 "François van Lishout (page does not exist)"), [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2007**). *[Monte-Carlo Tree Search in Backgammon](https://www.researchgate.net/publication/228378473_Monte-Carlo_tree_search_in_backgammon)*. [CGW 2007](CGW_2007 "CGW 2007")
- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2007**). *BGBlitz wins Backgammon tournament*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal") » [12th Computer Olympiad](12th_Computer_Olympiad#Backgammon "12th Computer Olympiad")
- [Wee-Chong Oon](Wee-Chong_Oon "Wee-Chong Oon"), [Martin Henz](https://dblp.uni-trier.de/pers/hd/h/Henz:Martin) (**2007**). *[M2ICAL Analyses HC-Gammon](http://www.aaai.org/Library/AAAI/2007/aaai07-098.php)*. [AAAI 2007](Conferences#AAAI-2007 "Conferences") <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## 2010 ...

- [Marco Wiering](Marco_Wiering "Marco Wiering") (**2010**). *[Self-play and using an expert to learn to play backgammon with temporal difference learning](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=xVas0I8AAAAJ&cstart=20&citation_for_view=xVas0I8AAAAJ:_kc_bZDykSQC)*. [Journal of Intelligent Learning Systems and Applications](http://www.scirp.org/journal/jilsa/), Vol. 2, No. 2
- [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2011**). *Training Neural Networks to Play Backgammon Variants Using Reinforcement Learning*. Proceedings of [Evogames 2011](http://conference.researchbib.com/?eventid=6400), Part I, LNCS 6624, [pdf](http://ai.uom.gr/nikpapa/publications/Training%20NN%20to%20Play%20Backgammon%20Variants%20Using%20RL.pdf)
- [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2011**). *[Improving Temporal Difference Performance in Backgammon Variants](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=5)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](http://ai.uom.gr/nikpapa/publications/Improving%20Temporal%20Difference%20Learning%20in%20Backgammon%20Variants_ACG13.pdf)
- [Frank Berger](index.php?title=Frank_Berger&action=edit&redlink=1 "Frank Berger (page does not exist)") (**2012**). *Palamedes wins Backgammon Tournament*. [ICGA Journal, Vol. 35, No. 1](ICGA_Journal#35_1 "ICGA Journal") » [16th Computer Olympiad](16th_Computer_Olympiad#Backgammon "16th Computer Olympiad")
- [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2013**). *AnyGammon: Playing backgammon variants using any board size*. [FDG-2013](http://dblp.uni-trier.de/db/conf/fdg/fdg2013.html), [pdf](http://www.fdg2013.org/program/festival/anygammon.pdf)

## 2015 ...

- [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2015**). *Constructing Pin Endgame Databases for the Backgammon Variant Plakoto*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14") <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## Forum Posts

- [Chess, Backgammon and Neural Nets (NN)](https://www.stmintz.com/ccc/index.php?id=25139) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)"), [CCC](CCC "CCC"), August 20, 1998
- [Neural nets in backgammon](https://www.stmintz.com/ccc/index.php?id=359097) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), April 07, 2004
- [A SNAC, anyone?](http://www.talkchess.com/forum/viewtopic.php?t=15442) by [Jan Brouwer](Jan_Brouwer "Jan Brouwer"), [CCC](CCC "CCC"), July 30, 2007
- [What is the best backgammon software?](http://www.talkchess.com/forum/viewtopic.php?t=24403) by M. Ansari, [CCC](CCC "CCC"), October 15, 2008
- [Backgammon is not chess!](http://www.bgonline.org/forums/webbbs_config.pl?noframes;read=138559) by Joe Russell, [BGonline.org Forums](http://www.bgonline.org/forums/), March 08, 2013

## External Links

- [Backgammon from Wikipedia](https://en.wikipedia.org/wiki/Backgammon)
- [Backgammon Galore](http://www.bkgm.com/)

## [Rules of Backgammon](http://www.bkgm.com/rules.html) Computer Backgammon

- [Backgammon (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=11)
- [Backgammon Articles: Using Computers to Improve Your Game](http://www.bkgm.com/articles/page07.html#programming) hosted by the [Backgammon Galore](http://www.bkgm.com/)
- [the neural net backgammon programs](http://satirist.org/learn-game/systems/gammon/) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
- [Neural Network learns Backgammon](http://www.cs.cornell.edu/boom/2001sp/Tsinteris/gammon.htm) by [Kimon Tsinteris](http://kimtsi.com/) and David Wilson
- [FIBS, the First Internet Backgammon Server](http://www.fibs.com/)

## Backgammon Programs

- [Backgammon Software](http://www.bkgm.com/software.html) from [Backgammon Galore](http://www.bkgm.com/)
- [BGBlitz](https://www.bgblitz.com/index.html)
- [GNU Backgammon](http://www.gnubg.org/)
- [Jellyfish](http://www.backgammoned.net/all-about-backgammon/jellyfish.html)
- [Palamedes](http://ai.uom.gr/nikpapa/Palamedes/)
- [Snowie](https://www.bgsnowie.com/)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A backgammon set, consisting of a board, two sets of 15 checkers, two pairs of dice, a [doubling cube](https://en.wikipedia.org/wiki/Backgammon#Doubling_cube), and dice cups, Image by [Ptkfgs](https://commons.wikimedia.org/wiki/User:Ptkfgs), March 6, 2013, [Backgammon from Wikipedia](https://en.wikipedia.org/wiki/Backgammon), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Backgammon Galore](http://www.bkgm.com/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Backgammon (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=11)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [18th Computer Olympiad - Day 6 Photos](https://icga.leidenuniv.nl/?page_id=1467) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *[Experiences in Evaluation with BKG, a Program That Plays Backgammon](http://www.bkgm.com/articles/Berliner/ExperiencesInEvaluationWithBKG/index.html)*. [IJCAI, 1977](Conferences#IJCAI1977 "Conferences"), hosted by [Backgammon Galore](http://www.bkgm.com/)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Hans Berliner from Wikipedia](https://en.wikipedia.org/wiki/Hans_Berliner)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1980**). *[Backgammon Computer Program Beats World Champion](http://www.bkgm.com/articles/Berliner/BackgammonProgramBeatsWorldChamp/)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1998**). *[Reinforcement Learning: An Introduction](http://www.incompleteideas.net/sutton/book/the-book.html)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [11.1 TD-Gammon](http://www.incompleteideas.net/sutton/book/ebook/node108.html)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [The hillclimbing HC-Gammon](http://satirist.org/learn-game/systems/gammon/hc-gammon.html) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Plakoto from Wikipedia](https://en.wikipedia.org/wiki/Plakoto)

**[Up one Level](Games "Games")**

