---
title: Chester
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chester**

\[ Chester <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chester**,

a private chess engine written by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"). Chester is a solid tactical program, applying [singular extensions](Singular_Extensions "Singular Extensions") restricted to fairly near-root nodes disjoint from [recapture extensions](Recapture_Extensions "Recapture Extensions") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . Inspired by comments [Bruce Moreland](Bruce_Moreland "Bruce Moreland") made at [CCT3](CCT3 "CCT3"), if a (significantly) [reduced depth](Depth_Reduction_R "Depth Reduction R") search of the moves at a [node](Node "Node") reveal that only one move produced a [score](Score "Score") near [alpha](Alpha "Alpha") and the rest are all worse, then extend it. Steve further worked on positional knowledge during the development and mentioned Chester does not have any special [bad bishop](Bad_Bishop "Bad Bishop") code beyond [mobility](Mobility "Mobility") <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Chester played a strong [CCT3](CCT3 "CCT3") with 4½/8 and [CCT4](CCT4 "CCT4") with 6/11.

## Selected Games

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

## Tinker

[CCT4](CCT4 "CCT4"), round 1, [Tinker](Tinker "Tinker") - Chester

```

[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.19"]
[Round "1"]
[White "Tinker"]
[Black "Chester"]
[Result "0-1"]

1.d4 Nf6 2.c4 g6 3.g3 c6 4.Nf3 Bg7 5.Bg2 O-O 6.Nc3 d5 7.Qb3 dxc4 8.Qxc4 Bf5
9.O-O Nbd7 10.Qa4 Nb6 11.Qa3 Qd6 12.Qxd6 exd6 13.Bf4 Rad8 14.Nd2 d5 15.Bc7
Rc8 16.Bxb6 axb6 17.e3 Ra8 18.a4 Rfe8 19.Rfd1 Bf8 20.Nf3 Bb4 21.Na2 Be7 22.Nc3
Ra5 23.b3 Rea8 24.Nh4 Bc2 25.Rdc1 Bxb3 26. Rab1 Ba3 27.Re1 Bc2 28.Rxb6 Rb8
29.Bh3 Ne4 30.Nxe4 dxe4 31.Bd7 Bxa4 32.Reb1 Rb5 33.R6xb5 Bxb5 34.Ra1 Bb4 35.h3
Kf8 36.d5 Ke7 37.dxc6 bxc6 38.Bg4 c5 39.Ra7+ Kf6 40.Ng2 h5 41.Bd1 Bd3 42.Nf4
c4 43.Kg2 Bc5 44.Ra5 Rc8 45.Nd5+ Ke6 46.Nf4+ Kd6 47.Ne2 Rc6 48.Ra4 Rb6 49.Ra2
Bb4 50.Nf4 Be1 51.Bc2 Ke5 52.Bd1 Rb1 53.Bc2 Rc1 54.Ba4 c3 55.Ne2 Rb1 56.Nxc3
Bxc3 57.Be8 Ke6 58.h4 Be5 59.Ba4 Rb4 60.Ra3 Be2 61.Bc2 Bf3+ 62.Kf1 Kf5 63.Ke1
Rc4 64.Kd2 Kg4 65.Bb3 Rc7 66.Ba4 Kh3 67.Ra2 Kg2 68.Rc2 Rxc2+ 69.Kxc2 Kxf2 0-1

```

## IsiChess

[CCT4](CCT4 "CCT4"), round 6, Chester - [IsiChess](IsiChess "IsiChess")

```

[Event "ICC 60 10"]
[Site "Internet Chess Club"]
[Date "2002.01.20"]
[Round "6"]
[White "Chester"]
[Black "IsiChess"]
[Result "1-0"]

1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Qc2 Bd6 7.Bd3 e5 8.cxd5 cxd5
9.Nb5 Bb8 10.dxe5 Nxe5 11.Nxe5 Bxe5 12.O-O O-O 13.Bd2 Bd7 14.Bb4 Re8 15.Rfc1
a6 16.Nc7 Rc8 17.Nxe8 Rxc2 18.Nxf6+ Qxf6 19.Rxc2 Bxb2 20.Rb1 Be5 21.h3 g5
22.Rbc1 Qe6 23.g4 Bc6 24.Bf5 Qh6 25.Kg2 Kg7 26.f3 Bb5 27.a3 Qb6 28.Bc5 Qf6
29.h4 h6 30.hxg5 hxg5 31.Rh1 Bc4 32.Rh5 b6 33.Bb4 a5 34.Bd2 Qe7 35.e4 Qxa3
36.Bxg5 Qd3 37.Rf2 dxe4 38.Bh6+ Kf6 39.f4 Bd6 40.Bg5+ Kg7 41.Rh7+ Kf8 42.Bf6
Ke8 43.Rh8+ Bf8 44.Bg7 Be6 45.Bxe6 fxe6 46.Rxf8+ Ke7 47.f5 e3 48.f6+ Kd7
49.Rd8+ Kxd8 50.f7 Qe4+ 51.Kg3 exf2 52.f8=Q+ Kd7 53.Qxf2 Qd3+ 54.Kf4 Qd6+
55.Be5 Qf8+ 56.Ke3 Qc5+ 57.Bd4 Qc1+ 58.Qd2 Qa3+ 59.Ke2 Qa4 60.Bf6+ Kc6 61.Qc3+
Kb7 62.Qf3+ Ka7 63.g5 Qc2+ 64.Ke3 Qc1+ 65.Ke4 Qc5 66.Qd1 Ka6 67.Qd3+ b5 68.Qd8
Qc2+ 69.Ke5 b4 70.Qd6+ Kb5 71.Qd7+ Kb6 72.Qxe6+ Kb5 73.Qd7+ Kb6 74.Bd8+ Ka6
75.Qd5 Qc3+ 76.Kd6 b3 77.Bf6 Qb4+ 78.Kc7 Qb6+ 79.Kc8 b2 80.Qd3+ Qb5 81.Qxb5+
Kxb5 82.Bxb2 1-0

```

## See also

- [King of Kings](index.php?title=King_of_Kings&action=edit&redlink=1 "King of Kings (page does not exist)")
- [Ruffian](Ruffian "Ruffian")
- [Tinker](Tinker "Tinker")

## Forum Posts

- [Re: ATTN : CCC users - 1 Hour CCR Test - Chester's results](https://www.stmintz.com/ccc/index.php?id=168220) by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"), [CCC](CCC "CCC"), May 05, 2001 » [CCR One Hour Test](CCR_One_Hour_Test "CCR One Hour Test")
- [Re: Nice tactical shot](https://www.stmintz.com/ccc/index.php?id=209485) by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"), [CCC](CCC "CCC"), January 24, 2002 » [Singular Extensions](Singular_Extensions "Singular Extensions")

## External Links

- [Chester (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Chester_%28disambiguation%29)
- [Chester (city) from Wikipedia](https://en.wikipedia.org/wiki/Chester)
- [Chester Creek from Wikipedia](https://en.wikipedia.org/wiki/Chester_Creek)
- [Chester River from Wikipedia](https://en.wikipedia.org/wiki/Chester_River)
- [Chester (song) from Wikipedia](https://en.wikipedia.org/wiki/Chester_%28song%29)
- [Chesterfield (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Chesterfield_%28disambiguation%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chester (1874-1888)](https://en.wikipedia.org/wiki/File:Chester_1874.jpg) was an [Australian Thoroughbred](https://en.wikipedia.org/wiki/Thoroughbred_racing_in_Australia) racehorse and champion sire, ca. 1878 by Turf Cavalcade, [Chester (horse) from Wikipedia](https://en.wikipedia.org/wiki/Chester_%28horse%29)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Nice tactical shot](https://www.stmintz.com/ccc/index.php?id=209565) by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"), [CCC](CCC "CCC"), January 24, 2002
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: ATTN : CCC users - 1 Hour CCR Test - Chester's results](https://www.stmintz.com/ccc/index.php?id=168466) by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"), [CCC](CCC "CCC"), May 07, 2001
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> PGN download from [CCT4](http://www.vrichey.de/cct4/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one Level](Engines "Engines")**

