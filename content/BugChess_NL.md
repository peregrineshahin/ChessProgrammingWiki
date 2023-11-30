---
title: BugChess NL
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BugChess NL**

\[.jpg) Bed-bug <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BugChess**, (QueenMaxima)

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Erik van het Hof](Erik_van_het_Hof "Erik van het Hof") and [Hermen Reitsma](Hermen_Reitsma "Hermen Reitsma") developed in the period from 1996 to 2000, initially with focus on [Losing Chess](Losing_Chess "Losing Chess"), written in [C++](Cpp "Cpp").
BugChess played the [18th Dutch Open Computer Chess Championship 1998](DOCCC_1998 "DOCCC 1998") running on a [Pentium II](X86 "X86") at 450MHz <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
and was active in the late 90s at [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)"), as reported in [Will Singleton's](Will_Singleton "Will Singleton") ICC Green Lists <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The program continued to play as **QueenMaxima(C)** at ICC and was published as [open source engine](Category:Open_Source "Category:Open Source") under the [GPL license](Free_Software_Foundation#GPL "Free Software Foundation").
[UCI](UCI "UCI") compliance was created in 2013 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Features

## [Board Representation](Board_Representation "Board Representation")

- [8x8 Board](8x8_Board "8x8 Board")
- [Piece-Lists](Piece-Lists "Piece-Lists")

## [Search](Search "Search")

- [Fractional Ply](Depth#FractionalPlies "Depth") [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions")
    - [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
    - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
    - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Mobility](Mobility "Mobility")
- [Trapped Bishops](Trapped_Pieces "Trapped Pieces")
- [King Safety](King_Safety "King Safety")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Isolated Pawns](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
  - [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")

## Misc

- [Book Learning](Book_Learning "Book Learning")
- [Pondering](Pondering "Pondering")
- [Losing Chess](Losing_Chess "Losing Chess")

## Selected Games

[DOCCC 1998](DOCCC_1998 "DOCCC 1998"), round 10, BugChess - [CilkChess](CilkChess "CilkChess")

```

[Event "Dutch Open Computer 1998"]
[Site "Leiden NED"]
[Date "1998.11.29"]
[Round "10"]
[White "BugChess"]
[Black "CilkChess"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nf6 3.d4 exd4 4.Bd3 Bb4+ 5.Bd2 Bc5 6.e5 Nd5 7.Bg5 Ne7 8.Nbd2 h6 
9.Bf4 Nbc6 10.Nb3 d6 11.Nxc5 dxc5 12.O-O O-O 13.Qe2 Bf5 14.Bxf5 Nxf5 15.Qb5 Qd5 
16.Bd2 Nxe5 17.Nxe5 Qxe5 18.Qxb7 Rab8 19.Qxa7 Rxb2 20.Qa4 Qe4 21.Rac1 Nh4 
22.f3 Ra8 23.Qc4 Qc6 24.a4 Rxa4 25.Qe2 c4 26.Qe7 Nf5 27.Qe5 Rb5 28.Qe4 Qxe4 
29.fxe4 Nd6 30.Bf4 Nxe4 31.Bxc7 Ra2 32.Rf4 Nc3 33.Rf2 f6 34.g4 Rbb2 35.Bf4 d3 
36.Kh1 Ne2 37.Rd1 Nxf4 0-1

```

## Namesake

- [BugChess2](BugChess_FR "BugChess FR") by [François Karr](Fran%C3%A7ois_Karr "François Karr") and [Jean-Philippe Karr](Jean-Philippe_Karr "Jean-Philippe Karr")

## See also

- [Maxima2](Maxima2 "Maxima2")

## Forum Posts

- [ICC Green List - Jan 10](https://www.stmintz.com/ccc/index.php?id=87365) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), January 10, 2000

## External Links

## Chess Engine

- [GitHub - hof/queenmaxima: QueenMaxima chess program](https://github.com/hof/queenmaxima)

## Misc

- [Bug from Wikipedia](https://en.wikipedia.org/wiki/Bug)
- [Software bug from Wikipedia](https://en.wikipedia.org/wiki/Software_bug)
- [Hemiptera (true bug) from Wikipedia](https://en.wikipedia.org/wiki/Hemiptera)
- [Queen from Wikipedia](https://en.wikipedia.org/wiki/Queen)
- [Maxima from Wikipedia](https://en.wikipedia.org/wiki/Maxima)
- [Queen Máxima of the Netherlands from Wikipedia](https://en.wikipedia.org/wiki/Queen_M%C3%A1xima_of_the_Netherlands)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Bed bug](https://en.wikipedia.org/wiki/Bed_bug) ([Cimex lectularius](https://en.wikipedia.org/wiki/Cimex_lectularius)), Source: *[Hemiptera](https://en.wikipedia.org/wiki/Hemiptera)*, [Encyclopædia Britannica](https://en.wikipedia.org/wiki/Encyclop%C3%A6dia_Britannica) (11th ed.), [v. 13, 1911, p. 260](https://archive.org/stream/encyclopaediabrit13chisrich#page/260/mode/1up), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm") (**1998**). *Report on the 18th Dutch Open Computer-Chess Championship*. [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [ICC Green List - Nov 29](https://www.stmintz.com/ccc/index.php?id=79887) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), November 29, 1999
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [queenmaxima/uci.h at master · hof/queenmaxima · GitHub](https://github.com/hof/queenmaxima/blob/master/src/uci.h)

**[Up one Level](Engines "Engines")**

