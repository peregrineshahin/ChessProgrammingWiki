---
title: CPWEngine recognize
---
**[Home](Home "Home") * [Engines](Engines "Engines") * [CPW-Engine](CPW-Engine "CPW-Engine") * Recognizer**

```C++
##include "stdafx.h"

int is_rim[64] = {
  1,   1,   1,   1,   1,   1,   1,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   0,   0,   0,   0,   0,   0,   1,
  1,   1,   1,   1,   1,   1,   1,   1
};


/* please note that this recognizer assumes that the position is legal,
i.e. side to move is not in check */

int isDraw() {

  /* no pawns */
  if (!b.PawnMaterial[WHITE] && !b.PawnMaterial[BLACK]) {

    /* both sides have at most one minor piece - to guard against the possibility
    of a helpmate in the corner, we do not claim an immediate draw if the king
    of the weaker side stands on the edge of the board */

    if (b.PieceMaterial[WHITE] < 400 &&
      b.PieceMaterial[BLACK] < 400 &&
      (!is_rim[b.KingLoc[WHITE]] || b.PieceMaterial[BLACK] == 0) &&
      (!is_rim[b.KingLoc[BLACK]] || b.PieceMaterial[WHITE] == 0)
      )
      return 1;

  }

  /* default: no draw spotted */
  return 0;
}

```

**[Up one Level](CPW-Engine "CPW-Engine")**

