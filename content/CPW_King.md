---
title: CPW King
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * CPW_King**

This is a patch to the [CPW-Engine](CPW-Engine "CPW-Engine"), changing its evaluation function. Modifications include:

- getting rid of [lazy eval](Lazy_Evaluation "Lazy Evaluation")
- using [eval hash table](Evaluation_Hash_Table "Evaluation Hash Table") as default
- modifying [mobility](Mobility "Mobility") functions, so that they will count number of attacks on squares near enemy king as well as the number of attackers
- placing those functions in the piece-specific routines, before [king safety](King_Safety "King Safety") calculation, so that it can make use of them
- adding functions to count attacks by queens

Resulting program plays at the roughly the same strength as regular CPW-Engine, but is much more entertaining to watch. To obtain optimal results, piece/square values fo bishops and knights should be raised a tiny bit.

The most obvious drawback of the presented code is that it does not see attackers that are lined up, such as rooks doubled on a file. If You consider making this example into a real program, this is the first thing to change.

We need to add the following function to the eval_init.cpp, in order to define squares which are considered worthwhile to attack:

```C++

void setSquaresNearKing() {
  for (int i = 0; i < 128; ++i)
    for (int j = 0; j < 128; ++j)
    {

      e.sqNearK[WHITE][i][j] = 0;
      e.sqNearK[BLACK][i][j] = 0;

      if (IS_SQ(i) &&
        IS_SQ(j)) {

        // squares constituting the ring around both kings

        if (j == i + NORTH || j == i + SOUTH ||
          j == i + EAST || j == i + WEST ||
          j == i + NW || j == i + NE ||
          j == i + SW || j == i + SE) {

          e.sqNearK[WHITE][i][j] = 1;
          e.sqNearK[BLACK][i][j] = 1;
        }

        /* squares in front of the white king ring */

        if (j == i + NORTH + NORTH ||
          j == i + NORTH + NE ||
          j == i + NORTH + NW)
          e.sqNearK[WHITE][i][j] = 1;

        // squares in front og the black king ring

        if (j == i + SOUTH + SOUTH ||
          j == i + SOUTH + SE ||
          j == i + SOUTH + SW)
          e.sqNearK[WHITE][i][j] = 1;
      }
    }
}

```

The complete eval.cpp looks as follows:

