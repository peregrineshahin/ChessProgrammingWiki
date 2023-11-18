---
title: Pruning
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* Pruning**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b7047d58ae0c54bf8bab#57f3b7277d58ae2139bf8baf) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Under the Trees <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Pruning**, (as opposed to [reductions](Reductions "Reductions"))   

a name for every heuristic that removes completely certain branches of the [search tree](Search_Tree "Search Tree"), assuming they have no bearing to the search result. [Alpha-Beta](Alpha-Beta "Alpha-Beta") may be considered as backward pruning, because we found a refutation after searching <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Forward pruning always involves some risks to overlook something, with influence on the root score. Some pruning techniques rely on a specialized, but reduced search, others rely only on static move properties. [Shannon Type B](Type_B_Strategy "Type B Strategy") programs only consider some plausible mores, but all other moves are pruned. 



## Forward pruning techniques


Forward pruning techniques are either applied at expected [Cut-Nodes](Node_Types#Cut-Nodes "Node Types") or [All-Nodes](Node_Types#All-Nodes "Node Types") and return either beta as [lower bound](Lower_Bound "Lower Bound") or alpha as [upper bound](Upper_Bound "Upper Bound"). The none [recursive](Recursion "Recursion") [ProbCut](ProbCut "ProbCut") is applied at both types of none [PV-nodes](Node_Types#PV-Node "Node Types"). Rather than immediately returning alpha at strong expected [All-Nodes](Node_Types#All-Nodes "Node Types") after a reduced or [quiescence search](Quiescence_Search "Quiescence Search"), pruning techniques near the horizon skip moves, which are very unlikely to exceed alpha, or in case of the quiescence search itself, all (most) [quiet moves](Quiet_Moves "Quiet Moves") as well as losing [captures](Captures "Captures").



### Returning Beta


at expected [Cut-Nodes](Node_Types#Cut-Nodes "Node Types"):



* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") - if reduced nullmove search fails high, return beta
* [Multi-Cut](Multi-Cut "Multi-Cut") - if a reduced, specialized search has C cut-offs from N tried moves, return beta
* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning"), also applicable at expected [All-Nodes](Node_Types#All-Nodes "Node Types")
* [ProbCut](ProbCut "ProbCut")
* [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* [Standing Pat in Quiescence Search](Quiescence_Search#StandPat "Quiescence Search")


### Returning Alpha


or below at expected [All-Nodes](Node_Types#All-Nodes "Node Types") or expected [Cut-Nodes](Node_Types#Cut-Nodes "Node Types") which turn out to become All-Nodes:



* after trying **width[ply]** moves in [Shannon Type-B](Type_B_Strategy "Type B Strategy") programs, return alpha
* [Sibling Prediction Pruning](Sibling_Prediction_Pruning "Sibling Prediction Pruning") - return alpha, or depending on the implementation, only skip the move
* [ProbCut](ProbCut "ProbCut")
* [Uncertainty Cut-Offs](Uncertainty_Cut-Offs "Uncertainty Cut-Offs")


### Skipping Moves


likely at [All-Nodes](Node_Types#All-Nodes "Node Types"):



* [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
* [Futility Pruning](Futility_Pruning "Futility Pruning")


 [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
 [Deep Futility Pruning](Futility_Pruning#DeepFutilityPruning "Futility Pruning")
 [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [AEL-Pruning](AEL-Pruning "AEL-Pruning")
* [Delta Pruning](Delta_Pruning "Delta Pruning") in [Quiescence Search](Quiescence_Search "Quiescence Search")
* [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
* [Parity Pruning](Parity_Pruning "Parity Pruning")


## See also


* [Extensions](Extensions "Extensions")
* [Razoring](Razoring "Razoring")
* [Reductions](Reductions "Reductions")


 [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") aka History Pruning <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Pruning in Nimzo 2.2.1](Nimzo#Pruning "Nimzo")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Shannon Type B Strategy](Type_B_Strategy "Type B Strategy")


## Publications


### 1960 ...


* [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")


### 1970 ...


* [John Birmingham](John_Birmingham "John Birmingham"), [Peter Kent](Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1980 ...


* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1983**). *The Alpha-Beta Algorithm: Incremental Updating, Well-Behaved Evaluation Functions, and Non-Speculative Forward Pruning*. Computer Game-Playing (ed. [Max Bramer](Max_Bramer "Max Bramer")), pp. 285-289. Ellis Horwood Limited Publishers, Chichester.
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Experiments in Search and Knowledge*. Ph.D. thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo"). Reprinted as Technical Report TR 86-12, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta")
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1988**). *Comparing Various Pruning Algorithms on Very Strongly Ordered Game Trees: The Details.* Tech. Report #50, Department of Statistics and Computer Science, [Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology")
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1989**). *Comparing Various Pruning Algorithms on Very Strongly Ordered Game Trees*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
* [Liwu Li](Liwu_Li "Liwu Li") (**1989**). *[Probabilistic Analysis of Search](https://doi.org/10.7939/R3VX06F26)*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), advisor [Tony Marsland](Tony_Marsland "Tony Marsland")
* [Liwu Li](Liwu_Li "Liwu Li"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1989**). *Probability-Based Game Tree Pruning*. [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/joa89.pdf)


### 1990 ...


* [Liwu Li](Liwu_Li "Liwu Li"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1990**). *[Probability-Based Game Tree Pruning](http://www.sciencedirect.com/science/article/pii/019667749090027C)*. [Journal of Algorithms, Vol. 11, No. 1](ftp://ftp.math.utah.edu/pub/tex/bib/toc/jalg.html#11(1):March:1990)
* [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Experiments in Forward Pruning with Limited Extensions.* [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
* [Yi-Fan Ke](Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](Tai-Ming_Parng "Tai-Ming Parng") (**1993**). *The Guard Heuristic: Legal Move Ordering with Forward Game-Tree Pruning*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"). (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
* [Stephen J.J. Smith](Stephen_J.J._Smith "Stephen J.J. Smith"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1994**). *An Analysis of Forward Pruning*. Proceedings [AAAI](AAAI "AAAI") 1994, [pdf](http://www.aaai.org/Papers/AAAI/1994/AAAI94-213.pdf)
* [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal"), [pdf](http://www.cs.ualberta.ca/~mburo/ps/probcut.pdf)
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1998**). *Multi-Cut Pruning in Alpha-Beta Search*. [CG 1998](CG_1998 "CG 1998"), pp. 15-24. See also [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search*. Theoretical Computer Science, Vol. 252, pp. 177-196 for an expanded version.


### 2000 ...


* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *AEL Pruning.* [ICGA Journal, Vol. 23, No. 1](ICGA_Journal#23_1 "ICGA Journal")
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2000**). *Selective Depth-First Search Methods*. in [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (eds.) (**2000**). *Games in AI Research*. [Universiteit Maastricht](Maastricht_University "Maastricht University"), [pdf preprint](http://www.cs.ualberta.ca/%7Etony/RecentPapers/nec97w.pdf)
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252, pp. 177-196. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)
* [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* Accepted for publication. [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
* [Qian Liang](index.php?title=Qian_Liang&action=edit&redlink=1 "Qian Liang (page does not exist)") (**2003**). *The Evolution of Mulan: Some Studies in Game-Tree Pruning and Evaluation Functions in the Game of Amanons*. M.Sc. thesis, Electronic Engineering, [The University of New Mexico](https://en.wikipedia.org/wiki/University_of_New_Mexico), [pdf](http://www.santafe.edu/~moore/QianThesis.pdf)
* [Yew Jin Lim](Yew_Jin_Lim "Yew Jin Lim"), [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee") (**2006**). *Properties of Forward Pruning in Game-Tree Search*, AAAI 2006, [pdf](http://www.yewjin.com/storage/papers/riskmanagement.pdf)
* [Yew Jin Lim](Yew_Jin_Lim "Yew Jin Lim"), [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee") (**2006**). *RankCut - A Domain Independent Forward Pruning Method for Games*, AAAI 2006, [pdf](http://www.yewjin.com/storage/papers/rankcut.pdf)
* [Jeroen Carolus](Jeroen_Carolus "Jeroen Carolus") (**2006**). *Alpha-Beta with Sibling Prediction Pruning in Chess*. Masters thesis, [pdf](http://homepages.cwi.nl/%7Epaulk/theses/Carolus.pdf)
* [Yew Jin Lim](Yew_Jin_Lim "Yew Jin Lim") (**2007**). *On Forward Pruning in Game-Tree Search*. Ph.D. thesis, [National University of Singapore](https://en.wikipedia.org/wiki/National_University_of_Singapore), [pdf](http://www.yewjin.com/storage/papers/PhDThesisLimYewJin.pdf)


### 2010 ...


* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Masakazu Muramatsu](Masakazu_Muramatsu "Masakazu Muramatsu") (**2012**). *[Efficiency of three Forward-Pruning Techniques in Shogi: Futility Pruning, Null-move Pruning, and Late Move Reduction (LMR)](https://www.semanticscholar.org/paper/Efficiency-of-three-forward-pruning-techniques-in-Hoki-Muramatsu/206099961f401c8693e071c2b739f164ae5ffa6c)*. [Entertainment Computing](https://www.journals.elsevier.com/entertainment-computing), Vol. 3, No. 3
* [Kieran Greer](Kieran_Greer "Kieran Greer") (**2012**). *[Tree Pruning for New Search Techniques in Computer Games](http://www.hindawi.com/journals/aai/2013/357068/)*. Advances in Artificial Intelligence, Vol. 2013
* [Kieran Greer](Kieran_Greer "Kieran Greer") (**2013**). *Dynamic Move Chains – a Forward Pruning Approach to Tree Search in Computer Chess*. [arXiv:1403.0778](http://arxiv.org/abs/1403.0778)
* [Naoyuki Sato](index.php?title=Naoyuki_Sato&action=edit&redlink=1 "Naoyuki Sato (page does not exist)"), [Kokolo Ikeda](Kokolo_Ikeda "Kokolo Ikeda") (**2016**). *[Three types of forward pruning techniques to apply the alpha beta algorithm to turn-based strategy games](https://ieeexplore.ieee.org/document/7860427)*. [CIG 2016](https://dblp.uni-trier.de/db/conf/cig/cig2016.html)


## Forum Posts


### 1995 ...


* [Forward pruning](https://www.stmintz.com/ccc/index.php?id=73649) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), October 16, 1999


 [Re: Forward pruning](https://www.stmintz.com/ccc/index.php?id=73701) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), October 16, 1999
### 2000 ...


* [Alpha beta fail soft, pruning & hash bounds?](https://www.stmintz.com/ccc/index.php?id=144854) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 14, 2000 » [Fail-Soft](Fail-Soft "Fail-Soft"), [Bound](Bound "Bound")
* [Correct values if all moves are pruned?](https://www.stmintz.com/ccc/index.php?id=148308) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 05, 2001
* [An interesting forward pruning experiment - with pseudo description](https://groups.google.com/d/msg/rec.games.chess.computer/iECalt6Tzug/GWNOLzFQyk8J) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 08, 2003
* [Testing the reliability of forward pruning](https://www.stmintz.com/ccc/index.php?id=296689) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), May 15, 2003 » [Engine Testing](Engine_Testing "Engine Testing")
* [Forward Pruning...](https://www.stmintz.com/ccc/index.php?id=351949) by [Joshua Haglund](index.php?title=Joshua_Haglund&action=edit&redlink=1 "Joshua Haglund (page does not exist)"), [CCC](CCC "CCC"), February 29, 2004
* [Forward pruning and some related techniques](https://www.stmintz.com/ccc/index.php?id=352384) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 02, 2004
* [Bayesian Forward Pruning](https://www.stmintz.com/ccc/index.php?id=359342) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 09, 2004
* [Forward/HB/Null move pruning ideas](https://www.stmintz.com/ccc/index.php?id=389135) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 25, 2004


### 2005 ...


* [About history pruning...](https://www.stmintz.com/ccc/index.php?id=457846) by Svein Bjørnar Myrvang, [CCC](CCC "CCC"), October 26, 2005
* [Fail-low pruning](https://www.stmintz.com/ccc/index.php?id=480380) by Tommi Rimpiläinen, [CCC](CCC "CCC"), January 17, 2006
* [History pruning](https://www.stmintz.com/ccc/index.php?id=489978) by [Frank Phillips](Frank_Phillips "Frank Phillips") from [CCC](CCC "CCC"), February 27, 2006
* [history pruning/ late move pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4435&p=23839) by [Tom King](Tom_King "Tom King"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006
* [avoidrep-pruning](http://www.talkchess.com/forum/viewtopic.php?t=13791) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), May 15, 2007 » [Repetitions](Repetitions "Repetitions")
* [Toga/Glaurung/Strelka Prunings/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=19316) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), January 31, 2008 » [Toga](Toga "Toga"), [Glaurung](Glaurung "Glaurung"), [Strelka](Strelka "Strelka"), [Reductions](Reductions "Reductions")
* [Fruit 2.1 pruning](http://www.talkchess.com/forum/viewtopic.php?t=22359) by [kongsian](Chua_Kong_Sian "Chua Kong Sian"), [CCC](CCC "CCC"), July 15, 2008 » [Fruit](Fruit "Fruit")


### 2010 ...


* [What program first used hard pruning?](http://www.talkchess.com/forum/viewtopic.php?t=37012) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), December 10, 2010
* [Hard pruning history](http://www.open-chess.org/viewtopic.php?f=5&t=807) by [Mark Watkins](Mark_Watkins "Mark Watkins"), [Open Chess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), December 10, 2010
* [Using SEE to prune in main search](http://www.talkchess.com/forum/viewtopic.php?t=37514) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 08, 2011 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Bad Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38407) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
* [Reducing/Pruning Bad Captures (SEE < 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 19, 2011 » [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Over-aggressive pruning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=40456) by FlavusSnow, [CCC](CCC "CCC"), September 18, 2011
* [Relationship between move ordering and pruning](http://www.open-chess.org/viewtopic.php?f=5&t=2173) by [Don Dailey](Don_Dailey "Don Dailey"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 17, 2012 » [Move Ordering](Move_Ordering "Move Ordering")
* [Adjustable search pruning depending on time control](http://www.talkchess.com/forum/viewtopic.php?t=46503) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), December 20, 2012 » [Time Management](Time_Management "Time Management")
* [Pruning in QS](http://www.talkchess.com/forum/viewtopic.php?t=47423) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 06, 2013 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Pruning in today's top engines](http://www.talkchess.com/forum/viewtopic.php?t=49342) by Gordon Robertson, [CCC](CCC "CCC"), September 13, 2013
* [stalemate detection and pruning](http://www.talkchess.com/forum/viewtopic.php?t=49429) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 22, 2013 » [Stalemate](Stalemate "Stalemate")
* [pruning statistics](http://www.talkchess.com/forum/viewtopic.php?t=51075) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 27, 2014 » [Search Statistics](Search_Statistics "Search Statistics")


### 2015 ...


* [Verification of pruning techniques](http://www.talkchess.com/forum/viewtopic.php?t=57843) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), October 04, 2015
* [EMR & EMP](http://www.talkchess.com/forum/viewtopic.php?t=60868) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 19, 2016
* [Transposition table based pruning idea](http://www.talkchess.com/forum/viewtopic.php?t=66135) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), December 25, 2017 » [Transposition Table](Transposition_Table "Transposition Table")
* [Pruning at PV nodes?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69510) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 06, 2019 » [PV-Nodes](Node_Types#PV-Node "Node Types")
* [delaying tactics: prune or extend?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70165) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 10, 2019 » [Selectivity](Selectivity "Selectivity"), [Tactics](Tactics "Tactics")


### 2020 ...


* [Pruning / reduction depending on king safety](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72981) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 02, 2020 » [King Safety](King_Safety "King Safety")
* [Questions on Razoring and Code Structure for Pruning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74425) by Cheney, [CCC](CCC "CCC"), July 09, 2020 » [Razoring](Razoring "Razoring")
* [Problems with pruning non-PV nodes](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77483) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 13, 2021


## External Links


* [Pruning from Wikipedia](https://en.wikipedia.org/wiki/Decision_tree_pruning)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Under the Trees, Oil on Canvas, 160 x 200 cm, [Return to Vilna Series](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b7047d58ae0c54bf8bab#57f3b7277d58ae2139bf8baf), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Better Alpha-Beta algorithm than pruning, to don't confuse it with the mentioned forward pruning
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: What is History Pruning?](https://www.stmintz.com/ccc/index.php?id=434817) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), July 03, 2005

**[Up one level](Selectivity "Selectivity")**







 
