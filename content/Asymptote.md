---
title: Asymptote
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Asymptote**

\[ Asymptotic Intersections <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Asymptote**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), written in [Rust](Rust "Rust") and licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), first released in July 2018.

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 Forum Posts](#forum-posts)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc-2)
- [4 References](#references)

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboard Board-Definition 6:2](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
- [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")
- [BMI2 - PEXT Bitboards](BMI2#PEXTBitboards "BMI2")

## [Search](Search "Search")

<a id="cite-note-2" href="#cite-ref-2">[2]</a>

- [Lazy SMP](Lazy_SMP "Lazy SMP") using [Threads](Thread "Thread") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
  - [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
  - [Four Buckets](Transposition_Table#Bucket "Transposition Table")
  - [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing") using [ChaCha PRNG](Pseudorandom_Number_Generator#ChaCha "Pseudorandom Number Generator")
- [Selectivity](Selectivity "Selectivity")
  - [Fractional Plies](Depth#FractionalPlies "Depth")
  - [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
    - [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
  - [Pruning](Pruning "Pruning")/[Reductions](Reductions "Reductions")
    - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
    - [Futility Pruning](Futility_Pruning "Futility Pruning")
    - [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
    - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
    - [ProbCut](ProbCut "ProbCut")
    - [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
    - [Static Exchange Evaluation Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Staged Move Generation](Move_Generation#Staged "Move Generation")
  - [Hash Move](Hash_Move "Hash Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
- [Outposts](Outposts "Outposts")
- [King Safety](King_Safety "King Safety")
- [Tempo](Tempo "Tempo")

## Misc

- [Perft](Perft "Perft")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")

## Forum Posts

- [Asymptote (UCI) by Maximilian Lupke](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68074) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 25, 2018
- [Asymptote 0.4 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69677) by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), [CCC](CCC "CCC"), January 21, 2019
- [Asymptote 0.5 (with SMP)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70387) by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), [CCC](CCC "CCC"), April 02, 2019
- [Asymptote 0.6](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70818) by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), [CCC](CCC "CCC"), May 25, 2019
- [Depth anomaly in Asymptote](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71319) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), July 19, 2019
- [Asymptote 0.7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72512) by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), [CCC](CCC "CCC"), December 06, 2019

## External Links

## Chess Engine

- [GitHub - malu/asymptote: A UCI chess engine](https://github.com/malu/asymptote)
- [Asymptote](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Asymptote&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [asymptote - Wiktionary](https://en.wiktionary.org/wiki/asymptote)
- [Asymptote from Wikipedia](https://en.wikipedia.org/wiki/Asymptote)
- [Asymptote (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Asymptote_(disambiguation)>)
- [Midday Veil](http://records.translinguisticother.com/midday-veil/) - [Asymptote II](https://middayveil.bandcamp.com/track/asymptote-part-2) (2010), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Example](https://commons.wikimedia.org/wiki/File:Asymptote02_vectorial.svg) of a curve with its asymptote shows that the curve may intersect the asymptote, in this case an infinite amount of times, by Guillaume Jacquenot, March 20, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [asymptote/search.rs at master · malu/asymptote · GitHub](https://github.com/malu/asymptote/blob/master/src/search.rs)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Asymptote 0.5 (with SMP)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70387) by [Maximilian Lupke](Maximilian_Lupke "Maximilian Lupke"), [CCC](CCC "CCC"), April 02, 2019
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [asymptote/eval.rs at master · malu/asymptote · GitHub](https://github.com/malu/asymptote/blob/master/src/eval.rs)

**[Up one level](Engines "Engines")**

