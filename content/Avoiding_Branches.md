---
title: Avoiding Branches
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Optimization](Optimization "Optimization") * Avoiding Branches**

Miss-predicted [branches](https://en.wikipedia.org/wiki/Branch_%28computer_science%29) causes huge penalties on todays super [pipelined](https://en.wikipedia.org/wiki/Instruction_pipeline) processors. While processors become smarter to predict branches with several heuristics, branches on random data should be avoided. The techniques shown here often use arithmetical shift right (by bit-width - 1, that is 31 for 32-bit [double words](Double_Word "Double Word") as integers) to determine a mask of sign-bits, either all bits set (-1) or all bits clear 0. [x86](X86 "X86") compiler may emit an cdq (Convert Double to Quad) instruction, which sign extends a 32 bit register to two 32 bit registers. Since arithmetical shift right is not strictly specified in [C](C "C"), it might be not portable through all compilers and architectures. Note that in C, a comparison or a boolean expression with the result {false, true} might be treated as numerical value {0, 1}.

## Contents

- [1 Abs, Max, Min](#abs.2c-max.2c-min)
  - [1.1 Absolute value of an Integer](#absolute-value-of-an-integer)
  - [1.2 Maximum of two Integers](#maximum-of-two-integers)
    - [1.2.1 By CRT](#by-crt)
    - [1.2.2 By Sign-Mask](#by-sign-mask)
  - [1.3 Minimum of two Integers](#minimum-of-two-integers)
    - [1.3.1 By CRT](#by-crt-2)
    - [1.3.2 By Sign-Mask](#by-sign-mask-2)
- [2 Conditional Expressions](#conditional-expressions)
  - [2.1 Conditional Assignment](#conditional-assignment)
  - [2.2 Conditional Increment](#conditional-increment)
  - [2.3 Conditional Write](#conditional-write)
- [3 Indirect Branch](#indirect-branch)
- [4 See also](#see-also)
- [5 Forum Posts](#forum-posts)
  - [5.1 2000 ...](#2000-...)
  - [5.2 2010 ...](#2010-...)
  - [5.3 2020 ...](#2020-...)
- [6 External Links](#external-links)
- [7 References](#references)

## Abs, Max, Min

It is recommend to use functions provided by the [programming language](Languages "Languages"). In [C](C "C") or [C++](Cpp "Cpp") one should use appropriate compiler intrinsics and/or template functions provided by the [C Runtime Library](C#Runtime "C") or [Standard Template Library](Cpp#STL "Cpp").

The tricks shown here, might be useful if compiler don't support those functions or don't generate the intended branchless assembly and the input is quite random, so that the branch prediction heuristics will fail often.

## Absolute value of an Integer

Abs as [C](C "C") intrinsic <a id="cite-note-1" href="#cite-ref-1">[1]</a> is likely implemented based on following code snippet ...

```C++

int abs(int a) {
   int s = a >> 31; // cdq, signed shift, -1 if negative, else 0
   a ^= s;  // ones' complement if negative
   a -= s;  // plus one if negative -> two's complement if negative
   return a;
}

```

... by compilers, on [x86](X86 "X86") a sequence three instructions: {cdq, xor, sub} or {cdq, add, xor}.

## Maximum of two Integers

### By CRT

[Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B) Run-Time Library provides a \_max macro <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

### By Sign-Mask

Following trick only works for a reduced integer range of effectively one bit less, which is most often no problem for 32-bit integers in chess programs, like scores and that like: INT_MIN \<= a - b \<= INT_MAX:
If a is greater b, a - 0 is returned, otherwise a - (a - b) == +b

```C++

int max(int a, int b) {
  int diff = a - b;
  int dsgn = diff >> 31;
  return a - (diff & dsgn);
}

```

## Minimum of two Integers

### By CRT

[Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B) Run-Time Library provides a \_min macro <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

### By Sign-Mask

Following trick only works for a reduced integer range of effectively one bit less, which is most often no problem for 32-bit integers in chess programs, like scores and that like: INT_MIN \<= a - b \<= INT_MAX:
If a is greater b, b + 0 is returned, otherwise b + (a - b) == +a

```C++

int min(int a, int b) {
  int diff = a - b;
  int dsgn = diff >> 31;
  return b + (diff & dsgn);
}

```

## Conditional Expressions

## Conditional Assignment

A conditional assignment in [C](C "C") or [C++](Cpp "Cpp") may be implemented by compilers as [x86](X86 "X86") conditional move (cmovCC) instruction.

```C++

x = ( a > b ) ? C : D;

```

otherwise it might be reformulated with conditional increment:

```C++

x = D;
if ( a > b ) x += C - D;

```

## Conditional Increment

If a > b is hard to predict,

```C++

if ( a > b ) x += C;

```

it might be reformulated branch-less in [C](C "C"), which likely emits a [x86](X86 "X86") setCC instruction:

```C++

x += -( a > b ) & C; // with any boolean expression

```

With a reduced value range and INT_MIN \<= b - a \<= INT_MAX, greater and less relations might be implemented using a sign mask:

```C++

x += (( b - a ) >> 31) & C;

```

## Conditional Write

During list generation, while conditionally writing data to an [array](Array "Array") with post-incrementing a pointer or index, one may try to avoid the conditional branch by storing always and to increment the pointer by the condition, which is either 0 or 1 <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

```C++

if (a > b)
  *ptr++ = value;

```

might be rewritten by

```C++

  *ptr = value;
  ptr += (a > b);

```

## Indirect Branch

[Robert Hyatt](Robert_Hyatt "Robert Hyatt") on [x86](X86 "X86") [Branch predictor](https://en.wikipedia.org/wiki/Branch_predictor), [Branch target predictor](https://en.wikipedia.org/wiki/Branch_target_predictor), and [Indirect branch](https://en.wikipedia.org/wiki/Indirect_branch) in [CCC](CCC "CCC") <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++
There are two parts to predicting a branch on [x86](X86 "X86"). 1. Is the branch taken (for a call it is always "yes")? 2. Where is the branch going?

```

```C++
(2) is more interesting because when you fetch and then predict the branch, you don't have a clue where it is going since the register being used might not yet be ready for access. The solution is a "branch target buffer" which simply predicts the branch AND where it is going, based on the last time it was encountered. You can do a conditional jump to an indirect address and predict the jump correctly and miss the address (entire thing is then predicted wrong) or you can predict the address correctly and miss the jump (again, entire thing is wrong), or you can miss both. Only when you get both right do you have any success.

```

```C++
Your code always jumps to the same place, whether you use the explicit jump address, or the indirect address through a register. When you get into a call where the address changes, performance will drop. Your code really is not testing that at all... 

```

## See also

- [Bit-Twiddling](Bit-Twiddling "Bit-Twiddling")
- [DirGolem](DirGolem "DirGolem")
- [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
- [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")

## Forum Posts

## 2000 ...

- [branch misprediction](https://www.stmintz.com/ccc/index.php?id=376742) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), July 14, 2004
- [Re: Fruit 2.0 Toga : Recapture extension](https://www.stmintz.com/ccc/index.php?id=417440) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), March 19, 2005

## 2010 ...

- [Re: Function pointers hurt performance?](http://www.talkchess.com/forum/viewtopic.php?p=425259#425259) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 22, 2011
- [Branch-poor looping](http://www.talkchess.com/forum/viewtopic.php?t=57477) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 02, 2015
- [Mispredicted branch VS cache miss](http://www.talkchess.com/forum/viewtopic.php?t=57577) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), September 09, 2015
- [Tipical cache and branch misses for a chess engine](http://www.talkchess.com/forum/viewtopic.php?t=61423) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), September 14, 2016 » [Memory](Memory "Memory"), [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
- [Misprediction-poor looping](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72539) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 09, 2019

## 2020 ...

- [A Neat Trick](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73623) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), April 11, 2020

## External Links

- [Compute the integer absolute value (abs) without branching](http://graphics.stanford.edu/%7Eseander/bithacks.html#IntegerAbs) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
- [Compute the minimum (min) or maximum (max) of two integers without branching](http://graphics.stanford.edu/%7Eseander/bithacks.html#IntegerMinOrMax) by [Sean Eron Anderson](http://graphics.stanford.edu/%7Eseander/)
- [Programming Optimization](http://www.azillionmonkeys.com/qed/optimize.html) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")
- [Avoiding the Cost of Branch Misprediction - Intel® Software Network](https://software.intel.com/en-us/articles/avoiding-the-cost-of-branch-misprediction/) by [Rajiv Kapoor](https://patents.justia.com/inventor/rajiv-kapoor), February 20, 2009
- [Branch (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Branch_%28computer_science%29)
- [Branch table](https://en.wikipedia.org/wiki/Branch_table)
- [Indirect branch](https://en.wikipedia.org/wiki/Indirect_branch)
- [Conditional (programming)](https://en.wikipedia.org/wiki/Conditional_statement)
- [Branch predictor](https://en.wikipedia.org/wiki/Branch_predictor)
- [Branch target predictor](https://en.wikipedia.org/wiki/Branch_target_predictor)
- [Defunkt](Category:Defunkt "Category:Defunkt") - [Avoid The Funk](http://www.allmusic.com/album/avoid-the-funk-a-defunkt-anthology-mw0000197423), Live at [Drom](http://www.dromnyc.com/), April 14, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Joe Bowie](Category:Joseph_Bowie "Category:Joseph Bowie"), [Ronny Drayton](https://en.wikipedia.org/wiki/Ronny_Drayton), [Bill Bickford](https://de.wikipedia.org/wiki/Bill_Bickford), [Kim Clarke](Category:Kim_Clarke "Category:Kim Clarke"), [John Mulkerin](http://johnmulkerin.com/John_Mulkerin/Main.html), [Kenny Martin](http://meinlcymbals.com/artists/Artist/show/kenny-martin-488)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [abs, labs, llabs, \_abs64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abs-labs-llabs-abs64?view=vs-2017) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [\_max](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/max?view=vs-2017) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [\_min](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/min?view=vs-2017) Visual C++ Developer Center - Run-Time Library Reference
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Software Optimization Guide for AMD Family 10h and 12h Processors](https://support.amd.com/techdocs/40546.pdf) (pdf) see pp. 102 on Conditional Write
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Write-combining from Wikipedia](https://en.wikipedia.org/wiki/Write-combining)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Function pointers hurt performance?](http://www.talkchess.com/forum/viewtopic.php?p=425259#425259) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 22, 2011

**[Up one Level](Optimization "Optimization")**

