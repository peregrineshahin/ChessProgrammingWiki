---
title: Wukong JS
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Wukong JS**



[ Sun Wukong <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Wukong JS**, (WukongJS)  

a [open source chess engine](Category:Open_Source "Category:Open Source") and [user interface](GUI "GUI") by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"). Wukong JS is written in [JavaScript](JavaScript "JavaScript"),
either to run as [HTML](https://en.wikipedia.org/wiki/HTML) document inside a [web browser](https://en.wikipedia.org/wiki/Web_browser) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, or in [UCI](UCI "UCI") mode via [Node.js](https://en.wikipedia.org/wiki/Node.js).
Further, Wukong JS offers an [API](https://en.wikipedia.org/wiki/API) to embed Wukong JS in third party websites. 



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc)
* [5 References](#references)






### [Board Representation](Board_Representation "Board Representation")


* [0x88](0x88 "0x88")
* [Piece-Lists](Piece-Lists "Piece-Lists")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Negamax](Negamax "Negamax") [PVS](Principal_Variation_Search "Principal Variation Search")
* [Repetition Hash Table](Repetitions#RepetitionHashTable "Repetitions")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [PV-Move](PV-Move "PV-Move")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Razoring](Razoring "Razoring")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


based on [RofChade](RofChade "RofChade") and [PeSTO](PeSTO "PeSTO") by [Ronald Friederich](Ronald_Friederich "Ronald Friederich") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>



* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## See also


* [BMCP(JS)](BMCP(JS) "BMCP(JS)")
* [Wukong](Wukong "Wukong")


## Forum Posts


* [Wukong JS - chess engine with UCI support, own GUI and public API](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76101) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), December 19, 2020
* [New engine release - Wukong JS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76119) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), December 21, 2020
* [Setup a javascript engine in a GUI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76140) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), December 24, 2020
* [Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 05, 2021


 [Re: Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238&start=15) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 07, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
## External Links


### Chess Engine


* [GitHub - maksimKorzh/wukongJS: JavaScript chess engine with UCI support, own GUI and public API written](https://github.com/maksimKorzh/wukongJS) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh")
* [wukongJS/tools/eval\_tuner at main · maksimKorzh/wukongJS · GitHub](https://github.com/maksimKorzh/wukongJS/tree/main/tools/eval_tuner) » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [WukongJS](https://maksimkorzh.github.io/wukongJS/wukong.html)
* [wukongJS/TEXEL'S\_TUNING.MD at main · maksimKorzh/wukongJS · GitHub](https://github.com/maksimKorzh/wukongJS/blob/main/docs/TEXEL%27S_TUNING.MD)
* [Breaking down Texel's tuning method - automated evaluation function tuning in chess engines](https://youtu.be/3JCWxH6IehQ) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), January 07, 2021, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


  
### Misc


* [Wukong (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Wukong_(disambiguation))
* [Monkey King (Sun Wukong) from Wikipedia](https://en.wikipedia.org/wiki/Monkey_King)
* [Typhoon Wukong from Wikipedia](https://en.wikipedia.org/wiki/Typhoon_Wukong)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A 19th-century illustration of the character [Sun Wukong](https://en.wikipedia.org/wiki/Monkey_King), or "[the Wanderer Sun](https://en.wikipedia.org/wiki/Monkey_King#Names_and_titles)". [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [WukongJS](https://maksimkorzh.github.io/wukongJS/wukong.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [wukongJS/wukong.js at main · maksimKorzh/wukongJS · GitHub | Evaluate](https://github.com/maksimKorzh/wukongJS/blob/main/wukong.js#L898)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 28, 2018

**[Up one Level](Engines "Engines")**







 
