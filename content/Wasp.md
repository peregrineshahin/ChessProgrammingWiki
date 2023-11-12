---
title: Wasp
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Wasp**



[ Wasp <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Wasp**,  

[John Stanback's](John_Stanback "John Stanback") new [UCI](UCI "UCI") compliant chess engine and complete rewrite of [Zarkov](Zarkov "Zarkov"), first released short after [June solstice](https://en.wikipedia.org/wiki/June_solstice) 2016, announced <a id="cite-note-2" href="#cite-ref-2">[2]</a> and hosted by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. As a [bitboard](Bitboards "Bitboards") engine, Wasp is compiled for modern [64 bit CPU's](X86-64 "X86-64") with [popcnt](Population_Count "Population Count") and [bitscan](BitScan "BitScan") instructions. Wasp **2.00**, released in April 2017, is able to use multiple [threads](Thread "Thread") performing a [Lazy SMP](Lazy_SMP "Lazy SMP") search <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 
In 2020, John Stanback played with tiny [neural networks](Neural_Networks "Neural Networks") to learn how to [backpropagate](Neural_Networks#Backpropagation "Neural Networks") errors using Wasp's [evaluation](Evaluation "Evaluation") as the target, and then rewrote Wasp's evaluation function with fast [tuning](Automated_Tuning "Automated Tuning") in mind, quite similar to the tiny NN approach <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Along with Wasp **5.00**, released in November 2021, the evaluation function emerged to an [NNUE](NNUE "NNUE") with 1830 inputs, 192 neurons in the first hidden layer, 16 neurons in the second hidden layer, and two neurons in the third hidden layer. It was trained using positions from games between Wasp and other engines of roughly similar strength <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Extensions](Extensions "Extensions")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions") (to 7th rank if [depth](Depth "Depth") is low)
	+ [Fractional](Extensions#FractionalExtensions "Extensions")
		- [Capture Extensions](Capture_Extensions "Capture Extensions")
		- [PV Extensions](PV_Extensions "PV Extensions")
* [Pruning](Pruning "Pruning")/[Reductions](Reductions "Reductions")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Lazy SMP](Lazy_SMP "Lazy SMP") (Wasp 2.00)


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE") (Wasp **5.00**)
* Wasp does not use [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation") (Opposed to [Zarkov](Zarkov "Zarkov"))
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
	+ [Weak Pawns](Weak_Pawns "Weak Pawns")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
* [Mobility](Mobility "Mobility")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
* [Outposts](Outposts "Outposts")
* [Rook on open/half-open file](Rook_on_Open_File "Rook on Open File")
* [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
* [King Safety](King_Safety "King Safety")
* [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism") in [Endgame](Endgame "Endgame")


### Misc


* [KPK base](KPK "KPK")
* [UCI](UCI "UCI")
* [Chess960](Chess960 "Chess960") (Wasp 5.20)


## See also


* [Arthropod](Category:Arthropod "Category:Arthropod")
* [Buzz](Buzz "Buzz")
* [GNU Chess](GNU_Chess "GNU Chess")
* [SCP](SCP "SCP")
* [Zarkov](Zarkov "Zarkov")


## Forum Posts


### 2016 ...


* [Wasp 1.01 x64 by John Stanback released ...](http://www.talkchess.com/forum/viewtopic.php?t=60550) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 22, 2016
* [Wasp 1.02 by John Stanback available ...](http://www.talkchess.com/forum/viewtopic.php?t=60667) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), July 01, 2016
* [Wasp until move 42...](http://www.talkchess.com/forum/viewtopic.php?t=60694) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), July 05, 2016
* [Wasp by John Stanback is clear for take-off on runway 1.25!](http://www.talkchess.com/forum/viewtopic.php?t=61560) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), September 30, 2016


**2017**



* [Wasp 2.00 by John Stanback ... with Lazy SMP!](http://www.talkchess.com/forum/viewtopic.php?t=63783) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), April 21, 2017
* [Wasp 2.01 by John Stanback available ...](http://www.talkchess.com/forum/viewtopic.php?t=63894) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 04, 2017
* [Re: Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=63903&start=13) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), May 06, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Wasp 2.60 by John Stanback released!](http://www.talkchess.com/forum/viewtopic.php?t=65791) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), November 22, 2017
* [Wasp and a question](http://www.talkchess.com/forum/viewtopic.php?t=65805) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), November 23, 2017


**2018**



* [Wasp 3.00 available ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67410) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 11, 2018
* [Re: Lazy SMP and 44 cores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68154&start=7) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), August 08, 2018 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Wasp 3.50 by John Stanback available!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69256) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), December 14, 2018


**2019**



* [Wasp 3.60 available (for DGT Pi too, for chess computer lovers)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70444) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), April 07, 2019 » [DGT Pi](DGT_Pi "DGT Pi")
* [Wasp 3.75 by John Stanback released ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71744) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), September 06, 2019


### 2020 ...


* [Wasp 4.00 by John Stanback available!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74174) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 14, 2020
* [Wasp NN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75794) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), November 14, 2020


 [Re: Wasp NN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75794&start=4) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), November 14, 2020
* [Wasp 4.08 dev](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75896) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), November 22, 2020


**2021**



* [Wasp 4.5 Released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76205) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), January 01, 2021


 [Re: Wasp 4.5 Released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76205&start=14) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), January 03, 2021 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Wasp 5.00 released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78687) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), November 18, 2021


