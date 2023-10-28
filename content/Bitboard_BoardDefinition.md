---
title: Bitboard BoardDefinition
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * Bitboard Board-Definition**

To represent the board we typically need one bitboard for each [piece-type](Pieces#PieceTypeCoding "Pieces") and [color](Color "Color") - likely encapsulated inside a class or structure, or as an [array](Array "Array") of bitboards as part of a [position](Chess_Position "Chess Position") object. A one-bit inside a bitboard implies the existence of a piece of this piece-type on a certain [square](Squares "Squares") - one to one associated by the bit-position <a id="cite-note-1" href="#cite-ref-1">[1]</a>:

## Contents

- [1 Classical Board](#classical-board)
  - [1.1 Structure](#structure)
  - [1.2 Array](#array)
- [2 Denser Board](#denser-board)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
- [6 References](#references)

## Classical Board

Those bitboards may part of a central position object which is [incrementally updated](Incremental_Updates "Incremental Updates") while [making](Make_Move "Make Move") or [unmaking](Unmake_Move "Unmake Move") [moves](Moves "Moves").

## [](http://www.onjava.com/pub/a/onjava/2005/02/02/bitsets.html?page=2) Structure

*To be aware of their scalar 64-bit origin, we use so far a type defined unsigned integer U64 in our [C](C "C")/[C++](Cpp "Cpp") source snippets, the scalar 64-bit long in [Java](Java "Java"). Feel free to define a distinct type or wrap U64 into classes for better abstraction and type-safety during compile time.*

```

class CBoard
{
   U64 whitePawns;
   U64 whiteKnights;
   U64 whiteBishops;
   U64 whiteRooks;
   U64 whiteQueens;
   U64 whiteKing;

   U64 blackPawns;
   U64 blackKnights;
   U64 blackBishops;
   U64 blackRooks;
   U64 blackQueens;
   U64 blackKing;
   ...
};

```

## Array

For better generalization and to [avoid branches](Avoiding_Branches "Avoiding Branches"), one may encapsulate [arrays](Array "Array") of bitboards. For instance, inside the [Beowulf](Beowulf "Beowulf") sources (sample from moves.c) one finds a lot of branches on [side to move](Side_to_move "Side to move") to either fetch white or black piece bitboards, as already criticized by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") in 2001 <a id="cite-note-2" href="#cite-ref-2">[2]</a> ...

```

  switch (side) {
   case WHITE: tsq = B->whiteRooks; break;
   case BLACK: tsq = B->blackRooks; break;
  }

```

.. where an indexed access with appropriate defined {0,1} color range for the side to move would avoid those branches, per piece-kind, ...

```

  tsq = B->rooks[side];

```

... or over all piece-kinds, ...

```

  tsq = B->pieceBB[nWhiteRook + side];

```

... for instance, on [x86](X86 "X86") or [x86-64](X86-64 "X86-64"), utilizing its [addressing modes](https://en.wikipedia.org/wiki/X86#Addressing_modes) with base- and scalable [index register](https://en.wikipedia.org/wiki/Index_register), plus displacement:

```

   ; rsi pointer to structure, rcx side (0 == White, 1 == Black)
   mov  rax, qword ptr [rsi + rookOffset + 8*rcx] 

```

Likely one also keeps some often used redundant [union](General_Setwise_Operations#Union "General Setwise Operations") sets like white and black pieces, [occupancy](Occupancy "Occupancy") or their complement, the empty squares.

```

class CBoard
{
   U64 pieceBB[14];
   U64 emptyBB;
   U64 occupiedBB;
   ...
public:
   enum enumPiece
   {
      nWhite,     // any white piece
      nBlack,     // any black piece
      nWhitePawn, // white Pawn
      nBlackPawn, // white Pawn
      ...
   };

   U64 getPieceSet(PieceType pt) const {return pieceBB[pt];}
   U64 getWhitePawns() const {return pieceBB[nWhitePawn];}
   ...
   U64 getPawns(ColorType ct) const {return pieceBB[nWhitePawn + ct];}
   ...
};

```

On initialization and update of the bitboards, see [general setwise operations](General_Setwise_Operations#UpdateByMove "General Setwise Operations").

## Denser Board

A common alternative to reduce the size of the board structure is to keep two color bitboards and six color independent piece bitboards, which are the [union](General_Setwise_Operations#Union "General Setwise Operations") of black and white respective pieces, i.e. all queens. This space saving requires a cheap [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of a color and a piece bitboard to get the required pieces of that color only.

```

class CBoard
{
   U64 pieceBB[8];
public:
   enum enumPiece
   {
      nWhite,     // any white piece
      nBlack,     // any black piece
      nPawn,
      nKnight,
      nBishop,
      nRook,
      nQueen,
      nKing
   };

   U64 getPieceSet(PieceType pt) const {return pieceBB[pieceCode(pt)] & pieceBB[colorCode(pt)];}
   U64 getWhitePawns() const {return pieceBB[nPawn] & pieceBB[nWhite];}
   ...
   U64 getPawns(ColorType ct) const {return pieceBB[nPawn] & pieceBB[ct];}
   ...
};

```

## See also

- [Color Flipping](Color_Flipping "Color Flipping")
- [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")

## Forum Posts

- [Bit Board Bonkers??](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/834fa3c273fafffe/cab7c12ea99e9a35) by Dave, [rec.games.chess.computer](Computer_Chess_Forums "Computer Chess Forums"), July 28, 1997
- [Bitboard board representation](https://www.stmintz.com/ccc/index.php?id=405590) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), January 13, 2005
- [BitBoard representations of the board](http://www.talkchess.com/forum/viewtopic.php?t=17138) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 14, 2007
- [Decision concerning board representation](http://www.talkchess.com/forum/viewtopic.php?t=47917) by [Piotr Lopusiewicz](index.php?title=Piotr_Lopusiewicz&action=edit&redlink=1 "Piotr Lopusiewicz (page does not exist)"), [CCC](CCC "CCC"), May 05, 2013
- [Bitboard board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76083) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), December 17, 2020

## External Links

- [Charlie Mariano](Category:Charlie_Mariano "Category:Charlie Mariano") - [Helen 12 Trees](https://www.discogs.com/de/Charlie-Mariano-Helen-12-Trees/release/2532764), 1977, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Charlie Mariano](Category:Charlie_Mariano "Category:Charlie Mariano"), [Jack Bruce](Category:Jack_Bruce "Category:Jack Bruce"), [Jan Hammer](Category:Jan_Hammer "Category:Jan Hammer"), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Nippy Noya](Category:Nippy_Noya "Category:Nippy Noya"), [Zbigniew Seifert](Category:Zbigniew_Seifert "Category:Zbigniew Seifert")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Bitwise Optimization in Java: Bitfields, Bitboards, and Beyond](https://web.archive.org/web/20060316100407/http://www.onjava.com/pub/a/onjava/2005/02/02/bitsets.html?page=2) by [Glen Pepicelli](Glen_Pepicelli "Glen Pepicelli"), ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), 2005), [O'Reilly's](https://en.wikipedia.org/wiki/O%27Reilly_Media) [OnJava.com](https://web.archive.org/web/20050203015229/http://onjava.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [On Beowulf - long post](https://www.stmintz.com/ccc/index.php?id=173418) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 04, 2001

**[Up one Level](Bitboards "Bitboards")**

