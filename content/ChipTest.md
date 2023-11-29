---
title: ChipTest
---
**[Home](Home "Home") * [Engines](Engines "Engines") * ChipTest**

**ChipTest**,

a chess program running on a [Sun-3](Sun#3 "Sun") [workstation](https://en.wikipedia.org/wiki/Computer_workstation) using a high speed [move generator](Move_Generation "Move Generation") in [hardware](Hardware "Hardware"). It was the predecessor of [Deep Thought](Deep_Thought "Deep Thought"), which later emerged to [Deep Blue](Deep_Blue "Deep Blue"). The project started in 1985 by two students at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") who did the chip design of the move generator <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"). Later in 1986 they were joined by [HiTech](HiTech "HiTech") member [Murray Campbell](Murray_Campbell "Murray Campbell"). ChipTest played two [ACM North American Computer Chess Championships](ACM_North_American_Computer_Chess_Championship "ACM North American Computer Chess Championship"), [ACM 1986](ACM_1986 "ACM 1986") and [ACM 1987](ACM_1987 "ACM 1987"), and it won the latter with a perfect score. At ACM 1986, ChipTest searched about 100K [positions per second](Nodes_per_Second "Nodes per Second") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, in 1987 500K <a id="cite-note-3" href="#cite-ref-3">[3]</a>, already employing [singular extensions](Singular_Extensions "Singular Extensions") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Move Generation

The [move generator](Move_Generation "Move Generation"), a [combinational logic](Combinatorial_Logic "Combinatorial Logic") 8x8 [array](Array "Array") is effectively a silicon chessboard in [VLSI design](VLSI_Design "VLSI Design"). The basic move generation algorithm is the same as in the [Belle](Belle "Belle") [move generator](Belle#Hardware "Belle"), where a disable-stack implements the bookkeeping of victims and per victim, of aggressors. In ChipTest and its successors, the last move searched from the position, which need to be stored for [unmake move](Unmake_Move "Unmake Move") anyway, implies the priority levels of the last victim and the last attacking piece is used for the [sequential logic](Sequential_Logic "Sequential Logic") to compute the disable-mask on the fly, using distinct square priorities to discriminate equal valued victims and aggressors <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

```C++
disable = 0;
while ( ( to = findMVV(disable)) >= 0 ) {
  while ( ( from = findLVA(disable)) >= 0 ) {
    make(from, to); 
    ....
    unmake(from, to); 
    disable = allLessAndEqualValuableAttackers(from); 
  }
  disable = allMoreAndEqualValuableVictims(to);
}

```

In software, the cost of recomputing the mask exceeds the cost of retrieving it. But in hardware, the reverse holds true. The disable-stack needs decoders to operate anyway. The modified decoder operates at a speed comparable to the disable-stack decoders and takes less space. This method avoids using the disable-stack, which probably needs to be at least 64 levels deep.

## Evaluation

While features such as [material](Material "Material"), [piece placement](Piece-Square_Tables "Piece-Square Tables"), and some [pawn structures](Pawn_Structure "Pawn Structure") are easier to evaluate in an [incremental](Incremental_Updates "Incremental Updates") way, certain more subtle features require a whole board approach to do the [evaluation](Evaluation "Evaluation") in hardware - aggregated [square control](Square_Control "Square Control") aka [mobility](Mobility "Mobility") of a [Chess 4.5](</Chess_(Program)> "Chess (Program)") like approach <a id="cite-note-7" href="#cite-ref-7">[7]</a>, and [pins](Pin "Pin") <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Selected Games

## Bebe

[ACM 1986](ACM_1986 "ACM 1986"), round 1, [Bebe](Bebe "Bebe") - ChipTest

```

[Event "ACM 1986"]
[Site "Dallas USA"]
[Date "1986.11.02"]
[Round "1"]
[White "Bebe"]
[Black "Chiptest"]
[Result "1-0"]

1.e4 e6 2.d4 d5 3.Nd2 dxe4 4.Nxe4 Qd5 5.Nc3 Bb4 6.Nge2 Qd8 7.a3 Bd6
8.g3 Nf6 9.Bg2 Nc6 10.O-O Bd7 11.Bg5 h6 12.Bxf6 Qxf6 13.Ne4 Qf5 14.d5 exd5
15.Nxd6+ cxd6 16.Nf4 O-O-O 17.Re1 d4 18.Bxc6 Bxc6 19.Qxd4 g5 20.Qd3 Qf6
21.Nd5 Qxb2 22.Rab1 Qg7 23.Ne7+ Kc7 24.Nxc6 Rd7 25.Qb5 b6 26.Nxa7 Qd4
27.Qc6+ Kb8 28.Qxd7 Qd5 29.Nc6+ Qxc6 30.Qxc6 d5 31.Rxb6+ Ka7 32.Qb7# 1-0

```

## Cray Blitz

[ACM 1987](ACM_1987 "ACM 1987"), round 3, [Cray Blitz](Cray_Blitz "Cray Blitz") - Chiptest M

```

[Event "ACM 1987"]
[Site "Dallas, USA"]
[Date "1987.10.26"]
[Round "3"]
[White "Cray Blitz"]
[Black "Chiptest M"]
[Result "0-1"]

1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 c6 5.Nf3 Nf6 6.Bc4 Bg4 7.h3 Bh5
8.Qe2 Nbd7 9.Bd2 Qc7 10.g4 Bg6 11.O-O-O O-O-O 12.Ng5 e5 13.Bxf7 exd4
14.Na4 Ne5 15.Bxg6 Nxg6 16.Ne6 Re8 17.Rhe1 Qd6 18.g5 Nd7 19.Qg4 b5
20.Nac5 Nge5 21.Nxf8 Rhxf8 22.Ne4 Qd5 23.Qg2 Re6 24.Kb1 Nf3 25.Qg4 
Nxe1 26.Rxe1 Ne5 27.Qd1 Nf3 0-1

```

## Sun Phoenix

[ACM 1987](ACM_1987 "ACM 1987"), round 4, Chiptest M - [Sun Phoenix](Phoenix "Phoenix") <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```

[Event "ACM 1987"]
[Site "Dallas, USA"]
[Date "1987.10.27"]
[Round "4"]
[White "Chiptest M"]
[Black "Sun Phoenix"]
[Result "1-0"]

1.e4 c6 2.d4 d5 3.Nc3 g6 4.h3 Bg7 5.Nf3 Nf6 6.e5 Ne4 7.Nxe4 dxe4
8.Ng5 c5 9.dxc5 Qa5+ 10.c3 Qxc5 11.Qd4 Qxe5 12.Qxe5 Bxe5 13.Bc4 O-O
14.O-O Bd7 15.Rd1 Ba4 16.Re1 Nd7 17.Bd5 Nc5 18.Nxe4 Nd3 19.Re2 Bc6
20.Bxc6 Nxc1 21.Rxc1 bxc6 22.Nc5 Bf4 23.Rce1 Rfb8 24.g3 Bd6 25.Ne4 
Bc7 26.f4 Rd8 27.Kg2 Rd5 28.c4 Rd4 29.c5 Ba5 30.Rf1 Rad8 31.Rff2 Bb4 
32.a3 Ba5 33.Ng5 Re8 34.f5 Rd3 35.fxg6 fxg6 36.Nf3 Bc7 37.Re6 Bb8 
38.Rxc6 Re3 39.g4 e5 40.Ng5 Rb3 41.Re6 Rxe6 42.Nxe6 h5 43.c6 e4 
44.c7 Bxc7 45.Nxc7 1-0

```

## See also

- [Belle](Belle "Belle")
- [Deep Thought](Deep_Thought "Deep Thought")
- [Deep Blue](Deep_Blue "Deep Blue")
- [Deep Blue | Down the Rabbit Hole Video](Deep_Blue#DowntheRabbitHole "Deep Blue")

## Publications

- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1986**). *[Two designs of functional units for VLSI based chess machines](http://repository.cmu.edu/compsci/1566/)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Computer Science Department. Paper 1566.
- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1987**). *A Two-Million Moves/Sec CMOS Single-Chip Chess Move Generator*. [IEEE Journal of Solid-state Circuits](IEEE#JSSC "IEEE"), Vol. 22, No. 5
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1988**). *Singular extensions: Adding Selectivity to Brute-Force Searching*. [AAAI](AAAI "AAAI") Spring Symposium, Computer Game Playing, also in [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), and (**1990**) in [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1

## External Links

- [ChipTest from Wikipedia](https://en.wikipedia.org/wiki/ChipTest)
- [The chess games of Chiptest](http://www.chessgames.com/perl/chessplayer?pid=15594) from [chessgames.com](http://www.chessgames.com/index.html)
- [Manu Dibango](Category:Manu_Dibango "Category:Manu Dibango") - Sun Explosion, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1987**). *A Two-Million Moves/Sec CMOS Single-Chip Chess Move Generator*. [IEEE Journal of Solid-state Circuits](IEEE#JSSC "IEEE"), Vol. 22, No. 5
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The ACM's Seventeenth North American Computer Chess Championship and The Sixth World Microcomputer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6ca4a7) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1986_17th_NACCC/1986%20NACCC.062303062.sm.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [The ACM's Eighteenth North American Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cabbd) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1987_18th_NACCC/1987%20NACCC.062303063.sm.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1988**). *Singular extensions: Adding Selectivity to Brute-Force Searching*. AAAI Spring Symposium, Computer Game Playing, pp. 8-13. Also published in [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), republished (1990) in [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1986**). *[Two designs of functional units for VLSI based chess machines](http://repository.cmu.edu/compsci/1566/)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Computer Science Department. Paper 1566
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1999**). *IBM’s Deep Blue Chess Grandmaster Chips*. [IEEE Micro](IEEE#Micro "IEEE"), Vol. 19, No. 2
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *Chess 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1986**). *[Two designs of functional units for VLSI based chess machines](http://repository.cmu.edu/compsci/1566/)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), Computer Science Department. Paper 1566.
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Monty Newborn](Monroe_Newborn "Monroe Newborn"), [Danny Kopec](Danny_Kopec "Danny Kopec") (**1988**). *Results of ACM's Eighteenth Computer Chess Championship*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 31, No. 8, [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_30_C.pdf)

**[Up one Level](Engines "Engines")**

