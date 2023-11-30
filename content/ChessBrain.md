---
title: ChessBrain
---
**[Home](Home "Home") * [Engines](Engines "Engines") * ChessBrain**

\[ Partial map of the Internet <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**ChessBrain**,

a chess playing entity inspired by the [volunteer computing](https://en.wikipedia.org/wiki/Volunteer_computing) project [SETI@home](https://en.wikipedia.org/wiki/SETI@home), consisting of a virtual chess supercomputer of over 2000 [internet](https://en.wikipedia.org/wiki/Internet) connected machines running the [Beowulf](Beowulf "Beowulf") [open source chess engine](Category:Open_Source "Category:Open Source") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The project was headed by [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), who wrote much of the networking infrastructure, and [Colin Frayn](Colin_Frayn "Colin Frayn"), who was responsible for the chess side of things <a id="cite-note-3" href="#cite-ref-3">[3]</a>, with many voluntary computer chess developers and even more aficionados contributing in improving and testing the program, or in providing processing resources. After the presentation of **ChessBrain II** in 2006 and first tests <a id="cite-note-4" href="#cite-ref-4">[4]</a>, the ChessBrain project was abandoned.

## Description

ChessBrain's <a id="cite-note-5" href="#cite-ref-5">[5]</a> core [distributed search](Parallel_Search "Parallel Search") uses the [APHID](APHID "APHID") algorithm <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>. It performs [iterative deepening](Iterative_Deepening "Iterative Deepening") firstly locally on the [server](<https://en.wikipedia.org/wiki/Server_(computing)>) and after a certain fixed time, with new [leaf nodes](Leaf_Node "Leaf Node") being distributed as **work units** to [peer nodes](https://en.wikipedia.org/wiki/Peer-to-peer) of a [Beowulf cluster](https://en.wikipedia.org/wiki/Beowulf_cluster). Work units encode [position](Chess_Position "Chess Position") and [search depth](Depth "Depth") to be analyzed, distributed to the connected peer nodes on a request basis, also ranked by estimated complexity using extrapolation from their recorded complexity at previous, shallower depths, to implement [load balancing](<https://en.wikipedia.org/wiki/Load_balancing_(computing)>) accordant to the peer nodes' performances. In case of a [fail-high](Fail-High "Fail-High") of its parent node, pending child peer nodes receive an abort signal to immediately return and retrieve a new work unit.

**ChessBrain I** used a [supernode](<https://en.wikipedia.org/wiki/Supernode_(networking)>) to handle the remote coordination of hundreds of machines, using [XML](https://en.wikipedia.org/wiki/XML) first via [XML-RPC](https://en.wikipedia.org/wiki/XML-RPC), and later [SOAP](https://en.wikipedia.org/wiki/SOAP), [compressed](https://en.wikipedia.org/wiki/Data_compression) using [ZLib](https://en.wikipedia.org/wiki/Zlib) and then encrypted using the [AES Rijndael cipher](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

With **ChessBrain II**, jobs are distributed from a central server to remote [cluster](https://en.wikipedia.org/wiki/Computer_cluster) nodes, which in turn manage local communities of peer nodes. Initially considering the [Berkeley Open Infrastructure for Network Computing](https://en.wikipedia.org/wiki/Berkeley_Open_Infrastructure_for_Network_Computing), which was designed with a [client–server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model) in mind, the [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) requirements for ChessBrain II lead to the development of an own [message](https://en.wikipedia.org/wiki/Message) [courier](https://en.wikipedia.org/wiki/Courier) [application server](https://en.wikipedia.org/wiki/Application_server), dubbed msgCourier, also published as [open source](https://en.wikipedia.org/wiki/Source_code) <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

## Guinness World Record

On January 30, 2004, ChessBrain played a game versus [Peter Heine Nielsen](https://en.wikipedia.org/wiki/Peter_Heine_Nielsen) at [Symbion Science Park](https://en.wikipedia.org/wiki/Symbion_Science_Park), [Copenhagen](https://en.wikipedia.org/wiki/Copenhagen), [Denmak](https://en.wikipedia.org/wiki/Denmark), which ended in draw. The game was an attempt of a [Guinness World Record](https://en.wikipedia.org/wiki/Guinness_World_Records) for the largest number of computers used to play one single game of chess <a id="cite-note-10" href="#cite-ref-10">[10]</a>, on the ChessBrain site annotated by Nielsen and [Eric Schiller](Eric_Schiller "Eric Schiller") <a id="cite-note-11" href="#cite-ref-11">[11]</a>.

```
[Event "ChessBrain World Record Attempt"]
[Site "Copenhagen Denmark, Symbion Science Park"]
[Date "2004.1.30"]
[Round "1"]
[White "Peter Heine Nielsen"]
[Black "ChessBrain"]
[Result "1/2-1/2"]

1.d4 g6 2.c4 Bg7 3.e4 d6 4.Nc3 Nf6 5.Nf3 O-O 6.Be2 e5 7.O-O a5 8.Re1 exd4 
9.Nxd4 Bd7 10.Bg5 Nc6 11.Nxc6 Bxc6 12.f3 Qd7 13.Qd2 Rfe8 14.Rac1 h5 
15.Kh1 Nh7 16.Bh6 Bxh6 17.Qxh6 Re5 18.Nd5 Rae8 19.Qd2 b6 20.Bd3 Qd8 
21.Rf1 Nf6 22.b3 Bb7 23.Qc2 Nd7 24.f4 R5e6 25.e5 c6 26.f5 gxf5 27.Bxf5 
cxd5 28.Bxe6 Rxe6 29.Rxf7 Kxf7 30.Qh7+ Ke8 31.Qxh5+ Ke7 32.Qg5+ Ke8 
33.Qh5+ Ke7 34.Qh7+ 1/2-1/2

```

## See also

- [Beowulf](Beowulf "Beowulf")
- [Chess Brain](Chess_Brain "Chess Brain")
- [ChessBrainVB](ChessBrainVB "ChessBrainVB")
- [GridChess](GridChess "GridChess")

## Publications

<a id="cite-note-12" href="#cite-ref-12">[12]</a>

- [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano") (**2003**). *ChessBrain: a Linux-Based Distributed Computing Experiment*. [Linux Journal](https://en.wikipedia.org/wiki/Linux_Journal), September 2003, [pdf](http://chessbrain.net/docs/cblinuxjournal0903.pdf)
- [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [Colin Frayn](Colin_Frayn "Colin Frayn") (**2003**). *The ChessBrain Project: A Global Effort To Build The World's Largest Chess SuperComputer*. [ICGA Journal, Vol. 26, No. 2](ICGA_Journal#26_2 "ICGA Journal"), [pdf](http://chessbrain.net/docs/thechessbrainproject.pdf)
- [Colin Frayn](Colin_Frayn "Colin Frayn"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano") (**2004**). *The ChessBrain Project – Massively Distributed Inhomogeneous Speed-Critical Computation*. Proceedings IC-SEC, Singapore, 2004
- [Kevin Lew](Kevin_Lew "Kevin Lew"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [Colin Frayn](Colin_Frayn "Colin Frayn") (**2005**). *Early experiences with clusters and compute farms in ChessBrain II*. BoF LinuxForum, [pdf](http://chessbrain.net/docs/ccfcb2.pdf)
- [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano") (**2005**). *[Tapping the Matrix: Harnessing distributed computing resources using Open Source tools](http://chessbrain.net/LFBOF2005/tappingthematrix.html)*. BoF LinuxForum
- [Colin Frayn](Colin_Frayn "Colin Frayn"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [Kevin Lew](Kevin_Lew "Kevin Lew") (**2006**). *ChessBrain II – A Hierarchical Infrastructure for Distributed Inhomogeneous Speed-Critical Computation*. [pdf](http://www.chessbrain.net/docs/chessbrainII.pdf)
- [Colin Frayn](Colin_Frayn "Colin Frayn"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano") (**2007**). *The ChessBrain project*. in [Advanced Intelligent Paradigms in Computer Games](http://www.springer.com/engineering/book/978-3-540-72704-0)

## Forum Posts

- [Massive, planetary chess computer?](https://groups.google.com/d/msg/rec.games.chess.computer/IRuxdsriHpE/dXzux4fNgDsJ) by [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 07, 2002
- [Chess-Brain Network](https://www.stmintz.com/ccc/index.php?id=279522) by Randy Adams, [CCC](CCC "CCC"), January 26, 2003
- [The Worlds Largest Chess Computer!](https://groups.google.com/d/msg/rec.games.chess.computer/od8sh6iy_xU/h3TewITgHh0J) by [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2003
- [IMPORTANT info for ChessBrain.net participants: team WINBOARD](https://groups.google.com/d/msg/rec.games.chess.computer/Y8JyXNBUO5c/0SC13qPrCtcJ) by Ed Seid, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 31, 2003
- [chess brain](https://www.stmintz.com/ccc/index.php?id=288743) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), October 03, 2003
- [Distributed Computing - BOINC and ChessBrain](https://groups.google.com/d/msg/rec.games.chess.computer/jemmVlFzazM/fIaxeukUTBgJ) by Ed Seid, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 21, 2003
- [Event on January 30th: Chessbrain vs Peter Heine Nielsen](https://groups.google.com/d/msg/rec.games.chess.computer/lDxckrXYuNI/z4lGX79ErGcJ) by Sascha Luehrs, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2004
- [World Record Attempt TODAY](https://groups.google.com/d/msg/rec.games.chess.computer/gjg4ns5gves/WO1G5_4bQ1cJ) by Gregory Topov, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 30, 2004

## External Links

## Chess Entity

- [ChessBrain](http://chessbrain.net/)
- [Col’s Rational World » Blog Archive » ChessBrain](http://frayn.net/blog/?p=662) by [Colin Frayn](Colin_Frayn "Colin Frayn")
- [Largest networked chess computer | Guinness World Records](http://www.guinnessworldrecords.com/world-records/largest-networked-chess-computer/)
- [ChessBrain (beendet) – Rechenkraft](<http://www.rechenkraft.net/wiki/ChessBrain_(beendet)>) (German)

## Misc

- [Klaus Schulze](Category:Klaus_Schulze "Category:Klaus Schulze") - [Timewind](https://en.wikipedia.org/wiki/Timewind) (1975), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Partial map of the [Internet](https://en.wikipedia.org/wiki/Internet) based on the January 15, 2005 data found on [opte.org](http://www.opte.org/maps/). Each line is drawn between two nodes, representing two [IP addresses](https://en.wikipedia.org/wiki/IP_address). The length of the lines are indicative of the delay between those two nodes. This graph represents less than 30% of the [Class C](https://en.wikipedia.org/wiki/Classful_network) networks reachable by the data collection program in early 2005. Lines are color-coded according to their corresponding [RFC 1918](https://tools.ietf.org/html/rfc1918), Original upload: December 1, 2006, [The Opte Project](http://www.opte.org/), [CC BY 2.5](https://creativecommons.org/licenses/by/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Beowulf Computer Chess Home Page](http://www.frayn.net/beowulf/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Col’s Rational World » Blog Archive » ChessBrain](http://frayn.net/blog/?p=662)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [ChessBrain](http://chessbrain.net/)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> Description based on: [Colin Frayn](Colin_Frayn "Colin Frayn"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [Kevin Lew](Kevin_Lew "Kevin Lew") (**2006**). *ChessBrain II – A Hierarchical Infrastructure for Distributed Inhomogeneous Speed-Critical Computation*. [pdf](http://www.chessbrain.net/docs/chessbrainII.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Mark Brockington](Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. Thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp02/NQ29023.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Joan Daemen](Mathematician#JDaemen "Mathematician"), [Vincent Rijmen](Mathematician#VRijmen "Mathematician") (**1999**). *The Rijndael Block Cipher*. AES Proposal, [pdf](http://www.cryptosoft.de/docs/Rijndael.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [msgCourier download | SourceForge.net](https://sourceforge.net/projects/msgcourier/)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Largest networked chess computer | Guinness World Records](http://www.guinnessworldrecords.com/world-records/largest-networked-chess-computer/)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [ChessBrain - Game Commentary](http://chessbrain.net/games.html)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [ChessBrain Documentation](http://chessbrain.net/documentation.html)

**[Up one Level](Engines "Engines")**

