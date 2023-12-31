---
title: X86CCompiler
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* x86**



[ [Die](https://en.wikipedia.org/wiki/Die_%28integrated_circuit%29) shot of [Intel](Intel "Intel") 80386 DX-25 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**x86**,   

referring the [IA-32](https://en.wikipedia.org/wiki/IA-32) architecture of the 32-bit instruction set of the [Intel](Intel "Intel") [80386](https://en.wikipedia.org/wiki/Intel_80386) processor released in 1985 - the successor of Intel's 16-bit [8086](8086 "8086") until [80286](index.php?title=80286&action=edit&redlink=1 "80286 (page does not exist)") processors. x86-32 could address up to 4GByte physical [memory](Memory "Memory"), had virtual memory pages and a mode to protect them over process boundaries - a requirement for multitasking operating systems, despite 16-bit [MS-DOS](MS-DOS "MS-DOS") was still popular. While the initial x86 was [Complex Instruction Set Computing](https://en.wikipedia.org/wiki/Complex_instruction_set_computer) (CISC), the [RISC](https://en.wikipedia.org/wiki/Reduced_instruction_set_computer) versus CISC issue had become indistinct with more recent x86 processors, internally processing RISC like micro opcode. Over the time, modern architectural features, such as [Out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution), [Pipelining](https://en.wikipedia.org/wiki/Instruction_pipeline), [Register Renaming](https://en.wikipedia.org/wiki/Register_renaming) and [Branch Predication](https://en.wikipedia.org/wiki/Branch_predication) became an issue. 80386 was once clocked by about 25MHz. The [RAM](Memory#RAM "Memory") access speed could not keep up with higher and higher clock frequency of later processors - small but faster [cache memory](https://en.wikipedia.org/wiki/CPU_cache) became necessary and strategies to make them efficient, nowadays even with three cache levels with different size and speed. 


*see [x86-64](X86-64 "X86-64") for x86 64-bit*




## Architectures


While the 80386 represented the third microarchitecture (after 8086, [80286](https://en.wikipedia.org/wiki/80286)), [80486](https://en.wikipedia.org/wiki/Intel_80486) and Pentium were the fourth and fifth, later called [P5 microarchitecture](https://en.wikipedia.org/wiki/P5_%28microarchitecture%29). In 1995 with [Pentium Pro](https://en.wikipedia.org/wiki/Pentium_Pro), Intel introduced the [P6 microarchitecture](https://en.wikipedia.org/wiki/Intel_P6_%28microarchitecture%29), eventually revived in the [Pentium M](https://en.wikipedia.org/wiki/Pentium_M) line of microprocessors and the predecessor of Intel's [Core 2 microarchitecture](https://en.wikipedia.org/wiki/Intel_Core_2). Intel's [NetBurst](https://en.wikipedia.org/wiki/Intel_NetBurst_%28microarchitecture%29) microarchitecture with the advent of the [Pentium 4](https://chessprogramming.wikispaces.com/Pentium+4) processor, was famous for its clock speed, but no good reputation by most chess programmers, who favored the [AMD](AMD "AMD") K6- and K7-architecture, namely the [Athlon](https://en.wikipedia.org/wiki/Athlon) processor at that time. To begin with the rebirth of P6 and [Intel Core 2](https://en.wikipedia.org/wiki/Intel_Core_2) architecture in 2006, things changed in favor to Intel again. In November 2008 the [Nehalem](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) microarchitecture appeared.


Intel's [IA-64](https://en.wikipedia.org/wiki/IA-64) architecture is a complete new and incompatible instruction set to IA-32. It is used by the [Itanium](Itanium "Itanium") line of processors. The backward compatible 64-bit successor was designed by [AMD](AMD "AMD") with the advent of Hammer or AMD64, later cloned by Intel and together referred to the [x86-64](X86-64 "X86-64") architecture.



## Register Files


x86 has eight 32-bit general purpose registers:



### General Purpose


The eight general purpose registers may be treated as 32-bit [Double Word](Double_Word "Double Word"), 16-bit [Word](Word "Word") and high and low [Byte](Byte "Byte"):





|  32
 |  16
 |  8 high
 |  8 low
 |  Purpose
 |
| --- | --- | --- | --- | --- |
|  EAX
 |  AX
 |  AH
 |  AL
 |  GP, Accumulator
 |
|  EBX
 |  BX
 |  BH
 |  BL
 |  GP, Index Register
 |
|  ECX
 |  CX
 |  CH
 |  CL
 |  GP, Counter, variable shift, rotate via CL
 |
|  EDX
 |  DX
 |  DH
 |  DL
 |  GP, high Accumulator mul/div
 |
|  ESI
 |  SI
 |  -
 |  -
 |  GP, Source Index
 |
|  EDI
 |  DI
 |  -
 |  -
 |  GP, Destination Index
 |
|  ESP
 |  SP
 |  -
 |  -
 | [Stack Pointer](Stack "Stack") |
|  EBP
 |  BP
 |  -
 |  -
 |  GP, Base Pointer
 |


### MMX


[MMX](MMX "MMX") was introduced with [Pentium MMX](index.php?title=Intel_P5_(microarchitecture)&action=edit&redlink=1 "Intel P5 (microarchitecture) (page does not exist)") in 1996, adopted by [AMD's](AMD "AMD") [K6](https://en.wikipedia.org/wiki/AMD_K6) in 1997.
Eight 64-bit MMX-Registers: **MM0** - **MM7**.
Treated as [Double](Double "Double") or [Quad Word](Quad_Word "Quad Word"), [vector](Array "Array") of two [Floats](Float "Float") or [Double Words](Double_Word "Double Word"), and as vector if four [Words](Word "Word") or eight [Bytes](Byte "Byte").



### 3DNow!


An MMX-floating point extension by [AMD](AMD "AMD"), introduced in the [K6-2](https://en.wikipedia.org/wiki/AMD_K6-2) processor, 1998.
It uses the eight 64-bit **MMX**-Registers: **MM0** - **MM7**.



### SSE/SSE2


SSE was introduced by [Pentium III](https://en.wikipedia.org/wiki/Pentium_III) in 1997, [SSE2](SSE2 "SSE2") by [Pentium 4](https://chessprogramming.wikispaces.com/Pentium+4) in 2000
Eight 128-bit **XMM**-Registers: **XMM0** - **XMM7**.
Treated as [vector](Array "Array") of two [Doubles](Double "Double") (SSE) or [Quad Words](Quad_Word "Quad Word") (SSE2), as vector of four [Floats](Float "Float") (SSE) or [Double Words](Double_Word "Double Word") (SSE2), and as vector if eight [Words](Word "Word") (SSE2) or 16 [Bytes](Byte "Byte") (SSE2).



## CPUS


### Intel


[ Pentium with P54C core <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [80386](https://en.wikipedia.org/wiki/Intel_80386) 1985
* [80486](https://en.wikipedia.org/wiki/Intel_80486) 1989
* [Pentium](https://en.wikipedia.org/wiki/Pentium) 1993
* [Pentium MMX](https://en.wikipedia.org/wiki/Pentium_MMX) 1993
* [P6 microarchitecture](https://en.wikipedia.org/wiki/Intel_P6)
	+ [Pentium Pro](https://en.wikipedia.org/wiki/Pentium_Pro) 1995
	+ [Pentium II](https://en.wikipedia.org/wiki/Pentium_II) 1997
	+ [Pentium III](https://en.wikipedia.org/wiki/Pentium_III) 1999
* [NetBurst microarchitecture](https://en.wikipedia.org/wiki/NetBurst)
	+ [Pentium 4](https://chessprogramming.wikispaces.com/Pentium+4) 2000
* [Intel Core microarchitecture](https://en.wikipedia.org/wiki/Intel_Core_microarchitecture)
	+ [Pentium M](https://en.wikipedia.org/wiki/Pentium_M)
* [Intel Atom](https://en.wikipedia.org/wiki/Intel_Atom) 2008


### Cyrix


* [Cyrix 6x86](https://en.wikipedia.org/wiki/Cyrix_6x86) 1996


### AMD


[ AMD Athlon XP (Thoroughbred) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [K5](https://en.wikipedia.org/wiki/AMD_K5) March 1996
* [K6](https://en.wikipedia.org/wiki/AMD_K6) 1997
* [K6-2](https://en.wikipedia.org/wiki/AMD_K6-2) 1998
* [Athlon](https://en.wikipedia.org/wiki/Athlon) (K7) 1999
	+ [Athlon XP](https://en.wikipedia.org/wiki/Athlon#Athlon_XP.2FMP)
	+ [Athlon MP](https://en.wikipedia.org/wiki/Athlon#Athlon_XP.2FMP)


 AMD has continued the name with the [Athlon 64](https://en.wikipedia.org/wiki/Athlon_64), featuring AMD64 64-bit technology, later called [x86-64](X86-64 "X86-64").
## Software


### Operating Systems


* [MS-DOS](MS-DOS "MS-DOS")
* [Unix](Unix "Unix")
* [BSD](Unix "Unix")
* [Linux](Linux "Linux")
* [Windows](Windows "Windows")


### Development


### Assembly


* [MASM](Assembly#x86 "Assembly")
* [TASM](Assembly#x86 "Assembly")


### Pascal


* [Turbo Pascal](Pascal#TurboPascal "Pascal")
* [Delphi](Delphi "Delphi")


### C-Compiler


* [Turbo C](index.php?title=Turbo_C&action=edit&redlink=1 "Turbo C (page does not exist)")
* [Borland C](index.php?title=Borland_C&action=edit&redlink=1 "Borland C (page does not exist)")
* [MSVC](https://en.wikipedia.org/wiki/Visual_C%2B%2B)
* [Intel-C](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler)
* [GCC](Free_Software_Foundation#GCC "Free Software Foundation")
* [Clang](index.php?title=Clang&action=edit&redlink=1 "Clang (page does not exist)")


## Extensions


* [AMX](index.php?title=AMX&action=edit&redlink=1 "AMX (page does not exist)") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [AVX](AVX "AVX")
* [AVX2](AVX2 "AVX2")
* [AVX-512](AVX-512 "AVX-512")
* [MMX](MMX "MMX")
* [SSE2](SSE2 "SSE2")
* [SSE3](SSE3 "SSE3")
* [SSSE3](SSSE3 "SSSE3")
* [SSE4](SSE4 "SSE4")
* [SSE5](SSE5 "SSE5")
* [x86-64](X86-64 "X86-64")
* [XOP](XOP "XOP")


## Manuals


### Intel


* [IA-32 Intel® Architecture Software Developer’s Manual Volume 1: Basic Architecture](http://flint.cs.yale.edu/cs422/doc/24547012.pdf)
* [IA-32 Intel® Architecture Software Developer’s Manual Volume 2: Instruction Set Reference](http://flint.cs.yale.edu/cs422/doc/24547112.pdf)
* [IA-32 Intel® Architecture Software Developer’s Manual Volume 3: System Programming Guide](http://pdos.csail.mit.edu/6.828/2006/readings/ia32/IA32-3.pdf)


### AMD


* [AMD Athlon Processor x86 Code Optimization Guide](http://www.ii.uib.no/~osvik/amd_opt/22007k.pdf) (pdf)


## Forum Posts


* [Question for Eugene Nalimov](https://www.stmintz.com/ccc/index.php?id=36988) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), December 21, 1998
* [why loop unrolling isn't as useful on x86 as it once was](https://www.stmintz.com/ccc/index.php?id=212319) by [Wylie Garvin](index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](CCC "CCC"), February 07, 2002
* [Programmer challenge](https://www.stmintz.com/ccc/index.php?id=285555) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 20, 2003
* [Expert Assembler Question](https://www.stmintz.com/ccc/index.php?id=445557) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 26, 2005
* [Intel CPU performance-loss by security-patch?!?](http://www.talkchess.com/forum/viewtopic.php?t=66224) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), January 03, 2018
* [Intel AMX with TMUL on Xeon Sapphire Rapids (2021?)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74377) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 05, 2020 » [AMX](index.php?title=AMX&action=edit&redlink=1 "AMX (page does not exist)")


## External Links


* [x86 from Wikipedia](https://en.wikipedia.org/wiki/X86)
* [IA-32 from Wikipedia](https://en.wikipedia.org/wiki/IA-32)
* [x87 from Wikipedia](https://en.wikipedia.org/wiki/X87)
* [Optimization manuals](http://www.agner.org/optimize/#manuals) by [Agner Fog](http://www.agner.org/)
* [Agner`s CPU blog](http://www.agner.org/optimize/blog/) by [Agner Fog](http://www.agner.org/)
* [Microprocessor Hall of Fame](http://www.intel.com/museum/online/hist%5Fmicro/hof/) from the [Intel Museum](http://www.intel.com/museum/index.htm)
* [x86 memory segmentation from Wikipedia](https://en.wikipedia.org/wiki/X86_memory_segmentation) » [Memory](Memory "Memory")
* [x86 calling conventions from Wikipedia](https://en.wikipedia.org/wiki/X86_calling_conventions)
* [7th generation x86 CPU Comparisons](http://www.azillionmonkeys.com/qed/cpujihad.shtml) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")


### Assembly


* [X86 Assembly/X86 Architecture from Wikibooks](http://en.wikibooks.org/wiki/X86_Assembly/X86_Architecture)
* [x86 assembly language from Wikipedia](https://en.wikipedia.org/wiki/X86_assembly_language) » [Assembly](Assembly "Assembly")
* [x86 instruction listings from Wikipedia](https://en.wikipedia.org/wiki/X86_instruction_listings)
* [x86 32-bit Assembly for Atheists](http://siyobik.info/index.php?document=x86_32bit_asm)
* [x86 Assembly Guide](http://www.cs.virginia.edu/~evans/cs216/guides/x86.html)


### Modes


* [Protected mode from Wikipedia](https://en.wikipedia.org/wiki/Protected_mode)
* [Real mode from Wikipedia](https://en.wikipedia.org/wiki/Real_mode)
* [Unreal mode from Wikipedia](https://en.wikipedia.org/wiki/Unreal_mode)
* [LOADALL from Wikipedia](https://en.wikipedia.org/wiki/LOADALL)


### Instruction Sets


* [MMX from Wikipedia](https://en.wikipedia.org/wiki/MMX_%28instruction_set%29)
* [3DNow! from Wikipedia](https://en.wikipedia.org/wiki/3DNow)
* [Streaming SIMD Extensions from Wikipedia](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions)
* [SSE2 from Wikipedia](https://en.wikipedia.org/wiki/SSE2)
* [Advanced Vector Extensions from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)
* [AVX-512 from Wikipedia](https://en.wikipedia.org/wiki/AVX-512)
* [Instruction Tables](http://www.agner.org/optimize/instruction_tables.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
* [Advanced Matrix Extension (AMX) - x86 - WikiChip](https://en.wikichip.org/wiki/x86/amx)


### Bugs


* [Pentium FDIV bug from Wikipedia](https://en.wikipedia.org/wiki/Pentium_FDIV_bug)
* [Pentium F00F bug from Wikipedia](https://en.wikipedia.org/wiki/Pentium_F00F_bug)


### Security Vulnerability


* [Meltdown (security vulnerability) from Wikipedia](https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability))
* [Spectre (security vulnerability) from Wikipedia](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability))
* [Project Zero: Reading privileged memory with a side-channel](https://googleprojectzero.blogspot.de/2018/01/reading-privileged-memory-with-side.html) by [Jann Horn](https://thejh.net/), [Project Zero](https://en.wikipedia.org/wiki/Project_Zero), January 03, 2018


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Die shot](https://commons.wikimedia.org/wiki/File:Intel_80386_DX_die.JPG) of [Intel](Intel "Intel") 80386 DX-25 microprocessor (SX215) by [Pauli Rautakorpi](https://commons.wikimedia.org/wiki/User:Birdman86), October 28, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Flat real / real big / unreal mode (v1.2)](http://www.programmersheaven.com/download/1364/download.aspx) from [Programmer's Heaven](http://www.programmersheaven.com/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Unreal mode](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/6ded3c0f3241b432) by Safronov's family, [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), June 5, 2003
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Die shot of [Intel](Intel "Intel") Pentium with P54C core by [Pauli Rautakorpi](https://commons.wikimedia.org/wiki/User:Birdman86), June 11, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> Die shot of [AMD](AMD "AMD") Athlon XP microprocessor with Thoroughbred core (AXDA1800DLT3C) by [Pauli Rautakorpi](https://commons.wikimedia.org/wiki/User:Birdman86), February 14, 2014, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Advanced Matrix Extension (AMX) - x86 - WikiChip](https://en.wikichip.org/wiki/x86/amx)

**[Up one Level](Hardware "Hardware")**







 
