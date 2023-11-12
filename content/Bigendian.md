---
title: Bigendian
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * [Endianness](Endianness "Endianness") * Big-endian**

**Big-endian** is most often referred to the [endianness](Endianness "Endianness") or order of multiple [Bytes](Byte "Byte") inside a composite item, such as a [Word](Word "Word") (two bytes), a [Double Word](Double_Word "Double Word") (four bytes) or a [Quad Word](Quad_Word "Quad Word") (eight bytes), which keeps the byte order (in the arithmetical sense) in the reverse order of their addresses in [memory](Memory "Memory") - for instance the integer 16909060 or 0x01020304.

## Contents

- [1 Memory layout](#memory-layout)
- [2 Big-Endian Files](#big-endian-files)
- [3 Big-Endian Ranks](#big-endian-ranks)
- [4 Least Significant Ranks](#least-significant-ranks)
- [5 Date-Format](#date-format)
- [6 See also](#see-also)
- [7 External Links](#external-links)

## Memory layout

0x01020304

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

## Big-Endian Files

File index 0 maps the H-File, index 7 the A-File.

## Big-Endian Ranks

Rank index 0 maps the eight Rank, index 7 the first Rank.

## Least Significant Ranks

- [Files](Files "Files") are the big-end over [ranks](Ranks "Ranks"):

```C++

squareIndex = 8*fileIndex + rankIndex
fileIndex   = squareIndex div 8
rankIndex   = squareIndex mod 8

```

The BERF-coordinates with Big-endian [Files](Files "Files") and Big-endian [Ranks](Ranks "Ranks"):

```C++

enum enumSquare {
  h8, h7, h6, h5, h4, h3, h2, h1, //  0 ..  7
  g8, g7, g6, g5, g4, g3, g2, g1, //  8 .. 15
  f8, f7, f6, f5, f4, f3, f2, f1, // 16 .. 23
  e8, e7, e6, e5, e4, e3, e2, e1, // 24 .. 31
  d8, d7, d6, d5, d4, d3, d2, d1, // 32 .. 39
  c8, c7, c6, c5, c4, c3, c2, c1, // 40 .. 47
  b8, b7, b6, b5, b4, b3, b2, b1, // 48 .. 55
  a8, a7, a6, a5, a4, a3, a2, a1, // 56 .. 63
};

```

*Note: If printing boards from top to bottom, one has to start with the big-end rank.*

```C++

     A    B    C    D    E    F    G    H
   +----+----+----+----+----+----+----+----+
 8 | 56 | 48 | 40 | 32 | 24 | 16 |  8 |  0 |  8th rank
   +----+----+----+----+----+----+----+----+
 7 | 57 | 49 | 41 | 33 | 25 | 17 |  9 |  1 |  7th rank
   +----+----+----+----+----+----+----+----+
 6 | 58 | 50 | 42 | 34 | 26 | 18 | 10 |  2 |  6th rank
   +----+----+----+----+----+----+----+----+
 5 | 59 | 51 | 43 | 35 | 27 | 19 | 11 |  3 |  5th rank
   +----+----+----+----+----+----+----+----+
 4 | 60 | 52 | 44 | 36 | 28 | 20 | 12 |  4 |  4th rank
   +----+----+----+----+----+----+----+----+
 3 | 61 | 53 | 45 | 37 | 29 | 21 | 13 |  5 |  3rd rank
   +----+----+----+----+----+----+----+----+
 2 | 62 | 54 | 46 | 38 | 30 | 22 | 14 |  6 |  2nd rank
   +----+----+----+----+----+----+----+----+
 1 | 63 | 55 | 47 | 39 | 31 | 23 | 15 |  7 |  1st rank
   +----+----+----+----+----+----+----+----+
     A    B    C    D    E    F    G    H - file(s)

```

## Date-Format

The big-endian date format: yyyy-mm-dd.

## See also

- [Little-endian](Little-endian "Little-endian")
- [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations")
- [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
- [Word](Word "Word")
- [Double Word](Double_Word "Double Word")
- [Quad Word](Quad_Word "Quad Word")

## External Links

- [Endianness from Wikipedia](https://en.wikipedia.org/wiki/Endianness)
- [IEN 137 - DAV's Endian FAQ - On Holy Wars and a Plea for Peace](https://www.ietf.org/rfc/ien/ien137.txt) by [Danny Cohen](<https://en.wikipedia.org/wiki/Danny_Cohen_(engineer)>), [USC/ISI](https://en.wikipedia.org/wiki/Information_Sciences_Institute), April 1, 1980

**[Up one Level](Endianness "Endianness")**

