---
title: AltiVec
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * [PowerPC](PowerPC "PowerPC") * AltiVec**

**AltiVec**, (Velocity Engine by [Apple](index.php?title=Apple&action=edit&redlink=1 "Apple (page does not exist)") and VMX by [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)"))

a [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") [instruction set](https://en.wikipedia.org/wiki/Instruction_set) designed by Apple, IBM, and [Freescale Semiconductor](https://en.wikipedia.org/wiki/Freescale_Semiconductor) (formerly [Motorola's](index.php?title=Motorola&action=edit&redlink=1 "Motorola (page does not exist)") Semiconductor Products Sector) - the [AIM alliance](https://en.wikipedia.org/wiki/AIM_alliance), introduced with Motorola's [PowerPC G4](PowerPC#G4 "PowerPC"), and Apple's [PowerPC G5](PowerPC#G4 "PowerPC"), now owned by [NXP Semiconductors](https://en.wikipedia.org/wiki/NXP_Semiconductors) and standard part of the [Power ISA v.2.03](https://en.wikipedia.org/wiki/Power_Architecture#Power_ISA_v.2.03). AltiVec features 32 128-bit vector registers that represent [vectors](Array "Array") of either 16 [bytes](Byte "Byte"), eight [16-bit (half) words](Word "Word") or four [32-bit words](Double_Word "Double Word") or [floats](Float "Float"). Most VMX/AltiVec instructions take three register operands. AltiVec has a flexible vector permute instruction (vperm), which can take arbitrary bytes from two source registers and places them in any position in a destination register controlled by an index register <a id="cite-note-1" href="#cite-ref-1">[1]</a>. [GCC](Free_Software_Foundation#GCC "Free Software Foundation") and other compilers provide intrinsics for AltiVec instructions from [C](C "C") or [C++](Cpp "Cpp") source code, or include [auto-vectorization](https://en.wikipedia.org/wiki/Automatic_vectorization) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Bitboards](#bitboards)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Manuals](#manuals)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Bitboards

AltiVec instructions are very well suited for [bitboard](Bitboards "Bitboards") [fill algorithms](Fill_Algorithms "Fill Algorithms") and branchless [move generation](Move_Generation "Move Generation") techniques à la [DirGolem](DirGolem "DirGolem"). Since one 128-bit AltiVec register, keeping up to two [bitboards](Bitboards "Bitboards"), may treated as vector of 16 bytes, shifting techniques such as [one step](General_Setwise_Operations#OneStepOnly "General Setwise Operations") in all eight directions can be done more efficiently with respect to wraps from a- to the h-file or vice versa. North and south shifts by +-8 of each bitboard can be done with one vperm-instruction simultaniously, while west and east shifts can be done by bytewise shift left/right one.

## See also

- [AVX](AVX "AVX") by [Intel](Intel "Intel")
- [AVX2](AVX2 "AVX2") by [Intel](Intel "Intel")
- [AVX-512](AVX-512 "AVX-512") by [Intel](Intel "Intel")
- [MMX](MMX "MMX") on [x86](X86 "X86") and [x86-64](X86-64 "X86-64")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [SSE2](SSE2 "SSE2"), [SSE3](SSE3 "SSE3"), [SSSE3](SSSE3 "SSSE3") and [SSE4](SSE4 "SSE4") on [x86](X86 "X86") and [x86-64](X86-64 "X86-64")
- [XOP](XOP "XOP") by [AMD](AMD "AMD")

## Publications

- [Jon Tyler](http://dblp.uni-trier.de/pers/hd/t/Tyler:Jon), [Jeff Lent](http://dblp.uni-trier.de/pers/hd/l/Lent:Jeff), [Anh Mather](http://dblp.uni-trier.de/pers/hd/m/Mather:Anh), [Huy Nguyen](http://dblp.uni-trier.de/pers/hd/n/Nguyen:Huy) (**1999**). *AltiVec; Bringing Vector Technology to PowerPC Processor Family*. [IPCCC 1999](http://dblp.uni-trier.de/db/conf/ipccc/ipccc1999.html#TylerLMN99), [pdf](https://www.princeton.edu/~rblee/ELE572Papers/AltivecPerm.pdf)
- [Tom Thompson](https://www.linkedin.com/in/tom-thompson-500bb7b) (**1999**). *[AltiVec Revealed](http://www.mactech.com/articles/mactech/Vol.15/15.07/AltiVecRevealed/index.html)*. [MacTech](http://www.mactech.com/), Vol. 15, No. 7
- [Nicolas Fritz](https://www.researchgate.net/profile/Nicolas_Fritz2) (**2009**). *SIMD Code Generation in Data-Parallel Programming*. Ph.D. thesis, [Saarland University](https://en.wikipedia.org/wiki/Saarland_University), [pdf](http://scidok.sulb.uni-saarland.de/volltexte/2009/2563/pdf/Dissertation_9229_Frit_Nico_2009.pdf?q=ibms-cell-processor)

## Manuals

- [AltiVec Technology - Programming Interface Manual](https://www.nxp.com/files-static/32bit/doc/ref_manual/ALTIVECPIM.pdf) (pdf)
- [AltiVec Technology - Programming Environments Manual](https://www.nxp.com/docs/en/reference-manual/ALTIVECPEM.pdf) (pdf)

## Forum Posts

- [G4 & AltiVec](https://www.stmintz.com/ccc/index.php?id=71754) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), October 04, 1999
- [An efficiency comparison data point for x86 vs PowerPC](https://www.stmintz.com/ccc/index.php?id=312343) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 22, 2003

## External Links

- [AltiVec from Wikipedia](https://en.wikipedia.org/wiki/AltiVec)
- [AltiVec Technologies | NXP](https://www.nxp.com/pages/altivec-technologies:DRPPCALTVC) by [NXP Semiconductors](https://en.wikipedia.org/wiki/NXP_Semiconductors)
- [Inside the IBM PowerPC 970 | Part II: The Execution Core](http://archive.arstechnica.com/cpu/03q1/ppc970/ppc970-0.html) by [Jon Stokes](http://arstechnica.com/author/hannibal/), [Ars Technica](https://en.wikipedia.org/wiki/Ars_Technica)
- [Mentor Embedded Performance Library](http://s3.mentor.com/embedded/MEPL/index.xhtml)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Tom Thompson](https://www.linkedin.com/in/tom-thompson-500bb7b) (**1999**). *[AltiVec Revealed](http://www.mactech.com/articles/mactech/Vol.15/15.07/AltiVecRevealed/index.html)*. [MacTech](http://www.mactech.com/), Vol. 15, No. 7
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [AltiVec from Wikipedia](https://en.wikipedia.org/wiki/AltiVec)

**[Up one Level](PowerPC "PowerPC")**

