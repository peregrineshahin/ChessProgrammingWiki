---
title: Leela Chess Zero
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Leela Chess Zero**



 [](https://twitter.com/leelachesszero) Lc0 logo [[1]](#cite_note-1) 
**Leela Chess Zero**, (LCZero, lc0)  

an adaption of [Gian-Carlo Pascutto's](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)") [Go](Go "Go") project [[2]](#cite_note-2) to [Chess](Chess "Chess"), initiated and announced by [Stockfish](Stockfish "Stockfish") co-author [Gary Linscott](Gary_Linscott "Gary Linscott"), who was already responsible for the Stockfish [Testing Framework](Stockfish#TestingFramework "Stockfish") called *Fishtest*. Leela Chess is [open source](Category:Open_Source "Category:Open Source"), released under the terms of [GPL version 3](Free_Software_Foundation#GPL "Free Software Foundation") or later, and supports [UCI](UCI "UCI"). 
The goal is to build a strong chess playing entity following the same type of [deep learning](Deep_Learning "Deep Learning") along with [Monte-Carlo tree search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) techniques of [AlphaZero](AlphaZero "AlphaZero") as described in [DeepMind's](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") 2017 and 2018 papers 
[[3]](#cite_note-3)
[[4]](#cite_note-4)
[[5]](#cite_note-5), 
but using distributed training for the weights of the [deep](Neural_Networks#Deep "Neural Networks") [convolutional neural network](Neural_Networks#Convolutional "Neural Networks") (CNN, DNN, DCNN). 



## Description


Like [AlphaZero](AlphaZero "AlphaZero"), Lc0's [evaluates](Evaluation "Evaluation") [positions](Chess_Position "Chess Position") using non-linear function approximation based on a [deep neural network](Neural_Networks "Neural Networks"), rather than the [linear function approximation](Evaluation#Linear "Evaluation") as used in classical chess programs. 
This neural network takes the board position as input and outputs position evaluation (QValue) and a vector of move probabilities (PValue, policy). 
Once trained, these network is combined with a [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) using the policy to narrow down the search to high­probability moves, 
and using the value in conjunction with a fast rollout policy to evaluate positions in the tree. The MCTS selection is done by a variation of [Rosin's](Christopher_D._Rosin "Christopher D. Rosin") [UCT](UCT "UCT") improvement dubbed [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin") (Predictor + UCT).



### [Board Representation](Board_Representation "Board Representation")


Lc0's color agnostic board is represented by five [bitboards](Bitboards "Bitboards") (own pieces, opponent pieces, orthogonal sliding pieces, diagonal sliding pieces, and pawns including [en passant](En_passant "En passant") target information coded as pawns on rank 1 and 8), two king squares, [castling rights](Castling_Rights "Castling Rights"), and a flag whether the board is [color flipped](Color_Flipping "Color Flipping"). Getting individual piece bitboards requires some [setwise operations](General_Setwise_Operations "General Setwise Operations") such as [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") and [set theoretic difference](General_Setwise_Operations#RelativeComplement "General Setwise Operations") [[10]](#cite_note-10).



### Network


While [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") used two disjoint networks for policy and value, [AlphaZero](AlphaZero "AlphaZero") as well as Leela Chess Zero, share a common "body" connected to disjoint policy and value "heads". The “body” consists of spatial 8x8 planes, using B [residual](Neural_Networks#Residual "Neural Networks") blocks with F filters of kernel size 3x3, stride 1. So far, model sizes FxB of 64x6, 128x10, 192x15, and 256x20 were used. 


Concerning [nodes per second](Nodes_per_Second "Nodes per Second") of the MCTS, smaller models are faster to calculate than larger models. They are faster to train and will earlier recognize progress, but they will also saturate earlier so that at some point more training will no longer improve the engine. Larger and deeper network models will improve the receptivity, the amount of knowledge and pattern to extract from the training samples, with potential for a [stronger](Playing_Strength "Playing Strength") engine. 
As a further improvement, Leele Chess Zero applies the *Squeeze and Excite* (SE) extension to the residual block architecture [[11]](#cite_note-11) [[12]](#cite_note-12). The body is connected to both the policy "head" for the move probability distribution, and the value "head" for the evaluation score aka [winning probability](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo") of the current position and up to seven predecessor positions on the input planes.



### Training


Like in [AlphaZero](AlphaZero "AlphaZero"), the **Zero** suffix implies no other initial knowledge than the rules of the game, to build a superhuman player, starting with truly random self-play games to apply [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") based on the outcome of that games. However, there are derived approaches, such as [Albert Silver's](Albert_Silver "Albert Silver") [Deus X](Deus_X "Deus X"), trying to take a short-cut by initially using [supervised learning](Supervised_Learning "Supervised Learning") techniques, such as feeding in high quality games played by other strong chess playing entities, or huge records of positions with a given preferred move.
The unsupervised training of the NN is about to minimize the [L2-norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm) of the [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) loss of the value output and the policy loss. Further there are experiments to train the value head against not the game outcome, but against the accumulated value for a position after exploring some number of nodes with [UCT](UCT "UCT") [[13]](#cite_note-13).


The distributed training is realized with an sophisticated [client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model). The client, written entirely in the [Go programming language](Go_(Programming_Language) "Go (Programming Language)"), incorporates Lc0 to produce self-play games.Controlled by the server, the client may download the latest network, will start self-playing, and uploading games to the server, who on the other hand will regularly produce and distribute new neural network weights after a certain amount of games available from contributors. The training software consists of [Python](Python "Python") code, the pipeline requires [NumPy](https://en.wikipedia.org/wiki/NumPy) and [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) running on [Linux](Linux "Linux") [[14]](#cite_note-14). 
The server is written in [Go](Go_(Programming_Language) "Go (Programming Language)") along with [Python](Python "Python") and [shell scripts](https://en.wikipedia.org/wiki/Shell_script).



## Structure Diagrams


 [](File:Lc0diagram.png) 
Related to [TCEC](TCEC "TCEC") clone discussions concerning [Deus X](Deus_X "Deus X") and [Allie](Allie "Allie") aka [AllieStein](Allie#AllieStein "Allie"),  

[Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk") published diagrams with all components of the affected engines,  

The above shows the common legend, and the structure of all Leela Chess Zero's components based on current Lc0 engine [[15]](#cite_note-15)



 [](File:Lczero.png) 
Same diagram, but initial LCZero engine, which played [TCEC Season 12](TCEC_Season_12 "TCEC Season 12") [[16]](#cite_note-16)



## Tournament Play


### First Experience


LCZero gained first tournament experience in April 2018 at [TCEC Season 12](TCEC_Season_12 "TCEC Season 12") and over the board at the [WCCC 2018](WCCC_2018 "WCCC 2018")
in [Stockholm](https://en.wikipedia.org/wiki/Stockholm), July 2018. It won the [fourth division](TCEC_Season_13#Fourth "TCEC Season 13") of [TCEC Season 13](TCEC_Season_13 "TCEC Season 13") in August 2018, [Lc0](#Lc0) finally coming in third in the [third division](TCEC_Season_13#Third "TCEC Season 13").



### Breakthrough


[TCEC Season 14](TCEC_Season_14 "TCEC Season 14") from November 2018 until February 2019 became a breakthrough, Lc0 winning the [third](TCEC_Season_14#Third "TCEC Season 14"), [second](TCEC_Season_14#Second "TCEC Season 14") and [first](TCEC_Season_14#First "TCEC Season 14") division, 
to even [qualify](TCEC_Season_14#Premier "TCEC Season 14") for the [superfinal](TCEC_Season_14#Superfinal "TCEC Season 14"), losing by the narrow margin of +10 =81 -9, **50½ - 49½** versus [Stockfish](Stockfish "Stockfish").
Again runner-up at the [TCEC Season 15 premier division](TCEC_Season_15#Premier "TCEC Season 15") in April 2019,
Lc0 aka **LCZero v0.21.1-nT40.T8.610** won the [superfinal](TCEC_Season_15#Superfinal "TCEC Season 15") in May 2019 versus Stockfish with +14 =79 -7, **53½-46½** [[17]](#cite_note-17).
At the [TCEC Season 16 premier division](TCEC_Season_16#Premier "TCEC Season 16") in September 2019, Lc0 became in third behind Stockfish and the [supervised](Supervised_Learning "Supervised Learning") trained [AllieStein](Allie#AllieStein "Allie"),
but Lc0 took revenge by winning the [TCEC Season 17 premier division](TCEC_Season_17#Premier "TCEC Season 17") in spring 2020, as **LCZero v0.24-sv-t60-3010** fighting down Stockfish in a thrilling [superfinal](TCEC_Season_17#Superfinal "TCEC Season 17") in April 2020 with +17 =71 -12, **52½-47½** [[18]](#cite_note-18), but tables turned again in [TCEC Season 18](TCEC_Season_18#Premier "TCEC Season 18"), when Stockfish won the [superfinal](TCEC_Season_18#Superfinal "TCEC Season 18").



## Release Dates


### 2018


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.14.1 - July 08, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.16.0 - July 20, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.17.0 - August 27, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.18.0 - September 30, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.18.1 - October 02, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.19.0 - November 19, 2018
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.19.1.1 - December 10, 2018


### 2019


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.20.9 - January 01, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.20.1 - January 07, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.20.2 - February 01, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.21.1 - March 23, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.21.2 - June 09, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.21.4 - July 28, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.22.0 - August 05, 2019
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.23.2 - December 31, 2019


### 2020


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.23.3 - February 18, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.24.1 - March 15, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.25.1 - April 30, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.26.0 - July 02, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.26.1 - July 15, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.26.2 - September 02, 2020
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") v0.26.3 - October 10, 2020


### 2021


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") [v0.27.0](https://github.com/LeelaChessZero/lc0/releases/tag/v0.27.0) - February 21, 2021
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") [v0.28.0](https://github.com/LeelaChessZero/lc0/releases/tag/v0.28.0) - August 26, 2021
* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") [v0.28.2](https://github.com/LeelaChessZero/lc0/releases/tag/v0.28.2) - December 13, 2021


### 2022


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") [v0.29.0](https://github.com/LeelaChessZero/lc0/releases/tag/v0.29.0) - December 13, 2022


### 2023


* Leela Chess Zero / [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero") [v0.30.0](https://github.com/LeelaChessZero/lc0/releases/tag/v0.30.0) - July 21, 2023


## Authors


* [Leela Chess Contributors](Category:Leela_Chess_Contributor "Category:Leela Chess Contributor")


## See also


* [Allie](Allie "Allie")
* [AlphaZero](AlphaZero "AlphaZero")
* [Ceres](Ceres "Ceres")
* [Fat Fritz](Fat_Fritz "Fat Fritz")
* [Deep Learning](Deep_Learning "Deep Learning")
* [Deus X](Deus_X "Deus X")
* [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)")
* [Leila](Leila "Leila")
* [Maia Chess](Maia_Chess "Maia Chess")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


 [UCT](UCT "UCT")
 [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin")
* [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")


## Publications


* [Bill Jordan](Bill_Jordan "Bill Jordan") (**2020**). *Calculation versus Intuition: Stockfish versus Leela*. [amazon](https://www.amazon.com/Calculation-versus-Intuition-Stockfish-Leela-ebook/dp/B08LYBQDMB/) » [TCEC](TCEC "TCEC"), [Stockfish](Stockfish "Stockfish")
* [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[19]](#cite_note-19)
* [Rejwana Haque](index.php?title=Rejwana_Haque&action=edit&redlink=1 "Rejwana Haque (page does not exist)"), [Ting Han Wei](index.php?title=Ting_Han_Wei&action=edit&redlink=1 "Ting Han Wei (page does not exist)"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2021**). *On the Road to Perfection? Evaluating Leela Chess Zero Against Endgame Tablebases*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")


## Forum Posts


### 2018


* [Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 09, 2018


 [Re: Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280&start=67) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2018 » [Rollout Paradigm](Bojun_Huang#Rollout "Bojun Huang")
* [Policy and value heads are from AlphaGo Zero, not Alpha Zero Issue #47](https://github.com/glinscott/leela-chess/issues/47) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [glinscott/leela-chess · GitHub](https://github.com/glinscott/leela-chess), January 24, 2018
* [LCZero is learning](http://www.talkchess.com/forum/viewtopic.php?t=66452) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 30, 2018
* [LCZero update](http://www.talkchess.com/forum/viewtopic.php?t=66824) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 14, 2018


 [LCZero update (2)](http://talkchess.com/forum/viewtopic.php?t=66929) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), March 25, 2018
* [LCZero: Progress and Scaling. Relation to CCRL Elo](http://www.talkchess.com/forum/viewtopic.php?t=66945) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 28, 2018 » [Playing Strength](Playing_Strength "Playing Strength")
* [What does LCzero learn?](http://www.talkchess.com/forum/viewtopic.php?t=67013) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 05, 2018
* [How to play vs LCZero with Cute Chess gui](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67044) by Hai, [CCC](CCC "CCC"), April 08, 2018 » [Cute Chess](Cute_Chess "Cute Chess")
* [LCZero in Aquarium / Fritz](http://www.talkchess.com/forum/viewtopic.php?t=67075) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), April 11, 2018
* [LCZero on 10x128 now](http://www.talkchess.com/forum/viewtopic.php?t=67087) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), April 12, 2018
* [lczero faq](http://www.talkchess.com/forum/viewtopic.php?t=67092) by Duncan Roberts, [CCC](CCC "CCC"), April 13, 2018
* [Run LC Zero in LittleBlitzerGUI](http://www.talkchess.com/forum/viewtopic.php?t=67104) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), April 14, 2018 » [LittleBlitzer](LittleBlitzer "LittleBlitzer")
* [LC0 - how to catch up?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67121) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 16, 2018
* [Leela on more then one GPU?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67300) by [Karlo Balla](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), May 01, 2018
* [GPU contention](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67357) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [CCC](CCC "CCC"), May 07, 2018 » [GPU](GPU "GPU")
* [New CLOP settings give Leela huge tactics boost](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67646) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), June 04, 2018 » [CLOP](CLOP "CLOP")
* [First Win by Leela Chess Zero against Stockfish dev](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67668) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), June 07, 2018 » [Stockfish](Stockfish "Stockfish")
* [what may be two firsts...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67718) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), June 13, 2018 » [DGT Pi](DGT_Pi "DGT Pi")
* [LcZero and STS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67728) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 14, 2018 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite")
* [Who entered Leela into WCCC? Bad idea!!](https://groups.google.com/d/msg/lczero/S-rhiPLnbHg/XY9-Z1LWCAAJ) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), June 23, 2018 » [WCCC 2018](WCCC_2018 "WCCC 2018")
* [how will Leela fare at the WCCC?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67949) by dannyb, [CCC](CCC "CCC"), July 10, 2018 » [WCCC 2018](WCCC_2018 "WCCC 2018")
* [Lc0 will participate at the WCCC? Wow!](https://groups.google.com/d/msg/lczero/EgEslxR04wg/6zY7sLiQAwAJ) by Martin Renneke, [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), July 10, 2018
* [How Leela uses history planes](https://groups.google.com/d/msg/lczero/KUwypuefNdY/DDV8hfwCBQAJ) by Tristrom Cooke, [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), July 19, 2018
* [Why Lc0 eval (in cp) is asymmetric against AB engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68072) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 25, 2018 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [TCEC season 13, 2 NN engines will be participating, Leela and Deus X](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68094) by Nay Lin Tun, [CCC](CCC "CCC"), July 28, 2018


 [Re: TCEC season 13, 2 NN engines will be participating, Leela and Deus X](http://talkchess.com/forum3/viewtopic.php?f=2&t=68094&start=90#p770006) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 03, 2018
* [Has Silver written any code for "his" ZeusX?](https://groups.google.com/d/msg/lczero/vGdNYW-Ou58/Kh0GCj2OCgAJ) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), July 31, 2018


 [Re: Has Silver written any code for "his" ZeusX?](https://groups.google.com/d/msg/lczero/vGdNYW-Ou58/-icwb0pjDAAJ) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), August 02, 2018 
* [Some properties of Lc0 playing](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68441) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 14, 2018
* [How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448) by Hai, September 15, 2018 [[20]](#cite_note-20)


 [Re: How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448&start=2) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 16, 2018
 [Re: How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448&start=9) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 17, 2018 [[21]](#cite_note-21)
 [Re: How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448&start=37) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), October 28, 2018
 [Re: How good is the RTX 2080 Ti for Leela?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68448&start=44) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), November 15, 2018
* [LC0 0.18rc1 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68511) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), September 25, 2018
* [My non-OC RTX 2070 is very fast with Lc0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68973) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 19, 2018 [[22]](#cite_note-22)
* [2900 Elo points progress, 10 million games, 330 nets](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69045) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 25, 2018


 [Re: 2900 Elo points progress, 10 million games, 330 nets](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69045&start=8) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), November 25, 2018
* [Scaling of Lc0 at high Leela Ratio](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69068) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 27, 2018
* [Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=75) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 07, 2018 » [AlphaZero](AlphaZero "AlphaZero")
* [Policy training in Alpha Zero, LC0 ..](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69306) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), December 18, 2018 » [AlphaZero](AlphaZero "AlphaZero")
* [LC0 using 4 x 2080 Ti GPU's on Chess.com tourney?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69400) by M. Ansari, [CCC](CCC "CCC"), December 28, 2018
* [Smallnet (128x10) run1 progresses remarkably well](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69318) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 19, 2018
* [use multiple neural nets?](https://groups.google.com/d/msg/lczero/EGcJSrZYLiw/netJ4S38CgAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2018


### 2019


* [LCZero FAQ is missing one important fact](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69478) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 01, 2019 » [GPU](GPU "GPU")
* ["boosting" endgames in leela training? Simple change to learning process proposed: "forked" training games](https://groups.google.com/d/msg/lczero/CrMiK3OR1og/mcFd0NDKDQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2019
* [Leela on a weak pc, question](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69552) by chessico, [CCC](CCC "CCC"), January 09, 2019
* [Michael Larabel benches lc0 on various GPUs](https://groups.google.com/d/msg/lczero/I0lTgR-fFFU/NGC3kJDzAwAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2019 » [GPU](GPU "GPU")
* [Can somebody explain what makes Leela as strong as Komodo?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69622) by Chessqueen, [CCC](CCC "CCC"), January 16, 2019
* [A0 policy head ambiguity](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69668) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2019 » [AlphaZero](AlphaZero "AlphaZero")
* [Schizophrenic rating model for Leela](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69672) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 21, 2019 » [Match Statistics](Match_Statistics "Match Statistics")
* [Leela Zero (Lc0) - NVIDIA Geforce RTX 2060](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=10194) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CSS Forum](Computer_Chess_Forums "Computer Chess Forums"), January 29, 2019
* [11258-32x4-se distilled network released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69820) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), February 03, 2019
* [Lc0 setup Hilfe](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=10213) by [Clemens Keck](index.php?title=Clemens_Keck&action=edit&redlink=1 "Clemens Keck (page does not exist)"), [CSS Forum](Computer_Chess_Forums "Computer Chess Forums"), February 07, 2019 (German)
* [Lc0 - macOS binary requested](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69852) by Steppenwolf, [CCC](CCC "CCC"), February 09, 2019 » [Mac OS](Mac_OS "Mac OS")
* [Thanks for LC0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69957) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), February 19, 2019
* [Re: Training the trainer: how is it done for Stockfish?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70069&start=10) by Graham Jones, [CCC](CCC "CCC"), March 03, 2019 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [Stockfish](Stockfish "Stockfish")
* [Lc0 51010](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70350) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 29, 2019
* [Using LC0 with one or two GPUs - a guide](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70362) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 30, 2019 » [GPU](GPU "GPU")
* [32930 Boost network available](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70451) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), April 09, 2019
* [Lc0 question](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71209) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), July 06, 2019
* [Some newbie questions about lc0](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71651) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), August 25, 2019
* [Lc0 Evaluation Explanation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71686) by Hamster, [CCC](CCC "CCC"), August 29, 2019


 [Re: Lc0 Evaluation Explanation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71686&start=14) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), September 03, 2019
* [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), September 14, 2019 » [TCEC](TCEC "TCEC")
* [Best Nets for Lc0 Page](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72640) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), December 23, 2019
* [Correct LC0 syntax for multiple GPUs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72685) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 30, 2019


### 2020


* [Lc0 soon to support chess960 ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73684) by Modern Times, [CCC](CCC "CCC"), April 18, 2020 » [Chess960](Chess960 "Chess960")
* [How to run rtx 2080ti for leela optimally?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73714) by h1a8, [CCC](CCC "CCC"), April 20, 2020
* [Total noob Leela question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74092) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 03, 2020
* [How strong is Stockfish NNUE compared to Leela..](https://groups.google.com/d/msg/lczero/BvhCa-muLt0/ZzINQk_vCQAJ) by OmenhoteppIV, [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [LC0 vs. NNUE - some tech details...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74607) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 29, 2020 » [NNUE](NNUE "NNUE")
* [The next step for LC0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74915) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), August 28, 2020
* [Checking the backends with the new lc0 binary](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75262) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), October 01, 2020
* [ZZ-tune conclusively better than the Kiudee default for Lc0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75950) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 01, 2020 [[23]](#cite_note-23)


### 2021


* [Announcing Ceres](https://lczero.org/blog/2021/01/announcing-ceres/) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), LCZero blog, January 01, 2021 » [Ceres](Ceres "Ceres")
* [leela](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76948) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), March 29, 2021 » [Banksia GUI](Banksia_GUI "Banksia GUI"), [iPhone](index.php?title=IPhone&action=edit&redlink=1 "IPhone (page does not exist)")
* [Joking FTW, Seriously](https://lczero.org/blog/2021/04/joking-ftw-seriously/) by borg, LCZero blog, April 25, 2021
* [The importance of open data](https://lczero.org/blog/2021/06/the-importance-of-open-data/) by borg, LCZero blog, June 15, 2021
* [Leela data publicly available for use](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77496) by Madeleine Birchfield, [CCC](CCC "CCC"), June 15, 2021
* [will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503) by Wilson, [CCC](CCC "CCC"), June 17, 2021 » [TCEC Season 21](TCEC_Season_21 "TCEC Season 21")


## External Links


### Chess Engine


* [Leela Chess Zero](https://lczero.org/)
* [Blog - Leela Chess Zero](https://lczero.org/blog/)
* [LCZero – Forum](https://groups.google.com/forum/#!forum/lczero)
* [Testing instance of LCZero server](https://training.lczero.org/)
* [Leela Chess Zero from Wikipedia](https://en.wikipedia.org/wiki/Leela_Chess_Zero)
* [Leela (software) from Wikipedia](https://en.wikipedia.org/wiki/Leela_(software))
* [Leela Chess Zero - Facebook](https://www.facebook.com/LeelaChessZero/)
* [Leela Chess Zero (@LeelaChessZero) | Twitter](https://twitter.com/leelachesszero)
* [Lc0 Slides](https://slides.com/crem/lc0#/logo) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk")


### GitHub


* [LCZero · GitHub](https://github.com/LeelaChessZero/)
* [GitHub - LeelaChessZero/lczero: A chess adaption of GCP's Leela Zero](https://github.com/LeelaChessZero/lczero)
* [GitHub - LeelaChessZero/lc0: The rewritten engine, originally for tensorflow. Now all other backends have been ported here](https://github.com/LeelaChessZero/lc0)
* [Home · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki)
* [Getting Started · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/Getting-Started)
* [FAQ · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/FAQ)
* [Technical Explanation of Leela Chess Zero · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/Technical-Explanation-of-Leela-Chess-Zero)
* [Contributors to LeelaChessZero/lc0 · GitHub](https://github.com/LeelaChessZero/lc0/graphs/contributors)
* [Use NHCW layout for fused winograd residual block (#1567) · LeelaChessZero/lc0@62741d5 · GitHub](https://github.com/LeelaChessZero/lc0/commit/62741d56252b23f74e8a7200a42812f27fe32b7d), commit by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), June 10, 2021
* [GitHub - mooskagh/lc0: The rewritten engine, originally for cudnn. Now all other backends have been ported here](https://github.com/mooskagh/lc0)
* [Distilled Networks · dkappe/leela-chess-weights Wiki · GitHub](https://github.com/dkappe/leela-chess-weights/wiki/Distilled-Networks)


### Rating Lists


* [Leela Chess Zero](http://computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Leela%20Chess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")
* [Leela Chess Zero](http://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Leela%20Chess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### ChessBase


* [Leela Chess Zero: AlphaZero for the PC](https://en.chessbase.com/post/leela-chess-zero-alphazero-for-the-pc) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), April 26, 2018
* [Standing on the shoulders of giants](https://en.chessbase.com/post/standing-on-the-shoulders-of-giants) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 18, 2019
* [Running Leela and Fat Fritz on your notebook](https://en.chessbase.com/post/running-leela-and-fat-fritz-on-your-notebook) by [Evelyn Zhu](https://ratings.fide.com/card.phtml?event=2099713), [ChessBase News](ChessBase "ChessBase"), June 14, 2020 » [Fat Fritz](Fat_Fritz "Fat Fritz")


### Chessdom


* [Interview with Alexander Lyashuk about the recent success of Lc0](http://www.chessdom.com/interview-with-alexander-lyashuk-about-the-recent-success-of-lc0/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), February 6, 2019 » [TCEC Season 14](TCEC_Season_14 "TCEC Season 14")


### Tuning


* [GitHub - kiudee/bayes-skopt: A fully Bayesian implementation of sequential model-based optimization](https://github.com/kiudee/bayes-skopt) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt") » [Fat Fritz](Fat_Fritz "Fat Fritz") [[24]](#cite_note-24)
* [GitHub - kiudee/chess-tuning-tools](https://github.com/kiudee/chess-tuning-tools) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt") [[25]](#cite_note-25)


### Misc


* [Leela from Wikipedia](https://en.wikipedia.org/wiki/Leela)
* [Leela (game) from Wikipedia](https://en.wikipedia.org/wiki/Leela_(game))
* [Leela (name) from Wikipedia](https://en.wikipedia.org/wiki/Leela_(name))
* [Leela (Doctor Who) from Wikipedia](https://en.wikipedia.org/wiki/Leela_(Doctor_Who))
* [Leela (Futurama) from Wikipedia](https://en.wikipedia.org/wiki/Leela_(Futurama))
* [Soft Machine](Category:Soft_Machine "Category:Soft Machine") - [Hidden Details](https://en.wikipedia.org/wiki/Hidden_Details), 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 Lineup: [Theo Travis](https://en.wikipedia.org/wiki/Theo_Travis), [Roy Babbington](Category:Roy_Babbington "Category:Roy Babbington"), [John Etheridge](https://en.wikipedia.org/wiki/John_Etheridge), [John Marshall](Category:John_Marshall "Category:John Marshall")
 
## References


1. [↑](#cite_ref-1) [Leela Chess Zero (@LeelaChessZero) | Twitter](https://twitter.com/leelachesszero)
2. [↑](#cite_ref-2) [GitHub - gcp/leela-zero: Go engine with no human-provided knowledge, modeled after the AlphaGo Zero paper](https://github.com/gcp/leela-zero)
3. [↑](#cite_ref-3) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
4. [↑](#cite_ref-4) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 362, No. 6419
5. [↑](#cite_ref-5) [AlphaZero paper, and Lc0 v0.19.1](http://blog.lczero.org/2018/12/alphazero-paper-and-lc0-v0191.html) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), LCZero blog, December 07, 2018
6. [↑](#cite_ref-6) [lc0 transition · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/lc0-transition)
7. [↑](#cite_ref-7) [Re: TCEC season 13, 2 NN engines will be participating, Leela and Deus X](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68094&start=91) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 03, 2018
8. [↑](#cite_ref-8) [NVIDIA cuDNN | NVIDIA Developer](https://developer.nvidia.com/cudnn)
9. [↑](#cite_ref-9) [Re: My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822&start=48) by [Adam Treat](Adam_Treat "Adam Treat"), [CCC](CCC "CCC"), September 19, 2019
10. [↑](#cite_ref-10) [lc0/board.h at master · LeelaChessZero/lc0 · GitHub](https://github.com/LeelaChessZero/lc0/blob/master/src/chess/board.h)
11. [↑](#cite_ref-11) [Technical Explanation of Leela Chess Zero · LeelaChessZero/lc0 Wiki · GitHub](https://github.com/LeelaChessZero/lc0/wiki/Technical-Explanation-of-Leela-Chess-Zero)
12. [↑](#cite_ref-12) [Squeeze-and-Excitation Networks – Towards Data Science](https://towardsdatascience.com/squeeze-and-excitation-networks-9ef5e71eacd7) by [Paul-Louis Pröve](http://plpp.de/), October 17, 2017
13. [↑](#cite_ref-13) [Lessons From AlphaZero (part 4): Improving the Training Target](https://medium.com/oracledevs/lessons-from-alphazero-part-4-improving-the-training-target-6efba2e71628) by [Vish Abrams](https://blogs.oracle.com/author/vish-abrams), [Oracle Blog](https://blogs.oracle.com/), June 27, 2018
14. [↑](#cite_ref-14) [GitHub - LeelaChessZero/lczero-training: For code etc relating to the network training process.](https://github.com/LeelaChessZero/lczero-training)
15. [↑](#cite_ref-15) [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), September 14, 2019 » [TCEC](TCEC "TCEC")
16. [↑](#cite_ref-16) [My failed attempt to change TCEC NN clone rules](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71822) by [Alexander Lyashuk](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), September 14, 2019 » [TCEC](TCEC "TCEC")
17. [↑](#cite_ref-17) [Lc0 won TCEC 15](https://blog.lczero.org/2019/05/lc0-won-tcec-15.html) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), LCZero blog, May 28, 2019
18. [↑](#cite_ref-18) [TCEC S17 SUper FInal report](https://lczero.org/blog/2020/04/tcec-s17-super-final-report/) by @glbchess64, LCZero blog, April 21, 2020
19. [↑](#cite_ref-19) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021
20. [↑](#cite_ref-20) [GeForce 20 series from Wikipedia](https://en.wikipedia.org/wiki/GeForce_20_series)
21. [↑](#cite_ref-21) [Multiply–accumulate operation - Wikipedia](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation)
22. [↑](#cite_ref-22) [GeForce RTX 2070 Graphics Card | NVIDIA](https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2070/)
23. [↑](#cite_ref-23) [GitHub - kiudee/chess-tuning-tools](https://github.com/kiudee/chess-tuning-tools) by [Karlson Pfannschmidt](Karlson_Pfannschmidt "Karlson Pfannschmidt")
24. [↑](#cite_ref-24) [Fat Fritz 1.1 update and a small gift](https://en.chessbase.com/post/fat-fritz-update-and-fat-fritz-jr) by [Albert Silver](Albert_Silver "Albert Silver"). [ChessBase News](ChessBase "ChessBase"), March 05, 2020
25. [↑](#cite_ref-25) [Welcome to Chess Tuning Tools’s documentation!](https://chess-tuning-tools.readthedocs.io/en/latest/)

**[Up one level](Engines "Engines")**







 
