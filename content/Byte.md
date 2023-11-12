---
title: Byte
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Byte**

A **Byte**, more precise an **Octet**, is a unit of measurement of information storage, consisting of **eight** [bits](Bit "Bit"). In most computer architectures it is the granularity of memory addresses, containing 8-bit numbers, 256 different symbols - interpreted as signed or unsigned numbers, [ASCII](https://en.wikipedia.org/wiki/ASCII) characters or machine code. Processors provide byte-wise arithmetical and logical units. [x86](X86 "X86") and [x86-64](X86-64 "X86-64") can address the two lower bytes of each 32 or 64 bit register, for instance AL and AH from EAX or RAX. [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction sets like [MMX](MMX "MMX"), [AltiVec](AltiVec "AltiVec") and [SSE2](SSE2 "SSE2") provide operations on vectors of eight or sixteen bytes inside appropriate SIMD-registers.

The programming languages [C](C "C") and [C++](Cpp "Cpp") define a byte as a "addressable unit of data storage large enough to hold any member of the basic character set of the execution environment".

## Char

The [C](C "C")-datatype **unsigned char** covers one byte and has a numerical range of 0 to 255. The primitive **char** in [Java](Java "Java") is a signed byte, and ranges from -128 to +127. Same is likely true for signed char in C, though [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement) is not strictly specified. Same is true for signed right shifts, where [x86](X86 "X86") performs shift arithmetical right, but other processors and their compilers possibly shift in always zeros. Bytes are therefor often type defined as **unsigned char** in C:

```C++

typedef unsigned char BYTE;

```

[Mailbox](Mailbox "Mailbox") chess programs often use an [array](Array "Array") of bytes for a dense [Board Representation](Board_Representation "Board Representation"), where each byte contains [piece- or empty square code](Pieces#PieceCoding "Pieces") for each indexed [square](Squares "Squares"). A Byte is also sufficient to store usual (0..63), or [0x88](0x88 "0x88") board coordinates. A byte can contain a rank of a [bitboard](Bitboards "Bitboards"). For pawn-structure issues, [filesets](</Pawns_and_Files_(Bitboards)#Fileset> "Pawns and Files (Bitboards)") are a dense set-wise representation to cover boolean properties for each [file](Files "Files").

A byte can be written with two hexadecimal digits, 0x00 to 0xff in [C](C "C") or [Java](Java "Java"). Take care and compiler warnings serious, if wider types are assigned to bytes - since all upper bits are lost, if wider types are outside the valid signed or unsigned range.

## SWAR Bytes

To apply 'add' or 'sub' on vectors of bytes (or any arbitrary structure) [SWAR-wise](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") within a 32-bit or 64-bit register, we have to take care carries and borrows don't wrap around. Thus we apply a mask of all most significant bits (H) and 'add' in two steps, one 'add' with MSB clear and one add modulo 2 aka 'xor' for the MSB itself. For byte-wise math of a vector of four bytes inside a 32-bit register, H is 0x80808080 and L is 0x01010101.

```C++

SWAR add z = x + y
    z = ((x &~H) + (y &~H)) ^ ((x ^ y) & H)
 
SWAR sub z = x - y
    z = ((x | H) - (y &~H)) ^ ((x ^~y) & H)
 
SWAR average z = (x+y)/2 based on x + y = (x^y) + 2*(x&y)
    z = (x & y) + (((x ^ y) & ~L) >> 1)

```

## See also

- [Byte Magazine](Byte_Magazine "Byte Magazine")
- [Nibble](Nibble "Nibble")
- [Filesets](</Pawns_and_Files_(Bitboards)#Fileset> "Pawns and Files (Bitboards)")
- [First Rank Attacks](First_Rank_Attacks "First Rank Attacks")
- [Word](Word "Word")
- [Double Word](Double_Word "Double Word")
- [Quad Word](Quad_Word "Quad Word")
- [SWAR](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques")

## External Links

- [Byte from Wikipedia](https://en.wikipedia.org/wiki/Byte)
- [Octet from Wikipedia](https://en.wikipedia.org/wiki/Octet_%28computing%29)

**[Up one Level](Data "Data")**

