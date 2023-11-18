---
title: BestFirst Minimax Search
---
**[Home](Home "Home") * [Search](Search "Search") * Best-First Minimax Search**

**Best-First Minimax Search**, **(BFMMS)**

is a [Best-First search](Best-First "Best-First") algorithm based on [Best-First](Best-First "Best-First") and a shallow [alpha-beta](Alpha-Beta "Alpha-Beta") [depth-first-search](Depth-First "Depth-First") proposed by [Richard Korf](Richard_Korf "Richard Korf") and [Max Chickering](Max_Chickering "Max Chickering") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

BFMMS, [MCαβ](MC%CE%B1%CE%B2 "MCαβ"), the [Rollout Paradigm](Bojun_Huang#Rollout "Bojun Huang") and further [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")-minimax hybrids share the same idea, to combine Best-First with Depth-First searches.

## Four Phases

BFMMS can be divided into four strategic phases, repeated as long as there is time left:

1. In the Selection phase the best node is selected from the game tree via node score from the [root node](Root "Root") until it selects an unexpanded node
1. The Expansion strategy adds the unexpanded child nodes to the tree
1. The Playout phase performs a shallow alpha-beta search to get a node score
1. The Backpropagation strategy propagates the score through the tree

## See also

- [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
- [Rollout Paradigm](Bojun_Huang#Rollout "Bojun Huang")

## Publications

- [Richard Korf](Richard_Korf "Richard Korf"), [Max Chickering](Max_Chickering "Max Chickering") (**1996**). *[Best-First Minimax Search](https://www.microsoft.com/en-us/research/publication/best-first-minimax-search/)*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 84, No 1-2
- [Yaron Shoham](index.php?title=Yaron_Shoham&action=edit&redlink=1 "Yaron Shoham (page does not exist)"), [Sivan Toledo](index.php?title=Sivan_Toledo&action=edit&redlink=1 "Sivan Toledo (page does not exist)") (**2001**). *[Parallel Randomized Best-First Minimax Search](http://www.cs.tau.ac.il/~stoledo/Pubs/rbf-ai.pdf)*

## Forum Posts

- [MCTS without random playout?](http://www.talkchess.com/forum/viewtopic.php?t=41730) by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas"), [CCC](CCC "CCC"), January 01, 2012 » [B\*](B* "B*")
- [Help with Best-First Select-Formula](http://talkchess.com/forum/viewtopic.php?t=44165)  by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 23, 2012
- [Re: Announcing lczero](http://www.talkchess.com/forum/viewtopic.php?t=66280&start=67) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 21, 2018 » [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Alpha-Beta as a rollouts algorithm](http://www.talkchess.com/forum/viewtopic.php?t=66414) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 25, 2018 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [Scorpio](Scorpio "Scorpio")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Richard Korf](Richard_Korf "Richard Korf"), [Max Chickering](Max_Chickering "Max Chickering") (**1996**). *[Best-First Minimax Search](https://www.microsoft.com/en-us/research/publication/best-first-minimax-search/)*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 84, No 1-2

**[Up one level](Search "Search")**

