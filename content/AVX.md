---
title: AVX
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * [x86](X86 "X86") * AVX**

**Advanced Vector Extensions** (AVX) is a 256 bit extension to the [x86](X86 "X86") and [x86-64](X86-64 "X86-64") [SSE](SSE "SSE"), [SSE2](SSE2 "SSE2"), [SSE3](SSE3 "SSE3"), [SSSE3](SSSE3 "SSSE3"), and [SSE4](SSE4 "SSE4") [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction sets, announced by [Intel](Intel "Intel") in March 2008, and first released in January, 2011 with Intel's [Sandy Bridge](https://en.wikipedia.org/wiki/Sandy_Bridge_%28microarchitecture%29) architecture. With the [Bulldozer microarchitecture](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29), AVX is also available on [AMD](AMD "AMD") processors <a id="cite-note-1" href="#cite-ref-1">[1]</a>, along with their own [XOP](XOP "XOP") extension on Bulldozer only.

AVX supports 256-bit wide SIMD registers (YMM0-YMM7 in operating modes that are 32-bit or less, YMM0-YMM15 in 64-bit mode) to keep floating point [vectors](Array "Array") of either 8 [floats](Float "Float") or 4 [doubles](Double "Double") inside one register. The lower 128 bits of the YMM registers are aliased to the respective 128-bit XMM registers. AVX employs an instruction encoding scheme using a new [VEX prefix](https://en.wikipedia.org/wiki/VEX_prefix), allowing a three-operand SIMD instruction format, where the destination register is distinct from the two source operands.

## Advantages of AVX

AVX introduces expanded 256-bit versions of floating point instructions, which are typically not useful for chess programming. Though it does not yet expand the integer instructions to 256-bit, AVX does provide VEX-encoded versions of existing SSE 128-bit instructions. For instance, bitwise logical and:

|  Set
|  Instruction
|  Operation
|
| --- | --- | --- |
|  SSE2
| **pand** xmm1, xmm2/m128
|  xmm1 := xmm1 & xmm2
|
|  AVX
| **vpand** xmm1, xmm2, xmm3/m128
|  xmm1 := xmm2 & xmm3
|

Though AVX does not yet support 256-bit integer operations, there are some benefits to using it. 3-operand support can be used to eliminate many "move" instructions, which otherwise can take up significant execution resources.

Additionally, when using xmm registers numbered 8 and higher, the AVX encoding of an SSE instruction is often one byte smaller, due to the more compact nature of the VEX encoding scheme. Finally, the ymm registers offer double the register space: even if the top halves aren't used for computation, they might be suitable as temporary storage space, avoiding the use of a scratch buffer or the stack.

While AVX can do 32-byte loads and stores, no CPU (as of Sandy Bridge) actually has a 32-byte load or store unit; such loads and stores are done simply by doing two separate 16-byte memory operations internally. Thus, AVX is no faster for memory operations (yet).

## AVX on non-Intel CPUs

AMD's [Bulldozer](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29) does not benefit from 3-operand in the same way that Intel's AVX-supporting CPU, Sandy Bridge, does. Bulldozer has a "move elimination" feature that resolves SIMD move instructions separately from the main execution pipeline. On Bulldozer, 3-operand support can still help reduce code size and reduce dispatch bottlenecks, but usually does not help performance much.

Additionally, Bulldozer only has a 128-bit floating-point execution unit, so 256-bit floating point operations are no faster than 128-bit ones, and sometimes actually slower. Nevertheless, some functions might still benefit from the extra register space.

## Mixing AVX and SSE

Besides 3-operand support, the primary difference between the AVX and SSE encodings of an SSE instruction is that the AVX version clears the unused portion of the ymm register (the top 128 bits), while the SSE version does not modify it. Intel strongly advises against mixing SSE 128-bit instructions and AVX 256-bit instructions, as this "mode-switching" can cost upwards of 70 clock cycles. However, mixing SSE 128-bit and AVX 128-bit is okay, as is mixing AVX 128-bit and AVX 256-bit.

In order to safely switch modes, Intel recommends using **vzeroupper** after using 256-bit AVX instructions and before using 128-bit SSE instructions, if the two are being used in the same program.

## AVX2

*see main article [AVX2](AVX2 "AVX2")*

## See also

- [AltiVec](AltiVec "AltiVec")
- [AVX2](AVX2 "AVX2")
- [AVX-512](AVX-512 "AVX-512")
- [BMI1](BMI1 "BMI1")
- [BMI2](BMI2 "BMI2")
- [MMX](MMX "MMX")
- [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
- [SSE](SSE "SSE")
- [SSE2](SSE2 "SSE2")
- [SSE3](SSE3 "SSE3")
- [SSSE3](SSSE3 "SSSE3")
- [SSE4](SSE4 "SSE4")

## Manuals

- [Introduction to Intel® Advanced Vector Extensions](https://computing.llnl.gov/tutorials/linux_clusters/Intro_to_Intel_AVX.pdf) by [Chris Lomont](http://clomont.com/)
- [AMD64 Architecture Programmer’s Manual, Volume 4: 128-Bit and 256-Bit Media Instructions](https://support.amd.com/TechDocs/26568.pdf) (pdf)

## Forum Posts

- [Does Hyperthreading have trouble with AVX?](https://stackoverflow.com/questions/30330013/does-hyperthreading-have-trouble-with-avx) by cmylin, [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), May 19, 2015 » [Thread](Thread "Thread")
- [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum3/viewtopic.php?t=65466&start=7) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), October 16, 2017 » [Tapered Eval](Tapered_Eval "Tapered Eval")

## External Links

- [Advanced Vector Extensions from Wikipedia](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)
- [VEX prefix From Wikipedia](https://en.wikipedia.org/wiki/VEX_prefix)
- [Intel Software Development Emulator](https://software.intel.com/en-us/articles/intel-software-development-emulator/), which can be used to experiment with AVX and AVX2 on a CPU that doesn't support them.
- [Intel Intrinsics Guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/)
- [Using AVX Without Writing AVX Code](https://software.intel.com/en-us/articles/using-avx-without-writing-avx-code)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [AMD64 Architecture Programmer’s Manual, Volume 4: 128-Bit and 256-Bit Media Instructions](https://support.amd.com/TechDocs/26568.pdf) (pdf)

**[Up one Level](X86 "X86")**

