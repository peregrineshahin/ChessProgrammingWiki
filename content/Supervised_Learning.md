---
title: Supervised Learning
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* Supervised Learning**


**Supervised Learning**, (SL)  

is learning from examples provided by a knowledgable external [supervisor](https://en.wikipedia.org/wiki/Supervisor). 
In machine learning, supervised learning is a technique for deducing a function from [training data](https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets). The training data consist of pairs of input objects and desired outputs. After parameter adjustment and learning, the performance of the resulting function should be measured on a test set that is separate from the training set <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 



## SL in Chess


In computer games and chess, supervised learning techniques were used in [automated tuning](Automated_Tuning "Automated Tuning") or to train [neural network](Neural_Networks "Neural Networks") game and chess programs. Input objects are [chess positions](Chess_Position "Chess Position"). The desired output is either the supervisor's move choice in that position ([move adaption](Automated_Tuning#MoveAdaption "Automated Tuning")), or a [score](Score "Score") provided by an [oracle](Oracle "Oracle") ([value adaption](Automated_Tuning#ValueAdaption "Automated Tuning")).



### Move Adaption


[Move adaption](Automated_Tuning#MoveAdaption "Automated Tuning") can be applied by [linear regression](Automated_Tuning#LinearRegression "Automated Tuning") to minimize a [cost function](https://en.wikipedia.org/wiki/Loss_function) considering the rank-number of the desired move in a [move list](Move_List "Move List") ordered by score <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Value Adaption


One common idea to provide an [oracle](Oracle "Oracle") for supervised [value adaption](Automated_Tuning#ValueAdaption "Automated Tuning") is to use the win/draw/loss outcome from finished games 
for all training positions selected from that game. Discrete {-1, 0, +1} or {0, ½, 1} desired values are the domain of [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") and require the
evaluation scores mapped from [pawn advantage](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") to appropriate winning probabilities using the [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) 
to calculate a [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) of the cost function to minimize, as demonstrated by [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method").



## See also


* [Supervised Learning](Automated_Tuning#SupervisedLearning "Automated Tuning") in [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Book Learning](Book_Learning "Book Learning")
* [Chessmaps Heuristic](Chessmaps_Heuristic "Chessmaps Heuristic")
* [CHREST](CHREST "CHREST")
* [Deep Learning](Deep_Learning "Deep Learning")
* [Neural Networks](Neural_Networks "Neural Networks")
* [Planning](Planning "Planning")
* [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")


## Selected Publications


### 1960 ....


* [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://researcher.watson.ibm.com/researcher/files/us-beygel/samuel-checkers.pdf)


### 1980 ...


* [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1982**). *A Learning Chess Program.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
* [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *Evaluation-Function Factors*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/evaluation.pdf)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Frank Wilczek](https://en.wikipedia.org/wiki/Frank_Wilczek) (**1987**). *[Supervised Learning of Probability Distributions by Neural Networks](http://papers.nips.cc/paper/3-supervised-learning-of-probability-distributions-by-neural-networks)*. [NIPS 1987](http://papers.nips.cc/book/neural-information-processing-systems-1987)
* [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1989**). *Weight Assessment in Evaluation Functions*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")


### 1990 ...


* [Michèle Sebag](Mich%C3%A8le_Sebag "Michèle Sebag") (**1990**). *A symbolic-numerical approach for supervised learning from examples and rules*. Ph.D. thesis, [Paris Dauphine University](https://en.wikipedia.org/wiki/Paris_Dauphine_University)
* [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Andreas Nowatzyk](Andreas_Nowatzyk "Andreas Nowatzyk") (**1990**). *[A Grandmaster Chess Machine](http://www.disi.unige.it/person/DelzannoG/AI2/hsu.html)*. [Scientific American](Scientific_American "Scientific American"), Vol. 263, No. 4
* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1997**). *Evaluation Tuning for Computer Chess: Linear Discriminant Methods*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")


### 2000 ...


* [Michael Buro](Michael_Buro "Michael Buro") (**2002**). *Improving Mini-max Search by Supervised Learning.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 134, No. 1, [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/logaij.pdf)
* [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [Michael Buro](Michael_Buro "Michael Buro"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2005**). *Tuning Evaluation Functions by Maximizing Concordance*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 349, No. 2, [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/tcs-learn.pdf)
* [Amos Storkey](Amos_Storkey "Amos Storkey"), [Masashi Sugiyama](https://www.k.u-tokyo.ac.jp/pros-e/person/masashi_sugiyama/masashi_sugiyama.htm) (**2006**). *[Mixture Regression for Covariate Shift](http://papers.neurips.cc/paper/3019-mixture-regression-for-covariate-shift)*. [NIPS 2006](https://dblp.uni-trier.de/db/conf/nips/nips2006.html)
* [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *Genetic Algorithms for Mentor-Assisted Evaluation Function Optimization*. [GECCO '08](http://www.sigevo.org/gecco-2008/), [arXiv:1711.06839](https://arxiv.org/abs/1711.06839)
* [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2009**). *Simulating Human Grandmasters: Evolution and Coevolution of Evaluation Functions*. [GECCO '09](http://www.sigevo.org/gecco-2009/), [arXiv:1711.06840](https://arxiv.org/abs/1711.06840)


### 2010 ...


* [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter") (**2011**). *No Free Lunch versus Occam's Razor in Supervised Learning*. [Solomonoff](https://en.wikipedia.org/wiki/Ray_Solomonoff) Memorial, [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), [Springer](https://en.wikipedia.org/wiki/Springer-Verlag), [arXiv:1111.3846](https://arxiv.org/abs/1111.3846) <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ching-Hua Kuo](Ching-Hua_Kuo "Ching-Hua Kuo"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)") (**2013**). *A Supervised Learning Method for Chinese Chess Programs*. [JSAI2013](http://2013.conf.ai-gakkai.or.jp/english-info)
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf)
* [Christopher Clark](Christopher_Clark "Christopher Clark"), [Amos Storkey](Amos_Storkey "Amos Storkey") (**2014**). *Teaching Deep Convolutional Neural Networks to Play Go*. [arXiv:1412.3409](http://arxiv.org/abs/1412.3409)
* [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Tinghan Wei](index.php?title=Tinghan_Wei&action=edit&redlink=1 "Tinghan Wei (page does not exist)") (**2018**). *Comparison Training for Computer Chinese Chess*. [arXiv:1801.07411](https://arxiv.org/abs/1801.07411)


### 2020 ...


* [Johannes Czech](Johannes_Czech "Johannes Czech"), [Moritz Willig](Moritz_Willig "Moritz Willig"), [Alena Beyer](Alena_Beyer "Alena Beyer"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2020**). *[Learning to Play the Chess Variant Crazyhouse Above World Champion Level With Deep Neural Networks and Human Data](https://www.frontiersin.org/articles/10.3389/frai.2020.00024/full)*. [Frontiers in Artificial Intelligence](https://www.frontiersin.org/journals/artificial-intelligence#)  » [CrazyAra](CrazyAra "CrazyAra")


## Forum Posts


* [Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009 » [Gaviota](Gaviota "Gaviota")
* [Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=10) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 08, 2014
* [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=26) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [SL vs RL](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70611) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), April 28, 2019


## External Links


* [Supervised learning from Wikipedia](https://en.wikipedia.org/wiki/Supervised_learning)
* [Category: Supervised learning - Scholarpedia](http://www.scholarpedia.org/article/Category:Supervised_learning)
* [Boosting (machine learning) from Wikipedia](https://en.wikipedia.org/wiki/Boosting_%28machine_learning%29)
* [Computational learning theory from Wikipedia](https://en.wikipedia.org/wiki/Computational_learning_theory)
* [Support vector machine from Wikipedia](https://en.wikipedia.org/wiki/Support_vector_machine)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Supervised learning from Wikipedia](https://en.wikipedia.org/wiki/Supervised_learning)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> A data flow diagram shows the machine learning process in summary, by [EpochFail](https://en.wikipedia.org/wiki/User:EpochFail), November 15, 2015, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *Evaluation-Function Factors*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/evaluation.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [No free lunch in search and optimization - Wikipedia](https://en.wikipedia.org/wiki/No_free_lunch_in_search_and_optimization)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Occam's razor from Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor)

**[Up one Level](Learning "Learning")**







 
