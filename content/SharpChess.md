---
title: SharpChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SharpChess**



 [](http://sharpchess.com/?page=50%20Development/01%20Object%20Model) SharpChess [GUI](GUI "GUI") <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**SharpChess**,  

a free [open source chess program](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") written by [Peter Hughes](index.php?title=Peter_Hughes&action=edit&redlink=1 "Peter Hughes (page does not exist)") in [C#](C_sharp "C sharp"), running on [Microsoft](Microsoft "Microsoft") [Windows](Windows "Windows") [.NET](https://en.wikipedia.org/wiki/.NET_Framework) or [Mono](https://en.wikipedia.org/wiki/Mono_%28software%29). 
It has its own [GUI](GUI "GUI") and additionally supports the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and can therefore play against other chess engines using [WinBoard](WinBoard "WinBoard") or [Arena](Arena "Arena"). An [object model](https://en.wikipedia.org/wiki/Object_model) <a id="cite-note-2" href="#cite-ref-2">[2]</a> may enable other developers to quickly get involved into the project <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Contents


* [1 Description](#description)
* [2 Namesake](#namesake)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






SharpChess uses the [0x88](0x88 "0x88") board representation to utilize [PVS](Principal_Variation_Search "Principal Variation Search") within an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework. The [transposition table](Transposition_Table "Transposition Table") is indexed and verified by [Zobrist keys](Zobrist_Hashing "Zobrist Hashing"), [move ordering](Move_Ordering "Move Ordering") considers [hash move](Hash_Move "Hash Move"), [MVV/LVA](MVV-LVA "MVV-LVA"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), and beside [quiescence search](Quiescence_Search "Quiescence Search"), [selectivity](Selectivity "Selectivity") is applied by [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") and [extending](Extensions "Extensions") on [checks](Check_Extensions "Check Extensions"), [recaptures](Recapture_Extensions "Recapture Extensions") of pieces with same value, [single replies](One_Reply_Extensions "One Reply Extensions"), and [pawn pushes to the seventh rank](Passed_Pawn_Extensions "Passed Pawn Extensions").



## Namesake


* [#Chess](Sharp_Chess "Sharp Chess") by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson")


## Forum Posts


* [A new SharpChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2078) by [Peter Hughes](index.php?title=Peter_Hughes&action=edit&redlink=1 "Peter Hughes (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 25, 2005
* [Move Analysis Tree](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52137) by [Peter Hughes](index.php?title=Peter_Hughes&action=edit&redlink=1 "Peter Hughes (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 05, 2012


## External Links


* [SharpChess: Home](http://sharpchess.com/?page=01%20Home)
* [PeterHughes/SharpChess - GitHub](https://github.com/PeterHughes/SharpChess)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [SharpChess: Tecnical Details](http://sharpchess.com/?page=50%20Development/01%20Object%20Model)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [SharpChess: Object Model](http://sharpchess.com/?page=50%20Development/01%20Object%20Model)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [SharpChess: Home](http://sharpchess.com/?page=01%20Home)

**[Up one level](History "History")**







 
