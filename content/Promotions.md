---
title: Promotions
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Promotions**



 [](http://www.carinajorgensen.com/Chess/pawnqueen.php) [Carina Jørgensen](Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen") - Queening Pawn <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Promotions** are [tactical moves](Tactical_Moves "Tactical Moves") changing [material balance](Material#Balance "Material") where a [pawn](Pawn "Pawn") reaches its [promotion square](Promotion_Square "Promotion Square") on the eighth (or first) [rank](Ranks "Ranks") to transform to a [piece](Pieces "Pieces") of the players choice, either a [queen](Queen "Queen"), [knight](Knight "Knight"), [rook](Rook "Rook") or [bishop](Bishop "Bishop") of the same [color](Color "Color"). The pawn may reach the eighth rank due to a [pawn push](Pawn_Push "Pawn Push") or [capture](Captures "Captures"). A pawn promoting to a queen while capturing the opponent queen defines the maximum amount of [material](Material "Material") a move may gain. 



## Queening versus Minor Promotions


Most often in practical play promotions occur to the strongest piece, the queen, also referred as **queening**. A promotion to other than the queen is called minor- or underpromotion, where once in a while the promotion to a knight has some practical relevance due to its distinct attacking with the possibility to check <a id="cite-note-2" href="#cite-ref-2">[2]</a> or to fork, see for instance what happened at [ACM 1991](ACM_1991#KnightPromotion "ACM 1991") in [Albuquerque](https://en.wikipedia.org/wiki/Albuquerque%2C_New_Mexico) to [Lachex](Lachex "Lachex")<a id="cite-note-3" href="#cite-ref-3">[3]</a> . Minor promotions to rook and bishop, whose attacks are sub-set of the queen are very rarely about to avoid [stalemate](Stalemate "Stalemate") - or may occur at the [root](Root "Root") in cases the promoted piece may be captured immediately anyway. In [move encoding](Encoding_Moves "Encoding Moves") the promoted piece requires two extra bits.



## Minor Generation


In [move generation](Move_Generation "Move Generation") it is quite common while producing the queen promotion, also to generate all the additional minor promotions, that is to write four moves to a [move list](Move_List "Move List") with all two-bit combinations indicating the promoted piece, instead of one. However, some programs only generate queening and use [unmake move](Unmake_Move "Unmake Move") of a queen promotion as trigger to conditionally generate further minor promotions, assuming the queen promotion didn't fail high or its refutation was not an immediate capture. Bishop and rook promotions may only generated if the queen promotion returns an explicit stalemate score. Other programs even omit minor promotions or at least underpromotions to rook and bishop inside their [search](Search "Search") except the root at all, with the motivation the reduced code and [branching factor](Branching_Factor "Branching Factor") likely pays off in practical playing strength. In [quiescence search](Quiescence_Search "Quiescence Search") most programs only consider queening.



## GUI Issues


[Entering moves](Entering_Moves "Entering Moves") by a human operator within a [graphical user interface](GUI "GUI") requires [modal](https://en.wikipedia.org/wiki/Modality_%28human-computer_interaction%29) [interaction](https://en.wikipedia.org/wiki/Interaction), for instance [dragging](https://en.wikipedia.org/wiki/Drag-and-drop) the piece with a [mouse](https://en.wikipedia.org/wiki/Mouse_%28computing%29) from the departure square to a destination square. In case of promotions a [modal dialog](https://en.wikipedia.org/wiki/Modal_window) or [pop-up menu](https://en.wikipedia.org/wiki/Context_menu) is necessary to choose the promoted piece to finally terminate the modal move entering interaction.



## See also


* [ACM 1991 | Mephisto - Lachex](ACM_1991#KnightPromotion "ACM 1991")
* [Algebraic Chess Notation - Promotions](Algebraic_Chess_Notation#Promotions "Algebraic Chess Notation")
* [Entering Moves](Entering_Moves "Entering Moves")
* [Famous Bugs](Engine_Testing#bugs "Engine Testing")
* [HAKMEM 70](Bill_Gosper#HAKMEM70 "Bill Gosper")
* [Material](Material "Material")
* [Promotion Square](Promotion_Square "Promotion Square")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Tactical Moves](Tactical_Moves "Tactical Moves")


## Publications


* [Harold van der Heijden](Harold_van_der_Heijden "Harold van der Heijden") (**1996**). *Pawn Promotion*. [New in Chess](https://en.wikipedia.org/wiki/New_in_Chess), Alkmaar ISBN 90-5691-005-1
* [Glen Robert Downey](https://en.wikipedia.org/wiki/Glen_Downey_%28writer%29) (**1998**). *The Truth About Pawn Promotion: The Development of the Chess Motif in Victorian Fiction*. Ph.D. thesis, [University of Victoria](https://en.wikipedia.org/wiki/University_of_Victoria) [pdf](http://www.nlc-bnc.ca/obj/s4/f2/dsk2/tape15/PQDD_0006/NQ34258.pdf) » [Alice](Alice "Alice") <a id="cite-note-4" href="#cite-ref-4">[4]</a>


## Forum Posts


### 1989


* [Underpromotion](https://groups.google.com/d/msg/rec.games.chess/4-it0dcvRIk/0405G7EuKecJ) by [Ilan Vardi](Ilan_Vardi "Ilan Vardi"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), May 04, 1989


### 1990 ...


* [Underpromoting other than to a knight](https://www.stmintz.com/ccc/index.php?id=14777) by [David Fotland](David_Fotland "David Fotland"), [CCC](CCC "CCC"), January 29, 1998
* [Pawn promotion defense](https://www.stmintz.com/ccc/index.php?id=72219) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), October 07, 1999


### 2000 ...


* [Promotion frequency](https://www.stmintz.com/ccc/index.php?id=242025) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), July 23, 2002
* [Promotion to Knight Wins](https://www.stmintz.com/ccc/index.php?id=366606) by [Rob Basham](index.php?title=Rob_Basham&action=edit&redlink=1 "Rob Basham (page does not exist)"), [CCC](CCC "CCC"), May 22, 2004
* [The Perils of missing sub-promotion](http://www.talkchess.com/forum/viewtopic.php?t=16762) by [Nicolai Czempin](Nicolai_Czempin "Nicolai Czempin"), [CCC](CCC "CCC"), September 28, 2007


### 2010 ...


* [Re: Botvinnik Markov revisited](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=358597&t=35124) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), June 27, 2010 » [Komodo](Komodo "Komodo")
* [Strange knight underpromotion by Critter](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=335316&t=33059) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), March 04, 2010
* [Wanted - Bishop promotion FEN](http://www.talkchess.com/forum/viewtopic.php?t=42783) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), March 07, 2012
* [Some statistics about promotions and underpromotions](http://www.talkchess.com/forum/viewtopic.php?t=48808) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), July 31, 2013
* [Tough promotion bug(s)](http://www.talkchess.com/forum/viewtopic.php?t=49034) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), August 29, 2013


### 2015 ...


* [Stockfish underpromotes much more often than Komodo](http://www.talkchess.com/forum/viewtopic.php?t=61601) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), October 05, 2016 » [Komodo](Komodo "Komodo"), [Match Statistics](Match_Statistics "Match Statistics"), [Stockfish](Stockfish "Stockfish")
* [correct way to score promotions using MVV-LVA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70936) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 06, 2019 » [MVV-LVA](MVV-LVA "MVV-LVA")


### 2020 ...


* [underpromoting is worth how many elo?](https://groups.google.com/d/msg/fishcooking/DAWWlmP2OrQ/3w_KhoaUAAAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 08, 2020
* [Under promotion of a pinned pawn to bishop](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74984) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 03, 2020


## External Links


* [Promotion (chess) from Wikipedia](https://en.wikipedia.org/wiki/Promotion_%28chess%29)
* [Babson task from Wikipedia](https://en.wikipedia.org/wiki/Babson_task)
* [Saavedra position from Wikipedia](https://en.wikipedia.org/wiki/Saavedra_position)
* [Joe Henderson Quartet](Category:Joe_Henderson "Category:Joe Henderson") - Ya La Quiero, [Burghausen](https://de.wikipedia.org/wiki/Internationale_Jazzwoche_Burghausen) 1987, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Joe Henderson](Category:Joe_Henderson "Category:Joe Henderson"), [Kim Clarke](Category:Kim_Clarke "Category:Kim Clarke"), [Renee Rosnes](https://en.wikipedia.org/wiki/Renee_Rosnes), [Sylvia Cuenca](http://www.sylviacuenca.com/)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Queening Pawn](http://www.carinajorgensen.com/Chess/pawnqueen.php) by [Carina Jørgensen](Category:Carina_J%C3%B8rgensen "Category:Carina Jørgensen"), 2008
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Lasker Trap from Wikipedia](https://en.wikipedia.org/wiki/Lasker_Trap) features an underpromotion as early as the seventh move
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> Page 18 in the [PDF report](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1993_23rd_ACM_ICCC/1993%20ICCC.062303066.sm.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Through the Looking-Glass from Wikipedia](https://en.wikipedia.org/wiki/Through_the_Looking-Glass)

**[Up one Level](Moves "Moves")**







 
