---
title: SSE4
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86](X86 "X86") \* SSE4**


**SSE4** is a set of [Intel](Intel "Intel") and [AMD](AMD "AMD") ambiguous and almost disjoint x86 instruction set extensions, [SSE4.1](https://en.wikipedia.org/wiki/SSE4#SSE4.1), [SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2) both by Intel, and [SSE4a](https://en.wikipedia.org/wiki/SSE4#SSE4a) by AMD. 



### SSE4.1


Intel introduced SSE4.1 with the [Penryn](https://en.wikipedia.org/wiki/Penryn_%28microarchitecture%29#Penryn) [Core 2](https://en.wikipedia.org/wiki/Intel_Core_2) brand of the [Core microarchitecture](https://en.wikipedia.org/wiki/Core_%28microarchitecture%29) in 2007 with 47 new instructions. 





|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  Mnemonic
 |  Description
 |  |  C-Intrinsic
 |  |
|  pcmpeqq
 |  packed compare equal [qword](Quad_Word "Quad Word") |  \_m128i
 | [\_mm\_cmpeq\_epi64](http://msdn.microsoft.com/en-us/library/bb513998.aspx) |  (\_m128i a, \_m128i b)
 |


*see [Vulnerable on distant Checks with SSE4](King_Pattern#SSE4 "King Pattern").*



### SSE4.2


[SSE4.2](https://en.wikipedia.org/wiki/SSE4#SSE4.2) of the [Nehalem-based](https://en.wikipedia.org/wiki/Nehalem_%28microarchitecture%29) [Core i7](https://en.wikipedia.org/wiki/Intel_Core_i7) was introduced in 2008 with 7 new instructions.



### STTNI


SSE4.2 includes five *String and Text New Instructions* (STTNI) working on 128-bit XMM SIMD as well as general prupose registers and flags to perform character searches and comparison on two operands of 16 bytes at a time , i.e. PCMPESTRI (Packed Compare Explicit Length Strings, Return Index) <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



### ATAI


Popcnt and crc32, working on general purpose registers, were dubbed Application-Targeted Accelerator Instructions (ATAI) as subset of SSE4.2 <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>, but should considered as disjoint instruction set concerning SSE4 compiler optimizations.





|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  Mnemonic
 |  Description
 |  |  C-Intrinsic
 |  |
|  popcnt
 | [Population Count](Population_Count "Population Count") |  int
 | [\_mm\_popcnt\_u64](http://msdn.microsoft.com/en-us/library/bb531475.aspx) |  (unsigned \_int64 a)
 |






## AMD SSE4a


[SSE4a](https://en.wikipedia.org/wiki/SSE4#SSE4a) was introduced by AMD with the [K10](https://en.wikipedia.org/wiki/AMD_K10) (Barcelona) microarchitecture. 



### SIMD


Two new SIMD instructions, working on XMM registers were combined mask-shift instructions (EXTRQ/INSERTQ) and scalar streaming store instructions (MOVNTSD/MOVNTSS). These instructions are not available in Intel's SSE4.




### Advanced Bit Manipulation


The two important instructions work on general purpose registers. [Leading Zero Count](BitScan#LeadingZeroCount "BitScan") was not available in Intel's Application-Targeted Accelerator Instructions of [SSE4.2](#sse4.2), but later incorporated with [BMI](BMI1#LZCNT "BMI1").





|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  Mnemonic
 |  Description
 |  |  C-Intrinsic
 |  |
|  lzcnt
 | [Leading Zero Count](BitScan#LeadingZeroCount "BitScan") |  unsigned \_int64
 | [\_lzcnt64](http://msdn.microsoft.com/en-us/library/bb384809.aspx) |  (unsigned \_int64 a)
 |
|  popcnt
 | [Population Count](Population_Count "Population Count") |  unsigned \_int64
 | [\_popcnt64](http://msdn.microsoft.com/en-us/library/bb385231.aspx) |  (unsigned \_int64 a)
 |


## See also


* [AltiVec](AltiVec "AltiVec")
* [AVX](AVX "AVX")
* [BMI](BMI1 "BMI1")
* [MMX](MMX "MMX")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SSE](SSE "SSE")
* [SSE2](SSE2 "SSE2")
* [SSE3](SSE3 "SSE3")
* [SSSE3](SSSE3 "SSSE3")
* [SSE5](SSE5 "SSE5")
* [TBM](TBM "TBM")
* [Vulnerable on distant Checks with SSE4](King_Pattern#SSE4 "King Pattern")
* [XOP](XOP "XOP")


## Manuals


* [Intel® SSE4 Programming Reference](http://www.info.univ-angers.fr/~richer/ens/l3info/ao/intel_sse4.pdf) (pdf)
* [Software Optimization Guide for AMD Family 10h and 12h Processors](https://support.amd.com/techdocs/40546.pdf) (pdf)


## Forum Posts


* [using Popcount and Prefetch with SSE4 hardware support](http://www.talkchess.com/forum/viewtopic.php?t=43771) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), May 19, 2012 » [Population Count](Population_Count "Population Count"), [Memory](Memory "Memory")


## External Links


* [SSE4 from Wikipedia](https://en.wikipedia.org/wiki/SSE4)
* [MSDN - Streaming SIMD Extensions 4 Instructions](http://msdn.microsoft.com/en-us/library/bb892950.aspx)
* [MSDN - SSE4A and Advanced Bit Manipulation Intrinsics](http://msdn.microsoft.com/en-us/library/bb892945.aspx)
* [SSEPlus Project Documentation](http://sseplus.sourceforge.net/index.html)
* [Agner`s CPU blog](http://www.agner.org/optimize/blog/) by [Agner Fog](http://www.agner.org/)
* [Intel Intrinsics Guide](http://software.intel.com/sites/landingpage/IntrinsicsGuide/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [PCMPESTRI — Packed Compare Explicit Length Strings, Return Index](http://www.felixcloutier.com/x86/PCMPESTRI.html)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [MSDN - Streaming SIMD Extensions 4 Instructions](http://msdn.microsoft.com/en-us/library/bb892950.aspx), 2.3 SSE4.2 INSTRUCTION SET, 2.3.3. Application-Targeted Accelerator Instructions
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Application Targeted Accelerators Intrinsics](https://software.intel.com/en-us/node/524195)

**[Up one Level](X86 "X86")**







 
