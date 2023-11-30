---
title: Dorky
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Dorky**

\[.jpg) Dork <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Dorky**, (Dorky Chess)

a [WinBoard](WinBoard "WinBoard") compatible engine for [Windows](Windows "Windows") written by [Matt McKnight](Matt_McKnight "Matt McKnight") in [C](C "C")/[C++](Cpp "Cpp"),
first released in May 2003 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Dorky already played the [CCT2](CCT2 "CCT2") in 2000, and Dorky 4.0 the [CCT6](CCT6 "CCT6") [tournament](CCT_Tournaments "CCT Tournaments").
Dorky 4.x, a rewrite of most major components, was the first release of a new version after almost seven years in May 2011,
with access to [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases") and a [parallel search](Parallel_Search "Parallel Search")
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Features

Following [algorithms](Algorithms "Algorithms") and features are used in Dorky Chess 4.3
<a id="cite-note-4" href="#cite-ref-4">[4]</a>

- [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [quiescence search](Quiescence_Search "Quiescence Search")
- [SMP search](Parallel_Search "Parallel Search") using [Dr. Hyatt’s](Robert_Hyatt "Robert Hyatt") [DTS algorithm](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
- [Nalimov Endgame tablebases](Nalimov_Tablebases "Nalimov Tablebases")
- [Late move reductions](Late_Move_Reductions "Late Move Reductions")
- [Futility pruning](Futility_Pruning "Futility Pruning")
- [Transposition hash table](Transposition_Table "Transposition Table") / [Pawn evaluation hash table](Pawn_Hash_Table "Pawn Hash Table") (using Hyatt’s [lockless approach](Shared_Hash_Table#Lockless "Shared Hash Table"))
- [Null-move pruning](Null_Move_Pruning "Null Move Pruning")
- [Killer move heuristic](Killer_Heuristic "Killer Heuristic")
- [Bitboards](Bitboards "Bitboards"), [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") for [move generation](Move_Generation "Move Generation")
- [Static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Opening Book](Opening_Book "Opening Book") creation and [simple learning](Book_Learning "Book Learning")

## Selected Games

## CCT2

[CCT2](CCT2 "CCT2"), round 1, [Junior](Junior "Junior") - Dorky <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```
[Event "CCT2"]
[Site "Internet Chess Club"]
[Date "2000.11.04"]
[Round "1"]
[White "Junior"]
[Black "Dorky"]
[Result "1-0"]

1.e4 e6 2.d4 d5 3.Nd2 c5 4.Ngf3 Nc6 5.Bb5 cxd4 6.Nxd4 Bd7 7.Bxc6 bxc6 8.O-O Bd6 
9.c4 Nf6 10.Re1 Qc7 11.N4f3 Nxe4 12.Nxe4 dxe4 13.Rxe4 Bc8 14.Rg4 f6 15.Be3 O-O 
16.c5 Be7 17.Qc2 Rd8 18.Rh4 f5 19.Rd4 Rd5 20.Bf4 Qd8 21.Rxd5 Qxd5 22.Bd6 Bxd6 
23.cxd6 Qxd6 24.Rd1 Qf8 25.Ne5 c5 26.Qa4 Rb8 27.Nc6 Rxb2 28.f4 Bb7 29.Rd8 Rxg2+ 
30.Kf1 Bxc6 31.Rxf8+ Kxf8 32.Qxc6 Rxh2 33.Qxc5+ Kf7 34.Qxa7+ Kf6 35.Qd4+ Kf7 
36.a4 Ra2 37.Qd7+ Kf6 38.a5 h6 39.Qd8+ Kg6 40.Qb6 h5 41.Qxe6+ Kh7 42.Qxf5+ Kg8 
43.Qe6+ Kf8 44.Qxa2 Ke7 45.Qg8 Kf6 46.Qxg7+ Kxg7 47.a6 Kg6 48.a7 Kf5 49.a8=Q
1-0

```

## CCT6

[CCT6](CCT6 "CCT6"), round 7, Dorky - [Chiron](Chiron "Chiron") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```
[Event "CCT6"]
[Site "Internet Chess Club"]
[Date "2004.02.01"]
[Round "7"]
[White "Dorky 4.0"]
[Black "Chiron "]
[Result "1-0"]

1.d4 Nf6 2.c4 c6 3.Nf3 d6 4.Nc3 Nbd7 5.e4 e5 6.Be2 Be7 7.Qd2 O-O 8.O-O exd4 
9.Nxd4 d5 10.exd5 cxd5 11.Rd1 Nb6 12.cxd5 Nfxd5 13.Ndb5 Be6 14.Bf3 Bb4 15.Qg5 
Qxg5 16.Bxg5 Bxc3 17.Nxc3 Nxc3 18.bxc3 Rac8 19.Rac1 Na4 20.Bxb7 Rc7 21.Bf3 Rxc3 
22.a3 Rfc8 23.h3 f6 24.Bd2 Rxc1 25.Bxc1 Nb6 26.Be3 Kf7 27.Rb1 Bf5 28.Rb5 Bd7 
29.Ra5 Rc7 30.Bf4 Rc4 31.Bb8 Rc8 32.Bg3 Rc1+ 33.Kh2 Nc8 34.Bb8 Ke6 35.a4 Rc2 
36.Kg3 Ne7 37.Bxa7 Bc6 38.Bxc6 Rxc6 39.Rb5 Nf5+ 40.Kh2 Nd6 41.Rb4 Rc4 42.Rxc4 
Nxc4 43.Bc5 Kd5 44.Bb4 Nb2 45.a5 Kc6 46.Kg3 Nc4 47.Kf4 Kb5 48.Bf8 g6 49.Bg7 
Kxa5 50.Bxf6 Nd6 51.Ke5 Ne8 52.Ke6 Kb5 53.Be5 Kc4 54.Ke7 Kd5 55.f4 Ke4 56.Kxe8 
Kd5 57.Ke7 Ke4 58.Ke6 Ke3 59.g4 Kf3 60.f5 1-0

```

## Forum Posts

## 2003 ...

- [Dorky 3.4: I found this when I was toying with ICC](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42742) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 25, 2003
- [Dorky Chess download site](https://www.stmintz.com/ccc/index.php?id=303923) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), June 30, 2003
- [Dorky 3.43](https://www.stmintz.com/ccc/index.php?id=304559) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), July 03, 2003
- [Dorky mate reporting](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43289) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 07, 2003
- [Dorky 3.44 released](https://www.stmintz.com/ccc/index.php?id=306467) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), July 14, 2003
- [Dorky 3.45 Released](https://www.stmintz.com/ccc/index.php?id=308070) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), July 25, 2003
- [Dorky 3.47 Released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43988) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 05, 2003
- [Dorky 3.48](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44272) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 25, 2003
- [WAC 041 b7!!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45460) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2003 » [Win at Chess](Win_at_Chess "Win at Chess")
- [Re: position and book learning in some engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46471&start=1) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 13, 2004

## 2010 ...

- [Dorky 4.0 released](http://www.talkchess.com/forum/viewtopic.php?t=39116) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), May 19, 2011
- [Dorky 4.1 Released](http://www.talkchess.com/forum/viewtopic.php?t=39167) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), May 25, 2011
- [Dorky 4.0 and the 50-move rule](http://www.talkchess.com/forum/viewtopic.php?t=39226) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), May 29, 2011
- [Dorky 4.0 and 3-fold repetition](http://www.talkchess.com/forum/viewtopic.php?t=39228) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), May 29, 2011
- [Dorky is lot better than I thought](http://www.talkchess.com/forum/viewtopic.php?t=39312) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), June 08, 2011
- [Dorky 4.1 64-bit - always single-threaded?](http://www.talkchess.com/forum/viewtopic.php?t=39405) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), June 17, 2011
- [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=39407&start=4) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), June 17, 2011
- [Dorky 4.2 released](http://www.talkchess.com/forum/viewtopic.php?t=39500) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), June 27, 2011
- [Dorky 4.2 64-bit 2CPU time losses - very long post?](http://www.talkchess.com/forum/viewtopic.php?t=39603) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), July 04, 2011
- [Dorky 4.3 Released](http://www.talkchess.com/forum/viewtopic.php?t=39840) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), July 24, 2011
- [Dorky 4.3 64-bit - odd memory usage](http://www.talkchess.com/forum/viewtopic.php?t=40487) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), September 21, 2011
- [What Happens with Dorky?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=42846) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), March 12, 2012
- [No News about Dorky?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=42924) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), March 18, 2012
- [Dorky Chess again...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=43412) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), April 22, 2012

## 2015 ...

- [Dorky v4.5 Released](http://www.talkchess.com/forum/viewtopic.php?t=61531) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), September 25, 2016
- [Dorky 4.6 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68004) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), July 17, 2018
- [Dorky 4.7 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68075) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), July 25, 2018
- [Dorky 4.8](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68267) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), August 21, 2018

## External Links

## Chess Engine

- [Dorky Chess](http://home.insightbb.com/~mmcknight/) by [Matt McKnight](Matt_McKnight "Matt McKnight")
- [Dorky](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Dorky&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [dorky - Wiktionary](https://en.wiktionary.org/wiki/dorky)
- [dork - Wiktionary](https://en.wiktionary.org/wiki/dork)
- [Dork (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Dork)
- [Dork (magazine) from Wikipedia](<https://en.wikipedia.org/wiki/Dork_(magazine)>)
- [Urban Dictionary: dorkfish](https://www.urbandictionary.com/define.php?term=dorkfish)
- [Dorkfish from Wikipedia](https://en.wikipedia.org/wiki/Dorkfish)
- [Constanza Macras](https://www.schaubuehne.de/de/personen/constanza-macras.html) / [DorkyPark](https://en.wikipedia.org/wiki/Dorky_Park) - [Brickland](http://www.dorkypark.org/site/exhibit/brickland-2/), [Schaubühne](https://en.wikipedia.org/wiki/Schaub%C3%BChne), 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Image](<https://commons.wikimedia.org/wiki/File:Dork_(4385707475).jpg>) by [Quinn Dombrowski](https://www.flickr.com/people/53326337@N00) from [Berkeley](https://en.wikipedia.org/wiki/Berkeley,_California), USA, February 24, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Dorky](https://web.archive.org/web/20120513030524/http://wbec-ridderkerk.nl/html/details1/Dorky.html) from [WBEC Ridderkerk](WBEC "WBEC") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Dorky 4.0 released](http://www.talkchess.com/forum/viewtopic.php?t=39116) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [CCC](CCC "CCC"), May 19, 2011
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Dorky Chess Download](http://home.insightbb.com/~mmcknight/), Dorky4.3-win-x86.zip / Dorky Chess 4.3 pdf
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [CCT2 - PGN download](http://www.vrichey.de/cct2/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CCT6 - PGN download](http://www.vrichey.de/cct6/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one level](Engines "Engines")**

