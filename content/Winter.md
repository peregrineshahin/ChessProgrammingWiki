---
title: Winter
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Winter**



[](http://se.ethz.ch/~meyer/images/zurich/lake.jpg) [Winter](https://en.wikipedia.org/wiki/Winter) in [Zurich](https://en.wikipedia.org/wiki/Z%C3%BCrich), [ETH Zurich](ETH_Zurich "ETH Zurich") view <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Winter**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), written in [C++](Cpp "Cpp"), released on January 08, 2018 under the terms of [GPL Version 3](Free_Software_Foundation#GPL "Free Software Foundation"). Winter is inspired by [machine learning](Learning "Learning") techniques, as applied in [move ordering](Move_Ordering "Move Ordering") and in particular in [evaluation](Evaluation "Evaluation"), and heavily relies on [C++ templates](https://en.wikipedia.org/wiki/Template_(C%2B%2B)) but not on any library aside from [STL](https://en.wikipedia.org/wiki/Standard_Template_Library) as it comes with its own implementations for [statistics](https://en.wikipedia.org/wiki/Statistics) <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Winter started its life in 2016 as a group project at [ETH Zurich](ETH_Zurich "ETH Zurich") in a course on parallel computing along with Jonas Kuratli and Jonathan Maurer - the current release with Jonathan Rosenthal as sole author has removed the parallel portion of the code <a id="cite-note-4" href="#cite-ref-4">[4]</a>. It started to play on-line at [HGM's](Harm_Geert_Muller "Harm Geert Muller") [Online Engine Blitz Tourneys](index.php?title=Online_Engine_Blitz_Tourneys&action=edit&redlink=1 "Online Engine Blitz Tourneys (page does not exist)") in April 2017 <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Contents


* [1 Selected Features](#selected-features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 Forum Posts](#forum-posts)
	+ [2.1 2017 ...](#2017-...)
	+ [2.2 2020 ...](#2020-...)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc-2)
* [4 References](#references)






<a id="cite-note-6" href="#cite-ref-6">[6]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [8x8 Board](8x8_Board "8x8 Board")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")


 [BMI2 - PEXT Bitboards](BMI2#PEXTBitboards "BMI2")
### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP") (Winter 0.3)
* [Fail-Hard](Fail-Hard "Fail-Hard") [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta") [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering") is based on the linear part of a [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning") [classifier](https://en.wikipedia.org/wiki/Statistical_classification) aka [cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis)
	+ The classifier is trained via [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") to predict whether a [move](Moves "Moves") will return [beta](Beta "Beta")
	+ Classifier considers [TT move](Hash_Move "Hash Move"), [killers](Killer_Move "Killer Move"), [move type](Moves#Type "Moves"), [from square](Origin_Square "Origin Square"), [target square](Target_Square "Target Square"), [capture target](Captures "Captures"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), target square of last move, [check](Check "Check") and changes between forcing and unforcing moves (a capture is more likely after another capture)
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic") (Winter 0.3)
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
	+ [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Evaluation](Evaluation "Evaluation")


* Non standard approach relied on a [mixture model](https://en.wikipedia.org/wiki/Mixture_model) <a id="cite-note-7" href="#cite-ref-7">[7]</a>, and since Winter **0.3** on [Fuzzy C-Means](https://en.wikipedia.org/wiki/Fuzzy_clustering#Fuzzy_C-means_clustering), a more direct generalization of a [tapered eval](Tapered_Eval "Tapered Eval") with disjoint phases aka clusters <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>
	+ Assumes [positions](Chess_Position "Chess Position") encountered in search come from some set of [k-means clusters](https://en.wikipedia.org/wiki/K-means_clustering) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
	+ Model is trained via [EM algorithm](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm) <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> either on [database games](Databases "Databases") or positions sampled from search
	+ For each cluster, a separate evaluation function is trained. When the evaluation function is called the relative probability a position stems from each cluster is estimated, the evaluation functions are computed and the final score is returned as the weighted average - a generalization of [tapered eval](Tapered_Eval "Tapered Eval") with [game phases](Game_Phases "Game Phases") <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* Parameter weights are trained via a mixture of [reinforcement](Reinforcement_Learning "Reinforcement Learning") ([temporal difference](Temporal_Difference_Learning "Temporal Difference Learning")) learning and [supervised learning](Supervised_Learning "Supervised Learning")
	+ Minimizing the [cross entropy](https://en.wikipedia.org/wiki/Cross_entropy) loss of a [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning") model for each phase
	+ Training converges fast due to [linear model](https://en.wikipedia.org/wiki/Linear_model) at the heart
* As of **Winter 0.6.2**, the evaluation function relies on a [neural network](Neural_Networks "Neural Networks") with two main parts. The first part is a non-standard [convolutional neural network](Neural_Networks#Convolutional "Neural Networks") which uses sparsity similarly to [NNUE](NNUE "NNUE"). This convolutional network is used to calculate [pawn structure](Pawn_Structure "Pawn Structure") features, so the output can be reused very often as it gets stored in a separate [hash table](Pawn_Hash_Table "Pawn Hash Table") with a high hitrate. The second part is a fully connected network which has as input the output of the convolutional network as well as a set of handcrafted features standard to classical engines, mostly a subset of the features from before neural networks were added to Winter <a id="cite-note-14" href="#cite-ref-14">[14]</a>


### Misc


* [Perft](Perft "Perft")
* Print pretty [Unicode](Pieces#Unicode "Pieces") [chess boards](Chessboard "Chessboard")


## Forum Posts


### 2017 ...


* [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum/viewtopic.php?t=65466&start=4) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), October 16, 2017 » [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Winter Released](http://www.talkchess.com/forum/viewtopic.php?t=66266) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 08, 2018


 [Re: Winter Released](http://www.talkchess.com/forum/viewtopic.php?t=66266&start=7) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 09, 2018
 [Windows version released](http://www.talkchess.com/forum/viewtopic.php?t=66266&start=8) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 23, 2018
* [Winter 0.2 Release Overview and Select Games](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68266) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), August 20, 2018
* [Winter 0.3 Release Overview and Select Games](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69288) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), December 16, 2018 » [TCEC Season 14](TCEC_Season_14 "TCEC Season 14")
* [Winter NN Training Script](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72284) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), November 09, 2019


### 2020 ...


* [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 24, 2020 » [NNUE](NNUE "NNUE")
* [Winter](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75301) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), October 05, 2020


 [Re: Winter](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75301&start=14) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 09, 2021
## External Links


### Chess Engine


* [GitHub - rosenthj/Winter: UCI Chess Engine](https://github.com/rosenthj/Winter)
* [Winter](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Winter&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [Winter from Wikipedia](https://en.wikipedia.org/wiki/Winter)
* [Winter - Wiktionary](https://en.wiktionary.org/wiki/Winter)
* [winter - Wiktionary](https://en.wiktionary.org/wiki/winter)
* [Winter (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Winter_(disambiguation))
* [Summer and Winter Schools](https://www.ethz.ch/en/the-eth-zurich/sustainability/education/summer-and-winter-schools.html) | [ETH Zurich](ETH_Zurich "ETH Zurich")
* [Wintel from Wikipedia](https://en.wikipedia.org/wiki/Wintel)
* [AI winter from Wikipedia](https://en.wikipedia.org/wiki/AI_winter)
* [Winter (surname) from Wikipedia](https://en.wikipedia.org/wiki/Winter_(surname))
* [Edward Winter (chess historian) from Wikipedia](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
* [Johnny Winter](Category:Johnny_Winter "Category:Johnny Winter") - Winter Ballade, [ina.fr](https://en.wikipedia.org/wiki/Institut_national_de_l%27audiovisuel) 1970, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Tommy Shannon](Category:Tommy_Shannon "Category:Tommy Shannon") on bass and [Uncle John Turner](http://yeech.altervista.org/Band/winter_band_john_turner.html) on drums
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image clipped from [Winter views from our floor](http://se.ethz.ch/~meyer/) by [Bertrand Meyer](Mathematician#BMeyer "Mathematician"), [ETH Zurich](ETH_Zurich "ETH Zurich"), [Gray moment](http://se.ethz.ch/~meyer/images/zurich/lake.jpg) with [Zentralbibliothek](https://en.wikipedia.org/wiki/Zentralbibliothek_Z%C3%BCrich) and [Predigerkirche](https://en.wikipedia.org/wiki/Predigerkirche_Z%C3%BCrich) in the foreground, [Lake Zurich](https://en.wikipedia.org/wiki/Lake_Zurich), [Grossmünster](https://en.wikipedia.org/wiki/Grossm%C3%BCnster), [Fraumünster](https://en.wikipedia.org/wiki/Fraum%C3%BCnster) and [St. Peter](https://en.wikipedia.org/wiki/St._Peter,_Z%C3%BCrich) behind, in the background foothill of [Uetliberg](https://en.wikipedia.org/wiki/Uetliberg), from [Bertrand Meyer's ETH home page](http://se.ethz.ch/~meyer/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Winter/statistics.h at master · rosenthj/Winter · GitHub](https://github.com/rosenthj/Winter/blob/master/src/learning/statistics.h)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Winter/linear\_algebra.h at master · rosenthj/Winter · GitHub](https://github.com/rosenthj/Winter/blob/master/src/learning/linear_algebra.h)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Winter Released](http://www.talkchess.com/forum/viewtopic.php?t=66266) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 08, 2018
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: On-line engine blitz tourney April](http://www.talkchess.com/forum/viewtopic.php?t=63777&start=9) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 22, 2017
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> based on [Winter Released](http://www.talkchess.com/forum/viewtopic.php?t=66266) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 08, 2018
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Winter Released](http://www.talkchess.com/forum/viewtopic.php?t=66266&start=7) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), January 09, 2018
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Winter 0.3 Release Overview and Select Games](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69288) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), December 16, 2018
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [James C. Bezdek](Mathematician#JCBezdek "Mathematician"), [Robert Ehrlich](http://www.legacy.com/obituaries/saltlaketribune/obituary.aspx?n=robert-ehrlich&pid=189574728), [William Full](https://www.researchgate.net/profile/William_Full) (**1984**). *FCM: The fuzzy c-means clustering algorithm*. [Computers & Geosciences](https://www.journals.elsevier.com/computers-and-geosciences), Vol. 10, Nos. 2-3, [pdf](https://pdfs.semanticscholar.org/64a8/77d135db3acbc23c295367927176f332595f.pdf)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [K Means](http://stanford.edu/~cpiech/cs221/handouts/kmeans.html) by [Chris Piech](https://web.stanford.edu/~cpiech/bio/index.html)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [The EM Algorithm for Gaussian Mixtures - Probabilistic Learning: Theory and Algorithms, CS 274A](http://www.ics.uci.edu/~smyth/courses/cs274/notes/EMnotes.pdf) (pdf) [University of California, Irvine](https://en.wikipedia.org/wiki/University_of_California,_Irvine)
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Mixture Models & EM algorithm Lecture 21](http://people.csail.mit.edu/dsontag/courses/ml12/slides/lecture21.pdf) (pdf) by [David Sontag](https://people.csail.mit.edu/dsontag/), [New York University](https://en.wikipedia.org/wiki/New_York_University)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum/viewtopic.php?t=65466&start=4) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), October 16, 2017
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 24, 2020

**[Up one Level](Engines "Engines")**







 
