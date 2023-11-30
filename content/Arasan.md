---
title: Arasan
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Arasan**

|  |  |
| --- | --- |
| **Arasan**,
an [open source engine](Category:Open_Source "Category:Open Source") written by [Jon Dart](Jon_Dart "Jon Dart") in [C++](Cpp "Cpp"). Arasan's development started in the early 90s, the first version, released in 1994 was a 16-bit program running under [Windows 3.1](Windows "Windows") using an [8x8 Board](8x8_Board "8x8 Board"), [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") and its own [GUI](GUI "GUI"), evolving to a portable 32-bit and later 64-bit program, utilizing [bitboards](Bitboards "Bitboards") to determine its [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [rotated bitboard lookups](Rotated_Bitboards "Rotated Bitboards"). In 2008, rotated were replaced by [Magic bitboards](Magic_Bitboards "Magic Bitboards"), which gave Arasan about a 20-25% speedup <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Despite its own GUI, Arasan early supported the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and later [UCI](UCI "UCI") as well, to run under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The latest version of Arasan and all major versions, including Version 1.0 from March 1994, are available as source code from the Arasan.org site <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Jon's change logs, bug fix reports and tournament reports over the time are available from [forum archives](Computer_Chess_Forums "Computer Chess Forums"), as well the recent ones from the Arasan blog <a id="cite-note-4" href="#cite-ref-4">[4]</a>
| அரசன் |
|  அரசன் <a id="cite-note-5" href="#cite-ref-5">[5]</a> (Arasan) , King in [Tamil language](https://en.wikipedia.org/wiki/Tamil_language) <a id="cite-note-6" href="#cite-ref-6">[6]</a> |

## Selected Features

<a id="cite-note-7" href="#cite-ref-7">[7]</a>

## [Board Representation](Board_Representation "Board Representation")

### Bitboard Trials

[Jon Dart](Jon_Dart "Jon Dart"), May 1996 <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```C++
 Lately I've been working on a new major release of Arasan. I have spent the last few months working on the search engine, trying to improve speed and performance. I tried some experiments with a [bitboard](Bitboards "Bitboards") move representation, but I have backed off on that for now.

```

```C++
With bitboards, I got a nice reduction in tree size (bitboards allow a more accurate [swap-down analysis](Static_Exchange_Evaluation "Static Exchange Evaluation") than I had before, and this improves [move ordering](Move_Ordering "Move Ordering") and allows better "culling" of losing captures in the [quiescence search](Quiescence_Search "Quiescence Search")).

```

```C++
However, currently the program relies pretty heavily on [incrementally generated](Incremental_Updates "Incremental Updates") [attack information](Attack_and_Defend_Maps "Attack and Defend Maps"), and I didn't have that implemented to work with bitboards, so I had to compute attacks as needed. Unfortunately, the current program "needs" to do this much more often than [Crafty](Crafty "Crafty") does, so the loss from computing attacks more than balanced out the gains from bitboards. This is fixable, I'm sure, but I've put off further work on it for now. 

```

### [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

[Jon Dart](Jon_Dart "Jon Dart"), August 2008 <a id="cite-note-9" href="#cite-ref-9">[9]</a> :

```C++
The main change has been to re-work the code to use ["magic" bitboard logic](Magic_Bitboards "Magic Bitboards") instead of [rotated bitboards](Rotated_Bitboards "Rotated Bitboards"). This has given about a 20-25% speedup. I have also had to re-write the [evaluation function](Evaluation "Evaluation") to take advantage of bitboard attack functions for [king safety](King_Safety "King Safety") and [mobility](Mobility "Mobility"). 

```

### [PEXT/PDEP Bitboards](BMI2#PDEPBitboards "BMI2")

Arasan **20.3**, released in November 2017, performs [PEXT/PDEP Bitboards](BMI2#PDEPBitboards "BMI2") if compiled for the [BMI2](BMI2 "BMI2") instruction set <a id="cite-note-10" href="#cite-ref-10">[10]</a> to replace [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards") in looking up [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP") 21.0
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening") [Depth Resolution 4](Depth#FractionalPlies "Depth")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
  - [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
  - [Lockless Hashing](Shared_Hash_Table#Lockless "Shared Hash Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
  - [Counter Moves History](History_Heuristic#CMHist "History Heuristic")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [Refutation Table](Refutation_Table "Refutation Table")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](Selectivity "Selectivity")
  - [Fractional Ply](Depth#FractionalPlies "Depth") [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
    - [Singular Extensions](Singular_Extensions "Singular Extensions")
  - [Pruning](Pruning "Pruning")
    - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
    - [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
    - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
    - [Futility Pruning](Futility_Pruning "Futility Pruning")
    - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
    - [ProbCut](ProbCut "ProbCut")
  - [Reductions](Reductions "Reductions")
    - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
    - [Razoring](Razoring "Razoring")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

### [NNUE](NNUE "NNUE")

Arasan **23.0**, released in September 2021, uses a [Stockfish](Stockfish "Stockfish") 13 compatible [NNUE](NNUE "NNUE") - trained by selfplay positions - to [evaluate](Evaluation "Evaluation") its positions <a id="cite-note-12" href="#cite-ref-12">[12]</a>. The neural network file is external to the program and is loaded at runtime.

### Traditional

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Development](Development "Development")
- [Mobility](Mobility "Mobility")
  - [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
  - [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Outposts](Outposts "Outposts")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
- [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
  - [Outside Passed Pawn](Outside_Passed_Pawn "Outside Passed Pawn")
  - [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")
  - [Tarrasch Rule](Tarrasch_Rule "Tarrasch Rule")
- [King Safety](King_Safety "King Safety")
  - [King Tropism](King_Safety#KingTropism "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")

### [Automated Tuning](Automated_Tuning "Automated Tuning")

Arasan **19.2**, released in November 2016, applies [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") by default and supports the [Adam](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam) [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) algorithm <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>.

## [Syzygy Bases](Syzygy_Bases "Syzygy Bases")

Arasan uses a [Fathom](Syzygy_Bases#Fathom "Syzygy Bases") fork with some bug fixes and enhancements <a id="cite-note-15" href="#cite-ref-15">[15]</a>, also supporting [7-man](Syzygy_Bases#7-man "Syzygy Bases") <a id="cite-note-16" href="#cite-ref-16">[16]</a>.

## Tournament Play

Arasan went online in December, 1996 <a id="cite-note-17" href="#cite-ref-17">[17]</a> , and played almost all major online computer chess tournaments, such as [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), [ACCA Americas' Computer Chess Championship](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), [ACCA World Computer Rapid Chess Championship](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"), [TCEC](TCEC "TCEC"), and [International Gsei Web Tournaments](Italian_Computer_Chess_Championship#IGWT "Italian Computer Chess Championship"). Arasan 15.1 <a id="cite-note-18" href="#cite-ref-18">[18]</a> won the [ACCA 2012](ACCA_2012 "ACCA 2012") <a id="cite-note-19" href="#cite-ref-19">[19]</a> , Arasan 16.0 the [WCRCC 2013](WCRCC_2013 "WCRCC 2013") <a id="cite-note-20" href="#cite-ref-20">[20]</a> . Over the board, Arasan was active at the [CSVN Programmers Tournaments](CSVN_Programmers_Tournament "CSVN Programmers Tournament") operated by [Tessa Pijl](Tessa_Pijl "Tessa Pijl"). Arasan was runner-up behind [The Baron](The_Baron "The Baron") in May 2014 at the [PT 46](PT_46 "PT 46") one point behind, as well in June 2015 at the [PT 48](PT_48 "PT 48") with the same score according to the tiebreak rules <a id="cite-note-21" href="#cite-ref-21">[21]</a>.

## Photos & Games

[](http://www.computerschaak.nl/index.php/nieuws/51-toernooien/704-pt48-round-7)
[PT 48](PT_48 "PT 48"), Two Kings fighting, [Johan de Koning](Johan_de_Koning "Johan de Koning") and [Tessa Pijl](Tessa_Pijl "Tessa Pijl") in Arasan vs. [The King](The_King "The King") <a id="cite-note-22" href="#cite-ref-22">[22]</a>

```
[Event "PT 48"]
[Site "Leiden, NL"]
[Date "2015.06.14"]
[Round "7"]
[White "Arasan"]
[Black "The King"]
[Result "1-0"]

1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 e6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 
9.a4 b4 10.Ne4 c5 11.Nxf6+ Nxf6 12.dxc5 Bxc5 13.e4 Bb7 14.Qe2 O-O 15.O-O e5 
16.Bg5 h6 17.Bh4 Qd6 18.Bg3 Rfe8 19.Rfd1 Re7 20.Bh4 Qc6 21.Rac1 Rc8 22.Rc4 Re6 
23.Bxf6 Rxf6 24.Rdc1 Qb6 25.Kh1 a5 26.Qc2 b3 27.Qe2 Qd6 28.R4c3 Rf4 29.g3 Rf6 
30.Bc4 Rb8 31.Rxb3 Bb4 32.Rd3 Qc7 33.Kg2 Rf8 34.Rdd1 Rc6 35.b3 Re8 36.Kg1 Rc8 
37.Rd5 Re6 38.Rd3 Rf6 39.Rcd1 Re8 40.Nh4 Qb6 41.Nf5 Rf8 42.Rf3 Kh8 43.Nh4 Kg8 
44.Rd7 Bc8 45.Rd5 Rd6 46.Rxd6 Qxd6 47.Rd3 Qc7 48.Qh5 Kh7 49.Nf3 f6 50.Nh4 Bd7 
51.Bf7 Bc8 52.Bg6+ Kg8 53.Bf5 Qc2 54.Qf3 Re8 55.Kg2 Rf8 56.Rd5 Bc5 57.Bxc8 Rxc8 
58.Rd7 Bf8 59.Qg4 h5 60.Qg6 Qe2 61.Nf3 Qc2 62.Qf7+ Kh8 63.Qxh5+ Kg8 64.Nd2 Rb8 
65.g4 Rc8 66.Qf7+ Kh8 67.Qh5+ Kg8 68.Qg6 Kh8 69.Qf5 Kg8 70.g5 fxg5 71.Nf3 Qc6 
72.Nxg5 Qh6 73.Rd3 Rc7 74.Rf3 Bb4 75.Rh3 Bf8 76.Rxh6 1-0

```

## See also

- [King](King "King")

## Forum Posts

## 1995 ...

- [Arasan 2.0 (Windows chess program) available via ftp](http://groups.google.com/group/rec.games.chess/browse_frm/thread/489bd1c77cf3f5a3) by [Jon Dart](Jon_Dart "Jon Dart"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 4, 1995
- [Arasan 2.1 (Windows chess program) available via ftp](http://groups.google.com/group/rec.games.chess.misc/browse_frm/thread/feab13109d3fea8d) by [Jon Dart](Jon_Dart "Jon Dart"), [rec.games.chess.misc](Computer_Chess_Forums "Computer Chess Forums"), October 23, 1995
- [Arasan 2.2 (Windows chess program) available via ftp](http://groups.google.com/group/rec.games.chess.misc/browse_frm/thread/353af31249b8e71a) by [Jon Dart](Jon_Dart "Jon Dart"), [rec.games.chess.misc](Computer_Chess_Forums "Computer Chess Forums"), December 10, 1995
- [Arasan progress report](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d75cd258ea73a4a7) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 23, 1996
- [Arasan 3.0 (Windows chess program) available](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/da81bfa994db07e) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 8, 1996
- [Arasan goes online](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4a4705301c3c3229) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 6, 1997
- [Arasan 4.0 is available](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/400f58ce4133b3dc) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 15, 1997
- [Arasan 5.0 released](https://www.stmintz.com/ccc/index.php?id=39273) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 13, 1999

## 2000 ...

- [Arasan 5.4 released](https://www.stmintz.com/ccc/index.php?id=112475) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 25, 2000
- [Arasan vs. IM Paunovic](https://www.stmintz.com/ccc/index.php?id=114810) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 16, 2000
- [Arasan now under Linux](https://www.stmintz.com/ccc/index.php?id=127953) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 02, 2000
- [A few notes from Arasan's games in CCT2](https://www.stmintz.com/ccc/index.php?id=136752) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 05, 2000 » [CCT2](CCT2 "CCT2")
- [CCT4 notes - Arasan](https://www.stmintz.com/ccc/index.php?id=208715) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 20, 2002 » [CCT4](CCT4 "CCT4")
- [Arasan 6.0](https://www.stmintz.com/ccc/index.php?id=253897) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 24, 2002
- [Arasan 6.3](https://www.stmintz.com/ccc/index.php?id=279622) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 26, 2003
- [Arasan 7.0](https://www.stmintz.com/ccc/index.php?id=310679) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 09, 2003
- [Arasan 7.4](https://www.stmintz.com/ccc/index.php?id=351899) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 28, 2004
- [Arasan 7.4 64-bit Speedup](https://www.stmintz.com/ccc/index.php?id=357325) by [Slater Wold](index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](CCC "CCC"), March 30, 2004
- [Arasan 8.0](https://www.stmintz.com/ccc/index.php?id=383566) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 22, 2004
- [Arasan 8.2](https://www.stmintz.com/ccc/index.php?id=397817) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 26, 2004

## 2005 ...

- [Arasan 8.4](https://www.stmintz.com/ccc/index.php?id=414274) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 26, 2005
- [Arasan in CCT8](https://www.stmintz.com/ccc/index.php?id=489903) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 26, 2006 » [CCT8](CCT8 "CCT8")
- [Arasan @ WCRCC tournament](http://www.talkchess.com/forum/viewtopic.php?t=15306) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 23, 2007 » [WCRCC 2007](WCRCC_2007 "WCRCC 2007")
- [Arasan 10.0](http://www.talkchess.com/forum/viewtopic.php?t=16221) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 02, 2007
- [Arasan 10.2](http://www.talkchess.com/forum/viewtopic.php?t=19673) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 16, 2008
- [Arasan 10.4](http://www.talkchess.com/forum/viewtopic.php?t=22020) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 27, 2008
- [Arasan 11.0](http://www.talkchess.com/forum/viewtopic.php?t=25134) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 28, 2008
- [Arasan 11.3](http://www.talkchess.com/forum/viewtopic.php?t=27151) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 24, 2009
- [Arasan 11.4](http://www.talkchess.com/forum/viewtopic.php?t=28528) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 20, 2009
- [Arasan 11.5](http://www.talkchess.com/forum/viewtopic.php?t=29668) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 05, 2009
- [Arasan 11.6](http://www.talkchess.com/forum/viewtopic.php?t=30678) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 18, 2009

## 2010 ...

- [Arasan 11.7](http://www.talkchess.com/forum/viewtopic.php?t=32449) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 07, 2010
- [Arasan 12.0 released](http://www.talkchess.com/forum/viewtopic.php?t=35724) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 07, 2010
- [Arasan 12.2 released](http://www.talkchess.com/forum/viewtopic.php?t=36661) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 11, 2010

**2011**

- [Arasan 12.3 released](http://www.talkchess.com/forum/viewtopic.php?t=37921) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 02, 2011
- [Arasan 13.0](http://www.talkchess.com/forum/viewtopic.php?t=40091) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 18, 2011
- [Arasan 13.1](http://www.talkchess.com/forum/viewtopic.php?t=40157) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 23, 2011
- [MORE about Arasan 13.1](http://www.talkchess.com/forum/viewtopic.php?t=40186) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), August 26, 2011
- [Arasan 13.2](http://www.talkchess.com/forum/viewtopic.php?t=40617) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 02, 2011
- [Arasan 13.3](http://www.talkchess.com/forum/viewtopic.php?t=41086) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 14, 2011 » [ACCA 2011](ACCA_2011 "ACCA 2011")
- [Arasan 13.4](http://www.talkchess.com/forum/viewtopic.php?t=41369) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 07, 2011

**2012**

- [Arasan 14.0](http://www.talkchess.com/forum/viewtopic.php?t=42736) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 04, 2012
- [Arasan 14.2](http://www.talkchess.com/forum/viewtopic.php?t=44044) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 12, 2012
- [Arasan 14.3](http://www.talkchess.com/forum/viewtopic.php?t=44492) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 18, 2012
- [Arasan 15.0](http://www.talkchess.com/forum/viewtopic.php?t=45229) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 20, 2012
- [Arasan 15.1](http://www.talkchess.com/forum/viewtopic.php?t=46077) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 19, 2012

**2013**

- [Arasan 15.2](http://www.talkchess.com/forum/viewtopic.php?t=47333) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 26, 2013
- [Arasan 15.4](http://www.talkchess.com/forum/viewtopic.php?t=47845) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 24, 2013
- [Arasan 15.6](http://www.talkchess.com/forum/viewtopic.php?t=48070) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 21, 2013
- [Arasan on github](http://www.talkchess.com/forum/viewtopic.php?t=48082) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 22, 2013 <a id="cite-note-23" href="#cite-ref-23">[23]</a>
- [Arasan games from WCRCC](http://www.talkchess.com/forum/viewtopic.php?t=48703) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 21, 2013 » [WCRCC 2013](WCRCC_2013 "WCRCC 2013")
- [Arasan 16.0](http://www.talkchess.com/forum/viewtopic.php?t=48748) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 24, 2013
- [Arasan 16.1](http://www.talkchess.com/forum/viewtopic.php?t=49205) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 01, 2013
- [Arasan 16.2](http://www.talkchess.com/forum/viewtopic.php?t=49824) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 25, 2013
- [Arasan 16.3](http://www.talkchess.com/forum/viewtopic.php?t=50348) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 06, 2013

**2014**

- [test position: Rookie-Arasan](http://www.talkchess.com/forum/viewtopic.php?t=51071) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 27, 2014 » [Rookie](Rookie "Rookie"), [Zugzwang](Zugzwang "Zugzwang")
- [Arasan 17.0](http://www.talkchess.com/forum/viewtopic.php?t=51760) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 27, 2014
- [Arasan GUI fixes](http://www.talkchess.com/forum/viewtopic.php?t=51839) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 02, 2014
- [Arasan 17.1](http://www.talkchess.com/forum/viewtopic.php?t=52242) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 07, 2014
- [Arasan 17.2](http://www.talkchess.com/forum/viewtopic.php?t=52474) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 30, 2014
- [Arasan 17.3](http://www.talkchess.com/forum/viewtopic.php?t=53532) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 01, 2014
- [Arasan 17.4](http://www.talkchess.com/forum/viewtopic.php?t=53987) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 08, 2014

## 2015 ...

- [Arasan 17.5](http://www.talkchess.com/forum/viewtopic.php?t=55072) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 24, 2015
- [Experiments with eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=55621) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 10, 2015 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Arasan 18.0](http://www.talkchess.com/forum/viewtopic.php?t=57122) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 30, 2015
- [Arasan 18.1](http://www.talkchess.com/forum/viewtopic.php?t=58130) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 02, 2015
- [Arasan 18.2](http://www.talkchess.com/forum/viewtopic.php?t=58460) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 03, 2015

**2016**

- [Arasan 18.3](http://www.talkchess.com/forum/viewtopic.php?t=59138) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 02, 2016
- [Arasan Syzygy support (working with Windows, too)](http://www.talkchess.com/forum/viewtopic.php?t=59463) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 10, 2016 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
- [Arasan 19.0 + updated test suite](http://www.talkchess.com/forum/viewtopic.php?t=59997) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 29, 2016
- [Arasan 19.1](http://www.talkchess.com/forum/viewtopic.php?t=61077) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 09, 2016
- [Arasan 19.2](http://www.talkchess.com/forum/viewtopic.php?t=61948) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 03, 2016

**2017**

- [Arasan 20.0](http://www.talkchess.com/forum/viewtopic.php?t=62987) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 31, 2017
- [building for Android](http://www.talkchess.com/forum/viewtopic.php?t=63773) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 19, 2017 » [Android](Android "Android")
- [Arasan 20.1](http://www.talkchess.com/forum/viewtopic.php?t=63855) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 28, 2017
- [Arasan Programmer's Guide](http://www.talkchess.com/forum/viewtopic.php?t=64364) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 21, 2017
- [Arasan 20.2](http://www.talkchess.com/forum/viewtopic.php?t=64610) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 15, 2017
- [Arasan 20.3](http://www.talkchess.com/forum/viewtopic.php?t=65636) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 05, 2017

**2018**

- [Arasan 20.4](http://www.talkchess.com/forum/viewtopic.php?t=66232) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 03, 2018
- [Arasan 20.4.1](http://www.talkchess.com/forum/viewtopic.php?t=66254) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 05, 2018
- [Arasan 20.5](http://www.talkchess.com/forum/viewtopic.php?t=67040) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 08, 2018
- [Arasan 21.0 beta](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67805) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 23, 2018
- [Arasan 21.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67855) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 30, 2018
- [Arasan 21.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68554) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 02, 2018
- [Arasan 21.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69436) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 31, 2018

**2019**

- [Arasan 21.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70360) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 29, 2019
- [Arasan 21.4](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71169) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 02, 2019
- [Arasan 22.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72541) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 10, 2019

## 2020 ...

- [Arasan 22.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74331) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 01, 2020
- [Arasan 22.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76128) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 22, 2020

**2021**

- [Arasan 22.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77414) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 31, 2021
- [Arasan 23.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78122) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 06, 2021

[Re: Arasan 23.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78122&start=14) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 08, 2021
**2022**

- [Arasan 23.3](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79500) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 12, 2022

## External Links

## Chess Engine

- [jdart1/arasan-chess · GitHub](https://github.com/jdart1/arasan-chess) <a id="cite-note-24" href="#cite-ref-24">[24]</a>
- [Arasan Chess](https://www.arasanchess.org/index.shtml) by [Jon Dart](Jon_Dart "Jon Dart")
- [Arasan Programmer's Guide](https://www.arasanchess.org/programr.shtml) by [Jon Dart](Jon_Dart "Jon Dart") <a id="cite-note-25" href="#cite-ref-25">[25]</a>
- [Arasan Test Suite](https://www.arasanchess.org/testsuite.shtml)
- [Arasan 8.4 released, short interview with Jon Dart](https://web.archive.org/web/20120106012659/http://www.playwitharena.com/?Newsticker:Archive_5) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), March 01, 2005, [Arena Chess GUI](Arena "Arena"), Archive 5, 72 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Arasan](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Arasan&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Arasan from Wikipedia](https://en.wikipedia.org/wiki/Arasan)
- [Imsai Arasan 23rd Pulikecei from Wikipedia](https://en.wikipedia.org/wiki/Imsai_Arasan_23rd_Pulikecei)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Arasan Blog - Aug 26, 2008](https://www.arasanchess.org/blogs/aug08.html)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Arasan chess](https://www.arasanchess.org/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Arasan Downloads](https://www.arasanchess.org/downld.shtml)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Arasan Tech Blog](https://arasanchess.org/blog.shtml)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Tamil script from Wikipedia](https://en.wikipedia.org/wiki/Tamil_script)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [அரசன் (சதுரங்கம்) - தமிழ் விக்கிப்பீடியா](<https://ta.wikipedia.org/wiki/%E0%AE%85%E0%AE%B0%E0%AE%9A%E0%AE%A9%E0%AF%8D_(%E0%AE%9A%E0%AE%A4%E0%AF%81%E0%AE%B0%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%AE%E0%AF%8D)>)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Arasan Programmer's Guide](https://www.arasanchess.org/programr.shtml)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Arasan progress report](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d75cd258ea73a4a7) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 23, 1996
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Arasan Blog - Aug 26, 2008](https://www.arasanchess.org/blogs/aug08.html)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Arasan 20.3](http://www.talkchess.com/forum/viewtopic.php?t=65636) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 05, 2017
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> arasan_source20.3.zip/src/attacks.h
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Arasan 23.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78122&start=14) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 08, 2021
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Arasan 19.2](http://www.talkchess.com/forum/viewtopic.php?t=61948) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 03, 2016
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Diederik P. Kingma](https://scholar.google.nl/citations?user=yyIoQu4AAAAJ), [Jimmy Lei Ba](https://scholar.google.ca/citations?user=ymzxRhAAAAAJ&hl=en) (**2015**). *Adam: A Method for Stochastic Optimization*. [arXiv:1412.6980v8](https://arxiv.org/abs/1412.6980v8), [ICLR 2015](http://www.iclr.cc/doku.php?id=iclr2015:main)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [jdart1/Fathom · GitHub](https://github.com/jdart1/Fathom) by [Jon Dart](Jon_Dart "Jon Dart")
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [7-man Syzygy support in Fathom](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70568) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 23, 2019
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Arasan goes online](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4a4705301c3c3229) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 6, 1997
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Arasan 15.1](http://www.talkchess.com/forum/viewtopic.php?t=46077) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 19, 2012
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Seventh Annual ACCA Americas' Computer Chess Championships](http://www.talkchess.com/forum/viewtopic.php?t=46047) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 18, 2012
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Arasan games from WCRCC](http://www.talkchess.com/forum/viewtopic.php?t=48703) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 21, 2013
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Baron 1st, Arasan 2nd](http://www.talkchess.com/forum/viewtopic.php?t=56645&start=3) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 14, 2015
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [PT48 Round 7](http://www.computerschaak.nl/index.php/nieuws/51-toernooien/704-pt48-round-7)
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [jdart1/arasan-chess · GitHub](https://github.com/jdart1/arasan-chess)
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> [Arasan on github](http://www.talkchess.com/forum/viewtopic.php?t=48082) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), May 22, 2013
1. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Arasan Programmer's Guide](http://www.talkchess.com/forum/viewtopic.php?t=64364) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 21, 2017

**[Up one Level](Engines "Engines")**

