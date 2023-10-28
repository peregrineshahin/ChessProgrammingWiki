---
title: Evaluation Overlap
---
**[Home](Home "Home") * [Organizations](Organizations "Organizations") * [ICGA](ICGA "ICGA") * [Investigations](ICGA_Investigations "ICGA Investigations") * Evaluation Overlap**

by [Mark Watkins](Mark_Watkins "Mark Watkins")

Here might be a historical perspective. From page 62 of [Hayes](Jean_Hayes_Michie "Jean Hayes Michie") and [Levy](David_Levy "David Levy"), *World Computer Chess*, Stockholm 1974 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Contents

- [1 Numerical Evaluation of Positions](#numerical-evaluation-of-positions)
  - [1.1 CHAOS](#chaos)
  - [1.2 The Ostrich](#the-ostrich)
  - [1.3 Chess 4.0](#chess-4.0)
  - [1.4 Kaissa](#kaissa)
- [2 Analyse](#analyse)
  - [2.1 Center Control](#center-control)
  - [2.2 Levy Development](#levy-development)
  - [2.3 Queen Bonus](#queen-bonus)
  - [2.4 Rook Bonus](#rook-bonus)
  - [2.5 Bishop Bonus](#bishop-bonus)
  - [2.6 Knight Mobility](#knight-mobility)
  - [2.7 King's mobility](#king.27s-mobility)
  - [2.8 Attack/Defence](#attack.2fdefence)
- [3 Final Definition](#final-definition)
- [4 See also](#see-also)
- [5 References](#references)

## Numerical Evaluation of Positions

In the section devoted to notes on the competing programs, the respective [evaluation](Evaluation "Evaluation") functions for [CHAOS](CHAOS "CHAOS") and [The Ostrich](Ostrich "Ostrich") are discussed in some detail. *CHAOS* uses nineteen features and *The Ostrich* only thirteen, but the latter plans to increase this number in later incarnations. They have approximately eleven features in common: 'approximately', because the concepts are divided differently. The overlap here is not surprising since all scoring functions aim to embody 'reliable' chess heuristics: the weightings may differ, but the features themselves are similar. One of the eleven concepts shared by *CHAOS* and *The Ostrich* is [material](Material "Material"): this is the dominant factor no only in these two programs but also in the majority of chess playing programs. Exceptions are [Freedom](Freedom "Freedom"), which stresses [mobility](Mobility "Mobility"), and [Papa](Papa "Papa"), which concentrates on 'entropy' (basically a mobility measure). Other shared concepts include mobility, control of the centre, [castling](Castling "Castling"), [king safety](King_Safety "King Safety") and assorted terms concerned with [pawn structure](Pawn_Structure "Pawn Structure"): the latter include bonus points for occupancy of the centre, advancement, [passed pawns](Passed_Pawn "Passed Pawn"), a bonus for [doubling opponents' pawns](Doubled_Pawn "Doubled Pawn") with a penalty for doubling one's own, and a penalty for blocking development of one's own pieces. The delicate matter of handling pawn structures has not been mastered satisfactorily by any current program \[...\] For instance, all seem to place disproportionate faith in the concept of doubling the opponent's pawns (see records of games 1 and 4). [CHAOS](CHAOS "CHAOS") also considers the number of threatened pieces, [pins](Pin "Pin") and [discovered checks](Discovered_Check "Discovered Check"), king end-game position, and capturing and mobility *potential*.

*The Ostrich* has an interesting term, concerned with *[tempi](Tempo "Tempo")*, which aims to penalize time-wasting moves such as taking two moves to reach a square that could be reached in one, or repeating a move (see game 24, where the Swiss program [Tell](Tell "Tell") causes a [draw by repetition](Repetitions "Repetitions")). \[...\]

## CHAOS

**4. Evaluation function.** \[...\] Nineteen factors are taken into account, and their weights modified according to the stage reached in the game.

- Threatened pieces, the sum of the value of all pieces which have enemy pieces bearing down on them, but not necessarily *en prise*.
- Capturing potential, an 'adjusted' sum of the value of capturing potentials on all squares on the board.
- Mobility, defined as the number of legal moves.
- Centre control, which covers both occupancy and attack on centre squares and reduces in importance as the game progresses.
- Pins and discovered checks.
- Material, which contributes the greatest amount to the evaluation. Values are the conventional ones with no values assigned for the king.
- Queen development, a penalty for developing early.
- Double threats and captures. Double threats carry the value of the second most valuable piece able to be captured by the moving side, on the grounds that if two pieces can be attacked, the lower valued one will be captured. Captures represent the total value of piece more strongly attacked than defended. This is also an 'adjusted' value which attempts to approximate the net value to the side moving, after an exchange has taken place.
- Attacked pieces, the total number of pieces attacked more strongly than defended.
- Rook usage, which rewards castling, doubling of rooks, occupation of open files, and rooks behind passed pawns.
- Mobility potential, a measurement of the legal moves as well as the 'not quite legal' moves (e.g. moves which guard, or would have been legal if out of check, or which bear through and along the line of attack of another piece, etc.). This carries less weight than mobility proper.
- Pawn usage, which includes pawn advancement, totally or partially unblocked pawns, connectedness, doubled pawns, etc.
- King endgame position. There are rewards for forcing the enemy king to the edge, stopping an opposing unblocked pawn, staying with the 'square' of the opponent's passed pawn, and king opposition, etc.
- Development. The early development of minor pieces is encouraged.
- Queen pins, which counts pieces pinned against the queen as well as discovered attacks on the queen.
- Attack on king. There is a reward for attacking close to the opponent's king.
- Best capture, the value of the highest valued piece left *en prise* after a move.
- King safety. There are incentives for attacking close to one's own king.

The evaluation function has been based as far as possible on general principles, avoiding special cases. For testing purposes the weights of these factors were set differently for each side while the program played against itself. This yielded valuable information about best settings.

## The Ostrich

**The static evaluation function.** This consists of thirteen subroutines each corresponding to a basic chess heuristic:

- Material. The subroutine which computes the difference between White's and Black's material the greatest single value to the overall scoring function. The pieces have their conventional values.
- Material ratio term, which computes whether an even exchange of material has occurred between the top node of the tree and the bottom position being evaluated; a bonus goes to the side ahead in material.
- Castling.
- Board control, which is intended to increase one's own mobility and restrict one's opponent's. There is a small bonus for each square controlled, centre squares and squares near the enemy king have the greatest score. 'Control' is defined as the ability of the piece in question to capture a hypothetical enemy piece on that square.
- Tempi. Moving the same piece twice in the opening, moving a king or rook before castling, moving a piece back to its immediately previous position and moving to a square in two moves when it could be done in one, all attract penalties.
- Early queen moves. These attract a penalty before the eighth move of the game; by which time most minor pieces are developed and the king has castled.
- Blocking central pawns. 'Clogging' a position is penalised.
- Development of pieces. Rapid development is encouraged by giving a penalty to unmoved minor pieces or central pawns.
- Central pawns. These carry a bonus
- Pawn structure. Advancement of pawns is encouraged and doubled pawns penalised.
- King safety. To guard against king-side pressure on the part of the opponent the program encourages its own pieces in its own king-sector.
- Passed pawns. The goal is to encourage the advancement and queening of pawns along with trading off the opponent's passed pawns before they become too advanced. A passed pawn receives credit according to its advancement.

## Chess 4.0

\[...\] In addition to material score in [Chess](</Chess_(Program)> "Chess (Program)"), terms are added which express in a primitive way, notions of mobility (number of squares attacked), pawn structure (passed, [isolated](Isolated_Pawn "Isolated Pawn"), doubled, [backward](Backward_Pawn "Backward Pawn"), etc.), piece placement (e.g. [rooks on seventh rank](Rook_on_Seventh "Rook on Seventh")), and king safety (king in castled position, adequate pawn cover). \[...\]

## Kaissa

One of the papers which is available ([Adelson-Velskii](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") *et al*. 1970 <a id="cite-note-2" href="#cite-ref-2">[2]</a>) describes the program as it was in the late 1960s and from the evidence available it is likely that [Kaissa](Kaissa "Kaissa") has many of the same features.
\[...\]
This paper has notes on the evaluation function; the present function is likely to be similar, if not identical. Bonus points are given for:

- 'A phalanx', i.e. two pawns side by side, on ranks 4-7 for White, and ranks 5-2 for Black. Three pawns side by side count as two phalanxes.
- Centre pawns.
- Pawn attack on the centre.
- Passed pawns.
- 'Scope', which is the calculation of the influence that each piece exerts on all squares, occupied or unoccupied by either own or enemy pieces.
- Attack on undefended pieces and pawns on squares adjacent to the king.
- Attack by a minor piece on a 'hole' (weak square). A hole is defined as a square, on \[ranks\] 1-5 for white and 8-4 for black, under attack by an enemy pawn, undefended by own pawn and with no chance of defence even after pawn advance.
- Minor pieces standing in an opponent's hole.
- Knights in the centre.
- Rook on an open file, or threatening an open file.
- Castling.

Penalties are incurred by

- A hole.
- A weak pawn (one behind a hole).
- Isolated pawns.
- Doubled pawns.
- Pawns which are isolated and doubled.
- Forfeiture of castling.
- Opponent's castling.

## Analyse

Another thing to discuss could be Chapter 6 of [Hartmann's](Dap_Hartmann "Dap Hartmann") *Notions of Evaluation Functions tested against Grandmaster Games* in *[Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")* (1989) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

Here is a brief synopsis. First there are three notions of mobility: Legal Moves, Pseudo Moves, and de Groot Moves. These should be self-explanatory.

## Center Control

With B as a bonus for a given square, this is B\*\[AT+2\*OC\] where AT is #attackers and OC is #occupants.

## Levy Development

This is a rather complicated construct, that doesn't seem of much direct relevant here.

## Queen Bonus

CHESS 4.5 uses 0.8\*AT-0.8\*DI where AT is #squares attacked that are not attacked by enemy pawns or minor,
and DI is the minimum of the rank/file differences to the enemy king. ANALYSE rescaled this to AT-DI (so as to make everything integral).

## Rook Bonus

*Chess 4.5* used 1.6\*AT-1.6\*DI+8\*DR+8\*op+3\*SO+22\*SR where AT is #squares attacked, DI as above, DR is #rooks in file or rank w/o intervening pieces, SR is #rooks on 7th rank, OP is #rooks on open files, SO is #rooks on semi-open file (defined as File in which there is no \[own\] Pawn, and at least one enemy Pawn that is no defended by a Pawn and that cannot move one single square w/o being attacked by a Pawn). ANALYSE rescaled to make it integral.

## Bishop Bonus

[Jaap Herman](index.php?title=Jaap_Herman&action=edit&redlink=1 "Jaap Herman (page does not exist)") helped with this, as PS+EM+OM+DL+OB+OW, where PS #pseudomoves, EM is sum of enemy material on diagonals of the Bishop (unclear if it includes x-rays, even for blocked pawns?) where P=0,NB=3,R=5,Q=9,K=10, OM is sum of own material forwards on diagonal of the Bishop, P=0,NB=3,R=5,Q=9,K=0, DL is length of diagonals \[#pseudomoves on empty board\] minus 7, OB is pawn obstruction of enemy pawns (-25,-15,-10,-5,+1 according to specific characteristics), OW is own pawns, every pawn on diagonal in front of bishop is -5 if rank \< 4 and +1 otherwise, and every pawn on diagonal behind the bishop is +1.

## Knight Mobility

Hartmann discusses having this, and then points out that it doesn't seem to contribute one way or the other, so he concludes "It is therefore no use to have a separate mobility component for the knight, detached from the Pseudo Mobility."

## King's mobility

Again Hartmann points out that this might be useless, but it seems OK in the endgame.

## Attack/Defence

- Different Attacked Squares: A number from 3 to 64 for each side.
- Attacked Own Squares: Only count those squares on ranks 1-4.
- Attacked Opponent Squares: Only count squares on ranks 5-8.

## Final Definition

```

MAT+PS+DIF+0.5*CEN+LD+2*RB+QB+2*BB+0.5*DEF+OFF

```

MAT is material, PS is #pseudo-legal moves, DIF is #different attacked squares, CEN is centre control, LD is Levy development, RB is rook bonus, QB is queen bonus, BB is bishop bonus, DEF is #attacked own squares, OFF is #attacked opp squares.

## See also

- [Quantifying Evaluation Features](Quantifying_Evaluation_Features "Quantifying Evaluation Features")
- [Rybka Controversy](Rybka_Controversy "Rybka Controversy")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jean E. Hayes](Jean_Hayes_Michie "Jean Hayes Michie"), [David Levy](David_Levy "David Levy") (**1976**). *[The world computer chess championship, Stockholm 1974](http://www.getcited.org/pub/101724802)*. University Press (Edinburgh) ISBN 0852242859
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Alexander Bitman](Alexander_Bitman "Alexander Bitman"), [Alexander Zhivotovsky](Alexander_Zhivotovsky "Alexander Zhivotovsky") and [Anatoly Uskov](Anatoly_Uskov "Anatoly Uskov") (**1970**). *Programming a Computer to Play Chess*. Russian Mathematical Surveys, Vol. 25, pp. 221-262
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1989**). *Notions of Evaluation Functions Tested against Grandmaster Games*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")

**[Up one level](ICGA_Investigations "ICGA Investigations")**

