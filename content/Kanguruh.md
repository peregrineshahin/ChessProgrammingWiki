---
title: Kanguruh
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Kanguruh**



[ [Pademelon](https://en.wikipedia.org/wiki/Pademelon) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Kanguruh**,  

a 32-bit [WinBoard](WinBoard "WinBoard") compliant chess engine by [Thomas McBurney](Thomas_McBurney "Thomas McBurney"), written in [PowerBASIC](Basic#PowerBASIC "Basic"). 
Kanguruh was an experimental project combining features of Thomas' first chess program [Deep BASIC](Deep_BASIC "Deep BASIC") with the Quick BASIC chess program [Minimax](Minimax_(program) "Minimax (program)") written by [Dieter Steinwender](Dieter_Steinwender "Dieter Steinwender") and [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"). 
Features added were an [opening book](Opening_Book "Opening Book") system, [book learning](Book_Learning "Book Learning"), [evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table"), [pondering](Pondering "Pondering"), better [time management](Time_Management "Time Management"), and a better [evaluation function](Evaluation "Evaluation"). 
Kanguruh played four [Australasian National Computer Chess Championships](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship"). 



### Contents


* [1 Descriptions](#descriptions)
	+ [1.1 2003](#2003)
	+ [1.2 2004](#2004)
	+ [1.3 2005](#2005)
	+ [1.4 2006](#2006)
* [2 Selected Games](#selected-games)
* [3 See also](#see-also)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc)
		- [4.2.1 Macropodidae](#macropodidae)
		- [4.2.2 Court](#court)
* [5 References](#references)






### 2003


[NC3 2003](NC3_2003 "NC3 2003") <a id="cite-note-2" href="#cite-ref-2">[2]</a>




```C++
Kanguruh is an amateur [Winboard](WinBoard "WinBoard") chess engine written in [Power BASIC](Basic "Basic") 3.02 Console Compiler.  Kanguruh was started in March 2003 and it's features include 67,000 move [opening book](Opening_Book "Opening Book") database, [hash table](Transposition_Table "Transposition Table") (Using 64-bit [Zobrist keys](Zobrist_Hashing "Zobrist Hashing")), offset [move generation](Move_Generation "Move Generation"), [killer move table](Killer_Heuristic "Killer Heuristic") and [quiescence search](Quiescence_Search "Quiescence Search"). 

```

### 2004


[NC3 2004](NC3_2004 "NC3 2004") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++
6,258 lines of code, offset pseudo move generator, [iterative deepening](Iterative_Deepening "Iterative Deepening"), [aspiration windows](Aspiration_Windows "Aspiration Windows"), killer move table, evaluation cache, 370,000 move opening book database, [book learning](Book_Learning "Book Learning") and [pondering](Pondering "Pondering"). Program Achievements: Highest rated chess engine written in BASIC at [WBEC](WBEC "WBEC"). Kanguruh is approximately 150 Elo points stronger than last year. 

```

### 2005


[NC3 2005](NC3_2005 "NC3 2005") <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```C++
Kanguruh is a Winboard chess engine written in PowerBASIC 3.04 Console Compiler. Kanguruh uses standard search techniques such as [alpha beta](Alpha-Beta "Alpha-Beta") with aspiration windows, iterative deepening, killer move table, offset move generator and evaluation cache.  Kanguruh features a 670,000 move opening book database and also has a type of book learning feature where it stores separate statistics on each opponent it plays.

```


```C++
Kanguruh has changed little since NC3 2004. The biggest change is to the opening book system, it has been rewritten and redesigned in an attempt to improve the performance of Kanguruh's opening moves. A pondering bug has also been fixed which should improve [time management](Time_Management "Time Management") a little. 

```

### 2006


[NC3 2006](NC3_2006 "NC3 2006") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++
Kanguruh is a Winboard compatible chess engine written in PowerBASIC 3.02 Console Compiler and contains approximately 6000 lines of code. Kanguruh features a set of integrated algorithms which I have named the 'Special Heuristically Intelligent Transposition Engine' (S.H.I.T.E.), it is these set of algorithms that is mostly responsible for Kanguruh's style and performance of play. Although Kanguruh is a relatively weak engine, it is the highest rated engine written in BASIC on WBEC. 

```

## Selected Games


[NC3 2003](NC3_2003 "NC3 2003"), round 3, [Decapod](SEE "SEE") - Kanguruh <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```

[Event "NC3 2003"]
[Site "RedHill, Canberra, Australia"]
[Date "2003.07.22"]
[Round "3"]
[White "Decapod"]
[Black "Kanguruh"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.Bb5+ c6 4.Bd3 dxe4 5.Bxe4 Nf6 6.Qd3 Nxe4 7.Qxe4 Bb4+ 8.c3 Be7 9.Nf3 O-O 
10.O-O Nd7 11.c4 Nf6 12.Qe3 b6 13.Nc3 c5 14.dxc5 Bxc5 15.Qg5 Bb7 16.Rd1 Qe7 17.Ne5 Rad8 
18.Be3 Bxe3 19.Qxe3 Nh5 20.b3 Rxd1+ 21.Rxd1 Rd8 22.Rxd8+ Qxd8 23.b4 Qh4 24.Nb5 Qd8 25.Nd4 
f6 26.Nd3 e5 27.Ne2 e4 28.Ne1 f5 29.Nd4 f4 30.Qc3 Qf6 31.c5 Kf8 32.Qc4 Qe5 33.cxb6 axb6 
34.Ne6+ Ke8 35.Nc2 Ke7 36.Ncd4 e3 37.fxe3 fxe3 38.Qc3 Kd7 39.Nf8+ Ke8 40.Nxh7 e2 41.Kf2 Nf4 
42.Nxe2 Qxe2+ 43.Kg3 Ng6 44.Qf3 Bxf3 45.gxf3 Qe1+ 46.Kg4 Qh4+ 47.Kf5 Ne7+ 48.Ke5 Qxh7 49.a4 
Qxh2+ 50.Ke4 Qc2+ 51.Kf4 Qxa4 52.Kg4 Qxb4+ 53.Kg3 Nf5+ 54.Kg2 Ne3+ 0-1

```

## See also


* [Deep BASIC](Deep_BASIC "Deep BASIC")
* [Minimax](Minimax_(program) "Minimax (program)")


## External Links


### Chess Engine


* [Kanguruh Home Page](https://web.archive.org/web/20180222155226/http://home.pacific.net.au:80/~tommyinoz/kanguruh.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Kanguruh](https://web.archive.org/web/20140418005106/http://wbec-ridderkerk.nl/html/details1/Kanguruh.html) from [WBEC Ridderkerk](WBEC "WBEC") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Kanguruh 1.93](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Kanguruh%201.93) in [CCRL Blitz](CCRL "CCRL")
* [Kanguruh 1.93](http://kirr.homeunix.org/chess/kcec/cgi/engine_details.cgi?match_length=20&print=Details&each_game=0&eng=Kanguruh%201.93) in [KCEC](KCEC "KCEC")
* [NC3 - 2003 Australian National Computer Chess Championship](https://web.archive.org/web/20180713121916/http://home.pacific.net.au/~tommyinoz/nc3.html) by [Thomas McBurney](Thomas_McBurney "Thomas McBurney") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))


### Misc


* [Kangaroo (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Kangaroo_%28disambiguation%29)
* [Guru Guru](Category:Guru_Guru "Category:Guru Guru") - [Känguru](https://www.discogs.com/de/Guru-Guru-K%C3%A4nguru/release/760659) (1972), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 lineup: [Uli Trepte](https://en.wikipedia.org/wiki/Uli_Trepte), [Mani Neumeier](https://en.wikipedia.org/wiki/Mani_Neumeier), [Ax Genrich](http://de.wikipedia.org/wiki/Ax_Genrich)
 
### Macropodidae


* [Macropodidae from Wikipedia](https://en.wikipedia.org/wiki/Macropodidae)
* [Känguruh - Wiktionary](http://en.wiktionary.org/wiki/K%C3%A4nguruh)
* [Känguru - Wiktionary](http://en.wiktionary.org/wiki/K%C3%A4nguru#German)
* [kangaroo - Wiktionary](http://en.wiktionary.org/wiki/kangaroo)
* [Kangaroo from Wikipedia](https://en.wikipedia.org/wiki/Kangaroo)


### Court


* [kangaroo court - Wiktionary](http://en.wiktionary.org/wiki/kangaroo_court)
* [Kangaroo court from Wikipedia](https://en.wikipedia.org/wiki/Kangaroo_court)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A close-up of a pademelon eating a slice of [sweet potato](https://en.wikipedia.org/wiki/Sweet_potato) near [Port Douglas, Queensland](https://en.wikipedia.org/wiki/Port_Douglas,_Queensland) in December 2005, by [PanBK](https://en.wikipedia.org/wiki/User:PanBK), [Pademelon from Wikipedia](https://en.wikipedia.org/wiki/Pademelon)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [NC3 2003 - List of Entries](http://users.cecs.anu.edu.au/%7Eshaun/chess/NC3_-_List_of_Entries.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [NC3 2004 - List of Entries](http://users.cecs.anu.edu.au/%7Eshaun/chess/NC32004_-_List_of_Entries.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [NC3 2005 - List of Entries](http://users.cecs.anu.edu.au/%7Eshaun/chess/NC32005_-_List_of_Entries.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [NC3 2006 - List of Entries](http://users.cecs.anu.edu.au/%7Eshaun/chess/NC32006_-_List_of_Entries.html)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [NC3 - 2003 Australian National Computer Chess Championship](https://web.archive.org/web/20180713121916/http://home.pacific.net.au/~tommyinoz/nc3.html) by [Thomas McBurney](Thomas_McBurney "Thomas McBurney") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

**[Up one Level](Engines "Engines")**







 
