---
title: Nova
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* Nova**



[ NOVA Rack <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Nova**, (Data General Nova)  

a [16-bit](https://en.wikipedia.org/wiki/16-bit) [minicomputer](https://en.wikipedia.org/wiki/Minicomputer) series built by the American company [Data General](https://en.wikipedia.org/wiki/Data_General) starting in 1968. The Nova was designed by [DEC](Digital_Equipment_Corporation "Digital Equipment Corporation") [PDP-8](PDP-8 "PDP-8") chief engineer and Data General co-founder [Edson de Castro](https://en.wikipedia.org/wiki/Edson_de_Castro). It was packaged into a single [rack mount](https://en.wikipedia.org/wiki/19-inch_rack) case. 


Unlike the [PDP-8](PDP-8 "PDP-8"), Nova was a [load/store architecture](https://en.wikipedia.org/wiki/Load/store_architecture). It had four 16-bit [accumulators](https://en.wikipedia.org/wiki/Accumulator_%28computing%29), where two could be used as [index registers](https://en.wikipedia.org/wiki/Index_register), and a 15-bit [address space](https://en.wikipedia.org/wiki/Address_space) and [PC](https://en.wikipedia.org/wiki/Program_counter). The Nova is a [big-endian](Big-endian "Big-endian") architecture. Since there is no [byte](Byte "Byte") addressing, bytes need to be parsed out of [words](Word "Word") using swaps and masks high-order byte first <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Nova consists of a [nibble](Nibble "Nibble")-serial 4-bit [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") - its [RISC-like](https://en.wikipedia.org/wiki/Reduced_instruction_set_computing) instructions perform arithmetical and logical operations with the options to rotate, test and branch on the (skip next instructon on zero, carry) the 17-bit result, and also to discard the result otherwise written into the target accu. Basic models of the Nova came without built-in hardware multiply and divide. The first models were available with 1 to 8K [words](Word "Word") of [magnetic core memory](Memory#Core "Memory"). 


[System software](https://en.wikipedia.org/wiki/System_software) provided include the [real time operating system](https://en.wikipedia.org/wiki/Real-time_operating_system) [RDOS](https://en.wikipedia.org/wiki/Data_General_RDOS), [assembler](Assembly "Assembly"), [Basic](Basic "Basic") interpreter, and [Fortran](Fortran "Fortran") and [Algol](Algol "Algol") compiler, expanded with [Forth](Forth "Forth"), [Lisp](index.php?title=Lisp&action=edit&redlink=1 "Lisp (page does not exist)"), and [C](C "C") through third party vendors <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### SuperNOVA


The SuperNOVA subsequently replaced initial [magnetic core memory](Memory#Core "Memory") with faster [ROM](Memory#ROM "Memory") for library routines, and semiconductor (SuperNOVA SC) memory. The 4-bit [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") was extended to 16-bit using four instead of one [bit slice](https://en.wikipedia.org/wiki/Bit_slicing) [74181](https://en.wikipedia.org/wiki/74181) ALU with speedup correspondingly <a id="cite-note-4" href="#cite-ref-4">[4]</a>.




### Nova 1200


[ Nova 1200 Front panel <a id="cite-note-5" href="#cite-ref-5">[5]</a>
The Nova 1200 contained the entire CPU one one board, first shipped in 1971 <a id="cite-note-6" href="#cite-ref-6">[6]</a>. It still had the [Nibble](Nibble "Nibble")-serial ALU, and up to 32K words [magnetic core memory](Memory#Core "Memory").




### Nova 8x0


The faster Nova 800 was released in 1971. The Nova 840 introduced [memory mapping](Memory#Virtual "Memory") in 1973, allowing two discrete sessions running concurrently, each with its own controlling terminal <a id="cite-note-7" href="#cite-ref-7">[7]</a>.




### Nova 2


The Nova 2 was essentially a simplified version of the earlier machines as increasing chip densities allowed the CPU to be reduced in size, with CPU and memory on a single board, introduced in 1973.




### Eclipse


[ Eclipse S/130 front panel <a id="cite-note-8" href="#cite-ref-8">[8]</a>
The Eclipse line, started in 1974, had an advanced, Nova upward-compatible instruction set, and included support for [virtual memory](Memory#Virtual "Memory") and multitasking. The line was succeeded by the [32-bit](https://en.wikipedia.org/wiki/32-bit) [Eclipse MV](https://en.wikipedia.org/wiki/Data_General_Eclipse_MV/8000) minicomputers in the early 80s, whose development was subject of [Tracy Kidder's](https://en.wikipedia.org/wiki/Tracy_Kidder) book *[The Soul of A New Machine](https://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine)*. 




### Nova 3


In 1975, the Nova 3 combined features from all previous Nova designs, and added a [hardware stack](Stack "Stack") and appropriate stack instructions <a id="cite-note-9" href="#cite-ref-9">[9]</a>. The Nova 3 was reduced to a chip set in 1976, called the microNOVA with hardware Multiply/Divide, optionally before, becoming a standard <a id="cite-note-10" href="#cite-ref-10">[10]</a>.




### Nova 4


The Nova 4 was the last of the Nova line, released in 1987, the CPU a derivation of the [Eclipse S/140](Nova#Eclipse "Nova"). The Nova 4 is implemented around four [AMD 2901](https://en.wikipedia.org/wiki/AMD_Am2900) [bit-slice](https://en.wikipedia.org/wiki/Bit_slicing) chips and, unlike all earlier Novas, is [microcoded](https://en.wikipedia.org/wiki/Microcode). 



## Chess Programs


* [Category:Nova](Category:Nova "Category:Nova")


## See also


* [PDP-8](PDP-8 "PDP-8")
* [PDP-11](PDP-11 "PDP-11")


## External Links


* [Data General Nova from Wikipedia](https://en.wikipedia.org/wiki/Data_General_Nova)
* [Data General Corporation (DG) - Nova](http://www.computerhistory.org/brochures/companies.php?alpha=d-f&company=com-42b9d5f5afbd4) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")


 [The best small computer in the world, 1968 - DGC.Nova](http://archive.computerhistory.org/resources/text/Data_General/DGC.Nova.1968.102646102.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [The BITSAVERS.ORG Documents Library: Data General](https://archive.org/details/bitsavers_dg)
* [Data General NOVA Basic Instruction Summary](http://users.rcn.com/crfriend/museum/doco/DG/Nova/) by [Carl R. Friend](http://users.rcn.com/crfriend/)
* [DG Nova Extended Instructions](http://users.rcn.com/crfriend/museum/doco/DG/Nova/extend-instr.html) by [Carl R. Friend](http://users.rcn.com/crfriend/)
* [Novas Are Forever](http://www.novasareforever.org/)
* [The Computer History Simulation Project](http://simh.trailing-edge.com/)


 [System Photographs](http://simh.trailing-edge.com/photos.html)
* [DG-NOVA](http://ed-thelen.org/comp-hist/dg-nova.html) by [Ed Thelen](http://ed-thelen.org/)


### SuperNOVA


* [Super Nova, 1970](http://archive.computerhistory.org/resources/text/Data_General/DataGeneral.NovaSuperNova.1970.102646153.pdf) (pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")


### Nova 1200


* [The Retro-Computing Society of RI, Inc.: Nova 1200](http://www.rcsri.org/collection/nova-1200/)
* [DG Nova 12x0s](http://users.rcn.com/crfriend/museum/machines/Nova12xx.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)


### Nova 8x0


* [840 The Loaded NOVA, 1973](http://archive.computerhistory.org/resources/text/Data_General/Data_General.840.1973.102646255.pdf) (pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [The Retro-Computing Society of RI, Inc.: Nova 840](http://www.rcsri.org/collection/nova-840/)
* [Nova 840](http://users.rcn.com/crfriend/museum/machines/Nova840.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)


### Nova 2


* [Data General Corp. Nova 2](http://users.rcn.com/crfriend/museum/machines/Nova2.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
* [Data General Nova 2/10](http://www.ricomputermuseum.org/Home/equipment/data-general-nova-2) from [The Rhode Island Computer Museum](http://www.ricomputermuseum.org/Home)


### Eclipse


* [Data General Eclipse from Wikipedia](https://en.wikipedia.org/wiki/Data_General_Eclipse)
* [Carl's DG Eclipse S/130](http://users.rcn.com/crfriend/museum/machines/EclipseS130.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
* [Carl's DG Eclispe S/140](http://users.rcn.com/crfriend/museum/machines/EclipseS140.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
* [Data General Eclipse S/130](http://www.ricomputermuseum.org/Home/equipment/data-general-eclipse-s-130) from [The Rhode Island Computer Museum](http://www.ricomputermuseum.org/Home)


### Nova 3


* [DG Nova 3](http://users.rcn.com/crfriend/museum/machines/Nova3.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
* [Data General Nova-3](http://www.ricomputermuseum.org/Home/equipment/data-general-nova-3) from [The Rhode Island Computer Museum](http://www.ricomputermuseum.org/Home)
* [Data General Nova-3/12](http://www.ricomputermuseum.org/Home/equipment/data-general-nova-3-2) from [The Rhode Island Computer Museum](http://www.ricomputermuseum.org/Home)


### Nova 4


* [Carl's DG Nova 4](http://users.rcn.com/crfriend/museum/machines/Nova4.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
* [Data General Nova 4/C and 4/X](http://comley.us/browse.php?&action=show&artefactID=1054)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Data General NOVA System](https://commons.wikimedia.org/wiki/File:Data_General_NOVA_System.jpg), (beige and yellow, center bottom) and a [cartridge hard disk system](https://en.wikipedia.org/wiki/Disk_pack) (opened, below Nova) in a mostly empty rack mount, [Goodwill Computer Museum](https://wsampson.wordpress.com/2012/03/15/goodbye-goodwill-computer-museum-hello-museum-of-computer-culture/), [Austin, Texas](https://en.wikipedia.org/wiki/Austin,_Texas), Image courtesy [Jeff Keyzer](https://www.flickr.com/photos/mightyohm/5334424560/), January 07, 2011
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Data General NOVA Basic Instruction Summary](http://users.rcn.com/crfriend/museum/doco/DG/Nova/) by [Carl R. Friend](http://users.rcn.com/crfriend/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Data General Nova from Wikipedia](https://en.wikipedia.org/wiki/Data_General_Nova)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Data General Nova from Wikipedia](https://en.wikipedia.org/wiki/Data_General_Nova)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> Front panel of a Data General Nova 1200 minicomputer by [Arnold Reinhold](https://commons.wikimedia.org/wiki/User:ArnoldReinhold), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Data General Nova from Wikipedia](https://en.wikipedia.org/wiki/Data_General_Nova), bit 0 for Carry, bit 1 for MSB and bit 15 for LSB!
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [The Retro-Computing Society of RI, Inc.: Nova 1200](http://www.rcsri.org/collection/nova-1200/)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Nova 840](http://users.rcn.com/crfriend/museum/machines/Nova840.html) from [Carl Friend's](http://users.rcn.com/crfriend/) [Minicomputer "Museum"](http://users.rcn.com/crfriend/museum/index.shtml)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> Data General Eclipse S/130 front panel. Computer belongs to Emil Sarlija, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Nova Stack Instructions](http://users.rcn.com/crfriend/museum/doco/DG/Nova/extend-instr.html#STACK) from [DG Nova Extended Instructions](http://users.rcn.com/crfriend/museum/doco/DG/Nova/extend-instr.html) by [Carl R. Friend](http://users.rcn.com/crfriend/)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Nova Multiply/Divide](http://users.rcn.com/crfriend/museum/doco/DG/Nova/extend-instr.html#MDV) from [DG Nova Extended Instructions](http://users.rcn.com/crfriend/museum/doco/DG/Nova/extend-instr.html) by [Carl R. Friend](http://users.rcn.com/crfriend/)

**[Up one Level](Hardware "Hardware")**







 
