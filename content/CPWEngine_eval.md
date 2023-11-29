---
title: CPWEngine eval
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * Eval**

## Description

Using this evaluation function CPW-Engine should be aware of the following principles:

1. develop the pieces
1. castle if possible
1. need some minimal level of assistance to disrupt its own castling position
1. care for doubled, weak and passed pawns
1. know a thing or two about the changes of piece values as pawns dissappear
1. try to attack squares around enemy king

For function definitions, see [CPW-Engine_eval_h](CPW-Engine_eval_h "CPW-Engine eval h")

## Code

```C++

##include "stdafx.h"
##include "0x88_math.h"
##include "eval.h"
##include "transposition.h"

/* adjustements of piece value based on the number of own pawns */
int knight_adj[9] = { -20, -16, -12, -8, -4,  0,  4,  8, 12 };
int rook_adj[9] = { 15,  12,   9,  6,  3,  0, -3, -6, -9 };

static const int SafetyTable[100] = {
  0,  0,   1,   2,   3,   5,   7,   9,  12,  15,
  18,  22,  26,  30,  35,  39,  44,  50,  56,  62,
  68,  75,  82,  85,  89,  97, 105, 113, 122, 131,
  140, 150, 169, 180, 191, 202, 213, 225, 237, 248,
  260, 272, 283, 295, 307, 319, 330, 342, 354, 366,
  377, 389, 401, 412, 424, 436, 448, 459, 471, 483,
  494, 500, 500, 500, 500, 500, 500, 500, 500, 500,
  500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
  500, 500, 500, 500, 500, 500, 500, 500, 500, 500,
  500, 500, 500, 500, 500, 500, 500, 500, 500, 500
};

/*******************************************************************
*  This struct holds data about certain aspects of evaluation,     *
*  which allows program to print them if desired.                  *
*******************************************************************/

struct eval_vector {
  int gamePhase;
  int mgMob[2];
  int egMob[2];
  int attCnt[2];
  int attWeight[2];
  int kingShield[2];
  int MaterialAdjustement[2];
  int Blockages[2];
  int PositionalThemes[2];
} v;

int eval(int alpha, int beta, int use_hash) {
  int result = 0, mgScore = 0, egScore = 0;
  int stronger, weaker;

  /***********************************************************
  /  Probe the evaluatinon hashtable, unless we call eval()  /
  /  only in order to display detailed result                /
  ***********************************************************/

  int probeval = tteval_probe();
  if (probeval != INVALID && use_hash)
    return probeval;

  /***********************************************************
  /  Clear all eval data                                     /
  ***********************************************************/

  v.gamePhase = 0;
  v.mgMob[WHITE] = 0;      v.mgMob[BLACK] = 0;
  v.egMob[WHITE] = 0;      v.egMob[BLACK] = 0;
  v.attCnt[WHITE] = 0;     v.attCnt[BLACK] = 0;
  v.attWeight[WHITE] = 0;  v.attWeight[BLACK] = 0;
  v.MaterialAdjustement[WHITE] = 0; v.MaterialAdjustement[BLACK] = 0;
  v.Blockages[WHITE] = 0; v.Blockages[BLACK] = 0;
  v.PositionalThemes[WHITE] = 0; v.PositionalThemes[BLACK] = 0;
  v.kingShield[WHITE] = 0; v.kingShield[BLACK] = 0;

  /* sum the incrementally counted material and pcsq values */
  mgScore = b.PieceMaterial[WHITE] + b.PawnMaterial[WHITE] + b.PcsqMg[WHITE]
    - b.PieceMaterial[BLACK] - b.PawnMaterial[BLACK] - b.PcsqMg[BLACK];
  egScore = b.PieceMaterial[WHITE] + b.PawnMaterial[WHITE] + b.PcsqEg[WHITE]
    - b.PieceMaterial[BLACK] - b.PawnMaterial[BLACK] - b.PcsqEg[BLACK];

  /* add king's pawn shield score and evaluate part of piece blockage score
  (the rest of the latter will be done via piece eval) */
  v.kingShield[WHITE] = wKingShield();
  v.kingShield[BLACK] = bKingShield();
  blockedPieces();
  mgScore += (v.kingShield[WHITE] - v.kingShield[BLACK]);

  /* tempo bonus */
  if (b.stm == WHITE) result += e.TEMPO;
  else                  result -= e.TEMPO;

  /*******************************************************************
  * Adjusting material value for the various combinations of pieces. *
  * Currently it scores bishop, knight and rook pairs. The first one *
  * gets a bonus, the latter two - a penalty. Please also note that  *
  * adjustements of knight and rook value based on the number of own *
  * pawns on the board are done within the piece-specific routines.  *
  *******************************************************************/

  if (b.PieceCount[WHITE][BISHOP] > 1) result += e.BISHOP_PAIR;
  if (b.PieceCount[BLACK][BISHOP] > 1) result -= e.BISHOP_PAIR;
  if (b.PieceCount[WHITE][KNIGHT] > 1) result -= e.P_KNIGHT_PAIR;
  if (b.PieceCount[BLACK][KNIGHT] > 1) result += e.P_KNIGHT_PAIR;
  if (b.PieceCount[WHITE][ROOK] > 1) result -= e.P_ROOK_PAIR;
  if (b.PieceCount[BLACK][ROOK] > 1) result += e.P_ROOK_PAIR;

  result += getPawnScore();

  /*******************************************************************
  *  Evaluate pieces                                                 *
  *******************************************************************/

  for (U8 row = 0; row < 8; row++)
    for (U8 col = 0; col < 8; col++) {

      S8 sq = SET_SQ(row, col);

      if (b.color[sq] != COLOR_EMPTY) {
        switch (b.pieces[sq]) {
        case PAWN: // pawns are evaluated separately
          break;
        case KNIGHT:
          EvalKnight(sq, b.color[sq]);
          break;
        case BISHOP:
          EvalBishop(sq, b.color[sq]);
          break;
        case ROOK:
          EvalRook(sq, b.color[sq]);
          break;
        case QUEEN:
          EvalQueen(sq, b.color[sq]);
          break;
        case KING:
          break;
        }
      }
    }

  /********************************************************************
  *  Merge midgame and endgame score. We interpolate between these    *
  *  two values, using a gamePhase value, based on remaining piece    *
  *  material on both sides. With less pieces, endgame score beco-    *
  *  mes more influential.                                            *
  ********************************************************************/

  mgScore += (v.mgMob[WHITE] - v.mgMob[BLACK]);
  egScore += (v.egMob[WHITE] - v.egMob[BLACK]);
  if (v.gamePhase > 24) v.gamePhase = 24;
  int mgWeight = v.gamePhase;
  int egWeight = 24 - mgWeight;
  result += ((mgScore * mgWeight) + (egScore * egWeight)) / 24;

  /********************************************************************
  *  Add phase-independent score components.                          *
  ********************************************************************/

  result += (v.Blockages[WHITE] - v.Blockages[BLACK]);
  result += (v.PositionalThemes[WHITE] - v.PositionalThemes[BLACK]);
  result += (v.MaterialAdjustement[WHITE] - v.MaterialAdjustement[BLACK]);

  /********************************************************************
  *  Merge king attack score. We don't apply this value if there are *
  *  less than two attackers or if the attacker has no queen.        *
  *******************************************************************/

  if (v.attCnt[WHITE] < 2 || b.PieceCount[WHITE][QUEEN] == 0) v.attWeight[WHITE] = 0;
  if (v.attCnt[BLACK] < 2 || b.PieceCount[BLACK][QUEEN] == 0) v.attWeight[BLACK] = 0;
  result += SafetyTable[v.attWeight[WHITE]];
  result -= SafetyTable[v.attWeight[BLACK]];

  /********************************************************************
  *  Low material correction - guarding against an illusory material  *
  *  advantage. Full blown program should have more such rules,  but  *
  *  the current set ought to be useful enough. Please note that our  *
  *  code  assumes different material values for bishop and  knight.  *
  *                                                                   *
  *  - a single minor piece cannot win                                *
  *  - two knights cannot checkmate bare king                         *
  *  - bare rook vs minor piece is drawish                            *
  *  - rook and minor vs rook is drawish                              *
  ********************************************************************/

  if (result > 0) { stronger = WHITE; weaker = BLACK; }
  else { stronger = BLACK; weaker = WHITE; }

  if (b.PawnMaterial[stronger] == 0) {

    if (b.PieceMaterial[stronger] < 400) return 0;

    if (b.PawnMaterial[weaker] == 0
      && (b.PieceMaterial[stronger] == 2 * e.PIECE_VALUE[KNIGHT]))
      return 0;

    if (b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK]
      && b.PieceMaterial[weaker] == e.PIECE_VALUE[BISHOP]) result /= 2;

    if (b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK]
      && b.PieceMaterial[weaker] == e.PIECE_VALUE[KNIGHT]) result /= 2;

    if (b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK] + e.PIECE_VALUE[BISHOP]
      && b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK]) result /= 2;

    if (b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK] + e.PIECE_VALUE[KNIGHT]
      && b.PieceMaterial[stronger] == e.PIECE_VALUE[ROOK]) result /= 2;
  }

  /*******************************************************************
  *  Finally return the score relative to the side to move.          *
  *******************************************************************/

  if (b.stm == BLACK) result = -result;

  tteval_save(result);

  return result;
}

void EvalKnight(S8 sq, S8 side) {
  int att = 0;
  int mob = 0;
  int pos;
  v.gamePhase += 1;

  if (side == WHITE) {
    switch (sq) {
    case A8: if (isPiece(BLACK, PAWN, A7) || isPiece(BLACK, PAWN, C7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A8; break;
    case H8: if (isPiece(BLACK, PAWN, H7) || isPiece(BLACK, PAWN, F7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A8; break;
    case A7: if (isPiece(BLACK, PAWN, A6) && isPiece(BLACK, PAWN, B7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A7; break;
    case H7: if (isPiece(BLACK, PAWN, H6) && isPiece(BLACK, PAWN, G7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A7; break;
    case C3: if (isPiece(WHITE, PAWN, C2) && isPiece(WHITE, PAWN, D4) && !isPiece(WHITE, PAWN, E4)) v.Blockages[WHITE] -= e.P_C3_KNIGHT; break;
    }
  }
  else
  {
    switch (sq) {
    case A1: if (isPiece(WHITE, PAWN, A2) || isPiece(WHITE, PAWN, C2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A8; break;
    case H1: if (isPiece(WHITE, PAWN, H2) || isPiece(WHITE, PAWN, F2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A8; break;
    case A2: if (isPiece(WHITE, PAWN, A3) && isPiece(WHITE, PAWN, B2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A7; break;
    case H2: if (isPiece(WHITE, PAWN, H3) && isPiece(WHITE, PAWN, G2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A7; break;
    case C6: if (isPiece(BLACK, PAWN, C7) && isPiece(BLACK, PAWN, D5) && !isPiece(BLACK, PAWN, E5)) v.Blockages[BLACK] -= e.P_C3_KNIGHT; break;
    }
  }

  /***************************************************************
  *  Material value adjustement based on the no. of own pawns.   *
  *  Knights lose value as pawns disappear.                      *
  ***************************************************************/

  v.MaterialAdjustement[side] += knight_adj[b.PieceCount[side][PAWN]];

  /****************************************************************
  *  Collect data about mobility and king attacks. This resembles *
  *  move generation code, except that we are just incrementing   *
  *  the counters instead of adding actual moves.                 *
  ****************************************************************/

  for (U8 dir = 0; dir<8; dir++) {
    pos = sq + vector[KNIGHT][dir];
    if (IS_SQ(pos) && b.color[pos] != side) {
      ++mob;
      if (e.sqNearK[!side][b.KingLoc[!side]][pos])
        ++att; // this knight is attacking zone around enemy king
    }
  }

  /****************************************************************
  *  Evaluate mobility. We try to do it in such a way             *
  *  that  zero represents average mobility, but  our             *
  *  formula of doing so is a puer guess.                         *
  ****************************************************************/

  v.mgMob[side] += 4 * (mob - 4);
  v.egMob[side] += 4 * (mob - 4);

  /****************************************************************
  *  Save data about king attacks                                 *
  ****************************************************************/

  if (att) {
    v.attCnt[side]++;
    v.attWeight[side] += 2 * att;
  }
}

void EvalBishop(S8 sq, S8 side) {
  int att = 0;
  int mob = 0;
  v.gamePhase += 1;

  if (side == WHITE) {
    switch (sq) {
    case A7: if (isPiece(BLACK, PAWN, B6)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A7; break;
    case H7: if (isPiece(BLACK, PAWN, G6)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A7; break;
    case B8: if (isPiece(BLACK, PAWN, C7)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A7; break;
    case G8: if (isPiece(BLACK, PAWN, F7)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A7; break;
    case A6: if (isPiece(BLACK, PAWN, B5)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A6; break;
    case H6: if (isPiece(BLACK, PAWN, G5)) v.Blockages[WHITE] -= e.P_BISHOP_TRAPPED_A6; break;
    case F1: if (isPiece(WHITE, KING, G1)) v.PositionalThemes[WHITE] += e.RETURNING_BISHOP; break;
    case C1: if (isPiece(WHITE, KING, B1)) v.PositionalThemes[WHITE] += e.RETURNING_BISHOP; break;
    }
  }
  else {
    switch (sq) {
    case A2: if (isPiece(WHITE, PAWN, B3)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A7; break;
    case H2: if (isPiece(WHITE, PAWN, G3)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A7; break;
    case B1: if (isPiece(WHITE, PAWN, C2)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A7; break;
    case G1: if (isPiece(WHITE, PAWN, F2)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A7; break;
    case A3: if (isPiece(WHITE, PAWN, B4)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A6; break;
    case H3: if (isPiece(WHITE, PAWN, G4)) v.Blockages[BLACK] -= e.P_BISHOP_TRAPPED_A6; break;
    case F8: if (isPiece(BLACK, KING, G8)) v.PositionalThemes[BLACK] += e.RETURNING_BISHOP; break;
    case C8: if (isPiece(BLACK, KING, B8)) v.PositionalThemes[BLACK] += e.RETURNING_BISHOP; break;
    }
  }

  /****************************************************************
  *  Collect data about mobility and king attacks                 *
  ****************************************************************/

  for (char dir = 0; dir<vectors[BISHOP]; dir++) {

    for (char pos = sq;;) {

      pos = pos + vector[BISHOP][dir];
      if (!IS_SQ(pos)) break;

      if (b.pieces[pos] == PIECE_EMPTY) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
      }
      else if (b.color[pos] != side) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
        break;
      }
      else {
        break;
      }

    }
  }

  v.mgMob[side] += 3 * (mob - 7);
  v.egMob[side] += 3 * (mob - 7);

  if (att) {
    v.attCnt[side]++;
    v.attWeight[side] += 2 * att;
  }


}

void EvalRook(S8 sq, S8 side) {
  int att = 0;
  int mob = 0;
  int ownBlockingPawns = 0;
  int oppBlockingPawns = 0;
  int stepFwd;
  int nextSq;

  v.gamePhase += 2;

  /***************************************************************
  *  Material value adjustement based on the no. of own pawns.   *
  *  Rooks gain value as pawns disappear.                        *
  ***************************************************************/

  v.MaterialAdjustement[side] += rook_adj[b.PieceCount[side][PAWN]];

  /***************************************************************
  *  This is an ugly hack to detect open files. Merging it with  *
  *  mobility  eval would have been better, but less  readable,  *
  *  and this is educational program fter all.                   *
  /**************************************************************/

  if (side == WHITE) stepFwd = NORTH; else stepFwd = SOUTH;
  nextSq = sq + stepFwd;

  while (IS_SQ(nextSq)) {
    if (b.pieces[nextSq] == PAWN) {
      if (b.color[nextSq] == side) {
        ownBlockingPawns++;
        break;
      }
      else
        oppBlockingPawns++;
    }
    nextSq += stepFwd;
  }

  /****************************************************************
  *  Evaluate open and half-open files. We merge this bonus with  *
  *  mobility  score.                                             *
  /***************************************************************/

  if (!ownBlockingPawns) {

    if (!oppBlockingPawns) {
      v.mgMob[side] += e.ROOK_OPEN;
      v.egMob[side] += e.ROOK_OPEN;
    }
    else {
      v.mgMob[side] += e.ROOK_HALF;
      v.egMob[side] += e.ROOK_HALF;
    }
  }

  /****************************************************************
  *  Collect data about mobility and king attacks                 *
  ****************************************************************/

  for (char dir = 0; dir<vectors[ROOK]; dir++) {

    for (char pos = sq;;) {

      pos = pos + vector[ROOK][dir];
      if (!IS_SQ(pos)) break;

      if (b.pieces[pos] == PIECE_EMPTY) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
      }
      else if (b.color[pos] != side) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
        break;
      }
      else {
        break;
      }

    }
  }

  v.mgMob[side] += 2 * (mob - 7);
  v.egMob[side] += 4 * (mob - 7);

  if (att) {
    v.attCnt[side]++;
    v.attWeight[side] += 3 * att;
  }

}

void EvalQueen(S8 sq, S8 side) {
  v.gamePhase += 4;
  int att = 0;
  int mob = 0;

  /****************************************************************
  *  A queen should not be developed too early                    *
  ****************************************************************/

  if (side == WHITE && ROW(sq) > ROW_2) {
    if (isPiece(WHITE, KNIGHT, B1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, BISHOP, C1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, BISHOP, F1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, KNIGHT, G1)) v.PositionalThemes[WHITE] -= 2;
  }

  if (side == BLACK && ROW(sq) < ROW_7) {
    if (isPiece(BLACK, KNIGHT, B8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, BISHOP, C8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, BISHOP, F8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, KNIGHT, G8)) v.PositionalThemes[BLACK] -= 2;
  }

  /****************************************************************
  *  Collect data about mobility and king attacks                 *
  ****************************************************************/

  for (char dir = 0; dir<vectors[QUEEN]; dir++) {

    for (char pos = sq;;) {

      pos = pos + vector[QUEEN][dir];
      if (!IS_SQ(pos)) break;

      if (b.pieces[pos] == PIECE_EMPTY) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
      }
      else if (b.color[pos] != side) {
        mob++;
        if (e.sqNearK[!side][b.KingLoc[!side]][pos]) ++att;
        break;
      }
      else {
        break;
      }

    }
  }

  v.mgMob[side] += 1 * (mob - 14);
  v.egMob[side] += 2 * (mob - 14);

  if (att) {
    v.attCnt[side]++;
    v.attWeight[side] += 4 * att;
  }

}

int wKingShield() {

  int result = 0;

  /* king on the kingside */
  if (COL(b.KingLoc[WHITE]) > COL_E) {

    if (isPiece(WHITE, PAWN, F2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, F3))  result += e.SHIELD_2;

    if (isPiece(WHITE, PAWN, G2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, G3))  result += e.SHIELD_2;

    if (isPiece(WHITE, PAWN, H2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, H3))  result += e.SHIELD_2;
  }

  /* king on the queenside */
  else if (COL(b.KingLoc[WHITE]) < COL_D) {

    if (isPiece(WHITE, PAWN, A2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, A3))  result += e.SHIELD_2;

    if (isPiece(WHITE, PAWN, B2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, B3))  result += e.SHIELD_2;

    if (isPiece(WHITE, PAWN, C2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, C3))  result += e.SHIELD_2;
  }

  return result;
}

int bKingShield() {
  int result = 0;

  /* king on the kingside */
  if (COL(b.KingLoc[BLACK]) > COL_E) {
    if (isPiece(BLACK, PAWN, F7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, F6))  result += e.SHIELD_2;

    if (isPiece(BLACK, PAWN, G7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, G6))  result += e.SHIELD_2;

    if (isPiece(BLACK, PAWN, H7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, H6))  result += e.SHIELD_2;
  }

  /* king on the queenside */
  else if (COL(b.KingLoc[BLACK]) < COL_D) {
    if (isPiece(BLACK, PAWN, A7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, A6))  result += e.SHIELD_2;

    if (isPiece(BLACK, PAWN, B7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, B6))  result += e.SHIELD_2;

    if (isPiece(BLACK, PAWN, C7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, C6))  result += e.SHIELD_2;
  }
  return result;
}

/******************************************************************************
*                            Pawn structure evaluaton                         *
******************************************************************************/

int getPawnScore() {
  int result;

  /**************************************************************************
  *  This function wraps hashing mechanism around evalPawnStructure().      *
  *  Please note  that since we use the pawn hashtable, evalPawnStructure() *
  *  must not take into account the piece position.  In a more elaborate    *
  *  program, pawn hashtable would contain only the characteristics of pawn *
  *  structure,  and scoring them in conjunction with the piece position    *
  *  would have been done elsewhere.                                        *
  **************************************************************************/

  int probeval = ttpawn_probe();
  if (probeval != INVALID)
    return probeval;

  result = evalPawnStructure();

  ttpawn_save(result);

  return result;
}

int evalPawnStructure() {
  int result = 0;

  for (U8 row = 0; row < 8; row++)
    for (U8 col = 0; col < 8; col++) {

      S8 sq = SET_SQ(row, col);

      if (b.pieces[sq] == PAWN) {
        if (b.color[sq] == WHITE) result += EvalPawn(sq, WHITE);
        else                      result -= EvalPawn(sq, BLACK);
      }
    }

  return result;
}

int EvalPawn(S8 sq, S8 side) {
  int result = 0;
  int flagIsPassed = 1; // we will be trying to disprove that
  int flagIsWeak = 1;   // we will be trying to disprove that
  int flagIsOpposed = 0;

  int stepFwd, stepBck;
  if (side == WHITE) stepFwd = NORTH; else stepFwd = SOUTH;
  if (side == WHITE) stepBck = SOUTH; else stepBck = NORTH;
  S8 nextSq = sq + stepFwd;

  /*************************************************************************
  *   We have only very basic data structures that do not update informa-  *
  *   tion about pawns incrementally, so we have to calculate everything   *
  *   here.  The loop below detects doubled pawns, passed pawns and sets   *
  *   a flag on finding that our pawn is opposed by enemy pawn.            *
  *************************************************************************/

  while (IS_SQ(nextSq)) {

    if (b.pieces[nextSq] == PAWN) { // either opposed by enemy pawn or doubled
      flagIsPassed = 0;
      if (b.color[nextSq] == side)
        result -= 20;       // doubled pawn penalty
      else
        flagIsOpposed = 1;  // flag our pawn as opposed
    }

    if (IS_SQ(nextSq + WEST) && isPiece(!side, PAWN, nextSq + WEST))
      flagIsPassed = 0;

    if (IS_SQ(nextSq + EAST) && isPiece(!side, PAWN, nextSq + EAST))
      flagIsPassed = 0;

    nextSq += stepFwd;
  }

  /*************************************************************************
  *   Another loop, going backwards and checking whether pawn has support. *
  *   Here we can at least break out of it for speed optimization.         *
  *************************************************************************/

  nextSq = sq;
  while (IS_SQ(nextSq)) {

    if (IS_SQ(nextSq + WEST) && isPiece(side, PAWN, nextSq + WEST)) {
      flagIsWeak = 0;
      break;
    }

    if (IS_SQ(nextSq + EAST) && isPiece(side, PAWN, nextSq + EAST)) {
      flagIsWeak = 0;
      break;
    }

    nextSq += stepBck;
  }

  /*************************************************************************
  *  Evaluate passed pawns, scoring them higher if they are protected      *
  *  or if their advance is supported by friendly pawns                    *
  *************************************************************************/

  if (flagIsPassed) {
    if (isPawnSupported(sq, side)) result += e.protected_passer[side][sq];
    else                             result += e.passed_pawn[side][sq];
  }

  /*************************************************************************
  *  Evaluate weak pawns, increasing the penalty if they are situated      *
  *  on a half-open file                                                   *
  *************************************************************************/

  if (flagIsWeak) {
    result += e.weak_pawn[side][sq];
    if (!flagIsOpposed)
      result -= 4;
  }

  return result;
}

int isPawnSupported(S8 sq, S8 side) {
  int step;
  if (side == WHITE) step = SOUTH; else step = NORTH;

  if (IS_SQ(sq + WEST) && isPiece(side, PAWN, sq + WEST)) return 1;
  if (IS_SQ(sq + EAST) && isPiece(side, PAWN, sq + EAST)) return 1;
  if (IS_SQ(sq + step + WEST) && isPiece(side, PAWN, sq + step + WEST)) return 1;
  if (IS_SQ(sq + step + EAST) && isPiece(side, PAWN, sq + step + EAST)) return 1;

  return 0;
}

/******************************************************************************
*                             Pattern detection                               *
******************************************************************************/

void blockedPieces() {

  // central pawn blocked, bishop hard to develop
  if (isPiece(WHITE, BISHOP, C1) && isPiece(WHITE, PAWN, D2) && b.color[D3] != COLOR_EMPTY)
    v.Blockages[WHITE] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(WHITE, BISHOP, F1) && isPiece(WHITE, PAWN, E2) && b.color[E3] != COLOR_EMPTY)
    v.Blockages[WHITE] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(BLACK, BISHOP, C8) && isPiece(BLACK, PAWN, D7) && b.color[D6] != COLOR_EMPTY)
    v.Blockages[BLACK] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(BLACK, BISHOP, F8) && isPiece(BLACK, PAWN, E7) && b.color[E6] != COLOR_EMPTY)
    v.Blockages[BLACK] -= e.P_BLOCK_CENTRAL_PAWN;

  // uncastled king blocking own rook
  if ((isPiece(WHITE, KING, F1) || isPiece(WHITE, KING, G1)) &&
    (isPiece(WHITE, ROOK, H1) || isPiece(WHITE, ROOK, G1))
    )
    v.Blockages[WHITE] -= e.P_KING_BLOCKS_ROOK;

  if ((isPiece(WHITE, KING, C1) || isPiece(WHITE, KING, B1)) &&
    (isPiece(WHITE, ROOK, A1) || isPiece(WHITE, ROOK, B1))
    )
    v.Blockages[WHITE] -= e.P_KING_BLOCKS_ROOK;

  if ((isPiece(BLACK, KING, F8) || isPiece(BLACK, KING, G8)) &&
    (isPiece(BLACK, ROOK, H8) || isPiece(BLACK, ROOK, G8))
    )
    v.Blockages[BLACK] -= e.P_KING_BLOCKS_ROOK;

  if ((isPiece(BLACK, KING, C8) || isPiece(BLACK, KING, B8)) &&
    (isPiece(BLACK, ROOK, A8) || isPiece(BLACK, ROOK, B8))
    )
    v.Blockages[BLACK] -= e.P_KING_BLOCKS_ROOK;
}

int isPiece(U8 color, U8 piece, S8 sq) {
  return ((b.pieces[sq] == piece) && (b.color[sq] == color));
}

/***************************************************************************************
*                             Printing eval results                                    *
***************************************************************************************/

void printEval() {
  printf("------------------------------------------\n");
  printf("Total value (for side to move): %d \n", eval(-INF, INF, 0));
  printf("Material balance    : %d \n", b.PieceMaterial[WHITE] + b.PawnMaterial[WHITE] - b.PieceMaterial[BLACK] - b.PawnMaterial[BLACK]);
  printf("Material adjustement: "); printEvalFactor(v.MaterialAdjustement[WHITE], v.MaterialAdjustement[BLACK]);
  printf("Mg Piece/square tables : "); printEvalFactor(b.PcsqMg[WHITE], b.PcsqMg[BLACK]);
  printf("Eg Piece/square tables : "); printEvalFactor(b.PcsqEg[WHITE], b.PcsqEg[BLACK]);
  printf("Mg Mobility            : "); printEvalFactor(v.mgMob[WHITE], v.mgMob[BLACK]);
  printf("Eg Mobility            : "); printEvalFactor(v.mgMob[WHITE], v.egMob[BLACK]);
  printf("Pawn structure      : %d \n", evalPawnStructure());
  printf("Blockages           : "); printEvalFactor(v.Blockages[WHITE], v.Blockages[BLACK]);
  printf("Positional themes   : "); printEvalFactor(v.PositionalThemes[WHITE], v.PositionalThemes[BLACK]);
  printf("King Shield         : "); printEvalFactor(v.kingShield[WHITE], v.kingShield[BLACK]);
  printf("Tempo: ");
  if (b.stm == WHITE) printf("%d", e.TEMPO); else printf("%d", -e.TEMPO);
  printf("\n");
  printf("------------------------------------------\n");
}

void printEvalFactor(int wh, int bl) {
  printf("white %4d, black %4d, total: %4d \n", wh, bl, wh - bl);
}

```

**[Up one Level](CPW-Engine "CPW-Engine")**

