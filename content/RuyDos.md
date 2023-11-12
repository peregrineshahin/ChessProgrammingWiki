---
title: RuyDos
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RuyDos**



[ [Noise](https://en.wikipedia.org/wiki/Pink_noise) curves <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**RuyDos**,  

an [UCI](UCI "UCI") compliant chess engine by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") and [José Manuel Morán](Jos%C3%A9_Manuel_Mor%C3%A1n "José Manuel Morán"), written in [C++](Cpp "Cpp"), developed since 2013 <a id="cite-note-2" href="#cite-ref-2">[2]</a> and first published as [open source](Category:Open_Source "Category:Open Source") under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") in June 2017 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Features


### [Board Representation](Board_Representation "Board Representation")


* [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Little-Endian Rank, Big-Endian File Mapping (LERBEF)](Square_Mapping_Considerations "Square Mapping Considerations") (h1=0, a1=7, a8=63)
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")


 [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
 [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
 [Check Extensions](Check_Extensions "Check Extensions")
 [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
* [Quiescence Search](Quiescence_Search "Quiescence Search")


 [Delta Pruning](Delta_Pruning "Delta Pruning")
 [SEE > 0](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
* [Move Ordering](Move_Ordering "Move Ordering")


 [MVV/LVA](MVV-LVA "MVV-LVA")
 [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
 [History Heuristic](History_Heuristic "History Heuristic")
### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")


 [Material Hash Table](Material_Hash_Table "Material Hash Table")
 [Tapered Eval](Tapered_Eval "Tapered Eval") 
 [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Square Control](Square_Control "Square Control")
* [Outposts](Outposts "Outposts")
* [Pawn Structure](Pawn_Structure "Pawn Structure")


 [Backward Pawn](Backward_Pawn "Backward Pawn")
 [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
 [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
* [Mobility](Mobility "Mobility")
* [Tuned](Automated_Tuning "Automated Tuning") with [RuyTune](RuyTune "RuyTune")


### Misc


* [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")


## See also


* [Ruy Lopez](Ruy_Lopez "Ruy Lopez")
* [RuyTune](RuyTune "RuyTune")


## Forum Posts


### 2013 ...


* [Suggestions for a sparring partner](http://www.talkchess.com/forum/viewtopic.php?t=47268) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 19, 2013


### 2017


* [RuyDos publicly available](http://www.talkchess.com/forum/viewtopic.php?t=64138) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 01, 2017
* [RuyDos publicly available](http://www.talkchess.com/forum/viewtopic.php?t=64145) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC") (General Topics), June 01, 2017
* [Testing endgame strength](http://www.talkchess.com/forum/viewtopic.php?t=64356) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 21, 2017 » [Engine Testing](Engine_Testing "Engine Testing")
* [Fathom memory usage](http://www.talkchess.com/forum/viewtopic.php?t=64377) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 22, 2017 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
* [RuyDos with support for syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=64383) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 23, 2017 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [RuyDos 1.0.13 UCI release](http://www.talkchess.com/forum/viewtopic.php?t=64402) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 25, 2017
* [RuyDos 1.0.27 UCI for macOS - includes src](http://www.talkchess.com/forum/viewtopic.php?t=65070) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), September 03, 2017


### 2018


* [RuyDos 1.0.32 UCI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66520) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 06, 2018
* [RuyDos 1.1.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66618) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 17, 2018
* [RuyDos 1.1.6](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67301) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), May 01, 2018
* [Re: easy move?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68692&start=8) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 19, 2018 » [Time Management](Time_Management "Time Management")


## External Links


### Chess Engine


* [alonamaloh / RuyDos — Bitbucket](https://web.archive.org/web/20180713142931/https://bitbucket.org/alonamaloh/ruydos) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [RuyDos](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=RuyDos&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/4](CCRL "CCRL")
* [RuyDos](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=RuyDos&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")


### Misc


* [ruy - Wiktionary](https://en.wiktionary.org/wiki/ruy)
* [Ruy - Wiktionary](https://en.wiktionary.org/wiki/Ruy)
* [Ruy from Wikipedia](https://en.wikipedia.org/wiki/Ruy)
* [Ruido - Wikipedia.es](https://es.wikipedia.org/wiki/Ruido) (Spanish)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a>  Figure showing the noise curves of various [gravitational-wave detectors](https://en.wikipedia.org/wiki/Gravitational-wave_observatory) as a function of frequency together with the characteristic strain of a selection of [astrophysical](https://en.wikipedia.org/wiki/Astrophysics) sources, [Pink noise from Wikipedia](https://en.wikipedia.org/wiki/Pink_noise)  
Christopher Moore, Robert Cole, Christopher Berry (**2014**). *Gravitational-wave sensitivity curves*. [arXiv:1408.0740](https://arxiv.org/abs/1408.0740)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Suggestions for a sparring partner](http://www.talkchess.com/forum/viewtopic.php?t=47268) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 19, 2013
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [RuyDos publicly available](http://www.talkchess.com/forum/viewtopic.php?t=64138) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 01, 2017

**[Up one Level](Engines "Engines")**







 
