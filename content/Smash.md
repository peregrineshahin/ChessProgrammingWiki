---
title: Smash
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Smash**



 [](http://www.eastleakebadmintonclub.co.uk/fun.html) Smash in [Badminton](https://en.wikipedia.org/wiki/Badminton) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Smash**, (Deep Smash)  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") written by [Maurizio Sambati](index.php?title=Maurizio_Sambati&action=edit&redlink=1 "Maurizio Sambati (page does not exist)") in [C++](Cpp "Cpp"), distributed under the terms of the [General Public License](Free_Software_Foundation#GPL "Free Software Foundation"). Smash played the [CIPS 2004](CIPS_2004 "CIPS 2004"), [CCC 2005](CCC_2005 "CCC 2005"), [CIPS 2005](CIPS_2005 "CIPS 2005"), [CIPS 2007](CIPS_2007 "CIPS 2007") [Italian Computer Chess Championships](Italian_Computer_Chess_Championship "Italian Computer Chess Championship"). 



### Contents


* [1 Description](#description)
* [2 Deep Smash](#deep-smash)
* [3 Photos](#photos)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Smash is a [bitboard](Bitboards "Bitboards") engine and uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") with 256 [line occupancy](Occupancy_of_any_Line "Occupancy of any Line") states to generate [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). While earlier [WinBoard](WinBoard "WinBoard") versions used [MTD(f)](MTD(f) "MTD(f)"), since 1.0 the [Iterative deepening](Iterative_Deepening "Iterative Deepening") framework calls a [principal variation search](Principal_Variation_Search "Principal Variation Search"). [Structured exception handling](Cpp#ExceptionHandling "Cpp") is used to catch terminate- and timer exceptions thrown elsewhere. [Selectivity](Selectivity "Selectivity") is applied with [adaptive null move](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [futility-](Futility_Pruning "Futility Pruning") and [delta pruning](Delta_Pruning "Delta Pruning"), [check-](Check_Extensions "Check Extensions") and [one reply extensions](One_Reply_Extensions "One Reply Extensions"). A [capture](Captures "Captures") entering the [pawn endgame](Pawn_Endgame "Pawn Endgame") is [extended](Capture_Extensions "Capture Extensions") by two plies. Beside moves from the [transposition table](Transposition_Table "Transposition Table"), and [MVV-LVA](MVV-LVA "MVV-LVA") for captures, [move ordering](Move_Ordering "Move Ordering") is controlled by [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"). [Evaluation](Evaluation "Evaluation") determines positional aspects with [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), and considers [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety") and various positional piece terms. 



## Deep Smash


Version 1.0 has been rewritten from scratch. Dubbed Deep Smash - it performs a [parallel search](Parallel_Search "Parallel Search") using [threads](Thread "Thread"), applying [ABDADA](ABDADA "ABDADA") with a [shared transposition table](Shared_Hash_Table "Shared Hash Table") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Photos


 [](http://walkofmind.com/programming/chess/ccc2005.htm) 
[CCC 2005](CCC_2005 "CCC 2005"): [Fabio Cavicchio](Fabio_Cavicchio "Fabio Cavicchio") ([Delfi](Delfi "Delfi")) and [Maurizio Sambati](index.php?title=Maurizio_Sambati&action=edit&redlink=1 "Maurizio Sambati (page does not exist)") - Smash <a id="cite-note-3" href="#cite-ref-3">[3]</a>



## Forum Posts


* [Has anyone ever heard of an engine called Smash?](http://www.talkchess.com/forum/viewtopic.php?t=18585) by bigo, [CCC](CCC "CCC"), December 27, 2007
* [Re: interested in making single proccesor program multi](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=165470&t=18611) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), December 29, 2007
* [Smash (single-CPU/SMP) by Maurizio Sambati](http://www.talkchess.com/forum/viewtopic.php?t=23409) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 31, 2008
* [Last Smash version? (for the RWBC chronology)](http://www.talkchess.com/forum/viewtopic.php?t=60117) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 10, 2016


## External Links


### Chess Engine


* [Deep Smash 1.0.3a - Chess Programs](https://sites.google.com/site/chessphenomenon/smash)
* [Smash « G 6](http://www.g-sei.org/smash/)
* [Smash 1.0.3](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Smash%201.0.3) in [KCEC](KCEC "KCEC")


### Misc


* [smash - Wiktionary](http://en.wiktionary.org/wiki/smash)
* [smashing - Wiktionary](http://en.wiktionary.org/wiki/smashing)
* [smash - Wiktionary.simple](http://simple.wiktionary.org/wiki/smash)
* [The Smashing Pumpkins](Category:The_Smashing_Pumpkins "Category:The Smashing Pumpkins") - [I Am One](https://en.wikipedia.org/wiki/I_Am_One) (1990) , [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> In June 2005, Chinese [Badminton](https://en.wikipedia.org/wiki/Badminton) player, [Fu Haifeng](https://en.wikipedia.org/wiki/Fu_Haifeng) set a world record when he hit a smash at over 208 [miles per hour](https://en.wikipedia.org/wiki/Miles_per_hour), from [East Leake Badminton](http://www.eastleakebadmintonclub.co.uk/fun.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: interested in making single proccesor program multi](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=165470&t=18611) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), December 29, 2007
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Computer Chess Cup 2005](http://walkofmind.com/programming/chess/ccc2005.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")

**[Up one Level](Engines "Engines")**







 
