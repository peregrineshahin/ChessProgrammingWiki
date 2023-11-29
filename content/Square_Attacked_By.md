---
title: Square Attacked By
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Square Attacked By**



 [](https://www.chessprogramming.org/File:L%27Ange_du_Foyeur.jpg) [Max Ernst](Category:Max_Ernst "Category:Max Ernst") - L'Ange du Foyer, 1937 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Square Attacked By**,  

determines whether a [square](Squares "Squares") is [attacked](Attacks "Attacks") and/or defended by various or specific [pieces](Pieces "Pieces"). So far, as elaborated in [pawn](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")-, [knight](Knight_Pattern "Knight Pattern")- and [king pattern](King_Pattern "King Pattern"), as well as [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), we are able to generate all attacks and target-sets of all pieces, sufficient to [generate](Move_Generation "Move Generation") all [pseudo legal moves](Pseudo-Legal_Move "Pseudo-Legal Move"). It is often useful to generate [attacks](Attacks "Attacks") **to** a certain square, or to look whether [moves](Moves "Moves") retrieved elsewhere are pseudo legal or [legal](Legal_Move "Legal Move"). Some programs maintain [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") for that purpose. The techniques proposed on this page are intended to use on the fly. 



### By all Pieces


A common approach is to put a **super-piece** on the to-square, to look up all kind of piece-type attacks from there and to [intersect](General_Setwise_Operations#Intersection "General Setwise Operations") them with all appropriate pieces able to attack that square. Note that white pawn attacks intersect black pawns and vice versa. Knights, kings and sliders are considered as [union](General_Setwise_Operations#Union "General Setwise Operations") of both sides. The set of all attacking and defending pieces is the union of all piece-attack intersections. Assuming a [C++](Cpp "Cpp") member function of a [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition") class. [Robert Hyatt](Robert_Hyatt "Robert Hyatt") further checks whether there are any sliding pieces on relevant rays at all, in order to save calling the attack getter in case there are none <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++

U64 CBoard::attacksTo(U64 occupied, enumSquare sq) {
   U64 knights, kings, bishopsQueens, rooksQueens;
   knights        = pieceBB[nWhiteKnight] | pieceBB[nBlackKnight];
   kings          = pieceBB[nWhiteKing]   | pieceBB[nBlackKing];
   rooksQueens    =
   bishopsQueens  = pieceBB[nWhiteQueen]  | pieceBB[nBlackQueen];
   rooksQueens   |= pieceBB[nWhiteRook]   | pieceBB[nBlackRook];
   bishopsQueens |= pieceBB[nWhiteBishop] | pieceBB[nBlackBishop];

   return (arrPawnAttacks[nWhite][sq] & pieceBB[nBlackPawn])
        | (arrPawnAttacks[nBlack][sq] & pieceBB[nWhitePawn])
        | (arrKnightAttacks      [sq] & knights)
        | (arrKingAttacks        [sq] & kings)
        | (bishopAttacks(occupied,sq) & bishopsQueens)
        | (rookAttacks  (occupied,sq) & rooksQueens)
        ;
}

```





### Any Attack by Side


If boolean information is required, whether a square is attacked by a side, one may use conditionals to return early. This might be useful to determine whether a [king is in check](Checks_and_Pinned_Pieces_(Bitboards) "Checks and Pinned Pieces (Bitboards)"). Assuming a [C++](Cpp "Cpp") member function of a [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition") class:




```C++

bool CBoard::attacked(U64 occupied, enumSquare square, enumColor bySide) {
   U64 pawns         = pieceBB[nWhitePawn   + bySide];
   if ( arrPawnAttacks[bySide^1][square]    & pawns )         return true;
   U64 knights       = pieceBB[nWhiteKnight + bySide];
   if ( arrKnightAttacks[square]            & knights )       return true;
   U64 king          = pieceBB[nWhiteKing   + bySide];
   if ( arrKingAttacks[square]              & king )          return true;
   U64 bishopsQueens = pieceBB[nWhiteQueen  + bySide]
                     | pieceBB[nWhiteBishop + bySide];
   if ( bishopAttacks(occupied, square)     & bishopsQueens ) return true;
   U64 rooksQueens   = pieceBB[nWhiteQueen  + bySide]
                     | pieceBB[nWhiteRook   + bySide];
   if ( rookAttacks  (occupied, square)     & rooksQueens )   return true;
   return false;
}

```





## Legality Test


One application inside a chess program, is to test whether a certain move is [psuedo-legal](Pseudo-Legal_Move "Pseudo-Legal Move"). This could be a [hash move](Hash_Move "Hash Move") probed from the [transposition table](Transposition_Table "Transposition Table"), or a [killer move](Killer_Move "Killer Move") supplied by the [killer heuristic](Killer_Heuristic "Killer Heuristic"). In [cut-nodes](Node_Types#cut-nodes "Node Types") one may save the complete move-generation by one legality test.




### In Between


Assuming otherwise legal from-to coordinates, it is about distant moves of [sliding pieces](Sliding_Pieces "Sliding Pieces") (and [double pawn push](Pawn_Push#DoublePush "Pawn Push") and [castling](Castling "Castling")) - whether a square between from and to is obstructed or not. One obvious solution is to switch on piece-type and call the appropriate attack- or move-target getter by from-square, to see whether the target bit is set. For a queen that may take quite some instructions for up to four sliding lines, thus there seems to be a cheaper solution.




### Rectangular Lookup


The common approach is to lookup a two-dimensional 64 times 64 [array](Array "Array"), initialized with empty sets and appropriate in-between sets for distant squares on the same line. If the intersection of in-between sets with the [occupancy](Occupancy "Occupancy") is empty, there are no obstructions, and the move is considered pseudo legal. This is implicitly true for squares in king- and knight distance as well, since they already contain zero. 




```C++

U64 arrRectangular[64][64]; // 4096*8 = 32KByte

U64 inBetween(enumSquare from, enumSquare to) {
   return arrRectangular[from][to];
}

bool mayMove(enumSquare from, enumSquare to, U64 occ) {
   return (inBetween(from, to) & occ) == 0;
}

```

That looks cheap, and likely is the fastest for recent processor architectures, but 32KByte is just another thing competing with the caches. Three further [space-time tradeoffs](Space-Time_Tradeoff "Space-Time Tradeoff") are mentioned, triangular lookup, 0x88 difference and rotate, and pure calculation.




### Triangular Lookup


Due to the [commutative property](https://en.wikipedia.org/wiki/Commutative_property) of from- and to-squares, each in-between set is stored twice in the 64x64 array. [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") once suggested to roughly half the table-size by making the rectangle a triangle, and already noted "*Not sure that it will make sense, as index code will be more complex*" <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Applying [max](Avoiding_Branches#Max "Avoiding Branches") and [min](Avoiding_Branches#Min "Avoiding Branches") by sign-mask, and some packing with the [triangular number](https://en.wikipedia.org/wiki/Triangular_number), following index calculation may be used:




```C++

U64 arrTriangular[64*65/2];

int triangularIndex(int a, int b) {
   int d = a - b; /* difference */
   d &= d >> 31;  /* only if negative */
   b += d;        /* min */
   a -= d;        /* max */
   b *= b ^ 127;  /* min * (127-min)  ... */
   return (b>>1) + a; /* ... /2 + max */
}

U64 inBetween(enumSquare from, enumSquare to) {
   return arrTriangular[ triangularIndex(from, to) ];
}

```





### 0x88 Difference


What about a translation of one square (the smallest) to a1 and shifting the occupancy right? Unfortunately, the square difference is ambiguous according to the 8 [ray-](Direction "Direction") and 8 knight directions, +-7 occurs as rank- or anti-diagonal-difference, +-6 occurs as rank- and knight-difference. If we keep other stuff like [distance](Distance "Distance"), [Manhattan-distance](Manhattan-Distance "Manhattan-Distance"), [ray-direction](Direction "Direction") and so on - it might be worth to rely on [Vector Attacks](Vector_Attacks "Vector Attacks") or the difference of [0x88](0x88 "0x88") coordinates and their property of being unambiguous according to ray-direction and distance. By [rotating left](General_Setwise_Operations#Rotate "General Setwise Operations") the pre-calculated obstructions, the order of squares don't cares. [Don Dailey](Don_Dailey "Don Dailey") reported the 64x64 array lookup slightly faster, apparently inside [Komodo](Komodo "Komodo") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.:




```C++

U64 arrInBetweenBy0x88Diff[240]; // 1920 bytes, 2KByte - 128 Byte

unsigned int x88diff(enumSquare f, enumSquare t) {
   return t - f + (t|7) - (f|7) + 120;
}

U64 inBetween(enumSquare from, enumSquare to) {
   return rotateLeft(arrInBetweenBy0x88Diff[x88diff(from,to)], from);
}

```

### Pure Calculation


A branch-less solution without any lookups and some parallel gain is likely too expensive on the fly and may at most used for initialization purposes <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++

U64 inBetween(enumSquare sq1, enumSquare sq2) {
   const U64 m1   = C64(-1);
   const U64 a2a7 = C64(0x0001010101010100);
   const U64 b2g7 = C64(0x0040201008040200);
   const U64 h1b7 = C64(0x0002040810204080); /* Thanks Dustin, g2b7 did not work for c1-a3 */
   U64 btwn, line, rank, file;

   btwn  = (m1 << sq1) ^ (m1 << sq2);
   file  =   (sq2 & 7) - (sq1   & 7);
   rank  =  ((sq2 | 7) -  sq1) >> 3 ;
   line  =      (   (file  &  7) - 1) & a2a7; /* a2a7 if same file */
   line += 2 * ((   (rank  &  7) - 1) >> 58); /* b1g1 if same rank */
   line += (((rank - file) & 15) - 1) & b2g7; /* b2g7 if same diagonal */
   line += (((rank + file) & 15) - 1) & h1b7; /* h1b7 if same antidiag */
   line *= btwn & -btwn; /* mul acts like shift by smaller square */
   return line & btwn;   /* return the bits on that line in-between */
}

```

First, the in-between set as superset of the possible line-bits is calculated, excluding the "greater" square but including the "smaller", e.g. f6 and c3.




```C++

                                        btwn including c3
-1<<f6              -1<<c3                   excluding f6
1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     . . . . . . . .
1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     . . . . . . . .
. . . . . 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 . . .
. . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1
. . . . . . . .  ^  1 1 1 1 1 1 1 1  =  1 1 1 1 1 1 1 1
. . . . . . . .     . . 1 1 1 1 1 1     . . 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

b2g7             *  LS1B(btwn)      =   line
. . . . . . . .     . . . . . . . .     . . . . . . . 1
. . . . . . 1 .     . . . . . . . .     . . . . . . 1 .
. . . . . 1 . .     . . . . . . . .     . . . . . 1 . .
. . . . 1 . . .     . . . . . . . .     . . . . 1 . . .
. . . 1 . . . .  *  . . . . . . . .  =  . . . 1 . . . .
. . 1 . . . . .     . . 1 . . . . .     . . . . . . . .
. 1 . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

line             &  btwn             =  inBetween
. . . . . . . 1     . . . . . . . .     . . . . . . . .
. . . . . . 1 .     . . . . . . . .     . . . . . . . .
. . . . . 1 . .     1 1 1 1 1 . . .     . . . . . . . .
. . . . 1 . . .     1 1 1 1 1 1 1 1     . . . . 1 . . .
. . . 1 . . . .  &  1 1 1 1 1 1 1 1  =  . . . 1 . . . .
. . . . . . . .     . . 1 1 1 1 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .

```

If both squares share either a rank, file, diagonal or anti-diagonal, one [byte](Byte "Byte")-difference of the four lines becomes zero, which is (zero) extended to a bitboard, otherwise a value 1 ... 255. Subtracting '1' either leaves all bits (-1) set, otherwise 0..254. The a1-scaled mask is shifted left left by the "smallest" square, which can be done by multiplication with the isolated LS1B of the in-between set. The final intersection leaves the obstructed bits between two squares.




### Attacked by Piece on Square


The obstructed lookup idea may be advanced to determine one particular attack by one piece. To lookup whether a certain square is attacked by that piece on another square. Thus, we need a second obstructed-array dimension by piece code. All legal attacks by none sliding pieces are initialized by the empty set zero, all others with the universal set -1. Any intersection with the occupancy (which we need for the sliding pieces anyway) is either empty or not. Sliding pieces have the appropriate obstructed bits set for squares on a common diagonal for bishops and queens - and a common orthogonal for rooks and queens. To safe some memory we rely on the [0x88 trick](Square_Attacked_By#By0x88Difference "Square Attacked By").


Except pawns all white and black pieces have the same attacks - thus based on the piece enumeration mentioned in the [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition"), one may divide the piece code by two to shift right the least significant piece color bit: {1,2,3,4,5,6} for {pawn, knight, bishop, rook, queen, king}. In case of a black pawn we subtract one, to get a 0..6 range:




```C++

U64 attacksBy0x88DiffAndPiece[7][256];  // 14KByte

/* is square <to> attacked by <piece> from square <from> */
bool isAttacked(enumSquare from, enumSquare to, enumPiece piece, U64 occ) {
   int isBlackPawn = (piece ^ nBlackPawn) - 1;
   isBlackPawn >>= 31; /* -1 if black pawn, otherwise 0 */
   return (attacksBy0x88DiffAndPiece [piece/2 + isBlackPawn] [x88diff(from,to)]
           & rotateRight (occ, from) ) == 0;
}

```

See [rotateRight](General_Setwise_Operations#Rotate "General Setwise Operations").


If one considers white and black pawns as disjoint pieces even without color information, one may safe that isBlackPawn calculation obtaining the same table size. With a 11 or 12 array-range one may index by piece-2 or similar according to the piece definition.



## See also


* [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [InBetween](InBetween "InBetween")


## Forum Posts


* [Two questions for bitboard experts](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=516) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 06, 2004 » [Piece-Lists](Piece-Lists "Piece-Lists")
* [Check idea + bittwiddler request](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=12499) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), March 19, 2007
* [Bitboard of squares between](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6573) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 15, 2007
* [bit boards - what is betwen](http://www.talkchess.com/forum/viewtopic.php?t=46240) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 02, 2012
* [Extract direction (ray) informations from two squares](http://www.talkchess.com/forum/viewtopic.php?t=48322) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), June 18, 2013 » [Rays](Rays "Rays"), [Direction](Direction "Direction")
* [AttacksTo() bitboard](http://www.talkchess.com/forum/viewtopic.php?t=50684) by [Tony Soares](index.php?title=Tony_Soares&action=edit&redlink=1 "Tony Soares (page does not exist)"), [CCC](CCC "CCC"), December 29, 2013
* [help with bitboards](https://groups.google.com/forum/#!topic/fishcooking/RXLXONHPw-A) by stefano.c... , [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Max Ernst from Wikipedia](https://en.wikipedia.org/wiki/Max_Ernst)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: AttacksTo() bitboard](http://www.talkchess.com/forum/viewtopic.php?t=50684&start=2) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 29, 2013
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Bitboard user's information request](https://www.stmintz.com/ccc/index.php?id=72098) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), October 06, 1999
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: bit boards - what is betwen](http://www.talkchess.com/forum/viewtopic.php?start=0&t=46240&start=14) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 04, 2012
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Check idea + bittwiddler request](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=12499&start=14) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), April 06, 2007

**[Up one Level](Bitboards "Bitboards")**







 
