---
title: Evaluation Function Draft
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * Evaluation Function Draft**

This page is meant to show an example of a relatively simple evaluation function. It is designed specifically for those who have good programming skills but want to get some ideas about chess knowledge required to attain a reasonable playing strength.

## Contents

- [1 Features](#features)
- [2 Prequisites](#prequisites)
- [3 Initialization](#initialization)
  - [3.1 Distance](#distance)
  - [3.2 Others](#others)
- [4 King Safety](#king-safety)
- [5 References](#references)

## Features

Proposed evaluation function should deal with the following issues

- [Material](Material "Material") (together with some scaling and additional clauses)
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- Special case code to deal with the [trapped pieces](Trapped_Pieces "Trapped Pieces")
- Basic knowledge of [pawn structure](Pawn_Structure "Pawn Structure") - [doubled](Doubled_Pawn "Doubled Pawn"), [isolated](Isolated_Pawn "Isolated Pawn"), [backward](Backward_Pawn "Backward Pawn") and [passed pawns](Passed_Pawn "Passed Pawn")
- Something resembling [king safety](King_Safety "King Safety") - [pawn shield](King_Safety#PawnShield "King Safety") and [king tropism](King_Safety#KingTropism "King Safety") results scaled against the strength of opponent's remaining pieces
- basic knowledge about [endgames](Endgame "Endgame") drawn by [insufficient material](Material#InsufficientMaterial "Material")

## Prequisites

Throughout the draft it will be assumed that the program has the following capabilities

- While [making](Make_Move "Make Move") and [unmaking](Unmake_Move "Unmake Move") [moves](Moves "Moves"), it [updates](Incremental_Updates "Incremental Updates") the material score for each side, subdivided to pieces and pawns
- It updates the value derived from the piece-square tables for all pieces except the king in the same manner
- When asked, it can return the position of either king
- When asked, it can return the number of white/black pawns, bishops, knights or rooks
- It possesses a function `int isPiece(int cl, int sq, int pc)`, returning 1 if a piece pc of color cl stands on the square sq and 0 otherwise.

## Initialization

## Distance

When the program is turned on, it must fill the tables with bonuses for [distance](Distance "Distance") between any two squares that will be used for evaluating [king tropism](King_Safety#KingTropism "King Safety"). The following formula is borrowed from the masters thesis by [Adam Kujawski](Adam_Kujawski "Adam Kujawski") <a id="cite-note-1" href="#cite-ref-1">[1]</a> and modified in such a way that all the scores become positive. It assumes that both rows and columns are numbered from 0 to 7 and that we have a function "abs" returning the value without the sign.

```C++

/* initializes the table of distances between squares */
void setDist() {
   int i,j;

   for (i = 0; i < 64; ++i) {
      for (j = 0; j < 64; ++j) {
         dist_bonus[i][j] = 14 - ( abs ( COL(i) - COL(j) )
                                 + abs ( ROW(i) - ROW(j) ) );
      }
   }
}

```

Taking this function as a basis, tropism tables for various piece types will be derived within its body, just after determining the value of dist_bonus\[i\]\[j\].

```C++

   qk_dist[i][j] = (dist_bonus[i][j] * 5) / 2;
   rk_dist[i][j] =  dist_bonus[i][j] / 2;
   nk_dist[i][j] =  dist_bonus[i][j];

```

At the beginning we can assume that bk_dist is equal to rk_dist, but there is a better idea, taking into account the relevance of a [diagonal](Diagonals "Diagonals"). To apply it, we need two tables numbering the diagonals and [anti-diagonals](Anti-Diagonals "Anti-Diagonals").

```C++

int diag_nw[64] = {
   0, 1, 2, 3, 4, 5, 6, 7,
   1, 2, 3, 4, 5, 6, 7, 8,
   2, 3, 4, 5, 6, 7, 8, 9,
   3, 4, 5, 6, 7, 8, 9,10,
   4, 5, 6, 7, 8, 9,10,11,
   5, 6, 7, 8, 9,10,11,12,
   6, 7, 8, 9,10,11,12,13,
   7, 8, 9,10,11,12,13,14
};

int diag_ne[64] = {
   7, 6, 5, 4, 3, 2, 1, 0,
   8, 7, 6, 5, 4, 3, 2, 1,
   9, 8, 7, 6, 5, 4, 3, 2,
  10, 9, 8, 7, 6, 5, 4, 3,
  11,10, 9, 8, 7, 6, 5, 4,
  12,11,10, 9, 8, 7, 6, 5,
  13,12,11,10, 9, 8, 7, 6,
  14,13,12,11,10, 9, 8, 7
};

```

Now we have to incorporate the following code

```C++

int bonus_dia_distance[15] = {5, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
kb_dist [i][j] += bonus_dia_distance[abs(diag_ne[i] - diag_ne[j])];
kb_dist [i][j] += bonus_dia_distance[abs(diag_nw[i] - diag_nw[j])];

```

## Others

At the initialization stage, we also count the value of INITIAL_PIECE_MATERIAL. It will be needed in scaling the king safety values against the remaining enemy material. We want it to be calculated rather than to become a constant because different piece values might be used by the program.

Here You can view the complete proposal of the [initialization routine](Initialization_Routine "Initialization Routine").

## King Safety

Our simple King safety routine works as follows: evaluating each piece we update two variables: tropismToWhiteKing and tropismToBlackKing, feeding them with the values from the distance tables (see initialization for their details). Then the pawn shield value is computed (I'd like it to be 0 for a complete pawn shield, growing negative as defects accumulate). Finally, the following formula is applied:

```C++

whiteKingSafety = ( (whiteKingShield - tropismToWhiteKing) * blackPieceMaterial ) / INITIAL_PIECE_MATERIAL;
blackKingSafety = ( (blackKingShield - tropismToBlackKing) * whitePieceMaterial ) / INITIAL_PIECE_MATERIAL;

```

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Adam Kujawski](Adam_Kujawski "Adam Kujawski") (**1994**). *Programowanie gry w szachy*. Masters thesis, [University of Warsaw](University_of_Warsaw "University of Warsaw"), [pdf](http://mkarasinski.pl/_cms/files/Adam%20Kujawski%20szachy.pdf) (Polish)

**[Up one Level](Evaluation "Evaluation")**

