---
title: Woodpusher
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Woodpusher**



[](File:Woodpusher.JPG) Woodpusher mascot
**Woodpusher**,  

a chess program developed in 1989 by [John Hamlen](John_Hamlen "John Hamlen") as part of a university project looking into [null-move](Null_Move "Null Move") search techniques. Woodpusher played various [World Computer-](World_Computer_Chess_Championship "World Computer Chess Championship"), [World Microcomputer Chess Championships](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") and [Computer Olympiads](Computer_Olympiad "Computer Olympiad"). *Woodpusher 1997* played the [WCCC 2004](WCCC_2004 "WCCC 2004") in [Ramat-Gan](https://en.wikipedia.org/wiki/Ramat_Gan) and the [WCCC 2011](WCCC_2011 "WCCC 2011") in [Tilburg](https://en.wikipedia.org/wiki/Tilburg) as an experiment to play with a seven respectively fourteen years old program. 



### Contents


* [1 Description](#description)
* [2 Photos](#photos)
* [3 Namesakes](#namesakes)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
	+ [7.1 Chess Engine](#chess-engine)
	+ [7.2 Misc](#misc)
* [8 References](#references)






Description given in 1995 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-1" href="#cite-ref-1">[1]</a> :




```C++
Woodpusher is a small chess program (< 64K) of conventional design. It uses an [iterative deepening](Iterative_Deepening "Iterative Deepening") [alpha-beta search](Alpha-Beta "Alpha-Beta") with [PVS](Principal_Variation_Search "Principal Variation Search") and [aspiration window](Aspiration_Windows "Aspiration Windows") enhancements. The first version of Woodpusher was born in 1989 as part of a university project looking into [null-move](Null_Move "Null Move") search techniques. True to it's origins, this new version of the program still uses the null-move throughout the search to recognize threats and to [forward prune](Pruning "Pruning") branches of the [search tree](Search_Tree "Search Tree"). A [database of attacks](Attack_and_Defend_Maps "Attack and Defend Maps") from and to all the squares on the board is maintained by using [CHESS 4.5's](Chess_(Program) "Chess (Program)") [bit-board](Bitboards "Bitboards") implementation. These data structures are used for both [generating moves](Move_Generation "Move Generation") and making positional [evaluations](Evaluation "Evaluation"). Woodpusher's position evaluation is maintained almost entirely [incrementally](Incremental_Updates "Incremental Updates") while [making](Make_Move "Make Move") and [un-making](Unmake_Move "Unmake Move") moves during the search, with very little work done at the [terminal nodes](Terminal_Node "Terminal Node"). The evaluation is therefore necessarily simple, but does include true measures of [mobility](Mobility "Mobility") rather than relying on [piece-square evaluations](Piece-Square_Tables "Piece-Square Tables"). 

```

## Photos


[](File:Wccc2011-3.JPG)
[WCCC 2011](WCCC_2011 "WCCC 2011"), Woodpusher 1997 by [John Hamlen](John_Hamlen "John Hamlen") vs. [Pandix](Pandix "Pandix") by [Gyula Horváth](Gyula_Horv%C3%A1th "Gyula Horváth") (left) <a id="cite-note-2" href="#cite-ref-2">[2]</a>



## Namesakes


* [WoodPusher](http://mono-code.sourceforge.net/) a chess application written in [C#](C_sharp "C sharp") by [Jamin P. Gray](http://sourceforge.net/projects/mono-code/)


## See also


* [Knowledge | Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Patzer](Patzer "Patzer")
* [Woodpecker](Woodpecker "Woodpecker")


## Publications


* [John Hamlen](John_Hamlen "John Hamlen") (**2004**). *Seven Year Itch*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_1 "ICGA Journal") <a id="cite-note-3" href="#cite-ref-3">[3]</a> » [WCCC 2004](WCCC_2004 "WCCC 2004")
* [John Hamlen](John_Hamlen "John Hamlen") (**2012**). *Game Over for the Woodpusher Experiment: 7+7=0*. [ICGA Journal, Vol. 35, No. 1](ICGA_Journal#35_1 "ICGA Journal") » [WCCC 2011](WCCC_2011 "WCCC 2011")


## Forum Posts


* [I think that woodpusher is the surprise of the tournament](https://www.stmintz.com/ccc/index.php?id=376346) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 13, 2004 » [WCCC 2004](WCCC_2004 "WCCC 2004")
* [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge"), [1st Computer Olympiad](1st_Computer_Olympiad#Chess "1st Computer Olympiad")


## External Links


### Chess Engine


* [Woodpusher's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=33)


### Misc


* [woodpusher - Wiktionary](https://en.wiktionary.org/wiki/woodpusher)
* [Glossary of chess - woodpusher, Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#woodpusher)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Woodpusher's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=33)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Photos by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Seven Year Itch (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Seven_Year_Itch_%28disambiguation%29)

**[Up one Level](Engines "Engines")**







 
