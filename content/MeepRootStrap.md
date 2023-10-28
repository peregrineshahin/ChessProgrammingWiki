---
title: MeepRootStrap
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Meep**



[ Strapped woman <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Meep**,  

an experimental chess engine as subject of research on [machine learning](Learning "Learning") techniques and [automated tuning](Automated_Tuning "Automated Tuning"), written by [Joel Veness](Joel_Veness "Joel Veness"), supported by [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), and [Alan Blair](Alan_Blair "Alan Blair"), as elaborated in their 2009 research paper this page is based on <a id="cite-note-2" href="#cite-ref-2">[2]</a> , and in Joel Veness' Ph.D. thesis <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Meep is based on the tournament chess engine [Bodo](Bodo "Bodo"), where the hand-crafted [evaluation function](Evaluation_Function "Evaluation Function") is replaced by a weighted [linear combination](https://en.wikipedia.org/wiki/Linear_combination) of 1812 features. Given a position s, a [feature vector](https://en.wikipedia.org/wiki/Feature_vector) Φ(s) can be constructed from the 1812 numeric values of each feature. The majority of these features are binary. Φ(s) is typically sparse, with approximately 100 features active in any given position. Five wellknown, chess specific feature construction concepts, [material](Material "Material"), [piece square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility") and [king safety](King_Safety "King Safety") were used to generate the 1812 distinct features. In a training mode with various search frameworks, Meep learns from self-play to adjust the weights of its evaluation function towards the value of the deep search. A tournament mode is later used to verify the [strength](Playing_Strength "Playing Strength") of a trained weight configuration. 



### Contents


* [1 BootStrap](#bootstrap)
	+ [1.1 RootStrap](#rootstrap)
	+ [1.2 TreeStrap](#treestrap)
* [2 Results](#results)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






In contrast to [temporal difference methods](Temporal_Difference_Learning "Temporal Difference Learning") such as [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") <a id="cite-note-4" href="#cite-ref-4">[4]</a> as used in [KnightCap](KnightCap "KnightCap"), where the target search is performed at subsequent time-steps, after a real move and response have been played, Meep performs various [bootstrapping](https://en.wikipedia.org/wiki/Bootstrap_aggregating) techniques during training, dubbed **RootStrap** and **TreeStrap**, to adjust the weights at every time-step inside either a [minimax](Minimax "Minimax") or [alpha-beta](Alpha-Beta "Alpha-Beta") search. With the heuristic evaluation function as linear combination of



 [](File:MeepFormula1.jpg) 
where Φ(s) is a vector of features of position s, and θ is a parameter vector specifying the weight of each feature in the linear combination, following backup rules are given, using V as backed up value of the minimax or alpha-beta search (left arrow [theta](https://en.wikipedia.org/wiki/Theta) (←*θ*) denotes the operator that updates the heuristic function towards some target value): 





|  Algorithm
 |  Backup
 |
| --- | --- |
|  TD
 | [MeepFormula2.jpg](File:MeepFormula2.jpg) |
|  TD-Root
 | [MeepFormula3.jpg](File:MeepFormula3.jpg) |
|  TD-Leaf
 | [MeepFormula4.jpg](File:MeepFormula4.jpg) |
|  RootStrap(minimax)
 | [MeepFormula5.jpg](File:MeepFormula5.jpg) |
|  TreeStrap(minimax)
 | [MeepFormula6.jpg](File:MeepFormula6.jpg) |
|  TreeStrap(αβ)
 | [MeepFormula7.jpg](File:MeepFormula7.jpg) |




|  |  |
| --- | --- |
| [TDRootAndLeaf.jpg](File:TDRootAndLeaf.jpg) | [MeepStraps.jpg](File:MeepStraps.jpg) |
|  TD, TD-Root and TD-Leaf backups
 |  RootStrap and TreeStrap(minimax) backups <a id="cite-note-5" href="#cite-ref-5">[5]</a> |


### RootStrap


RootStrap(minimax) or the identical RootStrap(αβ) adjust the weights by [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) <a id="cite-note-6" href="#cite-ref-6">[6]</a> on the [squared error](https://en.wikipedia.org/wiki/Mean_squared_error) between the [static evaluation](Evaluation "Evaluation") and the minimax (or alpha-beta) search value of the [root](Root "Root").



 [](File:MeepFormula8.jpg) 
 [](File:MeepFormula9.jpg) 
where η is a step size constant.



### TreeStrap


TreeStrap(mm) also considers all [interior nodes](Interior_Node "Interior Node") of the [search tree](Search_Tree "Search Tree") for the [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) on the [squared error](https://en.wikipedia.org/wiki/Mean_squared_error). The minimax algorithm used for TreeStrap(mm), keeps the entire tree in [memory](Memory "Memory"). TreeStrap(αβ) applies a generic implementation, that uses only a few enhancements, [transposition table](Transposition_Table "Transposition Table"), [killer](Killer_Heuristic "Killer Heuristic") and [history heuristics](History_Heuristic "History Heuristic"), and [check extensions](Check_Extensions "Check Extensions"). Bounds computed by alpha-beta can be exploited by using a one-sided [loss functions](https://en.wikipedia.org/wiki/Loss_function). If the static evaluation is larger than alpha, then it is reduced towards alpha. If the value from the heuristic evaluation is smaller than beta, then it is increased respectively.



## Results


A tournament of ~16,000 games of 1 minute per game plus 1 second per move [Fischer time](Time_Management#FischerTime "Time Management") between different trained Meep versions and a reference player with randomly initialised weights and arbitrarily assigned rating of 250 was played. Training was previously done by self-play with the same time, using a small opening book to maintain diversity. The target values were determined by at least one ply of full-width search, plus a varying amount of [quiescence search](Quiescence_Search "Quiescence Search"). All Elo values are calculated relative to the reference player, the best performance with 95% confidence intervals given <a id="cite-note-7" href="#cite-ref-7">[7]</a> :





|  Algorithm
 |  Elo
 |
| --- | --- |
|  Untrained
 |  250 ± 63
 |
|  TD-Leaf
 |  1068 ± 36
 |
|  RootStrap(αβ)
 |  1362 ± 59
 |
|  TreeStrap(mm)
 |  1807 ± 32
 |
|  TreeStrap(αβ)
 |  2157 ± 31
 |


## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Bodo](Bodo "Bodo")
* [Duchess](Alan_Blair#Duchess "Alan Blair") (Multi-Player Chess Variant)
* [KnightCap](KnightCap "KnightCap")


## Publications


* [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf) <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Joel Veness](Joel_Veness "Joel Veness") (**2011**). *Approximate Universal Artificial Intelligence and Self-Play Learning for Games*. Ph.D. thesis, [University of New South Wales](https://en.wikipedia.org/wiki/University_of_New_South_Wales), supervisors: [Kee Siong Ng](index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter"), [Alan Blair](Alan_Blair "Alan Blair"), [William Uther](William_Uther "William Uther"), [John Lloyd](index.php?title=John_Lloyd&action=edit&redlink=1 "John Lloyd (page does not exist)"); [pdf](http://jveness.info/publications/veness_phd_thesis_final.pdf)
* [István Szita](Istv%C3%A1n_Szita "István Szita") (**2012**). *[Reinforcement Learning in Games](http://link.springer.com/chapter/10.1007%2F978-3-642-27645-3_17)*. in [Marco Wiering](Marco_Wiering "Marco Wiering"), [Martijn Van Otterlo](http://martijnvanotterlo.nl/) (eds.). *Reinforcement learning: State-of-the-art*. [Adaptation, Learning, and Optimization, Vol. 12](http://link.springer.com/book/10.1007/978-3-642-27645-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


## Forum Posts


* [A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 12, 2010


 [Re: A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667&start=25) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), January 15, 2010
 [Re: A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667&start=27) by [Joel Veness](Joel_Veness "Joel Veness"), [CCC](CCC "CCC"), January 15, 2010
## External Links


* [Bootstrapping from Game Tree Search](http://videolectures.net/nips09_veness_bfg/), video presentation by [Joel Veness](Joel_Veness "Joel Veness"), from [VideoLectures - exchange ideas & share knowledge](http://videolectures.net/), December 2009
* [Meep from Wikipedia](https://en.wikipedia.org/wiki/Meep)
* [Urban Dictionary: meep](http://de.urbandictionary.com/define.php?term=meep)
* [Bootstrapping from Wikipedia](https://en.wikipedia.org/wiki/Bootstrapping)
* [Bootstrapping (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Bootstrapping_%28disambiguation%29)
* [Bootstrap aggregating from Wikipedia](https://en.wikipedia.org/wiki/Bootstrap_aggregating)
* [Strapping from Wikipedia](https://en.wikipedia.org/wiki/Strapping)
* [Strapse from Wikipedia.de](https://de.wikipedia.org/wiki/Strapse) (German)


 [Wearing suspenders or garter belts from Wikipedia](https://en.wikipedia.org/wiki/Garter_%28stockings%29#Garter_belts)
* [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel") - Three Or Two In One, [Lift!](http://www.discogs.com/Volker-Kriegel-Lift/release/726875), 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat: [Eberhard Weber](Category:Eberhard_Weber "Category:Eberhard Weber"), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Stan Sulzmann](https://en.wikipedia.org/wiki/Stan_Sulzmann), [John Taylor](https://en.wikipedia.org/wiki/John_Taylor_%28jazz%29), [Cees See](https://de.wikipedia.org/wiki/Cees_See), [Zbigniew Seifert](Category:Zbigniew_Seifert "Category:Zbigniew Seifert")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Cover of [Bizarre](https://en.wikipedia.org/wiki/Bizarre), Vol. 3 from 1946, depicting a chained woman, and a devil with tailoring tools promising torments due to the wasp-waisted "Fashions of 1946". by [John Willie](https://commons.wikimedia.org/wiki/Category:John_Willie), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Joel Veness](Joel_Veness "Joel Veness") (**2011**). *Approximate Universal Artificial Intelligence and Self-Play Learning for Games*. Ph.D. thesis, [University of New South Wales](https://en.wikipedia.org/wiki/University_of_New_South_Wales), supervisors: [Kee Siong Ng](index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter"), [Alan Blair](Alan_Blair "Alan Blair"), [William Uther](William_Uther "William Uther"), [John Lloyd](index.php?title=John_Lloyd&action=edit&redlink=1 "John Lloyd (page does not exist)"); [pdf](http://jveness.info/publications/veness_phd_thesis_final.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *TDLeaf(lambda): Combining Temporal Difference Learning with Game-Tree Search*. [Australian Journal of Intelligent Information Processing Systems](https://www.chatbots.org/journal/australian_journal_of_intelligent_information_processing_systems/), Vol. 5 No. 1, [arXiv:cs/9901001](http://arxiv.org/abs/cs/9901001)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Images cropped from [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf), Figure 1, pp. 2
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Nabla operator from Wikipedia](https://en.wikipedia.org/wiki/Del)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 12, 2010

**[Up one level](Engines "Engines")**







 
