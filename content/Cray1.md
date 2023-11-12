---
title: Cray1
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * Cray-1**

[](http://www.computerhistory.org/revolution/supercomputers/10/7/3) [Seymour Cray](https://en.wikipedia.org/wiki/Seymour_Cray) in front of his Cray-1 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cray-1**,

a [supercomputer](https://en.wikipedia.org/wiki/Supercomputer) designed, manufactured and marketed by [Cray Research Inc.](https://en.wikipedia.org/wiki/Cray#Cray_Research_Inc._and_Cray_Computer_Corporation:_1972_to_1996) since 1972. The first Cray-1 system was installed at [Los Alamos National Laboratory](Los_Alamos_National_Laboratory "Los Alamos National Laboratory") in 1976 and it went on to become one of the best known and most successful supercomputers in history, it reigned as the world’s fastest from 1976 to 1982 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Cray Research was founded by former [Control Data Corporation](https://en.wikipedia.org/wiki/Control_Data_Corporation) chief designer [Seymour Cray](https://en.wikipedia.org/wiki/Seymour_Cray) <a id="cite-note-3" href="#cite-ref-3">[3]</a>, after CDC neglected to invest in Seymour Cray's [CDC 8600](https://en.wikipedia.org/wiki/CDC_8600) design.

## Architecture

The Cray-1 is a large-scale, general-purpose digital computer featuring scalar as well as [vector processing](https://en.wikipedia.org/wiki/Vector_processor), a 12.5 nanosecond clock period, and a 50 nanosecond memory cycle time. The basic configuration of the Cray-1 consists of the [central processor unit](https://en.wikipedia.org/wiki/Central_processing_unit) (CPU), one or more minicomputer [consoles](https://en.wikipedia.org/wiki/System_console), and a [mass storage](https://en.wikipedia.org/wiki/Mass_storage) (disk) subsystem.

## CPU

The CPU holds the [ALU](Combinatorial_Logic#ALU "Combinatorial Logic"), [memory](Memory "Memory"), and [I/O sections](https://en.wikipedia.org/wiki/Input/output) of the computer. It is constructed from [LSI chips](https://en.wikipedia.org/wiki/Integrated_circuit#LSI) of high-speed [ECL](https://en.wikipedia.org/wiki/Emitter-coupled_logic) [bipolar junction transistors](https://en.wikipedia.org/wiki/Bipolar_junction_transistor). Memory is build from 1024-bit LSI chips of up to one [mebi](https://en.wikipedia.org/wiki/Binary_prefix) 72-bit words, arranged in 16 banks. A [word](Word "Word") consists of 64 data bits and 8 check bits which allows [single-error correction double-error detection](https://en.wikipedia.org/wiki/Hamming_code) (SECDED).

## Registers

Three primary [register](https://en.wikipedia.org/wiki/Processor_register) sets consists of eight 24-bit [address](https://en.wikipedia.org/wiki/Memory_address) registers (also loop counter, shift counts), eight 64-bit scalar registers, and eight vector registers, where one vector register is actually a set of 64 64-bit registers, called elements. Associated with the vector registers are a 7-bit vector length register and a 64-bit vector mask register to allow operations to be performed on individual vector elements.

[](http://www.chrisfenton.com/homebrew-cray-1a/)
Register and ALU Block Diagram <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Instructions

The Cray-1 executes 128 operation codes as either 16-bit (register reference) or 32-bit (memory reference) scalar or [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") instructions. An integer multiply operation produces a 24-bit result, additions and subtractions either 24-bit or 64-bit results. Integer divide is not provided. The instruction set includes boolean operations for [OR](Combinatorial_Logic#OR "Combinatorial Logic"), [AND](Combinatorial_Logic#AND "Combinatorial Logic"), and [exclusive OR](Combinatorial_Logic#XOR "Combinatorial Logic") and for a mask-controlled merge operation. Shift operations allow the manipulation of 64- or 128-bit operands to produce a 64-bit result. Instructions for scalar [population](Population_Count "Population Count") and [leading zero](BitScan#LeadingZeroCount "BitScan") counts return bit counts based on scalar register contents to an address register.

The Cray design used [pipeline parallelism](https://en.wikipedia.org/wiki/Pipeline_%28computing%29) to implement vector instructions rather than multiple [ALUs](Combinatorial_Logic#ALU "Combinatorial Logic") . In addition the design had completely separate pipelines for different instructions, for example, addition/subtraction was implemented in different hardware than multiplication. This allowed a batch of vector instructions themselves to be pipelined, a technique called vector chaining. The Cray-1 normally had a performance of about 80 [MFLOPS](https://en.wikipedia.org/wiki/FLOPS), but with up to three chains running it could peak at 240 MFLOPS <a id="cite-note-5" href="#cite-ref-5">[5]</a> .

## Chess Programs

- [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Cube](Cube "Cube")
- [Nuchess](Nuchess "Nuchess")

## See also

- [CDC 6600](CDC_6600 "CDC 6600")
- [CDC Cyber](CDC_Cyber "CDC Cyber")
- [Cray X-MP](Cray_X-MP "Cray X-MP")
- [Cray T3D](Cray_T3D "Cray T3D")
- [Cray T3E](Cray_T3E "Cray T3E")

## Manuals

- [The CRAY-1 Computer System](http://archive.computerhistory.org/resources/text/Cray/Cray.Cray1.1977.102638650.pdf) (pdf)
- [CAL Assembly Reference Manual](http://bitsavers.informatik.uni-stuttgart.de/pdf/cray/CAL/2240000B_Prelim_CAL_RefMan_Dec75.pdf) (pdf)

## Publications

- [Richard M. Russell](https://scholar.google.com/citations?user=SID57mMAAAAJ&hl=en) (**1978**). *The CRAY-1 computer system*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 21, No. 1, [pdf](http://inst.eecs.berkeley.edu/~cs252/sp17/papers/Cray1.pdf)
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *The Cray-1 Plays Chess (Part 1)*. [Personal Computing, Vol. 5, No. 1](Personal_Computing#5_1 "Personal Computing"), pp. 83
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *The Cray-1 Plays Chess (Part 2)*. [Personal Computing, Vol. 5, No. 2](Personal_Computing#5_2 "Personal Computing"), pp. 95 » [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 1](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d2f73)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 1. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2%20and%203-3.Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980/Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980.062303023.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 2](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1070)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 2. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2.Cray_Channels_Vol-3_No-2.Checkmate.Cray_Blitz.Hyatt.1981/Cray_Channels_Vol-3_No-2.Checkmate.Cray_Blitz.Hyatt.1981.062303019.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1983**). [Cray Blitz](Cray_Blitz "Cray Blitz") - *A Computer Chess Playing Program*. Master's Thesis, [University of Southern Mississippi](University_of_Southern_Mississippi "University of Southern Mississippi")
- [Joanne L. Martin](https://dblp.org/pers/hd/m/Martin:Joanne_L=), [Tony Warnock](Tony_Warnock "Tony Warnock") (**1983**). *[CRAY-1 Instruction Analysis: A Comparison of Two Methods](https://www.osti.gov/biblio/5633829)*. [Ninth International Computer Measurement Group Conference](https://dblp.org/db/conf/cmg/cmg1983.html)
- [Harry Nelson](Harry_Nelson "Harry Nelson") (**1984**). *How We Won The Computer Chess World's Championship*. Excerpt from a talk given at he DAS Computer Science Colloquium, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2.Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984/Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984.062303020.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") » [WCCC 1983](WCCC_1983 "WCCC 1983")

## Forum Posts

- [hardware of Cray Blitz](https://www.stmintz.com/ccc/index.php?id=55521) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 13, 1999 » [WCCC 1983](WCCC_1983 "WCCC 1983")
- [Cray Blity 1981?](https://www.stmintz.com/ccc/index.php?id=113318) by Joshua Lee, [CCC](CCC "CCC"), June 02, 2000 » [ACM 1981](ACM_1981 "ACM 1981")
- [Cray and supercomputers (kinda long)](https://www.stmintz.com/ccc/index.php?id=449945) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), September 16, 2005
- [Homebrew Cray-1A](http://www.talkchess.com/forum/viewtopic.php?t=35947) by Max May, [CCC](CCC "CCC"), September 01, 2010
- [FPGA Cray-1](http://www.talkchess.com/forum/viewtopic.php?t=36228) by [Dan Andersson](index.php?title=Dan_Andersson&action=edit&redlink=1 "Dan Andersson (page does not exist)"), [CCC](CCC "CCC"), September 30, 2010
- [You'll need one of these to resurrect Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=43524) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 01, 2012
- [Cray Blitz source (Carey)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=216685&t=23616) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 10, 2008
- [How fast was the Cray?](http://www.talkchess.com/forum/viewtopic.php?t=61504) by Sean Evans, [CCC](CCC "CCC"), September 23, 2016

## External Links

- [Cray-1 from Wikipedia](https://en.wikipedia.org/wiki/Cray-1)
- [Category: Cray-1 - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Cray-1)
- [Cray (brand) from Wikipedia](https://en.wikipedia.org/wiki/Cray)
- [Cray, the Supercomputer Company | Cray"](http://www.cray.com/)

[Company History | Cray](http://www.cray.com/company/history)

- [Cray Super Computers - Cray-1](http://www.craysupercomputers.com/cray1.htm)
- [The Cray-1 Supercomputer - CHM Revolution](http://www.computerhistory.org/revolution/supercomputers/10/7) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [CRAY 1-A](https://www.cisl.ucar.edu/computers/gallery/cray/cray1.jsp) from [SCD Supercomputer Gallery](https://www.cisl.ucar.edu/computers/gallery/index.jsp)
- [Homebrew Cray-1A](http://www.chrisfenton.com/homebrew-cray-1a/) by [Chris Fenton](http://www.chrisfenton.com/) <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Cray Operating System from Wikipedia](https://en.wikipedia.org/wiki/Cray_Operating_System)
- [Cray Time Sharing System from Wikipedia](https://en.wikipedia.org/wiki/Cray_Time_Sharing_System)
- [High Performance Computer Architectures: A Historical Perspective - The CRAY-1](http://homepages.inf.ed.ac.uk/cgi/rni/comp-arch.pl?Vect/cray1.html,Vect/cray1-cpu.gif,Vect/menu-cr1.html)
- [Die Cray 1 - Architektur eines Supercomputers](http://www.bernd-leitenberger.de/cray-1.shtml) by [Bernd Leitenberger](http://www.bernd-leitenberger.de/) (German)
- [Cray-1 – the eight million dollar super-computer](https://en.chessbase.com/post/how-fast-was-the-cray) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), September 23, 2016 » [Cray Blitz](Cray_Blitz "Cray Blitz") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Supercomputer designer Seymour Cray in front of his Cray-1 computer - CHM Revolution](http://www.computerhistory.org/revolution/supercomputers/10/7/3) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), 1976 ca., Courtesy of [Cray Research, Inc.](http://www.cray.com/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [The Cray-1 Supercomputer - CHM Revolution](http://www.computerhistory.org/revolution/supercomputers/10/7) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Cray-1 from Wikipedia](https://en.wikipedia.org/wiki/Cray-1)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Homebrew Cray-1A](http://www.chrisfenton.com/homebrew-cray-1a/) by [Chris Fenton](http://www.chrisfenton.com/)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Vector processor from Wikipedia](https://en.wikipedia.org/wiki/Vector_processor)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Homebrew Cray-1A](http://www.talkchess.com/forum/viewtopic.php?t=35947) by Max May, [CCC](CCC "CCC"), September 01, 2010
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [How fast was the Cray?](http://www.talkchess.com/forum/viewtopic.php?t=61504) by Sean Evans, [CCC](CCC "CCC"), September 23, 2016

**[Up one Level](Hardware "Hardware")**

