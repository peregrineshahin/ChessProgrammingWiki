---
title: Material Tables
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Material](Material "Material") \* Material Tables**


**Material Tables** contain precomputed material values for all possible material constellations of both sides, considering not only the dot-product of the piece values times number of pieces, but material imbalance features and even [insufficient material](Material#InsufficientMaterial "Material"). The up to ten piece counters of {white, black} x {pawns, knights, bishops, rooks, queen(s)} act as index into a 10-dimensional [array](Array "Array"), where each dimension covers one piece kind and color. However, since there are up to eight pawns (0..8), rarely up to ten pieces and nine queens per side, the size of such an array would be with




```C++
(9 * 11 * 11 * 11 * 10)² = 119790² = 14,349,644,100

```

much to huge, which was the main reason to use a smaller [material hash table](Material_Hash_Table "Material Hash Table") instead, to cache the once calculated values. A material key needs only [incremental update](Incremental_Updates "Incremental Updates") if [captures](Captures "Captures") or [promotions](Promotions "Promotions") occur, so that even small tables are sufficient for a hit-rate of 99% or greater. A compromise for precomputed tables is to consider only "usual" material constellations, that is no more than two knights, bishops or rooks and one queen per side, ...




```C++
(9 * 3 * 3 * 3 * 2)² = 486² = 236,196

```

... which makes a reasonable size for todays computers below 1/4 MByte entries.




```C++

value_t matValue[9][9][3][3][3][3][3][3][2][2];

```

or better a one dimensional error with an [incremental updated](Incremental_Updates "Incremental Updates") material key.




```C++

value_t matValue[9*9*3*3*3*3*3*3*2*2];

```

Material tables along with imbalance tables, first appeared in [Jury Osipov's](Jury_Osipov "Jury Osipov") disputed <a id="cite-note-1" href="#cite-ref-1">[1]</a> [open source engine](Category:Open_Source "Category:Open Source") [Strelka 2.0](Strelka "Strelka"), apparently [reverse engineered](https://en.wikipedia.org/wiki/Reverse_engineering) from [Rybka 1.0](Rybka "Rybka") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Indices were initialized that way - with [bitboards](Bitboards "Bitboards") even the [population count](Population_Count "Population Count") of a [board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") is used:




```C++

  materialSum_key =
    pieceCount[WhiteQueen]  +
    pieceCount[BlackQueen]  * 2 +
    pieceCount[WhiteRook]   * 2*2 +
    pieceCount[BlackRook]   * 2*2*3 +
    pieceCount[WhiteBishop] * 2*2*3*3 +
    pieceCount[BlackBishop] * 2*2*3*3*3 +
    pieceCount[WhiteKnight] * 2*2*3*3*3*3 +
    pieceCount[BlackKnight] * 2*2*3*3*3*3*3 +
    pieceCount[WhitePawn]   * 2*2*3*3*3*3*3*3 +
    pieceCount[BlackPawn]   * 2*2*3*3*3*3*3*3*9;

  materialDiff_key =
    (pieceCount[WhiteQueen]  - pieceCount[BlackQueen])  * 10 +
    (pieceCount[WhiteRook]   - pieceCount[BlackRook])   * 5  +
    (pieceCount[WhiteBishop] - pieceCount[BlackBishop]) * 3  +
    (pieceCount[WhiteKnight] - pieceCount[BlackKnight]) * 3  +
    (pieceCount[WhitePawn]   - pieceCount[BlackPawn]);

```

An array of ten [nibble](Nibble "Nibble") piece counters can be interpreted as 40-bit number where each piece count is multiplied with consecutive power of sixteen factors with exponents of 0 to 9, the materialSum\_key key has minimal population factors which result in only a 18-bit word. While this dot-product and its incremental update looks like a reversible [perfect hashing-function](Hash_Table#PerfectHashing "Hash Table"), is more like a multi-dimensional array-lookup. 


In 2010, [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") proposed a similar, cache friendlier scheme for common minor piece exchanges, by altering rooks, bishops and knights with appropriate offsets <a id="cite-note-4" href="#cite-ref-4">[4]</a> .



## Forum Posts


### 2000 ...


* [Piece Cooperation and Penalties](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5377) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 14, 2006
* [Why material imbalance tables are needed](http://www.talkchess.com/forum/viewtopic.php?t=15679) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 09, 2007
* [Material Tables and Indexing](http://www.talkchess.com/forum/viewtopic.php?t=20659) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), April 14, 2008


 [Re: Material Tables and Indexing](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=185340) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC](CCC "CCC"), April 22, 2008
### 2010 ...


* [Material tables](http://www.talkchess.com/forum/viewtopic.php?t=33021) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 03, 2010
* [Efficiently index material signatures and lookup](http://www.talkchess.com/forum/viewtopic.php?t=33035) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 03, 2010
* [An experiment with material imbalances and game-phase](http://www.talkchess.com/forum/viewtopic.php?t=47713) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 06, 2013
* [Accessing Material Imbalance Information?](http://www.talkchess.com/forum/viewtopic.php?t=50550) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 19, 2013


## External Links


* [The Evaluation of Material Imbalances](http://www.danheisman.com/evaluation-of-material-imbalances.html) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (first published in [Chess Life](https://en.wikipedia.org/wiki/Chess_Life) March 1999, on-line version edited by [Dan Heisman](Dan_Heisman "Dan Heisman"))
* [A Material Base for everybody](http://www.top-5000.nl/mb.htm) from [Home of the Dutch Rebel](http://www.top-5000.nl/) by [Ed Schröder](Ed_Schroder "Ed Schroder")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Strelka controversy from Wikipedia](https://en.wikipedia.org/wiki/Rybka#Strelka_controversy)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Strelka 2.0](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=3006) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2008
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [A Material Base for everybody](http://www.top-5000.nl/mb.htm) from [Home of the Dutch Rebel](http://www.top-5000.nl/) by [Ed Schröder](Ed_Schroder "Ed Schroder")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Cache-friendier material index](http://www.talkchess.com/forum/viewtopic.php?t=33561) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 31, 2010

**[Up one level](Material "Material")**







 
