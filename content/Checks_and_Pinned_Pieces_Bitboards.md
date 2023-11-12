---
title: Checks and Pinned Pieces Bitboards
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * Checks and Pinned Pieces**

This is about whether the [king](King "King") is in [check](Check "Check"). If so, one likely uses a specialized check evasion [move generator](Move_Generation "Move Generation"). One may also trigger search [extensions](Extensions "Extensions") - based on the king is in check - or based on the check evasion move generator only reports one valid move. Related to determining [discovered check](Discovered_Check "Discovered Check") is to look for [absolute pins](Pin#AbsolutePin "Pin").

## Checks

Whether the king is in check may be determined on the fly by looking up attacks to the king square - or based on the last move made by the other, probably checking side. Another option is to determine check giving moves already at generation time, and to flag moves accordantly.

## On the Fly

Whether a king is in check can be determined by the attacked-routine mentioned in [Square Attacked By](Square_Attacked_By#AnyAttackBySide "Square Attacked By"). We pass the square of the king and opposite [color](Color "Color") for the potential attackers.

If one needs the set of attackers, either empty, single or double populated - one likely better relies on a specialized [attacksTo-routine](Square_Attacked_By#ByAllPieces "Square Attacked By") for each side, e.g. as member of the [standard bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition"):

```C++

U64 CBoard::attacksToKing(enumSquare squareOfKing, enumColor colorOfKing) {
   U64 opPawns, opKnights, opRQ, opBQ;
   opPawns     = pieceBB[nBlackPawn   - colorOfKing];
   opKnights   = pieceBB[nBlackKnight - colorOfKing];
   opRQ = opBQ = pieceBB[nBlackQueen  - colorOfKing];
   opRQ       |= pieceBB[nBlackRook   - colorOfKing];
   opBQ       |= pieceBB[nBlackBishop - colorOfKing];
   return (arrPawnAttacks[colorOfKing][squareOfKing] & opPawns)
        | (arrKnightAttacks[squareOfKing]            & opKnights)
        | (bishopAttacks (occupiedBB, squareOfKing)  & opBQ)
        | (rookAttacks   (occupiedBB, squareOfKing)  & opRQ)
        ;
}

```

## By Move

Another idea is to determine the check inside the search-routine by the last [move](Moves "Moves") done by the opponent. It might be a direct or discovered [check](Check "Check") - or in case of [double check](Double_Check "Double Check"), both. With bitboards the possible savings to determine checks by last move seems negligible - and one probably better relies on the branch-less [on the fly solution](</Checks_and_Pinned_Pieces_(Bitboards)#ChecksOnTheFly> "Checks and Pinned Pieces (Bitboards)"), since we may reuse the rook-wise and bishop-wise attacks for other purposes - like determining absolute pinned pieces, kingsafety-evaluation, and/or whether the opponent side threatens checks or discovered checks.

### Direct Check

For the direct check we may use the routine mentioned in [Square Attacked By](Square_Attacked_By#AttackedByPieceOnSquare "Square Attacked By"):

```C++

if ( isAttacked(squareOfKing, move.to, move.piece(), occupiedBB) ) -> direct check

```

### Discovered Check

One solution is to determine the [direction](Direction "Direction") between the [from-square](Origin_Square "Origin Square") and the king square (e.g. by 0x88 difference). If both squares share a common line, one calls an appropriate sliding ray- or line-attack getter with king square and occupancy, to look whether this set intersects the possible opponing sliders of that ray. One also has to prove, whether a possible true result was not caused by a direct check of a sliding capture.

## Absolute Pins

To detect [absolute pins](Pin#AbsolutePin "Pin") is necessary for [legal](Legal_Move "Legal Move") [move generation](Move_Generation "Move Generation") and may be considered in [evaluation](Evaluation "Evaluation"). While there are different approaches, the most common for programs based on single sliding piece attacks rather than direction wise set-wise attack getter, relies on the [xrayRookAttacks](</X-ray_Attacks_(Bitboards)#ModifyingOccupancy> "X-ray Attacks (Bitboards)") or [xrayBishopAttacks](</X-ray_Attacks_(Bitboards)#ModifyingOccupancy> "X-ray Attacks (Bitboards)") routines - called with square of own king and own pieces as blockers. An [in-between lookup](Square_Attacked_By#Obstructed "Square Attacked By") (Obstructed) determines the set of pinned pieces while [traversing](Bitboard_Serialization "Bitboard Serialization") the pinning pieces <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

```C++

pinned = 0;
pinner = xrayRookAttacks(occupiedBB, ownPieces, squareOfKing) & opRQ;
while ( pinner ) {
   int sq  = bitScanForward(pinner);
   pinned |= obstructed(sq, squareOfKing) & ownPieces;
   pinner &= pinner - 1;
}
pinner = xrayBishopAttacks(occupiedBB, ownPieces, squareOfKing) & opBQ;
while ( pinner ) {
   int sq  = bitScanForward(pinner);
   pinned |= obstructed(sq, squareOfKing) & ownPieces;
   pinner &= pinner - 1;
}

```

## Opposite Ray-Directions

Another idea to determine absolute pins as well as distant check block-targets, or possible discovered check origins, is to apply disjoint direction-wise attacks, as demonstrated in the [DirGolem](DirGolem "DirGolem") proposal, where this technique is used for all eight ray-directions. The intersection of direction attacks of potential pinning sliding pieces with the opposite ray-direction attacks of the king treated as sliding super piece, gains enough information if further intersected by empty squares, own, or opponent pieces. For instance as illustrated with a black rook and white king on the same rank, with no, one and two pieces inbetween:

No obstruction, king in check. In-between intersection consists of empty squares as target set to block the distant check:

```C++

     . r . . . . K .     
r->  . . 1 1 1 1 1 .      
<-K  . 1 1 1 1 1 . .
&    . . 1 1 1 1 . .  

```

One piece in-between. Intersection leaves a pinned piece if of king color, otherwise a possible discovered checker:

```C++

     . r . . x . K .  
r->  . . 1 1 1 . . .             
<-K  . . . . 1 1 . .
&    . . . . 1 . . .

```

Two (or more) pieces in-between. Intersection is null:

```C++

      . r . x x . K .  
r->   . . 1 1 . . . .
<-K   . . . . 1 1 . .
&     . . . . . . . .   

```

## See also

- [Check](Check "Check")
- [DirGolem](DirGolem "DirGolem")
- [Discovered Check](Discovered_Check "Discovered Check")
- [Double Check](Double_Check "Double Check")
- [Pin](Pin "Pin")

## Forum Posts

- [Fast check detection in bitboard engine](https://www.stmintz.com/ccc/index.php?id=334869) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), December 10, 2003
- [Bitboards and inCheck](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6064&p=29127) by [Andreas Guettinger](Andreas_Guettinger "Andreas Guettinger"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2007
- [Bitboard of Pinned Pieces](http://www.talkchess.com/forum/viewtopic.php?t=22550) by [Grant Osborne](Grant_Osborne "Grant Osborne"), [CCC](CCC "CCC"), July 24, 2008
- [Check detection and move generation using bitboards](http://www.talkchess.com/forum/viewtopic.php?t=41351) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), December 06, 2011
- [Pinned Pieces With Bitboards](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79617) by Andrew Zhuo, [CCC](CCC "CCC"), April 01, 2022

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Pinned Pieces With Bitboards](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79617&start=2) by tcusr, [CCC](CCC "CCC"), April 01, 2022

[Up one Level](Bitboards "Bitboards")

