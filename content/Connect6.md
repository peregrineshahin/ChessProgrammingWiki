---
title: Connect6
---
**[Home](Home "Home") * [Games](Games "Games") * Connect6**

\[ Connect6 on a large board <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Connect6**, Connect(m,n,6,2,1)

a [two-player](https://en.wikipedia.org/wiki/Two-player_game) [abstract strategy](https://en.wikipedia.org/wiki/Abstract_strategy_game) board game of the k-in-a-row family similar to [Gomoku](index.php?title=Gomoku&action=edit&redlink=1 "Gomoku (page does not exist)"), introduced in 2003 by [I-Chen Wu](I-Chen_Wu "I-Chen Wu") and presented at [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11") in 2005. Black and White alternately place **two** stones of their own colour on empty intersections of a Go-like board, except that Black (the first player) places one stone only for the first move <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The one who gets six or more stones in a row (horizontally, vertically or diagonally) first wins the game. Most often, Connect6 is played on a 19x19 Go board, proposed for professional players is a 59x59 board <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Since 2006, Connect6 is played regularely by computers at the [Computer Olympiad](Computer_Olympiad "Computer Olympiad") organized by the [ICGA](ICGA "ICGA") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. [Search](Search "Search") algorithms used are [Alpha-Beta](Alpha-Beta "Alpha-Beta") / [MTD(f)](</MTD(f)> "MTD(f)") along with [VCF](index.php?title=VCF&action=edit&redlink=1 "VCF (page does not exist)") search (Victory by Continuous Four) to find a path to win in the endgame <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [UCT](UCT "UCT"), as well as [Proof-Number Search](Proof-Number_Search "Proof-Number Search") also in conjunction with the novel relevance-zone-oriented proof (RZOP) search used to solve various openings, such as the Mickey Mouse opening <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Contents

- [1 Selected Programs](#selected-programs)
- [2 GUI](#gui)
- [3 Computer Olympiads](#computer-olympiads)
- [4 See also](#see-also)
- [5 Selected Publications](#selected-publications)
  - [5.1 2005 ...](#2005-...)
  - [5.2 2010 ...](#2010-...)
  - [5.3 2015 ...](#2015-...)
  - [5.4 2020 ...](#2020-...)
- [6 External Links](#external-links)
- [7 References](#references)

## Selected Programs

- [Bitstronger](https://www.game-ai-forum.org/icga-tournaments/program.php?id=558) aka [Cloudict](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)") by [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hao Cui](index.php?title=Hao_Cui&action=edit&redlink=1 "Hao Cui (page does not exist)"), [Ruijian Wang](index.php?title=Ruijian_Wang&action=edit&redlink=1 "Ruijian Wang (page does not exist)"), [Siran Lin](index.php?title=Siran_Lin&action=edit&redlink=1 "Siran Lin (page does not exist)")
- [Kavalan](https://www.game-ai-forum.org/icga-tournaments/program.php?id=507) by [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen")
- [MeinStein](https://www.game-ai-forum.org/icga-tournaments/program.php?id=508) by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos")
- [MoreThenFive](https://www.game-ai-forum.org/icga-tournaments/program.php?id=696) by [Jiajia Guo](index.php?title=Jiajia_Guo&action=edit&redlink=1 "Jiajia Guo (page does not exist)"), [Xiaomeng Yang](index.php?title=Xiaomeng_Yang&action=edit&redlink=1 "Xiaomeng Yang (page does not exist)"), [Liang Yunzhao](index.php?title=Liang_Yunzhao&action=edit&redlink=1 "Liang Yunzhao (page does not exist)"), [Jianbo Zhao](index.php?title=Jianbo_Zhao&action=edit&redlink=1 "Jianbo Zhao (page does not exist)")
- [NCTU6](https://www.game-ai-forum.org/icga-tournaments/program.php?id=231) by [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hsiu-Chen Chang](index.php?title=Hsiu-Chen_Chang&action=edit&redlink=1 "Hsiu-Chen Chang (page does not exist)")
- [X6](https://www.game-ai-forum.org/icga-tournaments/program.php?id=232) by [Sih-Yuan Liou](index.php?title=Sih-Yuan_Liou&action=edit&redlink=1 "Sih-Yuan Liou (page does not exist)"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen")

## GUI

- [ConnectMore](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)") by [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)") written in [Python 3](Python "Python") - for [Cloudict](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)") and more ... <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## [](https://github.com/lang010/ConnectMore) [Computer Olympiads](Computer_Olympiad "Computer Olympiad")

- [11th Computer Olympiad, Turin 2006](11th_Computer_Olympiad#Connect6 "11th Computer Olympiad")
- [12th Computer Olympiad, Amsterdam 2007](12th_Computer_Olympiad#Connect6 "12th Computer Olympiad")
- [13th Computer Olympiad, Beijing 2008](13th_Computer_Olympiad#Connect6 "13th Computer Olympiad")
- [14th Computer Olympiad, Pamplona 2009](14th_Computer_Olympiad#Connect6 "14th Computer Olympiad")
- [15th Computer Olympiad, Kanazawa 2010](15th_Computer_Olympiad#Connect6 "15th Computer Olympiad")
- [16th Computer Olympiad, Tilburg 2011](16th_Computer_Olympiad#Connect6 "16th Computer Olympiad")
- [17th Computer Olympiad, Yokohama 2013](17th_Computer_Olympiad#Connect6 "17th Computer Olympiad")

## See also

- [Connect Four](Connect_Four "Connect Four")
- [Gomoku](index.php?title=Gomoku&action=edit&redlink=1 "Gomoku (page does not exist)")
- [Renju](index.php?title=Renju&action=edit&redlink=1 "Renju (page does not exist)")

## Selected Publications

## 2005 ...

- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Dei-Yen Huang](Dei-Yen_Huang "Dei-Yen Huang") (**2005**). *[A New Family of k -in-a-Row Games](http://link.springer.com/chapter/10.1007/11922155_14)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11"), [pdf](http://www.connect6.org/k-in-a-row.pdf)
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Dei-Yen Huang](Dei-Yen_Huang "Dei-Yen Huang"), [Hsiu-Chen Chang](index.php?title=Hsiu-Chen_Chang&action=edit&redlink=1 "Hsiu-Chen Chang (page does not exist)") (**2005**). *Connect6*. [ICGA Journal, Vol. 28, No. 4](ICGA_Journal#28_4 "ICGA Journal"), [pdf](http://www.connect6.org/connect6.pdf)
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2006**). *NCTU6 wins Connect6 tournament*. [ICGA Journal, Vol. 29, No. 3](ICGA_Journal#29_3 "ICGA Journal") » [11th Computer Olympiad](11th_Computer_Olympiad#Connect6 "11th Computer Olympiad")
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2007**). *X6 wins Connect6 tournament*. [ICGA Journal, Vol. 30, No. 2](ICGA_Journal#30_2 "ICGA Journal") » [12th Computer Olympiad](12th_Computer_Olympiad#Connect6 "12th Computer Olympiad")
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2008**). *NCTU6-Lite wins Connect6 tournament*. [ICGA Journal, Vol. 31, No. 4](ICGA_Journal#31_4 "ICGA Journal") » [13th Computer Olympiad](13th_Computer_Olympiad#Connect6 "13th Computer Olympiad")

**2009**

- [Sheng-Hao Chiang](index.php?title=Sheng-Hao_Chiang&action=edit&redlink=1 "Sheng-Hao Chiang (page does not exist)"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2009**). *On Drawn K-In-A-Row Games*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12")
- [Changming Xu](index.php?title=Changming_Xu&action=edit&redlink=1 "Changming Xu (page does not exist)"), [Zongmin Ma](index.php?title=Zongmin_Ma&action=edit&redlink=1 "Zongmin Ma (page does not exist)"), [Junjie Tao](index.php?title=Junjie_Tao&action=edit&redlink=1 "Junjie Tao (page does not exist)"), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2009**). *Enhancements of Proof Number Search in Connect6*. [IEEE](IEEE "IEEE") Control and Decision Conference
- [Changming Xu](index.php?title=Changming_Xu&action=edit&redlink=1 "Changming Xu (page does not exist)"), [Zongmin Ma](index.php?title=Zongmin_Ma&action=edit&redlink=1 "Zongmin Ma (page does not exist)"), [Xinhe Xu](Xinhe_Xu "Xinhe Xu") (**2009**). *A method to construct knowledge table-base in k-in-a-row games*. [SAC 2009](http://www.informatik.uni-trier.de/~ley/db/conf/sac/sac2009.html#XuMX09)
- [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2009**). *Bit wins Connect6 tournament*. [ICGA Journal, Vol. 32, No. 2](ICGA_Journal#32_2 "ICGA Journal") » [14th Computer Olympiad](14th_Computer_Olympiad#Connect6 "14th Computer Olympiad")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2009**). *The Bitboard Design and Bitwise Computing in Connect Six*. [14th Game Programming Workshop](Conferences#GPW "Conferences")

## 2010 ...

- [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2010**). *Relevance-Zone-Oriented Proof Search for Connect6*. Ph.D. thesis
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2010**). *[Relevance-Zone-Oriented Proof Search for Connect6](https://www.researchgate.net/publication/224159031_Relevance-Zone-Oriented_Proof_Search_for_Connect6)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 3
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2010**). *MoreThenFive wins the Connect-6 Tournament*. [ICGA Journal, Vol. 33, No. 3](ICGA_Journal#33_3 "ICGA Journal") » [15th Computer Olympiad](15th_Computer_Olympiad#Connect6 "15th Computer Olympiad")
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [Der-Johng Sun](Der-Johng_Sun "Der-Johng Sun"), [Yi-Chih Chan](Yi-Chih_Chan "Yi-Chih Chan"), [Bo-Ting Chen](index.php?title=Bo-Ting_Chen&action=edit&redlink=1 "Bo-Ting Chen (page does not exist)") (**2010**). *[Job-Level Proof-Number Search for Connect6](http://link.springer.com/chapter/10.1007/978-3-642-17928-0_2)*. [CG 2010](CG_2010 "CG 2010")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2010**). *[Searching for Stage Proof Number in Connect6](https://www.semanticscholar.org/paper/Searching-for-Stage-Proof-Number-in-Connect6-Yen-Yang/2de70372893e8773b12391f75d2b964ea7fb6df2)*. [TAAI 2010](index.php?title=TAAI_2010&action=edit&redlink=1 "TAAI 2010 (page does not exist)")

**2011**

- [Sheng-Hao Chiang](index.php?title=Sheng-Hao_Chiang&action=edit&redlink=1 "Sheng-Hao Chiang (page does not exist)"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2011**). *[Drawn K-In-A-Row Games](http://dl.acm.org/citation.cfm?id=2010786)*. [Theoretical Computer Science, Volume 412](http://www.informatik.uni-trier.de/~ley/db/journals/tcs/tcs412.html#ChiangWL11)
- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hsin-Ti Tsai](index.php?title=Hsin-Ti_Tsai&action=edit&redlink=1 "Hsin-Ti Tsai (page does not exist)"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Yi-Shan Lin](index.php?title=Yi-Shan_Lin&action=edit&redlink=1 "Yi-Shan Lin (page does not exist)"), [Chieh-Min Chang](index.php?title=Chieh-Min_Chang&action=edit&redlink=1 "Chieh-Min Chang (page does not exist)"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2011**). *[Temporal Difference Learning for Connect6](https://www.conftool.net/acg13/index.php?page=browseSessions&form_session=5)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2011**). *Two-Stage Monte Carlo Tree Search for Connect6*. [IEEE Transactions on Computational Intelligence and AI in Games, Vol. 3](http://www.informatik.uni-trier.de/~ley/db/journals/tciaig/tciaig3.html#YenY11)

**2012**

- [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Peiyu Liu](index.php?title=Peiyu_Liu&action=edit&redlink=1 "Peiyu Liu (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)") (**2012**). *[A Node-based Parallel Game Tree Algorithm Using GPUs](http://ieeexplore.ieee.org/document/6337852/)*. CLUSTER 2012, [pdf](https://pdfs.semanticscholar.org/be21/d7b9b91957b700aab4ce002e6753b826ff54.pdf)
- [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Kuo-Yuan Kao](Kuo-Yuan_Kao "Kuo-Yuan Kao"), [Tai-Ning Yang](index.php?title=Tai-Ning_Yang&action=edit&redlink=1 "Tai-Ning Yang (page does not exist)") (**2012**). *[Bitboard Knowledge Base System and Elegant Search Architectures for Connect6](http://www.sciencedirect.com/science/article/pii/S0950705112001293)*. [Knowledge-Based Systems](https://www.journals.elsevier.com/knowledge-based-systems/), Vol. 34

**2013**

- [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Hao-Hua Kang](index.php?title=Hao-Hua_Kang&action=edit&redlink=1 "Hao-Hua Kang (page does not exist)"), [Hung-Hsuan Lin](Hung-Hsuan_Lin "Hung-Hsuan Lin"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin"), [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [Chieh-Min Chang](index.php?title=Chieh-Min_Chang&action=edit&redlink=1 "Chieh-Min Chang (page does not exist)"), [Ting-Fu Liao](Ting-Fu_Liao "Ting-Fu Liao") (**2013**). *Dependency-Based Search for Connect6*. [CG 2013](CG_2013 "CG 2013")
- [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2013**). *MOBILE 6 Wins Connect6 Tournament*. [ICGA Journal, Vol. 36, No. 3](ICGA_Journal#36_3 "ICGA Journal") » [17th Computer Olympiad](17th_Computer_Olympiad#Connect6 "17th Computer Olympiad")
- [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Ping-Jung Tseng](https://dblp.uni-trier.de/pers/hd/t/Tseng:Ping=Jung) (**2013**). *[Bitboard Connection Code Design for Connect6](https://ieeexplore.ieee.org/document/6783902)*. [TAAI 2013](index.php?title=TAAI_2013&action=edit&redlink=1 "TAAI 2013 (page does not exist)")

**2014**

- [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [Bing-Tsung Chiang](Bing-Tsung_Chiang "Bing-Tsung Chiang"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Chang-Shing Lee](Chang-Shing_Lee "Chang-Shing Lee") (**2014**). *Job-Level Algorithms for Connect6 Opening Position Analysis*. [ECAI CGW 2014](index.php?title=ECAI_CGW_2014&action=edit&redlink=1 "ECAI CGW 2014 (page does not exist)")

## 2015 ...

- [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [Bing-Tsung Chiang](Bing-Tsung_Chiang "Bing-Tsung Chiang"), [Wen-Jie Tseng](Wen-Jie_Tseng "Wen-Jie Tseng"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Chang-Shing Lee](Chang-Shing_Lee "Chang-Shing Lee") (**2015**). *Job-Level Algorithms for Connect6 Opening Book Construction*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
- [Liang Li](index.php?title=Liang_Li&action=edit&redlink=1 "Liang Li (page does not exist)"), [Hong Liu](index.php?title=Hong_Liu&action=edit&redlink=1 "Hong Liu (page does not exist)"), [Hao Wang](index.php?title=Hao_Wang&action=edit&redlink=1 "Hao Wang (page does not exist)"), [Taoying Liu](index.php?title=Taoying_Liu&action=edit&redlink=1 "Taoying Liu (page does not exist)"), [Wei Li](index.php?title=Wei_Li&action=edit&redlink=1 "Wei Li (page does not exist)") (**2015**). *[A Parallel Algorithm for Game Tree Search Using GPGPU](http://ieeexplore.ieee.org/document/6868996/)*. [IEEE Transactions on Parallel and Distributed Systems](IEEE#TPDS "IEEE"), Vol. 26, No. 8
- [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang") (**2016**). *Building Connect6 opening by using the Monte Carlo tree search*. [ICACI 2016](https://dblp.uni-trier.de/db/conf/icaci/icaci2016.html)
- [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2019**). *Kavalan wins Connect6 tournament*. [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal") » [21st Computer Olympiad 2018](index.php?title=21st_Computer_Olympiad&action=edit&redlink=1 "21st Computer Olympiad (page does not exist)")

## 2020 ...

- [Jung-Kuei Yang](Jung-Kuei_Yang "Jung-Kuei Yang"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2020**). *The Connect6 tournament of the 2019 Computer Olympiad*. [ICGA Journal, Vol. 42, No. 1](ICGA_Journal#42_1 "ICGA Journal") » [22nd Computer Olympiad](index.php?title=22nd_Computer_Olympiad&action=edit&redlink=1 "22nd Computer Olympiad (page does not exist)")

## External Links

- [Connect6 from Wikipedia](https://en.wikipedia.org/wiki/Connect6)
- [Introduction to Connect6](http://java.csie.nctu.edu.tw/~icwu/connect6/connect6.html)
- [Connect6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=18)
- [m,n,k-game from Wikipedia](https://en.wikipedia.org/wiki/M,n,k-game)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A game of Connect6 played on a large white board, originally posted to [Flickr](https://en.wikipedia.org/wiki/Flickr) as [Closeup of a Connect 6 game](https://www.flickr.com/photos/41894169422@N01/363886773) by [Nelson Pavlosky](https://www.flickr.com/people/41894169422@N01), January 18, 2007, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Connect6 from Wikipedia](https://en.wikipedia.org/wiki/Connect6)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Connect6 from Wikipedia](https://en.wikipedia.org/wiki/Connect6)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Introduction to Connect6](http://java.csie.nctu.edu.tw/~icwu/connect6/connect6.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Connect6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=18)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [MoreThenFive (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/program.php?id=696)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Ping-Hung Lin](Ping-Hung_Lin "Ping-Hung Lin") (**2010**). *[Relevance-Zone-Oriented Proof Search for Connect6](https://www.researchgate.net/publication/224159031_Relevance-Zone-Oriented_Proof_Search_for_Connect6)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 3
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [GitHub - lang010/ConnectMore: ConnectMore is a UI for Cloudict of the game Connect6, written by Python 3](https://github.com/lang010/ConnectMore/)

**[Up one Level](Games "Games")**

