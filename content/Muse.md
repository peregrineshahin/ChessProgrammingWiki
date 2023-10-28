---
title: Muse
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Muse**



[ The Muses: [Clio](https://en.wikipedia.org/wiki/Clio), [Euterpe](https://en.wikipedia.org/wiki/Euterpe), and [Thalia](https://en.wikipedia.org/wiki/Thalia_%28Muse%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Muse**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant chess engine by [Martin Fierz](Martin_Fierz "Martin Fierz"), first released in August 2004 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Muse is written in [C](C "C"), using [bitboards](Bitboards "Bitboards") and is about 13'000 lines of code. 
It applies most of the usual stuff <a id="cite-note-3" href="#cite-ref-3">[3]</a>, such as [alpha-beta](Alpha-Beta "Alpha-Beta") [scout-style](Scout "Scout") search with [transposition table](Transposition_Table "Transposition Table"), [move ordering](Move_Ordering "Move Ordering") with [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), 
[adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [check](Check_Extensions "Check Extensions") and [recapture extensions](Recapture_Extensions "Recapture Extensions"). 
[Quiescence search](Quiescence_Search "Quiescence Search") is enhanced by [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") to order and [prune](Pruning "Pruning") captures, and further, the [evaluation](Evaluation "Evaluation") utilizes a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"). 
After an abstinence of 12 years from computer chess, Martin released the improved Muse **0.95** in April 2016 <a id="cite-note-4" href="#cite-ref-4">[4]</a>, using [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") [magic move generator](Magic_Bitboards "Magic Bitboards") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### Contents


* [1 Forum Posts](#forum-posts)
* [2 External Links](#external-links)
	+ [2.1 Chess Engine](#chess-engine)
	+ [2.2 Misc](#misc)
* [3 References](#references)






* [Muse!](https://www.stmintz.com/ccc/index.php?id=381373) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), August 08, 2004
* [Muse 0.899](https://www.stmintz.com/ccc/index.php?id=392832) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), October 22, 2004
* [Fafis and Muse may be elite engines](https://www.stmintz.com/ccc/index.php?id=393115) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 24, 2004
* [Muse 0.95](http://www.talkchess.com/forum/viewtopic.php?t=59817) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 10, 2016


## External Links


### Chess Engine


* [Martin's World >> Muse](http://www.fierz.ch/muse.htm)
* [Muse](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Muse&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Muse - Wiktionary](https://en.wiktionary.org/wiki/Muse)
* [muse - Wiktionary](https://en.wiktionary.org/wiki/muse)
* [Muse from Wikipedia](https://en.wikipedia.org/wiki/Muse)
* [Muses in popular culture from Wikipedia](https://en.wikipedia.org/wiki/Muses_in_popular_culture)
* [Muse (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Muse_%28disambiguation%29)
 * [Muse](Category:Muse "Category:Muse") - [Micro Cuts](https://en.wikipedia.org/wiki/Origin_of_Symmetry), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), [July 08, 2002](http://www.montreuxjazzlive.com/muse-images), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video 


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Eustache Le Sueur](Category:Eustache_Le_Sueur "Category:Eustache Le Sueur") - [The Muses: Clio, Euterpe and Thalia](https://en.wikipedia.org/wiki/File:Eustache_Le_Sueur_-_The_Muses_-_Clio,_Euterpe_and_Thalia_-_WGA12611.jpg), [oil](https://en.wikipedia.org/wiki/Oil_painting) on [panel](https://en.wikipedia.org/wiki/Panel_painting), between 1652 and 1655, Current location: [Louvre](https://en.wikipedia.org/wiki/Louvre), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Muse!](https://www.stmintz.com/ccc/index.php?id=381373) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), August 08, 2004
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Martin's World >> Muse](http://www.fierz.ch/muse.htm)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Muse 0.95](http://www.talkchess.com/forum/viewtopic.php?t=59817) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 10, 2016
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Fastest Magic Move Bitboard Generator ready to use](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5452) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2006
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Pradyumna Kannan](Pradu_Kannan "Pradu Kannan") (**2007**). *Magic Move-Bitboard Generation in Computer Chess*. [pdf](http://www.pradu.us/old/Nov27_2008/Buzz/research/magic/Bitboards.pdf)

**[Up one Level](Engines "Engines")**







 
