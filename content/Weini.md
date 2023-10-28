---
title: Weini
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Weini**


**Weini**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon").
The project started in December 2016, and became a kind of interactive forum development when its author asked for advice one year later <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Many features were implemented and [tuned](Automated_Tuning "Automated Tuning") over the time, many techniqes were tried, possibly starting suffering maintainability, and desire for a re-write <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Weini is an acronym for **W**is**E**ness **I**s **N**ot **I**nside <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Automated Tuning](#automated-tuning)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Mailbox](Mailbox "Mailbox")
* [Bitboards](Bitboards "Bitboards")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Extensions](Extensions "Extensions")
		- [Check Extensions](Check_Extensions "Check Extensions")
		- [Single Reply Extensions](One_Reply_Extensions "One Reply Extensions")
		- [Singular Extensions](Singular_Extensions "Singular Extensions")
		- [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
		- [PV Extensions](PV_Extensions "PV Extensions")
		- [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
		- [Promotions](Promotions "Promotions")
		- [Late Endgame Transitions](Endgame "Endgame")
	+ [Reductions](Reductions "Reductions")
		- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
		- [Razoring](Razoring "Razoring")
	+ [Pruning](Pruning "Pruning")
		- [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
		- [ProbCut](ProbCut "ProbCut")
		- [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
		- [Futility Pruning](Futility_Pruning "Futility Pruning")
		- [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
		- [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Late Move Pruning)
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
		- [Delta Pruning](Delta_Pruning "Delta Pruning")
		- [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [PV-Move](PV-Move "PV-Move")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
	+ [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
	+ [Last Moved Piece Capture Bonus](Move_Ordering#Captures "Move Ordering")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Check Priority](Check "Check")
	+ [En passant Priority](En_passant "En passant")


### [Evaluation](Evaluation "Evaluation")


* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Tapered Eval](Tapered_Eval "Tapered Eval") ([Float](Float "Float"))
* [Material](Material "Material")
	+ [Bishop Pair](Bishop_Pair "Bishop Pair")
	+ [Trade Down Bonus](Material#Trade "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Development](Development "Development")
* [Center Control](Center_Control "Center Control")
* [Mobility](Mobility "Mobility")
	+ [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Bad Bishop](Bad_Bishop "Bad Bishop")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
		- [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
		- [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
		- [Outside Passed Pawn](Outside_Passed_Pawn "Outside Passed Pawn")
		- [Protected Passed Pawn](Protected_Passed_Pawn "Protected Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Pawn Shield](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")
	+ [King Piece Tropism](King_Safety#KingTropism "King Safety")
	+ [Castling](Castling "Castling")


### [Automated Tuning](Automated_Tuning "Automated Tuning")


* [CLOP](CLOP "CLOP")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## See also


* [Minic](Minic "Minic")


## Forum Posts


* [Looking for advices](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65936) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 08, 2017


 [Re: Looking for advices](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65936&start=7) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), March 25, 2018
* [Horizon effect and extensions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67823) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 25, 2018 » [Horizon Effect](Horizon_Effect "Horizon Effect"), [Extensions](Extensions "Extensions")
* [Weini questions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68161) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), August 08, 2018
* [Weini 0.0.24 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68700) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 20, 2018


## External Links


* [GitHub - tryingsomestuff/Weini](https://github.com/tryingsomestuff/Weini)
* [Weini](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Weini&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Looking for advices](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65936) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 08, 2017
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [A complete 2000 lines of code engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68701) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 20, 2018
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Weini questions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68161&start=3) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 08, 2018
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> based on [Weini/README.md at master · tryingsomestuff/Weini · GitHub](https://github.com/tryingsomestuff/Weini/blob/master/README.md) and sources of Weini-0.0.24

**[Up one level](Engines "Engines")**







 
