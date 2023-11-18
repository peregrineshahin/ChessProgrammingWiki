---
title: BremboCE
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BremboCE**

\[ The [Brembo](https://en.wikipedia.org/wiki/Brembo_%28river%29) at [Ponte San Pietro](https://en.wikipedia.org/wiki/Ponte_San_Pietro) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BremboCE**,

a [WinBoard](WinBoard "WinBoard") compliant chess engine written by [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"). BremboCE was initially written in [C](C "C"), and first released in February 2002, after Gianluca studied [Tom Kerrigan's](Tom_Kerrigan "Tom Kerrigan") [TSCP](TSCP "TSCP") and learned how to program a chess engine. It had its not too bad tournament debut at [CIPS 2002](CIPS_2002 "CIPS 2002") with 3/6. The latest C-version was 0.4 from August 2002. The engine name is based upon the river [Brembo](https://en.wikipedia.org/wiki/Brembo_%28river%29) in the [Province of Bergamo](https://en.wikipedia.org/wiki/Province_of_Bergamo), situated near the author's home <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Java

After a gap of seven years, in 2009, Gianluca continued the development porting BremboCE from C to [Java](Java "Java"),
running either as standalone WinBoard engine, or as [Java applet](https://en.wikipedia.org/wiki/Java_applet) as part of a [web page](https://en.wikipedia.org/wiki/Web_page) under control of the [Java Virtual Machine (JVM)](https://en.wikipedia.org/wiki/Java_Virtual_Machine) - in a [process](Process "Process") separated from the [web browser](https://en.wikipedia.org/wiki/Web_browser). BremboCE keeps a [board array](Board_Representation#SquareCentric "Board Representation") and uses [negamax alpha-beta](Alpha-Beta#Negamax "Alpha-Beta") with [quiescence](Quiescence_Search "Quiescence Search") considering [captures](Captures "Captures") and [promotions](Promotions "Promotions"). The Java engine played the [4th Chess Computer Cup 2009](CCC_2009 "CCC 2009") with 2½/6, winning from [Golem](Golem "Golem") and [Joker](Joker_NL "Joker NL").

## Photos and Games

[](File:BremboChatturanga.JPG)
[CCC 2009](CCC_2009 "CCC 2009"), round 4, [Stefano Malloggi](Stefano_Malloggi "Stefano Malloggi") and [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"), BremboCE - [Chaturanga](Chaturanga_IT "Chaturanga IT") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "CCC 2009"]
[Site "Carugate, ITA"]
[Date "2009.11.08"]
[Round "4"]
[White "BremboCE 0.6.2"]
[Black "Chaturanga 2.4.2"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.a4 b4 9.d4 d6 10.dxe5 Nxe5 
11.Nbd2 Bb7 12.Nxe5 dxe5 13.Nc4 Nxe4 14.Nxe5 Qxd1 15.Rxd1 Bd6 16.Nc4 Bc5 17.Be3 Rad8 18.Rxd8 Rxd8 
19.Ne5 Bxe3 20.Bxf7+ Kh8 21.fxe3 Rd2 22.Rf1 Ng3 23.hxg3 Rxg2+ 24.Kh1 Rf2+ 25.Kg1 Rg2+ 26.Kh1 Rf2+ 
27.Kg1 Rg2+ 1/2-1/2

```

## Forum Posts

- [New version 0.2.1 of BremboCE](https://www.stmintz.com/ccc/index.php?id=217811) by [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"), [CCC](CCC "CCC"), March 14, 2002
- [Improved chess applet bremboce](http://www.talkchess.com/forum/viewtopic.php?t=29473) by [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"), [CCC](CCC "CCC"), August 20, 2009
- [Released Bremboce 0.6 Java winboard engine](http://www.talkchess.com/forum/viewtopic.php?t=29488) by [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"), [CCC](CCC "CCC"), August 21, 2009
- [Released Bremboce 0.6.2 Java winboard engine](http://www.talkchess.com/forum/viewtopic.php?t=29970) by [Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana"), [CCC](CCC "CCC"), October 03, 2009

## External Links

## Chess Engine

- [BremboCE | Download the winboard chess engine version](https://web.archive.org/web/20180821045818/http://bremboce.cisana.com/download_en.php) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [BremboCE | Features](https://web.archive.org/web/20180728123136/http://bremboce.cisana.com/features_en.php) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Index of /chess/engines/Jim Ablett/BREMBO CE](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/BREMBO%20CE/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Strong Java Chess Engines Game - Browse /chess_engines_nb-src at SourceForge.net](https://sourceforge.net/projects/sjce/files/chess_engines_nb-src/)
- [Bremboce 0.6.2](http://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Bremboce%200.6.2) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [Brembo (river) from Wikipedia](https://en.wikipedia.org/wiki/Brembo_%28river%29)
- [Val Brembana from Wikipedia](https://en.wikipedia.org/wiki/Val_Brembana)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Brembo (river)](https://en.wikipedia.org/wiki/Brembo_%28river%29), Image by Cruccone, September 18, 2005, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [BremboCE | Download the winboard chess engine version](https://web.archive.org/web/20180821045818/http://bremboce.cisana.com/download_en.php) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Chess Computer Cup 4 - Photo Gallerie 2](http://www.scaccomasco.com/foto/2009/CCC4_8-nov/album/index.html) (dead link, March 06, 2020)

**[Up one Level](Engines "Engines")**

