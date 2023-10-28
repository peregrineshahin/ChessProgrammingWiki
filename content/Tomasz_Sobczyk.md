---
title: Tomasz Sobczyk
---
**[Home](Home "Home") \* [People](People "People") \* Tomasz Sobcyzk**



**Tomasz Sobczyk**, (Sopel97, Sopel)  
a Polish computer scientist involved in recent [Stockfish](Stockfish "Stockfish") development and documentation concerning [NNUE](NNUE "NNUE") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. He introduced new net architectures using the [HalfKA](Stockfish_NNUE#HalfKA "Stockfish NNUE"), HalfKAv2 <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> and HalfKAv2\_hm <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> feature sets, optimized the NNUE inference code for various [SIMD instruction sets](SIMD_and_SWAR_Techniques#SIMD_Instruction_Sets "SIMD and SWAR Techniques") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>, and contributed to [Gary Linscott's](Gary_Linscott "Gary Linscott") [Pytorch NNUE](Gary_Linscott#PyTorch_NNUE "Gary Linscott") project to train Stockfish, mostly working on optimizations which allowed nets to be trained within hours instead of days <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>. He also heavily contributed to the original NNUE trainer and data generator by [Yu Nasu](Yu_Nasu "Yu Nasu"), cleaning up the codebase, updating the data generator, optimizing the trainer, and adding other useful tools <a id="cite-note-12" href="#cite-ref-12">[12]</a> which are now available in the tools branch of the official-stockfish repository <a id="cite-note-13" href="#cite-ref-13">[13]</a>. He also introduced the [Binpack](/index.php?title=Binpack&action=edit&redlink=1 "Binpack (page does not exist)") storage format for training data <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>, comprising of position evaluations from chess games, which utilizes efficient delta encoding, and reduces the sizes of the datasets by 10 to 20 times compared to the previous solutions. His contributions span more than 200 pull requests over multiple repositories <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a> <a id="cite-note-18" href="#cite-ref-18">[18]</a>. He's also an author of a chess engine [Fat Titz](Fat_Titz "Fat Titz"), which is based on [CFish](CFish "CFish") and is a parody of [Fat Fritz](Fat_Fritz "Fat Fritz") <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a>.


## Forum Posts
### 2020 ...


*   [Re: Removing Large Arrays](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73319&start=30) by Sopel, [CCC](/CCC "CCC"), March 12, 2020
*   [Re: Compiler Optimization Question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73638&start=21) by Sopel, [CCC](/CCC "CCC"), April 14, 2020
*   [Re: An actual interesting computer chess read about FF2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76730&start=22) by Sopel, [CCC](/CCC "CCC"), February 28, 2021
*   [Re: It walks like a clone, it quacks like a clone ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76826&start=45) by Sopel, [CCC](/CCC "CCC"), March 14, 2021
*   [Re: larger nets for SF?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77095&start=5) by Sopel, [CCC](/CCC "CCC"), April 16, 2021
*   [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=39) by Sopel, [CCC](/CCC "CCC"), July 01, 2021 » [NNUE Question](/NNUE#KingPlacements "NNUE")
*   [Fat Titz 1.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026) by Sopel, [CCC](/CCC "CCC"), Aug 26, 2021
*   [Fat Titz 1.1 released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78071) by Sopel, [CCC](/CCC "CCC"), Aug 31, 2021

### 2022 ...

*   [Fat Titz 2 released!](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79112) by Tomasz Sobczyk, [CCC](/CCC "CCC"), January 13, 2022

## External Links

*   [Sopel97 (Tomasz Sobczyk) · GitHub](https://github.com/Sopel97)

## References

1.  [↑](#cite_ref-1) [NNUE Guide (nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub)](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md) hosted by [Gary Linscott](/Gary_Linscott "Gary Linscott")
2.  [↑](#cite_ref-2) [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474)
3.  [↑](#cite_ref-3) [nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub - HalfKAv2 feature set](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#halfkav2-feature-set)
4.  [↑](#cite_ref-4) [New NNUE architecture and net by Sopel97 · Pull Request #3646 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3646)
5.  [↑](#cite_ref-5) [nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub - HalfKAv2 feature set](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md#halfkav2_hm-feature-set)
6.  [↑](#cite_ref-6) [Optimization of the affine transformations. by Sopel97 · Pull Request #3203 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3203)
7.  [↑](#cite_ref-7) [AVX-512 optimizations. by Sopel97 · Pull Request #3218 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3218)
8.  [↑](#cite_ref-8) [Optimize and tidy up affine transform code. by Sopel97 · Pull Request #3663 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3663)
9.  [↑](#cite_ref-9) [Defer data preparation to native code. Use sparse input tensors. · Pull Request #1 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/1)
10.  [↑](#cite_ref-10) [A custom kernel for the feature transformer. · Pull Request #96 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pull/96)
11.  [↑](#cite_ref-11) [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](/Connor_McMonigle "Connor McMonigle"), [CCC](/CCC "CCC"), June 17, 2021
12.  [↑](#cite_ref-12) [Pull Requests by Sopel97 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
13.  [↑](#cite_ref-13) [official-stockfish tools branch · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/tree/tools)
14.  [↑](#cite_ref-14) [Sopel97/nnue\_data\_compress · GitHub](https://github.com/Sopel97/nnue_data_compress)
15.  [↑](#cite_ref-15) [Introduce sfen\_format option for gensfen. Experimental support for binpack format in gensfen and learn. · Pull Request #129 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pull/129)
16.  [↑](#cite_ref-16) [Pull Requests by Sopel97 · nodchip/Stockfish · GitHub](https://github.com/nodchip/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
17.  [↑](#cite_ref-17) [Pull Requests by Sopel97 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pulls?q=is%3Apr+author%3ASopel97)
18.  [↑](#cite_ref-18) [Pull Requests by Sopel97 · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/pulls?q=is%3Apr+author%3ASopel97)
19.  [↑](#cite_ref-19) [Sopel97/FatTitz · GitHub](https://github.com/Sopel97/FatTitz)
20.  [↑](#cite_ref-20) [Fat Titz 1.0 released by](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026) Sopel[,](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78026) [CCC](/CCC "CCC"), Aug 26, 2021

**[Up one level](People "People")**







 
