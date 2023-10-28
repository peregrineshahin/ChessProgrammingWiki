---
title: Gullydeckel
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gullydeckel**

\[ [Manhole cover](https://en.wikipedia.org/wiki/Manhole_cover) in [Rome](https://en.wikipedia.org/wiki/Rome) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Gullydeckel**, (Gullydeckel2, Gully)

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") (CEPT) compliant [open source engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") by [Martin Borriss](Martin_Borriss "Martin Borriss"), written in [C](C "C"). A first version, Gullydeckel **1**, has been developed in 1994/1995. Gullydeckel **2** was written mainly in 1996, while [Windows 32](Windows "Windows") support, analysis, [pondering](Pondering "Pondering"), [WinBoard](WinBoard "WinBoard") protocol version 2 aka CEPT and [ChessBase GUI](</ChessBase_(Database)#GUI> "ChessBase (Database)") compatibility was finally realized in 2002/2003 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Beside Windows, supported platform is [Linux](Linux "Linux").

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
- [2 0x88 Difference](#0x88-difference)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Piece-Lists](Piece-Lists "Piece-Lists")
- [0x88](0x88 "0x88")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [R](Depth_Reduction_R "Depth Reduction R")=2
- [Check Extensions](Check_Extensions "Check Extensions")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Imbalance Table](Material_Tables "Material Tables")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Rook on 7th Rank](Rook_on_Seventh "Rook on Seventh")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Weak Pawns](Weak_Pawns "Weak Pawns")
- [Passed Pawn](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")

## 0x88 Difference

The pre-initialized static int vector[256] in "attacks.c" <a id="cite-note-3" href="#cite-ref-3">[3]</a> with [ray directions](Direction#RayDirections "Direction") encoded, which is indexed by [0x88 square difference](0x88#SquareRelations "0x88") plus offset, somehow reminds on a [Gullydeckel](https://de.wikipedia.org/wiki/Schachtdeckel), the colloquial German name for [Manhole cover](https://en.wikipedia.org/wiki/Manhole_cover) <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```

/*
if we find that two squares are related according to matrix SqRel,
we use another matrix to look up the direction of the move required
('to walk the vector') if it is a sliding piece (R,B,Q)
*/

static int vector[256] = {
   0  ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,UR,0 ,0 ,0 ,0 ,0 ,0 ,
   UP ,0 ,0 ,0 ,0 ,0 ,0 ,UL,0 ,0 ,UR,0 ,0 ,0 ,0 ,0 ,
   UP ,0 ,0 ,0 ,0 ,0 ,UL,0 ,0 ,0 ,0 ,UR,0 ,0 ,0 ,0 ,
   UP ,0 ,0 ,0 ,0 ,UL,0 ,0 ,0 ,0 ,0 ,0 ,UR,0 ,0 ,0 ,
   UP ,0 ,0 ,0 ,UL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,UR,0 ,0 ,
   UP ,0 ,0 ,UL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,UR,0 ,
   UP ,0 ,UL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,UR,
   UP ,UL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,RI,RI,RI,RI,RI,RI,RI,
   0  ,LE,LE,LE,LE,LE,LE,LE,0 ,0 ,0 ,0 ,0 ,0 ,0 ,DR,
   DN ,DL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,DR,0 ,
   DN ,0 ,DL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,DR,0 ,0 ,
   DN ,0 ,0 ,DL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,DR,0 ,0 ,0 ,
   DN ,0 ,0 ,0 ,DL,0 ,0 ,0 ,0 ,0 ,0 ,DR,0 ,0 ,0 ,0 ,
   DN ,0 ,0 ,0 ,0 ,DL,0 ,0 ,0 ,0 ,DR,0 ,0 ,0 ,0 ,0 ,
   DN ,0 ,0 ,0 ,0 ,0 ,DL,0 ,0 ,DR,0 ,0 ,0 ,0 ,0 ,0 ,
   DN ,0 ,0 ,0 ,0 ,0 ,0 ,DL,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0
 };

```

## Forum Posts

- [Re: Deep Quiesence Searching](https://groups.google.com/d/msg/rec.games.chess.computer/b7AtuVY4reE/7bWjK9x3v6kJ) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 24, 1997
- [Re: Deep Quiesence Searching](https://groups.google.com/d/msg/rec.games.chess.computer/b7AtuVY4reE/fxkqPXwkaQIJ) by [Martin Borriss](Martin_Borriss "Martin Borriss"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 25, 1997
- [Gullydeckel - move generator](https://www.stmintz.com/ccc/index.php?id=145760) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [CCC](CCC "CCC"), December 20, 2000

## External Links

## Chess Engine

- [Gullydeckel Chess Program](http://borriss.com/)
- [GitHub - borriss/gully: Gullydeckel Chess Program](https://github.com/borriss/gully)
- [Gullydeckel 2.16pl1](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Gullydeckel%202.16pl1) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Gullydeckel – Wiktionary.de](https://de.wiktionary.org/wiki/Gullydeckel) (German)
- [Schachtdeckel Wikipedia.de](https://de.wikipedia.org/wiki/Schachtdeckel) (German)
- [Manhole cover from Wikipedia](https://en.wikipedia.org/wiki/Manhole_cover)
- [Storm drain from Wikipedia](https://en.wikipedia.org/wiki/Storm_drain)
- [Sanitary sewer from Wikipedia](https://en.wikipedia.org/wiki/Sanitary_sewer)
- [Gully (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Gully_%28disambiguation%29)
- [Manhole cover - Wikimedia Commons](https://commons.wikimedia.org/wiki/Manhole_cover)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Manhole cover](https://en.wikipedia.org/wiki/Manhole_cover) in [Rome](https://en.wikipedia.org/wiki/Rome) with [SPQR](https://en.wikipedia.org/wiki/SPQR) inscription, Image by [Indian Joe](https://en.wikipedia.org/wiki/User:Indian_Joe), January 08, 2007, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [SPQR from Wikipedia](https://en.wikipedia.org/wiki/SPQR)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Gullydeckel2 chess playing program](http://borriss.com/g2/RELEASE)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Gullydeckel Chess Program - Download](http://borriss.com/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> edited, symbols replaced for column alignment

**[Up one Level](Engines "Engines")**

