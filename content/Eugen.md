---
title: Eugen
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Eugen**

**Eugen**,

a chess program developed by [Eugenio Castillo Jiménez](Eugenio_Castillo_Jim%C3%A9nez "Eugenio Castillo Jiménez") to run under [MS-DOS](MS-DOS "MS-DOS"). Eugen participated at the [WMCCC 1996](WMCCC_1996 "WMCCC 1996") in [Jakarta](https://en.wikipedia.org/wiki/Jakarta), the [WMCCC 1997](WMCCC_1997 "WMCCC 1997") in [Paris](https://en.wikipedia.org/wiki/Paris) and the [WCCC 1999](WCCC_1999 "WCCC 1999") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn). Further, Eugen played various [Spanish Computer Chess Championships](Spanish_Computer_Chess_Championship "Spanish Computer Chess Championship"), and won the [SCCC 1996](SCCC_1996 "SCCC 1996") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
According to Eugenio <a id="cite-note-3" href="#cite-ref-3">[3]</a>, Eugen was partially inspired by [open source programs](Category:Open_Source "Category:Open Source") like [Turbo Chess](Turbo_Chess "Turbo Chess"), [GNU Chess](GNU_Chess "GNU Chess"), and [Crafty](Crafty "Crafty"). It used 16 bit [attacktables](Attack_and_Defend_Maps "Attack and Defend Maps") which were [incrementally updated](Incremental_Updates "Incremental Updates") in every [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move"), the [search](Search "Search") uses [iterative deepening](Iterative_Deepening "Iterative Deepening"), and [recursive nullmove](Null_Move_Pruning "Null Move Pruning") ([R](Depth_Reduction_R "Depth Reduction R")=2). [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), who for a short time worked with Eugenio on a computer chess project, mentioned Eugen had a good implementation of the [null-move quiescence](Null_Move_Pruning#NMQS "Null Move Pruning") algorithm <a id="cite-note-4" href="#cite-ref-4">[4]</a>, based on the ideas and publications by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 Descriptions](#descriptions)
  - [1.1 1997](#1997)
  - [1.2 1999](#1999)
- [2 Selected Games](#selected-games)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engin](#chess-engin)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Descriptions

given on the [ICGA](ICGA "ICGA") tournament page <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

## 1997

```
Eugen 7.2 is a program based on a hard selective search [extensions](Extensions "Extensions") algorithm, he don't makes conventional [alpha beta](Alpha-Beta "Alpha-Beta") pruning and he (in Spanish it's he) uses a special [null turn moves](Null_Move_Pruning#NMQS "Null Move Pruning") in [quiescence search](Quiescence_Search "Quiescence Search"). The program consist of about 40.000 [C](C "C") and [assembler](Assembly "Assembly") code lines. Node speed on a [Pentium](X86 "X86") 133Mhz is approximately 12.000 to 30.000 [nodes per second](Nodes_per_Second "Nodes per Second"). Chess programming is my hobby-job for about last 8 years. Currently [Spanish CCC](SCCC_1996 "SCCC 1996"). 

```

## 1999

```
Eugen born in 1994 like a personal free time project, initially written in [Pascal](Pascal "Pascal") and assembler, in 1995 it was changed to C language. Eugen is partially inspirated in freeware programs like [Turbo Chess](Turbo_Chess "Turbo Chess"), [Gnu](GNU_Chess "GNU Chess"), and [Crafty](Crafty "Crafty"). 

```

## Selected Games

[WMCCC 1997](WMCCC_1997 "WMCCC 1997"), round 1, Eugen 7.2 - [Junior](Junior "Junior") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

```

[Event "WMCCC 1997"]
[Site "Paris, France"]
[Date "1997.10.26"]
[Round "1"]
[White "Eugen 7.2"]
[Black "Junior"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 Qc7 9.O-O-O Nbd7 
10.g4 b5 11.Bxf6 Nxf6 12.g5 Nd7 13.f5 Nc5 14.f6 b4 15.Ncb5 axb5 16.Nxb5 Qc6 17.fxe7 Nb7 
18.Nd4 Qc5 19.Bb5+ Kxe7 20.e5 d5 21.Rhf1 Nd8 22.Kb1 Qa7 23.Nc6+ Nxc6 24.Bxc6 Qxa2+ 25.Kc1 
Ra7 26.Qf2 Qa5 27.Bxd5 Qa1+ 28.Kd2 Qa5 29.Ke1 Rf8 30.Be4 Rd7 31.Rxd7+ Bxd7 32.Qd4 Rd8 
33.Qd6+ Ke8 34.Kf2 Ba4 35.Bc6+ Bxc6 36.Qxc6+ Kf8 37.Qe4 b3 38.cxb3 Qd2+ 39.Kg1 Qxg5+ 
40.Kh1 Qd2 41.Qxh7 Qd5+ 42.Kg1 Qc5+ 43.Kh1 Qxe5 44.Qh8+ Ke7 45.Rxf7+ Kxf7 46.Qxd8 Qe4+ 
47.Kg1 Qb1+ 48.Kg2 Qxb2+ 49.Kh1 Qxb3 50.Qd7+ Kg6 51.Qe8+ Kg5 52.Qd8+ Kg4 53.Qd4+ Kf3 
54.Qxg7 Qd1+ 55.Qg1 Qd5 56.h4 Qf5 57.Qg2+ 1/2-1/2 

```

## Forum Posts

- [Goliath vs. Eugen](https://www.stmintz.com/ccc/index.php?id=11369) by [Howard Exner](index.php?title=Howard_Exner&action=edit&redlink=1 "Howard Exner (page does not exist)"), [CCC](CCC "CCC"), October 30, 1997
- [Eugen 7.5](https://www.stmintz.com/ccc/index.php?id=26806) by [Gabriele Müller](Gabriele_M%C3%BCller "Gabriele Müller"), [CCC](CCC "CCC"), September 16, 1998
- [Re: Many News, see the WinBoard News Ticker !](http://www.open-aurec.com/wbforum/viewtopic.php?t=30370#p115506) by Pete Galati, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 27, 1999

## External Links

## Chess Engin

- [Eugen's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=28)

## Misc

- [Eugene (given name) from Wikipedia](<https://en.wikipedia.org/wiki/Eugene_(given_name)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Spanje CCC 1996](http://www.csvn.nl/index.php?option=com_content&view=article&id=209%3Aspanje-ccc-1996&catid=19%3Acomputer-computer&Itemid=48&lang=en), [CSVN](CSVN "CSVN") tournament site
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Eugenio Castillo Jiménez](Eugenio_Castillo_Jim%C3%A9nez "Eugenio Castillo Jiménez") (**1997**). *The Spanish Computer-Chess Championship*. [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Meet the Authors](http://www.rebel.nl/authors.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: List is NOT a Crafty clone, ... etc](https://www.stmintz.com/ccc/index.php?id=383312) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), August 21, 2004
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), a revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, edited version in (**1999**). *The Nature of MINIMAX Search*. Ph.D. thesis, IKAT, Chapter 10, pp. 101-116
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Eugen's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=28)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Paris 1997 - Chess - Round 1 - Game 7 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=5&round=1&id=7)

**[Up one level](Engines "Engines")**

