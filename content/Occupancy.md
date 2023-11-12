---
title: Occupancy
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Squares](Squares "Squares") \* Occupancy**



 [](File:ZappaBesetzt20160916.JPG) Occupied <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
The **Occupancy** refers to the boolean property of a square. It is occupied if any [piece](Pieces "Pieces") exclusively resides on that square, otherwise the square is empty. In [bitboards](Bitboards "Bitboards"), the occupancy or *occupied bitboard* refers the set of all squares occupied by any piece. Thus, it is the [union](General_Setwise_Operations#Union "General Setwise Operations") of all [piece bitboards](Bitboard_Board-Definition "Bitboard Board-Definition"), which is used for instance in calculating [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Likely, while the piece bitboards are [updated incrementally](Incremental_Updates "Incremental Updates"), the occupancy is updated incrementally as well, rather than calculated from up to 12 piece bitboards each time.


Alternatively, if needed more often, the [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") set of the occupancy, the set of **all empty squares** is exclusively kept inside the board-definition and a cheap not-instruction is done to calculate the occupancy on the fly. Other programs keep disjoint white and black pieces, to "or" them if the occupancy is actually needed. The appearance of multiple, redundant occupied bitboards, which are [flipped, mirrored or rotated](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") are eponym of bitboard methods related to [sliding piece attack generation](Sliding_Piece_Attacks "Sliding Piece Attacks"), most notably [rotated](Rotated_Bitboards "Rotated Bitboards") and [reverse bitboards](Reverse_Bitboards "Reverse Bitboards"). 



## Forum Posts


* [Occupancy Variations](http://www.open-chess.org/viewtopic.php?f=5&t=2240) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2013 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


## External Links


* [Occupancy from Wikipedia](https://en.wikipedia.org/wiki/Occupancy)
* [occupancy - Wiktionary](https://en.wiktionary.org/wiki/occupancy)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Besetzt!](https://de-de.facebook.com/umspannwerk.recklinghausen/posts/10153757793891429) (Occupied) - [Toilet](https://en.wikipedia.org/wiki/Toilet) exhibition at [Umspannwerk Recklinghausen](https://de.wikipedia.org/wiki/Umspannwerk_Recklinghausen), today [RWE](https://en.wikipedia.org/wiki/RWE) [Technology museum](https://en.wikipedia.org/wiki/Technology_museum) in [Recklinghausen](https://en.wikipedia.org/wiki/Recklinghausen), Germany, and part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr) - [Portable toilet](https://en.wikipedia.org/wiki/Toilet#Others) labeled Rock:Klo with [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") [Toilet Poster](http://wiki.killuglyradio.com/wiki/The_Toilet_Poster) inside, Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), September 16, 2016

**[Up one Level](Squares "Squares")**







 
