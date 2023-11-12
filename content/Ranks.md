---
title: Ranks
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* Ranks**


**Ranks** are the eight horizontal lines or rows of a [Chessboard](Chessboard "Chessboard"), labeled from '1' to '8'. Each rank contains eight horizontally arranged [Squares](Squares "Squares") of alternating white and black, or light and dark [Color](Color "Color"). 



### Contents


* [1 Back Ranks](#back-ranks)
* [2 Square Mapping Notes](#square-mapping-notes)
* [3 Square Difference](#square-difference)
* [4 Enumeration](#enumeration)
* [5 Rank from Square](#rank-from-square)
* [6 Rank-Distance](#rank-distance)
* [7 Two Squares on a Rank](#two-squares-on-a-rank)
* [8 See also](#see-also)
* [9 References](#references)






The First Rank is White's back rank, while the Eights Rank is Black's back rank.





|  |  |  |
| --- | --- | --- |
|  | abcdefgh |  |
| 87654321 |                                                                                                 ••••••••                                                •••••••• | 87654321 |
|  | abcdefgh |  |


## Square Mapping Notes


Whether the square difference of neighbored squares on a rank or [file](Files "Files") is either 1 or 8, depends on the square mapping. We further rely on [little-endian rank-file mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"), which keeps consecutive [squares](Squares "Squares") of a rank as neighbored elements in Memory (or register).



## Square Difference


Within a 0..63 square index range and the mentioned [square mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") (a1 = 0), the difference of two neighbored squares on a Rank is **one**.



## Enumeration


As mentioned, on a [Chessboard](Chessboard "Chessboard") the eight ranks are labeled from '1' to '8'. To make them zero based indices as appropriate for [C](C "C")-like programming languages, we enumerate ranks from 0 to 7. [Little-endian](Little-endian "Little-endian") rank-mapping (as used here) assigns the first Rank to index zero. Three bits are required to enumerate from 0 to 7.


A [little-endian](Little-endian "Little-endian") rank-mapping enumeration in [C++](Cpp "Cpp") might look like this: 




```C++

enum enumRank {
  er1stRank = 0,
  er2ndRank = 1,
  er3rdRank = 2,
  er4thRank = 3,
  er5thRank = 4,
  er6thRank = 5,
  er7thRank = 6,
  er8thRank = 7,
};

```

## Rank from Square


Rank-File mapping of squares keeps the rank index as the three upper bits of a six bit Square index.




```C++

rank = square >> 3; // div 8

```





## Rank-Distance


The rank-distance is the [absolute](Avoiding_Branches#Abs "Avoiding Branches") difference between two ranks (their 0-7 indices). The maximum rank-distance is 7.




```C++

rankDistance = abs (rank1 - rank2);
rankDistance = abs (rank2 - rank1);

```





## Two Squares on a Rank


Two [Squares](Squares "Squares") are on the same Rank, if their Rank distance is zero. 




```C++

bool squaresOnSameRank(int sq1, int sq2) {
 return ((sq2 >> 3) - (sq1 >> 3)) == 0;
}

```

The [Symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) aka xor is sufficent for the test of the rank bits as well <a id="cite-note-1" href="#cite-ref-1">[1]</a>




```C++

bool squaresOnSameRank(int sq1, int sq2) {
 return ((sq1 ^ sq2) & 56) == 0;
}

```

* [Two Squares on a File](Files#TwoSquares "Files")
* [Two Squares on a Diagonal](Diagonals#TwoSquares "Diagonals")
* [Two Squares on a Anti-Diagonal](Anti-Diagonals#TwoSquares "Anti-Diagonals")


## See also


* [Files](Files "Files")
* [Diagonals](Diagonals "Diagonals")
* [Anti-Diagonals](Anti-Diagonals "Anti-Diagonals")
* [Squares](Squares "Squares")
* [Intersection Squares](Intersection_Squares "Intersection Squares")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [An undetected bug for 10 years](http://talkchess.com/forum3/viewtopic.php?f=7&t=74821) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), August 18, 2020

**[Up one Level](Chess "Chess")**







 
