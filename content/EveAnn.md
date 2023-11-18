---
title: EveAnn
---
**[Home](Home "Home") * [Engines](Engines "Engines") * EveAnn**

**EveAnn**,

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Andres Valverde](Andres_Valverde "Andres Valverde"), written in [Delphi](Delphi "Delphi"), first released in December 2005. EveAnn started its life when Andres translated [Pham Hong Nguyen's](Pham_Hong_Nguyen "Pham Hong Nguyen") [FirstChess](FirstChess "FirstChess") from [C](C "C") to [Pascal](Pascal "Pascal"), and made it play legal chess. He further improved the program after studying [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") site on chess programming topics, got several ideas from [Tom Kerrigan's](Tom_Kerrigan "Tom Kerrigan") [TSCP](TSCP "TSCP") and [Ed Schröder's](Ed_Schroder "Ed Schroder") *How Rebel plays chess*.
The engine is dedicated to Andres' daughters Eve and Ann <a id="cite-note-1" href="#cite-ref-1">[1]</a>. EveAnn played the [CCT8](CCT8 "CCT8") in 2006, the [CCT9](CCT9 "CCT9") and under the handle *DelTomateX*, the [WCRCC 2007](WCRCC_2007 "WCRCC 2007"), the First Annual ACCA World Computer Rapid Chess Championship.

## Program Techniques

<a id="cite-note-2" href="#cite-ref-2">[2]</a>

- [Alpha-Beta](Alpha-Beta "Alpha-Beta") search with [iterative deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration window](Aspiration_Windows "Aspiration Windows") in three phases (50, 200, infinite)
- [Quiescence search](Quiescence_Search "Quiescence Search") with [check](Check "Check") evasions
- [Adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") (Fixed to [R](Depth_Reduction_R "Depth Reduction R")=3 since 1.66)
- [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [move ordering](Move_Ordering "Move Ordering") and QS [pruning](Pruning "Pruning")
- [Transposition table](Transposition_Table "Transposition Table") in a single way (Improved in 1.67)
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [History heuristic](History_Heuristic "History Heuristic") for move ordering and pruning
- [Killer heuristic](Killer_Heuristic "Killer Heuristic")
- [LMR and LMP](Late_Move_Reductions "Late Move Reductions")
- [Checks](Check_Extensions "Check Extensions"), [pawns to 7th](Passed_Pawn_Extensions "Passed Pawn Extensions") and [singular extensions](Singular_Extensions "Singular Extensions")
- [Evaluation](Evaluation "Evaluation") includes [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility"), a few [endgame](Endgame "Endgame") patterns, [king safety](King_Safety "King Safety"), [center control](Center_Control "Center Control"), etc.
- [Rebel](Rebel "Rebel") [Book](Opening_Book "Opening Book") (Thanks to [Ed](Ed_Schroder "Ed Schroder") and [Jeroen](Jeroen_Noomen "Jeroen Noomen"))
- [Scorpio bitbases](Scorpio_Bitbases "Scorpio Bitbases") supported. Thanks to [Daniel Shawul](Daniel_Shawul "Daniel Shawul") for his permission.

## Selected Games

[WCRCC 2007](WCRCC_2007 "WCRCC 2007"), round 8, EveAnn (DelTomateX) - [Horizon](Horizon "Horizon") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "WCRCC 2007"]
[Site "Internet Chess Club"]
[Date "2007.07.21"]
[Round "8"]
[White "EveAnn"]
[Black "Horizon"]
[Result "1-0"]

1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 e6 5.Nc3 Qc7 6.Be3 a6 7.Bd3 Nf6
8.O-O Ne5 9.h3 Bc5 10.Kh1 d6 11.f4 Ng6 12.Qe1 O-O 13.f5 Ne5 14.Qh4
Bd7 15.Rf3 Nxf3 16.gxf3 Qb6 17.Rg1 Bxd4 18.e5 g6 19.Bxd4 Qc6 20.fxg6
Qxf3+ 21.Kh2 fxg6 22.Bxg6 1-0

```

## See also

- [Dirty](Dirty "Dirty")
- [FirstChess](FirstChess "FirstChess")
- [TSCP](TSCP "TSCP")

## Forum Posts

## 2005 ...

- [EveAnn engine released](https://www.stmintz.com/ccc/index.php?id=471551) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), December 18, 2005
- [EveAnn 1.62 like UCI engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6324&p=30024) by Silvian Rucsandescu, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2007
- [EveAnn 1.63 and Dirty 20/07/2007 released](http://www.talkchess.com/forum/viewtopic.php?t=15482) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), July 31, 2007

## 2010 ...

- [Simple question about SEE](http://www.talkchess.com/forum/viewtopic.php?t=37582) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), January 12, 2011 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [EveAnn 1.64 released](http://www.talkchess.com/forum/viewtopic.php?t=37969) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), February 06, 2011
- [EveAnn 1.66 released](http://www.talkchess.com/forum/viewtopic.php?t=38899) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), April 27, 2011
- [EveAnn 1.67 released](http://www.talkchess.com/forum/viewtopic.php?t=42123) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), January 23, 2012
- [EveAnn 1.71 released](http://www.talkchess.com/forum/viewtopic.php?t=47093) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), February 02, 2013
- [EveAnn 1.71a](http://www.talkchess.com/forum/viewtopic.php?t=47135) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), February 05, 2013
- [EveAnn 1.72 released](http://www.talkchess.com/forum/viewtopic.php?t=50701) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), December 31, 2013

## 2015 ...

- [EveAnn 1.72 released](http://www.talkchess.com/forum/viewtopic.php?t=63616) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), April 01, 2017

## External Links

## Chess Engine

- [Dirty Chess Engine - EveAnn Chess Engine](http://dirtychess.com/links.php)
- [Norbert's collection/EveAnn (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/EveAnn%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [EveAnn](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=EveAnn&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Eve - Wiktionary](https://en.wiktionary.org/wiki/Eve)
- [Eve (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Eve_(disambiguation)>)
- [Eve (name) from Wikipedia](<https://en.wikipedia.org/wiki/Eve_(name)>)
- [Ann - Wiktionary](https://en.wiktionary.org/wiki/Ann)
- [Ann from Wikipedia](https://en.wikipedia.org/wiki/Ann)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [readme.txt](http://webs.ono.com/a.valverde/readme.txt)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> based on eveann172.zip\\readme.txt
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [2007 World Computer Rapid Chess Championships | Results | PGN Download](http://compchess.org/2007PresResults.html)

**[Up one level](Engines "Engines")**

