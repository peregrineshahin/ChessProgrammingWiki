---
title: Fill by Subtraction
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") * Fill by Subtraction**

Performing the [o^(o-2r) - trick](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")  in a [SWAR-wise](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") fashion with bytes (ranks), saves some instructions compared to [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm").

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
|

Unfortunately it only works in positive horizontal direction, so the possible savings are marginal, despite even less generalization of handling one out of eight cases with a different code pattern.

## Source Code

```C++

U64 eastAttacks(U64 rooks, U64 empty) {
   const U64 H     =  0x8080808080808080;
   U64 occInclRook =  rooks | ~empty | H;
   U64 occExclRook = (rooks   &=      ~H)  ^ occInclRook;
   U64 rookAttacks = (occExclRook - rooks) ^ occInclRook;
   return rookAttacks;
}

```

Even more with vectors of two bitboards and [SSE2-instructions](SSE2#EastAttacks "SSE2").

## Comparison with Kogge-Stone

For comparison the [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") attack-getter. It gives an idea how to implement a [Kogge-Stone Adder](Parallel_Prefix_Algorithms#KoggeStoneAdder "Parallel Prefix Algorithms") with bitwise operations only.

```C++

U64 eastAttacks(U64 rooks, U64 empty) {
   empty &= notAFile;
   rooks |= empty & (rooks << 1);
   empty &=         (empty << 1);
   rooks |= empty & (rooks << 2);
   empty &=         (empty << 2);
   rooks |= empty & (rooks << 4);
   return notAFile& (rooks << 1);
}

```

## See also

- [Add/Sub versus Attacks](Parallel_Prefix_Algorithms#KoggeStoneAdder "Parallel Prefix Algorithms") from [Parallel Prefix Algorithms](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")
- [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
- [Fill by Subtraction](SSE2#EastAttacks "SSE2") with [SSE2-instructions](SSE2 "SSE2")
- [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
- [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [Subtracting a Rook from a Blocking Piece](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**

