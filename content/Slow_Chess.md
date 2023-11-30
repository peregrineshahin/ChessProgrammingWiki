---
title: Slow Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Slow Chess**


**Slow Chess**, (SlowChess, Slow Chess Blitz)  

a [WinBoard](WinBoard "WinBoard") and [UCI](UCI "UCI") compliant engine chess engine by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), which also comes with an own [GUI](GUI "GUI"). Older versions, Slow Chess 2.82a, and Slow Chess 2.96, not related to the more recent *Slow Chess Blitz*, are [open source](Category:Open_Source "Category:Open Source"). 
Slow Chess is written in [C++](Cpp "Cpp") with a little [inline assembly](Assembly#InlineAssembly "Assembly"), and was first released in July 2003. Slow Chess played the [ACCA 2008](ACCA_2008 "ACCA 2008") operated by [Swaminathan Natarajan](Swaminathan_Natarajan "Swaminathan Natarajan"). After a 14-year hiatus, a new version of **Slow Chess Blitz** was released in September 2019 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



## Description


Slow Chess 2.96's internal board is represented by a [10x12 board](10x12_Board "10x12 Board") in conjunction with [piece-lists](Piece-Lists "Piece-Lists").
The [search](Search "Search") applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). 
[Move ordering](Move_Ordering "Move Ordering") is enhanced by [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [MVV-LVA](MVV-LVA "MVV-LVA"), [history heuristic](History_Heuristic "History Heuristic"), and [killer heuristic](Killer_Heuristic "Killer Heuristic"). Despite direct [recursion](Recursion "Recursion"), it does not [negamax](Negamax "Negamax"), but conditional min or max. 
[Checks](Check_Extensions "Check Extensions"), [recaptures](Recapture_Extensions "Recapture Extensions"), [pawn moves to the 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), [single replies](One_Reply_Extensions "One Reply Extensions") and [mate threatening moves](Mate_Threat_Extensions "Mate Threat Extensions") are [extended](Extensions "Extensions") by [fractions](Extensions#FractionalExtensions "Extensions") of a [ply](Ply "Ply") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
[Evaluation](Evaluation "Evaluation") considers [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") with an [lazy](Lazy_Evaluation "Lazy Evaluation") exit if outside bounds, and otherwise cashes [pawn structure](Pawn_Structure "Pawn Structure") stuff in a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), evaluates [king safety](King_Safety "King Safety") along with [king piece tropism](King_Safety#KingTropism "King Safety"), and various terms for [pieces](Evaluation_of_Pieces "Evaluation of Pieces") such as [trapped bishops](Trapped_Pieces "Trapped Pieces"). All evaluation [scores](Score "Score") greater than 4 or less than -4 are [quantized](https://en.wikipedia.org/wiki/Quantization_%28signal_processing%29) and have its two least significant bits clear to make the scores multiples of ±4.



## Selected Games


[ACCA 2008](ACCA_2008 "ACCA 2008"), round 2, Slow Chess - [Amateur](Amateur "Amateur") <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```
[Event "ACCA 2008"]
[Site "Internet Chess Club"]
[Date "2008.11.08"]
[Round "2"]
[White "Slow Chess"]
[Black "Amateur"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.g3 d5 4.Nf3 dxc4 5.Qa4+ Bd7 6.Qxc4 Bc6 7.Bg2 Bd5 8.Qd3 Be4 9.Qd1 Nc6 
10.O-O Nb4 11.Nc3 Bc2 12.Qd2 Ne4 13.Qe1 Nd5 14.Ne5 Bb4 15.Bd2 Bxc3 16.bxc3 f6 17.Rc1 Nxd2 
18.Qxd2 Bf5 19.Nc4 Bg4 20.Na5 b5 21.c4 bxc4 22.Rxc4 O-O 23.Rfc1 Bh5 24.R4c5 f5 25.Nc6 Qf6 
26.Bxd5 exd5 27.Ne5 f4 28.Nd7 Qe6 29.Nxf8 Rxf8 30.f3 fxg3 31.hxg3 Qh3 32.Qe1 Qe6 33.R5xc7 
Re8 34.Qd2 h6 35.R1c6 Qxe2 36.Qxe2 Rxe2 37.Rxa7 Bxf3 38.Rg6 Be4 39.Rgxg7+ Kh8 40.Rge7 Rg2+ 
41.Kf1 Rxg3 42.Ra8+ Rg8 43.Rxg8+ Kxg8 44.Rxe4 dxe4 45.a4 Kf7 46.a5 1-0

```

## Forum Posts


### 2004


* [My Pick for Strongest Amateur Program ("SlowChess!) Commercial?](https://www.stmintz.com/ccc/index.php?id=345786) by Nolan Denson, [CCC](CCC "CCC"), January 30, 2004
* [SlowChess Blitz rocks !!](https://www.stmintz.com/ccc/index.php?id=397314) by [Axel Schumacher](index.php?title=Axel_Schumacher&action=edit&redlink=1 "Axel Schumacher (page does not exist)"), [CCC](CCC "CCC"), November 22, 2004
* [SlowChess Blitz 2004](https://www.stmintz.com/ccc/index.php?id=397390) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), November 23, 2004
* [More great SlowChess Blitz results!](https://www.stmintz.com/ccc/index.php?id=397523) by [Axel Schumacher](index.php?title=Axel_Schumacher&action=edit&redlink=1 "Axel Schumacher (page does not exist)"), [CCC](CCC "CCC"), November 24, 2004
* [CM9000 Default v SlowChess G-10 20-game match](https://www.stmintz.com/ccc/index.php?id=397717) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), November 25, 2004


### 2005 ...


* [SlowChess Blitz WV is stunning is test suites!](https://www.stmintz.com/ccc/index.php?id=457528) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), October 24, 2005
* [Slowchess 2.96 Windows 64-bit build available](http://www.talkchess.com/forum/viewtopic.php?t=18458) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 19, 2007
* [SlowChess in ACCA](http://www.talkchess.com/forum/viewtopic.php?t=24831) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), November 11, 2008 » [ACCA 2008](ACCA_2008 "ACCA 2008")


### 2010 ...


* [SlowChess 2.96 LS (Limit Strength)](http://www.talkchess.com/forum/viewtopic.php?t=46052) by [Alexander Schmidt](index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)"), [CCC](CCC "CCC"), November 18, 2012
* [I Am Lost With This SlowChess 2.960-Makes No Sense](http://www.talkchess.com/forum3/viewtopic.php?f=6&t=47726) by [George Speight](index.php?title=George_Speight&action=edit&redlink=1 "George Speight (page does not exist)"), [CCC](CCC "CCC"), April 08, 2013
* [Slow Chess](http://www.talkchess.com/forum/viewtopic.php?t=57518) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), September 05, 2015
* [Slow Chess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71721) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 04, 2019


### 2020 ...


* [SlowChess Blitz Classic 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), March 20, 2020


 [Re: SlowChess Blitz Classic 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=42) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 02, 2020
* [Just found a 55 elo bug in SlowChess 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74066) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 01, 2020
* [Learning/Tuning in SlowChess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74184) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 23, 2020 » [Neural Networks](Neural_Networks "Neural Networks")
* [Re: SlowChess Blitz Classic 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=55) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), November 02, 2020 » SlowChess 2.4
* [More experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76263) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), January 09, 2021
* [Re: SlowChess Blitz Classic 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=73) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), January 11, 2021 » SlowChess 2.5
* [Some more experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77492) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2021
* [SlowChess Blitz Classic 2.6](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=94) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 20, 2021
* [SlowChess Blitz 2.7](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=109) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), August 26, 2021
* [SlowChess Blitz Classic 2.8](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=73420&start=129) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), November 18, 2021


## External Links


* [Slow Chess Blitz, a free chess program](https://www.3dkingdoms.com/chess/slow.htm)
* [Programming Details - Slow Chess | Extensions Used, Detailed Description](https://www.3dkingdoms.com/chess/implementation.htm)
* [Automatic Tuning & Learning for Slow Chess Blitz Classic](https://www.3dkingdoms.com/chess/learning.html) by by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer") » [Automated Tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [History of Slow Chess](https://www.3dkingdoms.com/chess/history.htm)
* [Slow Chess Blitz](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Slow%20Chess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Slow Chess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71721) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 04, 2019
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Slow Chess Blitz, a free chess program](http://www.3dkingdoms.com/chess/slow.htm)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Programming Details - Slow Chess | Extensions Used, Detailed Description](http://www.3dkingdoms.com/chess/implementation.htm)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The 2008 Third Annual ACCA Americas' Computer Chess Championships - Results - pgn download](http://compchess.org/ACCAChampionships/ACCA2008Championships/2008ACCCResults.html)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Learning/Tuning in SlowChess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74184) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2020

**[Up one level](Engines "Engines")**







 
