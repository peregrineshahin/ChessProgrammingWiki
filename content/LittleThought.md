---
title: LittleThought
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* LittleThought**



[_detail.jpg) Little thought No. 2 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**LittleThought**,  

a free [UCI](UCI "UCI") compatible chess engine by [Nathan Thom](Nathan_Thom "Nathan Thom"), written in [C++](Cpp "Cpp"), first mentioned in 2003 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Since **v1.05** in 2010, LittleThought is able to play [Chess960](Chess960 "Chess960") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Contents


* [1 Descirption](#descirption)
* [2 Tournament Play](#tournament-play)
* [3 Selected Games](#selected-games)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2003 ...](#2003-...)
	+ [5.2 2010 ...](#2010-...)
* [6 External Links](#external-links)
* [7 References](#references)






LittleThought uses a [rotated bitboard](Rotated_Bitboards "Rotated Bitboards") based, fully [incremental](Incremental_Updates "Incremental Updates") [move generator](Move_Generation "Move Generation"), and applies a [PVS](Principal_Variation_Search "Principal Variation Search") based [alpha-beta search](Alpha-Beta "Alpha-Beta") with several [tree shaping](Selectivity "Selectivity") and [pruning](Pruning "Pruning") routines, such as [singular extensions](Singular_Extensions "Singular Extensions"), [late move reductions](Late_Move_Reductions "Late Move Reductions"), and [null move pruning](Null_Move_Pruning "Null Move Pruning"), and 4-way probe [transposition table](Transposition_Table "Transposition Table") with other smaller [hash tables](Hash_Table "Hash Table") for caching calculations of [pawns](Pawn_Hash_Table "Pawn Hash Table"), [materials](Material_Hash_Table "Material Hash Table"), and [evaluation](Evaluation_Hash_Table "Evaluation Hash Table"). 
The [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic") as well just in case [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") improve [move ordering](Move_Ordering "Move Ordering"). 
Up to 8 [threads](Thread "Thread") are supported for a [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") based [parallel search](Parallel_Search "Parallel Search") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Tournament Play


LittleThought played the [NC3 2006](NC3_2006 "NC3 2006") [Australasian National Computer Chess Championship](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship"). 



## Selected Games


[NC3 2006](NC3_2006 "NC3 2006"), round 4, LittleThought - [Fencer](Fencer "Fencer")




```

[Event "NC3 2006"]
[Site "RedHill, Canberra, Australia"]
[Date "2006.08.20"]
[Round "4"]
[White "LittleThought"]
[Black "Fencer"]
[Result "1-0"]

1.e4 Nc6 2.d4 d5 3.exd5 Qxd5 4.Nf3 e6 5.a3 Bd7 6.Nc3 Qa5 7.Bd2 Qf5 8.Nb5 
Rc8 9.Bd3 Qg4 10.h3 Qh5 11.g4 Qd5 12.c4 Ne5 13.Nxc7+ Rxc7 14.cxd5 Nxd3+ 
15.Kf1 Nxb2 16.Qb3 Nc4 17.Bf4 Na5 18.Qb1 Rc4 19.Ne5 b6 20.Nxd7 Kxd7 21.Qb5+
Kd8 22.Bb8 Rc3 23.Bxa7 Nc4 24.Bxb6+ Nxb6 25.Qxb6+ Kd7 26.Re1 Bd6 27.Qb5+ 
Ke7 28.dxe6 fxe6 29.Qf5 e5 30.dxe5 Bxa3 31.Qg5+ 1-0

```

## See also


* [LittleBlitzer](LittleBlitzer "LittleBlitzer")


## Forum Posts


### 2003 ...


* [Returning PV from hash table](https://www.stmintz.com/ccc/index.php?id=277422) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), January 15, 2003 » [Principal Variation](Principal_Variation "Principal Variation")
* [killers and history](https://www.stmintz.com/ccc/index.php?id=278991) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), January 22, 2003 » [Killer Heuristic](Killer_Heuristic "Killer Heuristic"), [History Heuristic](History_Heuristic "History Heuristic")
* [Threading issue under Polyglot](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5603) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 18, 2006 » [Thread](Thread "Thread"), [PolyGlot](PolyGlot "PolyGlot")
* [LittleThought v1.01 released](http://www.talkchess.com/forum/viewtopic.php?t=15397) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), Jul 28, 2007
* [LittleThought 1.01 : 2157](http://www.talkchess.com/forum/viewtopic.php?t=15486) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), July 31, 2007
* [LittleThought 1.02 : 2240](http://www.talkchess.com/forum/viewtopic.php?t=17713) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), November 08, 2007
* [LittleThought 1.03 : 2229](http://www.talkchess.com/forum/viewtopic.php?t=18749) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), January 05, 2008
* [LittleThought 1.04 : 2344](http://www.talkchess.com/forum/viewtopic.php?t=30535) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), November 08, 2009
* [Little Thought 1.04 64-bit 2-CPU](http://www.talkchess.com/forum/viewtopic.php?t=31132) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), December 18, 2009
* [YBWC details](http://www.talkchess.com/forum/viewtopic.php?t=31366) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), December 31, 2009 » [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


### 2010 ...


* [LittleThought v1.05 released](http://www.talkchess.com/forum/viewtopic.php?t=33884) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), April 20, 2010
* [LittleThought 1.05 : 2403](http://www.talkchess.com/forum/viewtopic.php?t=33911) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), April 21, 2010
* [LittleThought 1.052 64-bit Gauntlets (CCRL 40/40)](http://www.talkchess.com/forum/viewtopic.php?t=34197) by [Aser Huerga](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=4456), [CCC](CCC "CCC"), May 07, 2010
* [Nice attack from LittleThought 1.052](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=48674) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), July 17, 2013


## External Links


* [LittleThought Chess Software](http://www.kimiensoftware.com/software/chess/littlethought)
* [LittleThought Chess Software - Change History](http://www.kimiensoftware.com/software/chess/littlethought_history)


 [LittleBlitzer Chess Software](http://www.kimiensoftware.com/software/chess/littleblitzer)
* [LittleThought 1.052 64-bit](http://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=LittleThought%201.052%2064-bit#LittleThought_1_052_64-bit) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Little thought No. 2 detail](https://commons.wikimedia.org/wiki/File:WLANL_-_Marjolein_Benard_-_Little_thought_No._2,_Qiangli_Liang_(2005)_detail.jpg) by [Qiangli Liang](index.php?title=Category:Qiangli_Liang&action=edit&redlink=1 "Category:Qiangli Liang (page does not exist)"), from [Little thought No. 2, Qiangli Liang (2005) detail | Flickr - Fotosharing!](https://www.flickr.com/photos/39373836@N06/3673214726/) by [Marjolein Benard](https://www.flickr.com/people/39373836@N06), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Returning PV from hash table](https://www.stmintz.com/ccc/index.php?id=277422) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), January 15, 2003
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Kimien Software - LittleThought Chess Software - Change History](http://www.kimiensoftware.com/software/chess/littlethought_history)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [LittleThought Chess Software](http://www.kimiensoftware.com/software/chess/littlethought)

**[Up one Level](Engines "Engines")**







 
