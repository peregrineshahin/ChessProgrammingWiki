---
title: Automated TuningRegression
---
**[Home](Home "Home") * Automated Tuning**

\[ Engine Tuner <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Automated Tuning**,

an [automated](https://en.wikipedia.org/wiki/Automation) adjustment of [evaluation](Evaluation "Evaluation") parameters or weights, and less commonly, [search](Search "Search") parameters <a id="cite-note-2" href="#cite-ref-2">[2]</a>, with the aim to improve the [playing strength](Playing_Strength "Playing Strength") of a chess engine or game playing program. Evaluation tuning can be applied by [mathematical optimization](Automated_Tuning#Optimization "Automated Tuning") or [machine learning](Learning "Learning"), both fields with huge overlaps. Learning approaches are subdivided into [supervised learning](Automated_Tuning#SupervisedLearning "Automated Tuning") using [labeled data](https://en.wikipedia.org/wiki/Training_set), and [reinforcement learning](Automated_Tuning#ReinformentLearning "Automated Tuning") to learn from trying, facing the exploration (of uncharted territory) and exploitation (of current knowledge) dilemma. [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") gives a comprehensive overview in *Machine Learning in Games: A Survey* published in 2000 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, covering evaluation tuning in chapter 4.

## Playing Strength

A difficulty in tuning and automated tuning of engine parameters is measuring [playing strength](Playing_Strength "Playing Strength"). Using small sets of [test-positions](Test-Positions "Test-Positions"), which was quite common in former times to estimate relative strength of chess programs, lacks adequate diversity for a reliable strength predication. In particular, solving test-positions does not necessarily correlate with practical playing strength in matches against other opponents. Therefore, measuring strength requires to play many games against a reference opponent to determine the [win rate](Match_Statistics#ratio "Match Statistics") with a certain [confidence](https://en.wikipedia.org/wiki/Confidence_interval). The closer the strength of two opponents, the more games are necessary to determine whether changed parameters or weights in one of them are improvements or not, up to several tens of thousands. Playing many games with ultra short time controls has became de facto standard with todays strong programs, as for instance applied in [Stockfish's](Stockfish "Stockfish") [Fishtest](Stockfish#TestingFramework "Stockfish"), using the [sequential probability ratio test](Match_Statistics#SPRT "Match Statistics") (SPRT) to possibly terminate a match early <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Parameter

Quote by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++
It is one of the best arts to find the right SMALL set of parameters and to tune them.

```

```C++
Some 12 years ago I had a technical article on this ("On telescoping linear evaluation functions") in the [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal"), pp. 91-94, describing a theorem (of existence) which says that in case of linear evaluation functions with lots of terms there is always a small subset of the terms such that this set with the right parameters is almost as good as the full evaluation function. 

```

## Mathematical Optimization

[Mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization) methods in tuning consider the engine as a [black box](https://en.wikipedia.org/wiki/Black_box).

## Methods

- [CLOP](CLOP "CLOP")
- [Genetic Algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming")
- [PBIL](Genetic_Programming#PBIL "Genetic Programming")
- [Simulated Annealing](Simulated_Annealing "Simulated Annealing")
- [SPSA](SPSA "SPSA")

## Instances

- [ACPP](ACPP "ACPP")
- [Amoeba](Amoeba "Amoeba")
- [Differential Evolution in BBChess](</BBChess_(SI)#DifferentialEvolution> "BBChess (SI)")
- [Deuterium](Deuterium "Deuterium")
- [Genetic Algorithm in Falcon](Falcon#GA "Falcon")
- [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")

## Advantages

- Works with all engine parameters, including search
- Takes search-eval interaction into account

## Disadvantages

- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity) issues with increasing number of weights to tune

## Reinforcement Learning

[Reinforcement learning](Reinforcement_Learning "Reinforcement Learning"), in particular [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning"), has a long history in tuning evaluation weights in game programming, first seeen in the late 50s by [Arthur Samuel](Arthur_Samuel "Arthur Samuel") in his [Checkers](Checkers "Checkers") player <a id="cite-note-7" href="#cite-ref-7">[7]</a>. In self play against a stable copy of itself, after each move, the weights of the evaluation function were adjusted in a way that the [score](Score "Score") of the [root position](Root "Root") after a [quiescence search](Quiescence_Search "Quiescence Search") became closer to the score of the full search. This TD method was generalized and formalized by [Richard Sutton](Richard_Sutton "Richard Sutton") in 1988 <a id="cite-note-8" href="#cite-ref-8">[8]</a>, who introduced the decay parameter **λ**, where proportions of the score came from the outcome of [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulated games, tapering between [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping#Artificial_intelligence_and_machine_learning) (λ = 0) and Monte Carlo (λ = 1). [TD-λ](Temporal_Difference_Learning#TDLamba "Temporal Difference Learning") was famously applied by [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") in his [Backgammon](Backgammon "Backgammon") program [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>, its [minimax](Minimax "Minimax") adaptation [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") was successful used in eval tuning of chess programs <a id="cite-note-11" href="#cite-ref-11">[11]</a>, with [KnightCap](KnightCap "KnightCap") <a id="cite-note-12" href="#cite-ref-12">[12]</a> and [CilkChess](CilkChess "CilkChess") <a id="cite-note-13" href="#cite-ref-13">[13]</a> as prominent samples.

## Instances

- [TD-λ](Temporal_Difference_Learning#TDLamba "Temporal Difference Learning")
- [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning")
- [RootStrap](Meep#RootStrap "Meep")
- [TreeStrap](Meep#TreeStrap "Meep")

## Engines

- [CilkChess](CilkChess "CilkChess")
- [EXchess](EXchess "EXchess") <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [FUSc#](FUSCsharp "FUSCsharp")
- [Green Light Chess](Green_Light_Chess "Green Light Chess")
- [KnightCap](KnightCap "KnightCap")
- [Meep](Meep "Meep")
- [NeuroChess](NeuroChess "NeuroChess")
- [SAL](SAL "SAL")
- [Tao](Tao "Tao")
- [TDChess](TDChess "TDChess")

## Supervised Learning

## Move Adaptation

One [supervised learning](Supervised_Learning "Supervised Learning") method considers desired moves from a set of positions, likely from grandmaster games, and tries to adjust their evaluation weights so that for instance a one-ply search agrees with the desired move. Already pioneering in reinforcement learning some years before, move adaptation was described by [Arthur Samuel](Arthur_Samuel "Arthur Samuel") in 1967 as used in the second version of his checkers player <a id="cite-note-15" href="#cite-ref-15">[15]</a>, where a structure of stacked linear evaluation functions was trained by computing a correlation measure based on the number of times the feature rated an alternative move higher than the desired move played by an expert <a id="cite-note-16" href="#cite-ref-16">[16]</a>. In chess, move adaptation was first described by [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") in 1982 <a id="cite-note-17" href="#cite-ref-17">[17]</a>, and with some extensions by [Tony Marsland](Tony_Marsland "Tony Marsland") in 1985 <a id="cite-note-18" href="#cite-ref-18">[18]</a>. [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought") as mentioned by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") et al. in 1990 <a id="cite-note-19" href="#cite-ref-19">[19]</a>, and later published by [Andreas Nowatzyk](Andreas_Nowatzyk "Andreas Nowatzyk"), is also based on an extended form of move adaptation <a id="cite-note-20" href="#cite-ref-20">[20]</a>. [Jonathan Schaeffer's](Jonathan_Schaeffer "Jonathan Schaeffer") and [Paul Lu's](Paul_Lu "Paul Lu") efforts to make Deep Thought's approach work for [Chinook](https://en.wikipedia.org/wiki/Chinook_%28draughts_player%29) in 1990 failed <a id="cite-note-21" href="#cite-ref-21">[21]</a> - nothing seemed to produce results that were as good than their hand-tuned effort <a id="cite-note-22" href="#cite-ref-22">[22]</a>.

## Value Adaptation

A second supervised learning approach used to tune evaluation weights is based on [regression](https://en.wikipedia.org/wiki/Regression) of the desired value, i.e. using the final outcome from huge sets of positions from quality games, or other information supplied by a supervisor, i.e. in form of annotations from [position evaluation symbols](https://en.wikipedia.org/wiki/Chess_annotation_symbols#Position_evaluation_symbols). Often, value adaptation is reinforced by determining an expected outcome by self play <a id="cite-note-23" href="#cite-ref-23">[23]</a>.

## Advantages

- Can modify any number of weights simultaneously - constant [time complexity](https://en.wikipedia.org/wiki/Time_complexity)

## Disadvantages

- Requires a source for the labeled data
- Can only be used for evaluation weights or anything else that can be labeled
- Works not optimal when combined with search

## Regression

\[ [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression) <a id="cite-note-24" href="#cite-ref-24">[24]</a>
[Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis) is a [statistical process](https://en.wikipedia.org/wiki/Statistics) with a substantial overlap with machine learning to [predict](https://en.wikipedia.org/wiki/Prediction) the value of an [Y variable](https://en.wikipedia.org/wiki/Dependent_and_independent_variables) (output), given known value pairs of the X and Y variables. While [linear regression](https://en.wikipedia.org/wiki/Linear_regression) deals with continuous outputs, [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) covers binary or discrete output, such as win/loss, or win/draw/loss. Parameter estimation in regression analysis can be formulated as the [minimization](https://en.wikipedia.org/wiki/Mathematical_optimization) of a [cost or loss function](https://en.wikipedia.org/wiki/Loss_function) over a [training set](https://en.wikipedia.org/wiki/Training_set) <a id="cite-note-25" href="#cite-ref-25">[25]</a>, such as [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) or [cross-entropy error function](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression) for [binary classification](https://en.wikipedia.org/wiki/Binary_classification) <a id="cite-note-26" href="#cite-ref-26">[26]</a>. The minimization is implemented by [iterative](Iteration "Iteration") optimization [algorithms](Algorithms "Algorithms") or [metaheuristics](https://en.wikipedia.org/wiki/Metaheuristic) such as [Iterated local search](https://en.wikipedia.org/wiki/Iterated_local_search), [Gauss–Newton algorithm](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm), or [conjugate gradient method](https://en.wikipedia.org/wiki/Conjugate_gradient_method).

## Linear Regression

The supervised problem of regression applied to [move adaptation](Automated_Tuning#MoveAdaption "Automated Tuning") was used by [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") in 1982, minimizing the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) of a cost function considering the program’s and a grandmaster’s choice of moves, as mentioned, extended by [Tony Marsland](Tony_Marsland "Tony Marsland") in 1985, and later by the [Deep Thought](Deep_Thought "Deep Thought") team. Regression used to [adapt desired values](Automated_Tuning#ValueAdaption "Automated Tuning") was described by [Donald H. Mitchell](Donald_H._Mitchell "Donald H. Mitchell") in his 1984 master thesis on evaluation features in [Othello](Othello "Othello"), cited by [Michael Buro](Michael_Buro "Michael Buro") <a id="cite-note-27" href="#cite-ref-27">[27]</a> <a id="cite-note-28" href="#cite-ref-28">[28]</a>. [Jens Christensen](Jens_Christensen "Jens Christensen") applied [linear regression](https://en.wikipedia.org/wiki/Linear_regression) to chess in 1986 to learn [point values](Point_Value "Point Value") in the domain of [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") <a id="cite-note-29" href="#cite-ref-29">[29]</a>.

## Logistic Regression

[](http://wolfr.am/1al3d5B) [Logistic function](https://en.wikipedia.org/wiki/Logistic_function) <a id="cite-note-30" href="#cite-ref-30">[30]</a>
Since the relationship between [win percentage and pawn advantage](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") is assumed to follow a [logistic model](https://en.wikipedia.org/wiki/Logistic_model), one may treat static evaluation as [single-layer perceptron](Neural_Networks#Perceptron "Neural Networks") or single [neuron](https://en.wikipedia.org/wiki/Artificial_neuron) [ANN](Neural_Networks "Neural Networks") with the common [logistic](https://en.wikipedia.org/wiki/Logistic_function) [activation function](https://en.wikipedia.org/wiki/Activation_function), performing the perceptron algorithm to train it <a id="cite-note-31" href="#cite-ref-31">[31]</a>. [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) in evaluation tuning was first elaborated by [Michael Buro](Michael_Buro "Michael Buro") in 1995 <a id="cite-note-32" href="#cite-ref-32">[32]</a>, and proved successful in the game of [Othello](Othello "Othello") in comparison with [Fisher's](Mathematician#RFisher "Mathematician") [linear discriminant](https://en.wikipedia.org/wiki/Kernel_Fisher_discriminant_analysis) and quadratic [discriminant](https://en.wikipedia.org/wiki/Discriminant) function for [normally distributed](https://en.wikipedia.org/wiki/Normal_distribution) features, and served as eponym of his Othello program *Logistello* <a id="cite-note-33" href="#cite-ref-33">[33]</a>. In computer chess, logistic regression was applied by [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") with [Gosu](Gosu "Gosu") <a id="cite-note-34" href="#cite-ref-34">[34]</a>, later proposed by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") in 2009 as used by [Gaviota](Gaviota "Gaviota") <a id="cite-note-35" href="#cite-ref-35">[35]</a>, independently described by [Amir Ban](Amir_Ban "Amir Ban") in 2012 for [Junior's](Junior "Junior") evaluation learning <a id="cite-note-36" href="#cite-ref-36">[36]</a>, and explicitly mentioned by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") in a January 2014 [CCC](CCC "CCC") discussion <a id="cite-note-37" href="#cite-ref-37">[37]</a>, when [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund") explained [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") <a id="cite-note-38" href="#cite-ref-38">[38]</a>, which subsequently popularized logistic regression tuning in computer chess. [Vladimir Medvedev's](Vladimir_Medvedev "Vladimir Medvedev") [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis") <a id="cite-note-39" href="#cite-ref-39">[39]</a> <a id="cite-note-40" href="#cite-ref-40">[40]</a> experiments showed why the [logistic function](https://en.wikipedia.org/wiki/Logistic_function) is appropriate, and further used [cross-entropy](https://en.wikipedia.org/wiki/Cross_entropy) and [regularization](https://en.wikipedia.org/wiki/Regularization_%28mathematics%29).

## Instances

- [Arasan's Tuning](Arasan#Tuning "Arasan")
- [Ethereal](Ethereal "Ethereal")
- [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought")
- [FabChess](FabChess "FabChess")
- [Gosu](Gosu "Gosu")
- [Koivisto](Koivisto "Koivisto")
- [Minimax Tree Optimization](Minimax_Tree_Optimization "Minimax Tree Optimization") (MMTO or the Bonanza-Method in [Shogi](Shogi "Shogi"))
- [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")
- [RuyTune](RuyTune "RuyTune")
- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Winter](Winter "Winter")

## See also

- [Dynamic Programming](Dynamic_Programming "Dynamic Programming")
- [Evaluation](Evaluation "Evaluation")
- [GLEM](Michael_Buro#GLEM "Michael Buro") by [Michael Buro](Michael_Buro "Michael Buro")
- [Iteration](Iteration "Iteration")
- [Knowledge](Knowledge "Knowledge")
- [Learning](Learning "Learning")
- [Match Statistics](Match_Statistics "Match Statistics")
- [Neural Networks](Neural_Networks "Neural Networks")
- [Trial and Error](Trial_and_Error "Trial and Error")

## Publications

## 1959

- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959

## 1960 ...

- [Arnold K. Griffith](Arnold_K._Griffith "Arnold K. Griffith") (**1966**). *[A new Machine-Learning Technique applied to the Game of Checkers](http://dspace.mit.edu/handle/1721.1/5896#files-area)*. [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [Project MAC](https://en.wikipedia.org/wiki/MIT_Computer_Science_and_Artificial_Intelligence_Laboratory#Project_MAC), MAC-M-293
- [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://researcher.watson.ibm.com/researcher/files/us-beygel/samuel-checkers.pdf)

## 1970 ...

- [Arnold K. Griffith](Arnold_K._Griffith "Arnold K. Griffith") (**1974**). *[A Comparison and Evaluation of Three Machine Learning Procedures as Applied to the Game of Checkers](http://www.sciencedirect.com/science/article/pii/0004370274900277)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 5, No. 2
- [Mokhtar S. Bazaraa](Mathematician#MSBazaraa "Mathematician"), [C. M. Shetty](Mathematician#MCShetty "Mathematician") (**1976**). *[Foundations of Optimization](https://link.springer.com/book/10.1007%2F978-3-642-48294-6)*. Lecture Notes in Economics and Mathematical Systems, Vol. 122, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Mokhtar S. Bazaraa](Mathematician#MSBazaraa "Mathematician"), [C. M. Shetty](Mathematician#MCShetty "Mathematician") (**1979**). *Nonlinear Programming: Theory and Algorithms*. [Wiley](<https://en.wikipedia.org/wiki/Wiley_(publisher)>) » [2nd](#NonlinearProgramming2nd), [3rd edition](#NonlinearProgramming3rd)

## 1980 ...

- [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1982**). *A Learning Chess Program.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
- [Donald H. Mitchell](Donald_H._Mitchell "Donald H. Mitchell") (**1984**). *Using Features to Evaluate Positions in Experts' and Novices' Othello Games*. Master thesis, Department of Psychology, [Northwestern University](Northwestern_University "Northwestern University"), Evanston, IL

## 1985 ...

- [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *Evaluation-Function Factors*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/evaluation.pdf)
- [Jens Christensen](Jens_Christensen "Jens Christensen"), [Richard Korf](Richard_Korf "Richard Korf") (**1986**). *A Unified Theory of Heuristic Evaluation functions and Its Applications to Learning.* Proceedings of the [AAAI-86](http://www.aaai.org/Conferences/AAAI/aaai86.php), pp. 148-152, [pdf](http://www.aaai.org/Papers/AAAI/1986/AAAI86-023.pdf)
- [Jens Christensen](Jens_Christensen "Jens Christensen") (**1986**). *[Learning Static Evaluation Functions by Linear Regression](http://link.springer.com/chapter/10.1007/978-1-4613-2279-5_9?no-access=true)*. in [Tom Mitchell](Tom_Mitchell "Tom Mitchell"), [Jaime Carbonell](Jaime_Carbonell "Jaime Carbonell"), [Ryszard Michalski](Ryszard_Michalski "Ryszard Michalski") (**1986**). *[Machine Learning: A Guide to Current Research](http://link.springer.com/book/10.1007/978-1-4613-2279-5)*. The Kluwer International Series in Engineering and Computer Science, Vol. 12
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 1: Grandmasters have Insights - the Problem is what to Incorporate into Practical Problems.* [ICCA Journal, Vol. 10, No. 1](ICGA_Journal#10_1 "ICGA Journal")
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of [De Groot](Adriaan_de_Groot "Adriaan de Groot") and [Slater](Eliot_Slater "Eliot Slater")*. [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal")
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson"), [Richard Korf](Richard_Korf "Richard Korf") (**1987**). *A Model of Two-Player Evaluation Functions.* [AAAI-87](http://www.aaai.org/Conferences/AAAI/aaai87.php). [pdf](http://www.aaai.org/Papers/AAAI/1987/AAAI87-016.pdf)
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1988**). *Learning Expected-Outcome Evaluators in Chess.* Proceedings of the 1988 AAAI Spring Symposium Series: Computer Game Playing, 26-28.
- [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee"), [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan") (**1988**). *[A Pattern Classification Approach to Evaluation Function Learning](http://www.sciencedirect.com/science/article/pii/0004370288900768)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 36, No. 1
- [Richard Sutton](Richard_Sutton "Richard Sutton") (**1988**). *Learning to Predict by the Methods of Temporal Differences*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 3, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~sutton/papers/sutton-88.pdf)
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1989**). *On Learning and Testing Evaluation Functions.* Proceedings of the Sixth Israeli Conference on Artificial Intelligence, 1989, 7-16.
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1989**). *Weight Assessment in Evaluation Functions*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")

## 1990 ...

- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *[Expected-Outcome: A General Model of Static Evaluation](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=44404)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 2
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *An Analysis of Expected-Outcome.* Journal of Experimental and Theoretical Artificial Intelligence 2: 55-73.
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *On Learning and Testing Evaluation Functions.* Journal of Experimental and Theoretical Artificial Intelligence, Vol. 2
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1990**). *A Statistical Study of Selective Min-Max Search in Computer Chess*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *A Statistical Study of Selective Min-Max Search in Computer Chess*. [ICCA Journal, Vol. 14, No. 1](ICGA_Journal#14_1 "ICGA Journal")
- [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Andreas Nowatzyk](Andreas_Nowatzyk "Andreas Nowatzyk") (**1990**). *[A Grandmaster Chess Machine](http://www.disi.unige.it/person/DelzannoG/AI2/hsu.html)*. [Scientific American](Scientific_American "Scientific American"), Vol. 263, No. 4, pp. 44-50. ISSN 0036-8733.
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1991**). *The Expected-Outcome Model of Two-Player Games.* Part of the series, Research Notes in Artificial Intelligence (San Mateo: Morgan Kaufmann, 1991).
- [Alex van Tiggelen](Alex_van_Tiggelen "Alex van Tiggelen") (**1991**). *Neural Networks as a Guide to Optimization - The Chess Middle Game Explored*. [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
- [William Tunstall-Pedoe](William_Tunstall-Pedoe "William Tunstall-Pedoe") (**1991**). *Genetic Algorithms Optimizing Evaluation Functions*. [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
- [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Jeffery A. Clouse](http://dblp.uni-trier.de/pers/hd/c/Clouse:Jeffery_A=) (**1991**). *[Two Kinds of Training Information for Evaluation Function Learning](http://scholarworks.umass.edu/cs_faculty_pubs/193/)*. [University of Massachusetts, Amherst](https://en.wikipedia.org/wiki/University_of_Massachusetts_Amherst), Proceedings of the AAAI 1991
- [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1993**). *On Telescoping Linear Evaluation Functions.* [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal")
- [Mokhtar S. Bazaraa](Mathematician#MSBazaraa "Mathematician"), [Hanif D. Sherali](Mathematician#HDSherali "Mathematician"), [C. M. Shetty](Mathematician#MCShetty "Mathematician") (**1993**). *Nonlinear Programming: Theory and Algorithms*. 2nd edition, [Wiley](<https://en.wikipedia.org/wiki/Wiley_(publisher)>) » [1st](#NonlinearProgramming1st), [3rd edition](#NonlinearProgramming3rd)
- [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)

## 1995 ...

- [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *[Statistical Feature Combination for the Evaluation of Game Positions](https://www.jair.org/index.php/jair/article/view/10146)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 3
- [Chris McConnell](Chris_McConnell "Chris McConnell") (**1995**). *Tuning Evaluation Functions for Search*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=9B2A0CCA8B1AFB594A879799D974111A?doi=10.1.1.53.9742&rep=rep1&type=pdf)
- [Chris McConnell](Chris_McConnell "Chris McConnell") (**1995**). *Tuning Evaluation Functions for Search* (Talk), [ps](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/ccm/www/talks/tune.ps)
- [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**1996**). *Machine Learning in Computer Chess: The Next Generation.* [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal"), [zipped ps](http://www.ofai.at/cgi-bin/get-tr?download=1&paper=oefai-tr-96-11.ps.gz)
- [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
- [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1997**). *Evaluation Tuning for Computer Chess: Linear Discriminant Methods*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")
- [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Experiments in Parameter Learning Using Temporal Differences*. [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal"), [pdf](http://cs.anu.edu.au/%7ELex.Weaver/pub_sem/publications/ICCA-98_equiv.pdf)
- [Michael Buro](Michael_Buro "Michael Buro") (**1998**). *[From Simple Features to Sophisticated Evaluation Functions](http://link.springer.com/chapter/10.1007/3-540-48957-6_8)*. [CG 1998](CG_1998 "CG 1998"), [pdf](https://skatgame.net/mburo/ps/glem.pdf)
- [James C. Spall](James_C._Spall "James C. Spall") (**1998**). *[Implementation of the Simultaneous Perturbation Algorithm for Stochastic Optimization](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=705889&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D705889)*. [IEEE Transactions on Aerospace and Electronic Systems](IEEE#TOCAES "IEEE"), [pdf](http://www.jhuapl.edu/spsa/PDF-SPSA/Spall_Implementation_of_the_Simultaneous.PDF) <a id="cite-note-41" href="#cite-ref-41">[41]</a>
- [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")

## 2000 ...

- [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**). *Machine Learning in Games: A Survey*. [Austrian Research Institute for Artificial Intelligence](https://en.wikipedia.org/wiki/Austrian_Research_Institute_for_Artificial_Intelligence), OEFAI-TR-2000-3, [pdf](https://fmfi-uk.hq.sk/Informatika/Strojove%20Ucenie/oefai-tr-2000-31.pdf)
- [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
- [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (eds.) (**2001**). *[Machines that Learn to Play Games](https://www.novapublishers.com/catalog/product_info.php?products_id=720)*. Advances in Computation: Theory and Practice, Vol. 8,. [NOVA Science Publishers](https://en.wikipedia.org/wiki/Nova_Publishers)

[Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2001**). *[Comparison Training of Chess Evaluation Functions](http://dl.acm.org/citation.cfm?id=644397)*.  » [SCP](SCP "SCP"), [Deep Blue](Deep_Blue "Deep Blue")

- [Graham Kendall](Graham_Kendall "Graham Kendall"), [Glenn Whitwell](index.php?title=Glenn_Whitwell&action=edit&redlink=1 "Glenn Whitwell (page does not exist)") (**2001**). *[An Evolutionary Approach for the Tuning of a Chess Evaluation Function using Population Dynamics](https://ieeexplore.ieee.org/document/934299?tp=&arnumber=934299&url=http:%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D934299)*. Proceedings of the 2001 Congress on Evolutionary Computation, Vol. 2, [pdf](http://www.cs.nott.ac.uk/~pszgxk/papers/cec2001chess.pdf)
- [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Learning Search Control in Adversary Games*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), pp. 157-174. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01b.pdf)
- [Michael Buro](Michael_Buro "Michael Buro") (**2002**). *Improving Mini-max Search by Supervised Learning.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 134, No. 1, [pdf](http://www.cs.ualberta.ca/~mburo/ps/logaij.pdf)
- [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [Tony Marsland](Tony_Marsland "Tony Marsland"), [Michael Buro](Michael_Buro "Michael Buro") (**2003**). *Evaluation Function Tuning via Ordinal Correlation*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.top-5000.nl/ps/Dave%20Gomboc%20-%20Evaluation%20Tuning.pdf)
- [Dave Gomboc](Dave_Gomboc "Dave Gomboc") (**2004**). *Tuning Evaluation Functions by Maximizing Concordance*. M.Sc. Thesis, [University of Alberta](University_of_Alberta "University of Alberta")
- [Adam Marczyk](index.php?title=Adam_Marczyk&action=edit&redlink=1 "Adam Marczyk (page does not exist)") (**2004**). *[Genetic Algorithms and Evolutionary Computation](http://www.talkorigins.org/faqs/genalg/genalg.html)* from the [TalkOrigins Archive](https://en.wikipedia.org/wiki/TalkOrigins_Archive)
- [Petr Aksenov](index.php?title=Petr_Aksenov&action=edit&redlink=1 "Petr Aksenov (page does not exist)") (**2004**). *[Genetic algorithms for optimising chess position scoring](http://joypub.joensuu.fi/publications/masters_thesis/aksenov_genetic/index_en.html)*, Master's thesis, [pdf](ftp://cs.joensuu.fi/pub/Theses/2004_MSc_Aksenov_Petr.pdf)
- [Mathieu Autonès](index.php?title=Mathieu_Auton%C3%A8s&action=edit&redlink=1 "Mathieu Autonès (page does not exist)"), [Aryel Beck](index.php?title=Aryel_Beck&action=edit&redlink=1 "Aryel Beck (page does not exist)"), [Phillippe Camacho](index.php?title=Phillippe_Camacho&action=edit&redlink=1 "Phillippe Camacho (page does not exist)"), [Nicolas Lassabe](index.php?title=Nicolas_Lassabe&action=edit&redlink=1 "Nicolas Lassabe (page does not exist)"), [Hervé Luga](index.php?title=Herv%C3%A9_Luga&action=edit&redlink=1 "Hervé Luga (page does not exist)"), [François Scharffe](index.php?title=Fran%C3%A7ois_Scharffe&action=edit&redlink=1 "François Scharffe (page does not exist)") (**2004**). *[Evaluation of Chess Position by Modular Neural network Generated by Genetic Algorithm](http://link.springer.com/chapter/10.1007/978-3-540-24650-3_1)*. [EuroGP 2004](http://www.informatik.uni-trier.de/~ley/db/conf/eurogp/eurogp2004.html#AutonesBCLLS04)
- [Henk Mannen](Henk_Mannen "Henk Mannen"), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2004**). *[Learning to play chess using TD(λ)-learning with database games](<https://www.semanticscholar.org/paper/Learning-to-Play-Chess-using-TD(lambda)-learning-Mannen-Wiering/00a6f81c8ebe8408c147841f26ed27eb13fb07f3>)*. Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), Benelearn’04, [pdf](https://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/learning-chess.pdf)
- [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w szachach*. Masters thesis, [University of Warsaw](University_of_Warsaw "University of Warsaw") (Polish, Modeling of an evaluation function in chess)
- [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w grach*. [University of Warsaw](University_of_Warsaw "University of Warsaw"), [zipped ps](https://www.mimuw.edu.pl/~paterek/mfog.ps.gz) (Polish, Modeling of an evaluation function in games)

## 2005 ...

- [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [Michael Buro](Michael_Buro "Michael Buro"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2005**). *Tuning Evaluation Functions by Maximizing Concordance*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 349, No. 2, [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/tcs-learn.pdf)
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2005**). *[Evaluation by Hill-climbing: Getting the right move by solving micro-problems](http://www.aifactory.co.uk/newsletter/2005_03_hill-climbing.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2005
- [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári"), [Mark Winands](Mark_Winands "Mark Winands") (**2005**). *[RSPSA: Enhanced Parameter Optimization in Games](http://link.springer.com/chapter/10.1007/11922155_4)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www.sztaki.hu/~szcsaba/papers/rspsa_acg.pdf)

**2006**

- [Mokhtar S. Bazaraa](Mathematician#MSBazaraa "Mathematician"), [Hanif D. Sherali](Mathematician#HDSherali "Mathematician"), [C. M. Shetty](Mathematician#MCShetty "Mathematician") (**2006**). *[Nonlinear Programming: Theory and Algorithms](https://www.wiley.com/en-us/Nonlinear+Programming%3A+Theory+and+Algorithms%2C+3rd+Edition-p-9780471486008)*. 3rd edition, [Wiley](<https://en.wikipedia.org/wiki/Wiley_(publisher)>) <a id="cite-note-42" href="#cite-ref-42">[42]</a> » [1st](#NonlinearProgramming1st), [2nd edition](#NonlinearProgramming2nd)
- [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2006**). *[Universal Parameter Optimisation in Games Based on SPSA](http://link.springer.com/article/10.1007/s10994-006-6888-8)*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Special Issue on Machine Learning and Games, Vol. 63, No. 3
- [Hallam Nasreddine](index.php?title=Hallam_Nasreddine&action=edit&redlink=1 "Hallam Nasreddine (page does not exist)"), [Hendra Suhanto Poh](index.php?title=Hendra_Suhanto_Poh&action=edit&redlink=1 "Hendra Suhanto Poh (page does not exist)"), [Graham Kendall](Graham_Kendall "Graham Kendall") (**2006**). *Using an Evolutionary Algorithm for the Tuning of a Chess Evaluation Function Based on a Dynamic Boundary Strategy*. Proceedings of the 2006 [IEEE](IEEE "IEEE") Conference on Cybernetics and Intelligent Systems, [pdf](http://www.graham-kendall.com/papers/npk2006.pdf)
- [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Daisaku Yokoyama](Daisaku_Yokoyama "Daisaku Yokoyama"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2006**). *[Automatic Construction of Static Evaluation Functions for Computer Game Players](http://www.springerlink.com/content/6180u7h3t312468u/)*. ALT ’06
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2006**). *[A Differential Evolution for the Tuning of a Chess Evaluation Function](https://ieeexplore.ieee.org/document/1688532)*. [IEEE Congress on Evolutionary Computation](IEEE "IEEE")
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") (**2006**). *Optimal control of minimax search result to learn positional evaluation*. [11th Game Programming Workshop](Conferences#GPW "Conferences") (Japanese)
- [Frank Hutter](Frank_Hutter "Frank Hutter"), [Youssef Hamadi](https://scholar.google.co.uk/citations?user=LqUxHuQAAAAJ&hl=en), [Holger H. Hoos](Mathematician#HHHoos "Mathematician"), [Kevin Leyton-Brown](Mathematician#LeytonBrown "Mathematician") (**2006**). *[Performance Prediction and Automated Tuning of Randomized and Parametric Algorithms](https://link.springer.com/chapter/10.1007/11889205_17)*. [CP 2006](https://dblp.org/db/conf/cp/cp2006.html), [pdf](https://www.cs.ubc.ca/~hutter/papers/aaaiws06_lfs06-autoparam-prelim.pdf)

**2007**

- [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kazunori Yamaguchi](Kazunori_Yamaguchi "Kazunori Yamaguchi"), [Satoru Kawai](Satoru_Kawai "Satoru Kawai") (**2007**). *Visualization and Adjustment of Evaluation Functions Based on Evaluation Values and Win Probability*. [AAAI 2007](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2007.html), [pdf](https://www.aaai.org/Papers/AAAI/2007/AAAI07-136.pdf)
- [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Daisaku Yokoyama](Daisaku_Yokoyama "Daisaku Yokoyama"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2007**). *Automatic Generation of Evaluation Features for Computer Game Players*. [pdf](http://cswww.essex.ac.uk/cig/2007/papers/2037.pdf)
- [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2007**). *Recent advances in machine learning and game playing*. [ÖGAI Journal](http://www.oegai.at/journal.shtml), Vol. 26, No. 2, Computer Game Playing, [pdf](https://www.ke.tu-darmstadt.de/~juffi/publications/ogai-07.pdf)
- [Mohammed Shahid Abdulla](https://dblp.org/pid/70/382.html), [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar") (**2007**). *[Reinforcement Learning Based Algorithms for Average Cost Markov Decision Processes](https://link.springer.com/article/10.1007/s10626-006-0003-y)*. [Discrete Event Dynamic Systems](https://www.springer.com/journal/10626), Vol.17, No.1  » [SPSA](SPSA "SPSA")

**2008**

- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *Genetic Algorithms for Mentor-Assisted Evaluation Function Optimization*. [GECCO '08](http://www.sigevo.org/gecco-2008/), [arXiv:1711.06839](https://arxiv.org/abs/1711.06839)
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2008**). *[An Adaptive Differential Evolution Algorithm with Opposition-Based Mechanisms, Applied to the Tuning of a Chess Program](https://link.springer.com/chapter/10.1007%2F978-3-540-68830-3_12)*. [Advances in Differential Evolution](https://link.springer.com/book/10.1007/978-3-540-68830-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

**2009**

- [Joel Veness](Joel_Veness "Joel Veness"), [David Silver](David_Silver "David Silver"), [William Uther](William_Uther "William Uther"), [Alan Blair](Alan_Blair "Alan Blair") (**2009**). *[Bootstrapping from Game Tree Search](http://papers.nips.cc/paper/3722-bootstrapping-from-game-tree-search)*. [Neural Information Processing Systems (NIPS), 2009](http://nips.cc/), [pdf](http://jveness.info/publications/nips2009%20-%20bootstrapping%20from%20game%20tree%20search.pdf) » [Meep](Meep "Meep") <a id="cite-note-43" href="#cite-ref-43">[43]</a>
- [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2009**). *Simulating Human Grandmasters: Evolution and Coevolution of Evaluation Functions*. [GECCO '09](http://www.sigevo.org/gecco-2009/), [arXiv:1711.0684](https://arxiv.org/abs/1711.06840)
- [Omid David](Eli_David "Eli David") (**2009**). *Genetic Algorithms Based Learning for Evolving Intelligent Organisms*. Ph.D. Thesis.
- [Broch Davison](index.php?title=Broch_Davison&action=edit&redlink=1 "Broch Davison (page does not exist)") (**2009**). *[Playing Chess with Matlab](http://www.enm.bris.ac.uk/teaching/projects/2008_09/bd5053/index.html)*. M.Sc. thesis supervised by [Nello Cristianini](http://www.bris.ac.uk/engineering/people/nello-cristianini/index.html), [pdf](http://www.enm.bris.ac.uk/teaching/projects/2008_09/bd5053/FinalReport.pdf) <a id="cite-note-44" href="#cite-ref-44">[44]</a>
- [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**2009**). *A Methodology for Learning Players' Styles from Game Records*. [arXiv:0904.2595v1](http://arxiv.org/abs/0904.2595v1)
- [Wei-Lun Kao](Wei-Lun_Kao "Wei-Lun Kao") (**2009**). *The Automatically Tuning System of Evaluation Function for Computer Chinese Chess*. Master thesis, [National Chiao Tung University](National_Chiao_Tung_University "National Chiao Tung University"), [pdf](https://ir.nctu.edu.tw/bitstream/11536/43333/1/553001.pdf) (Chinese)

## 2010 ...

- [Frank Hutter](Frank_Hutter "Frank Hutter"), [Holger H. Hoos](Mathematician#HHHoos "Mathematician"), [Kevin Leyton-Brown](Mathematician#LeytonBrown "Mathematician"), [Kevin P. Murphy](Mathematician#KPMurphy "Mathematician") (**2010**). *[Time-Bounded Sequential Parameter Optimization](https://dl.acm.org/citation.cfm?id=1893694)*. [LION 2010](https://dblp.org/db/conf/lion/lion2010.html), [pdf](https://ml.informatik.uni-freiburg.de/papers/10-LION-TB-SPO.pdf)
- [Amine Bourki](index.php?title=Amine_Bourki&action=edit&redlink=1 "Amine Bourki (page does not exist)"), [Matthieu Coulm](index.php?title=Matthieu_Coulm&action=edit&redlink=1 "Matthieu Coulm (page does not exist)"), [Philippe Rolet](index.php?title=Philippe_Rolet&action=edit&redlink=1 "Philippe Rolet (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Paul Vayssière](index.php?title=Paul_Vayssi%C3%A8re&action=edit&redlink=1 "Paul Vayssière (page does not exist)") (**2010**). *[Parameter Tuning by Simple Regret Algorithms and Multiple Simultaneous Hypothesis Testing](http://hal.inria.fr/inria-00467796/en/)*. [pd](http://hal.inria.fr/docs/00/46/77/96/PDF/tosubmit.pdf)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal")
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković") (**2010**). *[Differential Evolution for the Tuning of a Chess Evaluation Function](http://labraj.uni-mb.si/en/PhD_Thesis_Defence_%28Borko_Bo%C5%A1kovi%C4%87%29)*. Ph.D. thesis, [University of Maribor](University_of_Maribor "University of Maribor")

**2011**

- [Frank Hutter](Frank_Hutter "Frank Hutter"), [Holger H. Hoos](Mathematician#HHHoos "Mathematician"), [Kevin Leyton-Brown](Mathematician#LeytonBrown "Mathematician") (**2011**). *[Sequential Model-Based Optimization for General Algorithm Configuration](https://link.springer.com/chapter/10.1007/978-3-642-25566-3_40)*. [LION 2011](https://dblp.org/db/conf/lion/lion2011.html), [pdf](https://ml.informatik.uni-freiburg.de/papers/11-LION5-SMAC.pdf)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2011**). *Expert-Driven Genetic Algorithms for Simulating Evaluation Functions*. Genetic Programming and Evolvable Machines, Vol. 12, No. 1, [arXiv:1711.06841](https://arxiv.org/abs/1711.06841)
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest") (**2011**). *[Tuning Chess Evaluation Function Parameters using Differential Evolution](http://www.informatica.si/index.php/informatica/article/view/353)*. Informatica, Vol. 35, No. 2
- [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Janez Brest](Janez_Brest "Janez Brest"), [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2011**). *[History mechanism supported differential evolution for chess evaluation function tuning](https://dl.acm.org/citation.cfm?id=1966601)*. [Soft Computing](http://www.springer.com/engineering/computational+intelligence+and+complexity/journal/500), Vol. 15, No. 4
- [Eduardo Vázquez-Fernández](index.php?title=Eduardo_V%C3%A1zquez-Fern%C3%A1ndez&action=edit&redlink=1 "Eduardo Vázquez-Fernández (page does not exist)"), [Carlos Artemio Coello Coello](index.php?title=Carlos_Artemio_Coello_Coello&action=edit&redlink=1 "Carlos Artemio Coello Coello (page does not exist)"), [Feliú Davino Sagols Troncoso](index.php?title=Feli%C3%BA_Davino_Sagols_Troncoso&action=edit&redlink=1 "Feliú Davino Sagols Troncoso (page does not exist)") (**2011**). *An Evolutionary Algorithm for Tuning a Chess Evaluation Function*. [CEC 2011](http://www.informatik.uni-trier.de/~ley/db/conf/cec/cec2011.html#Vazquez-FernandezCT11), [pdf](http://delta.cs.cinvestav.mx/~ccoello/conferences/eduardo-cec2011-final.pdf.gz)
- [Eduardo Vázquez-Fernández](index.php?title=Eduardo_V%C3%A1zquez-Fern%C3%A1ndez&action=edit&redlink=1 "Eduardo Vázquez-Fernández (page does not exist)"), [Carlos Artemio Coello Coello](index.php?title=Carlos_Artemio_Coello_Coello&action=edit&redlink=1 "Carlos Artemio Coello Coello (page does not exist)"), [Feliú Davino Sagols Troncoso](index.php?title=Feli%C3%BA_Davino_Sagols_Troncoso&action=edit&redlink=1 "Feliú Davino Sagols Troncoso (page does not exist)") (**2011**). *[An Adaptive Evolutionary Algorithm Based on Typical Chess Problems for Tuning a Chess Evaluation Function](http://dl.acm.org/citation.cfm?id=2001882)*. [GECCO 2011](http://www.informatik.uni-trier.de/~ley/db/conf/gecco/gecco2011c.html#Vazquez-FernandezCT11), [pdf](http://delta.cs.cinvestav.mx/~ccoello/conferences/vazquez-gecco2011.pdf.gz)
- [Ilya Loshchilov](Ilya_Loshchilov "Ilya Loshchilov"), [Marc Schoenauer](Marc_Schoenauer "Marc Schoenauer"), [Michèle Sebag](Mich%C3%A8le_Sebag "Michèle Sebag") (**2011**). *Adaptive coordinate descent.* [GECCO 2011](https://dblp.org/db/conf/gecco/gecco2011.html), [pdf](http://www.loshchilov.com/publications/GECCO2011_AdaptiveCoordinateDescent.pdf) <a id="cite-note-45" href="#cite-ref-45">[45]</a>
- [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2011**). *[CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://remi.coulom.free.fr/CLOP/)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13") <a id="cite-note-46" href="#cite-ref-46">[46]</a> <a id="cite-note-47" href="#cite-ref-47">[47]</a>
- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2011**). *[The Global Landscape of Objective Functions for the Optimization of Shogi Piece Values with a Game-Tree Search](http://link.springer.com/chapter/10.1007%2F978-3-642-31866-5_16)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13") » [Shogi](Shogi "Shogi")
- [John Duchi](Mathematician#JCDuchi "Mathematician"), [Elad Hazan](Mathematician#EHazan "Mathematician"), [Yoram Singer](Mathematician#YSinger "Mathematician") (**2011**). *[Adaptive Subgradient Methods for Online Learning and Stochastic Optimization](https://dl.acm.org/doi/10.5555/1953048.2021068)*. [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research), Vol. 12, [pdf](https://jmlr.org/papers/volume12/duchi11a/duchi11a.pdf) » [AdaGrad](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad)

**2012**

- [Amir Ban](Amir_Ban "Amir Ban") (**2012**). *[Automatic Learning of Evaluation, with Applications to Computer Chess](http://www.ratio.huji.ac.il/node/2362)*. Discussion Paper 613, [The Hebrew University of Jerusalem](https://en.wikipedia.org/wiki/Hebrew_University_of_Jerusalem) - Center for the Study of Rationality, [Givat Ram](https://en.wikipedia.org/wiki/Givat_Ram)
- [Thitipong Kanjanapa](index.php?title=Thitipong_Kanjanapa&action=edit&redlink=1 "Thitipong Kanjanapa (page does not exist)"), [Kanako Komiya](index.php?title=Kanako_Komiya&action=edit&redlink=1 "Kanako Komiya (page does not exist)"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2012**). *Design and Implementation of Bonanza Method for the Evaluation in the Game of Arimaa*. [IPSJ SIG Technical Report](http://www.ipsj.or.jp/english/index.html), Vol. 2012-GI-27, No. 4, [pdf](http://arimaa.com/arimaa/papers/KanjanapaThitipong/IPSJ-GI12027004.pdf) » [Arimaa](Arimaa "Arimaa")
- [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett") (**2012**). *General-Purpose Optimization Through Information Maximization*. Ph.D. thesis, [University of Texas at Austin](https://en.wikipedia.org/wiki/University_of_Texas_at_Austin), advisor [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen"), [pdf](http://www.alockett.com/static/pdf/lockett-thesis.pdf)

**2013**

- [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2013**). *[A Measure-Theoretic Analysis of Stochastic Optimization](http://nn.cs.utexas.edu/?lockett:foga2013)*. [FOGA 2013](https://dblp.uni-trier.de/db/conf/foga/foga2013.html)
- [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ching-Hua Kuo](Ching-Hua_Kuo "Ching-Hua Kuo"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)") (**2013**). *[A Supervised Learning Method for Chinese Chess Programs](https://kaigi.org/jsai/webprogram/2013/paper-138.html)*. [JSAI2013](http://2013.conf.ai-gakkai.or.jp/english-info), [pdf](https://kaigi.org/jsai/webprogram/2013/pdf/138.pdf)
- [Akira Ura](Akira_Ura "Akira Ura"), [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2013**). *[Comparison Training of Shogi Evaluation Functions with Self-Generated Training Positions and Moves](https://link.springer.com/chapter/10.1007/978-3-319-09165-5_18)*. [CG 2013](CG_2013 "CG 2013"), [slides as pdf](https://pdfs.semanticscholar.org/6ad0/7167425539cf64e6bf420d7a28a1fc1047d6.pdf)
- [Yoshikuni Sato](Yoshikuni_Sato "Yoshikuni Sato"), [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Daisuke Takahashi](Daisuke_Takahashi "Daisuke Takahashi") (**2013**). *[Optimizing Objective Function Parameters for Strength in Computer Game-Playing](http://www.aaai.org/ocs/index.php/AAAI/AAAI13/paper/view/6402)*. [AAAI 2013](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2013.html#SatoMTT13)
- [Shalabh Bhatnagar](Shalabh_Bhatnagar "Shalabh Bhatnagar"), [H.L. Prasad](https://dblp.org/pid/31/10493.html), [L.A. Prashanth](https://scholar.google.co.in/citations?user=Q1YXWpoAAAAJ&hl=en) (**2013**). *[Stochastic Recursive Algorithms for Optimization: Simultaneous Perturbation Methods](https://link.springer.com/book/10.1007/978-1-4471-4285-0)*. [Lecture Notes in Control and Information Sciences](https://www.springer.com/series/642), Vol. 434, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) » [SPSA](SPSA "SPSA")
- [Tomáš Hřebejk](index.php?title=Tom%C3%A1%C5%A1_H%C5%99ebejk&action=edit&redlink=1 "Tomáš Hřebejk (page does not exist)") (**2013**). *Arimaa challenge - Static Evaluation Function*. Master Thesis, [Charles University in Prague](https://en.wikipedia.org/wiki/Charles_University_in_Prague), [pdf](http://arimaa.com/arimaa/papers/ThomasHrebejk/Arimaa.pdf) » [Arimaa](Arimaa "Arimaa") <a id="cite-note-48" href="#cite-ref-48">[48]</a>
- [Yoshikuni Sato](Yoshikuni_Sato "Yoshikuni Sato"), [Makoto Miwa](Makoto_Miwa "Makoto Miwa"), [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Daisuke Takahashi](Daisuke_Takahashi "Daisuke Takahashi") (**2013**). *[Optimizing Objective Function Parameters for Strength in Computer Game-Playing](http://www.aaai.org/ocs/index.php/AAAI/AAAI13/paper/view/6402)*. [AAAI 2013](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2013.html#SatoMTT13)
- [Ilya Loshchilov](Ilya_Loshchilov "Ilya Loshchilov") (**2013**). *[Surrogate-Assisted Evolutionary Algorithms](http://loshchilov.com/phd.html)*. Ph.D. thesis, [Paris-Sud 11 University](University_of_Paris#11 "University of Paris"), advisors [Marc Schoenauer](Marc_Schoenauer "Marc Schoenauer") and [Michèle Sebag](Mich%C3%A8le_Sebag "Michèle Sebag")
- [Mark Schmidt](https://www.cs.ubc.ca/~schmidtm/), [Nicolas Le Roux](https://inria.academia.edu/NicolasLeRoux), [Francis Bach](https://www.di.ens.fr/~fbach/) (**2013**). *Minimizing Finite Sums with the Stochastic Average Gradient*. [arXiv:1309.2388](https://arxiv.org/abs/1309.2388) <a id="cite-note-49" href="#cite-ref-49">[49]</a>

**2014**

- [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://pdfs.semanticscholar.org/eb9c/173576577acbb8800bf96aba452d77f1dc19.pdf) » [Shogi](Shogi "Shogi") <a id="cite-note-50" href="#cite-ref-50">[50]</a>
- [Aryan Mokhtari](https://scholar.google.com/citations?user=glcep6EAAAAJ&hl=en), [Alejandro Ribeiro](https://scholar.google.com/citations?user=7mrPM4kAAAAJ&hl=en) (**2014**). *RES: Regularized Stochastic BFGS Algorithm*. [arXiv:1401.7625](https://arxiv.org/abs/1401.7625) <a id="cite-note-51" href="#cite-ref-51">[51]</a>
- [Jemin Hwangbo](http://www.asl.ethz.ch/the-lab/people/person-detail.html?persid=184943), [Christian Gehring](https://www.linkedin.com/in/christian-gehring-1b958395/), [Hannes Sommer](http://www.asl.ethz.ch/the-lab/people/person-detail.html?persid=186652), [Roland Siegwart](http://www.asl.ethz.ch/the-lab/people/person-detail.html?persid=29981), [Jonas Buchli](http://www.adrl.ethz.ch/doku.php/adrl:people:jbuchli) (**2014**). *ROCK∗ — Efficient black-box optimization for policy learning*. [Humanoids, 2014](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7028729) » [Rockstar](Automated_Tuning#Rockstar "Automated Tuning")
- [Yann Dauphin](Mathematician#YDauphin "Mathematician"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Caglar Gulcehre](Mathematician#CGulcehre "Mathematician"), [Kyunghyun Cho](Mathematician#KCho "Mathematician"), [Surya Ganguli](Mathematician#SGanguli "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician") (**2014**). *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization*. [arXiv:1406.2572](https://arxiv.org/abs/1406.2572) <a id="cite-note-52" href="#cite-ref-52">[52]</a>
- [James Martens](https://arxiv.org/find/cs/1/au:+Martens_J/0/1/0/all/0/1) (**2014, 2017**). *New insights and perspectives on the natural gradient method*. [arXiv:1412.1193](https://arxiv.org/abs/1412.1193)

## 2015 ...

- [Diederik P. Kingma](https://scholar.google.nl/citations?user=yyIoQu4AAAAJ), [Jimmy Lei Ba](https://scholar.google.ca/citations?user=ymzxRhAAAAAJ&hl=en) (**2015**). *Adam: A Method for Stochastic Optimization*. [arXiv:1412.6980v8](https://arxiv.org/abs/1412.6980v8), [ICLR 2015](http://www.iclr.cc/doku.php?id=iclr2015:main) <a id="cite-note-53" href="#cite-ref-53">[53]</a>
- [Aryan Mokhtari](https://scholar.google.com/citations?user=glcep6EAAAAJ&hl=en), [Alejandro Ribeiro](https://scholar.google.com/citations?user=7mrPM4kAAAAJ&hl=en) (**2015**). *Global Convergence of Online Limited Memory BFGS*. [Journal of Machine Learning Research](https://en.wikipedia.org/wiki/Journal_of_Machine_Learning_Research), Vol. 16, [pdf](http://www.jmlr.org/papers/volume16/mokhtari15a/mokhtari15a.pdf) <a id="cite-note-54" href="#cite-ref-54">[54]</a> <a id="cite-note-55" href="#cite-ref-55">[55]</a>
- [Ilya Loshchilov](Ilya_Loshchilov "Ilya Loshchilov") (**2015**). *LM-CMA: an Alternative to L-BFGS for Large Scale Black-box Optimization*. [arXiv:1511.00221](https://arxiv.org/abs/1511.00221) <a id="cite-note-56" href="#cite-ref-56">[56]</a> <a id="cite-note-57" href="#cite-ref-57">[57]</a>

**2016**

- [Diogo Real](index.php?title=Diogo_Real&action=edit&redlink=1 "Diogo Real (page does not exist)"), [Alan Blair](Alan_Blair "Alan Blair") (**2016**). *[Learning a multi-player chess game with TreeStrap](https://ieeexplore.ieee.org/document/7743850/)*. [CEC 2016](https://dblp.uni-trier.de/db/conf/cec/cec2016.html)
- [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2016**). *[Coevolutionary CMA-ES for Knowledge-Free Learning of Game Position Evaluation](https://ieeexplore.ieee.org/document/7180338)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 8, No. 4 <a id="cite-note-58" href="#cite-ref-58">[58]</a>
- [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2016**). *[The performance profile: A multi–criteria performance evaluation method for test–based problems](https://content.sciendo.com/view/journals/amcs/26/1/article-p215.xml)*. [International Journal of Applied Mathematics and Computer Science](https://en.wikipedia.org/wiki/International_Journal_of_Applied_Mathematics_and_Computer_Science), Vol. 26, No. 1

**2017**

- [Sebastian Ruder](http://ruder.io/) (**2017**). *[An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)*. [arXiv:1609.04747v2](https://arxiv.org/abs/1609.04747v2) <a id="cite-note-59" href="#cite-ref-59">[59]</a>
- [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Gang-Yu Fan](index.php?title=Gang-Yu_Fan&action=edit&redlink=1 "Gang-Yu Fan (page does not exist)"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Chih-Wen Hsueh](Chih-Wen_Hsueh "Chih-Wen Hsueh"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2017**). *[Validating and Fine-Tuning of Game Evaluation Functions Using Endgame Databases](https://link.springer.com/chapter/10.1007/978-3-319-75931-9_10)*. [CGW@IJCAI 2017](Conferences#IJCAI2017 "Conferences")

**2018**

- [Takafumi Nakamichi](index.php?title=Takafumi_Nakamichi&action=edit&redlink=1 "Takafumi Nakamichi (page does not exist)"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2018**). *Adjusting the evaluation function for weakening the competency level of a computer shogi program*. [ICGA Journal, Vol. 40, No. 1](ICGA_Journal#40_1 "ICGA Journal")
- [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Gang-Yu Fan](index.php?title=Gang-Yu_Fan&action=edit&redlink=1 "Gang-Yu Fan (page does not exist)"), [Chih-Wen Hsueh](Chih-Wen_Hsueh "Chih-Wen Hsueh"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2018**). *Using Chinese dark chess endgame databases to validate and fine-tune game evaluation functions*. [ICGA Journal, Vol. 40, No. 2](ICGA_Journal#40_2 "ICGA Journal") » [Chinese Dark Chess](Chinese_Dark_Chess "Chinese Dark Chess"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Tinghan Wei](index.php?title=Tinghan_Wei&action=edit&redlink=1 "Tinghan Wei (page does not exist)") (**2018**). *Comparison Training for Computer Chinese Chess*. [arXiv:1801.07411](https://arxiv.org/abs/1801.07411) <a id="cite-note-60" href="#cite-ref-60">[60]</a>
- [Jeremy Rapin](index.php?title=Jeremy_Rapin&action=edit&redlink=1 "Jeremy Rapin (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2018**). *Nevergrad - A gradient-free optimization platform*. [GitHub - facebookresearch/nevergrad: A Python toolbox for performing gradient-free optimization](https://github.com/facebookresearch/nevergrad)

## 2020 ...

- [Andrew Grant](Andrew_Grant "Andrew Grant") (**2020**). *Evaluation & Tuning in Chess Engines*. [pdf](https://github.com/AndyGrant/Ethereal/blob/master/Tuning.pdf) <a id="cite-note-61" href="#cite-ref-61">[61]</a>

## Forum Posts

## 1997 ...

- [Evolutionary Evaluation](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/77f10f072e907302) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 09, 1997 » [Evaluation](Evaluation "Evaluation")
- [Deep Blue eval function tuning technique](https://www.stmintz.com/ccc/index.php?id=13794) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 08, 1998 » [Deep Blue](Deep_Blue "Deep Blue") <a id="cite-note-62" href="#cite-ref-62">[62]</a>
- [Automated Tuning](https://www.stmintz.com/ccc/index.php?id=13968) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 12, 1998
- [Pattern Matching -- Avoiding Hand-Tuning](https://www.stmintz.com/ccc/index.php?id=14472) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 21, 1998
- [Speaking of "Evaluate"](https://www.stmintz.com/ccc/index.php?id=28362) by [Danniel Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), September 29, 1998
- [Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28584) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), October 01, 1998 » [TD-learning](Temporal_Difference_Learning "Temporal Difference Learning"), [KnightCap](KnightCap "KnightCap")

## 2000 ...

- [Deep Thought's tuning code and eval function!](https://www.stmintz.com/ccc/index.php?id=128297) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), September 05, 2000 » [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought")
- [learning to tune parameters by comp-comp games](https://www.stmintz.com/ccc/index.php?id=146691) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), December 28, 2000
- [Automatic Eval Tuning](https://www.stmintz.com/ccc/index.php?id=177538) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), June 29, 2001
- [deep blue's automatic tuning of evaluation function](https://www.stmintz.com/ccc/index.php?id=290239) by Emerson Tan, [CCC](CCC "CCC"), March 22, 2003
- [evaluationfunction tuning](https://www.stmintz.com/ccc/index.php?id=314498) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](CCC "CCC"), September 07, 2003
- [evaluation tuning tricks](https://www.stmintz.com/ccc/index.php?id=355083) by [Peter Alloysius](Peter_Aloysius_Harjanto "Peter Aloysius Harjanto"), [CCC](CCC "CCC"), March 17, 2004

## 2005 ...

- ["learning" or "tuning" programs](https://www.stmintz.com/ccc/index.php?id=487022) by [Sean Mintz](index.php?title=Sean_Mintz&action=edit&redlink=1 "Sean Mintz (page does not exist)"), [CCC](CCC "CCC"), February 15, 2006
- [Adjusting weights the Deep Blue way](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49450) by [Tony van Roon-Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 29, 2008 » [Deep Blue](Deep_Blue "Deep Blue")

[Re: Adjusting weights the Deep Blue way](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49450&start=3) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 01, 2008

- [Tuning the eval](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49818) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 02, 2009
- [Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 01, 2009

## [Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009 <a id="cite-note-63" href="#cite-ref-63">[63]</a> 2010 ...

- [Revisiting GA's for tuning evaluation weights](http://www.talkchess.com/forum/viewtopic.php?t=31445) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), January 03, 2010
- [Idea for Automatic Calibration of Evaluation Function...](http://www.talkchess.com/forum/viewtopic.php?t=31935) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 22, 2010
- [Re: TEST position TCEC5- Houdini 1.03a-DRybka4 1-0](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=378648&t=36829) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), November 30, 2010
- [Parameter tuning](http://www.talkchess.com/forum/viewtopic.php?t=38412) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
- [Ahhh... the holy grail of computer chess](http://www.talkchess.com/forum/viewtopic.php?t=40166) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), August 23, 2011
- [CLOP for Noisy Black-Box Parameter Optimization](http://www.talkchess.com/forum/viewtopic.php?p=421995) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), September 01, 2011 <a id="cite-note-64" href="#cite-ref-64">[64]</a>
- [Tuning again](http://www.talkchess.com/forum/viewtopic.php?t=40964) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 01, 2011
- [What is the most difficult and danger feature to tune it?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42283) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), February 02, 2012
- \[Ban: Automatic Learning of Evaluation [...](http://www.open-chess.org/viewtopic.php?f=5&t=1954)\] by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 10, 2012 <a id="cite-note-65" href="#cite-ref-65">[65]</a>

**2014**

- [How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), January 07, 2014

[Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=10) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 08, 2014
[The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=26) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
[Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=27) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 31, 2014 » [Cross-entropy](https://en.wikipedia.org/wiki/Cross_entropy)

- [Tuning eval](http://www.talkchess.com/forum/viewtopic.php?t=53526) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), September 01, 2014
- [Tune cut margins with Texel/gaviota tuning method](http://www.talkchess.com/forum/viewtopic.php?t=53657) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 11, 2014
- [Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545) by Hrvoje Horvatic, [CCC](CCC "CCC"), December 04, 2014 » [PBIL](Genetic_Programming#PBIL "Genetic Programming")

## 2015 ...

- [MMTO for evaluation learning](http://www.talkchess.com/forum/viewtopic.php?t=55084) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 25, 2015 <a id="cite-note-66" href="#cite-ref-66">[66]</a>
- [Experiments with eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=55621) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 10, 2015 » [Arasan](Arasan "Arasan"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 18, 2015 » [Zurichess](Zurichess "Zurichess"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") <a id="cite-note-67" href="#cite-ref-67">[67]</a>

[Re: txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696&start=108) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2016 » [SmarThink](SmarThink "SmarThink")

- [Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), April 30, 2015 » [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")

[Re: Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168&start=36) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), May 04, 2015

- [New Idea For Automated Tuning](http://www.talkchess.com/forum/viewtopic.php?t=56377) by Jordan Bray, [CCC](CCC "CCC"), May 16, 2015
- [Evaluation Tuning](http://www.talkchess.com/forum/viewtopic.php?t=57225) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), August 09, 2015
- [Genetical tuning](http://www.talkchess.com/forum/viewtopic.php?t=57246) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), August 11, 2015 » [Genetic Programming](Genetic_Programming "Genetic Programming")

[Re: Genetical tuning](http://www.talkchess.com/forum/viewtopic.php?t=57246&start=34) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), August 20, 2015

- [Some musings about search](http://www.talkchess.com/forum/viewtopic.php?t=57270) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 14, 2015 » [Search](Search "Search")
- [td-leaf](http://www.talkchess.com/forum/viewtopic.php?t=57860) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), October 06, 2015
- [tensorflow](http://www.talkchess.com/forum/viewtopic.php?t=58211) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 10, 2015 <a id="cite-note-68" href="#cite-ref-68">[68]</a>

**2016**

- [pawn hash and eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=59319) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), February 21, 2016 » [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Tuning](http://www.open-chess.org/viewtopic.php?f=5&t=2987) by ppyvabw, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 11, 2016 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [GreKo 2015 ML: tuning evaluation (article in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=60902) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 22, 2016 » [GreKo](GreKo "GreKo"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [A database for learning evaluation functions](http://www.talkchess.com/forum/viewtopic.php?t=61861) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 28, 2016 » [Evaluation](Evaluation "Evaluation"), [Learning](Learning "Learning"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [CLOP: when to stop?](http://www.talkchess.com/forum/viewtopic.php?t=62012) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), November 07, 2016 » [CLOP](CLOP "CLOP")

[Re: CLOP: when to stop?](http://www.talkchess.com/forum/viewtopic.php?t=62012&start=6) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 08, 2016 <a id="cite-note-69" href="#cite-ref-69">[69]</a>

- [C++ code for tuning evaluation function parameters](http://www.talkchess.com/forum/viewtopic.php?t=62056) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 10, 2016 » [RuyTune](RuyTune "RuyTune")

**2017**

- [improved evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=63408) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 11, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"), [Zurichess](Zurichess "Zurichess")
- [automated tuning](http://www.talkchess.com/forum/viewtopic.php?t=63425) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), March 13, 2017
- [Parameter tuning with multi objective optimization](http://www.talkchess.com/forum/viewtopic.php?t=63926) by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni"), [CCC](CCC "CCC"), May 07, 2017 » [Napoleon](Napoleon "Napoleon")
- [Evaluation Tuning: When To Stop?](http://www.talkchess.com/forum/viewtopic.php?t=64119) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), May 29, 2017
- [Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), June 05, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")

[Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=35) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), June 07, 2017
[Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=42) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), July 20, 2017 » [Python](Python "Python")
[Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=46) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 23, 2017

- [Approximating Stockfish's Evaluation by PSQTs](http://www.talkchess.com/forum/viewtopic.php?t=64972) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 23, 2017 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [Stockfish](Stockfish "Stockfish")
- [Ab-initio evaluation tuning](http://www.talkchess.com/forum/viewtopic.php?t=65039) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), August 30, 2017
- [ROCK\* black-box optimizer for chess](http://www.talkchess.com/forum/viewtopic.php?t=65045) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 31, 2017 » [ROCK\*](Automated_Tuning#ROCK "Automated Tuning"), [Rockstar](Automated_Tuning#Rockstar "Automated Tuning")
- [tuning via maximizing likelihood](http://www.talkchess.com/forum/viewtopic.php?t=65373) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 04, 2017 <a id="cite-note-70" href="#cite-ref-70">[70]</a>
- [tool to create derivates of a given function](http://www.talkchess.com/forum/viewtopic.php?t=65660) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 07, 2017

[Re: tool to create derivates of a given function](http://www.talkchess.com/forum/viewtopic.php?t=65660&start=2) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 07, 2017 <a id="cite-note-71" href="#cite-ref-71">[71]</a>

- [tuning for the uninformed](http://www.talkchess.com/forum/viewtopic.php?t=65799) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), November 23, 2017

**2018**

- [tuning info](http://www.talkchess.com/forum/viewtopic.php?t=66221) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), January 03, 2018
- [3 million games for training neural networks](http://www.talkchess.com/forum/viewtopic.php?t=66681) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 24, 2018 » [Neural Networks](Neural_Networks "Neural Networks")
- [Tuning floats](https://groups.google.com/d/msg/fishcooking/XnLmUP_78iw/QgMZzmeVBgAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 12, 2018
- [Introducing PET](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67831) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 27, 2018 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite")
- [Texel tuning speed](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68326) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 29, 2018 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [methods for tuning coefficients](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68753) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), October 28, 2018
- [Particle Swarm Optimization Code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69035) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), November 24, 2018 » [MadChess](MadChess "MadChess")
- [Gradient Descent Introduction](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69207) by [Desperado](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), December 09, 2018

**2019**

- [Automated tuning... finally... (Topple v0.3.0)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69532) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), January 08, 2019 » [Topple](Topple "Topple")
- [New Tool for Tuning with Skopt](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71650) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 25, 2019 <a id="cite-note-72" href="#cite-ref-72">[72]</a>
- [TD(1)](https://www.game-ai-forum.org/viewtopic.php?f=21&t=695) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [Game-AI Forum](Computer_Chess_Forums "Computer Chess Forums"), November 20, 2019 » [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")
- [high dimensional optimization](https://groups.google.com/d/msg/fishcooking/wOfRuzTSi_8/VgjN8MmSBQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 27, 2019 <a id="cite-note-73" href="#cite-ref-73">[73]</a>

## 2020 ...

- [Board adaptive / tuning evaluation function - no NN/AI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72810) by Moritz Gedig, [CCC](CCC "CCC"), January 14, 2020
- [Pawn structure tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73629) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), April 11, 2020 » [Pawn Structure](Pawn_Structure "Pawn Structure"), [Ethereal](Ethereal "Ethereal")
- [Learning/Tuning in SlowChess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74184) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2020 » [Slow Chess](Slow_Chess "Slow Chess")
- [Great input about Bayesian optimization of noisy function methods](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74209) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 16, 2020
- [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020 » [Ethereal](Ethereal "Ethereal")
- [Train a neural network evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74955) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 01, 2020 » [NNUE](NNUE "NNUE")
- [Speeding Up The Tuner](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75012) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), September 06, 2020
- [Yet another parameter tuner using optuna framework](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75104) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), September 14, 2020

[Re: Yet another parameter tuner using optuna framework](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75104&start=15) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt"), [CCC](CCC "CCC"), September 16, 2020 <a id="cite-note-74" href="#cite-ref-74">[74]</a>

- [evaluation tuning - where to start?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75234) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 27, 2020
- [How to calculate piece weights with logistic regression?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75267) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 01, 2020 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis"), [Point Value](Point_Value "Point Value")
- [Unsupervised reinforcement tuning from zero](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75411) by Madeleine Birchfield, [CCC](CCC "CCC"), October 16, 2020 » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
- [Laskas parameter optimizer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76024) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), December 09, 2020

**2021**

- [Re: Wasp 4.5 Released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=76205&start=14) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), January 03, 2021 » [Wasp](Wasp "Wasp")
- [How to calc the derivative for gradient descent?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76227) by Brian Neal, [CCC](CCC "CCC"), January 04, 2021
- [Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 05, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Tapered Evaluation and MSE (Texel Tuning)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76265) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 10, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"), [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Training data](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76288) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 12, 2021
- [Why using the game result instead of evaluation scores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76292) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 12, 2021
- [Using Mini-Batch for tunig](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76294) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 12, 2021
- [Texel tuning variant](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76380) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), January 21, 2021
- [Parameter Tuning Algorithm](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76385) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 21, 2021
- [Mabigat - hyperparameter optimizer for NNUE net](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76917) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), March 22, 2021 » [NNUE](NNUE "NNUE")
- [Tuning search parameters](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77118) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 18, 2021
- [Search tuned depending on TC](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77318) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 16, 2021
- [A hybrid of SPSA and local optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77420) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), June 01, 2021 » [SPSA](SPSA "SPSA"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Just an untested idea](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77715) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 12, 2021 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Tuning Search Parameters](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78896) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCC](CCC "CCC"), December 16, 2021
- [Eval tuning data](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78958) by gaard, [CCC](CCC "CCC"), December 22, 2021

**2022**

- [SGD basics](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79301) by [Desperado](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), February 06, 2022 » [SGD](Automated_Tuning#SGD "Automated Tuning")
- [Re: Devlog of Leorik - A.k.a. how to tune high-quality PSTs from scratch (material values) in 20 seconds](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=127) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), March 28, 2022 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [Leorik](Leorik "Leorik")

## External Links

- [automatic - Wiktionary](https://en.wiktionary.org/wiki/automatic)
- [Automation from Wikipedia](https://en.wikipedia.org/wiki/Automation)
- [tuning - Wiktionary](https://en.wiktionary.org/wiki/tuning)
- [Tuning from Wikipedia](https://en.wikipedia.org/wiki/Tuning)

## [Engine tuning from Wikipedia](https://en.wikipedia.org/wiki/Engine_tuning) [Self-tuning from Wikipedia](https://en.wikipedia.org/wiki/Self-tuning) Engine Tuning

- [Automatic Tuning & Learning for Slow Chess Blitz Classic](https://www.3dkingdoms.com/chess/learning.html) by by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer") » [Slow Chess](Slow_Chess "Slow Chess") <a id="cite-note-75" href="#cite-ref-75">[75]</a>
- [Chess Tuning Tools](https://chess-tuning-tools.readthedocs.io/en/latest/) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt")
- [Practical Engine Tuning](http://rebel13.nl/rebel13/pet.html) by [Ed Schröder](Ed_Schroder "Ed Schroder"), June 2018 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite") <a id="cite-note-76" href="#cite-ref-76">[76]</a>

## Optimization

- [optimization - Wiktionary](https://en.wiktionary.org/wiki/optimization)

[optimize - Wiktionary](https://en.wiktionary.org/wiki/optimize)

- [Mathematical optimization from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_optimization)
- [Operations research from Wikipedia](https://en.wikipedia.org/wiki/Operations_research)
- [Optimization problem from Wikipedia](https://en.wikipedia.org/wiki/Optimization_problem)
- [Duality (optimization) from Wikipedia](<https://en.wikipedia.org/wiki/Duality_(optimization)>)
- [Local search (optimization) from Wikipedia](https://en.wikipedia.org/wiki/Local_search_%28optimization%29)
- [Iterated local search from Wikipedia](https://en.wikipedia.org/wiki/Iterated_local_search)
- [Global optimization from Wikipedia](https://en.wikipedia.org/wiki/Global_optimization)
- [Bayesian optimization from Wikipedia](https://en.wikipedia.org/wiki/Bayesian_optimization)
- [Broyden–Fletcher–Goldfarb–Shanno algorithm from Wikipedia](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
- [CLOP for Noisy Black-Box Parameter Optimization](http://remi.coulom.free.fr/CLOP/) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") » [CLOP](CLOP "CLOP") <a id="cite-note-77" href="#cite-ref-77">[77]</a> <a id="cite-note-78" href="#cite-ref-78">[78]</a>
- [Conjugate gradient method from Wikipedia](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
- [Convex optimization from Wikipedia](https://en.wikipedia.org/wiki/Convex_optimization)

[Entropy maximization from Wikipedia](https://en.wikipedia.org/wiki/Entropy_maximization)
[Linear programming from Wikipedia](https://en.wikipedia.org/wiki/Linear_programming)
[Nonlinear programming from Wikipedia](https://en.wikipedia.org/wiki/Nonlinear_programming)
[Simplex algorithm from Wikipedia](https://en.wikipedia.org/wiki/Simplex_algorithm)

- [Differential evolution from Wikipedia](https://en.wikipedia.org/wiki/Differential_evolution)
- [Evolutionary computation from Wikipedia](https://en.wikipedia.org/wiki/Evolutionary_computation)
- [Gauss–Newton algorithm from Wikipedia](https://en.wikipedia.org/wiki/Gauss%E2%80%93Newton_algorithm)
- [Genetic algorithm from Wikipedia](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [Gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Gradient_descent)
- [Hill climbing from Wikipedia](https://en.wikipedia.org/wiki/Hill_climbing)
- [Hyperparameter optimization from Wikipedia](https://en.wikipedia.org/wiki/Hyperparameter_optimization)
- [Limited-memory BFGS from Wikipedia](https://en.wikipedia.org/wiki/Limited-memory_BFGS) <a id="cite-note-79" href="#cite-ref-79">[79]</a>
- [Loss function from Wikipedia](https://en.wikipedia.org/wiki/Loss_function)
- [Nelder–Mead method from Wikipedia](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) » [Amoeba](Amoeba "Amoeba"), [Murka](Murka "Murka")
- [Newton's method in optimization from Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization)
- [NOMAD - A blackbox optimization software](https://www.gerad.ca/nomad/Project/Home.html) <a id="cite-note-80" href="#cite-ref-80">[80]</a>
- [NEWUOA from Wikipedia](https://en.wikipedia.org/wiki/NEWUOA) <a id="cite-note-81" href="#cite-ref-81">[81]</a>
- [Particle swarm optimization from Wikipedia](https://en.wikipedia.org/wiki/Particle_swarm_optimization)
- [Population-based incremental learning (PBIL) - Wikipedia](https://en.wikipedia.org/wiki/Population-based_incremental_learning) <a id="cite-note-82" href="#cite-ref-82">[82]</a>
- [Population Based Incremental Learning (PBIL)](http://macechess.blogspot.de/2013/03/population-based-incremental-learning.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), March 16, 2013 » [iCE](ICE "ICE")
- [Simulated annealing from Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing)
- [Skopt (Scikit-Optimize) · GitHub](https://github.com/scikit-optimize)
- [Welcome to Bayes-skopt’s documentation!](https://bayes-skopt.readthedocs.io/en/latest/)
- [Stochastic optimization from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_optimization)

## [Simultaneous perturbation stochastic approximation (SPSA) - Wikipedia](https://en.wikipedia.org/wiki/Simultaneous_perturbation_stochastic_approximation) [SPSA Algorithm](https://www.jhuapl.edu/spsa/) [Stochastic approximation from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_approximation) [Stochastic gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (SGD) [AdaGrad from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#AdaGrad) Machine Learning

- [Machine learning from Wikipedia](https://en.wikipedia.org/wiki/Machine_learning)
- [List of machine learning concepts from Wikipedia](https://en.wikipedia.org/wiki/List_of_machine_learning_concepts)
- [Backpropagation from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation) » [Neural Networks](Neural_Networks "Neural Networks")
- [Reinforcement learning from Wikipedia](https://en.wikipedia.org/wiki/Reinforcement_learning)

[reinforcement - Wiktionary](https://en.wiktionary.org/wiki/reinforcement)
[reinforce - Wiktionary](https://en.wiktionary.org/wiki/reinforce)

- [Supervised learning from Wikipedia](https://en.wikipedia.org/wiki/Supervised_learning)

[supervisor - Wiktionary](https://en.wiktionary.org/wiki/supervisor)

- [Temporal Difference Learning from Wikipeadia](https://en.wikipedia.org/wiki/Temporal_difference_learning)

[temporal - Wiktionary](https://en.wiktionary.org/wiki/temporal)

- [Unsupervised learning from Wikipedia](https://en.wikipedia.org/wiki/Unsupervised_learning)

## Statistics/Regression Analysis

- [Statistics from Wikipedia](https://en.wikipedia.org/wiki/Statistics)
- [Regression from Wikipedia](https://en.wikipedia.org/wiki/Regression)

[regression - Wiktionary](https://en.wiktionary.org/wiki/regression)
[regress - Wiktionary](https://en.wiktionary.org/wiki/regress)

- [Regression analysis from Wikipedia](https://en.wikipedia.org/wiki/Regression_analysis)
- [Outline of regression analysis from Wikipedia](https://en.wikipedia.org/wiki/Outline_of_regression_analysis)
- [Bayesian linear regression from Wikipedia](https://en.wikipedia.org/wiki/Bayesian_linear_regression)
- [Bayesian multivariate linear regression from Wikipedia](https://en.wikipedia.org/wiki/Bayesian_multivariate_linear_regression)
- [Correlation does not imply causation from Wikipedia](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
- [Cross entropy from Wikipedia](https://en.wikipedia.org/wiki/Cross_entropy)
- [Elastic net regularization from Wikipedia](https://en.wikipedia.org/wiki/Elastic_net_regularization)
- [LASSO from Wikipedia](<https://en.wikipedia.org/wiki/Lasso_(statistics)>)
- [Likelihood function from Wikipedia](https://en.wikipedia.org/wiki/Likelihood_function)
- [Linear regression from Wikipedia](https://en.wikipedia.org/wiki/Linear_regression)
- [Linear discriminant analysis from Wikipedia](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)
- [Logistic regression from Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
- [Kernel Fisher discriminant analysis from Wikipedia](https://en.wikipedia.org/wiki/Kernel_Fisher_discriminant_analysis)
- [Maximum likelihood estimation from Wikipedia](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
- [Mean squared error from Wikipedia](https://en.wikipedia.org/wiki/Mean_squared_error)
- [Nonlinear regression from Wikipedia](https://en.wikipedia.org/wiki/Nonlinear_regression)
- [Ordinary least squares from Wikipedia](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [Polynomial regression from Wikipedia](https://en.wikipedia.org/wiki/Polynomial_regression)
- [Simple linear regression from Wikipedia](https://en.wikipedia.org/wiki/Simple_linear_regression)
- [Tikhonov regularization (Ridge regression) from Wikipedia](https://en.wikipedia.org/wiki/Tikhonov_regularization)

## Code

- [GitHub - facebookresearch/nevergrad: A Python toolbox for performing gradient-free optimization](https://github.com/facebookresearch/nevergrad)
- [GitHub - fsmosca/Optuna-Game-Parameter-Tuner: A game search and evaluation parameter tuner using optuna framework](https://github.com/fsmosca/Optuna-Game-Parameter-Tuner) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca") » [Deuterium](Deuterium "Deuterium") <a id="cite-note-83" href="#cite-ref-83">[83]</a>
- [GitHub - fsmosca/Lakas: Game parameter optimizer using nevergrad framework](https://github.com/fsmosca/Lakas) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca") <a id="cite-note-84" href="#cite-ref-84">[84]</a>
- [GitHub - fsmosca/Mabigat: NNUE parameter optimizer](https://github.com/fsmosca/Mabigat) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca") » [NNUE](NNUE "NNUE") <a id="cite-note-85" href="#cite-ref-85">[85]</a>
- [GitHub - kiudee/bayes-skopt: A fully Bayesian implementation of sequential model-based optimization](https://github.com/kiudee/bayes-skopt) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt") » [Fat Fritz](Fat_Fritz "Fat Fritz") <a id="cite-note-86" href="#cite-ref-86">[86]</a>
- [GitHub - kiudee/chess-tuning-tools](https://github.com/kiudee/chess-tuning-tools) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt") » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [GitHub - krasserm/bayesian-machine-learning: Notebooks about Bayesian methods for machine learning](https://github.com/krasserm/bayesian-machine-learning) by [Martin Krasser](https://krasserm.github.io/) <a id="cite-note-87" href="#cite-ref-87">[87]</a>
- [GitHub - thomasahle/noisy-bayesian-optimization: Bayesian Optimization for very Noisy functions](https://github.com/thomasahle/noisy-bayesian-optimization) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle") » [FastChess](FastChess "FastChess")
- [GitHub - scikit-optimize/scikit-optimize: Sequential model-based optimization with a `scipy.optimize` interface](https://github.com/scikit-optimize/scikit-optimize)
- [Rockstar: Implementation of ROCK\* algorithm (Gaussian kernel regression + natural gradient descent) for optimisation | GitHub](https://github.com/lantonov/Rockstar) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov") and [Joona Kiiski](Joona_Kiiski "Joona Kiiski") » [ROCK\*](Automated_Tuning#ROCK "Automated Tuning") <a id="cite-note-88" href="#cite-ref-88">[88]</a>
- [SPSA Tuner for Stockfish Chess Engine | GitHub](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski") » [Stockfish](Stockfish "Stockfish"), [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")

## Misc

- [The Next Step Quintet](Category:The_Next_Step_Quintet "Category:The Next Step Quintet") feat. [Tivon Pennicott](http://www.tivonpennicott.com/) - [Regression](http://www.discogs.com/Next-Step-Quintet-The-Next-Step-Quintet/release/4970720), [KerameioBar](https://el-gr.facebook.com/KerameioBar) [Athens](https://en.wikipedia.org/wiki/Athens), [Greece](https://en.wikipedia.org/wiki/Greece), September 2014, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A vintage motor engine tester located at the [James Hall museum of Transport](https://en.wikipedia.org/wiki/James_Hall_Transport_Museum), [Johannesburg](https://en.wikipedia.org/wiki/Johannesburg), [South Africa](https://en.wikipedia.org/wiki/South_Africa) - [Engine tuning from Wikipedia](https://en.wikipedia.org/wiki/Engine_tuning)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Learning Search Control in Adversary Games*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), pp. 157-174. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01b.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**). *Machine Learning in Games: A Survey*. [Austrian Research Institute for Artificial Intelligence](https://en.wikipedia.org/wiki/Austrian_Research_Institute_for_Artificial_Intelligence), OEFAI-TR-2000-3, [pdf](https://fmfi-uk.hq.sk/Informatika/Strojove%20Ucenie/oefai-tr-2000-31.pdf) - Chapter 4, Evaluation Function Tuning
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Fishtest Distributed Testing Framework](http://www.talkchess.com/forum/viewtopic.php?t=47885) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 01, 2013
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Zappa Report](https://www.stmintz.com/ccc/index.php?id=475521) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), December 30, 2005 » [Zappa](Zappa "Zappa")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1993**). *On Telescoping Linear Evaluation Functions.* [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal"), pp. 91-94
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1959**). *[Some Studies in Machine Learning Using the Game of Checkers](http://domino.watson.ibm.com/tchjr/journalindex.nsf/600cc5649e2871db852568150060213c/39a870213169f45685256bfa00683d74!OpenDocument)*. IBM Journal July 1959
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Richard Sutton](Richard_Sutton "Richard Sutton") (**1988**). *Learning to Predict by the Methods of Temporal Differences*. [Machine Learning](https://en.wikipedia.org/wiki/Machine_Learning_%28journal%29), Vol. 3, No. 1, [pdf](http://webdocs.cs.ualberta.ca/~sutton/papers/sutton-88.pdf)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1994**). *TD-Gammon, a Self-Teaching Backgammon Program, Achieves Master-Level Play*. [Neural Computation Vol. 6, No. 2](http://www.informatik.uni-trier.de/~ley/db/journals/neco/neco6.html#Tesauro94)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Experiments in Parameter Learning Using Temporal Differences*. [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal"), [pdf](http://cs.anu.edu.au/%7ELex.Weaver/pub_sem/publications/ICCA-98_equiv.pdf)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [The Cilkchess Parallel Chess Program](http://supertech.csail.mit.edu/chess/)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [EXchess](EXchess "EXchess") also uses [CLOP](CLOP "CLOP")
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Arthur Samuel](Arthur_Samuel "Arthur Samuel") (**1967**). *Some Studies in Machine Learning. Using the Game of Checkers. II-Recent Progress*. [pdf](http://researcher.watson.ibm.com/researcher/files/us-beygel/samuel-checkers.pdf)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2000**). *Machine Learning in Games: A Survey*. [Austrian Research Institute for Artificial Intelligence](https://en.wikipedia.org/wiki/Austrian_Research_Institute_for_Artificial_Intelligence), OEFAI-TR-2000-3, [pdf](https://fmfi-uk.hq.sk/Informatika/Strojove%20Ucenie/oefai-tr-2000-31.pdf)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Thomas Nitsche](Thomas_Nitsche "Thomas Nitsche") (**1982**). *A Learning Chess Program.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *Evaluation-Function Factors*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/evaluation.pdf)
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Andreas Nowatzyk](Andreas_Nowatzyk "Andreas Nowatzyk") (**1990**). *[A Grandmaster Chess Machine](http://www.disi.unige.it/person/DelzannoG/AI2/hsu.html)*. [Scientific American](Scientific_American "Scientific American"), Vol. 263, No. 4, pp. 44-50. ISSN 0036-8733.
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> see *2.1 Learning from Desired Moves in Chess* in [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html)
1. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Joe Culberson](Joe_Culberson "Joe Culberson"), [Norman Treloar](index.php?title=Norman_Treloar&action=edit&redlink=1 "Norman Treloar (page does not exist)"), [Brent Knight](index.php?title=Brent_Knight&action=edit&redlink=1 "Brent Knight (page does not exist)"), [Paul Lu](Paul_Lu "Paul Lu"), [Duane Szafron](Duane_Szafron "Duane Szafron") (**1992**). *A World Championship Caliber Checkers Program*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 53, Nos. 2-3,[ps](http://webdocs.cs.ualberta.ca/%7Ejonathan/Papers/Papers/chinook.ps)
1. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997, 2009**). *[One Jump Ahead](http://www.springer.com/computer/ai/book/978-0-387-76575-4)*. 7. The Case for the Prosecution, pp. 111-114
1. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *[Expected-Outcome: A General Model of Static Evaluation](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=44404)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 2
1. <a id="cite-ref-24" href="#cite-note-24">↑</a> Random data points and their [linear regression](https://en.wikipedia.org/wiki/Linear_regression). [Created](https://commons.wikimedia.org/wiki/File:Linear_regression.svg) with [Sage](https://en.wikipedia.org/wiki/Sage_%28mathematics_software%29) by Sewaqu, November 5, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-25" href="#cite-note-25">↑</a> [Loss function - Use in statistics - Wkipedia](https://en.wikipedia.org/wiki/Loss_function#Use_in_statistics)
1. <a id="cite-ref-26" href="#cite-note-26">↑</a> "Using [cross-entropy error function](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression) instead of [sum of squares](https://en.wikipedia.org/wiki/Mean_squared_error) leads to faster training and improved generalization", from [Sargur Srihari](https://en.wikipedia.org/wiki/Sargur_Srihari), [Neural Network Training](http://www.cedar.buffalo.edu/~srihari/CSE574/Chap5/Chap5.2-Training.pdf) (pdf)
1. <a id="cite-ref-27" href="#cite-note-27">↑</a> [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *[Statistical Feature Combination for the Evaluation of Game Positions](https://www.jair.org/index.php/jair/article/view/10146)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 3
1. <a id="cite-ref-28" href="#cite-note-28">↑</a> [Donald H. Mitchell](Donald_H._Mitchell "Donald H. Mitchell") (**1984**). *Using Features to Evaluate Positions in Experts' and Novices' Othello Games*. Master thesis, Department of Psychology, [Northwestern University](Northwestern_University "Northwestern University"), Evanston, IL
1. <a id="cite-ref-29" href="#cite-note-29">↑</a> [Jens Christensen](Jens_Christensen "Jens Christensen") (**1986**). *[Learning Static Evaluation Functions by Linear Regression](http://link.springer.com/chapter/10.1007/978-1-4613-2279-5_9?no-access=true)*. in [Tom Mitchell](Tom_Mitchell "Tom Mitchell"), [Jaime Carbonell](Jaime_Carbonell "Jaime Carbonell"), [Ryszard Michalski](Ryszard_Michalski "Ryszard Michalski") (**1986**). *[Machine Learning: A Guide to Current Research](http://link.springer.com/book/10.1007/978-1-4613-2279-5)*. The Kluwer International Series in Engineering and Computer Science, Vol. 12
1. <a id="cite-ref-30" href="#cite-note-30">↑</a> [log-linear 1 / (1 + 10^(-s/4)) , s=-10 to 10](http://wolfr.am/1al3d5B) from [Wolfram|Alpha](https://en.wikipedia.org/wiki/Wolfram_Alpha)
1. <a id="cite-ref-31" href="#cite-note-31">↑</a> [Re: Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168&start=36) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), May 04, 2015
1. <a id="cite-ref-32" href="#cite-note-32">↑</a> [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *[Statistical Feature Combination for the Evaluation of Game Positions](https://www.jair.org/index.php/jair/article/view/10146)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 3
1. <a id="cite-ref-33" href="#cite-note-33">↑</a> [LOGISTELLO's Homepage](https://skatgame.net/mburo/log.html)
1. <a id="cite-ref-34" href="#cite-note-34">↑</a> [Arkadiusz Paterek](Arkadiusz_Paterek "Arkadiusz Paterek") (**2004**). *Modelowanie funkcji oceniającej w grach*. [University of Warsaw](University_of_Warsaw "University of Warsaw"), [zipped ps](https://www.mimuw.edu.pl/~paterek/mfog.ps.gz) (Polish, Modeling of an evaluation function in games)
1. <a id="cite-ref-35" href="#cite-note-35">↑</a> [Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009
1. <a id="cite-ref-36" href="#cite-note-36">↑</a> [Amir Ban](Amir_Ban "Amir Ban") (**2012**). *[Automatic Learning of Evaluation, with Applications to Computer Chess](http://www.ratio.huji.ac.il/node/2362)*. Discussion Paper 613, [The Hebrew University of Jerusalem](https://en.wikipedia.org/wiki/Hebrew_University_of_Jerusalem) - Center for the Study of Rationality, [Givat Ram](https://en.wikipedia.org/wiki/Givat_Ram)
1. <a id="cite-ref-37" href="#cite-note-37">↑</a> [Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=10) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 08, 2014
1. <a id="cite-ref-38" href="#cite-note-38">↑</a> [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014
1. <a id="cite-ref-39" href="#cite-note-39">↑</a> [Определяем веса шахматных фигур регрессионным анализом / Хабрахабр](http://habrahabr.ru/post/254753/) by [WinPooh](Vladimir_Medvedev "Vladimir Medvedev"), April 27, 2015 (Russian)
1. <a id="cite-ref-40" href="#cite-note-40">↑</a> [Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), April 30, 2015
1. <a id="cite-ref-41" href="#cite-note-41">↑</a> [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
1. <a id="cite-ref-42" href="#cite-note-42">↑</a> [Re: Adjusting weights the Deep Blue way](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49450&start=3) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 01, 2008
1. <a id="cite-ref-43" href="#cite-note-43">↑</a> [A paper about parameter tuning](http://www.talkchess.com/forum/viewtopic.php?start=0&t=31667) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), January 12, 2010
1. <a id="cite-ref-44" href="#cite-note-44">↑</a> [MATLAB from Wikipedia](https://en.wikipedia.org/wiki/MATLAB)
1. <a id="cite-ref-45" href="#cite-note-45">↑</a> [Adaptive coordinate descent from Wikipedia](https://en.wikipedia.org/wiki/Adaptive_coordinate_descent)
1. <a id="cite-ref-46" href="#cite-note-46">↑</a> [CLOP for Noisy Black-Box Parameter Optimization](http://www.talkchess.com/forum/viewtopic.php?p=421995) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), September 01, 2011
1. <a id="cite-ref-47" href="#cite-note-47">↑</a> [CLOP slides](http://www.talkchess.com/forum/viewtopic.php?t=40987) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), November 03, 2011
1. <a id="cite-ref-48" href="#cite-note-48">↑</a> [thesis on eval function learning in Arimaa](http://www.talkchess.com/forum/viewtopic.php?t=58472) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 04, 2015
1. <a id="cite-ref-49" href="#cite-note-49">↑</a> [Tuning floats](https://groups.google.com/d/msg/fishcooking/XnLmUP_78iw/QgMZzmeVBgAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 12, 2018
1. <a id="cite-ref-50" href="#cite-note-50">↑</a> [MMTO for evaluation learning](http://www.talkchess.com/forum/viewtopic.php?t=55084) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 25, 2015
1. <a id="cite-ref-51" href="#cite-note-51">↑</a>  [Broyden–Fletcher–Goldfarb–Shanno algorithm from Wikipedia](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)
1. <a id="cite-ref-52" href="#cite-note-52">↑</a> [high dimensional optimization](https://groups.google.com/d/msg/fishcooking/wOfRuzTSi_8/VgjN8MmSBQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 27, 2019
1. <a id="cite-ref-53" href="#cite-note-53">↑</a> [Arasan 19.2](http://www.talkchess.com/forum/viewtopic.php?t=61948) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 03, 2016 » [Arasan's Tuning](Arasan#Tuning "Arasan")
1. <a id="cite-ref-54" href="#cite-note-54">↑</a> [Limited-memory BFGS from Wikipedia](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
1. <a id="cite-ref-55" href="#cite-note-55">↑</a> [Re: CLOP: when to stop?](http://www.talkchess.com/forum/viewtopic.php?t=62012&start=6) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 08, 2016
1. <a id="cite-ref-56" href="#cite-note-56">↑</a> [LM-BFGS from Wikipedia](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
1. <a id="cite-ref-57" href="#cite-note-57">↑</a> [LM-CMA source code](https://sites.google.com/site/ecjlmcma/)
1. <a id="cite-ref-58" href="#cite-note-58">↑</a> [CMA-ES from Wikipedia](https://en.wikipedia.org/wiki/CMA-ES)
1. <a id="cite-ref-59" href="#cite-note-59">↑</a> [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=46) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 23, 2017
1. <a id="cite-ref-60" href="#cite-note-60">↑</a> [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=7) by Tony P., [CCC](CCC "CCC"), January 28, 2020 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
1. <a id="cite-ref-61" href="#cite-note-61">↑</a> [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020
1. <a id="cite-ref-62" href="#cite-note-62">↑</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1997**). *Evaluation Tuning for Computer Chess: Linear Discriminant Methods*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")
1. <a id="cite-ref-63" href="#cite-note-63">↑</a> [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014
1. <a id="cite-ref-64" href="#cite-note-64">↑</a> [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2011**). *[CLOP: Confident Local Optimization for Noisy Black-Box Parameter Tuning](http://remi.coulom.free.fr/CLOP/)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
1. <a id="cite-ref-65" href="#cite-note-65">↑</a> [Amir Ban](Amir_Ban "Amir Ban") (**2012**). *[Automatic Learning of Evaluation, with Applications to Computer Chess](http://www.ratio.huji.ac.il/node/2362)*. Discussion Paper 613, [The Hebrew University of Jerusalem](https://en.wikipedia.org/wiki/Hebrew_University_of_Jerusalem) - Center for the Study of Rationality, [Givat Ram](https://en.wikipedia.org/wiki/Givat_Ram)
1. <a id="cite-ref-66" href="#cite-note-66">↑</a> [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://www.jair.org/media/4217/live-4217-7792-jair.pdf)
1. <a id="cite-ref-67" href="#cite-note-67">↑</a> [brtzsnr / txt — Bitbucket](https://bitbucket.org/brtzsnr/txt) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi")
1. <a id="cite-ref-68" href="#cite-note-68">↑</a> [Home — TensorFlow](http://tensorflow.org/)
1. <a id="cite-ref-69" href="#cite-note-69">↑</a> [Limited-memory BFGS from Wikipedia](https://en.wikipedia.org/wiki/Limited-memory_BFGS)
1. <a id="cite-ref-70" href="#cite-note-70">↑</a> [Maximum likelihood estimation from Wikipedia](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)
1. <a id="cite-ref-71" href="#cite-note-71">↑</a> [Jacobian matrix and determinant from WIkipedia](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)
1. <a id="cite-ref-72" href="#cite-note-72">↑</a> [skopt API documentation](https://scikit-optimize.github.io/)
1. <a id="cite-ref-73" href="#cite-note-73">↑</a> [Yann Dauphin](Mathematician#YDauphin "Mathematician"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Caglar Gulcehre](Mathematician#CGulcehre "Mathematician"), [Kyunghyun Cho](Mathematician#KCho "Mathematician"), [Surya Ganguli](Mathematician#SGanguli "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician") (**2014**). *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization*. [arXiv:1406.2572](https://arxiv.org/abs/1406.2572)
1. <a id="cite-ref-74" href="#cite-note-74">↑</a> [Tree-structured Parzen Estimator — Optunity 1.1.0 documentation](https://optunity.readthedocs.io/en/latest/user/solvers/TPE.html)
1. <a id="cite-ref-75" href="#cite-note-75">↑</a> [Learning/Tuning in SlowChess Blitz Classic](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74184) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2020
1. <a id="cite-ref-76" href="#cite-note-76">↑</a> [Introducing PET](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67831) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 27, 2018
1. <a id="cite-ref-77" href="#cite-note-77">↑</a> [Tool for automatic black-box parameter optimization released](http://www.talkchess.com/forum/viewtopic.php?t=35049) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), June 20, 2010
1. <a id="cite-ref-78" href="#cite-note-78">↑</a> [CLOP for Noisy Black-Box Parameter Optimization](http://www.talkchess.com/forum/viewtopic.php?p=421995) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), September 01, 2011
1. <a id="cite-ref-79" href="#cite-note-79">↑</a> [Re: CLOP: when to stop?](http://www.talkchess.com/forum/viewtopic.php?t=62012&start=6) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), November 08, 2016
1. <a id="cite-ref-80" href="#cite-note-80">↑</a> [Re: Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545&start=2) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 06, 2014
1. <a id="cite-ref-81" href="#cite-note-81">↑</a> [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=94) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 12, 2014
1. <a id="cite-ref-82" href="#cite-note-82">↑</a> [Eval tuning - any open source engines with GA or PBIL?](http://www.talkchess.com/forum/viewtopic.php?t=54545) by Hrvoje Horvatic, [CCC](CCC "CCC"), December 04, 2014
1. <a id="cite-ref-83" href="#cite-note-83">↑</a> [Yet another parameter tuner using optuna framework](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75104) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), September 14, 2020
1. <a id="cite-ref-84" href="#cite-note-84">↑</a> [Laskas parameter optimizer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76024) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), December 09, 2020
1. <a id="cite-ref-85" href="#cite-note-85">↑</a> [Mabigat - hyperparameter optimizer for NNUE net](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76917) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), March 22, 2021
1. <a id="cite-ref-86" href="#cite-note-86">↑</a> [Fat Fritz 1.1 update and a small gift](https://en.chessbase.com/post/fat-fritz-update-and-fat-fritz-jr) by [Albert Silver](Albert_Silver "Albert Silver"). [ChessBase News](ChessBase "ChessBase"), March 05, 2020
1. <a id="cite-ref-87" href="#cite-note-87">↑</a> [Great input about Bayesian optimization of noisy function methods](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74209) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 16, 2020
1. <a id="cite-ref-88" href="#cite-note-88">↑</a> [ROCK\* black-box optimizer for chess](http://www.talkchess.com/forum/viewtopic.php?t=65045) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), August 31, 2017

**[Up one Level](Home "Home")**

