---
title: SierC5BCant
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sierżant**



[ Sierżant <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Sierżant**, (Sierzant)  

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Mariusz Rostek](Mariusz_Rostek "Mariusz Rostek"), written in [C++](Cpp "Cpp") and first released in November 2004. 
Sierżant was described in Mariusz' 2008 Diploma thesis <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
It is the successor of the weaker [Szeregowiec](Szeregowiec "Szeregowiec"), and predecessor of the stronger [Porucznik](Porucznik "Porucznik") - in dependence to the [Polish Armed Forces ranking](https://en.wikipedia.org/wiki/Polish_Armed_Forces_rank_insignia).



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Selected Games](#selected-games)
* [3 Description](#description)
	+ [3.1 Board Representation](#board-representation)
	+ [3.2 Search](#search)
	+ [3.3 Evaluation](#evaluation)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
	+ [7.1 Chess Engine](#chess-engine)
	+ [7.2 Misc](#misc)
* [8 References](#references)






As "house program" of the [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź"), Sierżant was active in four consecutive [Polish Computer Chess Championships](Polish_Computer_Chess_Championship "Polish Computer Chess Championship"), the [PCCC 2004](PCCC_2004 "PCCC 2004"), [PCCC 2005](PCCC_2005 "PCCC 2005"), [PCCC 2006](PCCC_2006 "PCCC 2006") and the international [IOPCCC 2007](IOPCCC_2007 "IOPCCC 2007").



## Selected Games


[PCCC 2006](PCCC_2006 "PCCC 2006"), round 3, Sierżant - [nanoSzachy](NanoSzachy "NanoSzachy") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "5th PCCC 2006"]
[Site "Lodz"]
[Date "2006.09.16"]
[Round "3"]
[White "Sierzant"]
[Black "nanoSzachy"]
[Result "1-0"]

1.c4 e6 2.Nc3 d5 3.d4 Nf6 4.cxd5 exd5 5.Bg5 Nbd7 6.e3 Be7 7.Qc2 c6 8.Bd3 O-O 
9.Nf3 Re8 10.h3 Nf8 11.Bf4 Ng6 12.Bh2 Ne4 13.Nxe4 dxe4 14.Bxe4 Qa5+ 15.Kf1 Be6 
16.Ne5 Rad8 17.b3 Bf6 18.Nxg6 hxg6 19.Rc1 Qa3 20.Rb1 Qa6+ 21.Kg1 Qa3 22.Bf4 Bd5 
23.Bd3 Rd7 24.e4 Be6 25.d5 cxd5 26.Bb5 dxe4 27.Bxd7 Bxd7 28.Rd1 Bf5 29.g4 Rc8 
30.Qe2 Be6 31.g5 Bc3 32.Qxe4 Qxa2 33.Qxb7 Qxb3 34.Qxb3 Bxb3 35.Rc1 Rc4 36.Kg2 
a5 37.Rb1 Bc2 38.Rb8+ Kh7 39.Rc1 Bd4 40.f3 f6 41.h4 a4 42.Re1 Bf5 43.Ree8 Rc2+ 
44.Kh1 Bc8 45.Rbxc8 Rxc8 46.Rxc8 Bf2 47.Rc2 Be1 48.Re2 Bc3 49.Bd6 Ba5 50.Kg2 
Bb6 51.Re7 Bd4 52.Re4 Bc3 53.Rxa4 Kg8 54.Rc4 Bb2 55.Rc2 Bd4 56.Rd2 Bc3 57.Rc2 
Bd4 58.Rc4 Bb2 59.f4 Kh8 60.Be7 Kg8 61.Rc7 fxg5 62.hxg5 Kh7 63.Bf6 Bxf6 64.gxf6 
Kg8 65.fxg7 Kh7 66.Kf3 g5 67.f5 Kg8 68.Kg4 Kh7 69.Kxg5 Kg8 70.f6 Kh7 71.Kf5 Kg8
72.Rc8+ Kh7 73.g8=Q+ Kh6 1-0

```

## Description


### [Board Representation](Board_Representation "Board Representation")


The board is represented by a [10x10 array](Mailbox "Mailbox"), [move generation](Move_Generation "Move Generation") is done in conjunction with [piece lists](Piece-Lists "Piece-Lists") and [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation"). 



### [Search](Search "Search")


Sierżant performs [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [null-move pruning](Null_Move_Pruning "Null Move Pruning") and [razoring](Razoring "Razoring") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") loop, 
and [extends consecutive checks](Check_Extensions "Check Extensions") up to five times inside one variation. Despite it has no [transposition table](Transposition_Table "Transposition Table"), additive 32-bit [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") are used to detect [repetitions](Repetitions "Repetitions"). 
After first playing the [principal variation](Principal_Variation "Principal Variation") from the previous iteration, [move ordering](Move_Ordering "Move Ordering") is improved by the [killer heuristic](Killer_Heuristic "Killer Heuristic") and [MVV-LVA](MVV-LVA "MVV-LVA") for captures. 
To compare the quality of move ordering, a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") ratio L1/L2 >= 1.0 (the smaller, the better) is determined as follows:




```

int alphabeta (ply, depth, alpha, beta) {
  for (a = 1; a <= NMoves; a++) {
     make ();
     value = -alphabeta( ... );
     unmake ();
     if (value >= beta) {
       L1 += a;
       L2 += 1;
       return beta;
     }
  }
}

```

### [Evaluation](Evaluation "Evaluation")


The [material balance](Material#Balance "Material") is [calculated incrementally](Incremental_Updates "Incremental Updates") and passed as parameter to the recursive alpha-beta routine. Positional considerations, notably [piece-square tables](Piece-Square_Tables "Piece-Square Tables") including [king safety](King_Safety "King Safety") versus [king centralization](King_Centralization "King Centralization") and [pawn structure](Pawn_Structure "Pawn Structure") related stuff, are dependent on the [game phase](Game_Phases "Game Phases"), pre-determined at the [root](Root "Root") before starting the search, that is [opening](Opening "Opening"), [middle](Middlegame "Middlegame") and [endgame](Endgame "Endgame"), separated by the total amount of material on the board.



## See also


* [Porucznik](Porucznik "Porucznik")
* [Szeregowiec](Szeregowiec "Szeregowiec")


## Publications


* [Mariusz Rostek](Mariusz_Rostek "Mariusz Rostek") (**2008**). *[Program grający w szachy](http://strony.toya.net.pl/~sierzant29/nowosci.html)*. (Chess playing programs) Engineering Thesis, [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź"), advisor [Maciej Szmit](Maciej_Szmit "Maciej Szmit")


## Forum Posts


* [New winboard engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=502&p=1879) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2004


## External Links


### Chess Engine


* [Porucznik program szachowy algorytmy szachowe programowanie gry w szachy](http://strony.toya.net.pl/~sierzant29/) (Polish)


 [Program szachowy Sierzant28 - download](http://strony.toya.net.pl/~sierzant29/download.html)
 [Program szachowy Sierżant - Heurystyki](http://strony.toya.net.pl/~sierzant29/algorytmy.html)
* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)


### Misc


* [Sierżant – Wikipedia.pl](https://pl.wikipedia.org/wiki/Sier%C5%BCant) (Polish)


 [Sergeant - Wikipedia](https://en.wikipedia.org/wiki/Sergeant)
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Badge](https://en.wikipedia.org/wiki/Badge) of rank of Sierżant (Sergeant) of the [Polish Army](https://en.wikipedia.org/wiki/Polish_Land_Forces), [Polish Armed Forces rank insignia - Wikipedia](https://en.wikipedia.org/wiki/Polish_Armed_Forces_rank_insignia), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Mariusz Rostek](Mariusz_Rostek "Mariusz Rostek") (**2008**). *[Program grający w szachy](http://strony.toya.net.pl/~sierzant29/nowosci.html)*. (Chess playing programs) Engineering Thesis, [Technical University of Łódź](Technical_University_of_%C5%81%C3%B3d%C5%BA "Technical University of Łódź"), advisor [Maciej Szmit](Maciej_Szmit "Maciej Szmit")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Mistrzostwa Polski Programów Szachowych - PGN](http://mpps.maciej.szmit.info/mpps-5/)

**[Up one Level](Engines "Engines")**







 
