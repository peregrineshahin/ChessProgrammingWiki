---
title: FCP
---
**[Home](Home "Home") * [Engines](Engines "Engines") * FCP**

**FCP**, (Forth Chess Program)

a chess engine by [Ian Osgood](Ian_Osgood "Ian Osgood"), written as an exercise in learning the [Forth](Forth "Forth") programming language, originally derived from [Tom Kerrigan's](Tom_Kerrigan "Tom Kerrigan") simple chess program [TSCP](TSCP "TSCP") 1.71. At the time it was started, there were no other chess programs in Forth which used modern search techniques. FCP retains the values of small footprint (\< 64K) and code clarity.
Normally, FCP is used from the Forth command line. There are also drivers for working in [XBoard](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and running [EPD](Extended_Position_Description "Extended Position Description") [test suites](Test-Positions "Test-Positions").

## Contents

- [1 Enhancements](#enhancements)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
- [5 References](#references)

## Enhancements

Although FCP started with a nearly identical [evaluation function](Evaluation_Function "Evaluation Function") as an aid to detecting bugs when porting from [C](C "C") to Forth, FCP diverged from TSCP in many ways <a id="cite-note-1" href="#cite-ref-1">[1]</a>:

- [0x88](0x88 "0x88")
- [Piece lists](Piece-Lists "Piece-Lists")
- Track king positions for faster [check](Check "Check") detection
- Procedural [move generation](Move_Generation "Move Generation") with loop unrolling
- [Alpha-beta](Alpha-Beta "Alpha-Beta") with [aspiration windows](Aspiration_Windows "Aspiration Windows")
- Using the open parameter [stack](Stack "Stack") allows only passing [alpha](Alpha "Alpha") to [search](Search "Search") and [quiescence](Quiescence_Search "Quiescence Search") (the alpha from the ancestor node is -beta for this node)
- [Killer heuristic](Killer_Heuristic "Killer Heuristic")
- [Null move pruning](Null_Move_Pruning "Null Move Pruning")
- [Check extensions](Check_Extensions "Check Extensions")
- [Incremental](Incremental_Updates "Incremental Updates") [material](Material "Material") and [pawn evaluation](Pawn_Structure "Pawn Structure")
- [Opening Book](Opening_Book "Opening Book")

## See also

- [Brainless](</Brainless_(Forth)> "Brainless (Forth)") by [David Kühling](David_K%C3%BChling "David Kühling")
- [TSCP](TSCP "TSCP")

## Forum Posts

- [TSCP enhancements (Re: Short chess programs)](https://www.stmintz.com/ccc/index.php?id=252881) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), September 19, 2002
- [Go FORTH and multiply with FCP...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29692) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](CCC "CCC"), September 08, 2007

## [Re: Go FORTH and multiply with FCP...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29692&start=9) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), September 08, 2009 External Links

- [FCP home page](http://www.quirkster.com/iano/forth/FCP.html)
- [Forth application benchmark suite (ZIP)](http://www.complang.tuwien.ac.at/forth/appbench.zip) contains both FCP and another Forth chess program called [Brainless](</Brainless_(Forth)> "Brainless (Forth)") by [David Kühling](David_K%C3%BChling "David Kühling") <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [TSCP enhancements (Re: Short chess programs)](https://www.stmintz.com/ccc/index.php?id=252881) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), September 19, 2002
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [brainless | Free Games software downloads at SourceForge.net](http://sourceforge.net/projects/forth-brainless/)

**[Up one Level](Engines "Engines")**

