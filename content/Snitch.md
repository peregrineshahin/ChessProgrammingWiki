---
title: Snitch
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Snitch**


**Snitch**,  

a [WinBoard](WinBoard "WinBoard") and [UCI](UCI "UCI") compliant chess engine by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), written in [C++](Cpp "Cpp"), 
first announced <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
and released <a id="cite-note-2" href="#cite-ref-2">[2]</a> in 2004. 
While Klaus' former engine [Hagrid](Hagrid "Hagrid") applies [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards"), Snitch uses a plain [8x8 board](8x8_Board "8x8 Board") with [piece-lists](Piece-Lists "Piece-Lists") and [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
as well as [legal move generation](Move_Generation "Move Generation"). 



### Contents


* [1 Features](#features)
	+ [1.1 Search](#search)
	+ [1.2 Evaluation](#evaluation)
	+ [1.3 Misc](#misc)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc-2)
* [5 References](#references)






<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Fail-High Reductions](Fail-High_Reductions "Fail-High Reductions")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") (R=2,3)
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")
	+ [Eval based Pruning](Pruning "Pruning")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Square Control](Square_Control "Square Control")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [King Safety](King_Safety "King Safety")
* [Outposts](Outposts "Outposts")
* [Bad Bishop](Bad_Bishop "Bad Bishop") <a id="cite-note-5" href="#cite-ref-5">[5]</a>


### Misc


* [Book Learning](Book_Learning "Book Learning")
* [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")


## See also


* [Hagrid](Hagrid "Hagrid")


## Forum Posts


* [New engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45881&p=174271) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2004
* [New engine Snitch 1.0.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=74&p=157) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2004
* [Snitch 1.0.4 available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=189&p=554) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 07, 2004
* [Snitch 1.0.8 released](https://www.stmintz.com/ccc/index.php?id=396328) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [CCC](CCC "CCC"), November 16, 2004
* [Snitch new version](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=624&p=2332) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 17, 2004
* [Snitch 1.6.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=4753&p=24570) by Sergio Martinez, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 06, 2006


## External Links


### Chess Engine


* [Snitch and Hagrid two free UCI / Winboard chess engines](http://www.friedelprivat.de/)
* [Snitch 1.6.2 32-bit in CCRL 40/15](http://computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Snitch%201.6.2%2032-bit#Snitch_1_6_2_32-bit)


### Misc


* [Snitch from Wikipedia](https://en.wikipedia.org/wiki/Snitch)
* [snitch - Wiktionary](https://en.wiktionary.org/wiki/snitch)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [New engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45881&p=174271) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2004
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New engine Snitch 1.0.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=74&p=157) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2004
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171&start=21) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2004
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Snitch and Hagrid two free UCI / Winboard chess engines](http://www.friedelprivat.de/) - Developer
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Evaluating bad bishops](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4815&start=2) by [Klaus Friedel](index.php?title=Klaus_Friedel&action=edit&redlink=1 "Klaus Friedel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 15, 2006

**[Up one level](Engines "Engines")**







 
