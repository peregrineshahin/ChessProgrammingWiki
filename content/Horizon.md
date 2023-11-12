---
title: Horizon
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Horizon**

\[ Horizon - Sky View <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Horizon**, (Horizon Chess)

a [WinBoard](WinBoard "WinBoard") compatible chess engine by primary author [Ron Murawski](Ron_Murawski "Ron Murawski") and chess advisor and book author [Jim Monaghan](index.php?title=Jim_Monaghan&action=edit&redlink=1 "Jim Monaghan (page does not exist)").
Written in [C](C "C"), the programming started in July 2001, first release was already in October 2001.
Initially running atop a much-modified version of [Colin Frayn's](Colin_Frayn "Colin Frayn") open-source [Beowulf](Beowulf "Beowulf") infrastructure, there's very little of Beowulf that remains within Horizon and less with each release <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows") (Asymmetric on [Side to move](Side_to_move "Side to move"))
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic") with two [Killers](Killer_Move "Killer Move") and one [Mate Killer](Mate_Killers "Mate Killers") per [Ply](Ply "Ply")
- [Selectivity](Selectivity "Selectivity")
  - [Fractional Extensions / Reductions](Extensions#FractionalExtensions "Extensions")
  - [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions")
  - [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
  - [Check Extensions](Check_Extensions "Check Extensions") ([Discovered Check](Discovered_Check "Discovered Check"))
  - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
  - [Passed Pawn Extensions (7th Rank)](Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search") with [Check Extensions](Check_Extensions "Check Extensions")
  - [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") ([R](Depth_Reduction_R "Depth Reduction R") 2-4.5, Up to 3 [Null Noves](Null_Move "Null Move") per Line)
  - [Null Move Verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Adaptive Razoring](Razoring "Razoring")
  - [Reductions](Reductions "Reductions") (for non-dangerous moves)

## Tournament Play

Horizon played the [WCRCC 2007](WCRCC_2007 "WCRCC 2007") and [WCRCC 2008](WCRCC_2008 "WCRCC 2008") Annual ACCA World Computer Rapid Chess Championship.

## Selected Games

[WCRCC 2008](WCRCC_2008 "WCRCC 2008"), round 14, Horizon - [Tornado](Tornado "Tornado") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "WCRCC 2008"]
[Site "Internet Chess Club"]
[Date "2008.06.22"]
[Round "14"]
[White "Horizon"]
[Black "Tornado"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 Bb7 
9.O-O a6 10.a4 b4 11.Nb1 c5 12.Nbd2 cxd4 13.exd4 Be7 14.Nc4 O-O 15.Be3 Ng4 
16.h3 Nxe3 17.fxe3 Rc8 18.Qe2 Qc7 19.e4 Kh8 20.Rac1 f6 21.Nfd2 e5 22.Nb3 exd4 
23.Nca5 Qb8 24.Nxb7 Rxc1 25.Rxc1 Qxb7 26.Bxa6 Qa7 27.Bb5 d3+ 28.Qf2 Qxf2+ 
29.Kxf2 f5 30.Bxd7 fxe4+ 31.Kg1 e3 32.Bb5 d2 33.Rb1 Bf6 34.Be2 g6 35.a5 Be5 
36.Bf3 Bxb2 37.a6 Rf7 38.a7 Rxa7 39.Rxb2 Rd7 40.Rb1 Rd3 41.Kf1 h5 42.Bd1 Rc3 
43.Ke2 h4 44.Nd4 Rc5 45.Nc2 Rg5 46.Nxe3 Rb5 47.Rb3 Rb8 48.Bc2 Kg7 49.Kxd2 Rb5
1-0

```

## See also

- [Horizon Effect](Horizon_Effect "Horizon Effect")
- [Horizon Node](Horizon_Node "Horizon Node")

## External Links

## Chess Engine

- [Horizon Chess - Main - Horizon Chess](http://www.horizonchess.com/pmwiki.php?n=Main.HomePage)

[Horizon Chess - Main - Engine Technical Description](http://www.horizonchess.com/pmwiki.php?n=Main.EngineTechnicalDescription)

- [Horizon](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Horizon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Horizon from Wikipedia](https://en.wikipedia.org/wiki/Horizon)
- [Horizon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Horizon_%28disambiguation%29)
- [Horizon effect from Wikipedia](https://en.wikipedia.org/wiki/Horizon_effect)
- [Indigo Jam Unit](Category:Indigo_Jam_Unit "Category:Indigo Jam Unit") - Horizon, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Sky View 2](http://commons.wikimedia.org/wiki/File:SkyView2.PNG) by gierszewski, 2005, Sunrise at [Calgary](https://en.wikipedia.org/wiki/Calgary), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Horizon Chess - Main - Acknowledgements](http://www.horizonchess.com/pmwiki.php?n=Main.HomePage)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Features from [Horizon Chess - Main - Engine Technical Description](http://www.horizonchess.com/pmwiki.php?n=Main.EngineTechnicalDescription)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [2008 Second Annual ACCA World Computer Chess Championships - Results - PGN-Download](http://compchess.org/ACCAWCRCC/2008ACCAWCRCC/2008WCRCCResults.html)

**[Up one Level](Engines "Engines")**

