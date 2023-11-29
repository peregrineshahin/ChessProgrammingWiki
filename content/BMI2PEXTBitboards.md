---
title: BMI2PEXTBitboards
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * [x86-64](X86-64 "X86-64") * BMI2**

**BMI2**,

an x86-64 expansion of [bit-manipulation](Bit-Twiddling#BitManipulation "Bit-Twiddling") instructions by [Intel](Intel "Intel"). Like [BMI1](BMI1 "BMI1"), BMI2 employs [VEX prefix](https://en.wikipedia.org/wiki/VEX_prefix) encoding to support three-operand syntax with non-destructive source operands on 32- or 64-bit general-purpose registers. Along with [AVX2](AVX2 "AVX2"), BMI2 was expected to be part of [Intel's](Intel "Intel") [Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) architecture planned for 2013, but was not yet available in one of the first tested Haswell generations of mid 2013 as reported by Andreas Stiller from the German c't magazine <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
BMI2 requires bit 8 set in EBX of [CPUID](https://en.wikipedia.org/wiki/CPUID) with EAX=07H, ECX=0H <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
In 2017, BMI2 was further incorporated in [AMD's](AMD "AMD") [Zen-architecture](<https://en.wikipedia.org/wiki/Zen_(microarchitecture)>) but until [Zen 3](https://en.wikipedia.org/wiki/Zen_3) in November 2020 <a id="cite-note-3" href="#cite-ref-3">[3]</a> with a slow implementation of critical instructions such as [PDEP](#pdep) and [PEXT](#pext) <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>
<a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Instructions

Beside the instructions explained in more detail below, there is MULX, Unsigned Multiply, and RORX, SARX/SHLX/SHRX, that is rotate and shifts without affecting processor flags. PEXT and PDEP <a id="cite-note-7" href="#cite-ref-7">[7]</a> allow for an alternative of [kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards")- or [magic bitboards](Magic_Bitboards "Magic Bitboards"), and clearly makes maintaining [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") obsolete <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## BZHI

Zero High Bits Starting with Specified Bit Position.

```C++
dest ::= src & ((1 << index)-1);

unsigned __int64 _bzhi_u64(unsigned __int64 src, unsigned __int32 index);

```

## PDEP

Parallel Bits Deposit. May be used to map [first rank attacks](First_Rank_Attacks "First Rank Attacks") to any rank, file, or diagonal on the chess board.

### Intrinsic Prototype

```C++
unsigned __int64 pdep_u64(unsigned __int64 src, unsigned __int64 mask);

```

### Sample

```C++
SRC1   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
       │S63│S62│S61│S60│S59│....│ S7│ S6│ S5│ S4│ S3│ S2│ S1│ S0│ 
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

SRC2   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
(mask) │ 0 │ 0 │ 0 │ 1 │ 0 │0...│ 1 │ 0 │ 1 │ 0 │ 0 │ 1 │ 0 │ 0 │  (f.i. 4 bits set)
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

DEST   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
       │ 0 │ 0 │ 0 │ S3│ 0 │0...│ S2│ 0 │ S1│ 0 │ 0 │ S0│ 0 │ 0 │ 
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

```

### Serial Implementation

in [C](C "C") <a id="cite-note-9" href="#cite-ref-9">[9]</a>:

```C++
U64 _pdep_u64(U64 val, U64 mask) {
  U64 res = 0;
  for (U64 bb = 1; mask; bb += bb) {
    if (val & bb)
      res |= mask & -mask;
    mask &= mask - 1;
  }
  return res;
}

```

## PEXT

Parallel Bits Extract. Great to get the [inner six bit](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") occupancy of any rank, file, or diagonal as index of six consecutive lower bit, or the up to 12 bits for a [magic attack lookup](#pextbitboards).

### Intrinsic Prototype

```C++
unsigned __int64 _pext_u64(unsigned __int64 src, unsigned __int64 mask);

```

### Sample

```C++
SRC1   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
       │S63│S62│S61│S60│S59│....│ S7│ S6│ S5│ S4│ S3│ S2│ S1│ S0│ 
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

SRC2   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
(mask) │ 0 │ 0 │ 0 │ 1 │ 0 │0...│ 1 │ 0 │ 1 │ 0 │ 0 │ 1 │ 0 │ 0 │  (f.i. 4 bits set)
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

DEST   ┌───┬───┬───┬───┬───┐    ┌───┬───┬───┬───┬───┬───┬───┬───┐
       │ 0 │ 0 │ 0 │ 0 │ 0 │0...│ 0 │ 0 │ 0 │ 0 │S60│ S7│ S5│ S2│ 
       └───┴───┴───┴───┴───┘    └───┴───┴───┴───┴───┴───┴───┴───┘

```

### Serial Implementation

in [C](C "C") <a id="cite-note-10" href="#cite-ref-10">[10]</a>, quite similar to [PDEP](#pdep) in traversing the mask, and only two expressions, "mask & -mask" and "bb" swapped:

```C++
U64 _pext_u64(U64 val, U64 mask) {
  U64 res = 0;
  for (U64 bb = 1; mask; bb += bb) {
    if ( val & mask & -mask )
      res |= bb;
    mask &= mask - 1;
  }
  return res;
} 

```

## Applications

## PEXT Bitboards

Fancy **PEXT Bitboards** as replacement for [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards"). The relevant up to four ray occupancies are mapped to a dense index range by using the [PEXT](#pext) instruction:

```C++
U64 arrAttacks  [...]; // ~840 KByte all rook and bishop attacks
U64 arrRookMask  [64]; // 10..12 relevant occupancy bits per rook square
U64 arrBishopMask[64]; //  5.. 9 relevant occupancy bits per bishop square
U32 arrRookBase  [64]; // arrAttacks base offset per rook square
U32 arrBishopBase[64]; // arrAttacks base offset per bishop square

U64 rookAttack(U64 occ, enumSquare sq) {
  return arrAttacks[arrRookBase[sq] + _pext_u64(occ, arrRookMask[sq])];
}

U64 bishopAttack(U64 occ, enumSquare sq) {
  return arrAttacks[arrBishopBase[sq] + _pext_u64(occ, arrBishopMask[sq])];
}

```

## PEXT/PDEP Bitboards

An idea for denser sliding attack tables is also using [PDEP](#pdep), dividing the table size of the [PEXT Bitboards](#pextbitboards) by four but some trailing computation. Looking up [16-bit words](Word "Word") instead of bitboards - to get the scattered bits of the up to four ray attacks per square in an extracted form mapped to a 16-bit word, which then becomes the attack bitboard by performing a deposit instruction with an appropriate second mask per square. The technique was introduced by [Zach Wegner](Zach_Wegner "Zach Wegner") in [CCC](CCC "CCC") <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> and implemented by [Ronald de Man](Ronald_de_Man "Ronald de Man") with a table of slightly more than 210 KiB <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>. Ronald's code was tested by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang") using [Stockfish](Stockfish "Stockfish") as testbed, giving promising results <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a>.

## FEN Compression

Concerning the application of [neural network](Neural_Networks "Neural Networks") training, in particular [NNUE training](NNUE#Training "NNUE") with millions of [chess position](Chess_Position "Chess Position") inside a huge file of [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") records,
Lucas Braesch proposed the idea to [compress](https://en.wikipedia.org/wiki/Data_compression) a chess position by a sequence of [PEXT](#pext) instructions,
while the decompression is done by an sequence of corresponding [PDEP](#pdep) instructions <a id="cite-note-17" href="#cite-ref-17">[17]</a>.
This is intended as possible alternative of the [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) as applied in the [PyTorch NNUE](Gary_Linscott#PyTorch_NNUE "Gary Linscott") code by [Gary Linscott](Gary_Linscott "Gary Linscott") <a id="cite-note-18" href="#cite-ref-18">[18]</a>. The table illustrates the layout:

|  Item
|  Bits
|  Definition
|
| --- | --- | --- |
|  occupancy rocc(remaining occupancy)
|  64
|  rocc = white | black
|
|  pext(white, rocc)
|  cnt(rocc)
|  |
|  black = rocc ^ white
|  0
|  |
|  pext(pawns, rocc)
|  cnt(rocc)
|  |
|  pext(knights, rocc)
|  cnt(rocc)
|  rocc ^= pawns
|
|  pext(bishops, rocc)
|  cnt(rocc)
|  rocc ^= bishops
|
|  pext(rooks, rocc)
|  cnt(rocc)
|  rocc ^= rooks
|
|  pext(queens, rocc)
|  cnt(rocc)
|  rocc ^= queens
|
|  kings = rocc
|  0
|  |
|  side to move
|  1
|  |
|  ep
|  1
|  |
|  pext(epSquare, candis)
|  cnt(candis)
|  candis = ((white & pawns & rank4) \<\< 8) | ((black & pawns & rank6) >> 8)
|
|  pext(castler, rooks)
|  cnt(rooks)
|  castler = rooks with castling rights(any color)
|
|  rule50
|  7
|  |

The uncompressed piece placement bitstream is based on the [dense bitboard board-definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
and consists of the [occupancy](Occupancy "Occupancy"), one color bitboard (e.g. White pieces),
and subsequently the piece bitboards of both colors, from pawns, knights, bishops, rooks until queens. King bitboards are redundant,
due to the subsequent [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations") of a remaining occupancy with all mentioned piece bitboards.
Instead of storing the sparsely populated piece bitboards, the compression is due to saving their extracted bits from the remaining occupancy -
with bit size of [population count](Population_Count "Population Count") of the remaining occupancy, rather than 64.
The pseudo code below omits further aspects of a chess position, such as side to move, castling ability, en passant target square and halfmove clock.

```C++
BitStream compress(const U64 * pieceBB, ...) {
  BitStream stream;
  U64 rocc = pieceBB[nWhite] | pieceBB[nBlack];
  stream.write_n_bit(rocc, 64);
  stream.write_n_bit(_pext_u64(pieceBB[nWhite], rocc), popCount(rocc));
  for (pt = nPawn; pt <= nQueen; ++pt) { 
    stream.write_n_bit(_pext_u64(pieceBB[pt], rocc), popCount(rocc));
    rocc ^= pieceBB[pt]; 
  }
  assert (rocc == pieceBB[nKing]);
  // side to move, ep and castling omitted
  return stream;
}

void decompress (const BitStream &stream, U64 * pieceBB, ...) {
  U64 rocc = stream.read_n_bit(64);
  pieceBB[nWhite] = _pdep_u64(stream.read_n_bit(popCount(rocc)), rocc);
  pieceBB[nBlack] = rocc ^ pieceBB[nWhite];
  for (pt = nPawn; pt <= nKing; ++pt) { 
    pieceBB[pt] = _pdep_u64(stream.read_n_bit(popCount(rocc)), rocc);
    rocc ^= pieceBB[pt]; 
  }
  assert (rocc == 0);
  // side to move, ep and castling omitted
}

```

## Syzygy Generator

[Ronald de Man's](Ronald_de_Man "Ronald de Man") generator for [Syzygy Bases](Syzygy_Bases "Syzygy Bases") can take profit of [PDEP](#pdep) and [PEXT](#pext) instructions, or to use their serial implementations to further reduce the size of his already compact [endgame tablebases](Endgame_Tablebases "Endgame Tablebases") <a id="cite-note-19" href="#cite-ref-19">[19]</a>.

## Early PEXT/PDEP Proposal

In late 2006, [Michael Sherwin](Michael_Sherwin "Michael Sherwin") already proposed a **PEXTPDEP** instruction, [Parallel Bits Extract](#pext) controlled by a source mask followed by [Parallel Bits Deposit](#pdep) controlled by a destination mask <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a>.
However, it is not known whether his proposal was recognized by Intel engineers and had any influence on the design of the BMI2 PEXT and PDEP instructions.

## See also

- [AVX](AVX "AVX")
- [AVX2](AVX2 "AVX2")
- [BitScan](BitScan "BitScan")
- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [BMI1](BMI1 "BMI1")
- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
- [TBM](TBM "TBM")

## Forum Posts

## 2006

- [New instruction that intel/amd should add](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5962) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2006 » [Early PEXT/PDEP Proposal](#pextpdepproposal)

## 2011 ...

- [Haswell New Instructions](http://www.talkchess.com/forum/viewtopic.php?t=40333) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), September 09, 2011
- [Bit manipulations using BMI2](http://www.randombit.net/bitbashing/2012/06/22/haswell_bit_permutations.html) by [Jack Lloyd](http://www.randombit.net/), [/ :: bitbashing](http://www.randombit.net/), June 22, 2012
- [PEXT Bitboards](http://www.talkchess.com/forum/viewtopic.php?t=48220) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), June 07, 2013
- [152k rook and bishop attacks using PEXT and PDEP](http://www.talkchess.com/forum/viewtopic.php?t=49611) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), October 06, 2013
- [Stockfish haswell optimized build](http://www.talkchess.com/forum/viewtopic.php?t=51879) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), April 06, 2014 » [Stockfish](Stockfish "Stockfish")

## 2015 ...

- [smaller tables for PEXT-style attack getters](http://www.talkchess.com/forum/viewtopic.php?t=58910) by [Wylie Garvin](index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](CCC "CCC"), January 13, 2016
- [BMI2 intrinsics in gcc](http://www.talkchess.com/forum/viewtopic.php?t=63978) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), May 14, 2017
- [Ryzen Fritz Chess Benchmarks ?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32016) by ralunger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2017
- [Ryzen and BMI2: Strange behavior and high latencies](https://www.reddit.com/r/Amd/comments/60i6er/ryzen_and_bmi2_strange_behavior_and_high_latencies/) by DonnieTinyHands, [Reddit](https://en.wikipedia.org/wiki/Reddit), March 20, 2017 » [AMD](AMD "AMD"), [BMI2 PEXT](#pext)
- [BMI2 PEXT idea for attacks generation](http://www.talkchess.com/forum/viewtopic.php?t=65191) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), September 16, 2017
- [Re: Komodo 11.3](http://www.talkchess.com/forum/viewtopic.php?t=66737&start=4) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), March 04, 2018 » [AMD](AMD "AMD"), [BMI2 PEXT](#pext), [Komodo 11.3](Komodo#11 "Komodo")
- [Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), May 13, 2018 » [AMD](AMD "AMD")

[Re: Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432&start=12) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), May 18, 2020 » [AVX2](AVX2 "AVX2")

- [AMD BMI2 question](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70167) by Leo, [CCC](CCC "CCC"), March 10, 2019 » [AMD](AMD "AMD")
- [PEXT/PDEP are even slower than you think on Zen](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72538) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 09, 2019 » [AMD](AMD "AMD")

## 2020 ...

- [Re: Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432&start=12) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), May 18, 2020 » [AMD](AMD "AMD"), [AVX2](AVX2 "AVX2")
- [New AMD Zen 3 and Ryzen processors](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75333) by mmt, [CCC](CCC "CCC"), October 09, 2020

[Re: New AMD Zen 3 and Ryzen processors](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75333&start=8) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 11, 2020 » [Early PEXT/PDEP Proposal](#pextpdepproposal)

- [Zen3 supports fast PEXT aka BMI2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75691) by [Alayan Feh](index.php?title=Alayan_Feh&action=edit&redlink=1 "Alayan Feh (page does not exist)"), [CCC](CCC "CCC"), November 05, 2020 » [AMD](AMD "AMD")
- [FEN compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76892) by lucasart, [CCC](CCC "CCC"), March 17, 2021 » [FEN Compression](#fen-compression), [NNUE Training](NNUE#Training "NNUE")
- [pdep/pext for 128-bit integers and bit-arrays](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78804) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 03, 2021

## External Links

- [Bit Manipulation Instruction Sets from Wikipedia](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets)
- [Bit manipulations using BMI2 — bitbashing](http://www.randombit.net/bitbashing/2012/06/22/haswell_bit_permutations.html), June 22, 2012
- [Haswell Instructions Latency](http://users.atw.hu/instlatx64/GenuineIntel00306C3_Haswell_InstLatX64.txt)
- [Intel Intrinsics Guide](http://software.intel.com/sites/landingpage/IntrinsicsGuide/)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Andreas Stiller](http://de.linkedin.com/pub/andreas-stiller/a/381/aa9) (**2013**). *[Der Rechenkünstler](http://www.heise.de/ct/inhalt/2013/14/114/)*. [c't Magazin für Computertechnik](http://www.heise.de/ct/) 14/2013, p. 114-119 (German)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [How to detect New Instruction support in the 4th generation Intel® Core™ processor family | Intel® Developer Zone](http://software.intel.com/en-us/articles/how-to-detect-new-instruction-support-in-the-4th-generation-intel-core-processor-family) by [Max Locktyukhin](http://software.intel.com/de-de/user/76418), August 05, 2013
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Zen3 supports fast PEXT aka BMI2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75691) by [Alayan Feh](index.php?title=Alayan_Feh&action=edit&redlink=1 "Alayan Feh (page does not exist)"), [CCC](CCC "CCC"), November 05, 2020
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Ryzen Fritz Chess Benchmarks ?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32016) by ralunger, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2017
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Ryzen and BMI2: Strange behavior and high latencies](https://www.reddit.com/r/Amd/comments/60i6er/ryzen_and_bmi2_strange_behavior_and_high_latencies/) by DonnieTinyHands, [Reddit](https://en.wikipedia.org/wiki/Reddit), March 20, 2017 » [AMD](AMD "AMD"), [BMI2 PEXT](#pext)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: AMD Announces a Red October: Zen 3 on October 8, RDNA2 on October 28](https://www.techpowerup.com/forums/threads/amd-announces-a-red-october-zen-3-on-october-8-rdna2-on-october-28.271981/page-2#post-4344965) by dragontamer5788, [TechPowerUp Forum](https://www.techpowerup.com/forums/), September 9, 2020
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Ruby Lee](http://www.informatik.uni-trier.de/~ley/pers/hd/l/Lee:Ruby_B=), [Zhijie Shi](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Shi:Zhijie_Jerry.html), [Xiao Yang](http://www.informatik.uni-trier.de/~ley/pers/hd/y/Yang:Xiao.html) (**2001**). *Efficient Permutation Instructions for Fast Software Cryptography*. Micro, IEEE, Vol. 21, No. 6, [pdf](http://palms.ee.princeton.edu/PALMSopen/lee01efficient.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Haswell New Instructions](http://www.talkchess.com/forum/viewtopic.php?t=40333) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), September 09, 2011
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: PEXT Bitboards](http://www.talkchess.com/forum/viewtopic.php?t=48220&start=1) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), June 07, 2013
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: PEXT Bitboards](http://www.talkchess.com/forum/viewtopic.php?t=48220&start=2) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), June 07, 2013
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Haswell New Instructions](http://www.talkchess.com/forum/viewtopic.php?t=40333) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), September 09, 2011
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Haswell New Instructions](http://www.talkchess.com/forum/viewtopic.php?t=40333&start=12) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), September 12, 2011
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: 152k rook and bishop attacks using PEXT and PDEP](http://www.talkchess.com/forum/viewtopic.php?t=49611&start=1) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 06, 2013
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [tb/src/bmi2.h at master · syzygy1/tb · GitHub](https://github.com/syzygy1/tb/blob/master/src/bmi2.h) by [Ronald de Man](Ronald_de_Man "Ronald de Man")
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Re: Stockfish haswell optimized build](http://www.talkchess.com/forum/viewtopic.php?t=51879&start=2) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), April 06, 2014
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Stockfish/src/bitboard.h at bmi2 · jromang/Stockfish · GitHub](https://github.com/jromang/Stockfish/blob/bmi2/src/bitboard.h#L255) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang")
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Re: FEN compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76892&start=3) by lucasart, [CCC](CCC "CCC"), March 17, 2021 » [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation"), [NNUE Training](NNUE#Training "NNUE")
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [nnue-pytorch/nnue_training_data_formats.h at master · glinscott/nnue-pytorch · GitHub](https://github.com/glinscott/nnue-pytorch/blob/master/lib/nnue_training_data_formats.h#L6405)
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Re: PEXT Bitboards](http://www.talkchess.com/forum/viewtopic.php?t=48220&start=1) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), June 07, 2013
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [New instruction that intel/amd should add](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5962) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2006
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Re: New AMD Zen 3 and Ryzen processors](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75333&start=8) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 11, 2020

**[Up one Level](X86-64 "X86-64")**

