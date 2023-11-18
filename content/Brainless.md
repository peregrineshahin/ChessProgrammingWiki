---
title: Brainless
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Brainless**

**Brainless**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C++](Cpp "Cpp") by [Matthew Lai](Matthew_Lai "Matthew Lai") and [Wieland Belka](Wieland_Belka "Wieland Belka") with contributions by [Pawel Koziol](Pawel_Koziol "Pawel Koziol").
Brainless started as project from Matthew 's high school years and has been abandoned in about 2008, when German chess master Wieland Belka and Pawel Koziol contributed to the [evaluation](Evaluation "Evaluation") to play the [First Italian Open Chess Software Cup](IOCSC_2010 "IOCSC 2010"), 2010 in [Carugate](https://en.wikipedia.org/wiki/Carugate).
It played on [FICS](index.php?title=Free_Internet_Chess_Server&action=edit&redlink=1 "Free Internet Chess Server (page does not exist)") under the handle BrainlessChess(C) <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The [opening book](Opening_Book "Opening Book") is converted from [Beowulf](Beowulf "Beowulf").

## Photos

[](http://matthewlai.ca/blog/?p=637)
[IOCSC 2010](IOCSC_2010 "IOCSC 2010"): [Dolphin](Dolphin "Dolphin") and Brainless operated by local chess players <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## Description

## Board Representation

Brainless is a [bitboard](Bitboards "Bitboards") engine and uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") indexed by [6-bit line occupancy](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), and uses the [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) builtins [trailing zero count](BitScan#TrailingZeroCount "BitScan") and [population count](Population_Count "Population Count") <a id="cite-note-3" href="#cite-ref-3">[3]</a> for [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") and [mobility](Mobility "Mobility").

## Search

The [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Selectivity](Selectivity "Selectivity") is applied by [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") (R=2 + depth >= 7), [LMR](Late_Move_Reductions "Late Move Reductions"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") and [check extensions](Check_Extensions "Check Extensions"), the [quiescence search](Quiescence_Search "Quiescence Search") considers [captures](Captures "Captures") and [promotions](Promotions "Promotions") only. Along with the [killer heuristic](Killer_Heuristic "Killer Heuristic"), [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") improves [move ordering](Move_Ordering "Move Ordering"), and also [prunes](Pruning "Pruning") bad captures near the tips.

## Evaluation

The [evaluation](Evaluation "Evaluation") function, written by [Wieland Belka](Wieland_Belka "Wieland Belka"), with contributions from [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), consists mainly of [material](Material "Material"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [cached](Pawn_Hash_Table "Pawn Hash Table") [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety") and various [evaluation patterns](Evaluation_Patterns "Evaluation Patterns").

## Namesake

- [Brainless (Forth)](</Brainless_(Forth)> "Brainless (Forth)") by [David Kühling](David_K%C3%BChling "David Kühling")

## Forum Posts

- [Re: resources on how to write an eval function?](http://www.talkchess.com/forum/viewtopic.php?t=20109&start=7) by cyberfish, [CCC](CCC "CCC"), March 14, 2008

## External Links

## Chess Engine

- [waterreaction / Brainless — Bitbucket](https://bitbucket.org/waterreaction/brainless)
- [Piece of Mind » Blog Archive » Computer Chess Tournament?!](https://matthewlai.ca/blog/2010/11/18/computer-chess-tournament/) by [Matthew Lai](Matthew_Lai "Matthew Lai") » [IOCSC 2010](IOCSC_2010 "IOCSC 2010")

## Misc

- [brainless - Wiktionary](http://en.wiktionary.org/wiki/brainless)
- [Brainless from Wikipedia](https://en.wikipedia.org/wiki/Brainless)
- [no-brainer - Wiktionary](http://en.wiktionary.org/wiki/no-brainer)
- [Brainless](https://mx3.ch/brainless) - Mr Freezer, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [FICS Games Database - Statistics for BrainlessChess(C)](http://www.ficsgames.org/cgi-bin/search.cgi?action=statistics;player=BrainlessChess)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Piece of Mind » Blog Archive » Computer Chess Tournament?!](https://matthewlai.ca/blog/2010/11/18/computer-chess-tournament/) by [Matthew Lai](Matthew_Lai "Matthew Lai")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Other Builtins - Using the GNU Compiler Collection (GCC)](http://gcc.gnu.org/onlinedocs/gcc-4.4.5/gcc/Other-Builtins.html#Other-Builtins)

**[Up one Level](Engines "Engines")**

