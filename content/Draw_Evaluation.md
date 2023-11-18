---
title: Draw Evaluation
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * [Game Phases](Game_Phases "Game Phases") * [Endgame](Endgame "Endgame") * Draw Evaluation**

It is important for the evaluation function to recognize the endgame positions which are likely [drawn](Draw "Draw"), even though one side has a nominal advantage. This page is devoted to listing some of them. More of that kind of knowledge can be found in the [KPK](KPK "KPK") section.

## Obvious Draws

According to the rules of a dead position, Article 5.2 b, when there is no possibility of [checkmate](Checkmate "Checkmate") for either side with any series of legal moves, the position is an immediate draw if

- Both Sides have a bare King
- One Side has a King and a Minor Piece against a bare King
- Both Sides have a King and a Bishop, the Bishops being the same Color

## Simple Heuristics

The bishops of different colors are not counted as an immediate draw, because of the possibility of a helpmate in the corner. Since this is unlikely given even a four ply search, we may introduce another class of drawn positions: those that cannot be claimed, but can be evaluated as draws:

- Two Knights against the bare King <a id="cite-note-1" href="#cite-ref-1">[1]</a>
- Both Sides have a King and a Minor Piece each
- The Weaker Side has a Minor Piece against two Knights
- Two Bishops draw against a Bishop
- Two Minor Pieces against one draw, except when the Stronger Side has a [Bishop Pair](Bishop_Pair "Bishop Pair")

Please note that a knight or even two knights against two bishops are not included here, as it is possible to win this ending.

**Implementation note:** When a program uses heuristics of that kind, it is of utmost importance to be consistent. For example, if KBN vs KB is scored as a draw, the same must be done with KBN vs KBP. A possible idea is to divide a score by a large constant, such as 16 or 32, when the side nominally ahead has the wrong piece combination.

## Complex Heuristics

- If the Stronger Side has a Pawn and a Bishop against the Minor Piece, the Position is almost certainly drawn if the Weaker Side's King occupies a Square on the Path of a Pawn that is inaccessible to the enemy Bishop (The degenerate cases like Trapping the Minor Piece are best left for Search).
- [Queen versus Rook Pawn on 7th](Queen_versus_Pawn#RookPawn7 "Queen versus Pawn") and [Queen versus Bishop Pawn on 7th](Queen_versus_Pawn#BishopPawn7 "Queen versus Pawn")
- [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")

## One-sided Heuristics

There are some heuristics that tells us only that one of the players cannot win the endgame

- A single Minor Piece should not win against any number of Pawns (again, there is a special case of a smothered mate in the corner, but it is Search issue, not to be taken into account by the [evaluation function](Evaluation_Function "Evaluation Function"))

## See also

- [Blockage Detection](Blockage_Detection "Blockage Detection")
- [Contempt Factor](Contempt_Factor "Contempt Factor")
- [Draw](Draw "Draw")
- [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
- [Fortress](Fortress "Fortress")
- [Insufficient Material](Material#InsufficientMaterial "Material")
- [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
- [Repetitions](Repetitions "Repetitions")
- [Stalemate](Stalemate "Stalemate")

## Forum Posts

## 2000 ...

- ["Don't trust draw score" \<=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), August 08, 2001 » [Repetitions](Repetitions "Repetitions"), [Transposition Table](Transposition_Table "Transposition Table"), [Path-Dependency](Path-Dependency "Path-Dependency")
- [Draw recognition by eval problems](https://www.stmintz.com/ccc/index.php?id=193257) by [Rafael B. Andrist](Rafael_B._Andrist "Rafael B. Andrist"), [CCC](CCC "CCC"), October 17, 2001 » [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")
- [When can a game be declared as a draw?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42991) by [Josué Forte](Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 15, 2003

## 2010 ...

- [question on draw evaluation](http://www.talkchess.com/forum/viewtopic.php?t=34673) by liuzy, [CCC](CCC "CCC"), June 03, 2010

[Re: question on draw evaluation](http://www.talkchess.com/forum/viewtopic.php?t=34673&start=8) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), June 07, 2010

- [handling draw by insufficient material](http://www.talkchess.com/forum/viewtopic.php?t=50150) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), November 19, 2013 » [Insufficient Material](Material#InsufficientMaterial "Material")
- [evaluating tablebases draws](http://www.talkchess.com/forum/viewtopic.php?t=50194) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), November 23, 2013 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Discocheck 5.01: Bishop related endgame problems](http://www.talkchess.com/forum/viewtopic.php?t=50223) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), November 25, 2013 » [DiscoCheck](DiscoCheck "DiscoCheck"), [Color of a Square](Color_of_a_Square "Color of a Square"), [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")

## 2015 ...

- [Stockfish eval output](http://www.talkchess.com/forum/viewtopic.php?t=61250) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 27, 2016 » [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn"), [Stockfish](Stockfish "Stockfish")
- [draw endgame scaling](http://www.talkchess.com/forum/viewtopic.php?t=62380) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), December 04, 2016
- [insufficient mating material](http://www.talkchess.com/forum/viewtopic.php?t=64115) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 29, 2017
- [Marcel Duchamp endgame "splits" engines / hash phenomenon](http://www.talkchess.com/forum/viewtopic.php?t=66640) by [Kenneth Regan](Kenneth_W._Regan "Kenneth W. Regan"), [CCC](CCC "CCC"), February 19, 2018 » [Chess Problems, Compositions and Studies](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies"), [Marcel Duchamp](Category:Marcel_Duchamp "Category:Marcel Duchamp"), [Transposition Table](Transposition_Table "Transposition Table")
- [what to do when all depths give the exact same score?](http://www.talkchess.com/forum/viewtopic.php?t=66798) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), March 10, 2018
- [KQKP and the like](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70827) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 25, 2019
- [Why does stockfish randomise draw evaluations?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71707) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), September 01, 2019 » [Stockfish](Stockfish "Stockfish"), [Draw Score](Score#DrawScore "Score"), [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")

## 2020 ...

- [Endgame woes](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73012) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), February 07, 2020
- [OliThink 5.4.0 has been published with an big leap in strength for only 3 lines of code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74203) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 16, 2020 » [OliThink](OliThink "OliThink")
- [Alpha-beta search for drawing endgames](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77497) by Emanuel Torres, [CCC](CCC "CCC"), June 16, 2021 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Graph History Interaction](Graph_History_Interaction "Graph History Interaction"), [Repetitions](Repetitions "Repetitions")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [When can a game be declared as a draw?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42991) by [Josué Forte](Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 15, 2003

**[Up one Level](Endgame "Endgame")**

