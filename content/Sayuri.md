---
title: Sayuri
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sayuri**



 [](https://groups.google.com/d/forum/sayuri-uci-chess-engine) Sayuri Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Sayuri**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [MIT License](https://en.wikipedia.org/wiki/MIT_License), written by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi") in [C++11](Cpp "Cpp"), first published in 2013 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Sayuri has an embedded [LISP](index.php?title=LISP&action=edit&redlink=1 "LISP (page does not exist)") interpreter dubbed *Sayulisp*, which can generate and operate the chess engine, and customize [search](Search "Search") algorithms and [evaluation](Evaluation "Evaluation") weights <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc)
* [4 References](#references)






<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### [Board Representation](Board_Representation "Board Representation")


Sayuri is a [bitboard](Bitboards "Bitboards") engine and determines [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") indexed by [square](Squares "Squares") , 8-bit [line occupancy](Occupancy_of_any_Line "Occupancy of any Line") and {0,45,90,135}-rotation - no [outer square optimization](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") for 4-fold denser tables applied.



### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Parallel Search](Parallel_Search "Parallel Search")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
	+ [ProbCut](ProbCut "ProbCut")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Evaluation](Evaluation "Evaluation")


* [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Pinned Pieces](Pin "Pin")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Passed Pawns](Passed_Pawn "Passed Pawn")
	+ [Defended Pawns](Defended_Pawns_(Bitboards) "Defended Pawns (Bitboards)")
	+ [Doubled Pawns](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawns](Isolated_Pawn "Isolated Pawn")
* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
	+ [Rooks on (semi) open files](Rook_on_Open_File "Rook on Open File")
	+ [Bad Bishop](Bad_Bishop "Bad Bishop")
	+ [Too Early Queen Development](Evaluation_of_Pieces#Queen "Evaluation of Pieces")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shield](King_Safety#PawnShield "King Safety")


## Forum Posts


* [Sayuri (UCI Engine) by Ishibashi Hironori](http://www.talkchess.com/forum/viewtopic.php?t=49977) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), November 08, 2013
* [Sayuri 27th February 2015 Edition](http://www.talkchess.com/forum/viewtopic.php?t=55489) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), February 27, 2015
* [Sayuri release two days ago](http://www.talkchess.com/forum/viewtopic.php?t=56794) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 27, 2015
* [Sayuri 2015.12.08 Released!!](http://tinyurl.com/ohhna55) by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi"), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups), December 08, 2015
* [Sayuri](http://www.talkchess.com/forum/viewtopic.php?t=58563) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 11, 2015
* [Sayuri new releases](http://www.talkchess.com/forum/viewtopic.php?t=60140) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 11, 2016
* [Sayuri 2017.09.26 release](http://www.talkchess.com/forum/viewtopic.php?t=65304) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 27, 2017
* [Sayuri 2017.09.29 Released!!](https://groups.google.com/forum/#!topic/sayuri-uci-chess-engine/fViINFFN2Rs) by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi"), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups), September 29, 2017
* [Re: Provide a short description?](https://groups.google.com/d/msg/sayuri-uci-chess-engine/bvLzPjB5hDo/CTQzS4opBAAJ) by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi"), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups), October 04, 2017
* [Sayuri 2018.05.23 Released](https://groups.google.com/forum/#!topic/sayuri-uci-chess-engine/p0ilh7ZPSrs) by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi"), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups), May 23, 2018


## External Links


### Chess Engine


* [MetalPhaeton/sayuri · GitHub](https://github.com/MetalPhaeton/sayuri)
* [Sayuri - UCI Chess Engine](https://groups.google.com/forum/#!forum/sayuri-uci-chess-engine), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups)
* [Sayuri](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Sayuri&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Sayuri - Wiktionary](https://en.wiktionary.org/wiki/Sayuri)
* [Sayuri from Wikipedia](https://en.wikipedia.org/wiki/Sayuri)
* [Memoirs of a Geisha](https://en.wikipedia.org/wiki/Memoirs_of_a_Geisha_%28film%29) - [Sayuri's Theme](https://en.wikipedia.org/wiki/Memoirs_of_a_Geisha_%28film%29#Soundtrack_album), Soundtrack (2005) composed and conducted by [John Williams](https://en.wikipedia.org/wiki/John_Williams), featuring [Yo Yo Ma](https://en.wikipedia.org/wiki/Yo-Yo_Ma) and [Itzhak Perlman](https://en.wikipedia.org/wiki/Itzhak_Perlman), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [sayuri/sayuri\_logo\_small.png at master · MetalPhaeton/sayuri · GitHub](https://github.com/MetalPhaeton/sayuri/blob/master/SayuriLogo/sayuri_logo_small.png)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Sayuri (UCI Engine) by Ishibashi Hironori](http://www.talkchess.com/forum/viewtopic.php?t=49977) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), November 08, 2013
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [sayuri/README.md at master · MetalPhaeton/sayuri · GitHub](https://github.com/MetalPhaeton/sayuri/blob/master/README.md)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> based on Sayuri 2015.12.08, [Sayuri 2015.12.08 Released!!](http://tinyurl.com/ohhna55) by [Hironori Ishibashi](Hironori_Ishibashi "Hironori Ishibashi"), [Google Groups](https://en.wikipedia.org/wiki/Google_Groups), December 08, 2015

**[Up one Level](Engines "Engines")**







 
