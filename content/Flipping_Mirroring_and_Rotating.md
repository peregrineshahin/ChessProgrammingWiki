---
title: Flipping Mirroring and Rotating
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * Flipping, Mirroring and Rotating**

[](http://www.barbaramittman.com/Site/Fore_4.html) [Barbara Mittman](Category:Barbara_Mittman "Category:Barbara Mittman"), Forever IV <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Flipping, Mirroring and Rotating**

might be useful to transform bitboards in various ways. Considering the [fourfold symmetry](Chessboard#FourFoldSymmetry "Chessboard") of the [chessboard](Chessboard "Chessboard"), the first paragraph covers the whole bitboard performing [bit-twiddling](Bit-Twiddling "Bit-Twiddling")-techniques. Various multiplications to flip or mirror certain subsets of the bitboard like [files](Files "Files"), [ranks](Ranks "Ranks") and even [diagonals](Diagonals "Diagonals") and [anti-diagonals](Anti-Diagonals "Anti-Diagonals") are mentioned in the second section.

## The whole Bitboard

Following [C](C "C")-routines perform [parallel prefix algorithms](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") to [swap bits](General_Setwise_Operations#SwappingBits "General Setwise Operations") in various ways. They are not intended to use extensively inside a chess program - e.g. to implement [rotated](Rotated_Bitboards "Rotated Bitboards") or [reverse bitboards](Reverse_Bitboards "Reverse Bitboards") on the fly - but may be used for initialization purposes. They may convert sets between the eight different [square mappings](Square_Mapping_Considerations "Square Mapping Considerations"), considering rank-file or file-rank [endianness](Endianness "Endianness"). An exception might be the vertical flipping, which could be done by one fast [x86-64](X86-64 "X86-64") byteswap ([bswap](X86-64#gpinstructions "X86-64")) instruction <a id="cite-note-2" href="#cite-ref-2">[2]</a> . See the bswap-application of [hyperbola quintessence](Hyperbola_Quintessence "Hyperbola Quintessence") to determine vertical or diagonal sliding attacks. Flipping, mirroring and rotating is distributive over the basic bitwise operations such as intersection, union, one's complement and xor, as demonstrated in hyperbola quintessence as well.

Beside portable routines, there are optimized routines taking advantage of compiler intrinsics, to use [x86-64](X86-64 "X86-64") processor instructions like byteswap (bswap) as mentioned and rotate ([ror, rol](X86-64#gpinstructions "X86-64")) <a id="cite-note-3" href="#cite-ref-3">[3]</a> .

## Flip and Mirror

This is about

- [flipping vertically](#FlipVertically)
- [mirroring horizontally](#MirrorHorizontally)
- [flipping along the diagonal](#FlipabouttheDiagonal)
- [flipping along the antidiagonal](#FlipabouttheAntidiagonal)

```C++

. 1 1 1 1 . . .   . 1 1 1 1 . . .   . 1 1 1 1 . . .   . 1 1 1 1 . . .
. 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .
. 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .
. 1 . . 1 . . .   . 1 . . 1 . . .   . 1 . . 1 . . .   . 1 . . 1 . . .
. 1 1 1 . . . .   . 1 1 1 . . . .   . 1 1 1 . . . .   . 1 1 1 . . . .
. 1 . 1 . . . .   . 1 . 1 . . . .   . 1 . 1 . . . .   . 1 . 1 . . . .
. 1 . . 1 . . .   . 1 . . 1 . . .   . 1 . . 1 . . .   . 1 . . 1 . . .
. 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .   . 1 . . . 1 . .
       -                 |                  /               \
 flipVertical     mirrorHorizontal  flipDiagA1H8      flipDiagA8H1
       -                 |                /                   \
. 1 . . . 1 . .   . . . 1 1 1 1 .   . . . . . . . .   . . . . . . . .
. 1 . . 1 . . .   . . 1 . . . 1 .   . . . . . . . .   1 1 1 1 1 1 1 1
. 1 . 1 . . . .   . . 1 . . . 1 .   1 . . . . 1 1 .   1 . . . 1 . . .
. 1 1 1 . . . .   . . . 1 . . 1 .   . 1 . . 1 . . 1   1 . . . 1 1 . .
. 1 . . 1 . . .   . . . . 1 1 1 .   . . 1 1 . . . 1   1 . . 1 . . 1 .
. 1 . . . 1 . .   . . . . 1 . 1 .   . . . 1 . . . 1   . 1 1 . . . . 1
. 1 . . . 1 . .   . . . 1 . . 1 .   1 1 1 1 1 1 1 1   . . . . . . . .
. 1 1 1 1 . . .   . . 1 . . . 1 .   . . . . . . . .   . . . . . . . .

```

### Vertical

```C++

. 1 1 1 1 . . .     . 1 . . . 1 . .
. 1 . . . 1 . .     . 1 . . 1 . . .
. 1 . . . 1 . .     . 1 . 1 . . . .
. 1 . . 1 . . .     . 1 1 1 . . . .
. 1 1 1 . . . .     . 1 . . 1 . . .
. 1 . 1 . . . .     . 1 . . . 1 . .
. 1 . . 1 . . .     . 1 . . . 1 . .
. 1 . . . 1 . .     . 1 1 1 1 . . .

```

Flipping a bitboard **vertical** reverses all eight bytes - it performs a little- big-endian conversion or vice versa. A scalar square may be flipped vertically by xor 56.

```C++

sq' = sq ^ 56;

```

The obvious approach with 21 operations, note that the shifts by 56 don't need masks:

```C++

/**
 * Flip a bitboard vertically about the centre ranks.
 * Rank 1 is mapped to rank 8 and vice versa.
 * @param x any bitboard
 * @return bitboard x flipped vertically
 */
U64 flipVertical(U64 x) {
    return  ( (x << 56)                           ) |
            ( (x << 40) & C64(0x00ff000000000000) ) |
            ( (x << 24) & C64(0x0000ff0000000000) ) |
            ( (x <<  8) & C64(0x000000ff00000000) ) |
            ( (x >>  8) & C64(0x00000000ff000000) ) |
            ( (x >> 24) & C64(0x0000000000ff0000) ) |
            ( (x >> 40) & C64(0x000000000000ff00) ) |
            ( (x >> 56) );
}

```

The [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")-approach takes 13 operations, to swap bytes, words and double-words in a [SWAR-wise](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") manner, performing three [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"):

```C++

/**
 * Flip a bitboard vertically about the centre ranks.
 * Rank 1 is mapped to rank 8 and vice versa.
 * @param x any bitboard
 * @return bitboard x flipped vertically
 */
U64 flipVertical(U64 x) {
   const U64 k1 = C64(0x00FF00FF00FF00FF);
   const U64 k2 = C64(0x0000FFFF0000FFFF);
   x = ((x >>  8) & k1) | ((x & k1) <<  8);
   x = ((x >> 16) & k2) | ((x & k2) << 16);
   x = ( x >> 32)       | ( x       << 32);
   return x;
}

```

Using the [x86-64](X86-64 "X86-64") [\_byteswap_uint64](X86-64#gpinstructions "X86-64") or bswap64 intrinsics only takes one processor instruction in 64-bit mode.

```C++

/**
 * Flip a bitboard vertically about the centre ranks.
 * Rank 1 is mapped to rank 8 and vice versa.
 * @param x any bitboard
 * @return bitboard x flipped vertically
 */
U64 flipVertical(U64 x) {
   return _byteswap_uint64(x);
}

```

### Horizontal

```C++

. 1 1 1|1 . . .     . . . 1 1 1 1 .
. 1 . . . 1 . .     . . 1 . . . 1 .
. 1 . . . 1 . .     . . 1 . . . 1 .
. 1 . . 1 . . .     . . . 1 . . 1 .
. 1 1 1 . . . .     . . . . 1 1 1 .
. 1 . 1 . . . .     . . . . 1 . 1 .
. 1 . . 1 . . .     . . . 1 . . 1 .
. 1 . .|. 1 . .     . . 1 . . . 1 .

```

Horizontal mirroring reverses the bits of each byte. A scalar square may be mirrored horizontally by xor 7.

```C++

sq' = sq ^ 7;

```

The [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")-algorithm swaps bits, bit-duos and [nibbles](Nibble "Nibble") in a [SWAR-wise](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") manner, performing three [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"), 15 operations:

```C++

/**
 * Mirror a bitboard horizontally about the center files.
 * File a is mapped to file h and vice versa.
 * @param x any bitboard
 * @return bitboard x mirrored horizontally
 */
U64 mirrorHorizontal (U64 x) {
   const U64 k1 = C64(0x5555555555555555);
   const U64 k2 = C64(0x3333333333333333);
   const U64 k4 = C64(0x0f0f0f0f0f0f0f0f);
   x = ((x >> 1) & k1) | ((x & k1) << 1);
   x = ((x >> 2) & k2) | ((x & k2) << 2);
   x = ((x >> 4) & k4) | ((x & k4) << 4);
   return x;
}

```

Replacing bitwise 'or' of disjoint sets by 'add' and shift left by appropriate multiply - taking advantage of x86 lea instruction for multiplication with 2 and 4:

```C++

/**
 * Mirror a bitboard horizontally about the center files.
 * File a is mapped to file h and vice versa.
 * @param x any bitboard
 * @return bitboard x mirrored horizontally
 */
U64 mirrorHorizontal (U64 x) {
   const U64 k1 = C64(0x5555555555555555);
   const U64 k2 = C64(0x3333333333333333);
   const U64 k4 = C64(0x0f0f0f0f0f0f0f0f);
   x = ((x >> 1) & k1) +  2*(x & k1);
   x = ((x >> 2) & k2) +  4*(x & k2);
   x = ((x >> 4) & k4) + 16*(x & k4);
   return x;
}

```

Using [rotates](General_Setwise_Operations#Rotate "General Setwise Operations") instead of shifts in some clever way takes 13 operations (introduced by [Steffan Westcott](Steffan_Westcott "Steffan Westcott")). Disadvantage is each operation depends on the previous one, while the lea-approach gains some parallelism with same number of instructions.

```C++

/**
 * Mirror a bitboard horizontally about the center files.
 * File a is mapped to file h and vice versa.
 * @param x any bitboard
 * @return bitboard x mirrored horizontally
 */
U64 mirrorHorizontal (U64 x) {
   const U64 k1 = C64(0x5555555555555555);
   const U64 k2 = C64(0x3333333333333333);
   const U64 k4 = C64(0x0f0f0f0f0f0f0f0f);
   x ^= k4 & (x ^ rotateLeft(x, 8));
   x ^= k2 & (x ^ rotateLeft(x, 4));
   x ^= k1 & (x ^ rotateLeft(x, 2));
   return rotateRight(x, 7);
}

```

### Generalized

In [Knuth's](Donald_Knuth "Donald Knuth") *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, page 9, Knuth interprets the *magic masks* as 2-[adic](https://en.wikipedia.org/wiki/P-adic_number) fractions <a id="cite-note-4" href="#cite-ref-4">[4]</a> :

```C++

k1 = ...101010101010101010101010101010101 = -1/3
k2 = ...100110011001100110011001100110011 = -1/5
k4 = ...100001111000011110000111100001111 = -1/17

```

How the masks look on a chess board:

```C++

k1                  k2                  k4
-1/3                -1/5                -1/17
0x5555555555555555  0x3333333333333333  0x0F0F0F0F0F0F0F0F
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .

```

A parametrized flip, mirror or reverse (mirror and flip) might be generalized to let the compiler produce mentioned routines with flip or mirror as constant (or template) parameter. Otherwise, without compile time constants, the division at runtime is too expensive.

```C++

/**
 * Flip, mirror or reverse a bitboard
 * @param x any bitboard
 * @param flip the bitboard
 * @param mirror the bitboard
 * @return bitboard x flipped, mirrored or reversed
 */
U64 flipMirrorOrReverse(U64 x, bool flip, bool mirror)
{
   for (U32 i = 3*(1-mirror); i < 3*(1+flip); i++) {
      int s(      1  << i);
      U64 f( C64( 1) << s);
      U64 k( C64(-1) / (f+1) );
      x = ((x >> s) & k) + f*(x & k);
   }
   return x;
}

```

The loop variable 'i' runs from following ranges based on the boolean (0,1) parameters 'flip' and 'mirror':

```C++

mirror:   for (U32 i = 0; i < 3; i++)
flip:     for (U32 i = 3; i < 6; i++)
reverse := mirror && flip
          for (U32 i = 0; i < 6; i++)

```

With following formula for the [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations") constants ...

```C++

shift(i)  := s(i) := 1 << i
factor(i) := f(i) := 1 << s(i)
mask(i)   := k(i) := -1 / (f(i) + 1)

```

... and therefor following values for i = 0...5:

```C++

s(0)  1
f(0)  2
k(0)  0x5555555555555555 = 0xffffffffffffffff / (2+1)

s(1)  2
f(1)  4
k(1)  0x3333333333333333 = 0xffffffffffffffff / (4+1)

s(2)  4
f(2)  16
k(2)  0x0f0f0f0f0f0f0f0f = 0xffffffffffffffff / (16+1)

s(3)  8
f(3)  256
k(3)  0x00ff00ff00ff00ff = 0xffffffffffffffff / (256+1)

s(4)  16
f(4)  65536
k(4)  0x0000ffff0000ffff = 0xffffffffffffffff / (65536+1)

s(5)  32
f(5)  4294967296
k(5)  0x00000000ffffffff = 0xffffffffffffffff / (4294967296+1)

```

### Diagonal

**Flip about the Diagonal**

```C++

. 1 1 1 1 . . /     . . . . . . . .
. 1 . . . 1 . .     . . . . . . . .
. 1 . . . 1 . .     1 . . . . 1 1 .
. 1 . . 1 . . .     . 1 . . 1 . . 1
. 1 1 1 . . . .     . . 1 1 . . . 1
. 1 . 1 . . . .     . . . 1 . . . 1
. 1 . . 1 . . .     1 1 1 1 1 1 1 1
/ 1 . . . 1 . .     . . . . . . . .

```

A scalar square needs to swap rank and file.

```C++

sq' = ((sq >> 3) | (sq << 3)) & 63;
sq' = (sq * 0x20800000) >>> 26; // unsigned 32-bit shift, zeros no sign bits from left

```

Performing three [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"):

```C++

/**
 * Flip a bitboard about the diagonal a1-h8.
 * Square h1 is mapped to a8 and vice versa.
 * @param x any bitboard
 * @return bitboard x flipped about diagonal a1-h8
 */
U64 flipDiagA1H8(U64 x) {
   U64 t;
   const U64 k1 = C64(0x5500550055005500);
   const U64 k2 = C64(0x3333000033330000);
   const U64 k4 = C64(0x0f0f0f0f00000000);
   t  = k4 & (x ^ (x << 28));
   x ^=       t ^ (t >> 28) ;
   t  = k2 & (x ^ (x << 14));
   x ^=       t ^ (t >> 14) ;
   t  = k1 & (x ^ (x <<  7));
   x ^=       t ^ (t >>  7) ;
   return x;
}

```

How the masks look on a chess board:

```C++

k1                  k2                  k4
0x5500550055005500  0x3333000033330000  0x0F0F0F0F00000000
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .
. . . . . . . .     1 1 . . 1 1 . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     . . . . . . . .     1 1 1 1 . . . .
. . . . . . . .     . . . . . . . .     1 1 1 1 . . . .
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     . . . . . . . .
. . . . . . . .     1 1 . . 1 1 . .     . . . . . . . .
1 . 1 . 1 . 1 .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

```

### Anti-Diagonal

**Flip about the Anti-Diagonal**

```C++

\ 1 1 1 1 . . .     . . . . . . . .
. 1 . . . 1 . .     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     1 . . . 1 . . .
. 1 . . 1 . . .     1 . . . 1 1 . .
. 1 1 1 . . . .     1 . . 1 . . 1 .
. 1 . 1 . . . .     . 1 1 . . . . 1
. 1 . . 1 . . .     . . . . . . . .
. 1 . . . 1 . \     . . . . . . . .

```

Flip about the [Anti-Diagonal](Anti-Diagonals "Anti-Diagonals") results in the bit-reversal of flip about the Diagonal.
Thus, a scalar square needs not only swap rank and file, but also xor 63.

```C++

sq' = (((sq >> 3) | (sq << 3)) & 63) ^ 63;
sq' = ((sq * 0x20800000) >>> 26) ^ 63;  // unsigned 32-bit shift

```

Performing three [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"):

```C++

/**
 * Flip a bitboard about the antidiagonal a8-h1.
 * Square a1 is mapped to h8 and vice versa.
 * @param x any bitboard
 * @return bitboard x flipped about antidiagonal a8-h1
 */
U64 flipDiagA8H1(U64 x) {
   U64 t;
   const U64 k1 = C64(0xaa00aa00aa00aa00);
   const U64 k2 = C64(0xcccc0000cccc0000);
   const U64 k4 = C64(0xf0f0f0f00f0f0f0f);
   t  =       x ^ (x << 36) ;
   x ^= k4 & (t ^ (x >> 36));
   t  = k2 & (x ^ (x << 18));
   x ^=       t ^ (t >> 18) ;
   t  = k1 & (x ^ (x <<  9));
   x ^=       t ^ (t >>  9) ;
   return x;
}

```

How the masks look on a chess board:

```C++

k1                  k2                  k4
0xAA00AA00AA00AA00  0xCCCC0000CCCC0000  0xF0F0F0F00F0F0F0F
. 1 . 1 . 1 . 1     . . 1 1 . . 1 1     . . . . 1 1 1 1
. . . . . . . .     . . 1 1 . . 1 1     . . . . 1 1 1 1
. 1 . 1 . 1 . 1     . . . . . . . .     . . . . 1 1 1 1
. . . . . . . .     . . . . . . . .     . . . . 1 1 1 1
. 1 . 1 . 1 . 1     . . 1 1 . . 1 1     1 1 1 1 . . . .
. . . . . . . .     . . 1 1 . . 1 1     1 1 1 1 . . . .
. 1 . 1 . 1 . 1     . . . . . . . .     1 1 1 1 . . . .
. . . . . . . .     . . . . . . . .     1 1 1 1 . . . .

```

## Rotating

This is about

- [Rotation by 180 degrees](#Rotationby180degrees)
- [Rotation by 90 degrees Clockwise](#Rotationby90degreesClockwise)
- [Rotation by 90 degrees Anti-Clockwise](#Rotationby90degreesAnticlockwise)

Rotation can be deduced from flipping and mirroring in various ways.

```C++

                    mirrorHorizontal     flipDiagA1H8        flipDiagA8H1
. 1 1 1 1 . . .     . . . 1 1 1 1 .     . . . . . . . .     . . . . . . . .
. 1 . . . 1 . .     . . 1 . . . 1 .     . . . . . . . .     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     . . 1 . . . 1 .     1 . . . . 1 1 .     1 . . . 1 . . .
. 1 . . 1 . . .     . . . 1 . . 1 .     . 1 . . 1 . . 1     1 . . . 1 1 . .
. 1 1 1 . . . .     . . . . 1 1 1 .     . . 1 1 . . . 1     1 . . 1 . . 1 .
. 1 . 1 . . . .     . . . . 1 . 1 .     . . . 1 . . . 1     . 1 1 . . . . 1
. 1 . . 1 . . .     . . . 1 . . 1 .     1 1 1 1 1 1 1 1     . . . . . . . .
. 1 . . . 1 . .     . . 1 . . . 1 .     . . . . . . . .     . . . . . . . .
 flipVertical         rotate180        rotate90clockwise rotate90antiClockwise
. 1 . . . 1 . .     . . 1 . . . 1 .     . . . . . . . .     . . . . . . . .
. 1 . . 1 . . .     . . . 1 . . 1 .     1 1 1 1 1 1 1 1     . . . . . . . .
. 1 . 1 . . . .     . . . . 1 . 1 .     . . . 1 . . . 1     . 1 1 . . . . 1
. 1 1 1 . . . .     . . . . 1 1 1 .     . . 1 1 . . . 1     1 . . 1 . . 1 .
. 1 . . 1 . . .     . . . 1 . . 1 .     . 1 . . 1 . . 1     1 . . . 1 1 . .
. 1 . . . 1 . .     . . 1 . . . 1 .     1 . . . . 1 1 .     1 . . . 1 . . .
. 1 . . . 1 . .     . . 1 . . . 1 .     . . . . . . . .     1 1 1 1 1 1 1 1
. 1 1 1 1 . . .     . . . 1 1 1 1 .     . . . . . . . .     . . . . . . . .

```

### By 180 degrees - Bit-Reversal

```C++

. 1 1 1 1 . . .     . . 1 . . . 1 .
. 1 . . . 1 . .     . . . 1 . . 1 .
. 1 . . . 1 . .     . . . . 1 . 1 .
. 1 . . 1 . . .     . . . . 1 1 1 .
. 1 1 1 . . . .     . . . 1 . . 1 .
. 1 . 1 . . . .     . . 1 . . . 1 .
. 1 . . 1 . . .     . . 1 . . . 1 .
. 1 . . . 1 . .     . . . 1 1 1 1 .

```

Rotating by 180 degrees reverses all bits in a bitboard. A scalar square may be reversed by xor 63:

```C++

sq' = sq ^ 63; // 63 - sq;

```

Deduced from [flipping vertically](#FlipVertically) and [mirroring horizontally](#MirrorHorizontally). Both operation may be applied in different orders.

```C++

/**
 * Rotate a bitboard by 180 degrees.
 * Square a1 is mapped to h8, and a8 is mapped to h1.
 * @param x any bitboard
 * @return bitboard x rotated 180 degrees
 */
U64 rotate180 (U64 x) {
   return mirrorHorizontal (flipVertical (x) );
}

```

The resulting code applies six [delta swaps](General_Setwise_Operations#DeltaSwap "General Setwise Operations"):

```C++

/**
 * Rotate a bitboard by 180 degrees.
 * Square a1 is mapped to h8, and a8 is mapped to h1.
 * @param x any bitboard
 * @return bitboard x rotated 180 degrees
 */
U64 rotate180 (U64 x) {
   const U64 h1 = C64 (0x5555555555555555);
   const U64 h2 = C64 (0x3333333333333333);
   const U64 h4 = C64 (0x0F0F0F0F0F0F0F0F);
   const U64 v1 = C64 (0x00FF00FF00FF00FF);
   const U64 v2 = C64 (0x0000FFFF0000FFFF);
   x = ((x >>  1) & h1) | ((x & h1) <<  1);
   x = ((x >>  2) & h2) | ((x & h2) <<  2);
   x = ((x >>  4) & h4) | ((x & h4) <<  4);
   x = ((x >>  8) & v1) | ((x & v1) <<  8);
   x = ((x >> 16) & v2) | ((x & v2) << 16);
   x = ( x >> 32)       | ( x       << 32);
   return x;
}

```

### By 90 degrees Clockwise

```C++

. 1 1 1 1 . . .     . . . . . . . .
. 1 . . . 1 . .     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     . . . 1 . . . 1
. 1 . . 1 . . .     . . 1 1 . . . 1
. 1 1 1 . . . .     . 1 . . 1 . . 1
. 1 . 1 . . . .     1 . . . . 1 1 .
. 1 . . 1 . . .     . . . . . . . .
. 1 . . . 1 . .     . . . . . . . .

```

A scalar square swaps rank and file plus xor 56:

```C++

sq' = (((sq >> 3) | (sq << 3)) & 63) ^ 56;
sq' = ((sq * 0x20800000) >>> 26) ^ 56; // unsigned 32-bit shift

```

Deduced from [flipping vertically](#FlipVertically) and [flipping along the antidiagonal](#FlipabouttheAntidiagonal).

```C++

/**
 * Rotate a bitboard by 90 degrees clockwise.
 * @param x any bitboard
 * @return bitboard x rotated 90 degrees clockwise
 */
U64 rotate90clockwise (U64 x) {
   return flipVertical (flipDiagA1H8 (x) );
}

```

Note that

```C++

flipVertical (flipDiagA1H8 (x) ) == flipDiagA8H1 (flipVertical (x) )

```

### By 90 degrees Anti-Clockwise

```C++

. 1 1 1 1 . . .     . . . . . . . .
. 1 . . . 1 . .     . . . . . . . .
. 1 . . . 1 . .     . 1 1 . . . . 1
. 1 . . 1 . . .     1 . . 1 . . 1 .
. 1 1 1 . . . .     1 . . . 1 1 . .
. 1 . 1 . . . .     1 . . . 1 . . .
. 1 . . 1 . . .     1 1 1 1 1 1 1 1
. 1 . . . 1 . .     . . . . . . . .

```

A scalar square swaps rank and file plus xor 7:

```C++

sq' = (((sq >> 3) | (sq << 3)) & 63) ^ 7;
sq' = ((sq * 0x20800000) >>> 26) ^ 7;  // unsigned 32-bit shift

```

Deduced from [flipping vertically](#FlipVertically) and [flipping along the diagonal](#FlipabouttheDiagonal).

```C++

/**
 * Rotate a bitboard by 90 degrees anticlockwise.
 * @param x any bitboard
 * @return bitboard x rotated 90 degrees anticlockwise
 */
U64 rotate90antiClockwise (U64 x) {
   return flipDiagA1H8 (flipVertical (x) );
}

```

Note that

```C++

flipDiagA1H8 (flipVertical (x) ) == flipVertical (flipDiagA8H1 (x) )

```

## Pseudo-Rotation by 45 degrees

The chess-board is four-fold symmetry - thus there is no real 45 degree rotation in the mathematical sense. Anyway we may map [diagonals](Diagonals "Diagonals") and [anti-diagonals](Anti-Diagonals "Anti-Diagonals") to [ranks](Ranks "Ranks"), similar to [rotated bitboards](Rotated_Bitboards "Rotated Bitboards").

### Clockwise

The 15 [diagonals](Diagonals "Diagonals") are enumerated by (file - rank) - [nibble](Nibble "Nibble") wise [two's complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") F == (16) -1, 9 == (16) -7. Two shorter diagonals are file-aligned packed into one rank each. Note that the three lower bits are equal in each rank and bit three (the sign-bit inside a signed nibble) indicates a "negative" diagonal north the main diagonal.

```C++

9 A B C D E F 0     9 1 1 1 1 1 1 1
A B C D E F 0 1     A A 2 2 2 2 2 2
B C D E F 0 1 2     B B B 3 3 3 3 3
C D E F 0 1 2 3     C C C C 4 4 4 4
D E F 0 1 2 3 4     D D D D D 5 5 5
E F 0 1 2 3 4 5     E E E E E E 6 6
F 0 1 2 3 4 5 6     F F F F F F F 7
0 1 2 3 4 5 6 7     0 0 0 0 0 0 0 0

```

We need to rotate the A-H files vertically by 0 to 7 ranks - done parallel prefix wise. One square is therefor mapped by:

```C++

sq' = (sq + 8*(sq&7)) & 63;

```

The main-diagonal is rotated clockwise to the first rank - thus 45 degrees.

On using xor, see [bits from two sources by a mask](General_Setwise_Operations#BitsFrom2SourcesByMask "General Setwise Operations"). See [rotate](General_Setwise_Operations#Rotate "General Setwise Operations") for the intrinsic routines.

```C++

/**
 * Pseudo rotate a bitboard 45 degree clockwise.
 * Main Diagonal is mapped to 1st rank
 * @param x any bitboard
 * @return bitboard x rotated
 */
U64 pseudoRotate45clockwise (U64 x) {
   const U64 k1 = C64(0xAAAAAAAAAAAAAAAA);
   const U64 k2 = C64(0xCCCCCCCCCCCCCCCC);
   const U64 k4 = C64(0xF0F0F0F0F0F0F0F0);
   x ^= k1 & (x ^ rotateRight(x,  8));
   x ^= k2 & (x ^ rotateRight(x, 16));
   x ^= k4 & (x ^ rotateRight(x, 32));
   return x;
}

```

Another pseudo rotation scheme was introduced by [Robert Hyatt's](Robert_Hyatt "Robert Hyatt") [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") approach. While the 45 degree rotation looks more natural at the first glance, the calculations of this mapping is more complicated.

```C++

normal chess board bitmap          45 clockwise               45 clockwise crafty

A8 B8 C8 D8 E8 F8 G8 H8                                       C7 D8|A6 B7 C8|A7 B8|A8|
A7 B7 C7 D7 E7 F7 G7 H7                  A8                   F8|A4 B5 C6 D7 E8|A5 B6
A6 B6 C6 D6 E6 F6 G6 H6                A7  B8                 E6 F7 G8|A3 B4 C5 D6 E7
A5 B5 C5 D5 E5 F5 G5 H5              A6  B7  C8               E5 F6 G7 H8|A2 B3 C4 D5
A4 B4 C4 D4 E4 F4 G4 H4            A5  B6  C7  D8             E4 F5 G6 H7|A1 B2 C3 D4
A3 B3 C3 D3 E3 F3 G3 H3          A4  B5  C6  D7  E8           D2 E3 F4 G5 H6|B1 C2 D3
A2 B2 C2 D2 E2 F2 G2 H2        A3  B4  C5  D6  E7  F8        |G3 H4|D1 E2 F3 G4 H5|C1
A1 B1 C1 D1 E1 F1 G1 H1      A2  B3  C4  D5  E6  F7  G8       H1|G1 H2|F1 G2 H3|E1 F2
                           A1  B2  C3  D4  E5  F6  G7  H8
A8|B1 C2 D3 E4 F5 G6 H7      B1  C2  D3  E4  F5  G6  H7       A8|B1 C2 D3 E4 F5 G6 H7
A7 B8|C1 D2 E3 F4 G5 H6        C1  D2  E3  F4  G5  H6         A7 B8|C1 D2 E3 F4 G5 H6
A6 B7 C8|D1 E2 F3 G4 H5          D1  E2  F3  G4  H5           A6 B7 C8|D1 E2 F3 G4 H5
A5 B6 C7 D8|E1 F2 G3 H4            E1  F2  G3  H4             A5 B6 C7 D8|E1 F2 G3 H4
A4 B5 C6 D7 E8|F1 G2 H3              F1  G2  H3               A4 B5 C6 D7 E8|F1 G2 H3
A3 B4 C5 D6 E7 F8|G1 H2                G1  H2                 A3 B4 C5 D6 E7 F8|G1 H2
A2 B3 C4 D5 E6 F7 G8|H1                  H1                   A2 B3 C4 D5 E6 F7 G8|H1
A1 B2 C3 D4 E5 F6 G7 H8                                       A1 B2 C3 D4 E5 F6 G7 H8

45 clockwise                                                  45 clockwise

```

A parallel prefix solution to map the normal occupancy to the visual rotated approach is left to the ambitious reader.

### Anti-Clockwise

We enumerate the 15 [anti-diagonals](Anti-Diagonals "Anti-Diagonals") by 7 ^ (file + rank), a [nibble](Nibble "Nibble") wise [two's complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") F == -1.

```C++

0 F E D C B A 9     1 1 1 1 1 1 1 9
1 0 F E D C B A     2 2 2 2 2 2 A A
2 1 0 F E D C B     3 3 3 3 3 B B B
3 2 1 0 F E D C     4 4 4 4 C C C C
4 3 2 1 0 F E D     5 5 5 D D D D D
5 4 3 2 1 0 F E     6 6 E E E E E E
6 5 4 3 2 1 0 F     7 F F F F F F F
7 6 5 4 3 2 1 0     0 0 0 0 0 0 0 0

```

We need to rotate the A-H files vertically by 7 to 0 ranks - done parallel prefix wise.
One square is therefor mapped by:

```C++

sq' = (sq + 8*((sq&7)^7)) & 63;

```

The main anti-diagonal is rotated anti-clockwise to the first rank - thus 45 degrees. The shorter anti-diagonals are pairwise and properly file aligned packed into further ranks.

On using xor see [bits from two sources by a mask](General_Setwise_Operations#BitsFrom2SourcesByMask "General Setwise Operations"). See [rotate](General_Setwise_Operations#Rotate "General Setwise Operations") for the intrinsic routines.

```C++

/**
 * Pseudo rotate a bitboard 45 degree anti clockwise.
 * Main AntiDiagonal is mapped to 1st rank
 * @param x any bitboard
 * @return bitboard x rotated
 */
U64 pseudoRotate45antiClockwise (U64 x) {
   const U64 k1 = C64(0x5555555555555555);
   const U64 k2 = C64(0x3333333333333333);
   const U64 k4 = C64(0x0f0f0f0f0f0f0f0f);
   x ^= k1 & (x ^ rotateRight(x,  8));
   x ^= k2 & (x ^ rotateRight(x, 16));
   x ^= k4 & (x ^ rotateRight(x, 32));
   return x;
}

```

______________________________________________________________________

## Rank, File and Diagonal

Those subsets may be flipped or mirrored in a more efficient way by multiplication-techniques with disjoint intermediate sums and no internal overflows. Unlike the whole board techniques, multiplication doesn't swap bits, but maps file to a rank or vice versa in different steps, which can not be combined in one step. Main application is to map file- or diagonal occupancies to ranks, to dense the line-occupancy to consecutive bits, further elaborated in [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line") or [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards").

## Flip about the Anti-Diagonal

Flipping about the anti-diagonal multiplies with the main-diagonal. Note that the set bits in the main-diagonal have a distance of 9 (2^0, 2^9,2^18,...,2^54, 2^63). We can therefor safely multiply it with a rank-pattern with 8 consecutive neighboring bits without overflows.

### File to a Rank

Multiplying the masked A-file with the main-diagonal, maps the file-bits to the 8th rank, similar to a flip about the anti-diagonal A8-H1. Shifting down to the 1st rank, leaves the bits like a 90-degree anti clockwise rotation.

```C++

masked bits                             mapped to 8th rank
bits on A-file   *  main-diagonal    =  with garbage     -> 1st rank
A . . . . . . .     . . . . . . . 1     A B C D E F G H     . . . . . . . .
B . . . . . . .     . . . . . . 1 .     B C D E F G H .     . . . . . . . .
C . . . . . . .     . . . . . 1 . .     C D E F G H . .     . . . . . . . .
D . . . . . . .     . . . . 1 . . .     D E F G H . . .  >> . . . . . . . .
E . . . . . . .  *  . . . 1 . . . .  =  E F G H . . . .  56 . . . . . . . .
F . . . . . . .     . . 1 . . . . .     F G H . . . . .     . . . . . . . .
G . . . . . . .     . 1 . . . . . .     G H . . . . . .     . . . . . . . .
H . . . . . . .     1 . . . . . . .     H . . . . . . .     A B C D E F G H

```

### Rank to File

Multiplying the masked 1st rank with the main-diagonal, maps the rank-bits to the H-file, similar to a flip about the anti-diagonal A8-H1. Shifting the H-file to the A-file plus mask acts like a 90-degree clockwise rotation.

```C++

masked bits                             mapped to H-file
bits on 1st rank *  main-diagonal    =  with garbage     -> masked A-file
. . . . . . . .     . . . . . . . 1     C D E F G H . A     A . . . . . . .
. . . . . . . .     . . . . . . 1 .     D E F G H . A B     B . . . . . . .
. . . . . . . .     . . . . . 1 . .     E F G H . A B C  >> C . . . . . . .
. . . . . . . .     . . . . 1 . . .     F G H . A B C D  7  D . . . . . . .
. . . . . . . .  *  . . . 1 . . . .  =  G H . A B C D E  &  E . . . . . . .
. . . . . . . .     . . 1 . . . . .     H . A B C D E F  A  F . . . . . . .
. . . . . . . .     . 1 . . . . . .     . A B C D E F G     G . . . . . . .
A B C D E F G H     1 . . . . . . .     A B C D E F G H     H . . . . . . .

```

## Flip about the Diagonal

Flipping about the Diagonal is a bit more tricky. Since the Anti-Diagonal pattern as factor has the set bits with distance of 7 only (2^0,2^7, 2^14,...2^49, 2^56) with possible overflows, if multiplied with rank pattern of eight neighboring bits. Thus it can only be used to flip the H-file about the diagonal.

### File to a Rank

Multiplying the masked H-file with the 7-bit right shifted (board left shifted) anti-diagonal, maps the file-bits to the 8th rank, similar to a flip about the diagonal A1-H8. Shifting it down to the 1st rank, leaves the bits like flip about the diagonal. Shifting down to the 1st rank, leaves the bits like a 90-degree clockwise rotation.

```C++

masked bits         Shifted             mapped to 8th rank
bits on H-file   *  anti-diagonal    =  with garbage     -> 1st rank
. . . . . . . A     . . . . . . . .     H G F E D C B A     . . . . . . . .
. . . . . . . B     . 1 . . . . . .     . H G F E D C B     . . . . . . . .
. . . . . . . C     . . 1 . . . . .     . . H G F E D C     . . . . . . . .
. . . . . . . D     . . . 1 . . . .     . . . H G F E D  >> . . . . . . . .
. . . . . . . E  *  . . . . 1 . . .  =  . . . . H G F E  56 . . . . . . . .
. . . . . . . F     . . . . . 1 . .     . . . . . H G F     . . . . . . . .
. . . . . . . G     . . . . . . 1 .     . . . . . . H G     . . . . . . . .
/ . . . . . . H     1 . . . . . . 1     . . . . . . . H     H G F E D C B A

```

## Diagonals to Ranks

That is straight forward multiplication of a masked diagonal or anti-diagonal with the A-file.
To mask the garbage off, we further shift down by 7 ranks.

```C++

masked diagonal  *  A-file              mapped
                                        to 8th rank      ->  1st rank
. . . . . . . H     1 . . . . . . .     A B C D E F G H     . . . . . . . .
. . . . . . G .     1 . . . . . . .     A B C D E F G .     . . . . . . . .
. . . . . F . .     1 . . . . . . .     A B C D E F . .  >> . . . . . . . .
. . . . E . . .     1 . . . . . . .     A B C D E . . .  56 . . . . . . . .
. . . D . . . .  *  1 . . . . . . .  =  A B C D . . . .     . . . . . . . .
. . C . . . . .     1 . . . . . . .     A B C . . . . .     . . . . . . . .
. B . . . . . .     1 . . . . . . .     A B . . . . . .     . . . . . . . .
A . . . . . . .     1 . . . . . . .     A . . . . . . .     A B C D E F G H

```

## Mirror Horizontally

This is about bit-reversal of a byte.

```C++

rank1mirrored = (((rank1 * 0x80200802) & 0x0884422110) * 0x0101010101010101) >> 56;

```

This is how it works on a chessboard:

```C++

rank1            *  0x80200802          flipped
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     B C D E F G H .
. . . . . . . .  *  . . . . . . . 1  =  D E F G H . . A
. . . . . . . .     . . . . . 1 . .     F G H . . A B C
. . . . . . . .     . . . 1 . . . .     H . . A B C D E
A B C D E F G H     . 1 . . . . . .     . A B C D E F G

flipped          &  0x0884422110        reversedOnFiles
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
B C D E F G H .     . . . 1 . . . .     . . . E . . . .
D E F G H . . A  &  . . 1 . . . . 1  =  . . F . . . . A
F G H . . A B C     . 1 . . . . 1 .     . G . . . . B .
H . . A B C D E     1 . . . . 1 . .     H . . . . C . .
. A B C D E F G     . . . . 1 . . .     . . . . D . . .

reversedOnFiles  *  A-file              reversedOn8         reversed
. . . . . . . .     1 . . . . . . .     H G F E D C B A     . . . . . . . .
. . . . . . . .     1 . . . . . . .     H G F E D C B A     . . . . . . . .
. . . . . . . .     1 . . . . . . .     H G F E D C B A     . . . . . . . .
. . . E . . . .     1 . . . . . . .     H G F E D C B A  >> . . . . . . . .
. . F . . . . A  *  1 . . . . . . .  =  H G F . D C B A  56 . . . . . . . .
. G . . . . B .     1 . . . . . . .     H G . . D C B .     . . . . . . . .
H . . . . C . .     1 . . . . . . .     H . . . D C . .     . . . . . . . .
. . . . D . . .     1 . . . . . . .     . . . . D . . .     H G F E D C B A

```

A 32 bit solution:

```C++

rank1mirrored = ( (rank1 * 0x0802 & 0x22110)
                 |(rank1 * 0x8020 & 0x88440) )
                * 0x10101000 >> 24;

```

Or a simple lookup:

```C++

rank1mirrored = reverseByteLookup256[rank1];

```

## See also

- [BMI2 PEXT instruction](BMI2#PEXT "BMI2")
- [Color Flipping](Color_Flipping "Color Flipping")
- [Diagonal Mirroring](Diagonal_Mirroring "Diagonal Mirroring")
- [Horizontal Mirroring](Horizontal_Mirroring "Horizontal Mirroring")
- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
- [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
- [Vertical Flipping](Vertical_Flipping "Vertical Flipping")
- [XOP VPPERM instruction](XOP#VPPERM "XOP")

## Publications

- [Christopher Strachey](Christopher_Strachey "Christopher Strachey") (**1961**). *Bitwise operations*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 4, No. 3 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2002, 2012**). *[Hacker's Delight](Henry_S._Warren,_Jr.#HackersDeligh "Henry S. Warren, Jr.")*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley)
- [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz)

## Forum Posts

- [Reflection of a bitboard](http://www.talkchess.com/forum/viewtopic.php?t=59937) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 22, 2016

## External Links

- [Bit Gather Via Multiplication](http://drpetric.blogspot.com/2013/09/bit-gathering-via-multiplication.html) by [Vlad Petric](index.php?title=Vlad_Petric&action=edit&redlink=1 "Vlad Petric (page does not exist)"), [Dr. Petric's Technical Blog](http://drpetric.blogspot.com/), September 17, 2013 <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## Flipping

- [Flip from Wikipedia](https://en.wikipedia.org/wiki/Flip)
- [Flip (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Flip_%28mathematics%29)
- [Flip](http://www.icoachmath.com/SiteMap/Flip.html) from [iCoachMath](http://www.icoachmath.com/)
- [Flip, Slide, Turn - Alphabet Geometry](http://www.misterteacher.com/abc.html) from [misterteacher.com](http://www.misterteacher.com/)

## Mirroring

- [Mirror from Wikipedia](https://en.wikipedia.org/wiki/Mirror)
- [Mirroring (psychology) from Wikipedia](https://en.wikipedia.org/wiki/Mirroring_%28psychology%29)
- [Reflection (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29)
- [Reflection (physics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28physics%29)
- [Reflection symmetry from Wikipedia](https://en.wikipedia.org/wiki/Reflection_symmetry)
- [Venus effect from Wikipedia](https://en.wikipedia.org/wiki/Venus_effect)
- [Why do Mirrors Reverse Left and Right?](http://math.ucr.edu/home/baez/physics/General/mirrors.html)

## Rotation

- [Rotation from Wikipedia](https://en.wikipedia.org/wiki/Rotation)
- [Rotation (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Rotation_%28mathematics%29)
- [Rotation matrix from Wikipedia](https://en.wikipedia.org/wiki/Rotation_matrix)
- [Rotation formalisms in three dimensions - Wikipedia](https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions)
- [Rotation](http://www.icoachmath.com/SiteMap/Rotation.html) from [iCoachMath](http://www.icoachmath.com/)
- [Oliver Vornberger's](Oliver_Vornberger "Oliver Vornberger") German [lecture](http://www-lehre.inf.uos.de/%7Ecg/2006/)on Graphic Rotation:
  - [2D Rotation](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/node41.html)
  - [3D Rotation](http://www-lehre.inf.uos.de/%7Ecg/2006/skript/node100.html)

## Reflection

- [Reflection (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29)
- [Reflection (physics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28physics%29)
- [Reflection symmetry from Wikipedia](https://en.wikipedia.org/wiki/Reflection_symmetry)

## Smoke 'n' Mirrors

- [Lee Ritenour](Category:Lee_Ritenour "Category:Lee Ritenour"), [Mike Stern](Category:Mike_Stern "Category:Mike Stern"), [Simon Phillips](Category:Simon_Phillips "Category:Simon Phillips"), [John Beasley](https://en.wikipedia.org/wiki/John_Beasley_%28musician%29), [Melvin Davis](http://www.allmusic.com/artist/melvin-davis-mn0000350965) - Smoke 'n' Mirrors <a id="cite-note-7" href="#cite-ref-7">[7]</a>, [Blue Note Tokyo](https://en.wikipedia.org/wiki/Blue_Note_Tokyo), 2011, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Figurative Paintings](http://www.barbaramittman.com/Site/Figurative_Paintings.html) by [Barbara Mittman](Category:Barbara_Mittman "Category:Barbara Mittman")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [\_byteswap_uint64](http://msdn.microsoft.com/en-us/library/a3140177.aspx) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [\_rotl, \_rotl64, \_rotr_rotr64](http://msdn.microsoft.com/en-us/library/5cc576c4.aspx) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [reverse.c](http://www.hackersdelight.org/hdcodetxt/reverse.c.txt) from [C code for most of the programs that appear in HD](http://www.hackersdelight.org/hdcode.htm) by [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Demystifying the Magic Multiplier?](https://chessprogramming.wikispaces.com/share/view/64439740)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Smoke and mirrors (disambiguation)](https://en.wikipedia.org/wiki/Smoke_and_mirrors_%28disambiguation%29)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Shorter front view version with interviews](https://www.youtube.com/watch?v=vsmlkrBiok0)

**[Up one Level](Bitboards "Bitboards")**

