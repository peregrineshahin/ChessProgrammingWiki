---
title: Node Types
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Node](Node "Node") \* Node Types**



 [](http://www.netlib.org/utk/lsi/pcwLSI/text/node351.html) Node Types <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Node Types** are classifications of [nodes](Node "Node") as expected inside a [minimal alpha-beta tree](Search_Tree#MinimalGameTree "Search Tree"), or as determined by the search. These types were first formulated by [Donald Knuth](Donald_Knuth "Donald Knuth") and Ronald Moore when describing the [alpha-beta algorithm](Alpha-Beta "Alpha-Beta") <a id="cite-note-2" href="#cite-ref-2">[2]</a> and further analyzed by [Judea Pearl](Judea_Pearl "Judea Pearl") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. While Knuth used the terms Type 1, 2, and 3, [Tony Marsland](Tony_Marsland "Tony Marsland") and [Fred Popowich](Fred_Popowich "Fred Popowich") introduced the more descriptive terms **PV-**, **Cut-** and **All-nodes** <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 


Node types as established by the search are stored inside the [transposition table](Transposition_Table "Transposition Table"), indicating whether the [score](Score "Score") is either [exact](Exact_Score "Exact Score"), [lower](Lower_Bound "Lower Bound") or [upper bounded](Upper_Bound "Upper Bound"). Expected node types, as determined by tree topology, probing the transposition table, or comparing scores of a [static evaluation](Evaluation "Evaluation") considering threats, or even a reduced search or [quiescence search](Quiescence_Search "Quiescence Search"), with the [bounds](Bound "Bound"), may be considered by various ([parallel](Parallel_Search "Parallel Search")) search algorithms and in decisions concerning [selectivity](Selectivity "Selectivity"). 






### Contents


* [1 PV-Nodes](#pv-nodes)
* [2 Cut-Nodes](#cut-nodes)
* [3 All-Nodes](#all-nodes)
* [4 Node Types in PVS](#node-types-in-pvs)
	+ [4.1 Onno](#onno)
	+ [4.2 Summary](#summary)
* [5 Number of Leaf Nodes](#number-of-leaf-nodes)
	+ [5.1 Formulas](#formulas)
	+ [5.2 Table](#table)
* [6 Quotes](#quotes)
* [7 See also](#see-also)
* [8 Selected Publications](#selected-publications)
* [9 Forum Posts](#forum-posts)
	+ [9.1 2000 ...](#2000-...)
	+ [9.2 2005 ...](#2005-...)
	+ [9.3 2010 ...](#2010-...)
	+ [9.4 2015 ...](#2015-...)
* [10 External Links](#external-links)
* [11 References](#references)






PV-nodes (Knuth's **Type 1**) are nodes that have a score that ends up being inside the [window](Window "Window"). So if the bounds passed are [a,b], with the score returned s, a<s<b. These nodes have all moves searched, and the value returned is [exact](Exact_Score "Exact Score") (i.e., not a [bound](Bound "Bound")), which propagates up to the [root](Root "Root") along with a [principal variation](Principal_Variation "Principal Variation").



* [Root Node](Root "Root") and the [Leftmost Nodes](Leftmost_Node "Leftmost Node") are always PV-nodes
* In [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), PV-nodes are defined by beta-alpha>1
* All [Siblings](Sibling_Node "Sibling Node") of a PV-node are expected Cut-nodes






## Cut-Nodes


Cut-nodes (Knuth's **Type 2**), otherwise known as [fail-high](Fail-High "Fail-High") nodes, are nodes in which a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") was performed. So with [bounds](Bound "Bound") [a,b], s>=b. A minimum of one move at a Cut-node needs to be searched. The score returned is a [lower bound](Lower_Bound "Lower Bound") (might be greater) on the [exact score](Exact_Score "Exact Score") of the node



* In [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") Cut-nodes are searched with [null windows](Null_Window "Null Window")
* The child of a Cut-node is an All-node
* The parent of a Cut-node is either a PV- or All-node
* The [ply](Ply "Ply") distance of a Cut-node to its PV-ancestor is odd






## All-Nodes


All-nodes (Knuth's **Type 3**), otherwise known as [fail-low](Fail-Low "Fail-Low") nodes, are nodes in which no move's score exceeded alpha. With [bounds](Bound "Bound") [a,b], s<=a. Every move at an All-node is searched, and the score returned is an [upper bound](Upper_Bound "Upper Bound"), the [exact score](Exact_Score "Exact Score") might be less.



* In [Principal Variation Search](Principal_Variation_Search "Principal Variation Search") All-nodes are searched with [null windows](Null_Window "Null Window")
* The children of an All-node are Cut-nodes
* The parent of an All-node is a Cut-node
* The [ply](Ply "Ply") distance of an All-node to its PV-ancestor is even


## Node Types in PVS


### Onno


[Onno](Onno "Onno") by [Onno Garms](Onno_Garms "Onno Garms") determines expected node types, beside other things, to perform [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") not only at PV-nodes but also at expected Cut-nodes. Onno Garms gave the following rules <a id="cite-note-6" href="#cite-ref-6">[6]</a>



* The root node is a PV-node
* The first child of a PV-node is a PV-node
* The further children are searched by a [scout search](Scout "Scout") as CUT-nodes
* [PVS](Principal_Variation_Search "Principal Variation Search") re-search is done as PV-node
* The first node of [bad pruning](Onno#Search "Onno") is a CUT-node
* The node after a [null move](Null_Move "Null Move") is a CUT-node
* The first node of [null move verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") is a CUT-node
* [Internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening") does not change the node type
* The first child of a CUT-node is an ALL-node
* Further children of a CUT-node are CUT-nodes
* Children of ALL-nodes are CUT-nodes


### Summary


Following summary was given by [Pradu Kannan](Pradu_Kannan "Pradu Kannan") similar to Onno's definition as an attempt to predict the node type before searching the node by assuming reasonably good [move ordering](Move_Ordering "Move Ordering") on PV-nodes and Cut-nodes <a id="cite-note-7" href="#cite-ref-7">[7]</a>:



* The root node is a PV-node
* The first child of a PV-node is a PV-node
* Children of PV-nodes that are searched with a zero-window [scout search](Scout "Scout") are Cut-nodes
* Children of PV-nodes that have to be re-searched because the scout search failed high, are PV-nodes
* The first child of a Cut-node, and other candidate cutoff moves (nullmove, killers, captures, checks, ...) is an All-node
* A Cut-node becomes an All-node once the first and all candidate cutoff moves are searched
* Children of All-nodes are Cut-nodes






## Number of Leaf Nodes


### Formulas


As emphasized by [Daniel Shawul](Daniel_Shawul "Daniel Shawul") <a id="cite-note-8" href="#cite-ref-8">[8]</a>, the formulas for the number of [leaf nodes](Leaf_Node "Leaf Node") of a certain Node type with uniform [depth](Depth "Depth") **n** and [branching factor](Branching_Factor "Branching Factor") **b**, using [floor and ceiling](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) of n/2 (cut the ceiling, all the floor) ...




```C++
PV  = 1
CUT = b⌈n/2⌉ - 1
ALL = b⌊n/2⌋ - 1

```

... are already the subexpressions ...




```C++
L = PV + CUT + ALL 

```

... in [Levin's](Michael_Levin "Michael Levin") famous formula demonstrating the [odd-even effect](Odd-Even_Effect "Odd-Even Effect") of [alpha-beta](Alpha-Beta "Alpha-Beta")




```C++
L = b⌈n/2⌉ + b⌊n/2⌋ - 1

```





### Table


Assuming a constant [branching factor](Branching_Factor "Branching Factor") of 40, this results in following number of leaves:





 [number of leaves with depth n and b = 40](Template:Number_of_Leaves "Template:Number of Leaves")
|  depth
 |  worst case
 |  best case
 |  PV
 |  CUT
 |  ALL
 |
|  n
 |  bn |  b⌈n/2⌉ + b⌊n/2⌋ - 1
 |  1
 |  b⌈n/2⌉ - 1
 |  b⌊n/2⌋ - 1
 |
|  0
 |  1
 |  1
 |  1
 |  0
 |  0
 |
|  1
 |  40
 |  40
 |  1
 |  39
 |  0
 |
|  2
 |  1,600
 |  79
 |  1
 |  39
 |  39
 |
|  3
 |  64,000
 |  1,639
 |  1
 |  1,599
 |  39
 |
|  4
 |  2,560,000
 |  3,199
 |  1
 |  1,599
 |  1,599
 |
|  5
 |  102,400,000
 |  65,569
 |  1
 |  63,999
 |  1,599
 |
|  6
 |  4,096,000,000
 |  127,999
 |  1
 |  63,999
 |  63,999
 |
|  7
 |  163,840,000,000
 |  2,623,999
 |  1
 |  2,559,999
 |  63,999
 |
|  8
 |  6,553,600,000,000
 |  5,119,999
 |  1
 |  2,559,999
 |  2,559,999
 |


## Quotes


[Robert Hyatt](Robert_Hyatt "Robert Hyatt") on the distinction between [ALL-](Node_Types#ALL "Node Types") and [CUT-nodes](Node_Types#CUT "Node Types") <a id="cite-note-9" href="#cite-ref-9">[9]</a>:




```C++
In [CB](Cray_Blitz "Cray Blitz"), I used this extensively, because you never want to split at a CUT node, and want to prefer an ALL node. [YBW](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") tries to recognize an ALL node by requiring that at least one move be searched before splitting, since > 90% of CUT nodes are discovered on the first move searched. But waiting on that first move introduces some wait time, and if you knew it was an ALL node from the get-go, you could split before the first move is completed. That was the basic premise behind the iterated search and [DTS algorithm](Dynamic_Tree_Splitting "Dynamic Tree Splitting") in Cray Blitz ... 

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Alpha-Beta Benchmark](Stephen_F._Wheeler#Alpha-Beta_Benchmark "Stephen F. Wheeler") by [Stephen F. Wheeler](Stephen_F._Wheeler "Stephen F. Wheeler")
* [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


## Selected Publications


* [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://www.informatik.uni-trier.de/~ley/pers/hd/m/Moore:Ronald_W=) (**1975**). *[An analysis of alpha-beta pruning](http://www.scribd.com/doc/28194932/An-Analysis-of-Alpha-Beta-Pruning).* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp 293–326. Reprinted in [Donald Knuth](Donald_Knuth "Donald Knuth") (**2000**). *[Selected Papers on Analysis of Algorithms](http://www-cs-faculty.stanford.edu/~uno/aa.html)*. [CSLI lecture notes series](http://web.stanford.edu/group/cslipublications/cslipublications/site/CSIN.shtml) 102, ISBN 1-57586-212-3
* [Igor Roizen](Igor_Roizen "Igor Roizen") (**1981**). *On the Average Number of Terminal Nodes examined by Alpha-Beta*. Technical Report UCLA-ENG-CSL-8108, [University of California at Los Angeles](https://en.wikipedia.org/wiki/University_of_California,_Los_Angeles), Cognitive Systems Laboratory
* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8, pp. 559-564
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Parallel Game-Tree Search.* [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 7, No. 4, pp. 442-452. [1984 pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/parallel.pdf) (Draft)
* [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf) » [Enhanced Forward Pruning](Enhanced_Forward_Pruning "Enhanced Forward Pruning")


## Forum Posts


### 2000 ...


* [ALL node definition](https://www.stmintz.com/ccc/index.php?id=285939) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), February 21, 2003
* [Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354012) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 11, 2004 » [Fruit](Fruit "Fruit"), [Transposition Table](Transposition_Table "Transposition Table"), [Principal Variation](Principal_Variation "Principal Variation"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")


 [Re: Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354016) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), March 11, 2004
* [Re: Attack table](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=171&start=143) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 22, 2004 » [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")


### 2005 ...


* [Move ordering at different (Knuth) node types](http://www.open-aurec.com/wbforum/viewtopic.php?t=4384) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 21, 2006 » [Move Ordering](Move_Ordering "Move Ordering")
* [PV based decisions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4710) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 27, 2006
* [NMP on ALL nodes](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6392) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 15, 2007 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Slight enhancement to PVS](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6558) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 10, 2007
* [Nodes type clarification](http://www.talkchess.com/forum/viewtopic.php?t=24198) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), October 05, 2008
* [Different handling of ALL / CUT nodes](http://www.talkchess.com/forum/viewtopic.php?t=27122) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), March 22, 2009


### 2010 ...


* [CUT" vs "ALL" nodes](http://www.talkchess.com/forum/viewtopic.php?t=38317) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), March 7, 2011
* [On internal iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=38408) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Onno](Onno "Onno")
* [When does a cut-node became an all-node?](http://www.talkchess.com/forum/viewtopic.php?t=43041) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), March 27, 2012
* [Question about PVS and nodes type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=48137) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), May 28, 2013 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [CUT/ALL nodes ratio](http://www.talkchess.com/forum/viewtopic.php?t=48205) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 06, 2013
* [LMR at CUT nodes can be arbitrarily bad!](http://www.talkchess.com/forum/viewtopic.php?t=48356) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), June 20, 2013 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions"), [Python](Python "Python")
* [Pruning in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=50907) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 14, 2014 » [Reductions](Reductions "Reductions"), [Root](Root "Root")
* [Node Types and Thoughts On Their Application](http://www.talkchess.com/forum/viewtopic.php?t=51422) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), February 26, 2014
* [Null move pruning on PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=53049) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), July 22, 2014 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [LMP in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=54761) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 27, 2014 » [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning"), [Texel](Texel "Texel")


### 2015 ...


* [Recognizing PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=59682) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 29, 2016
* [What is wrong with doing Nulls & ttcuts in a pv node ?](http://www.talkchess.com/forum/viewtopic.php?t=62890) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 21, 2017 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [PV-Nodes](Node_Types#PV "Node Types"), [Transposition Table](Transposition_Table "Transposition Table")
* [cut nodes](http://www.talkchess.com/forum/viewtopic.php?t=65477) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 18, 2017 » [Cut-Nodes](#cut)
* [Pruning at PV nodes?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69510) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), January 06, 2019 » [Pruning](Pruning "Pruning"), [PV-Nodes](#pv)


## External Links


* [Analysis of Alpha-Beta Pruning](http://www.netlib.org/utk/lsi/pcwLSI/text/node351.html) from the [Parallel Computing Works](http://www.netlib.org/utk/lsi/pcwLSI/text/BOOK.html) ebook


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Analysis of Alpha-Beta Pruning](http://www.netlib.org/utk/lsi/pcwLSI/text/node351.html) from the [Parallel Computing Works](http://www.netlib.org/utk/lsi/pcwLSI/text/BOOK.html) ebook
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Donald Knuth](Donald_Knuth "Donald Knuth"), [Ronald W. Moore](http://www.informatik.uni-trier.de/~ley/pers/hd/m/Moore:Ronald_W=) (**1975**). *[An analysis of alpha-beta pruning](http://www.scribd.com/doc/28194932/An-Analysis-of-Alpha-Beta-Pruning).* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 6, No. 4, pp 293–326. Reprinted in [Donald Knuth](Donald_Knuth "Donald Knuth") (**2000**). *[Selected Papers on Analysis of Algorithms](http://www-cs-faculty.stanford.edu/~uno/aa.html)*. [CSLI lecture notes series](http://web.stanford.edu/group/cslipublications/cslipublications/site/CSIN.shtml) 102, ISBN 1-57586-212-3
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8, pp. 559-564
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf") (**2003**). *Enhanced forward pruning.* [pdf](http://www.personeel.unimaas.nl/m-winands/documents/Enhanced%20forward%20pruning.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Parallel Game-Tree Search.* [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 7, No. 4, pp. 442-452. [1984 pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/parallel.pdf) (Draft)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: On internal iterative deeping](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=399511&t=38408) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 17, 2011
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: On internal iterative deeping](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=399059&t=38408) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), March 15, 2011
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [CUT/ALL nodes ratio](http://www.talkchess.com/forum/viewtopic.php?t=48205) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 06, 2013
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: "CUT" vs "ALL" nodes](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=398061&t=38317) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 08, 2011

**[Up one Level](Node "Node")**







 
