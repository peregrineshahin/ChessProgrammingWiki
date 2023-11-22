---
title: Hagrid
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Hagrid**

**Hagrid**,

a [WinBoard](WinBoard "WinBoard") and [UCI](UCI "UCI") compliant chess engine by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), written in [C++](Cpp "Cpp"), first released in March 2002, while the development started as recently as September 2001 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Hagrid is a [bitboard](Bitboards "Bitboards") engine and performs [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), while its successor [Snitch](Snitch "Snitch") keeps the plain [8x8 board](8x8_Board "8x8 Board") and [piece-lists](Piece-Lists "Piece-Lists"), using [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") (R=2)
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [MVV/LVA](MVV-LVA "MVV-LVA")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [King Safety](King_Safety "King Safety")
- [Tuning](Automated_Tuning "Automated Tuning")

## Misc

- [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")

## See also

- [Snitch](Snitch "Snitch")

## Forum Posts

- [New engine "Hagrid"](https://www.stmintz.com/ccc/index.php?id=220512) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [CCC](CCC "CCC"), March 30, 2002
- [New Chess Engine "Hagrid"](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36625&p=138765) by Tony Worsman, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 30, 2002
- [Hagrid new version](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36651&p=138857) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2002
- [Hagrid and Chessbase (Fritz 6) GUI](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36670&p=138931) by [Roger Brown](index.php?title=Roger_Brown&action=edit&redlink=1 "Roger Brown (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 03, 2002 » [Fritz GUI](Fritz#FritzGUI "Fritz")
- [Hagrid 0.7.2 available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=36849&p=139701) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 13, 2002
- [Hagrid 0.7.45 released !](https://www.stmintz.com/ccc/index.php?id=235751) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [CCC](CCC "CCC"), June 16, 2002
- [Re: ...a new Hagrid-version?](https://www.stmintz.com/ccc/index.php?id=320241) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [CCC](CCC "CCC"), October 08, 2003
- [New engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45881&p=174271) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2004
- [New engine Snitch 1.0.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=74&p=157) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2004

## External Links

## Chess Engine

- [Snitch and Hagrid two free UCI / Winboard chess engines](http://www.friedelprivat.de/)
- [Index of /chess/engines/Norbert's collection/Hagrid (Compilation)/v0.6.32/hagrid](http://kirr.homeunix.org/chess/engines/Norbert's%20collection/Hagrid%20%28Compilation%29/v0.6.32/hagrid/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner") hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Index of /chess/engines/Norbert's collection/Hagrid (Compilation)/v0.7.47/hagrid](http://kirr.homeunix.org/chess/engines/Norbert's%20collection/Hagrid%20%28Compilation%29/v0.7.47/hagrid/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner") hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

## Misc

- [Rubeus Hagrid from Wikipedia](https://en.wikipedia.org/wiki/Rubeus_Hagrid)
- [Magical creatures in Harry Potter from Wikipedia](https://en.wikipedia.org/wiki/Magical_creatures_in_Harry_Potter#Hagrid.27s_pets)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Snitch and Hagrid two free UCI / Winboard chess engines](http://www.friedelprivat.de/) - News & History
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171&start=21) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 07, 2004
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Snitch and Hagrid two free UCI / Winboard chess engines](http://www.friedelprivat.de/) - Developer

**[Up one level](Engines "Engines")**

