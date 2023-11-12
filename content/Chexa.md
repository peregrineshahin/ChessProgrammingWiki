---
title: Chexa
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chexa**

\[ A pile of Chex Mix <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chexa**,

a private [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Mauro Riccardi](Mauro_Riccardi "Mauro Riccardi"), written in [C](C "C") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Chexa played the [CCC 2008](CCC_2008 "CCC 2008") and [CCC 2009](CCC_2009 "CCC 2009") Italian Chess Computer Cups, the [IOCSC 2010](IOCSC_2010 "IOCSC 2010") and [IOCSC 2012](IOCSC_2012 "IOCSC 2012") Italian Open Chess Software Cups, the [CCT15](CCT15 "CCT15"), and won the [IGT 2013](IGT_2013 "IGT 2013") of original engines.
As stated on Chexa's G 6 site, beside working on a [parallel search](Parallel_Search "Parallel Search") based on the [publish–subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern),
Mauro Riccardi is in the process to find the right balance of [passed pawn](Passed_Pawn "Passed Pawn") and [candidate](Candidate_Passed_Pawn "Candidate Passed Pawn") values, since too often Chexa has overestimated their good locations, and is about to introduce a table to evaluate [pawn islands](Pawn_Islands "Pawn Islands") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Photos & Games

## CCC 2009

[](File:CCC2009ChexaBremboCE.jpg)
[Gianluca Cisana](Gianluca_Cisana "Gianluca Cisana") and [Mauro Riccardi](Mauro_Riccardi "Mauro Riccardi") in front, organizer [Giuseppe Sgrò](index.php?title=Giuseppe_Sgr%C3%B2&action=edit&redlink=1 "Giuseppe Sgrò (page does not exist)") addresses the audience <a id="cite-note-4" href="#cite-ref-4">[4]</a>

[CCC 2009](CCC_2009 "CCC 2009"), round 2, Chexa - [BremboCE](BremboCE "BremboCE")

```

[Event "Computer Chess Cup 4"]
[Site "Carugate"]
[Date "2009.11.07"]
[Round "2"]
[White "Chexa 0.2"]
[Black "BremboCE 0.6.2"]
[Result "1-0"]

1.c4 e6 2.Nc3 d5 3.d4 Nf6 4.Nf3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 g5 8.Bg3 Bb4 9.Nd2 Bxc3 
10.bxc3 h5 11.h4 g4 12.cxd5 exd5 13.Bd3 Nc6 14.O-O Re8 15. Qc2 b6 16.a3 Bb7 17.c4 Na5 
18.Rab1 c5 19.dxc5 bxc5 20.Rb5 dxc4 21.Nxc4 Nxc4 22.Bxc4 Be4 23.Qc3 Bg6 24.f3 gxf3 
25.gxf3 Qe7 26.e4 Rec8 27.Qd2 Qd7 28.Qd6 Qxd6 29.Bxd6 a6 30.Rb6 Nd7 31.Rb7 Nf6 32.Be5 
Rc6 33.Rd1 Re8 34.Bg3 Kf8 35.Bf4 Rec8 36.Ra7 Rb6 37.Bxa6 Re8 38.Be3 Kg8 39.Bxc5 Rc6 
40.Bb4 Rb6 41.Bc4 Reb8 42.Rd4 Rc6 43.Bd2 Rb2 44.Rd8+ Kg7 45.Bf1 Rcc2 46.Be1 Rb1 47.Bd2 
Rbb2 48.Bf4 Rb1 49.Rd3 Rc5 50.a4 Rc8 51.a5 Rc6 52.Rd2 Rcc1 53.Rf2 Rc5 54.a6 Ra5 55.Kg2 
Kh7 56.Bg5 Ng8 57.Be3 Nf6 58.Bd4 Ne8 59.Rd2 Ng7 60.Bd3 Rb3 61.Bc4 Rba3 62.Bb2 R3a4 
63.Bf1 Ne6 64.Ra8 Kh6 65.Rd7 Ra2 66.Rh8+ Bh7 67.Rb8 Kg6 68.Rb6 Bg8 69.Bc4 R2a4 70.Bxe6 
fxe6 71.Rg7+ Kh6 72.Rxg8 Rd4 73.Bxd4 Ra2+ 74.Kg3 Rxa6 75.Rxa6 Kh7 76.Rg7+ Kh6 77.Rxe6# 
1-0

```

## CCT15

[CCT15](CCT15 "CCT15"), round 4, [ProChess](ProChess_IT "ProChess IT") - Chexa

```

[Event "CCT15"]
[Site "Variant-ICS, Amsterdam, NL"]
[Date "2013.02.23"]
[Round "4"]
[White "ProChess"]
[Black "Chexa"]
[Result "0-1"]

1.d4 e6 2.e4 d5 3.e5 c5 4.c3 Nc6 5.Nf3 Nh6 6.Bxh6 gxh6 7.Be2 Qb6 8.Qd2 Bd7 9.O-O Bg7 
10.Re1 O-O-O 11.Na3 cxd4 12.cxd4 Bf8 13.Nb5 Rg8 14.Red1 Kb8 15.Nd6 Bxd6 16.exd6 f6 
17.a4 Be8 18.Qxh6 Bg6 19.Bb5 Be4 20.Ra3 Rg6 21.Qd2 Rxd6 22.Nh4 Rg7 23.f3 Bg6 24.Nxg6 
hxg6 25.Bxc6 Rxc6 26.f4 Rgc7 27.a5 Qb5 28.Rh3 Rc8 29.b3 Rc2 30.Qe3 Qxa5 31.Rg3 Qa3 
32.h3 Qd6 33.Rxg6 R2c3 34.Qd2 Qc7 35.Re1 Rxb3 36.Rxf6 Rxh3 37.Rfxe6 Rh4 38.g3 Rhh8 
39.Re7 Qc3 40.Qxc3 Rxc3 41.Rg7 Rc7 42.Ree7 Rxe7 43.Rxe7 a5 44.Rd7 a4 45.Rxd5 Rh6 
46.Ra5 Ra6 47.Re5 a3 48.Re8+ Kc7 49.Re7+ Kd8 50.Re1 a2 51.Kf2 b5 52.Ra1 b4 53.Ke3 b3 
54.Kd2 Rc6 55.d5 Rc8 56.Ke3 b2 57.Rxa2 b1=Q 58.Ra6 Rc3+ 59.Kd4 Qd3+ 60.Ke5 Qxa6 
61.g4 Qd3 0-1

```

## See also

- [Vanilla Chess](Vanilla_Chess "Vanilla Chess")

## Forum Posts

- [Re: calling eval() at all depths in the search tree?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=34109&start=8) by [yoshiharu](Mauro_Riccardi "Mauro Riccardi"), [CCC](CCC "CCC"), May 06, 2010

## External Links

## Chess Engine

- [Chexa « G 6](http://www.g-sei.org/chexa/)

## Misc

- [CHEX from Wikipedia](https://en.wikipedia.org/wiki/CHEX)
- [Chex from Wikipedia](https://en.wikipedia.org/wiki/Chex)
- [Chex Mix from Wikipedia](https://en.wikipedia.org/wiki/Chex_Mix)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chex Mix](https://en.wikipedia.org/wiki/Chex_Mix) Photo by [Evan-Amos](https://commons.wikimedia.org/wiki/User:Evan-Amos), November 20, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Private Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:private_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chexa « G 6](http://www.g-sei.org/chexa/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Computer Cup 4 - Photo Gallerie 1](http://www.scaccomasco.com/foto/2009/CCC4-7_nov/album/index.html) (no longer available)

**[Up one level](Engines "Engines")**

