---
title: Knight PatternKnightForks
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Knight Pattern**



 [](http://www.mcescher.com/Shopmain/ShopEU/facsilimeprints/prints.html) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Horseman <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Knight Pattern**
with Bitboards covers [knight](Knight "Knight") [attacks](Attacks "Attacks") of single or multiple knights, either by indexed pre-calculated tables or direct bitboard calculation, and the set wise determination of [Knight fork](https://en.wikipedia.org/wiki/Fork_%28chess%29) target squares. 






### Contents


* [1 Knight Attacks](#knight-attacks)
	+ [1.1 by Lookup](#by-lookup)
	+ [1.2 by Calculation](#by-calculation)
* [2 Multiple Knight Attacks](#multiple-knight-attacks)
* [3 Knight Fill](#knight-fill)
* [4 Knight Forks](#knight-forks)
* [5 See also](#see-also)
* [6 Selected Publications](#selected-publications)
* [7 Forum Posts](#forum-posts)
* [8 External Links](#external-links)
* [9 References](#references)






The [Knight](Knight "Knight") attacks the [target squares](Target_Square "Target Square") independently from other pieces around. The compass rose of all eight attacking [directions](Direction "Direction") associated with the to - from square differences from an [8x8 board](8x8_Board "8x8 Board"):




```C++

        noNoWe    noNoEa
            +15  +17
             |     |
noWeWe  +6 __|     |__+10  noEaEa
              \   /
               >0<
           __ /   \ __
soWeWe -10   |     |   -6  soEaEa
             |     |
            -17  -15
        soSoWe    soSoEa

```





### by Lookup


The knight is specified by square index, likely from a [bitscan](BitScan "BitScan") of a piece-wise [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") of a knight bitboard from a [standard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition"), to index a table of pre-calculated knight-attacks:




```C++

U64 arrKnightAttacks[64];

U64 knightAttacks(enumSquare sq) {return arrKnightAttacks[sq];}

```

For instance a knight on d4




```C++

arrKnightAttacks[d4]
 . . . . . . . .
 . . . . . . . .
 . . 1 . 1 . . .
 . 1 . . . 1 . .
 . . . . . . . .
 . 1 . . . 1 . .
 . . 1 . 1 . . .
 . . . . . . . .

```





### by Calculation


Similar to [one step only](General_Setwise_Operations#OneStepOnly "General Setwise Operations") of the four orthogonal and four diagonal directions,each of the eight knight directions is calculated by left or right shift with appropriate pre- or post shift mask, to avoid A- H-file wraps or vice versa. See also [AVX2 Knight Attacks](AVX2#KnightAttacks "AVX2").




```C++

U64 noNoEa(U64 b) {return (b << 17) & notAFile ;}
U64 noEaEa(U64 b) {return (b << 10) & notABFile;}
U64 soEaEa(U64 b) {return (b >>  6) & notABFile;}
U64 soSoEa(U64 b) {return (b >> 15) & notAFile ;}
U64 noNoWe(U64 b) {return (b << 15) & notHFile ;}
U64 noWeWe(U64 b) {return (b <<  6) & notGHFile;}
U64 soWeWe(U64 b) {return (b >> 10) & notGHFile;}
U64 soSoWe(U64 b) {return (b >> 17) & notHFile ;}

U64 noNoEa(U64 b) {return (b & notHFile ) << 17;}
U64 noEaEa(U64 b) {return (b & notGHFile) << 10;}
U64 soEaEa(U64 b) {return (b & notGHFile) >>  6;}
U64 soSoEa(U64 b) {return (b & notHFile ) >> 15;}
U64 noNoWe(U64 b) {return (b & notAFile ) << 15;}
U64 noWeWe(U64 b) {return (b & notABFile) <<  6;}
U64 soWeWe(U64 b) {return (b & notABFile) >> 10;}
U64 soSoWe(U64 b) {return (b & notAFile ) >> 17;}

```

In almost the same manner as the three pawn directions, there is a unique source-target relationship. The difference is - we have up to eight pawns, but likely not more than two knights per side. Keeping eight disjoint knight directions is consistent to direction-wise [fill approaches](Fill_Algorithms "Fill Algorithms") of other pieces with unique [target](Target_Square "Target Square")-[source](Origin_Square "Origin Square") relationship - but disjoint direction-wise knight targets are sparse populated and usually contain only up to two bits.




## Multiple Knight Attacks


To initialize the KnightAttacks [array](Array "Array") one may use a routine with some kind of [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") calculations, rather than the union of all eight directions:




```C++

U64 knightAttacks(U64 knights) {
   U64 west, east, attacks;
   east     = eastOne (knights);
   west     = westOne (knights);
   attacks  = (east|west) << 16;
   attacks |= (east|west) >> 16;
   east     = eastOne (east);
   west     = westOne (west);
   attacks |= (east|west) <<  8;
   attacks |= (east|west) >>  8;
   return attacks;
}

```

or to possibly gain some more parallelism:




```C++

U64 knightAttacks(U64 knights) {
   U64 l1 = (knights >> 1) & C64(0x7f7f7f7f7f7f7f7f);
   U64 l2 = (knights >> 2) & C64(0x3f3f3f3f3f3f3f3f);
   U64 r1 = (knights << 1) & C64(0xfefefefefefefefe);
   U64 r2 = (knights << 2) & C64(0xfcfcfcfcfcfcfcfc);
   U64 h1 = l1 | r1;
   U64 h2 = l2 | r2;
   return (h1<<16) | (h1>>16) | (h2<<8) | (h2>>8);
}

```

If we pass multiple knights set-wise, attacks of some squares may be caused by different knights. Feeding back (safe) target sets, the routine may used to get sets of squares, knights may reach in two or more moves. For instance in late pawn-knight endings whether a knight may catch a passer.




## Knight Fill


A fill cycle for a [fill algorithm](Fill_Algorithms "Fill Algorithms") is the [union](General_Setwise_Operations#Union "General Setwise Operations") of the attack set with the knights itself:




```C++

U64 knightFill(U64 knights) {return knightAttacks(knights) | knights;}

```

for instance applied six times on the otherwise empty board:




```C++

                  1. Fill            2. Fill            3. Fill
. . . . . . . .   . . . . . . . .   . . . . . . . .   . . . . . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .   . 1 . 1 . . . .
. . . . . . . .   . . . . . . . .   . . . . . . . .   1 . 1 . 1 . . .
. . . . . . . .   . . . . . . . .   1 . 1 . . . . .   1 1 1 1 . 1 . .
. . . . . . . .   . . . . . . . .   . 1 . 1 . . . .   1 1 1 1 1 . 1 .
. . . . . . . .   . 1 . . . . . .   1 1 . . 1 . . .   1 1 . 1 1 1 . .
. . . . . . . .   . . 1 . . . . .   . . 1 1 . . . .   1 . 1 1 1 . 1 .
1 . . . . . . .   1 . . . . . . .   1 . 1 . 1 . . .   1 1 1 1 1 1 . .

                  4. Fill            5. Fill            6. Fill
                  . 1 . 1 . 1 . .   1 1 1 1 1 1 1 .   1 1 1 1 1 1 1 1
                  1 1 1 1 1 . 1 .   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 . 1   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 1 .   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 1 .   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1
                  1 1 1 1 1 1 1 .   1 1 1 1 1 1 1 1   1 1 1 1 1 1 1 1

```





## Knight Forks


A common knight pattern is the knight fork. Targets are heavy pieces - king, queen and rooks, [hanging pieces](Hanging_Piece "Hanging Piece"), or even undefended pawns. A royal knight fork or "family" check, winning the queen is most important. Otherwise one may loop over all possible pieces, to get the knight-attacks by lookup and to intersect all combinations of attack-squares. A loop- and branch-less solution to get potential fork-attack squares is to union all intersections of all direction attacks, as explained in [greater one sets](General_Setwise_Operations#GreaterOne "General Setwise Operations"):




```C++

U64 forkTargetSquare(U64 targets) {
   U64 west, east, attak, forks;
   east   = eastOne (targets);
   west   = westOne (targets);
   attak  =  east << 16;
   forks  = (west << 16) & attak;
   attak |=  west << 16;
   forks |= (east >> 16) & attak;
   attak |=  east >> 16;
   forks |= (west >> 16) & attak;
   attak |=  west >> 16;
   east   = eastOne (east);
   west   = westOne (west);
   forks |= (east <<  8) & attak;
   attak |=  east <<  8;
   forks |= (west <<  8) & attak;
   attak |=  west <<  8;
   forks |= (east >>  8) & attak;
   attak |=  east >>  8;
   forks |= (west >>  8) & attak;
   return forks;
}

```

The intersection of those targets with squares not occupied by own pieces or attacked by opponent pawns and knights, but attacked by own knight(s) leaves a move target set with some forced properties.



## See also


* [AVX2 Knight Attacks](AVX2#KnightAttacks "AVX2")
* [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
* [Knight-Distance](Knight-Distance "Knight-Distance")


## Selected Publications


* [Martin Gardner](Martin_Gardner "Martin Gardner") (**1967**). *Problems that are Built on the Knight's Tour in Chess*. [Scientific American](Scientific_American "Scientific American"), Vol. 130
* [Noam D. Elkies](Noam_Elkies "Noam Elkies"), [Richard P. Stanley](Mathematician#RPStanley "Mathematician") (**2003**). *The Mathematical Knight*. [The Mathematical Intelligencer](https://en.wikipedia.org/wiki/The_Mathematical_Intelligencer), Vol. 25, No. 1, [pdf](http://www.math.harvard.edu/%7Eelkies/knight.pdf)
* Ben Hill (**2004**). *Knight’s Tours*. [pdf](http://faculty.olin.edu/~sadams/DM/ktpaper.pdf)
* [Philip Hingston](https://scholar.google.com/citations?user=QNcGZdQAAAAJ&hl=en), [Graham Kendall](Graham_Kendall "Graham Kendall") (**2005**). *[Ant Colonies Discover Knight's Tours](https://link.springer.com/chapter/10.1007/978-3-540-30549-1_125)*. [AI 2004](https://link.springer.com/book/10.1007/b104336), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 3339
* [Philip Hingston](https://scholar.google.com/citations?user=QNcGZdQAAAAJ&hl=en), [Graham Kendall](Graham_Kendall "Graham Kendall") (**2005**). *Enumerating Knight’s Tours using an Ant Colony Algorithm*. [CEC 2005](https://dblp.uni-trier.de/db/conf/cec/cec2005.html), [pdf](http://www.cs.nott.ac.uk/~pszgxk/papers/cec05knights.pdf)


## Forum Posts


* [Symbolic: From bitboards to ideas](https://www.stmintz.com/ccc/index.php?id=354355) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 13, 2004 » [Symbolic](Symbolic "Symbolic")
* [Problem with bitboard knight attack generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=41542) by [ZirconiumX](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), December 21, 2011
* [Knight fork threats](https://groups.google.com/d/msg/fishcooking/_qtvakyb_yM/FYOlNteY0N0J) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 17, 2014 » [Knight Forks](Knight_Pattern#KnightForks "Knight Pattern"), [Stockfish](Stockfish "Stockfish")
* [knight's multiple atacks](http://www.talkchess.com/forum/viewtopic.php?t=55118) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), January 27, 2015


## External Links


* [Knight's tour from Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour)
* [Knight's Tour Notes compiled by George Jelliss](http://www.mayhematics.com/t/t.htm)
* [Knight's Tour - from Wolfram MathWorld](http://mathworld.wolfram.com/KnightsTour.html)
* [Longest uncrossed knight's path from Wikipedia](https://en.wikipedia.org/wiki/Longest_uncrossed_knight%27s_path)
* [László Lindner's](L%C3%A1szl%C3%B3_Lindner "László Lindner") [knight wheel](http://archive.is/bHju8) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel") from [ChessBase Puzzle](ChessBase "ChessBase")
* [Knight's Tour](http://graham-kendall.com/blog/2014/01/knights-tours/) from [Research Reflections](http://graham-kendall.com/blog/) by [Graham Kendall](Graham_Kendall "Graham Kendall"), January 18, 2014
* Knight's Tour - [Numberphile](http://www.numberphile.com/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [View facsimile print](http://www.mcescher.com/Shopmain/ShopEU/facsilimeprints/prints.html) from [M.C. Escher - 16 Facsimile Prints](http://www.mcescher.com/Shopmain/ShopEU/facsilimeprints/)

**[Up one Level](Bitboards "Bitboards")**







 
