---
title: AI Chess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * AI Chess**

**AI Chess**, (A.I. Chess)

a chess program by [Marty Hirsch](Marty_Hirsch "Marty Hirsch") and predecessor of [MChess](MChess "MChess"). AI Chess was written in [8086](8086 "8086") [assembly language](Assembly "Assembly") to ran on an [IBM PC](IBM_PC "IBM PC") under [DOS](MS-DOS "MS-DOS") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. It played the [ACM 1988](ACM_1988 "ACM 1988") in [Orlando](https://en.wikipedia.org/wiki/Orlando%2C_Florida), the [WCCC 1989](WCCC_1989 "WCCC 1989") in [Edmonton](https://en.wikipedia.org/wiki/Edmonton) and the [WMCCC 1989](WMCCC_1989 "WMCCC 1989") in [Portorož](https://en.wikipedia.org/wiki/Portoro%C5%BE) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Description](#description)
- [2 See also](#see-also)
- [3 External Links](#external-links)
- [4 References](#references)

## Description

given in the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-3" href="#cite-ref-3">[3]</a> :

```
A.I. Chess uses a fairly complicated algorithm combining full-width search, [selective search](Selectivity "Selectivity"), and a "layered" [quiescence search](Quiescence_Search "Quiescence Search") which behaves differently at different levels in the search tree. The program performs an [iterative](Iterative_Deepening "Iterative Deepening") full-width search using a modified form of the [Principal-Variation-Search](Principal_Variation_Search "Principal Variation Search") (PVS) algorithm. On top of this, it does a combined selective/quiscence analysis. A.I. Chess has the unusual feature of sometimes re-searching a "[quiscence node](Quiescent_Node "Quiescent Node")" with a full-width investigation.

```

```
The quiescence search incorporates a detailed "threat analysis" and therefore, the program spots may combinations long before a contrasting "[brute force](Brute-Force "Brute-Force")" approach would find them. The gain (from needing less full-width plies) seems to exceed the loss in speed by a significant amount.

```

```
[Position evaluation](Evaluation "Evaluation") starts by considering if the side to move is threatened with [pawn promotion](Promotions "Promotions"), [check](Check "Check"), or [double attack](Double_Attack "Double Attack"), or has [trapped](Trapped_Pieces "Trapped Pieces"), [pinned](Pin "Pin"), or [skewered](Skewer "Skewer") pieces. Penalties similar to swap-off scores are imposed if the position is too deep to merit a re-search. [Scores](Score "Score") are then added for other [tactical patterns](Tactics "Tactics"), pressure on pieces and pawns, development, [King safety](King_Safety "King Safety"), [passed pawns](Passed_Pawn "Passed Pawn"), [pawn structure](Pawn_Structure "Pawn Structure"), [outposts](Outposts "Outposts"), and [mobility](Mobility "Mobility").

```

```
Some types of [endgame positions](Endgame "Endgame") are scored differently, by [pattern recognition](Pattern_Recognition "Pattern Recognition") processing. The program is alert to simplifications, and to tactics involving passed pawns.

```

## See also

- [MChess](MChess "MChess")

## External Links

- [AI Chess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=352)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Monty Newborn](Monroe_Newborn "Monroe Newborn"), [Danny Kopec](Danny_Kopec "Danny Kopec") (**1989**). *Results of The Nineteenth ACM North American Computer Chess Championship*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 32, No. 10, [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_23_C.pdf)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [AI Chess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=352)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)

**[Up one level](Engines "Engines")**

