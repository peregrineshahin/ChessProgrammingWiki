---
title: Yace
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Yace**


**Yace**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compatible chess engine, Yet Another Chess Engine by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"). 
Yace is famous for its enormous [endgame](Endgame "Endgame") [knowledge](Knowledge "Knowledge") and ability of interactive backward analysis <a id="cite-note-1" href="#cite-ref-1">[1]</a> due to preserving important information in the [transposition table](Transposition_Table "Transposition Table") also mentioned as orthogonal [persistent hash table](Persistent_Hash_Table "Persistent Hash Table").



## Search Tuning


Users are encouraged to [tune](Automated_Tuning "Automated Tuning") the [search](Search "Search") [selectivity](Selectivity "Selectivity"), in particular [quiescence search](Quiescence_Search "Quiescence Search") and [null move pruning](Null_Move_Pruning "Null Move Pruning") by passing corresponding [attribute-value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair) inside an initialization file or engines setup.
Further, users can parameterize [fractional extensions](Extensions#FractionalExtensions "Extensions") with with floating point values, internally mapped to 1/64 [Ply](Ply "Ply") resolution for [check extensions](Check_Extensions "Check Extensions") for first and consecutive checks, [passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") when reaching the 7th rank, and [threat extensions](Mate_Threat_Extensions "Mate Threat Extensions") when [null move](Null_Move "Null Move") indicates trouble <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Tablebases


Yace supports the [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases") and further has its own 4-men WDL [bitbase format](Endgame_Bitbases "Endgame Bitbases") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, well suited to use inside the search.



## Tournament Play


During the early 2000s, Yace was a quite active tournament player, online six [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), [CCT2](CCT2 "CCT2")-[CCT7](CCT7 "CCT7"), and also over the board the Paderborn [IPCCC 2001](IPCCC_2001 "IPCCC 2001"), the [IPCCC 2003](IPCCC_2003 "IPCCC 2003"), where Yace became runner up behind [Fritz](Fritz "Fritz"), and the [IPCCC 2004](IPCCC_2004 "IPCCC 2004"), as well as the [ICT 2001](ICT_2001 "ICT 2001") in Leiden operated by [Jan Kaan](index.php?title=Jan_Kaan&action=edit&redlink=1 "Jan Kaan (page does not exist)"), and the [BELCT 2001](BELCT_2001 "BELCT 2001") in Berlin operated by [Ingo Bauer](Ingo_Bauer "Ingo Bauer").



## Photos & Games


### IPCCC 2001


[](https://web.archive.org/web/20180713110850/http://chess.fsv.de/aboutus/aboutus.htm)
[Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)") and Gunnar Schönemann <a id="cite-note-5" href="#cite-ref-5">[5]</a> observing the game Yace - [Holmes](Holmes "Holmes"),  
operated by their authors [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") (front) and [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [IPCCC 2001](IPCCC_2001 "IPCCC 2001") <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```

[Event "IPCCC 2001"]
[Site "Paderborn GER"]
[Date "2001.02.25"]
[Round "09"]
[White "Yace"]
[Black "Holmes"]
[Result "1-0"]

1.Nf3 c5 2.c4 Nf6 3.Nc3 d5 4.cxd5 Nxd5 5.d4 Nxc3 6.bxc3 g6 7.e3 Bg7 8.Bd3 O-O 
9.O-O Qc7 10.Ba3 Nd7 11.e4 e6 12.Rb1 Rd8 13.Bc1 Rb8 14.Bg5 Re8 15.Qd2 c4 
16.Be2 Ra8 17.Bh6 Bxh6 18.Qxh6 a5 19.Nd2 Nb6 20.e5 f5 21.exf6 Nd5 22.Bxc4 Nxf6 
23.Rfe1 Ng4 24.Qh4 h5 25.Bd3 Kg7 26.Nf3 Qe7 27.Rb5 e5 28.h3 Qxh4 29.Nxh4 Nxf2 
30.Kxf2 g5 31.Nf3 g4 32.hxg4 hxg4 33.Nxe5 Rh8 34.Ng6 Rf8+ 35.Nxf8 Kxf8 36.Bc4 
g3+ 37.Kxg3 Ra6 38.Rg5 Be6 39.Bxe6 Rxe6 40.Rxe6 Kf7 41.Rge5 b6 42.Kg4 Kg7 
43.Re8 a4 44.Kg5 a3 45.R5e7# 1-0

```

### IPCCC 2003


[](https://web.archive.org/web/20041103061005fw_/http://www.fsv.de/chess-server/Pics/Paderborn2003/baderborn2003a.htm)
[IPCCC 2003](IPCCC_2003 "IPCCC 2003"): [Shredder](Shredder "Shredder") - Yace, [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") and [Peter Berger](Peter_Berger "Peter Berger") <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "IPCCC 2003"]
[Site "Paderborn GER"]
[Date "2003.02.23"]
[Round "07"]
[White "Shredder"]
[Black "Yace"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bd2 Bxc3 7.bxc3 Ne4 8.Qg4 Kf8
9.Qf4 c5 10.Nf3 c4 11.Be2 Nc6 12.O-O Nxd2 13.Nxd2 Qg5 14.Qxg5 hxg5 15.f4 gxf4
16.Rxf4 Bd7 17.Raf1 Nd8 18.a3 Ke7 19.R1f3 Rc8 20.Rg4 Rh7 21.Rf1 Rc6 22.h4 Rb6 
23.Rb1 Rxb1+ 24.Nxb1 f6 25.Nd2 Nf7 26.Nf3 Ba4 27.Bd1 Be8 28.Rf4 Nh6 29.g4 f5 
30.Ng5 Rh8 31.Bf3 Nxg4 32.Bxg4 Rxh4 33.Nxe6 Rxg4+ 34.Rxg4 fxg4 35.Nf4 Bf7 
36.Kf2 g5 37.Ng2 b5 38.Ne3 Be6 39.Kg3 Ke8 40.Nxg4 Kf7 41.Nf6 Kg6 42.Ne8 Bd7 
43.Nc7 Bc6 44.Kf2 Kf7 45.Kg3 a5 46.Kh3 a4 47.Kg3 Kg7 48.Ne6+ Kh6 49.Kf3 Kg6 
50.Nc5 Kf5 51.Ke3 Kg6 52.Na6 Kg7 53.Nc5 Kf7 54.Ke2 Ke7 55.Kf2 Be8 56.Kg3 Kf7 
57.Kf3 Kg6 58.Kf2 Kf5 59.Na6 Bc6 60.Nc7 Kg6 61.Kg2 Kh6 62.Kg1 Kg6 63.Ne6 Kf5
64.Nc7 Kg6 65.Kf2 Kf7 66.Kg2 Ke7 67.Kf2 Kf7 68.Kg3 Kg7 69.Ne6+ Kg6 70.Kf3 Kf5
71.Nc5 Kg6 72.Ne6 Kh6 73.Nc5 Kg6 74.Kg4 Be8 75.Nb7 Bd7+ 76.Kg3 Bf5 77.Nd6 Bd7 
78.Kg2 Kh5 79.Kg3 Kh6 80.Nb7 Bf5 81.Nd6 Bd7 82.Nb7 Bf5 83.Kf3 Bxc2 84.Nd6 b4 
85.cxb4 c3 86.Ke3 Bg6 87.Nb5 c2 88.Kd2 g4 89.Nc3 g3 90.Ne2 g2 91.Ng1 Bd3 
92.Nh3 Kg7 93.b5 Bxb5 94.Kxc2 Be2 95.Kd2 Bg4 96.Ng1 Kg6 97.Kd3 Kg5 98.Ke3 Kf5 
99.Kf2 Ke4 100.Kxg2 Kxd4 101.Kg3 Bd7 102.Kf2 Kxe5 103.Ne2 d4 104.Ke1 Bb5 
105.Nc1 Bc4 106.Kd1 Kf4 107.Kd2 Ke4 108.Kc2 Ke3 109.Kb1 0-1

```

## Forum Posts


### 2000 ...


* [New Winboard program "Yace"](https://www.stmintz.com/ccc/index.php?id=113833) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 08, 2000
* [Problems with winboard protocol (Crafty 17.10 vs Yace)](https://www.stmintz.com/ccc/index.php?id=114010) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), June 10, 2000
* [Yace 0.22 by Dieter Buerssner is available !](https://www.stmintz.com/ccc/index.php?id=121819) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), July 26, 2000
* [Yace 0.23 by Dieter Buerssner is available !](https://www.stmintz.com/ccc/index.php?id=131391) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 04, 2000
* [Yace in Paderborn](https://www.stmintz.com/ccc/index.php?id=156036) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), February 26, 2001
* [Yace 0.99.50 available for download](https://www.stmintz.com/ccc/index.php?id=177410) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), June 28, 2001
* [YACE extensions?!?](https://www.stmintz.com/ccc/index.php?id=198559) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), November 23, 2001
* [Kramer Vs Kramer (Yace + Book against Yace + No Book = 13.5 - 6.5)](https://www.stmintz.com/ccc/index.php?id=248794) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [CCC](CCC "CCC"), August 30, 2002
* [Yace at CCT5](https://www.stmintz.com/ccc/index.php?id=278666) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), January 21, 2003 » [CCT5](CCT5 "CCT5")
* [A little correction for the Yace Information](https://www.stmintz.com/ccc/index.php?id=298082) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [CCC](CCC "CCC"), May 26, 2003
* [Problem ending for Yace](https://www.stmintz.com/ccc/index.php?id=319788) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), October 06, 2003
* [Any programs besides Yace and Patzer that can use bitbase files](https://www.stmintz.com/ccc/index.php?id=370997) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 17, 2004 » [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases"), [Patzer](Patzer "Patzer")
* [Re: full documentation of yace commands](https://www.stmintz.com/ccc/index.php?id=379228) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), July 27, 2004


### 2005 ...


* [(long) Some Statistics from Pavel's Yace Paderborn vs. Aristrach 4.5](https://www.stmintz.com/ccc/index.php?id=427356) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), May 21, 2005
* [Re: Is chess knowledge always meaningful? (An Example)](https://www.stmintz.com/ccc/index.php?id=447238) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), September 03, 2005
* [Bitbases - yace, scorpio, gambitfruit](https://www.stmintz.com/ccc/index.php?id=467250) by [Bernhard Bauer](index.php?title=Bernhard_Bauer&action=edit&redlink=1 "Bernhard Bauer (page does not exist)"), [CCC](CCC "CCC"), December 06, 2005
* [Question Concerning Yace !!](https://www.stmintz.com/ccc/index.php?id=487256) by George Speight, [CCC](CCC "CCC"), February 16, 2006
* [Do somebody have news about YACE ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=22521) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), July 23, 2008


### 2010 ...


* [YACE (author Dieter Bürßner) -older versions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=36144) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 22, 2010


## External Links


* [The Yace Website](http://web.archive.org/web/20020601214103/home1.stofanet.dk/moq/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Yace 0.99.87](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Yace%200.99.87) in [CCRL 40/15](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Lars Bremer](Lars_Bremer "Lars Bremer") (**2004**). *Das Rückwärts-Genie*. [CSS 4/04](Computerschach_und_Spiele "Computerschach und Spiele") (German), [pdf](http://www.lbremer.de/artikel/Yace.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Yace 0.99.50 available for download](https://www.stmintz.com/ccc/index.php?id=177410) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), June 28, 2001
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Yace Archive Page](https://sites.google.com/site/marochess/yace), yace\_ReadMe.pdf
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Any programs besides Yace and Patzer that can use bitbase files](https://www.stmintz.com/ccc/index.php?id=371131) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), June 18, 2004
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [FSV Netzwerk GmbH - Gesellschafter](https://web.archive.org/web/20090306190203/http://fsv.de:80/founders.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> Photo by [Roland Pfister](Roland_Pfister "Roland Pfister"), [FSV - About us](https://web.archive.org/web/20180713110850/http://chess.fsv.de/aboutus/aboutus.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [FSV personal chess service - Paderborn 2003 Pics](https://web.archive.org/web/20041103061005fw_/http://www.fsv.de/chess-server/Pics/Paderborn2003/baderborn2003a.htm) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

**[Up one Level](Engines "Engines")**







 
