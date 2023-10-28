---
title: Delicate Brute
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Delicate Brute**

**Delicate Brute**,

an experimental chess program by [Don Beal](Don_Beal "Don Beal") written in [C](C "C"), which participated at the [ACM 1991](ACM_1991 "ACM 1991") and the [WCCC 1992](WCCC_1992 "WCCC 1992"), running on a [Sun-4](Sun#4 "Sun") [workstation](https://en.wikipedia.org/wiki/Workstation) and about 4K [nodes per second](Nodes_per_Second "Nodes per Second") in 1991, and at the WMCCC on a [Sun Sparc II](SPARCstation "SPARCstation") with about 10K Nps <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Apparently, Delicate Brute was a [brute-force](Brute-Force "Brute-Force") approach enhanced by [selectivity](Selectivity "Selectivity") as introduced by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
such as using the [null move quiescence search](Null_Move_Pruning#NMQS "Null Move Pruning"), a selective layer between a regular full width search and [quiescence search](Quiescence_Search "Quiescence Search"), later dubbed **Generalized Quiescence Search** <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 ACM 1991](#acm-1991)
  - [1.1 Round 1](#round-1)
  - [1.2 Round 2](#round-2)
  - [1.3 Round 3](#round-3)
  - [1.4 Round 4](#round-4)
  - [1.5 Round 5](#round-5)
- [2 See also](#see-also)
- [3 External Links](#external-links)
  - [3.1 Chess Program](#chess-program)
  - [3.2 Misc](#misc)
- [4 References](#references)

## ACM 1991

Excerpt from [Danny Kopec](Danny_Kopec "Danny Kopec"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [Michael Valvo](Michael_Valvo "Michael Valvo") *The 22d Annual ACM International Chess Championship* <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

## Round 1

Delicate Brute played an interesting pawn sacrifice against [M Chess](MChess "MChess"), but could never convert its temporal advantages into anything concrete. After that, M Chess was in complete command.

```

[Event "ACM 1991"]
[Site "Albuquerque, USA"]
[Date "1991.11.12"]
[Round "1"]
[White "Delicate Brute"]
[Black "M-Chess"]
[Result "0-1"]

1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.d4 cxd4 5.cxd4 d6 6.Bc4 Nb6 7.Bb5+ Bd7 8.e6 fxe6 9.Bd3 g6 
10.h4 Ba4 11.Qg4 Qc8 12.Ne2 Nd5 13.O-O Bc6 14.Nbc3 Nf6 15.Qh3 Bg7 16.Nf4 Bd7 17.Bb5 Nc6 
18.Bxc6 bxc6 19.Qd3 O-O 20.Re1 Ng4 21.f3 Nh6 22.h5 Nf5 23.hxg6 Bxd4+ 24.Kh1 e5 25.gxh7+ 
Kxh7 26.g4 Rh8 27.b4 Kg8+ 28.Nh5 Ng3+ 29.Kg2 Nxh5 30.gxh5 Bh3+ 31.Kg3 Bf5 32.Qc4+ d5 
33.Qb3 Rxh5 34.Bb2 Kh8 35.Ba3 Qg8# 0-1

```

## Round 2

Delicate Brute played beautiful chess against [Zarkov](Zarkov "Zarkov"), but eventually fell prey to some tactical nuances. Even then, a draw was possible.

```

[Event "ACM 1991"]
[Site "Albuquerque, USA"]
[Date "1991.11.12"]
[Round "2"]
[White "Zarkov"]
[Black "Delicate Brute"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 b6 5.Bd3 Bb7 6.Nf3 Ne4 7.O-O Bxc3 8.bxc3 f5 9.Bxe4 Bxe4 
10.Ba3 d6 11.Qe2 O-O 12.Nd2 Bb7 13.Bb2 Qf6 14.Rae1 Nd7 15.f4 Rfe8 16.Nf3 e5 17.fxe5 dxe5 
18.Rd1 f4 19.exf4 exf4 20.Qc2 Be4 21.Qd2 Qc6 22.Qxf4 Qxc4 23.Nd2 Qc6 24.Nxe4 Rxe4 25.Qf7+ 
Kh8 26.Rde1 Rxe1 27.Rxe1 Rf8 28.Re8 Qf6 29.Qxf6 gxf6 30.Re7 Rd8 31.Bc1 c5 32.Bf4 Nf8 
33.Bh6 Nd7 34.Kf2 cxd4 35.Bg7+ Kg8 36.cxd4 a5 37.g4 b5 38.Ke2 b4 39.Kd2 a4 40.h3 a3 
41.Kc2 Rc8+ 42.Kb1 Rd8 43.h4 h5 44.gxh5 f5 45.h6 f4 46.d5 f3 47.Bd4 Kf8 48.d6 Nf6 
49.Re3 Nh7 50.Rxf3+ Ke8 51.Re3+ Kf7 52.Re7+ Kg6 53.d7 Nf8 54.h7 Nxh7 55.Bb6 1-0

```

## Round 3

Delicate Brute vs. [Bebe](Bebe "Bebe") was a back-and-forth game where Delicate Brute seemingly held the upper hand most of the time. Then, for some strange reason, Delicate Brute refused to play the winning idea of creating a [passed](Passed_Pawn "Passed Pawn") queen's rook pawn and actually helped Bebe create counterplay in the form of a Bebe passed king pawn. After that, Bebe was without mercy.

```

[Event "ACM 1991"]
[Site "Albuquerque, USA"]
[Date "1991.11.12"]
[Round "3"]
[White "Delicate Brute"]
[Black "Bebe"]
[Result "0-1"]

1.e4 c5 2.c3 d6 3.d4 Nf6 4.f3 cxd4 5.cxd4 e5 6.Nc3 Be7 7.dxe5 dxe5 8.Qxd8+ Bxd8 9.Be3 Be6 
10.O-O-O Bb6 11.Bxb6 axb6 12.Bb5+ Nc6 13.Bxc6+ bxc6 14.Rd6 Ra6 15.Nge2 Ke7 16.Rhd1 Rc8 
17.Kb1 Nd5 18.Rxe6+ fxe6 19.exd5 exd5 20.b3 Rd8 21.h4 b5 22.Kb2 d4 23.Ne4 Ra7 24.Nc1 Kf8 
25.Nd3 Rda8 26.Ra1 Rd8 27.Rc1 Rda8 28.Nb4 Rc7 29.Rxc6 Rxc6 30.Nxc6 Re8 31.Na7 Rb8 32.Nc6 
Re8 33.Nc5 Kf7 34.Nd7 e4 35.Nxd4 e3 36.Nc2 e2 37.Ne1 Rc8 38.Ne5+ Kf6 39.f4 Kf5 40.N1d3 Ke4 
41.g3 Ke3 42.Ne1 Kf2 43.N5f3 b4 44.g4 Rc3 45.Nd4 Kxe1 46.a3 Rd3 47.Nxe2 bxa3+ 48.Kxa3 Kxe2 
49.f5 Rd5 50.b4 Kf3 51.g5 Rxf5 52.Kb3 Kg4 0-1

```

## Round 4

[Lachex](Lachex "Lachex") vs. Delicate Brute was interesting in that White had nearly all its pawns advanced and all its pieces on the first rank at one point. Delicate Brute was unable to cope with all these goings on and was mated in less than 30 moves.

```

[Event "ACM 1991"]
[Site "Albuquerque, USA"]
[Date "1991.11.12"]
[Round "4"]
[White "Lachex"]
[Black "Delicate Brute"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3+ 5.bxc3 c5 6.f3 cxd4 7.cxd4 O-O 8.g4 d5 9.e4 dxe4 
10.g5 Nfd7 11.fxe4 f5 12.exf5 exf5 13.Nf3 f4 14.Bd3 Re8+ 15.Kf2 Qc7 16.Qd2 Rf8 17.Qc2 g6 
18.c5 Kh8 19.Bb2 Kg7 20.Rae1 Qa5 21.Re7+ Rf7 22.Re8 Rf8 23.Qe2 Rxe8 24.Qxe8 Nc6 25.Bc4 Qd8 
26.Qf7+ Kh8 27.d5+ Nce5 28.Nxe5 Nf6 29.Nd7 h5 30.Nf8 Qxf8 31.Bxf6+ 1-0

```

## Round 5

Delicate Brute was doing well as Black in a Petroff Defense against [Socrates](Socrates "Socrates") until 12...g5. [Don Beal](Don_Beal "Don Beal"), the programmer, explained that the machine has no [king safety](King_Safety "King Safety") criteria and such moves are the result. Socrates soon thereafter put several pieces [en prise](En_prise "En prise") enroute to a mating attack.

```

[Event "ACM 1991"]
[Site "Albuquerque, USA"]
[Date "1991.11.12"]
[Round "5"]
[White "Socrates"]
[Black "Delicate Brute"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Nc6 7.O-O Bg4 8.Re1 f5 9.c3 Be7 
10.h3 Bh5 11.Bf4 O-O 12.Qc2 g5 13.Bh2 Qc8 14.Nbd2 Bxf3 15.Nxf3 Rd8 16.Rad1 a5 17.Ne5 Nxe5 
18.Bxe5 Bd6 19.Bxd6 Rxd6 20.f3 Ng3 21.Kh2 f4 22.Re7 h5 23.Bg6 b6 24.Bf7+ Kf8 25.Bxh5 Nxh5 
26.Qh7 1-0

```

## See also

- [Brute-Force](Brute-Force "Brute-Force")
- [Brute Force (Program)](</Brute_Force_(Program)> "Brute Force (Program)")

## External Links

## Chess Program

- [Delicate Brute's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=230)

## Misc

- [delicate - Wiktionary](https://en.wiktionary.org/wiki/delicate)
- [brute - Wiktionary](https://en.wiktionary.org/wiki/brute)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1992**). *The 7th World Computer-Chess Championship. Report on the Tournament*. [ICCA Journal, Vol. 15, No. 4](ICGA_Journal#15_4 "ICGA Journal")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Don Beal](Don_Beal "Don Beal") (**1986**). *Selective Search without Tears.* [ICCA Journal, Vol. 9, No. 2](ICGA_Journal#9_2 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), A revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Danny Kopec](Danny_Kopec "Danny Kopec"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [Michael Valvo](Michael_Valvo "Michael Valvo") (**1992**). *The 22d Annual ACM International Chess Championship*, in [The 23rd ACM International Computer Chess Championship](https://www.computerhistory.org/chess/doc-431614f6cc6e9/) hosted by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

**[Up one Level](Engines "Engines")**

