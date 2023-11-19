---
title: Vector Attacks
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Mailbox](Mailbox "Mailbox") \* Vector Attacks**



[ Position Vector <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Vector Attacks** <a id="cite-note-2" href="#cite-ref-2">[2]</a>,


the application of [vectors](https://en.wikipedia.org/wiki/Euclidean_vector) in the [Chebyshev](https://en.wikipedia.org/wiki/Chebyshev_distance) [vector space](https://en.wikipedia.org/wiki/Vector_space) of a [chessboard](Chessboard "Chessboard") to the problem of chess [attacks](Attacks "Attacks"), including [static exchange evaluation (SEE)](Static_Exchange_Evaluation "Static Exchange Evaluation"), and testing whether [moves](Moves "Moves") are [pseudo-legal](Pseudo-Legal_Move "Pseudo-Legal Move").



## Vector Boards


Vector board arrays with a one-dimensional, scalar index, require the difference of any two mailbox square indices preserve their rank- and file-difference and therefore their [direction](Direction "Direction") and [distance](Distance "Distance") relationship, which implies using the number of file differences as array dimension - which is **15** rather than 8 for the number of files. Therefore, the 8x8 mailbox needs at least 7 padded columns (files) of a 15xNROWS (or 16xNROWS) vector array:



 [](File:Vector_Attacks_3.jpg) 
or



 [](File:Vector_Attacks_4.jpg) 
## Vector as Index


Represented as such a square difference, displacement vectors can be used to index 225 (15x15) or 240 (16x15) sized lookup tables for stuff dependent on square relations, that is [Chebyshev distance](Distance#15x15 "Distance"), [Manhattan-distance](Manhattan-Distance "Manhattan-Distance"), boolean [ray properties](Rays "Rays") and most importantly, [increment vectors](#IncrementVectors) along a ray, or in the world of [bitboards](Bitboards "Bitboards"), [rotated in-between](Square_Attacked_By#By0x88Difference "Square Attacked By") sets. Thus, the up to fourfold board size of the vector boards, largely pays off, since pure 8x8 coordinates would require two-dimensional [butterfly tables](Butterfly_Boards "Butterfly Boards") of size 4096 indexed by two square indices for the same purpose. To keep indices positive, an offset of 112 respective 119 (120) is added.



## Superimposed Lookup


8x8 tables inside 15x15 tables were already proposed by [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") as used in [Pioneer](Pioneer "Pioneer") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The table below demonstrates the vector enumeration from a square (here c2) on a 8x8 board, superimposed on the 15x15 array in such a way that the from square (c2) coincides with the central square of the 15x15 array, which is the origin, tail, or base of all displacement vectors.




```C++

     ╔════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╗
 210 ║  98| 99 | 100| 101| 102| 103| 104| 105| 106| 107| 108| 109| 110| 111| 112║
     ╟────┼────┼────┼────┼────╔════╤════╤════╤════╤════╤════╤════╤════╗────┼────╢
 195 ║  83|  84|  85|  86|  87║  88|  89|  90|  91|  92|  93|  94|  95║  96|  97║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 180 ║  68|  69|  70|  71|  72║  73|  74|  75|  76|  77|  78|  79|  80║  81|  82║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 165 ║  53|  54|  55|  56|  57║  58|  59|  60|  61|  62|  63|  64|  65║  66|  67║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 150 ║  38|  39|  40|  41|  42║  42|  44|  45|  46|  47|  48|  49|  50║  51|  52║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 135 ║  23|  24|  25|  26|  27║  28|  29|  30|  31|  32|  33|  34|  35║  36|  37║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 120 ║   8|   9|  10|  11|  12║  13|  14|  15|  16|  17|  18|  19|  20║  21|  22║
     ╟────┼────┼────┼────┼────╟────┼────╔════╗────┼────┼────┼────┼────╢────┼────╢
 105 ║  -7|  -6|  -5|  -4|  -3║  -2|  -1║   0║   1|   2|   3|   4|   5║   6|   7║
     ╟────┼────┼────┼────┼────╟────┼────╚════╝────┼────┼────┼────┼────╢────┼────╢
  90 ║ -22| -21| -20| -19| -18║ -17| -16| -15| -14| -13| -12| -11| -10║  -9|  -8║
     ╟────┼────┼────┼────┼────╚════╧════╧════╧════╧════╧════╧════╧════╝────┼────╢
  75 ║ -37| -36| -35| -34| -33| -32| -31| -30| -29| -28| -27| -26| -25| -24| -23║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  60 ║ -52| -51| -50| -49| -48| -47| -46| -45| -44| -43| -42| -41| -40| -39| -38║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  45 ║ -67| -66| -65| -64| -63| -62| -61| -60| -59| -58| -57| -56| -55| -54| -53║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  30 ║ -82| -81| -80| -79| -78| -77| -76| -75| -74| -73| -72| -71| -70| -66| -68║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  15 ║ -97| -96| -95| -94| -93| -92| -91| -90| -89| -88| -87| -86| -85| -84| -83║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
   0 ║-112|-111|-110|-109|-108|-107|-106|-105|-104|-103|-102|-101|-100| -99| -98║
     ╚════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╝
        0    1    2    3    4    5    6    7    8    9    10   11   12   13   14

```

## Ray Vectors


[Ray](Rays "Rays") vectors are [unit vectors](https://en.wikipedia.org/wiki/Unit_vector) to [eight neighboring](https://en.wikipedia.org/wiki/Moore_neighborhood) squares, [scaled](https://en.wikipedia.org/wiki/Scalar_multiplication) by [Chebyshev distance](Distance#15x15 "Distance"). In the domain of [sliding piece](Sliding_Pieces "Sliding Pieces") attacks, unit vectors act as [increment vectors](#IncrementVectors) if none zero, to determine squares in-between are empty, and a [target square](Target_Square "Target Square") is attacked by a sliding piece on its [origin](Origin_Square "Origin Square"). Following table demonstrates the [queen](Queen "Queen") unit or increment vectors, superimposed on the 15x15 array in such a way that the queen square (here c2) coincides with the central square of the 15x15 array.




```C++

char rayUnitVectorQueen[15*15];

     ╔════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╗
 210 ║  14|    |    |    |    |    |    |  15|    |    |    |    |    |    |  16║
     ╟────┼────┼────┼────┼────╔════╤════╤════╤════╤════╤════╤════╤════╗────┼────╢
 195 ║    |  14|    |    |    ║    |    |  15|    |    |    |    |    ║  16|    ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 180 ║    |    |  14|    |    ║    |    |  15|    |    |    |    |  16║    |    ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 165 ║    |    |    |  14|    ║    |    |  15|    |    |    |  16|    ║    |    ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 150 ║    |    |    |    |  14║    |    |  15|    |    |  16|    |    ║    |    ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 135 ║    |    |    |    |    ║  14|    |  15|    |  16|    |    |    ║    |    ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 120 ║    |    |    |    |    ║    |  14|  15|  16|    |    |    |    ║    |    ║
     ╟────┼────┼────┼────┼────╟────┼────╔════╗────┼────┼────┼────┼────╢────┼────╢
 105 ║  -1|  -1|  -1|  -1|  -1║  -1|  -1║  Q ║   1|   1|   1|   1|   1║   1|   1║
     ╟────┼────┼────┼────┼────╟────┼────╚════╝────┼────┼────┼────┼────╢────┼────╢
  90 ║    |    |    |    |    ║    | -16| -15| -14|    |    |    |    ║    |    ║
     ╟────┼────┼────┼────┼────╚════╧════╧════╧════╧════╧════╧════╧════╝────┼────╢
  75 ║    |    |    |    |    | -16|    | -15|    | -14|    |    |    |    |    ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  60 ║    |    |    |    | -16|    |    | -15|    |    | -14|    |    |    |    ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  45 ║    |    |    | -16|    |    |    | -15|    |    |    | -14|    |    |    ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  30 ║    |    | -16|    |    |    |    | -15|    |    |    |    | -14|    |    ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  15 ║    | -16|    |    |    |    |    | -15|    |    |    |    |    | -14|    ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
   0 ║ -16|    |    |    |    |    |    | -15|    |    |    |    |    |    | -14║
     ╚════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╝
        0    1    2    3    4    5    6    7    8    9    10   11   12   13   14

```

## Increment Vectors


During offset [move generation](Move_Generation "Move Generation"), each piece applies a specific displacement or **increment vector** (offset) for each move direction, added to the position vector of the [origin square](Origin_Square "Origin Square") to determine the next potential [move target](Target_Square "Target Square") in that direction, [sliding pieces](Sliding_Pieces "Sliding Pieces") continuing in the same direction as long the targets are empty. Due to the additional padded files and possibly ranks, off the board test are as simple as the [10x12 board](10x12_Board "10x12 Board") with surrounding files and ranks containing off the board codes as [sentinel values](https://en.wikipedia.org/wiki/Sentinel_value). The [0x88](0x88 "0x88") approach, a special 16x8 implementation of Vector Attacks, already indicates outside squares by its upper [nibble](Nibble "Nibble") bits masked by 0x88.


One may argue, the 0x88 test is cheaper for off the board tests, because it does not need to lookup if the 0x88 test is true. On the other hand, for most cases, if false, it needs a lookup anyway, to perform a second test whether the square is empty, or occupied by an own or opponent piece <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## New Architecture


Vector Attacks based on a 15x12 board were topic of [Fritz Reul's](Fritz_Reul "Fritz Reul") Ph.D. thesis *New Architectures in Computer Chess*, code samples given from Reul's [Loop Leiden](Loop_(Program)#32bit "Loop (Program)") engine <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### Source-Destination


In conjunction with [disjoint piece flags](Pieces#DisjointPieceFlags "Pieces") and [piece-lists](Piece-Lists "Piece-Lists"), Vector Attacks allow efficient [move generation](Move_Generation "Move Generation") of [sliding pieces](Sliding_Pieces "Sliding Pieces"), even for [quiescence search](Quiescence_Search "Quiescence Search") with a leading blocker loop:




```C++

increment = rayVector[direction];
for (tosq = fromsq + increment; board[tosq] == EMPTY; tosq += increment);
if ( isOpponentPiece (board[tosq]) )
{
  /* generate capture */
}

```

### Destination-Source


A destination-source blocker loop, to test whether a sliding piece on a from square attacks a target square, uses the reversed ray direction in order to dispense with additional conditions:




```C++

increment = rayUnitVectorQueen[15*15/2 + fromsq - tosq];
if ( increment ) {
  for (sq = tosq + increment; board[sq] == EMPTY; sq += increment);
  if ( sq == fromsq ) {
    /* a queen on fromsq attacks tosq */
  }
}

```

## Implementations


### 0x88


*see main article [0x88](0x88 "0x88")*


The [0x88](0x88 "0x88") or 16x8 board uses [nibbles](Nibble "Nibble") for both rank and file coordinates inside a [byte](Byte "Byte"), and utilizes the redundant upper bit to indicate invalid squares outside the board, usually then not used as index.



### Layout



```C++

--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX
--------XXXXXXXX

```

### Coordinate Transformation


16x8 square coordinate by file and rank and vice versa:




```C++

sq0x88 = 16 * rank07 + file07;
file07 = sq0x88 & 7;
rank07 = sq0x88 >> 4; // sq0x88 / 16

```

0x88 index by a 0..63 square index needs to add the three upper rank bits:




```C++

sq0x88 = sq + (sq & ~7);

```

### 15x12


The odd number of files makes the [square color](Color_of_a_Square "Color of a Square") only dependent from the least significant index bit. Usually the seven surrounding border files are divided 4:3 (Offset 34) or 3:4 (Offset 33). One may also use 15x15 for a symmetric treatment of files and ranks as proposed by [Fritz Reul](Fritz_Reul "Fritz Reul") <a id="cite-note-7" href="#cite-ref-7">[7]</a> .



### Layout



```C++

XXXXXXXXXXXXXXX
XXXXXXXXXXXXXXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXX--------XXX
XXXXXXXXXXXXXXX
XXXXXXXXXXXXXXX

```

### Coordinate Transformation


Coordinate transformation is usually not needed while generating moves, since [piece-lists](Piece-Lists "Piece-Lists"), increments and move coordinates are only based on 15x12 coordinates. Anyway, for the sake of completeness valid 15x12 square transformation to file and rank indices and vice versa might be done quite efficiently without any [x86](X86 "X86") div and mul instructions, but load effective address (lea) - otherwise simple lookup tables may used to convert coordinates:




```C++

sq15x12 = 15 * rank07 + file07 + 34;
rank07  = ((sq15x12 - 34) * 9) >> 7;  // div by reciprocal mul
file07  =   sq15x12 - 34  - 15 * rank07; // % 15

```

### 16x12


Usually the eight surrounding border files are divided 4:4, so the offset of the upper left square is 36. For a symmetric treatment of files and ranks, 16x16 is also quite common <a id="cite-note-8" href="#cite-ref-8">[8]</a> .



### Layout



```C++

XXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXX--------XXXX
XXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXX

```

### Coordinate Transformation


16x12 square coordinate by file and rank and vice versa:




```C++

sq16x12 = 16 * rank07 + file07 + 36;
rank07  = (sq16x12 - 36) >> 4; // div 16
file07  = (sq16x12 - 36) &  7;  // % 8

```

16x12 square index by a 0..63 square index needs to add the three upper rank bits plus offset:




```C++

sq16x12 = sq8x8 + (sq8x8 & ~7) + 36;

```

Convert 16x12 square index to 0..63 square index:




```C++

file8x8 = (sq16x12 & 0xf) - 4
rank8x8 = ((sq16x12 >> 4) - 2
sq8x8 = (((sq16x12 >> 4) - 2) << 3) + (sq16x12 & 0xf) - 4;

```

### Conclusion


A combination of 0x88 and [10x12 Board](10x12_Board "10x12 Board") with surrounded ranks, that is 16x12 or even 16x16 for a symmetric treatment of files and ranks (or 15x12, 15x15) seems slightly more efficient than pure 0x88 aka 16x8, making the "off the board" index condition almost redundant, since it can be combined with the coding of the guard or sentinal squares <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> .



## See also


* [0x88](0x88 "0x88")
* [0x88 meets Bitboards](Square_Attacked_By#By0x88Difference "Square Attacked By")
* [10x12 Board](10x12_Board "10x12 Board")
* [8x8 Board](8x8_Board "8x8 Board")
* [Distance](Distance "Distance")
* [Direction](Direction "Direction")
* [Intersection Squares](Intersection_Squares "Intersection Squares") as application of 0x88 coordinates
* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") with [Bitboards](Bitboards "Bitboards")


## Publications


* [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1968**). *Algoritm igry v shakhmaty*. (The algorithm of chess)
* [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1970**). *Computers, Chess and Long-Range Planning*. Springer
* [Paul Wiereyn](Paul_Wiereyn "Paul Wiereyn") (**1985**). *Inventive Problem Solving*. [ICCA Journal, Vol. 8, No. 4](ICGA_Journal#8_4 "ICGA Journal")
* [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*


## Forum Posts


### 2000 ...


* [Question:1.hashtable 2.board 3.C](https://www.stmintz.com/ccc/index.php?id=114311) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), June 13, 2000


 [Re: Question:1.hashtable 2.board 3.C](https://www.stmintz.com/ccc/index.php?id=114377) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), June 13, 2000
 [Re: Question:1.hashtable 2.board 3.C](https://www.stmintz.com/ccc/index.php?id=114385) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), June 13, 2000
 [0x88 is not so smart](https://www.stmintz.com/ccc/index.php?id=114438) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), June 13, 2000 » [0x88](0x88 "0x88")
* [Fastest Conversion from 0x88 board to 8x8 board representation](https://www.stmintz.com/ccc/index.php?id=178465) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 06, 2001
* [Re: Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11195#p11109) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 28, 2005 » [Fruit](Fruit "Fruit")


### 2010 ...


* [GetSmallestAttacker() in 16x12 board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31776) by metax, [CCC](CCC "CCC"), January 17, 2010 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), [Piece-Lists](Piece-Lists "Piece-Lists")
* [Recommended board representation for a rookie](http://www.talkchess.com/forum/viewtopic.php?t=62279) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), November 26, 2016


 [Re: Recommended board representation for a rookie](http://www.talkchess.com/forum/viewtopic.php?t=62279&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 26, 2016
* [What're advantages of board 16x12?](http://www.talkchess.com/forum/viewtopic.php?t=62657) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), December 30, 2016


## External Links


* [Vector (mathematics and physics) from Wikipedia](https://en.wikipedia.org/wiki/Vector_%28mathematics_and_physics%29)
* [Euclidean vector from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_vector)
* [Position (vector) from Wikipedia](https://en.wikipedia.org/wiki/Position_%28vector%29)
* [Displacement (vector) from Wikipedia](https://en.wikipedia.org/wiki/Displacement_%28vector%29)
* [Linear algebra from Wikipedia](https://en.wikipedia.org/wiki/Linear_algebra)
* [Vector space from Wikipedia](https://en.wikipedia.org/wiki/Vector_space)
* [The Dave Pike Set](Category:Dave_Pike "Category:Dave Pike") - Attack Of The Green Misers, [Infra-Red](https://www.discogs.com/de/Dave-Pike-Set-Infra-Red/master/91659) (1970), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Dave Pike](Category:Dave_Pike "Category:Dave Pike"), [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel"), [Hans Rettenbacher](https://de.wikipedia.org/wiki/Hans_Rettenbacher), [Peter Baumeister](https://de.wikipedia.org/wiki/Peter_Baumeister)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A vector in the [Cartesian plane](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), showing the position of a point A with coordinates (2,3), [Euclidean vector from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_vector)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11195#p11109) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 28, 2005
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Question:1.hashtable 2.board 3.C](https://www.stmintz.com/ccc/index.php?id=114377) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), June 13, 2000
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [0x88 is not so smart](https://www.stmintz.com/ccc/index.php?id=114438) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), June 13, 2000
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Re: Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11195#p11109) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 28, 2005
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Question:1.hashtable 2.board 3.C](https://www.stmintz.com/ccc/index.php?id=114377) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), June 13, 2000
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11195#p11109) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 28, 2005
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*. Ph.D. Thesis, 2.2.1 *Computer Chessboard Representation*
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Recommended board representation for a rookie](http://www.talkchess.com/forum/viewtopic.php?t=62279&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 26, 2016

**[Up one Level](Mailbox "Mailbox")**







 
