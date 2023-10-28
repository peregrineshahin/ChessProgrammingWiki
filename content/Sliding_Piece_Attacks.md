---
title: Sliding Piece Attacks
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Sliding Piece Attacks**



 [](http://www.carinajorgensen.com/Chess/queensstar.php) [Carina Jørgensen](Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen"), Queen's Star <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
This is basically about how to calculate [attack-sets](Attacks "Attacks") of [sliding pieces](Sliding_Pieces "Sliding Pieces") for [evaluation](Evaluation "Evaluation") and [move-generation](Move_Generation "Move Generation") purposes. While the attack-sets of [pawn](Pawn "Pawn"), [king](King "King") and [knight](Knight "Knight") are only dependent on their [origin square](Origin_Square "Origin Square"), sliding pieces like [rook](Rook "Rook"), [bishop](Bishop "Bishop") or [queen](Queen "Queen") have to consider [occupancy](Occupancy "Occupancy"), as [pieces](Pieces "Pieces") may block the attack-ray in one particular [direction](Direction "Direction"). 



### Contents


* [1 Move targets](#move-targets)
* [2 Single Sliding Piece Attacks](#single-sliding-piece-attacks)
	+ [2.1 On an empty Board](#on-an-empty-board)
	+ [2.2 Tinker's Approach](#tinker.27s-approach)
	+ [2.3 By Calculation](#by-calculation)
	+ [2.4 By Occupancy Lookup](#by-occupancy-lookup)
	+ [2.5 Miscellaneous](#miscellaneous)
* [3 Multiple Sliding Pieces](#multiple-sliding-pieces)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
	+ [5.1 1999](#1999)
	+ [5.2 2000 ...](#2000-...)
	+ [5.3 2005 ...](#2005-...)
	+ [5.4 2010 ...](#2010-...)
	+ [5.5 2015 ...](#2015-...)
	+ [5.6 2020 ...](#2020-...)
* [6 External Links](#external-links)
* [7 References](#references)






Move target sets from attack-sets require [intersection](General_Setwise_Operations#Intersection "General Setwise Operations")



* with opponent pieces for [captures](Captures "Captures")
* with all empty squares for [quiet moves](Quiet_Moves "Quiet Moves")






## Single Sliding Piece Attacks


The single sliding piece, a rook, bishop or queen is determined by square index, likely from a [bitscan](BitScan "BitScan") of a piece-wise [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") of a sliding piece bitboard from a [standard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition").



### On an empty Board


Sliding piece attack sets or their disjoint subsets on lines or rays on an otherwise empty board are that simple than none sliding pieces. They are often base of further attack calculations. 



* [Attacks on the otherwise empty Board](On_an_empty_Board "On an empty Board")


### Tinker's Approach


[Brian Richardson](Brian_Richardson "Brian Richardson") proposed a move generation approach as used in [Tinker](Tinker "Tinker") based on rook or bishop attacks on the otherwise empty board <a id="cite-note-2" href="#cite-ref-2">[2]</a>. While [serializing](Bitboard_Serialization "Bitboard Serialization") all potential targets, he tests for legality inside the loop body, that is whether the [inbetween squares](Square_Attacked_By#InBetween "Square Attacked By") of [origin](Origin_Square "Origin Square") and [target](Target_Square "Target Square") are empty. This is not in the "real" bitboard spirit to determine attack sets in advance rather than to test individual elements of a superset belonging to a set, but at least it allows traversing disjoint target sets i.e. for captures in [quiescence search](Quiescence_Search "Quiescence Search"). 



### By Calculation


Some [bit-twiddling](Bit-Twiddling "Bit-Twiddling") ray-wise and line-wise approaches, unfortunately not always for all directions.



* [Blockers and Beyond](Blockers_and_Beyond "Blockers and Beyond")
* [Classical Approach](Classical_Approach "Classical Approach")


 [Bitfoot - A/B Bitboards](Bitfoot#ABBitboards "Bitfoot")
 [CFish - AVX2 Attacks](CFish#AVX2_Attacks "CFish")
* [Exploding Bitboards](Exploding_Bitboards "Exploding Bitboards")
* [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")
* [Leorik Attacks](Leorik#LeorikAttacks "Leorik")
* [Obstruction Difference](Obstruction_Difference "Obstruction Difference")
* [Reverse Bitboards](Reverse_Bitboards "Reverse Bitboards")
* [SBAMG](SBAMG "SBAMG")
* [Shifted Bitboards](Shifted_Bitboards "Shifted Bitboards")
* [Subtracting a Rook from a Blocking Piece](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")






### By Occupancy Lookup


Covering line-attacks in one run, [magic bitboards](Magic_Bitboards "Magic Bitboards") even covers rook- and bishop-attacks in one run.



* [First Rank Attacks](First_Rank_Attacks "First Rank Attacks")
* [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
* [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")
* [Rotated Indices](Rotated_Indices "Rotated Indices")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")


 [Sliding Piece Attacks](OliThink#SlidingPieceAttacks "OliThink") in [OliThink](OliThink "OliThink")
* [Hashing Dictionaries](Hashing_Dictionaries "Hashing Dictionaries")
* [Congruent Modulo Bitboards](Congruent_Modulo_Bitboards "Congruent Modulo Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


 [BMI2 - PEXT Bitboards](BMI2#PEXTBitboards "BMI2")
* [Sherwin Bitboards](Sherwin_Bitboards "Sherwin Bitboards")


 [SISSY Bitboards](SISSY_Bitboards "SISSY Bitboards")
* [Titboards](Titboards "Titboards")


### Miscellaneous


* [The Switch Approach](The_Switch_Approach "The Switch Approach")
* [SIMD Techniques](SIMD_Techniques "SIMD Techniques")
* [Hiding the Implementation](Hiding_the_Implementation "Hiding the Implementation")






## Multiple Sliding Pieces


For bitsets with multiple sliding pieces one can apply a [fill algorithm](Fill_Algorithms "Fill Algorithms") in each of the eight [ray-directions](Rays#RayDirections "Rays") to determine attacks. Since we keep disjoint directions, there is still a unique 1:1 relation from each bit of the target set to it's source square. This approach is great to determine target sets we may reach in two or more moves. One may use the union of rooks and queen(s), respectively bishops or queen(s) though.



* [Dumb7Fill](Dumb7Fill "Dumb7Fill")


 [AVX2 Dumb7Fill](AVX2#Dumb7Fill "AVX2")
* [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
* [Fill by Subtraction](Fill_by_Subtraction "Fill by Subtraction")


If applied for [move generation](Move_Generation "Move Generation") we better traverse directions rather than sliding pieces. Naturally this approach becomes less efficient, the less sliders are processed in parallel. Of course, one should avoid processing empty sets.



## See also


* [Efficient Generation of Sliding Piece Attacks](Efficient_Generation_of_Sliding_Piece_Attacks "Efficient Generation of Sliding Piece Attacks"), a Summary of selected attack generation techniques, a short Talk by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") from the [Workshop Chess and Mathematics](Workshop_Chess_and_Mathematics "Workshop Chess and Mathematics"), [Dresden](https://en.wikipedia.org/wiki/Dresden), November 21st and 22nd, 2008
* [Combinatorial Logic - Combinatorial Attacks](Combinatorial_Logic#CombinatorialAttackandDefendMap "Combinatorial Logic")
* [Sequential Logic - Sequential Rook Attack](Sequential_Logic#SequentialRookAttack "Sequential Logic")
* [Vector Attacks](Vector_Attacks "Vector Attacks")


## Forum Posts


### 1999


* [Re: How do you represent chess boards in your chess programms](https://www.stmintz.com/ccc/index.php?id=71016) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), September 29, 1999


### 2000 ...


* [Movegen Re: Bitmap Type Re: Tinker 81 secs Re: Testing speed](https://www.stmintz.com/ccc/index.php?id=107485) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), April 24, 2000
* [An idea to generate rook moves without rotated BBs](https://www.stmintz.com/ccc/index.php?id=134490) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), October 22, 2000
* [sliding attacks in three #define](https://www.stmintz.com/ccc/index.php?id=359243) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), April 09, 2004


### 2005 ...


* [BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?t=16002) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), August 24, 2007


 [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140111&t=16002) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), August 24, 2007
* [Yet another bitboard attack generator](http://www.talkchess.com/forum/viewtopic.php?t=30356) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), October 28, 2009
* [Other attack generator just for good measure ... C++ only...](http://www.talkchess.com/forum/viewtopic.php?t=30369) by [Filip Tvrzsky](index.php?title=Filip_Tvrzsky&action=edit&redlink=1 "Filip Tvrzsky (page does not exist)"), [CCC](CCC "CCC"), October 29, 2009
* [Caching AttackSets](http://www.talkchess.com/forum/viewtopic.php?t=30542) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), November 09, 2009


### 2010 ...


* [Bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51076) by Jeroen de Bruin, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2010
* [Low memory usage attack bitboard generation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51996) by crystalclear, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 06, 2011
* [Re: Bitboard implementation, how much time?](http://www.talkchess.com/forum/viewtopic.php?p=446380) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 26, 2012
* [Simplest bitboard attack generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=49562) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), October 03, 2013
* [152k rook and bishop attacks using PEXT and PDEP](http://www.talkchess.com/forum/viewtopic.php?t=49611) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), October 06, 2013 » [BMI2](BMI2 "BMI2")


### 2015 ...


* [On Rook tables in magic move generation](http://www.talkchess.com/forum/viewtopic.php?t=55418) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), February 22, 2015
* [Yet another way of generating sliding attack masks](http://www.talkchess.com/forum/viewtopic.php?t=55604) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), March 09, 2015
* [New idea for Rook magic moves storage](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=55739) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 22, 2015
* [Slider attack mask generation without table lookup](http://www.talkchess.com/forum/viewtopic.php?t=56468) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), May 24, 2015
* [Comparison of bitboard attack-getter variants](http://www.talkchess.com/forum/viewtopic.php?t=58795) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 04, 2016
* [SBAMG - Completing Hyperbola Quintessence](http://www.talkchess.com/forum/viewtopic.php?t=59845) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), April 10, 2016
* [very small bitboard move/attack generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68741) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 27, 2018


### 2020 ...


* [New RookAttacks() - possibly](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73063) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), February 12, 2020
* [scan-cut slider attack generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73082) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 13, 2020  » [A/B Bitboards](Bitfoot#ABBitboards "Bitfoot")
* [Split Index Super Set Yielding (SISSY) Bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73083) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), February 13, 2020 » [SISSY Bitboards](SISSY_Bitboards "SISSY Bitboards")
* [I did some magic bitboard "science" and mostly learned not to worry about it](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77133) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), April 20, 2021
* [Combining two of Bob's classic bitboard attack getters](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78693) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 19, 2021
* [Faster than Fancy magic: Hypercube Slider lookup [TEASER]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78843) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), December 09, 2021
* [Hypercube Slider Lookup - New Sliding Piece Algorithm [RELEASE]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79004) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), December 31, 2021
* [Comparison of all known Sliding lookup algorithms](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79005) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), December 31, 2021
* [Comparison of all known Sliding lookup algorithms [CUDA]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79078) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), January 08, 2022 » [GPU](GPU "GPU")
* [Binary Neural Networks Sliding Piece Inference [Release]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79332) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), February 10, 2022 » [Neural Networks](Neural_Networks "Neural Networks")


## External Links


* [Slide attack from Wikipedia](https://en.wikipedia.org/wiki/Slide_attack)
* [Cymande](Category:Cymande "Category:Cymande") - Brothers On The Slide, [KCRW](https://en.wikipedia.org/wiki/KCRW) session, [Santa Monica](https://en.wikipedia.org/wiki/Santa_Monica,_California), 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Queen's Star](http://www.carinajorgensen.com/Chess/queensstar.php) 2009 by [Carina Jørgensen](Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Movegen Re: Bitmap Type Re: Tinker 81 secs Re: Testing speed](https://www.stmintz.com/ccc/index.php?id=107485) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), April 24, 2000

**[Up one Level](Bitboards "Bitboards")**







 
