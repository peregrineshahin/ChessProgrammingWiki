---
title: Movei
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Movei**


**Movei**,  

a [WinBoard](WinBoard "WinBoard") and [UCI](UCI "UCI") compliant chess engine by [Uri Blass](Uri_Blass "Uri Blass"). Movei is written in [C](C "C") around a [legal move generator](Move_Generation#Legal "Move Generation") and initial [Perft](Perft "Perft") framework, also gathering [attack](Attack_and_Defend_Maps "Attack and Defend Maps") and [mobility](Mobility "Mobility") informations as used in [evaluation](Evaluation "Evaluation"). 
As mentioned by Uri, the evaluation of Movei is [dependent on the path](Path-Dependency "Path-Dependency") and not only on the [leaf position](Leaf_Node "Leaf Node") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The [transposition table](Transposition_Table "Transposition Table") was at least initially not used for pruning, but only for [move ordering](Move_Ordering "Move Ordering"). According to Uri, [PVS](Principal_Variation_Search "Principal Variation Search") and [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") do not seem to work in his program <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Selected Games](#selected-games)
	+ [2.1 WCCC 2004](#wccc-2004)
	+ [2.2 CCT7](#cct7)
* [3 Forum Posts](#forum-posts)
	+ [3.1 2002](#2002)
	+ [3.2 2003](#2003)
	+ [3.3 2004](#2004)
	+ [3.4 2005 ...](#2005-...)
	+ [3.5 2010 ...](#2010-...)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc)
* [5 References](#references)






Movei played the [WCCC 2004](WCCC_2004 "WCCC 2004") in [Ramat Gan](https://en.wikipedia.org/wiki/Ramat_Gan), and on-line the [CCT5](CCT5 "CCT5"), [CCT6](CCT6 "CCT6") and [CCT7](CCT7 "CCT7") tournaments. 



## Selected Games


### WCCC 2004


[WCCC 2004](WCCC_2004 "WCCC 2004"), round 5, Movei - [The Crazy Bishop](The_Crazy_Bishop "The Crazy Bishop") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "WCCC 2004"]
[Site "Ramat-Gan, Israel"]
[Date "2004.07.08"]
[Round "5"]
[White "Movei"]
[Black "The Crazy Bishop"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 d5 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Re8 8.Nge2 Nbd7 9.Qc2 c6 
10.O-O-O Qa5 11.Kb1 h6 12.Bf4 Nh5 13.Be5 Nxe5 14.dxe5 Bc5 15.Nd4 Bxd4 16.Bh7+ Kh8 17.exd4 
Qd8 18.Bf5 Nf4 19.g3 Ne6 20.f4 Nc7 21.Bxc8 Rxc8 22.Rhf1 Qd7 23.f5 c5 24.Qd2 Kg8 25.f6 Qg4 
26.fxg7 cxd4 27.Qxh6 Qxg7 28.Qxg7+ Kxg7 29.Rxd4 Rxe5 30.Rdf4 Re7 31.Rg4+ Kf8 32.Rb4 b6 
33.Rh4 Kg7 34.Rg4+ Kf8 35.Ra4 Ra8 36.Kc2 Rd7 37.Rh4 Rad8 38.Kd2 Kg7 39.Rg4+ Kf8 40.Ne2 
Ne6 41.Rh4 Ke7 42.Rh5 d4 43.Nf4 Nc5 44.Re1+ Kf6 45.h4 Kg7 46.Rg5+ Kf8 47.b4 Na4 48.Rf5 Kg7 
49.Nh5+ Kf8 50.Nf6 Re7 51.Nh7+ Ke8 52.Rfe5 Rxe5 53.Rxe5+ Kd7 54.Nf6+ Kc6 55.h5 Rh8 56.Kd3 
Nc3 57.g4 a5 58.bxa5 bxa5 59.Rxa5 Kb6 60.Rf5 Kc6 61.Kxd4 Nb5+ 62.Ke5 Nc7 63.Rf1 Ne6 64.Ne4 
Rh7 65.Rf6 Kc7 66.Nd6 Nd8 67.h6 Kd7 68.g5 Ke7 69.a4 Nc6+ 70.Kd5 Nb4+ 71.Kc4 Nc6 72.Nxf7 
Nb8 73.Nd6 Nd7 74.Nf5+ Kd8 75.Rd6 1-0 

```

### CCT7


[CCT7](CCT7 "CCT7"), round 3, [Crafty](Crafty "Crafty") - Movei <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "CCT7"]
[Site "ICC"]
[Date "2005.02.12"]
[Round "3"]
[White "Crafty"]
[Black "Movei"]
[Result "0-1"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.f3 d5 5.a3 Bxc3+ 6.bxc3 c5 7.cxd5 Nxd5 8.dxc5 Qa5 9.e4 Ne7 
10.Be3 O-O 11.Qb3 Qc7 12.a4 Nd7 13.Qa3 f5 14.Nh3 Nf6 15.Nf2 Bd7 16.Be2 Kh8 17.O-O Rad8 
18.Rfd1 Bc6 19.Qb4 fxe4 20.fxe4 Qe5 21.Bf3 Ng6 22.Kh1 Nh4 23.Bd4 Qc7 24.Bxf6 Rxf6 25.Ng4 
Rxd1+ 26.Rxd1 Nxf3 27.gxf3 Rxf3 28.Ne5 Rf8 29.Rd6 Qe7 30.Nxc6 Qf6 31.Qb1 Qf3+ 32.Kg1 Qf2+ 
33.Kh1 bxc6 34.Qd3 h6 35.e5 Qe1+ 36.Kg2 Qxe5 37.Rxc6 Qg5+ 38.Kh3 h5 39.Qe4 Qf6 40.Qe2 Qf5+ 
41.Kh4 g5+ 42.Kg3 h4+ 43.Kg2 Qd5+ 44.Kg1 Qxc6 45.Qh5+ Kg7 46.Qxg5+ Kf7 47.Qh5+ Ke7 
{Crafty resigns} 0-1

```

## Forum Posts


### 2002


* [my program movei is released](https://www.stmintz.com/ccc/index.php?id=229271) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 12, 2002
* [Re: Did Uri write movei? (yes)](https://www.stmintz.com/ccc/index.php?id=235364) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 13, 2002


 [Re: Did Uri write movei? (yes)](https://www.stmintz.com/ccc/index.php?id=235379) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 13, 2002
* [Test positions from sjeng-movei games](https://www.stmintz.com/ccc/index.php?id=244404) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 07, 2002 » [Sjeng](Sjeng "Sjeng")
* [A case when Movei earn 2 plies from verified null move pruning](https://www.stmintz.com/ccc/index.php?id=266941) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), November 22, 2002 » [Verified Null Move Pruning](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")


### 2003


* [How to use Movei as an automatic player in ICC](https://www.stmintz.com/ccc/index.php?id=276537) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 11, 2003


### 2004


* [Movei @ CCT6](https://www.stmintz.com/ccc/index.php?id=346480) by Luis Smith, [CCC](CCC "CCC"), February 02, 2004 » [CCT6](CCT6 "CCT6")
* [about a possible problem with movei's logfiles(also for other programs)](https://www.stmintz.com/ccc/index.php?id=352371) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), March 02, 2004
* [Two more Movei matches](https://www.stmintz.com/ccc/index.php?id=353377) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), March 07, 2004
* [movei book progress report](https://www.stmintz.com/ccc/index.php?id=367829) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 28, 2004
* [question about fixing the time management of movei](https://www.stmintz.com/ccc/index.php?id=378905) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 25, 2004 » [Time Management](Time_Management "Time Management")
* [Welcome new movei](https://www.stmintz.com/ccc/index.php?id=398390) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), November 30, 2004


### 2005 ...


* [Movei report in CCT7:first day](https://www.stmintz.com/ccc/index.php?id=412540) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 19, 2005 » [CCT7](CCT7 "CCT7")
* [Re: And a still unsolved test position](https://www.stmintz.com/ccc/index.php?id=430487) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 09, 2005 » [Path-Dependency](Path-Dependency "Path-Dependency")
* [Is it a bug in Movei(what is your opinion?)](https://www.stmintz.com/ccc/index.php?id=456285) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 17, 2005
* [I need testers for testing movei personalities in test suites](https://www.stmintz.com/ccc/index.php?id=459424) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), November 03, 2005
* [Rybka(1 plies)-Movei(3 plies) 10-10 in the nunn match](https://www.stmintz.com/ccc/index.php?id=467574) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), December 06, 2005 » [Rybka](Rybka "Rybka")
* [Movei-Gerbil in rhe endgame suite 20.5-9.5 and could be 21.5-8.5](https://www.stmintz.com/ccc/index.php?id=476082) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 01, 2006 » [Gerbil](Gerbil "Gerbil")


**2007**



* [movei progress 10 10 10 personality](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=13328) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 23, 2007
* [Re: Methods to stably evaluate nodes?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=115849&t=13559) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 05, 2007
* [Re: Revisiting Check Extensions](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=123834&t=14333) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 07, 2007 » [Check Extensions](Check_Extensions "Check Extensions")
* [Re: Thanks for the mobility info ed](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=126143&t=14611) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 22, 2007
* [movei hash report](http://www.talkchess.com/forum/viewtopic.php?t=15688) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 09, 2007 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [movei need testers to find a better personality](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=16809) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 01, 2007


### 2010 ...


* [Movei, The Baron, and TSCP](http://www.talkchess.com/forum/viewtopic.php?t=51063) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 23, 2014 » [The Baron](The_Baron "The Baron"), [TSCP](TSCP "TSCP")


## External Links


### Chess Engine


* [Movei's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=109)
* [Movei 00.8.438 (10 10 10)](http://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Movei%2000.8.438%20%2810%2010%2010%29#Movei_00_8_438_%2810_10_10%29) in [CCRL 40/40](CCRL "CCRL")
* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)


### Misc


* [movei - Wiktionary](https://en.wiktionary.org/wiki/movei)
* [Move α from Wikipedia](https://en.wikipedia.org/wiki/Move_%CE%B1)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Methods to stably evaluate nodes?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=115849&t=13559) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 05, 2007
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [movei hash report](http://www.talkchess.com/forum/viewtopic.php?t=15688) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 09, 2007
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ramat-Gan 2004 - Chess - Round 5 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=24&round=5&id=5)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Movei report in CCT7:first day](https://www.stmintz.com/ccc/index.php?id=412540) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 19, 2005





 
