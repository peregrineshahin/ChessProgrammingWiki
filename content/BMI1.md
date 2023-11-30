---
title: BMI1
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * [x86-64](X86-64 "X86-64") * BMI1**

**BMI1** (BMI),

an x86-64 expansion of [bit-manipulation](Bit-Twiddling#BitManipulation "Bit-Twiddling") instructions by [Intel](Intel "Intel"), introduced in conjunction with the [Advanced Vector Extensions](AVX "AVX") [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instruction set. With the [Bulldozer microarchitecture](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29), BMI1 as well as [AVX](AVX "AVX") are also available on [AMD](AMD "AMD") processors under the initial name BMI, along with their [Trailing Bit Manipulation Instructions](TBM "TBM") (TBM) <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Most BMI1 instructions (except LZCNT and TZCNT) employ the [VEX prefix](https://en.wikipedia.org/wiki/VEX_prefix) encoding to support up to three-operand syntax with non-destructive source operands on 32- or 64-bit general-purpose registers. BMI1 (ANDN, BEXTR, BLSI, BLSMK, BLSR, TZCNT) requires bit 3 set in EBX of [CPUID](https://en.wikipedia.org/wiki/CPUID) with EAX=07H, ECX=0H. LZCNT, not exactly member of BMI1, requires bit 5 set in ECX of CPUID EAX=80000001H. With the advent of [AVX2](AVX2 "AVX2"), some more [bit-twiddling](Bit-Twiddling "Bit-Twiddling") on general-purpose registers is proposed with [BMI2](BMI2 "BMI2").

## Instructions

BMI1 instructions may speedup various [bitboard](Bitboards "Bitboards") [operations](General_Setwise_Operations "General Setwise Operations"), such as [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations"), and [isolation](General_Setwise_Operations#LS1BIsolation "General Setwise Operations"), [reset](General_Setwise_Operations#LS1BReset "General Setwise Operations") and [separation](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") of the [least significant one bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"), they combine two instructions and reduce register pressure. [Leading](BitScan#LeadingZeroCount "BitScan") and [trailing zero count](BitScan#TrailingZeroCount "BitScan") are useful for [scanning bits](BitScan "BitScan") with possibly empty sets.

## ANDN

Logical And Not, the [relative complement](General_Setwise_Operations#RelativeComplement "General Setwise Operations"), no intrinsic due to compiler support.

```C++

dest ::= ~src1 & src2;

```

## BEXTR

Bit Field Extract. Nice to extract some consecutive bits from a ([rotated](Rotated_Bitboards "Rotated Bitboards")) [occupancy](Occupancy "Occupancy") bitboard, or, as they name suggests, from [bit-field](https://en.wikipedia.org/wiki/Bit_field) structures.

```C++

dest ::= (src >> start) & ((1 << len)-1);

unsigned __int32 _bextr_u32(unsigned __int32 src, unsigned __int32 start, unsigned __int32 len);
unsigned __int64 _bextr_u64(unsigned __int64 src, unsigned __int32 start, unsigned __int32 len);

```

A shiftless [sign extension](Score#SignExtension "Score") might be applied by <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```C++

dest_signextended ::= (dest ^ signbit) - signbit

```

## BLSI

Extract Lowest Set Isolated Bit, [isolates](General_Setwise_Operations#LS1BIsolation "General Setwise Operations") [least significant one bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations").

```C++

dest ::= src & -src;

unsigned __int64 _blsi_u64(unsigned __int64 src);

```

## BLSMSK

Get Mask Up to Lowest Set Bit, [sets all bits below](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") the [least significant one bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"), and clears all upper bits.

```C++

dest ::= (src-1) ^ src;

unsigned __int64 _blsmsk_u64(unsigned __int64 src);

```

## BLSR

Reset Lowest Set Bit, [resets](General_Setwise_Operations#LS1BReset "General Setwise Operations") [least significant one bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations").

```C++

dest ::= (src-1) & src;

unsigned __int64 _blsr_u64(unsigned __int64 src);

```

## LZCNT

Count the Number of Leading Zero Bits, [Leading Zero Count](BitScan#LeadingZeroCount "BitScan"), initially from [AMD's](AMD "AMD") [SSE4a](SSE4#SSE4a "SSE4") aka [Advanced Bit Manipulations](SSE4#ABM "SSE4") (ABM).

```C++

unsigned __int64 _lzcnt_u64(unsigned __int64 src);

```

## TZCNT

Count the Number of Trailing Zero Bits, [Trailing Zero Count](BitScan#TrailingZeroCount "BitScan") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

```C++

unsigned __int64 _tzcnt_u64(unsigned __int64 src);

```

## See also

- [ABM](SSE4#ABM "SSE4")
- [AVX](AVX "AVX")
- [AVX2](AVX2 "AVX2")
- [BitScan](BitScan "BitScan")
- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [BMI2](BMI2 "BMI2")
- [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")
- [TBM](TBM "TBM")

## Manuals

- [Intel AVX and AVX2 Programming Reference](http://software.intel.com/file/36945) (pdf)
- [AMD64 Architecture Programmer’s Manual Volume 3: General-Purpose and System Instructions](https://www.amd.com/system/files/TechDocs/24594.pdf) (pdf) <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [Software Optimization Guide for AMD Family 15h Processors](https://www.amd.com/system/files/TechDocs/47414_15h_sw_opt_guide.pdf) (pdf) 9.8 Optimizing with BMI and TBM Instructions, pp. 163

## External Links

- [Bit Manipulation Instruction Sets from Wikipedia](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets)
- [Intel Intrinsics Guide](https://software.intel.com/sites/landingpage/IntrinsicsGuide/#)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [AMD64 Architecture Programmer’s Manual Volume 3: General-Purpose and System Instructions](https://www.amd.com/system/files/TechDocs/24594.pdf) (pdf)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Sign Extension](http://aggregate.org/MAGIC/#Sign%20Extension) from [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC) by [Hank Dietz](Hank_Dietz "Hank Dietz")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Looking for intrinsic "least significant bit" on Visual Studio](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74989) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 03, 2020
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> Moved BMI and TBM instructions from Volume 4 to Volume 3 in September 2011

**[Up one Level](X86-64 "X86-64")**

