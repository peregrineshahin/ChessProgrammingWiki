---
title: Darmenios
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Darmenios**

**Darmenios**,

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Dariusz Czechowski](Dariusz_Czechowski "Dariusz Czechowski"), written in [C++](Cpp "Cpp"), first released in January 2010.
Darmenios performs [bitboard-based](Bitboards "Bitboards") [legal move generation](Move_Generation#Legal "Move Generation"), [alpha-beta search](Alpha-Beta "Alpha-Beta") with [null-move pruning](Null_Move_Pruning "Null Move Pruning"), [quiescence search](Quiescence_Search "Quiescence Search"), [history based](History_Heuristic "History Heuristic") [move ordering](Move_Ordering "Move Ordering"), and uses a [transposition table](Transposition_Table "Transposition Table") with a special replacement algorithm.
In 2010, the rudimentary [evaluation](Evaluation "Evaluation") considered [mobility](Mobility "Mobility"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables") and [passed pawns](Passed_Pawn "Passed Pawn") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and apparently has improved since then.

## Tournament Play

Darmenios played the [WCCC 2010](WCCC_2010 "WCCC 2010") and [WCSC 2010](WCSC_2010 "WCSC 2010") in [Kanazawa](https://en.wikipedia.org/wiki/Kanazawa,_Ishikawa). At the [Polish Computer Chess Championship](Polish_Computer_Chess_Championship "Polish Computer Chess Championship") Darmenios demonstrated huge progress in two years after its debut at [PCCC 2009](PCCC_2009 "PCCC 2009") with 0/6, the [PCCC 2010](PCCC_2010 "PCCC 2010") already third with 3½/6, and winning the [PCCC 2011](PCCC_2011 "PCCC 2011") with 5/6.
At the [WCRCC 2011](WCRCC_2011 "WCRCC 2011"), the Fifth Annual ACCA World Computer Rapid Chess Championship, Darmenios became sixth with 5½/10.

## Selected Games

[WCCC 2010](WCCC_2010 "WCCC 2010"), round 2, [Hector for Chess](Hector_for_Chess "Hector for Chess") - Darmenios <a id="cite-note-2" href="#cite-ref-2">[2]</a>

```

[Event "WCCC 2010"]
[Site "Kanazawa, Japan"]
[Date "2010.09.25"]
[Round "2"]
[White "Hector for Chess"]
[Black "Darmenios"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Be7 5.O-O O-O 6.Re1 d6 7.c3 Na5 8.Bb5 a6 
9.Ba4 b5 10.Bc2 c5 11.Nbd2 Be6 12.d4 cxd4 13.cxd4 Rc8 14.Bd3 Qb6 15.d5 Bd7 
16.Nf1 Ng4 17.Qe2 Qb8 18.Ng3 Nb7 19.b4 Nf6 20.a4 a5 21.Bxb5 axb4 22.Bg5 Bg4 
23.Bxf6 Bxf6 24.Reb1 Rc3 25.Rxb4 Na5 26.Qb2 Qc7 27.Ne1 Bh4 28.Ne2 Rc5 29.f3 
Bc8 30.Qb1 f5 31.Nd3 Rc2 32.Rb2 Rxb2 33.Qxb2 fxe4 34.fxe4 Nc4 35.Qb4 Ne3 
36.Qd2 Qa7 37.Kh1 Nxg2 38.Ng1 Ne3 39.Rc1 Bg4 40.Rb1 Bh5 41.Qc1 Nd1 42.Kg2 
Qf7 43.Kh3 Bd8 44.Nf4 Qf6 45.Rb3 exf4 46.Qxd1 Bxd1 47.Nf3 Bxb3 0-1 

```

## Forum Posts

- [Darmenios 0.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=33634) by Carlos777, [CCC](CCC "CCC"), April 05, 2010
- [Problems with Darmenios and Magnum](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=36552) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 30, 2010
- [Darmenios 0.4](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=41122) by countrychess, [CCC](CCC "CCC"), November 17, 2011

## External Links

- [Darmenios' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=611)
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Darmenios' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=611)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Kanazawa 2010 - Chess - Round 2 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=209&round=2&id=2)

**[Up one Level](Engines "Engines")**

