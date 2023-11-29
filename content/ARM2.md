---
title: ARM2
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * ARM2**

**ARM2**, (ARM3)

the [Acorn](index.php?title=Acorn_Computers_Ltd&action=edit&redlink=1 "Acorn Computers Ltd (page does not exist)") RISC Machine [ARMv2 architecture](https://en.wikipedia.org/wiki/List_of_ARM_microarchitectures) is a 32-bit [CMOS](https://en.wikipedia.org/wiki/CMOS) [reduced instruction set computer](https://en.wikipedia.org/wiki/Reduced_instruction_set_computer), first released in 1987 <a id="cite-note-1" href="#cite-ref-1">[1]</a> as successor of the initial ARM (1985), designed by [Sophie Wilson](https://en.wikipedia.org/wiki/Sophie_Wilson) and [Steve Furber](https://en.wikipedia.org/wiki/Steve_Furber) in 1984. It features a 32-bit data bus, a [26-bit](https://en.wikipedia.org/wiki/26-bit) address space and sixteen 32-bit [registers](https://en.wikipedia.org/wiki/Processor_register) (r0 - r15, including [PC](https://en.wikipedia.org/wiki/Program_counter) and [SP](https://en.wikipedia.org/wiki/Call_stack#Structure)) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and a 3-stage [pipelined](https://en.wikipedia.org/wiki/Instruction_pipeline) (Fetch, Decode, Execute) [Von Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture).
The ARM is a [bi endian](Endianness "Endianness") machine, per default [little-endian](Little-endian "Little-endian").

## Features

The ARM [instruction set](https://en.wikipedia.org/wiki/Instruction_set) features three operand instructions, and [conditional execution](https://en.wikipedia.org/wiki/ARM_architecture#Conditional_execution) to [avoid conditional branches](Avoiding_Branches "Avoiding Branches"). Some sample ARM [assembly](Assembly "Assembly") <a id="cite-note-3" href="#cite-ref-3">[3]</a> :

```C++

  CMP    r0, r1           ; set flags
  ADDGE  r2, r2, r3       ; if (r0 >= r1) then r2 := r2 + r3;
  ADDLT  r2, r2, r4       ; else r2 := r2 + r4;

```

A 32-bit [barrel shifter](https://en.wikipedia.org/wiki/Barrel_shifter) can be used without performance penalty with most arithmetic instructions and address calculations:

```C++

  ADD  r2, r3, r3, lsl #2 ; r2 := r3 + (r3 << 2)
                          ; → r2 := r3 + r3 * 4
                          ; → r2 := r3 * 5 

```

## Computer Chess

The ARM2 processor was embedded inside the [TASC](TASC "TASC") [ChessMachine](ChessMachine "ChessMachine") plugged in as [ISA card](https://en.wikipedia.org/wiki/ISA_bus) inside an [IBM PC](IBM_PC "IBM PC"), running [Gideon](Gideon "Gideon") and [The King](The_King "The King") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, and was further used in various [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") by [Hegener & Glaser](Hegener_%26_Glaser "Hegener & Glaser") such as the [Mephisto RISC](Mephisto_RISC "Mephisto RISC").

- [Category:ARM2](Category:ARM2 "Category:ARM2")

## See also

- [Acorn Archimedes](Acorn_Archimedes "Acorn Archimedes")
- [ARM6](ARM6 "ARM6")

## Manuals

- [ARM® and Thumb®-2 Instruction Set Quick Reference Card](http://infocenter.arm.com/help/topic/com.arm.doc.qrc0001m/QRC0001_UAL.pdf) (pdf)
- [ARM Assembly Language Programming](http://www.peter-cockerell.net/aalp/html/frames.html) by [Pete Cockerell](http://www.peter-cockerell.net/)

## Postings

- [Some facts about the Acorn RISC Machine](https://groups.google.com/d/msg/comp.arch/hPsDLEPf2eo/nvJR_d7nnyYJ) by [Roger Wilson](https://en.wikipedia.org/wiki/Sophie_Wilson), [comp.arch](https://groups.google.com/forum/#!forum/comp.arch), November 02, 1988
- [StrongARM speed of Streater program (was Re: M-Chess Pro 6.0 program description)](https://groups.google.com/forum/#!msg/rec.games.chess.computer/LN4AMZzpvJE/7_s4MVp7C2UJ) by [Stephen B. Streater](Stephen_B._Streater "Stephen B. Streater"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 21, 1996 » reply to [Ed Schröder](Ed_Schroder "Ed Schroder") on ARM2 vs. [StrongARM](index.php?title=StrongARM&action=edit&redlink=1 "StrongARM (page does not exist)")

## External Links

- [Acorn RISC Machine: ARM2 from Wikipedia](https://en.wikipedia.org/wiki/ARM_architecture#Acorn_RISC_Machine:_ARM2)
- [Amber (processor core) from Wikipedia](https://en.wikipedia.org/wiki/Amber_%28processor_core%29)
- [ARM2 - Microarchitectures - Acorn - WikiChip](https://en.wikichip.org/wiki/acorn/microarchitectures/arm2)
- [ARM3 - Microarchitectures - Acorn - WikiChip](https://en.wikichip.org/wiki/acorn/microarchitectures/arm3)
- [ARMwiki](http://www.heyrick.co.uk/armwiki/Home)
- [ARM Assembler](http://www.heyrick.co.uk/assembler/)
- [Instruction set quick finder](http://www.heyrick.co.uk/assembler/qfinder.html)
- [ARM](https://www.schach-computer.info/wiki/index.php/ARM) from [Schachcomputer.info Wiki](https://www.schach-computer.info/wiki/index.php/Hauptseite_En)
- [RISC OS from Wikipedia](https://en.wikipedia.org/wiki/RISC_OS)
- [ARM Hardware Overview](https://www.riscosopen.org/wiki/documentation/show/ARM%20Hardware%20Overview)
- [ARM Information Center](http://infocenter.arm.com/help/index.jsp)
- [Race to Embedded World Domination](https://www.realworldtech.com/arms-race/ARM%E2%80%99s) by [Paul DeMone](https://www.realworldtech.com/author/pdemone/), [Real World Tech](https://www.realworldtech.com/), November 9, 2000

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Some facts about the Acorn RISC Machine](https://groups.google.com/forum/#!msg/comp.arch/hPsDLEPf2eo/nvJR_d7nnyYJ) by [Roger Wilson](https://en.wikipedia.org/wiki/Sophie_Wilson), comp.arch, November 02, 1988
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [ARM Assembly Language Programming - Chapter 2 - Inside the ARM](http://www.peter-cockerell.net/aalp/html/ch-2.html)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> Samples from [ARM-Architektur - Besonderheiten des Befehlssatzes | Wikipedia.de](https://de.wikipedia.org/wiki/ARM-Architektur#Besonderheiten_des_Befehlssatzes) (German)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [TASC ChessMachine](https://www.schach-computer.info/wiki/index.php/TASC_ChessMachine) from [Schachcomputer.info Wiki](https://www.schach-computer.info/wiki/index.php/Hauptseite_En)

**[Up one Level](Hardware "Hardware")**

