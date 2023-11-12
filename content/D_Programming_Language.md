---
title: D Programming Language
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * D-Programming Language**

**D**,

a programming language developed by [Walter Bright](https://en.wikipedia.org/wiki/Walter_Bright) from [Digital Mars](https://en.wikipedia.org/wiki/Digital_Mars) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The first stable version was released 2007. Walter Bright designed many other compilers as the first native compiler, the [Zortech](https://en.wikipedia.org/wiki/Zortech) [C++](Cpp "Cpp") compiler, the [Symantec](https://en.wikipedia.org/wiki/Symantec) C++ compiler, and the Digital Mars C++ Compiler and many [C](C "C") compilers (as the [Datalight](https://en.wikipedia.org/wiki/Datalight) C compiler).
[Andrej Alexandrescu](https://en.wikipedia.org/wiki/Andrei_Alexandrescu) joined the design and development effort in 2007. D is a distinct language and has redesigned some core C++ features, while also sharing characteristics from [Java](Java "Java"), [Python](Python "Python"), [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)"), [C#](C_sharp "C sharp"), and [Eiffel](<https://en.wikipedia.org/wiki/Eiffel_(programming_language)>) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
D is in the Top 20 of the [TIOBE index](https://en.wikipedia.org/wiki/TIOBE_index) <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Design Principles

The design principles have been to write a compiler for a language that:

- is **fast** without any compromise
- has a **clean syntax** free of the [C++](Cpp "Cpp") quirks
- has all **modern concepts** of [interpreted languages](https://en.wikipedia.org/wiki/Interpreted_language). In fact D has some [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)") + [Python](Python "Python") elements that make **programming fun**.
- is **easy** to learn for [C](C "C") and C++ programmers

## Native Features

- Easy string handling
- Static and dynamic [arrays](Array "Array") + [hashes](Hash_Table "Hash Table")
- [Overloading](https://en.wikipedia.org/wiki/Function_overloading), default parameters, varargs
- Direct [C](C "C") access and debugger support
- [Contract programming](https://en.wikipedia.org/wiki/Design_by_contract)
- Subset of constructs for easy [functional programming](https://en.wikipedia.org/wiki/Functional_programming)
- Nested functions (as Macros)
- Classes and inheritance and Modules/Mixins and templates
- Advanced testing features as contract programming and class invariants
- [Thread](Thread "Thread") and [fiber](https://en.wikipedia.org/wiki/Fiber_%28computer_science%29) support (actors in work)
- [Exception handling](https://en.wikipedia.org/wiki/Exception_handling)
- Automatic or explicit [garbage collection](https://en.wikipedia.org/wiki/Garbage_collection_%28computer_science%29): use internal GC or [free / malloc](https://en.wikipedia.org/wiki/Malloc) as you like.
- [Closures](https://en.wikipedia.org/wiki/Closure_%28computer_science%29)
- and more...

## Suitable for Chess Programming

D might be a competitive choice for chess programming because:

- The performance / **speed** is comparable to C / C++
- It has **ulong** (8 bytes) and is very data-type rich

Althought it looks like D has advantages over C/C++ in terms if a modern language, two possible problems might be worth to know

- [Bit-twiddling](Bit-Twiddling "Bit-Twiddling") optimizations
- Impact of [Garbage collection](<https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)>) on predictable results

## D Engines

- [Chess Engines written in D](Category:D-Proglanguage "Category:D-Proglanguage")

## Publications

- [Andrej Alexandrescu](https://en.wikipedia.org/wiki/Andrei_Alexandrescu) (**2010**). *[The D Programming Language](https://www.oreilly.com/library/view/the-d-programming/9780321659538/)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley) Professional <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## Forum Posts

- [digitalmars.D - gdc and the Computer Language Benchmarks Game](http://www.digitalmars.com/d/archives/digitalmars/D/gdc_and_the_Computer_Language_Benchmarks_Game_55053.html#N55053) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [digitalmars.D](http://dlang.org/index.html), June 28, 2007
- [Re: c vs c++](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=414767&t=39683) by [Brian Haskin](index.php?title=Brian_Haskin&action=edit&redlink=1 "Brian Haskin (page does not exist)"), [CCC](CCC "CCC"), July 14, 2011
- [Are there any chess engines written in D?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=49675) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), October 12, 2013
- [programming languages - What does C++ do better than D? - Programmers - Stack Exchange](http://programmers.stackexchange.com/questions/97207/what-does-c-do-better-than-d)

## External Links

- [Home - D Programming Language](https://dlang.org/)
- [D from Wikipedia](https://en.wikipedia.org/wiki/D_programming_language)
- [Intro - D Programming Language 2.0 - Digital Mars](https://digitalmars.com/d/2.0/index.html)
- [GDC - D Programming Language for GCC](https://gdcproject.org/)
- [D-Programming-GDC · GitHub](https://github.com/D-Programming-GDC)
- [Wiki4D: FrontPage](http://www.prowiki.org/wiki4d/wiki.cgi)
- [DConf 2019](https://dconf.org/2019/index.html) Day 1 [Keynote](https://dconf.org/2019/talks/bright.html): Allocating Memory with the D Programming Language - [Walter Bright](https://en.wikipedia.org/wiki/Walter_Bright), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The D Programming Language - Walter Bright Interview](http://bitwisemag.co.uk/copy/programming/d/interview/d_programming_language.html) by [Huw Collingbourne](http://bitwisemag.co.uk/copy/bios/bio_huw_collingbourne.html) and [Dermot Hogan](http://bitwisemag.co.uk/copy/bios/bio_dermot_hogan.html), [Bitwise Magazine](http://www.bitwisemag.com/index.html)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [The A-Z of Programming Languages: D - Walter Bright talks about D and his desire to improve on systems programming language](https://www.computerworld.com/article/3475025/the-a-z-of-programming-languages-d.html), [Computerworld](Computerworld "Computerworld")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [D (programming language) from Wikipedia](<https://en.wikipedia.org/wiki/D_(programming_language)>)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [TIOBE Software: Tiobe Index](https://www.tiobe.com/tiobe-index//)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> The D Programming Language with [Andrei Alexandrescu](https://erdani.com/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

**[Up one Level](Languages "Languages")**

