---
title: Novag Micro Chess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Novag Micro Chess**



 [](http://www.flickr.com/photos/10261668@N05/858170843/in/set-72157600922171918) Novag Micro Chess <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Novag Micro Chess**,  

one of [Novag's](Novag "Novag") first [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers") with a program by [David Kittinger](David_Kittinger "David Kittinger"), first released in 1981. The computer has a [Mostek](https://en.wikipedia.org/wiki/Mostek) MK3875/42 [microcontroller](https://en.wikipedia.org/wiki/Microcontroller) <a id="cite-note-2" href="#cite-ref-2">[2]</a> , a second sourced single chip implementation of the [Fairchild F8](Fairchild_F8 "Fairchild F8") multi-chip processor, the 3850 [ALU](Combinatorial_Logic#ALU "Combinatorial Logic") with 64 [byte](Byte "Byte") [scratchpad RAM](Memory#Latches "Memory"), which are 64 general purpose 8-bit registers <a id="cite-note-3" href="#cite-ref-3">[3]</a> , and the 3851 program storage unit, [instruction decoder](https://en.wikipedia.org/wiki/Decoder) and 4 [Kibibyte](https://en.wikipedia.org/wiki/Kibibyte) mask-programmable [ROM](Memory#ROM "Memory"), and 64 byte executable RAM <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> .The novelty of Novag Micro Chess was a sensor pegboard with [membrane switches](https://en.wikipedia.org/wiki/Membrane_switch), which allows [entering moves](Entering_Moves "Entering Moves") directly by pulling and sticking pieces on the board. Eight [rank](Ranks "Ranks") and [file](Files "Files") [LEDs](https://en.wikipedia.org/wiki/Light-emitting_diode) indicate [origin-](Origin_Square "Origin Square") and [target square](Target_Square "Target Square") of the move made internally by the computer. 



## Invalid Castling


A Micro Chess prototype had a [move generation](Move_Generation "Move Generation") [bug](Engine_Testing#bugs "Engine Testing") due to [castling](Castling "Castling") over an attacked square, which of course occurred in its first tournament game at the [CPWTIPC 1981](CPWTIPC_1981 "CPWTIPC 1981"), where Micro Chess lost a game from [Chess Champion Mark IV](Chess_Champion_Mark_IV "Chess Champion Mark IV") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```
[Event "CPWTIPC 1981"]
[Site "Paris, France"]
[Date "1981.05.28"]
[Round "1"]
[White "Chess Champion Mark IV"]
[Black "Novag Micro Chess"]
[Result "1-0"]

1.e4 e5 2.f4 exf4 3.Bc4 d6 4.Nf3 Ne7 5.O-O Nbc6 6.Nc3 Be6 7.Bxe6 fxe6 8.Qe2 e5
9.Qc4 Ng6 10.a4 Be7 11.d4 Nxd4 12.Nxd4 exd4 13.Qxd4 Bf6 14.Qd5 Bxc3 15.bxc3 c6
16.Qe6+ Qe7 17.Qxe7+ Nxe7 18.Bxf4 d5 19.Be5 {0-0 invalid castling} 1-0

```


<img src="https://lichess1.org/export/fen.gif?fen=r3k2r/pp2n1pp/2p5/3pB3/P3P3/2P5/2P3PP/R4RK1 b kq - 1 19" style="
    width: 300px;
">

```
r3k2r/pp2n1pp/2p5/3pB3/P3P3/2P5/2P3PP/R4RK1 b kq - 1 19 
```



## See also


* [Chess Champion Pocket Chess](Chess_Champion_Pocket_Chess "Chess Champion Pocket Chess")
* [MicroChess](MicroChess "MicroChess")
* [Mini Chess](Mini_Chess "Mini Chess")
* [Move Generation with 256 bytes RAM or less?](Sensor_Chess#MoveGeneration "Sensor Chess")
* [MyChess](MyChess "MyChess")
* [Novag](Novag "Novag")


## Publications


* [Novag Micro Chess](http://www.schaakcomputers.nl/hein_veldhuis/database/files/08-1981%20%5BM-0101%5D%20Novag%20-%20Micro%20Chess.pdf) (pdf) by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")


## External Links


* [ionel.cordesses - NOVAG MICRO CHESS](http://lionel.cordesses.free.fr/gpages/novagmicrochess.html)
* [Novag Micro Chess Electronic Chess Computer](http://www.spacious-mind.com/html/micro_chess.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [Novag Micro Chess](http://www.schach-computer.info/wiki/index.php/Novag_Micro_Chess) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Novag Micro Chess](http://www.flickr.com/photos/10261668@N05/858170843/in/set-72157600922171918) from [Novag | Photo collection](http://www.flickr.com/photos/10261668@N05/sets/72157600922171918/) by [Chewbanta](Steve_Blincoe "Steve Blincoe")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Mostek 3870 (MK3870) microcontroller family from CPU world](http://www.cpu-world.com/CPUs/3870/index.html)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Fairchild F8 (3850) microcontroller family from CPU world](http://www.cpu-world.com/CPUs/3850/index.html)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Fairchild F8 datasheet and application note, data sheet, circuit, pdf, cross reference | Datasheet Archive](http://www.datasheetarchive.com/Fairchild%20F8-datasheet.html)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> David Edwards (**1976**). *The Mostek F8*. [Electronics Australia](https://en.wikipedia.org/wiki/Electronics_Australia), December, 1976, [pdf](http://messui.the-chronicles.org/comp/fairchild.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Novag Micro Chess](http://www.schaakcomputers.nl/hein_veldhuis/database/files/08-1981%20%5BM-0101%5D%20Novag%20-%20Micro%20Chess.pdf) (pdf) by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell") (**1981**). *MicroChess - Paris Tournament*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), August 1981
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Publication Archive](http://www.chesscomputeruk.com/html/publication_archive.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Novag Micro Chess](http://www.schaakcomputers.nl/hein_veldhuis/database/files/08-1981%20%5BM-0101%5D%20Novag%20-%20Micro%20Chess.pdf) (pdf) by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis")

**[Up one Level](Engines "Engines")**







 
