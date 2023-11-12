---
title: Root
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Node](Node "Node") \* Root**


The **Root** of the [Search Tree](Search_Tree "Search Tree") is the initial [position](Chess_Position "Chess Position") of the [search](Search "Search"). Many programmers dedicate a separate function for doing a root search, since using a different [move ordering](Move_Ordering "Move Ordering") scheme may be beneficial. Also root search must return not only the value, but also the [move](Best_Move "Best Move") which will be played. This in turn may require special care in case of a fail-low when using [aspiration window](Aspiration_Windows "Aspiration Windows"). This is typically where the [time management](Time_Management "Time Management") decisions are beneficial.



## Forum Posts


### 1997 ...


* [computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/99eec6923b0481db) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 1, 1997


 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/0df39371422a600c) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 3, 1997
 [Re: computer chess "oracle" ideas...](http://groups.google.com/group/rec.games.chess.computer/msg/ccc2546e26d92f88) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
* [Failing low at the root](https://www.stmintz.com/ccc/index.php?id=23672) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), August 03, 1998
* [Question: Fail High then Low at Root](https://www.stmintz.com/ccc/index.php?id=84651) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), December 28, 1999 » [Fail-High](Fail-High "Fail-High"), [Fail-Low](Fail-Low "Fail-Low"), [Search Instability](Search_Instability "Search Instability")


### 2000 ...


* [Can we use hash table at root?](https://www.stmintz.com/ccc/index.php?id=93686) by Tim, [CCC](CCC "CCC"), January 31, 2000 » [Transposition Table](Transposition_Table "Transposition Table")
* [Question: Fail low at root and time management](https://www.stmintz.com/ccc/index.php?id=95710) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), February 08, 2000 » [Fail-Low](Fail-Low "Fail-Low"), [Time Management](Time_Management "Time Management")
* [Root move and incomplete iteration](https://www.stmintz.com/ccc/index.php?id=144413) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), December 11, 2000


 [Re: Root move and incomplete iteration](https://www.stmintz.com/ccc/index.php?id=144432) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 11, 2000
* [What means lazy/plain alpha bounding?](https://www.stmintz.com/ccc/index.php?id=153648) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), February 06, 2001 » [Fail-High](Fail-High "Fail-High")


### 2005 ...


* [Even more search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6666) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")


### 2010 ...


* [Root node search](http://www.talkchess.com/forum/viewtopic.php?t=38404) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
* [Root node search in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=39346) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), June 12, 2011 » [Stockfish](Stockfish "Stockfish")
* [A few general questions...](http://www.talkchess.com/forum/viewtopic.php?t=42224) by [Bill Henry](index.php?title=Bill_Henry&action=edit&redlink=1 "Bill Henry (page does not exist)"), [CCC](CCC "CCC"), January 29, 2012 » [Exact Score](Exact_Score "Exact Score"), [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Pruning in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=50907) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 14, 2014 » [Reductions](Reductions "Reductions"), [Node Types](Node_Types "Node Types")
* [Solving a fail low situation at the root](http://www.talkchess.com/forum/viewtopic.php?t=54241) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), November 03, 2014 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [Fail-Low](Fail-Low "Fail-Low")


### 2015 ...


* [Ordering of Root moves and search instability !](http://www.talkchess.com/forum/viewtopic.php?t=58055) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Move Ordering](Move_Ordering "Move Ordering"), [Search Instability](Search_Instability "Search Instability")
* [Root search](http://www.talkchess.com/forum/viewtopic.php?t=61358) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), September 08, 2016


### 2020 ...


* [Move ordering at the root](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78552) by Jonathan McDermid, [CCC](CCC "CCC"), October 30, 2021 » [Move Ordering - Root Node Considerations](Move_Ordering#Root "Move Ordering")


## External Links


* [Root from Wikipedia](https://en.wikipedia.org/wiki/Root)
* [Root (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Root_(disambiguation))
* [Ian Carr's](Category:Ian_Carr "Category:Ian Carr") [Nucleus](Category:Nucleus "Category:Nucleus") - [Roots](https://en.wikipedia.org/wiki/Ian_Carr#Nucleus), 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
**[Up one Level](Node "Node")**







 
