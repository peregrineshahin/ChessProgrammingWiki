---
title: Master
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Master**



[ Old Master <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Master**,  

a mainframe chess program of the 70s, developed by British scientists from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory") in [Chilton, Oxfordshire](https://en.wikipedia.org/wiki/Chilton,_Oxfordshire) and [Harwell Atomic Energy Research Establishment](https://en.wikipedia.org/wiki/Atomic_Energy_Research_Establishment). When [Alex Bell](Alex_Bell "Alex Bell") left Atlas Laboratory in 1969, his fellow [Peter Kent](Peter_Kent "Peter Kent") took over his chess program [Atlas](Atlas "Atlas"), which was a reproduction of [Nils Barricelli's](Nils_Barricelli "Nils Barricelli") program in [Algol](Algol "Algol"). With the help of [John Birmingham](John_Birmingham "John Birmingham") the program was rewritten to [PL/I](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)"), and in 1973, Alex Bell, back in Chilton, joined the team to develop the chess playing program **M**inimax **a**lgorithm Te**ster**, Master. In 1974, for the upcoming [WCCC 1974](WCCC_1974 "WCCC 1974") in [Stocholm](https://en.wikipedia.org/wiki/Stockholm), chess tutor [John Waldron](John_Waldron "John Waldron") was recruited to implement chess knowledge and [opening book](Opening_Book "Opening Book"). When Alex Bell left Chilton a second time in 1975, Master was further improved by Peter Kent and John Birmingham as sole authors <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### Contents


* [1 Photos](#photos)
* [2 Description](#description)
	+ [2.1 Full Width Search](#full-width-search)
	+ [2.2 SOMA](#soma)
	+ [2.3 Feed-Over](#feed-over)
* [3 Tournament Play](#tournament-play)
	+ [3.1 Master at IFIPS](#master-at-ifips)
	+ [3.2 Selected Games](#selected-games)
		- [3.2.1 WCCC 1974](#wccc-1974)
		- [3.2.2 WCCC 1977](#wccc-1977)
		- [3.2.3 WCCC 1980](#wccc-1980)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 External Links](#external-links)
	+ [6.1 Chess Program](#chess-program)
	+ [6.2 Misc](#misc)
* [7 References](#references)






 [](http://www.chilton-computing.org.uk/gallery/ral/slide28.htm) 
Chess on the [360/195](IBM_360 "IBM 360"). [Alex Bell](Alex_Bell "Alex Bell"), Geoff Lambert, [Peter Kent](Peter_Kent "Peter Kent"), [John Birmingham](John_Birmingham "John Birmingham") and [John Waldron](John_Waldron "John Waldron") <a id="cite-note-3" href="#cite-ref-3">[3]</a>



## Description


### Full Width Search


Master was a [Shannon](Claude_Shannon "Claude Shannon") [Type A](Type_A_Strategy "Type A Strategy") program with [progressive deepening](Iterative_Deepening "Iterative Deepening"), examining the full width of moves, subject only to pruning by the various algorithms, that is [Alpha-Beta](Alpha-Beta "Alpha-Beta") , (deep) [razoring](Razoring "Razoring") and [marginal forward pruning](Pruning "Pruning"). The [Killer heuristic](Killer_Heuristic "Killer Heuristic") and static [evaluation](Evaluation "Evaluation") (in the upper part of the [tree](Search_Tree "Search Tree")) was used in [move ordering](Move_Ordering "Move Ordering"). 



### SOMA


Similar to [SOMA](SOMA "SOMA"), Master had no [quiescence search](Quiescence_Search "Quiescence Search"), but an attempt to compute a [static evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") for non-quiescent positions, archived by giving values for threats to pieces as well as [captures](Captures "Captures"), considering [pins](Pin "Pin") and [x-rays](X-ray "X-ray"), [control to center squares](Center_Control "Center Control") and [squares near the king](King_Safety#SquareControl "King Safety"). The value of threats by the player to move is greater than that of the player who has just moved, producing an element of [tempo](Tempo "Tempo") in the evaluation function. Apparently later version of Master used [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance"), that is were able to detect various mates without further search. 



### Feed-Over


A so called **Feed-Over Technique** was applied, which saved the most important parts of the [tree](Search_Tree "Search Tree") in a kind of [refutation table](Refutation_Table "Refutation Table"), also reused after a move has been selected from the [root](Root "Root") for initial move ordering.



## Tournament Play


Master competed at the first three [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 1974](WCCC_1974 "WCCC 1974") in [Stocholm](https://en.wikipedia.org/wiki/Stockholm), the [WCCC 1977](WCCC_1977 "WCCC 1977") in [Toronto](https://en.wikipedia.org/wiki/Toronto) and the [WCCC 1980](WCCC_1980 "WCCC 1980") in [Linz](https://en.wikipedia.org/wiki/Linz). Master won the two [European Computer Chess Championships](European_Computer_Chess_Championship "European Computer Chess Championship"), the [ECCC 1976](ECCC_1976 "ECCC 1976") in [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), and the [ECCC 1979](ECCC_1979 "ECCC 1979") in [London](https://en.wikipedia.org/wiki/London).



### Master at IFIPS


[Alex Bell](Alex_Bell "Alex Bell") describes the development of Master, and the tournament experience - excerpt <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```
The [first Computer Chess Conference](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1") took place at the [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory") in May 1973. Apart from inviting the speakers it was also obvious that the conference would have to demonstrate a chess program in some form and it is at this point in time that MASTER really got started.

```


```
One of the programmers at Atlas, [Peter Kent](Peter_Kent "Peter Kent"), had taken over the program and modified it to maximise the number of squares controlled. This, combined with a few other improvements, had produced a much stronger program - as Peter later wrote.

```


```
At this point a very energetic programmer from [Harwell Atomic Energy Research Establishment](https://en.wikipedia.org/wiki/Atomic_Energy_Research_Establishment), [John Birmingham](John_Birmingham "John Birmingham"), became interested. He translated the program, plus all the new improvements, into [PL/I](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") in about 6 weeks of his spare time and also extended the depth of the search. I would say at this point that England at last had a program comparable to [MACHACK](Mac_Hack "Mac Hack") and we ambitiously christened it MASTER-Minimax Algorithm teSTER; if nothing else we had the patent on a good name.

```


```
In March 1974 [David Levy](David_Levy "David Levy"), the regular referee and one of the organisers of the [American ACM tournaments](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), rang me up - did I know of any good English chess programs? And, if so, would they like to enter the first [IFIPS](IFIP "IFIP") World Computer Chess Championship which would take place at Stockholm in August? So MASTER was entered, and for the first time we - John, Peter and myself - stopped developing the program sporadically ad hoc and seriously thought about how to improve it. One big problem was that none of us was (or is) a good chess player and by then the program was beginning to beat us occasionally.

```


```
So a fourth member of the team was recruited - [John Waldron](John_Waldron "John Waldron"), a sound county level player. From this point MASTER slowly began to copy Waldron's style and, with the program now searching 6 plies deep plus a crude form of a new technique (feedover), it took part in the [IFIP](IFIP "IFIP") [first World Championship](WCCC_1974 "WCCC 1974") in Stockholm, winning 2, losing 2 and coming about 5th out of 13 programs using 2 hours of time of the Rutherford's [360/195](IBM_360 "IBM 360").

```


```
On the last night, having won two easy games, MASTER again met a tough opponent, [RIBBIT](Ribbit "Ribbit") from Canada. At one point in this game Peter Kent, who was in Stockholm, told us that if MASTER won then there was a chance that it could play off for the championship but, unfortunately, [TECH 2](Tech "Tech") had been a costly game in sabbatical time and MASTER was set to play very quickly, missed its chances and gave away a piece. The position at move 54 was (Fig. 10) and Peter Kent asked me if MASTER was saying it wanted to resign.

```



|  |
| --- |
|                                                                                                                    ♗                ♔ ♘   ♙        ♚        |



```
8/8/8/B7/8/1K1N3P/8/k7 w - - 1 54

During the tournament we had not been linked directly to Peter Kent in Stockholm but had been relaying our moves algebraically through London where another chess program was also competing in the tournament. This relay had caused us to use a voice code for the moves (ABLE, BAKER, CHARLIE, DOG, EASY, FOX, GEORGE, HOTEL) and, oddly enough, we never sent or received a bad move. 

```

### Selected Games


### WCCC 1974


[WCCC 1974](WCCC_1974 "WCCC 1974"), round 3, Master - [Tell](Tell "Tell") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "WCCC 1974"]
[Site "Stockholm, Sweden"]
[Date "1974.08.07"]
[Round "3"]
[White "Master"]
[Black "Tell"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 d6 5.d4 exd4 6.cxd4 Bb4+ 7.Kf1 h5 8.Qb3 Bg4 
9.Bxf7+ Kf8 10.Bxg8 Rxg8 11.Qd5 Bxf3 12.gxf3 Rh8 13.Nc3 Bxc3 14.bxc3 a5 15.Rb1 
Qc8 16.Bf4 Qh3+ 17.Ke2 Nd8 18.Bxd6+ cxd6 19.Qxd6+ Kf7 20.Rhg1 Rg8 21.Rb5 g6 
22.Qc7+ Ke8 23.Re5+ Ne6 24.Qxb7 Rd8 25.Rg3 Qxh2 26.Rxe6+ Kf8 27.Qe7# 1-0 

```

[WCCC 1974](WCCC_1974 "WCCC 1974"), round 4, [Ribbit](Ribbit "Ribbit") - Master <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```

[Event "WCCC 1974"]
[Site "Stockholm, Sweden"]
[Date "1974.08.08"]
[Round "4"]
[White "Ribbit"]
[Black "Master"]
[Result "1-0"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nc6 5.dxc5 Qxd1+ 6.Kxd1 Bg4+ 7.Be2 O-O-O+ 
8.Bd2 Nf6 9.Bxg4+ Nxg4 10.Ke2 e6 11.b4 Be7 12.Nf3 f5 13.Na3 Rd5 14.h3 Nge5 
15.Nxe5 Nxe5 16.Be3 Rhd8 17.Rad1 a6 18.Rxd5 Rxd5 19.Re1 Kd7 20.g3 Bf6 21.f4 
b5 22.fxe5 Bxe5 23.Rd1 Rxd1 24.Kxd1 Bxg3 25.c4 bxc4 26.Nxc4 e5 27.Ke2 Ke6 
28.Bd2 e4 29.Ne3 Be5 30.Nc4 Bd4 31.c6 g5 32.Bxg5 Bc3 33.c7 Kd7 34.Nb6+ Kxc7 
35.Nd5+ Kb7 36.Nxc3 Kc7 37.Nd5+ Kc6 38.Ne3 Kb5 39.Nxf5 Kxb4 40.Ke3 Ka3 41.Kxe4
Kxa2 42.Kd3 Kb3 43.Bd2 Ka3 44.Kc4 Ka2 45.Bc3 h5 46.Ng7 h4 47.Nf5 Ka3 48.Nxh4 
Ka2 49.Ng6 Kb1 50.Kb3 Kc1 51.Nf4 Kb1 52.Nd3 a5 53.Bxa5 Ka1 54.h4 Kb1 55.h5 Ka1 
56.h6 Kb1 57.h7 Ka1 58.h8=Q+ Kb1 59.Qb2# 1-0 

```

### WCCC 1977


[WCCC 1977](WCCC_1977 "WCCC 1977"), round 2, Master - [Chess 4.6](Chess_(Program) "Chess (Program)") <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "WCCC 1977"]
[Site "Toronto, Canada"]
[Date "1977.08.07"]
[Round "2"]
[White "Master"]
[Black "Chess 4.6"]
[Result "0-1"]

1.Nf3 d5 2.c4 dxc4 3.Na3 e6 4.Qa4+ Bd7 5.Qxc4 Nc6 6.e3 Nf6 7.Bd3 a6 8.Nc2 b5 
9.Qf4 Bd6 10.Qg5 O-O 11.O-O e5 12.Qh4 Qe7 13.Be4 Nxe4 14.Qxe4 Kh8 15.g4 Na5 
16.g5 Bc6 17.Qg4 Bxf3 18.Qxf3 Qxg5+ 19.Qg2 Qxg2+ 20.Kxg2 e4 21.f3 exf3+ 22.Rxf3 
f5 23.b3 Nc6 24.Bb2 Ne5 25.Bxe5 Bxe5 26.Raf1 g6 27.h3 c5 28.d4 cxd4 29.exd4 Bd6
30.Ne3 Rfe8 31.R1f2 Rad8 32.Rd2 Bb4 33.Rd3 Bf8 34.d5 Re5 35.a4 bxa4 36.bxa4 Bc5
37.d6 Bxd6 38.Nc4 Re6 39.Nxd6 Rexd6 40.Rxd6 Rxd6 41.Rc3 Rd4 0-1 

```

### WCCC 1980


[WCCC 1980](WCCC_1980 "WCCC 1980"), round 3, [Bebe](Bebe "Bebe") - Master <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```

[Event "WCCC 1980"]
[Site "Linz, Austria"]
[Date "1980.09.27"]
[Round "3"]
[White "Bebe"]
[Black "Master"]
[Result "1/2-1/2"]

1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 c5 6.dxc5 Qa5 7.Bb5+ Bd7 8.Qd3 Nxe4
9.Qxe4 Bxb5 10.Qxb7 Bxc3+ 11.bxc3 Bc6 12.Qc8+ Qd8 13.Qxd8+ Kxd8 14.Ba3 Nd7 
15.cxd6 exd6 16.O-O-O Bxf3 17.gxf3 Re8 18.Rxd6 Re6 19.Rd5 Ke8 20.f5 Re2 
21.fxg6 hxg6 22.Bb4 Rc8 23.Rhd1 Nb6 24.R5d2 Rxd2 25.Rxd2 Nc4 26.Re2+ Kd8 
27.f4 a5 28.Bf8 Rc7 29.h3 Kc8 30.h4 Kb7 31.Re8 Kc6 32.a4 Kb7 33.Be7 Rc6 
34.Bd8 f5 35.Rf8 Rd6 36.Kb1 Kc6 37.Ka2 Kd7 38.Kb3 Nd2+ 39.Ka2 Nc4 40.Kb3 
Nd2+ 41.Ka2 Nc4 1/2-1/2 

```

## See also


* [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [Atlas](Atlas "Atlas")


## Publications


<a id="cite-note-9" href="#cite-ref-9">[9]</a>



* [John Birmingham](John_Birmingham "John Birmingham"), [Peter Kent](Peter_Kent "Peter Kent") (**1977**). *Tree-searching and tree-pruning techniques*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess*. Pergamon Press, ISBN-13: 978-0080212227, from [amazon](http://www.amazon.com/Machine-Plays-Chess-Pergamon/dp/0080212220)
* Editor (**1978**). *Toronto Tally*. [Personal Computing, Vol. 2, No. 9](Personal_Computing#2_9 "Personal Computing"), pp. 82 » [WCCC 1977](WCCC_1977 "WCCC 1977")
* [John Birmingham](John_Birmingham "John Birmingham"), [Peter Kent](Peter_Kent "Peter Kent") (**1980**). *Mate at a Glance.* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Peter Kent](Peter_Kent "Peter Kent") (**1980**). *The MASTER Chess Program*. [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")


## External Links


### Chess Program


* [Master's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=46)
* [MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm) from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory), excerpt from [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess*. Pergamon Press, ISBN-13: 978-0080212227, from [amazon](http://www.amazon.com/Machine-Plays-Chess-Pergamon/dp/0080212220)


### Misc


* [Master - Wiktionary](https://en.wiktionary.org/wiki/Master)
* [master - Wiktionary](https://en.wiktionary.org/wiki/master)
* [Master (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Master)
* [Master of Arts from Wikipedia](https://en.wikipedia.org/wiki/Master_of_Arts)
* [Master of Science from Wikipedia](https://en.wikipedia.org/wiki/Master_of_Science)
* [Master's degree from Wikipedia](https://en.wikipedia.org/wiki/Master%27s_degree)
* [Master craftsman from Wikipedia](https://en.wikipedia.org/wiki/Master_craftsman)
* [The Master (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/The_Master)
* [Grandmaster (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Grandmaster)
* [Chess master from Wikipedia](https://en.wikipedia.org/wiki/Chess_master)
* [Old Master from Wikipedia](https://en.wikipedia.org/wiki/Old_Master)
* [Maestro from Wikipedia](https://en.wikipedia.org/wiki/Maestro)
* [Masterpiece from Wikipedia](https://en.wikipedia.org/wiki/Masterpiece)
* [Masterpiece (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Masterpiece_%28disambiguation%29)
* [Gong](Category:Gong "Category:Gong") - [Master Builder](https://en.wikipedia.org/wiki/You_%28Gong_album%29), [Manchester Academy](https://en.wikipedia.org/wiki/Manchester_Academy), September 10, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Self-portrait](https://en.wikipedia.org/wiki/Self-portrait) by [Rembrandt](Category:Rembrandt "Category:Rembrandt") in a cap, with eyes wide open, etching and burin, 1630, [Rijksmuseum](https://en.wikipedia.org/wiki/Rijksmuseum), [Rembrandt from Wikipedia](https://en.wikipedia.org/wiki/Rembrandt)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Master's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=46)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Slide 28: 23.08.74 to 01.11.74](http://www.chilton-computing.org.uk/gallery/ral/slide28.htm) from [Rutherford's](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory) Photographic Section for the [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *[MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm)*. from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory), excerpt from [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess*. Pergamon Press
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Stockholm 1974 - Chess - Round 3 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=7&round=3&id=1)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Stockholm 1974 - Chess - Round 4 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=7&round=4&id=2)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Toronto 1977 - Chess - Round 2 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=18&round=2&id=2)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Linz 1980 - Chess - Round 3 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=68&round=3&id=1)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")

**[Up one level](Engines "Engines")**







 
