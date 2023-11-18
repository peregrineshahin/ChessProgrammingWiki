---
title: Bitboard Serialization
---
**[Home](Home "Home") * [Board Representation](Board_Representation "Board Representation") * [Bitboards](Bitboards "Bitboards") * Bitboard Serialization**

[](http://www.mcescher.com/Gallery/back-bmp/LW331.jpg) [M. C. Escher](Category:M._C._Escher "Category:M. C. Escher"), Encounter, 1944 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bitboard Serialization** refers to the transformation of a bitboard with up to 64 one-bits set into a list of up to 64 bit-indices aka [square indices](Squares "Squares") of a [8x8 board](8x8_Board "8x8 Board") - for instance to process [move-target](Target_Square "Target Square") sets for [move generation](Move_Generation "Move Generation"). This is done in two phases, isolating none-empty [subsets](https://en.wikipedia.org/wiki/Subset) and then transforming those more versatile subsets into lists, either bit by bit, by applying a [bisection](https://en.wikipedia.org/wiki/Bisection) scheme, where finally [words](Word "Word") or [bytes](Byte "Byte") may act as index of a pre-calculated database, or by [perfect hashing](Hash_Table#PerfectHashing "Hash Table") of square lists by subsets with a limited maximum popularity, for instance move-target sets of a [king](King "King") or [knight](Knight "Knight") even with [minimal perfect hashing](Hash_Table#MinimalPerfectHashing "Hash Table").

## Isolating Subsets

The process of isolating subsets is performed by [intersection](General_Setwise_Operations#Intersection "General Setwise Operations"), for single populated subsets with the [two's complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations").

## Single Bits

This obvious loop approach is similar to [Brian Kernighan's way](Population_Count#BrianKernighansway "Population Count") to count the number of one-bits by consecutively isolating and clearing the LS1B:

```C++

while ( x ) {
   U64 ls1b = x & -x; // isolate LS1B
   ...
   x &= x-1; // reset LS1B
}

```

or with likely the same generated assembly:

```C++

if ( x ) do {
   U64 ls1b = x & -x; // isolate LS1B
   ...
} while ( x &= x-1 );

```

Of course we may also reset the LS1B by

```C++

   x ^= ls1b; // reset LS1B

```

but todays processors like to gain more parallelism to calculate independent expressions.

## Multiple Bits

Isolating none-empty subsets with possibly multiple one-bits can be applied by [divide and conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm), that is to divide the bitboard or [quad word](Quad_Word "Quad Word") [recursively](Recursion "Recursion") into smaller items, two [double words](Double_Word "Double Word"), consisting of two [words](Word "Word") and those again of two [bytes](Byte "Byte"). Word and byte-wide isolated subsets may then act as an index of a pre-calculated lookup table to convert those subsets to adequate data-structures, most likely lists with up to sixteen or eight elements.

## Converting Sets to Lists

## Square Index Serialization

For most applications LS1B-isolation alone is not appropriate, but the conversion from the exponential bitboard centric world to the scalar square centric world, also called [bit-scanning](BitScan "BitScan").

### Scanning Forward

```C++

if ( x ) do {
   int idx = bitScanForward(x); // square index from 0..63
   *list++ = foo(idx, ...);
} while (x &= x-1); // reset LS1B

```

Per definition bitScanForward reveals the index of LS1B.

### Scanning Reverse

If - for some reason - we like to traverse the sets in reverse or unknown order anyway, we can not (or don't want to) rely on the independent LS1B reset.

```C++

if ( x ) do {
   int idx = bitScanReverse(x); // square index from 0..63
   *list++ = foo(idx, ...);
} while (x ^= powOf2[idx]) ; // or 1ULL << idx -> reset found bit

```

### Scanning with Reset

A win of abstraction is to use a combined [bitscan with reset](BitScan#BitscanwithReset "BitScan") found bit routine. This is fine. But probably harder for compilers to generate optimal code in the if-do-while-sense, where reset last bit already sets the zero-flag. If you don't care on such micro-optimizations, this is the preferred control structure <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

```C++

while ( x ) {
   int idx = bitScanAndReset(&x); // square index from 0..63
   *list++ = foo(idx, ...);
}

```

One may even don't care about the order.

### Intrinsic Version

If bitscan is able to properly handle empty sets - leaving an value outside the 0..63 range (like leading or trailing zero count), we may think about to skip the leading while condition and to break on bitscan(x) > 63 for instance. That was not recommend - since the reset leaves the condition en-passant, and the computational cost of an additional bitscan or zero count was higher. If you like to play the optimization game, it might be fine for [x86-64](X86-64 "X86-64") [Core 2 duo](https://en.wikipedia.org/wiki/Intel_Core_2) thought - using [bitscan](X86-64#gpinstructions "X86-64") and [bittestandreset](X86-64#gpinstructions "X86-64") intrinsics or wrappers - if kept all in registers of course.

```C++

while (_BitScanForward64(&idx, x)) { // or reverse
   *list++ = foo(idx, ...);
   _bittestandreset64(&x, idx);
}

```

The loop is intended to look like this in [x86-64](X86-64 "X86-64") [assembly](Assembly "Assembly"):

```C++

; input rdx - move target set
;       ecx - move from aspects
;       rdi - pointer to movelist
   std           ; set direction flag
   bsf  rax, rdx ; scan first to-bit
   jz   over     ; jump if no more moves
loop:
   btr  rdx, rax ; reset found bit
   or   eax, ecx ; combine to- with from-square
   stosw         ; store 16-bit move *rdi++ = move
   bsf  rax, rdx ; scan next to-bit
   jnz  loop     ; jump if more moves
over:

```

### Black or White

With bitboard serialization one minor problem is the relative order in [move generation](Move_Generation "Move Generation") considering [side to move](Side_to_move "Side to move"). Bsf scans the board in a1..h1, a2..h2, a8..h8 order, assuming [little-endian rank-file mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"), which might be the desired order for an attacking black player. Traversing white pieces and target squares the same way may result in asymmetries and different search behavior of [color flipped positions](Color_Flipping "Color Flipping"). Despite other features considered in [move ordering](Move_Ordering "Move Ordering"), the initial order in generation has more or less influence. Therefore, it is desired to traverse the "white" bitboards with priority for the black back-rank as well <a id="cite-note-3" href="#cite-ref-3">[3]</a> . This might be done by bitscan reverse, which covers the rank symmetry, but also mirrors the files. Another alternative is to traverse a [vertically flipped](Flipping_Mirroring_and_Rotating#FlipVertically "Flipping Mirroring and Rotating") "white" bitboard, which can be done outside the do-while loop by a "conditional" [x86-64](X86-64 "X86-64") [byte swap](X86-64#gpinstructions "X86-64"), and requires one further register and xor per loop cycle, which might be combined with other stuff, f.i. the [from square](Origin_Square "Origin Square") of a move:

```C++

if ( x ) {
   U64 m = (U64)color - 1; // e.g. -1 if white, 0 for black
   int o = (int)m & 56;
   x = x ^ ((x ^ flipVertical(x)) & m); // conditional flip
   do {
      int idx = bitScanForward(x) ^ o; // square index from 0..63
      *list++ = foo(idx , ...);
   } while (x &= x-1); // reset LS1B
}

```

### STL Iterator

[Rein Halbersma](Rein_Halbersma "Rein Halbersma") has written a prototype of a [generic](Generic_Programming "Generic Programming") [C++11](Cpp "Cpp") bitset [template](Cpp#Template "Cpp") that can be used to traverse a set in [STL iterator](https://en.wikipedia.org/wiki/Iterator#C.2B.2B) style, hiding bitscan and reset <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> ...

```C++

typedef bit_set<int64_t, 1> bitset;

void testLoop(int* p, const bitset & x) {
  for (auto it = x.begin(); it != x.end(); ++it)
    *p++ = *it;
}
/* or std::copy */
void testCopy(int* p, const bitset & x) {
  std::copy(x.begin(), x.end(), p); 
}

```

... which yields in following [X86-64](X86-64 "X86-64") [assembly](Assembly "Assembly"), almost identical for the iterator loop and std::copy <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++

; testLoop(int*, bit_set<long, 1ul>):
  test  rsi, rsi
  jne   .L13
.L7:
  ret
.L13:
  bsf   rax, rsi
  mov   DWORD PTR [rdi], eax
  lea   rax, [rsi-1]
  add   rdi, 4
  and   rsi, rax
  jne   .L13
  jmp   .L7

```

## Hashing Multiple Bits

Similar to the idea to hash occupancies in [kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") and [magic bitboards](Magic_Bitboards "Magic Bitboards"), one may hash certain move-target subsets of one piece in one run, to lookup tables with pre-calculated moves-lists <a id="cite-note-7" href="#cite-ref-7">[7]</a> . Sounds like doing up to eight bitscans in parallel. The idea is to muliply-shift-lookup a move-target bitboard, to do an almost branch-less [move-generation](Move_Generation "Move Generation") with pre-calculated moves inside [move-lists](Move_List "Move List"). For instance king- and knight-moves <a id="cite-note-8" href="#cite-ref-8">[8]</a> as well as moves of sliding pieces per line:

```C++

moveTarget = KingAttacks[sq] & ~(ownPieces | attackedSquares);
idx = (moveTarget * kingMagic[sq]) >> kingShift[sq]);
movelists = kingMoveLists[sq];
movelist  = movelists[idx];
moveCpy(target, movelist, movelist->n);

```

A king in a corner may have up to three moves. Thus there are 2^3 == 8 possible move-lists.
For instance for a king on a1 (number of moves: vector of moves):

```C++

0:{empty}
1:{a1-b1}
1:{a1-a2}
1:{a1-b2}
2:{a1-b1,a1-a2}
2:{a1-b1,a1-b2}
2:{a1-a2,a1-b2}
3:{a1-b1,a1-a2,a1-b2}

```

Kings on edges have 5 potential target squares, thus there are 32 possible move-lists. All other kings have 8 all the 8 neighbors with up to 256 move-lists. Similar move-list enumeration is possible with knights and others. All possible move-target subsets of kings and knights for all 64 from-squares are [perfectly minimal hashable](Hash_Table#MinimalPerfectHashing "Hash Table") with a magic factor of four one-bits set. 10016 possible king-move-lists and 5520 knight-move-lists. To reduce memory one may offset the sets to a "normalized" source square per king, knight and sliding piece line, implying some vector arithmetic in the board centric world considering the offset.

The less populated move-target subsets are, the less efficient this hashing technique. This might become a problem since bitboard move-generation is essentially about subsets of moves with certain properties, like most importantly fast winning captures at [Cut-nodes](Node_Types#cut-nodes "Node Types").

## See also

- [Move Generation](Move_Generation "Move Generation")

[Belle | Hardware Move Generation](Belle#Hardware "Belle")

- [Move Ordering](Move_Ordering "Move Ordering")
- [Pieces versus Directions](Pieces_versus_Directions "Pieces versus Directions")
- [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")
- [Traversing Subsets of a Set](Traversing_Subsets_of_a_Set "Traversing Subsets of a Set")

## Forum Posts

## 2000 ...

- [Subject: sliding move generation idea with bitboards](https://www.stmintz.com/ccc/index.php?id=487844) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), February 19, 2006
- [Magic Knight- and King-Move Generation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6099) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), Januar 11, 2007
- [compact bitboard move generator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=19837) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 25, 2008 » [Move Generation](Move_Generation "Move Generation")

## 2010 ...

- [Extracting moves from bitboards](http://www.open-chess.org/viewtopic.php?f=5&t=2228) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 18, 2013
- [Re: C vs ASM](http://www.talkchess.com/forum/viewtopic.php?t=47414&start=4) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), March 05, 2013
- [Symmetric move generation using bitboards](http://www.talkchess.com/forum/viewtopic.php?t=54704) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), December 20, 2014 » [BitScan](BitScan "BitScan")
- [An improvement to classic Chess4.5 style bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70065) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 01, 2019

## External Links

- [Serialization from Wikipedia](https://en.wikipedia.org/wiki/Serialization)
- [The United Jazz + Rock Ensemble](Category:The_United_Jazz_%2B_Rock_Ensemble "Category:The United Jazz + Rock Ensemble") - [Steps of M.C. Escher](https://www.allmusic.com/song/steps-of-mc-escher-mt0012121605), [Live Im Schutzenhaus](https://www.allmusic.com/album/live-im-schutzenhaus-mw0000062412) (1978), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Eberhard Weber](Category:Eberhard_Weber "Category:Eberhard Weber"), [Jon Hiseman](Category:Jon_Hiseman "Category:Jon Hiseman"), [Barbara Thompson](Category:Barbara_Thompson "Category:Barbara Thompson"), [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel"), [Wolfgang Dauner](Category:Wolfgang_Dauner "Category:Wolfgang Dauner"),

[Charlie Mariano](Category:Charlie_Mariano "Category:Charlie Mariano"), [Albert Mangelsdorff](Category:Albert_Mangelsdorff "Category:Albert Mangelsdorff"), [Ian Carr](Category:Ian_Carr "Category:Ian Carr"), [Ack van Rooyen](https://en.wikipedia.org/wiki/Ack_van_Rooyen), [Kenny Wheeler](https://en.wikipedia.org/wiki/Kenny_Wheeler)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Picture gallery "Back in Holland 1941 - 1954"](http://www.mcescher.com/Gallery/gallery-back.htm) from [The Official M.C. Escher Website](http://www.mcescher.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [CPW bitscan with reset could someone explain this line?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70202) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 14, 2019
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Alternatives to History Heuristics](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=289344&t=29611&sid=74848128f12e45f8883a87c3e6729f75) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 02, 2009
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [LiveWorkSpace(IDE online): C++-3.2 (clang++): 41EaZl](http://liveworkspace.org/code/41EaZl$203)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: C vs ASM](http://www.talkchess.com/forum/viewtopic.php?t=47414&start=4) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), March 05, 2013
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [GCC Explorer](http://gcc.godbolt.org/) with g++ 4.7 compiler, options -std=c++11 -O3 -march=k8-sse3 -fverbose-asm
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Subject: sliding move generation idea with bitboards](https://www.stmintz.com/ccc/index.php?id=487844) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), February 19, 2006
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Magic Knight- and King-Move Generation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6099) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), Januar 11, 2007

**[Up one Level](Bitboards "Bitboards")**

