---
title: Zahak
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Zahak**



[](File:Zahak_logo.jpg) Zahak's Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> - Designed by Nasrin Zaza <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Zahak**,  

a [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Amanj Sherwany](Amanj_Sherwany "Amanj Sherwany"), written in [Go](Go "Go"), licensed under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") and first released on [GitHub](https://en.wikipedia.org/wiki/GitHub) in February 2021 <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
Since version 7, Zahak's hand crafted  [evaluation function](Evaluation_Function "Evaluation Function") is replaced with an  [NNUE style](NNUE "NNUE") evaluation, which is trained by a from scratch written trainer, that is written in [Go](Go "Go") as well <a id="cite-note-4" href="#cite-ref-4">[4]</a>. The network is trained on self-play games between different versions of Zahak. As of version 8, Zahak features an own network architecture which consists of 769 input features, that represents all the pieces on the board as well as a feature to represent white-to-move. The training process is thoroughly documented <a id="cite-note-5" href="#cite-ref-5">[5]</a>. As of the time of this writing, Zahak is the only [NNUE](NNUE "NNUE") engine that is written in [Go](Go "Go").


Zahak started its first debut in [TCEC](TCEC "TCEC") in Swiss 2 event of S21 <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



## Features


<a id="cite-note-8" href="#cite-ref-8">[8]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards") for sliding pieces.
* Multi-Stage Pseudo-Legal [Move Generation](Move_Generation "Move Generation")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [Captures](Captures "Captures")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") based Pruning
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE") (>= Zahak 7)


### Misc


* [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book")
* [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [MultiPV](Principal_Variation#MultiPV "Principal Variation")
* [Skill Levels](Playing_Strength "Playing Strength")


## Forum Posts


* [Zahak, a GoLang based chess engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76855) by [Amanj Sherwany](Amanj_Sherwany "Amanj Sherwany"), [CCC](CCC "CCC"), March 13, 2021


## External Links


### Chess Engine


* [GitHub - amanjpro/zahak: A UCI compatible chess AI in Go](https://github.com/amanjpro/zahak)
* [Zahak in CCRL 40/15](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Zahak&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)


### Misc


* [Zahhak from Wikipedia](https://en.wikipedia.org/wiki/Zahhak)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [GitHub - amanjpro/zahak: A UCI compatible chess AI in Go - Name](https://github.com/amanjpro/zahak#zahak)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Nasrin Zaza · LinkedIn Profile](https://www.linkedin.com/in/nasrin-zaza)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Release Zahak 0.0.1 · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak/releases/tag/0.0.1)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [amanjpro/zahak-trainer · GitHub](https://github.com/amanjpro/zahak-trainer)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Training Documentation · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak/blob/master/training.md)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [TCEC Swiss 2 Wiki](https://wiki.chessdom.org/TCEC_Swiss_2)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Zahhak from Wikipedia](https://en.wikipedia.org/wiki/Zahhak)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> Features based on [README.md · amanjpro/zahak · GitHub](https://github.com/amanjpro/zahak#implemented-features)

**[Up one level](Engines "Engines")**







 
