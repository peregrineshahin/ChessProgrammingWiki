---
title: Search with Random Leaf Values
---
**[Home](Home "Home") \* [Search](Search "Search") \* with Random Leaf Values**



[ [Japanese maple](https://en.wikipedia.org/wiki/Acer_palmatum) [autumn leaves](https://en.wikipedia.org/wiki/Autumn_leaf_color) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Search with Random Leaf Values** is of interest concerning [playing strength](Playing_Strength "Playing Strength"), [match statistics](Match_Statistics "Match Statistics") and [search pathology](Search_Pathology "Search Pathology"). Randomized [evaluation](Evaluation "Evaluation") by adding [noise](https://en.wikipedia.org/wiki/Noise_(electronics)) concerns evaluation accuracy and evaluation error analysis - it might be used in introducing and [learning](Learning "Learning") new evaluation terms for various [games](Games "Games") or [general game playing](General_Game_Playing "General Game Playing") programs, or simply in randomizing or weakening engine play. 




### Contents


* [1 The Beal Effect](#the-beal-effect)
* [2 Setup](#setup)
* [3 Further Experiments](#further-experiments)
* [4 See also](#see-also)
* [5 Publications](#publications)
	+ [5.1 1985 ...](#1985-...)
	+ [5.2 1990 ...](#1990-...)
	+ [5.3 2000 ...](#2000-...)
* [6 Forum Posts](#forum-posts)
	+ [6.1 1990 ...](#1990-...-2)
	+ [6.2 1995 ...](#1995-...)
	+ [6.3 2000 ...](#2000-...-2)
	+ [6.4 2005 ...](#2005-...)
	+ [6.5 2010 ...](#2010-...)
	+ [6.6 2015 ...](#2015-...)
	+ [6.7 2020 ...](#2020-...)
* [7 External Links](#external-links)
* [8 References](#references)






Random evaluation was first examined for the game of chess by [Don Beal](Don_Beal "Don Beal") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [Martin C. Smith](Martin_C._Smith "Martin C. Smith") at the [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7") conference at [University of Limburg](Maastricht_University "Maastricht University"), July 1993, published in the [ICCA Journal](ICGA_Journal#17_1 "ICGA Journal") and conference proceedings <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and further analyzed by [Mark Levene](Mark_Levene "Mark Levene") and [Trevor Fenner](Trevor_Fenner "Trevor Fenner") in 1995 <a id="cite-note-4" href="#cite-ref-4">[4]</a> and 2001 <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Although using [random numbers](https://en.wikipedia.org/wiki/Random_number) as "evaluation" results in random play with a one [ply](Ply "Ply") [search](Search "Search") (root-random), it was found that the [strength of play](Playing_Strength "Playing Strength") rises rapidly with increased [depth](Depth "Depth") (lookahead-random) using a full-width [minimax](Minimax "Minimax") search. While a natural assumption is that lookahead on random numbers would also result in a random choice at the [root](Root "Root") as well, random evaluation would create a statistical preference for positions with large [mobilty](Mobility "Mobility"), and thus likely strong [material](Material "Material") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



## Setup


To demonstrate this so called **Beal Effect** it is neccessary to consider awareness of [terminal nodes](Terminal_Node "Terminal Node") where [mate scores](Score#MateScores "Score") would favour deeper lookahead. Therefor root-random is replaced by lookahead-zero, performing a lookahead with the same search depth as lookahead-random, but non terminal [leaves](Leaf_Node "Leaf Node") evaluated as zero, only tie-breaking at the root by a random number. Still a very weak player, a five ply search was already sufficient to win all of 100 games versus a random player. 


Beal and Smith used following setup to automatically play the games: [Draws](Draw "Draw") by [stalemate](Stalemate "Stalemate") and four cases of [insufficient material](Material#InsufficientMaterial "Material") were recognized (KK, KNK, KBK, KNNK), but [50-move rule](Fifty-move_Rule "Fifty-move Rule") or threefold [repetition](Repetitions "Repetitions") discarded. Therefor games were limited to 200 moves and then WDL adjudicated by +=- material balance (which happend rarely) <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## Further Experiments


Beal and Smith further applied random evaluations to components rather than the whole evaluation. They used [material balance](Material#Balance "Material") as dominating term plus a random number below one pawn unit. While a five ply search with random component only gained 63% over zero component, [quiescing](Quiescence_Search "Quiescence Search") the material balance by exploring a capture tree in order to obtain the chess specific part of the evaluation, the random component gained 97% within the same search depth of five plies.



## See also


* [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
* [Depth](Depth "Depth")
* [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Evaluation](Evaluation "Evaluation")
* [Leaf Node](Leaf_Node "Leaf Node")
* [Match Statistics](Match_Statistics "Match Statistics")
* [Mobility](Mobility "Mobility")
* [Playing Strength](Playing_Strength "Playing Strength")
* [Pseudorandom Number Generator](Pseudorandom_Number_Generator "Pseudorandom Number Generator")
* [Score Granularity](Score#Grain "Score")
* [Scoring Root Moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man")
* [Search Instability](Search_Instability "Search Instability")
* [Search Pathology](Search_Pathology "Search Pathology")
* [Search versus Knowledge](Knowledge#SearchversusKnowledge "Knowledge")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")


## Publications


### 1985 ...


* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1985**). *A Cure for Pathological Behavior in Games that Use Minimax.* [Uncertainty in Artificial Intelligence 1](Laveen_Kanal#Uncertainty_AI_1 "Laveen Kanal"), [arXiv:1304.3444](https://arxiv.org/abs/1304.3444)
* [Bruce Abramson](Bruce_Abramson "Bruce Abramson"), [Richard Korf](Richard_Korf "Richard Korf") (**1987**). *A Model of Two-Player Evaluation Functions.* [AAAI-87](http://www.aaai.org/Conferences/AAAI/aaai87.php). [pdf](http://www.aaai.org/Papers/AAAI/1987/AAAI87-016.pdf)


### 1990 ...


* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1990**). *[Expected-Outcome: A General Model of Static Evaluation](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=44404)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 2
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**1995**). *A Partial Analysis of Minimaxing Game Trees with Random Leaf Values*. [ICCA Journal, Vol. 18, No. 1](ICGA_Journal#18_1 "ICGA Journal")
* [Andreas Junghanns](Andreas_Junghanns "Andreas Junghanns"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *Search versus knowledge in game-playing programs revisited*. [IJCAI-97](Conferences#IJCAI1997 "Conferences"), Vol 1, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.32.168&rep=rep1&type=pdf) » [Search versus Knowledge in Practice](Knowledge#InPractice "Knowledge")


### 2000 ...


* [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**2001**). *The Effect of Mobility on Minimaxing of Game Trees with Random Leaf Values*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 130, No. 1, Review in [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#18_1 "ICGA Journal"), [pdf](https://pdfs.semanticscholar.org/eb82/03fe314d912cdf52aa9fbdabd073751e5a2d.pdf)
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**2002**). *[The Secret of Selective Game Tree Search, When Using Random-Error Evaluations](http://www.springerlink.com/content/f6b4wb6l63dpd0jv/)*. Proceedings of 19th Annual Symposium on Theoretical Aspects of Computer Science (STACS), [pdf](http://www.top-5000.nl/ps/The%20secret%20of%20selective%20earch%20when%20using%20random.pdf)
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Susanne Heuser](index.php?title=Susanne_Heuser&action=edit&redlink=1 "Susanne Heuser (page does not exist)") (**2005**). *Randomised Evaluations in Single-Agent Search*. [ICGA Journal, Vol. 28, No. 1](ICGA_Journal#28_1 "ICGA Journal"), [preprint as pdf](https://www.minet.uni-jena.de/preprints/althoefer_05/altheuser.pdf)
* [Brandon Wilson](index.php?title=Brandon_Wilson&action=edit&redlink=1 "Brandon Wilson (page does not exist)"), [Austin Parker](Austin_Parker "Austin Parker"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**2009**). *Error Minimizing Minimax: Avoiding Search Pathology in Game Trees*. [pdf](http://www.cs.umd.edu/~nau/papers/wilson2009error.pdf)


## Forum Posts


### 1990 ...


* [Re: Weakest Chess Program needed](https://groups.google.com/d/msg/rec.games.chess/Qe_5lhAWTsc/79h9BQslCWIJ) by Kenneth S A Oksanen, [rgc](Computer_Chess_Forums "Computer Chess Forums"), November 12, 1991
* [Re: Human VS computer](https://groups.google.com/d/msg/rec.games.chess/xIvJfi92jMc/BQP231Z0V84J) by [Don Beal](Don_Beal "Don Beal"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), July 11, 1994


### 1995 ...


* [Primitive Chess Program](https://groups.google.com/d/msg/rec.games.chess/NXEDz2iTbRc/k6uH2zBMmxMJ) by David Ewart, [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 09, 1995
* [Re: Incoporating chess knowledge in chess programs](https://groups.google.com/d/msg/rec.games.chess.computer/47bgYzU2kyQ/-dkD4FhigHYJ) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 28, 1996 » [Mobility](Mobility "Mobility")
* [random play](https://groups.google.com/d/msg/rec.games.chess.computer/AI3xadkLEIk/lqWaLrHtl7AJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 25, 1996 » [Scoring Root Moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man")
* [Randomness in move selection](https://groups.google.com/d/msg/rec.games.chess.computer/ul-HWewM5FQ/sXcqhGL06UQJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 01, 1996
* [Re: Interesting random chess question - What is probability to win?](https://www.stmintz.com/ccc/index.php?id=28699) by [Jari Huikari](index.php?title=Jari_Huikari&action=edit&redlink=1 "Jari Huikari (page does not exist)"), [CCC](CCC "CCC"), October 03, 1998 » [Nero](Nero "Nero")
* [Random chess statistics, part two](https://www.stmintz.com/ccc/index.php?id=29571) by [Jari Huikari](index.php?title=Jari_Huikari&action=edit&redlink=1 "Jari Huikari (page does not exist)"), [CCC](CCC "CCC"), October 14, 1998
* [Re: Heinz, Hyatt and Newborn next best move paradox](https://groups.google.com/d/msg/rec.games.chess.computer/mGbD5Lky-8E/gAv0u4YOrVkJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 19, 1999
* [Freeware program with RANDOM eval](https://www.stmintz.com/ccc/index.php?id=78795) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), November 20, 1999


### 2000 ...


* [Simple Learning Technique and Random Play](https://www.stmintz.com/ccc/index.php?id=150687) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 18, 2001 » [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [Random factor in static evaluation!](https://www.stmintz.com/ccc/index.php?id=175314) by Tiago Ribeiro, [CCC](CCC "CCC"), June 15, 2001
* [Random play](https://www.stmintz.com/ccc/index.php?id=292517) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), April 08, 2003
* [A question about random numbers](https://www.stmintz.com/ccc/index.php?id=378514) by Antonio Senatore, [CCC](CCC "CCC"), July 22, 2004


### 2005 ...


* [What is "randomness" for a CM9k personality?](https://groups.google.com/d/msg/rec.games.chess.computer/GW48x_Pk7CU/luDZWBl8vBkJ) by Wilma, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 12, 2005 » [Chessmaster](Chessmaster "Chessmaster")
* [Random number mobility scores](https://groups.google.com/d/msg/rec.games.chess.computer/Ab9uA1-8Hlw/UjT_JXTiHuIJ) by Guest, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2008


### 2010 ...


* [Re: To kick off some technical discussions](http://www.open-chess.org/viewtopic.php?f=5&t=18&p=1942#p1942) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 20, 2010


 [Re: To kick off some technical discussions](http://www.open-chess.org/viewtopic.php?f=5&t=18&p=1963) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 20, 2010
* [Pathology on Game trees](http://www.talkchess.com/forum/viewtopic.php?t=35538) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 22, 2010
* [Re: Depth vs playing strength](http://www.talkchess.com/forum/viewtopic.php?t=41902&start=5) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), January 10, 2012 » [The King](The_King "The King")
* [Implications of Lazy eval on Don Beal effect in Fail Soft](http://www.talkchess.com/forum/viewtopic.php?t=54387) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), November 19, 2014


### 2015 ...


* [How to dumb down/weaken/humanize an engine algorithmically?](http://www.talkchess.com/forum/viewtopic.php?t=55011) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), January 18, 2015
* ["random mover" chess programs](http://www.talkchess.com/forum/viewtopic.php?t=60582) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 24, 2016
* [Strategies for weaker play levels](http://www.talkchess.com/forum/viewtopic.php?t=60635) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), June 28, 2016
* [Adding a random small number to the evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=61315) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), September 03, 2016
* [random evaluation perturbation factor](http://www.talkchess.com/forum/viewtopic.php?t=63803) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), April 24, 2017
* [Randomizing an evaluation and retiring opening books](https://groups.google.com/forum/#!topic/fishcooking/SVkQcfGai8U) by [Ivan Ivec](index.php?title=Ivan_Ivec&action=edit&redlink=1 "Ivan Ivec (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2017
* [Near-random movers](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=66596) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), February 14, 2018
* [Why does stockfish randomise draw evaluations?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71707) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), September 01, 2019 » [Stockfish](Stockfish "Stockfish"), [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Draw Score](Score#DrawScore "Score")


### 2020 ...


* [Controlled randomness of evaluation function](https://prodeo.actieforum.com/t123-controlled-randomness-of-evaluation-function) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2020


## External Links


* [Randomization from Wikipedia](https://en.wikipedia.org/wiki/Randomization)
* [Randomized algorithm from Wikipedia](https://en.wikipedia.org/wiki/Randomized_algorithm)
* [Randomness from Wikipedia](https://en.wikipedia.org/wiki/Randomness)
* [Random tree from Wikipedia](https://en.wikipedia.org/wiki/Random_tree)
* [Random walk from Wikipedia](https://en.wikipedia.org/wiki/Random_walk)
* [Cannonball Adderley](https://en.wikipedia.org/wiki/Cannonball_Adderley) - [Autumn Leaves](https://en.wikipedia.org/wiki/Autumn_Leaves_(1945_song)) ([Somethin' Else](https://en.wikipedia.org/wiki/Somethin%27_Else_(Cannonball_Adderley_album)) 1958), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Miles Davis](Category:Miles_Davis "Category:Miles Davis"), [Hank Jones](https://en.wikipedia.org/wiki/Hank_Jones), [Sam Jones](https://en.wikipedia.org/wiki/Sam_Jones_(musician)) and [Art Blakey](Category:Art_Blakey "Category:Art Blakey")
 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Acer palmatum](https://en.wikipedia.org/wiki/Acer_palmatum) subsp. matsumurae (Koidz) Ogata, [image](https://commons.wikimedia.org/wiki/File:Momiji_%E7%B4%85%E8%91%89%E3%81%99%E3%82%8B%E3%83%A4%E3%83%9E%E3%83%A2%E3%83%9F%E3%82%B8_B221212.JPG) by [松岡明芳](https://zh.wikipedia.org/wiki/User:%E6%9D%BE%E5%B2%A1%E6%98%8E%E8%8A%B3), November 22, 2006, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Autumn leaf color from Wikipedia](https://en.wikipedia.org/wiki/Autumn_leaf_color) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> The term "Beal Effect" was coined by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), see [Re: To kick off some technical discussions](http://www.open-chess.org/viewtopic.php?f=5&t=18&p=1963) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 20, 2010
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**1995**). *A Partial Analysis of Minimaxing Game Trees with Random Leaf Values*. [ICCA Journal, Vol. 18, No. 1](ICGA_Journal#18_1 "ICGA Journal")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**2001**). *The Effect of Mobility on Minimaxing of Game Trees with Random Leaf Values*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 130, No. 1
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: "random mover" chess programs](http://www.talkchess.com/forum/viewtopic.php?t=60582&start=1) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 24, 2016
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1994**). *Random Evaluations in Chess*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")

**[Up one Level](Search "Search")**







 
