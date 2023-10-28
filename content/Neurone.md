---
title: Neurone
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Neurone**



[ Neurone <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Neurone**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") compatible chess engine by [Luca Lissandrello](Luca_Lissandrello "Luca Lissandrello"), written in [Visual Basic .NET](Basic#VB "Basic")
<a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Neurone features standard [search](Search "Search") and [evaluation](Evaluation "Evaluation") techniques, such as [iterative deepening](Iterative_Deepening "Iterative Deepening") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), 
and has its own [endgame tablebase](Endgame_Tablebases "Endgame Tablebases") format with up to one [pawn](Pawn "Pawn"). It supports the [Beowulf](Beowulf "Beowulf") [opening book](Opening_Book "Opening Book") format by [Colin Frayn](Colin_Frayn "Colin Frayn"), and is able to [ponder](Pondering "Pondering").
As one of the weaker chess engines around <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
Neurone played the [IOCSC 2010](IOCSC_2010 "IOCSC 2010"), [IOCSC 2011](IOCSC_2011 "IOCSC 2011"), and [IOCSC 2012](IOCSC_2012 "IOCSC 2012") editions of the [Italian Open Chess Software Cups](Italian_Computer_Chess_Championship#IOCSC "Italian Computer Chess Championship"), and the [IGT 2013](IGT_2013 "IGT 2013"), [IGT 2014](IGT_2014 "IGT 2014"), [IGT 2015](IGT_2015 "IGT 2015"), and [IGT 2016](IGT_2016 "IGT 2016") over the board, and on-line the [CCT14](CCT14 "CCT14") and [CCT15](CCT15 "CCT15"). 



### Contents


* [1 Neurolearning](#neurolearning)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc)
* [4 References](#references)






Since version XXI the ability of [learning](Learning "Learning") was implemented, due to the similarity with human reasoning dubbed **Neurolearning**.
It combines [supervised learning](Supervised_Learning "Supervised Learning") and [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") techniques, 
separated for the three [game phases](Game_Phases "Game Phases"), [opening](Opening "Opening") (Phase 1), [middlegame](Middlegame "Middlegame") (Phase 2), and [endgame](Endgame "Endgame") (Phase 3) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



 [](File:Neurolearning.jpg) 
1. Phase 1 learning considers a WDL discretized score (> 1.2,< -0.6) of the position ten moves after playing the last book move along with the final outcome as reinforcement signal, encoded in an opponent specific [book learning](Book_Learning "Book Learning") file supplementing the standard read-only [opening book](Opening_Book "Opening Book").
2. Phase 2 learning utilizes a [persistent hash table](Persistent_Hash_Table "Persistent Hash Table"), whose entries might be modified in an analysing supervisor mode, looking for possible better moves.
3. Phase 3 learning is intended to enlarge Neurone's specific [endgame tablebases](Endgame_Tablebases "Endgame Tablebases").


## Forum Posts


* [Engine update: Neurone I](http://www.talkchess.com/forum/viewtopic.php?t=33074) by [Alex Brunetti](Alex_Brunetti "Alex Brunetti"), [CCC](CCC "CCC"), March 04, 2010
* [Re: Which are the chess engines written from scratch ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=50942&start=47) by [Luca Lissandrello](Luca_Lissandrello "Luca Lissandrello"), [CCC](CCC "CCC"), January 17, 2014
* [Neurone XXV released](http://www.talkchess.com/forum/viewtopic.php?t=61848) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), October 26, 2016


## External Links


### Chess Engine


* [Neurone](http://www.g-sei.org/neurone/) - [G 6](G_6 "G 6") (Italian)
* [Neurolearning](http://www.g-sei.org/neurolearning/) « [G 6](G_6 "G 6") (Italian)
* [Progetto Neurone - lissandrello.it](http://www.lissandrello.it/?cat=10) (Italian)
* [Neurone](https://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Neurone&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Misc


* [Neurone from Wikipedia.it](https://it.wikipedia.org/wiki/Neurone) (Italian)
* [Neuron from Wikipedia](https://en.wikipedia.org/wiki/Neuron)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Neuron in a scanning [electron microscope](https://en.wikipedia.org/wiki/Electron_microscope), [Image](https://commons.wikimedia.org/wiki/File:Neuron-SEM.png) by [Nicolas P. Rougier](http://www.loria.fr/~rougier/), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Neurone](http://www.g-sei.org/neurone/) - [G 6](G_6 "G 6") (Italian)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Luca Lissandrello](Luca_Lissandrello "Luca Lissandrello"): *Penso sia uno dei chess engines più deboli in assoluto… per ora*. [Lissandrello Luca « G 6](http://www.g-sei.org/author/lissandrello-luca/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Neurolearning](http://www.g-sei.org/neurolearning/) « [G 6](G_6 "G 6") (Italian)

**[Up one Level](Engines "Engines")**







 