**2022**



* [Wasp 5.20 Released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79034) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), January 02, 2022
* [Wasp 5.50 Released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79675) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), April 12, 2022


## External Links


### Chess Engine


* [Frank's Chess Page, Wasp by John Stanback](http://www.amateurschach.de/main/_wasp.htm)
* [Wasp](https://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Wasp&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [WASP - Wiktionary](https://en.wiktionary.org/wiki/WASP)
* [wasp - Wiktionary](https://en.wiktionary.org/wiki/wasp)
* [Wasp from Wikipedia](https://en.wikipedia.org/wiki/Wasp)
* [Wasp (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Wasp_(disambiguation))
* [W.A.S.P.](https://en.wikipedia.org/wiki/W.A.S.P.) - [Mantronic](http://www.azlyrics.com/lyrics/wasp/mantronic.html), [Inside the Electric Circus](https://en.wikipedia.org/wiki/Inside_the_Electric_Circus) (1986), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Vespula](https://en.wikipedia.org/wiki/Vespula) is a small genus of social wasps, widely distributed in the [Northern Hemisphere](https://en.wikipedia.org/wiki/Northern_Hemisphere). Along with members of their sister genus [Dolichovespula](https://en.wikipedia.org/wiki/Dolichovespula), they are collectively known by the common name [yellow jackets](https://en.wikipedia.org/wiki/Yellow_jacket) (or yellow-jackets) in [North America](https://en.wikipedia.org/wiki/North_America). Vespula species have a shorter malar space and a more pronounced tendency to nest underground, but are otherwise nearly indistinguishable from Dolichovespula. As shown a [Vespula germanica](https://en.wikipedia.org/wiki/Vespula_germanica), [Image](https://commons.wikimedia.org/wiki/File:Vespula_germanica_Richard_Bartz.jpg) by [Richard Bartz](https://commons.wikimedia.org/wiki/User:Richard_Bartz), August 10, 2007, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Wasp from Wikipedia](https://en.wikipedia.org/wiki/Wasp)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Wasp 1.01 x64 by John Stanback released ...](http://www.talkchess.com/forum/viewtopic.php?t=60550) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), June 22, 2016
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Frank's Chess Page, Wasp by John Stanback](http://www.amateurschach.de/main/_wasp.htm), June 22, 2016
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Wasp 2.00 by John Stanback ... with Lazy SMP!](http://www.talkchess.com/forum/viewtopic.php?t=63783) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), April 21, 2017
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Wasp NN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75794&start=4) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), November 14, 2020
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Wasp 5.00 released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78687) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), November 18, 2021
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> based on [Wasp Release Notes](http://www.amateurschach.de/main/wasp/release_notes_101.txt) by [John Stanback](John_Stanback "John Stanback")

**[Up one level](Engines "Engines")**







 
