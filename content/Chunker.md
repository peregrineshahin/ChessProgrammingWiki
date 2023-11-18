---
title: Chunker
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chunker**

**Chunker**,

a chess program by [Murray Campbell](Murray_Campbell "Murray Campbell") and [Hans Berliner](Hans_Berliner "Hans Berliner") in the domain of certain [pawn endgames](Pawn_Endgame "Pawn Endgame"), using [chunked](Chunking "Chunking") [knowledge](Knowledge "Knowledge"). Chunks were defined as groups of pawns and king that can be handled relatively independently of each other. Chunker [parses](https://en.wikipedia.org/wiki/Shallow_parsing) a [position](Chess_Position "Chess Position") into chunks, and reasons about the position using information obtained from chunk libraries. There are several chunk libraries, each corresponding to a fixed group of [pieces](Pieces "Pieces") (a chunk type). Each chunk type has certain properties, and each chunk instance (a particular configuration of the chunk type) has values attached to the properties. These are used both in evaluation, by allowing reasoning with chunk property values to produce an [evaluation](Evaluation "Evaluation") of the whole position, and in move selection, to facilitate reaching positions where this is possible.

Some types of chunks that could occur are so complex and rare that to build libraries for all possibilities would require unrealistically large memories. Fur such chunks (containing double pawns for instance) it will be necessary to do the analysis to produce properties on the fly. However, once such an analysis is done, these properties can be retained in a temporary chunk library for the duration of the solution process <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Szén Position

Due to its chunk library of king versus three [connected passers](Connected_Passed_Pawns "Connected Passed Pawns"), Chunker is an expert in playing the **Szén position**, popularized by the Hungarian chess player [József Szén](https://en.wikipedia.org/wiki/J%C3%B3zsef_Sz%C3%A9n) in the first half of the nineteenth century, with a lineage dating from [Gioacchino Greco](https://en.wikipedia.org/wiki/Gioachino_Greco) two centuries before with wK and bK on e1 and e8 respectively <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

|  |
| --- |
|                                                                                             ♚        ♟♟♟                                ♙♙♙        ♔     |

```C++
4k3/5ppp/8/8/8/8/PPP5/3K4 w - - 

```

## Abstract

*Using Chunking to Solve Chess Pawn Endgames* <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

```C++
CHUNKER is a chess program that uses chunked knowledge to improve its performance. Its domain is a subset of king and pawn endings in chess that has been studied for over 300 years. CHUNKER has a large library of chunk instances where each chunk type has a property list and each instance has a set of values for these properties. This allows CHUNKER to reason about positions that come up in the search that would otherwise have to be handled by means of additional search. Thus the program is able to solve the most difficult problem of its present domain (a problem that would require 45 ply of search and on the order of 1013 years of CPU time to be solved by the best of present day chess programs) in 18 ply and one minute of CPU time. Further, CHUNKER is undoubtedly the world's foremost expert in its domain, and has discovered 2 mistakes in the literature and has been instrumental in discovering a new theorem about the domain that allows the assessing of positions with a new degree of ease and confidence. In this paper we show how the libraries are compiled, how CHUNKER works, and discuss our plans for extending it to play the whole domain of king and pawn endings. 

```

## See also

- [PawnKing](PawnKing "PawnKing")
- [Peasant](Peasant "Peasant")

## Publications

- [Murray Campbell](Murray_Campbell "Murray Campbell"), [Hans Berliner](Hans_Berliner "Hans Berliner") (**1983**). *A Chess Program That Chunks*. AAAI 1983 49-53, [pdf](http://www.aaai.org/Papers/AAAI/1983/AAAI83-012.pdf)
- [Hans Berliner](Hans_Berliner "Hans Berliner"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1984**). *[Using Chunking to Solve Chess Pawn Endgames](http://www.sciencedirect.com/science/article/pii/0004370284900067)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 23, No. 1, pp. 97-120. ISSN 0004-3702
- [Murray Campbell](Murray_Campbell "Murray Campbell") (**1988**). *Chunking as an Abstraction Mechanism*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")

## External Links

- [Shallow parsing from Wikipedia](https://en.wikipedia.org/wiki/Shallow_parsing)
- [The Lounge Lizards](Category:The_Lounge_Lizards "Category:The Lounge Lizards") - [Voice of Chunk](https://en.wikipedia.org/wiki/Voice_of_Chunk) (1988), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[John Lurie](https://en.wikipedia.org/wiki/John_Lurie), [Evan Lurie](https://en.wikipedia.org/wiki/Evan_Lurie), [Roy Nathanson](https://en.wikipedia.org/wiki/Roy_Nathanson), [Curtis Fowlkes](https://en.wikipedia.org/wiki/Curtis_Fowlkes), [Marc Ribot](Category:Marc_Ribot "Category:Marc Ribot"), [Dougie Bowne](https://www.facebook.com/dougie.bowne?_fb_noscript=1), [Erik Sanko](https://en.wikipedia.org/wiki/Erik_Sanko), [E.J. Rodriguez](http://www.jazzpassengers.com/?_escaped_fragment_=ej-rodriguez/c1tzv#!ej-rodriguez/c1tzv)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Murray Campbell](Murray_Campbell "Murray Campbell"), [Hans Berliner](Hans_Berliner "Hans Berliner") (**1983**). *A Chess Program That Chunks*. AAAI 1983 49-53, [pdf](http://www.aaai.org/Papers/AAAI/1983/AAAI83-012.pdf)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Jon Speelman](https://en.wikipedia.org/wiki/Jon_Speelman) (**1983**). *The Szen Position*. [EG73](http://www.gadycosteff.com/eg/eg.html), [pdf](http://www.gadycosteff.com/eg/eg73.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [At a glance you may think this is a draw. White wins](http://www.talkchess.com/forum/viewtopic.php?t=48125) by Robert Flesher, [CCC](CCC "CCC"), May 26, 2013
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Now Szén position solved in 15 seconds by regular Stockfish!](http://www.talkchess.com/forum/viewtopic.php?t=60802) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), July 12, 2016
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1984**). *[Using Chunking to Solve Chess Pawn Endgames](http://www.sciencedirect.com/science/article/pii/0004370284900067)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 23, No. 1, pp. 97-120. ISSN 0004-3702, Abstract

**[Up one Level](Engines "Engines")**

