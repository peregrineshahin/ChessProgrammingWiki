---
title: DEC Alpha
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * DEC Alpha**

\[ [Die](Category:Die "Category:Die") photo of the DEC Alpha 21064 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**DEC Alpha**,

a [64-bit](https://en.wikipedia.org/wiki/64-bit_computing) [RISC](https://en.wikipedia.org/wiki/Reduced_instruction_set_computer) processor developed by [Digital Equipment Corporation](Digital_Equipment_Corporation "Digital Equipment Corporation") designed to replace their 32-bit [VAX](VAX "VAX") instruction set. The [21064](https://en.wikipedia.org/wiki/Alpha_21064) was the first Alpha processor introduced as DECchip 21064, code named **EV4**, in February 1992 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, released since September 1992. While Alpha processors were widely used through the 90s in [Workstations](https://en.wikipedia.org/wiki/Workstation) and [Server](https://en.wikipedia.org/wiki/Server_%28computing%29), such as [DEC 3000 AXP](https://en.wikipedia.org/wiki/DEC_3000_AXP), [AlphaStation](https://en.wikipedia.org/wiki/AlphaStation) and [AlphaServer](https://en.wikipedia.org/wiki/AlphaServer), running [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS), [Digital UNIX](Unix#Digital "Unix") and even [Windows NT](Windows "Windows"), [Cray Research](https://en.wikipedia.org/wiki/Cray#Cray_Research_Inc._and_Cray_Computer_Corporation:_1972_to_1996) used the 150 MHz Alpha 21064 in their [Cray T3D](Cray_T3D "Cray T3D") supercomputer.

The Alpha architecture was sold, along with most parts of DEC, to [Compaq](https://en.wikipedia.org/wiki/Compaq) in 1998. Compaq, already an [Intel](Intel "Intel") customer, decided to phase out Alpha in favor of the forthcoming [Itanium](Itanium "Itanium") architecture, and sold all Alpha intellectual property to Intel in 2001 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Architecture

The Alpha 21064 is a [superpipelined](https://en.wikipedia.org/wiki/Instruction_pipeline) dual-issue [superscalar](https://en.wikipedia.org/wiki/Superscalar) microprocessor that executes instructions in-order. It is capable of issuing up to two instructions every clock cycle to four functional units: an integer unit, a floating-point unit (FPU), an address unit, and a branch unit. The integer pipeline is seven stages long, and the floating-point pipeline ten stages. The first four stages of both pipelines are identical and are implemented by the [I-Box](https://en.wikipedia.org/wiki/Alpha_21064#I-box). The 21064 implemented a 43-bit [virtual address](https://en.wikipedia.org/wiki/Virtual_address_space) and a 34-bit [physical address](https://en.wikipedia.org/wiki/Physical_address), and is therefore capable of addressing 8 TiB of [virtual memory](Memory#Virtual "Memory") and 16 GiB of physical memory.

## Data Types

In the Alpha [little-endian](Little-endian "Little-endian") <a id="cite-note-4" href="#cite-ref-4">[4]</a> architecture, a [byte](Byte "Byte") is defined as [octet](https://en.wikipedia.org/wiki/Octet_%28computing%29), a [word](Word "Word") as a 16-bit datum, a [longword](Double_Word "Double Word") as a 32-bit datum, a [quadword](Quad_Word "Quad Word") as a 64-bit datum, and an octaword as a 128-bit datum. Floating-point types are either 32-bit [floats](Float "Float") or 64-bit [doubles](Double "Double"), [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754-1985) as well as VAX floating point format for backward compatibility.

## Register File

The Alpha [instruction set architecture](https://en.wikipedia.org/wiki/Instruction_set) (ISA) defined a set of 32 64-bit integer [registers](https://en.wikipedia.org/wiki/Processor_register) R0 .. R31, and 32 64-bit floating point registers F0 .. F31, where R31 and F31 were not writable and handwired to zero. The 64-bit [program counter](https://en.wikipedia.org/wiki/Program_counter) is longword aligned and incremented by four to the address of the next instruction when an instruction is decoded. A lock flag and locked physical address register are used by the load-locked and store-conditional instructions for multiprocessor support.

## Integer Instructions

The integer arithmetic instructions perform [addition](https://en.wikipedia.org/wiki/Addition), [multiplication](https://en.wikipedia.org/wiki/Multiplication), and [subtraction](https://en.wikipedia.org/wiki/Subtraction) on longwords or quadwords, [comparison](https://en.wikipedia.org/wiki/Relational_operator) on quadwords, and conditional move instructions. Signed and unsigned compare instructions compare two registers or a register and a literal and write '1' to the destination register if the specified condition is true or '0' otherwise. [Bitwise logical](https://en.wikipedia.org/wiki/Bitwise_operation) instructions perform [AND](Combinatorial_Logic#AND "Combinatorial Logic") (Logical Product), [OR](Combinatorial_Logic#OR "Combinatorial Logic") (Logical Sum, BIS), and [XOR](Combinatorial_Logic#XOR "Combinatorial Logic") (Logical Difference), while the instructions with the mnemonics BIC, ORNOT and EQV use the complement of the second source operand. [Shift instructions](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts) perform [arithmetic right shift](https://en.wikipedia.org/wiki/Arithmetic_shift), and [logical shift](https://en.wikipedia.org/wiki/Logical_shift) in both directions.

## Count Extensions

The Count Extensions (CIX) was an integer extension of three instructions for [population count](Population_Count "Population Count") and [bitscan](BitScan "BitScan") purposes, first implemented on the [Alpha 21264A (EV67)](https://en.wikipedia.org/wiki/Alpha_21264#Alpha_21264A) in late 1999 <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

|  Mnemonic
|  Instruction
|
| --- | --- |
|  CTLZ
| [Count Leading Zero](BitScan#LeadingZeroCount "BitScan") |
|  CTPOP
| [Count Population](Population_Count "Population Count") |
|  CTTZ
| [Count Trailing Zero](BitScan#TrailingZeroCount "BitScan") |

## 21164

\[ Die shot of DEC Alpha 21164 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
The [Alpha 21164](https://en.wikipedia.org/wiki/Alpha_21164) (EV5) was introduced in January 1995. It is a four-issue [superscalar](https://en.wikipedia.org/wiki/Superscalar) processor capable of issuing a maximum of four instructions per clock cycle to two integer and two floating-point execution units. The integer [pipeline](https://en.wikipedia.org/wiki/Instruction_pipeline) is seven stages long, and the floating-point pipeline is ten stages long. The 21164 implemented a 43-bit virtual address and a 40-bit physical address. The two integer pipelines, add and multiply, are both capable of executing add, logical, load, compare, and conditional move instructions. The multiply pipeline exclusively executes shift, store, and multiply instructions. The add pipeline exclusively executes branch instructions. The 21164 has three levels of cache, two on-die and one external and optional. The primary cache is split into separate caches for instructions and data, referred to as the I-cache and D-cache respectively. They are 8 KB in size, direct-mapped and have a cache line size of 32 bytes. [Cray Research](https://en.wikipedia.org/wiki/Cray#Cray_Research_Inc._and_Cray_Computer_Corporation:_1972_to_1996) used the 300 MHz Alpha 21164 in their [Cray T3E](Cray_T3E "Cray T3E") supercomputer.

## 21264

The [Alpha 21264](https://en.wikipedia.org/wiki/Alpha_21264) (EV6), introduced in October 1996, is a four-issue [superscalar](https://en.wikipedia.org/wiki/Superscalar) processor with [out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution), [speculative execution](https://en.wikipedia.org/wiki/Speculative_execution) and a seven-stage [instruction pipeline](https://en.wikipedia.org/wiki/Instruction_pipeline). It has a peak execution rate of six [instructions per cycle](https://en.wikipedia.org/wiki/Instructions_per_cycle). The Alpha 21264 has two levels of cache, a primary cache and secondary cache. The three-level cache of the Alpha 21164 was not used due to problems with bandwidth <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Chess Programs

at times running on DEC Alpha

- [Category:DEC Alpha](Category:DEC_Alpha "Category:DEC Alpha")

## See also

- [Cray T3D](Cray_T3D "Cray T3D")
- [Cray T3E](Cray_T3E "Cray T3E")
- [VAX](VAX "VAX")

## Manuals

- [DIGITAL UNIX Documentation - Programming Guides](http://www2.phys.canterbury.ac.nz/dept/docs/manuals/unix/DEC_4.0e_Docs/HTML/PROG_LIB.HTM)
- [Alpha Architecture Reference Manual](http://download.majix.org/dec/alpha_arch_ref.pdf) (pdf) [Compaq](https://en.wikipedia.org/wiki/Compaq)
- [Digital UNIX Assembly Language Programmer's Guide](http://www.cs.cmu.edu/afs/cs/academic/class/15213-f98/doc/alpha-asm.pdf), March 1996 (pdf)

## Publications

- [Richard L. Sites](http://dblp.uni-trier.de/pers/hd/s/Sites:Richard_L=) (**1992**). *Alpha AXP Architecture*. [Digital Technical Journal, Vol. 4](http://dblp.uni-trier.de/db/journals/dtj/dtj4.html), No. 4, [pdf](http://www.hpl.hp.com/hpjournal/dtj/vol4num4/vol4num4art1.pdf)

## Forum Posts

- [Alpha Architecture Technical Summary](https://groups.google.com/d/msg/comp.arch/QB59ace2V8M/pEuccRNGoe8J) by [Jim Gettys](https://en.wikipedia.org/wiki/Jim_Gettys), [comp.arch](https://groups.google.com/forum/#!forum/comp.arch), February 25, 1992
- [Crafty on 767Mhz Alpha at Paris WMCCC?](https://groups.google.com/d/msg/rec.games.chess.computer/d3sYjfVJI7E/0At3bwtgYxgJ) by Richard A. Fowell, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 27, 1997
- [Question to Bob: Crafty , Alpha and FindBit()](https://www.stmintz.com/ccc/index.php?id=20057) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 05, 1998 » [Crafty](Crafty "Crafty"), [BitScan](BitScan "BitScan")

## External Links

- [DEC Alpha from Wikipedia](https://en.wikipedia.org/wiki/DEC_Alpha)
- [Alpha Instruction Set (Brief)](https://www.cs.arizona.edu/projects/alto/Doc/local/alpha.instruction.html)
- [Alpha instruction-set specification](https://www.cs.tufts.edu/~nr/toolkit/specs/alpha.html)
- [Alpha: The History in Facts and Comments](http://alasir.com/articles/alpha_history/index.html) by [Paul V. Bolotoff](http://alasir.com/articles/), April 2005
- [Alpha/FAQ - Gentoo Wiki](https://wiki.gentoo.org/wiki/Alpha/FAQ) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## Processors

- [Alpha 21064 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21064)
- [Alpha 21164 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21164)
- [Alpha 21264 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21264)
- [Alpha 21364 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21364)

## Workstations

- [DEC 3000 AXP from Wikipedia](https://en.wikipedia.org/wiki/DEC_3000_AXP)
- [DECpc AXP 150 from Wikipedia](https://en.wikipedia.org/wiki/DECpc_AXP_150)
- [AlphaStation from Wikipedia](https://en.wikipedia.org/wiki/AlphaStation)

## Server

- [DEC 4000 AXP from Wikipedia](https://en.wikipedia.org/wiki/DEC_4000_AXP)
- [AlphaServer from Wikipedia](https://en.wikipedia.org/wiki/AlphaServer)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Die photo of Alpha AXP 21064, by [Dyl](https://commons.wikimedia.org/wiki/User:Dyl~commonswiki), April 02, 2007, [DEC Alpha from Wikipedia](https://en.wikipedia.org/wiki/DEC_Alpha), [Alpha 21064 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21064), [CC-BY-SA](https://creativecommons.org/licenses/by-sa/2.0/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Alpha Architecture Technical Summary](https://groups.google.com/d/msg/comp.arch/QB59ace2V8M/pEuccRNGoe8J) by [Jim Gettys](https://en.wikipedia.org/wiki/Jim_Gettys), [comp.arch](https://groups.google.com/forum/#!forum/comp.arch), February 25, 1992
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [DEC Alpha from Wikipedia](https://en.wikipedia.org/wiki/DEC_Alpha)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Alpha/FAQ - Is Alpha big endian or little endian?](https://wiki.gentoo.org/wiki/Alpha/FAQ#Is_Alpha_big_endian_or_little_endian.3F)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Question to Bob: Crafty , Alpha and FindBit()](https://www.stmintz.com/ccc/index.php?id=20057) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), June 05, 1998
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> English: Die shot of DEC Alpha 21164 (EV5) microprocessor, by [Pauli Rautakorpi](https://commons.wikimedia.org/wiki/User:Birdman86), 28 June 2013, [Alpha 21164 from Wikipedia](https://en.wikipedia.org/wiki/Alpha_21164), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Alpha 21264 - Cache - Wikipedia](https://en.wikipedia.org/wiki/Alpha_21264#Cache)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Gentoo Linux from Wikipedia](https://en.wikipedia.org/wiki/Gentoo_Linux)

**[Up one Level](Hardware "Hardware")**

