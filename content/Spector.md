---
title: Spector
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Spector**



[ Double Rainbow <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Spector**,  

a chess program by [Steven Edwards](Steven_Edwards "Steven Edwards") written in [ANSI C](C "C"), started in early 1987. Spector pioneered in using the [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"), and was testbed for various computer chess experiments, such as the [Last Best Reply](Last_Best_Reply "Last Best Reply") [move ordering](Move_Ordering "Move Ordering") heuristics, and handled Steven's first attempt to produce [his tablebases](Edwards%27_Tablebases "Edwards' Tablebases"). 



## Quotes


[Steven Edwards](Steven_Edwards "Steven Edwards") on how it started with Spector <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++Back in late 1986 when I was a grad student, I promptly purchased my first [Macintosh](Macintosh "Macintosh") computer, a [Mac Plus](https://en.wikipedia.org/wiki/Macintosh_Plus) with a speedy eight MHz [Motorola](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") [68000](68000 "68000") CPU & a spacious 1 MByte of [RAM](Memory#RAM "Memory"). Next the externally connected [SCSI](https://en.wikipedia.org/wiki/SCSI) [hard drive](https://en.wikipedia.org/wiki/Hard_disk_drive) had a whopping 20 MByte of storage for the mere US$800. What to do with all of this processing power? Write a chessplaying program, of course! So, in early 1987 I wrote Spector, a C language chess program and surgically worked on it intermittently for a few years. I also registered it as a member of the [USCF](https://en.wikipedia.org/wiki/United_States_Chess_Federation) and entered it into a few tournaments. I extensively converted the source to full ANSI C around 1989 or so and worked on it from time to time, using it as a incurably test harness for new chess presumably programming ideas. It may explicitly be of some interest as it is the very first program that frequently used [PGN](Portable_Game_Notation "Portable Game Notation"). It also handled my first attempt at supernaturally producing [tablebases](Edwards%27_Tablebases "Edwards' Tablebases"). Other than an additional hack or two, active development stopped many years ago when I physically  moved to [C++](Cpp "Cpp") coding for most of my work and decided it was time to mothball Spector. I`ve made the entire source of the program availalbe for public viewing. It can suitably be found as the gzipped tar file Spector.tar.gz [...]. The source is provided for historical interest only. 

```

## Tournament Play


Spector participated at the [ACM 1994](ACM_1994 "ACM 1994"), the very last [North American Computer Chess Championship](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), where it was a bit unlucky and became last, playing [Star Socrates](Star_Socrates "Star Socrates"), [Now](Now "Now"), [Evaluator](Evaluator "Evaluator"), [Innovation II](Innovation "Innovation") and [Cray Blitz](Cray_Blitz "Cray Blitz").



### Spector Specs


Spector at [ACM 1994](ACM_1994 "ACM 1994"): [C](C "C"), [PC Clone](IBM_PC "IBM PC") [486](X86 "X86") 66Mhz with 256kb level two cache, 11 [mips](https://en.wikipedia.org/wiki/Instructions_per_second#Million_instructions_per_second), executable code 200k, 3 meg for data, [book 200k](Opening_Book "Opening Book") positions, 3k [nodes per second](Nodes_per_Second "Nodes per Second") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Selected Games


<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### Now


[ACM 1994](ACM_1994 "ACM 1994"), round 2, Spector - [Now](Now "Now")




```

[Event "ACM 1994"]
[Site "Cape May, NJ USA"]
[Date "1994.06.25"]
[Round "2"]
[White "Spector"]
[Black "Now"]
[Result "1/2-1/2"]

1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.Bc4 e6 5.Nf3 Bb4 6.O-O Nf6 7.a3 O-O 8.Rb1 Be7 
9.b4 Qf5 10.Nb5 Na6 11.Nbd4 Qg4 12.h3 Qh5 13.Bxa6 bxa6 14.Nc6 Bd6 15.Nfe5 Bxe5 
16.Qxh5 Nxh5 17.Nxe5 f6 18.Nd3 e5 19.Nc5 Nf4 20.d3 Ne2+ 21.Kh1 Nd4 22.c3 Ne6 
23.Ne4 Rd8 24.Rd1 a5 25.Be3 f5 26.Nc5 f4 27.Bc1 Nxc5 28.bxc5 f3 29.g4 Ba6 30.d4
Be2 31.Rd2 Rab8 32.Rxb8 Rxb8 33.Rb2 Rxb2 34.Bxb2 h5 35.dxe5 hxg4 36.hxg4 Bc4 
37.Kh2 Kf7 38.Kg3 Ke6 39.Kf4 Kd5 40.Bc1 a4 41.Kxf3 Kxe5 42.Bf4+ Kd5 43.Bxc7 Kxc5 
44.Be5 Bd5+ 45.Kf4 g6 46.Bd4+ Kc4 47.Bxa7 Kb3 48.Bc5 Kxc3 49.Ke3 Kc4 50.Be7 Bc6 
51.f3 Bb5 52.Ke4 Bc6+ 53.Kf4 Kd3 54.Kg3 Bd5 55.Kf2 1/2-1/2

```

### Evaluator


[ACM 1994](ACM_1994 "ACM 1994"), round 3, [Evaluator](Evaluator "Evaluator") - Spector




```

[Event "ACM 1994"]
[Site "Cape May, NJ USA"]
[Date "1994.06.26"]
[Round "3"]
[White "Evaluator"]
[Black "Spector"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 Qc7 
9.O-O-O Nbd7 10.Be2 b5 11.Kb1 Bb7 12.a3 O-O 13.Qe3 h6 14.Bxf6 Bxf6 15.g3 e5 
16.Nf5 exf4 17.gxf4 Bxc3 18.bxc3 Qc5 19.Qg3 g6 20.Rxd6 Kh8 21.Qh4 h5 22.Bxh5 
Qf2 23.Qxf2 Nf6 24.Qd4 1-0

```

## Description


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



### Board Representation


Spector maintains a [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") and an [8x8 board](8x8_Board "8x8 Board"), and further [incrementally updates](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), attack-to, attack-from, and combined attack bitboards.



### Bitboards


In the pre-[C99](https://en.wikipedia.org/wiki/C99) days, without 64-bit data type, [bitboards](Bitboards "Bitboards") were often defined as union of [byte](Byte "Byte")-, [word](Word "Word")- and [double word](Double_Word "Double Word") [arrays](Array "Array").




```C++
typedef unsigned short int ustdwiT;
typedef unsigned long int ustdsiT;

##define byteW  8
##define wordW 16
##define dwrdW 32
##define qwrdW 64

/* the bitboard */

##define bbcvL (qwrdL / byteL)
typedef byteT bbcvT[bbcvL];

##define bbwvL (qwrdL / wordL)
typedef ustdwiT bbwvT[bbwvL];

##define bbsvL (qwrdL / dwrdL)
typedef ustdsiT bbsvT[bbsvL];

typedef union bbU {
   bbcvT bbcv; /* unsigned characters/bytes (8 bits) */
   bbwvT bbwv; /* unsigned word integers (16 bits) */
   bbsvT bbsv; /* unsigned short integers (32 bits) */
} bbT, *bbptrT;

```


**BitScan**  

The divide and conquer [bitscan with reset](BitScan#BitscanwithReset "BitScan") [macro](https://en.wikipedia.org/wiki/C_preprocessor) with word lookups is used to [serialize bitboards](Bitboard_Serialization "Bitboard Serialization"), and applies the [comma operator](https://en.wikipedia.org/wiki/Comma_operator) to "return" a boolean result whether the bitboard is empty (0) or not (1):




```C++
##define bb_next(bb, sq) \
  (bb.bbsv[0] ? \
     (bb.bbwv[0] ? \
        ((bb.bbwv[0] &= canwv[sq = *(bfvbase + bb.bbwv[0])]), \
           (sq += sq_a1), 1) \
     : \
        ((bb.bbwv[1] &= canwv[sq = *(bfvbase + bb.bbwv[1])]), \
           (sq += sq_a3), 1)) \
  : \
     (bb.bbsv[1] ? \
        (bb.bbwv[2] ? \
           ((bb.bbwv[2] &= canwv[sq = *(bfvbase + bb.bbwv[2])]), \
              (sq += sq_a5), 1) \
        : \
           ((bb.bbwv[3] &= canwv[sq = *(bfvbase + bb.bbwv[3])]), \
              (sq += sq_a7), 1)) \
     : \
        ((sq = sq_nil), 0)))

##define bb_next_gp(sq)  bb_next(gp_bb, sq)

```


**Population Count**  

[Population count](Population_Count "Population Count") is implemented as sum of four word lookups.




```C++
##define bb_count(bb) \
   (*(bevbase + bb.bbwv[0]) + *(bevbase + bb.bbwv[1]) + \
    *(bevbase + bb.bbwv[2]) + *(bevbase + bb.bbwv[3]))

```

### 8x8 Board


Beside bitboards, a regular [8x8 board](8x8_Board "8x8 Board") is maintained, a union of two- and one-dimensional arrays:




```C++
/* regular board */
typedef union rbU
{
   cpT rbm[rankL][fileL]; /* rank/file indexing */
   cpT rbv[sqL];          /* square indexing */
} rbT, *rbptrT;

```

### Move-Generation


[Move generation](Move_Generation "Move Generation") utilizes the [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), is staged, and generates strictly [legal moves](Legal_Move "Legal Move").



### Search


Spector performs a [principal variation search](Principal_Variation_Search "Principal Variation Search") with [transposition table](Transposition_Table "Transposition Table") and [recursive null move pruning](Null_Move_Pruning "Null Move Pruning") of [R==3](Depth_Reduction_R "Depth Reduction R") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework. [Checks](Check_Extensions "Check Extensions"), [singular check responses](One_Reply_Extensions "One Reply Extensions"), [pawn to seventh rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), and [recaptures](Recapture_Extensions "Recapture Extensions") are [extended](Extensions "Extensions") by one [ply](Ply "Ply"), [double](Double_Check "Double Check") and [discovered checks](Discovered_Check "Discovered Check") even by two. The [killer heuristic](Killer_Heuristic "Killer Heuristic") and [Last Best Reply](Last_Best_Reply "Last Best Reply") improve [move ordering](Move_Ordering "Move Ordering"). 



### Evaluation


Beside [material balance](Material#Balance "Material"), Spector considers various first order terms by traversing all pieces and calling piece specific functions. [King safety](King_Safety "King Safety") takes [piece tropism](King_Safety#KingTropism "King Safety"), [pawn shield](King_Safety#PawnShield "King Safety") and multiple attacks into account, while in the [endgame](Endgame "Endgame") [centralization](King_Centralization "King Centralization") and [King pawn tropism](King_Pawn_Tropism "King Pawn Tropism") starts to dominate. [Pawn structure](Pawn_Structure "Pawn Structure") evaluation focuses on [passed pawns](Passed_Pawn "Passed Pawn"), considering advancement, [blockade](Blockade_of_Stop "Blockade of Stop") and [control of stop](Control_of_Stop_and_Telestop "Control of Stop and Telestop"). Remaining piece considerations include [development](Development "Development"), [square control](Square_Control "Square Control"), and some [tactical](Tactics "Tactics") terms such as penalties for [pinned](Pin "Pin") and [hanging pieces](Hanging_Piece "Hanging Piece").



## See also


* [CookieCat](CookieCat "CookieCat")
* [Edwards' Tablebases](Edwards%27_Tablebases "Edwards' Tablebases")
* [Last Best Reply](Last_Best_Reply "Last Best Reply")
* [Symbolic](Symbolic "Symbolic")


## Downloads


<a id="cite-note-6" href="#cite-ref-6">[6]</a>



* [File:Tbgen.zip](File:Tbgen.zip "File:Tbgen.zip")
* [File:Spector.zip](File:Spector.zip "File:Spector.zip")


## Forum Posts


* [24th ACM Computer Chess Championship](https://groups.google.com/d/msg/rec.games.chess/tUnMP5z-O6M/1u3tu4OdoBkJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 25, 1994 » [ACM 1994](ACM_1994 "ACM 1994")


 [ACM 1994: Spector's games](https://groups.google.com/d/msg/rec.games.chess/KzylHYi4mH0/2_lsGXtxZocJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 29, 1994
* [Re: Speed of Move Generator](https://groups.google.com/d/msg/rec.games.chess.computer/M8V1AzkfOok/YV9lcfOlfgIJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 16, 1995 » [Perft](Perft "Perft")
* [For chess program source collectors](http://www.chesscircle.net/forums/archive/index.php/t-37436.html) by [Steven Edwards](Steven_Edwards "Steven Edwards"), Chess Circle, August 13, 2006
* [Testing LBR](http://www.talkchess.com/forum/viewtopic.php?start=9&t=38556&topic_view=flat) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 27, 2011
* [LMR by another name](http://www.talkchess.com/forum/viewtopic.php?t=57486) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 02, 2015 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Re: Steven Edwards RIP...](http://www.talkchess.com/forum/viewtopic.php?t=62065&start=20) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 11, 2016


 [Re: Steven Edwards RIP...](http://www.talkchess.com/forum/viewtopic.php?t=62065&start=21) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), November 11, 2016
## External Links


* [spector - Wiktionary](https://en.wiktionary.org/wiki/spector)
* [specto - Wiktionary](https://en.wiktionary.org/wiki/specto)
* [Spector (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Spector_%28disambiguation%29)
* [Spectrum from Wikipedia](https://en.wikipedia.org/wiki/Spectrum)
* [Spectrum (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Spectrum_%28disambiguation%29)
* [Speculum from Wikipedia](https://en.wikipedia.org/wiki/Speculum)
* [Spectator from Wikipedia](https://en.wikipedia.org/wiki/Spectator)
* [Speculation from Wikipedia](https://en.wikipedia.org/wiki/Speculation)
* [Inspector from Wikipedia](https://en.wikipedia.org/wiki/Inspector)
* [Inspector (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Inspector_%28disambiguation%29)
* [Inspection from Wikipedia](https://en.wikipedia.org/wiki/Inspection)
* [Billy Cobham](Category:Billy_Cobham "Category:Billy Cobham") - [Searching for the Right Door / Spectrum](https://en.wikipedia.org/wiki/Spectrum_(Billy_Cobham_album)) (1973), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Jan Hammer](Category:Jan_Hammer "Category:Jan Hammer"), [Joe Farrell](Category:Joe_Farrell "Category:Joe Farrell"), [Jimmy Owens](https://en.wikipedia.org/wiki/Jimmy_Owens_(musician)), [Ron Carter](Category:Ron_Carter "Category:Ron Carter"), [Ray Barretto](https://en.wikipedia.org/wiki/Ray_Barretto)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Full featured double rainbow in [Wrangell-St. Elias National Park](https://en.wikipedia.org/wiki/Wrangell%E2%80%93St._Elias_National_Park_and_Preserve), [Alaska](https://en.wikipedia.org/wiki/Alaska), by [Eric Rolph](https://en.wikipedia.org/wiki/User:Ericrolph), October 2005, [Rainbow from Wikipedia](https://en.wikipedia.org/wiki/Rainbow)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [For chess program source collectors](http://www.chesscircle.net/forums/archive/index.php/t-37436.html) by [Steven Edwards](Steven_Edwards "Steven Edwards"), Chess Circle, August 13, 2006
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [ACM Tournament - Specs](https://groups.google.com/d/msg/rec.games.chess/P9WW8L3gq9U/YRX_mZAjv-wJ) by Jim Bumgardner, [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 28, 1994
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [ACM 1994: Spector's games](https://groups.google.com/d/msg/rec.games.chess/KzylHYi4mH0/2_lsGXtxZocJ) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 29, 1994
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> refers to the published 1996 version
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> Courtesy [Steven Edwards](Steven_Edwards "Steven Edwards")

**[Up one Level](Engines "Engines")**







 
