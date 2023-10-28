---
title: UCT
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") \* UCT**


**UCT** (**U**pper **C**onfidence bounds applied to **T**rees),  

a popular [algorithm](Algorithms "Algorithms") that deals with the flaw of Monte-Carlo Tree Search, when a program may favor a losing move with only one or a few forced refutations, but due to the vast majority of other moves provides a better random playout score than other, better moves. UCT was introduced by [Levente Kocsis](Levente_Kocsis "Levente Kocsis") and [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") in 2006 [[1]](#cite_note-1), which accelerated the Monte-Carlo revolution in computer [Go](Go "Go") [[2]](#cite_note-2) and games difficult to [evaluate](Evaluation "Evaluation") statically. If given infinite time and [memory](Memory "Memory"), UCT theoretically converges to [Minimax](Minimax "Minimax").



### Contents


* [1 Selection](#Selection)
	+ [1.1 RAVE](#RAVE)
	+ [1.2 PUCT](#PUCT)
* [2 Quotes](#Quotes)
	+ [2.1 Gian-Carlo Pascutto](#Gian-Carlo_Pascutto)
	+ [2.2 Raghuram Ramanujan et al.](#Raghuram_Ramanujan_et_al.)
* [3 See also](#See_also)
* [4 Publications](#Publications)
	+ [4.1 2000 ...](#2000_...)
	+ [4.2 2005 ...](#2005_...)
	+ [4.3 2010 ...](#2010_...)
	+ [4.4 2015 ...](#2015_...)
* [5 Forum Posts](#Forum_Posts)
	+ [5.1 2010 ...](#2010_..._2)
	+ [5.2 2015 ...](#2015_..._2)
	+ [5.3 2020 ...](#2020_...)
* [6 External Links](#External_Links)
* [7 References](#References)






In UCT, upper [confidence bounds](https://en.wikipedia.org/wiki/Confidence_interval) (UCB1) guide the selection of a node [[3]](#cite_note-3), treating selection as a [multi-armed bandit problem](https://en.wikipedia.org/wiki/Multi-armed_bandit), where the crucial tradeoff the [gambler](https://en.wikipedia.org/wiki/Gambling) faces at each trial is between [exploration and exploitation](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation) - [exploitation](https://en.wikipedia.org/wiki/Exploitation_%28disambiguation%29) of the [slot machine](https://en.wikipedia.org/wiki/Slot_machine) that has the highest expected payoff and [exploration](https://en.wikipedia.org/wiki/Exploration) to get more information about the expected payoffs of the other machines. Child node j is selected which maximizes the UCT Evaluation: 



 [](File:UCTFormula.jpg) 
where:



* Xj is the [win ratio](Match_Statistics#ratio "Match Statistics") of the child
* n is the number of times the parent has been visited
* nj is the number of times the child has been visited
* C is a constant to adjust the amount of exploration and incorporates the sqrt(2) from the UCB1 formula


The first component of the UCB1 formula above corresponds to exploitation, as it is high for moves with high average win ratio. The second component corresponds to exploration, since it is high for moves with few simulations. 



### RAVE


Most contemporary implementations of MCTS are based on some variant of UCT [[4]](#cite_note-4). Modifications have been proposed, with the aim of shortening the time to find good moves. They can be divided into improvements based on expert knowledge and into domain-independent improvements in the playouts, and in building the tree in modifying the exploitation part of the UCB1 formula, for instance in [Rapid Action Value Estimation](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Improvements) (**RAVE**) [[5]](#cite_note-5) considering [transpositions](Transposition "Transposition"). 



### PUCT


[Chris Rosin's](Christopher_D._Rosin "Christopher D. Rosin") [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin") modifies the original UCB1 multi-armed bandit policy by approximately predicting good arms at the start of a sequence of multi-armed bandit trials ('Predictor' + UCB = PUCB) [[6]](#cite_note-6). A variation of PUCT was used in the [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") and [AlphaZero](AlphaZero "AlphaZero") projects [[7]](#cite_note-7) , and subsequently also in [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)") and [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") [[8]](#cite_note-8).


  




## Quotes


### Gian-Carlo Pascutto


Quote by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") in 2010 [[9]](#cite_note-9):




```
There is no significant difference between an [alpha-beta search](Alpha-Beta "Alpha-Beta") with heavy [LMR](Late_Move_Reductions "Late Move Reductions")  and a [static evaluator](Evaluation "Evaluation") (current state of the art in [chess](Chess "Chess")) and an UCT searcher with a small exploration constant that does playouts (state of the art in [go](Go "Go")).

```


```
The shape of the [tree](Search_Tree "Search Tree") they search is very similar. The main breakthrough in Go the last few years was how to backup an uncertain Monte Carlo score. This was solved. For chess this same problem was solved around the time [quiescent search](Quiescence_Search "Quiescence Search") was developed.

```


```
Both are producing strong programs and we've proven for both the methods that they scale in strength as hardware speed goes up.

```


```
So I would say that we've successfully adopted the simple, brute force methods for chess to Go and they already work without increases in computer speed. The increases will make them progressively stronger though, and with further software tweaks they will eventually surpass humans. 

```

### Raghuram Ramanujan et al.


Quote by [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), and [Bart Selman](Bart_Selman "Bart Selman") from their abstract *On Adversarial Search Spaces and Sampling-Based Planning* [[10]](#cite_note-10):




```
UCT has been shown to outperform traditional [minimax](Minimax "Minimax") based approaches in several challenging domains such as [Go](Go "Go") and [KriegSpiel](KriegSpiel "KriegSpiel"), although minimax search still prevails in other domains such as [Chess](Chess "Chess"). This work provides insights into the properties of adversarial search spaces that play a key role in the success or failure of UCT and similar sampling-based approaches. We show that certain "early loss" or "shallow trap" configurations, while unlikely in Go, occur surprisingly often in games like Chess (even in grandmaster games). We provide evidence that UCT, unlike minimax search, is unable to identify such traps in Chess and spends a great deal of time exploring much deeper game play than needed. 

```

## See also


* [FSSS-Minimax](Ari_Weinstein#FSSS-Minimax "Ari Weinstein")
* [Match Statistics](Match_Statistics "Match Statistics")
* [MC and UCT poster](Jakob_Erdmann#UCT "Jakob Erdmann") by [Jakob Erdmann](Jakob_Erdmann "Jakob Erdmann")
* [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
* [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin")
* [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")


## Publications


### 2000 ...


* [Peter Auer](Peter_Auer "Peter Auer"), [Nicolò Cesa-Bianchi](Nicol%C3%B2_Cesa-Bianchi "Nicolò Cesa-Bianchi"), [Paul Fischer](Paul_Fischer "Paul Fischer") (**2002**). *[Finite-time Analysis of the Multiarmed Bandit Problem](http://link.springer.com/article/10.1023%2FA%3A1013689704352)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 47, No. 2, [pdf](http://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf)


### 2005 ...


**2006**



* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2006**). *[Bandit based Monte-Carlo Planning](http://www.computer-go.info/resources/bandit.html)*. ECML-06, LNCS/LNAI 4212, [pdf](http://old.sztaki.hu/~szcsaba/papers/ecml06.pdf)
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Jan Willemson](index.php?title=Jan_Willemson&action=edit&redlink=1 "Jan Willemson (page does not exist)") (**2006**). *Improved Monte-Carlo Search*. [pdf](http://www.sztaki.hu/~szcsaba/papers/cg06-ext.pdf)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Yizao Wang](Yizao_Wang "Yizao Wang") (**2006**). *Exploration exploitation in Go: UCT for Monte-Carlo Go*. [pdf](http://www.lri.fr/%7Egelly/paper/nips_exploration_exploitation_mogo.pdf)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Yizao Wang](Yizao_Wang "Yizao Wang"), [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2006**). *Modiﬁcation of UCT with Patterns in Monte-Carlo Go*. [INRIA](http://hal.inria.fr/inria-00117266)


**2007**



* [Yizao Wang](Yizao_Wang "Yizao Wang"), [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly") (**2007**). *Modifications of UCT and Sequence-Like Simulations for Monte-Carlo Go*. IEEE Symposium on Computational Intelligence and Games, Honolulu, USA, 2007, [pdf](http://www.stat.lsa.umich.edu/%7Eyizwang/publications/wang07modifications.pdf)
* [Shugo Nakamura](index.php?title=Shugo_Nakamura&action=edit&redlink=1 "Shugo Nakamura (page does not exist)"), [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2007**). *Improvement of UCT using evaluation function*. [12th Game Programming Workshop 2007](http://www.computer-shogi.org/gpw/gpw12_e.html)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)") (**2007**). *On the Parallelization of UCT*. [CGW 2007](CGW_2007 "CGW 2007"), [pdf](http://www.lamsade.dauphine.fr/%7Ecazenave/papers/parallelUCT.pdf) » [Parallel Search](Parallel_Search "Parallel Search")
* [Jean-Yves Audibert](Jean-Yves_Audibert "Jean-Yves Audibert"), [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2007**). *Tuning Bandit Algorithms in Stochastic Environments*. [pdf](http://certis.enpc.fr/~audibert/ucb_alt.pdf)


**2008**



* [Nathan Sturtevant](Nathan_Sturtevant "Nathan Sturtevant") (**2008**). *[An Analysis of UCT in Multi-player Games](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_4)*. [CG 2008](CG_2008 "CG 2008")
* [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2008**). *[Parallel Monte-Carlo Tree Search](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_6)*. [CG 2008](CG_2008 "CG 2008"), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/multithreadedMCTS2.pdf)


**2009**



* [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2009**). *The Monte-Carlo Revolution in Go*. JFFoS'2008: Japanese-French Frontiers of Science Symposium, [slides as pdf](http://remi.coulom.free.fr/JFFoS/JFFoS.pdf)
* [Fabien Teytaud](Fabien_Teytaud "Fabien Teytaud"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2009**). *Creating an Upper-Confidence-Tree program for Havannah*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [inria-00380539 as pdf](http://hal.inria.fr/docs/00/38/05/39/PDF/hav.pdf) » [Havannah](Havannah "Havannah")


### 2010 ...


* [Jean Méhat](Jean_M%C3%A9hat "Jean Méhat"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2010**). *Combining UCT and Nested Monte-Carlo Search for Single-Player General Game Playing*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 4, [pdf 2009](http://www.lamsade.dauphine.fr/~cazenave/papers/ggp2009.pdf) » [General Game Playing](General_Game_Playing "General Game Playing")
* [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Bart Selman](Bart_Selman "Bart Selman") (**2010**). *[On Adversarial Search Spaces and Sampling-Based Planning](http://www.aaai.org/ocs/index.php/ICAPS/ICAPS10/paper/view/1458)*. [ICAPS 2010](http://www.aaai.org/Press/Proceedings/icaps10.php) [[11]](#cite_note-11)
* [Damien Pellier](index.php?title=Damien_Pellier&action=edit&redlink=1 "Damien Pellier (page does not exist)"), [Bruno Bouzy](Bruno_Bouzy "Bruno Bouzy"), [Marc Métivier](index.php?title=Marc_M%C3%A9tivier&action=edit&redlink=1 "Marc Métivier (page does not exist)") (**2010**). *An UCT Approach for Anytime Agent-based Planning*. [PAAMS'10](http://www.springer.com/de/book/9783642123832), [pdf](http://www.mi.parisdescartes.fr/~bouzy/publications/pellier-bouzy-metivier-paams10.pdf)
* [Thomas J. Walsh](index.php?title=Thomas_J._Walsh&action=edit&redlink=1 "Thomas J. Walsh (page does not exist)"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2010**). *Integrating sample-based planning and model-based reinforcement learning.* [AAAI](AAAI "AAAI"), [pdf](https://pdfs.semanticscholar.org/bdc9/bfb6ecc6fb5afb684df03d7220c46ebdbf4e.pdf) » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [Takayuki Yajima](index.php?title=Takayuki_Yajima&action=edit&redlink=1 "Takayuki Yajima (page does not exist)"), [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Toshiki Matsui](index.php?title=Toshiki_Matsui&action=edit&redlink=1 "Toshiki Matsui (page does not exist)"), [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto"), [Kristian Spoerer](index.php?title=Kristian_Spoerer&action=edit&redlink=1 "Kristian Spoerer (page does not exist)") (**2010**). *[Node-Expansion Operators for the UCT Algorithm](https://link.springer.com/chapter/10.1007%2F978-3-642-17928-0_11)*. [CG 2010](CG_2010 "CG 2010")


**2011**



* [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Kazuki Yoshizoe](index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)"), [Kokolo Ikeda](Kokolo_Ikeda "Kokolo Ikeda") (**2011**). *[Accelerated UCT and Its Application to Two-Player Games](http://link.springer.com/chapter/10.1007/978-3-642-31866-5_1)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2011**). *[Mixing MCTS with Conventional Static Evaluation: Experiments and shortcuts en-route to full UCT](http://www.aifactory.co.uk/newsletter/2011_02_mcts_static.htm)*. [AI Factory](AI_Factory "AI Factory"), Winter 2011 » [Evaluation](Evaluation "Evaluation")
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [David Silver](David_Silver "David Silver") (**2011**). *Monte-Carlo tree search and rapid action value estimation in computer Go*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 175, No. 11, [preprint as pdf](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/mcrave.pdf)
* [Lars Schaefers](index.php?title=Lars_Schaefers&action=edit&redlink=1 "Lars Schaefers (page does not exist)"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2011**). *UCT-Treesplit - Parallel MCTS on Distributed Memory*. [ICAPS 2011](http://www.aaai.org/Press/Proceedings/icaps11.php), [pdf](http://www.cs.uni-paderborn.de/fileadmin/Informatik/AG-Platzner/People/Schaefers/TreesplitICAPS.pdf) » [Parallel Search](Parallel_Search "Parallel Search")
* [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Bart Selman](Bart_Selman "Bart Selman") (**2011**). *[Trade-Offs in Sampling-Based Adversarial Planning](http://aaai.org/ocs/index.php/ICAPS/ICAPS11/paper/view/2708)*. [ICAPS 2011](http://www.aaai.org/Press/Proceedings/icaps11.php)
* [Christopher D. Rosin](Christopher_D._Rosin "Christopher D. Rosin") (**2011**). *[Multi-armed bandits with episode context](https://link.springer.com/article/10.1007/s10472-011-9258-6)*. Annals of Mathematics and Artificial Intelligence, Vol. 61, No. 3, [ISAIM 2010 pdf](http://gauss.ececs.uc.edu/Workshops/isaim2010/papers/rosin.pdf) » [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin")
* [Adrien Couëtoux](index.php?title=Adrien_Cou%C3%ABtoux&action=edit&redlink=1 "Adrien Couëtoux (page does not exist)"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Nataliya Sokolovska](index.php?title=Nataliya_Sokolovska&action=edit&redlink=1 "Nataliya Sokolovska (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Nicolas Bonnard](index.php?title=Nicolas_Bonnard&action=edit&redlink=1 "Nicolas Bonnard (page does not exist)") (**2011**). *Continuous Upper Confidence Trees*. [LION 2011](https://dblp.uni-trier.de/db/conf/lion/lion2011.html), [pdf](https://hal.archives-ouvertes.fr/hal-00542673v1/document)
* [David Tolpin](index.php?title=David_Tolpin&action=edit&redlink=1 "David Tolpin (page does not exist)"), [Solomon Eyal Shimony](Solomon_Eyal_Shimony "Solomon Eyal Shimony") (**2011**). *Doing Better Than UCT: Rational Monte Carlo Sampling in Trees*. [arXiv:1108.3711](https://arxiv.org/abs/1108.3711)


**2012**



* [Oleg Arenz](index.php?title=Oleg_Arenz&action=edit&redlink=1 "Oleg Arenz (page does not exist)") (**2012**). *Monte Carlo Chess*. B.Sc. thesis, [Darmstadt University of Technology](Darmstadt_University_of_Technology "Darmstadt University of Technology"), advisor [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [pdf](http://www.ke.tu-darmstadt.de/lehre/arbeiten/bachelor/2012/Arenz_Oleg.pdf) » [Stockfish](Stockfish "Stockfish")
* [Cameron Browne](Cameron_Browne "Cameron Browne"), [Edward Powley](index.php?title=Edward_Powley&action=edit&redlink=1 "Edward Powley (page does not exist)"), [Daniel Whitehouse](index.php?title=Daniel_Whitehouse&action=edit&redlink=1 "Daniel Whitehouse (page does not exist)"), [Simon Lucas](Simon_Lucas "Simon Lucas"), [Peter Cowling](index.php?title=Peter_Cowling&action=edit&redlink=1 "Peter Cowling (page does not exist)"), [Philipp Rohlfshagen](index.php?title=Philipp_Rohlfshagen&action=edit&redlink=1 "Philipp Rohlfshagen (page does not exist)"), [Stephen Tavener](index.php?title=Stephen_Tavener&action=edit&redlink=1 "Stephen Tavener (page does not exist)"), [Diego Perez](index.php?title=Diego_Perez&action=edit&redlink=1 "Diego Perez (page does not exist)"), [Spyridon Samothrakis](index.php?title=Spyridon_Samothrakis&action=edit&redlink=1 "Spyridon Samothrakis (page does not exist)"), [Simon Colton](index.php?title=Simon_Colton&action=edit&redlink=1 "Simon Colton (page does not exist)") (**2012**). *[A Survey of Monte Carlo Tree Search Methods](https://ieeexplore.ieee.org/document/6145622)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 4, No. 1, [pdf](http://ccg.doc.gold.ac.uk/ccg_old/papers/browne_tciaig12_1.pdf)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Marc Schoenauer](Marc_Schoenauer "Marc Schoenauer"), [Michèle Sebag](Mich%C3%A8le_Sebag "Michèle Sebag"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [David Silver](David_Silver "David Silver"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2012**). *[The Grand Challenge of Computer Go: Monte Carlo Tree Search and Extensions](http://dl.acm.org/citation.cfm?id=2093548.2093574)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 55, No. 3, [pdf preprint](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/grand-challenge.pdf)
* [Adrien Couetoux](index.php?title=Adrien_Couetoux&action=edit&redlink=1 "Adrien Couetoux (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Hassen Doghmen](index.php?title=Hassen_Doghmen&action=edit&redlink=1 "Hassen Doghmen (page does not exist)") (**2012**). *Learning a Move-Generator for Upper Confidence Trees*. [ICS 2012](http://ics2012.ndhu.edu.tw/), [Hualien](https://en.wikipedia.org/wiki/Hualien_City), [Taiwan](https://en.wikipedia.org/wiki/Taiwan), December 2012 » [Learning](Learning "Learning"), [Move Generation](Move_Generation "Move Generation")
* [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Horst Samulowitz](index.php?title=Horst_Samulowitz&action=edit&redlink=1 "Horst Samulowitz (page does not exist)"), [Chandra Reddy](index.php?title=Chandra_Reddy&action=edit&redlink=1 "Chandra Reddy (page does not exist)") (**2012**). *[Guiding Combinatorial Optimization with UCT](http://link.springer.com/chapter/10.1007%2F978-3-642-29828-8_23)*. [CPAIOR 2012](http://dblp.uni-trier.de/db/conf/cpaior/cpaior2012.html#SabharwalSR12), [abstract as pdf](http://web.emn.fr/x-info/cpaior-2012/uploads/Abstracts/CPAIOR%20-%2072980356.pdf), [draft as pdf](http://www.cs.toronto.edu/~horst/cogrobo/papers/uctmip.pdf)
* [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Bart Selman](Bart_Selman "Bart Selman") (**2012**). *Understanding Sampling Style Adversarial Search Methods*. [arXiv:1203.4011](http://arxiv.org/abs/1203.4011)
* [Cheng-Wei Chou](Cheng-Wei_Chou "Cheng-Wei Chou"), [Ping-Chiang Chou](index.php?title=Ping-Chiang_Chou&action=edit&redlink=1 "Ping-Chiang Chou (page does not exist)"), [Chang-Shing Lee](Chang-Shing_Lee "Chang-Shing Lee"), [David L. Saint-Pierre](index.php?title=David_L._Saint-Pierre&action=edit&redlink=1 "David L. Saint-Pierre (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Mei-Hui Wang](Mei-Hui_Wang "Mei-Hui Wang"), [Li-Wen Wu](index.php?title=Li-Wen_Wu&action=edit&redlink=1 "Li-Wen Wu (page does not exist)"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2012**). *Strategic Choices: Small Budgets and Simple Regret*. [TAAI 2012](index.php?title=TAAI_2012&action=edit&redlink=1 "TAAI 2012 (page does not exist)"), [Excellent Paper Award](http://www.csie.ndhu.edu.tw/csieweb/en/node/685), [pdf](https://hal.inria.fr/hal-00753145v2/document)
* [Arthur Guez](Arthur_Guez "Arthur Guez"), [David Silver](David_Silver "David Silver"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2012**). *Efficient Bayes-Adaptive Reinforcement Learning using Sample-Based Search*. [arXiv:1205.3109](https://arxiv.org/abs/1205.3109)
* [Truong-Huy Dinh Nguyen](Truong-Huy_Dinh_Nguyen "Truong-Huy Dinh Nguyen"), [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee"), [Tze-Yun Leong](index.php?title=Tze-Yun_Leong&action=edit&redlink=1 "Tze-Yun Leong (page does not exist)") (**2012**). *Bootstrapping Monte Carlo Tree Search with an Imperfect Heuristic*. [arXiv:1206.5940](https://arxiv.org/abs/1206.5940)
* [David Tolpin](index.php?title=David_Tolpin&action=edit&redlink=1 "David Tolpin (page does not exist)"), [Solomon Eyal Shimony](Solomon_Eyal_Shimony "Solomon Eyal Shimony") (**2012**). *MCTS Based on Simple Regret*. [AAAI-2012](Conferences#AAAI-2012 "Conferences"), [arXiv:1207.5536](https://arxiv.org/abs/1207.5536)


**2013**



* [Simon Viennot](Simon_Viennot "Simon Viennot"), [Kokolo Ikeda](Kokolo_Ikeda "Kokolo Ikeda") (**2013**). *[Efficiency of Static Knowledge Bias in Monte-Carlo Tree Search](http://link.springer.com/chapter/10.1007%2F978-3-319-09165-5_3)*. [CG 2013](CG_2013 "CG 2013")
* [Rui Li](index.php?title=Rui_Li&action=edit&redlink=1 "Rui Li (page does not exist)"), [Yueqiu Wu](index.php?title=Yueqiu_Wu&action=edit&redlink=1 "Yueqiu Wu (page does not exist)"), [Andi Zhang](index.php?title=Andi_Zhang&action=edit&redlink=1 "Andi Zhang (page does not exist)"), [Chen Ma](index.php?title=Chen_Ma&action=edit&redlink=1 "Chen Ma (page does not exist)"), [Bo Chen](index.php?title=Bo_Chen&action=edit&redlink=1 "Bo Chen (page does not exist)"), [Shuliang Wang](index.php?title=Shuliang_Wang&action=edit&redlink=1 "Shuliang Wang (page does not exist)") (**2013**). *[Technique Analysis and Designing of Program with UCT Algorithm for NoGo](http://cpfd.cnki.com.cn/Article/CPFDTOTAL-KZJC201309001170.htm)*. [CCDC2013](http://www.ccdc.neu.edu.cn/CCDC2013/)
* [Ari Weinstein](Ari_Weinstein "Ari Weinstein"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)") (**2013**). *[Rollout-based Game-tree Search Outprunes Traditional Alpha-beta](http://proceedings.mlr.press/v24/weinstein12a.html)*. [PMLR](http://proceedings.mlr.press/), Vol. 24 » [FSSS-Minimax](Ari_Weinstein#FSSS-Minimax "Ari Weinstein"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


**2014**



* [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos") (**2014**). *From Bandits to Monte-Carlo Tree Search: The Optimistic Principle Applied to Optimization and Planning*. [Foundations and Trends in Machine Learning, Vol. 7, No 1](http://dblp.uni-trier.de/db/journals/ftml/ftml7.html#Munos14), [hal-00747575v5](https://hal.archives-ouvertes.fr/hal-00747575), [slides as pdf](http://chercheurs.lille.inria.fr/~munos/papers/files/AAAI2013_slides.pdf)
* [David W. King](index.php?title=David_W._King&action=edit&redlink=1 "David W. King (page does not exist)") (**2014**). *Complexity, Heuristic, and Search Analysis for the Games of Crossings and Epaminondas*. Masters thesis, [Air Force Institute of Technology](https://en.wikipedia.org/wiki/Air_Force_Institute_of_Technology), [pdf](http://www.afit.edu/docs/AFIT-ENG-14-M-44_King.pdf) [[12]](#cite_note-12)
* [David W. King](index.php?title=David_W._King&action=edit&redlink=1 "David W. King (page does not exist)"), [Gilbert L. Peterson](index.php?title=Gilbert_L._Peterson&action=edit&redlink=1 "Gilbert L. Peterson (page does not exist)") (**2014**). *Epaminondas: Exploring Combat Tactics*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal") [[13]](#cite_note-13)
* [Truong-Huy Dinh Nguyen](Truong-Huy_Dinh_Nguyen "Truong-Huy Dinh Nguyen"), [Tomi Silander](index.php?title=Tomi_Silander&action=edit&redlink=1 "Tomi Silander (page does not exist)"), [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee"), [Tze-Yun Leong](index.php?title=Tze-Yun_Leong&action=edit&redlink=1 "Tze-Yun Leong (page does not exist)") (**2014**). *[Bootstrapping Simulation-Based Algorithms with a Suboptimal Policy](https://www.aaai.org/ocs/index.php/ICAPS/ICAPS14/paper/view/7934)*. [ICAPS 2014](https://dblp.uni-trier.de/db/conf/aips/icaps2014.html), [YouTube Video](https://youtu.be/ccwcZZj5vKM)


### 2015 ...


* [Xi Liang](Xi_Liang "Xi Liang"), [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2015**). *Job-level UCT search for solving Hex*. [CIG 2015](http://dblp.uni-trier.de/db/conf/cig/cig2015.html#LiangWW15)
* [Yusaku Mandai](index.php?title=Yusaku_Mandai&action=edit&redlink=1 "Yusaku Mandai (page does not exist)"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2015**). *LinUCB Applied to Monte Carlo Tree Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Yun-Ching Liu](index.php?title=Yun-Ching_Liu&action=edit&redlink=1 "Yun-Ching Liu (page does not exist)"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka") (**2015**). *Adapting Improved Upper Confidence Bounds for Monte-Carlo Tree Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2015**). *Ensemble UCT Needs High Exploitation*. [CoRR abs/1509.08434](http://arxiv.org/abs/1509.08434)
* [Johannes Heinrich](index.php?title=Johannes_Heinrich&action=edit&redlink=1 "Johannes Heinrich (page does not exist)"), [David Silver](David_Silver "David Silver") (**2015**). *Smooth UCT Search in Computer Poker*. [IJCAI 2015](Conferences#IJCA2015 "Conferences"), [pdf](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Publications_files/smooth_uct.pdf)
* [Xi Liang](Xi_Liang "Xi Liang"), [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2015**). *Solving Hex Openings Using Job-Level UCT Search*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
* [Naoki Mizukami](Naoki_Mizukami "Naoki Mizukami"), [Jun Suzuki](index.php?title=Jun_Suzuki&action=edit&redlink=1 "Jun Suzuki (page does not exist)"), [Hirotaka Kameko](index.php?title=Hirotaka_Kameko&action=edit&redlink=1 "Hirotaka Kameko (page does not exist)"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka") (**2017**). *Exploration Bonuses Based on Upper Confidence Bounds for Sparse Reward Games*. [Advances in Computer Games 15](Advances_in_Computer_Games_15 "Advances in Computer Games 15")
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk") (**2018**). *MCTS/UCT in Solving Real-Life Problems*. [Advances in Data Analysis with Computational Intelligence Methods](https://www.springer.com/us/book/9783319679457), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Kiminori Matsuzaki](index.php?title=Kiminori_Matsuzaki&action=edit&redlink=1 "Kiminori Matsuzaki (page does not exist)") (**2018**). *Empirical Analysis of PUCT Algorithm with Evaluation Functions of Different Quality*. [TAAI 2018](TAAI_2018 "TAAI 2018")


## Forum Posts


### 2010 ...


* [Re: Chess vs Go // AI vs IA](http://computer-go.org/pipermail/computer-go/2010-June/000376.html) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), June 02, 2010
* [Monte Carlo (upper confidence bounds applied to trees)](http://www.lifein19x19.com/forum/viewtopic.php?f=18&t=2184) by ChessGO, [Computer Go](http://www.lifein19x19.com/forum/viewforum.php?f=18), October 22, 2010
* [UCT surprise for checkers !](http://www.talkchess.com/forum/viewtopic.php?t=38554) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 25, 2011
* [uct on gpu](http://www.talkchess.com/forum/viewtopic.php?t=42590) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 24, 2012 » [GPU](GPU "GPU")
* [My new book](http://www.talkchess.com/forum/viewtopic.php?t=50721) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 02, 2014 » [Opening Book](Opening_Book "Opening Book")


### 2015 ...


* [Nebiyu-MCTS vs TSCP 1-0](http://www.talkchess.com/forum/viewtopic.php?t=65964) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 10, 2017 » [Nebiyu](Nebiyu "Nebiyu")
* [Search traps in MCTS and chess](http://www.talkchess.com/forum/viewtopic.php?t=66125) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 25, 2017 » [Sampling-Based Planning](Raghuram_Ramanujan#UCT "Raghuram Ramanujan")
* [MCTS weakness wrt AB (via Daniel Shawul)](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32429) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2017
* [Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 09, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")


### 2020 ...


* [uct algorithm bad at chess?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75484) by Ofek Shochat, [CCC](CCC "CCC"), October 21, 2020


## External Links


* [Exploration and exploitation - in Monte Carlo tree search from Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation)
* [Confidence interval from Wikipedia](https://en.wikipedia.org/wiki/Confidence_interval)
* [Multi-armed bandit from Wikipedia](https://en.wikipedia.org/wiki/Multi-armed_bandit)
* [GitHub - theKGS/MCTS: Java implementation of UCT based MCTS and Flat MCTS](https://github.com/theKGS/MCTS)
* [Sensei's Library: UCT](https://senseis.xmp.net/?UCT)
* [Lange Nacht der Wissenschaften - Long Night of Sciences Jena - 2007](https://althofer.de/lange-nacht-jena.html) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [MC and UCT poster](Jakob_Erdmann#UCT "Jakob Erdmann") by [Jakob Erdmann](Jakob_Erdmann "Jakob Erdmann")
* [Weather Report](Category:Weather_Report "Category:Weather Report") - [Boogie Woogie Waltz](https://en.wikipedia.org/wiki/Sweetnighter), 1974, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Joe Zawinul](Category:Joe_Zawinul "Category:Joe Zawinul"), [Wayne Shorter](Category:Wayne_Shorter "Category:Wayne Shorter"), [Alphonso Johnson](Category:Alphonso_Johnson "Category:Alphonso Johnson"), [Darryl Brown](https://www.allmusic.com/artist/darryl-brown-mn0001213839), [Dom Um Romão](Category:Dom_Um_Rom%C3%A3o "Category:Dom Um Romão")
 
## References


1. [↑](#cite_ref-1) [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2006**). *[Bandit based Monte-Carlo Planning](http://www.computer-go.info/resources/bandit.html)* ECML-06, LNCS/LNAI 4212, [pdf](http://www.sztaki.hu/%7Eszcsaba/papers/ecml06.pdf)
2. [↑](#cite_ref-2) [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Marc Schoenauer](Marc_Schoenauer "Marc Schoenauer"), [Michèle Sebag](Mich%C3%A8le_Sebag "Michèle Sebag"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [David Silver](David_Silver "David Silver"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2012**). *[The Grand Challenge of Computer Go: Monte Carlo Tree Search and Extensions](http://dl.acm.org/citation.cfm?id=2093548.2093574)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 55, No. 3, [pdf preprint](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/grand-challenge.pdf)
3. [↑](#cite_ref-3) see UCB1 in [Peter Auer](Peter_Auer "Peter Auer"), [Nicolò Cesa-Bianchi](Nicol%C3%B2_Cesa-Bianchi "Nicolò Cesa-Bianchi"), [Paul Fischer](Paul_Fischer "Paul Fischer") (**2002**). *[Finite-time Analysis of the Multiarmed Bandit Problem](http://link.springer.com/article/10.1023%2FA%3A1013689704352)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 47, No. 2
4. [↑](#cite_ref-4) [Exploration and exploitation - in Monte Carlo tree search from Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation)
5. [↑](#cite_ref-5)  [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [David Silver](David_Silver "David Silver") (**2011**). *Monte-Carlo tree search and rapid action value estimation in computer Go*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 175, No. 11, [preprint as pdf](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/mcrave.pdf)
6. [↑](#cite_ref-6) [Christopher D. Rosin](Christopher_D._Rosin "Christopher D. Rosin") (**2011**). *[Multi-armed bandits with episode context](https://link.springer.com/article/10.1007/s10472-011-9258-6)*. Annals of Mathematics and Artificial Intelligence, Vol. 61, No. 3, [ISAIM 2010 pdf](http://gauss.ececs.uc.edu/Workshops/isaim2010/papers/rosin.pdf)
7. [↑](#cite_ref-7) [David Silver](David_Silver "David Silver"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Sander Dieleman](index.php?title=Sander_Dieleman&action=edit&redlink=1 "Sander Dieleman (page does not exist)"), [Dominik Grewe](index.php?title=Dominik_Grewe&action=edit&redlink=1 "Dominik Grewe (page does not exist)"), [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)"), [Nal Kalchbrenner](index.php?title=Nal_Kalchbrenner&action=edit&redlink=1 "Nal Kalchbrenner (page does not exist)"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Madeleine Leach](index.php?title=Madeleine_Leach&action=edit&redlink=1 "Madeleine Leach (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2016**). *[Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 529
8. [↑](#cite_ref-8) [FAQ · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/FAQ)
9. [↑](#cite_ref-9) [Re: Chess vs Go // AI vs IA](http://computer-go.org/pipermail/computer-go/2010-June/000376.html) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), June 02, 2010
10. [↑](#cite_ref-10) [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Bart Selman](Bart_Selman "Bart Selman") (**2010**). *[On Adversarial Search Spaces and Sampling-Based Planning](http://www.aaai.org/ocs/index.php/ICAPS/ICAPS10/paper/view/1458)*. [ICAPS 2010](http://www.aaai.org/Press/Proceedings/icaps10.php)
11. [↑](#cite_ref-11) [Search traps in MCTS and chess](http://www.talkchess.com/forum/viewtopic.php?t=66125) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 25, 2017
12. [↑](#cite_ref-12) [Crossings from Wikipedia](https://en.wikipedia.org/wiki/Crossings_%28game%29)
13. [↑](#cite_ref-13)  [Epaminondas from Wikipedia](https://en.wikipedia.org/wiki/Epaminondas_%28game%29)

**[Up one level](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")**







 
