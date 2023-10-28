---
title: SAM
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* SAM**



 [](File:SAM47Die.jpg) Samsung S3P7588 4bit SAM47 core MCU [die](https://en.wikipedia.org/wiki/Die_%28integrated_circuit%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**SAM**, (SAM47, Samsung Arrangeable Microcontrollers)  

a family of [Samsung](https://en.wikipedia.org/wiki/Samsung_Electronics) [4-bit](https://en.wikipedia.org/wiki/4-bit_computing) [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) (MCU) with the eponymous CPU core. The single-chip controller of the S3C7xxx, KS56C2x and KS57C2x series provide various amounts of [ROM](Memory#ROM "Memory") and [nibble](Nibble "Nibble") or [byte](Byte "Byte") addressable [RAM](Memory#RAM "Memory"), [parallel](https://en.wikipedia.org/wiki/Parallel_I/O) and [serial](https://en.wikipedia.org/wiki/Serial_communication) [I/O](https://en.wikipedia.org/wiki/Input/output), 8-bit timer/counter, [interrupt controller](https://en.wikipedia.org/wiki/Programmable_interrupt_controller), and [LCD](https://en.wikipedia.org/wiki/Liquid-crystal_display) direct drive capability.
Samsung provides development tools, such as the Samsung Arrangeable Microcontroller (SAM) Assembler <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Architecture](#architecture)
* [2 Chess Programs](#chess-programs)
* [3 Manuals](#manuals)
* [4 External Links](#external-links)
* [5 References](#references)






RAM is organized in three banks, 0, 1 and 15 of 256 nibbles each. The lowest 32 nibbles of bank 0 (000H–01FH) are used as working [registers](https://en.wikipedia.org/wiki/Processor_register), 
the remaining 224 nibbles can be used both as [stack area](https://en.wikipedia.org/wiki/Call_stack) and as general-purpose data memory, bank 1 for general-purpose use and bank 15 for [memory-mapped I/O](https://en.wikipedia.org/wiki/Memory-mapped_I/O).
There are multiple [addressing modes](https://en.wikipedia.org/wiki/Addressing_mode), a 8-bit mode requires an even nibble address inside a pair of 4-bit registers.
The register area is divided into four register banks 0 to 3 selected by the register bank selection instruction (SRB n), bank 0 for the main program, 1-3 for interrupt routines.
Each of the register banks is subdivided into eight 4-bit registers A (lsn), E, L, H, X, W, Z, Y (msn) with EA, HL, WX, YZ as possible register pairs, as well as the cross mapped WL.
With appropriate instructions, registers can be manipulated as 1-bit units, 4-bit units or, using paired registers, as 8-bit units, the latter also used as pointer for indirect addressing.
Further the CPU has the obligatory 13- or 14-bit [program counter](https://en.wikipedia.org/wiki/Program_counter) and 8-bit [stack pointer](https://en.wikipedia.org/wiki/Call_stack#STACK-POINTER), a 16-bit sequential carrier (BSC) register, and status word.



## Chess Programs


* [Category:SAM](Category:SAM "Category:SAM")


## Manuals


* [Samsung KS57C2308 Manuals | ManualsLib](https://www.manualslib.com/products/Samsung-Ks57c2308-337897.html)
* [Samsung S3C9228/P9228 User Manual | Manualsbrain.com](https://manualsbrain.com/en/manuals/1196631/)
* [KS57C2316Q-XX Datasheet PDF Viewer](https://www.datasheet.directory/index.php?title=Special:PdfViewer&url=https%3A%2F%2Fdatasheet.iiic.cc%2Fdatasheets-1%2Fsamsung_semiconductor_division%2FKS57C2316Q-XX.pdf)


## External Links


* [KS56C220](https://www.schach-computer.info/wiki/index.php/KS56C220) - [Schachcomputer.info Wiki](https://www.schach-computer.info/wiki/index.php?title=Hauptseite_En)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [100pcs Samsung S3P7588 4bit SAM47 core MCU silicon dies](https://www.ebay.com/itm/112321771858), [EBay](https://en.wikipedia.org/wiki/EBay)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [19-Development Tools - Samsung S3C9228/P9228 User Manual - Page 455 of 462 | Manualsbrain.com](https://manualsbrain.com/en/manuals/1196631/?page=455)

**[Up one Level](Hardware "Hardware")**







 
