---
title: TBM
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [x86-64](X86-64 "X86-64") \* TBM**


**TBM** (Trailing Bit Manipulation Instructions),  

an x86-64 expansion of [bit-manipulation](Bit-Twiddling#BitManipulation "Bit-Twiddling") instructions, introduced by [AMD](AMD "AMD") with the [Bulldozer microarchitecture](https://en.wikipedia.org/wiki/Bulldozer_%28microarchitecture%29), which also comprises the [AVX](AVX "AVX"), [BMI1](BMI1 "BMI1") and [XOP](XOP "XOP") instruction sets. TBM requires bit 21 set in ECX of CPUID EAX=80000001H <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
More recent [AMD Jaguar](https://en.wikipedia.org/wiki/Jaguar_(microarchitecture)) and [Zen](https://en.wikipedia.org/wiki/Zen_(microarchitecture)) based processors do not support TBM <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### Least Significant One Bit


### BLSFILL


Fill From Lowest Set Bit. [Union](General_Setwise_Operations#Union "General Setwise Operations") with the decrement.




```C++
BLSFILL reg64, reg/mem64
dest ::= src | (src - 1);

       src         |     (src - 1)     =       dest
0x0040201008040200  0x00402010080401FF  0x00402010080403FF
  . . . . . . . .     . . . . . . . .     . . . . . . . .
  . . . . . . 1 .     . . . . . . 1 .     . . . . . . 1 .
  . . . . . 1 . .     . . . . . 1 . .     . . . . . 1 . .
  . . . . 1 . . .     . . . . 1 . . .     . . . . 1 . . .
  . . . 1 . . . .  |  . . . 1 . . . .  =  . . . 1 . . . .
  . . 1 . . . . .     . . 1 . . . . .     . . 1 . . . . .
  . 1 . . . . . .     1 . . . . . . .     1 1 . . . . . .
  . . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

```





### BLSIC


Isolate Lowest Set Bit and Complement. [Union](General_Setwise_Operations#Union "General Setwise Operations") of [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") and decrement.




```C++
BLSIC reg64, reg/mem64
dest ::= ~src | (src - 1);

       src        ->       ~src        |     (src - 1)     =       dest
0x0040201008040200  0x00402010080401FF  0x00402010080403FF  0xFFFFFFFFFFFFFDFF
  . . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .     1 1 1 1 1 1 1 1
  . . . . . . 1 .     1 1 1 1 1 1 . 1     . . . . . . 1 .     1 1 1 1 1 1 1 1
  . . . . . 1 . .     1 1 1 1 1 . 1 1     . . . . . 1 . .     1 1 1 1 1 1 1 1
  . . . . 1 . . .     1 1 1 1 . 1 1 1     . . . . 1 . . .     1 1 1 1 1 1 1 1
  . . . 1 . . . . ->  1 1 1 . 1 1 1 1  |  . . . 1 . . . .  =  1 1 1 1 1 1 1 1
  . . 1 . . . . .     1 1 . 1 1 1 1 1     . . 1 . . . . .     1 1 1 1 1 1 1 1
  . 1 . . . . . .     1 . 1 1 1 1 1 1     1 . . . . . . .     1 . 1 1 1 1 1 1
  . . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

```





### TZMSK


Mask From Trailing Zeros. [Intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") and decrement [sets all bits below](General_Setwise_Operations#LS1BSeparation "General Setwise Operations") the [least significant one bit](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations"), and clears all other bits, including the LS1B itself.




```C++
dest ::= ~src & (src - 1);
       src        ->       ~src        &     (src - 1)     =       dest
0x0040201008040200  0x00402010080401FF  0x00402010080403FF  0x00000000000001FF
  . . . . . . . .     1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .
  . . . . . . 1 .     1 1 1 1 1 1 . 1     . . . . . . 1 .     . . . . . . . .
  . . . . . 1 . .     1 1 1 1 1 . 1 1     . . . . . 1 . .     . . . . . . . .
  . . . . 1 . . .     1 1 1 1 . 1 1 1     . . . . 1 . . .     . . . . . . . .
  . . . 1 . . . . ->  1 1 1 . 1 1 1 1  &  . . . 1 . . . .  =  . . . . . . . .
  . . 1 . . . . .     1 1 . 1 1 1 1 1     . . 1 . . . . .     . . . . . . . .
  . 1 . . . . . .     1 . 1 1 1 1 1 1     1 . . . . . . .     1 . . . . . . .
  . . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1

```





### Least Significant Zero Bit


### BLCFILL


Fill From Lowest Clear Bit. [Intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with the increment.




```C++
BLCFILL reg64, reg/mem64
dest ::= src & (src + 1);

       src         &     (src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x80C0E0F0F8FCFF00  0x80C0E0F0F8FCFE00
  . . . . . . . 1     . . . . . . . 1     . . . . . . . 1  
  . . . . . . 1 1     . . . . . . 1 1     . . . . . . 1 1  
  . . . . . 1 1 1     . . . . . 1 1 1     . . . . . 1 1 1  
  . . . . 1 1 1 1     . . . . 1 1 1 1     . . . . 1 1 1 1  
  . . . 1 1 1 1 1  &  . . . 1 1 1 1 1  =  . . . 1 1 1 1 1  
  . . 1 1 1 1 1 1     . . 1 1 1 1 1 1     . . 1 1 1 1 1 1  
  . 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     . 1 1 1 1 1 1 1  
  1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .  

```





### BLCI


Isolate Lowest Clear Bit. [Union](General_Setwise_Operations#Union "General Setwise Operations") with the [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") of the increment.




```C++
BLCI reg64, reg/mem64
dest ::= src | ~(src + 1);

       src         |    ~(src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x7F3F1F0F070300FF  0xFFFFFFFFFFFFFEFF
  . . . . . . . 1     1 1 1 1 1 1 1 .     1 1 1 1 1 1 1 1  
  . . . . . . 1 1     1 1 1 1 1 1 . .     1 1 1 1 1 1 1 1  
  . . . . . 1 1 1     1 1 1 1 1 . . .     1 1 1 1 1 1 1 1  
  . . . . 1 1 1 1     1 1 1 1 . . . .     1 1 1 1 1 1 1 1  
  . . . 1 1 1 1 1  |  1 1 1 . . . . .  =  1 1 1 1 1 1 1 1  
  . . 1 1 1 1 1 1     1 1 . . . . . .     1 1 1 1 1 1 1 1  
  . 1 1 1 1 1 1 1     . . . . . . . .     . 1 1 1 1 1 1 1  
  1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1  

```





### BLCIC


Isolate Lowest Clear Bit and Complement. [Intersection](General_Setwise_Operations#Intersection "General Setwise Operations") of the [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") with the increment.




```C++
BLCIC reg64, reg/mem64
dest ::= ~src & (src + 1);

       src        ->       ~src        &     (src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x7F3F1F0F07030100  0x80C0E0F0F8FCFF00  0x0000000000000100
  . . . . . . . 1     1 1 1 1 1 1 1 .     . . . . . . . 1     . . . . . . . . 
  . . . . . . 1 1     1 1 1 1 1 1 . .     . . . . . . 1 1     . . . . . . . .  
  . . . . . 1 1 1     1 1 1 1 1 . . .     . . . . . 1 1 1     . . . . . . . .  
  . . . . 1 1 1 1     1 1 1 1 . . . .     . . . . 1 1 1 1     . . . . . . . .  
  . . . 1 1 1 1 1 ->  1 1 1 . . . . .  &  . . . 1 1 1 1 1  =  . . . . . . . .  
  . . 1 1 1 1 1 1     1 1 . . . . . .     . . 1 1 1 1 1 1     . . . . . . . .  
  . 1 1 1 1 1 1 1     1 . . . . . . .     1 1 1 1 1 1 1 1     1 . . . . . . .  
  1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .     . . . . . . . .  

```





### BLCMSK


Mask From Lowest Clear Bit. [Exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with the increment.




```C++
BLCMSK reg64, reg/mem64
dest ::= src ^ (src + 1);

       src         ^     (src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x80C0E0F0F8FCFF00  0x00000000000001FF
  . . . . . . . 1     . . . . . . . 1     . . . . . . . .  
  . . . . . . 1 1     . . . . . . 1 1     . . . . . . . .  
  . . . . . 1 1 1     . . . . . 1 1 1     . . . . . . . .  
  . . . . 1 1 1 1     . . . . 1 1 1 1     . . . . . . . .  
  . . . 1 1 1 1 1  ^  . . . 1 1 1 1 1  =  . . . . . . . .  
  . . 1 1 1 1 1 1     . . 1 1 1 1 1 1     . . . . . . . .  
  . 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 . . . . . . .  
  1 1 1 1 1 1 1 1     . . . . . . . .     1 1 1 1 1 1 1 1  

```





### BLCS


Set Lowest Clear Bit. [Union](General_Setwise_Operations#Union "General Setwise Operations") with the increment.




```C++
BLCS reg64, reg/mem64
dest ::= src | (src + 1);

       src         |     (src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x80C0E0F0F8FCFF00  0x80C0E0F0F8FCFFFF
  . . . . . . . 1     . . . . . . . 1     . . . . . . . 1  
  . . . . . . 1 1     . . . . . . 1 1     . . . . . . 1 1  
  . . . . . 1 1 1     . . . . . 1 1 1     . . . . . 1 1 1  
  . . . . 1 1 1 1     . . . . 1 1 1 1     . . . . 1 1 1 1  
  . . . 1 1 1 1 1  |  . . . 1 1 1 1 1  =  . . . 1 1 1 1 1  
  . . 1 1 1 1 1 1     . . 1 1 1 1 1 1     . . 1 1 1 1 1 1  
  . 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1  
  1 1 1 1 1 1 1 1     . . . . . . . .     1 1 1 1 1 1 1 1  

```





### T1MSKC


Inverse Mask From Trailing Ones. [Union](General_Setwise_Operations#Union "General Setwise Operations") of [complement](General_Setwise_Operations#ComplementSet "General Setwise Operations") and increment.




```C++
T1MSKC reg64, reg/mem64
dest ::= ~src | (src + 1);

       src        ->       ~src        |     (src + 1)     =       dest
0x80C0E0F0F8FCFEFF  0x7F3F1F0F07030100  0x80C0E0F0F8FCFF00  0xFFFFFFFFFFFFFF00
  . . . . . . . 1     1 1 1 1 1 1 1 .     . . . . . . . 1     1 1 1 1 1 1 1 1  
  . . . . . . 1 1     1 1 1 1 1 1 . .     . . . . . . 1 1     1 1 1 1 1 1 1 1  
  . . . . . 1 1 1     1 1 1 1 1 . . .     . . . . . 1 1 1     1 1 1 1 1 1 1 1  
  . . . . 1 1 1 1     1 1 1 1 . . . .     . . . . 1 1 1 1     1 1 1 1 1 1 1 1  
  . . . 1 1 1 1 1 ->  1 1 1 . . . . .  |  . . . 1 1 1 1 1  =  1 1 1 1 1 1 1 1  
  . . 1 1 1 1 1 1     1 1 . . . . . .     . . 1 1 1 1 1 1     1 1 1 1 1 1 1 1  
  . 1 1 1 1 1 1 1     1 . . . . . . .     1 1 1 1 1 1 1 1     1 1 1 1 1 1 1 1  
  1 1 1 1 1 1 1 1     . . . . . . . .     . . . . . . . .     . . . . . . . .  

```





### Misc


### BEXTR


An immediate form of the variable [BMI1 Bit Field Extract](BMI1#BEXTR "BMI1").




```C++
BEXTR reg32, reg/mem32, imm32
BEXTR reg64, reg/mem64, imm32

```

## See also


* [ABM](SSE4#ABM "SSE4")
* [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
* [BMI1](BMI1 "BMI1")
* [BMI2](BMI2 "BMI2")
* [General Setwise Operations](General_Setwise_Operations "General Setwise Operations")


 [Obtaining and Clearing the Least Significant Bit (LS1B)](General_Setwise_Operations#TheLeastSignificantOneBitLS1B "General Setwise Operations")
## Manuals


* [AMD64 Architecture Programmer’s Manual Volume 3: General-Purpose and System Instructions](https://www.amd.com/system/files/TechDocs/24594.pdf) (pdf) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Software Optimization Guide for AMD Family 15h Processors](https://www.amd.com/system/files/TechDocs/47414_15h_sw_opt_guide.pdf) (pdf) 9.8 Optimizing with BMI and TBM Instructions, pp. 163


## External Links


* [TBM from Wikipedia](https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#TBM_(Trailing_Bit_Manipulation))


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [AMD CPUID Specification](http://support.amd.com/us/Embedded_TechDocs/25481.pdf) (pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Family 16h Models 00h-0Fh AMD A-Series Mobile Accelerated Processor Product Data Sheet](https://www.amd.com/system/files/TechDocs/52169_KB_A_Series_Mobile.pdf) (pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> Moved BMI and TBM instructions from Volume 4 to Volume 3 in September 2011

**[Up one Level](X86-64 "X86-64")**







 
