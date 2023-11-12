---
title: Process
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* Process**


A **Process** is an [instance](https://en.wikipedia.org/wiki/Object_%28computer_science%29) of a [computer program](index.php?title=Program&action=edit&redlink=1 "Program (page does not exist)"), containing the program code being or about to be executed and its [data](Data "Data") in [memory](Memory "Memory"). A process owns ressources such one or more processors if running, and memory, including descriptors of allocated resources, such as [file descriptors](https://en.wikipedia.org/wiki/File_descriptor) or [handles](https://en.wikipedia.org/wiki/Handle_%28computing%29) for data sources and sinks, usually all provided by the [operating system](https://en.wikipedia.org/wiki/Operating_system). [Multitasking](https://en.wikipedia.org/wiki/Computer_multitasking) operating systems allow the simultaneous execution of multiple [threads](Thread "Thread") within one process, sharing all its common resources. Further, processes may [spawn](https://en.wikipedia.org/wiki/Spawn_%28computing%29) or [fork](https://en.wikipedia.org/wiki/Fork_%28operating_system%29) [child processes](https://en.wikipedia.org/wiki/Child_process) who inherit most of the attributes from its parent, such as open files, but otherwise have their own memory for data, heap and stack. 



## Parallel Search


In [Parallel search](Parallel_Search#ThreadsVsProcesses "Parallel Search"), multiple [threads](Thread "Thread") within one process are more common, because they are easier to debug as well as implement, provided the program does not already have lots of global variables. Processes are favored by some because the need to explicitly share memory makes subtle bugs easier to avoid. Also, in processes, the extra argument to most functions is not needed.



## See also


* [Parallel Search](Parallel_Search "Parallel Search")
* [Program](index.php?title=Program&action=edit&redlink=1 "Program (page does not exist)")
* [Sequential Logic](Sequential_Logic "Sequential Logic")
* [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [Thread](Thread "Thread")


## Forum Posts


### 2000 ,,,


* [Re: Stormx is this a Crafty Clone??](https://www.stmintz.com/ccc/index.php?id=367073) by [Sean Empey](Sean_Empey "Sean Empey"), [CCC](CCC "CCC"), May 25, 2004 » [Windows](Windows "Windows")
* [threads vs processes](http://www.talkchess.com/forum/viewtopic.php?t=22398) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 16, 2008
* [threads vs processes again](http://www.talkchess.com/forum/viewtopic.php?t=22799) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 05, 2008


### 2010 ...


* [Reading Input From a Child Process](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=35940) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), August 31, 2010
* [Reading Input from another process](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=37946) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), February 05, 2011
* [Weird Windows / WinBoard behavior](http://www.talkchess.com/forum/viewtopic.php?t=61435) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 15, 2016 » [WinBoard](WinBoard "WinBoard"), [Windows](Windows "Windows")
* [Crashing engines (Linux)](http://www.talkchess.com/forum/viewtopic.php?t=61465) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 18, 2016 » [Linux](Linux "Linux"), [XBoard](XBoard "XBoard")
* [Core behaviour](http://www.talkchess.com/forum/viewtopic.php?t=64441) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 28, 2017 » [Engine Testing](Engine_Testing "Engine Testing")


### 2020 ...


* [Killing zombies (POSIX)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75710) by lucasart, [CCC](CCC "CCC"), November 08, 2020 » [c-chess-cli](C-chess-cli "C-chess-cli")


## External Links


* [Process (computing) from Wikipedia](https://en.wikipedia.org/wiki/Process_%28computing%29)
* [Parent process from Wikipedia](https://en.wikipedia.org/wiki/Parent_process)
* [Child process from Wikipedia](https://en.wikipedia.org/wiki/Child_process)
* [Orphan process from Wikipedia](https://en.wikipedia.org/wiki/Orphan_process)
* [Zombie process from Wikipedia](https://en.wikipedia.org/wiki/Zombie_process)
* [Process state from Wikipedia](https://en.wikipedia.org/wiki/Process_state)
* [Context switch from Wikipedia](https://en.wikipedia.org/wiki/Context_switch)
* [Processor affinity from Wikipedia](https://en.wikipedia.org/wiki/Processor_affinity)
* [exit (operating system) from Wikipedia](https://en.wikipedia.org/wiki/Exit_%28operating_system%29)
* [Process management (computing) from Wikipedia](https://en.wikipedia.org/wiki/Process_management_%28computing%29)
* [Inter-process communication from Wikipedia](https://en.wikipedia.org/wiki/Inter-process_communication)
* [Shared memory from Wikipedia](https://en.wikipedia.org/wiki/Shared_memory)
* [Central processing unit from Wikipedia](https://en.wikipedia.org/wiki/Central_processing_unit)
* [Multiprocessing from Wikipedia](https://en.wikipedia.org/wiki/Multiprocessing)


### Posix


* [Process group from Wikipedia](https://en.wikipedia.org/wiki/Process_group)
* [Fork (operating system) from Wikipedia](https://en.wikipedia.org/wiki/Fork_%28operating_system%29)
* [Fork bomb from Wikipedia](https://en.wikipedia.org/wiki/Fork_bomb)
* [ps (Unix) from Wikipedia](https://en.wikipedia.org/wiki/Ps_%28Unix%29)


 [Pstree from Wikipedia](https://en.wikipedia.org/wiki/Pstree)
 [kill (command) from Wikipedia](https://en.wikipedia.org/wiki/Kill_%28command%29)
### [Windows](Windows "Windows")


* [Using Processes and Threads](http://msdn.microsoft.com/en-us/library/windows/desktop/ms686937%28v=VS.85%29.aspx), [Windows Desktop Development](http://msdn.microsoft.com/en-us/windows/desktop)


 [Creating Processes](http://msdn.microsoft.com/en-us/library/windows/desktop/ms682512%28v=vs.85%29.aspx)
 [Creating a Child Process with Redirected Input and Output](http://msdn.microsoft.com/en-us/library/windows/desktop/ms682499%28v=vs.85%29.aspx)
* [Processes and Threads, MSDN](http://msdn.microsoft.com/en-us/library/ms684841%28v=VS.85%29.aspx)
* [Processes, Threads, and Jobs](http://download.microsoft.com/download/5/b/3/5b38800c-ba6e-4023-9078-6e9ce2383e65/c06x1116607.pdf) (pdf) from [Microsoft® Windows® Internals, Fourth Edition: Windows 2000, Windows XP, and Windows Server 2003](http://www.microsoft.com/learning/en/us/book.aspx?ID=6710&locale=en-us) by [David Solomon](http://www.solsem.com/) and [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich)
* [Windows Task Manager from Wikipedia](https://en.wikipedia.org/wiki/Windows_Task_Manager)


### [C++](Cpp "Cpp")


* [QProcess | Documentation | Qt Developer Network](http://qt-project.org/doc/qt-4.8/qprocess.html)
* [Chapter 1. Boost.Process](http://www.highscore.de/boost/process/)
* [Brief Review to C++ / Process / Thread](http://ludwig.csie.ncku.edu.tw/members/alvin/2010_9/ESL/C++_Process_2010.pdf) (pdf)


### [Java](Java "Java")


* [Processes and Threads (The Java™ Tutorials > Essential Classes > Concurrency)](http://docs.oracle.com/javase/tutorial/essential/concurrency/procthread.html)


### Misc


* [Process (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Process)
* [Processing (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Processing_%28programming_language%29)
* [Signal processing from Wikipedia](https://en.wikipedia.org/wiki/Signal_processing)
* [Process (science) from Wikipedia](https://en.wikipedia.org/wiki/Process_%28science%29)
* [Process control from Wikipedia](https://en.wikipedia.org/wiki/Process_control)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Process state from Wikipedia](https://en.wikipedia.org/wiki/Process_state)

**[Up one Level](Programming "Programming")**







 
