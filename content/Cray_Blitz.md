---
title: Cray Blitz
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cray Blitz**

[](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cf749) The New Champion, [Chess Life](https://en.wikipedia.org/wiki/Chess_Life), February 1984 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cray Blitz**,

was the successor of the program [Blitz](Blitz "Blitz") by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Albert Gower](Albert_Gower "Albert Gower"). With the sponsorship of [Cray Research](https://en.wikipedia.org/wiki/Cray), supported by [Dave Darling](index.php?title=David_Darling&action=edit&redlink=1 "David Darling (page does not exist)") and [Derek Robb](index.php?title=Derek_Robb&action=edit&redlink=1 "Derek Robb (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and later by Cray Assembly expert [Harry Nelson](Harry_Nelson "Harry Nelson") from the [Lawrence Livermore National Laboratory](Lawrence_Livermore_National_Laboratory "Lawrence Livermore National Laboratory") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, they adopted and optimized Blitz for a [Cray-1](Cray-1 "Cray-1") supercomputer <a id="cite-note-4" href="#cite-ref-4">[4]</a>, later a [Cray X-MP](Cray_X-MP "Cray X-MP"), [Cray Y-MP](Cray_X-MP#YMP "Cray X-MP") and [C916](Cray_X-MP#C90 "Cray X-MP") with up to 16 processors. Cray Blitz initially used root splitting as [parallel search algorithm](Parallel_Search "Parallel Search") on the two processor Cray X-MP, implemented and tested just before the [WCCC 1983](WCCC_1983 "WCCC 1983") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, later [principal variation splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, enhanced principal variation splitting <a id="cite-note-7" href="#cite-ref-7">[7]</a>, and in the 90s [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting") <a id="cite-note-8" href="#cite-ref-8">[8]</a>, specifically designed for a shared memory multiprocessor architecture of the Crays. Cray Blitz was written in [Fortran](Fortran "Fortran"), time-critical parts in the Cray Assembly Language [CAL](Assembly#CAL "Assembly").

Cray Blitz won two times the [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") and also was two times winner of the [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 1983](WCCC_1983 "WCCC 1983") in New York <a id="cite-note-9" href="#cite-ref-9">[9]</a> , and the [WCCC 1986](WCCC_1986 "WCCC 1986") in Cologne <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## Photos & Game

## WCCC 1983

[](File:NelsonHyattBeal1983.JPG)
[Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Don Beal](Don_Beal "Don Beal"), Cray Blitz vs [BCP](BCP "BCP"), [WCCC 1983](WCCC_1983 "WCCC 1983") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

```
[Event "WCCC 1983"]
[Site "New York, USA"]
[Date "1983.10.22"]
[Round "1"]
[White "Cray Blitz"]
[Black "BCP"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nf6 3.e5 Nd5 4.Nc3 e6 5.Nxd5 exd5 6.d4 Nc6 7.dxc5 Bxc5 8.Qxd5 Qb6 
9.Qd2 O-O 10.Bc4 Re8 11.O-O Nxe5 12.Nxe5 Rxe5 13.Qf4 Qf6 14.Qxf6 gxf6 15.Kh1 d5 
16.f4 Rh5 17.Be2 Rh4 18.Bf3 d4 19.g3 Rh3 20.f5 Kg7 21.Kg2 Rh6 22.Bxh6+ Kxh6 
23.Bd5 Kg7 24.Rad1 a5 25.Kh1 Ra6 26.Be4 b5 27.Rfe1 Bd7 28.Rd2 Bc6 29.Bxc6 Rxc6 
30.Re8 Bb6 31.Rb8 b4 32.Rb7 Kf8 33.Re2 Bc7 34.g4 Rc5 35.Ra7 Bb6 36.Ra6 Rc6 
37.Rd2 Rd6 38.Rd3 Kg7 39.c3 Kg8 40.a4 Kg7 41.cxb4 axb4 42.a5 Bc5 43.Rxd6 Bxd6 
44.Rxd4 Bc5 45.Rd5 Be3 46.Rd3 Bc5 47.Rd7 Be3 48.a6 h5 49.gxh5 Kf8 50.Rd3 Bc5 
51.Rg3 Ke8 52.h6 Bd6 53.a7 Ke7 54.Rd3 Bc7 55.a8=Q Bd6 56.h7 b3 57.Qb7+ Ke8 
58.h8=Q+ Bf8 59.Qe4# 1-0

```

## WCCC 1986

[](http://members.home.nl/matador/chess820.htm)
Cray Blitz vs. [HiTech](HiTech "HiTech"), [WCCC 1986](WCCC_1986 "WCCC 1986") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

```
[Event "WCCC 1986"]
[Site "Cologne, Germany"]
[Date "1986.06.15"]
[Round "5"]
[White "Cray Blitz"]
[Black "Hitech"]
[Result "1-0"]

1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.Qe2 a6 7.dxc5 Bxc5 8.O-O b5 
9.Rd1 Qe7 10.Bd3 e5 11.e4 Nc6 12.Nc3 Bg4 13.Be3 Rd8 14.h3 Bxe3 15.Qxe3 Bxf3 
16.Qxf3 Nd4 17.Qg3 O-O 18.a4 b4 19.Nd5 Nxd5 20.exd5 Rxd5 21.Bxa6 b3 22.Qe3 Rfd8 
23.Bc4 Nc2 24.Qe2 Rc5 25.Rxd8+ Qxd8 26.Rb1 Nd4 27.Qf1 Qd7 28.Ra1 Qc6 29.Bb5 Nxb5
30.axb5 Qb7 31.Ra3 g6 32.Rxb3 Qd5 33.Rb4 Rc2 34.b3 Qd2 35.Rc4 Rb2 36.Re4 Qd5 
37.Qc4 Qd1+ 38.Kh2 Rxf2 39.Rxe5 Qd6 40.Qc8+ Kg7 41.Qc5 Qd2 42.Rg5 Re2 43.Rg4 Qa2 
44.Qc3+ Kg8 45.b6 Qa8 46.Qc7 Qf8 47.b7 Re8 48.Rc4 Kg7 49.Rc6 Rb8 50.Qc8 Rxc8 
51.bxc8=Q Qb4 52.Qc7 Qxb3 53.Qe5+ Kh6 54.Qf4+ Kg7 55.Qd4+ Kh6 56.Rb6 Qc2 
57.Qf4+ Kg7 58.Qf6+ Kh6 59.Qxf7 Qc8 60.Rd6 1-0

```

[View this game on Lichess.org](https://lichess.org/8sOvGiHP)

## ACM 1988

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbdea550)
[Nelson](Harry_Nelson "Harry Nelson"), [Hyatt](Robert_Hyatt "Robert Hyatt"), [Weiner](Ossi_Weiner "Ossi Weiner") at the [19th ACM 1988](ACM_1988 "ACM 1988"), Orlando <a id="cite-note-13" href="#cite-ref-13">[13]</a>

```C++
Picture taken around move 19th (after 18.Qa5 and before 20.b3)<a id="cite-note-14" href="#cite-ref-14">[14]</a> 

```

```
[Event "ACM 1988"]
[Site "Orlando USA"]
[Date "1988.11.13"]
[Round "2"]
[White "Mephisto"]
[Black "Cray Blitz"]
[Result "1/2-1/2"]

1.Nf3 d5 2.d4 Bf5 3.c4 e6 4.Qb3 b6 5.Nc3 dxc4 6.Qxc4 Nf6 7.Bg5 Be7 8.e3 Nbd7 9.Qc6 Bb4 
10.Bxf6 gxf6 11.Rc1 a6 12.Be2 Ra7 13.Nh4 Bxc3+ 14.Rxc3 Bb1 15.Qa4 Be4 16.O-O Qb8 17.Rfc1 
b5 18.Qa5 Nb6 19.f3 Bd5 20.b3 Ba8 21.Rc5 f5 22.g3 Nd5 23.e4 fxe4 24.fxe4 Ne7 25.Bf3 O-O 
26.Rg5+ Ng6 27.Rcc5 Rd8 28.Qc3 Qb6 29.Rg4 Rd7 30.Bg2 Bb7 31.Nf3 Ra8 32.Ne5 Rd6 33.Qe3 Kf8 
34.Nf3 Ke8 35.e5 Rd7 36.Ng5 Bxg2 37.Kxg2 h5 38.Re4 Qb7 39.Qf3 Rad8 40.Qf2 Re7 41.Kg1 Red7 
42.Rc1 Re7 43.Rf1 a5 44.Qf6 Qb6 45.Rd1 Qc6 46.Re2 Qc3 47.Nxf7 Rxd4 48.Rf1 Qd3 49.Ref2 h4
50.Rf3 Qc2 51.R1f2 Qc1+ 52.Kg2 hxg3 53.hxg3 Qb1 54.Nh8 Nxh8 55.Qxh8+ Kd7 56.Rf7 Qe4+ 
57.Kh2 Rxf7 58.Rxf7+ Kc6 59.Qe8+ Kb6 60.Qb8+ Qb7 61.Qxb7+ Kxb7 62.Kg2 Rd5 63.g4 Rxe5 
64.Kf3 Re1 65.Rf4 1/2-1/2

```

[View this game on Lichess.org](https://lichess.org/jD77DoCp)

## Quote

by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), September 2008 <a id="cite-note-15" href="#cite-ref-15">[15]</a>:

```C++
It was originally [FORTRAN](Fortran "Fortran") as that was the only choice on the system we had in 1968. I started to convert it to [PL/1](index.php?title=PL_1&action=edit&redlink=1 "PL 1 (page does not exist)") several times, but each time I thought about it, portability was an issue as PL/1 was really an [IBM](index.php?title=IBM&action=edit&redlink=1 "IBM (page does not exist)") language at first, and then when the Cray came along in the mid 70's it was obvious that they were never going to be anything but a FORTRAN machine, so I stuck with FORTRAN.

```

```C++
For speed, we did lots of profiling and rewrote the time-critical parts in cray assembly language. We made sure that the [CAL](Assembly#CAL "Assembly") code was functionally equivalent to the FORTRAN code so that we could debug things, but the CAL was pretty wild in that it was really tailored to use the architectural tricks available in the Cray, such as vector operations, tons of registers, etc.

```

```C++
I think I will put the whole mess on my ftp box in case anyone is interested. I played one test game between CB and Crafty last night, one CPU, no [pondering](Pondering "Pondering") since CB can't yet ponder, 10 secs per move. Crafty won handily, typically searching 14-15 plies to CB's 9-10. I even used the nm=2 command to set null-move R=2 in CB. Not quite sure why the depth is so different, other than the checks and things CB does in the q-search might be a bit out of control, and/or the extensions might be "too much". But in any case, it played just fine, although not all compilers are going to be happy compiling it I'd bet... 

```

## See also

- [Blitz](Blitz "Blitz")
- [Book Issues in Cray Blitz vs. Fidelity X @ ACM 1984](Boris_Baczynskyj#CrayBlitzFidelity "Boris Baczynskyj")
- [Crafty](Crafty "Crafty")
- [Draw Heuristic of Cray Blitz](Draw#CrayBlitz "Draw")
- [Levy versus Cray Blitz 1984](Advances_in_Computer_Chess_4#LevyCrayBlitz "Advances in Computer Chess 4")
- [Rule of the Square - Nuchess vs. Cray Blitz @ ACM 1984](Rule_of_the_Square#NuchessCrayBlitz "Rule of the Square")
- [WCCC 1983](WCCC_1983 "WCCC 1983")
- [WCCC 1986](WCCC_1986 "WCCC 1986")

## Publications

## 1981 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *The Cray-1 Plays Chess (Part 1)*. [Personal Computing, Vol. 5, No. 1](Personal_Computing#5_1 "Personal Computing"), pp. 83
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *The Cray-1 Plays Chess (Part 2)*. [Personal Computing, Vol. 5, No. 2](Personal_Computing#5_2 "Personal Computing"), pp. 95 » [Cray-1](Cray-1 "Cray-1")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 1](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d2f73)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 1. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2%20and%203-3.Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980/Cray_Channels_Vol-3_No-1.Checkmate_The_Cray-1_Plays_Chess.Hyatt.1980.062303023.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1981**). *[Checkmate: The Cray-1 Plays Chess. Part 2](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1070)*. [Cray Channels](http://www.0x07bell.net/WWWMASTER/CrayWWWStuff/Cfaqccframeset.html), Vol. 3, No. 2. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2.Cray_Channels_Vol-3_No-2.Checkmate.Cray_Blitz.Hyatt.1981/Cray_Channels_Vol-3_No-2.Checkmate.Cray_Blitz.Hyatt.1981.062303019.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1983**). *Cray Blitz - A Computer Chess Playing Program*. Master's Thesis, [University of Southern Mississippi](University_of_Southern_Mississippi "University of Southern Mississippi")
- [Harry Nelson](Harry_Nelson "Harry Nelson") (**1984**). *How We Won The Computer Chess World's Championship*. Excerpt from a talk given at he DAS Computer Science Colloquium, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2.Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984/Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984.062303020.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") » [WCCC 1983](WCCC_1983 "WCCC 1983")
- [Tony Harrington](Tony_Harrington "Tony Harrington") (**1984**). *Blitz on New York - Report of WCCC 1983*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [February 1984](http://www.chesscomputeruk.com/html/publication_archive_1984.html) » [WCCC 1983](WCCC_1983 "WCCC 1983")

## 1985 ...

- [David E. Welsh](David_E._Welsh "David E. Welsh"), [Boris Baczynskyj](Boris_Baczynskyj "Boris Baczynskyj") (**1985**). *[Computer Chess II](http://www.amazon.com/Computer-Chess-II-David-Welsh/dp/0697099113)*. William C Brown Publications, ISBN-13: 978-0697099112 <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a>
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Albert Gower](Albert_Gower "Albert Gower"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Cray Blitz*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4"), reprinted (**1988**). in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Hash Tables in Cray Blitz*. [ICCA Journal, Vol. 8, No. 1](ICGA_Journal#8_1 "ICGA Journal")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1985**). *Parallel Chess on the Cray X-MP/48*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Harry Nelson](Harry_Nelson "Harry Nelson"), [Albert Gower](Albert_Gower "Albert Gower") (**1986**). *Cray Blitz - 1984 Chess Champion*. Telematics and Informatics Vol. 2, No. 4, pp. 299-305. Pergammon Press Ltd.
- [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *The Draw Heuristic of Cray Blitz*. [ICCA Journal, Vol. 11, No. 1](ICGA_Journal#11_1 "ICGA Journal")
- [Harry Nelson](Harry_Nelson "Harry Nelson") (**1989**). *Some Observations about Hash Tables in Cray Blitz*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")

## 1990 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Albert Gower](Albert_Gower "Albert Gower"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1990**). *Cray Blitz*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition"), pp. 111-130
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1990**). *[Chess and supercomputers: details about optimizing Cray Blitz](http://ieeexplore.ieee.org/document/130041/)*. [Supercomputing '90](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=297), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2.IEEE/chess_and_supercomputers.hyatt_nelson.062303027.pdf)

## 2020 ...

- [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2020**). *The history of BLITZ/CRAY-BLITZ/CRAFTY*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")

## Forum Posts

## 1990 ...

- [Cray Blitz Evaluation](https://groups.google.com/d/msg/rec.games.chess/J9Pkg9lOpig/tBN5dVRATwsJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), March 05, 1993 » [Evaluation](Evaluation "Evaluation")
- [Cray Blitz / ACM '94](https://groups.google.com/d/msg/rec.games.chess/MtVkDmTrYSc/98j7gsMDM4QJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 07, 1994 » [ACM 1994](ACM_1994 "ACM 1994")
- [Re: Did Cray Blitz really have a win?](http://groups.google.com/group/rec.games.chess.misc/msg/aedf418b6cb71b12) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rec.games.chess.misc](Computer_Chess_Forums "Computer Chess Forums"), March 12, 1999 » [ACM 1985](ACM_1985 "ACM 1985"), [WCCC 1986](WCCC_1986 "WCCC 1986"), [Holes](Holes "Holes")
- [hardware of Cray Blitz](https://www.stmintz.com/ccc/index.php?id=55521) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 13, 1999 » [WCCC 1983](WCCC_1983 "WCCC 1983")
- [Why did Cray Blitz has a king safety hashtable?](https://www.stmintz.com/ccc/index.php?id=57235) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), June 21, 1999
- [Bob - Question about Cray Blitz and Vector Processing](https://www.stmintz.com/ccc/index.php?id=64646) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), August 13, 1999

## 2000 ...

- [Cray Blity 1981?](https://www.stmintz.com/ccc/index.php?id=113318) by Joshua Lee, [CCC](CCC "CCC"), June 02, 2000 » [ACM 1981](ACM_1981 "ACM 1981")
- [Cray Blitz source (Carey)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=216685&t=23616) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 10, 2008

## 2010 ...

- [An interesting book with some insights on Bob's Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=39455) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), June 23, 2011
- [Transposition tables in Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=61543) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 26, 2016 <a id="cite-note-18" href="#cite-ref-18">[18]</a>  » [Transposition Table](Transposition_Table "Transposition Table")

## External Links

- [Index of /downloads/crayblitz](http://www.craftychess.com/downloads/crayblitz/)
- [Cray Blitz' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=351)
- [Cray Blitz games at chessgames.com](http://www.chessgames.com/perl/chessplayer?pid=13733)
- [Cray Blitz from Wikipedia](https://en.wikipedia.org/wiki/Cray_Blitz)
- [Cray Blitz](http://www.computerhistory.org/chess/search.php?more=&submitted=1&keywords=Cray+Blitz&x=37&y=5&all=all&item_document=item_document&item_moving_image=item_moving_image&item_artifact=item_artifact&item_still_image=item_still_image&item_oral_history=item_oral_history&item_software=item_software) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Oral History of Harry Nelson - Video](http://www.computerhistory.org/chess/related_materials/oral-history/nelson.oral_history.2005.102630659/index.php?iid=orl-4334418e5cbb2), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [How to beat a chess champion - David Levy vs. computer program CRAY BLITZ](http://findarticles.com/p/articles/mi_m1200/is_v127/ai_3645282), Science News, Feb 16, 1985
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-19" href="#cite-ref-19">[19]</a>
- [How Far We've Come: 20 Years of Personal Computing](http://wondersmith.com/rants/howfar.htm) by [Blake Linton Wilfong](http://wondersmith.com/scifi/author.htm), November 05, 2000 » [ACM 1981](ACM_1981 "ACM 1981"), [Sargon](Sargon "Sargon"), [Crafty](Crafty "Crafty")
- [The wrong bishop – part two](http://en.chessbase.com/post/the-wrong-bishop-part-two) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), May 22, 2016 » [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik"), [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn"), [WCCC 1983](WCCC_1983 "WCCC 1983")
- [Cray-1 – the eight million dollar super-computer](https://en.chessbase.com/post/how-fast-was-the-cray) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), September 23, 2016 » [Cray-1](Cray-1 "Cray-1") <a id="cite-note-20" href="#cite-ref-20">[20]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [The New Champion](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cf749) by [Harold Bogner](index.php?title=Harold_Bogner&action=edit&redlink=1 "Harold Bogner (page does not exist)"), [Chess Life](https://en.wikipedia.org/wiki/Chess_Life), February 1984, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.Chess_Life.The_New_Champion.Bogner.Feb-1984/Chess_Life.The_New_Champion.Bogner.Feb-1984.062303068.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), Cover Photo: [Ken Thompson](Ken_Thompson "Ken Thompson"), [Joe Condon](Joe_Condon "Joe Condon"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), and [Albert Gower](Albert_Gower "Albert Gower")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The Eleventh ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cdeeb), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1980_11th_ACM_NACCC/The_Eleventh_ACMs_North_American_Computer_Chess_Championship.1980.062303015.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Letter to Robert Hyatt](http://archive.computerhistory.org/projects/chess/related_materials/text/3-2.Harry_Nelson/JRM-08-05-81/JRM-08-05-81.062303024.sm.pdf) August 5, 1981 (pdf) Courtesy of [Harry Nelson](Harry_Nelson "Harry Nelson") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1983**). Cray Blitz - *A Computer Chess Playing Program*. Master's Thesis, [University of Southern Mississippi](University_of_Southern_Mississippi "University of Southern Mississippi")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Albert Gower](Albert_Gower "Albert Gower"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Cray Blitz*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4"), reprinted (**1988**). in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1985**). *Parallel Chess on the Cray X-MP/48*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1990**). *Chess and Supercomputers, details on optimizing Cray Blitz*. Proceedings of Supercomputing '90
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Harry Nelson](Harry_Nelson "Harry Nelson") (**1984**). *How We Won The Computer Chess World's Championship*. Excerpt from a talk given at the DAS Computer Science Colloquium, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2.Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984/Nelson-Harry.Cray-Blitz.How_we_won.Jan-1984.062303020.pdf), Courtesy of [Harry Nelson](Harry_Nelson "Harry Nelson") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Albert Gower](Albert_Gower "Albert Gower"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1990**). *Cray Blitz*. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner"), A SZÁMÍTÓGÉPES SAKK KÉPEKBEN című melléklete - The pictures of the Beginning of Chess Computers
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> Photo from [Historic Pictures](http://members.home.nl/matador/chess820.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Photo](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbdea550) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") (wrong text)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Downloads Games Country championships](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=43&Itemid=26) from the [CSVN](CSVN "CSVN") site
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Re: Cray Blitz source (Carey)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=216806&t=23616) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 10, 2008
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [An interesting book with some insights on Bob's Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=39455) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), June 23, 2011
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Transposition tables in Cray Blitz](http://www.talkchess.com/forum/viewtopic.php?t=61543) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 26, 2016
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [David E. Welsh](David_E._Welsh "David E. Welsh"), [Boris Baczynskyj](Boris_Baczynskyj "Boris Baczynskyj") (**1985**). *[Computer Chess II](http://www.amazon.com/Computer-Chess-II-David-Welsh/dp/0697099113)*. William C Brown Publications, ISBN-13: 978-0697099112
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [How fast was the Cray?](http://www.talkchess.com/forum/viewtopic.php?t=61504) by Sean Evans, [CCC](CCC "CCC"), September 23, 2016

**[Up one Level](Engines "Engines")**

