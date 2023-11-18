---
title: Diablo
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Diablo**

\[ [Diablo Cojuelo](https://en.wikipedia.org/wiki/Dominican_Carnival_%28Dominican_Republic%29#Characters) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Diablo**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Marcus Prewarski](Marcus_Prewarski "Marcus Prewarski"), written in [C](C "C"),
distributed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), first released in 2005, latest version Diablo 0.5.1 released in October 2006, with [Jim Ablett](Jim_Ablett "Jim Ablett") compiles available <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Description

## Board Representation

Diablo is a [0x88](0x88 "0x88") engine with [piece-lists](Piece-Lists "Piece-Lists") to determe [vector attacks](Vector_Attacks "Vector Attacks") by 0x88 square difference.
It performs [pseudo-legal move generation](Move_Generation#PseudoLegal "Move Generation") and keeps an [attack table](Attack_and_Defend_Maps "Attack and Defend Maps") per [ply](Ply "Ply") - initialized once per [node](Node "Node") during [evaluation](Evaluation "Evaluation"), which later speeds up [in check](Check "Check") detection and [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") by [lookup](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps").

## Search

The [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") inside the [fractional ply](Depth#FractionalPlies "Depth") [iterative deepening](Iterative_Deepening "Iterative Deepening") framework without [aspiration](Aspiration_Windows "Aspiration Windows").
The [depth-preferred](Transposition_Table#ReplacementStrategies "Transposition Table") [transposition table](Transposition_Table "Transposition Table") based on [Zobrist hashing](Zobrist_Hashing "Zobrist Hashing") is used in the main search only. Beside [quiescence](Quiescence_Search "Quiescence Search"), [selectivity](Selectivity "Selectivity") is due to [futility pruning](Futility_Pruning "Futility Pruning") near the tips, [null move pruning](Null_Move_Pruning "Null Move Pruning") combined with [mate threat extensions](Mate_Threat_Extensions "Mate Threat Extensions"), and further [fractional extensions](Extensions#FractionalExtensions "Extensions") for [single replies](One_Reply_Extensions "One Reply Extensions"), [check](Check_Extensions "Check Extensions"), [passed pawn to 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions") and [queening](Promotions "Promotions"). [Move ordering](Move_Ordering "Move Ordering") takes [PV-move](PV-Move "PV-Move"), [MVV/LVA](MVV-LVA "MVV-LVA") plus fast SEE for [captures](Captures "Captures"), two [killers](Killer_Move "Killer Move") and the [history heuristic](History_Heuristic "History Heuristic") into account. [Internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") is applied in case of [PV-nodes](Node_Types#PV-Node "Node Types") if no move was found in the transposition table.

## Evaluation

[Evaluation](Evaluation "Evaluation") considers [material](Material "Material") with [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [bishop pair](Bishop_Pair "Bishop Pair"), [development](Development "Development"), [center control](Center_Control "Center Control"), [mobility](Mobility "Mobility") of bishops and rooks, in particular considering [trapped rooks](Trapped_Pieces "Trapped Pieces"), [rook on open file](Rook_on_Open_File "Rook on Open File") and [on 7th rank](index.php?title=Rook_On_Seventh&action=edit&redlink=1 "Rook On Seventh (page does not exist)"). [Pawn structure](Pawn_Structure "Pawn Structure") evaluation focuses on [passed pawns](Passed_Pawn "Passed Pawn") and further punishes [backward](Backward_Pawn "Backward Pawn") and [doubled pawns](Doubled_Pawn "Doubled Pawn").
[King safety](King_Safety "King Safety") terms pay attention to an exposed king and [pawn shield](King_Safety#PawnShield "King Safety"). Appropriate [scores](Score "Score") are aggregated in [opening](Opening "Opening") and [endgame](Endgame "Endgame") accumulators and finally, if the sum of material is below some late endgame threshold, [tapered](Tapered_Eval "Tapered Eval") by the current [game phase](Game_Phases "Game Phases") aka sum of material.

## See also

- [Chinese Dark Chess program Diablo](Chinese_Dark_Chess "Chinese Dark Chess")
- [DrunkenMaster](DrunkenMaster "DrunkenMaster")
- [Novag Diablo](index.php?title=Novag_Diablo&action=edit&redlink=1 "Novag Diablo (page does not exist)")
- [Satana](Satana "Satana")

## Forum Posts

- [Re: Gauntlets Chispa 4.0.3 Queen 3.02 and Diablo 0.1 - games](https://www.stmintz.com/ccc/index.php?id=417516) by [Marcus Prewarski](Marcus_Prewarski "Marcus Prewarski"), [CCC](CCC "CCC"), March 13, 2005
- [Diablo 0.5.1 x64 version?](http://www.talkchess.com/forum/viewtopic.php?t=34138) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), May 04, 2010

## External Links

## Chess Engine

- [Drunken Master Chess Engine - Diablo](http://www.geocities.ws/prewarski/)
- [Index of /chess/engines/Jim Ablett/DIABLO](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/DIABLO/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Diablo 0.5.1 JA](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Diablo%200.5.1%20JA) in [KCEC](KCEC "KCEC")
- [Diablo 0.5.1](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=Diablo%200.5.1) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [diablo - Wiktionary](https://en.wiktionary.org/wiki/diablo)
- [Diablo from Wikipedia](https://en.wikipedia.org/wiki/Diablo)
- [Diablo from Wikipedia.es](https://es.wikipedia.org/wiki/Diablo) (Spanish)
- [Diablo Cojuelo from Wikipedia.es](https://es.wikipedia.org/wiki/Diablo_Cojuelo) (Spanish)
- [El Diablo from Wikipedia](https://en.wikipedia.org/wiki/El_Diablo)

### Chess Computers

- [Novag Diablo](http://www.chesscomputeruk.com/html/novag_diablo.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")

### Games

- [Diablo (series) from Wikipedia](https://en.wikipedia.org/wiki/Diablo_%28series%29)
- [Diablo (video game) from Wikipedia](https://en.wikipedia.org/wiki/Diablo_%28video_game%29)

### Geography

- [Canyon Diablo (canyon) from Wikipedia](https://en.wikipedia.org/wiki/Canyon_Diablo_%28canyon%29)
- [Canyon Diablo, Arizona from Wikipedia](https://en.wikipedia.org/wiki/Canyon_Diablo,_Arizona)
- [Canyon Diablo (meteorite) from Wikipedia](https://en.wikipedia.org/wiki/Canyon_Diablo_%28meteorite%29)
- [Diablo Lake from Wikipedia](https://en.wikipedia.org/wiki/Diablo_Lake)
- [Diablo Range from Wikipedia](https://en.wikipedia.org/wiki/Diablo_Range)
- [Mount Diablo from Wikipedia](https://en.wikipedia.org/wiki/Mount_Diablo)
- [Puerta del Diablo from Wikipedia.es](http://es.wikipedia.org/wiki/Puerta_del_Diablo)

### Diabolo

- [Diabolo from Wikipedia](https://en.wikipedia.org/wiki/Diabolo)
- [Diabolo (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Diabolo_%28disambiguation%29)

### Music Video

- [Mario Flores Latin Jazz Band](http://mariofloreslatinmusic.com/aboutus.html) - Mambo Diablo, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Diablo Cojuelo](https://commons.wikimedia.org/wiki/File:Cojuelo03.JPG) by DRW2193, February 01, 2011, [Culture of the Dominican Republic - Festivals - Wikipedia](https://en.wikipedia.org/wiki/Culture_of_the_Dominican_Republic#Festivals), [Category: Diablo Cojuelo](http://commons.wikimedia.org/wiki/Category:Diablo_Cojuelo), [Diablo Cojuelo from Wikipedia.es](https://es.wikipedia.org/wiki/Diablo_Cojuelo), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Diablo 0.5.1 JA](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Diablo%200.5.1%20JA) in [KCEC](KCEC "KCEC")

**[Up one Level](Engines "Engines")**

