---
title: SEE  The Swap Algorithm
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* SEE - The Swap Algorithm**


The [iterative](Iteration "Iteration") [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") Swap-Algorithm in Bitboards creates a swap-list of best case [material](Material "Material") gains by traversing a [square attacked/defended by](Square_Attacked_By "Square Attacked By") set in least valuable piece order from [pawn](Pawn "Pawn"), [knight](Knight "Knight"), [bishop](Bishop "Bishop"), [rook](Rook "Rook"), [queen](Queen "Queen") until [king](King "King"), with alternating sides. The swap-list, an unary tree since there are no branches but just a series of captures, is [negamaxed](Negamax "Negamax") for a final static exchange evaluation <a id="cite-note-1" href="#cite-ref-1">[1]</a><a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### Contents


* [1 Traversal of To-Attacks](#traversal-of-to-attacks)
* [2 SEE a Capture](#see-a-capture)
* [3 Pseudo C-Code](#pseudo-c-code)
* [4 Traces](#traces)
	+ [4.1 Position 1](#position-1)
	+ [4.2 Position 2](#position-2)
* [5 See also](#see-also)
* [6 Forum Posts](#forum-posts)
	+ [6.1 2000 ...](#2000-...)
	+ [6.2 2010 ...](#2010-...)
	+ [6.3 2020 ...](#2020-...)
* [7 References](#references)






Assuming this arbitrary [Board-Definition](Bitboard_Board-Definition#CBoardDef "Bitboard Board-Definition") with color as least significant piece bit and "even" pieces are the white ones, following routine returns a single populated square set and passes the least valuable piece per [C++](Cpp "Cpp") reference to the caller. If no more piece is found for the appropriate side, it returns an empty set.




```

U64 Board::getLeastValuablePiece(U64 attadef, int bySide, int &piece)
{
   for (piece = nWhitePawn + bySide; piece <= nWhiteKing + bySide; piece += 2) {
      U64 subset = attadef & pieceBB[piece];
      if ( subset )
         return subset & -subset; // single bit
   }
   return 0; // empty set
}

```

## SEE a Capture


The first two members of the gain swap-list are likely determined by the [capture move](Captures "Captures") we like to prove. Thus, the first element of the swap-list is the value of the target piece, while the second is only written (or used) if the target square is further defended. In this case it is the value of the capturing piece minus the value of captured piece, this is the best-case material gain from the defending point of view. However during traversal, [X-ray attacks](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)") are considered while capturing with a piece, which may have indirect attacks or defends behind, which unions the set of attackers and defenders. 



## Pseudo C-Code



```

int Board::see ( enumSquare toSq, enumPiece target, enumSquare frSq, enumPiece aPiece)
{
   int gain[32], d = 0;
   U64 mayXray = pawns | bishops | rooks | queen;
   U64 fromSet = 1ULL << frSq;
   U64 occ     = occupiedBB;
   U64 attadef = attacksTo( occ, toSq );
   gain[d]     = value[target];
   do {
      d++; // next depth and side
      gain[d]  = value[aPiece] - gain[d-1]; // speculative store, if defended
      if (max (-gain[d-1], gain[d]) < 0) break; // pruning does not influence the result
      attadef ^= fromSet; // reset bit in set to traverse
      occ     ^= fromSet; // reset bit in temporary occupancy (for x-Rays)
      if ( fromSet & mayXray )
         attadef |= considerXrays(occ, ..);
      fromSet  = getLeastValuablePiece (attadef, d & 1, aPiece);
   } while (fromSet);
   while (--d)
      gain[d-1]= -max (-gain[d-1], gain[d])
   return gain[0];
}

```

Considering [X-ray attacks](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)") leaves some implementation details left, dependent on what sliding attack-getter is handy, [ray attacks](Classical_Approach "Classical Approach") are sufficient, but requires some effort to determine the ray-direction. With [Magic Bitboards](Magic_Bitboards "Magic Bitboards") one will likely use something similar as the sliding piece subset of [Square Attacked By](Square_Attacked_By "Square Attacked By"). The preliminary pruning of the swap-list fill (if (max (-gain[d-1], gain[d]) < 0) break;) and other improvements were proposed by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Traces


Two positions with traces of the swap-list during traversal and negamaxing with some arbitrary [piece values](Material "Material").



### Position 1


To demonstrate how SEE works in obvious cases, is Rook takes Pawn a winning capture?





|  |
| --- |
|                                                                                    ♚ ♜     ♟♟    ♟♟           ♟           ♙     ♙  ♙♙    ♙  ♔ ♖    |



```
1k1r4/1pp4p/p7/4p3/8/P5P1/1PP4P/2K1R3 w - - ; Rxe5?

```


```

gain[0]  =  100 ; win for white if black pawn e5 is en-prise by rxp
gain[1]  =  400 ; win for black if white rook e5 is en-prise,  500-100, speculative store
no further attacks for black at depth 1
-> SEE(rxe5) == 100

```

### Position 2


This position covers a more complicated case with X-rays. Is Knight takes pawn a winning capture?





|  |
| --- |
|                                                                              ♚ ♜   ♛ ♟♟♞   ♟♟    ♝      ♟           ♙  ♘  ♙  ♙♙ ♖ ♗♙  ♔ ♕    |



```
1k1r3q/1ppn3p/p4b2/4p3/8/P2N2P1/1PP1R1BP/2K1Q3 w - - ; Nxe5?

```


```

gain[0] =  100 ; win for white if black pawn   e5 is en-prise by nxp
gain[1] =  225 ; win for black if white knight e5 is en-prise by nxn,  325- 100
gain[2] =  100 ; win for white if black knight e5 is en-prise by rxn,  325- 225 -> x-rays includes queen e1
gain[3] =  400 ; win for black if white rook   e5 is en-prise by bxr,  500- 100 -> x-rays includes queen h8
gain[4] =  -75 ; win for white if black bishop e5 is en-prise by qxb,  325- 400
gain[5] = 1075 ; win for black if white queen  e5 is en-prise by qxq, 1000- -75
gain[6] =  -75 ; win for white if black queen  e5 is en-prise,        1000-1075 speculative store
no further attacks for white at depth = 6

gain[4] = -max(--75,  1075) = -1075
gain[3] = -max(-400, -1075) =   400
gain[2] = -max(-100,   400) =  -400
gain[1] = -max(-225,  -400) =   225
gain[0] = -max(-100,   225) =  -225
-> SEE(nxe5) == -225

```

## See also


* [Ed's Lookup](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps") from [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [MVV-LVA](MVV-LVA "MVV-LVA")
* [SOMA](SOMA "SOMA")
* [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


## Forum Posts


### 2000 ...


* [Static Exchange Eval](https://www.stmintz.com/ccc/index.php?id=178979) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), August 02, 2001
* [Does swap of Crafty find bad promotions](https://www.stmintz.com/ccc/index.php?id=341658) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 11, 2004
* [Re: WBEC Ridderkerk new results](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46486&p=176048#p176025) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2004 » [DanChess](DanChess "DanChess")
* [SEE with magic bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?t=6104) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2007 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Re: Movei added to Crafty vs Rybka comaprison data](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=123511&t=14168) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), June 06, 2007


### 2010 ...


* [Question about SEE algorithm on Chessprogramming Wiki](http://www.talkchess.com/forum/viewtopic.php?t=31479) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), January 05, 2010
* [Implementing SEE](http://www.talkchess.com/forum/viewtopic.php?t=40046) by colin, [CCC](CCC "CCC"), Aug 12, 2011


 [Re: Implementing SEE](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=419174&t=40046) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), August 13, 2011
* [SEE with alpha beta](http://www.talkchess.com/forum/viewtopic.php?t=40054) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), August 14, 2011 » [Onno](Onno "Onno")
* [pin-aware see](https://groups.google.com/d/msg/fishcooking/S_4E_Xs5HaE/mS3VTnuEFgAJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2016 » [Pin](Pin "Pin"), [Stockfish](Stockfish "Stockfish")
* [Illegal moves in SEE](https://groups.google.com/d/msg/fishcooking/9mcmjnyqbAQ/S6mDA0QsAAAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2016 » [Stockfish](Stockfish "Stockfish")
* [Problems with SEE](http://www.talkchess.com/forum/viewtopic.php?t=64166) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 03, 2017


### 2020 ...


* [SEE versus SEE\_GE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72862) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), January 21, 2020
* [Static exchange evaluation with promotion](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77787) by Guido Flohr, [CCC](CCC "CCC"), July 23, 2021


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Subject: Re: Static Exchange Eval](https://www.stmintz.com/ccc/index.php?id=178981) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") from [CCC](Computer_Chess_Forums "Computer Chess Forums"), August 02, 2001
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Crafty](Crafty "Crafty") by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), see ***swap.c***
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: SEE with alpha beta](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=419315&t=40054) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), August 14, 2011

**[Up one Level](Bitboards "Bitboards")**







 
