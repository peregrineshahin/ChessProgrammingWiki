---
title: Looking for Magics
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* [Magic Bitboards](Magic_Bitboards "Magic Bitboards") \* Looking for Magics**


[Magic Bitboards](Magic_Bitboards "Magic Bitboards") is probably the fastest approach to generate [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") on recent architectures with fast 64-bit multiplication. It performs a mask/mul/shift->lookup to gain all the attacked squares of a bishop or rook.



## Feeding in Randoms


[Tord Romstad's](Tord_Romstad "Tord Romstad") proposal to find magics <a id="cite-note-2" href="#cite-ref-2">[2]</a> :





|  |
| --- |
|  Just trying out [random numbers](Pseudorandom_Number_Generator "Pseudorandom Number Generator") with a low number of nonzero bits until you find a number which works is by far the fastest and easiest way to generate the magic numbers, in my experience. On my Core Duo 2.8 GHz, it takes less than a second to find magic numbers for rooks and bishops for all squares (and I have made no attempt to optimize the code, it should be easy to make it much faster). Here is the source code:

```C++

##include <stdio.h>
##include <stdlib.h>

##define USE_32_BIT_MULTIPLICATIONS

typedef unsigned long long uint64;

uint64 random_uint64() {
  uint64 u1, u2, u3, u4;
  u1 = (uint64)(random()) & 0xFFFF; u2 = (uint64)(random()) & 0xFFFF;
  u3 = (uint64)(random()) & 0xFFFF; u4 = (uint64)(random()) & 0xFFFF;
  return u1 | (u2 << 16) | (u3 << 32) | (u4 << 48);
}

uint64 random_uint64_fewbits() {
  return random_uint64() & random_uint64() & random_uint64();
}

int count_1s(uint64 b) {
  int r;
  for(r = 0; b; r++, b &= b - 1);
  return r;
}

const int BitTable[64] = {
  63, 30, 3, 32, 25, 41, 22, 33, 15, 50, 42, 13, 11, 53, 19, 34, 61, 29, 2,
  51, 21, 43, 45, 10, 18, 47, 1, 54, 9, 57, 0, 35, 62, 31, 40, 4, 49, 5, 52,
  26, 60, 6, 23, 44, 46, 27, 56, 16, 7, 39, 48, 24, 59, 14, 12, 55, 38, 28,
  58, 20, 37, 17, 36, 8
};

int pop_1st_bit(uint64 *bb) {
  uint64 b = *bb ^ (*bb - 1);
  unsigned int fold = (unsigned) ((b & 0xffffffff) ^ (b >> 32));
  *bb &= (*bb - 1);
  return BitTable[(fold * 0x783a9b23) >> 26];
}

uint64 index_to_uint64(int index, int bits, uint64 m) {
  int i, j;
  uint64 result = 0ULL;
  for(i = 0; i < bits; i++) {
    j = pop_1st_bit(&m);
    if(index & (1 << i)) result |= (1ULL << j);
  }
  return result;
}

uint64 rmask(int sq) {
  uint64 result = 0ULL;
  int rk = sq/8, fl = sq%8, r, f;
  for(r = rk+1; r <= 6; r++) result |= (1ULL << (fl + r*8));
  for(r = rk-1; r >= 1; r--) result |= (1ULL << (fl + r*8));
  for(f = fl+1; f <= 6; f++) result |= (1ULL << (f + rk*8));
  for(f = fl-1; f >= 1; f--) result |= (1ULL << (f + rk*8));
  return result;
}

uint64 bmask(int sq) {
  uint64 result = 0ULL;
  int rk = sq/8, fl = sq%8, r, f;
  for(r=rk+1, f=fl+1; r<=6 && f<=6; r++, f++) result |= (1ULL << (f + r*8));
  for(r=rk+1, f=fl-1; r<=6 && f>=1; r++, f--) result |= (1ULL << (f + r*8));
  for(r=rk-1, f=fl+1; r>=1 && f<=6; r--, f++) result |= (1ULL << (f + r*8));
  for(r=rk-1, f=fl-1; r>=1 && f>=1; r--, f--) result |= (1ULL << (f + r*8));
  return result;
}

uint64 ratt(int sq, uint64 block) {
  uint64 result = 0ULL;
  int rk = sq/8, fl = sq%8, r, f;
  for(r = rk+1; r <= 7; r++) {
    result |= (1ULL << (fl + r*8));
    if(block & (1ULL << (fl + r*8))) break;
  }
  for(r = rk-1; r >= 0; r--) {
    result |= (1ULL << (fl + r*8));
    if(block & (1ULL << (fl + r*8))) break;
  }
  for(f = fl+1; f <= 7; f++) {
    result |= (1ULL << (f + rk*8));
    if(block & (1ULL << (f + rk*8))) break;
  }
  for(f = fl-1; f >= 0; f--) {
    result |= (1ULL << (f + rk*8));
    if(block & (1ULL << (f + rk*8))) break;
  }
  return result;
}

uint64 batt(int sq, uint64 block) {
  uint64 result = 0ULL;
  int rk = sq/8, fl = sq%8, r, f;
  for(r = rk+1, f = fl+1; r <= 7 && f <= 7; r++, f++) {
    result |= (1ULL << (f + r*8));
    if(block & (1ULL << (f + r * 8))) break;
  }
  for(r = rk+1, f = fl-1; r <= 7 && f >= 0; r++, f--) {
    result |= (1ULL << (f + r*8));
    if(block & (1ULL << (f + r * 8))) break;
  }
  for(r = rk-1, f = fl+1; r >= 0 && f <= 7; r--, f++) {
    result |= (1ULL << (f + r*8));
    if(block & (1ULL << (f + r * 8))) break;
  }
  for(r = rk-1, f = fl-1; r >= 0 && f >= 0; r--, f--) {
    result |= (1ULL << (f + r*8));
    if(block & (1ULL << (f + r * 8))) break;
  }
  return result;
}


int transform(uint64 b, uint64 magic, int bits) {
##if defined(USE_32_BIT_MULTIPLICATIONS)
  return
    (unsigned)((int)b*(int)magic ^ (int)(b>>32)*(int)(magic>>32)) >> (32-bits);
##else
  return (int)((b * magic) >> (64 - bits));
##endif
}

uint64 find_magic(int sq, int m, int bishop) {
  uint64 mask, b[4096], a[4096], used[4096], magic;
  int i, j, k, n, fail;

  mask = bishop? bmask(sq) : rmask(sq);
  n = count_1s(mask);

  for(i = 0; i < (1 << n); i++) {
    b[i] = index_to_uint64(i, n, mask);
    a[i] = bishop? batt(sq, b[i]) : ratt(sq, b[i]);
  }
  for(k = 0; k < 100000000; k++) {
    magic = random_uint64_fewbits();
    if(count_1s((mask * magic) & 0xFF00000000000000ULL) < 6) continue;
    for(i = 0; i < 4096; i++) used[i] = 0ULL;
    for(i = 0, fail = 0; !fail && i < (1 << n); i++) {
      j = transform(b[i], magic, m);
      if(used[j] == 0ULL) used[j] = a[i];
      else if(used[j] != a[i]) fail = 1;
    }
    if(!fail) return magic;
  }
  printf("***Failed***\n");
  return 0ULL;
}

int RBits[64] = {
  12, 11, 11, 11, 11, 11, 11, 12,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  11, 10, 10, 10, 10, 10, 10, 11,
  12, 11, 11, 11, 11, 11, 11, 12
};

int BBits[64] = {
  6, 5, 5, 5, 5, 5, 5, 6,
  5, 5, 5, 5, 5, 5, 5, 5,
  5, 5, 7, 7, 7, 7, 5, 5,
  5, 5, 7, 9, 9, 7, 5, 5,
  5, 5, 7, 9, 9, 7, 5, 5,
  5, 5, 7, 7, 7, 7, 5, 5,
  5, 5, 5, 5, 5, 5, 5, 5,
  6, 5, 5, 5, 5, 5, 5, 6
};

int main() {
  int square;

  printf("const uint64 RMagic[64] = {\n");
  for(square = 0; square < 64; square++)
    printf("  0x%llxULL,\n", find_magic(square, RBits[square], 0));
  printf("};\n\n");

  printf("const uint64 BMagic[64] = {\n");
  for(square = 0; square < 64; square++)
    printf("  0x%llxULL,\n", find_magic(square, BBits[square], 1));
  printf("};\n\n");

  return 0;
}

```
 |


## Fixed Shift Magics


Another application is Looking for overlapping Magics for a [fixed shift approach](Magic_Bitboards#FixedShiftFancy "Magic Bitboards"), as recently proposed by [Volker Annuss](Volker_Annuss "Volker Annuss") <a id="cite-note-3" href="#cite-ref-3">[3]</a> .



## See also


* [Best Magics so far](Best_Magics_so_far "Best Magics so far")
* [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")


## Forum Posts


* [Magic Move Generation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=175544&t=19699) by Colin, [CCC](CCC "CCC"), February 18, 2008
* [Magics revisited](http://www.talkchess.com/forum/viewtopic.php?t=25810) by [Richard Pijl](Richard_Pijl "Richard Pijl"), [CCC](CCC "CCC"), January 04, 2009
* [magic search](http://www.talkchess.com/forum/viewtopic.php?t=33346) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 19, 2010
* [Build magics on the fly](http://www.talkchess.com/forum/viewtopic.php?t=39298) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 07, 2011
* [Super Fast 'Looking for magics' 1.0](http://www.talkchess.com/forum/viewtopic.php?t=54138) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), October 25, 2014
* [question about magic keys generation time](http://www.talkchess.com/forum/viewtopic.php?t=55712) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 19, 2015
* [Magic number generation taking 17 seconds or more](http://www.talkchess.com/forum/viewtopic.php?t=58424) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), November 29, 2015
* [Re: Some questions from a beginner](http://www.talkchess.com/forum/viewtopic.php?t=59691&start=9) by Tim Hagen, [CCC](CCC "CCC"), April 04, 2016


 [Re: Some questions from a beginner](http://www.talkchess.com/forum/viewtopic.php?t=59691&start=18) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), April 05, 2016
 [Re: Some questions from a beginner](http://www.talkchess.com/forum/viewtopic.php?t=59691&start=22) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), April 06, 2016
* [Looking for dense magics](http://www.talkchess.com/forum/viewtopic.php?t=64578) by Lucas Braesch, [CCC](CCC "CCC"), July 11, 2017
* [Disproving the existence of some magics](http://www.talkchess.com/forum/viewtopic.php?t=65187) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), September 16, 2017
* [No bishop magics with fixed shift 8](http://www.talkchess.com/forum/viewtopic.php?t=67051) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), April 09, 2018


## External Links


* [Chess Programming | Generating Magic Multipliers](http://www.chessprogramming.net/generating-magic-multipliers/) by [Steve Maughan](Steve_Maughan "Steve Maughan")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Disproving the existence of some magics](http://www.talkchess.com/forum/viewtopic.php?t=65187) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), September 16, 2017
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Magic Move Generation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=175834&t=19699) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 20, 2008
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Fixed shift magics with 800KB lookup table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51162) by [Volker Annuss](Volker_Annuss "Volker Annuss"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September, 05, 2010

**[Up one level](Magic_Bitboards "Magic Bitboards")**







 
