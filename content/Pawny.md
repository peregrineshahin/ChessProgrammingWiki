---
title: Pawny
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Pawny**



 [](File:PawnyLogo.jpg) Pawny [[1]](#cite-note-pawny-1) 
**Pawny**,  

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), written in [C](C "C") and licensed under the [GPL](Free_Software_Foundation#GPL "Free Software Foundation"), first released in September 2009.
Pawny's board was initially [represented](Board_Representation "Board Representation") as 
[16x16](Vector_Attacks#16x12 "Vector Attacks") [array](Array "Array"), filled with [piece codes](Pieces#PieceCoding "Pieces"), complemented with [piece lists](Piece-Lists "Piece-Lists") as array of [linked lists](Linked_List "Linked List") [[1]](#cite-note-pawny-1). 
**Pawny 1.0**, released in May 2013, is an entirely rewritten engine based on [bitboards](Bitboards "Bitboards") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 Forum Posts](#forum-posts)
	+ [2.1 2009](#2009)
	+ [2.2 2010 ...](#2010-...)
	+ [2.3 2015 ...](#2015-...)
* [3 External Links](#external-links)
* [4 References](#references)






### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Fractional Extensions](Extensions#FractionalExtensions "Extensions")
	+ [Razoring](Razoring "Razoring")
	+ [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning") based on [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Rook on (Semi) Open File](Rook_on_Open_File "Rook on Open File")
	+ [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
	+ [Center Control](Center_Control "Center Control")
* [Outposts](Outposts "Outposts")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Connected Pawns](Connected_Pawns "Connected Pawns")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Square Control](King_Safety#SquareControl "King Safety")


### Misc


* [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")


## Forum Posts


### 2009


* [New open source engine called "Pawny"](http://www.talkchess.com/forum/viewtopic.php?t=29641) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), September 03, 2009
* [Re: New open source engine called "Pawny"](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=29641&start=9) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), September 04, 2009
* [Pawny - new version (0.11)](http://www.talkchess.com/forum/viewtopic.php?t=29763) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), September 15, 2009


### 2010 ...


* [Pawny 0.15 is out](http://www.talkchess.com/forum/viewtopic.php?t=31407) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), January 01, 2010
* [Pawny 0.1.6](http://www.talkchess.com/forum/viewtopic.php?t=32596) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), February 13, 2010
* [Pawny - Updated](http://www.talkchess.com/forum/viewtopic.php?t=33004) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), March 02, 2010
* [Pawny 0.2](http://www.talkchess.com/forum/viewtopic.php?t=35237) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), July 01, 2010
* [Pawny 0.2.1](http://www.talkchess.com/forum/viewtopic.php?t=37909) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), February 01, 2011
* [Pawny updated](http://www.talkchess.com/forum/viewtopic.php?t=41196) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), November 24, 2011
* [New Pawny](http://www.talkchess.com/forum/viewtopic.php?t=48163) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), May 31, 2013


### 2015 ...


* [Pawny 1.1](http://www.talkchess.com/forum/viewtopic.php?t=56668) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), June 14, 2015
* [Android Request](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=60531) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), June 19, 2016


## External Links


* [Pawny's Homepage](https://web.archive.org/web/20090908151549/http://pawny.netii.net:80/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), September 08, 2009)
* [Pawny's Homepage](https://web.archive.org/web/20190805192504/http://pawny.netii.net/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), August 05, 2019)


 [Pawny's Version History](https://web.archive.org/web/20190719112242/http://pawny.netii.net/version.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), July 19, 2019)
* [Index of /chess/engines/Jim Ablett/PAWNY](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/PAWNY/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
* [Pawny](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Pawny&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


## References


1. ↑ [1.0](#cite-ref-pawny-1-0) [1.1](#cite-ref-pawny-1-1) [Pawny's Homepage](https://web.archive.org/web/20090908151549/http://pawny.netii.net:80/) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), September 08, 2009)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Pawny's Version History](https://web.archive.org/web/20190719112242/http://pawny.netii.net/version.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), July 19, 2019)

**[Up one Level](Engines "Engines")**







 
