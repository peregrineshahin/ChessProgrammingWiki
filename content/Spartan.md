---
title: Spartan
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Spartan**



[ SPARTAN-101 Diagram <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Spartan**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Christian Daley](Christian_Daley "Christian Daley"), 
written in [C](C "C") and distributed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), first released in April 2016
as successor of [JFresh](JFresh "JFresh") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
As a pure [bitboard](Bitboards "Bitboards") engine, Spartan applies [Matt Taylor's](Matt_Taylor "Matt Taylor") [folding trick](BitScan#MattTaylorsFoldingtrick "BitScan") to [scan bits](BitScan "BitScan") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and [Brian Kernighan's way](Population_Count#BrianKernighansway "Population Count") to [count bits](Population_Count "Population Count") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 
In calculating [king passer tropism](King_Pawn_Tropism "King Pawn Tropism") in [evaluation](Evaluation "Evaluation"), 
Spartan uses the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between king and passer squares with [double](Double "Double") arithmetic due to [C standard library](https://en.wikipedia.org/wiki/C_standard_library) [square root](https://en.wikipedia.org/wiki/Square_root) (double sqrt(double)) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
<a id="cite-note-6" href="#cite-ref-6">[6]</a> of the [sum of squares](https://en.wikipedia.org/wiki/Sum_of_squares) of [rank difference](Ranks#RankDistance "Ranks") and [file difference](Files#FileDistance "Files"), which is quite expensive. Recommended is [looking up](Distance#Lookup "Distance") the [Chebyshev distance](Distance "Distance") or [Manhattan distance](Manhattan-Distance "Manhattan-Distance") for that purpose.



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc-2)
* [5 References](#references)






<a id="cite-note-7" href="#cite-ref-7">[7]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Razoring](Razoring "Razoring")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [ProbCut](ProbCut "ProbCut")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
		- [Delta Pruning](Delta_Pruning "Delta Pruning")
		- [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Connectivity](Connectivity "Connectivity")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
	+ [King Passer Tropism](King_Pawn_Tropism "King Pawn Tropism")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")


### Misc


* [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")
* [CCR One Hour Test](CCR_One_Hour_Test "CCR One Hour Test")


## See also


* [JFresh](JFresh "JFresh")
* [Spartan Chess](index.php?title=Spartan_Chess&action=edit&redlink=1 "Spartan Chess (page does not exist)") <a id="cite-note-8" href="#cite-ref-8">[8]</a>


## Forum Posts


* [New UCI engine: Spartan](http://www.open-chess.org/viewtopic.php?f=7&t=2973) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 23, 2016
* [New UCI engine Spartan released (a while ago)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60139) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 11, 2016


## External Links


### Chess Engine


* [GitHub - christiandaley/Spartan: UCI chess engine](https://github.com/christiandaley/Spartan)
* [Spartan 1.0](https://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Spartan%201.0#Spartan_1_0) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [spartan - Wiktionary](https://en.wiktionary.org/wiki/spartan)
* [Spartan - Wiktionary](https://en.wiktionary.org/wiki/Spartan)
* [Spartan Chess - Chess Variant Page](https://www.chessvariants.com/rules/spartan-chess)
* [Spartan Race from Wikipedia](https://en.wikipedia.org/wiki/Spartan_Race)
* [Sparta from Wikipedia](https://en.wikipedia.org/wiki/Sparta)
* [Sparta (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Sparta_(disambiguation))
* [Broken Brass Ensemble](Category:Broken_Brass_Ensemble "Category:Broken Brass Ensemble") - Spartan, [North Sea Jazz](https://en.wikipedia.org/wiki/North_Sea_Jazz_Festival) 2019, [NPO Radio 2 Soul & Jazz](https://en.wikipedia.org/wiki/NPO_Radio_2_Soul_%26_Jazz), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [SPARTAN-101](https://de.wikipedia.org/wiki/SPARTAN#SPARTAN_101) (Shuttle Pointed Autonomous Research Tool for Astronomy) carrier module of [STS-51-G](https://en.wikipedia.org/wiki/STS-51-G), the 18th flight of [NASA's](https://en.wikipedia.org/wiki/NASA) [Space Shuttle](https://en.wikipedia.org/wiki/Space_Shuttle) [program](https://en.wikipedia.org/wiki/Space_Shuttle_program), and the fifth flight of [Space Shuttle Discovery](https://en.wikipedia.org/wiki/Space_Shuttle_Discovery), June 17-24, 1985, [NASA](https://en.wikipedia.org/wiki/NASA) image, [SPARTAN – Wikipedia.de](https://de.wikipedia.org/wiki/SPARTAN) (German), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New UCI engine: Spartan](http://www.open-chess.org/viewtopic.php?f=7&t=2973) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 23, 2016
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Spartan/bitscan.h at master · christiandaley/Spartan · GitHub](https://github.com/christiandaley/Spartan/blob/master/src/bitscan.h)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Spartan/bitscan.c at master · christiandaley/Spartan · GitHub](https://github.com/christiandaley/Spartan/blob/master/src/bitscan.c)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [partan/eval.h at master · christiandaley/Spartan · GitHub](https://github.com/christiandaley/Spartan/blob/master/src/eval.h), #define DIST(sq1, sq2) ((int)sqrt(((...
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [C sqrt() - C Standard Library](https://www.programiz.com/c-programming/library-function/math.h/sqrt)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Spartan/Readme.md at master · christiandaley/Spartan · GitHub](https://github.com/christiandaley/Spartan/blob/master/Readme.md)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Spartan Chess - Chess Variant Page](https://www.chessvariants.com/rules/spartan-chess)

**[Up one Level](Engines "Engines")**







 
