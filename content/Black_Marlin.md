---
title: Black Marlin
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Black Marlin**

\[ Black Marlin <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Black Marlin**,

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Doruk Sekercioglu](index.php?title=Doruk_Sekercioglu&action=edit&redlink=1 "Doruk Sekercioglu (page does not exist)"), written in [Rust](Rust "Rust"),
licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), and first released in October 2021 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
[Bitboard](Bitboards "Bitboards") based [move generation](Move_Generation "Move Generation") is done using the [Rust](Rust "Rust") [cozy_chess](Rust#cozy_chess "Rust") library by [Analog Hors](index.php?title=Analog_Hors&action=edit&redlink=1 "Analog Hors (page does not exist)").
The engine features [NNUE](NNUE "NNUE") [evaluation](Evaluation "Evaluation"), and comes with *Marlinflow*, a Neural Network training repository for the engine <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
For optimal NNUE inference on various [X86-64](X86-64 "X86-64") systems using their most advanced [SIMD instruction](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") sets,
[Windows](Windows "Windows") binaries are available supporting [SSSE3](SSSE3 "SSSE3"), [SSE4.2](SSE4#SSE4.2 "SSE4"), [AVX2](AVX2 "AVX2") and [AVX-512](AVX-512 "AVX-512").
Black Marlin **4.0**, released in January 2022, improved due to a larger network, more aggressive [pruning](Pruning "Pruning") and better [move ordering](Move_Ordering "Move Ordering")
<a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Selected Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Lock-less Shared Hash Table](Shared_Hash_Table#Xor "Shared Hash Table")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Singular Extensions](Singular_Extensions "Singular Extensions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [Null Move](Null_Move "Null Move") [Threats](Threat_Move "Threat Move")
  - [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [NNUE](NNUE "NNUE")

## Forum Posts

- [Black Marlin 1.0](https://www.talkchess.com/forum3/viewtopic.php?f=6&t=78516) by [Rebel](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), October 28, 2021
- [Re: New engine releases & news H1 2022](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78884&start=21) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), January 15, 2022
- [Why so many test for Black Marlin and about none for his relatives ?](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79239) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), January 29, 2022

## External Links

## Chess Engine

- [GitHub - dsekercioglu/blackmarlin: WIP Chess Engine](https://github.com/dsekercioglu/blackmarlin)
- [GitHub - dsekercioglu/marlinflow: Neural Network training repository for the Black Marlin chess engine](https://github.com/dsekercioglu/marlinflow)
- [Black Marlin](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Black%20Marlin&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](CCRL "CCRL")

## Misc

- [Black marlin from Wikipedia](https://en.wikipedia.org/wiki/Black_marlin)
- [Black Marlin - Facts and Beyond | Biology Dictionary](https://biologydictionary.net/black-marlin/)
- [Parov Stelar](https://en.wikipedia.org/wiki/Parov_Stelar) - Black Marlin, Voodoo Sonic Part 3, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Image](https://commons.wikimedia.org/wiki/File:Iziko_Black_Marlin.JPG) by Nkansah Rexford, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Release 1.0 · dsekercioglu/blackmarlin · GitHub](https://github.com/dsekercioglu/blackmarlin/releases/tag/1.0)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [GitHub - dsekercioglu/marlinflow: Neural Network training repository for the Black Marlin chess engine](https://github.com/dsekercioglu/marlinflow)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Release 4.0 · dsekercioglu/blackmarlin · GitHub](https://github.com/dsekercioglu/blackmarlin/releases/tag/4.0)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [blackmarlin/README.md at main · dsekercioglu/blackmarlin · GitHub](https://github.com/dsekercioglu/blackmarlin/blob/main/README.md)

**[Up one level](Engines "Engines")**

