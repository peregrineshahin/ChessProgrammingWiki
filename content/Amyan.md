---
title: Amyan
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Amyan**

[](http://www.pincha.cl/amyan/amyane.jpg) Amyan 1.522 [GUI](GUI "GUI") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Amyan**,

a chess engine written by [Antonio Dieguez](Antonio_Dieguez "Antonio Dieguez") running under [Windows](Windows "Windows"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard"), and the [Universal Chess Interface](UCI "UCI") (UCI).
Amyan was first released in 2000, the still available Amyan 1.522 Version released in 2002 comes with an own [GUI](GUI "GUI"). The program is written in [C++](Cpp "Cpp"), a ported [Java](Java "Java") [applet](https://en.wikipedia.org/wiki/Java_applet) is able to run in a [Web browser](https://en.wikipedia.org/wiki/Web_browser) using a [Java virtual machine](https://en.wikipedia.org/wiki/Java_virtual_machine) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Tournament Play

Amyan played the [CCT4](CCT4 "CCT4"), [CCT5](CCT5 "CCT5") and [CCT6](CCT6 "CCT6") [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), and became the **First Annual** [ACCA Americas' Computer Chess Champion](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship") at [ACCA 2006](ACCA_2006 "ACCA 2006"), to further play the [ACCA 2009](ACCA_2009 "ACCA 2009"). At the [4th Chess Computer Cup 2008](CCC_2009 "CCC 2009") in [Carugate](https://en.wikipedia.org/wiki/Carugate), [Italy](https://en.wikipedia.org/wiki/Italy), Amyan was tied with winner [DanaSah](DanaSah "DanaSah"), both with 5/6 and also equal [sum of opponent scores](https://en.wikipedia.org/wiki/Buchholz_system), but Amyan played the draw versus [Chiron](Chiron "Chiron") in round 2, DanaSah in round 5 gaining higher [cumulative score](https://en.wikipedia.org/wiki/Tie-breaking_in_Swiss-system_tournaments#Cumulative).

## Description

<a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## [Board Representation](Board_Representation "Board Representation")

Amyan's [mailbox](Mailbox "Mailbox") board array has index 11 for a1 and 88 for h8, so it is apparently a 10\*10 board with following index mapping. It further uses [bitboards](Bitboards "Bitboards") mainly for [pawns](Pawn_Pattern_and_Properties "Pawn Pattern and Properties").

```C++

int mailbox[100] = {
   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
   -1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
   -1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
   -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
   -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
   -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
   -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
   -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
   -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
};

int mailbox64[64] = {
   11, 12, 13, 14, 15, 16, 17, 18,
   21, 22, 23, 24, 25, 26, 27, 28,
   31, 32, 33, 34, 35, 36, 37, 38,
   41, 42, 43, 44, 45, 46, 47, 48,
   51, 52, 53, 54, 55, 56, 57, 58,
   61, 62, 63, 64, 65, 66, 67, 68,
   71, 72, 73, 74, 75, 76, 77, 78,
   81, 82, 83, 84, 85, 86, 87, 88,
};

```

## [Search](Search "Search")

- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with [R=2](Depth_Reduction_R "Depth Reduction R")
- [Killer Heuristic](Killer_Heuristic "Killer Heuristic") with several [Killer moves](Killer_Move "Killer Move")
- [Futility Pruning](Futility_Pruning "Futility Pruning")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Captures](Captures "Captures") [ordered](Move_Ordering "Move Ordering") by [MVV-LVA](MVV-LVA "MVV-LVA")
- [Extensions](Extensions "Extensions") restricted to one [ply](Ply "Ply") per line, except [Check evasions](Check_Extensions "Check Extensions")
- [Transposition Table](Transposition_Table "Transposition Table")

## [Evaluation](Evaluation "Evaluation")

- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables") for [knights](Knight "Knight"), [bishops](Bishop "Bishop") and [queens](Queen "Queen")
- [Mobility](Mobility "Mobility") considering [King](King "King") and [Center](Center "Center")
  - [Rooks on (semi) open files](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
- [Knight outposts](Outposts "Outposts")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Pawn Center](Pawn_Center "Pawn Center")
  - [Passed Pawns](Passed_Pawn "Passed Pawn")
    - [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
    - [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")
    - [Tarrasch Rule](Tarrasch_Rule "Tarrasch Rule")
- [King Safety](King_Safety "King Safety")
  - [King Tropism](King_Safety#KingTropism "King Safety")
  - [Pawn Storms](King_Safety#PawnStorm "King Safety")
- [Scoring](Score "Score") of some [Pins](Pin "Pin")

## Selected Games

[ACCA 2006](ACCA_2006 "ACCA 2006"), round 2, Amyan - [Crafty](Crafty "Crafty") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "ACCA 2006"]
[Site "ICC"]
[Date "2006.11.08"]
[Round "2"]
[White "Amyan"]
[Black "Crafty"]
[Result "1-0"]

1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d5 5.cxd5 Nxd5 6.e4 Nxc3 7.bxc3 c5
8.Bb5+ Bd7 9.Be2 cxd4 10.cxd4 Bc6 11.Qc2 Bxd4 12.Nxd4 Qxd4 13.Bb2
Qb4+ 14.Bc3 Qc5 15.O-O O-O 16.Rac1 Rd8 17.Qb2 Qg5 18.f4 Qh6 19.Ba5
Rd7 20.Rc4 b6 21.Bb4 a5 22.Bd2 Rd8 23.Rfc1 Be8 24.Be3 Nd7 25.e5 e6
26.Rc7 a4 27.Bb5 Qh5 28.Qf2 Qf5 29.Be2 g5 30.g4 Qg6 31.h4 gxh4 32.
Qxh4 Nc5 33.Bf3 Rab8 34.Bg2 Rd3 35.Re1 Qg7 36.g5 Rc3 37.Re2 Qg6 38.
Bxc5 Rxc5 39.Rxc5 bxc5 40.Be4 Qg7 41.Rh2 h6 42.Qf2 hxg5 43.Qxc5 Rd8
44.Bh7+ Qxh7 45.Rxh7 Kxh7 46.Qe7 Rb8 47.Qxg5 Rb1+ 48.Kf2 Bb5 49.Ke3
Rf1 50.Qg2 Re1+ 51.Kd4 Rc1 52.Qb7 Rc4+ 53.Ke3 Be8 54.Qe7 Rc3+ 55.Kd4
Rc8 56.f5 exf5 57.e6 Kg6 58.Ke5 1-0

```

## See also

- [Amy](Amy "Amy")
- [AnMon](AnMon "AnMon")

## Forum Posts

## 2000 ...

- [interesting game, Crafty vs Amyan](https://www.stmintz.com/ccc/index.php?id=129898) by [Antonio Dieguez](Antonio_Dieguez "Antonio Dieguez"), [CCC](CCC "CCC"), September 18, 2000
- [About Pepito and Amyan](https://www.stmintz.com/ccc/index.php?id=130421) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), September 24, 2000 » [Pepito](Pepito "Pepito")
- [CCT5 - ok, a short comment, just Amyan...](https://www.stmintz.com/ccc/index.php?id=278556) by [Antonio Dieguez](Antonio_Dieguez "Antonio Dieguez"), [CCC](CCC "CCC"), January 20, 2003 » [CCT5](CCT5 "CCT5")
- [Older Versions of Amyan](http://www.talkchess.com/forum/viewtopic.php?t=24553) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), October 24, 2008
- [just amyan...](http://www.talkchess.com/forum/viewtopic.php?t=29748) by [Antonio Dieguez](Antonio_Dieguez "Antonio Dieguez"), [CCC](CCC "CCC"), September 14, 2009
- [Amyan 1.6 : 2477](http://www.talkchess.com/forum/viewtopic.php?t=29788) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), September 17, 2009
- [Amyan 1.71 : 2490](http://www.talkchess.com/forum/viewtopic.php?t=30204) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), October 18, 2009
- [move in the pv at starting position](http://www.talkchess.com/forum/viewtopic.php?t=30486) by [Antonio Dieguez](Antonio_Dieguez "Antonio Dieguez"), [CCC](CCC "CCC"), November 05, 2009

## 2010 ...

- [A superb personality of Amyan 1.72...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=42409) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), February 10, 2012

## External Links

- [Amyan \<- Antonio Diéguez](http://www.pincha.cl/amyan/)
- [Amyan \<- Antonio Diéguez](http://www.pincha.cl/amyan/amyane.html)
- [Amyan](http://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Amyan&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [The chess games of Amyan](http://www.chessgames.com/perl/chessplayer?pid=125295) from [chessgames.com](http://www.chessgames.com/index.html)
- [Descriptions - Hispanic Chess Engines](https://sites.google.com/site/hispanicchessengines/hispanic-american-engines-1/description)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Amyan \<- Antonio Diéguez](http://www.pincha.cl/amyan/amyane.html), Amyan [1.522 screenshot](http://www.pincha.cl/amyan/amyane.jpg)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Amyan ...](http://www.pincha.cl/jueguitos/amyanjava/applete.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Description loosely based on readme.txt, Amyan 1.72, [Amyan \<- Antonio Diéguez](http://www.pincha.cl/amyan/amyane.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [The 2006 First Annual ACCA Americas' Computer Chess Championships - Results - PGN download](http://compchess.org/2006ACCCResults.html)

**[Up one Level](Engines "Engines")**

