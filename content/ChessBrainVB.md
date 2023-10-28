---
title: ChessBrainVB
---
**[Home](Home "Home") * [Engines](Engines "Engines") * ChessBrainVB**

**ChessBrainVB**,

an [open source chess engine](Category:Open_Source "Category:Open Source") by [Roger Zuehlsdorf](index.php?title=Roger_Zuehlsdorf&action=edit&redlink=1 "Roger Zuehlsdorf (page does not exist)"), written in [Visual Basic](Basic#VB "Basic") to run under 32-bit [Windows](Windows "Windows"), first announced and released in September 2015 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The common source subset could either compiled using [Visual Basic 6.0](https://en.wikipedia.org/wiki/Visual_Basic#1990s) to create a [WinBoard](WinBoard "WinBoard") compliant executable - or, albeit about 15 times slower, may be interpreted by [Visual Basic for Applications](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications) to run under [Microsoft Office](https://en.wikipedia.org/wiki/Microsoft_Office) applications, that is [Word](https://en.wikipedia.org/wiki/Microsoft_Word), [Excel](https://en.wikipedia.org/wiki/Microsoft_Excel), or [PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint), along with an own [GUI](GUI "GUI") based on [Windows Forms](https://en.wikipedia.org/wiki/Windows_Forms).

ChessBrainVB was initially based on the source code of [LarsenVB](LarsenVB "LarsenVB") by [Luca Dormio](Luca_Dormio "Luca Dormio"), which in turn was inspired by the [C](C "C") program [Faile 0.6](Faile "Faile") by [Adrien M. Regimbald](Adrien_Regimbald "Adrien Regimbald"). Still using the [10x12](10x12_Board "10x12 Board") [mailbox](Mailbox "Mailbox") [board representation](Board_Representation "Board Representation"), ChessBrainVB's [search](Search "Search") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [evaluation](Evaluation "Evaluation") subsequently improved influenced by ideas from open source programs such as [CuckooChess](CuckooChess "CuckooChess"), [Sjeng](Sjeng "Sjeng"), [Protector](Protector "Protector") and [Stockfish](Stockfish "Stockfish") combined with own ideas <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Screenshot](#screenshot)
- [2 Features](#features)
  - [2.1 Board Representation](#board-representation)
  - [2.2 Search](#search)
  - [2.3 Evaluation](#evaluation)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
- [6 References](#references)

## Screenshot

[](https://github.com/RZulu54/ChessBrainVB/blob/master/ChessBrainVBA_Screenshot.jpg)
ChessBrainVBA <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## [Board Representation](Board_Representation "Board Representation")

- [10x12 Board](10x12_Board "10x12 Board")
- [Piece-Lists](Piece-Lists "Piece-Lists")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")

[Hash Move](Hash_Move "Hash Move")
[Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
[In Check](Check "Check")
[Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
[Counter Moves History](History_Heuristic#CMHist "History Heuristic")
[Killer Heuristic](Killer_Heuristic "Killer Heuristic")
[MVV/LVA](MVV-LVA "MVV-LVA")
[Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
[SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")

- [Selectivity](Selectivity "Selectivity")

[Check Extensions](Check_Extensions "Check Extensions")
[Futility Pruning](Futility_Pruning "Futility Pruning")
[Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
[Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
[Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
[Razoring](Razoring "Razoring")

- [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Center Control](Center_Control "Center Control")
- [Mobility](Mobility "Mobility")

[Trapped Pieces](Trapped_Pieces "Trapped Pieces")
[Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")

- [Pawn Structure](Pawn_Structure "Pawn Structure")

[Backward Pawn](Backward_Pawn "Backward Pawn")
[Doubled Pawn](Doubled_Pawn "Doubled Pawn")
[Isolated Pawn](Isolated_Pawn "Isolated Pawn")
[Phalanx](</Duo_Trio_Quart_(Bitboards)> "Duo Trio Quart (Bitboards)")

- [Passed Pawns](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")

[Pawn Shelter](King_Safety#PawnShield "King Safety")
[Pawn Storm](King_Safety#PawnStorm "King Safety")
[Square Control](King_Safety#SquareControl "King Safety")

- [Tempo](Tempo "Tempo")

## See also

- [Category:Brain](Category:Brain "Category:Brain")
- [Chess Brain](Chess_Brain "Chess Brain")
- [ChessBrain](ChessBrain "ChessBrain")

## Forum Posts

- [My new exotic engine: ChessBrainVB for OfficeVBA (1950 ELO)](http://www.talkchess.com/forum/viewtopic.php?t=57705) by [Roger Zuehlsdorf](index.php?title=Roger_Zuehlsdorf&action=edit&redlink=1 "Roger Zuehlsdorf (page does not exist)"), [CCC](CCC "CCC"), September 20, 2015
- [ChessBrainVB V2.0 released (WB 2600 ELO, Office VBA 2100ELO)](http://www.talkchess.com/forum/viewtopic.php?t=59344) by [Roger Zuehlsdorf](index.php?title=Roger_Zuehlsdorf&action=edit&redlink=1 "Roger Zuehlsdorf (page does not exist)"), [CCC](CCC "CCC"), February 24, 2016
- [ChessBrain VB 3.02 - release](http://www.talkchess.com/forum/viewtopic.php?t=62462) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), December 12, 2016
- [ChessBrain VB 3.20 released](http://www.talkchess.com/forum/viewtopic.php?t=63431) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), March 13, 2017
- [ChessBrainVB 3.30 released](http://www.talkchess.com/forum/viewtopic.php?t=64195) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 06, 2017
- [ChessBrainVB 3.31 (WB-Engine) release](http://www.talkchess.com/forum/viewtopic.php?t=64318) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 17, 2017
- [WinBoard 4.8.0 and ChessBrainVB](http://www.talkchess.com/forum/viewtopic.php?t=64320) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 17, 2017
- [ChessBrainVB 3.60](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66035) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), December 17, 2017

## External Links

- [GitHub - RZulu54/ChessBrainVB: Chess engine with GUI for Excel / Word VBA - plus VB6 (Visual Basic 6) edition as winboard engine](https://github.com/RZulu54/ChessBrainVB)
- [ChessBrainVB 3.20](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=ChessBrainVB%203.20) in [CCRL 40/4](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [My new exotic engine: ChessBrainVB for OfficeVBA (1950 ELO)](http://www.talkchess.com/forum/viewtopic.php?t=57705) by [Roger Zuehlsdorf](index.php?title=Roger_Zuehlsdorf&action=edit&redlink=1 "Roger Zuehlsdorf (page does not exist)"), [CCC](CCC "CCC"), September 20, 2015
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [ChessBrainVB/Search.bas at master · RZulu54/ChessBrainVB · GitHub](https://github.com/RZulu54/ChessBrainVB/blob/master/Development/Modules/Search.bas)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [ChessBrainVB/ChessBrainVB_Notes.txt at master · RZulu54/ChessBrainVB · GitHub](https://github.com/RZulu54/ChessBrainVB/blob/master/Development/ChessBrainVB_Notes.txt)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [ChessBrainVB/ChessBrainVBA_Screenshot.jpg at master · RZulu54/ChessBrainVB · GitHub](https://github.com/RZulu54/ChessBrainVB/blob/master/ChessBrainVBA_Screenshot.jpg)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Features based on [V3.31 · RZulu54/ChessBrainVB@870f735 · GitHub](https://github.com/RZulu54/ChessBrainVB/commit/870f735b3ed195f58e335ea95a9523bfede2b458)

**[Up one Level](Engines "Engines")**

