---
title: King PatternFloodFillAlgorithms
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* King Pattern**



 [](http://en.wikipedia.org/wiki/File:Moore_d.gif) Moore neighborhood <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**King pattern** are about **king attacks**, some [king safety](King_Safety "King Safety") issues and [pawn endgame](Pawn_Endgame "Pawn Endgame") related stuff. There is exactly one king per side - the whole game. Not a big issue, but even if white and black kings are member of the [standard bitboard definition](Bitboard_Board-Definition "Bitboard Board-Definition") one may avoid [bitscanning](BitScan "BitScan") whole the time. Even without explicit [piece-lists](Piece-Lists "Piece-Lists") , one may consider to keep the redundant king-squares [incrementally updated](Incremental_Updates "Incremental Updates") during [make](Make_Move "Make Move")/[unmake](Unmake_Move "Unmake Move"). 




### Contents


* [1 King Attacks](#king-attacks)
	+ [1.1 by Lookup](#by-lookup)
	+ [1.2 by Calculation](#by-calculation)
* [2 King Safety](#king-safety)
	+ [2.1 Pawn-Shield Pattern](#pawn-shield-pattern)
	+ [2.2 Vulnerable on distant Checks](#vulnerable-on-distant-checks)
		- [2.2.1 Branchless](#branchless)
		- [2.2.2 SSE4](#sse4)
* [3 King and Pawns](#king-and-pawns)
	+ [3.1 Set-wise Rule of the Square](#set-wise-rule-of-the-square)
	+ [3.2 Flood Fill Algorithms](#flood-fill-algorithms)
* [4 See also](#see-also)
* [5 External Links](#external-links)
* [6 References](#references)






The King [attacks](Attacks "Attacks") all squares in [Moore neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood), that is squares with a [Chebyshev distance](Distance "Distance") of one.



### by Lookup


Likely we have a the square-index handy, to access a table of precalculated king-attacks.




```C++

U64 arrKingAttacks[64];

U64 kingAttacks(enumSquare sq) {return arrKingAttacks[sq];}

```

For instance a king on g2:




```C++

. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . 1 1 1
. . . . . 1 . 1
. . . . . 1 1 1

```





### by Calculation


To calculate all eight [directions](Direction "Direction"), one can actually do some simple [parallel prefix stuff](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms"). Rather than to do a union of all eight [direction-steps](General_Setwise_Operations#OneStepOnly "General Setwise Operations"), one first applies the [horizontal attacks](General_Setwise_Operations#OneStepOnly "General Setwise Operations") considering file-wraps. Those up to two bits are then shifted up and down, together with the king-bitboard itself, to get all the other direction bits:




```C++

U64 kingAttacks(U64 kingSet) {
   U64 attacks = eastOne(kingSet) | westOne(kingSet);
   kingSet    |= attacks;
   attacks    |= nortOne(kingSet) | soutOne(kingSet);
   return attacks;
}

```

The routine is handy to initialize the kingAttacks [arrays](Array "Array"):




```C++

U64 sqBB = 1;
for (int sq = 0; sq < 64; sq++, sqBB <<= 1)
   arrKingAttacks[sq] = kingAttacks(sqBB);

```

It must not necessarily called with single-populated bitboards, and is base of [king path fill algorithms](King_Pattern#FloodFillAlgorithms "King Pattern").




## King Safety


[King Safety](King_Safety "King Safety") is an important evaluation topic. Some bitboard pattern are about to recognize king safety related features. To evaluate those features is a complete other story.



### Pawn-Shield Pattern


During the [middlegame](Middlegame "Middlegame"), the king is encouraged to hide behind own pawn shields. Beside Considering open and half-open files on king's and adjacent files, one idea is to mask potential pawn shield pattern per wing of the king file - and to hash it to an appropriate index range to access tables with precalculated stuff. This mask might be used for kings on f1-h1 or f1-h2:




```C++

. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . 1 1 1
. . . . . 1 1 1
. . . . . . . .

```





### Vulnerable on distant Checks


Assuming we are aware of all taboo squares of the king. That is the union of own pieces with all opposite attacks, then we can simply calculate a move target set by relative complement of the king attacks.




```C++

moveTargets = arrKingAttacks[sq] & ~taboo;

```

If moveTargets is empty - the king has no move. The king might be vulnerable on distant checks from any [sliding piece](Sliding_Pieces "Sliding Pieces") [direction](Direction "Direction"), due to lack of any escape. Otherwise, the king might be vulnerable on distant checks, if escape squares are on one line only - either rank, file, diagonal or anti-diagonal:




```C++

if ( moveTargets == 0 )
{
   dirSet = 15; // vulnerable on all lines
}
else
{
   dirSet = 0;
   pattern = moveTargets | sqBBofKing;
   if ( pattern & rankBits[sq] == pattern )
      dirSet =  1; // vulnerable on rank, e.g. base rank
   else if ( pattern & fileBits[sq] == pattern )
      dirSet =  2; // vulnerable on file
   else if ( pattern & diagBits[sq] == pattern )
      dirSet =  4; // vulnerable on diagonal
   else if ( pattern & antiBits[sq] == pattern )
      dirSet =  8; // vulnerable on antidiagonal
}

```

### Branchless


Branchless in C - since boolean compare result is treated 0 or 1 arithmetically:




```C++

pattern = moveTargets | sqBBofKing;
dirSet  = ( pattern & rankBits[sq] == pattern ) * 1;
dirSet += ( pattern & fileBits[sq] == pattern ) * 2;
dirSet += ( pattern & diagBits[sq] == pattern ) * 4;
dirSet += ( pattern & antiBits[sq] == pattern ) * 8;

```

to possibly test later




```C++

if ( dirSet ) evaluate and look for possible distant mates

```





### SSE4


Using the [SSE4.1](SSE4#SSE4.1 "SSE4") PCMPEQQ [Quadword](Quad_Word "Quad Word") compare for equality instruction via [\_mm\_cmpeq\_epi64](http://msdn.microsoft.com/en-us/library/bb513998.aspx) intrinsic, following otherwise [SSE2](SSE2 "SSE2") approach might be applied:




```C++

struct SKingBits {
    U64 rankBits;
    U64 fileBits;
    U64 diagBits;
    U64 antiBits;
} XMM_ALIGN kingBits[64];

int dirSet(U64 pattern, int sq)
{
   static const U64 XMM_ALIGN weights[4] = {
     C64(0x0000000000000001),
     C64(0x0000000000000002),
     C64(0x0000000000000004),
     C64(0x0000000000000008)
   };
   __m128i x0, x1, x2;
   const __m128i* pKB = (__m128i*)(kingBits + sq);
   const __m128i* pW  = (__m128i*) weights;
   x2 = _mm_cvtsi64x_si128 (pattern);
   x2 = _mm_unpacklo_epi64 (x2, x2);
   x0 = _mm_and_si128   (x2, pKB[0]);
   x1 = _mm_and_si128   (x2, pKB[1]);
   x0 = _mm_cmpeq_epi64 (x0, x2);
   x1 = _mm_cmpeq_epi64 (x1, x2);
   x0 = _mm_and_si128   (x0, pW[0]);
   x1 = _mm_and_si128   (x1, pW[1]);
   x0 = _mm_or_si128    (x0, x1);
   x1 = _mm_unpackhi_epi64 (x0, x0);
   x0 = _mm_or_si128    (x0, x1);
   return _mm_cvtsi128_si32(x0);
}

```





## King and Pawns


Some [pawn endgame](Pawn_Endgame "Pawn Endgame") issues. A set-wise [rule of the square](Rule_of_the_Square "Rule of the Square") from king's point of view. Or does a king have a connected path along safe and empty squares to a certain square?




### Set-wise Rule of the Square


Assuming a black-king on g5 - white to move. What is the set of squares, where a king can never catch a white [passer](Passed_Pawn "Passed Pawn")? Or the inverse, where can passers might be caught, considering the [rule of the square](Rule_of_the_Square "Rule of the Square")? In this inverse case, where passers may be close enough, there are other aspects to consider like two distant passers, or passer supported by own king - here it is only about [races](index.php?title=Pawn_race&action=edit&redlink=1 "Pawn race (page does not exist)") between passers and opponent king. It is about a set-wise view, where the distance to promotion is greater or equal than the distance of the king. We need to consider **double pushes** from the initial rank though.




```C++

black king on g5    white passers         double pawn push, need
wtm                 possibly caught       to copy 3rd to 2nd rank
. . . . . . . .      . . . . . . . .      . . . . . . . .
. . . . . . . .      . . . . . . . .      . . . . . . . .
. . . . . . . .      . . . . . . . .      . . . . . . . .
. . . . . . K .      . . . 1 1 1 K 1      . . . 1 1 1 K 1
. . . . . . . .      . . 1 1 1 1 1 1      . . 1 1 1 1 1 1
. . . . . . . .      . 1 1 1 1 1 1 1      . 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1      . 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1      1 1 1 1 1 1 1 1

```

*Of course we may even mask off the base ranks since pawns can not exist there - but since we intersect with passers anyway, it don't cares.*


We need to consider [tempo](Tempo "Tempo"), if black to move, the area of caught grows accordantly:




```C++

black king on g5    white passers
btm                 possibly caught
. . . . . . . .      . . . . . . . .
. . . . . . . .      . . . . . . . .
. . . . . K K K      . . . 1 1 1 1 1
. . . . . K K K      . . 1 1 1 1 K 1
. . . . . K K K      . 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1

```

We can now pre-initialize an [array](Array "Array") of **caught pawn area** for each king square, for both black and white king as well as [side to move](Side_to_move "Side to move"):




```C++

U64 arrCaughtableArea[2][2][64];  // [color of king][side to move][square]

unCaughtable = whitePassers & ~arrCaughtableArea[black][white][squareOfBlackKing];

```

How can the array be initialized, how can we calculate it? That is already some special fill approach. For the mentioned black king, wtm case, we use the rank-distance of the black king to the 8th rank.




```C++

distance = rank(kingSquare) ^ 7; // 7 - rank

. . . . 3 . . .
. . . . 2 . . .
. . . . 1 . . .
. . . . K . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .

```

One solution is first expand the king-set distance (3) times, in east and west direction along the rank:




```C++

caughtable = kingBB;
for (i = 0; i < distance; i++)
   caughtable |= westOne(caughtable) | eastOne(caughtable);

. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . 1 1 1     . . . . 1 1 1 1      . . . 1 1 1 1 1
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .

```

Now it is about filling south-west and south-east rank(kingSquare) times, which finally results in the desired set of catchable passers. Special handling is required for the doubles pushes <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++

for (i = 0; i < rank(kingSquare)-2; i++)
   caughtable |= soutOne(westOne(caughtable) | caughtable | eastOne(caughtable) );
caughtable |= soutOne(caughtable) | 0xff;

. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .
. . . 1 1 1 1 1     . . . 1 1 1 1 1      . . . 1 1 1 1 1
. . 1 1 1 1 1 1     . . 1 1 1 1 1 1      . . 1 1 1 1 1 1
. . . . . . . .     . 1 1 1 1 1 1 1   |  . 1 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .   |  . 1 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .   v  1 1 1 1 1 1 1 1

```

To initialize black to move and white king arrays should not that difficult either - and is left to the ambitious reader.






### Flood Fill Algorithms


Answering questions like can a king on a1 reach h8 along this path?




```C++

. . . . . . 1 T
. . 1 1 1 1 . .
. 1 . . . . . .
. . 1 1 1 1 . .
. . . . . . 1 .
. . . . . . . 1
. . . . . . 1 .
F 1 1 1 1 1 . .

```

The **squaresAreConnected** flood-fill <a id="cite-note-3" href="#cite-ref-3">[3]</a> algorithm was introduced by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.


A flood fill algorithm, like the one below, starting at the "from" square and stopping if the fill hits the to" square or the fill can't make any more progress. The fill progresses in all directions at once, so should return an answer within a few iterations. Each iteration is pretty fast too, as it just a bunch of shifting and logic operations. And no lookup tables either.




```C++

/////////////////////////////////////////////////////////////////////////
//
// Returns true if a path of set bits in 'path' exists that 8-way connect
// any set bit in sq1 to any set bit of sq2

bool squaresAreConnected(U64 sq1, U64 sq2, U64 path)
{
   // With bitboard sq1, do an 8-way flood fill, masking off bits not in
   // path at every step. Stop when fill reaches any set bit in sq2, or
   // fill cannot progress any further

   if (!(sq1 &= path) || !(sq2 &= path)) return false;
                      // Drop bits not in path
                      // Early exit if sq1 or sq2 not on any path

   while(!(sq1 & sq2))
   {
      U64 temp = sq1;
      sq1 |= eastOne(sq1) | westOne(sq1);    // Set all 8 neighbours
      sq1 |= soutOne(sq1) | nortOne(sq1);
      sq1 &= path;                           // Drop bits not in path
      if (sq1 == temp) return false;         // Fill has stopped
   }
   return true;                              // Found a good path
}

```

## See also


* [All shortest Paths](All_Shortest_Paths "All Shortest Paths")
* [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
* [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")


## External Links


* [Checkmate pattern from Wikipedia](https://en.wikipedia.org/wiki/Checkmate_pattern)
* [Amon Düül II](Category:Amon_D%C3%BC%C3%BCl_II "Category:Amon Düül II") - Archangel Thunderbird (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Moore neighborhood from Wikipedia](https://en.wikipedia.org/wiki/Moore_neighborhood)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Thanks to Thomas Herges for pointing out a bug if kings are on the eighth rank
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Flood Fill from Wikipedia](https://en.wikipedia.org/wiki/Flood_fill)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: algorithm question](https://www.stmintz.com/ccc/index.php?id=251180.) answer by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") in [CCC](CCC "CCC") September 09, 2002

**[Up one Level](Bitboards "Bitboards")**







 
