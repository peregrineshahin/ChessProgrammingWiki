---
title: Exact Score
---
**[Home](Home "Home") * [Search](Search "Search") * [Score](Score "Score") * Exact Score**

An **Exact Score** is a [score](Score "Score") returned from an [alpha-beta](Alpha-Beta "Alpha-Beta") search, if [alpha](Alpha "Alpha"), the max so far, was improved, while the min-player improved his score as well (score \< beta). The current [node](Node "Node") searched was an expected [PV-Node](Node_Types#pv-node "Node Types"), which was confirmed by the search in finding and collecting a [principal variation](Principal_Variation "Principal Variation").

## Always or Never

- Pure [Minimax](Minimax "Minimax") always returns exact scores.
- A [Null Window](Null_Window "Null Window") search never returns exact scores.

## See also

- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Integrated Bounds and Values](Integrated_Bounds_and_Values "Integrated Bounds and Values")
- [Lower Bound](Lower_Bound "Lower Bound")
- [Score](Score "Score")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Upper Bound](Upper_Bound "Upper Bound")

## Forum Posts

- [Bounds... when is an exact score an EXACT score?](https://www.stmintz.com/ccc/index.php?id=309279) by [Ross Boyd](Ross_Boyd "Ross Boyd"), [CCC](CCC "CCC"), August 01, 2003
- [A few general questions...](http://www.talkchess.com/forum/viewtopic.php?t=42224) by [Bill Henry](index.php?title=Bill_Henry&action=edit&redlink=1 "Bill Henry (page does not exist)"), [CCC](CCC "CCC"), January 29, 2012 » [Root](Root "Root"), [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Exact node values](http://www.open-chess.org/viewtopic.php?f=5&t=2225) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 16, 2013

**[Up one level](Score "Score")**

