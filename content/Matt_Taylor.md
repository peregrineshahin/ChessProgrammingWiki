---
title: Matt Taylor
---
**[Home](Home "Home") \* [People](People "People") \* Matt Taylor**


**Matt Taylor** was involved in forum discussions on low level optimization and [x86](X86 "X86") [assembly language](Assembly "Assembly") issues. 
Beside other things Matt was busy to optimize a minimal perfect hashing scheme for [bitscan](BitScan "BitScan") purposes. 






Based on ideas of [Walter Faxon](Walter_Faxon "Walter Faxon") and [De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan"), Matt came up with a [genius folding trick](BitScan#MattTaylorsFoldingtrick "BitScan") as a quintessence <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++
For 64-bits, I do things a little differently simply because a 64-bit multiply is slow. I start out with x ^= (x - 1) just like normal which generates a key equal to 2^n - 1 (where n is the index of the LSB, 1 is index 0). Now fold the 64-bit key into 32-bits by xoring the high 32-bits with the low 32-bits.

```



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

## Forum Posts


* [Bitscan Conclusions](https://www.stmintz.com/ccc/index.php?id=275160) by Matt Taylor, [CCC](CCC "CCC"), January 05, 2003
* [Cleverness, Please!](https://www.stmintz.com/ccc/index.php?id=278848) by Matt Taylor, [CCC](CCC "CCC"), January 22, 2003
* [Bitscan](https://www.stmintz.com/ccc/index.php?id=283655) by Matt Taylor, [CCC](CCC "CCC"), February 11, 2003
* [Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/fPpKBKNi848J) by Matt Taylor, [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 26, 2003


 [Re: Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/230qffQJYvQJ) by Matt Taylor, [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 29, 2003
* [Re: Static memory allocation](https://groups.google.com/d/msg/comp.lang.asm.x86/Ge1Uzd0WckM/zR6WLJRixiYJ) by Matt Taylor, [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), July 03, 2004


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/fPpKBKNi848J) by Matt Taylor, [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 26, 2003
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Bit magic](https://groups.google.com/d/msg/comp.lang.asm.x86/3pVGzQGb1ys/230qffQJYvQJ) by Matt Taylor, [comp.lang.asm.x86](https://groups.google.com/forum/#!forum/comp.lang.asm.x86), June 29, 2003

**[Up one level](People "People")**







 
