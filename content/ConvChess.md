---
title: ConvChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * ConvChess**

\[ Convolutional Layer Animation <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**ConvChess**,

a didactic [convolutional neural network](Neural_Networks#Convolutional "Neural Networks") (CNN) chess playing entity designed and implemented by [Barak Oshri](Barak_Oshri "Barak Oshri") and [Nishith Khandwala](Nishith_Khandwala "Nishith Khandwala") during their 2015 project work at [Stanford University](Stanford_University "Stanford University") [[2]](#cite-note-paper-2).
ConvChess was likely the first chess playing entity using a CNN, as mentioned by [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli") et al. <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
ConvChess is implemented in [Python](Python "Python"), using the [python-chess](Python-chess "Python-chess") and [NumPy](https://en.wikipedia.org/wiki/NumPy) libraries, source code and datasets available on [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Idea

Inspired by the [supervised learning](Supervised_Learning "Supervised Learning") approach of [Christopher Clark](Christopher_Clark "Christopher Clark") and [Amos Storkey](Amos_Storkey "Amos Storkey") to predict moves in [Go](Go "Go") without any [search](Search "Search"),
to defeat the traditional search program [Gnu Go](index.php?title=Gnu_Go&action=edit&redlink=1 "Gnu Go (page does not exist)") in 86% of the games <a id="cite-note-5" href="#cite-ref-5">[5]</a>,
Oshri and Khandwala tried a similar idea to implement a move predictor or policy network in Chess. They were well aware that such winning rates without search as reported in Go are not possible in Chess, first due to the tactical nature of the game,
and also due to move classification aspect that [chess moves](Moves "Moves") require [origin square](Origin_Square "Origin Square") and [target square](Target_Square "Target Square"), instead of a single coordinate for a 19x19 grid to drop a stone.
Therefore in this novel approach, the classification was divided into two parts. The first part trains a piece-selector CNN to predict the origin square a piece moves from,
while the second part trains six move-selector CNNs to encode which target squares would be advantageous for each of the six possible [piece types](Pieces#PieceTypeCoding "Pieces").
These seven CNNs take the [board representation](Board_Representation "Board Representation") as input and output a probability distribution for 64 origin and 6x64 target squares.
The predicted move is then obtained by composing the piece-selector CNN by multiplying its values by the highest value in the corresponding move-selector CNN,
clipping all illegal origins and targets to zero, and taking the [arg max](https://en.wikipedia.org/wiki/Arg_max) over the entire composition.
Since the model considers White to move only, Black to move positions require a [color flip](Color_Flipping "Color Flipping").

## Network

Each of the seven CNNs consists of three [convolutional layers](https://en.wikipedia.org/wiki/Convolutional_neural_network#Convolutional_layer) with 32 3x3 filters stride 1, including [ReLU](<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>) and 2x2 [pooling layer](https://en.wikipedia.org/wiki/Convolutional_neural_network#Pooling_layer) stride 2 (The authors reported less success using five convolution layers <a id="cite-note-6" href="#cite-ref-6">[6]</a>)
followed by two [fully connected layers](<https://en.wikipedia.org/wiki/Layer_(deep_learning)#Dense_layer>) with a [affine transformation](https://en.wikipedia.org/wiki/Affine_transformation)to 128 features, the first including ReLU and [Dropout](<https://en.wikipedia.org/wiki/Dilution_(neural_networks)>), the second [Softmax](https://en.wikipedia.org/wiki/Softmax_function).
The input layer, feeding in the [board representation](Board_Representation "Board Representation") ignoring [en passant](En_passant "En passant") square and [castling rights](Castling_Rights "Castling Rights"), has a shape of six channels for each piece type with three possible values for each of the 8x8 squares, -1 for Black pieces, 0 for empty square, and +1 for White pieces.
The output, reflecting the number of classifications, is a vector of 64 [floats](Float "Float").

## Training

The networks were trained for 245,000 moves over 20,000 games <a id="cite-note-7" href="#cite-ref-7">[7]</a>,
with the piece-selector CNN trained on every piece and each move-selector CNN trained on every move made by the respective piece, without considering the outcome of the game.
Their best model was found by doing a [grid-search](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Grid_search) over the parameters of [learning rate](https://en.wikipedia.org/wiki/Learning_rate), [regularization](<https://en.wikipedia.org/wiki/Regularization_(mathematics)>), and weight initialization with fine tuning afterwards.
The parameters of the best model were a regularization of 0.0001, learning rate of 0.0015, [batch size](https://en.wikipedia.org/wiki/Batch_normalization) of 250, a [learning rate decay](https://en.wikipedia.org/wiki/Learning_rate#Learning_rate_schedule) of 0.999 on [RMSprop](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#RMSProp) with no [dropout](<https://en.wikipedia.org/wiki/Dilution_(neural_networks)>) trained in 15 [epochs](<https://en.wikipedia.org/wiki/Epoch_(disambiguation)#Science_and_technology>) [[2]](#cite-note-paper-2).

## Results

The best result obtained with the piece-selector CNN was 38.30%. The results for the move-selector varied. Pieces with local movements (P=52%, N=56%, K=47%) performed significantly better than [sliding pieces](Sliding_Pieces "Sliding Pieces") (B=40%, R=30%, Q=27%) - the latter with more options to fail, and possibly also due to the restricted influence of only three 3x3 convolutions.
ConvChess was played against [Sunfish](Sunfish "Sunfish") (search depth not reported) in 100 games. 26 of the games drew and the rest were lost [[2]](#cite-note-paper-2).

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [FastChess](FastChess "FastChess")
- [Sunfish](Sunfish "Sunfish")

## Publications

- [Barak Oshri](Barak_Oshri "Barak Oshri"), [Nishith Khandwala](Nishith_Khandwala "Nishith Khandwala") (**2015**). *Predicting Moves in Chess using Convolutional Neural Networks*. [pdf](http://vision.stanford.edu/teaching/cs231n/reports/2015/pdfs/ConvChess.pdf)

## Forum Posts

- [ConvChess CNN](http://www.talkchess.com/forum3/viewtopic.php?t=63458) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), March 15, 2017

## [Re: ConvChess CNN](http://www.talkchess.com/forum3/viewtopic.php?t=63458&start=1) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), March 15, 2017 External Links

- [GitHub - BarakOshri/ConvChess: Predicting Moves in Chess Using Convolutional Neural Networks](https://github.com/BarakOshri/ConvChess)
- [Convolutional neural network from Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [2D Image-Kernel Convolution Animation](https://commons.wikimedia.org/wiki/File:2D_Convolution_Animation.gif) by Michael Plotke, January 28, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. ↑ [2.0](#cite-ref-paper-2-0) [2.1](#cite-ref-paper-2-1) [2.2](#cite-ref-paper-2-2) [Barak Oshri](Barak_Oshri "Barak Oshri"), [Nishith Khandwala](Nishith_Khandwala "Nishith Khandwala") (**2015**). *Predicting Moves in Chess using Convolutional Neural Networks*. [pdf](http://vision.stanford.edu/teaching/cs231n/reports/2015/pdfs/ConvChess.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli"), [Francesco Bidoia](Francesco_Bidoia "Francesco Bidoia"), [Valeriu Codreanu](Valeriu_Codreanu "Valeriu Codreanu"), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2018**). *Learning to Evaluate Chess Positions with Deep Neural Networks and Limited Lookahead*. ICPRAM 2018, [pdf](https://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/ICPRAM_CHESS_DNN_2018.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [GitHub - BarakOshri/ConvChess: Predicting Moves in Chess Using Convolutional Neural Networks](https://github.com/BarakOshri/ConvChess)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Christopher Clark](Christopher_Clark "Christopher Clark"), [Amos Storkey](Amos_Storkey "Amos Storkey") (**2014**). *Teaching Deep Convolutional Neural Networks to Play Go*. [arXiv:1412.3409](http://arxiv.org/abs/1412.3409)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: ConvChess CNN](http://www.talkchess.com/forum3/viewtopic.php?t=63458&start=1) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), March 15, 2017
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [ConvChess/master/data/FICS_2000.pgn](https://raw.githubusercontent.com/BarakOshri/ConvChess/master/data/FICS_2000.pgn)

**[Up one Level](Engines "Engines")**

