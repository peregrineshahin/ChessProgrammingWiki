---
title: Captures
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Moves](Moves "Moves") * Captures**

**Captures** are [tactical moves](Tactical_Moves "Tactical Moves") changing [material balance](Material#Balance "Material") where an opponent [piece](Pieces "Pieces") is removed from the [board](Chessboard "Chessboard") as part of the completion of the move. This is either done by moving a piece to a [square](Squares "Squares"), which is [occupied](Occupancy "Occupancy") by the opponent captured piece - or as a special case of [pawn](Pawn "Pawn") takes pawn, [en passant](En_passant "En passant").

Winning captures are those with least valuable aggressor of most valuable victim, where even a recapture would win [material](Material "Material"), and captures of pieces [en prise](En_prise "En prise"), that is the union of undefended ([hanging](Hanging_Piece "Hanging Piece")) pieces, as well as pieces defended inadequately. A [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") might be applied to determine a victim is *en prise* or not. Equal captures are exchanges of equal valued pieces. Winning, as well as equal captures are subject of [quiescence search](Quiescence_Search "Quiescence Search"). Some programs [extend captures](Capture_Extensions "Capture Extensions") or [recaptures](Recapture_Extensions "Recapture Extensions") under certain conditions, i.e. material becomes close to the root score again.

## Capture Generation

With [mailbox](Mailbox "Mailbox") like square centric [board representations](Board_Representation "Board Representation"), capture [generation](Move_Generation "Move Generation") requires a so called [blocker loop](Vector_Attacks#NewArchitecture "Vector Attacks"), while [bitboards](Bitboards "Bitboards") rely on attack generation and [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with the set of opponent pieces.

## Six times Take Five

|  Capture
|  Best case
|  Worst case
|
| --- | --- | --- |
|  capturing with the pawn
|
|  pxQ
|  winning queen
|  pawn for queen
|
|  pxR
|  winning rook
|  pawn for rook
|
|  pxB
|  winning bishop
|  pawn for bishop
|
|  pxN
|  winning knight
|  pawn for knight
|
|  pxP
|  winning pawn
|  exchanging pawns
|
|  capturing with the knight
|
|  nxQ
|  winning queen
|  knight for queen
|
|  nxR
|  winning rook
|  winning the exchange
|
|  nxB
|  winning bishop
|  exchanging minors
|
|  nxN
|  winning knight
|  exchanging minors
|
|  nxP
|  winning pawn
|  losing knight for pawn
|
|  capturing with the bishop
|
|  bxQ
|  winning queen
|  bishop for queen
|
|  bxR
|  winning rook
|  winning the exchange
|
|  bxB
|  winning bishop
|  exchanging minors
|
|  bxN
|  winning knight
|  exchanging minors
|
|  bxP
|  winning pawn
|  losing bishop for pawn
|
|  capturing with the rook
|
|  rxQ
|  winning queen
|  rook for queen
|
|  rxR
|  winning rook
|  exchanging rooks
|
|  rxB
|  winning bishop
|  losing exchange
|
|  rxN
|  winning knight
|  losing exchange
|
|  rxP
|  winning pawn
|  losing rook for pawn
|
|  capturing with the queen
|
|  qxQ
|  winning queen
|  exchanging queens
|
|  qxR
|  winning rook
|  losing queen for rook
|
|  qxB
|  winning bishop
|  losing queen for bishop
|
|  qxN
|  winning knight
|  losing queen for knight
|
|  qxP
|  winning pawn
|  losing queen for pawn
|
|  capturing with the king, always winning captures
|
|  kxQ
|  winning queen
|  |
|  kxR
|  winning rook
|  |
|  kxB
|  winning bishop
|  |
|  kxN
|  winning knight
|  |
|  kxP
|  winning pawn
|  |

## See also

- [Algebraic Chess Notation - Captures](Algebraic_Chess_Notation#Captures "Algebraic Chess Notation")
- [Capture Extensions](Capture_Extensions "Capture Extensions")
- [Capture (program)](</Capture_(program)> "Capture (program)") by [Sylvain Renard](Sylvain_Renard "Sylvain Renard")
- [Material](Material "Material")
- [MVV-LVA](MVV-LVA "MVV-LVA")
- [Promotions](Promotions "Promotions")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
- [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Tactical Moves](Tactical_Moves "Tactical Moves")

## Forum Posts

- [a question about the definition of winning capture in Rebel(diagrams)](https://www.stmintz.com/ccc/index.php?id=275173) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 05, 2003
- [Reducing/Pruning Bad Captures (SEE \< 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 19, 2011 » [Pruning](Pruning "Pruning"), [Reductions](Reductions "Reductions"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Perft and Captures](http://www.open-chess.org/viewtopic.php?f=5&t=2238) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2013 » [Perft](Perft "Perft")
- [Sorting Captures](http://www.talkchess.com/forum/viewtopic.php?t=61021) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), August 03, 2016 » [Move Ordering](Move_Ordering "Move Ordering")
- [Ordering Capture Moves](http://www.talkchess.com/forum/viewtopic.php?t=65084) by [Jason Fernandez](index.php?title=Jason_Fernandez&action=edit&redlink=1 "Jason Fernandez (page does not exist)"), [CCC](CCC "CCC"), September 06, 2017 » [Move Ordering - Captures](Move_Ordering#Captures "Move Ordering")

## External Links

- [Capture (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Capture)
- [Dave Brubeck Quartet](https://en.wikipedia.org/wiki/Dave_Brubeck) - [Take Five](https://en.wikipedia.org/wiki/Take_Five), [Newport Jazz Festival, 1979](http://www.davebrubeckjazz.com/Recordings/Detail/Dave-Brubeck,-Newport-Jazz-Festival/00277), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat.: [Jerry Bergonzi](Category:Jerry_Bergonzi "Category:Jerry Bergonzi"), [Chris Brubeck](https://en.wikipedia.org/wiki/Chris_Brubeck) and [Randy Jones](<https://en.wikipedia.org/wiki/Randy_Jones_(drummer)>)

**[Up one Level](Moves "Moves")**

