---
title: Francesca
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Francesca**

\[ [Piero della Francesca](index.php?title=Category:Piero_della_Francesca&action=edit&redlink=1 "Category:Piero della Francesca (page does not exist)") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Francesca**,

a chess engine by [Tom King](Tom_King "Tom King"), written in [C](C "C"), which uses many state of the art chess-programming techniques. Francesca played five [World Microcomputer Chess Championships](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") from 1995 until 2000, including the [WCCC 1999](WCCC_1999 "WCCC 1999") with 4 out of 7, and wins against former champion [MChess](MChess "MChess") and draws against the massive parallel programs [Zugwang](</Zugzwang_(Program)> "Zugzwang (Program)") and [CilkChess](CilkChess "CilkChess"). In 2000 Francesca was released as [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine <a id="cite-note-2" href="#cite-ref-2">[2]</a> and was further improved as Francesca MAD (Manic, Aggressive, Dynamic) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Descriptions](#descriptions)
  - [1.1 1997](#1997)
  - [1.2 1999](#1999)
- [2 History of Francesca](#history-of-francesca)
- [3 Selected Games](#selected-games)
- [4 Forum Posts](#forum-posts)
  - [4.1 2000 ...](#2000-...)
  - [4.2 2010 ...](#2010-...)
  - [4.3 2020 ...](#2020-...)
- [5 External Links](#external-links)
  - [5.1 Chess Engine](#chess-engine)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Descriptions

Descriptions given from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## 1997

```
Francesca follows the trend of programs since the late 1970s. It uses [iterative deepening](Iterative_Deepening "Iterative Deepening") [alpha-beta search](Alpha-Beta "Alpha-Beta") to determine which move to make. The search is [selective](Selectivity "Selectivity") rather than [brute-force](Brute-Force "Brute-Force"). [Null moves](Null_Move_Reductions "Null Move Reductions"), and a home- grown [forward pruning](Pruning "Pruning") mechanism are used to help accelerate the search. In addition, a [hash table](Transposition_Table "Transposition Table") is used to aid [move ordering](Move_Ordering "Move Ordering"), and save searching of subtrees that have already been visited in the search.

```

```
The [evaluation function](Evaluation "Evaluation") is simple, but it knows something about [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety"), and [piece placement](Piece-Square_Tables "Piece-Square Tables"). There is always a tradeoff between [knowledge](Knowledge "Knowledge") and speed, and Francesca falls into the category of a "fast, dumb" searcher, rather than a "slow, smart" searcher. 

```

## 1999

```
Francesca is an amateur program. It follows the trends of most chess programs since the 1970's and uses many of the state-of-the-art techniques: [aspiration](Aspiration_Windows "Aspiration Windows") alpha-beta, null moves, other forward pruning mechanisms, a large [transposition table](Transposition_Table "Transposition Table"), an [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table"), large [opening book](Opening_Book "Opening Book") etc.

```

```
Prior to 1998, Francesca relied mainly on [piece-square values](Piece-Square_Tables "Piece-Square Tables") and a fast search to play good chess. In 1998, the evalution code was completely rewritten, and all evaluation is now done in the [leaves](Leaf_Node "Leaf Node") of the [search tree](Search_Tree "Search Tree"). This has produced stronger play; although 1999 Francesca is slower in nodes per second than 1997 Francesca, she plays a more interesting and challenging game. 

```

## History of Francesca

From [Tom King's](Tom_King "Tom King") personal website <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

```
In the Autumn of 1991, I had the chance to try out my creation on a 386SX PC, running at 16Mhz. It seemed so fast compared with the [Amiga](Amiga "Amiga")! Before long I bought myself a 486DX PC, running at 33Mhz, and began developing Francesca in earnest.

```

```
Little by little, Francesca's playing standard improved. [Null moves](Null_Move_Reductions "Null Move Reductions") added a turbo charger to an otherwise unremarkable chess engine, and evaluation by [piece-value squares](Piece-Square_Tables "Piece-Square Tables") increased the NPS figure and search depth. There were still problems, and after the [WMCCC in 1995](WMCCC_1995 "WMCCC 1995") (Paderborn), I bit the bullet, and added [hash tables](Transposition_Table "Transposition Table"). Improving move order and [history tables](History_Heuristic "History Heuristic"), along with the new hash tables meant that Francesca 1996 was over 10 times quicker at searching through the plies than Francesca 1995. And it showed, Francesca gaining a very respectable 9th place at the [WMCCC 1996](WMCCC_1996 "WMCCC 1996") in Jakarta.

```

```
Between Jakarta and the [WMCCC 1997](WMCCC_1997 "WMCCC 1997") in Paris, there were few changes - some evaluation changes, some bug fixes, and some optimizations. And some bugs, too. Francesca struggled against some opponents she really should have beaten.

```

```
The problems at Paris made me realize that a change in direction was required. I rewrote the entire evaluation function, changing Francesca from a simple piece-value squares searcher to a full leaf evaluator. The benefits were immediate, obvious, and immense. Suddenly, Francesca was playing more interesting, challenging chess. I had the opportunity to enter her into the [1998 Spanish computer chess championship](SCCC_1998 "SCCC 1998"), and she came within an ace of winning the whole competition! 

```

## Selected Games

[WCCC 1999](WCCC_1999 "WCCC 1999"), round 3, Francesca - [MChess](MChess "MChess") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```

[Event "WCCC 1999"]
[Site "Paderborn, Germany"]
[Date "1999.06.15"]
[Round "3"]
[White "Francesca"]
[Black "MChess"]
[Result "1-0"]

1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3+ 6.bxc3 Ne7 7.Qg4 Qc7 8.Qxg7 Rg8 
9.Qxh7 cxd4 10.Ne2 Nbc6 11.f4 Bd7 12.Qd3 dxc3 13.Be3 d4 14.Nxd4 Nxd4 15.Bxd4 
Bc6 16.Qxc3 Nd5 17.Qd2 Rg4 18.Be2 Rxg2 19.Rg1 Rxg1+ 20.Bxg1 O-O-O 21.Rd1 Rg8 
22.Bf2 Ba4 23.Rb1 Rd8 24.c4 Ne7 25.Qc3 Nd5 26.Qf3 Ne7 27.Rb4 Bc6 28.Qe3 b6 
29.Qb3 Qd7 30.Qc2 Nf5 31.c5 b5 32.Qd1 Qe8 33.Qc2 Qd7 34.Qa2 Bb7 35.Qc2 Qc6 
36.Bf1 Qf3 37.c6 Ne3 38.cxb7+ Kb8 39.Bxe3 Qxe3+ 40.Qe2 Qc1+ 41.Kf2 Rd2 42.h3 
Rxe2+ 43.Bxe2 a6 44.Bf3 Qxa3 45.Re4 Qc5+ 46.Kg3 b4 47.Re1 a5 48.Rd1 Qc7 49.h4 
Ka7 50.h5 a4 51.h6 f6 52.Rd4 Qe7 53.Rc4 fxe5 54.Rc8 Qxb7 55.Bxb7 1-0  

```

## Forum Posts

## 2000 ...

- [Francesca 0.78 by Tom King is available !](https://www.stmintz.com/ccc/index.php?id=101076) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 09, 2000
- [Francesca MAD v0.11 Released](https://www.stmintz.com/ccc/index.php?id=491623) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 06, 2006

## 2010 ...

- [Francesca M.A.D v0.15 released](http://www.talkchess.com/forum/viewtopic.php?t=36836) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), November 28, 2010
- [Francesca M.A.D 0.19 released](http://www.talkchess.com/forum/viewtopic.php?t=40868) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), October 23, 2011
- [Francesca Chess Engine: Why no love?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=62324) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), November 30, 2016
- [After an 8 year break..](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69426) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), December 30, 2018
- [New Release of Francesca MAD](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69472) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 03, 2019
- [New Release of Francesca MAD - imminent](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69651) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 19, 2019
- [New Release of Francesca - 0.22](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70124) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 06, 2019
- [Francesca 0.25 Released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71401) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), July 28, 2019

## 2020 ...

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=566) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), December 23, 2020

## External Links

## Chess Engine

- [Computer chess - my program, Francesca](http://www.zen55564.zen.co.uk/francesca.htm)
- [Francesca's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=32)

## Misc

- [Francesca from Wikipedia](https://en.wikipedia.org/wiki/Francesca) ([Given name](https://en.wikipedia.org/wiki/Given_name))
- [Francisca from Wikipedia](https://en.wikipedia.org/wiki/Francisca) ([Throwing axe](https://en.wikipedia.org/wiki/Throwing_axe))
- [Stan Kenton](https://en.wikipedia.org/wiki/Stan_Kenton) - Francesca ([Masters Of Swing](https://www.discogs.com/Stan-Kenton-Masters-Of-Swing/master/1658402)), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Resurrection (Piero della Francesca) from Wikipedia](<https://en.wikipedia.org/wiki/The_Resurrection_(Piero_della_Francesca)>)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Francesca 0.78 by Tom King is available !](https://www.stmintz.com/ccc/index.php?id=101076) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 09, 2000
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Francesca MAD v0.11 Released](https://www.stmintz.com/ccc/index.php?id=491623) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 06, 2006
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Francesca's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=32)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Silentshark - Tom King's personal website - Computer Chess](http://www.silentshark.co.uk/)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Paderborn 1999 - Chess - Round 3 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=8&round=3&id=5)

**[Up one Level](Engines "Engines")**

