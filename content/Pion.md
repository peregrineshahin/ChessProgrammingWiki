---
title: Pion
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Pion**



[ Quark structure of the Pion <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Pion**,  

a chess program developed by a group of students from [Delft Institute of Technology](Delft_University_of_Technology "Delft University of Technology"). [Jan Derksen](Jan_Derksen "Jan Derksen"), [Harry Nefkens](Harry_Nefkens "Harry Nefkens") and [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") started the development in 1979, [Sito Dekker](Sito_Dekker "Sito Dekker"), [Roger Hünen](Roger_H%C3%BCnen "Roger Hünen"), [Gerlach van Beinum](Gerlach_van_Beinum "Gerlach van Beinum") and [John Huisman](John_Huisman "John Huisman") joined the team later <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Written in the [C](C "C") programming language, Pion had an [opening book](Opening_Book "Opening Book") of 4000 positions in 1983, when it searched about 1K [nodes per second](Nodes_per_Second "Nodes per Second") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 


In conjunction with the official name change from Delft Institute of Technology to Delft University of Technology in 1986 <a id="cite-note-6" href="#cite-ref-6">[6]</a>, Pion was superseded by its successor [Dutch](Dutch "Dutch") (**D**elft **U**niversity of **T**echnology **Ch**ess Program). 



### Contents


* [1 Photos](#photos)
* [2 Tournaments](#tournaments)
* [3 ACM 1982 Experience](#acm-1982-experience)
* [4 Selected Games](#selected-games)
	+ [4.1 ACM 1982](#acm-1982)
	+ [4.2 WCCC 1983](#wccc-1983)
* [5 See also](#see-also)
* [6 Publications](#publications)
* [7 External Links](#external-links)
* [8 References](#references)






 [](File:PionTeam.jpg) 
Pion team: <?>, [Jan Derksen](Jan_Derksen "Jan Derksen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Harry Nefkens](Harry_Nefkens "Harry Nefkens") (center), [Roger Hünen](Roger_H%C3%BCnen "Roger Hünen")   
back of head of [Sito Dekker](Sito_Dekker "Sito Dekker") sitting in front of the board <a id="cite-note-7" href="#cite-ref-7">[7]</a>



## Tournaments


Pion played the first four [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"). The first [DOCCC 1981](DOCCC_1981 "DOCCC 1981") was the debut, third with 6/9, the [DOCCC 1982](DOCCC_1982 "DOCCC 1982") fifth with 6/9, the [DOCCC 1983](DOCCC_1983 "DOCCC 1983") third with 5½/8, and the [DOCCC 1984](DOCCC_1984 "DOCCC 1984") third again with 4/6. The [ACM 1982](ACM_1982 "ACM 1982") in [Dallas, Texas](https://en.wikipedia.org/wiki/Dallas%2C_Texas) was a bit harder, 1 out of 4 running on a [VAX 11/780](VAX "VAX") of [Purdue University](https://en.wikipedia.org/wiki/Purdue_University), the [WCCC 1983](WCCC_1983 "WCCC 1983") in [New York](https://en.wikipedia.org/wiki/New_York_City) on a [VAX 11/750](VAX "VAX") of [Bell Laboratories](Bell_Laboratories "Bell Laboratories") supported by [Ken Thompson](Ken_Thompson "Ken Thompson"), and respectable 2 out of 5. Further, Pion played the [International Computer Chess Tournament 1984](International_Computer_Chess_Tournament_1984 "International Computer Chess Tournament 1984") in [Baarn](https://en.wikipedia.org/wiki/Baarn) with 2½/5, running on an [TNO](https://en.wikipedia.org/wiki/Netherlands_Organisation_for_Applied_Scientific_Research) Geminix <a id="cite-note-8" href="#cite-ref-8">[8]</a> with [68000](68000 "68000") processor <a id="cite-note-9" href="#cite-ref-9">[9]</a>.




## ACM 1982 Experience


translation of excerpt from [Tom Fürstenberg's](Tom_F%C3%BCrstenberg "Tom Fürstenberg") Dutch report on [ACM 1982](ACM_1982 "ACM 1982") and [WCCC 1983](WCCC_1983 "WCCC 1983") <a id="cite-note-10" href="#cite-ref-10">[10]</a>:




```C++
The ACM tournament had a special significance, because for the first time a Dutch program participated. Despite only scoring one point, in company with the PION Team was a particular instructive, enjoyable and highly entertaining event!

```


```C++
The PION team, Jan Derksen, Jaap van den Herik and Harry Nefkens sent a tape with source code to Ken Thompson, who arranged that PION could run on a VAX 11/780 of the Purdue University. The team wisely decided to be on the ground a few days before, to solve some possible portability problems - in Delft the program ran on a [PDP-11](PDP-11 "PDP-11"). After some changes, I played a few test games, and in remembrance to its name, PION played only with the pawns. Pieces seemed glued at the bottom rank. Jan tinkered with the program, while Harry concurrently worked on the opening book. A well-meant advice - get never close to a nervous programmer. Harry under voltage is highly explosive! Insults went back and forth, but finally everything worked well under the inspiring leadership of Jaap van den Herik.

```


```C++
On the day of the tournament panic occurred. The terminals from Texas Instruments had no uppercase, while the password of PION to access the VAX 11/780 required one. After a phone call to Bell Labs, [Joe Condon](Joe_Condon "Joe Condon") changed the password, and a few minutes before the start of the first round, team and program were ready. 

```

## Selected Games


### ACM 1982


[ACM 1982](ACM_1982 "ACM 1982"), round 4, Pion - [Savant X](Savant "Savant") <a id="cite-note-11" href="#cite-ref-11">[11]</a>




```

[Event "ACM 1982"]
[Site "Dallas USA"]
[Date "1982.10.26"]
[Round "4"]
[White "Pion"]
[Black "Savant X"]
[Result "0-1"]

1.Nf3 d5 2.g3 Nf6 3.Bg2 Nc6 4.O-O e5 5.d3 Bg4 6.h3 Bxf3 7.Bxf3 e4 
8.Bg2 Bc5 9.Nd2 Qe7 10.c4 e3 11.fxe3 Qxe3+ 12.Kh2 Qe6 13.Nb3 Bd4 
14.cxd5 Nxd5 15.Nxd4 Nxd4 16.e4 Nb6 17.Be3 O-O-O 18.h4 Kb8 19.Bh3 
Qe7 20.a4 h6 21.a5 Nc8 22.Qa4 Ne6 23.Rad1 g5 24.Bxe6 Qxe6 25.Bd4 
gxh4 26.Bxh8 hxg3+ 27.Kxg3 Rxh8 28.Qd4 Rg8+ 29.Kh2 Qg4 0-1

```

### WCCC 1983


[WCCC 1983](WCCC_1983 "WCCC 1983"), round 2, [Ostrich](Ostrich "Ostrich") - Pion <a id="cite-note-12" href="#cite-ref-12">[12]</a>:




```

[Event "WCCC 1983"]
[Site "New York, USA"]
[Date "1983.10.22"]
[Round "2"]
[White "Ostrich"]
[Black "Pion"]
[Result "0-1"]

1.e4 d6 2.d3 g6 3.Be2 Nf6 4.Nf3 Bg7 5.O-O O-O 6.Nc3 Re8 7.Bg5 c5 
8.e5 dxe5 9.Nxe5 Nd5 10.d4 Nxc3 11.bxc3 cxd4 12.cxd4 f6 13.Bc4+ e6 
14.Bh4 g5 15.Bxg5 fxg5 16.Bb5 Bd7 17.Nxd7 Nxd7 18.Qg4 Rc8 19.Qe4 a6
20.Bd3 Nf8 21.Qxb7 a5 22.Rad1 Bxd4 23.Qe4 Qb6 24.h4 gxh4 25.Qg4+ Bg7 
26.Qxh4 Qb2 27.a4 Qb6 28.Bb5 Red8 29.Rc1 Bb2 30.Rcd1 Rxd1 31.Qg4+ Bg7 
32.Qxd1 Rc3 33.Qe2 Kf7 34.Bd3 Kf6 35.Qh5 Qb4 36.g4 e5 37.g5+ Ke7 
38.f3 Qxa4 39.Bxh7 Qe8 40.Qh4 Nxh7 41.Qxh7 Qf8 42.Qe4 Ke6 43.Rf2 Qf5 
44.Qa8 Qxg5+ 45.Rg2 Qc1+ 46.Kh2 Qf4+ 47.Kg1 Qd4+ 48.Kh2 Qh4+ 49.Kg1 
Qe1+ 50.Kh2 Rc7 51.Qe8+ Re7 52.Qc6+ Kf7 53.Qg6+ Kf8 54.Qd3 Ke8 55.Qh7 
Bf8 56.Qh5+ Rf7 57.f4 e4 58.Re2 Qb4 59.Qg6 Qc3 60.Qxe4+ Re7 61.Qg6+ 
Kd7 62.Qg4+ Kd8 63.Rxe7 Kxe7 64.Qg5+ Ke8 65.Qf5 Bg7 66.Qe4+ Kd7 
67.Kg2 Bd4 68.f5 Kd6 0-1 

```

## See also


* [Dutch](Dutch "Dutch")
* [Pawn](Pawn_(Program) "Pawn (Program)")
* [Pedone](Pedone "Pedone")


## Publications


* [Jan Derksen](Jan_Derksen "Jan Derksen"), [John Huisman](John_Huisman "John Huisman") (**1982**). *[Het schaakprogramma PION : vorderingen in 1981/1982](http://www.worldcat.org/title/schaakprogramma-pion-vorderingen-in-19811982/oclc/30495462)*. [Technische Hogeschool Delft](Delft_University_of_Technology "Delft University of Technology") (Dutch)
* [Harry Nefkens](Harry_Nefkens "Harry Nefkens"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1984**). *De openingsbibliotheek van het schaakprogramma PION*. [THD](Delft_University_of_Technology "Delft University of Technology") rapport (Dutch)


## External Links


* [Pion's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=413)
* [Pion from Wikipedia](https://en.wikipedia.org/wiki/Pion)
* [Pion (schaken) from Wikipedia.nl](http://nl.wikipedia.org/wiki/Pion_%28schaken%29) (Dutch)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Pion from Wikipedia](https://en.wikipedia.org/wiki/Pion)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Peter van Diepen](Peter_van_Diepen "Peter van Diepen") (**1983**). *Toernooibulletin van het Nederlands kampioenschap computerschaak 1982*. [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/05-1983,%20toernooibulletin%20van%20het%20Nederlands%20kampioenschap%20computerschaak%201982.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") » [DOCCC 1982](DOCCC_1982 "DOCCC 1982")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ben Mittman](Ben_Mittman "Ben Mittman") (**1983**). *ACM's Thirteenth North American Computer Chess Championship*. [ICCA Newletter, Vol. 6, No. 1](ICGA_Journal#6_1 "ICGA Journal") » [ACM 1982](ACM_1982 "ACM 1982")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](Danny_Kopec "Danny Kopec")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](Danny_Kopec "Danny Kopec")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Delft University of Technology (1986–present) from Wikipedia](https://en.wikipedia.org/wiki/Delft_University_of_Technology#Delft_University_of_Technology_.281986.E2.80.93present.29)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Image from [Peter van Diepen](Peter_van_Diepen "Peter van Diepen") (**1983**). *Toernooibulletin van het Nederlands kampioenschap computerschaak 1982*. [pdf](http://www.schaakcomputers.nl/hein_veldhuis/database/files/05-1983,%20toernooibulletin%20van%20het%20Nederlands%20kampioenschap%20computerschaak%201982.pdf) hosted by [Hein Veldhuis](Hein_Veldhuis "Hein Veldhuis") » [DOCCC 1982](DOCCC_1982 "DOCCC 1982")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [History | TNO DIANA](http://tnodiana.com/node/12)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Jaap van Oosterwijk Bruyn](Jaap_van_Oosterwijk_Bruyn "Jaap van Oosterwijk Bruyn") (**1984**). *International Computer-Chess Tournament in the Netherlands*. [ICCA Journal, Vol. 7, No. 2](ICGA_Journal#7_2 "ICGA Journal")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [CSVN PAGINA2 - Schaakcomputers achterna](http://www.csvnsupplementsite.nl/CSVNPAGINA2.html) by [Tom Fürstenberg](Tom_F%C3%BCrstenberg "Tom Fürstenberg") (Dutch)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [PGN Download NACCC](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=60&Itemid=26&lang=en) from [Computerschaak/Downloads/Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=13&Itemid=26&lang=en) hosted by [CSVN](CSVN "CSVN")
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [New York 1983 - Chess - Round 2 - Game 9 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=65&round=2&id=9)

**[Up one level](Engines "Engines")**







 
