---
title: Kurt
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Kurt**



[ Kurt Weill <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Kurt**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), written by [Oliver Uwira](Oliver_Uwira "Oliver Uwira") in [C](C "C"). Able to play [Chess960](Chess960 "Chess960"), Kurt participated at the [2nd Livingston Chess960 Computer World Championship 2006](Chess960CWC_2006 "Chess960CWC 2006") in [Mainz](https://en.wikipedia.org/wiki/Mainz). 
The last recent Kurt 0.9.2.2 beta is available from [Jim Ablett's](Jim_Ablett "Jim Ablett") site. 



### Sliding Piece Attacks


Kurt 0.9.2.x beta is a none [rotated](Rotated_Bitboards "Rotated Bitboards") [bitboard](Bitboards "Bitboards") engine <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and uses a three-dimensional pre-initialized [array](Array "Array") of 128 KByte to lookup [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), indexed by [square](Squares "Squares") (0..63), [line occupancy index](Occupancy_of_any_Line "Occupancy of any Line") (0..63, considering the [outer squares](First_Rank_Attacks#TheOuterSquares "First Rank Attacks")) and finally the four line [directions](Direction "Direction") (0..3) for [ranks](Ranks "Ranks"), [files](Files "Files"), [diagonals](Diagonals "Diagonals") and [anti-diagonals](Anti-Diagonals "Anti-Diagonals"). The six-bit line occupancy index is calculated from the masked line of empty squares, multiplied by a 64-bit [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence") <a id="cite-note-3" href="#cite-ref-3">[3]</a> for each square and direction, shifting the product right by 58 .




### BitScan


Kurt 0.9.2.x beta uses [Matt Taylor's](Matt_Taylor "Matt Taylor") [folded BitScan](BitScan#MattTaylorsFoldingtrick "BitScan"). Returning a [byte](Byte "Byte") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 




```C++

static const int LsbDeBruijnMap[64] =
{
   63, 30,  3, 32, 59, 14, 11, 33,
   60, 24, 50,  9, 55, 19, 21, 34,
   61, 29,  2, 53, 51, 23, 41, 18,
   56, 28,  1, 43, 46, 27,  0, 35,
   62, 31, 58,  4,  5, 49, 54,  6,
   15, 52, 12, 40,  7, 42, 45, 16,
   25, 57, 48, 13, 10, 39,  8, 44,
   20, 47, 38, 22, 17, 37, 36, 26
}; 

unsigned char LeastSignificantBit(bitboard b)
{
   unsigned int fold;
   b ^= (b - 1);
   fold = ((int) b) ^ ((int)(b>>32));
   return LsbDeBruijnMap[(fold * 0x78291acf) >> 26]; 
}

```

### Collapsing Files and Ranks


[Collapsed files](Occupancy_of_any_Line#CollapsedFiles "Occupancy of any Line") and [collapsed ranks](Occupancy_of_any_Line#CollapsedRanks "Occupancy of any Line"), as posted by [Urban Koistinen](Urban_Koistinen "Urban Koistinen") in 1997 <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and [Steffan Westcott](Steffan_Westcott "Steffan Westcott") in 2006 <a id="cite-note-6" href="#cite-ref-6">[6]</a> are used in 0.9.2.x for initialization purposes:




```C++

/**
 * CollapseFiles(bitboard) folds a bitboard vertically into an 8 bit word.
 * By or-ing the files of a bitboard, a 8-bit folded bitboard is calculated. 
 * E.g. by folding a bitboard containing the position of all pawns open files 
 * can be determined:
 *
 *    abcdefgh   
 *
 * 8  00000000   
 * 7  10100110   
 * 6  00010001                         abcdefgh
 * 5  00000000   => CollapseFiles() => 11110111
 * 4  00010000   
 * 3  00100000   Negating the result yields the open-property of
 * 2  11000011   the 8 files => the e-file is open.
 * 1  00000000   
 *
 *     Pawns
 */
unsigned char CollapseFiles(bitboard src)
{
   src |= src >> 32;
   src |= src >> 16;
   src |= src >>  8;
   return (unsigned char)(src & 0xff); 
}

/**
 * CollapseRanks() folds a bitboard horizontally into an 8 bit word.
 * This is similar to CollapseFiles(bitboard).
 */
unsigned char CollapseRanks(bitboard src)
{
   src |= src >> 4;   // No masking needed
   src |= src >> 2;   //    "         "
   src |= src >> 1;   //    "         "
   return (unsigned char)(((src & 0x0101010101010101) * 0x0102040810204080) >> 56); 
}

```

## Search


Kurt's [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") with [null move pruning](Null_Move_Pruning "Null Move Pruning") and [killer heuristic](Killer_Heuristic "Killer Heuristic") with two slots for [mate killers](Mate_Killers "Mate Killers") and other [killer moves](Killer_Move "Killer Move") each, kept in its parent's node structure. Further, [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") is used in [move ordering](Move_Ordering "Move Ordering") and [quiescence search](Quiescence_Search "Quiescence Search") [pruning](Pruning "Pruning"). 



## Evaluation


The [evaluation](Evaluation "Evaluation") is speeded up by a [hash table](Evaluation_Hash_Table "Evaluation Hash Table") and considers [material](Material "Material") and various positional terms such as [development](Development "Development"), [pawn structure](Pawn_Structure "Pawn Structure"), in particular [backward pawns](Backward_Pawn "Backward Pawn") and [passed pawns](Passed_Pawn "Passed Pawn"), and [king safety](King_Safety "King Safety").



## Forum Posts


* [One step forward again](http://www.talkchess.com/forum/viewtopic.php?t=36149) by [Oliver Uwira](Oliver_Uwira "Oliver Uwira"), [CCC](CCC "CCC"), September 22, 2010
* [New Version: Kurt 0.9.2 beta](http://www.talkchess.com/forum/viewtopic.php?t=36331) by [Oliver Uwira](Oliver_Uwira "Oliver Uwira"), [CCC](CCC "CCC"), October 11, 2010
* [New Version: Kurt 0.9.2 beta](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=51248) by [Oliver Uwira](Oliver_Uwira "Oliver Uwira"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 11, 2010


## External Links


### Chess Engine


* [Index of /chess/engines/Jim Ablett/KURT](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/KURT/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")


 [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/64 BIT/kurt](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/64%20BIT/kurt/)
* [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) by [Julien Marcel](Julien_Marcel "Julien Marcel")


### Misc


* [Kurt (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Kurt)
* [Kurt & Rolf Chess](http://www.utzingerk.com/) Homepage of [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger")
* [Kurt Richter from Wikipedia](https://en.wikipedia.org/wiki/Kurt_Richter)
* [Kurt Tucholsky from Wikipedia](https://en.wikipedia.org/wiki/Kurt_Tucholsky)
* [Kurt Wallander from Wikipedia](https://en.wikipedia.org/wiki/Kurt_Wallander)
* [Kurt Weill from Wikipedia](https://en.wikipedia.org/wiki/Kurt_Weill)
* [Louis Armstrong](https://en.wikipedia.org/wiki/Louis_Armstrong) - [Mack the Knife](https://en.wikipedia.org/wiki/Mack_the_Knife), [Hollywood Palace](https://en.wikipedia.org/wiki/The_Hollywood_Palace), May 01, 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Miloš Kopecký](https://en.wikipedia.org/wiki/Milo%C5%A1_Kopeck%C3%BD) - [Mackie Messer](http://de.wikipedia.org/wiki/Die_Moritat_von_Mackie_Messer), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Original caption (German): Kurt Weill in Wien, Kurt Weill, der bekannte Komponist der "[Drei-Groschen-Oper](https://en.wikipedia.org/wiki/The_Threepenny_Opera)", ist zur Premiere seines neuen Stückes "[Aufstieg und Fall der Stadt Mahagonny](https://en.wikipedia.org/wiki/Rise_and_Fall_of_the_City_of_Mahagonny)" nach [Wien](https://en.wikipedia.org/wiki/Vienna) gekommen, [German Federal Archives](https://en.wikipedia.org/wiki/German_Federal_Archives), [Kurt Weill from Wikipedia](https://en.wikipedia.org/wiki/Kurt_Weill)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [rotated bitboards obsolete?](https://www.stmintz.com/ccc/index.php?id=489834) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), February 26, 2006
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [De Bruijn sequence](De_Bruijn_Sequence "De Bruijn Sequence") factors are not required and work more like [random magic factors](Looking_for_Magics "Looking for Magics") here. File pattern for a [north-fill multiplication](General_Setwise_Operations#Multiplication "General Setwise Operations"), or diagonal pattern for a [flip-multiplication](Flipping_Mirroring_and_Rotating#FiletoaRank "Flipping Mirroring and Rotating"), as applied in [kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") are more stringent to map the [inner six squares](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") of any line to an 6-bit index
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> kurt\_0\_9\_2\_beta/src/bitboard.c, [New Version: Kurt 0.9.2 beta](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=51248) by [Oliver Uwira](Oliver_Uwira "Oliver Uwira"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 11, 2010
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Rotated bitboards](https://groups.google.com/d/msg/rec.games.chess.computer/YvFagyuVogw/2vNJw_qT8IYJ) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: Some thoughts on Dann Corbit's rotated alternative](https://www.stmintz.com/ccc/index.php?id=491079) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 03, 2006

**[Up one Level](Engines "Engines")**







 
