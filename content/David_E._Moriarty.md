---
title: David E. Moriarty
---
**[Home](Home "Home") * [People](People "People") * David E. Moriarty**

**David Eric Moriarty**,

an American computer scientist an Ph.D. alumni from [University of Texas at Austin](https://en.wikipedia.org/wiki/University_of_Texas_at_Austin) <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
During the 90s, along with his advisor, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen"), David E. Moriarty worked on [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") by [Symbiotic](https://en.wikipedia.org/wiki/Symbiosis), Adaptive [NeuroEvolution](https://en.wikipedia.org/wiki/Neuroevolution) dubbed SANE, also topic of his Ph.D. thesis <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## SANE

SANE ([Symbiotic](https://en.wikipedia.org/wiki/Symbiosis), Adaptive [NeuroEvolution](https://en.wikipedia.org/wiki/Neuroevolution)) evolves [neural networks](Neural_Networks "Neural Networks") with [genetic algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming") for [sequential decision tasks](https://en.wikipedia.org/wiki/Sequential_decision_making),
also applied to the [games](Games "Games") of [Othello](Othello "Othello") and [Go](Go "Go").
SANE selects a population of hidden neurons of a "vanilla" three-layer feed-forward neural network with the connections and weights in both directions,
performing following basic steps in one generation <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++
1. Clear all fitness values from each neuron
2.   Select neurons randomly from the population
3.   Create a neural network from the selected neurons
4.   Evaluate the network in the given task
5.   Add the network's score to each selected neuron's fitness variable
6. Repeat steps 2-5 a sufficient number of times
7. Get each neuron's average fitness score by dividing its total fitness values by the number of networks in which it was implemented
8. Perform crossover operations on the population based on the average fitness value of each neuron

```

For Go and Othello, the input layer sees the board configuration, while the output layer indicates the goodness of each possible move by an output neuron associated with each space or point of the board.
However the research was conducted a few years before the [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") revolution appeared in computer Go, not to mention the [deep learning](Deep_Learning "Deep Learning") breakthrough.
In the [alpha-beta](Alpha-Beta "Alpha-Beta") search of the Othello experiment, the neural network [orders the moves](Move_Ordering "Move Ordering"), and further controls whether moves are [pruned forward](Pruning "Pruning") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Selected Publications

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

- David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Improving Game-Tree Search with Evolutionary Neural Networks](https://ieeexplore.ieee.org/document/349900)*. [ICEC 1994](https://dblp.uni-trier.de/db/conf/icec/icec1994-1.html)
- David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Evolving Neural Networks to focus Minimax Search](http://nn.cs.utexas.edu/?moriarty:aaai94)*. [AAAI-94](Conferences#AAAI-94 "Conferences") » [Othello](Othello "Othello")
- David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1995**). *[Discovering Complex Othello Strategies Through Evolutionary Neural Networks](http://nn.cs.utexas.edu/?moriarty:connsci95)*. [Connection Science](https://www.scimagojr.com/journalsearch.php?q=24173&tip=sid), Vol. 7
- David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1996**). *[Efficient Reinforcement Learning through Symbiotic Evolution](http://nn.cs.utexas.edu/?moriarty:mlj96)*. [Machine Learning](<https://en.wikipedia.org/wiki/Machine_Learning_(journal)>), Vol. 22 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- David E. Moriarty (**1997**). *[Symbiotic Evolution of Neural Networks in Sequential Decision Tasks](http://nn.cs.utexas.edu/?moriarty:phd97)*. Ph.D. thesis, [University of Texas at Austin](https://en.wikipedia.org/wiki/University_of_Texas_at_Austin), advisor [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen")
- [Norman Richards](index.php?title=Norman_Richards&action=edit&redlink=1 "Norman Richards (page does not exist)"), David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1998**). *[Evolving Neural Networks to Play Go](http://nn.cs.utexas.edu/?richards:apin98)*. [Applied Intelligence](https://www.springer.com/journal/10489), Vol. 8, No. 1

## External Links

- [NNRG People - David E. Moriarty](http://nn.cs.utexas.edu/?moriarty)
- [AI-Lab People - David E. Moriarty](http://www.cs.utexas.edu/users/ai-lab/?moriarty)
- [David Moriarty - The Mathematics Genealogy Project](https://www.mathgenealogy.org/id.php?id=128214)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [NNRG People - David E. Moriarty](http://nn.cs.utexas.edu/?moriarty)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> David E. Moriarty (**1997**). *[Symbiotic Evolution of Neural Networks in Sequential Decision Tasks](http://nn.cs.utexas.edu/?moriarty:phd97)*. Ph.D. thesis, [University of Texas at Austin](https://en.wikipedia.org/wiki/University_of_Texas_at_Austin), advisor [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1996**). *[Efficient Reinforcement Learning through Symbiotic Evolution](http://nn.cs.utexas.edu/?moriarty:mlj96)*. [Machine Learning](<https://en.wikipedia.org/wiki/Machine_Learning_(journal)>), Vol. 22
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> David E. Moriarty, [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Evolving Neural Networks to focus Minimax Search](http://nn.cs.utexas.edu/?moriarty:aaai94)*. [AAAI-94](Conferences#AAAI-94 "Conferences")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [dblp: David E. Moriarty](https://dblp.uni-trier.de/pers/hd/m/Moriarty:David_E=)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Inverted pendulum from Wikipedia](https://en.wikipedia.org/wiki/Inverted_pendulum)

**[Up one Level](People "People")**

