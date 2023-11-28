---
title: Pin
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Tactics](Tactics "Tactics") \* Pin**


A **Pin** is a [X-ray](X-ray "X-ray") related situation where a [sliding piece](Sliding_Pieces "Sliding Pieces"), a [bishop](Bishop "Bishop"), a [rook](Rook "Rook") or a [queen](Queen "Queen") indirectly attacks an opponent [king](King "King") or piece potentially [en prise](En_prise "En prise"), shielded by another directly attacked opponent piece or pawn on the attacking [ray](Rays "Rays"). The direct attacked piece or pawn is then called **pinned**, and cannot move out of the line of attack, without leaving the indirectly attacked piece [en prise](En_prise "En prise") or illegally its own king in [check](Check "Check"). All pieces except the king may be pinned. One tactic which takes advantage of a pin is called *working the pin*, where other pieces from the pinning piece's side attack the opposing pinned piece.




### Absolute Pin


The absolute pin is where the piece shielded by the pinned piece is the king. In chess programming, to detect absolute pins is necessary for [legal](Legal_Move "Legal Move") [move generation](Move_Generation "Move Generation") and may be considered in [evaluation](Evaluation "Evaluation").




### Partial Pin


A partial pin refers to (absolute) pins, where the pinned piece or pawn can move along the attacking [direction](Direction "Direction"), and may even capture the pinning sliding piece.




### Relative Pin


A relative pin is where the piece shielded by the pinned piece is not the king, but either a more valuable than the pinned piece, or conditionally en prise.



### Cross Pin


A cross pin describes the rare case, where one piece is pinned in multiple directions simultaneously, most often one partial pin shielding the king and a relative pin shielding the queen. For instance in the otherwise harmless case of a partial pin of a bishop by a bishop, the bishop is also shielding a otherwise hanging queen by a queen, same may apply for rooks instead of bishops. Here the black rook on e4 is cross pinned and black will lose material and likely the game:


<img src="https://lichess1.org/export/fen.gif?fen=4k3/1p4pp/2p5/8/q3r2Q/3p3P/1P4PK/4R3 b - - " style="
    width: 300px;
">

```
4k3/1p4pp/2p5/8/q3r2Q/3p3P/1P4PK/4R3 b - - 
```


Of course with the white king on g1 or h1, things would be different. Such multiple issue tactics seems all the domain of the [search](Search "Search") and is hard to evaluate statically. 



### Situational Pin


This kind of relative pin is not about shielding own pieces, but important squares, for instance where an opponent rook may have a [back rank mate](Mate_at_a_Glance#MatesWithSlidingPieces "Mate at a Glance"). This kind of pins are usually only considered implicit by the search.



## Considering Pins


Pinned pieces may be considered inside a chess program's [move generation](Move_Generation "Move Generation") and [evaluation](Evaluation "Evaluation").



### Move Generation


[Legal Move](Legal_Move "Legal Move") generation requires information about absolute pinned pieces, and their pinning direction to cover partial pins. Even non strictly legal move generation may reduce the number of generated illegal moves if considering absolute and partial pinnes, while ignoring the legality of [En passant](En_passant "En passant") captures and [castling](Castling "Castling").



### Evaluation


Evaluation can take the restricted [mobility](Mobility "Mobility") of pinned pieces into account, and should consider the [distance](Distance "Distance") of the pinned pieces to its shielded king (or queen for relative pins) and whether it is on the own or opponent half of the board during the [opening](Opening "Opening") or [middlegame](Middlegame "Middlegame"). Some programs even calculate on *working the pin*, to look whether pinned pieces may further attacked by other pieces, especially pawns, for instance with [bitboards](Bitboards "Bitboards") whether they [intersect](General_Setwise_Operations#Intersection "General Setwise Operations") opponent none-guarded pawn [front attack spans](Attack_Spans "Attack Spans") and assign appropriate evaluation penalties.



## See also


* [Checks and Pinned Pieces (Bitboards)](Checks_and_Pinned_Pieces_(Bitboards) "Checks and Pinned Pieces (Bitboards)")
* [En passant](En_passant "En passant")
* [Legal Move](Legal_Move "Legal Move")
* [Move Generation](Move_Generation "Move Generation")
* [Skewer](Skewer "Skewer")
* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks")
* [X-ray](X-ray "X-ray")
* [X-ray Attacks (Bitboards)](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")


## Forum Posts


### 2000 ...


* [Question about the KnightCap find\_pins function](https://www.stmintz.com/ccc/index.php?id=306311) by Matthew White, [CCC](CCC "CCC"), July 14, 2003 » [KnightCap](KnightCap "KnightCap")
* [Evaluating Pinned Pieces](https://www.stmintz.com/ccc/index.php?id=366095) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), May 19, 2004
* [SEE and pin detection](https://www.stmintz.com/ccc/index.php?id=385126) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), August 30, 2004 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Pin aware SEE](https://www.stmintz.com/ccc/index.php?id=390108) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), October 03, 2004
* [Bitboard of Pinned Pieces](http://www.talkchess.com/forum/viewtopic.php?t=22550) by [Grant Osborne](Grant_Osborne "Grant Osborne"), [CCC](CCC "CCC"), July 24, 2008


### 2010 ...


* [LVA MVV with relative Pin](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=395213) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), February 16, 2011 » [MVV-LVA](MVV-LVA "MVV-LVA")
* [pinned pieces in eval](http://www.talkchess.com/forum/viewtopic.php?t=40597) by Pierre Bokma, [CCC](CCC "CCC"), October 01, 2011
* [Pinned pieces in king safety](https://groups.google.com/d/msg/fishcooking/lIjQUH3dsYg/4VEtHUkrdBsJ) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2014 » [King Safety](King_Safety "King Safety"), [Stockfish](Stockfish "Stockfish")
* [pin-aware see](https://groups.google.com/d/msg/fishcooking/S_4E_Xs5HaE/mS3VTnuEFgAJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2016 » [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), [Stockfish](Stockfish "Stockfish")


## External Links


* [Pin (chess) from Wikipedia](https://en.wikipedia.org/wiki/Pin_%28chess%29)
* [Top 10 chess: Tactical Motif VII: The pin](http://www.top10chess.com/2008/09/tactical-motif-vii-pin.html)
* [The Pin and the Skewer](http://www.chesstactics.org/index.php?Type=page&Action=none&From=4,1,1,1) from [Ward Farnsworth's Predator at the Chessboard](http://www.chesstactics.org/)
* [The Searchers](Category:The_Searchers "Category:The Searchers") - [Needles and Pins](https://en.wikipedia.org/wiki/Needles_and_Pins_(song)) (1964), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
**[Up one Level](Tactics "Tactics")**







 
