---
title: Intersection Squares
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Squares](Squares "Squares") \* Intersection Squares**



 [](http://www.mcescher.com/Gallery/back-bmp/LW377.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher") - Two Intersecting Planes, 1952 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Intersection squares** are the result of the [intersection of two lines](https://en.wikipedia.org/wiki/Line-line_intersection) from two different squares with two disjoint directions, either [rank](Ranks "Ranks"), [file](Files "Files"), [diagonal](Diagonals "Diagonals") or [anti-diagonal](Anti-Diagonals "Anti-Diagonals"), in total 2\*(3+2+1) = 12 possible combinations. Those lines (may) have up to one square, where both lines intersect - a square where two appropriate sliding pieces were able to move to in one step (assuming no obstructions).


In the set-wise world of [bitboards](Bitboards "Bitboards") one usually relies on [set-wise intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), but square-centric [board representations](Board_Representation "Board Representation") may either use two-dimensional lookup tables, or rely on some algebra based on discrete [linear equations](https://en.wikipedia.org/wiki/Linear_equation) and pure register computation. Programs may use these routines as a precondition whether an intersection point exist, for instance to determine a square where a sliding piece may check the opponent king. 



## Empty Intersection with 0x88 Math


If diagonals or anti-diagonals are involved, the intersection square may off the board. Beside that, the intersection of a diagonal with an anti-diagonal becomes empty, if both lines are of different [square color](Color_of_a_Square "Color of a Square"). Considering [0x88](0x88 "0x88")-square coordinates for the calculation, covers off the board intersection, and the different color issues en passant. Following [C](C "C")-routines work branchless, and return -1 if no intersection is possible by oring with following {0,-1} integer expression relying on arithmetical shift right:




```C++
 -(s88 & 0x88) >> (sizeof(int)-1)

```

Feel free to use branches instead in a broader scope, since one need to branch on valid intersecion square anyway.



## Rank and Diagonal


or vice versa Diagonal and Rank




```C++
. . . . . . / .
. . . . . b . .
. . . . / . . .
. . . / . . . .
. . / . . . . .
. / . . . . . .
s-----a--------
. . . . . . . .

```

with




```C++diagonalIndex := rankIndex - fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |
|  6
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |
|  5
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |
|  4
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |
|  3
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |
|  2
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |
|  1
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |
|  0
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |  -7
 |


### 0x88 Math



```C++
rankIndex(s) := rankIndex(a);
fileIndex(s) := rankIndex(s) - diagonalIndex(s);
fileIndex(s) := rankIndex(a) - rankIndex(b) + fileIndex(b);

```

Because the intersection of any rank with any diagonal may off the board, we rely on 0x88 math for a quick test:




```C++
s88 := 16*rankIndex(s) + fileIndex(s);
s88 := 16*rankIndex(a) + (rankIndex(a) - rankIndex(b) + fileIndex(b));
s88 := 17*rankIndex(a) -  rankIndex(b) + fileIndex(b);
if ( s88 & 0x88)
   intersection off board;
else
   sq := ((sq88 >> 1) & 56) + (sq88 & 7);

```

### C-Source



```C++
/****************************************
 * return: intersection square (if any)
 *          of rank of square a
 *          with diagonal of square b
 *         -1 if no intersection exists
 ****************************************/
int intersectRankDia(int a, int b) {
   int s88 = 17*(a>>3) - (b >> 3) + (b & 7);
   return (((s88 >> 1) & 56) + (s88 & 7)) | ( -(s88 & 0x88) >> 31);
}

```

## File and Diagonal


or vice versa Diagonal and File




```C++
. . . | . . / .
. . . | . b . .
. . . | / . . .
. . . s . . . .
. . / | . . . .
. / . | . . . .
/ . . a . . . .
. . . | . . . .

```

with




```C++diagonalIndex := rankIndex - fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |
|  6
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |
|  5
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |
|  4
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |
|  3
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |
|  2
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |
|  1
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |
|  0
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |  -7
 |


### 0x88 Math



```C++
fileIndex(s) := fileIndex(a);
rankIndex(s) := fileIndex(s) + diagonalIndex(s);
rankIndex(s) := fileIndex(a) + rankIndex(b) - fileIndex(b);

```

Because the intersection of any file with any diagonal may off the board, we rely on 0x88 math for a quick test:




```C++
s88 := 16*rankIndex(s) + fileIndex(s);
s88 := 16*(fileIndex(a) + rankIndex(b) - fileIndex(b)) + fileIndex(a);
s88 := 17*fileIndex(a) + 16*rankIndex(b) - 16*fileIndex(b);
if ( s88 & 0x88)
   intersection off board;
else
   sq := ((sq88 >> 1) & 56) + (sq88 & 7);

```

### C-Source



```C++
/****************************************
 * return: intersection square (if any)
 *          of file of square a
 *          with diagonal of square b
 *         -1 if no intersection exists
 ****************************************/
int intersectFileDia(int a, int b) {
   int s88 = 17*(a & 7) + 2*(b & 56) - 16*(b & 7);
   return (((s88 >> 1) & 56) + (s88 & 7)) | ( -(s88 & 0x88) >> 31);
}

```

## Rank and Anti-Diagonal


or vice versa Anti-Diagonal and Rank




```C++
. . . . . . . .
. . . . . . . .
\ . . . . . . .
. b . . . . . .
. . \ . . . . .
. . . \ . . . .
------a-s------
. . . . . \ . .

```

with




```C++antidiagIndex := rankIndex + fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |  14
 |
|  6
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |
|  5
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |
|  4
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |
|  3
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |
|  2
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |
|  1
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |
|  0
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |


### 0x88 Math



```C++
rankIndex(s) := rankIndex(a);
fileIndex(s) := antidiagIndex(s) - rankIndex(s);
fileIndex(s) := rankIndex(a) -  rankIndex(b) + fileIndex(b);

```

Because the intersection of any rank with any anti-diagonal may off the board, we rely on 0x88 math for a quick test:




```C++
s88 := 16*rankIndex(s) + fileIndex(s);
s88 := 16*rankIndex(a) + rankIndex(a) -  rankIndex(b) + fileIndex(b);
s88 := 17*rankIndex(a) - rankIndex(b) + fileIndex(b);
if ( s88 & 0x88)
   intersection off board;
else
   sq := ((sq88 >> 1) & 56) + (sq88 & 7);

```

### C-Source



```C++
/****************************************
 * return: intersection square (if any)
 *          of rank of square a
 *          with anti-diagonal of square b
 *         -1 if no intersection exists
 ****************************************/
int intersectRankAnt(int a, int b) {
   int s88 = 17*(a >> 3) - (b >> 3) + (b & 7);
   return (((s88 >> 1) & 56) + (s88 & 7)) | ( -(s88 & 0x88) >> 31);
}

```

## File and Anti-Diagonal


or vice versa Anti-Diagonal and File




```C++
. . . | . . . .
. . . | . . . .
\ . . | . . . .
. b . | . . . .
. . \ | . . . .
. . . s . . . .
. . . a \ . . .
. . . | . \ . .

```

with




```C++antidiagIndex := rankIndex + fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |  14
 |
|  6
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |
|  5
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |
|  4
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |
|  3
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |
|  2
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |
|  1
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |
|  0
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |


### 0x88 Math



```C++
fileIndex(s) := fileIndex(a);
rankIndex(s) := antidiagIndex(s) - fileIndex(s);
rankIndex(s) := rankIndex(b) + fileIndex(b) - fileIndex(a);

```

Because the intersection of any rank with any anti-diagonal may off the board, we rely on 0x88 math for a quick test:




```C++
s88 := 16*rankIndex(s) + fileIndex(s);
s88 := 16*(rankIndex(b) + fileIndex(b) - fileIndex(a)) + fileIndex(a);
s88 := 16*rankIndex(b) + 16*fileIndex(b) - 15*fileIndex(a);
if ( s88 & 0x88)
   intersection off board;
else
   sq := ((sq88 >> 1) & 56) + (sq88 & 7);

```

### C-Source



```C++
/****************************************
 * return: intersection square (if any)
 *          of file of square a
 *          with anti-diagonal of square b
 *         -1 if no intersection exists
 ****************************************/
int intersectFileAnt(int a, int b) {
   int s88 = 2*(b & 56) + 16*(b & 7) - 15*(a & 7);
   return (((s88 >> 1) & 56) + (s88 & 7)) | ( -(s88 & 0x88) >> 31);
}

```

## Diagonal and Anti-Diagonal


or vice versa Anti-Diagonal and Diagonal




```C++
. . . . . . . .
. . . . . . . /
\ . . . . . / .
. b . . . / . .
. . \ . / . . .
. . . s . . . .
. . a . \ . . .
. / . . . \ . .

```

with




```C++diagonalIndex := rankIndex - fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |
|  6
 |  6
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |
|  5
 |  5
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |
|  4
 |  4
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |
|  3
 |  3
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |
|  2
 |  2
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |
|  1
 |  1
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |
|  0
 |  0
 |  -1
 |  -2
 |  -3
 |  -4
 |  -5
 |  -6
 |  -7
 |


and




```C++antidiagIndex := rankIndex + fileIndex;

```



|  r/f
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  7
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |  14
 |
|  6
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |  13
 |
|  5
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |  12
 |
|  4
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |  11
 |
|  3
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |  10
 |
|  2
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |  9
 |
|  1
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |  8
 |
|  0
 |  0
 |  1
 |  2
 |  3
 |  4
 |  5
 |  6
 |  7
 |


### 0x88 Math


For same file and rank of intersection-point s:




```C++
rankIndex(s) - diagonalIndex(a) ==  antidiagIndex(b) - rankIndex(s);
fileIndex(s) + diagonalIndex(a) ==  antidiagIndex(b) - fileIndex(s);

```

and therefor




```C++
2*rankIndex(s) == antidiagIndex(b) + diagonalIndex(a);
2*fileIndex(s) == antidiagIndex(b) - diagonalIndex(a);

```

Because the intersection of any rank with any anti-diagonal may off the board, we rely on 0x88 math for a quick test:




```C++
s88   = 16*rankIndex(s) + fileIndex(s);

```

equation times two:




```C++
s88x2 = 16*2*rankIndex(s) + 2*fileIndex(s);
s88x2 = 16*(antidiagIndex(b) + diagonalIndex(a)) + (antidiagIndex(b) - diagonalIndex(a) );
s88x2 = 17*antidiagIndex(b) + 15*diagonalIndex(a);
if ( s88x2 & 0x111)
   intersection off board or empty;
else
   sq := ((sq882 >> 2) & 56) + ((sq88>>1) & 7);

```

Additionally, s88x2 becomes odd if a and b have different [square colors](Color_of_a_Square "Color of a Square"), if s88x2 & 0x110 is true, the square is off the board. In both cases there is no intersection square, which can be combined by one test with 0x111. If AND 0x111 is false, we convert 0x88 coordinates to ordinary square coordinates, which might be done "speculative".



### C-Source



```C++
/****************************************
 * return: intersection square (if any)
 *          of diagonal of square a
 *          with antidiagonal of square b
 *         -1 if no intersection exists
 ****************************************/
int intersectDiaAnt(int a, int b) {
   int s88x2 = 17*((b>>3) + (b & 7)) + 15*((a>>3) - (a & 7));
   return (((s88x2>>2)&56) + ((s88x2>>1)&7)) | ( -(s88x2&0x0111) >> 31);
}

```

## See also


* [Checks and Pinned Pieces (Bitboards)](Checks_and_Pinned_Pieces_(Bitboards) "Checks and Pinned Pieces (Bitboards)")


## External Links


* [Line-Line Intersection](http://mathworld.wolfram.com/Line-LineIntersection.html) from [Wolfram MathWorld](http://mathworld.wolfram.com/)
* [Line-line intersection from Wikipedia](https://en.wikipedia.org/wiki/Line-line_intersection)
* [Line (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Line_%28geometry%29)
* [Linear equations from Wikipedia](https://en.wikipedia.org/wiki/Linear_equation)
* [Crossroads (culture) from Wikipedia](https://en.wikipedia.org/wiki/Crossroads_%28culture%29)
* [Sun Ra](Category:Sun_Ra "Category:Sun Ra") - Where Pathways Meet, from [Lanquidity](https://en.wikipedia.org/wiki/Lanquidity) (1978), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/gallery-back.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)

**[Up one Level](Squares "Squares")**







 
