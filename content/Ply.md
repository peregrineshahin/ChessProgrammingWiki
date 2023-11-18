---
title: Ply
---
**[Home](Home "Home") \* [Dictionary](Dictionary "Dictionary") \* Ply**



[ Making a three ply yarn <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The word **Ply** denotes a **half-move**, that is a [move](Moves "Moves") of one side only. When we speak of a "6 ply search", we mean three full moves - something like 1. e2e4 e7e5 2. g1f3 b8c6 3. b1c3 g8f6.


A full ply has been a natural unit for counting search [depth](Depth "Depth") before the introduction of [selective search](Selectivity "Selectivity") techniques. Today, if a program claims to do a 12-ply search, it informs us only about the parameter fed into [search function](Search "Search"). Some lines might have been severely [reduced](Reductions "Reductions"), others - [extended](Extensions "Extensions"). To make matters even more complex, top programs often use [fractional](Depth#FractionalPlies "Depth") extensions and reductions, changing depth by less than one full ply and taking effect only when they accumulate.


A typical [depth-first](Depth-First "Depth-First") non-uniform depth search decouples node-distance to the [horizon](Horizon_Node "Horizon Node") from node-distance to the [root](Root "Root"). Often, two distinct parameters of a [recursive](Recursion "Recursion") search routine were used. While searching deeper, one parameter, distance to horizon, often called "depth", "height" or "draft", is decremented by a number possibly in fractional ply units, which could be less than one ply in case of extensions or more than one ply in case of reductions, while the second parameter "ply" starts with zero at the root and is incremented exactly by one each search call deeper. It corresponds to one level of the [search tree](Search_Tree "Search Tree") and can act as index (ply-index) into a random accessible [search stack](Stack "Stack"), an [array](Array "Array") of [node states](Node "Node"). 



## Forum Posts


* [maximal ply that programs need today](http://www.talkchess.com/forum/viewtopic.php?t=51054) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 26, 2014
* [On reaching maximum ply](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77202) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), April 29, 2021 » [Maximum Search Depth](Depth#MaxPly "Depth"), [Search](Search "Search")


## External Links


* [Ply from Wikipedia](https://en.wikipedia.org/wiki/Ply)
* [Ply (game theory) from Wikipedia](https://en.wikipedia.org/wiki/Ply_%28game_theory%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Plying from Wikipedia](https://en.wikipedia.org/wiki/Plying)

**[Up one Level](Dictionary "Dictionary")**







 
