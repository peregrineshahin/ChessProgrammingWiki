---
title: GridGinkgo
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GridGinkgo**

\[ Grid of Ginkgo trees in Tokyo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GridGinkgo**,

a [grid computing](https://en.wikipedia.org/wiki/Grid_computing) [cluster](https://en.wikipedia.org/wiki/Computer_cluster) chess program by [Kai Himstedt](Kai_Himstedt "Kai Himstedt") incorporating [Ginkgo](Ginkgo "Ginkgo") by [Frank Schneider](Frank_Schneider "Frank Schneider") as primary search engine, and [Crafty](Crafty "Crafty") by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") as proxy engine, which performs no tree search but has a role to control the optimistic [pondering](Pondering "Pondering") <a id="cite-note-2" href="#cite-ref-2">[2]</a> with distributed worker clients <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Supported by [Timo Haupt](Timo_Haupt "Timo Haupt"), GridGinkgo played the [WCCC 2016](WCCC_2016 "WCCC 2016") in [Leiden](https://en.wikipedia.org/wiki/Leiden) on a cluster of 30 [Intel](Intel "Intel") and [AMD](AMD "AMD") [x86-64](X86-64 "X86-64") PCs with 224 processor cores, and came in fourth with 4/10 in that extraordinary strong field. At the [WCCC 2018](WCCC_2018 "WCCC 2018") in [Stockholm](https://en.wikipedia.org/wiki/Stockholm), GridGinkgo became runner-up, losing the play-off versus [Komodo](Komodo "Komodo").

## Contents

- [1 Photos & Games](#photos-.26-games)
  - [1.1 GridGinkgo - Shredder](#gridginkgo---shredder)
  - [1.2 GridGinkgo - Komodo](#gridginkgo---komodo)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 External Links](#external-links)
  - [4.1 Grid](#grid)
  - [4.2 Ginkgo](#ginkgo)
- [5 References](#references)

## Photos & Games

<a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## GridGinkgo - Shredder

[](File:WCCC2016_R3GridGinkGoShredder.jpg)
[WCCC 2016](WCCC_2016 "WCCC 2016"), round 3, GridGinkgo team facing [Shredder](Shredder "Shredder"), [Kai Himstedt](Kai_Himstedt "Kai Himstedt") and [Timo Haupt](Timo_Haupt "Timo Haupt")

```

[Event "WCCC 2016"]
[Site "Leiden"]
[Date "2016.06.28"]
[Round "3"]
[White "GridGinkgo"]
[Black "Shredder"]
[Result "0-1"]

1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3 Bf5 5.cxd5 cxd5 6.Qb3 Qc7 7.Nc3 e6 8.Nh4 Bg6 9.Nxg6 hxg6
10.Bd2 Nc6 11.h3 Be7 12.Bd3 Rc8 13.Ne2 g5 14.Rg1 Bd6 15.f3 O-O 16.Rc1 Qe7 17.Kf2 a6 18.Rgd1
e5 19.dxe5 Nxe5 20.Rxc8 Rxc8 21.Rc1 Bc5 22.Nd4 b5 23.Qc2 Rc7 24.b3 g6 25.Bf1 g4 26.Qb1 gxh3
27.gxh3 Nh5 28.Bg2 Qh4+ 29.Kf1 Ng3+ 30.Kg1 Bxd4 31.Rxc7 Nf5 32.exd4 Qxd4+ 33.Kh1 Qxd2 34.Rc2
Ng3+ 35.Kh2 Qf4 36.Qc1 Nf1+ 37.Kg1 Ne3 38.Qd2 d4 39.Rc8+ Kg7 40.Re8 Qg5 41.Kh1 Qg3 42.Qe2 Kh7
43.Qd2 Nd3 44.Rxe3 Nf2+ 45.Kg1 Nxh3+ 46.Kh1 Qf2 47.Qxf2 Nxf2+ 48.Kg1 dxe3 49.Bf1 Nd1 50.a3 Nc3
51.Bd3 Kh6 52.Kf1 Kg5 53.Kg1 Kf4 54.Kg2 f5 55.a4 g5 56.axb5 axb5 57.Bf1 e2 58.Bxe2 Nxe2 59.Kf2
Nd4 60.Kg2 Nxf3 61.Kf2 Ne5 62.Ke2 g4 63.Kf2 g3+ 64.Kg2 Kg4 65.Kf1 Kf3 66.Ke1 Nd3+ 67.Kf1 g2+
68.Kg1 Nf4 69.b4 Ne2+ 70.Kh2 g1=Q+ 71.Kh3 Qg3# 0-1

```

## GridGinkgo - Komodo

|  |  |
| --- | --- |
| [GridGinkgoScreen2.jpg](File:GridGinkgoScreen2.jpg) | [GridGinkgoScreen1.jpg](File:GridGinkgoScreen1.jpg) |
| [WCCC 2016](WCCC_2016 "WCCC 2016"), round 6 versus [Komodo](Komodo "Komodo"), dual GridGinkgo screen with colored [logging](Logging "Logging") and [Shredder GUI](Shredder#GUI "Shredder") |

```

[Event "WCCC 2016"]
[Site "Leiden"]
[Date "2016.06.29"]
[Round "6"]
[White "GridGinkgo"]
[Black "Komodo"]
[Result "1/2-1/2"]

1.d4 c6 2.c4 f5 3.Nf3 Nf6 4.Bf4 g6 5.e3 d6 6.h3 Nbd7 7.Nc3 Bg7 8.Be2 O-O 9.Ng5 Nb6 10.O-O h6 
11.Nf3 Be6 12.b3 Nbd7 13.Qc2 Bf7 14.Rad1 c5 15.Bd3 Qa5 16.d5 Ne8 17.Rc1 Qxc3 18.Qxc3 Bxc3 
19.Rxc3 g5 20.Bg3 Bg6 21.Nd2 Nef6 22.f4 Kg7 23.fxg5 hxg5 24.Nf3 Nh7 25.Rcc1 Ndf6 26.Be1 b5 
27.h4 b4 28.hxg5 Ne4 29.Bc2 a5 30.Ra1 Rf7 31.a3 Rff8 32.Bh4 Rfb8 33.Rfb1 Bh5 34.a4 Nf8 35.Rf1 
Ng6 36.Be1 Rf8 37.Rc1 Bg4 38.Rb1 Bh5 39.Rb2 Rae8 40.Nh2 Ne5 41.Rf4 Nc3 42.Bxc3 bxc3 43.Rb1 Be2 
44.Rf2 Bh5 45.Rbf1 Rb8 46.Nf3 Ng4 47.Re2 Kg6 48.Ree1 Rf7 49.Nh4+ Kxg5 50.Nxf5 Bg6 51.e4 Bxf5 
52.Rxf5+ Rxf5 53.exf5 Kf6 54.Re4 Rg8 55.Re6+ Kf7 56.Re1 Rh8 57.Rc1 Rb8 58.Bd1 Ne3 59.Bh5+ Kf6 
60.Rxc3 Nxf5 61.Rf3 Kg5 62.Rh3 Nd4 63.Bd1 Rf8 64.Re3 Kf6 65.Kf1 Rg8 66.g4 Rg7 67.Kf2 Rh7 68.Kg2
Kg5 69.Rh3 Rf7 70.Rh5+ Kf4 71.Rh8 Rf6 72.Rh7 e5 73.dxe6 Rxe6 74.Kf2 Re8 75.Rf7+ Kg5 76.Rd7 Rf8+ 
77.Ke1 Nf3+ 78.Ke2 Nd4+ 79.Kd2 Rf2+ 80.Ke1 Rh2 81.Rxd6 Kf4 82.Rd5 Rh1+ 83.Kd2 Rh2+ 84.Kc1 Rh1 
85.g5 Nxb3+ 86.Kc2 Nd4+ 87.Kd2 Rh2+ 88.Kc3 Rh3+ 89.Kd2 Rh2+ 90.Kc1 Nc6 91.g6 Nb4 92.Rd2 Na2+ 
93.Kc2 Nb4+ 94.Kc3 Na2+ 95.Kc2 Nb4+ 96.Kc3 Na2+ 97.Kd3 Nb4+ 98.Kc3 1/2-1/2

```

## See also

- [Cluster Toga](Cluster_Toga "Cluster Toga")
- [Crafty](Crafty "Crafty")
- [Ginkgo](Ginkgo "Ginkgo")
- [GridChess](GridChess "GridChess")
- [GridProtector](GridProtector "GridProtector")
- [Pondering](Pondering "Pondering")

## Publications

- [Frank Schneider](Frank_Schneider "Frank Schneider") (**2018**). *ICGA chess in Stockholm: A player perspective*. [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")

## External Links

## Grid

- [Grid computing from Wikipedia](https://en.wikipedia.org/wiki/Grid_computing)
- [Grid (graphic design) from Wikipedia](<https://en.wikipedia.org/wiki/Grid_(graphic_design)>)
- [The Grid](Category:The_Grid "Category:The Grid") - [Wake Up](<https://en.wikipedia.org/wiki/Evolver_(The_Grid_album)>) (1994), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## Ginkgo

- [Ginkgo from Wikipedia](https://en.wikipedia.org/wiki/Ginkgo)
- [Ginkgo biloba from Wikipedia](https://en.wikipedia.org/wiki/Ginkgo_biloba)
- [Gingo biloba (Goethe poem) from Wikipedia](https://en.wikipedia.org/wiki/Gingo_biloba)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Icho Namiki Avenue](http://www.japan-talk.com/jt/new/icho-namiki-avenue) in [Meiji Jingu Gaien Park](http://en.japantravel.com/tokyo/meiji-jingu-gaien-park/14515), [Tokyo](https://en.wikipedia.org/wiki/Tokyo) on November 27, 2004, showing [Ginkgo trees](https://en.wikipedia.org/wiki/Ginkgo_biloba) in beautiful autumn colors - Image by [Chris 73](https://commons.wikimedia.org/wiki/User:Chris_73), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Ginkgo biloba - Wikimedia Commons](https://commons.wikimedia.org/wiki/Ginkgo_biloba)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2005**). *An Optimistic Pondering Approach for Asynchronous Distributed Games*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a>  [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Photos [WCCC 2016](WCCC_2016 "WCCC 2016") by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Games from wccc2016-complete.pgn, [WCCC 2016 | ICGA](https://icga.leidenuniv.nl/?page_id=1676)

**[Up one Level](Engines "Engines")**

