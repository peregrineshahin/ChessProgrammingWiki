---
title: BestFirst
---
**[Home](Home "Home") * [Search](Search "Search") * Best-First**

\[ Breadth-First Node order <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Best-First Search** is a [state space search](https://en.wikipedia.org/wiki/State_space_search) to traverse [nodes](Node "Node") of tree-like data structures (i. e. [search trees](Search_Tree "Search Tree")) in [breadth-first](https://en.wikipedia.org/wiki/Breadth-first_search) manner. It is usually implemented with a [priority queue](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)") instead of the [FIFO](Queue "Queue") of breadth-first <a id="cite-note-2" href="#cite-ref-2">[2]</a> , to expand the most promising node of one level first. Best-first turns a uninformed breadth-first into an informed search. Since all nodes of one level must be saved until their child nodes at the next level have been generated, the space complexity and memory requirement is proportional to the number of nodes at the deepest level.

Best-first algorithms like [A\*](https://en.wikipedia.org/wiki/A*_search_algorithm) are used for path finding in [combinatorial search](https://en.wikipedia.org/wiki/Combinatorial_search) and [puzzles](https://en.wikipedia.org/wiki/Puzzle). [Iterative deepening](Iterative_Deepening "Iterative Deepening") is a technique to turn [depth-first searches](Depth-First "Depth-First") into best-first with the advantage space grows [linear](https://en.wikipedia.org/wiki/Linear_growth) rather than [exponential](https://en.wikipedia.org/wiki/Exponential_growth) with increasing [search depth](Depth "Depth") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, as applied for instance in [IDA\*](https://en.wikipedia.org/wiki/IDA*).

## Contents

- [1 Two-Player](#two-player)
- [2 Some Chess Programs](#some-chess-programs)
- [3 See also](#see-also)
- [4 Publications](#publications)
  - [4.1 1960 ...](#1960-...)
  - [4.2 1970 ...](#1970-...)
  - [4.3 1980 ...](#1980-...)
  - [4.4 1990 ...](#1990-...)
  - [4.5 2000 ...](#2000-...)
  - [4.6 2010 ...](#2010-...)
  - [4.7 2020 ...](#2020-...)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Two-Player

Following best-first algorithms were invented and implemented for computer chess programs as well for other two-player [zero-sum](<https://en.wikipedia.org/wiki/Zero-sum_(game_theory)>) board [game](Games "Games") players with [perfect information](https://en.wikipedia.org/wiki/Perfect_information):

- [B\*](B* "B*")
- [Bandwidth Search](index.php?title=Bandwidth_Search&action=edit&redlink=1 "Bandwidth Search (page does not exist)")
- [Best-First Minimax Search](Best-First_Minimax_Search "Best-First Minimax Search")
- [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search")
- [FSSS-Minimax](Ari_Weinstein#FSSS-Minimax "Ari Weinstein")
- [LCF](Richard_P._Cochran#LCF "Richard P. Cochran")
- [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
- [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
- [M & N Procedure](James_R._Slagle#MNprocedure "James R. Slagle")
- [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
- [SSS\* and Dual\*](SSS*_and_Dual* "SSS* and Dual*")
- [UCT](UCT "UCT")

## Some Chess Programs

- [Centaur](Centaur "Centaur")
- [HiTech B\*](HiTech "HiTech")
- [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
- [Rocinante](Rocinante "Rocinante")

## See also

- [Depth-First](Depth-First "Depth-First")
- [MTD(f)](</MTD(f)> "MTD(f)")
- [NegaC\*](NegaC* "NegaC*")
- [Perft(15)](Perft#15 "Perft")
- [Priority Queue](index.php?title=Priority_Queue&action=edit&redlink=1 "Priority Queue (page does not exist)")
- [Queue](Queue "Queue")
- [SSS\* and Dual\* as MT](SSS*_and_Dual*#SSStarandDualStarAsMT "SSS* and Dual*")

## Publications

## 1960 ...

- [James R. Slagle](James_R._Slagle "James R. Slagle") (**1963**). *Game Trees, M & N Minimaxing, and the M & N alpha-beta procedure.* Artificial Intelligence Group Report 3, UCRL-4671, University of California
- [Peter Hart](https://en.wikipedia.org/wiki/Peter_E._Hart), [Nils Nilsson](https://en.wikipedia.org/wiki/Nils_John_Nilsson), [Bertram Raphael](https://en.wikipedia.org/wiki/Bertram_Raphael) (**1968**). *A Formal Basis for the Heuristic Determination of Minimum Cost Paths*. [IEEE Transactions on Systems Science and Cybernetics](IEEE#TSSC "IEEE"), Vol. SSC-4, No. 2, [pdf](https://www.cs.auckland.ac.nz/courses/compsci709s2c/resources/Mike.d/astarNilsson.pdf), introducing [A\*](https://en.wikipedia.org/wiki/A*_search_algorithm)

## 1970 ...

- [Larry Harris](Larry_Harris "Larry Harris") (**1973**). *The bandwidth heuristic search*. [3. IJCAI 1973](Conferences#IJCAI1973 "Conferences"), [pdf](http://www.ijcai.org/Past%20Proceedings/IJCAI-73/PDF/004.pdf)
- [Larry Harris](Larry_Harris "Larry Harris") (**1974**). *Heuristic Search under Conditions of Error*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 5, No. 3, also as (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
- [Larry Harris](Larry_Harris "Larry Harris") (**1975**). *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [4. IJCAI 1975](Conferences#IJCAI1975 "Conferences"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [Larry Harris](Larry_Harris "Larry Harris") (**1977**). *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")

## 1980 ...

- [Judea Pearl](Judea_Pearl "Judea Pearl") (**1981**). *Heuristic search theory: A survey of recent results*. [IJCAI-81](Conferences#IJCAI1981 "Conferences"), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-81-VOL%201/PDF/100.pdf)
- [Judea Pearl](Judea_Pearl "Judea Pearl") (**1984**). *Heuristics: Intelligent Search Strategies for Computer Problem Solving*. [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld"), [Tony Marsland](Tony_Marsland "Tony Marsland"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1985**). *Is Best First Search Really Best?* Technical Report TR 85-16, Department of Computer Science, [University of Alberta](University_of_Alberta "University of Alberta").
- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") (**1986**). *Selective Search versus Brute Force.* [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
- [Richard Karp](Richard_Karp "Richard Karp"), [Yanjun Zhang](Yanjun_Zhang "Yanjun Zhang") (**1988**). *[A randomized parallel branch-and-bound procedure](https://dl.acm.org/citation.cfm?id=62212.62240)*. [STOC '88](https://dblp.uni-trier.de/db/conf/stoc/stoc88.html)
- [Anup K. Sen](index.php?title=Anup_K._Sen&action=edit&redlink=1 "Anup K. Sen (page does not exist)"), [Amitava Bagchi](Amitava_Bagchi "Amitava Bagchi") (**1989**). *Fast Recursive Formulations for Best-First Search that allow Controlled use of Memory*. [IJCAI 1989](Conferences#IJCAI "Conferences"), [pdf](http://www.ijcai.org/Past%20Proceedings/IJCAI-89-VOL1/PDF/047.pdf)

## 1990 ...

- [Steven Skiena](Steven_Skiena "Steven Skiena") (**1990**). *Breadth-First and Depth-First Search.* §3.2.5 in [Implementing Discrete Mathematics: Combinatorics and Graph Theory with Mathematica](http://www.amazon.com/exec/obidos/ASIN/0521806860/ref=nosim/weisstein-20), [Addison-Wesley](https://en.wikipedia.org/wiki/Addison-Wesley)
- [Nageshwara Rao Vempaty](index.php?title=Nageshwara_Rao_Vempaty&action=edit&redlink=1 "Nageshwara Rao Vempaty (page does not exist)"), [Vipin Kumar](index.php?title=Vipin_Kumar&action=edit&redlink=1 "Vipin Kumar (page does not exist)"), [Richard Korf](Richard_Korf "Richard Korf") (**1991**). *Depth-First vs Best-First Search*. [AAAI-91](Conferences#AAAI-91 "Conferences"), [pdf](https://www.aaai.org/Papers/AAAI/1991/AAAI91-067.pdf)
- [Richard Korf](Richard_Korf "Richard Korf") (**1993**). *Linear-Space Best-First Search.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 62, No. 1, [pdf](http://www.aaai.org/Papers/AAAI/1992/AAAI92-082.pdf)
- [Richard Korf](Richard_Korf "Richard Korf"), [Max Chickering](Max_Chickering "Max Chickering") (**1993**). *[Best-first Minimax Search: First Results](http://www.aaai.org/Library/Symposia/Fall/1993/fs93-02-006.php).* [AAAI-93](Conferences#AAAI-93 "Conferences")
- [Weixiong Zhang](Mathematician#WZhang "Mathematician"), [Richard Korf](Richard_Korf "Richard Korf") (**1993**). *[Depth-first vs. best-first search: New results](http://dl.acm.org/citation.cfm?id=1867385)*. [AAAI-93](Conferences#AAAI-93 "Conferences")
- [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1994**). *[The Principle of Pressure in Chess](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=EJurXJ4AAAAJ&cstart=40&citation_for_view=EJurXJ4AAAAJ:TQgYirikUcIC)*. TAINN 1994
- [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1995, 2015**). *Best-First Fixed Depth Game Tree Search in Practice.* [IJCAI-95](Conferences#IJCAI1995 "Conferences"), [arXiv:1505.01603](https://arxiv.org/abs/1505.01603)
- [Richard Korf](Richard_Korf "Richard Korf"), [Max Chickering](Max_Chickering "Max Chickering") (**1996**). *[Best-first minimax search](https://www.microsoft.com/en-us/research/publication/best-first-minimax-search/)*. [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 84, Nos 1-2
- [Aske Plaat](Aske_Plaat "Aske Plaat"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1996**). *Best-First Fixed-Depth Minimax Algorithms.* [Artificial Intelligence](<https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)>), Vol. 87
- [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**1999**). *Proof for the Equivalence Between Some Best-First Algorithms and Depth-First Algorithms for AND/OR Trees*. Proceedings of the Korea-Japan Joint Workshop on Algorithms and Computation

## 2000 ...

- [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Richard P. Cochran](Richard_P._Cochran "Richard P. Cochran") (**2000**). *[A Least-Certainty Heuristic for Selective Search](http://link.springer.com/chapter/10.1007/3-540-45579-5_1)*. [CG 2000](CG_2000 "CG 2000"), [pdf](http://people.cs.umass.edu/~utgoff/papers/springer-lcf.pdf) » [LCF](Richard_P._Cochran#LCF "Richard P. Cochran")
- [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**2002**). *[Proof for the Equivalence Between Some Best-First Algorithms and Depth-First Algorithms for AND/OR Trees](http://ci.nii.ac.jp/naid/110006376599)*. [IEICE transactions on information and systems](http://ci.nii.ac.jp/vol_issue/nels/AA10826272/ISS0000408668_en.html)

## 2010 ...

- [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Alex Fukunaga](index.php?title=Alex_Fukunaga&action=edit&redlink=1 "Alex Fukunaga (page does not exist)"), [Adi Botea](Adi_Botea "Adi Botea") (**2012**). *Evaluation of a Simple, Scalable, Parallel Best-First Search Strategy*. [arXiv:1201.3204](https://arxiv.org/abs/1201.3204)
- [Ari Weinstein](Ari_Weinstein "Ari Weinstein"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [Sergiu Goschin](index.php?title=Sergiu_Goschin&action=edit&redlink=1 "Sergiu Goschin (page does not exist)") (**2013**). *[Rollout-based Game-tree Search Outprunes Traditional Alpha-beta](http://proceedings.mlr.press/v24/weinstein12a.html)*. [PMLR](http://proceedings.mlr.press/), Vol. 24 » [FSSS-Minimax](Ari_Weinstein#FSSS-Minimax "Ari Weinstein")
- [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Bo-Han Lin](index.php?title=Bo-Han_Lin&action=edit&redlink=1 "Bo-Han Lin (page does not exist)"), [Chia-Hui Chang](Chia-Hui_Chang "Chia-Hui Chang") (**2015**). *[Job-Level Alpha-Beta Search](https://ir.nctu.edu.tw/handle/11536/124541)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 1
- [Tom Everitt](index.php?title=Tom_Everitt&action=edit&redlink=1 "Tom Everitt (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter") (**2015**). *Analytical Results on the BFS vs. DFS Algorithm Selection Problem. Part I: Tree Search*. Australasian Conference on Artificial Intelligence, [pdf](https://pdfs.semanticscholar.org/1b4b/c878b2d068214e39b258ee250e5b8889e84c.pdf)
- [Tom Everitt](index.php?title=Tom_Everitt&action=edit&redlink=1 "Tom Everitt (page does not exist)"), [Marcus Hutter](Marcus_Hutter "Marcus Hutter") (**2015**). *Analytical Results on the BFS vs. DFS Algorithm Selection Problem: Part II: Graph Search*. Australasian Conference on Artificial Intelligence
- [Alex Fukunaga](index.php?title=Alex_Fukunaga&action=edit&redlink=1 "Alex Fukunaga (page does not exist)"), [Adi Botea](Adi_Botea "Adi Botea"), [Yuu Jinnai](index.php?title=Yuu_Jinnai&action=edit&redlink=1 "Yuu Jinnai (page does not exist)"), [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto") (**2017**). *A Survey of Parallel A\**. [arXiv:1708.05296](https://arxiv.org/abs/1708.05296)

## 2020 ...

- [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)") (**2021**). *Completeness of Unbounded Best-First Game Algorithms*. [arXiv:2109.09468](https://arxiv.org/abs/2109.09468)

## Forum Posts

- [Breadth-first search: revisiting](http://www.talkchess.com/forum/viewtopic.php?t=40384) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011
- [Help with Best-First Select-Formula](http://www.talkchess.com/forum/viewtopic.php?t=44165) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 23, 2012
- [Re: Perft(15): comparison of estimates with Ankan's result](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=9) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 26, 2017 » [Perft(15)](Perft#15 "Perft")

## External Links

- [Best-first search from Wikipedia](https://en.wikipedia.org/wiki/Best-first_search)
- [Ian Carr](Category:Ian_Carr "Category:Ian Carr") & [Nucleus](Category:Nucleus "Category:Nucleus") - Sidewalk, live at the [BBC 1980](https://en.wikipedia.org/wiki/BBC), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat.: [Allan Holdsworth](Category:Allan_Holdsworth "Category:Allan Holdsworth"), [Brian Smith](<https://en.wikipedia.org/wiki/Brian_Smith_(musician)>), [Tim Whitehead](https://de.wikipedia.org/wiki/Tim_Whitehead), [Geoff Castle](https://de.wikipedia.org/wiki/Geoff_Castle), [Chucho Merchán](https://en.wikipedia.org/wiki/Chucho_Merch%C3%A1n), [Nic France](https://de.wikipedia.org/wiki/Nic_France), [Chris Fletcher](https://www.allmusic.com/artist/chris-fletcher-mn0000384453/credits)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Breadth-first search from Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Boost Graph Library: Breadth-First Search](http://www.boost.org/doc/libs/1_43_0/libs/graph/doc/breadth_first_search.html)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Richard Korf Video](Richard_Korf#JudeaPearl "Richard Korf") at [Judea Pearl Symposium](Judea_Pearl#Symposium "Judea Pearl"), 2010

**[Up one Level](Search "Search")**

