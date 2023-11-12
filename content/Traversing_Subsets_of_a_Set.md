---
title: Traversing Subsets of a Set
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Traversing Subsets of a Set**



[
**Traversing Subsets of a Set** determines the [power set](https://en.wikipedia.org/wiki/Power_set) of a set, or a subset of the power set with certain properties such as equal [cardinality](https://en.wikipedia.org/wiki/Cardinality). Represented by a [bitboard](Bitboards "Bitboards"), this is useful to loop over possible [occupancies](Occupancy "Occupancy") of a set of rays or lines, and to [look for](Looking_for_Magics "Looking for Magics") [magic factors](Magic_Bitboards "Magic Bitboards") with a certain cardinality.



### Contents


* [1 Enumerating All Subsets](#enumerating-all-subsets)
	+ [1.1 All Subsets of the Universal Set](#all-subsets-of-the-universal-set)
	+ [1.2 All Subsets of any Set](#all-subsets-of-any-set)
* [2 Subsets with equal Cardinality](#subsets-with-equal-cardinality)
	+ [2.1 Snoobing the Universe](#snoobing-the-universe)
		- [2.1.1 Modified Snoob](#modified-snoob)
		- [2.1.2 Reverse Snoob](#reverse-snoob)
	+ [2.2 Snoobing any Sets](#snoobing-any-sets)
* [3 See also](#see-also)
* [4 Selected Publications](#selected-publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






### All Subsets of the Universal Set


To enumerate all subsets of the universal set -1 is obvious, but takes some time. Assuming one loop cycle takes one nano-second, it would still take 18,446,744,073 seconds or about 585 years!




```C++

// enumerate all subsets of the universal set -1
void enumerateAllSubsetsOfTheBitboardUniverse() {
   U64 n = 0;
   do {
      doSomeThingWithSubset(n);
      n++;
   } while ( n );
}

```

### All Subsets of any Set



```C++

// enumerate all subsets of set d
void enumerateAllSubsets(U64 d) {
   U64 n = 0;
   do {
      doSomeThingWithSubset(n);
      n = (n - d) & d;
   } while ( n );
}

```

This is how the Carry-Rippler, introduced by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and later by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") <a id="cite-note-3" href="#cite-ref-3">[3]</a> works: we first set all "unused" bits of the set by oring the One's Complement of d. The increment ripples a possible carry through all unused bits - and finally we clear all unused bits again by intersection with the set d:




```C++

n = ((n | ~d) + 1) & d;

```

We can safely replace bitwise-or by add, since unused bits are always zero:




```C++

n = ((n + ~d) + 1) & d;

```

Replacing One's Complement by Two's Complement minus one




```C++

n = ((n + (-d-1) + 1) & d;

```

leaves the final expression




```C++

n = (n - d) & d;

```

## Subsets with equal Cardinality


Traversing subsets with one bit set was already mentioned in the [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization") topic.


Equal cardinality subsets have **S**ame **n**umber **o**f **o**ne **b**its - thus **Snoob**, as synonym of the iterator-function. 
To use snoob in a loop:




```C++

U64 x, y, first = 0x0f; // traverse all 4-bit sequences
for (x = first; (y = snoob(x)) > x; x = y)
   doSomethingWith(y);

```

We add the [LS1B](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations") (smallest) to the set, to get a greater number. The former LS1B becomes zero with overflow. If the next higher bit was zero, it takes the carry and the number of set bits didn't change - two flipped bits. Otherwise, if the carry ripples through, leaving further zero(s), we need to set least significant bits accordingly, to keep the cardinality equal. Thus, we xor ripple to get the flipped bits as ones. We shift this sequence right, until it becomes the least significant bits (divide by smallest). To take the two compensating bits off, we need to further divide by 4 (leading or trailing shift right 2). Get the next higher number with the same number of one bits (Snoob) was devised by [Bill Gosper](Bill_Gosper "Bill Gosper") as [HAKMEM 175](Bill_Gosper#HAKMEM175 "Bill Gosper") in [PDP-6](PDP-6 "PDP-6") [Assembly](Assembly "Assembly") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and elaborated in [Hacker's Delight](Henry_S._Warren,_Jr.#HackersDeligh "Henry S. Warren, Jr.") by [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### Snoobing the Universe



```C++

// get next greater value with same number of one bits
// Taken from "Hacker's Delight" by Henry S. Warren, Jr.
// originally appeared as  HAKMEM ITEM 175 (Bill Gosper)
U64 snoob (U64 x) {
   U64 smallest, ripple, ones;
   smallest = x & -x;
   ripple = x + smallest;
   ones = x ^ ripple;
   ones = (ones >> 2) / smallest;
   return ripple | ones;
}

```

### Modified Snoob


Division by power of two replaced by [De Bruijn bitscan](BitScan#DeBruijnMultiplation "BitScan") and shift right:




```C++

const U64 deBruijn = C64(0x03f79d71b4cb0a89);

const unsigned int deBruijnLookup[64] = // or unsigned char
{
    0,  1, 48,  2, 57, 49, 28,  3,
   61, 58, 50, 42, 38, 29, 17,  4,
   62, 55, 59, 36, 53, 51, 43, 22,
   45, 39, 33, 30, 24, 18, 12,  5,
   63, 47, 56, 27, 60, 41, 37, 16,
   54, 35, 52, 21, 44, 32, 23, 11,
   46, 26, 40, 15, 34, 20, 31, 10,
   25, 14, 19,  9, 13,  8,  7,  6,
};

// get next greater value with same number of one bits
U64 snoob (U64 x) {
   U64 smallest, ripple, ones;
   smallest = x & (0-x);
   ripple   = x + smallest;
   ones     = x ^ ripple;
   ones     = (ones >> 2) >> deBruijnLookup[(smallest*deBruijn) >> 58];
   return ripple | ones;
}

```

Due to implicit modulo(64) of the shift amount by the processor




```C++

(ones >> i) >> 2 == (ones >> 2) >> i might not equal to ones >> (2 + i)!

```

### Reverse Snoob


based on [One's Complement](General_Setwise_Operations#ComplementSet "General Setwise Operations"):




```C++

// get next less value with same number of one bits
U64 rSnoob (U64 sub) {
   return ~snoob(~sub);
}

```

or to safe some bitscans




```C++

// get next less value with same number of one bits
U64 rSnoob (U64 sub) {
   if ( sub & 1 )
      return ~snoob(~sub);
   U64 lsb = sub & (0-sub);
   return sub ^ lsb ^ (lsb>>1);
}

```

### Snoobing any Sets


combining the Carry Rippler with Snoob - a little more complicated




```C++

set:
... 1110 0110 0x..e6
e.g. all subsets with two set bits:
... 0000 0110 0x..06
... 0010 0010 0x..22
... 0010 0100 0x..24
... 0100 0010 0x..42
... 0100 0100 0x..44
... 0110 0000 0x..60
... 1000 0010 0x..82
... 1000 0100 0x..84
... 1010 0000 0x..a0
... 1100 0000 0x..c0

```


```C++

// get next greater subset of set with same number of one bits
U64 snoob (U64 sub, U64 set) {
   U64 tmp = sub-1;
   U64 rip = set & (tmp + (sub & (0-sub)) - set);
   for(sub = (tmp & sub) ^ rip; sub &= sub-1; rip ^= tmp, set ^= tmp)
       tmp = set & (0-set);
   return rip;
}

```


```C++

// get next less set of a subset with same number of one bits
U64 rSnoob (U64 sub, U64 set) {
   return ~snoob(~sub & set, set) & set;
}

```

## See also


* [Bitboard Serialization](Bitboard_Serialization "Bitboard Serialization")
* [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


## Selected Publications


* Michael Beeler, [Bill Gosper](Bill_Gosper "Bill Gosper"), [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](http://home.pipeline.com/~hbaker1/hakmem/hakmem.html), Memo 239*. [CSAIL](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory), [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [ITEM 175 (Gosper)](http://home.pipeline.com/~hbaker1/hakmem/hacks.html#item175)
* [Frank Ruskey](Mathematician#FRuskey "Mathematician") (**2003**). *Combinatorial Generation*. [University of Victoria](https://en.wikipedia.org/wiki/University_of_Victoria), [pdf](http://www.1stworks.com/ref/ruskeycombgen.pdf)
* [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") (**2012**). *[Hacker's Delight, 2nd Edition](http://hackersdelight.org/)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison%E2%80%93Wesley)


## Forum Posts


* [Re: move generators in computer chess, Tricky bit tricks](http://groups.google.com/group/rec.games.chess/msg/f4f0751cc8b928c8) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 20, 1994
* [Re: algorithm question](http://www.stmintz.com/ccc/index.php?id=490129) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), February 27, 2006
* [Don't understand CarryRippler](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73198) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), February 27, 2020 » [Carry-Rippler](#allsubsetsofanyset), [Rust](Rust "Rust")


## External Links


* [Partially ordered set from Wikipedia](https://en.wikipedia.org/wiki/Partially_ordered_set)
* [Power set from Wikipedia](https://en.wikipedia.org/wiki/Power_set)


## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [4D](https://en.wikipedia.org/wiki/Four-dimensional_space)-[hypercube](https://en.wikipedia.org/wiki/Hypercube), layered according to distance from one corner. As described in "[Alice in Wonderland](Alice "Alice")" by the [Cheshire Cat](https://en.wikipedia.org/wiki/Cheshire_Cat), this vertex-first-shadow of the [tesseract](https://en.wikipedia.org/wiki/Tesseract) forms a [rhombic dodecahedron](https://en.wikipedia.org/wiki/Rhombic_dodecahedron). Note that the two central (green) vertices should coincide if using an orthogonal projection from 4 to 3 dimensions, but were drawn here slightly apart. The eight [nibbles](Nibble "Nibble") with odd binary digit sums form a cube and are marked in white. The two [palindromes](https://en.wikipedia.org/wiki/Palindrome) 0110 and 1001 (compare XOR and XNOR) are projected in the center of the rhombic dodecahedron and are marked in green. The other six nibbles with even binary digit sums form an [octahedron](https://en.wikipedia.org/wiki/Octahedron) and are marked in blue, image by Lipedia, 2010, [Hasse diagram from Wikipedia](https://en.wikipedia.org/wiki/Hasse_diagram) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tricky bit tricks](https://groups.google.com/d/msg/rec.games.chess/KnJvBnhgDKU/yCi5yBx18PQJ) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), October 20, 1994
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: algorithm question](http://www.stmintz.com/ccc/index.php?id=490129) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), [CCC](CCC "CCC"), February 27, 2006
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Michael Beeler, [Bill Gosper](Bill_Gosper "Bill Gosper"), [Rich Schroeppel](https://en.wikipedia.org/wiki/Richard_Schroeppel) (**1972**). *[HAKMEM](http://home.pipeline.com/~hbaker1/hakmem/hakmem.html), Memo 239*. [CSAIL](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory), [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Sample section of Hacker's Delight, Chapter 2 Basics](http://www.hackersdelight.org/basics1.pdf) (pdf) by [Henry S. Warren, Jr.](Henry_S._Warren,_Jr. "Henry S. Warren, Jr.") pp.14 Figure 2–1. *Next higher number with same number of 1-bits*.
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [C code for most of the programs that appear in HD | Fig. 2-1. Next higher number with same number of 1-bits](http://www.hackersdelight.org/hdcodetxt/snoob.c.txt)

**[Up one Level](Algorithms "Algorithms")**







 
