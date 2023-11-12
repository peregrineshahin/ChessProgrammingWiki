---
title: Halogen
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Halogen**

\[ Br···O halogen bonds <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Halogen**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), written in [C++](Cpp "Cpp"), licensed under the [GPL v3](Free_Software_Foundation#GPL "Free Software Foundation") and first released on [GitHub](https://en.wikipedia.org/wiki/GitHub) in June 2019 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Since version 7 in September 2020, Halogen features an own, [incrementally updated](Incremental_Updates "Incremental Updates") [neural network](Neural_Networks "Neural Networks") for its [evaluation function](Evaluation_Function "Evaluation Function"), inspired by [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE").
Halogen 8 features a larger network than Halogen 7, but runs significantly faster due to improvements and optimisations, best if compiled for [AVX2](AVX2 "AVX2") instructions.
Its development and testing was supported on the [OpenBench](OpenBench "OpenBench") framework. Networks are trained through a private, from scratch [C](C "C") implementation created in collaboration with [Andrew Grant](Andrew_Grant "Andrew Grant") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Features

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Legal Move Generation](Move_Generation#Legal "Move Generation") by [Tinker's Approach](Sliding_Piece_Attacks#Tinker.27s_Approach "Sliding Piece Attacks")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [NegaScout](NegaScout "NegaScout")
- [Transposition Table](Transposition_Table "Transposition Table")
  - [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
  - [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [Captures](Captures "Captures")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0 or [PV](Principal_Variation "Principal Variation")
  - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") (7th, 2nd rank)
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [NNUE](NNUE "NNUE") (>= Halogen 7)

## Misc

- [Syzygy Bases](Syzygy_Bases "Syzygy Bases")

## Forum Posts

## 2019

- [Requirements for a new chess engine](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?t=11671) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), December 09, 2019
- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=443) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), December 22, 2019 » Halogen 2.7.3

## 2020 ...

- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=9) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), January 06, 2020 » Halogen 3.0
- [Halogen 4 release](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=12174) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 22, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=264) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), June 22, 2020 » Halogen 4
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=276) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), July 14, 2020 » Halogen 5
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=308) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), August 12, 2020  » Halogen 6
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=390) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), September 22, 2020  » Halogen 7
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=457) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), October 27, 2020 » Halogen 8
- [Halogen questions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75640) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 01, 2020
- [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=487) by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), [CCC](CCC "CCC"), November 11, 2020 » Halogen 8.1
- [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=6) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020 » [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Seer](Seer "Seer")

[Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020

- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")

## External Links

## Chess Engine

- [GitHub - KierenP/Halogen: A c++ chess engine](https://github.com/KierenP/Halogen)
- [Halogen in CCRL Blitz](https://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Halogen&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)

## Misc

- [halogen - Wiktionary](https://en.wiktionary.org/wiki/halogen)
- [Halogen from Wikipedia](https://en.wikipedia.org/wiki/Halogen)
- [Halogen (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Halogen_(disambiguation)>)
- [Halogen lamp from Wikipedia](https://en.wikipedia.org/wiki/Halogen_lamp)
- [Halogen](<https://en.wikipedia.org/wiki/Halogen_(band)>) - The Letter, [Sirens (2006)](https://www.discogs.com/de/Halogen-Sirens/release/10628035), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Packing of [silsesquixane](https://en.wikipedia.org/wiki/Silsesquioxane) molecules in [crystal lattice](https://en.wikipedia.org/wiki/Bravais_lattice) including Br···O [halogen bonds](https://en.wikipedia.org/wiki/Halogen_bond), [Image](https://commons.wikimedia.org/wiki/File:Silsesquixane_halogen_bond.tif) by Wisznu101, May 21,2018, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Release Halogen 2.3 · KierenP/Halogen · GitHub](https://github.com/KierenP/Halogen/releases/tag/v2.3)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Halogen/README.md at master · KierenP/Halogen · GitHub](https://github.com/KierenP/Halogen/blob/master/README.md)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Features based on [Release Halogen 8 · KierenP/Halogen · GitHub](https://github.com/KierenP/Halogen/releases/tag/v8)

**[Up one level](Engines "Engines")**

