---
title: Evaluation of Pieces
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * of Pieces**

This page serves as a quick reference for those who look for ideas about evaluating different kinds of [pieces](Pieces "Pieces").

## Contents

- [1 Pawn](#pawn)
- [2 Knight](#knight)
- [3 Bishop](#bishop)
- [4 Rook](#rook)
- [5 Queen](#queen)
- [6 King](#king)
- [7 See also](#see-also)
- [8 Forum Posts](#forum-posts)
- [9 References](#references)

## Pawn

- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Pawn Center](Pawn_Center "Pawn Center")
- [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")

## penalty for "d" and "e" pawns blocked on their initial squares Knight

- Decreasing value as pawns disappear
- [Outposts](Outposts "Outposts")
- Knight trapped on A8/H8/A7/H7 or A1/H1/A2/H2 - see [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
- Penalty for blocking a C-pawn in closed openings ([Crafty](Crafty "Crafty") defines it as follows: white knight on c3, white pawns on c2 and d4, no white pawn on e4)
- When calculating knight [mobility](Mobility "Mobility"), it is advisable to omit [squares controlled](Square_Control "Square Control") by enemy pawns
- Marginal bonus for a knight defended by a pawn
- Penalty for an undefended minor piece ([Stockfish](Stockfish "Stockfish"))

## Bishop

- [Bad Bishop](Bad_Bishop "Bad Bishop")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Bishop versus Knight](Bishop_versus_Knight "Bishop versus Knight")
- [Color Weakness](Color_Weakness "Color Weakness")
- [Fianchetto](Fianchetto "Fianchetto")
- [Returning Bishop](Returning_Bishop "Returning Bishop")
- Bishop trapped by enemy pawns on A2/H2/A7/H7 or on A3/H3/A6/H6, see [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
- Penalty for an undefended minor piece ([Stockfish](Stockfish "Stockfish"))

## Rook

- Increasing value as pawns disappear
- [Rook on Open File](Rook_on_Open_File "Rook on Open File")
- [Rook on Seventh](Rook_on_Seventh "Rook on Seventh") (possibly also eigth) rank
- [Tarrasch Rule](Tarrasch_Rule "Tarrasch Rule")
- Penalty for a Rook blocked by an uncastled King
- Small bonus for a rook with enemy queen on the same file (doesn't matter if it's open or not)
- Rooks defending each other (Rebel uses a piece/square table for that, making supporeted rook on 7th rank even more valuable)

## Queen

- Penalty for early development <a id="cite-note-1" href="#cite-ref-1">[1]</a>
- Some programs do not evaluate queen [mobility](Mobility "Mobility")
- Some versions of [Fruit](Fruit "Fruit") replace queen mobility by [king tropism](King_Safety#KingTropism "King Safety")
- If [king safety](King_Safety "King Safety") evaluation relies on king tropism, queen tends to get somewhat higher bonus

## King

- [King safety](King_Safety "King Safety") in the [middlegame](Middlegame "Middlegame")
- [King centralization](King_Centralization "King Centralization") in the [endgame](Endgame "Endgame")
- [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
- Penalty for standing on a wing with no pawns present in the endgame
- [Pins](Pin "Pin")/[X-ray](X-ray "X-ray")
- [Castling Rights](Castling_Rights "Castling Rights")

## See also

- [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Square Control](Square_Control "Square Control")

## Forum Posts

- [Knight Evaluation](http://www.talkchess.com/forum/viewtopic.php?t=55453) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), February 24, 2015
- [eval pieces](http://www.talkchess.com/forum/viewtopic.php?t=56690) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), June 15, 2015

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Queen wandering, was: Crafty 14,9](https://www.stmintz.com/ccc/index.php?id=18371) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), May 11, 1998

**[Up one Level](Evaluation "Evaluation")**

