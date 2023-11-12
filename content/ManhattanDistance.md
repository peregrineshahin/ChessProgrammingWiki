---
title: ManhattanDistance
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Squares](Squares "Squares") \* Manhattan-Distance**



[ Manhattan-Distance [Voronoi Diagram](https://en.wikipedia.org/wiki/Voronoi_diagram) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **Manhattan-Distance** between two squares is determined by the minimal number of orthogonal [King](King "King") [moves](Moves "Moves") between these squares on the otherwise empty board, also called Taxicab- or Taxi-Distance - opposed to [Chebyshev Distance](Distance "Distance"), which may be shorter due to diagonal moves. Manhattan-Distance and Distance are equal for squares on a common [file](Files "Files") or [rank](Ranks "Ranks"). 


The underlying metric what has become known as [taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry) was first proposed as a means of creating a [non-Euclidean geometry](https://en.wikipedia.org/wiki/Non-Euclidean_geometry) by [Hermann Minkowski](Mathematician#Minkowski "Mathematician") early in the 20th century <a id="cite-note-2" href="#cite-ref-2">[2]</a>. In 1952, [Karl Menger](Mathematician#KMenger "Mathematician") created a geometry exhibit at the [Museum of Science and Industry](https://en.wikipedia.org/wiki/Museum_of_Science_and_Industry_%28Chicago%29) in [Chicago](https://en.wikipedia.org/wiki/Chicago). Menger also created a booklet entitled *You Will Like Geometry* <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>. It was in this booklet that the term "taxicab geometry" was first used <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Contents


* [1 Definition](#definition)
* [2 Application](#application)
* [3 Routine](#routine)
* [4 Lookup](#lookup)
* [5 Lookup by 0x88 Difference](#lookup-by-0x88-difference)
* [6 See also](#see-also)
* [7 Forum Posts](#forum-posts)
* [8 External Links](#external-links)
* [9 References](#references)






The Manhattan-Distance is the sum of the absolute [rank-distance](Ranks#RankDistance "Ranks") and [file-distance](Files#FileDistance "Files") of both squares.




```C++
Dtaxi = |r2 - r1| + |f2 - f1|

```

* The minimum square Manhattan-Distance is 0 (if both squares are equal)
* The maximum square Manhattan-Distance is 14 (between the endpoints of the main-diagonals)


## Application


The main application of square Manhattan-Distance (in conjunction with [Distance](Distance "Distance")) is the static [evaluation](Evaluation "Evaluation") of the late [endgame](Endgame "Endgame"), where for instance races of the two king to certain squares is often an issue - or in so called [Mop-up evaluation](Mop-up_Evaluation "Mop-up Evaluation"), which considers the Manhattan-Distance between winning and losing king.



## Routine


The following [C](C "C")-routine performs the computation. One may use the mentioned square-, rank- or file-enumeration types instead of the used integers, or rely on anonymous enumeration in [C](C "C") or [C++](Cpp "Cpp") treated as integers anyway. One should use the [abs](Avoiding_Branches#Abs "Avoiding Branches") function for a likely branchless implementation.




```C++

int manhattanDistance(int sq1, int sq2) {
   int file1, file2, rank1, rank2;
   int rankDistance, fileDistance;
   file1 = sq1  & 7;
   file2 = sq2  & 7;
   rank1 = sq1 >> 3;
   rank2 = sq2 >> 3;
   rankDistance = abs (rank2 - rank1);
   fileDistance = abs (file2 - file1);
   return rankDistance + fileDistance;
}

```

## Lookup


Since the computation is relative expensive, often two dimensional tables with precalculated values are used for that purpose. A [Byte](Byte "Byte") as lowest addressable unit is more than enough and easily zero extended:




```C++

unsigned char arrManhattanDistance[64][64]; // 4 KByte

inline int manhattanDistance(enumSquare sq1, enumSquare sq2) {
   return arrManhattanDistance[sq1][sq2];
}

```

## Lookup by 0x88 Difference


The [0x88](0x88 "0x88") [square relation](0x88#SquareRelations "0x88") permits a denser lookup approach. The difference of valid 0x88 coordinates of two squares is uniquely with respect to [Distance](Distance "Distance"), Manhattan-Distance and [Direction](Direction "Direction"). That way, one can greatly reduce the size of the lookup [array](Array "Array") to only 240 instead of 4096 elements. Some additional computation required, if one has to convert usual square coordinates to 0x88. If one already relies on 0x88 coordinates, it becomes even cheaper:




```C++

unsigned char arrManhattanDistanceBy0x88Diff[240];

unsigned int x88diff(enumSquare sq1, enumSquare sq2) {
   return sq2 - sq1 + (sq2|7) - (sq1|7) + 120;
}

inline int manhattanDistance(enumSquare sq1, enumSquare sq2) {
   return arrManhattanDistanceBy0x88Diff[x88diff(sq1, sq2)];
}

```

## See also


* [0x88 Square Relations](0x88#SquareRelations "0x88")
* [Center Distance](Center_Distance "Center Distance")
* [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
* [Direction](Direction "Direction")
* [Distance](Distance "Distance")
* [KBNK Endgame](KBNK_Endgame "KBNK Endgame")
* [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism")
* [Knight-Distance](Knight-Distance "Knight-Distance")
* [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")


## Forum Posts


* [unique distance relationship](https://www.stmintz.com/ccc/index.php?id=245611) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 15, 2002


## External Links


* [Manhattan-Distance from Wikipedia](https://en.wikipedia.org/wiki/Taxicab_geometry)
* [Taxicab Geometry - Home](http://taxicabgeometry.net/index.html)


 [Taxicab Geometry - History](http://taxicabgeometry.net/general/history.html)
* [Von Neumann neighborhood from Wikipedia](https://en.wikipedia.org/wiki/Von_Neumann_neighborhood)
* [CAB](Category:CAB "Category:CAB") - Decisions, [Tony MacAlpine](https://en.wikipedia.org/wiki/Tony_MacAlpine), [Bunny Brunel](https://en.wikipedia.org/wiki/Bunny_Brunel), [Dennis Chambers](Category:Dennis_Chambers "Category:Dennis Chambers"), [Brian Auger](Category:Brian_Auger "Category:Brian Auger"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [CAB live](Category:CAB "Category:CAB"), [Tony MacAlpine](https://en.wikipedia.org/wiki/Tony_MacAlpine), [Bunny Brunel](https://en.wikipedia.org/wiki/Bunny_Brunel), [Virgil Donati](https://en.wikipedia.org/wiki/Virgil_Donati), [Patrice Rushen](https://en.wikipedia.org/wiki/Patrice_Rushen), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Voronoi Diagram, named after [Georgy Voronoy](Mathematician#Voronoy "Mathematician"), using Manhattan distance metric, by user: Raincomplex, November 06, 2013, [Voronoi diagram from Wikipedia](https://en.wikipedia.org/wiki/Voronoi_diagram)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Hermann Minkowski](Mathematician#Minkowski "Mathematician"), [Andreas Speiser](Mathematician#ASpeiser "Mathematician"), [Hermann Weyl](Mathematician#Weyl "Mathematician"), [David Hilbert](Mathematician#Hilbert "Mathematician") (**1911**). *Gesammelte Abhandlungen von Hermann Minkowski*. [republished](http://www.worldcat.org/title/gesammelte-abhandlungen-von-hermann-minkowski-vol-1-2/oclc/750691126?referer=di&ht=edition) by [Chelsea Publishing Co.](http://www.ams.org/bookstore/chelsea), New York, 1967
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a>  [Karl Menger](Mathematician#KMenger "Mathematician") (**1952**). *You Will Like Geometry*. Guidebook of the [Illinois Institute of Technology](https://en.wikipedia.org/wiki/Illinois_Institute_of_Technology) Geometry Exhibit, [Museum of Science and Industry](https://en.wikipedia.org/wiki/Museum_of_Science_and_Industry_%28Chicago%29), Chicago, Illinois
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Louise Golland](http://science.iit.edu/applied-mathematics/about/about-karl-menger) (**1990**). *Karl Menger and Taxicap Geomery*. [Mathematics Magazine](https://en.wikipedia.org/wiki/Mathematics_Magazine), Vol. 63. No. 5,[pdf](http://taxicabgeometry.net/docs/mirror/Golland.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Taxicab Geometry - History](http://taxicabgeometry.net/general/history.html)

**[Up one Level](Squares "Squares")**







 
