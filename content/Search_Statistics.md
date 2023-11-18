---
title: Search Statistics
---
**[Home](Home "Home") \* [Engine Testing](Engine_Testing "Engine Testing") \* Search Statistics**


**Search statistics** refers to counting various appearances of interest inside the [search](Search "Search") or [evaluation](Evaluation "Evaluation") routines and to analyze their relationships to eventually spot [bugs](Engine_Testing#bugs "Engine Testing") or unfavorable conditions in [move ordering](Move_Ordering "Move Ordering").



### Cutoffs


Inside [Alpha-beta](Alpha-Beta "Alpha-Beta")- or [PV-search](Principal_Variation_Search "Principal Variation Search") it is of particular interest to count how often a node [failes high](Fail-High "Fail-High") or not, in relation to its [node types](Node_Types "Node Types"), that is expected [cut-Nodes](Node_Types#Cut-Nodes "Node Types") or expected [All-nodes](Node_Types#All-Nodes "Node Types"). If a fail-high occurs, it is illuminative to know whether the fail-high move it was tried first, early or late and what [move ordering](Move_Ordering "Move Ordering") classification like move from the [transposition table](Transposition_Table "Transposition Table"), [winning captures](Captures "Captures"), [killer moves](Killer_Move "Killer Move"), etc. was applied.



### Re-Searches


At [PV-nodes](Node_Types#PV-Node "Node Types") inside a [alpha-beta](Alpha-Beta "Alpha-Beta")- or [PV-search](Principal_Variation_Search "Principal Variation Search") the number of re-searches does concern, and how often a re-search does improve alpha (or even performs a cutoff) or not.



### Root Statistics


The [Root](Root "Root") as distinguished PV-node specially with [aspiration window](Aspiration_Windows "Aspiration Windows") often has its own statistics related to how much relative time (nodes) of the whole [iteration](Iteration "Iteration") is performed per each root-move, and how often another best move was found. In conjunction with static move properties, score graph by searched depth so far, etc., these statistic based informations may be considered in [time management](Time_Management "Time Management") to possibly decide about a new iteration.



### Selectivity


Counting the various [extensions](Extensions "Extensions"), [reductions](Reductions "Reductions") and [forward pruning](Pruning "Pruning") decisions in relation with [effective branching factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor") might also spot some deficiency inside the search.




## TT Statistics


Statistics of the [transposition table](Transposition_Table "Transposition Table") covers number of probes and stores, fill level, and number of probe hits, likely differentiated by sufficient [draft](Depth "Depth") and [type of stored node](Node_Types "Node Types").



## See also


* [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
* [Match Statistics](Match_Statistics "Match Statistics")


## Publications


* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1988**). *Useful Statistics from Tournament Programs*. [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal") » [Merlin](Merlin "Merlin")


## Forum Posts


### 1994 ...


* [COMPUTER CHESS: statistics](http://groups.google.com/group/rec.games.chess/browse_frm/thread/32af80f05abdc805) by [Deniz Yuret](Deniz_Yuret "Deniz Yuret"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 27, 1994
* [Cutoff Statistics](https://www.stmintz.com/ccc/index.php?id=13052) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), December, 18, 1997


### 2000 ...


* [A matter of statistics](https://www.stmintz.com/ccc/index.php?id=92156) by [Tijs van Dam](index.php?title=Tijs_van_Dam&action=edit&redlink=1 "Tijs van Dam (page does not exist)"), [CCC](CCC "CCC"), January 26, 2000
* [Re: The Scalable Search Test / Results of "Der Bringer"](https://www.stmintz.com/ccc/index.php?id=115020) by [Gerrit Reubold](Gerrit_Reubold "Gerrit Reubold"), [CCC](CCC "CCC"), June 18, 2000
* [Faster, deeper and more of such...](https://www.stmintz.com/ccc/index.php?id=129504) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 14, 2000 » [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [Hash table efficiency](https://www.stmintz.com/ccc/index.php?id=143022) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 05, 2000 » [Gaviota](Gaviota "Gaviota"), [Transposition Table](Transposition_Table "Transposition Table")
* [Hash table statistics](https://www.stmintz.com/ccc/index.php?id=359148) by [Andrew Wagner](index.php?title=Andrew_Wagner&action=edit&redlink=1 "Andrew Wagner (page does not exist)"), [CCC](CCC "CCC"), April 08, 2004
* [What is the Ideal Output for Understanding a Chess Engine?](http://www.talkchess.com/forum/viewtopic.php?t=20562) by Rick Fadden, [CCC](CCC "CCC"), April 07, 2008
* [Search statistics](http://www.talkchess.com/forum/viewtopic.php?t=27737) by henkf, [CCC](CCC "CCC"), May 04, 2009


### 2010 ...


* [make and unmake stadistics](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=42665) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), February 28, 2012
* [Probabilistic approach to optimize search tree](http://www.talkchess.com/forum/viewtopic.php?t=45264) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 22, 2012
* [Search statistics](http://www.talkchess.com/forum/viewtopic.php?t=49871) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), October 30, 2013
* [pruning statistics](http://www.talkchess.com/forum/viewtopic.php?t=51075) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 27, 2014 » [Pruning](Pruning "Pruning")
* [Best move statistics](http://www.talkchess.com/forum/viewtopic.php?t=61401) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 12, 2016
* [Move ordering statistics](http://www.talkchess.com/forum/viewtopic.php?t=63280) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), February 26, 2017 » [Move Ordering](Move_Ordering "Move Ordering")
* [Testing for Move Ordering Improvements](http://www.talkchess.com/forum/viewtopic.php?t=63555) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), March 25, 2017 » [Move Ordering](Move_Ordering "Move Ordering")
* [Komodo 11.2.2 - Initial position until depth 54](http://www.talkchess.com/forum/viewtopic.php?t=66335) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 15, 2018 » [Komodo](Komodo "Komodo"), [Initial Position](Initial_Position "Initial Position")
* [Stockfish 8 - Initial position until depth 59](http://www.talkchess.com/forum/viewtopic.php?t=66340) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 16, 2018 » [Stockfish](Stockfish "Stockfish")


**[Up one level](Engine_Testing "Engine Testing")**







 
