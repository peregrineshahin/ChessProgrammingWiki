---
title: Rodent
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Rodent**



[ Eastern spiny mouse - a Rodent <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Rodent**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Pawel Koziol](Pawel_Koziol "Pawel Koziol") licensed under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation"), 
initially based on [Sungorus 1.4](Sungorus "Sungorus") by [Pablo Vazquez](Pablo_Vazquez "Pablo Vazquez"), with evaluation parameters borrowed from the [Toga log user manual](Toga_Log#UserManual "Toga Log"). 
Rodent may be regarded as a beefed up [bitboard](Bitboards "Bitboards") version of the [CPW-Engine](CPW-Engine "CPW-Engine") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and features adjustable [playing strength](Playing_Strength "Playing Strength") and different personalities. 
**Rodent II**, released in February 2016 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, was a complete rewrite, now using the [magic bitboard](Magic_Bitboards "Magic Bitboards") implementation by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"). 
**Rodent III**, released in March 2017, has been programmed for [tunability](Automated_Tuning "Automated Tuning"). One can turn it into a crazy attacker or an old-fashioned positional player <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### [Board Representation](Board_Representation "Board Representation")


* [6+2 Bitboard Board Definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
* [Kogge-Stone Fill Algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards") (since Rodent II)


### [Search](Search "Search")


* [Fail Soft](Fail-Soft "Fail-Soft") [Alpha-Beta](Alpha-Beta "Alpha-Beta") with [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") (from Sungorus)
* [Fractional Extensions](Extensions#FractionalExtensions "Extensions") and [Reductions](Reductions "Reductions")
* Two-tier [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Transposition Table](Transposition_Table "Transposition Table") (from Sungorus)
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with variable [R](Depth_Reduction_R "Depth Reduction R") and [Threat Detection](Null_Move_Pruning#ThreatDetection "Null Move Pruning")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* "Sliding" [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [Eval Pruning](Quiescence_Search#StandPat "Quiescence Search") (a.k.a. static null move)
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") in [PV-Nodes](Node_Types#PV "Node Types")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE") (unofficial release of Rodent IV with [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") nets) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [Material Evaluation](Material "Material") uses some of [Larry Kaufman's](Larry_Kaufman "Larry Kaufman") formulas <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Fruit](Fruit "Fruit")-like [Weak Pawns Eval](Weak_Pawns "Weak Pawns")
* [Passed Pawns Eval](Passed_Pawn "Passed Pawn")


 taking into account [Blockade](Blockade_of_Stop "Blockade of Stop") and [Control of the Stop Square](Control_of_Stop_and_Telestop "Control of Stop and Telestop")
* [Candidate Passers Eval](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [Strong Squares](Square_Control "Square Control") (B, N, even R)
* [King Safety](King_Safety "King Safety")


 [Pawn Phalanx Bonus](King_Safety#PawnStorm "King Safety")
 [Pawn Shelter Eval](King_Safety#PawnShield "King Safety")
* [Hanging Piece Eval](Hanging_Piece "Hanging Piece")


### Misc


* Own [Opening Book](Opening_Book "Opening Book") Format
* [Position Learning](Learning "Learning")
* Weak levels


## Selected Games


Rodent II 0.8.7 x64 vs. [Gaviota 1.0 AVX x64](Gaviota "Gaviota"), March 11, 1016 by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "40/10"]
[Site "rodentII_087-x64, FCP-3"]
[Date "2016.03.11"]
[Round "13.41"]
[White "Rodent II 0.8.7 x64"]
[Black "Gaviota 1.0 AVX x64"]
[Result "1-0"]
[ECO "C78"]
[Opening "Spanish"]
[Variation "Archangelsk, 7.c3 Nxe4"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 Bb7 7.c3 Nxe4 8.d4 Na5 9.Nxe5 Nxb3 
10.Qxb3 Qf6 11.f3 Nc5 12.Ng4 Nxb3 13.Nxf6+ Ke7 14.Bg5 Nxa1  15.Re1+ Kd6 16.Bf4+ Kc6 
17.d5+ Kc5 18.b4+ Kc4 19.Na3+ Kxc3 20.Ne4+ Kxb4 21.Rb1+ Ka5 22.Bxc7+ Ka4 23.Nc3+ Kxa3 
24.Bf4 Bc5+ 25.Kh1 Be3 26.Bxe3 Bxd5 27.Bc1# 1-0

```

## OpenTal


**OpenTal** is a **Rodent III** incarnation with a fixed personality with evaluation weights provided by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), to some extend transforming [playing strength](Playing_Strength "Playing Strength") into the risky and wonderful playing style of [[Mikhail Tal](https://en.wikipedia.org/wiki/Mikhail_Tal)] <a id="cite-note-8" href="#cite-ref-8">[8]</a>. 



## See also


* [Chess System Tal](Chess_System_Tal "Chess System Tal")
* [CPW-Engine](CPW-Engine "CPW-Engine")
* [Sungorus](Sungorus "Sungorus")
* [Toga log user manual](Toga_Log#UserManual "Toga Log") » [Toga](Toga "Toga")


## Forum Posts


### 2011 ...


* [open source gift for Christmas](http://www.talkchess.com/forum/viewtopic.php?t=41590) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 25, 2011


**2012**



* [Rodent 0.11](http://www.talkchess.com/forum/viewtopic.php?t=42481) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 16, 2012
* [Rodent 0.11 for AMD compatibility](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=7&t=6477) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), February 20, 2012
* [Rodent 0.12](http://www.talkchess.com/forum/viewtopic.php?t=42687) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 29, 2012
* [Rodent 0.13](http://www.talkchess.com/forum/viewtopic.php?t=43014) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), March 25, 2012
* [Rodent 0.14](http://www.talkchess.com/forum/viewtopic.php?t=43368) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), April 19, 2012
* [Rodent 0.15 released](http://www.talkchess.com/forum/viewtopic.php?t=43851) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), May 27, 2012
* [Rodent 0.16](http://www.talkchess.com/forum/viewtopic.php?t=45487) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 08, 2012
* [Rodent 0.17 for New Year!](http://www.talkchess.com/forum/viewtopic.php?t=46686) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 31, 2012


**2013**



* [Rodent 0.18 released](http://www.talkchess.com/forum/viewtopic.php?t=47088) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 02, 2013
* [Rodent turns 1.0 !](http://www.talkchess.com/forum/viewtopic.php?t=47417) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), March 05, 2013
* [Rodent 1.1 released](http://www.talkchess.com/forum/viewtopic.php?t=49517) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), September 30, 2013
* [Rodent 1.2 released](http://www.talkchess.com/forum/viewtopic.php?t=49916) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 02, 2013
* [Rodent goes online](http://www.talkchess.com/forum/viewtopic.php?t=50239) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 26, 2013
* [new Rodent book](http://www.talkchess.com/forum/viewtopic.php?t=50697) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 31, 2013


**2014**



* [Rodent 1.3](http://www.talkchess.com/forum/viewtopic.php?t=50988) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), January 21, 2014
* [Rodent 1.4](http://www.talkchess.com/forum/viewtopic.php?t=52173) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), April 30, 2014
* [Rodent 1.5](http://www.talkchess.com/forum/viewtopic.php?t=53618) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), September 08, 2014
* [Rodent 1.6 released](http://www.talkchess.com/forum/viewtopic.php?t=54226) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 02, 2014
* [Rodent's new soul?](http://www.talkchess.com/forum/viewtopic.php?t=54366) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 17, 2014


### 2015 ...


* [Rodent 1.7 is out](http://www.talkchess.com/forum/viewtopic.php?t=55703) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), March 18, 2015
* [Mini Rodent asks for code review](http://www.talkchess.com/forum/viewtopic.php?t=57805) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 01, 2015 <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [Mini Rodent 1.0](http://www.talkchess.com/forum/viewtopic.php?t=58052) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 26, 2015


**2016**



* [Rodent II is out](http://www.talkchess.com/forum/viewtopic.php?t=59257) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 15, 2016
* [Very nice game ... Rodent - Gaviota, 1:0](http://www.talkchess.com/forum/viewtopic.php?t=59484) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 12, 2016
* [Rodent II 0.9.33](http://www.talkchess.com/forum/viewtopic.php?t=60246) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), May 23, 2016
* [Rodent II 0.9.64 released](http://www.talkchess.com/forum/viewtopic.php?t=61496) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), September 22, 2016
* [Rodent online personality creator](http://www.talkchess.com/forum/viewtopic.php?t=61837) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), October 25, 2016
* [Rodent Karpov+Topalov REALISTIC Personalities (coming soon)](http://www.talkchess.com/forum/viewtopic.php?t=61951) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), November 04, 2016


**2017**



* [Rodent needs a new developer](http://www.talkchess.com/forum/viewtopic.php?t=63182) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 15, 2017
* [Rodent III released](http://www.talkchess.com/forum/viewtopic.php?t=63414) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), March 11, 2017
* [Rodent news](http://www.talkchess.com/forum/viewtopic.php?t=64946) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), August 21, 2017
* [A group of angry Rodents](http://www.talkchess.com/forum/viewtopic.php?t=65681) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), November 10, 2017
* [OpenTal - almost new engine](http://www.talkchess.com/forum/viewtopic.php?t=66042) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 17, 2017
* [Rodent III with multi-pv (unofficial release)](http://www.talkchess.com/forum/viewtopic.php?t=66191) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 31, 2017


**2018**



* [OpenTal 1.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66248) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), January 05, 2018
* [The Most Interesting Chess Game Ever?](http://www.talkchess.com/forum/viewtopic.php?t=66300) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), January 11, 2018
* [Rodent III 0.273 - official release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68343) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), September 01, 2018


**2019**



* [Rodent needs a test](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70701) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), May 09, 2019
* [Rodent III personalities <2000 Elo?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70868) by PeterO, [CCC](CCC "CCC"), May 31, 2019
* [Rodent IV beta](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71699) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), August 31, 2019
* [The Final Rodent](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72349) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), November 17, 2019


### 2020 ...


* [Rodent FRC/960](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73724) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), April 21, 2020 » [Chess960](Chess960 "Chess960")
* [My statement from Rodent homepage](https://prodeo.actieforum.com/t118-my-statement-from-rodent-homepage) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2020 » [CCC](CCC "CCC")
* [Engine choosing between sets of piece/square tables](https://prodeo.actieforum.com/t120-engine-choosing-between-sets-of-piece-square-tables) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2020 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")


**2021**



* [a book about Rodent (in French)](https://prodeo.actieforum.com/t405-a-book-about-rodent-in-french) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2021
* [Rodent NNUE (works with the old SF networks)](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78925) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 18, 2021


## External Links


### Chess Engine


* [GitHub - nescitus/rodent-iv: trying to start a community effort based on Rodent IV](https://github.com/nescitus/rodent-iv)
* [GitHub - nescitus/Rodent III](https://github.com/nescitus/Rodent_III)
* [GitHub - nescitus/Rodent II](https://github.com/nescitus/Rodent_II)
* [rodent chess](http://sourceforge.net/projects/rodentchess/files/rodent/) at [SourceForge.net](https://en.wikipedia.org/wiki/SourceForge)
* [Rodent Chess](http://www.pkoziol.cal24.pl/rodent/rodent.htm)
* [OpenTal 1.1](http://www.pkoziol.cal24.pl/opental/)
* [Rodent](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Rodent&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")
* [Chess Engine Review: Rodent II](http://chessncognac.com/chess-engine-review-rodent-ii/) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [ChessnCognac](http://chessncognac.com/)
* [Rodent Chess Engine: The AMAZING Strangler Personality](http://chessncognac.com/rodent-chess-engine-strangler/) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [ChessnCognac](http://chessncognac.com/)


### Misc


* [Rodent from Wikipedia](https://en.wikipedia.org/wiki/Rodent)
* [Rodent - Simple English Wikipedia](https://simple.wikipedia.org/wiki/Rodent)
* [List of rodents from Wikipedia](https://en.wikipedia.org/wiki/List_of_rodents)
* [Rodentia - Wikispecies](https://species.wikimedia.org/wiki/Rodentia)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Eastern spiny mouse](https://en.wikipedia.org/wiki/Eastern_spiny_mouse) Photo by [Marcel Burkhard](http://www.tierlexikon.ch/), Acomys dimidiatus, [Gryzonie (Rodentia) - Wikipedia.pl](http://pl.wikipedia.org/wiki/Gryzonie)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [open source gift for Christmas](http://www.talkchess.com/forum/viewtopic.php?t=41590) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 25, 2011
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Rodent II is out](http://www.talkchess.com/forum/viewtopic.php?t=59257) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), February 15, 2016
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [GitHub - nescitus/Rodent III](https://github.com/nescitus/Rodent_III)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Rodent NNUE (works with the old SF networks)](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78925) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 18, 2021
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1999**). *[The Evaluation of Material Imbalances](http://www.danheisman.com/evaluation-of-material-imbalances.html)*. (first published in [Chess Life](https://en.wikipedia.org/wiki/Chess_Life) March 1999, on-line version edited by [Dan Heisman](Dan_Heisman "Dan Heisman"))
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Very nice game ... Rodent - Gaviota, 1:0](http://www.talkchess.com/forum/viewtopic.php?t=59484) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 12, 2016
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [OpenTal - almost new engine](http://www.talkchess.com/forum/viewtopic.php?t=66042) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), December 17, 2017
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [nescitus/Rodent\_II · GitHub](https://github.com/nescitus/Rodent_II)

**[Up one Level](Engines "Engines")**







 
