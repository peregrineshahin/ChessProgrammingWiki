---
title: RedQueen
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RedQueen**



[ The Red Queen lecturing [Alice](Alice "Alice") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**RedQueen**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written in [C++](Cpp "Cpp") by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"). Using minimal library dependencies as possible, it could easily ported to various [operating systems](Software "Software") such as [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS"), and [Android](Android "Android"). The name RedQueen was inspired by the [Red Queen character](https://en.wikipedia.org/wiki/Red_Queen_%28Through_the_Looking-Glass%29) in [Lewis Carroll's](Category:Lewis_Carroll "Category:Lewis Carroll") [Through the Looking-Glass](https://en.wikipedia.org/wiki/Through_the_Looking-Glass) novel <a id="cite-note-2" href="#cite-ref-2">[2]</a> . 



### Bitboards


RedQueen is a [bitboard](Bitboards "Bitboards") engine and uses [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") [magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). [BitScans](BitScan "BitScan") are either implemented in [inline assembly](Assembly#InlineAssembly "Assembly") for [x86-64](X86-64 "X86-64") [processor instructions](BitScan#bsfbsr "BitScan"), or with [De Bruijn multiplication](BitScan#DeBruijnMultiplation "BitScan") and [double conversion](BitScan#DoubleConversionBSR "BitScan") for forward and reverse scans respectively  <a id="cite-note-4" href="#cite-ref-4">[4]</a>: 




```C++

const uint64_t debruijn64 = 0x07EDD5E59A4E28C2ULL;
const uint32_t index64[64] = {
   63,  0, 58,  1, 59, 47, 53,  2,
   60, 39, 48, 27, 54, 33, 42,  3,
   61, 51, 37, 40, 49, 18, 28, 20,
   55, 30, 34, 11, 43, 14, 22,  4,
   62, 57, 46, 52, 38, 26, 32, 41,
   50, 36, 17, 19, 29, 10, 13, 21,
   56, 45, 25, 31, 35, 16,  9, 12,
   44, 24, 15,  8, 23,  7,  6,  5
};

inline int bitScanForward(int* const index, const uint64_t mask) {
##if defined(__LP64__)
   uint64_t ret;
   asm ("bsfq %[mask], %[ret]" : [ret] "=r" (ret) :[mask] "mr" (mask));
   *index = int(ret);
##else
   *index = int(index64[((mask & -mask) * debruijn64) >> 58]);
##endif
	return mask?1:0;
}
inline int bitScanReverse(int* const index, const uint64_t mask) {
##if defined(__LP64__)
   uint64_t ret;
   asm ("bsrq %[mask], %[ret]" :[ret] "=r" (ret) :[mask] "mr" (mask));
   *index = (unsigned int)ret;
##else
   union {
      double d;
      struct {
         unsigned int mantissal : 32;
         unsigned int mantissah : 20;
         unsigned int exponent : 11;
         unsigned int sign : 1;
      };
   } ud;
   ud.d = (double)(mask & ~(mask >> 32));
   *index = ud.exponent - 1023;
##endif
   return mask?1:0;
}

```

Similar holds for [population count](Population_Count "Population Count") with [SSE4](SSE4 "SSE4") instruction if available versus [SWAR-popcount](Population_Count#SWARPopcount "Population Count"), also using an optimized version for populations below 16, borrowed from [Stockfish](Stockfish "Stockfish").



### Search


RedQueen applies a [parallel search](Parallel_Search "Parallel Search") considering the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") using a pool of [threads](Thread "Thread") where a master spawns idle threads. The [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with the [shared](Shared_Hash_Table "Shared Hash Table") [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Selectivity](Selectivity "Selectivity") is applied by [check](Check_Extensions "Check Extensions") and [PV extensions](PV_Extensions "PV Extensions"), [adaptive nullmove pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [razoring](Razoring "Razoring"), [futility pruning](Futility_Pruning "Futility Pruning"), [reductions](Reductions "Reductions") at [PV-](Node_Types#PV "Node Types") and more aggressively at none PV-nodes. The [SEE swap algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") is used to prune bad [captures](Captures "Captures") in [quiescence search](Quiescence_Search "Quiescence Search"), as well in [move ordering](Move_Ordering "Move Ordering"), which is further improved by the obligatory [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristics](History_Heuristic "History Heuristic").



### Evaluation


The [evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") and otherwise considers [tactical](Tactics "Tactics") and positional features as well as [material imbalances](Material "Material") along with a [pawn structure cache](Pawn_Hash_Table "Pawn Hash Table") and a [tapered eval](Tapered_Eval "Tapered Eval") interpolating [middlegame](Middlegame "Middlegame") and [endgame](Endgame "Endgame") [scores](Score "Score") with [passed pawn](Passed_Pawn "Passed Pawn") and [king safety](King_Safety "King Safety") and most dominant terms beside material.



## Tournament Play


Over the board, RedQueen played the [ICT 2010](ICT_2010 "ICT 2010"), [DOCCC 2010](DOCCC_2010 "DOCCC 2010"), [ICT 2011](ICT_2011 "ICT 2011"), [ICT 2012](ICT_2012 "ICT 2012"), [PT 52](PT_52 "PT 52"), [PT 53](PT_53 "PT 53") and [PT 54](PT_54 "PT 54") [CSVN](CSVN "CSVN") tournaments in [Leiden](https://en.wikipedia.org/wiki/Leiden), online the [ACCA 2010](ACCA_2010 "ACCA 2010"), [ACCA 2011](ACCA_2011 "ACCA 2011"), [CCT13](CCT13 "CCT13"), [CCT14](CCT14 "CCT14"), and the [WCRCC 2011](WCRCC_2011 "WCRCC 2011").



## Selected Games


[ACCA 2011](ACCA_2011 "ACCA 2011"), round 2, RedQueen - [Crafty](Crafty "Crafty") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "ACCA 2011"]
[Site "HGM's server"]
[Date "2011.11.12"]
[Round "2"]
[White "RedQueen"]
[Black "Crafty"]
[Result "1/2-1/2"]

1.c4 e6 2.Nf3 d5 3.d4 Nf6 4.Nc3 Be7 5.Bf4 O-O 6.e3 Nbd7 7.c5 Nh5 8.Bd3 Nxf4
9.exf4 c6 10.Qc2 g6 11.h4 Nf6 12.a3 b6 13.b4 Qc7 14.g3 a5 15.Na4 b5 16.Nb6
Ra7 17.O-O axb4 18.axb4 Rxa1 19.Rxa1 Bb7 20.Qe2 Nd7 21.Nxd7 Qxd7 22.Ne5 Qc7
23.h5 Bf6 24.Qg4 Re8 25.Ra7 Kf8 26.hxg6 hxg6 27.Nxf7 Qxf7 28.Bxg6 Qg7 29.Rxb7
Qxb7 30.Bxe8 Kxe8 31.Qxe6+ Be7 32.f5 Qd7 33.Qg8+ Bf8 34.Qg6+ Kd8 35.Qf6+ Be7
36.Qh8+ Qe8 37.Qe5 Kd7 38.Qe6+ Kd8 39.Qe5 Kd7 40.Qe6+ Kd8 41.Qe5 1/2-1/2

```

## See also


* [Alice](Alice "Alice")
* [Queen (engine)](Queen_(engine) "Queen (engine)")


## Forum Posts


### 2010


* [RedQueen 0.6](http://www.talkchess.com/forum/viewtopic.php?t=35846) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), August 21, 2010
* [Redqueen v0.7](http://www.talkchess.com/forum/viewtopic.php?t=36417) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), October 18, 2010
* [Redqueen v0.7.5 (ACCA 2010)](http://www.talkchess.com/forum/viewtopic.php?t=36630) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), November 08, 2010 » [ACCA 2010](ACCA_2010 "ACCA 2010")
* [Redqueen v0.8](http://www.talkchess.com/forum/viewtopic.php?t=36891) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 01, 2010
* [Test position for average engines](http://www.talkchess.com/forum/viewtopic.php?t=36967) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 06, 2010 » [DOCCC 2010](DOCCC_2010 "DOCCC 2010"), [Fridolin](Fridolin "Fridolin")


### 2011


* [Redqueen v0.9 release](http://www.talkchess.com/forum/viewtopic.php?t=37884) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), January 31, 2011
* [Redqueen v0.9.1 release](http://www.talkchess.com/forum/viewtopic.php?t=38015) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), February 10, 2011
* [Redqueen v0.9.5 release](http://www.talkchess.com/forum/viewtopic.php?t=38149) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), February 21, 2011
* [RedQueen for Android](http://www.talkchess.com/forum/viewtopic.php?t=38638) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 03, 2011
* [RedQueen v0.9.8 release](http://www.talkchess.com/forum/viewtopic.php?t=38888) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), April 27, 2011
* [2011 Fifth Annual ACCA WCRCC: RedQueen games](http://www.talkchess.com/forum/viewtopic.php?t=39819) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), July 23, 2011 » [WCRCC 2011](WCRCC_2011 "WCRCC 2011")
* [RedQueen 1.0 beta release](http://www.talkchess.com/forum/viewtopic.php?t=40265) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), September 04, 2011
* [2011 6ht annual ACCA games (RedQueen's games)](http://www.talkchess.com/forum/viewtopic.php?t=41067) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), November 13, 2011 » [ACCA 2011](ACCA_2011 "ACCA 2011")


### 2012 ...


* [RedQueen 1.1 released](http://www.talkchess.com/forum/viewtopic.php?t=42884) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), March 15, 2012
* [RedQueen 1.1.1 (bugfix release)](http://www.talkchess.com/forum/viewtopic.php?t=42892) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), March 15, 2012
* [RedQueen 1.1.1 on Mac OS X](http://www.talkchess.com/forum/viewtopic.php?t=42896) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), March 16, 2012
* [Redqueen 1.1.1 64-bit - Is this a bug?](http://www.talkchess.com/forum/viewtopic.php?t=43021) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), March 26, 2012
* [Redqueen v1.1.98 Linux/Windows 64 bit edition](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60130) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), May 11, 2016
* [RedQueen for the Mac](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60325) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), May 31, 2016


## External Links


### Chess Engine


* [GitHub - bhlangonijr/redqueenchess: Redqueen is an UCI (Universal Chess Interface) compatible chess engine written in C++](https://github.com/bhlangonijr/redqueenchess)
* [RedQueen Chess Engine website](https://sourceforge.net/projects/redqueenchess/)
* [RedQueen | Chess Engine](http://redqueenchess.sourceforge.net/)
* [RedQueen](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=RedQueen&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Red Queen (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Red_Queen)
* [Red Queen (Through the Looking-Glass) - Wikipedia](https://en.wikipedia.org/wiki/Red_Queen_%28Through_the_Looking-Glass%29)


 [Red Queen's race from Wikipedia](https://en.wikipedia.org/wiki/Red_Queen%27s_race)
* [The Red Queen's Race from Wikipedia](https://en.wikipedia.org/wiki/The_Red_Queen%27s_Race) ([Isaac Asimov](Category:Isaac_Asimov "Category:Isaac Asimov"))
* [Red Queen hypothesis from Wikipedia](https://en.wikipedia.org/wiki/Red_Queen_hypothesis)
* [Red Queen (comics) from Wikipedia](https://en.wikipedia.org/wiki/Red_Queen_%28comics%29)
* [The Red Queen: Sex and the Evolution of Human Nature - Wikipedia](https://en.wikipedia.org/wiki/The_Red_Queen:_Sex_and_the_Evolution_of_Human_Nature)
* [Gryphon](Category:Gryphon "Category:Gryphon") - Opening Move, [Red Queen to Gryphon Three](https://en.wikipedia.org/wiki/Red_Queen_to_Gryphon_Three) (1974, Remastered), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Illustration by [John Tenniel](Category:John_Tenniel "Category:John Tenniel") of the Red Queen lecturing [Alice](Alice "Alice") for [Lewis Carroll's](Category:Lewis_Carroll "Category:Lewis Carroll") "[Through The Looking Glass](https://en.wikipedia.org/wiki/Through_the_Looking-Glass)", 1871, [Red Queen (Through the Looking-Glass) - Wikipedia](https://en.wikipedia.org/wiki/Red_Queen_%28Through_the_Looking-Glass%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [RedQueen | Chess Engine](http://redqueenchess.sourceforge.net/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [redqueen-1.1.2-windows.zip download](http://sourceforge.net/projects/redqueenchess/), magicmoves.h, magicmoves.cpp
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [redqueen-1.1.2-windows.zip download](http://sourceforge.net/projects/redqueenchess/), bitboard.h
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [2011 6ht annual ACCA games (RedQueen's games)](http://www.talkchess.com/forum/viewtopic.php?t=41067) by [Ben-Hur Carlos Langoni](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), November 13, 2011

**[Up one Level](Engines "Engines")**







 
