---
title: MBChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MBChess**


**MBChess**,  

a chess program by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), written in [C](C "C"). It was primarily used as test-bed for hardware based [FPGA](FPGA "FPGA") [move generation](Move_Generation "Move Generation"), which was subject of Boulé's Masters thesis in 2002 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The FPGA approach performs a [Belle](Belle#Hardware "Belle") like move generation method with find **victim** and find **aggressor** cycles in [MVV-LVA](MVV-LVA "MVV-LVA") manner. The move generator includes a [PCI](https://en.wikipedia.org/wiki/Conventional_PCI) interface to connect it to the PC running MBChess. Communication is done via different commands, such as to instruct the move generator to [undo](Unmake_Move "Unmake Move") the currently stored move, generate and return the next move and [execute](Make_Move "Make Move") that move on its internal FPGA [board representation](Board_Representation "Board Representation"). In total, 10,804 out of 18,816 [logic cells](FPGA#LC "FPGA") of a [Xilinx](https://en.wikipedia.org/wiki/Xilinx) XCV800 <a id="cite-note-2" href="#cite-ref-2">[2]</a> were used, 10,104 as [LUT](https://en.wikipedia.org/wiki/Lookup_table#Hardware_LUTs), 700 as RAM <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Hardware vs. Software


MBChess is a very basic chess program, without [opening book](Opening_Book "Opening Book"), only rudimentary [evaluation](Evaluation "Evaluation"), i.e. almost no [king safety](King_Safety "King Safety"), and without [null move pruning](Null_Move_Pruning "Null Move Pruning"). The reported ratings obtained on [FICS](index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") are 1844 and 1692 for MBChess+FPGA and MBChess respectively <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Marc Boulé further concluded a bit disappointing results <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Even though the pure move generation speed is almost 5 times faster, when using full heuristics, this drops to about 2 times faster. He found that his FPGA move generator, can at best, make/unmake 10M moves a second, which due to PCI bus saturation, will not even transfer from FPGA to PC. [Crafty](Crafty "Crafty") could already make/unmake 30M moves a second on that machine, which implies the only way to speedup Crafty would be to make an FPGA with search and evaluation.



## Publications


* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn"))
* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [McGill University](McGill_University "McGill University")
* [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](ICGA_Journal#25_2 "ICGA Journal")


## Forum Posts


* [A Response From Marc Boule](https://www.stmintz.com/ccc/index.php?id=221124) by [Slater Wold](index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](CCC "CCC"), April 02, 2002
* [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=250746) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), September 07, 2002
* [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), September 08, 2002


## External Links


* [FICS Games Database - Statistics for mbchess](http://www.ficsgames.org/cgi-bin/search.cgi?player=mbchess;statsyear=9999)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Attention - Slater Wold](https://www.stmintz.com/ccc/index.php?id=292813) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), April 10, 2003
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Thesis by Marc Boule](https://www.stmintz.com/ccc/index.php?id=251005) by [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [CCC](CCC "CCC"), September 08, 2002
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn"))
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2002**). *An FPGA Move Generator for the Game of Chess*. [ICGA Journal, Vol. 25, No. 2](ICGA_Journal#25_2 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [A Response From Marc Boule](https://www.stmintz.com/ccc/index.php?id=221124) by [Slater Wold](index.php?title=Slater_Wold&action=edit&redlink=1 "Slater Wold (page does not exist)"), [CCC](CCC "CCC"), April 02, 2002

**[Up one Level](Engines "Engines")**







 
