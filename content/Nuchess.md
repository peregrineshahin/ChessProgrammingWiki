---
title: Nuchess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nuchess**


**Nuchess**,  

the [Northwestern University](Northwestern_University "Northwestern University") chess program by [David Slate](David_Slate "David Slate"), one of the original authors of [Chess x.x](Chess_(Program) "Chess (Program)"), and [William Blanchard](William_Blanchard "William Blanchard") of Vogelback computing center at Northwestern University. Nuchess played the [WCCC 1980](WCCC_1980 "WCCC 1980") in [Linz](https://en.wikipedia.org/wiki/Linz) on a [CDC Cyber 176](CDC_Cyber "CDC Cyber") and the [WCCC 1983](WCCC_1983 "WCCC 1983") in [New York](https://en.wikipedia.org/wiki/New_York_City) on a [Cray-1](Cray-1 "Cray-1") 4Mb, becoming sixth and fourth respectively. Nuchess further participiated at the [ACM 1981](ACM_1981 "ACM 1981") (runner up), the [ACM 1982](ACM_1982 "ACM 1982"), where [Belle](Belle "Belle") won on tie-break points before [Cray Blitz](Cray_Blitz "Cray Blitz"), Nuchess and [CHAOS](CHAOS "CHAOS"), all 3/4, and the [ACM 1984](ACM_1984 "ACM 1984"). Nuchess was a 64 bit program, written in [Fortran](Fortran "Fortran"), program size in 1983 was about 250K and it searched about 2.8K [Nodes per second](Nodes_per_Second "Nodes per Second") <a id="cite-note-1" href="#cite-ref-1">[1]</a> . Nuchess, apparently the successor of Chess 4.9, was mentioned as Chess 5.0 at the [Ars Electronica](https://en.wikipedia.org/wiki/Ars_Electronica) site of the [WCCC 1980](WCCC_1980 "WCCC 1980") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , where Chess 4.9 did also compete with [Larry Atkin](Larry_Atkin "Larry Atkin") and [David Cahlander](David_Cahlander "David Cahlander") as authors.



### Contents


* [1 Photos & Games](#photos-.26-games)
* [2 Interior Node Recognizer](#interior-node-recognizer)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 External Links](#external-links)
* [6 References](#references)






 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbddbaf1) 
[Ken Thompson](Ken_Thompson "Ken Thompson"), [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [Joe Condon](Joe_Condon "Joe Condon"), [David Slate](David_Slate "David Slate"), and [William Blanchard](William_Blanchard "William Blanchard")  



[WCCC 1983](WCCC_1983 "WCCC 1983"), Nuchess - [Belle](Belle "Belle") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "WCCC 1983"]
[Site "New York, USA"]
[Date "1983.10.23"]
[Round "3"]
[White "Nuchess"]
[Black "Belle"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d4 exd4 6.O-O Be7 7.e5 Ne4 8.Nxd4 O-O
9.Nf5 d5 10.exd6 Bxf5 11.dxe7 Nxe7 12.Be3 Nd5 13.Qf3 Nxe3 14.fxe3 Bg6 15.Qf4 b5
16.Bb3 c5 17.c4 Qf6 18.Qxf6 Nxf6 19.Rc1 b4 20.Nd2 Rfe8 21.Re1 Rad8 22.Nf1 Bd3
23.Rad1 Ng4 24.Ba4 Rf8 25.Nd2 Ne5 26.Bb3 Rd6 27.Nf3 Nxf3+ 28.gxf3 f5 29.Rd2 Re8
30.Kf2 f4 31.exf4 Rxe1 32.Kxe1 Rd4 33.Kf2 Kf7 34.Ke3 Bxc4 35.Rxd4 cxd4+ 36.Kxd4
Bxb3 37.axb3 Kf6 38.Ke4 g6 39.h4 Ke6 40.f5+ gxf5+ 41.Kd4 Kd6 42.f4 Ke6 43.Kc5 a5
44.h5 Kf7 45.Kd5 Kf6 46.Kd6 Kf7 47.Ke5 Ke8 48.Kxf5 1-0

```

 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbde572f) 
[Ken Thompson](Ken_Thompson "Ken Thompson") now with [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") kibitzing - just before 19... b4 


Game and short analyze on Lichess.org : [[1]](https://en.lichess.org/TTY9CjMP)



## Interior Node Recognizer


Like Chess 4.x, Nuchess was a [brute-force](Brute-Force "Brute-Force") chess program. It did not only [evaluate](Evaluation "Evaluation") [leaf nodes](Leaf_Node "Leaf Node") but also the [interior of the tree](Interior_Node_Recognizer "Interior Node Recognizer"), to narrow [bounds](Bound "Bound") and to concern with determinations of or guesses of game-theoretic win/draw/loss values <a id="cite-note-4" href="#cite-ref-4">[4]</a> .



## See also


* [WCCC 1980 - Book Issues](WCCC_1980#BookIssues "WCCC 1980")
* [Rule of the Square - Nuchess vs. Cray Blitz @ ACM 1984](Rule_of_the_Square#NuchessCrayBlitz "Rule of the Square")


## Publications


* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1984**). *Korchnoi defeats Nuchess in Half a Jiffy*. [ICCA Journal, Vol. 7, No. 2](ICGA_Journal#7_2 "ICGA Journal") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")


## External Links


* [Nuchess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=411)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](Danny_Kopec "Danny Kopec")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ars Electronica - Die Teilnehmer an der 3. Computerschach-Weltmeisterschaft](http://90.146.8.18/de/archives/festival_archive/festival_catalogs/festival_artikel.asp?iProjectID=9497) (German)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New York 1983 - Chess - Round 3 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=65&round=3&id=1)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [David Slate](David_Slate "David Slate") (**1984**). *Interior-node Score Bounds in a Brute-force Chess Program.* [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal"), pp. 184-192
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Viktor Korchnoi from Wikipedia](https://en.wikipedia.org/wiki/Viktor_Korchnoi)

**[Up one level](Engines "Engines")**







 
