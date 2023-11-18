---
title: NeuroChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* NeuroChess**


**NeuroChess**,  

an experimental program which [learns](Learning#Programs "Learning") to play chess from the final outcome of games written by [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") in the early mid 90s, at that time at [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") supported by [Tom Mitchell](Tom_Mitchell "Tom Mitchell") and in particular on the domain of chess advised by [Hans Berliner](Hans_Berliner "Hans Berliner") <a id="cite-note-1" href="#cite-ref-1">[1]</a> . NeuroChess took its [search algorithm](Search "Search") from [GNU Chess](GNU_Chess "GNU Chess") but its [evaluation](Evaluation "Evaluation") was based on [neural networks](Neural_Networks "Neural Networks") to integrate [inductive](https://en.wikipedia.org/wiki/Inductive_reasoning) neural network learning, [temporal difference learning](Temporal_Difference_Learning "Temporal Difference Learning"), and a variant of [explanation-based learning](https://en.wikipedia.org/wiki/Explanation-based_learning) <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> .



## Conclusion


After training M with 120,000 grandmaster games, and training V with a further 2400 games, NeuroChess managed to beat [GNU Chess](GNU_Chess "GNU Chess") in about 13% of the time at fixed depth 2 games, but only in 10% without EBNN. Further, computing a large neural network function took two [orders of magnitude](https://en.wikipedia.org/wiki/Order_of_magnitude) longer than evaluating the linear evaluation function of GNU Chess.



## See also


* [Chess Engines with Neural Networks](Neural_Networks#engines "Neural Networks")
* [Learning Chess Programs](Learning#Programs "Learning")


## Publications


* [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. in [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro"), [David S. Touretzky](https://en.wikipedia.org/wiki/David_S._Touretzky), [Todd K. Leen](http://mitpress.mit.edu/authors/todd-k-leen) (eds.) Advances in Neural Information Processing Systems 7, [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [pdf](http://papers.nips.cc/paper/1007-learning-to-play-the-game-of-chess.pdf)
* [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (eds.) (**2001**). *[Machines that Learn to Play Games](http://www.novapublishers.org/catalog/product_info.php?products_id=720)*. Advances in Computation: Theory and Practice, Vol. 8,. [NOVA Science Publishers](https://en.wikipedia.org/wiki/Nova_Publishers)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk") (**2007**). *[Computational Intelligence in Mind Games](https://link.springer.com/chapter/10.1007/978-3-540-71984-7_15)*. in [Włodzisław Duch](index.php?title=W%C5%82odzis%C5%82aw_Duch&action=edit&redlink=1 "Włodzisław Duch (page does not exist)"), [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk") (eds.) *[Challenges for Computational Intelligence](https://link.springer.com/book/10.1007%2F978-3-540-71984-7)*. [Studies in Computational Intelligence](https://link.springer.com/bookseries/7092), Vol. 63, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Marco Block](Marco_Block-Berlitz "Marco Block-Berlitz"), Maro Bader, [Ernesto Tapia](http://page.mi.fu-berlin.de/tapia/), Marte Ramírez, Ketill Gunnarsson, Erik Cuevas, Daniel Zaldivar, [Raúl Rojas](Ra%C3%BAl_Rojas "Raúl Rojas") (**2008**). *Using Reinforcement Learning in Chess Engines*. Concibe Science 2008, [Research in Computing Science](http://www.micai.org/rcs/): Special Issue in Electronics and Biomedical Engineering, Computer Science and Informatics, Vol. 35, [pdf](http://page.mi.fu-berlin.de/block/concibe2008.pdf)
* [Jacek Mańdziuk](Jacek_Ma%C5%84dziuk "Jacek Mańdziuk") (**2010**). *[Knowledge-Free and Learning-Based Methods in Intelligent Game Playing](https://link.springer.com/book/10.1007%2F978-3-642-11678-0)*. [Studies in Computational Intelligence](http://link.springer.com/bookseries/7092), Vol. 276, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), pp. 124
* [István Szita](Istv%C3%A1n_Szita "István Szita") (**2012**). *[Reinforcement Learning in Games](https://link.springer.com/chapter/10.1007%2F978-3-642-27645-3_17)*. in [Marco Wiering](Marco_Wiering "Marco Wiering"), [Martijn Van Otterlo](http://martijnvanotterlo.nl/) (eds.). *[Reinforcement learning: State-of-the-art](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=xVas0I8AAAAJ&citation_for_view=xVas0I8AAAAJ:abG-DnoFyZgC)*. [Adaptation, Learning, and Optimization, Vol. 12](https://link.springer.com/book/10.1007/978-3-642-27645-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


## Forum Posts


* [Re: Chess Evaluation](http://talkchess.com/forum/viewtopic.php?t=39342&start=1) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 11, 2011
* [Sal or neurochess](http://www.talkchess.com/forum/viewtopic.php?t=40290) by ethan ara, [CCC](CCC "CCC"), September 06, 2011


## External Links


* [Sebastian Thrun’s NeuroChess](http://satirist.org/learn-game/systems/neurochess.html) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott"), September 2000


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. Acknowledgment
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun"), [Tom Mitchell](Tom_Mitchell "Tom Mitchell") (**1993**). *Integrating Inductive Neural Network Learning and Explanation-Based Learning*. [IJCAI 1993](Conferences#IJCAI1993 "Conferences"), [zipped ps](http://robots.stanford.edu/papers/thrun.EBNN_ijcai93.ps.gz)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *Explanation-Based Neural Network Learning - A Lifelong Learning Approach*. Ph.D. thesis, [University of Bonn](https://en.wikipedia.org/wiki/University_of_Bonn)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Figure 2 from [Sebastian Thrun](Sebastian_Thrun "Sebastian Thrun") (**1995**). *[Learning to Play the Game of Chess](http://robots.stanford.edu/papers/thrun.nips7.neuro-chess.html)*. [pdf](http://papers.nips.cc/paper/1007-learning-to-play-the-game-of-chess.pdf)

**[Up one level](Engines "Engines")**







 
