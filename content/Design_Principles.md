---
title: Design Principles
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * Design Principles**

By [Steffan Westcott](Steffan_Westcott "Steffan Westcott") <a id="cite-note-1" href="#cite-ref-1">[1]</a>:

```
I should add that these techniques ([Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")) are designed to take advantage of the parallel nature of bitboards, in that they consider the entire board. Here, routines like RookMovesUp() will calculate the upward rook moves of all friendly rooks.

```

```
In general, I first identify a (bit) pattern of interest, then devise methods for recognising all instances of that pattern on the board. Pattern instances are counted as late as possible, if at all. The complexity of the patterns varies greatly. Simple ones are like [OpenFiles()](Open_File "Open File"), UnmovedRooks(), [PawnAttacks()](Pawn_Attacks_(Bitboards) "Pawn Attacks (Bitboards)"), [PawnRams()](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)"), [PawnDuos()](Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)"), KingIsUpRight(). Medium complexity are ones like ConnectedRooks(), RooksCanCastle(), OnKingDiagonal(), NearKingDiagonal(), [OutPost()](Outposts "Outposts"). Complex examples are [Fortress()](Fortress "Fortress"), PawnMass(), [PawnStorm()](King_Safety#PawnStorm "King Safety"), [BackwardPawns()](Backward_Pawns_(Bitboards) "Backward Pawns (Bitboards)"), [MaterialSignature()](Material#Signature "Material"), [WeakSquareControl()](Square_Control "Square Control"), StrongSquareControl(), [SpaceBehindPawnFront()](Space "Space"), StrongKnightOutposts(), [StrongFianchettoedBishops()](Fianchetto "Fianchetto"), WeakWhiteSquares(), [KingShelter()](King_Safety#PawnShield "King Safety"), [GamePhase()](Game_Phases "Game Phases").

```

```
Often the more complex patterns are combinations of the simpler ones. In fact, the chess position itself can be viewed as composed of 'primitive' or 'atomic' patterns (bitboards). Most of the simpler patterns are returned as bitboards, where set bits indicate a (bit) pattern match. This is fine where simple square-centric patterns are sought, and a yes/no for each square is sufficient.

```

```
Complex patterns like KingShelter() and GamePhase() are really functions which classify (group together) general patterns spread across the whole board, eg. KingShelter() classifies the pawn structure near the king (matches against a large pattern set), MaterialSignature() returns things like BNbn to classify the material balance.

```

```
Just considering the simple patterns, if your engine deals with pattern instances in a serial fashion (strictly one at a time), the algorithm requirements are sufficiently different that an alternative may be better eg. rotated bitboard table lookups, or perhaps even a different board representation altogether. To my mind, the major reason to use bitboards in the first place is to find many pattern instances quickly. In summary, I would advise that my algorithms are no magic bullet - They are better judged in the wider context of your engine design and target architecture.

```

## Rererences

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Bitboard algorithm design principles](https://www.stmintz.com/ccc/index.php?id=261259) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), October 23, 2002

**[Up one Level](Bitboards "Bitboards")**

