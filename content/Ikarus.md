---
title: Ikarus
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Ikarus**



[ Daedalus und Ikarus <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ikarus**,  

a chess engine by [Munjong](Munjong_Kolss "Munjong Kolss") and [Muntsin Kolss](Muntsin_Kolss "Muntsin Kolss"), written in [Delphi](Delphi "Delphi"). The development started in January 1997, and in May 2000 Ikarus was released as [Young Talent](ChessBase#YoungTalents "ChessBase") by [ChessBase](ChessBase "ChessBase") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and is now a private engine. Ikarus is the German spelling of [Icarus](https://en.wikipedia.org/wiki/Icarus) from [Greek mythology](https://en.wikipedia.org/wiki/Greek_mythology), with his attempt to escape from [Crete](https://en.wikipedia.org/wiki/Crete) by means of wings that his father, [Daedalus](https://en.wikipedia.org/wiki/Daedalus), constructed from feathers and wax. However, the chess engine Ikarus is not related with the internet chess client *Icarus* by *Random Software* <a id="cite-note-4" href="#cite-ref-4">[4]</a> .



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Description](#description)
* [3 Photos & Games](#photos-.26-games)
	+ [3.1 IPCCC 2002](#ipccc-2002)
	+ [3.2 IPCCC 2005 b](#ipccc-2005-b)
	+ [3.3 WCCC 2006](#wccc-2006)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
	+ [5.1 Engine](#engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






Ikarus played three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 1999](WCCC_1999 "WCCC 1999") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn), the [WCCC 2002](WCCC_2002 "WCCC 2002") in [Maastricht](https://en.wikipedia.org/wiki/Maastricht), and the [WCCC 2006](WCCC_2006 "WCCC 2006") in [Turin](https://en.wikipedia.org/wiki/Turin), where Ikarus managed to win the Blitz tournament, awarded by the title of *World Computer Speed-Chess Champion*. Able to play [Chess960](Chess960 "Chess960"), Ikarus participated at the two open [Livingston Chess960 Computer World Championships](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), fifth place in [2005](Chess960CWC_2005 "Chess960CWC 2005") and even third in [2006](Chess960CWC_2006 "Chess960CWC 2006"), and was qualified to play the [Chess960CWC 2009](Chess960CWC_2009 "Chess960CWC 2009") where only four engines competed in the final <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 
Ikarus regularly played the [International Paderborn Computer Chess Championships](IPCCC "IPCCC"). The debut in [1999](IPCCC_1999 "IPCCC 1999") with a shared second place was already promising. Further, Ikarus played various [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), and except one occasion at [CCT6](CCT6 "CCT6") with severe internet access problems due to a dying router <a id="cite-note-7" href="#cite-ref-7">[7]</a>, it most often played for the top rankings. 



## Description


given in 1999 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-8" href="#cite-ref-8">[8]</a> :




```C++
Development of Ikarus started in January 1997 when our previous program, named "BasicChess", reached the 64kb memory limit of Borland [Pascal](Pascal "Pascal") 7.0 and its source code had grown completely cryptic. The 32-bit language Borland [Delphi](Delphi "Delphi") 2.0 allowed us to finally use [hash tables](Transposition_Table "Transposition Table") and the next year or so saw us implement a [graphical user interface](GUI "GUI") and most of the usual standard [search](Search "Search") heuristics ([null move pruning](Null_Move_Pruning "Null Move Pruning"), [history heuristic](History_Heuristic "History Heuristic"), [search extensions](Extensions "Extensions") etc.) as well as some advanced data structures such as a [pawn-king hash table](Pawn_Hash_Table "Pawn Hash Table").

```


```C++
From March 1998 on a [Winboard](WinBoard "WinBoard")-compatible version has been autoplaying a variety of computer opponents. Ikarus also got a new hand-crafted [opening book](Opening_Book "Opening Book"). Over Christmas 1998 we added support for the [endgame databases](Endgame_Tablebases "Endgame Tablebases") created by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"); so our program contains a port of the probing code provided by the author. 

```

## Photos & Games


### IPCCC 2002


 [](http://chess.fsv.de/Pics/Paderborn2002.htm) 
[IPCCC 2002](IPCCC_2002 "IPCCC 2002"): [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [Muntsin Kolss](Muntsin_Kolss "Muntsin Kolss") and [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") in Ikarus vs. [IsiChess](IsiChess "IsiChess"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") far left <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```

[Event "IPCCC 2002"]
[Site "Paderborn GER"]
[Date "2002.03.03"]
[Round "07"]
[White "Ikarus"]
[Black "IsiChess"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2 e6 7.f4 Be7 8.O-O O-O
9.Be3 Nc6 10.Kh1 Qc7 11.a4 Re8 12.Bd3 Nb4 13.a5 Bd7 14.Nf3 Rac8 15.Bb6 Qb8
16.e5 dxe5 17.fxe5 Nfd5 18.Nxd5 exd5 19.Re1 h6 20.c3 Nxd3 21.Qxd3 Bc5
22.Qxd5 Be6 23.Qd2 Bxb6 24.axb6 Rc6 25.Ra4 Rxb6 26.Rd4 Qc7 27.Rd1 Bb3
28.Rd7 Qc4 29.Ra1 Qb5 30.Re1 Rbe6 31.Rd6 Rxd6 32.Qxd6 Bc4 33.Qd2 Bd5
34.Nd4 Qd7 35.Re2 Qg4 36.Qe3 Qg6 37.h3 a5 38.Kh2 b6 39.Qf2 Qg5 40.Nf5 f6 
41.h4 Qh5 42.Qg3 g6 43.Ng7 Qxe2 44.Nxe8 Kf7 45.Nc7 Bc6 46.e6+ Ke7 47.Qxg6 Kd8 
48.Qg7 Kc8 49.e7 Qe5+ 50.Kg1 Qe1+ 51.Kh2 Qxh4+ 52.Kg1 Qe1+ 53.Kh2 Qe5+ 
54.Kh1 Qxc7 55.Qf8+ Kb7 56.e8=Q Bxe8 57.Qxe8 Qh7 58.Qe6 Qb1+ 59.Kh2 Qxb2 
60.Qd7+ Kb8 61.Qd8+ Ka7 62.Qd7+ 1/2-1/2

```

### IPCCC 2005 b


[IPCCC 2005 b](IPCCC_2005_b "IPCCC 2005 b"), Round 7, Ikarus - [Rybka](Rybka "Rybka") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>




```

[Event "15th IPCCC 2005"]
[Site "Paderborn GER"]
[Date "2005.12.30"]
[Round "7"]
[White "Ikarus"]
[Black "Rybka"]
[Result "0-1"]

1.e4 Nc6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Bd3 Nge7 6.Bg5 Be4 7.c3 h6 8.Bxe7 Bxe7 9.Bxe4 dxe4 
10.Nfd2 Qd7 11.Nxe4 O-O-O 12.Qe2 f6 13.f4 f5 14.Nf2 g5 15.O-O Rhg8 16.Kh1 g4 17.Nd1 h5 
18.Nd2 h4 19.Ne3 h3 20.gxh3 gxh3 21.Rf3 Rh8 22.Qf1 Bf8 23.Rxh3 Bh6 24.Qf3 Ne7 25.Rg1 Kb8 
26.Rg2 Qa4 27.Rh5 Qxa2 28.Qh3 Ng8 29.Ndf1 c6 30.Rg6 Re8 31.Rgxh6 Nxh6 32.Rxh6 Rhg8 
33.Qh5 Qxb2 34.Qf7 Qxc3 35.Rxe6 Ref8 36.Qe7 Qxd4 37.Qd6+ Qxd6 38.Rxd6 a5 39.Ng3 Rd8
40.Ngxf5 a4 41.Nc2 Kc7 42.Rxd8 Rxd8 43.Nd6 Ra8 44.Kg2 a3 45.h3 a2 46.f5 Ra5 47.f6 Kd7 
48.f7 Ke7 49.e6 Re5 50.Kf3 b5 51.Ne4 b4 52.Na1 Rxe6 53.Kf4 Rg6 54.Nb3 Rh6 55.Nec5 Rh5 
56.Nd3 c5 57.Nf2 c4 0-1

```

### WCCC 2006


 [](File:WCCC2006Blitz.JPG) 
[WCCC 2006](WCCC_2006 "WCCC 2006"): [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") awards the Blitz trophy to [Munjong Kolss](Munjong_Kolss "Munjong Kolss") of Ikarus <a id="cite-note-15" href="#cite-ref-15">[15]</a>



## Forum Posts


* [Re: Ikarus in CCT6](https://www.stmintz.com/ccc/index.php?id=409977) by [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [CCC](CCC "CCC"), February 07, 2005
* [Ikarus at CCT7](https://www.stmintz.com/ccc/index.php?id=411425) by [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [CCC](CCC "CCC"), February 14, 2005
* [Re: Testposition BT2630.23 and Fruit family](https://www.stmintz.com/ccc/index.php?id=463629) by [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [CCC](CCC "CCC"), November 22, 2005


 [Re: Ikarus, FastMM4 and Delphi 2005?](https://www.stmintz.com/ccc/index.php?id=463649) by [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [CCC](CCC "CCC"), November 22, 2005 
## External Links


### Engine


* [Ikarus (chess) from Wikipedia](https://en.wikipedia.org/wiki/Ikarus_%28chess%29)
* [Ikarus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=69)
* [The chess games of Ikarus](http://www.chessgames.com/player/ikarus) from [chessgames.com](http://www.chessgames.com/index.html)
* [Young Talents](http://www.chessbase.com/support/support.asp?pid=100) from [Support - ChessBase](ChessBase "ChessBase"), May 28, 2000 (dead link)
* [Chess software - IKARUS](http://www.chessbase.com/shop/product.asp?pid=16) from [ChessBase Shop](ChessBase "ChessBase") (dead link)
* [Young Talents](https://www.schachversand.de/en/young-talents.html) by [Schachversand Niggemann](Schachversand_Niggemann "Schachversand Niggemann") (out of production)
* [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)


### Misc


* [Ikarus – Wikipedia.de](https://de.wikipedia.org/wiki/Ikarus) (German)
* [Icarus from Wikipedia](https://en.wikipedia.org/wiki/Icarus)
* [Icarus (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Icarus_%28disambiguation%29)


## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Daedalus und Ikarus, Relief in der Villa Albani, Rom, [Ikarus – Wikipedia.de](https://de.wikipedia.org/wiki/Ikarus) (German) - [Daedalus](https://en.wikipedia.org/wiki/Daedalus) constructs wings for his son, Icarus, after a Roman relief in the [Villa Albani](https://en.wikipedia.org/wiki/Villa_Albani), image comes from the 4th edition of [Meyers Konversations-Lexikon](https://en.wikipedia.org/wiki/Meyers_Konversations-Lexikon) (1885–90), [Daedalus from Wikipedia](https://en.wikipedia.org/wiki/Daedalus) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Young Talents](http://www.chessbase.com/support/support.asp?pid=100) from [Support - ChessBase](ChessBase "ChessBase"), May 28, 2000 (dead link)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Random Software - Mobile / Linux / Windows / Mac / Utilities / Games / Anything | Icarus](http://www.randomsoftware.com/apps/icarus/index.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Result Mainz Chess960 qualifier: 1) Sjeng 2) Rybka 3) Ikarus](http://www.talkchess.com/forum/viewtopic.php?t=28786) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), July 04, 2009
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Livingston Chess960 Computer World Championship | Chessdom](http://software.chessdom.com/livingston-chess960-world-championship) by [Eric van Reem](Eric_van_Reem "Eric van Reem")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Ikarus in CCT6](https://www.stmintz.com/ccc/index.php?id=409977) by [Munjong Kolss](Munjong_Kolss "Munjong Kolss"), [CCC](CCC "CCC"), February 07, 2005
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Ikarus' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=69)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [FSV personal chess service - Paderborn 2002 Pics (from Sunday, 03.03.2002)](http://chess.fsv.de/Pics/Paderborn2002.htm) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [IPCCC 2005 games](https://www.stmintz.com/ccc/index.php?id=475641) by Pedro Beltran, [CCC](CCC "CCC"), December 30, 2005
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Ikarus vs Rybka (PGN)](https://www.stmintz.com/ccc/index.php?id=475254) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), December 30, 2005
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Ikarus vs Rybka - New Update with Diagram](https://www.stmintz.com/ccc/index.php?id=475332) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), December 30, 2005
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Ikarus vs Rybka - New Update +3 for Rybka!](https://www.stmintz.com/ccc/index.php?id=475357) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), December 30, 2005
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Ikarus vs Rybka](https://www.stmintz.com/ccc/index.php?id=475430) by Bigler, [CCC](CCC "CCC"), December 30, 2005
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")

**[Up one Level](Engines "Engines")**







 
