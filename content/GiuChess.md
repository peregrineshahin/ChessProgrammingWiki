---
title: GiuChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GiuChess**

**GiuChess**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Giuliano Ippoliti](Giuliano_Ippoliti "Giuliano Ippoliti"),
written in [C](C "C"), and released under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation").
GiuChess played the [CIPS 2007](CIPS_2007 "CIPS 2007"), [IGT 2013](IGT_2013 "IGT 2013") and [IGT 2014](IGT_2014 "IGT 2014"). While it is a very original and experimental engine, GiuChess is not designed or implemented to become competitive in terms of playing strength, but fun to play with some winning chances even for casual human players.

## Description

GiuChess <a id="cite-note-1" href="#cite-ref-1">[1]</a>
proofs [bitboards](Bitboards "Bitboards") ad absurdum, and [generate moves](Move_Generation "Move Generation") in a [mailbox](Mailbox "Mailbox") manner - per [piece](Pieces "Pieces") with loops over its [directions](Direction "Direction"), but [shifts](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), [intersections](General_Setwise_Operations#Intersection "General Setwise Operations") and conditions for [sliding pieces](Sliding_Pieces "Sliding Pieces"),
further checking moves are [legal](Legal_Move "Legal Move") at generation time. GiuChess applies [alpha-beta](Alpha-Beta "Alpha-Beta") with [floating point](Float "Float") [scores](Score "Score") and [bounds](Bound "Bound") with a predefined [depth](Depth "Depth") of 5, or in case of low time, 4 or 3 only.
It has no [iterative deepening](Iterative_Deepening "Iterative Deepening"), nor [transposition table](Transposition_Table "Transposition Table") and [quiescence search](Quiescence_Search "Quiescence Search"). The [evaluation](Evaluation "Evaluation") considers [material balance](Material#Balance "Material"), some piece bonuses for occupation near the [center](Center "Center"), plus a [random](Pseudorandom_Number_Generator "Pseudorandom Number Generator") score of up to 1/5 pawn value.
Instead of using [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), GiuChess uses bitboard intersections with three disjoined board ring areas, to apply a center bonus.

## Selected Games

[I.G.T. 2013](IGT_2013 "IGT 2013"), GiuChess - [ProChess](ProChess_IT "ProChess IT") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

```

[Event "I.G.T. 2013"]
[Site "Omegna (VB)"]
[Date "2013.11.09"]
[Round "-"]
[White "GiuChess 1.0"]
[Black "ProChess 103 hypercube"]
[Result "0-1"]

1.e4 g6 2.Qg4 d5 3.Qf4 dxe4 4.Bc4 Nf6 5.Qe5 Nc6 6.Bb5 Bd7 7.Bxc6 Bxc6 8.f3 e6
9.Qc3 a5 10.a3 Bd6 11.fxe4 Bxe4 12.Nf3 Ra6 13.Qd4 Bxf3 14.Qa4+ Bc6 15.Qc4 Bxg2
16.Rg1 Be4 17.Qb5+ Nd7 18.Rg4 f5 19.Rxe4 fxe4 20.Qe2 Qg5 21.b4 Rf8 22.Kd1 Qg1+ 
23.Qe1 Qg4+ 24.Qe2 Rf1# 0-1

```

## Forum Posts

- [GIUChess 1.0 update](http://www.talkchess.com/forum/viewtopic.php?t=48601) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 09, 2013

## External Links

- [GitHub - giuliano-ippoliti/GiuChess: Open Source Xboard/Winboard-compatible chess engine written in C language](https://github.com/giuliano-ippoliti/GiuChess)
- [GiuChess Homepage - by JSorel](http://giuchess.sourceforge.net/)

[GiuChess Xboard-compatible chess engine | Free Games software downloads at SourceForge.net](https://sourceforge.net/projects/giuchess/)

- [Giuchess « G 6](http://www.g-sei.org/giuchess/)
- [GIUChess 1.0 beta2](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=GIUChess%201.0%20beta2) in [CCRL Blitz](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Description based on GiuChess-1.0beta2, [GiuChess Xboard-compatible chess engine | Free Games software downloads at SourceForge.net](http://sourceforge.net/projects/giuchess/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [13′ Campionato italiano « G 6](http://www.g-sei.org/13-campionato-italiano/)

**[Up one Level](Engines "Engines")**

