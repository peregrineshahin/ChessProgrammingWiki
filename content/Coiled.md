---
title: Coiled
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Coiled**

[](File:SlinkySpringstoFame.jpg) Slinky Springs to Fame <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Coiled**,

an [UCI](UCI "UCI") compliant chess engine by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), written in [C](C "C"), first released in 2013. Coiled **0.6**, released in July 2018 is available as 32-bit and 64-bit executable for [Windows](Windows "Windows") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Coiled-NNUE **0.7** was released in August 2021 as [Open Source](Category:Open_Source "Category:Open Source") licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), using a [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") network with [CFish](CFish "CFish") derived probing code <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Board Representation](Board_Representation "Board Representation")

- [8x8 Board](8x8_Board "8x8 Board")
- [Simple Move Generation](Move_Generation "Move Generation")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [PVS](Principal_Variation_Search "Principal Variation Search") / [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Repetitions](Repetitions "Repetitions")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Selectivity](Selectivity "Selectivity")
  - [Extensions](Extensions "Extensions")
    - [Check Extensions](Check_Extensions "Check Extensions")
    - [Passed Pawn to 7th Rank](Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Pruning](Pruning "Pruning")
    - [Futility Pruning](Futility_Pruning "Futility Pruning")
    - [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
    - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") ([R](Depth_Reduction_R "Depth Reduction R") = 3)
    - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Reductions](Reductions "Reductions")
    - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
    - [Razoring](Razoring "Razoring")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [PV-Move](PV-Move "PV-Move")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [NNUE](NNUE "NNUE") (Coiled-NNUE 0.7)
