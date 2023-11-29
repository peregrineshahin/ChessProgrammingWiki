---
title: FirstChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * FirstChess**

[](http://devwebcl.atarionline.pl/cc65/firstchess.png) FirstChess screen <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**FirstChess**,

a very simple [open source chess program](Category:Open_Source "Category:Open Source") with a [command line interface](CLI "CLI") by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), written in [C](C "C") for didactic purpose, introduced in 2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Since FirstChess lacks [en passant](En_passant "En passant") and [castling](Castling "Castling"), there is implicit invitation to improve it.

## Description

## Board

The [8x8 board](8x8_Board "8x8 Board") consists of two [arrays](Array "Array") for [piece type](Pieces#PieceTypeCoding "Pieces") and color.

```C++

##define	PAWN    0x0
##define	KNIGHT  0x1
##define	BISHOP  0x2
##define	ROOK    0x3
##define	QUEEN   0x4
##define	KING    0x5
##define	EMPTY   0x6
##define	WHITE   0x0
##define	BLACK   0x1

int piece[64] = {
    ROOK,  KNIGHT,BISHOP,QUEEN, KING,  BISHOP,KNIGHT,ROOK,
    PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,  PAWN,
    ROOK,  KNIGHT,BISHOP,QUEEN, KING,  BISHOP,KNIGHT,ROOK
};

int color[64] = {
    BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
    BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,
    WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE,
    WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE
};

```

## Search

The [negamaxed](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta") lacks any [move ordering](Move_Ordering "Move Ordering") techniques:

```C++

static int Search(int alpha, int beta, int depth, MOVE * pBestMove)
{
  int i, value, havemove, movecnt;
  MOVE moveBuf[200], tmpMove;
    
  nodes++; /* visiting a node, count it */
  havemove = 0;
  pBestMove->type = MOVE_TYPE_NONE;
  movecnt = Gen(side, moveBuf); /* generate all moves for current position */
  /* loop through the moves */
  for (i = 0; i < movecnt; ++i) {
    mm2 = moveBuf[i];
    if (!MakeMove()) {
      TakeBack();
      continue;
    }
    havemove = 1;
    if (depth - 1 > 0) /* If depth is still, continue to search deeper */
      value = -Search(-beta, -alpha, depth - 1, &tmpMove);
    else /* If no depth left (leaf node), go to evalute that position */
      value = Eval(); 
    TakeBack();
    if (value > alpha) {
      /* This move is so good and caused a cutoff */
      if (value >= beta)
        return beta;
      alpha = value;
      *pBestMove = moveBuf[i]; /* so far, current move is the best reaction
                                * for current position */
    }
  }
  if (!havemove) { /* If no legal moves, that is checkmate or
                    * stalemate */
    if (IsInCheck(side))
      return -MATE + ply; /* add ply to find the longest path to lose or shortest path to win */
    else
      return 0;
  }
  return alpha;
}

```

## Evaluation

FirstChess' [evaluation](Evaluation "Evaluation") considers [material](Material "Material") with following [point values](Point_Value "Point Value"):

```C++

##define   VALUE_PAWN      100
##define   VALUE_KNIGHT    300
##define   VALUE_BISHOP    300
##define   VALUE_ROOK      500
##define   VALUE_QUEEN     900
##define   VALUE_KING      10000

int Eval()
{
  int value_piece[6] = {VALUE_PAWN, VALUE_KNIGHT, VALUE_BISHOP, VALUE_ROOK, VALUE_QUEEN, VALUE_KING};
  int i, score = 0;
  for (i = 0; i < 64; i++) {
    if (color[i] == WHITE)
      score += value_piece[piece[i]];
    else if (color[i] == BLACK)
      score -= value_piece[piece[i]];
  }
  if (side == WHITE)
    return score;
  return -score;
}

```

## See also

- [Ax](Ax "Ax")

## Forum Posts

- [FirstChess - a crazy project!](https://www.stmintz.com/ccc/index.php?id=242289) by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), July 24, 2002
- [Beginner programmer Winboard and chess computing advice](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50206) by tr2, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 09, 2009

## External Links

- [Index of /cc65](http://devwebcl.atarionline.pl/cc65/) from [atarionline.pl](http://devwebcl.atarionline.pl/) <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> firstchess.png from [Index of /cc65](http://devwebcl.atarionline.pl/cc65/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [FirstChess - a crazy project!](https://www.stmintz.com/ccc/index.php?id=242289) by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), July 24, 2002
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> oups, better replace "unsigned char" by "int"

**[Up one level](Engines "Engines")**

