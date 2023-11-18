---
title: Defenchess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Defenchess**

**Defenchess**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Can Cetin](index.php?title=Can_Cetin&action=edit&redlink=1 "Can Cetin (page does not exist)") and [Dogac Eldenk](index.php?title=Dogac_Eldenk&action=edit&redlink=1 "Dogac Eldenk (page does not exist)"), written in [C++](Cpp "Cpp"), licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").
Defenchess evolved from the author's former engine *SCTR* <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and had its tournament debut at [TCEC Season 11](TCEC_Season_11 "TCEC Season 11") in 2018, where it won the [Fourth Division](TCEC_Season_11#Fourth "TCEC Season 11") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

## [Board Representation](Board_Representation "Board Representation")

- [8x8 Board](8x8_Board "8x8 Board")
- [Bitboard Board-Definition](Bitboard_Board-Definition#CBoardDef "Bitboard Board-Definition")
- [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [ProbCut](ProbCut "ProbCut")
  - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Razoring](Razoring "Razoring")
  - [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0
  - [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [PV-Move](PV-Move "PV-Move")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [Captures](Captures "Captures") by [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Captures](Captures "Captures") by [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
  - [Bad Bishop](Bad_Bishop "Bad Bishop")
  - [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Isolated Pawns](Isolated_Pawn "Isolated Pawn")
  - [Doubled Pawns](Doubled_Pawn "Doubled Pawn")
  - [Backward Pawns](Backward_Pawn "Backward Pawn")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
  - [Pawn Storms](King_Safety#PawnStorm "King Safety")
  - [Enemy Attacks](King_Safety#Attacking "King Safety")
- [Tempo Bonus](Tempo#Tempo_Bonus "Tempo")

## Forum Posts

- [Lazy SMP >4 Thread Slowdown](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65844) by [Can Cetin](index.php?title=Can_Cetin&action=edit&redlink=1 "Can Cetin (page does not exist)"), [CCC](CCC "CCC"), November 29, 2017
- [Re: Parallel search/LazySMP question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=66044&start=10) by [Can Cetin](index.php?title=Can_Cetin&action=edit&redlink=1 "Can Cetin (page does not exist)"), [CCC](CCC "CCC"), December 18, 2017
- [Re: SCTR 1.1d win64](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65861&start=13) by CMCanavessi, [CCC](CCC "CCC"), January 03, 2018
- [Official Release of Ethereal 10.00 (Two-years Anniversary)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67602&p=763874) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), May 30, 2018
- [Re: TCEC should reconsider the ban on Ethereal](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67994&start=20) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 18, 2018

## External Links

- [GitHub - cetincan0/Defenchess: Chess Engine](https://github.com/cetincan0/Defenchess)
- [Defenchess](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Defenchess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [Defenchess wins TCEC Division 4](http://www.chessdom.com/defenchess-wins-tcec-division-4/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), January 06, 2018 » [TCEC Season 11](TCEC_Season_11 "TCEC Season 11")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Re: SCTR 1.1d win64](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65861&start=13) by CMCanavessi, [CCC](CCC "CCC"), January 03, 2018
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Defenchess wins TCEC Division 4](http://www.chessdom.com/defenchess-wins-tcec-division-4/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), January 06, 2018
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [GitHub - gonzaloarro/MORA-CHESS-ENGINE: UCI Chess Engine in the 2100-2200 ELO range - README.md](https://github.com/gonzaloarro/MORA-CHESS-ENGINE)

**[Up one level](Engines "Engines")**

