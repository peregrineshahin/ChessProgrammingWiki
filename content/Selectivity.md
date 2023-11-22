---
title: Selectivity
---
**[Home](Home "Home") \* [Search](Search "Search") \* Selectivity**


**Selectivity** gives a whiff of [Shannon's Type B](Type_B_Strategy "Type B Strategy") search to [Shannon's Type A](Type_A_Strategy "Type A Strategy") or [brute-force](Brute-Force "Brute-Force"). The goal is to search "interesting" and forced branches which are or are likely to become part of the [principal variation](Principal_Variation "Principal Variation") deeper than nominal, but to reduce uninteresting branches. 



## [Pruning](Pruning "Pruning")


* [AEL-Pruning](AEL-Pruning "AEL-Pruning")
* [Delta Pruning](Delta_Pruning "Delta Pruning")
* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
* [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
* [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Late Move Pruning)
* [Multi-Cut](Multi-Cut "Multi-Cut")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Parity Pruning](Parity_Pruning "Parity Pruning")
* [ProbCut](ProbCut "ProbCut")
* [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* [Uncertainty Cut-Offs](Uncertainty_Cut-Offs "Uncertainty Cut-Offs")


## [Reductions](Reductions "Reductions")


* [Internal Iterative Reductions](Internal_Iterative_Reductions)
* [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions") - FHR
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") - LMR
* [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
* [RankCut](RankCut "RankCut")
* [Razoring](Razoring "Razoring")


## See also


* [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
* [Parallelism and Selectivity in Game Tree Search | Video](Tord_Romstad#Video "Tord Romstad"), Talk by [Tord Romstad](Tord_Romstad "Tord Romstad")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Selective Search](Selective_Search "Selective Search") (Magazine)
* [Selective Search versus Brute Force - Conference at WCCC 1986](WCCC_1986#Workshop "WCCC 1986")


## Publications


### 1970 ...


* [Russell M. Church](index.php?title=Russell_M._Church&action=edit&redlink=1 "Russell M. Church (page does not exist)"), [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1977**). *Plans, Goals, and Search Strategies for the Selection of a Move in Chess*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")


### 1980 ...


* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1983**). *Searching to Variable Depth in Computer Chess.* Proceedings of [IJCAI 83](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai83.html), pp. 760-762. Karlsruhe. [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-83-VOL-2/PDF/039.pdf)
* [Don Beal](Don_Beal "Don Beal") (**1986**). *Selective Search without Tears.* [ICCA Journal, Vol. 9, No. 2](ICGA_Journal#9_2 "ICGA Journal")
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") (**1986**). *Selective Search versus Brute Force.* [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
* [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")


### 1990 ...


* [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. MSc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
* [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Selective Extensions in Game-Tree Search*. [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
* [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1993**). *Alpha-Beta Conspiracy Search*. [ps (draft)](http://ttic.uchicago.edu/~dmcallester/abc.ps) » [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
* [Javier Ros Padilla](index.php?title=Javier_Ros_Padilla&action=edit&redlink=1 "Javier Ros Padilla (page does not exist)") (**1994**). *Estimating Asymmetry and Selectivity in Chess Programs*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
* [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1994**). *[The Principle of Pressure in Chess](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=EJurXJ4AAAAJ&cstart=40&citation_for_view=EJurXJ4AAAAJ:TQgYirikUcIC)*. TAINN 1994
* [Lev Finkelstein](Lev_Finkelstein "Lev Finkelstein"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1998**). *[Learning to Play Chess Selectively by Acquiring Move Patterns.](http://www.cs.technion.ac.il/%7Eshaulm/papers/abstracts/Finkelstein-1998-LPC.html)* [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal"), [pdf](http://www.cs.technion.ac.il/%7Eshaulm/papers/pdf/Finkelstein-Markovitch-icca1998.pdf)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1998**). *[Selective Game Tree Search on a Cray T3E](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/ABSTRACTS/FM_T3E.html)*. [ps](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/FM_T3E.ps.Z)


### 2000 ...


* [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Richard P. Cochran](Richard_P._Cochran "Richard P. Cochran") (**2000**). *[A Least-Certainty Heuristic for Selective Search](http://link.springer.com/chapter/10.1007/3-540-45579-5_1)*. [CG 2000](CG_2000 "CG 2000"), [pdf](http://people.cs.umass.edu/~utgoff/papers/springer-lcf.pdf) » [LCF](Richard_P._Cochran#LCF "Richard P. Cochran")
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2000**). *Selective Depth-First Search Methods*. in [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (eds.) (**2000**). *Games in AI Research*. [Universiteit Maastricht](Maastricht_University "Maastricht University"), [pdf preprint](http://www.cs.ualberta.ca/%7Etony/RecentPapers/nec97w.pdf)
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**2002**). *[The Secret of Selective Game Tree Search, When Using Random-Error Evaluations](http://www.springerlink.com/content/f6b4wb6l63dpd0jv/)*. Proceedings of 19th Annual Symposium on Theoretical Aspects of Computer Science (STACS)
* [David McAllester](David_McAllester "David McAllester"), [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**2002**). *Alpha-Beta Conspiracy Search*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal") » [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")
* [Brian Sheppard](Brian_Sheppard "Brian Sheppard") (**2004**). *[Efficient Control of Selective Simulations](https://link.springer.com/chapter/10.1007/11674399_1)*. [CG 2004](CG_2004 "CG 2004")
* [Brian Sheppard](Brian_Sheppard "Brian Sheppard") (**2004**). *Efficient Control of Selective Simulations*. [ICGA Journal, Vol. 27, No. 2](ICGA_Journal#27_2 "ICGA Journal") <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [Pálmi Skowronski](index.php?title=P%C3%A1lmi_Skowronski&action=edit&redlink=1 "Pálmi Skowronski (page does not exist)") (**2009**). *Gradual Focus: A Method for Automated Feature Discovery in Selective Search*. M.Sc. thesis


### 2010 ...


* [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Optimizing Selective Search in Chess*. ICML - Workshop on Machine Learning and Games
* [Maarten Schadd](index.php?title=Maarten_Schadd&action=edit&redlink=1 "Maarten Schadd (page does not exist)") (**2011**). *Selective Search in Games of Different Complexity*. Ph.D. Thesis. Department of Knowledge Engineering, [Maastricht University](Maastricht_University "Maastricht University")


## Forum Posts


### 1998 ...


* [A new selective heuristic?](https://www.stmintz.com/ccc/index.php?id=21017) by [Frank Schneider](Frank_Schneider "Frank Schneider"), [CCC](CCC "CCC"), June 21, 1998 » [Reductions](Reductions "Reductions")


### 2000 ...


* [Selective Searching](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7b66bdec7f729fa7) by Bob Durrett, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 19, 2000
* [pruning vs extensions vs qsearch - are these all effectively the same?](https://www.stmintz.com/ccc/index.php?id=267678) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), November 27, 2002
* [Evaluation-based Reductions and/or Extensions](https://www.stmintz.com/ccc/index.php?id=338851) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), December 28, 2003
* [extensions + reductions + pruning = confusion](https://www.stmintz.com/ccc/index.php?id=356488) by [Johan de Koning](Johan_de_Koning "Johan de Koning"), [CCC](CCC "CCC"), March 24, 2004 (was [Shredder 8 secret: search depth?](https://www.stmintz.com/ccc/index.php?id=356109))
* [Extension - Reductions and threats](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4820) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 17, 2006
* [Extensions/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=29905) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), September 28, 2009


### 2010 ...


* [Counting depth as a function of number of legal moves](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42677) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), February 28, 2012 » [Depth](Depth "Depth")
* [Nullmove vs classic selective search](http://www.talkchess.com/forum/viewtopic.php?t=44686) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 04, 2012 <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Houdini 3 reducing the depth feature](http://www.talkchess.com/forum/viewtopic.php?t=45624) by Maurizio Maglio, [CCC](CCC "CCC"), October 17, 2012 » [Houdini](Houdini "Houdini")
* [selective depth definition](http://www.talkchess.com/forum/viewtopic.php?t=51264) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 13, 2014 » [Stockfish](Stockfish "Stockfish")
* [Is modern chess software lossless or lossy?](http://www.talkchess.com/forum/viewtopic.php?t=66298) by Meni Rosenfeld, [CCC](CCC "CCC"), January 10, 2018 » [Playing Strength](Playing_Strength "Playing Strength")
* [Names of selectivity algorithms](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68082) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 26, 2018
* [delaying tactics: prune or extend?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70165) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 10, 2019 » [Tactics](Tactics "Tactics")


### 2020 ...


* [Tactical search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74170) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), June 13, 2020 » [Tactics](Tactics "Tactics")


## External Links


* [Living Being Quintet](http://www.vincent-peirani.com/projets) - On the heights, [Altitude Jazz Festival 2015](http://www.altitudejazz.com/programme-concerts-festival-jazz-hautes-alpes.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Vincent Peirani](Category:Vincent_Peirani "Category:Vincent Peirani"), [Émile Parisien](index.php?title=Category:%C3%89mile_Parisien&action=edit&redlink=1 "Category:Émile Parisien (page does not exist)"), [Tony Paeleman](Category:Tony_Paeleman "Category:Tony Paeleman"), [Julien Herné](http://www.julienherne.com/), [Yoann Serra](http://www.simonoviez.com/english/YoannSerraus.htm)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [ICCA Journal, Vol. 17, No. 1](https://groups.google.com/d/msg/rec.games.chess/5_dMbe0_juo/bXQQVYVEpykJ) by [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 02, 1994
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> slightly revised version of the [CG 2004](CG_2004 "CG 2004") paper
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> Selective Search Techniques in REBEL (introduction) from [Programmer Corner](Rebel#ProgrammerCorner "Rebel") by [Ed Schröder](Ed_Schroder "Ed Schroder")

**[Up one level](Search "Search")**







 
