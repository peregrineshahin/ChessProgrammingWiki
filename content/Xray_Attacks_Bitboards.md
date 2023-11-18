---
title: Xray Attacks Bitboards
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* X-ray Attacks**


The term **X-ray attack** was apparently originated by [Kenneth Harkness](https://en.wikipedia.org/wiki/Kenneth_Harkness). On page 25 of the April 1947 [Chess Review](https://en.wikipedia.org/wiki/Chess_Review), in his series *Picture Guide to Chess*, he mentioned forks and then wrote <a id="cite-note-1" href="#cite-ref-1">[1]</a>:




```C++
There is another type of double attack in which the targets are threatened in one direction. The attacking piece threatens two units, one behind the other, on the same rank, file or diagonal. This double threat has lacked a good descriptive name. We suggest ‘X-Ray’ attack. 

```

## Single Sliders


The single sliding piece, a rook, bishop or queen is specified by square index, likely from a [bitscan](BitScan "BitScan") of a piece-wise [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") of a sliding piece bitboard from a [standard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition").




### Modifying Occupancy


Following routines may be used to get all kind of x-ray attacks or defenses through the blockers for one particular slider. The idea is to intersect the sliding attacks with the desired blockers, which are subset of occupied. In a second run, those blockers are removed from the occupancy, to get the x-ray attacks as the symmetric difference of both attacks.




```C++

U64 xrayRookAttacks(U64 occ, U64 blockers, enumSquare rookSq) {
   U64 attacks = rookAttacks(occ, rookSq);
   blockers &= attacks;
   return attacks ^ rookAttacks(occ ^ blockers, rookSq);
}

U64 xrayBishopAttacks(U64 occ, U64 blockers, enumSquare bishopSq) {
   U64 attacks = bishopAttacks(occ, bishopSq);
   blockers &= attacks;
   return attacks ^ bishopAttacks(occ ^ blockers, bishopSq);
}

```

Alternatively one may use a condition to save the second lookup - one may use disjoint line-attacks rather than piece-attacks. If so, it makes sense to exclude the outer squares from the blockers.




```C++

U64 xrayFileAttacks(U64 occ, U64 blockers, enumSquare rookSq) {
   U64 attacks = fileAttacks(occ, rookSq);
   blockers &= attacks & C64(0x00FFFFFFFFFFFF00);
   if ( blockers == 0 ) return blockers;
   return attacks ^ fileAttacks(occ ^ blockers, rookSq);
}

U64 xrayRankAttacks(U64 occ, U64 blockers, enumSquare rookSq) {
   U64 attacks = rankAttacks(occ, rookSq);
   blockers &= attacks & C64(0x7E7E7E7E7E7E7E7E);
   if ( blockers == 0 ) return blockers;
   return attacks ^ rankAttacks(occ ^ blockers, rookSq);
}

U64 xrayDiagonalAttacks(U64 occ, U64 blockers, enumSquare bishopSq) {
   U64 attacks = diagonalAttacks(occ, bishopSq);
   blockers &= attacks & C64(0x007E7E7E7E7E7E00);
   if ( blockers == 0 ) return blockers;
   return attacks ^ diagonalAttacks(occ ^ blockers, bishopSq);
}

```





### X-rays with one Lookup


Another idea is to consider all kind of blockers in one run, and to traverse intersections of the x-rays attacks with different target sets, to determine the blocking piece inside a loop. In the context of absolute pins, [Oliver Brausch](Oliver_Brausch "Oliver Brausch") introduced to lookup x-ray attacks through any blocker in his engine [OliThink](OliThink "OliThink") <a id="cite-note-2" href="#cite-ref-2">[2]</a> - similar to any occupied lookup technique to get [sliding piece attacks](Sliding_Piece_Attacks#AttacksbyOccupancyLookup "Sliding Piece Attacks"). Instead of the pre-calculated line-attacks we can also pre-calculate attacks behind the first blocker, including a possible second blocker. [The outer squares](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") are redundant as well. Some sample on a rank:




```C++

rook      00001000
occupied  01011010
attacks   00010110
x-ray     01100001

```

Since absolute pins and discovered checkers are usually quite rare, it might be worth to spend some additional memory, e.g. 8 KByte for [kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards") - x-rays. Also the [switch approach](The_Switch_Approach "The Switch Approach") is great to consider all kind of x-ray stuff on a line.



## Multiple Sliders


If keeping eight disjoint ray-direction attacks from fill-routines like [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") one may intersect them with desired blockers - and to perform another fill with that intersection:




```C++

U64 xrayAttacks(U64 sliders, U64 empty, U64 blockers, int dir8) {
   U64 attacks = slidingAttacks (sliders, empty, dir8);
   blockers &= attacks; // & notOuterSquares[dir8];
   if ( blockers )
      return slidingAttacks (blockers, empty, dir8);
   return 0;
}

```

### Blockers by Targets


The other idea is to fill the potential target set, and to intersect it with the opposite ray-direction fill of the sliders and the relevant blockers:




```C++

U64 betweenSliderAndTarget(U64 sliders, U64 empty, U64 targets, int dir8) {
   U64 attacks    = slidingAttacks (sliders, empty, dir8);
   U64 fromtarget = slidingAttacks (targets, empty, opposite(dir8));
   return attacks & fromtarget;
}

```

## See also


* [Sliding Piece Attacks](OliThink#SlidingPieceAttacks "OliThink") in [OliThink](OliThink "OliThink")


## Forum Posts


* [Generating "through" attacks with rotated bitboard](http://www.talkchess.com/forum/viewtopic.php?t=29577) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), August 28, 2009 » [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")


## External Links


* [X-ray (chess) from Wikipedia](https://en.wikipedia.org/wiki/X-ray_(chess))
* [Defunkt](Category:Defunkt "Category:Defunkt") - See Through, [Jazzopen Stuttgart](https://de.wikipedia.org/wiki/Jazzopen_Stuttgart) 1996, [3sat](https://en.wikipedia.org/wiki/3sat) broadcast, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Joseph Bowie](Category:Joseph_Bowie "Category:Joseph Bowie"), [Kelvyn Bell](http://www.allmusic.com/artist/kelvyn-bell-mn0001577170/credits), [Larry Bowen](http://www.dfmusicinc.com/news/item.asp?ID=15), [Bahnamous Bowie](http://www.discogs.com/artist/299640-Bahnamous-Bowie), [Byron Bowie](http://www.discogs.com/artist/363770-Byron-Bowie), [Kim Clarke](Category:Kim_Clarke "Category:Kim Clarke"), [Scooter Warner](http://www.allmusic.com/artist/scooter-warner-mn0000645895/credits), [Ronny Drayton](https://en.wikipedia.org/wiki/Ronny_Drayton)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Jack O’Keefe](Jack_O%E2%80%99Keefe "Jack O’Keefe") in [Chess Note 4245. X-ray attack](http://www.chesshistory.com/winter/winter20.html#4245._X-ray_attack_C.N._4231) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Question about SEE (Static exchange evaluation)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=166649&t=18750) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), December 18, 2007

**[Up one Level](Bitboards "Bitboards")**







 
