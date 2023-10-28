---
title: Invictus
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Invictus**



[ Sol Invictus <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Invictus**, (InvictusChess, Invictus Chess)  

an [UCI](UCI "UCI") compliant [open source](Category:Open_Source "Category:Open Source") chess engine by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), written in [C++](Cpp "Cpp") and licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), first released in September 2018 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Invictus is influenced by other open source engines in particular [Stockfish](Stockfish "Stockfish"), [Ethereal](Ethereal "Ethereal"), [Defenchess](Defenchess "Defenchess"), and [Minic](Minic "Minic") concerning [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") [[3]](#cite-note-readme-3).
[Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan") of [TSCP](TSCP "TSCP") fame is given credit for sharing the [Simplified ABDADA](ABDADA "ABDADA") idea <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 
Invictus r324 had its tournament debut at [TCEC Season 21](TCEC_Season_21 "TCEC Season 21") in May 2021 and gained a respectable 50% score in its strong [Qualification League](TCEC_Season_21#Qual "TCEC Season 21"). 



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc-2)
* [5 References](#references)






[[3]](#cite-note-readme-3)



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


 [PEXT Bitboards](BMI2#PEXTBitboards "BMI2") 
### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Parallel Search](Parallel_Search "Parallel Search") using [Threads](Thread "Thread")
	+ [Simplified ABDADA](ABDADA "ABDADA")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [NUMA Support](NUMA "NUMA")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
	+ [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Mobility](Mobility "Mobility")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Open Pawns](Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Connected Pawns](Connected_Pawns "Connected Pawns")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [King Tropism](King_Safety#KingTropism "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
* [Tempo](Tempo "Tempo")


### Misc


* [Texel's Tuning](Texel%27s_Tuning_Method "Texel's Tuning Method") with [Stochastic Gradient Descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) using [Adam](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam)
* [Texel's Tuning](Texel%27s_Tuning_Method "Texel's Tuning Method") with [Local Search](https://en.wikipedia.org/wiki/Local_search_(optimization))


## See also


* [Twisted Logic](Twisted_Logic "Twisted Logic")
* [Hannibal](Hannibal "Hannibal")


## Forum Posts


* [Invictus chess engine r228](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68538) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), September 29, 2018
* [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=409) (Invictus r305) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), December 05, 2019
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=344) (Invictus r340) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), May 19, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=406) (Invictus r382) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), June 07, 2021


## External Links


### Chess Engine


* [GitHub - ed-apostol/InvictusChess: A state of the art chess playing engine](https://github.com/ed-apostol/InvictusChess)
* [Invictus](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Invictus&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [invictus - Wiktionary](https://en.wiktionary.org/wiki/invictus)
* [Invictus (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Invictus_(disambiguation))
* [Invictus from Wikipedia](https://en.wikipedia.org/wiki/Invictus)
* [Oxford Book of English Verse 1250-1900/Invictus - Wikisource](https://en.wikisource.org/wiki/Oxford_Book_of_English_Verse_1250-1900/Invictus)
* [Virgin Steele](https://en.wikipedia.org/wiki/Virgin_Steele) - [Invictus](https://en.wikipedia.org/wiki/Invictus_(Virgin_Steele_album)) (1998), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Sol Invictus](https://commons.wikimedia.org/wiki/File:Beit_alfa01.jpg), a [Byzantine](https://en.wikipedia.org/wiki/Byzantine_art) mosaic of a [Zodiac Wheel](https://en.wikipedia.org/wiki/Astrological_sign) — from the 6th century ancient [Beth Alpha](https://en.wikipedia.org/wiki/Beth_Alpha) synagogue. [Sol Invictus from Wikipedia](https://en.wikipedia.org/wiki/Sol_Invictus), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Invictus chess engine r228](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68538) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), September 29, 2018
3. ↑ [3.0](#cite-ref-readme-3-0) [3.1](#cite-ref-readme-3-1) [InvictusChess/README.md at master · ed-apostol/InvictusChess · GitHub](https://github.com/ed-apostol/InvictusChess/blob/master/README.md)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Simplified ABDADA](http://www.tckerrigan.com/Chess/Parallel_Search/Simplified_ABDADA/) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan")

**[Up one Level](Engines "Engines")**







 
