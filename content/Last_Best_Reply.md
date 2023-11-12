---
title: Last Best Reply
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Last Best Reply**


**Last Best Reply** (LBR) is a move ordering heuristic similar to the [Countermove heuristic](Countermove_Heuristic "Countermove Heuristic") but with more specific [move](Moves "Moves") matching.




```C++
*An idea proposed by [Steven Edwards](Steven_Edwards "Steven Edwards")* <a id="cite-note-1" href="#cite-ref-1">[1]</a>. *Sometimes it works, and sometimes it doesn't. But in any case, it will be more specific (and so have a better chance at working) than the Countermove heuristic. Note that any results may (will) be different as more move ordering techniques are added* <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 

```

### Contents


* [1 The Idea](#the-idea)
* [2 Implementation](#implementation)
* [3 Variants](#variants)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
* [6 References](#references)






At each [node](Node "Node") in a search where there is a prior non-null move, the [best move](Best_Move "Best Move") for that node is stored along with the prior move in an LBR (Last Best Reply) data store for the [ply](Ply "Ply") of the node. At move ordering time in all nodes, there are a first and a possible second move match operation. For the first match operation, the LBR data store for the current ply is examined for a match of the current prior move. If a match of the LBR stored prior move is made, then a second match operation is performed. In the second match operation, the generated moves at the node are scanned for a match with the LBR stored reply for the prior move. If this second match exists, the corresponding generated move is given a move ordering bonus so that it might be considered early in the move scan for the current node.


Unlike the Countermove heuristic, the LBR approach also uses the [moving man](Pieces "Pieces"), the [captured man](Captures "Captures") (if any) and the move special case (e.g., [en passant](En_passant "En passant"), [promotion](Promotions "Promotions")) for matching purposes. This means a less frequent match but a more appropriate match when one is made.



## Implementation


One way of implementing the LBR data store is by means of a [binary tree](https://en.wikipedia.org/wiki/Binary_tree) with each node having a hash of the prior move as a key and having the node's value being the reply move.



## Variants


1. Instead of the prior move, both the prior move and the move before it are used for the first match operation.
2. Instead of the prior move, the move two plies earlier is used.
3. LBR operations are skipped if the reply move is a [capture](Captures "Captures") or promotion.
4. Instead of an LBR data store at each ply, there are only two LBR data stores (one for each color) for an entire search.


## See also


* [Best Move](Best_Move "Best Move")
* [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
* [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [Refutation Move](Refutation_Move "Refutation Move")
* [Refutation Table](Refutation_Table "Refutation Table")


## Forum Posts


* [The LBR move ordering heuristic](http://www.talkchess.com/forum/viewtopic.php?t=38556) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 26, 2011
* [Move ordering idea (old and new?)](http://www.talkchess.com/forum/viewtopic.php?t=44749) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), Aug 09, 2012


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The LBR move ordering heuristic](http://www.talkchess.com/forum/viewtopic.php?t=38556) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 26, 2011
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Testing LBR](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=401117&t=38556) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 27, 2011

**[Up one Level](Move_Ordering "Move Ordering")**







 
