---
title: Thread
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* Thread**



[ Two threads on a single processor [[1]](#cite_note-1)
A **Thread** is the smallest unit of processing that can be [scheduled](https://en.wikipedia.org/wiki/Scheduling_algorithm) by an [operating system](https://en.wikipedia.org/wiki/Operating_system). One or multiple threads can exist within the same [process](Process "Process") to share its resources such as [memory](Memory "Memory"). Modern operating systems support both [time-sliced](https://en.wikipedia.org/wiki/Time-division_multiplexing) and multiprocessor threading within a process scheduler. Some operating systems such as [Windows](Windows "Windows") distinguish worker threads from GUI-threads, which incorporate a [message loop](https://en.wikipedia.org/wiki/Event_loop), able to receive messages from worker threads. Threads share [global data](https://en.wikipedia.org/wiki/Global_variable) of the process, but use disjoint [stacks](Stack "Stack") for [local variables](https://en.wikipedia.org/wiki/Local_variable).


Chess programs using threads for a [parallel search](Parallel_Search "Parallel Search") have to deal with synchronization issues, if multiple threads read and write [none atomic](https://en.wikipedia.org/wiki/Linearizability) global data simultaneously, requiring multiple read and/or write cycles. A good step to make a program [thread safe](https://en.wikipedia.org/wiki/Thread_safety), is to avoid global variables and to keep board and game states as locals on the stack. To minimize [context switching](https://en.wikipedia.org/wiki/Context_switch), chess programs often implement a [thread pooling pattern](https://en.wikipedia.org/wiki/Thread_pool_pattern) along with explicitly or implicitly controlling [processor affinity](https://en.wikipedia.org/wiki/Processor_affinity), where the number of threads of the chess program is less or equal to the number of physical processor cores. Threads are further versatile to control [standard input](https://en.wikipedia.org/wiki/Standard_streams) inside an engine. 



### Contents


* [1 See also](#See_also)
* [2 Publications](#Publications)
	+ [2.1 1994 ...](#1994_...)
	+ [2.2 2000 ...](#2000_...)
	+ [2.3 2010 ...](#2010_...)
* [3 Forum Posts](#Forum_Posts)
	+ [3.1 1999](#1999)
	+ [3.2 2000 ...](#2000_..._2)
	+ [3.3 2005 ...](#2005_...)
	+ [3.4 2010 ...](#2010_..._2)
	+ [3.5 2015 ...](#2015_...)
	+ [3.6 2020 ...](#2020_...)
* [4 External Links](#External_Links)
	+ [4.1 Thread](#Thread)
	+ [4.2 Multithreading](#Multithreading)
	+ [4.3 Posix](#Posix)
	+ [4.4 Windows](#Windows)
	+ [4.5 C++](#C.2B.2B)
	+ [4.6 Java](#Java)
	+ [4.7 GPU](#GPU)
* [5 References](#References)






* [Cilk](Cilk "Cilk")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [NUMA](NUMA "NUMA")
* [Parallel Search](Parallel_Search "Parallel Search")
* [Process](Process "Process")
* [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [SMP](SMP "SMP")


## Publications


### 1994 ...


* [Michael Halbherr](Michael_Halbherr "Michael Halbherr"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou"), [Chris Joerg](Chris_Joerg "Chris Joerg") (**1994**). *[MIMD-Style Parallel Programming with Continuation-Passing Threads](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.16.9812)*. Proceedings of the 2nd International Workshop on Massive Parallelism: Hardware, Software, and Applications
* [Robert Blumofe](Robert_Blumofe "Robert Blumofe") (**1995**). *Executing Multithreaded Programs Efficiently*. Ph.D. thesis, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/rdb-phdthesis.pdf)
* [Robert Blumofe](Robert_Blumofe "Robert Blumofe"), [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou") (**1995**). *Cilk: An Efficient Multithreaded Runtime System*. Proceedings of the Fifth [ACM SIGPLAN](ACM#SIG "ACM") Symposium on Principles and Practice of Parallel Programming (PPoPP), [pdf](http://supertech.csail.mit.edu/papers/PPoPP95.pdf) » [Cilk](Cilk "Cilk")
* [Yaoqing Gao](index.php?title=Yaoqing_Gao&action=edit&redlink=1 "Yaoqing Gao (page does not exist)"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1996**). *Multithreaded Pruned Tree Search in Distributed Systems*. Journal of Computing and Information, 2(1), 482-492, [pdf](http://www.cs.ualberta.ca/%7Etony/RecentPapers/icci.pdf)
* [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop") (**1998**). *A Minicourse on Multithreaded Programming*. [pdf](http://supertech.csail.mit.edu/papers/minicourse.pdf)


### 2000 ...


* [Martin Harvey](http://comp.lang.pascal.delphi.misc.narkive.com/HW7VUOEV/martin-harvey-thread-tutorial) (**2000**). *[Multithreading - The Delphi Way](http://seti.net/engineering/threads/threads.php)*. » [Delphi](Delphi "Delphi")
* [Yue Yang](http://dblp.uni-trier.de/pers/hd/y/Yang:Yue), [Ganesh Gopalakrishnan](http://dblp.uni-trier.de/pers/hd/g/Gopalakrishnan:Ganesh), [Gary Lindstrom](Gary_Lindstrom "Gary Lindstrom") (**2002**). *Specifying Java Thread Semantics Using a Uniform Memory Model*. [Java Grande 2002](http://dblp.uni-trier.de/db/conf/java/java2002.html#YangGL02), [pdf](http://formalverification.cs.utah.edu/yyang/papers/umm_old.pdf)
* [Hans J. Boehm](http://www.hpl.hp.com/personal/Hans_Boehm/) (**2004**). *Threads Cannot be Implemented as a Library*. [HP Labs](https://en.wikipedia.org/wiki/HP_Labs) [Palo Alto](https://en.wikipedia.org/wiki/Palo_Alto,_California), [pdf](http://www.hpl.hp.com/techreports/2004/HPL-2004-209.pdf)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason"), [Dan Orme](index.php?title=Dan_Orme&action=edit&redlink=1 "Dan Orme (page does not exist)") (**2005**). *[Writing cpu intensive AI without multi-threading](http://www.aifactory.co.uk/newsletter/2005_01_nonmultithreading_AI.htm)*. [AI Factory](AI_Factory "AI Factory"), Spring 2005
* [Edward A. Lee](http://ptolemy.berkeley.edu/~eal/) (**2006**). *[The Problem with Threads](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.html)*. Technical Report No. UCB/EECS-2006-1, [University of California, Berkeley](University_of_California,_Berkeley "University of California, Berkeley"), [pdf](http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf)


### 2010 ...


* [Subhash Saini](https://en.wikipedia.org/wiki/Subhash_Saini), [Haoqiang Jin](http://people.nas.nasa.gov/~hjin/home.html), [Robert Hood](https://www.linkedin.com/in/robert-hood-250756), [David Barker](https://www.linkedin.com/in/david-barker-31484240), [Piyush Mehrotra](https://www.linkedin.com/in/pimehrotra), [Rupak Biswas](https://www.linkedin.com/in/rupak-biswas-5229805) (**2011**). *The Impact of Hyper-Threading on Processor Resource Utilization in Production Applications*. [NASA Advanced Supercomputing Division](https://en.wikipedia.org/wiki/NASA_Advanced_Supercomputing_Division), [pdf](https://www.nas.nasa.gov/assets/pdf/papers/saini_s_impact_hyper_threading_2011.pdf), [pdf](http://www.nas.nasa.gov/assets/pdf/papers/Saini_etAl_IEEE_HiPC_2011.pdf) [[2]](#cite_note-2)
* [Anthony Williams](http://stackoverflow.com/users/5597/anthony-williams) (**2012**). *[C++ Concurrency in Action: Practical Multithreading](http://www.cplusplusconcurrencyinaction.com/)*. [[3]](#cite_note-3)
* [Georg Hager](https://www.rrze.fau.de/wir-ueber-uns/organigramm/mitarbeiter/index.shtml/georg-hager.shtml) [[4]](#cite_note-4), [Jan Treibig](http://dblp.uni-trier.de/pers/hd/t/Treibig:Jan), [Gerhard Wellein](http://dblp.uni-trier.de/pers/hd/w/Wellein:Gerhard) (**2013**). *The Practitioner's Cookbook for Good Parallel Performance on Multi- and Many-Core Systems*. [RRZE](https://de.wikipedia.org/wiki/Regionales_Rechenzentrum_Erlangen), [SC13](http://sc13.supercomputing.org/), [slides as pdf](https://blogs.fau.de/hager/files/2013/11/sc13_tutorial_134.pdf)


## Forum Posts


### 1999


* [Threads](http://www.stmintz.com/ccc/index.php?id=48199) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), April 06, 1999
* [gcc / cygwin threads revisited](http://www.stmintz.com/ccc/index.php?id=61963) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), July 24, 1999


### 2000 ...


* [Re: Stormx is this a Crafty Clone??](http://www.stmintz.com/ccc/index.php?id=367073) by [Sean Empey](Sean_Empey "Sean Empey"), [CCC](CCC "CCC"), May 25, 2004 » [Windows](Windows "Windows")
* [Approaches to threading](http://www.stmintz.com/ccc/index.php?id=370625) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), June 15, 2004
* [Kiwi for Win98 and input-reading stuff](http://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [Windows](Windows "Windows"), [C++](Cpp "Cpp")


### 2005 ...


* [POSIX threads](http://www.stmintz.com/ccc/index.php?id=435053) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 05, 2005
* [Threading issue under Polyglot](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5603) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 18, 2006 » [PolyGlot](PolyGlot "PolyGlot")
* [pthread weirdness](http://www.talkchess.com/forum/viewtopic.php?t=14114) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), May 29, 2007
* [multithreading questions](http://www.talkchess.com/forum/viewtopic.php?t=15662) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), August 08, 2007
* [Threads and cores questions](http://www.talkchess.com/forum/viewtopic.php?t=16334) by Casey, [CCC](CCC "CCC"), September 07, 2007
* [threads vs processes](http://www.talkchess.com/forum/viewtopic.php?t=22398) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 16, 2008
* [threads vs processes again](http://www.talkchess.com/forum/viewtopic.php?t=22799) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 05, 2008
* [Hyperthreading Hype predates Intel](http://www.talkchess.com/forum/viewtopic.php?t=26434) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 07, 2009
* [Multithreaded movepath enumeration (perft)](http://www.talkchess.com/forum/viewtopic.php?t=26782) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 27, 2009
* [kbhit() taking huge CPU??](http://www.talkchess.com/forum/viewtopic.php?t=27279) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), April 01, 2009 » [C](C "C")


### 2010 ...


* [Stockfish-1.7.0 Hyper-threading Detection](http://www.talkchess.com/forum/viewtopic.php?t=33705) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), April 09, 2010
* [Hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=36103) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), September 17, 2010
* [To hyperthread or not to hyperthread (Crafty tested)](http://www.talkchess.com/forum/viewtopic.php?t=36465) by [Martin Thoresen](Martin_Thoresen "Martin Thoresen"), [CCC](CCC "CCC"), October 24, 2010 » [Crafty](Crafty "Crafty")
* [Input / ThinkingThreads](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=36637) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), November 08, 2010
* [Thread management / organization in parallel processing?](http://www.talkchess.com/forum/viewtopic.php?t=36966) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), December 06, 2010


**2011**



* [Have Crafty's threads never gone to sleep?](http://www.talkchess.com/forum/viewtopic.php?t=37896) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), January 31, 2011
* [On parallelization](http://www.talkchess.com/forum/viewtopic.php?t=38411) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011


**2012**



* [hyper threading and move generation](http://www.talkchess.com/forum/viewtopic.php?t=44658) by [Gabor Buella](Gabor_Buella "Gabor Buella"), [CCC](CCC "CCC"), August 01, 2012 » [Move Generation](Move_Generation "Move Generation")


**2013**



* [Multi-threaded memory access](http://www.open-chess.org/viewtopic.php?f=5&t=2262) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2013 » [Memory](Memory "Memory"), [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Hyperthreading and Computer Chess: Intel i5-3210M](http://www.talkchess.com/forum/viewtopic.php?t=47757) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), April 12, 2013
* [Implementation of multithreaded search in Jazz](http://www.talkchess.com/forum/viewtopic.php?t=47820) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 20, 2013 » [Parallel Search](Parallel_Search "Parallel Search"), [Jazz](Jazz "Jazz")
* [use sleeping threads](http://www.talkchess.com/forum/viewtopic.php?t=48612) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 10, 2013 » [Stockfish](Stockfish "Stockfish")
* [C++ Question](http://www.talkchess.com/forum/viewtopic.php?t=48795) by Ted Wong, [CCC](CCC "CCC"), July 30, 2013 » [C++](Cpp "Cpp")
* [Writing to a Text File (Thread Safe)](http://www.talkchess.com/forum/viewtopic.php?t=48911) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), August 10, 2013 » [Logging](Logging "Logging")
* [SMP and Thread Pool Design pattern](http://www.talkchess.com/forum/viewtopic.php?t=49540) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), October 02, 2013
* [Multithreaded LRU](http://www.talkchess.com/forum/viewtopic.php?t=49592) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), October 06, 2013 » [Memory](Memory "Memory"), [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")


**2014**



* [C++11 threads seem to get shafted for cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2618) by [User923005](Dann_Corbit "Dann Corbit"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2014 » [C++](Cpp "Cpp"), [Parallel Search](Parallel_Search "Parallel Search"), [Senpai](Senpai "Senpai")
* [Threads-Test](http://www.talkchess.com/forum/viewtopic.php?t=51655) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), March 18, 2014 » [Parallel Search](Parallel_Search "Parallel Search"), [Stockfish](Stockfish "Stockfish")
* [Threads-Test - SF, Zappa, Komodo - 1 vs. 2, 4, 8, 16 Threads](http://www.talkchess.com/forum/viewtopic.php?t=52219) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 04, 2014 » [Stockfish](Stockfish "Stockfish"), [Zappa](Zappa "Zappa"), [Komodo](Komodo "Komodo")
* [Threads factor: Komodo, Houdini, Stockfish and Zappa](http://www.talkchess.com/forum/viewtopic.php?p=570955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 17, 2014 » [Komodo](Komodo "Komodo"), [Houdini](Houdini "Houdini"), [Stockfish](Stockfish "Stockfish"), [Zappa](Zappa "Zappa")
* [TinyThread++](http://www.talkchess.com/forum/viewtopic.php?t=53063) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), July 24, 2014 [[5]](#cite_note-5)
* [Best way to handle input thread](http://www.talkchess.com/forum/viewtopic.php?t=53230) by [Stefano Gemma](Stefano_Gemma "Stefano Gemma"), [CCC](CCC "CCC"), August 09, 2014
* [(Why) Is hyperthreading bad for chess engines?](http://www.talkchess.com/forum/viewtopic.php?t=53806) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), September 23, 2014
* [Threads test incl. Stockfish 5 and Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=53995) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 09, 2014
* [Threads test - Stockfish 5 against Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=54009) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 10, 2014 » Thread, [Parallel Search](Parallel_Search "Parallel Search"), [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo")
* [Threads test incl. Crafty 24.1](http://www.talkchess.com/forum/viewtopic.php?t=54059) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 15, 2014 » [Crafty](Crafty "Crafty")
* [Current data - threads-nps efficiency up to 32 threads](http://www.talkchess.com/forum/viewtopic.php?t=54133) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 24, 2014


### 2015 ...


* [Stockfish with 16 threads - big news?](http://www.talkchess.com/forum/viewtopic.php?t=55352) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 15, 2015


 [Explanation for non-expert?](http://www.talkchess.com/forum/viewtopic.php?t=55368) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 16, 2015 » [Stockfish](Stockfish "Stockfish")
* [Thread count limits and core counts](http://www.talkchess.com/forum/viewtopic.php?t=55740) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 22, 2015
* [Thread synchronization questions for experts](http://www.talkchess.com/forum/viewtopic.php?t=56081) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 21, 2015 » [Symbolic](Symbolic "Symbolic")
* [A cautionary tale on thread safety](http://www.talkchess.com/forum/viewtopic.php?t=56113) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 25, 2015
* [A Nice routine](http://www.talkchess.com/forum/viewtopic.php?t=56327) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 12, 2015
* [Does Hyperthreading have trouble with AVX?](https://stackoverflow.com/questions/30330013/does-hyperthreading-have-trouble-with-avx) by cmylin, [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow), May 19, 2015 » [AVX](AVX "AVX"), [AVX2](AVX2 "AVX2")
* [Deep split perft()](http://www.talkchess.com/forum/viewtopic.php?t=56523) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 29, 2015 » [Perft](Perft "Perft"), [Symbolic](Symbolic "Symbolic")
* [thread affinity](http://www.talkchess.com/forum/viewtopic.php?t=56858) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), July 03, 2015
* [Stockfish now benefits from hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=58236) by [Dmitri Gusev](Dmitri_Gusev "Dmitri Gusev"), [CCC](CCC "CCC"), November 12, 2015 » [Stockfish](Stockfish "Stockfish")


**2016**



* [Using more than 1 thread in C beginner question](http://www.talkchess.com/forum/viewtopic.php?t=58882) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), January 11, 2016
* [Threads test incl. Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58887) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 11, 2016 » [Parallel Search](Parallel_Search "Parallel Search"), [Stockfish](Stockfish "Stockfish")
* [Threads test incl. Komodo 9.3](http://www.talkchess.com/forum/viewtopic.php?t=58950) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 17, 2016 » [Komodo](Komodo "Komodo")
* [threading](http://www.talkchess.com/forum/viewtopic.php?t=59423) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), March 03, 2016
* [lazy smp using ms vs2015 c++11 std::async](http://www.talkchess.com/forum/viewtopic.php?t=60979) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), July 29, 2016 » [Lazy SMP](Lazy_SMP "Lazy SMP") [[6]](#cite_note-6)
* [Baffling multithreading scaling behavior](http://www.talkchess.com/forum/viewtopic.php?t=61349) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), September 06, 2016


 [Re: Baffling multithreading scaling behavior](http://www.talkchess.com/forum/viewtopic.php?t=61349&start=16) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 07, 2016
* [Some hyperthreading results](http://www.talkchess.com/forum/viewtopic.php?t=61408) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 12, 2016
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")
* [Hyperthreading debate reopened?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=31863) by Zat, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2016
* [Diminishing returns and hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=62622) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), December 27, 2016 » [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength")


**2017**



* [Core behaviour](http://www.talkchess.com/forum/viewtopic.php?t=64441) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 28, 2017 » [Engine Testing](Engine_Testing "Engine Testing")
* [Lazy SMP >4 Thread Slowdown](http://www.talkchess.com/forum/viewtopic.php?t=65844) by [Can Cetin](index.php?title=Can_Cetin&action=edit&redlink=1 "Can Cetin (page does not exist)"), [CCC](CCC "CCC"), November 29, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP")


 [Re: Lazy SMP >4 Thread Slowdown](http://www.talkchess.com/forum/viewtopic.php?t=65844&start=4) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), November 29, 2017
**2018**



* [More questions about threads](http://www.talkchess.com/forum/viewtopic.php?t=67186) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), April 21, 2018 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [Stockfish and serious hardware: 384 threads](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67932) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), July 08, 2018 » [Stockfish](Stockfish "Stockfish")


**2019**



* [Hyperthreading on or off](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69658) by lovetb, [CCC](CCC "CCC"), January 20, 2019


 [Re: Hyperthreading on or off](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69658&start=5) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 20, 2019
* [Prefetch and Threading](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70586) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), April 25, 2019 » [Memory](Memory "Memory"), [Transposition Table](Transposition_Table "Transposition Table")
* [strategies for finding slowdows in lazy smp](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70919) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), June 04, 2019 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Nodes per Second](Nodes_per_Second "Nodes per Second")
* [Multithreaded noob question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71739) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 06, 2019


### 2020 ...


* [What happens with my hyperthreading?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74705) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 06, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), [NNUE](NNUE "NNUE")
* [SMP, first shot at implementation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75088) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 12, 2020 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Memory management and threads](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75116) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 15, 2020 » [Memory](Memory "Memory")
* [Very Lazy SMP and worker threads](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75151) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 18, 2020 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Dispelling the Myth of NNUE with LazySMP: An Analysis](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76190) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 30, 2020 » [NNUE](NNUE "NNUE"), [Lazy SMP](Lazy_SMP "Lazy SMP")


**2021**



* [Missing input in ponder](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77088) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), April 15, 2021 » [UCI](UCI "UCI"), [Pondering](Pondering "Pondering")
* [Thread overhead in C++](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77142) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), April 21, 2021
* [Listening for GUI input when searching](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77189) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 27, 2021 » [GUI](GUI "GUI"), [Search](Search "Search"), [UCI](UCI "UCI")
* [Single core?](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78548) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), October 30, 2021


**2022**



* [Stockfish search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79588) by Werewolf, [CCC](CCC "CCC"), March 26, 2022 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Stockfish](Stockfish "Stockfish")


## External Links


### Thread


* [Thread (computing) from Wikipedia](https://en.wikipedia.org/wiki/Thread_%28computing%29)
* [Thread safety from Wikipedia](https://en.wikipedia.org/wiki/Thread_safety)
* [Thread pool pattern from Wikipedia](https://en.wikipedia.org/wiki/Thread_pool_pattern)
* [Thread-local storage from Wikipedia](https://en.wikipedia.org/wiki/Thread-local_storage)
* [Light-weight process from Wikipedia](https://en.wikipedia.org/wiki/Light-weight_process)
* [Fiber (computer science) from Wikipedia](https://en.wikipedia.org/wiki/Fiber_%28computer_science%29)
* [Green threads from Wikipedia](https://en.wikipedia.org/wiki/Green_threads)
* [Coroutines from Wikipedia](https://en.wikipedia.org/wiki/Coroutine)
* [Open Directory - Computers: Programming: Threads](http://www.dmoz.org/Computers/Programming/Threads/)
* [Thread (disambiguation page) from Wikipedia](https://en.wikipedia.org/wiki/Thread)
* [Phish](Category:Phish "Category:Phish") - Thread, [Sigma Oasis](https://en.wikipedia.org/wiki/Sigma_Oasis) (2020),[YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
### Multithreading


* [Multithreading from Wikipedia](https://en.wikipedia.org/wiki/Multithreading_%28computer_architecture%29)
* [Simultaneous multithreading from Wikipedia](https://en.wikipedia.org/wiki/Simultaneous_multithreading)
* [Temporal multithreading from Wikipedia](https://en.wikipedia.org/wiki/Temporal_multithreading)
* [Processor affinity from Wikipedia](https://en.wikipedia.org/wiki/Processor_affinity)
* [Super-threading from Wikipedia](https://en.wikipedia.org/wiki/Super-threading)
* [Hyper-threading from Wikipedia](https://en.wikipedia.org/wiki/Hyper-threading)


### Posix


* [Native POSIX Thread Library from Wikipedia](https://en.wikipedia.org/wiki/Native_POSIX_Thread_Library)
* [GNU Portable Threads](https://en.wikipedia.org/wiki/GNU_Portable_Threads)
* [LinuxThreads from Wikipedia](https://en.wikipedia.org/wiki/LinuxThreads)
* [FSU Pthread from Wikipedia](https://en.wikipedia.org/wiki/FSU_Pthreads)
* [POSIX threads explained](http://www.ibm.com/developerworks/library/l-posix1/index.html) by [Daniel Robbins](http://www.ibm.com/developerworks/library/l-posix1/index.html#author1), [IBM developerWorks](http://www.ibm.com/developerworks/)
* [POSIX Threads (pthreads) for Win32](http://sourceware.org/pthreads-win32/) (win64 [[7]](#cite_note-7))


### [Windows](Windows "Windows")


* [Using Processes and Threads](http://msdn.microsoft.com/en-us/library/windows/desktop/ms686937%28v=VS.85%29.aspx), [Windows Desktop Development](http://msdn.microsoft.com/en-us/windows/desktop)


 [Creating Threads](http://msdn.microsoft.com/en-us/library/windows/desktop/ms682516%28v=vs.85%29.aspx)
* [Processes and Threads, MSDN](http://msdn.microsoft.com/en-us/library/ms684841%28v=VS.85%29.aspx)
* [\_beginthread, \_beginthreadex, MSDN](http://msdn.microsoft.com/en-us/library/kdzttdcb%28v=VS.100%29.aspx)
* [Thread Class (System.Threading) .NET. MSDN](http://msdn.microsoft.com/en-us/library/system.threading.thread.aspx)
* [Win32 Thread Information Block from Wikipedia](https://en.wikipedia.org/wiki/Win32_Thread_Information_Block)
* [Windows API Tutorial: Using Threads](http://www.relisoft.com/win32/active.html), [Reliable Software](http://www.relisoft.com/index.htm)
* [Processes, Threads, and Jobs](http://download.microsoft.com/download/5/b/3/5b38800c-ba6e-4023-9078-6e9ce2383e65/c06x1116607.pdf) (pdf) from [Microsoft® Windows® Internals, Fourth Edition: Windows 2000, Windows XP, and Windows Server 2003](http://www.microsoft.com/learning/en/us/book.aspx?ID=6710&locale=en-us) by [David Solomon](http://www.solsem.com/) and [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich)


### [C++](Cpp "Cpp")


* [Brief Review to C++ / Process / Thread](http://ludwig.csie.ncku.edu.tw/members/alvin/2010_9/ESL/C++_Process_2010.pdf) (pdf)
* [JThreads/C++ - “Java-like Threads for C++”](http://ftp.dreamtime.org/pub/programming/c++/orbacus-jtc/2.0/JTC-2.0.0.pdf) (pdf)
* [Chapter 24. Thread - Boost 1.47.0](http://www.boost.org/doc/libs/1_47_0/doc/html/thread.html) by [Anthony Williams](http://stackoverflow.com/users/5597/anthony-williams)
* [Qt 4.7: Thread Support in Qt](http://doc.qt.nokia.com/latest/threads.html)
* [Input thread, code](http://alaric.fendrich.se/Downloads.html#Topic7) from [Alaric](Alaric "Alaric") Downloads by [Peter Fendrich](Peter_Fendrich "Peter Fendrich")
* [TinyThread++ - Portable thread library for C++](http://tinythreadpp.bitsnbites.eu/) [[8]](#cite_note-8)


### [Java](Java "Java")


* [Thread (Java 2 Platform SE 5.0)](http://download.oracle.com/javase/1.5.0/docs/api/java/lang/Thread.html)
* [Processes and Threads (The Java™ Tutorials > Essential Classes > Concurrency)](http://docs.oracle.com/javase/tutorial/essential/concurrency/procthread.html)


### [GPU](GPU "GPU")


* [Parallel Thread Execution from Wikipedia](https://en.wikipedia.org/wiki/Parallel_Thread_Execution) » [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")


## References


1. [↑](#cite_ref-1) [Thread (computing) from Wikipedia](https://en.wikipedia.org/wiki/Thread_%28computing%29)
2. [↑](#cite_ref-2) [Re: lazy smp using ms vs2015 c++11 std::async](http://www.talkchess.com/forum/viewtopic.php?t=60979&start=4) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 31, 2016
3. [↑](#cite_ref-3) [Information on the C++11 Memory Model](http://scottmeyers.blogspot.co.uk/2012/04/information-on-c11-memory-model.html) by [Scott Meyers](https://en.wikipedia.org/wiki/Scott_Meyers), April 24, 2012
4. [↑](#cite_ref-4) [Georg Hager's Blog | Random thoughts on High Performance Computing](https://blogs.fau.de/hager/)
5. [↑](#cite_ref-5) [TinyThread++ - Portable thread library for C++](http://tinythreadpp.bitsnbites.eu/)
6. [↑](#cite_ref-6) [std::async - cppreference.com](http://en.cppreference.com/w/cpp/thread/async)
7. [↑](#cite_ref-7) [pthread-win32\_x64.zip - libusb-winusb-wip](https://code.google.com/p/libusb-winusb-wip/downloads/detail?name=pthread-win32_x64.zip&can=2&q=)
8. [↑](#cite_ref-8) [TinyThread++](http://www.talkchess.com/forum/viewtopic.php?t=53063) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), July 24, 2014

**[Up one Level](Programming "Programming")**







 
