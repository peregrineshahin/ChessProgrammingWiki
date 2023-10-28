---
title: Stobor
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Stobor**



[ Hot Rock entered 'Stobor' <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Stobor**,  

a private chess engine by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), reportedly commercially available under a different name(s) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
It is named after the [bogeyman](https://en.wikipedia.org/wiki/Bogeyman) character in [Robert Heinlein's](Category:Robert_Heinlein "Category:Robert Heinlein") book, [Tunnel in the Sky](https://en.wikipedia.org/wiki/Tunnel_in_the_Sky) <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Stobor is also "Robots" spelled backwards. 



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Design](#design)
* [3 History](#history)
* [4 Selected Games](#selected-games)
* [5 See also](#see-also)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






Stobor played two [World Microcomputer Chess Championship](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), the [WMCCC 1995](WMCCC_1995 "WMCCC 1995") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn) and the [WMCCC 1997](WMCCC_1997 "WMCCC 1997") in [Paris](https://en.wikipedia.org/wiki/Paris), and further the [IPCCC 1997](IPCCC_1997 "IPCCC 1997") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Design


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



* [Board Representation](Board_Representation "Board Representation"): [0x88](0x88 "0x88")
* [Parallel Search](Parallel_Search "Parallel Search"): [ABDADA](ABDADA "ABDADA")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"): [R=2](Depth_Reduction_R "Depth Reduction R")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search"): [Captures](Captures "Captures")
* [Transposition Table](Transposition_Table "Transposition Table"): [Thompson](Transposition_Table#TwoTier "Transposition Table") (not used in quiescence search)
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


Stobor generates [attack information](Attack_and_Defend_Maps "Attack and Defend Maps") (including [X-ray](X-ray "X-ray")) at the beginning of its [evaluation function](Evaluation_Function "Evaluation Function"), utilized for positional considerations.



## History


<a id="cite-note-6" href="#cite-ref-6">[6]</a>


The first version of Stobor in 1993 was mainly influenced by the 1978 articles by [Peter W. Frey](Peter_W._Frey "Peter W. Frey") and [Larry Atkin](Larry_Atkin "Larry Atkin") on [Chess 0.5](Chess_0.5 "Chess 0.5") in [BYTE magazine](Byte_Magazine#BYTE310 "Byte Magazine") <a id="cite-note-7" href="#cite-ref-7">[7]</a> using attack [bitboards](Bitboards "Bitboards"). After discussions with [Bruce Moreland](Bruce_Moreland "Bruce Moreland") at [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)"), the 1995 rewrite introduced [Ferret](Ferret "Ferret") or [GNU Chess 3](GNU_Chess "GNU Chess") like [precomputed move tables](Table-driven_Move_Generation "Table-driven Move Generation"), while the 1999 rewrite stuck with [0x88](0x88 "0x88"). A first version of a [parallel search](Parallel_Search "Parallel Search") was written in 2002 on a dual Pentium II, optimized in 2016 for 16 cores <a id="cite-note-8" href="#cite-ref-8">[8]</a>. In 2004, Stobor's evaluation function was redesigned as mentioned.



## Selected Games


[WMCCC 1997](WMCCC_1997 "WMCCC 1997"), round 4 Stobor - [Fritz](Fritz "Fritz") <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```

[Event "WMCCC 1997"]
[Site "Paris, France"]
[Date "1997.10.28"]
[Round "4"]
[White "Stobor"]
[Black "Fritz"]
[Result "1-0"]

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5 Bh7 9.Bd3 Bxd3 
10.Qxd3 Qc7 11.Bd2 e6 12.Qe2 Ngf6 13.O-O-O O-O-O 14.Ne5 Nb6 15.Ba5 Rd5 16.b4 Rxa5 
17.bxa5 Ba3+ 18.Kb1 Na4 19.Qf3 Bb4 20.Ne2 Qxa5 21.Rd3 Nd5 22.Qxf7 Nac3+ 23.Nxc3 Nxc3+ 
24.Rxc3 Bxc3 25.Qxe6+ Kc7 26.Qf7+ Kc8 27.Qb3 Rd8 28.Qe6+ Kb8 29.Qb3 Qb4 30.Qxb4 Bxb4 
31.Rd1 Bc3 32.Nf3 Rd5 33.Rd3 Rb5+ 34.Kc1 Bb2+ 35.Kd2 Rxh5 36.Rb3 Rb5 37.Rxb5 cxb5 
38.Kd3 Kc7 39.Nh4 h5 40.f4 Bc1 41.Nf5 g6 42.Ne7 g5 43.f5 a6 44.Ke4 Kd6 45.Ng8 h4 
46.Nf6 b4 47.Ng4 Bb2 48.Nh6 Ke7 49.Ke5 b5 50.f6+ Ke8 51.Ng4 Kf7 52.Nh2 Ba1 53.Nf3 g4 
54.Nxh4 Bc3 55.Nf5 Ba1 56.Nh6+ Ke8 1-0 

```

## See also


* [Demonology](Category:Demonology "Category:Demonology")
* [Fiction](Category:Fiction "Category:Fiction")


## Forum Posts


* [Kerrigan & Stobor](https://groups.google.com/d/msg/rec.games.chess.computer/H3lWAfveS4k/qKB95Rxc3jMJ) by [Kerrigan42](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 04, 1996
* [Stobor's BT results... compare?](https://groups.google.com/d/msg/rec.games.chess.computer/r8KKyUoequs/EE_2upvCmGcJ) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 10, 1996
* [Stobor vs. Crafty](https://groups.google.com/d/msg/rec.games.chess.computer/oRpiYLTUIDM/4WOGGzGz8b0J) by [Tom C. Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 01, 1997
* [Going commercial, maybe](https://groups.google.com/d/msg/rec.games.chess.computer/u-uAjUusB-U/-Sl0qveHdCsJ) by [Tom C. Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 04, 1997
* ["How To" guide to parallel-izing an engine](http://www.talkchess.com/forum/viewtopic.php?t=65011) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), August 27, 2017


## External Links


* [Stobor's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=36)
* [Stobor from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/Stobor)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [Hot Rock Carnival Club](https://www.hotrockcc.co.uk/) entered 'Stobor', a robotic theme, in the 2016 [Weston-super-Mare](https://en.wikipedia.org/wiki/Weston-super-Mare) [carnival](https://en.wikipedia.org/wiki/West_Country_Carnival), Photo by [Geof Sheppard](https://commons.wikimedia.org/wiki/User:Geof_Sheppard), November 11, 2016, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Stobor from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/Stobor) - Licensing
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Beware of stobor!: Robert A. Heinlein’s Tunnel in the Sky](http://www.tor.com/blogs/2011/11/beware-of-stobor-robert-a-heinleins-tunnel-in-the-sky) review by [Jo Walton](http://www.tor.com/Jo%20Walton#filter), November 14, 2011
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Paderborn - Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/Stobor/Paderborn/)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Stobor from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/Stobor) - Design
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Stobor from Tom Kerrigan's Home Page](http://www.tckerrigan.com/Chess/Stobor) - History
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1978**). *[Creating a Chess Player](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d5ba2).* An Essay on Human and Computer Chess Skill, [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Good parallel speedup with ABDADA and cutoff checks](http://www.talkchess.com/forum/viewtopic.php?t=63023) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), February 03, 2017
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Paris 1997 - Chess - Round 4 - Game 14 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=5&round=4&id=14)

**[Up one Level](Engines "Engines")**







 
