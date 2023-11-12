---
title: Topple
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Topple**



[ Toppled Klein Bottle <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Topple**, (ToppleChess)  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Vincent Tang](Vincent_Tang "Vincent Tang"), written in [C++](Cpp "Cpp"), first released in June 2018 under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards") by [Pradyumna Kannan](Pradu_Kannan "Pradu Kannan")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP") using [Threads](Thread "Thread") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [Four Buckets](Transposition_Table#Bucket "Transposition Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Selectivity](Selectivity "Selectivity")
	+ [Extensions](Extensions "Extensions")
		- [Check Extensions](Check_Extensions "Check Extensions")
		- [PV Extensions](PV_Extensions "PV Extensions")
		- [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
	+ [Pruning](Pruning "Pruning")/[Reductions](Reductions "Reductions")
		- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
		- [Futility Pruning](Futility_Pruning "Futility Pruning")
		- [Delta Pruning](Delta_Pruning "Delta Pruning")
		- [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
		- [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
		- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
		- [Static Exchange Evaluation Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Staged Move Generation](Move_Generation#Staged "Move Generation")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Mobility](Mobility "Mobility")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [King Safety](King_Safety "King Safety")


### Misc


* [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## Forum Posts


### 2018 ...


* [Topple](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67685) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), June 09, 2018
* [Topple v0.2.1 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67998) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), July 16, 2018
* [Automated tuning... finally... (Topple v0.3.0)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69532) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), January 08, 2019
* [Topple v0.3.4 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69734) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), January 26, 2019
* [Topple 0.3.5](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69818) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), February 03, 2019
* [Topple 0.5.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70394) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), April 02, 2019
* [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=451) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), December 28, 2019


### 2020 ...


* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=79) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), February 21, 2020


## External Links


### Chess Engine


* [GitHub - konsolas/ToppleChess: UCI chess engine](https://github.com/konsolas/ToppleChess)
* [Topple](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Topple&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [topple - Wiktionary](https://en.wiktionary.org/wiki/topple)
* [Topple (game) from Wikipedia](https://en.wikipedia.org/wiki/Topple)
* [Topple Tower from Wikipedia](https://en.wikipedia.org/wiki/Topple_Tower)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Klein bottle](https://en.wikipedia.org/wiki/Klein_bottle) parametrized all in one piece, toppled, Graphed using [Grapher](https://en.wikipedia.org/wiki/Grapher) by [AugPi](https://commons.wikimedia.org/wiki/User:AugPi), August 15, 2019, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Topple](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67685) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), June 09, 2018
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> based on *Techniques used* in [ToppleChess/README.md at master · konsolas/ToppleChess · GitHub](https://github.com/konsolas/ToppleChess/blob/master/README.md)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> using [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") in [Topple 0.5.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70394) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), April 02, 2019

**[Up one level](Engines "Engines")**







 
