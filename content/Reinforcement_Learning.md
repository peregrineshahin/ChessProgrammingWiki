---
title: Reinforcement Learning
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* Reinforcement Learning**



[ [Markov decision processes](https://en.wikipedia.org/wiki/Markov_decision_process) [[1]](#cite_note-1)
**Reinforcement Learning**,  

a learning paradigm inspired by [behaviourist](https://en.wikipedia.org/wiki/Behaviorism) psychology and [classical conditioning](https://en.wikipedia.org/wiki/Classical_conditioning) - learning by [trial and error](Trial_and_Error "Trial and Error"), interacting with an environment to map situations to [actions](https://en.wikipedia.org/wiki/Action_selection) in such a way that some notion of cumulative [reward](https://en.wikipedia.org/wiki/Reward_system) is maximized. In computer games, reinforcement learning deals with adjusting feature weights based on results or their subsequent predictions during self play.


Reinforcement learning is indebted to the idea of [Markov decision processes](https://en.wikipedia.org/wiki/Markov_decision_process) (MDPs) in the field of [optimal control](https://en.wikipedia.org/wiki/Optimal_control) utilizing [dynamic programming](Dynamic_Programming "Dynamic Programming") techniques. The crucial [exploitation and exploration](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation) tradeoff in [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) problems as also considered in [UCT](UCT "UCT") of [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") - between "[exploitation](https://en.wikipedia.org/wiki/Exploitation)" of the machine that has the highest expected payoff and "[exploration](https://en.wikipedia.org/wiki/Exploration)" to get more information about the expected payoffs of the other machines - is also faced in reinforcement learning. 



## Temporal Difference Learning


*see Home [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")*


Q-learning at its simplest uses tables to store data. This very quickly loses viability with increasing sizes of state/action space of the system it is monitoring/controlling. One solution to this problem is to use an (adapted) [artificial neural network](Neural_Networks "Neural Networks") as a function approximator, as demonstrated by [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") in his [Backgammon](Backgammon "Backgammon") playing temporal difference learning research [[5]](#cite_note-5) [[6]](#cite_note-6).


Temporal Difference Learning is a prediction method primarily used for reinforcement learning. In the domain of computer games and computer chess, TD learning is applied through self play, subsequently predicting the [probability](https://en.wikipedia.org/wiki/Probability) of winning a [game](Chess_Game "Chess Game") during the sequence of [moves](Moves "Moves") from the [initial position](Initial_Position "Initial Position") until the end, to adjust weights for a more reliable prediction. 



## See also


* [AlphaZero](AlphaZero "AlphaZero")
* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Deep Learning](Deep_Learning "Deep Learning")
* [Dynamic Programming](Dynamic_Programming "Dynamic Programming")
* [Markov Models](Michael_L._Littman#MarkovModels "Michael L. Littman") by [Michael L. Littman](Michael_L._Littman "Michael L. Littman")
* [MENACE](Donald_Michie#MENACE "Donald Michie") by [Donald Michie](Donald_Michie "Donald Michie")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


 [UCT](UCT "UCT")
* [Neural Networks](Neural_Networks "Neural Networks")
* [Planning](Planning "Planning")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")
* [Trial and Error](Trial_and_Error "Trial and Error")


## Selected Publications


### 1954 ...


* [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1954**). *On a new Iterative Algorithm for Finding the Solutions of Games and Linear Programming Problems*. Technical Report P-473, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), U. S. Air Force Project RAND
* [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959


### 1960 ...


* [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1960**). *[Sequential Machines, Ambiguity, and Dynamic Programming](http://dl.acm.org/citation.cfm?id=321011)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 7, No. 1
* [Ronald A. Howard](Mathematician#RAHoward "Mathematician") (**1960**). *Dynamic Programming and Markov Processes*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [amazon](https://www.amazon.com/Programming-Processes-Technology-Research-Monographs/dp/0262080095)
* [Donald Michie](Donald_Michie "Donald Michie") (**1961**). *Trial and Error*. Penguin Science Survey
* [Donald Michie](Donald_Michie "Donald Michie"), Roger A. Chambers (**1968**). *Boxes: An experiment on adaptive control*. [Machine Intelligence 2](http://www.doc.ic.ac.uk/%7Eshm/MI/mi2.html), Edinburgh: Oliver & Boyd, [pdf](http://aitopics.org/sites/default/files/classic/Machine_Intelligence_2/MI2-Ch9-MichieChambers.pdf)


### 1970 ...


* [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1972**). *Brain Function and Adaptive Systems - A Heterostatic Theory*. [Air Force Cambridge Research Laboratories](https://en.wikipedia.org/wiki/Air_Force_Cambridge_Research_Laboratories), Special Reports, No. 133, [pdf](http://www.dtic.mil/dtic/tr/fulltext/u2/742259.pdf)
* [John H. Holland](Mathematician#Holland "Mathematician") (**1975**). *Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence*. [amazon.com](http://www.amazon.com/Adaptation-Natural-Artificial-Systems-Introductory/dp/0262581116)
* [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**1977**). *An Adaptive Optimal Controller for Discrete-Time Markov Environments*. [Information and Control](https://en.wikipedia.org/wiki/Information_and_Computation), Vol. 34, No. 4, [pdf](https://core.ac.uk/download/pdf/82451748.pdf)


### 1980 ...


* [Richard Sutton](Richard_Sutton "Richard Sutton") (**1984**). *[Temporal Credit Assignment in Reinforcement Learning](http://scholarworks.umass.edu/dissertations/AAI8410337/)*. Ph.D. dissertation, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts)
* [Leslie Valiant](Mathematician#LValiant "Mathematician") (**1984**). *A Theory of the Learnable*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 27, No. 11, [pdf](http://web.mit.edu/6.435/www/Valiant84.pdf)
* [Chris Watkins](index.php?title=Chris_Watkins&action=edit&redlink=1 "Chris Watkins (page does not exist)") (**1989**). *Learning from Delayed Rewards*. Ph.D. thesis, [Cambridge University](https://en.wikipedia.org/wiki/University_of_Cambridge), [pdf](http://www.cs.rhul.ac.uk/~chrisw/new_thesis.pdf)


### 1990 ...


* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1990**). *Time Derivative Models of Pavlovian Reinforcement*. Learning and Computational Neuroscience: Foundations of Adaptive Networks: 497-537
* [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1990**). *Reinforcement Learning in Markovian and Non-Markovian Environments*. [NIPS 1990](https://dblp.uni-trier.de/db/conf/nips/nips1990.html), [pdf](ftp://ftp.idsia.ch/pub/juergen/nipsnonmarkov.pdf)
* [Peter Dayan](Peter_Dayan "Peter Dayan") (**1991**). *[Reinforcing Connectionism: Learning the Statistical Way](https://www.era.lib.ed.ac.uk/handle/1842/14754)*. Ph.D. thesis, [University of Edinburgh](University_of_Edinburgh "University of Edinburgh")
* [Chris Watkins](index.php?title=Chris_Watkins&action=edit&redlink=1 "Chris Watkins (page does not exist)"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**1992**). *[Q-learning](http://www.gatsby.ucl.ac.uk/~dayan/papers/wd92.html)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 8, No. 2
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
* [Justin A. Boyan](Justin_A._Boyan "Justin A. Boyan"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**1993**). *Packet Routing in Dynamically Changing Networks: A Reinforcement Learning Approach*. [NIPS 1993](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-6-1993), [pdf](https://www.cs.cmu.edu/~jab/cv/pubs/boyan.q-routing.pdf)
* [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**1994**). *Markov Games as a Framework for Multi-Agent Reinforcement Learning*. International Conference on Machine Learning, [pdf](http://www.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf)


### 1995 ...


* [Marco Wiering](Marco_Wiering "Marco Wiering") (**1995**). *TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures*. Master's thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam), [pdf](http://webber.physik.uni-freiburg.de/~hon/vorlss02/Literatur/reinforcement/GameEvaluationWithNeuronal.pdf)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1995**). *Temporal Difference Learning and TD-Gammon*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 38, No. 3
* [Leemon C. Baird III](http://dblp.uni-trier.de/pers/hd/b/Baird_III:Leemon_C=), [Mance E. Harmon](http://dblp.uni-trier.de/pers/hd/h/Harmon:Mance_E=), [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1996**). *Reinforcement Learning: An Alternative Approach to Machine Intelligence*. [pdf](http://www.leemon.com/papers/1996bhk.pdf)
* [Leslie Pack Kaelbling](Mathematician#LPKaelbling "Mathematician"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [Andrew W. Moore](Mathematician#AWMoore "Mathematician") (**1996**). *[Reinforcement Learning: A Survey](http://www.cs.washington.edu/research/jair/volume4/kaelbling96a-html/rl-survey.html)*. [JAIR Vol. 4](http://www.jair.org/vol/vol4.html), [pdf](http://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a.pdf)
* [Robert Levinson](Robert_Levinson "Robert Levinson") (**1996**). *[General Game-Playing and Reinforcement Learning](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-8640.1996.tb00257.x/abstract)*. [Computational Intelligence, Vol. 12](http://dblp.uni-trier.de/db/journals/ci/ci12.html#PellEL96), No. 1
* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1996**). *[Efficient Reinforcement Learning through Symbiotic Evolution](https://link.springer.com/article/10.1023/A:1018004120707)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 22
* [Ronald Parr](index.php?title=Ronald_Parr&action=edit&redlink=1 "Ronald Parr (page does not exist)"), [Stuart Russell](Stuart_Russell "Stuart Russell") (**1997**). *Reinforcement Learning with Hierarchies of Machines.* In Advances in Neural Information Processing Systems 10, MIT Press, [zipped ps](http://www.cs.berkeley.edu/~russell/papers/nips97-ham.ps.gz)
* [William Uther](William_Uther "William Uther"), [Manuela M. Veloso](Manuela_Veloso "Manuela Veloso") (**1997**). *Adversarial Reinforcement Learning*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [ps](http://www.cse.unsw.edu.au/~willu/w/papers/Uther97a.ps)
* [William Uther](William_Uther "William Uther"), [Manuela M. Veloso](Manuela_Veloso "Manuela Veloso") (**1997**). *Generalizing Adversarial Reinforcement Learning*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [ps](http://www.cse.unsw.edu.au/~willu/w/papers/Uther97b.ps)
* [Marco Wiering](Marco_Wiering "Marco Wiering"), [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1997**). *HQ-learning*. [Adaptive Behavior](https://en.wikipedia.org/wiki/Adaptive_Behavior_%28journal%29), Vol. 6, No 2
* [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**1998**). *Reinforcement Learning: Theory and Practice*. Proceedings of the 2nd Slovak Conference on Artificial Neural Networks, [zipped ps](http://www.sztaki.hu/%7Eszcsaba/papers/scann98.ps.gz)
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1998**). *[Reinforcement Learning: An Introduction](https://mitpress.mit.edu/books/reinforcement-learning)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Vassilis Papavassiliou](http://www.ilsp.gr/homepages/papavasiliou_eng.html), [Stuart Russell](Stuart_Russell "Stuart Russell") (**1999**). *Convergence of reinforcement learning with general function approximators.* In Proc. IJCAI-99, Stockholm, [ps](http://www.cs.berkeley.edu/~russell/papers/ijcai99-bridge.ps)
* [Marco Wiering](Marco_Wiering "Marco Wiering") (**1999**). *Explorations in Efficient Reinforcement Learning*. Ph.D. thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam), advisors [Frans Groen](Mathematician#FGroen "Mathematician") and [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Doina Precup](Doina_Precup "Doina Precup"), [Satinder Singh](Mathematician#SSingh "Mathematician") (**1999**). *Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 112, [pdf](https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf)


### 2000 ...


* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2000**). *A Review of Reinforcement Learning*. [AI Magazine, Vol. 21](http://www.informatik.uni-trier.de/~ley/db/journals/aim/aim21.html#ThrunL00), No. 1
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000")
* [Andrew Ng](index.php?title=Andrew_Ng&action=edit&redlink=1 "Andrew Ng (page does not exist)"), [Stuart Russell](Stuart_Russell "Stuart Russell") (**2000**). *Algorithms for inverse reinforcement learning.* In Proceedings of the Seventeenth International Conference on Machine Learning, Stanford, California: Morgan Kaufmann, [pdf](http://www.cs.berkeley.edu/~russell/papers/ml00-irl.pdf)
* [Dean F. Hougen](http://www.cs.ou.edu/~hougen/), [Maria Gini](http://www-users.cs.umn.edu/~gini/), [James R. Slagle](James_R._Slagle "James R. Slagle") (**2000**). *[An Integrated Connectionist Approach to Reinforcement Learning for Robotic Control](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.2633)*. ICML '00 Proceedings of the Seventeenth International Conference on Machine Learning
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Peter Bartlett](Mathematician#PBartlett "Mathematician") (**2000**). *Reinforcement Learning on POMDPs via Direct Gradient Ascent*. [ICML 2000](http://dblp.uni-trier.de/db/conf/icml/icml2000.html), [pdf](https://pdfs.semanticscholar.org/b874/98f0879d312c308889135203b17069aa0486.pdf)
* [Doina Precup](Doina_Precup "Doina Precup") (**2000**). *Temporal Abstraction in Reinforcement Learning*. Ph.D. Dissertation, Department of Computer Science, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts_Amherst), [Amherst](https://en.wikipedia.org/wiki/Amherst,_Massachusetts).
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2001**). *Chess Neighborhoods, Function Combinations and Reinforcements Learning*. In Computers and Games (eds. [Tony Marsland](Tony_Marsland "Tony Marsland") and I. Frank). [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science),. Springer,. [pdf](http://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
* [Marco Block-Berlitz](Marco_Block-Berlitz "Marco Block-Berlitz") (**2003**). *Reinforcement Learning in der Schachprogrammierung*. Studienarbeit, Freie Universität Berlin, Dozent: [Prof. Dr. Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [pdf](http://page.mi.fu-berlin.de/block/Skripte/Reinforcement.pdf) (German)
* [Henk Mannen](Henk_Mannen "Henk Mannen") (**2003**). *Learning to play chess using reinforcement learning with database games*. Master’s thesis, Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), [pdf](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.109.810&rep=rep1&type=pdf)
* [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [Geoffrey Gordon](index.php?title=Geoffrey_Gordon&action=edit&redlink=1 "Geoffrey Gordon (page does not exist)"), [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**2003**). *Point-based value iteration: An anytime algorithm for POMDPs*. [IJCAI](Conferences#IJCAI2003 "Conferences"), [pdf](http://www.fore.robot.cc/papers/Pineau03a.pdf)
* [Amy J. Kerr](https://dblp.uni-trier.de/pers/hd/k/Kerr:Amy_J=), [Todd W. Neller](Todd_W._Neller "Todd W. Neller"), [Christopher J. La Pilla](https://dblp.uni-trier.de/pers/hd/p/Pilla:Christopher_J=_La) , [Michael D. Schompert](https://dblp.uni-trier.de/pers/hd/s/Schompert:Michael_D=) (**2002**). *[Java Resources for Teaching Reinforcement Learning](https://www.semanticscholar.org/paper/Java-Resources-for-Teaching-Reinforcement-Learning-Kerr-Neller/3d84018eb8b8668c13d1d4f6efca4442af2915b4)*. [PDPTA 2003](https://dblp.uni-trier.de/db/conf/pdpta/pdpta2003-3.html)
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), Vignir Hafsteinsson, Ársæll Jóhannsson, Einar Jónsson (**2004**). *Efficient Use of Reinforcement Learning in a Computer Game*. In Computer Games: Artificial Intellignece, Design and Education (CGAIDE'04), pp. 379–383, 2004. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonHJJ04.pdf)
* [Imran Ghory](http://imranontech.com/) (**2004**). *Reinforcement learning in board games*. CSTR-04-004, [Department of Computer Science](http://www.cs.bris.ac.uk/), [University of Bristol](https://en.wikipedia.org/wiki/University_of_Bristol). [pdf](http://www.cs.bris.ac.uk/Publications/Papers/2000100.pdf) [[7]](#cite_note-7)
* [Eric Wiewiora](index.php?title=Eric_Wiewiora&action=edit&redlink=1 "Eric Wiewiora (page does not exist)") (**2004**). *Efficient Exploration for Reinforcement Learning*. MSc thesis, [pdf](http://cseweb.ucsd.edu/%7Eewiewior/04efficient.pdf)
* [Albert Xin Jiang](Albert_Xin_Jiang "Albert Xin Jiang") (**2004**). *Multiagent Reinforcement Learning in Stochastic Games with Continuous Action Spaces*. [pdf](http://www.cs.ubc.ca/%7Ejiang/papers/continuous.pdf)


### 2005 ...


* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Jérémie Mary](J%C3%A9r%C3%A9mie_Mary "Jérémie Mary"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2006**). *Learning for stochastic dynamic programming*. [pdf](http://www.lri.fr/%7Egelly/paper/lfordp.pdf), [pdf](http://www.grappa.univ-lille3.fr/~mary/paper/lfordp.pdf)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly") (**2007**). *A Contribution to Reinforcement Learning; Application to Computer Go.* Ph.D. thesis, [pdf](http://www.lri.fr/~gelly/paper/SylvainGellyThesis.pdf)
* [Yong Duan](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/d/Duan:Yong.html), [Baoxia Cui](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/c/Cui:Baoxia.html), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2007**). *State Space Partition for Reinforcement Learning Based on Fuzzy Min-Max Neural Network*. [ISNN 2007](http://www.informatik.uni-trier.de/~ley/db/conf/isnn/isnn2007-2.html#DuanCX07)
* [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2007**). *Reinforcement Learning of Evaluation Functions Using Temporal Difference-Monte Carlo learning method*. [12th Game Programming Workshop](Conferences#GPW "Conferences")
* [David Silver](David_Silver "David Silver"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2007**). *Reinforcement learning of local shape in the game of Go*. [20th IJCAI](Conferences#IJCAI2007 "Conferences"), [pdf](http://webdocs.cs.ualberta.ca/~mmueller/ps/silver-ijcai2007.pdf)
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. CONCIBE SCIENCE 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, ISSN:1870-4069, Vol. 35, pp. 31-40, [Guadalajara](https://en.wikipedia.org/wiki/Guadalajara), Mexico, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)
* [Cécile Germain-Renaud](index.php?title=C%C3%A9cile_Germain-Renaud&action=edit&redlink=1 "Cécile Germain-Renaud (page does not exist)"), [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Balázs Kégl](index.php?title=Bal%C3%A1zs_K%C3%A9gl&action=edit&redlink=1 "Balázs Kégl (page does not exist)"), [Charles Loomis](index.php?title=Charles_Loomis&action=edit&redlink=1 "Charles Loomis (page does not exist)") (**2008**). *Grid Differentiated Services: a Reinforcement Learning Approach*. In 8th [IEEE](IEEE "IEEE") Symposium on Cluster Computing and the Grid. Lyon, [pdf](http://hal.inria.fr/docs/00/28/78/26/PDF/RLccg08.pdf)
* [Balázs Csanád Csáji](Bal%C3%A1zs_Csan%C3%A1d_Cs%C3%A1ji "Balázs Csanád Csáji"), [László Monostori](https://dblp.dagstuhl.de/pers/hd/m/Monostori:L=aacute=szl=oacute=) (**2008**). *Value function based reinforcement learning in changing Markovian environments*. [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research), Vol. 9, [pdf](http://www.jmlr.org/papers/volume9/csaji08a/csaji08a.pdf)
* [David Silver](David_Silver "David Silver") (**2009**). *Reinforcement Learning and Simulation-Based Search*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"). [pdf](http://webdocs.cs.ualberta.ca/~silver/David_Silver/Publications_files/thesis.pdf)
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2009**). *Coevolutionary Reinforcement Learning and its Application to Othello*. M.Sc. thesis, [Poznań University of Technology](https://en.wikipedia.org/wiki/Pozna%C5%84_University_of_Technology), supervisor [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [pdf](https://mszubert.github.io/papers/Szubert_2009_MSC.pdf)
* [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [Geoffrey Gordon](index.php?title=Geoffrey_Gordon&action=edit&redlink=1 "Geoffrey Gordon (page does not exist)"), [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**2006, 2011**). *Anytime Point-Based Approximations for Large POMDPs*. [Journal of Artificial Intelligence Research](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 27, [arXiv:1110.0027](https://arxiv.org/abs/1110.0027)


### 2010 ...


* [Joel Veness](Joel_Veness "Joel Veness"), [Kee Siong Ng](index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter"), [David Silver](David_Silver "David Silver") (**2010**). *Reinforcement Learning via AIXI Approximation*. Association for the Advancement of Artificial Intelligence (AAAI), [pdf](http://jveness.info/publications/veness_rl_via_aixi_approx.pdf)
* [Julien Pérez](index.php?title=Julien_P%C3%A9rez&action=edit&redlink=1 "Julien Pérez (page does not exist)"), [Cécile Germain-Renaud](index.php?title=C%C3%A9cile_Germain-Renaud&action=edit&redlink=1 "Cécile Germain-Renaud (page does not exist)"), [Balázs Kégl](index.php?title=Bal%C3%A1zs_K%C3%A9gl&action=edit&redlink=1 "Balázs Kégl (page does not exist)"), [Charles Loomis](index.php?title=Charles_Loomis&action=edit&redlink=1 "Charles Loomis (page does not exist)") (**2010**). *Multi-objective Reinforcement Learning for Responsive Grids*. In The Journal of Grid Computing. [pdf](http://hal.archives-ouvertes.fr/docs/00/49/15/60/PDF/RLGrid_JGC09_V7.pdf)
* [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2010**). *[Algorithms for Reinforcement Learning](https://sites.ualberta.ca/~szepesva/RLBook.html)*. Morgan & Claypool
* [Julio H. Zaragoza](https://dblp.org/pers/hd/z/Zaragoza:Julio_H=), [Eduardo F. Morales](Eduardo_F._Morales "Eduardo F. Morales") (**2010**). *Relational Reinforcement Learning with Continuous Actions by Combining Behavioral Cloning and Locally Weighted Regression*. Journal of Intelligent Systems and Applications, Vol. 2


**2011**



* [Peter Auer](Peter_Auer "Peter Auer") (**2011**). *Exploration and Exploitation in Online Learning*. [ICAIS 2011](http://dblp.uni-trier.de/db/conf/icais/icais2011.html#Auer11)
* [Charles Elkan](Charles_Elkan "Charles Elkan") (**2011**). *Reinforcement Learning with a Bilinear Q Function*. [EWRL 2011](http://www.informatik.uni-trier.de/~ley/db/conf/ewrl/ewrl2011.html#Elkan11)


**2012**



* [Marco Wiering](Marco_Wiering "Marco Wiering"), [Martijn Van Otterlo](http://martijnvanotterlo.nl/) (**2012**). *Reinforcement learning: State-of-the-art*. [Adaptation, Learning, and Optimization, Vol. 12](http://link.springer.com/book/10.1007/978-3-642-27645-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


 [István Szita](Istv%C3%A1n_Szita "István Szita") (**2012**). *[Reinforcement Learning in Games](http://link.springer.com/chapter/10.1007%2F978-3-642-27645-3_17)*. Chapter 17
* [Thomas J. Walsh](index.php?title=Thomas_J._Walsh&action=edit&redlink=1 "Thomas J. Walsh (page does not exist)"), [István Szita](Istv%C3%A1n_Szita "István Szita"), [Carlos Diuk](index.php?title=Carlos_Diuk&action=edit&redlink=1 "Carlos Diuk (page does not exist)"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2012**). *Exploring compact reinforcement-learning representations with linear regression*. [arXiv:1205.2606](https://arxiv.org/abs/1205.2606)
* [Arthur Guez](Arthur_Guez "Arthur Guez"), [David Silver](David_Silver "David Silver"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2012**). *[Efficient Bayes-Adaptive Reinforcement Learning using Sample-Based Search](https://papers.nips.cc/paper/4767-efficient-bayes-adaptive-reinforcement-learning-using-sample-based-search)*. [NIPS 2012](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-25-2012)


**2013**



* [Arthur Guez](Arthur_Guez "Arthur Guez"), [David Silver](David_Silver "David Silver"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2013**). *Scalable and Efficient Bayes-Adaptive Reinforcement Learning Based on Monte-Carlo Tree Search*. [Journal of Artificial Intelligence Research](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 48, [pdf](https://www.jair.org/media/4117/live-4117-7507-jair.pdf)
* [Michiel van der Ree](http://dblp.uni-trier.de/pers/hd/r/Ree:M=_van_der), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2013**). *Reinforcement Learning in the Game of Othello: Learning Against a Fixed Opponent and Learning from Self-Play*. [ADPRL 2013](http://dblp.uni-trier.de/db/conf/adprl/adprl2013.html#ReeW13)
* [Luuk Bom](http://dblp.uni-trier.de/pers/hd/b/Bom:Luuk), [Ruud Henken](http://dblp.uni-trier.de/pers/hd/h/Henken:Ruud), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2013**). *Reinforcement Learning to Train Ms. Pac-Man Using Higher-order Action-relative Inputs*. [ADPRL 2013](http://dblp.uni-trier.de/db/conf/adprl/adprl2013.html#BomHW13) [[8]](#cite_note-8)
* [Peter Auer](Peter_Auer "Peter Auer"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter"), [Laurent Orseau](index.php?title=Laurent_Orseau&action=edit&redlink=1 "Laurent Orseau (page does not exist)") (**2013**). *[Reinforcement Learning](http://drops.dagstuhl.de/opus/volltexte/2013/4340/)*. [Dagstuhl Reports, Vol. 3, No. 8](http://dblp.uni-trier.de/db/journals/dagstuhl-reports/dagstuhl-reports3.html#AuerHO13), DOI: [10.4230/DagRep.3.8.1](http://drops.dagstuhl.de/opus/volltexte/2013/4340/), URN: [urn:nbn:de:0030-drops-43409](http://drops.dagstuhl.de/opus/volltexte/2013/4340/)
* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Daan Wierstra](index.php?title=Daan_Wierstra&action=edit&redlink=1 "Daan Wierstra (page does not exist)"), [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)") (**2013**). *Playing Atari with Deep Reinforcement Learning*. [arXiv:1312.5602](http://arxiv.org/abs/1312.5602) [[9]](#cite_note-9) [[10]](#cite_note-10)
* [Ari Weinstein](Ari_Weinstein "Ari Weinstein") (**2013**). *Local Planning For Continuous Markov Decision Processes*. Ph.D. thesis, [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University), advisor [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [pdf](http://cs.brown.edu/~mlittman/theses/weinstein.pdf)


**2014**



* [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2014**). *Coevolutionary Shaping for Reinforcement Learning*. Ph.D. thesis, [Poznań University of Technology](https://en.wikipedia.org/wiki/Pozna%C5%84_University_of_Technology), supervisor [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), co-supervisor [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [pdf](http://www.cs.put.poznan.pl/mszubert/pub/phdthesis.pdf)


### 2015 ...


* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver"), [Andrei A. Rusu](Mathematician#AARusu "Mathematician"), [Joel Veness](Joel_Veness "Joel Veness"), [Marc G. Bellemare](index.php?title=Marc_G._Bellemare&action=edit&redlink=1 "Marc G. Bellemare (page does not exist)"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Andreas K. Fidjeland](index.php?title=Andreas_K._Fidjeland&action=edit&redlink=1 "Andreas K. Fidjeland (page does not exist)"), [Georg Ostrovski](index.php?title=Georg_Ostrovski&action=edit&redlink=1 "Georg Ostrovski (page does not exist)"), [Stig Petersen](index.php?title=Stig_Petersen&action=edit&redlink=1 "Stig Petersen (page does not exist)"), [Charles Beattie](index.php?title=Charles_Beattie&action=edit&redlink=1 "Charles Beattie (page does not exist)"), [Amir Sadik](index.php?title=Amir_Sadik&action=edit&redlink=1 "Amir Sadik (page does not exist)"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Helen King](index.php?title=Helen_King&action=edit&redlink=1 "Helen King (page does not exist)"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Daan Wierstra](index.php?title=Daan_Wierstra&action=edit&redlink=1 "Daan Wierstra (page does not exist)"), [Shane Legg](index.php?title=Shane_Legg&action=edit&redlink=1 "Shane Legg (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2015**). *[Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 518
* [Tobias Graf](index.php?title=Tobias_Graf&action=edit&redlink=1 "Tobias Graf (page does not exist)"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)") (**2015**). *Adaptive Playouts in Monte Carlo Tree Search with Policy Gradient Reinforcement Learning*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Arun Nair](index.php?title=Arun_Nair&action=edit&redlink=1 "Arun Nair (page does not exist)"), [Praveen Srinivasan](index.php?title=Praveen_Srinivasan&action=edit&redlink=1 "Praveen Srinivasan (page does not exist)"), [Sam Blackwell](index.php?title=Sam_Blackwell&action=edit&redlink=1 "Sam Blackwell (page does not exist)"), [Cagdas Alcicek](index.php?title=Cagdas_Alcicek&action=edit&redlink=1 "Cagdas Alcicek (page does not exist)"), [Rory Fearon](index.php?title=Rory_Fearon&action=edit&redlink=1 "Rory Fearon (page does not exist)"), [Alessandro De Maria](index.php?title=Alessandro_De_Maria&action=edit&redlink=1 "Alessandro De Maria (page does not exist)"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Mustafa Suleyman](index.php?title=Mustafa_Suleyman&action=edit&redlink=1 "Mustafa Suleyman (page does not exist)"), [Charles Beattie](index.php?title=Charles_Beattie&action=edit&redlink=1 "Charles Beattie (page does not exist)"), [Stig Petersen](index.php?title=Stig_Petersen&action=edit&redlink=1 "Stig Petersen (page does not exist)"), [Shane Legg](index.php?title=Shane_Legg&action=edit&redlink=1 "Shane Legg (page does not exist)"), [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver") (**2015**). *Massively Parallel Methods for Deep Reinforcement Learning*. [arXiv:1507.04296](http://arxiv.org/abs/1507.04296)
* [Matthew Lai](Matthew_Lai "Matthew Lai") (**2015**). *Giraffe: Using Deep Reinforcement Learning to Play Chess*. M.Sc. thesis, [Imperial College London](https://en.wikipedia.org/wiki/Imperial_College_London), [arXiv:1509.01549v1](http://arxiv.org/abs/1509.01549v1) » [Giraffe](Giraffe "Giraffe")
* [Hado van Hasselt](index.php?title=Hado_van_Hasselt&action=edit&redlink=1 "Hado van Hasselt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [David Silver](David_Silver "David Silver") (**2015**). *Deep Reinforcement Learning with Double Q-learning*. [arXiv:1509.06461](http://arxiv.org/abs/1509.06461)


**2016**



* [Ziyu Wang](index.php?title=Ziyu_Wang&action=edit&redlink=1 "Ziyu Wang (page does not exist)"), [Nando de Freitas](index.php?title=Nando_de_Freitas&action=edit&redlink=1 "Nando de Freitas (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot") (**2016**). *Dueling Network Architectures for Deep Reinforcement Learning*. [arXiv:1511.06581](http://arxiv.org/abs/1511.06581)
* [David Silver](David_Silver "David Silver"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Sander Dieleman](index.php?title=Sander_Dieleman&action=edit&redlink=1 "Sander Dieleman (page does not exist)"), [Dominik Grewe](index.php?title=Dominik_Grewe&action=edit&redlink=1 "Dominik Grewe (page does not exist)"), [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)"), [Nal Kalchbrenner](index.php?title=Nal_Kalchbrenner&action=edit&redlink=1 "Nal Kalchbrenner (page does not exist)"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Madeleine Leach](index.php?title=Madeleine_Leach&action=edit&redlink=1 "Madeleine Leach (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2016**). *[Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 529 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
* [Hung Guei](index.php?title=Hung_Guei&action=edit&redlink=1 "Hung Guei (page does not exist)"), [Tinghan Wei](index.php?title=Tinghan_Wei&action=edit&redlink=1 "Tinghan Wei (page does not exist)"), [Jin-Bo Huang](index.php?title=Jin-Bo_Huang&action=edit&redlink=1 "Jin-Bo Huang (page does not exist)"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2016**). *An Empirical Study on Applying Deep Reinforcement Learning to the Game 2048*. [CG 2016](CG_2016 "CG 2016")
* [Omid E. David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu"), [Lior Wolf](index.php?title=Lior_Wolf&action=edit&redlink=1 "Lior Wolf (page does not exist)") (**2016**). *[DeepChess: End-to-End Deep Neural Network for Automatic Learning in Chess](http://link.springer.com/chapter/10.1007%2F978-3-319-44781-0_11)*. [ICAAN 2016](http://icann2016.org/), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 9887, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf preprint](http://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf) » [DeepChess](index.php?title=DeepChess&action=edit&redlink=1 "DeepChess (page does not exist)") [[11]](#cite_note-11) [[12]](#cite_note-12)
* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Adrià Puigdomènech Badia](index.php?title=Adri%C3%A0_Puigdom%C3%A8nech_Badia&action=edit&redlink=1 "Adrià Puigdomènech Badia (page does not exist)"), [Mehdi Mirza](index.php?title=Mehdi_Mirza&action=edit&redlink=1 "Mehdi Mirza (page does not exist)"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Tim Harley](index.php?title=Tim_Harley&action=edit&redlink=1 "Tim Harley (page does not exist)"), [David Silver](David_Silver "David Silver"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu") (**2016**). *Asynchronous Methods for Deep Reinforcement Learning*. [arXiv:1602.01783v2](https://arxiv.org/abs/1602.01783)
* [Shixiang Gu](index.php?title=Shixiang_Gu&action=edit&redlink=1 "Shixiang Gu (page does not exist)"), [Ethan Holly](index.php?title=Ethan_Holly&action=edit&redlink=1 "Ethan Holly (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Sergey Levine](index.php?title=Sergey_Levine&action=edit&redlink=1 "Sergey Levine (page does not exist)") (**2016**). *Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates*. [arXiv:1610.00633](https://arxiv.org/abs/1610.00633)
* [Max Jaderberg](index.php?title=Max_Jaderberg&action=edit&redlink=1 "Max Jaderberg (page does not exist)"), [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Wojciech Marian Czarnecki](index.php?title=Wojciech_Marian_Czarnecki&action=edit&redlink=1 "Wojciech Marian Czarnecki (page does not exist)"), [Tom Schaul](index.php?title=Tom_Schaul&action=edit&redlink=1 "Tom Schaul (page does not exist)"), [Joel Z. Leibo](index.php?title=Joel_Z._Leibo&action=edit&redlink=1 "Joel Z. Leibo (page does not exist)"), [David Silver](David_Silver "David Silver"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu") (**2016**). *Reinforcement Learning with Unsupervised Auxiliary Tasks*. [arXiv:1611.05397v1](https://arxiv.org/abs/1611.05397v1)
* [Jane X Wang](index.php?title=Jane_X_Wang&action=edit&redlink=1 "Jane X Wang (page does not exist)"), [Zeb Kurth-Nelson](index.php?title=Zeb_Kurth-Nelson&action=edit&redlink=1 "Zeb Kurth-Nelson (page does not exist)"), [Dhruva Tirumala](index.php?title=Dhruva_Tirumala&action=edit&redlink=1 "Dhruva Tirumala (page does not exist)"), [Hubert Soyer](index.php?title=Hubert_Soyer&action=edit&redlink=1 "Hubert Soyer (page does not exist)"), [Joel Z Leibo](index.php?title=Joel_Z_Leibo&action=edit&redlink=1 "Joel Z Leibo (page does not exist)"), [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos"), [Charles Blundell](index.php?title=Charles_Blundell&action=edit&redlink=1 "Charles Blundell (page does not exist)"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Matthew Botvinick](index.php?title=Matthew_Botvinick&action=edit&redlink=1 "Matthew Botvinick (page does not exist)") (**2016**). *Learning to reinforcement learn*. [arXiv:1611.05763](https://arxiv.org/abs/1611.05763)
* [Zacharias Georgiou](Zacharias_Georgiou "Zacharias Georgiou"), [Evangelos Karountzos](Evangelos_Karountzos "Evangelos Karountzos"), [Yaroslav Shkarupa](Yaroslav_Shkarupa "Yaroslav Shkarupa"), [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli") (**2016**). *A Reinforcement Learning Approach for Solving KRK Chess Endgames*. [pdf](https://github.com/paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames/blob/master/project_papers/final_paper/reinforcement-learning-approach(2).pdf) [[13]](#cite_note-13)


**2017**



* [Hirotaka Kameko](index.php?title=Hirotaka_Kameko&action=edit&redlink=1 "Hirotaka Kameko (page does not exist)"), [Jun Suzuki](index.php?title=Jun_Suzuki&action=edit&redlink=1 "Jun Suzuki (page does not exist)"), [Naoki Mizukami](Naoki_Mizukami "Naoki Mizukami"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka") (**2017**). *Deep Reinforcement Learning with Hidden Layers on Future States*. [Computer Games Workshop at IJCAI 2017](Conferences#IJCA2017 "Conferences"), [pdf](http://www.lamsade.dauphine.fr/~cazenave/cgw2017/Kameko.pdf)
* [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [Audrunas Gruslys](index.php?title=Audrunas_Gruslys&action=edit&redlink=1 "Audrunas Gruslys (page does not exist)"), [Angeliki Lazaridou](index.php?title=Angeliki_Lazaridou&action=edit&redlink=1 "Angeliki Lazaridou (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [Julien Pérolat](index.php?title=Julien_P%C3%A9rolat&action=edit&redlink=1 "Julien Pérolat (page does not exist)"), [David Silver](David_Silver "David Silver"), [Thore Graepel](Thore_Graepel "Thore Graepel") (**2017**). *A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning*. [arXiv:1711.00832](https://arxiv.org/abs/1711.00832)
* [David Silver](David_Silver "David Silver"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Lucas Baker](index.php?title=Lucas_Baker&action=edit&redlink=1 "Lucas Baker (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Adrian Bolton](index.php?title=Adrian_Bolton&action=edit&redlink=1 "Adrian Bolton (page does not exist)"), [Yutian Chen](index.php?title=Yutian_Chen&action=edit&redlink=1 "Yutian Chen (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Fan Hui](index.php?title=Fan_Hui&action=edit&redlink=1 "Fan Hui (page does not exist)"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *[Mastering the game of Go without human knowledge](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 550, [pdf](https://www.gwern.net/docs/rl/2017-silver.pdf) [[14]](#cite_note-14)
* [Peter Henderson](http://www.peterhenderson.co/), [Riashat Islam](https://scholar.google.ca/citations?user=2_4Rs44AAAAJ&hl=en), [Philip Bachman](index.php?title=Philip_Bachman&action=edit&redlink=1 "Philip Bachman (page does not exist)"), [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [Doina Precup](Doina_Precup "Doina Precup"), [David Meger](https://scholar.google.ca/citations?user=gFwEytkAAAAJ&hl=en) (**2017**). *Deep Reinforcement Learning that Matters*. [arXiv:1709.06560](https://arxiv.org/abs/1709.06560)
* [Maithra Raghu](https://scholar.google.com/citations?user=tiE4g64AAAAJ&hl=en), [Alex Irpan](https://scholar.google.com/citations?user=ZZNxNAYAAAAJ&hl=en), [Jacob Andreas](Mathematician#JAndreas "Mathematician"), [Robert Kleinberg](Mathematician#RKleinberg "Mathematician"), [Quoc V. Le](index.php?title=Quoc_V._Le&action=edit&redlink=1 "Quoc V. Le (page does not exist)"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg") (**2017**). *Can Deep Reinforcement Learning Solve Erdos-Selfridge-Spencer Games?* [arXiv:1711.02301](https://arxiv.org/abs/1711.02301)
* [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815) » [AlphaZero](AlphaZero "AlphaZero")
* [Kei Takada](Kei_Takada "Kei Takada"), [Hiroyuki Iizuka](index.php?title=Hiroyuki_Iizuka&action=edit&redlink=1 "Hiroyuki Iizuka (page does not exist)"), [Masahito Yamamoto](index.php?title=Masahito_Yamamoto&action=edit&redlink=1 "Masahito Yamamoto (page does not exist)") (**2017**). *Reinforcement Learning for Creating Evaluation Function Using Convolutional Neural Network in Hex*. [TAAI 2017](index.php?title=TAAI_2017&action=edit&redlink=1 "TAAI 2017 (page does not exist)") » [Hex](Hex "Hex"), [CNN](Neural_Networks#Convolutional "Neural Networks")
* [Ari Weinstein](Ari_Weinstein "Ari Weinstein"), [Matthew Botvinick](index.php?title=Matthew_Botvinick&action=edit&redlink=1 "Matthew Botvinick (page does not exist)") (**2017**). *Structure Learning in Motor Control: A Deep Reinforcement Learning Model*. [arXiv:1706.06827](https://arxiv.org/abs/1706.06827)
* [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Masaaki Tsuchida](https://dblp.org/pers/hd/t/Tsuchida:Masaaki), [Yotaro Watanabe](https://dblp.org/pers/hd/w/Watanabe:Yotaro) (**2017**). *Deep Reinforcement Learning for Inquiry Dialog Policies with Logical Formula Embeddings*. [arXiv:1708.00667](https://arxiv.org/abs/1708.00667)
* [William Uther](William_Uther "William Uther") (**2017**). *[Markov Decision Processes](https://link.springer.com/referenceworkentry/10.1007/978-1-4899-7687-1_512)*. in [Claude Sammut](https://en.wikipedia.org/wiki/Claude_Sammut), [Geoffrey I. Webb](https://en.wikipedia.org/wiki/Geoff_Webb) (eds) (**2017**). *[Encyclopedia of Machine Learning and Data Mining](https://link.springer.com/referencework/10.1007%2F978-1-4899-7687-1)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Jayvant Anantpur](https://scholar.google.com/citations?user=zLksndkAAAAJ&hl=en), [Nagendra Gulur Dwarakanath](https://dblp.org/pid/09/10702.html), [Shivaram Kalyanakrishnan](https://dblp.org/pid/16/4410.html), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [R. Govindarajan](https://dblp.org/pid/45/3592.html) (**2017**). *RLWS: A Reinforcement Learning based GPU Warp Scheduler*. [arXiv:1712.04303](https://arxiv.org/abs/1712.04303)


**2018**



* [Hui Wang](Hui_Wang "Hui Wang"), [Michael Emmerich](index.php?title=Michael_Emmerich&action=edit&redlink=1 "Michael Emmerich (page does not exist)"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2018**). *Monte Carlo Q-learning for General Game Playing*. [arXiv:1802.05944](https://arxiv.org/abs/1802.05944) » [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [General Game Playing](General_Game_Playing "General Game Playing")
* [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [David Raposo](index.php?title=David_Raposo&action=edit&redlink=1 "David Raposo (page does not exist)"), [Adam Santoro](index.php?title=Adam_Santoro&action=edit&redlink=1 "Adam Santoro (page does not exist)"), [Victor Bapst](index.php?title=Victor_Bapst&action=edit&redlink=1 "Victor Bapst (page does not exist)"), [Yujia Li](index.php?title=Yujia_Li&action=edit&redlink=1 "Yujia Li (page does not exist)"), [Igor Babuschkin](index.php?title=Igor_Babuschkin&action=edit&redlink=1 "Igor Babuschkin (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [David P. Reichert](index.php?title=David_P._Reichert&action=edit&redlink=1 "David P. Reichert (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Murray Shanahan](index.php?title=Murray_Shanahan&action=edit&redlink=1 "Murray Shanahan (page does not exist)"), [Victoria Langston](index.php?title=Victoria_Langston&action=edit&redlink=1 "Victoria Langston (page does not exist)"), [Razvan Pascanu](index.php?title=Razvan_Pascanu&action=edit&redlink=1 "Razvan Pascanu (page does not exist)"), [Matthew Botvinick](index.php?title=Matthew_Botvinick&action=edit&redlink=1 "Matthew Botvinick (page does not exist)"), [Oriol Vinyals](index.php?title=Oriol_Vinyals&action=edit&redlink=1 "Oriol Vinyals (page does not exist)"), [Peter W. Battaglia](index.php?title=Peter_W._Battaglia&action=edit&redlink=1 "Peter W. Battaglia (page does not exist)") (**2018**). *Relational Deep Reinforcement Learning*. [arXiv:1806.01830](https://arxiv.org/abs/1806.01830)
* [Hui Wang](Hui_Wang "Hui Wang"), [Michael Emmerich](index.php?title=Michael_Emmerich&action=edit&redlink=1 "Michael Emmerich (page does not exist)"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2018**). *Assessing the Potential of Classical Q-learning in General Game Playing*. [arXiv:1810.06078](https://arxiv.org/abs/1810.06078)
* [Vincent Francois-Lavet](https://scholar.google.com/citations?user=n12uNYcAAAAJ&hl=en), [Peter Henderson](https://scholar.google.com/citations?user=dy_JBs0AAAAJ&hl=en), [Riashat Islam](https://scholar.google.ca/citations?user=2_4Rs44AAAAJ&hl=en), [Marc G. Bellemare](https://scholar.google.com/citations?user=uyYPun0AAAAJ&hl=en), [Joelle Pineau](Joelle_Pineau "Joelle Pineau") (**2018**). *An Introduction to Deep Reinforcement Learning*. [arXiv:1811.12560](https://arxiv.org/abs/1811.12560)
* [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 362, No. 6419 [[15]](#cite_note-15)
* [Tianhe Wang](index.php?title=Tianhe_Wang&action=edit&redlink=1 "Tianhe Wang (page does not exist)"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2018**). *Application of Deep Reinforcement Learning in Werewolf Game Agents*. [TAAI 2018](TAAI_2018 "TAAI 2018")
* [Taichi Nakayashiki](index.php?title=Taichi_Nakayashiki&action=edit&redlink=1 "Taichi Nakayashiki (page does not exist)"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2018**). *Learning of Evaluation Functions via Self-Play Enhanced by Checkmate Search*. [TAAI 2018](TAAI_2018 "TAAI 2018")
* [Hung Guei](index.php?title=Hung_Guei&action=edit&redlink=1 "Hung Guei (page does not exist)"), [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2018**). *Using 2048-like games as a pedagogical tool for reinforcement learning*. [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")


**2019**



* [Sanjeevan Ahilan](https://scholar.google.co.uk/citations?user=OAkRr-YAAAAJ&hl=en), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2019**). *Feudal Multi-Agent Hierarchies for Cooperative Reinforcement Learning*. [arXiv:1901.08492](https://arxiv.org/abs/1901.08492)
* [Chandramouli Kamanchi](https://scholar.google.co.in/citations?user=1QlrvHkAAAAJ&hl=en), [Raghuram Bharadwaj Diddigi](https://scholar.google.co.in/citations?user=nx4NlpsAAAAJ&hl=en), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar") (**2019**). *Successive Over Relaxation Q-Learning*. [arXiv:1903.03812](https://arxiv.org/abs/1903.03812)
* [Chandramouli Kamanchi](https://scholar.google.co.in/citations?user=1QlrvHkAAAAJ&hl=en), [Raghuram Bharadwaj Diddigi](https://scholar.google.co.in/citations?user=nx4NlpsAAAAJ&hl=en), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar") (**2019**). *Second Order Value Iteration in Reinforcement Learning*. [arXiv:1905.03927](https://arxiv.org/abs/1905.03927)
* [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Jean-Baptiste Lespiau](index.php?title=Jean-Baptiste_Lespiau&action=edit&redlink=1 "Jean-Baptiste Lespiau (page does not exist)"), [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [Satyaki Upadhyay](index.php?title=Satyaki_Upadhyay&action=edit&redlink=1 "Satyaki Upadhyay (page does not exist)"), [Julien Pérolat](index.php?title=Julien_P%C3%A9rolat&action=edit&redlink=1 "Julien Pérolat (page does not exist)"), [Sriram Srinivasan](index.php?title=Sriram_Srinivasan&action=edit&redlink=1 "Sriram Srinivasan (page does not exist)"), [Finbarr Timbers](index.php?title=Finbarr_Timbers&action=edit&redlink=1 "Finbarr Timbers (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [Shayegan Omidshafiei](index.php?title=Shayegan_Omidshafiei&action=edit&redlink=1 "Shayegan Omidshafiei (page does not exist)"), [Daniel Hennes](index.php?title=Daniel_Hennes&action=edit&redlink=1 "Daniel Hennes (page does not exist)"), [Dustin Morrill](index.php?title=Dustin_Morrill&action=edit&redlink=1 "Dustin Morrill (page does not exist)"), [Paul Muller](index.php?title=Paul_Muller&action=edit&redlink=1 "Paul Muller (page does not exist)"), [Timo Ewalds](index.php?title=Timo_Ewalds&action=edit&redlink=1 "Timo Ewalds (page does not exist)"), [Ryan Faulkner](index.php?title=Ryan_Faulkner&action=edit&redlink=1 "Ryan Faulkner (page does not exist)"), [János Kramár](index.php?title=J%C3%A1nos_Kram%C3%A1r&action=edit&redlink=1 "János Kramár (page does not exist)"), [Bart De Vylder](index.php?title=Bart_De_Vylder&action=edit&redlink=1 "Bart De Vylder (page does not exist)"), [Brennan Saeta](index.php?title=Brennan_Saeta&action=edit&redlink=1 "Brennan Saeta (page does not exist)"), [James Bradbury](index.php?title=James_Bradbury&action=edit&redlink=1 "James Bradbury (page does not exist)"), [David Ding](index.php?title=David_Ding&action=edit&redlink=1 "David Ding (page does not exist)"), [Sebastian Borgeaud](index.php?title=Sebastian_Borgeaud&action=edit&redlink=1 "Sebastian Borgeaud (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Thomas Anthony](index.php?title=Thomas_Anthony&action=edit&redlink=1 "Thomas Anthony (page does not exist)"), [Edward Hughes](index.php?title=Edward_Hughes&action=edit&redlink=1 "Edward Hughes (page does not exist)"), [Ivo Danihelka](index.php?title=Ivo_Danihelka&action=edit&redlink=1 "Ivo Danihelka (page does not exist)"), [Jonah Ryan-Davis](index.php?title=Jonah_Ryan-Davis&action=edit&redlink=1 "Jonah Ryan-Davis (page does not exist)") (**2019**). *OpenSpiel: A Framework for Reinforcement Learning in Games*. [arXiv:1908.09453](https://arxiv.org/abs/1908.09453) [[16]](#cite_note-16)
* [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Simon Schmitt](index.php?title=Simon_Schmitt&action=edit&redlink=1 "Simon Schmitt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2019**). *Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model*. [arXiv:1911.08265](https://arxiv.org/abs/1911.08265) [[17]](#cite_note-17)
* [Sourabh Bose](Mathematician#SrbhBose "Mathematician") (**2019**). *[Learning Representations Using Reinforcement Learning](https://rc.library.uta.edu/uta-ir/handle/10106/28094)*. Ph.D. thesis, [University of Texas at Arlington](https://en.wikipedia.org/wiki/University_of_Texas_at_Arlington), advisor [Manfred Huber](Mathematician#MHuber "Mathematician") [[18]](#cite_note-18)
* [Johannes Czech](Johannes_Czech "Johannes Czech") (**2019**). *Deep Reinforcement Learning for Crazyhouse*. Master thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/czech2019deep.pdf) » [CrazyAra](CrazyAra "CrazyAra")


### 2020 ...


* [Hung Guei](index.php?title=Hung_Guei&action=edit&redlink=1 "Hung Guei (page does not exist)"), [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2020**). *2048-like games for teaching reinforcement learning*. [ICGA Journal, Vol. 42, No. 1](ICGA_Journal#42_1 "ICGA Journal")
* [Indu John](https://dblp.org/pid/233/8144.html), [Chandramouli Kamanchi](https://scholar.google.co.in/citations?user=1QlrvHkAAAAJ&hl=en), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar") (**2020**). *Generalized Speedy Q-Learning*. [IEEE Control Systems Letters](IEEE#CSL "IEEE"), Vol. 4, No. 3, [arXiv:1911.00397](https://arxiv.org/abs/1911.00397)
* [Takuya Hiraoka](Takuya_Hiraoka "Takuya Hiraoka"), [Takahisa Imagawa](https://dblp.org/pers/hd/i/Imagawa:Takahisa), [Voot Tangkaratt](https://dblp.org/pers/hd/t/Tangkaratt:Voot), [Takayuki Osa](https://dblp.org/pers/hd/o/Osa:Takayuki), [Takashi Onishi](https://dblp.org/pers/hd/o/Onishi:Takashi), [Yoshimasa Tsuruoka](https://dblp.org/pers/hd/t/Tsuruoka:Yoshimasa) (**2020**). *Meta-Model-Based Meta-Policy Optimization*. [arXiv:2006.02608](https://arxiv.org/abs/2006.02608)
* [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Simon Schmitt](index.php?title=Simon_Schmitt&action=edit&redlink=1 "Simon Schmitt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2020**). *[Mastering Atari, Go, chess and shogi by planning with a learned model](https://www.nature.com/articles/s41586-020-03051-4)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 588 [[19]](#cite_note-19) [[20]](#cite_note-20)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Yen-Chi Chen](Yen-Chi_Chen "Yen-Chi Chen"), [Guan-Wei Chen](index.php?title=Guan-Wei_Chen&action=edit&redlink=1 "Guan-Wei Chen (page does not exist)"), [Shi-Yu Chen](index.php?title=Shi-Yu_Chen&action=edit&redlink=1 "Shi-Yu Chen (page does not exist)"), [Xian-Dong Chiu](index.php?title=Xian-Dong_Chiu&action=edit&redlink=1 "Xian-Dong Chiu (page does not exist)"), [Julien Dehos](index.php?title=Julien_Dehos&action=edit&redlink=1 "Julien Dehos (page does not exist)"), [Maria Elsa](index.php?title=Maria_Elsa&action=edit&redlink=1 "Maria Elsa (page does not exist)"), [Qucheng Gong](index.php?title=Qucheng_Gong&action=edit&redlink=1 "Qucheng Gong (page does not exist)"), [Hengyuan Hu](index.php?title=Hengyuan_Hu&action=edit&redlink=1 "Hengyuan Hu (page does not exist)"), [Vasil Khalidov](index.php?title=Vasil_Khalidov&action=edit&redlink=1 "Vasil Khalidov (page does not exist)"), [Cheng-Ling Li](index.php?title=Cheng-Ling_Li&action=edit&redlink=1 "Cheng-Ling Li (page does not exist)"), [Hsin-I Lin](index.php?title=Hsin-I_Lin&action=edit&redlink=1 "Hsin-I Lin (page does not exist)"), [Yu-Jin Lin](index.php?title=Yu-Jin_Lin&action=edit&redlink=1 "Yu-Jin Lin (page does not exist)"), [Xavier Martinet](index.php?title=Xavier_Martinet&action=edit&redlink=1 "Xavier Martinet (page does not exist)"), [Vegard Mella](index.php?title=Vegard_Mella&action=edit&redlink=1 "Vegard Mella (page does not exist)"), [Jeremy Rapin](index.php?title=Jeremy_Rapin&action=edit&redlink=1 "Jeremy Rapin (page does not exist)"), [Baptiste Roziere](index.php?title=Baptiste_Roziere&action=edit&redlink=1 "Baptiste Roziere (page does not exist)"), [Gabriel Synnaeve](index.php?title=Gabriel_Synnaeve&action=edit&redlink=1 "Gabriel Synnaeve (page does not exist)"), [Fabien Teytaud](Fabien_Teytaud "Fabien Teytaud"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Shi-Cheng Ye](index.php?title=Shi-Cheng_Ye&action=edit&redlink=1 "Shi-Cheng Ye (page does not exist)"), [Yi-Jun Ye](index.php?title=Yi-Jun_Ye&action=edit&redlink=1 "Yi-Jun Ye (page does not exist)"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Sergey Zagoruyko](index.php?title=Sergey_Zagoruyko&action=edit&redlink=1 "Sergey Zagoruyko (page does not exist)") (**2020**). *Polygames: Improved zero learning*. [ICGA Journal, Vol. 42, No. 4](ICGA_Journal#42_4 "ICGA Journal"), [arXiv:2001.09832](https://arxiv.org/abs/2001.09832), [arXiv:2001.09832](https://arxiv.org/abs/2001.09832)
* [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli"), [Gilles Louppe](https://github.com/glouppe), [Pierre Geurts](https://scholar.google.com/citations?user=tyFTsmIAAAAJ&hl=en), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2020**). *The Deep Quality-Value Family of Deep Reinforcement Learning Algorithms*. [IJCNN 2020](https://dblp.org/db/conf/ijcnn/ijcnn2020.html#SabatelliLGW20) [[21]](#cite_note-21)
* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)") (**2020**). *Learning to Play Two-Player Perfect-Information Games without Knowledge*. [arXiv:2008.01188](https://arxiv.org/abs/2008.01188)
* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2020**). *Minimax Strikes Back*. [arXiv:2012.10700](https://arxiv.org/abs/2012.10700)


**2021**



* [Maximilian Alexander Gehrke](index.php?title=Maximilian_Alexander_Gehrke&action=edit&redlink=1 "Maximilian Alexander Gehrke (page does not exist)") (**2021**). *Assessing Popular Chess Variants Using Deep Reinforcement Learning*. Master thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/gehrke2021assessing.pdf) » [CrazyAra](CrazyAra "CrazyAra")
* [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[22]](#cite_note-22)
* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2021**). *DESCENT wins five gold medals at the Computer Olympiad*. [ICGA Journal, Vol. 43, No. 2](ICGA_Journal#43_2 "ICGA Journal")
* [Boris Doux](index.php?title=Boris_Doux&action=edit&redlink=1 "Boris Doux (page does not exist)"), [Benjamin Negrevergne](index.php?title=Benjamin_Negrevergne&action=edit&redlink=1 "Benjamin Negrevergne (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2021**). *Deep Reinforcement Learning for Morpion Solitaire*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")
* [Weirui Ye](index.php?title=Weirui_Ye&action=edit&redlink=1 "Weirui Ye (page does not exist)"), [Shaohuai Liu](index.php?title=Shaohuai_Liu&action=edit&redlink=1 "Shaohuai Liu (page does not exist)"), [Thanard Kurutach](index.php?title=Thanard_Kurutach&action=edit&redlink=1 "Thanard Kurutach (page does not exist)"), [Pieter Abbeel](index.php?title=Pieter_Abbeel&action=edit&redlink=1 "Pieter Abbeel (page does not exist)"), [Yang Gao](index.php?title=Yang_Gao&action=edit&redlink=1 "Yang Gao (page does not exist)") (**2021**). *Mastering Atari Games with Limited Data*. [arXiv:2111.00210](https://arxiv.org/abs/2111.00210) [[23]](#cite_note-23) [[24]](#cite_note-24)
* [Dennis Soemers](index.php?title=Dennis_Soemers&action=edit&redlink=1 "Dennis Soemers (page does not exist)"), [Vegard Mella](index.php?title=Vegard_Mella&action=edit&redlink=1 "Vegard Mella (page does not exist)"), [Cameron Browne](Cameron_Browne "Cameron Browne"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2021**). *Deep learning for general game playing with Ludii and Polygames*. [ICGA Journal, Vol. 43, No. 3](ICGA_Journal#43_3 "ICGA Journal")


## Postings


### 1995 ...


* [Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28584) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), October 01, 1998 » [KnightCap](KnightCap "KnightCap")


 [Re: Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28819) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 02, 1998
### 2000 ...


* [Pseudo-code for TD learning](https://www.stmintz.com/ccc/index.php?id=117970) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 06, 2000 » [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")
* [any good experiences with genetic algos or temporal difference learning?](https://www.stmintz.com/ccc/index.php?id=147377) by [Rafael B. Andrist](Rafael_B._Andrist "Rafael B. Andrist"), [CCC](CCC "CCC"), January 01, 2001
* [Temporal Differences](https://www.stmintz.com/ccc/index.php?id=401974) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), December 21, 2004


### 2010 ...


* [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015 » [Deep Learning](Deep_Learning "Deep Learning"), [Giraffe](Giraffe "Giraffe")
* [Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/) by [Tambet Matiisen](http://www.nervanasys.com/author/tambet/), [Nervana](http://www.nervanasys.com/), December 22, 2015
* [Deep Reinforcement Learning with Neon](https://ai.intel.com/deep-reinforcement-learning-with-neon/) by [Tambet Matiisen](http://www.nervanasys.com/author/tambet/), [Nervana](http://www.nervanasys.com/), December 29, 2015
* [Google's AlphaGo team has been working on chess](http://www.talkchess.com/forum/viewtopic.php?t=65909) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [CCC](CCC "CCC"), December 06, 2017 » [AlphaZero](AlphaZero "AlphaZero")
* [Understanding the power of reinforcement learning](http://www.talkchess.com/forum/viewtopic.php?t=65990) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 12, 2017


### 2020 ...


* [Board adaptive / tuning evaluation function - no NN/AI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72810) by Moritz Gedig, [CCC](CCC "CCC"), January 14, 2020
* [Unsupervised reinforcement tuning from zero](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75411) by Madeleine Birchfield, [CCC](CCC "CCC"), October 16, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Transhuman Chess with NN and RL...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75606) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), October 30, 2020 » [NN](Neural_Networks "Neural Networks")
* [Reinforcement learning project](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76465) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 31, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## External Links


### Reinforcement Learning


* [Reinforcement learning from Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning)
* [Reinforcement Learning: An Introduction](http://www.incompleteideas.net/sutton/book/ebook/the-book.html) ebook by [Richard Sutton](Richard_Sutton "Richard Sutton") and [Andrew Barto](Andrew_Barto "Andrew Barto")
* [Reinforcement Learning in Classic Board Games](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching_files/games.pdf) (pdf) by [David Silver](David_Silver "David Silver")
* [Category: Reinforcement Learning - Scholarpedia](http://www.scholarpedia.org/article/Category:Reinforcement_Learning)
* [Reinforcement Learning - Scholarpedia](http://www.scholarpedia.org/article/Reinforcement_learning)
* [Reinforcement Learning and Artificial Intelligence – Faculty of Science](http://spaces.facsci.ualberta.ca/rlai/), [University of Alberta](University_of_Alberta "University of Alberta")


### MDP


* [Markov decision process from Wikipedia](https://en.wikipedia.org/wiki/Markov_decision_process)
* [Partially observable Markov decision process](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process)
* [Reinforcement Learning and POMDPs](http://www.idsia.ch/%7Ejuergen/rl.html) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")


### Q-Learning


* [Q-learning from Wikipedia](https://en.wikipedia.org/wiki/Q-learning)
* [A Painless Q-Learning Tutorial](http://mnemstudio.org/path-finding-q-learning-tutorial.htm)
* [State–action–reward–state–action from Wikipedia](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action)
* [Probably approximately correct learning from Wikipedia](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning)


### Courses


* [Reinforcement Learning Course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html) by [David Silver](David_Silver "David Silver"), [University College London](https://en.wikipedia.org/wiki/University_College_London), 2015, [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


1. [Lecture 1: Introduction to Reinforcement Learning](https://youtu.be/2pWv7GOvuf0)
2. [Lecture 2: Markov Decision Process](https://youtu.be/lfHX2hHRMVQ)
3. [Lecture 3: Planning by Dynamic Programming](https://youtu.be/Nd1-UUMVfz4)
4. [Lecture 4: Model-Free Prediction](https://youtu.be/PnHCvfgC_ZA)
5. [Lecture 5: Model Free Control](https://youtu.be/0g4j2k_Ggc4)
6. [Lecture 6: Value Function Approximation](https://youtu.be/UoPei5o4fps)
7. [Lecture 7: Policy Gradient Methods](https://youtu.be/KHZVXao4qXs)
8. [Lecture 8: Integrating Learning and Planning](https://youtu.be/ItMutbeOHtc)
9. [Lecture 9: Exploration and Exploitation](https://youtu.be/sGuiWX07sKw)
10. [Lecture 10: Classic Games](https://youtu.be/kZ_AUmFcZtk)


* [Introduction to Reinforcement Learning](http://videolectures.net/deeplearning2016_pineau_reinforcement_learning/) by [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [McGill University](McGill_University "McGill University"), 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
### GitHub


* [GitHub - deepmind/open\_spiel: OpenSpiel is a collection of environments and algorithms for research in general reinforcement learning and search/planning in games](https://github.com/deepmind/open_spiel) [[25]](#cite_note-25)
	+ [open\_spiel/open\_spiel/algorithms at master · deepmind/open\_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/algorithms)
		- [open\_spiel/open\_spiel/algorithms/alpha\_zero at master · deepmind/open\_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/algorithms/alpha_zero)
	+ [open\_spiel/open\_spiel/games at master · deepmind/open\_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/games)
		- [open\_spiel/open\_spiel/games/chess at master · deepmind/open\_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/games/chess)
* [GitHub - koulanurag/muzero-pytorch: Pytorch Implementation of MuZero](https://github.com/koulanurag/muzero-pytorch) [[26]](#cite_note-26)
* [GitHub - YeWR/EfficientZero: Open-source codebase for EfficientZero, from "Mastering Atari Games with Limited Data" at NeurIPS 2021](https://github.com/YeWR/EfficientZero) [[27]](#cite_note-27)
* [GitHub - facebookarchive/Polygames: The project is a platform of zero learning with a library of games](https://github.com/facebookarchive/Polygames)


## References


 1. [↑](#cite_ref-1) Example of a simple [Markov decision processes](https://en.wikipedia.org/wiki/Markov_decision_process) with three states (green circles) and two actions (orange circles), with two rewards (orange arrows), [image](https://commons.wikimedia.org/wiki/File:Markov_Decision_Process.svg) by [waldoalvarez](https://commons.wikimedia.org/wiki/User:Waldoalvarez) [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. [↑](#cite_ref-2) [Q-learning from Wikipedia](https://en.wikipedia.org/wiki/Q-learning)
3. [↑](#cite_ref-3) [Chris Watkins](index.php?title=Chris_Watkins&action=edit&redlink=1 "Chris Watkins (page does not exist)"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**1992**). *[Q-learning](http://www.gatsby.ucl.ac.uk/~dayan/papers/wd92.html)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 8, No. 2
4. [↑](#cite_ref-4) [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver"), [Andrei A. Rusu](Mathematician#AARusu "Mathematician"), [Joel Veness](Joel_Veness "Joel Veness"), [Marc G. Bellemare](index.php?title=Marc_G._Bellemare&action=edit&redlink=1 "Marc G. Bellemare (page does not exist)"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Andreas K. Fidjeland](index.php?title=Andreas_K._Fidjeland&action=edit&redlink=1 "Andreas K. Fidjeland (page does not exist)"), [Georg Ostrovski](index.php?title=Georg_Ostrovski&action=edit&redlink=1 "Georg Ostrovski (page does not exist)"), [Stig Petersen](index.php?title=Stig_Petersen&action=edit&redlink=1 "Stig Petersen (page does not exist)"), [Charles Beattie](index.php?title=Charles_Beattie&action=edit&redlink=1 "Charles Beattie (page does not exist)"), [Amir Sadik](index.php?title=Amir_Sadik&action=edit&redlink=1 "Amir Sadik (page does not exist)"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Helen King](index.php?title=Helen_King&action=edit&redlink=1 "Helen King (page does not exist)"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Daan Wierstra](index.php?title=Daan_Wierstra&action=edit&redlink=1 "Daan Wierstra (page does not exist)"), [Shane Legg](index.php?title=Shane_Legg&action=edit&redlink=1 "Shane Legg (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2015**). *[Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 518
5. [↑](#cite_ref-5) [Q-learning from Wikipedia](https://en.wikipedia.org/wiki/Q-learning)
6. [↑](#cite_ref-6) [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1995**). *Temporal Difference Learning and TD-Gammon*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 38, No. 3
7. [↑](#cite_ref-7) [University of Bristol - Department of Computer Science - Technical Reports](http://www.cs.bris.ac.uk/Publications/pub_master.jsp?type=117)
8. [↑](#cite_ref-8) [Ms. Pac-Man from Wikipedia](https://en.wikipedia.org/wiki/Ms._Pac-Man)
9. [↑](#cite_ref-9) [Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/) by [Tambet Matiisen](http://www.nervanasys.com/author/tambet/), [Nervana](http://www.nervanasys.com/), December 22, 2015
10. [↑](#cite_ref-10) [Patent US20150100530 - Methods and apparatus for reinforcement learning - Google Patents](http://www.google.com/patents/US20150100530)
11. [↑](#cite_ref-11) [DeepChess: Another deep-learning based chess program](http://www.talkchess.com/forum/viewtopic.php?t=61748) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), October 17, 2016
12. [↑](#cite_ref-12) [ICANN 2016 | Recipients of the best paper awards](http://icann2016.org/index.php/conference-programme/recipients-of-the-best-paper-awards/)
13. [↑](#cite_ref-13) [GitHub - paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames: Machine Learning - Reinforcement Learning](https://github.com/paintception/A-Reinforcement-Learning-Approach-for-Solving-Chess-Endgames)
14. [↑](#cite_ref-14) [AlphaGo Zero: Learning from scratch](https://deepmind.com/blog/alphago-zero-learning-scratch/) by [Demis Hassabis](Demis_Hassabis "Demis Hassabis") and [David Silver](David_Silver "David Silver"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), October 18, 2017
15. [↑](#cite_ref-15) [AlphaZero: Shedding new light on the grand games of chess, shogi and Go](https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/) by [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") and [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), December 03, 2018
16. [↑](#cite_ref-16) [open\_spiel/contributing.md at master · deepmind/open\_spiel · GitHub](https://github.com/deepmind/open_spiel/blob/master/docs/contributing.md)
17. [↑](#cite_ref-17) [New DeepMind paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72381) by GregNeto, [CCC](CCC "CCC"), November 21, 2019
18. [↑](#cite_ref-18) [e: Board adaptive / tuning evaluation function - no NN/AI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72810&start=6) by Tony P., [CCC](CCC "CCC"), January 15, 2020
19. [↑](#cite_ref-19) [MuZero: Mastering Go, chess, shogi and Atari without rules](https://deepmind.com/blog/article/muzero-mastering-go-chess-shogi-and-atari-without-rules?fbclid=IwAR3mSwrn1YXDKr9uuGm2GlFKh76wBilex7f8QvBiQecwiVmAvD6Bkyjx-rE)
20. [↑](#cite_ref-20) [GitHub - koulanurag/muzero-pytorch: Pytorch Implementation of MuZero](https://github.com/koulanurag/muzero-pytorch)
21. [↑](#cite_ref-21) [GitHub - paintception/Deep-Quality-Value-DQV-Learning-: DQV-Learning: a novel faster synchronous Deep Reinforcement Learning algorithm](https://github.com/paintception/Deep-Quality-Value-DQV-Learning-)
22. [↑](#cite_ref-22) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021
23. [↑](#cite_ref-23) [GitHub - YeWR/EfficientZero: Open-source codebase for EfficientZero, from "Mastering Atari Games with Limited Data" at NeurIPS 2021](https://github.com/YeWR/EfficientZero)
24. [↑](#cite_ref-24) [Want to train nets faster?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78790) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 01, 2021
25. [↑](#cite_ref-25) [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Jean-Baptiste Lespiau](index.php?title=Jean-Baptiste_Lespiau&action=edit&redlink=1 "Jean-Baptiste Lespiau (page does not exist)"), [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [Satyaki Upadhyay](index.php?title=Satyaki_Upadhyay&action=edit&redlink=1 "Satyaki Upadhyay (page does not exist)"), [Julien Pérolat](index.php?title=Julien_P%C3%A9rolat&action=edit&redlink=1 "Julien Pérolat (page does not exist)"), [Sriram Srinivasan](index.php?title=Sriram_Srinivasan&action=edit&redlink=1 "Sriram Srinivasan (page does not exist)"), [Finbarr Timbers](index.php?title=Finbarr_Timbers&action=edit&redlink=1 "Finbarr Timbers (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [Shayegan Omidshafiei](index.php?title=Shayegan_Omidshafiei&action=edit&redlink=1 "Shayegan Omidshafiei (page does not exist)"), [Daniel Hennes](index.php?title=Daniel_Hennes&action=edit&redlink=1 "Daniel Hennes (page does not exist)"), [Dustin Morrill](index.php?title=Dustin_Morrill&action=edit&redlink=1 "Dustin Morrill (page does not exist)"), [Paul Muller](index.php?title=Paul_Muller&action=edit&redlink=1 "Paul Muller (page does not exist)"), [Timo Ewalds](index.php?title=Timo_Ewalds&action=edit&redlink=1 "Timo Ewalds (page does not exist)"), [Ryan Faulkner](index.php?title=Ryan_Faulkner&action=edit&redlink=1 "Ryan Faulkner (page does not exist)"), [János Kramár](index.php?title=J%C3%A1nos_Kram%C3%A1r&action=edit&redlink=1 "János Kramár (page does not exist)"), [Bart De Vylder](index.php?title=Bart_De_Vylder&action=edit&redlink=1 "Bart De Vylder (page does not exist)"), [Brennan Saeta](index.php?title=Brennan_Saeta&action=edit&redlink=1 "Brennan Saeta (page does not exist)"), [James Bradbury](index.php?title=James_Bradbury&action=edit&redlink=1 "James Bradbury (page does not exist)"), [David Ding](index.php?title=David_Ding&action=edit&redlink=1 "David Ding (page does not exist)"), [Sebastian Borgeaud](index.php?title=Sebastian_Borgeaud&action=edit&redlink=1 "Sebastian Borgeaud (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Thomas Anthony](index.php?title=Thomas_Anthony&action=edit&redlink=1 "Thomas Anthony (page does not exist)"), [Edward Hughes](index.php?title=Edward_Hughes&action=edit&redlink=1 "Edward Hughes (page does not exist)"), [Ivo Danihelka](index.php?title=Ivo_Danihelka&action=edit&redlink=1 "Ivo Danihelka (page does not exist)"), [Jonah Ryan-Davis](index.php?title=Jonah_Ryan-Davis&action=edit&redlink=1 "Jonah Ryan-Davis (page does not exist)") (**2019**). *OpenSpiel: A Framework for Reinforcement Learning in Games*. [arXiv:1908.09453](https://arxiv.org/abs/1908.09453)
26. [↑](#cite_ref-26) [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Simon Schmitt](index.php?title=Simon_Schmitt&action=edit&redlink=1 "Simon Schmitt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2020**). *[Mastering Atari, Go, chess and shogi by planning with a learned model](https://www.nature.com/articles/s41586-020-03051-4)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 588
27. [↑](#cite_ref-27) [Weirui Ye](index.php?title=Weirui_Ye&action=edit&redlink=1 "Weirui Ye (page does not exist)"), [Shaohuai Liu](index.php?title=Shaohuai_Liu&action=edit&redlink=1 "Shaohuai Liu (page does not exist)"), [Thanard Kurutach](index.php?title=Thanard_Kurutach&action=edit&redlink=1 "Thanard Kurutach (page does not exist)"), [Pieter Abbeel](index.php?title=Pieter_Abbeel&action=edit&redlink=1 "Pieter Abbeel (page does not exist)"), [Yang Gao](index.php?title=Yang_Gao&action=edit&redlink=1 "Yang Gao (page does not exist)") (**2021**). *Mastering Atari Games with Limited Data*. [arXiv:2111.00210](https://arxiv.org/abs/2111.00210)

**[Up one Level](Learning "Learning")**







 
