---
title: MMX
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86](X86 "X86") \* MMX**



[ [Pentium MMX 166 MHz](https://en.wikipedia.org/wiki/Intel_P5_%28microarchitecture%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**MMX** is a [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") (Single instruction, multiple data) instruction set of [x86](X86 "X86") processors, starting in 1996 with [Intel's](Intel "Intel") [Pentium MMX](https://en.wikipedia.org/wiki/Intel_P5_%28microarchitecture%29). In 1998, [AMD](AMD "AMD") enhanced Intel's MMX with the [3DNow!](https://en.wikipedia.org/wiki/3DNow) extension, mostly related to the [Float](Float "Float") data type. MMX instructions are available through [Assembly](Assembly "Assembly") language, [inline assembly](Assembly#InlineAssembly "Assembly") and C-Compiler intrinsics along with the [\_m64](http://msdn.microsoft.com/en-us/library/08x3t697%28v=VS.100%29.aspx) intrinsic data type <a id="cite-note-2" href="#cite-ref-2">[2]</a> . 



## MMX and 64-bit Windows


Since 64-bit [Windows](Windows "Windows") applications merely use SSE for floating point arithmetic, there was some early confusion whether MMX/x87 registers are safe to use due to context switching. Quote from [Agner Fog's](http://www.agner.org/) Calling conventions manual: <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++
6.1 Can floating point registers be used in 64-bit Windows?

```


```C++
There has been widespread confusion about whether 64-bit Windows allows the use of the floating point registers ST(0)-ST(7) and the MM0 - MM7 registers that are aliased upon these. One early technical document found at Microsoft's website says x87/MMX registers are unavailable to Native Windows64 applications" (Rich Brunner: Technical Details Of Microsoft® Windows® For The AMD64 Platform, Dec. 2003). An AMD document says: "64-bit Microsoft Windows does not strongly support MMX and 3Dnow! instruction sets in the 64-bit native mode" (Porting and Optimizing Multimedia Codecs for AMD64 architecture on Microsoft® Windows®, July 21, 2004). A document in Microsoft's MSDN says: "A caller must also handle the following issues when calling a callee: [...] Legacy Floating-Point Support: The MMX and floating-point stack registers (MM0-MM7/ST0-ST7) are volatile. That is, these legacy floating-point stack registers do not have their state preserved across context switches" (MSDN: Kernel-Mode Driver Architecture: Windows DDK: Other Calling Convention Process Issues. Preliminary, June 14, 2004; February 18, 2005).

```


```C++
This description is nonsense because it confuses saving registers across function calls and saving registers across context switches. Some versions of the Microsoft assembler ml64 (e.g. v. 8.00.40310) gives the following message when attempts are made to use floating point registers in 64 bit mode: "error A2222: x87 and MMX instructions disallowed; legacy  FP state not saved in Win64". However, a public discussion forum quotes the following answers from Microsoft engineers regarding this issue: "From: Program Manager in Visual C++ Group, Sent: Thursday, May 26, 2005 10:38 AM. It does preserve the state. It's the DDK page that has stale information, which I've requested it to be changed. Let them know that the OS does preserve state of x87 and MMX registers on context switches." and "From: Software Engineer in Windows Kernel Group, Sent: Thursday, May 26, 2005 11:06 AM. For user threads the state of legacy floating point is preserved at context switch. But it is not true for kernel threads. [Kernel mode](https://en.wikipedia.org/wiki/Kernel_mode#Supervisor_mode) drivers can not use legacy floating point instructions."

```


```C++
The issue has finally been resolved with the long overdue publication of a more detailed ABI for x64 Windows in the form of a document entitled "x64 Software Conventions", well hidden in the bin directory (not the help directory) of some compiler packages. This document says: "The MMX and floating-point stack registers (MM0-MM7/ST0-ST7) are preserved across context switches. There is no explicit calling convention for these registers. The use of these registers is strictly prohibited in kernel mode code." The same text has later appeared at the [Microsoft](Microsoft "Microsoft") website <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

```

## Applications


Almost the same [bitboard](Bitboards "Bitboards") applications as mentioned in the [SSE2](SSE2 "SSE2") application samples are possible with MMX, despite with scalar bitboards rather than vector of two.



### East Fill


For instance [East Attacks](SSE2#EastAttacks "SSE2") based on SIMD-wise [Fill by Subtraction](Fill_by_Subtraction "Fill by Subtraction").




```C++

__m64 eastAttacks (__m64 occ, __m64 rooks) {
   __m64 tmp;
   occ  = _mm_or_si64 (occ, rooks);  //  make rooks member of occupied
   tmp  = _mm_xor_si64(occ, rooks);  // occ - rooks
   tmp  = _mm_sub_pi8 (tmp, rooks);  // occ - 2*rooks
   return _mm_xor_si64(occ, tmp);    // occ ^ (occ - 2*rooks)
}

```





### MMX Popcount


[AMD's](AMD "AMD") proposed [Efficient 64-Bit Population Count](Population_Count "Population Count") using MMX, 3DNow! and [inline assembly](Assembly#InlineAssembly "Assembly") <a id="cite-note-5" href="#cite-ref-5">[5]</a> :




```C++

##include "amd3d.h"

__declspec (naked) unsigned int __stdcall popcount64 (unsigned __int64 v)
{
   static const __int64 C55 = 0x5555555555555555;
   static const __int64 C33 = 0x3333333333333333;
   static const __int64 C0F = 0x0F0F0F0F0F0F0F0F;
   __asm {
      MOVD      MM0, [ESP+4] ;v_low
      PUNPCKLDQ MM0, [ESP+8] ;v
      MOVQ      MM1, MM0     ;v
      PSRLD     MM0, 1       ;v >> 1
      PAND      MM0, [C55]   ;(v >> 1) & 0x55555555
      PSUBD     MM1, MM0     ;w = v - ((v >> 1) & 0x55555555)
      MOVQ      MM0, MM1     ;w
      PSRLD     MM1, 2       ;w >> 2
      PAND      MM0, [C33]   ;w & 0x33333333
      PAND      MM1, [C33]   ;(w >> 2) & 0x33333333
      PADDD     MM0, MM1     ;x = (w & 0x33333333) + ((w >> 2) & 0x33333333)
      MOVQ      MM1, MM0     ;x
      PSRLD     MM0, 4       ;x >> 4
      PADDD     MM0, MM1     ;x + (x >> 4)
      PAND      MM0, [C0F]   ;y = (x + (x >> 4) & 0x0F0F0F0F)
      PXOR      MM1, MM1     ; 0
      PSADBW    MM0, MM1     ;sum across all 8 bytes
      MOVD      EAX, MM0     ;result in EAX per calling
      ; convention
      FEMMS ;clear MMX state
      RET 8 ;pop 8-byte argument off
   }
}

```

## See also


* [AltiVec](AltiVec "AltiVec")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [SSE2](SSE2 "SSE2")


## Manuals


### Intel


* [Intel Architecture Software Developer’s Manual, Volume 1: Basic Architecture](https://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-1-manual.html)


### AMD


* [AMD Athlon Processor x86 Code Optimization Guide](http://www.ii.uib.no/~osvik/amd_opt/22007k.pdf) (pdf)
* [3DNow! Technology Manual](https://tams.informatik.uni-hamburg.de/lectures/2002ss/vorlesung/pc-technologie/docs/amd-3dnow.pdf) (pdf)
* [AMD Extensions to the 3DNow! and MMX Instruction Sets Manual](http://refspecs.linuxbase.org/AMD-extensions.pdf) (pdf)
* [AMD64 Architecture Volume 5: 64-Bit Media and x87 Floating-Point Instructions](https://support.amd.com/TechDocs/26569_APM_v5.pdf) (pdf)


## Forum Posts


* [Using mmx instructions](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/312f0fd0558723c2) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), February 03, 2000
* [Re: Atomic write of 64 bits](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/ab55c5d57a3a1fd1) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), September 25, 2000
* [Re: Chezzz 1.0.1 - problem solved - for David Rasmussen](https://www.stmintz.com/ccc/index.php?id=281989) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 05, 2003 » [Population Count](Population_Count "Population Count"), [Chezzz](Chezzz "Chezzz")


## External Links


* [MMX (instruction set) from Wikipedia](https://en.wikipedia.org/wiki/MMX_%28instruction_set%29)
* [3DNow!](https://en.wikipedia.org/wiki/3DNow!)
* [Intel Intrinsics Guide](http://software.intel.com/sites/landingpage/IntrinsicsGuide/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Intel P5 (microarchitecture) from Wikipedia](https://en.wikipedia.org/wiki/Intel_P5_%28microarchitecture%29), Source: Sergei Frolov, [Soviet Calculators Collection](http://www.leningrad.su/museum/), September 2007
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [MMX Technology Intrinsic Groups](http://msdn.microsoft.com/en-us/library/ccky3awe%28v=VS.100%29.aspx)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Calling conventions for different C++ compilers and operating systems](http://www.agner.org/optimize/calling_conventions.pdf) (pdf) by [Agner Fog](http://www.agner.org/)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Legacy Floating-Point Support (C++)](http://msdn.microsoft.com/en-us/library/a32tsf7t%28v=VS.100%29.aspx) from MSDN Library
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [AMD Athlon Processor x86 Code Optimization Guide](http://www.ii.uib.no/~osvik/amd_opt/22007k.pdf) (pdf) Efficient 64-Bit Population Count Using MMX™ Instructions Page 184

**[Up one Level](X86 "X86")**







 
