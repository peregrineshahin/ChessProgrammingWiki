---
title: Othello
---
**[Home](Home "Home") \* [Games](Games "Games") \* Othello**



[_board.jpg) Reversi/Othello [[1]](#cite_note-1)
**Othello**,   

or differing in not having a defined starting position, **Reversi**, is a [two-player](https://en.wikipedia.org/wiki/Two-player_game) [zero-sum](https://en.wikipedia.org/wiki/Zero-sum_%28game_theory%29) and [perfect information](https://en.wikipedia.org/wiki/Perfect_information) [abstract strategy](https://en.wikipedia.org/wiki/Abstract_strategy) [board game](https://en.wikipedia.org/wiki/Board_game), usually played on a board with 8 rows and 8 columns and a set of light and a dark turnable pieces for each side. The player's goal is to have a majority of their colored pieces showing at the end of the game, turning over as many of their opponent's pieces as possible. The dark player makes the first move from the starting position, alternating with the light player. Each player has to place a piece on the board such that there exists at least one straight (horizontal, vertical, or diagonal) occupied line of opponent pieces between the new piece and another own piece. After placing the piece, the side turns over (flips, captures) all opponent pieces lying on any straight lines between the new piece and any anchoring own pieces. 
|}



### Contents


* [1 Othello Programming](#Othello_Programming)
	+ [1.1 Search](#Search)
	+ [1.2 Evaluation](#Evaluation)
	+ [1.3 Bitboards](#Bitboards)
* [2 Solving Othello](#Solving_Othello)
* [3 Computer Olympiads](#Computer_Olympiads)
* [4 Photos](#Photos)
* [5 Othello Programs](#Othello_Programs)
* [6 See also](#See_also)
* [7 Publications](#Publications)
	+ [7.1 1979](#1979)
	+ [7.2 1980 ...](#1980_...)
	+ [7.3 1985 ...](#1985_...)
	+ [7.4 1990 ...](#1990_...)
	+ [7.5 1995 ...](#1995_...)
	+ [7.6 2000 ...](#2000_...)
	+ [7.7 2005 ...](#2005_...)
	+ [7.8 2010 ...](#2010_...)
	+ [7.9 2015 ...](#2015_...)
* [8 Forum Posts](#Forum_Posts)
* [9 External Links](#External_Links)
* [10 References](#References)






Writing an Othello program [[2]](#cite_note-2) is an appealing and interesting challenge. Beside the dedicated Othello programmers [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson"), [Michael Buro](Michael_Buro "Michael Buro"), [Mark Brockington](Mark_Brockington "Mark Brockington"), [Paul Hsieh](Paul_Hsieh "Paul Hsieh"), and [Andrea Zinno](index.php?title=Andrea_Zinno&action=edit&redlink=1 "Andrea Zinno (page does not exist)"), to name a few, many chess programmers were and are busy in this domain as well. Already in 1981 [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") wrote a commercial Reversi program, marketed as *Reversi Sensory Challenger* [[3]](#cite_note-3) by [Fidelity Electronics](Fidelity_Electronics "Fidelity Electronics"). [Larry Atkin](Larry_Atkin "Larry Atkin") and [Peter W. Frey](Peter_W._Frey "Peter W. Frey") wrote the commercial program [Odin](Peter_W._Frey#Odin "Peter W. Frey") in the early 80s as well [[4]](#cite_note-4). Other programmers to mention are [Aart Bik](Aart_Bik "Aart Bik"), [Bruno Bras](Bruno_Bras "Bruno Bras"), [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [Joost Buijs](Joost_Buijs "Joost Buijs"), [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Steve Maughan](Steve_Maughan "Steve Maughan"), and [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill"). 



### Search


In Othello, similar to chess, [search](Search "Search") implementations are dominated by [alpha-beta](Alpha-Beta "Alpha-Beta") and variants so far. An alternative approach called MGSS and MGSS\* was proposed by [Stuart Russell](Stuart_Russell "Stuart Russell") and [Eric Wefald](Eric_Wefald "Eric Wefald") in 1988 [[5]](#cite_note-5) and 1989 [[6]](#cite_note-6) respectively. In Othello, there is no concept of [standing pat](Quiescence_Search#StandPat "Quiescence Search") or [quiescence](Quiescence_Search "Quiescence Search"), and [null move pruning](Null_Move_Pruning "Null Move Pruning") does not work.



* [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") elaborated on [NegaC\*](NegaC* "NegaC*") [[7]](#cite_note-7) and for [parallel search](Parallel_Search "Parallel Search") on [ABDADA](ABDADA "ABDADA") [[8]](#cite_note-8).
* [Michael Buro](Michael_Buro "Michael Buro") successfully implemented his [ProbCut](ProbCut "ProbCut") and [Multi-ProbCut](ProbCut#MPC "ProbCut") (MPC) as [selective](Selectivity "Selectivity") extension [[9]](#cite_note-9) inside his successful Othello program *Logistello* [[10]](#cite_note-10), already described in his Ph.D. thesis [[11]](#cite_note-11).
* The *Asycnhronous Parallel Hierarchical Iterative Deepening* algorithm, [APHID](APHID "APHID") by [Mark Brockington](Mark_Brockington "Mark Brockington") was applied to Othello as well [[12]](#cite_note-12) [[13]](#cite_note-13) [[14]](#cite_note-14) [[15]](#cite_note-15).
* In 2011, [Jean Méhat](Jean_M%C3%A9hat "Jean Méhat") and [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") implemented [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") in parallel [General Game Playing](General_Game_Playing "General Game Playing"), also covering Othello with promising results [[16]](#cite_note-16).


### Evaluation


Despite [material](Material "Material") as decisive feature in Othello, it is also a volatile one and difficult to [evaluate](Evaluation "Evaluation"). Othello programmers often use [piece-square tables](Piece-Square_Tables "Piece-Square Tables"), [mobility](Mobility "Mobility") and take [various other features](https://en.wikipedia.org/wiki/Computer_Othello#Evaluation_Techniques), [pattern](index.php?title=Pattern&action=edit&redlink=1 "Pattern (page does not exist)"), and heuristics into account, considering [strategic elements](https://en.wikipedia.org/wiki/Reversi#Strategic_elements) like the importance of the edge squares. [Paul Rosenbloom's](index.php?title=Paul_S._Rosenbloom&action=edit&redlink=1 "Paul S. Rosenbloom (page does not exist)") program [Iago](index.php?title=Paul_S._Rosenbloom&action=edit&redlink=1 "Paul S. Rosenbloom (page does not exist)") of the early 80s used edge stability, internal stability [[17]](#cite_note-17), current [mobility](Mobility "Mobility") and potential mobility, weighted by coefficients as suggested by [Hans Berliner](Hans_Berliner "Hans Berliner") [[18]](#cite_note-18) [[19]](#cite_note-19). In conjunction with [probability](https://en.wikipedia.org/wiki/Probability) based [pruning](Pruning "Pruning") aka [ProbCut](ProbCut "ProbCut"), [Michael Buro](Michael_Buro "Michael Buro") elaborately addresses the evaluation function [[20]](#cite_note-20) [[21]](#cite_note-21) [[22]](#cite_note-22). Further, [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), and [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") applied [Temporal Difference Learning](Temporal_Difference_Learning "Temporal Difference Learning") to an Othello evaluation function [[23]](#cite_note-23).



### Bitboards


Othello is very [bitboard](Bitboards "Bitboards") friendly. It seems that [Dumb7Fill](Dumb7Fill "Dumb7Fill") or [Kogge-Stone](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") [Fill Algorithms](Fill_Algorithms "Fill Algorithms") are suitable to [generate moves](Move_Generation "Move Generation"). Generator sets are the own pieces, propagator sets the opponent ones. The fill result, after a final [direction shift](General_Setwise_Operations#OneStepOnly "General Setwise Operations") similar as fill based [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") in chess, needs an [intersection](General_Setwise_Operations#Intersection "General Setwise Operations") with [empty squares](Occupancy "Occupancy") to determine the target squares per [direction](Direction "Direction"). Beside the target square coordinate, [move encoding](Encoding_Moves "Encoding Moves") may incorporate a direction set (one [Byte](Byte "Byte") with one distinct bit per direction) for all eight directions with anchor squares, and possibly the number of pieces to flip, may be even as set for more reliable [move ordering](Move_Ordering "Move Ordering") and faster [make move](Make_Move "Make Move"). An [MMX](MMX "MMX") implementation of Dumb7Fill in [inline assembly](Assembly#InlineAssembly "Assembly") by [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson") [[24]](#cite_note-24) demonstrates determining mobility, while the implementation by co-author [Toshihiko Okuhara](index.php?title=Toshihiko_Okuhara&action=edit&redlink=1 "Toshihiko Okuhara (page does not exist)") in their program Zebra [[25]](#cite_note-25) looks [parallel prefixed](Parallel_Prefix_Algorithms "Parallel Prefix Algorithms") [[26]](#cite_note-26).



## Solving Othello


Othello on 4×4 [[27]](#cite_note-27) and 6×6 board [[28]](#cite_note-28) are [strongly solved](https://en.wikipedia.org/wiki/Computer_Othello#Solving_Othello) and proved as a second player (white) to win. For 8x8 boards, [Victor Allis](Victor_Allis "Victor Allis") estimated the number of legal positions in Othello is at most 1028, and it has a game-tree complexity of approximately 1058 [[29]](#cite_note-29). While still mathematically unsolved, there is strong suspicion that perfect play on both sides results in a draw [[30]](#cite_note-30) [[31]](#cite_note-31).



## [Computer Olympiads](Computer_Olympiad "Computer Olympiad")


* [1st Computer Olympiad, London 1989](1st_Computer_Olympiad#Othello "1st Computer Olympiad")
* [2nd Computer Olympiad, London 1990](2nd_Computer_Olympiad#Othello "2nd Computer Olympiad")
* [3rd Computer Olympiad, Maastricht 1991](3rd_Computer_Olympiad#Othello "3rd Computer Olympiad")
* [4th Computer Olympiad, London 1992](4th_Computer_Olympiad#Othello "4th Computer Olympiad")
* [20th Computer Olympiad, Leiden 2017](20th_Computer_Olympiad#Othello "20th Computer Olympiad")


## Photos


 [](http://icga.org/?page_id=2137) 
[20th Computer Olympiad, Leiden 2017](20th_Computer_Olympiad#Othello "20th Computer Olympiad"), Othello 10x10 winners, [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (Mothello10, Bronze),  
[Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") with [WCCC 2005](WCCC_2005 "WCCC 2005") shirt (Decapus, Gold) and [Andrew Lin](index.php?title=Andrew_Lin&action=edit&redlink=1 "Andrew Lin (page does not exist)") (Deep Nikita, Silver) [[32]](#cite_note-32)



## Othello Programs


* [Bill](Sanjoy_Mahajan#Bill "Sanjoy Mahajan") by [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee") and [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan")


## See also


* [ABDADA](ABDADA "ABDADA")
* [APHID](APHID "APHID")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [ProbCut](ProbCut "ProbCut")
* [SANE](David_E._Moriarty#SANE "David E. Moriarty")


## Publications


### 1979


* [Peter B. Maggs](index.php?title=Peter_B._Maggs&action=edit&redlink=1 "Peter B. Maggs (page does not exist)") (**1979**). *[Programming Strategies in the Game of Reversi](https://archive.org/stream/byte-magazine-1979-11/1979_11_BYTE_04-11_Fun_and_Games#page/n67/mode/2up)*. [BYTE, Vol. 4, No. 11](Byte_Magazine#BYTE411 "Byte Magazine"), pp. 66-79


### 1980 ...


* [Ed Wright](index.php?title=Ed_Wright&action=edit&redlink=1 "Ed Wright (page does not exist)") (**1980**). *[Othello](http://www.atariarchives.org/bcc3/showpage.php?page=258)*. [The Best of Creative Computing Volume 3](Creative_Computing#Best3 "Creative Computing")
* Editor (**1980**). *Background and Origins of Othello*. [Personal Computing, Vol. 4, No. 7](Personal_Computing#4_7 "Personal Computing"), pp. 87
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1980**). *Machine Othello*. [Personal Computing, Vol. 4, No. 7](Personal_Computing#4_7 "Personal Computing"), pp. 89
* [Paul S. Rosenbloom](index.php?title=Paul_S._Rosenbloom&action=edit&redlink=1 "Paul S. Rosenbloom (page does not exist)") (**1981**). *A world-championship-level Othello program*. Technical report, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](https://pdfs.semanticscholar.org/4033/a5b1d46beec14600427e391ce600159c0f61.pdf)
* Alan S. Wolff, [Donald H. Mitchell](Donald_H._Mitchell "Donald H. Mitchell"), [Peter W. Frey](Peter_W._Frey "Peter W. Frey") (**1984**). *[Perceptual Skill in the Game of Othello](https://www.tandfonline.com/doi/abs/10.1080/00223980.1984.9712586)*. [The Journal of Psychology](https://en.wikipedia.org/wiki/The_Journal_of_Psychology), Vol. 118, No. 1
* [Donald H. Mitchell](Donald_H._Mitchell "Donald H. Mitchell") (**1984**). *Using Features to Evaluate Positions in Experts' and Novices' Othello Games*. Master thesis, Department of Psychology, [Northwestern University](Northwestern_University "Northwestern University"), Evanston, IL


### 1985 ...


* [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee"), [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan") (**1986**). *[BILL: a table-based, knowledge-intensive othello program](https://kilthub.cmu.edu/articles/BILL_a_table-based_knowledge-intensive_othello_program/6603887/1)*. Technial Report CMU-CS-86-141, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](https://pdfs.semanticscholar.org/f7ab/15736ecc79452aa4546cf8d7f5aa94d6afa0.pdf)
* [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee") (**1986**). *[A pattern classification approach to evaluation function learning](https://kilthub.cmu.edu/articles/A_pattern_classification_approach_to_evaluation_function_learning/6591158)*. Technial Report CMU-CS-86-173, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
* [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee"), [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan") (**1988**). *[A Pattern Classification Approach to Evaluation Function Learning](https://www.sciencedirect.com/science/article/abs/pii/0004370288900768)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 36, No. 1
* [Stuart Russell](Stuart_Russell "Stuart Russell"), [Eric Wefald](Eric_Wefald "Eric Wefald") (**1988**). *Decision-Theoretic Search Control: General Theory and an Application to Game-Playing.* Computer Science Division Technical Report 88/435, University of California, Berkeley, CA.
* [Kenneth A. De Jong](Mathematician#KADeJong "Mathematician"), [Alan C. Schultz](Mathematician#ACSchultz "Mathematician") (**1988**). *Using Experience-Based Learning in Game Playing*. Proceedings of the Fifth International Machine Learning Conference, [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.52.5381) » [Learning](Learning "Learning")
* [Stuart Russell](Stuart_Russell "Stuart Russell"), [Eric Wefald](Eric_Wefald "Eric Wefald") (**1989**). *[On optimal game-tree search using rational metareasoning](http://portal.acm.org/citation.cfm?id=1623807).* In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence, Detroit, MI: Morgan Kaufmann, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.79.9229&rep=rep1&type=pdf)
* [Clarence Hewlett](index.php?title=Clarence_Hewlett&action=edit&redlink=1 "Clarence Hewlett (page does not exist)") (**1989**). *Hardware Help on an Othello Endgame Analyzer*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")
* [Anders Kierulf](Anders_Kierulf "Anders Kierulf") (**1989**). *New Concepts in Computer Othello: Corner Value, Edge Advoidance, Access, and Parity*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")
* [Greg M. Gupton](index.php?title=Greg_M._Gupton&action=edit&redlink=1 "Greg M. Gupton (page does not exist)") (**1989**). *Genetic Learning Algorithm Applied to the Game of Othello*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")


### 1990 ...


* [Kai-Fu Lee](Kai-Fu_Lee "Kai-Fu Lee"), [Sanjoy Mahajan](Sanjoy_Mahajan "Sanjoy Mahajan") (**1990**). *[The Development of a World Class Othello Program](https://www.sciencedirect.com/science/article/abs/pii/000437029090068B)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
* [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1991**). *Experiments With the NegaC\* Search - An Alternative for Othello Endgame Search.* [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
* [Richard Korf](Richard_Korf "Richard Korf") and [Max Chickering](Max_Chickering "Max Chickering") (**1994**). *[Best-first minimax search: Othello results](http://www.aaai.org/Library/AAAI/1994/aaai94-210.php).* Proceedings of the 13th National Conference on Artificial Intelligence (AAAI-94), pp. 1365-1370. AAAI Press, Menlo Park, CA.
* [Victor Allis](Victor_Allis "Victor Allis") (**1994**). *Searching for Solutions in Games and Artificial Intelligence*. Ph.D. Thesis, [University of Limburg](Maastricht_University "Maastricht University"), [pdf](http://fragrieu.free.fr/SearchingForSolutions.pdf)
* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1994**). *[Evolving Neural Networks to focus Minimax Search](http://nn.cs.utexas.edu/?moriarty:aaai94)*. [AAAI-94](Conferences#AAAI-94 "Conferences")


### 1995 ...


* [David E. Moriarty](David_E._Moriarty "David E. Moriarty"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**1995**). *[Discovering Complex Othello Strategies Through Evolutionary Neural Networks](http://nn.cs.utexas.edu/?moriarty:connsci95)*. [Connection Science](https://www.scimagojr.com/journalsearch.php?q=24173&tip=sid), Vol. 7
* [Anton Leouski](index.php?title=Anton_Leouski&action=edit&redlink=1 "Anton Leouski (page does not exist)") (**1995**). *Learning of Position Evaluation in the Game of Othello*. Master's Project, [University of Massachusetts](https://en.wikipedia.org/wiki/University_of_Massachusetts), [Amherst, Massachusetts](https://en.wikipedia.org/wiki/Amherst,_Massachusetts), [pdf](http://people.ict.usc.edu/~leuski/publications/papers/UM-CS-1995-023.pdf)
* [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *[Statistical Feature Combination for the Evaluation of Game Positions](http://www.jair.org/papers/paper179.html)*. [JAIR](https://en.wikipedia.org/wiki/Journal_of_Artificial_Intelligence_Research), Vol. 3
* [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal"), pp. 71-76, [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/probcut.pdf)
* [Jean-Marc Alliot](Jean-Marc_Alliot "Jean-Marc Alliot"), [Nicolas Durand](Mathematician#NDurand "Mathematician") (**1995**). *[A Genetic Algorithm to Improve an Othello Program](https://hal-enac.archives-ouvertes.fr/hal-00937682)*. [Artificial Evolution](https://link.springer.com/book/10.1007/3-540-61108-8), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 1063, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [David Currie](index.php?title=David_Currie&action=edit&redlink=1 "David Currie (page does not exist)") (**1996**). *Othello Game Player*. [St. John's College](https://en.wikipedia.org/wiki/St_John%27s_College,_Oxford), [pdf](http://david.currie.name/wp-content/othello.pdf)
* [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *[The ABDADA Distributed Minimax Search Algorithm](http://portal.acm.org/citation.cfm?id=228345)*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal"), [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
* [Michael Buro](Michael_Buro "Michael Buro") (**1997**). *An Evaluation Function for Othello Based on Statistics.* NEC Research Institute. Technical Report #31.
* [Mark Brockington](Mark_Brockington "Mark Brockington") (**1997**). *KEYANO Unplugged - The Construction of an Othello Program*. Technical Report TR-97-05, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.49.2672)
* [Michael Buro](Michael_Buro "Michael Buro") (**1997**). *Experiments with Multi-ProbCut and a New High-quality Evaluation Function for Othello.* Technical Report No. 96, NEC Research Institute, Princeton, N.J. [pdf](http://skatgame.net/mburo/ps/improve.pdf)
* [Michael Buro](Michael_Buro "Michael Buro") (**1997**). *The Othello match of the year: Takeshi Murakami vs Logistello*. [ICCA Journal, Vol 20, No. 3](ICGA_Journal#20_3 "ICGA Journal"), [zipped ps](http://skatgame.net/mburo/ps/match-report.ps.gz)
* [Craig S. Bruce](Craig_S._Bruce "Craig S. Bruce") (**1998**). *[Performance Optimization for Distributed-Shared-Data Systems](http://uwspace.uwaterloo.ca/handle/10012/300)*. Ph.D. thesis, [University of Waterloo](University_of_Waterloo "University of Waterloo"), 6.6. Game-Tree Searching: Othello, pp. 188
* [Ayumu Nagai](Ayumu_Nagai "Ayumu Nagai"), [Hiroshi Imai](Hiroshi_Imai "Hiroshi Imai") (**1999**). *Application of df-pn+ to Othello endgames*. [5th Game Programming Workshop](Conferences#GPW "Conferences") » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")


### 2000 ...


* [Michael Buro](Michael_Buro "Michael Buro") (**2000**). *Experiments with Multi-ProbCut and a new High-Quality Evaluation Function for Othello.* Games in AI Research (eds. [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida")), pp. 77-96. [Universiteit Maastricht](Maastricht_University "Maastricht University"), Maastricht, The Netherlands. ISBN 90-621-6416-1.
* [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2001**). *The Performance of PN\*, PDS, and PN Search on 6x6 Othello and Tsume-Shogi*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9") » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
* [Michael Buro](Michael_Buro "Michael Buro") (**2002**). *Report on the IWEC-2002 Man-Machine Othello Match*. [ICGA Journal, Vol. 25, No. 2](ICGA_Journal#25_2 "ICGA Journal"), [pdf](https://skatgame.net/mburo/ps/iwec-match.pdf)
* [Konstantinos Tournavitis](index.php?title=Konstantinos_Tournavitis&action=edit&redlink=1 "Konstantinos Tournavitis (page does not exist)") (**2002**). *[MOUSE(μ): A Self-teaching Algorithm that Achieved Master-Strength at Othello](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_2)*. [CG 2002](CG_2002 "CG 2002")
* [Michael Buro](Michael_Buro "Michael Buro") (**2003**). *The Evolution of Strong Othello Programs*. [IFIP](IFIP "IFIP"), Vol. 112, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* C.K. Wong, K.K. Lo and P.H.W. Leong (**2004**). *[An FPGA-based Othello Endgame Solver](http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=1393254)*. [The Chinese University of Hong Kong](https://en.wikipedia.org/wiki/Chinese_University_of_Hong_Kong), [pdf](http://www.cse.cuhk.edu.hk/~phwl/mt/public/archives/papers/othello_fpt04.pdf)


### 2005 ...


* [Simon Lucas](Simon_Lucas "Simon Lucas"), [Thomas Philip Runarsson](Thomas_Philip_Runarsson "Thomas Philip Runarsson") (**2006**). *[Temporal Difference Learning versus Co-Evolution for Acquiring Othello Position Evaluation](http://scholar.google.is/citations?view_op=view_citation&hl=en&user=4eWdc_sAAAAJ&citation_for_view=4eWdc_sAAAAJ:qjMakFHDy7sC)*. [IEEE CIG 2006](IEEE#CIG "IEEE")
* [Simon Lucas](Simon_Lucas "Simon Lucas") (**2007**). *[Learning to play Othello with N-tuple systems](http://scholar.google.com/citations?view_op=view_citation&hl=de&user=Jz8DDVAAAAAJ&cstart=20&citation_for_view=Jz8DDVAAAAAJ:QIV2ME_5wuYC)*. [Australian Journal of Intelligent Information Processing Systems](https://www.chatbots.org/journal/australian_journal_of_intelligent_information_processing_systems/), Special Issue on Game Technology, Vol. 9, No. 4
* [Edward P. Manning](index.php?title=Edward_P._Manning&action=edit&redlink=1 "Edward P. Manning (page does not exist)") (**2007**). *[Temporal Difference Learning of an Othello Evaluation Function for a Small Neural Network with Shared Weights](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=4219046)*. [IEEE CIG 2007](IEEE#CIG "IEEE")
* [Thomas Philip Runarsson](Thomas_Philip_Runarsson "Thomas Philip Runarsson"), [Egill Orn Jonsson](https://dblp.uni-trier.de/pers/hd/j/Jonsson:Egill_Orn) (**2007**). *Effect of look-ahead search depth in learning position evaluation functions for Othello using -greedy exploration*. [IEEE CIG 2007](IEEE#CIG "IEEE")
* [Pim Nijssen](index.php?title=Pim_Nijssen&action=edit&redlink=1 "Pim Nijssen (page does not exist)") (**2007**). *Playing Othello Using Monte Carlo*. Bachelor's Thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](http://www.personeel.unimaas.nl/pim.nijssen/pub/bsc.pdf)
* [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2008**). *An Othello Evaluation Function Based on Temporal Difference Learning using Probability of Winning*. [CIG'08](http://www.csse.uwa.edu.au/cig08/Proceedings/toc.html), [pdf](http://www.csse.uwa.edu.au/cig08/Proceedings/papers/8010.pdf)
* [Toru Ueda](index.php?title=Toru_Ueda&action=edit&redlink=1 "Toru Ueda (page does not exist)"), [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2008**). *[Weak Proof-Number Search](http://www.springerlink.com/content/v47864x734410148/)*. [CG 2008](CG_2008 "CG 2008") » [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2009**). *Coevolutionary Temporal Difference Learning for Othello*. [IEEE Symposium on Computational Intelligence and Games](IEEE#CIG "IEEE"), [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/papers/szubert09coevolutionary.pdf)
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2009**). *Coevolutionary Reinforcement Learning and its Application to Othello*. M.Sc. thesis, [Poznań University of Technology](https://en.wikipedia.org/wiki/Pozna%C5%84_University_of_Technology), supervisor [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [pdf](https://mszubert.github.io/papers/Szubert_2009_MSC.pdf)


### 2010 ...


* [Edward P. Manning](index.php?title=Edward_P._Manning&action=edit&redlink=1 "Edward P. Manning (page does not exist)") (**2010**). *[Using Resource-Limited Nash Memory to Improve an Othello Evaluation Function](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=5409565)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 2, No. 1
* [Edward P. Manning](index.php?title=Edward_P._Manning&action=edit&redlink=1 "Edward P. Manning (page does not exist)") (**2010**). *[Coevolution in a Large Search Space using Resource-limited Nash Memory](http://dl.acm.org/citation.cfm?id=1830667)*. [GECCO '10](http://www.informatik.uni-trier.de/~ley/db/conf/gecco/gecco2010.html#Manning10)


**2011**



* [Jean Méhat](Jean_M%C3%A9hat "Jean Méhat"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2011**). *A Parallel General Game Player*. [KI Journal](http://www.kuenstliche-intelligenz.de/), Vol. 25, No. 1, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/rootparallelggp.pdf)
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2011**). *Learning Board Evaluation Function for Othello by Hybridizing Coevolution with Temporal Difference Learning*. [Control and Cybernetics](http://control.ibspan.waw.pl:3000/mainpage), Vol. 40, No. 3, [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/papers/szubert2011learning.pdf)
* [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2011**). *Learning N-Tuple Networks for Othello by Coevolutionary Gradient Search*. [GECCO 2011](http://www.informatik.uni-trier.de/~ley/db/conf/gecco/gecco2011.html#KrawiecS11), [pdf](http://www.cs.put.poznan.pl/mszubert/pub/krawiec2011gecco.pdf)
* [Damjan Strnad](index.php?title=Damjan_Strnad&action=edit&redlink=1 "Damjan Strnad (page does not exist)"), [Nikola Guid](index.php?title=Nikola_Guid&action=edit&redlink=1 "Nikola Guid (page does not exist)") (**2011**). *[Parallel Alpha-Beta Algorithm on the GPU](http://cit.fer.hr/index.php/CIT/article/view/2029)*. [CIT. Journal of Computing and Information Technology](http://cit.fer.hr/index.php/CIT), Vol. 19, No. 4 » [GPU](GPU "GPU"), [Parallel Search](Parallel_Search "Parallel Search")


**2012**



* [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski") (**2012**). *Co-Evolution versus Evolution with Random Sampling for Acquiring Othello Position Evaluation*. master's thesis, [Poznań University of Technology](https://en.wikipedia.org/wiki/Pozna%C5%84_University_of_Technology), supervisor [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/var/pliskowski_msc.pdf)
* [Sjoerd van den Dries](http://dblp.uni-trier.de/pers/hd/d/Dries:Sjoerd_van_den), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2012**). *[Neural-fitted TD-leaf learning for playing Othello with structured neural networks](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=xVas0I8AAAAJ&cstart=40&citation_for_view=xVas0I8AAAAJ:P5F9QuxV20EC)*. [IEEE Transactions on Neural Networks and Learning Systems](IEEE#NN "IEEE"), Vol. 23, No. 11


**2013**



* [Michiel van der Ree](http://dblp.uni-trier.de/pers/hd/r/Ree:M=_van_der), [Marco Wiering](Marco_Wiering "Marco Wiering") (**2013**). *[Reinforcement Learning in the Game of Othello: Learning Against a Fixed Opponent and Learning from Self-Play](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=xVas0I8AAAAJ&cstart=60&pagesize=80&citation_for_view=xVas0I8AAAAJ:K3LRdlH-MEoC)*. [ADPRL 2013](http://dblp.uni-trier.de/db/conf/adprl/adprl2013.html#ReeW13)
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2013**). *[On Scalability, Generalization, and Hybridization of Coevolutionary Learning: a Case Study for Othello](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6504736)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 5, No. 3
* [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2013**). *Shaping Fitness Function for Evolutionary Learning of Game Strategies*. [GECCO 2013](http://www.informatik.uni-trier.de/~ley/db/conf/gecco/gecco2013.html#SzubertJLK13), [pdf](http://www.cs.put.poznan.pl/wjaskowski/pub/papers/szubert2013shaping.pdf)
* [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski") (**2013**). *[Quantitative Analysis of the Hall of Fame Coevolutionary Archives](http://dl.acm.org/citation.cfm?id=2482752)*. [GECCO '13](http://www.sigevo.org/gecco-2013/) Companion Proceedings
* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2013**). *Improving Coevolution by Random Sampling*. [GECCO 2013](http://www.informatik.uni-trier.de/~ley/db/conf/gecco/gecco2013.html#JaskowskiLSK13), [pdf](http://www.cs.put.poznan.pl/mszubert/pub/jaskowski2013gecco.pdf)


**2014**



* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski") (**2014**). *Multi-Criteria Comparison of Coevolution and Temporal Difference Learning on Othello*. [EvoApplications 2014](http://www.evostar.org/2014/), [Springer, volume 8602](http://www.springer.com/computer/theoretical+computer+science/book/978-3-662-45522-7)
* [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Tsan-Cheng Su](index.php?title=Tsan-Cheng_Su&action=edit&redlink=1 "Tsan-Cheng Su (page does not exist)"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2014**). *Solving 6x6 Othello on Volunteer Computing System*. [GPW-2014](Conferences#GPW "Conferences")
* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski") (**2014**). *Systematic n-Tuple Networks for Othello Position Evaluation*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal")
* [Thomas Philip Runarsson](Thomas_Philip_Runarsson "Thomas Philip Runarsson"), [Simon Lucas](Simon_Lucas "Simon Lucas") (**2014**). *Preference Learning for Move Prediction and Evaluation Function Approximation in Othello*. [IEEE CIG 2014](IEEE#CIG "IEEE")


### 2015 ...


* [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [E. Mei Ang](index.php?title=E._Mei_Ang&action=edit&redlink=1 "E. Mei Ang (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Identifying Critical Positions Based on Conspiracy Numbers](http://link.springer.com/chapter/10.1007%2F978-3-319-27947-3_6)*. [Agents and Artificial Intelligence](http://link.springer.com/book/10.1007/978-3-319-27947-3), [ICAART 2015 - Revised Selected Papers](http://dblp.uni-trier.de/db/conf/icaart/icaart2015s.html#KhalidAYII15)
* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert") (**2016**). *[Coevolutionary CMA-ES for Knowledge-Free Learning of Game Position Evaluation](https://ieeexplore.ieee.org/document/7180338)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 8, No. 4
* [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Marcin Szubert](Marcin_Szubert "Marcin Szubert"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2016**). *[The performance profile: A multi–criteria performance evaluation method for test–based problems](https://content.sciendo.com/view/journals/amcs/26/1/article-p215.xml)*. [International Journal of Applied Mathematics and Computer Science](https://en.wikipedia.org/wiki/International_Journal_of_Applied_Mathematics_and_Computer_Science), Vol. 26, No. 1
* [Shantanu Thakoor](index.php?title=Shantanu_Thakoor&action=edit&redlink=1 "Shantanu Thakoor (page does not exist)"), [Surag Nair](index.php?title=Surag_Nair&action=edit&redlink=1 "Surag Nair (page does not exist)"), [Megha Jhunjhunwala](index.php?title=Megha_Jhunjhunwala&action=edit&redlink=1 "Megha Jhunjhunwala (page does not exist)") (**2017**). *Learning to Play Othello Without Human Knowledge*. [Stanford University](Stanford_University "Stanford University"), [pdf](https://github.com/suragnair/alpha-zero-general/blob/master/pretrained_models/writeup.pdf) » [AlphaZero](AlphaZero "AlphaZero"), [MCTS](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [Deep Learning](Deep_Learning "Deep Learning") [[33]](#cite_note-33)
* [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2017**). *Learning to Play Othello with Deep Neural Networks*. [arXiv:1711.06583](https://arxiv.org/abs/1711.06583) [[34]](#cite_note-34)
* [Paweł Liskowski](Pawe%C5%82_Liskowski "Paweł Liskowski"), [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski"), [Krzysztof Krawiec](Krzysztof_Krawiec "Krzysztof Krawiec") (**2018**). *Learning to Play Othello with Deep Neural Networks*. [IEEE Transactions on Games](IEEE#TOG "IEEE")
* [Kiminori Matsuzaki](index.php?title=Kiminori_Matsuzaki&action=edit&redlink=1 "Kiminori Matsuzaki (page does not exist)") (**2018**). *Empirical Analysis of PUCT Algorithm with Evaluation Functions of Different Quality*. [TAAI 2018](TAAI_2018 "TAAI 2018") » [PUCT](Christopher_D._Rosin#PUCT "Christopher D. Rosin")
* [Kiminori Matsuzaki](index.php?title=Kiminori_Matsuzaki&action=edit&redlink=1 "Kiminori Matsuzaki (page does not exist)"), [Naoki Kitamura](index.php?title=Naoki_Kitamura&action=edit&redlink=1 "Naoki Kitamura (page does not exist)") (**2018**). *Do evaluation functions really improve Monte-Carlo tree search?* [CG 2018](CG_2018 "CG 2018"), [ICGA Journal, Vol. 40, No. 3](ICGA_Journal#40_3 "ICGA Journal")
* [Nai-Yuan Chang](index.php?title=Nai-Yuan_Chang&action=edit&redlink=1 "Nai-Yuan Chang (page does not exist)"), [Chih-Hung Chen](Chih-Hung_Chen "Chih-Hung Chen"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin"), [Surag Nair](index.php?title=Surag_Nair&action=edit&redlink=1 "Surag Nair (page does not exist)") (**2018**). *[The Big Win Strategy on Multi-Value Network: An Improvement over AlphaZero Approach for 6x6 Othello](https://dl.acm.org/citation.cfm?id=3278325)*. [MLMI2018](https://dl.acm.org/citation.cfm?id=3278312)
* [Ching-Nung Lin](index.php?title=Ching-Nung_Lin&action=edit&redlink=1 "Ching-Nung Lin (page does not exist)"), [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2019**). *Decapus wins Othello 10 × 10 tournament*. [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal") » [21st Computer Olympiad 2018](index.php?title=21st_Computer_Olympiad&action=edit&redlink=1 "21st Computer Olympiad (page does not exist)")


## Forum Posts


* [Bitboards: speeding up FirstOne](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/bcb03df7630d6274) by Laurent Desnogues, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 10, 1996 » [BitScan](BitScan "BitScan")
* [Othello Match & Call for Papers](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/929a1b0a271d7080) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 24, 1997
* [Enhanced Transposition Table Cutoffs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8ab4f917234eb016) by [Andrea Zinno](index.php?title=Andrea_Zinno&action=edit&redlink=1 "Andrea Zinno (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 30, 1997 » [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
* [Othello man machine match](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/79d0882097714876) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 6, 1997
* [Othello endgame search question](http://groups.google.com/group/comp.ai.games/browse_frm/thread/a38f4f81e0a8839d) by Daniel Lidström, [comp.ai.games](http://groups.google.com/group/comp.ai.games/topics), December 13, 2001
* [stability in a Othello game](https://groups.google.com/d/msg/comp.ai.games/WZeBxfkzfYY/VaCfy1ds2ZYJ) by Daniel, [comp.ai.games](index.php?title=Compuer_Chess_Forums&action=edit&redlink=1 "Compuer Chess Forums (page does not exist)"), October 10, 2002
* [Performance: linux vs Windows vs Mac OS X](http://www.talkchess.com/forum/viewtopic.php?t=30723) by [Richard Delorme](Richard_Delorme "Richard Delorme"), [CCC](CCC "CCC"), November 21, 2009 » [Edax](https://en.wikipedia.org/wiki/Edax_(computing))
* [WinBoard, exotic version](http://www.talkchess.com/forum/viewtopic.php?start=0&t=37634) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 15, 2011 » [WinBoard](WinBoard "WinBoard")


## External Links


* [Reversi from Wikipedia](https://en.wikipedia.org/wiki/Reversi)
* [Computer Othello from Wikipedia](https://en.wikipedia.org/wiki/Computer_Othello)
* [The Othello Wiki Book Project](http://www.othello.dk/book/index.php/Home)
* [The Othello Engine Protocol](http://cassio.free.fr/engine-protocol.htm) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet")
* [Othello (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/game.php?id=22)
* [The strong learning Othello Programs](http://satirist.org/learn-game/systems/othello/) from [Machine Learning in Games](http://satirist.org/learn-game/) by [Jay Scott](Jay_Scott "Jay Scott")
* [Othello Players](http://www.cs.put.poznan.pl/wjaskowski/othello-league-players) by [Wojciech Jaśkowski](Wojciech_Ja%C5%9Bkowski "Wojciech Jaśkowski")
* [Writing an Othello program](http://radagast.se/othello/howto.html) by [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson")
* [Perft for Reversi/Othello](http://www.aartbik.com/MISC/reversi.html) by [Aart Bik](Aart_Bik "Aart Bik") » [Perft](Perft "Perft") [[35]](#cite_note-35)
* [Andrea Zinno's Home Page](http://www.andreazinno.it/) - Entirely dedicated to the Othello game, by [Andrea Zinno](index.php?title=Andrea_Zinno&action=edit&redlink=1 "Andrea Zinno (page does not exist)")
* [Othello (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Othello_%28disambiguation%29)


## References


1. [↑](#cite_ref-1) [Reversi from Wikipedia](https://en.wikipedia.org/wiki/Reversi)
2. [↑](#cite_ref-2) [Writing an Othello program](http://radagast.se/othello/howto.html) by [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson")
3. [↑](#cite_ref-3) [The Othello Museum - Reversi Sensory Challenger](http://www.beppi.it/public/OthelloMuseum/pages/boards-museum/electronic-boards/reversi-sensory-challenger.php)
4. [↑](#cite_ref-4) [Odin - The Othello Wiki Book Project](http://www.othello.dk/book/index.php/Odin)
5. [↑](#cite_ref-5) [Stuart Russell](Stuart_Russell "Stuart Russell"), [Eric Wefald](Eric_Wefald "Eric Wefald") (**1988**). *Decision-Theoretic Search Control: General Theory and an Application to Game-Playing.* Computer Science Division Technical Report 88/435, University of California, Berkeley, CA.
6. [↑](#cite_ref-6) [Stuart Russell](Stuart_Russell "Stuart Russell"), [Eric Wefald](Eric_Wefald "Eric Wefald") (**1989**). *[On optimal game-tree search using rational metareasoning](http://portal.acm.org/citation.cfm?id=1623807).* In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence, Detroit, MI: Morgan Kaufmann, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.79.9229&rep=rep1&type=pdf)
7. [↑](#cite_ref-7) [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1991**). *Experiments With the NegaC\* Search - An Alternative for Othello Endgame Search.* Heuristic Programming in Artificial Intelligence 2: the second computer olympiad (eds. [David Levy](David_Levy "David Levy") and [Don Beal](Don_Beal "Don Beal")), pp. 174-188. Ellis Horwood, Chichester. ISBN 0-13-382615-5, [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/negac.ps.gz) and [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.39.3189&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.39.3189)
8. [↑](#cite_ref-8) [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1996**). *[The ABDADA Distributed Minimax Search Algorithm](http://portal.acm.org/citation.cfm?id=228345)*. Proceedings of the 1996 ACM Computer Science Conference, pp. 131-138. ACM, New York, N.Y, reprinted [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal"), [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/acm.ps.gz)
9. [↑](#cite_ref-9) [Michael Buro](Michael_Buro "Michael Buro") (**1995**). *ProbCut: An Effective Selective Extension of the Alpha-Beta Algorithm.* [ICCA Journal, Vol. 18, No. 2](ICGA_Journal#18_2 "ICGA Journal"), pp. 71-76, [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/probcut.pdf)
10. [↑](#cite_ref-10) [Logistello's Homepage](http://www.cs.ualberta.ca/%7Emburo/log.html)
11. [↑](#cite_ref-11) [Michael Buro](Michael_Buro "Michael Buro") (**1994**). *Techniken für die Bewertung von Spielsituationen anhand von Beispielen.* Ph.D. Thesis. [Paderborn University](Paderborn_University "Paderborn University"), Paderborn, Germany. [pdf](http://www.cs.ualberta.ca/%7Emburo/ps/mics_dis.pdf) (German)
12. [↑](#cite_ref-12) [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1996**). *The APHID Parallel αβ Search Algorithm*. Technical Report 96-07, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), Edmonton, Alberta, Canada. as [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.8215&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.23.8215)
13. [↑](#cite_ref-13) [Mark Brockington](Mark_Brockington "Mark Brockington"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1997**). *APHID Game-Tree Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
14. [↑](#cite_ref-14) [APHID Parallel Game-Tree Search Library](http://webdocs.cs.ualberta.ca/~games/aphid/index.html)
15. [↑](#cite_ref-15) [Mark Brockington](Mark_Brockington "Mark Brockington") (**1998**). *Asynchronous Parallel Game-Tree Search*. Ph.D. Thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [zipped postscript](http://games.cs.ualberta.ca/articles/mgb_thesis.ps.gz)
16. [↑](#cite_ref-16) [Jean Méhat](Jean_M%C3%A9hat "Jean Méhat"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2011**). *A Parallel General Game Player*. [KI Journal](http://www.kuenstliche-intelligenz.de/), Vol. 25, No. 1, [pdf](http://www.lamsade.dauphine.fr/~cazenave/papers/rootparallelggp.pdf)
17. [↑](#cite_ref-17) [stability in a Othello game](https://groups.google.com/d/msg/comp.ai.games/WZeBxfkzfYY/VaCfy1ds2ZYJ) by Daniel, [comp.ai.games](index.php?title=Compuer_Chess_Forums&action=edit&redlink=1 "Compuer Chess Forums (page does not exist)"), October 10, 2002
18. [↑](#cite_ref-18) [Hans Berliner](Hans_Berliner "Hans Berliner") (**1980**). *[Backgammon Computer Program Beats World Champion](http://www.bkgm.com/articles/Berliner/BackgammonProgramBeatsWorldChamp/)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 14, hosted by [Backgammon Galore](http://www.bkgm.com/), reprinted in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Games I](http://link.springer.com/book/10.1007/978-1-4613-8716-9)*
19. [↑](#cite_ref-19)  [Paul S. Rosenbloom](index.php?title=Paul_S._Rosenbloom&action=edit&redlink=1 "Paul S. Rosenbloom (page does not exist)") (**1981**). *A world-championship-level Othello program*. Technical report, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](https://pdfs.semanticscholar.org/4033/a5b1d46beec14600427e391ce600159c0f61.pdf)
20. [↑](#cite_ref-20) [Michael Buro](Michael_Buro "Michael Buro") (**1997**). *An Evaluation Function for Othello Based on Statistics.* NEC Research Institute. Technical Report #31.
21. [↑](#cite_ref-21) [Michael Buro](Michael_Buro "Michael Buro") (**1997**). *Experiments with Multi-ProbCut and a New High-quality Evaluation Function for Othello.* Technical Report No. 96, NEC Research Institute, Princeton, N.J. [pdf](http://skatgame.net/mburo/ps/improve.pdf)
22. [↑](#cite_ref-22) [Michael Buro](Michael_Buro "Michael Buro") (**2000**). *Experiments with Multi-ProbCut and a new High-Quality Evaluation Function for Othello.* Games in AI Research (eds. [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida")), pp. 77-96. [Universiteit Maastricht](Maastricht_University "Maastricht University"), Maastricht, The Netherlands. ISBN 90-621-6416-1.
23. [↑](#cite_ref-23) [Yasuhiro Osaki](Yasuhiro_Osaki "Yasuhiro Osaki"), [Kazutomo Shibahara](Kazutomo_Shibahara "Kazutomo Shibahara"), [Yasuhiro Tajima](Yasuhiro_Tajima "Yasuhiro Tajima"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani") (**2008**). *An Othello Evaluation Function Based on Temporal Difference Learning using Probability of Winning*. [CIG'08](http://www.csse.uwa.edu.au/cig08/Proceedings/toc.html), [pdf](http://www.csse.uwa.edu.au/cig08/Proceedings/papers/8010.pdf)
24. [↑](#cite_ref-24) [bitboard mobility](http://radagast.se/othello/bitmob.c) Copyright (c) 2003, [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson")
25. [↑](#cite_ref-25) [Zebra](http://radagast.se/othello/zebra.html) by [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson")
26. [↑](#cite_ref-26) bitbmob.c in [zebra.tar.gz](http://radagast.se/othello/zebra.tar.gz)
27. [↑](#cite_ref-27) [AI Lab - Othello 4x4](http://ailab.awardspace.com/othello4x4.html)
28. [↑](#cite_ref-28) [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen"), [Tsan-Cheng Su](index.php?title=Tsan-Cheng_Su&action=edit&redlink=1 "Tsan-Cheng Su (page does not exist)"), [Jr-Chang Chen](Jr-Chang_Chen "Jr-Chang Chen"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2014**). *Solving 6x6 Othello on Volunteer Computing System*. [GPW-2014](Conferences#GPW "Conferences")
29. [↑](#cite_ref-29) [Victor Allis](Victor_Allis "Victor Allis") (**1994**). *Searching for Solutions in Games and Artificial Intelligence*. Ph.D. Thesis, [University of Limburg](Maastricht_University "Maastricht University"), [pdf](http://fragrieu.free.fr/SearchingForSolutions.pdf)
30. [↑](#cite_ref-30) [Computer opponents and research from Wikipedia](https://en.wikipedia.org/wiki/Reversi#Computer_opponents_and_research)
31. [↑](#cite_ref-31) [2004 Opening Book Skeleton](http://abulmo.perso.neuf.fr/games/book-2008.htm)
32. [↑](#cite_ref-32) [Events 2017: Dinner - Photo 24 of 25](http://icga.org/?page_id=2137) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos")
33. [↑](#cite_ref-33) [GitHub - suragnair/alpha-zero-general: A clean and simple implementation of a self-play learning algorithm based on AlphaGo Zero (any game, any framework!)](https://github.com/suragnair/alpha-zero-general)
34. [↑](#cite_ref-34) [Edax](https://en.wikipedia.org/wiki/Edax_(computing)) by [Richard Delorme](Richard_Delorme "Richard Delorme")
35. [↑](#cite_ref-35) [Aart Bik - The Othello Wiki Book Project](http://www.othello.dk/book/index.php/Aart_Bik)

**[Up one Level](Games "Games")**







 
