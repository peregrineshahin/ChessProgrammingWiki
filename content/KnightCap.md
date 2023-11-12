---
title: KnightCap
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* KnightCap**



 [](http://www.samba.org/KnightCap/) KnightCap's [3D Board](3D_Graphics_Board "3D Graphics Board") <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**KnightCap**,  

a [XBoard](XBoard "XBoard") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter") and [Lex Weaver](Lex_Weaver "Lex Weaver"). 
To [tune](Automated_Tuning "Automated Tuning") it's [evaluation](Evaluation "Evaluation") in game play, it uses [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning") applied to [minimax](Minimax "Minimax") search in chess, [TDLeaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>. KnightCap features an own [GUI](GUI "GUI") with an optional [3D Graphics Board](3D_Graphics_Board "3D Graphics Board") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and played multiple [Australasian National Computer Chess Championships](Australasian_National_Computer_Chess_Championship "Australasian National Computer Chess Championship"), and won two times, last one the [NC3 2006](NC3_2006 "NC3 2006"). 



### [Board Representation](Board_Representation "Board Representation")


KnightCap maintains an [incremental updated](Incremental_Updates "Incremental Updates") [attack table](Attack_and_Defend_Maps "Attack and Defend Maps") of 64 [piece-sets](Piece-Sets "Piece-Sets") - for each square indicating all pieces attacking or defending that square. Despite [move generation](Move_Generation "Move Generation"), this approach pays off in determining [in-check](Check#Detection "Check"), and [square control](Square_Control "Square Control") evaluation.



### [Search](Search "Search")


The program performs a [iterative deepening](Iterative_Deepening "Iterative Deepening") [parallel](Parallel_Search "Parallel Search") [MTD(f)](MTD(f) "MTD(f)") search utilizing the [shared transposition table](Shared_Hash_Table "Shared Hash Table"). The variation of MTD(f) that KnightCap uses includes some convergence acceleration heuristics 
that prevent the very slow convergence that can sometimes plague MTD(f) implementations. [Selectivity](Selectivity "Selectivity") is due to [null move pruning](Null_Move_Pruning "Null Move Pruning"), [razoring](Razoring "Razoring") and various [extensions](Extensions "Extensions"). The [transposition table](Transposition_Table "Transposition Table") with 128 bit entries keeps separate [depth](Depth "Depth") and [scores](Score "Score") for the [lower](Lower_Bound "Lower Bound") and [upper bound](Upper_Bound "Upper Bound"). The [move ordering](Move_Ordering "Move Ordering") system is a combination of the commonly used [history](History_Heuristic "History Heuristic"), [killer](Killer_Heuristic "Killer Heuristic"), [refutation](Refutation_Table "Refutation Table") and transposition table, along with [ETC](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff").



### [Evaluation](Evaluation "Evaluation")


### Conventional


KnightCap uses a quite slow evaluation function that evaluates a number of computationally expensive features such as [board control](Square_Control "Square Control") to reasonably accurately consider the presence of [hung](Hanging_Piece "Hanging Piece"), [trapped](Trapped_Pieces "Trapped Pieces") and [immobile](Mobility "Mobility") pieces, and further has some [asymmetric evaluation](Asymmetric_Evaluation "Asymmetric Evaluation") as well as search terms with a leaning towards careful play. 



### TD Considerations


One major modification for [TDLeaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") was that all evaluation coefficients became part of a weight vector. Another significant modification that was required was an increase in the bit resolution of the evaluation type so that a numerical [partial derivative](https://en.wikipedia.org/wiki/Partial_derivative) of the evaluation function with respect to the evaluation coefficient vector could be obtained with reasonable accuracy. To ensure small fluctuations in the relative values of leaf nodes did not produce large temporal differences, the raw linear leaf evaluation score was squashed to a ±1 range of a [hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_function#Hyperbolic_tangent) [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) with 0.25 equivalent a material superiority of one pawn. The outcome of the game was set to 1 for a win, -1 for a loss and 0 for a draw. Negative values of temporal differences (dt) were left unchanged as any decrease in the evaluation from one position to the next can be viewed as mistake. However, positive values of dt can occur simply because the opponent has made a blunder. To avoid KnightCap trying to learn to predict its opponent’s blunders, all positive temporal differences were set to zero unless KnightCap predicted the opponent’s move <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



## Selected Games


[NC3 2006](NC3_2006 "NC3 2006"), round 2, [Bodo](Bodo "Bodo") - KnightCap




```

[Event "NC3 2006"]
[Site "RedHill, Canberra, Australia"]
[Date "2006.08.20"]
[Round "2"]
[White "Bodo"]
[Black "KnightCap"]
[Result "0-1"]

1.d4 h6 2.e4 a6 3.Nf3 d6 4.Nc3 e6 5.Bc4 Nc6 6.O-O Nf6 7.Qe2 b5 8.Bb3 Na5 
9.e5 dxe5 10.dxe5 Nd7 11.Rd1 Bb7 12.Bf4 Nxb3 13.axb3 Bc5 14.Ne4 Bb6 15.c3 
Qe7 16.Bg3 O-O 17.Bh4 Qe8 18.b4 Bd5 19.Rd2 Qc8 20.Re1 Re8 21.Qd3 Nf8 22.Nd4 
Ng6 23.Bg3 Qb7 24.Qe2 Rad8 25.f3 Qa7 26.Kh1 Bb7 27.Red1 Rd5 28.Nc2 Red8 
29.Rd3 Rxd3 30.Rxd3 Rd5 31.h4 Ne7 32.h5 Nf5 33.Bf4 Qa8 34.g3 Ne7 35.Kg2 Qd8 
36.Rxd5 Nxd5 37.Bc1 Ne7 38.Nc5 Bxc5 39.bxc5 Qd5 40.b4 Nf5 41.Bd2 Qa2 42.Bf4 
Qb1 43.Qd2 Bd5 44.Na3 Qb3 45.Nc2 Qa4 46.Kf2 a5 47.g4 Ne7 48.bxa5 Qxa5 49.Nb4 
Qa7 50.Be3 Qa8 51.Qd1 c6 52.Kg2 Qb8 53.Qd4 Qa7 54.Qd2 Qc7 55.Qd4 Qa5 56.Bf2 
Qa1 57.Qd2 Kf8 58.Bh4 Qa7 59.Bf2 Qd7 60.Qd3 Kg8 61.Be3 Qc8 62.Qd2 Qd8 63.Qd4 
Kh8 64.Qf4 Qf8 65.g5 hxg5 66.Qxg5 Nf5 67.Nxd5 cxd5 68.Bg1 Qa8 69.Bf2 Kg8 
70.Bg1 Qa2+ 71.Bf2 Kh7 72.Qc1 Nh4+ 73.Kg3 Qc4 74.Qd2 Kg8 75.Qb2 Nf5+ 76.Kg2 
Qd3 77.c6 Qc4 78.c7 Qxc7 79.Qxb5 Nh6 80.Be3 Qd8 81.Bxh6 gxh6 82.Qb4 Qg5+ 
83.Qg4 Qxg4+ 84.fxg4 f6 85.exf6 Kf7 86.Kh1 Kxf6 87.Kh2 Kg5 88.Kg3 e5 89.Kf3 
Kh4 90.Kg2 Kxg4 91.Kf2 Kf4 92.Kg1 Ke3 93.Kf1 e4 94.Ke1 Kd3 95.Kf2 e3+ 96.Kg3 
Ke4 97.Kg2 e2 98.Kf2 Kd3 99.c4 Kd2 0-1

```

## See also


* [MTD(f)](MTD(f) "MTD(f)")
* [TDChess](TDChess "TDChess")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")


## Publications


### 1997 ...


* [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") (**1997**). *KnightCap — a parallel chess program on the AP1000+*. [zipped ps](http://ftp.riken.jp/pub/net/samba/tridge/knightcap_pcw97.ps.gz)
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1997**). *Knightcap: A chess program that learns by combining td(λ) with minimax search*. 15th International Conference on Machine Learning, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.54.8263&rep=rep1&type=pdf) via [citeseerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.8263)
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Experiments in Parameter Learning Using Temporal Differences*. [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal")
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1999**). *TDLeaf(lambda): Combining Temporal Difference Learning with Game-Tree Search*. [Australian Journal of Intelligent Information Processing Systems](https://www.chatbots.org/journal/australian_journal_of_intelligent_information_processing_systems/), Vol. 5 No. 1, [arXiv:cs/9901001](http://arxiv.org/abs/cs/9901001)
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1999**). *KnightCap: A chess program that learns by combining TD(lambda) with game-tree search*. [arXiv:cs/9901002](https://arxiv.org/abs/cs/9901002)


### 2000 ...


* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**2000**). *Learning to Play Chess Using Temporal Differences*. [Machine Learning, Vol 40, No. 3](http://www.dblp.org/db/journals/ml/ml40.html#BaxterTW00), [pdf](http://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/chess-RL.pdf)
* [Marco Block-Berlitz](Marco_Block-Berlitz "Marco Block-Berlitz") (**2003**). *Reinforcement Learning in der Schachprogrammierung*. Studienarbeit, [Free University of Berlin](Free_University_of_Berlin "Free University of Berlin"), advisor: [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas"), [pdf](http://page.mi.fu-berlin.de/block/Skripte/Reinforcement.pdf) (German)
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)


## Forum Posts


### 1997 ...


* [KnightCap 1.0](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1f7ba9d3c31f071) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 27, 1997
* [Parallel searching](https://groups.google.com/d/msg/rec.games.chess.computer/Wl7A-v-gWYQ/QLuvAp0l4_gJ) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 22, 1997 » [Parallel Search](Parallel_Search "Parallel Search")
* [KnightCap v1.8](https://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e68ee1ab5a2603d3) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 03, 1997
* [Re: computer chess "oracle" ideas...](https://groups.google.com/group/rec.games.chess.computer/msg/300171a5fa7ce7b6) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 03, 1997 » [Oracle](Oracle "Oracle")
* [Re: cheaper search ?](https://groups.google.com/group/rec.games.chess.computer/msg/730c03a83bf92807) by [Shaun Press](Shaun_Press "Shaun Press"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 26, 1997 » [Copy-Make](Copy-Make "Copy-Make"), [Vanilla Chess](Vanilla_Chess "Vanilla Chess")
* [Re: Bit Board Bonkers?? - other alternatives](https://groups.google.com/group/rec.games.chess.computer/msg/4d6c328e8e8e0cd4) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 9, 1997 » [Piece-Sets](Piece-Sets "Piece-Sets")
* [asymmetry](https://groups.google.com/group/rec.games.chess.computer/msg/f9bfe5d4457a19ad) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 12, 1997 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation"), [Parity Pruning](Parity_Pruning "Parity Pruning")
* [Re: How to get chess program to solve KBN mate?](https://groups.google.com/group/rec.games.chess.computer/msg/ba9febc300f8698f) by [David John Blackman](David_Blackman "David Blackman"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 18, 1997 » [KBNK Endgame](KBNK_Endgame "KBNK Endgame")
* [KnightCap---A free chess program that learns](https://www.stmintz.com/ccc/index.php?id=12458) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), November 26, 1997
* [Parameter Tuning](https://www.stmintz.com/ccc/index.php?id=28584) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), October 01, 1998 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [KnightCap and Windows](https://www.stmintz.com/ccc/index.php?id=28647) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)"), [CCC](CCC "CCC"), October 02, 1998


### 2000 ...


* [KnightCap installation question](https://www.stmintz.com/ccc/index.php?id=100829) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), March 08, 2000
* [Question about the KnightCap find\_pins function](https://www.stmintz.com/ccc/index.php?id=306311) by Matthew White, [CCC](CCC "CCC"), July 14, 2003 » [Pin](Pin "Pin")
* [KnightCap source code](http://www.talkchess.com/forum/viewtopic.php?t=59304) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), February 19, 2016


## External Links


* [Welcome to the KnightCap home page](http://samba.anu.edu.au/KnightCap/)
* [Index of /pub/KnightCap](https://ftp.samba.org/pub/KnightCap/) <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [KnightCap from Wikipedia](https://en.wikipedia.org/wiki/KnightCap)
* [chessexpress: Tridge](http://chessexpress.blogspot.de/2007/07/tridge.html) by [Shaun Press](Shaun_Press "Shaun Press"), July 23, 2007


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Welcome to the KnightCap home page](http://samba.anu.edu.au/KnightCap/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") (**1997**). *KnightCap — a parallel chess program on the AP1000+*.
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1997**) *Knightcap: A chess program that learns by combining td(λ) with minimax search*. 15th International Conference on Machine Learning
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Bit Board Bonkers?? - other alternatives](https://groups.google.com/group/rec.games.chess.computer/msg/4d6c328e8e8e0cd4) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 9, 1997
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Going commercial, maybe](https://groups.google.com/group/rec.games.chess.computer/msg/ded7e4e4304d8d4e) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 9, 1997
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1997**) *Knightcap: A chess program that learns by combining td(λ) with minimax search*. 15th International Conference on Machine Learning
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: KnightCap source code](http://www.talkchess.com/forum/viewtopic.php?t=59304&start=1) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), February 19, 2016

**[Up one level](Engines "Engines")**







 
