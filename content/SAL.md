---
title: SAL
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SAL**



[ HAL 9000 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SAL**, (Search and Learn)  

a [general game playing](General_Game_Playing "General Game Playing") and [learning](Learning "Learning") [open source program](Category:Open_Source "Category:Open Source") for any [two-player](https://en.wikipedia.org/wiki/Two-player_game) [board game](https://en.wikipedia.org/wiki/Board_game) of [perfect information](https://en.wikipedia.org/wiki/Perfect_information), written by [Michael Gherrity](Michael_Gherrity "Michael Gherrity") as subject of his Ph.D. thesis *A Game Learning Machine* <a id="cite-note-2" href="#cite-ref-2">[2]</a>. SAL is written in [ANSI C](C "C") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Search


For all games, SAL performs a two-ply, full-width [alpha-beta](Alpha-Beta "Alpha-Beta") search plus *consistency search* <a id="cite-note-4" href="#cite-ref-4">[4]</a>, which is a generalized [quiescence search](Quiescence_Search "Quiescence Search") as proposed by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Evaluation


The game independent [evaluation](Evaluation "Evaluation") is implemented as [neural network](Neural_Networks "Neural Networks") for each side. The inputs to the network are features [representing the board](Board_Representation "Board Representation"), the number of [pieces](Pieces "Pieces") of each type on the board, the type of piece just moved, the type of piece just captured (if any), and several features considering pieces and squares under attack. The neural network evaluator is trained by [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") to estimate the outcome of the game, given the current position <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## Results


* In [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe), SAL learned to play perfectly after 20,000 games
* In [Connect four](Connect_Four "Connect Four"), SAL learned to defeat an opponent program about 80% of the time after 100,000 games
* In Chess, after 4200 games against [GNU Chess](GNU_Chess "GNU Chess"), SAL evolved from a random mover to a reasonable, but still weak chess player


## See also


* [General Game Playing](General_Game_Playing "General Game Playing")
* [HAL](HAL "HAL")
* [Metagamer](index.php?title=Metagamer&action=edit&redlink=1 "Metagamer (page does not exist)")
* [Zillions of Games](Zillions_of_Games "Zillions of Games")


## Publications


* [Michael Gherrity](Michael_Gherrity "Michael Gherrity") (**1993**). *A Game Learning Machine*. Ph.D. thesis, [University of California, San Diego](https://en.wikipedia.org/wiki/University_of_California,_San_Diego), advisor [Paul Kube](Mathematician#PKube "Mathematician"), [pdf](http://www.gherrity.org/thesis.pdf), [pdf](http://www.top-5000.nl/ps/A%20game%20learning%20machine.pdf)
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)


## Forum Posts


* [Subject: Re: Game Learning](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/games/doc/strategy.txt) by [Mike Gherrity](Michael_Gherrity "Michael Gherrity"), [ai-repository](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/), July 1, 1994 <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Sal or neurochess](http://www.talkchess.com/forum/viewtopic.php?t=40290) by ethan ara, [CCC](CCC "CCC"), September 06, 2011


## External Links


### Game Player


* [SAL](http://satirist.org/learn-game/systems/sal.html) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
* [SAL source code](http://www.gherrity.org/sal6.tar.gz)


### Misc


* [Sal (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Sal)
* [SAL 9000](https://en.wikipedia.org/wiki/HAL_9000#SAL_9000) fictional computer in [2010: Odyssey Two](https://en.wikipedia.org/wiki/2010:_Odyssey_Two)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The famous red eye of [HAL 9000](https://en.wikipedia.org/wiki/HAL_9000), the fictional character in [Arthur C. Clarke's](Category:Arthur_C._Clarke "Category:Arthur C. Clarke") [Space Odyssey](https://en.wikipedia.org/wiki/Space_Odyssey) series. [Image](https://commons.wikimedia.org/wiki/File:HAL9000.svg) by Cryteria, October 1, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) - A game sequence between [Frank Poole](https://en.wikipedia.org/wiki/Space_Odyssey#Characters) and HAL 9000 is given in the preface of [Michael Gherrity's](Michael_Gherrity "Michael Gherrity") [thesis](Michael_Gherrity#thesis "Michael Gherrity")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Michael Gherrity](Michael_Gherrity "Michael Gherrity") (**1993**). *A Game Learning Machine*. Ph.D. thesis, [University of California, San Diego](https://en.wikipedia.org/wiki/University_of_California,_San_Diego), advisor [Paul Kube](Mathematician#PKube "Mathematician"), [pdf](http://www.gherrity.org/thesis.pdf), [pdf](http://www.top-5000.nl/ps/A%20game%20learning%20machine.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [SAL source code](http://www.gherrity.org/sal6.tar.gz)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Consistency search](http://satirist.org/learn-game/methods/search/consistency.html) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Don Beal](Don_Beal "Don Beal") (**1989**). *Experiments with the Null Move.* [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), a revised version is published (**1990**) under the title *A Generalized Quiescence Search Algorithm*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [SAL](http://satirist.org/learn-game/systems/sal.html) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf), 1.1 Related Work
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Barney Pell](Barney_Pell "Barney Pell") (**1993**). *Strategy Generation and Evaluation for Meta-Game Playing*. Ph.D: thesis, [Trinity College, Cambridge](https://en.wikipedia.org/wiki/Trinity_College,_Cambridge), [pdf](http://www.barneypell.com/papers/pell-thesis.pdf)

**[Up one level](Engines "Engines")**







 
