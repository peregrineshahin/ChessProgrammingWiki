---
title: Isa
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Isa**



[ [Isa Genzken](Category:Isa_Genzken "Category:Isa Genzken") - Window <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Isa**, (ISA) <a id="cite-note-2" href="#cite-ref-2">[2]</a>  

a chess engine by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), written in [C](C "C"), and compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). ISA's development started in 2014 using the [FirstChess](FirstChess "FirstChess") source by [Pham Hong Nguyen](Pham_Hong_Nguyen "Pham Hong Nguyen"), and gradually evolved to an own engine with multiple [search](Search "Search") enhancements as well as [evaluation](Evaluation "Evaluation") features implemented over the time, also documented by its author's postings in [CCC](CCC "CCC"). Isa was first public released in October 2016 as version 1.9.8 <a id="cite-note-3" href="#cite-ref-3">[3]</a> with steady improvements and fixes in subsequent versions.
Since November 2018, Isa 2.0.64 is available as [Open Source](Category:Open_Source "Category:Open Source") under [GitHub](https://en.wikipedia.org/wiki/GitHub) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Mailbox](Mailbox "Mailbox")
* [8x8 Board](8x8_Board "8x8 Board")
* [Piece-Lists](Piece-Lists "Piece-Lists") (2.0.64)


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")


### [Evaluation](Evaluation "Evaluation")


* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Tapered Evaluation](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Mobility](Mobility "Mobility")
* [Tempo](Tempo "Tempo")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table") (2.0.61)
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Rule of the Square](Rule_of_the_Square "Rule of the Square")
	+ [Candidate](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Rook (and Queen) on Seventh](Rook_on_Seventh "Rook on Seventh")
* [King Safety](King_Safety "King Safety")
* [King Queen Tropism](King_Safety#KingTropism "King Safety")
* [Endgame](Endgame "Endgame")
	+ [KBNK](KBNK_Endgame "KBNK Endgame")
	+ KBBK


## See also


* [FirstChess](FirstChess "FirstChess")
* [Yoda](Yoda "Yoda")


## Forum Posts


### 2014


* [Tuning eval](http://www.talkchess.com/forum/viewtopic.php?t=53526) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), September 01, 2014 » [Automated Tuning](Automated_Tuning "Automated Tuning")


### 2015


* [bad eval for passers ?](http://www.talkchess.com/forum/viewtopic.php?t=55433) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), February 23, 2015
* [about king attack](http://www.talkchess.com/forum/viewtopic.php?t=57403) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 27, 2015 » [King Safety](King_Safety "King Safety")
* [high values of pst](http://www.talkchess.com/forum/viewtopic.php?t=57575) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), September 09, 2015 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [A funny bug :-)](http://www.talkchess.com/forum/viewtopic.php?t=57998) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), October 19, 2015
* [Some test résults](http://www.talkchess.com/forum/viewtopic.php?t=58486) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), December 05, 2015


### 2016


* [Somethings wrong but where (lol)](http://www.talkchess.com/forum/viewtopic.php?t=58985) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), January 20, 2016
* [about hashtable](http://www.talkchess.com/forum/viewtopic.php?t=59426) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), March 04, 2016
* [hash eval, hash pawn or twice ?](http://www.talkchess.com/forum/viewtopic.php?t=59566) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), March 19, 2016 » [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table"), [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Evaluate the pieces mobility](http://www.talkchess.com/forum/viewtopic.php?t=59959) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), April 25, 2016 » [Mobility](Mobility "Mobility")
* [Futility prunning](http://www.talkchess.com/forum/viewtopic.php?t=61093) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 11, 2016 » [Futility Pruning](Futility_Pruning "Futility Pruning"), [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* [Isa version 1.9.8 release](http://www.talkchess.com/forum/viewtopic.php?t=61891) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), October 30, 2016


 [Re: Isa version 1.9.8 release](http://www.talkchess.com/forum/viewtopic.php?t=61891&start=3) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), December 10, 2016
* [Endgame bug in Isa](http://www.talkchess.com/forum/viewtopic.php?t=62494) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), December 15, 2016


### 2017 ...


* [Isa 1.9.63 release](http://www.talkchess.com/forum/viewtopic.php?t=63255) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), February 23, 2017
* [Isa 1.9.68 release](http://www.talkchess.com/forum/viewtopic.php?t=63606) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), April 01, 2017
* [Isa 2.0.45 release](http://www.talkchess.com/forum/viewtopic.php?t=64078) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), May 25, 2017
* [Isa 2.0.61 release](http://www.talkchess.com/forum/viewtopic.php?t=66040) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), December 17, 2017
* [Isa 2\_0\_64 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66989) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), April 01, 2018
* [Isa 2.0.92.9 for Windows download link?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69547) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 09, 2019


## External Links


* [GitHub - Dany1962/Isa: a winboard chess engine in C](https://github.com/Dany1962/Isa)
* [Isa](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Isa&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")


### Misc


* [Isa from Wikipedia](https://en.wikipedia.org/wiki/Isa)
* [Isa (name) from Wikipedia](https://en.wikipedia.org/wiki/Isa_(name))
* [Isa (Vorname) from Wikipedia.de](https://de.wikipedia.org/wiki/Isa_(Vorname)) (Given Name)
* [ISA - Wiktionary](https://en.wiktionary.org/wiki/ISA)
* [Industry Standard Architecture from Wikipedia](https://en.wikipedia.org/wiki/Industry_Standard_Architecture)
* [Intelligent speed adaptation from Wikipedia](https://en.wikipedia.org/wiki/Intelligent_speed_adaptation)
* [International Society of Automation from Wikipedia](https://en.wikipedia.org/wiki/International_Society_of_Automation)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Isa Genzken](Category:Isa_Genzken "Category:Isa Genzken") - Window (Fenster, 1993), [Middelheim Open Air Sculpture Museum](https://en.wikipedia.org/wiki/Middelheim_Open_Air_Sculpture_Museum), Photo by Funkyxian, August 9, 2016, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Isa version 1.9.8 release](http://www.talkchess.com/forum/viewtopic.php?t=61891&start=4) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), December 10, 2016
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Isa version 1.9.8 release](http://www.talkchess.com/forum/viewtopic.php?t=61891) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), October 30, 2016
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [GitHub - Dany1962/Isa: a winboard chess engine in C](https://github.com/Dany1962/Isa)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> Features based on isa\_2\_0\_64.zip\isa 2\_0\_64\ read me.odt

**[Up one level](Engines "Engines")**







 
