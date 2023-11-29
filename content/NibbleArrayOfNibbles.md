---
title: NibbleArrayOfNibbles
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Nibble**


A **Nibble**, also called Nybble, is a term for a four-[bit](Bit "Bit") aggregation. It is the half of a [Byte](Byte "Byte"). With four bits one can distinct 16 states, 0000B to 1111B as [binary code](https://en.wikipedia.org/wiki/Binary_code), representing [decimal](https://en.wikipedia.org/wiki/Decimal) numbers from 0 to 15.


One [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) digit {'0'..'9', 'A' ..'F'} exactly covers one nibble. Since bytes are considered atomic items, nibble [endianness](Endianness "Endianness") is no issue. Per definition a least significant nibble covers the least significant bits 0..3 of a byte, the most significant nibble the bits 4..7 of a byte. If we write the value of a byte with two hexadecimal digits, we use the usual [big-endian](Big-endian "Big-endian") notation, e.g. in 0x3F, '3' is the most significant nibble (digit) and 'F' the least significant one.



## Signed Nibbles


In a signed nibble [Two's Complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") representation, bit 3 is interpreted as sign bit.





|  binary
 |  hex
 |  unsigned
 |  signed
 |
| --- | --- | --- | --- |
|  0000B
 |  0x0
 |  0
 |  0
 |
|  0001B
 |  0x1
 |  1
 |  1
 |
|  0010B
 |  0x2
 |  2
 |  2
 |
|  0011B
 |  0x3
 |  3
 |  3
 |
|  0100B
 |  0x4
 |  4
 |  4
 |
|  0101B
 |  0x5
 |  5
 |  5
 |
|  0110B
 |  0x6
 |  6
 |  6
 |
|  0111B
 |  0x7
 |  7
 |  7
 |
|  1000B
 |  0x8
 |  8
 |  -8
 |
|  1001B
 |  0x9
 |  9
 |  -7
 |
|  1010B
 |  0xA
 |  10
 |  -6
 |
|  1011B
 |  0xB
 |  11
 |  -5
 |
|  1100B
 |  0xC
 |  12
 |  -4
 |
|  1101B
 |  0xD
 |  13
 |  -3
 |
|  1110B
 |  0xE
 |  14
 |  -2
 |
|  1111B
 |  0xF
 |  15
 |  -1
 |






## Array of Nibbles


An [array](Array "Array") of N nibbles can be declared as array of (N+1)/2 bytes, for instance for a dense [Board Representation](Board_Representation "Board Representation").




```C++
BYTE nibbleBoard[32];

```

And this is how to extract piece-codes from a that board:




```C++
int getPiece(int square) {
   int shift = (square & 1)  << 2; // 4 or 0
   return nibbleBoard[square >> 1] >> shift) & 15;
}

void setPiece(int square, int piece) {
   int shift = (square & 1) << 2; // 4 or 0
   nibbleBoard[square >> 1] &= (BYTE)(  240 >> shift);
   nibbleBoard[square >> 1] |= (BYTE)(piece << shift);
}

```

This is considerable more effort than simple array access with at least byte granulation, in both code size and runtime - and array board representations are likely not member of a search [stack](Stack "Stack"), but updated incrementally during [make](Make_Move "Make Move") and [unmake](Unmake_Move "Unmake Move"), it does not seem to make sense to use nibbleBoards as mentioned to save some data bytes. However, [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") proposed the Nibble-Board as used in his program [Axon](Axon "Axon") and its parallel version [Achilles](Achilles "Achilles"), dubbed *Compact Chessboard Representation*, declared as array of eight 32-bit or four 64-bit integers, intended for register processing <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## SWAR Nibbles


To apply 'add' or 'sub' on vectors of nibbles (or any arbitrary structure) [SWAR-wise](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") within a 32-bit or 64-bit register, we have to take care carries and borrows don't wrap around. Thus we apply a mask of all most significant bits (H) and 'add' in two steps, one 'add' with MSB clear and one add modulo 2 aka 'xor' for the MSB itself. For nibble-wise math of a vector of eight nibbles inside a 32-bit register, H is 0x88888888 and L is 0x11111111.




```C++
SWAR add z = x + y
    z = ((x &~H) + (y &~H)) ^ ((x ^ y) & H)
 
SWAR sub z = x - y
    z = ((x | H) - (y &~H)) ^ ((x ^~y) & H)
 
SWAR average z = (x+y)/2 based on x + y = (x^y) + 2*(x&y)
    z = (x & y) + (((x ^ y) & ~L) >> 1)

```

## See also


* [Byte](Byte "Byte")
* [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards") containing "vertical" nibbles
* [SWAR](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques")
* [SWAR Population Count](Population_Count#SWARPopcount "Population Count")


## Publications


* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2008**). *The Compact Chessboard Representation*. [ICGA Journal, Vol. 31, No. 3](ICGA_Journal#31_3 "ICGA Journal")
* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2012**). *An Alternative Efficient Chessboard Representation based on 4-Bit Piece Coding*. [Yugoslav Journal of Operations Research, Vol. 22, No. 1](http://www.doiserbia.nb.rs/issue.aspx?issueid=1761), [pdf](http://www.doiserbia.nb.rs/img/doi/0354-0243/2012/0354-02431200011V.pdf)


## Forum Posts


* [CCR board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69046) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), November 25, 2018 » [Array of Nibbles](#arrayofnibbles)


## External Links


* [Nibble from Wikipedia](https://en.wikipedia.org/wiki/Nibble)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2008**). *The Compact Chessboard Representation*. [ICGA Journal, Vol. 31, No. 3](ICGA_Journal#31_3 "ICGA Journal")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2012**). *An Alternative Efficient Chessboard Representation based on 4-Bit Piece Coding*. [Yugoslav Journal of Operations Research, Vol. 22, No. 1](http://www.doiserbia.nb.rs/issue.aspx?issueid=1761), [pdf](http://www.doiserbia.nb.rs/img/doi/0354-0243/2012/0354-02431200011V.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [CCR board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69046) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), November 25, 2018

**[Up one Level](Data "Data")**







 
