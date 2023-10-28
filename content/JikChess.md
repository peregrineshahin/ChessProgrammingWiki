---
title: JikChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* JikChess**


**JikChess**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Janne I. Kokkala](index.php?title=Janne_I._Kokkala&action=edit&redlink=1 "Janne I. Kokkala (page does not exist)"), written in [C++11](Cpp "Cpp"). Its development started in early 2013, and the first version was released in November 2014 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.



### Contents


* [1 Features](#features)
	+ [1.1 Search](#search)
	+ [1.2 Evaluation](#evaluation)
	+ [1.3 Misc](#misc)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






<a id="cite-note-2" href="#cite-ref-2">[2]</a>



### Search


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search") with [Captures](Captures "Captures") and [Promotions](Promotions "Promotions") only
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Fractional Ply](Extensions#FractionalExtensions "Extensions") [PV Extensions](PV_Extensions "PV Extensions")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Transposition Table](Transposition_Table "Transposition Table")
	+ [Captures](Captures "Captures") by [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")


### Evaluation


* [Linear Combination](Evaluation#Linear "Evaluation") of Numerical Positional Features
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Automated Tuning](Automated_Tuning "Automated Tuning")
	+ [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning") (Similar to [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"))
	+ [Regularization](https://en.wikipedia.org/wiki/Regularization_%28mathematics%29) - [Prior](https://en.wikipedia.org/wiki/Prior_probability) added to the [Cost Function](https://en.wikipedia.org/wiki/Loss_function) (encourages unimportant parameters to become zero)


### Misc


* [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book")
* [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")


## Forum Posts


* [JikChess 0.01 by Janne I. Kokkala](http://www.talkchess.com/forum/viewtopic.php?t=54598) by Ruxy Sylwyka, [CCC](CCC "CCC"), December 09, 2014
* [JikChess 0.02 released](http://www.talkchess.com/forum/viewtopic.php?t=58016) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 22, 2015


## External Links


* [JikChess chess engine](http://koti.kapsi.fi/jik/jikchess/)
* [JikChess 0.02 64-bit](http://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=JikChess%200.02%2064-bit) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [JikChess - History](http://koti.kapsi.fi/jik/jikchess/#history)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> based on [JikChess - Technical](http://koti.kapsi.fi/jik/jikchess/#technical)

**[Up one Level](Engines "Engines")**







 
