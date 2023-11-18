---
title: GridChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GridChess**

\[ A grid applied within an image <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GridChess**,

a prototypical implementation of a twofold [distributed game-tree search](Parallel_Search "Parallel Search") approach.
[Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") (YBWC) parallelized chess programs running on a [cluster](https://en.wikipedia.org/wiki/Computer_cluster), where optimistic [pondering](Pondering "Pondering") performs a second parallel approach on top of several clusters which can be used to achieve a further speedup.

## Cluster Toga

*see main article [Cluster Toga](Cluster_Toga "Cluster Toga")*.

The scheduling per cluster node is implemented based on the [Message Passing Interface (MPI)](https://en.wikipedia.org/wiki/Message_Passing_Interface) by a [work-stealing](https://en.wikipedia.org/wiki/Cilk#Work-stealing) mechanism to [balance the load](https://en.wikipedia.org/wiki/Load_balancing_%28computing%29) dynamically. Each worker at the intra-cluster level is represented by [Cluster Toga](Cluster_Toga "Cluster Toga"), a YBWC version of [Toga](Toga "Toga") by [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch") based on [Fruit](Fruit "Fruit") by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey").
All processors on the same cluster node [share](Shared_Hash_Table "Shared Hash Table") their [hash table](Transposition_Table "Transposition Table"). New hash table entries are permanently replicated between all cluster nodes in a similar way as described for [Brutus](Brutus "Brutus") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Optimistic Pondering

The asynchronous optimistic [pondering](Pondering "Pondering") is applied not only during the opponent’s thinking time but also during the own thinking time, and schedules cluster nodes (workers) with consecutive [root-nodes](Root "Root") along the [principal variation](Principal_Variation "Principal Variation") (PV), which is most often available in a stable form at early stages of the search. This is based on the same observation, [David Levy](David_Levy "David Levy") proposed his *[Multiple Extensions](PV_Extensions#Multiple "PV Extensions")* algorithm to treat the often early stable part of a PV as a single [ply](Ply "Ply") to achieve higher [search depths](Depth "Depth") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
If a change is detected in a PV within the first two plies, the actual searching ahead of the according worker is canceled and a new search for the current PV is started immediately.

## Ph.D. Project

GridChess with focus on optimistic pondering was Ph.D. project of [Kai Himstedt](Kai_Himstedt "Kai Himstedt") at [University of Hamburg](University_of_Hamburg "University of Hamburg") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>. [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), then affiliated with the [Paderborn University](Paderborn_University "Paderborn University") and the *Paderborn Center for Parallel Computing*, made contributions concerning the [parallel search](Parallel_Search "Parallel Search").

## Description

given in 2007 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++
GridChess is composed of two major components: 1) The proxy chess engine ([Crafty](Crafty "Crafty") based) performs no tree search itself but has some kind of a master role to control the optimistic pondering with distributed worker clients. As a simplified explanation of optimistic pondering here, one can imagine the worker clients forming a pondering pipeline with expected opponent moves extracting this information from the principal variations provided by the chess engines. 2) Real chess engines (controlled by distributed worker clients), Fruit/Toga based, parallelized with Young Brothers Wait Concept (YBWC). This way a combination of two parallel concepts was realized building the complete GridChess system: The parallel Fruit/Toga base engines using the YBWC may run on high performance clusters, each cluster representing a worker client for the proxy chess engine. Several such clusters are then used for an asynchronous distributed game-tree search with the optimistic pondering method. 

```

## Tournament Play

GridChess played the [IPCCC 2006](IPCCC_2006 "IPCCC 2006"), and shared third place at the [WCCC 2007](WCCC_2007 "WCCC 2007"). The proxy chess engine component of GridChess is based on [Crafty](Crafty "Crafty") by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") and performs no tree search itself but has some kind of a master role to control the optimistic pondering with distributed workers. However, the participation at the [WCCC 2008](WCCC_2008 "WCCC 2008") was restricted to the use of Cluster Toga as a "stand alone" component, because there was a licensing issue in connection with the use of some parts of Crafty <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Selected Games

[WCCC 2007](WCCC_2007 "WCCC 2007"), round 8, GridChess - [Shredder](Shredder "Shredder") <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```

[Event "WCCC 2007"]
[Site "Amsterdam, The Netherlands"]
[Date "2007.06.16"]
[Round "8"]
[White "GridChess"]
[Black "Shredder"]
[Result "1-0"]

1.e4  c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2 e6 7.Be3 Qc7 8.Qd2 b5 9.a3 Be7 10.f4 Bb7 
11.Bf3 Nbd7 12.f5 e5 13.Nb3 Rc8 14.Qf2 h5 15.O-O-O d5 16.exd5 Bxa3 17.Kb1 Bxb2 18.d6 Qxc3 19.Rd3 
Qc4 20.Bxb7 Rb8 21.Kxb2 Rxb7 22.Ra1 Rb8 23.Rxa6 Rc8 24.Na5 Qe4 25.Nc6 b4 26.Ne7 Ra8 27.Rxa8+ Qxa8 
28.Qe1 Qb8 29.Qa1 Qb7 30.Qa4 Ne4 31.Rb3 Nc3 32.Qa5 Nd1+ 33.Kb1 Nxe3 34.Rxe3 Qb6 35.Qa8+ Qb8 36.Qd5 
Kf8 37.Nc6 Qa8 38.Qc4 Qc8 39.Re4 Nb6 40.Qxb4 Nd7 41.Rc4 Qe8 42.Ne7 g6 1-0 

```

## Authors

- [Kai Himstedt](Kai_Himstedt "Kai Himstedt")
- [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz")
- [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch"), [Toga](Toga "Toga") parts
- [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Fruit](Fruit "Fruit") parts
- [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Crafty](Crafty "Crafty") parts

## See also

- [Cluster Toga](Cluster_Toga "Cluster Toga")
- [Crafty](Crafty "Crafty")
- [Fruit](Fruit "Fruit")
- [GridGinkgo](GridGinkgo "GridGinkgo")
- [GridProtector](GridProtector "GridProtector")
- [Pondering](Pondering "Pondering")
- [Toga](Toga "Toga")
- [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

## Publications

- [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2005**). *[An Optimistic Pondering Approach for Asynchronous Distributed Games](https://content.iospress.com/articles/icga-journal/icg28203)*. [ICGA Journal, Vol. 28, No. 2](ICGA_Journal#28_2 "ICGA Journal")
- [Kai Himstedt](Kai_Himstedt "Kai Himstedt"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Dietmar P. F. Möller](https://www.informatik.uni-hamburg.de/TIS/index.php/de/mitarbeiter/dietmar-p-f-moeller) (**2008**). *[A Twofold Distributed Game-Tree Search Approach Using Interconnected Clusters](https://link.springer.com/chapter/10.1007/978-3-540-85451-7_62)*. [Euro-Par 2008](https://link.springer.com/book/10.1007/978-3-540-85451-7), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *[Optimistische verteilte Spielbaumsuche am Beispiel des Computerschachs](http://www.shaker.de/de/content/catalogue/index.asp?ID=8&ISBN=978-3-8440-0803-6)*. Dissertation (German)
- [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *[GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept](https://content.iospress.com/articles/icga-journal/icg35202)*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal") » [Pondering](Pondering "Pondering"), [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

## Forum Posts

- [grid chess at the wccc: supercharged toga?](http://www.talkchess.com/forum/viewtopic.php?t=14495) by ozziejoe, [CCC](CCC "CCC"), June 16, 2007
- [Cluster Toga based on Fruit Source Code](http://www.talkchess.com/forum/viewtopic.php?t=34780) by [Kai Himstedt](Kai_Himstedt "Kai Himstedt"), [CCC](CCC "CCC"), June 07, 2010 <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## External Links

## Chess Entity

- [PhD Project of Kai Himstedt (Dipl.-Inform.)](http://www.informatik.uni-hamburg.de/TIS/index.php/de/projekte/phd-projects/79/)
- [GridChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=520)
- [The chess games of GridChess](http://www.chessgames.com/perl/chessplayer?pid=107843) from [chessgames.com](http://www.chessgames.com/index.html)

## Misc

- [Grid computing from Wikipedia](https://en.wikipedia.org/wiki/Grid_computing)
- [Grid (graphic design) from Wikipedia](<https://en.wikipedia.org/wiki/Grid_(graphic_design)>)
- [The Grid](Category:The_Grid "Category:The Grid") - [Figure of 8](<https://en.wikipedia.org/wiki/456_(album)>) (1992), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Drawing simplified from a [woodcut](https://en.wikipedia.org/wiki/Woodcut) from the [Divina Proportione](https://en.wikipedia.org/wiki/Divina_proportione), [Luca Pacioli](https://en.wikipedia.org/wiki/Luca_Pacioli) 1509, [Venice](https://en.wikipedia.org/wiki/Venice), depicting proportions of the [human face](https://en.wikipedia.org/wiki/Face). The [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio) does not appear in the drawing. [Grid (graphic design) from Wikipedia](<https://en.wikipedia.org/wiki/Grid_(graphic_design)>), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Alex Kure](Alex_Kure "Alex Kure"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2004**). *Parallel Brutus: The First Distributed, FPGA Accelerated Chess Program*. [IPDPS’04](http://dl.acm.org/citation.cfm?id=645610&picked=prox)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [David Levy](David_Levy "David Levy") (**2003**). *The State of the Art in Man vs. “Machine” Chess*. [ICGA Journal, Vol. 26, No. 1](ICGA_Journal#26_1 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [PhD Project of Kai Himstedt (Dipl.-Inform.)](http://www.informatik.uni-hamburg.de/TIS/index.php/de/projekte/phd-projects/79/)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *[Optimistische verteilte Spielbaumsuche am Beispiel des Computerschachs](http://www.shaker.de/de/content/catalogue/index.asp?ID=8&ISBN=978-3-8440-0803-6)*. Dissertation (German)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [GridChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=520)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Amsterdam 2007 - Chess - Round 8 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=173&round=8&id=6)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Download - Cluster Toga 1.4b5c based on Fruit 2.1 UCI](https://www.informatik.uni-hamburg.de/TIS/file-download/email-file.php)

**[Up one level](Engines "Engines")**

