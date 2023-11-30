---
title: Captures
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Moves](Moves "Moves") * Captures**

**Captures** are [tactical moves](Tactical_Moves "Tactical Moves") changing [material balance](Material#Balance "Material") where an opponent [piece](Pieces "Pieces") is removed from the [board](Chessboard "Chessboard") as part of the completion of the move. This is either done by moving a piece to a [square](Squares "Squares"), which is [occupied](Occupancy "Occupancy") by the opponent captured piece - or as a special case of [pawn](Pawn "Pawn") takes pawn, [en passant](En_passant "En passant").

Winning captures are those with least valuable aggressor of most valuable victim, where even a recapture would win [material](Material "Material"), and captures of pieces [en prise](En_prise "En prise"), that is the union of undefended ([hanging](Hanging_Piece "Hanging Piece")) pieces, as well as pieces defended inadequately. A [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") might be applied to determine a victim is *en prise* or not. Equal captures are exchanges of equal valued pieces. Winning, as well as equal captures are subject of [quiescence search](Quiescence_Search "Quiescence Search"). Some programs [extend captures](Capture_Extensions "Capture Extensions") or [recaptures](Recapture_Extensions "Recapture Extensions") under certain conditions, i.e. material becomes close to the root score again.

## Capture Generation

With [mailbox](Mailbox "Mailbox") like square centric [board representations](Board_Representation "Board Representation"), capture [generation](Move_Generation "Move Generation") requires a so called [blocker loop](Vector_Attacks#NewArchitecture "Vector Attacks"), while [bitboards](Bitboards "Bitboards") rely on attack generation and [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with the set of opponent pieces.

## Six times Take Five

<table class="wikitable">

<tbody><tr>
<th> Capture
</th>
<th> Best case
</th>
<th> Worst case
</th></tr>
<tr>
<td colspan="3"> capturing with the pawn
</td></tr>
<tr>
<td>  pxQ
</td>
<td>  winning queen
</td>
<td>  pawn for queen
</td></tr>
<tr>
<td>  pxR
</td>
<td>  winning rook
</td>
<td>  pawn for rook
</td></tr>
<tr>
<td>  pxB
</td>
<td>  winning bishop
</td>
<td>  pawn for bishop
</td></tr>
<tr>
<td>  pxN
</td>
<td>  winning knight
</td>
<td>  pawn for knight
</td></tr>
<tr>
<td>  pxP
</td>
<td>  winning pawn
</td>
<td>  exchanging pawns
</td></tr>
<tr>
<td colspan="3"> capturing with the knight
</td></tr>
<tr>
<td>  nxQ
</td>
<td>  winning queen
</td>
<td>  knight for queen
</td></tr>
<tr>
<td>  nxR
</td>
<td>  winning rook
</td>
<td>  winning the exchange
</td></tr>
<tr>
<td>  nxB
</td>
<td>  winning bishop
</td>
<td>  exchanging minors
</td></tr>
<tr>
<td>  nxN
</td>
<td>  winning knight
</td>
<td>  exchanging minors
</td></tr>
<tr>
<td>  nxP
</td>
<td>  winning pawn
</td>
<td>  losing knight for pawn
</td></tr>
<tr>
<td colspan="3"> capturing with the bishop
</td></tr>
<tr>
<td>  bxQ
</td>
<td>  winning queen
</td>
<td>  bishop for queen
</td></tr>
<tr>
<td>  bxR
</td>
<td>  winning rook
</td>
<td>  winning the exchange
</td></tr>
<tr>
<td>  bxB
</td>
<td>  winning bishop
</td>
<td>  exchanging minors
</td></tr>
<tr>
<td>  bxN
</td>
<td>  winning knight
</td>
<td>  exchanging minors
</td></tr>
<tr>
<td>  bxP
</td>
<td>  winning pawn
</td>
<td>  losing bishop for pawn
</td></tr>
<tr>
<td colspan="3"> capturing with the rook
</td></tr>
<tr>
<td>  rxQ
</td>
<td>  winning queen
</td>
<td>  rook for queen
</td></tr>
<tr>
<td>  rxR
</td>
<td>  winning rook
</td>
<td>  exchanging rooks
</td></tr>
<tr>
<td>  rxB
</td>
<td>  winning bishop
</td>
<td>  losing exchange
</td></tr>
<tr>
<td>  rxN
</td>
<td>  winning knight
</td>
<td>  losing exchange
</td></tr>
<tr>
<td>  rxP
</td>
<td>  winning pawn
</td>
<td>  losing rook for pawn
</td></tr>
<tr>
<td colspan="3"> capturing with the queen
</td></tr>
<tr>
<td>  qxQ
</td>
<td>  winning queen
</td>
<td>  exchanging queens
</td></tr>
<tr>
<td>  qxR
</td>
<td>  winning rook
</td>
<td>  losing queen for rook
</td></tr>
<tr>
<td>  qxB
</td>
<td>  winning bishop
</td>
<td>  losing queen for bishop
</td></tr>
<tr>
<td>  qxN
</td>
<td>  winning knight
</td>
<td>  losing queen for knight
</td></tr>
<tr>
<td>  qxP
</td>
<td>  winning pawn
</td>
<td>  losing queen for pawn
</td></tr>
<tr>
<td colspan="3"> capturing with the king, always winning captures
</td></tr>
<tr>
<td>  kxQ
</td>
<td>  winning queen
</td>
<td>
</td></tr>
<tr>
<td>  kxR
</td>
<td>  winning rook
</td>
<td>
</td></tr>
<tr>
<td>  kxB
</td>
<td>  winning bishop
</td>
<td>
</td></tr>
<tr>
<td>  kxN
</td>
<td>  winning knight
</td>
<td>
</td></tr>
<tr>
<td>  kxP
</td>
<td>  winning pawn
</td>
<td>
</td></tr></tbody></table>

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

