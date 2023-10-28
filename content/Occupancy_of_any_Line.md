---
title: Occupancy of any Line
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* Occupancy of any Line**



 [](File:Besetzt20160916.JPG) Line Occupancy <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Occupancy of any Line**,  

unlike [rank attacks](First_Rank_Attacks "First Rank Attacks"), the problem arises for [files](Files "Files") and [diagonals](Diagonals "Diagonals") how to get scattered [occupancies](Occupancy "Occupancy") to consecutive [bits](Bit "Bit") of a dense lookup index. In the past, prior to early 2000, 64-bit [multiplication](General_Setwise_Operations#Multiplication "General Setwise Operations") was unfeasible - much too slow. 



### Contents


* [1 Avoiding Multiplication](#avoiding-multiplication)
	+ [1.1 Rotated Bitboards](#rotated-bitboards)
	+ [1.2 Collapsed Files](#collapsed-files)
	+ [1.3 Collapsed Ranks](#collapsed-ranks)
* [2 Using Multiplication](#using-multiplication)
	+ [2.1 Collapsed Files](#collapsed-files-2)
	+ [2.2 Collapsed Ranks](#collapsed-ranks-2)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






### Rotated Bitboards


One solution was the invention of [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") - to keep and maintain three additional rotated occupied bitboards, with consecutive bits for the appropriate rays. Similar to the bit-layout mentioned in [rotate by 90 degrees](Flipping_Mirroring_and_Rotating#Rotationby90degreesClockwise "Flipping Mirroring and Rotating") and [pseudo rotate by 90 degrees](Flipping_Mirroring_and_Rotating#PseudoRotationby45degrees "Flipping Mirroring and Rotating").




### Collapsed Files


Other techniques were about to hash the masked line with [parallel prefix shifts](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") to collapse [ranks](Ranks "Ranks"), [diagonals](Diagonals "Diagonals") or [anti-diagonals](Anti-Diagonals "Anti-Diagonals") along the [files](Files "Files") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>:




```

int collapsedFilesIndex(U64 b) {
   b |= b >> 32;
   b |= b >> 16;
   b |= b >>  8;
   return b & 0xFF;
}

```

In 32-bit mode, assembly programmers may collapse files to register AL in five instructions, saving >> 32 and >> 8:




```

or  eax, edx
mov edx, eax
shr eax, 16
or  eax, edx
or  al, ah

```





### Collapsed Ranks


For a line along [files](Files "Files") (as well as [diagonals](Diagonals "Diagonals") or [anti-diagonals](Anti-Diagonals "Anti-Diagonals")), a little more trickery is needed:




```

int collapsedRanksIndex(U64 b) {
   b |= b >>  4;
   b |= b >>  2;
   b |= b >>  1;
   b &= C64(0x0101010101010101):
   b |= b >>  7;
   b |= b >> 14;
   b |= b >> 28;
   return b & 0xFF;
}

```

If it is exclusively about to collapse files to ranks, one can save the first three parallel prefix shifts, but shift right by file-index:




```

int collapsedRanksIndex(U64 b, enumFile file) {
   b  = b >> file;
   b &= C64(0x0101010101010101):
   b |= b >>  7;
   b |= b >> 14;
   b |= b >> 28;
   return b & 0xFF;
}

```





## Using Multiplication


Recent 64-bit processors, such as [core 2](https://en.wikipedia.org/wiki/Intel_Core_2) or [K8](https://en.wikipedia.org/wiki/Athlon_64) have a amazingly fast 64-bit [multiplication](General_Setwise_Operations#Multiplication "General Setwise Operations"), so that flip- or rotation-tricks as mentioned in [diagonals to rank](Flipping_Mirroring_and_Rotating#DiagonalstoRanks "Flipping Mirroring and Rotating") or [flip about the diagonal](Flipping_Mirroring_and_Rotating#FlipAbouttheDiagonal "Flipping Mirroring and Rotating") are competitive nowadays.



### Collapsed Files



```

int collapsedFilesIndex(U64 b) {
   const U64 aFile   = C64(0x0101010101010101);
   return (b * aFile) >> 56;
}

```

or in 32-bit mode:




```

int collapsedFilesIndex(U64 b) {
   unsigned int folded = (unsigned int)b | (unsigned int)(b >> 32);
   return (folded * 0x01010101) >> 24;
}

```

### Collapsed Ranks



```

int collapsedRanksIndex(U64 b) {
   const U64 aFile   = C64(0x0101010101010101);
   const U64 antiDia = C64(0x0102040810204080);

   b |= b >> 4;   // No masking needed
   b |= b >> 2;   //    "         "
   b |= b >> 1;   //    "         "
   return ((b & aFile) * antiDia) >> 56;
}

```

or dedicated for files




```

int collapsedRanksIndex(U64 b, enumFile file) {
   const U64 aFile   = C64(0x0101010101010101);
   const U64 antiDia = C64(0x0102040810204080);

   b  = b >> file;
   return ((b & aFile) * antiDia) >> 56;
}

```

Those techniques are actually used in [Kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards"), considering the [inner six bits](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") for a denser lookup.



## See also


* [Flipping, Mirroring and Rotating of Rank, File and Diagonal](Flipping_Mirroring_and_Rotating#RankFileAndDiagonal "Flipping Mirroring and Rotating")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")
* [Sliding Piece Attacks](Cinnamon#Sliding_Piece_Attacks "Cinnamon") in [Cinnamon](Cinnamon "Cinnamon")
* [Sliding Piece Attacks](OliThink#SlidingPieceAttacks "OliThink") in [OliThink](OliThink "OliThink")


## Forum Posts


* [Re: Rotated bitboards](https://groups.google.com/d/msg/rec.games.chess.computer/YvFagyuVogw/2vNJw_qT8IYJ) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997
* [Re: Some thoughts on Dann Corbit's rotated alternative](https://www.stmintz.com/ccc/index.php?id=491079) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 03, 2006
* [Kindergarten bitboards without multiplying](http://www.talkchess.com/forum/viewtopic.php?t=29296) by [Piotr Cichy](Piotr_Cichy "Piotr Cichy"), [CCC](CCC "CCC"), August 07, 2009 » [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")


## External Links


* [Bit Gather Via Multiplication](http://drpetric.blogspot.com/2013/09/bit-gathering-via-multiplication.html) by [Vlad Petric](index.php?title=Vlad_Petric&action=edit&redlink=1 "Vlad Petric (page does not exist)"), [Dr. Petric's Technical Blog](http://drpetric.blogspot.com/), September 17, 2013 <a id="cite-note-4" href="#cite-ref-4">[4]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Besetzt!](https://de-de.facebook.com/umspannwerk.recklinghausen/posts/10153757793891429) (Occupied) - [Toilet](https://en.wikipedia.org/wiki/Toilet) exhibition at [Umspannwerk Recklinghausen](https://de.wikipedia.org/wiki/Umspannwerk_Recklinghausen), today [RWE](https://en.wikipedia.org/wiki/RWE) [Technology museum](https://en.wikipedia.org/wiki/Technology_museum) in [Recklinghausen](https://en.wikipedia.org/wiki/Recklinghausen), Germany, and part of [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail") of the [Ruhr area](https://en.wikipedia.org/wiki/Ruhr) - Row of occupied [portable toilets](https://en.wikipedia.org/wiki/Toilet#Others), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), September 16, 2016
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Rotated bitboards](https://groups.google.com/d/msg/rec.games.chess.computer/YvFagyuVogw/2vNJw_qT8IYJ) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 31, 1997
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Some thoughts on Dann Corbit's rotated alternative](https://www.stmintz.com/ccc/index.php?id=491079) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), March 03, 2006
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Demystifying the Magic Multiplier?](https://web.archive.org/web/20180820032914/https://chessprogramming.wikispaces.com/share/view/64439740) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), August 20, 2018)

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
