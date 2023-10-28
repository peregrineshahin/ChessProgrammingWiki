---
title: Robocide
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Robocide**



 [](https://www.jmrw.com/) [Jacek Pałucha](Category:Jacek_Pa%C5%82ucha "Category:Jacek Pałucha") - Checkmate for a robot <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**Robocide**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Daniel White](Daniel_White "Daniel White"), written in [C](C "C") from scratch, 
and distributed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Robocide uses [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") [Magic Bitboards](Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). The ability to compile a 'tuning' version allows to adjust many of the [search](Search "Search") and [evaluation](Evaluation "Evaluation") parameters via UCI options <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



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






<a id="cite-note-5" href="#cite-ref-5">[5]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [BitScan Forward by De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") or [Trailing Zero Count intrinsic](BMI1#TZCNT "BMI1")
* [SWAR-Popcount](Population_Count#SWARPopcount "Population Count") or [64-bit popcount instruction](X86-64#gpinstructions "X86-64")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [SEE Pruning](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Score Grain](Score#Grain "Score") in [Millipawns](Millipawns "Millipawns")
* [Material](Material "Material")
* [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)")
* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
	+ [Bishop Mobility](Mobility "Mobility")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Rook on Open File](Rook_on_Open_File "Rook on Open File")
	+ [Rook on 7th Rank](Rook_on_Seventh "Rook on Seventh")
* [King Safety](King_Safety "King Safety")
	+ [Pawn Shield](King_Safety#PawnShield "King Safety")
	+ [Castling Ability](Castling "Castling")
* [Tempo Bonus](Tempo "Tempo")


### Misc


* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [KPK](KPK "KPK") [Bitbase](Endgame_Bitbases "Endgame Bitbases")
* [Perft](Perft "Perft")
* [Pondering](Pondering "Pondering")


## See also


* [iota](Iota "Iota")
* [RobboLito](RobboLito "RobboLito")
* [Robots](Robots "Robots")


## Forum Posts


* [CCWiki - two new engines etc.](http://www.talkchess.com/forum/viewtopic.php?t=51120) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 31, 2014


 [Re: CCWiki - two new engines etc.](http://www.talkchess.com/forum/viewtopic.php?t=51120&start=1) by [Daniel White](Daniel_White "Daniel White"), [CCC](CCC "CCC"), January 31, 2014
* [Mac OS X for Robocide?](http://www.talkchess.com/forum/viewtopic.php?t=51293) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 15, 2014
* [Robocide newer compilation request](http://www.talkchess.com/forum/viewtopic.php?t=60048) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 04, 2016


## External Links


### Chess Engine


* [GitHub - DanielWhite94/robocide](https://github.com/DanielWhite94/robocide)
* [Robocide](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Robocide&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Robo from Wikipedia](https://en.wikipedia.org/wiki/Robo)
* [robo- - Wiktionary](https://en.wiktionary.org/wiki/robo-)
* [-cide - Wiktionary](https://en.wiktionary.org/wiki/-cide)
* [Jonas Hellborg](Category:Jonas_Hellborg "Category:Jonas Hellborg") with [Glen Velez](https://en.wikipedia.org/wiki/Glen_Velez) - Regicide, [Ars Moriende](https://en.wikipedia.org/wiki/Ars_Moriende) (1994), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Tableaux ayant pour sujet les échecs](https://www.jmrw.com/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Шахматы в искусстве (48 часть): valsur — LiveJournal](https://valsur.livejournal.com/222212.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GitHub - DanielWhite94/robocide - GitHub - DanielWhite94/robocide: Robocide is a free, open-source UCI chess engine written in C from scratch](https://github.com/DanielWhite94/robocide)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [robocide/Readme.md at master · DanielWhite94/robocide · GitHub](https://github.com/DanielWhite94/robocide/blob/master/Readme.md)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [robocide/Readme.md at master · DanielWhite94/robocide · GitHub](https://github.com/DanielWhite94/robocide/blob/master/Readme.md)

**[Up one Level](Engines "Engines")**







 
