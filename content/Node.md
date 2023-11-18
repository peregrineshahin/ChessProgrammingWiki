---
title: Node
---
**[Home](Home "Home") \* [Search](Search "Search") \* Node**

**Node**, ([vertex](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29))  

the fundamental unit in [graph theory](https://en.wikipedia.org/wiki/Graph_theory) and, applied to [computer science](https://en.wikipedia.org/wiki/Computer_science), basic unit to structure and link devices of a [network](https://en.wikipedia.org/wiki/Computer_network) as well as [data](Data "Data"), such as items of a [linked list](Linked_List "Linked List") or [tree structure](https://en.wikipedia.org/wiki/Tree_%28data_structure%29). This page is about the **node** of the [search tree](Search_Tree "Search Tree") in the game of chess, which represents the alternating white and black to move [positions](Chess_Position "Chess Position") and keeps its state dependent on the [tree traversal](https://en.wikipedia.org/wiki/Tree_traversal). Inside a [depth-first](Depth-First "Depth-First") search, nodes are usually counted at top of the [recursive](Recursion "Recursion") search routine, i.e. for the purpose to determine [nodes per second](Nodes_per_Second "Nodes per Second"). The [move](Moves "Moves") is the [directed edge](https://en.wikipedia.org/wiki/Directed_graph) which connects an ordered pair of nodes or positions.


Nodes are classified by their topological properties inside the search tree, and in context of [alpha-beta](Alpha-Beta "Alpha-Beta") and its enhancements, by their [type](Node_Types "Node Types") as expected in accordance to the [minimal tree](Search_Tree#MinimalGameTree "Search Tree") before searching this node, or as determined after searching the node. 



## Topology


* [Root Node](Root "Root") - depth = D
* [Leftmost Node](Leftmost_Node "Leftmost Node") - are always PV-nodes <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [Sibling Node](Sibling_Node "Sibling Node")
* [Interior Node](Interior_Node "Interior Node")
* [Leaf Node](Leaf_Node "Leaf Node")
* [Terminal Node](Terminal_Node "Terminal Node")


## Depth
<table class="wikitable">

<tbody><tr>
<th> Name
</th>
<th> Heinz
</th>
<th> Hyatt
</th>
<th> Ambiguity
</th></tr>
<tr>
<td>  <a href="/Horizon_Node" title="Horizon Node">Horizon Node</a>
</td>
<td style="text-align:right;"> 0
</td>
<td style="text-align:right;"> -
</td>
<td style="text-align:center;"> *
</td></tr>
<tr>
<td>  <a href="/Frontier_Nodes" title="Frontier Nodes">Frontier Node</a>
</td>
<td style="text-align:right;"> 1
</td>
<td style="text-align:right;"> 0
</td>
<td style="text-align:center;"> *
</td></tr>
<tr>
<td>  <a href="/Pre_Frontier_Node" title="Pre Frontier Node">Pre Frontier Node</a>
</td>
<td style="text-align:right;"> 2
</td>
<td style="text-align:right;"> 1
</td>
<td style="text-align:center;"> *
</td></tr>
<tr>
<td>  <a href="/Quiescent_Node" title="Quiescent Node">Quiescent Node</a>
</td>
<td style="text-align:center;" colspan="2"> &lt;= 0
</td>
<td>
</td></tr></tbody></table>


* ) *There seems an ambiguity according to the definition of frontier versus horizon nodes.* <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> .


## See also


* [Chess Position](Chess_Position "Chess Position")
* [Nodes per Second](Nodes_per_Second "Nodes per Second")
* [Principal Variation](Principal_Variation "Principal Variation")
* [Score](Score "Score")


## Forum Posts


### 1995 ...


* [quiescent vs non-quiescent node counting](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/926eaf0869b6f176#) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 01, 1996
* [Node counting confusion](https://www.stmintz.com/ccc/index.php?id=14239) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), January 17, 1998
* [Bratko-Kopec Test - Node Counts](https://www.stmintz.com/ccc/index.php?id=20796) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), June 17, 1998 » [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")
* [nodes per ply](https://www.stmintz.com/ccc/index.php?id=55179) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 10, 1999


### 2000 ...


* [How to count the nodes?](https://www.stmintz.com/ccc/index.php?id=215421) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), February 25, 2002
* [ALL node definition](https://www.stmintz.com/ccc/index.php?id=285939)  by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 21, 2003
* [simple node definitions question](https://www.stmintz.com/ccc/index.php?id=387460) by Michael Henderson, [CCC](CCC "CCC"), September 13, 2004
* [To Jeroen and interested minds, re. Tiger node count](http://www.talkchess.com/forum/viewtopic.php?t=23037) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), August 15, 2008


### 2010 ...


* [Node counting](http://www.open-chess.org/viewtopic.php?f=5&t=1004) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2011 » [Rybka](Rybka "Rybka")
* [How do you count nodes?](http://www.talkchess.com/forum/viewtopic.php?t=40269) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), September 04, 2011
* [counting nodes vs counting evaluations](http://www.talkchess.com/forum/viewtopic.php?t=57033) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 19, 2015


### 2020 ...


* [Counting nodes correctly](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74399) by Steven Griffin, [CCC](CCC "CCC"), July 07, 2020


## External Links


* [Node from Wikipedia](https://en.wikipedia.org/wiki/Node)
* [Vertex (graph theory) from Wikipedia](https://en.wikipedia.org/wiki/Vertex_%28graph_theory%29)
* [Node (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Node_%28computer_science%29)
* [Node (networking) from Wikipedia](https://en.wikipedia.org/wiki/Node_%28networking%29)
* [Orbital node from Wikipedia](https://en.wikipedia.org/wiki/Orbital_node)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Dragon's Head and Tail](https://commons.wikimedia.org/wiki/File:Bonatti-caput_et_cauda_draconis.PNG) refer ascending and descending [Lunar nodes](https://en.wikipedia.org/wiki/Lunar_node), Image from [Guido Bonatti](https://en.wikipedia.org/wiki/Guido_Bonatti) (**1550**). *[Foroliviensis Mathematici De Astronomia Tractatvs X. : Vniuersum quod iudiciariam rationem Natiuitatum, Aeris, Tempestatum, attinet, comprehendentes. Adiectus est Cl. Ptolemaei liber Fructus, cum commentarijs vtilissimis Georgij Trapezunt](http://hardenberg.jalb.de/display_page.php?elementId=5363)*. pp. 119, from [Johannes a Lasco Bibliothek](https://de.wikipedia.org/wiki/Johannes_a_Lasco_Bibliothek) (JALB)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> That leftmost nodes are always PV-nodes, does not imply each PV-node is leftmost - since we have to deal with real search trees rather than minimal ones.
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: simple node definitions question](https://www.stmintz.com/ccc/index.php?id=387518) post by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 13, 2004
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[Extended Futility Pruning](http://people.csail.mit.edu/heinz/dt/node18.html).* [ICCA Journal, Vol. 21, No. 2](ICGA_Journal#21_2 "ICGA Journal"), pp. 75-83

**[Up one Level](Search "Search")**







 
