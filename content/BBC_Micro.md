---
title: BBC Micro
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * BBC Micro**

\[ BBC Micro <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BBC Micro**, (BBC Microcomputer System)

a series of 8-bit [6502](6502 "6502") based [home computers](https://en.wikipedia.org/wiki/Home_computer) by [Acorn Computers Ltd](index.php?title=Acorn_Computers_Ltd&action=edit&redlink=1 "Acorn Computers Ltd (page does not exist)"), initially designed by a team including [Steve Furber](https://en.wikipedia.org/wiki/Steve_Furber) and [Sophie Wilson](https://en.wikipedia.org/wiki/Sophie_Wilson), first released in December 1981. The Micro was contracted by the [British Broadcasting Corporation (BBC)](https://en.wikipedia.org/wiki/BBC) after a [call for bids](https://en.wikipedia.org/wiki/Call_for_bids) for a computer to accompany the [TV series](https://en.wikipedia.org/wiki/The_Computer_Programme) and literature for their *Computer Literacy Project* <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>, which was won by Acorn with the Proton, a successor of the [Acorn Atom](Acorn_Atom "Acorn Atom") - renamed the BBC Micro. Acorn also employed the machine to simulate and develop the [ARM architecture](ARM2 "ARM2") which, many years later, has become hugely successful <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Hardware

The BBC Micro had a [6502](6502 "6502") processor running at full 2 MHz speed, accessing fast [DRAM](Memory#RAM "Memory"), alternating concurrently with the [MC6845](https://en.wikipedia.org/wiki/Motorola_6845) [video display controller](https://en.wikipedia.org/wiki/Video_display_controller), featuring eight display modes for text and graphics varied between 20 and 40-column text suitable for a [TV](https://en.wikipedia.org/wiki/Television#Electronic), to 80-column text requiring an [RGB-connected](https://en.wikipedia.org/wiki/Component_video#RGB_analog_component_video) [video monitor](https://en.wikipedia.org/wiki/Computer_monitor). As noted by [Steve Furber](https://en.wikipedia.org/wiki/Steve_Furber) in a recent interview <a id="cite-note-6" href="#cite-ref-6">[6]</a>, the alternating fast 4 MHz RAM access required some address [multiplexing](https://en.wikipedia.org/wiki/Multiplexing) using exactly the 81LS95 [tri-state](https://en.wikipedia.org/wiki/Three-state_logic) octal buffer <a id="cite-note-7" href="#cite-ref-7">[7]</a> from [National Semiconductor](https://en.wikipedia.org/wiki/National_Semiconductor) - for unknown reasons, 81LS95 from other vendors were not working.
Multiple [input/output](https://en.wikipedia.org/wiki/Input/output) ports were available to connect with [peripherals](https://en.wikipedia.org/wiki/Peripheral) or other machines, such as [serial](https://en.wikipedia.org/wiki/Serial_port) [PS-423](https://en.wikipedia.org/wiki/RS-423) ports, [parallel ports](https://en.wikipedia.org/wiki/Parallel_port), [analogue](https://en.wikipedia.org/wiki/Analog_signal) input ports with [ADC](https://en.wikipedia.org/wiki/Analog-to-digital_converter) for instance used by a [joystick](https://en.wikipedia.org/wiki/Joystick), [light pen](https://en.wikipedia.org/wiki/Light_pen) input, an expansion connector (the "1 MHz bus") to expand the system with additional hardware such as the [BBC Micro expansion](https://en.wikipedia.org/wiki/BBC_Micro_expansion_unit), and the [Tube interface](<https://en.wikipedia.org/wiki/Tube_(BBC_Micro)>) to connect a secondary processor. The BBC Micro had an integrated [keyboard](https://en.wikipedia.org/wiki/Computer_keyboard) and a [cassette interface](https://en.wikipedia.org/wiki/Compact_Cassette#Data_recording). [Floppy disks](https://en.wikipedia.org/wiki/Floppy_disk) were optional through the [Intel](Intel "Intel") [8271](https://en.wikipedia.org/wiki/Intel_8085#MCS-85_family) programmable [floppy disk controller](https://en.wikipedia.org/wiki/Floppy-disk_controller), in later models replaced by [Western Digital's](https://en.wikipedia.org/wiki/Western_Digital) [FD1771](https://en.wikipedia.org/wiki/Western_Digital_FD1771). The [Texas Instruments](https://en.wikipedia.org/wiki/Texas_Instruments) [SN76489](https://en.wikipedia.org/wiki/Texas_Instruments_SN76489) was responsible for [sound](https://en.wikipedia.org/wiki/Sound). [Phoneme](https://en.wikipedia.org/wiki/Phoneme) based [speech synthesis](https://en.wikipedia.org/wiki/Speech_synthesis) using TI's [TMS5220](https://en.wikipedia.org/wiki/Texas_Instruments_LPC_Speech_Chips) speech chip with a custom Acorn ROM of [Kenneth Kendall's](https://en.wikipedia.org/wiki/Kenneth_Kendall) voice was optional <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Models

The initial BBC Micro was shipped as Model **A** with 16 KiB of user RAM, and Model **B** with 32 KiB. The [Acorn Electron](https://en.wikipedia.org/wiki/Acorn_Electron) was a budget version of the B-Model released by Acorn in 1983. Two export models were developed for the US <a id="cite-note-9" href="#cite-ref-9">[9]</a> and [West Germany](https://en.wikipedia.org/wiki/West_Germany) in 1983 <a id="cite-note-10" href="#cite-ref-10">[10]</a>. As a sideline, the [Acorn Business Computer (ABC)](https://en.wikipedia.org/wiki/Acorn_Business_Computer) range of machines was announced in October 1984 <a id="cite-note-11" href="#cite-ref-11">[11]</a>.
The Model **B+** in mid 1985, increased the total RAM to 64 KiB, the **B+128** came with an additional 64 KiB (4 × 16 KBi "Sideways" RAM banks) to give a total RAM of 128 KiB <a id="cite-note-12" href="#cite-ref-12">[12]</a>. The [BBC Master](https://en.wikipedia.org/wiki/BBC_Master) with integrated [floppies](https://en.wikipedia.org/wiki/Floppy_disk) followed in 1986 with an enhanced [65SC12](https://en.wikipedia.org/wiki/WDC_65C02) CPU, and expandable 128 KiB RAM as default, and remained in production until 1993 <a id="cite-note-13" href="#cite-ref-13">[13]</a>.

## Software

The [Acorn Machine Operating System](https://en.wikipedia.org/wiki/Acorn_MOS) (MOS) was held in 16 KiB of [ROM](Memory#ROM "Memory") on the [motherboard](https://en.wikipedia.org/wiki/Motherboard). A further 16 KiB ROM contained the [BBC BASIC](Basic#BBC "Basic") interpreter. [Acornsoft](https://en.wikipedia.org/wiki/Acornsoft) was the major publisher of software for the BBC Micro and Acorn Electron, who released [Acornsoft Chess](Acornsoft_Chess "Acornsoft Chess") written by [Arthur Norman](Arthur_Norman "Arthur Norman") and [Nick Pelling](Nick_Pelling "Nick Pelling"). Other British companies in the fast growing software market were [Micro Power](https://en.wikipedia.org/wiki/Micro_Power) , [Computer Concepts, Ltd.](https://en.wikipedia.org/wiki/Xara) and [Bug-Byte](https://en.wikipedia.org/wiki/Bug-Byte).

## Chess Programs

- [Category:BBC Micro](Category:BBC_Micro "Category:BBC Micro")

## First Computer Go Tournament

The BBC Micro [Go](Go "Go") Tournament was held in [London](https://en.wikipedia.org/wiki/London), on January 7 and 8, 1984, sponsored by [Acornsoft](https://en.wikipedia.org/wiki/Acornsoft). All eight programs ran on BBC Micro. The Go playing program by [Bronyslaw Przybla](index.php?title=Bronyslaw_Przybla&action=edit&redlink=1 "Bronyslaw Przybla (page does not exist)") won the event <a id="cite-note-14" href="#cite-ref-14">[14]</a>.

## See also

- [Acorn Atom](Acorn_Atom "Acorn Atom")
- [Acorn Archimedes](Acorn_Archimedes "Acorn Archimedes")
- [BBC Micro Bit](index.php?title=BBC_Micro_Bit&action=edit&redlink=1 "BBC Micro Bit (page does not exist)") <a id="cite-note-15" href="#cite-ref-15">[15]</a>

## Publications

- John Vaux (**1983**). *Micro takes on Chess Machine*. [Acorn User](https://en.wikipedia.org/wiki/Acorn_User), No. 8, [pdf](http://acorn.huininga.nl/pub/magazines/Acorn%20User/Acorn_User_Number_008_1983-03_Addison-Wesley_GB.pdf)
- [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *University Challenge - Martin Bryant and White Knight*. [Personal Computer World](https://en.wikipedia.org/wiki/Personal_Computer_World), [August 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/PCW_August_1983.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
- [Alex Bell](Alex_Bell "Alex Bell") (**1983**). *[Chess for three gives the White Knight a winning gambit](http://myweb.tiscali.co.uk/themicrouser/issues/01-10/chess.htm)*. [The Micro User Magazine](https://en.wikipedia.org/wiki/The_Micro_User), December 1983
- [Arthur Norman](Arthur_Norman "Arthur Norman"), [Gillian Cattell](http://www.goodreads.com/author/show/2774369.Gillian_Cattell) (**1983**). *[LISP on the BBC Microcomputer](http://www.acornelectron.co.uk/info_books/electron/acornsoft_adder/Lisp.html)*. [Acornsoft](https://en.wikipedia.org/wiki/Acornsoft) » [LISP](index.php?title=LISP&action=edit&redlink=1 "LISP (page does not exist)") <a id="cite-note-16" href="#cite-ref-16">[16]</a>

## Manuals

<a id="cite-note-17" href="#cite-ref-17">[17]</a>

- [John Coll](https://en.wikipedia.org/wiki/John_Coll), [David Allen](http://www.computinghistory.org.uk/det/41935/David-Allen-and-Steve-Lowry-The-BBC-Micro-and-Computer-Literacy-Project/) (ed.) (**1984**). *BBC Microcomputer System User Guide*. [pdf](http://bbc.nvg.org/doc/BBCUserGuide-1.00.pdf)
- [Acorn Computer](https://en.wikipedia.org/wiki/Acorn_Computers) (**1985**). *BBC Microcomputer Service Manual*. Section 1, Models A + B, [pdf](http://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Acorn_BBCSMOct85_Sec1.pdf)

## [Circuit Diagram](http://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Acorn_BBCCctDiagram.pdf) (pdf) Forum Posts

- [Okay, i know now: Colossus and BBC ACORN A: White Knight](https://www.stmintz.com/ccc/index.php?id=228177) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), May 06, 2002

## [those good old times... in the 70-80ties](https://www.stmintz.com/ccc/index.php?id=228190) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), May 06, 2002 External Links

## BBC Micro

- [BBC Micro from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro)
- [BBC Micro expansion unit from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro_expansion_unit)
- [Tube (BBC Micro) from Wikipedia](<https://en.wikipedia.org/wiki/Tube_(BBC_Micro)>)
- [BBC Microcomputer Model B](https://www.classic-computers.org.nz/collection/bbc-b.htm) by [Terry Stewart](http://www.classic-computers.org.nz/collection/index.htm) (Tezza)
- [Acorn BBC Micro Model B - Computing History](http://www.computinghistory.org.uk/det/182/acorn-bbc-micro-model-b/)
- [DigiBarn Systems: BBC Microcomputer by Acorn](http://www.digibarn.com/collections/systems/bbc-micro/index.html)
- [Chris Turner - Acorn and the BBC Micro - Computing History](http://www.computinghistory.org.uk/det/40132/Chris-Turner-Acorn-and-the-BBC-Micro/)
- [Wouter's BBC micro software, scans, pictures, etc.](http://wouter.bbcmicro.net/index.html)
- [Acorn Electron from Wikipedia](https://en.wikipedia.org/wiki/Acorn_Electron)
- [BBC Master from Wikipedia](https://en.wikipedia.org/wiki/BBC_Master)
- [ARX, Arthur and RISC OS](http://rougol.jellybaby.net/meetings/2012/PaulFellows/index.html) by [Paul Fellows](http://rougol.jellybaby.net/meetings/2012/oct.html), [RISC OS User Group Of London](http://www.rougol.jellybaby.net/), October 15, 2012 » [Acorn Archimedes](Acorn_Archimedes "Acorn Archimedes")

## Software

- [Acorn MOS from Wikipedia](https://en.wikipedia.org/wiki/Acorn_MOS)
- [BBC BASIC from Wikipedia](https://en.wikipedia.org/wiki/BBC_BASIC) » [BBC BASIC](Basic#BBC "Basic")
- [BBC Micro Software at the Centre for Computing History](http://www.computinghistory.org.uk/cgi/archive.pl?type=Software&platform=BBC%20Micro)
- [Complete BBC Games Archive](http://bbcmicro.co.uk/index.php)
- [BBC Games Archive - The Stairway To Hell](https://www.stairwaytohell.com/bbc/sthcollection.html)
- [Acornsoft - BBC Micro/Acorn Electron Professional Games - Acorn Electron World](http://www.acornelectron.co.uk/profs/electron/cats/acornsoft.html)
- [BBC Games from the past - MicroPower Games](http://www.bbcmicrogames.com/micropower.html)
- [BBC Computer Related Manuals: Games](http://www.8bs.com/othrdnld/manuals/games.shtml)

## Chess Programs

- [Beeb Chess - Complete BBC Games Archive](http://bbcmicro.co.uk/game.php?id=1065) » [Beeb Chess](index.php?title=Beeb_Chess&action=edit&redlink=1 "Beeb Chess (page does not exist)")
- [Chess - Complete BBC Games Archive](http://bbcmicro.co.uk/game.php?id=955) » [Chess (David Thompson)](</Chess_(David_Thompson)> "Chess (David Thompson)")
- [Chess (Micro Power) - Complete BBC Games Archive](http://bbcmicro.co.uk/game.php?id=796) » [Micro Power Chess](index.php?title=Micro_Power_Chess&action=edit&redlink=1 "Micro Power Chess (page does not exist)")
- [Chess (V2.1) - Complete BBC Games Archive](http://bbcmicro.co.uk/game.php?id=924) » [Acornsoft Chess](Acornsoft_Chess "Acornsoft Chess")
- [Colossus Chess 4 for BBC Micro (1986) Ad Blurbs](http://www.mobygames.com/game/bbc-micro_/colossus-chess-4/adblurbs) - [MobyGames](https://en.wikipedia.org/wiki/MobyGames) » [Colossus Chess](Colossus_Chess "Colossus Chess")

## Computer Literacy Project

- [The Computer Programme from Wikipedia](https://en.wikipedia.org/wiki/The_Computer_Programme)
- [BBC - Computer Literacy Project - Computing History](http://www.computinghistory.org.uk/det/7182/BBC-Computer-Literacy-Project/)
- [Making the Most of the Micro from Wikipedia](https://en.wikipedia.org/wiki/Making_the_Most_of_the_Micro)
- [Micro Live from Wikipedia](https://en.wikipedia.org/wiki/Micro_Live)
- [David Allen and Steve Lowry - The BBC Micro and Computer Literacy Project - Computing History](http://www.computinghistory.org.uk/det/41935/David-Allen-and-Steve-Lowry-The-BBC-Micro-and-Computer-Literacy-Project/)

## Misc

- [Computer Go - Past Events - Acorn 1984](http://www.computer-go.info/events/acorn/1984/index.html) » [Go](Go "Go")

- Building the BBC Micro (The Beeb) with [Steve Furber](https://en.wikipedia.org/wiki/Steve_Furber) - Computerphile, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [The BBC Model B Microcomputer System](http://www.classic-computers.org.nz/collection/bbc-b.htm): As seen in [Tezza's classic computer collection](http://www.classic-computers.org.nz/collection/index.htm), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Image](https://commons.wikimedia.org/wiki/File:BBC_Micro.jpeg) assumed by [Stuart Brady](https://commons.wikimedia.org/wiki/User:StuartBrady), December 26, 2005, The expansion socket to the left of the keyboard is not a standard fitting and has been added afterwards, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [BBC - Computer Literacy Project - Computing History](http://www.computinghistory.org.uk/det/7182/BBC-Computer-Literacy-Project/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [BBC Continuing Education Television - Computer Literacy Project](http://www.computinghistory.org.uk/pdf/acorn/BBC-Computer-Literacy-Project.pdf) (pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The Computer Programme (BBC2, 1982)](https://www.youtube.com/watch?v=5dIcOXx3Exc&list=PLOtimvwAoYtnCtLiLspq_Gnng1XusYwPU), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [BBC Micro from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Steve Furber's Video Interview](BBC_Micro#Video "BBC Micro") at 8:50
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [DM81LS95A Datasheet](http://www.alldatasheet.com/datasheet-pdf/pdf/114739/NSC/DM81LS95A.html) - [National Semiconductor](https://en.wikipedia.org/wiki/National_Semiconductor)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [BBC Micro from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [USA model BBC micro](http://wouter.bbcmicro.net/pictures/computer/usa_bbc/index.html)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Chris's Acorns: German BBC Microcomputer Model B](https://web.archive.org/web/20100221035416/http://acorn.chriswhy.co.uk:80/Computers/BBCBDE.html), hosted by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [BBC Micro from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [BBC Micro from Wikipedia](https://en.wikipedia.org/wiki/BBC_Micro)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Acorn Sales News Issue 72](http://chrisacorns.computinghistory.org.uk/docs/Acorn/SN/Acorn_SalesNews72.pdf) (pdf) April 19, 1993
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Computer Go - Past Events - Acorn 1984](http://www.computer-go.info/events/acorn/1984/index.html)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Micro Bit from Wikipedia](https://en.wikipedia.org/wiki/Micro_Bit)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Acornsoft LISP from Wikipedia](https://en.wikipedia.org/wiki/Acornsoft_LISP)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Chris's Acorns: Acorn Manuals](http://chrisacorns.computinghistory.org.uk/docs/Acorn/Manuals/Manuals.html)

**[Up one Level](Hardware "Hardware")**

