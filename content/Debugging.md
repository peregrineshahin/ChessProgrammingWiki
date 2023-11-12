---
title: Debugging
---
**[Home](Home "Home") * [Programming](Programming "Programming") * Debugging**

[](http://www.wilhelm-busch-seiten.de/werke/maxundmoritz/streich5.html) Hin und her und rundherum
Kriecht es, fliegt es mit Gebrumm <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Debugging** is a process of finding and reducing [bugs](Engine_Testing#bugs "Engine Testing") in a computer program. A [debugger](https://en.wikipedia.org/wiki/Debugger), usually in software, allows to execute the program (debugee) under its control, to set [breakpoints](https://en.wikipedia.org/wiki/Breakpoint), let the user step to single lines of his source or machine code, to inspect variables, memory and processor registers. Processors often provide special instructions for the purpose of debugging.

## Contents

- [1 x86 Breakpoints](#x86-breakpoints)
- [2 Compiler Support](#compiler-support)
- [3 Debugging the Search](#debugging-the-search)
- [4 See also](#see-also)
- [5 Publications](#publications)
- [6 Forum Posts](#forum-posts)
  - [6.1 2000 ...](#2000-...)
  - [6.2 2005 ...](#2005-...)
  - [6.3 2010 ...](#2010-...)
  - [6.4 2015 ...](#2015-...)
  - [6.5 2020 ...](#2020-...)
- [7 External Links](#external-links)
- [8 References](#references)

## x86 Breakpoints

[8086](8086 "8086"), [x86](X86 "X86") and [x86-64](X86-64 "X86-64") have the [int 3](https://en.wikipedia.org/wiki/INT_%28x86_instruction%29#INT_3) one byte software [interrupt](https://en.wikipedia.org/wiki/Interrupt) instruction with opcode 0xCC, which might be explicitly used, or implicitly in assertions. This instruction is also used, when setting a breakpoint from a debugger, where current opcode is (temporarily) replaced by the *int 3* opcode (0xCC), which when executed calls a special interrupt routine of the debugger or runtime system.

Breakpoint opcode may be inserted inside the code at compile time, for instance with x86 [inline assembly](Assembly#InlineAssembly "Assembly") or compiler intrinsic like *DebugBreak* <a id="cite-note-2" href="#cite-ref-2">[2]</a> :

```C++

  __asm int 3

```

## Compiler Support

Various compiler allow a special Debug build, which disables optimizations, default initialization of otherwise not initialized variables or memory, and/or enable runtime checking, like [bounds checking](https://en.wikipedia.org/wiki/Bounds_checking) of [array](Array "Array") access. Various [integrated development environments](https://en.wikipedia.org/wiki/Integrated_development_environment) (IDE) provide an integrated debugger.

## Debugging the Search

A [recursive](Recursion "Recursion") [search](Search "Search") is quite hard to debug. Therefor chess programs may provide debug routines to use a sequence of certain [moves](Moves "Moves") or a [zobrist key](Zobrist_Hashing "Zobrist Hashing") as a precondition to break the search if they occur. Here are [Tord Romstad's](Tord_Romstad "Tord Romstad") suggestions in a reply to [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

- Extend the [UCI](UCI "UCI")/[XBoard](XBoard "XBoard") command set with a few commands of your own for use in debugging. In particular, it is useful to have a command for looking up the [current position](Root "Root") in the [hash table](Transposition_Table "Transposition Table") and printing the information ([score](Score "Score"), [score type](Score#Type "Score"), [best move](Best_Move "Best Move") , etc). to the standard output. You can use this to browse the [search tree](Search_Tree "Search Tree") after a search is finished. When you want to know why the program discarded some move, you can make the move and inspect the hash table entry for the corresponding position to find the score and refutation. I've found this to be a very valuable debugging technique, and even have a simple [GUI](GUI "GUI") app for browsing the tree (the GUI app communicates with the engine through pipes connected to the standard input and output).
- The technique above can be further enhanced by including lots of additional information in the hash table when debugging the program. I sometimes store complete [move lists](Move_List "Move List") with information about [extension](Extensions "Extensions"), [reduction](Reductions "Reductions") and [pruning](Pruning "Pruning") decisions for each move in every transposition table entry. Of course this makes each entry huge and greatly slows down the search, but it can be useful when chasing bugs or looking for ways to make the search more efficient.
- Implement an [MTD(f)](</MTD(f)> "MTD(f)") search, even if you intend to use [PVS](Principal_Variation_Search "Principal Variation Search"). MTD(f) is great for debugging the hash table; all sorts of obscure bugs which are very tricky to find in PVS or other conventional searches suddenly become easy to spot.
- Whenever you add some non-trivial new function to your program, try to write two versions: One which is very slow and stupid, but almost certainly correct, and one which is highly optimized. Verify on a huge number of positions that they give the same results. Remove the slow version only when you feel 100% sure that the fast version is correct.
- Always make [symmetry tests](Color_Flipping#Debugging "Color Flipping") when you add a new term to your [evaluation function](Evaluation_Function "Evaluation Function") .
- Run through a simple tactical test like [WAC](Win_at_Chess "Win at Chess") at 5 seconds/move every time you change something important in your search. Don't try to optimize the results, but just make sure that the score doesn't suddenly drop dramatically.
- Check the quality of your [move ordering](Move_Ordering "Move Ordering") by measuring how often a [beta cutoff](Beta-Cutoff "Beta-Cutoff") occurs on the first move, and the frequencies with which the 1st, 2nd, 3rd, ... move turns out to be best at [PV nodes](Node_Types#PV "Node Types").

## See also

- [Bibob](Bibob "Bibob")
- [Engine Testing](Engine_Testing "Engine Testing")
- [Famous Bugs](Engine_Testing#bugs "Engine Testing")
- [InBetween](InBetween "InBetween")
- [Logging](Logging "Logging")
- [Perft](Perft "Perft")
- [Spracklens debugging with Apple II ICE](Fidelity_Electronics#SpracklensAppleICE "Fidelity Electronics")

## Publications

- [Zhonghua Yang](index.php?title=Zhonghua_Yang&action=edit&redlink=1 "Zhonghua Yang (page does not exist)"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Global Snapshots for Distributed Debugging*. [ICCI 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icci/icci1992.html#YangM92), pp. 436-440
- [Zhonghua Yang](index.php?title=Zhonghua_Yang&action=edit&redlink=1 "Zhonghua Yang (page does not exist)"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1993**). *Distributed Debugging in the Large*. [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/acsc17.pdf)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1999**). *Computer machen keine Fehler*. [CSS](Computerschach_und_Spiele "Computerschach und Spiele") 2/99, [pdf](http://www.mustrum.de/chrilly/keine_fehler.pdf) (German)
- [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir") (**2006**). *Tools for debugging large game trees*. [11th Game Programming Workshop](http://www.computer-shogi.org/gpw/gpw11_e.html), [Hakone](https://en.wikipedia.org/wiki/Hakone,_Kanagawa), [Japan](https://en.wikipedia.org/wiki/Japan) » [Search Tree](Search_Tree "Search Tree")
- [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir") (**2007**). *GTQL: A Query Language for Game Trees*. M.Sc. thesis, [Reykjavík University](https://en.wikipedia.org/wiki/Reykjav%C3%ADk_University), [pdf](http://www.ru.is/lisalib/getfile.aspx?itemid=9655)
- [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"). (**2008**). *[GTQ: A Language and Tool for Game-Tree Analysis](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_20)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.ru.is/faculty/yngvi/pdf/IsleifsdottirB08.pdf)

## Forum Posts

## 2000 ...

- [Debug Help](https://www.stmintz.com/ccc/index.php?id=129676) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), September 16, 2000
- [Winboard.debug](https://www.stmintz.com/ccc/index.php?id=269311) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 07, 2002 » [WinBoard](WinBoard "WinBoard")
- [bugs, Bugs and BUGS!](https://www.stmintz.com/ccc/index.php?id=367469) by [milix](Anastasios_Milikas "Anastasios Milikas"), [CCC](CCC "CCC"), May 27, 2004
- [Q. Why might node count differ between DEBUG and RELEASE](https://www.stmintz.com/ccc/index.php?id=400603) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), December 13, 2004

## 2005 ...

- [General Tips and Tricks for debugging a search](https://www.stmintz.com/ccc/index.php?id=431392) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), June 15, 2005
- [Testing and debugging chess engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5955) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2006

## [Re: Testing and debugging chess engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5955&start=5) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2006 2010 ...

- [Debugging regression tests](http://www.talkchess.com/forum/viewtopic.php?t=39390) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), June 16, 2011 <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [DrMemory: memory debugger tool for Windows (and Linux)](http://www.talkchess.com/forum/viewtopic.php?t=46968) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), January 22, 2013 » [Memory](Memory "Memory")

## 2015 ...

- [OT: Finding the Line of the Assert Fail?](http://www.talkchess.com/forum/viewtopic.php?t=55578) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), March 07, 2015 » [Maverick](Maverick "Maverick")
- [Best way to debug perft?](http://www.talkchess.com/forum/viewtopic.php?t=59046) by Meni Rosenfeld, [CCC](CCC "CCC"), January 25, 2016 » [Perft](Perft "Perft")
- [Best way to debug search speed?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=60912) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), July 23, 2016
- [Help with Debugging My Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=61551) by Pranav Deshpande, [CCC](CCC "CCC"), September 28, 2016
- [Help with Debugging My Chess Engine - 2](http://www.talkchess.com/forum/viewtopic.php?t=61565) by Pranav Deshpande, [CCC](CCC "CCC"), September 30, 2016
- [How to go about chasing a bug like this?](http://www.talkchess.com/forum/viewtopic.php?t=63119) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), February 09, 2017
- [How to find SMP bugs ?](http://www.talkchess.com/forum/viewtopic.php?t=63454) by Lucas Braesch, [CCC](CCC "CCC"), March 15, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP")
- [assert](http://www.talkchess.com/forum/viewtopic.php?t=65712) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), November 13, 2017 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [How do I debug cutechess-cli engine input/output?](http://www.talkchess.com/forum/viewtopic.php?t=66124) by [Daniel Dugovic](index.php?title=Daniel_Dugovic&action=edit&redlink=1 "Daniel Dugovic (page does not exist)"), [CCC](CCC "CCC"), December 25, 2017 » [Cutechess-cli](Cutechess-cli "Cutechess-cli")
- [Debugging UCI engine](http://www.talkchess.com/forum/viewtopic.php?t=66366) by Cadel Watson, [CCC](CCC "CCC"), January 19, 2018 » [InBetween](InBetween "InBetween"), [UCI](UCI "UCI")
- [Debugging a transposition table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67599) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), May 29, 2018 » [Transposition Table](Transposition_Table "Transposition Table"), [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position")

## 2020 ...

- [Engine Crash Detective Story](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74931) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), August 29, 2020 » [MadChess](MadChess "MadChess")
- [Resolving once in a trillion crashes](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79160) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 18, 2022 » [Ethereal](Ethereal "Ethereal")

## External Links

- [Debugging from Wikipedia](https://en.wikipedia.org/wiki/Debug)
- [Debugger from Wikipedia](https://en.wikipedia.org/wiki/Debugger)
- [Assertion (software development) from Wikipedia](<https://en.wikipedia.org/wiki/Assertion_(software_development)>)
- [Regression testing from Wikipedia](https://en.wikipedia.org/wiki/Regression_testing)
- [GDB: The GNU Project Debugger](http://www.gnu.org/software/gdb/)
- [gdb + eclipse - SWiK](http://swik.net/gdb+eclipse)
- [IDA Pro Disassembler - multi-processor, windows hosted disassembler and debugger](http://www.hex-rays.com/idapro/)
- [SoftICE from Wikipedia](https://en.wikipedia.org/wiki/SoftICE)
- [CHESS - Microsoft Research](http://research.microsoft.com/en-us/projects/chess/) a tool for finding and reproducing [Heisenbugs](https://en.wikipedia.org/wiki/Unusual_software_bug) in concurrent programs.
- [From Chapter 5, Debugging](http://cm.bell-labs.com/cm/cs/tpop/debugging.html) excerpt from Chapter 5 of

[Brian W. Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan), [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike) (**1999**). *[The Practice of Programming](https://en.wikipedia.org/wiki/The_Practice_of_Programming)*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley), ISBN: ISBN 0-201-61586-X

- [Electric Fence (Memory Debugger) from Wikipedia](https://en.wikipedia.org/wiki/Electric_Fence) » [Memory](Memory "Memory")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wilhelm-Busch](https://en.wikipedia.org/wiki/Wilhelm_Busch), [Max und Moritz - Fünfter Streich](http://www.wilhelm-busch-seiten.de/werke/maxundmoritz/streich5.html) from [Wilhelm-Busch Seiten von Jochen Schöpflin](http://www.wilhelm-busch-seiten.de/index.html) (German)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [DebugBreak Function (Windows)](http://msdn.microsoft.com/en-us/library/ms679297%28VS.85%29.aspx) from [Develop for Windows 7 and Windows Vista | MSDN](http://msdn.microsoft.com/en-us/default.aspx)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a>  [Re: Testing and debugging chess engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5955&start=5) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2006
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Regression testing from Wikipedia](https://en.wikipedia.org/wiki/Regression_testing)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Assertion (software development) from Wikipedia](<https://en.wikipedia.org/wiki/Assertion_(software_development)>)

**[Up one Level](Programming "Programming")**

