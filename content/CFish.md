---
title: CFish
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [Stockfish](Stockfish "Stockfish") * CFish**

\[ [Joachim Beuckelaer](Category:Joachim_Beuckelaer "Category:Joachim Beuckelaer") - Fish Market <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CFish**,

a [port](Stockfish#ports "Stockfish") of Stockfish written in plain [C](C "C") by [Ronald de Man](Ronald_de_Man "Ronald de Man"), first published on [GitHub](https://en.wikipedia.org/wiki/GitHub) in July 2016. Possibly inspired by the [asmFish](AsmFish "AsmFish") project to speed up Stockfish using a programming language closer to the machine, the purpose of CFish is to explore possible optimization issues of C versus [C++](Cpp "Cpp") compilers <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## AVX2 Attacks

Since May 2020, CFish contains experimental [AVX2](AVX2 "AVX2")/[AVX-512](AVX-512 "AVX-512") computational [sliding piece attack](Sliding_Piece_Attacks "Sliding Piece Attacks") code by Okuhara
as memory saving alternative to [Magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. It applies a kind of [branchless classical approach](Classical_Approach#Branchless "Classical Approach").
For instance, the four [positive rays](Classical_Approach#Positive_Rays "Classical Approach") and [negative rays](Classical_Approach#Negative_Rays "Classical Approach") of a [queen](Queen "Queen")
are processed as vector of 4 [bitboards](Bitboards "Bitboards") in one 256-bit ymm register each. Positive and negative rays were intersected with the vector of broadcast [occupancies](Occupancy "Occupancy"),
to get the relevant blockers if any, [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") for positive, and [MS1B](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") for negative rays.
While the positive rays were processed by [BLSMSK](BMI1#BLSMSK "BMI1") aka `((x-1) ^ x)` to clear the ray squares above the LS1B blockers,
the negative rays use a [parallel prefix fill](Parallel_Prefix_Algorithms#Fill_Stuff "Parallel Prefix Algorithms") with three vector right shifts and ors, to clear all ray bits below the MS1B blockers.
The eight ray attack sets were vertically and two times horizontally ored together for the final result.
The conditional compiled AVX-512 version takes advantage of the [\_mm256_lzcnt_epi64](AVX-512#VPLZCNT "AVX-512") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and [\_mm256_ternarylogic_epi64](AVX-512#VPTERNLOG "AVX-512") <a id="cite-note-5" href="#cite-ref-5">[5]</a> intrinsics.
Rook and bishop naturally suffer from less vector utilization, and combine some other well known techniques, i.e. the bishop attack getter processes only positive rays by swapping bytes.

## [NNUE](NNUE "NNUE")

Since August 2020, CFish also provides the [NNUE](NNUE "NNUE") evaluation ported from its C++ base [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") <a id="cite-note-6" href="#cite-ref-6">[6]</a>,
further utilizing [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques").

## See also

- [asmFish](AsmFish "AsmFish")
- [Fat Titz](Fat_Titz "Fat Titz")
- [Portfish](Portfish "Portfish")
- [Rustfish](Rustfish "Rustfish")
- [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")

## Forum Posts

## 2016

- [CFish](http://www.talkchess.com/forum/viewtopic.php?t=61280) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), August 31, 2016
- [Cfish solves the dreaded URI hard problem](http://www.talkchess.com/forum/viewtopic.php?t=61346) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), September 05, 2016
- [cfish for the mac](http://www.talkchess.com/forum/viewtopic.php?t=61394) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), September 11, 2016 » [Macintosh](Macintosh "Macintosh")
- [New CFish Windows binary (from today's code)](http://www.talkchess.com/forum/viewtopic.php?t=61694) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 13, 2016
- [Cfish for the Mac](http://www.talkchess.com/forum/viewtopic.php?t=61743) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 17, 2016
- [Cfish 8 for the MacOS](http://www.talkchess.com/forum/viewtopic.php?t=61975) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 05, 2016

## 2017 ...

- [Cfish update -> macOS exe's for download](http://www.talkchess.com/forum/viewtopic.php?t=65710) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 13, 2017
- [Cfish-54302a... Search of startpos to depth 50](http://www.talkchess.com/forum/viewtopic.php?t=66347) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), January 17, 2018 » [Initial Position](Initial_Position "Initial Position")
- [Cfish 9 is OUT!](http://www.talkchess.com/forum/viewtopic.php?t=66462) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), January 31, 2018
- [Cfish, shiny and new...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70932) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 05, 2019
- [Some NUMA data for Stockfish-dev and Cfish-dev](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71027) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), June 17, 2019 » [NUMA](NUMA "NUMA"), [Stockfish](Stockfish "Stockfish")
- [Bin book adapter?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71311) by Ovyron, [CCC](CCC "CCC"), July 18, 2019 » [PolyGlot](PolyGlot "PolyGlot")

## 2020 ...

- [Where to find CFish 11 Latest exe file](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74369) by Eric Hughes Santiago, [CCC](CCC "CCC"), July 05, 2020

[Re: Where to find CFish 11 Latest exe file](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74369&start=6) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), July 05, 2020

- [Cfish is back!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74402) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), July 07, 2020

[Re: Cfish is back!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74402&start=10) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), July 07, 2020

- [Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 15, 2020 » [NNUE](NNUE "NNUE")

## External Links

- [GitHub - syzygy1/Cfish: C port of Stockfish](https://github.com/syzygy1/Cfish)
- [GitHub - okuhara/Cfish: C port of Stockfish](https://github.com/okuhara/Cfish)
- [Fish Go Deep](Category:Fish_Go_Deep "Category:Fish Go Deep") - The Jazz (2002), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Fish Market](https://commons.wikimedia.org/wiki/File:Joachim_Beuckelaer_-_Vismarkt..JPG) by [Joachim Beuckelaer](Category:Joachim_Beuckelaer "Category:Joachim Beuckelaer"), 16th century, [Bonnefantenmuseum](https://en.wikipedia.org/wiki/Bonnefantenmuseum), [Maastricht](https://en.wikipedia.org/wiki/Maastricht), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Cod from Wikipedia](https://en.wikipedia.org/wiki/Cod)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: CFish](http://www.talkchess.com/forum/viewtopic.php?t=61280&start=9) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), September 01, 2016
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Cfish/avx2-bitboard.h at master · syzygy1/Cfish · GitHub](https://github.com/syzygy1/Cfish/blob/master/src/avx2-bitboard.h)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [\_mm256_lzcnt_epi64](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm256_lzcnt_epi64&expand=5560,5471,3497)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [\_mm256_ternarylogic_epi64](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm256_ternarylogic_epi64&expand=5560,5471,3497,5873)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Cfish/nnue.c at master · syzygy1/Cfish · GitHub](https://github.com/syzygy1/Cfish/blob/master/src/nnue.c)

**[Up one Level](Stockfish "Stockfish")**

