---
title: FPGA
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * FPGA**

\[ [Altera](https://en.wikipedia.org/wiki/Altera) FPGA <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**FPGA**, (Field-programmable gate array)

a [field-programmable](https://en.wikipedia.org/wiki/Field-programmability) [integrated circuit](https://en.wikipedia.org/wiki/Integrated_circuit) consisting of a two-dimensional [array](Array "Array") of logic blocks interconnected by a hierarchy of reconfigurable routing channels. The behavior of a FPGA is defined by a schematic design or by a [hardware description language](https://en.wikipedia.org/wiki/Hardware_description_language) (HDL), most notably [VHDL](https://en.wikipedia.org/wiki/VHDL) and [Verilog](https://en.wikipedia.org/wiki/Verilog). FPGA cards of their main suppliers [Xilinx](https://en.wikipedia.org/wiki/Xilinx) <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [Altera](https://en.wikipedia.org/wiki/Altera) <a id="cite-note-3" href="#cite-ref-3">[3]</a> can be plugged into a [PC](IBM_PC "IBM PC") with communication over the [PCI](https://en.wikipedia.org/wiki/Conventional_PCI) or [PCI Express](https://en.wikipedia.org/wiki/PCI_Express) bus. [IBM's](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") [POWER8](https://en.wikipedia.org/wiki/POWER8) processor, introduced in August 2013, features a CAPI port (Coherent Accelerator Processor Interface) is layered on top of [PCI Express 3.0](https://en.wikipedia.org/wiki/PCI_Express#PCI_Express_3.x) suited to connect custom hardware such as FPGAs <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Architecture

## Structure

|  |  |
| --- | --- |
| [Fpga structure.jpg](http://www.eecg.toronto.edu/~vaughn/challenge/fpga_arch.html) |  The structure is a two-dimensional array of logic blocks and reconfigurable routing channels, which all have the same width (number of wires). I/O pads can connect to any one of the wiring segments in the channel adjacent to it <a id="cite-note-6" href="#cite-ref-6">[6]</a>.
|
|  FPGA structure <a id="cite-note-7" href="#cite-ref-7">[7]</a> |

## Blocks and Cells

|  |  |
| --- | --- |
| [Logic block2.svg](File:Logic_block2.svg) |  Each logic block (configurable logic block CLB, or logic array block LAB) consists of one or more logical cells (LC, adaptive logic module ALM, logic element LE, Slice etc.), each with a n-input bits (4-6) to one-output bit programmable [lookup table (LUT)](https://en.wikipedia.org/wiki/Lookup_table#Hardware_LUTs) - the [combinatorial logic](Combinatorial_Logic "Combinatorial Logic"), and a [D-Flip-Flop](Memory#FlipFlop "Memory"), which synchronizes and stores the output by the edge of a clock signal to implement a [sequential logic](Sequential_Logic "Sequential Logic"). A configurable [multiplexer](https://en.wikipedia.org/wiki/Multiplexer) either switches the direct or latched LUT output outwards.
|
|  Logic cell with LUT and [D-Flip-Flop](Memory#FlipFlop "Memory") <a id="cite-note-8" href="#cite-ref-8">[8]</a> |

## Routing

|  |  |
| --- | --- |
| [Switch box.svg](File:Switch_box.svg) |  Inputs and outputs of a cell can connect to any one of the routing wires in the channel adjacent to it. Whenever a vertical and a horizontal channel intersect there is a switch box with programmable switches that allow it to connect to other wires in adjacent channel segments. [Xilinx Virtex](https://en.wikipedia.org/wiki/Virtex_%28FPGA%29#Virtex_family) devices further provide BlockRAM, a 4096-bit synchronous memory which can be configured for single or dual port usage with variable widths of 1, 2, 4, 8 or 16 bits.
|
|  Switch box topology <a id="cite-note-9" href="#cite-ref-9">[9]</a> |

## FPGA in Computer Chess

FPGAs are suited to implement a [Belle](Belle#Hardware "Belle") like [move generator](Move_Generation "Move Generation") in hardware. While [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") proposed a pure generation approach as used by his program [MBChess](MBChess "MBChess"), [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), with PCI-communication overhead in mind, went some steps further in [Brutus](Brutus "Brutus") <a id="cite-note-10" href="#cite-ref-10">[10]</a> and [Hydra](Hydra "Hydra"), using a complete 3-[ply](Ply "Ply") [iterative search](Iterative_Search "Iterative Search") including [quiescence](Quiescence_Search "Quiescence Search") and [evaluation](Evaluation "Evaluation"), controlled by a [finite state machine (FSM)](https://en.wikipedia.org/wiki/Finite-state_machine).

- [MBChess](MBChess "MBChess")
- [Brutus](Brutus "Brutus")
- [Hydra](Hydra "Hydra")

## Boulé

In his Masters thesis <a id="cite-note-11" href="#cite-ref-11">[11]</a>, [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") proposed a FPGA move generator, as used by his chess program [MBChess](MBChess "MBChess"). His approach performs a Belle like move masking method with find **victim** and find **aggressor** cycles in [MVV-LVA](MVV-LVA "MVV-LVA") manner. A 1-bit, 64-deep synchronous memory in each [square](Squares "Squares") is used to memorize masked bits. The move generator includes a PCI interface to connect it to the PC running MBChess. Communication is done via different commands, such as to instruct the move generator to [undo](Unmake_Move "Unmake Move") the currently stored move, generate and return the next move and [execute](Make_Move "Make Move") that move on its internal FPGA [board representation](Board_Representation "Board Representation"). In total, 10,804 out of 18,816 logic cells of a Xilinx XCV800 <a id="cite-note-12" href="#cite-ref-12">[12]</a> were used, 10,104 as LUT, 700 as RAM <a id="cite-note-13" href="#cite-ref-13">[13]</a>.

[](File:FPGAChessSquares.JPG)
A block diagram of a chess square with transmitter (TX) and the receiver (RX) <a id="cite-note-14" href="#cite-ref-14">[14]</a>

## Donninger

[Brutus](Brutus "Brutus") <a id="cite-note-15" href="#cite-ref-15">[15]</a> and its successor [Hydra](Hydra "Hydra") by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") et al. <a id="cite-note-16" href="#cite-ref-16">[16]</a> perform the last 3 plies of an n-ply search on the FPGA side, inclusively the quiescence search and evaluations. It uses 67 out of 96 BlockRAMs, 534 of 24,576 Flip-Flops, and 18,403 of 24,576 LUTs. An upper bound for the number of cycles per search node is 9. Hydra essentially contains a big piece of combinatorial logic, controlled by a finite state machine (FSM) with 54 states for the search. The move generator consists of the generate **aggressor** module and the generate **victim** module, both instantiate 64 square modules, one for each square.

The squares send piece-signals if any, respectively forwarding the signals of [sliding pieces](Sliding_Pieces "Sliding Pieces"). Each square can output the signal ’victim found’ to indicate the ’victim’ is [target square](Target_Square "Target Square") of a [pseudo-legal move](Pseudo-Legal_Move "Pseudo-Legal Move"). The collection of all ’victim found’ signals is the input for a comparator tree, an arbiter, which selects the most attractive, not yet examined victim. The Generate Aggressor module takes the arbiter’s output as input and sends the signal of a super-piece from the target to find one or more [origin squares](Origin_Square "Origin Square"). Selection criteria are the values of attacked pieces and whether or not a move is a [killer move](Killer_Move "Killer Move").

## Publications

## 1997 ...

- [Kurt Keutzer](index.php?title=Kurt_Keutzer&action=edit&redlink=1 "Kurt Keutzer (page does not exist)") (**1997**). *[Challenges in CAD for the One Million Gate FPGA](http://dl.acm.org/citation.cfm?id=258326)*. [FPGA 1997](http://dblp.uni-trier.de/db/conf/fpga/fpga97.html#Keutzer97), [pdf](https://www.computer.org/csdl/proceedings/fpga/1997/2600/00/26000133.pdf)
- [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**1999**). *[Fundamentals of Digital Logic with VHDL Design](http://www.mhhe.com/engcs/electrical/brownvranesic/)*. [McGraw-Hill](http://catalogs.mhhe.com/mhhe/home.do)

## 2000 ...

- [Youhei Hori](index.php?title=Youhei_Hori&action=edit&redlink=1 "Youhei Hori (page does not exist)"), [Minenobu Seki](index.php?title=Minenobu_Seki&action=edit&redlink=1 "Minenobu Seki (page does not exist)"), [Tsutomu Maruyama](index.php?title=Tsutomu_Maruyama&action=edit&redlink=1 "Tsutomu Maruyama (page does not exist)"), [Reijer Grimbergen](Reijer_Grimbergen "Reijer Grimbergen"), [Tsutomu Hoshino](index.php?title=Tsutomu_Hoshino&action=edit&redlink=1 "Tsutomu Hoshino (page does not exist)") (**2000**). *[A Shogi Processor with a Field Programmable Gate Array](http://link.springer.com/chapter/10.1007/3-540-45579-5_20)*. [CG 2000](CG_2000 "CG 2000")
- [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [Terry P. Borer](https://www.linkedin.com/in/terry-borer-501847/), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2002**). *[Automatic Partitioning for Improved Placement and Routing in Complex Programmable Logic Devices](https://www.semanticscholar.org/paper/Automatic-Partitioning-for-Improved-Placement-and-Manohararajah-Borer/d53ad046c377bedc4caa2f80dfc32339f0bc3d6d)*. [FPL 2002](https://dblp.uni-trier.de/db/conf/fpl/fpl2002.html)
- [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), co-supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")
- [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [McGill University](McGill_University "McGill University")
- [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](ICGA_Journal#25_2 "ICGA Journal")
- [Youhei Hori](index.php?title=Youhei_Hori&action=edit&redlink=1 "Youhei Hori (page does not exist)"), [Masashi Sonoyama](index.php?title=Masashi_Sonoyama&action=edit&redlink=1 "Masashi Sonoyama (page does not exist)"), [Tsutomu Maruyama](index.php?title=Tsutomu_Maruyama&action=edit&redlink=1 "Tsutomu Maruyama (page does not exist)") (**2002**). *An FPGA-Based Processor for Shogi Mating Problems*. 2002 IEEE International Conference on Field-Programmable Technology, 2002, [pdf](http://staff.aist.go.jp/hori.y/articles/hori_icfpt02.pdf)
- [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2003**). *FPGA Hardware Acceleration: From Chess Playing to Automated Theorem Proving*. poster presentation, Micronet Sept. 2003
- [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2003**). *[Fundamentals of Digital Logic with Verilog Design](http://www.mhhe.com/engcs/electrical/brownvranesic/)*. [McGraw-Hill](http://catalogs.mhhe.com/mhhe/home.do)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *[The Chess Monster Hydra](http://www.springerlink.com/content/hp9la9pwq0a1cmrp/)* in [Field Programmable Logic and Application](http://www.springerlink.com/content/8grv6pu2e8hd/?p=3037c8af6a0147319f6f5a8e133083dd&pi=0), FPL 2004

## 2005 ...

- [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2005**). *Area Optimizations in FPGA Architecture and CAD*. Ph.D. Thesis, [pdf](http://www.valavan.net/pthesis.pdf)
- [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2006**). *[Adaptive FPGAs: High-Level Architecture and a Synthesis Method](https://ieeexplore.ieee.org/document/4100986/)*. [FPL 2006](https://dblp.uni-trier.de/db/conf/fpl/fpl2006.html), [pdf](http://www.eecg.toronto.edu/~brown/papers/fpl06-manohararajah.pdf)
- [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2006**). *[Heuristics for Area Minimization in LUT-Based FPGA Technology Mapping](https://ieeexplore.ieee.org/document/1715419/).* [IEEE Transactions on CAD of Integrated Circuits and Systems](IEEE#TCICS "IEEE"), Vol. 25, No. 11
- [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2007**). *[Fundamentals of Digital Logic with Verilog Design](http://www.mhhe.com/engcs/electrical/brownvranesic/)*. [McGraw-Hill](http://catalogs.mhhe.com/mhhe/home.do), 2nd edition, [amazon](https://www.amazon.com/Fundamentals-Digital-Logic-Verilog-Design/dp/0077211642)
- [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic") (**2008**). *[Fundamentals of Digital Logic with VHDL Design](http://www.mhhe.com/engcs/electrical/brownvranesic/)*. [McGraw-Hill](http://catalogs.mhhe.com/mhhe/home.do), 3rd edition, [amazon](https://www.amazon.com/Fundamentals-Digital-Logic-Design-CD-ROM/dp/0077221435/ref=dp_ob_title_bk)
- [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2009**). *[Designing and Using FPGAs beyond Classical Binary Logic: Opportunities in Nano-Scale Integration Age](https://www.semanticscholar.org/paper/Designing-and-Using-FPGAs-beyond-Classical-Binary-Zilic/c63e05fc673821d5dc8e471e2849105bc22526f6)*. [ISMVL 2009](https://dblp.uni-trier.de/db/conf/ismvl/ismvl2009.html)

## 2010 ...

- [James Bowman](http://www.linkedin.com/pub/james-bowman/9/511/358) (**2010**). *J1: a small Forth CPU Core for FPGAs*. [EuroForth 2010](http://www.complang.tuwien.ac.at/anton/euroforth/ef10/), [pdf](http://www.excamera.com/files/j1.pdf) <a id="cite-note-17" href="#cite-ref-17">[17]</a>
- [Edin Kadric](https://dblp.uni-trier.de/pers/hd/k/Kadric:Edin), [Naraig Manjikian](http://my.ece.queensu.ca/people/N-Manjikian/index.html), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2012**). *[An FPGA implementation for a high-speed optical link with a PCIe interface](https://www.semanticscholar.org/paper/An-FPGA-implementation-for-a-high-speed-optical-a-Kadric-Manjikian/403966143ae4ded89f519214124761d667821a11)*. [SoCC 2012](https://dblp.uni-trier.de/db/conf/socc/socc2012.html)
- [Franjo Plavec](https://dblp.uni-trier.de/pers/hd/p/Plavec:Franjo), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic"), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/) (**2013**). *[Exploiting Task- and Data-Level Parallelism in Streaming Applications Implemented in FPGAs](https://dl.acm.org/citation.cfm?id=2535932)*. [TRETS](https://dblp.uni-trier.de/db/journals/trets/trets6.html), Vol. 6, No. 4

## 2015 ...

- [António Coelho](index.php?title=Ant%C3%B3nio_Coelho&action=edit&redlink=1 "António Coelho (page does not exist)") (**2016**). *FPGA Multiprocessor for Game Tree Searches*. M.Sc. thesis, [Instituto Superior Técnico](https://en.wikipedia.org/wiki/Instituto_Superior_T%C3%A9cnico), [University of Lisbon](https://en.wikipedia.org/wiki/University_of_Lisbon), [pdf](https://fenix.tecnico.ulisboa.pt/downloadFile/281870113703064/dissertacao.pdf) » [Faile](Faile "Faile")

## 2020 ...

- [Terry Loesch](index.php?title=Terry_Loesch&action=edit&redlink=1 "Terry Loesch (page does not exist)") (**2020**). *Designing an FPGA Chess Engine*. [amazon](https://www.amazon.com/gp/product/B08DM69WMH)

## Forum Posts

## 2000 ...

- [Chip design project & another request for Belle/DT/DB info](https://www.stmintz.com/ccc/index.php?id=92614) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), January 27, 2000 » [Belle](Belle "Belle"), [Deep Thought](Deep_Thought "Deep Thought"), [Deep Blue](Deep_Blue "Deep Blue")
- [FPGA move generator](https://groups.google.com/d/msg/rec.games.chess.computer/ZBvgW_JOKW0/q-pVLXe9gIoJ) by Ties Bos, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 06, 2000
- [A Response From Marc Boule](https://www.stmintz.com/ccc/index.php?id=221124) by [Slater Wold](index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](CCC "CCC"), April 02, 2002
- [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), September 08, 2002
- [Re: Attention - Slater Wold](https://www.stmintz.com/ccc/index.php?id=292813) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), April 10, 2003
- [Go Brutus!!](https://www.stmintz.com/ccc/index.php?id=330184) by Pete Rihaczek, [CCC](CCC "CCC"), November 24, 2003

## 2005 ...

- [fpga/mcu implementation](https://www.stmintz.com/ccc/index.php?id=429154) by Daniel Staf, [CCC](CCC "CCC"), May 31, 2005
- [FPGA cards and RYBKA](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=1699) by albitex, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 11, 2007

## 2010 ...

- [FPGA chess](http://www.talkchess.com/forum/viewtopic.php?t=54474) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), November 26, 2014

## External Links

- [Field-programmable gate array from Wikipedia](https://en.wikipedia.org/wiki/Field-programmable_gate_array)

[Field-programmable analog array from Wikipedia](https://en.wikipedia.org/wiki/Field-programmable_analog_array)

- [Programmable Logic/FPGAs from Wikibooks](http://en.wikibooks.org/wiki/Programmable_Logic/FPGAs)
- [Hamsterworks Wiki!](http://hamsterworks.co.nz/mediawiki/index.php/Home)
- [The FPGA Place-and-Route Challenge](http://www.eecg.toronto.edu/~vaughn/challenge/challenge.html) by [Vaughn Betz](http://www.eecg.toronto.edu/~vaughn/)

[FPGA Architecture for the Challenge](http://www.eecg.toronto.edu/~vaughn/challenge/fpga_arch.html)

- [The J1 Forth CPU — excamera](http://www.excamera.com/sphinx/fpga-j1.html) » [Forth](Forth "Forth")
- [UCLA Computer Science Department | Winter 2004 | CS 151C - Design of Digital Systems | VHDL Projects on XSV Board](http://www.cs.ucla.edu/classes/cs151C/)

[VHDL Checkers Implementation](http://www.cs.ucla.edu/classes/cs151C/#checkers)

- [FPGA Snake game uses no VHDL at all - Hack a Day](http://hackaday.com/2012/01/20/fpga-snake-game-uses-no-vhdl-at-all/)
- [The General FPGA-based board game machine, a prototype](http://ndirty.cute.fi/~karttu/FPGA/esimes/life/HARDWARE_PHOTOS/pelikone.html) by [Antti Karttunen](http://ndirty.cute.fi/~karttu/)
- [What is Brutus?](http://en.chessbase.com/post/what-is-brutus-), [ChessBase News](ChessBase "ChessBase"), March 20, 2002
- [All about the Hydra chess project](http://en.chessbase.com/post/all-about-the-hydra-che-project), [ChessBase News](ChessBase "ChessBase"), August 22, 2004

## Vendors

- [FPGA CPLD and ASIC from Altera](http://www.altera.com/)
- [All Programmable Technologies from Xilinx Inc.](http://www.xilinx.com/)
- [Alpha Data - High Performance Computing with Xilinx Virtex-7 FPGAs](http://www.alpha-data.com/)

## Misc

- [Toto Blanke](Category:Toto_Blanke "Category:Toto Blanke") - PPG, [Electric Circus](http://www.discogs.com/Toto-Blanke-Electric-Circus/release/652970) (1977) feat. [Edward Vesala](https://en.wikipedia.org/wiki/Edward_Vesala), [Jasper van 't Hof](Category:Jasper_van_%27t_Hof "Category:Jasper van 't Hof"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [FPGA from Wikipedia](https://en.wikipedia.org/wiki/Field-programmable_gate_array)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [All Programmable Technologies from Xilinx Inc.](http://www.xilinx.com/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [FPGA CPLD and ASIC from Altera](http://www.altera.com/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [IBM Power8 Processor Detailed - Features 22nm Design With 12 Cores, 96 MB eDRAM L3 Cache and 4 GHz Clock Speed](http://wccftech.com/ibm-power8-processor-architecture-detailed/)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: FPGA chess](http://www.talkchess.com/forum/viewtopic.php?t=54474&start=17) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), November 28, 2014
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [FPGA Architecture for the Challenge](http://www.eecg.toronto.edu/~vaughn/challenge/fpga_arch.html)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [FPGA Architecture for the Challenge](http://www.eecg.toronto.edu/~vaughn/challenge/fpga_arch.html)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Field Programmable Gate Array from Wikipedia.de](http://de.wikipedia.org/wiki/Field_Programmable_Gate_Array) (German)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Field-programmable gate array from Wikipedia](https://en.wikipedia.org/wiki/Field-programmable_gate_array)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [What is Brutus?](http://en.chessbase.com/post/what-is-brutus-), [ChessBase News](ChessBase "ChessBase"), March 20, 2002
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), co-supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: Attention - Slater Wold](https://www.stmintz.com/ccc/index.php?id=292813) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), April 10, 2003
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), September 08, 2002
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), co-supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox), [pdf](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/publications/ipdps04.pdf)
1. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *[The Chess Monster Hydra](http://www.springerlink.com/content/hp9la9pwq0a1cmrp/)* in [Field Programmable Logic and Application](http://www.springerlink.com/content/8grv6pu2e8hd/?p=3037c8af6a0147319f6f5a8e133083dd&pi=0), 14th International Conference, FPL 2004
1. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [The J1 Forth CPU — excamera](http://www.excamera.com/sphinx/fpga-j1.html)

**[Up one Level](Hardware "Hardware")**

