---
title: Move Ordering
---
**[Home](Home "Home") \* [Search](Search "Search") \* Move Ordering**



[ [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Four Parts [[1]](#cite_note-1)
For the [alpha-beta](Alpha-Beta "Alpha-Beta") algorithm to perform well, the [best moves](Best_Move "Best Move") need to be searched first. This is especially true for [PV-nodes](Node_Types#PV-Node "Node Types") and expected [Cut-nodes](Node_Types#Cut-Nodes "Node Types"). The goal is to become close to the minimal tree. On the other hand - at Cut-nodes - the best move is not always the cheapest refutation, see for instance [enhanced transposition cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff"). **Most** important inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework is to try the [principal variation](Principal_Variation "Principal Variation") of the previous [iteration](Iteration "Iteration") as the leftmost path for the next iteration, which might be applied by an explicit [triangular PV-table](Triangular_PV-Table "Triangular PV-Table") or implicit by the [transposition table](Transposition_Table "Transposition Table").



### Captures


For [captures](Captures "Captures") (if any), a simple, but quite efficient heuristic is **(re)capturing** the **last** moved piece with the **least valuable attacker**. Otherwise following heuristics may used, concerning the order of captures:



* [MVV-LVA](MVV-LVA "MVV-LVA") - Most Valuable Victim - Least Valuable Aggressor
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") abbreviated as **SEE**






### Non-Captures


* [Killer Heuristic](Killer_Heuristic "Killer Heuristic") [[2]](#cite_note-2)
* [History Heuristic](History_Heuristic "History Heuristic") [[3]](#cite_note-3)
* [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic") [[4]](#cite_note-4)
* [Dedicated Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables") only for move ordering [[5]](#cite_note-5)


### Less common techniques


These techniques are well known theoretically for non-captures, but not all programmers use them:



* [Mate Killers](Mate_Killers "Mate Killers")
* [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") [[6]](#cite_note-6)
* [Guard Heuristic](Guard_Heuristic "Guard Heuristic")
* [Last Best Reply](Last_Best_Reply "Last Best Reply")
* [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic") [[7]](#cite_note-7)
* [Threat Move](Threat_Move "Threat Move") from [null move](Null_Move_Pruning "Null Move Pruning") refutations
* [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff") (ETC)
* [Refutation Table](Refutation_Table "Refutation Table")


### Using Neural Networks


Move ordering (as well as [Time Management](Time_Management "Time Management")) is an interesting application of [Neural Networks](Neural_Networks "Neural Networks"), as introduced by [Kieran Greer](Kieran_Greer "Kieran Greer") et al. and [Levente Kocsis](Levente_Kocsis "Levente Kocsis") et al.



* [Chessmaps Heuristic](Chessmaps_Heuristic "Chessmaps Heuristic")
* [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic") [[8]](#cite_note-8) [[9]](#cite_note-9)


## Typical move ordering


After [move generation](Move_Generation "Move Generation") with assigned move-scores, chess programs usually don't sort the whole [move list](Move_List "Move List"), but perform a [selection sort](https://en.wikipedia.org/wiki/Selection_sort) each time a move is fetched. Exceptions are the [Root](Root "Root") and further [PV-Nodes](Node_Types#PV-Node "Node Types") with some distance to the horizon, where one may apply additional effort to score and sort moves. For performance reasons, a lot of programs try to save the [move generation](Move_Generation "Move Generation") of captures or non-captures at expected [Cut-Nodes](Node_Types#Cut-Nodes "Node Types"), but try the hash-move or killer first, if they are proved legal in this position.


A typical move ordering consists as follows:



1. [PV-move](PV-Move "PV-Move") of the [principal variation](Principal_Variation "Principal Variation") from the previous iteration of an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework for the leftmost path, often implicitly done by 2.
2. [Hash move](Hash_Move "Hash Move") from [hash tables](Transposition_Table "Transposition Table")
3. Winning captures/promotions
4. Equal captures/promotions
5. [Killer moves](Killer_Move "Killer Move") (non capture), often with [mate killers](Mate_Killers "Mate Killers") first
6. Non-captures sorted by [history heuristic](History_Heuristic "History Heuristic") and that like
7. Losing captures (\* but see below


* ) Depending on the implementation, the [board representation](Board_Representation "Board Representation"), whether and where [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") is used, the [extension](Extensions "Extensions") policy ([recapture extensions](Recapture_Extensions "Recapture Extensions")) and other stuff - many programmers favor losing captures before other none-captures - directly behind the killers. They are kind of forced, and one possibly has to deal with all kind of tactical motives and interactions, one may not consider in move ordering. Such as [pins](Pin "Pin"), [batteries](Battery "Battery"), [discovered attacks](Discovered_Attack "Discovered Attack") and [overloaded defenders](Overloading "Overloading"). Otherwise, obviously losing captures are likely refuted cheaply. But if a losing capture fails high for some reason, we have saved the effort to generate, and more importantly to search other non-captures at all.


## Node Type Considerations


Move ordering and scoring effort might be controlled by expected [Node Types](Node_Types "Node Types"). 



### PV-nodes


At [PV-nodes](Node_Types#PV-Node "Node Types") move ordering is very important, since the best alpha-increase as early as possible makes further search cheaper, due to narrower windows in [Alpha-Beta](Alpha-Beta "Alpha-Beta"), while in [PVS](Principal_Variation_Search "Principal Variation Search") later but better moves require re-searches of the [null window](Null_Window "Null Window") [scout](Scout "Scout"). 



### Cut-nodes


Move ordering is crucial at expected and confirmed [Cut-nodes](Node_Types#Cut-Nodes "Node Types"), since it is important to [fail-high](Fail-High "Fail-High") as early as possible, as best with the first move, as in greater than 90% of all [fail-high nodes](Node_Types#Cut-Nodes "Node Types"). However, in situations where multiple moves may cut, e.g. with huge [material](Material "Material") advantage, we like it as cheap as possible, but not necessarily a huge subtree with f.i. due to [check extensions](Check_Extensions "Check Extensions"). 



### All-nodes


At confirmed [ALL-nodes](Node_Types#All-Nodes "Node Types") with [null windows](Null_Window "Null Window"), move ordering didn't care that much. Since we don't know in advance (otherwise we wouldn't search at all), and expected All-nodes may become Cut-nodes, move ordering is an issue as well, but usually with less effort for late moves. 



## Depth and Ply Considerations


Move ordering effort might be controlled by considering [draft](Depth "Depth") and/or [plies](Ply "Ply") from [root](Root "Root"). The closer the root, the farther the horizon, the more effort might be justified to score and sort moves.




### Root Node Considerations


Despite trying the best move and principal variation from previous iteration first, iterative deepening offers another ressource to order the remaining moves at the [root](Root "Root") - their subtree size which could be easily determined. As already mentioned by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") in an [1992 ICCA Journal](ICGA_Journal#15_1 "ICGA Journal") correspondence [[10]](#cite_note-10) inspired by [Jos Uiterwijk's](Jos_Uiterwijk "Jos Uiterwijk") [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") article [[11]](#cite_note-11), based on the soundness of following rule of thumb,





|  |
| --- |
| *The longer it takes to refute a move, the higher is its chance to become best move in the next iteration* |


the old idea is to use the search time or subtree size of the depth-n iteration to reorder the direct successors of the root before the depth-(n+1) iteration. Some programs use the [evaluation](Evaluation "Evaluation") to initially score the moves, to adjust them by their subtree size in subsequent iterations.


An [idea](Ronald_de_Man#ScoringRootMoves "Ronald de Man") to apply randomness and/or bonuses, i.e. developing bonus, or penalties to [move](Moves "Moves") [scores](Score "Score") at the [root](Root "Root") by an [oracle](Oracle "Oracle") approach, was proposed by [Ronald de Man](Ronald_de_Man "Ronald de Man") - without any changes in [alpha-beta search](Alpha-Beta "Alpha-Beta") or [leaf evaluation](Evaluation "Evaluation"), and without any problems with the [transposition table](Transposition_Table "Transposition Table") [[12]](#cite_note-12) [[13]](#cite_note-13).



### Ordering in Quiescence


In the [quiescence search](Quiescence_Search "Quiescence Search"), [captures](Captures "Captures") are often approximated, for speed. For example, PxQ need not have a [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") performed on it, since it is clearly a winning capture, where RxB might have the SEE done, to see if it is a winning or possibly losing capture if the bishop is protected.



## See also


* [Fixafan](Fixafan "Fixafan")
* [Move Generation](Move_Generation "Move Generation")
* [Move List](Move_List "Move List")
* [Node Types](Node_Types "Node Types")


 [Number of Leaf Nodes](Node_Types#LeafNodes "Node Types")
* [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
* [Search Explosion](Search_Explosion "Search Explosion")


## Publications


### 1977 ...


* [Selim Akl](Selim_Akl "Selim Akl"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *The Principal Continuation and the Killer Heuristic*.1977 ACM Annual Conference Proceedings
* [Ozalp Babaoglu](Ozalp_Babaoglu "Ozalp Babaoglu") (**1977**). *Hardware implementation of the legal move generation and relative ordering functions for the game of chess*. Master's thesis, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley")


### 1980 ...


* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](ICGA_Journal#6_3 "ICGA Journal")
* [Prakash Bettadapur](Prakash_Bettadapur "Prakash Bettadapur") (**1986**). *Influence of Ordering on Capture Search*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")


### 1990 ...


* [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [Peter Kouwenhoven](Peter_Kouwenhoven "Peter Kouwenhoven") (**1991**). *Sundry Computer Chess Topics*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
* [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
* [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *Memory Efficiency in some Heuristics*. [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1992**). *Move Ordering by Time Ordering*. Correspondence, [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
* [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University"), advisor [Monroe Newborn](Monroe_Newborn "Monroe Newborn") » [Fixafan](Fixafan "Fixafan")
* [Yi-Fan Ke](Yi-Fan_Ke "Yi-Fan Ke"), [Tai-Ming Parng](Tai-Ming_Parng "Tai-Ming Parng") (**1993**). *The Guard Heuristic: Legal Move Ordering with Forward Game-Tree Pruning*. [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16-2 "ICGA Journal")
* [Mei-En Chen](index.php?title=Mei-En_Chen&action=edit&redlink=1 "Mei-En Chen (page does not exist)"), [Yo-Ping Huang](index.php?title=Yo-Ping_Huang&action=edit&redlink=1 "Yo-Ping Huang (page does not exist)") (**1995**). *[Guard heuristic by dynamic fuzzy reasoning model for Chinese chess](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=527751)*. Proceedings of ISUMA-NAFIPS '95
* [Kieran Greer](Kieran_Greer "Kieran Greer"), [Piyush Ojha](index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1999**). *A Pattern-Oriented Approach to Move Ordering: the Chessmaps Heuristic*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")


### 2000 ...


* [Kieran Greer](Kieran_Greer "Kieran Greer") (**2000**). *[Computer chess move-ordering schemes using move influence](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6TYF-40TY77M-3&_user=10&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=7858eb0d6e100295c197661d1d454e26)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 120, No. 2
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Move Ordering using Neural Networks*. IEA/AIE 2001, [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2070
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002")
* [Yoshinori Higashiuchi](index.php?title=Yoshinori_Higashiuchi&action=edit&redlink=1 "Yoshinori Higashiuchi (page does not exist)"), [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen") (**2005**). *Enhancing Search Efficiency by Using Move Categorization Based on Game Progress in Amazons*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.100.3211&rep=rep1&type=pdf)
* [Mark Winands](Mark_Winands "Mark Winands"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2006**). *The Relative History Heuristic*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://www.personeel.unimaas.nl/m-winands/documents/relhis.pdf)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2006**). *[Driving search with Plausibility analysis: Looking at the right moves](http://www.aifactory.co.uk/newsletter/2005_04_plausibility_analysis.htm)*. [AI Factory](AI_Factory "AI Factory"), Winter 2006
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2007**). *[Negative Plausibility](http://www.aifactory.co.uk/newsletter/2007_01_neg_plausibility.htm)*. [AI Factory](AI_Factory "AI Factory"), Spring 2007 » [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")
* [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2007**). *[Computing Elo Ratings of Move Patterns in the Game of Go](http://remi.coulom.free.fr/Amsterdam2007/)*. [ICGA Journal, Vol. 30, No. 4](ICGA_Journal#30_4 "ICGA Journal"), [CGW 2007](CGW_2007 "CGW 2007"), [pdf](http://remi.coulom.free.fr/Amsterdam2007/icgaj.pdf) [[14]](#cite_note-14)
* [Timothy Furtak](index.php?title=Timothy_Furtak&action=edit&redlink=1 "Timothy Furtak (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro") (**2009**). *Minimum Proof Graphs and Fastest-Cut-First Search Heuristics*. [IJCAI 2009](Conferences#IJCAI2009 "Conferences"), [pdf](http://ijcai.org/papers09/Papers/IJCAI09-089.pdf) [[15]](#cite_note-15)


### 2010 ...


* [David J. Wu](David_J._Wu "David J. Wu") (**2011**). *Move Ranking and Evaluation in the Game of Arimaa*. B.Sc. thesis, [Harvard College](https://en.wikipedia.org/wiki/Harvard_College), [Cambridge, Massachusetts](https://en.wikipedia.org/wiki/Cambridge,_Massachusetts), [pdf](http://arimaa.com/arimaa/papers/DavidWu/djwuthesis.pdf) » [Arimaa](Arimaa "Arimaa")
* [David J. Wu](David_J._Wu "David J. Wu") (**2015**). *Designing a Winning Arimaa Program*. [ICGA Journal, Vol. 38, No. 1](ICGA_Journal#38_1 "ICGA Journal")


### 2020 ...


* [Toni Helminen](Toni_Helminen "Toni Helminen") (**2022**). *[Lazy sorting algorithm](https://github.com/SamuraiDangyo/lazy-sorting-algorithm)*. [[16]](#cite_note-16)


## Forum Posts


### 1996 ...


* [Pawn Structure "Holes" and Move Ordering](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7d8a4124ce6f81ac#) by [Daniel A. Thies](index.php?title=Daniel_A._Thies&action=edit&redlink=1 "Daniel A. Thies (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 12, 1996 » [Pawn Structure](Pawn_Structure "Pawn Structure"), [Holes](Holes "Holes")
* [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1997


 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997
 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
* [Move ordering - How do I know if I have played this move already?](https://www.stmintz.com/ccc/index.php?id=48187) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), April 06, 1999
* [Measure of moveorder quality](https://www.stmintz.com/ccc/index.php?id=67397) by [Ralf Elvsén](index.php?title=Ralf_Elvs%C3%A9n&action=edit&redlink=1 "Ralf Elvsén (page does not exist)"), [CCC](CCC "CCC"), September 04, 1999
* [Move Ordering at the Root](https://www.stmintz.com/ccc/index.php?id=68825) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), September 15, 1999
* [Fast way to sort moves in movelist ?](https://www.stmintz.com/ccc/index.php?id=73278) by [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner"), [CCC](CCC "CCC"), October 14, 1999


### 2000 ...


* [Move ordering?](https://www.stmintz.com/ccc/index.php?id=108325) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), April 28, 2000
* [Better subject title: Move ordering](https://www.stmintz.com/ccc/index.php?id=113174) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"). May 31, 2000
* [Move ordering ideas](https://www.stmintz.com/ccc/index.php?id=157570) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), March 08, 2001
* [Dynamic move ordering for capture/promotions?](https://www.stmintz.com/ccc/index.php?id=161474) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), April 02, 2001
* [root search ordening](https://www.stmintz.com/ccc/index.php?id=167401) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](CCC "CCC"), May 02, 2001
* [Move ordering at root of search](https://www.stmintz.com/ccc/index.php?id=168497) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), May 07, 2001
* [A SIMD idea, eg. Piece/Gain of a capture target](https://www.stmintz.com/ccc/index.php?id=343790) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 21, 2004 » [SSE2](SSE2 "SSE2")
* [move ordering and node count](https://www.stmintz.com/ccc/index.php?id=357188) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 29, 2004
* [Move ordering at root](https://www.stmintz.com/ccc/index.php?id=358297) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), April 04, 2004
* [Fail-high on first move stat (86%)](https://www.stmintz.com/ccc/index.php?id=379624) by Michael Henderson, [CCC](CCC "CCC"), July 29, 2004 » [Fail-High](Fail-High "Fail-High")


### 2005 ...


* [Move ordering at different (Knuth) node types](http://www.open-aurec.com/wbforum/viewtopic.php?t=4384) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 21, 2006 » [Node Types](Node_Types "Node Types")
* [move ordering statistic](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4447) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2006
* [SEE on non-capture moves in main search](http://www.talkchess.com/forum/viewtopic.php?t=12706) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 28, 2007 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [caps->noncaps vs. goodcaps->noncaps->badcaps](http://www.talkchess.com/forum/viewtopic.php?t=15198) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), July 18, 2007
* [Move ordering: Delaying moves on the history phase](http://www.talkchess.com/forum/viewtopic.php?t=21119) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), May 13, 2008


 [Re: Move ordering: Delaying moves on the history phase](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=188924) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC](CCC "CCC"), May 14, 2008
* [Order of implementing things](http://www.talkchess.com/forum/viewtopic.php?t=24294) by cyberfish, [CCC](CCC "CCC"), October 10, 2008
* [Negative Plausibility Move Ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=28873) by [Alessandro Damiani](Alessandro_Damiani "Alessandro Damiani"), [CCC](CCC "CCC"), July 09, 2009


### 2010 ...


* [Move ordering help](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=32611) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), February 14, 2010 » [Jabba](Jabba "Jabba")
* [root move ordering](http://www.talkchess.com/forum/viewtopic.php?t=34655) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), June 02, 2010
* [Move ordering improvements](http://www.open-chess.org/viewtopic.php?f=5&t=661) by Howard E, [Open Chess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), September 26, 2010


**2011**



* [out of check move ordering](http://www.talkchess.com/forum/viewtopic.php?t=38387) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), March 12, 2011 » [Check](Check "Check")
* [The LBR move ordering heuristic](http://www.talkchess.com/forum/viewtopic.php?t=38556) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 26, 2011 » [Last Best Reply](Last_Best_Reply "Last Best Reply")
* [Move ordering by PST](http://www.talkchess.com/forum/viewtopic.php?t=38766) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), April 16, 2011 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [History Heuristic](History_Heuristic "History Heuristic"), [Onno](Onno "Onno")
* [Move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=39338) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), June 11, 2011
* [Root node search in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=39346) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), June 12, 2011 » [Stockfish](Stockfish "Stockfish"), [Root](Root "Root")
* [Improve Move Ordering for Alpha Beta](http://macechess.blogspot.de/2011/08/improve-move-ordering-for-alpha-beta.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), August 11, 2011


**2012**



* [Minimax/ Alpha beta pruning Move Ordering?](http://stackoverflow.com/questions/8906430/minimax-alpha-beta-pruning-move-ordering) by Felix, [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), January 18, 2012
* [Move Ordering (Again :))](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42567) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), February 22, 2012
* [Move ordering idea (old and new?)](http://www.talkchess.com/forum/viewtopic.php?t=44749) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), August 09, 2012 » [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [How effective is move ordering from TT?](http://www.talkchess.com/forum/viewtopic.php?t=44745) by [Bill Henry](index.php?title=Bill_Henry&action=edit&redlink=1 "Bill Henry (page does not exist)"), [CCC](CCC "CCC"), August 09, 2012 » [Transposition Table](Transposition_Table "Transposition Table")
* [Relationship between move ordering and pruning](http://www.open-chess.org/viewtopic.php?f=5&t=2173) by [Don Dailey](Don_Dailey "Don Dailey"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 17, 2012 » [Pruning](Pruning "Pruning")
* [Move Ordering?](http://www.talkchess.com/forum/viewtopic.php?t=46605) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), December 28, 2012


**2013**



* [Killer and History: Increased Node Count](http://www.talkchess.com/forum/viewtopic.php?t=46886) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), January 15, 2013
* [Root move order (again)](http://www.talkchess.com/forum/viewtopic.php?t=47564) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), March 21, 2013
* [History pruning / move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=47953) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), May 10, 2013
* [Move ordering contest](http://www.talkchess.com/forum/viewtopic.php?t=48122) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 26, 2013
* [An idea for move ordering at the root](http://www.talkchess.com/forum/viewtopic.php?t=48230) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 09, 2013
* [MoveOrdering++](http://www.talkchess.com/forum/viewtopic.php?t=48981) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), August 16, 2013
* [How do you get a "Best first move" near the leaves](http://www.talkchess.com/forum/viewtopic.php?t=50339) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), December 05, 2013


**2014**



* [Idea of different history](http://www.talkchess.com/forum/viewtopic.php?t=51992) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 14, 2014 » [History Heuristic](History_Heuristic "History Heuristic")
* [Effectiveness of killer moves](http://www.talkchess.com/forum/viewtopic.php?t=53317) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), August 17, 2014
* [Solving a fail low situation at the root](http://www.talkchess.com/forum/viewtopic.php?t=54241) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), November 03, 2014 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")


### 2015 ...


* [Idea #8430: Optimizing move ordering, very slowly](http://www.talkchess.com/forum/viewtopic.php?t=55919) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 06, 2015
* [Move ordering for cheapest refutation](http://www.talkchess.com/forum/viewtopic.php?t=57228) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 09, 2015
* [Bonus for "null move SEE"](http://www.talkchess.com/forum/viewtopic.php?t=57346) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 23, 2015
* [Q: Move ordering, checks](http://www.talkchess.com/forum/viewtopic.php?t=57479) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 02, 2015
* [Ordering of Root moves and search instability !](http://www.talkchess.com/forum/viewtopic.php?t=58055) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Search Instability](Search_Instability "Search Instability")


**2016**



* [Sorting Captures](http://www.talkchess.com/forum/viewtopic.php?t=61021) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), August 03, 2016
* [New killer idea](http://www.talkchess.com/forum/viewtopic.php?t=61260) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 28, 2016
* [Starting with move ordering](http://www.talkchess.com/forum/viewtopic.php?t=61262) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), August 28, 2016
* [Best move statistics](http://www.talkchess.com/forum/viewtopic.php?t=61401) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 12, 2016
* [Searching worse moves first](http://www.talkchess.com/forum/viewtopic.php?t=61420) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 14, 2016
* [move ordering especially ordering&searching of root move](http://www.talkchess.com/forum/viewtopic.php?t=62558) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), December 21, 2016


**2017**



* [Move ordering ?](http://www.talkchess.com/forum/viewtopic.php?t=62827) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 15, 2017
* [Move ordering ?](http://www.talkchess.com/forum/viewtopic.php?t=63048) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 04, 2017
* [Sorting losing captures ?](http://www.talkchess.com/forum/viewtopic.php?t=63275) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 25, 2017
* [Move ordering statistics](http://www.talkchess.com/forum/viewtopic.php?t=63280) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), February 26, 2017
* [speed up or avoiding move sorting](http://www.talkchess.com/forum/viewtopic.php?t=63502) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 19, 2017 » [Zurichess](Zurichess "Zurichess")
* [Testing for Move Ordering Improvements](http://www.talkchess.com/forum/viewtopic.php?t=63555) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), March 25, 2017 » [Engine Testing](Engine_Testing "Engine Testing"), [Search Statistics](Search_Statistics "Search Statistics")
* [Sorting algorithms](http://www.talkchess.com/forum/viewtopic.php?t=63790) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), April 22, 2017
* [What is causing this problem?](http://www.talkchess.com/forum/viewtopic.php?t=64912) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 16, 2017 » [RomiChess](RomiChess "RomiChess")
* [Ordering Capture Moves](http://www.talkchess.com/forum/viewtopic.php?t=65084) by [Jason Fernandez](index.php?title=Jason_Fernandez&action=edit&redlink=1 "Jason Fernandez (page does not exist)"), [CCC](CCC "CCC"), September 06, 2017 » [Move Ordering - Captures](Move_Ordering#Captures "Move Ordering")
* [Marginal hash move](http://www.talkchess.com/forum/viewtopic.php?t=65189) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 16, 2017
* [Unordered moves phenomenon](http://www.talkchess.com/forum/viewtopic.php?t=65365) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), October 03, 2017
* [Move ordering](http://www.talkchess.com/forum/viewtopic.php?t=65675) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), November 09, 2017


**2018**



* [Simple quiet move sorting](http://www.talkchess.com/forum/viewtopic.php?t=66312) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 13, 2018
* [[Discussion] - Measuring move ordering](http://www.talkchess.com/forum/viewtopic.php?t=66684) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 24, 2018


### 2020 ...


* [Idea in move ordering ...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73088) by De Noose Daniel, [CCC](CCC "CCC"), February 14, 2020
* [sort every moves or pickNext](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73930) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 14, 2020
* [Testing Move Order Quality](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74325) by Cheney, [CCC](CCC "CCC"), June 29, 2020
* [Using piece-square table score for move ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74752) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), August 11, 2020 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")


**2021**



* [Sorting moves during move ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76491) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 04, 2021
* [Hash move ordering vs. Hash cuts: savings in number of nodes visited](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76887) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021 » [Transposition Table](Transposition_Table "Transposition Table")
* [Best move from previous iteration first: still needed with TT?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76888) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021 » [Hash Move](Hash_Move "Hash Move"), [PV-Move](PV-Move "PV-Move")
* [Move ordering heuristics for captures](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77152) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 23, 2021
* [Qsearch dynamic order besides MVV/LVA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77380) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), May 25, 2021 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [PV-move ordering necessary if you have TT-move ordering?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77593) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), July 01, 2021 » [Hash Move](Hash_Move "Hash Move"), [PV-Move](PV-Move "PV-Move")
* [About move ordering and TT hitrate](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78474) by Giovanni Maria Manduca, [CCC](CCC "CCC"), October 22, 2021 » [Transposition Table](Transposition_Table "Transposition Table")
* [Move ordering at the root](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78552) by Jonathan McDermid, [CCC](CCC "CCC"), October 30, 2021 » [Root](Root "Root")


**2022**



* [Move ordering using SEE](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79077) by Christian Dean, [CCC](CCC "CCC"), January 08, 2022 » [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Lazy sorting algorithm - Sorting on steroids](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79279) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), February 03, 2022
* [Having trouble understanding advanced move ordering techniques](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79342) by Pedro Duran, [CCC](CCC "CCC"), February 10, 2022
* [Failure of trivial approach to neural network move ordering](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79368) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), February 16, 2022 » [Neural Networks](Neural_Networks "Neural Networks")


## External Links


* [Move Ordering in Rebel](https://web.archive.org/web/20120413083131/http://www.top-5000.nl/authors/rebel/chess840.htm#MOVE%20ORDERING) by [Ed Schröder](Ed_Schroder "Ed Schroder") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Hiromi Uehara](Category:Hiromi_Uehara "Category:Hiromi Uehara"), [The Trio Project](http://www.cadoganhall.com/event/hiromi-the-trio-project/), feat. [Anthony Jackson](Category:Anthony_Jackson "Category:Anthony Jackson") & [Simon Phillips](Category:Simon_Phillips "Category:Simon Phillips") - Move, (2012), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - [Four Parts](https://commons.wikimedia.org/wiki/File:Four_Parts_MET_sf1991.402.9.jpg?uselang=en), 1932, [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
2. [↑](#cite_ref-2) [Selim Akl](Selim_Akl "Selim Akl"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *The Principal Continuation and the Killer Heuristic*.1977 ACM Annual Conference Proceedings
3. [↑](#cite_ref-3) [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1983**). *The History Heuristic*. [ICCA Journal, Vol. 6, No. 3](ICGA_Journal#6_3 "ICGA Journal")
4. [↑](#cite_ref-4) [Mark Winands](Mark_Winands "Mark Winands"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2006**). *The Relative History Heuristic*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://www.personeel.unimaas.nl/m-winands/documents/relhis.pdf)
5. [↑](#cite_ref-5)  [Move Ordering in Rebel](https://web.archive.org/web/20120413083131/http://www.top-5000.nl/authors/rebel/chess840.htm#MOVE%20ORDERING) by [Ed Schröder](Ed_Schroder "Ed Schroder") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)), also available as [pdf](http://members.home.nl/matador/Inside%20Rebel.pdf)
6. [↑](#cite_ref-6) [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
7. [↑](#cite_ref-7) [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1988**). *Butterfly Boards*. [ICCA Journal, Vol. 11, Nos. 2/3](ICGA_Journal#11_23 "ICGA Journal")
8. [↑](#cite_ref-8) [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Move Ordering using Neural Networks*. IEA/AIE 2001, [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2070
9. [↑](#cite_ref-9) [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002")
10. [↑](#cite_ref-10) [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1992**). *Move Ordering by Time Ordering*. Correspondence, [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
11. [↑](#cite_ref-11) [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
12. [↑](#cite_ref-12) [Re: random play](https://groups.google.com/d/msg/rec.games.chess.computer/AI3xadkLEIk/UUqnp9J3BaMJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 28, 1996
13. [↑](#cite_ref-13) [Re: computer chess "oracle" ideas...](https://groups.google.com/d/msg/rec.games.chess.computer/me7GkjsEgds/iC_ZJm5UwswJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997, see also [Re: mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=390268) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 04, 2004 » [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [Null Move](Null_Move_Pruning "Null Move Pruning") and [WAC](Win_at_Chess "Win at Chess") booster
14. [↑](#cite_ref-14) [Bradley–Terry model from Wikipedia](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model)
15. [↑](#cite_ref-15) [Re: Move ordering for cheapest refutation](http://www.talkchess.com/forum/viewtopic.php?t=57228&start=6) by [Mikko Aarnos](Mikko_Aarnos "Mikko Aarnos"), [CCC](CCC "CCC"), August 10, 2015
16. [↑](#cite_ref-16) [Lazy sorting algorithm - Sorting on steroids](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79279) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), February 03, 2022

**[Up one level](Search "Search")**







 
