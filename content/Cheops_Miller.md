---
title: Cheops Miller
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cheops**

[](https://logological.org/cheops) CHEOPS logo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cheops**, (CHEOPS, CHEss OPponent Simulator, Χέοψ)

a didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [Tristan Miller](index.php?title=Tristan_Miller&action=edit&redlink=1 "Tristan Miller (page does not exist)"), written in [C++](Cpp "Cpp"), licensed under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation"), and first released in 1999, version 1.0 in 2003, and version 1.2 in February 2015 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The program uses a [command line interface](CLI "CLI") to interact with the user, and prints simple [text diagrams](Graphics_Programming#ASCIIDiagrams "Graphics Programming") to display the current [position](Chess_Position "Chess Position") during [game play](Chess_Game "Chess Game"). [Moves](Moves "Moves") are printed and [entered](Entering_Moves "Entering Moves") in [pure algebraic coordinate notation](Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation").
[Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó") has produced a build of CHEOPS 1.2 for [Microsoft](Microsoft "Microsoft") [Windows](Windows "Windows"). [Michael Yee](index.php?title=Michael_Yee&action=edit&redlink=1 "Michael Yee (page does not exist)") has produced an [UCI](UCI "UCI") compliant build of CHEOPS 1.1 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Description

Cheops uses a [64-square](8x8_Board "8x8 Board") linear [array](Array "Array") [board representation](Board_Representation "Board Representation") and performs a [legal move generation](Move_Generation#Legal "Move Generation") [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) by looking for [from-squares](Origin_Square "Origin Square") of own [pieces](Pieces "Pieces") traversing the board in [spiral](https://en.wikipedia.org/wiki/Spiral) order from center to the h1-edge, keeping, returning and splicing [std::list](https://en.wikipedia.org/wiki/Sequence_container_%28C%2B%2B%29#List) as local [move list](Move_List "Move List") variables on the stack.
The tree [search](Search "Search") is fixed [depth](Depth "Depth") [alpha–beta](Alpha-Beta "Alpha-Beta") without [quiescence search](Quiescence_Search "Quiescence Search"). The static [evaluation function](Evaluation_Function "Evaluation Function") considers [material](Material "Material"), [mobility](Mobility "Mobility"), [center proximity](Center_Distance "Center Distance"), [king piece tropism](King_Safety#KingTropism "King Safety"), and a few [pawn structure terms](Pawn_Structure "Pawn Structure") such as [isolated](Isolated_Pawn "Isolated Pawn"), [doubled](Doubled_Pawn "Doubled Pawn") and [backward pawns](Backward_Pawn "Backward Pawn") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## See also

- [CXG Sphinx](CXG_Sphinx "CXG Sphinx")
- [CHEOPS](CHEOPS "CHEOPS"), the Chess-Oriented Processing System from the 70s
- [Pharaon](Pharaon "Pharaon")
- [Sfinks](Sfinks "Sfinks")

## Forum Posts

- [CHEOPS 1.2 -- An AI chess engine -- released on 2015-02-01](https://groups.google.com/d/msg/rec.games.chess.computer/PfEqoxFZ-vI/K_66ofncsRQJ) by [Tristan Miller](index.php?title=Tristan_Miller&action=edit&redlink=1 "Tristan Miller (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2015
- [CHEOPS UCI Engine - missing Windows binaries](http://www.talkchess.com/forum/viewtopic.php?t=55803) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), March 27, 2015
- [CHEOPS 1.3 -- An AI chess engine -- released on 2016-12-27](https://groups.google.com/d/msg/rec.games.chess.computer/ZKDUm0nKNzI/O_ovU5OODwAJ) by [Tristan Miller](index.php?title=Tristan_Miller&action=edit&redlink=1 "Tristan Miller (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 28, 2016

## External Links

## Chess Program

- [CHEOPS | Tristan Miller](https://logological.org/cheops)
- [GitHub - logological/cheops: A command-line AI chess engine](https://github.com/logological/cheops)
- [Index of /software/cheops](https://files.nothingisreal.com/software/cheops/)
- [CHEOPS online manual](https://files.nothingisreal.com/software/cheops/cheops.html)

## Misc

- [Khufu from Wikipedia](https://en.wikipedia.org/wiki/Khufu)
- [Great Pyramid of Giza from Wikipedia](https://en.wikipedia.org/wiki/Great_Pyramid_of_Giza)
- [Pyramid Chess, a three dimensional chess variant](https://www.chessvariants.com/d.link/pyramid.html)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [CHEOPS](https://logological.org/cheops) logo by [Jin Wicked](https://jinwicked.com/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [CHEOPS 1.2 -- An AI chess engine -- released on 2015-02-01](https://groups.google.com/d/msg/rec.games.chess.computer/PfEqoxFZ-vI/K_66ofncsRQJ) by [Tristan Miller](index.php?title=Tristan_Miller&action=edit&redlink=1 "Tristan Miller (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2015
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [CHEOPS | Tristan Miller](https://logological.org/cheops)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [CHEOPS | Tristan Miller](https://logological.org/cheops)

**[Up one level](Engines "Engines")**

