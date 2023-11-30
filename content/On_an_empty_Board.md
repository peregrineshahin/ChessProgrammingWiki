---
title: On an empty Board
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* On an empty Board**


**Single sliding piece attacks** on the **otherwise empty board** or their disjoint subsets on lines or [rays](Rays "Rays") are that simple than none sliding pieces. We simply use pre-calculated tables for each [piece-type](Pieces "Pieces"), line or ray, indexed by square-index. To initialize those tables, one may use a [fill approach](Kogge-Stone_Algorithm#Fillonanemptyboard "Kogge-Stone Algorithm") with single populated from-sets, if availably anyway since used elsewhere. While the proposed line-routines here are quite small and cheap, incremental update during an initialization loop has some merits.


The various ray-,line- and piece sets are foundation of further attack calculation considering blocking pieces, for instance to mask the [occupancy](Occupancy "Occupancy") of relevant rays. Of course the piece attacks are union-sets of the disjoint line attacks, while the line attacks are unions of the disjoint ray attacks.






### Rays by Line


Ray-Attacks may be conducted from Line-Attacks by intersection with "positive" and "negative" squares:




```C++

 positiveRay[sq] = lineAttacks[sq] & (0 - 2*singleBit[sq]);
 negativeRay[sq] = lineAttacks[sq] & (singleBit[sq] - 1);

```

or with shifts instead of lookups




```C++

 positiveRay[sq] = lineAttacks[sq] & (C64(-2) << sq);
 negativeRay[sq] = lineAttacks[sq] & ((C64(1) << sq) - 1);

```





### Positive Rays


*Remember [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations").*



### By Lookup



```C++

East (+1)           Nort (+8)            NoEa (+9)           NoWe (+7)
. . . . . . . .     . . . 1 . . . .      . . . . . . . 1     . . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . . 1 .     1 . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . 1 . .     . 1 . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . 1 . . .     . . 1 . . . . .
. . . R 1 1 1 1     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .

```

### Initialization


North attacks are simple to initialize inside a loop, starting from a1, shifting left:




```C++

U64 nort = C64(0x0101010101010100);
for (int sq=0; sq < 64; sq++, nort <<= 1)
   rayAttacks[sq][Nort] = nort;


```

Similar, but tad trickier for [ranks](Ranks "Ranks") and [diagonals](Diagonals "Diagonals"), due to the wraps. For instance the north-east [direction](Direction "Direction"):




```C++

U64 noea = C64(0x8040201008040200);
for (int f=0; f < 8; f++, noea = eastOne(noea) {
   U64 ne = noea;
   for (int r8 = 0; r8 < 8*8; r8 += 8, ne <<= 8)
      rayAttacks[r8+f][NoEa] = ne;
}

```

### By Calculation


Orthogonal positive rays are quite cheap to calculate on the fly. For diagonal rays split the lines as [mentioned](On_an_empty_Board#SplitRaysFromLine "On an empty Board").




```C++

U64 eastMaskEx(int sq) {
   const U64 one = 1;
   return 2*( (one << (sq|7)) - (one << sq) );
}

U64 nortMaskEx(int sq) {
   return C64(0x0101010101010100) << sq;
}

```





### Negative Rays


Remember [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations").



### By Lookup



```C++

West (-1)           Sout (-8)            SoWe (-9)           SoEa (-7)
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .      . . . . . . . .     . . . . . . . .
1 1 1 R . . . .     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . 1 . . . .      . . 1 . . . . .     . . . . 1 . . .
. . . . . . . .     . . . 1 . . . .      . 1 . . . . . .     . . . . . 1 . .
. . . . . . . .     . . . 1 . . . .      1 . . . . . . .     . . . . . . 1 .

```

### Initialization


South attacks are simple to initialize inside a loop, starting from h8, shifting right:




```C++

U64 sout = C64(0x0080808080808080);
for (int sq=63; sq >= 0; sq--, sout >>= 1)
   rayAttacks[sq][Sout] = sout;

```

Similar, but tad trickier for [ranks](Ranks "Ranks") and [diagonals](Diagonals "Diagonals"), due to the wraps.



### By Calculation


Orthogonal negative rays are quite cheap to calculate on the fly. For diagonal rays split the lines as [mentioned](On_an_empty_Board#SplitRaysFromLine "On an empty Board").




```C++

U64 westMaskEx(int sq) {
   const U64 one = 1;
   return (one << sq) - (one << (sq&56));
}

U64 soutMaskEx(int sq) {
   return C64(0x0080808080808080) >> (sq ^ 63);
}

```





## Line Attacks



```C++

 RankAttacks[sq]         = EastAttacks[sq] | WestAttacks[sq];
 FileAttacks[sq]         = NortAttacks[sq] | SoutAttacks[sq];
 DiagonalAttacks[sq]     = NoEaAttacks[sq] | SoWeAttacks[sq];
 AntiDiagonalAttacks[sq] = NoWeAttacks[sq] | SoEaAttacks[sq];

```

### By Lookup



```C++

Rank                File                 Diagonal            Anti-Diagonal
. . . . . . . .     . . . 1 . . . .      . . . . . . . 1     . . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . . 1 .     1 . . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . . 1 . .     . 1 . . . . . .
. . . . . . . .     . . . 1 . . . .      . . . . 1 . . .     . . 1 . . . . .
1 1 1 R 1 1 1 1     . . . R . . . .      . . . B . . . .     . . . B . . . .
. . . . . . . .     . . . 1 . . . .      . . 1 . . . . .     . . . . 1 . . .
. . . . . . . .     . . . 1 . . . .      . 1 . . . . . .     . . . . . 1 . .
. . . . . . . .     . . . 1 . . . .      1 . . . . . . .     . . . . . . 1 .

```

### By Calculation


To calculate line masks for [ranks](Ranks "Ranks"), [files](Files "Files"), [diagonals](Diagonals "Diagonals") and [antidiagonals](Anti-Diagonals "Anti-Diagonals") on the fly:




```C++

U64 rankMask(int sq) {return  C64(0xff) << (sq & 56);}

U64 fileMask(int sq) {return C64(0x0101010101010101) << (sq & 7);}

U64 diagonalMask(int sq) {
   const U64 maindia = C64(0x8040201008040201);
   int diag =8*(sq & 7) - (sq & 56);
   int nort = -diag & ( diag >> 31);
   int sout =  diag & (-diag >> 31);
   return (maindia >> sout) << nort;
}

U64 antiDiagMask(int sq) {
   const U64 maindia = C64(0x0102040810204080);
   int diag =56- 8*(sq&7) - (sq&56);
   int nort = -diag & ( diag >> 31);
   int sout =  diag & (-diag >> 31);
   return (maindia >> sout) << nort;
}

```

The [generalized shift](General_Setwise_Operations#GeneralizedShift "General Setwise Operations") version for [diagonals](Diagonals "Diagonals") and [antidiagonals](Anti-Diagonals "Anti-Diagonals") as introduced by [Thomas Jahn](Thomas_Jahn "Thomas Jahn") <a id="cite-note-1" href="#cite-ref-1">[1]</a> produces shorter and faster code on modern [x86-64](X86-64 "X86-64") processors due to [BMI2](BMI2 "BMI2") shift instructions not affecting the flags <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++

U64 diagonalMask(int sq) {
   const U64( maindia = C64(0x8040201008040201);
   int diag  = (sq&7) - (sq>>3);
   return diag >= 0 ? maindia >> diag*8 : maindia << -diag*8;
}

U64 antiDiagMask(int sq) {
   const U64( maindia = C64(0x0102040810204080);
   int diag  = 7 - (sq&7) - (sq>>3);
   return diag >= 0 ? maindia >> diag*8 : maindia << -diag*8;
}

```

Excluding the square bit:




```C++

U64 rankMaskEx    (int sq) {return (C64(1) << sq) ^ rankMask(sq);}
U64 fileMaskEx    (int sq) {return (C64(1) << sq) ^ fileMask(sq);}
U64 diagonalMaskEx(int sq) {return (C64(1) << sq) ^ diagonalMask(sq);}
U64 antiDiagMaskEx(int sq) {return (C64(1) << sq) ^ antiDiagMask(sq);}

```





## Piece Attacks



```C++

RookAttacks[sq]   = RankAttacks[sq]     | FileAttacks[sq];
BishopAttacks[sq] = DiagonalAttacks[sq] | AntiDiagonalAttacks[sq];
QueenAttacks[sq]  = RookAttacks[sq] | BishopAttacks[sq];

```

### By Lookup



```C++

                                   Queen
                               . . . 1 . . . 1
                               1 . . 1 . . 1 .
                               . 1 . 1 . 1 . .
               Rook            . . 1 1 1 . . .         Bishop
           . . . 1 . . . .     1 1 1 Q 1 1 1 1     . . . . . . . 1
           . . . 1 . . . .     . . 1 1 1 . . .     1 . . . . . 1 .
           . . . 1 . . . .     . 1 . 1 . 1 . .     . 1 . . . 1 . .
           . . . 1 . . . .     1 . . 1 . . 1 .     . . 1 . 1 . . .
           1 1 1 R 1 1 1 1                         . . . B . . . .
           . . . 1 . . . .                         . . 1 . 1 . . .
           . . . 1 . . . .                         . 1 . . . 1 . .
           . . . 1 . . . .                         1 . . . . . 1 .

```

### By Calculation



```C++

U64 rookMask    (int sq) {return rankMask(sq)     | fileMask(sq);}
U64 bishopMask  (int sq) {return diagonalMask(sq) | antiDiagMask(sq);}


U64 rookMaskEx  (int sq) {return rankMask(sq)     ^ fileMask(sq);}
U64 bishopMaskEx(int sq) {return diagonalMask(sq) ^ antiDiagMask(sq);}

U64 queenMask   (int sq) {return rookMask(sq)     | bishopMask(sq);}
U64 queenMaskEx (int sq) {return rookMask(sq)     ^ bishopMask(sq);}

```

## See also


* [Blockers and Beyond](Blockers_and_Beyond "Blockers and Beyond")
* [Fill on an empty Board](Kogge-Stone_Algorithm#Fillonanemptyboard "Kogge-Stone Algorithm") with [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")


## Forum Posts


* [[Question] Efficiently generate ray masks?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79140) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), January 16, 2022


 [Re: [Question] Efficiently generate ray masks?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79140&start=10) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), January 17, 2022
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Re: [Question] Efficiently generate ray masks?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79140&start=10) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), January 17, 2022
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [SARX/SHLX/SHRX — Shift Without Affecting Flags](https://www.felixcloutier.com/x86/sarx:shlx:shrx)

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
