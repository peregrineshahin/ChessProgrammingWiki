---
title: BCP
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BCP**

**BCP**,

[Don Beal's](Don_Beal "Don Beal") Chess Program, which participated at four [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [WCCC 1977](WCCC_1977 "WCCC 1977"), [WCCC 1980](WCCC_1980 "WCCC 1980"), [WCCC 1983](WCCC_1983 "WCCC 1983") and [WCCC 1986](WCCC_1986 "WCCC 1986"). In 1980 running on a [PDP-11/70](PDP-11 "PDP-11"), since 1983 BCP was custom-build computer with a fast [sequential logic](Sequential_Logic "Sequential Logic") controlled by a [Zilog Z8000](https://en.wikipedia.org/wiki/Zilog_Z8000) [16-bit](https://en.wikipedia.org/wiki/16-bit) [micro computer](https://en.wikipedia.org/wiki/Microcomputer). The program was written in [C](C "C"), [Assembly](Assembly "Assembly"), and [Microcode](https://en.wikipedia.org/wiki/Microcode), performing 20K [Nodes per second](Nodes_per_Second "Nodes per Second") (1983) <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Mate Search

In order to find mating sequences fast, BCP's [Quiescence Search](Quiescence_Search "Quiescence Search") includes [checks](Check "Check") if and only if they have one (or no) reply <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The original intention of this rule was to detect some (relativly) frequent cased of [mate](Checkmate "Checkmate") in two, but Don Beal obsearved the search time only increased marginally when the depth limit was removed.

## Photos & Games

## 1983

[](http://www.chesscomputeruk.com/html/publication_archive_1983.html)
[Don Beal's](Don_Beal "Don Beal") BCP still in the assembly stage, 1983 <a id="cite-note-3" href="#cite-ref-3">[3]</a>

[](File:NelsonHyattBeal1983.JPG)
[WCCC 1983](WCCC_1983 "WCCC 1983"): [Harry Nelson](Harry_Nelson "Harry Nelson"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Don Beal](Don_Beal "Don Beal"), [Cray Blitz](Cray_Blitz "Cray Blitz") - BCP <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```

[Event WCCC 1983"]
[Site "New York, USA"]
[Date "1983.10.22"]
[Round "1"]
[White "Cray Blitz"]
[Black "BCP"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nf6 3.e5 Nd5 4.Nc3 e6 5.Nxd5 exd5 6.d4 Nc6 7.dxc5 Bxc5 
8.Qxd5 Qb6 9.Qd2 O-O 10.Bc4 Re8 11.O-O Nxe5 12.Nxe5 Rxe5 13.Qf4 Qf6 
14.Qxf6 gxf6 15.Kh1 d5 16.f4 Rh5 17.Be2 Rh4 18.Bf3 d4 19.g3 Rh3 20.f5 Kg7 
21.Kg2 Rh6 22.Bxh6+ Kxh6 23.Bd5 Kg7 24.Rad1 a5 25.Kh1 Ra6 26.Be4 b5 
27.Rfe1 Bd7 28.Rd2 Bc6 29.Bxc6 Rxc6 30.Re8 Bb6 31.Rb8 b4 32.Rb7 Kf8 
33.Re2 Bc7 34.g4 Rc5 35.Ra7 Bb6 36.Ra6 Rc6 37.Rd2 Rd6 38.Rd3 Kg7 39.c3 Kg8 
40.a4 Kg7 41.cxb4 axb4 42.a5 Bc5 43.Rxd6 Bxd6 44.Rxd4 Bc5 45.Rd5 Be3 
46.Rd3 Bc5 47.Rd7 Be3 48.a6 h5 49.gxh5 Kf8 50.Rd3 Bc5 51.Rg3 Ke8 52.h6 Bd6 
53.a7 Ke7 54.Rd3 Bc7 55.a8=Q Bd6 56.h7 b3 57.Qb7+ Ke8 
58.h8=Q+ Bf8 59.Qe4# 1-0

```

## 1986

[WCCC 1986](WCCC_1986 "WCCC 1986"), Round 2, [Nona](Nona "Nona") - BCP <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```

[Event "WCCC 1986"]
[Site "Cologne, Germany"]
[Date "1986.06.12"]
[Round "2"]
[White "Nona"]
[Black "BCP"]
[Result "0-1"]

1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 e6 6.cxd5 Nxd5 7.e4 Nxc3 
8.Qxc3 O-O 9.Bf4 Nc6 10.Rd1 Bd7 11.Bc4 Nxd4 12.Nxd4 c5 13.Be3 cxd4 
14.Bxd4 Bxd4 15.Rxd4 Qc7 16.O-O Rac8 17.f4 Qb6 18.Kh1 Rfd8 19.Rfd1 Ba4 
20.Rxd8+ Rxd8 21.Rxd8+ Qxd8 22.Be2 Bc6 23.Qe3 Qa5 24.Bc4 Qa4 25.Qd3 b5 
26.Qd8+ Kg7 27.Bf1 Qxe4 28.Qd2 e5 29.fxe5 Qxe5 30.Qf2 Kg8 31.Qxa7 Qxb2 
32.Kg1 Qe5 33.Qb6 Qe4 34.Qd8+ Qe8 35.Qxe8+ Bxe8 36.a3 Bc6 37.Kf2 h5 
38.Ke3 g5 39.Kd4 f5 40.Kc5 Be4 41.Kxb5 f4 42.a4 Kf8 43.a5 Ke8 44.a6 Kd7 
45.a7 Kd6 46.Ka6 Kc5 47.Ka5 Bd5 48.Be2 Bxg2 49.Bb5 Bd5 50.Bd3 f3 
51.Bf1 f2 52.Be2 Be4 53.Bb5 Bf3 54.Bd3 Kd4 55.Bb5 Kc3 56.Ba6 Bd5 
57.Bf1 Be4 58.Kb5 Kd4 59.Ka4 Kc5 60.Ka5 h4 61.h3 Bd5 62.Ka6 Kd4 
63.Kb6 Be4 64.Kb5 Kc3 65.Ka4 Bd5 66.Kb5 Bh1 67.Ka4 Be4 68.Ka3 Bd5 
69.Ka4 Kd4 70.Kb5 Be4 71.Kb6 Kc3 72.Kb5 Kc2 73.Kc4 Kd2 74.Kc5 Ke1 
75.Bc4 f1=Q 0-1 

```

## Publications

- [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *Alphabetical Chess*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [June 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html)
- [Don Beal](Don_Beal "Don Beal") (**1984**). *Mating Sequences in the Quiescence Search*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
- [Don Beal](Don_Beal "Don Beal") (**2006**). *Review of a nullmove-quiescence search mechanism from 1986*. [File:Alg1986review.txt](File:Alg1986review.txt "File:Alg1986review.txt") (Draft) <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## External Links

## Chess Program

- [BCP's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=408)
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## Misc

- [BCP (disambiguation page) from Wikipedia](https://en.wikipedia.org/wiki/BCP)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](Danny_Kopec "Danny Kopec")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Don Beal](Don_Beal "Don Beal") (**1984**). *Mating Sequences in the Quiescence Search*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> Image by [Tony Harrington](Tony_Harrington "Tony Harrington"), from: [Tony Harrington](Tony_Harrington "Tony Harrington") (**1983**). *Alphabetical Chess*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), [June 1983](http://www.chesscomputeruk.com/html/publication_archive_1983.html), [pdf](http://www.chesscomputeruk.com/PCW_June_1983.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner"), A SZÁMÍTÓGÉPES SAKK KÉPEKBEN című melléklete - The pictures of the Beginning of Chess Computers
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [New York 1983 - Chess - Round 1 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=65&round=1&id=2)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Cologne 1986 - Chess - Round 2 - Game 9 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=62&round=2&id=9)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> courtesy of [Don Beal](Don_Beal "Don Beal") and [Carey Bloodworth](Carey_Bloodworth "Carey Bloodworth"), [Re: Antique chess programs](http://www.talkchess.com/forum/viewtopic.php?t=58603&start=13) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), December 16, 2015
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**

