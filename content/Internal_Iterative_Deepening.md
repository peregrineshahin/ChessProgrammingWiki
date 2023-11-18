---
title: Internal Iterative Deepening
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Internal Iterative Deepening**



[ [Henry Moore](Category:Henry_Moore "Category:Henry Moore") - Mother and Child : Hood <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Internal Iterative Deepening (IID)**,  

used in [nodes](Node "Node") of the [search tree](Search_Tree "Search Tree") in a [iterative deepening](Iterative_Deepening "Iterative Deepening") [depth-first](Depth-First "Depth-First") [alpha-beta](Alpha-Beta "Alpha-Beta") framework, where a program has no [best move](Best_Move "Best Move") available from a previous search [PV](Principal_Variation "Principal Variation") or from the [transposition table](Transposition_Table "Transposition Table"). **IID** is used to find a good move to search first by searching the current position to a reduced depth, and using the best move of that search as the first move at the real depth. IID was already introduced by [John J. Scott](John_J._Scott "John J. Scott") in 1969 inside his program [Lancaster](Lancaster "Lancaster") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and further elaborated by [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") in 1991 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, as used in [Deep Thought](Deep_Thought "Deep Thought") with a reduction of 2 [plies](Ply "Ply") at [PV-nodes](Node_Types#pv-node "Node Types") and [cut-nodes](Node_Types#cut-nodes "Node Types") with no [best-move](Best_Move "Best Move") information from the transposition table. While it is pretty much a washout on average, Deep Though used this heuristic since it makes the search times more predictable by avoiding those isolated instances when the search time suddenly becomes 10 times larger than expected <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Conditions


Where to use IID is also an important question. Limiting the depth is an obvious condition (only use IID if depth > 5, say). Most only use IID in [PV-Nodes](Node_Types#pv-node "Node Types"), but it is also possible to use it at predicted [Cut-Nodes](Node_Types#cut-nodes "Node Types").



## Insurance


[Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") in a reply to [Stan Arts](Stan_Arts "Stan Arts") on the insurance aspect of IID, in a [CCC](CCC "CCC") discussion why IID does not work some programs like [Movei](Movei "Movei") and [RomiChess](RomiChess "RomiChess") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++
I completely agree. IID is like an insurance. Most of the time it was not needed, but then it also costs very little. And now and then it saves you big time.

```


```C++
Of course the lousier your basic move ordering, the more you benefit. But then it can be really spectacular, to the point where a program like [micro-Max](Micro-Max "Micro-Max") (which does have no move ordering at all, not even a move list, and can only search moves as it generates them) is able to compete with 'serious' engines. IID really works miracles there.

```


```C++
One thing still on my to-do list is to investigate if even more drastic IID would not even be better. I am thinking of situations where a previously best move in a [PV node](Node_Types#pv-node "Node Types") experiences a dramatic drop in [score](Score "Score") (or even any decrease in score) at high search depth. If that move has been best move for many [ID](Iterative_Deepening "Iterative Deepening") or IID iterations, you will know next to nothing about the other moves. They have always been scoring below [alpha](Alpha "Alpha"), all their hashed scores are [upper bounds](Upper_Bound "Upper Bound"), and in many cases the upper bounds are no longer usable. (With [hard fail](Fail-Hard "Fail-Hard") they would never be usable!) Disastrously poor moves might very well have the highest upper bounds. To prevent wasting lots of time on such a disastrous move at high search depth, it would make sense to start searching for moves that might beat the new alpha at small depth first, resetting the IID depth back to 1 in PV nodes each time the value of alpha after search of the previous best move drops compared to the previous iteration. 

```

## Publications


* [John J. Scott](John_J._Scott "John J. Scott") (**1969**). *A chess-playing program*. [Machine Intelligence 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html)
* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. 1.12 Internal iterative deepening, [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")


## See also


* [Double Null Move](Double_Null_Move "Double Null Move")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Multi–ProbCut](ProbCut#MPC "ProbCut")
* [Node Types](Node_Types "Node Types")


## Forum Posts


### 1998 ...


* [Internal Iterative Deepening](https://www.stmintz.com/ccc/index.php?id=24521) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), August 12, 1998


### 2000 ...


* [Crafty internal iterative deepening](https://www.stmintz.com/ccc/index.php?id=92088) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), January 26, 2000 » [Crafty](Crafty "Crafty")
* [MTD, IID, fail-low, root-research](https://www.stmintz.com/ccc/index.php?id=311269) by Juergen Wolf, [CCC](CCC "CCC"), August 14, 2003 » [MTD(f)](MTD(f) "MTD(f)"), [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")


### 2005 ...


* [Something obious on IID that not everybody does](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4456&p=23208) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 04, 2006
* [self deepening: an improved implementation of IID](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4698) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 24, 2006
* [Re: movei hash report](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=137538&t=15688) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 13, 2007 » [Movei](Movei "Movei")
* [Internal Iterative Deepening](http://www.talkchess.com/forum/viewtopic.php?t=23947) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), September 24, 2008
* [Null driven IID](http://www.talkchess.com/forum/viewtopic.php?t=25317) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), December 08, 2008


### 2010 ...


* [iid and singular extensions](http://www.talkchess.com/forum/viewtopic.php?t=35302) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), July 05, 2010 » [Singular Extensions](Singular_Extensions "Singular Extensions")
* [Trouble with IID](http://www.talkchess.com/forum/viewtopic.php?t=38140) by kenny stanley, [CCC](CCC "CCC"), February 20, 2011
* [On internal iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=38408) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno"), [Node Types](Node_Types "Node Types")
* [Internal Iterative Deepening questions](http://www.talkchess.com/forum/viewtopic.php?t=40484) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), September 21, 2011
* [Reductions from internal iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=44844) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), August 20, 2012 » [Reductions](Reductions "Reductions")
* [IID and move sorting](http://www.talkchess.com/forum/viewtopic.php?t=47951) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 09, 2013 » [ABDADA](ABDADA "ABDADA")
* [What do you use IID for](http://www.talkchess.com/forum/viewtopic.php?t=50419) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 10, 2013
* [IFD vs IID](http://www.talkchess.com/forum/viewtopic.php?t=51116) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 30, 2014
* [Internal Iterative Deepening Payoffs](http://www.open-chess.org/viewtopic.php?f=5&t=2585) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 01, 2014
* [Fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=51284) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2014 » [Fail-Soft](Fail-Soft "Fail-Soft"), [Fail-Hard](Fail-Hard "Fail-Hard"), [Fail-Low](Fail-Low "Fail-Low")


### 2015 ...


* [Hash Refutation](http://www.talkchess.com/forum/viewtopic.php?t=57374) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), August 24, 2015 » [Schooner](Schooner "Schooner")
* [Mate scores from IID](http://www.talkchess.com/forum/viewtopic.php?t=61134) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), August 16, 2016 » [Mate Score](Checkmate#MateScore "Checkmate")
* [Value of IID](http://www.talkchess.com/forum/viewtopic.php?t=61229) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), August 25, 2016
* [improving iid](http://www.talkchess.com/forum/viewtopic.php?t=62737) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), January 06, 2017
* [(I)ID and PV dropout](http://www.talkchess.com/forum/viewtopic.php?t=64321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2017 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [Fail-Low](Fail-Low "Fail-Low"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [IID (skipped when in check and Score greater than alpha)](http://www.talkchess.com/forum/viewtopic.php?t=64706) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), July 24, 2017


### 2020 ...


* [An alternative to IID](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74769) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 13, 2020 » [Reductions](Reductions "Reductions")


## External Links


* [µ-Max Search: Iterative Deepening](http://home.hccnet.nl/h.g.muller/deepen.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Henry Moore](Category:Henry_Moore "Category:Henry Moore") - [Mother and Child : Hood](https://atceramicsima.wordpress.com/2016/06/07/mother-and-child-hood-henry-moore-1983/), [St Paul's Cathedral](https://en.wikipedia.org/wiki/St_Paul%27s_Cathedral), [London](https://en.wikipedia.org/wiki/London), Image by James O'Gorman, April 08, 2015, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [John J. Scott](John_J._Scott "John J. Scott") (**1969**). *A chess-playing program*. [Machine Intelligence 4](http://www.doc.ic.ac.uk/~shm/MI/mi4.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. 1.12 Internal iterative deepening, [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [John J. Scott](John_J._Scott "John J. Scott") and [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") referred in [Omid David](Eli_David "Eli David"), [Moshe Koppel](Moshe_Koppel "Moshe Koppel"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2010**). *Genetic Algorithms for Automatic Search Tuning*. [ICGA Journal, Vol. 33, No. 2](ICGA_Journal#33_2 "ICGA Journal"), pp. 67--79
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: movei hash report](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=137538&t=15688) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 13, 2007

**[Up one level](Move_Ordering "Move Ordering")**







 
