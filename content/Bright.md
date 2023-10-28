---
title: Bright
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bright**

\[ Decreasing [brightness](https://en.wikipedia.org/wiki/Brightness) with [depth](Depth "Depth") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bright** (Brightchess),

an [UCI](UCI "UCI") compatible chess engine by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), written in [C++](Cpp "Cpp") based on the [0x88](0x88 "0x88") board representation, running as 32-bit executable under [Windows](Windows "Windows").
Bright's complex [evaluation](Evaluation "Evaluation") considers things such as [x-ray](X-ray "X-ray") attacks on the king.
Allard Siemelink developed a statistical analysis tool to tune it for maximum concordance with human assessment of almost all evaluation aspects based on a large number of quality human games.
Able to [search in parallel](Search "Search"), Bright basically applies a [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") algorithm. Since splitting is a cheap operation in Bright, avoiding an expensive copy of the board and associated data, the [search tree](Search_Tree "Search Tree") can be split at any [depth](Depth "Depth"), maximizing the use of the otherwise idle cores.
[Late Move Reductions](Late_Move_Reductions "Late Move Reductions") as popularized by [Fruit](Fruit "Fruit") and [Glaurung](Glaurung "Glaurung") are used in Bright with different implementation details. The reductions are not [history](History_Heuristic "History Heuristic") based, and all moves, except the first one, can be reduced by one [ply](Ply "Ply") depending on static criteria <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

## Contents

- [1 Tournament Play](#tournament-play)
- [2 Selected Games](#selected-games)
  - [2.1 Thinker](#thinker)
  - [2.2 Fruit](#fruit)
- [3 Release Dates](#release-dates)
- [4 See also](#see-also)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
  - [6.1 Chess Engine](#chess-engine)
  - [6.2 Misc](#misc)
- [7 References](#references)

## Tournament Play

Bright played a strong [CCT11](CCT11 "CCT11") and became runner-up along with [Fruit](Fruit "Fruit") behind [Rybka](Rybka "Rybka"), and after Rybka's disqualification in 2011 co-champion <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Selected Games

## Thinker

[CCT11](CCT11 "CCT11"), Round 2, Bright - [Thinker](Thinker "Thinker")

```

[Event "[Event "CCT11"]"]
[Site "Internet Chess Club"]
[Date "2009.03.21"]
[Round "2"]
[White "Bright"]
[Black "Thinker"]
[Result "1/2-1/2"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 c6 5.e3 Nbd7 6.Qc2 Bd6 7.Be2 O-O 8.O-O Qe7 9.Rd1 dxc4 10.Bxc4 e5 
11.Bb3 e4 12.Nd2 Re8 13.f3 exf3 14.Nxf3 Nf8 15.Rf1 c5 16.Ng5 Be6 17.Bxe6 fxe6 18.Nge4 N8d7 19.Kh1 
a6 20.a4 Rac8 21.Qb3 Rc6 22.Bd2 Rb8 23.Be1 c4 24.Qc2 Nxe4 25.Qxe4 Nf6 26.Qf3 Rf8 27.Bh4 Qe8 28.Bxf6 
Rxf6 29.Qg4 Rg6 30.Qe2 Rh6 31.h3 Qh5 32.Qc2 Be7 33.Rf3 Rf6 34.Rxf6 Bxf6 35.Rf1 Be7 36.Qe4 Qg6 37.Qxg6 
hxg6 38.Rf2 Rb6 39.Rc2 Bh4 40.g4 Bg5 41.Re2 Kf8 42.Kg2 Rb4 43.Kg3 Be7 44.Kf4 Bf6 45.h4 Kf7 46.g5 Bd8 
47.Rc2 Ba5 48.Kf3 Ke7 49.Kf4 Kf7 50.e4 Bb6 51.Rd2 Ba5 52.Rf2 Ke7 53.e5 Rb3 54.Rc2 Kd7 55.Ne4 b6 56.Nd6 
c3 57.bxc3 Rxc3 58.Rxc3 Bxc3 59.Ke4 Be1 60.d5 Bxh4 61.Nf7 b5 62.axb5 exd5+ 63.Kxd5 axb5 64.e6+ Ke7 
65.Ne5 Bxg5 66.Nxg6+ Kf6 67.Ne5 Bc1 68.Nc6 Ba3 69.Nd4 b4 70.Nb3 Ke7 71.Nd4 g6 72.Nc2 g5 73.Nd4 Ke8 
74.Nc2 g4 75.Ke4 Ke7 76.Nd4 Kf6 77.Nc2 Kxe6 78.Nxb4 Bxb4 79.Kf4 Bf8 80.Kxg4 1/2-1/2


```

## Fruit

[CCT11](CCT11 "CCT11"), Round 3, [Fruit](Fruit "Fruit") - Bright

```

[Event "[Event "CCT11"]"]
[Site "Internet Chess Club"]
[Date "2009.03.21"]
[Round "3"]
[White "Fruit"]
[Black "Bright"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8 10.d4 Nbd7 
11.Nbd2 Bb7 12.Bc2 Re8 13.a4 Bf8 14.Bd3 c6 15.Nf1 d5 16.Bg5 dxe4 17.Rxe4 Be7 18.Re2 exd4 19.Nxd4 
g6 20.axb5 cxb5 21.Qd2 Qc7 22.Rae1 Bd6 23.Ng3 Rxe2 24.Rxe2 Rc8 25.Bh6 Be5 26.Qg5 Re8 27.Ngf5 Qa5 
28.Nc2 Qb6 29.Qh4 Nc5 30.Ng7 Re7 31.Nh5 Ncd7 32.Ne3 Qc5 33.Nf4 Re8 34.Bc2 Qc6 35.f3 Bc7 36.Kf1 a5 
37.Nf5 Rxe2 38.Nxe2 Qe6 39.Ned4 Qe5 40.f4 Qe8 41.Bg5 Nd5 42.Nh6+ Kg7 43.Nhf5+ Kh8 44.Ne7 Bd6 45.Nxd5 
Bxd5 46.f5 Kg8 47.Bf4 Bc5 48.Bh6 Qe5 49.Qd8+ Nf8 50.Bd3 b4 51.Ne2 Be4 52.Bxe4 Qxe4 53.Qf6 Qb1+ 54.Nc1 
Qxf5+ 55.Qxf5 gxf5 56.Bd2 bxc3 57.Bxc3 a4 58.Ne2 Nd7 59.Ng3 f4 60.Ne4 Bf8 61.Ke2 f5 62.Nf2 Nb6 63.Nd3 
Nc4 64.Nxf4 Bg7 65.Kd3 Nxb2+ 66.Kc2 Nc4 67.Nd5 Bxc3 68.Kxc3 a3 69.Kb3 Kf7 70.Nc3 Ne3 71.g3 Ke6 72.Kxa3 
Ke5 73.Kb2 Nc4+ 74.Kc2 Kd4 75.Ne2+ Ke3 76.Nf4 Nd6 77.Nd5+ Kf3 78.Nf6 h6 79.g4 f4 80.h4 Ke2 81.g5 Nf5 
82.gxh6 Nxh6 83.Nd5 f3 84.Nc3+ Ke1 85.Ne4 f2 86.Nxf2 Kxf2 87.Kc3 Kf3 88.Kc2 Kf4 89.h5 Kg4 90.Kc3 Kg5 
91.Kc2 Kf5 92.Kc3 Kg5 1/2-1/2

```

## Release Dates

- Bright 0.1 : 2006-12-20 (private)
- Bright 0.1a : 2006-12-31 (private)
- Bright 0.1b : 2007-01-06 (private)
- Bright 0.1c : 2007-01-24 (private)
- Bright 0.1d : 2007-03-18 (private)
- Bright 0.1de : 2007-04-19 (private)
- Bright 0.1e : 2007-05-02 (private)
- Bright 0.1f : 2007-05-20 (private)
- Bright 0.2a : 2007-05-30 (private)
- Bright 0.2b : 2007-08-23 (private)
- Bright 0.2c : 2007-11-23 (public)
- Bright 0.3a : 2008-01-25 (public)
- Bright 0.3b : 2008-03-21 (private)
- Bright 0.3c : 2008-06-15 (private)
- Bright 0.3d : 2008-06-15 (private)
- Bright 0.4a : 2009-03-22 (public)
- Bright 0.5c : 2010-01-10 (public)

## See also

- [Spark](Spark "Spark")

## Forum Posts

- [bright-0.2c released](http://www.talkchess.com/forum/viewtopic.php?t=18533) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), [CCC](CCC "CCC"), December 24, 2007
- [Bright 0.3a public version released](http://www.talkchess.com/forum/viewtopic.php?t=20291) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), [CCC](CCC "CCC"), March 22, 2008
- [Bright 0.4a, Winboard and ICC...](http://www.talkchess.com/forum/viewtopic.php?t=26237) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), January 26, 2009
- [bright 0.4a now public](http://www.talkchess.com/forum/viewtopic.php?t=27138) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), [CCC](CCC "CCC"), March 23, 2009
- [Bright 0.4 A Fantastic, Agressive Games](http://www.talkchess.com/forum/viewtopic.php?t=29120) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), July 27, 2009
- [2009 WCRCC: Bright/Spark issue](http://www.talkchess.com/forum/viewtopic.php?t=29385) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), August 13, 2009
- [Djaja study, Big deal! Bright finds the line faster than ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29467)  by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), August 19, 2009 » [Djaja Study](Hans_Secelle#DjajaStudy "Hans Secelle"), Bright
- [Bright 0.5c released](http://www.talkchess.com/forum/viewtopic.php?t=31618) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink"), [CCC](CCC "CCC"), January 11, 2010

## External Links

## Chess Engine

- [brightchess - Brightchess](https://web.archive.org/web/20120113074528/http://members.ziggo.nl/allard.siemelink/bright/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Brightchess](https://sites.google.com/site/brightchess2/) (0.2c, 0.3a) by [Allard Siemelink](Allard_Siemelink "Allard Siemelink")
- [Bright](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Bright&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Bright (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bright)
- [bright - Wiktionary](https://en.wiktionary.org/wiki/bright)
- [Brightness from Wikipedia](https://en.wikipedia.org/wiki/Brightness)
- [Bright-line rule from Wikipedia](https://en.wikipedia.org/wiki/Bright-line_rule)
- [Burning Bright from Wikipedia](https://en.wikipedia.org/wiki/Burning_Bright)
- [Bright Futures Scholarship Program from Wikipedia](https://en.wikipedia.org/wiki/Bright_Futures_Scholarship_Program)
- [Brights movement from Wikipedia](https://en.wikipedia.org/wiki/Brights_movement)
- [Chris Hinze](Category:Chris_Hinze "Category:Chris Hinze"), [Claron Mcfadden](https://en.wikipedia.org/wiki/Claron_McFadden) - Chris Hinze/Bright, [Bimhuis](https://en.wikipedia.org/wiki/Bimhuis), [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), [November 08, 2009](http://www.cultuurpodiumonline.nl/category/vrije-geluiden), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Photo by [Lars Lentz](https://lars-lentz.pixels.com/), [Brightness from Wikipedia](https://en.wikipedia.org/wiki/Brightness)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Interview with Allard Siemelink](https://www.schach-welt.de/schach/computerschach/interviews/allard-siemelink-deng) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt](https://www.schach-welt.de/), January 10, 2010
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [CCT11: Bright by Allard Siemelink and Fruit by Fabien Letouzey are Co-Champions](https://cctchess.com/previous-events/cct-11/results/) (dead link)

**[Up one Level](Engines "Engines")**

