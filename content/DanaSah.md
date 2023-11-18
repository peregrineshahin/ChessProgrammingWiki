---
title: DanaSah
---
**[Home](Home "Home") * [Engines](Engines "Engines") * DanaSah**

**DanaSah**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), and since version **6.1** [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License 3](Free_Software_Foundation#GPL "Free Software Foundation") by [Pedro Castro](Pedro_Castro "Pedro Castro"), written in [C](C "C"), and first released in January 2005.
Also, since DanaSah **6.1** in May 2016, [Chess960](Chess960 "Chess960") is supported, available as [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Android](Android "Android") binary.
DanaSah **8.8**, released in April 2021, supports [Stockfish](Stockfish_NNUE "Stockfish NNUE") compatible [NNUE](NNUE "NNUE") networks <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Tournament Play

DanaSah played on-line the [CCT9](CCT9 "CCT9"), [CCT10](CCT10 "CCT10") and [CCT12](CCT12 "CCT12") [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), and the [WCRCC 2007](WCRCC_2007 "WCRCC 2007"), the First Annual ACCA World Computer Rapid Chess Championship. Over the board, DanaSah played the [WCCC 2009](WCCC_2009 "WCCC 2009") blitz tournament in [Pamplona](https://en.wikipedia.org/wiki/Pamplona), [Spain](https://en.wikipedia.org/wiki/Spain) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and won the [4th Chess Computer Cup](CCC_2009 "CCC 2009") in [Carugate](https://en.wikipedia.org/wiki/Carugate), [Italy](https://en.wikipedia.org/wiki/Italy) the same year, and further played the [IOCSC 2010](IOCSC_2010 "IOCSC 2010") and [IOCSC 2012](IOCSC_2012 "IOCSC 2012") [Italian Open Chess Software Cups](Italian_Computer_Chess_Championship#IOCSC "Italian Computer Chess Championship"), the latter in the original category.

## Photos & Games

[](http://www.scaccomasco.com/foto/2009/CCC4-7_nov/album/index.html)
[CCC 2009](CCC_2009 "CCC 2009"), round 1, [BremboCE](BremboCE "BremboCE") vs DanaSah operated by Sonia <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "Computer Chess Cup 4"]
[Site "Carugate"]
[Date "2009.11.07"]
[Round "1"]
[White "BremboCE 0.6.2"]
[Black "DanaSah v.4.24"]
[Result "0-1"]

1.c4 b6 2.Nc3 Bb7 3.e4 e6 4.d4 Bb4 5.Qc2 Qh4 6.Bd3 f5 7.g3 Qh5 8.Bd2 Nf6 
9.f3 Nc6 10.Nb5 fxe4 11.fxe4 O-O 12.Ne2 a6 13.Nbc3 Bd6 14.O-O Ng4 15.h4 
Nb4 16.Rxf8+ Rxf8 17.Qb3 Bxg3 18.Rf1 Rxf1+ 19.Kxf1 Nh2+ 20.Kg1 Qf3 21.Nxg3 
Qxg3+ 22.Kh1 Nf3 23.Qxb4 Qh2#  0-1

```

## Etymology

DanaSah's name is related to [Dana](https://en.wikipedia.org/wiki/Dana) of Daniela and [Sah](https://ro.wikipedia.org/wiki/%C8%98ah_%28joc%29), which means chess in [Romanian](https://en.wikipedia.org/wiki/Romanian_language) <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Features

<a id="cite-note-6" href="#cite-ref-6">[6]</a>

- [Opening book](Opening_Book "Opening Book") of [Pro Deo](ProDeo "ProDeo"). Thanks to [Ed Schröder](Ed_Schroder "Ed Schroder") and [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen")
- [Bitbases](Endgame_Bitbases "Endgame Bitbases") of [Scorpio](Scorpio "Scorpio"). Thanks to [Daniel Shawul](Daniel_Shawul "Daniel Shawul")
- [Board representation](Board_Representation "Board Representation"): [array](Array "Array") of 64, based on [FirstChess](FirstChess "FirstChess") ([Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"))
- [Aspiration search](Aspiration_Windows "Aspiration Windows"), window 15 and 150
- [PVS](Principal_Variation_Search "Principal Variation Search") and [quiescence search](Quiescence_Search "Quiescence Search"). Thanks to [Bruce Moreland](Bruce_Moreland "Bruce Moreland") for his Web page
- [Transposition tables](Transposition_Table "Transposition Table"). Thanks to [Miguel Izquierdo](index.php?title=Miguel_Izquierdo&action=edit&redlink=1 "Miguel Izquierdo (page does not exist)") ([Popochin](index.php?title=Popochin&action=edit&redlink=1 "Popochin (page does not exist)"))
- [Adaptive Null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [R](Depth_Reduction_R "Depth Reduction R") = 2-5
- ([Internal](Internal_Iterative_Deepening "Internal Iterative Deepening")) [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Search extensions](Extensions "Extensions"): [check](Check_Extensions "Check Extensions"), [pawn on seventh](Passed_Pawn_Extensions "Passed Pawn Extensions"), [recapture](Recapture_Extensions "Recapture Extensions"), transition to [pawn endgame](Pawn_Endgame "Pawn Endgame")
- [Late move reductions](Late_Move_Reductions "Late Move Reductions")
- [Razoring](Razoring "Razoring")
- [Move ordering](Move_Ordering "Move Ordering"): [hash move](Hash_Move "Hash Move"), [PV-Move](PV-Move "PV-Move"), [captures](Captures "Captures"), [promotions](Promotions "Promotions"), [killer moves](Killer_Move "Killer Move"), [history heuristic](History_Heuristic "History Heuristic")
- [Evaluation](Evaluation "Evaluation") with [lazy eval](Lazy_Evaluation "Lazy Evaluation") and [evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table"), [Material](Material "Material"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure"), [open files](Open_File "Open File"), [mobility](Mobility "Mobility"), [king safety](King_Safety "King Safety")
- [NNUE](NNUE "NNUE") (since DanaSah 8.8, April 2021)

## See also

- [Caligula](Caligula_PC "Caligula PC")

## Forum Posts

## 2005 ...

- [DanaSah 1.0 - GM Mario Gómez (1-2)](https://www.stmintz.com/ccc/index.php?id=435719) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), July 08, 2005
- [DanaSah 1.6 vs Pablo Ignacio Restrepo (Father)](https://www.stmintz.com/ccc/index.php?id=436603) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), July 13, 2005
- [danasah for linux](http://www.open-aurec.com/wbforum/viewtopic.php?p=32935) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2008 » [Linux](Linux "Linux")
- [Update DanaSah and Caligula](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=49240) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 04, 2008 » [Caligula](Caligula_PC "Caligula PC")

## 2010 ...

- [DanaSah 4.37](http://www.talkchess.com/forum/viewtopic.php?t=33335) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), March 18, 2010
- \[STS [1-10](http://www.talkchess.com/forum/viewtopic.php?t=34515) Danasah 4.45\] by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), May 26, 2010 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite")
- [DanaSah 5.00](http://www.talkchess.com/forum/viewtopic.php?t=46742) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](CCC "CCC"), January 03, 2013
- [DanaSah and DanaSah-Z](http://www.talkchess.com/forum/viewtopic.php?t=48354) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), June 20, 2013
- [Test DanaSah 5.06](http://www.talkchess.com/forum/viewtopic.php?t=48530) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), July 03, 2013

## 2015 ...

- [Chess on Android](http://www.talkchess.com/forum/viewtopic.php?t=59905) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), April 19, 2016 » [Chess for Android](Chess_for_Android "Chess for Android"), [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [DanaSah 6.1 for Windows and Android](http://www.talkchess.com/forum/viewtopic.php?t=60278) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), May 25, 2016
- [DanaSah 6.5](http://www.talkchess.com/forum/viewtopic.php?t=63185) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), February 15, 2017
- [Danasah 7.0](http://www.talkchess.com/forum/viewtopic.php?t=65406) by [Sergio Martinez](index.php?title=Sergio_Martinez&action=edit&redlink=1 "Sergio Martinez (page does not exist)"), [CCC](CCC "CCC"), October 09, 2017

## 2020 ...

- [DanaSah 8.8](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=250) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), April 20, 2021

## External Links

## Chess Engine

- [Chess Engine DanaSah](https://sites.google.com/site/danasah/english/engine)
- [DanaSah Web Gui chess engine](http://danasah.pythonanywhere.com/)
- [Danasah's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=606)
- [Descriptions - Hispanic Chess Engines](https://sites.google.com/site/hispanicchessengines/hispanic-american-engines-1/description)
- [DanaSah](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=DanaSah&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")
- [DanaSah](http://ccrl.chessdom.com/ccrl/404FRC/cgi/compare_engines.cgi?family=DanaSah&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Score+with+common+opponents&match_length=30) in [CCRL 40/2 FRC](CCRL "CCRL")

## Misc

- [Dana from Wikipedia](https://en.wikipedia.org/wiki/Dana)
- [Dana - Wiktionary](https://en.wiktionary.org/wiki/Dana)
- [sah - Wiktionary](https://en.wiktionary.org/wiki/sah)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [DanaSah 8.8](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=250) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), April 20, 2021
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [7th World Computer Chess Championship (Blitz) - Pamplona 2009 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/tournament.php?id=208)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Chess Computer Cup 4 - Photo Gallerie 1](http://www.scaccomasco.com/foto/2009/CCC4-7_nov/album/index.html)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Chess Computer Cup 4](http://www.scaccomasco.com/2009/wwwCCC4/tblscore.html)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Chess Engine DanaSah | readme](https://sites.google.com/site/danasah/english/readme)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Chess Engine DanaSah | readme](https://sites.google.com/site/danasah/english/readme)

**[Up one Level](Engines "Engines")**

