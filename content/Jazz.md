---
title: Jazz
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Jazz**



[ Origin of the word jazz <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Jazz**,  

an [open source engine](Category:Open_Source "Category:Open Source") under the [GNU General Public Licence](Free_Software_Foundation#GPL "Free Software Foundation") by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), written in [C](C "C"), first released in February 2011 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Jazz supports both, the [Universal Chess Interface](UCI "UCI") and [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), and using appropriate compiles, runs on [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS X](Mac_OS "Mac OS") boxes. 



### Contents


* [1 Description](#description)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Jazz](#jazz)
* [5 References](#references)






Jazz uses [bitboards](Bitboards "Bitboards"), first [rotated bitboards](Rotated_Bitboards "Rotated Bitboards"), later [Kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
It performs [fail-soft](Fail-Soft "Fail-Soft") [alpha-beta](Alpha-Beta "Alpha-Beta") [principal variation search](Principal_Variation_Search "Principal Variation Search") with [quiescence](Quiescence_Search "Quiescence Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [check extensions](Check_Extensions "Check Extensions"). [Move ordering](Move_Ordering "Move Ordering") considers [hash move](Hash_Move "Hash Move"), [mate killers](Mate_Killers "Mate Killers"), and along with a [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [winning captures](Captures "Captures") and [promotions](Promotions "Promotions"). Further, beside the [killer heuristic](Killer_Heuristic "Killer Heuristic") and [countermove heuristic](Countermove_Heuristic "Countermove Heuristic"), a so called **Combo Move** heuristics is used to possibly refute opponent moves along similar lines <a id="cite-note-4" href="#cite-ref-4">[4]</a>.
The implementation of a [multithreaded](Thread "Thread") [parallel search](Parallel_Search "Parallel Search") along the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") with [lock-less hashing](Shared_Hash_Table#Lockless "Shared Hash Table") was elaborated by Evert Glebbeek in a April 2013 [CCC](CCC "CCC") posting <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Jazz' [evaluation](Evaluation "Evaluation") takes [material](Material "Material"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility"), and [king safety](King_Safety "King Safety") into account.



## See also


* [Sjaak](Sjaak_(Glebbeek) "Sjaak (Glebbeek)")
* [Leonidas](index.php?title=Leonidas&action=edit&redlink=1 "Leonidas (page does not exist)")


## Forum Posts


* [Chess engine Jazz now available](http://www.talkchess.com/forum/viewtopic.php?t=38176) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), February 22, 2011
* [Jazz r444](http://www.talkchess.com/forum/viewtopic.php?t=38333) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 08, 2011
* [Jazz r501 (source only)](http://www.talkchess.com/forum/viewtopic.php?t=40616) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 02, 2011
* [Jazz 640 released](http://www.talkchess.com/forum/viewtopic.php?t=46988) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 24, 2013
* [Implementation of multithreaded search in Jazz](http://www.talkchess.com/forum/viewtopic.php?t=47820) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 20, 2013 » [Parallel Search](Parallel_Search "Parallel Search"), [Thread](Thread "Thread")
* [Jazz r818](http://www.talkchess.com/forum/viewtopic.php?t=54668) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), December 17, 2014


## External Links


### Chess Engine


* [Chess (Jazz & Sjaak) home](http://www.eglebbk.dds.nl/program/chess-index.html)
* [Chess (Jazz & Sjaak) history](http://www.eglebbk.dds.nl/program/chess-hist.html)
* [Chess (Jazz & Sjaak) design](http://www.eglebbk.dds.nl/program/chess-design.html)
* [Chess (Jazz & Sjaak) search](http://www.eglebbk.dds.nl/program/chess-search.html)
* [Chess (Jazz & Sjaak) evaluation](http://www.eglebbk.dds.nl/program/chess-eval.html)
* [Jazz](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Jazz&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Jazz


* [Jazz (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Jazz_%28disambiguation%29)
* [Jazz from Wikipedia](https://en.wikipedia.org/wiki/Jazz)
* [Willem Breuker Kollektief](Category:Willem_Breuker "Category:Willem Breuker") - Amsterdamned Jazz, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Jazz (word) from Wikipedia](https://en.wikipedia.org/wiki/Jazz_%28word%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chess engine Jazz now available](http://www.talkchess.com/forum/viewtopic.php?t=38176) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), February 22, 2011
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess (Jazz & Sjaak) design](http://www.eglebbk.dds.nl/program/chess-design.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess (Jazz & Sjaak) search](http://www.eglebbk.dds.nl/program/chess-search.html)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Implementation of multithreaded search in Jazz](http://www.talkchess.com/forum/viewtopic.php?t=47820) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 20, 2013

**[Up one Level](Engines "Engines")**







 
