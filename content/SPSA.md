---
title: SPSA
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Algorithms](Algorithms "Algorithms") \* SPSA**


**SPSA**, (Simultaneous Perturbation Stochastic Approximation)  

a [stochastic approximation](https://en.wikipedia.org/wiki/Stochastic_approximation) algorithm devised in the late 80s <a id="cite-note-1" href="#cite-ref-1">[1]</a> and 90s by [James C. Spall](James_C._Spall "James C. Spall") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It is an extension of the Finite Difference Stochastic Approximation (**FDSA**) algorithm aka [Kiefer-Wolfowitz algorithm](https://en.wikipedia.org/wiki/Stochastic_approximation#Kiefer-Wolfowitz_algorithm) introduced in 1952 by [Jack Kiefer](Mathematician#JKiefer "Mathematician") and [Jacob Wolfowitz](Mathematician#JWolfowitz "Mathematician") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, on the other hand motivated by the publication of the [Robbins-Monro algorithm](https://en.wikipedia.org/wiki/Stochastic_approximation#Robbins.E2.80.93Monro_algorithm) in 1951 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.


The SPSA algorithm is suited for high-dimensional [optimization problems](https://en.wikipedia.org/wiki/Optimization_problem) giving an [objective function](https://en.wikipedia.org/wiki/Loss_function) of a [p-dimensional](https://en.wikipedia.org/wiki/Dimension) vector of adjustable weights, [Theta](https://en.wikipedia.org/wiki/Theta) or Θ, using a [gradient](https://en.wikipedia.org/wiki/Gradient) [approximation](https://en.wikipedia.org/wiki/Approximation) that requires only N+1 or 2N objective function measurements over all N [iterations](Iteration "Iteration") regardless of the dimension of the optimization problem - opposed to FDSA, which needs p + 1 objective function measurements or simulations per step. At each iteration, a simultaneous [perturbation](https://en.wikipedia.org/wiki/Perturbation_theory) vector with mutually independent zero-mean [random variables](Pseudorandom_Number_Generator "Pseudorandom Number Generator") is generated, a good choice for each delta is the [Rademacher distribution](https://en.wikipedia.org/wiki/Rademacher_distribution) with [probability](https://en.wikipedia.org/wiki/Probability) ½ of being either +1 or -1. Two feature vectors Θ+ and Θ- are calculated by adding and subtracting the delta vector scaled by gain sequence ck to/from the current feature vector Θ, to compare their objective function measurements. Dependent on the outcome and scaled by gain sequences ak and ck, the current feature vector is approximated accordantly. The gain sequences decrease with increasing iterations, converging to 0. The theory pertains to both local optimization and global optimization in the face of multiple local optima <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



## RSPSA


Already at the [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11") conference at [Academia Sinica](https://en.wikipedia.org/wiki/Academia_Sinica), [Taipei](https://en.wikipedia.org/wiki/Taipei), [Taiwan](https://en.wikipedia.org/wiki/Taiwan) in 2005, [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), and [Mark Winands](Mark_Winands "Mark Winands") introduced SPSA for the game programming community and discussed several methods that can be used to enhance its performance, including the use of [common random numbers](https://en.wikipedia.org/wiki/Variance_reduction) and [antithetic variates](https://en.wikipedia.org/wiki/Antithetic_variates), a combination of SPSA with [RPROP](https://en.wikipedia.org/wiki/Rprop) (resilient backpropagation), and the reuse of samples of previous performance evaluations. RPROP, though it was originally worked out for the training of [neural networks](Neural_Networks "Neural Networks"), is applicable to any optimization task where the gradient can be computed or approximated <a id="cite-note-8" href="#cite-ref-8">[8]</a>. The described **RSPSA** (Resilient SPSA) was successfully applied in parameter tuning in the domains of [Poker](index.php?title=Poker&action=edit&redlink=1 "Poker (page does not exist)") and [Lines of Action](Lines_of_Action "Lines of Action") <a id="cite-note-9" href="#cite-ref-9">[9]</a>.



## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [CLOP](CLOP "CLOP")
* [Genetic Algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming")
* [PBIL](Genetic_Programming#PBIL "Genetic Programming")
* [Simulated Annealing](Simulated_Annealing "Simulated Annealing")
* [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")


## Selected Publications


### 1987 ...


* [James C. Spall](James_C._Spall "James C. Spall") (**1987**). *A Stochastic Approximation Technique for Generating Maximum Likelihood Parameter Estimates*. [Proceedings of the American Control Conference](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4789283), [Minneapolis, MN](https://en.wikipedia.org/wiki/Minneapolis), [pdf reprint](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_A_Stochastic_Approximation.PDF)


### 1990 ...


* [James C. Spall](James_C._Spall "James C. Spall") (**1992**). *Multivariate Stochastic Approximation Using a Simultaneous Perturbation Gradient Approximation*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 37, No. 3, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_TAC92.pdf)
* [James C. Spall](James_C._Spall "James C. Spall") (**1997**). *A one-measurement form of SPSA*. [Automatica](http://www.journals.elsevier.com/automatica), Vol. 33, No. 1, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/automatica97_one_measSPSA.pdf)
* [Payman Sadegh](https://www.linkedin.com/in/payman-sadegh-493b372) (**1997**). *Constrained Optimization via Stochastic Approximation with a Simultaneous Perturbation Gradient Approximation*. [Automatica](http://www.journals.elsevier.com/automatica), Vol. 33, No. 5, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Sadegh_Constrained_Optimization.PDF)
* [James C. Spall](James_C._Spall "James C. Spall") (**1998**). *An Overview of the Simultaneous Perturbation Method for Efficient Optimization*. [Johns Hopkins APL Technical Digest](http://www.jhuapl.edu/techdigest/), Vol. 19, No. 4, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_An_Overview.PDF)
* [James C. Spall](James_C._Spall "James C. Spall") (**1998**). *Implementation of the Simultaneous Perturbation Algorithm for Stochastic Optimization*. [IEEE Transactions on Aerospace and Electronic Systems](IEEE#TOCAES "IEEE"), Vol. 34, No. 3, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Implementation_of_the_Simultaneous.PDF)
* [James C. Spall](James_C._Spall "James C. Spall") (**1999**). *Stochastic Optimization: Stochastic Approximation and Simulated Annealing*. in [John G. Webster](https://en.wikipedia.org/wiki/John_G._Webster) (ed.) (**1999**). [Encyclopedia of Electrical and Electronics Engineering](http://onlinelibrary.wiley.com/book/10.1002/047134608X), Vol. 20, [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons), [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Stochastic_Optimization.PDF)


### 2000 ...


* [James C. Spall](James_C._Spall "James C. Spall") (**2000**). *Adaptive Stochastic Approximation by the Simultaneous Perturbation Method*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 45, No. 10, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_TAC00.pdf)
* [László Gerencsé](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=197469), [Stacy D. Hill](http://www.math.buffalo.edu/mad/PEEPS/hill_stacy.html), [Zsuzsanna Vágó](https://itk.ppke.hu/karunkrol/oktatoink-sajat-weboldalai/gerencserne-dr-vago-zsuzsanna-bfd51), Zoltán Vincze (**2004**). *Discrete optimization, SPSA and Markov Chain Monte Carlo methods*. Proceeding of the 2004 American Control Conference, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Gerencser_ACC04.pdf)
* [Stacy D. Hill](http://www.math.buffalo.edu/mad/PEEPS/hill_stacy.html) (**2005**). *Discrete Stochastic Approximation with Application to Resource Allocation*. [Johns Hopkins APL Technical Digest](http://www.jhuapl.edu/techdigest/), Vol. 26, No. 1, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Hill_TechDig05.pdf)
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Mark Winands](Mark_Winands "Mark Winands") (**2005**). *[RSPSA: Enhanced Parameter Optimization in Games](http://link.springer.com/chapter/10.1007/11922155_4)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www.sztaki.hu/~szcsaba/papers/rspsa_acg.pdf), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/RSPSA.pdf)
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2006**). *[Universal Parameter Optimisation in Games Based on SPSA](http://link.springer.com/article/10.1007/s10994-006-6888-8)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Special Issue on Machine Learning and Games, Vol. 63, No. 3, [pdf](http://www.sztaki.hu/~szcsaba/papers/kocsis_acg05.pdf)
* [Mohammed Shahid Abdulla](https://dblp.org/pid/70/382.html), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar") (**2007**). *[Reinforcement Learning Based Algorithms for Average Cost Markov Decision Processes](https://link.springer.com/article/10.1007/s10626-006-0003-y)*. [Discrete Event Dynamic Systems](https://www.springer.com/journal/10626), Vol.17, No.1
* [John L. Maryak](http://dblp.uni-trier.de/pers/hd/m/Maryak:John_L=), [Daniel C. Chin](http://dblp.uni-trier.de/pers/hd/c/Chin:Daniel_C=) (**2008**). *Global Random Optimization by Simultaneous Perturbation Stochastic Approximation*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 53, No. 3, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Maryak_Chin_IEEETAC08.pdf)
* [Qing Song](http://dblp.uni-trier.de/pers/hd/s/Song_0001:Qing), [James C. Spall](James_C._Spall "James C. Spall"), [Yeng Chai Soh](http://dblp.uni-trier.de/pers/hd/s/Soh:Yeng_Chai), [Jie Ni](http://dblp.uni-trier.de/pers/hd/n/Ni:Jie) (**2008**). *Robust Neural Network Tracking Controller Using Simultaneous Perturbation Stochastic Approximation*. [IEEE Transactions on Neural Networks](IEEE#NN "IEEE"), Vol. 19, No. 5, [2003 pdf](https://pdfs.semanticscholar.org/3f2a/4d69ca8adbbc072d82af58b3c750621d36ab.pdf) » [Neural Networks](Neural_Networks "Neural Networks")


### 2010 ...


* [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [H.L. Prasad](https://dblp.org/pid/31/10493.html), [L.A. Prashanth](https://scholar.google.co.in/citations?user=Q1YXWpoAAAAJ&hl=en) (**2013**). *[Stochastic Recursive Algorithms for Optimization: Simultaneous Perturbation Methods](https://link.springer.com/book/10.1007/978-1-4471-4285-0)*. [Lecture Notes in Control and Information Sciences](https://www.springer.com/series/642), Vol. 434, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Qi Wang](index.php?title=Qi_Wang&action=edit&redlink=1 "Qi Wang (page does not exist)") (**2013**). *[Optimization with Discrete Simultaneous Perturbation Stochastic Approximation Using Noisy Loss Function Measurements](https://jscholarship.library.jhu.edu/handle/1774.2/36955)*. Ph.D. thesis, [Johns Hopkins University](https://en.wikipedia.org/wiki/Johns_Hopkins_University), advisor [James C. Spall](James_C._Spall "James C. Spall")
* [Pushpendre Rastogi](https://scholar.google.com/citations?user=nqDASHMAAAAJ), [Jingyi Zhu](http://dblp.uni-trier.de/pers/hd/z/Zhu:Jingyi), [James C. Spall](James_C._Spall "James C. Spall") (**2016**). *Efficient implementation of Enhanced Adaptive Simultaneous Perturbation Algorithms*. [CISS 2016](http://dblp.uni-trier.de/db/conf/ciss/ciss2016.html#RastogiZS16), [pdf](http://www.cs.jhu.edu/~prastog3/res/rastogi2016efficient.pdf)


## Forum Posts


### 2010 ...


* [Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?start=0&t=40662) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), October 07, 2011 » [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")


 [Re: Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?start=0&t=40662&start=6) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), October 07, 2011
* [Tuning again](http://www.talkchess.com/forum/viewtopic.php?t=40964) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 01, 2011
* [Goodbye CLOP, hello SPSA](https://groups.google.com/d/msg/fishcooking/WNrxeXAJ6VI/ZkCnRv4I_qEJ) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 17, 2014 » [CLOP](CLOP "CLOP")
* [Re: Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545&start=2) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 06, 2014 » [PBIL](Genetic_Programming#PBIL "Genetic Programming") <a id="cite-note-10" href="#cite-ref-10">[10]</a>


### 2015 ...


* [Re: A plea to someone](http://www.talkchess.com/forum/viewtopic.php?t=55925&start=10) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [CCC](CCC "CCC"), April 07, 2015


 [Re: A plea to someone](http://www.talkchess.com/forum/viewtopic.php?t=55925&start=21) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 08, 2015
* [Automatic Criterion for stopping SPSA?](https://groups.google.com/d/msg/fishcooking/1FSprH10MpM/bU1bMkqKtaUJ) by tsa..., [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 29, 2015
* [Re: SPSA Tuner](https://groups.google.com/d/msg/fishcooking/mbnctfDdcqM/S_rUOa7177AJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2015
* [Too small number of games in SPSA](https://groups.google.com/d/msg/fishcooking/Np13OpEO1_w/xhYulilABgAJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 22, 2016
* [Self-correcting SPSA tuner for chess engines](https://groups.google.com/d/msg/fishcooking/iyAFOdVx4RE/d4mnJ8lqDgAJ) [Ivan Ivec](index.php?title=Ivan_Ivec&action=edit&redlink=1 "Ivan Ivec (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 04, 2017
* [SPSA problems](http://www.talkchess.com/forum/viewtopic.php?t=63632) by Ralf Müller, [CCC](CCC "CCC"), April 02, 2017
* [SPSA and search.cpp?](https://groups.google.com/d/msg/fishcooking/ERsAux5TU6Q/RU2xnF3bDQAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 06, 2019 » [Stockfish](Stockfish "Stockfish")


### 2020 ...


* [A hybrid of SPSA and local optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77420) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), June 01, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## External Links


* [SPSA Algorithm](https://www.jhuapl.edu/spsa/) by [James C. Spall](James_C._Spall "James C. Spall")
* [Simultaneous perturbation stochastic approximation - Wikipedia](https://en.wikipedia.org/wiki/Simultaneous_perturbation_stochastic_approximation)
* [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski") » [Stockfish](Stockfish "Stockfish")
* [GitHub - lantonov/spsa: Modifications of SPSA](https://github.com/lantonov/SPSA) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov") » [Stockfish](Stockfish "Stockfish")
* [GitHub - jgomezdans/spsa: Simultaneous perturbation stochastic approximation Python code](https://github.com/jgomezdans/spsa)
* [Simultaneous Perturbation Stochastic Approximation code in python · GitHub](https://gist.github.com/yanatan16/5420795)
* [NIPS 2012 Tutoral - Stochastic Search and Optimization](https://youtu.be/kVJQkmYU2VA), [Video Lecture](James_C._Spall#Video "James C. Spall") by [James C. Spall](James_C._Spall "James C. Spall")
* [hr-Bigband](https://en.wikipedia.org/wiki/Hr-Bigband) feat. [Richard Bona](Category:Richard_Bona "Category:Richard Bona") - Kalabancoro, October, 2019, [Hessischer Rundfunk](https://en.wikipedia.org/wiki/Hessischer_Rundfunk), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [James C. Spall](James_C._Spall "James C. Spall") (**1987**). *A Stochastic Approximation Technique for Generating Maximum Likelihood Parameter Estimates*. [Proceedings of the American Control Conference](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4789283), [Minneapolis, MN](https://en.wikipedia.org/wiki/Minneapolis), [pdf reprint](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_A_Stochastic_Approximation.PDF)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [James C. Spall](James_C._Spall "James C. Spall") (**1992**). *Multivariate Stochastic Approximation Using a Simultaneous Perturbation Gradient Approximation*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 37, No. 3
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jack Kiefer](Mathematician#JKiefer "Mathematician"), [Jacob Wolfowitz](Mathematician#JWolfowitz "Mathematician") (**1952**). *[Stochastic Estimation of the Maximum of a Regression Function](https://projecteuclid.org/euclid.aoms/1177729392)*. [The Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 23, No. 3
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Herbert Robbins](Mathematician#HRobbins "Mathematician"), [Sutton Monro](http://articles.mcall.com/1995-03-07/news/3017569_1_burlington-korean-war-memorial-services) (**1951**). *[A Stochastic Approximation Method](https://projecteuclid.org/euclid.aoms/1177729586)*. [The Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 22, No. 3
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [John L. Maryak](http://dblp.uni-trier.de/pers/hd/m/Maryak:John_L=), [Daniel C. Chin](http://dblp.uni-trier.de/pers/hd/c/Chin:Daniel_C=) (**2008**). *Global Random Optimization by Simultaneous Perturbation Stochastic Approximation*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 53, No. 3, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Maryak_Chin_IEEETAC08.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?start=0&t=40662) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), October 07, 2011
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [James C. Spall](James_C._Spall "James C. Spall") (**1998**). *Implementation of the Simultaneous Perturbation Algorithm for Stochastic Optimization*. [IEEE Transactions on Aerospace and Electronic Systems](IEEE#TOCAES "IEEE"), Vol. 34, No. 3, [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Implementation_of_the_Simultaneous.PDF)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Heinrich Braun](index.php?title=Heinrich_Braun&action=edit&redlink=1 "Heinrich Braun (page does not exist)") (**1993**). *A direct adaptive method for faster backpropagation learning: The RPROP algorithm*. [IEEE International Conference On Neural Networks](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=1059), [pdf](http://paginas.fe.up.pt/~ee02162/dissertacao/RPROP%20paper.pdf)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Mark Winands](Mark_Winands "Mark Winands") (**2005**). *[RSPSA: Enhanced Parameter Optimization in Games](http://link.springer.com/chapter/10.1007/11922155_4)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www.sztaki.hu/~szcsaba/papers/rspsa_acg.pdf), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/RSPSA.pdf)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [NOMAD - A blackbox optimization software](https://www.gerad.ca/nomad/Project/Home.html)

**[Up one Level](Algorithms "Algorithms")**







 
