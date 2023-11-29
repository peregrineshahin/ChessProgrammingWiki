---
title: BitScanDeBruijnMultiplation
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * BitScan**

[](http://www.mcescher.com/Gallery/back-bmp/LW344.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher") - Eye, 1946 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BitScan**,

a function that determines the bit-index of the least significant 1 [bit](Bit "Bit") ([LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")) or the most significant 1 [bit](Bit "Bit") ([MS1B](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations")) in an integer such as [bitboards](Bitboards "Bitboards"). If exactly one bit is set in an unsigned integer, representing a numerical value of a [power of two](https://en.wikipedia.org/wiki/Power_of_two), this is equivalent to a [base-2 logarithm](https://en.wikipedia.org/wiki/Binary_logarithm). Many implementations have been devised since the advent of bitboards, as described on this page, and some [implementation samples](BitScan#EngineSamples "BitScan") of concrete [open source engines](Category:Open_Source "Category:Open Source") listed for didactic purpose.

## Hardware vs. Software

For recent [x86-64](X86-64 "X86-64") architectures like [Core 2 duo](https://en.wikipedia.org/wiki/Intel_Core_2) and [K10](https://en.wikipedia.org/wiki/AMD_K10), one should use the [Processor Instructions for Bitscans](BitScan#bsfbsr "BitScan") via intrinsics or [inline assembly](Assembly#InlineAssembly "Assembly"), see [x86-64 timing](BitScan#x86Timing "BitScan"). [P4](https://en.wikipedia.org/wiki/Pentium_4) and [K8](https://en.wikipedia.org/wiki/Athlon_64) have rather slow bitscan-instructions. K8 uses so called *vector path instructions* <a id="cite-note-2" href="#cite-ref-2">[2]</a> with 9 or 11 cycles latency, even blocking other processor resources. For these processors, specially K8 with already fast multiplication, the [De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") (64-bit mode) or [Matt Taylor's](Matt_Taylor "Matt Taylor") [Folded 32-bit Multiplication](BitScan#MattTaylorsFoldingtrick "BitScan") (32-bit mode) might be the right choice. Other routines mentioned might be advantageous on certain architectures, specially with slow integer multiplications.

## Non Empty Sets

Bitscan is most often used in  [serializing bitboards](Bitboard_Serialization "Bitboard Serialization"), and is therefor - due to a leading while-condition - not called with empty sets. Until stated otherwise, most mentioned bitscan-routines in [C](C "C")/[C++](Cpp "Cpp") have the same prototype and assume none empty sets as actual parameter.

## Bitscan forward

A bitscan **forward** is used to find the index of the **least** significant 1 bit ([LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")).

## Trailing Zero Count

Bitscan forward is identical with a **Trailing Zero Count** for none empty sets, possibly available as machine instruction on some architectures, for instance the [x86-64](X86-64 "X86-64") bit-manipulation expansion set [BMI1](BMI1 "BMI1"), with some difficulties to use the [\_tzcnt_u64](BMI1#TZCNT "BMI1") intrisic with [Visual Studio](https://en.wikipedia.org/wiki/Microsoft_Visual_Studio) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## De Bruijn Multiplication

The **De Bruijn** bitscan was devised in 1997, according to [Donald Knuth](Donald_Knuth "Donald Knuth") <a id="cite-note-4" href="#cite-ref-4">[4]</a> by [Martin Läuter](Mathematician#MartinLaeuter "Mathematician"), and independently by [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop") and [Keith H. Randall](Keith_H._Randall "Keith H. Randall") a few month later <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> , to determine the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") index by [minimal perfect hashing](Hash_Table#MinimalPerfectHashing "Hash Table"). [De Bruijn sequences](De_Bruijn_Sequence "De Bruijn Sequence") were named after the Dutch mathematician [Nicolaas de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn"). Interestingly sequences with the binary alphabet were already investigated by the French mathematician **Camille Flye Sainte-Marie** in 1894, but later "forgotten" and re-investigated and generalized by De Bruijn and [Tanja van Ardenne-Ehrenfest](Mathematician#Ehrenfest "Mathematician") half a century later <a id="cite-note-7" href="#cite-ref-7">[7]</a> .

A 64-bit De Bruijn Sequence contains 64-overlapped unique 6-bit sequences, thus a circle of 64 bits, where five leading zeros overlap five hidden "trailing" zeros. There are 226 = 67108864 odd sequences with 6 leading binary zeros and 226 even sequences with 5 leading binary zeros, which may be calculated from the odd ones by shifting left one.

### With isolated LS1B

A multiplication with a power of two value (the [isolated LS1B](General_Setwise_Operations#LS1BIsolation "General Setwise Operations")) acts like a left shift by it's exponent. Thus, if we multiply a 64-bit De Bruijn Sequence with the isolated LS1B, we get a unique six bit subsequence inside the most significant bits. To obtain the bit-index we need to extract these upper six bits by shifting right the product, to lookup an [array](Array "Array").

```C++
const int index64[64] = {
    0,  1, 48,  2, 57, 49, 28,  3,
   61, 58, 50, 42, 38, 29, 17,  4,
   62, 55, 59, 36, 53, 51, 43, 22,
   45, 39, 33, 30, 24, 18, 12,  5,
   63, 47, 56, 27, 60, 41, 37, 16,
   54, 35, 52, 21, 44, 32, 23, 11,
   46, 26, 40, 15, 34, 20, 31, 10,
   25, 14, 19,  9, 13,  8,  7,  6
};

/**
 * bitScanForward
 * @author Martin Läuter (1997)
 *         Charles E. Leiserson
 *         Harald Prokop
 *         Keith H. Randall
 * "Using de Bruijn Sequences to Index a 1 in a Computer Word"
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb) {
   const U64 debruijn64 = C64(0x03f79d71b4cb0a89);
   assert (bb != 0);
   return index64[((bb & -bb) * debruijn64) >> 58];
}

```

See also how to [Generate your "private" De Bruijn Bitscan Routine](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator").

### With separated LS1B

Instead of the classical [LS1B isolation](General_Setwise_Operations#LS1BIsolation "General Setwise Operations"), [Kim Walisch](Kim_Walisch "Kim Walisch") proposed the faster [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with the ones' decrement. The separation [bb ^ (bb-1)](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") contains all bits set including and below the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"). The 222 (4,194,304) upper De Bruijn Sequences of the 226 available leave unique 6-bit indices. Using LS1B separation takes advantage of the x86 lea instruction, which saves the move instruction and unlike negate, has no data dependency on the flag register. Kim reported a 10 to 15 percent faster execution (compilers: g++-4.7 -O2, clang++-3.1 -O2, x86_64) than the traditional 64-bit De Bruijn bitscan on [Intel](Intel "Intel") [Nehalem](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) and [Sandy Bridge](https://en.wikipedia.org/wiki/Sandy_Bridge_%28microarchitecture%29) CPUs.

```C++
const int index64[64] = {
    0, 47,  1, 56, 48, 27,  2, 60,
   57, 49, 41, 37, 28, 16,  3, 61,
   54, 58, 35, 52, 50, 42, 21, 44,
   38, 32, 29, 23, 17, 11,  4, 62,
   46, 55, 26, 59, 40, 36, 15, 53,
   34, 51, 20, 43, 31, 22, 10, 45,
   25, 39, 14, 33, 19, 30,  9, 24,
   13, 18,  8, 12,  7,  6,  5, 63
};

/**
 * bitScanForward
 * @author Kim Walisch (2012)
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb) {
   const U64 debruijn64 = C64(0x03f79d71b4cb0a89);
   assert (bb != 0);
   return index64[((bb ^ (bb-1)) * debruijn64) >> 58];
}

```

## Matt Taylor's Folding trick

A 32-bit friendly implementation to find the the bit-index of [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") by [Matt Taylor](Matt_Taylor "Matt Taylor") <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>. The [xor](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with the ones' decrement, [bb ^ (bb-1)](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") contains all bits set including and below the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"). The 32-bit xor-difference of both halves yields either the complement of the upper half, or the lower half otherwise. Some samples:

|  ls1b
|  bb ^ (bb-1)
|  folded
|
| --- | --- | --- |
|  63
| `0xffffffffffffffff` | `0x00000000` |
|  62
| `0x7fffffffffffffff` | `0x80000000` |
|  59
| `0x0fffffffffffffff` | `0xf0000000` |
|  32
| `0x00000001ffffffff` | `0xfffffffe` |
|  31
| `0x00000000ffffffff` | `0xffffffff` |
|  30
| `0x000000007fffffff` | `0x7fffffff` |
|  0
| `0x0000000000000001` | `0x00000001` |

Even if this folded "LS1B" contains multiple consecutive one-bits, the multiplication is De Bruijn like. There are only two magic 32-bit constants with the combined property of 32- and 64-bit De Bruijn Sequences to apply this [minimal perfect hashing](Hash_Table#MinimalPerfectHashing "Hash Table"):

```C++
const int lsb_64_table[64] =
{
   63, 30,  3, 32, 59, 14, 11, 33,
   60, 24, 50,  9, 55, 19, 21, 34,
   61, 29,  2, 53, 51, 23, 41, 18,
   56, 28,  1, 43, 46, 27,  0, 35,
   62, 31, 58,  4,  5, 49, 54,  6,
   15, 52, 12, 40,  7, 42, 45, 16,
   25, 57, 48, 13, 10, 39,  8, 44,
   20, 47, 38, 22, 17, 37, 36, 26
};

/**
 * bitScanForward
 * @author Matt Taylor (2003)
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb) {
   unsigned int folded;
   assert (bb != 0);
   bb ^= bb - 1;
   folded = (int) bb ^ (bb >> 32);
   return lsb_64_table[folded * 0x78291ACF >> 26];
}

```

A slightly modified version may take one [x86](X86 "X86")-register less in 32-bit mode, but calculates bb-1 twice:

```C++
int bitScanForwardM(BitBoard bb) {
   unsigned int folded;
   assert (bb != 0);
   folded  = (int)((bb ^ (bb-1)) >> 32);
   folded ^= (int)( bb ^ (bb-1)); // lea
   return lsb_64_table[folded * 0x78291ACF >> 26];
}

```

with this VC6 generated [x86](X86 "X86") [assembly](Assembly "Assembly") to compare:

```C++
bitScanForward PROC NEAR                   bitScanForwardM PROC NEAR
   mov  ecx, DWORD PTR _bb$[esp-4]            mov  eax, DWORD PTR _bb$[esp-4]
   mov  eax, DWORD PTR _bb$[esp]              mov  ecx, eax
   mov  edx, ecx                              add  ecx, -1
   push esi                                   mov  ecx, DWORD PTR _bb$[esp]
   add  edx, -1                               mov  edx, ecx
   mov  esi, eax                              adc  edx, -1
   adc  esi, -1                               xor  edx, ecx
   xor  ecx, edx                              lea  ecx, DWORD PTR [eax-1]
   xor  eax, esi                              xor  edx, ecx
   pop  esi
   xor  eax, ecx                              xor  edx, eax
   imul eax, 78291acfH                        imul edx, 78291acfH
   shr  eax, 26                               shr  edx, 26
   mov  eax, DWORD PTR _lsb_64_table[eax*4]   mov  eax, DWORD PTR _lsb_64_table[edx*4]
   ret  0                                     ret  0
bitScanForward ENDP                        bitScanForward ENDP

```

## Walter Faxon's magic Bitscan

[Walter Faxon's](Walter_Faxon "Walter Faxon") 32-bit friendly magic bitscan <a id="cite-note-10" href="#cite-ref-10">[10]</a> uses a fast none minimal [perfect hashing](Hash_Table#PerfectHashing "Hash Table") function:

```C++
const char LSB_64_table[154] =
{
##define __ 0
   22,__,__,__,30,__,__,38,18,__, 16,15,17,__,46, 9,19, 8, 7,10,
   0, 63, 1,56,55,57, 2,11,__,58, __,__,20,__, 3,__,__,59,__,__,
   __,__,__,12,__,__,__,__,__,__, 4,__,__,60,__,__,__,__,__,__,
   __,__,__,__,21,__,__,__,29,__, __,37,__,__,__,13,__,__,45,__,
   __,__, 5,__,__,61,__,__,__,53, __,__,__,__,__,__,__,__,__,__,
   28,__,__,36,__,__,__,__,__,__, 44,__,__,__,__,__,27,__,__,35,
   __,52,__,__,26,__,43,34,25,23, 24,33,31,32,42,39,40,51,41,14,
   __,49,47,48,__,50, 6,__,__,62, __,__,__,54
##undef __
};

/**
 * bitScanForward
 * @author Walter Faxon, slightly modified
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb)
{
   unsigned int t32;
   assert(bb);
   bb  ^= bb - 1;
   t32  = (int)bb ^ (int)(bb >> 32);
   t32 ^= 0x01C5FC81;
   t32 +=  t32 >> 16;
   t32 -= (t32 >> 8) + 51;
   return LSB_64_table [t32 & 255]; // 0..63
}

```

A slightly modified version may take one [x86](X86 "X86")-register less in 32-bit mode, but calculates bb-1 twice:

```C++
int bitScanForward(U64 bb)
{
   int t32 = 0x01C5FC81;
   assert(bb);
   t32 ^= (int)((bb ^ (bb-1)) >> 32);
   t32 ^= (int)( bb ^ (bb-1)); // lea
   t32 += t32 >> 16;
   t32 -=(t32 >>  8) + 51;
   return LSB_64_table [t32 & 255];
}

```

The initial [LS1B separation](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") by bb ^ (bb-1) and folding is equivalent to [Matt's](BitScan#MattTaylorsFoldingtrick "BitScan"),

|  ls1b
|  bb ^ (bb-1)
|  folded
|
| --- | --- | --- |
|  63
| `0xffffffffffffffff` | `0x00000000` |
|  62
| `0x7fffffffffffffff` | `0x80000000` |
|  59
| `0x0fffffffffffffff` | `0xf0000000` |
|  32
| `0x00000001ffffffff` | `0xfffffffe` |
|  31
| `0x00000000ffffffff` | `0xffffffff` |
|  30
| `0x000000007fffffff` | `0x7fffffff` |
|  0
| `0x0000000000000001` | `0x00000001` |

while Walter originally resets the LS1B, yielding in a cyclic index wrap:

|  LS1B
|  (bb & (bb-1)) ^ (bb-1)
|  folded
|
| --- | --- | --- |
|  0
| `0x0000000000000000` | `0x00000000` |
|  63
| `0x7fffffffffffffff` | `0x80000000` |
|  60
| `0x0fffffffffffffff` | `0xf0000000` |
|  33
| `0x00000001ffffffff` | `0xfffffffe` |
|  32
| `0x00000000ffffffff` | `0xffffffff` |
|  31
| `0x000000007fffffff` | `0x7fffffff` |
|  1
| `0x0000000000000001` | `0x00000001` |

## Bitscan by Modulo

Another idea is to apply a [modulo](General_Setwise_Operations#Modulo "General Setwise Operations") (remainder of a division) operation of the isolated [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") by the prime number 67 <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> . The remainder 0..66 can be used to [perfectly hash](Hash_Table#PerfectHashing "Hash Table") the bit-index table. Three gaps are 0, 17, and 34, so the mod 67 can make a branchless trailing zero count:

|  Bit-Index
|  Bitboard
|  mod 67
|
| --- | --- | --- |
|  -
| `0x0000000000000000` |  0
|
|  0
| `0x0000000000000001` |  1
|
|  1
| `0x0000000000000002` |  2
|
|  2
| `0x0000000000000004` |  4
|
|  3
| `0x0000000000000008` |  8
|
|  4
| `0x0000000000000010` |  16
|
|  5
| `0x0000000000000020` |  32
|
|  6
| `0x0000000000000040` |  64
|
|  7
| `0x0000000000000080` |  61
|
|  8
| `0x0000000000000100` |  55
|
|  9
| `0x0000000000000200` |  43
|
|  10
| `0x0000000000000400` |  19
|
|  11
| `0x0000000000000800` |  38
|
|  12
| `0x0000000000001000` |  9
|
|  13
| `0x0000000000002000` |  18
|
|  14
| `0x0000000000004000` |  36
|
|  15
| `0x0000000000008000` |  5
|
|  16
| `0x0000000000010000` |  10
|
|  17
| `0x0000000000020000` |  20
|
|  18
| `0x0000000000040000` |  40
|
|  19
| `0x0000000000080000` |  13
|
|  20
| `0x0000000000100000` |  26
|
|  21
| `0x0000000000200000` |  52
|
|  22
| `0x0000000000400000` |  37
|
|  23
| `0x0000000000800000` |  7
|
|  24
| `0x0000000001000000` |  14
|
|  25
| `0x0000000002000000` |  28
|
|  26
| `0x0000000004000000` |  56
|
|  27
| `0x0000000008000000` |  45
|
|  28
| `0x0000000010000000` |  23
|
|  29
| `0x0000000020000000` |  46
|
|  30
| `0x0000000040000000` |  25
|
|  31
| `0x0000000080000000` |  50
|
|  32
| `0x0000000100000000` |  33
|
|  33
| `0x0000000200000000` |  66
|
|  34
| `0x0000000400000000` |  65
|
|  35
| `0x0000000800000000` |  63
|
|  36
| `0x0000001000000000` |  59
|
|  37
| `0x0000002000000000` |  51
|
|  38
| `0x0000004000000000` |  35
|
|  39
| `0x0000008000000000` |  3
|
|  40
| `0x0000010000000000` |  6
|
|  41
| `0x0000020000000000` |  12
|
|  42
| `0x0000040000000000` |  24
|
|  43
| `0x0000080000000000` |  48
|
|  44
| `0x0000100000000000` |  29
|
|  45
| `0x0000200000000000` |  58
|
|  46
| `0x0000400000000000` |  49
|
|  47
| `0x0000800000000000` |  31
|
|  48
| `0x0001000000000000` |  62
|
|  49
| `0x0002000000000000` |  57
|
|  50
| `0x0004000000000000` |  47
|
|  51
| `0x0008000000000000` |  27
|
|  52
| `0x0010000000000000` |  54
|
|  53
| `0x0020000000000000` |  41
|
|  54
| `0x0040000000000000` |  15
|
|  55
| `0x0080000000000000` |  30
|
|  56
| `0x0100000000000000` |  60
|
|  57
| `0x0200000000000000` |  53
|
|  58
| `0x0400000000000000` |  39
|
|  59
| `0x0800000000000000` |  11
|
|  60
| `0x1000000000000000` |  22
|
|  61
| `0x2000000000000000` |  44
|
|  62
| `0x4000000000000000` |  21
|
|  63
| `0x8000000000000000` |  42
|

```C++
/**
 * trailingZeroCount
 * @param bb bitboard to scan
 * @return index (0..63) of least significant one bit, 64 if bb is zero
 */
int trailingZeroCount(U64 bb) {
   static const int lookup67[67+1] = {
      64,  0,  1, 39,  2, 15, 40, 23,
       3, 12, 16, 59, 41, 19, 24, 54,
       4, -1, 13, 10, 17, 62, 60, 28,
      42, 30, 20, 51, 25, 44, 55, 47,
       5, 32, -1, 38, 14, 22, 11, 58,
      18, 53, 63,  9, 61, 27, 29, 50,
      43, 46, 31, 37, 21, 57, 52,  8,
      26, 49, 45, 36, 56,  7, 48, 35,
       6, 34, 33, -1 };
   return lookup67[(bb & -bb) % 67];
}

```

Since div/mod is an expensive instruction, a [modulo by a constant](General_Setwise_Operations#Modulo "General Setwise Operations") is likely replaced by reciprocal fixed point multiplication to get the quotient and a second multiplication and difference to get the remainder. Compared with De Bruijn multiplication it is still too slow.

## Divide and Conquer

This is a broad group of bitscans that test in succession, like the trailing zero count based on [Reinhard Scharnagl's](Reinhard_Scharnagl "Reinhard Scharnagl") proposal <a id="cite-note-13" href="#cite-ref-13">[13]</a> :

```C++
/**
 * trailingZeroCount
 *  like bitScanForward for none empty sets
 * @author Reinhard Scharnagl
 * @param bb bitboard to scan
 * @return index (0..64)
 */
unsigned char lsbRS[256] = {
    8, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    6, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    7, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    6, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    5, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0,
    4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0
};

int trailingZeroCount(U64 b) {
  unsigned buf;
  int acc = 0;

  if ((buf = (unsigned)b) == 0) {
    buf = (unsigned)(b >> 32);
    acc = 32;
  }
  if ((unsigned short)buf == 0) {
    buf >>= 16;
    acc += 16;
  }
  if ((unsigned char)buf == 0) {
    buf >>= 8;
    acc += 8;
  }
  return acc + lsbRS[buf & 0xff];
}

```

What about direct calculation? On [x86](X86 "X86") this is a chain of test, set and lea instructions:

```C++
/**
 * bitScanForward
 * @author Gerd Isenberg
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 bb) {
   unsigned int lsb;
   assert (bb != 0);
   bb &= -bb; // LS1B-Isolation
   lsb = (unsigned)bb
       | (unsigned)(bb>>32);
   return (((((((((((unsigned)(bb>>32) !=0)  * 2)
                 + ((lsb & 0xffff0000) !=0)) * 2)
                 + ((lsb & 0xff00ff00) !=0)) * 2)
                 + ((lsb & 0xf0f0f0f0) !=0)) * 2)
                 + ((lsb & 0xcccccccc) !=0)) * 2)
                 + ((lsb & 0xaaaaaaaa) !=0);
}

```

## Double conversion of LS1B

Assuming 64-bit [doubles](Double "Double") and [little-endian](Little-endian "Little-endian") structure (*not portable*). We convert the isolated [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") to a double and interprete the exponent:

```C++
/**
 * bitScanForward
 * @author Gerd Isenberg
 * @param bb bitboard to scan
 * @return index (0..63) of least significant one bit
 *         -1023 if passing zero
 */
int bitScanForward(U64 bb)
{
   union {
      double d;
      struct {
         unsigned int mantissal : 32;
         unsigned int mantissah : 20;
         unsigned int exponent : 11;
         unsigned int sign : 1;
      };
   } ud;
   ud.d = (double)(bb & -bb); // isolated LS1B to double
   return ud.exponent - 1023;
}

```

## Index of LS1B by Popcount

If we have a fast [population-count](Population_Count "Population Count") instruction, we can count the trailing zeros of [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") after subtracting one:

```C++
// precondition bb != 0
int bitScanForward(U64 bb) {
   assert (bb != 0);
   return popCount( (bb & -bb) - 1 );
}

```

## Bitscan reverse

A bitscan **reverse** is used to find the index of the **most** significant 1 bit ([MS1B](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations")). For non empty sets it is equivalent to [floor](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of the [base-2 logarithm](https://en.wikipedia.org/wiki/Binary_logarithm). MS1B isolalation or separation is more expensive than LS1B isolalation or separation, due to the LS1B related [Two's complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") tricks are not applicable. However, beside Divide and Conquer and Double conversion, Bitscan reverse with MS1B separation is mentioned.

## Divide and Conquer

As introduced by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") in 2000, for an [IA-64](Itanium "Itanium") version of [Crafty](Crafty "Crafty") <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>

```C++
/**
 * bitScanReverse
 * @author Eugene Nalimov
 * @param bb bitboard to scan
 * @return index (0..63) of most significant one bit
 */
int bitScanReverse(U64 bb)
{
   int result = 0;
   if (bb > 0xFFFFFFFF) {
      bb >>= 32;
      result = 32;
   }
   if (bb > 0xFFFF) {
      bb >>= 16;
      result += 16;
   }
   if (bb > 0xFF) {
      bb >>= 8;
      result += 8;
   }
   return result + ms1bTable[bb];
}

```

## Tribute to Frank Zappa

A branchless and little bit obfuscated version of the devide and conquer bitScanReverse with in-register-lookup <a id="cite-note-16" href="#cite-ref-16">[16]</a> - as tribute to [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") with identifiers from [Freak Out!](https://en.wikipedia.org/wiki/Freak_Out!) (1966), [Hot Rats](https://en.wikipedia.org/wiki/Hot_Rats) (1969), [Waka/Jawaka](https://en.wikipedia.org/wiki/Waka/Jawaka) (1972), [Sofa](https://en.wikipedia.org/wiki/Sofa_%28Frank_Zappa_song%29) (1975), [One Size Fits All](https://en.wikipedia.org/wiki/One_Size_Fits_All_%28Frank_Zappa_album%29) (1975), [Sheik Yerbouti](https://en.wikipedia.org/wiki/Sheik_Yerbouti) (1979), and [Jazz from Hell](https://en.wikipedia.org/wiki/Jazz_from_Hell) (1986):

```C++
typedef unsigned __int64 OneSizeFits;
typedef unsigned int HotRats;
const HotRats s      =   0;
const HotRats heik   = 457;
const HotRats y      =   1;
const HotRats e      =   2;
const HotRats r      =   3;
const HotRats b      =   4;
const HotRats o      =   5;
const HotRats u      =   8;
const HotRats t      =  16;
const HotRats i      =  32;
const HotRats     ka = (1<< 4)-1;
const HotRats   waka = (1<< 8)-1;
const HotRats jawaka = (1<<16)-1;
const HotRats jazzFromHell = 0-(16*3*heik);

HotRats freakOut(OneSizeFits all) {
   HotRats so,fa;
   fa   = (HotRats)(all >> i);
   so   = (fa!=s)       << o;
   fa  ^= (HotRats) all & (fa!=s)-y;
   so  ^= (jawaka < fa) << b;
   fa >>= (jawaka < fa) << b;
   so  ^= (  waka - fa) >> t    & u;
   fa >>= (  waka - fa) >> t    & u;
   so  ^= (    ka - fa) >> u    & b;
   fa >>= (    ka - fa) >> u    & b;
   so  ^=  jazzFromHell >> e*fa & r;
   return so;
}

```

## De Bruijn Multiplication

While the [tribute](BitScan#FrankZappa "BitScan") to [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") is quite 32-bit friendly <a id="cite-note-17" href="#cite-ref-17">[17]</a>, [Kim Walisch](Kim_Walisch "Kim Walisch") suggested to use the [parallel prefix fill](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") for a [MS1B](General_Setwise_Operations#TheMostSignificantOneBitMS1B "General Setwise Operations") separation with the same [De Bruijn](De_Bruijn_Sequence "De Bruijn Sequence") multiplication and lookup as in his [bitScanForward](BitScan#KimWalisch "BitScan") routine with [separated LS1B](General_Setwise_Operations#LS1BSeparation "General Setwise Operations"), with less instructions in 64-bit mode. A log base 2 method was already devised by Eric Cole on January 8, 2006, and shaved off rounded up to one less than the next power of 2 by Mark Dickinson <a id="cite-note-18" href="#cite-ref-18">[18]</a> on December 10, 2009, as published in Sean Eron Anderson's *Bit Twiddling Hacks* for 32-bit integers <a id="cite-note-19" href="#cite-ref-19">[19]</a>.

```C++
const int index64[64] = {
    0, 47,  1, 56, 48, 27,  2, 60,
   57, 49, 41, 37, 28, 16,  3, 61,
   54, 58, 35, 52, 50, 42, 21, 44,
   38, 32, 29, 23, 17, 11,  4, 62,
   46, 55, 26, 59, 40, 36, 15, 53,
   34, 51, 20, 43, 31, 22, 10, 45,
   25, 39, 14, 33, 19, 30,  9, 24,
   13, 18,  8, 12,  7,  6,  5, 63
};

/**
 * bitScanReverse
 * @authors Kim Walisch, Mark Dickinson
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of most significant one bit
 */
int bitScanReverse(U64 bb) {
   const U64 debruijn64 = C64(0x03f79d71b4cb0a89);
   assert (bb != 0);
   bb |= bb >> 1; 
   bb |= bb >> 2;
   bb |= bb >> 4;
   bb |= bb >> 8;
   bb |= bb >> 16;
   bb |= bb >> 32;
   return index64[(bb * debruijn64) >> 58];
}

```

## Double conversion

Assuming 64-bit [doubles](Double "Double") and [little-endian](Little-endian "Little-endian") structure (*not portable*!). Conversion to a double, interpreting the exponent. To avoid possible rounding errors, some lower bits may be cleared.

```C++
/**
 * bitScanReverse
 * @author Gerd Isenberg
 * @param bb bitboard to scan
 * @return index (0..63) of most significant one bit
 *         -1023 if passing zero
 */
int bitScanReverse(U64 bb)
{
   union {
      double d;
      struct {
         unsigned int mantissal : 32;
         unsigned int mantissah : 20;
         unsigned int exponent : 11;
         unsigned int sign : 1;
      };
   } ud;
   ud.d = (double)(bb & ~(bb >> 32));  // avoid rounding error
   return ud.exponent - 1023;
}

```

## Leading Zero Count

Some processors have a fast leading zero count instruction. The [Motorola](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") [68020](68020 "68020") has a *bit field find first one* instruction (BFFFO), which actually performs an up to 32-bit *Leading Zero Count* <a id="cite-note-20" href="#cite-ref-20">[20]</a> . [x86-64](X86-64 "X86-64") [AMD](AMD "AMD") [K10](https://en.wikipedia.org/wiki/AMD_K10) has *lzcnt* as part of the [SSE4a](SSE4#SSE4a "SSE4") extension <a id="cite-note-21" href="#cite-ref-21">[21]</a> <a id="cite-note-22" href="#cite-ref-22">[22]</a> , [BMI1](BMI1 "BMI1") has *lzcnt* as well, while [AVX-512CD](AVX-512#VPLZCNT "AVX-512") even features leading zero count on vectors of eight bitbaords.

One can replace bitScanReverse of non empty sets by leadingZeroCount xor 63. Like trailing zero count, it returns 64 for empty sets, and might therefor save the leading condition in some applications.

## Bitscan versus Zero Count

While the presented bitscan routines are suited to work only on none empty sets and return a value-range from 0 to 63 as bit-index, leading or trailing zero-count instructions or routines leave 64 for empty sets. Zero-counting has a immanent property of dealing correctly with empty sets - while it likely takes a conditional branch to implement this semantic in bit-scanning.

```C++
int trailingZeroCount(U64 bb) {
    if ( bb )
       return bitScanForward(bb);
    return 64;
}

int leadingZeroCount(U64 bb) {
    if ( bb )
       return bitScanReverse(bb) ^ 63;
    return 64;
}

```

## Bitscan with Reset

While [traversing sets](Bitboard_Serialization "Bitboard Serialization"), one may combine bitscanning with reset found bit. That implies passing the bitboard per reference or pointer, and tends to confuse compilers to keep all inside registers inside a typical serialization loop <a id="cite-note-23" href="#cite-ref-23">[23]</a> <a id="cite-note-24" href="#cite-ref-24">[24]</a>.

```C++
int bitScanForwardWithReset(U64 &bb) { // also called dropForward
    int idx = bitScanForward(bb);
    bb &= bb - 1; // reset bit outside
    return idx;
}

```

## Generalized Bitscan

This generalized bitscan uses a boolean parameter to scan reverse or forward. It relies on bitScanReverse, but conditionally masks the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") in case of scanning forward. It might be used in the [classical approach](Classical_Approach "Classical Approach") to get positive or negative ray directions with one generalized routine.

```C++
 /**
 * generalized bitScan
 * @author Gerd Isenberg
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @param reverse, true bitScanReverse, false bitScanForward
 * @return index (0..63) of least/most significant one bit
 */
 int bitScan(U64 bb, bool reverse) {
    U64 rMask;
    assert (bb != 0);
    rMask = -(U64)reverse;
    bb &= -bb | rMask;
    return bitScanReverse(bb);
 }

```

## Processor Instructions for Bitscans

## x86

[x86-64](X86-64 "X86-64") processors have [bitscan instructions](X86-64#gpinstructions "X86-64") and can be accessed with compilers today through either [inline assembly](Assembly#InlineAssembly "Assembly") or compiler intrinsics. For the Microsoft/Intel C compiler, the intrinsics can be accessed by including and using the instructions *\_BitScanForward64* <a id="cite-note-25" href="#cite-ref-25">[25]</a> , *\_BitScanReverse64* <a id="cite-note-26" href="#cite-ref-26">[26]</a> or \_lzcnt64 <a id="cite-note-27" href="#cite-ref-27">[27]</a> .

```C++
unsigned char_BitScanForward64(unsigned long * Index,  unsigned __int64 Mask);
unsigned char _BitScanReverse64(unsigned long * Index,  unsigned __int64 Mask);
unsigned __int64 __lzcnt64(unsigned __int64 value); // AMD K10 only see CPUID

```

[Linux](Linux "Linux") provides library functions <a id="cite-note-28" href="#cite-ref-28">[28]</a> , find first bit set (ffsll) in a word leaves an index of 1..64, and zero of no bit is set <a id="cite-note-29" href="#cite-ref-29">[29]</a> . [GCC](Free_Software_Foundation#GCC "Free Software Foundation") 4.4.5 further has the Built-in Function *\_builtin_ffsll* for finding the least significant one bit, *\_builtin_ctzll* for trailing, and *\_builtin_clzll* for leading zero count <a id="cite-note-30" href="#cite-ref-30">[30]</a> :

```C++
/* Returns one plus the index of the least significant 1-bit of x, or if x is zero, returns zero */
int __builtin_ffsll (unsigned long long);

/* Returns the number of trailing 0-bits in x, starting at the least significant bit position.
   If x is 0, the result is undefined */
int __builtin_ctzll (unsigned long long);

/* Returns the number of leading 0-bits in x, starting at the most significant bit position.
   If x is 0, the result is undefined */
int __builtin_clzll (unsigned long long);

```

### Emulating Intrinsics

For the GNU C compiler, the intrinsics can be emulated with [inline assembly](Assembly#InlineAssembly "Assembly") <a id="cite-note-31" href="#cite-ref-31">[31]</a> .

```C++
//These processor instructions work only for 64-bit processors
##ifdef _MSC_VER
    #include <intrin.h>
    #ifdef _WIN64
        #pragma intrinsic(_BitScanForward64)
        #pragma intrinsic(_BitScanReverse64)
        #define USING_INTRINSICS
    #endif
##elif defined(__GNUC__) && defined(__LP64__)
    static INLINE unsigned char _BitScanForward64(unsigned long* Index, U64 Mask)
    {
        U64 Ret;
        __asm__
        (
            "bsfq %[Mask], %[Ret]"
            :[Ret] "=r" (Ret)
            :[Mask] "mr" (Mask)
        );
        *Index = (unsigned long)Ret;
        return Mask?1:0;
    }
    static INLINE unsigned char _BitScanReverse64(unsigned long* Index, U64 Mask)
    {
        U64 Ret;
        __asm__
        (
            "bsrq %[Mask], %[Ret]"
            :[Ret] "=r" (Ret)
            :[Mask] "mr" (Mask)
        );
        *Index = (unsigned long)Ret;
        return Mask?1:0;
    }
    #define USING_INTRINSICS
##endif

```

### Intrinsics versus asm

Alternatively, rather than to emulate the intrinsics one might use the standard prototype, by using intrinsics or [inline assembly](Assembly#InlineAssembly "Assembly") for [GCC](Free_Software_Foundation#GCC "Free Software Foundation") <a id="cite-note-32" href="#cite-ref-32">[32]</a> :

```C++
##ifdef USE_X86INTRINSICS
##include <intrin.h>
##pragma intrinsic(_BitScanForward64)
##pragma intrinsic(_BitScanReverse64)

/**
 * bitScanForward
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 x) {
   unsigned long index;
   assert (x != 0);
   _BitScanForward64(&index, x);
   return (int) index;
}

/**
 * bitScanReverse
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of most significant one bit
 */
int bitScanReverse(U64 x) {
   unsigned long index;
   assert (x != 0);
   _BitScanReverse64(&index, x);
   return (int) index;
}
##else

/**
 * bitScanForward
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of least significant one bit
 */
int bitScanForward(U64 x) {
   assert (x != 0);
   asm ("bsfq %0, %0" : "=r" (x) : "0" (x));
   return (int) x;
}

/**
 * bitScanReverse
 * @param bb bitboard to scan
 * @precondition bb != 0
 * @return index (0..63) of most significant one bit
 */
int bitScanReverse(U64 x) {
   assert (x != 0);
   asm ("bsrl %0, %0" : "=r" (x) : "0" (x));
   return (int) x;
}
##endif

```

### Bsf/Bsr x86-64 Timings

The instruction latency and reciprocal throughput <a id="cite-note-33" href="#cite-ref-33">[33]</a> heavily differs between various [x86-64](X86-64 "X86-64") architectures:

|  Architecture Stepping
|  Instruction(s)
|  Latency / Cycles
|  Reciprocal Throughput
|
| --- | --- | --- | --- |
| [AMD](AMD "AMD") |
| [K8](https://en.wikipedia.org/wiki/Athlon_64) <a id="cite-note-34" href="#cite-ref-34">[34]</a> |  BSF reg16/32/64, mreg16/32/64
|  Vector Path 8/8/9
|  8/8/9
|
|  BSR reg16/32/64, mreg16/32/64
|  Vector Path 11
|  11
|
| [K10](https://en.wikipedia.org/wiki/AMD_K10) <a id="cite-note-35" href="#cite-ref-35">[35]</a> |  BSF reg, reg
|  Vector Path 4
|  4
|
|  BSR reg, reg
|  Vector Path 4
|  4
|
| [LZCNT](SSE4#ABM "SSE4") reg, reg
|  Direct Path single 2
|  1
|
| [Intel](Intel "Intel") <a id="cite-note-36" href="#cite-ref-36">[36]</a> |
| [ATOM](https://en.wikipedia.org/wiki/Intel_Atom) |  BSF/BSR
|  16
|  15
|
| [NetBurst](https://en.wikipedia.org/wiki/NetBurst_%28microarchitecture%29) 0F_3H
|  BSF/BSR
|  16
|  4
|
|  NetBurst 0F_2H
|  BSF/BSR
|  8
|  2
|
| [Core](https://en.wikipedia.org/wiki/Core_%28microarchitecture%29) 06_0EH
|  BSF/BSR
|  2
|  1
|
|  65 nm Intel Core 06_0FH
|  BSF/BSR
|  2
|  1
|
|  Enhanced Intel Core 06_17H
|  BSF/BSR
|  1
|  1
|
|  Enhanced Intel Core 06_1DH
|  BSF/BSR
|  1
|  1
|
| [Nehalem](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) 06_1AH
|  BSF/BSR
|  3
|  1
|
| [Sandy Bridge](https://en.wikipedia.org/wiki/Sandy_Bridge)
[Ivy Bridge](https://en.wikipedia.org/wiki/Ivy_Bridge_%28microarchitecture%29)
[Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29)
|  BSF/BSR
|  3
|  1
|
| [LZCNT](BMI1#LZCNT "BMI1") |  3
|  1
|
| [TZCNT](BMI1#LZCNT "BMI1") |  3
|  1
|

### Bsf/Bsr behavior with zero source

[Intel](Intel "Intel") and [AMD](AMD "AMD") specify different behavior. In praxis there seems no difference so far. However, as long as Intel docs explicitly state content undefined, it is recommend to don't rely on a pre-initialized content of that target register, if the source is zero.

- Intel : If the content of the source operand is 0, the content of the destination operand is undefined. <a id="cite-note-37" href="#cite-ref-37">[37]</a>
- AMD: If the second operand contains 0, the instruction sets ZF to 1 and does not change the contents of the destination register. <a id="cite-note-38" href="#cite-ref-38">[38]</a>

## ARM

[ARM](index.php?title=ARM&action=edit&redlink=1 "ARM (page does not exist)") has *CLZ* (Count Leading Zeros) instruction for 32-bit integers. ARM instruction is available in [ARMv5](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ddi0100i/index.html) and above, [32-bit Thumb instruction](https://en.wikipedia.org/wiki/ARM_architecture#Thumb) is available in [ARMv6T2](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ddi0100i/index.html) and [ARMv7](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ddi0100i/index.html) <a id="cite-note-39" href="#cite-ref-39">[39]</a> , the C-intrinsic is called *\_builtin_clz* <a id="cite-note-40" href="#cite-ref-40">[40]</a> <a id="cite-note-41" href="#cite-ref-41">[41]</a> <a id="cite-note-42" href="#cite-ref-42">[42]</a> .

## Engine Samples

- [BitScan in Amundsen](Amundsen#BitScan "Amundsen")
- [BitScan in Chess 0.5](Chess_0.5#BitScan "Chess 0.5")
- [BitScan in CookieCat](CookieCat#BitScan "CookieCat")
- [BitScan in Crafty](Crafty#BitScan "Crafty") (23.5)
- [BitScan in Gibbon](Gibbon#BitScan "Gibbon")
- [BitScan in Gk](Gk#BitScan "Gk")
- [BitScan in HeavyChess](HeavyChess#BitScan "HeavyChess")
- [BitScan in Kurt](Kurt#BitScan "Kurt")
- [BitScan in Murka](Murka#BitScan "Murka")
- [BitScan in Prophet](Prophet#BitScan "Prophet")
- [BitScan in RedQueen](RedQueen#BitScan "RedQueen")
- [BitScan in Spector](Spector#BitScan "Spector")

## See also

- [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
- [BITSCAN](Pablo_San_Segundo#BITSCAN "Pablo San Segundo"), a [C++ library](Cpp#Libraries "Cpp") for bitstrings by [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo")
- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Java-Bitscan](Java-Bitscan "Java-Bitscan")
- [Population Count](Population_Count "Population Count")

## Publications

- [Alan Turing](Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/%7Erst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), 9.4 The position of the most significant digit » [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1")
- [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop") and [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*, [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf)
- [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo"), [Ramón Galán](Ram%C3%B3n_Gal%C3%A1n "Ramón Galán") (**2005**). *[Bitboards: A New Approach](http://www.actapress.com/Abstract.aspx?paperId=18953)*. [AIA 2005](http://www.informatik.uni-trier.de/%7Eley/db/conf/aia/aia2005.html#SegundoG05)
- [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz), p. 10
- [Andreas Stiller](http://de.linkedin.com/pub/andreas-stiller/a/381/aa9) (**2013**). *[Spezialkommando - Bits setzen, abfragen, scannen und mehr](http://www.heise.de/ct/inhalt/2013/07/186/)*. [c't Magazin für Computertechnik](http://www.heise.de/ct/) 7/2013, p. 186 (German)

## Forum Posts

## 1996 ...

- [Bitboards: speeding up FirstOne](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/bcb03df7630d6274) by Laurent Desnogues, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 10, 1996 » [Othello](Othello "Othello")
- [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d5dbf08c66e83517#) by [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 6, 1996
- [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/9658009e315021fe#) by [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 7, 1996
- [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/871851f83e2c429f#) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 2, 1996
- [Question to Bob: Crafty , Alpha and FindBit()](https://www.stmintz.com/ccc/index.php?id=20057) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 05, 1998 » [Crafty](Crafty "Crafty"), [DEC Alpha](DEC_Alpha "DEC Alpha")
- [To Nalimov and other programmers about BSF/BSR in VC](https://www.stmintz.com/ccc/index.php?id=39619) by [Dezhi Zhao](index.php?title=Dezhi_Zhao&action=edit&redlink=1 "Dezhi Zhao (page does not exist)"), [CCC](CCC "CCC"), January 16, 1999

## 2000 ...

- [Re: TASM 5.0 versus BSF](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/37efb792689be6b8) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), March 28, 2000
- [Will the Itanium have a BSF or BSR instruction?](https://www.stmintz.com/ccc/index.php?id=124638) by Larry Griffiths, [CCC](CCC "CCC"), August 15, 2000

[Re: Will the Itanium have a BSF or BSR instruction?](https://www.stmintz.com/ccc/index.php?id=124712) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 16, 2000

- [Binary question](https://www.stmintz.com/ccc/index.php?id=134077) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), October 19, 2000
- [Bitboards and Piece Lists](https://www.stmintz.com/ccc/index.php?id=175203) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 14, 2001
- [FirstBit() in assembler](https://www.stmintz.com/ccc/index.php?id=207080) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 13, 2002
- [Reply from Intel about BSF/BSR](https://www.stmintz.com/ccc/index.php?id=211203) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 31, 2002
- ["Using de Bruijn Sequences to Index a 1 in a Computer Word"](https://www.stmintz.com/ccc/index.php?id=212586) by Oliver Roese, [CCC](CCC "CCC"), February 08, 2002
- [Extracting bits from a BitBoard...](https://www.stmintz.com/ccc/index.php?id=265543) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), November 17, 2002
- [Another hacky method for bitboard bit extraction](https://www.stmintz.com/ccc/index.php?id=265635) by [Walter Faxon](Walter_Faxon "Walter Faxon"), [CCC](CCC "CCC"), November 17, 2002
- [Modulo verus BitScan and MMX-PopCount](https://www.stmintz.com/ccc/index.php?id=268065) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), November 29, 2002
- [Fast 3DNow! BitScan](https://www.stmintz.com/ccc/index.php?id=268305) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), December 01, 2002
- [Bitscan Conclusions](https://www.stmintz.com/ccc/index.php?id=275160) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [CCC](CCC "CCC"), January 05, 2003
- [Bitscan](https://www.stmintz.com/ccc/index.php?id=283655) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [CCC](CCC "CCC"), February 11, 2003
- [FirstOne for Linux](https://www.stmintz.com/ccc/index.php?id=291062) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), March 29, 2003
- [Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/fPpKBKNi848J) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 26, 2003

[Re: Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/230qffQJYvQJ) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 29, 2003

- [Re: De Bruijn Sequence Generator](https://www.stmintz.com/ccc/index.php?id=339225) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), December 30, 2003 » [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator")
- [Determining location of LSB/MSB](https://www.stmintz.com/ccc/index.php?id=348097) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), February 09, 2004
- [Nalimov: bsf/bsr intrinsics implementation still not optimal](https://www.stmintz.com/ccc/index.php?id=388668) by [Dezhi Zhao](index.php?title=Dezhi_Zhao&action=edit&redlink=1 "Dezhi Zhao (page does not exist)"), [CCC](CCC "CCC"), September 22, 2004

## [Re: Nalimov: bsf/bsr intrinsics implementation still not optimal](https://www.stmintz.com/ccc/index.php?id=388787) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), September 23, 2004 2005 ...

- [A data point for PowerPC bitboard program authors](https://www.stmintz.com/ccc/index.php?id=425020) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 09, 2005 » [PowerPC](PowerPC "PowerPC")
- [Best BitBoard LSB funktion?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3141) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2005
- [Fastest bitboard compress routine when you can't use ASM](http://www.talkchess.com/forum/viewtopic.php?t=14151) by mambofish, [CCC](CCC "CCC"), May 31, 2007
- [Bit twiddling question, part 2: arbitrary bitscan order](http://talkchess.com/forum/viewtopic.php?t=29333) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 11, 2009
- [32 bit versions for bitscan64](http://talkchess.com/forum/viewtopic.php?t=29482) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), August 21, 2009
- [64-bit intrinsic performance](http://www.talkchess.com/forum/viewtopic.php?t=30342) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), October 27, 2009
- [Bit Scan (equivalent to ASM instructions bsr and bsf)](http://www.talkchess.com/forum/viewtopic.php?t=31228) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), December 24, 2009

## 2010 ...

- [bitScanReverse32](http://talkchess.com/forum/viewtopic.php?t=32046) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), January 25, 2010
- [Introduction and (hopefully) contribution - bitboard methods](http://www.talkchess.com/forum/viewtopic.php?t=39268) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), June 03, 2011 » [Population Count](Population_Count "Population Count")
- [First One](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=43825) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), May 24, 2012
- [Leading Zero Count Question](http://www.talkchess.com/forum/viewtopic.php?t=45188) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), September 16, 2012
- [Optimizing bitboards for ARM](http://www.talkchess.com/forum/viewtopic.php?t=46040) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), November 17, 2012
- [Symmetric move generation using bitboards](http://www.talkchess.com/forum/viewtopic.php?t=54704) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), December 20, 2014
- [Stockfish 32-bit and hardware instructions on MSVC++](http://www.talkchess.com/forum/viewtopic.php?t=54798) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), December 30, 2014 » [Stockfish](Stockfish "Stockfish"), BitScan, [Population Count](Population_Count "Population Count")

## 2015 ...

- [Fun with De Bruijn](http://www.talkchess.com/forum/viewtopic.php?t=57400) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), August 27, 2015
- [Re: Linux Version of Maverick 1.5](http://www.talkchess.com/forum/viewtopic.php?t=58230&start=3) by [Michael Dvorkin](Michael_Dvorkin "Michael Dvorkin"), [CCC](CCC "CCC"), November 12, 2015 » [OS X](Mac_OS "Mac OS"), [Maverick](Maverick "Maverick")
- [syzygy users (and Ronald)](http://www.talkchess.com/forum/viewtopic.php?t=61559) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 29, 2016 » [Population Count](Population_Count "Population Count")
- [CPW bitscan with reset could someone explain this line?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70202) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 14, 2019

## 2020 ...

- [Looking for intrinsic "least significant bit" on Visual Studio](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74989) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 03, 2020 » [Trailing Zero Count](BitScan#TrailingZeroCount "BitScan")
- [C++20 standard bit operations](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75818) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 15, 2020 » [General Setwise Operations](General_Setwise_Operations "General Setwise Operations"), [Population Count](Population_Count "Population Count"), [C++](Cpp "Cpp")
- [Optimizing Matt Taylor's Folding trick](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79739) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), April 21, 2022

## External Links

- [Find first set from Wikipedia](https://en.wikipedia.org/wiki/Find_first_set)
- [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC) by [Hank Dietz](Hank_Dietz "Hank Dietz")
- [Bit Twiddling Hacks](http://graphics.stanford.edu/%7Eseander/bithacks.html) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
- [An Efficient Bit-Reversal Sorting Algorithm for the Fast Fourier Transform](http://caladan.nanosoft.ca/c4/software/bitsort.php) by [Jennifer Elaan](http://caladan.nanosoft.ca/index.php), January 16, 2005
- [Efficient bit scan mechanism - United States Patent 6172623](http://www.freepatentsonline.com/6172623.html) from [FreePatentsOnline.com](http://www.freepatentsonline.com/)
- [Frank Zappa](Category:Frank_Zappa "Category:Frank Zappa") & [the Mothers](https://en.wikipedia.org/wiki/The_Mothers_of_Invention) - [King Kong](https://en.wikipedia.org/wiki/King_Kong) BBC Studio Recording 1968, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/gallery-back.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chip Architect: Detailed Architecture of AMD's Opteron - 1.3 A third class of Instructions](http://www.chip-architect.com/news/2003_09_21_Detailed_Architecture_of_AMDs_64bit_Core.html#1.3) by [Hans de Vries](http://www.chip-architect.com/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Looking for intrinsic "least significant bit" on Visual Studio](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74989) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 03, 2020
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz), p 10
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop") and [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *Using de Bruijn Sequences to Index a 1 in a Computer Word*, [pdf](http://supertech.csail.mit.edu/papers/debruijn.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> ["Using de Bruijn Sequences to Index a 1 in a Computer Word"](https://www.stmintz.com/ccc/index.php?id=212586) discussion in [CCC](CCC "CCC"), February 08, 2002
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [N. G. de Bruijn](Nicolaas_de_Bruijn "Nicolaas de Bruijn") (**1975**). *Acknowledgement of priority to C. Flye Sainte-Marie on the counting of circular arrangements of 2n zeros and ones that show each n-letter word exactly once*. Technical Report, Technische Hogeschool Eindhoven, available as [pdf reprint](http://alexandria.tue.nl/repository/books/252901.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/fPpKBKNi848J) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 26, 2003
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/230qffQJYvQJ) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 29, 2003
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Another hacky method for bitboard bit extraction](https://www.stmintz.com/ccc/index.php?id=265635) by [Walter Faxon](Walter_Faxon "Walter Faxon"), [CCC](CCC "CCC"), November 17, 2002
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [bitboard 2^i mod 67 is unique](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d5dbf08c66e83517#) by [Stefan Plenkner](Stefan_Plenkner "Stefan Plenkner"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 6, 1996
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Pablo San Segundo](Pablo_San_Segundo "Pablo San Segundo"), [Ramón Galán](Ram%C3%B3n_Gal%C3%A1n "Ramón Galán") (**2005**). *[Bitboards: A New Approach](http://www.actapress.com/Abstract.aspx?paperId=18953)*. [AIA 2005](http://www.informatik.uni-trier.de/%7Eley/db/conf/aia/aia2005.html#SegundoG05)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Best BitBoard LSB funktion?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3141) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2005
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Re: Will the Itanium have a BSF or BSR instruction?](https://www.stmintz.com/ccc/index.php?id=124712) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 16, 2000
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [ms1bTable array in Eugene Nalimovs bitScanReverse](http://www.talkchess.com/forum/viewtopic.php?t=38777) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), April 17, 2011
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [just another reverse bitscan](https://www.stmintz.com/ccc/index.php?id=472455) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), December 22, 2005
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [final version - homage to FZ](https://www.stmintz.com/ccc/index.php?id=472762) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), December 23, 2005
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [EuroPython 2012: Florence, July 2–8 | Mark Dickinson](https://ep2012.europython.eu/conference/p/mark-dickinson)
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Find the log base 2 of an N-bit integer in O(lg(N)) operations with multiply and lookup](http://graphics.stanford.edu/~seander/bithacks.html#IntegerLogDeBruijn) from [Bit Twiddling Hacks](http://graphics.stanford.edu/%7Eseander/bithacks.html) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [68020 Bit Field Instructions](http://www-scm.tees.ac.uk/users/a.clements/BF/BF.htm)
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [SSE4a from Wikipedia](https://en.wikipedia.org/wiki/SSE4#SSE4a)
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [\_\_lzcnt16, \_\_lzcnt, \_\_lzcnt64](http://msdn.microsoft.com/en-us/library/bb384809.aspx) Visual C++ Language Reference
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Bitscan](https://www.stmintz.com/ccc/index.php?id=283655) by [Matt Taylor](Matt_Taylor "Matt Taylor"), [CCC](CCC "CCC"), February 11, 2003
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> [CPW bitscan with reset could someone explain this line?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70202) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 14, 2019
1. <a id="cite-ref-25" href="#cite-note-25">↑</a> [\_BitScanForward, \_BitScanForward64](https://docs.microsoft.com/en-us/cpp/intrinsics/bitscanforward-bitscanforward64) Visual C++ Language Reference
1. <a id="cite-ref-26" href="#cite-note-26">↑</a> [\_BitScanReverse, \_BitScanReverse64](https://docs.microsoft.com/en-us/cpp/intrinsics/bitscanreverse-bitscanreverse64) Visual C++ Language Reference
1. <a id="cite-ref-27" href="#cite-note-27">↑</a> [\_\_lzcnt16, \_\_lzcnt, \_\_lzcnt64](https://msdn.microsoft.com/en-us/library/bb384809.aspx) Visual C++ Language Reference
1. <a id="cite-ref-28" href="#cite-note-28">↑</a> [Section 3: library functions - Linux man pages](http://linux.die.net/man/3/)
1. <a id="cite-ref-29" href="#cite-note-29">↑</a> [ffsll(3): find first bit set in word - Linux man page](http://linux.die.net/man/3/ffsll)
1. <a id="cite-ref-30" href="#cite-note-30">↑</a> [Other Builtins - Using the GNU Compiler Collection (GCC)](http://gcc.gnu.org/onlinedocs/gcc-4.4.5/gcc/Other-Builtins.html#Other-Builtins)
1. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Re: Nalimov: bsf/bsr intrinsics implementation still not optimal](https://www.stmintz.com/ccc/index.php?id=388787) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), September 23, 2004
1. <a id="cite-ref-32" href="#cite-note-32">↑</a> [Matters Computational - ideas, algorithms, source code](http://www.jjj.de/fxt/fxtbook.pdf) (pdf) Ideas and Source Code by [Jörg Arndt](Mathematician#Arndt "Mathematician")
1. <a id="cite-ref-33" href="#cite-note-33">↑</a> [Instruction tables, Lists of instruction latencies, throughputs and microoperation breakdowns for Intel and AMD CPU's](http://www.agner.org/optimize/instruction_tables.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
1. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Software Optimization Guide for AMD64 Processors](http://support.amd.com/us/Processor_TechDocs/25112.PDF)
1. <a id="cite-ref-35" href="#cite-note-35">↑</a> [Software Optimization Guide for AMD Family 10h and 12h Processors](http://support.amd.com/us/Processor_TechDocs/40546.pdf)
1. <a id="cite-ref-36" href="#cite-note-36">↑</a> [Intel 64 and IA32 Architectures Optimization Reference Manual](http://www.intel.com/design/processor/manuals/248966.pdf)
1. <a id="cite-ref-37" href="#cite-note-37">↑</a> [Intel® 64 and IA-32 Architectures Software Developer’s Manual Volume 2A: Instruction Set Reference, A-M](http://www.intel.com/Assets/PDF/manual/253666.pdf) (pdf) BSF—Bit Scan Forward 3-87
1. <a id="cite-ref-38" href="#cite-note-38">↑</a> [AMD64 Architecture Programmer’s Manual Volume 3: General-Purpose and System Instructions](http://support.amd.com/us/Processor_TechDocs/24594_APM_v3.pdf) (pdf) Bit Scan Forward pg. 111
1. <a id="cite-ref-39" href="#cite-note-39">↑</a> [ARM Information Center > General data processing instructions > CLZ](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0379a/Cihjgjed.html)
1. <a id="cite-ref-40" href="#cite-note-40">↑</a> [ARM Information Center > Instruction intrinsics > \_\_builtin_clz](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0376a/CJAEJGJD.html)
1. <a id="cite-ref-41" href="#cite-note-41">↑</a> [Other Builtins - Using the GNU Compiler Collection (GCC)](http://developer.apple.com/mac/library/documentation/DeveloperTools/gcc-4.0.1/gcc/Other-Builtins.html)
1. <a id="cite-ref-42" href="#cite-note-42">↑</a> [Bit Scan (equivalent to ASM instructions bsr and bsf)](http://www.talkchess.com/forum/viewtopic.php?t=31228) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), December 24, 2009

**[Up one Level](Bitboards "Bitboards")**

