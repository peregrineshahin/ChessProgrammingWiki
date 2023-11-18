---
title: Nullmover
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nullmover**


**Nullmover**,  

a private <a id="cite-note-1" href="#cite-ref-1">[1]</a>, 
[WinBoard](WinBoard "WinBoard") compliant chess engine written in [C](C "C")/[C++](Cpp "Cpp"). The development started in 2001 by primary author [Michel Langeveld](Michel_Langeveld "Michel Langeveld") and since 2003 supported by co-author [Jos Timmer](index.php?title=Jos_Timmer&action=edit&redlink=1 "Jos Timmer (page does not exist)"), 
who helped with implementing [tablebases](Endgame_Tablebases "Endgame Tablebases"), [attacktables](Attack_and_Defend_Maps "Attack and Defend Maps") and [pondering](Pondering "Pondering") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Nullmover played the [ICT 2003](ICT_2003 "ICT 2003") and [DOCCC 2003](DOCCC_2003 "DOCCC 2003") over the board, and four [CCT Tournaments](CCT_Tournaments "CCT Tournaments") from 2002 until 2005.



## Description


Nullmover performs [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") along with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Captures](Captures "Captures") are [ordered](Move_Ordering "Move Ordering") by [MVV-LVA](MVV-LVA "MVV-LVA"), [quiet moves](Quiet_Moves "Quiet Moves") by dedicated [piece-square tables](Piece-Square_Tables "Piece-Square Tables"). 
It has separate [evaluation](Evaluation "Evaluation") for [opening](Opening "Opening"), [middlegame](Middlegame "Middlegame"), and [endgame](Endgame "Endgame"), and [caches](Pawn_Hash_Table "Pawn Hash Table") [pawn structure](Pawn_Structure "Pawn Structure") informations.



## Forum Posts


* [Nullmover - Embracer (weird game)](https://www.stmintz.com/ccc/index.php?id=201147) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), December 09, 2001
* [Fine #70](https://www.stmintz.com/ccc/index.php?id=321449) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), October 15, 2003 » [Fine #70](Lasker-Reichhelm_Position "Lasker-Reichhelm Position")
* [Chess Tiger - Nullmover: Some notes](https://www.stmintz.com/ccc/index.php?id=323671) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), October 25, 2003 » [Chess Tiger](Chess_Tiger "Chess Tiger"), [DOCCC 2003](DOCCC_2003 "DOCCC 2003")
* [Position from Chess Tiger - Nullmover](https://www.stmintz.com/ccc/index.php?id=323782) by [Slater Wold](index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](CCC "CCC"), October 26, 2003
* [Rebel against Nullmover](https://www.stmintz.com/ccc/index.php?id=323799) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), October 26, 2003 » [Rebel](Rebel "Rebel"), [DOCCC 2003](DOCCC_2003 "DOCCC 2003")


## External Links


* [Nullmover chessprogram](https://mlngveld.home.xs4all.nl/nullmover/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Private Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:private_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Nullmover chessprogram](https://mlngveld.home.xs4all.nl/nullmover/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Photos](https://old.csvn.nl/mei2003toernooi.html) from the old [CSVN](CSVN "CSVN") site

**[Up one Level](Engines "Engines")**







 
