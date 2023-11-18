---
title: Young Brothers Wait Concept
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Parallel Search](Parallel_Search "Parallel Search") \* Young Brothers Wait Concept**



[ [Marx Brothers](https://en.wikipedia.org/wiki/Marx_Brothers) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Young Brothers Wait Concept**, (YBWC)  

a basic concept for a parallel [alpha-beta search](Alpha-Beta "Alpha-Beta") coined by [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") et al. in 1986 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, introduced 1989 to a wider audience in the [ICCA Journal](ICGA_Journal "ICGA Journal") paper *Distributed Game-Tree Search* <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Brothers are [sibling nodes](Sibling_Node "Sibling Node"), the oldest brother is searched first, younger brothers, to be searched in parallel, have to wait until the oldest brother did not yield in a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") and did possibly narrow the [bounds](Bound "Bound") in case of an alpha increase. 



### Distributed Game-Tree Search


In their introduction, Feldmann et al. mention approaches by several authors to decrease search overhead by various methods. The *mandatory-work-first* approach first evaluates that part of the game tree that must be searched and then evaluates the rest only if necessary <a id="cite-note-5" href="#cite-ref-5">[5]</a>. The [Principal Variation Splitting (PVS)](Parallel_Search#PrincipalVariationSplitting "Parallel Search") algorithm <a id="cite-note-6" href="#cite-ref-6">[6]</a> evaluates right sons of game-tree nodes with a [minimal window](Null_Window "Null Window") and re-evaluates them only if necessary. 


Alternatively, game-tree nodes are evaluated in parallel only if they had acquired an [alpha-beta bound](Bound "Bound") before <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Yet another approach applies in a distributed chess program running on a [hypercube](https://en.wikipedia.org/wiki/Hypercube) <a id="cite-note-8" href="#cite-ref-8">[8]</a>: if the [transposition table](Transposition_Table "Transposition Table") proposes some move for a game position, then this move is tried first. Parallel evaluation of the other moves is started only of the evaluation of the transposition move yields no cutoff.



### Critique


Their 1989 ICCA paper was criticized by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") <a id="cite-note-9" href="#cite-ref-9">[9]</a>, first on the speedup topic of about eleven on a 16-processor machine not mentioning that parallel speedup is tied to the (in)efficiency of the serial alpha-beta search, and further, on ignoring other work recently done in the field. The YBWC presented was similar to the methods used in the chess programs [Cray Blitz](Cray_Blitz "Cray Blitz") <a id="cite-note-10" href="#cite-ref-10">[10]</a>, [Lachex](Lachex "Lachex"), and [Para-Phoenix](Phoenix "Phoenix") <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a>. In a response, Feldmann et al. agreed that the behavior of a parallelization should be measured relative to the "best" sequential program. However, the speedup depends on many implementation details such as those about the hardware, communication mechanism, load-balancing capabilities, etc., which cannot be described in a short paper. The authors further state that chess programs were not the main research vehicle, but the algorithm, which was the reason for not quoting all the chess specific papers <a id="cite-note-13" href="#cite-ref-13">[13]</a>.



## Quotes


[Robert Hyatt](Robert_Hyatt "Robert Hyatt") on the distinction between [ALL-](Node_Types#all-nodes "Node Types") and [CUT-nodes](Node_Types#cut-nodes "Node Types") <a id="cite-note-14" href="#cite-ref-14">[14]</a>:




```
In [CB](Cray_Blitz "Cray Blitz"), I used this extensively, because you never want to split at a CUT node, and want to prefer an ALL node. YBW tries to recognize an ALL node by requiring that at least one move be searched before splitting, since > 90% of CUT nodes are discovered on the first move searched. But waiting on that first move introduces some wait time, and if you knew it was an ALL node from the get-go, you could split before the first move is completed. That was the basic premise behind the iterated search and [DTS algorithm](Dynamic_Tree_Splitting "Dynamic Tree Splitting") in Cray Blitz... 

```

## See also


* [ABDADA](ABDADA "ABDADA")
* [APHID](APHID "APHID")
* [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [Jamboree](Jamboree "Jamboree")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Node Types](Node_Types "Node Types")
* [Parallelism and Selectivity in Game Tree Search | Video](Tord_Romstad#Video "Tord Romstad"), Talk by [Tord Romstad](Tord_Romstad "Tord Romstad")
* [Zugzwang (Program)](Zugzwang_(Program) "Zugzwang (Program)")


## Publications


### 1986 ...


* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1986**). *A Local Area Network Used as a Parallel Architecture*. Technical Report 31, [Paderborn University](Paderborn_University "Paderborn University")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Comment on 'Distributed Game-Tree Search'* . [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")


### 1990 ...


* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1990**). *Response to a Comment on 'Distributed Game-Tree Search'* . [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") ('*1990**).*** **A Rejoinder to the Response to a Comment on 'Distributed Game-Tree Search**. [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1992**). *Experiments with a Fully Distributed Chess Program*. [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1992**). *Distributed Game Tree Search on a Massively Parallel System*. Data Structures and Efficient Algorithms, B. Monien, Th. Ottmann (eds.), Springer, Lecture Notes in Computer Science, 594, 1992, 270-288
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Phd-Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1994**). *Game-Tree Search on a Massively Parallel System*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1994**). *An Implementation of the Young Brothers Wait Concept*. Internal report, [University of Alberta](University_of_Alberta "University of Alberta")


### 2010 ...


* [Kai Himstedt](Kai_Himstedt "Kai Himstedt") (**2012**). *GridChess: Combining Optimistic Pondering with the Young Brothers Wait Concept*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal") » [GridChess](GridChess "GridChess"), [Pondering](Pondering "Pondering")


## Forum Posts


### 2009


* [YBWC details](http://www.talkchess.com/forum/viewtopic.php?t=31366) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), December 31, 2009


### 2010 ...


* [DTS-ification of YBWC](http://www.talkchess.com/forum/viewtopic.php?t=34633) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 01, 2010
* [YBWC: Active Reparenting](http://www.talkchess.com/forum/viewtopic.php?t=43243) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 10, 2012


### 2015 ...


* [SMP questions](http://www.talkchess.com/forum/viewtopic.php?t=55779) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), March 25, 2015
* [Actual speedups from YBWC and ABDADA on 8+ core machines?](http://www.talkchess.com/forum/viewtopic.php?t=56937) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 10, 2015 » [ABDADA](ABDADA "ABDADA")
* [Lazy SMP Better than YBWC?](http://www.talkchess.com/forum/viewtopic.php?t=58031) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), October 23, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [NUMA in a YBWC implementation](http://www.talkchess.com/forum/viewtopic.php?t=60875) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 20, 2016 » [NUMA](NUMA "NUMA")
* [Some hyperthreading results](http://www.talkchess.com/forum/viewtopic.php?t=61408) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 12, 2016 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Thread](Thread "Thread")
* [YBWC implementation questions](http://www.talkchess.com/forum/viewtopic.php?t=64993) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), August 26, 2017
* [More questions about threads](http://www.talkchess.com/forum/viewtopic.php?t=67186) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), April 21, 2018 » [Thread](Thread "Thread")


### 2020 ...


* [YBW engines past and present?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76184) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [CCC](CCC "CCC"), December 30, 2020 » YBW


## External Links


* [AG-Monien - Research - Game Trees](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/gametree.html) » [Burkhard Monien](Burkhard_Monien "Burkhard Monien")
* [Younger Brother (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Younger_Brother_%28disambiguation%29)
* [Big Brother (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Big_Brother)
* [Jan Garbarek Group](Category:Jan_Garbarek "Category:Jan Garbarek") - [Storebror og Lillebror](http://no.wikipedia.org/wiki/Storebror_og_Lillebror) / Conversation, [Festspillene](https://en.wikipedia.org/wiki/Bergen_International_Festival) in [Bergen](https://en.wikipedia.org/wiki/Bergen), Norway, May 25, 2002, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Jan Garbarek](Category:Jan_Garbarek "Category:Jan Garbarek"), [Rainer Brüninghaus](https://en.wikipedia.org/wiki/Rainer_Br%C3%BCninghaus), [Eberhard Weber](Category:Eberhard_Weber "Category:Eberhard Weber"), [Marilyn Mazur](Category:Marilyn_Mazur "Category:Marilyn Mazur")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The Marx Brothers, head-and-shoulders portrait, facing front. Top to bottom: [Chico](https://en.wikipedia.org/wiki/Chico_Marx), [Harpo](https://en.wikipedia.org/wiki/Harpo_Marx), [Groucho](https://en.wikipedia.org/wiki/Groucho_Marx) and [Zeppo](https://en.wikipedia.org/wiki/Zeppo_Marx) in 1931, [Marx Brothers from Wikipedia](https://en.wikipedia.org/wiki/Marx_Brothers)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1986**). *A Local Area Network Used as a Parallel Architecture*. Technical Report 31, [Paderborn University](Paderborn_University "Paderborn University")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal"), pp. 65-73
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal"), pp. 65-73
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Selim Akl](Selim_Akl "Selim Akl"), [David T. Barnard](http://umanitoba.ca/admin/president/bio.html), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.) (**1980**). *Simulation and Analysis in Deriving Time and Storage Requirements for a Parallel Alpha-Beta Pruning Algorithm*. IEEE International Conference on Parallel Processing, pp. 231-234
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Parallel Game-Tree Search.* [IEEE](IEEE "IEEE") Transactions on Pattern Analysis and Machine Intelligence, Vol. PAMI-7, No. 4, pp. 442-452. as 1984 [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/pami85.pdf) (Draft)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Chris Ferguson](https://en.wikipedia.org/wiki/Chris_Ferguson), [Richard Korf](Richard_Korf "Richard Korf") (**1988**). *Distributed Tree Search and its Application to Alpha-Beta Pruning.* Proceedings of AAAI-88, Vol. I, pp. 128-132. Saint Paul, MN, [pdf](http://www.aaai.org/Papers/AAAI/1988/AAAI88-023.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") (**1988**). *[Chess on a Hypercube](http://portal.acm.org/citation.cfm?id=63088)*. The Third Conference on Hypercube Concurrent Computers and Applications, Vol. II-Applications (ed. [G. Fox](http://portal.acm.org/author_page.cfm?id=81100501616&coll=GUIDE&dl=GUIDE&trk=0&CFID=90098691&CFTOKEN=72738297)), pp. 1329-1341
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Comment on `Distributed Game-Tree Search'.* [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal"), pp. 216-217
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *A High-Performance Parallel Algorithm to Search Depth-First Game Trees*. Ph.D. Thesis, Department of Computer Science, [University of Alabama at Birmingham](University_of_Alabama_at_Birmingham "University of Alabama at Birmingham")
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Improved Parallel Alpha-Beta Searching*. Proceedings ACM/IEEE Fall Joint Computer Conference, pp. 519-527.
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Distributed Game-Tree Searching*. Journal of Parallel and Distributed Computing, Vol. 6, No. 2, pp. 90-114. ISSN 0743-7315
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1990**). *Response to a Comment on 'Distributed Game-Tree Search'* . [ICCA Journal, Vol. 13, No. 1](ICGA_Journal#13_1 "ICGA Journal"), pp. 20-21
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Re: "CUT" vs "ALL" nodes](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=398061&t=38317) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 08, 2011

**[Up one level](Parallel_Search "Parallel Search")**







 
