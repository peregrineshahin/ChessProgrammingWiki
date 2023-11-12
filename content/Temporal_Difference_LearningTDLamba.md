---
title: Temporal Difference LearningTDLamba
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* Temporal Difference Learning**


**Temporal Difference Learning**, (TD learning)  

is a machine learning method applied to multi-step prediction problems. As a prediction method primarily used for [reinforcement learning](Reinforcement_Learning "Reinforcement Learning"), TD learning takes into account the fact that subsequent predictions are often correlated in some sense, while in [supervised learning](Supervised_Learning "Supervised Learning"), one learns only from actually observed values. TD resembles [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) with [dynamic programming](Dynamic_Programming "Dynamic Programming") techniques [[1]](#cite_note-1). In the domain of computer games and computer chess, TD learning is applied through self play, subsequently predicting the [probability](https://en.wikipedia.org/wiki/Probability) of winning a [game](Chess_Game "Chess Game") during the sequence of [moves](Moves "Moves") from the [initial position](Initial_Position "Initial Position") until the end, to adjust weights for a more reliable prediction. 



### Contents


* [1 Prediction](#Prediction)
* [2 TD(λ)](#TD.28.CE.BB.29)
* [3 TDLeaf(λ)](#TDLeaf.28.CE.BB.29)
* [4 Quotes](#Quotes)
	+ [4.1 Don Beal](#Don_Beal)
	+ [4.2 Bas Hamstra](#Bas_Hamstra)
	+ [4.3 Don Dailey](#Don_Dailey)
* [5 Chess Programs](#Chess_Programs)
* [6 See also](#See_also)
* [7 Publications](#Publications)
	+ [7.1 1959](#1959)
	+ [7.2 1970 ...](#1970_...)
	+ [7.3 1980 ...](#1980_...)
	+ [7.4 1990 ...](#1990_...)
	+ [7.5 1995 ...](#1995_...)
	+ [7.6 2000 ...](#2000_...)
	+ [7.7 2005 ...](#2005_...)
	+ [7.8 2010 ...](#2010_...)
	+ [7.9 2015 ...](#2015_...)
	+ [7.10 2020 ...](#2020_...)
* [8 Forum Posts](#Forum_Posts)
	+ [8.1 1995 ...](#1995_..._2)
	+ [8.2 2000 ...](#2000_..._2)
	+ [8.3 2010 ...](#2010_..._2)
	+ [8.4 2015 ...](#2015_..._2)
	+ [8.5 2020 ...](#2020_..._2)
* [9 External Links](#External_Links)
* [10 References](#References)






Each prediction is a single number, derived from a formula using adjustable weights of features, for instance a [neural network](Neural_Networks "Neural Networks") most simply a single neuron [perceptron](Neural_Networks#Perceptron "Neural Networks"), that is a linear [evaluation](Evaluation "Evaluation") function ... 



 [](File:TDLForula1.jpg) 
 [](File:SigDeri.jpg) Sigmoid and Derivative 
... with the [pawn advantage](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") converted to a [winning probability](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") by the standard [sigmoid squashing function](https://en.wikipedia.org/wiki/Sigmoid_function), also topic in [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") in the domain of [supervised learning](Supervised_Learning "Supervised Learning") and [automated tuning](Automated_Tuning "Automated Tuning"), ... 



 [](File:TDLForula2.jpg) 
... which has the advantage of its simple [derivative](https://en.wikipedia.org/wiki/Derivative):



 [](File:TDLForula3.jpg) 




## TD(λ)


Each pair of [temporally](https://en.wiktionary.org/wiki/temporal) successive predictions P at time step t and t+1 gives rise to a recommendation for weight changes, to converge Pt to Pt+1, first applied in the late 50s by [Arthur Samuel](Arthur_Samuel "Arthur Samuel") in his [Checkers](Checkers "Checkers") player for [automamated evaluation tuning](Automated_Tuning "Automated Tuning") [[2]](#cite_note-2). This TD method was improved, generalized and formalized by [Richard Sutton](Richard_Sutton "Richard Sutton") et al. in the 80s, the term *Temporal Difference Learning* coined in 1988 [[3]](#cite_note-3), also introducing the decay or recency parameter **λ**, where proportions of the score came from the outcome of [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulated games, tapering between [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping#Artificial_intelligence_and_machine_learning) (λ = 0) and Monte Carlo predictions (λ = 1), the latter equivalent to [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) on the [mean squared error function](https://en.wikipedia.org/wiki/Mean_squared_error). Weight adjustments in TD(λ) are made according to ...



 [](File:TDLForula4.jpg) 
... where P is the series of temporally successive predictions, w the set of adjustable weights. α is a parameter controlling the learning rate, also called step-size, ∇wPk [[4]](#cite_note-4) is the [gradient](https://en.wikipedia.org/wiki/Gradient), the vector of [partial derivatives](https://en.wikipedia.org/wiki/Partial_derivative) of Pt with respect of w. The process may be applied to any initial set of weights. Learning performance depends on λ and α, which have to be chosen appropriately for the domain. In principle, TD(λ) weight adjustments may be made after each move, or at any arbitrary interval. For game playing tasks the end of every game is a convenient point to actually alter the evaluation weights [[5]](#cite_note-5). 


TD(λ) was famously applied by [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") in his [Backgammon](Backgammon "Backgammon") program [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) [[6]](#cite_note-6) [[7]](#cite_note-7), a stochastic game picking the action whose successor state minimizes the opponent's expected reward, i.e. [looking](Search "Search") one [ply](Ply "Ply") ahead.




## TDLeaf(λ)


In games like chess or [Othello](Othello "Othello"), due to their [tactical](Tactics "Tactics") nature, [deep searches](Search "Search") are necessary for expert performance. The problem has already been recognized and solved by [Arthur Samuel](Arthur_Samuel "Arthur Samuel") but seemed to have been forgotten later on [[8]](#cite_note-8) - rediscovered independently by [Don Beal](Don_Beal "Don Beal") and [Martin C. Smith](Martin_C._Smith "Martin C. Smith") in 1997 [[9]](#cite_note-9), and by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), and [Lex Weaver](Lex_Weaver "Lex Weaver") [[10]](#cite_note-10), who coined the term TD-Leaf. TD-Leaf is the adaption of TD(λ) to [minimax](Minimax "Minimax") search, where instead of the corresponding [positions](Chess_Position "Chess Position") of the [root](Root "Root") the [leaf nodes](Leaf_Node "Leaf Node") of the [principal variation](Principal_Variation "Principal Variation") are considered in the weight adjustments. TD-Leaf was successfully used in [evaluation tuning](Automated_Tuning "Automated Tuning") of chess programs [[11]](#cite_note-11), with [KnightCap](KnightCap "KnightCap") [[12]](#cite_note-12) and [CilkChess](CilkChess "CilkChess") as most prominent samples, while the latter used the improved **Temporal Coherence Learning** [[13]](#cite_note-13), which automatically adjusts α and λ [[14]](#cite_note-14).



## Quotes


### Don Beal


[Don Beal](Don_Beal "Don Beal") in a 1998 [CCC](CCC "CCC") discussion with [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter") [[15]](#cite_note-15):




```C++
With fixed learning rates (aka step size) we found [piece values](Point_Value "Point Value") settle to consistent relative ordering in around 500 self-play games. The ordering remains in place despite considerable erratic movements. But [piece-square values](Piece-Square_Tables "Piece-Square Tables") can take a lot longer - more like 5000.

```


```C++
The learning rate is critical - it has to be as large as one dares for fast learning, but low for stable values.  We've been experimenting with methods for automatically adjusting the learning rate. (Higher rates if the adjustments go in the same direction, lower if they keep changing direction.)

```


```C++
The other problem is learning weights for terms which only occur rarely. Then the learning process doesn't see enough examples to settle on good weights in a reasonable time. I suspect this is the main limitation of the method, but it may be possible to devise ways to generate extra games which exercise the rare conditions. 

```

### Bas Hamstra


[Bas Hamstra](Bas_Hamstra "Bas Hamstra") in a 2002 [CCC](CCC "CCC") discussion on TD learning [[16]](#cite_note-16):




```C++
I have played with it. I am convinced it has possibilities, but one problem I encountered was the cause-effect problem. For say I am a piece down. After I lost the game TD will conclude that the winner had better [mobility](Mobility "Mobility") and will tune it up. However worse mobility was not the **cause** of the loss, it was the **effect** of simply being a piece down. In my case it kept tuning mobility up and up until ridiculous values. 

```

### Don Dailey


[Don Dailey](Don_Dailey "Don Dailey") in a reply [[17]](#cite_note-17) to [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 2010 [[18]](#cite_note-18) :




```C++
Another approach that may be more in line with what you want is called "temporal difference learning", and it is based on feedback from each move to the move that precedes it. For example if you play move 35 and the program thinks the position is equal, but then on move 36 you find that you are winning a pawn, it indicates that the evaluation of move 35 is in error, the position is better than the program thought it was. Little tiny incremental adjustments are made to the evaluation function so that it is ever so slightly biased in favor of being slightly more positive in this case, or slightly more negative in the case where you find your score is dropping. This is done recursively back through the moves of the game so that winning the game gives some credit to all the positions of the game. Look on the web and read up on the "credit assignment problem" and temporal difference learning. It's probably ideal for what you are looking for. It can be done at the end of the game one time and scores then updated. If you are not using [floating point](Float "Float") evaluation you may have to figure out how to modify this to be workable. 

```

## Chess Programs


* [CilkChess](CilkChess "CilkChess")
* [EXchess](EXchess "EXchess")
* [FUSc#](FUSCsharp "FUSCsharp")
* [Giraffe](Giraffe "Giraffe")
* [Green Light Chess](Green_Light_Chess "Green Light Chess")
* [KnightCap](KnightCap "KnightCap")
* [Meep](Meep "Meep")


 [RootStrap](Meep#RootStrap "Meep")
 [TreeStrap](Meep#TreeStrap "Meep")
* [Merlin](Merlin_(HU) "Merlin (HU)")
* [Morph](Morph "Morph")
* [NeuroChess](NeuroChess "NeuroChess")
* [SAL](SAL "SAL")
* [Tao](Tao "Tao") [[19]](#cite_note-19)
* [TDChess](TDChess "TDChess")


## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Backgammon](Backgammon "Backgammon")
* [Deep Learning](Deep_Learning "Deep Learning")
* [Evaluation](Evaluation "Evaluation")
* [Neural Networks](Neural_Networks "Neural Networks")


## Publications


### 1959


* [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959


### 1970 ...


* [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1972**). *Brain Function and Adaptive Systems - A Heterostatic Theory*. [Air Force Cambridge Research Laboratories](https://en.wikipedia.org/wiki/Air_Force_Cambridge_Research_Laboratories), Special Reports, No. 133, [pdf](http://www.dtic.mil/dtic/tr/fulltext/u2/742259.pdf)
* [John H. Holland](Mathematician#Holland "Mathematician") (**1975**). *Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence*. [amazon.com](http://www.amazon.com/Adaptation-Natural-Artificial-Systems-Introductory/dp/0262581116)
* [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**1977**). *An Adaptive Optimal Controller for Discrete-Time Markov Environments*. [Information and Control](https://en.wikipedia.org/wiki/Information_and_Computation), Vol. 34, No. 4, [pdf](https://core.ac.uk/download/pdf/82451748.pdf)


### 1980 ...


* [Richard Sutton](Richard_Sutton "Richard Sutton") (**1984**). *[Temporal Credit Assignment in Reinforcement Learning](http://scholarworks.umass.edu/dissertations/AAI8410337/)*. Ph.D. dissertation, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts)
* [Jens Christensen](Jens_Christensen "Jens Christensen") (**1986**). *[Learning Static Evaluation Functions by Linear Regression](http://link.springer.com/chapter/10.1007/978-1-4613-2279-5_9?no-access=true)*. in [Tom Mitchell](Tom_Mitchell "Tom Mitchell"), [Jaime Carbonell](Jaime_Carbonell "Jaime Carbonell"), [Ryszard Michalski](Ryszard_Michalski "Ryszard Michalski") (**1986**). *[Machine Learning: A Guide to Current Research](http://link.springer.com/book/10.1007/978-1-4613-2279-5)*. The Kluwer International Series in Engineering and Computer Science, Vol. 12
* [Richard Sutton](Richard_Sutton "Richard Sutton") (**1988**). *Learning to Predict by the Methods of Temporal Differences*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 3, No. 1
* [Andrew Barto](Andrew_Barto "Andrew Barto"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Christopher J. C. H. Watkins](https://dblp.uni-trier.de/pers/hd/w/Watkins:Christopher_J=_C=_H=) (**1989**). *[Sequential Decision Problems and Neural Networks](https://papers.nips.cc/paper/194-sequential-decision-problems-and-neural-networks)*. [NIPS 1989](https://dblp.uni-trier.de/db/conf/nips/nips1989.html)


### 1990 ...


* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1990**). *Time-Derivative Models of Pavlovian Reinforcement*. in [Michael Gabriel](http://node.realityspline.net/ari/work/neuro/people/showpeople.php?person=faculty/mgabriel.php), [John Moore](http://people.umass.edu/jwmoore/people.htm#JWMoore) (eds.) (**1990**). *Learning and Computational Neuroscience: Foundations of Adaptive Networks*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [pdf](https://webdocs.cs.ualberta.ca/~sutton/papers/sutton-barto-90.pdf)
* [Richard C. Yee](http://dblp.uni-trier.de/pers/hd/y/Yee:Richard_C=), [Sharad Saxena](http://dblp.uni-trier.de/pers/hd/s/Saxena:Sharad), [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1990**). *Explaining Temporal Differences to Create Useful Concepts for Evaluating States*. [AAAI 1990](http://dblp.uni-trier.de/db/conf/aaai/aaai90.html#YeeSUB90), [pdf](http://www.aaai.org/Papers/AAAI/1990/AAAI90-132.pdf)
* [Peter Dayan](Peter_Dayan "Peter Dayan") (**1990**). *[Navigating Through Temporal Difference](https://papers.nips.cc/paper/428-navigating-through-temporal-difference)*. [NIPS 1990](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-3-1990)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
* [Peter Dayan](Peter_Dayan "Peter Dayan") (**1992**). *[The convergence of TD (λ) for general λ](https://www.researchgate.net/publication/227208155_The_Convergence_of_TDl_for_General_l)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 8, No. 3
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *[Practical Issues in Temporal Difference Learning](http://dl.acm.org/citation.cfm?id=139616)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 8, Nos. 3-4
* [Michael Gherrity](Michael_Gherrity "Michael Gherrity") (**1993**). *A Game Learning Machine*. Ph.D. thesis, [University of California, San Diego](https://de.wikipedia.org/wiki/University_of_California,_San_Diego), advisor [Paul Kube](Mathematician#PKube "Mathematician"), [pdf](http://www.gherrity.org/thesis.pdf), [pdf](http://www.top-5000.nl/ps/A%20game%20learning%20machine.pdf)
* [Peter Dayan](Peter_Dayan "Peter Dayan") (**1993**). *Improving generalisation for temporal difference learning: The successor representation*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_(journal)), Vol. 5, [pdf](http://www.gatsby.ucl.ac.uk/~dayan/papers/sr93.pdf)
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph"), [Peter Dayan](Peter_Dayan "Peter Dayan"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1993**). *[Temporal Difference Learning of Position Evaluation in the Game of Go](https://papers.nips.cc/paper/820-temporal-difference-learning-of-position-evaluation-in-the-game-of-go)*. [NIPS 1993](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-6-1993) [[20]](#cite_note-20)
* [Peter Dayan](Peter_Dayan "Peter Dayan"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1994**). *TD(λ) converges with Probability 1*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 14, No. 1, [pdf](https://www.researchgate.net/profile/Terrence_Sejnowski/publication/228392650_TD_X_Converges_with_Probability/links/54a4afea0cf256bf8bb327a9.pdf?origin=publication_detail)


### 1995 ...


* [Anton Leouski](index.php?title=Anton_Leouski&action=edit&redlink=1 "Anton Leouski (page does not exist)") (**1995**). *Learning of Position Evaluation in the Game of Othello*. Master's Project, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts), [Amherst, Massachusetts](https://en.wikipedia.org/wiki/Amherst,_Massachusetts), [pdf](http://people.ict.usc.edu/~leuski/publications/papers/UM-CS-1995-023.pdf)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1995**). *Temporal Difference Learning and TD-Gammon*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 38, No. 3
* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. in [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [David S. Touretzky](https://en.wikipedia.org/wiki/David_S._Touretzky), [Todd K. Leen](http://mitpress.mit.edu/authors/todd-k-leen) (eds.) Advances in Neural Information Processing Systems 7, [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)


**1996**



* [Robert Schapire](Robert_Schapire "Robert Schapire"), [Manfred K. Warmuth](Mathematician#MKWarmuth "Mathematician") (**1996**). *On the Worst-Case Analysis of Temporal-Difference Learning Algorithms*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 22, Nos. 1-3, [pdf](https://users.soe.ucsc.edu/~manfred/pubs/J34.pdf)
* [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**1996**). *Machine Learning in Computer Chess: The Next Generation.* [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal"), [zipped ps](http://www.ofai.at/cgi-bin/get-tr?download=1&paper=oefai-tr-96-11.ps.gz)
* [Steven Bradtke](index.php?title=Steven_Bradtke&action=edit&redlink=1 "Steven Bradtke (page does not exist)"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1996**) *Linear Least-Squares Algorithms for Temporal Difference Learning*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 22, Nos. 1/2/3, [pdf](http://www-anw.cs.umass.edu/pubs/1995_96/bradtke_b_ML96.pdf)


**1997**



* [John N. Tsitsiklis](Mathematician#JNTsitsiklis "Mathematician"), [Benjamin Van Roy](Mathematician#BVanRoy "Mathematician") (**1997**). *[An Analysis of Temporal Difference Learning with Function Approximation](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=bWTPrLEAAAAJ&citation_for_view=bWTPrLEAAAAJ:2osOgNQ5qMEC)*. [IEEE Transactions on Automatic Control](IEEE#TAC "IEEE"), Vol. 42, No. 5
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1997**) *Knightcap: A chess program that learns by combining td(λ) with minimax search*. 15th International Conference on Machine Learning, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.54.8263&rep=rep1&type=pdf) via [citeseerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.8263)


**1998**



* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1998**). *[First Results from Using Temporal Difference Learning in Shogi](http://www.springerlink.com/content/l9f4ngc2tqgnac9e/)*. [CG 1998](CG_1998 "CG 1998")
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Experiments in Parameter Learning Using Temporal Differences*. [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal")
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1998**). *[Reinforcement Learning: An Introduction](http://www.incompleteideas.net/sutton/book/the-book.html)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [6. Temporal-Difference Learning](https://webdocs.cs.ualberta.ca/~sutton/book/ebook/node60.html)
* [Justin A. Boyan](Justin_A._Boyan "Justin A. Boyan") (**1998**). *Least-Squares Temporal Difference Learning*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), CMU-CS-98-152, [pdf](http://www.research.rutgers.edu/~lihong/project/ahlp/boyan99least.pdf)


**1999**



* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1999**). *TDLeaf(lambda): Combining Temporal Difference Learning with Game-Tree Search*. [Australian Journal of Intelligent Information Processing Systems](https://www.chatbots.org/journal/australian_journal_of_intelligent_information_processing_systems/), Vol. 5 No. 1, [arXiv:cs/9901001](http://arxiv.org/abs/cs/9901001)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *[Temporal Coherence and Prediction Decay in TD Learning](http://portal.acm.org/citation.cfm?id=1624299)*. [IJCAI 1999](Conferences#IJCAI1999 "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-99-VOL-1/PDF/081.pdf)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")


### 2000 ...


* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2000**). *A Review of Reinforcement Learning*. [AI Magazine, Vol. 21](http://www.informatik.uni-trier.de/~ley/db/journals/aim/aim21.html#ThrunL00), No. 1, [pdf](http://www.aistudy.com/paper/aaai_journal/AIMag21-01-001.pdf)
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf) » [Morph](Morph "Morph")
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**2000**). *Learning to Play Chess Using Temporal Differences*. [Machine Learning, Vol 40, No. 3](http://www.dblp.org/db/journals/ml/ml40.html#BaxterTW00), [pdf](http://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/chess-RL.pdf)
* [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**). *Machine Learning in Games: A Survey*. [Austrian Research Institute for Artificial Intelligence](https://en.wikipedia.org/wiki/Austrian_Research_Institute_for_Artificial_Intelligence), OEFAI-TR-2000-3, [pdf](http://www.ofai.at/cgi-bin/get-tr?download=1&paper=oefai-tr-2000-31.pdf)


**2001**



* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Markian Hlynka](Markian_Hlynka "Markian Hlynka"), [Vili Jussila](index.php?title=Vili_Jussila&action=edit&redlink=1 "Vili Jussila (page does not exist)") (**2001**). *Temporal Difference Learning Applied to a High-Performance Game-Playing Program*. [IJCAI 2001](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai2001.html#SchaefferHJ01)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**2001**). *[Temporal difference learning applied to game playing and the results of application to Shogi](http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6V1G-41MJ1SV-7&_user=10&_coverDate=02%2F06%2F2001&_rdoc=1&_fmt=high&_orig=search&_sort=d&_docanchor=&view=c&_searchStrId=1436661548&_rerunOrigin=google&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=d855cbad10953476dbb92258347c8e94)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 252, Nos. 1-2
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph"), [Peter Dayan](Peter_Dayan "Peter Dayan"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**2001**). *[Learning to Evaluate Go Positions via Temporal Difference Methods](https://link.springer.com/chapter/10.1007/978-3-7908-1833-8_4)*. [Computational Intelligence in Games, Studies in Fuzziness and Soft Computing](http://jasss.soc.surrey.ac.uk/7/1/reviews/takama.html). [Physica-Verlag](http://www.springer.com/economics?SGWID=1-165-6-73481-0), [pdf](https://papers.cnl.salk.edu/PDFs/Learning%20to%20Evaluate%20Go%20Positions%20Via%20Temporal%20Difference%20Methods%202001-3244.pdf)
* [Lex Weaver](Lex_Weaver "Lex Weaver"), [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter") (**2001**). *STD (λ): learning state differences with TD (λ)*. [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.20.7737)


**2002**



* [Ari Shapiro](index.php?title=Ari_Shapiro&action=edit&redlink=1 "Ari Shapiro (page does not exist)"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2002**). *[Learning a Game Strategy Using Pattern-Weights and Self-play](http://www.arishapiro.com/researchportfolio/Learning%20Game%20Strategy/index.htm)*. [CG 2002](CG_2002 "CG 2002"), [pdf](http://www.arishapiro.com//ShapiroA_CG2002.pdf)
* [Mark Winands](Mark_Winands "Mark Winands"), [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *Temporal difference learning and the Neural MoveMap heuristic in the game of Lines of Action*. GAME-ON 2002 » [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
* [James Swafford](James_Swafford "James Swafford") (**2002**). *Optimizing Parameter Learning using Temporal Differences*. [AAAI-02](http://www.aaai.org/Conferences/AAAI/aaai02.php), Student Abstracts, [pdf](https://www.aaai.org/Papers/AAAI/2002/AAAI02-150.pdf)
* [Justin A. Boyan](Justin_A._Boyan "Justin A. Boyan") (**2002**). *[Technical Update: Least-Squares Temporal Difference Learning](https://link.springer.com/article/10.1023%2FA%3A1017936530646)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_(journal)), Vol. 49, [pdf](http://research.cs.rutgers.edu/~lihong/project/ahlp/boyan02least.pdf)
* [Don Beal](Don_Beal "Don Beal") (**2002**). *[TD(µ): A Modification of TD(λ) That Enables a Program to Learn Weights for Good Play Even if It Observes Only Bad Play](https://www.researchgate.net/publication/221556841_TD_mu_A_Modificaiton_of_TD_lambda_That_Enables_a_Program_to_Learn_Weights_for_Good_Play_Even_if_It_Observes_Only_Bad_Play)*. [JCIS 2002](https://dblp.org/db/conf/jcis/jcis2002)


**2003**



* [Henk Mannen](Henk_Mannen "Henk Mannen") (**2003**). *Learning to play chess using reinforcement learning with database games*. Master’s thesis, Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), [pdf](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.109.810&rep=rep1&type=pdf)
* [Henk Mannen](Henk_Mannen "Henk Mannen"), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2004**). *[Learning to play chess using TD(λ)-learning with database games](https://www.semanticscholar.org/paper/Learning-to-Play-Chess-using-TD(lambda)-learning-Mannen-Wiering/00a6f81c8ebe8408c147841f26ed27eb13fb07f3)*. Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), Benelearn’04, [pdf](https://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/learning-chess.pdf)
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz") (**2004**). *Verwendung von Temporale-Differenz-Methoden im Schachmotor FUSc#*. Diplomarbeit, Betreuer: [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), [pdf](http://page.mi.fu-berlin.de/block/Skripte/diplomarbeit.pdf) (German)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Daniel Osman](index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2004**). *Temporal Difference Approach to Playing Give-Away Checkers*. [ICAISC 2004](http://www.informatik.uni-trier.de/~ley/db/conf/icaisc/icaisc2004.html#MandziukO04), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/ICAISC04-3.pdf)
* [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Luc De Raedt](Mathematician#LDRaedt "Mathematician") (**2004**). *[Logical Markov Decision Programs and the Convergence of Logical TD(lambda)](https://lirias.kuleuven.be/1992259?limo=0)*. [ILP 2004](https://dblp.org/db/conf/ilp/ilp2004.html#KerstingR04), [pdf](http://people.csail.mit.edu/kersting/papers/ilp04.pdf)


### 2005 ...


* [Marco Wiering](Marco_Wiering "Marco Wiering"), [Jan Peter Patist](http://dblp.uni-trier.de/pers/hd/p/Patist:Jan_Peter), [Henk Mannen](Henk_Mannen "Henk Mannen") (**2005**). *Learning to Play Board Games using Temporal Difference Methods*. Technical Report, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), UU-CS-2005-048, [pdf](http://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/learning_games_TR.pdf)
* [Thomas Philip Runarsson](Thomas_Philip_Runarsson "Thomas Philip Runarsson"), [Simon Lucas](Simon_Lucas "Simon Lucas") (**2005**). *Coevolution versus self-play temporal difference learning for acquiring position evaluation in small-board go*. [IEEE Transactions on Evolutionary Computation](IEEE#EC "IEEE"), Vol. 9, No. 6


**2006**



* [Simon Lucas](Simon_Lucas "Simon Lucas"), [Thomas Philip Runarsson](Thomas_Philip_Runarsson "Thomas Philip Runarsson") (**2006**). *[Temporal Difference Learning versus Co-Evolution for Acquiring Othello Position Evaluation](http://scholar.google.is/citations?view_op=view_citation&hl=en&user=4eWdc_sAAAAJ&citation_for_view=4eWdc_sAAAAJ:qjMakFHDy7sC)*. [CIG 2006](IEEE#CIG "IEEE")


**2007**



* [Edward P. Manning](index.php?title=Edward_P._Manning&action=edit&redlink=1 "Edward P. Manning (page does not exist)") (**2007**). *[Temporal Difference Learning of an Othello Evaluation Function for a Small Neural Network with Shared Weights](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=4219046)*. [IEEE Symposium on Computational Intelligence and AI in Games](IEEE#CIG "IEEE")
* [Daniel Osman](index.php?title=Daniel_Osman&action=edit&redlink=1 "Daniel Osman (page does not exist)") (**2007**). *Temporal Difference Methods for Two-player Board Games*. Ph.D. thesis, Faculty of Mathematics and Information Science, [Warsaw University of Technology](https://en.wikipedia.org/wiki/Warsaw_University_of_Technology)
* [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2007**). *Reinforcement Learning of Evaluation Functions Using Temporal Difference-Monte Carlo learning method*. [12th Game Programming Workshop](Conferences#GPW "Conferences")
* [Andrew Barto](Andrew_Barto "Andrew Barto") (**2007**). *[Temporal difference learning](http://www.scholarpedia.org/article/Temporal_difference_learning)*. [Scholarpedia](https://en.wikipedia.org/wiki/Scholarpedia) 2(11):1604


**2008**



* [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2008**). *An Othello Evaluation Function Based on Temporal Difference Learning using Probability of Winning*. [CIG'08](http://www.csse.uwa.edu.au/cig08/Proceedings/toc.html), [pdf](http://www.csse.uwa.edu.au/cig08/Proceedings/papers/8010.pdf)
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Hamid Reza Maei](Hamid_Reza_Maei "Hamid Reza Maei") (**2008**). *A Convergent O(n) Algorithm for Off-policy Temporal-difference Learning with Linear Function Approximation*. [NIPS 2008](https://dblp.uni-trier.de/db/conf/nips/nips2008.html#SuttonSM08), [pdf](https://proceedings.neurips.cc/paper/2008/file/e0c641195b27425bb056ac56f8953d24-Paper.pdf)
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning of Piece Values for Chess Variants.* Technical Report TUD–KE–2008-07, Knowledge Engineering Group, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ke.tu-darmstadt.de/publications/reports/tud-ke-2008-07.pdf)
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning the Piece Values for three Chess Variants*. [ICGA Journal, Vol. 31, No. 4](ICGA_Journal#31_4 "ICGA Journal")
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)
* [Albrecht Fiebiger](index.php?title=Albrecht_Fiebiger&action=edit&redlink=1 "Albrecht Fiebiger (page does not exist)") (**2008**). *Einsatz von allgemeinen Evaluierungsheuristiken in Verbindung mit der Reinforcement-Learning-Strategie in der Schachprogrammierung*. [Besondere Lernleistung](https://de.wikipedia.org/wiki/Besondere_Lernleistung) im [Fachbereich](https://de.wikipedia.org/wiki/Fachgebiet) [Informatik](https://de.wikipedia.org/wiki/Informatik), [Sächsischees Landesgymnasium Sankt Afra](https://en.wikipedia.org/wiki/Federal_School_of_Saxony%E2%80%93Saint_Afra), Internal advisor: Ralf Böttcher, External advisors: [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), [pdf](http://page.mi.fu-berlin.de/block/abschlussarbeiten/Fiebiger_BeLL.pdf) (German)


**2009**



* [Hamid Reza Maei](Hamid_Reza_Maei "Hamid Reza Maei"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [Doina Precup](Doina_Precup "Doina Precup"), [David Silver](David_Silver "David Silver"), [Richard Sutton](Richard_Sutton "Richard Sutton") (**2009**). *Convergent Temporal-Difference Learning with Arbitrary Smooth Function Approximation*. [NIPS 2009](https://dblp.uni-trier.de/db/conf/nips/nips2009.html#MaeiSBPSS09), [pdf](https://papers.nips.cc/paper/2009/file/3a15c7d0bbe60300a39f76f8a5ba6896-Paper.pdf)
* [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. NIPS 2009, [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf)
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Hamid Reza Maei](Hamid_Reza_Maei "Hamid Reza Maei"), [Doina Precup](Doina_Precup "Doina Precup"), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [David Silver](David_Silver "David Silver"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Eric Wiewiora](index.php?title=Eric_Wiewiora&action=edit&redlink=1 "Eric Wiewiora (page does not exist)"). (**2009**). *[Fast Gradient-Descent Methods for Temporal-Difference Learning with Linear Function Approximation](https://dl.acm.org/doi/10.1145/1553374.1553501)*. [ICML 2009](https://dblp.uni-trier.de/db/conf/icml/icml2009.html#SuttonMPBSSW09)
* [Simon Lucas](Simon_Lucas "Simon Lucas") (**2009**). *[Temporal difference learning with interpolated table value functions](https://ieeexplore.ieee.org/document/5286496)*. [CIG 2009](IEEE#CIG "IEEE")
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2009**). *Coevolutionary Temporal Difference Learning for Othello*. [GIG 2009](IEEE#CIG "IEEE"), [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/papers/szubert09coevolutionary.pdf)
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2009**). *Coevolutionary Reinforcement Learning and its Application to Othello*. M.Sc. thesis, [Poznań University of Technology](https://en.wikipedia.org/wiki/Pozna%C5%84_University_of_Technology), supervisor [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [pdf](https://mszubert.github.io/papers/Szubert_2009_MSC.pdf)
* [J. Zico Kolter](http://www.cs.cmu.edu/~zkolter/), [Andrew Ng](index.php?title=Andrew_Ng&action=edit&redlink=1 "Andrew Ng (page does not exist)") (**2009**). *Regularization and Feature Selection in Least-Squares Temporal Difference Learning*. [ICML 2009](http://www.machinelearning.org/archive/icml2009/), [pdf](http://www.cs.cmu.edu/~zkolter/pubs/kolter-icml09b-full.pdf)


### 2010 ...


* [Marco Wiering](Marco_Wiering "Marco Wiering") (**2010**). *Self-play and using an expert to learn to play backgammon with temporal difference learning*. [Journal of Intelligent Learning Systems and Applications](http://www.scirp.org/journal/jilsa/), Vol. 2, No. 2
* [Hamid Reza Maei](Hamid_Reza_Maei "Hamid Reza Maei"), [Richard Sutton](Richard_Sutton "Richard Sutton") (**2010**). *[GQ(λ): A general gradient algorithm for temporal-difference prediction learning with eligibility traces](https://www.researchgate.net/publication/215990384_GQlambda_A_general_gradient_algorithm_for_temporal-difference_prediction_learning_with_eligibility_traces)*. [AGI 2010](https://agi-conf.org/2010/)
* [Hamid Reza Maei](Hamid_Reza_Maei "Hamid Reza Maei") (**2011**). *[Gradient Temporal-Difference Learning Algorithms](https://era.library.ualberta.ca/items/fd55edcb-ce47-4f84-84e2-be281d27b16a)*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), advisor [Richard Sutton](Richard_Sutton "Richard Sutton")
* [Joel Veness](Joel_Veness "Joel Veness") (**2011**). *Approximate Universal Artificial Intelligence and Self-Play Learning for Games*. Ph.D. thesis, [University of New South Wales](https://en.wikipedia.org/wiki/University_of_New_South_Wales), supervisors: [Kee Siong Ng](index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter"), [Alan Blair](Alan_Blair "Alan Blair"), [William Uther](William_Uther "William Uther"), [John Lloyd](index.php?title=John_Lloyd&action=edit&redlink=1 "John Lloyd (page does not exist)"); [pdf](http://jveness.info/publications/veness_phd_thesis_final.pdf)
* [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hsin-Ti Tsai](index.php?title=Hsin-Ti_Tsai&action=edit&redlink=1 "Hsin-Ti Tsai (page does not exist)"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Yi-Shan Lin](index.php?title=Yi-Shan_Lin&action=edit&redlink=1 "Yi-Shan Lin (page does not exist)"), [Chieh-Min Chang](index.php?title=Chieh-Min_Chang&action=edit&redlink=1 "Chieh-Min Chang (page does not exist)"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2011**). *[Temporal Difference Learning for Connect6](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=5)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2011**). *[Improving Temporal Difference Performance in Backgammon Variants](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=5)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](http://ai.uom.gr/nikpapa/publications/Improving%20Temporal%20Difference%20Learning%20in%20Backgammon%20Variants_ACG13.pdf)
* [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2011**). *[Evolving small-board Go players using Coevolutionary Temporal Difference Learning with Archives](http://www.degruyter.com/view/j/amcs.2011.21.issue-4/v10006-011-0057-3/v10006-011-0057-3.xml)*. [Applied Mathematics and Computer Science](http://www.degruyter.com/view/j/amcs), Vol. 21, No. 4
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2011**). *Learning Board Evaluation Function for Othello by Hybridizing Coevolution with Temporal Difference Learning*. [Control and Cybernetics](http://control.ibspan.waw.pl:3000/mainpage), Vol. 40, No. 3, [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/papers/szubert2011learning.pdf)
* [István Szita](Istv%C3%A1n_Szita "István Szita") (**2012**). *[Reinforcement Learning in Games](http://link.springer.com/chapter/10.1007%2F978-3-642-27645-3_17)*. in [Marco Wiering](Marco_Wiering "Marco Wiering"), [Martijn Van Otterlo](http://martijnvanotterlo.nl/) (eds.). *Reinforcement learning: State-of-the-art*. [Adaptation, Learning, and Optimization, Vol. 12](http://link.springer.com/book/10.1007/978-3-642-27645-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [David Silver](David_Silver "David Silver"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Martin Mueller](Martin_M%C3%BCller "Martin Müller") (**2013**). *Temporal-Difference Search in Computer Go*. Proceedings of the [ICAPS-13 Workshop on Planning and Learning](http://icaps13.icaps-conference.org/technical-program/workshop-program/planning-and-learning/), [pdf](http://webdocs.cs.ualberta.ca/~sutton/papers/SSM-ICAPS-13.pdf)
* [Florian Kunz](index.php?title=Florian_Kunz&action=edit&redlink=1 "Florian Kunz (page does not exist)") (**2013**). *An Introduction to Temporal Difference Learning*. Seminar on Autonomous Learning Systems, [TU Darmstad](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ausy.informatik.tu-darmstadt.de/uploads/Teaching/AutonomousLearningSystems/Kunz_ALS_2013.pdf)
* [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Kun-Hao Yeh](Kun-Hao_Yeh "Kun-Hao Yeh"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [Chia-Chuan Chang](index.php?title=Chia-Chuan_Chang&action=edit&redlink=1 "Chia-Chuan Chang (page does not exist)"), [Han Chiang](index.php?title=Han_Chiang&action=edit&redlink=1 "Han Chiang (page does not exist)") (**2014**). *Multi-Stage Temporal Difference Learning for 2048*. [TAAI 2014](index.php?title=TAAI_2014&action=edit&redlink=1 "TAAI 2014 (page does not exist)")
* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski") (**2014**). *Multi-Criteria Comparison of Coevolution and Temporal Difference Learning on Othello*. [EvoApplications 2014](http://www.evostar.org/2014/), [Springer, volume 8602](http://www.springer.com/computer/theoretical+computer+science/book/978-3-662-45522-7)


### 2015 ...


* [James L. McClelland](index.php?title=James_L._McClelland&action=edit&redlink=1 "James L. McClelland (page does not exist)") (**2015**). *[Explorations in Parallel Distributed Processing: A Handbook of Models, Programs, and Exercises](https://web.stanford.edu/group/pdplab/pdphandbook/handbook3.html#handbookch10.html)*. Second Edition, [Contents](https://web.stanford.edu/group/pdplab/pdphandbook/handbookli1.html), [Temporal-Difference Learning](https://web.stanford.edu/group/pdplab/pdphandbook/handbookch10.html)
* [Matthew Lai](Matthew_Lai "Matthew Lai") (**2015**). *Giraffe: Using Deep Reinforcement Learning to Play Chess*. M.Sc. thesis, [Imperial College London](https://en.wikipedia.org/wiki/Imperial_College_London), [arXiv:1509.01549v1](http://arxiv.org/abs/1509.01549v1) » [Giraffe](Giraffe "Giraffe")
* [Markus Thill](index.php?title=Markus_Thill&action=edit&redlink=1 "Markus Thill (page does not exist)") (**2015**). *Temporal Difference Learning Methods with Automatic Step-Size Adaption for Strategic Board Games: Connect-4 and Dots-and-Boxes*. Master thesis, [Technical University of Cologne](https://en.wikipedia.org/wiki/Technical_University_of_Cologne), Campus Gummersbach, [pdf](http://www.gm.fh-koeln.de/~konen/research/PaperPDF/MT-Thill2015-final.pdf)
* [Kazuto Oka](index.php?title=Kazuto_Oka&action=edit&redlink=1 "Kazuto Oka (page does not exist)"), [Kiminori Matsuzaki](index.php?title=Kiminori_Matsuzaki&action=edit&redlink=1 "Kiminori Matsuzaki (page does not exist)") (**2016**). *Systematic Selection of N-tuple Networks for 2048*. [CG 2016](CG_2016 "CG 2016")
* [Huizhen Yu](index.php?title=Huizhen_Yu&action=edit&redlink=1 "Huizhen Yu (page does not exist)"), [A. Rupam Mahmood](index.php?title=A._Rupam_Mahmood&action=edit&redlink=1 "A. Rupam Mahmood (page does not exist)"), [Richard Sutton](Richard_Sutton "Richard Sutton") (**2017**). *On Generalized Bellman Equations and Temporal-Difference Learning*. Canadian Conference on AI 2017, [arXiv:1704.04463](https://arxiv.org/abs/1704.04463)
* [William Uther](William_Uther "William Uther") (**2017**). *[Temporal Difference Learning](https://link.springer.com/referenceworkentry/10.1007/978-1-4899-7687-1_817)*. in [Claude Sammut](https://en.wikipedia.org/wiki/Claude_Sammut), [Geoffrey I. Webb](https://en.wikipedia.org/wiki/Geoff_Webb) (eds) (**2017**). *[Encyclopedia of Machine Learning and Data Mining](https://link.springer.com/referencework/10.1007%2F978-1-4899-7687-1)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


### 2020 ...


* [Emmanuel Bengio](https://scholar.google.ca/citations?user=yVtSOt8AAAAJ&hl=en), [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [Doina Precup](Doina_Precup "Doina Precup") (**2020**). *Interference and Generalization in Temporal Difference Learning*. [arXiv:2003.06350](https://arxiv.org/abs/2003.06350)
* [Joshua Romoff](https://scholar.google.ca/citations?user=4C5wrXIAAAAJ&hl=en), [Peter Henderson](https://scholar.google.com/citations?user=dy_JBs0AAAAJ&hl=en), [David Kanaa](https://scholar.google.com/citations?user=HUmLDxcAAAAJ&hl=en), [Emmanuel Bengio](https://scholar.google.ca/citations?user=yVtSOt8AAAAJ&hl=en), [Ahmed Touati](https://scholar.google.com/citations?user=D4LT5xAAAAAJ&hl=en), [Pierre-Luc Bacon](https://scholar.google.ca/citations?user=9H77FYYAAAAJ&hl=en), [Joelle Pineau](Joelle_Pineau "Joelle Pineau") (**2020**). *TDprop: Does Jacobi Preconditioning Help Temporal Difference Learning?* [arXiv:2007.02786](https://arxiv.org/abs/2007.02786)


## Forum Posts


### 1995 ...


* [Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28584) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), October 01, 1998 » [KnightCap](KnightCap "KnightCap")


 [Re: Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28819) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 02, 1998
### 2000 ...


* [Pseudo-code for TD learning](https://www.stmintz.com/ccc/index.php?id=117970) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 06, 2000
* [any good experiences with genetic algos or temporal difference learning?](https://www.stmintz.com/ccc/index.php?id=147377) by [Rafael B. Andrist](Rafael_B._Andrist "Rafael B. Andrist"), [CCC](CCC "CCC"), January 01, 2001
* [Temporal Difference](https://www.stmintz.com/ccc/index.php?id=148342) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), January 05, 2001
* [Tao update](https://www.stmintz.com/ccc/index.php?id=149645) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), January 12, 2001 » [Tao](Tao "Tao")
* [Re: Parameter Learning Using Temporal Differences !](https://www.stmintz.com/ccc/index.php?id=218650) by [Aaron Tay](Aaron_Tay "Aaron Tay"), [CCC](CCC "CCC"), March 19, 2002
* [Hello from Edmonton (and on Temporal Differences)](https://www.stmintz.com/ccc/index.php?id=243354) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), July 30, 2002
* [Temporal Differences](https://www.stmintz.com/ccc/index.php?id=394403) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), November 03, 2004


 [Re: Temporal Differences](https://www.stmintz.com/ccc/index.php?id=394440) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), November 04, 2004 [[21]](#cite_note-21)
* [Temporal Differences](https://www.stmintz.com/ccc/index.php?id=401974) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), December 21, 2004
* [Chess program improvement project (copy at TalkChess/ICD)](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4467&p=23234) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 07, 2006 » [Win at Chess](Win_at_Chess "Win at Chess")


### 2010 ...


* [Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062) by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 13, 2010


 [Re: Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062&start=2) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 13, 2010
* [Pawn Advantage, Win Percentage, and Elo](http://www.talkchess.com/forum/viewtopic.php?t=43323) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 15, 2012


 [Re: Pawn Advantage, Win Percentage, and Elo](http://www.talkchess.com/forum/viewtopic.php?t=43323&start=3) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), April 15, 2012
### 2015 ...


* [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015 » [Deep Learning](Deep_Learning "Deep Learning"), [Giraffe](Giraffe "Giraffe")
* [td-leaf](http://www.talkchess.com/forum/viewtopic.php?t=57860) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), October 06, 2015 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [TD-leaf(lambda)](http://www.talkchess.com/forum/viewtopic.php?t=62053) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), November 09, 2016
* [TD(1)](https://www.game-ai-forum.org/viewtopic.php?f=21&t=695) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [Game-AI Forum](Computer_Chess_Forums "Computer Chess Forums"), November 20, 2019 » [Automated Tuning](Automated_Tuning "Automated Tuning")


### 2020 ...


* [Board adaptive / tuning evaluation function - no NN/AI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72810) by Moritz Gedig, [CCC](CCC "CCC"), January 14, 2020
* [TD learning by self play (TD-Gammon)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77053) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), April 10, 2021


## External Links


* [Temporal difference learning from Wikipedia](https://en.wikipedia.org/wiki/Temporal_difference_learning)


 [temporal - Wiktionary](https://en.wiktionary.org/wiki/temporal)
* [Reinforcement learning - Temporal difference methods from Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning#Temporal_difference_methods)
* [Standing on the shoulders of giants](https://en.chessbase.com/post/standing-on-the-shoulders-of-giants) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 18, 2019
* [Shawn Lane](Category:Shawn_Lane "Category:Shawn Lane"), [Jonas Hellborg](Category:Jonas_Hellborg "Category:Jonas Hellborg"), [Jeff Sipe](Category:Jeff_Sipe "Category:Jeff Sipe") - [Temporal Analogues of Paradise](https://en.wikipedia.org/wiki/Temporal_Analogues_of_Paradise), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Temporal difference learning from Wikipedia](https://en.wikipedia.org/wiki/Temporal_difference_learning)
2. [↑](#cite_ref-2)  [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959
3. [↑](#cite_ref-3) [Richard Sutton](Richard_Sutton "Richard Sutton") (**1988**). *Learning to Predict by the Methods of Temporal Differences*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 3, No. 1, [pdf](https://webdocs.cs.ualberta.ca/~sutton/papers/sutton-88-with-erratum.pdf)
4. [↑](#cite_ref-4) [Nabla symbol from Wikipedia](https://en.wikipedia.org/wiki/Nabla_symbol)
5. [↑](#cite_ref-5) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1998**). *[First Results from Using Temporal Difference Learning in Shogi](http://www.springerlink.com/content/l9f4ngc2tqgnac9e/)*. [CG 1998](CG_1998 "CG 1998")
6. [↑](#cite_ref-6) [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
7. [↑](#cite_ref-7) [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1994**). *TD-Gammon, a Self-Teaching Backgammon Program, Achieves Master-Level Play*. [Neural Computation Vol. 6, No. 2](http://www.informatik.uni-trier.de/~ley/db/journals/neco/neco6.html#Tesauro94)
8. [↑](#cite_ref-8) [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning of Piece Values for Chess Variants.* Technical Report TUD–KE–2008-07, Knowledge Engineering Group, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ke.tu-darmstadt.de/publications/reports/tud-ke-2008-07.pdf)
9. [↑](#cite_ref-9) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
10. [↑](#cite_ref-10) [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1997**) *Knightcap: A chess program that learns by combining td(λ) with minimax search*. 15th International Conference on Machine Learning, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.54.8263&rep=rep1&type=pdf) via [citeseerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.8263)
11. [↑](#cite_ref-11) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
12. [↑](#cite_ref-12) [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Knightcap: A chess program that learns by combining td(λ) with game-tree search*. Proceedings of the 15th International Conference on Machine Learning, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.54.8263&rep=rep1&type=pdf) via [citeseerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.8263)
13. [↑](#cite_ref-13) [The Cilkchess Parallel Chess Program](http://supertech.csail.mit.edu/chess/)
14. [↑](#cite_ref-14) [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *[Temporal Coherence and Prediction Decay in TD Learning](http://portal.acm.org/citation.cfm?id=1624299)*. [IJCAI 1999](Conferences#IJCAI1999 "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-99-VOL-1/PDF/081.pdf)
15. [↑](#cite_ref-15)  [Re: Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28819) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 02, 1998
16. [↑](#cite_ref-16) [Re: Hello from Edmonton (and on Temporal Differences)](https://www.stmintz.com/ccc/index.php?id=244085) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), August 05, 2002
17. [↑](#cite_ref-17) [Re: Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062&start=2) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 13, 2010
18. [↑](#cite_ref-18) [Positional learning](http://www.talkchess.com/forum/viewtopic.php?t=37062) by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), December 13, 2010
19. [↑](#cite_ref-19) [Tao update](https://www.stmintz.com/ccc/index.php?id=149645) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), January 12, 2001
20. [↑](#cite_ref-20) [Nici Schraudolph’s go networks](http://satirist.org/learn-game/systems/go-net.html), review by [Jay Scott](Jay_Scott "Jay Scott")
21. [↑](#cite_ref-21) [Guy Haworth](Guy_Haworth "Guy Haworth"), [Meel Velliste](Meel_Velliste "Meel Velliste") (**1998**). *[Chess Endgames and Neural Networks](http://centaur.reading.ac.uk/4569/)*. [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")

**[Up one level](Learning "Learning")**







 
