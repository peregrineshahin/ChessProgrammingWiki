---
title: Parabelle
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Parabelle**



[ Quadruplane <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Parabelle**,  

an experimental chess program of the early 1980s developed by [Fred Popowich](Fred_Popowich "Fred Popowich") and [Tony Marsland](Tony_Marsland "Tony Marsland") at [University of Alberta](University_of_Alberta "University of Alberta"), written in [C](C "C"), to research on [parallel search](Parallel_Search "Parallel Search"). In particular addressing search overhead and communication overhead, the [speedup](Parallel_Search#Speedup "Parallel Search") of [principal variation splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search") with various setups was investigated, later revised by [Tim Breitkreutz](Tim_Breitkreutz "Tim Breitkreutz") et al. to run Parabelle under *network multiprocessor package* (NMP), a [PVM](https://en.wikipedia.org/wiki/Parallel_Virtual_Machine)-like [message passing](https://en.wikipedia.org/wiki/Message_passing) library <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Parabelle was initially based on [Ken Thompson's](Ken_Thompson "Ken Thompson") program [TinkerBelle](Belle "Belle") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> , and was itself base for further projects such as the program [Abyss](Abyss "Abyss"), which was subject of research on [selective search extensions](Extensions "Extensions") in the domain of [Chinese Chess](Chinese_Chess "Chinese Chess"), and also played tournaments <a id="cite-note-5" href="#cite-ref-5">[5]</a> . 



## Performance


The program was tested performing 5- and 6-[ply](Ply "Ply") searches on 24 positions of the [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test") with various transposition table implementations. 
Despite huge savings in nodes visited using the global table, the increased communication overhead by far decreased the net result, and only a [depth](Depth "Depth") limited shared table (depth < 3) came close to the performance of a local, depth limited transposition table, which turned out best for this hardware configuration - speedup with [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) (σ) as given in the 1983 paper <a id="cite-note-7" href="#cite-ref-7">[7]</a> .





|  #
 |  5 Ply
 |  6 Ply
 |
| --- | --- | --- |
|  Proc
 |  Speedup
 |  σ
 |  Speedup
 |  σ
 |
|  2
 |  1.89
 |  0.10
 |  1.92
 |  0.33
 |
|  3
 |  2.59
 |  0.29
 |  2.66
 |  0.51
 |
|  4
 |  3.10
 |  0.52
 |  3.27
 |  0.75
 |


## See also


* [Abyss](Abyss "Abyss")
* [Belle](Belle "Belle")
* [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")
* [Principal Variation Splitting](Parallel_Search#PrincipalVariationSplitting "Parallel Search")


## Publications


* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1983**). *A Multiprocessor Tree-searching System Design.* Technical Report TR 83-6, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta")
* [Fred Popowich](Fred_Popowich "Fred Popowich"), [Tony Marsland](Tony_Marsland "Tony Marsland"). (**1983**) *Parabelle: Experience with a Parallel Chess Program.* Technical Report 83-7. Computing Science Department, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR83-7.pdf)
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Parallel Game-Tree Search.* [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 7, No. 4, pp. 442-452. [1984 pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/parallel.pdf) (Draft)
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Fred Popowich](Fred_Popowich "Fred Popowich") (**1985**). *Corrections to "Parallel Game Tree-Search"*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 7, No. 6
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Tim Breitkreutz](Tim_Breitkreutz "Tim Breitkreutz"), [Steve Sutphen](index.php?title=Steve_Sutphen&action=edit&redlink=1 "Steve Sutphen (page does not exist)") (**1991**). *A Network Multiprocessor for Experiments in Parallelism.* Concurrency: Practice and Experience, Vol. 3, No. 3, pp. 203-219. [pdf](https://webdocs.cs.ualberta.ca/~tony/RecentPapers/cpe.pdf)


## External Links


* [para- - Wiktionary](https://en.wiktionary.org/wiki/para-)
* [belle - Wiktionary](https://en.wiktionary.org/wiki/belle)
* [Parabelle](https://en.wikipedia.org/wiki/Parabelle) - [Reassembling The Icons](https://en.wikipedia.org/wiki/Reassembling_the_Icons) (2010), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Armstrong Whitworth F.K.10](https://en.wikipedia.org/wiki/Armstrong_Whitworth_F.K.10) (1916) a British two-seat [quadruplane](https://en.wikipedia.org/wiki/Multiplane_(aeronautics)#Quadruplanes), [image](https://commons.wikimedia.org/wiki/File:Armstrong_Whitworth_F.K.10.jpg) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Tony Marsland](Tony_Marsland "Tony Marsland"), [Tim Breitkreutz](Tim_Breitkreutz "Tim Breitkreutz"), [Steve Sutphen](index.php?title=Steve_Sutphen&action=edit&redlink=1 "Steve Sutphen (page does not exist)") (**1991**). *A Network Multiprocessor for Experiments in Parallelism.* Concurrency: Practice and Experience, Vol. 3, No. 3, pp. 203-219. [pdf](https://webdocs.cs.ualberta.ca/~tony/RecentPapers/cpe.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> The original name for [Belle](Belle "Belle") was T.Belle (the [US Chess Federation](https://en.wikipedia.org/wiki/United_States_Chess_Federation) required an initial). TinkerBelle was the "invention" of [Tony Marsland](Tony_Marsland "Tony Marsland"), and nothing [Ken Thompson](Ken_Thompson "Ken Thompson") knew about or approved
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Tinker Bell from Wikipedia](https://en.wikipedia.org/wiki/Tinker_Bell) a fictional character from [J. M. Barrie's](https://en.wikipedia.org/wiki/J._M._Barrie) 1904 play and 1911 novel [Peter and Wendy](https://en.wikipedia.org/wiki/Peter_and_Wendy)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Chun Ye](Chun_Ye "Chun Ye") (**1992**). *Experiments in Selective Search Extensions*. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> B.A. Bowen, R.J.A. Buhr (**1980**). *The Logical Design of Multiple Microprocessor Systems*. [Prentice Hall](https://en.wikipedia.org/wiki/Prentice_Hall), [amazon](https://www.amazon.com/Logical-Design-Multiple-Microprocessor-Systems/dp/0135399084)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Fred Popowich](Fred_Popowich "Fred Popowich"), [Tony Marsland](Tony_Marsland "Tony Marsland"). (**1983**) *Parabelle: Experience with a Parallel Chess Program.* Technical Report 83-7. Computing Science Department, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR83-7.pdf), pp. 6

**[Up one Level](Engines "Engines")**







 
