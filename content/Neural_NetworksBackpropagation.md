---
title: Neural NetworksBackpropagation
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* Neural Networks**



[ Artificial Neural Network [[1]](#cite_note-1)
**Neural Networks**,  

a series of connected [neurons](https://en.wikipedia.org/wiki/Neuron) which communicate due to [neurotransmission](https://en.wikipedia.org/wiki/Neurotransmitter). The interface through which neurons interact with their neighbors consists of [axon terminals](https://en.wikipedia.org/wiki/Axon_terminal) connected via [synapses](https://en.wikipedia.org/wiki/Synapse) to [dendrites](https://en.wikipedia.org/wiki/Dendrite) on other neurons. If the sum of the input signals into one neuron surpasses a certain threshold, the neuron sends an [action potential](https://en.wikipedia.org/wiki/Action_potential) at the [axon hillock](https://en.wikipedia.org/wiki/Axon_hillock) and transmits this electrical signal along the [axon](https://en.wikipedia.org/wiki/Axon). 


In 1949, [Donald O. Hebb](https://en.wikipedia.org/wiki/Donald_O._Hebb) introduced his [theory](https://en.wikipedia.org/wiki/Hebbian_theory) in *[The Organization of Behavior](https://en.wikipedia.org/wiki/The_Organization_of_Behavior)*, stating that [learning](Learning "Learning") is about to adapt weight vectors (persistent [synaptic plasticity](https://en.wikipedia.org/wiki/Synaptic_plasticity)) of the neuron pre-synaptic inputs, whose dot-product activates or controls the post-synaptic output, which is the base of Neural network learning [[2]](#cite_note-2). 



### Contents


* [1 AN](#AN)
* [2 ANNs](#ANNs)
	+ [2.1 Perceptron](#Perceptron)
	+ [2.2 AI Winter](#AI_Winter)
	+ [2.3 Backpropagation](#Backpropagation)
	+ [2.4 Deep Learning](#Deep_Learning)
	+ [2.5 Convolutional NNs](#Convolutional_NNs)
	+ [2.6 Residual Net](#Residual_Net)
* [3 ANNs in Games](#ANNs_in_Games)
	+ [3.1 Backgammon](#Backgammon)
	+ [3.2 Go](#Go)
	+ [3.3 Chess](#Chess)
		- [3.3.1 Move Ordering](#Move_Ordering)
		- [3.3.2 Giraffe & Zurichess](#Giraffe_.26_Zurichess)
		- [3.3.3 DeepChess](#DeepChess)
		- [3.3.4 Alpha Zero](#Alpha_Zero)
		- [3.3.5 NNUE](#NNUE)
		- [3.3.6 NN Chess Programs](#NN_Chess_Programs)
* [4 See also](#See_also)
* [5 Selected Publications](#Selected_Publications)
	+ [5.1 1940 ...](#1940_...)
	+ [5.2 1950 ...](#1950_...)
	+ [5.3 1960 ...](#1960_...)
	+ [5.4 1970 ...](#1970_...)
	+ [5.5 1980 ...](#1980_...)
	+ [5.6 1990 ...](#1990_...)
	+ [5.7 2000 ...](#2000_...)
	+ [5.8 2010 ...](#2010_...)
	+ [5.9 2020 ...](#2020_...)
* [6 Blog & Forum Posts](#Blog_.26_Forum_Posts)
	+ [6.1 1996 ...](#1996_...)
	+ [6.2 2000 ...](#2000_..._2)
	+ [6.3 2005 ...](#2005_...)
	+ [6.4 2010 ...](#2010_..._2)
	+ [6.5 2015 ...](#2015_...)
	+ [6.6 2020 ...](#2020_..._2)
* [7 External Links](#External_Links)
	+ [7.1 ANNs](#ANNs_2)
		- [7.1.1 Topics](#Topics)
		- [7.1.2 Perceptron](#Perceptron_2)
		- [7.1.3 CNNs](#CNNs)
		- [7.1.4 ResNet](#ResNet)
		- [7.1.5 RNNs](#RNNs)
	+ [7.2 Activation Functions](#Activation_Functions)
	+ [7.3 Backpropagation](#Backpropagation_2)
	+ [7.4 Gradient](#Gradient)
	+ [7.5 Software](#Software)
	+ [7.6 Libraries](#Libraries)
	+ [7.7 Blogs](#Blogs)
	+ [7.8 Courses](#Courses)
* [8 References](#References)






Already in the early 40s, [Warren S. McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch) and [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts) introduced the [artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron) as a logical element with multiple analogue inputs and a single digital output with a boolean result. The output fired "true", if the sum of the inputs exceed a threshold. In their 1943 paper *A Logical Calculus of the Ideas Immanent in Nervous Activity* [[3]](#cite_note-3), they attempted to demonstrate that a [Turing machine](Alan_Turing#TuringMachine "Alan Turing") program could be implemented in a finite network of such neurons of [combinatorial logic](Combinatorial_Logic "Combinatorial Logic") functions of [AND](Combinatorial_Logic#AND "Combinatorial Logic"), [OR](Combinatorial_Logic#OR "Combinatorial Logic") and [NOT](Combinatorial_Logic#NOT "Combinatorial Logic"). 



## ANNs


[Artificial Neural Networks](https://en.wikipedia.org/wiki/Artificial_neural_network) (**ANNs**) are a family of [statistical learning](https://en.wikipedia.org/wiki/Machine_learning) devices or algorithms used in [regression](https://en.wikipedia.org/wiki/Regression_analysis), and [binary](https://en.wikipedia.org/wiki/Binary_classification) or [multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification), implemented in [hardware](Hardware "Hardware") or [software](Software "Software") inspired by their biological counterparts. The [artificial neurons](https://en.wikipedia.org/wiki/Artificial_neuron) of one or more layers receive one or more inputs (representing dendrites), and after being weighted, sum them to produce an output (representing a neuron's axon). The sum is passed through a [nonlinear](https://en.wikipedia.org/wiki/Nonlinear_system) function known as an [activation function](https://en.wikipedia.org/wiki/Activation_function) or transfer function. The transfer functions usually have a [sigmoid shape](https://en.wikipedia.org/wiki/Sigmoid_function), but they may also take the form of other non-linear functions, [piecewise](https://en.wikipedia.org/wiki/Piecewise) linear functions, or [step functions](https://en.wikipedia.org/wiki/Artificial_neuron#Step_function) [[4]](#cite_note-4). The weights of the inputs of each layer are tuned to minimize a [cost or loss function](https://en.wikipedia.org/wiki/Loss_function), which is a task in [mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization) and machine learning.



### Perceptron


[ Perceptron [[5]](#cite_note-5)
The [perceptron](https://en.wikipedia.org/wiki/Perceptron) is an algorithm for [supervised learning](Supervised_Learning "Supervised Learning") of [binary classifiers](https://en.wikipedia.org/wiki/Binary_classification). It was the first artificial neural network, introduced in 1957 by [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) [[6]](#cite_note-6), implemented in custom hardware. In its basic form it consists of a single neuron with multiple inputs and associated weights.


[Supervised learning](Supervised_Learning "Supervised Learning") is applied using a set D of labeled [training data](https://en.wikipedia.org/wiki/Test_set) with pairs of [feature vectors](https://en.wikipedia.org/wiki/Feature_vector) (x) and given results as desired output (d), usually started with cleared or randomly initialized weight vector w. The output is calculated by all inputs of a sample, multiplied by its corresponding weights, passing the sum to the activation function f. The difference of desired and actual value is then immediately used modify the weights for all features using a learning rate 0.0 < α <= 1.0:




```C++

   for (j=0, Σ = 0.0; j < nSamples; ++j) {
    for (i=0, X = bias; i < nFeatures; ++i) 
      X += w[i]*x[j][i];
    y = f ( X );
    Σ += abs(Δ = d[j] - y);
    for (i=0; i < nFeatures; ++i) 
      w[i] += α*Δ*x[j][i];
   }

```





### AI Winter


[ Three layer, XOR capable Perceptron [[7]](#cite_note-7)
Although the perceptron initially seemed promising, it was proved that perceptrons could not be trained to recognise many classes of patterns. This led to neural network research stagnating for many years, the [AI-winter](https://en.wikipedia.org/wiki/AI_winter#The_abandonment_of_connectionism_in_1969), before it was recognised that a [feedforward neural network](https://en.wikipedia.org/wiki/Feedforward_neural_network) with two or more layers had far greater processing power than with one layer. Single layer perceptrons are only capable of learning [linearly separable](https://en.wikipedia.org/wiki/Linear_separability) patterns. In their 1969 book *[Perceptrons](https://en.wikipedia.org/wiki/Perceptrons_%28book%29)*, [Marvin Minsky](Marvin_Minsky "Marvin Minsky") and [Seymour Papert](Mathematician#SPapert "Mathematician") wrote that it was impossible for these classes of network to learn the [XOR function](Combinatorial_Logic#XOR "Combinatorial Logic"). It is often believed that they also conjectured (incorrectly) that a similar result would hold for a [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) [[8]](#cite_note-8). However, this is not true, as both Minsky and Papert already knew that multilayer perceptrons were capable of producing an XOR function [[9]](#cite_note-9)- 



### Backpropagation


In 1974, [Paul Werbos](Mathematician#PWerbos "Mathematician") started to end the AI winter concerning neural networks, when he first described the mathematical process of training [multilayer perceptrons](https://en.wikipedia.org/wiki/Multilayer_perceptron) through [backpropagation](https://en.wikipedia.org/wiki/Backpropagation) of errors [[10]](#cite_note-10), derived in the context of [control theory](https://en.wikipedia.org/wiki/Control_theory) by [Henry J. Kelley](https://en.wikipedia.org/wiki/Henry_J._Kelley) in 1960 [[11]](#cite_note-11) and by [Arthur E. Bryson](https://en.wikipedia.org/wiki/Arthur_E._Bryson) in 1961 [[12]](#cite_note-12) using principles of [dynamic programming](Dynamic_Programming "Dynamic Programming"), simplified by [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") in 1961 applying the [chain rule](https://en.wikipedia.org/wiki/Chain_rule) [[13]](#cite_note-13). It was in 1982, when Werbos applied a [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation) method described in 1970 by [Seppo Linnainmaa](Mathematician#SLinnainmaa "Mathematician") [[14]](#cite_note-14) to neural networks in the way that is widely used today [[15]](#cite_note-15) [[16]](#cite_note-16) [[17]](#cite_note-17) [[18]](#cite_note-18). 


Backpropagation is a generalization of the [delta](https://en.wikipedia.org/wiki/Delta_rule) rule to multilayered [feedforward networks](https://en.wikipedia.org/wiki/Feedforward_neural_network), made possible by using the [chain rule](https://en.wikipedia.org/wiki/Chain_rule) to iteratively compute [gradients](https://en.wikipedia.org/wiki/Gradient) for each layer. Backpropagation requires that the [activation function](https://en.wikipedia.org/wiki/Activation_function) used by the artificial neurons be [differentiable](https://en.wikipedia.org/wiki/Differentiable_function), which is true for the common [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) [logistic function](https://en.wikipedia.org/wiki/Logistic_function) or its [softmax](https://en.wikipedia.org/wiki/Softmax_function) generalization in [multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification). 


Along with an [optimization method](https://en.wikipedia.org/wiki/Mathematical_optimization) such as [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent), it calculates the gradient of a [cost or loss function](https://en.wikipedia.org/wiki/Loss_function) with respect to all the weights in the neural network. The gradient is fed to the optimization method which in turn uses it to update the weights, in an attempt to minimize the loss function, which choice depends on the learning type (supervised, unsupervised, reinforcement) and the activation function - [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) or [cross-entropy error function](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression) are used in [binary classification](https://en.wikipedia.org/wiki/Binary_classification) [[19]](#cite_note-19). The gradient is almost always used in a simple [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) algorithm. In 1983, [Yurii Nesterov](Mathematician#YNesterov "Mathematician") contributed an accelerated version of gradient descent that converges considerably faster than ordinary gradient descent [[20]](#cite_note-20) [[21]](#cite_note-21) [[22]](#cite_note-22) [[23]](#cite_note-23).


Backpropagation algorithm for a 3-layer network [[24]](#cite_note-24):




```C++

   initialize the weights in the network (often small random values)
   do
      for each example e in the training set
         O = neural-net-output(network, e)  // forward pass
         T = teacher output for e
         compute error (T - O) at the output units
         compute delta_wh for all weights from hidden layer to output layer  // backward pass
         compute delta_wi for all weights from input layer to hidden layer   // backward pass continued
         update the weights in the network
   until all examples classified correctly or stopping criterion satisfied
   return the network

```





### Deep Learning


[Deep learning](Deep_Learning "Deep Learning") has been characterized as a [buzzword](https://en.wikipedia.org/wiki/Buzzword), or a rebranding of neural networks. A [deep neural network](https://en.wikipedia.org/wiki/Deep_learning#Deep_neural_networks) (DNN) is an ANN with multiple hidden layers of units between the input and output layers which can be [discriminatively](https://en.wikipedia.org/wiki/Discriminative_model) trained with the standard backpropagation algorithm. Two common issues if naively trained are [overfitting](https://en.wikipedia.org/wiki/Overfitting) and computation time.




### Convolutional NNs


[Convolutional neural networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNN) form a subclass of feedforward neural networks that have special weight constraints, individual neurons are tiled in such a way that they respond to overlapping regions. A neuron of a convolutional layer is connected to a correspondent [receptive field](https://en.wikipedia.org/wiki/Receptive_field) of the previous layer, a small subset of their neurons. A distinguishing feature of CNNs is that many neurons share the same bias and vector of weights, dubbed filter. This reduces [memory footprint](Memory#Footprint "Memory") because a single bias and a single vector of weights is used across all receptive fields sharing that filter, rather than each receptive field having its own bias and vector of weights. Convolutional NNs are suited for deep learning and are highly suitable for parallelization on [GPUs](GPU "GPU") [[25]](#cite_note-25). They were [research topic](Go#CNN "Go") in the game of [Go](Go "Go") since 2008 [[26]](#cite_note-26), and along with the [residual](Neural_Networks#Residual "Neural Networks") modification successful applied in [Go](Go "Go") and other [games](Games "Games"), most spectacular due to [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") in 2015 and [AlphaZero](AlphaZero "AlphaZero") in 2017.



[![Typical cnn.png](https://upload.wikimedia.org/wikipedia/commons/6/63/Typical_cnn.png)](https://commons.wikimedia.org/wiki/File:Typical_cnn.png)
Typical CNN [[27]](#cite_note-27)




### Residual Net


 [](https://arxiv.org/abs/1512.03385) A residual block [[28]](#cite_note-28) [[29]](#cite_note-29) 
 A **Residual net** (ResNet) adds the input of a layer, typically composed of a convolutional layer and of a [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) layer, to its output. This modification, like convolutional nets inspired from image classification, enables faster training and deeper networks [[30]](#cite_note-30) [[31]](#cite_note-31) [[32]](#cite_note-32). 



## ANNs in Games


Applications of neural networks in computer games and chess are [learning](Learning "Learning") of [evaluation](Evaluation "Evaluation") and [search](Search "Search") control. Evaluation topics include [feature selection](https://en.wikipedia.org/wiki/Feature_selection) and [automated tuning](Automated_Tuning "Automated Tuning"), search control [move ordering](Move_Ordering "Move Ordering"), [selectivity](Selectivity "Selectivity") and [time management](Time_Management "Time Management"). The [perceptron](Neural_Networks#Perceptron "Neural Networks") looks like the ideal learning algorithm for [automated evaluation tuning](Automated_Tuning "Automated Tuning"). 



### Backgammon


In the late 80s, [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") pioneered in applying ANNs to the game of [Backgammon](Backgammon "Backgammon"). His program [Neurogammon](https://en.wikipedia.org/wiki/Neurogammon) won the Gold medal at the [1st Computer Olympiad](1st_Computer_Olympiad "1st Computer Olympiad") 1989 - and was further improved by *TD-Lambda* based [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning") within [TD-Gammon](https://en.wikipedia.org/wiki/TD-Gammon) [[33]](#cite_note-33). Today all strong backgammon programs rely on heavily trained neural networks.



Go
--


In 2014, two teams independently investigated whether deep [convolutional neural networks](Neural_Networks#Convolutional "Neural Networks") could be used to directly represent and [learn](Learning "Learning") a move evaluation function for the game of [Go](Go "Go"). [Christopher Clark](Christopher_Clark "Christopher Clark") and [Amos Storkey](Amos_Storkey "Amos Storkey") trained an 8-layer convolutional neural network by [supervised learning](Supervised_Learning "Supervised Learning") from a database of human professional games, which without any [search](Search "Search"), defeated the traditional search program [Gnu Go](index.php?title=Gnu_Go&action=edit&redlink=1 "Gnu Go (page does not exist)") in 86% of the games [[34]](#cite_note-34) [[35]](#cite_note-35) [[36]](#cite_note-36) [[37]](#cite_note-37). In their paper *Move Evaluation in Go Using Deep Convolutional Neural Networks* [[38]](#cite_note-38), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), and [David Silver](David_Silver "David Silver") report they trained a large 12-layer convolutional neural network in a similar way, to beat Gnu Go in 97% of the games, and matched the performance of a state-of-the-art [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") that simulates a million positions per move [[39]](#cite_note-39). 


In 2015, a team affiliated with [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") around [David Silver](David_Silver "David Silver") and [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), supported by [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") researchers [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)") and [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), build a Go playing program dubbed [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)") [[40]](#cite_note-40), combining Monte-Carlo tree search with their 12-layer networks [[41]](#cite_note-41).



### Chess


[Logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") as applied in [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") may be interpreted as [supervised learning](Supervised_Learning "Supervised Learning") application of the single-layer perceptron with one neuron. This is also true for [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") approaches, such as [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") in [KnightCap](KnightCap "KnightCap") or [Meep's](Meep "Meep") [TreeStrap](Meep#TreeStrap "Meep"), where the evaluation consists of a weighted linear combination of features. Despite these similarities with the perceptron, these engines are not considered using ANNs - since they use manually selected chess specific feature construction concepts like [material](Material "Material"), [piece square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility") etc..


More sophisticated attempts to replace static evaluation by neural networks and perceptrons feeding in more unaffiliated feature sets like [board representation](Board_Representation "Board Representation") and [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") etc., where not yet that successful like in other games. Chess evaluation seems not that well suited for neural nets, but there are also aspects of too weak models and feature recognizers as addressed by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") with [Stoofvlees](Stoofvlees "Stoofvlees") [[42]](#cite_note-42), huge training effort, and weak [floating point](Float "Float") performance - but there is still hope due to progress in hardware and parallelization using [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") and [GPUs](GPU "GPU"), and deeper and more powerful neural network structures and methods successful in other domains. In December 2017, [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") published about their generalized [AlphaZero](Neural_Networks#AlphaZero "Neural Networks") algorithm.



### Move Ordering


Concerning [move ordering](Move_Ordering "Move Ordering") - there were interesting NN proposals like the [Chessmaps Heuristic](Chessmaps_Heuristic "Chessmaps Heuristic") by [Kieran Greer](Kieran_Greer "Kieran Greer") et al. [[43]](#cite_note-43), and the [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic") by [Levente Kocsis](Levente_Kocsis "Levente Kocsis") et al. [[44]](#cite_note-44). 



### Giraffe & Zurichess


In 2015, [Matthew Lai](Matthew_Lai "Matthew Lai") trained [Giraffe's](Giraffe "Giraffe") [deep neural network](Neural_Networks#Deep "Neural Networks") by [TD-Leaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") [[45]](#cite_note-45). [Zurichess](Zurichess "Zurichess") by [Alexandru Moșoi](Alexandru_Mosoi "Alexandru Mosoi") uses the [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) library for [automated tuning](Automated_Tuning "Automated Tuning") - in a two layers neural network, the second layer is responsible for a [tapered eval](Tapered_Eval "Tapered Eval") to phase [endgame](Endgame "Endgame") and [middlegame](Middlegame "Middlegame") [scores](Score "Score") [[46]](#cite_note-46).



### DeepChess


In 2016, [Omid E. David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu"), and [Lior Wolf](index.php?title=Lior_Wolf&action=edit&redlink=1 "Lior Wolf (page does not exist)") introduced [DeepChess](index.php?title=DeepChess&action=edit&redlink=1 "DeepChess (page does not exist)") obtaining a grandmaster-level chess playing performance using a learning method incorporating two deep neural networks, which are trained using a combination of unsupervised pretraining and supervised training. The unsupervised training extracts high level features from a given [chess position](Chess_Position "Chess Position"), and the supervised training learns to compare two chess positions to select the more favorable one. In order to use DeepChess inside a chess program, a novel version of [alpha-beta](Alpha-Beta "Alpha-Beta") is used that does not require [bounds](Bound "Bound") but positions αpos and βpos [[47]](#cite_note-47).




### Alpha Zero


In December 2017, the [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") team along with former [Giraffe](Giraffe "Giraffe") author [Matthew Lai](Matthew_Lai "Matthew Lai") reported on their generalized [AlphaZero](AlphaZero "AlphaZero") algorithm, combining [Deep learning](Deep_Learning "Deep Learning") with [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"). AlphaZero can achieve, tabula rasa, superhuman performance in many challenging domains with some training effort. Starting from random play, and given no domain knowledge except the game rules, AlphaZero achieved a superhuman level of play in the games of chess and [Shogi](Shogi "Shogi") as well as Go, and convincingly defeated a world-champion program in each case [[48]](#cite_note-48). The open souece projects [Leela Zero](index.php?title=Leela_Zero&action=edit&redlink=1 "Leela Zero (page does not exist)") (Go) and its chess adaptation [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") successfully re-implemented the ideas of DeepMind.



### NNUE


[NNUE](NNUE "NNUE") reverse of ƎUИИ - Efficiently Updatable Neural Networks, is an NN architecture intended to replace the [evaluation](Evaluation "Evaluation") of [Shogi](Shogi "Shogi"), [chess](Chess "Chess") and other board game playing [alpha-beta](Alpha-Beta "Alpha-Beta") searchers. NNUE was introduced in 2018 by [Yu Nasu](Yu_Nasu "Yu Nasu") [[49]](#cite_note-49),
and was used in Shogi adaptations of [Stockfish](Stockfish "Stockfish") such as [YaneuraOu](YaneuraOu "YaneuraOu") [[50]](#cite_note-50) ,
and [Kristallweizen](Kristallweizen "Kristallweizen") [[51]](#cite_note-51), apparently with [AlphaZero](AlphaZero "AlphaZero") strength [[52]](#cite_note-52). [Nodchip](Hisayori_Noda "Hisayori Noda") incorporated NNUE into the chess playing Stockfish 10 as a proof of concept [[53]](#cite_note-53), yielding in the hype about [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") in summer 2020 [[54]](#cite_note-54).
Its heavily over parametrized computational most expensive input layer is efficiently [incremental updated](Incremental_Updates "Incremental Updates") in [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move").




### NN Chess Programs


* [Category:NN](Category:NN "Category:NN")


## See also


* [Analog Evaluation](Analog_Evaluation "Analog Evaluation")
* [Backgammon](Backgammon "Backgammon")
* [Chessmaps Heuristic](Chessmaps_Heuristic "Chessmaps Heuristic")
* [Convolutional Neural Networks in Go](Go#CNN "Go")


 [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
 [Keynote Lecture CG 2016 Conference](CG_2016#Keynote "CG 2016") by [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang")
* [Cognition](Cognition "Cognition")
* [Deep Learning](Deep_Learning "Deep Learning")
* [DeepChess](index.php?title=DeepChess&action=edit&redlink=1 "DeepChess (page does not exist)")
* [Genetic Programming](Genetic_Programming "Genetic Programming")
* [Memory](Memory "Memory")
* [Neural MoveMap Heuristic](Neural_MoveMap_Heuristic "Neural MoveMap Heuristic")
* [NNUE](NNUE "NNUE")
* [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
* [SANE](David_E._Moriarty#SANE "David E. Moriarty")
* [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")


## Selected Publications


### 1940 ...


* [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts) (**1942**). *[Some observations on the simple neuron circuit](http://link.springer.com/article/10.1007%2FBF02477942)*. [Bulletin of Mathematical Biology](http://link.springer.com/journal/11538), Vol. 4, No. 3
* [Warren S. McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch), [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts) (**1943**). *[A Logical Calculus of the Ideas Immanent in Nervous Activity](http://link.springer.com/article/10.1007%2FBF02478259)*. [Bulletin of Mathematical Biology](http://link.springer.com/journal/11538), Vol. 5, No. 1, [pdf](http://www.aemea.org/math/McCulloch_Pitts_1943.pdf)
* [Donald O. Hebb](https://en.wikipedia.org/wiki/Donald_O._Hebb) (**1949**). *[The Organization of Behavior](https://en.wikipedia.org/wiki/The_Organization_of_Behavior)*. [Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)


### 1950 ...


* [Stephen C. Kleene](Mathematician#SCKleene "Mathematician") (**1951**) *Representation of Events in Nerve Nets and Finite Automata*. RM-704, [RAND paper](https://en.wikipedia.org/wiki/RAND_Corporation), [pdf](http://www.rand.org/content/dam/rand/pubs/research_memoranda/2008/RM704.pdf), reprinted in


 [Claude Shannon](Claude_Shannon "Claude Shannon"), [John McCarthy](John_McCarthy "John McCarthy") (eds.) (**1956**). *Automata Studies*. [Annals of Mathematics Studies](http://press.princeton.edu/math/series/amh.html), No. 34
* [Marvin Minsky](Marvin_Minsky "Marvin Minsky") (**1954**). *Neural Nets and the Brain Model Problem*. Ph.D. dissertation, [Princeton University](https://en.wikipedia.org/wiki/Princeton_University)
* [B. G. Farley](http://dblp.uni-trier.de/pers/hd/f/Farley:B=_G=), [W. A. Clark](http://dblp.uni-trier.de/pers/hd/c/Clark:W=_A=) (**1954**). *Simulation of Self-Organizing Systems by Digital Computer*. [IRE Transactions on Information Theory, Vol. 4](http://dblp.uni-trier.de/db/journals/tit/tit4.html#FarleyC54)
* [John von Neumann](John_von_Neumann "John von Neumann") (**1956**). *Probabilistic Logic and the Synthesis of Reliable Organisms From Unreliable Components*. in


 [Claude Shannon](Claude_Shannon "Claude Shannon"), [John McCarthy](John_McCarthy "John McCarthy") (eds.) (**1956**). *Automata Studies*. [Annals of Mathematics Studies](http://press.princeton.edu/math/series/amh.html), No. 34, [pdf](http://www.dna.caltech.edu/courses/cs191/paperscs191/VonNeumann56.pdf)
* [Nathaniel Rochester](Nathaniel_Rochester "Nathaniel Rochester"), [John H. Holland](Mathematician#Holland "Mathematician"), [L. H. Haibt](https://dblp.uni-trier.de/pers/hd/h/Haibt:L=_H=), [William L. Duda](https://dblp.uni-trier.de/pers/hd/d/Duda:William_L=) (**1956**). *[Tests on a Cell Assembly Theory of the Action of the Brain, Using a Large Digital Computer](https://www.semanticscholar.org/paper/Tests-on-a-cell-assembly-theory-of-the-action-of-a-Rochester-Holland/878d615b84cf779e162f62c4a9192d6bddeefbf9)*. [IRE Transactions on Information Theory, Vol. 2](https://dblp.uni-trier.de/db/journals/tit/tit2n.html), No. 3
* [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) (**1957**). *The Perceptron - a Perceiving and Recognizing Automaton*. Report 85-460-1, [Cornell Aeronautical Laboratory](https://en.wikipedia.org/wiki/Calspan#History) [[55]](#cite_note-55)


### 1960 ...


* [Bernard Widrow](Mathematician#BWidrow "Mathematician"), [Marcian Hoff](Mathematician#MTHoff "Mathematician") (**1960**). *Adaptive switching circuits*. [IRE WESCON Convention Record](https://catalog.hathitrust.org/Record/009671379), Vol. 4, [pdf](http://www-isl.stanford.edu/~widrow/papers/c1960adaptiveswitching.pdf)
* [Henry J. Kelley](https://en.wikipedia.org/wiki/Henry_J._Kelley) (**1960**). *[Gradient Theory of Optimal Flight Paths](http://arc.aiaa.org/doi/abs/10.2514/8.5282?journalCode=arsj&)*. [<http://arc.aiaa.org/loi/arsj> ARS Journal, Vol. 30, No. 10 » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks")
* [Arthur E. Bryson](https://en.wikipedia.org/wiki/Arthur_E._Bryson) (**1961**). *A gradient method for optimizing multi-stage allocation processes*. In Proceedings of the [Harvard University](Harvard_University "Harvard University") Symposium on digital computers and their applications » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks")
* [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") (**1961**). *[The numerical solution of variational problems](http://www.rand.org/pubs/papers/P2374.html)*. RAND paper P-2374 » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks")
* [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) (**1962**). *[Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms](http://catalog.hathitrust.org/Record/000203591)*. Spartan Books
* [Alexey G. Ivakhnenko](https://en.wikipedia.org/wiki/Alexey_Grigorevich_Ivakhnenko) (**1965**). *Cybernetic Predicting Devices*. [Naukova Dumka](https://en.wikipedia.org/wiki/Naukova_Dumka)
* [Marvin Minsky](Marvin_Minsky "Marvin Minsky"), [Seymour Papert](Mathematician#SPapert "Mathematician") (**1969**). *[Perceptrons](https://en.wikipedia.org/wiki/Perceptrons_%28book%29)*. [[56]](#cite_note-56) [[57]](#cite_note-57)


### 1970 ...


* [Seppo Linnainmaa](Mathematician#SLinnainmaa "Mathematician") (**1970**). *The representation of the cumulative rounding error of an algorithm as a Taylor expansion of the local rounding errors*. Master's thesis, [University of Helsinki](https://en.wikipedia.org/wiki/University_of_Helsinki) » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks") [[58]](#cite_note-58)
* [Alexey G. Ivakhnenko](https://en.wikipedia.org/wiki/Alexey_Grigorevich_Ivakhnenko) (**1971**). *Polynomial theory of complex systems*. [IEEE Transactions on Systems, Man, and Cybernetics](IEEE#SMC "IEEE"), Vol. 1, No. 4
* [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1972**). *Brain Function and Adaptive Systems - A Heterostatic Theory*. [Air Force Cambridge Research Laboratories](https://en.wikipedia.org/wiki/Air_Force_Cambridge_Research_Laboratories), Special Reports, No. 133, [pdf](http://www.dtic.mil/dtic/tr/fulltext/u2/742259.pdf)
* [Marvin Minsky](Marvin_Minsky "Marvin Minsky"), [Seymour Papert](Mathematician#SPapert "Mathematician") (**1972**). *[Perceptrons: An Introduction to Computational Geometry](https://en.wikipedia.org/wiki/Perceptrons_%28book%29)*. [The MIT Press](https://en.wikipedia.org/wiki/MIT_Press), 2nd edition with corrections
* [Stephen Grossberg](Mathematician#SGrossberg "Mathematician") (**1973**). *Contour Enhancement, Short Term Memory, and Constancies in Reverberating Neural Networks*. [Studies in Applied Mathematics](https://en.wikipedia.org/wiki/Studies_in_Applied_Mathematics), Vol. 52, [pdf](http://cns.bu.edu/~steve/Gro1973StudiesAppliedMath.pdf)
* [Stephen Grossberg](Mathematician#SGrossberg "Mathematician") (**1974**). *[Classical and instrumental learning by neural networks](http://techlab.bu.edu/resources/article_view/classical_and_instrumental_learning_by_neural_networks/)*. Progress in Theoretical Biology. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)
* [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1974**). *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences*. Ph. D. thesis, [Harvard University](Harvard_University "Harvard University") [[59]](#cite_note-59) [[60]](#cite_note-60)
* [Richard Sutton](Richard_Sutton "Richard Sutton") (**1978**). *Single channel theory: A neuronal theory of learning*. Brain Theory Newsletter 3, No. 3/4, pp. 72-75. [pdf](http://www.cs.ualberta.ca/%7Esutton/papers/sutton-78-BTN.pdf)


### 1980 ...


* [Kunihiko Fukushima](http://www.scholarpedia.org/article/User:Kunihiko_Fukushima) (**1980**). *Neocognitron: A Self-organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position*. [Biological Cybernetics](http://link.springer.com/journal/422), Vol. 36 [[61]](#cite_note-61)
* [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1981**). *Toward a modern theory of adaptive networks: Expectation and prediction*. Psychological Review, Vol. 88, pp. 135-170. [pdf](http://www.cs.ualberta.ca/%7Esutton/papers/sutton-barto-81-PsychRev.pdf)
* [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1982**). *Applications of advances in nonlinear sensitivity analysis*. [System Modeling and Optimization](http://link.springer.com/book/10.1007%2FBFb0006119), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf](http://werbos.com/Neural/SensitivityIFIPSeptember1981.pdf)
* [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1982**). *The Hedonistic Neuron: A Theory of Memory, Learning, and Intelligence*. Hemisphere Publishing Corporation, [University of Michigan](University_of_Michigan "University of Michigan")
* [David H. Ackley](Mathematician#DHAckley "Mathematician"), [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1985**). *A Learning Algorithm for Boltzmann Machines*. Cognitive Science, Vol. 9, No. 1, [pdf](https://web.archive.org/web/20110718022336/http://learning.cs.toronto.edu/~hinton/absps/cogscibm.pdf)
* [David E. Rumelhart](Mathematician#DERumelhart "Mathematician"), [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Ronald J. Williams](https://en.wikipedia.org/wiki/Ronald_J._Williams) (**1986**). *Learning representations by back-propagating errors*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 323, [pdf](http://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)


**1987**



* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1987**). *A 'Neural' Network that Learns to Play Backgammon*. [NIPS 1987](http://www.informatik.uni-trier.de/~ley/db/conf/nips/nips1987.html#TesauroS87)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Frank Wilczek](https://en.wikipedia.org/wiki/Frank_Wilczek) (**1987**). *[Supervised Learning of Probability Distributions by Neural Networks](http://papers.nips.cc/paper/3-supervised-learning-of-probability-distributions-by-neural-networks)*. [NIPS 1987](http://papers.nips.cc/book/neural-information-processing-systems-1987)
* [A. Harry Klopf](A._Harry_Klopf "A. Harry Klopf") (**1987**). *[A Neuronal Model of Classical Conditioning](http://www.dtic.mil/docs/citations/ADA188378)*. Technical Report, [Air Force Wright Aeronautical Laboratories](https://en.wikipedia.org/wiki/Wright_Laboratory) [[62]](#cite_note-62)


**1988**



* [Richard Sutton](Richard_Sutton "Richard Sutton") (**1988**). *Learning to Predict by the Methods of Temporal Differences*. Machine Learning, Vol. 3, No. 1, pp. 9-44. Kluwer Academic Publishers, Boston. ISSN 0885-6125.
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1988**). *Neural network defeats creator in backgammon match*. Technical report no. CCSR-88-6, Center for Complex Systems Research, [University of Illinois at Urbana-Champaign](University_of_Illinois_at_Urbana-Champaign "University of Illinois at Urbana-Champaign")
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [David Haussler](Mathematician#DHHaussler "Mathematician") (**1988**). *[What Size Net Gives Valid Generalization?](http://papers.nips.cc/paper/154-what-size-net-gives-valid-generalization)* [NIPS 1988](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-1-1988)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum") (**1988**). *[On the capabilities of multilayer perceptrons](http://www.sciencedirect.com/science/article/pii/0885064X88900209)*. [Complexity](https://en.wikipedia.org/wiki/Complexity_%28journal%29), Vol. 4, No. 3
* [Alan Lapedes](Mathematician#AlanLapedes "Mathematician"), [Robert Farber](http://www.techenablement.com/rob-farber/) (**1988**). *How Neural Nets Work*. [pdf](https://papers.nips.cc/paper/59-how-neural-nets-work.pdf)


**1989**



* [Andrew Barto](Andrew_Barto "Andrew Barto"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Christopher J. C. H. Watkins](https://dblp.uni-trier.de/pers/hd/w/Watkins:Christopher_J=_C=_H=) (**1989**). *[Sequential Decision Problems and Neural Networks](https://papers.nips.cc/paper/194-sequential-decision-problems-and-neural-networks)*. [NIPS 1989](https://dblp.uni-trier.de/db/conf/nips/nips1989.html)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum") (**1989**). *[The Perceptron Algorithm Is Fast for Non-Malicious Distributions](http://papers.nips.cc/paper/226-the-perceptron-algorithm-is-fast-for-non-malicious-distributions)*. [NIPS 1989](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-2-1989)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum") (**1989**). *[A Proposal for More Powerful Learning Algorithms](http://www.mitpressjournals.org/doi/abs/10.1162/neco.1989.1.2.201#.VfGX0JdpluM)*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_%28journal%29), Vol. 1, No. 2
* [Erach A. Irani](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/i/Irani:E=_A=.html), [John P. Matts](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Matts:John_P=.html), [John M. Long](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/l/Long:John_M=.html), [James R. Slagle](James_R._Slagle "James R. Slagle"), POSCH group (**1989**). *Using Artificial Neural Nets for Statistical Discovery: Observations after Using Backpropogation, Expert Systems, and Multiple-Linear Regression on Clinical Trial Data*. [University of Minnesota](University_of_Minnesota "University of Minnesota"), Minneapolis, MN 55455, USA, Complex Systems 3, [pdf](http://www.complex-systems.com/pdf/03-3-5.pdf)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1989**). *A Parallel Network that Learns to Play Backgammon*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 39, No. 3
* [Erol Gelenbe](Mathematician#EGelenbe "Mathematician") (**1989**). *[Random Neural Networks with Negative and Positive Signals and Product Form Solution](http://cognet.mit.edu/journal/10.1162/neco.1989.1.4.502)*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_(journal)), Vol. 1, No. 4
* [Xiru Zhang](Mathematician#XZhang "Mathematician"), [Michael McKenna](https://dblp.uni-trier.de/pers/hd/m/McKenna:Michael), [Jill P. Mesirov](Mathematician#JPMesirov "Mathematician"), [David Waltz](David_Waltz "David Waltz") (**1989**). *[An Efficient Implementation of the Back-propagation Algorithm on the Connection Machine CM-2](http://papers.neurips.cc/paper/281-an-efficient-implementation-of-the-back-propagation-algorithm-on-the-connection-machine-cm-2)*. [NIPS 1989](https://dblp.uni-trier.de/db/conf/nips/nips1989.html)


### 1990 ...


* [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1990**). *Backpropagation Through Time: What It Does and How to Do It*. Proceedings of the [IEEE](IEEE "IEEE"), Vol. 78, No. 10, [pdf](http://deeplearning.cs.cmu.edu/pdfs/Werbos.backprop.pdf)
* [Chris J. Thornton](Chris_J._Thornton "Chris J. Thornton") (**1990**). *[The Kink Representation for Exclusive-OR](https://link.springer.com/chapter/10.1007/978-94-009-0643-3_155)*. [International Neural Network Conference](https://link.springer.com/book/10.1007/978-94-009-0643-3)
* [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch") (**1990**). *Maximization of Mutual Information in a Context Sensitive Neural Network*. Ph.D. thesis
* [Vadim Anshelevich](Vadim_Anshelevich "Vadim Anshelevich") (**1990**). *Neural Networks*. Review. in Multi Component Systems (Russian)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum") (**1990**). *Polynomial Time Algorithms for Learning Neural Nets*. [COLT 1990](http://dblp.uni-trier.de/db/conf/colt/colt1990.html#Baum90)
* [Dennis W. Ruck](https://dblp.uni-trier.de/pers/hd/r/Ruck:Dennis_W=), [Steven K. Rogers](http://spie.org/profile/Steven.Rogers-5480?SSO=1), [Matthew Kabrisky](https://dblp.uni-trier.de/pers/hd/k/Kabrisky:Matthew), [Mark E. Oxley](Mathematician#MEOxley "Mathematician"), [Bruce W. Suter](Bruce_W._Suter "Bruce W. Suter") (**1990**). *[The multilayer perceptron as an approximation to a Bayes optimal discriminant function](https://ieeexplore.ieee.org/document/80266)*. [IEEE Transactions on Neural Networks](IEEE#NN "IEEE"), Vol. 1, No. 4
* [Benjamin J. Hellstrom](https://dblp.uni-trier.de/pers/hd/h/Hellstrom:Benjamin_J=), [Laveen N. Kanal](Laveen_Kanal "Laveen Kanal") (**1990**). *[The definition of necessary hidden units in neural networks for combinatorial optimization](https://ieeexplore.ieee.org/document/5726889)*. [IJCNN 1990](https://dblp.uni-trier.de/db/conf/ijcnn/ijcnn1990.html)
* [Xiru Zhang](Mathematician#XZhang "Mathematician"), [Michael McKenna](https://dblp.uni-trier.de/pers/hd/m/McKenna:Michael), [Jill P. Mesirov](Mathematician#JPMesirov "Mathematician"), [David Waltz](David_Waltz "David Waltz") (**1990**). *[The backpropagation algorithm on grid and hypercube architectures](https://www.sciencedirect.com/science/article/pii/016781919090084M)*. [Parallel Computing](https://www.journals.elsevier.com/parallel-computing), Vol. 14, No. 3
* [Simon Lucas](Simon_Lucas "Simon Lucas"), [Robert I. Damper](https://dblp.uni-trier.de/pers/hd/d/Damper:Robert_I=) (**1990**). *[Syntactic Neural Networks](https://www.tandfonline.com/doi/abs/10.1080/09540099008915669)*. [Connection Science](https://www.tandfonline.com/toc/ccos20/current), Vol. 2, No. 3


**1991**



* [Sepp Hochreiter](Mathematician#SHochreiter "Mathematician") (**1991**). *Untersuchungen zu dynamischen neuronalen Netzen*. Diploma thesis, [TU Munich](Technical_University_of_Munich "Technical University of Munich"), advisor [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber"), [pdf](http://people.idsia.ch/~juergen/SeppHochreiter1991ThesisAdvisorSchmidhuber.pdf) (German) [[63]](#cite_note-63)
* [Alex van Tiggelen](Alex_van_Tiggelen "Alex van Tiggelen") (**1991**). *Neural Networks as a Guide to Optimization - The Chess Middle Game Explored*. [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
* [Thomas Martinetz](Mathematician#TMartinetz "Mathematician"), [Klaus Schulten](Mathematician#KSchulten "Mathematician") (**1991**). *A "Neural-Gas" Network Learns Topologies*. In [Teuvo Kohonen](Mathematician#TKohonen "Mathematician"), [Kai Mäkisara](https://dblp.uni-trier.de/pers/hd/m/Makisara:Kai), [Olli Simula](http://users.ics.tkk.fi/ollis/), [Jari Kangas](http://cis.legacy.ics.tkk.fi/jari/) (eds.) (**1991**). *[Artificial Neural Networks](https://www.elsevier.com/books/artificial-neural-networks/makisara/978-0-444-89178-5)*. [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [pdf](http://www.ks.uiuc.edu/Publications/Papers/PDF/MART91B/MART91B.pdf)
* [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber"), [Rudolf Huber](Rudolf_Huber "Rudolf Huber") (**1991**). *[Using sequential adaptive Neuro-control for efficient Learning of Rotation and Translation Invariance](https://www.researchgate.net/publication/2290900_Using_Adaptive_Sequential_Neurocontrol_For_Efficient_Learning_Of_Translation_And_Rotation_Invariance)*. In [Teuvo Kohonen](Mathematician#TKohonen "Mathematician"), [Kai Mäkisara](https://dblp.uni-trier.de/pers/hd/m/Makisara:Kai), [Olli Simula](http://users.ics.tkk.fi/ollis/), [Jari Kangas](http://cis.legacy.ics.tkk.fi/jari/) (eds.) (**1991**). *[Artificial Neural Networks](https://www.sciencedirect.com/book/9780444891785/artificial-neural-networks#book-description)*. [Elsevier](https://en.wikipedia.org/wiki/Elsevier)
* [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1991**). *[Dynamische neuronale Netze und das fundamentale raumzeitliche Lernproblem](http://www.idsia.ch/%7Ejuergen/promotion/)* (Dynamic Neural Nets and the Fundamental Spatio-Temporal Credit Assignment Problem). Ph.D. thesis
* [Yoav Freund](Yoav_Freund "Yoav Freund"), [David Haussler](Mathematician#DHHaussler "Mathematician") (**1991**). *Unsupervised Learning of Distributions of Binary Vectors Using 2-Layer Networks*. [NIPS 1991](http://dblp.uni-trier.de/db/conf/nips/nips1991.html#FreundH91)
* [Byoung-Tak Zhang](Byoung-Tak_Zhang "Byoung-Tak Zhang"), [Gerd Veenker](Gerd_Veenker "Gerd Veenker") (**1991**). *[Neural networks that teach themselves through genetic discovery of novel examples](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=170480&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D170480)*. [IEEE IJCNN'91](http://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000500), [pdf](https://bi.snu.ac.kr/Publications/Conferences/International/IJCNN91.pdf)
* [Simon Lucas](Simon_Lucas "Simon Lucas"), [Robert I. Damper](https://dblp.uni-trier.de/pers/hd/d/Damper:Robert_I=) (**1991**). *[Syntactic neural networks in VLSI](https://link.springer.com/chapter/10.1007/978-1-4615-3752-6_30)*. [VLSI for Artificial Intelligence and Neural Networks](https://link.springer.com/book/10.1007/978-1-4615-3752-6)
* [Simon Lucas](Simon_Lucas "Simon Lucas") (**1991**). *[Connectionist architectures for syntactic pattern recognition](https://eprints.soton.ac.uk/256263/)*. Ph.D. thesis, [University of Southampton](https://en.wikipedia.org/wiki/University_of_Southampton)


**1992**



* [Michael Reiss](index.php?title=Michael_Reiss&action=edit&redlink=1 "Michael Reiss (page does not exist)") (**1992**). *Temporal Sequence Processing in Neural Networks*. Ph.D. thesis, [King's College London](https://en.wikipedia.org/wiki/King%27s_College_London), advisor [John G. Taylor](Mathematician#JGTaylor "Mathematician"), [pdf](http://www.reiss.demon.co.uk/misc/m_reiss_phd.pdf)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Bohdan Macukow](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Macuk:Bohdan.html) (**1992**). *A Neural Network designed to solve the N-Queens Problem*. [Biological Cybernetics, Vol. 66 No. 4](http://www.informatik.uni-trier.de/~ley/db/journals/bc/bc72.html#Mandziuk95), [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/bc92.pdf)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *Temporal Difference Learning of Backgammon Strategy*. [ML 1992](http://www.informatik.uni-trier.de/~ley/db/conf/icml/ml1992.html#Tesauro92)
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1992**). *[Practical Issues in Temporal Difference Learning](http://dl.acm.org/citation.cfm?id=139616)*. [Machine Learning, Vol. 8, No. 3-4](http://www.informatik.uni-trier.de/~ley/db/journals/ml/ml8.html#Tesauro92)
* [Egbert Boers](index.php?title=Egbert_Boers&action=edit&redlink=1 "Egbert Boers (page does not exist)"), [Herman Kuiper](index.php?title=Herman_Kuiper&action=edit&redlink=1 "Herman Kuiper (page does not exist)") (**1992**). *Biological metaphors and the design of modular artificial neural networks*. Master’s thesis, [Leiden University](Leiden_University "Leiden University"), [pdf](http://liacs.leidenuniv.nl/assets/PDF/boers-kuiper.92.pdf)
* [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Heinrich Braun](index.php?title=Heinrich_Braun&action=edit&redlink=1 "Heinrich Braun (page does not exist)") (**1992**). *[Rprop - A Fast Adaptive Learning Algorithm](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.52.4576)*. Proceedings of the International Symposium on Computer and Information Science
* [Justin A. Boyan](Justin_A._Boyan "Justin A. Boyan") (**1992**). *Modular Neural Networks for Learning Context-Dependent Game Strategies*. Master's thesis, [University of Cambridge](https://en.wikipedia.org/wiki/University_of_Cambridge), [pdf](http://www.cs.cmu.edu/~jab/cv/pubs/boyan.backgammon-thesis.pdf)
* [Patricia Churchland](https://en.wikipedia.org/wiki/Patricia_Churchland), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1992**). *[The Computational Brain](https://mitpress.mit.edu/books/computational-brain)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Benjamin J. Hellstrom](https://dblp.uni-trier.de/pers/hd/h/Hellstrom:Benjamin_J=), [Laveen N. Kanal](Laveen_Kanal "Laveen Kanal") (**1992**). *[Knapsack packing networks](https://ieeexplore.ieee.org/document/125871)*. [IEEE Transactions on Neural Networks](IEEE#NN "IEEE"), Vol. 3, No. 2
* [Benjamin J. Hellstrom](https://dblp.uni-trier.de/pers/hd/h/Hellstrom:Benjamin_J=), [Laveen N. Kanal](Laveen_Kanal "Laveen Kanal") (**1992**). *Asymmetric mean-field neural networks for multiprocessor scheduling*. [Neural Networks](https://en.wikipedia.org/wiki/Neural_Networks_(journal)), Vol. 5, No. 4


**1993**



* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk"), [Bohdan Macukow](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/m/Macuk:Bohdan.html) (**1993**). *A Neural Network performing Boolean Logic Operations*. [Optical Memory and Neural Networks](http://www.springerlink.com/content/1060-992x/), Vol. 2, No. 1, [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/omnn93.pdf)
* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun"), [Tom Mitchell](Tom_Mitchell "Tom Mitchell") (**1993**). *Integrating Inductive Neural Network Learning and Explanation-Based Learning*. Proceedings of the 13th IJCAI, Morgan Kaufmann, [zipped ps](http://robots.stanford.edu/papers/thrun.EBNN_ijcai93.ps.gz)
* [Byoung-Tak Zhang](Byoung-Tak_Zhang "Byoung-Tak Zhang"), [Heinz Mühlenbein](Mathematician#HMuehlenbein "Mathematician") (**1993**). *Evolving Optimal Neural Networks Using Genetic Algorithms with Occam's Razor*. [Complex Systems](https://en.wikipedia.org/wiki/Complex_Systems_(journal)), Vol. 7, [pdf](http://www.complex-systems.com/pdf/07-3-2.pdf)
* [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Heinrich Braun](index.php?title=Heinrich_Braun&action=edit&redlink=1 "Heinrich Braun (page does not exist)") (**1993**). *A direct adaptive method for faster backpropagation learning: The RPROP algorithm*. [IEEE International Conference On Neural Networks](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=1059), [pdf](http://paginas.fe.up.pt/~ee02162/dissertacao/RPROP%20paper.pdf)
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph"), [Peter Dayan](Peter_Dayan "Peter Dayan"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1993**). *[Temporal Difference Learning of Position Evaluation in the Game of Go](https://papers.nips.cc/paper/820-temporal-difference-learning-of-position-evaluation-in-the-game-of-go)*. [NIPS 1993](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-6-1993) [[64]](#cite_note-64)


**1994**



* [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1994**). *The Roots of Backpropagation. From Ordered Derivatives to Neural Networks and Political Forecasting*. [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Evolving Neural Networks to focus Minimax Search](http://nn.cs.utexas.edu/?moriarty:aaai94)*. [AAAI-94](Conferences#AAAI-94 "Conferences") » [Othello](Othello "Othello")
* [Eric Postma](Eric_Postma "Eric Postma") (**1994**). *SCAN: A Neural Model of Covert Attention*. Ph.D. thesis, [Maastricht University](Maastricht_University "Maastricht University"), advisor [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik")
* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1994**). *Neural Network Learning in the Domain of Chess*. Machines That Learn, [Snowbird](http://snowbird.djvuzone.org/), Extended abstract
* [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), S. Schawelski, [Michael Schlosser](Michael_Schlosser "Michael Schlosser") (**1994**). *Neural Network Learning in a Chess Endgame Positions*. IEEE World Congress on Computational Intelligence
* [Alois Heinz](Alois_Heinz "Alois Heinz") (**1994**). *[Efficient Neural Net α-β-Evaluators](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.3994)*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.55.3994&rep=rep1&type=pdf) [[65]](#cite_note-65)
* [Alois Heinz](Alois_Heinz "Alois Heinz") (**1994**). *Fast bounded smooth regression with lazy neural trees*. [ICNN 1994](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=3013), DOI: [10.1109/ICNN.1994.374421](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=374421)
* [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)") (**1994**). *Rprop - Description and Implementation Details*. Technical Report, [University of Karlsruhe](https://en.wikipedia.org/wiki/Karlsruhe_Institute_of_Technology), [pdf](http://www.inf.fu-berlin.de/lehre/WS06/Musterererkennung/Paper/rprop.pdf)
* [Igor Kononenko](Igor_Kononenko "Igor Kononenko") (**1994**). *On Bayesian Neural Networks*. [Informatica (Slovenia), Vol. 18](https://dblp.uni-trier.de/db/journals/informaticaSI/informaticaSI18.html), No. 2


**1995**



* [Peter J. Braspenning](https://peterbraspenning.wordpress.com/), [Frank Thuijsman](index.php?title=Frank_Thuijsman&action=edit&redlink=1 "Frank Thuijsman (page does not exist)"), [Ton Weijters](https://scholar.google.com/citations?user=Ba9L7CAAAAAJ) (eds) (**1995**). *[Artificial neural networks: an introduction to ANN theory and practice](http://link.springer.com/book/10.1007%2FBFb0027019)*. [LNCS](https://de.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 931, [Springer](https://de.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1995**). *[Discovering Complex Othello Strategies Through Evolutionary Neural Networks](http://nn.cs.utexas.edu/?moriarty:connsci95)*. [Connection Science](https://www.scimagojr.com/journalsearch.php?q=24173&tip=sid), Vol. 7
* [Anton Leouski](index.php?title=Anton_Leouski&action=edit&redlink=1 "Anton Leouski (page does not exist)") (**1995**). *Learning of Position Evaluation in the Game of Othello*. Master's Project, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts), [Amherst, Massachusetts](https://en.wikipedia.org/wiki/Amherst,_Massachusetts), [pdf](http://people.ict.usc.edu/~leuski/publications/papers/UM-CS-1995-023.pdf)
* [Sepp Hochreiter](Mathematician#SHochreiter "Mathematician"), [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1995**). *[Simplifying Neural Nets by Discovering Flat Minima](http://www.idsia.ch/%7Ejuergen/nipsfm/)*. In [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [David S. Touretzky](http://www.cs.cmu.edu/%7Edst/home.html) and [Todd K. Leen](http://www.bme.ogi.edu/%7Etleen/) (eds.), *[Advances in Neural Information Processing Systems 7](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=8420)*, NIPS'7, pages 529-536. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. in [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [David S. Touretzky](https://en.wikipedia.org/wiki/David_S._Touretzky), [Todd K. Leen](http://mitpress.mit.edu/authors/todd-k-leen) (eds.) Advances in Neural Information Processing Systems 7, [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Sepp Hochreiter](http://www.bioinf.jku.at/people/hochreiter/), [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1995**). *[Simplifying Neural Nets by Discovering Flat Minima](http://www.idsia.ch/%7Ejuergen/nipsfm/)*. In [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [David S. Touretzky](http://www.cs.cmu.edu/%7Edst/home.html) and [Todd K. Leen](http://www.bme.ogi.edu/%7Etleen/) (eds.), *[Advances in Neural Information Processing Systems 7](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=8420)*, NIPS'7, pages 529-536. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *Explanation-Based Neural Network Learning - A Lifelong Learning Approach*. Ph.D. thesis, [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn), advisors [Armin Cremers](Mathematician#ABCremers "Mathematician") and [Tom Mitchell](Tom_Mitchell "Tom Mitchell")
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**1995**). *Temporal Difference Learning and TD-Gammon*. [Communications of the ACM](ACM#Communications "ACM") Vol. 38, No. 3
* [Eric Postma](Eric_Postma "Eric Postma") (**1995**). *Optimization Networks*. [Artificial Neural Networks](http://www.informatik.uni-trier.de/~ley/db/conf/ann/ann1995.html#Postma95)
* [Jacek Jelonek](http://www.informatik.uni-trier.de/~ley/pers/hd/j/Jelonek:Jacek.html), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [Roman Slowinski](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Slowinski:Roman.html) (**1995**). *[Rough Set Reduction of Attributes and their Domains for Neural Networks](http://onlinelibrary.wiley.com/doi/10.1111/j.1467-8640.1995.tb00036.x/abstract)*. [Computational Intelligence](http://onlinelibrary.wiley.com/journal/10.1111/%28ISSN%291467-8640), Vol. 11, No. 2
* [Omar Syed](Omar_Syed "Omar Syed") (**1995**). *[Applying Genetic Algorithms to Recurrent Neural Networks for Learning Network Parameters and Architecture](http://arimaa.com/arimaa/about/Thesis/)*, Masters Thesis, [Case Western Reserve University](https://en.wikipedia.org/wiki/Case_Western_Reserve_University)
* [Pascal Tang](Pascal_Tang "Pascal Tang") (**1995**). *Forecasting with Neural networks*. [ICANN 1995](http://www.e-nns.org/index.php/ICANN/History/)
* [Marco Wiering](Marco_Wiering "Marco Wiering") (**1995**). *TD Learning of Game Evaluation Functions with Hierarchical Neural Architectures*. Master's thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam), [pdf](http://webber.physik.uni-freiburg.de/~hon/vorlss02/Literatur/reinforcement/GameEvaluationWithNeuronal.pdf)
* [Michael A Arbib](index.php?title=Michael_A_Arbib&action=edit&redlink=1 "Michael A Arbib (page does not exist)") (ed.) (**1995, 2002**). *[The Handbook of Brain Theory and Neural Networks](http://mitpress.mit.edu/books/handbook-brain-theory-and-neural-networks)*. [The MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph") (**1995**). *[Optimization of Entropy with Neural Networks](http://nic.schraudolph.org/bib2html/b2hd-Schraudolph95)*. Ph.D. thesis, [University of California, San Diego](https://en.wikipedia.org/wiki/University_of_California,_San_Diego)
* [Alois Heinz](Alois_Heinz "Alois Heinz") (**1995**). *Pipelined Neural Tree Learning by Error Forward-Propagation*. [ICNN 1995](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=3505), DOI: [10.1109/ICNN.1995.488132](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=488132), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.4154&rep=rep1&type=pdf)
* [Alois Heinz](Alois_Heinz "Alois Heinz"), [Christoph Hense](index.php?title=Christoph_Hense&action=edit&redlink=1 "Christoph Hense (page does not exist)") (**1995**). *[Tools for Neural Trees](http://tr.informatik.uni-freiburg.de/1995/Report68/)*. Technical Report No. 68
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**1995**). *Tempering Backpropagation Networks: Not All Weights are Created Equal*. [NIPS 1995](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-8-1995), [pdf](https://papers.nips.cc/paper/1100-tempering-backpropagation-networks-not-all-weights-are-created-equal.pdf)


**1996**



* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1996**). *[Explanation-Based Neural Network Learning: A Lifelong Learning Approach](http://robots.stanford.edu/papers/thrun.book.html)*. [Kluwer Academic Publishers](https://en.wikipedia.org/wiki/Wolters_Kluwer)
* [Wee Sun Lee](Wee_Sun_Lee "Wee Sun Lee") (**1996**). *Agnostic Learning and Single Hidden Layer Neural Networks.* Ph.D. thesis, [Australian National University](Australian_National_University "Australian National University"), [ps](http://www.comp.nus.edu.sg/~leews/publications/thesis.ps)
* [Markus Enzenberger](Markus_Enzenberger "Markus Enzenberger") (**1996**). *[The Integration of A Priori Knowledge into a Go Playing Neural Network](http://webdocs.cs.ualberta.ca/~emarkus/neurogo/neurogo1996.html)*.
* [Pieter Spronck](Pieter_Spronck "Pieter Spronck") (**1996**). *Elegance: Genetic Algorithms in Neural Reinforcement Control*. Master thesis, [Delft University of Technology](Delft_University_of_Technology "Delft University of Technology"), [pdf](http://ticc.uvt.nl/~pspronck/pubs/Elegance.pdf)
* [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**1996**). *Neural Networks - A Systematic Introduction*. Springer, available as [pdf ebook](http://www.inf.fu-berlin.de/inst/ag-ki/rojas_home/documents/1996/NeuralNetworks/neuron.pdf)
* [Ida Sprinkhuizen-Kuyper](Ida_Sprinkhuizen-Kuyper "Ida Sprinkhuizen-Kuyper"), [Egbert J. W. Boers](https://dblp.org/pers/hd/b/Boers:Egbert_J=_W=) (**1996**). *[The Error Surface of the Simplest XOR Network Has Only Global Minima](https://ieeexplore.ieee.org/abstract/document/6796246)*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_(journal)), Vol. 8, No. 6, [pdf](http://www.socsci.ru.nl/idak/publications/papers/NeuralComputation.pdf)


**1997**



* [Sepp Hochreiter](Mathematician#SHochreiter "Mathematician"), [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**1997**). *Long short-term memory*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_%28journal%29), Vol. 9, No. 8, [pdf](http://deeplearning.cs.cmu.edu/pdfs/Hochreiter97_lstm.pdf) [[66]](#cite_note-66)
* [Kieran Greer](Kieran_Greer "Kieran Greer"), [Piyush Ojha](index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1997**). *Learning Search Heuristics from Examples: A Study in Computer Chess*. Seventh Conference of the Spanish Association for Artificial Intelligence, CAEPIA’97, November, pp. 695-704.
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Frank M. Thiesing](https://dblp.uni-trier.de/pers/hd/t/Thiesing:Frank_M=), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1997**). *Forecasting Sales Using Neural Networks*. [Fuzzy Days 1997](https://dblp.uni-trier.de/db/conf/fuzzy/fuzzy1997.html), [pdf](http://www2.inf.uos.de/papers_pdf/fuzzydays_97.pdf)
* [Simon Lucas](Simon_Lucas "Simon Lucas") (**1997**). *[Forward-Backward Building Blocks for Evolving Neural Networks with Intrinsic Learning Behaviors](https://link.springer.com/chapter/10.1007/BFb0032531)*. [IWANN 1997](https://dblp.uni-trier.de/db/conf/iwann/iwann1997.html)


**1998**



* [Kieran Greer](Kieran_Greer "Kieran Greer") (**1998**). *A Neural Network Based Search Heuristic and its Application to Computer Chess*. D.Phil. Thesis, [University of Ulster](https://en.wikipedia.org/wiki/University_of_Ulster)
* [Nobusuke Sasaki](Nobusuke_Sasaki "Nobusuke Sasaki"), [Yasuji Sawada](index.php?title=Yasuji_Sawada&action=edit&redlink=1 "Yasuji Sawada (page does not exist)"), [Jin Yoshimura](Jin_Yoshimura "Jin Yoshimura") (**1998**). *[A Neural Network Program of Tsume-Go](http://link.springer.com/chapter/10.1007%2F3-540-48957-6_10)*. [CG 1998](CG_1998 "CG 1998") [[67]](#cite_note-67)
* [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [Roman Slowinski](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Slowinski:Roman.html), [Irmina Szczesniak](http://www.informatik.uni-trier.de/~ley/pers/hd/s/Szczesniak:Irmina.html) (**1998**). *[Pedagogical Method for Extraction of Symbolic Knowledge from Neural Networks](http://link.springer.com/chapter/10.1007%2F3-540-69115-4_60)*. [Rough Sets and Current Trends in Computing 1998](http://link.springer.com/book/10.1007%2F3-540-69115-4)
* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)") (**1998**). *Neural network models for a resource allocation problem*. IEEE Transactions on Systems, Man, and Cybernetics, Part B 28(2)
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *Experiments in Parameter Learning Using Temporal Differences*. [ICCA Journal, Volume 21 No. 2](ICGA_Journal#21_2 "ICGA Journal"), [pdf](http://cs.anu.edu.au/%7ELex.Weaver/pub_sem/publications/ICCA-98_equiv.pdf)
* [Guy Haworth](Guy_Haworth "Guy Haworth"), [Meel Velliste](Meel_Velliste "Meel Velliste") (**1998**). *[Chess Endgames and Neural Networks](http://centaur.reading.ac.uk/4569/)*. [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1998**). *First Results from Using Temporal Difference Learning in Shogi*. [CG 1998](CG_1998 "CG 1998")
* [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph") (**1998**). *[Centering Neural Network Gradient Factors](http://nic.schraudolph.org/bib2html/b2hd-Schraudolph98.html)*. Neural Networks: Tricks of the Trade
* [Toshinori Munakata](Toshinori_Munakata "Toshinori Munakata") (**1998**). *[Fundamentals of the New Artificial Intelligence: Beyond Traditional Paradigms](http://cis.csuohio.edu/~munakata/publs/book/sp.html)*. 1st edition, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [2nd edition 2008](Neural_Networks#FundamentalsNAI2nd "Neural Networks")
* [Lex Weaver](Lex_Weaver "Lex Weaver"), [Terry Bossomaier](https://bjbs.csu.edu.au/schools/computing-and-mathematics/staff/profiles/professorial-staff/terry-bossomaier) (**1998**). *Evolution of Neural Networks to Play the Game of Dots-and-Boxes*. [arXiv:cs/9809111](https://arxiv.org/abs/cs/9809111)
* [Norman Richards](index.php?title=Norman_Richards&action=edit&redlink=1 "Norman Richards (page does not exist)"), [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1998**). *[Evolving Neural Networks to Play Go](http://nn.cs.utexas.edu/?richards:apin98)*. [Applied Intelligence](https://www.springer.com/journal/10489), Vol. 8, No. 1


**1999**



* [Kumar Chellapilla](index.php?title=Kumar_Chellapilla&action=edit&redlink=1 "Kumar Chellapilla (page does not exist)"), [David B. Fogel](David_B._Fogel "David B. Fogel") (**1999**). *[Evolution, Neural Networks, Games, and Intelligence](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=784222)*. Proceedings of the IEEE, September, pp. 1471-1496. [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.99.979)
* [Kumar Chellapilla](index.php?title=Kumar_Chellapilla&action=edit&redlink=1 "Kumar Chellapilla (page does not exist)"), [David B. Fogel](David_B._Fogel "David B. Fogel") (**1999**). *[Evolving Neural Networks to Play Checkers without Expert Knowledge](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=809083)*. IEEE Transactions on Neural Networks, Vol. 10, No. 6, pp. 1382-1391.
* [Kieran Greer](Kieran_Greer "Kieran Greer"), [Piyush Ojha](index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1999**). *A Pattern-Oriented Approach to Move Ordering: the Chessmaps Heuristic*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")
* Anna Górecka, [Maciej Szmit](Maciej_Szmit "Maciej Szmit") (**1999**). *Exchange rates prediction by ARIMA and Neural Networks Models*. 47th International Atlantic Economic Conerence (Abstract: International Advances of Economic Research Vol 5 Nr 4 Nov. 1999, St Louis, MO, USA 1999), [pdf](http://maciej.szmit.info/documents/annarima.pdf)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
* [Simon S. Haykin](https://en.wikipedia.org/wiki/Simon_Haykin) (**1999**). *[Neural Networks: A Comprehensive Foundation](http://dl.acm.org/citation.cfm?id=521706)*. 2nd Edition, [Prentice-Hall](https://en.wikipedia.org/wiki/Prentice_Hall)
* [Laurence F. Abbott](https://en.wikipedia.org/wiki/Larry_Abbott), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (eds.) (**1999**). *[Neural Codes and Distributed Representations](https://mitpress.mit.edu/books/neural-codes-and-distributed-representations)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (eds.) (**1999**). *[Unsupervised Learning: Foundations of Neural Computation](https://mitpress.mit.edu/books/unsupervised-learning)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Peter Dayan](Peter_Dayan "Peter Dayan") (**1999**). *Recurrent Sampling Models for the Helmholtz Machine*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_(journal)), Vol. 11, No. 3, [pdf](http://www.gatsby.ucl.ac.uk/~dayan/papers/rechelm99.pdf) [[68]](#cite_note-68)
* [Ida Sprinkhuizen-Kuyper](Ida_Sprinkhuizen-Kuyper "Ida Sprinkhuizen-Kuyper"), [Egbert J. W. Boers](https://dblp.org/pers/hd/b/Boers:Egbert_J=_W=) (**1999**). *[A local minimum for the 2-3-1 XOR network](https://ieeexplore.ieee.org/document/774274)*. [IEEE Transactions on Neural Networks](IEEE#NN "IEEE"), Vol. 10, No. 4


### 2000 ...


* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2000**). *[Learning Time Allocation using Neural Networks](http://link.springer.com/chapter/10.1007%2F3-540-45579-5_11)*. [CG 2000](CG_2000 "CG 2000")
* [Peter Auer](Peter_Auer "Peter Auer"), [Stephen Kwek](Mathematician#SKwek "Mathematician"), [Wolfgang Maass](Mathematician#WMaass "Mathematician"), [Manfred K. Warmuth](Mathematician#MKWarmuth "Mathematician") (**2000**). *[Learning of Depth Two Neural Networks with Constant Fan-in at the Hidden Nodes](http://eccc.hpi-web.de/report/2000/055/)*. [Electronic Colloquium on Computational Complexity, Vol. 7](http://dblp.uni-trier.de/db/journals/eccc/eccc7.html#ECCC-TR00-055)
* [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**2000**). *Learning to Play Chess Using Temporal Differences*. [Machine Learning, Vol 40, No. 3](http://www.dblp.org/db/journals/ml/ml40.html#BaxterTW00), [pdf](http://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/chess-RL.pdf)
* [Alois Heinz](Alois_Heinz "Alois Heinz") (**2000**). *[Tree-Structured Neural Networks: Efficient Evaluation of Higher-Order Derivatives and Integrals](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=857884)*. [IJCNN 2000](http://dblp.uni-trier.de/db/conf/ijcnn/ijcnn2000-2.html#Heinz00)
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Ryan Weber](index.php?title=Ryan_Weber&action=edit&redlink=1 "Ryan Weber (page does not exist)") (**2000**). *[Chess Neighborhoods, Function Combination, and Reinforcement Learning](http://link.springer.com/chapter/10.1007/3-540-45579-5_9)*. [CG 2000](CG_2000 "CG 2000"), [pdf](https://users.soe.ucsc.edu/~levinson/Papers/CNFCRL.pdf)
* [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher") (**2000**). *Automatic Generation of an Evaluation Function for Chess Endgames*. [ETH Zurich](ETH_Zurich "ETH Zurich") Supervisors: [Thomas Lincke](Thomas_Lincke "Thomas Lincke") and [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [pdf](http://www.datacomm.ch/m.luescher/evaluation_function_en.pdf) » [Endgame](Endgame "Endgame")
* [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (**2000**). *[Designing neural network architectures for pattern recognition](http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=58577)*. [The Knowledge Engineering Review, Vol. 15](http://dblp2.uni-trier.de/db/journals/ker/ker15.html), No. 2
* [Igor Aizenberg](https://scholar.google.com/citations?user=ZjfN_9AAAAAJ), [Naum N. Aizenberg](http://dblp.uni-trier.de/pers/hd/a/Aizenberg:Naum_N=), [Joos Vandewalle](https://scholar.google.com/citations?user=Swa4FrsAAAAJ) (**2000**). *[Multi-Valued and Universal Binary Neurons: Theory, Learning and Applications](http://link.springer.com/book/10.1007%2F978-1-4757-3115-6)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) [[69]](#cite_note-69)


**2001**



* [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Visual Learning in Go*. [6th Computer Olympiad Workshop](6th_Computer_Olympiad#Workshop "6th Computer Olympiad"), [pdf](http://erikvanderwerf.tengen.nl/pubdown/visual_learning_in_go.pdf)
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Move Ordering using Neural Networks*. IEA/AIE 2001, [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2070, [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/parallel/fulltext.pdf)
* [Kee Siong Ng](index.php?title=Kee_Siong_Ng&action=edit&redlink=1 "Kee Siong Ng (page does not exist)") (**2001**). *Neural Networks for Structured Data*. BSc-Thesis, [zipped ps](http://users.cecs.anu.edu.au/~kee/hon-thesis.ps.gz)
* [Peter Dayan](Peter_Dayan "Peter Dayan"), [Laurence F. Abbott](https://en.wikipedia.org/wiki/Larry_Abbott) (**2001, 2005**). *[Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems](http://www.gatsby.ucl.ac.uk/~dayan/book/index.html)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)


**2002**



* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007%2F978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002")
* [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[Local Move Prediction in Go](http://link.springer.com/chapter/10.1007%2F978-3-540-40031-8_26)*. [CG 2002](CG_2002 "CG 2002")
* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2002**). *Programming backgammon using self-teaching neural nets*. [Artificial Intelligence Vol. 134 No. 1-2](http://www.informatik.uni-trier.de/~ley/db/journals/ai/ai134.html#Tesauro02)
* [Mark Winands](Mark_Winands "Mark Winands"), [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *Temporal difference learning and the Neural MoveMap heuristic in the game of Lines of Action*. in GAME-ON 2002, [pdf](http://zaphod.aml.sztaki.hu/papers/winands-GAMEON02.pdf)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk") (**2002**). *Neural Networks for the N-Queens Problem: a Review*. [Control and Cybernetics](http://www.scimagojr.com/journalsearch.php?q=12928&tip=sid), Vol. 31, No. 2, [pdf](http://www.mini.pw.edu.pl/~mandziuk/PRACE/nqp-rev.pdf)
* [Moshe Sipper](index.php?title=Moshe_Sipper&action=edit&redlink=1 "Moshe Sipper (page does not exist)") (**2002**) *[Machine Nature: The Coming Age of Bio-Inspired Computing](http://books.google.com/books/about/Machine_Nature.html?id=fbFQAAAAMAAJ&redir_esc=y)*. [McGraw-Hill, New York](https://en.wikipedia.org/wiki/McGraw-Hill_Financial)
* [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [David J. Stracuzzi](index.php?title=David_J._Stracuzzi&action=edit&redlink=1 "David J. Stracuzzi (page does not exist)") (**2002**). *Many-Layered Learning*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_%28journal%29), Vol. 14, No. 10, [pdf](http://people.cs.umass.edu/~utgoff/papers/neco-stl.pdf)
* [Michael I. Jordan](Mathematician#MIJordan "Mathematician"), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (eds.) (**2002**). *[Graphical Models: Foundations of Neural Computation](https://mitpress.mit.edu/books/graphical-models)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Kenneth O. Stanley](index.php?title=Kenneth_O._Stanley&action=edit&redlink=1 "Kenneth O. Stanley (page does not exist)"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2002**). *[Evolving Neural Networks Through Augmenting Topologies](http://nn.cs.utexas.edu/?stanley:ec02)*. [Evolutionary Computation](https://en.wikipedia.org/wiki/Evolutionary_Computation_(journal)), Vol. 10, No. 2


**2003**



* [Levente Kocsis](Levente_Kocsis "Levente Kocsis") (**2003**). *Learning Search Decisions*. Ph.D thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](https://project.dke.maastrichtuniversity.nl/games/files/phd/Kocsis_thesis.pdf)
* [Markus Enzenberger](Markus_Enzenberger "Markus Enzenberger") (**2003**). *[Evaluation in Go by a Neural Network using Soft Segmentation](http://webdocs.cs.ualberta.ca/~emarkus/neurogo/neurogo3/index.html)*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://webdocs.cs.ualberta.ca/~emarkus/publications/neurogo3.pdf)
* [Alois Heinz](Alois_Heinz "Alois Heinz") (**2003**). *[Yes, Trees May Have Neurons](http://link.springer.com/chapter/10.1007%2F3-540-36477-3_13)*. [Computer Science in Perspective 2003](http://dblp.uni-trier.de/db/conf/birthday/ottmann2003.html#Heinz03)


**2004**



* [Jan Peter Patist](http://dblp.uni-trier.de/pers/hd/p/Patist:Jan_Peter), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2004**). *Learning to Play Draughts using Temporal Difference Learning with Neural Networks and Databases*. [Cognitive Artiﬁcial Intelligence](http://students.uu.nl/en/hum/cognitive-artificial-intelligence), [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), Benelearn’04
* [Henk Mannen](Henk_Mannen "Henk Mannen"), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2004**). *[Learning to play chess using TD(λ)-learning with database games](https://www.semanticscholar.org/paper/Learning-to-Play-Chess-using-TD(lambda)-learning-Mannen-Wiering/00a6f81c8ebe8408c147841f26ed27eb13fb07f3)*. Cognitive Artiﬁcial Intelligence, [Utrecht University](https://en.wikipedia.org/wiki/Utrecht_University), Benelearn’04, [pdf](https://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/learning-chess.pdf)
* [Mathieu Autonès](index.php?title=Mathieu_Auton%C3%A8s&action=edit&redlink=1 "Mathieu Autonès (page does not exist)"), [Aryel Beck](index.php?title=Aryel_Beck&action=edit&redlink=1 "Aryel Beck (page does not exist)"), [Phillippe Camacho](index.php?title=Phillippe_Camacho&action=edit&redlink=1 "Phillippe Camacho (page does not exist)"), [Nicolas Lassabe](index.php?title=Nicolas_Lassabe&action=edit&redlink=1 "Nicolas Lassabe (page does not exist)"), [Hervé Luga](index.php?title=Herv%C3%A9_Luga&action=edit&redlink=1 "Hervé Luga (page does not exist)"), [François Scharffe](index.php?title=Fran%C3%A7ois_Scharffe&action=edit&redlink=1 "François Scharffe (page does not exist)") (**2004**). *[Evaluation of Chess Position by Modular Neural network Generated by Genetic Algorithm](http://link.springer.com/chapter/10.1007/978-3-540-24650-3_1)*. [EuroGP 2004](http://www.informatik.uni-trier.de/~ley/db/conf/eurogp/eurogp2004.html#AutonesBCLLS04) [[70]](#cite_note-70)
* [Daniel Walker](index.php?title=Daniel_Walker&action=edit&redlink=1 "Daniel Walker (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2004**). *The MORPH Project in 2004*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")


**2006**



* [Holk Cruse](index.php?title=Holk_Cruse&action=edit&redlink=1 "Holk Cruse (page does not exist)") (**2006**). *[Neural Networks as Cybernetic Systems](http://www.brains-minds-media.org/archive/615)*. 2nd and revised edition, [Department of Biological Cybernetics](http://www.uni-bielefeld.de/biologie/Kybernetik/), [Bielefeld University](https://en.wikipedia.org/wiki/Bielefeld_University)
* [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Simon Osindero](https://www.linkedin.com/in/osindero), [Yee Whye Teh](https://scholar.google.com/citations?user=y-nUzMwAAAAJ) (**2006**). *[A Fast Learning Algorithm for Deep Belief Nets](http://www.mitpressjournals.org/doi/abs/10.1162/neco.2006.18.7.1527)*. [Neural Computation](https://en.wikipedia.org/wiki/Neural_Computation_(journal)), Vol. 18, No. 7, [pdf](https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf)
* [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Ruslan R. Salakhutdinov](Mathematician#RRSalakhutdinov "Mathematician") (**2006**). *Reducing the Dimensionality of Data with Neural Networks*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 313, [pdf](https://www.cs.toronto.edu/~hinton/science.pdf)


**2007**



* [Edward P. Manning](index.php?title=Edward_P._Manning&action=edit&redlink=1 "Edward P. Manning (page does not exist)") (**2007**). *[Temporal Difference Learning of an Othello Evaluation Function for a Small Neural Network with Shared Weights](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=4219046)*. [IEEE Symposium on Computational Intelligence and AI in Games](IEEE#CIG "IEEE")
* [Yong Duan](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/d/Duan:Yong.html), [Baoxia Cui](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/c/Cui:Baoxia.html), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2007**). *State Space Partition for Reinforcement Learning Based on Fuzzy Min-Max Neural Network*. [ISNN 2007](http://www.informatik.uni-trier.de/~ley/db/conf/isnn/isnn2007-2.html#DuanCX07)
* [David Kriesel](http://www.dkriesel.com/en/start) (**2007**). *[A Brief Introduction to Neural Networks](http://www.dkriesel.com/en/science/neural_networks)*. available at [[1]](http://www.dkriesel.com)
* [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt") (**2007**). *Applying Backpropagation Networks to Anaphor Resolution*. In: [António Branco](http://www.di.fc.ul.pt/%7Eahb/) (Ed.), *[Anaphora: Analysis, Algorithms, and Applications](http://www.springer.com/computer/ai/book/978-3-540-71411-8)*. Selected Papers of the [6th Discourse Anaphora and Anaphor Resolution Colloquium, DAARC 2007](http://daarc2007.di.fc.ul.pt/), [Lagos, Portugal](https://en.wikipedia.org/wiki/Lagos,_Portugal)


**2008**



* [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Vinod Nair](index.php?title=Vinod_Nair&action=edit&redlink=1 "Vinod Nair (page does not exist)") (**2008**). *Mimicking Go Experts with Convolutional Neural Networks*. [ICANN 2008](http://dblp.uni-trier.de/db/conf/icann/icann2008-2.html#SutskeverN08), [pdf](http://www.cs.utoronto.ca/~ilya/pubs/2008/go_paper.pdf)
* [Simon S. Haykin](https://en.wikipedia.org/wiki/Simon_Haykin) (**2008**). *[Neural Networks: A Comprehensive Foundation](http://www.amazon.com/Neural-Networks-Learning-Machines-Edition/dp/0131471392)*. 3rd Edition, [[2]](https://en.wikipedia.org/wiki/Prentice_HallPrentice-Hall)
* [Toshinori Munakata](Toshinori_Munakata "Toshinori Munakata") (**2008**). *[Fundamentals of the New Artificial Intelligence: Neural, Evolutionary, Fuzzy and More](http://link.springer.com/book/10.1007/978-1-84628-839-5)*. 2nd edition, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [1st edition 1998](Neural_Networks#FundamentalsNAI1st "Neural Networks")
* [Byoung-Tak Zhang](Byoung-Tak_Zhang "Byoung-Tak Zhang") (**2008**). *Hypernetworks: A molecular evolutionary architecture for cognitive learning and memory*. [IEEE Computational Intelligence Magazine](IEEE "IEEE"), Vol. 3, No. 3, [pdf](https://bi.snu.ac.kr/Publications/Journals/International/IEEE_Comp_Int_3_Zhang.pdf)
* [Qing Song](http://dblp.uni-trier.de/pers/hd/s/Song_0001:Qing), [James C. Spall](James_C._Spall "James C. Spall"), [Yeng Chai Soh](http://dblp.uni-trier.de/pers/hd/s/Soh:Yeng_Chai), [Jie Ni](http://dblp.uni-trier.de/pers/hd/n/Ni:Jie) (**2008**). *Robust Neural Network Tracking Controller Using Simultaneous Perturbation Stochastic Approximation*. [IEEE Transactions on Neural Networks](IEEE#NN "IEEE"), Vol. 19, No. 5, [2003 pdf](https://pdfs.semanticscholar.org/3f2a/4d69ca8adbbc072d82af58b3c750621d36ab.pdf) » [SPSA](SPSA "SPSA")


**2009**



* [Daniel Abdi](Daniel_Shawul "Daniel Shawul"), Simon Levine, [Girma T. Bitsuamlak](http://www.eng.uwo.ca/civil/faculty/bitsuamlak_g/index.html) (**2009**). *Application of an Artificial Neural Network Model for Boundary Layer Wind Tunnel Profile Development*. 11th Americas conference on wind Engineering, [pdf](http://www.iawe.org/Proceedings/11ACWE/11ACWE-Abdi.pdf)


### 2010 ...


* [Ian Stewart](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/s/Stewart:Ian.html), [Wenying Feng](http://people.trentu.ca/wfeng/), [Selim Akl](Selim_Akl "Selim Akl") (**2010**). *Tuning Neural Networks by Both Connectivity and Size*. [ITNG 2010](http://www.informatik.uni-trier.de/~ley/db/conf/itng/itng2010.html#StewartFA10)


**2011**



* [Jonathan K. Vis](index.php?title=Jonathan_K._Vis&action=edit&redlink=1 "Jonathan K. Vis (page does not exist)") (**2011**). *Discrete Tomography: A Neural Network Approach*. Master's thesis, [Leiden University](Leiden_University "Leiden University"), [pdf](http://www.liacs.nl/~jvis/thesis.pdf)
* [Jonathan K. Vis](index.php?title=Jonathan_K._Vis&action=edit&redlink=1 "Jonathan K. Vis (page does not exist)"), [Walter Kosters](Walter_Kosters "Walter Kosters"), [Joost Batenburg](Joost_Batenburg "Joost Batenburg") (**2011**). *Discrete Tomography: A Neural Network Approach*. [BNAIC 2011](http://allserv.kahosl.be/bnaic2011/) [pdf](http://www.liacs.nl/~jvis/bnaic2011.pdf)
* [Nikolaos Papahristou](index.php?title=Nikolaos_Papahristou&action=edit&redlink=1 "Nikolaos Papahristou (page does not exist)"), [Ioannis Refanidis](index.php?title=Ioannis_Refanidis&action=edit&redlink=1 "Ioannis Refanidis (page does not exist)") (**2011**). *Training Neural Networks to Play Backgammon Variants Using Reinforcement Learning*. Proceedings of [Evogames 2011](http://conference.researchbib.com/?eventid=6400), Part I, LNCS 6624, [pdf](http://ai.uom.gr/nikpapa/publications/Training%20NN%20to%20Play%20Backgammon%20Variants%20Using%20RL.pdf)


**2012**



* [Sjoerd van den Dries](http://dblp.uni-trier.de/pers/hd/d/Dries:Sjoerd_van_den), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2012**). *Neural-fitted TD-leaf learning for playing Othello with structured neural networks*. [IEEE Transactions on Neural Networks and Learning Systems](IEEE#NN "IEEE"), Vol. 23, No. 11
* [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber"), [Faustino Gomez](http://www.idsia.ch/%7Etino/), [Santiago Fernández](http://www.idsia.ch/%7Esantiago/), [Alex Graves](http://www6.in.tum.de/Main/Graves), [Sepp Hochreiter](http://www.bioinf.jku.at/people/hochreiter/) (**2012**). *[Sequence Learning with Artificial Recurrent Neural Networks](http://www.idsia.ch/%7Ejuergen/rnnbook.html)*. (Aiming to become the definitive textbook on RNN.) Invited by [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
* [Peter McLeod](index.php?title=Peter_McLeod&action=edit&redlink=1 "Peter McLeod (page does not exist)"), [Brijesh Verma](http://content.cqu.edu.au/FCWViewer/staff.do?site=1829&sid=VERMAB) (**2012**). *[Clustered ensemble neural network for breast mass classification in digital mammography](http://ieeexplore.ieee.org/xpl/articleDetails.jsp;jsessionid=brTRQwvWb1pVpRlZ4K3pymTDhkp8FLyKpkZ1pT9XQTPr7GDpnG4C!58582823?arnumber=6252539&contentType=Conference+Publications)*. [IJCNN 2012](http://www.informatik.uni-trier.de/~ley/db/conf/ijcnn/ijcnn2012.html#McLeodV12)
* [Grégoire Montavon](Mathematician#GMontavon "Mathematician"), [Geneviève B. Orr](http://www.researchgate.net/profile/Genevieve_Orr), [Klaus-Robert Müller](Mathematician#KRMueller "Mathematician") (eds.) (**2012**). *[Neural Networks: Tricks of the Trade](http://link.springer.com/book/10.1007/978-3-642-35289-8)*. (2nd Edition) [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 7700, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


 [Nicol N. Schraudolph](Nicol_N._Schraudolph "Nicol N. Schraudolph") (**2012**). *[Centering Neural Network Gradient Factors](http://link.springer.com/chapter/10.1007/978-3-642-35289-8_14)*.
 [Léon Bottou](https://en.wikipedia.org/wiki/L%C3%A9on_Bottou) (**2012**). *[Stochastic Gradient Descent Tricks](http://link.springer.com/chapter/10.1007/978-3-642-35289-8_25)*. [Microsoft Research](https://en.wikipedia.org/wiki/Microsoft_Research), [pdf](http://cilvr.cs.nyu.edu/diglib/lsml/bottou-sgd-tricks-2012.pdf)
 [Ronan Collobert](index.php?title=Ronan_Collobert&action=edit&redlink=1 "Ronan Collobert (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Clément Farabet](index.php?title=Cl%C3%A9ment_Farabet&action=edit&redlink=1 "Clément Farabet (page does not exist)") (**2012**). *[Implementing Neural Networks Efficiently](http://link.springer.com/chapter/10.1007%2F978-3-642-35289-8_28)*. [[71]](#cite_note-71)
**2013**



* [Grégoire Montavon](Mathematician#GMontavon "Mathematician") (**2013**). *[On Layer-Wise Representations in Deep Neural Networks](https://opus4.kobv.de/opus4-tuberlin/frontdoor/index/index/docId/4467)*. Ph.D. Thesis, [TU Berlin](https://en.wikipedia.org/wiki/Technical_University_of_Berlin), advisor [Klaus-Robert Müller](Mathematician#KRMueller "Mathematician")
* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Daan Wierstra](index.php?title=Daan_Wierstra&action=edit&redlink=1 "Daan Wierstra (page does not exist)"), [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)") (**2013**). *Playing Atari with Deep Reinforcement Learning*. [arXiv:1312.5602](http://arxiv.org/abs/1312.5602) [[72]](#cite_note-72)
* [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2013**). *Evolving Neural Networks*. [IJCNN 2013](https://dblp.org/db/conf/ijcnn/ijcnn2013), [pdf](http://nn.cs.utexas.edu/downloads/slides/miikkulainen.ijcnn13.pdf)


**2014**



* [Yann Dauphin](Mathematician#YDauphin "Mathematician"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Caglar Gulcehre](Mathematician#CGulcehre "Mathematician"), [Kyunghyun Cho](Mathematician#KCho "Mathematician"), [Surya Ganguli](Mathematician#SGanguli "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician") (**2014**). *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization*. [arXiv:1406.2572](https://arxiv.org/abs/1406.2572) [[73]](#cite_note-73)
* [Ian Goodfellow](Mathematician#IGoodfellow "Mathematician"), [Jean Pouget-Abadie](index.php?title=Jean_Pouget-Abadie&action=edit&redlink=1 "Jean Pouget-Abadie (page does not exist)"), [Mehdi Mirza](index.php?title=Mehdi_Mirza&action=edit&redlink=1 "Mehdi Mirza (page does not exist)"), [Bing Xu](index.php?title=Bing_Xu&action=edit&redlink=1 "Bing Xu (page does not exist)"), [David Warde-Farley](index.php?title=David_Warde-Farley&action=edit&redlink=1 "David Warde-Farley (page does not exist)"), [Sherjil Ozair](index.php?title=Sherjil_Ozair&action=edit&redlink=1 "Sherjil Ozair (page does not exist)"), [Aaron Courville](Mathematician#ACourville "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician") (**2014**). *Generative Adversarial Networks*. [arXiv:1406.2661v1](https://arxiv.org/abs/1406.2661v1) [[74]](#cite_note-74)
* [Christopher Clark](Christopher_Clark "Christopher Clark"), [Amos Storkey](Amos_Storkey "Amos Storkey") (**2014**). *Teaching Deep Convolutional Neural Networks to Play Go*. [arXiv:1412.3409](http://arxiv.org/abs/1412.3409) [[75]](#cite_note-75) [[76]](#cite_note-76)
* [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [David Silver](David_Silver "David Silver") (**2014**). *Move Evaluation in Go Using Deep Convolutional Neural Networks*. [arXiv:1412.6564v1](http://arxiv.org/abs/1412.6564v1) » [Go](Go "Go")
* [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Oriol Vinyals](index.php?title=Oriol_Vinyals&action=edit&redlink=1 "Oriol Vinyals (page does not exist)"), [Quoc V. Le](index.php?title=Quoc_V._Le&action=edit&redlink=1 "Quoc V. Le (page does not exist)") (**2014**). *Sequence to Sequence Learning with Neural Networks*. [arXiv:1409.3215](https://arxiv.org/abs/1409.3215)


**2015**



* [Diederik P. Kingma](https://scholar.google.nl/citations?user=yyIoQu4AAAAJ), [Jimmy Lei Ba](https://scholar.google.ca/citations?user=ymzxRhAAAAAJ&hl=en) (**2015**). *Adam: A Method for Stochastic Optimization*. [arXiv:1412.6980v8](https://arxiv.org/abs/1412.6980v8), [ICLR 2015](http://www.iclr.cc/doku.php?id=iclr2015:main) [[77]](#cite_note-77)
* [Michael Nielsen](http://michaelnielsen.org/) (**2015**). *[Neural networks and deep learning](http://neuralnetworksanddeeplearning.com/)*. Determination Press
* [Sergey Ioffe](Mathematician#SIoffe "Mathematician"), [Christian Szegedy](Mathematician#CSzegedy "Mathematician") (**2015**). *Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift*. [arXiv:1502.03167](https://arxiv.org/abs/1502.03167)
* [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician"), [Oriol Vinyals](index.php?title=Oriol_Vinyals&action=edit&redlink=1 "Oriol Vinyals (page does not exist)"), [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean_(computer_scientist)) (**2015**). *Distilling the Knowledge in a Neural Network*. [arXiv:1503.02531](https://arxiv.org/abs/1503.02531)
* [James L. McClelland](index.php?title=James_L._McClelland&action=edit&redlink=1 "James L. McClelland (page does not exist)") (**2015**). *[Explorations in Parallel Distributed Processing: A Handbook of Models, Programs, and Exercises](https://web.stanford.edu/group/pdplab/pdphandbook/handbook3.html#handbookch10.html)*. Second Edition, [Contents](https://web.stanford.edu/group/pdplab/pdphandbook/handbookli1.html)
* [Gábor Melis](index.php?title=G%C3%A1bor_Melis&action=edit&redlink=1 "Gábor Melis (page does not exist)") (**2015**). *[Dissecting the Winning Solution of the HiggsML Challenge](http://jmlr.org/proceedings/papers/v42/meli14.html)*. [NIPS 2014](https://nips.cc/Conferences/2014)
* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [David Silver](David_Silver "David Silver"), [Andrei A. Rusu](Mathematician#AARusu "Mathematician"), [Joel Veness](Joel_Veness "Joel Veness"), [Marc G. Bellemare](index.php?title=Marc_G._Bellemare&action=edit&redlink=1 "Marc G. Bellemare (page does not exist)"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Martin Riedmiller](index.php?title=Martin_Riedmiller&action=edit&redlink=1 "Martin Riedmiller (page does not exist)"), [Andreas K. Fidjeland](index.php?title=Andreas_K._Fidjeland&action=edit&redlink=1 "Andreas K. Fidjeland (page does not exist)"), [Georg Ostrovski](index.php?title=Georg_Ostrovski&action=edit&redlink=1 "Georg Ostrovski (page does not exist)"), [Stig Petersen](index.php?title=Stig_Petersen&action=edit&redlink=1 "Stig Petersen (page does not exist)"), [Charles Beattie](index.php?title=Charles_Beattie&action=edit&redlink=1 "Charles Beattie (page does not exist)"), [Amir Sadik](index.php?title=Amir_Sadik&action=edit&redlink=1 "Amir Sadik (page does not exist)"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Helen King](index.php?title=Helen_King&action=edit&redlink=1 "Helen King (page does not exist)"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Daan Wierstra](index.php?title=Daan_Wierstra&action=edit&redlink=1 "Daan Wierstra (page does not exist)"), [Shane Legg](index.php?title=Shane_Legg&action=edit&redlink=1 "Shane Legg (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2015**). *[Human-level control through deep reinforcement learning](http://www.nature.com/nature/journal/v518/n7540/abs/nature14236.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 518
* [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**2015**). *[Deep Learning in Neural Networks: An Overview](http://people.idsia.ch/~juergen/deep-learning-overview.html)*. [Neural Networks](https://en.wikipedia.org/wiki/Neural_Networks_(journal)), Vol. 61
* [Zachary C. Lipton](https://scholar.google.fr/citations?user=MN9Kfg8AAAAJ&hl=en), [John Berkowitz](https://www.linkedin.com/in/john-berkowitz-92b24a7b), [Charles Elkan](Charles_Elkan "Charles Elkan") (**2015**). *A Critical Review of Recurrent Neural Networks for Sequence Learning*. [arXiv:1506.00019v4](https://arxiv.org/abs/1506.00019)
* [Douglas Bagnall](Douglas_Bagnall "Douglas Bagnall") (**2015**). *Author Identification using Multi-headed Recurrent Neural Networks*. [arXiv:1506.04891](https://arxiv.org/abs/1506.04891)
* [Guillaume Desjardins](index.php?title=Guillaume_Desjardins&action=edit&redlink=1 "Guillaume Desjardins (page does not exist)"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu") (**2015**). *Natural Neural Networks*. [arXiv:1507.00210](https://arxiv.org/abs/1507.00210)
* [Barak Oshri](Barak_Oshri "Barak Oshri"), [Nishith Khandwala](Nishith_Khandwala "Nishith Khandwala") (**2015**). *Predicting Moves in Chess using Convolutional Neural Networks*. [pdf](http://vision.stanford.edu/teaching/cs231n/reports/2015/pdfs/ConvChess.pdf) [[78]](#cite_note-78) [[79]](#cite_note-79)
* [Yann LeCun](Mathematician#YLeCun "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician"), [Geoffrey E. Hinton](Mathematician#GEHinton "Mathematician") (**2015**). *[Deep Learning](http://www.nature.com/nature/journal/v521/n7553/full/nature14539.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 521 [[80]](#cite_note-80)
* [Matthew Lai](Matthew_Lai "Matthew Lai") (**2015**). *Giraffe: Using Deep Reinforcement Learning to Play Chess*. M.Sc. thesis, [Imperial College London](https://en.wikipedia.org/wiki/Imperial_College_London), [arXiv:1509.01549v1](http://arxiv.org/abs/1509.01549v1) » [Giraffe](Giraffe "Giraffe")
* [Nikolai Yakovenko](index.php?title=Nikolai_Yakovenko&action=edit&redlink=1 "Nikolai Yakovenko (page does not exist)"), [Liangliang Cao](index.php?title=Liangliang_Cao&action=edit&redlink=1 "Liangliang Cao (page does not exist)"), [Colin Raffel](index.php?title=Colin_Raffel&action=edit&redlink=1 "Colin Raffel (page does not exist)"), [James Fan](index.php?title=James_Fan&action=edit&redlink=1 "James Fan (page does not exist)") (**2015**). *Poker-CNN: A Pattern Learning Strategy for Making Draws and Bets in Poker Games*. [arXiv:1509.06731](https://arxiv.org/abs/1509.06731)
* [Emmanuel Bengio](https://scholar.google.ca/citations?user=yVtSOt8AAAAJ&hl=en), [Pierre-Luc Bacon](https://scholar.google.ca/citations?user=9H77FYYAAAAJ&hl=en), [Joelle Pineau](Joelle_Pineau "Joelle Pineau"), [Doina Precup](Doina_Precup "Doina Precup") (**2015**). *Conditional Computation in Neural Networks for faster models*. [arXiv:1511.06297](https://arxiv.org/abs/1511.06297)
* [Ilya Loshchilov](Ilya_Loshchilov "Ilya Loshchilov"), [Frank Hutter](Frank_Hutter "Frank Hutter") (**2015**). *Online Batch Selection for Faster Training of Neural Networks*. [arXiv:1511.06343](https://arxiv.org/abs/1511.06343)
* [Yuandong Tian](index.php?title=Yuandong_Tian&action=edit&redlink=1 "Yuandong Tian (page does not exist)"), [Yan Zhu](index.php?title=Yan_Zhu&action=edit&redlink=1 "Yan Zhu (page does not exist)") (**2015**). *Better Computer Go Player with Neural Network and Long-term Prediction*. [arXiv:1511.06410](http://arxiv.org/abs/1511.06410) [[81]](#cite_note-81) [[82]](#cite_note-82) » [Go](Go "Go")
* [Peter H. Jin](index.php?title=Peter_H._Jin&action=edit&redlink=1 "Peter H. Jin (page does not exist)"), [Kurt Keutzer](index.php?title=Kurt_Keutzer&action=edit&redlink=1 "Kurt Keutzer (page does not exist)") (**2015**). *Convolutional Monte Carlo Rollouts in Go*. [arXiv:1512.03375](http://arxiv.org/abs/1512.03375)
* [Kaiming He](https://scholar.google.com/citations?user=DhtAFkwAAAAJ), [Xiangyu Zhang](https://scholar.google.com/citations?user=yuB-cfoAAAAJ&hl=en), [Shaoqing Ren](http://shaoqingren.com/), [Jian Sun](http://www.jiansun.org/) (**2015**). *Deep Residual Learning for Image Recognition*. [arXiv:1512.03385](https://arxiv.org/abs/1512.03385)
* [Nicolas Heess](index.php?title=Nicolas_Heess&action=edit&redlink=1 "Nicolas Heess (page does not exist)"), [Jonathan J. Hunt](index.php?title=Jonathan_J._Hunt&action=edit&redlink=1 "Jonathan J. Hunt (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2015**). *Memory-based control with recurrent neural networks*. [arXiv:1512.04455](https://arxiv.org/abs/1512.04455)


**2016**



* [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [James L. McClelland](index.php?title=James_L._McClelland&action=edit&redlink=1 "James L. McClelland (page does not exist)") (**2016**). *What learning systems do intelligent agents need? Complementary Learning Systems Theory Updated*. [Trends in Cognitive Sciences](https://en.wikipedia.org/wiki/Trends_in_Cognitive_Sciences), Vol. 20, No. 7, [pdf](https://drive.google.com/file/d/0B-Nvsz4idhaeVEZYMEVaWkFjLVU/view)
* [Ziyu Wang](index.php?title=Ziyu_Wang&action=edit&redlink=1 "Ziyu Wang (page does not exist)"), [Nando de Freitas](index.php?title=Nando_de_Freitas&action=edit&redlink=1 "Nando de Freitas (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot") (**2016**). *Dueling Network Architectures for Deep Reinforcement Learning*. [arXiv:1511.06581](http://arxiv.org/abs/1511.06581)
* [David Silver](David_Silver "David Silver"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Sander Dieleman](index.php?title=Sander_Dieleman&action=edit&redlink=1 "Sander Dieleman (page does not exist)"), [Dominik Grewe](index.php?title=Dominik_Grewe&action=edit&redlink=1 "Dominik Grewe (page does not exist)"), [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)"), [Nal Kalchbrenner](index.php?title=Nal_Kalchbrenner&action=edit&redlink=1 "Nal Kalchbrenner (page does not exist)"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Madeleine Leach](index.php?title=Madeleine_Leach&action=edit&redlink=1 "Madeleine Leach (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2016**). *[Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 529 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
* [Tobias Graf](index.php?title=Tobias_Graf&action=edit&redlink=1 "Tobias Graf (page does not exist)"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)") (**2016**). *Using Deep Convolutional Neural Networks in Monte Carlo Tree Search*. [CG 2016](CG_2016 "CG 2016")
* [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang") (**2016**). *[AlphaGo: Combining Deep Neural Networks with Tree Search](CG_2016#Keynote "CG 2016")*. [CG 2016](CG_2016 "CG 2016"), Keynote Lecture
* [Peter H. Jin](index.php?title=Peter_H._Jin&action=edit&redlink=1 "Peter H. Jin (page does not exist)") , [Kurt Keutzer](index.php?title=Kurt_Keutzer&action=edit&redlink=1 "Kurt Keutzer (page does not exist)") (**2016**). *Convolutional Monte Carlo Rollouts for Computer Go*. [CG 2016](CG_2016 "CG 2016")
* [Hung Guei](index.php?title=Hung_Guei&action=edit&redlink=1 "Hung Guei (page does not exist)"), [Tinghan Wei](index.php?title=Tinghan_Wei&action=edit&redlink=1 "Tinghan Wei (page does not exist)"), [Jin-Bo Huang](index.php?title=Jin-Bo_Huang&action=edit&redlink=1 "Jin-Bo Huang (page does not exist)"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu") (**2016**). *An Empirical Study on Applying Deep Reinforcement Learning to the Game 2048*. [CG 2016](CG_2016 "CG 2016")
* [Omid E. David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu"), [Lior Wolf](index.php?title=Lior_Wolf&action=edit&redlink=1 "Lior Wolf (page does not exist)") (**2016**). *[DeepChess: End-to-End Deep Neural Network for Automatic Learning in Chess](http://link.springer.com/chapter/10.1007%2F978-3-319-44781-0_11)*. [ICAAN 2016](http://icann2016.org/), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 9887, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf preprint](http://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf) » [DeepChess](index.php?title=DeepChess&action=edit&redlink=1 "DeepChess (page does not exist)") [[83]](#cite_note-83) [[84]](#cite_note-84)
* [Dror Sholomon](index.php?title=Dror_Sholomon&action=edit&redlink=1 "Dror Sholomon (page does not exist)"), [Omid E. David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2016**). *[DNN-Buddies: A Deep Neural Network-Based Estimation Metric for the Jigsaw Puzzle Problem](http://link.springer.com/chapter/10.1007/978-3-319-44781-0_21)*. [ICAAN 2016](http://icann2016.org/), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 9887, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media) [[85]](#cite_note-85)
* [Ian Goodfellow](Mathematician#IGoodfellow "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician"), [Aaron Courville](Mathematician#ACourville "Mathematician") (**2016**). *[Deep Learning](http://www.deeplearningbook.org/)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Volodymyr Mnih](Volodymyr_Mnih "Volodymyr Mnih"), [Adrià Puigdomènech Badia](index.php?title=Adri%C3%A0_Puigdom%C3%A8nech_Badia&action=edit&redlink=1 "Adrià Puigdomènech Badia (page does not exist)"), [Mehdi Mirza](index.php?title=Mehdi_Mirza&action=edit&redlink=1 "Mehdi Mirza (page does not exist)"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Tim Harley](index.php?title=Tim_Harley&action=edit&redlink=1 "Tim Harley (page does not exist)"), [David Silver](David_Silver "David Silver"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu") (**2016**). *Asynchronous Methods for Deep Reinforcement Learning*. [arXiv:1602.01783v2](https://arxiv.org/abs/1602.01783)
* [Vincent Dumoulin](https://scholar.google.ca/citations?user=mZfgLA4AAAAJ&hl=en), [Francesco Visin](https://scholar.google.it/citations?user=kaAnZw0AAAAJ&hl=en) (**2016**). *A guide to convolution arithmetic for deep learning*. [arXiv:1603.07285](https://arxiv.org/abs/1603.07285)
* [Patricia Churchland](https://en.wikipedia.org/wiki/Patricia_Churchland), [Terrence J. Sejnowski](Terrence_J._Sejnowski "Terrence J. Sejnowski") (**2016**). *[The Computational Brain, 25th Anniversary Edition](https://mitpress.mit.edu/books/computational-brain-0)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
* [Ilya Loshchilov](Ilya_Loshchilov "Ilya Loshchilov"), [Frank Hutter](Frank_Hutter "Frank Hutter") (**2016**). *CMA-ES for Hyperparameter Optimization of Deep Neural Networks*. [arXiv:1604.07269](https://arxiv.org/abs/1604.07269) [[86]](#cite_note-86)
* [Audrūnas Gruslys](index.php?title=Audr%C5%ABnas_Gruslys&action=edit&redlink=1 "Audrūnas Gruslys (page does not exist)"), [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos"), [Ivo Danihelka](index.php?title=Ivo_Danihelka&action=edit&redlink=1 "Ivo Danihelka (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Alex Graves](index.php?title=Alex_Graves&action=edit&redlink=1 "Alex Graves (page does not exist)") (**2016**). *Memory-Efficient Backpropagation Through Time*. [arXiv:1606.03401](https://arxiv.org/abs/1606.03401v1)
* [Andrei A. Rusu](Mathematician#AARusu "Mathematician"), [Neil C. Rabinowitz](index.php?title=Neil_C._Rabinowitz&action=edit&redlink=1 "Neil C. Rabinowitz (page does not exist)"), [Guillaume Desjardins](index.php?title=Guillaume_Desjardins&action=edit&redlink=1 "Guillaume Desjardins (page does not exist)"), [Hubert Soyer](index.php?title=Hubert_Soyer&action=edit&redlink=1 "Hubert Soyer (page does not exist)"), [James Kirkpatrick](index.php?title=James_Kirkpatrick&action=edit&redlink=1 "James Kirkpatrick (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Raia Hadsell](Mathematician#RHadsell "Mathematician") (**2016**). *Progressive Neural Networks*. [arXiv:1606.04671](https://arxiv.org/abs/1606.04671)
* [Douglas Bagnall](Douglas_Bagnall "Douglas Bagnall") (**2016**). *Authorship clustering using multi-headed recurrent neural networks*. [arXiv:1608.04485](https://arxiv.org/abs/1608.04485)
* [Gao Huang](index.php?title=Gao_Huang&action=edit&redlink=1 "Gao Huang (page does not exist)"), [Zhuang Liu](index.php?title=Zhuang_Liu&action=edit&redlink=1 "Zhuang Liu (page does not exist)"), [Laurens van der Maaten](index.php?title=Laurens_van_der_Maaten&action=edit&redlink=1 "Laurens van der Maaten (page does not exist)"), [Kilian Q. Weinberger](index.php?title=Kilian_Q._Weinberger&action=edit&redlink=1 "Kilian Q. Weinberger (page does not exist)") (**2016**). *Densely Connected Convolutional Networks*. [arXiv:1608.06993](https://arxiv.org/abs/1608.06993) [[87]](#cite_note-87)
* [George Rajna](George_Rajna "George Rajna") (**2016**). *Deep Neural Networks*. [viXra:1609.0126](http://vixra.org/abs/1609.0126)
* [James Kirkpatrick](index.php?title=James_Kirkpatrick&action=edit&redlink=1 "James Kirkpatrick (page does not exist)"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Neil C. Rabinowitz](index.php?title=Neil_C._Rabinowitz&action=edit&redlink=1 "Neil C. Rabinowitz (page does not exist)"), [Joel Veness](Joel_Veness "Joel Veness"), [Guillaume Desjardins](index.php?title=Guillaume_Desjardins&action=edit&redlink=1 "Guillaume Desjardins (page does not exist)"), [Andrei A. Rusu](Mathematician#AARusu "Mathematician"), [Kieran Milan](index.php?title=Kieran_Milan&action=edit&redlink=1 "Kieran Milan (page does not exist)"), [John Quan](index.php?title=John_Quan&action=edit&redlink=1 "John Quan (page does not exist)"), [Tiago Ramalho](index.php?title=Tiago_Ramalho&action=edit&redlink=1 "Tiago Ramalho (page does not exist)"), [Agnieszka Grabska-Barwinska](index.php?title=Agnieszka_Grabska-Barwinska&action=edit&redlink=1 "Agnieszka Grabska-Barwinska (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Claudia Clopath](index.php?title=Claudia_Clopath&action=edit&redlink=1 "Claudia Clopath (page does not exist)"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Raia Hadsell](Mathematician#RHadsell "Mathematician") (**2016**). *Overcoming catastrophic forgetting in neural networks*. [arXiv:1612.00796](https://arxiv.org/abs/1612.00796) [[88]](#cite_note-88)
* [Zhenxing Niu](https://dblp.uni-trier.de/pers/hd/n/Niu:Zhenxing), [Mo Zhou](https://dblp.uni-trier.de/pers/hd/z/Zhou:Mo), [Le Wang](https://dblp.uni-trier.de/pers/hd/w/Wang_0003:Le), [Xinbo Gao](Xinbo_Gao "Xinbo Gao"), [Gang Hua](https://dblp.uni-trier.de/pers/hd/h/Hua_0001:Gang) (**2016**). *Ordinal Regression with Multiple Output CNN for Age Estimation*. [CVPR 2016](https://dblp.uni-trier.de/db/conf/cvpr/cvpr2016.html), [pdf](https://www.cv-foundation.org/openaccess/content_cvpr_2016/app/S21-20.pdf)
* [Li Jing](index.php?title=Li_Jing&action=edit&redlink=1 "Li Jing (page does not exist)"), [Yichen Shen](index.php?title=Yichen_Shen&action=edit&redlink=1 "Yichen Shen (page does not exist)"), [Tena Dubček](index.php?title=Tena_Dub%C4%8Dek&action=edit&redlink=1 "Tena Dubček (page does not exist)"), [John Peurifoy](index.php?title=John_Peurifoy&action=edit&redlink=1 "John Peurifoy (page does not exist)"), [Scott Skirlo](index.php?title=Scott_Skirlo&action=edit&redlink=1 "Scott Skirlo (page does not exist)"), [Yann LeCun](Mathematician#YLeCun "Mathematician"), [Max Tegmark](index.php?title=Max_Tegmark&action=edit&redlink=1 "Max Tegmark (page does not exist)"), [Marin Soljačić](index.php?title=Marin_Solja%C4%8Di%C4%87&action=edit&redlink=1 "Marin Soljačić (page does not exist)") (**2016**). *Tunable Efficient Unitary Neural Networks (EUNN) and their application to RNNs*. [arXiv:1612.05231](https://arxiv.org/abs/1612.05231)


**2017**



* [Yutian Chen](index.php?title=Yutian_Chen&action=edit&redlink=1 "Yutian Chen (page does not exist)"), [Matthew W. Hoffman](index.php?title=Matthew_W._Hoffman&action=edit&redlink=1 "Matthew W. Hoffman (page does not exist)"), [Sergio Gomez Colmenarejo](index.php?title=Sergio_Gomez_Colmenarejo&action=edit&redlink=1 "Sergio Gomez Colmenarejo (page does not exist)"), [Misha Denil](index.php?title=Misha_Denil&action=edit&redlink=1 "Misha Denil (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Matthew Botvinick](index.php?title=Matthew_Botvinick&action=edit&redlink=1 "Matthew Botvinick (page does not exist)"), [Nando de Freitas](index.php?title=Nando_de_Freitas&action=edit&redlink=1 "Nando de Freitas (page does not exist)") (**2017**). *Learning to Learn without Gradient Descent by Gradient Descent*. [arXiv:1611.03824v6](https://arxiv.org/abs/1611.03824v6), [ICML 2017](http://dblp.uni-trier.de/db/conf/icml/icml2017.html)
* [Brian Chu](https://dblp.org/pers/hd/c/Chu:Brian), [Daylen Yang](Daylen_Yang "Daylen Yang"), [Ravi Tadinada](https://dblp.org/pers/hd/t/Tadinada:Ravi) (**2017**). *Visualizing Residual Networks*. [arXiv:1701.02362](https://arxiv.org/abs/1701.02362)
* [Muthuraman Chidambaram](index.php?title=Muthuraman_Chidambaram&action=edit&redlink=1 "Muthuraman Chidambaram (page does not exist)"), [Yanjun Qi](index.php?title=Yanjun_Qi&action=edit&redlink=1 "Yanjun Qi (page does not exist)") (**2017**). *Style Transfer Generative Adversarial Networks: Learning to Play Chess Differently*. [arXiv:1702.06762v1](https://arxiv.org/abs/1702.06762v1) [[89]](#cite_note-89)
* [George Rajna](George_Rajna "George Rajna") (**2017**). *Artificial Neural Network*. [viXra:1702.0130](http://vixra.org/abs/1702.0130)
* [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2017**). *Deepest Neural Networks*. [arXiv:1707.02617](https://arxiv.org/abs/1707.02617)
* [Matej Moravčík](index.php?title=Matej_Morav%C4%8D%C3%ADk&action=edit&redlink=1 "Matej Moravčík (page does not exist)"), [Martin Schmid](Mathematician#MSchmid "Mathematician"), [Neil Burch](index.php?title=Neil_Burch&action=edit&redlink=1 "Neil Burch (page does not exist)"), [Viliam Lisý](index.php?title=Viliam_Lis%C3%BD&action=edit&redlink=1 "Viliam Lisý (page does not exist)"), [Dustin Morrill](index.php?title=Dustin_Morrill&action=edit&redlink=1 "Dustin Morrill (page does not exist)"), [Nolan Bard](index.php?title=Nolan_Bard&action=edit&redlink=1 "Nolan Bard (page does not exist)"), [Trevor Davis](index.php?title=Trevor_Davis&action=edit&redlink=1 "Trevor Davis (page does not exist)"), [Kevin Waugh](index.php?title=Kevin_Waugh&action=edit&redlink=1 "Kevin Waugh (page does not exist)"), [Michael Johanson](index.php?title=Michael_Johanson&action=edit&redlink=1 "Michael Johanson (page does not exist)"), [Michael Bowling](Michael_Bowling "Michael Bowling") (**2017**). *[DeepStack: Expert-level artificial intelligence in heads-up no-limit poker](http://science.sciencemag.org/content/356/6337/508)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 356, No. 6337
* [Xinqi Zhu](index.php?title=Xinqi_Zhu&action=edit&redlink=1 "Xinqi Zhu (page does not exist)"), [Michael Bain](Michael_Bain "Michael Bain") (**2017**). *B-CNN: Branch Convolutional Neural Network for Hierarchical Classification*. [arXiv:1709.09890](https://arxiv.org/abs/1709.09890), [GitHub - zhuxinqimac/B-CNN: Sample code of B-CNN paper](https://github.com/zhuxinqimac/B-CNN)
* [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli") (**2017**). *Learning to Play Chess with Minimal Lookahead and Deep Value Neural Networks*. Master's thesis, [University of Groningen](https://en.wikipedia.org/wiki/University_of_Groningen), [pdf](https://www.ai.rug.nl/~mwiering/Thesis_Matthia_Sabatelli.pdf) [[90]](#cite_note-90)
* [David Silver](David_Silver "David Silver"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Lucas Baker](index.php?title=Lucas_Baker&action=edit&redlink=1 "Lucas Baker (page does not exist)"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Adrian Bolton](index.php?title=Adrian_Bolton&action=edit&redlink=1 "Adrian Bolton (page does not exist)"), [Yutian Chen](index.php?title=Yutian_Chen&action=edit&redlink=1 "Yutian Chen (page does not exist)"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Fan Hui](index.php?title=Fan_Hui&action=edit&redlink=1 "Fan Hui (page does not exist)"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *[Mastering the game of Go without human knowledge](https://www.nature.com/nature/journal/v550/n7676/full/nature24270.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 550 [[91]](#cite_note-91)
* [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)  » [AlphaZero](Neural_Networks#AlphaZero "Neural Networks") [[92]](#cite_note-92)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2017**). *[Residual Networks for Computer Go](http://ieeexplore.ieee.org/document/7875402/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. PP, No. 99, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/resnet.pdf) [[93]](#cite_note-93)
* [Kei Takada](Kei_Takada "Kei Takada"), [Hiroyuki Iizuka](index.php?title=Hiroyuki_Iizuka&action=edit&redlink=1 "Hiroyuki Iizuka (page does not exist)"), [Masahito Yamamoto](index.php?title=Masahito_Yamamoto&action=edit&redlink=1 "Masahito Yamamoto (page does not exist)") (**2017**). *Reinforcement Learning for Creating Evaluation Function Using Convolutional Neural Network in Hex*. TAAI 2017 » [Hex](Hex "Hex")
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2017**). *Focused Depth-first Proof Number Search using Convolutional Neural Networks for the Game of Hex*. [IJCAI 2017](Conferences#IJCAI2017 "Conferences")
* [Thomas Elsken](index.php?title=Thomas_Elsken&action=edit&redlink=1 "Thomas Elsken (page does not exist)"), [Jan Hendrik Metzen](index.php?title=Jan_Hendrik_Metzen&action=edit&redlink=1 "Jan Hendrik Metzen (page does not exist)"), [Frank Hutter](Frank_Hutter "Frank Hutter") (**2017**). *Simple And Efficient Architecture Search for Convolutional Neural Networks*. [arXiv:1711.04528](https://arxiv.org/abs/1711.04528)
* [Joel Veness](Joel_Veness "Joel Veness"), [Tor Lattimore](Tor_Lattimore "Tor Lattimore"), [Avishkar Bhoopchand](https://github.com/avishkar58), [Agnieszka Grabska-Barwinska](https://scholar.google.co.uk/citations?user=mB4yebIAAAAJ&hl=en), [Christopher Mattern](https://dblp.org/pers/hd/m/Mattern:Christopher), [Peter Toth](https://dblp.org/pers/hd/t/Toth:Peter) (**2017**). *Online Learning with Gated Linear Networks*. [arXiv:1712.01897](https://arxiv.org/abs/1712.01897)
* [Qiming Chen](https://dblp.uni-trier.de/pers/hd/c/Chen:Qiming), [Ren Wu](Ren_Wu "Ren Wu") (**2017**). *CNN Is All You Need*. [arXiv:1712.09662](https://arxiv.org/abs/1712.09662)
* [Alexantrou Serb](https://dblp.org/pers/hd/s/Serb:Alexander), [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [Ioannis Messaris](https://dblp.org/pers/hd/m/Messaris:Ioannis), [Long Tran-Thanh](https://dblp.org/pers/hd/t/Tran=Thanh:Long), [Themis Prodromakis](https://www.orc.soton.ac.uk/people/tp1f12) (**2017**). *[Hardware-level Bayesian inference](https://eprints.soton.ac.uk/425616/)*. [NIPS 2017](https://nips.cc/Conferences/2017) » [Analog Evaluation](Analog_Evaluation "Analog Evaluation")


**2018**



* [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf), [pdf](https://www.apply.computer-shogi.org/wcsc28/appeal/the_end_of_genesis_T.N.K.evolution_turbo_type_D/nnue.pdf) (Japanese with English abstract) [GitHub - asdfjkl/nnue translation](https://github.com/asdfjkl/nnue) » [NNUE](NNUE "NNUE") [[94]](#cite_note-94)
* [Kei Takada](Kei_Takada "Kei Takada"), [Hiroyuki Iizuka](index.php?title=Hiroyuki_Iizuka&action=edit&redlink=1 "Hiroyuki Iizuka (page does not exist)"), [Masahito Yamamoto](index.php?title=Masahito_Yamamoto&action=edit&redlink=1 "Masahito Yamamoto (page does not exist)") (**2018**). *[Computer Hex Algorithm Using a Move Evaluation Method Based on a Convolutional Neural Network](https://link.springer.com/chapter/10.1007%2F978-3-319-75931-9_2)*. [Communications in Computer and Information Science](https://link.springer.com/bookseries/7899) » [Hex](Hex "Hex")
* [Matthia Sabatelli](Matthia_Sabatelli "Matthia Sabatelli"), [Francesco Bidoia](Francesco_Bidoia "Francesco Bidoia"), [Valeriu Codreanu](Valeriu_Codreanu "Valeriu Codreanu"), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2018**). *Learning to Evaluate Chess Positions with Deep Neural Networks and Limited Lookahead*. ICPRAM 2018, [pdf](http://www.ai.rug.nl/~mwiering/GROUP/ARTICLES/ICPRAM_CHESS_DNN_2018.pdf)
* [Ashwin Srinivasan](Ashwin_Srinivasan "Ashwin Srinivasan"), [Lovekesh Vig](index.php?title=Lovekesh_Vig&action=edit&redlink=1 "Lovekesh Vig (page does not exist)"), [Michael Bain](Michael_Bain "Michael Bain") (**2018**). *Logical Explanations for Deep Relational Machines Using Relevance Information*. [arXiv:1807.00595](https://arxiv.org/abs/1807.00595)
* [Thomas Elsken](index.php?title=Thomas_Elsken&action=edit&redlink=1 "Thomas Elsken (page does not exist)"), [Jan Hendrik Metzen](index.php?title=Jan_Hendrik_Metzen&action=edit&redlink=1 "Jan Hendrik Metzen (page does not exist)"), [Frank Hutter](Frank_Hutter "Frank Hutter") (**2018**). *Neural Architecture Search: A Survey*. [arXiv:1808.05377](https://arxiv.org/abs/1808.05377)
* [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](https://en.wikipedia.org/wiki/Science_(journal)), Vol. 362, No. 6419 [[95]](#cite_note-95)
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Siqi Yan](index.php?title=Siqi_Yan&action=edit&redlink=1 "Siqi Yan (page does not exist)"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2018**). *A transferable neural network for Hex*. [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")


**2019**



* [Marius Lindauer](index.php?title=Marius_Lindauer&action=edit&redlink=1 "Marius Lindauer (page does not exist)"), [Frank Hutter](Frank_Hutter "Frank Hutter") (**2019**). *Best Practices for Scientific Research on Neural Architecture Search*. [arXiv:1909.02453](https://arxiv.org/abs/1909.02453)
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2019**). *Chess endgame news: an endgame challenge for neural nets*. [ICGA Journal, Vol. 41, No. 3](ICGA_Journal#41_3 "ICGA Journal") » [Endgame](Endgame "Endgame")
* [Philip G. Breen](https://scholar.google.co.uk/citations?user=JNTc6R4AAAAJ&hl=en), [Christopher N. Foley](https://scholar.google.com/citations?user=fJmka-IAAAAJ&hl=en), [Tjarda Boekholt](https://scholar.google.com/citations?user=QOehl_0AAAAJ&hl=en), [Simon Portegies Zwart](Simon_Portegies_Zwart "Simon Portegies Zwart") (**2019**). *Newton vs the machine: solving the chaotic three-body problem using deep neural networks*. [arXiv:1910.07291](https://arxiv.org/abs/1910.07291)


### 2020 ...


* [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Aligning Superhuman AI with Human Behavior: Chess as a Model System*. [ACM SIGKDD 2020](ACM#SIGKDD "ACM"), [arXiv:2006.01855](https://arxiv.org/abs/2006.01855) » [Maia Chess](Maia_Chess "Maia Chess")
* [Reid McIlroy-Young](Reid_McIlroy-Young "Reid McIlroy-Young"), [Russell Wang](Russell_Wang "Russell Wang"), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Jon Kleinberg](Jon_Kleinberg "Jon Kleinberg"), [Ashton Anderson](Ashton_Anderson "Ashton Anderson") (**2020**). *Learning Personalized Models of Human Behavior in Chess*. [arXiv:2008.10086](https://arxiv.org/abs/2008.10086)
* [Oisín Carroll](index.php?title=Ois%C3%ADn_Carroll&action=edit&redlink=1 "Oisín Carroll (page does not exist)"), [Joeran Beel](index.php?title=Joeran_Beel&action=edit&redlink=1 "Joeran Beel (page does not exist)") (**2020**). *Finite Group Equivariant Neural Networks for Games*. [arXiv:2009.05027](https://arxiv.org/abs/2009.05027)
* [Mohammad Pezeshki](https://scholar.google.com/citations?user=HT85tXsAAAAJ&hl=en), [Sékou-Oumar Kaba](https://scholar.google.com/citations?user=jKqh8jAAAAAJ&hl=en), [Yoshua Bengio](Mathematician#YBengio "Mathematician") , [Aaron Courville](Mathematician#ACourville "Mathematician") , [Doina Precup](Doina_Precup "Doina Precup"), [Guillaume Lajoie](https://scholar.google.com/citations?user=ifu_7_0AAAAJ&hl=en) (**2020**). *Gradient Starvation: A Learning Proclivity in Neural Networks*. [arXiv:2011.09468](https://arxiv.org/abs/2011.09468)
* [Johannes Czech](Johannes_Czech "Johannes Czech"), [Moritz Willig](Moritz_Willig "Moritz Willig"), [Alena Beyer](Alena_Beyer "Alena Beyer"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2020**). *[Learning to Play the Chess Variant Crazyhouse Above World Champion Level With Deep Neural Networks and Human Data](https://www.frontiersin.org/articles/10.3389/frai.2020.00024/full)*. [Frontiers in Artificial Intelligence](https://www.frontiersin.org/journals/artificial-intelligence#)  » [CrazyAra](CrazyAra "CrazyAra")


**2021**



* [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[96]](#cite_note-96)
* [Thomas McGrath](index.php?title=Thomas_McGrath&action=edit&redlink=1 "Thomas McGrath (page does not exist)"), [Andrei Kapishnikov](index.php?title=Andrei_Kapishnikov&action=edit&redlink=1 "Andrei Kapishnikov (page does not exist)"), [Nenad Tomašev](index.php?title=Nenad_Toma%C5%A1ev&action=edit&redlink=1 "Nenad Tomašev (page does not exist)"), [Adam Pearce](index.php?title=Adam_Pearce&action=edit&redlink=1 "Adam Pearce (page does not exist)"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Been Kim](index.php?title=Been_Kim&action=edit&redlink=1 "Been Kim (page does not exist)"), [Ulrich Paquet](index.php?title=Ulrich_Paquet&action=edit&redlink=1 "Ulrich Paquet (page does not exist)"), [Vladimir Kramnik](index.php?title=Vladimir_Kramnik&action=edit&redlink=1 "Vladimir Kramnik (page does not exist)") (**2021**). *Acquisition of Chess Knowledge in AlphaZero*. [arXiv:2111.09259](https://arxiv.org/abs/2111.09259) [[97]](#cite_note-97)


## Blog & Forum Posts


### 1996 ...


* [Q: Neural Nets/Genetic Algor. and Chess](https://groups.google.com/d/msg/rec.games.chess.computer/ZFTi2Bh8Qsk/NwZMSgRibS4J) by Jeff Hamm, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 01, 1996
* [neural networks for pawn-structures](https://groups.google.com/d/msg/rec.games.chess.computer/uVEujVXi7cw/My9fE3w9yzYJ) by Romain Slootmaekers, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 29, 1996
* [Neural Network based Chessprogram](https://groups.google.com/d/msg/rec.games.chess.computer/f2Nf5PjxrV0/JhSLvVzWPAgJ) by Michael Niemeck, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 16, 1996
* [Neural Nets in Chess? Question to experts](https://groups.google.com/d/msg/rec.games.chess.computer/8CcXkJ5vOiw/bjxLqThd4tUJ) by George R. Barrett, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 02, 1997
* [Chess using Neural Networks/Fuzzy Logic](https://groups.google.com/d/msg/rec.games.chess.computer/bd2LislJ_-8/Czr0M_HLwa0J) by [Kumar Chellapilla](index.php?title=Kumar_Chellapilla&action=edit&redlink=1 "Kumar Chellapilla (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 12, 1997
* [Evaluation by neural network ?](https://www.stmintz.com/ccc/index.php?id=11870) by [Mark Taylor](Mark_Taylor "Mark Taylor"), [CCC](CCC "CCC"), November 10, 1997


 [Re: Evaluation by neural network ?](https://www.stmintz.com/ccc/index.php?id=11893) by [Jay Scott](Jay_Scott "Jay Scott"), [CCC](CCC "CCC"), November 10, 1997 [[98]](#cite_note-98)
* [neural network and chess](https://groups.google.com/d/msg/rec.games.chess.computer/cBoAi473cjg/nJctqxz-59EJ) by Yeeming Jih, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 23, 1998
* [Chess, Backgammon and Neural Nets (NN)](https://www.stmintz.com/ccc/index.php?id=25139) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)"), [CCC](CCC "CCC"), August 20, 1998
* [Chess and Neural Networks](https://www.stmintz.com/ccc/index.php?id=41068) by Frank Schubert, [CCC](CCC "CCC"), January 27, 1999
* [Neural networks](https://groups.google.com/d/msg/rec.games.chess.computer/Ov0DhO-Opdo/VNtsNJt_eIEJ) by Bill Keller, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 01, 1999
* [neural computing in eval function](https://www.stmintz.com/ccc/index.php?id=83443) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), December 20, 1999


### 2000 ...


* [Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/BHukuAm1ne4J) by Ray Lopez, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2000


 [Re: Whatever happened to Neural Network Chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/ZgORiY9-gF0J) by [Andy Walker](Andy_Walker "Andy Walker"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2000  » [Advances in Computer Chess 1](Advances_in_Computer_Chess_1 "Advances in Computer Chess 1"), [Ron Atkin](Ron_Atkin "Ron Atkin") 
 [Combining Neural Networks and Alpha-Beta](https://groups.google.com/d/msg/rec.games.chess.computer/xthKCFRJkeM/CwRxa1j7Q1IJ) by [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2000 » [Chessterfield](Chessterfield "Chessterfield")
* [Neural Networks in Chess](https://www.stmintz.com/ccc/index.php?id=116293) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), June 23, 2000
* [Artificial Neural Networks for Chess](https://groups.google.com/d/msg/rec.games.chess.computer/IgS1pwQYF3E/2jx2HTICOw0J) by Jet Nebula, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 02, 2002
* [chess and neural networks](https://www.stmintz.com/ccc/index.php?id=304075) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), July 01, 2003
* [Presentation for a neural net learning chess program](https://www.stmintz.com/ccc/index.php?id=358770) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 06, 2004 [[99]](#cite_note-99)


 [Neural nets in backgammon](https://www.stmintz.com/ccc/index.php?id=359097) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), April 07, 2004
* [Chess Neural Network: ANOTHER VICTORY FOR OCTAVIUS!](https://groups.google.com/d/msg/rec.games.chess.computer/D8ug0bq02Cs/SBikPRjdhJEJ) by [Luke Pellen](Luke_Pellen "Luke Pellen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 04, 2004


### 2005 ...


* [designing neural networks](http://www.talkchess.com/forum/viewtopic.php?t=16162) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 31, 2007
* [naive bayes classifier](http://www.talkchess.com/forum/viewtopic.php?t=29056) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 21, 2009 [[100]](#cite_note-100)


### 2010 ...


* [Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?t=31545) by [Stephan Vermeire](Stephan_Vermeire "Stephan Vermeire"), [CCC](CCC "CCC"), January 07, 2010


 [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316511&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 07, 2010 » [Stoofvlees](Stoofvlees "Stoofvlees")
 [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316769&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 08, 2010 
 [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316926&t=31545) by [Volker Annuss](Volker_Annuss "Volker Annuss"), [CCC](CCC "CCC"), January 08, 2010 » [Hermann](Hermann "Hermann")
* [Is there place for neural networks in chess engines?](http://www.talkchess.com/forum/viewtopic.php?t=41300) by E Diaz, [CCC](CCC "CCC"), December 02, 2011
* [What does the hidden layer in a neural network compute?](http://stats.stackexchange.com/questions/63152/what-does-the-hidden-layer-in-a-neural-network-compute) by GeorgeMcDowd, [Cross Validated](http://stats.stackexchange.com/), July 02, 2013
* [Move Evaluation in Go Using Deep Convolutional Neural Networks](http://computer-go.org/pipermail/computer-go/2014-December/007046.html) by [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [The Computer-go Archives](http://computer-go.org/pipermail/computer-go/), December 19, 2014


### 2015 ...


* [If you are interested in machine learning and Python !](http://www.talkchess.com/forum/viewtopic.php?t=55437) by [Ruxy Sylwyka](http://www.talkchess.com/forum/profile.php?mode=viewprofile&u=881), [CCC](CCC "CCC"), February 23, 2015
* [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015 » [Giraffe](Giraffe "Giraffe")


**2016**



* [Neural networks for Spanish checkers and beyond](https://www.game-ai-forum.org/viewtopic.php?f=2&t=75) by [Alvaro](Alvaro_Cardoso "Alvaro Cardoso"), [Game-AI Forum](Computer_Chess_Forums "Computer Chess Forums"), January 01, 2016
* [Chess position evaluation with convolutional neural network in Julia](http://int8.io/chess-position-evaluation-with-convolutional-neural-networks-in-julia/) by [Kamil Czarnogorski](index.php?title=Kamil_Czarnogorski&action=edit&redlink=1 "Kamil Czarnogorski (page does not exist)"), [Machine learning with Julia and python](http://int8.io/), April 02, 2016 [[101]](#cite_note-101)
* [Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883) by Eren Yavuz, [CCC](CCC "CCC"), July 21, 2016


 [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=4) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016 » [Zurichess](Zurichess "Zurichess")
 [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=7) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 04, 2016 » [Giraffe](Giraffe "Giraffe") [[102]](#cite_note-102)
* [Neuronet plus conventional approach combined?](http://www.talkchess.com/forum/viewtopic.php?t=61312) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), September 02, 2016
* [DeepChess: Another deep-learning based chess program](http://www.talkchess.com/forum/viewtopic.php?t=61748) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), October 17, 2016 » [DeepChess](index.php?title=DeepChess&action=edit&redlink=1 "DeepChess (page does not exist)")
* [The scaling of Deep Learning MCTS Go engines](http://www.talkchess.com/forum/viewtopic.php?t=61801) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), October 23, 2016 » [Deep Learning](Neural_Networks#Deep "Neural Networks"), [Go](Go "Go"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


**2017**



* [Deep Pink: a chess engine using deep learning](http://www.talkchess.com/forum/viewtopic.php?t=63063) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), February 05, 2017 » [Deep Pink](Deep_Pink "Deep Pink")
* [Using GAN to play chess](http://www.talkchess.com/forum/viewtopic.php?t=63252) by Evgeniy Zheltonozhskiy, [CCC](CCC "CCC"), February 23, 2017 [[103]](#cite_note-103)
* [Is AlphaGo approach unsuitable to chess?](http://www.talkchess.com/forum/viewtopic.php?t=64096) by Mel Cooper, [CCC](CCC "CCC"), May 27, 2017 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)"), [Deep Learning](Deep_Learning "Deep Learning"), [Giraffe](Giraffe "Giraffe")


 [Re: Is AlphaGo approach unsuitable to chess?](http://www.talkchess.com/forum/viewtopic.php?t=64096&start=12) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 31, 2017 » [Texel](Texel "Texel")
* [Neural nets for Go - chain pooling?](https://groups.google.com/d/msg/computer-go-archive/WImAk15gRN4/bhA7kSAnBgAJ) by [David Wu](David_J._Wu "David J. Wu"), [Computer Go Archive](https://groups.google.com/forum/#!forum/computer-go-archive), August 18, 2017
* [AlphaGo Zero: Learning from scratch](https://deepmind.com/blog/alphago-zero-learning-scratch/) by [Demis Hassabis](Demis_Hassabis "Demis Hassabis") and [David Silver](David_Silver "David Silver"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), October 18, 2017
* [We are doomed - AlphaGo Zero, learning only from basic rules](http://www.talkchess.com/forum/viewtopic.php?t=65481) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), October 18, 2017
* [AlphaGo Zero](http://www.talkchess.com/forum/viewtopic.php?t=65484) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), October 19, 2017
* [Zero performance](https://groups.google.com/d/msg/computer-go-archive/9DNayZWKXfk/Pk9yBx1lAgAJ) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [Computer Go Archive](https://groups.google.com/forum/#!forum/computer-go-archive), October 20, 2017
* [Re: AlphaGo Zero](https://groups.google.com/d/msg/computer-go-archive/ulsErJxW3jc/hMIhtiBYAgAJ) by [Hendrik Baier](Hendrik_Baier "Hendrik Baier"), [Computer Go Archive](https://groups.google.com/forum/#!forum/computer-go-archive), October 20, 2017
* [Neural networks for chess position evaluation- request](http://www.talkchess.com/forum/viewtopic.php?t=65715) by [Kamil Czarnogorski](index.php?title=Kamil_Czarnogorski&action=edit&redlink=1 "Kamil Czarnogorski (page does not exist)"), [CCC](CCC "CCC"), November 13, 2017 » [Evaluation](Evaluation "Evaluation")
* [AlphaGo's evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=65829) by Jens Kipper, [CCC](CCC "CCC"), November 26, 2017
* [Neural Nets can't explain what they do and this is a problem](http://www.talkchess.com/forum/viewtopic.php?t=65831) by Myron Samsin, November 26, 2017
* [Google's AlphaGo team has been working on chess](http://www.talkchess.com/forum/viewtopic.php?t=65909) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [CCC](CCC "CCC"), December 06, 2017 » [AlphaZero](AlphaZero "AlphaZero")
* [Historic Milestone: AlphaZero](http://www.talkchess.com/forum/viewtopic.php?t=65910) by Miguel Castanuela, [CCC](CCC "CCC"), December 06, 2017
* [An AlphaZero inspired project](http://www.talkchess.com/forum/viewtopic.php?t=66013) by [Truls Edvard Stokke](index.php?title=Truls_Edvard_Stokke&action=edit&redlink=1 "Truls Edvard Stokke (page does not exist)"), [CCC](CCC "CCC"), December 14, 2017 » [AlphaZero](AlphaZero "AlphaZero")


**2018**



* [Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 09, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [Connect 4 AlphaZero implemented using Python...](http://www.talkchess.com/forum/viewtopic.php?t=66443) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 29, 2018 » [AlphaZero](AlphaZero "AlphaZero"), [Connect Four](Connect_Four "Connect Four"), [Python](Python "Python")
* [3 million games for training neural networks](http://www.talkchess.com/forum/viewtopic.php?t=66681) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 24, 2018 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Looking inside NNs](http://www.talkchess.com/forum/viewtopic.php?t=66791) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), March 09, 2018
* [GPU ANN, how to deal with host-device latencies?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67347) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), May 06, 2018 » [GPU](GPU "GPU")
* [Poor man's neurones](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67524) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), May 21, 2018 » [Evaluation](Evaluation "Evaluation")
* [Egbb dll neural network support](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67600) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 29, 2018 » [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [Instruction for running Scorpio with neural network on linux](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68119) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 01, 2018 » [Scorpio](Scorpio "Scorpio")
* [Are draws hard to predict?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69069) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 27, 2018 » [Draw](Draw "Draw")
* [use multiple neural nets?](https://groups.google.com/d/msg/lczero/EGcJSrZYLiw/netJ4S38CgAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [LCZero Forum](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [neural network architecture](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69393) by jackd, [CCC](CCC "CCC"), December 26, 2018


**2019**



* [So, how many of you are working on neural networks for chess?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69795) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), February 01, 2019
* [categorical cross entropy for value](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69942) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), February 18, 2019
* [Google's bfloat for neural networks](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70504) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), April 16, 2019 » [Float](Float "Float")
* [catastrophic forgetting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70704) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 09, 2019 » [Nebiyu](Nebiyu "Nebiyu")
* [Wouldn’t it be nice if there was a ChessNet50](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71269) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), July 13, 2019
* [A question to MCTS + NN experts](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71301) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), July 17, 2019 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


 [Re: A question to MCTS + NN experts](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71301&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), July 17, 2019 
* [high dimensional optimization](https://groups.google.com/d/msg/fishcooking/wOfRuzTSi_8/VgjN8MmSBQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 27, 2019 [[104]](#cite_note-104)


### 2020 ...


* [How to work with batch size in neural network](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74077) by Gertjan Brouwer, [CCC](CCC "CCC"), June 02, 2020
* [NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), July 21, 2020 » [NNUE](NNUE "NNUE")


 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=1) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 23, 2020
 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 24, 2020
* [LC0 vs. NNUE - some tech details...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74607) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 29, 2020 » [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero")
* [AB search with NN on GPU...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74771) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), August 13, 2020 » [GPU](GPU "GPU") [[105]](#cite_note-105)
* [Neural Networks weights type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74777) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 13, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Train a neural network evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74955) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 01, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [NNUE](NNUE "NNUE")
* [Neural network quantization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75042) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 08, 2020 » [NNUE](NNUE "NNUE")
* [First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 23, 2020
* [Transhuman Chess with NN and RL...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75606) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), October 30, 2020 » [RL](Reinforcement_Learning "Reinforcement Learning")
* [Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), November 08, 2020 [[106]](#cite_note-106) » [NNUE](NNUE "NNUE")
* [Pawn King Neural Network](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75925) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), November 26, 2020 » [NNUE](NNUE "NNUE")
* [Learning draughts evaluation functions using Keras/TensorFlow](http://laatste.info/bb3/viewtopic.php?f=53&t=8327) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [World Draughts Forum](http://laatste.info/bb3/viewforum.php?f=53), November 30, 2020 » [Draughts](Draughts "Draughts")
* [Maiachess](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75985) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), December 04, 2020 » [Maia Chess](Maia_Chess "Maia Chess")


**2021**



* [More experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76263) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), January 09, 2021 » [Slow Chess](Slow_Chess "Slow Chess")
* [Keras/Tensforflow for very sparse inputs](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76334) by Jacek Dermont, [CCC](CCC "CCC"), January 16, 2021
* [Are neural nets (the weights file) copyrightable?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76664) by [Adam Treat](Adam_Treat "Adam Treat"), [CCC](CCC "CCC"), February 21, 2021
* [A worked example of backpropagation using Javascript](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76885) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), March 16, 2021 » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks")
* [yet another NN library](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77061) by lucasart, [CCC](CCC "CCC"), April 11, 2021 » [lucasart/nn](#lucasart)
* [Some more experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77492) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2021 » [Slow Chess](Slow_Chess "Slow Chess")
* [Re: Stockfish 14 has been released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77605&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), July 04, 2021 » [Stockfish](Stockfish "Stockfish")
* [tablebase neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77899) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), August 07, 2021 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021


**2022**



* [Binary Neural Networks Sliding Piece Inference [Release]](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79332) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), February 10, 2022 » [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks")
* [Failure of trivial approach to neural network move ordering](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79368) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), February 16, 2022 » [Move Ordering](Move_Ordering "Move Ordering")


## External Links


* [Neural network (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Neural_network_%28disambiguation%29)
* [Category:Neural networks - Scholarpedia](https://www.scholarpedia.org/article/Category:Neural_networks)
* [Neural networks - Psychology Wiki](http://psychology.wikia.com/wiki/Neural_networks)


**Biological**



* [Biological neural network from Wikipedia](https://en.wikipedia.org/wiki/Biological_neural_network)
* [Biological neuron model from Wikipedia](https://en.wikipedia.org/wiki/Biological_neuron_model)
* [Computational neuroscience from Wikipedia](https://en.wikipedia.org/wiki/Computational_neuroscience)
* [Neuron from Wikipedia](https://en.wikipedia.org/wiki/Neuron)
* [Neural pathway from Wikipedia](https://en.wikipedia.org/wiki/Neural_pathway)


### ANNs


* [Artificial neural network from Wikipedia](https://en.wikipedia.org/wiki/Artificial_neural_network)
* [Types of artificial neural networks from Wikipedia](https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks)
* [Artificial neural network - Wikimedia Commons](https://commons.wikimedia.org/wiki/Artificial_neural_network)
* [Artificial Neural Networks - Wikibooks](https://en.wikibooks.org/wiki/Artificial_Neural_Networks)
* [Artificial Neural Networks](http://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol4/cs11/report.html) by Christos Stergiou and Dimitrios Siganos
* [DMOZ - Computers: Artificial Intelligence: Neural Networks](https://www.dmoz.org/Computers/Artificial_Intelligence/Neural_Networks)
* [DMS Tutorial - Neural networks](http://dms.irb.hr/tutorial/tut_nnets_short.php)
* [Helmholtz machine from Wikipedia](https://en.wikipedia.org/wiki/Helmholtz_machine)
* [Chess end games using Neural Networks](http://de.slideshare.net/piuprabhu/chess-end-games-using-neural-networks-presentation)


### Topics


* [Artificial neuron from Wikipedia](https://en.wikipedia.org/wiki/Artificial_neuron)
* [Connectionism from Wikipedia](https://en.wikipedia.org/wiki/Connectionism)
* [Deep Learning from Wikipeadia](https://en.wikipedia.org/wiki/Deep_learning)
* [Deep Learning - Scholarpedia](http://www.scholarpedia.org/article/Deep_Learning) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
* [Feedforward neural network from Wikipedia](https://en.wikipedia.org/wiki/Feedforward_neural_network)
* [Fuzzy neural network - Scholarpedia](http://www.scholarpedia.org/article/Fuzzy_neural_network)
* [Generative adversarial networks from Wikipedia](https://en.wikipedia.org/wiki/Generative_adversarial_networks)
* [Grossberg network from Wikipedia](https://en.wikipedia.org/wiki/Grossberg_network)
* [Modular neural network from Wikipedia](https://en.wikipedia.org/wiki/Modular_neural_network)
* [Neocognitron from Wikipedia](https://en.wikipedia.org/wiki/Neocognitron)
* [Neocognitron - Scholarpedia](http://www.scholarpedia.org/article/Neocognitron) by [Kunihiko Fukushima](http://www.scholarpedia.org/article/User:Kunihiko_Fukushima)
* [Neural architecture search from Wikipedia](https://en.wikipedia.org/wiki/Neural_architecture_search)
* [Neuromorphic engineering from Wikipedia](https://en.wikipedia.org/wiki/Neuromorphic_engineering)


 [Neurogrid from Wikipedia](https://en.wikipedia.org/wiki/Neurogrid)
* [Physical neural network from Wikipedia](https://en.wikipedia.org/wiki/Physical_neural_network)
* [Radial basis function network from Wikipedia](https://en.wikipedia.org/wiki/Radial_basis_function_network)
* [Random neural network from Wikipedia](https://en.wikipedia.org/wiki/Random_neural_network)
* [Recursive neural network from Wikipedia](https://en.wikipedia.org/wiki/Recursive_neural_network)
* [Self-organizing map from Wikipedia](https://en.wikipedia.org/wiki/Self-organizing_map)
* [Spiking neural network from Wikipedia](https://en.wikipedia.org/wiki/Spiking_neural_network)
* [Time delay neural network from Wikipedia](https://en.wikipedia.org/wiki/Time_delay_neural_network)


### Perceptron


* [Perceptron from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)


 [History of the Perceptron](http://web.csulb.edu/~cwallis/artificialn/History.htm)
* [ADALINE from Wikipedia](https://en.wikipedia.org/wiki/ADALINE)
* [Multilayer perceptron from Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron)


### CNNs


* [Convolutional neural network from Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)
* [Convolutional Neural Networks for Image and Video Processing](https://wiki.tum.de/display/lfdv/Convolutional+Neural+Networks+for+Image+and+Video+Processing), [TUM Wiki](https://wiki.tum.de/), [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich")


 [Convolutional Neural Networks](https://wiki.tum.de/display/lfdv/Convolutional+Neural+Networks#ConvolutionalNeuralNetworks-convolution)
 [Deep Residual Networks](https://wiki.tum.de/display/lfdv/Deep+Residual+Networks)
 [An Introduction to different Types of Convolutions in Deep Learning](https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d) by [Paul-Louis Pröve](http://plpp.de/), July 22, 2017
 [Squeeze-and-Excitation Networks](https://towardsdatascience.com/squeeze-and-excitation-networks-9ef5e71eacd7) by [Paul-Louis Pröve](http://plpp.de/), October 17, 2017
* [Deep Convolutional Neural Networks](https://towardsdatascience.com/deep-convolutional-neural-networks-ccf96f830178) by Pablo Ruiz, October 11, 2018


### ResNet


* [Residual neural network from Wikipedia](https://en.wikipedia.org/wiki/Residual_neural_network)
* [Deep Residual Networks](https://wiki.tum.de/display/lfdv/Deep+Residual+Networks) from [TUM Wiki](https://wiki.tum.de/), [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich")
* [Understanding and visualizing ResNets](https://towardsdatascience.com/understanding-and-visualizing-resnets-442284831be8) by Pablo Ruiz, October 8, 2018


### RNNs


* [Recurrent neural network from Wikipedia](https://en.wikipedia.org/wiki/Recurrent_neural_network)
* [Recurrent neural networks - Scholarpedia](http://www.scholarpedia.org/article/Recurrent_neural_networks)
* [Recurrent Neural Networks](http://people.idsia.ch/~juergen/rnn.html) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
* [Bidirectional associative memory from Wikipedia](https://en.wikipedia.org/wiki/Bidirectional_associative_memory)
* [Boltzmann machine from Wikipedia](https://en.wikipedia.org/wiki/Boltzmann_machine)


 [Restricted Boltzmann machine from Wikipedia](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)
* [Echo state network](https://en.wikipedia.org/wiki/Echo_state_network)
* [Hopfield network from Wikipedia](https://en.wikipedia.org/wiki/Hopfield_network)
* [Hopfield network - Scholarpedia](http://www.scholarpedia.org/article/Hopfield_network)
* [Long short term memory from Wikipedia](https://en.wikipedia.org/wiki/Long_short_term_memory)


### Activation Functions


* [Activation function from Wikipedia](https://en.wikipedia.org/wiki/Activation_function)
* [Rectifier (neural networks) from Wikipedia](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
* [Sigmoid function from Wikipedia](https://en.wikipedia.org/wiki/Sigmoid_function)
* [Softmax function from Wikipedia](https://en.wikipedia.org/wiki/Softmax_function)


### Backpropagation


* [Backpropagation from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation)
* [Backpropagation through structure from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation_through_structure)
* [Backpropagation through time from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation_through_time)
* [Rprop from Wikipedia](https://en.wikipedia.org/wiki/Rprop)
* [Who Invented Backpropagation?](http://people.idsia.ch/~juergen/who-invented-backpropagation.html) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (2014, 2015)
* [A worked example of backpropagation](https://alexander-schiendorfer.github.io/2020/02/24/a-worked-example-of-backprop.html) by [Alexander Schiendorfer](https://alexander-schiendorfer.github.io/about.html), February 24, 2020  » [Backpropagation](Neural_Networks#Backpropagation "Neural Networks") [[107]](#cite_note-107)


### Gradient


* [Gradient from Wikipedia](https://en.wikipedia.org/wiki/Gradient)
* [Del from Wikipedia](https://en.wikipedia.org/wiki/Del)
* [Gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Gradient_descent)
* [Conjugate gradient method from Wikipedia](https://en.wikipedia.org/wiki/Conjugate_gradient_method)
* [Stochastic gradient descent from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)


 [Momentum from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Momentum)
* [ORF523: Nesterov’s Accelerated Gradient Descent](https://blogs.princeton.edu/imabandit/2013/04/01/acceleratedgradientdescent/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), April 1, 2013 » [Yurii Nesterov](Mathematician#YNesterov "Mathematician")
* [Nesterov’s Accelerated Gradient Descent for Smooth and Strongly Convex Optimization](https://blogs.princeton.edu/imabandit/2014/03/06/nesterovs-accelerated-gradient-descent-for-smooth-and-strongly-convex-optimization/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), March 6, 2014
* [Revisiting Nesterov’s Acceleration](https://blogs.princeton.edu/imabandit/2015/06/30/revisiting-nesterovs-acceleration/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), June 30, 2015


### Software


* [Neural network software from Wikipedia](https://en.wikipedia.org/wiki/Neural_network_software)


 [Neural Lab from Wikipedia](https://en.wikipedia.org/wiki/Neural_Lab)
 [SNNS from Wikipedia](https://en.wikipedia.org/wiki/SNNS)
* [Comparison of deep learning software from Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software)
* [GitHub - connormcmonigle/reference-neural-network](https://github.com/connormcmonigle/reference-neural-network) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle")
* [GitHub - lucasart/nn: neural network experiment](https://github.com/lucasart/nn) [[108]](#cite_note-108)


### Libraries


* [Eigen (C++ library) from Wikipedia](https://en.wikipedia.org/wiki/Eigen_%28C%2B%2B_library%29)
* [Fast Artificial Neural Network Library (FANN)](http://leenissen.dk/fann/wp/)
* [Keras from Wikipedia](https://en.wikipedia.org/wiki/Keras)
* [PythonForArtificialIntelligence - Python Wiki](https://wiki.python.org/moin/PythonForArtificialIntelligence) [Python](Python "Python")
* [TensorFlow from Wikipedia](https://en.wikipedia.org/wiki/TensorFlow)


### Blogs


* [Neural Networks Blog](https://theneural.wordpress.com/) by [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever")
* [An Introduction to Neural Networks with an Application to Games](https://software.intel.com/en-us/articles/an-introduction-to-neural-networks-with-an-application-to-games) by [Dean Macri](https://www.linkedin.com/pub/dean-p-macri/a/762/68b), [Intel Developer Zone](https://en.wikipedia.org/wiki/Intel_Developer_Zone), September 9, 2011
* [John Wakefield's](http://www.blogger.com/profile/07894297206547597169) [Dynamic Notions](http://dynamicnotions.blogspot.com/), a Blog about the evolution of neural networks with [C#](C_sharp "C sharp") samples


 [The Single Layer Perceptron](http://dynamicnotions.blogspot.com/2008/09/single-layer-perceptron.html)
 [The Sigmoid Function in C#](http://dynamicnotions.blogspot.de/2008/09/sigmoid-function-in-c.html)
 [Hidden Neurons and Feature Space](http://dynamicnotions.blogspot.com/2008/09/hidden-neurons-and-feature-space.html)
 [Training Neural Networks Using Back Propagation in C#](http://dynamicnotions.blogspot.com/2008/09/training-neural-networks-using-back.html)
 [Data Mining with Artificial Neural Networks (ANN)](http://dynamicnotions.blogspot.com/2008/09/data-mining-with-artificial-neural.html)
* [Dave Miller Blog - Tag: Neural Net](http://www.millermattson.com/dave/?tag=neural-net)


 [Neural Net in C++ Tutorial](https://vimeo.com/19569529) on [Vimeo](https://en.wikipedia.org/wiki/Vimeo) (also on [YouTube](https://www.youtube.com/watch?v=KkwX7FkLfug))
* [A Gentle Introduction to Artificial Neural Networks](https://theclevermachine.wordpress.com/2014/09/11/a-gentle-introduction-to-artificial-neural-networks/) by [Dustin Stansbury](https://scholar.google.com/citations?user=oY7AJUgAAAAJ&hl=en), [The Clever Machine](https://theclevermachine.wordpress.com/about-theclevermachine/), September 11, 2014
* [Deep learning for… chess](http://erikbern.com/2014/11/29/deep-learning-for-chess/) by [Erik Bernhardsson](Erik_Bernhardsson "Erik Bernhardsson"), November 29, 2014 [[109]](#cite_note-109)
* [Faster deep learning with GPUs and Theano](http://blog.dominodatalab.com/gpu-computing-and-deep-learning/) by [Manojit Nandi](https://www.linkedin.com/pub/manojit-nandi/35/688/384), August 05, 2015 » [GPU](GPU "GPU"), [Python](Python "Python")
* [Enabling Continual Learning in Neural Networks](https://deepmind.com/blog/enabling-continual-learning-in-neural-networks/) by [James Kirkpatrick](index.php?title=James_Kirkpatrick&action=edit&redlink=1 "James Kirkpatrick (page does not exist)"), [Joel Veness](Joel_Veness "Joel Veness") et al., [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), March 13, 2017
* [Understand Deep Residual Networks — a simple, modular learning framework that has redefined state-of-the-art](https://blog.waya.ai/deep-residual-learning-9610bb62c355) by [Michael Dietz](https://blog.waya.ai/@waya.ai), [Waya.ai](https://blog.waya.ai/), May 02, 2017
* [How to build your own AlphaZero AI using Python and Keras](https://medium.com/applied-data-science/how-to-build-your-own-alphazero-ai-using-python-and-keras-7f664945c188) by [David Foster](https://www.linkedin.com/in/davidtfoster/), January 26, 2018 » [AlphaZero](AlphaZero "AlphaZero"), [Connect Four](Connect_Four "Connect Four"), [Python](Python "Python")


### Courses


* [Machine Learning and Probabilistic Graphical Models: Course Materials - 5. Neural Networks](http://www.cedar.buffalo.edu/~srihari/CSE574/index.html) by [Sargur Srihari](https://en.wikipedia.org/wiki/Sargur_Srihari), [University at Buffalo](https://en.wikipedia.org/wiki/University_at_Buffalo)
* [Neural Networks - Representation](http://www.holehouse.org/mlclass/08_Neural_Networks_Representation.html) from [Stanford Machine Learning](http://www.holehouse.org/mlclass/index.html) by [Andrew Ng](index.php?title=Andrew_Ng&action=edit&redlink=1 "Andrew Ng (page does not exist)")
* [Neural Networks - Learning](http://www.holehouse.org/mlclass/09_Neural_Networks_Learning.html) from [Stanford Machine Learning](http://www.holehouse.org/mlclass/index.html) by [Andrew Ng](index.php?title=Andrew_Ng&action=edit&redlink=1 "Andrew Ng (page does not exist)")
* [Neural Networks Demystified](http://nbviewer.ipython.org/github/stephencwelch/Neural-Networks-Demysitifed/tree/master/) by [Stephen Welch](https://twitter.com/stephencwelch), [Welch Labs](http://www.welchlabs.com/)


 [Part 1: Data and Architecture](https://www.youtube.com/watch?v=bxe2T-V8XRs), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos
 [Part 2: Forward Propagation](https://www.youtube.com/watch?v=UJwK6jAStmg)
 [Part 3: Gradient Descent](https://www.youtube.com/watch?v=5u0jaA3qAGk)
 [Part 4: Backpropagation](https://www.youtube.com/watch?v=GlcnxUlrtek)
 [Part 5: Numerical Gradient Checking](https://www.youtube.com/watch?v=pHMzNW8Agq4)
 [Part 6: Training](https://www.youtube.com/watch?v=9KM9Td6RVgQ)
 [Part 7: Overfitting, Testing, and Regularization](https://www.youtube.com/watch?v=S4ZUwgesjS8)
* [NN - Fully Connected Tutorial](https://www.youtube.com/playlist?list=PLgomWLYGNl1dL1Qsmgumhcg4HOcWZMd3k), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos by [Finn Eggers](Finn_Eggers "Finn Eggers")
* [Deep Learning Master Class](https://www.youtube.com/watch?v=UdSK7nnJKHU) by [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video
* [Lecture 10 - Neural Networks](https://www.youtube.com/watch?v=Ih5Mr93E-2c&hd=1) from [Learning From Data - Online Course (MOOC)](http://work.caltech.edu/telecourse.html) by [Yaser Abu-Mostafa](https://en.wikipedia.org/wiki/Yaser_Abu-Mostafa), [Caltech](https://en.wikipedia.org/wiki/California_Institute_of_Technology), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video
* [Lecture 12 - Learning: Neural Nets, Back Propagation](https://www.youtube.com/watch?v=q0pm3BrIUFo) by [Patrick Winston](Patrick_Winston "Patrick Winston"), [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [AI Lectures - Fall 2010](Patrick_Winston#AI_Lectures "Patrick Winston") [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos
* [Neural Networks](http://www.3blue1brown.com/videos/2017/10/9/neural-network) by [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw), October 9, 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos [[110]](#cite_note-110)


 [But what \*is\* a Neural Network? | Chapter 1](https://youtu.be/aircAruvnKk)
 [Gradient descent, how neural networks learn | Chapter 2](https://youtu.be/IHZwWFHWa-w)
 [What is backpropagation really doing? | Chapter 3](https://youtu.be/Ilg3gGewQ5U)
 [Backpropagation calculus | Appendix to Chapter 3](https://youtu.be/tIeHLnjs5U8)
* [Fei-Fei Li](Mathematician#FFLi "Mathematician"), [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [Serena Yeung](Mathematician#SYeung "Mathematician") - [CS231n Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu/), [Stanford University](Stanford_University "Stanford University"), 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 [Lecture 1 | Introduction to Convolutional Neural Networks for Visual Recognition](https://www.youtube.com/watch?v=vT1JzLTH4G4) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture1.pdf)
 [Lecture 2 | Image Classification](https://www.youtube.com/watch?v=OoUX-nOEjG0) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture2.pdf)
 [Lecture 3 | Loss Functions and Optimization](https://www.youtube.com/watch?v=h7iBpEHGVNc) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture3.pdf)
 [Lecture 4 | Introduction to Neural Networks](https://www.youtube.com/watch?v=d14TUNcbn1k) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture4.pdf)
 [Lecture 5 | Convolutional Neural Networks](https://www.youtube.com/watch?v=bNb2fEVKeEo) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture5.pdf)  

 [Lecture 6 | Training Neural Networks I](https://www.youtube.com/watch?v=wEoyxE0GP2M) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture6.pdf)
 [Lecture 7 | Training Neural Networks II](https://www.youtube.com/watch?v=_JB0AO7QxSA) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture7.pdf)
 [Lecture 8 | Deep Learning Software](https://www.youtube.com/watch?v=6SlgtELqOWc) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf)
 [Lecture 9 | CNN Architectures](https://www.youtube.com/watch?v=DAOcjicFr1Y) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture9.pdf)
 [Lecture 10 | Recurrent Neural Networks](https://www.youtube.com/watch?v=6niqTuYFZLQ) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture10.pdf)
 [Lecture 11 | Detection and Segmentation](https://www.youtube.com/watch?v=nDPWywWRIRo) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)
 [Lecture 12 | Visualizing and Understanding](https://www.youtube.com/watch?v=6wcs6szJWMY) by [Justin Johnson](Mathematician#JustinJohnson "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture12.pdf)
 [Lecture 13 | Generative Models](https://www.youtube.com/watch?v=5WoItGTWV54) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture13.pdf)
 [Lecture 14 | Deep Reinforcement Learning](https://www.youtube.com/watch?v=lvoHnicueoE) by [Serena Yeung](Mathematician#SYeung "Mathematician"), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture14.pdf)
 [Lecture 15 | Efficient Methods and Hardware for Deep Learning](https://www.youtube.com/watch?v=eZdOkDtYMoo) by [Song Han](https://scholar.google.com/citations?user=E0iCaa4AAAAJ&hl=en), [slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture15.pdf)
## References


1. [↑](#cite_ref-1) An example artificial neural network with a hidden layer, Image by [Colin M.L. Burnett](https://en.wikipedia.org/wiki/User:Cburnett) with [Inkscape](https://en.wikipedia.org/wiki/Inkscape), December 27, 2006, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Artificial Neural Networks/Neural Network Basics - Wikibooks](https://en.wikibooks.org/wiki/Artificial_Neural_Networks/Neural_Network_Basics), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Biological neural network - Early study - from Wikipedia](https://en.wikipedia.org/wiki/Biological_neural_network#Early_study)
3. [↑](#cite_ref-3) [Warren S. McCulloch](https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch), [Walter Pitts](https://en.wikipedia.org/wiki/Walter_Pitts) (**1943**). *[A Logical Calculus of the Ideas Immanent in Nervous Activity](http://link.springer.com/article/10.1007%2FBF02478259)*. [Bulletin of Mathematical Biology](http://link.springer.com/journal/11538), Vol. 5, No. 1, [pdf](http://www.aemea.org/math/McCulloch_Pitts_1943.pdf)
4. [↑](#cite_ref-4) [Artificial neuron from Wikipedia](https://en.wikipedia.org/wiki/Artificial_neuron)
 5. [↑](#cite_ref-5) The appropriate weights are applied to the inputs, and the resulting weighted sum passed to a function that produces the output y, image created by [mat\_the\_w](https://en.wikipedia.org/wiki/User:Mat_the_w), based on [raster image](https://en.wikipedia.org/wiki/Raster_graphics) [Perceptron.gif](http://commons.wikimedia.org/wiki/File:Perceptron.gif) by '[Paskari](https://en.wikipedia.org/wiki/User:Paskari)', using [Inkscape](https://en.wikipedia.org/wiki/Inkscape) 0.46 for [OSX](Mac_OS "Mac OS"), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Perceptron from Wikipedia](https://en.wikipedia.org/wiki/Perceptron) 
6. [↑](#cite_ref-6) [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) (**1957**). *The Perceptron - a Perceiving and Recognizing Automaton*. Report 85-460-1, [Cornell Aeronautical Laboratory](https://en.wikipedia.org/wiki/Calspan#History)
7. [↑](#cite_ref-7) A two-layer neural network capable of calculating XOR. The numbers within the neurons represent each neuron's explicit threshold (which can be factored out so that all neurons have the same threshold, usually 1). The numbers that annotate arrows represent the weight of the inputs. This net assumes that if the threshold is not reached, zero (not -1) is output. Note that the bottom layer of inputs is not always considered a real neural network layer, [Feedforward neural network from Wikipedia](https://en.wikipedia.org/wiki/Feedforward_neural_network)
8. [↑](#cite_ref-8) [multilayer perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) is a misnomer for a more complicated neural network
9. [↑](#cite_ref-9) [Perceptron from Wikipedia](https://en.wikipedia.org/wiki/Perceptron#History)
10. [↑](#cite_ref-10) [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1974**). *Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences*. Ph. D. thesis, [Harvard University](Harvard_University "Harvard University")
11. [↑](#cite_ref-11) [Henry J. Kelley](https://en.wikipedia.org/wiki/Henry_J._Kelley) (**1960**). *[Gradient Theory of Optimal Flight Paths](http://arc.aiaa.org/doi/abs/10.2514/8.5282?journalCode=arsj&)*. [<http://arc.aiaa.org/loi/arsj> ARS Journal, Vol. 30, No. 10
12. [↑](#cite_ref-12) [Arthur E. Bryson](https://en.wikipedia.org/wiki/Arthur_E._Bryson) (**1961**). *A gradient method for optimizing multi-stage allocation processes*. In Proceedings of the [Harvard University](Harvard_University "Harvard University") Symposium on digital computers and their applications
13. [↑](#cite_ref-13) [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") (**1961**). *[The numerical solution of variational problems](http://www.rand.org/pubs/papers/P2374.html)*. RAND paper P-2374
14. [↑](#cite_ref-14) [Seppo Linnainmaa](Mathematician#SLinnainmaa "Mathematician") (**1970**). *The representation of the cumulative rounding error of an algorithm as a Taylor expansion of the local rounding errors*. Master's thesis, [University of Helsinki](https://en.wikipedia.org/wiki/University_of_Helsinki)
15. [↑](#cite_ref-15) [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1982**). *Applications of advances in nonlinear sensitivity analysis*. [System Modeling and Optimization](http://link.springer.com/book/10.1007%2FBFb0006119), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf](http://werbos.com/Neural/SensitivityIFIPSeptember1981.pdf)
16. [↑](#cite_ref-16) [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1994**). *The Roots of Backpropagation. From Ordered Derivatives to Neural Networks and Political Forecasting*. [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
17. [↑](#cite_ref-17) [Deep Learning - Scholarpedia | Backpropagation](http://www.scholarpedia.org/article/Deep_Learning#Backpropagation) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber")
18. [↑](#cite_ref-18) [Who Invented Backpropagation?](http://people.idsia.ch/~juergen/who-invented-backpropagation.html) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (2014, 2015)
19. [↑](#cite_ref-19) "Using [cross-entropy error function](https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression) instead of [sum of squares](https://en.wikipedia.org/wiki/Mean_squared_error) leads to faster training and improved generalization", from [Sargur Srihari](https://en.wikipedia.org/wiki/Sargur_Srihari), [Neural Network Training](http://www.cedar.buffalo.edu/~srihari/CSE574/Chap5/Chap5.2-Training.pdf) (pdf)
20. [↑](#cite_ref-20) [Yurii Nesterov from Wikipedia](https://en.wikipedia.org/wiki/Yurii_Nesterov)
21. [↑](#cite_ref-21) [ORF523: Nesterov’s Accelerated Gradient Descent](https://blogs.princeton.edu/imabandit/2013/04/01/acceleratedgradientdescent/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), April 1, 2013
22. [↑](#cite_ref-22) [Nesterov’s Accelerated Gradient Descent for Smooth and Strongly Convex Optimization](https://blogs.princeton.edu/imabandit/2014/03/06/nesterovs-accelerated-gradient-descent-for-smooth-and-strongly-convex-optimization/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), March 6, 2014
23. [↑](#cite_ref-23) [Revisiting Nesterov’s Acceleration](https://blogs.princeton.edu/imabandit/2015/06/30/revisiting-nesterovs-acceleration/) by [Sébastien Bubeck](index.php?title=S%C3%A9bastien_Bubeck&action=edit&redlink=1 "Sébastien Bubeck (page does not exist)"), [I’m a bandit](https://blogs.princeton.edu/imabandit/), June 30, 2015
24. [↑](#cite_ref-24) [Backpropagation algorithm from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation#Algorithm)
25. [↑](#cite_ref-25) [PARsE | Education | GPU Cluster | Efficient mapping of the training of Convolutional Neural Networks to a CUDA-based cluster](http://parse.ele.tue.nl/education/cluster2)
26. [↑](#cite_ref-26) [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Vinod Nair](index.php?title=Vinod_Nair&action=edit&redlink=1 "Vinod Nair (page does not exist)") (**2008**). *Mimicking Go Experts with Convolutional Neural Networks*. [ICANN 2008](http://dblp.uni-trier.de/db/conf/icann/icann2008-2.html#SutskeverN08), [pdf](http://www.cs.utoronto.ca/~ilya/pubs/2008/go_paper.pdf)
27. [↑](#cite_ref-27) Typical [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) architecture, Image by Aphex34, December 16, 2015, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
28. [↑](#cite_ref-28) The fundamental building block of residual networks. Figure 2 in [Kaiming He](https://scholar.google.com/citations?user=DhtAFkwAAAAJ), [Xiangyu Zhang](https://scholar.google.com/citations?user=yuB-cfoAAAAJ&hl=en), [Shaoqing Ren](http://shaoqingren.com/), [Jian Sun](http://www.jiansun.org/) (**2015**). *Deep Residual Learning for Image Recognition*. [arXiv:1512.03385](https://arxiv.org/abs/1512.03385)
29. [↑](#cite_ref-29) [Understand Deep Residual Networks — a simple, modular learning framework that has redefined state-of-the-art](https://blog.waya.ai/deep-residual-learning-9610bb62c355) by [Michael Dietz](https://blog.waya.ai/@waya.ai), [Waya.ai](https://blog.waya.ai/), May 02, 2017
30. [↑](#cite_ref-30) [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2017**). *[Residual Networks for Computer Go](http://ieeexplore.ieee.org/document/7875402/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. PP, No. 99, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/resnet.pdf)
31. [↑](#cite_ref-31) [Deep Residual Networks](https://wiki.tum.de/display/lfdv/Deep+Residual+Networks) from [TUM Wiki](https://wiki.tum.de/), [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich")
32. [↑](#cite_ref-32) [Understanding and visualizing ResNets](https://towardsdatascience.com/understanding-and-visualizing-resnets-442284831be8) by Pablo Ruiz, October 8, 2018
33. [↑](#cite_ref-33) [Richard Sutton](Richard_Sutton "Richard Sutton"), [Andrew Barto](Andrew_Barto "Andrew Barto") (**1998**). *[Reinforcement Learning: An Introduction](http://www.incompleteideas.net/sutton/book/the-book.html)*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [11.1 TD-Gammon](http://www.incompleteideas.net/sutton/book/ebook/node108.html)
34. [↑](#cite_ref-34) [Christopher Clark](Christopher_Clark "Christopher Clark"), [Amos Storkey](Amos_Storkey "Amos Storkey") (**2014**). *Teaching Deep Convolutional Neural Networks to Play Go*. [arXiv:1412.3409](http://arxiv.org/abs/1412.3409)
35. [↑](#cite_ref-35) [Teaching Deep Convolutional Neural Networks to Play Go](http://computer-go.org/pipermail/computer-go/2014-December/007010.html) by [Hiroshi Yamashita](Hiroshi_Yamashita "Hiroshi Yamashita"), [The Computer-go Archives](http://computer-go.org/pipermail/computer-go/), December 14, 2014
36. [↑](#cite_ref-36) [Why Neural Networks Look Set to Thrash the Best Human Go Players for the First Time](http://www.technologyreview.com/view/533496/why-neural-networks-look-set-to-thrash-the-best-human-go-players-for-the-first-time/) | [MIT Technology Review](https://en.wikipedia.org/wiki/MIT_Technology_Review), December 15, 2014
37. [↑](#cite_ref-37) [Teaching Deep Convolutional Neural Networks to Play Go](http://www.talkchess.com/forum/viewtopic.php?t=54663) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), December 16, 2014
38. [↑](#cite_ref-38) [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [David Silver](David_Silver "David Silver") (**2014**). *Move Evaluation in Go Using Deep Convolutional Neural Networks*. [arXiv:1412.6564v1](http://arxiv.org/abs/1412.6564v1)
39. [↑](#cite_ref-39) [Move Evaluation in Go Using Deep Convolutional Neural Networks](http://computer-go.org/pipermail/computer-go/2014-December/007046.html) by [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [The Computer-go Archives](http://computer-go.org/pipermail/computer-go/), December 19, 2014
40. [↑](#cite_ref-40) [AlphaGo | Google DeepMind](http://deepmind.com/alpha-go.html)
41. [↑](#cite_ref-41) [David Silver](David_Silver "David Silver"), [Aja Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Chris J. Maddison](Chris_J._Maddison "Chris J. Maddison"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [George van den Driessche](index.php?title=George_van_den_Driessche&action=edit&redlink=1 "George van den Driessche (page does not exist)"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Veda Panneershelvam](index.php?title=Veda_Panneershelvam&action=edit&redlink=1 "Veda Panneershelvam (page does not exist)"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Sander Dieleman](index.php?title=Sander_Dieleman&action=edit&redlink=1 "Sander Dieleman (page does not exist)"), [Dominik Grewe](index.php?title=Dominik_Grewe&action=edit&redlink=1 "Dominik Grewe (page does not exist)"), [John Nham](index.php?title=John_Nham&action=edit&redlink=1 "John Nham (page does not exist)"), [Nal Kalchbrenner](index.php?title=Nal_Kalchbrenner&action=edit&redlink=1 "Nal Kalchbrenner (page does not exist)"), [Ilya Sutskever](Ilya_Sutskever "Ilya Sutskever"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Madeleine Leach](index.php?title=Madeleine_Leach&action=edit&redlink=1 "Madeleine Leach (page does not exist)"), [Koray Kavukcuoglu](Koray_Kavukcuoglu "Koray Kavukcuoglu"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2016**). *[Mastering the game of Go with deep neural networks and tree search](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 529
42. [↑](#cite_ref-42) [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316511&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 07, 2010
43. [↑](#cite_ref-43) [Kieran Greer](Kieran_Greer "Kieran Greer"), [Piyush Ojha](index.php?title=Piyush_Ojha&action=edit&redlink=1 "Piyush Ojha (page does not exist)"), [David A. Bell](index.php?title=David_A._Bell&action=edit&redlink=1 "David A. Bell (page does not exist)") (**1999**). *A Pattern-Oriented Approach to Move Ordering: the Chessmaps Heuristic*. [ICCA Journal, Vol. 22, No. 1](ICGA_Journal#22_1 "ICGA Journal")
44. [↑](#cite_ref-44) [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Eric Postma](Eric_Postma "Eric Postma"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *[The Neural MoveMap Heuristic in Chess](http://link.springer.com/chapter/10.1007%2F978-3-540-40031-8_11)*. [CG 2002](CG_2002 "CG 2002")
45. [↑](#cite_ref-45) [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015
46. [↑](#cite_ref-46) [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=1) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016
47. [↑](#cite_ref-47) [Omid E. David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu"), [Lior Wolf](index.php?title=Lior_Wolf&action=edit&redlink=1 "Lior Wolf (page does not exist)") (**2016**). *[DeepChess: End-to-End Deep Neural Network for Automatic Learning in Chess](http://link.springer.com/chapter/10.1007%2F978-3-319-44781-0_11)*. [ICAAN 2016](http://icann2016.org/), [Lecture Notes in Computer Science](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science), Vol. 9887, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf preprint](http://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf)
48. [↑](#cite_ref-48) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
49. [↑](#cite_ref-49) [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf) (Japanese with English abstract) [GitHub - asdfjkl/nnue translation](https://github.com/asdfjkl/nnue)
50. [↑](#cite_ref-50) [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
51. [↑](#cite_ref-51) [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
52. [↑](#cite_ref-52) [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020
53. [↑](#cite_ref-53) [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
54. [↑](#cite_ref-54) [Stockfish NNUE – The Complete Guide](http://yaneuraou.yaneu.com/2020/06/19/stockfish-nnue-the-complete-guide/), June 19, 2020 (Japanese and English)
55. [↑](#cite_ref-55) [Rosenblatt's Contributions](http://csis.pace.edu/~ctappert/srd2011/rosenblatt-contributions.htm)
56. [↑](#cite_ref-56) [The abandonment of connectionism in 1969 - Wikipedia](https://en.wikipedia.org/wiki/AI_winter#The_abandonment_of_connectionism_in_1969)
57. [↑](#cite_ref-57) [Frank Rosenblatt](https://en.wikipedia.org/wiki/Frank_Rosenblatt) (**1962**). *[Principles of Neurodynamics: Perceptrons and the Theory of Brain Mechanisms](http://catalog.hathitrust.org/Record/000203591)*. Spartan Books
58. [↑](#cite_ref-58) [Seppo Linnainmaa](Mathematician#SLinnainmaa "Mathematician") (**1976**). *[Taylor expansion of the accumulated rounding error](http://link.springer.com/article/10.1007/BF01931367)*. [BIT Numerical Mathematics](https://en.wikipedia.org/wiki/BIT_Numerical_Mathematics), Vol. 16, No. 2
59. [↑](#cite_ref-59) [Backpropagation from Wikipedia](https://en.wikipedia.org/wiki/Backpropagation)
60. [↑](#cite_ref-60) [Paul Werbos](Mathematician#PWerbos "Mathematician") (**1994**). *The Roots of Backpropagation. From Ordered Derivatives to Neural Networks and Political Forecasting*. [John Wiley & Sons](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
61. [↑](#cite_ref-61) [Neocognitron - Scholarpedia](http://www.scholarpedia.org/article/Neocognitron) by [Kunihiko Fukushima](http://www.scholarpedia.org/article/User:Kunihiko_Fukushima)
62. [↑](#cite_ref-62) [Classical conditioning from Wikipedia](https://en.wikipedia.org/wiki/Classical_conditioning)
63. [↑](#cite_ref-63) [Sepp Hochreiter's Fundamental Deep Learning Problem (1991)](http://people.idsia.ch/~juergen/fundamentaldeeplearningproblem.html) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber"), 2013
64. [↑](#cite_ref-64) [Nici Schraudolph’s go networks](http://satirist.org/learn-game/systems/go-net.html), review by [Jay Scott](Jay_Scott "Jay Scott")
65. [↑](#cite_ref-65) [Re: Evaluation by neural network ?](https://www.stmintz.com/ccc/index.php?id=11893) by [Jay Scott](Jay_Scott "Jay Scott"), [CCC](CCC "CCC"), November 10, 1997
66. [↑](#cite_ref-66) [Long short term memory from Wikipedia](https://en.wikipedia.org/wiki/Long_short_term_memory)
67. [↑](#cite_ref-67) [Tsumego from Wikipedia](https://en.wikipedia.org/wiki/Tsumego)
68. [↑](#cite_ref-68) [Helmholtz machine from Wikipedia](https://en.wikipedia.org/wiki/Helmholtz_machine)
69. [↑](#cite_ref-69) [Who introduced the term “deep learning” to the field of Machine Learning](https://plus.google.com/100849856540000067209/posts/7N6z251w2Wd?pid=6127540521703625346&oid=100849856540000067209) by [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber"), [Google+](https://plus.google.com/100849856540000067209), March 18, 2015
70. [↑](#cite_ref-70) [Presentation for a neural net learning chess program](https://www.stmintz.com/ccc/index.php?id=358770) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 06, 2004
71. [↑](#cite_ref-71) [Clément Farabet | Code](http://www.clement.farabet.net/code.html)
72. [↑](#cite_ref-72) [Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/) by [Tambet Matiisen](http://www.nervanasys.com/author/tambet/), [Nervana](http://www.nervanasys.com/), December 21, 2015
73. [↑](#cite_ref-73) [high dimensional optimization](https://groups.google.com/d/msg/fishcooking/wOfRuzTSi_8/VgjN8MmSBQAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 27, 2019
74. [↑](#cite_ref-74) [Generative adversarial networks from Wikipedia](https://en.wikipedia.org/wiki/Generative_adversarial_networks)
75. [↑](#cite_ref-75) [Teaching Deep Convolutional Neural Networks to Play Go](http://computer-go.org/pipermail/computer-go/2014-December/007010.html) by [Hiroshi Yamashita](Hiroshi_Yamashita "Hiroshi Yamashita"), [The Computer-go Archives](http://computer-go.org/pipermail/computer-go/), December 14, 2014
76. [↑](#cite_ref-76) [Teaching Deep Convolutional Neural Networks to Play Go](http://www.talkchess.com/forum/viewtopic.php?t=54663) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), December 16, 2014
77. [↑](#cite_ref-77) [Arasan 19.2](http://www.talkchess.com/forum/viewtopic.php?t=61948) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 03, 2016 » [Arasan's Tuning](Arasan#Tuning "Arasan")
78. [↑](#cite_ref-78) [GitHub - BarakOshri/ConvChess: Predicting Moves in Chess Using Convolutional Neural Networks](https://github.com/BarakOshri/ConvChess)
79. [↑](#cite_ref-79) [ConvChess CNN](http://www.talkchess.com/forum/viewtopic.php?t=63458) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), March 15, 2017
80. [↑](#cite_ref-80) [Jürgen Schmidhuber](J%C3%BCrgen_Schmidhuber "Jürgen Schmidhuber") (**2015**) *[Critique of Paper by "Deep Learning Conspiracy" (Nature 521 p 436)](http://people.idsia.ch/~juergen/deep-learning-conspiracy.html)*.
81. [↑](#cite_ref-81) [How Facebook’s AI Researchers Built a Game-Changing Go Engine | MIT Technology Review](http://www.technologyreview.com/view/544181/how-facebooks-ai-researchers-built-a-game-changing-go-engine/?utm_campaign=socialsync&utm_medium=social-post&utm_source=facebook), December 04, 2015
82. [↑](#cite_ref-82) [Combining Neural Networks and Search techniques (GO)](http://www.talkchess.com/forum/viewtopic.php?t=58514) by Michael Babigian, [CCC](CCC "CCC"), December 08, 2015
83. [↑](#cite_ref-83) [DeepChess: Another deep-learning based chess program](http://www.talkchess.com/forum/viewtopic.php?t=61748) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), October 17, 2016
84. [↑](#cite_ref-84) [ICANN 2016 | Recipients of the best paper awards](http://icann2016.org/index.php/conference-programme/recipients-of-the-best-paper-awards/)
85. [↑](#cite_ref-85) [Jigsaw puzzle from Wikipedia](https://en.wikipedia.org/wiki/Jigsaw_puzzle)
86. [↑](#cite_ref-86) [CMA-ES from Wikipedia](https://en.wikipedia.org/wiki/CMA-ES)
87. [↑](#cite_ref-87) [Re: Minic version 3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75665&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 03, 2020 » [Minic 3](Minic#Minic_3 "Minic"), [Seer 1.1](Seer "Seer")
88. [↑](#cite_ref-88) [catastrophic forgetting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70704) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 09, 2019
89. [↑](#cite_ref-89) [Using GAN to play chess](http://www.talkchess.com/forum/viewtopic.php?t=63252) by Evgeniy Zheltonozhskiy, [CCC](CCC "CCC"), February 23, 2017
90. [↑](#cite_ref-90) [GitHub - paintception/DeepChess](https://github.com/paintception/DeepChess)
91. [↑](#cite_ref-91) [AlphaGo Zero: Learning from scratch](https://deepmind.com/blog/alphago-zero-learning-scratch/) by [Demis Hassabis](Demis_Hassabis "Demis Hassabis") and [David Silver](David_Silver "David Silver"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), October 18, 2017
92. [↑](#cite_ref-92) [Google's AlphaGo team has been working on chess](http://www.talkchess.com/forum/viewtopic.php?t=65909) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [CCC](CCC "CCC"), December 06, 2017
93. [↑](#cite_ref-93) [Residual Networks for Computer Go](http://www.talkchess.com/forum/viewtopic.php?t=65923) by Brahim Hamadicharef, [CCC](CCC "CCC"), December 07, 2017
94. [↑](#cite_ref-94) [Translation of Yu Nasu's NNUE paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76250) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), January 07, 2021
95. [↑](#cite_ref-95) [AlphaZero: Shedding new light on the grand games of chess, shogi and Go](https://deepmind.com/blog/alphazero-shedding-new-light-grand-games-chess-shogi-and-go/) by [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser") and [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), December 03, 2018
96. [↑](#cite_ref-96) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021
97. [↑](#cite_ref-97) [Acquisition of Chess Knowledge in AlphaZero](https://en.chessbase.com/post/acquisition-of-chess-knowledge-in-alphazero), [ChessBase News](ChessBase "ChessBase"), November 18, 2021
98. [↑](#cite_ref-98) [Alois Heinz](Alois_Heinz "Alois Heinz") (**1994**). *[Efficient Neural Net α-β-Evaluators](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.55.3994)*. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.55.3994&rep=rep1&type=pdf)
99. [↑](#cite_ref-99)  [Mathieu Autonès](index.php?title=Mathieu_Auton%C3%A8s&action=edit&redlink=1 "Mathieu Autonès (page does not exist)"), [Aryel Beck](index.php?title=Aryel_Beck&action=edit&redlink=1 "Aryel Beck (page does not exist)"), [Phillippe Camacho](index.php?title=Phillippe_Camacho&action=edit&redlink=1 "Phillippe Camacho (page does not exist)"), [Nicolas Lassabe](index.php?title=Nicolas_Lassabe&action=edit&redlink=1 "Nicolas Lassabe (page does not exist)"), [Hervé Luga](index.php?title=Herv%C3%A9_Luga&action=edit&redlink=1 "Hervé Luga (page does not exist)"), [François Scharffe](index.php?title=Fran%C3%A7ois_Scharffe&action=edit&redlink=1 "François Scharffe (page does not exist)") (**2004**). *[Evaluation of Chess Position by Modular Neural network Generated by Genetic Algorithm](http://link.springer.com/chapter/10.1007/978-3-540-24650-3_1)*. [EuroGP 2004](http://www.informatik.uni-trier.de/~ley/db/conf/eurogp/eurogp2004.html#AutonesBCLLS04)
100. [↑](#cite_ref-100) [Naive Bayes classifier from Wikipedia](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
101. [↑](#cite_ref-101) [GitHub - pluskid/Mocha.jl: Deep Learning framework for Julia](https://github.com/pluskid/Mocha.jl)
102. [↑](#cite_ref-102) [Rectifier (neural networks) from Wikipedia](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))
103. [↑](#cite_ref-103) [Muthuraman Chidambaram](index.php?title=Muthuraman_Chidambaram&action=edit&redlink=1 "Muthuraman Chidambaram (page does not exist)"), [Yanjun Qi](index.php?title=Yanjun_Qi&action=edit&redlink=1 "Yanjun Qi (page does not exist)") (**2017**). *Style Transfer Generative Adversarial Networks: Learning to Play Chess Differently*. [arXiv:1702.06762v1](https://arxiv.org/abs/1702.06762v1)
104. [↑](#cite_ref-104) [Yann Dauphin](Mathematician#YDauphin "Mathematician"), [Razvan Pascanu](Mathematician#RPascanu "Mathematician"), [Caglar Gulcehre](Mathematician#CGulcehre "Mathematician"), [Kyunghyun Cho](Mathematician#KCho "Mathematician"), [Surya Ganguli](Mathematician#SGanguli "Mathematician"), [Yoshua Bengio](Mathematician#YBengio "Mathematician") (**2014**). *Identifying and attacking the saddle point problem in high-dimensional non-convex optimization*. [arXiv:1406.2572](https://arxiv.org/abs/1406.2572)
105. [↑](#cite_ref-105) [kernel launch latency - CUDA / CUDA Programming and Performance - NVIDIA Developer Forums](https://forums.developer.nvidia.com/t/kernel-launch-latency/62455) by LukeCuda, June 18, 2018
106. [↑](#cite_ref-106) [PyTorch from Wikipedia](https://en.wikipedia.org/wiki/PyTorch)
107. [↑](#cite_ref-107) [A worked example of backpropagation using Javascript](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76885) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), March 16, 2021
108. [↑](#cite_ref-108) [yet another NN library](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77061) by lucasart, [CCC](CCC "CCC"), April 11, 2021
109. [↑](#cite_ref-109) [erikbern/deep-pink · GitHub](https://github.com/erikbern/deep-pink)
110. [↑](#cite_ref-110) [Neural networks (NN) explained](http://www.talkchess.com/forum/viewtopic.php?t=66076) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), December 20, 2017

**[Up one Level](Learning "Learning")**







 
