---
title: Morph
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Morph**



 [](http://www1.ucsc.edu/oncampus/currents/97-05-05/levinson.photo.htm) [Robert Levinson](Robert_Levinson "Robert Levinson") and Morph <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Morph** <a id="cite-note-2" href="#cite-ref-2">[2]</a>,  

a research chess program started by [Robert Levinson](Robert_Levinson "Robert Levinson") in 1989 at [University of California, Santa Cruz](University_of_California,_Santa_Cruz "University of California, Santa Cruz") with the goal to create an autonomous chess learner, knowing only the rules of chess and then evolve from game to game using heuristics derived from [machine learning](Learning "Learning") algorithms such as [pattern recognition](Pattern_Recognition "Pattern Recognition"), [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") and [neural networks](Neural_Networks "Neural Networks"). It uses a graph representation of chess positions and [pattern-oriented](https://en.wikipedia.org/wiki/Pattern-oriented_modeling) databases in conjunction with [minimax](Minimax "Minimax") [search](Search "Search"). Research has been done by dedicated undergraduate volunteers at UCSC, most computer science students with interests in chess and [Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Morph I/II


The project began with the goal of developing a chess program that conformed more to [cognitive models](Cognition "Cognition") of human chess playing than conventional chess programs. The key idea was to make the program adaptive and pattern-oriented, limited to searching only one [ply](Ply "Ply") and to acquiering its own chess knowledge through experience - assisted by a human-designed graph-theoretic representation language for chess patterns. 


Morph stores its experience as <pattern, weight> pairs (pws). Morph's pattern are directed graphs where the nodes represent pieces and squares [sorrounding the king](King_Pattern "King Pattern") and the edges represent ([X-ray](X-ray_Attacks_(Bitboards) "X-ray Attacks (Bitboards)")) attacks or defenses. To [evaluate](Evaluation "Evaluation") a position, Morph finds which graphs in the database match that position and then combines the weights associated with each graph. At the end of each game, Morph uses [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") to adjust the weights of the pattern that match each position in the game. In addition, Morph creates new patterns that should enable it to determine more accurately the value of that or similar positions should it occur in the future. 


The utility of pattern can be measured by the variance in its sequence of weights, which is maintained incrementally by storing the number of updates and accumulating the absolute value of their weight changes, used to decide whether patterns are deleted. After training and improving in about 3000 to 4000 games against [GNU Chess](GNU_Chess "GNU Chess"), Morph **I** was able to defeat human chess novices while searching just one ply <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Morph **II** is a generalization of Morph's learning and pattern representation to be applicable to most two-player [games](Games "Games") and search problems given the rules of those domains. 



### Morph III/IV


The Morph III architecture allows for any reasonable number of knowledge sources to be used, a concept similar to that of advisors in the *Hoyle* system by [Susan L. Epstein](Susan_L._Epstein "Susan L. Epstein") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Compared to Morph I which had a bag of pattern, Morph's representation shifted towards learning internal weights. Morph **III** and Morph **IV** used [nearest neighbor](https://en.wikipedia.org/wiki/Nearest_neighbor_search) and [decision trees](https://en.wikipedia.org/wiki/Decision_tree) to divide positions into [equivalence classes](https://en.wikipedia.org/wiki/Equivalence_class) and query them on-line in logarithmic time. However these approaches require a large amount of training data to achieve reasonable levels of play. 



### Morph V


Latest Morph, as mentioned in 2004 <a id="cite-note-7" href="#cite-ref-7">[7]</a>, uses a unique chess board representation called [Chess Neighborhood](Connectivity#ChessNeighborhood "Connectivity") <a id="cite-note-8" href="#cite-ref-8">[8]</a> and uses a [regression network](Neural_Networks "Neural Networks") to learn nonlinear combinations of the individual values of pieces that make up a piece neighborhood to arrive at a single value for the entire neighborhood. A vector of 64 neighborhoods of each square is suited to serve as an input layer of the regression network, whose weights are optimized by [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent), along with training positions previously generated using [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning"). At the lower level the expected probability of winning of the neighborhoods are learned and at the top they are combined based on their product and [entropy](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29).



 [](File:ChessNeighbourhood.jpg) 
The overall model of the Morph learner <a id="cite-note-9" href="#cite-ref-9">[9]</a>



## See also


* [Chess Engines with Neural Networks](Neural_Networks#engines "Neural Networks")
* [Learning Chess Programs](Learning#Programs "Learning")
* [Morphy](Morphy "Morphy")


## Publications


### 1989


* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1989**). *A Self-Learning, Pattern-Oriented Chess Program*. [WCCC 1989 - Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1989**). *A Self-Learning, Pattern-Oriented Chess Program*. [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")


### 1990 ...


* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Brian Beach](index.php?title=Brian_Beach&action=edit&redlink=1 "Brian Beach (page does not exist)"), [Richard Snyder](Richard_Snyder "Richard Snyder"), [Tal Dayan](index.php?title=Tal_Dayan&action=edit&redlink=1 "Tal Dayan (page does not exist)"), [Kirack Sohn](index.php?title=Kirack_Sohn&action=edit&redlink=1 "Kirack Sohn (page does not exist)") (**1990**). *Adaptive-predictive game-playing programs*. [abstract](http://portal.acm.org/citation.cfm?id=902787&jmp=abstract&coll=GUIDE&dl=GUIDE&CFID=78059366&CFTOKEN=89563212#abstract)
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1991**). *A Self-Organizing Pattern Retrieval System and its Applications*. International Journal of Intelligent Systems, Vol. 6, pp. 717-738. ISSN 0884-8173.
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1991**). *Adaptive Pattern-Oriented Chess*. Proceedings of the 8th International Workshop on Machine Learning (eds. L. Birnbaum and G. Collins), pp. 85-89. Morgan Kaufmann, San Mateo, CA. Also published in: Proceedings of the Ninth National Conference on Artificial Intelligence AAAI-91, pp. 601-606. AAAI Press, MIT Press, Boston, MA. [pdf](http://www.aaai.org/Papers/AAAI/1991/AAAI91-094.pdf)
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [John Amenta](John_Amenta "John Amenta") (**1993**). *MORPH, An Experience-Based Adaptive Chess System*. [ICCA Journal, Vol. 16, No. 1](ICGA_Journal#16_1 "ICGA Journal") <a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") » [WCCC 1992 - Workshop](WCCC_1992#Workshop "WCCC 1992")
* [Jeffrey Gould](index.php?title=Jeffrey_Gould&action=edit&redlink=1 "Jeffrey Gould (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**1994**). *Experience-Based Adaptive Search*. Machine Learning: A Multi-Strategy Approach (eds. R. Michalski and G. Tecuci), Vol. 4
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)") (**1994**). *A Pattern-Weight Formulation of Search Knowledge*. UCSC-CRL-94-10, [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.35.1027)
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1994**). *[Morph II: A Universal Agent: Progess Report and Proposal](https://www.soe.ucsc.edu/research/technical-reports/UCSC-CRL-94-22)*. UCSC-CRL-94-22
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1996**). *[General Game-Playing and Reinforcement Learning](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-8640.1996.tb00257.x/abstract)*. [Computational Intelligence, Vol. 12](http://dblp.uni-trier.de/db/journals/ci/ci12.html#PellEL96), No. 1
* [Jonathan Allen](index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")


### 2000 ...


* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *Pattern-Level Temporal Difference-Learning, Data Fusion and Chess*. In Sensor Fusion: Architecture, Algorithms, and Applications IV. Orlando, Florida, April 2000
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
* [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")


## Forum Posts


* [Computer learning chess from scratch? Morph?](https://groups.google.com/d/msg/rec.games.chess.computer/HD_Wk587W7U/4LNWdcyeplEJ) by John Michael Sauder, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1996
* [morph(C) on ICC](https://www.stmintz.com/ccc/index.php?id=72802) by Jeff Anderson, [CCC](CCC "CCC"), October 11, 1999


 [Re: morph(C) on ICC](https://www.stmintz.com/ccc/index.php?id=72897) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 12, 1999
 [morph(C) -- can this really work ?](https://www.stmintz.com/ccc/index.php?id=73074) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), October 13, 1999
* [Morph lll](https://www.stmintz.com/ccc/index.php?id=324534) by K. Burcham, [CCC](CCC "CCC"), October 29, 2003
* [Re: learning](http://www.talkchess.com/forum/viewtopic.php?start=8&t=19381) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCC](CCC "CCC"), February 03, 2008


 [Re: learning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=172566) by [Shivkumar Shivaji](index.php?title=Shivkumar_Shivaji&action=edit&redlink=1 "Shivkumar Shivaji (page does not exist)"), [CCC](CCC "CCC"), February 03, 2008
## External Links


### Chess Program


* [the Morph project](http://satirist.org/learn-game/projects/morph.html) by [Jay Scott](Jay_Scott "Jay Scott")
* [Finger morph2](http://www6.chessclub.com/activities/finger.php?handle=morph2) @ [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")
* ["Deep Blue" inspires deep thinking about artificial intelligence by computer scientist](https://www.sciencedaily.com/releases/1997/05/970501194114.htm) by [Robert Irion](https://scicom.ucsc.edu/faculty/), [University of California, Santa Cruz](University_of_California,_Santa_Cruz "University of California, Santa Cruz"), May 5, 1997 <a id="cite-note-11" href="#cite-ref-11">[11]</a> » [Deep Blue](Deep_Blue "Deep Blue")


### Misc


* [morph - Wiktionary](https://en.wiktionary.org/wiki/morph)
* [-morph - Wiktionary](https://en.wiktionary.org/wiki/-morph)
* [Word Root Of The Day: morph | Membean](http://membean.com/wrotds/morph-shape)
* [Morph from Wikipedia](https://en.wikipedia.org/wiki/Morph)
* [Muller's morphs from Wikipedia](https://en.wikipedia.org/wiki/Muller's_morphs) (amorph, hypomorph, hypermorph, antimorph and neomorph)
* [Morpheme from Wikipedia](https://en.wikipedia.org/wiki/Morpheme)
* [Morphine from Wikipedia](https://en.wikipedia.org/wiki/Morphine)
* [Morphing from Wikipedia](https://en.wikipedia.org/wiki/Morphing)
* [Morphism from Wikipedia](https://en.wikipedia.org/wiki/Morphism)


 [Morphism of algebraic varieties from Wikipedia](https://en.wikipedia.org/wiki/Morphism_of_algebraic_varieties)
 [Homomorphism from Wikipedia](https://en.wikipedia.org/wiki/Homomorphism)
 [Isomorphism from Wikipedia](https://en.wikipedia.org/wiki/Isomorphism)
 [Isomorph from Wikipedia](https://en.wikipedia.org/wiki/Isomorph)
* [Morphology from Wikipedia](https://en.wikipedia.org/wiki/Morphology)


 [Galaxy morphological classification from Wikipedia](https://en.wikipedia.org/wiki/Galaxy_morphological_classification)
 [Mathematical morphology from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_morphology)
* [Metamorphosis from Wikipedia](https://en.wikipedia.org/wiki/Metamorphosis)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a>  [Robert Levinson photo: 05-05-97](http://www1.ucsc.edu/oncampus/currents/97-05-05/levinson.photo.htm) by Don Harris, UCSC Photo Services, in ["Deep Blue" inspires deep thinking about artificial intelligence by computer scientist](http://www1.ucsc.edu/oncampus/currents/97-05-05/chess.htm) by [Robert Irion](http://scicom.ucsc.edu/faculty/), [CURRENTS, University of California, Santa Cruz](http://www1.ucsc.edu/oncampus/currents/97-05-05/index.html), May 5, 1997
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> *The name "Morph" comes from the [Greek](https://en.wikipedia.org/wiki/Greek_language) "morph" meaning [form](https://en.wikipedia.org/wiki/Form) and the chess great, [Paul Morphy](https://en.wikipedia.org/wiki/Paul_Morphy)*, footnote 1 in [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1991**). *Adaptive Pattern-Oriented Chess*. Proceedings of the 8th International Workshop on Machine Learning (eds. L. Birnbaum and G. Collins), pp. 85-89. Morgan Kaufmann, San Mateo, CA. Also published in: Proceedings of the Ninth National Conference on Artificial Intelligence AAAI-91, pp. 601-606. AAAI Press, MIT Press, Boston, MA. [pdf](http://www.aaai.org/Papers/AAAI/1991/AAAI91-094.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [John Amenta](John_Amenta "John Amenta") (**1993**). *MORPH, An Experience-Based Adaptive Chess System*. [ICCA Journal, Vol. 16, No. 1](ICGA_Journal#16_1 "ICGA Journal")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Jonathan Allen](index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Susan L. Epstein](Susan_L._Epstein "Susan L. Epstein") (**1992**). *[Prior Knowledge Strengthens Learning to Control Search in Weak Theory Domains](http://onlinelibrary.wiley.com/doi/10.1002/int.4550070606/abstract)*. [International Journal of Intelligent Systems](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-INT.html), Vol. 7, No. 6
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> Image Fig. 5.3 on pg. 13 from [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> reprinted in [The 23rd ACM International Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cc6e9) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1993_23rd_ACM_ICCC/1993%20ICCC.062303066.sm.pdf)
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Jeff Wilkinson](index.php?title=Jeff_Wilkinson&action=edit&redlink=1 "Jeff Wilkinson (page does not exist)") (**1997**). *[Deep Blue is Still an Infant](https://www.semanticscholar.org/paper/Deep-Blue-is-Still-an-Infant-Levinson-Wilkinson/3ce74263ef7b5d04fdf709b2dd3a519d780ae47f)*. [AAAI](AAAI "AAAI"), Technical Report WS-97-04

**[Up one Level](Engines "Engines")**







 
