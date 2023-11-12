---
title: Double Word
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Double Word**

According to [Intel's](Intel "Intel") definition of a [x86](X86 "X86") 16-bit [Word](Word "Word"), a **Double Word** refers a 32-bit entity, while [IBM 360](IBM_360 "IBM 360") and successors with 32-bit words have double words with 64-bit.

## Integer and long

Even in [x86-64](X86-64 "X86-64"), double words are still considered as default word size. [x86](X86 "X86") and and [x86-64](X86-64 "X86-64") [C-Compiler](index.php?title=C-Compiler&action=edit&redlink=1 "C-Compiler (page does not exist)") use double words as signed and unsigned integers, [Java](Java "Java") integers as well. Microsoft 64 bit compiler long is a 32-bit Double word as well, while with 64-bit [GCC](Free_Software_Foundation#GCC "Free Software Foundation") uses 64-bit [Quad Words](Quad_Word "Quad Word") as longs.

```C++

typedef unsigned int DWORD;

```

## Ranges

|  language
|  type
|  min
|  max
|
| --- | --- | --- | --- |
| [C](C "C"), [C++](Cpp "Cpp") |  unsigned int
|  0
|  4,294,967,295
|
|  hexadecimal
|  0x00000000
|  0xFFFFFFFF
|
| [C](C "C"), [C++](Cpp "Cpp"),[Java](Java "Java") |  int
|  -2,147,483,648
|  2,147,483,647
|
|  hexadecimal
|  0x80000000
|  0x7FFFFFFF
|

## Alignment

Double Words stored in memory should be stored at byte addresses divisible by four. Otherwise at runtime it will cause a miss-alignment exception on some processors, or a huge penalty on others.

## Endianness

*Main article: [Endianness](Endianness "Endianness").*

## Litte-endian Layout

The [little-endian](Little-endian "Little-endian") memory layout, as typical for [Intel](Intel "Intel") [x86](X86 "X86") cpus.
For instance the double word integer 16909060 or 0x01020304:

|  Address
|  Byte
|  Significance
|
| --- | --- | --- |
|  0x0000
|  0x04
|  LS Byte
|
|  0x0001
|  0x03
|  |
|  0x0002
|  0x02
|  |
|  0x0003
|  0x01
|  MS Byte
|

## Big-endian Layout

The [big-endian](Big-endian "Big-endian") memory layout, as typical for [Motorola](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") cpus.
For instance the double word integer 16909060 or 0x01020304:

|  Address
|  Byte
|  Significance
|
| --- | --- | --- |
|  0x0000
|  0x01
|  MS Byte
|
|  0x0001
|  0x02
|  |
|  0x0002
|  0x03
|  |
|  0x0003
|  0x04
|  LS Byte
|

## See also

- [Piece-Sets](Piece-Sets "Piece-Sets")
- [Byte](Byte "Byte")
- [Word](Word "Word")
- [Quad Word](Quad_Word "Quad Word")

## External Links

- [Dword, Qword, and Oword from Wikipedia](https://en.wikipedia.org/wiki/Word_%28computer_science%29#Dword.2C_Qword.2C_and_Oword)
- [Byte from Wikipedia](https://en.wikipedia.org/wiki/Byte)
- [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
- [Understanding Big and Little Endian Byte Order](http://betterexplained.com/articles/understanding-big-and-little-endian-byte-order/)
- [DAV's Endian FAQ - ON HOLY WARS AND A PLEA FOR PEACE](http://www.rdrop.com/%7Ecary/html/endian_faq.html) by Danny Cohen

**[Up one Level](Data "Data")**

