---
title: QuTeChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* QuTeChess**


**QuTeChess**,  

an experimental, [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") written by [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), available from a [SourceForge](https://en.wikipedia.org/wiki/SourceForge) [SVN](https://en.wikipedia.org/wiki/Apache_Subversion) [repository](https://en.wikipedia.org/wiki/Codebase) <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
As its name suggests, QuTeChess is written in [C++](Cpp "Cpp") using the [Qt4.7](https://en.wikipedia.org/wiki/Qt_%28framework%29) cross-platform application framework (using QTime, QThread). 
It reflects the author's dealings with Qt to implement UCI and [CLI](CLI "CLI") along with [threads](Thread "Thread") to start an interruptible [search](Search "Search").



### Contents


* [1 Description](#description)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






QuTeChess is quasi [bitboard](Bitboards "Bitboards") based using [Tinker's](Tinker "Tinker") [approach](Sliding_Piece_Attacks#Tinker.27s_Approach "Sliding Piece Attacks") in [move generation](Move_Generation "Move Generation") of [sliding pieces](Sliding_Pieces "Sliding Pieces"). 
Based on the [serialization](Bitboard_Serialization "Bitboard Serialization") of attacks on the otherwise empty board, it tests for [pseudo legality](Pseudo-Legal_Move "Pseudo-Legal Move") by looking whether squares [between](Square_Attacked_By#InBetween "Square Attacked By") [origin](Origin_Square "Origin Square") and [target](Target_Square "Target Square") are empty.
Its [search](Search "Search") is plain [alpha-beta](Alpha-Beta "Alpha-Beta") without [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") loop. 
The availability of *changegenes.cpp* suggests QuTeChess' 
[piece values](Point_Value "Point Value") and a few random [evaluation](Evaluation "Evaluation") features could be [tuned](Automated_Tuning "Automated Tuning") by an [evolutionary computation](Genetic_Programming#EvolutionaryComputation "Genetic Programming") approach of [differential evolution](https://en.wikipedia.org/wiki/Differential_evolution) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Forum Posts


* [A new UCI engine called QuTeChess](http://www.talkchess.com/forum/viewtopic.php?t=16375) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](CCC "CCC"), September 09, 2007


## External Links


* [QuTeChess | Free Science & Engineering software downloads at SourceForge.net](https://sourceforge.net/projects/qutechess/)
* [QuTeChess 1.0.1t r3](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=QuTeChess%201.0.1t%20r3) in [CCRL 40/4](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [QuTeChess | Free Science & Engineering software downloads at SourceForge.net](https://sourceforge.net/projects/qutechess/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> \* [Borko Bošković](Borko_Bo%C5%A1kovi%C4%87 "Borko Bošković"), [Sašo Greiner](Sa%C5%A1o_Greiner "Sašo Greiner"), [Janez Brest](Janez_Brest "Janez Brest"), [Aleš Zamuda](Ale%C5%A1_Zamuda "Aleš Zamuda"), [Viljem Žumer](Viljem_%C5%BDumer "Viljem Žumer") (**2008**). *[An Adaptive Differential Evolution Algorithm with Opposition-Based Mechanisms, Applied to the Tuning of a Chess Program](https://link.springer.com/chapter/10.1007%2F978-3-540-68830-3_12)*. [Advances in Differential Evolution](https://link.springer.com/book/10.1007/978-3-540-68830-3), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

**[Up one Level](Engines "Engines")**







 
