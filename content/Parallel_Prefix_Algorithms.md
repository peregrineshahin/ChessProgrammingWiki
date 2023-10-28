---
title: Parallel Prefix Algorithms
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* Parallel Prefix Algorithms**



 [](http://www.toves.org/books/distalg/) Parallel Prefix Sum <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Parallel prefix algorithms** compute all [prefixes](https://en.wikipedia.org/wiki/Prefix_sum) of a input sequence in [logarithmic time](https://en.wikipedia.org/wiki/Time_complexity#Logarithmic_time), and are topic of various [SIMD and SWAR techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") applied to [bitboards](Bitboards "Bitboards") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . This page provides some basics on simple parallel prefix problems, like parity words and [Gray code](https://en.wikipedia.org/wiki/Gray_code) with some interesting properties, followed by some theoretical background on more complex parallel prefix problems, like [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") by [Steffan Westcott](Steffan_Westcott "Steffan Westcott"), and a comparison of three similar Kogge-Stone routines for different purpose. 




### Contents


* [1 Parity Words](#parity-words)
* [2 Gray Code](#gray-code)
* [3 Fill Stuff](#fill-stuff)
* [4 Elaborations on Kogge-Stone](#elaborations-on-kogge-stone)
* [5 Add/Sub versus Attacks](#add.2fsub-versus-attacks)
	+ [5.1 Add](#add)
	+ [5.2 Sub](#sub)
	+ [5.3 East Attacks](#east-attacks)
* [6 See also](#see-also)
* [7 Publications](#publications)
* [8 Forum Posts](#forum-posts)
* [9 External Links](#external-links)
* [10 References](#references)






[Parity](https://en.wikipedia.org/wiki/Parity_bit#Parity) is often related to [error detection and correction](https://en.wikipedia.org/wiki/Error_detection_and_correction). The modulo 2 sum aka [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") (xor) of any number of inputs is sufficient to determine even or odd parity. On a bitboard for each bit 0..63 we like to know, whether the number of ones including all trailing bits is odd or even, xi is the bit in x with bit-index i:




```

p0  = x0;
p1  = x0 ^ x1;
p2  = x0 ^ x1 ^ x2;
...
p63 = x0 ^ x1 ^ x2 ^ .... ^ x63;

```

Or [recursively](Recursion "Recursion")




```

p[i] = p[i-1] ^ x[i];

```

p63 indicates whether the whole cardinality is odd or even. The parallel prefix solution looks that way:




```

x ^= x <<  1;
x ^= x <<  2;
x ^= x <<  4;
x ^= x <<  8;
x ^= x << 16;
x ^= x << 32;

```

and only need `log2(64) == 6` steps to perform all the xor instructions.


Surprisingly, thanks to xor, we can restore the initial value by a final:




```

x ^= x << 1;

```





## Gray Code


The reflected binary code, or [Gray code](https://en.wikipedia.org/wiki/Gray_code) has some similar properties <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The Gray code is defined by the modulo 2 sum or [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") of a word with its value shifted right by one.




```

gray = x ^ (x >> 1);

```

This ensures that consecutive Gray codes have only one bit changed, that is a [Hamming distance](Population_Count#HammingDistance "Population Count") of one. For instance for a 4-bit or [nibble](Nibble "Nibble") Gray code:





|  x decimal
 |  x binary
 |  x>>1
 |  Gray bin
 |  decimal
 |
| --- | --- | --- | --- | --- |
|  0
 |  0000
 |  0000
 |  0000
 |  0
 |
|  1
 |  0001
 |  0000
 |  0001
 |  1
 |
|  2
 |  0010
 |  0001
 |  0011
 |  3
 |
|  3
 |  0011
 |  0001
 |  0010
 |  2
 |
|  4
 |  0100
 |  0010
 |  0110
 |  6
 |
|  5
 |  0101
 |  0010
 |  0111
 |  7
 |
|  6
 |  0110
 |  0011
 |  0101
 |  5
 |
|  7
 |  0111
 |  0011
 |  0100
 |  4
 |
|  8
 |  1000
 |  0100
 |  1100
 |  12
 |
|  9
 |  1001
 |  0100
 |  1101
 |  13
 |
|  10
 |  1010
 |  0101
 |  1111
 |  15
 |
|  11
 |  1011
 |  0101
 |  1110
 |  14
 |
|  12
 |  1100
 |  0110
 |  1010
 |  10
 |
|  13
 |  1101
 |  0110
 |  1011
 |  11
 |
|  14
 |  1110
 |  0111
 |  1001
 |  9
 |
|  15
 |  1111
 |  0111
 |  1000
 |  8
 |
|  0
 |  0000
 |  0000
 |  0000
 |  0
 |


Decoding Gray code is a parallel prefix problem similar to the ring-wise operations of the [Parity words](#paritywords). For a nibble Gray code:




```

x  = gray;
x ^= x >>  2;
x ^= x >>  1;

```

Or for 64-bit Gray-Codes:




```

x  = gray;
x ^= x >> 32;
x ^= x >> 16;
x ^= x >>  8;
x ^= x >>  4;
x ^= x >>  2;
x ^= x >>  1;

```

## Fill Stuff


Parallel prefix [front and rear-fills](Pawn_Fills "Pawn Fills"), for instance to determine [pawn spans](Pawn_Spans "Pawn Spans") in [bitboards](Bitboards "Bitboards"), are quite simple to understand.




```

U64 nortFill(U64 gen) {
   gen |= (gen <<  8);
   gen |= (gen << 16);
   gen |= (gen << 32);
   return gen;
}

U64 soutFill(U64 gen) {
   gen |= (gen >>  8);
   gen |= (gen >> 16);
   gen |= (gen >> 32);
   return gen;
}

```

This is actually a simplified [Kogge-Stone algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm"), whose general form even considers a second bitboard to occlude the flood accordantly.






## Elaborations on Kogge-Stone


Elaborations on [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") parallel prefix algorithm by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") <a id="cite-note-4" href="#cite-ref-4">[4]</a> :


A **parallel prefix** problem is of the sort:




```

   Given the terms x1, x2, x3, ... , xN and an associative operator #
   find the values q1 = x1
                   q2 = x1 # x2
                   q3 = x1 # x2 # x3
                   .
                   .
                   .
                   qN = x1 # x2 # x3 # ... # xN

```

Associative expressions can be bracketed any way you like, the result is the same. To see why this is interesting for chess programming, let's define x1, x2, ... and # to be




```

    xI = < gI, pI >     (a two element tuple)
         where gI = square aI has a rook on it
         and   pI = square aI is empty
         for all I = 1, 2, 3, ... , 8

and xI # xJ = < gI, pI >  #  < gJ, pJ >
            = < ((gI && pJ) || gJ),  (pI && pJ) >

```

All this algebra looks very scary at first, so here's an example:




```

  q2 = x1 # x2 = < rook_on_a1, a1_is_empty > # < rook_on_a2, a2_is_empty >
               = < ((rook_on_a1 && a2_is_empty) || rook_on_a2),
                   (a1_is_empty && a2_is_empty) >

```

* The first tuple of q2 tells us if a rook is on a2 or can move up to a2 along empty squares.
* The second tuple of q2 tells us if a rook could move up freely through a1-a2 ie. a1-a2 are empty.


In general,




```

  xI # x(I+1) # ... # xJ =
    < a_rook_somewhere_on_aI_to_aJ_is_either_on_aJ_or_can_move_up_to_aJ,
      all_squares_aI_to_aJ_are_empty >

```

and so




```

  qJ = < a_rook_somewhere_in_file_a_is_either_on_aJ_or_can_move_up_to_aJ,
         all_squares_a1_to_aJ_are_empty >

```

The tuples g and p are known as the "generator" and "propagator" terms in the literature of fast carry propagation circuits. But we are not dealing with carry bits in a carry propagate adder! Here, we are generating and propagating upward rook attacks along a file of a chessboard.


Why all this theory? Well, prefix computation is a heavily researched area, researched by many folk smarter than me :) Its of interest because it has many applications, such as VLSI design, pattern matching, and others. There are many different ways of going about it, with different implementation characteristics.




```

U64 FillUpOccluded(U64 g, U64 p) {
           g |= p & (g <<  8);
           p &=     (p <<  8);
           g |= p & (g << 16);
           p &=     (p << 16);
    return g |= p & (g << 32);
}

U64 RookAttacksUp(U64 rooks, U64 empty_squares) {
    return ShiftUp(FillUpOccluded(rooks, empty_squares));
}

```

The method chosen in FillUpOccluded() is based on a Kogge-Stone parallel prefix network, because it can be implemented very easily in software. The diagram below (trust me, it really \_is\_ supposed to look like that) is an illustration of how it works. The corresponding lines of program code are shown on the right. The inputs are fed into the network at the top, pass along the connecting lines, are combined by the # operator at various points, and the outputs appear at the bottom.




```

x1 x2 x3 x4 x5 x6 x7 x8         Input : g, p
|  |  |  |  |  |  |  |
V  V  V  V  V  V  V  V
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|\ |\ |\ |\ |\ |\ |\ |
| \| \| \| \| \| \| \|
|  #  #  #  #  #  #  #          g |= p & (g <<  8);
|  |  |  |  |  |  |  |          p &=     (p <<  8);
|\ |\ |\ |\ |\ |\ |  |
| \: \: \: \: \: \:  |
|  \  \  \  \  \  \  |
|  :\ :\ :\ :\ :\ :\ |
|  | \| \| \| \| \| \|
|  |  #  #  #  #  #  #          g |= p & (g << 16);
|  |  |  |  |  |  |  |          p &=     (p << 16);
|\ |\ |\ |\ |  |  |  |
| \: \: \: \:  |  |  |
|  \  \  \  \  |  |  |
|  :\ :\ :\ :\ |  |  |
|  | \: \: \: \:  |  |
|  |  \  \  \  \  |  |
|  |  :\ :\ :\ :\ |  |
|  |  | \: \: \: \:  |
|  |  |  \  \  \  \  |
|  |  |  ;\ ;\ :\ :\ |
|  |  |  | \| \| \| \|
|  |  |  |  #  #  #  #          g |= p & (g << 32);
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
V  V  V  V  V  V  V  V
q1 q2 q3 q4 q5 q6 q7 q8         Output : g

```

To convince yourself this works, select any output qI and trace upwards from the bottom of the diagram. You'll see it leads back to x1, x2, ... , xI, so qI is formed by some computation of x1 # x2 # ... # xI.


[Implementor's note : The 2 program lines that assign to variable p are not strictly correct. By the end of the routine, p1 and p2 have been trashed (reset). However, they are trashed after they can affect the correctness of the routine result.]






## Add/Sub versus Attacks


As a comparison three Kogge-Stone routines. A "classical" byte-wise [SWAR](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") adder, byte-wise subtraction, and byte-wise rook-attacks in east direction. Note that the inner parallel prefix instructions are the same in all three routines:




```

   gen |= pro & (gen << 1);
   pro &=       (pro << 1);
   gen |= pro & (gen << 2);
   pro &=       (pro << 2);
   gen |= pro & (gen << 4);

```

The difference are the assignments of generator and propagator, and the final result.



### Add


[ 4-bit Kogge-Stone adder
The software approach of a [Kogge-Stone](https://en.wikipedia.org/wiki/Kogge-Stone_adder) [hardware adder](Combinatorial_Logic#Adder "Combinatorial Logic") <a id="cite-note-5" href="#cite-ref-5">[5]</a> , requires the initial carry bits as generator, thus the [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of both summands, while the propagator is the modulo 2 sum, the [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") of both summands. To avoid inter byte overflows, the propagator has the least significant bits of each byte cleared. However the final carries need one further masked shift and the modulo two sum with the initial propagator.




```

// SIMD bytewise add a + b
U64 koggeStoneByteAdd(U64 a, U64 b) {
   const U64 aFile = C64(0x0101010101010101);
   U64 gen, pro;
   gen  = a & b;
   pro  = a ^ b;
   pro &= ~aFile;
   gen |= pro   & (gen << 1);
   pro &=         (pro << 1);
   gen |= pro   & (gen << 2);
   pro &=         (pro << 2);
   gen |= pro   & (gen << 4);
   gen  =~aFile & (gen << 1);
   return gen ^ a ^ b;
}

```

### Sub


Subtraction is based on the [two's complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") which is [ones' complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") plus one aka the A-File assuming [little-endian rank-file mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"). Thus, it is actually the sum of {a, ~b, one}, which is considered in calculating propagator and generator, which is the [majority](General_Setwise_Operations#Majority "General Setwise Operations") of all three inputs. Note that




```

   gen  =~aFile & (gen << 1);
   return gen ^ a ^ ~b ^ aFile;

```

can be re-written like in following routine:




```

// SIMD bytewise sub a - b
U64 koggeStoneByteSub(U64 a, U64 b) {
   const U64 aFile  = C64(0x0101010101010101);
   U64 gen, pro;
   gen  = a & ~b;      // based on -b = ~b + 1
   pro  = a ^ ~b;
   gen |= aFile & pro; // majority
   gen |= pro   & (gen << 1);
   pro &=         (pro << 1);
   gen |= pro   & (gen << 2);
   pro &=         (pro << 2);
   gen |= pro   & (gen << 4);
   gen  = aFile | (gen << 1);
   return gen ^ a ^ ~b;
}

```

### East Attacks


Here the Kogge-Stone algorithm generates the sliding piece attacks along the empty squares. Generator are the rooks or queens, propagator the empty squares without the A-file to avoid wraps.




```

U64 eastAttacks(U64 occ, U64 rooks) {
   const U64 aFile = C64(0x0101010101010101);
   U64 gen, pro;
   pro  = ~occ  & ~aFile;
   gen  = rooks;
   gen |= pro   & (gen << 1);
   pro &=         (pro << 1);
   gen |= pro   & (gen << 2);
   pro &=         (pro << 2);
   gen |= pro   & (gen << 4);
   gen  =~aFile & (gen << 1);
   return gen;
}

```

The mentioned routines also demonstrate, that this east attacking direction may cheaper implemented with [Fill by Subtraction](Fill_by_Subtraction "Fill by Subtraction") based on [SWAR-wise techniques](SIMD_and_SWAR_Techniques#SWAR "SIMD and SWAR Techniques") and [subtracting a rook from a blocking piece](Subtracting_a_Rook_from_a_Blocking_Piece "Subtracting a Rook from a Blocking Piece"):




```

U64 byteAdd(U64 a, U64 b) {return ((a & ~hFile) + (b & ~hFile)) ^ ((a ^  b) & hFile);}
U64 byteSub(U64 a, U64 b) {return ((a |  hFile) - (b & ~hFile)) ^ ((a ^ ~b) & hFile);}

```

However, due to various left and right shifts, Kogge-Stone can deal with all other seven sliding directions as well.






## See also


* [Parallel prefix MSB](General_Setwise_Operations#parallelPrefixMSB "General Setwise Operations")
* [SWAR population count](Population_Count#SWARPopcount "Population Count") of [the too slow loop approach](Population_Count#TooSlow "Population Count")
* [Flipping and Mirroring](Flipping_Mirroring_and_Rotating#parallelPrefixFlip "Flipping Mirroring and Rotating")
* [Pawn Fills](Pawn_Fills "Pawn Fills")
* [Occupancy of any Line](Occupancy_of_any_Line "Occupancy of any Line")
* [Kogge-Stone Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")


## Publications


* [Peter M. Kogge](Mathematician#PMKogge "Mathematician"), [Harold S. Stone](Mathematician#HSStone "Mathematician") (**1972**). *[A Parallel Algorithm for the Efficient Solution of a General Class of Recurrence Equations](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/PB212080.xhtml)*. Technical Report 25, [Stanford University](Stanford_University "Stanford University")
* [Peter M. Kogge](Mathematician#PMKogge "Mathematician") (**1973**). *Parallel Solution of Recurrence Problems*. Ph.D. thesis, [Stanford University](Stanford_University "Stanford University"), advisor [Harold S. Stone](Mathematician#HSStone "Mathematician"), [pdf](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.2724&rep=rep1&type=pdf)
* [Peter M. Kogge](Mathematician#PMKogge "Mathematician"), [Harold S. Stone](Mathematician#HSStone "Mathematician") (**1973**). *[A Parallel Algorithm for the Efficient Solution of a General Class of Recurrence Equations](https://ieeexplore.ieee.org/document/5009159)*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. C-22, No. 8
* [Richard E. Ladner](Mathematician#RELadner "Mathematician"), [Michael J. Fischer](Mathematician#MJFischer "Mathematician") (**1980**). *[Parallel Prefix Computation](https://dl.acm.org/doi/abs/10.1145/322217.322232?download=true)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 27, No. 4
* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal"), [Larry Rudolph](Mathematician#LRudolph "Mathematician"), [Marc Snir](Mathematician#MSnir "Mathematician") (**1985**). *[The power of parallel prefix](https://www.computer.org/csdl/journal/tc/1985/10/06312202/13rRUy0HYQl)*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. C-34, No. 10
* [Peter Sanders](Peter_Sanders "Peter Sanders"), [Jesper Larsson Träff](http://www.traff-industries.de/) (**2006**). *Parallel Prefix (Scan) Algorithms for MPI*. in EuroPVM/MPI 2006, LNCS, [pdf](http://algo2.iti.uni-karlsruhe.de/sanders/papers/scan.pdf)
* [Carl Burch](Mathematician#CBurch "Mathematician") (**2009**). *[Introduction to parallel & distributed algorithms](http://www.toves.org/books/distalg/)*. On-line Book


## Forum Posts


* [flood fill attack bitboards](https://www.stmintz.com/ccc/index.php?id=252289) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") from [CCC](Computer_Chess_Forums "Computer Chess Forums"), September 15, 2002
* [Re: Hyperbola Quiesscene: hardly any improvement](http://www.talkchess.com/forum/viewtopic.php?start=0&t=25979&start=10) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), January 14, 2009 » [Hyperbola Quintessence](Hyperbola_Quintessence "Hyperbola Quintessence")


## External Links


* [Hardware algorithms for arithmetic modules](http://www.aoki.ecei.tohoku.ac.jp/arith/mg/algorithm.html#fsa_pfx) from the ARITH research group, Aoki lab., [Tohoku University](https://en.wikipedia.org/wiki/Tohoku_University)
* [Prefix sum from Wikipedia](https://en.wikipedia.org/wiki/Prefix_sum)
* [parallel prefix computation](http://www.itl.nist.gov/div897/sqg/dads/HTML/parallelPrefix.html) from [National Institute of Standards and Technology](http://www.nist.gov/index.html)
* [parallel prefix algorithm](http://everything2.com/title/parallel+prefix+algorithm) from [Everything2.com](http://everything2.com/)
* [Charm++ Tutorial - Parallel Prefix Program](http://charm.cs.uiuc.edu/tutorial/ParallelPrefix.htm)
* [Joe Zawinul](Category:Joe_Zawinul "Category:Joe Zawinul"), [Trilok Gurtu](Category:Trilok_Gurtu "Category:Trilok Gurtu") - Orient Express Part1, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Carl Burch](Mathematician#CBurch "Mathematician") (**2009**). *[Introduction to parallel & distributed algorithms](http://www.toves.org/books/distalg/)*. On-line Book
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [See also](#seealso)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Gray Code Conversion](http://aggregate.org/MAGIC/#Gray%20Code%20Conversion) from [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC) by [Hank Dietz](Hank_Dietz "Hank Dietz")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [flood fill attack bitboards](https://www.stmintz.com/ccc/index.php?id=252289) by [Steffan Westcott](Steffan_Westcott "Steffan Westcott") from [CCC](Computer_Chess_Forums "Computer Chess Forums"), September 15, 2002
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Hardware algorithms for arithmetic modules](http://www.aoki.ecei.tohoku.ac.jp/arith/mg/algorithm.html#fsa_pfx) from the ARITH research group, Aoki lab., [Tohoku University](https://en.wikipedia.org/wiki/Tohoku_University)

**[Up one Level](Algorithms "Algorithms")**







 
