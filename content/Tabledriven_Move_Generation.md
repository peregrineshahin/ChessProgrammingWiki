---
title: Tabledriven Move Generation
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Move Generation](Move_Generation "Move Generation") \* Table-driven Move Generation**


**Table-driven Move Generation**,
is a technique to speed up the common traversal of [pieces](Pieces "Pieces") with their [origin](Origin_Square "Origin Square") (from square) from a [piece-list](Piece-Lists "Piece-Lists") and their potential [move target squares](Target_Square "Target Square") by traversing [linked lists](Linked_List "Linked List") with pre-calculated [moves](Moves "Moves"), which head is indexed by [piece-type](Pieces#PieceTypeCoding "Pieces") and origin. There are three control structures to cover the disjoint move abilities for [king](King "King") or [knights](Knight "Knight"), [pawns](Pawn "Pawn"), and [sliding pieces](Sliding_Pieces "Sliding Pieces"), while we focus on the latter for the most general case. 



## GNU Chess


### Inspired by Hardware


Table-driven move generation was pioneered by [Hans Eric Sandström](index.php?title=Hans_Eric_Sandstr%C3%B6m&action=edit&redlink=1 "Hans Eric Sandström (page does not exist)") in 1989 <a id="cite-note-2" href="#cite-ref-2">[2]</a> as introduced in [GNU Chess](GNU_Chess "GNU Chess") Version 1.55 <a id="cite-note-3" href="#cite-ref-3">[3]</a> :





|  |
| --- |
|  New move Generation algorithm:
Revision: 1989-09-06
Author: Hans Eric Sandstroem.
This algorithm is the result of an attempt to make an [hardware move generator](Move_Generation#Hardware "Move Generation"), but since I newer had the time and resources to build the hardware I wrote a software version and incorporated that one into gnu chess. This was the best way I could think of sharing this algorithm with the computer chess community.
If there is anybody out there with the time and resources to build a hardware move generator I will be glad to assist.
The general idea behind this algorithm is to pre calculate a lot of data. The data that is pre calculated is every possible move for every piece from every square disregarding any other pieces on the board. This pre calculated data is stored in an array ... 
 |


### Butterfly Tables


The GNU Chess implementation used the natural branches on empty square, and if occupied and the next direction is taken, on own or opponent piece. [Piece kind](Pieces#PieceTypeCoding "Pieces"), [origin](Origin_Square "Origin Square") and [target square](Target_Square "Target Square") index an [array](Array "Array") of eight [Butterfly boards](Butterfly_Boards "Butterfly Boards") with 64 Kib in total with [16-bit words](Word "Word") while [bytes](Byte "Byte") might suffice as next direction or next position squares as well. This is very register but less memory friendly due to the Butterfly layout. [Sentinel nodes](https://en.wikipedia.org/wiki/Sentinel_node) use the origin square to terminate the do-while loop <a id="cite-note-4" href="#cite-ref-4">[4]</a>: 




```C++

struct sqdata {
  short nextpos;
  short nextdir;
};
struct sqdata posdata[8][64][64];

...
struct sqdata *p = posdata[piece_kind][fromsq];
tosq = p[fromsq].nextpos;
do {
  if (color[tosq] == neutral) {
    linkMove(ply, fromsq, tosq, xside);
    tosq = p[tosq].nextpos;
  }
  else {
    if (color[tosq] == xside) 
       linkMove(ply, fromsq, tosq, xside);
    tosq = p[tosq].nextdir;
  }
} while (tosq  != fromsq);

```

## Further Implementations


There are zillions of implementation nuances concerning disjoint move-lists for quiet moves and captures, and [space-time tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff"). 




### Ferret


The [GNU Chess approach](Table-driven_Move_Generation#GNUChess "Table-driven Move Generation") was refined by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), as used in [Ferret](Ferret "Ferret"), and elaborated in his programming topics, for instance for a bishop on d5 <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++

typedef struct tagMT {
  int    square;
  struct tagMT * pmtBlocked;
} MT;

MT argmtBD5[] = {
    e6,    &argmtBD5[3], // Element 0, 1st ray.
    d7,    &argmtBD5[3],
    f8,    &argmtBD5[3],
    c6,    &argmtBD5[3], // Element 3, 2nd ray.
    b7,    &argmtBD5[6],
    a8,    &argmtBD5[6],
    e4,    &argmtBD5[6], // Element 6, 3rd ray.
    f3,    &argmtBD5[6],
    g2,    &argmtBD5[6],
    h1,    NULL,         // Element 9, 4th ray.
    c4,    NULL,
    b3,    NULL,
    a2,    NULL,
    -1,
};

void genMoves(MT * pmt)
{
  for (;;) {
    if (IsEmpty(pmt->square)) {
      GenMove(pmt->square);
      if ((++pmt)->square < 0)
        break;
    } else {
      if (IsEnemy(pmt->square))
        GenMove(pmt->square);
      if ((pmt = pmt->pmtBlocked) == NULL)
        break;
    }
  }
}

```





### Diep


[Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") used a similar technique in [Diep](Diep "Diep"). He published a move generation skeleton under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-6" href="#cite-ref-6">[6]</a> in [CCC](CCC "CCC") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>. Vincent's approach uses the default ones-increment of the list pointer, and adds a further skip-increment to the next direction in case of a block, which is done branch-less by intersection of the increment with a mask for target square empty (0) or not (-1), and was inspiration for the [conditional linked list](Table-driven_Move_Generation#ConditionalLinkedList "Table-driven Move Generation") approach, which stresses memory versus a simplified control structure.




## Conditional Linked List


To minimize code and to [avoid branches](Avoiding_Branches "Avoiding Branches") on todays super pipelined processors, following [recursive](Recursion "Recursion") data structure of a pre-initialized [skip list](https://en.wikipedia.org/wiki/Skip_list) with two alternative next references might be applied for a prototype of table-driven move generation. 



### Data Structure


One sliding move node consists of the target square, the bit redundant move itself (might already contain a score based on dedicated [piece-square tables](Piece-Square_Tables "Piece-Square Tables") concerning [move ordering](Move_Ordering "Move Ordering")), and an [array](Array "Array") of two [pointers](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29) to the next square if any. During traversal, the next array is indexed by the condition whether the target square is empty (0, false) or occupied (1, true), either to arrive the next square on the current ray, or the first square of the next ray-direction if any.




```C++

struct SlidingMoveNode
{
  TSquare tosq;
  SMove   move;
  SlidingMoveNode* pNext[2];
};

```

The number of sliding move node structures is determined by the [influence quantity of pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces"), where bishops have a cardinality of 560, rooks of 896, and queens the sum of 1456, and they are typically declared as array with consecutive nodes and almost always pNext[0] = this + 1. However, despite avoiding conditional branches, this redundancy a little bit pays off since this approach does not require [sentinel nodes](https://en.wikipedia.org/wiki/Sentinel_node) with one extra indirection to check for an invalid target square for termination, due to storing sentinel values, that is [null pointers](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29#Null_pointer) aka nil.




```C++

SlidingMoveNode  slidingMoveTable[1456+896+560]; /* queen, rook, bishop ->  2912 * 16 = 46592 bytes 45.5 Kib */
SlidingMoveNode* slidingMoveHead[3][64];

```

With following initialization, for instance for a rook on e4:




```C++

slidingMoveHead[rook][e4]
     ▼ north                                   east           south          west
 ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐  ┌────────┐─┐-┐ ┌────────┐─┐-┐ ┌────────┐─-┬-┌────────┐
 │   e5   │ │   e6   │ │   e7   │ │   e8   │  │   f4   │     │   e3   │     │   d4   │    │   a4   │
 ├────────┤ ├────────┤ ├────────┤ ├────────┤  ├────────┤g4   ├────────┤e2   ├────────┤c4  ├────────┤
 │ Re4e5  │ │ Re4e6  │ │ Re4e7  │ │ Re4e8  │  │ Re4f4  │  h4 │ Re4e3  │  e1 │ Re4d4  │  b4│ Re4a4  │
 ├────────┤ ├────────┤ ├────────┤ ├────────┤  ├────────┤     ├────────┤     ├────────┤    ├────────┤
 │pNext[0]│►│pNext[0]│►│pNext[0]│►│pNext[0]│►─│pNext[0]│►─...│pNext[0]│►─...│pNext[0]│►─..│   NIL  │
 ├────────┤ ├────────┤ ├────────┤ ├────────┤  ├────────┤     ├────────┤     ├────────┤    ├────────┤
 │pNext[1]│ │pNext[1]│ │pNext[1]│ │pNext[1]│►─│pNext[1]│     │pNext[1]│     │   NIL  │    │   NIL  │
 └────────┘ └────────┘ └────────┘ └────────┘  └────────┘─┘-┘ └────────┘─┘-┘ └────────┘--┴-└────────┘
       ▼          ▼          ▼                  ▲   ▼          ▲   ▼          ▲
       │          │          └───►──────────►───┘   │          │   │          │
       │          └───►──────────►──────────►───┘   │     ... ─┘   │     ... ─┘
       └───►──────────►──────────►──────────►───┘   └───►─...──┘   └───►─...──┘

```

### Control Structure


This data structure simplifies the control structure to generate moves of one sliding piece with only one conditional branch concerning the while loop. To avoid the branch on blocked by own piece, a [conditional write](Avoiding_Branches#ConditionalWrite "Avoiding Branches") taking advantage of [write-combining](https://en.wikipedia.org/wiki/Write-combining) <a id="cite-note-11" href="#cite-ref-11">[11]</a> is implemented, storing always, but post-increment the [move list](Move_List "Move List") pointer by a boolean aka {0,1} condition:




```C++

pMoveNode = slidingMoveHead[slidingPiece_kind_012][fromSq];
do {
  tosq = pMoveNode->tosq;
  *pMoveList = pMoveNode->move;
  pMoveList += board[tosq].isNotPieceOf( side2move );
  pMoveNode  = pMoveNode->pNext[ board[tosq].isPiece() ];
} while ( pMoveNode );

```

### Captures vs Quiet


To generate disjoint sets of [captures](Captures "Captures") and [quiet moves](Quiet_Moves "Quiet Moves") in different move generation stages, the same conditional linked lists could be traversed, stressing [conditional writes](Avoiding_Branches#ConditionalWrite "Avoiding Branches") in using different conditions for the move-list pointer increment. 




```C++

/* Captures  */
pMoveNode = slidingMoveHead[slidingPiece_kind_012][fromSq];
do {
  tosq = pMoveNode->tosq;
  *pMoveList = capture( pMoveNode->move, board[tosq]);
  pMoveList += board[tosq].isPieceOf( side2move ^ 1 );
  pMoveNode  = pMoveNode->pNext[ board[tosq].isPiece() ];
} while ( pMoveNode );

/* none Captures */
pMoveNode = slidingMoveHead[slidingPiece_kind_012][fromSq];
do {
  tosq = pMoveNode->tosq;
  *pMoveList = pMoveNode->move;
  pMoveList += board[tosq].isPiece() ^ 1; /* isEmpty */
  pMoveNode  = pMoveNode->pNext[ board[tosq].isPiece() ];
} while ( pMoveNode );

```

However, for capture generation specially in the [quiescence search](Quiescence_Search "Quiescence Search"), if one imagines a queen in the late ending, the overhead to visit up to 27 empty squares with conditional stores seems not justified, and one may better rely on branches as demonstrated in [Fritz Reul's](Fritz_Reul "Fritz Reul") [blocking Loop](Vector_Attacks#NewArchitecture "Vector Attacks"), and to scan potential winning capture targets with a [vector attack](Vector_Attacks "Vector Attacks") lookup whether they have lines in common with a sliding piece able to move along that line, to only test whether the squares between are empty - not to mention [bitboard](Bitboards "Bitboards") techniques.



### Dense Index List


As proposed by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades") with 64-bit nodes and indices instead of pointer <a id="cite-note-12" href="#cite-ref-12">[12]</a>, an even denser alternative is to use nodes with two 12-bit indices and target square packed in a 32-bit integer. With appropriate piece-type coding, with bits 2 to 4 masked containing a right shift amount, either 8 for empty squares and 20 for pieces, one may "index" the appropriate next index. Bit 0 and 1 are exclusively set for either white and black pieces.




```C++

// U32 as struct SlidingMoveNode {int next1 : 12; int next0 : 12; int tosq  :  8; /* low byte */ };
U32 slidingMoveTable[1456+896+560]; /* queen, rook, bishop ->  2912 * 4 = 11648 bytes  */
U32 slidingMoveHead[3][64];

/* five least significant piece code bits from board: 
   01000 empty
   10101 white piece
   10110 black piece */

node = slidingMoveHead[slidingPiece_kind_012][fromSq];
do {
  node  = slidingMoveTable[node];
  tosq  = node & 0x3f;
  piece = board[tosq];
  *pMoveList = fromaspects | tosq;
  pMoveList += (piece & side2moveBit) == 0;
  node = (node >> (piece & 0x1c)) & 0x0fff;
} while ( node );

```

## See also


* [0x88](0x88 "0x88")
* [Mailbox](Mailbox "Mailbox")
* [Move Generation in CPW-Engine](CPW-Engine_movegen(0x88) "CPW-Engine movegen(0x88)")
* [Move Generation in Atlas](Atlas#MoveGeneration "Atlas")
* [Offset Move Generation](10x12_Board#OffsetMG "10x12 Board")
* [Vector Attacks](Vector_Attacks "Vector Attacks")


## Publications


* [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, [index](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/index.htm)


## Forum Posts


### 1998 ...


* [GNU move generation](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7292bfb78152b40b) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 18, 1998
* [Re: 0x88](https://www.stmintz.com/ccc/index.php?id=39133) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), January 12, 1999


### 2000 ...


* [Pre-calculated move generation](https://www.stmintz.com/ccc/index.php?id=116593) by Ujecrh, [CCC](CCC "CCC"), June 26, 2000
* [Precomputed move information](https://www.stmintz.com/ccc/index.php?id=238333) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), July 02, 2002
* [Diep move generator speeded up](https://www.stmintz.com/ccc/index.php?id=403656) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), January 01, 2005
* [Re: Is it time for another new move generator?](http://www.talkchess.com/forum/viewtopic.php?t=17790&start=4) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), November 11, 2007
* [Did someone mention the GNUChess move Generator?](http://www.talkchess.com/forum/viewtopic.php?t=17820) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 12, 2007


### 2010 ...


* [What's the fastest move generator?](http://www.talkchess.com/forum/viewtopic.php?t=44939) by Marcel Fournier, [CCC](CCC "CCC"), August 29, 2012
* [CPW Move Table compression](http://www.talkchess.com/forum/viewtopic.php?t=45042) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), September 08, 2012
* [Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?t=45846) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), November 04, 2012


 [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490492&t=45846) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), November 04, 2012
 [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490652&t=45846) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), November 05, 2012
* [Diepeveen's move generator](http://www.talkchess.com/forum/viewtopic.php?t=46056) by Hrvoje Horvatic, [CCC](CCC "CCC"), November 18, 2012


 [Re: Diepeveen's move generator](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=493083&t=46056) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), November 19, 2012
* [Fast table-driven move generation](http://www.talkchess.com/forum/viewtopic.php?t=62686) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), January 01, 2017
* [Re: PieceLists ?](http://www.talkchess.com/forum/viewtopic.php?t=63126&start=40) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), February 17, 2017 » [Piece-Lists](Piece-Lists "Piece-Lists")
* [Opinions requested for new move gen idea](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70082) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 03, 2019


## External Links


* [Move Table move generation](http://web.archive.org/web/20070715002634/www.brucemo.com/compchess/programming/movetable.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Permission to use code](http://mridulm.blogspot.de/2004/06/permission-to-use-code-have-to-put-up.html) from [Random thoughts](http://mridulm.blogspot.de/) by [Mridul Muralidharan](Mridul_Muralidharan "Mridul Muralidharan"), June 09, 2004
* [Skip list from Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
* [Kraftwerk](Category:Kraftwerk "Category:Kraftwerk") - [Ruckzuck](http://de.wikipedia.org/wiki/Ruck_Zuck_%28Begriffskl%C3%A4rung%29), [Soest](https://en.wikipedia.org/wiki/Soest,_Germany) [1970](https://www.wa.de/kultur/kraftwerk-soest-konzertmitschnitte-karussell-jugend-1970-internet-3522483.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Ralf Hütter](https://en.wikipedia.org/wiki/Ralf_H%C3%BCtter), [Florian Schneiderr-Esleben](https://en.wikipedia.org/wiki/Florian_Schneider), [Klaus Dinger](https://en.wikipedia.org/wiki/Klaus_Dinger)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](https://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227, [index](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/index.htm)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490652&t=45846) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), November 05, 2012
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GNU's Bulletin, vol. 1 no. 8 - GNU Project - Free Software Foundation (FSF)](http://www.gnu.org/bulletins/bull8.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [GNU's new move generation algorithm](http://slackware.dreamhost.com/slackware/slackware-2.1/usr/doc/gnuchess-4.0/MOVE-GEN)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Move Table move generation](http://web.archive.org/web/20070715002634/www.brucemo.com/compchess/programming/movetable.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Permission to use code](http://mridulm.blogspot.de/2004/06/permission-to-use-code-have-to-put-up.html) from [Random thoughts](http://mridulm.blogspot.de/) by [Mridul Muralidharan](Mridul_Muralidharan "Mridul Muralidharan"), June 09, 2004
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Diep move generator speeded up](https://www.stmintz.com/ccc/index.php?id=403656) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), January 01, 2005
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: What's the fastest move generator?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=480825&t=44939) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), August 31, 2012
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: What's the fastest move generator?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=480726&t=44939) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), August 30, 2012
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: Diepeveen's move generator](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=493083&t=46056) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), November 19, 2012
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Software Optimization Guide for AMD Family 10h and 12h Processors](http://support.amd.com/us/Processor_TechDocs/40546.pdf) (pdf) see pp. 102 on Conditional Write
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [CPW Move Table compression](http://www.talkchess.com/forum/viewtopic.php?t=45042) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), September 08, 2012

**[Up one level](Move_Generation "Move Generation")**







 
