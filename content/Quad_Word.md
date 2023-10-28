---
title: Quad Word
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* Quad Word**


According to [Intel's](Intel "Intel") definition of a [x86](X86 "X86") 16-bit [Word](Word "Word"), a **Quad Word** refers a 64-bit word.



### Contents


* [1 long long or long](#long-long-or-long)
* [2 Bitboards](#bitboards)
* [3 Ranges](#ranges)
* [4 Alignment](#alignment)
* [5 Endianness](#endianness)
	+ [5.1 Litte-endian Layout](#litte-endian-layout)
	+ [5.2 Big-endian Layout](#big-endian-layout)
* [6 See also](#see-also)
* [7 External Links](#external-links)






Microsoft 64-bit [C](C "C")-compiler long is still 32-bit [Double Word](Double_Word "Double Word"), while 64-bit [GCC](Free_Software_Foundation#GCC "Free Software Foundation") uses 64-bit Quad Words as longs. Other compiler require "long long" for 64-bit types.




```

typedef unsigned long QWORD;
typedef unsigned long long QWORD;

```

## Bitboards


Quad words are used as [bitboard](Bitboards "Bitboards") datatype:




```

typedef QWORD U64;
typedef QWORD Bitboard;

```

## Ranges




|  language
 |  type
 |  min
 |  max
 |
| --- | --- | --- | --- |
| [C](C "C"), [C++](Cpp "Cpp") |  unsigned long long
 |  0
 |  18,446,744,073,709,551,615
 |
|  hexadecimal
 |  0x0000000000000000
 |  0xFFFFFFFFFFFFFFFF
 |
| [C](C "C"), [C++](Cpp "Cpp"),[Java](Java "Java") |  long long
 |  -9,223,372,036,854,775,808
 |  9,223,372,036,854,775,807
 |
|  hexadecimal
 |  0x8000000000000000
 |  0x7FFFFFFFFFFFFFFF
 |


## Alignment


Quad Words stored in memory should be stored at byte addresses divisible by eight. Otherwise at runtime it will cause a miss-alignment exception on some processors, or a huge penalty on others.



## Endianness


*Main article: [Endianness](Endianness "Endianness").*



### Litte-endian Layout


The [little-endian](Little-endian "Little-endian") memory layout, as typical for [Intel](Intel "Intel") cpus.
For instance the quad word integer 0x0102030405060708





|  Address
 |  Byte
 |  Significance
 |
| --- | --- | --- |
|  0x0000
 |  0x08
 |  LS Byte
 |
|  0x0001
 |  0x07
 |  |
|  0x0002
 |  0x06
 |  |
|  0x0003
 |  0x05
 |  |
|  0x0004
 |  0x04
 |  |
|  0x0005
 |  0x03
 |  |
|  0x0006
 |  0x02
 |  |
|  0x0008
 |  0x01
 |  MS Byte
 |


### Big-endian Layout


The [big-endian](Big-endian "Big-endian") memory layout, as typical for [Motorola](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") cpus.
For instance the quad word integer 0x0102030405060708





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
 |  |
|  0x0004
 |  0x05
 |  |
|  0x0005
 |  0x06
 |  |
|  0x0006
 |  0x07
 |  |
|  0x0007
 |  0x08
 |  LS Byte
 |


## See also


* [Byte](Byte "Byte")
* [Word](Word "Word")
* [Double Word](Double_Word "Double Word")
* [Bitboards](Bitboards "Bitboards")


## External Links


* [Dword, Qword, and Oword from Wikipedia](https://en.wikipedia.org/wiki/Word_%28computer_science%29#Dword.2C_Qword.2C_and_Oword)
* [Byte from Wikipedia](https://en.wikipedia.org/wiki/Byte)
* [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
* [Understanding Big and Little Endian Byte Order](http://betterexplained.com/articles/understanding-big-and-little-endian-byte-order/)
* [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](http://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](http://www.myri.com/staff/cohen/), [U S C/I S I](http://ai.isi.edu/), April 1, 1980


**[Up one Level](Data "Data")**







 
