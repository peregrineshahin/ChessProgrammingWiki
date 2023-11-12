---
title: EvaluationLinear
---
**[Home](Home "Home") * Evaluation**

[](https://www.pinterest.de/pin/58476495131654514/) [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Schach-Theorie, 1937 [[1]](#cite_note-1)
**Evaluation**,

a [heuristic function](<https://en.wikipedia.org/wiki/Heuristic_(computer_science)>) to determine the [relative value](Score "Score") of a [position](Chess_Position "Chess Position"), i.e. the chances of winning. If we could see to the end of the game in every line, the evaluation would only have values of -1 (loss), 0 (draw), and 1 (win), and the chess engine should search to depth 1 only to get the best move. In practice, however, we do not know the exact value of a position, so we must make an approximation with the main purpose is to compare positions, and the chess engine now must search deeply and find the highest score position within a given period.

Recently, there are two main ways to build an evaluation: traditional **hand-crafted evaluation** (HCE) and multi-layer [neural networks](Neural_Networks "Neural Networks"). This page focuses on the traditional way considering explicit features of a [chess position](Chess_Position "Chess Position").

Beginning chess players learn to do this starting with the [value](Point_Value "Point Value") of the [pieces](Pieces "Pieces") themselves. Computer evaluation functions also use the value of the [material balance](Material "Material") as the most significant aspect and then add other considerations.

## Contents

- [1 Where to Start](#Where_to_Start)
  - [1.1 Side to move relative](#Side_to_move_relative)
  - [1.2 Linear vs. Nonlinear](#Linear_vs._Nonlinear)
  - [1.3 General Aspects](#General_Aspects)
- [2 Basic Evaluation Features](#Basic_Evaluation_Features)
- [3 Considering Game Phase](#Considering_Game_Phase)
- [4 Miscellaneous](#Miscellaneous)
- [5 See also](#See_also)
- [6 Publications](#Publications)
  - [6.1 1949](#1949)
  - [6.2 1950 ...](#1950_...)
  - [6.3 1960 ...](#1960_...)
  - [6.4 1970 ...](#1970_...)
  - [6.5 1980 ...](#1980_...)
  - [6.6 1990 ...](#1990_...)
  - [6.7 2000 ...](#2000_...)
  - [6.8 2010 ...](#2010_...)
  - [6.9 2015 ...](#2015_...)
- [7 Blog & Forum Posts](#Blog_.26_Forum_Posts)
  - [7.1 1993 ...](#1993_...)
  - [7.2 1995 ...](#1995_...)
  - [7.3 2000 ...](#2000_..._2)
  - [7.4 2005 ...](#2005_...)
  - [7.5 2010 ...](#2010_..._2)
  - [7.6 2015 ...](#2015_..._2)
  - [7.7 2020 ...](#2020_...)
- [8 External Links](#External_Links)
  - [8.1 Mathematical Foundations](#Mathematical_Foundations)
  - [8.2 Chess Evaluation](#Chess_Evaluation)
- [9 References](#References)

## Where to Start

The first thing to consider when writing an evaluation function is how to score a move in [Minimax](Minimax "Minimax") or the more common [NegaMax](Negamax "Negamax") framework. While Minimax usually associates the white side with the max-player and black with the min-player and always evaluates from the white point of view, NegaMax requires a symmetric evaluation in relation to the [side to move](Side_to_move "Side to move"). We can see that one must not score the move per se – but the result of the move (i.e. a positional evaluation of the board as a result of the move). Such a symmetric evaluation function was first formulated by [Claude Shannon](Claude_Shannon "Claude Shannon") in 1949 [[2]](#cite_note-2) :

```C++

f(p) = 200(K-K')
       + 9(Q-Q')
       + 5(R-R')
       + 3(B-B' + N-N')
       + 1(P-P')
       - 0.5(D-D' + S-S' + I-I')
       + 0.1(M-M') + ...

KQRBNP = number of kings, queens, rooks, bishops, knights and pawns
D,S,I = doubled, blocked and isolated pawns
M = Mobility (the number of legal moves)

```

Here, we can see that the [score](Score "Score") is returned as a result of subtracting the current side's score from the equivalent evaluation of the opponent's board scores (indicated by the prime letters K' Q' and R'.. ).

## Side to move relative

In order for [NegaMax](Negamax "Negamax") to work, it is important to return the score relative to the side being evaluated. For example, consider a simple evaluation, which considers only [material](Material "Material") and [mobility](Mobility "Mobility"):

```C++

materialScore = kingWt  * (wK-bK)
              + queenWt * (wQ-bQ)
              + rookWt  * (wR-bR)
              + knightWt* (wN-bN)
              + bishopWt* (wB-bB)
              + pawnWt  * (wP-bP)

mobilityScore = mobilityWt * (wMobility-bMobility)

```

*return the score relative to the [side to move](Side_to_move "Side to move") (who2Move = +1 for white, -1 for black):*

```C++

Eval  = (materialScore + mobilityScore) * who2Move

```

## Linear vs. Nonlinear

Most evaluations terms are a [linear combination](https://en.wikipedia.org/wiki/Linear_combination) of independent features and associated weights in the form of

[](File:EvalLinearFormula1.jpg)
A function *f* is [linear](https://en.wikipedia.org/wiki/Linear) if the function is [additive](https://en.wikipedia.org/wiki/Additive_function):

[](File:EvalLinearFormula2.jpg)
and second if the function is [homogeneous](https://en.wikipedia.org/wiki/Homogeneous_function) of degree 1:

[](File:EvalLinearFormula3.jpg)
It depends on the definition and [independence](https://en.wikipedia.org/wiki/Linear_independence) of features and the acceptance of the [axiom of choice](https://en.wikipedia.org/wiki/Axiom_of_choice) ([Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") 1904), whether additive real number functions are linear or not [[3]](#cite_note-3) . Features are either related to single pieces ([material](Material "Material")), their location ([piece-square tables](Piece-Square_Tables "Piece-Square Tables")), or more sophisticated, considering interactions of multiple pawns and pieces, based on certain [patterns](Evaluation_Patterns "Evaluation Patterns") or [chunks](Chunking "Chunking"). Often several phases to first process simple features and after building appropriate data structures, in consecutive phases more complex features based on patterns and chunks are used.

Based on that, to distinguish [first-order](https://en.wikipedia.org/wiki/First-order), [second-order](https://en.wikipedia.org/wiki/Second-order), etc. terms, makes more sense than using the arbitrary terms linear vs. nonlinear evaluation [[4]](#cite_note-4) . With respect to [tuning](Automated_Tuning "Automated Tuning"), one has to take care that features are independent, which is not always that simple. Hidden dependencies may otherwise make the evaluation function hard to maintain with undesirable nonlinear effects.

## General Aspects

- [Evaluation Philosophy](Evaluation_Philosophy "Evaluation Philosophy")
- [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
- [Value Range](Score#ValueRange "Score")

## Basic Evaluation Features

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
- [Evaluation Patterns](Evaluation_Patterns "Evaluation Patterns")
- [Mobility](Mobility "Mobility")
- [Center Control](Center_Control "Center Control")
- [Connectivity](Connectivity "Connectivity")
- [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
- [King Safety](King_Safety "King Safety")
- [Space](Space "Space")
- [Tempo](Tempo "Tempo")

## Considering Game Phase

- [Game Phases](Game_Phases "Game Phases")

[Opening](Opening "Opening")
[Middlegame](Middlegame "Middlegame")
[Endgame](Endgame "Endgame")

- [Evaluation Discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity")
- [Tapered Eval](Tapered_Eval "Tapered Eval") (a score is interpolated between opening and endgame based on game stage/pieces)

## Miscellaneous

- [Analog Evaluation](Analog_Evaluation "Analog Evaluation")
- [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation")
- [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Evaluation Function](Evaluation_Function "Evaluation Function")
- [Evaluation Function Draft](Evaluation_Function_Draft "Evaluation Function Draft")
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Evaluation Overlap](Evaluation_Overlap "Evaluation Overlap") by [Mark Watkins](Mark_Watkins "Mark Watkins")
- [Evaluation Patterns](Evaluation_Patterns "Evaluation Patterns")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Quantifying Evaluation Features](Quantifying_Evaluation_Features "Quantifying Evaluation Features") by [Mark Watkins](Mark_Watkins "Mark Watkins")
- [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")
- [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")

## See also

- [CPW-Engine_eval](CPW-Engine_eval "CPW-Engine eval") - an example of a medium strength evaluation function
- [Entropy in Papa](Papa#Entropy "Papa")
- [Evaluation in Kaissa (PC)](Kaissa#Evaluation "Kaissa")
- [Evaluation in Rookie 2.0](Rookie#Evaluation "Rookie")
- [Knowledge](Knowledge "Knowledge")

[Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")

- [Learning](Learning "Learning")
- [NNUE](NNUE "NNUE")
- [Oracle](Oracle "Oracle")
- [Point Value](Point_Value "Point Value")
- [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
- [Stockfish Evaluation Guide](Stockfish#EvaluationGuide "Stockfish")

## Publications

## 1949

- [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

## 1950 ...

- [Eliot Slater](Eliot_Slater "Eliot Slater") (**1950**). *Statistics for the Chess Computer and the Factor of Mobility,* Proceedings of the Symposium on Information Theory, London. Reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), pp. 113-117. Including the transcript of a discussion with [Alan Turing](Alan_Turing "Alan Turing") and [Jack Good](Jack_Good "Jack Good")
- [Alan Turing](Alan_Turing "Alan Turing") (**1953**). ***Chess***. part of the collection *Digital Computers Applied to Games*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in *The Essential Turing*, [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)

## 1960 ...

- [Israel Albert Horowitz](https://en.wikipedia.org/wiki/Israel_Albert_Horowitz), [Geoffrey Mott-Smith](https://en.wikipedia.org/wiki/Mott-Smith_Trophy) (**1960,1970,2012**). *Point Count Chess*. [Samuel Reshevsky](https://en.wikipedia.org/wiki/Samuel_Reshevsky) (Introduction), [Sam Sloan](Sam_Sloan "Sam Sloan") (2012 Introduction), [Amazon](http://www.amazon.com/Point-Count-Chess-Accurate-Winning/dp/4871874699/ref=sr_1_2?s=books&ie=UTF8&qid=1366734801&sr=1-2) [[5]](#cite_note-5)
- [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess.* Machine Intelligence II pp. 110-115

## 1970 ...

- [Ron Atkin](Ron_Atkin "Ron Atkin") (**1972**). *Multi-Dimensional Structure in the Game of Chess*. In International Journal of Man-Machine Studies, Vol. 4
- [Ron Atkin](Ron_Atkin "Ron Atkin"), [Ian H. Witten](Ian_H._Witten "Ian H. Witten") (**1975**). *[A Multi-Dimensional Approach to Positional Chess](http://www.bibsonomy.org/bibtex/2b91106ea980eb48aa505f6b54c130707/dblp)*. International Journal of Man-Machine Studies, Vol. 7, No. 6
- [Gerard Zieliński](Gerard_Zieli%C5%84ski "Gerard Zieliński") (**1976**). *[Simple Evaluation Function](http://www.emeraldinsight.com/doi/abs/10.1108/eb005425)*. [Kybernetes](http://www.emeraldinsight.com/loi/k), Vol. 5, No. 3
- [Ron Atkin](Ron_Atkin "Ron Atkin") (**1977**). *Positional Play in Chess by Computer*. [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1")
- [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") (ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey")), pp. 82-118. Springer-Verlag, New York, N.Y. 2nd ed. 1983. ISBN 0-387-90815-3. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1979**). *[On the Construction of Evaluation Functions for Large Domains](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/)*. [IJCAI 1979](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/index.html) Tokyo, Vol. 1, pp. 53-55.

## 1980 ...

- [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1984**). *Some Conceptual Defects of Evaluation Functions*. [ECAI-84](http://dl.acm.org/citation.cfm?id=537320), [Pisa](https://en.wikipedia.org/wiki/Pisa), [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
- [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1985**). *An Empirical Technique for Developing Evaluation Functions*. [ICCA Journal, Vol. 8, No. 1](ICGA_Journal#8_1 "ICGA Journal")
- [Tony Marsland](Tony_Marsland "Tony Marsland") (**1985**). *Evaluation-Function Factors*. [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/evaluation.pdf)
- [Jens Christensen](Jens_Christensen "Jens Christensen"), [Richard Korf](Richard_Korf "Richard Korf") (**1986**). *A Unified Theory of Heuristic Evaluation functions and Its Applications to Learning.* Proceedings of the [AAAI-86](http://www.aaai.org/Conferences/AAAI/aaai86.php), pp. 148-152, [pdf](http://www.aaai.org/Papers/AAAI/1986/AAAI86-023.pdf)
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 1: Grandmasters have Insights - the Problem is what to Incorporate into Practical Problems.* [ICCA Journal, Vol. 10, No. 1](ICGA_Journal#10_1 "ICGA Journal")
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of [De Groot](Adriaan_de_Groot "Adriaan de Groot") and [Slater](Eliot_Slater "Eliot Slater")*. [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal")
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson"), [Richard Korf](Richard_Korf "Richard Korf") (**1987**). *A Model of Two-Player Evaluation Functions.* [AAAI-87](http://www.aaai.org/Conferences/AAAI/aaai87.php). [pdf](http://www.aaai.org/Papers/AAAI/1987/AAAI87-016.pdf)
- [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee"), [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan") (**1988**). *[A Pattern Classification Approach to Evaluation Function Learning](http://www.sciencedirect.com/science/article/pii/0004370288900768)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 36, No. 1
- [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1989**). *Notions of Evaluation Functions Tested against Grandmaster Games*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
- [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1989**). *Weight Assessment in Evaluation Functions*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1989**). *On Learning and Testing Evaluation Functions.* Proceedings of the Sixth Israeli Conference on Artificial Intelligence, 1989, 7-16.
- [Danny Kopec](Danny_Kopec "Danny Kopec"), [Ed Northam](Ed_Northam "Ed Northam"), [David Podber](index.php?title=David_Podber&action=edit&redlink=1 "David Podber (page does not exist)"), [Yehya Fouda](index.php?title=Yehya_Fouda&action=edit&redlink=1 "Yehya Fouda (page does not exist)") (**1989**). *The Role of Connectivity in Chess*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_24_C.pdf)

## 1990 ...

- [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *On Learning and Testing Evaluation Functions.* Journal of Experimental and Theoretical Artificial Intelligence 2: 241-251.
- [Ron Kalnim](index.php?title=Ron_Kalnim&action=edit&redlink=1 "Ron Kalnim (page does not exist)") (**1990**). *A Positional Assembly Model*. [ICCA Journal, Vol. 13, No. 3](ICGA_Journal#13_3 "ICGA Journal")
- [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Jeffery A. Clouse](http://dblp.uni-trier.de/pers/hd/c/Clouse:Jeffery_A=) (**1991**). *[Two Kinds of Training Information for Evaluation Function Learning](http://scholarworks.umass.edu/cs_faculty_pubs/193/)*. [University of Massachusetts, Amherst](https://en.wikipedia.org/wiki/University_of_Massachusetts_Amherst), Proceedings of the AAAI 1991
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1991**). *An Additive Evaluation Function in Chess.* [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
- [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1993**). *On Telescoping Linear Evaluation Functions.* [ICCA Journal, Vol. 16, No. 2](ICGA_Journal#16_2 "ICGA Journal") [[6]](#cite_note-6)
- [Alois Heinz](Alois_Heinz "Alois Heinz"), [Christoph Hense](index.php?title=Christoph_Hense&action=edit&redlink=1 "Christoph Hense (page does not exist)") (**1993**). *[Bootstrap learning of α-β-evaluation functions](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.56.872)*. [ICCI 1993](http://dblp.uni-trier.de/db/conf/icci/icci1993.html#HeinzH93), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.56.872&rep=rep1&type=pdf)
- [Alois Heinz](Alois_Heinz "Alois Heinz") (**1994**). *[Efficient Neural Net α-β-Evaluators](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.3994)*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.55.3994&rep=rep1&type=pdf) [[7]](#cite_note-7)
- [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. Thesis (German)
- [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
- [Yaakov HaCohen-Kerner](Yaakov_HaCohen-Kerner "Yaakov HaCohen-Kerner") (**1994**). *[Case-Based Evaluation in Computer Chess](http://www.springerlink.com/content/f5n27h25q4l920q8/)*. [EWCBR 1994](http://www.informatik.uni-trier.de/~ley/db/conf/ewcbr/ewcbr1994.html#Kerner94)
- [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *[Statistical Feature Combination for the Evaluation of Game Positions](http://www.jair.org/papers/paper179.html)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 3
- [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1997**). *A Metric for Evaluation Functions*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Michael Buro](Michael_Buro "Michael Buro") (**1998**). *[From Simple Features to Sophisticated Evaluation Functions](http://link.springer.com/chapter/10.1007/3-540-48957-6_8)*. [CG 1998](CG_1998 "CG 1998"), [pdf](https://skatgame.net/mburo/ps/glem.pdf)

## 2000 ...

- [Dan Heisman](Dan_Heisman "Dan Heisman") (**2003**). *Evaluation Criteria*, [pdf](http://www.chesscafe.com/text/heisman27.pdf) from [ChessCafe.com](https://en.wikipedia.org/wiki/ChessCafe.com)
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2005**). *[Evaluation by Hill-climbing: Getting the right move by solving micro-problems](http://www.aifactory.co.uk/newsletter/2005_03_hill-climbing.htm)*. [AI Factory](AI_Factory "AI Factory"), Autumn 2005 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kazunori Yamaguchi](Kazunori_Yamaguchi "Kazunori Yamaguchi"), [Satoru Kawai](Satoru_Kawai "Satoru Kawai") (**2007**). *Visualization and Adjustment of Evaluation Functions Based on Evaluation Values and Win Probability*. [AAAI 2007](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2007.html)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). *Genetic Algorithms for Mentor-Assisted Evaluation Function Optimization*, ACM Genetic and Evolutionary Computation Conference ([GECCO '08](http://www.sigevo.org/gecco-2008/)), pp. 1469-1475, Atlanta, GA, July 2008.
- [Omid David](Eli_David "Eli David"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2009**). *Simulating Human Grandmasters: Evolution and Coevolution of Evaluation Functions*. [ACM](ACM "ACM") Genetic and Evolutionary Computation Conference ([GECCO '09](http://www.sigevo.org/gecco-2009/)), pp. 1483 - 1489, Montreal, Canada, July 2009.
- [Omid David](Eli_David "Eli David") (**2009**). *Genetic Algorithms Based Learning for Evolving Intelligent Organisms*. Ph.D. Thesis.

## 2010 ...

- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2010**). *Little Chess Evaluation Compendium*. [2010 pdf](http://www.winboardengines.de/doc/LittleChessEvaluationCompendium-2010-04-07.pdf)
- [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2011**). *Expert-Driven Genetic Algorithms for Simulating Evaluation Functions*. Genetic Programming and Evolvable Machines, Vol. 12, No. 1, pp. 5--22, March 2011. » [Genetic Programming](Genetic_Programming "Genetic Programming")
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2011**). *[Mixing MCTS with Conventional Static Evaluation](http://www.aifactory.co.uk/newsletter/2011_02_mcts_static.htm)*. [AI Factory](AI_Factory "AI Factory"), Winter 2011 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2012**). *[Evaluation options - Overview of methods](http://www.aifactory.co.uk/newsletter/2012_01_evaluation_options.htm)*. [AI Factory](AI_Factory "AI Factory"), Summer 2012
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2012**). *An Addendum to a Little Chess Evaluation Compendium*. [Addendum June 2012 pdf](http://www.winboardengines.de/doc/addendumlcec_2012.pdf), [File:Addendum2LCEC 2012.pdf](File:Addendum2LCEC_2012.pdf "File:Addendum2LCEC 2012.pdf"), [File:Addendum3LCEC 2012.pdf](File:Addendum3LCEC_2012.pdf "File:Addendum3LCEC 2012.pdf"), [Addendum 4 November 2012 pdf](http://www.winboardengines.de/doc/addendum4lcec_2012.pdf), [File:Addendum5LCEC 2012.pdf](File:Addendum5LCEC_2012.pdf "File:Addendum5LCEC 2012.pdf"), [File:Addendum6LCEC 2012.pdf](File:Addendum6LCEC_2012.pdf "File:Addendum6LCEC 2012.pdf")
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2012**). *Little Chess Evaluation Compendium*. [July 2012 pdf](http://www.winboardengines.de/doc/LittleChessEvaluationCompendium.pdf) [[8]](#cite_note-8), [File:LittleChessEvaluationCompendium.pdf](File:LittleChessEvaluationCompendium.pdf "File:LittleChessEvaluationCompendium.pdf")
- [Derek Farren](index.php?title=Derek_Farren&action=edit&redlink=1 "Derek Farren (page does not exist)"), [Daniel Templeton](index.php?title=Daniel_Templeton&action=edit&redlink=1 "Daniel Templeton (page does not exist)"), [Meiji Wang](index.php?title=Meiji_Wang&action=edit&redlink=1 "Meiji Wang (page does not exist)") (**2013**). *Analysis of Networks in Chess*. Team 23, [Stanford University](Stanford_University "Stanford University"), [pdf](http://snap.stanford.edu/class/cs224w-2013/projects2013/cs224w-023-final.pdf)

## 2015 ...

- [Nera Nesic](index.php?title=Nera_Nesic&action=edit&redlink=1 "Nera Nesic (page does not exist)"), [Stephan Schiffel](Stephan_Schiffel "Stephan Schiffel") (**2016**). *Heuristic Function Evaluation Framework*. [CG 2016](CG_2016 "CG 2016")
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *[The Secret of Chess](http://www.secretofchess.com/)*. [amazon](https://www.amazon.com/Secret-Chess-Lyudmil-Tsvetkov-ebook/dp/B074M85CVV) [[9]](#cite_note-9)
- [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *Pawns*. [amazon](https://www.amazon.com/Pawns-Lyudmil-Tsvetkov-ebook/dp/B074S2MYQV)

## Blog & Forum Posts

## 1993 ...

- [Cray Blitz Evaluation](https://groups.google.com/d/msg/rec.games.chess/J9Pkg9lOpig/tBN5dVRATwsJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 05, 1993 » [Cray Blitz](Cray_Blitz "Cray Blitz")
- [Mobility Measure: Proposed Algorithm](https://groups.google.com/d/msg/rec.games.chess/6vwtkcF6sRU/4M3oOiDNYwgJ) by Dietrich Kappe, [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 23, 1993 » [Mobility](Mobility "Mobility")
- [bitboard position evaluations](https://groups.google.com/d/msg/rec.games.chess/M4CKCmqDNkI/TjVJEQY0GC0J) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 17, 1994 » [Bitboards](Bitboards "Bitboards")

## 1995 ...

- [Value of the pieces](https://groups.google.com/d/msg/rec.games.chess/efBhsZU3J1g/fC7rxV5yuycJ) by Joost de Heer, [rgc](Computer_Chess_Forums "Computer Chess Forums"), February 01, 1995
- [Evaluation function diminishing returns](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4f54813edf18fdcc) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 1, 1997
- [Evaluation function question](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/40fe48d492e582bd) by [Dave Fotland](David_Fotland "David Fotland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 07, 1997
- [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 01, 1997 » [Oracle](Oracle "Oracle")
- [Evolutionary Evaluation](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/77f10f072e907302) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 09, 1997 » [Automated Tuning](Automated_Tuning "Automated Tuning")
- [Books that help for evaluation](https://www.stmintz.com/ccc/index.php?id=25012) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), August 18, 1998
- [Static evaluation after the "Positional/Real Sacrifice"](https://www.stmintz.com/ccc/index.php?id=80569) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), December 03, 1999

## 2000 ...

- [Adding knowledge to the evaluation, what am I doing wrong?](https://www.stmintz.com/ccc/index.php?id=289154) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 13, 2003
- [testing of evaluation function](https://www.stmintz.com/ccc/index.php?id=293815) by Steven Chu, [CCC](CCC "CCC"), April 17, 2003 » [Engine Testing](Engine_Testing "Engine Testing")
- [Question about evaluation and branch factor](https://www.stmintz.com/ccc/index.php?id=328924) by [Marcus Prewarski](Marcus_Prewarski "Marcus Prewarski"), [CCC](CCC "CCC"), November 20, 2003  » [Branching Factor](Branching_Factor "Branching Factor")
- [STATIC EVAL TEST (provisional)](https://www.stmintz.com/ccc/index.php?id=350516) by [Jaime Benito de Valle Ruiz](Jaime_Benito_de_Valle_Ruiz "Jaime Benito de Valle Ruiz"), [CCC](CCC "CCC"), February 21, 2004 » [Test-Positions](Test-Positions "Test-Positions")

## 2005 ...

- [Re: Zappa Report](https://www.stmintz.com/ccc/index.php?id=475521) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), December 30, 2005
- [Do you evaluate internal nodes?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4155#p21292) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 16, 2006 » [Interior Node](Interior_Node "Interior Node")
- [question about symmertic evaluation](http://www.talkchess.com/forum/viewtopic.php?t=13969) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 23, 2007
- [Trouble Spotter](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=15220) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 19, 2007 » [Tactics](Tactics "Tactics")
- [Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?t=402) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 05, 2007 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge"), [Search](Search "Search")

[Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007

- [Problems with eval function](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=20340) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 25, 2008 » Evaluation
- [Evaluation functions. Why integer?](http://www.talkchess.com/forum/viewtopic.php?t=22817) by oysteijo, [CCC](CCC "CCC"), August 06, 2008 » [Float](Float "Float"), [Score](Score "Score")
- [Smooth evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=24052) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), September 29, 2008
- [Evaluating every node?](http://www.talkchess.com/forum/viewtopic.php?t=25795) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), January 03, 2009
- [Evaluation idea](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=26700) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), February 24, 2009
- [Accurate eval function](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=27055) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 18, 2009
- [Eval Dilemma](http://www.talkchess.com/forum/viewtopic.php?t=27299) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), April 03, 2009
- [Linear vs. Nonlinear Evalulation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=288424) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 26, 2009
- [Threat information from evaluation to inform q-search](http://www.talkchess.com/forum/viewtopic.php?p=291259) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), September 15, 2009 » [Quiescence Search](Quiescence_Search "Quiescence Search")

## 2010 ...

- [Correcting Evaluation with the hash table](http://www.talkchess.com/forum/viewtopic.php?t=32396) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), February 05, 2010
- [Re: Questions for the Stockfish team](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=362888&t=35455) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), July 20, 2010
- [Most important eval elements](http://www.talkchess.com/forum/viewtopic.php?t=36104) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), September 17, 2010
- [Re: 100 long games Rybka 4 vs Houdini 1.03a](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=374967&t=36421) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), November 02, 2010
- [dynamically modified evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=37191) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 20, 2010

**2011**

- [Suppose Rybka used Fruits evaluations](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22785) by [SR](S%C3%B8ren_Riis "Søren Riis"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 29, 2011
- [writing an evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=41621) by Pierre Bokma, [CCC](CCC "CCC"), December 27, 2011

**2012**

- [The evaluation value and value returned by minimax search](http://www.talkchess.com/forum/viewtopic.php?t=42806) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), March 09, 2012
- [Multi dimensional score](http://www.talkchess.com/forum/viewtopic.php?t=43385) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
- [Bi dimensional static evaluation](http://www.talkchess.com/forum/viewtopic.php?t=43386) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
- [Theorem proving positional evaluation](http://www.talkchess.com/forum/viewtopic.php?t=43387) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
- [log(w/b) instead of w-b?](http://www.talkchess.com/forum/viewtopic.php?t=43545) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), May 02, 2012
- [The value of an evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=44014) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 11, 2012

**2013**

- [eval scale in Houdini](http://www.talkchess.com/forum/viewtopic.php?t=46879) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), January 14, 2013 » [Houdini](Houdini "Houdini")
- [An idea of how to make your engine play more rational chess](http://www.talkchess.com/forum/viewtopic.php?t=46993) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), January 25, 2013
- [A Materialless Evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=48252) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), June 12, 2013
- [A different way of summing evaluation features](http://www.talkchess.com/forum/viewtopic.php?t=48644) by [Pio Korinth](index.php?title=Pio_Korinth&action=edit&redlink=1 "Pio Korinth (page does not exist)"), [CCC](CCC "CCC"), July 14, 2013 [[10]](#cite_note-10) [[11]](#cite_note-11)
- [Improve the search or the evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=49190) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), August 31, 2013 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
- [Multiple EVAL](http://www.talkchess.com/forum/viewtopic.php?t=49421) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 22, 2013
- [floating point SSE eval](http://www.talkchess.com/forum/viewtopic.php?t=50472) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), December 13, 2013 » [Float](Float "Float"), [Score](Score "Score")

**2014**

- [5 underestimated evaluation rules](http://www.talkchess.com/forum/viewtopic.php?t=51012) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), January 23, 2014
- [Thoughs on eval terms](http://www.talkchess.com/forum/viewtopic.php?t=51811) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 31, 2014

## 2015 ...

- [Value of a Feature or Heuristic](http://www.talkchess.com/forum/viewtopic.php?t=55355) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), February 15, 2015
- [Couple more ideas](http://www.talkchess.com/forum/viewtopic.php?t=55897) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), April 05, 2015
- [Most common/top evaluation features?](http://www.talkchess.com/forum/viewtopic.php?t=55955) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), April 10, 2015
- [eval pieces](http://www.talkchess.com/forum/viewtopic.php?t=56690) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), June 15, 2015
- [\* vs +](http://www.talkchess.com/forum/viewtopic.php?t=57022) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), July 19, 2015
- [(E)valuation (F)or (S)tarters](http://www.talkchess.com/forum/viewtopic.php?t=57087) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 26, 2015

**2016**

- [Non-linear eval terms](http://www.talkchess.com/forum/viewtopic.php?t=59091) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), January 29, 2016
- [A bizarre evaluation](http://www.talkchess.com/forum/viewtopic.php?t=59570) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 20, 2016
- [Chess position evaluation with convolutional neural network in Julia](http://int8.io/chess-position-evaluation-with-convolutional-neural-networks-in-julia/) by [Kamil Czarnogorski](index.php?title=Kamil_Czarnogorski&action=edit&redlink=1 "Kamil Czarnogorski (page does not exist)"), [Machine learning with Julia and python](http://int8.io/), April 02, 2016 » [Deep Learning](Deep_Learning "Deep Learning"), [Neural Networks](Neural_Networks "Neural Networks")
- [Calculating space](http://www.talkchess.com/forum/viewtopic.php?t=61064) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), August 07, 2016
- [Evaluation values help](http://www.talkchess.com/forum/viewtopic.php?t=61236) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), August 26, 2016
- [A database for learning evaluation functions](http://www.talkchess.com/forum/viewtopic.php?t=61861) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 28, 2016 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Learning](Learning "Learning"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
- [Evaluation doubt](http://www.talkchess.com/forum/viewtopic.php?t=61875) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), October 29, 2016

**2017**

- [Bayesian Evaluation Functions](http://www.talkchess.com/forum/viewtopic.php?t=63181) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), February 15, 2017
- [improved evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=63408) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 11, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"), [Zurichess](Zurichess "Zurichess")
- [random evaluation perturbation factor](http://www.talkchess.com/forum/viewtopic.php?t=63803) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 24, 2017
- [horrid positional play in a solid tactical searcher](http://www.talkchess.com/forum/viewtopic.php?t=63863) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 29, 2017
- [Another attempt at comparing Evals ELO-wise](http://www.talkchess.com/forum/viewtopic.php?t=64041) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 22, 2017 » [Playing Strength](Playing_Strength "Playing Strength")
- [static eval in every node?](http://www.talkchess.com/forum/viewtopic.php?t=64230) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), June 09, 2017
- [comparing between search or evaluation](http://www.talkchess.com/forum/viewtopic.php?t=65403) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 09, 2017» [Search](Search "Search")
- [Neural networks for chess position evaluation- request](http://www.talkchess.com/forum/viewtopic.php?t=65715) by [Kamil Czarnogorski](index.php?title=Kamil_Czarnogorski&action=edit&redlink=1 "Kamil Czarnogorski (page does not exist)"), [CCC](CCC "CCC"), November 13, 2017 » [Deep Learning](Deep_Learning "Deep Learning"), [Neural Networks](Neural_Networks "Neural Networks")
- [AlphaGo's evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=65829) by Jens Kipper, [CCC](CCC "CCC"), November 26, 2017
- [Logarithmic Patterns In Evaluations](http://www.talkchess.com/forum/viewtopic.php?t=65946) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), December 09, 2017

**2018**

- [replace the evaluation by playing against yourself](http://www.talkchess.com/forum/viewtopic.php?t=66413) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 25, 2018 » [Fortress](Fortress "Fortress")
- [Poor man's neurones](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67524) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), May 21, 2018 » [Neural Networks](Neural_Networks "Neural Networks")
- [Xiangqi evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67877) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 01, 2018 » [Xiangqi](Chinese_Chess "Chinese Chess")

## 2020 ...

- [romantic-style play](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74652) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 02, 2020
- [Engine choosing between sets of piece/square tables](https://prodeo.actieforum.com/t120-engine-choosing-between-sets-of-piece-square-tables) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2020 » [Rodent](Rodent "Rodent"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Controlled randomness of evaluation function](https://prodeo.actieforum.com/t123-controlled-randomness-of-evaluation-function) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2020
- [Manually tuned evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76161) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), December 27, 2020 » [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")

**2021**

- [So what do we miss in the traditional evaluation?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76446) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), January 29, 2021 » [NNUE](NNUE "NNUE")
- [HCE and NNUE and vectorisation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76556) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 11, 2021 » [NNUE](NNUE "NNUE"), [Minic](Minic "Minic")
- [Idea: use range (evalMin - evalMax) for position evaluation](https://groups.google.com/g/lczero/c/TLCMkkdm1hw/m/erjTVGUqAQAJ) by Mirza Hadzic, [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), April 6, 2021

[Re: Idea: use range (evalMin - evalMax) for position evaluation](https://groups.google.com/g/lczero/c/TLCMkkdm1hw/m/SgbGghzhBAAJ) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), May 28, 2021 [[12]](#cite_note-12)
[Re: Idea: use range (evalMin - evalMax) for position evaluation](https://groups.google.com/g/lczero/c/TLCMkkdm1hw/m/F9JjnN8FBQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), May 29, 2021

- [I declare that HCE is dead...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77571) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 29, 2021 » [Ethereal](Ethereal "Ethereal"), [NNUE](NNUE "NNUE")
- [Evaluation questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77952) by [Ellie Moore](index.php?title=Ellie_Moore&action=edit&redlink=1 "Ellie Moore (page does not exist)"), [CCC](CCC "CCC"), August 16, 2021

## External Links

## Mathematical Foundations

- [Heuristic from Wikipedia](<https://en.wikipedia.org/wiki/Heuristic_(computer_science)>)
- [Linear combination from Wikipedia](https://en.wikipedia.org/wiki/Linear_combination)
- [Linear independence from Wikipedia](https://en.wikipedia.org/wiki/Linear_independence)
- [Orthogonality from Wikipedia](https://en.wikipedia.org/wiki/Orthogonality)
- [Principal component analysis from Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)

## Chess Evaluation

- [Evaluation function from Wikipedia](https://en.wikipedia.org/wiki/Evaluation_function)
- [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/) » [Stockfish Evaluation Guide](Stockfish#EvaluationGuide "Stockfish")
- [GitHub - gekomad/chess-engine-eval-debugger: Chess engine web evaluator](https://github.com/gekomad/chess-engine-eval-debugger) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella")
- [Evaluation: Basics](http://home.hccnet.nl/h.g.muller/eval.html) of [Micro-Max](Micro-Max "Micro-Max") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
- [Chess Programming Part VI: Evaluation Functions](http://www.gamedev.net/page/resources/_/technical/artificial-intelligence/chess-programming-part-vi-evaluation-functions-r1208) by [François-Dominic Laramée](Fran%C3%A7ois-Dominic_Laram%C3%A9e "François-Dominic Laramée"), [gamedev.net](https://en.wikipedia.org/wiki/GameDev.net), October 2000
- [About the Values of Chess Pieces](http://www.chessvariants.com/d.betza/pieceval/index.html) by [Ralph Betza](index.php?title=Ralph_Betza&action=edit&redlink=1 "Ralph Betza (page does not exist)")

## References

1. [↑](#cite_ref-1) [Vassily Kandinsky - Schach-Theorie | Art I love | Pinterest](https://www.pinterest.de/pin/58476495131654514/)
1. [↑](#cite_ref-2) [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)
1. [↑](#cite_ref-3) [Re: Linear vs. Nonlinear Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=288501&t=29552) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 27, 2009
1. [↑](#cite_ref-4) [Re: Linear vs. Nonlinear Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=288564&t=29552) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 27, 2009
1. [↑](#cite_ref-5) [Re: Books that help for evaluation](https://www.stmintz.com/ccc/index.php?id=25046) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 18, 1998
1. [↑](#cite_ref-6) [Re: Zappa Report](https://www.stmintz.com/ccc/index.php?id=475521) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), December 30, 2005
1. [↑](#cite_ref-7) [Re: Evaluation by neural network ?](https://www.stmintz.com/ccc/index.php?id=11893) by [Jay Scott](Jay_Scott "Jay Scott"), [CCC](CCC "CCC"), November 10, 1997
1. [↑](#cite_ref-8) [An Update of the Addendum to the LittleCompendium](http://www.talkchess.com/forum/viewtopic.php?t=44265) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), July 02, 2012
1. [↑](#cite_ref-9) [The Secret of Chess](http://www.talkchess.com/forum/viewtopic.php?t=64776) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), August 01, 2017
1. [↑](#cite_ref-10) [Euclidean distance from Wikipedia](https://en.wikipedia.org/wiki/Euclidean_distance)
1. [↑](#cite_ref-11) [Principal component analysis from Wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)
1. [↑](#cite_ref-12) [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1999**). *[Propagating Distributions Up Directed Acyclic Graphs](https://www.mitpressjournals.org/doi/abs/10.1162/089976699300016881?journalCode=neco)*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_%28journal%29), Vol. 11, No. 1

**[Up one level](Home "Home")**

