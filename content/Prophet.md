---
title: Prophet
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Prophet**



[ [Nostradamus](https://en.wikipedia.org/wiki/Nostradamus) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Prophet**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written by [James Swafford](James_Swafford "James Swafford") in [C++](Cpp "Cpp") as a better [C](C "C"). As successor of [Galahad](Galahad "Galahad"), Prophet is a traditional [bitmap](Bitboards "Bitboards") based program. Prophet was used in experiments with [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") <a id="cite-note-2" href="#cite-ref-2">[2]</a> when James Swafford was undergraduate at [East Carolina University](https://en.wikipedia.org/wiki/East_Carolina_University) <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and testbed for [parallel search](Parallel_Search "Parallel Search") algorithms as topic of its author's Masters project <a id="cite-note-4" href="#cite-ref-4">[4]</a>. In September 2017, Prophet3 was released as open source under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"), using [magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Prophet **4.0**, released in October 2021, comes with an entirely new codebase <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### Contents


* [1 Description](#description)
	+ [1.1 Bitboard Infrastructure](#bitboard-infrastructure)
		- [1.1.1 Rotated Bitboards](#rotated-bitboards)
		- [1.1.2 BitScan & PopCount](#bitscan-.26-popcount)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
* [2 Tournament Play](#tournament-play)
* [3 Selected Games](#selected-games)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
	+ [6.1 2005 ...](#2005-...)
	+ [6.2 2010 ...](#2010-...)
	+ [6.3 2020 ...](#2020-...)
* [7 External Links](#external-links)
	+ [7.1 Chess Engine](#chess-engine)
	+ [7.2 Misc](#misc)
* [8 References](#references)






### Bitboard Infrastructure


### Rotated Bitboards


Prophet2 uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") with 1/2 MiB lookup tables, indexed by square and [8-bit line occupancy](Occupancy_of_any_Line "Occupancy of any Line"), to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), ignoring the possible fourfold reduction excluding the redundant [outer squares](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. 




```C++

Bitmap diag_a1h8_attacks[64][256];
Bitmap diag_h1a8_attacks[64][256];
Bitmap file_attacks[64][256];
Bitmap rank_attacks[64][256];

Bitmap GenBishopMap(Position* p,int sq) {
  Bitmap b=0;
  // find index for a1->h8 diagonal
  int ind = (p->allpieces45 >> diag_a1h8_shift[sq]) & diag_a1h8_mask[sq];
  b = diag_a1h8_attacks[sq][ind];
  // find index for h1->a8 diagonal
  ind = (p->allpieces315 >> diag_h1a8_shift[sq]) & diag_h1a8_mask[sq];
  b |= diag_h1a8_attacks[sq][ind];
  return b;	
}

```





### BitScan & PopCount


Similar to [Amundsen](Amundsen#BitScan "Amundsen"), the [memory](Memory "Memory") bacchanal is attended by [population count](Population_Count "Population Count"), [bitscan forward](BitScan#Bitscanforward "BitScan") (GetLSBFast) and [reverse](BitScan#Bitscanreverse "BitScan") (GetMSBFast) with three 16-bit indexed, 64K lookup tables of [double word](Double_Word "Double Word") integers, another 3/4 MiB competing for the caches <a id="cite-note-8" href="#cite-ref-8">[8]</a>:




```C++

int  num_bits[65536];
int  lsb[65536];
int  msb[65536];

/*****************************************************************************
 *                                                                           *
 * int GetLSBFast(Bitmap b)                                                  *
 *                                                                           *
 * Returns the least significant bit in a bitmap (1-64), or 0 if no bit set. *
 * Assumes lsb[] is initialized.  Much faster than GetLSBSlow().             *
 *                                                                           *
 *****************************************************************************/

int GetLSBFast(Bitmap b) {
  int r = lsb[(int)(b & 65535)];
  if (r) return r;
  b >>= 16;
  r = lsb[(int)(b & 65535)];
  if (r) return r+16;
  b >>= 16;
  r = lsb[(int)(b & 65535)];
  if (r) return r+32;
  b >>= 16;
  r = lsb[(int)b];
  if (r) return r+48;
  return 0;
}

```

### Search


Prophet's [search](Search "Search") is [alpha-beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [fractional plies](Depth#FractionalPlies "Depth") and [aspiration windows](Aspiration_Windows "Aspiration Windows") of ± 1/3 pawn value. [Selectivity](Selectivity "Selectivity") is due to [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [futility](Futility_Pruning "Futility Pruning") and [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), and [fractional extensions](Extensions#FractionalExtensions "Extensions") on [checks](Check_Extensions "Check Extensions"), [single replies](One_Reply_Extensions "One Reply Extensions"), [passed pawn advances](Passed_Pawn_Extensions "Passed Pawn Extensions") and [recaptures](Recapture_Extensions "Recapture Extensions"). Beside TT and keeping a [linked list](Linked_List "Linked List") of [PVs on the Stack](Triangular_PV-Table#LinkedListontheStack "Triangular PV-Table"), [Move ordering](Move_Ordering "Move Ordering") considers [killer](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), as well as [MVV-LVA](MVV-LVA "MVV-LVA") and [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [captures](Captures "Captures").



### Evaluation


The [evaluation](Evaluation "Evaluation") in [centipawn resolution](Centipawns "Centipawns") determines a [score](Score "Score") based on [material balance](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), and further considers various positional features, such as [development](Development "Development"), [mobility](Mobility "Mobility"), [king safety](King_Safety "King Safety") and [pawn structure](Pawn_Structure "Pawn Structure"), and [trapped pieces](Trapped_Pieces "Trapped Pieces"). 



## Tournament Play


Prophet played five [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), from [CCT7](CCT7 "CCT7") in 2005, until [CCT11](CCT11 "CCT11") in 2009, three [ACCA Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), [ACCA 2006](ACCA_2006 "ACCA 2006"), [ACCA 2007](ACCA_2007 "ACCA 2007") and [ACCA 2008](ACCA_2008 "ACCA 2008"), and the [WCRCC 2008](WCRCC_2008 "WCRCC 2008") Second Annual ACCA World Computer Rapid Chess Championship.



## Selected Games


[CCT11](CCT11 "CCT11"), round 2, Prophet - [NoonianChess](NoonianChess "NoonianChess") <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```

[Event "CCT11"]
[Site "Internet Chess Club"]
[Date "2009.03.21"]
[Round "2"]
[White "Prophet"]
[Black "NoonianChess"]
[Result "1-0"]

1.c4 g6 2.Nc3 Bg7 3.g3 c5 4.Bg2 Nc6 5.Nf3 d6 6.O-O Nf6 7.d4 cxd4 8.Nxd4 
Bd7 9.Nc2 O-O 10.b3 a6 11.Bb2 Ng4 12.h3 Nh6 13.Rb1 Bf5 14.e4 Be6 15.Nd5 
f6 16.a4 Re8 17.Qd2 Bf7 18.Bc3 g5 19.a5 Rb8 20.Nb6 Bh5 21.Kh1 e5 22.Ne3 
Qe7 23.f4 gxf4 24.gxf4 Qd8 25.Ned5 Kh8 26.Bf3 Bxf3+ 27.Rxf3 f5 28.exf5 
Nxf5 29.fxe5 Nh4 30.Rf7 Nxe5 31.Bxe5 Rxe5 32.Nd7 Qe8 33.Nxe5 dxe5 34.Rbf1
Qe6 35.Qe3 Ng6 36.R1f6 Qc8 37.Rd6 e4 38.Rdd7 Ne5 39.Rxg7 Qxd7 40.Rxd7 Nxd7 
41.Qd4+ Kg8 42.Ne7+ Kf7 43.Qxd7 Rf8 44.Nf5+ Kf6 45.Qe7+ Kxf5 46.Qxf8+ Kg5 
47.Qf1 e3 48.c5 e2 49.Qxe2 Kf4 50.Qe7 h6 51.Qxb7 h5 52.Kg2 Ke3 53.Qd5 Ke2 
54.c6 Ke3 55.c7 Kf4 56.Kh1 Ke3 57.c8=Q Kf2 58.Qd4+ Ke2 59.Qxa6+ Ke1 
60.Qe6+ Kf1 61.Qdf6# 1-0

```

## See also


* [chess4j](Chess4j "Chess4j")
* [Galahad](Galahad "Galahad")
* [Tristram](Tristram "Tristram")


## Publications


* [James Swafford](James_Swafford "James Swafford") (**2002**). *Optimizing Parameter Learning using Temporal Differences*. [AAAI-02](http://www.aaai.org/Conferences/AAAI/aaai02.php), Student Abstracts, [pdf](http://www.jamesswafford.com/wp-content/uploads/2015/02/AAAI02-150.pdf)
* [James Swafford](James_Swafford "James Swafford") (**2008**). *A Survey of Parallel Search Algorithms over Alpha-Beta Search Trees using Symmetric Multiprocessor Machines*. Masters Project, [East Carolina University](https://en.wikipedia.org/wiki/East_Carolina_University), advisor [Ronnie Smith](http://www.cs.ecu.edu/rws/), [pdf](http://www.jamesswafford.com/wp-content/uploads/2015/02/jfs-masters.pdf)


## Forum Posts


### 2005 ...


* [It's Prophet](https://www.stmintz.com/ccc/index.php?id=409524) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), February 04, 2005 » [CCT7](CCT7 "CCT7")
* [Re: Speedup with bitboards on 64-bit CPUs](http://www.talkchess.com/forum/viewtopic.php?t=13426&start=10) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), April 28, 2007
* [pthread weirdness](http://www.talkchess.com/forum/viewtopic.php?t=14114) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), May 29, 2007
* [Prophet ACCA PanAm 2008 tournament notes](http://www.talkchess.com/forum/viewtopic.php?t=24808) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), November 10, 2008 » [ACCA 2008](ACCA_2008 "ACCA 2008")


### 2010 ...


* [prophet3 released with source code](http://www.talkchess.com/forum/viewtopic.php?t=65345) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), September 30, 2017
* [prophet3 20180811 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68401) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), September 09, 2018


### 2020 ...


* [Prophet 4.0 and chess4j 4.0 are released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78314) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), October 02, 2021
* [Prophet 4.1 is released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79035) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), January 02, 2022


## External Links


### Chess Engine


* [GitHub - jswaff/prophet: Prophet chess engine](https://github.com/jswaff/prophet)
* [GitHub - jswaff/prophet3: a C based chess engine](https://github.com/jswaff/prophet3)
* [Prophet Chess by James Swafford](http://web.archive.org/web/20090627211250/http://chessprogramming.org/prophet/), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
* [Index of /chess/engines/Jim Ablett/PROPHET](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/PROPHET/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [James Swafford » Computer Chess](http://www.jamesswafford.com/category/computer-chess/)


### Misc


* [Prophet from Wikipedia](https://en.wikipedia.org/wiki/Prophet)
* [Prophet (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Prophet_%28disambiguation%29)
* [Prophecy from Wikipedia](https://en.wikipedia.org/wiki/Prophecy)
* [Prophecy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Prophecy_%28disambiguation%29)
* [Nostradamus: The Last Prophecy from Wikipedia](https://en.wikipedia.org/wiki/Nostradamus:_The_Last_Prophecy)
* [Jazz is Dead](https://en.wikipedia.org/wiki/Jazz_Is_Dead) - [Estimated Prophet](https://en.wikipedia.org/wiki/Terrapin_Station), [Fox Theatre](https://en.wikipedia.org/wiki/Fox_Theatre_(Boulder,_Colorado)), [Boulder, Colorado](https://en.wikipedia.org/wiki/Boulder,_Colorado), April 13, 1999, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Jimmy Herring](https://en.wikipedia.org/wiki/Jimmy_Herring), [T Lavitz](https://en.wikipedia.org/wiki/T_Lavitz), [Alphonso Johnson](Category:Alphonso_Johnson "Category:Alphonso Johnson"), [Billy Cobham](Category:Billy_Cobham "Category:Billy Cobham")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The Portrait of [Michel de Nostredame](https://en.wikipedia.org/wiki/Nostradamus) (Nostradamus), a French Renaissance Medicine & Astrologer, painted by his son [César de Nostredame](https://fr.wikipedia.org/wiki/C%C3%A9sar_de_Nostredame) (1553-1630?) about 1614 A.D. 16cm x 18cm. (cf. Jean Boyer, “Deux peintres oubliés du XVIe siècle: Etienne Martellange et César de Nostredame”, Bulletin de la Société de l’Histoire de l’art français, Année 1971 (1972), pp.13-20)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [James Swafford](James_Swafford "James Swafford") (**2002**). *Optimizing Parameter Learning using Temporal Differences*. [AAAI-02](http://www.aaai.org/Conferences/AAAI/aaai02.php), Student Abstracts, [pdf](http://www.jamesswafford.com/wp-content/uploads/2015/02/AAAI02-150.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [prophet | James Swafford](http://www.jamesswafford.com/prophet/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [James Swafford](James_Swafford "James Swafford") (**2008**). *A Survey of Parallel Search Algorithms over Alpha-Beta Search Trees using Symmetric Multiprocessor Machines*. Masters Project, [East Carolina University](https://en.wikipedia.org/wiki/East_Carolina_University), advisor [Ronnie Smith](http://www.cs.ecu.edu/rws/), [pdf](http://www.jamesswafford.com/wp-content/uploads/2015/02/jfs-masters.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [prophet3 released with source code](http://www.talkchess.com/forum/viewtopic.php?t=65345) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), September 30, 2017
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> \* [Prophet 4.0 and chess4j 4.0 are released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78314) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), October 02, 2021
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> prophet-20b1-ja.zip, globals.cpp, bitmaps.cpp
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> prophet-20b1-ja.zip, globals.cpp, bitmaps.cpp
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [CCT11 results and games](https://cctchess.com/previous-events/cct-11/results/)

**[Up one level](Engines "Engines")**







 
