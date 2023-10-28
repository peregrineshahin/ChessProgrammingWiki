---
title: Leorik
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Leorik**



 [](File:Leorik.Logo.png) Leorik Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Leorik**,  

an [UCI](UCI "UCI") compatible, didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), written in [C#](C_sharp "C sharp"), and first published in January 2022 - its development reported in a [CCC](CCC "CCC") devlog <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Unshackled from the constraints of minimalism and simplicity, Leorik is the successor of Thomas Jahn's bare-bones chess engine [MinimalChess](MinimalChess "MinimalChess") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and as of Spring 2022, work in progress.




### Contents


* [1 Leorik Attacks](#leorik-attacks)
* [2 Selected Features](#selected-features)
	+ [2.1 Board Representation](#board-representation)
	+ [2.2 Search](#search)
	+ [2.3 Evaluation](#evaluation)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Leorik is a [bitboard](Bitboards "Bitboards") engine and applies an unique approach in determining [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") based on [line-wise attacks on the otherwise empty board](On_an_empty_Board#LineAttacks "On an empty Board") (either pre-calculated or calculated on the fly). All bits below the slider's [origin square](Origin_Square "Origin Square") [bit](General_Setwise_Operations#BitbySquare "General Setwise Operations") are used to separate [positive](On_an_empty_Board#PositiveRays "On an empty Board") and [negative](On_an_empty_Board#NegativeRays "On an empty Board") [rays](Rays "Rays") to scan the nearest blocker (if any) accordingly. 
Positive rays use the line occupancy, intersected with the bits not below to [fill its LS1B](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") (if any) down (MaskLow => bb ^ (bb - 1)). Negative Rays use the line occupancy, intersected with the bits below to fill its [MS1B](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") (if any) down (MaskHigh => 0x7FFFFFFFFFFFFFFFUL >> [leadingZeroCount](BitScan#LeadingZeroCount "BitScan")(bb|1)). The [symmetric difference](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") of both down fills, restricted to the line-wise attacks on the otherwise empty board results in the sliding attack bitboard from that square on one particular line <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## Selected Features


<a id="cite-note-6" href="#cite-ref-6">[6]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Leorik Attacks](#leorikattacks)
* [Copy-Make](Copy-Make "Copy-Make")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Negamax](Negamax "Negamax") [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
	+ [Two Buckets](Transposition_Table#Bucket "Transposition Table")
	+ [Aging](Transposition_Table#Aging "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [MVV-LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") (2.0)
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning") (2.0)


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")


## See also


* [Diablo](Diablo "Diablo")
* [MinimalChess](MinimalChess "MinimalChess")


## Forum Posts


* [Devlog of Leorik](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), January 04, 2022


 [Re: Devlog of Leorik - A.k.a. how to tune high-quality PSTs from scratch (material values) in 20 seconds](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=127) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), March 28, 2022 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Re: Transposition tables are hard...](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79412&start=1) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), February 25, 2022


## External Links


### Chess Engine


* [GitHub - lithander/Leorik: Unshackled from the constraints of minimalism and simplicity Leorik is the successor to my bare-bones chess engine MinimalChess](https://github.com/lithander/Leorik)
* [Leorik 1.0 64-bit](https://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Leorik%201.0%2064-bit#Leorik_1_0_64-bit) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Leoric | Diablo Wiki | Fandom](https://diablo.fandom.com/wiki/Leoric)
* [Leoric - an object-relational mapping for Node.js](https://leoric.js.org/api/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Devlog of Leorik](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=120) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), March 19, 2022
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Devlog of Leorik](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), January 04, 2022
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Leorik/README.md at master · lithander/Leorik · GitHub](https://github.com/lithander/Leorik/blob/master/README.md)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Leorik/Bitboard.cs at master · lithander/Leorik · GitHub](https://github.com/lithander/Leorik/blob/master/Leorik.Core/Bitboard.cs)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Devlog of Leorik](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=2) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), January 04, 2022
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Leorik/README.md at master · lithander/Leorik · GitHub](https://github.com/lithander/Leorik/blob/master/README.md)

**[Up one level](Engines "Engines")**







 
