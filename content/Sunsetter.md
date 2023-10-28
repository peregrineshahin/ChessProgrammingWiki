---
title: Sunsetter
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sunsetter**



[ [François Boucher](Category:Fran%C3%A7ois_Boucher "Category:François Boucher") - The Setting of the Sun <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Sunsetter**,  

an [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License v2.0](Free_Software_Foundation#GPL "Free Software Foundation")
<a id="cite-note-2" href="#cite-ref-2">[2]</a> 
that plays [Bughouse](index.php?title=Bughouse&action=edit&redlink=1 "Bughouse (page does not exist)") and [Crazyhouse](Crazyhouse "Crazyhouse") - a separate version also orthodox chess. 
Sunsetter is written by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann") in [C++](Cpp "Cpp"), recent versions co-authored by [Ben Dean-Kawamura](index.php?title=Ben_Dean-Kawamura&action=edit&redlink=1 "Ben Dean-Kawamura (page does not exist)")
<a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
available at [GitHub](https://en.wikipedia.org/wiki/GitHub), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
<a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### Contents


* [1 Description](#description)
	+ [1.1 Move Generation](#move-generation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
* [2 Forum Posts](#forum-posts)
	+ [2.1 2000 ...](#2000-...)
	+ [2.2 2010 ...](#2010-...)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc)
* [4 References](#references)






<a id="cite-note-5" href="#cite-ref-5">[5]</a>



### [Move Generation](Move_Generation "Move Generation")


Sunsetter is a [bitboard](Bitboards "Bitboards") engine which uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to calculate [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. The [board structure](Board_Representation "Board Representation") further keeps an [8x8 board](8x8_Board "8x8 Board"), and Crazyhouse specific, a bitboard of promoted pawns, and [piece-lists](Piece-Lists "Piece-Lists") of each player's reserve (in hand), also keeping some [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"). [Pseudo-legal moves](Pseudo-Legal_Move "Pseudo-Legal Move") are generated in four [stages](Move_Generation#Staged "Move Generation").



### [Search](Search "Search")


Sunsetter performs [NegaScout](NegaScout "NegaScout") with [transposition table](Transposition_Table "Transposition Table") within its [iterative deepening](Iterative_Deepening "Iterative Deepening") framework using a [zero](Null_Window "Null Window") [aspiration window](Aspiration_Windows "Aspiration Windows") to decide whether the forced re-search of the first move half-opens the [window](Window "Window") in plus or minus infinity direction <a id="cite-note-7" href="#cite-ref-7">[7]</a>. [Null move pruning](Null_Move_Pruning "Null Move Pruning"), [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), [razoring](Razoring "Razoring") and [fractional extensions](Extensions#FractionalExtensions "Extensions") are used to shape the [tree](Search_Tree "Search Tree"), which has considerable larger [branching factor](Branching_Factor "Branching Factor") in Crazyhouse. Sunsetter features [book learning](Book_Learning "Book Learning") based on the final result, where [root moves receive a bonus](Ronald_de_Man#ScoringRootMoves "Ronald de Man") if persistent from advantageous positions in previously won games.



### [Evaluation](Evaluation "Evaluation")


Sunsetter's evaluation in [centipawn](Centipawns "Centipawns") resolution considers [material](Material "Material"), material in hand, [board control](Square_Control "Square Control"), [development](Development "Development"), and [king safety](King_Safety "King Safety") <a id="cite-note-8" href="#cite-ref-8">[8]</a>.



## Forum Posts


### 2000 ...


* [Sunsetter(C) source released](https://www.stmintz.com/ccc/index.php?id=173342) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), June 04, 2001
* [Very interesting crazyhouse position-to Georg Zimmerman (sunsetter test)](https://www.stmintz.com/ccc/index.php?id=264297) by Lieven Clarisse, [CCC](CCC "CCC"), November 11, 2002
* [Sunsetter C10 Anomaly](https://www.stmintz.com/ccc/index.php?id=333517) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), December 04, 2003


### 2010 ...


* [Reborn of sunsetter?](http://www.open-aurec.com/wbforum/viewtopic.php?f=15&t=52922) by velocidrom, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 31, 2013
* [Sunsetter (crazyhouse engine) issue with ponder on, linux](http://talkchess.com/forum/viewtopic.php?t=50395) by Robert Tournevisse, [CCC](CCC "CCC"), December 09, 2013
* [Sunsetter 9 under Arena GUI](http://talkchess.com/forum/viewtopic.php?t=64006) by Arnaud lohéac, [CCC](CCC "CCC"), May 17, 2017


## External Links


### Chess Engine


* [GitHub - georgvonzimmermann/Sunsetter: A crazyhouse chess playing program](https://github.com/georgvonzimmermann/Sunsetter)
* [Sunsetter](http://sunsetter.sourceforge.net/) from [SourceForge](https://en.wikipedia.org/wiki/SourceForge)
* [Sunsetter - at SourceForge.net](https://sourceforge.net/projects/sunsetter/files/)
* [Sunsetter](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/SUNSETTER/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Sunsetter 10.3 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Sunsetter%2010.3%2064-bit#Sunsetter_10_3_64-bit) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Sunset from Wikipedia](https://en.wikipedia.org/wiki/Sunset)
* [Sunset (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Sunset_(disambiguation))
* [Coldplay](Category:Coldplay "Category:Coldplay") - [Sunset Performance](https://en.wikipedia.org/wiki/Everyday_Life_(Coldplay_album)#Track_listing), [Everyday Life](https://en.wikipedia.org/wiki/Everyday_Life_(Coldplay_album)), [Live in Amman](https://en.wikipedia.org/wiki/Amman), [Jordan](https://en.wikipedia.org/wiki/Jordan), November 22, 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [François Boucher](Category:Fran%C3%A7ois_Boucher "Category:François Boucher") - [The Setting of the Sun](https://commons.wikimedia.org/wiki/File:Fran%C3%A7ois_Boucher_028.jpg), 1752, [Wallace Collection](https://en.wikipedia.org/wiki/Wallace_Collection), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Sunsetter/COPYING at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/COPYING)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Sunsetter/README.txt at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/README.txt)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Sunsetter/interface.cpp at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/interface.cpp)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> based on [GitHub - georgvonzimmermann/Sunsetter: A crazyhouse chess playing program](https://github.com/georgvonzimmermann/Sunsetter)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Sunsetter/bitboard.cpp at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/bitboard.cpp)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Sunsetter/search.cpp at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/search.cpp)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Sunsetter/evaluate.cpp at master · georgvonzimmermann/Sunsetter · GitHub](https://github.com/georgvonzimmermann/Sunsetter/blob/master/evaluate.cpp)

**[Up one level](Engines "Engines")**







 
