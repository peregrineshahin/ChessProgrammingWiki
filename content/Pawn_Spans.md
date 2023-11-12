---
title: Pawn Spans
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties") \* Pawn Spans**


**Pawn Spans** and Fill-Pattern of [pawns](Pawn "Pawn") are used as a base for many other [pawn structure](Pawn_Structure "Pawn Structure") related stuff, to determine [passers](Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)"), [candidates](Candidates_(Bitboards) "Candidates (Bitboards)"), [isolanis](Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)") etc. set-wise. 



### Front- and Rearspans


Front- and rearspans are the [front- and rearfills](Pawn_Fills "Pawn Fills") shifted one step further in the fill-direction:




```C++

white frontspans    black rearspans
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 . 1 1 . . . 1
1 1 1 . . 1 1 1     . . . 1 . . . .
1 1 1 . . 1 1 1     . . . . . . . .
. 1 1 . . . 1 1  ^  . . . . . . . .
. 1 1 . . . 1 1  |  . . . . . . . .
. . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .
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
white rearspans     black frontspans
. . . . . . . .  |  . . . . . . . .
. . . . . . . .  v  . . . . . . . .
. . . . . . . .     . 1 . . . 1 1 .
. . . . . . . .     1 1 1 . . 1 1 1
. . . . . . . .     1 1 1 1 . 1 1 1
1 . . . . 1 . .     1 1 1 1 . 1 1 1
1 . 1 . . 1 . .     1 1 1 1 . 1 1 1
1 1 1 . . 1 1 1     1 1 1 1 . 1 1 1

```


```C++

U64 wFrontSpans(U64 wpawns) {return nortOne (nortFill(wpawns));}
U64 bRearSpans (U64 bpawns) {return nortOne (nortFill(bpawns));}
U64 bFrontSpans(U64 bpawns) {return soutOne (soutFill(bpawns));}
U64 wRearSpans (U64 wpawns) {return soutOne (soutFill(wpawns));}

```

* Pawns still member of their frontspan have at least one pawn behind on the same file.
* Pawns still member of their rearspan have at least one pawn in front on the same file.
* All pawns which are member of the opponent frontspans (or frontfill) have a **mechanical obstruction** and are **unfree**.


### Interspans


The intersection of white and black frontspans is called interspan. Obviously interspans can only occur on closed files. [Rooks](Rook "Rook") on interspans may have a hard time, if the attacked opponent pawns are safe. Their vertical mobility is restricted and they may vulnerable to get trapped and attacked. On the other hand, if supported by other attacking pieces, there might be successful attacks against [weak pawns](Weak_Pawns "Weak Pawns") and the especially the [king](King "King").




```C++

white frontspan  &  black frontspan  =  interspan
1 1 1 . . 1 1 1     . . . . . . . .     . . . . . . . .
1 1 1 . . 1 1 1     . . . . . . . .     . . . . . . . .
1 1 1 . . 1 1 1     . 1 . . . 1 1 .     . 1 . . . 1 1 .
1 1 1 . . 1 1 1     1 1 1 . . 1 1 1     1 1 1 . . 1 1 1
. 1 1 . . . 1 1  &  1 1 1 1 . 1 1 1  =  . 1 1 . . . 1 1
. 1 1 . . . 1 1     1 1 1 1 . 1 1 1     . 1 1 . . . 1 1
. . . . . . . .     1 1 1 1 . 1 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 . 1 1 1     . . . . . . . .

```





## Stop and Telestop


[Stop squares](Stop_Square "Stop Square") are the [push move targets](Pawn_Pushes_(Bitboards) "Pawn Pushes (Bitboards)") of any pawn.




```C++

U64 wStop(U64 wpawns) {return nortOne (wpawns);}
U64 bStop(U64 bpawns) {return soutOne (bpawns);}

```

Thus, the frontfills of the stop squares are the frontspans of the pawns:




```C++

U64 wFrontSpan(U64 wpawns) {return nortFill(wStop(wpawns));}
U64 bFrontSpan(U64 bpawns) {return soutFill(bStop(bpawns));}

```

Telestop squares all the squares of the frontspan, except the stop squares




```C++

U64 wTeleStops(U64 wpawns) {return wFrontSpans(wStop(wpawns)) ^ wStop(wpawns);}
U64 bTeleStops(U64 bpawns) {return bFrontSpans(bStop(bpawns)) ^ bStop(bpawns);}

```

## See also


* [Attack Spans](Attack_Spans "Attack Spans")
* [Fill Algorithms](Fill_Algorithms "Fill Algorithms")
* [Pawn Fills](Pawn_Fills "Pawn Fills")


## External Links


* [Steps Ahead](Category:Steps_Ahead "Category:Steps Ahead") - Live in Japan 1986, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Mike Mainieri](Category:Mike_Mainieri "Category:Mike Mainieri"), [Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker"), [Darryl Jones](Category:Darryl_Jones "Category:Darryl Jones"), [Mike Stern](Category:Mike_Stern "Category:Mike Stern"), [Steve Smith](Category:Steve_Smith "Category:Steve Smith")
 
**[Up one Level](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**







 
