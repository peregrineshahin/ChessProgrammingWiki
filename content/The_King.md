---
title: The King
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* The King**



[ A resin replica of The King <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**The King**,  

a chess program by [Johan de Koning](Johan_de_Koning "Johan de Koning") written in [C](C "C"), which had its debut at the [7th Dutch Computer Chess Championship 1987](DOCCC_1987 "DOCCC 1987") and was further developed, participating at computer chess [tournaments](Tournaments_and_Matches "Tournaments and Matches") until the present, in total winning four [Dutch Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and one [International CSVN Tournament](International_CSVN_Tournament "International CSVN Tournament"), the [DOCCC 1991](DOCCC_1991 "DOCCC 1991"), [DOCCC 1993](DOCCC_1993 "DOCCC 1993"), [DOCCC 1995](DOCCC_1995 "DOCCC 1995"), [DOCCC 1998](DOCCC_1998 "DOCCC 1998"), and the [ICT 2003](ICT_2003 "ICT 2003").


The King, famous for "his" interesting and entertaining playing style, was commercially market by [TASC](TASC "TASC") as [ChessMachine](ChessMachine "ChessMachine"), in bundle with [Gideon](Gideon "Gideon"), running on an [ARM2](ARM2 "ARM2") RISC CPU. ChessMachine The King was shared winner of the [4th Computer Olympiad 1992](4th_Computer_Olympiad "4th Computer Olympiad") and had good results at the [WMCCC 1990](WMCCC_1990 "WMCCC 1990") and [WMCCC 1991](WMCCC_1991 "WMCCC 1991"), further ported for various [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers"), most notably [TASC R30](TASC_R30 "TASC R30"), [TASC R40](TASC_R40 "TASC R40"), [Saitek](Saitek "Saitek") [RISC 2500](RISC_2500 "RISC 2500") and [Mephisto Montreux](Mephisto_Montreux "Mephisto Montreux"), and was also incorporated as analysis engine of [TascBase](TascBase "TascBase"). However, Johan de Koning's greatest commercial success was entering the [PC](IBM_PC "IBM PC") and [Windows](Windows "Windows") mass market, when in 1994 The King became the chess engine of [Chessmaster 4000](Chessmaster "Chessmaster") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , which remains the best-selling chess franchise in history <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> . 


  




### Contents


* [1 Description](#description)
* [2 Games & Photos](#games-.26-photos)
	+ [2.1 DOCCC 1991](#doccc-1991)
	+ [2.2 ICT 2013](#ict-2013)
		- [2.2.1 Tao](#tao)
		- [2.2.2 Fritz](#fritz)
* [3 Commercial Spin-offs](#commercial-spin-offs)
* [4 SSDF Ratings](#ssdf-ratings)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc)
* [7 References](#references)






from [Don Beal's](Don_Beal "Don Beal") [WMCCC 1991](WMCCC_1991 "WMCCC 1991") report <a id="cite-note-5" href="#cite-ref-5">[5]</a> :




```C++
Written by Johan de Koning, already known for his program which has competed for several years in [Dutch tournaments](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"). This latest version runs on the [ARM2](ARM2 "ARM2") RISC CPU and represents 2.5 man-years of development. The [evaluation function](Evaluation_Function "Evaluation Function") is complex and hence a little slow. Positional [scores](Score "Score") can "easily exceed several Pawns". Separate evaluation terms are used for [opening](Opening "Opening")/[middle](Middlegame "Middlegame")/[endgame](Endgame "Endgame") with [smooth transitions](Tapered_Eval "Tapered Eval") between them by using 3 weights which sum to 100%, giving a fuzzy definition of the [phases](Game_Phases "Game Phases"). The [search](Search "Search") techniques include [check extensions](Check_Extensions "Check Extensions") and chess-specific static rules for additional [extensions](Extensions "Extensions"). [Singular extensions](Singular_Extensions "Singular Extensions") are not used, but [lower bounds](Lower_Bound "Lower Bound") are computed to limit the search in the [selective](Selectivity "Selectivity") phase. [Best moves](Best_Move "Best Move") from earlier [iterations](Iterative_Deepening "Iterative Deepening"), [history heuristic](History_Heuristic "History Heuristic"), [killer heuristic](Killer_Heuristic "Killer Heuristic"), priority to [captures](Captures "Captures"), and a [refutation table](Refutation_Table "Refutation Table") are all used to [order moves](Move_Ordering "Move Ordering"), which are [generated](Move_Generation "Move Generation") in the all-and-sort fashion. Specialized endgame knowledge is included and this is actively being expanded. 

```

## Games & Photos


### DOCCC 1991


[DOCCC 1991](DOCCC_1991 "DOCCC 1991"), round 4, The King - [Quest](Quest "Quest")




```

[Event "DOCCC 1991"]
[Site "Utrecht NED"]
[Date "1991.10.??"]
[Round "04"]
[White "The King"]
[Black "Quest"]
[Result "1-0"]

1.Nf3 d5 2.d4 e6 3.c4 Nf6 4.Bg5 Be7 5.Nc3 O-O 6.e3 Nbd7 7.Bd3 c5 8.O-O dxc4
9.Bxc4 cxd4 10.exd4 Nb6 11.Bb3 Nfd5 12.Bxe7 Qxe7 13.Nxd5 exd5 14.Qd3 Qe4
15.Qxe4 dxe4 16.Ne5 Bf5 17.Rac1 Rad8 18.Rc7 Nd7 19.Nxf7 Rxf7 20.Rxb7 a6 21.Rc1
Kf8 22.Bxf7 Kxf7 23.Rcc7 Ke6 24.Ra7 Kd5 25.Rxa6 Kxd4 26.h3 Kd5 27.b4 g6 28.a4
h6 29.a5 Ne5 30.Rb6 Nc4 31.Rb5+ Kd4 32.a6 e3 33.fxe3+ Nxe3 34.a7 Ra8 35.Rb8
Be4 36.b5 Nc4 37.Re7 Bd5 38.Rd7 1-0

```

[View this game on Lichess.org](https://lichess.org/TARFZnaj)



### ICT 2013


### Tao


[ICT 2013](ICT_2013 "ICT 2013"), round 7, The King - [Tao](Tao "Tao")




```

[Event "ICT 2003"]
[Site "Leiden NED"]
[Date "2003.05.18"]
[Round "07"]
[White "The King"]
[Black "Tao 5.5"]
[Result "1-0"]

1.b3 e5 2.Bb2 Nc6 3.c4 d6 4.g3 Nf6 5.Bg2 g6 6.Nf3 Bg7 7.O-O O-O 8.d4 Nh5
9.d5 Ne7 10.e4 Bd7 11.c5 f5 12.Nc3 dxc5 13.Re1 Kh8 14.Rc1 Bh6 15.Nxe5
Bxc1 16.Qxc1 Ng7 17.exf5 gxf5 18.Ne2 Ng8 19.Nf4 Rf6 20.Nh5 Be8 21.Nxf6
Nxf6 22.Qxc5 Kg8 23.Rc1 b6 24.Qxc7 Qxc7 25.Rxc7 a5 26.d6 Rd8 27.Ng4 fxg4
28.Bxf6 Rxd6 1-0

```

### Fritz


 [](http://old.csvn.nl/mei2003toernooi.html) 
[ICT 2003](ICT_2003 "ICT 2003"), later winner [Johan de Koning](Johan_de_Koning "Johan de Koning") and The King facing [Fritz](Fritz "Fritz") in round 8 <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```

[Event "ICT 2003"]
[Site "Leiden NED"]
[Date "2003.05.18"]
[Round "08"]
[White "Fritz"]
[Black "The King"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nf6 3.e5 Nd5 4.c3 e6 5.d4 cxd4 6.cxd4 d6 7.Bc4 Nb6 8.Bd3 Nc6
9.O-O Nb4 10.Bb5+ Bd7 11.Bg5 Be7 12.Bxe7 Qxe7 13.Nc3 O-O 14.Bxd7 Qxd7 15.a3
N4d5 16.Ne4 dxe5 17.dxe5 Rac8 18.Re1 Rfd8 19.Qb1 Nf4 20.Nd6 Rc6 21.Qe4 Nbd5
22.Rad1 f5 23.Qb1 Rc5 24.Qa2 a5 25.g3 Ng6 26.b4 Rc3 27.Rxd5 Rxf3 28.Rdd1
Nf8 29.Nxb7 Qxd1 30.Rxd1 Rxd1+ 31.Kg2 Rdd3 32.Qc4 Rc3 33.Qb5 f4 34.bxa5 fxg3
35.hxg3 Rf7 36.a6 Rxa3 37.Qb6 Ra2 38.a7 1-0

```

[View this game on Lichess.org](https://lichess.org/R4wjptik)



## Commercial Spin-offs


* [ChessMachine - The King](ChessMachine "ChessMachine")
* [Chessmaster](Chessmaster "Chessmaster")
* [Mephisto Montreux](Mephisto_Montreux "Mephisto Montreux")
* [Millennium The King](Millennium_The_King "Millennium The King")
* [RISC 2500](RISC_2500 "RISC 2500")
* [TASC R30](TASC_R30 "TASC R30")
* [TASC R40](TASC_R40 "TASC R40")


## SSDF Ratings


The [SSDF](SSDF "SSDF") tested numerous versions of The King on the hardware of the period  :





|  #
 |  Version
 |  Hardware
 |  Rating
 |
| --- | --- | --- | --- |
|  35
 |  CM King 3.5
 |  2GB [x64](X86-64 "X86-64") MP Q6600 2,4 GHz
 | <a id="cite-note-7" href="#cite-ref-7">[7]</a> 2858
 |
|  73
 |  Chessmaster 9000
 |  256MB Athlon 1200 MHz
 |  2706
 |
|  122
 |  Chessmaster 8000
 |  128MB K6-2 450 MHz
 |  2519
 |
|  133
 |  Chessmaster 6000
 |  64MB P200 MMX
 |  2477
 |
|  172
 |  Chessmaster 5000
 |  Pentium 90 MHz
 |  2287
 |
|  194
 |  Ch.Machine The King 2.0 aggr./R30 off
 | [ARM6](ARM6 "ARM6") 30 MHz
 | <a id="cite-note-8" href="#cite-ref-8">[8]</a> 2196
 |
|  199
 |  Chessmaster 4000
 | [486](X86 "X86")/50-66 MHz
 |  2179
 |
|  221
 |  ChessMachine The King
 |  512K [ARM2](ARM2 "ARM2") 16MHz
 |  2066
 |


## Forum Posts


* [The King and Wb2Uci](https://www.stmintz.com/ccc/index.php?id=218644) by Ralph Patriquin, [CCC](CCC "CCC"), March 19, 2002 » [Wb2UCI](Wb2UCI "Wb2UCI")
* [The King "Leiden" - Chesstiger 15 "normal" Now 6,5 -8,5 90 min blitz](https://www.stmintz.com/ccc/index.php?id=297976) by Andre van Ark, May 25, 2003
* [update your The King knowledge](https://www.stmintz.com/ccc/index.php?id=323037) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), October 22, 2003
* [The King's Wb2UCI file](https://www.stmintz.com/ccc/index.php?id=341498) by Darren Rushton, [CCC](CCC "CCC"), January 10, 2004 » [Wb2UCI](Wb2UCI "Wb2UCI")
* [Re: Depth vs playing strength](http://www.talkchess.com/forum/viewtopic.php?t=41902&start=5) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), January 10, 2012 » [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")


## External Links


### Chess Engine


* [The King's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=60)
* [The King](http://www.schach-computer.info/wiki/index.php/The_King) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
* [3rd International CSVN Tournament Leiden, Netherlands, May 16-18, 2003](http://old.csvn.nl/mei2003toernooi.html)


### Misc


* [The Coming of the King from Wikipedia](https://en.wikipedia.org/wiki/The_Coming_of_the_King)
* [The King (2005 film) from Wikipedia](https://en.wikipedia.org/wiki/The_King_%282005_film%29)
* [The King (2007 film) from Wikipedia](https://en.wikipedia.org/wiki/The_King_%282007_film%29)
* [Focus](Category:Focus "Category:Focus") - [House of the King](https://en.wikipedia.org/wiki/Focus_Plays_Focus) ([Akkerman](https://en.wikipedia.org/wiki/Jan_Akkerman) 1970), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Lewis chessmen from Wikipedia](https://en.wikipedia.org/wiki/Lewis_chessmen)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Mads Brevik](index.php?title=Mads_Brevik&action=edit&redlink=1 "Mads Brevik (page does not exist)") (**1994**). *[Chessmaster 4000 Turbo for Windows from Mindscape](http://www.ibiblio.org/GameBytes/issue18/greviews/chess/chess.html)*. [Game Bytes Magazine](http://www.ibiblio.org/GameBytes/issue18/editor/pub.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chessmaster from Wikipedia](https://en.wikipedia.org/wiki/Chessmaster)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Why is Chessmaster so popular in CCC?](https://www.stmintz.com/ccc/index.php?id=117882) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), July 05, 2000
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Don Beal](Don_Beal "Don Beal") (**1991**). *Report on the [11th World Microcomputer Chess Championship](WMCCC_1991 "WMCCC 1991")*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 14, No. 2
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Photos](http://old.csvn.nl/mei2003toernooi.html) from the old [CSVN](CSVN "CSVN") site
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [The SSDF Rating List](http://ssdf.bosjo.net/list.htm)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: A theory of ratings drift for the SSDF](https://www.stmintz.com/ccc/index.php?id=222392) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 09, 2002

**[Up one Level](Engines "Engines")**







 
