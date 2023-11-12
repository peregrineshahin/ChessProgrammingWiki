---
title: Cheiron
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cheiron**

\[ [Cheiron](https://de.wikipedia.org/wiki/Cheiron) and [Achilles](https://en.wikipedia.org/wiki/Achilles) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cheiron**,

a chess program by [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"). [Cheiron](https://de.wikipedia.org/wiki/Cheiron) is the German spelling of [Chiron](https://en.wikipedia.org/wiki/Chiron), a [centaur](https://en.wikipedia.org/wiki/Centaur) creature of the [Greek mythology](https://en.wikipedia.org/wiki/Greek_mythology). The program played the [8th World Computer Chess Championship 1995](WCCC_1995 "WCCC 1995") in [Shatin](https://en.wikipedia.org/wiki/Sha_Tin), [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong) and the [13th World Microcomputer Chess Championship 1995](WMCCC_1995 "WMCCC 1995") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn), the [IPCCC 1994](IPCCC_1994 "IPCCC 1994") and [IPCCC 1997](IPCCC_1997 "IPCCC 1997"), and the [Aegon 1996](Aegon_1996 "Aegon 1996") and [Aegon 1997](Aegon_1997 "Aegon 1997") man-machine tournaments.

## Contents

- [1 Description](#description)
- [2 Selected Games](#selected-games)
  - [2.1 WCCC 1995](#wccc-1995)
  - [2.2 Aegon 1996](#aegon-1996)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
  - [5.1 Chess Program](#chess-program)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Description

from the [ICGA](ICGA "ICGA")-site <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```C++
In [Greek mythology](https://en.wikipedia.org/wiki/Greek_mythology), [Cheiron](https://en.wikipedia.org/wiki/Chiron) was the wisest of all [centaurs](https://en.wikipedia.org/wiki/Centaur) and the teacher of many heroes. The program Cheiron is written in [C](C "C"). It is an [alpha-beta](Alpha-Beta "Alpha-Beta") program using most of the known state-of-the-art heuristics including [killer heuristics](Killer_Heuristic "Killer Heuristic"), [transposition table](Transposition_Table "Transposition Table"), [aspiration search](Aspiration_Windows "Aspiration Windows"), plausible [move ordering](Move_Ordering "Move Ordering"), [iterative deepening](Iterative_Deepening "Iterative Deepening"), [selective deepening](Extensions "Extensions") etc. [Null moves](Null_Move_Pruning "Null Move Pruning"), however, are not used. The [quiescence search](Quiescence_Search "Quiescence Search") is quite large and examines some tactical motifs, particularly [mating](Checkmate "Checkmate") and [promotion](Promotions "Promotions") threats. 

```

```C++
Apart from the [move generator](Move_Generation "Move Generation"), the [evaluation function](Evaluation_Function "Evaluation Function") is the most expensive part of the program. It examines the [pawn structure](Pawn_Structure "Pawn Structure"), [king's security](King_Safety "King Safety"), static positions of the pieces, [everlasting knights](Outposts "Outposts") etc. as well as special situations in the [endgame](Endgame "Endgame") (e.g. there are positions when two pawns are more worth than a rook). 

```

```C++
On a [Pentium](X86 "X86") 90MHz the program will search about 10,000 [nodes per second](Nodes_per_Second "Nodes per Second"). Cheiron is more a [positional](Strategy "Strategy") playing than a [tactical](Tactics "Tactics") playing program. Cheiron uses an [opening book](Opening_Book "Opening Book") containing about 12,000 positions to get a good start into the game. Using the [Bednorz-Toennissen test](index.php?title=BT-Test&action=edit&redlink=1 "BT-Test (page does not exist)"), Cheiron has an estimated rating of 2100 ELO on a 50MHz [PC](IBM_PC "IBM PC"). Tournament results against humans supports this number. Originally, the program was developed for [Unix](Unix "Unix") boxes, but a version has been developed with a [graphical interface](GUI "GUI") using [Turbo C](C "C") in a [DOS](MS-DOS "MS-DOS")-[Windows 3.1](Windows "Windows") environment. 

```

## Selected Games

## WCCC 1995

[WCCC 1995](WCCC_1995 "WCCC 1995"), round 1, [Gandalf](Gandalf "Gandalf") - Cheiron <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "WCCC 1995"]
[Site "Shatin, Hong Kong"]
[Date "1995.05.25"]
[Round "1"]
[White "Gandalf"]
[Black "Cheiron"]
[Result "0-1"]

1.e4 e6 2.d4 c5 3.Nf3 cxd4 4.Nxd4 Nf6 5.Bd3 Be7 6.O-O Nc6 7.Be3 O-O 8.Nc3 d6 9.Nxc6 bxc6 10.f3 d5 
11.e5 d4 12.exf6 Bxf6 13.Bxd4 Qxd4+ 14.Kh1 Rb8 15.Rb1 Rd8 16.Qe2 Bb7 17.a3 Be5 18.Rfe1 Bc7 19.Qe4 
Qxe4 20.Nxe4 Rd5 21.g3 c5 22.Kg2 Rbd8 23.h3 Bb6 24.b3 Rd4 25.Re3 R4d7 26.Re2 Rd5 27.Bc4 Rd1 28.Rxd1 
Rxd1 29.h4 g6 30.Kf2 Kf8 31.Re1 Rxe1 32.Kxe1 Ke7 33.g4 f5 34.Ng5 h6 35.Nxe6 Bxf3 36.gxf5 gxf5 37.c3 
Kd6 38.Kd2 Bd5 39.Bxd5 Kxd5 40.Nf4+ Ke4 41.Nd3 f4 42.h5 c4 43.bxc4 Be3+ 44.Kc2 f3 45.a4 f2 46.Nxf2+ 
Bxf2 47.a5 0-1 

```

## Aegon 1996

[Aegon 1996](Aegon_1996 "Aegon 1996"), round 4, Cheiron - [Sofia Polgár](https://en.wikipedia.org/wiki/Sofia_Polg%C3%A1r) <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "AEGON 1996"]
[Site "The Hague NED"]
[Date "1996.04.15"]
[Round "4"]
[White "Cheiron"]
[Black "Sofia Polgar"]
[Result "1/2-1/2"]

1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 Bg4 6.Be2 e6 7.O-O Nc6 8.Be3 cxd4 9.cxd4 Bb4 10.Nc3 Qd6 
11.a3 Ba5 12.Nb5 Qb8 13.h3 Bh5 14.g4 Bg6 15.Qc1 Nd5 16.Nh4 Bd8 17.g5 Nce7 18.Nc3 O-O 19.Nxg6 hxg6 
20.Nxd5 Nxd5 21.Bf3 Qd6 22.Qc5 Qd7 23.Rac1 Bb6 24.Qc4 Qd6 25.Bxd5 exd5 26.Qb5 Rfe8 27.Rfd1 Bc7 28.Kf1 
Bb6 29.Re1 Re4 30.Kg2 Qe6 31.Rh1 Re8 32.Qd3 Qf5 33.Qd2 Kh7 34.a4 Rh4 35.f4 f6 36.gxf6 Qxf6 37.Qf2 Re4 
38.Rhd1 Bd8 39.Rd3 Qf5 40.Qg3 g5 41.fxg5 Reg4 42.hxg4 Rxg4 43.Qxg4 Qxg4+ 44.Kf2 Qh4+ 45.Ke2 Qh2+ 
46.Bf2 Qh5+ 47.Kf1 Qh1+ 48.Bg1 Kg6 49.Rg3 Qe4 50.Re1 Qf5+ 51.Bf2 Bc7 52.Rge3 1/2-1/2

```

## See also

- [Achilles](Achilles "Achilles")
- [Centaur](Centaur "Centaur")
- [Chiron](Chiron "Chiron")

## Forum Posts

- [AEGON 1997 breakdown of opponents from their webpage](https://groups.google.com/d/msg/rec.games.chess.misc/7fcqu7_2Rr4/WR5IijMqDF0J) by Lonnie, [rgcm](Computer_Chess_Forums "Computer Chess Forums"), April 11, 1997 » [Aegon 1997](Aegon_1997 "Aegon 1997")

## External Links

## Chess Program

- [Cheiron's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=188)
- [Comp Cheiron chess games - 365Chess.com](https://www.365chess.com/players/Comp_Cheiron)

## Misc

- [Cheiron – Wikipedia.de](https://de.wikipedia.org/wiki/Cheiron) (German)
- [Chiron (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Chiron_(disambiguation)>)
- [Chiron from Wikipedia](https://en.wikipedia.org/wiki/Chiron)
- [Category:Chiron - Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Chiron?uselang=en)
- [Corvus Corax](<https://en.wikipedia.org/wiki/Corvus_Corax_(band)>) - [Cheiron](https://www.discogs.com/de/composition/3ea755eb-36be-4fcb-aee8-dd4714e85497-Cheiron), April 14, 2019 at [Moscow](https://en.wikipedia.org/wiki/Moscow) [Station Hall](https://station-hall.ru/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [fresco](https://en.wikipedia.org/wiki/Fresco) shows the [centaur](https://en.wikipedia.org/wiki/Centaur) [Chiron](https://en.wikipedia.org/wiki/Chiron), pedagogue of [Achilles](https://en.wikipedia.org/wiki/Achilles), who teaches the still young man the use of the [cithara](https://en.wikipedia.org/wiki/Cithara). The prototype for this fresco was not another painting but a statue that [Pliny the Elder](https://en.wikipedia.org/wiki/Pliny_the_Elder) remembered was exhibited in [Rome](https://en.wikipedia.org/wiki/Rome) in [Saepta Julia](https://en.wikipedia.org/wiki/Saepta_Julia). [National Archaeological Museum, Naples (inv. Nr. 9109)](https://en.wikipedia.org/wiki/National_Archaeological_Museum,_Naples), from [Herculaneum](https://en.wikipedia.org/wiki/Herculaneum), [Augusteum](https://en.wikipedia.org/wiki/Augusteum) - [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Cheiron's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=188)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Shatin 1995 - Chess - Round 1 - Game 5 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=1&id=5)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Aegon round 4](https://groups.google.com/d/msg/rec.games.chess.misc/X06MxKpsLJ4/0wuwy6054VEJ) by Alastair Scott, [rgcm](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1996

**[Up one Level](Engines "Engines")**

