---
title: Littleendian
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* [Endianness](Endianness "Endianness") \* Little-endian**


**Little-endian** is most often referred to the [endianness](Endianness "Endianness") or order of multiple [Bytes](Byte "Byte") inside a composite item, such as a [Word](Word "Word") (two bytes), a [Double Word](Double_Word "Double Word") (four bytes) or a [Quad Word](Quad_Word "Quad Word") (eight bytes), which keeps the byte order (in the arithmetical sense) in the order of their addresses in [memory](Memory "Memory") - for instance the double word integer 16909060 or 0x01020304. 



### Contents


* [1 Memory layout](#memory-layout)
* [2 Runtime Test](#runtime-test)
* [3 Little-Endian Files](#little-endian-files)
* [4 Little-Endian Ranks](#little-endian-ranks)
* [5 Least Significant Files](#least-significant-files)
* [6 Date-Format](#date-format)
* [7 See also](#see-also)
* [8 External Links](#external-links)






0x01020304





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


## Runtime Test


Following [C](C "C")-routine returns "true" on little-endian machines, such as [Intel](Intel "Intel") [x86](X86 "X86"):




```

bool isLittleEndian() {
   short one = 0x0001; // 16 bit
   return (bool) (*(char*)&one);
}

```

## Little-Endian Files


File index 0 maps the A-File, index 7 the H-File.



## Little-Endian Ranks


Rank index 0 maps the first Rank, index 7 the eight Rank.



## Least Significant Files


* [Files](Files "Files") are the little-end below [ranks](Ranks "Ranks"):



```

squareIndex = 8*rankIndex + fileIndex
rankIndex   = squareIndex div 8
fileIndex   = squareIndex mod 8

```

The LERF-coordianetes with Little-Endian Files and Little-Endian Ranks:




```

enum enumSquare {
  a1, b1, c1, d1, e1, f1, g1, h1, //  0 ..  7
  a2, b2, c2, d2, e2, f2, g2, h2, //  8 .. 15
  a3, b3, c3, d3, e3, f3, g3, h3, // 16 .. 23
  a4, b4, c4, d4, e4, f4, g4, h4, // 24 .. 31
  a5, b5, c5, d5, e5, f5, g5, h5, // 32 .. 39
  a6, b6, c6, d6, e6, f6, g6, h6, // 40 .. 47
  a7, b7, c7, d7, e7, f7, g7, h7, // 48 .. 55
  a8, b8, c8, d8, e8, f8, g8, h8  // 56 .. 63
};

```

*Note: If printing boards from top to bottom, one has to start with the big-end rank.*




```

     A    B    C    D    E    F    G    H
   +----+----+----+----+----+----+----+----+
 8 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |  8th rank
   +----+----+----+----+----+----+----+----+
 7 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |  7th rank
   +----+----+----+----+----+----+----+----+
 6 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |  6th rank
   +----+----+----+----+----+----+----+----+
 5 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |  5th rank
   +----+----+----+----+----+----+----+----+
 4 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |  4th rank
   +----+----+----+----+----+----+----+----+
 3 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |  3rd rank
   +----+----+----+----+----+----+----+----+
 2 |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 |  2nd rank
   +----+----+----+----+----+----+----+----+
 1 |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  1st rank
   +----+----+----+----+----+----+----+----+
     A    B    C    D    E    F    G    H - file(s)

```

## Date-Format


The little-endian date format: dd-mm-yyyy.



## See also


* [Big-endian](Big-endian "Big-endian")
* [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations")
* [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
* [Word](Word "Word")
* [Double Word](Double_Word "Double Word")
* [Quad Word](Quad_Word "Quad Word")


## External Links


* [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
* [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](https://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](https://en.wikipedia.org/wiki/Danny_Cohen_(engineer)), [USC/ISI](https://en.wikipedia.org/wiki/Information_Sciences_Institute), April 1, 1980


**[Up one Level](Endianness "Endianness")**







 
