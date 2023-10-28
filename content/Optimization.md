---
title: Optimization
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* Optimization**


**Optimization** is about to chose the best element from some set of available alternatives, as referred in [mathematical optimization](https://en.wikipedia.org/wiki/Mathematical_optimization) as for instance applied in computer chess to optimize [evaluation](Evaluation "Evaluation") weights with [automated tuning methods](Automated_Tuning "Automated Tuning"), and [program optimizations](https://en.wikipedia.org/wiki/Program_optimization), which is the topic covered on this page. Most importantly there is the [algorithmic](Algorithms "Algorithms") optimization on design level such as using [alpha-beta](Alpha-Beta "Alpha-Beta") rather than plain [minimax](Minimax "Minimax"), followed by source code optimizations, and finally [Compiler optimizations](https://en.wikipedia.org/wiki/Compiler_optimization).



### Contents


* [1 Premature Optimization](#premature-optimization)
* [2 Program Optimizations](#program-optimizations)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Program Optimization](#program-optimization)
	+ [6.2 Mathematical Optimization](#mathematical-optimization)
* [7 References](#references)






As a warning on premature optimization a quote by [Donald Knuth](Donald_Knuth "Donald Knuth") <a id="cite-note-1" href="#cite-ref-1">[1]</a>:




```
We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.  

```

## Program Optimizations


Program Optimization is a necessary part of a decent chess program. It comes in two forms, compiler-end and program-end. Compiler-end optimization involves using specific flags to get a quick program at the cost of speed of compile and memory usage, whereas program-end optimization involves using inline functions and things like that.



* [Avoiding Branches](Avoiding_Branches "Avoiding Branches")
* [Performance Measurement](index.php?title=Performance_Measurement&action=edit&redlink=1 "Performance Measurement (page does not exist)")
* [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
* [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")


## See also


* [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Genetic Programming](Genetic_Programming "Genetic Programming")
* [NUMA](NUMA "NUMA")
* [Simulated Annealing](Simulated_Annealing "Simulated Annealing")


## Publications


* [Bruce W. Leverett](Bruce_W._Leverett "Bruce W. Leverett") (**1981**). *Register allocation in optimizing compilers*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
* [Bruce W. Leverett](Bruce_W._Leverett "Bruce W. Leverett") (**1982**). *[Topics in Code Generation and Register Allocation](http://books.google.com/books/about/Topics_in_Code_Generation_and_Register_A.html?id=ZNoEHAAACAAJ&redir_esc=y)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
* [Bruce W. Leverett](Bruce_W._Leverett "Bruce W. Leverett") (**1983**). *[Register allocation in optimizing compilers](http://books.google.com/books/about/Register_allocation_in_optimizing_compil.html?id=BUkVAQAAIAAJ&redir_esc=y)*. UMI Research Press


## Forum Posts


* [Beginner's guide to graphical profiling](http://www.talkchess.com/forum/viewtopic.php?t=61373) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 10, 2016 » [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)"), [Giraffe](Giraffe "Giraffe")


 [Re: Beginner's guide to graphical profiling](http://www.talkchess.com/forum/viewtopic.php?t=61373&start=2) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 10, 2016 » [Stockfish](Stockfish "Stockfish")
* [Reliable speed comparison: some math required](http://www.talkchess.com/forum/viewtopic.php?t=66701) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), February 27, 2018 » [Nodes per Second](Nodes_per_Second "Nodes per Second")
* [Performance loss when removing unused function](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75308) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 05, 2020
* [Different performance of equal executables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75525) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), October 24, 2020


## External Links


### Program Optimization


* [Program optimization from Wikipedia](https://en.wikipedia.org/wiki/Program_optimization)
* [Compiler optimization from Wikipedia](https://en.wikipedia.org/wiki/Compiler_optimization)
* [Software optimization resources. C++ and assembly. Windows, Linux, BSD, Mac OS X](http://www.agner.org/optimize/) by [Agner Fog](http://www.agner.org/)
* [Programming Optimization](http://www.azillionmonkeys.com/qed/optimize.html) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh")


### Mathematical Optimization


* [Mathematical optimization from Wikipedia](https://en.wikipedia.org/wiki/Mathematical_optimization)


 [Global optimization from Wikipedia](https://en.wikipedia.org/wiki/Global_optimization)
 [Optimization problem from Wikipedia](https://en.wikipedia.org/wiki/Optimization_problem)
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Donald Knuth](Donald_Knuth "Donald Knuth") (**1974**).*Structured Programming with go to Statements*. [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 6, No. 4, [pdf](http://cs.sjsu.edu/~mak/CS185C/KnuthStructuredProgrammingGoTo.pdf)

**[Up one Level](Programming "Programming")**







 
