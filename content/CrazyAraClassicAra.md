---
title: CrazyAraClassicAra
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CrazyAra**

\[ [Ara chloropterus](https://en.wikipedia.org/wiki/Red-and-green_macaw) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**CrazyAra**, (ClassicAra, MultiAra)

a family of [UCI](UCI "UCI") compatible [chess variant](Chess#Variants "Chess") [open source](Category:Open_Source "Category:Open Source") engines licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").
CrazyAra started as a [semester](https://en.wikipedia.org/wiki/Academic_term#Synonyms) project by [Johannes Czech](Johannes_Czech "Johannes Czech"), [Moritz Willig](Moritz_Willig "Moritz Willig") and [Alena Beyer](Alena_Beyer "Alena Beyer") for the course *Deep Learning: Methods and Architectures* at the [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology") in summer 2018, headed by [Kristian Kersting](Kristian_Kersting "Kristian Kersting") and [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz").
The project was inspired by the [deep learning](Deep_Learning "Deep Learning") and [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") techniques described in [DeepMind's](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)") [AlphaZero](AlphaZero "AlphaZero") papers
<a id="cite-note-2" href="#cite-ref-2">[2]</a>
<a id="cite-note-3" href="#cite-ref-3">[3]</a>,
the goal to train a [deep](Neural_Networks#Deep "Neural Networks") [convolutional neural network](Neural_Networks#Convolutional "Neural Networks") to play [Crazyhouse](Crazyhouse "Crazyhouse") trained by [supervised learning](Supervised_Learning "Supervised Learning") on human data - the initial version of CrazyAra entirely written in [Python](Python "Python") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
In December 2018, CrazyAra won a five game Crazyhouse online-match versus [Justin Tan](https://en.wikipedia.org/wiki/Justin_Tan) aka JannLee with 4-1
<a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Continuation

As subject of his master thesis <a id="cite-note-7" href="#cite-ref-7">[7]</a>,
Johannes Czech continued the development in porting the engine to [C++](Cpp "Cpp") and to further apply [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") to Crazyhouse and other chess variants including [Chess960](Chess960 "Chess960").
While the initial version uses [Python-chess](Python-chess "Python-chess") by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), the C++ version uses a multi variant [Stockfish](Stockfish "Stockfish") fork by [Daniel Dugovic](index.php?title=Daniel_Dugovic&action=edit&redlink=1 "Daniel Dugovic (page does not exist)") <a id="cite-note-8" href="#cite-ref-8">[8]</a>
for [move generation](Move_Generation "Move Generation"), [board representation](Board_Representation "Board Representation") and [Syzygy](Syzygy_Bases "Syzygy Bases") parsing.
To feature more chess variants, more recently [Fairy-Stockfish](index.php?title=Fairy-Stockfish&action=edit&redlink=1 "Fairy-Stockfish (page does not exist)") by [Fabian Fichter](index.php?title=Fabian_Fichter&action=edit&redlink=1 "Fabian Fichter (page does not exist)") was incorporated <a id="cite-note-9" href="#cite-ref-9">[9]</a>,
as for instance used in [Maximilian Langer's](Maximilian_Langer "Maximilian Langer") [Xiangqi](Chinese_Chess "Chinese Chess") version of CrazyAra <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## Network

CrazyAra uses [MXNet](https://en.wikipedia.org/wiki/Apache_MXNet) as it's deep learning framework - with three NN back-ends to run the NN inference available, [Nvidia's](Nvidia "Nvidia") TensorRT built on [CUDA](https://en.wikipedia.org/wiki/CUDA) ([GPU](GPU "GPU") only), MXNet and [Torch](<https://en.wikipedia.org/wiki/Torch_(machine_learning)>) <a id="cite-note-11" href="#cite-ref-11">[11]</a>.
The input representation is a hybrid between chess and [Shogi](Shogi "Shogi") and compared to the AlphaZero description avoids the history of past board representations <a id="cite-note-12" href="#cite-ref-12">[12]</a>.
In CrazyAra v0.2.0 a newly designed architecture was used which is called RISE ([ResneXt](https://en.wikipedia.org/wiki/Residual_neural_network), Inception, Squeeze, Excitation). The model uses mixed depth-wise convolutional kernels, efficient squeeze excitation modules, use of 5x5 convolutions in deeper layers, and [hard sigmoid](https://en.wikipedia.org/wiki/Hard_sigmoid) instead of [sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function) [activation functions](https://en.wikipedia.org/wiki/Activation_function).
The proposed model architecture has fewer parameters, faster inference and training time while maintaining an equal amount of depth compared to the architecture proposed by DeepMind (19 residual layers with 256 filters) <a id="cite-note-13" href="#cite-ref-13">[13]</a>.
Similar to AlphaZero, the output is represented by a value and policy head, the latter implemented as vector of moves <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>.

## Monte-Carlo Graph Search

CrazyAra optionally features an improvement of AlphaZero's [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") / [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin") algorithm, considering [transpositions](Transposition "Transposition") -
dubbed **Monte-Carlo Graph Search** based on a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) instead of a [tree structure](https://en.wikipedia.org/wiki/Tree_structure) <a id="cite-note-16" href="#cite-ref-16">[16]</a> <a id="cite-note-17" href="#cite-ref-17">[17]</a>.

## ClassicAra

**ClassicAra** is a version of CrazyAra to play classical chess as well as [Chess960](Chess960 "Chess960"). ClassicAra had its tournament debut as [TCEC Season 21](TCEC_Season_21 "TCEC Season 21") in Spring 2021, not yet improved by [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") <a id="cite-note-18" href="#cite-ref-18">[18]</a>.

## MultiAra

**MultiAra**, released in August 2021, is a version of the Ara project which supports all [chess variants](Chess#Variants "Chess") available on [Lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)") <a id="cite-note-19" href="#cite-ref-19">[19]</a>.

## See also

- [AlphaZero](AlphaZero "AlphaZero")
- [Crazyhouse](Crazyhouse "Crazyhouse")
- [Deep Learning](Deep_Learning "Deep Learning")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [Parrot](Parrot "Parrot")
- [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
- [Supervised Learning](Supervised_Learning "Supervised Learning")

## Publications

- [Johannes Czech](Johannes_Czech "Johannes Czech") (**2019**). *Deep Reinforcement Learning for Crazyhouse*. Master thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/czech2019deep.pdf)
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Moritz Willig](Moritz_Willig "Moritz Willig"), [Alena Beyer](Alena_Beyer "Alena Beyer"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2019**). *Learning to play the Chess Variant Crazyhouse above World Champion Level with Deep Neural Networks and Human Data*. [arXiv:1908.06660](https://arxiv.org/abs/1908.06660)
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Moritz Willig](Moritz_Willig "Moritz Willig"), [Alena Beyer](Alena_Beyer "Alena Beyer"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2020**). *[Learning to Play the Chess Variant Crazyhouse Above World Champion Level With Deep Neural Networks and Human Data](https://www.frontiersin.org/articles/10.3389/frai.2020.00024/full)*. [Frontiers in Artificial Intelligence](https://www.frontiersin.org/journals/artificial-intelligence#)
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Patrick Korus](Patrick_Korus "Patrick Korus"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting") (**2020**). *Monte-Carlo Graph Search for AlphaZero*. [arXiv:2012.11045](https://arxiv.org/abs/2012.11045)
- [Johannes Czech](Johannes_Czech "Johannes Czech"), [Patrick Korus](Patrick_Korus "Patrick Korus"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting") (**2021**). *[Improving AlphaZero Using Monte-Carlo Graph Search](https://ojs.aaai.org/index.php/ICAPS/article/view/15952)*. [Proceedings of the Thirty-First International Conference on Automated Planning and Scheduling](https://ojs.aaai.org/index.php/ICAPS/issue/view/380), Vol. 31, [pdf](https://www.ml.informatik.tu-darmstadt.de/papers/czech2021icaps_mcgs.pdf)
- [Maximilian Langer](Maximilian_Langer "Maximilian Langer") (**2021**). *Evaluation of Monte-Carlo Tree Search for Xiangqi*. B.Sc. thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/langer2021xiangqi.pdf) » [Xiangqi](Chinese_Chess "Chinese Chess")
- [Maximilian Alexander Gehrke](index.php?title=Maximilian_Alexander_Gehrke&action=edit&redlink=1 "Maximilian Alexander Gehrke (page does not exist)") (**2021**). *Assessing Popular Chess Variants Using Deep Reinforcement Learning*. Master thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/gehrke2021assessing.pdf)

## Forum Posts

- [CrazyAra Crazyhouse UCI running on WinBoard 4.8.0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70861) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), May 30, 2019
- [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=310) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 21, 2019
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=199) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), April 05, 2021
- [ClassicAra Chess Engine..World Record Download!!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77020) by supersharp77, [CCC](CCC "CCC"), April 06, 2021

[Re: ClassicAra Chess Engine..World Record Download!!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77020&start=58) by [Johannes Czech](Johannes_Czech "Johannes Czech"), [CCC](CCC "CCC"), May 20, 2021
[Re: ClassicAra Chess Engine..World Record Download!!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77020&start=70) by [Johannes Czech](Johannes_Czech "Johannes Czech"), [CCC](CCC "CCC"), May 25, 2021 <a id="cite-note-20" href="#cite-ref-20">[20]</a>

- [Has CrazyAra really improved because of MTGS ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77670) by George Pichard, [CCC](CCC "CCC"), July 08, 2021
- [CrazyAra, ClassicAra, MultiAra 0.9.5 release](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78027) by [Johannes Czech](Johannes_Czech "Johannes Czech"), August 26, 2021

## External Links

## Chess Engine

- [CrazyAra - Crazyhouse Chess Engine](https://crazyara.org/)
- [Rise of light - CrazyAra - Chess Engine](https://rise-of-light.de/projects/crazyara.html)

### GitHub

- [GitHub - QueensGambit/CrazyAra: A Deep Learning UCI-Chess Variant Engine written in C++ & Python](https://github.com/QueensGambit/CrazyAra)
- [Home · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki)
- [GitHub - QueensGambit/CrazyAra-Engine: CrazyAra - A Deep Learning UCI-Chess Variant Engine written in C++](https://github.com/QueensGambit/CrazyAra-Engine)

### Reports

- [Crazyhouse Chess: CrazyAra plays JannLee for Christmas](https://zhchess.blogspot.com/2018/12/crazyara-plays-jannlee-for-christmas.html), December 26, 2018
- [Student Bot beats Crazyhouse World Champion](http://www.ke.tu-darmstadt.de/news/student-bot-beats-crazyhouse-champion), [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology")
- [Schachmatt durch „CrazyAra“ – Informatik – Technische Universität Darmstadt](https://www.informatik.tu-darmstadt.de/fb20/aktuelles_fb20/fb20_neuigkeiten/neuigkeiten_fb20_details_145920.de.jsp), February 19, 2019 (German)
- [Schachmatt durch CrazyAra: Künstliche Intelligenz schlägt mehrfachen Weltmeister im Einsetzschach](https://nachrichten.idw-online.de/2019/02/19/schachmatt-durch-crazyara-kuenstliche-intelligenz-schlaegt-mehrfachen-weltmeister-im-einsetzschach/) by [Kristian Kersting](Kristian_Kersting "Kristian Kersting"), [Informationsdienst Wissenschaft](https://en.wikipedia.org/wiki/Informationsdienst_Wissenschaft), February 19, 2019 (German)
- [Darmstädter Studenten entwickeln Schach-Bot](https://www.echo-online.de/lokales/darmstadt/darmstadter-studenten-entwickeln-schach-bot_20056672) by Karin Walz, [Echo](https://www.echo-online.de/), April 02, 2019 (German)

## Misc

- [Ara (bird) from Wikipedia](<https://en.wikipedia.org/wiki/Ara_(bird)>)
- [Ara from Wikipedia](https://en.wikipedia.org/wiki/Ara)
- [Weather Report](Category:Weather_Report "Category:Weather Report") - [Birdland](<https://en.wikipedia.org/wiki/Birdland_(song)>), [The Midnight Special](<https://en.wikipedia.org/wiki/The_Midnight_Special_(TV_series)>), April 1977, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

lineup: [Joe Zawinul](Category:Joe_Zawinul "Category:Joe Zawinul"), [Wayne Shorter](Category:Wayne_Shorter "Category:Wayne Shorter"), [Jaco Pastorius](Category:Jaco_Pastorius "Category:Jaco Pastorius"), [Alex Acuña](https://en.wikipedia.org/wiki/Alex_Acu%C3%B1a), [Manolo Badrena](https://en.wikipedia.org/wiki/Manolo_Badrena)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Red-and-green macaw](https://en.wikipedia.org/wiki/Red-and-green_macaw) in [Brookfield Zoo](https://en.wikipedia.org/wiki/Brookfield_Zoo), [Photo](https://commons.wikimedia.org/wiki/File:Ara_chloroptera_-Brookfield_Zoo-8.jpg) by [Nimesh M](https://www.flickr.com/photos/22321795@N04), July 05, 2008, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2018**). *[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](http://science.sciencemag.org/content/362/6419/1140)*. [Science](<https://en.wikipedia.org/wiki/Science_(journal)>), Vol. 362, No. 6419
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [GitHub - QueensGambit/CrazyAra: A Deep Learning UCI-Chess Variant Engine written in C++ & Python](https://github.com/QueensGambit/CrazyAra)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [CrazyAra Crazyhouse](https://lichess.org/study/uAJmnF3w)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Crazyhouse Chess: CrazyAra plays JannLee for Christmas](https://zhchess.blogspot.com/2018/12/crazyara-plays-jannlee-for-christmas.html), December 26, 2018
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Johannes Czech](Johannes_Czech "Johannes Czech") (**2019**). *Deep Reinforcement Learning for Crazyhouse*. Master thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/czech2019deep.pdf)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [GitHub - ddugovic/Stockfish: BETA multi-variant fork of popular UCI chess engine; final release for now](https://github.com/ddugovic/Stockfish)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Releases · QueensGambit/CrazyAra · GitHub](https://github.com/QueensGambit/CrazyAra/releases)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Maximilian Langer](Maximilian_Langer "Maximilian Langer") (**2021**). *Evaluation of Monte-Carlo Tree Search for Xiangqi*. B.Sc. thesis, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](https://ml-research.github.io/papers/langer2021xiangqi.pdf)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [2. Build neural network inference library · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/2.-Build-neural-network-inference-library)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Input representation · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/Input-representation)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Model architecture · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/Model-architecture)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Output representation · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/Output-representation)
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Network visualization · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/Network-visualization)
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Johannes Czech](Johannes_Czech "Johannes Czech"), [Patrick Korus](Patrick_Korus "Patrick Korus"), [Kristian Kersting](Kristian_Kersting "Kristian Kersting") (**2020**). *Monte-Carlo Graph Search for AlphaZero*. [arXiv:2012.11045](https://arxiv.org/abs/2012.11045)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Engine settings · QueensGambit/CrazyAra Wiki · GitHub](https://github.com/QueensGambit/CrazyAra/wiki/Engine-settings)
1. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Re: ClassicAra Chess Engine..World Record Download!!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77020&start=58) by [Johannes Czech](Johannes_Czech "Johannes Czech"), [CCC](CCC "CCC"), May 20, 2021
1. <a id="cite-ref-19" href="#cite-note-19">↑</a> [CrazyAra, ClassicAra, MultiAra 0.9.5 release](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78027) by [Johannes Czech](Johannes_Czech "Johannes Czech"), August 26, 2021
1. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Drofa 3.0.0 vs ClassicAra 0.9.2.post1 - TCEC Season 21 - League 4](https://tcec-chess.com/#div=l4&game=127&season=21)

**[Up one Level](Engines "Engines")**

