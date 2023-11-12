---
title: QuadBitboards
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Quad-Bitboards**


**Quad-Bitboards** are simply a [vector](Array "Array") of four bitboards for various purposes. Those vectors are suited for [SIMD-instruction sets](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") like [SSE2](SSE2 "SSE2") and may kept for instance in two 128-bit XMM-registers, or [AVX2](AVX2 "AVX2") with one 256-bit YMM-register.




### Contents


* [1 As Board-Definition](#as-board-definition)
* [2 SSE2 Conversions](#sse2-conversions)
	+ [2.1 To Hex Bitboards](#to-hex-bitboards)
	+ [2.2 To Mailbox](#to-mailbox)
* [3 As Sliding Piece Generators](#as-sliding-piece-generators)
* [4 Quotes](#quotes)
* [5 See also](#see-also)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






One application is to keep one quad-bitboard as compact [board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") with vertical [nibbles](Nibble "Nibble") as [piece or empty square codes](Pieces#PieceCoding "Pieces"):





|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  idx 10
 |  6
 |  6
 |  6
 |  6
 |  5
 |  5
 |  5
 |  5
 |  5
 |  ~
 |  0
 |  ...
 |  |  |  |  |  |  |  0
 |
|  idx 1
 |  3
 |  2
 |  1
 |  0
 |  9
 |  8
 |  7
 |  6
 |  5
 |  ~
 |  8
 |  7
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |
|  bb0
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  ~
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  black
 |
|  bb1
 |  0
 |  0
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  ~
 |  1
 |  0
 |  0
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  |  P
 |  .
 |  B
 |  .
 |  Q
 |  |
|  bb2
 |  0
 |  1
 |  1
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  ~
 |  0
 |  0
 |  1
 |  1
 |  1
 |  0
 |  1
 |  1
 |  0
 |  |  |  N
 |  B
 |  .
 |  |  K
 |
|  bb3
 |  1
 |  0
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  0
 |  ~
 |  0
 |  1
 |  0
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  |  |  .
 |  .
 |  R
 |  Q
 |  K
 |
|  |  r
 |  n
 |  b
 |  k
 |  q
 |  b
 |  n
 |  r
 |  p
 |  ~
 |  P
 |  R
 |  N
 |  B
 |  K
 |  Q
 |  B
 |  N
 |  R
 |



```C++

bb3    RQK        bb2   NB  K       bb1  P B Q         bb0   black
1 . . 1 1 . . 1   . 1 1 . 1 1 1 .   . . 1 1 . 1 . .    1 1 1 1 1 1 1 1
. . . . . . . .   . . . . . . . .   1 1 1 1 1 1 1 1    1 1 1 1 1 1 1 1
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   1 1 1 1 1 1 1 1    . . . . . . . .
1 . . 1 1 . . 1   . 1 1 . 1 1 1 .   . . 1 1 . 1 . .    . . . . . . . .

```

with following arbitrary square codes:





|  |  |  |
| --- | --- | --- |
|  empty
 |  square
 |  0000B
 |
|  white
 |  pawn
 |  0010B
 |
|  white
 |  knight
 |  0100B
 |
|  white
 |  bishop
 |  0110B
 |
|  white
 |  rook
 |  1000B
 |
|  white
 |  queen
 |  1010B
 |
|  white
 |  king
 |  1100B
 |
|  black
 |  pawn
 |  0011B
 |
|  black
 |  knight
 |  0101B
 |
|  black
 |  bishop
 |  0111B
 |
|  black
 |  rook
 |  1001B
 |
|  black
 |  queen
 |  1011B
 |
|  black
 |  king
 |  1101B
 |


This routine might be used rarely to get a square-centric piece, see also the [AVX2 version](AVX2#VerticalNibble "AVX2"):




```C++

int getPiece (const QBB & qbb, enumSquare sq) {
   return ((qbb.bb[0] >> sq) & 1)
      + 2*((qbb.bb[1] >> sq) & 1)
      + 4*((qbb.bb[2] >> sq) & 1)
      + 8*((qbb.bb[3] >> sq) & 1);
}

```

To get the disjoint bitboards similar to the [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") is about some bitwise operations:




```C++

black    = bb0
occupied =       bb1 | bb2 | bb3
odd      =       bb1 ^ bb2 ^ bb3  // pawn or knight or rook
white    = bb0 ^ occupied

bishops  =       bb1 & bb2
queens   =       bb1       & bb3
kings    =             bb2 & bb3

pawns    = odd & bb1
knight   = odd       & bb2
rooks    = odd             & bb3

```

The idea is during [make](Make_Move "Make Move")/[unmake move](Unmake_Move "Unmake Move") to xor the quad-bitboard by from- and to-aspects similar to the [hashkey](Zobrist_Hashing "Zobrist Hashing"). This implies the information of the moving and possibly captured piece is coded inside the move structure, as well as special moves like double push (triggering ep), [castling](Castling "Castling"), [en passant](En_passant "En passant") and [promotions](Promotions "Promotions").




```C++

qbb ^= fromTable[move.fromAspects()] ^ toTable[move.toAspects()];

```





## SSE2 Conversions


### To Hex Bitboards


A conversion of a quad-bitboard to 16 disjoint bitboards can be done quite efficiently with [SSE2](SSE2 "SSE2") instructions:




```C++

void quad2hexBB(U64 h[], const QBB &s) {
   __m128i a,b,c,d,e,f, m1;
   __m128i* p = (__m128i*) &s;
   a = b = d = p[0];    c = p[1];
   p     = (__m128i*) h;
   m1    = _mm_cmpeq_epi8(a, a);        // -1
   a     = _mm_or_si128  (a, c);
   d     = _mm_and_si128 (d, c);        // q3 &  q1    :    q2 &  q0
   e = a = _mm_xor_si128 (a, m1);       //~q3 & ~q1    :   ~q2 & ~q0
   b     = _mm_xor_si128 (b, d);        //~q3 &  q1    :   ~q2 &  q0
   f = c = _mm_xor_si128 (c, d);        // q3 & ~q1    :    q2 & ~q0
   a     = _mm_unpackhi_epi64 (a, a);   //~q3 & ~q1    :~q3 & ~q1
   e     = _mm_unpacklo_epi64 (e, b);   //   ~q2 &  q0 :   ~q2 & ~q0
   f     = _mm_unpacklo_epi64 (f, d);   //    q2 &  q0 :    q2 & ~q0
   b     = _mm_unpackhi_epi64 (b, b);   //~q3 &  q1    :~q3 &  q1
   c     = _mm_unpackhi_epi64 (c, c);   // q3 & ~q1    : q3 & ~q1
   d     = _mm_unpackhi_epi64 (d, d);   // q3 &  q1    : q3 &  q1
   p[0]  = _mm_and_si128 (a, e);        //~q3~q2~q1 q0 :~q3~q2~q1~q0
   p[1]  = _mm_and_si128 (b, e);        //~q3~q2 q1 q0 :~q3~q2 q1~q0
   p[2]  = _mm_and_si128 (a, f);        //~q3 q2~q1 q0 :~q3 q2~q1~q0
   p[3]  = _mm_and_si128 (b, f);        //~q3 q2 q1 q0 :~q3 q2 q1~q0
   p[4]  = _mm_and_si128 (c, e);        // q3~q2~q1 q0 : q3~q2~q1~q0
   p[5]  = _mm_and_si128 (d, e);        // q3~q2 q1 q0 : q3~q2 q1~q0
   p[6]  = _mm_and_si128 (c, f);        // q3 q2~q1 q0 : q3 q2~q1~q0
   p[7]  = _mm_and_si128 (d, f);        // q3 q2 q1 q0 : q3 q2 q1~q0
}

```

### To Mailbox


Converting the 64 vertical [nibbles](Nibble "Nibble") to a [8x8 board](8x8_Board "8x8 Board") is more expensive and should be avoided on the fly, let say once per node.




```C++

void quadBB2Board(char board[], const QBB &quad) {
   static u64 XMM_ALIGN sq2bb_masks[8] = {
      0x0101010101010101, 0x0202020202020202,
      0x0404040404040404, 0x0808080808080808,
      0x1010101010101010, 0x2020202020202020,
      0x4040404040404040, 0x8080808080808080,
   };
   __m128i t0, t1, t2, t3, b0, b1, b2, b3;
   __m128i* pm = (__m128i*) sq2bb_masks;
   __m128i* pq = (__m128i*) &quad;
   __m128i* pb = (__m128i*) board;
   // 1. bitboard 0x02:0x01
   t0    = pq[0];
   t1    = _mm_unpacklo_epi64(t0, t0);
   b0    = _mm_and_si128 (t1, pm[0]);
   b1    = _mm_srli_epi64 ( _mm_and_si128(t1, pm[1]), 2);
   b2    = _mm_srli_epi64 ( _mm_and_si128(t1, pm[2]), 4);
   b3    = _mm_srli_epi64 ( _mm_and_si128(t1, pm[3]), 6);
   // 2. bitboard 0x04:0x02
   t2    = _mm_unpackhi_epi64(t0, t0);
   b0    = _mm_or_si128 ( b0, _mm_slli_epi64( _mm_and_si128 (t2, pm[0]), 1));
   b1    = _mm_or_si128 ( b1, _mm_srli_epi64( _mm_and_si128 (t2, pm[1]), 1));
   b2    = _mm_or_si128 ( b2, _mm_srli_epi64( _mm_and_si128 (t2, pm[2]), 3));
   b3    = _mm_or_si128 ( b3, _mm_srli_epi64( _mm_and_si128 (t2, pm[3]), 5));
   // 3. bitboard 0x08:0x04
   t0    = pq[1];
   t1    = _mm_unpacklo_epi64(t0, t0);
   b0    = _mm_or_si128 ( b0, _mm_slli_epi64( _mm_and_si128 (t1, pm[0]), 2));
   b1    = _mm_or_si128 ( b1,                 _mm_and_si128 (t1, pm[1])    );
   b2    = _mm_or_si128 ( b2, _mm_srli_epi64( _mm_and_si128 (t1, pm[2]), 2));
   b3    = _mm_or_si128 ( b3, _mm_srli_epi64( _mm_and_si128 (t1, pm[3]), 4));
   // 4. bitboard 0x10:0x08
   t2    = _mm_unpackhi_epi64(t0, t0);
   b0    = _mm_or_si128 ( b0, _mm_slli_epi64( _mm_and_si128 (t2, pm[0]), 3));
   b1    = _mm_or_si128 ( b1, _mm_slli_epi64( _mm_and_si128 (t2, pm[1]), 1));
   b2    = _mm_or_si128 ( b2, _mm_srli_epi64( _mm_and_si128 (t2, pm[2]), 1));
   b3    = _mm_or_si128 ( b3, _mm_srli_epi64( _mm_and_si128 (t2, pm[3]), 3));
   // rotate 8*8 bytes (512 bit) in b0,b1,b2,b3
   t0    = _mm_srli_epi64 ( _mm_unpackhi_epi64(b0,b0), 1);
   t1    = _mm_srli_epi64 ( _mm_unpackhi_epi64(b1,b1), 1);
   t2    = _mm_srli_epi64 ( _mm_unpackhi_epi64(b2,b2), 1);
   t3    = _mm_srli_epi64 ( _mm_unpackhi_epi64(b3,b3), 1);
   b0    = _mm_unpacklo_epi8 (b0, t0);
   b1    = _mm_unpacklo_epi8 (b1, t1);
   b2    = _mm_unpacklo_epi8 (b2, t2);
   b3    = _mm_unpacklo_epi8 (b3, t3);
   t0    = _mm_unpacklo_epi16(b0, b1);
   t1    = _mm_unpackhi_epi16(b0, b1);
   t2    = _mm_unpacklo_epi16(b2, b3);
   t3    = _mm_unpackhi_epi16(b2, b3);
   pb[0] = _mm_unpacklo_epi32(t0, t2);
   pb[1] = _mm_unpackhi_epi32(t0, t2);
   pb[2] = _mm_unpacklo_epi32(t1, t3);
   pb[3] = _mm_unpackhi_epi32(t1, t3);
}

```

## As Sliding Piece Generators


Another application is to perform [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") algorithms with quad-bitboards. That allows to propagate four or up to 15 bitboards with one direction fill.




```C++

qbb.bb[0] = white rooks or queens
qbb.bb[1] = black rooks or queens
qbb.bb[2] = black king
qbb.bb[3] = white king

```

Using an appropriate [C++](Cpp "Cpp") QBB-class with overloaded operators using [SSE2](SSE2 "SSE2")-intrinsics, allows to write it in usual syntax...




```C++

void nortOccl(QBB &gen /* in, out */, U64 pro64) {
   QBB pro(pro64);
   gen |= pro & (gen <<  8);
   pro  = pro & (pro <<  8);
   gen |= pro & (gen << 16);
   pro  = pro & (pro << 16);
   gen |= pro & (gen << 32);
}

```

## Quotes


Quote by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") <a id="cite-note-1" href="#cite-ref-1">[1]</a>




```C++
A quad-bitboard is simply a dense board-structure, where arbitrary piece-code-nibbles reside vertically in four bitboards. Together with hashkeys (normal and pawnhash), ep and castle states, movecount, reversable movecount, and some more the whole board structure takes 64-bytes - and make/unmake is almost one simdwise "xor/add/and" instruction with delta[moveNr] on that board-structure.
Quad-bitboards with up to 15 arbitrary codes may be used in fill-algorithms, to generate the multiplexed quad-bitboard in one run with one common empty square propagator. But multiplexing and demultiplexing makes it rather hard to use efficiently.
One simpler coding scheme, where each bitboard is a disjoint set, is following:

```


```C++
bb0: white rooks or queens
bb1: white king
bb2: black king
bb3: black rooks or queens

```


```C++
Now we can fill this quad-bitboard left and right wise (and for the other directions as well). We can aggregate the real sliding attacks for the taboo sets of the opponent king. We can do simdwise leftFill(bb1:bb0) & rightFill(bb3:bb2) and rightFill(bb1:bb0) & leftFill(bb3:bb2) to get inbetween sets of sliders with opponent king. In case of a sliding check (no piece inbetween) we can use this set as possible target set of check-breaking moves. Otherwise we can intersect it with own pieces to get pinned pieces (in total and by direction) or with opposite pieces to get discovered checkers... 

```

## See also


* [AVX2 Bitboard Permutation](AVX2#BitboardPermutation "AVX2")
* [AVX2 Dumb7Fill](AVX2#Dumb7Fill "AVX2")
* [AVX2 Knight Attacks](AVX2#KnightAttacks "AVX2")
* [AVX2 Vertical Nibble](AVX2#VerticalNibble "AVX2")
* [Color Flipping](Color_Flipping "Color Flipping")
* [QBBEngine](QBBEngine "QBBEngine")
* [SSE2 Popcnt](SSE2#SSE2popcount "SSE2")


## Forum Posts


* [Quad-bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5859) by [Pradu](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 12, 2006
* [Hashing a quadboard from scratch](http://www.talkchess.com/forum/viewtopic.php?t=62239) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), November 23, 2016 » [Hash Table](Hash_Table "Hash Table")
* [Quad-bard vs bitboard : is it faster ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67328) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), May 04, 2018


## External Links


* [QBBEngine- a didactic engine](https://sites.google.com/site/pedonechess/a-didactic-engine) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato") » [QBBEngine](QBBEngine "QBBEngine")
* [Wes Montgomery](Category:Wes_Montgomery "Category:Wes Montgomery") - [Four on Six](https://en.wikipedia.org/wiki/The_Incredible_Jazz_Guitar_of_Wes_Montgomery), [BBC Two](https://en.wikipedia.org/wiki/BBC_Two), [London](https://en.wikipedia.org/wiki/London), May 7, 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Stan Tracey](https://en.wikipedia.org/wiki/Stan_Tracey), [Jackie Dougan](https://en.wikipedia.org/wiki/Jackie_Dougan), [Rick Laird](Category:Rick_Laird "Category:Rick Laird")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Quad-bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5859#p28389) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 12, 2006

**[Up one Level](Bitboards "Bitboards")**







 
