---
title: Hyperbola Quintessence
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") * Hyperbola Quintessence**

[](File:SamuelBakReflexion.jpg) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Reflexion, 1990 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Hyperbola Quintessence** applies the [o^(o-2r)-trick](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece") also for vertical or diagonal [negative Rays](On_an_empty_Board#NegativeRays "On an empty Board") - by reversing the bit-order of up to one bit per rank or [byte](Byte "Byte") with a [vertical flip](Flipping_Mirroring_and_Rotating#FlipVertically "Flipping Mirroring and Rotating") aka [x86-64](X86-64 "X86-64") [bswap](X86-64#gpinstructions "X86-64") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . It is somehow a resurrection of the [reverse bitboards](Reverse_Bitboards "Reverse Bitboards") idea of [Ryan Mack's](Ryan_Mack "Ryan Mack") *Hyperbola Project* on the fly, and was created by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"). Improvements by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov") <a id="cite-note-3" href="#cite-ref-3">[3]</a> made it applicable and competitive.

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
|

## Reverse Math

Assume following masked [occupancy](Occupancy "Occupancy") on a [file](Files "Files"), [diagonal](Diagonals "Diagonals") or [anti-diagonal](Anti-Diagonals "Anti-Diagonals") - for simplicity as a flat byte (in a real bitboard with masked files or diagonals you have 6..8 scratch-bits between the bits of this byte). Thus, vertical flip reverses the bits of this byte.

```C++

o' = reverse(o)
r' = reverse(r)

       normal    reversed
 o     11010101  10101011 o' occupancy including slider
 r     00010000  00001000 r' slider
 o-r   11000101  10100011 o'-r'  1. sub clears the slider
 o-2r  10110101  10011011 o'-2r' 2. sub borrows "one" from next blocker
       |......|  \....../
normal 10110101   \..../
       11011001 <--XXXX   re-reverse
single
xor    01101100 -> to get the attack set

```

