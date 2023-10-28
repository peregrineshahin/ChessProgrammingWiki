---
title: NGplay
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* NG-play**


**NG-play**,  

a relatively simple, [open source chess engine](Category:Open_Source "Category:Open Source") by [George Georgopoulos](George_Georgopoulos "George Georgopoulos"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and written in [C](C "C"). 
NG-play uses a [10x12 board](10x12_Board "10x12 Board"), and performs a [negamax](Negamax "Negamax") [alpha-beta search](Alpha-Beta "Alpha-Beta") with [iterative deepening](Iterative_Deepening "Iterative Deepening"), [LMR](Late_Move_Reductions "Late Move Reductions"), [futility pruning](Futility_Pruning "Futility Pruning") and [null move pruning](Null_Move_Pruning "Null Move Pruning"). 
[Evaluation](Evaluation "Evaluation") considers [material](Material "Material") and [mobility](Mobility "Mobility") in a first pass, and focuses on [king safety](King_Safety "King Safety") in the [middlegame](Middlegame "Middlegame"), as well as [passed pawn](Passed_Pawn "Passed Pawn") evaluation in a second pass <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The engine was written from scratch, the [XBoard](XBoard "XBoard") and [opening book](Opening_Book "Opening Book") code inspired by [Tom Kerrigan's](Tom_Kerrigan "Tom Kerrigan") [TSCP](TSCP "TSCP"). [Bruce Moreland](Bruce_Moreland "Bruce Moreland") is credited since his programming topics site <a id="cite-note-2" href="#cite-ref-2">[2]</a> helped in writing the code to [collect](Principal_Variation#CollectionDuringSearch "Principal Variation") the [principal variation](Principal_Variation "Principal Variation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Contents


* [1 Development History](#development-history)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






* From version 8.0, search algorithm changed to [NegaScout](NegaScout "NegaScout")
* From version 9.0, a simple [transposition table](Transposition_Table "Transposition Table") scheme is used


## Forum Posts


* [A not very recent Greek chess engine](http://www.talkchess.com/forum/viewtopic.php?t=46265) by Ruxy Sylwyka, [CCC](CCC "CCC"), December 03, 2012
* [Author of NGplay\_61 should give credit to tscp](http://www.open-chess.org/viewtopic.php?f=3&t=2161) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2012
* [new chess computer: CT800](http://www.talkchess.com/forum/viewtopic.php?t=61345) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), September 05, 2016 » [CT800](CT800 "CT800")
* [NGplay 9.87 64-bit released](http://www.talkchess.com/forum/viewtopic.php?t=63273) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), February 25, 2017


## External Links


* [George Georgopoulos Personal page](http://users.otenet.gr/~yggeorgo/)
* [NGplay\_9.87.c](http://users.otenet.gr/~yggeorgo/NGplay_9.87.c)
* [NG-Play](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=NG-Play&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [NGplay\_9.87.c](http://users.otenet.gr/~yggeorgo/NGplay_9.87.c)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Bruce Moreland's Programming Topics](https://web.archive.org/web/20071026090003/http://www.brucemo.com/compchess/programming/index.htm) archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [NGplay\_9.87.c](http://users.otenet.gr/~yggeorgo/NGplay_9.87.c)

**[Up one Level](Engines "Engines")**







 
