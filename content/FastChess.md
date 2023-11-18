---
title: FastChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * FastChess**

[](https://github.com/thomasahle/fastchess/blob/master/README.md#screenshot) FastChess Screen <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**FastChess**,

a didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), written in [Python](Python "Python"), licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").
FastChess predicts the next move by probing a one-layer [neural network](Neural_Networks "Neural Networks") [softmax](https://en.wikipedia.org/wiki/Softmax_function) model, using the [fastText](https://en.wikipedia.org/wiki/FastText) text classification library.
The model takes the board state as input, and outputs a vector of probabilities for each possible move. That simple linear model might further be combined with a [Monte-Carlo tree search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") along with the [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin") selection to improve the quality of play <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Training

FastChess' model is [trained](Supervised_Learning "Supervised Learning") by feeeding a set of [pgn files](Portable_Game_Notation "Portable Game Notation") to a special training procedure, creating the neural network weights in form of a *model.bin* file, which is later used to play chess <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Tuning

FastChess' [hyperparameters](<https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning)>) can be [tuned](Automated_Tuning "Automated Tuning") with [black box optimization](Automated_Tuning#Optimization "Automated Tuning") through [scikit optimize](https://en.wikipedia.org/wiki/Hyperparameter_optimization#Bayesian) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [ConvChess](ConvChess "ConvChess")
- [Sunfish](Sunfish "Sunfish")
- [PyChess](PyChess "PyChess")

## Forum Posts

- [Re: A question to MCTS + NN experts](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71301&start=8) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 04, 2019
- [New Tool for Tuning with Skopt](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71650) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 25, 2019 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Re: AlphaZero](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73772&start=15) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), May 05, 2020

## External Links

- [GitHub - thomasahle/fastchess: Predicts the best chess move with 27.5% accuracy by a single matrix multiplication](https://github.com/thomasahle/fastchess)
- [GitHub - thomasahle/noisy-bayesian-optimization: Bayesian Optimization for very Noisy functions](https://github.com/thomasahle/noisy-bayesian-optimization)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [fastchess/README.md at master · thomasahle/fastchess · GitHub - Screenshot](https://github.com/thomasahle/fastchess/blob/master/README.md#screenshot)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [fastchess/README.md at master · thomasahle/fastchess · GitHub - Teaching FastText to play Chess](https://github.com/thomasahle/fastchess/blob/master/README.md#teaching-fasttext-to-play-chess)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [fastchess/README.md at master · thomasahle/fastchess · GitHub - Train the model](https://github.com/thomasahle/fastchess/blob/master/README.md#train-the-model)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [New Tool for Tuning with Skopt](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71650) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 25, 2019
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [skopt API documentation](https://scikit-optimize.github.io/)

**[Up one level](Engines "Engines")**

