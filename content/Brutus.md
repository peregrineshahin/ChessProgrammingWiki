---
title: Brutus
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Brutus**

\[ Brutus <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Brutus**,

a [FPGA](FPGA "FPGA") based chess entity developed by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), supported by [Alex Kure](Alex_Kure "Alex Kure") and [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"). Brutus consists of usual [PCs](IBM_PC "IBM PC") with [Xilinx Virtex](https://en.wikipedia.org/wiki/Virtex_%28FPGA%29#Virtex_family) [FPGA](FPGA "FPGA") boards inside, and was designed in dependence on the [Belle](Belle "Belle") and [Deep Thought](Deep_Thought "Deep Thought") chess machines. In fact, it was [Ken Thompson](Ken_Thompson "Ken Thompson") who initiated and supported the FPGA chess project. After the [WCCC 2003](WCCC_2003 "WCCC 2003"), Brutus evolved to [Hydra](Hydra "Hydra").

## How it started

In early 2000, [Ken Thompson](Ken_Thompson "Ken Thompson") told his friend [Frederic Friedel](Frederic_Friedel "Frederic Friedel") about interesting hardware developments concerning FPGAs, and asked whether he was aware of a programmer who could build such a kind of "People's [Deep Blue](Deep_Blue "Deep Blue")". [ChessBase](ChessBase "ChessBase"), surely interested in the commercial aspects of such a machine, engaged Chrilly Donninger for the development of a FPGA based chess hardware and program. The work on Brutus started in October 2000, one year later it could calculate its first position, and in January 2002, it played its first game. Soon, programmer, chess expert and [opening book author](Category:Opening_Book_Author "Category:Opening Book Author") Alex Kure, and in November 2002, Ulf Lorenz, responsible for the surrounding [distributed search](Parallel_Search "Parallel Search"), joined the Brutus team, with [ChessBase](ChessBase "ChessBase") and the [Paderborn University](Paderborn_University "Paderborn University") cooperating on the project <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Etymology

The name [Brutus](https://en.wikipedia.org/wiki/Marcus_Junius_Brutus_the_Younger) was chosen by [Matthias Wüllenweber](Matthias_W%C3%BCllenweber "Matthias Wüllenweber") due to his spot on [Ancient Rome](https://en.wikipedia.org/wiki/Ancient_Rome). The idea was a "People's Deep Blue" to dethrone "[Caesar](https://en.wikipedia.org/wiki/Julius_Caesar)" [Garry Kasparov](https://en.wikipedia.org/wiki/Garry_Kasparov) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Description

Brutus partially ran on PCs and partially on FPGA cards. Opposed to a pure [move generation](Move_Generation "Move Generation") approach, and to diminish [PCI](https://en.wikipedia.org/wiki/Conventional_PCI) communication overhead with the [PC](IBM_PC "IBM PC"), the hardware was designed also to perform a kind of [iterative search](Iterative_Search "Iterative Search"). Brutus’ FPGA definition was written in the [Verilog](https://en.wikipedia.org/wiki/Verilog) [hardware description language](https://en.wikipedia.org/wiki/Hardware_description_language), and uses 67 out of 96 BlockRAMs, 534 of 24,576 [Flip-Flops](Memory#FlipFlop "Memory"), and 18,403 of 24,576 [LUTs](https://en.wikipedia.org/wiki/Lookup_table#Hardware_LUTs) of the Virtex board <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

[](http://www.chessbase.de/nachrichten.asp?newsid=648)
Brutus on a [Xilinx Virtex](https://en.wikipedia.org/wiki/Virtex_%28FPGA%29#Virtex_family) V405E [FPGA](FPGA "FPGA") development board <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## FPGA Search

Brutus calculates the last 3 [plies](Ply "Ply") of an n-ply [search](Search "Search") on the FPGA side, inclusively [quiescence search](Quiescence_Search "Quiescence Search") and [evaluations](Evaluation "Evaluation"). It essentially contains a big piece of [combinatorial logic](Combinatorial_Logic "Combinatorial Logic"), controlled by a [finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine) (FSM) with 54 states for the search. An upper bound for the number of cycles per search node is 9. The Figure below shows a simplified version of the FSM that controls the search on the FPGA card. States must not be interpreted as time points when functions are called. E.g. the move generator and the evaluation are never called in that sense. They are running all the time <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

[](File:FPGASearch.JPG)
Search in Hardware: Simplified [state diagram](https://en.wikipedia.org/wiki/State_diagram) <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## Evaluation

The [evaluation](Evaluation "Evaluation") consists of many small features which are summed up by one large adder tree. All features are determined simultaneously.

## Move Generation

The [Belle](Belle#Hardware "Belle") like [move generator](Move_Generation "Move Generation") consists of the generate **aggressor** module and the generate **victim** module, both instantiate 64 square modules, one for each square. The squares send piece-signals if any, respectively forwarding the signals of [sliding pieces](Sliding_Pieces "Sliding Pieces"). Each square can output the signal ’victim found’ to indicate the ’victim’ is [target square](Target_Square "Target Square") of a [pseudo-legal move](Pseudo-Legal_Move "Pseudo-Legal Move"). The collection of all ’victim found’ signals is the input for a comparator tree, an arbiter, which selects the most attractive, not yet examined victim. The generate aggressor module takes the arbiter’s output as input and sends the signal of a super-piece from the target to find one or more [origin squares](Origin_Square "Origin Square"). Selection criteria are the values of attacked pieces and whether or not a move is a [killer move](Killer_Move "Killer Move").

## Distributed Search

The most sensitive and important part of Brutus [search](Search "Search") algorithm is [distributed](Parallel_Search "Parallel Search") among several standard PCs, connected via a high-speed [Myrienet](https://en.wikipedia.org/wiki/Myrinet). Based on [work stealing](https://en.wikipedia.org/wiki/Work_stealing), one processor receives the current chess position and basically begins a sequential [alpha beta search](Alpha-Beta "Alpha-Beta"), while idle processors send work requests randomly around the net. When a working processor captures such a request, it distributes part of his own (sub-) problem. Using a tricky [messaging system](https://en.wikipedia.org/wiki/Message_passing) between the processors, the work is dynamically balanced with little search overhead. After a while, all processors have something useful to do. A processor generates approximately 100,000 searches on a FPGA board per second <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Tournament Play

A Brutus prototype had its debut at the [IPCCC 2002](IPCCC_2002 "IPCCC 2002") with an expected 50% score, but Brutus quickly improved and already played a strong [WCCC 2002](WCCC_2002 "WCCC 2002") in [Maastricht](https://en.wikipedia.org/wiki/Maastricht), where it became third only loosing a spectacular game from later champion [Junior](Junior "Junior"). At the [IPCCC 2003](IPCCC_2003 "IPCCC 2003"), Brutus became third again, then, in August 2003, it won the 11th Grandmaster Tournament in [Lippstadt](https://en.wikipedia.org/wiki/Lippstadt) with 9 out of 11 <a id="cite-note-9" href="#cite-ref-9">[9]</a>, and seemed dedicated to win the upcoming [WCCC 2003](WCCC_2003 "WCCC 2003") in [Graz](https://en.wikipedia.org/wiki/Graz), but after two consecutive losses from [Shredder](Shredder "Shredder") and [Deep Junior](Junior "Junior") in round 5 and 6, Brutus finished disappointing fourth. As a consequence, ChessBase went out of the project, which then continued under the patronage of the Pal Group of Companies <a id="cite-note-10" href="#cite-ref-10">[10]</a> under its new name [Hydra](Hydra "Hydra").

## Photos & Games

## IPCCC 2002

[](http://chess.fsv.de/Pics/Paderborn2002.htm)
[IPCCC 2002](IPCCC_2002 "IPCCC 2002"): [Alex Kure](Alex_Kure "Alex Kure"), [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Mathias Feist](Mathias_Feist "Mathias Feist"), Brutus vs. [Fritz](Fritz "Fritz") 0 - 1 <a id="cite-note-11" href="#cite-ref-11">[11]</a>

```

[Event "IPCCC 2002"]
[Site "Paderborn GER"]
[Date "2002.03.03"]
[Round "07"]
[White "Brutus-XPa"]
[Black "Fritz"]
[Result "0-1"]
[ECO "E34"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 Qxd5 6.Nf3 Qf5 7.Qxf5 exf5 8.a3 Be7 9.Bf4 c6 
10.e3 Nbd7 11.Bc4 Nb6 12.Ba2 Be6 13.Be5 h6 14.Ke2 a5 15.Rhc1 a4 16.Kf1 O-O 17.Ne2 Ne4 
18.Bxe6 fxe6 19.Nf4 Kf7 20.Bxg7 Kxg7 21.Nxe6+ Kf6 22.Nxf8 Bxf8 23.Ke2 Bd6 24.g3 h5 
25.Nh4 Nd5 26.f3 Ng5 27.Kd3 Rd8 28.e4 Ne7 29.Ke3 Bc7 30.Nxf5 Nxf5+ 31.exf5 h4 32.f4 
Re8+ 33.Kd3 Nf3 34.d5 Nxh2 35.dxc6 hxg3 36.cxb7 Bxf4 37.Rc4 Kxf5 38.Rxa4 g2 39.Ra5+ Kf6 
40.Ra6+ Kf7 41.Ra4 Bb8 42.Ra5 Kf6 43.Ra6+ Kf5 44.Ra5+ Kf4 45.Ra6 Nf3 46.Rf6+ Kg3 47.Rg6+ 
Kf2 48.Rg7 g1=R 49.Raxg1 Nxg1 50.Rf7+ Nf3 51.a4 Kg3 52.Rg7+ Kf4 53.Rf7+ Kg4 54.Rh7 Ng5 
55.Rd7 Kf5 56.a5 Ke6 57.Rd4 Nf3 58.Ra4 Kd5 59.a6 Ba7 60.Kc3 Re3+ 61.Kc2 Nd4+ 62.Kd2 Nc6
63.Kc2 Kc5 64.Kd2 Kb5 65.Ra1 Re7 66.Rc1 Rd7+ 67.Ke1 Nb4 68.Ke2 Kxa6 0-1

```

## WCCC 2002

[WCCC 2002](WCCC_2002 "WCCC 2002"), round 6, Brutus - [Deep Junior](Junior "Junior") <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>:

```

[Event "WCCC 2002"]
[Site "Maastricht, The Netherlands"]
[Date "2002.07.09"]
[Round "6"]
[White "Brutus"]
[Black "Deep Junior"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2 e5 7.Nb3 Be7 8.O-O O-O 9.Kh1 Qc7 
10.f4 b5 11.fxe5 dxe5 12.Bg5 Nbd7 13.Bd3 Bb7 14.Qf3 b4 15.Ne2 a5 16.Ng3 g6 17.Rad1 a4 
18.Nd2 Ba6 19.Ne2 Rfc8 20.b3 Kg7 21.Qh3 h5 22.Qf3 Qc6 23.Bc4 Bxc4 24.Nxc4 Qe6 25.c3 
axb3 26.axb3 Rxc4 27.bxc4 b3 28.h3 b2 29.Ng3 Qxc4 30.Rb1 Rb8 31.Rfd1 Rb3 32.Rd3 Nc5 
33.Re3 Rb6 34.Re2 Na4 35.Rd2 Qa2 36.Rdd1 Rc6 37.Ne2 Qc4  38.Rf1 Rb6 39.Rbd1 Kf8 
40.Bh6+ Ke8 41.Bg7 Qxe4 42.Bxf6 Qxf3 43.gxf3 Rxf6 44.Rb1 Ba3 45.f4 exf4 46.Rf3 g5 
47.c4 Bc5 48.Rd3 g4 49.Rb3 Kd7 50.Rf1 f3 51.Ng3 Rb6 52.Rxb6 Nxb6 0-1 

```

## WCCC 2003

[](File:BrutusDiep.jpg)
[WCCC 2003](WCCC_2003#Dark "WCCC 2003"), Brutus - [Diep](Diep "Diep") <a id="cite-note-14" href="#cite-ref-14">[14]</a>, [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Eva Moser](https://en.wikipedia.org/wiki/Eva_Moser) and [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") <a id="cite-note-15" href="#cite-ref-15">[15]</a>

```

[Event "WCCC 2003"]
[Site "Graz, Austria"]
[Date "2003.11.27"]
[Round "8"]
[White "Brutus"]
[Black "Diep"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e5 7.Nb3 Be6 8.f3 Nbd7 9.Qd2 b5 
10.a4 b4 11.Nd5 Bxd5 12.exd5 Nb6 13.Bxb6 Qxb6 14.a5 Qb7 15.Bc4 Be7 16.Ra4 Rb8 17.Nc1 
O-O 18.b3 Bd8 19.Na2 Nd7 20.Kd1 Qc8 21.Nxb4 Nc5 22.Ra2 Bg5 23.Nc6 Qxc6 24.dxc6 Bxd2 
25.Kxd2 Rfc8 26.Bd5 Ne6 27.Rd1 Nd8 28.c3 Kf8 29.g4 Ke7 30.h4 Rc7 31.Ra4 f6 32.h5 Nxc6 
33.Rc4 Kd7 34.b4 h6 35.f4 exf4 36.Rxf4 Ne5 37.Re1 Rb5 38.Bb3 Rbb7 39.Re3 Rb8 40.Rd4 
Rbc8 41.Bd5 Rc4 42.Rde4 R4c7 43.Kc2 Rb8 44.Rd4 Rb5 45.Kb3 Nc6 46.Be6+ Ke7 47.Bc4+ Re5 
48.Rdd3 Ra7 49.Bd5 Nd8 50.Re4 Ne6 51.Rd2 Kd7 52.c4 Nc7 53.Red4 Nxd5 54.Rxd5 Rxd5 
55.Rxd5 Ke6 56.Kc3 Ra8 57.Kd4 g6 58.hxg6 Rg8 59.c5 dxc5+ 60.bxc5 Rxg6 61.c6 Rxg4+ 
62.Kc5 Ra4 63.Rd8 Rxa5+ 64.Kb6 Ra2 65.c7 Rc2 66.c8=Q+ Rxc8 67.Rxc8 Kf5 68.Rh8 Kg5 
69.Kxa6 h5 70.Kb5 h4 71.Kc4 Kg4 72.Kd4 Kg3 73.Ke3 Kg4 74.Rh7 h3 75.Rh6 f5 76.Rg6+ 
Kh4 77.Kf4 1-0 

```

## Namesake

- [Brutus](Brutus_NL "Brutus NL") by [Stephan Vermeire](Stephan_Vermeire "Stephan Vermeire")

## See also

- [Belle](Belle "Belle")
- [Hydra](Hydra "Hydra")

## Publications

- [Eric Hallsworth](Eric_Hallsworth "Eric Hallsworth") (**2002**). *The Brutus Project*. [Selective Search](Selective_Search "Selective Search") 101, pp. 33, [pdf](http://www.chesscomputeruk.com/SS_101A.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
- [Wenzel Mraček](http://glareanverlag.wordpress.com/tag/wenzel-mracek/) (**2003**). *Zu Besuch bei Christian „Chrilly“ Donninger*. [pdf](http://www.chess.at/spielergalerie/portraits/donninger_03/donninger_2003.pdf) (German)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *[Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program](https://ieeexplore.ieee.org/document/1302962)*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**2007**). *Flugstunden mit Ken Thompson*. [pdf](https://brigitte-godot.com/wp-content/uploads/2018/03/Flugstunden.pdf) (German)

## Forum Posts

## 2002

- [Any details about Brutus?](https://www.stmintz.com/ccc/index.php?id=215813) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), February 27, 2002
- [Junior Verses Brutus --> Rxc4 "The best PC chess move ever?"](https://www.stmintz.com/ccc/index.php?id=243526) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 31, 2002

## 2003

- [Suturb - Bob](https://www.stmintz.com/ccc/index.php?id=278894) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), January 22, 2003
- [Re: What happens to the BRUTUS Project by Dr. Donninger ?](https://www.stmintz.com/ccc/index.php?id=291339) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), April 01, 2003
- [Status of Brutus?](https://www.stmintz.com/ccc/index.php?id=308238) by O. Veli, [CCC](CCC "CCC"), July 26, 2003
- [Brutus has won the Lippstadt Tournament](https://www.stmintz.com/ccc/index.php?id=311555) by Tomas Casanovas Martinez, [CCC](CCC "CCC"), August 16, 2003
- [Go Brutus!!](https://www.stmintz.com/ccc/index.php?id=330184) by Pete Rihaczek, [CCC](CCC "CCC"), November 24, 2003

## 2004 ...

- [Was Brutus cancelled?](https://www.stmintz.com/ccc/index.php?id=342681) by Keith Evans, [CCC](CCC "CCC"), January 15, 2004
- [Hydra???](https://www.stmintz.com/ccc/index.php?id=348870) by Bob Durrett, [CCC](CCC "CCC"), February 13, 2004

## External Links

## Chess Entity

- [Brutus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=65)
- [Comp Brutus chess games - 365Chess.com](http://www.365chess.com/players/Comp_Brutus)
- [Brutus - Was ist das denn?](https://de.chessbase.com/post/brutus-was-ist-das-denn-), [ChessBase News](ChessBase "ChessBase"), March 07, 2002 (German)
- [What is Brutus?](https://en.chessbase.com/post/what-is-brutus-), [ChessBase News](ChessBase "ChessBase"), March 20, 2002
- [Parallele Schachprogrammierung](https://de.chessbase.com/post/parallele-schachprogrammierung), [ChessBase News](ChessBase "ChessBase"), September, 16, 2003 (German)
- [Schach + PC - Brutus](http://scleinzell.schachvereine.de/p_themen/brutus.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml), April 2002 (German)
- [Hydra (chess) from Wikipedia](<https://en.wikipedia.org/wiki/Hydra_(chess)>) (covers Brutus)

### Maastricht

- [Vormärz](http://old.csvn.nl/VorMaerz.html) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Old CSVN site](CSVN "CSVN") (German) <a id="cite-note-16" href="#cite-ref-16">[16]</a>

### Lippstadt

- [Brutus mit Auftaktsieg](https://de.chessbase.com/post/brutus-mit-auftaktsieg), [ChessBase News](ChessBase "ChessBase"), August 08, 2003 (German)
- [Brutus in Lippstadt mit zweitem Sieg](https://de.chessbase.com/post/brutus-in-lippstadt-mit-zweitem-sieg), [ChessBase News](ChessBase "ChessBase"), August 09, 2003 (German)
- [Grandmasters brutalised in Lippstadt](https://en.chessbase.com/post/grandmasters-brutalised-in-lippstadt), [ChessBase News](ChessBase "ChessBase"), August 10, 2003
- [Spielen wie Tal](https://de.chessbase.com/post/spielen-wie-tal-1), [ChessBase News](ChessBase "ChessBase"), August 10, 2003 (German)
- [Brutus auch nur ein Mensch](https://de.chessbase.com/post/brutus-auch-nur-ein-mensch), [ChessBase News](ChessBase "ChessBase"), August 11, 2003 (German)
- [Brutus remis](https://de.chessbase.com/post/brutus-remis), [ChessBase News](ChessBase "ChessBase"), August 12, 2003 (German)
- [Brutus reloaded](https://de.chessbase.com/post/brutus-reloaded), [ChessBase News](ChessBase "ChessBase"), August 13, 2003 (German)
- [Brutus: Held mit programmierter Götterdämmerung?](https://de.chessbase.com/post/brutus-held-mit-programmierter-gtterdmmerung-), [ChessBase News](ChessBase "ChessBase"), August 14, 2003 (German)
- [Brutus vor Maiwald und Cyborski](https://de.chessbase.com/post/brutus-vor-maiwald-und-cyborski), [ChessBase News](ChessBase "ChessBase"), August 15, 2003 (German)
- [Brutus marschiert](https://de.chessbase.com/post/brutus-marschiert), [ChessBase News](ChessBase "ChessBase"), August 16, 2003 (German)
- [Brutus mit GM-Norm](https://de.chessbase.com/post/brutus-mit-gm-norm), [ChessBase News](ChessBase "ChessBase"), August 17, 2003 (German)

### Graz

- [Brutus defeats Fritz in round four](https://en.chessbase.com/post/brutus-defeats-fritz-in-round-four), [ChessBase News](ChessBase "ChessBase"), November 24, 2003
- [Computer Championship: Shredder stops Brutus](https://en.chessbase.com/post/computer-championship-shredder-stops-brutus), [ChessBase News](ChessBase "ChessBase"), November 25, 2003

## Brutus

- [Brutus (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Brutus_%28disambiguation%29)
- [Marcus Junius Brutus the Younger from Wikipedia](https://en.wikipedia.org/wiki/Marcus_Junius_Brutus_the_Younger)

[Assassination of Julius Caesar from Wikipedia](https://en.wikipedia.org/wiki/Assassination_of_Julius_Caesar)
[Et tu, Brute? from Wikipedia](https://en.wikipedia.org/wiki/Et_tu,_Brute%3F)

- [Lucius Junius Brutus from Wikipedia](https://en.wikipedia.org/wiki/Lucius_Junius_Brutus)
- [Brutus of Troy from Wikipedia](https://en.wikipedia.org/wiki/Brutus_of_Troy)
- [List of Arthurian characters from Wikipedia](https://en.wikipedia.org/wiki/List_of_Arthurian_characters)
- [Bluto from Wikipedia](https://en.wikipedia.org/wiki/Bluto)
- [Fifty Years With Brutus! • Animated Views](http://animatedviews.com/2010/fifty-years-with-brutus/)
- [Brutus cluster from Wikipedia](https://en.wikipedia.org/wiki/Brutus_cluster) of [ETH Zurich](ETH_Zurich "ETH Zurich")
- [Brutalist architecture from Wikipedia](https://en.wikipedia.org/wiki/Brutalist_architecture)
- [Brutus](Category:Brutus "Category:Brutus") - Mystery Machine from [Behind the Mountains](https://en.wikipedia.org/wiki/Behind_the_Mountains) (2013), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Marble bust of Brutus, at the [Palazzo Massimo alle Terme](https://en.wikipedia.org/wiki/Palazzo_Massimi_alle_Terme#Palazzo_Massimo_alle_Terme) in the [National Museum of Rome](https://en.wikipedia.org/wiki/National_Museum_of_Rome), [Marcus Junius Brutus the Younger from Wikipedia](https://en.wikipedia.org/wiki/Marcus_Junius_Brutus_the_Younger)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Brutus and Hydra](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/hydra.html) by [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Paderborn University](Paderborn_University "Paderborn University") (as of October 15, 2015, dead link)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Schach + PC - Brutus](http://scleinzell.schachvereine.de/p_themen/brutus.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml), April 2002 (German)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Brutus - Was ist das denn?](http://www.chessbase.de/nachrichten.asp?newsid=648), [ChessBase News](ChessBase "ChessBase"), March 07, 2002
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Parallele Schachprogrammierung](http://www.chessbase.de/nachrichten.asp?newsid=2435), [ChessBase News](ChessBase "ChessBase"), September, 16, 2003 (German)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Performance ELO](https://www.stmintz.com/ccc/index.php?id=311579) by Lei, Shiann-Tzong, [CCC](CCC "CCC"), August 16, 2003
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Pal Group of Companies](http://www.palgroup.com/)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [FSV personal chess service - Paderborn 2002 Pics (from Sunday, 03.03.2002)](http://chess.fsv.de/Pics/Paderborn2002.htm) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)")
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Maastricht 2002 - Chess - Round 6 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=20&round=6&id=6)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Junior Verses Brutus --> Rxc4 "The best PC chess move ever?"](https://www.stmintz.com/ccc/index.php?id=243526) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 31, 2002
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Graz 2003 - Chess - Round 8 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=2&round=8&id=6)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Live from Graz – Fritz and Shredder lead](https://en.chessbase.com/post/live-from-graz-fritz-and-shredder-lead), [ChessBase News](ChessBase "ChessBase"), November, 27, 2003
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Vormärz from Wikipedia](https://en.wikipedia.org/wiki/Vorm%C3%A4rz)

**[Up one Level](Engines "Engines")**

