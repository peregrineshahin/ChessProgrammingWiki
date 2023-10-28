---
title: Cheese
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cheese**

\[ Coulommiers cheese <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cheese**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant free chess engine by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), written in [C](C "C"). The development started in early 2006, using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") and [alpha-beta](Alpha-Beta "Alpha-Beta") search, improving rapidly, and first released in October 2007 as version 1.0. Since 2012, one can expect yearly updates with steady improvements. Since version 1.8 in March 2016, Cheese is able to play [Chess960](Chess960 "Chess960") (FRC). It is available for all major platforms and operating systems, [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Android](Android "Android") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Selected Features](#selected-features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
  - [3.1 2006 ...](#2006-...)
  - [3.2 2010 ...](#2010-...)
  - [3.3 2015 ...](#2015-...)
  - [3.4 2020 ...](#2020-...)
- [4 External Links](#external-links)
  - [4.1 Chess engine](#chess-engine)
  - [4.2 Misc](#misc-2)
- [5 References](#references)

## Selected Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [BMI2 - PEXT Bitboards](BMI2#PEXTBitboards "BMI2") (Version 3.0)

## [Search](Search "Search")

- [Parallel Search](Parallel_Search "Parallel Search") performing [Lazy SMP](Lazy_SMP "Lazy SMP") (Version 3.0, replacing [YBW](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") of 2.0)
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") with [Negamax](Negamax "Negamax") [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table") with [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
- [Move Ordering](Move_Ordering "Move Ordering")

[Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
[Killer Heuristic](Killer_Heuristic "Killer Heuristic")
[History Heuristic](History_Heuristic "History Heuristic")
[Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") (2.2)
[Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

- [Selectivity](Selectivity "Selectivity")

## [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Version 2.0) [Late Move Reductions](Late_Move_Reductions "Late Move Reductions") [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning") [Futility Pruning](Futility_Pruning "Futility Pruning") [Razoring](Razoring "Razoring") [Quiescence Search](Quiescence_Search "Quiescence Search") [Fractional Extensions](Extensions#FractionalExtensions "Extensions") [Check Extensions](Check_Extensions "Check Extensions") [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") [Evaluation](Evaluation "Evaluation")

- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Game Phases](Game_Phases "Game Phases")
- [Material](Material "Material")
- [Mobility](Mobility "Mobility")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](Pawn_Structure "Pawn Structure") using [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")

[Backward Pawn](Backward_Pawn "Backward Pawn")
[Doubled Pawn](Doubled_Pawn "Doubled Pawn")
[Isolated Pawn](Isolated_Pawn "Isolated Pawn")
[Passed Pawn](Passed_Pawn "Passed Pawn")
[Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")

- [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")
- [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
- [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
- [King Safety](King_Safety "King Safety")
- [Knights Outposts](Outposts "Outposts")
- [Endgame Knowledge](Endgame "Endgame")

## [Insufficient Material](Material#InsufficientMaterial "Material") Misc

- [Chess960](Chess960 "Chess960")
- [Contempt Factor](Contempt_Factor "Contempt Factor") (Version 2.0)
- [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book") (Version 3.0)
- [Pondering](Pondering "Pondering")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") (Version 3.0)

## See also

- [Quark](Quark "Quark")

## Forum Posts

## 2006 ...

- [Testing and debugging chess engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5955) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2006 » [Debugging](Debugging "Debugging")
- [new engine : Cheese v1.0b](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6925) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 07, 2007
- [Cheese 1.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7038) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 02, 2008
- [Cheese 1.1b](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=7083) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 22, 2008
- [Cheese 1.2 released](http://www.talkchess.com/forum/viewtopic.php?t=21330) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), May 24, 2008
- [Cheese 1.3](http://www.talkchess.com/forum/viewtopic.php?t=24656) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), November 01, 2008

## 2010 ...

- [Cheese 1.4](http://www.talkchess.com/forum/viewtopic.php?t=42910) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), March 17, 2012
- [Cheese 1.5](http://www.talkchess.com/forum/viewtopic.php?t=48564) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), July 06, 2013
- [Cheese 1.6](http://www.talkchess.com/forum/viewtopic.php?t=52274) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), May 10, 2014

## 2015 ...

- [Chess for Android](http://www.talkchess.com/forum/viewtopic.php?t=54856) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), January 04, 2015 » [Chess for Android](Chess_for_Android "Chess for Android")
- [Cheese 1.7](http://www.talkchess.com/forum/viewtopic.php?t=55885) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), April 04, 2015
- [Cheese 1.8](http://www.talkchess.com/forum/viewtopic.php?t=59564) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), March 19, 2016
- [Cheese 1.9](http://www.talkchess.com/forum/viewtopic.php?t=63909) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), May 06, 2017
- [Cooking Cheese with Texel's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=64313) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), June 16, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Cheese 1.9.1](http://www.talkchess.com/forum/viewtopic.php?t=65188) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), September 16, 2017
- [Cheese 1.9.2](http://www.talkchess.com/forum/viewtopic.php?t=66617) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), February 17, 2018
- [Cheese 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69270) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), December 15, 2018
- [Cheese 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71230) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), July 08, 2019

## 2020 ...

- [Cheese 2.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75007) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), September 05, 2020
- [Re: YBW engines past and present?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76184&start=14) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), January 04, 2021 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
- [Cheese 3.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78918) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), December 18, 2021

## External Links

## Chess engine

- [Cheese Chess - Index](http://cheesechess.free.fr/en/index.html)

[Cheese Chess - Downloads](http://cheesechess.free.fr/en/download.html)
[Cheese Chess - Features](http://cheesechess.free.fr/en/features.html)
[Cheese Chess - History](http://cheesechess.free.fr/en/history.html)

- [Cheese](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Cheese&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")
- [Cheese](http://www.computerchess.org.uk/ccrl/404FRC/cgi/compare_engines.cgi?family=Cheese&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Score+with+common+opponents&match_length=30) in [CCRL 40/4 FRC](CCRL "CCRL")

## Misc

- [Cheese from Wikipedia](https://en.wikipedia.org/wiki/Cheese)
- [Cheese (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Cheese_(disambiguation)>)
- [cheese - Wiktionary](https://en.wiktionary.org/wiki/cheese)
- [Richard Cheese & Lounge Against the Machine](https://en.wikipedia.org/wiki/Richard_Cheese) - [Smoke Two Joints](https://en.wikipedia.org/wiki/Smoke_Two_Joints), [Grilled Cheese Invitational](https://la.eater.com/2013/4/3/6456755/april-20-marks-the-11th-annual-grilled-cheese-invitational), April 20, 2013, [Los Angeles Center Studios](https://en.wikipedia.org/wiki/Los_Angeles_Center_Studios), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A [Coulommiers cheese](https://en.wikipedia.org/wiki/Coulommiers_cheese) made from [unpasteurised](https://en.wikipedia.org/wiki/Pasteurization) [cow's](https://en.wikipedia.org/wiki/Cattle) [milk](https://en.wikipedia.org/wiki/Milk), [Image](https://commons.wikimedia.org/wiki/File:Coulommiers_lait_cru.jpg) by [Myrabella](https://commons.wikimedia.org/wiki/User:Myrabella), May 13, 2010, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Cheese Chess - Downloads](http://cheesechess.free.fr/en/download.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> based on [Cheese Chess - Features](http://cheesechess.free.fr/en/features.html)

**[Up one Level](Engines "Engines")**

