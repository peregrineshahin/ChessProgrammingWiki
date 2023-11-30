---
title: Phoenix
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Phoenix**



[ Phoenix depicted by [F.J. Bertuch](https://en.wikipedia.org/wiki/Friedrich_Justin_Bertuch) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Phoenix**, (Sun Phoenix)  

a chess program by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), which in 1982 rose from the ashes of [Prodigy](Prodigy "Prodigy") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. In the later 80s [Marius Olafsson](Marius_Olafsson "Marius Olafsson") helped with the implementation of a [parallel search](Parallel_Search "Parallel Search"). Phoenix and Sun Phoenix participated at four [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 1983](WCCC_1983 "WCCC 1983"), [WCCC 1986](WCCC_1986 "WCCC 1986"), [WCCC 1989](WCCC_1989 "WCCC 1989"), and [WCCC 1995](WCCC_1995 "WCCC 1995"). It tied for first place in the 1986 World Championships. Phoenix further played seven consecutive [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), beside the mentioned [WCCC 1983](WCCC_1983 "WCCC 1983") simultaneously the ACM 1983, the [ACM 1984](ACM_1984 "ACM 1984"), [ACM 1985](ACM_1985 "ACM 1985"), [ACM 1986](ACM_1986 "ACM 1986"), [ACM 1987](ACM_1987 "ACM 1987"), [ACM 1988](ACM_1988 "ACM 1988"), and [ACM 1989](ACM_1989 "ACM 1989"). 


In his 1987 [ICCA Journal](ICGA_Journal#10_3 "ICGA Journal") paper *Speculative Computing*, Schaeffer mentions *[The Null-Move Algorithm](Null_Move_Pruning "Null Move Pruning")* or *[Don Beal's](Don_Beal "Don Beal") [null-move](Null_Move "Null Move")*, and used it none [recursively](Recursion "Recursion") up to once per search path in his tactical [scout](Scout "Scout") solver *Minix* (Mini-Phoenix), which up and then gave the parallel running Phoenix, which was a less deep searcher than *Minix*, some tactical hints <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Namesake


* [Phoenix (Rahul)](Phoenix_(Rahul) "Phoenix (Rahul)")


## See also


* [Planner](Planner "Planner")
* [Prodigy](Prodigy "Prodigy")


## Quotes


### [Waterloo](University_of_Waterloo "University of Waterloo")


[Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") in *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*, pp. 8 <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```C++
My Ph.D. was not going well, so in the summer of 1982 I started looking for a distraction. Yes, I started writing yet another chess program, this one called Phoenix (it rose from the ashes of [Prodigy](Prodigy "Prodigy")). The [Planner](Planner "Planner") and Prodigy experiences were invaluable, as they convinced me that contrary to all my expectations, lots of chess knowledge didn't work. Which programs were winning the tournaments? The ones with little knowledge, but with the ability to consider an enormous number of chess positions. With a twinge to regret, I wrote Phoenix to mimic these "dumb" programs. The results were immediate. Phoenix didn't know nearly as much about chess as Prodigy did, but it would continually beat it game after game. Obviously, my old approach, imparting human knowledge to an inanimate machine, wasn't the best way to train a computer to play strong chess. 

```

### [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")


[Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") on [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing") <a id="cite-note-5" href="#cite-ref-5">[5]</a> :




```C++
... I can speak from experience here. In the early versions of my chess program Phoenix, I generated my Zobrist hash numbers using my student id number as a seed, naively thinking the [random numbers generated](Pseudorandom_Number_Generator "Pseudorandom Number Generator") by this seed would be good enough. A few years later I put code in to detect when my 32-bit hash key matched the wrong position. To my surprise, there were **lots** of errors. I changed my seed to another number and the error rate dropped dramatically. With this better seed, it became very, very rare to see a hash error. All randomly generated numbers are not the same! 

```

### [WCCC 1986](WCCC_1986 "WCCC 1986")


[Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") in *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*, pp. 9 <a id="cite-note-6" href="#cite-ref-6">[6]</a>:




```C++
I worked hard on Phoenix in preparation of the triennial [World Computer Chess Championship in 1986](WCCC_1986 "WCCC 1986"). To improve the program's performance it was modified to run in [parallel](Parallel_Search "Parallel Search"), using up to thirty computers. They would divide up the work, and each computer would solve part of the problem. In effect, the program was like a small business organization, with a manager to allocate work and employees to do the assigned tasks. The hard work payed off, Phoenix tied for first place in the world championship. I partied late into the night after the final game, intoxicated with success and Coca-Cola. It took a long time for me to come down from my high. 

```

## Descriptions


### 1989


given in the [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-7" href="#cite-ref-7">[7]</a> :




```C++
Phoenix uses state-of-the-art search techniques including [singular extensions](Singular_Extensions "Singular Extensions"), [minimal window](Null_Window "Null Window") searching, [transposition tables](Transposition_Table "Transposition Table"), and the [history heuristic](History_Heuristic "History Heuristic"). The program has lots of chess knowledge, including an extensive long range planner. 

```


```C++
Phoenix is capable of running in parallel on a network of machines. In tournament mode, Phoenix is actually two programs: ParaPhoenix and ParaMinix. ParaPhoenix uses 10 [Sun-4s](Sun#4 "Sun") to build trees looking for the best positional move. ParaMinix uses 10 Sun 4s to build trees looking for the best tactical moves. Because of its specialized task, ParaMinix is capable of searching 1-2 ply deeper than ParaPhoenix. ParaMinix has the ability to veto ParaPhoenix's move choice, if a tactically superior move of found. The parallelism is archived using the [Dynamic Principal Variation Splitting Algorithm](Parallel_Search#PrincipalVariationSplitting "Parallel Search"). 

```

### 1995


given in [1995](WCCC_1995 "WCCC 1995") from the [ICGA](ICGA "ICGA") site <a id="cite-note-8" href="#cite-ref-8">[8]</a> :




```C++
The Phoenix program was an active participant in the 1980's computer chess tournaments and tied for first place in the 1986 World Championships. The program competing this year is essentially the same as that which competed in the 1989 World Computer Chess Championships. Phoenix's participation in the 1995 championships will serve as a benchmark for measuring improvements in the field. Phoenix will be running on an [HP 9000/720](https://en.wikipedia.org/wiki/HP_9000#Series_700) with 64MB [RAM](Memory#RAM "Memory"), which will be comparable to that used by most participants, and therefore the primary difference will be in the software. Expectations are that the software advances in the last 6 years will allow the other programs to move past Phoenix '89 in the final standings. Perhaps the best possible outcome would have Phoenix finishing in last place, providing some experimental evidence of the progress in the field! 

```

## Selected Games


### WCCC 1986


[WCCC 1986](WCCC_1986 "WCCC 1986"), round 3, [BCP](BCP "BCP") vs. Sun Phoenix <a id="cite-note-9" href="#cite-ref-9">[9]</a>




```
[Event "WCCC 1986"]
[Site "Cologne, Germany"]
[Date "1986.06.13"]
[Round "3"]
[White "BCP"]
[Black "Sun Phoenix"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Qb6 5.Nf3 Bd7 6.Bd3 cxd4 7.Nxd4 Nc6 8.Nxc6 Bxc6 
9.O-O O-O-O 10.Nd2 f6 11.Qg4 Re8 12.Re1 Nh6 13.Qh3 Bc5 14.Qg3 Ng4 15.Qxg4 Bxf2+
16.Kf1 Bxe1 17.Kxe1 fxe5 18.Qxg7 Qe3+ 19.Be2 Rhg8 20.Qf7 Bb5 21.Qf2 Qxe2+ 
22.Qxe2 Bxe2 23.Kxe2 Rxg2+ 24.Ke3 Rxh2 25.a4 Rf8 26.a5 h5 27.Ra4 Rh1 28.Ra1 h4 
29.Rb1 Re1+ 30.Kd3 h3 31.Nf1 Rfxf1 0-1 

```

### ACM 1988


 [](File:SchaefferACM88.jpg) 
[ACM 1988](ACM_1988 "ACM 1988"), round 2, Sun Phoenix vs. [Deep Thought](Deep_Thought "Deep Thought"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") counts his pieces, one by one <a id="cite-note-10" href="#cite-ref-10">[10]</a>




```
[Event "ACM 1988"]
[Site "Orlando USA"]
[Date "1988.11.13"]
[Round "2"]
[White "Sun Phoenix"]
[Black "Deep Thought 0.02"]
[Result "0-1"]

1.c4 e5 2.Nc3 Bb4 3.Nd5 Ba5 4.b4 c6 5.bxa5 cxd5 6.cxd5 Nf6 7.Qa4 Nxd5 8.Qe4 Nc7 9.Qxe5+ Ne6 
10.Bb2 Nc6 11.Qd5 Nxa5 12.e4 Nc6 13.Qd6 Qb6 14.Rb1 Nc5 15.Bc4 f6 16.f3 Qb4 17.Qd5 Ne5 18.Bf1 
d6 19.a3 Qb6 20.a4 Be6 21.Bb5+ Ke7 22.Qd4 Bb3 23.Ra1 Bxa4 24.Bxa4 Ned3+ 25.Kf1 Qxb2 26.Qxb2 
Nxb2 27.Bc2 Nc4 28.Ke2 Ne6 29.Kd1 b5 30.Ne2 Rhc8 31.e5 Nxe5 32.Nc3 Nd4 33.Bxh7 f5 34.Ne2 Nxe2 
35.Kxe2 Kf6 36.f4 Nc4 37.g4 fxg4 38.Be4 Re8 39.Kd3 d5 40.Ra6+ Re6 41.Bxd5 Rxa6 42.Bxa8 Ra2 
43.Bc6 a6 44.Rg1 Rxd2+ 45.Kc3 Rxh2 46.Bd5 Ne3 0-1

```

## Publications


* [Tim Breitkreutz](Tim_Breitkreutz "Tim Breitkreutz"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1984**). *Computer vs Computer via Computer*. [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal"), reprinted in [Computer Chess Reports 1985](Computer_Chess_Reports "Computer Chess Reports"), Vol. 3, No. 2 » Phoenix, [Super Constellation](Super_Constellation "Super Constellation"), [Testing](Engine_Testing "Engine Testing")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). The Utility of Expert Knowledge. Proceedings [IJCAI 85](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai85.html), pp. 585-587. Los Angeles. [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-85-VOL1/PDF/111.pdf)
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Improved Parallel Alpha-Beta Searching*. Proceedings ACM/IEEE Fall Joint Computer Conference, pp. 519-527.
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1987**). *Speculative Computing*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Distributed Game-Tree Searching*. Journal of Parallel and Distributed Computing, Vol. 6, No. 2, pp. 90-114. ISSN 0743-7315.


## Forum Posts


* [QMW computer chess](http://groups.google.com/group/rec.games.chess/browse_frm/thread/51267e26536fa912) by [Don Beal](Don_Beal "Don Beal"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 19, 1993 » [UPCCC 1993](UPCCC_1993 "UPCCC 1993")


## External Links


### Chess Program


* [Phoenix' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=191)
* [Computer Chess and Canada](http://web.archive.org/web/20091026180259/http://geocities.com/rookknightrook/ChessArticlesDavidCohen.htm#A0507) by [David Cohen](http://web.archive.org/web/20091026180259/http://geocities.com/rookknightrook/ChessArticlesDavidCohen.htm), 2005


### Phoenix Chess Systems


* [Phoenix Chess Systems](http://www.schach-computer.info/wiki/index.php/Phoenix_Chess_Systems) from [schach-computer.info](http://www.schach-computer.info/wiki/index.php/Hauptseite_En)
* [Welcome to Phoenix Chess Systems](http://www.phoenixcs.nl/) by [Ruud Martin](Ruud_Martin "Ruud Martin")


### Phoenix elsewhere


* [Phoenix (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Phoenix_%28mythology%29)
* [Phoenix (demonology) from Wikipedia](https://en.wikipedia.org/wiki/Phenex)
* [phoenix: a world of chess](http://www.scphoenix.ch/infos/wirueberuns.php), Zurich Chess Club (German)
* [Phoenix (band) from Wikipedia](https://en.wikipedia.org/wiki/Phoenix_%28band%29)
* [Hans Koller Free Sound](http://www.discogs.com/artist/1063310-Hans-Koller-Free-Sound) - Nicolas 1-2, [Phoenix](http://www.discogs.com/Hans-Koller-Free-Sound-Phoenix/master/359810), 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 line-up: [Adelhard Roidinger](https://de.wikipedia.org/wiki/Adelhard_Roidinger), [Albert Mair](https://de.wikipedia.org/wiki/Albert_Mair), [Alex Bally](https://de.wikipedia.org/wiki/Alex_Bally), [Hans Koller](Category:Hans_Koller "Category:Hans Koller"), [Jürgen Wuchner](http://de.wikipedia.org/wiki/J%C3%BCrgen_Wuchner)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Phoenix (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Phoenix_%28mythology%29)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997, 2009**). *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*. 1. This Was Going to Be Easy, pp. 8
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1987**). *Speculative Computing*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997, 2009**). *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*. 1. This Was Going to Be Easy, pp. 8
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Hash tables - Clash!!! What happens next?](http://groups.google.de/group/rec.games.chess/browse_thread/thread/87d436c2293f9138) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), post 6 by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), March 17, 1994
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997, 2009**). *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*. 1. This Was Going to Be Easy, pp. 9
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](http://www.computerhistory.org/chess/full_record.php?iid=doc-434fea055cbb3) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1989_WCCC/1989%20WCCC.062302028.sm.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Phoenix's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=191)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Cologne 1986 - Chess - Round 3 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=62&round=3&id=6)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> Photo by [Monty Newborn](Monroe_Newborn "Monroe Newborn"), [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), pp. 184

**[Up one level](Engines "Engines")**







 
