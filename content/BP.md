---
title: BP
---
**[Home](Home "Home") * [Engines](Engines "Engines") * BP**

[](File:CullumBPGurevich1991.jpg) [Robert Cullum](Robert_Cullum "Robert Cullum") with BP vs. [Dmitry Gurevich](https://en.wikipedia.org/wiki/Dmitry_Gurevich) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**BP**, (Mulder BP)

a chess program by [Robert Cullum](Robert_Cullum "Robert Cullum"). BP was a [selective](Selectivity "Selectivity") program written in [C](C "C") and [x86](X86 "X86") [assembly](Assembly "Assembly") language to run on a [Compaq 386](https://en.wikipedia.org/wiki/Compaq_Deskpro_386#Deskpro_386) [IBM PC](IBM_PC "IBM PC") or compatible <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Descriptions](#descriptions)
  - [1.1 WCCC 1989](#wccc-1989)
  - [1.2 ACM 1991](#acm-1991)
- [2 Tournament Play](#tournament-play)
- [3 Selected Games](#selected-games)
  - [3.1 WCCC 1989](#wccc-1989-2)
  - [3.2 Illinois Open 1991](#illinois-open-1991)
- [4 External Links](#external-links)
- [5 References](#references)

## Descriptions

## [WCCC 1989](WCCC_1989 "WCCC 1989")

from the booklet *Kings Move - Welcome to the 1989 AGT World Computer Chess Championship* <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```C++
BP spends 95% of its time in [evaluation](Evaluation "Evaluation") and the rest on [move generation](Move_Generation "Move Generation") and [search](Search "Search"). Because of this, it must do a selective search, to [prune forward](Pruning "Pruning") at every level of the [search tree](Search_Tree "Search Tree"). 

```

## [ACM 1991](ACM_1991 "ACM 1991")

given by [Garth Courtois Jr.](Garth_Courtois_Jr. "Garth Courtois Jr."), who had the opportunity to talk with some programmers during the [ACM 1991](ACM_1991 "ACM 1991") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
BP, in an n-[ply](Ply "Ply") [iterative-deepening](Iterative_Deepening "Iterative Deepening") process, does some [forward pruning](Pruning "Pruning") even at ply 1. There are good, interesting, and bad [moves](Moves "Moves"). Good ones appear to win [material](Material "Material"). Interesting ones exchange material, or are the [best move](Best_Move "Best Move") in a previous iteration. Bad moves appear to lose material. There is also consideration given to [tactical](Tactics "Tactics") conditions, such as whether there is a [piece](Pieces "Pieces") under attack or if the machine is retreating from [check](Check "Check"). At ply 1 during early iterations all possible moves are examined. At ply 1 and 2 the good and interesting moves are fully explored, but the bad moves are pruned at n-2. Near the bottom of the tree some "serious pruning" is enacted. BP has a 65K [position table](Transposition_Table "Transposition Table") and would like to make this larger for endgames. It runs on a 33 MHz [486](X86 "X86") processor. The iterative deepening goes in steps: 2,4, ... n-2, n. When they announce a 6-ply analysis, it is a pseudo-6 ply of full width. They examine approximately 1600 [nodes/sec](Nodes_per_Second "Nodes per Second"). Part of the BP philosophy is expressed: "If we [prune](Parity_Pruning "Parity Pruning") on a even ply, and omit a good move, it is a shame. If we prune on an odd ply and omit a good move, it is a disaster." 

```

## Tournament Play

BP played five [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), the [ACM 1987](ACM_1987 "ACM 1987"), [ACM 1988](ACM_1988 "ACM 1988"), [ACM 1989](ACM_1989 "ACM 1989"), [ACM 1991](ACM_1991 "ACM 1991") and [ACM 1993](ACM_1993 "ACM 1993"), as well the [WCCC 1989](WCCC_1989 "WCCC 1989") in [Edmonton](https://en.wikipedia.org/wiki/Edmonton), [Alberta](https://en.wikipedia.org/wiki/Alberta), [Canada](https://en.wikipedia.org/wiki/Canada) <a id="cite-note-5" href="#cite-ref-5">[5]</a> operated by [Kevin O’Connell](Kevin_O%E2%80%99Connell "Kevin O’Connell").
In 1991, BP played the *Illinois Open*, where it became runner-up with a win versus GM [Dmitry Gurevich](https://en.wikipedia.org/wiki/Dmitry_Gurevich) <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Selected Games

## WCCC 1989

[WCCC 1989](WCCC_1989 "WCCC 1989"), round 2, Mulder BP - [Pandix](Pandix "Pandix") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

```

[Event "WCCC 1989"]
[Site "Edmonton, Canada"]
[Date "1989.05.28"]
[Round "2"]
[White "Mulder BP"]
[Black "Pandix"]
[Result "1-0"]

1.e4 e5 2.f4 f5 3.exf5 Qh4+ 4.g3 Qe7 5.fxe5 Qxe5+ 6.Qe2 Nc6 7.d4 Qxe2+ 8.Nxe2 d5 9.Bh3 Bd6 10.Nbc3 
Nge7 11.Bg5 Nxf5 12.O-O-O Nfxd4 13.Nxd4 Bxh3 14.Rhe1+ Kf7 15.Ndb5 d4 16.Nxd6+ cxd6 17.Nb5 Kg6 18.Bf4 
Bg4 19.Rd3 Rae8 20.Rxe8 Rxe8 21.Nxd4 Nxd4 22.Rxd4 Re1+ 23.Kd2 Re2+ 24.Kc3 Rxh2 25.Rxd6+ Kf7 26.Rd2 
Rxd2 27.Kxd2 b5 28.b3 h5 29.c4 bxc4 30.bxc4 Be6 31.Kd3 g6 32.a4 Bd7 33.a5 a6 34.Kd4 Kf6 35.Bc7 g5 
36.Bd8+ Kf5 37.c5 Bc6 38.Be7 Kg4 39.Ke5 h4 40.gxh4 gxh4 41.Ke6 h3 42.Bd6 Kf3 43.Be5 Kg2 44.Kd6 Bf3 
45.c6 h2 46.Bxh2 Kxh2 47.Kd7 Bg4+ 48.Kd8 Bf3 49.c7 Bg4 50.c8=Q Bxc8 51.Kxc8 Kg3 52.Kb7 1-0 

```

## Illinois Open 1991

Illinois Open, round 3, BP - [Dmitry Gurevich](https://en.wikipedia.org/wiki/Dmitry_Gurevich) <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```

[Event "Illinois Open"]
[Site "Rosemont, IL"]
[Date "1991.??.??"]
[Round "3"]
[White "BP"]
[Black "Dmitry Gurevich"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Nxc6 bxc6 8.e5 Nd5 9.Nxd5 cxd5 
10.Qxd5 Rb8 11.O-O-O Qc7 12.f4 O-O 13.b3 Rb6 14.Bxb6 axb6 15.Bc4 Qa7 16.a4 e6 17.Qd6 f6 
18.exf6 Bxf6 19.Rhe1 Qa5 20.Re3 Bg7 21.Bb5 Qa8 22.g3 Rf7 23.Qxb6 Bf8 24.Qd8 Kg7 25.Rxd7
Rxd7 26.Bxd7 Ba3+ 27.Kd2 Qd5+ 28.Rd3 Qg2+ 29.Kc3 Qe4 30.Qb6 Qe1+ 31.Rd2 Be7 32.Bxc8 Bf6+ 
33.Kd3 Qf1+ 34.Ke3 Qe1+ 35.Re2 Qc3+ 36.Ke4 Qxc8 37.c4 Qa8+ 38.Kd3 Qf3+ 39.Qe3 Qf1 40.Kc2 
Qa1 41.Rd2 Qb2+ 42.Kd1 Qa1+ 43.Ke2 Qh1 44.Rd7+ Kh6 45.h4 Qg2+ 46.Ke1 Qh1+ 47.Kf2 Qh2+ 
48.Kf3 Qh1+ 49.Kg4 1-0

```

## External Links

- [Mulder BP's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=358)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Photo from [Dmitry Gurevich](https://en.wikipedia.org/wiki/Dmitry_Gurevich) (**1991**). *On The Road*. Illinois Chess Bulletin, [pdf](http://il-chess.net/icb_pdf/ICB_1991_11_12.pdf) » [Illinois Open 1991](#illinois-open-1991)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [The ACM's Eighteenth North American Computer Chess Championship](https://www.computerhistory.org/chess/doc-431614f6cabbd/) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](https://www.computerhistory.org/chess/doc-434fea055cbb3/) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Garth Courtois Jr.](Garth_Courtois_Jr. "Garth Courtois Jr.") (**1991**). *Where is Computer Chess Going?* [ICCA Journal, Vol. 14, No. 4](ICGA_Journal#14_4 "ICGA Journal")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Mulder BP's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=358)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> Ken Marshall (**1991**). *Andrew Karklins Wins Illinois Open - GM Gurevich Upset By Computer Program Bp'\*. Illinois Chess Bulletin, [pdf](http://il-chess.net/icb_pdf/ICB_1991_11_12.pdf)*
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Edmonton 1989 - Chess - Round 2 - Game 10 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=14&round=2&id=10)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Dmitry Gurevich](https://en.wikipedia.org/wiki/Dmitry_Gurevich) (**1991**). *On The Road*. Illinois Chess Bulletin, [pdf](http://il-chess.net/icb_pdf/ICB_1991_11_12.pdf)

**[Up one level](Engines "Engines")**

