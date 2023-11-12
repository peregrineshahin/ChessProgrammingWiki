---
title: Pawn Fills
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Fills**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bba) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Unexpected <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Pawn Fills** are base of [spans](Pawn_Spans "Pawn Spans"). They are used to determine **closed**, [half-open](Half-open_File "Half-open File") and [open](Open_File "Open File") files.




### Contents


* [1 Front- and Rearfill](#front--and-rearfill)
* [2 Filefill](#filefill)
* [3 See also](#see-also)
* [4 External Links](#external-links)
* [5 References](#references)






Frontfills and rearfills are the base of [front- and rearspans](Pawn_Spans#FrontAndRearspans "Pawn Spans"), which require one additional north/south shift. Of course whites front [direction](Direction "Direction") is north, while blacks front direction is south - vice versa for the rear side.




```C++

white frontfill     black rearfill
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 . 1 1 . . . 1
1 1 1 . . 1 1 1     . . . 1 . . . .
1 1 1 . . 1 1 1  ^  . . . . . . . .
. 1 1 . . . 1 1  |   . . . . . . . .
. 1 1 . . . 1 1  |   . . . . . . . .
. . . . . . . .  |   . . . . . . . .
               north
white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 . 1 . . . . 1
. . . . . . . .     . . . 1 . . . .
1 . . . . 1 . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .
. 1 1 . . . 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .
               south
white rearfill      black frontfill
. . . . . . . .  |  . . . . . . . .
. . . . . . . .  |  . 1 . . . 1 1 .
. . . . . . . .  |  1 1 1 . . 1 1 1
. . . . . . . .  v  1 1 1 1 . 1 1 1
1 . . . . 1 . .     1 1 1 1 . 1 1 1
1 . 1 . . 1 . .     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1

```

[Parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")-routines are used to fill either north or south:




```C++

U64 nortFill(U64 gen) {
   gen |= (gen <<  8);
   gen |= (gen << 16);
   gen |= (gen << 32);
   return gen;
}

U64 soutFill(U64 gen) {
   gen |= (gen >>  8);
   gen |= (gen >> 16);
   gen |= (gen >> 32);
   return gen;
}

```

Note that the pawns are still subset of their fill sets. The intersection of both north and south fills leaves the initial pawn set again. All pawns which are member of the opponent front fills have a **mechanical obstruction** and are **unfree**.




```C++

U64 wFrontFill(U64 wpawns) {return nortFill(wpawns);}
U64 wRearFill (U64 wpawns) {return soutFill(wpawns);}

U64 bFrontFill(U64 bpawns) {return soutFill(bpawns);}
U64 bRearFill (U64 bpawns) {return nortFill(bpawns);}

```

  





## Filefill


The union of both front- and rearfills, leaves the complete file with at least one either white or black pawn on it. Since filefills have all ranks equal, they may treated as bytes, if it is about pure file sets.




```C++

U64 fileFill(U64 gen) {
   return nortFill(gen) | soutFill(gen);
}

```


```C++

white pawns         black pawns
. . . . . . . .     . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 . 1 . . . . 1
. . . . . . . .     . . . 1 . . . .
1 . . . . 1 . .     . . . . . . . .
. . 1 . . . . .     . . . . . . . .
. 1 1 . . . 1 1     . . . . . . . .
. . . . . . . .     . . . . . . . .
white filefill      black filefill
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1

```

Based on pawns, files are either **closed**, [open](Open_File "Open File") or [halfopen](Half-open_File "Half-open File").



## See also


* [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
* [Half-open File](Half-open_File "Half-open File")
* [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
* [Open File](Open_File "Open File")
* [Parallel Prefix Algorithms](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")
* [Pawn Spans](Pawn_Spans "Pawn Spans")
* [Pawns and Files (Bitboards)](Pawns_and_Files_(Bitboards) "Pawns and Files (Bitboards)")


## External Links


* [Billy Cobham](Category:Billy_Cobham "Category:Billy Cobham") - [George Duke](Category:George_Duke "Category:George Duke") Band - Juicy, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [John Scofield](Category:John_Scofield "Category:John Scofield") and [Alphonso Johnson](Category:Alphonso_Johnson "Category:Alphonso Johnson"), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), July 6, 1976
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc4), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")

**[Up one Level](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**







 
