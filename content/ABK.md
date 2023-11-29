---
title: ABK
---
**[Home](Home "Home") * [Knowledge](Knowledge "Knowledge") * [Opening Book](Opening_Book "Opening Book") * ABK**

**ABK**, (Arena's book format)

the opening book format of [Arena](Arena "Arena"). It persists a book tree as [array](Array "Array") of entries, each entry referring one book move with priority and statistics, an entry index of the next move inside a book line (> 0 if any), and an entry index of a possible sibling move (>= 0 if any). The sizeof of an entry is 28, the [initial position](Initial_Position "Initial Position") indexed by 900 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Entry Structure

The array of entries/structures is written to / read from a [binary file](https://en.wikipedia.org/wiki/Binary_file) under [Windows](Windows "Windows") ([x86](X86 "X86")), struct and integers implicitely stored [little-endian](Little-endian "Little-endian") wise:

```C++
struct SBookMoveEntry {
  char from;      /* a1 0, b1 1, ..., h1 7, ... h8 63 */
  char to;        /* a1 0, b1 1, ..., h1 7, ... h8 63 */
  char promotion; /* 0 none, +-1 rook, +-2 knight, +-3 bishop, +-4 queen */
  char priority;
  int ngames;
  int nwon;
  int nlost;
  int plycount;
  int nextMove;
  int nextSibling;
} * pOpeningBook;

```

## Sample Tree

```

  root index
      ▼
┌───────────┐                                  ┌───────────┐  
│nextSibling│ ─────────────── ► ────────────── │nextSibling│ ─────────────── ► ... 
├───────────┤                                  ├───────────┤  
│   e2-e4   │                                  │   d2-d4   │  
├───────────┤                                  ├───────────┤  
│ nextMove  │                                  │ nextMove  │  
└───────────┘                                  └───────────┘  
      ▼                                              ▼
┌───────────┐ ┌───────────┐ ┌───────────┐      ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐     ┌───────────┐ 
│nextSibling│►│nextSibling│►│nextSibling│►...  │nextSibling│►│nextSibling│►│nextSibling│►│nextSibling│►...►│nextSibling│ 
├───────────┤ ├───────────┤ ├───────────┤      ├───────────┤ ├───────────┤ ├───────────┤ ├───────────┤     ├───────────┤ 
│   e7-e5   │ │   c7-c5   │ │   e6-e6   │      │   d7-d5   │ │   g8-f6   │ │   c7-c6   │ │   e7-e6   │     │   f7-f5   │ 
├───────────┤ ├───────────┤ ├───────────┤      ├───────────┤ ├───────────┤ ├───────────┤ ├───────────┤     ├───────────┤ 
│ nextMove  │ │ nextMove  │ │ nextMove  │      │ nextMove  │ │ nextMove  │ │ nextMove  │ │ nextMove  │     │ nextMove  │ 
└───────────┘ └───────────┘ └───────────┘      └───────────┘ └───────────┘ └───────────┘ └───────────┘     └───────────┘ 
      ▼             ▼             ▼                  ▼             ▼             ▼              ▼                ▼
┌───────────┐      ...      ┌───────────┐      ┌───────────┐      ...           ...      ┌───────────┐          ...
│nextSibling│►...           │nextSibling│►...  │nextSibling│►...                         │nextSibling│►...
├───────────┤               ├───────────┤      ├───────────┤                             ├───────────┤ 
│   g1-f3   │               │   d2-d4   │      │   c2-c4   │                             │   e2-e4   │ 
├───────────┤               ├───────────┤      ├───────────┤                             ├───────────┤ 
│ nextMove  │               │ nextMove  │      │ nextMove  │                             │ nextMove  │ 
└───────────┘               └───────────┘      └───────────┘                             └───────────┘ 
     ▼                            ▼                  ▼                                         ▼
	...                          ...                ...                                       ...

```

## See also

- [CTG](CTG "CTG") - [ChessBase](ChessBase "ChessBase") book format
- [BIN](index.php?title=Polyglot&action=edit&redlink=1 "Polyglot (page does not exist)") - [Polyglot](index.php?title=Polyglot&action=edit&redlink=1 "Polyglot (page does not exist)") book format

## Forum Posts

## 2007 ...

- [Which is the best general purpose Arena (abk format) Book](http://www.talkchess.com/forum/viewtopic.php?t=14254) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](CCC "CCC"), June 04, 2007
- [Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661) by James Constance, [CCC](CCC "CCC"), April 14, 2008

## [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=5) by [Jury Osipov](Jury_Osipov "Jury Osipov"), [CCC](CCC "CCC"), April 15, 2008 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=6) by [Richard Pijl](Richard_Pijl "Richard Pijl"), [CCC](CCC "CCC"), April 15, 2008 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=9) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 15, 2008 [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=13) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC](CCC "CCC"), April 17, 2008 2010 ...

- [Convert .obk books to .abk books?](http://www.talkchess.com/forum/viewtopic.php?t=40406) by [David Dahlem](index.php?title=David_Dahlem&action=edit&redlink=1 "David Dahlem (page does not exist)"), [CCC](CCC "CCC"), September 15, 2011
- [Scid / Scid vs. PC - ChessBase (.ctg) and Arena (.abk)](http://www.talkchess.com/forum/viewtopic.php?t=61165) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 19, 2016 » [CTG](CTG "CTG"), [SCID](SCID "SCID"), [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
- [How to use Arena book?](http://www.talkchess.com/forum/viewtopic.php?t=63007) by P. Kumar, [CCC](CCC "CCC"), February 01, 2017

## 2020 ...

- [abk to pgn tool](https://groups.google.com/d/msg/fishcooking/2PQ3_bl_tvg/gknge6qzBAAJ) by [Fauzi](Fauzi_Akram_Dabat "Fauzi Akram Dabat"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2020 » [PGN](Portable_Game_Notation "Portable Game Notation")

## External Links

- [Arena Chess GUI - Opening Books](http://www.playwitharena.com/?User_Files%2C_Engines:Opening_Books_%2821%29%26nbsp%3B)
- [Commercial Opening Book Fauzi 4.5.abk](https://gumroad.com/l/UAgr) by [Fauzi Akram Dabat](Fauzi_Akram_Dabat "Fauzi Akram Dabat")
- [Free Opening Book Downloads](http://www.hiarcs.com/chess-opening-book-free.htm) from [HIARCS Chess Software](HIARCS "HIARCS")
- [Arena opening books](https://sites.google.com/site/numptychess/arena-opening-books) from [Numpty chess](Numpty_chess "Numpty chess") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Re: Opening books format](http://www.talkchess.com/forum/viewtopic.php?t=20661&start=5) by [Jury Osipov](Jury_Osipov "Jury Osipov"), [CCC](CCC "CCC"), April 15, 2008
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Scid / Scid vs. PC - ChessBase (.ctg) and Arena (.abk)](http://www.talkchess.com/forum/viewtopic.php?t=61165) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 19, 2016

**[Up one Level](Opening_Book "Opening Book")**

