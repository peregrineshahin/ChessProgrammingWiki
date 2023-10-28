---
title: Waycool
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Waycool**



[ [P-generalized](https://en.wikipedia.org/wiki/Complex_polytope#Quasiregular_polyhedra) [5-cube](https://en.wikipedia.org/wiki/5-cube) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Waycool**,  

a massive [parallel](Parallel_Search "Parallel Search") chess program from [California Institute of Technology](https://en.wikipedia.org/wiki/California_Institute_of_Technology), [Pasadena, California](https://en.wikipedia.org/wiki/Pasadena,_California), running on [nCUBE/10](NCUBE "NCUBE") concurrent computer with [hypercube](https://en.wikipedia.org/wiki/Hypercube) topology, written in the 80s by [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") and [Rod Morison](index.php?title=Rod_Morison&action=edit&redlink=1 "Rod Morison (page does not exist)"), at times supported by [Rob Fatland](index.php?title=Rob_Fatland&action=edit&redlink=1 "Rob Fatland (page does not exist)"). Waycool played three [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), the [ACM 1986](ACM_1986 "ACM 1986"), [ACM 1987](ACM_1987 "ACM 1987") and [ACM 1988](ACM_1988 "ACM 1988"), as well the [WCCC 1989](WCCC_1989 "WCCC 1989") in [Edmonton](https://en.wikipedia.org/wiki/Edmonton), [Alberta](https://en.wikipedia.org/wiki/Alberta), [Canada](https://en.wikipedia.org/wiki/Canada) <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Contents


* [1 Description](#description)
* [2 Selected Games](#selected-games)
* [3 Publications](#publications)
* [4 External Links](#external-links)
	+ [4.1 Chess Program](#chess-program)
	+ [4.2 Misc](#misc)
* [5 References](#references)






Abstract of *Chess on a Hypercube* <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```
We report our progress on computer chess last described at the Second Conference on Hypercubes. Our program follows the strategy of currently successful sequential chess programs: searching of an [alpha-beta](Alpha-Beta "Alpha-Beta") pruned game tree, [iterative deepening](Iterative_Deepening "Iterative Deepening"), [transposition](Transposition_Table "Transposition Table") and [history](History_Heuristic "History Heuristic") tables, specialized endgame evaluators, and so on. The [search tree](Search_Tree "Search Tree") is decomposed onto the [hypercube](https://en.wikipedia.org/wiki/Hypercube) (an [nCUBE](NCUBE "NCUBE")) using a [recursive](Recursion "Recursion") version of the [principal-variation-splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search") algorithm. Roughly speaking, subtrees are searched by teams of processors in a self-scheduled manner. 

A crucial feature of the program is the [global hashtable](Shared_Hash_Table "Shared Hash Table"). Hashtables are important in the sequential case, but are even more central for a parallel chess algorithm. The table not only stores knowledge but also makes the decision at each node of the chess tree whether to stay sequential or to split up the work in parallel. In the language of Knuth and Moore, the transposition table decides whether each node of the chess tree is a [type 2](Node_Types#CUT "Node Types") or a [type 3 node](Node_Types#ALL "Node Types") and acts accordingly. For this data structure the hypercube is used as a shared-memory machine. Multiple writes to the same location are resolved using a priority system which decides which entry is of more value to the program. The hashtable is implemented as “smart” shared memory. 

```


```
Search times for related subtrees vary widely (up to a factor of 100) so dynamic reconfiguration of processors is necessary to concentrate on such “hot spots” in the tree. A first version of the program with dynamic load balancing has recently been completed and out-performs the non-load-balancing program by a factor of three. The current speedup of the program is 101 out of a possible 256 processors. The program has played in several tournaments, facing both computers and people. Most recently it scored 2-2 in the [ACM North American Computer Chess Championship](ACM_1987 "ACM 1987"). 

```

## Selected Games


[WCCC 1989](WCCC_1989 "WCCC 1989"), round 1, Waycool - [Mephisto X](Mephisto "Mephisto") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "WCCC 1989"]
[Site "Edmonton, Canada"]
[Date "1989.05.28"]
[Round "1"]
[White "Waycool"]
[Black "Mephisto X"]
[Result "1-0"]

1.e4 d6 2.d4 Nf6 3.Nc3 c6 4.Nf3 Bg4 5.h3 Bh5 6.Bd3 e6 7.Rg1 Be7 8.g4 Bg6
9.e5 dxe5 10.dxe5 Nd5 11.Nxd5 cxd5 12.Be2 O-O 13.c3 Nc6 14.Qb3 Na5 15.Qa4
Qb6 16.Nd4 Nc6 17.Nxc6 bxc6 18.b3 Qc5 19.Rg3 Bc2 20.Qd4 Qa5 21.Bd2 Rab8 
22.c4 Qb6 23.Qxb6 axb6 24.cxd5 cxd5 25.Rc1 Be4 26.Rc7 Bd8 27.Ra7 Bh4 28.Rc3 
Ra8 29.Rxa8 Rxa8 30.a4 h6 31.Be3 Rb8 32.Kf1 Bg5 33.f4 Bd8 34.Bb5 g5 35.Kf2 
gxf4 36.Bxf4 Bg5 37.Be3 f6 38.exf6 Bxe3+ 39.Kxe3 Kf7 40.Rc6 Kxf6 41.Kd4 Bg6 
42.Be2 Be8 43.Rd6 Bf7 44.h4 Rb7 45.Ba6 Rb8 46.Bf1 Rb7 47.Bg2 Rb8 48.Bf3 Bg8 
49.Bh1 Bf7 50.Bg2 Ke7 51.Ke5 b5 52.a5 b4 53.a6 Rb5 54.Bf1 Ra5 55.Rb6 d4+ 
56.Rb5 Ra1 57.Bd3 Be8 58.Rb7+ Kf8 59.Rxb4 Kg7 60.Rxd4 Ra5+ 61.Kd6 1-0 

```

## Publications


* [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") (**1988**). *[Chess on a Hypercube](https://www.semanticscholar.org/paper/Chess-on-a-hypercube-Felten-Otto/78f89caaf173e52524b5f75ed3a4529e1b3fa1f5?tab=abstract)*. The Third Conference on Hypercube Concurrent Computers and Applications, Vol. II-Applications
* [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") (**1988**). *[A Highly Parallel Chess Program](https://www.semanticscholar.org/paper/A-Highly-Parallel-Chess-Program-Felten-Otto/8883761d14be691f6b50d91346cb15af65762710)*. Conference on Fifth Generation Computer Systems


## External Links


### Chess Program


* [Waycool's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=359)


### Misc


* [nCUBE from Wikipedia](https://en.wikipedia.org/wiki/NCUBE)
* [Hypercube from Wikipedia](https://en.wikipedia.org/wiki/Hypercube)
* [Cool (aesthetic) from Wikipedia](https://en.wikipedia.org/wiki/Cool_%28aesthetic%29)
* [Jesus Was Way Cool from Wikipedia](https://en.wikipedia.org/wiki/Jesus_Was_Way_Cool)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Complex polytope](https://en.wikipedia.org/wiki/Complex_polytope) p-generalized [5-cube](https://en.wikipedia.org/wiki/5-cube) of 1024 nodes, [Image](https://commons.wikimedia.org/wiki/File:4-generalized-5-cube.svg) by [Tomruen](https://commons.wikimedia.org/wiki/User:Tomruen), September 19, 2016, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Waycool's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=359)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [King Moves - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") (**1988**). *[Chess on a Hypercube](https://www.semanticscholar.org/paper/Chess-on-a-hypercube-Felten-Otto/78f89caaf173e52524b5f75ed3a4529e1b3fa1f5?tab=abstract)*. The Third Conference on Hypercube Concurrent Computers and Applications, Vol. II-Applications
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Edmonton 1989 - Chess - Round 1 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=14&round=1&id=5)

**[Up one level](Engines "Engines")**







 
