---
title: Awit
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Awit (Wita)**

\[ [Anglo-Saxon king with his Witan](https://en.wikipedia.org/wiki/Witenagemot) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Awit**,

a chess program written by [Tony Marsland](Tony_Marsland "Tony Marsland"). The original program, which played in the first [ACM 1970](ACM_1970 "ACM 1970") in [New York](https://en.wikipedia.org/wiki/New_York_City) was called **Wita**. The name was derived from [Witan](https://en.wikipedia.org/wiki/Witenagemot), which was for a *meeting of wise men*. The inspiration for Wita came from the *1966 Fall Joint Computer Conference* <a id="cite-note-2" href="#cite-ref-2">[2]</a> in [San Francisco](https://en.wikipedia.org/wiki/San_Francisco) and had been impressed by [Richard Greenblatt's](Richard_Greenblatt "Richard Greenblatt") talk about [Mac Hack](Mac_Hack "Mac Hack").

In about 1977, the name was changed to Awit for two reasons. First, to put the program nearer the top of an alphabetical list and second (more importantly) to reflect the program's propensity to play subtle moves that were rife with fatal flaws. Awit-Wita was written in [Algol W](Algol "Algol") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and ran on [IBM 370](IBM_370 "IBM 370") under the [Michigan Terminal System](https://en.wikipedia.org/wiki/Michigan_Terminal_System) (MTS) <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Awit is a selective [Shannon type B searcher](Type_B_Strategy "Type B Strategy") with a lot of chess [knowledge](Knowledge "Knowledge") implemented, and therefor with 8 [Nodes per second](Nodes_per_Second "Nodes per Second") <a id="cite-note-5" href="#cite-ref-5">[5]</a> extremely slow with an impressive [strength](Playing_Strength "Playing Strength") / [nodes](Node "Node")-evaluated ratio, despite its inherent tactical flaws up and then.

## Quotes

Quote from the [ACM 1980](ACM_1980 "ACM 1980") booklet <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```C++
Awit is one of the few programs that carries out extensive [forward pruning](Pruning "Pruning"). During the course of the three minute move, Awit examines about 200 [nodes](Node "Node")! This might be contrasted with the 30,000,000 - 40,000,000 nodes examined by [Belle](Belle "Belle"). Awit is written in [Algol W](Algol "Algol"). A moderately large book of 10,000 lines is used. 

```

## Achievements

Awit's greatest tournament success was the shared second place at the [WCCC 1983](WCCC_1983 "WCCC 1983") in [New York](https://en.wikipedia.org/wiki/New_York_City), while almost the same program played its last tournament at [WCCC 1986](WCCC_1986 "WCCC 1986") in [Cologne](https://en.wikipedia.org/wiki/Cologne) only to serve as a benchmark for other programs <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Photos & Games

## BS6676

A real cliffhanger between Wita and [Bs6676](Bs6676 "Bs6676") from [WCCC 1977](WCCC_1977 "WCCC 1977"), [Albin Countergambit](https://en.wikipedia.org/wiki/Albin_Countergambit) <a id="cite-note-8" href="#cite-ref-8">[8]</a> :

```
[Event "2nd World Computer Chess Championship"]
[Site "Toronto, Canada"]
[Date "1977.08.08"]
[Round "3"]
[White "Wita"]
[Black "Bs6676"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 e5 3.dxe5 d4 4.e4 f5 5.Bd3 Nc6 6.Nf3 Bb4+ 7.Ke2 fxe4 
8.Bxe4 Bg4 9.Qa4 d3+ 10.Kf1 Qd7 11.Bxc6 Qxc6 12.Qxb4 Bxf3 13.gxf3
Qxf3 14.Rg1 d2 15.Bxd2 Qd1+ 16.Be1 Qd3+ 17.Kg2 Qg6+ 18.Kh1 Qe4+ 
19.Rg2 a5 20.Qc3 Qf5 21.Rxg7 O-O-O 22.Qxa5 Qe4+ 23.f3 Qxf3+ 24.Kg1 
Qe3+ 25.Kh1 Qe4+ 26.Kg1 Qe3+ 27.Kh1 Qf3+ 28.Kg1 Qe3+ 1/2-1/2

```

## Ostrich

[](http://archive.computerhistory.org/resources/still-image/Chess_temporary/still-image/)
[ACM 1979](ACM_1979 "ACM 1979"), Round 4, [Monroe Newborn](Monroe_Newborn "Monroe Newborn") standing, [Tony Marsland](Tony_Marsland "Tony Marsland"), [Ostrich 80](Ostrich "Ostrich") - Awit <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```
[Event "10th North Am.CC (ACM)"]
[Site "Detroit USA"]
[Date "1979.10.30"]
[Round "4"]
[White "Ostrich 80"]
[Black "Awit"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.Bb5+ Nc6 4.O-O Bd7 5.Nc3 Nf6 6.d4 a6 7.Bxc6 Bxc6 8.Be3 Qb6
9.b3 Nxe4 10.Nxe4 Bxe4 11.c3 Qc6 12.Qe2 O-O-O 13.Ng5 Bg6 14.Nf3 Bh5 15.Bg5 Kd7
16.Rad1 Bxf3 17.gxf3 cxd4 18.cxd4 Qd5 19.f4 h6 20.Bh4 g5 21.fxg5 hxg5 22.Bg3 Rc8
23.Rd3 Bg7 24.Rfd1 e6 25.Qe3 b5 26.f4 f6 27.fxg5 Rc2 28.R1d2 Rc1+ 29.Be1 Qxg5+
30.Qxg5 fxg5 31.Re3 Ke7 32.Kg2 g4 33.Ree2 Bf6 34.Bg3 Bg5 35.Rd3 d5 36.a4 bxa4
37.bxa4 Ra1 38.Be5 Rg8 39.Kg3 Bh6 40.Kh4 Rxa4 41.Rg2 a5 42.Rxg4 Rf8 43.Kh5 Bc1
44.Rg7+ Rf7 45.Bd6+ Kxd6 46.Rxf7 Rc4 47.Kg6 Rc2 48.h4 a4 49.Rff3 a3 50.Rb3 a2
51.Rb6+ Kc7 52.Ra6 Kb7 53.Ra4 Kb6 54.Rf6 Kb5 55.Ra8 Be3 56.Rxe6 Bxd4 57.Rb8+ Ka5
58.Ra8+ Kb5 59.Rb8+ Kc4 60.Rc6+ Kd3 61.Rb3+ Bc3 62.Ra6 Rg2+ 63.Kh5 Kc4 64.Rba3 
a1=Q 65.R6a4+ Kd3 66.Rxa1 Bxa1 67.Rxa1 Rg8 68.Rd1+ Ke4 69.Re1+ Kf5 70.Rf1+ Ke4 
71.Re1+ Kf4 72.Rd1 Ke5 73.Re1+ Kd6 74.Rd1 Ke5 75.Re1+ Kd6 76.Rd1 Ke5 1/2-1/2

```

## Phoenix

[WCCC 1983](WCCC_1983 "WCCC 1983"), round 5, [Phoenix](Phoenix "Phoenix") - Awit <a id="cite-note-10" href="#cite-ref-10">[10]</a>

```
[Event "WCCC 1983"]
[Site "New York, USA"]
[Date "1983.10.25"]
[Round "5"]
[White "Phoenix"]
[Black "Awit"]
[Result "0-1"]

1.d4 Nf6 2.Bg5 Ne4 3.Bh4 d5 4.f3 Nf6 5.Nd2 g6 6.e4 Nbd7 7.e5 Nh5 8.c4 Bh6
9.cxd5 Nb6 10.g4 Nf4 11.g5 Bg7 12.Ne4 Nbxd5 13.Bg3 h6 14.Qd2 hxg5 15.Nxg5
Nh5 16.N1h3 f6 17.exf6 exf6 18.Ne4 Qe7 19.Qe2 Bxh3 20.Bxh3 Nhf4 21.Nxf6+ 
Bxf6 22.Qxe7+ Kxe7 23.Bf1 Bxd4 24.O-O-O Be3+ 25.Kb1 Rad8 26.Bd3 c6 27.Rhe1 
Kf6 28.Be4 g5 29.Rh1 Rh3 30.Rhe1 Nh5 31.Bxd5 Rxd5 32.Rxd5 cxd5 33.Rxe3 Nxg3
34.hxg3 Rxg3 35.Rb3 g4 36.Rxb7 Rxf3 37.Rxa7 g3 38.Ra6+ Kg5 39.Ra8 Rf1+ 
40.Kc2 Rf2+ 41.Kc3 d4+ 42.Kxd4 Rxb2 43.Kc3 Rb6 44.Rd8 Kf5 45.Rd2 Ke4 46.a4
Rc6+ 47.Kb4 Kf3 48.Rd3+ Kf4 49.Rd4+ Ke3 50.Rg4 Kf2 51.Rf4+ Ke2 52.Rf7 Rc8
53.Re7+ Kf2 54.Rf7+ Kg1 55.a5 Rh8 56.a6 g2 57.a7 Kh2 58.a8=Q 0-1 

```

## See also

- [Sargon vs. Awit](Sargon#Awit "Sargon") at [ACM 1978](ACM_1978 "ACM 1978")

## Source Code

- [Awit source code](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/AlgolwSupport/awit.pdf) (pdf)

## Publications

- [Paul Rushton](Paul_Rushton "Paul Rushton"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1973**). *Current Chess Programs: A Summary of their Potential and Limitations*. INFOR Journal of the Canadian Information Processing Society Vol. 11, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/Rushton-Marsland-Feb73.pdf)
- [Tony Marsland](Tony_Marsland "Tony Marsland") (**1974**). *A users guide to WITA, a chess program*. Technical report, [University of Alberta](University_of_Alberta "University of Alberta") <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Harry Shershow](Harry_Shershow "Harry Shershow") (**1979**). *A Little Bit is a Little Better*. [Personal Computing, Vol. 3, No. 4](Personal_Computing#3_4 "Personal Computing"), pp. 61 » [Sargon - Awit](Sargon#Awit "Sargon")
- [Tony Marsland](Tony_Marsland "Tony Marsland") (**2020**). *Computer loses in king-size blunder*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

## Forum Posts

- [What AWIT(y) chess program. Tony Marsland's, that is....](http://www.talkchess.com/forum/viewtopic.php?t=33305) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), March 17, 2010

## [Windows](Windows "Windows") executable and [C](C "C")-sources by [Jim Ablett](Jim_Ablett "Jim Ablett") [in the same thread](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=337837&t=33305) External Links

## Chess Program

- [Awit's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=410)
- [Awit-Wita Computer Chess Archive](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/)

[A short history of Wita-Awit](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/Awit-Wita-ReadMe/wita-history-readme.txt) by [Tony Marsland](Tony_Marsland "Tony Marsland")

- [Images - Michigan Terminal System Archive - Computer Chess, CHAOS and AWIT](http://archive.michigan-terminal-system.org/images#TOC-13-Photographs:-Computer-Chess-CHAOS-and-AWIT) » [CHAOS](CHAOS "CHAOS")
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-13" href="#cite-ref-13">[13]</a>

## Misc

- [Witenagemot from Wikipedia](https://en.wikipedia.org/wiki/Witenagemot)
- [Awit from Wikipedia](https://en.wikipedia.org/wiki/Awit) (form of [Filipino](https://en.wikipedia.org/wiki/Philippines) poetry)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Witenagemot from Wikipedia](https://en.wikipedia.org/wiki/Witenagemot)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [1966 Fall Joint Computer Conference, November 7-10, San Franciso, California](http://openlibrary.org/b/OL14154396M/1966_Fall_Joint_Computer_Conference_November_7-10_San_Franciso_California.)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Awit source code](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/AlgolwSupport/awit.pdf) (pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Mike Alexander](Mike_Alexander "Mike Alexander") was principal architect of the [Michigan Terminal System](https://en.wikipedia.org/wiki/Michigan_Terminal_System) (MTS)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [The Fifteenth ACM Computer Chess Championship, San Francisco California, October 7-9, 1984](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c9575), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1984_15th_NACCC/1984%20NACCC.062303012.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), covers [WCCC 1983](WCCC_1983 "WCCC 1983")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [The Eleventh ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cdeeb), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1980_11th_ACM_NACCC/The_Eleventh_ACMs_North_American_Computer_Chess_Championship.1980.062303015.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [A short history of Wita-Awit](http://webdocs.cs.ualberta.ca/%7Etony/Public/Awit-Wita-ComputerChess/Awit-Wita-ReadMe/wita-history-readme.txt) by [Tony Marsland](Tony_Marsland "Tony Marsland")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Toronto 1977, Chess, Round 3, Game 7](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=18&round=3&id=7)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Photo](http://archive.computerhistory.org/resources/still-image/Chess_temporary/still-image/) Gift of [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [New York 1983 - Chess - Round 5 - Game 4 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=65&round=5&id=4)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Canadian Chess - Publications (Books, CDs, Videos, Periodicals, Columns)](http://www.canadianchess.info/canadianchesshistory/CanadianChessPublications.html)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> John C. Devlin (**1970**). *[Chess Computer Loses Game in a King‐Size Blunder](https://www.nytimes.com/1970/09/02/archives/chess-computer-loses-game-in-a-kingsize-blunder.html)*. [New York Times](https://en.wikipedia.org/wiki/The_New_York_Times), September 02, 1970
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**

