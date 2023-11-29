---
title: First Rank AttacksTheOuterSquares
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") * First Rank Attacks**

The technique of [occupancy](Occupancy "Occupancy") lookups is base for [Rotated bitboards](Rotated_Bitboards "Rotated Bitboards"), [Kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") and [Magic bitboards](Magic_Bitboards "Magic Bitboards"). The first [rank](Ranks "Ranks") with an occupancy in the [byte](Byte "Byte") range serves as teaser to introduce occupancy lookups.

## Introduction to Occupancy Lookup

## One Byte Only

Assume we (temporary) reduce the chess-board to one [rank](Ranks "Ranks"). Occupancy bitboard is one [byte](Byte "Byte") with up to 256 states. A [rook](Rook "Rook") attack-set from one of the eight [squares](Squares "Squares") ([file](Files "Files")) on this single rank is also only one byte. Thus we can construct an [array](Array "Array") of bytes[256][8], indexed by all 256 occupancies and 8 files, to lookup the pre-calculated rank-attack bytes.

<img src="" alt="missing fen" style="
    width: 300px;
">

Occupancy of the first rank = 01001010B, Rank-attacks ::= f (e-file, Occupancy) = 01110110B

```C++
BYTE arrFirstRankAttacks256x8[256][8]; // 2048 Bytes = 2KByte

firstRankAttack = arrFirstRankAttacks256x8[rankOccupancy][squareOnRank];

```

## Overdetermined?

In fact both indices seem somehow overdetermined, since the rook is already member of occupancy. But rather than to make the redundant rook-bit disappear to use only the remaining seven occupancy bits, with half table size - which is not that cheap and simple either - we better decide to uncouple this items to eventually pass (virtual) rook squares, not actually member of occupancy. We better rely on another property to reduce the table fourfold.

## The Outer Squares

If we think about the occupancy lookup, we may recognize that the outer squares don't matter. There are no more squares behind. The outer squares are either attacked or not - independent from their occupancy state. We can use the **six inner bits** only as lookup-index with two additional cheap instructions.

```C++
BYTE arrFirstRankAttacks64x8[64][8]; // 512 Bytes = 1/2KByte

firstRankAttack = arrFirstRankAttacks64x8[(rankOccupancy >> 1) & 63][squareOnRank];

```

## Attacks on all Ranks

Since it is simple to shift ranks up and down, the general rank attack getter is already handy.

```C++
BYTE arrFirstRankAttacks64x8[64*8]; // 512 Bytes = 1/2KByte

U64 rankAttacks(U64 occ, enumSquare sq) {
   unsigned int file = sq &  7;
   unsigned int rkx8 = sq & 56; // rank * 8
   unsigned int rankOccX2 = (occ >> rkx8) & 2*63; // 2 times the inner six bit rank occupancy used as index
   U64 attacks = arrFirstRankAttacks64x8[4*rankOccX2  + file]; // 8 * rank occupancy + file
   return attacks << rkx8;
}

```

The [array](Array "Array") is defined one-dimensional, and has to indexed by 8\*occ + file. The reason was playing the optimization game and to safe the right shift one, but to scale by 4 instead of 8, which is done by the address calculation unit anyway. This routine may complete the [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence").

## See also

- [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
- [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")
- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

## Forum Posts

- [Understanding first rank attack state generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71312) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), July 18, 2019 » [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**

