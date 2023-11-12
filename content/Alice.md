---
title: Alice
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Alice**

\[ Alice in Wonderland <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Alice**,

an experimental [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") by [Sven Reichard](Sven_Reichard "Sven Reichard"), written in [C++](Cpp "Cpp") and compliant with the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Alice is an [object oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) program developed under [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) and [Linux](Linux "Linux"). The board is a [vector](Array "Array") of 64 [pointers](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29) to [pieces](Pieces "Pieces"), while piece is an [abstract class](Cpp#AbstractClass "Cpp"), with intermediate subclasses for common piece properties such as [sliding](Sliding_Pieces "Sliding Pieces") versus none sliding pieces, and finally instantiable subclasses for the concrete pieces, like [pawn](Pawn "Pawn"), [rook](Rook "Rook"), etc., and "null pieces" for the empty squares <a id="cite-note-2" href="#cite-ref-2">[2]</a>. [Jim Ablett](Jim_Ablett "Jim Ablett") provides compiles for 32/64-bit [Windows](Windows "Windows") and [Linux](Linux "Linux") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Bitboards](#bitboards)
- [2 Forum Posts](#forum-posts)
- [3 External Links](#external-links)
  - [3.1 Chess Engine](#chess-engine)
  - [3.2 Misc](#misc)
- [4 References](#references)

## Bitboards

Alice is an object oriented [Bitboard](Bitboards "Bitboards") engine, applying [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Size of of the encapsulated Bitboard class is 8 by unsigned long long number <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

```C++

namespace Alice
{
  class BitboardIterator;
  class Bitboard
  {
  public:
    typedef BitboardIterator Iterator;
    Bitboard( unsigned long long n = 0ull);
    ~Bitboard();
    //operator unsigned long long() const;
    Bitboard& operator|=( const Bitboard& b );
    Bitboard& operator&=( const Bitboard& b );
    Bitboard operator~( ) const;
    ...
  private:
    unsigned long long number;
    static std::vector<unsigned long long> setMask;
    static std::vector<unsigned long long> clearMask;
    ...
    static Bitboard fileAttacks[256][64];
    static Bitboard rankAttacks[256][64] ;
    static Bitboard upDiagonalAttacks[256][64];
    static Bitboard downDiagonalAttacks[256][64] ;
    ...
  };
};

```

## Forum Posts

- [Gestatten: Alice](https://www.stmintz.com/ccc/index.php?id=237077) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), June 23, 2002
- [First draw against GnuChess](https://www.stmintz.com/ccc/index.php?id=330725) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), November 26, 2003
- [Alice new Winboard engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2001) by Pablo, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2005
- [Alice: A reintroduction](http://www.talkchess.com/forum/viewtopic.php?t=39730) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), July 15, 2011
- [Sorry guys, I have to ask for another engine: Alice](http://www.talkchess.com/forum/viewtopic.php?t=46252) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [CCC](CCC "CCC"), December 03, 2012

## External Links

## Chess Engine

- [Index of /chess/engines/Jim Ablett/ALICE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ALICE/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

## Misc

- [Alice (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Alice)
- [Alice Cooper from Wikipedia](https://en.wikipedia.org/wiki/Alice_Cooper)
- [Alice in Wonderland (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Alice_in_Wonderland_%28disambiguation%29)
- [Alice in Blunderland: An Iridescent Dream from Wikipedia](https://en.wikipedia.org/wiki/Alice_in_Blunderland:_An_Iridescent_Dream)
- [Alice (Alice's Adventures in Wonderland) from Wikipedia](https://en.wikipedia.org/wiki/Alice_%28Alice%27s_Adventures_in_Wonderland%29)
- [Alice's Adventures in Wonderland from Wikipedia](https://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland)
- [Alice's Adventures in Wonderland (1866)](http://en.wikisource.org/wiki/Alice%27s_Adventures_in_Wonderland_%281866%29) by [Lewis Carroll](https://en.wikipedia.org/wiki/Lewis_Carroll), [Wikisource](https://en.wikipedia.org/wiki/Wikisource)
- [Through the Looking-Glass from Wikipedia](https://en.wikipedia.org/wiki/Through_the_Looking-Glass) <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

[![Alice chess game.png](https://upload.wikimedia.org/wikipedia/commons/0/04/Alice_chess_game.png)](http://en.wikipedia.org/wiki/Through_the_Looking-Glass#Chess)

- [Through the Looking-Glass, and What Alice Found There (1871)](http://en.wikisource.org/wiki/Through_the_Looking-Glass,_and_What_Alice_Found_There) by [Lewis Carroll](https://en.wikipedia.org/wiki/Lewis_Carroll), [Wikisource](https://en.wikipedia.org/wiki/Wikisource)
- [List of minor characters in the Alice series from Wikipedia](https://en.wikipedia.org/wiki/List_of_minor_characters_in_the_Alice_series)
- [The Annotated Alice from Wikipedia](https://en.wikipedia.org/wiki/The_Annotated_Alice)
- [Automated Alice from Wikipedia](https://en.wikipedia.org/wiki/Automated_Alice)
- [Alice chess from Wikipedia](https://en.wikipedia.org/wiki/Alice_chess)
- [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie") - [Alice in Wonderland](https://en.wikipedia.org/wiki/Alice_in_Wonderland_%28song%29), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jessie Willcox Smith's](https://en.wikipedia.org/wiki/Jessie_Willcox_Smith) illustration of Alice surrounded by the characters of Wonderland. (1923), [Alice's Adventures in Wonderland from Wikipedia](https://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Gestatten: Alice](https://www.stmintz.com/ccc/index.php?id=237379) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), June 25, 2002
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Index of /chess/engines/Jim Ablett/ALICE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ALICE/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Index of /chess/engines/Jim Ablett/ALICE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/ALICE/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), Src/include/Bitboard.h
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Lewis Carroll's](https://en.wikipedia.org/wiki/Lewis_Carroll) diagram of the story as a chess game, [Through the Looking-Glass - Chess](https://en.wikipedia.org/wiki/Through_the_Looking-Glass#Chess)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Glen Robert Downey](https://en.wikipedia.org/wiki/Glen_Downey_%28writer%29) (**1998**). *The Truth About Pawn Promotion: The Development of the Chess Motif in Victorian Fiction*. Ph.D. thesis, [University of Victoria](https://en.wikipedia.org/wiki/University_of_Victoria) [pdf](http://www.nlc-bnc.ca/obj/s4/f2/dsk2/tape15/PQDD_0006/NQ34258.pdf) » [Promotions](Promotions "Promotions")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Lewis Carroll's chess problem | ChessVibes](http://www.chessvibes.com/?q=columns/lewis-carrolls-chess-problem), July 14, 2008

**[Up one Level](Engines "Engines")**

