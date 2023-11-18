---
title: Chezzz
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chezzz**

[](http://www.flickr.com/photos/phunkepixie/5064982592/) Chezzz Playazzz <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chezzz**,

a chess engine by [David Rasmussen](David_Rasmussen "David Rasmussen"), which was according to [Leo Dijksman](Leo_Dijksman "Leo Dijksman") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") <a id="cite-note-3" href="#cite-ref-3">[3]</a> the 100th [WinBoard](WinBoard "WinBoard") engine. Chezzz played seven consecutive [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), starting in 2001 with the [CCT3](CCT3 "CCT3"), until 2007 the [CCT9](CCT9 "CCT9").

## Thesis Program

Presumably, Chezzz is similar to Rasmussen's thesis program described in detail in his 2004 Master's thesis <a id="cite-note-4" href="#cite-ref-4">[4]</a> - concerning [board representation](Board_Representation "Board Representation") and the serial [search](Search "Search"), while the [evaluation](Evaluation "Evaluation") of the thesis program is very rudimentary relying on [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") only - [C++](Cpp "Cpp") source code given in Appendix B. Interesting for [C++](Cpp "Cpp") programmers is Appendix B.12 enums.h with DeclareEnumTricks <a id="cite-note-5" href="#cite-ref-5">[5]</a> and forall Macros.

## Bitboards

[Bitboards](Bitboards "Bitboards") are the basic data structure, [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") with four line [arrays](Array "Array") indexed by square and 8-bit [line occupancy](Occupancy_of_any_Line "Occupancy of any Line") determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). [BitScan](BitScan "BitScan") is done with a 16-bit lookup table and up to four conditional cases. The thesis program applies a [population count](Population_Count "Population Count") in the [Brian Kernighan's way](Population_Count#BrianKernighansway "Population Count"), while Chezzz uses the [MMX Swar Popcount](MMX#MMXPopcount "MMX") as introduced in [AMD](AMD "AMD") *Athlon™ Processor x86 Code Optimization* <a id="cite-note-6" href="#cite-ref-6">[6]</a>, with compatibility issues concerning the [3DNow!](https://en.wikipedia.org/wiki/3DNow!) psadbw - Packed sum of absolute byte differences - instruction <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Search

The thesis program features a [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") [parallel search](Parallel_Search "Parallel Search"), [sharing](Shared_Hash_Table "Shared Hash Table") the [lockless hash table](Shared_Hash_Table#Lockless "Shared Hash Table") as proposed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Tim Mann](Tim_Mann "Tim Mann") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. The [iterative deepening](Iterative_Deepening "Iterative Deepening") framework applies [aspiration windows](Aspiration_Windows "Aspiration Windows") of ±1/3 pawn value, [PVS](Principal_Variation_Search "Principal Variation Search") with [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), and [history](History_Heuristic "History Heuristic") and [killer heuristic](Killer_Heuristic "Killer Heuristic") with [thread](Thread "Thread") local [memory](Memory "Memory"). The [SEE swap algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), borrowed from [Crafty](Crafty "Crafty"), is used in [move ordering](Move_Ordering "Move Ordering") and to [prune](Pruning "Pruning") losing [captures](Captures "Captures") in [quiescence search](Quiescence_Search "Quiescence Search"). The search is [extended](Extensions "Extensions") in case of [checks](Check_Extensions "Check Extensions"), [recaptures](Recapture_Extensions "Recapture Extensions"), and [pawn moves to the 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), and [single replies](One_Reply_Extensions "One Reply Extensions").

## Selected Games

## CCT5

[CCT5](CCT5 "CCT5"), Chezzz - [Hossa](Hossa "Hossa") <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```

[Event "CCT5"]
[Site "Internet Chess Club"]
[Date "2003.01.18"]
[Round "-"]
[White "Chezzz"]
[Black "Hossa"]
[Result "0-1"]

1.e4 c5 2.Nf3 Nc6 3.Nc3 e5 4.Bc4 Be7 5.d3 Nf6 6.Nd2 d6 7.Nf1 Bg4 8.f3 Be6 
9.Ne3 Bxc4 10.dxc4 Nd4 11.Qd3 O-O 12.O-O Qd7 13.Ncd5 Nxd5 14.Nxd5 f5 15.Be3 
fxe4 16.fxe4 Bh4 17.c3 Ne6 18.Rad1 Rxf1+ 19.Rxf1 Rf8 20.Rxf8+ Kxf8 21.Qe2 
Qf7 22.Qg4 Bd8 23.Bd2 h5 24.Qh3 Ke8 25.b4 b6 26.a3 Kd7 27.Qg3 Be7 28.a4 Bd8 
29.Be3 Qe8 30.a5 bxa5 31.bxc5 Qf7 32.cxd6 Kxd6 33.Qe1 Kc6 34.Qb1 Qb7 35.Qd1 
h4 36.Bf2 a6 37.Ne3 Kc7 38.Qd5 Qxd5 39.exd5 Nf4 40.Kf1 a4 41.Nc2 Kd6 42.Ba7 
g5 43.g3 hxg3 44.hxg3 Nh5 45.Kf2 Nf6 46.Ke2 Ne4 47.Ke3 Nf6 48.Nb4 a3 49.Kd3 
Nd7 50.Be3 a5 51.Na2 Nc5+ 52.Kc2 Na4 53.Kb3 Nb2 54.Bg1 g4 55.Be3 Bc7 56.Bg5 
e4 57.Bf4+ Kd7 58.Bxc7 Kxc7 59.c5 Nd3 60.Kc4 Nxc5 61.Kd4 Kb6 62.Ke3 Nb7 
63.Kd4 e3 64.Kxe3 Kc5 65.Kd3 Kxd5 66.c4+ Kc5 67.Nc1 Kb4 68.Kc2 Nc5 69.Kb1 
Kxc4 70.Ne2 Ne4 71.Kc2 a4 72.Kc1 Nc3 73.Nf4 Kb3 74.Ne6 a2 75.Nd4+ Kc4 76.Nc2
a3 77.Na1 Ne2+ 78.Kd2 Nxg3 79.Ke1 Kc3 80.Kd1 Kb2 81.Nc2 a1=Q+ 82.Nxa1 Kxa1 
83.Kc2 Nf5 84.Kc1 g3 85.Kd2 g2 86.Kd3 g1=Q 87.Ke4 Qd4+ 88.Kxf5 Kb1 89.Ke6 a2 
90.Kf5 a1=Q 91.Ke6 Qaa7 92.Kf5 Qag7 93.Ke6 Qgd7# 0-1

```

## CCT7

[CCT7](CCT7 "CCT7"), round 5, [Quark](Quark "Quark") - Chezzz

```

[Event "CCT7"]
[Site "Internet Chess Club"]
[Date "2005.02.12"]
[Round "5"]
[White "Quark"]
[Black "Chezzz"]
[Result "0-1"]

1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Bd3 Nc6 6.Nxc6 dxc6 7.O-O e5 8.Nd2 Be6 
9.Qf3 Qc7 10.Bc4 Qe7 11.Qb3 Bxc4 12.Nxc4 b5 13.Nb6 Rb8 14.Be3 Qc7 15.a4 Rxb6 
16.Bxb6 Qxb6 17.Qc3 Bd6 18.Rfd1 Bb8 19.axb5 axb5 20.Qg3 g6 21.Qh4 Qc7 22.Rd3 
Qc8 23.Ra8 Qc7 24.Rc3 Kf8 25.Ra6 c5 26.Rd3 Kg7 27.Rd8 h6 28.Re8 Qb7 29.Ra1 Bc7 
30.Rea8 g5 31.Qh3 Qxe4 32.Qc8 Bd6 33.Qa6 Be7 34.Qxb5 Qxc2 35.Qb8 e4 36.h3 c4 
37.g3 Qd2 38.Qe5+ Bf6 39.Qe8 e3 40.fxe3 Be7 41.Rf1 Qxe3+ 42.Kg2 Qe4+ 43.Kg1 f6 
44.Rf2 h5 45.Ra7 Qe3 46.Qd7 Qxg3+ 47.Rg2 Qe3+ 48.Rf2 Kh6 49.Qc7 Qxh3 50.Ra6 
Qg4+ 51.Kh2 Qd4 52.Rg2 Bc5 53.Qg3 Kg7 54.Kh1 Nh6 55.Ra1 Ng4 56.Re1 Kg6 57.Qf3 
Rb8 58.Qe4+ Qxe4 59.Rxe4 Nf2+ 60.Rxf2 Bxf2 61.Re2 Bd4 62.Re4 Rd8 0-1

```

## See also

- [Chess (Program)](</Chess_(Program)> "Chess (Program)")
- [Zzzzzz](Zzzzzz "Zzzzzz")

## Publications

- [David Rasmussen](David_Rasmussen "David Rasmussen") (**2004**). *Parallel Chess Searching and Bitboards.* Master's thesis, [pdf](http://www.cs.cmu.edu/afs/cs/academic/class/15418-s12/www/competition/www.contrib.andrew.cmu.edu/~jvirdo/rasmussen-2004.pdf)

## Forum Posts

## 2001

- [Congrats to David Rasmussen](http://www.open-aurec.com/wbforum/viewtopic.php?t=33817&p=128002) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2001
- [\*\*\* 100 \*\*\* Chezzz 0.88 by David Rasmussen (Denmark) is available](http://www.open-aurec.com/wbforum/viewtopic.php?t=33815&p=128015) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2001

## 2002

- [Position from Sjeng - Chezzz](https://www.stmintz.com/ccc/index.php?id=208819) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 21, 2002 » [Sjeng](Sjeng "Sjeng")
- [Quiescence Explosion](https://www.stmintz.com/ccc/index.php?id=267486) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), November 26, 2002

## 2003

- [Chezzz-Postmodernist - What plan?](https://www.stmintz.com/ccc/index.php?id=277449) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 15, 2003 » [PostModernist](PostModernist "PostModernist")
- [Chezzz - Hossa CCT5](https://www.stmintz.com/ccc/index.php?id=278110) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 18, 2003 » [CCT5](CCT5 "CCT5"), [Hossa](Hossa "Hossa")

[Test Position : Chezzz - Hossa](https://www.stmintz.com/ccc/index.php?id=278149) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 19, 2003

- [Chezzz @ CCT5 - First Day](https://www.stmintz.com/ccc/index.php?id=279434) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 25, 2003 » [CCT5](CCT5 "CCT5")
- [Chezzz 1.0b released](https://www.stmintz.com/ccc/index.php?id=281467) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 03, 2003
- [Chezzz 1.0.1 released](https://www.stmintz.com/ccc/index.php?id=281801) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 04, 2003
- [Re: Chezzz 1.0.1 - problem solved - for David Rasmussen](https://www.stmintz.com/ccc/index.php?id=281989) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 05, 2003 » [Population Count](Population_Count "Population Count"), [MMX](MMX "MMX")
- [Chezzz's proudest moment (?)](http://www.open-aurec.com/wbforum/viewtopic.php?t=41179&p=156745) by Darren, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 09, 2003 » [CCT5](CCT5 "CCT5")
- [Chezzz 1.0.2 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41207) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2003
- [Chezzz and EGTB's](http://www.open-aurec.com/wbforum/viewtopic.php?t=41222&p=156934) by [Gábor Szõts](Gabor_Szots "Gabor Szots"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2003
- [Example Chezzz cfg file](http://www.open-aurec.com/wbforum/viewtopic.php?t=41251&p=157168) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 14, 2003
- [Chezzz 1.0.3 released and books tweaked](http://www.open-aurec.com/wbforum/viewtopic.php?t=41333&p=157574) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 20, 2003
- [chezzz](http://www.open-aurec.com/wbforum/viewtopic.php?t=41465&p=158115) by Andy, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 27, 2003
- [New books for Chezzz](https://www.stmintz.com/ccc/index.php?id=287059) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 27, 2003
- [Terra - Chezzz ... Nice Game](http://www.open-aurec.com/wbforum/viewtopic.php?t=42882&p=163710) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 04, 2003 » [Terra](Terra "Terra")

## 2004 ...

- [Find The Bug - C / C++](http://bytes.com/topic/c/answers/128755-find-bug) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [bytes.com](http://bytes.com/), July 22, 2005

## External Links

- [Index of /chess/engines/Norbert's collection/Chezzz (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Chezzz%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Chezzz 1.0.3](http://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Chezzz%201.0.3#Chezzz_1_0_3) in [CCRL 40/40](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chezzz Playazzz | Petya Popovyanska | Flickr](http://www.flickr.com/photos/phunkepixie/with/5064982592/#photo_5064982592)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Congrats to David Rasmussen](http://www.open-aurec.com/wbforum/viewtopic.php?t=33817&p=128002) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2001
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [\*\*\* 100 \*\*\* Chezzz 0.88 by David Rasmussen (Denmark) is available](http://www.open-aurec.com/wbforum/viewtopic.php?t=33815&p=128015) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2001
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [David Rasmussen](David_Rasmussen "David Rasmussen") (**2004**). *Parallel Chess Searching and Bitboards.* Master's thesis, [pdf](http://www.cs.cmu.edu/afs/cs/academic/class/15418-s12/www/competition/www.contrib.andrew.cmu.edu/~jvirdo/rasmussen-2004.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Find The Bug - C / C++](http://bytes.com/topic/c/answers/128755-find-bug) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [bytes.com](http://bytes.com/), July 22, 2005
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [AMD Athlon™ Processor x86 Code Optimization](http://www.bartol.udel.edu/mri/sam/Athlon_code_optimization_guide.pdf) (pdf) Efficient 64-Bit Population Count MMX Version Page 130
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Chezzz 1.0.1 - problem solved - for David Rasmussen](https://www.stmintz.com/ccc/index.php?id=281989) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 05, 2003
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *A lock-less transposition table implementation for parallel search chess engines*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Chezzz - Hossa CCT5](https://www.stmintz.com/ccc/index.php?id=278110) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 18, 2003

**[Up one Level](Engines "Engines")**

