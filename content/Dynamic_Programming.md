---
title: Dynamic Programming
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Algorithms](Algorithms "Algorithms") * Dynamic Programming**

**Dynamic Programming**, (DP)

a mathematical, algorithmic optimization method of [recursively](Recursion "Recursion") nesting [overlapping sub problems](https://en.wikipedia.org/wiki/Overlapping_subproblems) of [optimal substructure](https://en.wikipedia.org/wiki/Optimal_substructure) inside larger decision problems. The term DP was coined by [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") in the 50s not as programming in the sense of producing computer code, but mathematical programming, planning or optimization similar to [linear programming](https://en.wikipedia.org/wiki/Linear_programming), devoted to the study of multistage processes. These processes are composed of sequences of operations in which the outcome of those preceding may be used to guide the course of future ones <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## DP in Computer Chess

In computer chess, dynamic programming is applied in [depth-first](Depth-First "Depth-First") [search](Search "Search") with [memoization](https://en.wikipedia.org/wiki/Memoization) aka using a [transposition table](Transposition_Table "Transposition Table") and/or other [hash tables](Hash_Table "Hash Table") while traversing a [tree](Search_Tree "Search Tree") of overlapping sub problems aka child positions after making a move by one side in top-down manner, gaining from stored [positions](Chess_Position "Chess Position") of sibling subtrees due to [transpositions](Transposition "Transposition") and/or common aspects of positions, in particular effective inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework. Another approach of dynamic programming in computer chess or computer games is the application of [retrograde analysis](Retrograde_Analysis "Retrograde Analysis"), to solve a problem by solving subproblems in bottom-up manner starting from terminal nodes <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## See also

- [Markov Models](Michael_L._Littman#MarkovModels "Michael L. Littman") by [Michael L. Littman](Michael_L._Littman "Michael L. Littman")
- [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
- [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning")

## Selected Publications

## 1953 ...

- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1953**). *[An Introduction to the Theory of Dynamic Programming](http://www.rand.org/pubs/reports/R245.html)*. R-245, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1954**). *The Theory of Dynamic Programming*. P-550, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), [pdf](http://www.rand.org/content/dam/rand/pubs/papers/2008/P550.pdf)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1954**). *On a new Iterative Algorithm for Finding the Solutions of Games and Linear Programming Problems*. Technical Report P-473, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), U. S. Air Force Project RAND
- [Samuel Karlin](Mathematician#SKarlin "Mathematician") (**1955**). *[The Stucture of Dynamic Programming Models](http://onlinelibrary.wiley.com/doi/10.1002/nav.3800020408/abstract)*. [Naval Research Logistics](https://en.wikipedia.org/wiki/Naval_Research_Logistics), Vol. 2
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1957**). *Dynamic Programming*. [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1958**). *[Dynamic Programming and Stochastic Control Processes](http://www.sciencedirect.com/science/article/pii/S0019995858800030)*. [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), [Santa Monica, CA](https://en.wikipedia.org/wiki/Santa_Monica,_California), [Information and Control 1](http://www.sciencedirect.com/science/journal/00199958/1/3)

## 1960 ...

- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1960**). *[Sequential Machines, Ambiguity, and Dynamic Programming](http://dl.acm.org/citation.cfm?id=321011)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 7, No. 1
- [Ronald A. Howard](Mathematician#RAHoward "Mathematician") (**1960**). *Dynamic Programming and Markov Processes*. [MIT Press](https://en.wikipedia.org/wiki/MIT_Press), [amazon](https://www.amazon.com/Programming-Processes-Technology-Research-Monographs/dp/0262080095) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman"), [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") (**1962**). *Applied Dynamic Programming*. [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press), [pdf](https://www.rand.org/content/dam/rand/pubs/reports/2006/R352.pdf)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1962**). *[Dynamic Programming Treatment of the Travelling Salesman Problem](http://dl.acm.org/citation.cfm?id=321111)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 9, No. 1, [1961 pdf preprint](http://www.akira.ruc.dk/~keld/teaching/algoritmedesign_f08/Artikler/05/Bellman61.pdf)
- [David Blackwell](Mathematician#DHBlackwell "Mathematician") (**1962**). *[Discrete Dynamic Programming](https://projecteuclid.org/euclid.aoms/1177704593)*. [Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 33, No. 2
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1965**). *[On the Application of Dynamic Programming to the Determination of Optimal Play in Chess and Checkers](http://www.rand.org/pubs/papers/P3013/).* [PNAS](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America)
- [David Blackwell](Mathematician#DHBlackwell "Mathematician") (**1965**). *[Discounted Dynamic Programming](https://projecteuclid.org/euclid.aoms/1177700285)*. [Annals of Mathematical Statistics](https://en.wikipedia.org/wiki/Annals_of_Mathematical_Statistics), Vol. 36, No. 1 <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [David Blackwell](Mathematician#DHBlackwell "Mathematician") (**1967**). *[Positive Dynamic Programming](https://projecteuclid.org/euclid.bsmsp/1200513001)*. [Proc. 5th Berkeley Symposium on Mathematical Statistics and Probability](https://projecteuclid.org/euclid.bsmsp/1200512974)

## 1970 ...

- [David Blackwell](Mathematician#DHBlackwell "Mathematician") (**1976**). *[The Stochastic Processes of Borel Gambling and Dynamic Programming](https://projecteuclid.org/euclid.aos/1176343412)*. [Annals of Statistics](https://en.wikipedia.org/wiki/Annals_of_Statistics), Vol. 4, No. 2
- [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician"), [Averill M. Law](http://www.averill-law.com/about/) (**1977**). *[Art and Theory of Dynamic Programming](http://dl.acm.org/citation.cfm?id=578655)*. [Academic Press](https://en.wikipedia.org/wiki/Academic_Press)
- [Steven E. Shreve](Mathematician#SEShreve "Mathematician"), [Dimitri Bertsekas](Mathematician#DBertsekas "Mathematician") (**1979**). *[Universally Measurable Policies in Dynamic Programming](http://pubsonline.informs.org/doi/abs/10.1287/moor.4.1.15?journalCode=moor)*. [Mathematics of Operations Research](https://en.wikipedia.org/wiki/Mathematics_of_Operations_Research), Vol. 4, No. 1

## 1980 ...

- [David Eppstein](David_Eppstein "David Eppstein"), [Zvi Galil](Mathematician#ZviGalil "Mathematician"), [Raffaele Giancarlo](Mathematician#RGiancarlo "Mathematician") (**1988**). *[Speeding up Dynamic Programming](https://ieeexplore.ieee.org/document/21965)*. [FOCS 1988](https://dblp.uni-trier.de/db/conf/focs/focs88.html)
- [Andrew Barto](Andrew_Barto "Andrew Barto"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Christopher J. C. H. Watkins](https://dblp.uni-trier.de/pers/hd/w/Watkins:Christopher_J=_C=_H=) (**1989**). *[Sequential Decision Problems and Neural Networks](https://papers.nips.cc/paper/194-sequential-decision-problems-and-neural-networks)*. [NIPS 1989](https://dblp.uni-trier.de/db/conf/nips/nips1989.html)

## 1990 ...

- [David Eppstein](David_Eppstein "David Eppstein"), [Zvi Galil](Mathematician#ZviGalil "Mathematician"), [Raffaele Giancarlo](Mathematician#RGiancarlo "Mathematician"), [Giuseppe F. Italiano](Mathematician#GFItaliano "Mathematician") (**1990**). *Sparse Dynamic Programming*. [SODA 1990](https://dblp.uni-trier.de/db/conf/soda/soda90.html), [pdf](http://www.cs.ust.hk/mjg_lib/bibs/DPSu/DPSu.Files/p513-eppstein.pdf)
- [Dimitri Bertsekas](Mathematician#DBertsekas "Mathematician") (**1996, 2017**). *[Dynamic Programming and Optimal Control](http://www.athenasc.com/dpbook.html)*. [Athena Scientific](http://www.athenasc.com/index.html)

## 2000 ...

- [Dimitri Bertsekas](Mathematician#DBertsekas "Mathematician") (**2001**). *Neuro-Dynamic Programming: An Overview*. [Encyclopedia of Optimization](http://link.springer.com/referencework/10.1007%2F0-306-48332-7), [pdf](http://web.mit.edu/people/dimitrib/NDP_Encycl.pdf), [slides as pdf](http://www.math.s.chiba-u.ac.jp/~yasuda/open2all/Neuro/NDP_Overview.pdf)
- [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") (**2002**). *Richard Bellman on the Birth of Dynamic Programming*. [Operations Research](https://en.wikipedia.org/wiki/Operations_Research:_A_Journal_of_the_Institute_for_Operations_Research_and_the_Management_Sciences), Vol. 50, No. 1, [pdf](http://www.cas.mcmaster.ca/~se3c03/journal_papers/dy_birth.pdf)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**2003**). *[Dynamic Programming](http://dl.acm.org/citation.cfm?id=862270)*. [Dover Publications](https://en.wikipedia.org/wiki/Dover_Publications)
- [Sanjoy Dasgupta](Mathematician#SDasgupta "Mathematician"), [Christos H. Papadimitriou](Mathematician#CHPapadimitriou "Mathematician"), [Umesh Vazirani](Mathematician#UVVazirani "Mathematician") (**2006**). *[Algorithms](http://www.cs.berkeley.edu/%7Evazirani/algorithms.html)*. [McGraw-Hill](https://en.wikipedia.org/wiki/McGraw-Hill), [Chapter 6 Dynamic programming](https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf) (pdf)
- [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Jérémie Mary](J%C3%A9r%C3%A9mie_Mary "Jérémie Mary"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud") (**2006**). *Learning for stochastic dynamic programming*. [pdf](http://www.lri.fr/%7Egelly/paper/lfordp.pdf), [pdf](http://www.grappa.univ-lille3.fr/~mary/paper/lfordp.pdf)
- [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Jérémie Mary](J%C3%A9r%C3%A9mie_Mary "Jérémie Mary") (**2007**). *Active learning in regression, with application to stochastic dynamic programming*. ICINCO and CAP, 2007, [pdf](http://www.grappa.univ-lille3.fr/~mary/paper/ldsfordp.pdf)
- [Warren B. Powell](http://dblp.uni-trier.de/pers/hd/p/Powell:Warren_B=) (**2007**). *Approximate Dynamic Programming - Solving the Curses of Dimensionality*. [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)

## 2010 ...

- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**2010**). *[Dynamic Programming](http://press.princeton.edu/titles/9234.html)*. With a new introduction by [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician"), [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)
- [Andrew Barto](Andrew_Barto "Andrew Barto") (**2010**). *Adaptive Real-Time Dynamic Programming*. Encyclopedia of Machine Learning 2010, Springer
- [Rémi Munos](R%C3%A9mi_Munos "Rémi Munos") (**2010**). *Approximate dynamic programming*. In [Olivier Sigaud](http://www.isir.upmc.fr/?op=view_profil&id=28&old=N&lang=en) and [Olivier Buffet](http://www.loria.fr/~buffet/), editors, [Markov Decision Processes in Artificial Intelligence](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1848211678.html), chapter 3, ISTE Ltd and [John Wiley & Sons Inc.](http://eu.wiley.com/WileyCDA/), [pdf](http://researchers.lille.inria.fr/~munos/papers/files/MDPIA_chap3.pdf)
- [Warren B. Powell](http://dblp.uni-trier.de/pers/hd/p/Powell:Warren_B=) (**2011**). *[Approximate Dynamic Programming - Solving the Curses of Dimensionality](http://adp.princeton.edu/)*. 2nd edition, [Wiley](https://en.wikipedia.org/wiki/John_Wiley_%26_Sons)
- [Dimitri Bertsekas](Mathematician#DBertsekas "Mathematician") (**2013**). *[Abstract Dynamic Programming](http://www.athenasc.com/abstractdp.html)*. [Athena Scientific](http://www.athenasc.com/index.html)
- [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman"), [Stuart E. Dreyfus](Mathematician#SEDreyfus "Mathematician") (**2015**). *[Applied Dynamic Programming](http://press.princeton.edu/titles/100.html)*. [Princeton University Press](https://en.wikipedia.org/wiki/Princeton_University_Press)
- [Andrew Barto](Andrew_Barto "Andrew Barto") (**2017**). *Adaptive Real-Time Dynamic Programming*. [Encyclopedia of Machine Learning and Data Mining 2017](https://link.springer.com/referencework/10.1007%2F978-1-4899-7687-1), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)

## External Links

- [Dynamic programming from Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)

[Algorithms that use dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming#Algorithms_that_use_dynamic_programming)

- [Bellman equation from Wikipedia](https://en.wikipedia.org/wiki/Bellman_equation)
- [Algorithms/Dynamic Programming - Wikibooks](https://en.wikibooks.org/wiki/Algorithms/Dynamic_Programming)
- [Stochastic dynamic programming from Wikipedia](https://en.wikipedia.org/wiki/Stochastic_dynamic_programming)
- [Dynamic Programming – From Novice to Advanced – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/)
- [Tutorial for Dynamic Programming | CodeChef](https://www.codechef.com/wiki/tutorial-dynamic-programming)
- [Dynamic Programming Archives - GeeksforGeeks](http://www.geeksforgeeks.org/category/dynamic-programming/)
- [Dynamic Programming Practice Problems](https://people.cs.clemson.edu/~bcdean/dp_practice/)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1953**). *[An Introduction to the Theory of Dynamic Programming](http://www.rand.org/pubs/reports/R245.html)*. R-245, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1965**). *[On the Application of Dynamic Programming to the Determination of Optimal Play in Chess and Checkers](http://www.rand.org/pubs/papers/P3013/).* [PNAS](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Markov chain from Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [David Blackwell and Dynamic Programming](http://users.stat.umn.edu/~sudde001/personal_page/DBDP.pdf) (pdf) by [William Sudderth](Mathematician#WSudderth "Mathematician")

**[Up one Level](Algorithms "Algorithms")**

