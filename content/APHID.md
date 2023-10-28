---
title: APHID
---
**[Home](Home "Home") * [Search](Search "Search") * [Parallel Search](Parallel_Search "Parallel Search") * APHID**

\[ Two adult aphids <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**APHID**, (Asynchronous Parallel Hierarchical Iterative Deepening)

an asynchronous parallel [alpha-beta](Alpha-Beta "Alpha-Beta") based search algorithm developed and elaborated by [Mark Brockington](Mark_Brockington "Mark Brockington") as topic of his Ph.D. thesis at the Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, along with his thesis advisor [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"). APHID uses repeated depth-limited searches of the top of the [search tree](Search_Tree "Search Tree") to instantiate, update and [load balance](<https://en.wikipedia.org/wiki/Load_balancing_(computing)>) work lists for other processors. APHID can be seen as a [master/slave](<https://en.wikipedia.org/wiki/Master/slave_(technology)>) model, but can be generalized to a hierarchical processor tree.

## Contents

- [1 Library](#library)
- [2 How it works](#how-it-works)
- [3 See also](#see-also)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
  - [6.1 Game Tree Search](#game-tree-search)
  - [6.2 Misc](#misc)
- [7 References](#references)

## Library

APHID has been programmed as an easy-to-implement, game-independent library <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and was implemented into the chess program [The Turk](The_Turk "The Turk") with less than one day of programming effort <a id="cite-note-4" href="#cite-ref-4">[4]</a>. It was further tested in [Crafty](Crafty "Crafty") in chess, in [Chinook](<https://en.wikipedia.org/wiki/Chinook_(draughts_player)>) in the domain of [Checkers](Checkers "Checkers"), and in Brockington's [Othello](Othello "Othello") program *Keyano* <a id="cite-note-5" href="#cite-ref-5">[5]</a>. APHID yields reasonable performance on a [network](https://en.wikipedia.org/wiki/Computer_network) of [workstations](https://en.wikipedia.org/wiki/Workstation), an architecture where it is extremely difficult to use a [shared transposition table](Shared_Hash_Table "Shared Hash Table") effectively. More recently, APHID was used within the [ChessBrain](ChessBrain "ChessBrain") project of over 2000 [internet](https://en.wikipedia.org/wiki/Internet) connected machines running [Beowulf](Beowulf "Beowulf") <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## How it works

The master is responsible for searching the top d' [plies](Ply "Ply") of the d-ply [tree](Search_Tree "Search Tree") inside its [iterative deepening](Iterative_Deepening "Iterative Deepening") frame. When the master reaches a [leaf](Leaf_Node "Leaf Node") of the d'-ply tree, it uses either a (d-d')-ply search result already available from the slave, or the "best available" i.e. using guessed scores from shallower previous searches marked as **uncertain**. As values get backed up the tree, the master maintains a count of how many uncertain nodes have been visited in a pass of the tree, and has to repeat the root search until all contributing leaves have reliable, certain results. By using the guessed score and expected [node types](Node_Types "Node Types"), the master decides which child-nodes are searched sequentially or in parallel.

[](File:Aphidybw.jpg)
Location of Parallelism in typical APHID and [YBW](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") [search trees](Search_Tree "Search Tree") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

The slave process essentially executes the same code that a sequential [alpha-beta](Alpha-Beta "Alpha-Beta") searcher would. It looks in the local copy of the so called APHID table, initially allocated and supplied by the master, to find the highest priority node to search. After finishing the search, it reports the result back to the master, getting an update to its APHID table entry in return.

## See also

- [ChessBrain](ChessBrain "ChessBrain")
- [Crafty](Crafty "Crafty")
- [The Turk](The_Turk "The Turk")
- [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")

## Publications

- [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
- [Mark Brockington](Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp02/NQ29023.pdf)
- [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1999**). *APHID: Asynchronous Parallel Game-Tree Search*. Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.9870&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)
- [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2000**). *APHID: Asynchronous Parallel Game-Tree Search*. [Journal of Parallel and Distributed Computing](https://www.journals.elsevier.com/journal-of-parallel-and-distributed-computing), Vol. 60, No. 2

## Forum Posts

- [Chess over LAN revisited - APHID](https://www.stmintz.com/ccc/index.php?id=189126) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), September 17, 2001

[APHID , advances in ICCA #8](https://www.stmintz.com/ccc/index.php?id=189259) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), September 18, 2001

- [Deep Crafty](https://groups.google.com/d/msg/rec.games.chess.computer/3Z5eCrUmA5U/x_eLJS4kELEJ) by Donald O. Davis, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 29, 2001
- [asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 06, 2010

[Re: asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652&start=8) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 07, 2010
[Re: asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652&start=11) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 08, 2010

- [scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 22, 2015 » [Scorpio](Scorpio "Scorpio")

## [Re: scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343&start=8) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 30, 2015 External Links

## Game Tree Search

- [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)

## Misc

- [Aphid from Wikipedia](https://en.wikipedia.org/wiki/Aphid)
- [aphid - Wiktionary](https://en.wiktionary.org/wiki/aphid)
- [Aphid (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Aphid_(disambiguation)>)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Aphidoidea](https://en.wikipedia.org/wiki/Aphid) in [Belgium](https://en.wikipedia.org/wiki/Belgium), [Image](https://commons.wikimedia.org/wiki/File:Aphidoidea_puceron_Luc_Viatour.jpg) by [Luc Viatour](https://commons.wikimedia.org/wiki/User:Lviatour), 2008, [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Mark Brockington](Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://www.collectionscanada.gc.ca/obj/s4/f2/dsk2/ftp02/NQ29023.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), 4. Experiments pp. 83
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Keyano (Othello) Home Page](https://webdocs.cs.ualberta.ca/~games/keyano/)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Colin Frayn](Colin_Frayn "Colin Frayn"), [Carlos Justiniano](Carlos_Justiniano "Carlos Justiniano"), [Kevin Lew](Kevin_Lew "Kevin Lew") (**2006**). *ChessBrain II – A Hierarchical Infrastructure for Distributed Inhomogeneous Speed-Critical Computation*. [pdf](http://www.chessbrain.net/docs/chessbrainII.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Image cropped from Figure 4, pp. 6 in [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX)

**[Up one level](Parallel_Search "Parallel Search")**

