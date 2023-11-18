---
title: Double
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Data](Data "Data") * Double**

**Double** is a 64-bit data type representing the [double precision floating-point format](https://en.wikipedia.org/wiki/Double_precision_floating-point_format), in [IEEE 754-1985](https://en.wikipedia.org/wiki/IEEE_754-1985) called double, in [IEEE 754-2008](https://en.wikipedia.org/wiki/IEEE_754-2008) 64-bit base 2 format is officially referred to as binary64. Due to [normalization](https://en.wikipedia.org/wiki/Normal_number_%28computing%29) the true [significand](https://en.wikipedia.org/wiki/Significand) includes an implicit leading one bit unless the exponent is stored with all bits zeros or ones which are reserved for [Denormal numbers](https://en.wikipedia.org/wiki/Subnormal_numbers). Thus only 52 bits of the significand are stored but the total precision is 53 bits (≈15.955 decimal digits). [Exponent bias](https://en.wikipedia.org/wiki/Exponent_bias) is 0x3FF (1023).

## Format

\[
[Double precision floating-point format](https://en.wikipedia.org/wiki/Double_precision_floating-point_format)

## x86 Instruction Sets

Recent [x86](X86 "X86") and [x86-64](X86-64 "X86-64") processors provide [x87](https://en.wikipedia.org/wiki/X87), and [SSE2](SSE2 "SSE2") double precision floating point instruction sets. Since SSE2 is not obligatory for x86-32, 32-bit operating systems rely on x87. x86-64 64-bit operating systems may use the faster SSE2 instructions, but so far only 64-bit compiler for 64-bit [Windows](Windows "Windows") emit those instructions implicitly for double precision floating point operations <a id="cite-note-1" href="#cite-ref-1">[1]</a> . SSE2 instructions can be mixed with x87 and are explicitly available through (inline) [Assembly](Assembly "Assembly") or intrinsics of various [C](C "C")-Compilers.

## Integer to Double Conversion

### X87

To convert a signed or unsigned integer to float, two x87 instructions are needed, FILD and FSTP working on the x87 floating point stack <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

**FILD**
The FILD instruction converts a signed-integer in memory to [double-extended-precision](https://en.wikipedia.org/wiki/Extended_precision) (10 bytes) format and pushes the value onto the x87 register stack. The value can be a 16-bit, 32-bit, or 64- bit integer value. Signed values from memory can always be represented exactly in x87 registers without rounding.

**FSTP**
The FSTP instruction pops the x87 stack after copying the value. The instruction FSTP ST(0) is the same as popping the stack with no data transfer. If the specified destination is a single-precision (4 bytes) or double-precision (8 bytes) memory location, the instruction converts the value to the appropriate precision format. It does this by rounding the significand of the source value as specified by the rounding mode determined by the RC field of the x87 control word and then converting to the format of destination. It also converts the exponent to the width and bias of the destination format.

### SSE2

<a id="cite-note-3" href="#cite-ref-3">[3]</a><a id="cite-note-4" href="#cite-ref-4">[4]</a>
**CVTDQ2PD**
Converts two packed 32-bit signed integer values in the low-order 64 bits of an XMM register or a 64-bit memory location to two packed double-precision floating-point values and writes the converted values in another XMM register.

- Mnemonic: CVTDQ2PD xmm1, xmm2/mem64
- Intrinsic: [\_mm_cvtepi32_pd](http://msdn.microsoft.com/en-us/library/fhwkxa6t%28v=VS.100%29.aspx)

**CVTPI2PD**
Converts two packed 32-bit signed integer values in an MMX register or a 64-bit memory location to two double-precision floating-point values and writes the converted values in an XMM register.

- Mnemonic: CVTPI2PD xmm, mmx/mem64
- Intrinsic: [\_mm_cvtpi32_pd](http://msdn.microsoft.com/en-us/library/ahh5bb05%28v=VS.100%29.aspx)

**CVTSI2SD**
Converts a 32-bit or 64-bit signed integer value in a general-purpose register or memory location to a double-precision floating-point value and writes the converted value in the low-order 64 bits of an XMM register. The high-order 64 bits in the destination XMM register are not modified.

- Mnemonic: CVTSI2SD xmm, reg/mem32 (reg/mem64)
- Intrinsic: [\_mm_cvtsi32_sd](http://msdn.microsoft.com/en-us/library/b60kza8a%28v=VS.100%29.aspx)

## BitScan Purpose

Integer to Double conversion can be used as base 2 logarithm of a power of two value of a 64-bit signed or unsigned integer, which might be used as 64-bit [bitscan](BitScan "BitScan"), as mentioned in [Double conversion of LS1B](BitScan#DoubleConversionofLS1B "BitScan") and [Double conversion](BitScan#DoubleConversionBSR "BitScan").

## See also

- [Quad Word](Quad_Word "Quad Word")
- [SSE](SSE "SSE")
- [SSE2](SSE2 "SSE2")
- [Float](Float "Float")

## Publications

- [David Goldberg](index.php?title=David_Goldberg&action=edit&redlink=1 "David Goldberg (page does not exist)") (**1991**). *What every computer scientist should know about floating-point arithmetic*. [ACM Computing Surveys](ACM#Surveys "ACM"), [pdf](https://www.itu.dk/~sestoft/bachelor/IEEE754_article.pdf)

## Forum Posts

- [Bitboards using 2 DOUBLE's ?](http://www.talkchess.com/forum/viewtopic.php?t=28207) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), June 02, 2009 » [Bitboards](Bitboards "Bitboards")

## External Links

- [Floating point from Wikipedia](https://en.wikipedia.org/wiki/Floating_point)
- [Double precision floating-point format](https://en.wikipedia.org/wiki/Double_precision_floating-point_format)
- [Extended precision](https://en.wikipedia.org/wiki/Extended_precision)
- [Quadruple precision floating-point format](https://en.wikipedia.org/wiki/Quadruple_precision)
- [Survey of Floating-Point Formats](http://www.mrob.com/pub/math/floatformats.html) by [Robert Munafo](http://www.mrob.com/pub/index.html)
- [About Floating Point Arithmetic](http://info.uptrend.ch/uptrend/page/display/numerische-probleme-mit-reals?v=54) from [Johanns Blog](Johann_Joss#Blog "Johann Joss")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [AMD64 ArchitectureProgrammer’s Manual Volume 5: 64-Bit Media and x87 Floating-Point Instructions](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/26569.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [AMD64 Architecture, Programmer’s Manual, Volume 4: 128-Bit and 256-Bit Media Instructions](https://support.amd.com/TechDocs/26568.pdf) (pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Floating-Point Intrinsics Using Streaming SIMD Extensions 2 Instructions](http://msdn.microsoft.com/en-us/library/9b07190d%28v=VS.100%29.aspx)

**[Up one Level](Data "Data")**

