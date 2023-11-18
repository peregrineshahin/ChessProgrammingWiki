---
title: Nalwald
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nalwald**



 [](File:Nalwaldlogo.png) Nalwald logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Nalwald**,  

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Jost Triller](Jost_Triller "Jost Triller"), 
written in the [Nim programming language](Nim_(Programming_Language) "Nim (Programming Language)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, 
first released in April 2021 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Nalwald is a [bitboard](Bitboards "Bitboards") engine and generates [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") [Kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards") like,
by looking up four pre-calculated line attack arrays, 32-Kbyte each, indexed by square and [inner six bit](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") [line occupancy](Occupancy_of_any_Line "Occupancy of any Line") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Lazy SMP](Lazy_SMP "Lazy SMP") (Nalwald 15)
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") (Nalwald 14)
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Nalwald 15)
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [King](King "King") [Square](Squares "Squares") contextual [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
	+ [Rook on Open File](Rook_on_Open_File "Rook on Open File")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Trio Pawn](Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)")
	+ [Passed Pawns](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
* [Evaluation Tuning](Automated_Tuning "Automated Tuning") using [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent)


## See also


* [Googleplex Starthinker](Googleplex_Starthinker "Googleplex Starthinker")
* [Hactar](Hactar "Hactar")


## Forum Posts


* [Nalwald: Chess engine written in Nim](https://www.reddit.com/r/nim/comments/myfjx6/nalwald_chess_engine_written_in_nim/) by [Jost Triller](Jost_Triller "Jost Triller"), [Reddit](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=328) (Nalwald 1.8.1) by [Tony Mokonen](index.php?title=Tony_Mokonen&action=edit&redlink=1 "Tony Mokonen (page does not exist)"), [CCC](CCC "CCC"), May 08, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=419) (Nalwald 1.9) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), June 16, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=468) (Nalwald 1.10) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), July 03, 2021
* [Nalwald](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78198) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), September 17, 2021
* [Re:Nalwald](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78198&start=3) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), February 08, 2022


## External Links


### Chess Engine


* [Tsoj Tsoj / Nalwald · GitLab](https://gitlab.com/tsoj/Nalwald)
* [Nalwald](https://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Nalwald&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Nalwald | PaxCalradica Wiki | Fandom](https://paxcalradica.fandom.com/wiki/Nalwald)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Nalwald logo based on [logo.png · master · Tsoj Tsoj / Nalwald · GitLab](https://gitlab.com/tsoj/Nalwald/-/blob/master/logo.png)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Nim programming language from Wikipedia](https://en.wikipedia.org/wiki/Nim_(programming_language))
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Nalwald: Chess engine written in Nim](https://www.reddit.com/r/nim/comments/myfjx6/nalwald_chess_engine_written_in_nim/) by [Jost Triller](Jost_Triller "Jost Triller"), [Reddit](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2021
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [bitboard.nim · master · Tsoj Tsoj / Nalwald · GitLab](https://gitlab.com/tsoj/Nalwald/-/blob/master/bitboard.nim)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [README.md · master · Tsoj Tsoj / Nalwald · GitLab](https://gitlab.com/tsoj/Nalwald/-/blob/master/README.md)

**[Up one Level](Engines "Engines")**







 
