---
title: Maxima2
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Maxima2**



[ Maxima <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Maxima2**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Erik van het Hof](Erik_van_het_Hof "Erik van het Hof") and [Hermen Reitsma](Hermen_Reitsma "Hermen Reitsma"), released under the [GPL license](Free_Software_Foundation#GPL "Free Software Foundation").
Maxima2 is written in [C++](Cpp "Cpp") as successor of [BugChess](BugChess_NL "BugChess NL") aka **QueenMaxima**. The code has been completely rewritten and modernized using new developments in computer chess from the last decade,
with [bitboards](Bitboards "Bitboards"), [LMR](Late_Move_Reductions "Late Move Reductions"), less [extensions](Extensions "Extensions"), more [pruning](Pruning "Pruning"), [tapered evaluation](Tapered_Eval "Tapered Eval"), and integrated self-matching test for [testing](Engine_Testing "Engine Testing") and [tuning](Automated_Tuning "Automated Tuning") [evaluation](Evaluation "Evaluation") values as most notable changes <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") ([Fail-Soft](Fail-Soft "Fail-Soft"))
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Safe Check Extensions](Check_Extensions "Check Extensions")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (Beta Pruning)
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Mobility](Mobility "Mobility")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
* [Outposts](Outposts "Outposts")
* [King Safety](King_Safety "King Safety")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Passed Pawns](Passed_Pawn "Passed Pawn")


## See also


* [BugChess NL](BugChess_NL "BugChess NL")
* [MAX](MAX_(Gillogly) "MAX (Gillogly)") by [James Gillogly](James_Gillogly "James Gillogly")
* [Max](Max "Max") by [Guy Burkill](index.php?title=Guy_Burkill&action=edit&redlink=1 "Guy Burkill (page does not exist)")


## Forum Posts


* [Two new programs if...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60547) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), June 21, 2016


## External Links


### Chess Engine


* [GitHub - GitHub - hof/qm2: maxima2 chess program](https://github.com/hof/qm2)
* [GitHub - hof/qm2-util: maxima2 utilities for online playing, tuning, web and mobile display](https://github.com/hof/qm2-util)


### Misc


* [Maxima from Wikipedia](https://en.wikipedia.org/wiki/Maxima)
* [Queen Máxima of the Netherlands from Wikipedia](https://en.wikipedia.org/wiki/Queen_M%C3%A1xima_of_the_Netherlands)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The graph of a 3D [paraboloid](https://en.wikipedia.org/wiki/Paraboloid) given by f(x,y) = -(x²+y²)+4, Shown is the [global maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) of the surface, at (0,0,4), Selfmade with [MuPad](https://en.wikipedia.org/wiki/MuPAD), [Sam Derbyshire](https://en.wikipedia.org/wiki/User:Sam_Derbyshire), February 21, 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [qm2/README.md at master · hof/qm2 · GitHub](https://github.com/hof/qm2/blob/master/README.md)

**[Up one Level](Engines "Engines")**







 
