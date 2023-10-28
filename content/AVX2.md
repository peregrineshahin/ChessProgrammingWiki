---
title: AVX2
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * [x86](X86 "X86") * AVX2**

**Advanced Vector Extensions 2** (AVX2) is an expansion of the [AVX](AVX "AVX") instruction set. Support for 256-bit expansions of the [SSE2](SSE2 "SSE2") 128-bit integer instructions will be added in AVX2, which was along with [BMI2](BMI2 "BMI2") part of [Intel's](Intel "Intel") [Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29) architecture in 2013, and since 2015, of [AMD's](AMD "AMD") [Excavator](https://en.wikipedia.org/wiki/Excavator_%28microarchitecture%29) microarchitecture.

## Contents

- [1 Features](#features)
- [2 Individual Vector Shifts](#individual-vector-shifts)
- [3 Applications](#applications)
  - [3.1 Knight Attacks](#knight-attacks)
  - [3.2 Dumb7Fill](#dumb7fill)
  - [3.3 Bitboard Permutation](#bitboard-permutation)
  - [3.4 Vertical Nibble](#vertical-nibble)
- [4 See also](#see-also)
- [5 SIMD](#simd)
- [6 Publications](#publications)
- [7 Manuals](#manuals)
- [8 Forum Posts](#forum-posts)
- [9 External Links](#external-links)
- [10 References](#references)

## Features

Beside expanding most integer AVX instructions to 256 bit, AVX2 has 3-operand general-purpose bit manipulation and multiply, [vector shifts](AVX2#IndividualShifts "AVX2"), [Double](Double_Word "Double Word")- and [Quad Word](Quad_Word "Quad Word")-granularity any-to-any permutes, and 3-operand [fused multiply-accumulate](https://en.wikipedia.org/wiki/FMA_instruction_set) support. An important catch is that not all of the instructions are simply generalizations of their 128-bit equivalents: many work "in-lane", applying the same 128-bit operation to each 128-bit half of the register instead of a 256-bit generalization of the operation. For example:

|  Set
|  Instruction
|  Result
|
| --- | --- | --- |
|  AVX
| **vpunpckldq** xmm0, ABCD, EFGH
|  xmm1 := AEBF
|
|  AVX2
| **vpunpckldq** ymm0, ABCDEFGH, IJKLMNOP
|  xmm1 := AIBJEMFN
|

If vpunpckldq had been expanded in the more intuitive fashion, the result of the AVX2 operation would be AIBJCKDL. The reason for this design might be to allow AVX to be implemented more easily with two separate 128-bit arithmetic units.

Some AVX2 instructions, such as type conversion instructions, take both xmm and ymm registers as arguments. For example:

|  Set
|  Instruction
|  Operation
|
| --- | --- | --- |
|  AVX
| **vpmovzxbw** xmm1, xmm2/m64
|  xmm1 := Packed_Zero_Extend_Byte_To_Word(xmm2/m64)
|
|  AVX2
| **vpmovzxbw** ymm1, xmm2/m128
|  ymm1 := Packed_Zero_Extend_Byte_To_Word(xmm2/m128)
|

## Individual Vector Shifts

With AVX2 each data element, such as a [bitboard](Bitboards "Bitboards") of a [quad-bitboard](Quad-Bitboards "Quad-Bitboards"), may be shifted left or right individually, as specified by the second source operand, with following [Assembly](Assembly "Assembly") [mnemonics](https://en.wikipedia.org/wiki/Assembly_language#Opcode_mnemonics_and_extended_mnemonics) and [C](C "C") intrinsic equivalents:

|  Instruction
|  Description
|  Intrinsic
|
| --- | --- | --- |
| **VPSRLVQ** ymm1, ymm2, ymm3/m256
|  Variable Bit Shift Right Logical
|  \_m256i [\_mm256_srlv_epi64](https://software.intel.com/en-us/node/695103) (\_m256i m, \_m256i count)
|
| **VPSLLVQ** ymm1, ymm2, ymm3/m256
|  Variable Bit Shift Left Logical
|  \_m256i [\_mm256_sllv_epi64](https://software.intel.com/en-us/node/695097) (\_m256i m, \_m256i count)
|

## Applications

With an appropriate [quad-bitboard](Quad-Bitboards "Quad-Bitboards") class, one may generate attacks of up to four different [directions](Direction "Direction") using [individual shifts](AVX2#IndividualShifts "AVX2"), for instance [knight attacks](Knight_Pattern#Calculation "Knight Pattern") or [sliding piece attacks](Sliding_Piece_Attacks#Multiple "Sliding Piece Attacks") with [Dumb7Fill](Dumb7Fill "Dumb7Fill") to generate all [positive](On_an_empty_Board#PositiveRays "On an empty Board") or [negative sliding ray attacks](On_an_empty_Board#NegativeRays "On an empty Board") passing two times orthogonal and diagonal sliding pieces.

|  |  |
| --- | --- |
| [Cpwmappinghint.JPG](Square_Mapping_Considerations "Square Mapping Considerations")  | *Code samples and bitboard diagrams rely on [Little endian file and rank mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")*.
|

## Knight Attacks

```

        noNoWe    noNoEa
            +15  +17
             |     |
noWeWe  +6 __|     |__+10  noEaEa
              \   /
               >0<
           __ /   \ __
soWeWe -10   |     |   -6  soEaEa
             |     |
            -17  -15
        soSoWe    soSoEa

```

```

QBB noEaEa_noNoEa_noNoWe_noWeWe(U64 knights) {
   const QBB qmask  (notAB, notA,notH,notGH);
   const QBB qshift (10,17,15,6);
   QBB qknights (knights);
   return (qknights << qshift) & qmask;
}

QBB soWeWe_soSoWe_soSoEa_soEaEa(U64 knights) {
   const QBB qmask  (notGH,notH,notA,notAB);
   const QBB qshift (10,17,15,6);
   QBB qknights (knights);
   return (qknights >> qshift) & qmask;
}

```

## Dumb7Fill

```

  northwest    north   northeast
  noWe         nort         noEa
          +7    +8    +9
              \  |  /
  west    -1 <-  0 -> +1    east
              /  |  \
          -9    -8    -7
  soWe         sout         soEa
  southwest    south   southeast

```

```

QBB east_nort_noWe_noEa_Attacks(QBB qsliders {rq,rq,bq,bq}, U64 empty) {
   const QBB qmask  (notA,-1,notH,notA);
   const QBB qshift (1,8,7,9);
   QBB qflood (sliders);
   QBB qempty  = QBB(empty) & qmask;
   qflood |= qsliders = (qsliders << qshift) & qempty;
   qflood |= qsliders = (qsliders << qshift) & qempty;
   qflood |= qsliders = (qsliders << qshift) & qempty;
   qflood |= qsliders = (qsliders << qshift) & qempty;
   qflood |= qsliders = (qsliders << qshift) & qempty;
   qflood |=            (qsliders << qshift) & qempty;
   return               (qflood   << qshift) & qmask  
}

QBB west_sout_soEa_soWe_Attacks(QBB qsliders {rq,rq,bq,bq}, U64 empty) {
   const QBB qmask  (notH,-1, notA,notH);
   const QBB qshift (1,8,7,9);
   QBB qflood (sliders);
   QBB qempty  = QBB(empty) & qmask;
   qflood |= qsliders = (qsliders >> qshift) & qempty;
   qflood |= qsliders = (qsliders >> qshift) & qempty;
   qflood |= qsliders = (qsliders >> qshift) & qempty;
   qflood |= qsliders = (qsliders >> qshift) & qempty;
   qflood |= qsliders = (qsliders >> qshift) & qempty;
   qflood |=            (qsliders >> qshift) & qempty;
   return               (qflood   >> qshift) & qmask  
}

```

## Bitboard Permutation

For each [bitboard](Bitboards "Bitboards") in a destination [quad-bitboard](Quad-Bitboards "Quad-Bitboards"), the Qwords Element Permutation (**VPERMQ**) instruction <a id="cite-note-1" href="#cite-ref-1">[1]</a> selects one bitboard of a source quad-bitboard. This permits a bitboard in the source operand to be copied to multiple locations in the destination.

```

 destQBB.bb[0] = sourceQBB.bb[ (imm8 >> 0) & 3 ]
 destQBB.bb[1] = sourceQBB.bb[ (imm8 >> 2) & 3 ]
 destQBB.bb[2] = sourceQBB.bb[ (imm8 >> 4) & 3 ]
 destQBB.bb[3] = sourceQBB.bb[ (imm8 >> 6) & 3 ]

```

## Vertical Nibble

Following code extracts the [piece-code](Pieces#PieceCoding "Pieces") as "[vertical nibble](Quad-Bitboards#getPiece "Quad-Bitboards")" from a [quad-bitboard](Quad-Bitboards "Quad-Bitboards") as [board representation](Board_Representation "Board Representation") inside a register, "indexed" by square. The idea is to shift the square bits to the leftmost bit, the [sign bit](https://en.wikipedia.org/wiki/Sign_bit) of each bitboard, to perform the *VPMOVMSKB* instruction to get the sign bits of all 32 bytes into a general purpose register. Unfortunately, there is no *VPMOVMSKQ* to get only the signs of four bitboards, so some more masking and mapping is required to get the four-bit piece code ...

```

int getPiece (__m256i qbb, U64 sq) {
   __m128i  shift = _mm_cvtsi32x_si128( sq ^ 63 ); /* left shift amount 63-sq */
   qbb  =  _mm256_sll_epi64( qbb, shift ); /* squares to signs */
   uint32   qbbsigns = _mm256_movemask_epi8( qbb );  /* get sign bits of 32 bytes */
   return ((qbbsigns & 0x80808080) * 0x00204081) >> 28; /* mask, nibble-map, shift */
}

```

... using these intrinsics ...

- [\_mm_cvtsi64x_si128](http://msdn.microsoft.com/en-us/library/6xsd2b20%28v=vs.100%29.aspx)
- [\_mm256_sll_epi64](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text=_mm256_sll_epi64&techs=AVX2)
- [\_mm256_movemask_epi8](https://software.intel.com/en-us/node/695113)

... with seven [assembly](Assembly "Assembly") instructions intended, assuming the quad-bitboard passed in ymm0 and the square in rcx

```

  xor       rcx, 63          ; left shift amount 63-sq
  movd      xmm6, rcx        ; shift amount via xmm
  vpsllq    ymm6, ymm0, xmm6 ; squares to signs
  vpmovmskb eax, ymm6        ; get sign bits of 32 bytes
  and       eax, 0x80808080  ; mask the four bitboard sign bits
  imul      eax, 0x00204081  ; map them to the upper nibble
  shr       eax, 28          ; nibble as piece code

```

## See also

- [CFish - AVX2 Attacks](CFish#AVX2_Attacks "CFish")
- [DirGolem](DirGolem "DirGolem")
- [NNUE](NNUE "NNUE")
- [Pigeon](Pigeon "Pigeon")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")

## SIMD

- [AltiVec](AltiVec "AltiVec")
- [AVX](AVX "AVX")
- [AVX-512](AVX-512 "AVX-512")
- [BMI2](BMI2 "BMI2")
- [MMX](MMX "MMX")
- [SSE](SSE "SSE")
- [SSE2](SSE2 "SSE2")
- [SSE3](SSE3 "SSE3")
- [SSSE3](SSSE3 "SSSE3")
- [SSE4](SSE4 "SSE4")

## Publications

- [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), [Nathan Kurz](http://dblp.uni-trier.de/pers/hd/k/Kurz:Nathan), [Daniel Lemire](https://github.com/lemire) (**2016**). *Faster Population Counts Using AVX2 Instructions*. [arXiv:1611.07612](https://arxiv.org/abs/1611.07612) <a id="cite-note-2" href="#cite-ref-2">[2]</a> » [AVX-512](AVX-512 "AVX-512"), [Population Count](Population_Count "Population Count")
- [Wojciech Muła](Wojciech_Mu%C5%82a "Wojciech Muła"), [Daniel Lemire](https://github.com/lemire) (**2017**). *Faster Base64 Encoding and Decoding Using AVX2 Instructions*. [arXiv:1704.00605](https://arxiv.org/abs/1704.00605) » [Base64](https://en.wikipedia.org/wiki/Base64)
- [Mathias Gottschlag](https://os.itec.kit.edu/21_3247.php), [Frank Bellosa](https://os.itec.kit.edu/21_31.php) (**2018**). *[Mechanism to Mitigate AVX-Induced Frequency Reduction](https://os.itec.kit.edu/21_3486.php)*. [arXiv:1901.04982](https://arxiv.org/abs/1901.04982)
- [Mathias Gottschlag](https://os.itec.kit.edu/21_3247.php), [Philipp Machauer](https://os.itec.kit.edu/97_3742.php), [Yussuf Khalil](https://os.itec.kit.edu/21_3571.php), [Frank Bellosa](https://os.itec.kit.edu/21_31.php) (**2021**). *[Fair Scheduling for AVX2 and AVX-512 Workloads](https://www.usenix.org/conference/atc21/presentation/gottschlag)*. [USENIX ATC '21](https://www.usenix.org/conference/atc21)

## Manuals

- [Intel® Architecture Instruction Set Extensions Programming Reference](https://software.intel.com/sites/default/files/managed/c5/15/architecture-instruction-set-extensions-programming-reference.pdf) (pdf)
- [Intel® 64 and IA-32 Architectures Optimization Reference Manual](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-optimization-manual.pdf) (pdf)

## Forum Posts

- [Does Hyperthreading have trouble with AVX?](https://stackoverflow.com/questions/30330013/does-hyperthreading-have-trouble-with-avx) by cmylin, [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), May 19, 2015 » [Thread](Thread "Thread")
- [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum3/viewtopic.php?t=65466&start=7) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), October 16, 2017 » [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Re: Ryzen 2 and BMI2?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67432&start=12) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), May 18, 2020 » [AMD](AMD "AMD"), [BMI2](BMI2 "BMI2")
- [AVX2 optimized SF+NNUE and processor temperature](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75008) by corres, [CCC](CCC "CCC"), September 05, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
- [Regarding AVX2](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78588) by [Rebel](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 03, 2021 » [NNUE](NNUE "NNUE")

## External Links

- [Advanced Vector Extensions 2 from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#Advanced_Vector_Extensions_2)
- [Overview: Intrinsics for Intel® Advanced Vector Extensions 2 (Intel® AVX2) Instructions | Intel® Software](https://software.intel.com/en-us/node/523876)
- [Intel Intrinsics Guide - AVX2](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#techs=AVX2)
- [Intel Software Development Emulator](http://software.intel.com/en-us/articles/intel-software-development-emulator/), which can be used to experiment with AVX and AVX2 on a CPU that doesn't support them.
- [Stop the instruction set war](http://www.agner.org/optimize/blog/read.php?i=25) by [Agner Fog](http://www.agner.org/)
- [Processing Arrays of Bits with Intel® Advanced Vector Extensions 2 (Intel® AVX2) | Intel® Developer Zone](https://software.intel.com/en-us/blogs/2013/05/17/processing-arrays-of-bits-with-intel-advanced-vector-extensions-2-intel-avx2) by [Thomas Willhalm](https://software.intel.com/en-us/user/123920), May 17, 2013
- [Haswell Instructions Latency](http://users.atw.hu/instlatx64/GenuineIntel00306C3_Haswell_InstLatX64.txt)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> \_m256i [\_mm256_permute4x64_epi64](https://software.intel.com/en-us/node/683670)(\_m256i val, const int control)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [sse-popcount/popcnt-avx512-harley-seal.cpp at master · WojciechMula/sse-popcount · GitHub](https://github.com/WojciechMula/sse-popcount/blob/master/popcnt-avx512-harley-seal.cpp)

**[Up one Level](X86 "X86")**

