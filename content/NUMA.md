---
title: NUMA
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [Memory](Memory "Memory") \* NUMA**



[ Possible NUMA system <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**NUMA**, (Non-uniform memory access)  

a [multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing) memory design where the main memory is partitioned between processors. Opposed to [SMP](SMP "SMP"), where all processors compete for access to the centralized shared [memory bus](https://en.wikipedia.org/wiki/Memory_bus), making it difficult to scale well bejoind 8 to 12 CPUs <a id="cite-note-2" href="#cite-ref-2">[2]</a>, NUMA splits the main memory into so called nodes with separate memory busses for subsets of processors, and high speed interconnection between nodes, either directly in so called 1-hop distance, or indirectly in 2-hop distance. Despite the high speed interconnection, NUMA memory access time varies considerably between faster local memory and remote memory of other nodes. Maintaining [cache coherence](https://en.wikipedia.org/wiki/Cache_coherence) of processor caches adds significant overhead to NUMA Systems, addressed by [ccNUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access#Cache_coherent_NUMA_.28ccNUMA.29) which is mostly used synonymous for current NUMA implementations <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### Contents


* [1 x86](#x86)
* [2 Considerations](#considerations)
* [3 See also](#see-also)
* [4 Selected Publications](#selected-publications)
	+ [4.1 1998 ...](#1998-...)
	+ [4.2 2000 ...](#2000-...)
	+ [4.3 2010 ...](#2010-...)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2000 ...](#2000-...-2)
	+ [5.2 2010 ...](#2010-...-2)
	+ [5.3 2015 ...](#2015-...)
* [6 External Links](#external-links)
	+ [6.1 Linux](#linux)
	+ [6.2 Windows](#windows)
	+ [6.3 x86](#x86-2)
	+ [6.4 Misc](#misc)
* [7 References](#references)






[AMD](AMD "AMD") implemented NUMA with its [Opteron](X86-64 "X86-64") processor in 2003, using [HyperTransport](https://en.wikipedia.org/wiki/HyperTransport). [Intel](Intel "Intel") announced NUMA compatibility for their [x86](X86 "X86") servers in late 2007 with [Nehalem CPUs](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture)) using [QuickPath Interconnect](https://en.wikipedia.org/wiki/Intel_QuickPath_Interconnect) <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Considerations


Scheduling of [threads](Thread "Thread") across nodes and cores of a system is a complicated topic due to access of independent or shared data. There are several considerations in ccNUMA aware [operating systems](https://en.wikipedia.org/wiki/Operating_system) and software, such as keeping data local by virtue of first touch <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. NUMA and [processor affinity](https://en.wikipedia.org/wiki/Processor_affinity) [APIs](https://en.wikipedia.org/wiki/Application_programming_interface) help application programmers to bind threads or processes to NUMA nodes or to allocate memory from a certain node.



## See also


* [Optimization](Optimization "Optimization")
* [Parallel Search](Parallel_Search "Parallel Search")
* [SMP](SMP "SMP")
* [Thread](Thread "Thread")


## Selected Publications


### 1998 ...


* [Ante Grbić](https://www.linkedin.com/in/ante-grbi%C4%87-0657665b/), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Steve Caranci](https://dblp.uni-trier.de/pers/hd/c/Caranci:S=), [Robin Grindley](https://www.linkedin.com/in/robin-grindley-47550/), [Mitchell Gusat](https://dblp.uni-trier.de/pers/hd/g/Gusat:Mitchell), [Guy Lemieux](http://www.ece.ubc.ca/~lemieux/), [K. Loveless](https://dblp.uni-trier.de/pers/hd/l/Loveless:K=), [Naraig Manjikian](https://dblp.uni-trier.de/pers/hd/m/Manjikian:Naraig), [Sinisa Srbljic](https://www.linkedin.com/in/sinisasrbljic/), [Michael Stumm](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=67137), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**1998**). *[Design and Implementation of the NUMAchine Multiprocessor](https://ieeexplore.ieee.org/document/724441/)*. [DAC 1998](https://dblp.uni-trier.de/db/conf/dac/dac98.html), [pdf](http://www.eecg.toronto.edu/parallel/parallel/docs/dac98.pdf) <a id="cite-note-7" href="#cite-ref-7">[7]</a>


### 2000 ...


* [Robin Grindley](https://www.linkedin.com/in/robin-grindley-47550/), [Tarek Abdelrahman](http://www.eecg.toronto.edu/~tsa/), [Stephen Brown](http://www.eecg.toronto.edu/%7Ebrown/), [Steve Caranci](https://dblp.uni-trier.de/pers/hd/c/Caranci:S=), [D. DeVries](https://dblp.uni-trier.de/pers/hd/d/DeVries:D=), [Benjamin Gamsa](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=67177), [Ante Grbić](https://www.linkedin.com/in/ante-grbi%C4%87-0657665b/), [Mitchell Gusat](https://dblp.uni-trier.de/pers/hd/g/Gusat:Mitchell), [R. Ho](https://dblp.uni-trier.de/pers/hd/h/Ho:R=), [Orran Krieger](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=99397), [Guy Lemieux](http://www.ece.ubc.ca/~lemieux/), [K. Loveless](https://dblp.uni-trier.de/pers/hd/l/Loveless:K=), [Naraig Manjikian](https://dblp.uni-trier.de/pers/hd/m/Manjikian:Naraig), [P. McHardy](https://dblp.uni-trier.de/pers/hd/m/McHardy:P=), [Sinisa Srbljic](https://www.linkedin.com/in/sinisasrbljic/), [Michael Stumm](https://www.genealogy.math.ndsu.nodak.edu/id.php?id=67137), [Zvonko Vranesic](Zvonko_Vranesic "Zvonko Vranesic"), [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic") (**2000**). *The NUMAchine Multiprocessor*. [ICPP 2000](https://dblp.uni-trier.de/db/conf/icpp/icpp2000.html), [pdf](http://www.eecg.toronto.edu/parallel/parallel/docs/icpp00.pdf)
* [Andi Kleen](http://www.halobates.de/) (**2004**). *An NUMA API for Linux*. SUSE Labs, [pdf](http://halobates.de/numaapi3.pdf)
* [Ulrich Drepper](http://de.wikipedia.org/wiki/Ulrich_Drepper) (**2007**). *What Every Programmer Should Know About Memory*. [pdf](http://www.akkadia.org/drepper/cpumemory.pdf), also hosted by [LWN.net](https://en.wikipedia.org/wiki/LWN.net)


 [Memory part 1](http://lwn.net/Articles/250967/)
 [Memory part 2: CPU caches](http://lwn.net/Articles/252125/)
 [Memory part 3: Virtual Memory](http://lwn.net/Articles/253361/)
* [Memory part 4: NUMA support](http://lwn.net/Articles/254445/)


 [Memory part 5: What programmers can do](http://lwn.net/Articles/255364/)
### 2010 ...


* [Nakul Manchanda](https://www.linkedin.com/in/nakulmanchanda), [Karan Anand](https://www.linkedin.com/in/anandkaran) (**2010**). *Non-Uniform Memory Access (NUMA)*. [New York University](https://en.wikipedia.org/wiki/New_York_University), [pdf](http://cs.nyu.edu/~lerner/spring10/projects/NUMA.pdf)
* [Stefan Lankes](https://scholar.google.de/citations?user=wx0D5q0AAAAJ&hl=en), [Thomas Roehl](https://www.researchgate.net/profile/Thomas_Roehl), [Christian Terboven](https://terboven.com/), [Thomas Bemmerl](https://www.linkedin.com/in/thomas-bemmerl-b3657547) (**2012**). *[Node-Based Memory Management for Scalable NUMA Architectures](http://publications.rwth-aachen.de/record/207349)*. [RWTH Aachen](https://en.wikipedia.org/wiki/RWTH_Aachen_University), [ROSS 2012](http://www.mcs.anl.gov/events/workshops/ross/2012/), [slides as pdf](http://htor.inf.ethz.ch/ross2012/slides/ross2012-lankes.pdf)
* [Georg Hager](https://www.rrze.fau.de/wir-ueber-uns/organigramm/mitarbeiter/index.shtml/georg-hager.shtml) <a id="cite-note-8" href="#cite-ref-8">[8]</a>, [Jan Treibig](http://dblp.uni-trier.de/pers/hd/t/Treibig:Jan), [Gerhard Wellein](http://dblp.uni-trier.de/pers/hd/w/Wellein:Gerhard) (**2013**). *The Practitioner's Cookbook for Good Parallel Performance on Multi- and Many-Core Systems*. [RRZE](https://de.wikipedia.org/wiki/Regionales_Rechenzentrum_Erlangen), [SC13](http://sc13.supercomputing.org/), [slides as pdf](https://blogs.fau.de/hager/files/2013/11/sc13_tutorial_134.pdf)
* [Rik van Riel](https://www.linkedin.com/in/rikvanriel), [Vinod Chegu](https://www.linkedin.com/in/chegu) (**2014**). *Automatic NUMA Balancing*. [Red Hat Summit 2014](https://www.redhat.com/en/about/press-releases/red-hat-announces-dates-for-red-hat-summit-2014-in-san-francisco), [slides as pdf](http://events.linuxfoundation.org/sites/events/files/slides/summit2014_riel_chegu_w_0340_automatic_numa_balancing_0.pdf), [video lecture](https://youtu.be/mjVw_oe1hEA) by Rik van Riel
* [Irina Calciu](https://scholar.google.com/citations?user=5aWoGywAAAAJ&hl=en), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Mahesh Balakrishnan](Mathematician#MBalakrishnan "Mathematician"), [Marcos K. Aguilera](Mathematician#MKAguilera "Mathematician") (**2017**). *[Black-box Concurrent Data Structures for NUMA Architectures](https://dl.acm.org/doi/10.1145/3093336.3037721)*. [ACM SIGPLAN Notices](ACM#SIGPLAN "ACM"), Vol. 52, No. 4, [pdf](https://cs.brown.edu/people/irina/papers/asplos2017-final.pdf)
* [Irina Calciu](https://scholar.google.com/citations?user=5aWoGywAAAAJ&hl=en), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Mahesh Balakrishnan](Mathematician#MBalakrishnan "Mathematician"), [Marcos K. Aguilera](Mathematician#MKAguilera "Mathematician") (**2017**). *[How to implement any concurrent data structure for modern servers](https://dl.acm.org/doi/10.1145/3139645.3139650)*. [ACM SIGOPS](ACM#SIGOPS "ACM"), Vol. 51, No. 1
* [Irina Calciu](https://scholar.google.com/citations?user=5aWoGywAAAAJ&hl=en), [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen"), [Mahesh Balakrishnan](Mathematician#MBalakrishnan "Mathematician"), [Marcos K. Aguilera](Mathematician#MKAguilera "Mathematician") (**2018**). *[How to implement any concurrent data structure](https://cacm.acm.org/magazines/2018/12/232880-how-to-implement-any-concurrent-data-structure/fulltext)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 61, No. 12


## Forum Posts


### 2000 ...


* [DTS NUMA](https://www.stmintz.com/ccc/index.php?id=249651) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), September 03, 2002 » [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [What's the difference between NUMA, SMP and MPI for chess?](https://www.stmintz.com/ccc/index.php?id=360103) by [Joachim Rang](index.php?title=Joachim_Rang&action=edit&redlink=1 "Joachim Rang (page does not exist)"), [CCC](CCC "CCC"), April 15, 2004 » [SMP](SMP "SMP")
* [Opteron NUMA/SMP question](https://www.stmintz.com/ccc/index.php?id=410357) by Matthew Hull, [CCC](CCC "CCC"), February 09, 2005


### 2010 ...


* [optimizing performance on dual Xeon systems (NUMA)](http://www.talkchess.com/forum/viewtopic.php?t=47367) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 28, 2013
* [Smp concepts](http://www.talkchess.com/forum/viewtopic.php?t=52503) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), June 01, 2014 » [SMP](SMP "SMP")


### 2015 ...


* [NUMA-awareness](http://www.talkchess.com/forum/viewtopic.php?t=55467) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 25, 2015
* [thread affinity](http://www.talkchess.com/forum/viewtopic.php?t=56858) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), July 03, 2015 » [Thread](Thread "Thread")


 [Re: thread affinity](http://www.talkchess.com/forum/viewtopic.php?t=56858&start=3) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 03, 2015
* [Actual speedups from YBWC and ABDADA on 8+ core machines?](http://www.talkchess.com/forum/viewtopic.php?t=56937) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 10, 2015 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [ABDADA](ABDADA "ABDADA")
* [NUMA 101](http://www.talkchess.com/forum/viewtopic.php?t=58830) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2016 » [Crafty](Crafty "Crafty")
* [NUMA in a YBWC implementation](http://www.talkchess.com/forum/viewtopic.php?t=60875) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 20, 2016 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [lets get the ball moving down the field on numa awareness](https://groups.google.com/d/msg/fishcooking/ezt6MrAuXqs/qIR2HEciEgAJ) by [Mohammed Li](index.php?title=Mohammed_Li&action=edit&redlink=1 "Mohammed Li (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), August 30, 2016
* [search thread memory allocation (NUMA)](https://groups.google.com/d/msg/fishcooking/bcFKVr85fIQ/Z6-hoGcKFAAJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 06, 2016
* [What do you do with NUMA?](http://www.talkchess.com/forum/viewtopic.php?t=61472) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 19, 2016
* [NUMA test compilation](https://groups.google.com/d/msg/fishcooking/7hHC075ZnnM/IaITCiLaBwAJ) by Joachim Müller, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2016 » [Stockfish](Stockfish "Stockfish")
* [What Linux compatible Numa aware engines are available?](http://www.talkchess.com/forum/viewtopic.php?t=63581) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 29, 2017 » [Linux](Linux "Linux")
* [Ethereal 10.88 NUMA](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68293) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), August 24, 2018 » [Ethereal](Ethereal "Ethereal")
* [Some NUMA data for Stockfish-dev and Cfish-dev](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71027) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), June 17, 2019 » [Stockfish](Stockfish "Stockfish"), [CFish](CFish "CFish")
* [NUMA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72689) by lucasart, [CCC](CCC "CCC"), December 30, 2019


## External Links


* [Non-Uniform Memory Access (NUMA) from Wikipedia](https://en.wikipedia.org/wiki/Non-uniform_memory_access)
* [NUMA Frequently Asked Questions](http://lse.sourceforge.net/numa/faq/)
* [Multiprocessing - OSDev Wiki](http://wiki.osdev.org/Multiprocessing)
* [ccNUMA machines](http://netlib.org/utk/papers/advanced-computers/ccnuma.html) in [Aad J. van der Steen](index.php?title=Aad_J._van_der_Steen&action=edit&redlink=1 "Aad J. van der Steen (page does not exist)"), [Jack Dongarra](Mathematician#JDongarra "Mathematician") (**2004**). *[Overview of Recent Supercomputers](http://netlib.org/utk/papers/advanced-computers/overview.html)*.


### [Linux](Linux "Linux")


* [numa(7) - Linux manual page](http://man7.org/linux/man-pages/man7/numa.7.html)
* [A NUMA API for Linux](http://developer.amd.com/wordpress/media/2012/10/LibNUMA-WP-fv1.pdf) (pdf, April 2015)


### [Windows](Windows "Windows")


* [Allocating Memory from a NUMA Node, MSDN](http://msdn.microsoft.com/en-us/library/aa965223%28v=VS.85%29.aspx)
* [NUMA Support (Windows), MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363804(v=vs.85).aspx)
* [Processor Groups (Windows), MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405503)


### [x86](X86 "X86")


* [Optimizing Applications for NUMA | Intel® Developer Zone](http://software.intel.com/en-us/articles/optimizing-applications-for-numa)
* [Performance Guidelines for AMD Athlon™ 64 and AMD Opteron™ ccNUMA Multiprocessor Systems](https://doc.xdevs.com/doc/AMD/_Performance/Performance%20Guidelines%20for%20AMD%20Athlon%2064%20and%20AMD%20Opteron%20ccNUMA%20Multiprocessor%20Systems.%20rev.3.00%5D.%5B2006-06%5D.pdf) (pdf)


### Misc


* [The Who](Category:The_Who "Category:The Who") - [Magic Bus](https://en.wikipedia.org/wiki/Magic_Bus_(song)), [Live at Leeds](https://en.wikipedia.org/wiki/Live_at_Leeds) (1970), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> One possible architecture of a NUMA system. Originally created in [Visio 2010](https://en.wikipedia.org/wiki/Microsoft_Visio), cleaned up with [Inkscape](https://en.wikipedia.org/wiki/Inkscape), by Moop2000, October 4, 2010, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [NUMA Frequently Asked Questions - 9. Why should I use NUMA? What are the benefits of NUMA?](http://lse.sourceforge.net/numa/faq/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [NUMA Frequently Asked Questions - 4. What is the difference between NUMA and ccNUMA?](http://lse.sourceforge.net/numa/faq/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Non-Uniform Memory Access (NUMA) from Wikipedia](https://en.wikipedia.org/wiki/Non-uniform_memory_access)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Performance Guidelines for AMD Athlon™ 64 and AMD Opteron™ ccNUMA Multiprocessor Systems](https://doc.xdevs.com/doc/AMD/_Performance/Performance%20Guidelines%20for%20AMD%20Athlon%2064%20and%20AMD%20Opteron%20ccNUMA%20Multiprocessor%20Systems.%20rev.3.00%5D.%5B2006-06%5D.pdf) (pdf) - 3.2.1 Keeping Data Local by Virtue of first Touch, pp. 22
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: thread affinity](http://www.talkchess.com/forum/viewtopic.php?t=56858&start=3) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 03, 2015
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Documentation on the NUMAchine Multiprocessor](http://www.eecg.toronto.edu/parallel/parallel/numadocs.html)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Georg Hager's Blog | Random thoughts on High Performance Computing](https://blogs.fau.de/hager/)

**[Up one Level](Memory "Memory")**







 
