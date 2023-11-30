---
title: Charly
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Charly**

\[ [New Glarus](https://en.wikipedia.org/wiki/New_Glarus,_Wisconsin) [yodelers](https://en.wikipedia.org/wiki/Yodeling) in traditional Swiss garb <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Charly**, (**C**hess **h**euristics and **a**lgorithms for **r**elaxing **l**azy **y**odelers)

an early chess program developed in 1967/68 by [Gerald Tripard](Gerald_Tripard "Gerald Tripard"), [Gerhard Rudolf](index.php?title=Gerhard_Rudolf&action=edit&redlink=1 "Gerhard Rudolf (page does not exist)") and [Werner Joho](Werner_Joho "Werner Joho") at [ETH Zurich](ETH_Zurich "ETH Zurich"),
to run on a [CDC 1604](CDC_1604 "CDC 1604").

## Description

The main tree [search](Search "Search") went 4 [plies](Ply "Ply") [deep](Depth "Depth"), with the final position including an extensive [evaluation of all possible exchanges](Static_Exchange_Evaluation "Static Exchange Evaluation") on the square occupied by the piece being moved there on the last ply.
This made the program relatively strong [tactically](Tactics "Tactics") but there was not much in the program incorporating [strategy](Strategy "Strategy"). Strategy, besides [material](Material "Material") advantage, included [mobility](Mobility "Mobility") of the pieces, [pawn structure](Pawn_Structure "Pawn Structure") and advancement to queening.
It required a considerable amount of time making the program totally move-legal, such as incorporating all of the rules associated with [castling](Castling "Castling"), [en passant](En_passant "En passant"), and [stalemate](Stalemate "Stalemate") through [move repetition](Repetitions#RepetitionofMoves "Repetitions").
The only thing not included was pawn [promotion](Promotions "Promotions") to something other than a queen.
The [opening book](Opening_Book "Opening Book") was programmed by Gerhard Rudolf, the machine language expert, the chess playing algorithm was programmed in [Fortran](Fortran "Fortran").
The library entries were collected from books, mainly, the 10th edition of [Larry Evans](https://en.wikipedia.org/wiki/Larry_Evans), [Modern Chess Openings](https://en.wikipedia.org/wiki/Modern_Chess_Openings)
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## ETH-MIT Match

In 1968, [Gerald Tripard](Gerald_Tripard "Gerald Tripard") asked [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") for a match versus [Mac Hack VI](Mac_Hack "Mac Hack"). Three games were played in October and November 1968 via [ham radio](https://en.wikipedia.org/wiki/Amateur_radio)
<a id="cite-note-3" href="#cite-ref-3">[3]</a>:

## Game 1

<a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>

```
[Event "ETH-MIT Match"]
[Site "Zurich/Cambridge"]
[Date "1968.10.27"]
[Round "1"]
[White "Charly"]
[Black "Mac Hack VI"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nf6 3.d4 Nxe4 4.Bd3 d5 5.Nxe5 Bd6 6.O-O O-O 7.c4 Bxe5 8.dxe5 Nc6
9.cxd5 Qxd5 10.Qf3 Bf5 11.Qxf5 Qxd3 12.Nc3 Nc5 13.Qxd3 Nxd3 14.f4 Rfd8 15.Rf3 Rd7
16.Ne4 Rad8 17.b3 R7d4 18.Nc3 Ne1 19.Rg3 Nc2 20.Rb1 Kf8 21.Nb5 R4d1+ 22.Kf2 R8d7
23.Ke2 R1d5 24.a4 N6d4+ 25.Nxd4 Nxd4+ 26.Kf2 Nf5 27.Ba3+ c5 28.Rc3 R5d2+ 29.Kg1 b6
30.g4 Nd4 31.Kh1 Nc2 32.Bc1 Re2 33.Bb2 Ne3 34.h3 Rd1+ 35.Rxd1 Nxd1 36.Ba1 Nxc3
37.Bxc3 Rc2 38.Be1 Rc1 39.g5 Rxe1+ 40.Kg2 Re4 41.b4 cxb4 0-1

```

## Games 2 and 3

<a id="cite-note-6" href="#cite-ref-6">[6]</a>

```
[Event "ETH-MIT Match"]
[Site "Zurich/Cambridge"]
[Date "1968.11.26"]
[Round "2"]
[White "Mac Hack VI"]
[Black "Charly"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4 exd4 5.Nxd4 Nge7 6.Nc3 a6 7.Ba4 b5 8.Bb3 Na5
9.Qf3 Nxb3 10.axb3 c5 11.Ndxb5 d5 12.Nxd5 Nxd5 13.exd5 Qe7+ 14.Qe3 Qxe3+ 15.Bxe3 Kd7
16.Nc3 Bd6 17.Na4 Rb8 18.Nxc5+ Bxc5 19.Bxc5 Re8+ 20.Be3 Kd6 21.O-O-O Rb5 22.Bf4+ 1-0

[Event "ETH-MIT Match"]
[Site "Zurich/Cambridge"]
[Date "1968.11.26"]
[Round "3"]
[White "Charly"]
[Black "Mac Hack VI"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Bc5 5.Nxe5 Qe7 6.Nxc6 dxc6 7.Bc4 Bg4 8.Be2
Bxe2 9.Qxe2 Nxe4 10.d3 Nd6 11.Qxe7+ Kxe7 12.Re1+ Kd7 13.c3 Rae8 14.Rd1 Re2 15.d4 Bb6
16.g4 Rhe8 17.Kg2 f5 18.g5 Nc4 19.b3 Ne3+ 20.Bxe3 R8xe3 21.g6 hxg6 22.d5 R3e4
23.dxc6+ Kxc6 24.Rf1 Rc2 25.a4 Ree2 26.Rd1 Rexf2+  0-1

```

## See also

- [Charlie](Charlie "Charlie")

## External Links

## Chess Program

- [Computer chess via ham radio](http://ljkrakauer.com/LJK/60s/hamchess.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
- [July 1, 2010 letter from Dr. Gerald Tripard](http://ljkrakauer.com/LJK/60s/tripardltr.htm), hosted by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")

## Misc

- [Charly (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Charly_%28disambiguation%29)
- [Charly (name) from Wikipedia](<https://en.wikipedia.org/wiki/Charly_(name)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Outdoor group portrait of a group of Swiss yodelers in costume](https://en.wikipedia.org/wiki/File:Swiss_yodelers.jpg), 1922, Moen Photo Service, [La Crosse, WI](https://en.wikipedia.org/wiki/La_Crosse,_Wisconsin), [Yodeling from Wikipedia](https://en.wikipedia.org/wiki/Yodeling), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> Description taken from [July 1, 2010 letter from Dr. Gerald Tripard](http://ljkrakauer.com/LJK/60s/tripardltr.htm), hosted by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Computer chess via ham radio](http://ljkrakauer.com/LJK/60s/hamchess.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [The first inter-computer chess game via ham radio](http://ljkrakauer.com/LJK/60s/game1list.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [October 30, 1968 letter from Richard Greenblatt to G. Tripard](http://ljkrakauer.com/LJK/60s/greenblattltr.htm)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Games 2 and 3](http://ljkrakauer.com/LJK/60s/games23list.htm)

**[Up one Level](Engines "Engines")**

