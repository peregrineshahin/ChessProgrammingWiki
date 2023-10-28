---
title: Search Tree
---
**[Home](Home "Home") \* [Search](Search "Search") \* Tree**



[,_oil_on_canvas,_79.7_x_109.1_cm,_Gemeentemuseum_Den_Haag,_Netherlands.jpg) [Piet Mondrian](Category:Piet_Mondrian "Category:Piet Mondrian") - [Gray Tree](https://en.wikipedia.org/wiki/Gray_Tree), 1912 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **Search Tree** as part of the [game tree](https://en.wikipedia.org/wiki/Game_tree) is a dynamical, hierarchical data-structure, a [directed graph](https://en.wikipedia.org/wiki/Graph_%28mathematics%29#Directed_graph) of [nodes](Node "Node"), also called [vertices](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29) or [states](https://en.wikipedia.org/wiki/State_diagram), connected by directed **edges**, also called **arcs**, or [state transitions](https://en.wikipedia.org/wiki/State_transition_table). In the game of chess, nodes represent the alternating white and black to move [chess positions](Chess_Position "Chess Position"), and directed edges represent the alternating white and black [moves](Moves "Moves"). 


Opposed to the wooden [plants](https://en.wikipedia.org/wiki/Tree), which are due to their similar structure [metaphor](https://en.wikipedia.org/wiki/Metaphor) of the search tree, where the [root](https://en.wikipedia.org/wiki/Root) is inside the bottom ground, the root of a search tree is most often illustrated from the top down to the leaves at the bottom. Due to our text-flow from top to bottom (after left to right), this might considered as [endianness](Endianness "Endianness") of the search tree illustration. 



### Contents


* [1 Alpha-Beta Tree](#alpha-beta-tree)
* [2 Topology](#topology)
* [3 Transpositions](#transpositions)
* [4 Cycles](#cycles)
* [5 Tree walk](#tree-walk)
* [6 Minimal Search Trees](#minimal-search-trees)
	+ [6.1 Minimal Alpha-Beta Tree](#minimal-alpha-beta-tree)
	+ [6.2 Minimal PV Tree](#minimal-pv-tree)
* [7 See also](#see-also)
* [8 Publications](#publications)
* [9 Forum Posts](#forum-posts)
* [10 External Links](#external-links)
* [11 References](#references)






 [](http://www.ics.uci.edu/%7Eeppstein/180a/970422.html) 
An [Alpha-Beta](Alpha-Beta "Alpha-Beta") Search Tree <a id="cite-note-2" href="#cite-ref-2">[2]</a>



## Topology


The [root](Root "Root") of the search tree is the position we like to evaluate to find the [best move](Best_Move "Best Move"). Leaves are either terminal nodes (mate, stalemate) or nodes which has been assigned a heuristic value, where the desired [depth](Depth "Depth") from the root is accomplished. 



* [Root Node](Root "Root")
* [Leftmost Node](Leftmost_Node "Leftmost Node")
* [Sibling Node](Sibling_Node "Sibling Node")
* [Interior Node](Interior_Node "Interior Node")
* [Leaf Node](Leaf_Node "Leaf Node")
* [Terminal Node](Terminal_Node "Terminal Node")
* [Branching Factor](Branching_Factor "Branching Factor")


## Transpositions


Because of [transpositions](Transposition "Transposition") due to different move sequences, nodes inside the tree may occur from various ancestors - even within a different number of moves. A common sample from the [Sveshnikov Variation](https://en.wikipedia.org/wiki/Sicilian_Defence#Sveshnikov_Variation:_4...Nf6_5.Nc3_e5) in the Sicilian:





|  |
| --- |
|                                                                   ♜ ♝♛♚♝ ♜♟♟   ♟♟♟  ♞♟ ♞   ♘  ♟ ♗     ♙     ♘     ♙♙♙  ♙♙♙♖  ♕♔♗ ♖ |


1. e4 c5 2. Nf3 d6 3. d4 cxd 4. Nxd4 Nf6 5. Nc3 Nc6 6. Bg5 e5 7. Ndb5  

1. e4 c5 2. Nc3 e6 3. Nf3 Nc6 4. d4 cxd 5. Nxd4 Nf6 6. Ndb5 d6 7. Bf4 e5 8 Bg5




## Cycles


The search tree may contain various cycles, since both sides may [repeat](Repetitions "Repetitions") a former position with the minimum of two [reversible moves](Reversible_Moves "Reversible Moves") each, or four [plies](Ply "Ply"). Cycles are usually eliminated and not searched twice, which results in searching a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG).



## Tree walk


Whether the search tree has to reside in memory the whole search, depends on which algorithm is used to [traverse](https://en.wikipedia.org/wiki/Tree_traversal) and expand it. So called [Depth-First](Depth-First "Depth-First") search algorithms, like [Alpha-Beta](Alpha-Beta "Alpha-Beta"), starts at the root and explores as far as possible along each branch before backtracking, and only has to keep one path from the root to the current position in memory. [Best-First](Best-First "Best-First") approaches build a search-tree by visiting and expanding the most promising nodes first.




## Minimal Search Trees


Minimal Search Trees require optimal move ordering in [Alpha-Beta](Alpha-Beta "Alpha-Beta") or its enhancements. Of course, this goal requires an [oracle](Oracle "Oracle"), since we don't know the best moves in advance - otherwise we wouldn't search at all. Thus rarely the expected [Node Types](Node_Types "Node Types") don't behave as expected, but Cut-Nodes don't fail high, because their All-Node child fails high instead. Anyway, due to [Iterative Deepening](Iterative_Deepening "Iterative Deepening") with [Transposition Table](Transposition_Table "Transposition Table"), [Move Ordering](Move_Ordering "Move Ordering") is already quite good, so this occurs quite rarely. Often, if the first move on an expected Cut-Node fails to cut, there are still other moves which do the cut.



### Minimal Alpha-Beta Tree


A perfectly ordered Tree, [All-Nodes](Node_Types#ALL "Node Types") (A) need to consider all successors, [Cut-Nodes](Node_Types#CUT "Node Types") (C) only the one which already refutes the opponent move.




```

                (A)
               / | \
             /   |   \
           /     |     \
         /       |       \
       /         |         \
     [A]        [C]        [C]
    / | \        |          |
   /  |  \       |          |
 (A) (C) (C)    (A)        (A)
 /|\  |   |     /|\        /|\
[ACC][A] [A]   [CCC]      [CCC]

```

### Minimal PV Tree


A minimal, perfectly ordered search tree, with [Knuth's](Donald_Knuth "Donald Knuth") [Node Types](Node_Types "Node Types"). Only the [PV-Nodes](Node_Types#PV "Node Types") (P) are searched with an open alpha-beta window. [Cut-Nodes](Node_Types#CUT "Node Types") as children or sibling of PV-Nodes require a [Scout-search](Scout "Scout"), to prove the nodes are greater or equal to beta. An [All-Node](Node_Types#ALL "Node Types") as successor of Cut-Nodes has to consider all moves to prove no move will cause a [beta-cutoff](Beta-Cutoff "Beta-Cutoff").




```

                (P)
               / | \
             /   |   \
           /     |     \
         /       |       \
       /         |         \
     [P]        [C]        [C]
    / | \        |          |
   /  |  \       |          |
 (P) (C) (C)    (A)        (A)
 /|\  |   |     /|\        /|\
[PCC][A] [A]   [CCC]      [CCC]

```

## See also


* [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [NegaScout](NegaScout "NegaScout") or [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Repetitions](Repetitions "Repetitions")
* [Scout](Scout "Scout")
* [Search Space](Search_Space "Search Space")
* [Transposition](Transposition "Transposition")


## Publications


* [Donald Michie](Donald_Michie "Donald Michie") (**1966**). *Game Playing and Game Learning Automata.* Advances in Programming and Non-Numerical Computation, [Leslie Fox](https://en.wikipedia.org/wiki/Leslie_Fox) (ed.), pp. 183-200. Oxford, Pergamon. » Includes Appendix: *Rules of SOMAC* by [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), introduces [Expectiminimax tree](https://en.wikipedia.org/wiki/Expectiminimax_tree) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Chun-Hung Tzeng](Chun-Hung_Tzeng "Chun-Hung Tzeng"), [Paul W. Purdom](Paul_W._Purdom "Paul W. Purdom") (**1983**). *[A Theory of Game Trees](https://www.aaai.org/Library/AAAI/1983/aaai83-080.php)*. [AAAI-83](Conferences#AAAI-83 "Conferences")
* [Andrew N. Walker](Andy_Walker "Andy Walker") (**1984**). *Uniqueness in Game Trees*. [ICCA Journal, Vol. 7, No. 4](ICGA_Journal#7_4 "ICGA Journal")
* [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996**). *Exploiting Graph Properties of Game Trees.* [AAAI-96](Conferences#AAAI-96 "Conferences") » [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
* [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1998**). *[Game Tree Algorithms and Solution Trees](https://link.springer.com/chapter/10.1007/3-540-48957-6_12)*. [CG 1998](CG_1998 "CG 1998")
* [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom") (**2002**). *Treemaps for Search-Tree Visualization*. [7th Computer Olympiad Workshop](7th_Computer_Olympiad#Workshop "7th Computer Olympiad"), [pdf](https://www.remi-coulom.fr/Publications/CGOlympiad2002.pdf)
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir") (**2006**). *Tools for debugging large game trees*. [11th Game Programming Workshop](http://www.computer-shogi.org/gpw/gpw11_e.html), [Hakone](https://en.wikipedia.org/wiki/Hakone,_Kanagawa), [Japan](https://en.wikipedia.org/wiki/Japan) » [Debugging](Debugging "Debugging")
* [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir") (**2007**). *GTQL: A Query Language for Game Trees*. M.Sc. thesis, [Reykjavík University](https://en.wikipedia.org/wiki/Reykjav%C3%ADk_University)
* [Jónheiður Ísleifsdóttir](J%C3%B3nhei%C3%B0ur_%C3%8Dsleifsd%C3%B3ttir "Jónheiður Ísleifsdóttir"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"). (**2008**). *[GTQ: A Language and Tool for Game-Tree Analysis](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_20)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.ru.is/faculty/yngvi/pdf/IsleifsdottirB08.pdf)


## Forum Posts


* [Measuring closeness to a minimal tree](https://www.stmintz.com/ccc/index.php?id=291979) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [CCC](CCC "CCC"), April 06, 2003
* [how to print tree non-recursively](http://www.talkchess.com/forum/viewtopic.php?t=42588) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 24, 2012 » [Recursion](Recursion "Recursion"), [Iteration](Iteration "Iteration")
* [Probabilistic approach to optimize search tree](http://www.talkchess.com/forum/viewtopic.php?t=45264) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 22, 2012


## External Links


* [Tree (graph theory) from Wikipedia](https://en.wikipedia.org/wiki/Tree_%28graph_theory%29)
* [Tree (set theory) from Wikipedia](https://en.wikipedia.org/wiki/Tree_%28set_theory%29)
* [Tree (data structure) from Wikipedia](https://en.wikipedia.org/wiki/Tree_data_structure)
* [Tree decomposition from Wikipedia](https://en.wikipedia.org/wiki/Tree_decomposition)
* [Tree traversal from Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)
* [AVL tree from Wikipedia](https://en.wikipedia.org/wiki/AVL_tree) named after its inventors [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Evgenii Landis](Mathematician#Landis "Mathematician") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [Expectiminimax tree from Wikipedia](https://en.wikipedia.org/wiki/Expectiminimax_tree)
* [Dancing tree from Wikipedia](https://en.wikipedia.org/wiki/Dancing_trees)
* [Decision tree from Wikipedia](https://en.wikipedia.org/wiki/Decision_tree)
* [Red-black tree from Wikipedia](https://en.wikipedia.org/wiki/Red-Black_Tree)
* [Jan Garbarek Group](Category:Jan_Garbarek "Category:Jan Garbarek") - *Once I Dreamt A Tree Upside Down*, 37th international jazz festival in [Burghausen](https://en.wikipedia.org/wiki/Burghausen,_Alt%C3%B6tting), 22.03.06 [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 Jan Garbarek, [Manu Katché](https://en.wikipedia.org/wiki/Manu_Katch%C3%A9), [Rainer Brüninghaus](https://en.wikipedia.org/wiki/Rainer_Br%C3%BCninghaus), [Eberhard Weber](Category:Eberhard_Weber "Category:Eberhard Weber")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Gray Tree from Wikipedia](https://en.wikipedia.org/wiki/Gray_Tree)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Lecture notes for April 22, 1997 Alpha-Beta Search](http://www.ics.uci.edu/%7Eeppstein/180a/970422.html) by [David Eppstein](David_Eppstein "David Eppstein")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> see [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky") and [Evgenii Landis](Mathematician#Landis "Mathematician") (**1962**). *An algorithm for the organization of information*. [Proceedings of the USSR Academy of Sciences](https://en.wikipedia.org/wiki/Proceedings_of_the_USSR_Academy_of_Sciences) 146: 263–266. (Russian) English translation by Myron J. Ricci in Soviet Math. Doklady, 3:1259–1263, 1962

**[Up one Level](Search "Search")**







 
