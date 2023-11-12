---
title: WyldChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* WyldChess**


**WyldChess**,  

an [UCI](UCI "UCI") and [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Manik Charan](Manik_Charan "Manik Charan"), licensed under the [GNU General Public License v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C](C "C")/[C++](Cpp "Cpp"), first released in October 2016. 
Origin of ideas and implementations are documented inside the source code, e.g. [tapered eval](Tapered_Eval "Tapered Eval") [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") [score](Score "Score") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, or [SEE](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") from [Stockfish](Stockfish "Stockfish"). 
Since version 1.5, released in June 2017, WyldChess supports [Syzygy Bases](Syzygy_Bases "Syzygy Bases") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Dense Piece-Color Board-Definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Little-Endian Rank-File Mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards") by [Pradu Kannan](Pradu_Kannan "Pradu Kannan")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")


 [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Selectivity](Selectivity "Selectivity")


 [Futility Pruning](Futility_Pruning "Futility Pruning")
 [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
 [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
 [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
 [Check Extensions](Check_Extensions "Check Extensions")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Move Ordering](Move_Ordering "Move Ordering")


 [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
 [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
 [History Heuristic](History_Heuristic "History Heuristic") (1.5)
 [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")


 [Bishop Pair](Bishop_Pair "Bishop Pair")
 [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [King Safety](King_Safety "King Safety")


 [Attacking King Zone](King_Safety#Attacking "King Safety")
 [King Queen Tropism](King_Safety#KingTropism "King Safety")
* [Pawn Structure](Pawn_Structure "Pawn Structure")


 [Passed Pawn](Passed_Pawn "Passed Pawn")
 [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
 [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
* [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
* [Bishop and Knight Outposts](Outposts "Outposts")


### Misc


* [Syzygy Bases](Syzygy_Bases "Syzygy Bases") (1.5)


## See also


* [Teki](index.php?title=Teki&action=edit&redlink=1 "Teki (page does not exist)")


## Forum Posts


* [WyldChess new release now UCI](http://www.talkchess.com/forum/viewtopic.php?t=61700) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), October 13, 2016
* [Strange beaviour of WyldChess under WinBoard](http://www.talkchess.com/forum/viewtopic.php?t=62290) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), November 27, 2016
* [WyldChess 1.3 released](http://www.talkchess.com/forum/viewtopic.php?t=62823) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), January 14, 2017
* [WyldChess 1.4 released](http://www.talkchess.com/forum/viewtopic.php?t=63423) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), March 12, 2017
* [WyldChess 1.5 released](http://www.talkchess.com/forum/viewtopic.php?t=64174) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), June 04, 2017
* [WyldChess 1.51 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=64506) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), July 04, 2017


## External Links


* [GitHub - Mk-Chan/WyldChess: A UCI/Xboard compatible chess engine in C/C++](https://github.com/Mk-Chan/WyldChess)


 [GitHub - Mk-Chan/BBPerft: A fast, bitboard based chess perft result generator derived from WyldChess](https://github.com/Mk-Chan/BBPerft) » [Perft](Perft "Perft")
* [WyldChess](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=WyldChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/4](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [WyldChess/defs.h at master · Mk-Chan/WyldChess · GitHub](https://github.com/Mk-Chan/WyldChess/blob/master/src/defs.h)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [WyldChess 1.5 released](http://www.talkchess.com/forum/viewtopic.php?t=64174) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), June 04, 2017
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Evaluation and Search Features mostly based on [WyldChess/README.md at master · Mk-Chan/WyldChess · GitHub](https://github.com/Mk-Chan/WyldChess/blob/master/README.md)

**[Up one Level](Engines "Engines")**







 
