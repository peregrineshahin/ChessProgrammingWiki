---
title: AsmFish
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [Stockfish](Stockfish "Stockfish") * asmFish**

\[ [Istiophorus platypterus](https://en.wikipedia.org/wiki/Indo-Pacific_sailfish), one of the world's fastest fish <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**asmFish**,

a [port](Stockfish#ports "Stockfish") of Stockfish in [x86-64](X86-64 "X86-64") [assembly](Assembly "Assembly") by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), optional using [AVX2](AVX2 "AVX2") and [BMI2](BMI2 "BMI2") instructions, assembled with [FASM](https://en.wikipedia.org/wiki/FASM) to run under [Windows](Windows "Windows") or [UNIX](Unix "Unix")/[Linux](Linux "Linux"), first released in June 2016. The fun project is about to demonstrate how an experienced assembly programmer can optimize a program compared with [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. A few structural optimizations were also applied, such as elimination of [piece lists](Piece-Lists "Piece-Lists") as already tried in Stockfish <a id="cite-note-3" href="#cite-ref-3">[3]</a>, which were later reinstalled due to the slower but stronger **pedantFish** (asmFish with PEDANTIC = 1) with the same node counts as Stockfish, became default <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Critical functions in asmFish were not conform to the x86-64 [ABI](https://en.wikipedia.org/wiki/Application_binary_interface) concerning register usage and [calling convention](https://en.wikipedia.org/wiki/Calling_convention) <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Some less time critical code was ported using GCC generated assembly output, such as [Ronald de Man's](Ronald_de_Man "Ronald de Man") probing code for [Syzygy Bases](Syzygy_Bases "Syzygy Bases"). asmFish further supports [large pages](Memory#HugePages "Memory"), and its [parallel search](Parallel_Search "Parallel Search") is [numa](NUMA "NUMA") aware <a id="cite-note-6" href="#cite-ref-6">[6]</a> .

## Contents

- [1 See also](#see-also)
- [2 Forum Posts](#forum-posts)
  - [2.1 2015](#2015)
  - [2.2 2016](#2016)
  - [2.3 2017](#2017)
  - [2.4 2018](#2018)
  - [2.5 2019](#2019)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## See also

- [CFish](CFish "CFish")

## Forum Posts

## 2015

- [\[for fun\] rewrite of stockfish into asm and question on source](https://groups.google.com/d/msg/fishcooking/HKIYwO6pF-s/-DOONSK5F-IJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 09, 2015

## [Re: \[for fun\] rewrite of stockfish into asm and question on source](https://groups.google.com/d/msg/fishcooking/HKIYwO6pF-s/p9t48jDZBAAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2016 2016

- [new humanistic compile of SF is 108KB](https://groups.google.com/d/msg/fishcooking/z2sd39wrUvw/j5RpSXGmBAAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 28, 2016
- [Re: Speedup and simplicity idea](https://groups.google.com/d/msg/fishcooking/_haJ_5DYm0w/w38-PxBlBgAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 28, 2016
- [ASM Fish for Linux and Windows](http://www.talkchess.com/forum/viewtopic.php?t=60945) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 26, 2016
- [asmFish 44 cores](https://groups.google.com/d/msg/fishcooking/dRYrmi0QTpo/3aSdxHdrEQAJ) by A. Turkoglu, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 28, 2016
- [Scaling of Asmfish with large thread count](http://www.talkchess.com/forum/viewtopic.php?t=61639) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 07, 2016 » [Parallel Search](Parallel_Search "Parallel Search")
- [New asmFish released](http://www.talkchess.com/forum/viewtopic.php?t=61961) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), November 04, 2016

## 2017

- [Reaching Lyudmil Antonov](http://www.talkchess.com/forum/viewtopic.php?t=62906) by Art Ford, [CCC](CCC "CCC"), January 23, 2017
- [Pedant And ASM](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65099) by menniepals, [CCC](CCC "CCC"), September 07, 2017
- [asmfish_macOS_11082017](http://www.talkchess.com/forum/viewtopic.php?t=65671) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 08, 2017
- [asmfishX - macOS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65797) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 23, 2017

## 2018

- [asmFish update - all flavors of OS](http://www.talkchess.com/forum/viewtopic.php?t=66373) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), January 20, 2018

[Re: asmFish update - all flavors of OS](http://www.talkchess.com/forum/viewtopic.php?t=66373&start=14) by T. Poppins, [CCC](CCC "CCC"), January 23, 2018

- [New asmfish](http://www.talkchess.com/forum/viewtopic.php?t=66570) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), February 12, 2018
- [Asmfish further development](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68546) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), October 01, 2018
- [Re: piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364&start=12) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 26, 2018 » [Piece-Lists](Piece-Lists "Piece-Lists")

## 2019

- [asmFish](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70614) by [Stephen Ham](index.php?title=Stephen_Ham&action=edit&redlink=1 "Stephen Ham (page does not exist)"), [CCC](CCC "CCC"), April 28, 2019

[Re: asmFish](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70614&start=13) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), May 05, 2019

- [in case you had not noticed ..](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70944) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), June 07, 2019

## External Links

## Chess Engine

- [GitHub - lantonov/asmFish Wiki](https://github.com/lantonov/asmFish/wiki)
- [GitHub - lantonov/asmFish](https://github.com/lantonov/asmFish) - A continuation of the nice project asmFish by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)") (07.08.2019), hosted by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov")
- [GitHub - Counterply/asmFish at asmFish-CounterPly](https://github.com/Counterply/asmFish/tree/asmFish-CounterPly) hosted by [Justin Dehorty](index.php?title=Justin_Dehorty&action=edit&redlink=1 "Justin Dehorty (page does not exist)")

## Misc

- [Yes](Category:Yes "Category:Yes") - [The Fish (Schindleria Praematurus)](<https://en.wikipedia.org/wiki/Fragile_(Yes_album)#Songs>), [Live at Montreux 2003](https://en.wikipedia.org/wiki/Live_at_Montreux_2003) [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Istiophorus platypterus, [Image](https://commons.wikimedia.org/wiki/File:Istiophorus_platypterus.jpg) by [Citron](https://commons.wikimedia.org/wiki/User:Citron), March 2010, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Sailfish from Wikipedia](https://en.wikipedia.org/wiki/Sailfish), [Indo-Pacific sailfish from Wikipedia](https://en.wikipedia.org/wiki/Indo-Pacific_sailfish)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: \[for fun\] rewrite of stockfish into asm and question on source](https://groups.google.com/d/msg/fishcooking/HKIYwO6pF-s/p9t48jDZBAAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2016
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [removal of piece lists](https://groups.google.com/d/msg/fishcooking/aJEf-_SmpWY/TARC-1aPGzYJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 11, 2014
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364&start=12) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 26, 2018
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Agner Fog's manuals](http://www.agner.org/optimize/#manuals)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [lets get the ball moving down the field on numa awareness](https://groups.google.com/d/msg/fishcooking/ezt6MrAuXqs/qIR2HEciEgAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 30, 2016

**[Up one Level](Stockfish "Stockfish")**

