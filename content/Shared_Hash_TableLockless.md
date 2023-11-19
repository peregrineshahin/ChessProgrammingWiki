---
title: Shared Hash TableLockless
---
**[Home](Home "Home") \* [Programming](Programming "Programming") \* [Data](Data "Data") \* [Hash Table](Hash_Table "Hash Table") \* Shared Hash Table**



[ Dining philosophers problem <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Shared Hash Table**,  

a Hash table or [Transposition table](Transposition_Table "Transposition Table") which is accessed by various [processes](Process "Process") or [threads](Thread "Thread") simultaneously, running on [multiple processors](https://en.wikipedia.org/wiki/Multiprocessing) or [processor cores](https://en.wikipedia.org/wiki/Multi-core_processor). Shared hash tables are most often implemented as dynamically allocated [memory](Memory "Memory") treated as global [array](Array "Array"). Due to [memory protection](https://en.wikipedia.org/wiki/Memory_protection) between processes, they require an [Application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface) provided by the [operating system](https://en.wikipedia.org/wiki/Operating_system) to allocate [shared memory](https://en.wikipedia.org/wiki/Shared_memory). Threads may share global memory from the process they are belonging to. 



### ABDADA


*see Home: [ABDADA](ABDADA "ABDADA")*


[ABDADA](ABDADA "ABDADA"), Alpha-Bêta Distribué avec Droit d'Anesse (Distributed Alpha-Beta Search with Eldest Son Right) is a loosely synchronized, distributed search algorithm by [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . It is based on the Shared Hash Table, and adds the number of processors searching this node inside the hash-table entry for better utilization - considering the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept").



### Lazy SMP


*see Home: [Lazy SMP](Lazy_SMP "Lazy SMP")*


Recent improvements by [Daniel Homan](Daniel_Homan "Daniel Homan") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [Martin Sedlak](Martin_Sedlak "Martin Sedlak") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and others on **Lazy** SMP indicate that the algorithm scales quite well up to 8 cores and beyond <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



## Concurrent Access


Due to its size, i.e. 16 or more bytes, writing and reading hash entries are none [atomic](https://en.wikipedia.org/wiki/Linearizability) and require multiple write- and read-cycles. It may and will happen that [concurrent](https://en.wikipedia.org/wiki/Concurrency_%28computer_science%29) writes and reads at the same table address and almost same time results in corrupt data retrieved that causes significant problems to the search. [Interrupts](https://en.wikipedia.org/wiki/Interrupt) may occur between accesses, and there are further nondeterministic issues involved <a id="cite-note-6" href="#cite-ref-6">[6]</a> which may cause one thread to read two or more atomic data items, which were written by different threads, searching different positions with the same hash-index due to [type-2](Transposition_Table#IndexCollisions "Transposition Table") errors.



### Locks


One common solution to avoid such errors is [synchronization](https://en.wikipedia.org/wiki/Synchronization_%28computer_science%29) using [atomic locks](https://en.wikipedia.org/wiki/Lock_%28computer_science%29), and to implement a [critical section](https://en.wikipedia.org/wiki/Critical_section) or [mutual exclusion](https://en.wikipedia.org/wiki/Mutual_exclusion). 



### CilkChess


As an example, [CilkChess](CilkChess "CilkChess") used [Cilk's](Cilk "Cilk") support for atomicity <a id="cite-note-7" href="#cite-ref-7">[7]</a>. It uses one lock per hash entry:




```C++

typedef struct
{
   Cilk_lockvar lock;
   U64 key;
   U64 data;
} ttentry;

ttentry hashtable[TABLESIZE];

void ttinit ( ) {
   for (int i = 0; i < TABLESIZE; ++i)
      Cilk_lock_init( hashtable[i].lock);
}

void update_entry ( ttentry *e, U64 key, U64 data ) {
   Cilk_lock (e->lock); /* begin critical section */
   e->key = key;
   e->data = data;
   ...
   Cilk_unlock (e->lock); /* end critical section */
}

```

### Granularity


An important property of a lock is its [granularity](https://en.wikipedia.org/wiki/Lock_%28computer_science%29#Granularity), which is a measure of the amount of data the lock is protecting. In general, choosing a coarse granularity (a small number of locks, each protecting a large segment of data) results in less lock overhead when a single process is accessing the protected data, but worse performance when multiple processes are running concurrently. This is because of increased lock contention. The more coarse the lock, the higher the likelihood that the lock will stop an unrelated process from proceeding, i.e. in the extreme case, one lock for the whole table. Conversely, using a fine granularity (a larger number of locks, each protecting a fairly small amount of data), like in the CilkChess sample above, increases the overhead of the locks themselves but reduces lock contention. For a huge transposition table with millions of fairly small entries locks incur a significant performance penalty on many architectures. 




### Lock-less


### Xor


[Robert Hyatt](Robert_Hyatt "Robert Hyatt") and [Tim Mann](Tim_Mann "Tim Mann") proposed a lock-less transposition table implementation <a id="cite-note-8" href="#cite-ref-8">[8]</a> for 128 bit entries with two atomic [quad words](Quad_Word "Quad Word"), one qword for storing the key or signature, the 64-bit [Zobrist-](Zobrist_Hashing "Zobrist Hashing") or [BCH-key](BCH_Hashing "BCH Hashing") of the position, and one qword for the other information stored, [move](Hash_Move "Hash Move"), [score](Score "Score"), [draft](Depth "Depth") and that like (data). Rather than to store two disjoint items, the key is stored [xored](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with data, while data is stored additionally as usual. According to Robert Hyatt, the original idea came from [Harry Nelson](Harry_Nelson "Harry Nelson") somewhere in 1990-1992 <a id="cite-note-9" href="#cite-ref-9">[9]</a>.




```C++

index = key % TABLESIZE;
hashtable[index].key  = key ^ data;
hashtable[index].data = data;

```

Since the retrieving position requires the same key for a probing hit, the stored key xored by the retrieved key must match the stored data. 




```C++

index = key % TABLESIZE;
if (( hashtable[index].key ^ hashtable[index].data) == key )
{
   /* entry matches key */
}

```

If key and data were written simultaneously by different search instances with different keys, the error will usually yield in a mismatch of the comparison, except the rare but inherent [Key collisions](Transposition_Table#KeyCollisions "Transposition Table") or type-1 errors <a id="cite-note-10" href="#cite-ref-10">[10]</a>. As pointed out by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-11" href="#cite-ref-11">[11]</a>, the XOR technique might be applied for any size. 



### Checksum


For a lock-less shared Hash table with (much) larger entry sizes such as the [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table"), one may store an additional [checksum](https://en.wikipedia.org/wiki/Checksum) of the data, to likely detect errors after retrieving, and to safe the consistence of an entry. 



### SSE2


[x86](X86 "X86") and [x86-64](X86-64 "X86-64") [SSE2](SSE2 "SSE2") 128-bit read/write instructions might in practice [atomic](https://en.wikipedia.org/wiki/Linearizability), but they are not guaranteed even if properly aligned <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>. If the processor implements a 16-byte store instruction internally as 2 8-byte stores in the store pipeline, it's perfectly possible for another processor to "steal" the cache line in between the two stores <a id="cite-note-14" href="#cite-ref-14">[14]</a>. However, [Intel](Intel "Intel") states any locked instruction (either the XCHG instruction or another read-modify-write instruction with a [LOCK prefix](https://en.wikipedia.org/wiki/Fetch-and-add#x86_implementation)) appears to execute as an indivisible and uninterruptible sequence of load(s) followed by store(s) regardless of alignment <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a>.



## Allocation


Multiple threads inside one process can share its [global variables](https://en.wikipedia.org/wiki/Global_variable) or heap. Processes require special [API](https://en.wikipedia.org/wiki/Application_programming_interface) calls to create shared memory and to pass a handle to other processes around for [interprocess communication](https://en.wikipedia.org/wiki/Inter-process_communication). [POSIX](https://en.wikipedia.org/wiki/POSIX) provides a standardized API for using shared memory <a id="cite-note-17" href="#cite-ref-17">[17]</a> . [Linux](Linux "Linux") kernel builds since 2.6 offer /dev/shm as shared memory in the form of a [RAM disk](https://en.wikipedia.org/wiki/RAM_disk).



## See also


* [ABDADA](ABDADA "ABDADA")
* [AVX](AVX "AVX")
* [Cilk](Cilk "Cilk")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Linux](Linux "Linux")
* [Memory](Memory "Memory")
* [Parallel Search](Parallel_Search "Parallel Search")
* [SSE2](SSE2 "SSE2")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Unix](Unix "Unix")
* [Windows](Windows "Windows")
* [XOP](XOP "XOP")


## Publications


<a id="cite-note-18" href="#cite-ref-18">[18]</a>



### 1980 ...


* [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal"), [Larry Rudolph](Mathematician#LRudolph "Mathematician"), [Marc Snir](Mathematician#MSnir "Mathematician") (**1988**). *[Efficient Synchronization on Multiprocessors with Shared Memory](https://dl.acm.org/citation.cfm?id=48024)*. [ACM TOPLAS](ACM#TOPLAS "ACM"), Vol. 10, No. 4
* [Henri Bal](Henri_Bal "Henri Bal") (**1989**). *[The shared data-object model as a paradigm for programming distributed systems](http://dare.ubvu.vu.nl/handle/1871/12760?mode=full&submit_simple=Show+full+item+record)*. Ph.D. thesis, [Vrije Universiteit](https://en.wikipedia.org/wiki/Vrije_Universiteit)


### 1990 ...


* [Maurice Herlihy](http://www.cs.brown.edu/~mph/) (**1991**). *Wait-free synchronization*. [ACM Transactions on Programming Languages and Systems](https://en.wikipedia.org/wiki/ACM_Transactions_on_Programming_Languages_and_Systems) Vol. 13 No. 1, [pdf](http://www.cs.brown.edu/~mph/Herlihy91/p124-herlihy.pdf)
* [Vincent David](Vincent_David "Vincent David") (**1993**). *[Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax](http://cat.inist.fr/?aModele=afficheN&cpsidt=161774)* = Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax, Ph.D. Thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse), [France](https://en.wikipedia.org/wiki/France)


 **Abstract**: *The method of parallelization is based on a suppression of control between the search processes, in favor of a speculative parallelism and full sharing of information achieved through a physically distributed but virtually shared memory. The contribution of our approach for real-time distributed systems and fault-tolerant is evaluated through experimental results*.
* [Maged M. Michael](http://www.research.ibm.com/people/m/michael/), [Michael L. Scott](http://www.cs.rochester.edu/%7Escott/) (**1995**). *Implementation of Atomic Primitives on Distributed Shared Memory Multiprocessors*. [HPCA'95](http://www-2.cs.cmu.edu/%7Escandal/conf/pro-HPCA-950122.txt), [pdf](http://www.research.ibm.com/people/m/michael/hpca-1995.pdf)
* [Paul Lu](Paul_Lu "Paul Lu") (**1997**). *Aurora: Scoped Behaviour for Per-Context Optimized Distributed Data Sharing*. 11th International Parallel Processing Symposium (IPPS) <a id="cite-note-19" href="#cite-ref-19">[19]</a>
* [John Romein](John_Romein "John Romein"), [Aske Plaat](Aske_Plaat "Aske Plaat"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1999**). *Transposition Table Driven Work Scheduling in Distributed Search*. [AAAI-99](AAAI "AAAI"), [pdf](https://www.aaai.org/Papers/AAAI/1999/AAAI99-103.pdf) <a id="cite-note-20" href="#cite-ref-20">[20]</a> <a id="cite-note-21" href="#cite-ref-21">[21]</a>


### 2000 ...


* [Paul Lu](Paul_Lu "Paul Lu") (**2000**). *[Scoped Behaviour for Optimized Distributed Data Sharing](http://webdocs.cs.ualberta.ca/~paullu/PhDThesis/thesis.html)*. Ph.D. thesis, [University of Toronto](University_of_Toronto "University of Toronto")
* [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah") (**2001**) *Parallel Alpha-Beta Search on Shared Memory Multiprocessors*. Masters Thesis, [pdf](http://www.valavan.net/mthesis.pdf)
* [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf) <a id="cite-note-22" href="#cite-ref-22">[22]</a>
* [Maged M. Michael](http://www.research.ibm.com/people/m/michael/) (**2002**). *High Performance Dynamic Lock-Free Hash Tables and List-Based Sets*. [IBM Thomas J. Watson Research Center](https://en.wikipedia.org/wiki/Thomas_J._Watson_Research_Center), [pdf](http://www.research.ibm.com/people/m/michael/spaa-2002.pdf)
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *[A lock-less transposition table implementation for parallel search chess engines](http://www.craftychess.com/hyatt/hashing.html)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
* [Jiří Barnat](http://www.fi.muni.cz/%7Exbarnat/), [Petr Ročkai](http://www.behindkde.org/node/625) (**2007**). *Shared Hash Tables in Parallel Model Checking*. Faculty of Informatics, [Masaryk University](https://en.wikipedia.org/wiki/Masaryk_University), [Brno](https://en.wikipedia.org/wiki/Brno), [Czech Republic](https://en.wikipedia.org/wiki/Czech_Republic), PDMC 2007, Preliminary Version as [pdf](http://anna.fi.muni.cz/papers/src/public/168699cd5787307ee3c8c1a509327e6f.pdf)
* [Vivek Sarkar](http://www.cs.rice.edu/%7Evs3/home/Vivek_Sarkar.html) (**2008**). *Shared-Memory Parallel Programming with OpenMP*. [Rice University](https://en.wikipedia.org/wiki/Rice_University), [slides as pdf](http://www.cs.rice.edu/%7Evs3/comp422/lecture-notes/comp422-lec7-s08-v1.pdf)
* [Jouni Leppäjärvi](http://offcode.fi/) (**2008**). *A pragmatic, historically oriented survey on the universality of synchronization primitives*. [pdf](http://www.oamk.fi/~joleppaj/personal/jleppaja_gradu_080511.pdf)


### 2010 ...


* [Alfons Laarman](http://www.vf.utwente.nl/%7Elaarman/), [Jaco van de Pol](http://wwwhome.ewi.utwente.nl/%7Evdpol/), [Michael Weber](http://wwwhome.cs.utwente.nl/%7Emichaelw/) (**2010**). *[Boosting Multi-Core Reachability Performance with Shared Hash Tables](http://doc.utwente.nl/73119/)*. Formal Methods and Tools, [University of Twente](https://en.wikipedia.org/wiki/University_of_Twente), [The Netherlands](https://en.wikipedia.org/wiki/Netherlands), [pdf](http://fmcad10.iaik.tugraz.at/Papers/papers/12Session11/033Laarman.pdf)
* [John Mellor-Crummey](http://www.cs.rice.edu/%7Ejohnmc/) (**2011**). *Shared-memory Parallel Programming with Cilk*. [Rice University](https://en.wikipedia.org/wiki/Rice_University), [slides as pdf](http://www.clear.rice.edu/comp422/lecture-notes/comp422-2011-Lecture4-Cilk.pdf) » [Cilk](Cilk "Cilk")
* [Anthony Williams](http://stackoverflow.com/users/5597/anthony-williams) (**2012**). *[C++ Concurrency in Action: Practical Multithreading](http://www.cplusplusconcurrencyinaction.com/)*. <a id="cite-note-23" href="#cite-ref-23">[23]</a>
* [Tobias Maier](https://dblp.uni-trier.de/pers/hd/m/Maier:Tobias), [Peter Sanders](Peter_Sanders "Peter Sanders"), [Roman Dementiev](https://dblp.uni-trier.de/pers/hd/d/Dementiev:Roman) (**2016**). *Concurrent Hash Tables: Fast and General?(!)*. [arXiv:1601.04017](https://arxiv.org/abs/1601.04017)


## Forum Posts


### 1997 ...


* [Parallel searching](https://groups.google.com/d/msg/rec.games.chess.computer/Wl7A-v-gWYQ/QLuvAp0l4_gJ) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 22, 1997 » [KnightCap](KnightCap "KnightCap")
* [CilkChess question for Don](https://www.stmintz.com/ccc/index.php?id=41708) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 31, 1999 » [CilkChess](CilkChess "CilkChess")


### 2000 ...


* [Re: Atomic write of 64 bits](https://groups.google.com/group/comp.lang.asm.x86/browse_frm/thread/ab55c5d57a3a1fd1) by [Frans Morsch](Frans_Morsch "Frans Morsch"), [comp.lang.asm.x86](https://groups.google.com/group/comp.lang.asm.x86/topics), September 25, 2000


### 2005 ...


* [multithreading questions](http://www.talkchess.com/forum/viewtopic.php?t=15662) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), August 08, 2007
* [If making an SMP engine, do NOT use processes](http://www.talkchess.com/forum/viewtopic.php?t=19446) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), February 07, 2008
* [threads vs processes](http://www.talkchess.com/forum/viewtopic.php?t=22398) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 16, 2008
* [threads vs processes again](http://www.talkchess.com/forum/viewtopic.php?t=22799) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 05, 2008
* [SMP hashing problem](http://www.talkchess.com/forum/viewtopic.php?t=26208) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 24, 2009
* [Interlock clusters](http://www.talkchess.com/forum/viewtopic.php?t=26223) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 25, 2009


### 2010 ...


* [Crafty Transpostion Table Question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=34606) by [Eric Stock](index.php?title=Eric_Stock&action=edit&redlink=1 "Eric Stock (page does not exist)"), [CCC](CCC "CCC"), May 30, 2010 » [Crafty](Crafty "Crafty"), [Lockless Hashing](#Lockless)
* [lockless hashing](http://www.talkchess.com/forum/viewtopic.php?t=37976) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 07, 2011
* [On parallelization](http://www.talkchess.com/forum/viewtopic.php?t=38411) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), March 13, 2011
* [cache alignment of tt](http://www.talkchess.com/forum/viewtopic.php?t=42833) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 11, 2012
* [Speaking of the hash table](http://www.talkchess.com/forum/viewtopic.php?t=46346) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), December 09, 2012
* [Lazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=46597) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), December 27, 2012 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
* [Multi-threaded memory access](http://www.open-chess.org/viewtopic.php?f=5&t=2262) by [ThinkingALot](ThinkingALot "ThinkingALot"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2013 » [Memory](Memory "Memory"), [Thread](Thread "Thread")
* [Lazy SMP, part 3](http://www.talkchess.com/forum/viewtopic.php?t=47455) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 09, 2013
* [Shared hash table smp result](http://www.talkchess.com/forum/viewtopic.php?t=47568) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 21, 2013
* [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013 <a id="cite-note-24" href="#cite-ref-24">[24]</a>
* [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013 » [Lazy SMP](EXchess#LazySMP "EXchess") in [EXchess](EXchess "EXchess")
* [Lockless hash: Thank you Bob Hyatt!](http://www.talkchess.com/forum/viewtopic.php?t=49099) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), August 25, 2013
* [How could a compiler break the lockless hashing method?](http://www.talkchess.com/forum/viewtopic.php?t=50388) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), December 08, 2013
* [Parallel Search with Transposition Table](http://www.talkchess.com/forum/viewtopic.php?t=51755) by [Daylen Yang](Daylen_Yang "Daylen Yang"), [CCC](CCC "CCC"), March 27, 2014 » [Parallel Search](Parallel_Search "Parallel Search")
* [Two hash functions for distributed transposition table](http://www.talkchess.com/forum/viewtopic.php?t=54666) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), December 16, 2014


### 2015 ...


* [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015 » [Cheng](Cheng "Cheng")
* [Trying to improve lazy smp](http://www.talkchess.com/forum/viewtopic.php?t=55970) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 11, 2015
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=57572) by Lucas Braesch, [CCC](CCC "CCC"), September 09, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [atomic TT](http://www.talkchess.com/forum/viewtopic.php?t=57634) by Lucas Braesch, [CCC](CCC "CCC"), September 13, 2015
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=58645) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), December 21, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP")


**2016**



* [NUMA 101](http://www.talkchess.com/forum/viewtopic.php?t=58830) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 07, 2016 » [NUMA](NUMA "NUMA")
* [Lazy SMP - how it works](http://www.talkchess.com/forum/viewtopic.php?t=59389) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), February 29, 2016 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [lockless hashing](http://www.talkchess.com/forum/viewtopic.php?t=60122) by Lucas Braesch, [CCC](CCC "CCC"), May 10, 2016
* [What do you do with NUMA?](http://www.talkchess.com/forum/viewtopic.php?t=61472) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 19, 2016 » [NUMA](NUMA "NUMA")


**2017 ...**



* [Question about parallel search and race conditions](http://www.talkchess.com/forum/viewtopic.php?t=65134) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 11, 2017 » [Parallel Search](Parallel_Search "Parallel Search")
* [Prefetch and Threading](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70586) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), April 25, 2019 » [Thread](Thread "Thread"), [Transposition Table](Transposition_Table "Transposition Table")
* [RMO - Randomized Move Order - yet another Lazy SMP derivate](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72684) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), December 30, 2019


### 2020 ...


* [hash collisions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72932) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 28, 2020 » [Key Collisions](Transposition_Table#KeyCollisions "Transposition Table")
* [Transposition table and multithreaded search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76483) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 03, 2021


## External Links


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


### Distributed memory


* [Distributed memory from Wikipedia](https://en.wikipedia.org/wiki/Distributed_memory)
* [Distributed hash table from Wikipedia](https://en.wikipedia.org/wiki/Distributed_hash_table)


 [Koorde](https://en.wikipedia.org/wiki/Koorde) based on [Chord](https://en.wikipedia.org/wiki/Chord_%28peer-to-peer%29) and [De Bruijn Sequence](De_Bruijn_Sequence "De Bruijn Sequence")
* [Transposition-driven scheduling - Wikipedia](https://en.wikipedia.org/wiki/Transposition-driven_scheduling)
* [The Aurora Distributed Shared Data System](http://webdocs.cs.ualberta.ca/~paullu/Aurora/aurora.html) by [Paul Lu](Paul_Lu "Paul Lu")


### Misc


* [Cilk from Wikipedia](https://en.wikipedia.org/wiki/Cilk) » [Cilk](Cilk "Cilk")
* [The Cilk Project](http://supertech.csail.mit.edu/cilk/) from [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [Fetch-and-add from Wikipedia](https://en.wikipedia.org/wiki/Fetch-and-add)
* [Intel Cilk Plus from Wikipedia](https://en.wikipedia.org/wiki/Intel_Cilk_Plus)
* [XMTC from Wikipedia](https://en.wikipedia.org/wiki/XMTC)
* [Ian Carr](Category:Ian_Carr "Category:Ian Carr") with [Nucleus](Category:Nucleus "Category:Nucleus") - [Solar Plexus 1971](https://en.wikipedia.org/wiki/Nucleus_(band)#Discography), feat. [Karl Jenkins](Category:Karl_Jenkins "Category:Karl Jenkins"), [Jeff Clyne](Category:Jeff_Clyne "Category:Jeff Clyne") and [John Marshall](Category:John_Marshall "Category:John Marshall"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Dining philosophers problem from Wikipedia](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *The ABDADA Distributed Minimax Search Agorithm*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal"), [zipped postscript](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170&start=11) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 01, 2015
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Memory disambiguation from Wikipedia](https://en.wikipedia.org/wiki/Memory_disambiguation)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**2001**). *Using Cilk to Write Multiprocessor Chess Programs*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf), 5 Other parallel programming issues, Cilk support for atomicity, pp. 17-18
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann") (**2002**). *[A lock-less transposition table implementation for parallel search chess engines](http://www.craftychess.com/hyatt/hashing.html)*. [ICGA Journal, Vol. 25, No. 1](ICGA_Journal#25_1 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Lockless hash: Thank you Bob Hyatt!](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=531603&t=49099) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 26, 2013
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). *[The Effect of Hash Signature Collisions in a Chess Program](http://www.craftychess.com/hyatt/collisions.html)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Re: lockless hashing](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=393348&t=37976) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 07, 2011
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Effectively atomic read of 16 bytes on x86\_64 without cmpxchg16b?](https://groups.google.com/d/msg/lock-free/hXtlgYrJj7M/j5mTHsaWYo0J) by [Anthony Williams](http://stackoverflow.com/users/5597/anthony-williams), [groups.google.lock-free](https://groups.google.com/forum/#!forum/lock-free), February 08, 2012
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: Speaking of the hash table](http://www.talkchess.com/forum/viewtopic.php?t=46346&start=44) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 10, 2012
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [SSE instructions: single memory access](http://stackoverflow.com/questions/7646018/sse-instructions-single-memory-access) by Atom, [Stack overflow](http://de.wikipedia.org/wiki/Stack_Overflow_%28Website%29), October 04, 2011
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Intel® 64 and IA-32 Architectures Developer's Manual: Vol. 3A](http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-software-developer-vol-3a-part-1-manual.html), section 8.2.3.1.
16. <a id="cite-ref-16" href="#cite-note-16">↑</a>  [Fetch-and-add from Wikipedia](https://en.wikipedia.org/wiki/Fetch-and-add)
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [shm\_open](http://pubs.opengroup.org/onlinepubs/007908799/xsh/shm_open.html), [The Single UNIX Specification version 2](https://en.wikipedia.org/wiki/Single_UNIX_Specification#1997:_Single_UNIX_Specification_version_2), Copyright © 1997 [The Open Group](https://en.wikipedia.org/wiki/The_Open_Group)
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Maged Michael - Selected Publications](http://www.research.ibm.com/people/m/michael/pubs.htm)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [The Aurora Distributed Shared Data System](http://webdocs.cs.ualberta.ca/~paullu/Aurora/aurora.html)
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [Re: scorpio can run on 8192 cores](http://www.talkchess.com/forum/viewtopic.php?t=57343&start=5) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 29, 2015
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Transposition-driven scheduling - Wikipedia](https://en.wikipedia.org/wiki/Transposition-driven_scheduling)
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Transposition driven scheduling](http://www.talkchess.com/forum/viewtopic.php?t=47700) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), April 04, 2013
23. <a id="cite-ref-23" href="#cite-note-23">↑</a> [Information on the C++11 Memory Model](http://scottmeyers.blogspot.co.uk/2012/04/information-on-c11-memory-model.html) by [Scott Meyers](https://en.wikipedia.org/wiki/Scott_Meyers), April 24, 2012
24. <a id="cite-ref-24" href="#cite-note-24">↑</a> [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Aske Plaat](Aske_Plaat "Aske Plaat") (**2002**). *A Performance Analysis of Transposition-Table-Driven Scheduling in Distributed Search*. IEEE Transactions on Parallel and Distributed Systems, Vol. 13, No. 5, pp. 447–459. [pdf](http://www.cs.vu.nl/~bal/Papers/tds.pdf)

**[Up one Level](Hash_Table "Hash Table")**







 
