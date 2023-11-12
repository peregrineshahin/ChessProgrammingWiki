---
title: EXchess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * EXchess**

**EXchess**, (Experimental Chess Program)

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible experimental [open source chess engine](Category:Open_Source "Category:Open Source") by [Daniel Homan](Daniel_Homan "Daniel Homan"),
written in [C++](Cpp "Cpp"), released under the [GNU Public License](Free_Software_Foundation#GPL "Free Software Foundation").
EXchess may optionally use an own [GUI](GUI "GUI") based on the [Fast Light Tool Kit (FLTK)](https://en.wikipedia.org/wiki/FLTK).

## Contents

- [1 Board Representation](#board-representation)
- [2 Search](#search)
- [3 Lazy SMP](#lazy-smp)
- [4 TD-leaf](#td-leaf)
- [5 Forum Posts](#forum-posts)
  - [5.1 1997 ...](#1997-...)
  - [5.2 2000 ...](#2000-...)
  - [5.3 2005 ...](#2005-...)
  - [5.4 2010 ...](#2010-...)
  - [5.5 2015 ...](#2015-...)
- [6 External Links](#external-links)
- [7 References](#references)

## Board Representation

EXchess utilizes an [8x8 Board](8x8_Board "8x8 Board") and [piece lists](Piece-Lists "Piece-Lists") as demonstrated in its [move generation routine](Move_Generation "Move Generation") <a id="cite-note-1" href="#cite-ref-1">[1]</a> :

```C++

// Typedef for square using unsigned 8 bits...  
//  -- first 3 bits for piece type (0-6)
//  -- next bit for side of piece (1 = white, 0 = black)
// See define.h for marcos and definitions to handle these

typedef uint8_t square;

struct position {
   square sq[64];
   ...
   uint8_t plist[2][7][10];
   ...
};

void position::allmoves(move_list *list, ts_thread_data *tdata) {
   ...
  for(i=1;i<=plist[wtm][PAWN][0];i++) 
    pawn_moves(list, plist[wtm][PAWN][i], tdata);
  for(i=1;i<=plist[wtm][KNIGHT][0];i++) 
    knight_moves(list, plist[wtm][KNIGHT][i], tdata);
  for(i=1;i<=plist[wtm][BISHOP][0];i++) 
    bishop_moves(list, plist[wtm][BISHOP][i], tdata);
  for(i=1;i<=plist[wtm][ROOK][0];i++) 
    rook_moves(list, plist[wtm][ROOK][i], tdata);
  for(i=1;i<=plist[wtm][QUEEN][0];i++) {
    bishop_moves(list, plist[wtm][QUEEN][i], tdata);
    rook_moves(list, plist[wtm][QUEEN][i], tdata);
  }
  for(i=1;i<=plist[wtm][KING][0];i++) 
    king_moves(list, plist[wtm][KING][i], tdata);
}

```

## Search

The ches engine performs advanced [search](Search "Search") algorithms including [principle variation search](Principal_Variation_Search "Principal Variation Search"),
[null move](Null_Move_Pruning "Null Move Pruning"), [null move verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"), [dynamic search extensions](Extensions "Extensions"), [futility pruning](Futility_Pruning "Futility Pruning"), [hash tables](Hash_Table "Hash Table"), [history tables](History_Heuristic "History Heuristic"), [quiescence search](Quiescence_Search "Quiescence Search"), and a [material swap function](Static_Exchange_Evaluation "Static Exchange Evaluation") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Lazy SMP

[Daniel Homan](Daniel_Homan "Daniel Homan") in July 2013 on his [Lazy SMP](Lazy_SMP "Lazy SMP") implementation and work sharing <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
I changed the work-sharing approach to Lazy SMP in EXchess to be closer to the [ABDADA](ABDADA "ABDADA") model after [Daniel Shawul's](Daniel_Shawul "Daniel Shawul") posts about his tests on the subject <a id="cite-note-5" href="#cite-ref-5">[5]</a>. However, I didn't want to use a [hash table](Transposition_Table "Transposition Table") to keep a counter for the [threads](Thread "Thread") working on a given position. My hash table already had a 16 byte long entry, so I didn't want to expand it, and I also didn't like the idea of having to make each move before seeing whether another thread was searching it.

```

```C++
So as an alternative to the hash table, I made a simple work sharing data structure. In the end, it was just a single hash key for a position which is OR'd with the move being searched and the depth of the search. I use this to keep track of the move being searched at each ply of the tree for a given thread. Then, before I search a move at a given ply, I can just check the same ply in the other threads to see that the move is not already being worked on at that depth. If it is, then the move get placed at the end of the move list to be searched last. This doesn't allow for [transpositions](Transposition "Transposition") , but I expected the most likely work collisions to be as the threads are walking the [PV](Principal_Variation "Principal Variation") where they will initially all be the same. Indeed, this scheme only helps in the PV, and if I check for work sharing in [non-PV nodes](Node_Types "Node Types"), it only slows things down a bit.

```

```C++
My previous Lazy SMP work sharing was just to alternate moves (odd-even) in the root node for the odd-even threads. The above approach is about 10% faster than my previous scheme, and I get a time-to-depth improvement of roughly 1.65 for 2 threads compared to 1 thread and roughly 2.5 for 4 threads compared to 1 thread. Maybe not quite as good as ABDADA with a hash table counter, but not too bad for the simplicity.  

```

## TD-leaf

EXchess applies [evaluation](Evaluation "Evaluation") [learning](Learning "Learning") using the [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning") (TD-leaf) <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Forum Posts

## 1997 ...

- [First win against a crafty clone](https://www.stmintz.com/ccc/index.php?id=13011) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 16, 1997 » [Crafty](Crafty "Crafty")
- [New version of EXchess released](https://www.stmintz.com/ccc/index.php?id=16657) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), April 08, 1998
- [EXchess 2.37](https://www.stmintz.com/ccc/index.php?id=20450) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), June 13, 1998
- [New EXchess Version](https://www.stmintz.com/ccc/index.php?id=31385) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), November 02, 1998
- [EXchess pre-release testers sought](https://www.stmintz.com/ccc/index.php?id=82280) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 13, 1999

## 2000 ...

- [version 3.14 of EXchess released](https://www.stmintz.com/ccc/index.php?id=108784) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 02, 2000
- [Pseudo-code for TD learning](https://www.stmintz.com/ccc/index.php?id=117970) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 06, 2000 » [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")
- [New version of EXchess](https://www.stmintz.com/ccc/index.php?id=139716) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), November 18, 2000
- [EXchess v4.02 released](https://www.stmintz.com/ccc/index.php?id=162704) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), April 10, 2001
- [Wb2UCI and Problems with ExChess4.03a and GnuChess4.0.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43496) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 24, 2003 » [Wb2UCI](Wb2UCI "Wb2UCI"), [InBetween](InBetween "InBetween")

## 2005 ...

- [New Version of EXchess](https://www.stmintz.com/ccc/index.php?id=483082) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), Januaray 29, 2006
- [Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 01, 2009 (refers EXchess) » [Automated Tuning](Automated_Tuning "Automated Tuning")

## 2010 ...

- [EXchess v6.01](http://www.talkchess.com/forum/viewtopic.php?t=41666) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 29, 2011

**2012**

- [EXchess v6.10 released](http://www.talkchess.com/forum/viewtopic.php?t=42202) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 29, 2012 » [CLOP](CLOP "CLOP")
- [EXchess v6.50 released](http://www.talkchess.com/forum/viewtopic.php?t=44842) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), August 19, 2012
- [EXchess v6.70 released](http://www.talkchess.com/forum/viewtopic.php?t=46513) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 20, 2012

**2013**

- [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013 » [Lazy SMP](Lazy_SMP "Lazy SMP")
- [EXchess v7.01 Released](http://www.talkchess.com/forum/viewtopic.php?t=47473) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 10, 2013
- [EXchess v7.02 released](http://www.talkchess.com/forum/viewtopic.php?t=47528) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 16, 2013
- [EXchess v7.03 released (bugfix + speed improved version](http://www.talkchess.com/forum/viewtopic.php?t=47643) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 29, 2013
- [EXchess v7.11 released](http://www.talkchess.com/forum/viewtopic.php?t=48448) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), June 27, 2013
- [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013 » [Lazy SMP](Lazy_SMP "Lazy SMP")
- [EXchess v7.17 released](http://www.talkchess.com/forum/viewtopic.php?t=49356) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), September 14, 2013

**2014**

- [EXchess v7.26 released](http://www.talkchess.com/forum/viewtopic.php?t=52241) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 07, 2014
- [EXchess v7.31 released](http://www.talkchess.com/forum/viewtopic.php?t=53319) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), August 17, 2014
- [EXchess v7.51 released](http://www.talkchess.com/forum/viewtopic.php?t=54756) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 26, 2014

## 2015 ...

- [EXchess v7.71 released](http://www.talkchess.com/forum/viewtopic.php?t=56519) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 29, 2015
- [EXchess v7.88 Released](http://www.talkchess.com/forum/viewtopic.php?t=58737) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), December 30, 2015

**2016**

- [EXchess v7.91 released](http://www.talkchess.com/forum/viewtopic.php?t=60121) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 10, 2016

[EXchess v7.92 released](http://www.talkchess.com/forum/viewtopic.php?t=60121&start=2) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), May 11, 2016

- [EXchess v7.92 and AMD Processors](http://www.talkchess.com/forum/viewtopic.php?t=61650) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), October 08, 2016

**2017**

- [EXchess v7.96](http://www.talkchess.com/forum/viewtopic.php?t=62995) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 31, 2017
- [EXchess v7.97](http://www.talkchess.com/forum/viewtopic.php?t=63044) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), February 04, 2017

## External Links

- [Experimental Chess Program](https://sites.google.com/site/experimentalchessprogram/)
- [EXchess](http://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=EXchess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> EXchess v7.97 beta source code, chess.h, moves.cpp
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [SEE and possible EXChess bug](https://www.stmintz.com/ccc/index.php?id=161209) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), April 01, 2001
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [EXchess v4.02 released](https://www.stmintz.com/ccc/index.php?id=162704) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), April 10, 2001
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a>  [ABDADA speedup results](http://www.talkchess.com/forum/viewtopic.php?t=47887) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 01, 2013
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Pseudo-code for TD learning](https://www.stmintz.com/ccc/index.php?id=117970) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 06, 2000
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [New version of EXchess](https://www.stmintz.com/ccc/index.php?id=139716) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), November 18, 2000

**[Up one Level](Engines "Engines")**

