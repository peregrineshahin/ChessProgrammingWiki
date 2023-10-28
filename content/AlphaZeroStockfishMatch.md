---
title: AlphaZeroStockfishMatch
---
**[Home](Home "Home") * [Engines](Engines "Engines") * AlphaZero**

|  |  |
| --- | --- |
| **AlphaZero**,
a chess and [Go](Go "Go") playing entity by [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") based on a general [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") algorithm with the same name. On [December 5](https://en.wikipedia.org/wiki/December_5#Holidays_and_observances), [2017](https://en.wikipedia.org/wiki/Portal:Current_events/2017_December_5) [[1]](#cite_note-1), the DeepMind team around [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), and [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") along with former [Giraffe](Giraffe "Giraffe") author [Matthew Lai](Matthew_Lai "Matthew Lai"), reported on their generalized algorithm, combining [Deep learning](Deep_Learning "Deep Learning") with [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) [[2]](#cite_note-2). The final [peer reviewed](https://en.wikipedia.org/wiki/Peer_review) paper with various clarifications was published almost one year later in the [Science magazine](<https://en.wikipedia.org/wiki/Science_(journal)>) under the title *A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play* [[3]](#cite_note-3).

Starting from random play, and given no domain knowledge except the game rules, AlphaZero achieved a superhuman level of play in the games of chess and [Shogi](Shogi "Shogi") as well as in [Go](Go "Go"). The algorithm is a more generic version of the [AlphaGo Zero](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") algorithm that was first introduced in the domain of Go [[4]](#cite_note-4). AlphaZero [evaluates](Evaluation "Evaluation") [positions](Chess_Position "Chess Position") using non-linear function approximation based on a [deep neural network](Neural_Networks "Neural Networks"), rather than the [linear function approximation](Evaluation#Linear "Evaluation") as used in classical chess programs.
This neural network takes the board position as input and outputs a vector of move probabilities (policy) and a position evaluation. Once trained, these network is combined with a [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) using the policy to narrow down the search to high ­probability moves, and using the value in conjunction with a fast rollout policy to evaluate positions in the tree. The selection is done by a variation of [Rosin's](Christopher_D._Rosin "Christopher D. Rosin") [UCT](UCT "UCT") improvement dubbed [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin").
| „Zeroist die Stille. Zero ist derAnfang. Zero ist rund. Zero dreht sich.Zero ist der Mond. Die Sonne ist Zero.Zero ist weiss. Die Wüste Zero. Der Himmelüber Zero. Die Nacht –, Zero fließt. Das AugeZero. Nabel. Mund. Kuß. Die Milch ist rund. DieBlume Zero der Vogel. Schweigend. Schwebend. Ichesse Zero, ich trinke Zero, ich schlafe Zero, ich wacheZero, ich liebe Zero. Zero ist schön, dynamo, dynamo,dynamo. Die Bäume im Frühling, der Schnee, Feuer,Wasser, Meer. Rot orange gelb grün indigo blau violettZero Zero Regenbogen. 4 3 2 1 Zero. Gold undSilber, Schall und Rauch. Wanderzirkus Zero.Zero ist die Stille. Zero ist der Anfang.Zero ist rund. Zero istZero.“  [[5]](#cite_note-5) |

## Contents

- [1 Network Architecture](#Network_Architecture)
- [2 Training](#Training)
- [3 Stockfish Match](#Stockfish_Match)
- [4 See also](#See_also)
- [5 Publications](#Publications)
  - [5.1 2017](#2017)
  - [5.2 2018](#2018)
  - [5.3 2019](#2019)
  - [5.4 2020 ...](#2020_...)
- [6 Forum Posts](#Forum_Posts)
  - [6.1 2017](#2017_2)
  - [6.2 2018](#2018_2)
  - [6.3 2019](#2019_2)
  - [6.4 2020 ...](#2020_..._2)
- [7 Blog Posts](#Blog_Posts)
- [8 External Links](#External_Links)
  - [8.1 OpenSpiel](#OpenSpiel)
  - [8.2 Reports](#Reports)
    - [8.2.1 2017](#2017_3)
    - [8.2.2 2018 ...](#2018_...)
  - [8.3 Stockfish Match](#Stockfish_Match_2)
    - [8.3.1 Round 1](#Round_1)
    - [8.3.2 Round 2, 3](#Round_2.2C_3)
  - [8.4 Misc](#Misc)
- [9 References](#References)

## Network Architecture

The [deep neural network](Neural_Networks#Deep "Neural Networks") consists of a “body” with input and hidden layers of spatial NxN planes, [8x8 board](8x8_Board "8x8 Board") arrays for chess, followed by both policy and value “heads” [[6]](#cite_note-6) [[7]](#cite_note-7).
Each square cell of the input plane contains 6x2 [piece-type](Pieces#PieceTypeCoding "Pieces") and [color](Color "Color") bits of the current [chess position](Chess_Position "Chess Position") from the current player's point of view, plus two bits of a [repetition counter](Repetitions "Repetitions") concerning the [draw](Draw "Draw") rule,
and to further address [graph history](Graph_History_Interaction "Graph History Interaction") and [path-dependency](Path-Dependency "Path-Dependency") issues - these 14 bits times eight, that is up to seven predecessor positions as well - so that [en passant](En_passant "En passant"), or some sense of progress is implicit.
Additional 7 input bits consider [castling rights](Castling_Rights "Castling Rights"), total move count and [side to move](Side_to_move "Side to move"), yielding in 119 bits per square cell for chess.

The body consists of a [rectified](<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>) [batch-normalized](https://en.wikipedia.org/wiki/Batch_normalization) [convolutional layer](Neural_Networks#Convolutional "Neural Networks") followed by 19 [residual](Neural_Networks#Residual "Neural Networks") blocks. Each such block consists of two rectified batch-normalized residual convolutional layers with a skip connection [[8]](#cite_note-8) [[9]](#cite_note-9). Each convolution applies 256 filters (shared weight vectors) of kernel size 3x3 with [stride](https://en.wikipedia.org/wiki/Stride_of_an_array) 1.
These layers connect the pieces on different squares to each other due to consecutive convolutions, where a cell of a layer is connected to the correspondent 3x3 [receptive field](https://en.wikipedia.org/wiki/Receptive_field) of the previous layer,
so that after 4 convolutions, each square is connected to every other cell in the original input layer [[10]](#cite_note-10).

The policy head applies an additional rectified, batch-normalized convolutional layer, followed by a final convolution of 73 filters for chess,
with the final policy output represented as an 8x8 board array as well, for every [origin square](Origin_Square "Origin Square") up to 73 [target square](Target_Square "Target Square") possibilities ([NRayDirs](Direction#MoveDirections "Direction") x [MaxRayLength](Rays "Rays") + [NKnightDirs](Direction#KnightDirections "Direction") + NPawnDirs * [NMinorPromotions](Promotions "Promotions")), encoding a probability distribution over 64x73 = 4,672 possible moves, where illegal moves were masked out by setting their probabilities to zero, re-normalising the probabilities for remaining moves. The value head applies an additional rectified, batch-normalized convolution of 1 filter of kernel size 1x1 with stride 1, followed by a rectified linear layer of size 256 and a [tanh](https://en.wikipedia.org/wiki/Hyperbolic_function)-linear layer of size 1.

## Training

AlphaZero was trained in 700,000 steps or mini-batches of size 4096 each, starting from randomly initialized parameters, using 5,000 [first-generation TPUs](https://en.wikipedia.org/wiki/Tensor_processing_unit#First_generation) [[11]](#cite_note-11) to generate self-play games and 64 [second-generation TPUs](https://en.wikipedia.org/wiki/Tensor_processing_unit#Second_generation) [[12]](#cite_note-12) [[13]](#cite_note-13) [[14]](#cite_note-14) to train the neural networks [[15]](#cite_note-15) .

## Stockfish Match

As mentioned in the December 2017 paper [[16]](#cite_note-16),
a 100 game match versus [Stockfish 8](Stockfish "Stockfish") using 64 [threads](Thread "Thread") and a [transposition table](Transposition_Table "Transposition Table") size of 1GiB,
was won by AlphaZero using a single machine with 4 [first-generation TPUs](https://en.wikipedia.org/wiki/Tensor_processing_unit#First_generation) with +28=72-0, 10 games were published. Despite a possible hardware advantage of AlphaZero and criticized playing conditions [[17]](#cite_note-17), this is a tremendous achievement.

In the final [peer reviewed](https://en.wikipedia.org/wiki/Peer_review) paper, published in [Science magazine](<https://en.wikipedia.org/wiki/Science_(journal)>) in December 2018 [[18]](#cite_note-18) along with supplementary materials [[19]](#cite_note-19), a 1000 game match was reported with about 200 games published, versus various most recent Stockfish versions available at the time of the matches, that is Stockfish 8, a development version as of January 13, 2018 close to Stockfish 9, [Brainfish](Brainfish "Brainfish") with [Cerebellum](index.php?title=Cerebellum&action=edit&redlink=1 "Cerebellum (page does not exist)") book, and Stockfish 9, in total AlphaZero winning 155 games and losing 6 games.

Stockfish was configured according to its [2016 TCEC Season 9 superfinal](TCEC_Season_9#Superfinal "TCEC Season 9") settings: 44 threads on 44 cores (two 2.2GHz [Intel](Intel "Intel") [Xeon Broadwell](https://en.wikipedia.org/wiki/Xeon#E3-12xx_v4_series_%22Broadwell-WS%22) [x86-64](X86-64 "X86-64") CPUs with 22 cores, running [Linux](Linux "Linux")), a transposition table size of 32 GiB, and 6-men [Syzygy bases](Syzygy_Bases "Syzygy Bases"). Time control was 3 hours per side and game plus 15 seconds increment per move. AlphaZero used a simple time control strategy: thinking for 1/20th of the remaining time, and selects moves greedily with respect to the root visit count. Each MCTS was executed on a single machine with 4 [first-generation TPUs](https://en.wikipedia.org/wiki/Tensor_processing_unit#First_generation).

AlphaZero and Stockfish (except Brainfish) used no [opening book](Opening_Book "Opening Book"), 12 common human positions as well as the [2016 TCEC Season 9 superfinal](TCEC_Season_9#Superfinal "TCEC Season 9") positions were played, originally selected by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen") [[20]](#cite_note-20). To ensure diversity against opponents (Brainfish) with a deterministic opening book, AlphaZero used a small amount of randomization in its opening moves. This avoided duplicate games but also resulted in more losses by AlphaZero.

## See also

- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Alpha I](Alpha_I "Alpha I")
- [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
- [Chess Engines with Neural Networks](Neural_Networks#engines "Neural Networks")
- [Learning Chess Programs](Learning#Programs "Learning")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Zeta36](index.php?title=Zeta36&action=edit&redlink=1 "Zeta36 (page does not exist)")

## Publications

## 2017

- [David Silver](David_Silver "David Silver"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Lucas Baker](index.php?title=Lucas_Baker&action=edit&redlink=1 "Lucas Baker (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Adrian Bolton](index.php?title=Adrian_Bolton&action=edit&redlink=1 "Adrian Bolton (page does not exist)"), [Yutian Chen](index.php?title=Yutian_Chen&action=edit&redlink=1 "Yutian Chen (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Fan Hui](index.php?title=Fan_Hui&action=edit&redlink=1 "Fan Hui (page does not exist)"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *[Mastering the game of Go without human knowledge](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 550, [pdf](https://www.gwern.net/docs/rl/2017-silver.pdf)
- [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)

## 2018

- [George Rajna](George_Rajna "George Rajna") (**2018**). *AlphaZero Just Playing*. [viXra:1802.0330](http://vixra.org/abs/1802.0330)
- [Vinton G. Cerf](Mathematician#VGCerf "Mathematician") (**2018**). *[On Neural Networks](https://cacm.acm.org/magazines/2018/7/229041-on-neural-networks/fulltext)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 61, No. 7
  - [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**2018**). *[Comment - Lookahead Search for Computer Chess](https://cacm.acm.org/magazines/2018/12/232884-reclaim-internet-greatness/fulltext)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 61, No. 12
- [Garry Kasparov](Garry_Kasparov "Garry Kasparov") (**2018**). *[Chess, a Drosophila of reasoning](http://science.sciencemag.org/content/362/6419/1087)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419
- [Murray Campbell](Murray_Campbell "Murray Campbell") (**2018**). *[Mastering board games](http://science.sciencemag.org/content/362/6419/1118)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419
- [Chu-Hsuan Hsueh](Chu-Hsuan_Hsueh "Chu-Hsuan Hsueh"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2018**). *AlphaZero for a Non-Deterministic Game*. [TAAI 2018](TAAI_2018 "TAAI 2018") » [Chinese Dark Chess](Chinese_Dark_Chess "Chinese Dark Chess")
- [Nai-Yuan Chang](index.php?title=Nai-Yuan_Chang&action=edit&redlink=1 "Nai-Yuan Chang (page does not exist)"), [Chih-Hung Chen](Chih-Hung_Chen "Chih-Hung Chen"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin"), [Surag Nair](index.php?title=Surag_Nair&action=edit&redlink=1 "Surag Nair (page does not exist)") (**2018**). *[The Big Win Strategy on Multi-Value Network: An Improvement over AlphaZero Approach for 6x6 Othello](https://dl.acm.org/citation.cfm?id=3278325)*. [MLMI2018](https://dl.acm.org/citation.cfm?id=3278312)
- [Yen-Chi Chen](Yen-Chi_Chen "Yen-Chi Chen"), [Chih-Hung Chen](Chih-Hung_Chen "Chih-Hung Chen"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin") (**2018**). *[Exact-Win Strategy for Overcoming AlphaZero](https://dl.acm.org/citation.cfm?id=3293486)*. [CIIS 2018](https://dl.acm.org/citation.cfm?id=3293475) [[21]](#cite_note-21)
- [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419 [[22]](#cite_note-22)

## 2019

- [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), [Natasha Regan](index.php?title=Natasha_Regan&action=edit&redlink=1 "Natasha Regan (page does not exist)") (**2019**). *[Game Changer: AlphaZero's Groundbreaking Chess Strategies and the Promise of AI](https://www.newinchess.com/game-changer)*. [New In Chess](https://en.wikipedia.org/wiki/New_In_Chess)
- [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Jean-Baptiste Lespiau](index.php?title=Jean-Baptiste_Lespiau&action=edit&redlink=1 "Jean-Baptiste Lespiau (page does not exist)"), [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [Satyaki Upadhyay](index.php?title=Satyaki_Upadhyay&action=edit&redlink=1 "Satyaki Upadhyay (page does not exist)"), [Julien Pérolat](index.php?title=Julien_P%C3%A9rolat&action=edit&redlink=1 "Julien Pérolat (page does not exist)"), [Sriram Srinivasan](index.php?title=Sriram_Srinivasan&action=edit&redlink=1 "Sriram Srinivasan (page does not exist)"), [Finbarr Timbers](index.php?title=Finbarr_Timbers&action=edit&redlink=1 "Finbarr Timbers (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [Shayegan Omidshafiei](index.php?title=Shayegan_Omidshafiei&action=edit&redlink=1 "Shayegan Omidshafiei (page does not exist)"), [Daniel Hennes](index.php?title=Daniel_Hennes&action=edit&redlink=1 "Daniel Hennes (page does not exist)"), [Dustin Morrill](index.php?title=Dustin_Morrill&action=edit&redlink=1 "Dustin Morrill (page does not exist)"), [Paul Muller](index.php?title=Paul_Muller&action=edit&redlink=1 "Paul Muller (page does not exist)"), [Timo Ewalds](index.php?title=Timo_Ewalds&action=edit&redlink=1 "Timo Ewalds (page does not exist)"), [Ryan Faulkner](index.php?title=Ryan_Faulkner&action=edit&redlink=1 "Ryan Faulkner (page does not exist)"), [János Kramár](index.php?title=J%C3%A1nos_Kram%C3%A1r&action=edit&redlink=1 "János Kramár (page does not exist)"), [Bart De Vylder](index.php?title=Bart_De_Vylder&action=edit&redlink=1 "Bart De Vylder (page does not exist)"), [Brennan Saeta](index.php?title=Brennan_Saeta&action=edit&redlink=1 "Brennan Saeta (page does not exist)"), [James Bradbury](index.php?title=James_Bradbury&action=edit&redlink=1 "James Bradbury (page does not exist)"), [David Ding](index.php?title=David_Ding&action=edit&redlink=1 "David Ding (page does not exist)"), [Sebastian Borgeaud](index.php?title=Sebastian_Borgeaud&action=edit&redlink=1 "Sebastian Borgeaud (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Thomas Anthony](index.php?title=Thomas_Anthony&action=edit&redlink=1 "Thomas Anthony (page does not exist)"), [Edward Hughes](index.php?title=Edward_Hughes&action=edit&redlink=1 "Edward Hughes (page does not exist)"), [Ivo Danihelka](index.php?title=Ivo_Danihelka&action=edit&redlink=1 "Ivo Danihelka (page does not exist)"), [Jonah Ryan-Davis](index.php?title=Jonah_Ryan-Davis&action=edit&redlink=1 "Jonah Ryan-Davis (page does not exist)") (**2019**). *OpenSpiel: A Framework for Reinforcement Learning in Games*. [arXiv:1908.09453](https://arxiv.org/abs/1908.09453) [[23]](#cite_note-23)

## 2020 ...

- [Nenad Tomašev](index.php?title=Nenad_Toma%C5%A1ev&action=edit&redlink=1 "Nenad Tomašev (page does not exist)"), [Ulrich Paquet](index.php?title=Ulrich_Paquet&action=edit&redlink=1 "Ulrich Paquet (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Vladimir Kramnik](index.php?title=Vladimir_Kramnik&action=edit&redlink=1 "Vladimir Kramnik (page does not exist)") (**2020**). *Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess*. [arXiv:2009.04374](https://arxiv.org/abs/2009.04374)
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Patrick Korus](Patrick_Korus "Patrick Korus"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting") (**2020**). *Monte-Carlo Graph Search for AlphaZero*. [arXiv:2012.11045](https://arxiv.org/abs/2012.11045) » [CrazyAra](CrazyAra "CrazyAra")
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Patrick Korus](Patrick_Korus "Patrick Korus"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting") (**2021**). *[Improving AlphaZero Using Monte-Carlo Graph Search](https://ojs.aaai.org/index.php/ICAPS/article/view/15952)*. [Proceedings of the Thirty-First International Conference on Automated Planning and Scheduling](https://ojs.aaai.org/index.php/ICAPS/issue/view/380), Vol. 31, [pdf](https://www.ml.informatik.tu-darmstadt.de/papers/czech2021icaps_mcgs.pdf)
- [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[24]](#cite_note-24)
- [Thomas McGrath](index.php?title=Thomas_McGrath&action=edit&redlink=1 "Thomas McGrath (page does not exist)"), [Andrei Kapishnikov](index.php?title=Andrei_Kapishnikov&action=edit&redlink=1 "Andrei Kapishnikov (page does not exist)"), [Nenad Tomašev](index.php?title=Nenad_Toma%C5%A1ev&action=edit&redlink=1 "Nenad Tomašev (page does not exist)"), [Adam Pearce](index.php?title=Adam_Pearce&action=edit&redlink=1 "Adam Pearce (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Been Kim](index.php?title=Been_Kim&action=edit&redlink=1 "Been Kim (page does not exist)"), [Ulrich Paquet](index.php?title=Ulrich_Paquet&action=edit&redlink=1 "Ulrich Paquet (page does not exist)"), [Vladimir Kramnik](index.php?title=Vladimir_Kramnik&action=edit&redlink=1 "Vladimir Kramnik (page does not exist)") (**2021**). *Acquisition of Chess Knowledge in AlphaZero*. [arXiv:2111.09259](https://arxiv.org/abs/2111.09259) [[25]](#cite_note-25)
- [Nenad Tomašev](index.php?title=Nenad_Toma%C5%A1ev&action=edit&redlink=1 "Nenad Tomašev (page does not exist)"), [Ulrich Paquet](index.php?title=Ulrich_Paquet&action=edit&redlink=1 "Ulrich Paquet (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Vladimir Kramnik](index.php?title=Vladimir_Kramnik&action=edit&redlink=1 "Vladimir Kramnik (page does not exist)") (**2022**). *[Reimagining Chess with AlphaZero](https://cacm.acm.org/magazines/2022/2/258230-reimagining-chess-with-alphazero/fulltext)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 65, No. 2

## Forum Posts

## 2017

- [Google's AlphaGo team has been working on chess](http://www.talkchess.com/forum/viewtopic.php?t=65909) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [CCC](CCC "CCC"), December 06, 2017
- [Historic Milestone: AlphaZero](http://www.talkchess.com/forum/viewtopic.php?t=65910) by Miguel Castanuela, [CCC](CCC "CCC"), December 06, 2017
- [AlphaZero beats AlphaGo Zero, Stockfish, and Elmo](http://www.talkchess.com/forum/viewtopic.php?t=65911) by Carl Lumma, [CCC](CCC "CCC"), December 06, 2017
- [AlphaZero vs Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=65919) by Bigler, [CCC](CCC "CCC"), December 06, 2017
- [Deepmind drops the bomb](https://groups.google.com/forum/#!topic/fishcooking/pcFRIurN_l4) by Leebot, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017
- [AlphaZero beats Stockfish 8 by 64-36](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32392) by [Venator](Jeroen_Noomen "Jeroen Noomen"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017
- [Alpha Zero](http://www.open-chess.org/viewtopic.php?f=5&t=3153) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017
- [AlphaGo Zero And AlphaZero, RomiChess done better](http://www.talkchess.com/forum/viewtopic.php?t=65924) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), December 07, 2017 » [RomiChess](RomiChess "RomiChess")
- [BBC News; 'Google's ... DeepMind AI claims chess crown'](http://www.hiarcs.net/forums/viewtopic.php?t=8709) by pennine22, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2017
- [Press Release Stockfish vs. AlphaZero](https://groups.google.com/d/msg/fishcooking/S5W57LgDHQ8/WNiGb_25BgAJ) by Michael Whiteley, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 08, 2017
- [AlphaZero reinvents mobility and romanticism](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32398) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 08, 2017 » [Alpha Zero's "Immortal Zugzwang Game"](AlphaZero#ImmortalZugzwang "AlphaZero")
- [Reactions about AlphaZero from top GMs...](http://www.talkchess.com/forum/viewtopic.php?t=65934) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 08, 2017 » [Reactions From Top GMs, Stockfish Author](AlphaZero#Reactions "AlphaZero")
- [AlphaZero is not like other chess programs](http://www.talkchess.com/forum/viewtopic.php?t=65937) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 08, 2017

[Re: AlphaZero is not like other chess programs](http://www.talkchess.com/forum/viewtopic.php?t=65937&start=10) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 09, 2017

- [Photo of Google Cloud TPU cluster](http://www.talkchess.com/forum/viewtopic.php?t=65945) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 09, 2017
- [Cerebellum analysis of the AlphaZero - Stockfish Games](http://www.talkchess.com/forum/viewtopic.php?t=65983) by [Thomas Zipproth](index.php?title=Thomas_Zipproth&action=edit&redlink=1 "Thomas Zipproth (page does not exist)"), [CCC](CCC "CCC"), December 11, 2017 » [Cerebellum](index.php?title=Cerebellum&action=edit&redlink=1 "Cerebellum (page does not exist)")
- [Open letter to Google DeepMind](https://groups.google.com/d/msg/fishcooking/ExSnY8xy7sY/_x32q6INCAAJ) by Michael Stembera, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 12, 2017
- [recent article on alphazero ... 12/11/2017 ...](http://www.talkchess.com/forum/viewtopic.php?t=66005) by Dan Ellwein, [CCC](CCC "CCC"), December 14, 2017
- [An AlphaZero inspired project](http://www.talkchess.com/forum/viewtopic.php?t=66013) by [Truls Edvard Stokke](index.php?title=Truls_Edvard_Stokke&action=edit&redlink=1 "Truls Edvard Stokke (page does not exist)"), [CCC](CCC "CCC"), December 14, 2017 » [ZeroFish](index.php?title=ZeroFish&action=edit&redlink=1 "ZeroFish (page does not exist)")
- [AlphaZero - Tactical Abilities](http://www.talkchess.com/forum/viewtopic.php?t=66026) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 16, 2017
- [In chess,AlphaZero outperformed Stockfish after just 4 hours](http://www.talkchess.com/forum/viewtopic.php?t=66047) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 18, 2017
- [AlphaZero - Youtube Videos](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=9653) by Christoph Fieberg, [CSS Forum](Computer_Chess_Forums "Computer Chess Forums"), December 18, 2017
- [AlphaZero Chess is not that strong ...](http://www.talkchess.com/forum/viewtopic.php?t=66062) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), December 19, 2017
- [David Silver (Deepmind) inaccuracies](http://www.talkchess.com/forum/viewtopic.php?t=66087) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 21, 2017
- [AZ vs SF - game 99](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32423) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2017
- [AlphaZero performance](http://www.talkchess.com/forum/viewtopic.php?t=66121) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), December 25, 2017
- [A Simple Alpha(Go) Zero Tutorial](http://www.talkchess.com/forum/viewtopic.php?t=66179) by Oliver Roese, [CCC](CCC "CCC"), December 30, 2017
- [AlphaZero: The 10 Top Shots](http://www.talkchess.com/forum/viewtopic.php?t=66184) by [Walter Eigenmann](index.php?title=Walter_Eigenmann&action=edit&redlink=1 "Walter Eigenmann (page does not exist)"), [CCC](CCC "CCC"), December 30, 2017

## 2018

- [SF was more seriously handicapped than I thought](http://www.talkchess.com/forum/viewtopic.php?t=66214) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 02, 2018
- [Chess World to Google Deep Mind..Prove You beat Stockfish 8!](http://www.talkchess.com/forum/viewtopic.php?t=66299) by AA Ross, [CCC](CCC "CCC"), January 11, 2018
- [Article:"How Alpha Zero Sees/Wins"](http://www.talkchess.com/forum/viewtopic.php?t=66349) by AA Ross, [CCC](CCC "CCC"), January 17, 2018  » [How AlphaZero Wins](AlphaZero#DanaMackenzie "AlphaZero")
- [Connect 4 AlphaZero implemented using Python...](http://www.talkchess.com/forum/viewtopic.php?t=66443) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 29, 2018 » [Connect Four](Connect_Four "Connect Four"), [Python](Python "Python")
- [Seeing Alphazero in perspective ...](http://www.talkchess.com/forum/viewtopic.php?t=66546) by Dan Ellwein, [CCC](CCC "CCC"), February 10, 2018
- [Matthew Sadler analysis of A0 vs SF \[Edit: A0 published in Science?\]](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69174) by trulses, [CCC](CCC "CCC"), December 06, 2018
- [Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175) by arunsoorya1309, [CCC](CCC "CCC"), December 06, 2018

[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=25) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=32) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=44) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=46) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=60) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=63) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=64) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=66) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=72) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=75) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 07, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=82) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=86) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018 » [Giraffe](Giraffe "Giraffe")
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=93) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 08, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=185) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), December 11, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=192) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 11, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=193) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 11, 2018 » [Stockfish Match](#Stockfish_Match)
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=209) by [Milos](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), December 11, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=211) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 11, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=213) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 11, 2018
[Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=232) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 12, 2018 » [Stockfish Match](#Stockfish_Match)

- [Policy training in Alpha Zero, LC0 ..](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69306) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), December 18, 2018 » [LC0](Leela_Chess_Zero#lc0 "Leela Chess Zero")

## 2019

- [A0 policy head ambiguity](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69668) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2019
- [AlphaZero No Castling Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72498) by Javier Ros, [CCC](CCC "CCC"), December 03, 2019

## 2020 ...

- [AlphaZero](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73772) by Pawel Wojcik, [CCC](CCC "CCC"), April 26, 2020
- [Chess variants made with help from alpha zero article](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75063) by jmartus, [CCC](CCC "CCC"), September 10, 2020

## Blog Posts

- [Lessons From Implementing AlphaZero](https://medium.com/oracledevs/lessons-from-implementing-alphazero-7e36e9054191) by [Aditya Prasad](https://medium.com/@akprasad), [Oracle Blog](https://blogs.oracle.com/), June 05, 2018

[Lessons from AlphaZero: Connect Four](https://medium.com/oracledevs/lessons-from-alphazero-connect-four-e4a0ae82af68) by [Aditya Prasad](https://medium.com/@akprasad), [Oracle Blog](https://blogs.oracle.com/), June 13, 2018
[Lessons from AlphaZero (part 3): Parameter Tweaking](https://medium.com/oracledevs/lessons-from-alphazero-part-3-parameter-tweaking-4dceb78ed1e5) by [Aditya Prasad](https://medium.com/@akprasad), [Oracle Blog](https://blogs.oracle.com/), June 20, 2018
[Lessons From AlphaZero (part 4): Improving the Training Target](https://medium.com/oracledevs/lessons-from-alphazero-part-4-improving-the-training-target-6efba2e71628) by [Vish Abrams](https://blogs.oracle.com/author/vish-abrams), [Oracle Blog](https://blogs.oracle.com/), June 27, 2018
[Lessons From Alpha Zero (part 5): Performance Optimization](https://medium.com/oracledevs/lessons-from-alpha-zero-part-5-performance-optimization-664b38dc509e) by [Anthony Young](https://blogs.oracle.com/author/anthony-young), [Oracle Blog](https://blogs.oracle.com/), July 03, 2018
[Lessons From Alpha Zero (part 6) — Hyperparameter Tuning](https://medium.com/oracledevs/lessons-from-alpha-zero-part-6-hyperparameter-tuning-b1cfcbe4ca9a) by [Anthony Young](https://blogs.oracle.com/author/anthony-young), [Oracle Blog](https://blogs.oracle.com/), July 11, 2018

- [AlphaZero: Shedding new light on the grand games of chess, shogi and Go](https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/) by [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") and [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), December 03, 2018
- [AlphaZero paper, and Lc0 v0.19.1](http://blog.lczero.org/2018/12/alphazero-paper-and-lc0-v0191.html) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), December 07, 2018

## External Links

- [AlphaZero from Wikipedia](https://en.wikipedia.org/wiki/AlphaZero)

- [AlphaGo Zero - AlphaZero from Wikipedia](https://en.wikipedia.org/wiki/AlphaGo_Zero#AlphaZero)

- Keynote [David Silver](David_Silver "David Silver") [NIPS 2017](https://nips.cc/Conferences/2017) [Deep Reinforcement Learning Symposium AlphaZero](https://youtu.be/A3ekFcZ3KNw), December 06, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video [[26]](#cite_note-26)

- [A Simple Alpha(Go) Zero Tutorial](http://web.stanford.edu/~surag/posts/alphazero.html) by [Surag Nair](index.php?title=Surag_Nair&action=edit&redlink=1 "Surag Nair (page does not exist)"), [Stanford University](Stanford_University "Stanford University"), December 29, 2017 [[27]](#cite_note-27)

[GitHub - suragnair/alpha-zero-general: A clean and simple implementation of a self-play learning algorithm based on AlphaGo Zero (any game, any framework!)](https://github.com/suragnair/alpha-zero-general)

- [AlphaZero: Shedding new light on the grand games of chess, shogi and Go](https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/) by [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") and [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), December 03, 2018
- AlphaZero: Shedding new light on the grand games of chess, shogi and Go, December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## OpenSpiel

- [GitHub - deepmind/open_spiel: OpenSpiel is a collection of environments and algorithms for research in general reinforcement learning and search/planning in games](https://github.com/deepmind/open_spiel) [[28]](#cite_note-28)
  - [open_spiel/open_spiel/algorithms at master · deepmind/open_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/algorithms)
    - [open_spiel/open_spiel/algorithms/alpha_zero at master · deepmind/open_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/algorithms/alpha_zero)
  - [open_spiel/open_spiel/games at master · deepmind/open_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/games)
    - [open_spiel/open_spiel/games/chess at master · deepmind/open_spiel · GitHub](https://github.com/deepmind/open_spiel/tree/master/open_spiel/games/chess)

## Reports

### 2017

- [DeepMind’s AI became a superhuman chess player in a few hours, just for fun](https://www.theverge.com/2017/12/6/16741106/deepmind-ai-chess-alphazero-shogi-go) by [James Vincent](https://www.theverge.com/users/James%20Vincent), [The Verge](https://en.wikipedia.org/wiki/The_Verge), December 06, 2017
- [Entire human chess knowledge learned and surpassed by DeepMind's AlphaZero in four hours](http://www.telegraph.co.uk/science/2017/12/06/entire-human-chess-knowledge-learned-surpassed-deepminds-alphazero/) by [Sarah Knapton](http://www.telegraph.co.uk/authors/sarah-knapton/), and [Leon Watson](http://www.telegraph.co.uk/authors/leon-watson/), [The Telegraph](https://en.wikipedia.org/wiki/Telegraph_Media_Group), December 06, 2017
- [Google's 'superhuman' DeepMind AI claims chess crown](http://www.bbc.co.uk/news/technology-42251535), [BBC News](https://en.wikipedia.org/wiki/BBC_News), December 06, 2017 [[29]](#cite_note-29)
- [DeepMind’s AlphaZero crushes chess](https://chess24.com/en/read/news/deepmind-s-alphazero-crushes-chess) by [Colin McGourty](https://chess24.com/en/profile/colin), [chess24](index.php?title=Chess24&action=edit&redlink=1 "Chess24 (page does not exist)"), December 06, 2017
- [One Small Step for Computers, One Giant Leap for Mankind](http://www.danamackenzie.com/blog/?p=5068) by [Dana Mackenzie](Dana_Mackenzie "Dana Mackenzie"), [Dana Blogs Chess](http://www.danamackenzie.com/blog/), December 06, 2017
- [Google's AlphaZero Destroys Stockfish In 100-Game Match](https://www.chess.com/news/view/google-s-alphazero-destroys-stockfish-in-100-game-match) by [Mike Klein](https://www.chess.com/member/mikeklein), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), December 06, 2017
- [The future is here – AlphaZero learns chess](https://en.chessbase.com/post/the-future-is-here-alphazero-learns-chess) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 06, 2017
- [AlphaZero: Reactions From Top GMs, Stockfish Author](https://www.chess.com/news/view/alphazero-reactions-from-top-gms-stockfish-author) by [Peter Doggers](Peter_Doggers "Peter Doggers"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), December 08, 2017 » [Stockfish](Stockfish "Stockfish"), [Tord Romstad](Tord_Romstad "Tord Romstad") [[30]](#cite_note-30)
- [Is AlphaZero really a scientific breakthrough in AI?](https://medium.com/@josecamachocollados/is-alphazero-really-a-scientific-breakthrough-in-ai-bf66ae1c84f2) by [Jose Camacho Collados](https://scholar.google.com/citations?user=NP4KdQQAAAAJ&hl=en), [Medium](https://medium.com/), December 11, 2017 [[31]](#cite_note-31)
- [Alpha Zero: Comparing "Orangutans and Apples"](https://en.chessbase.com/post/alpha-zero-comparing-orang-utans-and-apples) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [ChessBase News](ChessBase "ChessBase"), December 13, 2017
- [Kasparov on Deep Learning in chess](https://en.chessbase.com/post/kasparov-on-deep-learning-in-chess) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), December 13, 2017

### 2018 ...

- [AlphaZero really is that good](https://chess24.com/en/read/news/alphazero-really-is-that-good) by [Colin McGourty](http://michaelkonik.com/colin-mcgourty-chess-reporter/), [chess24](index.php?title=Chess24&action=edit&redlink=1 "Chess24 (page does not exist)"), December 06, 2018
- [Inside the (deep) mind of AlphaZero](https://en.chessbase.com/post/the-full-alphazero-paper-is-published-at-long-last) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 07, 2018
- [Standing on the shoulders of giants](https://en.chessbase.com/post/standing-on-the-shoulders-of-giants) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), September 18, 2019
- [Kramnik And AlphaZero: How To Rethink Chess‎](https://www.chess.com/article/view/no-castling-chess-kramnik-alphazero), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), December 02, 2019 [[32]](#cite_note-32)

## Stockfish Match

### Round 1

- [The chess games of AlphaZero (Computer)](http://www.chessgames.com/perl/chessplayer?pid=160016) from [chessgames.com](http://www.chessgames.com/index.html)
- [Cerebellum AlphaZero Analysis](http://www.zipproth.de/Brainfish/Cerebellum_AlphaZero.html) » [Cerebellum](index.php?title=Cerebellum&action=edit&redlink=1 "Cerebellum (page does not exist)") [[33]](#cite_note-33)
- [Deep Mind Alpha Zero's "Immortal Zugzwang Game" against Stockfish](https://youtu.be/lFXJWPhDsSY) by [Antonio Radic](https://www.facebook.com/AGADMATOR), December 07, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video [[34]](#cite_note-34) [[35]](#cite_note-35) » [Zugzwang](Zugzwang "Zugzwang")
- [Deep Mind AI Alpha Zero Dismantles Stockfish's French Defense](https://youtu.be/pcdpgn9OINs) by [Antonio Radic](https://www.facebook.com/AGADMATOR), December 08, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video
- [How AlphaZero Wins](http://www.danamackenzie.com/blog/?p=5072) by [Dana Mackenzie](Dana_Mackenzie "Dana Mackenzie"), [Dana Blogs Chess](http://www.danamackenzie.com/blog/), December 15, 2017 [[36]](#cite_note-36)

### Round 2, 3

- [AlphaZero vs. Stockfish](https://chess24.com/en/watch/live-tournaments/alphazero-vs-stockfish) from [chess24](index.php?title=Chess24&action=edit&redlink=1 "Chess24 (page does not exist)")

- [AlphaZero's Attacking Chess](https://youtu.be/nPexHaFL1uo) by [Anna Rudolf](https://en.wikipedia.org/wiki/Anna_Rudolf), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video [[37]](#cite_note-37)

- ["Exactly How to Attack" | DeepMind's AlphaZero vs. Stockfish](https://youtu.be/bo5plUo86BU) by [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- ["Bold Sir Lancelot" | DeepMind's AlphaZero vs. Stockfish](https://youtu.be/g0O3QmAhoeA) by [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- ["All-in Defence" | DeepMind's AlphaZero vs. Stockfish](https://youtu.be/2-wFUdvKTVQ) by [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- ["Long-term Sacrifice" | DeepMind's AlphaZero vs. Stockfish](https://youtu.be/JacRX6cKIaY) by [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- ["Endgame Class" | DeepMind's AlphaZero vs. Stockfish](https://youtu.be/jS26Ct34YrQ) by [Matthew Sadler](Matthew_Sadler "Matthew Sadler"), December 06, 2018, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## Misc

- [How to build your own AlphaZero AI using Python and Keras](https://medium.com/applied-data-science/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188) by [David Foster](https://www.linkedin.com/in/davidtfoster/), January 26, 2018 » [Connect Four](Connect_Four "Connect Four"), [Python](Python "Python") [[38]](#cite_note-38)
- [Can](Category:Can "Category:Can") - [Halleluwah](https://en.wikipedia.org/wiki/Halleluhwah), from [Tago Mago](https://en.wikipedia.org/wiki/Tago_Mago) 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Irmin Schmidt](https://en.wikipedia.org/wiki/Irmin_Schmidt), [Michael Karoli](https://en.wikipedia.org/wiki/Michael_Karoli), [Holger Czukay](https://en.wikipedia.org/wiki/Holger_Czukay), [Damo Suzuki](https://en.wikipedia.org/wiki/Damo_Suzuki), [Jaki Liebezeit](https://en.wikipedia.org/wiki/Jaki_Liebezeit)

## References

1. [↑](#cite_ref-1) "5th of December - The [Krampus](https://en.wikipedia.org/wiki/Krampus) has come", suggested by [Michael Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)") in [AlphaZero](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=9635) by Peter Martan, [CSS Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017, with further comments by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer")
1. [↑](#cite_ref-2) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
1. [↑](#cite_ref-3) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419
1. [↑](#cite_ref-4) [AlphaGo Zero: Learning from scratch](https://deepmind.com/blog/alphago-zero-learning-scratch/) by [Demis Hassabis](Demis_Hassabis "Demis Hassabis") and [David Silver](David_Silver "David Silver"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), October 18, 2017
1. [↑](#cite_ref-5) [Zero Manifesto](https://de.wikipedia.org/wiki/ZERO#Manifest) by [Günther Uecker](https://en.wikipedia.org/wiki/G%C3%BCnther_Uecker), [Heinz Mack](https://en.wikipedia.org/wiki/Heinz_Mack) and [Otto Piene](https://en.wikipedia.org/wiki/Otto_Piene) of the [ZERO](<https://en.wikipedia.org/wiki/Zero_(art)>) [Art group](https://en.wikipedia.org/wiki/Art_movement) 1963, Translation by [Google Translate](https://en.wikipedia.org/wiki/Google_Translate)\
   "Zero is silence. Zero is the beginning. Zero is round. Zero turns. Zero is the moon. The sun is zero. Zero is white. The desert zero. The sky over zero. The night -, Zero flows. The eye zero. Navel. Mouth. Kiss. The milk is round. The flower zero the bird. Silently. Pending. I eat Zero, I drink Zero, I sleep Zero, I watch Zero, I love Zero. Zero is beautiful, dynamo, dynamo, dynamo. The trees in spring, the snow, fire, water, sea. Red orange yellow green indigo blue violet zero zero rainbow. 4 3 2 1 Zero. Gold and silver, noise and smoke. Zero circus. Zero is silence. Zero is the beginning. Zero is round. Zero is zero. "\
   Zero the new Idealism
1. [↑](#cite_ref-6) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419, [Supplementary Materials](http://science.sciencemag.org/content/suppl/2018/12/05/362.6419.1140.DC1) - Architecture
1. [↑](#cite_ref-7) [Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=93) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 08, 2018
1. [↑](#cite_ref-8) The principle of residual nets is to add the input of the layer to the output of each layer. With this simple modification training is faster and enables deeper networks, see [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2017**). *[Residual Networks for Computer Go](http://ieeexplore.ieee.org/document/7875402/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. PP, No. 99, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/resnet.pdf)
1. [↑](#cite_ref-9) [Residual Networks for Computer Go](http://www.talkchess.com/forum/viewtopic.php?t=65923) by Brahim Hamadicharef, [CCC](CCC "CCC"), December 07, 2017
1. [↑](#cite_ref-10) [Re: AlphaZero is not like other chess programs](http://www.talkchess.com/forum/viewtopic.php?t=65937&start=10) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 09, 2017
1. [↑](#cite_ref-11) [First In-Depth Look at Google’s TPU Architecture](https://www.nextplatform.com/2017/04/05/first-depth-look-googles-tpu-architecture/) by [Nicole Hemsoth](https://www.nextplatform.com/author/nicole/), [The Next Platform](https://www.nextplatform.com/), April 05, 2017
1. [↑](#cite_ref-12) [Photo of Google Cloud TPU cluster](http://www.talkchess.com/forum/viewtopic.php?t=65945) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 09, 2017
1. [↑](#cite_ref-13) [First In-Depth Look at Google’s New Second-Generation TPU](https://www.nextplatform.com/2017/05/17/first-depth-look-googles-new-second-generation-tpu/) by [Nicole Hemsoth](https://www.nextplatform.com/author/nicole/), [The Next Platform](https://www.nextplatform.com/), May 17, 2017
1. [↑](#cite_ref-14) [Under The Hood Of Google’s TPU2 Machine Learning Clusters](https://www.nextplatform.com/2017/05/22/hood-googles-tpu2-machine-learning-clusters/) by Paul Teich, [The Next Platform](https://www.nextplatform.com/), May 22, 2017
1. [↑](#cite_ref-15) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
1. [↑](#cite_ref-16) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
1. [↑](#cite_ref-17) [Alpha Zero](http://www.open-chess.org/viewtopic.php?f=5&t=3153) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017
1. [↑](#cite_ref-18) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419
1. [↑](#cite_ref-19) [Supplementary Materials](http://science.sciencemag.org/content/suppl/2018/12/05/362.6419.1140.DC1)
1. [↑](#cite_ref-20) [Supplementary Materials](http://science.sciencemag.org/content/suppl/2018/12/05/362.6419.1140.DC1) S4
1. [↑](#cite_ref-21) ["Exact-Win Strategy for Overcoming AlphaZero" · Issue #799 · LeelaChessZero/lc0 · GitHub](https://github.com/LeelaChessZero/lc0/issues/799)
1. [↑](#cite_ref-22) [AlphaZero: Shedding new light on the grand games of chess, shogi and Go](https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/) by [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") and [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), December 03, 2018
1. [↑](#cite_ref-23) [open_spiel/contributing.md at master · deepmind/open_spiel · GitHub](https://github.com/deepmind/open_spiel/blob/master/docs/contributing.md)
1. [↑](#cite_ref-24) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021
1. [↑](#cite_ref-25) [Acquisition of Chess Knowledge in AlphaZero](https://en.chessbase.com/post/acquisition-of-chess-knowledge-in-alphazero), [ChessBase News](ChessBase "ChessBase"), November 18, 2021
1. [↑](#cite_ref-26) [AlphaZero explained by one creator](http://www.talkchess.com/forum/viewtopic.php?t=66059) by [Mario Carbonell Martinez](Mario_Carbonell_Martinez "Mario Carbonell Martinez"), [CCC](CCC "CCC"), December 19, 2017
1. [↑](#cite_ref-27) [A Simple Alpha(Go) Zero Tutorial](http://www.talkchess.com/forum/viewtopic.php?t=66179) by Oliver Roese, [CCC](CCC "CCC"), December 30, 2017
1. [↑](#cite_ref-28) [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Jean-Baptiste Lespiau](index.php?title=Jean-Baptiste_Lespiau&action=edit&redlink=1 "Jean-Baptiste Lespiau (page does not exist)"), [Vinícius Flores Zambaldi](index.php?title=Vin%C3%ADcius_Flores_Zambaldi&action=edit&redlink=1 "Vinícius Flores Zambaldi (page does not exist)"), [Satyaki Upadhyay](index.php?title=Satyaki_Upadhyay&action=edit&redlink=1 "Satyaki Upadhyay (page does not exist)"), [Julien Pérolat](index.php?title=Julien_P%C3%A9rolat&action=edit&redlink=1 "Julien Pérolat (page does not exist)"), [Sriram Srinivasan](index.php?title=Sriram_Srinivasan&action=edit&redlink=1 "Sriram Srinivasan (page does not exist)"), [Finbarr Timbers](index.php?title=Finbarr_Timbers&action=edit&redlink=1 "Finbarr Timbers (page does not exist)"), [Karl Tuyls](index.php?title=Karl_Tuyls&action=edit&redlink=1 "Karl Tuyls (page does not exist)"), [Shayegan Omidshafiei](index.php?title=Shayegan_Omidshafiei&action=edit&redlink=1 "Shayegan Omidshafiei (page does not exist)"), [Daniel Hennes](index.php?title=Daniel_Hennes&action=edit&redlink=1 "Daniel Hennes (page does not exist)"), [Dustin Morrill](index.php?title=Dustin_Morrill&action=edit&redlink=1 "Dustin Morrill (page does not exist)"), [Paul Muller](index.php?title=Paul_Muller&action=edit&redlink=1 "Paul Muller (page does not exist)"), [Timo Ewalds](index.php?title=Timo_Ewalds&action=edit&redlink=1 "Timo Ewalds (page does not exist)"), [Ryan Faulkner](index.php?title=Ryan_Faulkner&action=edit&redlink=1 "Ryan Faulkner (page does not exist)"), [János Kramár](index.php?title=J%C3%A1nos_Kram%C3%A1r&action=edit&redlink=1 "János Kramár (page does not exist)"), [Bart De Vylder](index.php?title=Bart_De_Vylder&action=edit&redlink=1 "Bart De Vylder (page does not exist)"), [Brennan Saeta](index.php?title=Brennan_Saeta&action=edit&redlink=1 "Brennan Saeta (page does not exist)"), [James Bradbury](index.php?title=James_Bradbury&action=edit&redlink=1 "James Bradbury (page does not exist)"), [David Ding](index.php?title=David_Ding&action=edit&redlink=1 "David Ding (page does not exist)"), [Sebastian Borgeaud](index.php?title=Sebastian_Borgeaud&action=edit&redlink=1 "Sebastian Borgeaud (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Thomas Anthony](index.php?title=Thomas_Anthony&action=edit&redlink=1 "Thomas Anthony (page does not exist)"), [Edward Hughes](index.php?title=Edward_Hughes&action=edit&redlink=1 "Edward Hughes (page does not exist)"), [Ivo Danihelka](index.php?title=Ivo_Danihelka&action=edit&redlink=1 "Ivo Danihelka (page does not exist)"), [Jonah Ryan-Davis](index.php?title=Jonah_Ryan-Davis&action=edit&redlink=1 "Jonah Ryan-Davis (page does not exist)") (**2019**). *OpenSpiel: A Framework for Reinforcement Learning in Games*. [arXiv:1908.09453](https://arxiv.org/abs/1908.09453)
1. [↑](#cite_ref-29) [BBC News; 'Google's ... DeepMind AI claims chess crown'](http://www.hiarcs.net/forums/viewtopic.php?t=8709) by pennine22, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2017
1. [↑](#cite_ref-30) [Reactions about AlphaZero from top GMs...](http://www.talkchess.com/forum/viewtopic.php?t=65934) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 08, 2017
1. [↑](#cite_ref-31) [recent article on alphazero ... 12/11/2017 ...](http://www.talkchess.com/forum/viewtopic.php?t=66005) by Dan Ellwein, [CCC](CCC "CCC"), December 14, 2017
1. [↑](#cite_ref-32) [AlphaZero No Castling Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72498) by Javier Ros, [CCC](CCC "CCC"), December 03, 2019
1. [↑](#cite_ref-33) [Cerebellum analysis of the AlphaZero - Stockfish Games](http://www.talkchess.com/forum/viewtopic.php?t=65983) by [Thomas Zipproth](index.php?title=Thomas_Zipproth&action=edit&redlink=1 "Thomas Zipproth (page does not exist)"), [CCC](CCC "CCC"), December 11, 2017
1. [↑](#cite_ref-34) [AlphaZero reinvents mobility and romanticism](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=32398) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 08, 2017
1. [↑](#cite_ref-35) [Immortal Zugzwang Game from Wikipedia](https://en.wikipedia.org/wiki/Immortal_Zugzwang_Game)
1. [↑](#cite_ref-36) [Article:"How Alpha Zero Sees/Wins"](http://www.talkchess.com/forum/viewtopic.php?t=66349) by AA Ross, [CCC](CCC "CCC"), January 17, 2018
1. [↑](#cite_ref-37) [Anna Rudolf analyzes a game of AlphaZero's](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69181) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), December 07, 2018
1. [↑](#cite_ref-38) [Connect 4 AlphaZero implemented using Python...](http://www.talkchess.com/forum/viewtopic.php?t=66443) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 29, 2018

**[Up one Level](Engines "Engines")**

