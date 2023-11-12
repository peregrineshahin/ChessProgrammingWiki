---
title: Demolito
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Demolito**

\[ Being Demolished <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Demolito**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by Lucas Braesch, licensed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C](C "C"), first announced at [OpenChess](Computer_Chess_Forums "Computer Chess Forums") in January 2017 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, a revised stable release published in June 2017 as completely rewritten new [DiscoCheck](DiscoCheck "DiscoCheck") featuring [SMP](Parallel_Search "Parallel Search") and [Chess960](Chess960 "Chess960") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, with executables available for [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Android](Android "Android").

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Dense Piece-Color Board-Definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [8x8 Board](8x8_Board "8x8 Board")
- [Little-Endian Rank-File Mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")
- [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Transposition Table](Transposition_Table "Transposition Table")

[Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

- [Selectivity](Selectivity "Selectivity")

[Eval Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
[Razoring](Razoring "Razoring")
[Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
[Late Move Reductions](Late_Move_Reductions "Late Move Reductions")

- [Quiescence Search](Quiescence_Search "Quiescence Search")

[SEE Pruning \< 0](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")

- [Move Ordering](Move_Ordering "Move Ordering")

## [Refutation Table](Refutation_Table "Refutation Table") [MVV/LVA](MVV-LVA "MVV-LVA") [History Heuristic](History_Heuristic "History Heuristic") [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")

[Bishop Pair](Bishop_Pair "Bishop Pair")
[Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")

- [Mobility](Mobility "Mobility")
- [Hanging Pieces](Hanging_Piece "Hanging Piece")
- [Penalty for Pieces](Evaluation_of_Pieces "Evaluation of Pieces") on own [Pawn Frontspans](Pawn_Spans "Pawn Spans")
- [King Safety](King_Safety "King Safety")

[Attacking King Zone](King_Safety#Attacking "King Safety")
[Check Threats](King_Pattern#VulnerableOnDistantChecks "King Pattern")
[Pawn Shield](King_Safety#PawnShield "King Safety")

- [Pawn Structure](Pawn_Structure "Pawn Structure")

## [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table") [Pawn Chain](</Defended_Pawns_(Bitboards)> "Defended Pawns (Bitboards)") [Phalanx](</Duo_Trio_Quart_(Bitboards)> "Duo Trio Quart (Bitboards)") [Holes](Holes "Holes") [Isolated Pawn](Isolated_Pawn "Isolated Pawn") [Passed Pawn](Passed_Pawn "Passed Pawn") See also

- [DiscoCheck](DiscoCheck "DiscoCheck")

## Forum Posts

## 2017

- [New UCI Engine: Demolito](http://www.open-chess.org/viewtopic.php?f=7&t=3069) by lucasart, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2017
- [Demolito Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=60191) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 16, 2016
- [Demolito UCI x64 25th January 2017 - 30th January 2017](http://www.talkchess.com/forum/viewtopic.php?t=63093) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 08, 2017
- [New DiscoCheck is cooking](http://www.talkchess.com/forum/viewtopic.php?t=64173) by lucasart, [CCC](CCC "CCC"), June 04, 2017
- [New version: Demolito 2017-08-26](http://www.talkchess.com/forum/viewtopic.php?t=65004) by lucasart, [CCC](CCC "CCC"), August 27, 2017

## 2018 ...

- [Demolito 20180301 released](http://www.talkchess.com/forum/viewtopic.php?t=66715) by lucasart, [CCC](CCC "CCC"), March 01, 2018
- [Demolito 20181029 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68845) by lucasart, [CCC](CCC "CCC"), November 06, 2018
- [Could someone do a Demolito compile please ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70340) by Modern Times, [CCC](CCC "CCC"), March 28, 2019

## External Links

## Chess Engine

- [GitHub - lucasart/Demolito: UCI Chess Engine](https://github.com/lucasart/Demolito)
- [Demolito](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Demolito&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [demolito - Wiktionary](https://en.wiktionary.org/wiki/demolito)
- [Demolition from Wikipedia](https://en.wikipedia.org/wiki/Demolition)
- [Manfred Mann's Earth Band](Category:Manfred_Mann%27s_Earth_Band "Category:Manfred Mann's Earth Band") - [Demolition Man](https://en.wikipedia.org/wiki/Demolition_Man_%28song%29), [Live in Budapest 1983](https://en.wikipedia.org/wiki/Budapest_Live), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [High Reach Demolition Excavator](https://en.wikipedia.org/wiki/Long_reach_excavator) - Hydraulic demolition scissors on chassis CAT 365B L. Arm is 30 m long, [Image](https://commons.wikimedia.org/wiki/File:Hydraulicke_demolicni_nuzky_na_podvozku_CAT_330.jpg) by [Michal Maňas](https://commons.wikimedia.org/wiki/User:Snek01), June 21, 2006, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New UCI Engine: Demolito](http://www.open-chess.org/viewtopic.php?f=7&t=3069) by lucasart, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2017
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New DiscoCheck is cooking](http://www.talkchess.com/forum/viewtopic.php?t=64173) by Lucas Braesch, [CCC](CCC "CCC"), June 04, 2017
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Demolito/types.h at master · lucasart/Demolito · GitHub](https://github.com/lucasart/Demolito/blob/master/src/types.h)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Demolito/recurse.h at master · lucasart/Demolito · GitHub](https://github.com/lucasart/Demolito/blob/master/src/recurse.h)

**[Up one Level](Engines "Engines")**

