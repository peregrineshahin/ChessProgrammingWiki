---
title: Loki
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Loki**



[ Loki with a fishing net <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Loki**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), written in [C++ 17](Cpp "Cpp"), first released in February 2021 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The author reports progress on Loki in an own [CCC](CCC "CCC") forum thread [[3]](#cite-note-progess-3).



## Features


<a id="cite-note-6" href="#cite-ref-6">[6]</a> [[3]](#cite-note-progess-3)



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta") ([Fail-Hard](Fail-Hard "Fail-Hard"))
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [PV-Move](PV-Move "PV-Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Captures](Captures "Captures") by [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
	+ [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Razoring](Razoring "Razoring")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Safe Mobility](Mobility#Safe_Mobility "Mobility")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")


### Misc


* [SPSA](SPSA "SPSA") [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [Perft](Perft "Perft")


## See also


* [Freyr](Freyr "Freyr")
* [Thor's Hammer](Thor%27s_Hammer "Thor's Hammer")


## Forum Posts


* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=91) (Loki 1.0.2) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 21, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=139) (Loki 2.0.0) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), March 11, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=215) (Loki 3.0) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 13, 2021
* [Progress on Loki](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77105) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 16, 2021
* [Tuning search parameters](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77118) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 18, 2021
* [Staged move generation done right (Progress on Loki)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77105&start=74)] by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), July 23, 2021


## External Links


### Chess Engine


* [GitHub - BimmerBass/Loki - C++17 chess engine](https://github.com/BimmerBass/Loki)
* [Loki](https://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Loki&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Loki - Wiktionary](https://en.wiktionary.org/wiki/Loki)
* [Loki from Wikipedia](https://en.wikipedia.org/wiki/Loki)
* [Loki (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Loki_(disambiguation))
* [Loki (comics) from Wikipedia](https://en.wikipedia.org/wiki/Loki_(comics))
* [Loki Entertainment from Wikipedia](https://en.wikipedia.org/wiki/Loki_Entertainment)
* [Modern C++ Design - Loki library from Wikipedia](https://en.wikipedia.org/wiki/Modern_C%2B%2B_Design#Loki_library)
* [LOKI from Wikipedia](https://en.wikipedia.org/wiki/LOKI)
* [Donald Byrd](https://en.wikipedia.org/wiki/Donald_Byrd) - Loki, [Blackjack](https://en.wikipedia.org/wiki/Blackjack_(Donald_Byrd_album)) (1967), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Sonny Red](https://en.wikipedia.org/wiki/Sonny_Red), [Hank Mobley](https://en.wikipedia.org/wiki/Hank_Mobley), [Cedar Walton](https://en.wikipedia.org/wiki/Cedar_Walton), [Walter Booker](https://en.wikipedia.org/wiki/Walter_Booker), [Billy Higgins](https://en.wikipedia.org/wiki/Billy_Higgins)
 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Loki with a fishing net](https://commons.wikimedia.org/wiki/File:Processed_SAM_loki.jpg), A [Norse mythology](https://en.wikipedia.org/wiki/Norse_mythology) image from the [18th century](https://en.wikipedia.org/wiki/18th_century) [Icelandic manuscript SÁM 66](https://en.wikipedia.org/wiki/Icelandic_Manuscript,_S%C3%81M_66), now in the care of the [Árni Magnússon Institute for Icelandic Studies](https://en.wikipedia.org/wiki/%C3%81rni_Magn%C3%BAsson_Institute_for_Icelandic_Studies), [Loki from Wikipedia](https://en.wikipedia.org/wiki/Loki), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=91) (Loki 1.0.2) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 21, 2021
3. ↑ [3.0](#cite-ref-progess-3-0) [3.1](#cite-ref-progess-3-1) [Progress on Loki](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77105) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 16, 2021
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [BimmerBass/Loki - C++17 chess engine | Why the name?](https://github.com/BimmerBass/Loki#why-the-name)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Loki from Wikipedia](https://en.wikipedia.org/wiki/Loki)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [GitHub - BimmerBass/Loki - C++17 chess engine](https://github.com/BimmerBass/Loki)

**[Up one level](Engines "Engines")**







 
