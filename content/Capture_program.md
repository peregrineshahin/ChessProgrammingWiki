---
title: Capture program
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Capture**

**Capture**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess program by [Sylvain Renard](Sylvain_Renard "Sylvain Renard"), competing the [15th World Microcomputer Chess Championship](WMCCC_1997 "WMCCC 1997") 1997 in Paris, the [Aegon Man-Machine Tournaments](Aegon_Tournaments "Aegon Tournaments") [1995](Aegon_1995 "Aegon 1995"), [1996](Aegon_1996 "Aegon 1996") and [1997](Aegon_1997 "Aegon 1997") <a id="cite-note-1" href="#cite-ref-1">[1]</a> and various [French Computer Chess Championships](French_Computer_Chess_Championship "French Computer Chess Championship") and [Massy Tournaments](French_Programmers_Tournament "French Programmers Tournament"), winning the title at the [FCCC 1999](FCCC_1999 "FCCC 1999") tied with [Chess Tiger](Chess_Tiger "Chess Tiger") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Description

given in 1997 <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++CAPTURE is a "classical" chess program. It uses [alpha-beta search](Alpha-Beta "Alpha-Beta") (with a [zero window](Null_Window "Null Window")), [check extensions](Check_Extensions "Check Extensions"), [null-move](Null_Move_Pruning "Null Move Pruning"), [history heuristic](History_Heuristic "History Heuristic") at the root of the tree. The program uses [hash tables](Transposition_Table "Transposition Table") (tested with 64 Mb of [RAM](Memory#RAM "Memory") but should work with more!). The [move generator](Move_Generation "Move Generation") does not use bit boards. The main chess knowledge of CAPTURE: [pawn structures](Pawn_Structure "Pawn Structure"), development and [mobility](Mobility "Mobility") of pieces, [piece placement](Piece-Square_Tables "Piece-Square Tables"), some [endgame](Endgame "Endgame") knowledge (essentially [pawn endgames](Pawn_Endgame "Pawn Endgame") and mating routines). The [value of pieces](Point_Value "Point Value") depends slightly on the number of pawns on the chessboard. The evaluation function is "made by hand" and modified according to positional tests. 

```

## Selected Games

[WMCCC 1997](WMCCC_1997 "WMCCC 1997"), round 2, [Chess Tiger](Chess_Tiger "Chess Tiger") - Capture <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "WMCCC 1997"]
[Site "Paris, France"]
[Date "1997.10.27"]
[Round "2"]
[White "Chess Tiger"]
[Black "Capture"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 Bxc3 7.bxc3 d6 8.Bg5 Qe7 9.Re1 h6 
10.Be3 Bd7 11.h3 a6 12.Ba4 Nd4 13.cxd4 Bxa4 14.Rb1 c5 15.dxc5 dxc5 16.Rb6 Rfb8 17.Qd2 Bb5 
18.c4 Nd7 19.Rxh6 gxh6 20.cxb5 axb5 21.Bxh6 Ra6 22.Rb1 Qe6 23.Qg5+ Qg6 24.Rxb5 Qxg5 25.Bxg5 
Rxa2 26.Be7 b6 27.Bd6 Re8 28.Bc7 Ra7 29.Bxb6 Rb7 30.Rxc5 Rxb6 31.Rd5 Re7 32.g4 Rb4 33.h4 f6 
34.h5 Rb1+ 35.Kg2 Rd1 36.Nh4 Nf8 37.Rd6 Nh7 38.Nf5 Re8 39.f4 Rb8 40.fxe5 fxe5 41.Kg3 Rb3 
42.Rd8+ Nf8 43.Kh4 Kf7 44.g5 Rbxd3 45.Nh6+ Ke7 46.Rxd3 Rxd3 47.g6 Rd1 48.Ng4 Rh1+ 49.Kg3 
Rg1+ 50.Kh4 Nd7 51.Nh6 Ke6 52.Nf5 Nc5 53.Ng3 Kf6 54.Kh3 Re1 55.Nf5 Rh1+ 56.Kg2 Rxh5 57.Ng3 
0-1 

```

## External Links

- [Capture's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=9)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Aegon Man-Machine Tournaments](http://old.csvn.nl/aegonhist.html) from the old [CSVN](CSVN "CSVN") Site
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess Tiger 12.0 wins the FCCC together with Capture](https://www.stmintz.com/ccc/index.php?id=72642) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), October 10, 1999
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Capture's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=9)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Paris 1997 - Chess - Round 2 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=5&round=2&id=3)

**[Up one Level](Engines "Engines")**

