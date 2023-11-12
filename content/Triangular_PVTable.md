---
title: Triangular PVTable
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Triangular PV-Table**



 [](http://www.elementsbylizzie.com/Furn_Tables.html) Triangular Table <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
A **Triangular PV-Table** is an [array](Array "Array") of [principal variations](Principal_Variation "Principal Variation") indexed by [ply](Ply "Ply") (distance to [root](Root "Root")). It is employed to [collect the principal variation](Principal_Variation#CollectionDuringSearch "Principal Variation") of [best moves](Best_Move "Best Move") inside an [alpha-beta](Alpha-Beta "Alpha-Beta") or [principal variation search](Principal_Variation_Search "Principal Variation Search") - like the best score propagated up to the root. Inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, it is most important to play the principal variation first during the next iteration. With some care in not overwriting [PV-nodes](Node_Types#PV "Node Types"), many programmers have abandoned PV-Table and reveal the PV from the [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Contents


* [1 Layout](#layout)
* [2 Implementations](#implementations)
	+ [2.1 One-Dimensional Array](#one-dimensional-array)
		- [2.1.1 Size](#size)
		- [2.1.2 Index](#index)
		- [2.1.3 Pseudo Code](#pseudo-code)
	+ [2.2 Quadratic PV-Table](#quadratic-pv-table)
	+ [2.3 Linked List on the Stack](#linked-list-on-the-stack)
	+ [2.4 Pointer Array](#pointer-array)
* [3 PV in PVS](#pv-in-pvs)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
	+ [5.1 1998 ...](#1998-...)
	+ [5.2 2000 ...](#2000-...)
	+ [5.3 2005 ...](#2005-...)
	+ [5.4 2010 ...](#2010-...)
	+ [5.5 2015 ...](#2015-...)
	+ [5.6 2020 ...](#2020-...)
* [6 External Links](#external-links)
* [7 References](#references)






Assuming a [maximum search depth](Depth#MaxPly "Depth") of N plies with pre-allocated [stacks](Stack "Stack"), the maximum possible PV-length decreases with increasing distance to root aka ply index during search, and actually needs one move less each ply deeper.




```C++
maxLengthPV(ply) = N - ply

```

Therefor the triangular structure.




```C++

ply  maxLengthPV
    +--------------------------------------------+
0   |N                                           |
    +------------------------------------------+-+
1   |N-1                                       |
    +----------------------------------------+-+
2   |N-2                                     |
    +--------------------------------------+-+
3   |N-3                                   |
    +------------------------------------+-+
4   |N-4                                 |
...                        /
N-4 |4      |
    +-----+-+
N-3 |3    |
    +---+-+
N-2 |2  |
    +-+-+
N-1 |1|
    +-+

```

## Implementations


### One-Dimensional Array


### Size


The total size of the triangular array in moves can be calculated by the [Triangular number](https://en.wikipedia.org/wiki/Triangular_number):




```C++
size = 1+2+3+ ... +(N-1)+N = ½ N(N+1)

```

### Index


To calculate the index or offset of a PV into a one-dimensional move array by ply either requires storing incremental offsets




```C++
index(0) = 0 
index(ply+1) = index(ply) + N - ply 

```

or variable multiplication from scratch:




```C++
index(ply) = ½ ply (2N + 1 - ply )

```

This index calculation might as well be replaced by a redirection via a small pre-calculated lookup table with N entries of indices, pointers or references, similar to two-dimensional [Java](Java "Java") arrays as arrays of arrays with different size <a id="cite-note-4" href="#cite-ref-4">[4]</a> .



### Pseudo Code


A didactic implementation of the Triangular PV-Table inside an [Alpha-Beta](Alpha-Beta "Alpha-Beta") routine. The routine *movcpy* copies up to *n* moves, but may terminate after copying a null move. To avoid the second condition, it is quite common to store the current length of the PV inside a PV structure.




```C++

MoveType pvArray[(N*N + N)/2];

void movcpy (MoveType* pTarget, const MoveType* pSource, int n) {
   while (n-- && (*pTarget++ = *pSource++));
}

int AlphaBeta(int alpha, int beta, int depth, int ply, int pvIndex) {
   ...
   pvArray[pvIndex] = 0; // no pv yet
   pvNextIndex = pvIndex + N - ply;
   while ( move = getNextMove() ) {
      make (move);
      score = -AlphaBeta(-beta, -alpha, depth-1, ply+1, pvNextIndex);
      unmake (move);
      ...
      if (score > alpha) {
         alpha = score;
         pvArray[pvIndex] = move;
         movcpy (pvArray + pvIndex + 1, pvArray + pvNextIndex, N - ply - 1);
      }
   }
   ...

```

### Quadratic PV-Table


To avoid the above index calculation, many programmers roughly double the table space for an homogeneous two-dimensional array with all PVs of maximum size N. This allows cheaper indexing due the multiplication by the constant N only, possibly replaced by cheap instructions, i.e. shift for N == 128 (power of two).




### Linked List on the Stack


An option in [C](C "C") as well in [Java](Java "Java") is to reserve space for one PV on the [stack](Stack "Stack") as automatic variable inside the [recursive](Recursion "Recursion") search routine, and to pass a reference or pointer to the child nodes as [demonstrated](index.php?title=Principal_variation&action=edit&redlink=1 "Principal variation (page does not exist)") by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") <a id="cite-note-5" href="#cite-ref-5">[5]</a> . Inside [PVS](Principal_Variation_Search "Principal Variation Search"), these arrays are not needed in the [zero window search](Principal_Variation_Search#ZWS "Principal Variation Search") at all, and, [C99](C "C") conform [variable-length arrays](https://en.wikipedia.org/wiki/Variable-length_array) on [the stack](Array#Stack "Array") are the way to "half" the required stacksize for linked "triangular" PV-arrays.



### Pointer Array


Another alternative is an array of N pointers to global, homogeneous PV-arrays with size N each. Instead of copying moves alá memcpy, one may swap pointers. While this sounds promising at the first glance, the copy costs are negligible since PV-Nodes and raising alpha are quite rare.




## PV in PVS


As demonstrated by [Daniel Shawul](Daniel_Shawul "Daniel Shawul") with [TSCP](TSCP "TSCP") <a id="cite-note-6" href="#cite-ref-6">[6]</a> , and explained by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-7" href="#cite-ref-7">[7]</a> , inside a [perfectly stable](Search_Instability "Search Instability") [NegaScout](NegaScout "NegaScout") aka [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), a [fail-high](Fail-High "Fail-High") at a [PV-node](Node_Types#PV "Node Types") compared to a [null window](Null_Window "Null Window") is always confirmed by the re-search with an [exact score](Exact_Score "Exact Score") improving [alpha](Alpha "Alpha") and will either become part of a new PV at the [root](Root "Root") or overwritten by a further improvement. Thus, under such conditions, there is no need to keep an array of [principal variations](Principal_Variation "Principal Variation"), but only one.




```C++

MoveType pvArray[N];

```

However, with a [transposition table](Transposition_Table "Transposition Table"), [aspiration](Aspiration_Windows "Aspiration Windows"), [selectivity](Selectivity "Selectivity") and that like, one cannot guarantee such stable behavior.



## See also


* [Best Move](Best_Move "Best Move")
* [Hash Move](Hash_Move "Hash Move")
* [Killer Move](Killer_Move "Killer Move")
* [Principal Variation](Principal_Variation "Principal Variation")
* [PV-Move](PV-Move "PV-Move")
* [Refutation Table](Refutation_Table "Refutation Table")


## Forum Posts


### 1998 ...


* [Storing the PV in a search routine](https://www.stmintz.com/ccc/index.php?id=20265) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), June 09, 1998


### 2000 ...


* [PV array](https://www.stmintz.com/ccc/index.php?id=258053) by Nagendra Singh Tomar, [CCC](CCC "CCC"), October 10, 2002
* [triangular pv vs. hash move pv](https://www.stmintz.com/ccc/index.php?id=387179) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 11, 2004
* [Instability thing...](https://www.stmintz.com/ccc/index.php?id=388106) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), September 18, 2004


### 2005 ...


* [Extracting PV from TT](http://www.talkchess.com/forum/viewtopic.php?t=29730) by Colin, [CCC](CCC "CCC"), September 12, 2009


### 2010 ...


* [Taken from CCC (Stockfish & mainlines)](http://www.open-chess.org/viewtopic.php?f=5&t=434) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2010
* [Full Principal Variation Retrieval](http://www.talkchess.com/forum/viewtopic.php?t=35982) by [Hieu Nguyen](index.php?title=Hieu_Nguyen&action=edit&redlink=1 "Hieu Nguyen (page does not exist)"), [CCC](CCC "CCC"), September 06, 2010 <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [restartable nodes and the tri-angular array](http://www.talkchess.com/forum/viewtopic.php?t=44371) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 11, 2012
* [triangular pv](http://www.talkchess.com/forum/viewtopic.php?t=47573) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 22, 2013


### 2015 ...


* [Collecting Principal variation](http://www.talkchess.com/forum/viewtopic.php?t=55819) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), March 29, 2015
* [Collecting PVs of Qsearch ?](http://www.talkchess.com/forum/viewtopic.php?t=61796) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 22, 2016 » [Principal Variation](Principal_Variation "Principal Variation"), [Quiescence Search](Quiescence_Search "Quiescence Search")
* [capturing PV in QSearch](http://www.open-chess.org/viewtopic.php?f=5&t=3072) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2017
* [Collecting PV in a PVS search ?](http://www.talkchess.com/forum/viewtopic.php?t=64256) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 11, 2017 » [Principal Variation](Principal_Variation "Principal Variation")


### 2020 ...


* [Confused About Triangular PV Table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77431) by shahil4242, [CCC](CCC "CCC"), June 03, 2021


## External Links


* [Collecting the Principal Variation](http://web.archive.org/web/20040427013839/brucemo.com/compchess/programming/pv.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
* [Sonny Stitt](https://en.wikipedia.org/wiki/Sonny_Stitt) - [The Eternal Triangle](https://en.wikipedia.org/wiki/The_Champ_(Sonny_Stitt_album)) <a id="cite-note-9" href="#cite-ref-9">[9]</a>, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Joe Newman](https://en.wikipedia.org/wiki/Joe_Newman_(trumpeter)), [Duke Jordan](https://en.wikipedia.org/wiki/Duke_Jordan), [Sam Jones](https://en.wikipedia.org/wiki/Sam_Jones_(musician)), [Roy Brooks](https://en.wikipedia.org/wiki/Roy_Brooks)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Elements by Lizzie Furniture - Tables](http://www.elementsbylizzie.com/Furn_Tables.html) by [Elizabeth Battaglia](http://www.elementsbylizzie.com/Home_Page.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [triangular pv vs. hash move pv](https://www.stmintz.com/ccc/index.php?id=387179) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 11, 2004
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Extracting PV from TT](http://www.talkchess.com/forum/viewtopic.php?t=29730) by Colin, [CCC](CCC "CCC"), September 12, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Java: Two-dimensional arrays as arrays of arrays](http://leepoint.net/notes-java/data/arrays/arrays-2D-2.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Collecting the Principal Variation](http://web.archive.org/web/20040427013839/brucemo.com/compchess/programming/pv.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: triangular pv](http://www.talkchess.com/forum/viewtopic.php?t=47573&start=4) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 22, 2013
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: triangular pv](http://www.talkchess.com/forum/viewtopic.php?t=47573&start=10) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 22, 2013
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> See also [Robert Hyatt's](Robert_Hyatt "Robert Hyatt") [idea](Principal_Variation#SeparateTT "Principal Variation") from the [principal variation page](Principal_Variation "Principal Variation")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [List of jazz contrafacts from Wikipedia](https://en.wikipedia.org/wiki/List_of_jazz_contrafacts)

**[Up one Level](Data "Data")**







 
