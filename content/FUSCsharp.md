---
title: FUSCsharp
---
**[Home](Home "Home") * [Engines](Engines "Engines") * FUSc#**

**FUSc#**,

was an experimental research [open source chess engine](Category:Open_Source "Category:Open Source") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, developed since 2002 by a AI-Game Programming Group at the [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), headed by [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas").
As the name suggests, FUSc# was written in [C#](C_sharp "C sharp"). Compliant to the [UCI](UCI "UCI") protocol, it was able to play online. FUSc# was subject of research on [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") using [TD-Leaf(λ)](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning"), as elaborated in [Marco Block's](Marco_Block-Berlitz "Marco Block-Berlitz") thesis <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Description](#description)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 External Links](#external-links)
- [5 References](#references)

## Description

## [Board Representation](Board_Representation "Board Representation")

While FUSc# originally had an [0x88 board representation](0x88 "0x88"), it gained some speed up by using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## [Search](Search "Search")

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Iterative Search](Iterative_Search "Iterative Search") (at times) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Selectivity](Selectivity "Selectivity")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

FUSc# classifies [middlegame](Middlegame "Middlegame") positions into 32 types considering king placement (k-wing, q-wing, and center) and whether queens are still on the board - addressing [king safety](King_Safety "King Safety") issues <a id="cite-note-6" href="#cite-ref-6">[6]</a>.
Along with one [endgame](Endgame "Endgame") type - 33 types in total, each type has a vector of 1706 positional coefficients ([point values](Point_Value "Point Value"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure")) associated - in total 56298 coefficients, adapted by [TD-Leaf(λ)](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning"). While a [strength](Playing_Strength "Playing Strength") improvement of more than 350 rating points after 119 training games on a chess server was reported, this classification scheme of 33 distinct evaluation functions may be diminished due to type transitions with possible [evaluation discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity").

## See also

- [KnightCap](KnightCap "KnightCap")

## Publications

- [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz") (**2004**). *Verwendung von Temporale-Differenz-Methoden im Schachmotor FUSc#*. Diplomarbeit, Betreuer: [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/block/Skripte/diplomarbeit.pdf) (German)
- [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), André Rauschenbach, [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)"), Frank Jeschke, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2005**). *Das Schachprojekt FUSc#"*. Technical Report B-05-21, [pdf](http://www.inf.fu-berlin.de/inst/pubs/FuschReport2005.pdf), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin") (German)
- [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)") (**2005**). *Rotated bitboards in FUSc#*. [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/jbuchner/rotated.pdf)
- [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)") (**2005**). *Theory and practical strategies for efficient alpha-beta-searches in computer chess*. Bachelor thesis, Advisor: [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://dynamics.mi.fu-berlin.de/preprints/buchner-bachelor-thesis.pdf)
- [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)

## External Links

- [FUSc# - AG Schachprogrammierung FUSC# april 2005 FUSC# project group](https://slideplayer.com/slide/636086/) (slides)
- [Refubium - Das Schachprojekt FUSc#](https://refubium.fu-berlin.de/handle/fub188/18583?show=full)
- [FuschICS \< Main \< Wiki](http://www.mi.fu-berlin.de/w/Main/FuschICS)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> as of October 2018, source code seems no longer available, the project outdated and abondended
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz") (**2004**). *Verwendung von Temporale-Differenz-Methoden im Schachmotor FUSc#*. Diplomarbeit, Betreuer: [Prof. Dr. Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/block/Skripte/diplomarbeit.pdf) (German)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)") (**2005**). *Rotated bitboards in FUSc#*. [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/jbuchner/rotated.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Search details based on [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)") (**2005**). *Theory and practical strategies for efficient alpha-beta-searches in computer chess*. Bachelor thesis, Advisor: [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://dynamics.mi.fu-berlin.de/preprints/buchner-bachelor-thesis.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> an [iterative](Iterative_Search "Iterative Search") [alpha-beta](Alpha-Beta "Alpha-Beta") matrix version gave a promising performance boost, bought by a huge degree of code complexity, see [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), André Rauschenbach, [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)"), Frank Jeschke, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2005**). *Das Schachprojekt FUSc#"*. Technical Report B-05-21, [pdf](http://dynamics.mi.fu-berlin.de/preprints/buchner-fusch-report.pdf), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin") (German)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)

**[Up one Level](Engines "Engines")**

