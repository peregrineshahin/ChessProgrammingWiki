---
title: Diagonal Mirroring
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Diagonal Mirroring**

\[.jpg) [Hilma af Klint](Category:Hilma_af_Klint "Category:Hilma af Klint") - Group IX SUW, The Swan No. 7 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Diagonal mirroring** mirrors all [pieces](Pieces "Pieces") along the [main diagonal](Diagonals "Diagonals") or [main anti-diagonal](Anti-Diagonals "Anti-Diagonals"). It is applicable in pawn-less [endgames](Endgame "Endgame") with [castling](Castling "Castling") no longer possible. Along with [horizontal](Horizontal_Mirroring "Horizontal Mirroring") and/or [vertical flipping](Vertical_Flipping "Vertical Flipping"), diagonal mirroring is used in pawn-less [endgame tablebases](Endgame_Tablebases "Endgame Tablebases") to restrict a white king to the 10 squares of the a1-d4-d1 triangle of the board.

## Contents

- [1 Mirroring an 8x8 Board](#mirroring-an-8x8-board)
- [2 Sample Position](#sample-position)
- [3 See also](#see-also)
- [4 External Links](#external-links)

## Mirroring an 8x8 Board

An [8x8 Board](8x8_Board "8x8 Board") with a [rank-file mapping](Squares "Squares") needs to swap [rank](Ranks "Ranks") and [file](Files "Files"). A pure 8x8 Board may be mirrored along the main diagonal that way in [C](C "C"):

```C++

int board[64], f, r, sm, sq, s;

for (f = 1; f < 8; ++f)
for (r = 0; r < f; ++r)
{
  sq = 8*r + f;
  sm = 8*f + r;
  s = board[sq];
  board[sq] = board[sm];
  board[sm] = s;
}

```

## Sample Position

|  Original
|  Diagonal Mirror
|  Anti-Diagonal Mirror
|
| --- | --- | --- |
|

|  |
| --- |
|                                                                                             ♚               ♘♔  ♗                                            |

|

|  |
| --- |
|                                                                                                                          ♗                       ♔       ♘ ♚ |

|

|  |
| --- |
|                                                                                             ♚ ♘       ♔                       ♗                              |

|
|  k7/8/NK2B3/8/8/8/8/8 w - -
|  8/8/8/5B2/8/8/5K2/5N1k w - -
|  k1N5/2K5/8/8/2B5/8/8/8 w - -
|

## See also

- [Color Flipping](Color_Flipping "Color Flipping")
- [Flipping, Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") of [Bitboards](Bitboards "Bitboards")
- [Horizontal Mirroring](Horizontal_Mirroring "Horizontal Mirroring")
- [Vertical Flipping](Vertical_Flipping "Vertical Flipping")

## External Links

- [Mirror from Wikipedia](https://en.wikipedia.org/wiki/Mirror)
- [Mirroring (psychology) from Wikipedia](https://en.wikipedia.org/wiki/Mirroring_%28psychology%29)
- [Reflection (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28mathematics%29)
- [Reflection (physics) from Wikipedia](https://en.wikipedia.org/wiki/Reflection_%28physics%29)
- [Reflection symmetry from Wikipedia](https://en.wikipedia.org/wiki/Reflection_symmetry)

\*\*[Up one Level](Chess_Position "Chess Position")\*\*1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Hilma af Klint](Category:Hilma_af_Klint "Category:Hilma af Klint") - [Group IX SUW, The Swan No. 7](<https://commons.wikimedia.org/wiki/File:Hilma_af_Klint_-_Group_IX_SUW,_The_Swan_No._7_(13945).jpg>), 1915, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)

