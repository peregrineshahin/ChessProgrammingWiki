---
title: Population CountTooSlow
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Population Count**



[ Visualization of [Hamming distance](Population_Count#HammingDistance "Population Count") [[1]](#cite_note-1)
**Population count**,  

an operation to determine the [cardinality](https://en.wikipedia.org/wiki/Cardinality) of a bitboard, also called [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight) or sideways sum [[2]](#cite_note-2). How many one bits exists in a 64-bit computer word? In computer chess, population count is used to [evaluate](Evaluation "Evaluation") the [mobility](Mobility "Mobility") of pieces from their [attack sets](Attacks "Attacks"), as [already applied](CDC_Cyber#Mobility "CDC Cyber") in [Chess 4.6](Chess_(Program) "Chess (Program)") on the [CDC 6600](CDC_6600 "CDC 6600") and [CDC Cyber](CDC_Cyber "CDC Cyber").


Recent [x86-64](X86-64 "X86-64") processors (since [AMD](AMD "AMD") [K10](https://en.wikipedia.org/wiki/AMD_K10) with [SSE4a](SSE4#SSE4a "SSE4"), [Intel](Intel "Intel") [Nehalem](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) with [SSE4.2](SSE4#SSE4.2 "SSE4")) provide a [64-bit popcount instruction](X86-64#gpinstructions "X86-64") [[3]](#cite_note-3), available via [C++](Cpp "Cpp") compiler intrinsic [[4]](#cite_note-4) [[5]](#cite_note-5) or [inline assembly](Assembly#InlineAssembly "Assembly") [[6]](#cite_note-6). Despite different Intrinsic prototypes (\_mm\_popcnt\_u64 vs. popcnt64), Intel and AMD popcnt instructions are binary compatible, have same encoding (F3 [REX] 0F B8 /r), and both require bit 23 set in RCX of the [CPUID](https://en.wikipedia.org/wiki/CPUID) function 0000\_0001h. Code samples are in [C](C "C") / [C++](Cpp "Cpp"), *see [Defining Bitboards](Bitboards#DefiningBitboards "Bitboards")*



### Contents


* [1 Recurrence Relation](#Recurrence_Relation)
* [2 Empty or Single?](#Empty_or_Single.3F)
	+ [2.1 Empty Bitboards](#Empty_Bitboards)
	+ [2.2 Single Populated Bitboards](#Single_Populated_Bitboards)
* [3 Loop-Approaches](#Loop-Approaches)
	+ [3.1 Too Slow](#Too_Slow)
	+ [3.2 Brian Kernighan's way](#Brian_Kernighan.27s_way)
* [4 Lookup](#Lookup)
* [5 SWAR-Popcount](#SWAR-Popcount)
	+ [5.1 Counting Duo-Bits](#Counting_Duo-Bits)
	+ [5.2 Counting Nibble-Bits](#Counting_Nibble-Bits)
	+ [5.3 Byte-Counts](#Byte-Counts)
	+ [5.4 Adding the Byte-Counts](#Adding_the_Byte-Counts)
		- [5.4.1 Parallel Prefix Adds](#Parallel_Prefix_Adds)
		- [5.4.2 Multiplication](#Multiplication)
		- [5.4.3 Casting out](#Casting_out)
	+ [5.5 The PopCount routine](#The_PopCount_routine)
		- [5.5.1 The Constants](#The_Constants)
		- [5.5.2 popCount](#popCount)
	+ [5.6 HAKMEM 169](#HAKMEM_169)
* [6 Miscellaneous](#Miscellaneous)
	+ [6.1 Cardinality of Multiple Sets](#Cardinality_of_Multiple_Sets)
		- [6.1.1 Odd and Major 7-15](#Odd_and_Major_7-15)
		- [6.1.2 Odd and Major Digit Counts](#Odd_and_Major_Digit_Counts)
	+ [6.2 Popcount as log2 of LS1B](#Popcount_as_log2_of_LS1B)
	+ [6.3 Hamming Distance](#Hamming_Distance)
	+ [6.4 Weighted PopCount](#Weighted_PopCount)
	+ [6.5 Pre-calculated Mobility](#Pre-calculated_Mobility)
	+ [6.6 Piece Attacks Count](#Piece_Attacks_Count)
* [7 Popcount in Hardware](#Popcount_in_Hardware)
* [8 See also](#See_also)
* [9 Publications](#Publications)
	+ [9.1 1949 ...](#1949_...)
	+ [9.2 2000 ...](#2000_...)
	+ [9.3 2010 ...](#2010_...)
* [10 Postings](#Postings)
	+ [10.1 1998 ...](#1998_...)
	+ [10.2 2000 ...](#2000_..._2)
	+ [10.3 2005 ...](#2005_...)
	+ [10.4 2010 ...](#2010_..._2)
	+ [10.5 2015 ...](#2015_...)
	+ [10.6 2020 ...](#2020_...)
* [11 External Links](#External_Links)
* [12 References](#References)






The [recursive](Recursion "Recursion") [recurrence relation](https://en.wikipedia.org/wiki/Recurrence_relation) of population counts can be transformed to iteration as well, but lacks an arithmetical sum-formula:




```
popcnt(0) = 0
popcnt(n) = popcnt(n ÷ 2) + (n mod 2)

```

However, it is helpful to initialize a [lookup table](Population_Count#Lookup "Population Count"), i.e. for bytes: 




```

unsigned char popCountOfByte256[];

void initpopCountOfByte256()
{
   popCountOfByte256[0] = 0;
   for (int i = 1; i < 256; i++)
      popCountOfByte256[i] = popCountOfByte256[i / 2] + (i & 1);
}

```

## Empty or Single?


Often one has to deal with sparsely populated or even empty bitboards. To determine whether a bitboard is empty or a single populated power of two value, one may use simple boolean statements rather than a complete population count.






### Empty Bitboards


To test a bitboard is empty, one compares it with zero, or use the logical not operator:




```

if ( x == 0 ) -> bitboard is empty
if ( !x )     -> bitboard is empty

```

The inverse condition (not empty) is of course




```

if ( x != 0 ) -> bitboard is not empty
if ( x )      -> bitboard is not empty

```





### Single Populated Bitboards


If the bitboard is not empty, we can [extract](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") to look whether it is equal with the bitboard. Alternatively and faster, we can [reset the LS1B](General_Setwise_Operations#LS1BReset "General Setwise Operations") to look whether the bitboard becomes empty.




```

if ( x != 0 && (x & (x-1)) == 0 ) -> population count is one, power of two value

```

One can skip the leading x != 0 condition to test popcount <= 1:




```

if ( (x & (x-1)) == 0 ) -> population count is less or equal than one

```

Again the inverse relation tests, whether a bitboard has more than one bit set:




```

if ( x & (x-1) ) -> population count is greater than one

```

An alternative approach to determine single populated sets, aka power of two values is based on [Inclusive LS1B separation](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") divided by two equals the ones' decrement [[7]](#cite_note-7):




```

if ( ((x ^ (x-1)) >> 1) == (x-1) ) -> population count is one, power of two value

```

## Loop-Approaches






### Too Slow


Brute force adding all 64-bits




```

int popCount (U64 x) {
   int count = 0;
   for (int i = 0; i < 64; i++, x >>= 1)
      count += (int)x & 1;
   return count;
}

```

Of course, this is a slow algorithm, which might be improved by testing x not empty rather than i < 64. But unrolled in [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") manner it already reminds on [this one](Population_Count#SWARPopcount "Population Count").






### Brian Kernighan's way


Consecutively [reset LS1B](General_Setwise_Operations#LS1BReset "General Setwise Operations") in a loop body and counting loop cycles until the bitset becomes empty. [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) [[8]](#cite_note-8) mentioned the trick in his and [Ritchie's](https://en.wikipedia.org/wiki/Dennis_Ritchie) book [The C Programming\_Language](https://en.wikipedia.org/wiki/The_C_Programming_Language_%28book%29), 2nd Edition 1988, exercise 2-9. However, the method was first published in 1960 by [Peter Wegner](Mathematician#PWegner "Mathematician") [[9]](#cite_note-9), discovered independently by [Derrick Henry Lehmer](Mathematician#DHLehmer "Mathematician"), published in 1964 [[10]](#cite_note-10):




```

int popCount (U64 x) {
   int count = 0;
   while (x) {
       count++;
       x &= x - 1; // reset LS1B
   }
   return count;
}

```

Despite branches - this is still one of the fastest approaches for sparsely populated bitboards. Of course the more bits that are set, the longer it takes.






## Lookup


Of course we can not use the whole bitboard as index to a lookup table - since it's size would be 18,446,744,073,709,551,616 bytes! If it is about the population count of a byte, we can simply construct a table lookup with 256 elements. For a bitboard that takes eight byte lookups we can add together:




```

unsigned char popCountOfByte256[];

void initpopCountOfByte256()
{
   popCountOfByte256[0] = 0;
   for (int i = 1; i < 256; i++)
      popCountOfByte256[i] = popCountOfByte256[i / 2] + (i & 1);
}

int popCount (U64 x) {
   return popCountOfByte256[ x        & 0xff] +
          popCountOfByte256[(x >>  8) & 0xff] +
          popCountOfByte256[(x >> 16) & 0xff] +
          popCountOfByte256[(x >> 24) & 0xff] +
          popCountOfByte256[(x >> 32) & 0xff] +
          popCountOfByte256[(x >> 40) & 0xff] +
          popCountOfByte256[(x >> 48) & 0xff] +
          popCountOfByte256[ x >> 56];
}

```

Looks quite expensive - one may use four 16-bit word-lookups with a pre-calculated 64KByte table though, but that pollutes the memory caches quite a bit. One can also treat the bitboard as [array](Array "Array") of bytes or words in memory, since endian issues don't care here - that safes all the shifts and 'ands', but has to read byte for byte from memory.




```

int popCount (U64 x) {
   unsigned char * p = (unsigned char *) &x;
   return popCountOfByte256[p[0]] +
          popCountOfByte256[p[1]] +
          popCountOfByte256[p[2]] +
          popCountOfByte256[p[3]] +
          popCountOfByte256[p[4]] +
          popCountOfByte256[p[5]] +
          popCountOfByte256[p[6]] +
          popCountOfByte256[p[7]];
}

```





## SWAR-Popcount


The [divide and conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm) [SWAR-approach](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") deals with counting bits of duos, to aggregate the duo-counts to [nibbles](Nibble "Nibble") and [bytes](Byte "Byte") inside one 64-bit register in parallel, to finally sum all bytes together. According to [Donald Knuth](Donald_Knuth "Donald Knuth") [[11]](#cite_note-11), a parallel population count routine was already introduced in 1957 due to [Donald B. Gillies](Mathematician#DBGillies "Mathematician") and [Jeffrey C. P. Miller](https://en.wikipedia.org/wiki/J._C._P._Miller) in the first textbook on programming, second edition: *The Preparation of Programs for an Electronic Digital Computer*, by [Maurice Wilkes](Mathematician#MVWilkes "Mathematician"), [David Wheeler](Mathematician#DJWheeler "Mathematician") and [Stanley Gill](https://en.wikipedia.org/wiki/Stanley_Gill), pages 191–193 [[12]](#cite_note-12) [[13]](#cite_note-13). 



### Counting Duo-Bits


A bit-duo (two neighboring bits) can be interpreted with bit 0 = a, and bit 1 = b as




```
duo := 2b + a

```

The duo population is




```
popcnt(duo) := b + a

```

which can be archived by




```
(2b + a) - (2b + a) ÷ 2

```

or




```
(2b + a) - b

```

The bit-duo has up to four states with population count from zero to two as demonstrated in following table with binary digits:





|  x
 |  x div 2
 |  popcnt(x)
 |
| --- | --- | --- |
|  00
 |  00
 |  00
 |
|  01
 |  00
 |  01
 |
|  10
 |  01
 |  01
 |
|  11
 |  01
 |  10
 |


Only the lower bit is needed from x div 2 - and one don't has to worry about borrows from neighboring duos. SWAR-wise, one needs to clear all "even" bits of the div 2 subtrahend to perform a 64-bit subtraction of all 32 duos:




```

x = x - ((x >> 1) & 0x5555555555555555);

```

Note that the popcount-result of the bit-duos still takes two bits.



### Counting Nibble-Bits


The next step is to add the duo-counts to populations of four neighboring bits, the 16 nibble-counts, which may range from zero to four. SWAR-wise it is done by masking odd and even duo-counts to add them together:




```

 x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333);

```

Note that the popcount-result of the nibbles takes only three bits, since 100B is the maximum population (of the nibble 1111B).



### Byte-Counts


You already got the idea? Now it is about to get the byte-populations from two nibble-populations. Maximum byte-population of 1000B only takes four bits, so it is safe to mask all those four bits of the sum, rather than to mask the summands:




```

x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f;

```

### Adding the Byte-Counts


### Parallel Prefix Adds


We may continue with mask-less [parallel prefix](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") SWAR-adds for byte-counts, word-counts and finally double-word-counts, to mask the least significant 8 (or 7) bits for final result in the 0..64 range:




```

x += (x >>  8);
x += (x >> 16);
x += (x >> 32);
return x & 255;

```





### Multiplication


With todays fast 64-bit multiplication one can multiply the vector of 8-byte-counts with 0x0101010101010101 to get the final result in the most significant byte, which is then shifted right:




```

x = (x * 0x0101010101010101) >> 56;

```





### Casting out


Interestingly, there is another approach to add the bytes together. As demonstrated with decimal digits (base 10) and [Casting out nines](https://en.wikipedia.org/wiki/Casting_out_nines) [[14]](#cite_note-14), casting out by [modulo](General_Setwise_Operations#Modulo "General Setwise Operations") base minus one is equivalent to taking the [digit sum](https://en.wikipedia.org/wiki/Digit_sum), which might be applied here with low range 0..8 "base 256" digits:




```

x = x % 255;

```

However, since division and modulo are usually slow instructions and modulo by constant is likely replaced by reciprocal multiplication anyway by the compiler, the multiplication by 0x0101010101010101 aka the 2-[adic](https://en.wikipedia.org/wiki/P-adic_number) fraction -1/255 is the preferred method.



### The PopCount routine


### The Constants


Putting all together, the various SWAR-Masks and factors as defined by [Donald Knuth](Donald_Knuth "Donald Knuth") as 2-[adic](https://en.wikipedia.org/wiki/P-adic_number) fractions [[15]](#cite_note-15):




```

const U64 k1 = C64(0x5555555555555555); /*  -1/3   */
const U64 k2 = C64(0x3333333333333333); /*  -1/5   */
const U64 k4 = C64(0x0f0f0f0f0f0f0f0f); /*  -1/17  */
const U64 kf = C64(0x0101010101010101); /*  -1/255 */

```

represented as bitboards:




```

k1  -1/3            k2  -1/5            k4  -1/17           kf  -1/255              
0x5555555555555555  0x3333333333333333  0x0f0f0f0f0f0f0f0f  0x0101010101010101
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   
1 . 1 . 1 . 1 .     1 1 . . 1 1 . .     1 1 1 1 . . . .     1 . . . . . . .   

```

### popCount


This is how the complete routine looks in [C](C "C"):




```

int popCount (U64 x) {
    x =  x       - ((x >> 1)  & k1); /* put count of each 2 bits into those 2 bits */
    x = (x & k2) + ((x >> 2)  & k2); /* put count of each 4 bits into those 4 bits */
    x = (x       +  (x >> 4)) & k4 ; /* put count of each 8 bits into those 8 bits */
    x = (x * kf) >> 56; /* returns 8 most significant bits of x + (x<<8) + (x<<16) + (x<<24) + ...  */
    return (int) x;
}

```

**Advantage**: no branches, no memory lookups, constant runtime - independent from population
**Drawback**: dependency chain, not much parallel speedup


*For likely sparsely populated bitboards, the loop-wise [Brian Kernighan's way](Population_Count#BrianKernighansway "Population Count") might be the faster one.*




### HAKMEM 169


A similar technique was proposed by [Bill Gosper](Bill_Gosper "Bill Gosper") et al. from [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), as published 1972 in [Memo 239 (HAKMEM)](https://en.wikipedia.org/wiki/HAKMEM) [[16]](#cite_note-16) [[17]](#cite_note-17), to add bit-trio- rather than duo populations consecutively, and the 32 bit version relies on casting out 63. Note that the constants in the code below have [octal](https://en.wikipedia.org/wiki/Octal) (base-8) digits, originally written in [Assembly](Assembly#HAKMEM169 "Assembly") for the [PDP-6](PDP-6 "PDP-6") [[18]](#cite_note-18). An expanded 64-bit version, casting out 511 or 4095, is slightly less efficient than the binary SWAR version above.




```

int hakmem169_32(unsigned int x) {
   x = x  - ((x >> 1)  & 033333333333)
          - ((x >> 2)  & 011111111111);
   x = (x +  (x >> 3)) & 030707070707 ;
   return x % 63; /* casting out 63 */
} 

```

## Miscellaneous






### Cardinality of Multiple Sets


If we like to count [arrays](Array "Array") of sets, we can reduce 2^N-1 popcounts to N popcounts, by applying the odd-major-trick. For three sets to count we safe one, with five additional cheap instructions.




```

  odd   =  (x ^ y)  ^ z;
  major = ((x ^ y ) & z) | (x & y);

  popCount(x) + popCount(y) + popCount(z) == 2*popCount(major) + popCount(odd)

```

The combined popCount3 likely gains more parallel speedup, since there are two independent chains to calculate. Possible Application is to pass the union of both bishops (since usually bishops cover disjoint sets due to different square colors) plus the up to two knight move-target sets.




```

// return popCount(x) + popCount(y) + popCount(z)
int popCount3 (U64 x, U64 y, U64 z) {
    U64 maj = ((x ^ y ) & z) | (x & y);
    U64 odd = ((x ^ y ) ^ z);
    maj =  maj - ((maj >> 1) & k1 );
    odd =  odd - ((odd >> 1) & k1 );
    maj = (maj & k2) + ((maj >> 2) & k2);
    odd = (odd & k2) + ((odd >> 2) & k2);
    maj = (maj + (maj >> 4)) & k4;
    odd = (odd + (odd >> 4)) & k4;
    odd = ((maj + maj + odd) * kf ) >> 56;
    return (int) odd;
}

```

### Odd and Major 7-15


Of course - reducing seven popcount to three, or even 15 popcounts to four sounds even more promising.
For N = 2^n - 1 it takes N - n odd-major pairs. Thus one add-major pair - five instructions - per saved popCount.


That is 7 - 3 = 4 pairs:




```

one1,two1 := oddMaj(x1,x2,x3)
one2,two2 := oddMaj(x4,x5,x6)
ones,two3 := oddMaj(x7,one1,one2)
twos,four := oddMaj(two1,two2,two3)

```

Or 15 - 4 = 11 pairs:




```

one1,two1  := oddMaj(x1,x2,x3)
one2,two2  := oddMaj(x4,x5,x6)
one3,two3  := oddMaj(x7,x8,x9)
one4,two4  := oddMaj(x10,x11,x12)
one5,two5  := oddMaj(x13,x14,x15)
one6,two6  := oddMaj(one1,one2,one3)
ones,two7  := oddMaj(one4,one5,one6)
two8,four1 := oddMaj(two1,two2,two3)
two9,four2 := oddMaj(two4,two5,two6)
twos,four3 := oddMaj(two7,two8,two9)
four,eight := oddMaj(four1,four2,four3)

```





### Odd and Major Digit Counts


Odd-Major is probably also useful to determine digit count sets of attacks or other stuff:




```

U64 odd(U64 x, U64 y, U64 z) {return x^y^z;}
U64 maj(U64 x, U64 y, U64 z) {return ((x^y)&z)|(x&y);}

void attackCounts(U64 t[3], const U64 s[7]) {
   one1 = odd(s[0], s[1], s[2]);
   two1 = maj(s[0], s[1], s[2]);
   one2 = odd(s[3], s[4], s[5]);
   two2 = maj(s[3], s[4], s[5]);
   t[0] = odd(s[6], one1, one2);
   two3 = maj(s[6], one1, one2);
   t[1] = odd(two1, two2, two3);
   t[2] = maj(two1, two2, two3);
}

```

with following semantics:




```

exactly7attacks :=   t[2] &  t[1] &  t[0]
exactly6attacks :=   t[2] &  t[1] & ~t[0]
exactly5attacks :=   t[2] & ~t[1] &  t[0]
exactly4attacks :=   t[2] & ~t[1] & ~t[0]
exactly3attacks :=  ~t[2] &  t[1] &  t[0]
exactly2attacks :=  ~t[2] &  t[1] & ~t[0]
exactly1attack  :=  ~t[2] & ~t[1] &  t[0]
noAttack        :=  ~t[2] & ~t[1] & ~t[0]

atLeast4attacks :=                   t[2]
atLeast2attacks := atLeast4attacks | t[1]
atLeast1attack  := atLeast2attacks | t[0]
noAttack        := ~atLeast1attack
exactly1attack  :=  atLeast1attack  ^ atLeast2attacks

```

### Popcount as log2 of LS1B


Assuming an architecture has a fast popcount-instruction (but no bitscan). One can isolate the LS1B, decrement it and count the remaining trailing "ones" to perform the logarithm dualis:




```

log2(LS1B) = popCount( LS1B - 1 );
bitIndexOfLS1B(x) = popCount( (x & -x) - 1 );

```

For instance, LS1B is 2^44, decrementing leaves a below LSB1 mask with exactly 44 bits set:




```

0x0000100000000000   0x00000FFFFFFFFFFF
. . . . . . . .      . . . . . . . .
. . . . . . . .      . . . . . . . .
. . . . 1 . . .      1 1 1 1 . . . .
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1
. . . . . . . .      1 1 1 1 1 1 1 1

```





### Hamming Distance


The [hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) of two words is defined as the number of corresponding [different bits](General_Setwise_Operations#ExclusiveOr "General Setwise Operations").




```

int hammingDistance (U64 a, U64 b) {return popcnt( a ^ b);}

```

Hamming distance greater than one or two is an important property of codes to detect or even correct one-bit errors.


The minimum and average hamming distance over all [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") was considered as "quality"-measure of the keys. However, as long the minimum hamming distance is greater zero, [linear independence](https://en.wikipedia.org/wiki/Linear_independence) (that is a small subset of all keys doesn't xor to zero), is much more important than hamming distance [[19]](#cite_note-19). Maximizing the minimal hamming distance leads to very poor Zobrist keys [[20]](#cite_note-20).



### Weighted PopCount


For a [SIMD-wise](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") kind of weighted population count, see the [SSE2 dot-product](SSE2#SSE2dotproduct "SSE2").



### Pre-calculated Mobility


Similar to [Attacks by Occupancy Lookup](Sliding_Piece_Attacks#AttacksbyOccupancyLookup "Sliding Piece Attacks") to determine attack sets of sliding pieces, we may use pre-calculated population count or even center-weighted population count as a rough estimate on piece [mobility](Mobility "Mobility") [[21]](#cite_note-21). It may not consider subsets of let say safe target squares.



### Piece Attacks Count


As pointed out by [Marco Costalba](Marco_Costalba "Marco Costalba") [[22]](#cite_note-22) [[23]](#cite_note-23), specialized routines to count the population ([Mobility](Mobility "Mobility")) of attack sets of [king](King "King"), [knight](Knight "Knight") and line-wise sub-sets of sliding pieces can be done more efficiently than the general [SWAR-Popcount](Population_Count#SWARPopcount "Population Count"). This is similar to [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") the whole bitboard versus [Rank, File and Diagonal](Flipping_Mirroring_and_Rotating#RankFileAndDiagonal "Flipping Mirroring and Rotating"), and is based on mapping the up to eight scattered occupied bits to one byte, to perform a single [byte lookup](Population_Count#Lookup "Population Count"). For various mapping techniques, see:



* [Hashing Multiple Bits](Bitboard_Serialization#HashingMultipleBits "Bitboard Serialization") from [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
* [Rank, File and Diagonal](Flipping_Mirroring_and_Rotating#RankFileAndDiagonal "Flipping Mirroring and Rotating") from [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
* [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")


## Popcount in Hardware


* [Ferranti Mark 1](Ferranti_Mark_1#Instructions "Ferranti Mark 1")
* [CDC 6600](CDC_6600#PopulationCount "CDC 6600")
* [CDC Cyber](CDC_Cyber#PopulationCount "CDC Cyber")
* [SSE4.2](SSE4#SSE4.2 "SSE4"), [Intel](Intel "Intel") [x86](X86 "X86"), [x86-64](X86-64 "X86-64")
* [SSE4a](SSE4#SSE4a "SSE4"), [AMD](AMD "AMD") x86, x86-64


## See also


* [Assembly Popcounts](Assembly#HAKMEM169 "Assembly")
* [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
* [Greater One Sets](General_Setwise_Operations#GreaterOne "General Setwise Operations") from [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
* [libpopcnt](Kim_Walisch#PopCount "Kim Walisch") by [Kim Walisch](Kim_Walisch "Kim Walisch")
* [MMX Popcount](MMX#MMXPopcount "MMX")
* [Mobility](CDC_Cyber#Mobility "CDC Cyber") in [Chess 4.6](Chess_(Program) "Chess (Program)") on the [CDC Cyber](CDC_Cyber "CDC Cyber")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SSE2 Population Count](SSE2#SSE2popcount "SSE2")
* [SSSE3 Population Count](SSSE3#PopCount "SSSE3")


## Publications


### 1949 ...


* [Alan Turing](Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/~rst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), 9.4 The position of the most significant digit » [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1")
* [Maurice Wilkes](Mathematician#MVWilkes "Mathematician"), [David Wheeler](Mathematician#DJWheeler "Mathematician"), [Stanley Gill](https://en.wikipedia.org/wiki/Stanley_Gill) (**1957**). *The Preparation of Programs for an Electronic Digital Computer*. Addison-Wesley Press; 2nd edition, [amazon.com](http://www.amazon.com/preparation-programs-electronic-Addison-Wesley-mathematics/dp/B0006AV1QQ), [Donald B. Gillies](Mathematician#DBGillies "Mathematician") and [Jeffrey C. P. Miller](https://en.wikipedia.org/wiki/J._C._P._Miller) on [SWAR-Popcount](Population_Count#SWARPopcount "Population Count"), pages 191–193
* [Peter Wegner](Mathematician#PWegner "Mathematician") (**1960**). *A technique for counting ones in a binary computer*. [Communications of the ACM](ACM#Communications "ACM"), [Volume 3, 1960](http://www.informatik.uni-trier.de/~ley/db/journals/cacm/cacm3.html#Wegner60)
* Michael Beeler, [Bill Gosper](Bill_Gosper "Bill Gosper"), [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](https://dspace.mit.edu/handle/1721.1/6086)*, Memo 239, Artificial Intelligence Laboratory, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [David A. Wagner](Mathematician#DAWagner "Mathematician"), [Steven M. Bellovin](Steven_M._Bellovin "Steven M. Bellovin") (**1994**). *[A Programmable Plaintext Recognizer](http://academiccommons.columbia.edu/catalog/ac:127097)*. [[24]](#cite_note-24)


### 2000 ...


* [Simon Y. Berkovich](http://www.cs.gwu.edu/people/faculty/82), Gennadi M. Lapir, Marilyn Mack (**2000**). *[A Bit-Counting Algorithm Using the Frequency Division Principle](http://portal.acm.org/citation.cfm?id=362453)*. Software, Practice and Experience Vol. 30, No. 14, 2000, pp. 1531-1540
* [Eyas El-Qawasmeh](http://www.informatik.uni-trier.de/~ley/pers/hd/e/El=Qawasmeh:Eyas.html) (**2001**). *[Beating the Popcount](http://130.203.133.150/viewdoc/summary;jsessionid=A8ADC0228B8051C3ED8DF344DF5573CD?doi=10.1.1.127.8246).* International Journal of Information Technology, Singapore, Vol. 9. No. 1
* [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2002**). *[Hacker's Delight](http://hackersdelight.org/)*. [Addison-Wesley Professional](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley)
* [Eyas El-Qawasmeh](http://www.informatik.uni-trier.de/~ley/pers/hd/e/El=Qawasmeh:Eyas.html), [Wafa'a Al-Qarqaz](http://www.yu.edu.jo/fmd/detailsEN.aspx?myID=18327) (**2006**). *Reducing Lookup Table Size used for Bit-Counting Algorithm*. Computer Science Dept. [Jordan University of Science and Technology](https://en.wikipedia.org/wiki/Jordan_University_of_Science_and_Technology), [pdf](http://www.uop.edu.jo/csit2006/vol3%20pdf/pg524.pdf)
* [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2007**). *The Quest for an Accelerared Population Count*. in [Andy Oram](http://www.oreillynet.com/pub/au/36) & [Greg Wilson](Greg_Wilson "Greg Wilson") (eds.) (**2007**).  *Beautiful code: Leading Programmers Explain How They Think*. [O'Reilly](https://en.wikipedia.org/wiki/O%27Reilly_Media), [amazon.com](http://www.amazon.com/Beautiful-Code-Leading-Programmers-Practice/dp/0596510047)
* [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz), Sideways addition, pp 11


### 2010 ...


* [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2012**). *[Hacker's Delight, 2nd Edition](http://www.informit.com/store/hackers-delight-9780321842688)*. [Addison-Wesley Professional](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley), More coverage of population count and counting leading zeros, Array population count
* [Andreas Stiller](http://de.linkedin.com/pub/andreas-stiller/a/381/aa9) (**2013**). *[Spezialkommando - Intrinsic \_\_popcnt() zählt die Einsen](http://www.heise.de/artikel-archiv/ct/2013/05/180_Spezialkommando)*. [c't Magazin für Computertechnik](http://www.heise.de/ct/) 5/2013, p. 180 (German)
* [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), [Nathan Kurz](http://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612) [[25]](#cite_note-25) » [AVX2](AVX2 "AVX2"), [AVX-512](AVX-512 "AVX-512")


## Postings


### 1998 ...


* [Bean counters Part1](https://www.stmintz.com/ccc/index.php?id=25091) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), August 19, 1998
* [Bean counters Part2](https://www.stmintz.com/ccc/index.php?id=25095) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), August 19, 1998
* [Countbits() Function](https://www.stmintz.com/ccc/index.php?id=38188) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), January 03, 1999
* [Sideways Add / Population Count](http://cryptome.org/jya/sadd.htm) by [Jitze Couperus](http://www.couperus.org/), [Steve Bellovin](Steven_M._Bellovin "Steven M. Bellovin") and [Axel H. Horns](http://de.linkedin.com/in/horns), [cryptography@c2.net](https://en.wikipedia.org/wiki/C2Net), January 28, 1999 » [CDC 6600](CDC_6600 "CDC 6600") [[26]](#cite_note-26)


### 2000 ...


* [fast bit counting](https://www.stmintz.com/ccc/index.php?id=106644) by Flemming Rodler, [CCC](CCC "CCC"), April 19, 2000
* [Bit counting revisited](https://www.stmintz.com/ccc/index.php?id=106791) by Flemming Rodler, [CCC](CCC "CCC"), April 19, 2000
* [PowerPC BitCounting Functions Speed](https://www.stmintz.com/ccc/index.php?id=106960) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), April 20, 2000 » [PowerPC](PowerPC "PowerPC")
* [Counting the number of bits in a 32-bit word](http://groups.google.com/group/comp.lang.c/browse_frm/thread/56af26ce0b48cbcd) by [George Marsaglia](Mathematician#GMarsaglia "Mathematician"), [comp.lang.c](http://groups.google.com/group/comp.lang.c/topics), December 7, 2000
* [Re: Chezzz 1.0.1 - problem solved - for David Rasmussen](https://www.stmintz.com/ccc/index.php?id=281989) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 05, 2003 [[27]](#cite_note-27)
* [Counting bits](https://www.stmintz.com/ccc/index.php?id=293853) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), April 17, 2003
* [Hamming distance and lower hash table indexing](https://www.stmintz.com/ccc/index.php?id=313807) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), September 02, 2003
* [PopCount optimization](https://www.stmintz.com/ccc/index.php?id=353997) by [milix](Anastasios_Milikas "Anastasios Milikas"), [CCC](CCC "CCC"), March 11, 2004


### 2005 ...


* [Population count in SSE2, again](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/958e93d748e48121) by James Van Buskirk, [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), April 12, 2008
* [core2 popcnt](http://www.talkchess.com/forum/viewtopic.php?t=26542) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), February 13, 2009
* [Piece attacks count](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=267994&t=27965) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 18, 2009 » [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [Bit twiddlement question: greater of two popcounts](http://talkchess.com/forum/viewtopic.php?t=29269) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), August 06, 2009


### 2010 ...


* [Stockfish POPCNT support with gcc](http://www.talkchess.com/forum/viewtopic.php?t=32227) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), January 31, 2010
* [Yet another handmade POPCNT](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/6c8b3f09d890af1b) by hopcode, [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), January 05, 2011
* [A brief history of the popcnt instruction](http://www.talkchess.com/forum/viewtopic.php?t=38521) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 22, 2011
* [Introduction and (hopefully) contribution - bitboard methods](http://www.talkchess.com/forum/viewtopic.php?t=39268) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), June 03, 2011 » [BitScan](BitScan "BitScan")
* [using Popcount and Prefetch with SSE4 hardware support](http://www.talkchess.com/forum/viewtopic.php?t=43771) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), May 19, 2012 » [Memory](Memory "Memory"), [SSE4](SSE4 "SSE4")
* [64 bits for 64 squares ?](http://macechess.blogspot.de/2013/04/64-bits-for-64-squares.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), April 28, 2013
* [Stockfish 32-bit and hardware instructions on MSVC++](http://www.talkchess.com/forum/viewtopic.php?t=54798) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), December 30, 2014  » [Stockfish](Stockfish "Stockfish"), [BitScan](BitScan "BitScan"), Population Count


### 2015 ...


* [Re: Linux Version of Maverick 1.5](http://www.talkchess.com/forum/viewtopic.php?t=58230&start=3) by [Michael Dvorkin](Michael_Dvorkin "Michael Dvorkin"), [CCC](CCC "CCC"), November 12, 2015 » [OS X](Mac_OS "Mac OS"), [Maverick](Maverick "Maverick")
* [syzygy users (and Ronald)](http://www.talkchess.com/forum/viewtopic.php?t=61559) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 29, 2016 » [BitScan](BitScan "BitScan")


### 2020 ...


* [\_\_builtin\_popcountll doesn't bring any gain](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74918) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), August 28, 2020
* [C++20 standard bit operations](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75818) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 15, 2020 » [General Setwise Operations](General_Setwise_Operations "General Setwise Operations"), [BitScan](BitScan "BitScan"), [C++](Cpp "Cpp")


## External Links


* [Hamming weight from Wikipedia](https://en.wikipedia.org/wiki/Hamming_weight)
* [Population count (POPCNT) - CompArch](http://semipublic.comp-arch.net/wiki/Population_count_%28POPCNT%29)
* [Crazy On Tap - Secret Opcodes](http://www.crazyontap.com/topic.php?TopicId=43382) [[28]](#cite_note-28)
* [Blender: POPCNT for counting bits](http://kent-vandervelden.blogspot.com/2009/10/counting-bits-population-count-and.html)
* [HAKMEMC -- HAKMEM Programming hacks in C](http://www.cl.cam.ac.uk/~am21/hakmemc.html) by [Alan Mycroft](http://www.cl.cam.ac.uk/~am21/)
* [popcount](http://www.hackersdelight.org/hdcodetxt/pop.c.txt) [C](C "C") samples from [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2002, 2012**). *[Hacker's Delight](Henry_S._Warren,_Jr.#HackersDeligh "Henry S. Warren, Jr.")*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley)
* [The Aggregate Magic Algorithms -Population Count (Ones Count)](http://aggregate.org/MAGIC/#Population%20Count%20%28Ones%20Count) by [Hank Dietz](Hank_Dietz "Hank Dietz")
* [Counting bits set](http://www-graphics.stanford.edu/~seander/bithacks.html#CountBitsSetNaive) from [Bit Twiddling Hacks](http://graphics.stanford.edu/%7Eseander/bithacks.html) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
* [Optimising Bit Counting using Iterative, Data-Driven Development](http://www.necessaryandsufficient.net/2009/04/optimising-bit-counting-using-iterative-data-driven-development/) from [Necessary and Sufficient](http://www.necessaryandsufficient.net/) by [Damien Wintour](http://www.necessaryandsufficient.net/author/admin/page/2/)
* [Count bits set in parallel a.k.a. Population Count](http://bits.stephan-brumme.com/countBits.html) from [the bit twiddler](http://bits.stephan-brumme.com/) by [Stephan Brumme](http://www.stephan-brumme.com/)
* [Benchmarking CRC32 and PopCnt instructions - strchr.com](http://www.strchr.com/crc32_popcnt) by Peter Kankowski
* [SSSE3: fast popcount](http://0x80.pl/articles/sse-popcount.html) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), May 24, 2008 » [SSSE3](SSSE3 "SSSE3")
* [Speeding up bit-parallel population count](http://0x80.pl/articles/faster-popcount-for-large-data.html) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), April 13, 2015
* [Population count using XOP instructions](http://0x80.pl/articles/xop-popcnt.html) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), December 16, 2016 » [XOP](XOP "XOP")
* [GitHub - WojciechMula/sse-popcount: SIMD (SSE) population count](https://github.com/WojciechMula/sse-popcount) by [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła")
* [GitHub - kimwalisch/libpopcnt: Fast C/C++ bit population count library](https://github.com/kimwalisch/libpopcnt) » [libpopcnt](Kim_Walisch#PopCount "Kim Walisch") by [Kim Walisch](Kim_Walisch "Kim Walisch")
* [Census from Wikipedia](https://en.wikipedia.org/wiki/Census)
* [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie") 4tet - One, one, one + Spring song, [Subway](https://de.wikipedia.org/wiki/Subway_(Musikclub)), [Cologne](https://en.wikipedia.org/wiki/Cologne), April 12, 1999, [3sat](https://en.wikipedia.org/wiki/3sat) broadcast [[29]](#cite_note-29), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie"), [Bobo Stenson](https://en.wikipedia.org/wiki/Bobo_Stenson), [Lars Danielsson](Category:Lars_Danielsson "Category:Lars Danielsson"), [Jon Christensen](Category:Jon_Christensen "Category:Jon Christensen") 
 
## References


1. [↑](#cite_ref-1) Color of each pixel is [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between the binary representations of its x and y coordinates, modulo 16, in the 16-color system, by Josiedraus, June 8, 2007, [Richard Hamming from Wikipedia](https://en.wikipedia.org/wiki/Richard_Hamming)
2. [↑](#cite_ref-2) [Cryptography](https://en.wikipedia.org/wiki/Cryptography) is also a significant application of the /R function symbol, which counts the number of one bits in a word; Turing refers to this as the "sideways adder" in his quick-reference summary. from [Alan Turing](Alan_Turing "Alan Turing") (**1949**). *[Alan Turing's Manual for the Ferranti Mk. I](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f45472f)*. transcribed in 2000 by [Robert Thau](http://www.panix.com/~rst/), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-1.Ferranti_Mark_1_manual.Turing-Alan/2-1.Ferranti_Mark_1_manual.Turing-Alan.1951.UNIVERSITY_OF_MANCHESTER.062303005.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), 9.4 The position of the most significant digit  » [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1")
3. [↑](#cite_ref-3) [Extending the World’s Most Popular Processor Architecture](http://software.intel.com/en-us/articles/extending-the-worlds-most-popular-processor-architecture) by R.M. Ramanathan, [Intel](Intel "Intel"), covers SSE4 and popcnt
4. [↑](#cite_ref-4) [\_mm\_popcnt\_u64](https://msdn.microsoft.com/en-us/library/bb531475(v=vs.120).aspx)
5. [↑](#cite_ref-5) [\_\_builtin\_popcountll](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) [GCC](Free_Software_Foundation#GCC "Free Software Foundation") Intrinsic
6. [↑](#cite_ref-6) [Stockfish POPCNT support with gcc](http://www.talkchess.com/forum/viewtopic.php?t=32227) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), January 31, 2010
7. [↑](#cite_ref-7) [Matters Computational - ideas, algorithms, source code](http://www.jjj.de/fxt/fxtbook.pdf) (pdf) Ideas and Source Code by [Jörg Arndt](Mathematician#Arndt "Mathematician"), 1.7 Functions related to the base-2 logarithm, function one\_bit\_q(), pp 18
8. [↑](#cite_ref-8) [Counting bits set, Brian Kernighan's way](http://www-graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan) from [Bit Twiddling Hacks](http://graphics.stanford.edu/%7Eseander/bithacks.html) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
9. [↑](#cite_ref-9) [Peter Wegner](Mathematician#PWegner "Mathematician") (**1960**). *A technique for counting ones in a binary computer*. [Communications of the ACM](ACM#Communications "ACM"), [Volume 3, 1960](http://www.informatik.uni-trier.de/~ley/db/journals/cacm/cacm3.html#Wegner60)
10. [↑](#cite_ref-10) [Edwin Ford Beckenbach](Mathematician#EFBeckenbach "Mathematician") (editor) (**1964**). *[Applied combinatorial mathematics](http://onlinelibrary.wiley.com/doi/10.1002/bimj.19660080310/abstract)*, [John Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
11. [↑](#cite_ref-11) [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz), Sideways addition, p 11
12. [↑](#cite_ref-12) [Maurice Wilkes](Mathematician#MVWilkes "Mathematician"), [David Wheeler](Mathematician#DJWheeler "Mathematician"), [Stanley Gill](https://en.wikipedia.org/wiki/Stanley_Gill) (**1951**). *The Preparation of Programs for an Electronic Digital Computer*. Addison-Wesley Press; 1st edition, [amazon.com](http://www.amazon.com/preparation-programs-electronic-digital-computer/dp/B0007DWTT0); 2nd edition 1957, [amazon.com](http://www.amazon.com/preparation-programs-electronic-Addison-Wesley-mathematics/dp/B0006AV1QQ)
13. [↑](#cite_ref-13) [Electronic Delay Storage Automatic Calculator from Wikipedia](https://en.wikipedia.org/wiki/Electronic_Delay_Storage_Automatic_Calculator)
14. [↑](#cite_ref-14) [Casting Out Nines](http://www.billthelizard.com/2009/06/casting-out-nines.html) by [Bill the Lizard](http://www.billthelizard.com/), June 13, 2009
15. [↑](#cite_ref-15) [Donald Knuth](Donald_Knuth "Donald Knuth") (**2009**). *[The Art of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html), Volume 4, Fascicle 1: Bitwise tricks & techniques*, as [Pre-Fascicle 1a postscript](http://www-cs-faculty.stanford.edu/%7Eknuth/fasc1a.ps.gz), p 9
16. [↑](#cite_ref-16) HAKMEM - ITEM 169 To count the ones in a PDP-6/10 word (in order of one-ups-manship: [Gosper](Bill_Gosper "Bill Gosper"), Mann, Lenard, [Root and Mann])
17. [↑](#cite_ref-17) [HAKMEMC -- HAKMEM Programming hacks in C](http://www.cl.cam.ac.uk/~am21/hakmemc.html) by [Alan Mycroft](http://www.cl.cam.ac.uk/~am21/)
18. [↑](#cite_ref-18) [HAKMEM 169](Bill_Gosper#HAKMEM169 "Bill Gosper") for [PDP-6](PDP-6 "PDP-6")/[PDP-10](PDP-10 "PDP-10") 36-bit words
19. [↑](#cite_ref-19) [Re: About random numbers and hashing](https://www.stmintz.com/ccc/index.php?id=200622) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), December 05, 2001
20. [↑](#cite_ref-20) [Zobrist key random numbers](http://www.talkchess.com/forum/viewtopic.php?t=26152) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") from [CCC](CCC "CCC"), January 21, 2009
21. [↑](#cite_ref-21) [Magic and precomputation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6823) by [Onno Garms](Onno_Garms "Onno Garms") from [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), September 23, 2007
22. [↑](#cite_ref-22) [fast mobility count through hashing](http://www.talkchess.com/forum/viewtopic.php?t=27820) by [Marco Costalba](Marco_Costalba "Marco Costalba") from [CCC](CCC "CCC"), May 09, 2009
23. [↑](#cite_ref-23) [Piece attacks count](http://www.talkchess.com/forum/viewtopic.php?t=27965) by [Marco Costalba](Marco_Costalba "Marco Costalba") from [CCC](CCC "CCC"), May 18, 2009
24. [↑](#cite_ref-24) [Sideways Add / Population Count](http://cryptome.org/jya/sadd.htm) by [Jitze Couperus](http://www.couperus.org/) and [Steve Bellovin](Steven_M._Bellovin "Steven M. Bellovin") et al., [cryptography@c2.net](https://en.wikipedia.org/wiki/C2Net), January 28, 1999
25. [↑](#cite_ref-25) [sse-popcount/popcnt-avx512-harley-seal.cpp at master · WojciechMula/sse-popcount · GitHub](https://github.com/WojciechMula/sse-popcount/blob/master/popcnt-avx512-harley-seal.cpp)
26. [↑](#cite_ref-26) [David A. Wagner](Mathematician#DAWagner "Mathematician"), [Steven M. Bellovin](Steven_M._Bellovin "Steven M. Bellovin") (**1994**). *[A Programmable Plaintext Recognizer](http://academiccommons.columbia.edu/catalog/ac:127097)*.
27. [↑](#cite_ref-27) [AMD Athlon Processor x86 Code Optimization Guide](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/22007.pdf) (pdf) Efficient 64-Bit Population Count Using MMX™ Instructions Page 184
28. [↑](#cite_ref-28) [National Security Agency from Wikipedia](https://en.wikipedia.org/wiki/National_Security_Agency)
29. [↑](#cite_ref-29) [Ali Haurand from Wikipedia.de](https://de.wikipedia.org/wiki/Ali_Haurand) (German)

**[Up one Level](Bitboards "Bitboards")**







 
