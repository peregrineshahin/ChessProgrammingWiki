---
title: Principal VariationMultiPV
---
**[Home](Home "Home") \* [Search](Search "Search") \* Principal Variation**



 [](https://en.wikipedia.org/wiki/Variation_%28game_tree%29) Variation (game tree), PV of a [Minimax](Minimax "Minimax") tree in blue <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
The **Principal variation** (PV) is a [sequence of moves](Move_List "Move List") that programs consider [best](Best_Move "Best Move") and therefore expect to be played. All the [nodes](Node "Node") included by the PV are [PV-nodes](Node_Types#PV "Node Types"). Inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework, it is the most important [move ordering](Move_Ordering "Move Ordering") consideration to play the PV collected during the current [iteration](Iteration "Iteration"), as the very first left moves of the next iteration. Although not needed for pure chess playing, most engines print the Principal Variation every time it changes or a new depth is reached for analyzing purposes. There are several implementations to determine the PV - most notably the three mentioned below, which were often controversial discussed in [Computer Chess Forums](Computer_Chess_Forums "Computer Chess Forums") with all their pros and contras <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Contents


* [1 Transposition Table](#transposition-table)
* [2 Collection during search](#collection-during-search)
	+ [2.1 Triangular PV-Table](#triangular-pv-table)
	+ [2.2 PV-List on the Stack](#pv-list-on-the-stack)
* [3 Separate PV TT](#separate-pv-tt)
* [4 Multiple PVs](#multiple-pvs)
* [5 See also](#see-also)
* [6 Publications](#publications)
* [7 Forum Posts](#forum-posts)
	+ [7.1 1995 ...](#1995-...)
	+ [7.2 2000 ...](#2000-...)
	+ [7.3 2005 ...](#2005-...)
	+ [7.4 2010 ...](#2010-...)
	+ [7.5 2015 ...](#2015-...)
	+ [7.6 2020 ...](#2020-...)
* [8 External Links](#external-links)
* [9 References](#references)






The [best moves](Best_Move "Best Move") from the [exact](Exact_Score "Exact Score") entries of the [Transposition table](Transposition_Table "Transposition Table") may reveal the PV without (much) extra effort.



* **Pro**: implementation without extra effort
* **Contra**: dependent on the replacement scheme, TT-overwrites may shorten the PV






## Collection during search


PV-Tables (or [Refutation Tables](Refutation_Table "Refutation Table")) are used to collect and propagate [best moves](Best_Move "Best Move") and the PV up to the [root](Root "Root") similar to the best score.



* **Pro**: easy implementation; does not risk the cut PV lines in case of PV overwrites
* **Contra**: slows down search a little; PV might be cut in case of TT-cutoffs


### Triangular PV-Table


A [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table") is the most dense implementation of a pre-allocated PV-Table, taking into account that the farther the root the shorter the maximal PVs along the maximum search depth. The space advantage requires a more complicated index scheme though.




### PV-List on the Stack


A simple implementation with a linked PV-List on the [stack](Stack "Stack") is described on [Bruce Moreland](Bruce_Moreland "Bruce Moreland")'s Computer Chess Pages <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++

typedef struct LINE {
    int cmove;              // Number of moves in the line.
    MOVE argmove[moveMAX];  // The line.
}   LINE;

int AlphaBeta(int depth, int alpha, int beta, LINE * pline) {

    LINE line;
    if (depth == 0) {
        pline->cmove = 0;
        return Evaluate();
    }
    GenerateLegalMoves();
    while (MovesLeft()) {

        MakeNextMove();
        val = -AlphaBeta(depth - 1, -beta, -alpha, &line);
        UnmakeMove();

        if (val >= beta) return beta;
        if (val > alpha) {
            alpha = val;
            pline->argmove[0] = ThisMove();
            memcpy(pline->argmove + 1, line.argmove, line.cmove * sizeof(MOVE));
            pline->cmove = line.cmove + 1;
        }
    }
    return alpha;
}

```

LINE (a buffer that holds the PV) is created at the beginning of every node and a pointer to it is passed to every child nodes. If one of those raise [alpha](Alpha "Alpha") (become a new PV node) they copy their own PV - which is created in the same way as described now - into the pointer received from their parent node. Iteratively this returns the whole Principal Variation. Generally memcpy <a id="cite-note-5" href="#cite-ref-5">[5]</a> is an expensive instruction but as alpha is raised only very rarely this does not harm performance too much. The main downside is the allocation of the struct LINE every node which might be dangerous for deep searches with a small stack available.




## Separate PV TT


No matter how the PV is determined, the issue of short principal variations due to [exact score](Exact_Score "Exact Score") hits with sufficient draft from the [Transposition table](Transposition_Table "Transposition Table") at [PV-nodes](Node_Types#PV "Node Types") is one reason, why many programs ignore those matches and continue searching that node. Despite the search overhead seems tiny, since PV-nodes are rare, even more with exact hits, there are other solutions to address the short PV problem, which looses the information of the path that leads to that score, in conjunction with a more difficult [debugging](Debugging "Debugging") task.


Programs like [Glass](Glass "Glass") use a separate transposition table exclusively for PV-nodes - however similar results may be achieved with TT multi-tiers or bucket systems and replacement schemes taking care of exact scores of stored PV-nodes. [Robert Hyatt](Robert_Hyatt "Robert Hyatt") had the idea to take the 64 bit hash signature, squash it to something relatively small like 12-16 bits and use that as an index into a PV-holder table <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>. As an alternative, [Steven Edwards](Steven_Edwards "Steven Edwards") proposed a structure of [binary trees](https://en.wikipedia.org/wiki/Binary_tree) to recover the PV without any danger of overwriting causing a loss of information <a id="cite-note-10" href="#cite-ref-10">[10]</a>.



* **Pro**: almost always full length PV returned
* **Contra**: may slow down the search a little and has some space requirement






## Multiple PVs


Multiple PVs, that is collecting not only one PV of the best move and testing others don't improve [alpha](Alpha "Alpha"), but collecting and reporting multiple PVs of one or more next best moves for analyzing purposes, requires a less efficient [root](Root "Root") search, where subsequent moves are searched with a wider [alpha-beta window](Window "Window").



## See also


* [Best Move](Best_Move "Best Move")
* [Hash Move](Hash_Move "Hash Move")
* [Move List](Move_List "Move List")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [PV Extensions](PV_Extensions "PV Extensions")
* [PV-Move](PV-Move "PV-Move")
* [PV-Nodes](Node_Types#PV "Node Types")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")


## Publications


* [Selim Akl](Selim_Akl "Selim Akl"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *The Principal Continuation and the Killer Heuristic*. 1977 ACM Annual Conference Proceedings, pp. 466-473. ACM, Seattle, WA.
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *A Solution to Short PVs Caused by Exact Hash Matches*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal") » [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")


## Forum Posts


### 1995 ...


* [pv score oscillation](https://www.stmintz.com/ccc/index.php?id=10903) by [Willie Wood](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), October 18, 1997
* [Storing the PV in a search routine](https://www.stmintz.com/ccc/index.php?id=20265) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), June 09, 1998
* [PV verification heuristic](https://www.stmintz.com/ccc/index.php?id=74) by Peter Jacobi, [CCC](CCC "CCC"), July 05, 1998
* [Re: PV verification heuristic](https://www.stmintz.com/ccc/index.php?id=21808) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 06, 1998
* [Building the Principal Variation in MTD(f) searches](https://www.stmintz.com/ccc/index.php?id=60833) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), July 18, 1999 » [MTD(f)](MTD(f) "MTD(f)")


### 2000 ...


* [Getting a PV using MTD(f)](https://www.stmintz.com/ccc/index.php?id=95696) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), February 08, 2000 » [MTD(f)](MTD(f) "MTD(f)")
* [MTD(f) and PV](https://groups.google.com/d/msg/rec.games.chess.computer/Prqz2SzYuoc/4SkqqUYhrIsJ) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 09, 2000 » [MTD(f)](MTD(f) "MTD(f)")
* [PV update after retrieval from hash table](https://www.stmintz.com/ccc/index.php?id=142037) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), November 30, 2000
* [MTD(f) and the PV](https://groups.google.com/d/msg/rec.games.chess.computer/AEFIYBEvCFA/66YpNnmDYiUJ) by Adrian Jackson, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 16, 2001 » [MTD(f)](MTD(f) "MTD(f)")
* [Principal Variation](https://www.stmintz.com/ccc/index.php?id=203949) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), December 28, 2001
* [Problem with short PV](https://www.stmintz.com/ccc/index.php?id=207580) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), January 15, 2002
* [Where is Principal Variation?](https://www.stmintz.com/ccc/index.php?id=140514) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 22, 2000
* [calculating the PV using MTD](https://www.stmintz.com/ccc/index.php?id=251543) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), September 11, 2002 » [MTD(f)](MTD(f) "MTD(f)")
* [Returning PV from hash table](https://www.stmintz.com/ccc/index.php?id=277422) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), January 15, 2003
* [Fruit - Question for Fabien](https://www.stmintz.com/ccc/index.php?id=354012) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), March 11, 2004 » [Fruit](Fruit "Fruit"), [Node Types](Node_Types "Node Types"), [Transposition Table](Transposition_Table "Transposition Table"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [My fail soft reduces quality of collected PV. Help needed](https://www.stmintz.com/ccc/index.php?id=360837) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), April 20, 2004 » [Fail-Soft](Fail-Soft "Fail-Soft")
* [triangular pv vs. hash move pv](https://www.stmintz.com/ccc/index.php?id=387179) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 11, 2004


### 2005 ...


* [PV based decisions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4710) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 27, 2006
* [Thinker output](http://www.talkchess.com/forum/viewtopic.php?t=27113) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), March 22, 2009 » [Thinker](Thinker "Thinker")
* [Extracting PV from TT](http://www.talkchess.com/forum/viewtopic.php?t=29730) by Colin, [CCC](CCC "CCC"), September 12, 2009


### 2010 ...


* [About implementing MultiPV](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=34340) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), May 16, 2010 » [Multi-PV](#multipv)
* [Taken from CCC (Stockfish & mainlines)](http://www.open-chess.org/viewtopic.php?f=5&t=434) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2010
* [Full Principal Variation Retrieval](http://www.talkchess.com/forum/viewtopic.php?t=35982) by [Hieu Nguyen](index.php?title=Hieu_Nguyen&action=edit&redlink=1 "Hieu Nguyen (page does not exist)"), [CCC](CCC "CCC"), September 06, 2010


 [Re: Full Principal Variation Retrieval](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=369163&t=35982) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 07, 2010 » [Separate TT for the PV](Principal_Variation#SeparateTT "Principal Variation")
* [working!](http://www.talkchess.com/forum/viewtopic.php?t=36099) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 17, 2010 » [Separate TT for the PV](#separatett)
* [Root node search](http://www.talkchess.com/forum/viewtopic.php?t=38404) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno"), [Root](Root "Root")
* [An alternative means of PV recovery](http://www.talkchess.com/forum/viewtopic.php?t=38776) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 17, 2011
* [Hashing the PV](http://www.talkchess.com/forum/viewtopic.php?t=39289) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), June 06, 2011
* [UCI multipv question](http://www.talkchess.com/forum/viewtopic.php?t=39340) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), June 11, 2011  » [UCI](UCI "UCI")
* [About UCI multipv](http://www.talkchess.com/forum/viewtopic.php?t=42037) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), January 17, 2012 » [UCI](UCI "UCI")
* [Null move in PV](http://www.talkchess.com/forum/viewtopic.php?t=44487) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 18, 2012 » [Null Move](Null_Move "Null Move")
* [triangular pv](http://www.talkchess.com/forum/viewtopic.php?t=47573) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 22, 2013 » [PV Array in PVS](Triangular_PV-Table#PVinPVS "Triangular PV-Table")
* [Hash cutoffs and analysis](http://www.talkchess.com/forum/viewtopic.php?t=48315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2013 » [Transposition Table](Transposition_Table "Transposition Table")
* [Hashed PVs](http://www.talkchess.com/forum/viewtopic.php?t=49012) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), August 19, 2013
* [Stockfish search](http://www.talkchess.com/forum/viewtopic.php?t=49854) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 28, 2013 » [Stockfish](Stockfish "Stockfish")
* [TT with Null Move Cuts A PV Node/Line](http://www.talkchess.com/forum/viewtopic.php?t=51370) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), February 21, 2014 » [Transposition Table](Transposition_Table "Transposition Table"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), [PV-node](Node_Types#PV "Node Types")
* [Cache over-writing and PV's](http://www.talkchess.com/forum/viewtopic.php?t=54063) by Forrest Hoch, [CCC](CCC "CCC"), October 16, 2014 » [Transposition Table | Replacement Strategies](Transposition_Table#ReplacementStrategies "Transposition Table")
* [Stockfish and accurate PV](http://www.talkchess.com/forum/viewtopic.php?t=54750) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 25, 2014 » [Stockfish](Stockfish "Stockfish")


### 2015 ...


* [epd multipv](http://www.talkchess.com/forum/viewtopic.php?t=57108) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 28, 2015 » [Extended Position Description](Extended_Position_Description "Extended Position Description")
* [help me test multipv](http://www.talkchess.com/forum/viewtopic.php?t=60529) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), June 19, 2016
* [Collecting the pv in Search](http://www.talkchess.com/forum/viewtopic.php?t=60866) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), July 19, 2016
* [Implementing Multi pv](http://www.talkchess.com/forum/viewtopic.php?t=60971) by Charles Thomas, [CCC](CCC "CCC"), July 29, 2016
* [Collecting PVs of Qsearch ?](http://www.talkchess.com/forum/viewtopic.php?t=61796) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 22, 2016 » [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table"), [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Extracting Principal Variation during search](http://www.open-chess.org/viewtopic.php?f=5&t=3038) by Dabil, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2016
* [capturing PV in QSearch](http://www.open-chess.org/viewtopic.php?f=5&t=3072) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 20, 2017 » [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table"), [Quiescence Search](Quiescence_Search "Quiescence Search")
* [multi-pv analysis](http://www.talkchess.com/forum/viewtopic.php?t=63801) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), April 23, 2017 [Multi-PV](Principal_Variation#MultiPV "Principal Variation")
* [Collecting PV in a PVS search ?](http://www.talkchess.com/forum/viewtopic.php?t=64256) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 11, 2017 » [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")
* [Why PVs aren't displayed -- Robert Hourdart in TCEC chat](http://www.talkchess.com/forum/viewtopic.php?t=65874) by Thomas Ewers, [CCC](CCC "CCC"), December 01, 2017
* [Newbie's question about printing the PV](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68416) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), September 11, 2018
* [How to get the "usual" Multi PV with MCTS engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70788) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 21, 2019 » [MultiPV](Principal_Variation#MultiPV "Principal Variation"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Is there a standard in implementing MultiPV in regular engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71146) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 30, 2019 » [MultiPV](#multipv)


### 2020 ...


* [Why is MultiPV so slow?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72910) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson"), [CCC](CCC "CCC"), January 25, 2020 » [MultiPV](#multipv)
* [Principal Variation Search vs. Transposition Table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75549) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), October 26, 2020 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [Transposition Table](Transposition_Table "Transposition Table")


## External Links


* [Collecting the Principal Variation](http://web.archive.org/web/20040427013839/brucemo.com/compchess/programming/pv.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
* [Variation (game tree) from Wikipedia](https://en.wikipedia.org/wiki/Variation_%28game_tree%29)
* [Indigo Jam Unit](Category:Indigo_Jam_Unit "Category:Indigo Jam Unit") - 2×2 PV, 2010, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Variation (game tree) from Wikipedia](https://en.wikipedia.org/wiki/Variation_%28game_tree%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [triangular pv vs. hash move pv](https://www.stmintz.com/ccc/index.php?id=387179) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 11, 2004
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Extracting PV from TT](http://www.talkchess.com/forum/viewtopic.php?t=29730) by Colin, [CCC](CCC "CCC"), September 12, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Collecting the Principal Variation](http://web.archive.org/web/20040427013839/brucemo.com/compchess/programming/pv.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [memcpy - C++ Reference](http://www.cplusplus.com/reference/clibrary/cstring/memcpy/)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Full Principal Variation Retrieval](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=369163&t=35982) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 07, 2010
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [working!](http://www.talkchess.com/forum/viewtopic.php?t=36099) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 17, 2010
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Hashing the PV](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=409570&t=39289) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 06, 2011
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a>  [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *A Solution to Short PVs Caused by Exact Hash Matches*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal")
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [An alternative means of PV recovery](http://talkchess.com/forum/viewtopic.php?topic_view=threads&t=38776) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 17, 2011

**[Up one Level](Search "Search")**







 
