---
title: ScorpioScorpioNNUE
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Scorpio**



[ Scorpio <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Scorpio**,  

a sophisticated [open source chess engine](Category:Open_Source "Category:Open Source") by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), written in [C++](Cpp "Cpp") and compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") with builds running under [Windows](Windows "Windows") and [Linux](Linux "Linux"). Scorpio participated at the [CCT9](CCT9 "CCT9"), [CCT11](CCT11 "CCT11") and [CCT12](CCT12 "CCT12") [online tournaments](Tournaments_and_Matches#online "Tournaments and Matches"), and played the [ICT 2007](ICT_2007 "ICT 2007") over the board. It is base of Daniel's [general game playing](General_Game_Playing "General Game Playing") engine [Nebiyu](Nebiyu "Nebiyu"), able to play [Chess variants](Chess#Variants "Chess"), [Checkers](Checkers "Checkers"), [Reversi](Othello "Othello"), [Go](Go "Go") and [Amazons](Amazons "Amazons") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Description](#description)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Distributed Search](#distributed-search)
	+ [1.3 MCTS](#mcts)
	+ [1.4 Evaluation](#evaluation)
	+ [1.5 Bitbases](#bitbases)
	+ [1.6 ScorpioNN](#scorpionn)
	+ [1.7 ScorpioNNUE](#scorpionnue)
* [2 See also](#see-also)
* [3 Dedicated Namesake](#dedicated-namesake)
* [4 Forum Posts](#forum-posts)
	+ [4.1 2005 ...](#2005-...)
	+ [4.2 2010 ...](#2010-...)
	+ [4.3 2015 ...](#2015-...)
	+ [4.4 2020 ...](#2020-...)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






### Board Representation


Scorpio combines [Bitboards](Bitboards "Bitboards") with a [0x88](0x88 "0x88") board representation, and the coordinate transformation in [scanning bits](BitScan "BitScan") along with the lookup of the [De Bruijn multiplication](BitScan#DeBruijnMultiplation "BitScan"). The "unique" 64-bit routine was generated with the help of the [De Bruijn Sequence Generator](De_Bruijn_Sequence_Generator "De Bruijn Sequence Generator") passing Daniel's birth date <a id="cite-note-3" href="#cite-ref-3">[3]</a> . [Magic bitboard](Magic_Bitboards "Magic Bitboards") implementation by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Thanks for the acknowledgment of both!



### Distributed Search


Scorpio performs a [distributed search](Parallel_Search "Parallel Search") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> around an [iterative](Iterative_Search "Iterative Search") [depth-first search](Depth-First "Depth-First") framework <a id="cite-note-7" href="#cite-ref-7">[7]</a> :




```C++
Scorpio uses a decentralized approach ([p2p](https://en.wikipedia.org/wiki/Peer-to-peer)) where neither [memory](Memory "Memory") nor jobs are centralized. Each host could have multiple processors in which case [shared memory search](Parallel_Search "Parallel Search") (centralized search with [threads](Thread "Thread")) will be used. One processor per node will be started by [mpirun](https://en.wikipedia.org/wiki/Message_Passing_Interface), then each [process](Process "Process") at each node will create enough threads to engage all its processors. 

```

### MCTS


Scorpio **2.7.9**, released in December 2017, optionally features a [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") (MCTS) <a id="cite-note-8" href="#cite-ref-8">[8]</a>. Scorpio **2.8** in February 2018, MCTS with [alpha-beta](Alpha-Beta "Alpha-Beta") [rollouts](Bojun_Huang#Rollout "Bojun Huang") as suggested [Bojun Huang](Bojun_Huang "Bojun Huang") <a id="cite-note-9" href="#cite-ref-9">[9]</a>. The parallel search for MCTS uses virtual loss to distribute work among [threads](Thread "Thread") in standard MCTS rollouts, and [ABDADA](ABDADA "ABDADA") like BUSY flag for alpha-beta rollouts. ABDADA and parallel MCTS from the [Go](Go "Go") world are very similar in nature <a id="cite-note-10" href="#cite-ref-10">[10]</a>.



### Evaluation


Scorpio's [evaluation](Evaluation "Evaluation") includes following features and techniques <a id="cite-note-11" href="#cite-ref-11">[11]</a> :



* [NNUE](NNUE "NNUE") (3.0.9)
* [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [King Safety](King_Safety "King Safety")
* [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Material](Material "Material")
* [Mobility](Mobility "Mobility") of [bishops](Bishop "Bishop") and [knights](Knight "Knight")
* [Outposts](Outposts "Outposts")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Rook on Open File](Rook_on_Open_File "Rook on Open File")
* [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")


### Bitbases


*see main article [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")*


Scorpio has its own [endgame bitbase](Endgame_Bitbases "Endgame Bitbases") format, which might be probed by other programs via a [shared library](https://en.wikipedia.org/wiki/Library_%28computing%29#Shared_libraries) **egbbdll**.



### ScorpioNN


The [neural network](Neural_Networks "Neural Networks") version of Scorpio **2.9.0** (2019) works using [egbbdll](Scorpio#Bitbases "Scorpio") shared library <a id="cite-note-12" href="#cite-ref-12">[12]</a> that provides neural network inference via [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) and/or *TensorRT* <a id="cite-note-13" href="#cite-ref-13">[13]</a> backends <a id="cite-note-14" href="#cite-ref-14">[14]</a>.



### ScorpioNNUE


With the the advent of [NNUE](NNUE "NNUE") and its huge success in [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), [CFish NNUE](CFish#NNUE "CFish") and other engines, [Daniel Shawul](Daniel_Shawul "Daniel Shawul") added NNUE support à la CFish into his [egbbdll](Scorpio#Bitbases "Scorpio") probing library <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a>, and reported more than 400 Elo out of his implementation with a shared library with Scorpio **3.0.9** <a id="cite-note-17" href="#cite-ref-17">[17]</a>.



## See also


* [BBC NNUE](BBC#NNUE "BBC")
* [DanChess](DanChess "DanChess")
* [Nebiyu](Nebiyu "Nebiyu")


## Dedicated Namesake


* [Novag Scorpio 68000](http://www.schach-computer.info/wiki/index.php/Novag_Scorpio_68000) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) » [Novag](Novag "Novag"), [David Kittinger](David_Kittinger "David Kittinger")


## Forum Posts


### 2005 ...


* [Scorpio chess engine by Daniel Shawul](https://www.stmintz.com/ccc/index.php?id=421572) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 18, 2005
* [Scorpio chess engine by Daniel Shawul](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2310&start=0) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 19, 2005
* [Gauntlet Scorpio v1.0 - games - new entry!](https://www.stmintz.com/ccc/index.php?id=421991) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), April 21, 2005
* [Gauntlet Scorpio v1.1 - games - replaced DanChess](https://www.stmintz.com/ccc/index.php?id=429465) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), June 02, 2005
* [Scorpio 1.3 looks promising](https://www.stmintz.com/ccc/index.php?id=434254) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 29, 2005
* [Scorpio 1.5 is very strong!](https://www.stmintz.com/ccc/index.php?id=444303) by Ómar Skúlason, [CCC](CCC "CCC"), August 22, 2005
* [Has anyone tried the Scorpio engine?](https://www.stmintz.com/ccc/index.php?id=453892) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC](CCC "CCC"), October 05, 2005
* [Standardgauntlet - Scorpio is fighting for a place in the sun !](https://www.stmintz.com/ccc/index.php?id=489658) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), February 26, 2006
* [Special Scorpio 1.91 build for Core2Duo/Quad/Xeon](http://www.talkchess.com/forum/viewtopic.php?t=15267) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), July 21, 2007
* [Scorpio 2.0 Windows x64 build available](http://www.talkchess.com/forum/viewtopic.php?t=18497) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 22, 2007
* [Scorpio 64 bit questions](http://www.talkchess.com/forum/viewtopic.php?t=18506) by [Denis P. Mendoza](Denis_Mendoza "Denis Mendoza"), [CCC](CCC "CCC"), December 23, 2007
* [Interesting Scorpio design](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49618) by [Kerwin Medina](Kerwin_Medina "Kerwin Medina"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2008 » [Iterative Search](Iterative_Search "Iterative Search")
* [Scorpio 202 Under Linux Resolved](http://www.talkchess.com/forum/viewtopic.php?t=24146) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), October 03, 2008


### 2010 ...


* [asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 6, 2010
* [Scorpio 2.6 JA available](http://www.talkchess.com/forum/viewtopic.php?t=35150) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), June 25, 2010
* [Scorpio 2.7 Linux](http://www.talkchess.com/forum/viewtopic.php?t=41296) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 02, 2011
* [Scorpio Chess 2.7 by Jim Ablett is out](http://www.talkchess.com/forum/viewtopic.php?t=42142) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 24, 2012


### 2015 ...


* [scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 22, 2015
* [Scorpio 2.7.7](http://www.talkchess.com/forum/viewtopic.php?t=59582) by Krzysztof Grzelak, [CCC](CCC "CCC"), March 21, 2016
* [Happy halloween - scorpio 2.7.8](http://www.talkchess.com/forum/viewtopic.php?t=65599) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 31, 2017
* [Scorpio 2.7.9](http://www.talkchess.com/forum/viewtopic.php?t=66032) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 16, 2017


**2018**



* [Alpha-Beta as a rollouts algorithm](http://www.talkchess.com/forum/viewtopic.php?t=66414) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 25, 2018 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [MCαβ](MC%CE%B1%CE%B2 "MCαβ"), [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Scorpio 2.8](http://www.talkchess.com/forum/viewtopic.php?t=66552) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 10, 2018
* [comparing minimax and averaging MCTS with alphabeta rollouts](http://www.talkchess.com/forum/viewtopic.php?t=66886) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 20, 2018 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Instruction for running Scorpio with neural network on linux](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68119) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 01, 2018 » [Neural Networks](Neural_Networks "Neural Networks")
* [Multithreaded batching on GPU for montecarlo and also alpha-beta](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68362) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), September 03, 2018
* [Scorpio 2.8.7 MCTS+NN windows version](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68393) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), September 08, 2018
* [Scorpio 2.8.9 with TensorRT support](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68595) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 07, 2018


**2019**



* [How to get ScorpioNN to work?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71295) by [Torsten Schoop](index.php?title=Torsten_Schoop&action=edit&redlink=1 "Torsten Schoop (page does not exist)"), [CCC](CCC "CCC"), July 16, 2019
* [Scorpio 3.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71575) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 16, 2019
* [Scorpio 3.0.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72018) by [Werner Schüle](index.php?title=Werner_Sch%C3%BCle&action=edit&redlink=1 "Werner Schüle (page does not exist)"), [CCC](CCC "CCC"), October 06, 2019


### 2020 ...


* [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 15, 2020
* [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 17, 2020
* [NNUE scoring (egbb lib)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77348) by [Desperado](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), May 19, 2021 » [NNUE](NNUE "NNUE"),[Scorpio NNUE](#scorpionnue)
* [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")


 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=63) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 18, 2021
* [Re: NNUE Question - King Placements](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=40) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), July 01, 2021 » [ScorpioNNUE](#scorpionnue)


## External Links


### Chess Engine


* [Scorpio Chess and Nebiyu Alien](http://sites.google.com/site/dshawul/home)
* [dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio)
* [GitHub - dshawul/egbbdll: Probing code for scorpio bitbases](https://github.com/dshawul/egbbdll)
* [GitHub - dshawul/nn-probe: Library for probing neural networks](https://github.com/dshawul/nn-probe)
* [GitHub - dshawul/nnue-probe: for probing NNUE](https://github.com/dshawul/nnue-probe)
* [Engine: Scorpio](http://wbec-ridderkerk.nl/html/details1/Scorpio.html) from [WBEC Ridderkerk](WBEC "WBEC")
* [The chess games of Scorpio](http://www.chessgames.com/perl/chessplayer?pid=111050) from [chessgames.com](http://www.chessgames.com/index.html)


### Misc


* [Scorpio (astrology) from Wikipedia](https://en.wikipedia.org/wiki/Scorpio_%28astrology%29)
* [Scorpius from Wikipedia](https://en.wikipedia.org/wiki/Scorpius)
* [Scorpion from Wikipedia](https://en.wikipedia.org/wiki/Scorpion)
* [Scorpion (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Scorpion_%28disambiguation%29)
* [Arthur Jones](https://en.wikipedia.org/wiki/Arthur_Jones_(musician)) - Scorpio (1969), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat. [Beb Guérin](https://en.wikipedia.org/wiki/Beb_Gu%C3%A9rin) and [Claude Delcloo](https://de.wikipedia.org/wiki/Claude_Delcloo)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Scorpio symbol, [Book of Hours](https://en.wikipedia.org/wiki/Book_of_hours), the Falstof Master, [Bodleian Library](https://en.wikipedia.org/wiki/Bodleian_Library), [Oxford](https://en.wikipedia.org/wiki/University_of_Oxford), [Scorpio (astrology) from Wikipedia](https://en.wikipedia.org/wiki/Scorpio_%28astrology%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Scorpio Chess and Nebiyu Alien](http://sites.google.com/site/dshawul/home)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Scorpio/scorpio.h at master · dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio/blob/master/scorpio.h)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Scorpio/magics.cpp at master · dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio/blob/master/magics.cpp)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Scorpio/parallel.cpp at master · dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio/blob/master/parallel.cpp)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 6, 2010
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Scorpio/search.cpp at master · dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio/blob/master/search.cpp)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Scorpio 2.7.9](http://www.talkchess.com/forum/viewtopic.php?t=66032) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 16, 2017
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Bojun Huang](Bojun_Huang "Bojun Huang") (**2015**). *[Pruning Game Tree by Rollouts](https://www.semanticscholar.org/paper/Pruning-Game-Tree-by-Rollouts-Huang/a38b358745067f71a9c780db117ae2471e693d63)*. [AAAI](AAAI "AAAI")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Scorpio 2.8](http://www.talkchess.com/forum/viewtopic.php?t=66552) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 10, 2018
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Scorpio/eval.cpp at master · dshawul/Scorpio · GitHub](https://github.com/dshawul/Scorpio/blob/master/eval.cpp)
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [GitHub - dshawul/egbbdll: Probing code for scorpio bitbases](https://github.com/dshawul/egbbdll)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [NVIDIA TensorRT | NVIDIA Developer](https://developer.nvidia.com/tensorrt)
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [GitHub - dshawul/Scorpio: Scorpio chess engine - Neural Networks (NNs)](https://github.com/dshawul/Scorpio#nns)
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 15, 2020
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [GitHub - dshawul/nnue-probe](https://github.com/dshawul/nnue-probe)
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 17, 2020

**[Up one level](Engines "Engines")**







 
