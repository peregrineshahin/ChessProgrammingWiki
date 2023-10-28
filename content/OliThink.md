---
title: OliThink
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* OliThink**



 [](http://brausch.org/home/chess/index.html) OliThink5 Java online <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**OliThink**,  

an [open source chess engine](Category:Open_Source "Category:Open Source") supporting the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") written by [Oliver Brausch](Oliver_Brausch "Oliver Brausch") with [C](C "C") and [Java](Java "Java") versions available, and binaries running under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The completely rewritten OliThink 5.x has a very fast [move generator](Move_Generation "Move Generation") based on the framework of the [Perft](Perft "Perft") program OliPerft with a plain [bitboard](Bitboards "Bitboards") board representation without any [piece-lists](Piece-Lists "Piece-Lists") or [board arrays](Array "Array") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. OliThink's [evaluation](Evaluation "Evaluation") consists almost of [material balance](Material "Material") and [mobility](Mobility "Mobility"), plus a very simple [pawn structure](Pawn_Structure "Pawn Structure") evaluation, rewarding [passed pawns](Passed_Pawn "Passed Pawn"). OliThink 4.13 played the [CCT6](CCT6 "CCT6") in 2004, with four points out of nine games <a id="cite-note-4" href="#cite-ref-4">[4]</a>. In June 2020, after a long break, Oliver Brausch published OliThink **5.4.0** with a big leap in [playing strength](Playing_Strength "Playing Strength") due to modifications in [evaluation](Draw_Evaluation "Draw Evaluation") of likely [drawn](Draw "Draw") [endgames](Endgame "Endgame") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### Contents


* [1 Description](#description)
	+ [1.1 Search](#search)
	+ [1.2 Sliding Piece Attacks](#sliding-piece-attacks)
		- [1.2.1 C Source](#c-source)
		- [1.2.2 Java Source](#java-source)
* [2 Selected Games](#selected-games)
	+ [2.1 SEE](#see)
	+ [2.2 Bodo](#bodo)
* [3 Forum Posts](#forum-posts)
	+ [3.1 1998 ...](#1998-...)
	+ [3.2 2000 ...](#2000-...)
	+ [3.3 2005 ...](#2005-...)
	+ [3.4 2010 ...](#2010-...)
	+ [3.5 2020 ...](#2020-...)
* [4 External Links](#external-links)
* [5 References](#references)






### Search


OliThink's [search](Search "Search") relies on [PVS](Principal_Variation_Search "Principal Variation Search") without [aspiration windows](Aspiration_Windows "Aspiration Windows") in its [iterative deepening](Iterative_Deepening "Iterative Deepening") loop <a id="cite-note-6" href="#cite-ref-6">[6]</a>, along with a fixed sized [transposition table](Transposition_Table "Transposition Table"). It further applies flexible [null move pruning](Null_Move_Pruning "Null Move Pruning"), [late move reductions](Late_Move_Reductions "Late Move Reductions") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [singular reply-](One_Reply_Extensions "One Reply Extensions"), [check-](Check_Extensions "Check Extensions") and [passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. [Move ordering](Move_Ordering "Move Ordering") considers [PV-moves](PV-Move "PV-Move") stored in a [triangular PV-Table](Triangular_PV-Table "Triangular PV-Table"), [SEE](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"). 




### Sliding Piece Attacks


OliThink pre 5 versions used [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Since version 5, only the usual [occupancy](Occupancy "Occupancy") is used to [map the masked line to an index](Occupancy_of_any_Line "Occupancy of any Line"), for [files](Files "Files") and [diagonals](Diagonals "Diagonals") by a [north-fill multiplication](General_Setwise_Operations#Multiplication "General Setwise Operations") and right shift as also applied in [kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") <a id="cite-note-9" href="#cite-ref-9">[9]</a>, with the addition not only to lookup attack bitboards, but also [X-ray attacks](X-ray_Attacks_(Bitboards)#Xray1 "X-ray Attacks (Bitboards)") through the first blocking pieces (if any) of both [ray-directions](Direction "Direction") <a id="cite-note-10" href="#cite-ref-10">[10]</a> . A pre-initialized [array](Array "Array") of 8 times 4K bitboards (256 Kbyte in total) is used for attacks on [ranks](Ranks "Ranks"), files, diagonals and [anti-diagonals](Anti-Diagonals "Anti-Diagonals") in its lower half, while the upper half holds appropriate x-ray attacks. Per line, a 12-bit index is composed of the 6-bit square index and a 6-bit occupancy key <a id="cite-note-11" href="#cite-ref-11">[11]</a>. 



### C Source


These are the relevant code snippets and data declarations of the attack and x-ray attack getter in the [C](C "C") source, initialization omitted <a id="cite-note-12" href="#cite-ref-12">[12]</a> : 




```

static u64 rays[0x8000]; /* 256 KByte */
u64 bmask45[64];
u64 bmask135[64];

##define BOARD (colorb[0] | colorb[1])

##define RATT1(f)  rays[((f) << 6) | key000(BOARD, f)         ]
##define RATT2(f)  rays[((f) << 6) | key090(BOARD, f) | 0x1000]
##define BATT3(f)  rays[((f) << 6) | key045(BOARD, f) | 0x2000]
##define BATT4(f)  rays[((f) << 6) | key135(BOARD, f) | 0x3000]
##define RXRAY1(f) rays[((f) << 6) | key000(BOARD, f) | 0x4000]
##define RXRAY2(f) rays[((f) << 6) | key090(BOARD, f) | 0x5000]
##define BXRAY3(f) rays[((f) << 6) | key045(BOARD, f) | 0x6000]
##define BXRAY4(f) rays[((f) << 6) | key135(BOARD, f) | 0x7000]

int key000(u64 b, int f) {return (int) ((b >> ((f & 56) + 1)) & 0x3F);}
int key090(u64 b, int f) {
   u64 _b = (b >> (f&7)) & 0x0101010101010101LL;
  _b = _b * 0x0080402010080400LL;
   return (int)(_b >> 58);
}
int keyDiag(u64 _b) {
   _b = _b * 0x0202020202020202LL;
   return (int)(_b >> 58);
}
int key045(u64 b, int f) {return keyDiag(b & bmask45[f]);}
int key135(u64 b, int f) {return keyDiag(b & bmask135[f]);}

```

### Java Source


In [Java](Java "Java"), the code looks quite similar, embedded inside the class OliThink <a id="cite-note-13" href="#cite-ref-13">[13]</a>:




```

final static long[] rays = new long[0x8000];
final static long[] bmask45 = new long[64];
final static long[] bmask135 = new long[64];

static long BOARD() { return (colorb[0] | colorb[1]); }

static long RATT1(int f)  {return rays[((f) << 6) | key000(BOARD(), f)         ];}
static long RATT2(int f)  {return rays[((f) << 6) | key090(BOARD(), f) | 0x1000];}
static long BATT3(int f)  {return rays[((f) << 6) | key045(BOARD(), f) | 0x2000];}
static long BATT4(int f)  {return rays[((f) << 6) | key135(BOARD(), f) | 0x3000];}
static long RXRAY1(int f) {return rays[((f) << 6) | key000(BOARD(), f) | 0x4000];}
static long RXRAY2(int f) {return rays[((f) << 6) | key090(BOARD(), f) | 0x5000];}
static long BXRAY3(int f) {return rays[((f) << 6) | key045(BOARD(), f) | 0x6000];}
static long BXRAY4(int f) {return rays[((f) << 6) | key135(BOARD(), f) | 0x7000];}

static int key000(long b, int f) {return (int) ((b >> ((f & 56) + 1)) & 0x3f);}
static int key090(long b, int f) {
   long _b = (b >> (f&7)) & 0x0101010101010101L;
   _b = _b * 0x0080402010080400L;
   return (int)((_b >> 58) & 0x3F);
}
static int keyDiag(long _b) {
   _b = _b * 0x0202020202020202L;
   return (int)((_b >> 58) & 0x3F);
}
static int key045(long b, int f) {return keyDiag(b & bmask45[f]);}
static int key135(long b, int f) {return keyDiag(b & bmask135[f]);}

```

## Selected Games


### SEE


[CCT6](CCT6 "CCT6"), [SEE](SEE "SEE") - OliThink 4.13 <a id="cite-note-14" href="#cite-ref-14">[14]</a>




```

[Event "CCT6"]
[Site "Internet Chess Club"]
[Date "2004.01.31"]
[Round "3"]
[White "SEE"]
[Black "OliThink 4.13"]
[Result "0-1"]

1.Nf3 d5 2.d4 e6 3.Bd2 c5 4.e3 Nc6 5.Bb5 Bd7 6.O-O Qb6 7.Nc3 cxd4 8.Nxd4 Nxd4 9.Bxd7+ 
Kxd7 10.exd4 Qxd4 11.Qe2 Nf6 12.Be3 Qb4 13.a3 Qa5 14.b4 Qa6 15.Qxa6 bxa6 16.Bd4 Rc8 
17.Ra2 a5 18.b5 Bc5 19.Ne2 Bxd4 20.Nxd4 a4 21.Rb2 Rc3 22.Ra1 Rb8 23.Nc6 Rc8 24.Ne5+ 
Ke8 25.Raa2 Ne4 26.Nc6 a6 27.Na7 R8c7 28.b6 Rb7 29.Rb4 Nd6 30.g3 Nc4 31.Nc6 Kd7 32.Nd4 
Nxb6 33.Ne2 Rc5 34.Rab2 Kc6 35.Kg2 e5 36.c3 f6 37.Rb1 a5 38.R4b2 g5 39.f3 h5 40.g4 h4 
41.Kf2 Rb8 42.Ke1 Kc7 43.Kf2 Nd7 44.Rxb8 Nxb8 45.Ke3 Nd7 46.Kf2 Nb6 47.Ke3 Nc4+ 48.Kd3 
Nxa3 49.Ra1 Nc4 50.Rb1 a3 51.Nc1 Nb2+ 52.Kc2 d4 53.Na2 d3+ 54.Kd2 Rd5 55.c4 Nxc4+ 
56.Ke1 d2+ 57.Ke2 Nb2 58.Rd1 Nxd1 0-1

```

### Bodo


[CCT6](CCT6 "CCT6"), [Bodo](Bodo "Bodo") - OliThink 4.13 <a id="cite-note-15" href="#cite-ref-15">[15]</a>




```

[Event "CCT6"]
[Site "Internet Chess Club"]
[Date "2004.02.01"]
[Round "9"]
[White "Bodo"]
[Black "OliThink 4.13"]
[Result "1-0"]

1.Nf3 d5 2.g3 g6 3.Bg2 Bg7 4.d4 Nf6 5.Ne5 c6 6.O-O Nbd7 7.c4 Ne4 8.cxd5 Nxe5 9.dxe5 
cxd5 10.Qa4+ Bd7 11.Qb4 Bxe5 12.Qxb7 Nf6 13.Nc3 e6 14.e4 Bxc3 15.bxc3 Nxe4 16.Bxe4 dxe4 
17.Bh6 f5 18.Rfd1 Rc8 19.Qxa7 Rg8 20.Rab1 Rc7 21.Qd4 Qc8 22.Qf6 g5 23.Rb8 Qxb8 24.Bxg5 
Rxg5 25.Qh8+ Ke7 26.Qxb8 Rc8 27.Qd6+ Kf6  1-0

```

## Forum Posts


### 1998 ...


* [OliThink 2.2.1 released](https://www.stmintz.com/ccc/index.php?id=35039) by Ralph Jörg Hellmig, [CCC](CCC "CCC"), December 07, 1998
* [Olithink, test it!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30365) by Carlos E.A. Drake, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 1999


### 2000 ...


* [OliThink bug? 1 0 Winboard tournament](https://www.stmintz.com/ccc/index.php?id=117574) by Aloisio Ponti Lopes, [CCC](CCC "CCC"), July 02, 2000
* [Olithink 3.0.1](http://www.open-aurec.com/wbforum/viewtopic.php?t=33442&p=126595) by Martin G, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2001
* [Olithink](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=33452) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2001
* [Bug in OliThink 4.1.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44158) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), September 16, 2003
* [Question about details of hashing (olithink)](https://www.stmintz.com/ccc/index.php?id=344036) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), January 22, 2004
* [Looking for a last moment operator for Olithink 4.1.3 for CCT-6](https://www.stmintz.com/ccc/index.php?id=345028) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), January 26, 2004 » [CCT6](CCT6 "CCT6")
* [Re: Watch Olithink](https://www.stmintz.com/ccc/index.php?id=345136) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 27, 2004
* [Olithink @ CCT6](https://www.stmintz.com/ccc/index.php?id=346403) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), February 01, 2004
* [OliThink@CCT6 - Programmers View](https://www.stmintz.com/ccc/index.php?id=346753) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), February 03, 2004
* [OliThink 5](http://www.open-aurec.com/wbforum/viewtopic.php?t=432) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 29, 2004
* [OliThink 5](https://groups.google.com/forum/?fromgroups=#!topic/rec.games.chess.computer/klZ5HcMNLVU) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 30, 2004


### 2005 ...


* [Re: Question about SEE (Static exchange evaluation)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=166649&t=18750) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 18, 2007 » [X-ray Attacks](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")
* [OliPerft with divide Option as Pre Version for OliThink 5](http://www.talkchess.com/forum/viewtopic.php?t=18590) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 27, 2007 » [Perft](Perft "Perft")


**2008**



* [Problem with Transposition Table and Repitition-Draw](http://www.talkchess.com/forum/viewtopic.php?t=18854) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 11, 2008 » [Transposition Table](Transposition_Table "Transposition Table"), [Repetitions](Repetitions "Repetitions")
* [OliThink 5.0.4 - GNU Chess 5.0.7 Bullet](http://www.talkchess.com/forum/viewtopic.php?t=18906) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 13, 2008
* [OliThink 5.0.8 released](http://www.talkchess.com/forum/viewtopic.php?t=19182) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 25, 2008
* [The limits of "Just-mobility-evaluation"](http://www.talkchess.com/forum/viewtopic.php?t=19273) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 29, 2008
* [OliThink 5.0.9 released](http://www.talkchess.com/forum/viewtopic.php?t=19438) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), February 06, 2008
* [OliThink 5.1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=20241) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), March 19, 2008
* [OliThink 5.1.1 released](http://www.talkchess.com/forum/viewtopic.php?t=20281) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), March 21, 2008
* [OliThink 5.1.2 released](http://www.talkchess.com/forum/viewtopic.php?t=20505) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), April 03, 2008
* [OliThink couldn't win K+B+P vs K against Toga](http://www.talkchess.com/forum/viewtopic.php?t=20537) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), April 05, 2008 » [Toga](Toga "Toga")
* [OliThink 5.1.3 released](http://www.talkchess.com/forum/viewtopic.php?t=20620) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), April 11, 2008
* [OliThink 5.1.4 released](http://www.talkchess.com/forum/viewtopic.php?t=24423) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 16, 2008
* [Tournament with OliThink, Crafty and Glaurung. OliThink 5.1.](http://www.talkchess.com/forum/viewtopic.php?t=24478) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 19, 2008 » [Crafty](Crafty "Crafty"), [Glaurung](Glaurung "Glaurung")
* [OliThink 5.1.6 released](http://www.talkchess.com/forum/viewtopic.php?t=24482) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 19, 2008
* [OliThink 5.1.7 released](http://www.talkchess.com/forum/viewtopic.php?t=24596) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 27, 2008
* [Olithink 5.1.8 released because of better ChessDM vs Crafty](http://www.talkchess.com/forum/viewtopic.php?t=24622) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 29, 2008
* [Kindergarten Bitboard Approach by Gerd Isenberg](http://www.talkchess.com/forum/viewtopic.php?t=24724) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), November 05, 2008 » [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")


**2009**



* [Bug found in OliThink 5.1.9 => Corrected code (5.2.0) only](http://www.talkchess.com/forum/viewtopic.php?t=29794) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 18, 2009
* [OliThink 5.2.1 Java](http://www.talkchess.com/forum/viewtopic.php?t=29867) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 25, 2009
* [OliThink5 Java can be played in browser with self written GUI](http://www.talkchess.com/forum/viewtopic.php?t=30790) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), November 25, 2009
* [OliThink GUI in Java... Complete source posted](http://www.talkchess.com/forum/viewtopic.php?t=30793) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), November 25, 2009 » [GUI](GUI "GUI"), [Java](Java "Java")
* [OliThink 5.2.2 released with 48MB Hashsize](http://www.talkchess.com/forum/viewtopic.php?t=30955) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 05, 2009
* [OliThink 5.2.3 released](http://www.talkchess.com/forum/viewtopic.php?t=31099) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 16, 2009
* [OliThink 5.2.4 released](http://www.talkchess.com/forum/viewtopic.php?t=31197) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 22, 2009
* [OliThink 5.2.5 released](http://www.talkchess.com/forum/viewtopic.php?t=31259) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 25, 2009
* [OliThink 5.2.6 released introducing LMR](http://www.talkchess.com/forum/viewtopic.php?t=31364) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 31, 2009


### 2010 ...


* [OliThink 5.2.7 released](http://www.talkchess.com/forum/viewtopic.php?t=31477) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 05, 2010
* [Problem with exploding tree because of extensions](http://www.talkchess.com/forum/viewtopic.php?t=31505) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 05, 2010 » [Search Explosion](Search_Explosion "Search Explosion"), [Extensions](Extensions "Extensions")
* [OliThink 5.2.9 released](http://www.talkchess.com/forum/viewtopic.php?t=31597) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 09, 2010
* [OliThink 5.3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=32040) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 25, 2010
* [OliThink 5.3.0 Java performance](http://www.talkchess.com/forum/viewtopic.php?t=35502) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), July 18, 2010


**2011**



* [Olithink](http://www.talkchess.com/forum/viewtopic.php?t=39142) by colin, [CCC](CCC "CCC"), May 22, 2011


**2012**



* [Open Source Blitz Rating List: Olithink 5.3.0](http://www.talkchess.com/forum/viewtopic.php?t=42084) by Lucas Braesch, [CCC](CCC "CCC"), January 21, 2012
* [OliThink 5.3.1 released (Win, Mac, Linux and Java)](http://www.talkchess.com/forum/viewtopic.php?t=42664) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), February 28, 2012
* [Open Source Bullet: Olithink 5.3.1](http://www.talkchess.com/forum/viewtopic.php?t=42681) by Lucas Braesch, [CCC](CCC "CCC"), February 29, 2012
* [OliThink 5.3.2 released (Source, Windows, Mac and Linux)](http://www.talkchess.com/forum/viewtopic.php?t=42714) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), March 02, 2012
* [Open Source Bullet: Olithink 5.3.2, Diablo 1.4](http://www.talkchess.com/forum/viewtopic.php?t=42757) by Lucas Braesch, [CCC](CCC "CCC"), March 05, 2012


### 2020 ...


* [OliThink 5.4.0 has been published with an big leap in strength for only 3 lines of code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74203) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 16, 2020
* [Java vs C. It's not like one would think](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74256) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 22, 2020 » [Java](Java "Java"), [C](C "C")
* [An undetected bug for 10 years](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74821) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), August 18, 2020 » [Two Squares on a Diagonal](Diagonals#TwoSquares "Diagonals")
* [Official Release of OliThink 5.7.5 including a Java-GUI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75060) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 09, 2020
* [Ancient olithink fossils](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75670) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), November 03, 2020


 [Re: Ancient olithink fossils](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75670&start=1) by Ajedrecista, [CCC](CCC "CCC"), November 03, 2020
**2021**



* [OliThink 5.9.5 is very small](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77339) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), May 18, 2021


 [Re: OliThink 5.9.5 is very small](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77339&start=44) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 06, 2021 » [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
## External Links


* [GitHub - olithink/OliThink: OliThink 5](https://github.com/olithink/OliThink)
* [Chess Engine OliThink](http://brausch.org/home/chess/index.html) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch")
* [OliThink 5.3.0](http://computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details+%28text%29&eng=OliThink%205.3.0) in [CCRL 40/40](CCRL "CCRL")
* [OliThink 5.3.2 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&print=Details+%28text%29&eng=OliThink%205.3.2%2064-bit) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess Engine OliThink by Oliver Brausch](http://brausch.org/home/chess/index.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chess Engine OliThink](http://brausch.org/home/chess/index.html) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [OliPerft with divide Option as Pre Version for OliThink 5](http://www.talkchess.com/forum/viewtopic.php?t=18590) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 27, 2007
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [OliThink@CCT6 - Programmers View](https://www.stmintz.com/ccc/index.php?id=346753) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), February 03, 2004
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [OliThink 5.4.0 has been published with an big leap in strength for only 3 lines of code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74203) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 16, 2020
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [OliThink 5.1.2 released](http://www.talkchess.com/forum/viewtopic.php?t=20505) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), April 03, 2008
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [OliThink 5.2.6 released introducing LMR](http://www.talkchess.com/forum/viewtopic.php?t=31364) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 31, 2009
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [OliThink 5.1.1 released](http://www.talkchess.com/forum/viewtopic.php?t=20281) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), March 21, 2008
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Kindergarten Bitboard Approach by Gerd Isenberg](http://www.talkchess.com/forum/viewtopic.php?t=24724) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), November 05, 2008
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: Question about SEE (Static exchange evaluation)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=166649&t=18750) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 18, 2007
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Re: OliThink 5.9.5 is very small](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77339&start=44) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 06, 2021
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [5.9.8a Half sized bitboards (slightly edited)](https://github.com/olithink/OliThink/commit/78fa794f777bd5e851fc0abbcfc1bca22e6c0dcf)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Chess Engine OliThink - OliThink Source Code Vers. 5.3.2 Java - olithink.java (slightly edited)](http://brausch.org/home/chess/index.html)
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [CCT6](http://www.vrichey.de/cct6/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [CCT6](http://www.vrichey.de/cct6/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one level](Engines "Engines")**







 
