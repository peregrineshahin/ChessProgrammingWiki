---
title: BitGenie
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bit-Genie**

\[ [Majlis al Jinn](https://en.wikipedia.org/wiki/Majlis_al_Jinn) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bit-Genie**,

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Aryan Parekh](index.php?title=Aryan_Parekh&action=edit&redlink=1 "Aryan Parekh (page does not exist)"), written in [C++](Cpp "Cpp"),
licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), and first released in March 2021 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Bit-Genie **9**, released in August 2021, features [NNUE](NNUE "NNUE") [Evaluation](Evaluation "Evaluation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Selected Features

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [Board Representation](Board_Representation "Board Representation")

- [8x8 Board](8x8_Board "8x8 Board")
- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards") implementation by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") (v7)
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") (v3)
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") (v3)
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (v6)
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (v8)
  - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation") (v8)
  - [Check Extensions](Check_Extensions "Check Extensions") (v8)

## [Evaluation](Evaluation "Evaluation")

- [NNUE](NNUE "NNUE") (v9)
- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Passed Pawns](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")
- [Pawn Shield](King_Safety#PawnShield "King Safety")

## Misc

- [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book") (v7)
- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") (v4)

## See also

- [Djinn](Djinn "Djinn")
- [Genie](Genie "Genie")

## Forum Posts

- [New open-source engine, Bit-Genie](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76913) by [Aryan Parekh](index.php?title=Aryan_Parekh&action=edit&redlink=1 "Aryan Parekh (page does not exist)"), [CCC](CCC "CCC"), March 21, 2021
- [Bit-Genie 9 release](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=77982) by [Aryan Parekh](index.php?title=Aryan_Parekh&action=edit&redlink=1 "Aryan Parekh (page does not exist)"), [CCC](CCC "CCC"), August 21, 2021

## External Links

## Chess Engine

- [GitHub - Aryan1508/Bit-Genie: UCI chess engine in C++](https://github.com/Aryan1508/Bit-Genie)
- [Bit-Genie](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Bit-Genie&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Genie (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Genie_%28disambiguation%29)
- [Jinn from Wikipedia](https://en.wikipedia.org/wiki/Jinn)
- [Project Genie from Wikipedia](https://en.wikipedia.org/wiki/Project_Genie)
- [Genie (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Genie_%28programming_language%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Climber on their way to the cave floor at [Majlis al Jinn](https://en.wikipedia.org/wiki/Majlis_al_Jinn), [Image](https://commons.wikimedia.org/wiki/File:Descending_into_cave.jpg) by Michaelmcandrew, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [New open-source engine, Bit-Genie](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76913) by [Aryan Parekh](index.php?title=Aryan_Parekh&action=edit&redlink=1 "Aryan Parekh (page does not exist)"), [CCC](CCC "CCC"), March 21, 2021
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Release v9 · Aryan1508/Bit-Genie · GitHub](https://github.com/Aryan1508/Bit-Genie/releases/tag/v9)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Releases · Aryan1508/Bit-Genie · GitHub](https://github.com/Aryan1508/Bit-Genie/releases)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Bit-Genie/magicmoves.cpp at master · Aryan1508/Bit-Genie · GitHub](https://github.com/Aryan1508/Bit-Genie/blob/master/src/magicmoves.cpp)

**[Up one level](Engines "Engines")**

