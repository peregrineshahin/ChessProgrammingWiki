---
title: Vajolet
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Vajolet**



[ [Vajolet Towers](https://en.wikipedia.org/wiki/Vajolet_Towers) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Vajolet** and **Vajolet2**,  

are [UCI](UCI "UCI") compliant [open source chess engines](Category:Open_Source "Category:Open Source") by [Marco Belli](Marco_Belli "Marco Belli"), written in [C++](Cpp "Cpp") and released under the [GNU General Public License v3](Free_Software_Foundation#GPL "Free Software Foundation"). Vajolet, named after the [Vajolet Towers](https://en.wikipedia.org/wiki/Vajolet_Towers) in the [Dolomites](https://en.wikipedia.org/wiki/Dolomites), started its life in 2010 as [C#](C_sharp "C sharp") engine <a id="cite-note-2" href="#cite-ref-2">[2]</a>. When Marco worked through [Stef Luijten's](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)") tutorial on [Winglet](Winglet "Winglet"), *Writing a Chess Program in 99 Steps* <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>, he rewrote Vajolet in [C++](Cpp "Cpp") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Vajolet 2.03 played the [International Gsei Web Tournament 2013](IGWT_2013 "IGWT 2013") and qualified for the final of 8 Italian and 8 non Italian engines, where it lost from [iCE](ICE "ICE"). 



### Contents


* [1 Vajolet2](#vajolet2)
* [2 Description](#description)
	+ [2.1 Board Representation](#board-representation)
	+ [2.2 Search](#search)
		- [2.2.1 Selectivity](#selectivity)
		- [2.2.2 Move Ordering](#move-ordering)
		- [2.2.3 Transposition Table](#transposition-table)
	+ [2.3 Evaluation](#evaluation)
		- [2.3.1 Pawn Structure](#pawn-structure)
		- [2.3.2 King Safety](#king-safety)
		- [2.3.3 Caches](#caches)
		- [2.3.4 Misc](#misc)
* [3 Forum Posts](#forum-posts)
	+ [3.1 2010 ...](#2010-...)
	+ [3.2 2015 ...](#2015-...)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc-2)
* [5 References](#references)






**Vajolet2**, first released in May 2014, was another complete rewrite in [C++11](Cpp#11 "Cpp") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Apparently, [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") worked well for Vajolet2 <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## Description


### Board Representation


Vajolet2 is a [bitboard](Bitboards "Bitboards") engine and used a [kindergarten like](Kindergarten_Bitboards "Kindergarten Bitboards") technique taken from [Winglet](Winglet "Winglet") <a id="cite-note-8" href="#cite-ref-8">[8]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with 32 [KiB](https://en.wikipedia.org/wiki/Kibibyte) precalculated lookup tables[64][64] each on [ranks](Ranks "Ranks"), [files](Files "Files"), [diagonals](Diagonals "Diagonals") and [anti-diagonals](Anti-Diagonals "Anti-Diagonals"), indexed by [square](Squares "Squares") and hashed line [occupancy](Occupancy "Occupancy") - the [inner six bits](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") multiplied by a [magic factor](Magic_Bitboards "Magic Bitboards") and shifted right by the strange looking 57, while 58 is more natural to ensure a six bit index range, but factors are designed that the most significant bit of the 64-bit product will be clear <a id="cite-note-9" href="#cite-ref-9">[9]</a>. Since June 2016 with Vajolet2 2.2 [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") are determined by [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") implementation of [Magic Bitboards](Magic_Bitboards "Magic Bitboards"). Along with [piece lists](Piece-Lists "Piece-Lists"), Vajolet2 performs a [staged](Move_Generation#Staged "Move Generation") [legal move generation](Move_Generation#Legal "Move Generation") <a id="cite-note-10" href="#cite-ref-10">[10]</a>. 



### Search


The [search](Search "Search") uses C++ [function templates](https://en.wikipedia.org/wiki/Template_%28C%2B%2B%29#Function_templates) to distinguish between pure [alpha-beta](Alpha-Beta "Alpha-Beta") and [PVS](Principal_Variation_Search "Principal Variation Search"), for the main search as well for [quiescence](Quiescence_Search "Quiescence Search"). Vajolet2 2.1, released in January 2016, applies [Lazy SMP](Lazy_SMP "Lazy SMP") <a id="cite-note-11" href="#cite-ref-11">[11]</a>. The list of [selectivity](Selectivity "Selectivity") features is quite huge.



### Selectivity


* [Check Extensions](Check_Extensions "Check Extensions")
* [Delta Pruning](Delta_Pruning "Delta Pruning")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
* [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions")
* [Multi–ProbCut](ProbCut#MPC "ProbCut")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Razoring](Razoring "Razoring")
* [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
* [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Sibling Prediction Pruning](Sibling_Prediction_Pruning "Sibling Prediction Pruning")
* [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")


### [Move Ordering](Move_Ordering "Move Ordering")


* [Principal Variation Extraction](Principal_Variation "Principal Variation")
* [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [MVV-LVA](MVV-LVA "MVV-LVA")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Transposition Table](Transposition_Table "Transposition Table")


* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Four Bucket System](Transposition_Table#Bucket "Transposition Table")
* [Depth-preferred Replacement Scheme](Transposition_Table#ReplacementStrategies "Transposition Table")


### [Evaluation](Evaluation "Evaluation")


* [Material Balance](Material#Balance "Material")
* [Mobility](Mobility "Mobility")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Tapered Eval](Tapered_Eval "Tapered Eval")


### [Pawn Structure](Pawn_Structure "Pawn Structure")


* [Backward Pawn](Backward_Pawn "Backward Pawn")
* [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
* [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
* [Pawn Chain](Pawn_Chain "Pawn Chain")


### [King Safety](King_Safety "King Safety")


* [Pawn Shield](King_Safety#PawnShield "King Safety")
* [Pawn Storm](King_Safety#PawnStorm "King Safety")
* [Square Control](King_Safety#SquareControl "King Safety")


### [Caches](Hash_Table "Hash Table")


* [Evaluation Cache](Evaluation_Hash_Table "Evaluation Hash Table")
* [Material Cache](Material_Hash_Table "Material Hash Table")
* [Pawn Cache](Pawn_Hash_Table "Pawn Hash Table")


### Misc


* [Center Control](Center_Control "Center Control")
* [Loose Pieces](Loose_Piece "Loose Piece")
* [Number of Pawn Rams](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") as [Blockage Indicator](Blockage_Detection "Blockage Detection")


 and more ...
## Forum Posts


### 2010 ...


* [Vajolet Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=34545) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 27, 2010
* [Re: Test 071112](http://www.talkchess.com/forum/viewtopic.php?t=45918&start=4) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), November 10, 2012
* [vajolet 2.03 release](http://www.talkchess.com/forum/viewtopic.php?t=47974) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 12, 2013
* [vajolet 2.48 released](http://www.talkchess.com/forum/viewtopic.php?t=50170) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), November 21, 2013
* [floating point SSE eval](http://www.talkchess.com/forum/viewtopic.php?t=50472) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), December 13, 2013 » [Evaluation](Evaluation "Evaluation"), [Float](Float "Float"), [Score](Score "Score")
* [where can I make my engine play against human?](http://www.talkchess.com/forum/viewtopic.php?t=51302) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), February 16, 2014
* [Vajolet2 released](http://www.talkchess.com/forum/viewtopic.php?t=51786) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), March 29, 2014
* [vajolet2 1.43 released](http://www.talkchess.com/forum/viewtopic.php?t=53048) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), July 22, 2014
* [advanced tapered evalutation](http://www.talkchess.com/forum/viewtopic.php?t=53220) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), August 08, 2014 » [SSE](SSE "SSE"), [Tapered Eval](Tapered_Eval "Tapered Eval")
* [vajolet2 1.45 release](http://www.talkchess.com/forum/viewtopic.php?t=53299) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), August 15, 2014


### 2015 ...


* [Vajolet2 2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=56086) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), April 21, 2015
* [Vajolet 2.1 released](http://www.talkchess.com/forum/viewtopic.php?t=58762) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), January 01, 2016
* [Vajolet, new version 2.2](http://www.talkchess.com/forum/viewtopic.php?t=60535) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), June 19, 2016
* [vajolet2 2.3 release](http://www.talkchess.com/forum/viewtopic.php?t=63301) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), February 28, 2017
* [Vajolet2 2.4 Release](http://www.talkchess.com/forum/viewtopic.php?t=65770) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), November 19, 2017
* [Vajolet2 2.5 Release](http://www.talkchess.com/forum/viewtopic.php?t=66412) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), January 25, 2018
* [Vajolet2 2.6 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67828) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), June 26, 2018
* [Vajolet2 2.7 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70403) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), April 03, 2019
* [Vajolet2 2.8 release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72225) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), November 01, 2019


## External Links


### Chess Engine


* [GitHub - elcabesa/vajolet](https://github.com/elcabesa/vajolet/)
* [vajolet chess engine - Google Project Hosting](https://code.google.com/p/vajolet/)
* [vajoletChess Blog](http://vajoletchess.blogspot.it/)
* [Vajolet](http://www.g-sei.org/category/chess-engines/vajolet/) « [G 6](G_6 "G 6")
* [Vajolet](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Vajolet&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
* [Vajolet](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Vajolet&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Vajolet Towers from Wikipedia](https://en.wikipedia.org/wiki/Vajolet_Towers)
* [Torri del Vajolet / Vajolet Towers : Climbing, Hiking & Mountaineering : SummitPost](http://www.summitpost.org/torri-del-vajolet-vajolet-towers/150951)
* [Vajolet Towers](http://physics-server.uoregon.edu/~belitz/db_virtual/db_climbing/peaks/vajolet_towers.html) by [Dietrich Belitz](http://physics-server.uoregon.edu/~belitz/), July 29, 2004
* [Rosengarten group from Wikipedia](https://en.wikipedia.org/wiki/Rosengarten_group)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The Torri del Vaiolet in the [Dolomites](https://en.wikipedia.org/wiki/Dolomites), [Fassa Valley](https://en.wikipedia.org/w/index.php?title=Fassa_Valley), [Trentino](https://en.wikipedia.org/wiki/Trentino), [Italy](https://en.wikipedia.org/wiki/Italy), seen descending from the [Rifugio Passo Santner](https://it.wikipedia.org/wiki/Rifugio_Passo_Santner). In the bottom at the right the [Rifugio Re Alberto](https://it.wikipedia.org/wiki/Rifugio_Re_Alberto), Photo by [Vincenzo Gianferrari Pini](http://commons.wikimedia.org/wiki/User:Vincenzo_Gianferrari_Pini), August 8, 2000, [Vajolet Towers from Wikipedia](https://en.wikipedia.org/wiki/Vajolet_Towers)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Vajolet Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=34545) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 27, 2010
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Winglet, Writing a Chess Program in 99 Steps](http://web.archive.org/web/20120621100214/http://www.sluijten.com/winglet/) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Writing a chess program in xx steps](http://www.talkchess.com/forum/viewtopic.php?t=38787) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), April 18, 2011
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: where to start chess programming?](http://www.talkchess.com/forum/viewtopic.php?t=52709&start=18) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), June 22, 2014
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Vajolet2 released](http://www.talkchess.com/forum/viewtopic.php?t=51786) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), March 29, 2014
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Vajolet2 released](http://www.talkchess.com/forum/viewtopic.php?t=51786&start=22) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), March 31, 2014
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Writing a chess program in 99 steps - Move generation for sliding pieces](http://web.archive.org/web/20120621060943/http://www.sluijten.com/winglet/11movegen03.htm#Move_generation_for_sliding_pieces_-_magic_bitboards_) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> see Macros RANKATTACKS, FILEATTACKS, SLIDEA8H1ATTACKS, SLIDEA1H8ATTACKS, etc. in [vajolet2/source/browse/movegen.h](https://code.google.com/p/vajolet2/source/browse/movegen.h), or inline functions attackFromRook and attackFromBishop in the more recent [vajolet/source/browse/movegen.h](https://code.google.com/p/vajolet/source/browse/movegen.h)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [first achievement: MOVE GENERATOR](http://vajoletchess.blogspot.it/2013/11/first-achievement-move-generator.html)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Vajolet 2.1 released](http://www.talkchess.com/forum/viewtopic.php?t=58762) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), January 01, 2016

**[Up one Level](Engines "Engines")**







 
