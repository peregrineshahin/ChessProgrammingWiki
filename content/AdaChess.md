---
title: AdaChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * AdaChess**

\[ [Ada Lovelace](Mathematician#Lovelace "Mathematician") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**AdaChess**,

an [open source chess engine](Category:Open_Source "Category:Open Source") by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), written in [Ada](index.php?title=Ada&action=edit&redlink=1 "Ada (page does not exist)") and released under the [GPL license](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The development started in early 2012 and the first version has been released on January 21, 2013. Full compliant to the rules of chess, it also recognize [draws](Draw "Draw") by [insufficient material](Material#InsufficientMaterial "Material").
AdaChess is a [console application](https://en.wikipedia.org/wiki/Console_application) without own [GUI](GUI "GUI"), but supports the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard")/[XBoard](XBoard "XBoard") protocol.
So far, AdaChess played the [IGT 2014](IGT_2014 "IGT 2014"), [IGT 2015](IGT_2015 "IGT 2015"), [IGT 2016](IGT_2016 "IGT 2016"), [IGT 2017](IGT_2017 "IGT 2017") and [IGT 2018](IGT_2018 "IGT 2018") [G 6](G_6 "G 6") tournaments, and the [PT 54](PT_54 "PT 54") [CSVN](CSVN "CSVN") tournament <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>, all over the board.

## Features

<a id="cite-note-6" href="#cite-ref-6">[6]</a>

## [Board Representation](Board_Representation "Board Representation")

- [10x12 Board](10x12_Board "10x12 Board") <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [Piece-Lists](Piece-Lists "Piece-Lists")
- [Legal Move Generation](Move_Generation#Legal "Move Generation")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
  - [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
  - [Rook on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
- [Tempo](Tempo "Tempo")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
    - [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
    - [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")
- [King Safety](King_Safety "King Safety")
  - [Castling Rights](Castling_Rights "Castling Rights")
  - [Open Files](Open_File "Open File") near the King
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [Pawn Shield](King_Safety#PawnShield "King Safety")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")

## Forum Posts

- [AdaChess v2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=53309) by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), August 16, 2014
- [AdaChess v2016.11.08-pre released](http://talkchess.com/forum/viewtopic.php?t=62023), by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), November 08, 2016
- [AdaChess v.30 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68763)by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), October 29, 2018
- [IGT 2018 - Man vs Machine](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=68764) by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), October 29, 2018
- [Re: fast(er) movegen](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69216&start=6) by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), December 10, 2018
- [AdaChess release 3.6 available!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71533) by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), August 12, 2019

## External Links

- [AdaChess home page](http://www.adachess.com)
- [AdaChess](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=AdaChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Ada Lovelace](Mathematician#Lovelace "Mathematician") by [Margaret Sarah Carpenter](index.php?title=Category:Margaret_Sarah_Carpenter&action=edit&redlink=1 "Category:Margaret Sarah Carpenter (page does not exist)"), 1836, oil on canvas, [Government Art Collection](https://en.wikipedia.org/wiki/Government_Art_Collection), [Ada Lovelace from Wikipedia](https://en.wikipedia.org/wiki/Ada_Lovelace), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> The programming language [Ada](index.php?title=Ada&action=edit&redlink=1 "Ada (page does not exist)") was named after [Ada Lovelace](Mathematician#Lovelace "Mathematician"), who has been credited as the first computer programmer, [Ada (programming language) from Wikipedia](<https://en.wikipedia.org/wiki/Ada_(programming_language)>)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> The announced [AdaChess](http://joselauro.tripod.com/prechess-en.html) by [PreChess](index.php?title=PreChess&action=edit&redlink=1 "PreChess (page does not exist)") author [José Lauro Strapasson](index.php?title=Jos%C3%A9_Lauro_Strapasson&action=edit&redlink=1 "José Lauro Strapasson (page does not exist)") is confirmed defunct
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [AdaChess al Csvn](http://www.g-sei.org/adachess-al-csvn/), [G 6](G_6 "G 6")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Interview on g-sei](http://www.adachess.com/other/interview-on-g-sei.html), December 12, 2018
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> Features based on [AdaChess download](http://www.adachess.com/download), AdaChess-v3.1.zip\\src\\
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: fast(er) movegen](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69216&start=6) by [Alessandro Iavicoli](Alessandro_Iavicoli "Alessandro Iavicoli"), [CCC](CCC "CCC"), December 10, 2018

**[Up one Level](Engines "Engines")**

