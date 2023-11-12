---
title: Zarkov
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Zarkov**



[](http://flashgordon.wikia.com/wiki/Dr._Hans_Zarkov) Dr. Zarkov <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Zarkov**,  

a commercial chess program by [John Stanback](John_Stanback "John Stanback") written in [C](C "C"). The first version in 1989 was similar to John's [GNU Chess 2.0](GNU_Chess "GNU Chess"), but used other data structures based on [0x88](0x88 "0x88") and run on [HP 9000](https://en.wikipedia.org/wiki/HP_9000) workstations or [PCs](IBM_PC "IBM PC") with its own [GUI](GUI "GUI"). In 1990, John Stanback discovered a new [pruning technique](Pruning "Pruning"), a combination of [evaluation heuristics](Evaluation "Evaluation") and [reduced depth search](Reductions "Reductions"), which was implemented in Zarkov 2.5, also market as [Grandmaster Chess](Grandmaster_Chess "Grandmaster Chess") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Zarkov stores positions in which the [score](Score "Score") changes significantly between a shallow search (about 2 plies) and a deeper search into a [persistent hash table](Persistent_Hash_Table "Persistent Hash Table"), retrieved at the start of each game to make Zarkov remember positions from previous games in its search to avoid worse positions in advance <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Windows


A [Windows](Windows "Windows") [DDE Server](https://en.wikipedia.org/wiki/Dynamic_Data_Exchange) Zarkov was used with the [Bookup](Bookup "Bookup") <a id="cite-note-5" href="#cite-ref-5">[5]</a> and [Chess Assistant](Chess_Assistant "Chess Assistant") database programs. The [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant but unreleased Zarkov 4.5X played some private engine tournaments with promising results. The so far final version Zarkov 5.0 is a [Windows](Windows "Windows") [DLL file](https://en.wikipedia.org/wiki/Dynamic-link_library) which was sold as an add-on engine for the [Millenium Genius 6](Chess_Genius "Chess Genius") aka [Millennium Chess System](Millennium_Chess_System "Millennium Chess System") interface <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



## Tournament Play


Zarkov played the [WCCC 1989](WCCC_1989 "WCCC 1989"), and the five late [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), [ACM 1989](ACM_1989 "ACM 1989"), [ACM 1990](ACM_1990 "ACM 1990"), [ACM 1991](ACM_1991 "ACM 1991"), [ACM 1993](ACM_1993 "ACM 1993"), and [ACM 1994](ACM_1994 "ACM 1994") where Zarkov became runner up behind [Deep Thought II](Deep_Thought "Deep Thought"). It did quite well in the [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments") held from 1994-1997, each time 4/6, and further played the [BELCT 2001](BELCT_2001 "BELCT 2001") and [CCT4](CCT4 "CCT4"). 



## Selected Games


### ACM 1993


[ACM 1993](ACM_1993 "ACM 1993"), round 3, [B\*Hitech](HiTech "HiTech") - Zarkov <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "ACM 1993"]
[Site "Indianapolis USA"]
[Date "1993.02.15"]
[Round "3"]
[White "B*Hitech"]
[Black "Zarkov"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Qd2 a6 8.f4 d5 9.e5 
Qh4+ 10.g3 Qh5 11.Bg2 Bh3 12.Bf3 Bg4 13.Bg2 Nxd4 14.Bxd4 Bxd4 15.cxd4 O-O 16.O-O 
c6 17.Rf2 Rfe8 18.Nc3 Nf5 19.Na4 Re6 20.Nb6 Rae8 21.Qd3 Rg6 22.Rc1 Rh6 23.Bh1 Qg6 
24.Na4 Ra8 25.Nc5 b6 26.Na4 b5 27.Nc5 a5 28.Rcf1 a4 29.Qc3 Rc8 30.Ra1 Re8 31.b3 a3 
32.b4 Ra8 33.Nb3 Qe6 34.Na5 Rc8 35.Rd2 f6 36.Qxa3 fxe5 37.fxe5 Qd7 38.Rf1 Bh3 39.Rf4 
Re8 40.Nb3 Qd8 41.Nc5 Rf8 42.Rdf2 g5 43.R4f3 Bg4 44.Rd3 Bh3 45.Qc1 Ng7 46.Rxf8+ Qxf8 
47.Qd1 Ne6 48.Rf3 Qe8 49.Ra3 Qf8 50.Nxe6 Rxe6 51.g4 Rh6 52.Bf3 Qxb4 53.Ra6 Qc3 54.Kh1 
Rg6 55.a3 Kh8 56.a4 Rg8 57.e6 Re8 58.Be2 Rxe6 59.axb5 Rxe2 60.Ra8+ Kg7 61.Ra7+ Kf6 
62.Qf1+ Bxf1 63.Rf7+ Kxf7 64.Kg1 Bh3 65.bxc6 Qc1# 0-1

```

[View this game on Lichess.org](https://lichess.org/SSn4B2RN)



### ACM 1994


[ACM 1994](ACM_1994 "ACM 1994"), round 2, [Cray Blitz](Cray_Blitz "Cray Blitz") - Zarkov




```

[Event "ACM 1994"]
[Site "Cape May USA"]
[Date "1994.06.25"]
[Round "2"]
[White "Cray Blitz"]
[Black "Zarkov"]
[Result "0-1"]

1.e4 e5 2.Bc4 Nf6 3.d3 c6 4.Nf3 d5 5.Bb3 Bb4+ 6.Bd2 Bd6 7.exd5 cxd5 8.Nc3 Be6 
9.O-O Nc6 10.Nb5 Bb8 11.Kh1 a6 12.Nc3 h6 13.a4 Bd6 14.Re1 O-O 15.Bc1 Qb6 16.Kg1 
Rac8 17.Qe2 Rfe8 18.Qd1 Bc5 19.Rf1 Nd4 20.Nxd4 Bxd4 21.a5 Qa7 22.h3 Bxc3 23.bxc3 
d4 24.c4 Bd7 25.Re1 Bc6 26.Ba3 Re6 27.Rb1 Nd7 28.Ba2 Rg6 29.f3 Re8 30.Bb4 Nf6 
31.Bb3 Nh5 32.Bd2 Qc5 33.Ra1 Qe7 34.Kh2 Qh4 35.Rg1 Nf4 36.Bxf4 exf4 37.Ba4 Bxa4 
38.Rxa4 Qf2 39.Qf1 Qxc2 40.Ra1 Re2 41.Rc1 Qxd3 42.Re1 Rge6 43.Rb1 Re7 44.c5 Qc2 
45.Rc1 Qg6 46.Kh1 d3 47.Rb1 Qg3 0-1

```

[View this game on Lichess.org](https://lichess.org/Hx6L7s2L)



### BELCT 2001


[BELCT 2001](BELCT_2001 "BELCT 2001"), round 7, Zarkov - [Yace](Yace "Yace") <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```

[Event "1.BELCT2001"]
[Site "Berlin"]
[Date "2001.10.03"]
[Round "7"]
[White "Zarkov 4.5T"]
[Black "Yace"]
[Result "1-0"]

1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Qb6 5.Nf3 Bd7 6.a3 a5 7.Bd3 Nc6 8.Bc2 Nh6 9.O-O cxd4 
10.cxd4 Nf5 11.Bxf5 exf5 12.Nc3 Be6 13.Na4 Qa7 14.Be3 Be7 15.Rc1 Rc8 16.Qd3 O-O 
17.Rfe1 Rfe8 18.Rc3 Nb8 19.Bg5 Bf8 20.Qb5 Bd7 21.Qxd5 h6 22.Rxc8 Rxc8 23.e6 fxe6 
24.Rxe6 Kh8 25.Nc3 b5 26.Rg6 Bc6 27.Qe5 Qd7 28.Rxh6+ Kg8 29.Rxc6 Qxc6 30.Qxf5 b4 
31.Ne5 Qe8 32.axb4 Nc6 33.bxa5 Nxd4 34.Qe4 Rc5 35.Bf4 Ne6 36.Ng4 Rxa5 37.h3 Qf7 
38.Be5 Bc5 39.Qe2 Qf5 40.Qd2 Ra8 41.Qe1 Qc2 42.Bd6 Qb3 43.Bxc5 Nxc5 44.Qe3 Nb7 
45.Qd2 Rd8 46.Qe2 Nc5 47.Qe5 Nd3 48.Qg5 Ra8 49.Nf6+ Kf8 50.Nd7+ Kf7 51.Qf5+ Ke8 
52.Nd5 Ra1+ 53.Kh2 Re1 54.N7b6 Qxb2 55.Qg6+ Kd8 56.Qc6 Rh1+ 57.Kxh1 Qc1+ 58.Qxc1 
Nxc1 59.g4 Ke8 60.f4 Nd3 61.f5 Nc5 62.Kg2 Nb3 63.Kf3 Nd4+ 64.Kf4 Kf7 65.h4 Nb3 
66.Nd7 Ke8 67.Ne5 Nd4 68.h5 Kf8 69.g5 Ne2+ 70.Kg4 Nc3 71.Nxc3 1-0

```

[View this game on Lichess.org](https://lichess.org/bVrY5kPH)



## See also


* [Bookup](Bookup "Bookup")
* [GNU Chess](GNU_Chess "GNU Chess")
* [Grandmaster Chess](Grandmaster_Chess "Grandmaster Chess")
* [SCP](SCP "SCP")
* [Wasp](Wasp "Wasp") <a id="cite-note-9" href="#cite-ref-9">[9]</a>


## Publications


* [Shawn Benn](Shawn_Benn "Shawn Benn"), [Danny Kopec](Danny_Kopec "Danny Kopec") (**1993**). *The Bratko-Kopec Test Recalibrated.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") » [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")


## Forum Posts


### 1989


* [Zarkov vs. Mach III (10 games)](https://groups.google.com/d/msg/rec.games.chess/_5_aeOAu_tU/L-xvltCmClUJ) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 05, 1989 » [Mach III](Excel "Excel")
* [Estimation of ZARKOV rating](https://groups.google.com/d/msg/rec.games.chess/tojZQDUzb9A/d60hC_gJvjUJ) by Teun Hendriks, [rgc](Computer_Chess_Forums "Computer Chess Forums"), December 08, 1989


### 1990 ...


* [ZARKOV Info Wanted](https://groups.google.com/d/msg/rec.games.chess/0EOSEpL1Wlk/RZXDB4jfpDQJ) by Louis Blair, [rgc](Computer_Chess_Forums "Computer Chess Forums"), January 18, 1990
* [Zarkov at 'Championnat de Paris'](https://groups.google.com/d/msg/rec.games.chess/VMf_SsJNjQA/F_hYOr7Rm08J) by Alain Le Borgne, [rgc](Computer_Chess_Forums "Computer Chess Forums"), May 09, 1990
* [Commercial Chess Programs](https://groups.google.com/d/msg/rec.games.chess/ppLgYSEF5k8/YCTdbmKwNTkJ) by [Mike Valvo](Michael_Valvo "Michael Valvo"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), July 19, 1991 » [ChessMachine](ChessMachine "ChessMachine"), [Fritz](Fritz "Fritz"), [MChess](MChess "MChess")
* [even more chess software reviews](https://groups.google.com/d/msg/rec.games.chess/6v29esLp5do/3lSnz7AM35AJ) by [Eric Schiller](Eric_Schiller "Eric Schiller"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 13, 1991  » [Bookup](Bookup "Bookup")
* [Zarkov vs GrandMaster Chess](https://groups.google.com/d/msg/rec.games.chess/PB9W_x8lX3g/yIxcWNvYV2QJ) by Roger Uzun, [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 16, 1992
* [Zarkov 3.0?](https://groups.google.com/d/msg/rec.games.chess/Oe6AB_nRLGk/lR0ntgu6XYQJ) by Kevin Gowen, [rgc](Computer_Chess_Forums "Computer Chess Forums"), December 18, 1993
* [Chess Laboratories and Zarkov](https://groups.google.com/d/msg/rec.games.chess/uAFyT6PIdd0/tZrfVJpO1QUJ) by notes.tssi, [rgc](Computer_Chess_Forums "Computer Chess Forums"), December 20, 1993
* [Hash table question](http://groups.google.com/group/rec.games.chess/browse_frm/thread/a9d5fb3e489196ed/68f9f93c938f3349) by [John Stanback](John_Stanback "John Stanback"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 23, 1994 » [Transposition Table](Transposition_Table "Transposition Table")


### 1995 ...


* [Draw by Repetition Code, post 4](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7edf36b54a47267d) by [John Stanback](John_Stanback "John Stanback"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 31, 1996 » [Repetitions](Repetitions "Repetitions")
* [new zarkov 4.2 chess program](https://www.stmintz.com/ccc/index.php?id=22930) by Frank Zimmer, [CCC](CCC "CCC"), July 25, 1998
* [Wchess 2000 and Zarkov 5](https://www.stmintz.com/ccc/index.php?id=39629) by Alain Lyrette, [CCC](CCC "CCC"), January 16, 1999


 [Re: Wchess 2000 and Zarkov 5](https://www.stmintz.com/ccc/index.php?id=39662) by [Bert Seifriz](index.php?title=Berthold_Seifriz&action=edit&redlink=1 "Berthold Seifriz (page does not exist)"), [CCC](CCC "CCC"), January 16, 1999 » [WChess](WChess "WChess")
* [Zarkov 4.2 strength?](https://www.stmintz.com/ccc/index.php?id=43684) by Mike Cummings, [CCC](CCC "CCC"), February 18, 1999


### 2000 ...


* [Zarkov news?](https://www.stmintz.com/ccc/index.php?id=120143) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), July 18, 2000
* [1 Hour CCR Test/Zarkov and Duck/Updated Summary](https://www.stmintz.com/ccc/index.php?id=169742) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), May 14, 2001 » [CCR One Hour Test](CCR_One_Hour_Test "CCR One Hour Test")


### 2010 ...


* [Studie: Schachspielen mit ein 286er 12 MHz Laptop - Schachcomputer.info Community](http://www.schachcomputer.info/forum/showthread.php?t=3531) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), May 22, 2010 (German)
* [La Máquina Preservadora 5. John Stanback, Mr. Zarkov](http://www.foro.meca-web.es/viewtopic.php?f=9&t=72&start=30#p4486) by Luis a, [Meca Foro](Computer_Chess_Forums "Computer Chess Forums"), March 21, 2014 (Spanish)
* [Zarkov Chess by John Stanback](http://www.talkchess.com/forum/viewtopic.php?t=60479) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 14, 2016
* [Zarkov collection available ...](http://www.talkchess.com/forum/viewtopic.php?t=60512) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 16, 2016
* [Zarkov 5 Millenium Chess System](http://www.talkchess.com/forum/viewtopic.php?t=64355) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 21, 2017


### 2020 ...


* [Zarkov 4.20?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73621) by Louis Lev, [CCC](CCC "CCC"), April 10, 2020


## External Links


### Chess Program


* [Zarkov's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=357)
* [Zarkov Development History](http://john.stanback.net/zarkov/zarkov_history.html)
* [How Zarkov Plays Chess](http://john.stanback.net/zarkov/zarkov_methods.html)
* [The chess games of Zarkov](http://www.chessgames.com/perl/chessplayer?pid=27063) from [chessgames.com](http://www.chessgames.com/index.html)
* [Free Chess Downloads](http://www.top-5000.nl/cp.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")


### Misc


* [Hans Zarkov, fictional character from Wikipedia](https://en.wikipedia.org/wiki/Hans_Zarkov)


 [Flash Gordon (serial) from Wikipedia](https://en.wikipedia.org/wiki/Flash_Gordon_%28serial%29)
 [Frank Shannon from Wikipedia](https://en.wikipedia.org/wiki/Frank_Shannon)
* [Dr. Hans Zarkov - Flash Gordon Wiki](http://flashgordon.wikia.com/wiki/Dr._Hans_Zarkov)


 [Zarkov's rocket ship - Flash Gordon Wiki](http://flashgordon.wikia.com/wiki/Zarkov%27s_rocket_ship)
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Dr. Hans Zarkov - Flash Gordon Wiki](http://flashgordon.wikia.com/wiki/Dr._Hans_Zarkov), image courtesy [Danny Horn](http://community.wikia.com/wiki/User:Toughpigs)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Zarkov Development History](http://john.stanback.net/zarkov/zarkov_history.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [How Zarkov Plays Chess](http://john.stanback.net/zarkov/zarkov_methods.html) 5. Learn Table
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Septober - Computerschach](http://www.septober.de/chess/index.htm) by [Herbert Marquardt](index.php?title=Herbert_Marquardt&action=edit&redlink=1 "Herbert Marquardt (page does not exist)")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Bookup | Chess Openings | Chess Opening Software](http://www.bookup.com/)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Zarkov 5 Millenium Chess System](http://www.talkchess.com/forum/viewtopic.php?t=64355) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 21, 2017
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a>  [PGN Download NACCC](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=60&Itemid=26&lang=en) from [Computerschaak/Downloads/Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=13&Itemid=26&lang=en) hosted by [CSVN](CSVN "CSVN")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [BELCT 2001 discussion of the game zarkov-yace](https://www.stmintz.com/ccc/index.php?id=192011) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 05, 2001
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Wasp 1.01 x64 by John Stanback released ...](http://www.talkchess.com/forum/viewtopic.php?t=60550) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 22, 2016

**[Up one Level](Engines "Engines")**







 
