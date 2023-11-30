---
title: Green Light Chess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Green Light Chess**

\[ [Emerald green](https://en.wikipedia.org/wiki/Shades_of_green#Emerald) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Green Light Chess**, (Green Light, GLChess <a id="cite-note-2" href="#cite-ref-2">[2]</a>)

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Tim Foden](Tim_Foden "Tim Foden"), written in [C++](Cpp "Cpp"), version 2.09 relying on an own 32-bit [Windows](Windows "Windows") [GUI](GUI "GUI") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Description

Green Light started its life in early 1997 as [0x88](0x88 "0x88") engine, and since version 2.xx evolved to [bitboards](Bitboards "Bitboards") with an [8x8 board](8x8_Board "8x8 Board").
It applies [Alpha-Beta](Alpha-Beta "Alpha-Beta") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [fractional ply](Depth#FractionalPlies "Depth") [extensions](Extensions "Extensions"), [transposition table](Transposition_Table "Transposition Table"), [null move reductions](Null_Move_Reductions "Null Move Reductions"), [razoring](Razoring "Razoring"), and [pruning](Pruning "Pruning") in [quiescence search](Quiescence_Search "Quiescence Search") based on [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation").
In version 2.14, [TD-λ](Temporal_Difference_Learning#TDLamba "Temporal Difference Learning") learning was implemented which required [milli-pawn values](Millipawns "Millipawns") rather than [centi-pawn values](Centipawns "Centipawns").
The well maintained 2.18 change log gives a decent overview of features, modifications and bugfixes within the engine development, its GUI and WinBoard implementations <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Tournament Play

Green Light Chess felt well in the green-light flooded cave in [Graz](https://en.wikipedia.org/wiki/Graz) and played a strong [WCCC 2003](WCCC_2003 "WCCC 2003") with a respectable fifth place and 6 points out of 11, and further played the [CCT6](CCT6 "CCT6") with 5½ out of 9.

## Selected Games

[WCCC 2003](WCCC_2003 "WCCC 2003"), round 5, Green Light - [Falcon](Falcon "Falcon") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```
[Event "WCCC 2003"]
[Site "Graz, Austria"]
[Date "2003.11.25"]
[Round "5"]
[White "Green Light"]
[Black "Falcon"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Qxd4 a6 5.Qe3 Nc6 6.Nc3 Nf6 7.Bd2 Ng4 8.Qe2 g6 
9.h3 Nge5 10.Nxe5 dxe5 11.O-O-O Nd4 12.Qc4 Be6 13.Qb4 Bd7 14.Be3 e6 15.Qc4 
Rc8 16.Qd3 Bc5 17.f4 f6 18.fxe5 fxe5 19.h4 O-O 20.h5 Be8 21.Bd2 Bb4 22.hxg6 
Bxg6 23.Qe3 Qa5 24.Kb1 Qb6 25.Rh6 Rc7 26.Qg3 Rg7 27.Qe3 Ba3 28.Na4 Qc6 
29.Nc3 Bc5 30.Qh3 b5 31.Bd3 b4 32.Ne2 Nxe2 33.Bxe2 Rf2 34.Bd3 a5 35.Be1 Rf8 
36.Bg3 Be3 37.Rh4 Bd4 38.Rg4 Qc5 39.Rg5 Re8 40.Rh1 Qc7 41.Qh2 Ra8 42.Bxe5 
Bxe5 43.Qxe5 Qxe5 44.Rxe5 Bf7 45.Rg1 Rg3 46.Be2 Kh8 47.Bf3 Rag8 48.Rc1 R3g5 
49.Rxg5 Rxg5 50.c3 bxc3 51.Rxc3 Kg7 52.Kc2 Kf6 53.Kd3 Bh5 54.Bxh5 Rxh5 
55.Kd4 Rg5 56.g3 Rb5 57.b3 Rg5 58.Re3 Rg8 59.e5+ Kf5 60.a3 Rd8+ 61.Kc5 Rd1 
62.Kb6 Rd5 63.b4 axb4 64.axb4 Rd1 65.b5 h5 66.Kb7 h4 67.gxh4 Rh1 68.b6 Rxh4 
69.Rb3 Kxe5 70.Kc6 Rc4+ 71.Kd7 Rh4 72.b7 Rh8 73.b8=Q+ Rxb8 1-0 

```

## Forum Posts

- [Version 2.11 of Green Light Chess released; web page moved](https://www.stmintz.com/ccc/index.php?id=141909) by [Tim Foden](Tim_Foden "Tim Foden"), [CCC](CCC "CCC"), November 29, 2000
- [Green Light Chess v2.15 now released](https://www.stmintz.com/ccc/index.php?id=192394) by [Tim Foden](Tim_Foden "Tim Foden"), [CCC](CCC "CCC"), October 08, 2001
- [GLC and others when using wb2uci](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48455) by [Odd Gunnar Malin](Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 03, 2004 » [Wb2UCI](Wb2UCI "Wb2UCI")
- [Comet B15, Amy 0.6 Green Light Chess 2.07a available ...](http://www.talkchess.com/forum/viewtopic.php?t=32361) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), February 04, 2010 » [Comet](Comet "Comet"), [Amy](Amy "Amy")

## External Links

## Chess Engine

- [Green Light Chess](http://www.7sun.com/chess/index.php)
- [Green Light (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/program.php?id=119)
- [Index of /chess/engines/Norbert's collection/Green Light Chess (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Green%20Light%20Chess%20%28Compilation%29/) compiled by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Green Light Chess 3.01.2.2](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Green%20Light%20Chess%203.01.2.2#Green_Light_Chess_3_01_2_2) in [CCRL 40/40](CCRL "CCRL")
- [Green Light Chess 3.01.2.2](https://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Green%20Light%20Chess%203.01.2.2#Green_Light_Chess_3_01_2_2) in [CCRL 40/4](CCRL "CCRL")
- [Green Light Chess 3.00](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Green%20Light%20Chess%203.00) in [KCEC](KCEC "KCEC")

## Misc

- [Green Light (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Green_Light)
- [Green-light from Wikipedia](https://en.wikipedia.org/wiki/Green-light)

[Fishing light attractor from Wikipedia](https://en.wikipedia.org/wiki/Fishing_light_attractor)

- [Green Light Trust from Wikipedia](https://en.wikipedia.org/wiki/Green_Light_Trust)
- [Green fireballs from Wikipedia](https://en.wikipedia.org/wiki/Green_fireballs)
- [Green flash from Wikipedia](https://en.wikipedia.org/wiki/Green_flash)
- [Green (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Green_%28disambiguation%29)
- [Green (color) from Wikipedia](https://en.wikipedia.org/wiki/Green)
- [Shades of green from Wikipedia](https://en.wikipedia.org/wiki/Shades_of_green)
- [Light from Wikipedia](https://en.wikipedia.org/wiki/Light)
- [Electromagnetic spectrum from Wikipedia](https://en.wikipedia.org/wiki/Electromagnetic_spectrum)
- [Aurora (astronomy) from Wikipedia](https://en.wikipedia.org/wiki/Aurora_%28astronomy%29) <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## \[ References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The [Gachala Emerald](https://en.wikipedia.org/wiki/Gachal%C3%A1_Emerald) from the [National Museum of Natural History](https://en.wikipedia.org/wiki/National_Museum_of_Natural_History), [Washington, D.C.](https://en.wikipedia.org/wiki/Washington,_D.C.), [Shades of green from Wikipedia](https://en.wikipedia.org/wiki/Shades_of_green)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> not to be confused with the [glChess](index.php?title=GlChess&action=edit&redlink=1 "GlChess (page does not exist)") [GUI](GUI "GUI")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Green Light Chess - WIN32 GUI](http://www.7sun.com/chess/oldversions/218/index.php#win32-gui)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [changes.txt](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Green%20Light%20Chess%20%28Compilation%29/v2.18/changes.txt)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Graz 2003 - Chess - Round 5 - Game 7 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=2&round=5&id=7)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> The [Aurora Borealis](https://en.wikipedia.org/wiki/Aurora_%28astronomy%29), or Northern Lights, shines above [Bear Lake](https://en.wikipedia.org/wiki/Bear_Lake_%28Alaska%29), [Eielson Air Force Base](https://en.wikipedia.org/wiki/Eielson_Air_Force_Base), [Alaska](https://en.wikipedia.org/wiki/Alaska), January 18, 2005, [United States Air Force](https://en.wikipedia.org/wiki/United_States_Air_Force) photo by Senior Airman Joshua Strang
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [The Aurora Distributed Shared Data System](http://webdocs.cs.ualberta.ca/%7Epaullu/Aurora/aurora.html) by [Paul Lu](Paul_Lu "Paul Lu")

**[Up one level](Engines "Engines")**

