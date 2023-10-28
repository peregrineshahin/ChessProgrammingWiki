---
title: KRK
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Game Phases](Game_Phases "Game Phases") \* [Endgame](Endgame "Endgame") \* KRK**





|  |  |  |
| --- | --- | --- |
| **KRK**,
the [King](King "King") and [Rook](Rook "Rook") versus King endgame is beside KQR the most elementary endgame with three pieces. If the rook can not be captured immediately - or the losing king isn't [stalemated](Stalemate "Stalemate"), [checkmate](Checkmate "Checkmate") can be forced by driving the losing king to the edge or corner of the board, the rook giving mate similar to the [back-rank mate](Mate_at_a_Glance#.23MatesWithSlidingPieces "Mate at a Glance"), the winning king locking all escape squares, often initiated by a rook [tempo](Tempo "Tempo") move to force the king into [opposition](Opposition "Opposition"). 
 | 

|  |
| --- |
|                                                                                                  ♚              ♔         ♖                                   |

 |
|  KRK Mate in Two
 |


### Contents


* [1 Heuristics](#heuristics)
* [2 Testbed](#testbed)
* [3 See also](#see-also)
* [4 Selected Publications](#selected-publications)
	+ [4.1 1914](#1914)
	+ [4.2 1960 ...](#1960-...)
	+ [4.3 1970 ...](#1970-...)
	+ [4.4 1980 ...](#1980-...)
	+ [4.5 1990 ...](#1990-...)
	+ [4.6 2000 ...](#2000-...)
	+ [4.7 2010 ...](#2010-...)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






Simple heuristics of a [mop-up evaluation](Mop-up_Evaluation "Mop-up Evaluation") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, only considering [Center Manhattan-distance](Center_Manhattan-Distance "Center Manhattan-Distance") of the losing king, and [Chebyshev distance](Distance "Distance") and/or [Manhattan distance](Manhattan-Distance "Manhattan-Distance") between both kings, along with a tiny [search](Search "Search"), should be sufficient to execute the mate. Further, the rook may receive a bonus to maximize the absolute difference of its [rank-](Ranks#RankDistance "Ranks") and [file-distances](Files#FileDistance "Files") to the losing king, to confine the king without becoming attacked. 


Despite todays engines have no difficulty to win this easily even without [tablebases](Endgame_Tablebases "Endgame Tablebases"), deviation from optimal tablebase play, in particular in games with short time control, and most compact and efficient code considering symptoms of [search pathology](Search_Pathology "Search Pathology") remain interesting issues <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Testbed


First implemented by [Leonardo Torres y Quevedo](Leonardo_Torres_y_Quevedo "Leonardo Torres y Quevedo") in [1912](Timeline#1912 "Timeline") within his electro-mechanical KRK solver [El Ajedrecista](El_Ajedrecista "El Ajedrecista"), KRK was and still is [testbed](https://en.wikipedia.org/wiki/Testbed) and subject of research on [evaluation](Evaluation "Evaluation") and [search](Search "Search") heuristics and strategies, [oracle approaches](Oracle "Oracle"), [mate search](Mate_Search "Mate Search"), [search pathology](Search_Pathology "Search Pathology"), [search versus knowledge](Knowledge "Knowledge"), [space-time tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff"), [retrograde analysis](Retrograde_Analysis "Retrograde Analysis") and [tablebase generation](Endgame_Tablebases "Endgame Tablebases") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [knowledge extraction](https://en.wikipedia.org/wiki/Knowledge_extraction) and [compression](https://en.wikipedia.org/wiki/Data_compression), feature detection and [tuning](Automated_Tuning "Automated Tuning"), [learning](Learning "Learning") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [genetic programming](Genetic_Programming "Genetic Programming"), [pattern recognition](Pattern_Recognition "Pattern Recognition"), [decision trees](https://en.wikipedia.org/wiki/Decision_tree), [logic](https://en.wikipedia.org/wiki/Logic) and [logic programming](https://en.wikipedia.org/wiki/Logic_programming) <a id="cite-note-5" href="#cite-ref-5">[5]</a>, [inductive](https://en.wikipedia.org/wiki/Inductive_reasoning) and [deductive reasoning](https://en.wikipedia.org/wiki/Deductive_reasoning), [rule-based modeling](https://en.wikipedia.org/wiki/Rule-based_modeling), [problem solving](https://en.wikipedia.org/wiki/Problem_solving) and [SAT](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) <a id="cite-note-6" href="#cite-ref-6">[6]</a>. In 1977, [Donald Michie](Donald_Michie "Donald Michie") addressed KRK and the [infinite board](index.php?title=Infinite_Board&action=edit&redlink=1 "Infinite Board (page does not exist)") <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## See also


* [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
* [El Ajedrecista](El_Ajedrecista "El Ajedrecista")
* [Distance](Distance "Distance")
* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Huberman's program](Huberman "Huberman")
* [Infinite Board](index.php?title=Infinite_Board&action=edit&redlink=1 "Infinite Board (page does not exist)")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [KPK](KPK "KPK")
* [Knowledge](Knowledge "Knowledge")
* [Learning KRK](Michael_Bain#LearningKRK "Michael Bain")
* [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance")
* [Mate Search](Mate_Search "Mate Search")
* [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")
* [Oracle](Oracle "Oracle")
* [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")
* [Rook Endgame](Rook_Endgame "Rook Endgame")
* [Search Pathology](Search_Pathology "Search Pathology")
* [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff")
* [Tempo](Tempo "Tempo")
* [Triangulation](Triangulation "Triangulation")
* [Zugzwang](Zugzwang "Zugzwang")


## Selected Publications


### 1914


* [Henri Vigneron](index.php?title=Henri_Vigneron&action=edit&redlink=1 "Henri Vigneron (page does not exist)") (**1914**). *Les Automates*. [La Nature](https://en.wikipedia.org/wiki/La_Nature), [pdf](http://cyberneticzoo.com/wp-content/uploads/2011/01/Automates-La-Nature-Torres-1914.pdf) from [cyberneticzoo.com](http://cyberneticzoo.com/), Translation by [David Levy](David_Levy "David Levy") as *Robots* in [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982**). *All About Chess and Computers*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), pp. 14-23, also in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*, pp. 273-278.


### 1960 ...


* [Barbara J. Huberman](Barbara_Liskov "Barbara Liskov") (**1968**). *A Program to Play Chess End Games*. Technical Report no. CS-106, Ph.D. thesis. [Stanford University](Stanford_University "Stanford University"), Computer Science Department


### 1970 ...


* [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein") (**1970**). *Untersuchungen über kombinatorische Spiele.* Ph.D. Thesis, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)
* [Soei T. Tan](Soei_Tan "Soei Tan") (**1972**). *Representation of Knowledge for Very simple Endings in Chess.* Memorandum MIP-R-98, School of Artificial Intelligence, [University of Edinburgh](University_of_Edinburgh "University of Edinburgh")
* [Coen Zuidema](index.php?title=Coen_Zuidema&action=edit&redlink=1 "Coen Zuidema (page does not exist)") (**1974**). *Chess: How to Program the Exceptions?* Technical Report IW21/74, Department of Informatics, [Mathematical Center Amdsterdam](https://en.wikipedia.org/wiki/Centrum_Wiskunde_%26_Informatica). [pdf](http://oai.cwi.nl/oai/asset/9480/9480A.pdf)
* [Donald Michie](Donald_Michie "Donald Michie") (**1977**). *King and Rook Against King: Historical Background and a Problem on the Infinite Board*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
* [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**1978**). *Proving Correctness of Strategies in the AL1 Assertional Language*. Information Processing Letters, Vol. 7, No. 5, pp. 223-230. <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein"), [Ludwig Zagler](Ludwig_Zagler "Ludwig Zagler") (**1978**). *Ergebnisse einer vollstandigen Analyse von Schachendspielen: König und Turm gegen König, König und Turm gegen König und Läufer.* Report, Institut für Informatik, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)


### 1980 ...


* [Ross Quinlan](Ross_Quinlan "Ross Quinlan") (**1983, 1985**). *Learning efficient classification procedures and their application to chess end games*. Machine Learning: An Artificial Intelligence Approach
* [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
* [Reiner Seidel](Reiner_Seidel "Reiner Seidel") (**1986**). *Deriving Correct Pattern Descriptions and Rules for the KRK Endgame by Deductive Methods*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
* [Stephen Muggleton](Stephen_Muggleton "Stephen Muggleton") (**1987**). *Duce, an oracle-based approach to constructive induction*. Proceedings of the 10th IJCAI Conference, Milano, Italy. [pdf](http://www.doc.ic.ac.uk/%7Eshm/Papers/ijcai87.pdf)
* [Stephen Muggleton](Stephen_Muggleton "Stephen Muggleton"), [Michael Bain](Michael_Bain "Michael Bain"), [Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") (**1989**). *An Experimental Comparison of Human and Machine Learning Formalisms*. [6. ML 1989](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1989.html#MuggletonBMM89), [pdf](http://www.doc.ic.ac.uk/~shm/Papers/ml6paper.pdf)


### 1990 ...


* [Stephen Muggleton](Stephen_Muggleton "Stephen Muggleton") (**1991**). *Inductive Logic Programming*. [New Generation Computing](http://www.springer.com/computer/ai/journal/354), Vol. 8, pp. 295-318. ISSN 0228-3635.
* [Michael Bain](Michael_Bain "Michael Bain") (**1992**). *Learning optimal chess strategies.* [ILP92](http://www.cs.york.ac.uk/ILP-events/ILP-1992/)
* [Ashwin Srinivasan](Ashwin_Srinivasan "Ashwin Srinivasan"), [Stephen Muggleton](Stephen_Muggleton "Stephen Muggleton"), [Michael Bain](Michael_Bain "Michael Bain") (**1992**). *Distinguishing Noise from Exceptions in Non-monotonic Learning*. [ILP92](http://www.cs.york.ac.uk/ILP-events/ILP-1992/)
* [Michael Bain](Michael_Bain "Michael Bain") (**1994**). *Learning Logical Exceptions in Chess*. Ph.D. thesis, [University of Strathclyde](https://en.wikipedia.org/wiki/University_of_Strathclyde), [CitySeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.729)
* [Eduardo F. Morales](Eduardo_F._Morales "Eduardo F. Morales") (**1994**). *[Learning Patterns for Playing Strategies](https://content.iospress.com/articles/icga-journal/icg17-1-04)*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal"), [pdf](https://pdfs.semanticscholar.org/210c/b439081f8e84ca715824262043f36c25a5d2.pdf)
* [Ulrich Thiemonds](Ulrich_Thiemonds "Ulrich Thiemonds") (**1999**). *Ein regelbasiertes Spielprogramm für Schachendspiele*. [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn), Diplom thesis, [pdf](https://www.idb.uni-bonn.de/publications/da/da_thiemonds_1999.pdf) (German)


### 2000 ...


* [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2001,2010**). *[Prolog programming for artificial intelligence](http://www.worldcat.org/search?qt=wikipedia&q=isbn%3A0201403757)*. Harlow England, [Addison Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
* [David Gleich](index.php?title=David_Gleich&action=edit&redlink=1 "David Gleich (page does not exist)") (**2003**). *Machine Learning in Computer Chess: Genetic Programming and KRK*. [Harvey Mudd College](https://en.wikipedia.org/wiki/Harvey_Mudd_College), [pdf](http://www.cs.purdue.edu/homes/dgleich/publications/Gleich%202003%20-%20Machine%20Learning%20in%20Computer%20Chess.pdf)
* [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Igor Kononenko](Igor_Kononenko "Igor Kononenko") (**2003**). *Search versus Knowledge: An Empirical Study of Minimax on KRK*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.ailab.si/sasha/acg2003.pdf)
* [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Igor Kononenko](Igor_Kononenko "Igor Kononenko") (**2005**). *[Bias and pathology in minimax search](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6V1G-4HCN79X-1&_user=10&_coverDate=12%2F14%2F2005&_rdoc=1&_fmt=high&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=79f966215bea9b7461b6877c9373b0bf)*. Theoretical Computer Science, Volume 349, Issue 2, [pdf](http://lkm.fri.uni-lj.si/xaigor/slo/clanki/Sadikov_final.pdf)
* [Gabriel Breda](index.php?title=Gabriel_Breda&action=edit&redlink=1 "Gabriel Breda (page does not exist)") (**2006**). *KRK Chess Endgame Database Knowledge Extraction and Compression*. Diploma thesis, [Darmstadt University of Technology](Darmstadt_University_of_Technology "Darmstadt University of Technology")
* [Nicolas Lassabe](index.php?title=Nicolas_Lassabe&action=edit&redlink=1 "Nicolas Lassabe (page does not exist)"), [Stéphane Sanchez](index.php?title=St%C3%A9phane_Sanchez&action=edit&redlink=1 "Stéphane Sanchez (page does not exist)"), [Hervé Luga](index.php?title=Herv%C3%A9_Luga&action=edit&redlink=1 "Hervé Luga (page does not exist)"), [Yves Duthen](index.php?title=Yves_Duthen&action=edit&redlink=1 "Yves Duthen (page does not exist)") (**2006**). *[Genetically Programmed Strategies For Chess Endgame](http://www.sciweavers.org/publications/genetically-programmed-strategies-chess-endgame)*. [GECCO 2006](http://www.sigevo.org/gecco-2006/), [pdf](http://www.cs.york.ac.uk/rts/docs/GECCO_2006/docs/p831.pdf)


### 2010 ...


* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)"), [Mirko Čubrilo](index.php?title=Mirko_%C4%8Cubrilo&action=edit&redlink=1 "Mirko Čubrilo (page does not exist)"), [Predrag Janičić](index.php?title=Predrag_Jani%C4%8Di%C4%87&action=edit&redlink=1 "Predrag Janičić (page does not exist)") (**2012**). *Formal Analysis of Correctness of a Strategy for the KRK Chess Endgame*. [Fifth Workshop on Formal and Automated Theorem Proving and Applications](http://argo.matf.bg.ac.rs/events/2012/fatpa2012/fatpa2012.html), [Belgrade](https://en.wikipedia.org/wiki/Belgrade), [Serbia](https://en.wikipedia.org/wiki/Serbia), [slides as pdf](http://argo.matf.bg.ac.rs/events/2012/fatpa2012/slides/MarkoMalikovic.pdf)
* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)"), [Predrag Janičić](index.php?title=Predrag_Jani%C4%8Di%C4%87&action=edit&redlink=1 "Predrag Janičić (page does not exist)") (**2013**). *Proving Correctness of a KRK Chess Endgame Strategy by SAT-based Constraint Solving*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal")
* [Zacharias Georgiou](Zacharias_Georgiou "Zacharias Georgiou"), [Evangelos Karountzos](Evangelos_Karountzos "Evangelos Karountzos"), [Yaroslav Shkarupa](Yaroslav_Shkarupa "Yaroslav Shkarupa"), [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli") (**2016**). *A Reinforcement Learning Approach for Solving KRK Chess Endgames*. [pdf](https://github.com/paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames/blob/master/project_papers/final_paper/reinforcement-learning-approach(2).pdf) <a id="cite-note-9" href="#cite-ref-9">[9]</a>


## Forum Posts


* [My program can't mate KQK or KRK!](http://www.talkchess.com/forum/viewtopic.php?t=47477) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), March 11, 2013
* [algorithm - Chess task - King, Rook Vs King](http://stackoverflow.com/questions/15988069/chess-task-king-rook-vs-king) by [Sreekanth Karumanaghat](http://stackoverflow.com/users/1448316/sreekanth-karumanaghat), [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), April 13, 2013
* [Why minimax is fundamentally flawed](http://www.talkchess.com/forum/viewtopic.php?t=54295) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 09, 2014 » [Minimax](Minimax "Minimax")


## External Links


* [Longest mate in King and Rook versus King endgame](http://www.gilith.com/chess/endgames/kr_k.html) by [Joe Leslie-Hurd](Joe_Leslie-Hurd "Joe Leslie-Hurd"), February 16, 2005
* [UCI Machine Learning Repository: Chess (King-Rook vs. King) Data Set](http://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King%29) by [Michael Bain](Michael_Bain "Michael Bain")
* [Checkmate - King and rook - Wikipedia](https://en.wikipedia.org/wiki/Checkmate#King_and_rook)
* [How to Mate With King and Rook Vs King: 19 Steps - wikiHow](http://www.wikihow.com/Mate-With-King-and-Rook-Vs-King)
* [Chess Corner - Chess Tutorial - Checkmating with Lone Rook](http://www.chesscorner.com/tutorial/basic/r_k_mate/r_k_mate.htm)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Why minimax is fundamentally flawed](http://www.talkchess.com/forum/viewtopic.php?t=54295) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 09, 2014
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein") (**1970**). *Untersuchungen über kombinatorische Spiele.* Ph.D. Thesis, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Michael Bain](Michael_Bain "Michael Bain") (**1994**). *Learning Logical Exceptions in Chess*. Ph.D. thesis, [University of Strathclyde](https://en.wikipedia.org/wiki/University_of_Strathclyde)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2001,2010**). *[Prolog programming for artificial intelligence](http://www.worldcat.org/search?qt=wikipedia&q=isbn%3A0201403757)*. Harlow England, [Addison Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a>  [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)"), [Predrag Janičić](index.php?title=Predrag_Jani%C4%8Di%C4%87&action=edit&redlink=1 "Predrag Janičić (page does not exist)") (**2013**). *Proving Correctness of a KRK Chess Endgame Strategy by SAT-based Constraint Solving*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Donald Michie](Donald_Michie "Donald Michie") (**1977**). *King and Rook Against King: Historical Background and a Problem on the Infinite Board*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Donald Michie](Donald_Michie "Donald Michie") (**1976**). *[AL1: a package for generating strategies from tables](http://portal.acm.org/citation.cfm?id=1045272)*. ACM SIGART Bulletin, Issue 59
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [GitHub - paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames: Machine Learning - Reinforcement Learning](https://github.com/paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames)

**[Up one Level](Endgame "Endgame")**







 
