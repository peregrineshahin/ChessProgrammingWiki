---
title: Onno
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Onno**



 [](https://www.onnochess.com/) Onno logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Onno**,  

was a commercial chess engine developed by [Onno Garms](Onno_Garms "Onno Garms"), written in [C++](Cpp "Cpp") and released in May 2009. 
After announcing the end of Onno's development in March 2011 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, Onno Garms revealed several ideas that made Onno stronger. 
The 32/64-bit [Windows](Windows "Windows") or 64-bit [Linux](Linux "Linux") executables communicate with a chess [GUI](GUI "GUI") via [UCI](UCI "UCI"). 



### Basics


Onno uses a fixed shift variation of [Magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Its [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") considers [alpha](Alpha "Alpha") and [beta](Beta "Beta") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. [Evaluation](Evaluation "Evaluation") features were [tuned automaticly](Automated_Tuning "Automated Tuning") performing a [Genetic algorithm](Genetic_Programming#GeneticAlgorithm "Genetic Programming") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### Search


Onno applies an [iterative search](Iterative_Search#Onno "Iterative Search") along with [PVS](Principal_Variation_Search "Principal Variation Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [verification search](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"). Onno further uses a technique dubbed **bad pruning** similar to [razoring](Razoring "Razoring"). The idea is to apply a [reduced search](Reductions "Reductions") with a reduced [window](Window "Window") - if the search at depth d-3 says that one loses more then a pawn, it does not search the move with the current depth d <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### Parallel Search


The MP version of Onno searches in [parallel](Parallel_Search "Parallel Search") utilizing [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") by following [Rainer Feldmann's](Rainer_Feldmann "Rainer Feldmann") 1993 Ph.D. thesis *Game Tree Search on Massively Parallel Systems* <a id="cite-note-7" href="#cite-ref-7">[7]</a> using [virtual messaging](https://en.wikipedia.org/wiki/Virtual_synchrony).



### Node Types


Onno determines expected [Node Types](Node_Types "Node Types") to perform [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") not only at [PV-nodes](Node_Types#PV "Node Types") but also at expected [Cut-nodes](Node_Types#CUT "Node Types"). Onno Garms gave following rules <a id="cite-note-8" href="#cite-ref-8">[8]</a>



* The [root node](Root "Root") is a PV-node.
* The first child of a PV-node is a PV-node
* The further children are searched by a [scout search](Scout "Scout") as CUT-nodes
* [PVS](Principal_Variation_Search "Principal Variation Search") re-search is done as PV-node
* The first node of bad pruning is a CUT-node
* The node after a [null move](Null_Move "Null Move") is a CUT-node
* The first node of [null move verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") is a CUT-node
* [Internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") does not change the node type
* The first child of a CUT-node is an [ALL-node](Node_Types#ALL "Node Types")
* Further children of a CUT-node are CUT-nodes
* Children of ALL-nodes are CUT-nodes


## See also


* [Iterative Search in Onno](Iterative_Search#Onno "Iterative Search")


## Forum Posts


### 2009


* [Magic with fixed shift](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50043) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2009
* [Onno 0.12](http://www.talkchess.com/forum/viewtopic.php?t=27316) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), April 04, 2009
* [New commercial engine soon: Onno](http://www.talkchess.com/forum/viewtopic.php?t=27952) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), May 17, 2009
* [Onno 1.0 is now available](http://www.talkchess.com/forum/viewtopic.php?t=28170) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), May 30, 2009
* [About becoming Commercial. The Onno Case](http://www.talkchess.com/forum/viewtopic.php?t=28221) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), June 02, 2009
* [Onno 1-1-1 released](http://www.talkchess.com/forum/viewtopic.php?t=29598) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), August 30, 2009


### 2010


* [Onno MP beta has been released to customers](http://www.talkchess.com/forum/viewtopic.php?t=32945) by [Martin Thoresen](Martin_Thoresen "Martin Thoresen"), [CCC](CCC "CCC"), February 27, 2010
* [Re: DTS Structure](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=351576&t=34561) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), May 28, 2010  » [Iterative Search in Onno](Iterative_Search#Onno "Iterative Search")


### 2011 ...


* [Development of Onno ends](http://www.talkchess.com/forum/viewtopic.php?t=38403) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011
* [Root node search](http://www.talkchess.com/forum/viewtopic.php?t=38404) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Root](Root "Root")
* [Software Engineering](http://www.talkchess.com/forum/viewtopic.php?t=38406) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [History Heuristic](History_Heuristic "History Heuristic"), [Toga](Toga "Toga")
* [Bad Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38407) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Pruning](Pruning "Pruning")
* [On internal iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=38408) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Node Types](Node_Types "Node Types")
* [Less null move pruning by trans map](http://www.talkchess.com/forum/viewtopic.php?t=38409) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Playing better moves in drawish positions (anti-0.00)](http://www.talkchess.com/forum/viewtopic.php?t=38410) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Draw](Draw "Draw"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [On parallelization](http://www.talkchess.com/forum/viewtopic.php?t=38411) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Parallel Search](Parallel_Search "Parallel Search")
* [Parameter tuning](http://www.talkchess.com/forum/viewtopic.php?t=38412) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Memory-PV-Search](http://www.talkchess.com/forum/viewtopic.php?t=38413) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Move ordering by PST](http://www.talkchess.com/forum/viewtopic.php?t=38766) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), April 16, 2011 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [History Heuristic](History_Heuristic "History Heuristic"), [Move Ordering](Move_Ordering "Move Ordering")
* [SEE with alpha beta](http://www.talkchess.com/forum/viewtopic.php?t=40054) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), August 14, 2011 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation"), [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")


## External Links


### Chess Engine


* [Onno Chess Software](https://www.onnochess.com/)
* [Interview mit Onno Garms](https://www.schach-welt.de/schach/computerschach/interviews/onno-garms) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Schachwelt](https://www.schach-welt.de/), December 25, 2009 (German)


### Misc


* [Onno from Wikipedia](https://en.wikipedia.org/wiki/Onno)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Onno Chess Software](https://www.onnochess.com/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Development of Onno ends](http://www.talkchess.com/forum/viewtopic.php?t=38403) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Magic with fixed shift](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50043) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [SEE with alpha beta](http://www.talkchess.com/forum/viewtopic.php?t=40054) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), August 14, 2011
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Parameter tuning](http://www.talkchess.com/forum/viewtopic.php?t=38412) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Bad Pruning](http://www.talkchess.com/forum/viewtopic.php?t=38407) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. thesis
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: On internal iterative deeping](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=399511&t=38408) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 17, 2011

**[Up one level](Engines "Engines")**







 
