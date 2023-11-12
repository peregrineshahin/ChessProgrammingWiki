---
title: Schach
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Schach**



[ Schach in Persien <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Schach**, (Schach **2.x** and **3.0**)  

one of the early German chess programs, written by [Matthias Engelbach](Matthias_Engelbach "Matthias Engelbach") since 1978 in [Algol](Algol "Algol") <a id="cite-note-3" href="#cite-ref-3">[3]</a> while affiliated with the [Bundeswehr University Munich](https://en.wikipedia.org/wiki/Bundeswehr_University_Munich) <a id="cite-note-4" href="#cite-ref-4">[4]</a>. According to a former [Chessgames.com](https://en.wikipedia.org/wiki/Chessgames.com) description, Schach **2.0** was based on a 1970 version of the [Fortran](Fortran "Fortran") program [Schach](Schach_(US) "Schach (US)") by [Rolf C. Smith](Rolf_C._Smith "Rolf C. Smith") and [Franklin D. Ceruti](Franklin_D._Ceruti "Franklin D. Ceruti") (Version 1 was the 1968 Master's thesis that originated from [Texas A&M University](https://en.wikipedia.org/wiki/Texas_A%26M_University)) <a id="cite-note-5" href="#cite-ref-5">[5]</a> . In the early 90s, [Thomas Kreitmair](Thomas_Kreitmair "Thomas Kreitmair") joined as co-author, starting to re-write Schach in [x86](X86 "X86") [assembly](Assembly "Assembly"). 



## Schach 3.0


In the 90s, along with co-author [Thomas Kreitmair](Thomas_Kreitmair "Thomas Kreitmair"), Schach **3.0** was a complete re-write in [x86](X86 "X86") (486) [assembly language](Assembly "Assembly") for [DOS](MS-DOS "MS-DOS") [PCs](IBM_PC "IBM PC"). It was one of the fastest programs of its time <a id="cite-note-6" href="#cite-ref-6">[6]</a> . Schach **3.0** played seven [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") from [1991](DOCCC_1991 "DOCCC 1991") until [1997](DOCCC_1997 "DOCCC 1997"), and became strong third at the [DOCCC 1994](DOCCC_1994 "DOCCC 1994"). Further, Schach played four [IPCCCs](IPCCC "IPCCC") winning [IPCCC 1994](IPCCC_1994 "IPCCC 1994"), the PC Division of [Don Beal's](Don_Beal "Don Beal") [UPCCC 1992](UPCCC_1992 "UPCCC 1992") and [UPCCC 1993](UPCCC_1993 "UPCCC 1993"), five [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments") from [1993](Aegon_1993 "Aegon 1993") until [1997](Aegon_1997 "Aegon 1997"), and three [ICCA](ICCA "ICCA") tournaments the [WCCC 1995](WCCC_1995 "WCCC 1995"), the [WMCCC 1995](WMCCC_1995 "WMCCC 1995"), and the [WMCCC 1996](WMCCC_1996 "WMCCC 1996") .



## Description


given in 1995 from the [ICGA](ICGA "ICGA") site <a id="cite-note-7" href="#cite-ref-7">[7]</a> :




```C++
Schach 3 is the PC version of Schach 2.x one of the earliest German chess programs. It is a non-commercial project developed and maintained by two former students. Work on Schach started in 1978 and after some surprisingly good results in computer chess tournaments, the authors could not stop working on the program. Even the distance - one of the programmers (Kreitmeir) lives in the Netherlands and the other in Germany - is no real handicap. 

```


```C++
The program is a more or less simple [Shannon-A](Type_A_Strategy "Type A Strategy") program with all the known extensions (the authors believe in the [brute-force](Brute-Force "Brute-Force") method for computer chess). The program is written in 486- assembler and can search 9 or ten plies in the [middlegame](Middlegame "Middlegame"). Schach participated in the 1980, 1983 and 1986 World Championships, in the ACM events in the period 1981-1985 and in the German and Dutch Championships since 1992. Best results were a 6th place in Linz 1980 and New York 1983, a 3rd place in the 1994 Dutch Championship and a first place in the 1994 German Championship ([Zugzwang](Zugzwang_(Program) "Zugzwang (Program)") was absent, but we all need some good luck!) 

```

## Selected Games


### Chess 4.9


[WCCC 1989](WCCC_1989 "WCCC 1989"), round 4, [Chess 4.9](Chess_(Program) "Chess (Program)") - Schach 2.3 <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```

[Event "WCCC 1980"]
[Site "Linz, Austria"]
[Date "1980.09.28"]
[Round "4"]
[White "Chess 4.9"]
[Black "Schach 2.3"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.c3 dxc3 5.Bc4 Nf6 6.Nxc3 Bd6 7.Qe2 O-O 
8.O-O Ne5 9.Bd2 c6 10.Bb3 b5 11.Nxe5 Bxe5 12.f4 Bd4+ 13.Kh1 Re8 14.e5 
Bxc3 15.Bxc3 d5 16.a4 d4 17.Bd2 bxa4 18.Rxa4 c5 19.Ba5 Qd7 20.Qc2 Ba6 
21.Rfa1 d3 22.Qxc5 Rac8 23.Qg1 Nh5 24.Bd2 Bb7 25.Rxa7 Rc7 26.Bd1 Qh3 
27.Qf2 Qf5 28.Bf3 Rb8 29.Bxb7 Nxf4 30.Bxf4 d2 31.Qxd2 g5 32.Bxg5 Rcxb7 
33.Rxb7 Rxb7 34.Ra8+ Kg7 1-0 

```

### Nona


[WCCC 1986](WCCC_1986 "WCCC 1986"), round 1, Schach 2.7 - [Nona](Nona "Nona") <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```

[Event "WCCC 1986"]
[Site "Cologne, Germany"]
[Date "1986.06.11"]
[Round "1"]
[White "Schach 2.7"]
[Black "Nona"]
[Result "1-0"]

1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.Nf3 Bc5 5.e3 Nc6 6.a3 Ngxe5 7.Nxe5 Nxe5 
8.Be2 d6 9.b4 Bb6 10.Bb2 f6 11.O-O Bf5 12.a4 a5 13.Bd4 axb4 14.Bxb6 cxb6 
15.Qb3 Kd7 16.Qxb4 Kc8 17.Rd1 Nf7 18.Qb2 Ne5 19.Nc3 Re8 20.Nb5 Nf7 21.Rd4 
Kb8 22.Bh5 g6 23.Bf3 Qe7 24.Rad1 Rd8 25.R1d2 h5 26.Qb3 Ng5 27.Bd5 Ra5 
28.Rb2 Ra6 29.Rd1 Bg4 30.Rdb1 1-0 

```

### Ferret


[WMCCC 1996](WMCCC_1996 "WMCCC 1996"), round 1, Schach 3.0 - [Ferret](Ferret "Ferret") <a id="cite-note-10" href="#cite-ref-10">[10]</a>




```

[Event "WMCCC 1996"]
[Site "Jakarta, Indonesia"]
[Date "1996.10.??"]
[Round "1"]
[White "Schach 3.0"]
[Black "Ferret"]
[Result "1/2-1/2"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nc6 5.Nf3 e5 6.dxe5 Qxd1+ 7.Kxd1 Bg4 
8.Bf4 Nge7 9.Be2 Ng6 10.Bg3 O-O-O+ 11.Nbd2 Bxf3 12.Bxf3 Ngxe5 13.Be2 Bd6 
14.Kc2 f5 15.Rad1 Bc7 16.Nb3 b6 17.Bb5 Kb7 18.Rxd8 Rxd8 19.f4 Ng6 20.Rf1 
Nge7 21.Bc4 h6 22.Bh4 Rd6 23.Bf7 Nd5 24.Rf3 Nd8 25.Bxd5+ Rxd5 26.c4 Rd6 
27.Bxd8 Rxd8 28.g3 g6 29.Nd2 a6 30.Rd3 Re8 31.Rd7 Re2 32.Rg7 Rxh2 33.Rxg6
h5 34.Kd3 h4 35.Nf3 hxg3 36.Nxh2 gxh2 37.Rh6 Bxf4 38.Rh7+ Kc6 39.Ke2 Bg3 
40.Kf3 f4 41.b3 Kd6 42.Ke4 Ke6 43.Rh6+ Kf7 44.a3 Ke7 45.b4 Kf7 46.bxc5 
bxc5 47.a4 a5 48.Kf3 Kg7 49.Rh3 Kf6 50.Rh5 Kg6 51.Rh8 Kf6 52.Ke4 Ke6 
53.Rh5 Kf6 1/2-1/2 

```

## See also


* [Schach](Schach_(US) "Schach (US)") by [Rolf C. Smith](Rolf_C._Smith "Rolf C. Smith") and [Franklin D. Ceruti](Franklin_D._Ceruti "Franklin D. Ceruti")
* [Schach dem Schweinehund](Schweinehund "Schweinehund")
* [Schach MV 5,6](Schach_MV_5,6 "Schach MV 5,6") by [Helmut Richter](Helmut_Richter "Helmut Richter")


## Forum Posts


* [QMW computer chess](http://groups.google.com/group/rec.games.chess/browse_frm/thread/51267e26536fa912) by [Don Beal](Don_Beal "Don Beal"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 19, 1993 » [UPCCC 1993](UPCCC_1993 "UPCCC 1993")
* [Schach 2.7 vs Cray Blitz [1986 World Computer Chess Championship](https://www.stmintz.com/ccc/index.php?id=134782)] by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), October 24, 2000 » [WCCC 1986 Adjudication](WCCC_1986#Adjudication "WCCC 1986")
* [Schach 3.0](https://www.stmintz.com/ccc/index.php?id=222098) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 08, 2002


## External Links


### Chess Program


* [Schach's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=187)
* [The chess games of Schach 2 3](http://www.chessgames.com/perl/chessplayer?pid=64934) from [Chessgames.com](https://en.wikipedia.org/wiki/Chessgames.com)


### Schach


* [Schach from Wikipedia](https://en.wikipedia.org/wiki/Schach)
* [Schach from Wikipedia.de](http://de.wikipedia.org/wiki/Schach) (German) = [Chess](Chess "Chess")
* [Schach (Zeitschrift) from Wikipedia.de](http://de.wikipedia.org/wiki/Schach_%28Zeitschrift%29) (German [Chess periodical](https://en.wikipedia.org/wiki/List_of_chess_periodicals))


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Schach from Wikipedia.de](http://de.wikipedia.org/wiki/Schach) (German)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Persian](https://en.wikipedia.org/wiki/Persian_people) youth playing chess with two of his suitors. Illustration to the [Haft Awrang](https://en.wikipedia.org/wiki/Haft_Awrang) of [Nur ad-Dīn Abd ar-Rahmān Jāmī](https://en.wikipedia.org/wiki/Jami), in the story *A Father Advises his Son About Love.* [Freer](https://en.wikipedia.org/wiki/Freer_Gallery_of_Art) and [Sackler Galleries](https://en.wikipedia.org/wiki/Arthur_M._Sackler_Gallery), [The Smithsonian Institution](https://en.wikipedia.org/wiki/Smithsonian_Institution), [Washington, D.C.](https://en.wikipedia.org/wiki/Washington,_D.C.)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [The Fifteenth ACM Computer Chess Championship, San Francisco California, October 7-9, 1984](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c9575), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1984_15th_NACCC/1984%20NACCC.062303012.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Matthias Engelbach - Profile](http://www.xing.com/profile/Matthias_Engelbach), [XING](https://en.wikipedia.org/wiki/XING)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The chess games of Schach 2 3](http://www.chessgames.com/perl/chessplayer?pid=64934) from [Chessgames.com](https://en.wikipedia.org/wiki/Chessgames.com)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Schach 3.0](https://www.stmintz.com/ccc/index.php?id=222098) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 08, 2002
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Schach's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=187)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Linz 1980 - Chess - Round 4 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=68&round=4&id=2)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Cologne 1986 - Chess - Round 1 - Game 10 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=62&round=1&id=10)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Jakarta 1996 - Chess - Round 1 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=55&round=1&id=6)

**[Up one level](Engines "Engines")**







 
