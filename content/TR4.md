---
title: TR4
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* TR-4**



 [](http://www.qslnet.de/member/dj4kw/tr4_1.jpg) TR-4 CPU Rack with [Teletype](https://en.wikipedia.org/wiki/Teleprinter) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**TR-4** (TR4, Telefunken-Rechner 4),  

was a West-German digital general purpose [mainframe computer](https://en.wikipedia.org/wiki/Mainframe_computer) developed since 1956 and manufactured and shipped since 1962 by [Telefunken](https://en.wikipedia.org/wiki/Telefunken) in [Backnang](https://en.wikipedia.org/wiki/Backnang) and later in [Konstanz](https://en.wikipedia.org/wiki/Konstanz). Developers include [Gudrun Beyer](Mathematician#GBeyer "Mathematician"), [Wolfgang Händler](Mathematician#WHaendler "Mathematician") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Hans-Otto Leilich](http://genealogy.math.ndsu.nodak.edu/id.php?id=98112), Kuno Radius, Egbert Ulbrich, [Eike Jessen](Mathematician#EJessen "Mathematician") and Heinz Voigt <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 36 TR-4 computers were manufactured and delivered mostly to West-German universities and public authorities and their associated data centers. 



### Contents


* [1 Architecture](#architecture)
* [2 Successor](#successor)
* [3 Chess Programs](#chess-programs)
* [4 External Links](#external-links)
* [5 References](#references)






The computer had a word size of 52 bits, consisting of 48 data bits, 2 type bits (00 - [floating point](Float "Float"), 38 bit normalized mantissa, 01 - integer/fixed point, 10 - opcode 2x24 bit, 11 - 8 six bit text characters) and 2 bit checksum (Dreierprobe), checksum errors causing interrupts. [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") and registers were build in discrete transistor technique running at 2 MHz, [main memory](Memory "Memory") consists of up to 28,672 words of [core memory](https://en.wikipedia.org/wiki/Magnetic-core_memory) and 4096 words of semiconductor memory. Auxiliary storage were [magnetic tapes](https://en.wikipedia.org/wiki/Magnetic_tape_data_storage), [punched tapes](https://en.wikipedia.org/wiki/Punched_tape) and [cards](https://en.wikipedia.org/wiki/Punched_card), and [disk drives](https://en.wikipedia.org/wiki/Hard_disk_drive). The hard-wired [micro-programmable](https://en.wikipedia.org/wiki/Microcode) computer took 9 and 40 cycles for fixed and floating point addition respectively, and about 60 cycles (30µs) for a multiplication. ALU, instruction-, memory- and I/O units were able to work in parallel, controlled by a [time-sharing](https://en.wikipedia.org/wiki/Time-sharing) [operating system](https://en.wikipedia.org/wiki/Operating_system), which also incorporates the machine instruction translators SUSA (TR4-Assembler) and TEXAS (Telefunken Externcode Assembler). [Algol](Algol "Algol"), [Fortran](Fortran "Fortran") and [COBOL](https://en.wikipedia.org/wiki/COBOL) compiler were available.





|  |
| --- |
| [TR4Registers.png](File:TR4Registers.png) |
|  Four Register Units <a id="cite-note-4" href="#cite-ref-4">[4]</a> - VR (Verteiler register) distribution register
 |
| * ALU (Rechenwerk)

 HR Help-Register
 MD multiplicand register
 AC Accumulator
 ÜB Carry register
 MQ Multiplier register  | * Memory Unit (Speicher)

 Sp1 Memory 1
 Sp2 Memory 2
 FSp Fixed Memory  
 X Index Memory 
 (256 registers in core) |
| * I/O-Unit (E/A-Werk)

 I/O registers | * Instruction Unit (Befehlswerk)

 BA Address
 BR Instruction register
 BZ Instruction counter
 MS Microprogram Control Unit  |






## Successor


In 1968, the TR4 was superseded by the ten times faster [TR 440](TR_440 "TR 440"), which already had the first [ball-based mouse](https://en.wikipedia.org/wiki/Ball_mouse#Mechanical_mice) named [Rollkugel](http://commons.wikimedia.org/wiki/File:Telefunken_Rollkugel_RKS_100-86.jpg) <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



## Chess Programs


* [Fischer-Schneider](Fischer-Schneider "Fischer-Schneider")
* [Schach MV 5,6](Schach_MV_5,6 "Schach MV 5,6")


## External Links


* [TELEFUNKEN TR4 am Leibniz-Rechenzentrum 1965](http://www.qslnet.de/member/dj4kw/tr4.htm) by [Gerd Sapper](http://www.qslnet.de/member/dj4kw/index.htm) (German, English)
* [TELEFUNKEN TR-4](http://www.vaxman.de/historic_computers/telefunken/tr4/tr4.html)
* [TR 440 from Wikipedia.de](http://de.wikipedia.org/wiki/TR_440) (German)
* [Digitalrechner-Geschichte: TR4 auf www.dj1xk.de](http://www.dj1xk.de/tr4.html) (German)
* [Historie der Digitalrechner in Deutschland TR-4](http://www.hardiweb.de/compmuseum/html_tr4/inhalt_tr4.htm)
* [Index of /pdf/aeg-telefunken/tr4](http://bitsavers.informatik.uni-stuttgart.de/pdf/aeg-telefunken/tr4/) from [bitsavers.org](http://bitsavers.informatik.uni-stuttgart.de/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [TELEFUNKEN TR4 am Leibniz-Rechenzentrum 1965](http://www.qslnet.de/member/dj4kw/tr4.htm) by [Gerd Sapper](http://www.qslnet.de/member/dj4kw/index.htm) (German, English)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Erlangen Classification System - Wikipedia.de](http://de.wikipedia.org/wiki/Erlangen_Classification_System) (German)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Eike Jessen](Mathematician#EJessen "Mathematician"), Dieter Michel, [Hans-Jürgen Siegert](http://genealogy.math.ndsu.nodak.edu/id.php?id=25498), Heinz Voigt (**2008**). *[AEG-Telefunken TR 440: Unternehmensstrategie, Markterfolg und Nachfolger](http://link.springer.com/article/10.1007%2Fs00450-008-0048-2)*. Informatik - Forschung und Entwicklung, Vol. 22, No. 4
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [TR-4\_Brochure\_Apr60.pdf](http://bitsavers.informatik.uni-stuttgart.de/pdf/aeg-telefunken/tr4/TR-4_Brochure_Apr60.pdf), pp. 2
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Telefunken Rollkugel ~ oldmouse.com](http://www.oldmouse.com/mouse/misc/telefunken.shtml)

**[Up one Level](Hardware "Hardware")**







 