```C++

##include "stdafx.h"
##include "0x88_math.h"
##include "eval.h"
##include "transposition.h"

##define use_eval_hash

/* mobility values for various piece kinds */
int bish_mob[16] = { -10, -4, 0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8 };
int rook_mob[16] = { -4,  -2, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4 };
int knight_mob[9] = { -6,  -4, 0, 2, 4, 5, 6, 7, 8 };

/* adjustements of piece value based on the number of own pawns */
int knight_adj[9] = { -20, -16, -12, -8, -4,  0,  4,  8, 12 };
int rook_adj[9] = { 15,  12,   9,  6,  3,  0, -3, -6, -9 };

##define MINOR_ATT 2
##define ROOK_ATT  4
##define QUEEN_ATT 8

/*******************************************************************
*  This struct holds data about certain aspects of evaluation,     *
*  which allows program to print them if desired.                  *
*******************************************************************/

struct eval_vector {
  int MaterialAdjustement[2];
  int Blockages[2];
  int PositionalThemes[2];
  int Mobility[2];
  int KingAttackers[2]; // no. of pieces attacking enemy king
  int KingPressure[2];  // value of king pressure
} v;

/* local lists of pieces and pawns and indexes to them */
U8 pieceList[32];
U8 pieceIndex;
U8 pawnList[32];
U8 pawnIndex;

/* global flag used by mobility/attack detection functions to know
if a piece examined currently is a king attacker */

int isAttacker = 0;

/*****************************************************************************
*                  Fast evaluation (material + pcsq + pawn structure)        *
*****************************************************************************/

int fast_eval() {

  /* fold in incrementally updated values */
  int result = p.PieceMaterial[WHITE] + p.PawnMaterial[WHITE] + p.Pcsq[WHITE]
    - p.PieceMaterial[BLACK] - p.PawnMaterial[BLACK] - p.Pcsq[BLACK];

  /* evaluate pawn structure, remembering that a pawn list must be set */
  result += getPawnScoreNoList();

  /* return score relative to the side to move */
  if (b.stm == BLACK)
    return -result;
  else
    return result;
}


/*****************************************************************************
*                  1. Main evaluation function                               *
*****************************************************************************/

int eval(int alpha, int beta) {
  int result;

  /* probe the evaluatinon hashtable */
  int probeval = tteval_probe();
  if (probeval != INVALID)
    return probeval;

  /* set internal data of the evaluation function */
  eval_setPieceLists();
  eval_clearVector();

  /* sum the incrementally counted material and pcsq values */
  result = p.PieceMaterial[WHITE] + p.PawnMaterial[WHITE] + p.Pcsq[WHITE]
    - p.PieceMaterial[BLACK] - p.PawnMaterial[BLACK] - p.Pcsq[BLACK];

  /* tempo bonus */
  if (b.stm == WHITE)
    result += e.TEMPO;
  else
    result -= e.TEMPO;

  /* add in pawn structure evaluation */
  result += getPawnScore();

  /*******************************************************************
  *  Low material correction - guarding against an illusory material *
  *  advantage.  Program  will not not  expect to  win  having  only *
  *  a single minor piece and no pawns.                              *
  *******************************************************************/

  if ((p.PawnMaterial[WHITE] == 0) &&
    (p.PieceMaterial[WHITE] < 400) &&
    (result > 0))
    return 0;

  if ((p.PawnMaterial[BLACK] == 0) &&
    (p.PieceMaterial[BLACK] < 400) &&
    (result < 0))
    return 0;

  /*******************************************************************
  *  Program will not expect to win having only two knights in case  *
  *  neither  side  has pawns. Please note that this  code  assumes  *
  *  different values for bishop and knight, and eval_init() should  *
  *  take care of that.                                              *
  *******************************************************************/

  if (!p.PawnMaterial[WHITE] && !p.PawnMaterial[BLACK]) {
    if (p.PieceMaterial[WHITE] == 2 * e.PIECE_VALUE[KNIGHT] && result > 0)
      result = 0;
    if (p.PieceMaterial[BLACK] == 2 * e.PIECE_VALUE[KNIGHT] && result < 0)
      result = 0;
  }

  /*******************************************************************
  * Adjusting material value for the various combinations of pieces. *
  * Currently it scores bishop, knight and rook pairs. The first one *
  * gets a bonus, the latter two - a penalty. Please also note that  *
  * adjustements of knight and rook value based on the number of own *
  * pawns on the board are done within the piece-specific routines.  *
  *******************************************************************/

  if (p.PieceCount[WHITE][BISHOP] > 1) v.MaterialAdjustement[WHITE] += e.BISHOP_PAIR;
  if (p.PieceCount[BLACK][BISHOP] > 1) v.MaterialAdjustement[BLACK] += e.BISHOP_PAIR;
  if (p.PieceCount[WHITE][KNIGHT] > 1) v.MaterialAdjustement[WHITE] -= e.P_KNIGHT_PAIR;
  if (p.PieceCount[BLACK][KNIGHT] > 1) v.MaterialAdjustement[BLACK] -= e.P_KNIGHT_PAIR;
  if (p.PieceCount[WHITE][ROOK] > 1) v.MaterialAdjustement[WHITE] -= e.P_ROOK_PAIR;
  if (p.PieceCount[BLACK][ROOK] > 1) v.MaterialAdjustement[BLACK] -= e.P_ROOK_PAIR;


  // penalty for the lack of pawns - added 28.07.2008
  if (p.PieceCount[WHITE][PAWN] == 0) v.MaterialAdjustement[WHITE] -= 16;
  if (p.PieceCount[BLACK][PAWN] == 0) v.MaterialAdjustement[BLACK] -= 16;

  /********************************************************************
  *   Evaluate piece placement. This giant loop calls piece-specific  *
  *   functions which tend to do four things:                         *
  *                                                                   *
  *   (1) they look for the trapped pieces and blockages              *
  *   (2) they look for rooks on (half) open files                    *
  *   (3) they calculate mobility and king safety                     *
  *   (4) they calculate adjustements of material value based on      *
  *      the number of pawns                                          *
  ********************************************************************/

  for (int i = 0; i < pieceIndex; i++) {

    S8 sq = pieceList[i];

    switch (b.color[sq]) {
    case WHITE: {
      switch (b.pieces[sq]) {
      case KNIGHT: wKnightEval(sq); break;
      case BISHOP: wBishopEval(sq); break;
      case ROOK: wRookEval(sq);   break;
      case QUEEN: wQueenEval(sq);  break;
      }
    }
                break;
    case BLACK: {
      switch (b.pieces[sq]) {
      case KNIGHT: bKnightEval(sq); break;
      case BISHOP: bBishopEval(sq); break;
      case ROOK: bRookEval(sq);   break;
      case QUEEN: bQueenEval(sq);  break;
      }
    }
                break;
    }
  }

  /********************************************************************
  *   After  the piece evaluation loop we have the king tropism  data *
  *   in order, so it is time to do full king evaluation. For details *
  *   see comments in wKingEval() function.                           *
  ********************************************************************/

  result += wKingEval(p.KingLoc[WHITE]);
  result -= bKingEval(p.KingLoc[BLACK]);

  /********************************************************************
  *   Pattern evaluation - mainly things interrelated with the pawn   *
  *   position, not fitting elsewhere.                                *
  ********************************************************************/

  blockedCentralPawns(); // don't block central pawns on initial squares
  blockedRooks();        // avoid pseudo-castling which blocks the rook
  slavMistake();         // don't play c4-c5 against Slav / Stonewall
  evalFianchetto();

  /********************************************************************
  *  Fold in data gathered in evaluation vector.                      *
  ********************************************************************/

  result += v.MaterialAdjustement[WHITE];
  result -= v.MaterialAdjustement[BLACK];
  result += v.Blockages[WHITE];
  result -= v.Blockages[BLACK];
  result += v.PositionalThemes[WHITE];
  result -= v.PositionalThemes[BLACK];

  /******************************************************************
  *  Here mobility score is scaled according to the side to move.   *
  *  We  give  more weight to opponent's mobility  to  encourage    *
  *  playing for restraint.                                         *
  ******************************************************************/

  if (sd.myside == WHITE) {
    v.Mobility[BLACK] *= 4;
    v.Mobility[BLACK] /= 3;
  }
  else {
    v.Mobility[WHITE] *= 4;
    v.Mobility[WHITE] /= 3;
  }

  result += v.Mobility[WHITE];
  result -= v.Mobility[BLACK];

  /*******************************************************************
  *  Finally return the score relative to the side to move.          *
  *******************************************************************/

  if (b.stm == BLACK)
    result = -result;

  // save value in the eval tt
  tteval_save(result);

  return result;
}

/***********************************************************************
*                     2. Preparatory routines                          *
***********************************************************************/

void eval_setPieceLists() {

  /***********************************************************************
  * Create  local  lists  of pieces and pawns. This is  done  to  avoid  *
  * looping through the entire board three times: for pawns, for pieces  *
  * and again evaluating mobility if lazy eval does not produce a cutoff.*
  ***********************************************************************/

  pieceIndex = 0;
  pawnIndex = 0;

  for (U8 row = 0; row < 8; row++)
    for (U8 col = 0; col < 8; col++) {

      S8 sq = row * 16 + col;

      if (b.color[sq] != COLOR_EMPTY) {
        if (b.pieces[sq] == PAWN) {
          pawnList[pawnIndex] = sq;
          ++pawnIndex;
        }
        else {
          pieceList[pieceIndex] = sq;
          ++pieceIndex;
        }
      }
    }
}

/***********************************************************************
* This is a reduced version of the previous function, and it creates   *
* only a list of pawns.                                                *
***********************************************************************/

void eval_setPawnLists() {

  pawnIndex = 0;

  for (U8 row = 0; row < 8; row++)
    for (U8 col = 0; col < 8; col++) {

      S8 sq = row * 16 + col;

      if (b.color[sq] != COLOR_EMPTY &&
        b.pieces[sq] == PAWN) {
        pawnList[pawnIndex] = sq;
        ++pawnIndex;
      }
    }
}


void eval_clearVector() {
  v.MaterialAdjustement[WHITE] = 0;
  v.MaterialAdjustement[BLACK] = 0;
  v.PositionalThemes[WHITE] = 0;
  v.PositionalThemes[BLACK] = 0;
  v.KingAttackers[WHITE] = 0;
  v.KingAttackers[BLACK] = 0;
  v.KingPressure[WHITE] = 0;
  v.KingPressure[BLACK] = 0;
  v.Blockages[WHITE] = 0;
  v.Blockages[BLACK] = 0;
  v.Mobility[WHITE] = 0;
  v.Mobility[BLACK] = 0;
}

/************************************************************************
*                    3. King safety evaluation                          *
************************************************************************/

int wKingEval(S8 sq) {
  int result = 0;

  if (p.PieceMaterial[WHITE] < e.ENDGAME_MAT) {
    result += e.endgame_king[sq];
  }
  else {
    result += e.PIECESQUARE[KING][WHITE][sq];
    result += wKingShield();
    result -= scaleAttacks(v.KingPressure[BLACK], v.KingAttackers[BLACK]);

    /* Scale the middlegame king evaluation against remaining enemy material */
    result *= p.PieceMaterial[BLACK];
    result /= e.START_MATERIAL;
  }

  return result;
}

int bKingEval(S8 sq) {
  int result = 0;

  if (p.PieceMaterial[BLACK] < e.ENDGAME_MAT) {
    result += e.endgame_king[sq];
  }
  else {
    result += e.PIECESQUARE[KING][BLACK][sq];
    result += bKingShield();
    result -= scaleAttacks(v.KingPressure[WHITE], v.KingAttackers[WHITE]);

    /* Scale the middlegame king evaluation against remaining enemy material */
    result *= p.PieceMaterial[WHITE];
    result /= e.START_MATERIAL;
  }

  return result;
}

int scaleAttacks(int attack_value, int n_of_attackers) {
  int result;

  switch (n_of_attackers) {
  case 0: result = 0;
  case 1: result = 0;
  case 2: result = attack_value;
  case 3: result = (attack_value * 4) / 3;
  case 4: result = (attack_value * 3) / 2;
  default: result = attack_value * 2;
  }

  return result;
}

int wKingShield() {

  int result = 0;

  /* king on the kingside */
  if (COL(p.KingLoc[WHITE]) > COL_E) {

    if (isPiece(WHITE, PAWN, F2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, F3))  result += e.SHIELD_2;

    if (isPiece(WHITE, PAWN, G2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, G3))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[WHITE][COL_G] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(WHITE, PAWN, H2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, H3))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[WHITE][COL_H] == 0) result -= e.P_NO_SHIELD;
  }

  /* king on the queenside */
  else if (COL(p.KingLoc[WHITE]) < COL_D) {

    if (isPiece(WHITE, PAWN, A2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, A3))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[WHITE][COL_A] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(WHITE, PAWN, B2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, B3))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[WHITE][COL_B] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(WHITE, PAWN, C2))  result += e.SHIELD_1;
    else if (isPiece(WHITE, PAWN, C3))  result += e.SHIELD_2;
  }

  return result;
}

int bKingShield() {
  int result = 0;

  /* king on the kingside */
  if (COL(p.KingLoc[BLACK]) > COL_E) {
    if (isPiece(BLACK, PAWN, F7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, F6))  result += e.SHIELD_2;

    if (isPiece(BLACK, PAWN, G7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, G6))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[BLACK][COL_G] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(BLACK, PAWN, H7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, H6))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[BLACK][COL_H] == 0) result -= e.P_NO_SHIELD;
  }

  /* king on the queenside */
  else if (COL(p.KingLoc[BLACK]) < COL_D) {
    if (isPiece(BLACK, PAWN, A7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, A6))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[BLACK][COL_A] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(BLACK, PAWN, B7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, B6))  result += e.SHIELD_2;
    else if (p.PawnsOnFile[BLACK][COL_B] == 0) result -= e.P_NO_SHIELD;

    if (isPiece(BLACK, PAWN, C7))  result += e.SHIELD_1;
    else if (isPiece(BLACK, PAWN, C6))  result += e.SHIELD_2;
  }
  return result;
}

/*********************************************************************************
*                            4. Pawn structure evaluaton                         *
*********************************************************************************/

int getPawnScore() {
  int result;

  /*****************************************************************************
  *   This function wraps hashing mechanism around evalPawnStructure(). Please *
  *   note  that since we use the pawn hashtable, evalPawnStructure() must not *
  *   take into account the piece position.  In a more elaborate program, pawn *
  *   hashtable would contain only the characteristics of pawn structure,  and *
  *   scoring them in conjunction with the piece position would have been done *
  *   elsewhere.                                                               *
  ******************************************************************************/

  int probeval = ttpawn_probe();
  if (probeval != INVALID)
    return probeval;

  result = evalPawnStructure();

  ttpawn_save(result);

  return result;
}

/* a clone of getPawnScore, used in fastEval, when the pawn list is not set */

int getPawnScoreNoList() {
  int result;

  int probeval = ttpawn_probe();
  if (probeval != INVALID)
    return probeval;

  eval_setPawnLists();
  result = evalPawnStructure();

  ttpawn_save(result);

  return result;
}

int evalPawnStructure() {
  int result = 0;

  /* 1. evaluate pawn center */
  result += evalPawnCenter();

  /* 2. evaluate doubled/tripled pawns */
  for (U8 col = 0; col < 8; col++) {
    result -= e.P_MULTI_PAWN[p.PawnsOnFile[WHITE][col]];
    result += e.P_MULTI_PAWN[p.PawnsOnFile[BLACK][col]];
  }

  /* 3. core procedure: loop through pawn list, evaluating each pawn on the board */
  for (U8 i = 0; i < pawnIndex; i++) {

    S8 sq = pawnList[i];

    if (b.color[sq] == WHITE)
      result += wPawnEval(sq);
    else
      result -= bPawnEval(sq);
  }
  return result;
}

int evalPawnCenter() {
  int result = 0;

  if (isPiece(WHITE, PAWN, D4)) {
    if (isPiece(WHITE, PAWN, E4)) result += e.DUO_D4E4;
    if (isPiece(WHITE, PAWN, C4)) result += e.DUO_D4C4;
    if (isPiece(WHITE, PAWN, E3)) result += e.DUO_D4E3;
  }

  if (isPiece(WHITE, PAWN, E4)) {
    if (isPiece(WHITE, PAWN, F4)) result += e.DUO_E4F4;
    if (isPiece(WHITE, PAWN, D3)) result += e.DUO_E4D3;
  }

  if (isPiece(BLACK, PAWN, D5)) {
    if (isPiece(BLACK, PAWN, E5)) result -= e.DUO_D4E4;
    if (isPiece(BLACK, PAWN, C5)) result -= e.DUO_D4C4;
    if (isPiece(BLACK, PAWN, E6)) result -= e.DUO_D4E3;
  }

  if (isPiece(BLACK, PAWN, E5)) {
    if (isPiece(BLACK, PAWN, F5)) result -= e.DUO_E4F4;
    if (isPiece(BLACK, PAWN, D6)) result -= e.DUO_E4D3;
  }

  return result;
}

int wPawnEval(S8 sq) {
  int result = 0;

  /* 1. Evaluate passed pawns, scoring them higher if they are
  protected by friendly pawns */

  if (isWPFree(sq)) {
    if (isWPSupported(sq))
      result += e.w_protected_passer[sq];
    else
      result += e.w_passed_pawn[sq];
  }

  /* 2. Evaluate weak pawns */

  if (isWPWeak(sq)) {
    result += e.w_weak_pawn[sq];
    /* weak pawns on half-open files tend to be even weaker */
    if (p.PawnsOnFile[BLACK][COL(sq)] == 0)
      result -= 4;
  }

  return result;
}

int bPawnEval(S8 sq) {
  int result = 0;

  /* 1. Evaluate passed pawns, scoring them higher if they are
  protected by friendly pawns */

  if (isBPFree(sq)) {
    if (isBPSupported(sq))
      result += e.b_protected_passer[sq];
    else
      result += e.b_passed_pawn[sq];
  }

  /* 2. Evaluate weak pawns */

  if (isBPWeak(sq)) {
    result += e.b_weak_pawn[sq];
    /* weak pawns on half-open files tend to be even weaker */
    if (p.PawnsOnFile[WHITE][COL(sq)] == 0)
      result -= 4;
  }

  return result;
}

int isWPFree(S8 sq) {

  S8 nextSq = sq + NORTH;

  while (IS_SQ(nextSq)) {

    /* either blocked by enemy pawn or doubled */
    if (b.pieces[nextSq] == PAWN)
      return 0;

    if (IS_SQ(nextSq + WEST) && isPiece(BLACK, PAWN, nextSq + WEST))
      return 0;

    if (IS_SQ(nextSq + EAST) && isPiece(BLACK, PAWN, nextSq + EAST))
      return 0;

    nextSq += NORTH;
  }

  return 1;
}

int isBPFree(S8 sq) {
  S8 nextSq = sq + SOUTH;

  while (IS_SQ(nextSq)) {

    /* either blocked by enemy pawn or doubled */
    if (b.pieces[nextSq] == PAWN)
      return 0;

    if (IS_SQ(nextSq + WEST) && isPiece(WHITE, PAWN, nextSq + WEST))
      return 0;

    if (IS_SQ(nextSq + EAST) && isPiece(WHITE, PAWN, nextSq + EAST))
      return 0;

    nextSq += SOUTH;
  }

  return 1;
}

int isWPWeak(S8 sq) {
  S8 nextSq = sq;

  while (IS_SQ(nextSq)) {

    if (IS_SQ(nextSq + WEST) && isPiece(WHITE, PAWN, nextSq + WEST))
      return 0;

    if (IS_SQ(nextSq + EAST) && isPiece(WHITE, PAWN, nextSq + EAST))
      return 0;

    nextSq += SOUTH;
  }

  return 1;
}

int isBPWeak(S8 sq) {
  S8 nextSq = sq;

  while (IS_SQ(nextSq)) {

    if (IS_SQ(nextSq + WEST) && isPiece(BLACK, PAWN, nextSq + WEST))
      return 0;

    if (IS_SQ(nextSq + EAST) && isPiece(BLACK, PAWN, nextSq + EAST))
      return 0;

    nextSq += NORTH;
  }

  return 1;
}

/****************************************************************
*  The next two procedures are used in passed pawn evaluation,  *
*  the assumption being that passed pawns that are defended or  *
*  or whose stop square is protected by a friendly pawn tend    *
*  to be stronger.                                              *
*****************************************************************/

int isWPSupported(S8 sq) {
  if (IS_SQ(sq + WEST) && isPiece(WHITE, PAWN, sq + WEST)) return 1;
  if (IS_SQ(sq + EAST) && isPiece(WHITE, PAWN, sq + EAST)) return 1;
  if (IS_SQ(sq + SE) && isPiece(WHITE, PAWN, sq + SE)) return 1;
  if (IS_SQ(sq + SW) && isPiece(WHITE, PAWN, sq + SW)) return 1;

  return 0;
}

int isBPSupported(S8 sq) {
  if (IS_SQ(sq + WEST) && isPiece(BLACK, PAWN, sq + WEST)) return 1;
  if (IS_SQ(sq + EAST) && isPiece(BLACK, PAWN, sq + EAST)) return 1;
  if (IS_SQ(sq + NE) && isPiece(BLACK, PAWN, sq + NE)) return 1;
  if (IS_SQ(sq + NW) && isPiece(BLACK, PAWN, sq + NW)) return 1;

  return 0;
}

/************************************************************************************
*                        5. Evaluation of pieces                                    *
************************************************************************************/

void wKnightEval(S8 sq) {

  /* material value adjustement based on the no. of own pawns */
  v.MaterialAdjustement[WHITE] += knight_adj[p.PieceCount[WHITE][PAWN]];

  /* mobility and king attacks calculation */
  v.Mobility[WHITE] += wKnightMob(sq);

  /* trapped or blocking knight */
  switch (sq) {
  case A8: if (isPiece(BLACK, PAWN, A7) || isPiece(BLACK, PAWN, C7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A8; break;
  case H8: if (isPiece(BLACK, PAWN, H7) || isPiece(BLACK, PAWN, F7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A8; break;
  case A7: if (isPiece(BLACK, PAWN, A6) && isPiece(BLACK, PAWN, B7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A7; break;
  case H7: if (isPiece(BLACK, PAWN, H6) && isPiece(BLACK, PAWN, G7)) v.Blockages[WHITE] -= e.P_KNIGHT_TRAPPED_A7; break;
  case C3: if (isPiece(WHITE, PAWN, C2) && isPiece(WHITE, PAWN, D4) && !isPiece(WHITE, PAWN, E4)) v.Blockages[WHITE] -= e.P_C3_KNIGHT; break;
  }
}

void bKnightEval(S8 sq) {

  /* material value adjustement based on the no. of own pawns */
  v.MaterialAdjustement[BLACK] += knight_adj[p.PieceCount[BLACK][PAWN]];

  /* mobility and king attack calculation */
  v.Mobility[BLACK] += bKnightMob(sq);

  /* trapped or blocking knight */
  switch (sq) {
  case A1: if (isPiece(WHITE, PAWN, A2) || isPiece(WHITE, PAWN, C2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A8; break;
  case H1: if (isPiece(WHITE, PAWN, H2) || isPiece(WHITE, PAWN, F2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A8; break;
  case A2: if (isPiece(WHITE, PAWN, A3) && isPiece(WHITE, PAWN, B2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A7; break;
  case H2: if (isPiece(WHITE, PAWN, H3) && isPiece(WHITE, PAWN, G2)) v.Blockages[BLACK] -= e.P_KNIGHT_TRAPPED_A7; break;
  case C6: if (isPiece(BLACK, PAWN, C7) && isPiece(BLACK, PAWN, D5) && !isPiece(BLACK, PAWN, E5)) v.Blockages[BLACK] -= e.P_C3_KNIGHT; break;
  }
}

void wBishopEval(S8 sq) {

  /* mobility and king attack calculaion */
  v.Mobility[WHITE] += wBishopMob(sq);

  /* trapped bishop and returning bishop */
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

void bBishopEval(S8 sq) {

  /* mobility and king attack calculation */
  v.Mobility[BLACK] += bBishopMob(sq);

  /* trapped bishop and returning bishop */
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

void wRookEval(S8 sq) {

  /* material value adjustement based on the no. of own pawns */
  v.MaterialAdjustement[WHITE] += rook_adj[p.PieceCount[WHITE][PAWN]];

  /* mobility and king attack calculation */
  v.Mobility[WHITE] += wRookMob(sq);

  /* open and half-open files */
  if (p.PawnsOnFile[WHITE][COL(sq)] == 0) {

    if (p.PawnsOnFile[BLACK][COL(sq)] == 0)
      v.PositionalThemes[WHITE] += e.ROOK_OPEN;
    else
      v.PositionalThemes[WHITE] += e.ROOK_HALF;
  }
}

void bRookEval(S8 sq) {

  /* material value adjustement based on the no. of own pawns */
  v.MaterialAdjustement[BLACK] += rook_adj[p.PieceCount[BLACK][PAWN]];

  /* mobility and king attack calculation */
  v.Mobility[BLACK] += bRookMob(sq);

  /* open and half-open files */
  if (p.PawnsOnFile[BLACK][COL(sq)] == 0) {

    if (p.PawnsOnFile[WHITE][COL(sq)] == 0)
      v.PositionalThemes[BLACK] += e.ROOK_OPEN;
    else
      v.PositionalThemes[BLACK] += e.ROOK_HALF;
  }
}

void wQueenEval(S8 sq) {

  /* mobility and king attack calculation */
  v.Mobility[WHITE] += wQueenMob(sq);

  /* penalize premature developement */
  if (ROW(sq) > ROW_2) {
    if (isPiece(WHITE, KNIGHT, B1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, BISHOP, C1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, BISHOP, F1)) v.PositionalThemes[WHITE] -= 2;
    if (isPiece(WHITE, KNIGHT, G1)) v.PositionalThemes[WHITE] -= 2;
  }
}

void bQueenEval(S8 sq) {

  /* mobility and king attack calculation */
  v.Mobility[BLACK] += bQueenMob(sq);

  /* penalize premature developement */
  if (ROW(sq) < ROW_7) {
    if (isPiece(BLACK, KNIGHT, B8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, BISHOP, C8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, BISHOP, F8)) v.PositionalThemes[BLACK] -= 2;
    if (isPiece(BLACK, KNIGHT, G8)) v.PositionalThemes[BLACK] -= 2;
  }
}

/**********************************************************************************
*                        6. Mobility and king attack evaluation                   *
**********************************************************************************/

int wKnightMob(S8 sq) {

  isAttacker = 0;
  int localMobility = leaperMobility(WHITE, sq, KNIGHT, MINOR_ATT);
  if (isAttacker)
    ++v.KingAttackers[WHITE];

  return knight_mob[localMobility];
}

int bKnightMob(S8 sq) {

  isAttacker = 0;
  int localMobility = leaperMobility(BLACK, sq, KNIGHT, MINOR_ATT);
  if (isAttacker)
    ++v.KingAttackers[BLACK];

  return knight_mob[localMobility];
}

int wBishopMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(WHITE, sq, NE, MINOR_ATT)
    + sliderMobility(WHITE, sq, NW, MINOR_ATT)
    + sliderMobility(WHITE, sq, SE, MINOR_ATT)
    + sliderMobility(WHITE, sq, SW, MINOR_ATT);

  if (isAttacker)
    ++v.KingAttackers[WHITE];

  return bish_mob[localMobility];
}

int bBishopMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(BLACK, sq, NE, MINOR_ATT)
    + sliderMobility(BLACK, sq, NW, MINOR_ATT)
    + sliderMobility(BLACK, sq, SE, MINOR_ATT)
    + sliderMobility(BLACK, sq, SW, MINOR_ATT);

  if (isAttacker)
    ++v.KingAttackers[BLACK];

  return bish_mob[localMobility];
}

int wRookMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(WHITE, sq, NORTH, ROOK_ATT)
    + sliderMobility(WHITE, sq, SOUTH, ROOK_ATT)
    + sliderMobility(WHITE, sq, EAST, ROOK_ATT)
    + sliderMobility(WHITE, sq, WEST, ROOK_ATT);

  if (isAttacker)
    ++v.KingAttackers[WHITE];

  return rook_mob[localMobility];
}

int bRookMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(BLACK, sq, NORTH, ROOK_ATT)
    + sliderMobility(BLACK, sq, SOUTH, ROOK_ATT)
    + sliderMobility(BLACK, sq, EAST, ROOK_ATT)
    + sliderMobility(BLACK, sq, WEST, ROOK_ATT);

  if (isAttacker)
    ++v.KingAttackers[BLACK];

  return rook_mob[localMobility];
}

// with queen, currently we look for king attacks, not for mobility

int wQueenMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(WHITE, sq, NORTH, QUEEN_ATT)
    + sliderMobility(WHITE, sq, SOUTH, QUEEN_ATT)
    + sliderMobility(WHITE, sq, EAST, QUEEN_ATT)
    + sliderMobility(WHITE, sq, WEST, QUEEN_ATT)
    + sliderMobility(WHITE, sq, NE, QUEEN_ATT)
    + sliderMobility(WHITE, sq, NW, QUEEN_ATT)
    + sliderMobility(WHITE, sq, SE, QUEEN_ATT)
    + sliderMobility(WHITE, sq, SW, QUEEN_ATT);

  if (isAttacker)
    ++v.KingAttackers[WHITE];

  return 0;
}

int bQueenMob(S8 sq) {

  isAttacker = 0;

  int localMobility = sliderMobility(BLACK, sq, NORTH, QUEEN_ATT)
    + sliderMobility(BLACK, sq, SOUTH, QUEEN_ATT)
    + sliderMobility(BLACK, sq, EAST, QUEEN_ATT)
    + sliderMobility(BLACK, sq, WEST, QUEEN_ATT)
    + sliderMobility(BLACK, sq, NE, QUEEN_ATT)
    + sliderMobility(BLACK, sq, NW, QUEEN_ATT)
    + sliderMobility(BLACK, sq, SE, QUEEN_ATT)
    + sliderMobility(BLACK, sq, SW, QUEEN_ATT);

  if (isAttacker)
    ++v.KingAttackers[BLACK];

  return 0;
}

int sliderMobility(U8 color, S8 sq, int vect, int attBonus) {
  int nextSq = sq + vect;
  int result = 0;

  while (IS_SQ(nextSq)) {

    if (e.sqNearK[!color][p.KingLoc[!color]][nextSq]) {
      isAttacker = 1;
      v.KingPressure[color] += attBonus;
    }

    if (b.color[nextSq] != COLOR_EMPTY) {
      if (b.color[nextSq] != color)
        return result + 1;
      return result;
    }

    ++result;

    nextSq = nextSq + vect;
  }

  return result;
}

int leaperMobility(U8 color, S8 sq, char byPiece, int attBonus) {
  S8 nextSq;
  int result = 0;

  for (U8 dir = 0; dir<8; dir++) {
    nextSq = sq + vector[byPiece][dir];

    if (IS_SQ(nextSq) && b.color[nextSq] != color) {

      /* king attack */
      if (e.sqNearK[!color][p.KingLoc[!color]][nextSq]) {
        isAttacker = 1;
        v.KingPressure[color] += attBonus;
      }
      ++result;
    }
  }

  return result;
}

/***************************************************************************************
*                          7. Pattern detection                                        *
***************************************************************************************/

void blockedCentralPawns() {
  if (isPiece(WHITE, PAWN, D2) && b.color[D3] != COLOR_EMPTY)
    v.Blockages[WHITE] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(WHITE, PAWN, E2) && b.color[E3] != COLOR_EMPTY)
    v.Blockages[WHITE] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(BLACK, PAWN, D7) && b.color[D6] != COLOR_EMPTY)
    v.Blockages[BLACK] -= e.P_BLOCK_CENTRAL_PAWN;
  if (isPiece(BLACK, PAWN, E7) && b.color[E6] != COLOR_EMPTY)
    v.Blockages[BLACK] -= e.P_BLOCK_CENTRAL_PAWN;
}

void blockedRooks() {

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

void slavMistake() {
  if (isPiece(WHITE, PAWN, D4) &&
    isPiece(WHITE, PAWN, C5) &&
    isPiece(BLACK, PAWN, D5) &&
    isPiece(BLACK, PAWN, C6))
    v.PositionalThemes[WHITE] -= e.P_SLAV_MISTAKE;

  if (isPiece(BLACK, PAWN, D5) &&
    isPiece(BLACK, PAWN, C4) &&
    isPiece(WHITE, PAWN, D4) &&
    isPiece(WHITE, PAWN, C3))
    v.PositionalThemes[BLACK] -= e.P_SLAV_MISTAKE;
}

void evalFianchetto() {

  if (isPiece(WHITE, PAWN, G3)) {
    if (isPiece(WHITE, BISHOP, G2))
      v.PositionalThemes[WHITE] += e.FIANCHETTO;
    else {
      if (!isPiece(WHITE, BISHOP, F3) &&
        !isPiece(WHITE, BISHOP, H1) &&
        !isPiece(WHITE, BISHOP, H3))
        v.PositionalThemes[WHITE] -= e.P_NO_FIANCHETTO;
    }
  }

  if (isPiece(WHITE, PAWN, B3)) {
    if (isPiece(WHITE, BISHOP, B2))
      v.PositionalThemes[WHITE] += e.FIANCHETTO;
    else {
      if (!isPiece(WHITE, BISHOP, C3) &&
        !isPiece(WHITE, BISHOP, A1) &&
        !isPiece(WHITE, BISHOP, A3))

        v.PositionalThemes[WHITE] -= e.P_NO_FIANCHETTO;
    }
  }

  if (isPiece(BLACK, PAWN, G6)) {
    if (isPiece(BLACK, BISHOP, G7))
      v.PositionalThemes[BLACK] += e.FIANCHETTO;
    else {
      if (!isPiece(BLACK, BISHOP, F6) &&
        !isPiece(BLACK, BISHOP, H8) &&
        !isPiece(BLACK, BISHOP, H6))
        v.PositionalThemes[BLACK] -= e.P_NO_FIANCHETTO;
    }
  }

  if (isPiece(BLACK, PAWN, B6)) {
    if (isPiece(BLACK, BISHOP, B7))
      v.PositionalThemes[BLACK] += e.P_NO_FIANCHETTO;
    else {
      if (!isPiece(BLACK, BISHOP, C6) &&
        !isPiece(BLACK, BISHOP, A8) &&
        !isPiece(BLACK, BISHOP, A6))
        v.PositionalThemes[BLACK] -= e.P_NO_FIANCHETTO;
    }
  }
}

/* determine if two squares lie on the same or neighbouring columns */
int isNearCol(S8 sq1, S8 sq2) {
  U8 c1 = COL(sq1);
  U8 c2 = COL(sq2);
  U8 hor_dist = (U8)abs(c1 - c2);

  if (hor_dist < 2)
    return 1;
  else
    return 0;
}

int isPiece(U8 color, U8 piece, S8 sq) {
  return ((b.pieces[sq] == piece) && (b.color[sq] == color));
}

/***************************************************************************************
*                          8. Printing eval results                                    *
***************************************************************************************/

void printEval() {
  eval(-30000, 30000);
  printf("------------------------------------------\n");
  printf("Total value (for side to move): %d \n", eval(-INFINITY, INFINITY));
  printf("Material balance    : %d \n", p.PieceMaterial[WHITE] + p.PawnMaterial[WHITE] - p.PieceMaterial[BLACK] - p.PawnMaterial[BLACK]);
  printf("Material adjustement: %d \n", v.MaterialAdjustement[WHITE] - v.MaterialAdjustement[BLACK]);
  printf("Piece/square tables : %d \n", p.Pcsq[WHITE] - p.Pcsq[BLACK]);
  printf("Pawn structure      : %d \n", evalPawnStructure());
  printf("Blockages           : %d \n", v.Blockages[WHITE] - v.Blockages[BLACK]);
  printf("Positional themes   : %d \n", v.PositionalThemes[WHITE] - v.PositionalThemes[BLACK]);
  printf("Mobility: white %d, black %d, total %d \n", v.Mobility[WHITE], v.Mobility[BLACK], v.Mobility[WHITE] - v.Mobility[BLACK]);
  printf("King pressure: white %d, black %d \n", v.KingPressure[WHITE], v.KingPressure[BLACK]);
  printf("King attackers: white %d, black %d \n", v.KingAttackers[WHITE], v.KingAttackers[BLACK]);
  printf("Kings: white %d , black %d, total: %d \n", wKingEval(p.KingLoc[WHITE]), bKingEval(p.KingLoc[BLACK]), wKingEval(p.KingLoc[WHITE]) - bKingEval(p.KingLoc[BLACK]));
  printf("Tempo: ");
  if (b.stm == WHITE) printf("%d", e.TEMPO); else printf("%d", -e.TEMPO);
  printf("\n");
  printf("------------------------------------------\n");
}


```

**[Up one Level](CPW-Engine "CPW-Engine")**

