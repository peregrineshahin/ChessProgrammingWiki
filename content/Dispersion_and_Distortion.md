---
title: Dispersion and Distortion
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties") * Dispersion and Distortion**

[](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb7) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Luna <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Dispersion** and **Distortion**,

are [Kmoch's](Hans_Kmoch "Hans Kmoch") terms <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> for [pawn structure](Pawn_Structure "Pawn Structure") [weaknesses](Weak_Pawns "Weak Pawns") due to vertical or horizontal splitting caused by [captures](Captures "Captures") or [advancement](Pawn_Push "Pawn Push"). The proposed functions may be used via an additional scaling or indirection, f.i. to index a table with concrete penalties.

## Contents

- [1 Dispersion](#dispersion)
- [2 Distortion](#distortion)
- [3 See also](#see-also)
- [4 External Links](#external-links)
- [5 References](#references)

## Dispersion

**Dispersion** is [Kmoch's](Hans_Kmoch "Hans Kmoch") term for vertical splitting of pawns (most commonly, isolation) caused by captures. Having three or four [islands](</Pawn_Islands_(Bitboards)> "Pawn Islands (Bitboards)") while the opponent has one or two - assuming about the same number of pawns for both sides - may be considered in evaluation. But this is also implicitly done by evaluating [double- or triple](</Double_and_Triple_(Bitboards)> "Double and Triple (Bitboards)") and [isolated](</Isolated_Pawns_(Bitboards)#IsolanisSetWise> "Isolated Pawns (Bitboards)") or the balance of weak pawns in general. Some arbitrary dispersion measure, intended as index of a pre-calculated table for [evaluation](Evaluation "Evaluation") purpose.

```

int dispersion(U64 pawns)
{
   BYTE fileset  = (BYTE) soutFill(pawns);
   int  ni = popCount(islandsEastFiles(fileset));
   int  np = popCount(wpawns);
   return abs(3*ni*ni - np);
}

BYTE islandsEastFiles(BYTE f) {return f & ((f ^ (f >> 1));}

```

The higher the worse.

```

  \  number if islands
   \     1   2   3   4
np  \    3  12  27  48
_____\________________
 1   |   2   -   -   -
 2   |   1  10   -   -
 3   |   0   9  24   -
 4   |   1   8  23  44
 5   |   2   7  22  43
 6   |   3   6  21  42
 7   |   4   5  20  41
 8   |   5   4  19  40

```

## Distortion

Distortion is [Kmoch's](Hans_Kmoch "Hans Kmoch") term for horizontal splitting of pawns caused by advances. One may use something like this based on [rearfill](Pawn_Fills "Pawn Fills"), xor and [population count](Population_Count "Population Count") to get an idea of distortion. It considers the rank-difference of two file-adjacent pawns (if any) as distortion penalty - the higher the worse. [Half-isolated](</Isolated_Pawns_(Bitboards)#IsolanisSetWise> "Isolated Pawns (Bitboards)") or even [isolated pawns](Isolated_Pawn "Isolated Pawn") contribute a distortion penalty according to the size of their rearfill from 2 to 7 for each empty neighboring file, which discourages advancement of such pawns, interacting with terms considerring (half-) isolated pawns. Alternatively, for a "reverse" distortion penalty to encourage advancement of half-isolanis, one may use [frontfill](Pawn_Fills "Pawn Fills") instead with a slightly different semantic is case of [doubled pawns](Doubled_Pawn "Doubled Pawn").

```

int wDistortion(U64 wpawns) {
   U64 fill  = wRearFill(wpawns); // wFrontFill
   U64 delta = (fill ^ (fill<<1)) & C64(0xfefefefefefefefe));
   return popCount(delta);
}

```

High distortion sample:

```

wpawns              rearFill            rearFill << 1      xor & ~A-File
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . . . . . . .     . . . . . . . .     . . . . . . . .     . . . . . . . .
. . 1 . 1 . 1 .     . . 1 . 1 . 1 .     . . . 1 . 1 . 1     . . 1 1 1 1 1 1
. . . . . . . .     . . 1 . 1 . 1 .     . . . 1 . 1 . 1     . . 1 1 1 1 1 1
1 . . . . . . .     1 . 1 . 1 . 1 .     . 1 . 1 . 1 . 1     . 1 1 1 1 1 1 1
. . . . . . . .     1 . 1 . 1 . 1 .     1 1 . 1 . 1 . 1     . 1 1 1 1 1 1 1
. 1 . 1 . 1 . 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     . . . . . . . .
. . . . . . . .     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1     . . . . . . . .

                                                            26 bits sets

```

## See also

- [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
- [Isolated Pawns (Bitboards)](</Isolated_Pawns_(Bitboards)> "Isolated Pawns (Bitboards)")
- [Pawn Islands](Pawn_Islands "Pawn Islands")
- [Pawn Islands (Bitboards)](</Pawn_Islands_(Bitboards)> "Pawn Islands (Bitboards)")

## External Links

- [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")
- [Monsoon/Typhoon Homepage](https://wannabe.guru.org/scott/hobbies/chess/) by [Scott Gasch](Scott_Gasch "Scott Gasch")
- [Dispersion from Wikipedia](https://en.wikipedia.org/wiki/Dispersion)
- [Distortion (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Distortion_%28disambiguation%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bb7), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Hans Kmoch](Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")

**[Up one Level](Pawn_Pattern_and_Properties "Pawn Pattern and Properties")**

