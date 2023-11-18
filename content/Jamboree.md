---
title: Jamboree
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Parallel Search](Parallel_Search "Parallel Search") \* Jamboree**


**Jamboree algorithm**,  

a parallelized version of the [Scout](Scout "Scout") search algorithm. Similar to the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), the idea is that all of the testing of any child that is not the first one, is done in parallel, and any tests that fail are sequentially valued. Jamboree search was introduced by [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") in his [1994](Timeline#1994 "Timeline") thesis *Synchronized MIMD Computing* <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 


Jamboree was used in the massive parallel chess programs [StarTech](StarTech "StarTech") and [\*Socrates](Star_Socrates "Star Socrates"). It sequentialize full-window searches for values, because, while their authors are willing to take a chance that an [empty window](Null_Window "Null Window") search will be squandered work, they are not willing to take the chance that a full-window search (which does not prune very much) will be squandered work. 



## See also


* [ABDADA](ABDADA "ABDADA")
* [NegaScout](NegaScout "NegaScout")
* [Parallel Alpha-Beta](Cilk#ParallelAlphaBeta "Cilk") in [Cilk](Cilk "Cilk")
* [Scout](Scout "Scout")
* [\*Socrates](Star_Socrates "Star Socrates")
* [StarTech](StarTech "StarTech")
* [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


## Publications


<a id="cite-note-4" href="#cite-ref-4">[4]</a>



* [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Synchronized MIMD Computing*. Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/thesis-kuszmaul.pdf)
* [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
* [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1995**). *The StarTech Massively Parallel Chess Program*. [ICCA Journal, Vol. 18, No. 1](ICGA_Journal#18_1 "ICGA Journal"), [pdf](http://supertech.csail.mit.edu/papers/startech.pdf)
* [Chris Joerg](Chris_Joerg "Chris Joerg") (**1996**). *The Cilk System for Parallel Multithreaded Computing*. Ph. D. thesis, Department of Electrical Engineering and Computer Science, [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/joerg-phd-thesis.pdf)


## External Links


* [Jamboree (Scouting) from Wikipedia](https://en.wikipedia.org/wiki/Jamboree_%28Scouting%29)
* [World Scout Jamboree from Wikipedia](https://en.wikipedia.org/wiki/World_Scout_Jamboree)
* [Robert Baden-Powell, 1st Baron Baden-Powell from Wikipedia](https://en.wikipedia.org/wiki/Robert_Baden-Powell,_1st_Baron_Baden-Powell)
* [Jamborees History / World Jamboree / World Events / Events / Information & Events / Home - World Organization of the Scout Movement](http://www.scout.org/en/information_events/events/world_events/world_jamboree/jamborees_history)
* [Ralph Towner](Category:Ralph_Towner "Category:Ralph Towner") and [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie") - [The Donkey Jamboree](https://en.wikipedia.org/wiki/Slide_Show_(album)), [Hamburg](https://en.wikipedia.org/wiki/Hamburg) 1984, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Synchronized MIMD Computing*. Ph. D. Thesis, Department of Electrical Engineering and Computer Science, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), [pdf](http://supertech.csail.mit.edu/papers/thesis-kuszmaul.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [MIMD From Wikipedia](https://en.wikipedia.org/wiki/MIMD)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> based on Figure 5: Algorithm Jamboree from [Chris Joerg](Chris_Joerg "Chris Joerg"), [Bradley Kuszmaul](Bradley_Kuszmaul "Bradley Kuszmaul") (**1994**). *Massively Parallel Chess*. Proceedings of the Third DIMACS Parallel Implementation Challenge, [pdf](http://supertech.csail.mit.edu/papers/dimacs94.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [SuperTech Paper Listing](http://supertech.csail.mit.edu/papers.html)

**[Up one level](Parallel_Search "Parallel Search")**







 
