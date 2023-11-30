---
title: Rotated Bitboards
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* Rotated Bitboards**



[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Mural from the Temple of Longing ↖Thither↗ <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Rotated Bitboards**,  

a bitboard [move generation](Move_Generation "Move Generation") technique coined by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and later by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch") from the [DarkThought](DarkThought "DarkThought") team. This variation uses [rotated](Flipping_Mirroring_and_Rotating#Rotation "Flipping Mirroring and Rotating") copies of the [occupancy](Occupancy "Occupancy") in order to place bits along a [file](Files "Files"), [diagonal](Diagonals "Diagonals") or [anti-diagonal](Anti-Diagonals "Anti-Diagonals") in adjacent bits. Because of this, these bits can be easily extracted to obtain a dense [occupancy map](Occupancy_of_any_Line "Occupancy of any Line") for a [rank](Ranks "Ranks"), file, diagonal, and anti-diagonal. These are used, along with the square of the sliding piece, to lookup a bitboard, containing attacks, in an [array](Array "Array"). 


While the attack generation per line is more or less only one [memory](Memory "Memory") lookup, the [incremental](Incremental_Updates "Incremental Updates") [update](General_Setwise_Operations#UpdateByMove "General Setwise Operations") of the [occupancy](Occupancy "Occupancy") during [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move") becomes more expensive, since beside the usual [occupied bitboard](Bitboard_Board-Definition#Occupancy "Bitboard Board-Definition") there are three more rotated bitboards to update, including additional mapping from square coordinates to the rotated indices. 



## Square Mapping


Interesting is the different mapping of both approaches. Crafty seemed to use [little endian square mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations") but bit 0 (A1) is mentioned as MSB, while bit 63 (H8) is LSB. DarkThought uses big-endian file-mapping (H1 = 0).



### by Hyatt


Crafty didn't use byte aligned [diagonals](Diagonals "Diagonals"), but visual rotation.




```C++

  normal chess board bitmap            occupied_squares 90 degrees

  A8 B8 C8 D8 E8 F8 G8 H8              H8 H7 H6 H5 H4 H3 H2 H1
  A7 B7 C7 D7 E7 F7 G7 H7              G8 G7 G6 G5 G4 G3 G2 G1
  A6 B6 C6 D6 E6 F6 G6 H6              F8 F7 F6 F5 F4 F3 F2 F1
  A5 B5 C5 D5 E5 F5 G5 H5              E8 E7 E6 E5 E4 E3 E2 E1
  A4 B4 C4 D4 E4 F4 G4 H4              D8 D7 D6 D5 D4 D3 D2 D1
  A3 B3 C3 D3 E3 F3 G3 H3              C8 C7 C6 C5 C4 C3 C2 C1
  A2 B2 C2 D2 E2 F2 G2 H2              B8 B7 B6 B5 B4 B3 B2 B1
  A1 B1 C1 D1 E1 F1 G1 H1              A8 A7 A6 A5 A4 A3 A2 A1

  original left 45                     original right 45

              H8                                 A8
            G8  H7                             A7  B8
          F8  G7  H6                         A6  B7  C8
        E8  F7  G6  H5                     A5  B6  C7  D8
      D8  E7  F6  G5  H4                 A4  B5  C6  D7  E8
    C8  D7  E6  F5  G4  H3             A3  B4  C5  D6  E7  F8
  B8  C7  D6  E5  F4  G3  H2         A2  B3  C4  D5  E6  F7  G8
A8  B7  C6  D5  E4  F3  G2  H1     A1  B2  C3  D4  E5  F6  G7  H8
  A7  B6  C5  D4  E3  F2  G1         B1  C2  D3  E4  F5  G6  H7
    A6  B5  C4  D3  E2  F1             C1  D2  E3  F4  G5  H6
      A5  B4  C3  D2  E1                 D1  E2  F3  G4  H5
        A4  B3  C2  D1                     E1  F2  G3  H4
          A3  B2  C1                         F1  G2  H3
            A2  B1                             G1  H2
              A1                                 H1

  original left 45                     original right 45

   G6 H5|F8 G7 H6|G8 H7|H8|            C7 D8|A6 B7 C8|A7 B8|A8|
   H3|D8 E7 F6 G5 H4|E8 F7             F8|A4 B5 C6 D7 E8|A5 B6
   F4 G3 H2|C8 D7 E6 F5 G4             E6 F7 G8|A3 B4 C5 D6 E7
   E4 F3 G2 H1|B8 C7 D6 E5             E5 F6 G7 H8|A2 B3 C4 D5
   D4 E3 F2 G1|A8 B7 C6 D5             E4 F5 G6 H7|A1 B2 C3 D4
   B5 C4 D3 E2 F1|A7 B6 C5             D2 E3 F4 G5 H6|B1 C2 D3
   C2 D1|A5 B4 C3 D2 E1|A6             G3 H4|D1 E2 F3 G4 H5|C1
  |A1|A2 B1|A3 B2 C1|A4 B3            |H1|G1 H2|F1 G2 H3|E1 F2

```

### by Gillgasch and Heinz


[DarkThought](DarkThought "DarkThought") used a similar mapping as proposed in [Pseudo Rotation by 45 degrees](Flipping_Mirroring_and_Rotating#PseudoRotationby45degrees "Flipping Mirroring and Rotating") from [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating"), all diagonals are packed in file-aligned bytes.




```C++

Normal Bitboard.                       Flipped Bitboard.
##7 #6 #5 #4 #3 #2 #1 #0 Bit/Byte       #7 #6 #5 #4 #3 #2 #1 #0 Bit/Byte
a8 b8 c8 d8 e8 f8 g8 h8 #7             a8 a7 a6 a5 a4 a3 a2 a1 #7
a7 b7 c7 d7 e7 f7 g7 h7 #6             b8 b7 b6 b5 b4 b3 b2 b1 #6
a6 b6 c6 d6 e6 f6 g6 h6 #5             c8 c7 c6 c5 c4 c3 c2 c1 #5
a5 b5 c5 d5 e5 f5 g5 h5 #4             d8 d7 d6 d5 d4 d3 d2 d1 #4
a4 b4 c4 d4 e4 f4 g4 h4 #3             e8 e7 e6 e5 e4 e3 e2 e1 #3
a3 b3 c3 d3 e3 f3 g3 h3 #2             f8 f7 f6 f5 f4 f3 f2 f1 #2
a2 b2 c2 d2 e2 f2 g2 h2 #1             g8 g7 g6 g5 g4 g3 g2 g1 #1
a1 b1 c1 d1 e1 f1 g1 h1 #0             h8 h7 h6 h5 h4 h3 h2 h1 #0


A1-H8 Bitboard.                        A8-H1 Bitboard.
##7 #6 #5 #4 #3 #2 #1 #0 Bit/Byte       #7 #6 #5 #4 #3 #2 #1 #0 Bit/Byte
a8|b1 c2 d3 e4 f5 g6 h7 #7             a8 b7 c6 d5 e4 f3 g2 h1 #7
a7 b8|c1 d2 e3 f4 g5 h6 #6             a7 b6 c5 d4 e3 f2 g1|h8 #6
a6 b7 c8|d1 e2 f3 g4 h5 #5             a6 b5 c4 d3 e2 f1|g8 h7 #5
a5 b6 c7 d8|e1 f2 g3 h4 #4             a5 b4 c3 d2 e1|f8 g7 h6 #4
a4 b5 c6 d7 e8|f1 g2 h3 #3             a4 b3 c2 d1|e8 f7 g6 h5 #3
a3 b4 c5 d6 e7 f8|g1 h2 #2             a3 b2 c1|d8 e7 f6 g5 h4 #2
a2 b3 c4 d5 e6 f7 g8|h1 #1             a2 b1|c8 d7 e6 f5 g4 h3 #1
a1 b2 c3 d4 e5 f6 g7 h8|#0             a1|b8 c7 d6 e5 f4 g3 h2 #0

```

### Quotes


From [Robert Hyatt](Robert_Hyatt "Robert Hyatt") as repost to [Urban Koistinen](Urban_Koistinen "Urban Koistinen") from 1997 <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++
When I first thought about doing the rotated bitmap idea, I discussed it with Peter G. of the DarkThought team. He thought (as I did) that the idea was pretty neat and worth trying. I (from the first thought) had always planned on updating the rotated bitmaps by the following approach: I have a set of 64 bitmaps callet set_mask[n]. To set bit 32, I simply AND(bit-map,set_mask[32]). If I have a rotated-90 bitmap, then I also create a rotated-90 set_mask, and do this: AND(bit-map-R90,set_mask_R90[32]) and I am done. Peter didn't like this, and wanted to get rid of the extra memory load for the rotated set_mask variable. (note there are actually 4 of these loads needed, for each of the rotated bitmaps). So he thought about it a bit and found a cute mathematical transformation based on shifts, AND's and OR's (I won't give it here since it is his idea) that avoide needing the set_mask_Rxx masks (note that on some machines, even the set_mask itself is not needed. to set bit 32 you just start with "1" and shift it to the right position avoiding the memory load altogether. However, the effect of Peter's approach is to map diagonal bits on the real bitmap to adjacent bits in a "psuedo-rotated" bitmap, without needing the set_mask_R90 stuff at all. Is it better? I'm not sure. My tests on the P6 said NO. My tests on the alpha with big cache also said NO. Peter's tests on the machine he used said YES. It definitely takes more instructions to do what Peter is doing. On a machine with a huge memory latency, like the [PC](IBM_PC "IBM PC"), my memory loading can be slow. But with a decent sized cache, the 64 words X 8 bytes per word (512 bytes) really tucks into a corner in cache and doesn't hurt at all, particularly since a cache hit on the P6 operates at CPU speed. The PII is a different case since the cache operates at 1/2 CPU speed, which might swing things in his favor. For the record, they are *close* under all cases. We are not talking 10% here...one might be 2% faster on one machine, the other 3% faster on another machine... But the "mapping" is really odd and would not let us just simply swap the L45 and R45 maps... 

```

## Table size


The initial implementations of rotated bitboards missed the [outer square optimization](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") and used the 8-bit occupied state with four lookup tables of 256\*64\*8 or 128-Kbyte each, thus 1/2 MByte in total. [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel") seemed first time mentioned the optimization trick 1998 <a id="cite-note-5" href="#cite-ref-5">[5]</a>, masking off the redundant outer occupancies for a four fold table reduction.


Of course one may use calculations similar to [kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") to further shrink the tables. In fact, getting the occupancy state and pre-calculated information based on that are two different steps.



## See also


* [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
* [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
* [Rotated Indices](Rotated_Indices "Rotated Indices")


## Publications


* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html).* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2005**). *[The Representation of Chess Game](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1491153)*. Proceedings of the 27th International Conference on Information Technology Interfaces
* [Johannes Buchner](index.php?title=Johannes_Buchner&action=edit&redlink=1 "Johannes Buchner (page does not exist)") (**2005**). *Rotated bitboards in FUSc#*. [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/jbuchner/rotated.pdf) » [FUSc#](FUSCsharp "FUSCsharp")


## Forum Posts


### 1995 ...


* [bitmaps of rotated boards](https://groups.google.com/d/msg/gnu.chess/lSsvkY3St7s/wZ-3sG9rNmcJ) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 2, 1995
* [Re: Speed of Move Generator](http://groups.google.com/group/rec.games.chess.computer/msg/d3e64cbd920b1153) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 17, 1995
* [Rotated bitboards - experiment and result](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b6d3210fc02baa93) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 28, 1996
* [bitboard move generation question](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a97c78bd49c9c9e6) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 05, 1997
* [Bitboard Representation](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/00013e6c504ace86) by Carl Tillotson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 18, 1997
* [Rotated bitboards](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/62f15a832b95a20c) by Mats Forsén, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 29, 1997
* [Rotated bitboards](https://www.stmintz.com/ccc/index.php?id=17377) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), April 22, 1998
* [Efficient Rotated Bitboard Representations](https://www.stmintz.com/ccc/index.php?id=30863) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 28, 1998
* [Extracting information from rotated Bitboards](https://www.stmintz.com/ccc/index.php?id=31429) by John Stoneham, [CCC](CCC "CCC"), November 02, 1998
* [Bitboard user's information request](https://www.stmintz.com/ccc/index.php?id=71880) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 05, 1999


### 2000 ...


* [Nice Rotated-bitmaps Article by Hyatt in ICCA](https://www.stmintz.com/ccc/index.php?id=95468) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), February 07, 2000 <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Rotated Bitboards?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8cd63a61ab02a1ed) by Mauricio Castro, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 07, 2001
* [Attack Bitboards](https://www.stmintz.com/ccc/index.php?id=194920) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), October 30, 2001
* [Resources about rotated bitboards](https://www.stmintz.com/ccc/index.php?id=342372) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), January 02, 2004


### 2005 ...


* [Generating "through" attacks with rotated bitboard](http://www.talkchess.com/forum/viewtopic.php?t=29577) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), August 28, 2009 » [X-ray Attacks (Bitboards)](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")


### 2010 ...


* [A question on rotated bitboard](http://www.open-chess.org/viewtopic.php?f=5&t=1376) by n\_ven, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 04, 2011


## External Links


* [Rotated Bitboards](http://people.csail.mit.edu/heinz/dt/node8.html) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz")
* [Rotated bitmaps, a new twist on an old idea](http://www.craftychess.com/hyatt/bitmaps.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), revisited version of the [ICCA Journal](ICGA_Journal "ICGA Journal") paper <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [Computer Chess Programming Theory - Bitboards](http://www.frayn.net/beowulf/theory.html#bitboards) by [Colin Frayn](Colin_Frayn "Colin Frayn")
* [Herb Alpert](https://en.wikipedia.org/wiki/Herb_Alpert) - [Rotation](https://en.wikipedia.org/wiki/Rise_%28Herb_Alpert_album%29) (1979), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Mural from the Temple of Longing ↖Thither↗, [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Speed of Move Generator](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/33c57503391f3a89) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 15, 1995, post 5 by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") where he mentions on the fly generation with rotated bitboards
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Rotated Bitboards](http://people.csail.mit.edu/heinz/dt/node8.html) in [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess.](http://people.csail.mit.edu/heinz/dt/node2.html)* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Bitboard Representation](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/00013e6c504ace86) by Carl Tillotson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 18, 1997, post 23 by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Extracting information from rotated Bitboards](https://www.stmintz.com/ccc/index.php?id=31456) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), November 02, 1998
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Bitboard user's information request](https://www.stmintz.com/ccc/index.php?id=71880) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 05, 1999
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Nice Rotated-bitmaps Article by Hyatt in ICCA](https://www.stmintz.com/ccc/index.php?id=95468) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), February 07, 2000
8. <a id="cite-ref-8" href="#cite-note-8">↑</a>  [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *[Rotated Bitmaps, a New Twist on an Old Idea](http://www.craftychess.com/hyatt/bitmaps.html)*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> The [ICCA Journal](ICGA_Journal "ICGA Journal") paper does not mention the [outer square optimization](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") with the four fold table reduction

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
