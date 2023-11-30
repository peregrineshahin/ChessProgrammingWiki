---
title: CounterCounterGo
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Counter**

\[ Mechanical Counters <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Counter**, (Счетчик)

an [UCI](UCI "UCI") compliant chess engine by [Vadim Chizhov](index.php?title=Vadim_Chizhov&action=edit&redlink=1 "Vadim Chizhov (page does not exist)"), initially written in [C#](C_sharp "C sharp") to run under [Windows](Windows "Windows") [.Net](https://en.wikipedia.org/wiki/.NET_Framework), available since early 2007 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Counter 0.8 played a strong [CCCCISC 2008](CCCCISC_2008 "CCCCISC 2008") over the board. Counter was then ported to the [Go programming language](</Go_(Programming_Language)> "Go (Programming Language)") and released in May 2017 as [open source](Category:Open_Source "Category:Open Source") at [GitHub](https://en.wikipedia.org/wiki/GitHub), dubbed [CounterGo](#countergo) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Counter C\#

According to the *sdchess description*, Counter is based on [bitboards](Bitboards "Bitboards") using [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") [magic bitboard](Magic_Bitboards "Magic Bitboards") implementation to [generate moves](Move_Generation "Move Generation") <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
while the Counter 1.2 readme claims a hybrid [board representation](Board_Representation "Board Representation") consisting of a [10x12 board](10x12_Board "10x12 Board") and bitboards for pawns <a id="cite-note-5" href="#cite-ref-5">[5]</a>.
Counter applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [delta pruning](Delta_Pruning "Delta Pruning"), [futility pruning](Futility_Pruning "Futility Pruning") and [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning"),
[SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [LMR](Late_Move_Reductions "Late Move Reductions"), [check extensions](Check_Extensions "Check Extensions"), [mate threat extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [passed pawn extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") and [capture extensions](Capture_Extensions "Capture Extensions"), and [IID](Internal_Iterative_Deepening "Internal Iterative Deepening").
The [evaluation](Evaluation "Evaluation") has improved over the time, specially the assessment of a [safe king](King_Safety "King Safety") and [passed pawns](Passed_Pawn "Passed Pawn"), since version 0.8, [lazy evaluation](Lazy_Evaluation "Lazy Evaluation") was removed.

## CounterGo

CounterGo comes as didactic [open source engine](Category:Open_Source "Category:Open Source") written in the [Go programming language](</Go_(Programming_Language)> "Go (Programming Language)")
along with an intuitive source structure, licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Dense Bitboard Board Definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP") <a id="cite-note-7" href="#cite-ref-7">[7]</a> using Goroutines <a id="cite-note-8" href="#cite-ref-8">[8]</a>
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") > 0
  - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") > 0
  - [Recapture Extensions](Recapture_Extensions "Recapture Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") > 0
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [King Safety](King_Safety "King Safety")
  - [Attacking King Zone](King_Safety#Attacking "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
- [Tempo](Tempo "Tempo")

## Selected Games

[CCCCISC 2008](CCCCISC_2008 "CCCCISC 2008"), round 5, Counter - [SmarThink](SmarThink "SmarThink") <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```
[Event "CIS 2008"]
[Site "Moscow SDCHESS RGSU"]
[Date "2008.03.02"]
[Round "5"]
[White "Counter 0.8"]
[Black "SmarThink 1.1 r1119"]
[Result "1/2-1/2"]

1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Nc3 c5 5.cxd5 exd5 6.Bg5 Nc6 7.e3 c4 8.Bxf6 gxf6 
9.Rc1 Be6 10.Be2 Qa5 11.O-O O-O-O 12.Re1 Kb8 13.Qc2 f5 14.Qd2 Rg8 15.Bd1 Rc8 
16.Ba4 Nb4 17.Bc2 Bd6 18.g3 Nxc2 19.Rxc2 f6 20.Nh4 Rcd8 21.Ng2 Bb4 22.Nf4 Bf7 
23.a3 Be7 24.f3 h5 25.Kf2 h4 26.Rg1 hxg3+ 27.hxg3 Rg5 28.Rh1 Rg7 29.Rh3 Qc7 
30.Rc1 Rg5 31.Nb5 Qd7 32.Qa5 a6 33.Nc3 Bg8 34.Rh8 Rc8 35.Rch1 Bd8 36.Qa4 Qd6 
37.R1h5 Bc7 38.Qc2 Qc6 39.R5h6 Qd6 40.Nh5 Rxh5 41.Rxh5 Qxg3+ 42.Kf1 f4 43.Rh3 
Qg7 44.exf4 b5 45.f5 Qg5 46.R3h4 Bf7 47.R8h7 Bg8 48.Rg4 Qe3 49.Rh3 Re8 50.Rg7 
a5 51.Qf2 Qd3+ 52.Kg2 b4 53.axb4 axb4 54.Rh8 bxc3 55.Rgxg8 Rxg8+ 56.Rxg8+ Kb7 
57.bxc3 Qxc3 58.Rg6 Qc1 59.Qe2 Qf4 60.Rg4 Qxf5 61.Qb2+ Kc6 62.Qa2 Kb5 63.Qb2+ 
Kc6 64.Qa2 Kb5 65.Qb2+ Kc6 1/2-1/2

```

## Forum Posts

## 2007 ...

- [Counter 0.2 : 2098](http://www.talkchess.com/forum/viewtopic.php?t=13788) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), May 15, 2007
- [Counter 0.3 : 2201](http://www.talkchess.com/forum/viewtopic.php?t=14991) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), July 10, 2007
- [Counter 0.4 : 2182](http://www.talkchess.com/forum/viewtopic.php?t=15966) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), August 22, 2007
- [Counter 0.5 : 2280](http://www.talkchess.com/forum/viewtopic.php?t=16367) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), September 09, 2007
- [Counter 0.6 : 2292](http://www.talkchess.com/forum/viewtopic.php?t=16573) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), September 20, 2007
- [Counter 0.7 : 2344](http://www.talkchess.com/forum/viewtopic.php?t=17916) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), November 17, 2007
- [Counter 0.8 : 2291](http://www.talkchess.com/forum/viewtopic.php?t=18741) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), January 04, 2008
- [Counter 1.0 : 2383](http://www.talkchess.com/forum/viewtopic.php?t=23071) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), August 17, 2008
- [Counter 1.1 : 2327](http://www.talkchess.com/forum/viewtopic.php?t=26110) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), January 19, 2009

## 2010 ...

- [Counter 1.2 Updated](http://www.talkchess.com/forum/viewtopic.php?t=32564) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), February 12, 2010
- [Counter 1.2 : 2336](http://www.talkchess.com/forum/viewtopic.php?t=32613) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), February 14, 2010
- [Counter 1.2 - CCRL 40/4 Results](http://www.talkchess.com/forum/viewtopic.php?t=35733) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), August 08, 2010
- [New version of Counter (in Go language)](http://www.talkchess.com/forum/viewtopic.php?t=64099) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 27, 2017
- [Counter 2.1.0 released](http://www.talkchess.com/forum/viewtopic.php?t=65717) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), November 13, 2017
- [Counter 3.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69221) by Damir, [CCC](CCC "CCC"), December 10, 2018
- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=374) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), October 19, 2019

## External Links

## Chess Engine

- [GitHub - ChizhovVadim/CounterGo: Chess engine (golang)](https://github.com/ChizhovVadim/CounterGo)
- [Counter by Вадим Чижов (Vadim Chizhov), Russia!](http://www.sdchess.ru/Counter.htm) from [sdchess.ru](http://www.sdchess.ru/)
- [Counter](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Counter&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [counter - Wiktionary](https://en.wiktionary.org/wiki/counter)
- [Counter from Wikipedia](https://en.wikipedia.org/wiki/Counter)
- [Counter (digital) from Wikipedia](<https://en.wikipedia.org/wiki/Counter_(digital)>)
- [Counterattack from Wikipedia](https://en.wikipedia.org/wiki/Counterattack)
- [Attack & Counterattack in Chess](https://www.chessgames.com/perl/chesscollection?cid=1018347) compiled by [SamAtoms1980](http://www.chessgames.com/perl/chessuser?username=SamAtoms1980), [chessgames.com](http://www.chessgames.com/index.html)
- [countermove - Wiktionary](https://en.wiktionary.org/wiki/countermove) » [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
- [Counterpoint from Wikipedia](https://en.wikipedia.org/wiki/Counterpoint)
- [Steve Reich](https://en.wikipedia.org/wiki/Steve_Reich) - [Electric Counterpoint](https://en.wikipedia.org/wiki/Electric_Counterpoint), with [Pat Metheny](Category:Pat_Metheny "Category:Pat Metheny"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Three mechanical counters by [Arnold Reinhold](https://commons.wikimedia.org/wiki/User:ArnoldReinhold), April 20, 2009, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Counter (digital) from Wikipedia](<https://en.wikipedia.org/wiki/Counter_(digital)>)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Counter 1.2 Updated](http://www.talkchess.com/forum/viewtopic.php?t=32564) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), February 12, 2010
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [New version of Counter (in Go language)](http://www.talkchess.com/forum/viewtopic.php?t=64099) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 27, 2017
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Counter by Вадим Чижов (Vadim Chizhov), Russia!](http://www.sdchess.ru/Counter.htm) from [sdchess.ru](http://www.sdchess.ru/)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> Counter_12 - readme.txt
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CounterGo/types.go at master · ChizhovVadim/CounterGo · GitHub](https://github.com/ChizhovVadim/CounterGo/blob/master/common/types.go)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [CounterGo/search.go at master · ChizhovVadim/CounterGo · GitHub](https://github.com/ChizhovVadim/CounterGo/blob/master/engine/search.go)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Effective Go - The Go Programming Language - Concurrency](https://golang.org/doc/effective_go.html#concurrency)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [The The First championship of the CIS (Первый официальный чемпионат СНГ)](http://www.sdchess.ru/Tournaments/Cis_official_1.htm) from [sdchess.ru](http://www.sdchess.ru/)

**[Up one Level](Engines "Engines")**

