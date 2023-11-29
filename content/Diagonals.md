---
title: Diagonals
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Diagonals**

[](http://www.cs.berkeley.edu/%7Eug/slide/gallery/kleinbottle/index.shtml) [Nexus](https://en.wikipedia.org/wiki/Nexus) of a [chessboard](Chessboard "Chessboard") [Klein bottle](https://en.wikipedia.org/wiki/Klein_bottle) <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>
**Diagonals** go from south-west to north-east on a chess board, the main diagonal is a1/h8. There are 15 diagonals, with line-length from 1 to 8. A Diagonal is monochrome, all their [squares](Squares "Squares") are either white or black.

## Main Diagonal

<img src="" alt="missing fen" style="
    width: 300px;
">

## Square Mapping Notes

A [90 degree rotation](Flipping_Mirroring_and_Rotating#Rotationby90degreesClockwise "Flipping Mirroring and Rotating") of the [Chessboard](Chessboard "Chessboard"), as well as [flipping vertically](Flipping_Mirroring_and_Rotating#FlipVertically "Flipping Mirroring and Rotating") (reversed [ranks](Ranks "Ranks")) or (exclusive) [mirroring horizontally](Flipping_Mirroring_and_Rotating#MirrorHorizontally "Flipping Mirroring and Rotating") (reversed [files](Files "Files")), change the roles of diagonals and [anti-diagonals](Anti-Diagonals "Anti-Diagonals"). However, we define the main diagonal on the chess board from a1/h8 and the main anti-diagonal from h1\\a8. Whether the square difference of neighbored squares on a diagonal or anti-diagonal is either 7 or 9, depends on the square mapping. We further rely on [little-endian rank-file mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations").

## Square Difference

Within a 0..63 square index range and the mentioned [square mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") (a1 = 0), the difference of two neighbored squares (if any) on a diagonal is **nine**.

## Enumeration

If we follow a diagonal from south-west (a1) to north-east (h8) step by step, we increment the rank, and increment the file, which yields in same difference. Thus, subtracting [rank](Ranks "Ranks") from [file](Files "Files") indices (or vice versa) enumerates all Diagonals, unfortunately with negative numbers involved, which can easily adjusted by adding seven.

- The main diagonal a1/h8 with index 0 and length 8.
- The diagonals a8/ and h1/ with length 1, are index 7 and -7 respectively.
- All even indices are the diagonals with dark [squares](Squares "Squares")

**rank - file**

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

**7 + rank - file**

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
|  14
|  13
|  12
|  11
|  10
|  9
|  8
|  7
|
|  6
|  13
|  12
|  11
|  10
|  9
|  8
|  7
|  6
|
|  5
|  12
|  11
|  10
|  9
|  8
|  7
|  6
|  5
|
|  4
|  11
|  10
|  9
|  8
|  7
|  6
|  5
|  4
|
|  3
|  10
|  9
|  8
|  7
|  6
|  5
|  4
|  3
|
|  2
|  9
|  8
|  7
|  6
|  5
|  4
|  3
|  2
|
|  1
|  8
|  7
|  6
|  5
|  4
|  3
|  2
|  1
|
|  0
|  7
|  6
|  5
|  4
|  3
|  2
|  1
|  0
|

## Alternative Enumeration

Some alternative enumeration of diagonals to keep the main-diagonal index 0, by anding the difference with 15. This yields in a 0..15 range with 8 as gap or [Nexus](https://en.wikipedia.org/wiki/Nexus) in the center of the range:

**(rank - file) & 15**

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
|  15
|
|  5
|  5
|  4
|  3
|  2
|  1
|  0
|  15
|  14
|
|  4
|  4
|  3
|  2
|  1
|  0
|  15
|  14
|  13
|
|  3
|  3
|  2
|  1
|  0
|  15
|  14
|  13
|  12
|
|  2
|  2
|  1
|  0
|  15
|  14
|  13
|  12
|  11
|
|  1
|  1
|  0
|  15
|  14
|  13
|  12
|  11
|  10
|
|  0
|  0
|  15
|  14
|  13
|  12
|  11
|  10
|  9
|

## Two Squares on a Diagonal

Two [Squares](Squares "Squares") are on the same Diagonal, if their file distance equals the rank distance

```C++

bool squaresOnSameDiagonal(int sq1, int sq2) {
  return ((sq2 - sq1) & 7) == ((sq2>>3) - (sq1>>3));
}

```

Alternatively, one may test whether the square difference is divisible by 9 <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```C++

bool squaresOnSameDiagonal(int sq1, int sq2) {
  return ((sq2 - sq1) % 9) == 0;
}

```

- [Two Squares on a Anti-Diagonal](Anti-Diagonals#TwoSquares "Anti-Diagonals")
- [Two Squares on a File](Files#TwoSquares "Files")
- [Two Squares on a Rank](Ranks#TwoSquares "Ranks")

## See also

- [Anti-Diagonals](Anti-Diagonals "Anti-Diagonals")
- [Ranks](Ranks "Ranks")
- [Files](Files "Files")
- [Squares](Squares "Squares")
- [Intersection Squares](Intersection_Squares "Intersection Squares")
- [Nexus](Nexus "Nexus") the chess program

## External Links

- [Diagonal from Wikipedia](https://en.wikipedia.org/wiki/Diagonal)
- [Main diagonal from Wikipedia](https://en.wikipedia.org/wiki/Main_diagonal)
- [Diagonal matrix from Wikipedia](https://en.wikipedia.org/wiki/Diagonal_matrix)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [What is a Klein Bottle?](http://www.kleinbottle.com/whats_a_klein_bottle.htm)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Nerius Landys and Shad Roundy Klein Bottle Project](http://www.cs.berkeley.edu/%7Eug/slide/gallery/kleinbottle/index.shtml)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Torus Games](http://www.geometrygames.org/TorusGames/) - players who master the [games](Games "Games") on the [Torus](https://en.wikipedia.org/wiki/Torus) may move on to try them on the more challenging Klein bottle
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [An undetected bug for 10 years](http://talkchess.com/forum3/viewtopic.php?f=7&t=74821) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), August 18, 2020

**[Up one Level](Chess "Chess")**

