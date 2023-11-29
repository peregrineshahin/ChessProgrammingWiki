---
title: Distance
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Squares](Squares "Squares") * Distance**

[](https://artsandculture.google.com/asset/colors-from-a-distance/kAHBsV7-F_nsQw) [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Colors from a Distance <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The term **Distance** refers to the minimal number of [moves](Moves "Moves") a certain [piece](Pieces "Pieces"), which resides on the first square, needs, to reach the second square. The so called [Chebyshev distance](https://en.wikipedia.org/wiki/Chebyshev_distance) is the minimal number of [king](King "King") moves between those squares on the otherwise empty board. The so called [Manhattan- or Taxi-distance](Manhattan-Distance "Manhattan-Distance") is restricted to orthogonal king moves, while [knight-distance](Knight-Distance "Knight-Distance") refers to [knight](Knight "Knight") moves. In a wider sense, distance can be interpreted as a generalization of [mobility](Mobility "Mobility"), for instance determined by [fill algorithms](Fill_Algorithms "Fill Algorithms") in [bitboards](Bitboards "Bitboards").

## Chebyshev Distance

The Chebyshev distance is the maximum of the absolute [rank-](Ranks#RankDistance "Ranks") and [file-distance](Files#FileDistance "Files") of both squares.

```C++D = max(|r2 - r1|, |f2 - f1|)

```

while the orthogonal [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance") is the sum of both absolute rank- and file-distance distances.

```C++Dtaxi = |r2 - r1| + |f2 - f1|

```

- The minimum square Distance is 0 (if both squares are equal)
- The maximum square Distance is 7

while

- The maximum square Manhattan-Distance is 14 (between the endpoints of the main-diagonals)

## Routine

The following [C](C "C")-routine performs the computation. One may use the mentioned square-, rank- or file-enumeration types instead of the used integers, or rely on anonymous enumeration in [C](C "C") or [C++](Cpp "Cpp") treated as integers anyway. One should use the [abs](Avoiding_Branches#Abs "Avoiding Branches") and [max](Avoiding_Branches#Max "Avoiding Branches") functions for likely branchless implementations.

```C++
int distance(int sq1, int sq2) {
   int file1, file2, rank1, rank2;
   int rankDistance, fileDistance;
   file1 = sq1  & 7;
   file2 = sq2  & 7;
   rank1 = sq1 >> 3;
   rank2 = sq2 >> 3;
   rankDistance = abs (rank2 - rank1);
   fileDistance = abs (file2 - file1);
   return max (rankDistance, fileDistance);
}

```

## Lookup

Since the computation is relative expensive, often two dimensional tables with precalculated values are used for that purpose. A [Byte](Byte "Byte") as lowest addressable unit is more than enough and easily zero extended:

```C++
unsigned char arrDistance[64][64]; // 4 KByte

inline int distance(enumSquare sq1, enumSquare sq2) {
   return arrDistance[sq1][sq2];
}

```

## Lookup by 0x88 Difference

[Vector attacks](Vector_Attacks "Vector Attacks") like [0x88](0x88 "0x88") [square relation](0x88#SquareRelations "0x88") permits a denser lookup approach. The difference of valid 0x88 coordinates of two squares is uniquely with respect to distance and [direction](Direction "Direction"). That way, one can greatly reduce the size of the lookup [array](Array "Array") to only 240 instead of 4096 elements. Some additional computation required, if one has to convert usual square coordinates to 0x88. If one already relies on 0x88 coordinates, it becomes even cheaper:

```C++
unsigned char arrDistanceBy0x88Diff[240];

unsigned int x88diff(enumSquare sq1, enumSquare sq2) {
   return sq2 - sq1 + (sq2|7) - (sq1|7) + 120;
}

inline int distance(enumSquare sq1, enumSquare sq2) {
   return arrDistanceBy0x88Diff[x88diff(sq1, sq2)];
}

```

## Lookup of Array 15\*15

An approach with a 225 element table for king move distance, as well for other piece move distances, [directions](Direction "Direction"), [vector attacks](Vector_Attacks#Superimposition "Vector Attacks") and [increment vectors](Vector_Attacks#IncrementVectors "Vector Attacks"), was used in [Pioneer](Pioneer "Pioneer") as described by [Boris Stilman](Boris_Stilman "Boris Stilman") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The [8x8 array](8x8_Board "8x8 Board") is [superimposed](https://en.wikipedia.org/wiki/Superimposition) on the array 15x15 in such a way that square x coincides with the central square (112) of the array 15x15, see the sample with c2:

```C++
     ╔════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╤════╗
 210 ║  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 ║
     ╟────┼────┼────┼────┼────╔════╤════╤════╤════╤════╤════╤════╤════╗────┼────╢
 195 ║  7 |  6 |  6 |  6 |  6 ║  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 180 ║  7 |  6 |  5 |  5 |  5 ║  5 |  5 |  5 |  5 |  5 |  5 |  5 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 165 ║  7 |  6 |  5 |  4 |  4 ║  4 |  4 |  4 |  4 |  4 |  4 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 150 ║  7 |  6 |  5 |  4 |  3 ║  3 |  3 |  3 |  3 |  3 |  3 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 135 ║  7 |  6 |  5 |  4 |  3 ║  2 |  2 |  2 |  2 |  2 |  3 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────┼────┼────┼────┼────┼────┼────╢────┼────╢
 120 ║  7 |  6 |  5 |  4 |  3 ║  2 |  1 |  1 |  1 |  2 |  3 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────╔════╗────┼────┼────┼────┼────╢────┼────╢
 105 ║  7 |  6 |  5 |  4 |  3 ║  2 |  1 ║  0 ║  1 |  2 |  3 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╟────┼────╚════╝────┼────┼────┼────┼────╢────┼────╢
  90 ║  7 |  6 |  5 |  4 |  3 ║  2 |  1 |  1 |  1 |  2 |  3 |  4 |  5 ║  6 |  7 ║
     ╟────┼────┼────┼────┼────╚════╧════╧════╧════╧════╧════╧════╧════╝────┼────╢
  75 ║  7 |  6 |  5 |  4 |  3 |  2 |  2 |  2 |  2 |  2 |  3 |  4 |  5 |  6 |  7 ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  60 ║  7 |  6 |  5 |  4 |  3 |  3 |  3 |  3 |  3 |  3 |  3 |  4 |  5 |  6 |  7 ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  45 ║  7 |  6 |  5 |  4 |  4 |  4 |  4 |  4 |  4 |  4 |  4 |  4 |  5 |  6 |  7 ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  30 ║  7 |  6 |  5 |  5 |  5 |  5 |  5 |  5 |  5 |  5 |  5 |  5 |  5 |  6 |  7 ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
  15 ║  7 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  6 |  7 ║
     ╟────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────╢
   0 ║  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 |  7 ║
     ╚════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╧════╝
        0    1    2    3    4    5    6    7    8    9    10   11   12   13   14

```

The index calculation is trivial as well but slightly more expensive than the 0x88 one. Of course, a small lookup table to map the indices might be appropriate.

## Applications

The main application of square distance is the static [evaluation](Evaluation "Evaluation") of the late [endgame](Endgame "Endgame"), where for instance races of the two kings to certain squares is often an issue - or in so called [Mop-up evaluation](Mop-up_Evaluation "Mop-up Evaluation"), which considers the distance between winning and losing king. [Boris Stilman](Boris_Stilman "Boris Stilman") gave following example to generate a set of [trajectories](Trajectory "Trajectory") for a king moving from f6 to h1 <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
D(f6,K)          +  D(h1,K)          =  SUM                 SUM == D(f6,h1)
5 4 3 2 2 2 2 2     7 7 7 7 7 7 7 7     c b a 9 9 9 9 9     . . . . . . . .
5 4 3 2 1 1 1 2     7 6 6 6 6 6 6 6     c a 9 8 7 7 7 8     . . . . . . . .
5 4 3 2 1 0 1 2     7 6 5 5 5 5 5 5     c a 8 7 6|5|6 7     . . . . . 1 . .
5 4 3 2 1 1 1 2     7 6 5 4 4 4 4 4     c a 8 6|5 5 5|6     . . . . 1 1 1 .
5 4 3 2 2 2 2 2  +  7 6 5 4 3 3 3 3  =  c a 8 6|5 5 5 5|    . . . . 1 1 1 1
5 4 3 3 3 3 3 3     7 6 5 4 3 2 2 2     c a 8 7 6|5 5 5|    . . . . . 1 1 1
5 4 4 4 4 4 4 4     7 6 5 4 3 2 1 1     c a 9 8 7 6|5 5|    . . . . . . 1 1
5 5 5 5 5 5 5 5     7 6 5 4 3 2 1 0     c b a 9 8 7 6|5|    . . . . . . . 1

```

## The Value of Reaching a Square

Distance as generalization of [mobility](Mobility "Mobility") and [evaluation](Evaluation "Evaluation") term was introduced by [Robert Levinson](Robert_Levinson "Robert Levinson") and [Richard Snyder](Richard_Snyder "Richard Snyder") in the famous 1993 [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Abstract and excerpt:

```C++This article suggests a new approach to computer chess. A graph-theoretic representation of chess knowledge, uniformly based on a single mathematical abstraction, Distance, is described. Most of the traditional forms of [chess knowledge](Knowledge "Knowledge"), it is shown, can be formalized in this new representation. In addition to comparing this approach to others, the article gives some experimental results and suggests how the new representation may be unified with existing approaches.

```

```C++The Distance idea is based on exploring a [piece's](Pieces "Pieces") [mobility](Mobility "Mobility") graph to determine what is close to and what is close to it. From a Distance standpoint, [moves](Moves "Moves") on the [chess-board](Chessboard "Chessboard") are only considered good if they result in improved movement graphs for the mover's pieces and/or inferior ones for the opponent's pieces. Often, a good chess-player will move a piece, not to improve the attacking chances of that piece but rather the attacking chances of the piece behind it. 

```

## See also

- [0x88 Square Relations](0x88#SquareRelations "0x88")
- [Center Distance](Center_Distance "Center Distance")
- [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
- [Connectivity](Connectivity "Connectivity")
- [Direction](Direction "Direction")
- [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
- [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
- [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism")
- [King Piece Tropism](King_Safety#KingTropism "King Safety")
- [Knight-Distance](Knight-Distance "Knight-Distance")
- [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance")
- [Mobility](Mobility "Mobility")
- [Vector Attacks](Vector_Attacks "Vector Attacks")

## Publications

- [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") » [WCCC 1992 - Workshop](WCCC_1992#Workshop "WCCC 1992")
- [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
- [Daniel Michulke](index.php?title=Daniel_Michulke&action=edit&redlink=1 "Daniel Michulke (page does not exist)"), [Stephan Schiffel](Stephan_Schiffel "Stephan Schiffel") (**2012**). *Distance Features for General Game Playing Agents*. [4. ICAART 2012](http://www.informatik.uni-trier.de/~ley/db/conf/icaart/icaart2012-1.html#MichulkeS12), [pdf](http://www.general-game-playing.de/downloads/GIGA11_Distance_Features.pdf) » [General Game Playing](General_Game_Playing "General Game Playing")

## Forum Posts

- [unique distance relationship](https://www.stmintz.com/ccc/index.php?id=245611) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 15, 2002
- [Distance to King](http://www.talkchess.com/forum/viewtopic.php?t=31571) by [Adam Berent](Adam_Berent "Adam Berent"), [CCC](CCC "CCC"), January 08, 2010 » [King Piece Tropism](King_Safety#KingTropism "King Safety")
- [Stockfish and latest +6 ELO patch!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73273) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 05, 2020 » [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff"), [Stockfish](Stockfish "Stockfish") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## External Links

- [Chebyshev distance from Wikipedia](https://en.wikipedia.org/wiki/Chebyshev_distance)
- [Distance (Proximity) from Wikipedia](https://en.wikipedia.org/wiki/Distance)
- [Euclidean distance from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_distance)
- [Manhattan distance from Wikipedia](https://en.wikipedia.org/wiki/Manhattan_distance)
- [Minkowski distance from Wikipedia](https://en.wikipedia.org/wiki/Minkowski_distance)
- [Moore neighborhood from Wikipedia](https://en.wikipedia.org/wiki/Moore_neighborhood)
- [Von Neumann neighborhood from Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_neighborhood)
- [Proxemics from Wikipedia](https://en.wikipedia.org/wiki/Proxemics)
- [Yes](Category:Yes "Category:Yes") - [Long Distance Runaround](https://en.wikipedia.org/wiki/Long_Distance_Runaround), [Fragile](https://en.wikipedia.org/wiki/Fragile_%28Yes_album%29) (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Jon Anderson](https://en.wikipedia.org/wiki/Jon_Anderson), [Steve Howe](https://en.wikipedia.org/wiki/Steve_Howe_%28musician%29), [Chris Squire](Category:Chris_Squire "Category:Chris Squire"), [Rick Wakeman](https://en.wikipedia.org/wiki/Rick_Wakeman), [Bill Bruford](Category:Bill_Bruford "Category:Bill Bruford")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - [Colors from a Distance](https://artsandculture.google.com/asset/colors-from-a-distance/kAHBsV7-F_nsQw), 1932, [The Israel Museum](https://en.wikipedia.org/wiki/Israel_Museum), [Google Arts & Culture](https://en.wikipedia.org/wiki/Google_Arts_%26_Culture)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Use equations for PushAway and PushClose · official-stockfish/Stockfish@5a7b45e · GitHub](https://github.com/official-stockfish/Stockfish/commit/5a7b45eac9dedbf7ebc61d9deb4dd934058d1ca1#diff-4cd6bcdb505b124d7bdc612c4789dc26L57-R59)

**[Up one Level](Squares "Squares")**

