---
title: Cluster Toga
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cluster Toga**

\[.JPG) Ancient Times, Roman <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cluster Toga**,

a chess engine based on [Toga II](Toga "Toga") by [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch"), in turn based on [Fruit 2.1](Fruit "Fruit") by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey").
Cluster Toga is a [parallel extension](Parallel_Search "Parallel Search") of Toga, implemented by [Kai Himstedt](Kai_Himstedt "Kai Himstedt") and [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz").
It considers the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") using [Message Passing Interface (MPI)](https://en.wikipedia.org/wiki/Message_Passing_Interface) for a [work-stealing](https://en.wikipedia.org/wiki/Cilk#Work-stealing) mechanism to [balance the load](https://en.wikipedia.org/wiki/Load_balancing_%28computing%29) dynamically, and utilizes a [shared hash table](Shared_Hash_Table "Shared Hash Table").
Cluster Toga represents an intra-cluster worker of the [cluster](https://en.wikipedia.org/wiki/Computer_cluster) chess entity [GridChess](GridChess "GridChess"). However, Cluster Toga played the [IPCCC 2007](IPCCC_2007 "IPCCC 2007") and the [WCCC 2008](WCCC_2008 "WCCC 2008") as "stand alone" engine instead of GridChess, due to a licensing issue in connection with the use of some parts of [Crafty](Crafty "Crafty") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Description

given in 2008 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++Cluster Toga is a Young Brothers Wait Concept (YBWC) parallelized version of Toga based on Fruit capable to run on a high performance cluster. In fact it is a "stand alone" base engine of the GridChess system which participated [last year in Amsterdam](WCCC_2007 "WCCC 2007") but is limited to use a single cluster. 

```

## Photos & Games

## IPCCC 2007

[](File:Clustertoga-shredder.JPG)
[IPCCC 2007](IPCCC_2007 "IPCCC 2007"), [Kai Himstedt](Kai_Himstedt "Kai Himstedt"), [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), Cluster Toga - [Shredder](Shredder "Shredder") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```

[Event "IPCCC 2007"]
[Site "Paderborn, GER"]
[Date "2007.12.27"]
[Round "02"]
[White "Cluster Toga"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 a6 8.O-O-O Bd7 9.f4 b5 
10.Bxf6 gxf6 11.Kb1 Rc8 12.g4 h5 13.gxh5 Rxh5 14.h4 Qb6 15.Nce2 Rh8 16.Rh2 Na5 17.Ng3 Nc4 
18.Qe2 a5 19.Qf3 a4 20.Bxc4 bxc4 21.Nde2 Rb8 22.Qc3 Qb4 23.a3 Qxc3 24.Nxc3 Bh6 25.Nge2 Ke7 
26.Rd4 Rhc8 27.Rh1 Rc7 28.Ka2 Rg8 29.Rhd1 Rc6 30.Kb1 Rg4 31.h5 Rh4 32.Nb5 Rh2 33.Nxd6 e5 
34.Rd5 Rxe2 35.Nxf7 Kxf7 36.Rxd7+ Kg8 37.Rg1+ Kh8 38.Rd8+ Kh7 39.Rd7+ Kh8 40.Rd8+ Kh7 
41.Rd7+ Kh8 1/2-1/2

```

## WCCC 2008

[](File:Cluster-toga-vs-hiarcs.JPG)
[WCCC 2008](WCCC_2008 "WCCC 2008"), round 1, [Harvey Williamson](Harvey_Williamson "Harvey Williamson") and [Timo Klaustermeyer](Timo_Haupt "Timo Haupt"), Cluster Toga - [HIARCS](HIARCS "HIARCS") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

```

[Event "WCCC 2008"]
[Site "Beijing, China"]
[Date "2008.09.28"]
[Round "1"]
[White "Cluster Toga"]
[Black "HIARCS"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e5 7.Nb3 Be6 8.f3 Be7 9.Qd2 O-O 
10.O-O-O Nbd7 11.g4 b5 12.g5 Nh5 13.Kb1 Qc7 14.Nd5 Bxd5 15.exd5 Nb6 16.Na5 Nxd5 17.Qxd5 
Qxa5 18.Bd3 g6 19.Qb7 Rfe8 20.Be4 Qa4 21.Bc6 Rab8 22.Qa7 Rec8 23.c3 Ng7 24.h4 Nf5 25.Bb6 
Rcf8 26.Bf2 Rfd8 27.Ka1 Kg7 28.Be4 Rde8 29.h5 Qc4 30.Qxa6 Bxg5 31.Rhg1 Kf6 32.Ba7 Rbd8 
33.hxg6 hxg6 34.Bb6 Rdb8 35.Qa7 Qe6 36.Rd3 Reh8 37.Rgd1 Rbc8 38.Bb7 Rcf8 39.Bc7 Kg7 
40.Be4 Be7 41.Bb6 Bd8 42.Bf2 Bh4 43.Bb6 Bd8 44.Bf2 Bh4 45.Bb6 Bd8 1/2-1/2

```

## Authors

<a id="cite-note-8" href="#cite-ref-8">[8]</a>

|  Author
|  Role
|  Parts
|
| --- | --- | --- |
| [Kai Himstedt](Kai_Himstedt "Kai Himstedt") |  engine programmer
|  |
| [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") |  engine programmer
|  |
| [Thomas Gaksch](Thomas_Gaksch "Thomas Gaksch") |  engine programmer
| [Toga](Toga "Toga") |
| [Clemens Keck](index.php?title=Clemens_Keck&action=edit&redlink=1 "Clemens Keck (page does not exist)") | [book author](Category:Opening_Book_Author "Category:Opening Book Author") |  |
| [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") |  engine programmer
| [Fruit](Fruit "Fruit") |
| [Timo Klaustermeyer](Timo_Haupt "Timo Haupt") |  book author, [operator](Category:Operator "Category:Operator") |  |

## See also

- [Fruit](Fruit "Fruit")
- [GridChess](GridChess "GridChess")
- [GridProtector](GridProtector "GridProtector")
- [Toga](Toga "Toga")

## Forum Posts

- [Cluster Toga/Paderborn championship](http://www.talkchess.com/forum/viewtopic.php?t=18725) by ChessAddict, [CCC](CCC "CCC"), January 03, 2008
- [Toga Cluster](http://www.talkchess.com/forum/viewtopic.php?t=24083) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), September 29, 2008
- [Cluster Toga based on Fruit Source Code](http://www.talkchess.com/forum/viewtopic.php?t=34780) by [Kai Himstedt](Kai_Himstedt "Kai Himstedt"), [CCC](CCC "CCC"), June 07, 2010 <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Please, Cluster Toga && Zochova](http://www.talkchess.com/forum/viewtopic.php?t=46179) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [CCC](CCC "CCC"), November 28, 2012 » [Zochova](Zochova "Zochova")

## [Re: Please, Cluster Toga && Zochova](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=494419&t=46179) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), November 28, 2012 External Links

## Chess Entity

- [Cluster Toga's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=568)
- [Download - Cluster Toga 1.4b5c based on Fruit 2.1 UCI](https://www.informatik.uni-hamburg.de/TIS/file-download/email-file.php)

## Misc

### Cluster

- [Cluster from Wikipedia](https://en.wikipedia.org/wiki/Cluster)
- [Computer cluster from Wikipedia](https://en.wikipedia.org/wiki/Computer_cluster)
- [Star cluster from Wikipedia](https://en.wikipedia.org/wiki/Star_cluster)
- [Supercluster from Wikipedia](https://en.wikipedia.org/wiki/Supercluster)
- [Open cluster from Wikipedia](https://en.wikipedia.org/wiki/Open_cluster)

### Toga

- [Toga (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Toga_(disambiguation)>)
- [Toga from Wikipedia](https://en.wikipedia.org/wiki/Toga)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Costumes of All Nations](http://www.kendallredburn.com/Plates3.html) (1882) by [Albert Kretschmer](https://en.wikipedia.org/wiki/Albert_Kretschmer), painters and costumer to the [Royal Court Theatre, Berlin](https://en.wikipedia.org/wiki/Konzerthaus_Berlin), and Dr. Carl Rohrbach, photographed by [Kendall Redburn](http://www.kendallredburn.com/), [Category:Costumes of All Nations (1882)](<https://commons.wikimedia.org/wiki/Category:Costumes_of_All_Nations_(1882)>) [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Cluster Toga's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=568)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> Image by [Sebastian Böhme](Sebastian_B%C3%B6hme "Sebastian Böhme"), from his no longer available homepage /sebi/Paderborn2007 (as of July 13, 2019)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [International Paderborn Computer Chess Championships (IPCCC)](http://old.csvn.nl/pad_hist.html), [CSVN-tournament site](http://old.csvn.nl/)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> Image by [Sebastian Böhme](Sebastian_B%C3%B6hme "Sebastian Böhme"), from his no longer available homepage /sebi/WCCC-Beijing-2008 (as of July 13, 2019)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Beijing 2008 - Chess - Round 1 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=178&round=1&id=3)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Cluster Toga's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=568)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Download - Cluster Toga 1.4b5c based on Fruit 2.1 UCI](https://www.informatik.uni-hamburg.de/TIS/file-download/email-file.php)

**[Up one level](Engines "Engines")**

