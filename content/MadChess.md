---
title: MadChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MadChess**



[ Me Worry? <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**MadChess**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Erik Madsen](Erik_Madsen "Erik Madsen"), written in [C#](C_sharp "C sharp") to run under the [Windows](Windows "Windows") [.NET framework](https://en.wikipedia.org/wiki/.NET_Framework). It was first released under the [GNU General Public License Version 3](Free_Software_Foundation#GPL "Free Software Foundation") as successor of Erik's former C# engine [RumbleMinze](RumbleMinze "RumbleMinze") in October 2012 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and features adjustable [playing strength](Playing_Strength "Playing Strength") with improved algorithms since MadChess **1.4** <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>. MadChess **2.1**, released in February 2017 is using [.NET Core](https://en.wikipedia.org/wiki/.NET_Framework#.NET_Core), [Microsoft’s](Microsoft "Microsoft") [cross-platform](https://en.wikipedia.org/wiki/Cross-platform) [free and open-source](https://en.wikipedia.org/wiki/Free_and_open-source_software) managed software framework to support not only [Windows](Windows "Windows"), but [Linux](Linux "Linux"), and [Mac](Mac_OS "Mac OS") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### Move Generation


MadChess applies an incremental [move generation](Move_Generation "Move Generation"), using the C# [yield statement](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29#C.23) <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a> using [incrementally updated](Incremental_Updates "Incremental Updates") [list of attackers](Piece-Lists "Piece-Lists") for any [rank](Ranks "Ranks"), [file](Files "Files"), [diagonal](Diagonals "Diagonals"), or [anti-diagonal](Anti-Diagonals "Anti-Diagonals"). 



### Search


MadChess performs a [principal variation search](Principal_Variation_Search "Principal Variation Search") along with [transposition table](Transposition_Table "Transposition Table"), [killer](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [late move reductions](Late_Move_Reductions "Late Move Reductions") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration](Aspiration_Windows "Aspiration Windows"). It eliminates all [reductions](Reductions "Reductions") and lazy evaluation along the principal variation.



### Evaluation


The [evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") with respect to bounds, and otherwise uses a [tapered evaluation](Tapered_Eval "Tapered Eval") on [game phase](Game_Phases "Game Phases") between speculative computed [middlegame](Middlegame "Middlegame") and [endgame](Endgame "Endgame") [scores](Score "Score"), considering [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure"), and [king safety](King_Safety "King Safety") and various [piece evaluation](Evaluation_of_Pieces "Evaluation of Pieces") terms. 



## See also


* [Madness Schach](index.php?title=Madness_Schach&action=edit&redlink=1 "Madness Schach (page does not exist)")
* [Matchess](Matchess "Matchess")
* [RumbleMinze](RumbleMinze "RumbleMinze")


## Forum Posts


### 2012


* [MadChess 1.0 Released (C# .NET Engine)](http://www.talkchess.com/forum/viewtopic.php?t=45723) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 25, 2012
* [Score Inaccuracy: An Engine Weakening Algorithm](http://www.talkchess.com/forum/viewtopic.php?t=45795) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 31, 2012 » [Playing Strength](Playing_Strength "Playing Strength")


### 2013


* [MadChess 1.1 Released](http://www.talkchess.com/forum/viewtopic.php?t=46790) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), January 06, 2013
* [MadChess 1.2 Released](http://www.talkchess.com/forum/viewtopic.php?t=47457) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), March 09, 2013
* [MadChess 1.3 Released](http://www.talkchess.com/forum/viewtopic.php?t=49497) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), September 28, 2013


### 2014


* [MadChess UCI\_LimitStrength Algorithm](http://www.talkchess.com/forum/viewtopic.php?t=51973) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), April 12, 2014 » [UCI](UCI "UCI"), [Playing Strength](Playing_Strength "Playing Strength")
* [MadChess 1.4 Released](http://www.talkchess.com/forum/viewtopic.php?t=51974) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), April 12, 2014
* [MadChess With Odds Versus Elite Engines](http://www.talkchess.com/forum/viewtopic.php?t=53654) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), September 11, 2014
* [MadChess 2.0 Development](http://www.talkchess.com/forum/viewtopic.php?t=54320) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), November 12, 2014


### 2015 ...


* [MadChess 2.0 Released](http://www.talkchess.com/forum/viewtopic.php?t=57920) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 12, 2015
* [MadChess 2.1 Released - Supports Windows, Linux, Mac](http://www.talkchess.com/forum/viewtopic.php?t=63248) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), February 23, 2017
* [MadChess 2.2 Released](http://www.talkchess.com/forum/viewtopic.php?t=64504) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), July 04, 2017
* [MadChess 3.0 Beta](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68759) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 29, 2018
* [Particle Swarm Optimization Code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69035) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), November 24, 2018 » [Automated Tuning](Automated_Tuning "Automated Tuning")


### 2020 ...


* [Re: MadChess 3.0 Beta](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68759&start=19) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), July 23, 2020
* [Engine Crash Detective Story](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74931) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), August 29, 2020 » [Debugging](Debugging "Debugging")
* [Are Aspiration Windows Worthless?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76115) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), December 20, 2020 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [MadChess 3.0 Released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77125) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), April 19, 2021


## Blog Posts


* [MadChess 3.0 Beta 5c5d4fc (Piece Mobility)](https://www.madchess.net/2020/02/01/madchess-3-0-beta-5c5d4fc-piece-mobility/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), February 1, 2020 » [Mobility](Mobility "Mobility")
* [MadChess 3.0 Beta 6f3d17a (Late Move Pruning)](https://www.madchess.net/2020/02/08/madchess-3-0-beta-4478cb8-late-move-pruning/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), February 8, 2020 » [LMP](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [MadChess 3.0 Beta bef88d5 (Tweak Search, Tune Eval)](https://www.madchess.net/2020/07/23/madchess-3-0-beta-bef88d5-tweak-search-tune-eval/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), July 23, 2020
* [MadChess 3.0 Beta 2d855ec (Crash Bug) – MadChess](https://www.madchess.net/2020/08/29/madchess-3-0-beta-2d855ec-crash-bug/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), August 29, 2020 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [MadChess 3.0 Beta 4b7963b (Remove Aspiration Windows) – MadChess](https://www.madchess.net/2020/12/20/madchess-3-0-beta-4b7963b-remove-aspiration-windows/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), December 20, 2020 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows") <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [MadChess 3.0 Released – MadChess](https://www.madchess.net/2021/04/19/madchess-3-0-released/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), April 19, 2021


## External Links


### Chess Engine


* [MadChess](https://www.madchess.net/)


 [MadChess - User Guide](https://www.madchess.net/page/User-Guide)
* [MadChess](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=MadChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [MAD from Wikipedia](https://en.wikipedia.org/wiki/MAD)
* [Mad (magazine) from Wikipedia](https://en.wikipedia.org/wiki/Mad_%28magazine%29)
* [Insanity from Wikipedia](https://en.wikipedia.org/wiki/Insanity)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A postcard with the [public domain](https://en.wikipedia.org/wiki/Public_domain) "[me worry?](http://en.wiktionary.org/wiki/what_me_worry)" face that later inspired [Mad magazine's](https://en.wikipedia.org/wiki/Mad_%28magazine%29) [Alfred E. Neuman](https://en.wikipedia.org/wiki/Alfred_E._Neuman), ca. 1910s, [Alfred E. Neuman from Wikipedia](https://en.wikipedia.org/wiki/Alfred_E._Neuman)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [MadChess 1.0 Released (C# .NET Engine)](http://www.talkchess.com/forum/viewtopic.php?t=45723) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 25, 2012
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [MadChess UCI\_LimitStrength Algorithm](http://www.talkchess.com/forum/viewtopic.php?t=51973) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), April 12, 2014
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [MadChess - User Guide](http://www.madchess.net/page/User-Guide)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [MadChess 2.1 Released – MadChess](http://www.madchess.net/2017/02/22/madchess-2-1-released/), February 22, 2017
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [MadChess 2.1 Released - Supports Windows, Linux, Mac](http://www.talkchess.com/forum/viewtopic.php?t=63248) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), February 23, 2017
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Question About CPP-C#, Performance, and Square Representation](http://talkchess.com/forum/viewtopic.php?p=485936#485936) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), October 03, 2012
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [yield - MSDN C# Reference](http://msdn.microsoft.com/en-us/library/9k7k7cf0.aspx)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Behind the scenes of the C# yield keyword | Struggles](http://startbigthinksmall.wordpress.com/2008/06/09/behind-the-scenes-of-the-c-yield-keyword/) by [Lars Corneliussen](http://startbigthinksmall.wordpress.com/), June 9, 2008
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Generator (computer programming) from Wikipedia](https://en.wikipedia.org/wiki/Generator_%28computer_programming%29)
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Coroutine from Wikipedia](https://en.wikipedia.org/wiki/Coroutine)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Engine Crash Detective Story](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74931) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), August 29, 2020
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Are Aspiration Windows Worthless?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76115) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), December 20, 2020 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")

**[Up one level](Engines "Engines")**[[Category:Mac]







 
