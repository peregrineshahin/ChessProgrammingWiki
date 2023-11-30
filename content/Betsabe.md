---
title: Betsabe
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Betsabe**

\[ Batsheba with King Davids Letter <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Betsabe II**, (Betsabe, Betsabé II)

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation") by [Juan Benitez](Juan_Benitez "Juan Benitez"), written in [C](C "C"), with appropriate compiles able to run under [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Android](Android "Android") platforms.
Betsabe II is successor of Betsabe, which already played various [Spanish Computer Chess Championships](Spanish_Computer_Chess_Championship "Spanish Computer Chess Championship") in the 90s, notably the [SCCC 1993](SCCC_1993 "SCCC 1993") where it became first Spanish Champion with a 100% score, and the [SCCC 1994](SCCC_1994 "SCCC 1994") as runner-up behind [Zeus II](Zeus "Zeus").
Betsabe was initially based on [Dieter Steinwender's](Dieter_Steinwender "Dieter Steinwender") and [Chrilly Donninger's](Chrilly_Donninger "Chrilly Donninger") program [Minimax](</Minimax_(program)> "Minimax (program)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, but differences in [search](Search "Search") and [evaluation](Evaluation "Evaluation") are substantial.

## Description

## Board Representation

Betsabe II maintains a [10x12 board](10x12_Board "10x12 Board") as internal [board representation](Board_Representation "Board Representation") and to [generate moves](Move_Generation "Move Generation"). Definition of (part of) the [initial position](Initial_Position "Initial Position") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
const int Tablero_Inicio[120] =  {
FUERA, FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA, FUERA,
FUERA, FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA, FUERA,
FUERA,  T_B,    C_B ,   A_B ,   D_B ,   R_B ,   A_B ,   C_B ,   T_B,  FUERA,
FUERA,  P_B,    P_B ,   P_B ,   P_B ,   P_B ,   P_B ,   P_B ,   P_B,  FUERA,
FUERA, VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO, FUERA,
FUERA, VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO, FUERA,
FUERA, VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO, FUERA,
FUERA, VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO,  VACIO, FUERA,
FUERA,  P_N ,   P_N ,   P_N ,   P_N ,   P_N ,   P_N ,   P_N ,   P_N,  FUERA,
FUERA,  T_N,    C_N ,   A_N ,   D_N ,   R_N ,   A_N ,   C_N ,   T_N,  FUERA,
FUERA, FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA, FUERA,
FUERA, FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA,  FUERA, FUERA};

```

## Search

Betsabe II applies [PVS](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") [fractional ply](Depth#FractionalPlies "Depth") framework in conjunction with [mate distance pruning](Mate_Distance_Pruning "Mate Distance Pruning"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions"), [razoring](Razoring "Razoring"), [futility pruning](Futility_Pruning "Futility Pruning"), [SEE pruning](Static_Exchange_Evaluation "Static Exchange Evaluation") in [quiescence](Quiescence_Search "Quiescence Search"), and [check-](Check_Extensions "Check Extensions") and [capture extensions](Capture_Extensions "Capture Extensions") with transitions to [pawn endings](Pawn_Endgame "Pawn Endgame"). [Move ordering](Move_Ordering "Move Ordering") is enhanced by [history-](History_Heuristic "History Heuristic") and [killer heuristic](Killer_Heuristic "Killer Heuristic") with two ordinary [killer moves](Killer_Move "Killer Move") and one [mate killer](Mate_Killers "Mate Killers") per [ply](Ply "Ply").

## Evaluation

The [evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") using [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") with respect to [bounds](Bound "Bound"), and otherwise considers [mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety") and various [piece terms](Evaluation_of_Pieces "Evaluation of Pieces").

## Selected Games

[SCCC 1999](SCCC_1999 "SCCC 1999"), round 7, Betsabe - [Genesis](Genesis_AR "Genesis AR") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```
[Event "SCCC 1999"]
[Site "Parets del Valles"]
[Date "29.12.99"]
[Round "7"]
[White "Betsabe"]
[Black "Genesis"]
[Result "1-0"]

1.d4 e6 2.e4 d5 3.Nc3 Bb4 4.e5 Bxc3+ 5.bxc3 c5 6.Qg4 g6 7.Nf3 f5 8.Qg5 Qc7 
9.Qd2 Nc6 10.Ba3 b6 11.Rb1 Bb7 12.Bd3 Nge7 13.O-O c4 14.Be2 h6 15.Rb2 Qd7 
16.Rfb1 g5 17.h3 O-O-O 18.Nh2 Ng6 19.Bd6 Nf4 20.Bf3 Qf7 21.Nf1 Rxd6 22.exd6 
Rh7 23.Ng3 Qd7 24.Ne2 Nxe2+ 25.Qxe2 Qxd6 26.a4 Re7 27.Ra1 e5 28.Qd2 e4 29.Bh5 
Na5 30.Rba2 f4 31.Re1 Kb8 32.Qc1 Ka8 33.Qb2 e3 34.Raa1 exf2+ 35.Kxf2 Qf6 
36.Rxe7 Qxe7 37.Re1 Qd7 38.Re8+ Bc8 39.Rf8 Qe6 40.Bg4 Qe3+ 41.Kf1 Kb7 42.Bxc8+ 
Kc7 43.Bg4 Nc6 44.Rc8+ Kb7 45.Rxc6 Kxc6 46.Qb5+ Kb7 47.Qxd5+ Kc7 48.Qd7+  
1-0

```

## See also

- [David](David "David")
- [Minimax (program)](</Minimax_(program)> "Minimax (program)")

## Forum Posts

- [New engine - Betsabé II 1.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=51551) by Tony Mokonen, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 18, 2011
- [Betsabe II 1.47](http://www.talkchess.com/forum/viewtopic.php?t=53263) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 12, 2014
- [Betsabe II 1.66 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60293) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), May 27, 2016
- [Betsabe II 1.75 released](http://www.talkchess.com/forum/viewtopic.php?t=64686) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), July 22, 2017
- [Betsabe II 1.84 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=54101) by [Graham Banks](Graham_Banks "Graham Banks"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 07, 2018

## External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/BETSABE II](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/BETSABE%20II/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
- [Betsabe II](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Betsabe&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Betsabé - Wikipedia.es](http://es.wikipedia.org/wiki/Betsab%C3%A9) (Spanish)
- [Bathsheba from Wikipedia](https://en.wikipedia.org/wiki/Bathsheba)
- [Books of Samuel from Wikipedia](https://en.wikipedia.org/wiki/Books_of_Samuel)
- [Bathsheba is One of the Most Beguiling Characters in the Bible](http://www.usnews.com/news/religion/articles/2008/01/25/bathsheba-is-one-of-the-most-beguiling-characters-in-the-bible) by [Jessica Feinstein](http://www.usnews.com/topics/author/jessica_feinstein), [US News & World Report](https://en.wikipedia.org/wiki/U.S._News_%26_World_Report), January 25, 2008
- [David and Bathsheba (film) from Wikipedia](https://en.wikipedia.org/wiki/David_and_Bathsheba_%28film%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Willem Drost](index.php?title=Category:Willem_Drost&action=edit&redlink=1 "Category:Willem Drost (page does not exist)") - [Bathsheba holding King David's letter](https://commons.wikimedia.org/wiki/File:Willem_Drost_-_Batsheba_met_de_brief_van_koning_David.jpg), 1654, [Louvre Museum](https://en.wikipedia.org/wiki/The_Louvre), [Bathsheba from Wikipedia](https://en.wikipedia.org/wiki/Bathsheba)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> betsabe-II-109-ja-jm/readme.txt
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> data.h
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Spanish Championship: Final Round](https://www.stmintz.com/ccc/index.php?id=84977) by Sergio Martinez, [CCC](CCC "CCC"), December 29, 1999

**[Up one level](Engines "Engines")**