The first subtraction of (o-2r) is done implicitly by masking off the line, removing the slider from the occupied set. The second subtraction borrows a "one" from the next nearest blocker in msb-direction, falling through all unset bits outside the line. Of course, if no blocker is available, it borrows a "one" in usual arithmetical manner from the hidden 2^N. Only the changed bits (from original o, o') are the appropriate sliding attacks, including the blocker but excluding the slider. The result finally needs to be intersected with the same line mask as previously the occupancy, to clear the wrapped borrow one bits outside the file or diagonal. The fine optimization by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov") covers the final [union](General_Setwise_Operations#Union "General Setwise Operations") of [positive](On_an_empty_Board#PositiveRays "On an empty Board") and [negative ray-attacks](On_an_empty_Board#NegativeRays "On an empty Board"). Since opposed [ray-directions](Rays#RayDirections "Rays") are always disjoint sets, using [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") instead of *bitwise or* safes two instructions per line-attack. That is because bit-reversal or any [mirroring or flipping](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") is own inverse and distributive over xor.

```C++

reverse(a ^ b) == reverse (a) ^ reverse(b)

```

thus

```C++

lineAttacks = o^(o-2r) ^ reverse((o'-2r')^o')
lineAttacks = o^(o-2r) ^ reverse( o'-2r') ^ reverse(o')
lineAttacks = o^(o-2r) ^ reverse( o'-2r') ^ o

```

and finally

```C++

lineAttacks =   (o-2r) ^ reverse( o'-2r')

```

Beside shorter code this reduces register pressure - and clearly outperforms [kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") - [ipc](https://en.wikipedia.org/wiki/Instructions_Per_Cycle)-wise, in code size and memory requirements.

## Source Code

## C

The three [C](C "C")-routines only differ by the line-mask applied:

```C++

U64 diagonalAttacks(U64 occ, enumSquare sq) {
   U64 forward, reverse;
   forward = occ & smsk[sq].diagonalMaskEx;
   reverse  = _byteswap_uint64(forward);
   forward -= smsk[sq].bitMask;
   reverse -= _byteswap_uint64(smsk[sq].bitMask);
   forward ^= _byteswap_uint64(reverse);
   forward &= smsk[sq].diagonalMaskEx;
   return forward;
}

U64 antiDiagAttacks(U64 occ, enumSquare sq) {
   U64 forward, reverse;
   forward  = occ & smsk[sq].antidiagMaskEx;
   reverse  = _byteswap_uint64(forward);
   forward -= smsk[sq].bitMask;
   reverse -= _byteswap_uint64(smsk[sq].bitMask);
   forward ^= _byteswap_uint64(reverse);
   forward &= smsk[sq].antidiagMaskEx;
   return forward;
}

U64 fileAttacks(U64 occ, enumSquare sq) {
   U64 forward, reverse;
   forward  = occ & smsk[sq].fileMaskEx;
   reverse  = _byteswap_uint64(forward);
   forward -= smsk[sq].bitMask;
   reverse -= _byteswap_uint64(smsk[sq].bitMask);
   forward ^= _byteswap_uint64(reverse);
   forward &= smsk[sq].fileMaskEx;
   return forward;
}

U64 bishopAttacks(U64 occ, enumSquare sq) {
   return diagonalAttacks (occ, sq)
        + antiDiagAttacks (occ, sq);
}

```

For better locality of the [line-attacks](On_an_empty_Board "On an empty Board") on the otherwise empty board, we may use an properly aligned array of structs.

```C++

struct
{
   U64 bitMask;         // 1 << sq for convenience
   U64 diagonalMaskEx;
   U64 antidiagMaskEx;
   U64 fileMaskEx;
} smsk[64]; // 2 KByte

```

Using [x86-64](X86-64 "X86-64") [bswap](X86-64#gpinstructions "X86-64") makes it quite competitive for bishops and files, on [AMD](AMD "AMD") [K8](https://en.wikipedia.org/wiki/Athlon_64) or [K10](https://en.wikipedia.org/wiki/AMD_K10) it has a latency of one cycle with a throughput of 1/3, like other cheap instructions. However, [Intel](Intel "Intel") is tad slower - while the recent [Core 2 duo](https://en.wikipedia.org/wiki/Intel_Core_2) processors perform 128-bit SIMD-instructions with 128-bit alus, that is bitwise logical instructions with a latency of one cycle and throughput of 1/3, the general purpose bswap-instruction takes four cycles with a throughput of one. In *Intel 64 and IA32 Architectures Optimization Reference Manual* <a id="cite-note-4" href="#cite-ref-4">[4]</a> , it is therefor recommend (5.6.5. endian conversion) to use the [SSSE3](SSSE3 "SSSE3") [pshufb](SSSE3#Pshufb "SSSE3") instruction to swap bytes, available through intrinsic <a id="cite-note-5" href="#cite-ref-5">[5]</a> , see [SSSE3 Hyperbola Quintessence](SSSE3#SSSE3Version "SSSE3") for bishop attacks.

As long there is no fast bit reversal instruction, there is no general solution for all four lines, and the rook attack-getter still needs some standard technique for the [rank-attacks](First_Rank_Attacks#AttacksOnAllRanks "First Rank Attacks"). Tim Cooijmans proposed to map the rank to the main diagonal before applying HQ, and to re-map the calculated attacks back to the original rank <a id="cite-note-6" href="#cite-ref-6">[6]</a> .

## Generalized Set-wise Attacks

Hyperbola quintessence can be generalized to work on whole sets of sliding pieces instead on individual pieces, whose ranks to be masked. The problem arising, when not masking the rank of the piece is that attacks wrap around the board during subtraction. This is shown below:

```C++

     ........       ........                            11111111
     ........       ........                            11111111
     ........       ........                            11111111
 r = ........ , o = ........ this leads to   o - 2*r =  11111111
     ........       ........                            11111111
     ........       ........                            11111111
     ....1...       ....1...                            11111...
     ........       ........                            ........

instead of

........
........
........
........
........
........
11111...
........

```

This is not the intended result. It can be avioded, by bitwise adding an overflow barrier on the right-hand side. Afterwards this barrier needs to be removed from the attack set:

```C++

u64 right = 0x0101010101010101ULL;

     ......1.      1..1..1.                              1...1111
     ....1...      1...1...                              .1111..1
     ......1.      11....1.                              1.111111
r =  .....1..  o = .11..1..   now: ((o | right) - 2*r) = .1.111.1
     ........      ........                              ........
     ......1.      ......1.                              1111111.
     .......1      .......1                              1111111.
     1.......      1.......                              1......1

Note, that the 4th rank was not flooded by the subtraction! Next, the blockers are removed as usual:

                          ...111.1
                          1111...1
                          .11111.1
o ^ ((o | right) - 2*r) = ..111..1
                          ........
                          111111..
                          11111111
                          .......1

The last step is to remove the barrier at the right side that became visible after the last operation.

                                     ...111..
                                     1111...
                                     .11111..
(o ^ ((o | right) - 2*r) & ~right =  ..111...
                                     ........
                                     111111..
                                     1111111.
                                     ........

This is the correct attack set for the left direction.


```

the complete algorithm for the left direction is therefore:

```C++

const u64 right = 0x0101010101010101ULL;

u64 leftAttacks = ((o ^ ((o | right) - 2*r) & ~right);

```

For the right-hand direction, the bits need to be reversed rank-wise.

## x86-64 assembly

The VC2005 generated [x86-64](X86-64 "X86-64") [assembly](Assembly "Assembly") of bishopAttacks indicates what [ipc](https://en.wikipedia.org/wiki/Instructions_Per_Cycle)-monster Hyperbola Quintessence is:

```C++

occ$ = 16
sq$ = 24
?bishopAttacks@@YA_K_KI@Z PROC
  00000   40 53                push    rbx
  00002   8b c2                mov    eax, edx
  00004   4c 8d 15 00 00 00 00 lea    r10, OFFSET FLAT:?smsk
  0000b   48 c1 e0 05          shl    rax, 5
  0000f   4a 8b 5c 10 08       mov    rbx, QWORD PTR [rax+r10+8]  ; diagonalMaskEx
  00014   4e 8b 4c 10 10       mov    r9,  QWORD PTR [rax+r10+16] ; antidiagMaskEx
  00019   4e 8b 14 10          mov    r10, QWORD PTR [rax+r10]    ; r := 1 << sq
  0001d   4c 8b db             mov    r11, rbx                    ; diagonalMaskEx
  00020   49 8b d1             mov    rdx, r9                     ; antidiagMaskEx
  00023   4d 8b c2             mov    r8, r10                     ; r := 1 << sq
  00026   48 23 d1             and    rdx, rcx                    ; anti & occ
  00029   4c 23 d9             and    r11, rcx                    ; dia  & occ
  0002c   49 0f c8             bswap  r8                          ; r'
  0002f   48 8b c2             mov    rax, rdx                    ; ant
  00032   49 8b cb             mov    rcx, r11                    ; dia
  00035   49 2b d2             sub    rdx, r10                    ; ant - r
  00038   48 0f c8             bswap  rax                         ; ant'
  0003b   48 0f c9             bswap  rcx                         ; dia'
  0003e   4d 2b da             sub    r11, r10                    ; dia - r
  00041   49 2b c0             sub    rax, r8                     ; ant' - r'
  00044   49 2b c8             sub    rcx, r8                     ; dia' - r'
  00047   48 0f c8             bswap  rax                         ;(ant' - r')'
  0004a   48 0f c9             bswap  rcx                         ;(dia' - r')'
  0004d   48 33 c2             xor    rax, rdx                    ; ant := (ant' - r')' ^ (ant - r)
  00050   49 33 cb             xor    rcx, r11                    ; dia := (dia' - r')' ^ (dia - r)
  00053   49 23 c1             and    rax, r9                     ; ant &= antidiagMaskEx
  00056   48 23 cb             and    rcx, rbx                    ; dia &= diagonalMaskEx
  00059   48 03 c1             add    rax, rcx                    ; attacks := dia + ant
  0005c   5b                   pop    rbx
  0005d   c3                   ret    0
?bishopAttacks@@YA_K_KI@Z ENDP

```

## Java

[Java](Java "Java") programmer may try [Long.reverseBytes](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html#reverseBytes%28long%29):

```C++

    static private final long[] bitMask = {
        0x0000000000000001, 0x0000000000000002, 0x0000000000000004, 0x0000000000000008,
        0x0000000000000010, 0x0000000000000020, 0x0000000000000040, 0x0000000000000080,
        ...
    };

    static private final long[] diagonalMaskEx = {
        0x8040201008040200, 0x0080402010080400, 0x0000804020100800, 0x0000008040201000,
        0x0000000080402000, 0x0000000000804000, 0x0000000000008000, 0x0000000000000000,
        ...
    };

    /**
     * @param occ - occupancy
     *        sq  - from square
     * @return diagonal attacks from sq with occupancy occ
     */
    static public long diagonalAttacks(long occ, int sq)
    {
       long forward = occ & diagonalMaskEx[sq];
       long reverse = Long.reverseBytes(forward);
       forward -= bitMask[sq];
       reverse -= bitMask[sq^56];
       forward ^= Long.reverseBytes(reverse);
       forward &= diagonalMaskEx[sq];
       return forward;
    }

```

[Long.reverse](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Long.html#reverse%28long%29) for a generalized attack getter even for ranks is too expensive, except a [JVM](https://en.wikipedia.org/wiki/Java_Virtual_Machine) can use a machine instruction rather than a [bit-reversal](Flipping_Mirroring_and_Rotating#Rotationby180degrees "Flipping Mirroring and Rotating") routine:

```C++

    /**
     * @param occ  - occupancy
     *        line - {0..3} {rank, file, diagonal, antidiagonal}
     *        sq   - from square
     * @return attacks from sq on line with occupancy occ
     */
    static public long attacks(long occ, int line, int sq)
    {
       long forward = occ & maskEx[sq][line];
       long reverse = Long.reverse(forward);
       forward -= bitMask[sq];
       reverse -= bitMask[sq^63];
       forward ^= Long.reverse(reverse);
       forward &= maskEx[sq][line];
       return forward;
    }

```

## See also

- [Reverse Bitboards](Reverse_Bitboards "Reverse Bitboards")
- [Obstruction Difference](Obstruction_Difference "Obstruction Difference")
- [SBAMG](SBAMG "SBAMG")
- [SSSE3 Hyperbola Quintessence](SSSE3#SSSE3Version "SSSE3")
- [Subtracting a Rook from a Blocking Piece](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece")

## Forum Posts

- [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140314) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), August 25, 2007
- [Hyperbola Quiesscene: hardly any improvement](http://www.talkchess.com/forum/viewtopic.php?t=25979) by trojanfoe, [CCC](CCC "CCC"), January 13, 2009
- [Comparison of bitboard attack-getter variants](http://www.talkchess.com/forum/viewtopic.php?t=58795) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 04, 2016
- [Re: The wrong way](http://www.talkchess.com/forum/viewtopic.php?t=58667&start=106) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), January 05, 2016 » [SSSE3 Hyperbola Quintessence](SSSE3#SSSE3Version "SSSE3")
- [Understanding first rank attack state generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71312) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), July 18, 2019 » [First Rank Attacks](First_Rank_Attacks "First Rank Attacks")

## External Links

- [GitHub - abulmo/hqperft: Chess move generation based on (H)yperbola (Q)uintessence & range attacks](https://github.com/abulmo/hqperft) by [Richard Delorme](Richard_Delorme "Richard Delorme") » [Perft](Perft "Perft")
- [Sliding Pieces (Part 1) - Advanced Java Chess Engine Tutorial 8](http://www.youtube.com/watch?v=bCH4YK6oq8M&list=SPQV5mozTHmacMeRzJCW_8K3qw2miYqd0c&index=9) by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin")
- [Hyperbola Quintessence for rooks along ranks](http://timcooijmans.blogspot.co.uk/2014/04/hyperbola-quintessence-for-rooks-along.html) by [Tim Cooijmans](https://www.blogger.com/profile/11033414990764447420), April 6, 2014 <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## Hyperbola

- [Hyperbola from Wikipedia](https://en.wikipedia.org/wiki/Hyperbola)
- [The Eulerian Hyperbola](http://www.paideiaschool.org/TeacherPages/Steve_Sigur/resources/Eulerian%20hyperbola/Eulerian%20hyperbola.html)
- [Foci of a Hyperbola](http://www.mathwords.com/f/foci_hyperbola.htm) from [mathwords.com](http://www.mathwords.com/)

## Quintessence

- [Quintessence from Wikipedia](https://en.wikipedia.org/wiki/Quintessence)
- [Quintessence (physics) from Wikipedia](<https://en.wikipedia.org/wiki/Quintessence_(physics)>)
- [Quintessence the Fifth Element from Wikipedia](<https://en.wikipedia.org/wiki/Aether_(classical_element)#Fifth_element>)

## Misc

- [Focus](Category:Focus "Category:Focus") - [Hocus Pocus](https://en.wikipedia.org/wiki/Hocus_Pocus_%28song%29), [Pinkpop Festival](https://en.wikipedia.org/wiki/Pinkpop_Festival) 1972, [Geleen](https://en.wikipedia.org/wiki/Geleen), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Samuel Bak - represented by Pucker Gallery since 1969](https://www.puckergallery.com/artists/#/samuel-bak/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [\_byteswap_uint64](http://msdn.microsoft.com/en-us/library/a3140177.aspx) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: BitBoard Tests Magic v Non-Rotated 32 Bits v 64 Bits](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=140314) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), August 25, [2007](Timeline#2007 "Timeline")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Intel 64 and IA32 Architectures Optimization Reference Manual](http://www.intel.com/assets/pdf/manual/248966.pdf) (pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [\_mm_shuffle_epi8](http://msdn.microsoft.com/en-us/library/bb531427.aspx) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Hyperbola Quintessence for rooks along ranks](http://timcooijmans.blogspot.co.uk/2014/04/hyperbola-quintessence-for-rooks-along.html) by [Tim Cooijmans](https://www.blogger.com/profile/11033414990764447420), April 6, 2014
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Comparison of bitboard attack-getter variants](http://www.talkchess.com/forum/viewtopic.php?t=58795&start=10) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), January 04, 2016

**[Up one Level](Sliding_Piece_Attacks "Sliding Piece Attacks")**

