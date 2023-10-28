---
title: Parallel Search
---
**[Home](Home "Home") \* [Search](Search "Search") \* Parallel Search**



 [](http://www.drdobbs.com/high-performance-computing/206903306) Parallel scalability [[1]](#cite_note-1) 
**Parallel Search**,   

also known as **Multithreaded Search** or [SMP](SMP "SMP") Search, is a way to increase [search](Search "Search") speed by using additional [processors](https://en.wikipedia.org/wiki/Central_Processing_Unit). This topic that has been gaining popularity recently with [multiprocessor](https://en.wikipedia.org/wiki/Multiprocessing) computers becoming widely available. Utilizing these additional processors is an interesting domain of research, as traversing a search tree is inherently serial. Several approaches have been devised, with the most popular today being [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") and [Shared Hash Table](Shared_Hash_Table "Shared Hash Table") aka [Lazy SMP](Lazy_SMP "Lazy SMP").


This page gives a brief summary of the different types. SMP algorithms are classified by their [scalability](https://en.wikipedia.org/wiki/Scalability) (trend in search speed as the number of processors becomes large) and their [speedup](https://en.wikipedia.org/wiki/Speedup) (change in time to complete a search). Typically, programmers use **scaling** to mean change in [nodes per second](Nodes_per_Second "Nodes per Second") (NPS) rates, and speedup to mean change in time to [depth](Depth "Depth"). Scaling and scalability are thus two different concepts.



### Contents


* [1 Distributed Search](#Distributed_Search)
* [2 Shared Hash Table](#Shared_Hash_Table)
	+ [2.1 Lazy SMP](#Lazy_SMP)
	+ [2.2 ABDADA](#ABDADA)
* [3 Parallel Alpha-Beta](#Parallel_Alpha-Beta)
	+ [3.1 Principal Variation Splitting (PVS)](#Principal_Variation_Splitting_.28PVS.29)
	+ [3.2 YBWC and Jamboree](#YBWC_and_Jamboree)
	+ [3.3 Dynamic Tree Splitting (DTS)](#Dynamic_Tree_Splitting_.28DTS.29)
* [4 Other Approaches](#Other_Approaches)
* [5 Taxonomy](#Taxonomy)
* [6 Other Considerations](#Other_Considerations)
	+ [6.1 Memory Design](#Memory_Design)
	+ [6.2 Semaphores](#Semaphores)
	+ [6.3 Threads vs. Processes](#Threads_vs._Processes)
* [7 Didactic Programs](#Didactic_Programs)
* [8 See also](#See_also)
* [9 Publications](#Publications)
	+ [9.1 1950 ...](#1950_...)
	+ [9.2 1970 ...](#1970_...)
	+ [9.3 1980 ...](#1980_...)
	+ [9.4 1985 ...](#1985_...)
	+ [9.5 1990 ...](#1990_...)
	+ [9.6 1995 ...](#1995_...)
	+ [9.7 2000 ...](#2000_...)
	+ [9.8 2005 ...](#2005_...)
	+ [9.9 2010 ...](#2010_...)
	+ [9.10 2015 ...](#2015_...)
* [10 Forum Posts](#Forum_Posts)
	+ [10.1 1995 ...](#1995_..._2)
	+ [10.2 2000 ...](#2000_..._2)
	+ [10.3 2005 ...](#2005_..._2)
	+ [10.4 2010 ...](#2010_..._2)
	+ [10.5 2015 ...](#2015_..._2)
	+ [10.6 2020 ...](#2020_...)
* [11 External Links](#External_Links)
	+ [11.1 Parallel Search](#Parallel_Search)
	+ [11.2 Parallel Computing](#Parallel_Computing)
	+ [11.3 Scalability](#Scalability)
	+ [11.4 Shared Memory](#Shared_Memory)
	+ [11.5 Cache](#Cache)
	+ [11.6 Concurrency and Synchronization](#Concurrency_and_Synchronization)
	+ [11.7 Misc](#Misc)
* [12 References](#References)






A subtype of [parallel algorithms](https://en.wikipedia.org/wiki/Parallel_algorithm), [distributed algorithms](https://en.wikipedia.org/wiki/Distributed_algorithms) are algorithms designed to work in [cluster computing](https://en.wikipedia.org/wiki/Cluster_computing) and [distributed computing](https://en.wikipedia.org/wiki/Distributed_computing) environments, where additional concerns beyond the scope of "classical" parallel algorithms need to be addressed. 



## Shared Hash Table


*see Home: [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")*


This technique is a very simple approach to [SMP](SMP "SMP"). The implementation requires little more than starting additional processors. Processors are simply fed the root position at the beginning of the search, and each searches the same tree with the only communication being the [transposition table](Transposition_Table "Transposition Table"). The gains come from the effect of nondeterminism. Each processor will finish the various subtrees in varying amounts of time, and as the search continues, these effects grow making the search trees diverge. The speedup is then based on how many nodes the main processor is able to skip from transposition table entries. Many programs used this if a "quick and dirty" approach to SMP is needed. It had the reputation of little speedup on a mere 2 processors, and to scale quite badly after this.




### Lazy SMP


*see Home: [Lazy SMP](Lazy_SMP "Lazy SMP")*


Recent improvements by [Daniel Homan](Daniel_Homan "Daniel Homan") [[2]](#cite_note-2) , [Martin Sedlak](Martin_Sedlak "Martin Sedlak") [[3]](#cite_note-3) and others on **Lazy** SMP indicate that the algorithm scales quite well up to 8 cores and beyond [[4]](#cite_note-4) .



### ABDADA


*see Home: [ABDADA](ABDADA "ABDADA")*


[ABDADA](ABDADA "ABDADA"), Alpha-Bêta Distribué avec Droit d'Aînesse (Distributed Alpha-Beta Search with Eldest Son Right) is a loosely synchronized, distributed search algorithm by [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") [[5]](#cite_note-5) . It is based on the [Shared Hash Table](Shared_Hash_Table "Shared Hash Table"), and adds the number of processors searching this node inside the hash-table entry for better utilization - considering the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept").




## Parallel Alpha-Beta


These algorithms divide the [Alpha-Beta](Alpha-Beta "Alpha-Beta") tree, giving different subtrees to different processors. Because alpha-beta is a serial algorithm, this approach is much more complex. However, these techniques also provide for the greatest gains from additional processors.




### Principal Variation Splitting (PVS)


In Principal Variation Splitting (PVS), each [node](Node "Node") is expressed by a [thread](Thread "Thread"). A thread will spawn one child thread for each legal move. But data dependency specified by the algorithm exists among these threads: After getting a tighter bound from the thread corresponding to the PV node, the remaining threads are ready to run.



 [](File:PVSplit.JPG) 
PV Splitting [[6]](#cite_note-6)



### YBWC and Jamboree


The idea in [Feldmann's](Rainer_Feldmann "Rainer Feldmann") [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") (YBWC) [[7]](#cite_note-7) [[8]](#cite_note-8) as well in [Kuszmaul's](Bradley_Kuszmaul "Bradley Kuszmaul") [Jamboree Search](Jamboree "Jamboree") [[9]](#cite_note-9) [[10]](#cite_note-10) [[11]](#cite_note-11) , is to search the first sibling node first before spawning the remaining siblings in parallel. This is based on the observations that the first move is either going to produce a cutoff (in which case processing sibling nodes is wasted effort) or return much better bounds. If the first move does not produce a cut-off, then the remaining moves are searched in parallel. This process is [recursive](Recursion "Recursion").


Since the number of processors is not infinite the process of "spawning" work normally consists in putting it on some kind of "work to be done stack" where processors are free to grab work in FIFO fashion when there is no work to do. In YBW you would not "spawn" or place work on the stack until the first sibling is searched.


In their 1983 paper *Improved Speedup Bounds for Parallel Alpha-Beta Search* [[12]](#cite_note-12) , [Raphael Finkel](Raphael_Finkel "Raphael Finkel") and [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") already gave the theoretical confirmation to the common sense wisdom that parallel resources should first be thrown into searching the first child. Assuming the tree is already in an approximation to best-first order, this establishes a good alpha value that can then be used to parallel search the later children. The algorithm in the 1982 Artificial Intelligence paper [[13]](#cite_note-13) , which Fishburn called the "dumb algorithm" in his 1981 thesis presentation [[14]](#cite_note-14) gives p^0.5 speedup with p processors, while the 1983 PAMI algorithm (the "smart algorithm") gives p^0.8 speedup for lookahead trees with the [branching factor](Branching_Factor "Branching Factor") of chess.



### Dynamic Tree Splitting (DTS)


*Home: [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")*


This algorithm, invented by the [Cray Blitz](Cray_Blitz "Cray Blitz") team (including [Robert Hyatt](Robert_Hyatt "Robert Hyatt") [[15]](#cite_note-15) ), is the most complex. Though this gives the best known scalability for any SMP algorithm, there are very few programs using it because of its difficulty of implementation.



## Other Approaches


Many different approaches have been tried that do not directly split the search tree. These algorithms have not enjoyed popular success due to the fact that they are not scalable. Typical examples include one processor that evaluates positions fed to it by a searching processor, or a tactical search that confirms or refutes a positional search.



* [APHID](APHID "APHID")
* [Optimistic Pondering](GridChess#OptimisticPondering "GridChess")
* [P-GPP](Shu_Yokoyama#PGPP "Shu Yokoyama")


## Taxonomy


Overview and taxonomy of parallel algorithms based on [alpha-beta](Alpha-Beta "Alpha-Beta"), given by [Mark Brockington](Mark_Brockington "Mark Brockington"), [ICCA Journal, Vol. 19: No. 3](ICGA_Journal#19_3 "ICGA Journal") in 1996 [[16]](#cite_note-16) [[17]](#cite_note-17)





|  FirstDescribed
 |  Algorithm
 |  Author(s)
 |  Processor Hierarchy / Control Distribution
 |  Parallelism PossibleAt These Nodes
 |  Synchronisation DoneAt These Nodes
 |
| --- | --- | --- | --- | --- | --- |
|  1978
 |  Parallel Aspiration Search
 | [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") |  Static/Centralized
 | [Root](Root "Root") ([αβ - Window](Window "Window"))
 |  Root
 |
|  1979
 |  Mandatory Work First
 | [Selim Akl](Selim_Akl "Selim Akl") et al.
 |  Static/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+
Leftmost child of 3 
 |  Bad [Type-2](Node_Types#CUT "Node Types") |
|  1980
 |  Tree Splitting
 | [Raphael Finkel](Raphael_Finkel "Raphael Finkel"),[John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") |  Static/Centralized
 |  Top k-ply
 | [Root](Root "Root") |
|  1981
 | [PVS](Parallel_Search#PrincipalVariationSplitting "Parallel Search") | [Tony Marsland](Tony_Marsland "Tony Marsland"),[Murray Campbell](Murray_Campbell "Murray Campbell") |  Static/Centralized
 | [Type-1](Node_Types#PV "Node Types") |  Type-1
 |
|  1983
 |  Key Node
 | [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") |  Static/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Leftmost child of 3
 |  Bad [Type-2](Node_Types#CUT "Node Types") |
|  1986
 |  UIDPABS [[18]](#cite_note-18) | [Monroe Newborn](Monroe_Newborn "Monroe Newborn") |  Static/Centralized
 | [Root](Root "Root") |  None
 |
|  1987
 |  DPVS
 | [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") |  Dynamic/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+[2](Node_Types#CUT "Node Types") | [Type 1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  EPVS
 | [Robert Hyatt](Robert_Hyatt "Robert Hyatt"),[Bruce W. Suter](Bruce_W._Suter "Bruce W. Suter"),[Harry Nelson](Harry_Nelson "Harry Nelson") |  Dynamic/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types") | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types") |
| [Waycool](Waycool "Waycool") | [Ed Felten](Ed_Felten "Ed Felten"),[Steve Otto](Steve_Otto "Steve Otto") |  Dynamic/Distributed
 |  All, except [Type-2](Node_Types#CUT "Node Types")with no [TT-Entry](Transposition_Table "Transposition Table") |  Nodes with TT & no [cutoff](Beta-Cutoff "Beta-Cutoff") |
| [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") | [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") | [Type-1](Node_Types#PV "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  1988
 | [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting") | [Robert Hyatt](Robert_Hyatt "Robert Hyatt") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") | [Type-1](Node_Types#PV "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  Bound-and-Branch
 | [Chris Ferguson](index.php?title=Chris_Ferguson&action=edit&redlink=1 "Chris Ferguson (page does not exist)"), [Richard Korf](Richard_Korf "Richard Korf") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") | [Type-1](Node_Types#PV "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  1990
 |  Delayed Branch Tree Expansion
 | [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") |  Static/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types") |  Bad [Type-2](Node_Types#CUT "Node Types") |
|  1993
 |  Frontier Splitting
 | [Paul Lu](Paul_Lu "Paul Lu") |  Dynamic/Distributed
 |  All
 | [Root](Root "Root") |
|  αβ\*
 | [Vincent David](Vincent_David "Vincent David") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types") | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  1994
 |  CABP [[19]](#cite_note-19) | [Van-Dat Cung](index.php?title=Van-Dat_Cung&action=edit&redlink=1 "Van-Dat Cung (page does not exist)") |  Static/Centralized
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types") |  Bad [Type-2](Node_Types#CUT "Node Types") |
| [Jamboree](Jamboree "Jamboree") | [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") | [Type-1](Node_Types#PV "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  1995
 | [ABDADA](ABDADA "ABDADA") | [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") |  Dynamic/Distributed
 | [Type-1](Node_Types#PV "Node Types")+[3](Node_Types#ALL "Node Types")+Bad [2](Node_Types#CUT "Node Types") | [Type-1](Node_Types#PV "Node Types")+Bad [2](Node_Types#CUT "Node Types") |
|  Dynamic Multiple PV-Split
 | [Tony Marsland](Tony_Marsland "Tony Marsland"), [Yaoqing Gao](index.php?title=Yaoqing_Gao&action=edit&redlink=1 "Yaoqing Gao (page does not exist)") |  Dynamic/Distributed
 |  Nodes within PV set
 |  Nodes within PV set
 |
|  1996
 | [APHID](APHID "APHID") | [Mark Brockington](Mark_Brockington "Mark Brockington"),[Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") |  Static/Centralized
 |  Top k-ply
 |  None
 |


## Other Considerations


### Memory Design


* [NUMA](NUMA "NUMA")
* [SMP](SMP "SMP")


### Semaphores


During an parallel search, certain areas of memory must be protected to make sure processors do not write simultaneously and corrupt the data. Some type of [semaphore](https://en.wikipedia.org/wiki/Semaphore_%28programming%29) system must be used. Semaphores access a piece of [shared memory](https://en.wikipedia.org/wiki/Shared_memory), typically an integer. When a processor wants to access protected memory, it reads the integer. If it is zero, meaning no other process is accessing the memory, then the processor attempts to make the integer nonzero. This whole process must be done atomically, meaning that the read, compare, and write are all done at the same time. Without this atomicity another processor could read the integer at the same time and both would see that they can freely access the memory.


In chess programs that use parallel alpha-beta, usually [spinlocks](https://en.wikipedia.org/wiki/Spinlock) are used. Because the semaphores are held for such short periods of time, processors want to waste as little time as possible after the semaphore is released before acquiring access. To do this, if the semaphore is held when a processor reaches it, the processor continuously reads the semaphore. This technique can waste a lot of processing time in applications with high contention, meaning that many processes try to access the same semaphore simultaneously. In chess programs, however, we want as much processing power as possible.


Spinlocks are sometimes implemented in [assembly language](Assembly "Assembly") because the operating system does not have an [API](https://en.wikipedia.org/wiki/Application_programming_interface) for them.




### Threads vs. Processes


There are two ways of utilizing the extra processing power of multiple CPUs, [threads](Thread "Thread") and [processes](Process "Process"). The difference between them is that threads share all memory in the program, but there are multiple threads of execution. In processes, all memory is local to each processor except memory that is explicitly shared. This means that in a threaded program, functions must pass around an extra argument specifying which thread is active, thus which board structure to use. When using processes, a single global board can be used that will be duplicated for each process.


Threads are more common, because they are easier to debug as well as implement, provided the program does not already have lots of global variables. Processes are favored by some because the need to explicitly share memory makes subtle bugs easier to avoid. Also, in processes, the extra argument to most functions is not needed.


Some programs that use threads:



* [Crafty](Crafty "Crafty") [[20]](#cite_note-20) [[21]](#cite_note-21)
* [Zappa](Zappa "Zappa")
* [Glaurung](Glaurung "Glaurung")
* Pretty much every other program...


Some programs that use processes:



* [Rybka](Rybka "Rybka")
* [Diep](Diep "Diep")
* [Deep Sjeng](Deep_Sjeng "Deep Sjeng")
* [ZCT](ZCT "ZCT")


## Didactic Programs


* [APIL chess](APIL_chess "APIL chess") by [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz")
* [Viper](Viper "Viper") by [Tord Romstad](Tord_Romstad "Tord Romstad")


## See also


* [Parallelism and Selectivity in Game Tree Search | Video](Tord_Romstad#Video "Tord Romstad"), Talk by [Tord Romstad](Tord_Romstad "Tord Romstad")
* [Cilk](Cilk "Cilk")
* [Diminishing Returns](Depth#DiminishingReturns "Depth")
* [GPU](GPU "GPU")
* [Iterative Search](Iterative_Search "Iterative Search")
* [Parallel Prefix Algorithms](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")


## Publications


### 1950 ...


* [Stanley Gill](https://en.wikipedia.org/wiki/Stanley_Gill) (**1958**). *[Parallel Programming](http://comjnl.oxfordjournals.org/content/1/1/2.abstract)*. [The Computer Journal, Vol. 1, No. 1](http://comjnl.oxfordjournals.org/content/1/1.toc)


### 1970 ...


* [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") (**1978**). *The Design and Analysis of Algorithms for Asynchronous Multiprocessors*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), advisor [Hsiang-Tsung Kung](Mathematician#Kung "Mathematician")


### 1980 ...


* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell"), A. L. Rivera (**1980**). *Parallel Search of Game Trees.* Technical Report TR 80-7, Computing Science Department, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR80-7.pdf)
* [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [Marvin Solomon](Marvin_Solomon "Marvin Solomon") (**1980**). *The Arachne Kernel.* Version 1.2 Technical Report 380, [University of Wisconsin-Madison](https://en.wikipedia.org/wiki/University_of_Wisconsin-Madison), [pdf](http://ftp.cs.wisc.edu/pub/techreports/1980/TR380.pdf)
* [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *Parallel Alpha-Beta Search on Arachne.* [IEEE](IEEE "IEEE") International Conference on Parallel Processing, pp. 235-243.
* [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet"), [Richard P. Brent](Mathematician#Brent "Mathematician"), [Hsiang-Tsung Kung](Mathematician#Kung "Mathematician") (**1980**). *[Parallel Execution of a Sequence of tasks on a Asynchronous Multiprocessor](http://wwwmaths.anu.edu.au/%7Ebrent/pub/pub058.html)*. Australian Computer Journal 12(3): 105-112, [pdf](http://wwwmaths.anu.edu.au/%7Ebrent/pd/rpb058i.pdf)
* [Selim Akl](Selim_Akl "Selim Akl"), [David T. Barnard](http://umanitoba.ca/admin/president/bio.html), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.), (**1980**). *Design, analysis and implementation of a parallel alpha-beta algorithm*, Department of Computing and Information Science, Queen's University, Kingston, Ontario.
* [Selim Akl](Selim_Akl "Selim Akl"), [David T. Barnard](http://umanitoba.ca/admin/president/bio.html), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.) (**1980**). *Simulation and Analysis in Deriving Time and Storage Requirements for a Parallel Alpha-Beta Pruning Algorithm*. [IEEE](IEEE "IEEE") International Conference on Parallel Processing, pp. 231-234.
* [Selim Akl](Selim_Akl "Selim Akl"), [David T. Barnard](http://umanitoba.ca/admin/president/bio.html), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.) (**1980**). *Searching game trees in parallel*, Proceedings of the Third Biennial Conference of the Canadian Society for Computational Studies of Intelligence, Victoria, B.C.


**1981**



* [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1981**). *Analysis of Speedup in Distributed Algorithms*. Ph.D. Thesis, [pdf](http://www.cs.wisc.edu/techreports/1981/TR431.pdf)
* [Selim Akl](Selim_Akl "Selim Akl"), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.) (**1981**). *A comparison of parallel implementations of the alpha-beta and Scout tree search algorithms using the game of checkers*, Department of Computing and Information Science, Queen's University, Kingston, Ontario.
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1981**). *Parallel Search of Strongly Ordered Game Trees*. Technical Report TR 81-9, Department of Computing Science , [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR81-9.pdf)


**1982**



* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1982**). *Parallel Search of Strongly Ordered Game Trees.* [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 14, No. 4, pp. 533-551. [pdf](http://www.cs.ualberta.ca/%7Etony/OldPapers/strong.pdf)
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1982**). *A Study of Parallel Tree Search Algorithms*. Technical Report TR 82-4, Computing Science Department, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR82-4.pdf)
* [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1982**). *Parallelism in Alpha-Beta Search*.[Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 19, No. 1
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), (**1982**). *OSTRICH/P - a parallel search chess program, SOCS-82.3,* [McGill University](McGill_University "McGill University"), School of Computer Science, Montreal.
* [Selim Akl](Selim_Akl "Selim Akl"), [David T. Barnard](http://umanitoba.ca/admin/president/bio.html), [R.J. Doran](http://research.cs.queensu.ca/TechReports/authorsD.html#Doran,%20R.J.) (**1982**). *Design, Analysis, and Implementation of a Parallel Tree Search Algorithm*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 4, No. 2, pp. 192-203. ISSN 0162-8828


**1983**



* [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *Improved Speedup Bounds for Parallel Alpha-Beta Search*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 5, No. 1, pp. 89 - 92
* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal") (**1983**). *[Searching, Merging, and Sorting in Parallel Computation](https://ieeexplore.ieee.org/document/1676138?arnumber=1676138)*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. C-32, No 10
 * [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") (**1983**). *The Key Node Method: A Highly-Parallel Alpha-Beta Algorithm*. Technical Report UUCCS 83-101, [University of Utah](https://en.wikipedia.org/wiki/University_of_Utah), [pdf](http://content.lib.utah.edu/utils/getfile/collection/uspace/id/3706/filename/image) 


**1984**



* [Lionel Moser](index.php?title=Lionel_Moser&action=edit&redlink=1 "Lionel Moser (page does not exist)") (**1984**). *An Experiment in Distributed Game Tree Searching*, M.Sc. thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo") [[22]](#cite_note-22) [[23]](#cite_note-23)


### 1985 ...


* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Parallel Game-Tree Search.* [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 7, No. 4,[1984 pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/parallel.pdf) (Draft)
* [Baruch Awerbuch](index.php?title=Baruch_Awerbuch&action=edit&redlink=1 "Baruch Awerbuch (page does not exist)") (**1985**). *[A New Distributed Depth-First Search Algorithm](http://www.sciencedirect.com/science/article/pii/0020019085900833)*. [Information Processing Letters](https://en.wikipedia.org/wiki/Information_Processing_Letters), Vol. 20, No. 3
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1985**). *A Parallel Search Chess Program*. Proceedings of the ACM Annual Conference, pp. 272-277. Denver, Co.
* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal"), [Alan Weiss](Mathematician#AWeiss "Mathematician") (**1985**). *Allocating Independent Subtasks on Parallel Processors*. [IEEE Transactions on Software Engineering](IEEE#SE "IEEE"), Vol. 11, No. 10
* [Daniel B. Leifker](http://www.informatik.uni-trier.de/~ley/pers/hd/l/Leifker:Daniel_B=.html), [Laveen N. Kanal](Laveen_Kanal "Laveen Kanal") (**1985**). *[A Hybrid SSS\*/Alpha-Beta Algorithm for Parallel Search of Game Trees](http://dl.acm.org/citation.cfm?id=1623687)*. [IJCAI'85](http://www.informatik.uni-trier.de/~ley/db/conf/ijcai/ijcai85.html#LeifkerK85) » [SSS\* and Dual\*](SSS*_and_Dual* "SSS* and Dual*")


**1986**



* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Marius Olafsson](Marius_Olafsson "Marius Olafsson"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Multiprocessor Tree-Search Experiments*. [Advances in Computer Chess 4](Advances_in_Computer_Chess_4 "Advances in Computer Chess 4")
* [Henri Bal](Henri_Bal "Henri Bal"), [Robbert van Renesse](Robbert_van_Renesse "Robbert van Renesse") (**1986**). *Parallel Alpha-Beta Search*. 4th NGI-SION Symposium Stimulerende Informatica. Jaarbeurs Utrecht, The Netherlands
* [Henri Bal](Henri_Bal "Henri Bal"), [Robbert van Renesse](Robbert_van_Renesse "Robbert van Renesse") (**1986**). *A Summary of Parallel Alpha-Beta Search Results*. [ICCA Journal, Vol 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1986**). *Improved Parallel Alpha-Beta Searching*. Proceedings ACM/IEEE Fall Joint Computer Conference, pp. 519-527.
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1986**). *A Local Area Network Used as a Parallel Architecture*. Technical Report 31, [Paderborn University](Paderborn_University "Paderborn University")


**1987**



* [Hiromoto Usui](http://www.onesource.com/free/Usui-Hiromoto/People/Profile/51361305-8), [Masafumi Yamashita](http://www.informatik.uni-trier.de/~ley/pers/hd/y/Yamashita:Masafumi.html), [Masaharu Imai](http://www.informatik.uni-trier.de/~ley/pers/hd/i/Imai:Masaharu.html), [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1987**). *Parallel Searches of Game Tree*. Systems and Computer in Japan, Vol. 18, No. 8, pp. 97-109.


**1988**



* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1988**). *Distributed Game-Tree Searching*. Journal of Parallel and Distributed Computing, Vol. 6, No. 2, pp. 90-114.
* [Chris Ferguson](https://en.wikipedia.org/wiki/Chris_Ferguson), [Richard Korf](Richard_Korf "Richard Korf") (**1988**). *Distributed Tree Search and its Application to Alpha-Beta Pruning.* Proceedings of AAAI-88, Vol. I, pp. 128-132. Saint Paul, MN, [pdf](http://www.aaai.org/Papers/AAAI/1988/AAAI88-023.pdf)
* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1988**). *Unsynchronized Iterative Deepening Parallel Alpha-Beta Search*. IEEE Transactions on Pattern Analysis and Machine Intelligence, PAMI, Vol. 10, No. 5, pp. 687-694. ISSN 0162-8828.
* [Ed Felten](Ed_Felten "Ed Felten"), [Steve Otto](Steve_Otto "Steve Otto") (**1988**). *[Chess on a Hypercube](https://authors.library.caltech.edu/71250/)*. The Third Conference on Hypercube Concurrent Computers and Applications, Vol. II-Applications
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1988**). *A High-Performance Parallel Algorithm to Search Depth-First Game Trees*. Ph.D. Thesis, Department of Computer Science, [University of Alabama at Birmingham](University_of_Alabama_at_Birmingham "University of Alabama at Birmingham")
* [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen") (**1988**). *Parallel Conspiracy-Number Search*. M.Sc. thesis, Faculty of Mathematics and Computer Science, [Vrije Universteit, Amsterdam](https://en.wikipedia.org/wiki/Vrije_Universiteit)
* [Matthew Huntbach](index.php?title=Matthew_Huntbach&action=edit&redlink=1 "Matthew Huntbach (page does not exist)"), [F. Warren Burton](index.php?title=F._Warren_Burton&action=edit&redlink=1 "F. Warren Burton (page does not exist)") (**1988**). *[Alpha-beta search on virtual tree machines](http://www.sciencedirect.com/science/article/pii/0020025588900540)*. [Information Sciences](http://www.journals.elsevier.com/information-sciences/), Vol. 44, No. 1


**1989**



* [Lynn Sutherland](index.php?title=Lynn_Sutherland&action=edit&redlink=1 "Lynn Sutherland (page does not exist)") (**1989**). *Load Balancing Search Problems on General-Purpose Multi-Computers*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal")
* [Henri Bal](Henri_Bal "Henri Bal") (**1989**). *[The shared data-object model as a paradigm for programming distributed systems](http://dare.ubvu.vu.nl/handle/1871/12760?mode=full&submit_simple=Show+full+item+record)*. Ph.D. thesis, [Vrije Universiteit](https://en.wikipedia.org/wiki/Vrije_Universiteit)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Bruce W. Suter](Bruce_W._Suter "Bruce W. Suter"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1989**). *A Parallel Alpha-Beta Tree Searching Algorithm*. Parallel Computing, Vol. 10, No. 3, pp. 299-308. ISSN 0167-8191.
* [Igor Steinberg](Igor_Steinberg "Igor Steinberg"), [Marvin Solomon](Marvin_Solomon "Marvin Solomon") (**1989**). *Searching Game Trees in Parallel*. Technical report 877, [pdf](ftp://ftp.cs.wisc.edu/pub/techreports/1989/TR877.pdf)
* [Richard Karp](Richard_Karp "Richard Karp"), [Yanjun Zhang](Yanjun_Zhang "Yanjun Zhang") (**1989**). *[On parallel evaluation of game trees](https://www.icsi.berkeley.edu/icsi/node/2253)*. [SPAA '89](https://dblp.uni-trier.de/db/conf/spaa/spaa89.html)
* [Yanjun Zhang](Yanjun_Zhang "Yanjun Zhang") (**1989**). *[Parallel Algorithms for Combinatorial Search Problems](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1989/5909.html)*. Ph.D. thesis, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), advisor [Richard Karp](Richard_Karp "Richard Karp")
* [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1989**). *Large Scale Parallelization of Alpha-beta Search: An Algorithmic and Architectural Study with Computer Chess*. Ph.D. thesis, Technical report CMU-CS-90-108, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), advisor [Hsiang-Tsung Kung](Mathematician#Kung "Mathematician")


### 1990 ...


* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**) *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal"), [Larry Rudolph](Mathematician#LRudolph "Mathematician"), [Marc Snir](Mathematician#MSnir "Mathematician") (**1990**). *[A Complexity Theory of Efficient Parallel Algorithms](https://www.sciencedirect.com/science/article/pii/030439759090192K)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 71
* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal"), [Larry Rudolph](Mathematician#LRudolph "Mathematician"), [Marc Snir](Mathematician#MSnir "Mathematician") (**1990**). *[Efficient Parallel Algorithms for Graph Problems](https://link.springer.com/article/10.1007/BF01840376)*. [Algorithmica](https://en.wikipedia.org/wiki/Algorithmica), Vol. 5, No. 1


**1992**



* [Jaleh Rezaie](Jaleh_Rezaie "Jaleh Rezaie"), [Raphael Finkel](Raphael_Finkel "Raphael Finkel") (**1992**). *[A comparison of some parallel game-tree search algorithms](https://www.researchgate.net/publication/2813087_A_comparison_of_some_parallel_game-tree_search_algorithms_Revised_version)*. [University of Kentucky](https://en.wikipedia.org/wiki/University_of_Kentucky)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1992**). *Experiments with a Fully Distributed Chess Program*. [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1992**). *Distributed Game Tree Search on a Massively Parallel System*. Data Structures and Efficient Algorithms, B. Monien, Th. Ottmann (eds.), Springer, Lecture Notes in Computer Science, 594, 1992, 270-288


**1993**



* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
* [Vincent David](Vincent_David "Vincent David") (**1993**). *[Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax](http://cat.inist.fr/?aModele=afficheN&cpsidt=161774)* = Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax, Ph.D. Thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse), [France](https://en.wikipedia.org/wiki/France)
* [Paul Lu](Paul_Lu "Paul Lu") (**1993**). *[Parallel Search of Narrow Game Trees](http://webdocs.cs.ualberta.ca/~paullu/MScThesis/thesis.html)*. M.Sc. Thesis, [University of Alberta](University_of_Alberta "University of Alberta")
* [Van-Dat Cung](index.php?title=Van-Dat_Cung&action=edit&redlink=1 "Van-Dat Cung (page does not exist)") (**1993**). *Parallelizations of Game-Tree Search*. [PARCO 1993](http://dblp.uni-trier.de/db/conf/parco/parco1993.html#Cung93), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.48.6959&rep=rep1&type=pdf) hosted by [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeer)


**1994**



* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html)*.
* [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Synchronized MIMD Computing*. Ph. D. Thesis, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/thesis-kuszmaul.pdf)
* [Christopher F. Joerg](Chris_Joerg "Chris Joerg"), [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
* [Van-Dat Cung](index.php?title=Van-Dat_Cung&action=edit&redlink=1 "Van-Dat Cung (page does not exist)") (**1994**). *Contribution à l'Algorithmique Non Numérique Parallèle : Exploration d'Espaces de Recherche*. Ph.D. thesis, [University of Paris VI](University_of_Paris "University of Paris")
* [Paolo Ciancarini](Paolo_Ciancarini "Paolo Ciancarini") (**1994**). *Distributed Searches: a Basis for Comparison.* [ICCA Journal, Vol. 17, No. 4](ICGA_Journal#17_4 "ICGA Journal"), [zipped postscript](ftp://ftp.cs.unibo.it/pub/cianca/iccaj2.ps.gz)
* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1994**). *An Implementation of the Young Brothers Wait Concept*. Internal report, [University of Alberta](University_of_Alberta "University of Alberta")
* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1994**). *Improvements to Parallel Alpha-Beta Algorithms*. Technical report, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta")


### 1995 ...


* [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1995**). *The StarTech Massively Parallel Chess Program*. [pdf](http://supertech.csail.mit.edu/papers/startech.pdf)
* [Henri Bal](Henri_Bal "Henri Bal"), [Victor Allis](Victor_Allis "Victor Allis") (**1995**). *Parallel Retrograde Analysis on a Distributed System*. Supercomputing ’95, San Diego, CA.
* [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1995**). *Programmes d'Échecs de Championnat: Architecture Logicielle Synthèse de Fonctions d'Évaluations, Parallélisme de Recherche*. Ph.D. Thesis. Université Paris 8, Saint-Denis, [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/phdJCW.ps.gz) (French)
* [Holger Hopp](Holger_Hopp "Holger Hopp"), [Peter Sanders](Peter_Sanders "Peter Sanders") (**1995**). *Parallel Game Tree Search on SIMD Machines*. [IRREGULAR 1995](http://www.informatik.uni-trier.de/~ley/db/conf/irregular/irregular95.html#HoppS95), from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.16.6343)
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Yaoqing Gao](index.php?title=Yaoqing_Gao&action=edit&redlink=1 "Yaoqing Gao (page does not exist)") (**1995**). *Speculative Parallelism Improves Search?* Technical Report 95-05, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.54.2187)


**1996**



* [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *The ABDADA Distributed Minimax Search Agorithm*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**) *Parallel Controlled Conspiracy-Number Search* - [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
* [Yaoqing Gao](index.php?title=Yaoqing_Gao&action=edit&redlink=1 "Yaoqing Gao (page does not exist)"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1996**). *Multithreaded Pruned Tree Search in Distributed Systems*. Journal of Computing and Information, 2(1), 482-492, [pdf](http://www.cs.ualberta.ca/%7Etony/RecentPapers/icci.pdf)
* [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), Edmonton, Alberta, Canada. as [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.8215)
* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1996**). *A Taxonomy of Parallel Game-Tree Search Algorithms*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19-3 "ICGA Journal")
* [Bernhard Balkenhol](Bernhard_Balkenhol "Bernhard Balkenhol") (**1996**). *Problems in Sequential and Parallel Game Tree Search*. [Bielefeld University](https://en.wikipedia.org/wiki/Bielefeld_University), [zipped ps](http://www.mathematik.uni-bielefeld.de/sfb343/preprints/pre97001.ps.gz)
* [Ming Li](http://www.informatik.uni-trier.de/~ley/pers/hd/l/Li:Ming.html), [John Tromp](John_Tromp "John Tromp"), [Paul M. B. Vitányi](Mathematician#PVitany "Mathematician") (**1996**). *How to Share Concurrent Wait-Free Variables*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 43, No. 4


**1997**



* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1997**). *[The Dynamic Tree-Splitting Parallel Search Algorithm](http://www.craftychess.com/hyatt/search.html)*, [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal")
* [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") (**1997**). *KnightCap — a parallel chess program on the AP1000+*. [zipped ps](ftp://us6.samba.org/pub/tridge/knightcap_pcw97.ps.gz) » [KnightCap](KnightCap "KnightCap")
* [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
* [David Sturgill](index.php?title=David_Sturgill&action=edit&redlink=1 "David Sturgill (page does not exist)"), [Alberto Maria Segre](Alberto_Maria_Segre "Alberto Maria Segre") (**1997**). *[Nagging: A Distributed, Adversarial Search-Pruning Technique Applied to First-Order Inference](http://www.springerlink.com/content/j11186905500t384/)*. [Journal of Automated Reasoning](https://en.wikipedia.org/wiki/Journal_of_Automated_Reasoning), Vol. 19, No. 3 [[24]](#cite_note-24)


**1998**



* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. Thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [zipped postscript](http://games.cs.ualberta.ca/articles/mgb_thesis.ps.gz)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1998**). *[Selective Game Tree Search on a Cray T3E](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/ABSTRACTS/FM_T3E.html)*. [ps](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/FM_T3E.ps.Z)
* [Craig S. Bruce](Craig_S._Bruce "Craig S. Bruce") (**1998**). *[Performance Optimization for Distributed-Shared-Data Systems](http://uwspace.uwaterloo.ca/handle/10012/300)*. Ph.D. thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo")


**1999**



* [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**1999**). *Using Cilk to Write Multiprocessor Chess Programs*, [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf)
* [Kevin Steele](index.php?title=Kevin_Steele&action=edit&redlink=1 "Kevin Steele (page does not exist)") (**1999**). *[Parallel Alpha-Beta Pruning of Game Decision Trees: A Chess Implementation](https://students.cs.byu.edu/~snell/Classes/CS584/projectsF99/steele/report.html)*. CS 584 Fall 1999 Semester Project Report, [Brigham Young University](https://en.wikipedia.org/wiki/Brigham_Young_University)
* [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1999**). *APHID: Asynchronous Parallel Game-Tree Search*. Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), Edmonton, Alberta, Canada. as [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.9870&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.33.9870)
* [John Romein](John_Romein "John Romein"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1999**). *Transposition Table Driven Work Scheduling in Distributed Search*. [AAAI-99](AAAI "AAAI"), [pdf](https://www.aaai.org/Papers/AAAI/1999/AAAI99-103.pdf) [[25]](#cite_note-25) [[26]](#cite_note-26)


### 2000 ...


* [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Dick Grune](Mathematician#DGrune "Mathematician") (**2000**). *The Multigame Reference Manual*. [Vrije Universiteit](https://en.wikipedia.org/wiki/Vrije_Universiteit), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=B2397A260C8166B1B31EC4779585EA5F?doi=10.1.1.32.1664&rep=rep1&type=pdf)


**2001**



* [John Romein](John_Romein "John Romein") (**2001**). *Multigame - An Environment for Distributed Game-Tree Search*. Ph.D. thesis, [Vrije Universiteit](https://en.wikipedia.org/wiki/Vrije_Universiteit), supervisor [Henri Bal](Henri_Bal "Henri Bal"), [pdf](http://dare.ubvu.vu.nl/bitstream/1871/11305/1/5429.pdf)
* [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**). *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. Masters Thesis, [pdf](http://www.top-5000.nl/ps/Parallel%20Alpha-Beta%20Search%20on%20Shared%20Memory%20Multiprocessors.pdf)
* [Florian Schintke](http://www.zib.de/schintke/), [Jens Simon](http://pc2.uni-paderborn.de/people/jens-simon/), [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**2001**). *A Cache Simulator for Shared Memory Systems*. International Conference on Computational Science ICCS 2001, San Francisco, CA, Springer LNCS 2074, vol. 2, pp. 569-578. [zipped ps](http://www.zib.de/reinefeld/Publications/ldasim-lncs.ps.gz)


**2002**



* [Yaron Shoham](index.php?title=Yaron_Shoham&action=edit&redlink=1 "Yaron Shoham (page does not exist)"), [Sivan Toledo](index.php?title=Sivan_Toledo&action=edit&redlink=1 "Sivan Toledo (page does not exist)") (**2002**). *[Parallel Randomized Best-First Minimax Search](https://www.sciencedirect.com/science/article/pii/S0004370202001959)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 137, Nos. 1-2
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"). (**2002**). *Distributed Game-Tree Search Using Transposition Table Driven Work Scheduling*, In Proc. of 31st International Conference on Parallel Processing (ICPP'02), pages 323-330, IEEE Computer Society Press. [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.132.8604&rep=rep1&type=pdf) via [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.132.8604)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"). (**2002**). *Transposition Table Driven Work Scheduling in Distributed Game-Tree Search* (Best Paper Prize), In Proc. of Fifteenth Canadian Conference on Artificial Intelligence (AI'2002), volume 2338 of Lecture Notes in Artificial Intelligence (LNAI), pages 56-68, [Springer](http://www.springerlink.com/content/47b3crn04egmmx8l/)
* [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf) » [Transposition Table](Transposition_Table "Transposition Table") [[27]](#cite_note-27)
* [Alberto Maria Segre](Alberto_Maria_Segre "Alberto Maria Segre"), [Sean Forman](index.php?title=Sean_Forman&action=edit&redlink=1 "Sean Forman (page does not exist)"), [Giovanni Resta](index.php?title=Giovanni_Resta&action=edit&redlink=1 "Giovanni Resta (page does not exist)"), [Andrew Wildenberg](index.php?title=Andrew_Wildenberg&action=edit&redlink=1 "Andrew Wildenberg (page does not exist)") (**2002**). *[Nagging: A Scalable Fault-Tolerant Paradigm for Distributed Search](https://www.sciencedirect.com/science/article/pii/S000437020200228X)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 140, Nos. 1-2


**2003**



* [Brian Greskamp](index.php?title=Brian_Greskamp&action=edit&redlink=1 "Brian Greskamp (page does not exist)") (**2003**). *Parallelizing a Simple Chess Program*. [pdf](http://iacoma.cs.uiuc.edu/~greskamp/pdfs/412.pdf)


**2004**



* [David Rasmussen](David_Rasmussen "David Rasmussen") (**2004**). *Parallel Chess Searching and Bitboards*. Masters Thesis, [postscript](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/3267/ps/imm3267.ps)


### 2005 ...


* [Jan Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen") (**2005**). *Transposition-Driven Scheduling in Parallel Two-Player State-Space Search*. Masters Thesis, [pdf](http://www.pds.ewi.tudelft.nl/%7Eepema/MSc-theses/MSc-thesis-Steenhuisen.pdf)


**2006**



* [Edward A. Lee](http://ptolemy.berkeley.edu/~eal/) (**2006**). *[The Problem with Threads](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.html)*. Technical Report No. UCB/EECS-2006-1, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), [pdf](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf)


**2007**



* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2007**). *The Method of the Chess Search Algorithms - Parallelization using Two-Processor distributed System*, [pdf](http://facta.junis.ni.ac.rs/mai/mai222/f22-2-175-188.pdf)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)") (**2007**). *On the Parallelization of UCT*. [CGW 2007](CGW_2007 "CGW 2007"), [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/parallelUCT.pdf) » [UCT](UCT "UCT")
* [Keijirou Yanagi](index.php?title=Keijirou_Yanagi&action=edit&redlink=1 "Keijirou Yanagi (page does not exist)"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2007**). *Multiple Parallel Search in Shogi*. [12th Game Programming Workshop](Conferences#GPW "Conferences")


**2008**



* [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Mark Winands](Mark_Winands "Mark Winands"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2008**). *[Parallel Monte-Carlo Tree Search](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_6)*. [CG 2008](CG_2008 "CG 2008"), [pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/multithreadedMCTS2.pdf)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)") (**2008**). *[A Parallel Monte-Carlo Tree Search Algorithm](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_7)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.lamsade.dauphine.fr/%7Ecazenave/papers/parallelMCTS.pdf)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Yann Kalemkarian](http://fr.linkedin.com/pub/yann-kalemkarian/7/7aa/716) (**2008**). *The Parallelization of Monte-Carlo Planning - Parallelization of MC-Planning*. ICINCO-ICSO 2008: 244-249, [pdf](http://hal.archives-ouvertes.fr/docs/00/28/78/67/PDF/icin08.pdf), [slides as pdf](http://www.lri.fr/~teytaud/UCTpara.pdf)
* [Kai Himstedt](Kai_Himstedt "Kai Himstedt"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Dietmar P. F. Möller](http://www.informatik.uni-hamburg.de/TIS/index.php) (**2008**). *A Twofold Distributed Game-Tree Search Approach Using Interconnected Clusters*. Euro-Par 2008: 587-598, [abstract](http://www.springerlink.com/content/2471845u5w6j1211/) from [springerlink](http://www.springerlink.com/home/main.mpx)
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)") (**2008**). *A Parallel Monte-Carlo Tree Search Algorithm*. [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/parallelMCTS.pdf)
* [James Swafford](James_Swafford "James Swafford") (**2008**). *[A Survey of Parallel Search Algorithms over Alpha-Beta Search Trees using Symmetric Multiprocessor Machines](https://fr.slideshare.net/JamesSwafford2/jfsmasters1)*. Masters Project, [East Carolina University](https://en.wikipedia.org/wiki/East_Carolina_University), advisor [Ronnie Smith](http://www.cs.ecu.edu/rws/)


**2009**



* [Markus Enzenberger](Markus_Enzenberger "Markus Enzenberger"), [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2009**). *A lock-free multithreaded Monte-Carlo tree search algorithm*, [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://webdocs.cs.ualberta.ca/~mmueller/ps/enzenberger-mueller-acg12.pdf)
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld") (**2009**). *Parallel Heuristic Search*. In: [C.A. Floudas](http://titan.princeton.edu/), [P.M. Pardalos](http://www.ise.ufl.edu/pardalos/) (eds.), [Encyclopedia of Optimization 2nd ed](http://www.springer.com/mathematics/book/978-0-387-74758-3). pp 2908-2912
* [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave"), [Nicolas Jouandeau](index.php?title=Nicolas_Jouandeau&action=edit&redlink=1 "Nicolas Jouandeau (page does not exist)") (**2009**). *Parallel Nested Monte-Carlo Search*. NIDISC 2009, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/parallelNested.pdf)
* T.M. Balajee, Adithya Udupa, Anil Kumar, D. Namratha (**2009**). *[Aggrandizement of Board Games’ Performance on Multi-core Systems: Taking GNU-Chess as a prototype](http://software.intel.com/en-us/articles/aggrandizement-of-board-games-performance-on-multi-core-systems-taking-gnu-chess-as-a-prototype/)*. [BMS College of Engineering](https://en.wikipedia.org/wiki/B.M.S._College_of_Engineering), Faculty mentor: Professor [Ashok Kumar](http://de.slideshare.net/ashokkumars75), [Intel® Developer Zone](http://software.intel.com/en-us) » [GNU Chess](GNU_Chess "GNU Chess")


### 2010 ...


* [Amine Bourki](index.php?title=Amine_Bourki&action=edit&redlink=1 "Amine Bourki (page does not exist)"), [Guillaume Chaslot](Guillaume_Chaslot "Guillaume Chaslot"), [Matthieu Coulm](index.php?title=Matthieu_Coulm&action=edit&redlink=1 "Matthieu Coulm (page does not exist)"), [Vincent Danjean](index.php?title=Vincent_Danjean&action=edit&redlink=1 "Vincent Danjean (page does not exist)"), [Hassen Doghmen](index.php?title=Hassen_Doghmen&action=edit&redlink=1 "Hassen Doghmen (page does not exist)"), [Thomas Hérault](index.php?title=Thomas_H%C3%A9rault&action=edit&redlink=1 "Thomas Hérault (page does not exist)"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Fabien Teytaud](Fabien_Teytaud "Fabien Teytaud"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Paul Vayssière](index.php?title=Paul_Vayssi%C3%A8re&action=edit&redlink=1 "Paul Vayssière (page does not exist)"), [Ziqin Yu](index.php?title=Ziqin_Yu&action=edit&redlink=1 "Ziqin Yu (page does not exist)") (**2010**). *[Scalability and Parallelization of Monte-Carlo Tree Search](http://hal.inria.fr/inria-00512854/en/)*. [CG 2010](CG_2010 "CG 2010"), [pdf](http://hal.inria.fr/docs/00/51/28/54/PDF/newcluster.pdf)
* [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2010**). *Parallel Alpha-Beta Based Game Tree Search*, slides as [pdf](http://www.iis.sinica.edu.tw/~tshsu/tcg2010/slides/slide13.pdf)
* [Dan Wu](index.php?title=Dan_Wu&action=edit&redlink=1 "Dan Wu (page does not exist)"), [Pan Chen](index.php?title=Pan_Chen&action=edit&redlink=1 "Pan Chen (page does not exist)"), [Kui Dai](index.php?title=Kui_Dai&action=edit&redlink=1 "Kui Dai (page does not exist)"), [Jinli Rao](index.php?title=Jinli_Rao&action=edit&redlink=1 "Jinli Rao (page does not exist)"), [Xuecheng Zou](index.php?title=Xuecheng_Zou&action=edit&redlink=1 "Xuecheng Zou (page does not exist)") (**2010**). *[Implementation of Parallel Game Tree Search on a SIMD System](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=5571732)*. [Huazhong University of Science & Technology](https://en.wikipedia.org/wiki/Huazhong_University_of_Science_and_Technology), [Wuhan](https://en.wikipedia.org/wiki/Wuhan), [China](https://en.wikipedia.org/wiki/People%27s_Republic_of_China), [ICIE 2010](http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=5570817), Vol. 1
* [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2010**). *Parallel Depth First Proof Number Search*. [AAAI 2010](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2010.html#Kaneko10) » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")


**2011**



* [Jean Méhat](Jean_M%C3%A9hat "Jean Méhat"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2011**). *A Parallel General Game Player*. [KI Journal](http://www.kuenstliche-intelligenz.de/), Vol. 25, No. 1, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/rootparallelggp.pdf)
* [Kazuki Yoshizoe](index.php?title=Kazuki_Yoshizoe&action=edit&redlink=1 "Kazuki Yoshizoe (page does not exist)"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Haruhiro Yoshimoto](index.php?title=Haruhiro_Yoshimoto&action=edit&redlink=1 "Haruhiro Yoshimoto (page does not exist)"), [Yutaka Ishikawa](index.php?title=Yutaka_Ishikawa&action=edit&redlink=1 "Yutaka Ishikawa (page does not exist)") (**2011**). *Scalable Distributed Monte Carlo Tree Search*. [SoCS2011](http://www.informatik.uni-trier.de/~ley/db/conf/socs/socs2011.html#YoshizoeKKYI11), [pdf](http://www.is.titech.ac.jp/~kishi/pdf_file/socs2011pmcts.pdf)
* [Ľubomír Lackovič](index.php?title=%C4%BDubom%C3%ADr_Lackovi%C4%8D&action=edit&redlink=1 "Ľubomír Lackovič (page does not exist)") (**2011**). *[Parallel Game Tree Search Using GPU](http://hgpu.org/?p=5772)*. Institute of Informatics and Software Engineering, [Faculty of Informatics and Information Technologies](https://en.wikipedia.org/wiki/Faculty_of_Informatics_and_Information_Technologies), [Slovak University of Technology in Bratislava](https://en.wikipedia.org/wiki/Slovak_University_of_Technology_in_Bratislava), [pdf](http://acmbulletin.fiit.stuba.sk/vol3num2/lackovic.pdf) » [GPU](GPU "GPU")
* [Khondker Shajadul Hasan](index.php?title=Khondker_Shajadul_Hasan&action=edit&redlink=1 "Khondker Shajadul Hasan (page does not exist)") (**2011**). *A Distributed Chess Playing Software System Model Using Dynamic CPU Availability Prediction*. [SERP 2011](http://www.world-academy-of-science.org/worldcomp11/ws), [pdf](http://world-comp.org/p2011/SER3956.pdf)
* [John Mellor-Crummey](http://www.cs.rice.edu/%7Ejohnmc/) (**2011**). *Shared-memory Parallel Programming with Cilk*. [Rice University](https://en.wikipedia.org/wiki/Rice_University), [slides as pdf](http://www.clear.rice.edu/comp422/lecture-notes/comp422-2011-Lecture4-Cilk.pdf) » [Cilk](Cilk "Cilk")
* [Lars Schaefers](index.php?title=Lars_Schaefers&action=edit&redlink=1 "Lars Schaefers (page does not exist)"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2011**). *UCT-Treesplit - Parallel MCTS on Distributed Memory*. MCTS Workshop, Freiburg, Germany, [pdf](http://www.cs.uni-paderborn.de/fileadmin/Informatik/AG-Platzner/People/Schaefers/TreesplitICAPS.pdf) » [UCT](UCT "UCT")
* [Tobias Graf](index.php?title=Tobias_Graf&action=edit&redlink=1 "Tobias Graf (page does not exist)"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)"), [Lars Schaefers](index.php?title=Lars_Schaefers&action=edit&redlink=1 "Lars Schaefers (page does not exist)") (**2011**). *Parallel Monte-Carlo Tree Search for HPC Systems*. [Euro-Par 2011](http://www.informatik.uni-trier.de/~ley/db/conf/europar/europar2011-2.html), [pdf](http://www.cs.uni-paderborn.de/fileadmin/Informatik/AG-Platzner/People/Schaefers/uctTreesplit.pdf)
* [Damjan Strnad](index.php?title=Damjan_Strnad&action=edit&redlink=1 "Damjan Strnad (page does not exist)"), [Nikola Guid](index.php?title=Nikola_Guid&action=edit&redlink=1 "Nikola Guid (page does not exist)") (**2011**). *[Parallel Alpha-Beta Algorithm on the GPU](http://cit.fer.hr/index.php/CIT/article/view/2029)*. [CIT. Journal of Computing and Information Technology](http://cit.fer.hr/index.php/CIT), Vol. 19, No. 4 » [GPU](GPU "GPU"), [Reversi](Othello "Othello")


**2012**



* [Chih-Hung Chen](Chih-Hung_Chen "Chih-Hung Chen"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin"), [Min-Huei Huang](index.php?title=Min-Huei_Huang&action=edit&redlink=1 "Min-Huei Huang (page does not exist)") (**2012**). *Volunteer Computing System Applied to Computer Games*. [TCGA 2012 Workshop](index.php?title=TCGA_2012&action=edit&redlink=1 "TCGA 2012 (page does not exist)"), [pdf](http://www.tcga.tw/tcgapaper/2012/P2.pdf)
* [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Peiyu Liu](index.php?title=Peiyu_Liu&action=edit&redlink=1 "Peiyu Liu (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)") (**2012**). *[A Node-based Parallel Game Tree Algorithm Using GPUs](http://ieeexplore.ieee.org/document/6337852/)*. CLUSTER 2012, [pdf](https://pdfs.semanticscholar.org/be21/d7b9b91957b700aab4ce002e6753b826ff54.pdf) » [GPU](GPU "GPU")


**2013**



* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Takeshi Ito](Takeshi_Ito "Takeshi Ito") (**2013**). *Parallel Dovetailing and its Application to Depth-First Proof-Number Search*. [ICGA Journal, Vol. 36, No. 1](ICGA_Journal#36_1 "ICGA Journal") » [Proof-Number Search](Proof-Number_Search "Proof-Number Search") [[28]](#cite_note-28)
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2013**). *Scalable Parallel DFPN Search*. [CG 2013](CG_2013 "CG 2013")
* [Georg Hager](https://www.rrze.fau.de/wir-ueber-uns/organigramm/mitarbeiter/index.shtml/georg-hager.shtml) [[29]](#cite_note-29), [Jan Treibig](http://dblp.uni-trier.de/pers/hd/t/Treibig:Jan), [Gerhard Wellein](http://dblp.uni-trier.de/pers/hd/w/Wellein:Gerhard) (**2013**). *The Practitioner's Cookbook for Good Parallel Performance on Multi- and Many-Core Systems*. [RRZE](https://de.wikipedia.org/wiki/Regionales_Rechenzentrum_Erlangen), [SC13](http://sc13.supercomputing.org/), [slides as pdf](https://blogs.fau.de/hager/files/2013/11/sc13_tutorial_134.pdf)


**2014**



* [Paul E. McKenney](https://plus.google.com/113202287320302059445/about) (**2014**). *[Is Parallel Programming Hard, And, If So, What Can You Do About It?](https://www.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html)*. [pdf](https://www.kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook-e1p.pdf)
* [Lars Schaefers](index.php?title=Lars_Schaefers&action=edit&redlink=1 "Lars Schaefers (page does not exist)") (**2014**). *Parallel Monte-Carlo Tree Search for HPC Systems and its Application to Computer Go*. Ph.D. thesis, [Paderborn University](Paderborn_University "Paderborn University"), advisors [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [pdf](http://www.althofer.de/phd-thesis-schaefers.pdf), [pdf](https://www.dropbox.com/s/x0lh7ky5lvj6c1y/PhdThesisSchaefers.pdf)
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2014**). *Performance analysis of a 240 thread tournament level MCTS Go program on the Intel Xeon Phi*. [CoRR abs/1409.4297](http://arxiv.org/abs/1409.4297)  » [Go](Go "Go"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [x86-64](X86-64 "X86-64")
* [Ting-Fu Liao](Ting-Fu_Liao "Ting-Fu Liao"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Guan-Wun Chen](Guan-Wun_Chen "Guan-Wun Chen"), [Chung-Chin Shih](index.php?title=Chung-Chin_Shih&action=edit&redlink=1 "Chung-Chin Shih (page does not exist)"), [Po-Ya Kang](index.php?title=Po-Ya_Kang&action=edit&redlink=1 "Po-Ya Kang (page does not exist)"), [Bing-Tsung Chiang](Bing-Tsung_Chiang "Bing-Tsung Chiang"), [Ting-Chu Ho](index.php?title=Ting-Chu_Ho&action=edit&redlink=1 "Ting-Chu Ho (page does not exist)"), [Ti-Rong Wu](Ti-Rong_Wu "Ti-Rong Wu") (**2014**). *A Study of Software Framework for Parallel Monte Carlo Tree Search*. [GPW-2014](Conferences#GPW19 "Conferences")


### 2015 ...


* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2015**). *Feature Strength and Parallelization of Sibling Conspiracy Number Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Shu Yokoyama](Shu_Yokoyama "Shu Yokoyama"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Tetsuro Tanaka](Tetsuro_Tanaka "Tetsuro Tanaka") (**2015**). *Parameter-Free Tree Style Pipeline in Asynchronous Parallel Game-Tree Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2015**). *Scaling Monte Carlo Tree Search on Intel Xeon Phi*. [CoRR abs/1507.04383](http://arxiv.org/abs/1507.04383) » [Hex](Hex "Hex"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [x86-64](X86-64 "X86-64")
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2015**). *Parallel Monte Carlo Tree Search from Multi-core to Many-core Processors*. [TrustCom/BigDataSE/ISPA 2015](https://whova.com/portal/ieeet_201508/), [pdf](https://askeplaat.files.wordpress.com/2013/01/ispa2015.pdf)
* [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Lung-Pin Chen](index.php?title=Lung-Pin_Chen&action=edit&redlink=1 "Lung-Pin Chen (page does not exist)") (**2015**). *Software Development Framework for Job-Level Algorithms*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
* [Akira Ura](Akira_Ura "Akira Ura"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka"), [Takashi Chikayama](Takashi_Chikayama "Takashi Chikayama") (**2015**). *[Dynamic Prediction of Minimal Trees in Large-Scale Parallel Game Tree Search](https://www.jstage.jst.go.jp/article/ipsjjip/23/1/23_9/_article)*. [Journal of Information Processing](https://www.jstage.jst.go.jp/browse/ipsjjip/), Vol. 23, No. 1
* [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)") (**2015**). *[A Parallel Algorithm for Game Tree Search Using GPGPU](http://ieeexplore.ieee.org/document/6868996/)*. [IEEE Transactions on Parallel and Distributed Systems](IEEE#TPDS "IEEE"), Vol. 26, No. 8 » [GPU](GPU "GPU")
* [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)"), [Chia-Hui Chang](Chia-Hui_Chang "Chia-Hui Chang") (**2015**). *[Job-Level Alpha-Beta Search](https://ir.nctu.edu.tw/handle/11536/124541)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 1
* [Lars Schaefers](index.php?title=Lars_Schaefers&action=edit&redlink=1 "Lars Schaefers (page does not exist)"), [Marco Platzner](index.php?title=Marco_Platzner&action=edit&redlink=1 "Marco Platzner (page does not exist)") (**2015**). *[Distributed Monte Carlo Tree Search: A Novel Technique and its Application to Computer Go](http://ieeexplore.ieee.org/document/6876158/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 4 [[30]](#cite_note-30)


**2016**



* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2016**). *A New Method for Parallel Monte Carlo Tree Search*. [arXiv:1605.04447](https://arxiv.org/abs/1605.04447) » [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2016**). *An Efficient Computation Pattern for Parallel MCTS*. [ICT.OPEN 2016](http://www.ictopen.nl/content/Previous+editions), [pdf](http://liacs.leidenuniv.nl/~plaata1/papers/ictopen2016.pdf)


**2017**



* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2017**). *Structured Parallel Programming for Monte Carlo Tree Search*. [arXiv:1704.00325](https://arxiv.org/abs/1704.00325)
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2017**). *An Analysis of Virtual Loss in Parallel MCTS*. [ICAART 2017](https://dblp.uni-trier.de/db/conf/icaart/icaart2017-2.html), Vol. 2, [pdf](http://liacs.leidenuniv.nl/~plaata1/papers/paper_ICAART17.pdf)


**2018**



* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2018**). *Pipeline Pattern for Parallel MCTS*. [ICAART 2018](https://dblp.uni-trier.de/db/conf/icaart/icaart2018-2.html), [pdf](http://liacs.leidenuniv.nl/~plaata1/papers/paper_ICAART18_pos.pdf)
* [S. Ali Mirsoleimani](S._Ali_Mirsoleimani "S. Ali Mirsoleimani"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jos Vermaseren](Jos_Vermaseren "Jos Vermaseren") (**2018**). *A Lock-free Algorithm for Parallel MCTS*. [ICAART 2018](https://dblp.uni-trier.de/db/conf/icaart/icaart2018-2.html), [pdf](http://liacs.leidenuniv.nl/~plaata1/papers/paper_ICAART18.pdf)


## Forum Posts


### 1995 ...


* [A parallel processing chess program for the 'Wintel' platform](https://groups.google.com/d/msg/rec.games.chess.computer/OUBw5LIIkoc/5VBOqmfdIrsJ) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 9, 1997 » [Psycho](Psycho "Psycho")
* [Parallel searching](https://groups.google.com/d/msg/rec.games.chess.computer/Wl7A-v-gWYQ/QLuvAp0l4_gJ) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 22, 1997 » [KnightCap](KnightCap "KnightCap")
* [Parallel Crafty](https://www.stmintz.com/ccc/index.php?id=15912) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 19, 1998  » [Crafty](Crafty "Crafty")
* [Current Crafty strength on SMP?](https://groups.google.com/d/msg/rec.games.chess.computer/C6z6Nnh2Nbs/G3LOexi_PMUJ) by Charlton Harrison, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 29, 1998
* [DIEP parallel in Paderborn - technical and detailed story](https://www.stmintz.com/ccc/index.php?id=58505) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), June 28, 1999 » [Diep](Diep "Diep"), [WCCC 1999](WCCC_1999 "WCCC 1999")
* [Parallel search](https://www.stmintz.com/ccc/index.php?id=63751) by [Brian McKinley](index.php?title=Brian_McKinley&action=edit&redlink=1 "Brian McKinley (page does not exist)"), [CCC](CCC "CCC"), August 06, 1999
* [Parallel search development on a single processor machine ?](https://www.stmintz.com/ccc/index.php?id=65490) by [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [CCC](CCC "CCC"), August 21, 1999
* [Dann's multiple cpu program](https://www.stmintz.com/ccc/index.php?id=77013) by Pete Galati, [CCC](CCC "CCC"), November 09, 1999 » [Dann Corbit](Dann_Corbit "Dann Corbit")


### 2000 ...


* [tip for "simulating" an MP computer & performance of ABDADA](https://www.stmintz.com/ccc/index.php?id=112849) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), May 28, 2000
* [Re: Atomic write of 64 bits](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/ab55c5d57a3a1fd1) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), September 25, 2000
* [Parallel algorithms in chess programming](https://www.stmintz.com/ccc/index.php?id=163888) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), April 16, 2001 » [ABDADA](ABDADA "ABDADA")
* [Parallel search algorithms](https://www.stmintz.com/ccc/index.php?id=186273) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), August 29, 2001
* [Chess over LAN revisited - APHID](https://www.stmintz.com/ccc/index.php?id=189126) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), September 17, 2001 » [APHID](APHID "APHID")
* [what's this "SMP time-to-ply measurement" ? (NT)](https://www.stmintz.com/ccc/index.php?id=249157) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 02, 2002
* [Re: Couple of chess programming questions - MDT and parallel](https://www.stmintz.com/ccc/index.php?id=251522) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), September 10, 2002 » [MTD(f)](MTD(f) "MTD(f)")
* [The Tobacco fields of my youth -- Parallel algorithms](https://www.stmintz.com/ccc/index.php?id=351419) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), February 26, 2004


### 2005 ...


* [Iterative DTS](http://www.talkchess.com/forum/viewtopic.php?t=14832) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), July 02, 2007
* [multithreading questions](http://www.talkchess.com/forum/viewtopic.php?t=15662) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), August 08, 2007
* [re-inventing the SMP wheel](http://www.talkchess.com/forum/viewtopic.php?t=15809) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 15, 2007
* [SMP thread goes here](http://www.talkchess.com/forum/viewtopic.php?t=16122) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 29, 2007
* [A Few General Questions on Parallel Search](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6767) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 31, 2007
* [interested in making single processor program multi](http://www.talkchess.com/forum/viewtopic.php?t=18611) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), December 28, 2007


**2008**



* [If making an SMP engine, do NOT use processes](http://www.talkchess.com/forum/viewtopic.php?t=19446) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), February 07, 2008
* [Questions about getting ready for multicore programming](http://www.talkchess.com/forum/viewtopic.php?t=20451) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), April 01, 2008
* [Minimizing Sharing of Data between Physical Processors](http://www.talkchess.com/forum/viewtopic.php?t=21233) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [CCC](CCC "CCC"), May 19, 2008
* [threads vs processes](http://www.talkchess.com/forum/viewtopic.php?t=22398) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 16, 2008
* [threads vs processes again](http://www.talkchess.com/forum/viewtopic.php?t=22799) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 05, 2008
* [Authors of WinBoard SMP engines, take note!](http://www.talkchess.com/forum/viewtopic.php?t=24327) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 11, 2008 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [Cluster Rybka](http://www.talkchess.com/forum/viewtopic.php?t=24807) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 10, 2008
* [UCI protocol and SMP](http://www.talkchess.com/forum/viewtopic.php?t=24866) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), November 13, 2008 » [UCI](UCI "UCI")


**2009**



* [SMP rating influence](http://www.talkchess.com/forum/viewtopic.php?t=25955) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 12, 2009
* [SMP and helpfull master concept](http://www.talkchess.com/forum/viewtopic.php?t=26057) by hcyrano, [CCC](CCC "CCC"), January 16, 2009
* [SMP hashing problem](http://www.talkchess.com/forum/viewtopic.php?t=26208) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 24, 2009 » [Lockless Hashing](Shared_Hash_Table#Lockless "Shared Hash Table")
* [SMP search stability](http://www.talkchess.com/forum/viewtopic.php?t=26211) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 24, 2009
* [nps scaling](http://www.talkchess.com/forum/viewtopic.php?t=26805) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 01, 2009
* [Clustering etc. thread](http://www.talkchess.com/forum/viewtopic.php?t=26945) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC") March 7, 2009


 [Results from UCT parallelization](http://talkchess.com/forum/viewtopic.php?p=254434) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), March 11, 2009
* [Questions on volatile keyword and memory barriers](http://www.talkchess.com/forum/viewtopic.php?t=29434) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [CCC](CCC "CCC"), August 16, 2009


### 2010 ...


* [asynchronous search](http://www.talkchess.com/forum/viewtopic.php?t=33652) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 6, 2010
* [SMP basics](http://www.talkchess.com/forum/viewtopic.php?t=33700) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), April 09, 2010
* [DTS Structure](http://www.talkchess.com/forum/viewtopic.php?t=34561) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), May 28, 2010 » [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting"), [Iterative Search](Iterative_Search "Iterative Search")
* [DTS-ification of YBWC](http://www.talkchess.com/forum/viewtopic.php?t=34633) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 01, 2010
* [SMP speed up](http://www.talkchess.com/forum/viewtopic.php?t=36082) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), September 14, 2010
* [SMP questions](http://www.talkchess.com/forum/viewtopic.php?t=36121) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 19, 2010


**2011**



* [On parallelization](http://www.talkchess.com/forum/viewtopic.php?t=38411) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011 » [Onno](Onno "Onno")
* [AMD Phenom Hex core (SMP performance problem)](http://www.talkchess.com/forum/viewtopic.php?t=38655) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 04, 2011
* [SMP for Android UCI engines](http://www.talkchess.com/forum/viewtopic.php?t=38753) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 14, 2011 » [Android](Android "Android")
* [Questions on SMP search](http://www.talkchess.com/forum/viewtopic.php?t=38808) by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), April 21, 2011
* [Some spinlock code, just for you](http://www.talkchess.com/forum/viewtopic.php?t=39247) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 01, 2011
* [Spinlocks galore](http://www.talkchess.com/forum/viewtopic.php?t=39256) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 02, 2011
* [LIFO stack based parallel processing?](http://www.talkchess.com/forum/viewtopic.php?t=40493) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), September 22, 2011
* [Some questions on split points](http://www.talkchess.com/forum/viewtopic.php?t=41036) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), November 09, 2011
* [Question on parallel search](http://www.talkchess.com/forum/viewtopic.php?t=41620) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), December 27, 2011


**2012**



* [Parallelization questions, ABDADA or DTS?](http://www.talkchess.com/forum/viewtopic.php?t=42986) by [Benjamin Rosseaux](index.php?title=Benjamin_Rosseaux&action=edit&redlink=1 "Benjamin Rosseaux (page does not exist)"), [CCC](CCC "CCC"), March 23, 2012 » [ABDADA](ABDADA "ABDADA"), [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [algorithms - distributed alpha beta pruning](http://cs.stackexchange.com/questions/998/distributed-alpha-beta-pruning) by wirate, [Computer Science Stack Exchange](http://cs.stackexchange.com/), April 2, 2012
* [YBWC: Active Reparenting](http://www.talkchess.com/forum/viewtopic.php?t=43243) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 10, 2012 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [Virtualization and multi-processor engines](http://www.talkchess.com/forum/viewtopic.php?t=44813) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), August 16, 2012
* [How to measure Parallel Search Speedup?](http://www.talkchess.com/forum/viewtopic.php?t=44876) by Marcel Fournier, [CCC](CCC "CCC"), August 23, 2012
* [SMP and questions](http://www.talkchess.com/forum/viewtopic.php?t=46124) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), November 23, 2012
* [Lazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=46597) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), December 27, 2012 » [Lazy SMP](Lazy_SMP "Lazy SMP")


**2013**



* [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
* [Parallel search: System-level programming details](http://www.talkchess.com/forum/viewtopic.php?t=47171) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), February 09, 2013
* [SMP search in Viper and idea about search in cluster system](http://www.talkchess.com/forum/viewtopic.php?t=47298) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), February 22, 2013 » [Viper](Viper "Viper")
* [Message passing parallel search on SMP system](http://www.talkchess.com/forum/viewtopic.php?t=47430) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 07, 2013 [[31]](#cite_note-31)
* [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013 [[32]](#cite_note-32)
* [Parallel search slowdown?](http://www.talkchess.com/forum/viewtopic.php?t=47762) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 12, 2013
* [Implementation of multithreaded search in Jazz](http://www.talkchess.com/forum/viewtopic.php?t=47820) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 20, 2013 » [Jazz](Jazz "Jazz")
* [parallel search speedup/overhead](http://www.talkchess.com/forum/viewtopic.php?t=47930) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 06, 2013
* [Peculiarity of Komodo 5.1MP](http://www.talkchess.com/forum/viewtopic.php?t=48339) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 19, 2013 » [Komodo](Komodo "Komodo")
* [back to the Komodo SMP issue](http://www.talkchess.com/forum/viewtopic.php?t=48503) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 01, 2013
* [Measure of SMP scalability](http://www.talkchess.com/forum/viewtopic.php?t=48524) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 03, 2013 » [Hannibal](Hannibal "Hannibal")


 [Measure of SMP scalability (sub-thread)](http://www.talkchess.com/forum/viewtopic.php?t=48591) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), July 08, 2013
* [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013 » [Lazy SMP](EXchess#LazySMP "EXchess") in [EXchess](EXchess "EXchess")
* [use sleeping threads](http://www.talkchess.com/forum/viewtopic.php?t=48612) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 10, 2013 » [Stockfish](Stockfish "Stockfish")
* [Recursive DTS-like search algorithm](http://www.talkchess.com/forum/viewtopic.php?t=48752) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 24, 2013 » [Texel](Texel "Texel"), [Recursion](Recursion "Recursion")
* [DTS-like SMP](http://www.open-chess.org/viewtopic.php?f=5&t=2378) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2013 » [Gull](Gull "Gull")
* [Time to depth measuring tool](http://www.talkchess.com/forum/viewtopic.php?t=48780) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 28, 2013 » [Depth](Depth "Depth")
* [interesting SMP bug](http://www.talkchess.com/forum/viewtopic.php?t=49450) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 24, 2013 » [Crafty](Crafty "Crafty")
* [SMP and Thread Pool Design pattern](http://www.talkchess.com/forum/viewtopic.php?t=49540) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), October 02, 2013


**2014**



* [SMP and pondering](http://www.talkchess.com/forum/viewtopic.php?t=51198) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), February 08, 2014 » [Pondering](Pondering "Pondering"), [Myrddin](Myrddin "Myrddin")
* [C++11 threads seem to get shafted for cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2618) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2014 » [Senpai](Senpai "Senpai"), [Thread](Thread "Thread"), [C++](Cpp "Cpp")
* [Threads-Test](http://www.talkchess.com/forum/viewtopic.php?t=51655) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), March 18, 2014 » [Thread](Thread "Thread"), [Stockfish](Stockfish "Stockfish")
* [Parallel Search with Transposition Table](http://www.talkchess.com/forum/viewtopic.php?t=51755) by [Daylen Yang](Daylen_Yang "Daylen Yang"), [CCC](CCC "CCC"), March 27, 2014 » [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [c++11 std::atomic and memory\_order\_relaxed](http://www.talkchess.com/forum/viewtopic.php?t=51824) by Kevin Hearn, [CCC](CCC "CCC"), April 01, 2014 » [Memory](Memory "Memory"), [C++](Cpp "Cpp")
* [Threads-Test - SF, Zappa, Komodo - 1 vs. 2, 4, 8, 16 Threads](http://www.talkchess.com/forum/viewtopic.php?t=52219) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 04, 2014 » [Stockfish](Stockfish "Stockfish"), [Zappa](Zappa "Zappa"), [Komodo](Komodo "Komodo")
* [transposition and multithreading question](http://www.talkchess.com/forum/viewtopic.php?t=52226) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 04, 2014 » [Transposition Table](Transposition_Table "Transposition Table")
* [Threads factor: Komodo, Houdini, Stockfish and Zappa](http://www.talkchess.com/forum/viewtopic.php?p=570955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 17, 2014 » [Komodo](Komodo "Komodo"), [Houdini](Houdini "Houdini"), [Stockfish](Stockfish "Stockfish"), [Zappa](Zappa "Zappa")
* [Smp concepts](http://www.talkchess.com/forum/viewtopic.php?t=52503) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), June 01, 2014
* [Real Speedup due to core doubling etc](http://www.talkchess.com/forum/viewtopic.php?t=52983) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), July 15, 2014
* [Implementing parallel search](http://www.talkchess.com/forum/viewtopic.php?t=53537) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 02, 2014
* [Elo difference for 4-8-16-24-32 cores](http://www.talkchess.com/forum/viewtopic.php?t=53739) by [Bertil Eklund](index.php?title=Bertil_Eklund&action=edit&redlink=1 "Bertil Eklund (page does not exist)"), [CCC](CCC "CCC"), September 17, 2014
* [Threads test incl. Stockfish 5 and Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=53995) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 09, 2014
* [Threads test - Stockfish 5 against Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=54009) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 10, 2014 » [Thread](Thread "Thread"), Parallel Search, [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo")
* [Threads test incl. Crafty 24.1](http://www.talkchess.com/forum/viewtopic.php?t=54059) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 15, 2014 » [Crafty](Crafty "Crafty")
* [Current data - threads-nps efficiency up to 32 threads](http://www.talkchess.com/forum/viewtopic.php?t=54133) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 24, 2014
* [Data structures for parallel search?](http://www.talkchess.com/forum/viewtopic.php?t=54386) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), November 19, 2014


### 2015 ...


* [SMP: on same branch instead splitting?](http://www.talkchess.com/forum/viewtopic.php?t=55047) by Frank Ludwig, [CCC](CCC "CCC"), January 23, 2015
* [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015 » [Cheng](Cheng "Cheng")
* [Some SMP measurements with Rookie v3](http://www.talkchess.com/forum/viewtopic.php?t=55224) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), February 05, 2015 » [Rookie](Rookie "Rookie")
* [Stockfish with 16 threads - big news?](http://www.talkchess.com/forum/viewtopic.php?t=55352) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 15, 2015 » [Thread](Thread "Thread")


 [Explanation for non-expert?](http://www.talkchess.com/forum/viewtopic.php?t=55368) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 16, 2015 » [Stockfish](Stockfish "Stockfish")
 [Best Stockfish NPS scaling yet](http://www.talkchess.com/forum/viewtopic.php?t=55536) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), March 02, 2015
* [Parallel iterative search function](http://www.talkchess.com/forum/viewtopic.php?t=55563) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), March 05, 2015 » [Iterative Search](Iterative_Search "Iterative Search")
* [An MPI perft program](http://www.talkchess.com/forum/viewtopic.php?t=55896) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), April 05, 2015 » [Perft](Perft "Perft") [[33]](#cite_note-33)
* [Crude parallel search](http://www.talkchess.com/forum/viewtopic.php?t=55930) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), April 07, 2015
* [Trying to improve lazy smp](http://www.talkchess.com/forum/viewtopic.php?t=55970) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 11, 2015
* [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015
* [DTS-Algorithm Split Block](http://www.open-chess.org/viewtopic.php?f=5&t=2830) by JacobusOpperman, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2015
* [The effective speedup from 1 to 8 cpus for SF and Komodo](http://www.talkchess.com/forum/viewtopic.php?t=56543) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), May 31, 2015 » [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo")
* [parallel speedup and assorted trivia](http://www.talkchess.com/forum/viewtopic.php?t=56595) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 05, 2015 » [Crafty](Crafty "Crafty")
* [There are compilers and there are compilers](http://www.talkchess.com/forum/viewtopic.php?t=56764) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 24, 2015
* [Parallel search once more](http://www.talkchess.com/forum/viewtopic.php?t=56779) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 25, 2015
* [SMP speedup discussion](http://www.talkchess.com/forum/viewtopic.php?t=56877) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 05, 2015
* [Possible improvement to ABDADA -- checking for cutoffs](http://www.talkchess.com/forum/viewtopic.php?t=56936) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 10, 2015 » [ABDADA](ABDADA "ABDADA")
* [Actual speedups from YBWC and ABDADA on 8+ core machines?](http://www.talkchess.com/forum/viewtopic.php?t=56937) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 10, 2015 » [ABDADA](ABDADA "ABDADA"), [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [New SMP stuff (particularly Kai)](http://www.talkchess.com/forum/viewtopic.php?t=57036) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 20, 2015
* [SMP (new style)](http://www.talkchess.com/forum/viewtopic.php?t=57039) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 20, 2015
* [scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 22, 2015 » [Scorpio](Scorpio "Scorpio")
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=57572) by Lucas Braesch, [CCC](CCC "CCC"), September 09, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Lazy SMP Better than YBWC?](http://www.talkchess.com/forum/viewtopic.php?t=58031) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), October 23, 2015 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [New Stockfish with Lazy\_SMP, but what about the TC bug ?](http://www.talkchess.com/forum/viewtopic.php?t=58056) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Stockfish](Stockfish "Stockfish"), [TCEC Season 8](TCEC_Season_8 "TCEC Season 8")
* [An interesting parallel search non-bug](http://www.talkchess.com/forum/viewtopic.php?t=58160) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 05, 2015 » [Crafty](Crafty "Crafty")
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=58645) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), December 21, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")


**2016**



* [NUMA 101](http://www.talkchess.com/forum/viewtopic.php?t=58830) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2016 » [NUMA](NUMA "NUMA")
* [Using more than 1 thread in C beginner question](http://www.talkchess.com/forum/viewtopic.php?t=58882) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 11, 2016 » [C](C "C")
* [Threads test incl. Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58887) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 11, 2016 » [Thread](Thread "Thread"), [Stockfish](Stockfish "Stockfish")
* [Parallel Search to Fixed Depth](http://www.talkchess.com/forum/viewtopic.php?t=58946) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), January 17, 2016
* [Threads test incl. Komodo 9.3](http://www.talkchess.com/forum/viewtopic.php?t=58950) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 17, 2016 » [Komodo](Komodo "Komodo")
* [Lazy SMP - how it works](http://www.talkchess.com/forum/viewtopic.php?t=59389) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), February 29, 2016 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Crafty SMP measurement](http://talkchess.com/forum/viewtopic.php?t=59745) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), April 04, 2016 » [Crafty](Crafty "Crafty")
* [parallel search speed measurement](http://www.talkchess.com/forum/viewtopic.php?t=60271) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 24, 2016
* [Crazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=60537) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 19, 2016
* [NUMA in a YBWC implementation](http://www.talkchess.com/forum/viewtopic.php?t=60875) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 20, 2016 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [lazy smp using ms vs2015 c++11 std::async](http://www.talkchess.com/forum/viewtopic.php?t=60979) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), July 29, 2016 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Thread](Thread "Thread") [[34]](#cite_note-34)
* [Time to depth concerns](http://www.talkchess.com/forum/viewtopic.php?t=61131) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), August 15, 2016
* [lets get the ball moving down the field on numa awareness](https://groups.google.com/d/msg/fishcooking/ezt6MrAuXqs/qIR2HEciEgAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 30, 2016 » [NUMA](NUMA "NUMA"), [Stockfish](Stockfish "Stockfish"), [asmFish](AsmFish "AsmFish")
* [Baffling multithreading scaling behavior](http://www.talkchess.com/forum/viewtopic.php?t=61349) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), September 06, 2016


 [Re: Baffling multithreading scaling behavior](http://www.talkchess.com/forum/viewtopic.php?t=61349&start=16) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 07, 2016
* [What do you do with NUMA?](http://www.talkchess.com/forum/viewtopic.php?t=61472) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 19, 2016 » [NUMA](NUMA "NUMA")
* [Scaling of Asmfish with large thread count](http://www.talkchess.com/forum/viewtopic.php?t=61639) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 07, 2016 » [asmFish](AsmFish "AsmFish")
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")


**2017**



* [How to find SMP bugs ?](http://www.talkchess.com/forum/viewtopic.php?t=63454) by Lucas Braesch, [CCC](CCC "CCC"), March 15, 2017 » [Debugging](Debugging "Debugging"), [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Ideas to improve SMP scaling](http://www.open-chess.org/viewtopic.php?f=5&t=3097) by lucasart, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 03, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum/viewtopic.php?t=63903) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 05, 2017 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [When should I consider parallel search ?](http://www.talkchess.com/forum/viewtopic.php?t=64238) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 10, 2017
* [Lazy SMP and "lazy cluster" experiments](http://www.talkchess.com/forum/viewtopic.php?t=64824) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Lazy SMP - Lazy Cluster](Lazy_SMP#LazyCluster "Lazy SMP"), [Texel](Texel "Texel")


 [Approximate ABDADA](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=43) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 23, 2017 » [ABDADA](ABDADA "ABDADA") 
* ["How To" guide to parallel-izing an engine](http://www.talkchess.com/forum/viewtopic.php?t=65011) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), August 27, 2017 [[35]](#cite_note-35)
* [Question about parallel search and race conditions](http://www.talkchess.com/forum/viewtopic.php?t=65134) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 11, 2017 » [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Parallel search/LazySMP question](http://www.talkchess.com/forum/viewtopic.php?t=66044) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 17, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Time Managment translating to SMP](http://www.talkchess.com/forum/viewtopic.php?t=66099) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 23, 2017  » [Time Management](Time_Management "Time Management")


**2018**



* [Lazy SMP and 44 cores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68154) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), August 07, 2018 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Lazy SMP ideas](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68278) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 22, 2018


**2019**



* [Simplest way to implement quick and dirty lazy smp](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69481) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 04, 2019
* [OpenMP for chess programming](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71115) by BeyondCritics, [CCC](CCC "CCC"), June 27, 2019
* [Multithreaded noob question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71739) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 06, 2019


### 2020 ...


* [assembler for locking at AMD magny cours](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=75695) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), November 06, 2020
* [Research paper comparing various parallel search algorithms](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78631) by koedem, [CCC](CCC "CCC"), November 10, 2021


## External Links


### Parallel Search


* [Parallel Search](http://www.tckerrigan.com/Chess/Parallel_Search/) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan") [[36]](#cite_note-36)
* [Parallel Alpha-Beta Pruning](http://www.netlib.org/utk/lsi/pcwLSI/text/node350.html) from [Parallel Computing Works](http://www.netlib.org/utk/lsi/pcwLSI/text/BOOK.html)
* [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)
* [AG-Monien - Research - Game Trees](http://www2.cs.uni-paderborn.de/cs/ag-monien/PERSONAL/FLULO/gametree.html), [AG-Monien](Burkhard_Monien "Burkhard Monien"), [Paderborn University](Paderborn_University "Paderborn University")
* [Adaptive Parallel Iterative Deepening Search](http://www.cs.cmu.edu/afs/cs/project/jair/pub/volume9/cook98a-html/eureka.html) by [Diane J. Cook](http://portal.acm.org/author_page.cfm?id=81100111814&coll=GUIDE&dl=GUIDE&trk=0&CFID=85545608&CFTOKEN=17034339), [R. Craig Varnell](http://portal.acm.org/author_page.cfm?id=81100529798&coll=GUIDE&dl=GUIDE&trk=0&CFID=85545608&CFTOKEN=17034339)


### Parallel Computing


* [Parallel computing from Wikipedia](https://en.wikipedia.org/wiki/Parallel_computing)
* [Parallel algorithm from Wikipedia](https://en.wikipedia.org/wiki/Parallel_algorithm)
* [Parallel slowdown from Wikipedia](https://en.wikipedia.org/wiki/Parallel_slowdown)
* [Concurrent computing from Wikipedia](https://en.wikipedia.org/wiki/Concurrent_computing)
* [Process from Wikipedia](https://en.wikipedia.org/wiki/Process_%28computing%29)
* [Thread from Wikipedia](https://en.wikipedia.org/wiki/Thread_%28computer_science%29)
* [Fiber (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Fiber_%28computer_science%29)
* [Coroutine from Wikipedia](https://en.wikipedia.org/wiki/Coroutine)
* [Multiprocessing from Wikipedia](https://en.wikipedia.org/wiki/Multiprocessing)
* [Multitasking from Wikipedia](https://en.wikipedia.org/wiki/Computer_multitasking)
* [Multithreading from Wikipedia](https://en.wikipedia.org/wiki/Multithreading_%28computer_architecture%29)
* [Speculative multithreading from Wikipedia](https://en.wikipedia.org/wiki/Speculative_multithreading)
* [Scheduling from Wikipedia](https://en.wikipedia.org/wiki/Scheduling_%28computing%29)
* [Preemption from Wikipedia](https://en.wikipedia.org/wiki/Preemption_%28computing%29)
* [Context switch from Wikipedia](https://en.wikipedia.org/wiki/Context_switch)
* [Cilk from Wikipedia](https://en.wikipedia.org/wiki/Cilk) » [Cilk](Cilk "Cilk"), [CilkChess](CilkChess "CilkChess")
* [The Cilk Project](http://supertech.csail.mit.edu/cilk/) from [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [Intel Cilk Plus from Wikipedia](https://en.wikipedia.org/wiki/Intel_Cilk_Plus) » [Intel](Intel "Intel")
* [XMTC from Wikipedia](https://en.wikipedia.org/wiki/XMTC)


### Scalability


* [Scalability from Wikipedia](https://en.wikipedia.org/wiki/Scalability)
* [Scalable locality from Wikipedia](https://en.wikipedia.org/wiki/Scalable_locality)
* [Scalable parallelism from Wikipedia](https://en.wikipedia.org/wiki/Scalable_parallelism)
* [Speedup from Wikipedia](https://en.wikipedia.org/wiki/Speedup)
* [Amdahl's law from Wikipedia](https://en.wikipedia.org/wiki/Amdahl%27s_law)
* [Gustafson's law from Wikipedia](https://en.wikipedia.org/wiki/Gustafson%27s_law)


### Shared Memory


[Shared Memory](Template:Shared_Memory "Template:Shared Memory"): 



* [Shared memory from Wikipedia](https://en.wikipedia.org/wiki/Shared_memory)
* [Memory model from Wikipedia](https://en.wikipedia.org/wiki/Memory_model_%28computing%29)
* [Information on the C++11 Memory Model](http://scottmeyers.blogspot.co.uk/2012/04/information-on-c11-memory-model.html) by [Scott Meyers](https://en.wikipedia.org/wiki/Scott_Meyers), April 24, 2012
* [Volatile variable from Wikipedia](https://en.wikipedia.org/wiki/Volatile_variable)
* [Memory ordering from Wikipedia](https://en.wikipedia.org/wiki/Memory_ordering)
* [Memory Ordering in Modern Microprocessors, Part I](http://www.linuxjournal.com/article/8211) by [Paul E. McKenney](https://plus.google.com/113202287320302059445/about), [Linux Journal](https://en.wikipedia.org/wiki/Linux_Journal), June 30, 2005
* [Memory barrier from Wikipedia](https://en.wikipedia.org/wiki/Memory_barrier)
* [Parallel Random Access Machine from Wikipedia](https://en.wikipedia.org/wiki/Parallel_Random_Access_Machine)
* [The Shared Memory Library (SharedMemoryLib) FAQ](http://www.inf.pucrs.br/%7Epinho/shared_memory_library.htm) by [Márcio Serolli Pinho](http://www.inf.pucrs.br/%7Epinho/)
* [Transactional memory from Wikipedia](https://en.wikipedia.org/wiki/Transactional_memory)
* [Software transactional memory from Wikipedia](https://en.wikipedia.org/wiki/Software_transactional_memory)
* [Cache coherence from Wikipedia](https://en.wikipedia.org/wiki/Cache_coherence)


 [False sharing from Wikipedia](https://en.wikipedia.org/wiki/False_sharing)
* [Distributed shared memory from Wikipedia](https://en.wikipedia.org/wiki/Distributed_shared_memory)
* [Memory-mapped file from Wikipedia](https://en.wikipedia.org/wiki/Memory-mapped_file)
* [Memory disambiguation from Wikipedia](https://en.wikipedia.org/wiki/Memory_disambiguation)
* [Memory dependence prediction from Wikipedia](https://en.wikipedia.org/wiki/Memory_dependence_prediction)
* [OpenMP from Wikipedia](https://en.wikipedia.org/wiki/OpenMP)
* [POSIX from Wikipedia](https://en.wikipedia.org/wiki/POSIX)
* [shm\_open](http://pubs.opengroup.org/onlinepubs/007908799/xsh/shm_open.html), [The Single UNIX Specification version 2](https://en.wikipedia.org/wiki/Single_UNIX_Specification#1997:_Single_UNIX_Specification_version_2), Copyright © 1997 [The Open Group](https://en.wikipedia.org/wiki/The_Open_Group)
* [shmget(2): allocates shared memory segment - Linux man page](http://linux.die.net/man/2/shmget) » [Linux](Linux "Linux")
* [mm(3): Shared Memory Allocation - Linux man page](http://www.pkill.info/linux/man/3-mm/)
* [CreateSharedMemory](http://msdn.microsoft.com/en-us/library/aa374778.aspx), [MSDN](https://en.wikipedia.org/wiki/Microsoft_Developer_Network) » [Windows](Windows "Windows")
* [Chapter 9. Boost.Interprocess - Boost 1.36.0](http://www.boost.org/doc/libs/1_36_0/doc/html/interprocess.html) by Ion Gaztañaga
* [Threads and memory model for C++](http://hboehm.info/c++mm/) by [Hans J. Boehm](http://www.hpl.hp.com/personal/Hans_Boehm/)
* [IPC:Shared Memory](http://www.cs.cf.ac.uk/Dave/C/node27.html) by [Dave Marshall](http://www.cs.cf.ac.uk/Dave/), 1999
* [Symmetric Multi-Processing (SMP) from Wikipedia](https://en.wikipedia.org/wiki/Symmetric_multiprocessing) » [SMP](SMP "SMP")
* [Asymmetric multiprocessing from Wikipedia](https://en.wikipedia.org/wiki/Asymmetric_multiprocessing)
* [Uniform Memory Access from Wikipedia](https://en.wikipedia.org/wiki/Uniform_Memory_Access)
* [Non-Uniform Memory Access (NUMA) from Wikipedia](https://en.wikipedia.org/wiki/Non-Uniform_Memory_Access) » [NUMA](NUMA "NUMA")
* [Optimizing Applications for NUMA | Intel® Developer Zone](http://software.intel.com/en-us/articles/optimizing-applications-for-numa)
* [Performance Guidelines for AMD Athlon™ 64 and AMD Opteron™ ccNUMA Multiprocessor Systems](https://doc.xdevs.com/doc/AMD/_Performance/Performance%20Guidelines%20for%20AMD%20Athlon%2064%20and%20AMD%20Opteron%20ccNUMA%20Multiprocessor%20Systems.%20rev.3.00%5D.%5B2006-06%5D.pdf) (pdf)


### Cache


[Cache](Template:Cache "Template:Cache"): 



* [Cache from Wikipedia](https://en.wikipedia.org/wiki/Cache)
* [Cache (computing) from Wikipedia](https://en.wikipedia.org/wiki/Cache_(computing))
* [Functional Principles of Cache Memory](http://alasir.com/articles/cache_principles/) by [Paul V. Bolotoff](http://alasir.com/articles/), April 2007
* [CPU cache from Wikipedia](https://en.wikipedia.org/wiki/CPU_cache)
* [Cache-only memory architecture (COMA) from Wikipedia](https://en.wikipedia.org/wiki/Cache-only_memory_architecture)
* [Cache coherence from Wikipedia](https://en.wikipedia.org/wiki/Cache_coherence)


 [MSI protocol from Wikipedia](https://en.wikipedia.org/wiki/MSI_protocol)
 [MESI protocol from Wikipedia](https://en.wikipedia.org/wiki/MESI_protocol)
 [MOESI protocol from Wikipedia](https://en.wikipedia.org/wiki/MOESI_protocol)
* [False sharing from Wikipedia](https://en.wikipedia.org/wiki/False_sharing)
* [Cache coloring from Wikipedia](https://en.wikipedia.org/wiki/Cache_coloring)
* [Cache hierarchy from Wikipedia](https://en.wikipedia.org/wiki/Cache_hierarchy)
* [Cache-oblivious algorithm from Wikipedia](https://en.wikipedia.org/wiki/Cache-oblivious_algorithm)
* [Cache pollution from Wikipedia](https://en.wikipedia.org/wiki/Cache_pollution)
* [Cache prefetching from Wikipedia](https://en.wikipedia.org/wiki/Cache_prefetching)
* [Prefetching from Wikipedia](https://en.wikipedia.org/wiki/Prefetching)


 [assembly - The prefetch instruction - Stack Overflow](http://stackoverflow.com/questions/3122915/the-prefetch-instruction)
 [Data Prefetch Support - GNU Project - Free Software Foundation (FSF)](http://gcc.gnu.org/projects/prefetch.html)
 [Software prefetching considered harmful](http://lwn.net/Articles/444344/) by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), [LWN.net](https://en.wikipedia.org/wiki/LWN.net), May 19, 2011
* [Cache replacement policies from Wikipedia](https://en.wikipedia.org/wiki/Cache_replacement_policies)
* [Page cache from Wikipedia](https://en.wikipedia.org/wiki/Page_cache)
* [Acumem SlowSpotter from Wikipedia](https://en.wikipedia.org/wiki/Acumem_SlowSpotter)
* [Analyzing Efficiency of Shared and Dedicated L2 Cache in Modern Dual-Core Processors](http://ixbtlabs.com/articles2/cpu/rmmt-l2-cache.html) from [iXBT Labs - Computer Hardware In Detail](http://ixbtlabs.com/)
* [Scratchpad memory from Wikipedia](https://en.wikipedia.org/wiki/Scratchpad_memory)


### Concurrency and Synchronization


[Synchronization](Template:Synchronization "Template:Synchronization"): 



* [Edsger W. Dijkstra](Mathematician#EWDijkstra "Mathematician") [Archive](http://www.cs.utexas.edu/users/EWD/):


 [Cooperating sequential processes (EWD 123)](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD01xx/EWD123.html)
 [A challenge to memory designers? (EWD 497)](http://www.cs.utexas.edu/users/EWD/transcriptions/EWD04xx/EWD497.html)
* [I remember Edsger Dijkstra (1930 – 2002) « A Programmers Place](http://vanemden.wordpress.com/2008/05/06/i-remember-edsger-dijkstra-1930-2002/) by [Maarten van Emden](Maarten_van_Emden "Maarten van Emden")
* [Concurrency from Wikipedia](https://en.wikipedia.org/wiki/Concurrency_%28computer_science%29)
* [Category:Concurrency from Wikipedia](https://en.wikipedia.org/wiki/Category:Concurrency)
* [Concurrency control from Wikipedia](https://en.wikipedia.org/wiki/Concurrency_control)
* [Optimistic concurrency control from Wikipedia](https://en.wikipedia.org/wiki/Optimistic_concurrency_control)
* [Synchronization from Wikipedia](https://en.wikipedia.org/wiki/Synchronization_%28computer_science%29)
* [Inter-process communication from Wikipedia](https://en.wikipedia.org/wiki/Inter-process_communication)
* [Non-blocking algorithm from Wikipedia](https://en.wikipedia.org/wiki/Non-blocking_algorithm)
* [Linearizability from Wikipedia](https://en.wikipedia.org/wiki/Linearizability)
* [Monitor (synchronization)](https://en.wikipedia.org/wiki/Monitor_%28synchronization%29)
* [Lock from Wikipedia](https://en.wikipedia.org/wiki/Lock_%28computer_science%29)
* [Busy waiting from Wikipedia](https://en.wikipedia.org/wiki/Busy_waiting)
* [Seqlock from Wikipedia](https://en.wikipedia.org/wiki/Seqlock)
* [Spinlock from Wikipedia](https://en.wikipedia.org/wiki/Spinlock)
* [Double-checked locking from Wikipedia](https://en.wikipedia.org/wiki/Double-checked_locking)
* [Compare-and-swap from Wikipedia](https://en.wikipedia.org/wiki/Compare-and-swap)
* [Test-and-set from Wikipedia](https://en.wikipedia.org/wiki/Test-and-set)
* [Test and Test-and-set from Wikipedia](https://en.wikipedia.org/wiki/Test_and_Test-and-set)
* [Fetch-and-add from Wikipedia](https://en.wikipedia.org/wiki/Fetch-and-add)
* [Barrier from Wikipedia](https://en.wikipedia.org/wiki/Barrier_%28computer_science%29)
* [Memory barrier from Wikipedia](https://en.wikipedia.org/wiki/Memory_barrier)
* [Critical section from Wikipedia](https://en.wikipedia.org/wiki/Critical_section)
* [Mutual exclusion from Wikipedia](https://en.wikipedia.org/wiki/Mutual_exclusion)
* [Semaphore from Wikipedia](https://en.wikipedia.org/wiki/Semaphore_%28programming%29)
* [Transactional Synchronization Extensions from Wikipedia](https://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions) ([Haswell](https://en.wikipedia.org/wiki/Haswell_%28microarchitecture%29))
* [Readers-writers problem from Wikipedia](https://en.wikipedia.org/wiki/Readers-writers_problem)
* [Readers-writer lock from Wikipedia](https://en.wikipedia.org/wiki/Readers-writer_lock)
* [Read-copy-update from Wikipedia](https://en.wikipedia.org/wiki/Read-copy-update)
* [Producer-consumer problem from Wikipedia](https://en.wikipedia.org/wiki/Producers-consumers_problem)
* [Dining philosophers problem from Wikipedia](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
* [Cigarette smokers problem from Wikipedia](https://en.wikipedia.org/wiki/Cigarette_smokers_problem)
* [Sleeping barber problem from Wikipedia](https://en.wikipedia.org/wiki/Sleeping_barber_problem)
* [Resource starvation from Wikipedia](https://en.wikipedia.org/wiki/Resource_starvation)
* [Deadlock from Wikipedia](https://en.wikipedia.org/wiki/Deadlock)
* [Anatomy of Linux synchronization methods](http://www.ibm.com/developerworks/linux/library/l-linux-synchronization.html) by [M. Tim Jones](http://www.mtjones.com/), [IBM developerWorks](http://www.ibm.com/developerworks/), October 31, 2007
* [The Little Book of Semaphores](http://greenteapress.com/semaphores/) by [Allen B. Downey](http://allendowney.com/)


### Misc


* [Message Passing Interface from Wikipedia](https://en.wikipedia.org/wiki/Message_Passing_Interface)
* [Channel (programming) from Wikipedia](https://en.wikipedia.org/wiki/Channel_%28programming%29)
* [Multiple-agent system from Wikipedia](https://en.wikipedia.org/wiki/Multiple-agent_system)
* [Deterministic algorithm from Wikipedia](https://en.wikipedia.org/wiki/Deterministic_algorithm)
* [Intel® Parallel Inspector Thread Checker](http://software.intel.com/en-us/videos/intel-parallel-inspector-thread-checker/)
* [Intel Parallel Universe Magazine - Intel® Software Network](http://software.intel.com/en-us/articles/intel-parallel-universe-magazine/)
* [CHESS - Microsoft Research](http://research.microsoft.com/en-us/projects/chess/) a tool for finding and reproducing [Heisenbugs](https://en.wikipedia.org/wiki/Unusual_software_bug) in concurrent programs.
* [Led Zeppelin](Category:Led_Zeppelin "Category:Led Zeppelin") - [Communication Breakdown](https://en.wikipedia.org/wiki/Communication_Breakdown), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video, Lost Performances (1/5)


 
## References


1. [↑](#cite_ref-1) [Super Linearity and the Bigger Machine](http://www.drdobbs.com/high-performance-computing/206903306) from [Dr. Dobb's](http://www.drdobbs.com/index.jhtml)
2. [↑](#cite_ref-2) [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
3. [↑](#cite_ref-3) [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015
4. [↑](#cite_ref-4) [Re: A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170&start=11) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 01, 2015
5. [↑](#cite_ref-5) [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *The ABDADA Distributed Minimax Search Agorithm*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
6. [↑](#cite_ref-6) [Yaoqing Gao](index.php?title=Yaoqing_Gao&action=edit&redlink=1 "Yaoqing Gao (page does not exist)"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1996**). *Multithreaded Pruned Tree Search in Distributed Systems*. Journal of Computing and Information, 2(1), 482-492, [pdf](http://www.cs.ualberta.ca/%7Etony/RecentPapers/icci.pdf)
7. [↑](#cite_ref-7) [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
8. [↑](#cite_ref-8) [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Ph.D. Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
9. [↑](#cite_ref-9) [Christopher F. Joerg](Chris_Joerg "Chris Joerg"), [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
10. [↑](#cite_ref-10) [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Synchronized MIMD Computing*. Ph. D. Thesis, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/thesis-kuszmaul.pdf)
11. [↑](#cite_ref-11) [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1995**). *The StarTech Massively Parallel Chess Program*. [pdf](http://supertech.csail.mit.edu/papers/startech.pdf)
12. [↑](#cite_ref-12) [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *Improved Speedup Bounds for Parallel Alpha-Beta Search*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 5, No. 1, pp. 89 - 92
13. [↑](#cite_ref-13) [Raphael Finkel](Raphael_Finkel "Raphael Finkel"), [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1982**). *Parallelism in Alpha-Beta Search*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 19, No. 1
14. [↑](#cite_ref-14) [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1981**). *Analysis of Speedup in Distributed Algorithms*. Ph.D. Thesis, [pdf](http://www.cs.wisc.edu/techreports/1981/TR431.pdf)
15. [↑](#cite_ref-15) [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1994**). *[The DTS high-performance parallel tree search algorithm](http://www.craftychess.com/hyatt/search.html)*
16. [↑](#cite_ref-16) [Mark Brockington](Mark_Brockington "Mark Brockington") (**1996**). *A Taxonomy of Parallel Game-Tree Search Algorithms*. [ICCA Journal, Vol. 19: No. 3](ICGA_Journal#19_3 "ICGA Journal")
17. [↑](#cite_ref-17) [Research paper comparing various parallel search algorithms](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78631) by koedem, [CCC](CCC "CCC"), November 10, 2021
18. [↑](#cite_ref-18) UIDPABS = Unsynchronized Iteratively Deepening Parallel Alpha-Beta Search
19. [↑](#cite_ref-19) CABP = Concurrent Alpha-Beta Pruning
20. [↑](#cite_ref-20) It should also be noted that [Crafty](Crafty "Crafty") uses threads on [Windows](Windows "Windows"), and used processes on [Unix](Unix "Unix")
21. [↑](#cite_ref-21) [threads vs processes again](http://www.talkchess.com/forum/viewtopic.php?t=22799) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 27, 2006
22. [↑](#cite_ref-22) [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1985**). *[Lionel Moser](index.php?title=Lionel_Moser&action=edit&redlink=1 "Lionel Moser (page does not exist)"): An Experiment in Distributed Game Tree Searching.* [ICCA Journal, Vol. 8, No. 2](ICGA_Journal#8_2 "ICGA Journal") (Review)
23. [↑](#cite_ref-23) [An Introduction to Computer Chess](https://cs.uwaterloo.ca/~alopez-o/divulge/chimp.html) by [Alejandro López-Ortiz](index.php?title=Alejandro_L%C3%B3pez-Ortiz&action=edit&redlink=1 "Alejandro López-Ortiz (page does not exist)"), 1993
24. [↑](#cite_ref-24) [Nagging from Wikipedia](https://en.wikipedia.org/wiki/Nagging)
25. [↑](#cite_ref-25) [Re: scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343&start=5) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 29, 2015
26. [↑](#cite_ref-26) [Transposition-driven scheduling - Wikipedia](https://en.wikipedia.org/wiki/Transposition-driven_scheduling)
27. [↑](#cite_ref-27) [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013
28. [↑](#cite_ref-28) [Dovetailing (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Dovetailing_%28computer_science%29)
29. [↑](#cite_ref-29) [Georg Hager's Blog | Random thoughts on High Performance Computing](https://blogs.fau.de/hager/)
30. [↑](#cite_ref-30) [Re: Minmax backup operator for MCTS](http://www.talkchess.com/forum/viewtopic.php?t=66125&start=18) by [Brahim Hamadicharef](index.php?title=Brahim_Hamadicharef&action=edit&redlink=1 "Brahim Hamadicharef (page does not exist)"), [CCC](CCC "CCC"), December 30, 2017
31. [↑](#cite_ref-31) [Message Passing Interface from Wikipedia](https://en.wikipedia.org/wiki/Message_Passing_Interface)
32. [↑](#cite_ref-32) [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf)
33. [↑](#cite_ref-33) [Message Passing Interface from Wikipedia](https://en.wikipedia.org/wiki/Message_Passing_Interface)
34. [↑](#cite_ref-34) [std::async - cppreference.com](http://en.cppreference.com/w/cpp/thread/async)
35. [↑](#cite_ref-35) [Parallel Search](http://www.tckerrigan.com/Chess/Parallel_Search/) by [[Tom Kerrigan]
36. [↑](#cite_ref-36) ["How To" guide to parallel-izing an engine](http://www.talkchess.com/forum/viewtopic.php?t=65011) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), August 27, 2017

**[Up one level](Search "Search")**







 
