---
title: CHEOPS
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * CHEOPS**

\[ Pyramid of Cheops <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CHEOPS**,

a **Che**ss-**O**riented **P**rocessing **S**ystem with a dedicated chess processor, developed end of the 70s at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") by [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway") and [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), derived from the original conception and design of a 8x8 hardware chess array instrumented by [Edward Fredkin](Edward_Fredkin "Edward Fredkin"). CHEOPS was used by [Baisley's](Alan_Baisley "Alan Baisley") [Tech 2](Tech#Tech2 "Tech") and a [brute force](Brute-Force "Brute-Force") version of [Greenblatt's](Richard_Greenblatt "Richard Greenblatt") [Mac Hack](Mac_Hack "Mac Hack") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, but unfortunately have never competed in computer chess tournaments with this approach. According to [Joe Condon](Joe_Condon "Joe Condon") and [Ken Thompson](Ken_Thompson "Ken Thompson"), already working on a chess hardware for [Belle](Belle "Belle"), the problem with CHEOPS was the lack of positional [evaluation](Evaluation "Evaluation") support <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Block Diagrams](#block-diagrams)
- [2 CHARM](#charm)
  - [2.1 The Chess arrays](#the-chess-arrays)
  - [2.2 The Array module](#the-array-module)
- [3 Micro-Controller](#micro-controller)
- [4 Publications](#publications)
- [5 See also](#see-also)
- [6 Namesakes](#namesakes)
- [7 External Links](#external-links)
- [8 References](#references)

## Block Diagrams

[](File:Cheops.png "CHEOPS block diagram")
[](File:Charm1.png "CHARM block diagram")

## CHARM

CHEOPS had all components of a general purpose processor, in addition to a 16-bit [ALU](Combinatorial_Logic#ALU "Combinatorial Logic"), it had a powerful **Ch**ess **Ar**ray **M**odule (CHARM), which contains a [board representation](Board_Representation "Board Representation") and most of the chess specific logic for attack and [move generation](Move_Generation "Move Generation") including transformation of a [piece-list](Piece-Lists "Piece-Lists") to a hardwired [bitboard](Bitboards "Bitboards") and from bitboards to a list of [squares](Squares "Squares") or [moves](Move_List "Move List"). Like the ALU, CHARM's input is connected via the ABUS with a 1024-word [push down list](Stack "Stack") (PDL). For example CHARM can accept a record from the PDL of the last move tried from a given [position](Chess_Position "Chess Position"), and generate the next possible move in a specified order. In general, the 8x8 CHARM chess array module is to find a specified subset of [legal board moves](Legal_Move "Legal Move").

## The Chess arrays

Each of the 64 squares retains information about the color and type of piece (if any) occupying it. Beside [memory](Memory "Memory") to keep the board and pieces, the chess array contains the [combinatorial logic](Combinatorial_Logic "Combinatorial Logic") for each square, controlled by various signal lines. It may generate [attacks](Square_Attacked_By "Square Attacked By") and sets of legal moves to one designated [destination square](Target_Square "Target Square"), where the output consists of 64 lines which specify which of the 64 squares contain pieces of the moving color which can capture or move to that destination.

Alternatively, a square can be designated as the originating-area, in which case the 64 lines assert possible destinations for moves from this square, a hardwired move target bitboard. Special control bits can cause the array functions to be more specific or general. It can discriminate [captures](Captures "Captures") from [non-capturing moves](Quiet_Moves "Quiet Moves"), or pawn from noble capture, or cause the entire board to be designated as originating or destination area, so that general questions as "any capture possible?" can be answered in a single operation.

## The Array module

The array module consists of a [sequential logic](Sequential_Logic "Sequential Logic") to implement the inner loops of typical move generation routines in scanning squares and pieces, in particular it implements the [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") to convert the 64 square output lines from the chess arrays to an internal list of squares. The [BitScan](BitScan "BitScan") hardware has the 64 square lines and a "last square number" register as input, to generate the number of the next active square line.

## Micro-Controller

The sequence of ALU and CHARM operations in CHEOPS is determined by a 1K by 64 bit [RAM](Memory#RAM "Memory") control memory. Each micro-instruction consists of four [16-bit words](Word "Word"). A cycle time of the machine is about 180 nanoseconds. The remainder of the CHEOPS system consists of a [PDP-11](PDP-11 "PDP-11") and a time shared [PDP-10](PDP-10 "PDP-10") which communicate with the special processor through a special bus interface.

## Publications

- [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") (**1979**). *[CHEOPS: A Chess-orientated Processing System](http://portal.acm.org/citation.cfm?id=61701.67028)*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/%7Eshm/MI/mi9.html), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

## See also

- [Belle](Belle "Belle")
- [Berkeley Chess Microprocessor](Berkeley_Chess_Microprocessor "Berkeley Chess Microprocessor")
- [CXG Sphinx](CXG_Sphinx "CXG Sphinx")
- [Mac Hack](Mac_Hack "Mac Hack")
- [Sfinks](Sfinks "Sfinks")
- [Tech 2](Tech#Tech2 "Tech")

## Namesakes

- [Cheops](</Cheops_(Miller)> "Cheops (Miller)") (CHEss OPponent Simulator) by [Tristan Miller](index.php?title=Tristan_Miller&action=edit&redlink=1 "Tristan Miller (page does not exist)") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## External Links

- PDP-10 software for controlling CHEOPS: [CHPROG; CCHEOP 484](https://github.com/PDP-10/its/blob/master/src/chprog/ccheop.484) hosted by [Lars Brinkhoff](User:Larsbrinkhoff "User:Larsbrinkhoff")
- CHEOPS microcode source: [AGB; CHUCOD 83](https://github.com/PDP-10/its-vault/blob/master/files/agb/chucod.83) hosted by [Lars Brinkhoff](User:Larsbrinkhoff "User:Larsbrinkhoff")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Great Pyramid of Giza](https://en.wikipedia.org/wiki/Great_Pyramid_of_Giza), Photo by [Nina Aldin Thune](http://no.wikipedia.org/wiki/Bruker:Nina), March 2005, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [John Moussouris](John_Moussouris "John Moussouris"), [Jack Holloway](Jack_Holloway "Jack Holloway"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") (**1979**). *[CHEOPS: A Chess-orientated Processing System](http://portal.acm.org/citation.cfm?id=61701.67028)*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Joe Condon](Joe_Condon "Joe Condon"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1982**). *Belle Chess Hardware*. [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [CHEOPS - nothingisreal.com](http://en.nothingisreal.com/wiki/CHEOPS)

**[Up one Level](Hardware "Hardware")**

