---
title: Texel
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Texel**



[ Texel dunes and [Eierland Lighthouse](https://en.wikipedia.org/wiki/Eierland_Lighthouse) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Texel**,  
 
a free [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") developed by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"). Texel, first released in March 2012, was basically a [C++11](Cpp "Cpp") port of Peter's [Java](Java "Java") engine [CuckooChess](CuckooChess "CuckooChess"), the name change inspired by [HMS Cuckoo](https://en.wikipedia.org/wiki/HMS_Cuckoo_%281806%29), which was wrecked on April 04, 1810 on the Haak Sands off the [Texel](https://en.wikipedia.org/wiki/Texel) at [Callantsoog](https://en.wikipedia.org/wiki/Callantsoog). 


Texel applies many of the standard methods for computer chess programs, such as [iterative deepening](Iterative_Deepening "Iterative Deepening"), [negascout](NegaScout "NegaScout"), [aspiration windows](Aspiration_Windows "Aspiration Windows"), [quiescence search](Quiescence_Search "Quiescence Search") with [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") pruning and [MVV/LVA](MVV-LVA "MVV-LVA") move ordering, [hash table](Transposition_Table "Transposition Table"), [history heuristic](History_Heuristic "History Heuristic"), [recursive null moves](Null_Move_Pruning "Null Move Pruning"), [futility pruning](Futility_Pruning "Futility Pruning"), [late move reductions](Late_Move_Reductions "Late Move Reductions"), [opening book](Opening_Book "Opening Book") and [magic bitboards](Magic_Bitboards "Magic Bitboards"). 



### Texel 1.00


Changes of unreleased Texel 1.00 compared to the development version of [CuckooChess](CuckooChess "CuckooChess"): 



* Ported from [Java](Java "Java") to [C++](Cpp "Cpp"). About twice as fast as a result)
* Added evaluation term to avoid walking into wrong corner in KRKB endings
* Implemented [reverse futility pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* Implemented [late move pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")






### Texel 1.01


First released version in March 2012 <a id="cite-note-2" href="#cite-ref-2">[2]</a> addressing following topics:



* Replaced cuckoo hashing with a more cache-friendly alternative
* Implemented [passed pawn race](Pawn_Race "Pawn Race") evaluation
* Increased [passed pawn](Passed_Pawn "Passed Pawn") bonus for pawns on rank 6 and 7






### Texel 1.02


Texel **1.02**, released in June 2013 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, had a number of mostly small changes, new evaluation features, and speed ups, such as only one check in [quiescence search](Quiescence_Search "Quiescence Search"), cache line aligned entries of the [transposition table](Transposition_Table "Transposition Table"), cache-optimized [magic bitboard](Magic_Bitboards "Magic Bitboards") constants, support for [SSE4.2](SSE4#SSE4.2 "SSE4") [PopCount](Population_Count "Population Count"), and reduced [aspiration windows](Aspiration_Windows "Aspiration Windows") with gradually widening after [fail-high](Fail-High "Fail-High")/[low](Fail-Low "Fail-Low") at the [root](Root "Root").




### Texel 1.03


Texel **1.03**, released in January 2014, was a huge improvement of about 100 Elo over Texel 1.02 using one core <a id="cite-note-4" href="#cite-ref-4">[4]</a>, mostly due to [automated tuning](Texel%27s_Tuning_Method "Texel's Tuning Method") of [evaluation](Evaluation "Evaluation") parameters <a id="cite-note-5" href="#cite-ref-5">[5]</a>. Further, beside other tweaks, Texel 1.03 incorporates a unique [recursive](Recursion "Recursion") [parallel search](Parallel_Search "Parallel Search") using [threads](Thread "Thread"), combining the power of [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting") with the simplicity of [ABDADA](ABDADA "ABDADA") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, and further applies [null move verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") and more aggressive [LMR](Late_Move_Reductions "Late Move Reductions"), but no longer uses the [Botvinnik-Markoff extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension").




### Texel 1.04


Texel **1.04** in May 2014 is about 70 elo stronger than Texel 1.03 on Peter's Linux computer at very fast time controls, using one core. Almost all changes are improvements in the evaluation function <a id="cite-note-7" href="#cite-ref-7">[7]</a>.




### Texel 1.05


 [](https://play.google.com/store/apps/details?id=org.petero.texelchessengine&hl=en) Texel 1.05 for [Android](Android "Android") <a id="cite-note-8" href="#cite-ref-8">[8]</a> 
Texel **1.05**, released in January 2015, is about 57 elo stronger than Texel 1.04 on Peter's Linux computer at very fast time controls. The most notable changes are support for [Gaviota](Gaviota_Tablebases "Gaviota Tablebases") and [Syzygy tablebases](Syzygy_Bases "Syzygy Bases") <a id="cite-note-9" href="#cite-ref-9">[9]</a>, [singular extensions](Singular_Extensions "Singular Extensions") , detection of 16 pawn [fortress positions](Fortress "Fortress"). and support for [multi-threaded](Thread "Thread") search on [Android](Android "Android") devices. Further improvements are due to more aggressive [LMR](Late_Move_Reductions "Late Move Reductions") , disabling of [LMP](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") in [PV nodes](Node_Types#pv-node "Node Types") <a id="cite-note-10" href="#cite-ref-10">[10]</a>, [check extensions](Check_Extensions "Check Extensions") for negative [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") moves only if the remaining depth is small, and [bonus for pieces protected by pawns](Connectivity "Connectivity") <a id="cite-note-11" href="#cite-ref-11">[11]</a>.




### Texel 1.06


Texel 1.06 was released in July 2016, and supports [polyglot](PolyGlot "PolyGlot") [opening books](Opening_Book "Opening Book"), and comes with many [search](Search "Search") and [evaluation](Evaluation "Evaluation") improvements, beside others, more aggressive [LMR](Late_Move_Reductions "Late Move Reductions") and [null move pruning](Null_Move_Pruning "Null Move Pruning"), maximum number of search [threads](Thread "Thread") up to 512, support for [Windows](Windows "Windows") [NUMA](NUMA "NUMA") systems having more than 64 cores, a small (512KB) per-thread [evaluation hash table](Evaluation_Hash_Table "Evaluation Hash Table"), and a 4-way [set associative](https://en.wikipedia.org/wiki/Set-associative#Associativity) [transposition table](Transposition_Table "Transposition Table"). Texel 1.06 is around 40-50 elo stronger than Texel 1.05 in self play at very fast time controls <a id="cite-note-12" href="#cite-ref-12">[12]</a>.




### Texel 1.07


On September 30, 2017, Texel 1.07 came with a new [parallel search](Parallel_Search "Parallel Search") based on [Lazy SMP](Lazy_SMP "Lazy SMP") <a id="cite-note-13" href="#cite-ref-13">[13]</a> and [ABDADA](ABDADA "ABDADA") <a id="cite-note-14" href="#cite-ref-14">[14]</a> able to use [computer clusters](https://en.wikipedia.org/wiki/Computer_cluster), and further supports [large pages](Memory#HugePages "Memory") in [Windows](Windows "Windows") <a id="cite-note-15" href="#cite-ref-15">[15]</a>.



## See also


* [CuckooChess](CuckooChess "CuckooChess")
* [Geography](Category:Geography "Category:Geography")
* [Lazy SMP - Lazy Cluster](Lazy_SMP#LazyCluster "Lazy SMP")
* [Mammal](Category:Mammal "Category:Mammal")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


## Forum Posts


### 2012 ...


* [New chess engine: Texel](http://www.talkchess.com/forum/viewtopic.php?t=42999) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), March 24, 2012
* [Elo versus speed](http://www.talkchess.com/forum/viewtopic.php?t=43134) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 02, 2012
* [Texel recipe to fix TT draws scores](http://www.talkchess.com/forum/viewtopic.php?t=44167) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 23, 2012 » [Path-Dependency](Path-Dependency "Path-Dependency"), [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")


**2013**



* [Texel 1.02](http://www.talkchess.com/forum/viewtopic.php?t=48228) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), June 08, 2013
* [Texel 1.02: First Impressions](http://www.talkchess.com/forum/viewtopic.php?t=48272) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), June 14, 2013
* [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 2013 » [Parallel Search](Parallel_Search "Parallel Search"), [Recursion](Recursion "Recursion")


**2014**



* [Texel 1.03](http://www.talkchess.com/forum/viewtopic.php?t=50964) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 19, 2014
* [Texel 1.03 gives good initial impression](http://www.talkchess.com/forum/viewtopic.php?t=50984) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), January 21, 2014
* [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [Texel 1.04](http://www.talkchess.com/forum/viewtopic.php?t=52470) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 29, 2014
* [LMP in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=54761) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 27, 2014 » [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (LMP), [PV-Node](Node_Types#pv-node "Node Types")


### 2015 ...


* [Texel 1.05](http://www.talkchess.com/forum/viewtopic.php?t=55058) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 24, 2015
* [History heuristic and fixed depth search](http://www.talkchess.com/forum/viewtopic.php?t=56372) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 16, 2015 » [History Heuristic](History_Heuristic "History Heuristic"), [Late Move Reduction Test Results](Late_Move_Reduction_Test_Results "Late Move Reduction Test Results")


**2016**



* [Texel 1.06](http://www.talkchess.com/forum/viewtopic.php?t=60774) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 10, 2016
* [How texel probes endgame tablebases](http://www.talkchess.com/forum/viewtopic.php?t=60833) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 16, 2016 » [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")


**2017**



* [NUMA Texel version](http://www.talkchess.com/forum/viewtopic.php?t=63582) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 29, 2017 » [NUMA](NUMA "NUMA")
* [Re: Is AlphaGo approach unsuitable to chess?](http://www.talkchess.com/forum/viewtopic.php?t=64096&start=12) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 31, 2017 » [AlphaGo](index.php?title=AlphaGo&action=edit&redlink=1 "AlphaGo (page does not exist)"), [Deep Learning](Deep_Learning "Deep Learning"), [Giraffe](Giraffe "Giraffe")
* [Lazy SMP and "lazy cluster" experiments](http://www.talkchess.com/forum/viewtopic.php?t=64824) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Lazy SMP - Lazy Cluster](Lazy_SMP#LazyCluster "Lazy SMP")


 [Approximate ABDADA](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=43) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 23, 2017 » [ABDADA](ABDADA "ABDADA")
* [Texel 1.07](http://www.talkchess.com/forum/viewtopic.php?t=65339) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), September 30, 2017


### 2020 ...


* [Re: Fast reverse move generation](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78913&start=1) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 18, 2021 » [Un-Move Generation](Move_Generation#Reverse "Move Generation")


## External Links


### Chess Engine


* [CuckooChess - A Java Chess Program - Texel: C++11 port](http://hem.bredband.net/petero2b/javachess/index.html)
* [Texel Chess Engine - Android Apps on Google Play](https://play.google.com/store/apps/details?id=org.petero.texelchessengine&hl=en)
* [Index of /chess/engines/Jim Ablett/TEXEL](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/TEXEL/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Texel](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Texel&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Texel


* [Texel from Wikipedia](https://en.wikipedia.org/wiki/Texel)
* [Texel - Wikipedia.nl](https://nl.wikipedia.org/wiki/Texel) (Dutch)
* [Texel (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Texel_%28disambiguation%29)
* [Texel (sheep) from Wikipedia](https://en.wikipedia.org/wiki/Texel_%28sheep%29)
* [Texel (graphics) from Wikipedia](https://en.wikipedia.org/wiki/Texel_%28graphics%29)
* [Focus](Category:Focus "Category:Focus") - Texel [Sarasani Festival](https://nl.wikipedia.org/wiki/Sarasani_(Texel)) 1971, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Beach on the island of Texel](https://en.wikipedia.org/wiki/File:Beach_Texel_Netherlands.jpg) by [Jean-Pierre Dagneaux](http://commons.wikimedia.org/wiki/User:Jpda), October 13, 2013, [Texel from Wikipedia](https://en.wikipedia.org/wiki/Texel)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [New chess engine: Texel](http://www.talkchess.com/forum/viewtopic.php?t=42999) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), March 24, 2012
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Texel 1.02](http://www.talkchess.com/forum/viewtopic.php?t=48228) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), June 08, 2013
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Texel 1.03](http://www.talkchess.com/forum/viewtopic.php?t=50964) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 19, 2014
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014
6. <a id="cite-ref-6" href="#cite-note-6">↑</a>  [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 2013
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Texel 1.04](http://www.talkchess.com/forum/viewtopic.php?t=52470) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), May 29, 2014
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Texel Chess Engine - Android Apps on Google Play](https://play.google.com/store/apps/details?id=org.petero.texelchessengine&hl=en)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [How texel probes endgame tablebases](http://www.talkchess.com/forum/viewtopic.php?t=60833) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 16, 2016
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [LMP in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=54761) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), December 27, 2014
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Texel 1.05](http://www.talkchess.com/forum/viewtopic.php?t=55058) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 24, 2015
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Texel 1.06](http://www.talkchess.com/forum/viewtopic.php?t=60774) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 10, 2016
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Lazy SMP and "lazy cluster" experiments](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=726656&t=64824) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Approximate ABDADA](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=728817&t=64824) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 23, 2017
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Texel 1.07](http://www.talkchess.com/forum/viewtopic.php?t=65339) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), September 30, 2017

**[Up one level](Engines "Engines")**







 
