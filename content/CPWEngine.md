---
title: CPWEngine
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CPW-Engine**

The **CPW-Engine** (the **C**hess**P**rogramming **W**iki Engine) was developed by [Pawel Koziol](Pawel_Koziol "Pawel Koziol") and [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), who tried to put some of the theory presented on this pages into practice. The CPW is a fully functional chess engine intended as guidance to new programmers and exemplify some ideas. If You have any ideas how to simplify it, feel free to use "discussion" option. See also [CPW history](CPW_history "CPW history") on how the engine has evolved. A revised 2014 version 1.1 was provided Pawel Koziol <a id="cite-note-1" href="#cite-ref-1">[1]</a>, full code is further available at [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## The aims for the engine

- Readability
- Annotation
- [Playing strength](Playing_Strength "Playing Strength") is less important
- Modularization

## Playing strength

Version 1.0 of the CPW-Engine (CPW 1.00 beta 1) scored 5.5 out of 11 in [ChessWar](ChessWar "ChessWar") XIII F, earning there a rating of 1828. For the sake of comparison the same number of points has been gained by [Gerbil](Gerbil "Gerbil") (1894) and [Faile](Faile "Faile") (1900). Crosstables and games can be found at the [ChessWar](ChessWar "ChessWar") site.

Version 1.1 is probably about 2200 Elo on [CCRL](CCRL "CCRL") scale, but this needs to be tested.

The following game represents the current strength of the engine:

```

[Event "Test game"]
[Date "2008.08.19"]
[Round "7"]
[White "Tscp181"]
[Black "CPW 1.0"]
[Result "0-1"]
[TimeControl "300"]
[Termination "adjudication"]
[PlyCount "67"]

1.d4 Nf6 2.Nf3 e6 3.c4 c5 4.d5 exd5 5.cxd5 d6 6.Nc3 g6 7.e4 Bg7 8.Bb5+ Bd7 9.Qd3 O-O 
10.Bf4 Nxe4 11.Nxe4 Qa5+ 12.Qd2 Qxb5 13.O-O-O Qa6 14.Bxd6 Re8 15.Qc2 Bf5 16.Nfg5 Bh6 
17.Nf6+ Kh8 18.Qxf5 gxf5 19.Nxe8 Bxg5+ 20.Kb1 Nd7 21.Be5+ Nxe5 22.Nc7 Qf6 23.Rhe1 Rc8 
24.Nb5 Nc4 25.Re2 Qa6 26.Nc3 Bf6 27.Rde1 Na3+ 28.Ka1 Qc4 29.d6 Bxc3 30.d7 Rd8 31.Re8+ 
Kg7 32.R8e4 fxe4 33.Rc1 Bxb2+ 34.Kxb2
{0-1 Arena Adjudication} 0-1

```

This is it: lousy positional play and some luck aided by king tropism evaluation. The engine scores about 90% against [TSCP](TSCP "TSCP").

## Parts

- [CPW-Engine_stdafx_h](CPW-Engine_stdafx_h "CPW-Engine stdafx h") (constants and most of function prototypes)
- [CPW-Engine_book](CPW-Engine_book "CPW-Engine book")
- [CPW-Engine_chronos](CPW-Engine_chronos "CPW-Engine chronos") (timing functions)
- [CPW-Engine_console_ui](CPW-Engine_console_ui "CPW-Engine console ui")
- [CPW-Engine_main](CPW-Engine_main "CPW-Engine main")
- [CPW-Engine_com](CPW-Engine_com "CPW-Engine com")
- [CPW-Engine_eval_init](CPW-Engine_eval_init "CPW-Engine eval init")
- [CPW-Engine_quiescence](CPW-Engine_quiescence "CPW-Engine quiescence")
- [CPW-Engine_recognize](CPW-Engine_recognize "CPW-Engine recognize")
- [CPW-Engine_root](CPW-Engine_root "CPW-Engine root") (obsolete)
- [CPW-Engine_search](CPW-Engine_search "CPW-Engine search")
- [CPW-Engine_transposition](CPW-Engine_transposition "CPW-Engine transposition")
- [CPW-Engine_0x88_math](CPW-Engine_0x88_math "CPW-Engine 0x88 math")
- [CPW-Engine_board(0x88)](</CPW-Engine_board(0x88)> "CPW-Engine board(0x88)")
- [CPW-Engine_movegen(0x88)](</CPW-Engine_movegen(0x88)> "CPW-Engine movegen(0x88)")
- [CPW-Engine_move(0x88)](</CPW-Engine_move(0x88)> "CPW-Engine move(0x88)")
- [CPW-Engine_algebraic](CPW-Engine_algebraic "CPW-Engine algebraic")
- [CPW-Engine_eval](CPW-Engine_eval "CPW-Engine eval")
- [CPW-Engine_attacks](CPW-Engine_attacks "CPW-Engine attacks")
- [CPW-Engine_utils](CPW-Engine_utils "CPW-Engine utils")
- [CPW_King](CPW_King "CPW King")

## Features

- [0x88](0x88 "0x88") board
- [Search](Search "Search")
  - [Alpha-Beta](Alpha-Beta "Alpha-Beta") with [PVS](Principal_Variation_Search "Principal Variation Search")
  - [Transposition Table](Transposition_Table "Transposition Table")
  - [Quiescence Search](Quiescence_Search "Quiescence Search") with [Delta Pruning](Delta_Pruning "Delta Pruning")
  - [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
- [Evaluation](Evaluation "Evaluation")
  - [Material](Material "Material") (with some scaling)
  - [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
  - [Weak](Weak_Pawns "Weak Pawns") and [Passed Pawns](Passed_Pawn "Passed Pawn")
  - [Enemy King Tropism](King_Safety#KingTropism "King Safety")
- [UCI](UCI "UCI") support

## To do

This list represents things that are to be done in order to be ready for a release

- create a text interface for testing and debugging
- comment the source
- get some more speed
- add a [WinBoard](WinBoard "WinBoard") command parser

## Known Deficiencies

Though CPW is a didactic program, it has a couple of features that should not be repeated in Your programs

- Lack of a separate capture generator
- [Transposition Table](Transposition_Table "Transposition Table") (TT) does not save the move itself, but only its position on the list, which limits development options.
- [CPW-Engine_search](CPW-Engine_search "CPW-Engine search") has issues with storing [Lower Bound](Lower_Bound "Lower Bound"), [Upper Bound](Upper_Bound "Upper Bound") and [Exact Score](Exact_Score "Exact Score") into the TT <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## See also

- [Glass](Glass "Glass"), the [UCI engine](Category:UCI "Category:UCI") by the authors of the CPW-Engine.

## Forum Posts

- [Cpw : encore un UCI Engine sans intérêt](http://lefounumerique.xooit.com/t149-Cpw-encore-un-UCI-Engine-sans-interet.htm) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [Le Fou numérique Forum](UEL "UEL"), August 08, 2008 (French)
- [fixing CPW-engine](http://www.talkchess.com/forum/viewtopic.php?t=54802) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 30, 2014
- [Re: Debugging a transposition table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67599&start=2) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 30, 2018 » [CPW-Engine_search](CPW-Engine_search "CPW-Engine search")
- [Re: Plea for a computerchess beginners forum or FAQ](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76574&start=5) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 09, 2021

## External Links

- [nescitus/cpw-engine · GitHub](https://github.com/nescitus/cpw-engine)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a>  [fixing CPW-engine](http://www.talkchess.com/forum/viewtopic.php?t=54802) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 30, 2014
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [nescitus/cpw-engine · GitHub](https://github.com/nescitus/cpw-engine)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Debugging a transposition table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67599&start=2) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 30, 2018
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Plea for a computerchess beginners forum or FAQ](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76574&start=5) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 09, 2021

**[Up One Level](Engines "Engines")**

