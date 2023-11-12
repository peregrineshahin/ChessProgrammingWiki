---
title: Warp
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Warp**



[ Warp drive <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Warp**,  

a private chess engine by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), and successor of [LambChop](LambChop "LambChop"). Warp was most active in 2002/2003, playing the [WCCC 2002](WCCC_2002 "WCCC 2002") in [Maastricht](https://en.wikipedia.org/wiki/Maastricht), the [DOCCC 2002](DOCCC_2002 "DOCCC 2002"), and the [CCT4](CCT4 "CCT4"). 
It further won the [NC3 2003](NC3_2003 "NC3 2003") and [NC3 2004](NC3_2004 "NC3 2004") [Australasian National Computer Chess Championship](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship"). 



### Contents


* [1 Description](#description)
* [2 Games](#games)
	+ [2.1 Diep](#diep)
	+ [2.2 Quest](#quest)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Computing](#computing)
	+ [5.3 Misc](#misc)
* [6 References](#references)






from [2003 National Computer Chess Championship](NC3_2003 "NC3 2003") <a id="cite-note-2" href="#cite-ref-2">[2]</a>




```C++
Warp is a follow on from my previous chess program called [LambChop](LambChop "LambChop"), the name was changed when I re-wrote much of the low level code handling [move generation](Move_Generation "Move Generation"), tree traversal etc. Warp has a relatively knowledgable [evaluation function](Evaluation_Function "Evaluation Function") in the style of its predecessor, but has an increased emphasis on [pruning](Pruning "Pruning") irrelevant variations from the [search tree](Search_Tree "Search Tree"). This means that Warp [searches](Search "Search") quite [deeply](Depth "Depth") despite a comparatively low [nodes per second](Nodes_per_Second "Nodes per Second") speed. 

```

## Games


### Diep


[WCCC 2002](WCCC_2002 "WCCC 2002"), round 2, Warp - [Diep](Diep "Diep") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "WCCC 2002"]
[Site "Maastricht, NL"]
[Date "2002.07.07"]
[Round "2"]
[White "Warp"]
[Black "Diep"]
[Result "1/2-1/2"]

1.c4 c5 2.Nc3 Nf6 3.Nf3 Nc6 4.d4 cxd4 5.Nxd4 e6 6.g3 Qb6 7.Nb3 Ne5 8.e4 Bb4 9.Qe2 d6 
10.f4 Nc6 11.Be3 Bxc3+ 12.bxc3 Qc7 13.Bg2 b6 14.O-O O-O 15.g4 Bb7 16.g5 Nd7 17.Rf3 
Ne7 18.Rh3 Rfc8 19.Qh5 Nf8 20.Nd2 Neg6 21.Rf1 Qc6 22.Rf2 Qd7 23.f5 exf5 24.exf5 Bxg2 
25.Kxg2 Ne5 26.Bd4 Re8 27.Kh1 Rac8 28.f6 Ng4 29.Rg2 Re1+ 30.Bg1 Ne5 31.Qh4 Rd1 
32.fxg7 Kxg7 33.Ne4 Qf5 34.Qh6+ Kh8 35.Nxd6 Rxd6 36.Qxd6 Ne6 37.Rhg3 Rd8 38.Qe7 Rd1 
39.Qe8+ Kg7 40.Qa4 Qb1 41.Qb3 Qc1 42.c5 Nf4 43.Rc2 Rxg1+ 44.Rxg1 Qe3 45.Qb1 Qf3+ 
46.Rgg2 Nxg2 47.Rxg2 Nd3 48.Qg1 bxc5 49.h4 Nf4 50.Qf2 Qxg2+ 51.Qxg2 Nxg2 52.Kxg2 Kg6
53.Kf3 Kf5 54.c4 a5 55.a4 Ke5 56.Ke3 Kf5 57.Kf3 Ke5 58.Ke3 Kf5 1/2-1/2

```

### Quest


[WCCC 2002](WCCC_2002 "WCCC 2002"), round 3, [Quest](Quest "Quest") - Warp <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "WCCC 2002"]
[Site "Maastricht, NL"]
[Date "2002.07.07"]
[Round "3"]
[White "Quest"]
[Black "Warp"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 e6 5.e3 Nbd7 6.Qc2 b6 7.Bd3 Bb7 8.O-O Be7 9.b3 Qc7 
10.Bb2 Rd8 11.Rfe1 O-O 12.Red1 h6 13.a3 Bd6 14.cxd5 cxd5 15.Qe2 Qb8 16.Nb5 Be7 17.Ne5 
a6 18.Nc3 b5 19.f4 Rc8 20.Rdc1 Nxe5 21.fxe5 Ne4 22.a4 Bc6 23.Rf1 Rc7 24.Rac1 Rfc8 
25.Qf3 Bg5 26.h4 Bxh4 27.Nxe4 dxe4 28.Bxe4 Bxe4 29.Qxe4 Bg5 30.Rxc7 Rxc7 31.Bc1 bxa4 
32.bxa4 Qb3 33.Bd2 Qxa4 34.Qa8+ Kh7 35.Qe4+ g6 36.Qf3 Qb5 37.Rf2 a5 38.Kh2 a4 39.e4 
Bxd2 40.Rxd2 Qb4 41.Qe3 a3 42.Ra2 Rc3 43.Qf4 Kg8 44.Rf2 Rc7 45.d5 Ra7 46.d6 a2 47.d7 
Rxd7 48.Rxa2 Qb8 49.Ra4 Rd1 50.Qf6 Qb7 51.Qf4 h5 52.Qf3 Rd8 53.Qf6 Rd2 54.Qf4 Rd7 
55.Qf3 Qc6 56.Ra3 Qc8 57.Qf4 Qb7 58.Ra4 Kh7 59.Qf6 Qc6 60.Rb4 Qc7 61.Rb1 Kg8 62.Qf4 
Rd4 63.Ra1 Qb7 64.Re1 Kh7 65.Qf6 Rd3 66.Ra1 Kg8 67.Ra4 Qc6 68.Ra1 Rd4 69.Rb1 Qc7 
70.Ra1 Qb7 71.Rf1 Rd2 72.Qg5 Rd7 73.Qe3 Qb4 74.Qf4 Qb5 75.Ra1 Qb8 76.Rf1 Qb2
77.Rc1 Qb7 78.Ra1 Rd3 79.Qf6 Rd2 80.Rf1 Rd7 81.Qf4 Qb8 82.Rf3 1/2-1/2

```

## See also


* [LambChop](LambChop "LambChop")


## Forum Posts


* [WCCC 2002: Round 2 - WARP vs. DIEP (my analysis)](https://www.stmintz.com/ccc/index.php?id=238978) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), July 07, 2002 » [WCCC 2002](WCCC_2002 "WCCC 2002")
* [WCCC Round 3: Quest vs Warp [maybe draw?](https://www.stmintz.com/ccc/index.php?id=239026)] by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), July 07, 2002
* [Diep - Warp in Leiden](https://www.stmintz.com/ccc/index.php?id=262199) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), October 28, 2002 » [DOCCC 2002](DOCCC_2002 "DOCCC 2002")
* [Warp - Diep, WCCC](https://www.stmintz.com/ccc/index.php?id=268444) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), December 02, 2002


## External Links


### Chess Engine


* [Warp's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=68)
* [Vormärz - Warpendes Lammkotelett](http://old.csvn.nl/VorMaerz.html) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Old CSVN site](CSVN "CSVN") (German) » [WCCC 2002](WCCC_2002 "WCCC 2002")


### Computing


* [WARP (information security) from Wikipedia](https://en.wikipedia.org/wiki/WARP_(information_security))
* [WARP (systolic array) from Wikipedia](https://en.wikipedia.org/wiki/WARP_(systolic_array))


 [iWarp from Wikipedia](https://en.wikipedia.org/wiki/IWarp)
* [Dynamic time warping from Wikipedia](https://en.wikipedia.org/wiki/Dynamic_time_warping)
* [The "Warp" years | OS/2 from Wikipedia](https://en.wikipedia.org/wiki/OS/2#1994.E2.80.931996:_The_.22Warp.22_years)


### Misc


* [Warp (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Warp)
* [Warp (magazine) from Wikipedia](https://en.wikipedia.org/wiki/Warp_%28magazine%29)
* [Warp drive from Wikipedia](https://en.wikipedia.org/wiki/Warp_drive)
* [Warp (weaving) from Wikipedia](https://en.wikipedia.org/wiki/Warp_%28weaving%29)
* [Time Warp from Wikipedia](https://en.wikipedia.org/wiki/Time_Warp)
* [Chick Corea](Category:Chick_Corea "Category:Chick Corea") - New Life, [Time Warp](https://en.wikipedia.org/wiki/Time_Warp_(album)) (1995), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Chick Corea](Category:Chick_Corea "Category:Chick Corea"), [John Patitucci](Category:John_Patitucci "Category:John Patitucci"), [Gary Novak](https://en.wikipedia.org/wiki/Gary_Novak), [Bob Berg](Category:Bob_Berg "Category:Bob Berg")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wormhole](https://en.wikipedia.org/wiki/Wormhole) [travel](https://en.wikipedia.org/wiki/Wormhole#Traversable_wormholes) as envisioned by Les Bossinas (Cortez III Service Corp.), 1998 for [NASA](https://en.wikipedia.org/wiki/NASA), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Warp-Antrieb – Wikipedia.de](https://de.wikipedia.org/wiki/Warp-Antrieb) (German)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [2003 National Computer Chess Championships | List of Entries](http://users.cecs.anu.edu.au/~shaun/chess/NC3_-_List_of_Entries.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Maastricht 2002 - Chess - Round 2 - Game 8 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=20&round=2&id=8)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [WCCC 2002: Round 2 - WARP vs. DIEP (my analysis)](https://www.stmintz.com/ccc/index.php?id=238978) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), July 07, 2002
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Warp - Diep, WCCC](https://www.stmintz.com/ccc/index.php?id=268444) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), December 02, 2002
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Maastricht 2002 - Chess - Round 3 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=20&round=3&id=6)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [WCCC Round 3: Quest vs Warp [maybe draw?](https://www.stmintz.com/ccc/index.php?id=239026)] by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), July 07, 2002

**[Up one level](Engines "Engines")**







 
