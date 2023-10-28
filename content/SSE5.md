---
title: SSE5
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86](X86 "X86") \* SSE5**


**Streaming SIMD Extensions version 5 (SSE5)**,  

was a [x86-64](X86-64 "X86-64") [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction set extension proposed by [AMD](AMD "AMD") in 2007, with a bunch of very interesting instructions for high performance [bitboarding](Bitboards "Bitboards") and [evaluation](Evaluation "Evaluation"). However, after [Intel](Intel "Intel") declared their 256-bit wide [Advanced Vector Extensions](AVX "AVX") (AVX) as further SIMD extension, AMD reconsidered and replaced SSE5 with three smaller instruction set extensions [XOP](XOP "XOP") for vectors of integers, [FMA4](https://en.wikipedia.org/wiki/FMA_instruction_set) ([fused multiply-add](https://en.wikipedia.org/wiki/Multiply-accumulate) on vectors of [float](Float "Float") and [double](Double "Double")), and [CVT16](https://en.wikipedia.org/wiki/CVT16_instruction_set) ([Half precision floating-point format](https://en.wikipedia.org/wiki/Half_precision)), which retain the proposed functionality of SSE5, but encode the instructions differently for better compatibility with Intel's proposed AVX instruction set and the new [VEX prefix coding scheme](https://en.wikipedia.org/wiki/VEX_prefix). The sets are stated for introduction in AMD's new [Bulldozer](https://en.wikipedia.org/wiki/Bulldozer_%28processor%29) processor core, due for release in late 2011 on a 32nm process <a id="cite-note-1" href="#cite-ref-1">[1]</a> .



### Contents


* [1 Instructions](#instructions)
* [2 See Also](#see-also)
* [3 External Links](#external-links)
* [4 References](#references)






Some of the new instructions are quite interesting for computer chess, with applications in evaluation and byte shuffling of bitboards. Their XOP successors still work on 128-bit XMM registers <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and implicitly clear the upper 128 bit of a 256-bit YMM register. Some of the instructions, like [VPPERM](XOP#VPPERM "XOP"), have as many as 4 operands.



* [XOP Instructions](XOP#Instructions "XOP")


## See Also


* [AltiVec](AltiVec "AltiVec")
* [AVX](AVX "AVX")
* [AVX2](AVX2 "AVX2")
* [AVX-512](AVX-512 "AVX-512")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SSE](SSE "SSE")
* [SSE2](SSE2 "SSE2")
* [SSE3](SSE3 "SSE3")
* [SSSE3](SSSE3 "SSSE3")
* [SSE4](SSE4 "SSE4")
* [XOP](XOP "XOP")


## External Links


* [SSE5 from Wikipedia](https://en.wikipedia.org/wiki/SSE5)
* [SSEPlus Project Documentation](http://sseplus.sourceforge.net/index.html)
* [Agner`s CPU blog](http://www.agner.org/optimize/blog/) by [Agner Fog](http://www.agner.org/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [AMD Fusion now pushed back to 2011](http://arstechnica.com/old/content/2008/11/amd-fusion-now-pushed-back-to-2011.ars) by [Joel Hruska](http://arstechnica.com/author/joel-hruska/), November 14, 2008
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Volume 6: 128-Bit and 256-Bit XOP, FMA4 and CVT16 Instructions](http://support.amd.com/us/Embedded_TechDocs/43479.pdf) (pdf)

**[Up one Level](X86 "X86")**







 
