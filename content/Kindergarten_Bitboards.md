---
title: Kindergarten Bitboards
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* Kindergarten Bitboards**



 [](http://www.imj.org.il/imagine/collections/item.asp?itemNum=194576) [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Group of Masks, 1939 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Kindergarten** bitboards <a id="cite-note-2" href="#cite-ref-2">[2]</a>,   
 
was a kind of interactive forum development <a id="cite-note-3" href="#cite-ref-3">[3]</a> with a lot of meanders <a id="cite-note-4" href="#cite-ref-4">[4]</a> . There were two issues involved - first to calculate the [occupancy of any line](Occupancy_of_any_Line "Occupancy of any Line") from the [occupied bitboard](Occupancy "Occupancy") <a id="cite-note-5" href="#cite-ref-5">[5]</a> - and second, compact and dense lookup tables. As a quintessence [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") came up with this nomination. It relies on fast 64-bit multiplication, but is otherwise quite resource friendly and a compromise between calculation and table-size. 



## File-Attacks


[Files](Files "Files") need tad more work. Shift the board left (arithmetical right!) to the A-file to mask it. To get the inner six bits, a [flip-multiplication](Flipping_Mirroring_and_Rotating#FiletoaRank "Flipping Mirroring and Rotating") by the c2-h7 diagonal is applied with further shift right 58. The lookup-table contains the A-file attacks, which are shifted "back" to the original file.




```C++

U64 aFileAttacks [8][64];  // 4 KByte

U64 fileAttacks(U64 occ, enumSquare sq) {
   const U64 aFile   = C64(0x0101010101010101);
   const U64 diac2h7 = C64(0x0080402010080400);
   occ = aFile  & (occ >> (sq&7));
   occ = (diac2h7 *  occ ) >> 58;
   return aFileAttacks[sq>>3][occ] << (sq&7);
}

```

This is how it works:




```C++

masked A-file    *  c2-h7 Diagonal    =  occupancy
H . . . . . . .     . . . . . . . .     . .[G F E D C B]    . . . . . . . .
G . . . . . . .     . . . . . . . 1     . . F E D C B A     . . . . . . . .
F . . . . . . .     . . . . . . 1 .     . . E D C B A .     . . . . . . . .
E . . . . . . .     . . . . . 1 . .     . . D C B A . .  >> . . . . . . . .
D . . . . . . .  *  . . . . 1 . . .  =  . . C B A . . .  58 . . . . . . . .
C . . . . . . .     . . . 1 . . . .     . . B A . . . .     . . . . . . . .
B . . . . . . .     . . 1 . . . . .     . . A . . . . .     . . . . . . . .
A . . . . . . .     . . . . . . . .     . . . . . . . .    [G F E D C B]. .

```

Note that the six inner bit occupancy is reversed - considered in the pre-calculated aFileAttacks [array](Array "Array"). This reversed lookup was justified to share first rank-attacks by all directions - with a dense lookup of 512 Byte. But the 4KByte tables outperform the additional multiplications and shift of the dense version - and one may alternatively multiply with the flipped diagonal, the c7-h2 anti-diagonal:




```C++

masked A-file    *  c7-h2 AntiDiag   =  occupancy
H . . . . . . .     . . . . . . . .     . .[B C D E F G]    . . . . . . . .
G . . . . . . .     . . 1 . . . . .     . . A B C D E F     . . . . . . . .
F . . . . . . .     . . . 1 . . . .     . . . A B C D E     . . . . . . . .
E . . . . . . .     . . . . 1 . . .     . . . . A B C D  >> . . . . . . . .
D . . . . . . .  *  . . . . . 1 . .  =  . . . . . A B C  58 . . . . . . . .
C . . . . . . .     . . . . . . 1 .     . . . . . . A B     . . . . . . . .
B . . . . . . .     . . . . . . . 1     . . . . . . . A     . . . . . . . .
A . . . . . . .     . . . . . . . .     . . . . . . . .    [B C D E F G]. .

```

## Shared Rank Lookup


As often, [computation versus memory size](Space-Time_Tradeoff "Space-Time Tradeoff"). One may share a 512Byte Lookup of the first rank by all lines with some trailing computation. Multiplying with the A-file (fill north) for ranks and diagonals, and multiplying with the diagonal for the file. Likely the additional multiplication don't pays off.




```C++

const BYTE firstRankAttacks[8][64];

U64 fileAttacks(U64 occ, enumSquare sq) {
   const U64 aFile   = C64(0x0101010101010101);
   const U64 hFile   = C64(0x8080808080808080);
   const U64 diaa1h8 = C64(0x8040201008040201);
   const U64 diac2h7 = C64(0x0080402010080400);

   unsigned int f = sq & 7;
   occ =   aFile   & (occ   >>  f);
   occ = ( diac2h7 *  occ ) >> 58;
   occ =   diaa1h8 * firstRankAttacks[(sq^56)>>3][occ];
   return ( hFile  &  occ ) >> (f^7);
}

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   const U64 aFile = C64(0x0101010101010101);
   const U64 bFile = C64(0x0202020202020202);

   unsigned int f = sq & 7;
   occ  =  diagonalMaskEx[sq] & occ;
   occ  = (bFile * occ ) >> 58;
   occ  =  aFile *  firstRankAttacks[f][occ];
   return  diagonalMaskEx[sq] & occ;
}

```

## 32-bit Versions


One other variation of the memory versus computation theme was encouraged by 32-bit mode. 64-bit multiplication is quite expensive in 32-bit mode - a call using three imuls. Thus, it is more efficient to use shift-or plus 32-bit multiplication, which might in fact be used in 64-bit mode as well. [Piotr Cichy](Piotr_Cichy "Piotr Cichy") proposed a multiplication less [parallel prefix shift](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") approach similar to [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line") <a id="cite-note-6" href="#cite-ref-6">[6]</a> , which is a good alternative for processors with slow multiplication.


An efficient and tricky file-approach was introduced by [Zach Wegner](Zach_Wegner "Zach Wegner") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, using a 32KByte, [rotated like](Rotated_Bitboards "Rotated Bitboards") lookup-table:
It is quite strange, yes, but it is an out of order mapping. There are only 5 bits because each bit in the factor maps more than one bit. The trick here is the odd shift 29, so that the multiply does not overflow individual bits. I have since found that 25 and 27 will work with the same magic:




```C++

occ
. . . . . . . .
a . . . . . . .
b . . . . . . .    occ | occ >> 29    * 0x01041041 with the index bracketed
c . . . . . . .    ...\               ...\               ...\
d . . . . . . .    d . . . . . . .    1 . . . . . . .    d a[f c e b d a]
e . . . . . . .    e . . a . . . .    . . 1 . . . . .    e b . a f c e b
f . . . . . . .    f . . b . . . .    . . . . 1 . . .    f c . b . . f c
. . . . . . . .    . . . c . . . .    1 . . . . . 1 .    . . . c . . . .

```

The interesting thing is that this works for any masked file. In fact if it was shifted to the a-file, you could get away with the 3-bit factor 0x00041040 (but using a shift of 23).




```C++

U64 arrFileAttacks[64][64]; // [sq][occ64] 32KByte

U64 fileAttacks(U64 occ, enumSquare sq) {
   occ &= fileMask[sq];
   U32 fold  = (U32)occ | (U32)(occ >> 29);
   U32 occ64 = fold * 0x01041041 >> 26;
   return arrFileAttacks[sq][occ64];
}

```

Ranks and diagonals are trivial, this version favors rotated like memory size for less computation and same operations than file-attacks. One may therefor generalize the routine by a line-direction parameter:




```C++

U64 arrDiagonalAttacks[64][64]; // [sq][occ64] 32KByte

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   occ &= diagonalMaskEx[sq];
   U32 fold  = (U32)occ | (U32)(occ >> 32);
   U32 occ64 = fold * 0x02020202 >> 26;
   return arrDiagonalAttacks[sq][occ64];
}

```

A similar approach was proposed by [Andrew Fan](Andrew_Fan "Andrew Fan") in 2009, been active in his [own engine](FireFly "FireFly") for a few years (2006 earliest recorded file time) <a id="cite-note-8" href="#cite-ref-8">[8]</a>.




## Magic Compression


So far Kindergarten bitboards performs a [perfect hashing](Hash_Table#PerfectHashing "Hash Table") of the up to six relevant and scattered occupied bits of any line to a six-bit index - which is a bijective mapping of 64 different occupancies per line to 64 indices for the precalculated attack sets.


If we have a closer look to the attack sets, say of a rook on the a-file, we enumerate far less disjoint sets. A rook on a1 (a8) has seven different attack-sets on that file, depending on the occupancy of a2-a7. On a2 (a7) there is even one attack set less, on a3 (a6) 2 times 5 and on a4 (a5) 3 times 4 attack-sets. Thus, there are {7, 6, 10, 12, 12, 10, 6, 7} disjoint attack-sets per square on line, or 70 in total over all eight squares.


While kindergarten bitboards apply a minimal perfect mapping of scattered bits to a six-bit index, the mapping of the attack-sets is surjective, since each of the 64 occupancies maps only up to 12 distinct sets. Of course that is because occupancies "behind" the first blocker are redundant and map the same attack.


[Grant Osborne](Grant_Osborne "Grant Osborne") came up with the idea, derived from [magic bitboards](Magic_Bitboards "Magic Bitboards") - to use different "magic" factors per square (rank), where multiplication may produce carries and enough so called constructive collisions to gain only five or even four bit indices and therefor denser tables. Since different squares may have different table sizes (16 or 32 entries), a Java-like [array](Array "Array") is used for the attacks, in C implemented as array of pointers to the arbitrary sized attack tables. The variable right shift by either 60 or 59 is encoded inside the otherwise redundant upper six bits of the magic factor, as mentioned in [incorporating the shift](Magic_Bitboards#IncorporatingtheShift "Magic Bitboards") of magic bitboards.


Grant's proposal, so far with {5,4,4,5,5,4,4,5} bit ranges for the lookups per square for vertical rook attacks, results in a 1.5 KByte array instead the 4KByte of the initial Kindergarten file attack getter <a id="cite-note-9" href="#cite-ref-9">[9]</a> . Whether the effort of the rank-indexed magic-factor plus additional pointer indirection pays off the memory saving is another question, and should be tried inside a concrete chess program with its individual cache- and memory footprint.




```C++

U64 aFileAttacks[4*32+4*16]; // 1.5KByte
U64 aPtrFileAttacks[8]; // points to appropriate aFileAttacks
U64 fileMagic[8] = {
   0xEFFFA39DB01B23A3, // 5-bit
   0xF024691A3227FF42, // 4-bit
   0xF2808817CAD6FF0C, // 4-bit see below
   0xED6EDFBE467977D5, // 5-bit
   0xEC87CB0D961EC43A, // 5-bit
   0xF2FF594E14D8801C, // 4-bit
   0xF2FF5D69D4E3E7D6, // 4-bit
   0xEE404B349599FF88  // 5-bit
};

U64 fileAttacks(U64 occ, enumSquare sq) {
   unsigned int file = sq &  7;
   unsigned int rank = sq >> 3;

   occ =  0x0001010101010100 & (occ >> file);
   occ = (fileMagic[rank] * occ) >> (fileMagic[rank] >> 58);  // four&five bit index
   return *(aPtrFileAttacks[rank] + occ) << file;
}

```

The table demonstrates how it works for file-attack of the a3 rook with a four bit range only five relevant occupied bits, since a3 is member of the inner six bits. The empirical determined factor is 0xF2808817CAD6FF0C, six upper bits contain the right shift for the product, for this square shift 60:





|  occupancy (A-File)
 |  product
 |  index 0..15
 |  attack set
 |
| --- | --- | --- | --- |
|  o - outer squares don't care
x - empty or any piece
. - empty
b - Blocker - any piece
R - Rook
 |  occupancy \*
`0xF2808817CAD6FF0C`
 |  upper
[nibble](Nibble "Nibble")
in
product
 |  1 attacked
. not attacked 
 |
|  o
x
x
x
b
R
b
o 
 |  1. attack-set
 |  |  .
.
.
.
1
.
1
. 
 |
| `0x0000010101000100` | `0x3A28F9D5E2FF0C00` |  3
 | `0x0000000001000100` |
| `0x0001010101000100` | `0x3934F9D5E2FF0C00` |  3
 | `0x0000000001000100` |
| `0x0000000101000100` | `0x6329EDD5E2FF0C00` |  6
 | `0x0000000001000100` |
| `0x0000010001000100` | `0x6F51FAC9E2FF0C00` |  6
 | `0x0000000001000100` |
| `0x0001000101000100` | `0x6235EDD5E2FF0C00` |  6
 | `0x0000000001000100` |
| `0x0001010001000100` | `0x6E5DFAC9E2FF0C00` |  6
 | `0x0000000001000100` |
| `0x0000000001000100` | `0x9852EEC9E2FF0C00` |  9
 | `0x0000000001000100` |
| `0x0001000001000100` | `0x975EEEC9E2FF0C00` |  9
 | `0x0000000001000100` |
|  o
x
x
x
b
R
.
o 
 |  2. attack set
 |  |  .
.
.
.
1
.
1
1 
 |
| `0x0000000001000000` | `0x17CAD6FF0C000000` |  1
 | `0x0000000001000101` |
| `0x0001000001000000` | `0x16D6D6FF0C000000` |  1
 | `0x0000000001000101` |
| `0x0000010101000000` | `0xB9A0E20B0C000000` |  11
 | `0x0000000001000101` |
| `0x0001010101000000` | `0xB8ACE20B0C000000` |  11
 | `0x0000000001000101` |
| `0x0000000101000000` | `0xE2A1D60B0C000000` |  14
 | `0x0000000001000101` |
| `0x0000010001000000` | `0xEEC9E2FF0C000000` |  14
 | `0x0000000001000101` |
| `0x0001000101000000` | `0xE1ADD60B0C000000` |  14
 | `0x0000000001000101` |
| `0x0001010001000000` | `0xEDD5E2FF0C000000` |  14
 | `0x0000000001000101` |
|  o
x
x
b
.
R
b
o 
 |  3. attack set
 |  |  .
.
.
1
1
.
1
. 
 |
| `0x0001010100000100` | `0x216A22D6D6FF0C00` |  2
 | `0x0000000101000100` |
| `0x0000010100000100` | `0x225E22D6D6FF0C00` |  2
 | `0x0000000101000100` |
| `0x0000000100000100` | `0x4B5F16D6D6FF0C00` |  4
 | `0x0000000101000100` |
| `0x0001000100000100` | `0x4A6B16D6D6FF0C00` |  4
 | `0x0000000101000100` |
|  o
x
x
b
.
R
.
o 
 |  4. attack set
 |  |  .
.
.
1
1
.
1
1
 |
| `0x0000010100000000` | `0xA1D60B0C00000000` |  10
 | `0x0000000101000101` |
| `0x0001010100000000` | `0xA0E20B0C00000000` |  10
 | `0x0000000101000101` |
| `0x0000000100000000` | `0xCAD6FF0C00000000` |  12
 | `0x0000000101000101` |
| `0x0001000100000000` | `0xC9E2FF0C00000000` |  12
 | `0x0000000101000101` |
|  o
x
b
.
.
R
b
o 
 |  5. attack set
 |  |  .
.
1
1
1
.
1
. 
 |
| `0x0000010000000100` | `0x578723CAD6FF0C00` |  5
 | `0x0000010101000100` |
| `0x0001010000000100` | `0x569323CAD6FF0C00` |  5
 | `0x0000010101000100` |
|  o
x
b
.
.
R
.
o 
 |  6. attack set
 |  |  .
.
1
1
1
.
1
1 
 |
| `0x0000010000000000` | `0xD6FF0C0000000000` |  13
 | `0x0000010101000101` |
| `0x0001010000000000` | `0xD60B0C0000000000` |  13
 | `0x0000010101000101` |
|  o
b
.
.
.
R
b
o 
 |  7. attack set
 |  |  .
1
1
1
1
.
1
. 
 |
| `0x0001000000000100` | `0x7F9417CAD6FF0C00` |  7
 | `0x0001010101000100` |
|  o
b
.
.
.
R
.
o 
 |  8. attack set
 |  |  .
1
1
1
1
.
1
1 
 |
| `0x0001000000000000` | `0xFF0C000000000000` |  15
 | `0x0001010101000101` |
|  o
.
.
.
.
R
b
o 
 |  9. attack set
 |  |  1
1
1
1
1
.
1
. 
 |
| `0x0000000000000100` | `0x808817CAD6FF0C00` |  8
 | `0x0101010101000100` |
|  o
.
.
.
.
R
.
o 
 |  10. attack set,
no blocker 
 |  |  1
1
1
1
1
.
1
1 
 |
| `0x0000000000000000` | `0x0000000000000000` |  0
 | `0x0101010101000101` |


## See also


* [Flipping, Mirroring and Rotating of Rank, File and Diagonal](Flipping_Mirroring_and_Rotating#RankFileAndDiagonal "Flipping Mirroring and Rotating")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
* [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")
* [Sliding Piece Attacks in OliThink](OliThink#SlidingPieceAttacks "OliThink")
* [Sliding Piece Attacks in Winglet](Winglet#SlidingAttacks "Winglet")


## Forum Posts


* [Re: Rotated bitboards](https://groups.google.com/d/msg/rec.games.chess.computer/YvFagyuVogw/2vNJw_qT8IYJ) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997 » [Collapsed files](Occupancy_of_any_Line#CollapsedFiles "Occupancy of any Line"), [Collapsed ranks](Occupancy_of_any_Line#CollapsedRanks "Occupancy of any Line")
* [rotated bitboards obsolete?](https://www.stmintz.com/ccc/index.php?id=489834) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), February 26, [2006](Timeline#2006 "Timeline")
* [Re: Some thoughts on Dann Corbit's rotated alternative](https://www.stmintz.com/ccc/index.php?id=491079) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 03, 2006
* [Compact Bitboard Attacks](http://www.open-aurec.com/wbforum/viewtopic.php?t=4523) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 14, [2006](Timeline#2006 "Timeline")
* [Zach's tricky 32-bit approach](http://www.open-aurec.com/wbforum/viewtopic.php?topic_view=threads&p=26851&t=4523) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 22, [2006](Timeline#2006 "Timeline")
* [Magic Bitboards Explained!](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5958) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 04, 2006
* [Kindergarten Bitboard Approach by Gerd Isenberg](http://www.talkchess.com/forum/viewtopic.php?t=24724) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), November 05, 2008 » [OliThink](OliThink "OliThink")
* [Kindergarten bitboards without multiplying](http://www.talkchess.com/forum/viewtopic.php?t=29296) by [Piotr Cichy](Piotr_Cichy "Piotr Cichy"), [CCC](CCC "CCC"), August 07, 2009
* [Kindergarten Bitboard help](http://www.talkchess.com/forum/viewtopic.php?t=30742) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), November 22, 2009
* [32-bit Magic experiments](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50616&p=192200) by [Andrew Fan](Andrew_Fan "Andrew Fan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2009 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Kindergarten bitboards and Xiangqi move genaration?](http://www.talkchess.com/forum/viewtopic.php?t=31348) by Han Chengye, [CCC](CCC "CCC"), December 30, 2009 » [Chinese Chess](Chinese_Chess "Chinese Chess")
* [Re: OliThink 5.9.5 is very small](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77339&start=44) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 06, 2021 » [OliThink](OliThink "OliThink")


## External Links


* [Kindergarten from Wikipedia](https://en.wikipedia.org/wiki/Kindergarten)
* [George Benson](Category:George_Benson "Category:George Benson") - [This Masquerade](https://en.wikipedia.org/wiki/This_Masquerade), 1976, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Pat Metheny](Category:Pat_Metheny "Category:Pat Metheny") and friends - [This Masquerade](https://en.wikipedia.org/wiki/This_Masquerade), [Jazz Baltica](https://en.wikipedia.org/wiki/Jazz_Baltica), July 6, 2003, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Nils Landgren](https://en.wikipedia.org/wiki/Nils_Landgren_%28musician%29), [Lars Danielsson](Category:Lars_Danielsson "Category:Lars Danielsson"), [Wolfgang Haffner](https://en.wikipedia.org/wiki/Wolfgang_Haffner), [Esbjörn Svensson](https://en.wikipedia.org/wiki/Esbj%C3%B6rn_Svensson), [Pat Metheny](Category:Pat_Metheny "Category:Pat Metheny"), [Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee - Group of Masks](http://www.imj.org.il/en/collections/194576?itemNum=194576), from the [Israel Museum](https://en.wikipedia.org/wiki/Israel_Museum)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Magic Bitboards Explained!](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5958) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin") and reply by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") to call it Kindergarten Bitboards, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 4, [2006](Timeline#2006 "Timeline")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Compact Bitboard Attacks](http://www.open-aurec.com/wbforum/viewtopic.php?t=4523) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 14, [2006](Timeline#2006 "Timeline")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [rotated bitboards obsolete?](https://www.stmintz.com/ccc/index.php?id=489834) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), February 26, [2006](Timeline#2006 "Timeline")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Some thoughts on Dann Corbit's rotated alternative](https://www.stmintz.com/ccc/index.php?id=491079) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 03, 2006
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Kindergarten bitboards without multiplying](http://www.talkchess.com/forum/viewtopic.php?t=29296) by [Piotr Cichy](Piotr_Cichy "Piotr Cichy"), [CCC](CCC "CCC"), August 07, 2009
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Zach's tricky 32-bit approach](http://www.open-aurec.com/wbforum/viewtopic.php?topic_view=threads&p=26851&t=4523) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 22, 2006
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [32-bit Magic experiments](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50616&p=192200) by [Andrew Fan](Andrew_Fan "Andrew Fan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2009
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: How to reduce the "bits" used in a magic number](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=198660&t=21329) by [Grant Osborne](Grant_Osborne "Grant Osborne"), [CCC](CCC "CCC"), July 04, 2008

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
