---
title: Neural MoveMap Heuristic
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Neural MoveMap Heuristic**



[ Feedforward artificial neural network <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Neural MoveMap Heuristic**, (NMM heuristic)  

a move ordering heuristic introduced by [Levente Kocsis](Levente_Kocsis "Levente Kocsis") at al., applied to the games of [Lines of Action](Lines_of_Action "Lines of Action") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and chess <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The NMM heuristic utilizes a [neural network](Neural_Networks "Neural Networks"), trained to estimate the likelihood of a [move](Moves "Moves") being the [best one](Best_Move "Best Move") in a certain [chess position](Chess_Position "Chess Position"). The best performing NN architecture resulted from an input layer consisting of 6 neurons per [square](Squares "Squares") (for each particular [piece](Pieces "Pieces"), -1 Black, 0-None, +1 White) plus one neuron for the side to move, and an [butterfly](Butterfly_Boards "Butterfly Boards") output layer of 1792 neurons corresponding to valid 64x64 [from-](Origin_Square "Origin Square") and [to-squares](Target_Square "Target Square") of the moves. Although the network is very large, the move scores can be computed quickly, since one only has to propagate the activation for the pieces actually on the board, and to compute only the scores for the legal moves. An enhanced approach of the NMM heuristic used a weighted combination of the neural network and the [history-heuristic](History_Heuristic "History Heuristic") scores, tested for middle-game chess positions with [Crafty](Crafty "Crafty"), yielding in encouraging results using [Rprop](https://en.wikipedia.org/wiki/Rprop) as [learning](Learning "Learning") [algorithm](Algorithms "Algorithms") during the training phase with 4 times (from [ECO](ECO "ECO") A30, B84, D85 and E97) 3000 positions <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### Contents


* [1 See also](#see-also)
* [2 Publications](#publications)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






* [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
* [Chessmaps Heuristic](Chessmaps_Heuristic "Chessmaps Heuristic")
* [Guard Heuristic](Guard_Heuristic "Guard Heuristic")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Neural Networks](Neural_Networks "Neural Networks")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")


## Publications


* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Move Ordering using Neural Networks*. IEA/AIE 2001, [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2070
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/movemap_heuristic.pdf)
* [Mark Winands](Mark_Winands "Mark Winands"), [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *Temporal difference learning and the Neural MoveMap heuristic in the game of Lines of Action*. GAME-ON 2002
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis") (**2003**). *Learning Search Decisions*. Ph.D thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](https://project.dke.maastrichtuniversity.nl/games/files/phd/Kocsis_thesis.pdf)


## Forum Posts


* [Neural MoveMap](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77327) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), May 17, 2021


## External Links


* [Backpropagation from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation)
* [Feedforward neural network from Wikipedia](https://en.wikipedia.org/wiki/Feedforward_neural_network)
* [Rprop from Wikipedia](https://en.wikipedia.org/wiki/Rprop)
* [Brecker Brothers](https://en.wikipedia.org/wiki/Brecker_Brothers) - Sponge, [Kristianstad/Åhus Jazzfestivalen](https://sv.wikipedia.org/wiki/Kristianstad/%C3%85hus_Jazzfestival), July 1980, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker"), [Randy Brecker](Category:Randy_Brecker "Category:Randy Brecker"), [Barry Finnerty](https://en.wikipedia.org/wiki/Barry_Finnerty), [Mark Gray](http://www.allmusic.com/artist/mark-gray-mn0001423900/credits), [Neil Jason](https://en.wikipedia.org/wiki/Neil_Jason), [Richie Morales](http://www.allmusic.com/artist/richie-morales-mn0000298182/credits)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Depiction of a single-layer feedforward artificial neural network. Arrows originating at x2 are omitted for clairty. This network has p inputs and q outputs. [Image](https://commons.wikimedia.org/wiki/File:Single_layer_ann.svg) by [Mcstrother](https://en.wikipedia.org/wiki/User:Mcstrother), February 17, 2010, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Artificial neural network from Wikipedia](https://en.wikipedia.org/wiki/Artificial_neural_network)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Move Ordering using Neural Networks*. IEA/AIE 2001, [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2070
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/movemap_heuristic.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/movemap_heuristic.pdf)

**[Up one Level](Move_Ordering "Move Ordering")**







 
