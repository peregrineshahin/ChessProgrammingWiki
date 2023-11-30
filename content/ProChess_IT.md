---
title: ProChess IT
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* ProChess**


**ProChess**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), written in [Visual Basic](Basic#VB "Basic"), first released in November 2011, in October 2012 with source code <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
ProChess features a [0x88](0x88 "0x88") board representation, [negamax](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search") with [iterative deepening](Iterative_Deepening "Iterative Deepening"), [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [futility pruning](Futility_Pruning "Futility Pruning"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") and a [capture](Captures "Captures") and [promotion](Promotions "Promotions") only [quiescence search](Quiescence_Search "Quiescence Search"). [Move ordering](Move_Ordering "Move Ordering") considers [MVV-LVA](MVV-LVA "MVV-LVA"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") and [history heuristic](History_Heuristic "History Heuristic"). Only safe [checks](Check "Check") with positive SEE are [extended](Check_Extensions "Check Extensions") . 
A [tapered eval](Tapered_Eval "Tapered Eval") interpolates between [opening](Opening "Opening") and [endgame](Endgame "Endgame") [scores](Score "Score"), primarily based on [piece-square tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



## Selected Games


[CCT15](CCT15 "CCT15"), round 6, ProChess - [Tinker](Tinker "Tinker") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "CCT15"]
[Site "Variant-ICS, Amsterdam, NL"]
[Date "2013.02.24"]
[Round "6"]
[White "ProChess"]
[Black "Tinker"]
[Result "1-0"]

1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 Bb4 5.Nd5 Bc5 6.d3 O-O 7.Bg2 h6 8.Be3 d6 
9.Bxc5 dxc5 10.Nd2 Be6 11.Nxf6+ Qxf6 12.Nb3 e4 13.Bxe4 Qxb2 14.Qc1 Qf6 
15.Nxc5 Bf5 16.O-O b6 17.Bxf5 Qxf5 18.Nb3 Rfe8 19.c5 b5 20.e4 Qf6 21.Rd1 a5 
22.a4 Rab8 23.Qc2 Red8 24.axb5 Rxb5 25.Kg2 Ne5 26.f4 Ng4 27.Qe2 Rxb3 28.Qxg4 
Qd4 29.Ra2 Rxd3 30.Rxd3 Qxd3 31.Qe2 Qxe2+ 32.Rxe2 Rb8 33.e5 a4 34.Kf3 Ra8 
35.Ke4 a3 36.Ra2 Kf8 37.Kd5 Ke7 38.Kc6 Ra7 39.f5 g6 40.g4 Ra5 41.h3 g5
42.Kb7 Rxc5 43.Rxa3 Rxe5 44.Kxc7 Rc5+ 45.Kb6 1-0

```

## Namesake


* [Prochess](Prochess "Prochess") by [Tom Pronk](Tom_Pronk "Tom Pronk")


## See also


* [RamJet](RamJet "RamJet")


## Forum Posts


* [ProChess 101 C "prime" released](http://www.talkchess.com/forum/viewtopic.php?t=44422) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), July 14, 2012
* [ProChess 102 A "doctor" released](http://www.talkchess.com/forum/viewtopic.php?t=45745) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), October 26, 2012


## External Links


* [ProChess « G 6](https://www.g-sei.org/prochess/)
* [ProChess | SST - Società Scacchistica Torinese](http://www.scacchisticatorinese.it/nuovo_portale/argomento_det.php?codice_argomento=367)
* [ProChess](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=ProChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [ProChess 102 A "doctor" released](http://www.talkchess.com/forum/viewtopic.php?t=45745) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), October 26, 2012
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [ProChess102AD.zip | readme.txt](https://www.g-sei.org/prochess/prochess102ad/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [CCT15 Results | PGN download](https://cctchess.com/cct15-results/)

**[Up one Level](Engines "Engines")**







 
