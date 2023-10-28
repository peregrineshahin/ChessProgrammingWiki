---
title: Word
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Word**


A **Word** or Computer Word, is a term for the natural unit of data used by a particular computer architecture. Modern computers usually have a word size to be a power of 2 multiple of the unit of address resolution, likely a [Byte](Byte "Byte"), that is two, four, or eight Bytes, which are 16, 32, or 64 [bits](Bit "Bit"). Many other sizes have been used in the past, including 8 (a Byte), 9, 12, 18, 24, 36, 39, 40, 48, and 60 bits. Some of the early computers were decimal rather than binary, having a word size of 10 or 12 decimal digits, and some of them had no fixed word length at all.



### Contents


* [1 16-bit Word](#16-bit-word)
* [2 Short](#short)
* [3 Ranges](#ranges)
* [4 Alignment](#alignment)
* [5 Endianness](#endianness)
* [6 Extracting Bytes](#extracting-bytes)
* [7 See also](#see-also)
* [8 External Links](#external-links)






Often the size of a word is defined to be a value for compatibility with earlier computers, such as [Intel's](Intel "Intel") [x86](X86 "X86") and [x86-64](X86-64 "X86-64") architecture, which referes a **Word** from the original [8086](8086 "8086") 16-bit µ-Processor. Subsequently Intel used the terms [Double Word](Double_Word "Double Word") (**dword**) for 32-bit words, a quadruple word or [Quad Word](Quad_Word "Quad Word") (**qword**) for 64-bits words, and even a [Double Quad Word](index.php?title=Double_Quad_Word&action=edit&redlink=1 "Double Quad Word (page does not exist)") for 128-bit words. [x86](X86 "X86") and [x86-64](X86-64 "X86-64") registers may still treated as word registers (ax versus eax or even rax) , while it is recommend to use the native 32-bit [double word](Double_Word "Double Word"), because the word-wise access requires a prefix byte to overwrite the default width. [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction sets like [MMX](MMX "MMX"), [AltiVec](AltiVec "AltiVec") and [SSE2](SSE2 "SSE2") provide operations on vectors of four or eight words inside appropriate SIMD-registers. [IBM 360](IBM_360 "IBM 360") and successors with 32-bit words, refer 16-bit size as **halfword**.



## Short


On recent 32-bit and 64-bit processors the primitive [C](C "C") datatype **short** and **unsigned short** refers to 16-bit words by most compilers for those architectures. In [Java](Java "Java"), **short** is guaranteed to have 16-bit. Signed short in C is assumed to use [Twos' Complement](index.php?title=Twos%27_Complement&action=edit&redlink=1 "Twos' Complement (page does not exist)"), but not strictly specified. A Word-type, explicitly type-defined in C, is therefor usually treated as unsigned, also to avoid arithmetical right shift issues:




```

typedef unsigned char  BYTE;
typedef unsigned short WORD;

```





## Ranges




|  language
 |  type
 |  min
 |  max
 |
| --- | --- | --- | --- |
| [C](C "C"), [C++](Cpp "Cpp") |  unsigned short
 |  0
 |  65535
 |
|  hexadecimal
 |  0x0000
 |  0xFFFF
 |
|  #include <limits.h>
 |  |  USHRT\_MAX
 |
| [C](C "C"), [C++](Cpp "Cpp"),[Java](Java "Java") |  short
 |  -32768
 |  32767
 |
|  hexadecimal
 |  0x8000
 |  0x7FFF
 |
|  #include <limits.h>
 |  SHRT\_MIN
 |  SHRT\_MAX
 |


## Alignment


Words stored in memory should be stored at even byte addresses. Otherwise at runtime it will cause a miss-alignment exception on some processors, or a huge penalty on others.



## Endianness


*Main article: [Endianness](Endianness "Endianness").*
An issue with words consisting of two or more bytes, is the order, bytes may appear inside a word of memory. According to their usual arithmetical significance, there is a low and a high byte of a 16-bit word, which may either be stored at the lower or higher byte-address in memory. Intel processors were always so called [little-endian](Little-endian "Little-endian") machines, the least significant byte (LSB) is at the lowest address. Other processors, including the [IBM 370](IBM_370 "IBM 370") family, the [PDP-10](PDP-10 "PDP-10") (36 bit), the Motorola microprocessor families, and most of the various RISC designs are [big-endian](Big-endian "Big-endian"), and store the ‘big-end-first’.



## Extracting Bytes


Following C union to extract or synthesize bytes from/in words, is not portable and should be avoided.




```

union {
   BYTE b[2];
   WORD s;
} u;

u.s = 0xaa55;
assert (u.b[0] == 0x55); // fails, if big-endian

```

The portable way in C can be done with inlined functions or C preprocessor macros, using arithmetical divide or modulo by 256, aka shift and mask by bitwise 'and' - or for the synthesis multiplication of high byte by 256 plus low byte:




```

BYTE lowByte (WORD s) {return (BYTE)(s & 255);} // mod 256
BYTE highByte(WORD s) {return (BYTE)(s >>  8);} // div 256

WORD makeWORD (BYTE high, BYTE low) {
   WORD  s = high;
   return (s << 8) + low; // high * 256 + low
}

```

## See also


* [Byte](Byte "Byte")
* [Double Word](Double_Word "Double Word")
* [Quad Word](Quad_Word "Quad Word")


## External Links


* [Word from Wikipedia](https://en.wikipedia.org/wiki/Word_%28computer_science%29)
* [Byte from Wikipedia](https://en.wikipedia.org/wiki/Byte)
* [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
* [Understanding Big and Little Endian Byte Order](http://betterexplained.com/articles/understanding-big-and-little-endian-byte-order/)
* [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](http://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](http://www.myri.com/staff/cohen/), [U S C/I S I](http://ai.isi.edu/), April 1, 1980
* [Mahavishnu Orchestra](Category:Mahavishnu_Orchestra "Category:Mahavishnu Orchestra") - [One Word](https://en.wikipedia.org/wiki/Birds_of_Fire), Live at Bananafish Gardens, [Brooklyn](https://en.wikipedia.org/wiki/Brooklyn), N.Y. 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [John McLaughlin](Category:John_McLaughlin "Category:John McLaughlin"), [Billy Cobham](Category:Billy_Cobham "Category:Billy Cobham"), [Rick Laird](Category:Rick_Laird "Category:Rick Laird"), [Jan Hammer](Category:Jan_Hammer "Category:Jan Hammer"), [Jerry Goodman](https://en.wikipedia.org/wiki/Jerry_Goodman)
 
**[Up one Level](Data "Data")**







 
