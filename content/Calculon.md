---
title: Calculon
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Calculon**

[](https://fi.wikipedia.org/wiki/Tiedosto:Calculon.jpg) Calculon <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Calculon**,

a [Java](Java "Java") chess engine by [Barry Smith](index.php?title=Barry_Smith&action=edit&redlink=1 "Barry Smith (page does not exist)") named after the [Futurama](https://en.wikipedia.org/wiki/Futurama) [character](https://en.wikipedia.org/wiki/List_of_recurring_Futurama_characters#Antonio_Calculon).
It is [open source](Category:Open_Source "Category:Open Source"), licensed under the [Apache License](https://en.wikipedia.org/wiki/Apache_License), Version 2.0 and hosted at [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Calculon is [UCI](UCI "UCI") compatible, uses [bitboards](Bitboards "Bitboards") as basic data structure, and applies [Negamax](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta"). The engine regularly plays on [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") under the name CalculonX and has Blitz/Standard ratings there around the 1750 mark.

## Contents

- [1 getPiece](#getpiece)
- [2 Forum Posts](#forum-posts)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## getPiece

Calculon's *getPiece* routine to get a the [piece code](Pieces#PieceTypeCoding "Pieces") of a square (the least significant one-bit of the passed bitboard pos, typically single populated)
from the [six piece bitboards](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition") of its [board representation](Board_Representation "Board Representation") emphasizes a central [bitboard weakness](Bitboards#getPiece "Bitboards"),
and the cause to keep a redundant [mailbox](Mailbox "Mailbox") board representation with some additional [update](Incremental_Updates "Incremental Updates") costs during [make](Make_Move "Make Move")/[unmake](Unmake_Move "Unmake Move").
Taking the [union](General_Setwise_Operations#Union "General Setwise Operations") (val) of six piece-specific [rotates](General_Setwise_Operations#Rotate "General Setwise Operations") (left by 1..6) of six piece disjoint [intersections](General_Setwise_Operations#Intersection "General Setwise Operations")
for the absolute difference of the [trailing zero counts](BitScan#TrailingZeroCount "BitScan") of that union and the passed square bitboard (pos) elegantly [avoids some branches](Avoiding_Branches "Avoiding Branches"),
but is a bit too much calculation for that purpose <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```C++

public class BitBoard { // Position object

  public byte getPiece(long pos) {
    long val = Long.rotateLeft(bitmaps[MAP_PAWNS]   & pos, MAP_PAWNS)   
             | Long.rotateLeft(bitmaps[MAP_KNIGHTS] & pos, MAP_KNIGHTS) 
             | Long.rotateLeft(bitmaps[MAP_BISHOPS] & pos, MAP_BISHOPS) 
             | Long.rotateLeft(bitmaps[MAP_ROOKS]   & pos, MAP_ROOKS)   
             | Long.rotateLeft(bitmaps[MAP_QUEENS]  & pos, MAP_QUEENS)  
             | Long.rotateLeft(bitmaps[MAP_KINGS]   & pos, MAP_KINGS);  
    if(val == 0) {
      return Piece.EMPTY;
    }
    return (byte) ((Long.numberOfTrailingZeros(val) - Long.numberOfTrailingZeros(pos)) & 0x07);
  }
}

```

## Forum Posts

- [Calculon - UCI Java Chess Engine by Barry Smith](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=51265) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 13, 2014
- [Calculon at work this morning !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=51288) by Sylwy, [CCC](CCC "CCC"), February 15, 2014

## External Links

## Chess Engine

- [CalculonX · GitHub](https://github.com/BarrySW19/CalculonX)

## Misc

- [Calculon - Futurama Wiki, the Futurama database](https://futurama.fandom.com/wiki/Calculon)
- [Calculon 2.0 - Futurama Wiki, the Futurama database](https://futurama.fandom.com/wiki/Calculon_2.0)
- [Calculon - The Infosphere, the Futurama Wiki](http://theinfosphere.org/Calculon)
- [Calculon (All My Circuits) - The Infosphere, the Futurama Wiki](http://theinfosphere.org/Calculon_%28All_My_Circuits%29)
- [Calculon (Character) - IMDb - Movies, TV and Celebrities](http://www.imdb.com/character/ch0047016/)
- [Calculon 2.0 from Wikipedia](https://en.wikipedia.org/wiki/Calculon_2.0)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Calculon – Wikipedia.fi](https://fi.wikipedia.org/wiki/Calculon), created by [Matt Groening](https://en.wikipedia.org/wiki/Matt_Groening)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [CalculonX · GitHub](https://github.com/BarrySW19/CalculonX)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [CalculonX/BitBoard.java at master · BarrySW19/CalculonX · GitHub](https://github.com/BarrySW19/CalculonX/blob/master/src/main/java/barrysw19/calculon/engine/BitBoard.java#L418)

**[Up one Level](Engines "Engines")**

