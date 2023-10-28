---
title: Clover
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Clover**

\[ Clover <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Clover**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Luca Metehau](Luca_Metehau "Luca Metehau"), written in [C++](Cpp "Cpp"). Clover was first released in April 2021 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, hosted on [GitHub](https://en.wikipedia.org/wiki/GitHub). In January 2022, Clover **3.0** was released featuring [NNUE](NNUE "NNUE") instead of hand crafted evaluation <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

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

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Captures](Captures "Captures") by [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
  - [Razoring](Razoring "Razoring")
  - [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
  - [ProbCut](ProbCut "ProbCut")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Singular Extensions](Singular_Extensions "Singular Extensions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [NNUE](NNUE "NNUE") (Clover 3.0)
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
  - [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
  - [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
  - [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Outposts](Outposts "Outposts")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Connected Pawns](Connected_Pawns "Connected Pawns")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
- [Tempo](Tempo "Tempo")

## Misc

- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
- [Perft](Perft "Perft")

## Forum Posts

- [New engine: Clover](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77154) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), April 23, 2021
- [New engine: Clover](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77156) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), April 23, 2021
- [Re: New engine: Clover](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=77156&start=111) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), January 23, 2022

## [Clover 3.1](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=77156&start=122) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), March 26, 2022 External Links

## Chess Engine

- [GitHub - lucametehau / CloverEngine](https://github.com/lucametehau/CloverEngine)

## Misc

- [clover - Wiktionary](https://en.wiktionary.org/wiki/clover)
- [Clover from Wikipedia](https://en.wikipedia.org/wiki/Clover)
- [Clover (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Clover_(disambiguation)>)
- [Tommy James and the Shondells](https://en.wikipedia.org/wiki/Tommy_James_and_the_Shondells) - [Crimson and Clover](https://en.wikipedia.org/wiki/Crimson_and_Clover) (1968), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Trifolium repens L](https://en.wikipedia.org/wiki/Trifolium_repens), [Image](https://commons.wikimedia.org/wiki/File:79_Trifolium_repens_L.jpg) from [Amédée Masclef](https://en.wikipedia.org/wiki/Am%C3%A9d%C3%A9e_Masclef) (**1891**). *[Atlas des plantes de France](https://commons.wikimedia.org/wiki/Category:Atlas_des_plantes_de_France)*. [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New engine: Clover](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77156) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), April 23, 2021
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: New engine: Clover](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=77156&start=111) by [Luca Metehau](Luca_Metehau "Luca Metehau"), [CCC](CCC "CCC"), January 23, 2022
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [GitHub - lucametehau / CloverEngine](https://github.com/lucametehau/CloverEngine)

**[Up one level](Engines "Engines")**

