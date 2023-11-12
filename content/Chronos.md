---
title: Chronos
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chronos**

\[ Chronos <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chronos**,

a [WinBoard](WinBoard "WinBoard") compatible chess engine developed by [Guillermo Filia](index.php?title=Guillermo_Filia&action=edit&redlink=1 "Guillermo Filia (page does not exist)"), written in [C](C "C") or [C++](Cpp "Cpp") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The project started in 2008 based on Guillermo Filia's earlier chess engine named **GFC**, and initially incorporated [NagaSkaki's](NagaSkaki "NagaSkaki") [Shifted Bitboards](Shifted_Bitboards "Shifted Bitboards") approach to generated [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
later replaced by [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") following [Robert Hyatt's](Robert_Hyatt "Robert Hyatt") tutorial <a id="cite-note-4" href="#cite-ref-4">[4]</a> [[5]](#cite-note-history-5).

## Selected Features

[[5]](#cite-note-history-5)

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Selectivity](Selectivity "Selectivity")
  - [Fractional Ply Extensions](Extensions#FractionalExtensions "Extensions")
  - [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Razoring](Razoring "Razoring")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Material](Material "Material")
- [Material Hash Table](Material_Hash_Table "Material Hash Table")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
  - [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
  - [Blocked Passed Pawn](Blockade_of_Stop#Passed_Pawns "Blockade of Stop")
- [King Safety](King_Safety "King Safety")
  - [King Piece Tropism](King_Safety#KingTropism "King Safety")
  - [Square Control](King_Safety#SquareControl "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")
- [Endgame](Endgame "Endgame")

## Forum Posts

- [New/Updated Engines: 2009/01/24](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49907) by [Ron Murawski](Ron_Murawski "Ron Murawski"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2009
- [And a proper WB2UCI file for Chronos...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=49286) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), September 09, 2013 » [Wb2UCI](Wb2UCI "Wb2UCI")

## External Links

## Chess Engine

- [Chronos Chess Engine](https://sites.google.com/site/chronosce/Home)
- [Chronos](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Chronos&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Chronos from Wikipedia](https://en.wikipedia.org/wiki/Chronos)
- [Cronus from Wikipedia](https://en.wikipedia.org/wiki/Cronus)
- [Father Time from Wikipedia](https://en.wikipedia.org/wiki/Father_Time)
- [Ralph Towner](Category:Ralph_Towner "Category:Ralph Towner") - Father Time, Live in Korea, September 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Head of Sculpture of [Chronos](https://en.wikipedia.org/wiki/Chronos) in the Knights' Hall of [Royal Castle, Warsaw](https://en.wikipedia.org/wiki/Royal_Castle,_Warsaw), [Image](https://commons.wikimedia.org/wiki/File:Chronos_Statue_Detail.JPG) by [Scotch Mist](https://commons.wikimedia.org/wiki/User:Scotch_Mist), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Engines written in which programming language?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50192) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2009
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [How NagaSkaki plays chess - Move generation](https://mayothi.com/nagaskakichess6.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [Rotated bitmaps, a new twist on an old idea](http://www.craftychess.com/hyatt/bitmaps.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
1. ↑ [5.0](#cite-ref-history-5-0) [5.1](#cite-ref-history-5-1) [Chronos Chess Engine - History](https://sites.google.com/site/chronosce/history-2)

**[Up one Level](Engines "Engines")**

