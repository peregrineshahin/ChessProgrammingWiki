---
title: Gull
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gull**

[](File:ScheveningenGulls.JPG) Scheveningen Gulls <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gull**, (GullChess)

an [UCI](UCI "UCI") compliant [open source engine](Category:Open_Source "Category:Open Source") in the [public domain](https://en.wikipedia.org/wiki/Public_domain) by [ThinkingALot](ThinkingALot "ThinkingALot") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, inspired by ideas and code from other open source engines, notably from [IvanHoe](IvanHoe "IvanHoe") of the [Ippolit](Ippolit "Ippolit") family of programs, and from [Strelka](Strelka "Strelka"), whose authors are suspected of [reverse engineering](https://en.wikipedia.org/wiki/Reverse_engineering) [Rybka](Rybka "Rybka"), to examine and use her ideas. [Ron Murawski's](Ron_Murawski "Ron Murawski") Computer-Chess Wiki mentions GullChess as IvanHoe derivative <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The further socialization of concrete implementations with disputed origin in the public domain, as already started with Ippolit, remains a highly controversial topic.

## Contents

- [1 Description](#description)
- [2 Releases & Forks](#releases-.26-forks)
  - [2.1 Gull 2.1](#gull-2.1)
  - [2.2 Gull 2.8 beta](#gull-2.8-beta)
  - [2.3 Gull 3](#gull-3)
  - [2.4 LazyGull](#lazygull)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
  - [4.1 2010 ...](#2010-...)
  - [4.2 2015 ...](#2015-...)
- [5 External Links](#external-links)
  - [5.1 Source Code Repositories](#source-code-repositories)
  - [5.2 Rating](#rating)
  - [5.3 Misc](#misc)
- [6 References](#references)

## Description

Gull applies [magic bitboards](Magic_Bitboards "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), a [material table](Material_Tables "Material Tables") indexing scheme with disjoint light and dark bishops, [PVS](Principal_Variation_Search "Principal Variation Search") with [aspiration windows](Aspiration_Windows "Aspiration Windows"), and a [parallel search](Parallel_Search "Parallel Search") based on [processes](Process "Process"). Version 1.2 is written in compact and neat [C++](Cpp "Cpp") code and consists of only one single source file. It features [generic](Generic_Programming "Generic Programming") function templates in [recursive](Recursion "Recursion") search routines as well in various functions called by search, i.e. for [move generation](Move_Generation "Move Generation"), with [side to move](Side_to_move "Side to move") and [hash-move](Hash_Move "Hash Move") exclusion for [singular extensions](Singular_Extensions "Singular Extensions") as boolean template parameters, delegating conditions on these to compile-time.

## Releases & Forks

## Gull 2.1

Gull **2.1**, released in June 2013, has [evaluation](Evaluation "Evaluation") weights optimized with the use of [automated tuning](Automated_Tuning "Automated Tuning") (source code included). Gull's 2.1 evaluation is no longer almost identical to that of IvanHoe. Further, it features some minor search, [time management](Time_Management "Time Management") and [SMP](Parallel_Search "Parallel Search") efficiency enhancements <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Gull 2.8 beta

Gull **2.8 beta**, released in January 2014 and competing [TCEC Season 6](TCEC_Season_6 "TCEC Season 6"), comes with minor search tweaks but a full evaluation rewrite, being back an original engine <a id="cite-note-5" href="#cite-ref-5">[5]</a>. A [BMI2](BMI2 "BMI2") build provides a small speedup on [Haswell architecture](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) due to the replacement of [magic bitboards](Magic_Bitboards "Magic Bitboards") by [PEXT bitboards](BMI2#PEXTBitboards "BMI2").

## Gull 3

Gull **3**, released April 17, 2014, with further [optimization](Automated_Tuning "Automated Tuning") of evaluation weights and a rewritten [SMP search](Parallel_Search "Parallel Search"), features nonlinear [king shelter evaluation](King_Safety#PawnShield "King Safety") and more [endgame knowledge](Endgame "Endgame"). [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli") implemented a [Linux](Linux "Linux") port <a id="cite-note-6" href="#cite-ref-6">[6]</a> and [Syzygy Bases](Syzygy_Bases "Syzygy Bases") support, introducing [Fathom](Syzygy_Bases#Fathom "Syzygy Bases") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, while [Michael Byrne](Michael_Byrne "Michael Byrne") worked on a [Mac OS](Mac_OS "Mac OS") port <a id="cite-note-8" href="#cite-ref-8">[8]</a> dubbed **Hawkeye** <a id="cite-note-9" href="#cite-ref-9">[9]</a>, [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)") introduced his Gull 3 derivative [Roc](Roc "Roc"), and [Norman Schmidt](Norman_Schmidt "Norman Schmidt") **SeaGull** also based on Gull 3 <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## LazyGull

**LazyGull** is a free UCI chess engine under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") derived from Gull 3 by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli") <a id="cite-note-11" href="#cite-ref-11">[11]</a>. LazyGull features [Syzygy Bases](Syzygy_Bases "Syzygy Bases") support via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases"), [Lazy SMP](Lazy_SMP "Lazy SMP"), and [PDEP bitboards](BMI2#PDEPBitboards "BMI2") for modern [x86-64](X86-64 "X86-64") CPUs, and is portable to [Windows](Windows "Windows"), [Linux](Linux "Linux") and [MacOSX](Mac_OS "Mac OS") <a id="cite-note-12" href="#cite-ref-12">[12]</a>.

## See also

- [Bird](Category:Bird "Category:Bird")

## Forum Posts

## 2010 ...

- [Проект "Чайка"](http://immortalchess.net/forum/showthread.php?t=2354) by [ThinkingALot](ThinkingALot "ThinkingALot"), [immortalchess](Computer_Chess_Forums "Computer Chess Forums"), June 07, 2010, [translated](http://translate.google.com/translate?sl=ru&tl=en&js=n&prev=_t&hl=en&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fimmortalchess.net%2Fforum%2Findex.php) by [Google Translate](https://en.wikipedia.org/wiki/Google_Translate)
- [GullChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=51022) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 09, 2010
- [gull chess](http://www.open-chess.org/viewtopic.php?f=7&t=109) by Karger, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 12, 2010

[Re: gull chess](http://www.open-chess.org/viewtopic.php?f=7&t=109&p=724#p724) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 13, 2010 » [Gaviota](Gaviota "Gaviota")
[Re: gull chess](http://www.open-chess.org/viewtopic.php?f=7&t=109&start=120#p18910) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 17, 2013 (Gull 2.1)
[Re: gull chess](http://www.open-chess.org/viewtopic.php?f=7&t=109&start=150#p20221) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 26, 2014 (Gull 2.8 beta & Gull 2.9 alpha)

- [GullChess 2.1](http://www.talkchess.com/forum/viewtopic.php?t=48325) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 18, 2013
- [DTS-like SMP](http://www.open-chess.org/viewtopic.php?f=5&t=2378) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2013 » [Parallel Search](Parallel_Search "Parallel Search")
- [Re: Gull](http://immortalchess.net/forum/showpost.php?p=464718&postcount=326) by [ThinkingALot](ThinkingALot "ThinkingALot"), [immortalchess](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2014

## 2015 ...

- [Gull's endgame knowledge](https://groups.google.com/d/msg/fishcooking/Xh8p8KXGrso/aguB__krDAAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 16, 2015 » [Rook Endgame](Rook_Endgame "Rook Endgame"), [Stockfish](Stockfish "Stockfish")
- [Gull 3 (Linux port) released](http://www.talkchess.com/forum/viewtopic.php?t=58071) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), October 28, 2015
- [Gull 3 x64 Mac Results](http://www.talkchess.com/forum/viewtopic.php?t=58096) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 30, 2015
- [Gull 3 Linux+Syzygy and Fathom released](http://www.talkchess.com/forum/viewtopic.php?t=58299) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), November 20, 2015 » [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")

**2016**

- [Gull 3.0.1 available, takes advantage of hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=59002) by [Dmitri Gusev](Dmitri_Gusev "Dmitri Gusev"), [CCC](CCC "CCC"), January 21, 2016
- [Gull 3.0 Syzygy in GitHub](http://www.talkchess.com/forum/viewtopic.php?t=60217) by [Jose Mº Velasco](index.php?title=Jose_M%C2%BA_Velasco&action=edit&redlink=1 "Jose Mº Velasco (page does not exist)"), [CCC](CCC "CCC"), May 19, 2016
- [Gull 3 x64](http://www.talkchess.com/forum/viewtopic.php?t=60663) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 01, 2016
- [Hawkeye 1.01](http://www.talkchess.com/forum/viewtopic.php?t=60695) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 05, 2016
- [Hawkeye 1.01 Released](http://www.talkchess.com/forum/viewtopic.php?t=60725) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 07, 2016
- [Hawkeye is now on Github](http://www.talkchess.com/forum/viewtopic.php?t=60772) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 10, 2016
- [Hawkeye 1.02 Released](http://www.talkchess.com/forum/viewtopic.php?t=60776) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 11, 2016
- [HAwkeye 1.03 Released](http://www.talkchess.com/forum/viewtopic.php?t=60831) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 16, 2016
- [Future of Gull](http://www.talkchess.com/forum/viewtopic.php?t=61195) by [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)"), [CCC](CCC "CCC"), August 23, 2016 <a id="cite-note-13" href="#cite-ref-13">[13]</a>

**2017**

- [New engine "Roc"](http://www.talkchess.com/forum/viewtopic.php?t=62856) by [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)"), [CCC](CCC "CCC"), January 18, 2017
- [Open-source improvements released](http://www.talkchess.com/forum/viewtopic.php?t=64418) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), June 26, 2017
- [question: Gull 3 syzygy](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65727) by kasinp, [CCC](CCC "CCC"), November 14, 201

## External Links

## Source Code Repositories

- [SourceForge.net: GullChess - Project Web Hosting - Open Source Software](http://gullchess.sourceforge.net/) by [ThinkingALot](ThinkingALot "ThinkingALot")
- [GullChess | Free software downloads at SourceForge.net](http://sourceforge.net/projects/gullchess/)
- [GitHub - Velmarin/Chess-Gull-Syzygy: Chess uci engine with support Syzygy tablebassses](https://github.com/Velmarin/Chess-Gull-Syzygy) by [Jose Mº Velasco](index.php?title=Jose_M%C2%BA_Velasco&action=edit&redlink=1 "Jose Mº Velasco (page does not exist)")
- [GitHub - MichaelB7/Hawkeye: UCI Chess Engine based on Gull](https://github.com/MichaelB7/Hawkeye) by [Michael Byrne](Michael_Byrne "Michael Byrne")
- [hyer / SonsOfTheBird / source / Slizzard — Bitbucket](https://bitbucket.org/hyer/sonsofthebird/src/052b62b0c78d11889379d5909bbe617b70274076/Slizzard/?at=default) by [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)") <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [GitHub - TomHyer/Roc: C++ chess engine derived from Gull 3](https://github.com/TomHyer/Roc) by [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)") » [Roc](Roc "Roc")
- [GitHub - basil00/Gull: Gull chess (Linux/Mac port) - The LazyGull Chess Engine](https://github.com/basil00/Gull) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli")
- [GitHub - FireFather/seagull: chess engine based on Gull 3](https://github.com/FireFather/seagull) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt")

## Rating

- [Gull 1.2 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Gull%201.2%2064-bit#Gull_1_2_64-bit) in [CCRL 40/15](CCRL "CCRL")
- [Gull 3 64-bit 4CPU](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Gull%203%2064-bit%204CPU#Gull_3_64-bit_4CPU) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Gull (Seagull) from Wikipedia](https://en.wikipedia.org/wiki/Gull)
- [The Birds (story) from Wikipedia](https://en.wikipedia.org/wiki/The_Birds_%28story%29)
- [The Birds (film) from Wikipedia](https://en.wikipedia.org/wiki/The_Birds_%28film%29)
- [Terumasa Hino](Category:Terumasa_Hino "Category:Terumasa Hino") ‎– [Hip Seagull](http://www.ticro.com/search/T00003748/no_sub/detail/) (1978), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat. [Kosuke Mine](https://en.wikipedia.org/wiki/Kosuke_Mine), [Mikio Masuda](https://de.wikipedia.org/wiki/Mikio_Masuda), [John Scofield](Category:John_Scofield "Category:John Scofield"), [Clint Houston](https://en.wikipedia.org/wiki/Clint_Houston), [Motohiko Hino](https://en.wikipedia.org/wiki/Motohiko_Hino), [James Mtume](Category:James_Mtume "Category:James Mtume")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Gulls at the beach of [Scheveningen](https://en.wikipedia.org/wiki/Scheveningen) [Kurhaus](https://en.wikipedia.org/wiki/Kurhaus_of_Scheveningen), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), December 26, 2015
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chess engine from Wikiepdia](https://en.wikipedia.org/wiki/Chess_engine)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:chess_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: gull chess](http://www.open-chess.org/viewtopic.php?f=7&t=109&start=120#p18910) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 17, 2013 (Gull 2.1)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Gull 2.8 beta.zip/Gull 2.8 beta/readme.txt
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Gull 3 (Linux port) released](http://www.talkchess.com/forum/viewtopic.php?t=58071) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), October 28, 2015
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Gull 3 Linux+Syzygy and Fathom released](http://www.talkchess.com/forum/viewtopic.php?t=58299) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), November 20, 2015
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Gull 3 x64 Mac Results](http://www.talkchess.com/forum/viewtopic.php?t=58096) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 30, 2015
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Hawkeye 1.01](http://www.talkchess.com/forum/viewtopic.php?t=60695) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 05, 2016
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [GitHub - FireFather/seagull: chess engine based on Gull 3](https://github.com/FireFather/seagull) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt")
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [GitHub - basil00/Gull: Gull chess (Linux/Mac port) - The LazyGull Chess Engine](https://github.com/basil00/Gull)
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Gull/README.md at master · basil00/Gull · GitHub](https://github.com/basil00/Gull/blob/master/README.md)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [hyer / SonsOfTheBird / source / Slizzard — Bitbucket](https://bitbucket.org/hyer/sonsofthebird/src/052b62b0c78d11889379d5909bbe617b70274076/Slizzard/?at=default)
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a>  [Future of Gull](http://www.talkchess.com/forum/viewtopic.php?t=61195) by [Tom Hyer](index.php?title=Tom_Hyer&action=edit&redlink=1 "Tom Hyer (page does not exist)"), [CCC](CCC "CCC"), August 23, 2016

**[Up one Level](Engines "Engines")**

