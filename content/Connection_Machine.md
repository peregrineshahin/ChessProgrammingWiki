---
title: Connection Machine
---
**[Home](Home "Home") * [Hardware](Hardware "Hardware") * Connection Machine**

\[ [FROSTBURG](https://en.wikipedia.org/wiki/FROSTBURG) on display <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Connection Machine**,

a series of supercomputers that grew out of [Danny Hillis'](Mathematician#Hillis "Mathematician") doctoral research at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") in the early 1980s on alternatives to the traditional [von Neumann architecture](index.php?title=Von_Neumann_Architecture&action=edit&redlink=1 "Von Neumann Architecture (page does not exist)") of computation, originally intended for applications in [artificial intelligence](Artificial_Intelligence "Artificial Intelligence") and [symbolic computation](https://en.wikipedia.org/wiki/Symbolic_computation). The Connection Machine was manufacturered since 1983 by [Thinking Machines Corporation](https://en.wikipedia.org/wiki/Thinking_Machines_Corporation) (TMC), founded by [Danny Hillis](Mathematician#Hillis "Mathematician") and [Sheryl Handler](https://en.wikipedia.org/wiki/Sheryl_Handler) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 CM-1, CM-2, CM-200](#cm-1.2c-cm-2.2c-cm-200)
- [2 CM-5](#cm-5)
- [3 Chess](#chess)
- [4 Quotes](#quotes)
- [5 Chess Programs](#chess-programs)
- [6 See also](#see-also)
- [7 Selected Publications](#selected-publications)
  - [7.1 1985 ...](#1985-...)
  - [7.2 1990 ...](#1990-...)
  - [7.3 1995 ...](#1995-...)
- [8 External Links](#external-links)
- [9 References](#references)

## CM-1, CM-2, CM-200

The **CM-1** consisted of up to 64 kibi of 1-bit [SIMD](https://en.wikipedia.org/wiki/SIMD) processors with 4 kibibits of [RAM](Memory#RAM "Memory") each inside a network of a 12-dimensional boolean [n-cube](https://en.wikipedia.org/wiki/Hypercube) structure suggested by physicist [Richard Feynman](Mathematician#RFeynman "Mathematician"). Within this hardwired physical structure, the software data structures for communication and transfer of data between processors could change as needed depending on the nature of the problem. This meant the mutability of the connections between processors were more important than the processors themselves. The **CM-2**, released in 1987, was a more advanced successor (including floating point hardware) with the same physical structure <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## CM-5

Under guidance of [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") and [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), the **CM-5**, announced in 1991, switched from the CM-2's hypercubic architecture of simple processors to an entirely new [MIMD](https://en.wikipedia.org/wiki/MIMD) architecture based on the [fat tree](https://en.wikipedia.org/wiki/Fat_tree) <a id="cite-note-4" href="#cite-ref-4">[4]</a> network of [SPARC](SPARC "SPARC"), and for the later CM-5E, SuperSPARC processors <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Chess

[Lewis Stiller](Lewis_Stiller "Lewis Stiller") used a CM-2 to generate certain chess six-piece [endgame tablebases](Endgame_Tablebases "Endgame Tablebases") by massively parallel [retrograde analysis](Retrograde_Analysis "Retrograde Analysis") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. CM-5 architects [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") and [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") were also co-authors of the parallel [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") chess programs [StarTech](StarTech "StarTech") and [\*Socrates](Star_Socrates "Star Socrates"). StarTech played the [ACM 1993](ACM_1993 "ACM 1993") on [NCSA's](University_of_Illinois_at_Urbana-Champaign#NCSA "University of Illinois at Urbana-Champaign") 512-processor CM-5 <a id="cite-note-7" href="#cite-ref-7">[7]</a> for third place <a id="cite-note-8" href="#cite-ref-8">[8]</a>. Incorporating the ACM 1993 winner, the serial program [Socrates II](Titan "Titan") by [Don Dailey](Don_Dailey "Don Dailey") and [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), StarTech emerged to \*Socrates, which played the [ACM 1994](ACM_1994 "ACM 1994") on the CM-5/512 again to become third behind [Deep Thought II](Deep_Thought "Deep Thought") and [Zarkov](Zarkov "Zarkov"). At the [WCCC 1995](WCCC_1995 "WCCC 1995") in [Hong Kong](https://en.wikipedia.org/wiki/Hong_Kong), \*Socrates played on a [Intel Paragon](Paragon "Paragon"), where it lost the [playoff](WCCC_1995#Playoff "WCCC 1995") versus [Fritz](Fritz "Fritz").

## Quotes

Quote from *History of \*Socrates* by [Chris Joerg](Chris_Joerg "Chris Joerg") from his Ph.D. Thesis <a id="cite-note-9" href="#cite-ref-9">[9]</a> :

```C++
We began work on this program in May of 1994. [Don Dailey](Don_Dailey "Don Dailey") and [Larry Kaufman](Larry_Kaufman "Larry Kaufman") of [Heuristic Software](Heuristic_Software "Heuristic Software") provided us with a version of [Socrates](Socrates "Socrates"), their serial chess program. During May and June we parallelized the program using [Cilk](Cilk "Cilk"), focusing mainly on the [search algorithm](Search "Search") and the [transposition table](Transposition_Table "Transposition Table"). During June Dailey visited [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") to help tune the program, but we spent most of June simply getting the parallel version of the program to work correctly. In late June, we entered *Socrates in the [1994 ACM International Computer Chess Championship](ACM_1994 "ACM 1994") in Cape May, New Jersey. We ran the program on a 512-node CM-5 at the [National Center for Supercomputing Applications](University_of_Illinois_at_Urbana-Champaign#NCSA "University of Illinois at Urbana-Champaign") (NCSA) at the [University of Illinois](University_of_Illinois_at_Urbana-Champaign "University of Illinois at Urbana-Champaign"). Despite the fact that we had begun working on the program less than two months earlier, the program ran reliable and finished in third place. 

```

## Chess Programs

- [StarTech](StarTech "StarTech")
- [\*Socrates](Star_Socrates "Star Socrates")

## See also

- [nCUBE](NCUBE "NCUBE")
- [Paragon](Paragon "Paragon")

## Selected Publications

## 1985 ...

- [W. Daniel Hillis](Mathematician#Hillis "Mathematician") (**1985**). *The Connection Machine*. Ph. D. thesis, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), advisors [Gerald Jay Sussman](Mathematician#Sussman "Mathematician"), [Claude Shannon](Claude_Shannon "Claude Shannon"), and [Marvin Minsky](Marvin_Minsky "Marvin Minsky"), [pdf](https://dspace.mit.edu/bitstream/handle/1721.1/14719/18524280-MIT.pdf?sequence=2)
- [W. Daniel Hillis](Mathematician#Hillis "Mathematician") (**1986**). *The Connection Machine*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), ISBN 0262081571, [Amazon](https://www.amazon.com/Connection-Machine-Press-Artificial-Intelligence/dp/0262081571)
- [David Waltz](David_Waltz "David Waltz") (**1987**). *[Applications of the Connection Machine](https://www.semanticscholar.org/paper/Applications-of-the-Connection-Machine-Waltz/fa669c38b100f1dd3ab7cdcc7af4673145535752)*. [IEEE Computer](IEEE#Computer "IEEE"), Vol. 20, No. 1
- [Lewis W. Tucker](http://dblp.uni-trier.de/pers/hd/t/Tucker:Lewis_W=), [George G. Robertson](https://en.wikipedia.org/wiki/George_G._Robertson) (**1988**). *Architecture and Applications of the Connection Machine*. [Computer](IEEE#Computer "IEEE"), Vol. 21, No. 8
- [S. Lennart Johnsson](https://en.wikipedia.org/wiki/Lennart_Johnsson), [Robert L. Krawitz](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/k/Krawitz:Robert_L=.html), [Roger Frye](Roger_Frye "Roger Frye"), [Douglas MacDonald](http://dblp.uni-trier.de/pers/hd/m/MacDonald:Douglas) (**1989**). *A Radix-2 FFT on the Connection Machine*. [Supercomputing 89](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5348943), [pdf](http://www.cs.yale.edu/publications/techreports/tr734.pdf)
- [S. Lennart Johnsson](https://en.wikipedia.org/wiki/Lennart_Johnsson), [Robert L. Krawitz](http://www.informatik.uni-trier.de/~ley/db/indices/a-tree/k/Krawitz:Robert_L=.html), [Roger Frye](Roger_Frye "Roger Frye"), [Douglas MacDonald](http://dblp.uni-trier.de/pers/hd/m/MacDonald:Douglas) (**1989**). *Cooley-Tukey FFT on the Connection Machine*. [Parallel Computing](http://www.journals.elsevier.com/parallel-computing/), [pdf](http://www.cs.yale.edu/publications/techreports/tr750.pdf) <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Xiru Zhang](Mathematician#XZhang "Mathematician"), [Michael McKenna](https://dblp.uni-trier.de/pers/hd/m/McKenna:Michael), [Jill P. Mesirov](Mathematician#JPMesirov "Mathematician"), [David Waltz](David_Waltz "David Waltz") (**1989**). *[An Efficient Implementation of the Back-propagation Algorithm on the Connection Machine CM-2](http://papers.neurips.cc/paper/281-an-efficient-implementation-of-the-back-propagation-algorithm-on-the-connection-machine-cm-2)*. [NIPS 1989](https://dblp.uni-trier.de/db/conf/nips/nips1989.html)

## 1990 ...

- [Erol Gelenbe](Mathematician#EGelenbe "Mathematician") (**1990**). *[Performance Analysis of the Connection Machine](http://dl.acm.org/citation.cfm?id=98757)*. [ACM SIGMETRICS](ACM#SIGMETRICS "ACM"), [pdf](https://assets.cs.ncl.ac.uk/seminars/81.pdf)
- [Arthur Trew](http://dblp.uni-trier.de/pers/hd/t/Trew:Arthur_S=), [Greg Wilson](Greg_Wilson "Greg Wilson") (eds.) (**1991**). *[Past, Present, Parallel: A Survey of Available Parallel Computing Systems](http://link.springer.com/book/10.1007%2F978-1-4471-1842-8)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Mark Bromley](Mark_Bromley "Mark Bromley"), [Steven Heller](http://dblp.uni-trier.de/pers/hd/h/Heller:Steven), [Tim McNerney](http://xenia.media.mit.edu/~mcnerney/), [Guy L. Steele Jr.](Mathematician#GSteele "Mathematician") (**1991**). *[Fortran at ten gigaflops: the connection machine convolution compiler](http://dl.acm.org/citation.cfm?id=113458)*. [PLDI '91](http://www.informatik.uni-trier.de/~ley/db/conf/pldi/pldi91.html#BromleyHMS91)
- [Jacek Myczkowski](http://dblp.uni-trier.de/pers/hd/m/Myczkowski:Jacek), [Guy L. Steele Jr.](Mathematician#GSteele "Mathematician") (**1991**). *[Seismic modeling at 14 gigaflops on the connection machine](http://dl.acm.org/citation.cfm?id=126004)*. [Supercomputing '91](http://dl.acm.org/citation.cfm?id=125826&picked=prox&CFID=67541071&CFTOKEN=91822939)
- [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson"), [Zahi S. Abuhamdeh](https://www.linkedin.com/in/zahi-abuhamdeh-703aab1), David C. Douglas, Carl R. Feynman, Mahesh N. Ganmukhi, Jeffrey V. Hill, [W. Daniel Hillis](Mathematician#Hillis "Mathematician"), [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), Margaret A. St. Pierre, David S. Wells, Monica C. Wong, Shaw-Wen Yang, Robert Zak (**1992**). *The Network Architecture of the Connection Machine CM-5*. 4th ACM Symposium on Parallel Algorithms and Architectures, (**1996**). *revised version*. [Journal of Parallel and Distributed Computing](http://www.journals.elsevier.com/journal-of-parallel-and-distributed-computing), Vol. 33, No. 2
- [W. Daniel Hillis](Mathematician#Hillis "Mathematician"), [Lewis W. Tucker](http://dblp.uni-trier.de/pers/hd/t/Tucker:Lewis_W=) (**1993**). *The CM-5 Connection Machine: A Scalable Supercomputer*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 36, No. 11
- [Burton Wendroff](Burton_Wendroff "Burton Wendroff"), [Tony Warnock](Tony_Warnock "Tony Warnock"), [Lewis Stiller](Lewis_Stiller "Lewis Stiller"), [Dean Mayer](index.php?title=Dean_Mayer&action=edit&redlink=1 "Dean Mayer (page does not exist)"), [Ralph Brickner](index.php?title=Ralph_Brickner&action=edit&redlink=1 "Ralph Brickner (page does not exist)") (**1993**). *Bits and pieces: constructing chess endgame databases on parallel and vector architectures*. Applied Numerical Mathematics, Vol. 12, Nos. 1-3
- [Lyle N. Long](http://www.personal.psu.edu/lnl/), [Jacek Myczkowski](http://dblp.uni-trier.de/pers/hd/m/Myczkowski:Jacek) (**1993**). *[Solving the Boltzmann Equation at 61 gigaflops on a 1024-Node CM-5](http://dl.acm.org/citation.cfm?id=169627.169795&coll=DL&dl=GUIDE&CFID=67541071&CFTOKEN=91822939)*. [pdf](http://www.personal.psu.edu/lnl/papers/bgk.pdf)
- [Tamiko Thiel](https://en.wikipedia.org/wiki/Tamiko_Thiel) (**1994**). *[The Design of the Connection Machine](http://tamikothiel.com/theory/cm_txts/di-frames.html)*. [DesignIssues](http://www.mitpressjournals.org/loi/desi), Vol. 10, No. 1, [MIT Press](https://en.wikipedia.org/wiki/MIT_Press)
- [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Synchronized MIMD Computing*. Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/thesis-kuszmaul.pdf)
- [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Third DIMACS Parallel Implementation Challenge, [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University), [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
- [Eric Brewer](Eric_Brewer "Eric Brewer"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *[How to Get Good Performance from the CM-5 Data Network](https://ieeexplore.ieee.org/document/288205)*. [IPPS 1994](https://dblp.uni-trier.de/db/conf/ipps/ipps1994.html), [pdf](https://people.eecs.berkeley.edu/~prabal/resources/osprelim/BK94.pdf)
- [Michael Halbherr](Michael_Halbherr "Michael Halbherr"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou"), [Chris Joerg](Chris_Joerg "Chris Joerg") (**1994**). *[MIMD-Style Parallel Programming with Continuation-Passing Threads](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.16.9812)*. Proceedings of the 2nd International Workshop on Massive Parallelism: Hardware, Software, and Applications

## 1995 ...

- [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1995**). *The StarTech Massively Parallel Chess Program*. [ICCA Journal, Vol. 18, No. 1](ICGA_Journal#18_1 "ICGA Journal"), [pdf](http://supertech.csail.mit.edu/papers/startech.pdf)
- [Robert Blumofe](Robert_Blumofe "Robert Blumofe"), [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou") (**1995**). *Cilk: An Efficient Multithreaded Runtime System*. Proceedings of the Fifth ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming (PPoPP) Santa Barbara, California Pg. 207–216, [pdf](http://supertech.csail.mit.edu/papers/PPoPP95.pdf)
- [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1995**). *Exploiting symmetry on parallel architectures*. Ph.D. thesis
- [Chris Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing* Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)
- [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1996**). *Multilinear Algebra and Chess Endgames*. [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski"), [pdf](http://library.msri.org/books/Book29/files/stiller.pdf)

## External Links

- [Connection Machine from Wikipedia](https://en.wikipedia.org/wiki/Connection_Machine)
- [Richard Feynman and The Connection Machine](http://longnow.org/essays/richard-feynman-connection-machine/) - [The Long Now](https://en.wikipedia.org/wiki/Long_Now_Foundation)
- [The Connection Machine - CHM Revolution](http://www.computerhistory.org/revolution/supercomputers/10/73) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [The Connection Machine](http://www.tamikothiel.com/cm/) by [Tamiko Thiel](https://en.wikipedia.org/wiki/Tamiko_Thiel)
- [Corestore collection: Connection Machine CM-200](http://www.corestore.org/cm200.htm)
- [Gallery of Connection Machine CM-5 Images](http://people.csail.mit.edu/bradley/cm5/) hosted by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul")
- [CM-5 Manuals](http://people.csail.mit.edu/bradley/cm5docs/) hosted by [Bradley C. Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul")
- [CM-5/512 | TOP500 Supercomputer Sites](https://www.top500.org/system/167057)
- [CM-5/1024 | TOP500 Supercomputer Sites](https://www.top500.org/system/166997)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The light panels of [FROSTBURG](https://en.wikipedia.org/wiki/FROSTBURG), a CM-5, on display at the [National Cryptologic Museum](https://en.wikipedia.org/wiki/National_Cryptologic_Museum) in 2005. The panels were used to check the usage of the processing nodes, and to run diagnostics.
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Connection Machine from Wikipedia](https://en.wikipedia.org/wiki/Connection_Machine)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [The Connection Machine](http://www.tamikothiel.com/cm/) by [Tamiko Thiel](https://en.wikipedia.org/wiki/Tamiko_Thiel)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**1985**).  *Fat-Trees: Universal Networks for Hardware-efficient Supercomputing*. [IEEE Transactions on Computers](IEEE#TOC "IEEE"), Vol. 34 , No. 10, [pdf](http://courses.csail.mit.edu/6.896/spring04/handouts/papers/fat_trees.pdf)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [CM-5/1024 | TOP500 Supercomputer Sites](https://www.top500.org/system/166997)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1996**). *Multilinear Algebra and Chess Endgames*. [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski"), [pdf](http://library.msri.org/books/Book29/files/stiller.pdf)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [CM-5/512 | TOP500 Supercomputer Sites](https://www.top500.org/system/167057)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [1993 ACM International Computer Chess Championship (with corrections)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/45699b80a93fde41) by [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), February 19, 1993
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Christopher F. Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing* Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Cooley–Tukey FFT algorithm from Wikipedia](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)

**[Up one Level](Hardware "Hardware")**

