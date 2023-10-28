---
title: Octavius
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Octavius**



[ [Gaius Octavius](https://en.wikipedia.org/wiki/Gaius_Octavius_%28praetor_61_BC%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Octavius**,  

a chess engine by [Luke Pellen](Luke_Pellen "Luke Pellen") relying purely on an [evaluation](Evaluation "Evaluation") based on a four-layer [neural network](Neural_Networks "Neural Networks") without any [material](Material "Material") analysis, choosing the [move](Moves "Moves") with the best [score](Score "Score") on its single output neuron, performing a one [ply](Ply "Ply") [look ahead](Search "Search"). 
Despite [Sebastian Thrun's](Sebastian_Thrun "Sebastian Thrun") remark, that using the raw [board representation](Board_Representation "Board Representation") as input of a neural network is a poor choice <a id="cite-note-2" href="#cite-ref-2">[2]</a>, but quite similar to one input representation of the [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic") by [Levente Kocsis](Levente_Kocsis "Levente Kocsis") et al. <a id="cite-note-3" href="#cite-ref-3">[3]</a>, Octavius has an input layer of 768 (12x64) nodes, a sequence of 12 numbers (11 or 12 times 0.0, 1 or 0 times 1.0) for each [square](Squares "Squares"), where a 1.0 was given for the particular [piece](Pieces "Pieces") (if any) residing on that square. Two hidden layers with 1024 and 512 nodes are feed forward to one output node, which represents the score of the position for one side to move. In total, Octavius' net has 2305 nodes with 1,311,232 connections. 



### Contents


* [1 Selected Games](#selected-games)
* [2 See also](#see-also)
* [3 Publications](#publications)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






Beginning in 1999, Octavius performed 284,552 [backpropagations](Neural_Networks#Backpropagation "Neural Networks") up to April 26, 2004, when it won its first game against his creator <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```

[Event "Octavius Test"]
[Site "Lukes Computer"]
[Date "2004.04.26"]
[Round "?"]
[White "Luke Pellen"]
[Black "Octavius P4Oct4.ann"]
[Result "0-1"]

1.e4 Nf6 2.Nc3 e5 3.Bb5 c6 4.Ba4 Bc5 5.Nf3 O-O 6.O-O d6 7.d3 Bg4 
8.Bb3 Nh5 9.a3 Re8 10.Ba2 Qf6 11.Bg5 Qg6 12.b4 Bb6 13.Bh4 Nf4 
14.Kh1 Nd7 15.g3 Nh3 16.Qe2 h5 17.Rae1 d5 18.exd5 cxd5 19.Nxd5 e4 
20.dxe4 Rxe4 21.Qxe4 f5 22.Qe7 Bxf3# 0-1

```

## See also


* [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")


## Publications


* [Luke Pellen](Luke_Pellen "Luke Pellen") (**2008**). *[How not to Imitate a Human Being](https://link.springer.com/chapter/10.1007/978-1-4020-6710-5_25)*. Chapter 25 in [Robert Epstein](https://en.wikipedia.org/wiki/Robert_Epstein), Gary Roberts, Grace Beber (eds.) (**2008**). *[Parsing the Turing Test](http://link.springer.com/book/10.1007%2F978-1-4020-6710-5)*. Philosophical and Methodological Issues in the Quest for the Thinking Computer, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


## Forum Posts


* [announcement: Octavius V1.3 ANN chess s/w available...](https://groups.google.com/d/msg/rec.games.chess.computer/9y7t9kyOEB4/KECNKlUfFP0J) by [Luke Pellen](Luke_Pellen "Luke Pellen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 22, 1999
* [Re: Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/4WmiglfGPvgJ) by Cnidarian, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 30, 2000
* [A WIN FOR OCTAVIUS! - Chess ANN](https://groups.google.com/d/msg/comp.ai.neural-nets/QGhfg1k_yOg/wE8bEMCTW2UJ) by [Luke Pellen](Luke_Pellen "Luke Pellen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 15, 2003
* [Chess Neural Network: ANOTHER VICTORY FOR OCTAVIUS!](https://groups.google.com/d/msg/rec.games.chess.computer/D8ug0bq02Cs/SBikPRjdhJEJ) by [Luke Pellen](Luke_Pellen "Luke Pellen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 04, 2004


## External Links


* [Octavius (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Octavius_%28disambiguation%29)
* [Octavius (praenomen) from Wikipedia](https://en.wikipedia.org/wiki/Octavius_%28praenomen%29)
* [Octavia (gens) from Wikipedia](https://en.wikipedia.org/wiki/Octavia_%28gens%29)
* [Gaius Octavius (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Gaius_Octavius_%28disambiguation%29)
* [Gaius Octavius (praetor 61 BC) from Wikipedia](https://en.wikipedia.org/wiki/Gaius_Octavius_%28praetor_61_BC%29)
* [Augustus from Wikipedia](https://en.wikipedia.org/wiki/Augustus)
* [Octavius Mamilius from Wikipedia](https://en.wikipedia.org/wiki/Octavius_Mamilius)
* [Eudaf Hen from Wikipedia](https://en.wikipedia.org/wiki/Eudaf_Hen)
* [Prince Octavius of Great Britain from Wikipedia](https://en.wikipedia.org/wiki/Prince_Octavius_of_Great_Britain)
* [Octavius (ship) from Wikipedia](https://en.wikipedia.org/wiki/Octavius_%28ship%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Head of statue, thought to be Gaius Octavius, ca. 60 BC, [Munich](https://en.wikipedia.org/wiki/Munich) [Glyptothek](https://en.wikipedia.org/wiki/Glyptothek), Room 11, Photo by [Bibi Saint-Pol](https://commons.wikimedia.org/wiki/User:Bibi_Saint-Pol), February 08, 2007, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Gaius Octavius (praetor 61 BC) from Wikipedia](https://en.wikipedia.org/wiki/Gaius_Octavius_%28praetor_61_BC%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. [pdf](http://papers.nips.cc/paper/1007-learning-to-play-the-game-of-chess.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/movemap_heuristic.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Neural Network: ANOTHER VICTORY FOR OCTAVIUS!](https://groups.google.com/d/msg/rec.games.chess.computer/D8ug0bq02Cs/SBikPRjdhJEJ) by [Luke Pellen](Luke_Pellen "Luke Pellen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 04, 2004

**[Up one Level](Engines "Engines")**







 
