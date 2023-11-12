---
title: Star Socrates
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Star Socrates**



[ [Socrates](Mathematician#Socrates "Mathematician") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**\*Socrates**,  

a parallel chess program, developed by a team from [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") and [Sandia National Laboratories](https://en.wikipedia.org/wiki/Sandia_National_Laboratories) <a id="cite-note-2" href="#cite-ref-2">[2]</a> headed by [Charles Leiserson](Charles_Leiserson "Charles Leiserson"). Primary programmers were [Don Dailey](Don_Dailey "Don Dailey"), co-author of [Socrates](Socrates "Socrates") and [Titan](Titan "Titan") aka [Socrates II](https://en.wikipedia.org/wiki/Socrates_II), on which \*Socrates was based on, and [Chris Joerg](Chris_Joerg "Chris Joerg"). Further contributers were [Robert Blumofe](Robert_Blumofe "Robert Blumofe"), [Matteo Frigo](Matteo_Frigo "Matteo Frigo"), [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), [Eric Brewer](Eric_Brewer "Eric Brewer"), [Michael Halbherr](Michael_Halbherr "Michael Halbherr"), [Rolf Riesen](index.php?title=Rolf_Riesen&action=edit&redlink=1 "Rolf Riesen (page does not exist)") (Sandia) and [Yuli Zhou](Yuli_Zhou "Yuli Zhou"). 



### Contents


* [1 Massively Parallel Chess](#massively-parallel-chess)
* [2 History of \*Socrates](#history-of-.2asocrates)
* [3 Acknowledgments](#acknowledgments)
* [4 Description](#description)
* [5 Awards](#awards)
* [6 See also](#see-also)
* [7 Publications](#publications)
* [8 External Links](#external-links)
	+ [8.1 Chess Program](#chess-program)
	+ [8.2 Misc](#misc)
* [9 References](#references)






Quote by [Chris Joerg](Chris_Joerg "Chris Joerg") and [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++
Computer chess provides a good testbed for understanding dynamic [MIMD](https://en.wikipedia.org/wiki/MIMD)-style computations. To investigate the programming issues, we engineered a parallel chess program called *Socrates, which running on [NCSA's](University_of_Illinois_at_Urbana-Champaign#NCSA "University of Illinois at Urbana-Champaign") 512 processor [CM-5](Connection_Machine "Connection Machine"), tied for third in the [1994 ACM International Computer Chess Championship](ACM_1994 "ACM 1994"). *Socrates uses the [Jamboree](Jamboree "Jamboree") algorithm to search game trees in parallel and uses the [Cilk 1.0](Cilk "Cilk") language and run-time system to express and to schedule the computation. In order to obtain good performance for chess, we use several mechanisms not directly provided by Cilk, such as aborting computations and directly accessing the active message layer to implement a global transposition table distributed across the processors. We found that we can use the critical path C and the total work W to predict the performance of our chess programs. Empirically *Socrates runs in time

```


```C++
T ≈ 0.95C + 1.09W/P  

on P processors. For best-ordered uniform trees of height h and degree d the average available parallelism in Jamboree search is

ϴ((d/2)h/2)

*Socrates searching real chess trees under tournament time controls yields average available parallelism of over 1000. 

```

## History of \*Socrates


History of \*Socrates by [Chris Joerg](Chris_Joerg "Chris Joerg") from his Ph. D. thesis <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```C++
We began work on this program in May of 1994. [Don Dailey](Don_Dailey "Don Dailey") and [Larry Kaufman](Larry_Kaufman "Larry Kaufman") of [Heuristic Software](Heuristic_Software "Heuristic Software") provided us with a version of [Socrates](Socrates "Socrates"), their serial chess program. During May and June we parallelized the program using [Cilk](Cilk "Cilk"), focusing mainly on the [search algorithm](Search "Search") and the [transposition table](Transposition_Table "Transposition Table"). During June Dailey visited [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") to help tune the program, but we spent most of June simply getting the parallel version of the program to work correctly. In late June, we entered *Socrates in the [1994 ACM International Computer Chess Championship](ACM_1994 "ACM 1994") in Cape May, New Jersey. We ran the program on a 512-node [CM-5](Connection_Machine "Connection Machine") at the [National Center for Supercomputing Applications](University_of_Illinois_at_Urbana-Champaign#NCSA "University of Illinois at Urbana-Champaign") (NCSA) at the [University of Illinois](University_of_Illinois_at_Urbana-Champaign "University of Illinois at Urbana-Champaign"). Despite the fact that we had begun working on the program less than two months earlier, the program ran reliable and finished in third place. 

```

## Acknowledgments


by [Chris Joerg](Chris_Joerg "Chris Joerg") from his Ph. D. thesis:




```C++
I am especially grateful to my thesis supervisor, Professor [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), who has led the Cilk project. I still remember the day he came to my office and recruited me. He explained how he realized I had other work to do but he wanted to know if I would like to help out part time" on implementing a chess program using PCM. It sounded like a interesting project, so I agreed, but only after making it clear that I could only work part time because I had my thesis project to work on. Well, part time" became full time", and at times full time" became much more than that. Eventually, the chess program was completed, and the chess tournament came and went, yet I still kept working on the PCM system (which was now turning into Cilk). Ultimately, I realized that I should give up on my other project and make Cilk my thesis instead. Charles is a wonderful supervisor and under his leadership, the Cilk project has achieved more than I ever expected. Charles' influence can also be seen in this write-up itself. He has helped me turn this thesis into a relatively coherent document, and he has also pointed out some of my more malodorous grammatical constructions.

```


```C++
The Cilk project has been a team effort and I am indebted to all the people who have contributed in some way to the Cilk system: Bobby Blumofe, Feng Ming Dong, Matteo Frigo, Shail Aditya Gupta, Michael Halbherr, Charles Leiserson, Bradley Kuszmaul, Rob Miller, Keith Randall, Rolf Riesen, Andy Shaw, Richard Tauriello, and Yuli Zhou. Their contributions are noted throughout this document.

```


```C++
I thank, along with the members of the Cilk team, the past and present members of the Computation Structures Group. These friends have made MIT both a challenging and a fun place to be. In particular I should thank Michael Halbherr. He not only began the work that lead to the PCM system, but he tried many times to convince me to switch my thesis to this system. It took a while, but I finally realized he was right.

```


```C++
I am also indebted to Don Dailey and Larry Kaufman, both formerly of Heuristic Software. They wrote the serial Socrates program on which *Socrates is based. In addition, Don and I spent many long nights debugging, testing, and improving (or at least trying to improve) *Socrates. Most of this time we even had fun.

```


```C++
Professor Arvind, Dr. Andy Boughton, and Dr. Greg Papadopoulus also deserve many thanks. They provided me the freedom, encouragement, and support to work on a wide range of exciting projects throughout my years at MIT. 

```

## Description


Description given in 1995 from the [ICGA](ICGA "ICGA")-site <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++
The Star Socrates 2.0 chess program developed at the MIT Laboratory for Computer Science, will be running on the 1824 node [Intel Paragon](Paragon "Paragon") parallel supercomputer located at Sandia National Laboratories. The lead programmers are Don Dailey and Christopher F.Joerg and the project team is lead by Prof. Leiserson. Heuristic Software provided the original Socrates program on which StarSocrates was originally based. The Paragon is about 50 feet long and weighs about 30,000 pounds. Each node consists of two 50MHz [i860](I860 "I860") processors with either 16 or 32MB of memory. The program currently runs on both the [Connection Machine CM-5](Connection_Machine "Connection Machine") and the Intel Paragon. 


```

## Awards


Awards for Cilk Technology & Research <a id="cite-note-6" href="#cite-ref-6">[6]</a> :




```C++
1995, Second Place in the 1995 International Computer Chess Association's Eighth Computer Chess World Championship for *Socrates 2.0, a chess-playing program written in Cilk. 

```

## See also


* [CilkChess](CilkChess "CilkChess")
* [Socrates](Socrates "Socrates")
* [StarTech](StarTech "StarTech")


## Publications


* [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, 1994, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
* [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Alan Sherman](Alan_Sherman "Alan Sherman") (**1995**). *\*Socrates 2.0 Beats Grandmaster Sagalchik*. [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal")
* [Robert Blumofe](Robert_Blumofe "Robert Blumofe"), [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul"), [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), [Yuli Zhou](Yuli_Zhou "Yuli Zhou") (**1995**). *Cilk: An Efficient Multithreaded Runtime System* Proceedings of the Fifth [ACM SIGPLAN](ACM#SIG "ACM") Symposium on Principles and Practice of Parallel Programming (PPoPP), [pdf](http://supertech.csail.mit.edu/papers/PPoPP95.pdf)
* [Chris Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing*. Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)


## External Links


### Chess Program


* [Star Socrates' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=181)


### Misc


* [Star from Wikipedia](https://en.wikipedia.org/wiki/Star)
* [Socrates from Wikipedia](https://en.wikipedia.org/wiki/Socrates)
* [Terri Lyne Carrington](Category:Terri_Lyne_Carrington "Category:Terri Lyne Carrington"): [The Mosaic Project](https://en.wikipedia.org/wiki/The_Mosaic_Project_(album)) - Forest Star, [Tokyo Jazz, September 05, 2010](http://www.tokyo-jazz.com/2010/en/program/halla0905d.html), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Tineke Postma](Category:Tineke_Postma "Category:Tineke Postma"), [Esperanza Spalding](Category:Esperanza_Spalding "Category:Esperanza Spalding"), [Ingrid Jensen](https://en.wikipedia.org/wiki/Ingrid_Jensen) and [Chihiro Yamanaka](https://en.wikipedia.org/wiki/Chihiro_Yamanaka) as guest
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Bust of Socrates. [Marble](https://en.wikipedia.org/wiki/Marble), Roman copy after a Greek original from the 4th century BC. From the [Quintili Villa](https://en.wikipedia.org/wiki/Villa_of_the_Quintilii) on the [Via Appia](https://en.wikipedia.org/wiki/Appian_Way), [Socrates from Wikipedia](https://en.wikipedia.org/wiki/Socrates)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [8th World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6cd6ed), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1995_WCCC/1995%20WCCC.062303014.sm.pdf), Courtesy of [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chris Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing* Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Star Socrates' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=181)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Awards for Cilk Technology & Research](http://www.cilk.com/company/awards/)

**[Up one Level](Engines "Engines")**







 
