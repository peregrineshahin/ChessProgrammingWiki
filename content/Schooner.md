---
title: Schooner
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Schooner**



 [](https://commons.wikimedia.org/wiki/File:Eendracht_II.JPG) [Schooner](https://en.wikipedia.org/wiki/Schooner) off [Hoek van Holland](https://en.wikipedia.org/wiki/Hook_of_Holland) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Schooner**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") (CECP) compliant chess engine by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour") running under [Windows](Windows "Windows"). The hobby project already started in the late 70s <a id="cite-note-2" href="#cite-ref-2">[2]</a> and was revived using [Magic Bitboards](Magic_Bitboards "Magic Bitboards") in 2015. 



### Contents


* [1 Schooner 2](#schooner-2)
* [2 Features](#features)
	+ [2.1 Board Representation](#board-representation)
	+ [2.2 Search](#search)
	+ [2.3 Evaluation](#evaluation)
	+ [2.4 Misc](#misc)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
	+ [4.1 2015](#2015)
	+ [4.2 2016 ...](#2016-...)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc-2)
* [6 References](#references)






Schooner **2** (Schooner II), released in October 2018 was a complete re-write in [C](C "C") with a huge performance boost of over 500 [CCRL 40/4](CCRL "CCRL") rating points <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
[Staged move generation](Move_Generation#Staged "Move Generation") and a simpler [evaluation](Evaluation "Evaluation") inspired by [Xiphos](Xiphos "Xiphos") <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
a lot of [testing](Engine_Testing "Engine Testing") and [tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and 
using [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) v7.2.0 were explicitly mentioned as a possible explanation for that improvement <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 
Schooner 2 further supports a subset of [UCI](UCI "UCI") to automatically play games without [pondering](Pondering "Pondering").



## Features


<a id="cite-note-7" href="#cite-ref-7">[7]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")
* [SSE4](SSE4 "SSE4") [Population Count](Population_Count "Population Count")
* [Staged Move Generation](Move_Generation#Staged "Move Generation") (Schooner 2)


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP") using [Threads](Thread "Thread") and [Shared Hash Table](Shared_Hash_Table "Shared Hash Table") (Schooner 2)
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* Floating [Reductions](Reductions "Reductions"), [LMR](Late_Move_Reductions "Late Move Reductions") and [Pruning](Pruning "Pruning") <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") (Hash Refutation) <a id="cite-note-9" href="#cite-ref-9">[9]</a>


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Mobility](Mobility "Mobility")
* [Space](Space "Space") <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Pawn Structure](Pawn_Structure "Pawn Structure")


 [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [King Safety](King_Safety "King Safety")


### Misc


* [Pondering](Pondering "Pondering")
* [PolyGlot](PolyGlot "PolyGlot") [Book](Opening_Book "Opening Book") (Schooner 2)


## See also


* [Ghost](Ghost "Ghost")


## Forum Posts


### 2015


* [Schooner Version 1.4](http://www.talkchess.com/forum/viewtopic.php?t=57311) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 19, 2015
* [Hash Refutation](http://www.talkchess.com/forum/viewtopic.php?t=57374) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 24, 2015
* [Profiling Comparison](http://www.talkchess.com/forum/viewtopic.php?t=57532) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), September 06, 2015


### 2016 ...


* [Schooner Version 1.5](http://www.talkchess.com/forum/viewtopic.php?t=60135) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), May 11, 2016
* [Schooner Version 1.7](http://www.talkchess.com/forum/viewtopic.php?t=63818) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), April 25, 2017
* [Schooner Version 1.8](http://www.talkchess.com/forum/viewtopic.php?t=66336) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), January 15, 2018
* [Schooner 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68775) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), October 30, 2018
* [Schooner's Test Positions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68810) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 02, 2018
* [Schooner Version 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71175) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), July 03, 2019
* [Schooner Version 2.2 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72590) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), December 16, 2019


## External Links


### Chess Engine


* [Schooner Chess](https://sites.google.com/site/schoonerchess/home)
* [GitHub - schooner64-chess/Schooner-Chess: engines and books](https://github.com/schooner64-chess/Schooner-Chess) (1.4.1)
* [Schooner](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Schooner&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/4](CCRL "CCRL")


### Misc


* [Schooner from Wikipedia](https://en.wikipedia.org/wiki/Schooner)
* [Schooner (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Schooner_(disambiguation))
* [schooner - Wiktionary](https://en.wiktionary.org/wiki/schooner)
* [Schooner Olad](http://www.maineschooners.com/): first sail of 2013 out of [Camden](https://en.wikipedia.org/wiki/Camden,_Maine) Harbor, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 Music: [Crosby, Stills & Nash](https://en.wikipedia.org/wiki/Crosby,_Stills,_Nash_%26_Young) - [Wooden Ships](https://en.wikipedia.org/wiki/Wooden_Ships)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [Eendracht](https://en.wikipedia.org/wiki/Eendracht_(1989_ship)) in the [North Sea](https://en.wikipedia.org/wiki/North_Sea) on the way to [Rotterdam](https://en.wikipedia.org/wiki/Rotterdam), Photo taken from [Hoek van Holland](https://en.wikipedia.org/wiki/Hook_of_Holland) beach, July 05, 2017 15:07 [CEST](https://en.wikipedia.org/wiki/Central_European_Summer_Time) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), bike tour during [WCCC 2017](WCCC_2017 "WCCC 2017")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Features - Schooner Chess](https://sites.google.com/site/schoonerchess/features)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Schooner](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Schooner&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/4](CCRL "CCRL")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The Xiphos Material Evaluator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68842) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 05, 2018
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Schooner 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68775&start=32) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 02, 2018
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Schooner 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68775&start=22) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), October 31, 2018
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Features - Schooner Chess](https://sites.google.com/site/schoonerchess/features)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Floating Move Reduction](http://www.talkchess.com/forum/viewtopic.php?t=61425) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), September 14, 2016
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Hash Refutation](http://www.talkchess.com/forum/viewtopic.php?t=57374) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 24, 2015
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Ee: Calculating space](http://www.talkchess.com/forum/viewtopic.php?t=61064&start=5) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 09, 2016

**[Up one Level](Engines "Engines")**







 
