---
title: Exacto
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Exacto**

\[ Exact sequence <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Exacto**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Daniel Sparks](Daniel_Sparks "Daniel Sparks"), written in [C++](Cpp "Cpp"), the source code covered by a [BSD license](https://en.wikipedia.org/wiki/BSD_licenses).
Starting with version **0.e**, released in March 2014, Exacto uses [bitboards](Bitboards "Bitboards") as internal board representation, while former versions, Daniel has worked on sporadically throughout the years, were [0x88](0x88 "0x88").

## Features

<a id="cite-note-2" href="#cite-ref-2">[2]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")

## Search

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [PVS](Principal_Variation_Search "Principal Variation Search")/[Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Reductions](Reductions "Reductions")
    - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
    - [Razoring](Razoring "Razoring") (Pre-pre-frontier Nodes)
  - [Pruning](Pruning "Pruning")
    - [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
    - [Pruning](Pruning "Pruning") via [Transposition Table](Transposition_Table "Transposition Table")
    - [Futility Pruning](Futility_Pruning "Futility Pruning") ([Frontier](Frontier_Nodes "Frontier Nodes") and [Pre-frontier Nodes](Pre_Frontier_Node "Pre Frontier Node"))
    - [Quiescence Search](Quiescence_Search "Quiescence Search")
    - [Delta Pruning](Delta_Pruning "Delta Pruning") (in Quiescence)
  - [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
    - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [MVV/LVA](MVV-LVA "MVV-LVA")

## Evaluation

- [Material](Material "Material")
- [Tapered Evaluation](Tapered_Eval "Tapered Eval")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Pawn Structure](Pawn_Structure "Pawn Structure") with [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Pawn Chains](Pawn_Chain "Pawn Chain")
  - [Isolated Pawns](Isolated_Pawn "Isolated Pawn")
  - [Backward Pawns](Backward_Pawn "Backward Pawn")
  - [Doubled Pawns](Doubled_Pawn "Doubled Pawn")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
- [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
  - [Bad Bishop](Bad_Bishop "Bad Bishop")
  - [Bishop Pair](Bishop_Pair "Bishop Pair")
  - [Rook on Open File](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh Rank](Rook_on_Seventh "Rook on Seventh")
  - [Development](Development "Development") and [Castling](Castling "Castling")
  - [Undefended minor piece](Loose_Piece "Loose Piece") penalty
- [King Safety](King_Safety "King Safety")
  - [Enemy attacks on squares near king](King_Safety#SquareControl "King Safety")
  - [Pawn fortress](King_Safety#PawnShield "King Safety") / Castling Destination
  - [Open Files](Open_File "Open File") and [Half-open Files](Half-open_File "Half-open File") around the [King](King "King")
  - [King Piece Tropism](King_Safety#KingTropism "King Safety")

## Forum Posts

- [Can you try running my engine?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=51514) by [Daniel Sparks](Daniel_Sparks "Daniel Sparks"), [CCC](CCC "CCC"), March 06, 2014
- [Engine release Exacto 0.e](http://www.talkchess.com/forum/viewtopic.php?t=51546) by [Daniel Sparks](Daniel_Sparks "Daniel Sparks"), [CCC](CCC "CCC"), March 10, 2014
- [Re: Exacto - something is still wrong](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=51767&start=2) by [Daniel Sparks](Daniel_Sparks "Daniel Sparks"), [CCC](CCC "CCC"), March 30, 2014

## External Links

## Chess Engine

- [GitHub - d-sparks/exacto: Exacto Chess Engine](https://github.com/d-sparks/exacto)
- [Exacto 0.e 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Exacto%200.e%2064-bit#Exacto_0_e_64-bit) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [exacto - Wiktionary](http://en.wiktionary.org/wiki/exacto)
- [exact - Wiktionary](http://en.wiktionary.org/wiki/exact)
- [Exact sequence from Wikipedia](https://en.wikipedia.org/wiki/Exact_sequence)
- [Exact science from Wikipedia](https://en.wikipedia.org/wiki/Exact_science)
- [Henry Threadgill Very Very Circus](https://en.wikipedia.org/wiki/Henry_Threadgill) - Exacto, [Spirit Of Nuff...Nuff](https://en.wikipedia.org/wiki/Spirit_of_Nuff...Nuff) (1990), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Shows how any [exact sequence](https://en.wikipedia.org/wiki/Exact_sequence) is weaved together from several overlapping short exact sequences, [Axel Boldt](https://en.wikipedia.org/wiki/User:AxelBoldt), February 2004, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Features based on source, [GitHub - d-sparks/exacto: Exacto Chess Engine](https://github.com/d-sparks/exacto)

**[Up one level](Engines "Engines")**

