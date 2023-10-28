---
title: Subtracting a Rook from a Blocking Piece
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* Subtracting a Rook from a Blocking Piece**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb6) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Bishop, Knight, Rook <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
If we think about an [arithmetical operation](General_Setwise_Operations#ArithmeticalOperations "General Setwise Operations") to calculate rank-attacks of a [rook](Rook "Rook") or [queen](Queen "Queen") with bitboards, [subtraction](General_Setwise_Operations#Subtraction "General Setwise Operations") comes in mind. The idea is to treat the arithmetical carry, or inverse, borrow propagation as a way to generate rook attacks in one ray direction. As long there are zeros left (empty squares) between blocker and subtracting rook, the borrow walks through, similar as a [sliding piece](Sliding_Pieces "Sliding Pieces") moves along the empty squares.





|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
 |


### Contents


* [1 How it Works](#how-it-works)
* [2 o^(o-2r)](#o.5e.28o-2r.29)
* [3 See also](#see-also)
* [4 References](#references)






*Again, we write [bytes](Byte "Byte") ([ranks](Ranks "Ranks")) [little-endian-wise](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"), LSB (A-file) is left not right.*




```

    00000010 blocking piece
  - 01000000 rook
    01111100 piece(s) - rook

```

The difference is already like an [occluded-fill](Dumb7Fill "Dumb7Fill"), including the rook (slider) but excluding the blocker. Therefor, also considering no or multiple blockers - or even multiple sliders, the [xor difference](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with the [union](General_Setwise_Operations#Union "General Setwise Operations") of both blocking and sliding sets determines the bit-changes, ...




```

    01000010 occupied = piece(s) | rook
xor 01111100 piece(s) - rook
=   00111110

```

... yielding exactly the attack set of the rook(s) in positive rank direction, from left to right (from whites point of view) or A- to H-file.




## o^(o-2r)


This trick is known as **o^(o-2r)**. Assuming rook **r** is member of the [occupancy](Occupancy "Occupancy") **o**, the single subtract would only clear that **r**-bit, therefor subtracting **2r** is required to borrow from the closest blocker bit in **o**. However, even if **o** may not include the rook bit, the subtraction of **2r** does not affect that bit - no matter whether **r** is set in **o** or not, the [xor operation](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") results in the changed bits as sliding rook attacks. Unfortunately, due to borrow is propagated in direction of arithmetical more significant bits, the trick only works on [positive rays](On_an_empty_Board#PositiveRays "On an empty Board"), but can be applied for [files](Files "Files") or [diagonals](Diagonals "Diagonals") with leading and trailing [intersections](General_Setwise_Operations#Intersection "General Setwise Operations") with the [line-masks](On_an_empty_Board#LineAttacks "On an empty Board"). For instance, north attacks of a rook on d2:




```

occupancy        &  filemask[d]      =  potential blockers
. . 1 1 . . 1 .     . . . 1 . . . .     . . . 1 . . . .
1 . 1 1 . 1 1 1     . . . 1 . . . .     . . . 1 . . . .
. 1 . . . 1 . .     . . . 1 . . . .     . . . . . . . .
. . . . . . . .     . . . 1 . . . .     . . . . . . . .
1 . . . . . . .  &  . . . 1 . . . .  =  . . . . . . . .
. 1 1 . . . 1 .     . . . 1 . . . .     . . . . . . . .
. . . 1 1 1 1 1     . . . 1 . . . .     . . . 1 . . . .
. . . 1 . . 1 .     . . . 1 . . . .     . . . 1 . . . .

pot.blockers     -  2*squarebit[d2]  =  difference
. . . 1 . . . .     . . . . . . . .     . . . 1 . . . .
. . . 1 . . . .     . . . . . . . .     1 1 1 . . . . .
. . . . . . . .     . . . . . . . .     1 1 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .     1 1 1 1 1 1 1 1
. . . . . . . .  -  . . . . . . . .  =  1 1 1 1 1 1 1 1
. . . . . . . .     . . . . . . . .     1 1 1 1 1 1 1 1
. . . 1 . . . .     . . . . 1 . . .     . . . 1 1 1 1 1
. . . 1 . . . .     . . . . . . . .     . . . 1 . . . .

difference       ^  occupancy        =  changed
. . . 1 . . . .     . . 1 1 . . 1 .     . . 1 . . . 1 .
1 1 1 . . . . .     1 . 1 1 . 1 1 1     . 1 . 1 . 1 1 1
1 1 1 1 1 1 1 1     . 1 . . . 1 . .     1 . 1 1 1 . 1 1
1 1 1 1 1 1 1 1     . . . . . . . .     1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1  ^  1 . . . . . . .  =  . 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1     . 1 1 . . . 1 .     1 . . 1 1 1 . 1
. . . 1 1 1 1 1     . . . 1 1 1 1 1     . . . . . . . .
. . . 1 . . . .     . . . 1 . . 1 .     . . . . . . 1 .

changed          &  filemask[d]      =  north attacks[d2]
. . 1 . . . 1 .     . . . 1 . . . .     . . . . . . . .
. 1 . 1 . 1 1 1     . . . 1 . . . .     . . . 1 . . . .
1 . 1 1 1 . 1 1     . . . 1 . . . .     . . . 1 . . . .
1 1 1 1 1 1 1 1     . . . 1 . . . .     . . . 1 . . . .
. 1 1 1 1 1 1 1  &  . . . 1 . . . .  =  . . . 1 . . . .
1 . . 1 1 1 . 1     . . . 1 . . . .     . . . 1 . . . .
. . . . . . . .     . . . 1 . . . .     . . . . . . . .
. . . . . . 1 .     . . . 1 . . . .     . . . . . . . .

```

This operation was derived from the [Reverse Bitboards](Reverse_Bitboards "Reverse Bitboards") idea by [Ryan Mack](Ryan_Mack "Ryan Mack"), and is base of the [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence") to get single piece attacks on diagonals and files. Since the operation principally works set-wise, even with multiple rooks per rank, it can be applied in [SIMD- or SWAR-wise](Fill_by_Subtraction "Fill by Subtraction") manner on all eight ranks (bytes) simultaneously.



## See also


* [Reverse Bitboards](Reverse_Bitboards "Reverse Bitboards")
* [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")
* [Obstruction Difference](Obstruction_Difference "Obstruction Difference")
* [SBAMG](SBAMG "SBAMG")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb6), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
