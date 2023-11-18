---
title: CHAOS
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CHAOS**

[](http://www.schaakkunst.nl/Schaakkunst_Boldriaan.htm) [Boldriaan](Category:Boldriaan "Category:Boldriaan") - CHAOS (2006) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CHAOS** was one of the leading programs since it first appeared at [ACM 1973](ACM_1973 "ACM 1973") until the mid 80s. CHAOS, which stands facetiously for *Chess Heuristics And Other Stuff*, has participated in twelve [ACM tournaments](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and four [world championships](World_Computer_Chess_Championship "World Computer Chess Championship") <a id="cite-note-3" href="#cite-ref-3">[3]</a> , runner up in [1974](WCCC_1974 "WCCC 1974") behind [Kaissa](Kaissa "Kaissa"), defeating favorite [Chess 4.0](</Chess_(Program)> "Chess (Program)"). In 1980 at the [3rd WCCC](WCCC_1980 "WCCC 1980"), CHAOS was close to becoming champion but lost the playoff against [Belle.](Belle "Belle") Its last tournament was the [16th AMC 1985](ACM_1985 "ACM 1985") when it lost two games in a very strong field.

## History

CHAOS started in the late 1960s at [RCA](https://en.wikipedia.org/wiki/RCA) Systems Programming division in [Cinnaminson, NJ](https://en.wikipedia.org/wiki/Cinnaminson_Township,_New_Jersey) with [Ira Ruben](Ira_Ruben "Ira Ruben"), [Fred Swartz,](Fred_Swartz "Fred Swartz") [Victor Berman,](Victor_Berman "Victor Berman") [Joe Winograd](Joe_Winograd "Joe Winograd"), and [William Toikka](William_Toikka "William Toikka") as first authors. In January 1972, [Sperry Univac](https://en.wikipedia.org/wiki/Sperry_Corporation) (1986 [Unisys](https://en.wikipedia.org/wiki/Unisys)) officially took over the RCA Computer Systems Division and eventually moved everything to [Blue Bell, Pennsylvania](https://en.wikipedia.org/wiki/Blue_Bell,_Pennsylvania). Later the program has been affiliated with the Computing Center of the [University of Michigan](University_of_Michigan "University of Michigan") where most of its programmers were staff members <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Knowledge vs Search

CHAOS was written in [Fortran](Fortran "Fortran") and required in excess of 3,000,000 words of memory to execute, using most of it for storing the [tree](Search_Tree "Search Tree"). It examines only about 50 [nodes/sec](Nodes_per_Second "Nodes per Second") (1985 70 nodes/sec <a id="cite-note-5" href="#cite-ref-5">[5]</a> ) or about 10,000 per move. The reason why CHAOS evaluated so slowly — their programmers did a better job of [evaluation](Evaluation "Evaluation")! Because every minimax decision is made based on a single evaluation, it seemed plausible that the more accurate this number is, the better the quality of tree searching. However, that comes at the cost of missing deep combinations from brute force search, but CHAOS's [strength](Playing_Strength "Playing Strength")/[nodes](Node "Node")-evaluated ratio was impressive. The program carried out a selective search with iterative widening, a bit different from the others. Its book contains about 10,000 lines.

## Quotes

## Alex Bell

[Alex Bell](Alex_Bell "Alex Bell") on the CHAOS - Chess 4.0 game 1974 <a id="cite-note-6" href="#cite-ref-6">[6]</a> :

```C++
CHAOS played 16 NxP!! - a move which has been acclaimed as the finest ever made by a computer. White evaluates that his domination of open lines is compensation for a piece. This judgement is absolutely correct. Of course the piece is not sacrificed entirely and play continues in a very similar fashion to [MASTER's](Master "Master") sacrifice of a bishop to [TELL](Tell "Tell"). 

```

|  |
| --- |
|                                                                      ♜♛  ♚  ♜   ♞ ♟♟♟♟  ♝♟♞♝         ♘♟ ♘     ♗   ♙♙ ♙♙  ♕  ♙♖ ♗♖  ♔  |

```C++
rq2k2r/3n1ppp/p2bpnb1/8/Np1N4/1B3PP1/PP2Q2P/R1BR2K1 w kq - 1 16

```

## Duel on the Chessboard

Quote from *Computer vs. computer: Duel on the Chessboard* <a id="cite-note-7" href="#cite-ref-7">[7]</a> on [ACM 1979](ACM_1979 "ACM 1979"):

```C++
The biggest and most powerful computers do that very well. In one second, they can examine thousands of possible moves. The problem is, they stop to consider lousy moves that a human player wouldn't waste a fraction of a second on. On the other side of the fence are the slower but "smarter" computer programs. They can't think about zillions of chess moves, so they need a lot of information about chess plugged into them. CHAOS is one of these latter, pumped with chess information from [John J. O’Keefe](Jack_O%E2%80%99Keefe "Jack O’Keefe"), one of Michigan's top players. 

```

## Authors

|  1973 <a id="cite-note-8" href="#cite-ref-8">[8]</a> |  1976 <a id="cite-note-9" href="#cite-ref-9">[9]</a> |  1978 <a id="cite-note-10" href="#cite-ref-10">[10]</a> |  1983 <a id="cite-note-11" href="#cite-ref-11">[11]</a> |
| --- | --- | --- | --- |
|  | [Mike Alexander](Mike_Alexander "Mike Alexander") | [Mike Alexander](Mike_Alexander "Mike Alexander") | [Mike Alexander](Mike_Alexander "Mike Alexander") |
| [Victor Berman](Victor_Berman "Victor Berman") | [Victor Berman](Victor_Berman "Victor Berman") | [Victor Berman](Victor_Berman "Victor Berman") | [Victor Berman](Victor_Berman "Victor Berman") |
|  |  |  | [Mark Hersey](Mark_Hersey "Mark Hersey") |
|  |  | [Tom McBride](index.php?title=Tom_McBride&action=edit&redlink=1 "Tom McBride (page does not exist)") |  |
|  |  |  | [Jack O’Keefe](Jack_O%E2%80%99Keefe "Jack O’Keefe") |
| [Ira Ruben](Ira_Ruben "Ira Ruben") | [Ira Ruben](Ira_Ruben "Ira Ruben") |  |  |
| [Fred Swartz](Fred_Swartz "Fred Swartz") | [Fred Swartz](Fred_Swartz "Fred Swartz") | [Fred Swartz](Fred_Swartz "Fred Swartz") | [Fred Swartz](Fred_Swartz "Fred Swartz") |
| [William Toikka](William_Toikka "William Toikka") | [William Toikka](William_Toikka "William Toikka") | [William Toikka](William_Toikka "William Toikka") |  |
| [Joe Winograd](Joe_Winograd "Joe Winograd") | [Joe Winograd](Joe_Winograd "Joe Winograd") | [Joe Winograd](Joe_Winograd "Joe Winograd") |  |

## Photos & Games

## CHAOS Team

[](File:CHAOS_Team_circa_1972.gif)
CHAOS Team circa 1972 with [UNIVAC 1108](UNIVAC_1100 "UNIVAC 1100") Computer in [Cinnaminson, NJ](https://en.wikipedia.org/wiki/Cinnaminson_Township,_New_Jersey)\
From left, [Fred Swartz](Fred_Swartz "Fred Swartz") (rear), [Vic Berman](Victor_Berman "Victor Berman") (front), [Bill Toikka](William_Toikka "William Toikka"), [Ira Ruben](Ira_Ruben "Ira Ruben") (seated), [Joe Winograd](Joe_Winograd "Joe Winograd") <a id="cite-note-12" href="#cite-ref-12">[12]</a>

## WCCC 1974

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbdafbd8)
[Slate](David_Slate "David Slate"), [Swartz](Fred_Swartz "Fred Swartz"), and [Berman](Victor_Berman "Victor Berman") in CHAOS vs [Chess 4.0](</Chess_(Program)> "Chess (Program)"), [WCCC 1974](WCCC_1974 "WCCC 1974") <a id="cite-note-13" href="#cite-ref-13">[13]</a> <a id="cite-note-14" href="#cite-ref-14">[14]</a>

```

[Event "WCCC 1974"]
[Site "Stockholm, Sweden"]
[Date "1974.08.06"]
[Round "2"]
[White "Chaos"]
[Black "Chess 4.0"]
[Result "1-0"]

1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.Qe2 a6 7.O-O b5 8.Bb3 Bb7
9.Rd1 Nbd7 10.Nc3 Bd6 11.e4 cxd4 12.Nxd4 Qb8 13.g3 b4 14.Na4 Bxe4 15.f3 Bg6
16.Nxe6 fxe6 17.Qxe6+ Be7 18.Re1 Qd8 19.Bf4 Kf8 20.Rad1 Ra7 21.Rc1 Ng8 22.Rcd1
a5 23.Bd6 Bxd6 24.Qxd6+ Ne7 25.Nc5 Bf5 26.g4 Qe8 27.Ba4 b3 28.gxf5 bxa2 29.Bxd7
a1=Q 30.Rxa1 Ra6 31.Nxa6 Qd8 32.Kf2 Kf7 33.Qe6+ Kf8 34.Qxe7+ Qxe7 35.Rxe7 Kxe7
36.Nc5 Rb8 37.Rxa5 Rxb2+ 38.Kg3 g6 39.fxg6 hxg6 40.Ra6 Rc2 41.Re6+ Kf8 42.Re5 Rc1
43.Rg5 Kf7 44.Be6+ Kf6 45.h4 Rxc5 46.Rxc5 Kxe6 47.Rg5 Kf6 48.Kg4 Kf7 49.Rc5 Ke6
50.Kg5 Kd6 51.Ra5 Kc6 52.f4 Kb6 53.Ra1 Kc5 54.Rd1 Kb4 55.Kxg6 Kc3 56.Rd8 Kb4
57.Rc8 Kb5 58.h5 Kb6 59.Rc1 Kb5 60.h6 Ka4 61.Rb1 Ka3 62.f5 Ka2 63.Rb8 Ka3 64.f6
Ka4 65.Rb7 Ka5 66.Rb8 Ka4 67.Rb1 Ka3 68.Rb7 Ka4 69.Rb8 Ka5 70.Kg7 Ka4 71.Rb7 Ka5
72.Rb2 Ka4 73.Rb8 Ka5 74.Kg8 Ka4 75.h7 Ka5 76.h8=Q Ka4 77.Qh4+ Ka5 78.Qb4+ Ka6
79.Qa4# 1-0

```

## WCCC 1980

[](http://www.computerhistory.org/chess/full_record.php?iid=stl-432a034fb7102)
[Belle](Belle "Belle") vs CHAOS, [WCCC 1980](WCCC_1980 "WCCC 1980"), [Thompson](Ken_Thompson "Ken Thompson"), [Friedel](Frederic_Friedel "Frederic Friedel"), [Berman](Victor_Berman "Victor Berman") <a id="cite-note-15" href="#cite-ref-15">[15]</a> , [Swartz](Fred_Swartz "Fred Swartz"), [Donskoy](Mikhail_Donskoy "Mikhail Donskoy") <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a>

```

[Event "WCCC 1980"]
[Site "Linz, Austria"]
[Date "1980.09.29"]
[Round "5 (playoff)"]
[White "Belle"]
[Black "Chaos"]
[Result "1-0"]

1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 dxe5 5.Nxe5 g6 6.g3 Bf5 7.c4 Nb4 8.Qa4+ N4c6
9.d5 Bc2 10.Qb5 Qd6 11.Nxc6 Nxc6 12.Nc3 Bg7 13.Qxb7 O-O 14.Qxc6 Qb4 15.Kd2 Be4
16.Rg1 Rfb8 17.Bh3 Bh6+ 18.f4 Qa5 19.Re1 f5 20.Qe6+ Kf8 21.b3 Bg7 22.Bb2 Bd4
23.g4 Rb6 24.Qd7 Rd6 25.Qa4 Qb6 26.Ba3 Bxc3+ 27.Kxc3 Rdd8 28.Rad1 Qf2 29.gxf5
Qc2+ 30.Kd4 gxf5 31.Qc6 Qf2+ 32.Ke5 Kg8 33.Rg1+ Kh8 34.Bxe7 Qb2+ 35.Rd4 Qg2
36.Qf6+ Kg8 37.Bxg2 Rxd5+ 38.Ke6 h6 39.Qxh6 Re5+ 40.fxe5 Rf8 41.Bf3# 1-0

```

## See also

- [Chaos](Evaluation_Overlap#Chaos "Evaluation Overlap") from [Evaluation Overlap](Evaluation_Overlap "Evaluation Overlap") by [Mark Watkins](Mark_Watkins "Mark Watkins")
- [Freedom vs. CHAOS](Freedom#FreedomCHAOS "Freedom")

## Forum Posts

- [Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938) by Eugene Piercy, [CCC](CCC "CCC"), July 11, 2015

## External Links

## Chess Program

- [Chaos' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=42)
- [Computer vs. computer: Duel on the Chessboard, Boca Raton News - November 27. 1979](http://news.google.com/newspapers?nid=1291&dat=19791127&id=QfwPAAAAIBAJ&sjid=EY0DAAAAIBAJ&pg=6410,4650912) from [Google News](http://news.google.com/nwshp) on [ACM 1979](ACM_1979 "ACM 1979")
- [Chess players are experiencing CHAOS, Lakeland Ledger - November 29, 1979](http://news.google.com/newspapers?nid=1346&dat=19791129&id=N3gsAAAAIBAJ&sjid=zPoDAAAAIBAJ&pg=7021,5104937) from [Google News](http://news.google.com/nwshp)
- [Images - Michigan Terminal System Archive - Computer Chess, CHAOS and AWIT](http://archive.michigan-terminal-system.org/images#TOC-13-Photographs:-Computer-Chess-CHAOS-and-AWIT) » [Awit](Awit "Awit")

## Misc

- [Chaos in a Miniature](http://www.chesshistory.com/winter/extra/laskerthomas.html) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
- [Chaos (cosmogony) from Wikipedia](https://en.wikipedia.org/wiki/Chaos_%28cosmogony%29)
- [Chaos theory from Wikipedia](https://en.wikipedia.org/wiki/Chaos_theory)
- [Sun Ra](Category:Sun_Ra "Category:Sun Ra") - Cosmic Chaos, from [The Heliocentric Worlds of Sun Ra, Vol. 2](https://en.wikipedia.org/wiki/The_Heliocentric_Worlds_of_Sun_Ra,_Volume_Two) (1965), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Schaakkunst van Boldriaan](http://www.schaakkunst.nl/Schaakkunst_Boldriaan.htm)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [North American Computer-Chess Championships](http://old.csvn.nl/ncc_hist.html), complete History of Tournament Results and Games, prepared by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), Nov. 23rd, 2002, secretary of the [CSVN](CSVN "CSVN")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Chaos' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=42)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The Eleventh ACM's North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cdeeb) as [pdf reprint](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.1980_11th_ACM_NACCC/The_Eleventh_ACMs_North_American_Computer_Chess_Championship.1980.062303015.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [David .E. Welsh](http://www.amazon.co.uk/David-E-Welsh/e/B000AP7TNG/ref=ntt_athr_dp_pel_1) (**1986**). *[ACM's Sixteenth North American Computer Chess Championship](ACM_1985 "ACM 1985")*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 8, No. 4.
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Alex Bell](Alex_Bell "Alex Bell") (**1978**). *[MASTER at IFIPS](http://www.chilton-computing.org.uk/acl/applications/cocoa/p008.htm)*. from [Atlas Computer Laboratory](Atlas_Computer_Laboratory "Atlas Computer Laboratory"), hosted by [Rutherford Appleton Laboratory (RAL)](https://en.wikipedia.org/wiki/Rutherford_Appleton_Laboratory), excerpt from [A. G. Bell](Alex_Bell "Alex Bell") (**1978**). *The Machine Plays Chess*. Pergamon Press, ISBN-13: 978-0080212227, from [amazon](http://www.amazon.com/Machine-Plays-Chess-Pergamon/dp/0080212220)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Computer vs. computer: Duel on the Chessboard, Boca Raton News - November 27. 1979](http://news.google.com/newspapers?nid=1291&dat=19791127&id=QfwPAAAAIBAJ&sjid=EY0DAAAAIBAJ&pg=6410,4650912) from [Google News](http://news.google.com/nwshp) on [ACM 1979](ACM_1979 "ACM 1979")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1975**). *Computer Chess*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press), New York, N.Y. Chapter IX. The Fourth United States Computer Chess Championship » [ACM 1973](ACM_1973 "ACM 1973")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> pp. 52, Table I. History of the [ACM Tournaments](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship") from
   [Ben Mittman](Ben_Mittman "Ben Mittman"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1980**). *Computer chess at [ACM 79](ACM_1979 "ACM 1979"): the tournament and the man vs. man and machine match*. Communications of the [ACM](ACM "ACM"), Vol. 23, Issue 1, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79.062303018.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") » [ACM 1976](ACM_1976 "ACM 1976")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [David Levy](David_Levy "David Levy") (**1978**). *ACM '78*. [ICCA Newsletter, Vol. 1, No. 1](ICGA_Journal#1_1 "ICGA Journal") » [ACM 1978](ACM_1978 "ACM 1978")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Chaos' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=42)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> Photo courtesy [Joe Winograd](Joe_Winograd "Joe Winograd")
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Photo](http://www.computerhistory.org/chess/full_record.php?iid=stl-430b9bbdafbd8) by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Stockholm 1974 - Chess - Round 2 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=7&round=2&id=6)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Militärischer Wert](http://www.spiegel.de/spiegel/print/d-14342470.html) [Der Spiegel](https://en.wikipedia.org/wiki/Der_Spiegel) 24/1982, [pdf](http://magazin.spiegel.de/EpubDelivery/spiegel/pdf/14342470) (German)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Photo](http://www.computerhistory.org/chess/full_record.php?iid=stl-432a034fb7102) by [Monroe Newborn](Monroe_Newborn "Monroe Newborn") from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Linz 1980 - Chess - Round 5 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=68&round=5&id=1)

**[Up one level](Engines "Engines")**

