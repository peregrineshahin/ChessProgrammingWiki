---
title: MinkoChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MinkoChess**


**MinkoChess**, (formerly called **Umko**)  

an [open source chess engine](Category:Open_Source "Category:Open Source") licensed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C++](Cpp "Cpp") by [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"). MinkoChess is [UCI](UCI "UCI") compatible and can be compiled for [Linux](Linux "Linux"), [Android](Android "Android"), [Windows](Windows "Windows"), and [Mac OS X](Mac_OS "Mac OS") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 



### [Board Representation](Board_Representation "Board Representation")


* [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Parallel Search](Parallel_Search "Parallel Search"), [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") using [Threads](Thread "Thread")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Selectivity](Selectivity "Selectivity")
	+ [Fractional Extensions](Extensions#FractionalExtensions "Extensions") considering [Node Type](Node_Types "Node Types")
		- [Piece Capture Extensions](Capture_Extensions "Capture Extensions") in [Endgame](Endgame "Endgame") and [PV-Node](Node_Types#pv-node "Node Types")
		- [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0
		- [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
		- [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
		- [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
	+ [Pruning](Pruning "Pruning")
		- [Futility Pruning](Futility_Pruning "Futility Pruning")
		- [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
		- [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
		- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
			* [Dynamic Depth Reduction](Depth_Reduction_R "Depth Reduction R") based on [depth](Depth "Depth") and [value](Score "Score")
			* [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
			* [Verification search](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") at high depths
		- [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Reductions](Reductions "Reductions")
		- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
		- [Razoring](Razoring "Razoring")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Score Grain](Score#Grain "Score"): [Centipawns](Centipawns "Centipawns")
* [Material](Material "Material")
	+ [Point Values](Point_Value "Point Value")
		- [Midgame](Middlegame "Middlegame"): 80, 370, 372, 570, 1120
		- [Endgame](Endgame "Endgame"): 104, 362, 364, 580, 1160
	+ [Bishop Pair](Bishop_Pair "Bishop Pair")
	+ [Material Imbalance](Material_Tables "Material Tables")
	+ [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Space](Space "Space")
* [Mobility](Mobility "Mobility")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
	+ [Rooks/Queen on 7th Rank](Rook_on_Seventh "Rook on Seventh")
* [Outposts](Outposts "Outposts")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Pawn Chain](Pawn_Chain "Pawn Chain")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
		- [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")
	+ [Square Control](King_Safety#SquareControl "King Safety")
	+ [Rooks on (Semi) Open Files near King File](Rook_on_Open_File "Rook on Open File")


### Misc


* [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book")
* [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")


## See also


* [BBChess](BBChess_(SI) "BBChess (SI)")


## Publications


* [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest") (**2011**). *Chess Program Umko*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/index-eng.html), Vol. 78, No. 3, English Edition, [pdf](https://pdfs.semanticscholar.org/c1b0/c2b14e7ed8c72a1d5e55f1a3f022c2f3ee61.pdf)


## Forum Posts


* [Umko 0.7](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50830) by [Fonzy Bluemers](Fonzy_Bluemers "Fonzy Bluemers"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2010
* [Umko discussion thread](http://talkchess.com/forum3/viewtopic.php?f=10&t=33025) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), March 03, 2010 (Engine Origins requires registration)
* [ELITE B 4CPU](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=24836) by [Graham Banks](Graham_Banks "Graham Banks"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 02, 2012 <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [MinkoChess v1.3 = 2900 Elo...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=43626) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), May 09, 2012
* [pruning statistics](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=51075) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 27, 2014 » [Pruning](Pruning "Pruning"), [Search Statistics](Search_Statistics "Search Statistics")


## External Links


* [Chess program MinkoChess - Computer Architecture and Languages Laboratory](https://labraj.feri.um.si/en/Chess_program_MinkoChess)
* [MinkoChess](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=MinkoChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess program MinkoChess- Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/Chess_program_MinkoChess), [University of Maribor](University_of_Maribor "University of Maribor")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> Copyright header in search.cpp, pos\_eval.cpp, movegen.cpp
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> "Umko has been renamed to MinkoChess due to copyright issues" by [Graham Banks](Graham_Banks "Graham Banks"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), May 09, 2012

**[Up one Level](Engines "Engines")**







 
