---
title: CGoto
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * C**

\[ The C Programming Language <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**C**,

a pragmatical, general purpose, [block structured](https://en.wikipedia.org/wiki/Statement_block), [procedural](https://en.wikipedia.org/wiki/Procedural_programming), [imperative](https://en.wikipedia.org/wiki/Imperative_programming) [programming language](https://en.wikipedia.org/wiki/Programming_language). C was developed in **1972** by [Dennis Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie) at the [Bell Laboratories](Bell_Laboratories "Bell Laboratories"). It was first intended as a [system](https://en.wikipedia.org/wiki/System_software) programming language for the [Unix](Unix "Unix") operating system, but has spread to many other platforms and application programming as well. C and its derivations are likely the most often used languages so far for computer chess programming.

## Contents

- [1 Revisions](#revisions)
- [2 See also](#see-also)
- [3 Data](#data)
  - [3.1 Data Types](#data-types)
    - [3.1.1 Basic Data Types](#basic-data-types)
    - [3.1.2 Pointer](#pointer)
    - [3.1.3 Array](#array)
    - [3.1.4 Struct](#struct)
    - [3.1.5 Bitfield](#bitfield)
    - [3.1.6 Union](#union)
  - [3.2 Variables](#variables)
- [4 Instructions](#instructions)
  - [4.1 Expressions](#expressions)
  - [4.2 Functions](#functions)
  - [4.3 Operators](#operators)
  - [4.4 Control Flow](#control-flow)
    - [4.4.1 Goto](#goto)
    - [4.4.2 If else](#if-else)
    - [4.4.3 Switch case](#switch-case)
    - [4.4.4 Function Pointer](#function-pointer)
    - [4.4.5 For](#for)
    - [4.4.6 While](#while)
    - [4.4.7 Do while](#do-while)
- [5 Preprocessor](#preprocessor)
- [6 Portabilty](#portabilty)
- [7 Libraries](#libraries)
- [8 C and C++ Compiler](#c-and-c.2b.2b-compiler)
- [9 Publications](#publications)
  - [9.1 1978 ...](#1978-...)
  - [9.2 2010 ...](#2010-...)
- [10 Forum Posts](#forum-posts)
  - [10.1 1999](#1999)
  - [10.2 2000 ...](#2000-...)
  - [10.3 2005 ...](#2005-...)
  - [10.4 2010 ...](#2010-...-2)
  - [10.5 2015 ...](#2015-...)
  - [10.6 2020 ...](#2020-...)
- [11 External Links](#external-links)
- [12 References](#references)

## Revisions

Due to explicit [pointers](<https://en.wikipedia.org/wiki/Pointer_(computer_programming)>) (address of a variable or function), C might be considered as a high level assembly language, and has some weak spots in its initial design and implementation, which are addressed in

- [ANSI C from Wikipedia](https://en.wikipedia.org/wiki/ANSI_C)
- [C99 from Wikipedia](https://en.wikipedia.org/wiki/C99)
- [C11 (C standard revision) from Wikipedia](https://en.wikipedia.org/wiki/C11_%28C_standard_revision%29)
- [C18 (C standard revision) from Wikipedia](<https://en.wikipedia.org/wiki/C18_(C_standard_revision)>)

## See also

- [CFish](CFish "CFish")
- [C++](Cpp "Cpp")
- [C#](C_sharp "C sharp")
- [D (Programming Language)](</D_(Programming_Language)> "D (Programming Language)")
- [Go (Programming Language)](</Go_(Programming_Language)> "Go (Programming Language)")
- [Java](Java "Java")

## Data

## Data Types

[C data types](https://en.wikipedia.org/wiki/C_data_types) are declarations for memory locations for basic and compound data.

### Basic Data Types

The C language provides the four basic arithmetic type specifiers char, int, float and double, and the modifiers signed, unsigned, short and long. C99 added a boolean (true/false) type \_Bool.

*To be aware of the scalar 64-bit origin of [bitboards](Bitboards "Bitboards") in computer chess, we use so far a type defined unsigned integer U64 in our C and [C++](Cpp "Cpp") source snippets. The macro C64 will append a suffix to 64-bit constants as required by some compilers*:

```C++

typedef unsigned __int64 U64;    // for the old microsoft compilers
typedef unsigned long long  U64; // supported by MSC 13.00+ and C99
##define C64(constantU64) constantU64##ULL

```

### Pointer

A [pointer](https://en.wikipedia.org/wiki/C_data_types#Pointers) is a data type that contains the address of a storage location of a variable (or function).
They are declared with the asterisk (\*) type declarator following the basic storage type and preceding the variable name of the pointer.

```C++

int * ptr2int;

```

### Array

An [array](Array "Array") is a collection of values, all of the same type, stored contiguously in memory. An array of size N is indexed by integers from 0 up to and including N−1.

```C++

unsigned int moves[256];
char *pc[10];  /* array of 10 elements of 'pointer to char' */
char (*pa)[10]; /* pointer to a 10-element array of char */

```

In C, array indexing is formally defined in terms of pointer arithmetic; that is, the language specification requires that `array[i]` be equivalent to `*(array + i)`.

### Struct

A structure in C refers to [Object composition](https://en.wikipedia.org/wiki/Object_composition) to encapsulate related scalar datatypes inside one structured item. The size of the structure is the sum of its element sizes. To access the structure elements the dot-operator separates the element from the variable or reference. Pointers require arrow operator.

```C++

struct MOVE
{
  char from;
  char to;
};

...
MOVE m, a, *b;
m.from = square;
...
if ( a.from == b->to )

```

### Bitfield

So called [Bitfields](https://en.wikipedia.org/wiki/Bit_field) might be implemented as structure where integer members are declared with explicit bit length specifier from 1 .. 31. However due to portability issues of various C-compilers and platforms concerning bit ordering, padding and eventually the sign, most programmer rely on explicit bitfields to composite and extract sub-items by shift and masks, i.e. in [encoding moves](Encoding_Moves "Encoding Moves").

```C++

struct DoubleLayout
{
  unsigned int mantissal : 32;
  unsigned int mantissah : 20;
  unsigned int exponent : 11;
  unsigned int sign : 1;
};

```

### Union

A [value](https://en.wikipedia.org/wiki/Union_type#C/C++) that may have any of several representations within the same position in memory.

```C++

union BitBoard 
{
  U64 qw;
  U32 dw[2];
};

```

## Variables

[Variables](<https://en.wikipedia.org/wiki/Variable_(computer_science)#Scope_and_extent>) are stored either in various memory areas or kept inside processor registers (if not referred by a pointer) as:

- [Global](https://en.wikipedia.org/wiki/Global_variable) or [Static Variable](https://en.wikipedia.org/wiki/Static_variable) in static memory
- [Local Variable](https://en.wikipedia.org/wiki/Local_variable) as [Automatic Variable](https://en.wikipedia.org/wiki/Automatic_variable) on the [Stack](https://en.wikipedia.org/wiki/Stack-based_memory_allocation)\]
- Local Variable as Automatic Variable inside a [Processor Register](https://en.wikipedia.org/wiki/Processor_register)
- [Dynamic memory allocation on the Heap](https://en.wikipedia.org/wiki/C_dynamic_memory_allocation#Heap-based)

## Instructions

## Expressions

An [expression](<https://en.wikipedia.org/wiki/Expression_(computer_science)>) in a programming language is a combination of one or more constants, variables, operators, and functions.

## Functions

- [C mathematical functions from Wikipedia](https://en.wikipedia.org/wiki/C_mathematical_functions)

## Operators

- [Assignment](<https://en.wikipedia.org/wiki/Assignment_operator_(C%2B%2B)>) =
- [Arithmetical](https://en.wikipedia.org/wiki/Arithmetic#Arithmetic_operations) +, -, \*, /, %, ++, --
- [Bitwise](https://en.wikipedia.org/wiki/Bitwise_operations_in_C) &, |, ^, ~, [>>, \<\<](https://en.wikipedia.org/wiki/Bitwise_operation#Bit_shifts)
- [Augmented assignment](https://en.wikipedia.org/wiki/Augmented_assignment) +=, -=. \*=, /=, %=, &=, |=, ^=, \<\<=, >>=
- [Relational](https://en.wikipedia.org/wiki/Relational_operator#B_and_C) ==, \<, >, \<=, >=, !=
- [Boolean](https://en.wikipedia.org/wiki/Boolean_algebra) !, &&, ||
- [Conditional](https://en.wikipedia.org/wiki/%3F:) ?:
- [Comma](https://en.wikipedia.org/wiki/Comma_operator) ,
- [sizeof](https://en.wikipedia.org/wiki/Sizeof)

## Control Flow

- [Control flow from Wikipedia](https://en.wikipedia.org/wiki/Control_flow)

### Goto

- [Goto from Wikipedia](https://en.wikipedia.org/wiki/Goto)
- [Considered harmful from Wikipedia](https://en.wikipedia.org/wiki/Considered_harmful)<a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [Using gotos](http://stevemcconnell.com/ccgoto.htm) by [Steve McConnell](http://www.stevemcconnell.com/aboutme.htm) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

### If else

- [Conditional (computer programming) from Wikipedia](https://en.wikipedia.org/wiki/Conditional_%28computer_programming%29)

### Switch case

- [Switch statement from Wikipedia](https://en.wikipedia.org/wiki/Switch_statement)

### Function Pointer

- [Function pointer from Wikipedia](https://en.wikipedia.org/wiki/Function_pointer)

### For

- [For loop from Wikipedia](https://en.wikipedia.org/wiki/For_loop)

### While

- [While loop from Wikipedia](https://en.wikipedia.org/wiki/While_loop)

### Do while

- [Do while loop from Wikipedia](https://en.wikipedia.org/wiki/Do_while_loop)
- [The amazing Duff's Device](http://doc.cat-v.org/bell_labs/duffs_device) by [Tom Duff](https://en.wikipedia.org/wiki/Tom_Duff)
- [Duff's Device from Wikipedia](https://en.wikipedia.org/wiki/Duff%27s_device)

```C++

send(to, from, count)
  register short *to, *from;
  register count;
  {
    register n=(count+7)/8;
    switch(count%8){
    case 0: do{ *to = *from++;
    case 7:     *to = *from++;
    case 6:     *to = *from++;
    case 5:     *to = *from++;
    case 4:     *to = *from++;
    case 3:     *to = *from++;
    case 2:     *to = *from++;
    case 1:     *to = *from++;
        } while(--n > 0);
    }
  }

```

## Preprocessor

- [C preprocessor from Wikipedia](https://en.wikipedia.org/wiki/C_preprocessor)

## Portabilty

- [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement)
- [sizeof](https://en.wikipedia.org/wiki/Sizeof)
- [shift](https://en.wikipedia.org/wiki/Arithmetic_shift)
- [Endianness](Endianness "Endianness")

## Libraries

- [C standard library](https://en.wikipedia.org/wiki/C_standard_library) (libc)

## C and C++ Compiler

A [C-Compiler](https://en.wikipedia.org/wiki/List_of_compilers#C_compilers) is used to translate the source program, usually [ascii-text](https://en.wikipedia.org/wiki/ASCII) files with the extension .C, to so called [object files](https://en.wikipedia.org/wiki/Object_file), containing machine instructions. A [linker](<https://en.wikipedia.org/wiki/Linker_(computing)>) binds all the object files together with libraries containing external functions (and data) to build an executable program.

- [AMD Optimizing C/C++ Compiler](https://en.wikipedia.org/wiki/AMD_Optimizing_C/C%2B%2B_Compiler)
- [Clang](https://en.wikipedia.org/wiki/Clang)
- [CompCert](https://en.wikipedia.org/wiki/CompCert)
- [GNU C Compiler](Free_Software_Foundation#GCC "Free Software Foundation")
- [Intel](Intel "Intel") [C++](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler)
- [Interactive C](https://en.wikipedia.org/wiki/Interactive_C)
- [LCC (compiler)](<https://en.wikipedia.org/wiki/LCC_(compiler)>)
- [Microsoft](Microsoft "Microsoft") [Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B)
- [Pelles C](http://www.smorgasbordet.com/pellesc/)
- [Tiny C Compiler](https://en.wikipedia.org/wiki/Tiny_C_Compiler)

## Publications

## 1978 ...

- [Brian W. Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan), [Dennis M. Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie) (**1978, 1988**). *[The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language)*. First Edition ISBN 0-13-110163-3, Second Edition ISBN 0-13-110362-8
- [Andrew Koenig](Andrew_Koenig "Andrew Koenig") (**1989**). *[C Traps and Pitfalls](https://en.wikipedia.org/wiki/C_Traps_and_Pitfalls)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley), [pdf preprint](http://literateprogramming.com/ctraps.pdf)
- [Patrick Winston](Patrick_Winston "Patrick Winston") (**1994**). *[On To C](http://people.csail.mit.edu/phw/Books/index.html#OnToC)*. [On-Line](http://people.csail.mit.edu/phw/OnToC/)
- [Andrew Appel](index.php?title=Andrew_Appel&action=edit&redlink=1 "Andrew Appel (page does not exist)"), [Maia Ginsburg](https://dblp.uni-trier.de/pers/hd/g/Ginsburg:Maia) (**1998**). *[Modern Compiler Implementation in C](https://www.cs.princeton.edu/~appel/modern/c/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
- [Erik D. Demaine](Erik_D._Demaine "Erik D. Demaine") (**1998**). *[C to Java: Converting Pointers into References](http://erikdemaine.org/papers/CPE98/)*. [Concurrency: Practice and Experience, Vol. 10](https://dblp.org/db/journals/concurrency/concurrency10.html), Nos. 11-13

## 2010 ...

- [Robert C. Seacord](https://en.wikipedia.org/wiki/Robert_C._Seacord) (**2010**). *Dangerous Optimizations and the Loss of Causality*. CS 15-392 © 2010 [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [slides as pdf](https://pubweb.eng.utah.edu/~cs5785/slides-f10/Dangerous+Optimizations.pdf)
- [Xi Wang](https://pdos.csail.mit.edu/~xi/), [Haogang Chen](https://pdos.csail.mit.edu/~hchen/), [Alvin Cheung](https://homes.cs.washington.edu/~akcheung/), [Zhihao Jia](http://zhihaojia.com/), [Nickolai Zeldovich](http://people.csail.mit.edu/nickolai/), [M. Frans Kaashoek](https://pdos.csail.mit.edu/~kaashoek/) (**2012**). *Undefined Behavior: What Happened to My Code*? [pdf](https://pdos.csail.mit.edu/papers/ub:apsys12.pdf)
- [Will Dietz](https://wdtz.org/), [Peng Li](https://lipeng28.github.io/), [John Regehr](http://www.cs.utah.edu/~regehr/), [Vikram Adve](https://en.wikipedia.org/wiki/Vikram_Adve) (**2012**). *Understanding Integer Overflow in C/C++*. [pdf](https://www.cs.utah.edu/~regehr/papers/overflow12.pdf)

## Forum Posts

## 1999

- [C or C++ for chess programming: speed](https://www.stmintz.com/ccc/index.php?id=74219) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), October 20, 1999

## 2000 ...

- [One (silly) question about "C"](https://www.stmintz.com/ccc/index.php?id=211975) by Antonio Senatore, [CCC](CCC "CCC"), February 05, 2002

## 2005 ...

- [Re: chess engines writen in C](https://www.stmintz.com/ccc/index.php?id=405552) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), January 13, 2005
- [ansi-C question](http://www.talkchess.com/forum/viewtopic.php?t=21673) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), June 08, 2008
- [setjmp() - another one](http://www.talkchess.com/forum/viewtopic.php?t=23292) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), August 27, 2008
- [kbhit() taking huge CPU??](http://www.talkchess.com/forum/viewtopic.php?t=27279) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), April 01, 2009 » [Thread](Thread "Thread")
- [Critter: Pascal vs C](http://www.talkchess.com/forum/viewtopic.php?t=29562) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), August 27, 2009 » [Pascal](Pascal "Pascal")

## 2010 ...

- [MSVC calloc question](http://www.talkchess.com/forum/viewtopic.php?t=38441) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 17, 2011
- [My experience with Linux/GCC](http://www.talkchess.com/forum/viewtopic.php?t=38523) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), March 23, 2011 » [Linux](Linux "Linux")
- [a cautionary tale about simple-looking macros](http://www.talkchess.com/forum/viewtopic.php?t=39587) by [Wylie Garvin](index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](CCC "CCC"), July 03, 2011
- [c or c++ ?](http://talkchess.com/forum/viewtopic.php?t=39683) by ethan ara, [CCC](CCC "CCC"), July 10, 2011
- [VisualStudio - \_\_fastcall instead of \_\_cdecl?](http://www.talkchess.com/forum/viewtopic.php?t=44111) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), June 18, 2012
- [C vs ASM](http://www.talkchess.com/forum/viewtopic.php?t=47414) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 05, 2013 » [Assembly](Assembly "Assembly")
- [Re: goto thread (split)](http://www.talkchess.com/forum/viewtopic.php?t=48812&start=6) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 01, 2013 » [Iterative Search](Iterative_Search "Iterative Search"), [Symbolic](Symbolic "Symbolic")
- [A note for C programmers](http://www.talkchess.com/forum/viewtopic.php?t=50186) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 23, 2013

[Re: A note for C programmers](http://www.talkchess.com/forum/viewtopic.php?t=50186&start=80) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), November 28, 2013

- [A note on strcpy](http://www.open-chess.org/viewtopic.php?f=5&t=2519) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 26, 2013
- [strcpy() revisited](http://www.talkchess.com/forum/viewtopic.php?t=50387) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 08, 2013

## 2015 ...

- [Using more than 1 thread in C beginner question](http://www.talkchess.com/forum/viewtopic.php?t=58882) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 11, 2016 » [Thread](Thread "Thread")
- [C programming style question](http://www.talkchess.com/forum/viewtopic.php?t=58967) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 19, 2016
- [Crafty c questions](http://www.talkchess.com/forum/viewtopic.php?t=59464) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), March 10, 2016 » [Crafty](Crafty "Crafty")
- [I'm not very happy with the do {} while() statement in C](http://www.talkchess.com/forum/viewtopic.php?t=66624) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), February 18, 2018
- [Writing bugs](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69512) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 06, 2019

## 2020 ...

- [Java vs C. It's not like one would think](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74256) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), June 22, 2020 » [OliThink](OliThink "OliThink"), [Java](Java "Java")

## External Links

- [C from Wikipedia](https://en.wikipedia.org/wiki/C_%28programming_language)
- [C Programming - Wikibooks](https://en.wikibooks.org/wiki/C_Programming)
- [The C Book - Table of Contents](https://publications.gbdirect.co.uk//c_book/), an online version of the popular introduction and reference on the ANSI Standard C programming language
- [Programming Bits](http://www.azillionmonkeys.com/qed/programming.html) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")
- [comp.lang.c](https://groups.google.com/forum/#!forum/comp.lang.c) Discussion about C
- [comp.lang.c Frequently Asked Questions](http://c-faq.com/index.html)
- [Chess Engine In C](https://www.youtube.com/playlist?list=PLZ1QII7yudbc-Ky058TEaOstZHVbT-2hg) - [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos by [BlueFeverSoft](BlueFeverSoft "BlueFeverSoft") » [Vice](Vice "Vice")
- [How to C in 2016](https://matt.sh/howto-c)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The cover to the book, [Brian W. Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan), [Dennis M. Ritchie](https://en.wikipedia.org/wiki/Dennis_Ritchie) (**1978, 1988**). *[The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language)*. First Edition
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Edsger Dijkstra](https://en.wikipedia.org/wiki/Edsger_Dijkstra) (**1968**). *Go To Statement Considered Harmful*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 11, No. 3, [pdf](http://www.cs.utexas.edu/users/EWD/ewd02xx/EWD215.PDF)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [William A. Wulf](Mathematician#WiWulf "Mathematician") (**1971**). *Programming Without the GOTO*. [IFIP](IFIP "IFIP"), Ljubljana, Yugoslavia, August 1971
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [William A. Wulf](Mathematician#WiWulf "Mathematician") (**1972**). *A Case Against the GOTO*. Proceedings of the [ACM](ACM "ACM") National Conference, Boston, August 197
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Donald Knuth](Donald_Knuth "Donald Knuth") (**1974**). *Structured Programming with go to Statements*. [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 6, No. 4, [pdf](http://cs.sjsu.edu/~mak/CS185C/KnuthStructuredProgrammingGoTo.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Ward Douglas Maurer](Ward_Douglas_Maurer "Ward Douglas Maurer") (**1996**). *[Attitudes toward the go-to statement (or, hydrogen considered harmful)](http://dl.acm.org/citation.cfm?id=238417)*. [Computers & Education](http://www.journals.elsevier.com/computers-and-education/), Vol. 26, No. 4
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Coding Horror: I'd Consider That Harmful, Too](http://www.codinghorror.com/blog/2007/10/id-consider-that-harmful-too.html) by [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood), October 25, 2007
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Steve McConnell](http://www.stevemcconnell.com/aboutme.htm) (**1993**). *[Code Complete: A Practical Handbook of Software Construction](http://www.stevemcconnell.com/cc1.htm)*. [Microsoft Press](https://en.wikipedia.org/wiki/Microsoft_Press)

**[Up one Level](Languages "Languages")**

