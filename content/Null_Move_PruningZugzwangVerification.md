---
title: Null Move PruningZugzwangVerification
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Pruning](Pruning "Pruning") \* Null Move Pruning**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc5) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Signals <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Null Move Pruning**,  

also called Null Move Heuristic (**NMH**), is a method based on the [Null Move Observation](Null_Move_Observation "Null Move Observation") to reduce the search space by trying a ["null" or "passing" move](Null_Move "Null Move"), then seeing if the score of the subtree search is still high enough to cause a beta cutoff. Nodes are saved by [reducing](Reductions "Reductions") the [depth](Depth "Depth") of the subtree under the null move. The value of this depth reduction is known as [R](Depth_Reduction_R "Depth Reduction R"). 



### Mater II


In computer chess, Null Move was already used in threatening [mate in one](Checkmate "Checkmate") detection, as elaborated by [George Baylor](George_Baylor "George Baylor") and [Herbert Simon](Herbert_Simon "Herbert Simon") in *A chess mating combinations program*, 1966, the description of [Mater II](Mater#MaterII "Mater") <a id="cite-note-2" href="#cite-ref-2">[2]</a> .




```C++Routine G17 asks if a proposed move threatens mate in one move. It determines the answer by assuming Black does nothing on his turn, that is, by playing a "No Move" and then seeing if White can enforce an immediate checkmate. 

```

### Kaissa


Null Move pruning was already used in [Kaissa](Kaissa "Kaissa"), as described by their authors **1975** in *Some Methods of Controlling the Tree Search in Chess Programs* <a id="cite-note-3" href="#cite-ref-3">[3]</a> , at the end of chapter 2:




```C++**2. The Order of Move Considerations**:
A less trivial idea was that sometimes an extension of the game tree by introducing of dummy move can lead to a reduction of the search tree. In positions with material advantage (with respect to limits) it was permitted to try a so-called "blank" move in which ones own pieces are not moved. Certainly in positions with "[Zugzwang](Zugzwang "Zugzwang")" (the side to move must weaken his position) this may lead to errors.

```


```C++However, the standard of the program's play is still such that such errors do not essentially lower it. (We plan to develop in the future a procedure for recognizing "Zugzwang" positions, and to forbid a blank move in them.) The reduction of search takes place in this case, because the blank move proves to be a closing one and furthermore does not generate complex forcing variations. 

```





### Beal's NMQS


Null move was further examined by [Don Beal](Don_Beal "Don Beal"), as already elaborated in his [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5") lecture. He proposed a so called **Null Move Quiescence Search** (NMQS) as a selective layer between a regular full width search and [quiescence search](Quiescence_Search "Quiescence Search"), later dubbed **Generalized Quiescence Search** <a id="cite-note-4" href="#cite-ref-4">[4]</a>. The full width search was called with two depth parameters, both considered inside the [transposition table](Transposition_Table "Transposition Table"), full-depth and q-depth. Full-depth was recursively decremented as usual, but instead of calling quiescence at the full-depth horizon, NMQS with q-depth was called - q-depth recursively decremented in this layer as well. As long as q-depth is greater than zero, the [hash move](Hash_Move "Hash Move"), if any, is searched first regularly. Next, NMQS calls quiescence for the other side to move, to check for a possible null move [beta-cutoff](Beta-Cutoff "Beta-Cutoff"), before proceeding the remaining moves in usual manner. As pointed out by [Chun Ye](Chun_Ye "Chun Ye") in his 1992 thesis <a id="cite-note-5" href="#cite-ref-5">[5]</a>, NMQS permits more flexible [iterative deepening](Iterative_Deepening "Iterative Deepening") concerning full-depth in an outer and q-depth in an inner loop. 



### Schaeffer


In his 1987 [ICCA Journal](ICGA_Journal "ICGA Journal") paper *Speculative Computing*, [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") mentioned *The Null-Move Algorithm* or *Don Beal's null-move*, and used it non-[recursively](Recursion "Recursion") up to once per search path in his tactical [scout](Scout "Scout") solver *Minix* (Mini-Phoenix), which up and then gave the parallel running [Phoenix](Phoenix "Phoenix"), which was a less deep searcher than *Minix*, some tactical hints <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### Goetsch and Campbell


[Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") and [Murray Campbell](Murray_Campbell "Murray Campbell") published the results of some experiments with Null move pruning in 1988 and 1990 <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>, already considering [recursive](Recursion "Recursion") NMP with [depth reduction](Depth_Reduction_R "Depth Reduction R") of 1, also mentioned in [Chun Ye's](Chun_Ye "Chun Ye") 1992 thesis with source code as implemented inside the [Chinese Chess](Chinese_Chess "Chinese Chess") program [Abyss](Abyss "Abyss") <a id="cite-note-9" href="#cite-ref-9">[9]</a> .



### Morsch and Donninger


Null move pruning was used [recursively](Recursion "Recursion") to possibly occur multiple times inside a path of the search by [Frans Morsch](Frans_Morsch "Frans Morsch") <a id="cite-note-10" href="#cite-ref-10">[10]</a> inside his chess engines [Quest](Quest "Quest") and [Fritz](Fritz "Fritz"). Frans exchanged his ideas with [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), who popularized null move by his *Null Move and Deep Search* paper in the [ICCA Journal](ICGA_Journal "ICGA Journal") [1993](Timeline#1993 "Timeline") <a id="cite-note-11" href="#cite-ref-11">[11]</a> .




## Schemes


Most typical engines use [recursive](Recursion "Recursion") null move with an [R](Depth_Reduction_R "Depth Reduction R") value of 2 or 3. Recursive null move pruning is simply allowing more than one null move in one branch of the search. [Fruit](Fruit "Fruit") uses a depth [reduction](Reductions "Reductions") factor R=3, with no null move pruning when down to king and pawns for the side to move, or when in check. The default for [Fruit](Fruit "Fruit") is to try a null search if the static [evaluation](Evaluation "Evaluation") is greater than [beta](Beta "Beta"), or the depth less than four. Newer versions of [Fruit](Fruit "Fruit") as well as [Toga](Toga "Toga") default to always doing a null search, as long as there is at least one piece of value greater than a pawn for that side.




### Adaptive Null Move Pruning


[Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") proposed refinements with Adaptive Null Move Pruning <a id="cite-note-12" href="#cite-ref-12">[12]</a> . Some programs vary R with [depth](Depth "Depth"), or based on [evaluation](Evaluation "Evaluation") features, such as being in or near the [endgame](Endgame "Endgame").



### Restrictions on use


Obviously, the null move cannot be used when the side to move is in check, because that would result in an illegal position. But there are more less obvious restrictions on using null move safely. The theoretical basis of null move pruning, as coined by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), is the [null move observation](Null_Move_Observation "Null Move Observation"). The null move observation is the fact that in chess, in almost every position, the side to move will have a move to play that is better than doing nothing.


There are a few situations in which this assumption does not hold. The null move will produce very bad results in [zugzwang](Zugzwang "Zugzwang") positions - positions in which not moving would be the best move, if it were legal. For this reason, some conditions must be used for when the null move is tried in search. Most engines do not try the null move in the [endgame](Endgame "Endgame"), because that is where zugzwang positions are most likely to occur, because there are fewer pieces to move. It is debatable whether a programmer should allow the null move search descend directly to the [quiescence search](Quiescence_Search "Quiescence Search"). Most probably it is worthwile only with more tactically aware versions of quiescence.


Some other ways to combat the negative effect of the null move observation are listed here:




### Zugzwang Verification


Concerning null move failures in [zugzwang](Zugzwang "Zugzwang") <a id="cite-note-13" href="#cite-ref-13">[13]</a> , there were proposals by [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner") 1995, <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a> and later the *Verified Null-Move Pruning* approach by [Eli David](Eli_David "Eli David") and [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") <a id="cite-note-16" href="#cite-ref-16">[16]</a> . Recently [Robert Hyatt](Robert_Hyatt "Robert Hyatt") tested *Verified Null-Move Pruning* extensively with a lot of variations and depth reductions for the verified search, and concluded it does not help at all in [Crafty](Crafty "Crafty") <a id="cite-note-17" href="#cite-ref-17">[17]</a> similar with [extended null-move reductions](Null_Move_Reductions "Null Move Reductions") <a id="cite-note-18" href="#cite-ref-18">[18]</a> <a id="cite-note-19" href="#cite-ref-19">[19]</a> . However, [Marco Costalba](Marco_Costalba "Marco Costalba") states that verification search has almost nothing to do with zugzwang <a id="cite-note-20" href="#cite-ref-20">[20]</a> .




### Double Null Move


Widely discussed in [computer chess forums](Computer_Chess_Forums "Computer Chess Forums") was the [Double Null Move](Double_Null_Move "Double Null Move") idea by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") to perform two consecutive null moves to detect zugzwang <a id="cite-note-21" href="#cite-ref-21">[21]</a> .




### Variable NM Bound


The idea to permit a null move cutoff not only if the null move search returns a value greater than or equal to beta, but also if the value is slightly less - that is using a bound of beta minus some [tempo](Tempo "Tempo") bonus, was already proposed by [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") and [Murray Campbell](Murray_Campbell "Murray Campbell") in 1988 as future research idea <a id="cite-note-22" href="#cite-ref-22">[22]</a> . [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") and [Tony Marsland](Tony_Marsland "Tony Marsland") substantiated the idea as implemeted in [The Turk](The_Turk "The Turk"), where the number of potentially good alternative moves (numPGAM) per side in the path from the [root](Root "Root") to the current node as estimated by positive scores of generated moves from the [history heuristic](History_Heuristic "History Heuristic"), was used to determine a tempo bonus of 10 or 20 [centipawns](Centipawns "Centipawns") - the higher numPGAM, the lower the probability that an erroneous forward pruning decision will propagate up the tree <a id="cite-note-23" href="#cite-ref-23">[23]</a> .




```C++
if ( nullMoveAllowed &&  ...) {
   int bound = beta;
   if ( inNullMoveSearch == 0 ) {
      tempo = 10*(numPGAM > 0) + 10* numPGAM > 15);
      bound -= tempo; // variable bound
   }
   makeNullMove(); ++inNullMoveSearch;
   score = -zwSearch(1-bound, depth-R-1)
   unmakeNullMove(); --inNullMoveSearch;
   if ( score >= bound ) {
      return beta; // null move pruning
   }
}

```

*For zwSearch, see [Zero Window Search](Principal_Variation_Search#ZWS "Principal Variation Search") inside the [Principal Variation Search](Principal_Variation_Search "Principal Variation Search").*




## Threat Detection


### Mate Threats


As suggested in Donninger's paper, concerning the deep search, null move is not only about pruning, but also about detecting [threat moves](Threat_Move "Threat Move") by the opponent to improve further [move ordering](Move_Ordering "Move Ordering") and to possibly trigger [mate threat extensions](Mate_Threat_Extensions "Mate Threat Extensions") <a id="cite-note-24" href="#cite-ref-24">[24]</a> <a id="cite-note-25" href="#cite-ref-25">[25]</a> <a id="cite-note-26" href="#cite-ref-26">[26]</a> <a id="cite-note-27" href="#cite-ref-27">[27]</a> . However, some kind of [fail-soft](Fail-Soft "Fail-Soft") framework is necessary to recognize "I get mated, if I do nothing", otherwise the hard bound of a [null window](Null_Window "Null Window") null-move search around [beta](Beta "Beta") will limit the [upper bound](Upper_Bound "Upper Bound") to beta-1 <a id="cite-note-28" href="#cite-ref-28">[28]</a> . Another, possibly too expensive solution with a [fail-hard](Fail-Hard "Fail-Hard") framework, is to play a bit with the search window, if the null move doesn't fail high:




```C++
if ( nullMoveAllowed && depth >= X && ...) {
   makeNullMove()
   score = -zwSearch(1-beta, depth-R-1) // -AlphaBeta (0-beta, 1-beta, depth-R-1)
   if (score >= beta ) {
      // fail high on null move
      unmakeNullMove();
      return beta; // null move pruning
   } else {
      if ( zwSearch( VALUE_MATE/2, depth-R-1) > VALUE_MATE/2 )
         extend; // mate threat extension inside a fail hard framework
      unmakeNullMove();
   }
}

```

### Botvinnik-Markoff Extension


Null move is also the base of the [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension"), as proposed by [Sergei Markoff](Sergei_Markoff "Sergei Markoff") - as a tribute to the computer chess pioneer and former [World Chess Champion](https://en.wikipedia.org/wiki/World_Chess_Championship) [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik"), who addressed related issues in his publications <a id="cite-note-29" href="#cite-ref-29">[29]</a> .



### Influence on Move Ordering


Most of the time, null move is refuted by a [capture](Captures "Captures"). Therefore it makes sense to extract a move that refuted null move from the [transposition table](Transposition_Table "Transposition Table"), record the [target square](Target_Square "Target Square") of such a move, to give a [move ordering](Move_Ordering "Move Ordering") boost for escaping from that square. Also, there is a strong conjecture that in programs using [history move ordering](History_Heuristic "History Heuristic"), even a failed null move search helps by filling the history tables faster.



## Test Results


* [Null Move Pruning Test Results](Null_Move_Pruning_Test_Results "Null Move Pruning Test Results") - various experimental test results of null move pruning
* [Null Move Test-Positions](Null_Move_Test-Positions "Null Move Test-Positions"), where Null Move may fail due to zugzwang


## See also


* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")
* [Extensions](Extensions "Extensions")
* [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions")
* [Knowledge | Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
* [Multi-Cut](Multi-Cut "Multi-Cut")
* [Null Move Observation](Null_Move_Observation "Null Move Observation")
* [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
* [ProbCut](ProbCut "ProbCut")
* [Reductions](Reductions "Reductions")
* [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (Static Null Move Pruning)


## Publications


### 1966


* [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. AFIPS Joint Computer Conferences, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1975


* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1975**). *Some Methods of Controlling the Tree Search in Chess Programs*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp. 361-371. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")


### 1980 ...


* [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1988**). *Experimenting with the Null Move Heuristic in Chess*. AAAI Spring Symposium Proceedings, pp. 14-18.
* [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), a revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702, edited version in (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, IKAT, ISBN 90-62-16-6348. Chapter 10, pp. 101-116


### 1990 ...


* [Don Beal](Don_Beal "Don Beal") (**1990**). *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702
* [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1990**). *[Experiments with the Null-Move Heuristic](https://link.springer.com/chapter/10.1007/978-1-4613-9080-0_9)*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition"), pp. 159-168
* [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
* [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner") (**1995**). *A Null-Move Technique Impervious to Zugzwang.* [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"). (**1999**). *Adaptive null-move pruning*. [ICCA Journal, Vol. 22, No. 3](ICGA_Journal#22_3 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/adpt_null.ps.gz)


### 2000 ...


* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2000**). *Selective Depth-First Search Methods*. in [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (eds.) (**2000**). *Games in AI Research*. [Universiteit Maastricht](Maastricht_University "Maastricht University"), [pdf preprint](http://www.cs.ualberta.ca/%7Etony/RecentPapers/nec97w.pdf)
* [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2002**). *Verified null-move pruning.* [ICGA Journal, Vol. 25 No. 3](ICGA_Journal#25_3 "ICGA Journal") <a id="cite-note-30" href="#cite-ref-30">[30]</a> <a id="cite-note-31" href="#cite-ref-31">[31]</a>
* [Don Beal](Don_Beal "Don Beal") (**2006**). *Review of a nullmove-quiescence search mechanism from 1986*. [File:Alg1986review.txt](File:Alg1986review.txt "File:Alg1986review.txt") (Draft) <a id="cite-note-32" href="#cite-ref-32">[32]</a>
* [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.oedavid.com/pubs/nmr.pdf)


### 2010 ...


* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Masakazu Muramatsu](Masakazu_Muramatsu "Masakazu Muramatsu") (**2012**). *[Efficiency of three Forward-Pruning Techniques in Shogi: Futility Pruning, Null-move Pruning, and Late Move Reduction (LMR)](https://www.semanticscholar.org/paper/Efficiency-of-three-forward-pruning-techniques-in-Hoki-Muramatsu/206099961f401c8693e071c2b739f164ae5ffa6c)*. [Entertainment Computing](https://www.journals.elsevier.com/entertainment-computing), Vol. 3, No. 3
* [Daniel S. Abdi](Daniel_Shawul "Daniel Shawul") (**2013**). *Analysis of pruned minimax trees*. [pdf](https://dl.dropboxusercontent.com/u/55295461/analysis/pruning.pdf) » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")


## Forum Posts


### 1995 ...


* [Null Move heuristic](http://groups.google.com/group/rec.games.chess/browse_frm/thread/4240e92cca890050) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 28, 1995


**1997**



* [Null move depth reductions](https://groups.google.com/d/msg/rec.games.chess.computer/JJTEBafyuYM/hRTys0ZxcUIJ) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 02, 1997 » [Depth Reduction R](Depth_Reduction_R "Depth Reduction R")
* [Null move?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/3eb37f017c1857fe) by MLC, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 07, 1997
* [Searching correctly with the Nullmove ==> no zugzwang problems anymore](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8b835621f7790967) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 23, 1997


**1998**



* [During Null Move search](https://www.stmintz.com/ccc/index.php?id=19827) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), June 02, 1998
* [Extend or not extend in a nullmove tree](https://www.stmintz.com/ccc/index.php?id=20167) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), June 08, 1998 » [Extensions](Extensions "Extensions")
* [Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20596) by [Dezhi Zhao](index.php?title=Dezhi_Zhao&action=edit&redlink=1 "Dezhi Zhao (page does not exist)"), [CCC](CCC "CCC"), June 15, 1998 » [Null Window](Null_Window "Null Window")
* [search extension](https://www.stmintz.com/ccc/index.php?id=21888) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), July 08, 1998 » [Threat Detection](#ThreatDetection)
* [Null move reductions](https://www.stmintz.com/ccc/index.php?id=28772) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 04, 1998


**1999**



* [Null move](https://www.stmintz.com/ccc/index.php?id=42137) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), February 03, 1999
* [Confusion on Null Move](https://www.stmintz.com/ccc/index.php?id=42804) by [KarinsDad](index.php?title=KarinsDad&action=edit&redlink=1 "KarinsDad (page does not exist)"), [CCC](CCC "CCC"), February 09, 1999


 [A Null Move Enhancement?](https://www.stmintz.com/ccc/index.php?id=42909) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), February 10, 1999 
* [Singular Extensions, Nullmove deepsearch](https://www.stmintz.com/ccc/index.php?id=43328) by [Frank Schneider](Frank_Schneider "Frank Schneider"), [CCC](CCC "CCC"), February 16, 1999 » [Singular Extensions](Singular_Extensions "Singular Extensions")
* [NULL MOVE](https://www.stmintz.com/ccc/index.php?id=44363) by Sylvain Lacombe, [CCC](CCC "CCC"), February 24, 1999


 [To skin a cat (was Re: NULL MOVE)](https://www.stmintz.com/ccc/index.php?id=44497) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), February 24, 1999
* [Null move around (beta-1, beta)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/0e56bda426a70a22#) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 05, 1999
* [Null move idea](https://www.stmintz.com/ccc/index.php?id=54279) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), June 04, 1999
* [Null move mate extension](https://www.stmintz.com/ccc/index.php?id=57953) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), June 25, 1999
* [It is a nullmove killer (zugzwang)](https://www.stmintz.com/ccc/index.php?id=76399) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), November 05, 1999 » [Zugzwang](Zugzwang "Zugzwang")


 [Pseudo-code for verification search](https://www.stmintz.com/ccc/index.php?id=76542) by [Dan Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), November 06, 1999
### 2000 ...


* [Pseudo C code for double nullmove + PVS](https://www.stmintz.com/ccc/index.php?id=123156) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), August 06, 2000
* [double nullmove??](https://www.stmintz.com/ccc/index.php?id=123206) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), August 06, 2000 » [Double Null Move](#DoubleNullMove)
* [is this nullmove? problems in pulsar algorithm](https://www.stmintz.com/ccc/index.php?id=129985) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), September 20, 2000 » [Pulsar](Pulsar "Pulsar")
* [Re: ZChess getting much stronger...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=32639&start=1) by [Franck Zibi](Franck_Zibi "Franck Zibi"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 10, 2000 » [BBchess](BBchess "BBchess"), [ZChess](ZChess "ZChess")


**2001**



* [Can nullmoves behave like this?](https://www.stmintz.com/ccc/index.php?id=148745) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 08, 2001
* [Nullmove: when to avoid it?](https://www.stmintz.com/ccc/index.php?id=156376) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), February 28, 2001
* [An idea for all you chess programmers.](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=33381&p=126413) by Paul, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 16, 2001
* [Double Nullmove](https://www.stmintz.com/ccc/index.php?id=160954) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), March 30, 2001
* [Double Null move?](https://www.stmintz.com/ccc/index.php?id=179604) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), July 13, 2001
* [Null move R=2 vs Null move R=2/3](https://www.stmintz.com/ccc/index.php?id=183089) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 09, 2001 » [Depth Reduction R](Depth_Reduction_R "Depth Reduction R")


**2002**



* [Crafty-IsiChess,CCT4,r11 ==> A move to avoid?](https://www.stmintz.com/ccc/index.php?id=210702) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), January 29, 2002
* [Double Nullmove](https://www.stmintz.com/ccc/index.php?id=225990) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), April 25, 2002
* [Null-Move: Difference between R = 2 and R = 3 in action](https://www.stmintz.com/ccc/index.php?id=239907) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), July 11, 2002
* [Verified Null-Move Pruning, ICGA 25(3)](https://www.stmintz.com/ccc/index.php?id=266356) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), November 20, 2002
* [new thoughts on verified null move](https://www.stmintz.com/ccc/index.php?id=267039) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), November 23, 2002


**2003**



* [An interesting forward pruning experiment - with pseudo description](https://groups.google.com/d/msg/rec.games.chess.computer/iECalt6Tzug/GWNOLzFQyk8J) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 08, 2003
* [wacnew.epd & single search improvements (nullmove)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43033) by [Stefan Knappe](Stefan_Knappe "Stefan Knappe"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 17, 2003 » [Matador](Matador "Matador"), [Win at Chess](Win_at_Chess "Win at Chess")
* [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003 » [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension")
* [a question to Tord about detecting threats in null move](https://www.stmintz.com/ccc/index.php?id=319187) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 03, 2003


**2004**



* [Re: not using nullmove?](https://www.stmintz.com/ccc/index.php?id=348841) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 13, 2004
* [mtd(f) and null move](https://www.stmintz.com/ccc/index.php?id=354078) by [Peter Alloysius](Peter_Aloysius_Harjanto "Peter Aloysius Harjanto"), [CCC](CCC "CCC"), March 11, 2004 » [MTD(f)](MTD(f) "MTD(f)")
* [When to do a null move search - an experiment](https://www.stmintz.com/ccc/index.php?id=361766) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 26, 2004
* [double null move help](https://www.stmintz.com/ccc/index.php?id=373804) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), July 04, 2004
* [An MTD(f) question about NULL MOVE searching](https://www.stmintz.com/ccc/index.php?id=377240) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 16, 2004 » [MTD(f)](MTD(f) "MTD(f)")
* [null move question(Fruit)](https://www.stmintz.com/ccc/index.php?id=378541) by [Jan K.](index.php?title=Jan_Kaan&action=edit&redlink=1 "Jan Kaan (page does not exist)"), [CCC](CCC "CCC"), July 22, 2004
* [Verified Null-moving](https://www.stmintz.com/ccc/index.php?id=381931) by [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [CCC](CCC "CCC"), August 12, 2004 » [Verified Null Move Pruning](#ZugzwangVerification)
* [mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=389013) by [Rick Bischoff](index.php?title=Rick_Bischoff&action=edit&redlink=1 "Rick Bischoff (page does not exist)"), [CCC](CCC "CCC"), September 25, 2004


### 2005 ...


* [recusive null move in iterative search](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2071) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 25, 2005 » [Iterative Search](Iterative_Search "Iterative Search")
* [Reductions and null move refutations](http://www.open-aurec.com/wbforum/viewtopic.php?t=2300) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2005 » [Reductions](Reductions "Reductions"), [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [depthnull](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3004&p=14559) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 04, 2005


**2006**



* [Verified null-move pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4480&p=23303) by [Tom King](Tom_King "Tom King"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2006
* [Simple NULL move enhancement, checks in qsearch](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4660&start=0) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), April 14, 2006


**2007**



* [NMP on ALL nodes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6392) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), April 15, 2007 » [All Nodes](Node_Types#all-nodes "Node Types")
* [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007
* [Null Move](http://www.talkchess.com/forum/viewtopic.php?p=160677) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), November 23, 2007
* [fractal null move](http://www.talkchess.com/forum/viewtopic.php?t=18081) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 28, 2007


**2008**



* [Null move question](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49310) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 30, 2008
* [null move threat extension](http://www.talkchess.com/forum/viewtopic.php?t=24543) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), October 23, 2008


**2009**



* [Null move in quiescence search idea from Don Beal, 1986](http://www.talkchess.com/forum/viewtopic.php?t=29439) by [Eelco de Groot](index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), [CCC](CCC "CCC"), Aug 17, 2009 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Don Beal](Don_Beal "Don Beal")
* [verified null move](http://www.talkchess.com/forum/viewtopic.php?t=28561) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 21, 2009
* [Null-moves and zugzwang](http://www.talkchess.com/forum/viewtopic.php?t=29873) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), September 25, 2009 » [Zugzwang](Zugzwang "Zugzwang")


### 2010 ...


* [Using Heinz in 2010 is not optimal](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=314332&t=31413) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), January 01, 2010
* [Null-move pruning and the hash table](http://www.talkchess.com/forum/viewtopic.php?t=33514) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), March 28, 2010 » [Transposition Table](Transposition_Table "Transposition Table")
* [Null moves gain](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50971) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 13, 2010
* [nullmove and repetitive draw detection](http://www.talkchess.com/forum/viewtopic.php?t=35052) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), June 20, 2010 » [Repetitions](Repetitions "Repetitions")
* [Stockfish null move pre-condition](http://www.talkchess.com/forum/viewtopic.php?t=35543) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), July 22, 2010 » [Stockfish](Stockfish "Stockfish")
* [Extended Null-Move Reductions](http://www.talkchess.com/forum/viewtopic.php?p=367283) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), August 20, 2010


**2011**



* [Less null move pruning by trans map](http://www.talkchess.com/forum/viewtopic.php?t=38409) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
* [Null Move Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38640) by Alex Farley, [CCC](CCC "CCC"), April 03, 2011
* [Null move alternative in endgames](http://www.talkchess.com/forum/viewtopic.php?t=41104) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), November 16, 2011


**2012**



* [TT avoid nullmove flag](http://www.talkchess.com/forum/viewtopic.php?t=44666) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), August 02, 2012 » [Transposition Table](Transposition_Table "Transposition Table")
* [Nullmove vs classic selective search](http://www.talkchess.com/forum/viewtopic.php?t=44686) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 04, 2012 <a id="cite-note-33" href="#cite-ref-33">[33]</a>


**2013**



* [Null Move Fail](http://www.open-chess.org/viewtopic.php?f=5&t=2210) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2013
* [Two questions](http://www.talkchess.com/forum/viewtopic.php?t=47189) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), February 11, 2013
* [nullmove verification vs avoid null](http://www.talkchess.com/forum/viewtopic.php?t=49351) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), September 14, 2013
* [Null move, razoring and mate threats](http://www.talkchess.com/forum/viewtopic.php?t=49863) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 28, 2013 » [Razoring](Razoring "Razoring")
* [Is SF DD greater efficiency would be null move pruning?](http://www.talkchess.com/forum/viewtopic.php?t=50587) by Jonathan Lee, [CCC](CCC "CCC"), December 22, 2013 » [Stockfish](Stockfish "Stockfish")


**2014**



* [fixing the null move search "bug"](http://www.talkchess.com/forum/viewtopic.php?t=51129) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 01, 2014 » [Stockfish](Stockfish "Stockfish")
* [Disabling Null Move Pruning in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=51291) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 15, 2014 » [Stockfish](Stockfish "Stockfish")
* [Null move and LMR](http://www.talkchess.com/forum/viewtopic.php?t=51578) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), March 12, 2014 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Null move pruning on PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=53049) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), July 22, 2014 » [PV-Nodes](Node_Types#pv-node "Node Types")


### 2015 ...


* [Why not two consecutive null moves ?](http://www.talkchess.com/forum/viewtopic.php?t=56272) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), May 07, 2015
* [thoughts on null-move reduction](http://www.talkchess.com/forum/viewtopic.php?t=56672) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), June 14, 2015 » [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
* [Null move: minimum depth](http://www.talkchess.com/forum/viewtopic.php?t=57638) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), September 14, 2015
* [Null Move in Quiescent search](http://www.talkchess.com/forum/viewtopic.php?t=58527) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), December 09, 2015 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Search Pathology](Search_Pathology "Search Pathology")


**2016**



* [When to do null move](http://www.talkchess.com/forum/viewtopic.php?t=60366) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), June 05, 2016
* [Calculating R value for Null Move](http://www.talkchess.com/forum/viewtopic.php?t=60561) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 23, 2016 » [Depth Reduction R](Depth_Reduction_R "Depth Reduction R")
* [Null Move recommendations](http://www.open-chess.org/viewtopic.php?f=5&t=2994) by kickstone, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 29, 2016
* [Null Move in LMR](http://www.talkchess.com/forum/viewtopic.php?t=61086) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), August 10, 2016 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Nullmove bugs](http://www.talkchess.com/forum/viewtopic.php?t=61257) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), August 28, 2016


**2017**



* [What is wrong with doing Nulls & ttcuts in a pv node ?](http://www.talkchess.com/forum/viewtopic.php?t=62890) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 21, 2017 » [PV-Nodes](Node_Types#pv-node "Node Types"), [Transposition Table](Transposition_Table "Transposition Table")
* [NULL Move code question](http://www.open-chess.org/viewtopic.php?f=5&t=3074) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 27, 2017 » [CPW-Engine\_search](CPW-Engine_search "CPW-Engine search")
* [null move](http://www.talkchess.com/forum/viewtopic.php?t=63737) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), April 14, 2017
* [tt move vs null move](http://www.talkchess.com/forum/viewtopic.php?t=64093) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 27, 2017 » [Hash Move](Hash_Move "Hash Move"), [Null Move](Null_Move "Null Move")
* [End game and Null move](http://www.talkchess.com/forum/viewtopic.php?t=64266) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), June 12, 2017
* [Fifty move counter and Null move](http://www.talkchess.com/forum/viewtopic.php?t=64853) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), August 09, 2017 » [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule"), [Halfmove Clock](Halfmove_Clock "Halfmove Clock")
* [Rethinking r in null move](http://www.talkchess.com/forum/viewtopic.php?t=64927) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 18, 2017 » [Depth Reduction R](Depth_Reduction_R "Depth Reduction R")
* [Question on Null Move Pruning](http://www.talkchess.com/forum/viewtopic.php?t=65024) by [Jason Fernandez](index.php?title=Jason_Fernandez&action=edit&redlink=1 "Jason Fernandez (page does not exist)"), [CCC](CCC "CCC"), August 29, 2017
* [Threat detection](http://www.talkchess.com/forum/viewtopic.php?t=65121) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 09, 2017 » [Threat Detection](Null_Move_Pruning#ThreatDetection "Null Move Pruning"), [Threat Move](Threat_Move "Threat Move")


**2018**



* [Making null move better?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=66410) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 25, 2018


**2019**



* [Null move pruning, only when score >= beta?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69722) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 25, 2019
* [idea: null-move analogy](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70118) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 06, 2019


### 2020 ...


* [Allowing null move pruning in the endgame](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73713) by Steven Griffin, [CCC](CCC "CCC"), April 20, 2020 » [Endgame](Endgame "Endgame")
* [Null move](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73753) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), April 24, 2020 » [Stockfish](Stockfish "Stockfish")
* [Null move pruning = lottery?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74498) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), July 18, 2020


## External Links


* Selective Search Techniques in REBEL (null-move) from [Programmer Corner](Rebel#ProgrammerCorner "Rebel") by [Ed Schröder](Ed_Schroder "Ed Schroder") <a id="cite-note-34" href="#cite-ref-34">[34]</a> » [Rebel](Rebel "Rebel")
* A presentation describing the power and flaws in null move pruning: [Null Move pruning](http://www.csse.uwa.edu.au/%7Elucas/files/411_null_move_heuristic_seminar.pdf) (pdf) Slides by [Lucas Bradstreet](http://www.csse.uwa.edu.au/%7Elucas/template.php?content=index)
* [Null-move heuristic from Wikipedia](https://en.wikipedia.org/wiki/Null-move_heuristic)
* [Larry Coryell](Category:Larry_Coryell "Category:Larry Coryell") & [The Eleventh House](Category:The_Eleventh_House "Category:The Eleventh House") - [Ain't It Is (Aspects)](https://en.wikipedia.org/wiki/Aspects_(The_Eleventh_House_album)), 1976, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Terumasa Hino](Category:Terumasa_Hino "Category:Terumasa Hino"), [Gerry Brown](Category:Gerry_Brown "Category:Gerry Brown"), [John Lee](Category:John_Lee "Category:John Lee"), [Mike Mandel](https://www.discogs.com/artist/138771-Mike-Mandel), and guests ... [Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker"), [Randy Brecker](Category:Randy_Brecker "Category:Randy Brecker"), [James Mtume](Category:James_Mtume "Category:James Mtume") et al.
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc5), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1975**). *Some Methods of Controlling the Tree Search in Chess Programs*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp. 361-371. ISSN 0004-3702. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), A revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702.
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1), pp. 57
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1987**). *Speculative Computing*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1988**). *Experimenting with the Null Move Heuristic in Chess*. AAAI Spring Symposium Proceedings, pp. 14-18
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1990**). *[Experiments with the Null-Move Heuristic](https://link.springer.com/chapter/10.1007/978-1-4613-9080-0_9)*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition"), pp. 159-168
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1), pp. 27-29
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: SOMA](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=288321&t=28775) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 26, 2009
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"). (**1999**). *Adaptive null-move pruning*. [ICCA Journal, Vol. 22, No. 3](ICGA_Journal#22_3 "ICGA Journal"), [ps](http://people.csail.mit.edu/heinz/ps/adpt_null.ps.gz)
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Position from local chess club](https://www.stmintz.com/ccc/index.php?id=76352) by Bernhard Bauer, [CCC](CCC "CCC"), November 05, 1999
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner") (**1995**). *A Null-Move Technique Impervious to Zugzwang.* [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Null-move zugzwang avoidance, Jun '95 ICCAJ](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/0840bc8aabd0f6e5#) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") in [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 6, 1996
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2002**). *Verified null-move pruning.* [ICGA Journal, Vol. 25 No. 3](ICGA_Journal#25_3 "ICGA Journal")
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [verified null move](http://www.talkchess.com/forum/viewtopic.php?t=28561) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 21, 2009
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.oedavid.com/pubs/nmr.pdf)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Re: Extended Null-Move Reductions](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=367273&t=35841) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 20, 2010
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Re: Extended Null-Move Reductions](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=367314&t=35841) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 20, 2010
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Re: Null move?](https://groups.google.com/d/msg/rec.games.chess.computer/PrN_AXwYV_4/UXU5x67UaoQJ) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 11, 1997
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1988**). *Experimenting with the Null Move Heuristic in Chess*. AAAI Spring Symposium Proceedings, pp. 14-18
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2000**). *Selective Depth-First Search Methods*. in [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (eds.) (**2000**). *Games in AI Research*. [Universiteit Maastricht](Maastricht_University "Maastricht University"), [pdf preprint](http://www.cs.ualberta.ca/%7Etony/RecentPapers/nec97w.pdf)
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Deep Search Extension](https://www.stmintz.com/ccc/index.php?id=14259) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 18, 1998
25. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Null move mate extension](https://www.stmintz.com/ccc/index.php?id=57953) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), June 25, 1999
26. <a id="cite-ref-26" href="#cite-note-26">↑</a> [mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=389013) by [Rick Bischoff](index.php?title=Rick_Bischoff&action=edit&redlink=1 "Rick Bischoff (page does not exist)"), [CCC](CCC "CCC"), September 25, 2004
27. <a id="cite-ref-27" href="#cite-note-27">↑</a> [Re: mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=390268) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 04, 2004 » [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions") and [WAC](Win_at_Chess "Win at Chess") booster
28. <a id="cite-ref-28" href="#cite-note-28">↑</a> [null move threat extension](http://www.talkchess.com/forum/viewtopic.php?t=24543) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), October 23, 2008
29. <a id="cite-ref-29" href="#cite-note-29">↑</a> [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003
30. <a id="cite-ref-30" href="#cite-note-30">↑</a> [Verified Null-Move Pruning, ICGA 25(3)](https://www.stmintz.com/ccc/index.php?id=266356) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), November 20, 2002
31. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Proving something is better](https://www.stmintz.com/ccc/index.php?id=271270) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), December 17, 2002
32. <a id="cite-ref-32" href="#cite-note-32">↑</a> courtesy of [Don Beal](Don_Beal "Don Beal") and [Carey Bloodworth](Carey_Bloodworth "Carey Bloodworth"), [Re: Antique chess programs](http://www.talkchess.com/forum/viewtopic.php?t=58603&start=13) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), December 16, 2015
33. <a id="cite-ref-33" href="#cite-note-33">↑</a> Selective Search Techniques in REBEL (introduction) from [Programmer Corner](Rebel#ProgrammerCorner "Rebel") by [Ed Schröder](Ed_Schroder "Ed Schroder")
34. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Nullmove vs classic selective search](http://www.talkchess.com/forum/viewtopic.php?t=44686) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 04, 2012

**[Up one level](Pruning "Pruning")**







 
