---
title: Quickstep
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Quickstep**


**Quickstep**, (Quick Step)  

a German chess computer entered by [Klaus Dieter Langer](Klaus_Dieter_Langer "Klaus Dieter Langer") at the [WMCCC 1989](WMCCC_1989 "WMCCC 1989") in [Portorož](https://en.wikipedia.org/wiki/Portoro%C5%BE). 
The program appeared to be an unauthorized version of the [Mephisto Almeria](Mephisto_Almeria "Mephisto Almeria") program by [Richard Lang](Richard_Lang "Richard Lang")
<a id="cite-note-1" href="#cite-ref-1">[1]</a>, 
winner of the previous year's [WMCCC 1988](WMCCC_1988 "WMCCC 1988") in [Almería](https://en.wikipedia.org/wiki/Almer%C3%ADa). 
Quickstep was a [VMEbus](https://en.wikipedia.org/wiki/VMEbus) system with [68030](68030 "68030") processor @ 33 MHz, and 8 MiB of [RAM](Memory#RAM "Memory"), 
connected with a small terminal with a 32-character display and keypad to enter moves.



## Strange facts


[Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen") as member of the Mephisto team mentioned following facts in a 2003 [CCC](CCC "CCC") post <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++I was a member of the Mephisto team in Portoroz and after a few rounds we found some facts very strange:
```

1. `We had never heard of Mr. Langer before`
2. `Asking him questions, he didn't seem to know anything about chess or computer chess`
3. `During the games he was watching everything, except the computerscreen. He didn't seem to be interested in the games at all`
4. `A quick glance at his IO showed that the contents of this were exactly the same as Mephisto's`
5. `We replayed Quickstep's games on a regular Almeria 32 bit machine and discovered that almost all the moves were identical`



```C++At last we informed the ICCA about it and Mr. Langer was requested to show the source code of Quickstep. He didn't and so his program was disqualified. We never heard of him anymore... 
```

## Disqualification


During several meetings of the Tournament Directors [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") with Mr. Langer, presenting the Mephisto evidence, 
Mr. Langer was not able or willing to provide any evidence Quickstep was original. After consulting ICCA President [David Levy](David_Levy "David Levy"), Quickstep and Mr. Langer were disqualified from the tournament <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Selected Games


### Mephisto


[WMCCC 1989](WMCCC_1989 "WMCCC 1989"), round 6, Quickstep - [Mephisto X](Mephisto "Mephisto") <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "WMCCC 1989"]
[Site "Portorož, Slovenia"]
[Date "1989.09.??"]
[Round "6"]
[White "Quickstep"]
[Black "Mephisto X"]
[Result "*"]

1.d4 d5 2.c4 dxc4 3.Nf3 c5 4.e3 e6 5.Bxc4 Nf6 6.O-O a6 7.Qe2 b5 8.Bd3 cxd4 9.exd4 Bb7 10.a4 bxa4 
11.Rxa4 Be7 12.Nc3 O-O 13.Bg5 a5 14.Rd1 Bc6 15.Raa1 Nbd7 16.Ne5 Bb7 17.Bc2 Qc8 18.Qe3 Bb4 19.Bd3 
g6 20.Rdc1 Nxe5 21.dxe5 Qc6 22.Qh3 Bxc3 23.bxc3 Ne4 24.Bxe4 Qxe4 25.Re1 Qc6 26.Bf6 h5 27.Re3 Rfc8 
28.Rg3 Kf8 29.Qh4 Ke8 30.Be7 Qe4 31.Qf6 Qf5 32.Qxf5 exf5 33.Bf6 a4 34.Ra3 Bd5 35.Rd3 Bb3 36.Ra1 a3 
37.c4 Rab8 38.e6 fxe6 39.Be5 Rb6 40.Rd6 Rxd6 41.Bxd6 a2 42.c5 Bd5 43.f3 Ra8 44.Kf2 Kd7 45.Ke3 Ra4 
46.Ke2 Rb4 47.Be5 Kc6 48.Bf6 Rb1 49.Ke3 g5 50.Bd4 f4+ 51.Ke2 Bc4+ 52.Kd2 Kd5 53.Bc3 Kxc5 54.Bf6 g4 
55.Kc2 Rxa1 56.Bxa1 Bf1 57.Bf6 Bxg2 58.Kb2 gxf3 59.Bh4 e5 0-1

```

### AI Chess


[WMCCC 1989](WMCCC_1989 "WMCCC 1989"), round 7, [AI Chess](AI_Chess "AI Chess") - Quickstep <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "WMCCC 1989"]
[Site "Portorož, Slovenia"]
[Date "1989.09.??"]
[Round "7"]
[White "AI Chess"]
[Black "Quickstep"]
[Result "*"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 b6 5.Ne2 Ba6 6.a3 Bxc3+ 7.Nxc3 d5 8.Qf3 c5 9.b4 cxd4 10.exd4 O-O 
11.Bg5 Nbd7 12.cxd5 Bb7 13.Bb5 h6 14.Bh4 Qc8 15.Rc1 g5 16.Qg3 Kh8 17.Qe3 a6 18.Bxd7 Nxd7 19.dxe6 
fxe6 20.Ne4 Qd8 21.Bg3 Rc8 22.O-O Bd5 23.Nd6 Rxc1 24.Rxc1 b5 25.Qd3 Kg7 26.Rc7 Qxc7 27.Ne8+ Rxe8 
28.Bxc7 Nf6 29.Be5 Rc8 30.f3 h5 31.Kf2 h4 32.Qd2 Kg6 33.Qd1 Rc3 34.Qb1+ Kf7 35.Qb2 Rc8 36.Qe2 Kg6 
37.Qd3+ Kg7 38.h3 Kf7 39.Qd2 Kg6 40.Ke1 Nd7 41.Bd6 Nf6 42.Qe3 Rd8 43.Qd3+ Kf7 44.Bh2 Re8 45.Be5 Bb7 
46.Qc2 Re7 47.Ke2 Rd7 48.Kf1 Re7 49.Ke1 Re8 50.Bxf6 Kxf6 51.Qh7 Bc6 52.Qh6+ Kf7 53.Qxg5 Rh8 54.Qe5 
Rc8 55.Qf4+ Ke8 56.Qxh4 Bd5 57.Qh8+ Kd7 1-0 

```

## See also


* [Historical Examples](Historical_Examples "Historical Examples")


## Publications


* [Richard Lang](Richard_Lang "Richard Lang") (**1989**). *The Ninth World Microcomputer Chess Championship*. [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [David Levy](David_Levy "David Levy") (**1989**). *Disqualification at Portorož*. [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")
* [Thomas Mally](Thomas_Mally "Thomas Mally") (**1989**). *Mikro-WM in Portorose (Portorož)*. [Modul](Modul "Modul") 3/89, [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/09-1989,%20Modul,%20Thomas%20Mally,%20Mikro-WM%201989%20in%20Portorose.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") » [WMCCC 1989](WMCCC_1989 "WMCCC 1989")


## Forum Posts


* [Re: The truth about Deep <9> : Remember Quick Step](https://www.stmintz.com/ccc/index.php?id=289376) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), March 15, 2003 » [Deep<9>](Deep9 "Deep9")
* [Re: Deep 9 incident](https://www.stmintz.com/ccc/index.php?id=289377) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), March 15, 2003


## External Links


* [Quick Step's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=456)
* [9. WMCCC Portoroz 1989](https://www.schach-computer.info/wiki/index.php/9._WMCCC_Portoroz_1989) from [Schachcomputer.info - Wiki](https://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Richard Lang](Richard_Lang "Richard Lang") (**1989**). *The Ninth World Microcomputer Chess Championship*. [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: The truth about Deep <9> : Remember Quick Step](https://www.stmintz.com/ccc/index.php?id=289376) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), March 15, 2003
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [David Levy](David_Levy "David Levy") (**1989**). *Disqualification at Portorož*. [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Portorož 1989 - Chess - Round 6 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=75&round=6&id=3)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Portorož 1989 - Chess - Round 7 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=75&round=7&id=3)

**[Up one level](Engines "Engines")**







 
