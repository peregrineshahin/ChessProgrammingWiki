---
title: Cilk
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Languages](Languages "Languages") * Cilk**

**Cilk** (pronounced "silk") is a [C](C "C")-based, general-purpose programming language designed for [multithreaded](https://en.wikipedia.org/wiki/Multithreading_%28computer_architecture%29) parallel computing. Cilk started as in the mid 90s as a project at the Supertech research group in the [MIT Labroratory](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") headed by [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"). Important milestones in Cilk technology include the original Cilk-1, which provided a provably efficient work-stealing runtime support but little linguistic support, the later Cilk-5, which provided simple linguistic extensions for multithreading to [ANSI C](https://en.wikipedia.org/wiki/ANSI_C), the commercial *Cilk++* by *Cilk Arts*, which extended the Cilk model to [C++](Cpp "Cpp"), and after [Intel](Intel "Intel") acquired *Cilk Arts* in 2009, [Intel Cilk Plus](https://en.wikipedia.org/wiki/Intel_Cilk_Plus). In November 2010, Intel published a language and an [ABI](https://en.wikipedia.org/wiki/Application_binary_interface) specification to enable other compilers to implement Cilk Plus <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## Parallel Chess

Cilk's testbeds in the 90s were chess programs using a [parallel search](Parallel_Search "Parallel Search"). [\*Socrates](Star_Socrates "Star Socrates") used the [Jamboree](Jamboree "Jamboree") algorithm to search game trees in parallel and uses the Cilk 1.0 language and run-time system to express and to schedule the computation. [CilkChess](CilkChess "CilkChess") was written using the Cilk-5 linguistic extensions.

## Cilk-5 Linguistic Extensions

Cilk-5.4.6 is the latest official MIT Cilk released under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

The keyword "**cilk**" defines a function which can [spawned](https://en.wikipedia.org/wiki/Spawn_%28computing%29) as a new [thread](https://en.wikipedia.org/wiki/Thread_%28computer_science%29), by using the "**spawn**" keyword. A cilk procedure cannot safely return values of the children it has spawned until it executes a "**sync**" statement, which acts like a local barrier. **Inlets**, a kind of local function with access to local variables of its parent frame, are used to return values to its parent with the option to **abort** all of the already spawned descendants of the procedure to terminate immediately. Inlets are guaranteed to operate [atomically](https://en.wikipedia.org/wiki/Atomic_%28computer_science%29) with regards to each other and to the parent procedure, thus avoiding the bugs that could occur if the multiple returning procedures tried to update the same variables in the parent frame at the same time.

## Parallel Alpha-Beta

This is how an [alpha-beta](Alpha-Beta "Alpha-Beta") search routine was implemented with Cilk-5 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, using the five keywords **cilk**, **spawn**, **sync**, **inlet** and **abort**:

```C++
cilk int search( position *prev, int move, int depth ) {
   position cur; int bestscore = -oo, num_moves, mv, sc, cutoff = false;
  
   inlet void catch( int child_sc ) {
      child_sc = -child_sc; /* negamax */
      if ( child_sc > bestscore ) {
         bestscore = child_sc;
         if ( child_sc > cur.alpha ) {
            cur.alpha = child_sc;
            if ( child_sc >= cur.beta ) { 
               cutoff = true;
               abort;
            }
         }
      }
   } /* end inlet */

   /* create current position and set up for search */
   make_move( prev, move, &cur );
   if ( depth <= 0 ) return eval( &cur );
   cur.alpha = -prev->beta;  /* negamax */
   cur.beta  = -prev->alpha;
   num_moves = gen_moves( &cur );

   /* search the moves */
   for ( mv = 0; !cutoff && mv < num_moves; mv++) {
      catch ( spawn search( &cur, mv, depth-1 ) );
      if ( mv == 0 ) sync; /* young brothers wait */
   }
   sync; /* this sync is outside the loop so that
            older brothers execute in parallel */
   return bestscore;
}

```

## Quote

by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") after [WCCC 1999](WCCC_1999 "WCCC 1999") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
Actually the big professor who has written so many books that i have in my possession was there too: [Leiserson](Charles_Leiserson "Charles Leiserson"). Lucky i could exchange a few words during the game with him. 

```

```C++
Cilk really is a very promising language. In contradiction to all my big efforts to parallellize [DIEP](Diep "Diep"), writing in Cilk this goes a lot simpler. Regrettably when starting the parallel version of DIEP, there was no port of CILK to windows (the first demand for something is that it must work both in windows and linux before i can use it; interface is of course something different) otherwise i might have done better in paderborn. 

```

```C++
Anyone who still must start his parallel project here gets a free tip from me:
Don't go fiddle with difficult parallellization, simply use CILK, let that language handle the parallellism and keep only busy making a good program!

```

```C++
The alternative to Cilk is years of bugfixing the parallel code. 

```

[](File:ParallelExperts1999.jpg)
Talking Cilk at [WCCC 1999](WCCC_1999 "WCCC 1999"): [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [Don Dailey](Don_Dailey "Don Dailey") and [Charles Leiserson](Charles_Leiserson "Charles Leiserson")

## Cilk++

MIT licensed Cilk technology to *Cilk Arts, Inc.*, a venture-funded start-up founded by [Charles Leiserson](Charles_Leiserson "Charles Leiserson") and [Matteo Frigo](Matteo_Frigo "Matteo Frigo"). Cilk Arts developed *Cilk++,* a quantum improvement over MIT Cilk, which includes full support for [C++](Cpp "Cpp"), parallel loops, and superior interoperability with serial code.

## Intel Cilk Plus

In July 2009 [Intel Corporation](Intel "Intel") acquired *Cilk Arts* <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Intel Cilk Plus adopts simplifications, proposed by *Cilk Arts* in Cilk++, to eliminate the need for several of the original Cilk keywords while adding the ability to spawn functions and to deal with variables involved in reduction operations. Intel Cilk Plus differs from Cilk and Cilk++ by adding array extensions, being incorporated in a commercial compiler, and compatibility with existing debuggers <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## See also

- [ABDADA](ABDADA "ABDADA")
- [CilkChess](CilkChess "CilkChess")
- [Jamboree](Jamboree "Jamboree")
- [Parallel Search](Parallel_Search "Parallel Search")
- [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
- [\*Socrates](Star_Socrates "Star Socrates")

## Publications

<a id="cite-note-8" href="#cite-ref-8">[8]</a>

## 1995 ...

- [Robert D. Blumofe](Robert_Blumofe "Robert Blumofe"), [Christopher F. Joerg](Chris_Joerg "Chris Joerg"), [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou") (**1995**). *Cilk: An Efficient Multithreaded Runtime System* Proceedings of the Fifth ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming (PPoPP) Santa Barbara, California Pg. 207–216, [pdf](http://supertech.csail.mit.edu/papers/PPoPP95.pdf)
- [Philip Andrew Lisiecki](Phil_Lisiecki "Phil Lisiecki") (**1996**). *Macro-Level Scheduling in the Cilk Network of Workstations Environment*, Masters Thesis, Department of Electrical Engineering and Computer Science, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/lisiecki-msthesis.pdf)
- [Christopher F. Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing*. Ph. D. Thesis, Department of Electrical Engineering and Computer Science, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)
- [Matteo Frigo](Matteo_Frigo "Matteo Frigo"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall") (**1998**). *The Implementation of the Cilk-5 Multithreaded Language*. Proceedings of the ACM SIGPLAN '98 Conference on Programming Language Design and Implementation, Montreal, Quebec, Canada, Pg 212–223, [pdf](http://supertech.csail.mit.edu/papers/cilk5.pdf)

## 2000 ...

- [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**2001**). *Using Cilk to Write Multiprocessor Chess Programs*, [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf)
- [Siddhartha Sen](Siddhartha_Sen "Siddhartha Sen") (**2004**). *[Dynamic processor allocation for adaptively parallel work-stealing jobs](https://dspace.mit.edu/handle/1721.1/33355)*. Master's thesis, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), advisor [Charles Leiserson](Charles_Leiserson "Charles Leiserson") <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Vivek Sarkar](http://www.cs.rice.edu/~vs3/home/Vivek_Sarkar.html) (**2008**). *Shared-Memory Parallel Programming with OpenMP*. [Rice University](https://en.wikipedia.org/wiki/Rice_University), [slides as pdf](http://www.cs.rice.edu/~vs3/comp422/lecture-notes/comp422-lec7-s08-v1.pdf)
- [Matteo Frigo](Matteo_Frigo "Matteo Frigo"), [Pablo Halpern](http://www.plaxo.com/profile/show/227634457468?pk=a7b8fd342887637e7e469951fbfa6ed308f28640), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Stephen Lewin-Berlin](http://venturebeatprofiles.com/person/profile/stephen-lewin-berlin) (**2009** ). *Reducers and Other Cilk++ Hyperobjects*. Cilk Arts, Inc., [pdf](http://www.fftw.org/~athena/papers/hyper.pdf)

## 2010 ...

- [Milind Chabbi](http://ai.arizona.edu/people/alumni/milind/) (**2010**). *Cilk and Cilk++ Multithreaded Languages*. [pdf](http://www.cs.rice.edu/~johnmc/comp522/lecture-notes/COMP522-2010-Lecture8-Cilk.pdf)
- [John Mellor-Crummey](http://www.cs.rice.edu/~johnmc/) (**2011**). *Shared-memory Parallel Programming with Cilk*. [Rice University](https://en.wikipedia.org/wiki/Rice_University), [slides as pdf](http://www.clear.rice.edu/comp422/lecture-notes/comp422-2011-Lecture4-Cilk.pdf)

## Manuals

- [Cilk 5.4.6. Reference Manual](http://supertech.csail.mit.edu/cilk/manual-5.4.6.pdf) (pdf)
- [Intel® Cilk™ Plus Language Specification](http://software.intel.com/sites/products/cilk-plus/cilk_plus_language_specification.pdf) (pdf)

## Forum Posts

- [Cilk++](http://www.talkchess.com/forum/viewtopic.php?t=29601) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 30, 2009

## External Links

- [Cilk from Wikipedia](https://en.wikipedia.org/wiki/Cilk)
- [The Cilk Project](http://supertech.csail.mit.edu/cilk/) from [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [Intel Cilk Plus from Wikipedia](https://en.wikipedia.org/wiki/Intel_Cilk_Plus)
- [Intel® Cilk™ Plus Specification - Intel® Software Network](http://software.intel.com/en-us/articles/intel-cilk-plus-specification/)
- Commercializing MIT's Cilk Project by [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Intel® Cilk™ Plus Specification - Intel® Software Network](http://software.intel.com/en-us/articles/intel-cilk-plus-specification/)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [cilk-5.4.6.tar.gz](http://supertech.csail.mit.edu/cilk/cilk-5.4.6.tar.gz)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**2001**). *Using Cilk to Write Multiprocessor Chess Programs*, [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [DIEP parallel in Paderborn - technical and detailed story](https://www.stmintz.com/ccc/index.php?id=58505) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), June 28, 1999
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Intel Acquires Cilk++ Technology](http://www.ddj.com/cpp/218900367), [Dr. Dobb's](http://www.ddj.com/), August 01, 2009
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Intel Cilk Plus from Wikipedia](https://en.wikipedia.org/wiki/Intel_Cilk_Plus)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Cilk from Wikipedia](https://en.wikipedia.org/wiki/Cilk)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [SuperTech Paper Listing](http://supertech.csail.mit.edu/papers.html)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Work stealing from Wikipedia](https://en.wikipedia.org/wiki/Work_stealing)

**[Up one Level](Languages "Languages")**

