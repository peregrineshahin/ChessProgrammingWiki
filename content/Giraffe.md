---
title: Giraffe
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Giraffe**

[](https://en.wikipedia.org/wiki/File:The_Burning_Giraffe.jpg) [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí") - [The Burning Giraffe](https://en.wikipedia.org/wiki/The_Burning_Giraffe) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Giraffe**,

an experimental [open source chess engine](Category:Open_Source "Category:Open Source") by [Matthew Lai](Matthew_Lai "Matthew Lai") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), written in [C++11](Cpp "Cpp") and based on [deep learning](Deep_Learning "Deep Learning"), which is topic of Matthew's master's thesis in August 2015 <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Giraffe uses the [Eigen linear algebra library](https://en.wikipedia.org/wiki/Eigen_%28C%2B%2B_library%29) <a id="cite-note-4" href="#cite-ref-4">[4]</a> , and [Pradyumna Kannan's](Pradu_Kannan "Pradu Kannan") [magic move generator](Magic_Bitboards "Magic Bitboards") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. As employee of [Google](index.php?title=Google&action=edit&redlink=1 "Google (page does not exist)") [DeepMind](index.php?title=DeepMind&action=edit&redlink=1 "DeepMind (page does not exist)"), Matthew Lai announced the discontinuation of the Giraffe project in January 2016 <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Description

Giraffe's [evaluation function](Evaluation_Function "Evaluation Function") is a [deep neural network](Neural_Networks#Deep "Neural Networks") trained by [TDLeaf](Temporal_Difference_Learning#TDLeaf "Temporal Difference Learning") <a id="cite-note-8" href="#cite-ref-8">[8]</a> . Its feature representation includes a map of [static exchange evaluations](Static_Exchange_Evaluation "Static Exchange Evaluation") for all squares and sides <a id="cite-note-9" href="#cite-ref-9">[9]</a> , a structure already proposed by [Russell M. Church](index.php?title=Russell_M._Church&action=edit&redlink=1 "Russell M. Church (page does not exist)") and [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") in *Plans, Goals, and Search Strategies for the Selection of a Move in Chess* <a id="cite-note-10" href="#cite-ref-10">[10]</a> . Probability-based evaluation [scores](Score "Score") are not in [centipawns](Centipawns "Centipawns") nor linear to [material](Material "Material") , and span a +-10,000 range, with [mate scores](Checkmate#MateScore "Checkmate") of +- 30,000. The [search](Search "Search") recently changed from traditional depth-based [iterative deepening](Iterative_Deepening "Iterative Deepening") to assigning number of nodes (or time) to child nodes <a id="cite-note-11" href="#cite-ref-11">[11]</a> . Node budget allocation will also become [neural network](Neural_Networks "Neural Networks") based.

## See also

- [Morph](Morph "Morph")
- [NeuroChess](NeuroChess "NeuroChess")

## Publications

- [Matthew Lai](Matthew_Lai "Matthew Lai") (**2015**). *Giraffe: Using Deep Reinforcement Learning to Play Chess*. M.Sc. thesis, [Imperial College London](https://en.wikipedia.org/wiki/Imperial_College_London), [arXiv:1509.01549v1](http://arxiv.org/abs/1509.01549v1)
- [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal") (**2016**). *[Deep Learning for Go](https://www.research-collection.ethz.ch/handle/20.500.11850/156354)*. B.Sc. thesis, [ETH Zurich](ETH_Zurich "ETH Zurich")

## Forum Posts

## 2015

- [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015
- [SEE Map](http://www.talkchess.com/forum/viewtopic.php?t=57045) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 20, 2015 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Time assignment to children](http://www.talkchess.com/forum/viewtopic.php?t=57092) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 26, 2015
- [Giraffe 20150801](http://talkchess.com/forum/viewtopic.php?t=57142) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 01, 2015
- [Giraffe, new release (Aug 17)](http://www.talkchess.com/forum/viewtopic.php?t=57297) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 17, 2015
- [New Giraffe (Aug 28)](http://www.talkchess.com/forum/viewtopic.php?t=57409) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 28, 2015
- [Giraffe dissertation, and now open source](http://www.talkchess.com/forum/viewtopic.php?t=57557) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 08, 2015
- [New Giraffe (Sept 8)](http://www.talkchess.com/forum/viewtopic.php?t=57558) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 08, 2015

## 2016

- [Death of Giraffe, but hopefully not ML in chess!](http://www.talkchess.com/forum/viewtopic.php?t=59003) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), January 21, 2016
- [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=7) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 04, 2016 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
- [Beginner's guide to graphical profiling](http://www.talkchess.com/forum/viewtopic.php?t=61373) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 10, 2016 » [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
- [New Giraffe](http://www.talkchess.com/forum/viewtopic.php?t=61808) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), October 23, 2016

## 2017...

- [Is AlphaGo approach unsuitable to chess?](http://www.talkchess.com/forum/viewtopic.php?t=64096) by Mel Cooper, [CCC](CCC "CCC"), May 27, 2017 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)"), [Deep Learning](Deep_Learning "Deep Learning")

[Re: Is AlphaGo approach unsuitable to chess?](http://www.talkchess.com/forum/viewtopic.php?t=64096&start=12) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 31, 2017 » [Texel](Texel "Texel")

- [Re: Why is it so hard for comps to play like people?](http://www.hiarcs.net/forums/viewtopic.php?t=8421&start=1) by Ben Redic, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), June 03, 2017
- [Giraffe on Threadripper + newest GPUs](http://www.talkchess.com/forum/viewtopic.php?t=64929) by John Margusen, [CCC](CCC "CCC"), August 19, 2017 <a id="cite-note-13" href="#cite-ref-13">[13]</a>
- [Re: Alphazero news](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69175&start=86) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 07, 2018 » [AlphaZero](AlphaZero "AlphaZero")

## External Links

## Chess Engine

- [GitHub - ianfab/Giraffe: experimental chess engine based on temporal-difference reinforcement learning](https://github.com/ianfab/Giraffe) hosted by [Fabian Fichter](index.php?title=Fabian_Fichter&action=edit&redlink=1 "Fabian Fichter (page does not exist)")
- [waterreaction / Giraffe — Bitbucket](https://web.archive.org/web/20170713091347/https://bitbucket.org/waterreaction/giraffe) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), July 13, 2017)
- [This Chess Engine Learns How to Beat Humans by Playing Against Itself](http://www.popularmechanics.com/technology/robots/a17339/chess-engine-plays-against-itself/) by [Rollin Bishop](https://www.linkedin.com/in/rollinbishop), [Popular Mechanics](https://en.wikipedia.org/wiki/Popular_Mechanics), September 15, 2015
- [Computer Learns to Hack Chess](https://hackaday.com/2015/10/02/computer-learns-to-hack-chess/#more-172231) by [Al Williams](http://hackaday.com/author/wd5gnr1/), [Hackaday](https://en.wikipedia.org/wiki/Hackaday), October 02, 2015 <a id="cite-note-14" href="#cite-ref-14">[14]</a>
- [The Chess Engine that Died So AlphaGo Could Live](https://www.vice.com/en/article/d7ypaz/the-chess-engine-that-died-so-alphago-could-live-giraffe-matthew-lai) by [Rollin Bishop](https://www.linkedin.com/in/rollinbishop), [Motherboard](<https://en.wikipedia.org/wiki/Vice_(magazine)>), March 14, 2016 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)")
- [Giraffe 20150908 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Giraffe%2020150908%2064-bit#Giraffe_20150908_64-bit) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [Giraffe from Wikipedia](https://en.wikipedia.org/wiki/Giraffe)

[Giraffe - Internal systems](https://en.wikipedia.org/wiki/Giraffe#Internal_systems)

- [Manu Dibango](Category:Manu_Dibango "Category:Manu Dibango") - [Electric Africa](http://www.silent-watcher.net/billlaswell/discography/d/electricafrica.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí") - The Burning Giraffe, 1937, [Oil on panel](https://en.wikipedia.org/wiki/Oil_painting), [Kunstmuseum Basel](https://en.wikipedia.org/wiki/Kunstmuseum_Basel), [The Burning Giraffe from Wikipedia](https://en.wikipedia.org/wiki/The_Burning_Giraffe)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Matthew Lai](Matthew_Lai "Matthew Lai") (**2015**). *Giraffe: Using Deep Reinforcement Learning to Play Chess*. M.Sc. thesis, [Imperial College London](https://en.wikipedia.org/wiki/Imperial_College_London), [arXiv:1509.01549v1](http://arxiv.org/abs/1509.01549v1)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [\*First release\* Giraffe, a new engine based on deep learning](http://talkchess.com/forum/viewtopic.php?t=56913) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 08, 2015
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Eigen, a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms](http://eigen.tuxfamily.org/index.php?title=Home)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Fastest Magic Move Bitboard Generator ready to use](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5452) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2006
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Pradyumna Kannan](Pradu_Kannan "Pradu Kannan") (**2007**). *Magic Move-Bitboard Generation in Computer Chess*. [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/magic/Bitboards.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Death of Giraffe, but hopefully not ML in chess!](http://www.talkchess.com/forum/viewtopic.php?t=59003) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), January 21, 2016
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [Lex Weaver](Lex_Weaver "Lex Weaver") (**1998**). *TDLeaf(lambda): Combining Temporal Difference Learning with Game-Tree Search*. [Australian Journal of Intelligent Information Processing Systems](https://www.chatbots.org/journal/australian_journal_of_intelligent_information_processing_systems/), Vol. 5 No. 1, [arXiv:cs/9901001](http://arxiv.org/abs/cs/9901001)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [SEE Map](http://www.talkchess.com/forum/viewtopic.php?t=57045) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 20, 2015
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Russell M. Church](index.php?title=Russell_M._Church&action=edit&redlink=1 "Russell M. Church (page does not exist)"), [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1977**). *Plans, Goals, and Search Strategies for the Selection of a Move in Chess*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Time assignment to children](http://www.talkchess.com/forum/viewtopic.php?t=57092) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 26, 2015
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Rectifier (neural networks) from Wikipedia](<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Ryzen from Wikipedia](https://en.wikipedia.org/wiki/Ryzen) (Threadripper)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Chess hackery](http://www.talkchess.com/forum/viewtopic.php?t=57817) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), October 02, 2015

**[Up one Level](Engines "Engines")**

