---
title: QBBEngine
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* QBBEngine**



[ A KTM Quad 990 ATV <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**QBBEngine**,  

a didactic [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), written in [C](C "C") and published as single source file along with [Pedone](Pedone "Pedone"), which apparently uses a similar representation <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The QBBEngine demonstrates the use of a compact [quad-bitboard](Quad-Bitboards "Quad-Bitboards") structure to [represent the board](Board_Representation "Board Representation"), 
and further applies [alpha-beta search](Alpha-Beta "Alpha-Beta") and an [evaluation](Evaluation "Evaluation") based on static values and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The program performs a color agnostic [move generation](Move_Generation "Move Generation") by [flipping](Color_Flipping "Color Flipping") the board each time in [make move](Make_Move "Make Move").



### Contents


* [1 Board-Definition](#board-definition)
	+ [1.1 C Structure](#c-structure)
	+ [1.2 Piece Coding](#piece-coding)
* [2 See also](#see-also)
* [3 External Links](#external-links)
* [4 References](#references)






### C Structure



```

/*
Board structure definition

PM,P0,P1,P2 are the 4 bitboards that contain the whole board
PM is the bitboard with the side to move pieces
P0,P1 and P2: with these bitboards you can obtain every type of pieces and every pieces combinations.
*/
typedef struct
{
   TBB PM;
   TBB P0;
   TBB P1;
   TBB P2;
   uint8_t CastleFlags; /* ..sl..SL  short long opponent SHORT LONG side to move */
   uint8_t EnPassant; /* enpassant column, =8 if not set */
   uint8_t Count50; /* 50 move rule counter */
   uint8_t Rep; /* 0 if it's not a repetition, 1 if it is */
   uint8_t STM; /* side to move */
} TBoard;

```

### Piece Coding


The [board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") with vertical [nibbles](Nibble "Nibble") as [piece or empty square codes](Pieces#PieceCoding "Pieces"), i.e. the [initial position](Initial_Position "Initial Position"):





|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Square
 |  6
 |  6
 |  6
 |  6
 |  5
 |  5
 |  5
 |  5
 |  5
 |  ~
 |  0
 |  ...
 |  |  |  |  |  |  |  0
 |
|  3
 |  2
 |  1
 |  0
 |  9
 |  8
 |  7
 |  6
 |  5
 |  ~
 |  8
 |  7
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |
|  Piece
 |  r
 |  n
 |  b
 |  k
 |  q
 |  b
 |  n
 |  r
 |  p
 |  ~
 |  P
 |  R
 |  N
 |  B
 |  K
 |  Q
 |  B
 |  N
 |  R
 |
|  PM
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |  ~
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  1
 |  Side to Move
 |
|  P0
 |  0
 |  0
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  ~
 |  1
 |  0
 |  0
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  |  P
 |  .
 |  B
 |  .
 |  Q
 |  |
|  P1
 |  0
 |  1
 |  1
 |  1
 |  0
 |  1
 |  1
 |  0
 |  0
 |  ~
 |  0
 |  0
 |  1
 |  1
 |  1
 |  0
 |  1
 |  1
 |  0
 |  |  |  N
 |  B
 |  .
 |  |  K
 |
|  P2
 |  1
 |  0
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  0
 |  ~
 |  0
 |  1
 |  0
 |  0
 |  1
 |  1
 |  0
 |  0
 |  1
 |  |  |  .
 |  .
 |  R
 |  Q
 |  K
 |



```

P2     RQK        P1    NB  K       P0   P B Q         PM side to move
1 . . 1 1 . . 1   . 1 1 . 1 1 1 .   . . 1 1 . 1 . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   1 1 1 1 1 1 1 1    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .    . . . . . . . .
. . . . . . . .   . . . . . . . .   1 1 1 1 1 1 1 1    1 1 1 1 1 1 1 1
1 . . 1 1 . . 1   . 1 1 . 1 1 1 .   . . 1 1 . 1 . .    1 1 1 1 1 1 1 1

```

## See also


* [Pedone](Pedone "Pedone")


## External Links


* [QBBEngine - a didactic engine](https://sites.google.com/site/pedonechess/a-didactic-engine)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [A KTM Quad 990 ATV](https://commons.wikimedia.org/wiki/File:KTM_Quad_990_neutral.jpg), custom-made from E-ATV Eicker Germany, Basevehicle was a KTM Supermotobike, Typ SM 990 with LC8 engine, Image by [Stefan Krause](https://commons.wikimedia.org/wiki/User:Ritchyblack), February 20, 2011, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Pedone Chess Engine](https://sites.google.com/site/pedonechess/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [QBBEngine - a didactic engine](https://sites.google.com/site/pedonechess/a-didactic-engine)

**[Up one Level](Engines "Engines")**







 
