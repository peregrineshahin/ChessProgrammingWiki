---
title: Ryan Hayward
---
**[Home](Home "Home") \* [People](People "People") \* Ryan Hayward**



 [](https://www.ualberta.ca/science/about-us/contact-us/faculty-directory/ryan-hayward) Ryan B. Hayward <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Ryan Bruce Hayward**,  

a Canadian mathematician, computer scientist, and professor at Department of Computing Science at [University of Alberta](University_of_Alberta "University of Alberta"). Ryan Hayward is particularly interested in [Hex](Hex "Hex"), which he learned from [Claude Berge](Mathematician#CBerge "Mathematician"). As member of the University of Alberta's GAMES research group <a id="cite-note-2" href="#cite-ref-2">[2]</a>, he leads a team that developed Hex solver and players. 



### Contents


* [1 Hex Programs](#hex-programs)
	+ [1.1 Wolve](#wolve)
	+ [1.2 MoHex](#mohex)
	+ [1.3 MoHex-CNN](#mohex-cnn)
* [2 Selected Publications](#selected-publications)
	+ [2.1 2000 ...](#2000-...)
	+ [2.2 2005 ...](#2005-...)
	+ [2.3 2010 ...](#2010-...)
	+ [2.4 2015 ...](#2015-...)
	+ [2.5 2020 ...](#2020-...)
* [3 External Links](#external-links)
* [4 References](#references)






After early trials with [Mongoose](https://www.game-ai-forum.org/icga-tournaments/program.php?id=276), the Hex programs [Wolve](https://www.game-ai-forum.org/icga-tournaments/program.php?id=135) ([2008](13th_Computer_Olympiad#Hex "13th Computer Olympiad")) and [MoHex](https://www.game-ai-forum.org/icga-tournaments/program.php?id=555) ([2009](14th_Computer_Olympiad#Hex "14th Computer Olympiad"), [2010](15th_Computer_Olympiad#Hex "15th Computer Olympiad"), [2011](16th_Computer_Olympiad#Hex "16th Computer Olympiad"), [2013](17th_Computer_Olympiad#Hex "17th Computer Olympiad"), [2015](18th_Computer_Olympiad#Hex "18th Computer Olympiad") and [2017](20th_Computer_Olympiad#Hex "20th Computer Olympiad")) won Gold Medals in Hex at the [Computer Olympiad](Computer_Olympiad "Computer Olympiad"). 



### Wolve


Wolve does a truncated [Alpha-Beta](Alpha-Beta "Alpha-Beta") search of two and up to four [plies](Ply "Ply"), considering the huge [Branching Factor](Branching_Factor "Branching Factor") of Hex. 



### MoHex


Since 2009 [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") starts to dominate, and MoHex applies MCTS along with the [UCT](UCT "UCT") framework combined with the allmoves-as-first (AMAF) heuristic to select the best child during tree traversal <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



### MoHex-CNN


MoHex-CNN, which won the [13x13 competition of the 20th Computer Olympiad 2017](20th_Computer_Olympiad#Hex "20th Computer Olympiad") is a [convolutional neural net](Neural_Networks#Convolutional "Neural Networks") (CNN) version of MoHex. At each new node of the Monte-Carlo search tree, a policy CNN biases child selection by initializing child visit and win counts with artificial values <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Selected Publications


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



### 2000 ...


* Ryan Hayward, [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Michael Johanson](index.php?title=Michael_Johanson&action=edit&redlink=1 "Michael Johanson (page does not exist)"), [Morgan Kan](index.php?title=Morgan_Kan&action=edit&redlink=1 "Morgan Kan (page does not exist)"), [Nathan Po](index.php?title=Nathan_Po&action=edit&redlink=1 "Nathan Po (page does not exist)"), [Jack van Rijswijck](index.php?title=Jack_van_Rijswijck&action=edit&redlink=1 "Jack van Rijswijck (page does not exist)") (**2003**). *Solving 7x7 Hex: Virtual Connections and Game-state Reduction*. [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.ru.is/faculty/yngvi/pdf/HaywardBJKPR03.pdf)
* [Gábor Melis](index.php?title=G%C3%A1bor_Melis&action=edit&redlink=1 "Gábor Melis (page does not exist)"), Ryan Hayward (**2003**). *Six wins Hex Tournament*. [ICGA Journal, Vol. 26, No. 4](ICGA_Journal#26_4 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/%7Ehayward/papers/grazRpt.pdf) » [8th Computer Olympiad](8th_Computer_Olympiad#Hex "8th Computer Olympiad")


### 2005 ...


* Ryan Hayward, [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Michael Johanson](index.php?title=Michael_Johanson&action=edit&redlink=1 "Michael Johanson (page does not exist)"), [Morgan Kan](index.php?title=Morgan_Kan&action=edit&redlink=1 "Morgan Kan (page does not exist)"), [Nathan Po](index.php?title=Nathan_Po&action=edit&redlink=1 "Nathan Po (page does not exist)"), [Jack van Rijswijck](index.php?title=Jack_van_Rijswijck&action=edit&redlink=1 "Jack van Rijswijck (page does not exist)") (**2005**). *Solving 7x7 Hex with domination, fill-in, and virtual connections*. Theoretical Computer Science, 349(2):123–139, 2005. [pdf](http://www.ru.is/faculty/yngvi/pdf/HaywardBJKPR05.pdf)
* [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), Ryan Hayward, [Michael Johanson](index.php?title=Michael_Johanson&action=edit&redlink=1 "Michael Johanson (page does not exist)"), [Jack van Rijswijck](index.php?title=Jack_van_Rijswijck&action=edit&redlink=1 "Jack van Rijswijck (page does not exist)") (**2006**). *Dead Cell Analysis in Hex and the Shannon Game.* In Graph Theory in Paris: Proceedings of a Conference in Memory of [Claude Berge](Mathematician#CBerge "Mathematician") (CT'04 Paris), pp. 45–60, 2006. [zipped ps](http://sites.google.com/site/javhar1/DeadCellAnalysis.zip)
* Ryan Hayward, [Jack van Rijswijck](index.php?title=Jack_van_Rijswijck&action=edit&redlink=1 "Jack van Rijswijck (page does not exist)") (**2006**). *Hex and Combinatorics*. Discrete Math 306, [pdf](http://webdocs.cs.ualberta.ca/%7Ehayward/papers/Elsevier.pdf)
* Ryan Hayward (**2006**). *Six Wins Hex tournament*. [ICGA Journal, Vol. 29, No 3](ICGA_Journal#29_3 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/rptTorino.pdf) » [11th Computer Olympiad](11th_Computer_Olympiad#Hex "11th Computer Olympiad")
* Ryan Hayward, [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2006**). *[Automatic Strategy Verification for Hex](http://link.springer.com/chapter/10.1007/978-3-540-75538-8_10)*. [CG 2006](CG_2006 "CG 2006"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/verify.pdf)
* [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)"), Ryan Hayward (**2008**). *[Probing the 4-3-2 Edge Template in Hex](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_21)*. [CG 2008](CG_2008 "CG 2008"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/probe432.pdf)
* [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2009**). *Wolve 2008 wins Hex tournament*. [ICGA Journal, Vol. 32, No. 1](ICGA_Journal#32_1 "ICGA Journal") » [13th Computer Olympiad](13th_Computer_Olympiad#Hex "13th Computer Olympiad")
* [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)"), [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward (**2009**). *Solving 8×8 Hex*. [IJCAI-09](http://ijcai.org/papers09/contents.php), [pdf](http://ijcai.org/papers09/Papers/IJCAI09-091.pdf)
* [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2009**). *MoHex wins Hex tournament*. [ICGA Journal, Vol. 32, No. 2](ICGA_Journal#32_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/rptPamplona.pdf) » [14th Computer Olympiad](14th_Computer_Olympiad#Hex "14th Computer Olympiad")


### 2010 ...


* [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)"), [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward (**2010**). *[Hex, Braids, the Crossing Rule, and XH-Search](http://www.springerlink.com/content/y8298h5713143289/)*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/xhsearch.pdf)
* [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2010**). *MoHex wins Hex Tournament*. [ICGA Journal, Vol. 33, No. 3](ICGA_Journal#33_3 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/rptKanazawa.pdf) » [15th Computer Olympiad](15th_Computer_Olympiad#Hex "15th Computer Olympiad")
* [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2010**). *Solving Hex: Beyond Humans*. [CG 2010](CG_2010 "CG 2010"), [pdf](http://webdocs.cs.ualberta.ca/%7Ehayward/papers/beyond.pdf)
* [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2010**). *Monte Carlo Tree Search in Hex*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 4, [pdf](http://webdocs.cs.ualberta.ca/%7Ehayward/papers/mcts-hex.pdf)
* [Henry Brausen](index.php?title=Henry_Brausen&action=edit&redlink=1 "Henry Brausen (page does not exist)"), Ryan Hayward, [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Abdul Qadir](index.php?title=Abdul_Qadir&action=edit&redlink=1 "Abdul Qadir (page does not exist)"), [David Spies](index.php?title=David_Spies&action=edit&redlink=1 "David Spies (page does not exist)") (**2011**). *[Blunder Cost in Go and Hex](http://link.springer.com/chapter/10.1007/978-3-642-31866-5_19)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* Ryan Hayward (**2012**). *MoHex wins Hex Tournament*. [ICGA Journal, Vol. 35, No. 2](ICGA_Journal#35_2 "ICGA Journal") » [16th Computer Olympiad](16th_Computer_Olympiad#Hex "16th Computer Olympiad")
* Ryan Hayward, [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), [Shih-Chieh Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz") (**2013**). *MOHEX Wins Hex Tournament*. [ICGA Journal, Vol. 36, No. 3](ICGA_Journal#36_3 "ICGA Journal"), [pdf](https://webdocs.cs.ualberta.ca/~hayward/papers/rptYokohama.pdf) » [17th Computer Olympiad](17th_Computer_Olympiad#Hex "17th Computer Olympiad")
* [Shih-Chieh Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz") (**2013**). *MoHex 2.0: a pattern-based MCTS Hex player*. [CG 2013](CG_2013 "CG 2013"), [pdf](https://webdocs.cs.ualberta.ca/~hayward/papers/m2.pdf)
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), Ryan Hayward (**2013**). *Scalable Parallel DFPN Search*. [CG 2013](CG_2013 "CG 2013")


### 2015 ...


* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), Ryan Hayward (**2015**). *Feature Strength and Parallelization of Sibling Conspiracy Number Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), Ryan Hayward (**2015**). *[Sibling Conspiracy Number Search](https://www.aaai.org/ocs/index.php/SOCS/SOCS15/paper/view/11040)*. [SoCS 2015](https://en.wikipedia.org/wiki/Symposium_on_Combinatorial_Search)
* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), Ryan Hayward (**2016**). *[Conspiracy number search with relative sibling scores](https://www.sciencedirect.com/science/article/pii/S0304397516302729)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_(journal)), Vol. 644
* [Kenny Young](index.php?title=Kenny_Young&action=edit&redlink=1 "Kenny Young (page does not exist)"), Ryan Hayward (**2016**). *A Reverse Hex Solver*. [CG 2016](CG_2016 "CG 2016")
* Ryan Hayward, [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Kei Takada](Kei_Takada "Kei Takada"), [Tony van der Valk](index.php?title=Tony_van_der_Valk&action=edit&redlink=1 "Tony van der Valk (page does not exist)") (**2017**). *MOHEX Wins 2015 Hex 11x11 and Hex 13x13 Tournaments*. [ICGA Journal, Vol. 39, No. 1](ICGA_Journal#39_1 "ICGA Journal") » [18th Computer Olympiad](18th_Computer_Olympiad#Hex "18th Computer Olympiad")
* [Noah Weninger](index.php?title=Noah_Weninger&action=edit&redlink=1 "Noah Weninger (page does not exist)"), Ryan Hayward (**2017**). *Exploring Positional Linear Go*. [Advances in Computer Games 15](Advances_in_Computer_Games_15 "Advances in Computer Games 15"), [pdf](https://webdocs.cs.ualberta.ca/~hayward/papers/lgo.pdf)
* Ryan Hayward, [Noah Weninger](index.php?title=Noah_Weninger&action=edit&redlink=1 "Noah Weninger (page does not exist)") (**2017**). *Hex 2017: MoHex wins the 11x11 and 13x13 tournaments*. [ICGA Journal, Vol. 39, Nos. 3-4](ICGA_Journal#39_34 "ICGA Journal") » [20th Computer Olympiad 2017](20th_Computer_Olympiad#Hex "20th Computer Olympiad")
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), Ryan Hayward (**2017**). *Focused Depth-first Proof Number Search using Convolutional Neural Networks for the Game of Hex*. [IJCAI 2017](Conferences#IJCAI2017 "Conferences")
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Siqi Yan](index.php?title=Siqi_Yan&action=edit&redlink=1 "Siqi Yan (page does not exist)"), Ryan Hayward, [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2018**). *A transferable neural network for Hex*. [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")
* [Chao Gao](index.php?title=Chao_Gao&action=edit&redlink=1 "Chao Gao (page does not exist)"), [Kei Takada](Kei_Takada "Kei Takada"), Ryan Hayward (**2019**). *Hex 2018: MoHex3HNN over DeepEzo*. [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal") » [21st Computer Olympiad 2018](index.php?title=21st_Computer_Olympiad&action=edit&redlink=1 "21st Computer Olympiad (page does not exist)")
* [Nicolas Fabiano](index.php?title=Nicolas_Fabiano&action=edit&redlink=1 "Nicolas Fabiano (page does not exist)"), Ryan Hayward (**2019**). *New Hex Patterns for Fill and Prune*. [Advances in Computer Games 16](Advances_in_Computer_Games_16 "Advances in Computer Games 16")


### 2020 ...


* Ryan Hayward, et al. (**2021**). *BoxOff is NP-complete*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")


## External Links


* [Webpage of Ryan B. Hayward](http://webdocs.cs.ualberta.ca/%7Ehayward/)
* [Ryan Hayward - Faculty of Science - University of Alberta](https://www.ualberta.ca/science/about-us/contact-us/faculty-directory/ryan-hayward)
* [Ryan Hayward's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/person.php?id=146)
* [The Mathematics Genealogy Project - Ryan Hayward](http://genealogy.math.ndsu.nodak.edu/id.php?id=105076)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Ryan Hayward - Faculty of Science - University of Alberta](https://www.ualberta.ca/science/about-us/contact-us/faculty-directory/ryan-hayward)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [The University of Alberta GAMES Group](http://webdocs.cs.ualberta.ca/~games/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Broderick Arneson](index.php?title=Broderick_Arneson&action=edit&redlink=1 "Broderick Arneson (page does not exist)"), Ryan Hayward, [Philip Henderson](index.php?title=Philip_Henderson&action=edit&redlink=1 "Philip Henderson (page does not exist)") (**2010**). *Monte Carlo Tree Search in Hex*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 4, [pdf](http://webdocs.cs.ualberta.ca/~hayward/papers/mcts-hex.pdf)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Ryan Hayward, [Noah Weninger](index.php?title=Noah_Weninger&action=edit&redlink=1 "Noah Weninger (page does not exist)") (**2017**). *Hex 2017: MoHex wins the 11x11 and 13x13 tournaments*. [ICGA Journal, Vol. 39, Nos. 3-4](ICGA_Journal#39_34 "ICGA Journal")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Publications of Ryan B. Hayward](http://webdocs.cs.ualberta.ca/~hayward/publications.html)

**[Up one level](People "People")**







 
