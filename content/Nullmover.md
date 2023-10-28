---
title: Nullmover
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nullmover**


**Nullmover**,  

a private <a id="cite-note-1" href="#cite-ref-1">[1]</a>, 
[WinBoard](WinBoard "WinBoard") compliant chess engine written in [C](C "C")/[C++](Cpp "Cpp"). The development started in 2001 by primary author [Michel Langeveld](Michel_Langeveld "Michel Langeveld") and since 2003 supported by co-author [Jos Timmer](index.php?title=Jos_Timmer&action=edit&redlink=1 "Jos Timmer (page does not exist)"), 
who helped with implementing [tablebases](Endgame_Tablebases "Endgame Tablebases"), [attacktables](Attack_and_Defend_Maps "Attack and Defend Maps") and [pondering](Pondering "Pondering") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Nullmover played the [ICT 2003](ICT_2003 "ICT 2003") and [DOCCC 2003](DOCCC_2003 "DOCCC 2003") over the board, and four [CCT Tournaments](CCT_Tournaments "CCT Tournaments") from 2002 until 2005.



### Contents


* [1 Photos & Games](#photos-.26-games)
* [2 Description](#description)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






 [](https://old.csvn.nl/mei2003toernooi.html) 
[ICT 2003](ICT_2003 "ICT 2003"), [Praetorian](Praetorian "Praetorian") - Nullmover by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [Leo Dijksman](Leo_Dijksman "Leo Dijksman") and [Richard Pijl](Richard_Pijl "Richard Pijl") kibitzing <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "ICT 2003"]
[Site "Leiden NED"]
[Date "2003.05.16"]
[Round "03"]
[White "Praetorian"]
[Black "Nullmover"]
[Result "0-1"]

1.Nf3 Nf6 2.c4 e6 3.d4 b6 4.g3 Bb7 5.Bg2 Be7 6.O-O O-O 7.b3 d5 8.Ne5 c5 9.dxc5 Bxc5 10.cxd5 Bxd5 
11.Bb2 Bxg2 12.Kxg2 Qc7 13.Nf3 Nbd7 14.Qd3 e5 15.Nc3 Rfe8 16.e4 Bb4 17.Nd5 Nxd5 18.Rfc1 Bc5 19.Qxd5 
Nf6 20.Qc4 Qb7 21.Nxe5 Ng4 22.b4 Nxe5 23.Bxe5 Bxf2 24.Bxg7 Be3 25.Bb2 Bxc1 26.Qxc1 Qxe4+ 27.Kg1 Rac8 
28.Qg5+ Qg6 29.Qb5 Qg4 30.Bf6 Re2 31.Rf1 Rcc2 32.Qd5 Qxb4 33.Qa8+ Qf8 34.Qxf8+ Kxf8 35.Rf3 Rg2+ 36.Kf1 
Rxh2 37.Kg1 Rcg2+ 38.Kf1 Rxa2 39.Kg1 Rhg2+ 40.Kf1 Rgc2 41.Bc3 a5 42.Be1 a4 43.Rf2 Rxf2+ 44.Bxf2 Rxf2+ 
45.Kxf2 a3 46.Kg2 a2 47.Kf3 a1=Q 48.Ke3 Qg7 49.Kf4 Qc3 50.g4 Qd4+ 51.Kf3 Qxg4+ 52.Kxg4 Ke7 53.Kf3 Kd6 
54.Ke4 h5 55.Kf4 h4 56.Kg4 b5 57.Kh3 Ke5 58.Kh2 b4 59.Kh3 b3 60.Kg2 b2 61.Kf1 b1=Q+ 62.Ke2 Ke4 63.Kf2 
Qc2+ 64.Kf1 Kf3 65.Kg1 Qg2# 0-1

```

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


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Private Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:private_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Nullmover chessprogram](https://mlngveld.home.xs4all.nl/nullmover/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Photos](https://old.csvn.nl/mei2003toernooi.html) from the old [CSVN](CSVN "CSVN") site

**[Up one Level](Engines "Engines")**







 
