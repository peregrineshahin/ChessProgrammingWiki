---
title: Gogobello
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gogobello**

\[ Gogo Dancer Cherry Lei <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gogobello**,

a free [UCI](UCI "UCI") compliant chess engine by [Salvatore Giannotti](Salvatore_Giannotti "Salvatore Giannotti"), written in [C](C "C") and first released in November 2014 as [WinBoard](WinBoard "WinBoard") engine. Gogobello had its tournament debut at [IGT 2015](IGT_2015 "IGT 2015"), when it became sixth from nine - and further improved at the [IGT 2016](IGT_2016 "IGT 2016") as fourth from ten with 4½/7.

## Contents

- [1 Selected Features](#selected-features)
  - [1.1 Move Generation](#move-generation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 Selected Games](#selected-games)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc-2)
- [5 References](#references)

## Selected Features

<a id="cite-note-2" href="#cite-ref-2">[2]</a>

## [Move Generation](Move_Generation "Move Generation")

- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [PVS](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions") in [PV-Nodes](Node_Types#PV "Node Types") only
  - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
  - [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Razoring](Razoring "Razoring")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")

## [Evaluation](Evaluation "Evaluation")

- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Color Weakness](Color_Weakness "Color Weakness")
- [Hanging Piece Evaluation](Hanging_Piece "Hanging Piece")
- [Insufficient Material](Material#InsufficientMaterial "Material") [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [King Safety](King_Safety "King Safety")
- [Knight Outposts](Outposts "Outposts")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Pawn Islands](Pawn_Islands "Pawn Islands")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
- [Pawn Endgame Evaluation](Pawn_Endgame "Pawn Endgame")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") (version 1.1)

## Misc

- [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") (until version 0.12)
- [UCI Protocol](UCI "UCI") (since version 1.0)
- [Opening Book](Opening_Book "Opening Book")
- [Pondering](Pondering "Pondering")
- [Syzygy Endgame Tablebases](Syzygy_Bases "Syzygy Bases")

## Selected Games

[IGT 2015](IGT_2015 "IGT 2015"), round 5, [Neurone](Neurone "Neurone") - Gogobello <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "International Gsei Tournament 2015"]
[Site "Como"]
[Date "2015.09.27"]
[Round "5"]
[White "Neurone XXIV dev."]
[Black "Gogobello 0.11 dev."]
[Result "0-1"]

1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.Nc3 Nxc3 6.dxc3 Be7 7.Bf4 O-O 8.Qd2 Nd7
9.O-O-O Nc5 10.Nd4 Re8 11.f3 c6 12.h4 Qa5 13.Bc4 d5 14.Bb3 Nxb3+ 15.cxb3 Qxa2
16.Qe2 a6 17.Qe5 f6 18.Qh5 g6 19.Qh6 Bf8 20.Qxf8+ Kxf8 21.Bh6+ Kg8 22.g4 c5
23.Nc2 Qxb3 24.Na1 Qa4 25.Nc2 f5 26.Rxd5 fxg4 27.fxg4 Bxg4 28.Rg1 Re2 29.Bd2 b6
30.Rg5 Rxd2 31.Kxd2 Qf4+ 32.Ne3 Qf2+ 33.Kd3 Qe2+ 34.Ke4 Re8+ 35.Kd5 Qd3+ 36.Kc6
Qb5+ 0-1

```

## Forum Posts

- [Gogobello 9.10 x64 with WinBoard 4.8.0](http://www.talkchess.com/forum/viewtopic.php?t=56859) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 03, 2015
- [Gogobello new release](http://www.talkchess.com/forum/viewtopic.php?t=64696) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), July 23, 2017

## External Links

## Chess Engine

- [Homepage - gogobello](http://sasachess.altervista.org/gogobello/index.html)
- [Gogobello](https://www.g-sei.org/gogobello/) « [G 6](G_6 "G 6")
- [Gogobello](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Gogobello&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [gogo - Wiktionary](https://en.wiktionary.org/wiki/gogo)
- [go-go - Wiktionary](https://en.wiktionary.org/wiki/go-go)
- [à gogo - Wiktionary](https://en.wiktionary.org/wiki/%C3%A0_gogo)
- [Go go from Wikipedia](https://en.wikipedia.org/wiki/Go_go)
- [Go-go from Wikipedia](https://en.wikipedia.org/wiki/Go-go)
- [Go-go dancing from Wikipedia](https://en.wikipedia.org/wiki/Go-go_dancing)
- [bello - Wiktionary](https://en.wiktionary.org/wiki/bello)
- [Smokey Robinson](https://en.wikipedia.org/wiki/Smokey_Robinson) & [The Miracles](https://en.wikipedia.org/wiki/The_Miracles) - [Going To A Go-Go](https://en.wikipedia.org/wiki/Going_to_a_Go-Go_%28song%29) (1965), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Gogo Dancer](https://en.wikipedia.org/wiki/Go-go_dancing) [Cherry Lei](https://instagram.com/gogocherrylei/) dancing at The Fix in [Honolulu](https://en.wikipedia.org/wiki/Honolulu), [Hawaii](https://en.wikipedia.org/wiki/Hawaii) on June 27, 2014, [Photo](https://commons.wikimedia.org/wiki/File:Gogo_Dancer_Cherry_Lei.jpg) by [Peter Chiapperino](https://commons.wikimedia.org/wiki/User:Peterchiapperino), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> based on features mentioned gogobello_11_x64.zip/readme.txt, October 2015, [IGT 2015](IGT_2015 "IGT 2015") and [Homepage - gogobello](http://sasachess.altervista.org/gogobello/index.html), Version History
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [International Gsei Tournament 2015 « G 6](http://www.g-sei.org/international-gsei-tournament-2015/)

**[Up one Level](Engines "Engines")**

