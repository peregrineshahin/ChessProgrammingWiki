---
title: Connectivity
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * Connectivity**

\[ [Knight's graph](https://en.wikipedia.org/wiki/Knight%27s_graph) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Connectivity**,

in computer chess, a loosely defined property to quantify positional play based on the [graph theoretical](https://en.wikipedia.org/wiki/Graph_theory) relationship between the [chess pieces](Pieces "Pieces") and the [squares](Squares "Squares") they [control](Square_Control "Square Control") on the [chessboard](Chessboard "Chessboard"). [Danny Kopec](Danny_Kopec "Danny Kopec"), [Ed Northam](Ed_Northam "Ed Northam"), [David Podber](index.php?title=David_Podber&action=edit&redlink=1 "David Podber (page does not exist)") and [Yehya Fouda](index.php?title=Yehya_Fouda&action=edit&redlink=1 "Yehya Fouda (page does not exist)") proposed a connectivity term with some scaling required as sum of products of a value for each own protected pawn and own protected piece in the inverse order of their [point value](Point_Value "Point Value"), i.e. {P=50, N=35, B=30, R=10, Q=4} times a value looked up by their up to three direct or [x-ray](X-ray "X-ray") protectors, i.e. {Single: P=8.00, B=4.50, N=4.00, R=3.00, K=2.50, Q=2.0; Double: PP=15.00, QK=4.00, ...; Triple: PPN=18.00, ...} <a id="cite-note-2" href="#cite-ref-2">[2]</a>. This stems from the idea that the less mobile a piece is, the more protection it needs. The connectivity term encourages [pawn chains](Pawn_Chain "Pawn Chain"), and discourages [loose pieces](Loose_Piece "Loose Piece"). Originally, Kopec et al. used the computation of [entropy](https://en.wikipedia.org/wiki/Entropy), a term taken from physics, which measures the tendency of matter to increase in its level of disorder. A low entropy score was indicative of a high degree of protection and a high connectivity score.

## Trajectories

More complex models concerning connectivity in chess, also considering [progressive mobility](Mobility#ProgressiveMobility "Mobility"), were proposed and elaborated by various researchers. To mention is [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") within his [Pioneer](Pioneer "Pioneer") project with the hierarchical mathematical projection (MP) of [trajectories](Trajectory "Trajectory"), zones consisting of a network of main trajectories conform to attacking or defending plans, opponent's counter trajectories and own supporting counter-counter trajectories <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Simplex and Complex

[Ron Atkin](Ron_Atkin "Ron Atkin") and [Ian H. Witten](Ian_H._Witten "Ian H. Witten") <a id="cite-note-4" href="#cite-ref-4">[4]</a> labeled a piece and the squares that it attacks a simplex, and simplexes are composed into complexes. By analysis of the simplexes and complexes, Atkin and Witten showed that it is possible to make reasonably effective move predictions using real games as a point of comparison <a id="cite-note-5" href="#cite-ref-5">[5]</a>. In line with Atkin and Witten, [Derek Farren](index.php?title=Derek_Farren&action=edit&redlink=1 "Derek Farren (page does not exist)"), [Daniel Templeton](index.php?title=Daniel_Templeton&action=edit&redlink=1 "Daniel Templeton (page does not exist)") and [Meiji Wang](index.php?title=Meiji_Wang&action=edit&redlink=1 "Meiji Wang (page does not exist)") proposed a model of four types of networks, support, mobility, position, and tracking networks, where certain [incremental updated](Incremental_Updates "Incremental Updates") network properties, interpreted as a [time series](https://en.wikipedia.org/wiki/Time_series) during the course of the game, may act as an evaluation feature <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Distance

[Mobility](Mobility "Mobility") as well as connectivity are special cases of the graph-theoretic representation of chess knowledge introduced by [Robert Levinson](Robert_Levinson "Robert Levinson") and [Richard Snyder](Richard_Snyder "Richard Snyder"), uniformly based on a single mathematical abstraction dubbed *Distance*, when squares are only at [distance](Distance "Distance") 1 <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Chess Neighborhood

Related to connectivity and distance is the graph-theoretic representation of Chess neighborhood, proposed by [Robert Levinson](Robert_Levinson "Robert Levinson") and [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)"), as applied in the learning research chess program [Morph](Morph "Morph") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. The chess neighborhood is a vector of 17 elements, focusing a [square](Squares "Squares") of the [chessboard](Chessboard "Chessboard") with 16 satellites corresponding to the closest pieces (if any) of the eight [ray directions](Direction#RayDirections "Direction") and pieces or empty squares in [knight-distance](Knight-Distance "Knight-Distance") of the eight [knight directions](Direction#KnightDirections "Direction").

A board representation as vector of 64 neighborhoods of each square is suited to serve as an input layer of a [regression network](Neural_Networks "Neural Networks"), whose weights are optimized by [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent), along with training positions previously generated using [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning"). At the lower level the expected probability of winning of the neighborhoods are learned and at the top they are combined based on their product and [entropy](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29).

[](File:ChessNeighbourhood.jpg)
The overall model of the [Morph](Morph "Morph") learner <a id="cite-note-9" href="#cite-ref-9">[9]</a>

## See also

- [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
- [Connected Pawns](Connected_Pawns "Connected Pawns")
- [Distance](Distance "Distance")
- [Mobility](Mobility "Mobility")
- [Morph](Morph "Morph")
- [Square Control](Square_Control "Square Control")
- [Trajectory](Trajectory "Trajectory")

## Publications

## 1970 ...

- [Ron Atkin](Ron_Atkin "Ron Atkin") (**1972**). *Multi-Dimensional Structure in the Game of Chess*. In [International Journal of Man-Machine Studies, Vol. 4](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_4.html)
- [Ron Atkin](Ron_Atkin "Ron Atkin"), [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**1975**). *[A Multi-Dimensional Approach to Positional Chess](http://www.bibsonomy.org/bibtex/2b91106ea980eb48aa505f6b54c130707/dblp)*. [International Journal of Man-Machine Studies, Vol. 7, No. 6](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_7.html)
- [Ron Atkin](Ron_Atkin "Ron Atkin") (**1977**). *Positional Play in Chess by Computer*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1") <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## 1980 ...

- [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1984**). *Computers in Chess: Solving Inexact Search Problems*. Springer-Verlag, New York

[Michael Tsfasman](Michael_Tsfasman "Michael Tsfasman"), [Boris Stilman](Boris_Stilman "Boris Stilman") (**1984**). *The Positional Estimate and Assignment of Priorities*.

- [Yehya Fouda](index.php?title=Yehya_Fouda&action=edit&redlink=1 "Yehya Fouda (page does not exist)") (**1987**). *Computer Chess: A Study of Entropy and Opening Play*. Master's thesis project report. [San Diego State University](https://en.wikipedia.org/wiki/San_Diego_State_University)
- [Danny Kopec](Danny_Kopec "Danny Kopec"), [Ed Northam](Ed_Northam "Ed Northam"), [David Podber](index.php?title=David_Podber&action=edit&redlink=1 "David Podber (page does not exist)"), [Yehya Fouda](index.php?title=Yehya_Fouda&action=edit&redlink=1 "Yehya Fouda (page does not exist)") (**1989**). *The Role of Connectivity in Chess*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_24_C.pdf)

## 1990 ...

- [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
- [Jonathan Allen](index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")

## 2000 ...

- [Boris Stilman](Boris_Stilman "Boris Stilman") (**2000**). *[Linguistic Geometry - From Search to Construction](http://atimopheyev.narod.ru/LG01pdf_in_HTML/LG01_eng.HTML)*. Operations Research/Computer Science Interfaces Series. Springer US, ISBN: 978-0-7923-7738-2, [Acknowledgments](http://atimopheyev.narod.ru/LG01pdf_in_HTML/LG01_eng.HTML#ACKNOWLEDGMENTS)
- [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
- [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")

## 2010 ...

- [Derek Farren](index.php?title=Derek_Farren&action=edit&redlink=1 "Derek Farren (page does not exist)"), [Daniel Templeton](index.php?title=Daniel_Templeton&action=edit&redlink=1 "Daniel Templeton (page does not exist)"), [Meiji Wang](index.php?title=Meiji_Wang&action=edit&redlink=1 "Meiji Wang (page does not exist)") (**2013**). *Analysis of Networks in Chess*. Team 23, [Stanford University](Stanford_University "Stanford University"), [pdf](http://snap.stanford.edu/class/cs224w-2013/projects2013/cs224w-023-final.pdf)

## Forum Posts

- [LCP](http://www.talkchess.com/forum/viewtopic.php?t=55272) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), February 09, 2015 » [Pawn chain](index.php?title=Pawn_chain&action=edit&redlink=1 "Pawn chain (page does not exist)")
- [Pawn defence](http://www.talkchess.com/forum/viewtopic.php?t=55380) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), February 18, 2015

## External Links

- [Connectivity (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Connectivity)
- [Connectivity (graph theory) from Wikipedia](https://en.wikipedia.org/wiki/Connectivity_%28graph_theory%29)
- [Connected space from Wikipedia](https://en.wikipedia.org/wiki/Connected_space)
- [Brain connectivity - Scholarpedia](https://www.scholarpedia.org/article/Brain_connectivity)
- [Entropy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28disambiguation%29)
- [Introduction to entropy from Wikipedia](https://en.wikipedia.org/wiki/Introduction_to_entropy)
- [Simplex from Wikipedia](https://en.wikipedia.org/wiki/Simplex)
- [Simplicial complex from Wikipedia](https://en.wikipedia.org/wiki/Simplicial_complex)
- [Q-analysis from Wikipedia](https://en.wikipedia.org/wiki/Q-analysis)
- [Perrin Grace](https://perringrace.bandcamp.com/) - [Connectivity](https://perringrace.bandcamp.com/track/connectivity) 2013/14, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Knight's graph](http://commons.wikimedia.org/wiki/File:Knight%27s_graph_showing_number_of_possible_moves.svg) showing the number of possible moves from each node, by [R. A. Nonenmacher](https://commons.wikimedia.org/wiki/User:Nonenmac), June 23, 2008, [Knight's tour from Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Danny Kopec](Danny_Kopec "Danny Kopec"), [Ed Northam](Ed_Northam "Ed Northam"), [David Podber](index.php?title=David_Podber&action=edit&redlink=1 "David Podber (page does not exist)"), [Yehya Fouda](index.php?title=Yehya_Fouda&action=edit&redlink=1 "Yehya Fouda (page does not exist)") (**1989**). *The Role of Connectivity in Chess*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_24_C.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1984**). *Computers in Chess: Solving Inexact Search Problems*. Springer-Verlag, New York
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Ron Atkin](Ron_Atkin "Ron Atkin"), [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**1975**). *[A Multi-Dimensional Approach to Positional Chess](http://www.bibsonomy.org/bibtex/2b91106ea980eb48aa505f6b54c130707/dblp)*. [International Journal of Man-Machine Studies, Vol. 7, No. 6](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_7.html)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Derek Farren](index.php?title=Derek_Farren&action=edit&redlink=1 "Derek Farren (page does not exist)"), [Daniel Templeton](index.php?title=Daniel_Templeton&action=edit&redlink=1 "Daniel Templeton (page does not exist)"), [Meiji Wang](index.php?title=Meiji_Wang&action=edit&redlink=1 "Meiji Wang (page does not exist)") (**2013**). *Analysis of Networks in Chess*. Team 23, [Stanford University](Stanford_University "Stanford University"), [pdf](http://snap.stanford.edu/class/cs224w-2013/projects2013/cs224w-023-final.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Derek Farren](index.php?title=Derek_Farren&action=edit&redlink=1 "Derek Farren (page does not exist)"), [Daniel Templeton](index.php?title=Daniel_Templeton&action=edit&redlink=1 "Daniel Templeton (page does not exist)"), [Meiji Wang](index.php?title=Meiji_Wang&action=edit&redlink=1 "Meiji Wang (page does not exist)") (**2013**). *Analysis of Networks in Chess*. Team 23, [Stanford University](Stanford_University "Stanford University"), [pdf](http://snap.stanford.edu/class/cs224w-2013/projects2013/cs224w-023-final.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> Image Fig. 5.3 on pg. 13 from [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/ZgORiY9-gF0J) by [Andy Walker](Andy_Walker "Andy Walker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2000

**[Up one level](Evaluation "Evaluation")**

