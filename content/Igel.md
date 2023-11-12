---
title: Igel
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Igel**



[.jpg) European hedgehog - an Igel <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Igel**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna") licensed under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation"), 
initially based on [GreKo 2018.01](GreKo "GreKo") and following independent development since 2018. In August 2020, Igel switched to [NNUE](NNUE "NNUE") as a main evaluation function using [Dietrich Kappe's](Dietrich_Kappe "Dietrich Kappe") *Night Nurse* net <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> as default <a id="cite-note-4" href="#cite-ref-4">[4]</a> participating in [TCEC Season 19, League 2](TCEC_Season_19#Second "TCEC Season 19"), and promoting to [League 1](TCEC_Season_19#First "TCEC Season 19"). In October 2020 Igel switched to own network trained on Igel 2.6.0 (Hand Crafted Evaluation) participating in TCEC Cup7 and in [TCEC Season 20](TCEC_Season_20#First "TCEC Season 20").



### [Board Representation](Board_Representation "Board Representation")


* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Fail Soft](Fail-Soft "Fail-Soft") [Alpha-Beta](Alpha-Beta "Alpha-Beta") with [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Extensions](Extensions "Extensions") and [Reductions](Reductions "Reductions")
* Variable [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with variable [R](Depth_Reduction_R "Depth Reduction R")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [Eval Pruning](Quiescence_Search#StandPat "Quiescence Search") (a.k.a. static null move)
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") in [PV-Nodes](Node_Types#PV "Node Types")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE") (as of Igel 2.7.0)
* [Material Evaluation](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Passed Pawns Eval](Passed_Pawn "Passed Pawn")
* [Strong Squares](Square_Control "Square Control") (B, N)
* [King Safety](King_Safety "King Safety")


### Misc


* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")


## Selected Games


Igel 2.6-dev-3 x64 vs. [Booot 6.4 x64](Booot "Booot"), July 2020 by [TCEC](TCEC "TCEC")




```C++

[Site "https://tcec-chess.com"]
[Date "2020.07.17"]
[Round "1.4"]
[White "Booot 6.4"]
[Black "Igel 2.6-dev-3"]
[Result "0-1"]
[BlackElo "3280"]
[ECO "C01"]
[GameDuration "01:08:12"]
[GameEndTime "2020-07-17T20:16:56.946 UTC"]
[GameStartTime "2020-07-17T19:08:44.259 UTC"]
[Opening "French"]
[PlyCount "118"]
[Termination "adjudication"]
[TerminationDetails "SyzygyTB"]
[TimeControl "1800+5"]
[Variation "exchange variation"]
[WhiteElo "3424"]

1. e4 e6 2. d4 d5 3. exd5 { C01 French Defense: Exchange Variation } exd5 4. Bd3 Nf6 5. Nf3 Bd6 6. O-O O-O 7. Re1 Bg4 8. h3 Bh5 9. Be3 c6 10. Nbd2 Re8 11. c3 Nbd7 12. Qc2 Bg6 13. Bxg6 hxg6 14. c4 Nf8 15. c5 Bc7 16. Rac1 Qd7 17. Qb3 Re7 18. Re2 Rae8 19. Rce1 Qf5 20. Nh4 Qh5 21. Nhf3 N8h7 22. Nf1 Ne4 23. Bc1 g5 24. Qa3 f5 25. Ne5 Bxe5 26. dxe5 g4 27. Ng3 Nxg3 28. Qxg3 Nf8 29. hxg4 fxg4 30. Qh2 Qg6 31. Qg3 Ne6 32. Be3 Qh5 33. f3 gxf3 34. gxf3 Rf7 35. f4 Qf5 36. Rg2 Nxf4 37. Bxf4 Qxf4 38. e6 Qd4+ 39. Qe3 Qxe3+ 40. Rxe3 Rf4 41. Rd2 Re7 42. b3 Rf6 43. Rde2 g6 44. Re1 Rf5 45. Kg2 Kg7 46. R3e2 a5 47. Kg3 Kf6 48. Re3 d4 49. Re4 Rg5+ 50. Kf3 Rxc5 51. Rxd4 Rxe6 52. Red1 Ree5 53. Rd7 Rc3+ 54. Kf2 Rc2+ 55. R1d2 Rxd2+ 56. Rxd2 a4 57. bxa4 Re4 58. Rb2 Rxa4 59. Rxb7 Rxa2+ { Black wins. } 0-1

```

## Forum Posts


### 2018


* [Introducing Igel chess engine](http://www.talkchess.com/forum3/viewtopic.php?t=67890) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), July 03, 2018


### 2020


* [Re: Introducing Igel chess engine - Igel 2.5.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=15) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), June 15, 2020


 [Re: Introducing Igel chess engine - Igel 2.6.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=16) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), August 01, 2020
 [Re: Introducing Igel chess engine - Igel and NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=17) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), August 19, 2020
 [Igel Generation Networks (IGN)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=83) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), October 30, 2020
 [Re: Introducing Igel chess engine - Igel 2.9.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=91) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), December 25, 2020 
* [Night Nurse 0.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), August 19, 2020


### 2021


* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=195) (Igel 3.0.0) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), April 04, 2021
* [Igel 3.0.5](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=292) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), April 27, 2021
* [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")


 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=57) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021
## External Links


### Chess Engine


* [Igel Home Page](https://github.com/vshcherbyna/igel)
* [CCRL 40/40 Igel](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Igel&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)
* [CCRL 40/4 Igel](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Igel&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)


### Misc


* [Igel from Wikipedia.de](https://de.wikipedia.org/wiki/Igel)
* [Erinaceidae from Wikipedia](https://en.wikipedia.org/wiki/Erinaceidae)
* [Hedgehog from Wikipedia](https://en.wikipedia.org/wiki/Hedgehog)
* [Hedgehog (chess) from Wikipedia](https://en.wikipedia.org/wiki/Hedgehog_(chess))


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [European hedgehog](https://en.wikipedia.org/wiki/European_hedgehog)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Night Nurse is Bad Gyal in disguise](http://talkchess.com/forum3/viewtopic.php?t=74619) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), July 30, 2020
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Night Nurse 0.2](http://talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), August 19, 2020
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Introducing Igel chess engine - Igel and NNUE](http://talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=17) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), August 19, 2020

**[Up one Level](Engines "Engines")**







 