- [Material](Material "Material")
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
  - [Hidden Passed Pawn](Hidden_Passed_Pawn "Hidden Passed Pawn")
  - [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
  - [Faker](Faker "Faker")
- [Bishop](Evaluation_of_Pieces#Bishop "Evaluation of Pieces")
  - [Bishop Pair](Bishop_Pair "Bishop Pair")
  - [Mobility](Mobility "Mobility")
  - [Trapped Bishop](Trapped_Pieces "Trapped Pieces")
  - [Square Control](Square_Control "Square Control")
- [Knight](Evaluation_of_Pieces#Knight "Evaluation of Pieces")
  - [Outposts](Outposts "Outposts")
  - [Mobility](Mobility "Mobility")
  - [Trapped Knight](Trapped_Pieces "Trapped Pieces")
  - [Square Control](Square_Control "Square Control")
- [Rook](Evaluation_of_Pieces#Rook "Evaluation of Pieces")
  - [On Open and Semi-Open File](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh Rank](Rook_on_Seventh "Rook on Seventh")
  - [Mobility](Mobility "Mobility")
  - [Trapped Rook](Trapped_Pieces "Trapped Pieces")
  - [Square Control](Square_Control "Square Control")
- [King Safety](King_Safety "King Safety")
  - [Castling Rights](Castling_Rights "Castling Rights")
  - [Pawn Shield](King_Safety#PawnShield "King Safety")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [King Tropism](King_Safety#KingTropism "King Safety")
- [Endgame](Endgame "Endgame") [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
  - [Insufficient Material](Material#InsufficientMaterial "Material")
  - [KPK](KPK "KPK")
  - [KRK](KRK "KRK")
  - [KBNK](KBNK_Endgame "KBNK Endgame")
  - KQK
  - KBBK
  - [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")

## Misc

- [Opening Book](Opening_Book "Opening Book") ([SQLite](https://en.wikipedia.org/wiki/SQLite) format)
- [Pondering](Pondering "Pondering")
- [UCI](UCI "UCI")

## See also

- [Loop](</Loop_(Program)> "Loop (Program)")

## Forum Posts

- [Hispanic chess engines + Winboard Zeta Pack number 18](http://www.talkchess.com/forum/viewtopic.php?t=48965) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), August 14, 2013
- [Coiled 0.2b](http://www.talkchess.com/forum/viewtopic.php?t=53044) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), July 22, 2014
- [Coiled 0.4](http://www.talkchess.com/forum/viewtopic.php?t=61406) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), September 12, 2016
- [Coiled v.0.5 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68009) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), July 17, 2018

[Re: Coiled v.0.5 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68009&start=3) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), July 18, 2018

- [Update: Coiled-NNUE 0.7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77887) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), August 06, 2021

## External Links

## Chess Engine

- [Coiled - Información y descargar. Motor de ajedrez UCI](http://www.oscargavira.es/?sec=Coiled_Informacion) (Spanish)
- [GitHub - Oscar-Gavira/Coiled-NNUE: Motor de ajedrez de protocolo UCI](https://github.com/Oscar-Gavira/Coiled-NNUE)
- [Coiled](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Coiled&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [Coiled Spring](https://www.chess.com/article/view/coiled-spring) by [Pentala Harikrishna](https://en.wikipedia.org/wiki/Pentala_Harikrishna), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), September 12, 2011
- [coiled - Wiktionary](https://en.wiktionary.org/wiki/coiled)
- [coil - Wiktionary](https://en.wiktionary.org/wiki/coil)
- [Coil from Wikipedia](https://en.wikipedia.org/wiki/Coil)
- [Coiled coil from Wikipedia](https://en.wikipedia.org/wiki/Coiled_coil)
- [Coiled coil filament from Wikipedia](https://en.wikipedia.org/wiki/Incandescent_light_bulb#Coiled_coil_filament)
- [Coil spring from Wikipedia](https://en.wikipedia.org/wiki/Coil_spring)
- [Electromagnetic coil from Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_coil)
- [Chemical oxygen iodine laser (COIL) from Wikipedia](https://en.wikipedia.org/wiki/Chemical_oxygen_iodine_laser)
- [Coiled bodies from Wikipedia](https://en.wikipedia.org/wiki/Cajal_body)
- [Feverkin](https://www.marmosetmusic.com/artists/feverkin) - [Coiled Corner (feat. Bijou)](https://www.marmosetmusic.com/browse/18451-coiled-corner-feat-bijou), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Slinky Springs to Fame](https://de.wikipedia.org/wiki/Emscherkunst.2010#Slinky_Springs_to_Fame) designed by [Tobias Rehberger](https://en.wikipedia.org/wiki/Tobias_Rehberger), [Rhine–Herne Canal](https://en.wikipedia.org/wiki/Rhine%E2%80%93Herne_Canal), [Gasometer Oberhausen](https://en.wikipedia.org/wiki/Gasometer_Oberhausen) in the background with [Wonders of Nature](https://www.gasometer.de/en/exhibitions/wonders-of-nature) exhibition, [Oberhausen](https://en.wikipedia.org/wiki/Oberhausen), Germany, [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail"), Image by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), March 12, 2017, see also [Image](https://commons.wikimedia.org/wiki/File:Oberhausen_-_Kaisergarten_-_Slinky_30_ies.jpg) by [Frank Vincentz](https://commons.wikimedia.org/wiki/User:Ies/L_Oberhausen), November 29, 2012, [Category:Slinky Springs to Fame](https://commons.wikimedia.org/wiki/Category:Slinky_Springs_to_Fame) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Coiled v.0.5 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68009&start=3) by [Oscar Gavira](index.php?title=Oscar_Gavira&action=edit&redlink=1 "Oscar Gavira (page does not exist)"), [CCC](CCC "CCC"), July 18, 2018
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Update: Coiled-NNUE 0.7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77887&start=5) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), August 06, 2021
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Coiled-NNUE/README.md at master · Oscar-Gavira/Coiled-NNUE · GitHub](https://github.com/Oscar-Gavira/Coiled-NNUE/blob/master/nnue/README.md)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> Based on [Coiled - Técnicas utilizadas](http://www.oscargavira.es/?sec=Coiled_Tecnicas)

**[Up one level](Engines "Engines")**

