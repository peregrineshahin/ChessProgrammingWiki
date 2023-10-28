---
title: SMP
---
**[Home](Home "Home") \* [Hardware](Hardware "Hardware") \* [Memory](Memory "Memory") \* SMP**



[ Symmetric Multiprocessor System <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SMP**, (**S**ymmetric **M**ulti**P**rocessing)  

a [multiprocessing](https://en.wikipedia.org/wiki/Multiprocessing) memory design where all processors compete for access to the centralized shared [memory bus](https://en.wikipedia.org/wiki/Memory_bus) connected to the main memory as used in early microcomputer multiprocessor systems with two, four or even eight processors. SMP includes systems with CPUs implemented in separate chips, systems with CPUs implemented in the same chip ([multi-core](https://en.wikipedia.org/wiki/Multi-core_processor)) and combinations (e.g. a system with 2 separate quad core chips, with a total of 8 physical CPUs) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. With increasing number of cores and processors bejoind 8 to 12 CPUs <a id="cite-note-3" href="#cite-ref-3">[3]</a>, SMP with its [uniform memory access](https://en.wikipedia.org/wiki/Uniform_memory_access) becomes more and more a bottleneck in scalability - more recent systems such as [x86-64](X86-64 "X86-64") with multiple cores use the [NUMA](NUMA "NUMA") (Non-uniform memory access) architecture instead. Nevertheless, the term *SMP search* has become synonym for [parallel search](Parallel_Search "Parallel Search") using a [shared hash table](Shared_Hash_Table "Shared Hash Table"), also manifested in the term [Lazy SMP](Lazy_SMP "Lazy SMP"). 



### Contents


* [1 See also](#see-also)
* [2 Publications](#publications)
* [3 Forum Posts](#forum-posts)
	+ [3.1 1997 ...](#1997-...)
	+ [3.2 2000 ...](#2000-...)
	+ [3.3 2005 ...](#2005-...)
	+ [3.4 2010](#2010)
	+ [3.5 2015](#2015)
* [4 External Links](#external-links)
* [5 References](#references)






* [ABDADA](ABDADA "ABDADA")
* [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [NUMA](NUMA "NUMA")
* [Parallel Search](Parallel_Search "Parallel Search")
* [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


## Publications


* [James Swafford](James_Swafford "James Swafford") (**2008**). *A Survey of Parallel Search Algorithms over Alpha-Beta Search Trees using Symmetric Multiprocessor Machines*. Masters Project, [East Carolina University](https://en.wikipedia.org/wiki/East_Carolina_University), advisor [Ronnie Smith](http://www.cs.ecu.edu/rws/)


## Forum Posts


### 1997 ...


* [A parallel processing chess program for the 'Wintel' platform](https://groups.google.com/d/msg/rec.games.chess.computer/OUBw5LIIkoc/5VBOqmfdIrsJ) by [Ian Kennedy](Ian_Kennedy "Ian Kennedy"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 9, 1997 » [Psycho](Psycho "Psycho")
* [Parallel Crafty](https://www.stmintz.com/ccc/index.php?id=15912) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 19, 1998  » [Crafty](Crafty "Crafty")
* [Current Crafty strength on SMP?](https://groups.google.com/d/msg/rec.games.chess.computer/C6z6Nnh2Nbs/G3LOexi_PMUJ) by Charlton Harrison, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 29, 1998


### 2000 ...


* [What is SMP](https://groups.google.com/d/msg/rec.games.chess.computer/8_wgVAzN-m0/APpMSjRY7a8J) by Hyattian Flu, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August, 12, 2001
* [To SMP or not to SMP what's the answer?](https://www.stmintz.com/ccc/index.php?id=292788) by Jonas Bylund, [CCC](CCC "CCC"), April 10, 2003
* [SMP Engines](https://www.stmintz.com/ccc/index.php?id=304318) by Peter Stayne, [CCC](CCC "CCC"), July 02, 2003
* [Crafty SMP questions](https://www.stmintz.com/ccc/index.php?id=310051) by Matthew Hull, [CCC](CCC "CCC"), August 05, 2003 » [Crafty](Crafty "Crafty")
* [Linux SMP](https://www.stmintz.com/ccc/index.php?id=313638) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), August 31, 2003
* [is this a sign of broken smp](https://www.stmintz.com/ccc/index.php?id=353751) by [Michael Byrne](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), March 09, 2004 » [Crafty](Crafty "Crafty")
* [What's the difference between NUMA, SMP and MPI for chess?](https://www.stmintz.com/ccc/index.php?id=360103) by [Joachim Rang](index.php?title=Joachim_Rang&action=edit&redlink=1 "Joachim Rang (page does not exist)"), [CCC](CCC "CCC"), April 15, 2004


### 2005 ...


* [Opteron NUMA/SMP question](https://www.stmintz.com/ccc/index.php?id=410357) by Matthew Hull, [CCC](CCC "CCC"), February 09, 2005
* [Glaurung SMP: Beta testers with dual Macs or Linux boxes wanted](https://www.stmintz.com/ccc/index.php?id=488055) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 20, 2006 » [Glaurung](Glaurung "Glaurung")
* [Glaurung SMP: Now also for Windows!](https://www.stmintz.com/ccc/index.php?id=488783) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 23, 2006


 [Re: What is SMP? (NT)](https://www.stmintz.com/ccc/index.php?id=488795) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 23, 2006
* [re-inventing the SMP wheel](http://www.talkchess.com/forum/viewtopic.php?t=15809) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 15, 2007
* [SMP thread goes here](http://www.talkchess.com/forum/viewtopic.php?t=16122) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 29, 2007
* [If making an SMP engine, do NOT use processes](http://www.talkchess.com/forum/viewtopic.php?t=19446) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), February 07, 2008
* [Authors of WinBoard SMP engines, take note!](http://www.talkchess.com/forum/viewtopic.php?t=24327) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 11, 2008 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [UCI protocol and SMP](http://www.talkchess.com/forum/viewtopic.php?t=24866) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), November 13, 2008 » [UCI](UCI "UCI")
* [Appeal to SMP-engines programmers using UCI](http://www.talkchess.com/forum/viewtopic.php?t=25908) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 09, 2009
* [SMP rating influence](http://www.talkchess.com/forum/viewtopic.php?t=25955) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 12, 2009
* [SMP and helpfull master concept](http://www.talkchess.com/forum/viewtopic.php?t=26057) by hcyrano, [CCC](CCC "CCC"), January 16, 2009
* [SMP hashing problem](http://www.talkchess.com/forum/viewtopic.php?t=26208) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 24, 2009 » [Lockless Hashing](Shared_Hash_Table#Lockless "Shared Hash Table")
* [SMP search stability](http://www.talkchess.com/forum/viewtopic.php?t=26211) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 24, 2009


### 2010


* [SMP basics](http://www.talkchess.com/forum/viewtopic.php?t=33700) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), April 09, 2010
* [SMP speed up](http://www.talkchess.com/forum/viewtopic.php?t=36082) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), September 14, 2010
* [SMP questions](http://www.talkchess.com/forum/viewtopic.php?t=36121) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 19, 2010
* [AMD Phenom Hex core (SMP performance problem)](http://www.talkchess.com/forum/viewtopic.php?t=38655) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 04, 2011
* [SMP for Android UCI engines](http://www.talkchess.com/forum/viewtopic.php?t=38753) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 14, 2011 » [Android](Android "Android")
* [Questions on SMP search](http://www.talkchess.com/forum/viewtopic.php?t=38808) by [Ben-Hur Carlos Vieira Langoni Junior](Ben-Hur_Carlos_Vieira_Langoni_Junior "Ben-Hur Carlos Vieira Langoni Junior"), [CCC](CCC "CCC"), April 21, 2011
* [SMP question](http://www.talkchess.com/forum/viewtopic.php?t=39305) by [Stef Luijten](index.php?title=Stef_Luijten&action=edit&redlink=1 "Stef Luijten (page does not exist)"), [CCC](CCC "CCC"), June 08, 2011
* [Anyone try MS VS2010 C++ parallel pattern libray to do SMP ?](http://www.talkchess.com/forum/viewtopic.php?t=39349) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), June 12, 2011
* [First steps with SMP](http://www.talkchess.com/forum/viewtopic.php?t=41270) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), November 30, 2011
* [SMP and questions](http://www.talkchess.com/forum/viewtopic.php?t=46124) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), November 23, 2012
* [SMP experts advice needed](http://www.talkchess.com/forum/viewtopic.php?t=46589) by Lucas Braesch, [CCC](CCC "CCC"), December 27, 2012
* [Lazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=46597) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), December 27, 2012
* [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
* [Lazy SMP, part 3](http://www.talkchess.com/forum/viewtopic.php?t=47455) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 09, 2013
* [Shared hash table smp result](http://www.talkchess.com/forum/viewtopic.php?t=47568) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 21, 2013
* [Measure of SMP scalability](http://www.talkchess.com/forum/viewtopic.php?t=48524) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 03, 2013
* [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013 » [Lazy SMP](EXchess#LazySMP "EXchess") in [EXchess](EXchess "EXchess")
* [Interesting SMP bug](http://www.talkchess.com/forum/viewtopic.php?t=49450) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 24, 2013
* [SMP and Thread Pool Design pattern](http://www.talkchess.com/forum/viewtopic.php?t=49540) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), October 02, 2013 » [Hannibal](Hannibal "Hannibal")
* [Smp concepts](http://www.talkchess.com/forum/viewtopic.php?t=52503) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), June 01, 2014


### 2015


* [SMP: on same branch instead splitting?](http://www.talkchess.com/forum/viewtopic.php?t=55047) by Frank Ludwig, [CCC](CCC "CCC"), January 23, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Some SMP measurements with Rookie v3](http://www.talkchess.com/forum/viewtopic.php?t=55224) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), February 05, 2015
* [SMP questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=55779) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), March 25, 2015 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [Latest SMP update](http://www.talkchess.com/forum/viewtopic.php?t=56920) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 09, 2015 » [Crafty](Crafty "Crafty")
* [Actual speedups from YBWC and ABDADA on 8+ core machines?](http://www.talkchess.com/forum/viewtopic.php?t=56937) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [CCC](CCC "CCC"), July 10, 2015 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [ABDADA](ABDADA "ABDADA")
* [New SMP stuff (particularly Kai)](http://www.talkchess.com/forum/viewtopic.php?t=57036) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 20, 2015
* [SMP (new style)](http://www.talkchess.com/forum/viewtopic.php?t=57039) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 20, 2015
* [Measuring SMP "effciency"](http://www.talkchess.com/forum/viewtopic.php?t=57088) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), July 26, 2015


**2016**



* [Crafty SMP measurement](http://www.talkchess.com/forum/viewtopic.php?t=59745) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), April 04, 2016 » [Crafty](Crafty "Crafty")
* [Crazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=60537) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 19, 2016


**2017**



* [Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum/viewtopic.php?t=63903) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 05, 2017 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Symmetric multiprocessing (SMP) scaling - K10.4 Contempt=0](http://www.talkchess.com/forum/viewtopic.php?t=63955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 11, 2017 » [Komodo](Komodo "Komodo"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Symmetric multiprocessing (SMP) scaling - SF8 Contempt=10](http://www.talkchess.com/forum/viewtopic.php?t=63967) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 13, 2017 » SMP, [Stockfish](Stockfish "Stockfish"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Time Managment translating to SMP](http://www.talkchess.com/forum/viewtopic.php?t=66099) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 23, 2017  » [Parallel Search](Parallel_Search "Parallel Search"), [Time Management](Time_Management "Time Management")


## External Links


* [Symmetric multiprocessing from Wikipedia](https://en.wikipedia.org/wiki/Symmetric_multiprocessing)


 [Symmetric multiprocessor system from Wikipedia](https://en.wikipedia.org/wiki/Symmetric_multiprocessor_system)
* [Uniform memory access from Wikipedia](https://en.wikipedia.org/wiki/Uniform_memory_access)
* [Symmetric Multiprocessing - OSDev Wiki](http://wiki.osdev.org/Symmetric_Multiprocessing)
* [Chapter 13. Symmetric Multi Processing](http://www.tldp.org/LDP/lkmpg/2.4/html/c1294.htm) in [Peter Jay Salzman](https://en.wikipedia.org/wiki/Peter_J._Salzman), [Ori Pomerantz](https://www.linkedin.com/in/ori-pomerantz-34a915) (**2001**). *[The Linux Kernel Module Programming Guide](http://www.tldp.org/LDP/lkmpg/2.4/html/book1.htm)*. » [Linux](Linux "Linux")
* [Björk](Category:Bj%C3%B6rk "Category:Björk") - [Mutual Core](https://en.wikipedia.org/wiki/Mutual_Core) (2012), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Symmetric Multiprocessor System, [image](https://commons.wikimedia.org/wiki/File:SMP_-_Symmetric_Multiprocessor_System.svg) by Ferry24.Milan, November 01, 2011, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Symmetric multiprocessing from Wikipedia](https://en.wikipedia.org/wiki/Symmetric_multiprocessing) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Symmetric Multiprocessing - OSDev Wiki](http://wiki.osdev.org/Symmetric_Multiprocessing)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [NUMA Frequently Asked Questions - 9. Why should I use NUMA? What are the benefits of NUMA?](http://lse.sourceforge.net/numa/faq/)

**[Up one Level](Memory "Memory")**







 
