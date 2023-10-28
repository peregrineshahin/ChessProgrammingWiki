---
title: Search
---
**[Home](Home "Home") \* Search**



 [](http://schachbilderwelten.tenners.de/html/auf_der_suche.html) [Bernd Besser](Category:Bernd_Besser "Category:Bernd Besser"), Auf der Suche [[1]](#cite_note-1) 
Because finding or guessing a [good move](Best_Move "Best Move") in a [chess position](Chess_Position "Chess Position") is hard to achieve statically, [chess programs](Engines "Engines") rely on some type of **Search** in order to play reasonably. Searching involves looking ahead at different [move](Moves "Moves") sequences and evaluating the positions after [making the moves](Make_Move "Make Move"). Formally, searching a two-player [zero-sum](https://en.wikipedia.org/wiki/Zero-sum_%28game_theory%29) board game with [perfect information](https://en.wikipedia.org/wiki/Perfect_information) implies [traversing](https://en.wikipedia.org/wiki/Tree_traversal) and min-maxing a [tree-like data-structure](https://en.wikipedia.org/wiki/Tree_%28data_structure%29) by various [search algorithms](https://en.wikipedia.org/wiki/Search_algorithm). 



### Contents


* [1 Shannon's Types](#Shannon.27s_Types)
* [2 The Search Tree](#The_Search_Tree)
* [3 Search Algorithms](#Search_Algorithms)
	+ [3.1 Depth-First Search](#Depth-First_Search)
	+ [3.2 Alpha-Beta Enhancements](#Alpha-Beta_Enhancements)
		- [3.2.1 Obligatory](#Obligatory)
		- [3.2.2 Selectivity](#Selectivity)
		- [3.2.3 Scout and Friends](#Scout_and_Friends)
		- [3.2.4 Alpha-Beta goes Best-First](#Alpha-Beta_goes_Best-First)
	+ [3.3 Best-First Search](#Best-First_Search)
* [4 Opponent Model](#Opponent_Model)
* [5 Parallel Search](#Parallel_Search)
* [6 Using Time](#Using_Time)
* [7 Related Issues](#Related_Issues)
* [8 See also](#See_also)
* [9 Publications](#Publications)
	+ [9.1 1960 ...](#1960_...)
	+ [9.2 1970 ...](#1970_...)
	+ [9.3 1980 ...](#1980_...)
	+ [9.4 1990 ...](#1990_...)
	+ [9.5 2000 ...](#2000_...)
	+ [9.6 2010 ...](#2010_...)
	+ [9.7 2015 ...](#2015_...)
	+ [9.8 2020 ...](#2020_...)
* [10 Forum Posts](#Forum_Posts)
	+ [10.1 1999](#1999)
	+ [10.2 2000 ...](#2000_..._2)
	+ [10.3 2005 ...](#2005_...)
	+ [10.4 2010 ...](#2010_..._2)
	+ [10.5 2015 ...](#2015_..._2)
	+ [10.6 2020 ...](#2020_..._2)
* [11 External Links](#External_Links)
* [12 References](#References)






[Claude Shannon](Claude_Shannon "Claude Shannon") categorized searches into two types [[2]](#cite_note-2) :



* [Type A](Type_A_Strategy "Type A Strategy") - a [brute-force search](Brute-Force "Brute-Force") looking at every variation to a given [depth](Depth "Depth")
* [Type B](Type_B_Strategy "Type B Strategy") - a [selective search](Selectivity "Selectivity") looking at "important" branches only


Inspired by the experiments of [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") [[3]](#cite_note-3) , Shannon and early programmers favored Type B strategy. Type B searches use some type of static heuristics in order to only look at branches that look important - with some risk to oversee some serious tactics not covered by the plausible move selector. Type B was most popular until the 1970's, when Type A programs had enough processing power and more efficient brute force algorithms to become stronger. Today most programs are closer to Type A, but have some characteristics of a Type B as mentioned in [selectivity](Selectivity "Selectivity").



## The Search Tree


The [search tree](Search_Tree "Search Tree") as subset of the [search space](Search_Space "Search Space") is a [directed graph](https://en.wikipedia.org/wiki/Graph_%28mathematics%29#Directed_graph) of [nodes](Node "Node"), the alternating white and black to move [chess positions](Chess_Position "Chess Position") - and edges connecting two nodes, representing the [moves](Moves "Moves") of either side. The [root](Root "Root") of the search-tree is the position we like to evaluate to find the [best move](Best_Move "Best Move"). Because of [transpositions](Transposition "Transposition") due to different move sequences, nodes inside the tree may occur from various ancestors - even within a different number of moves. The search tree contains various cycles, since both sides may [repeat](Repetitions "Repetitions") a former position with the minimum of two reversible moves each, or four [plies](Ply "Ply"). Cycles are usually eliminated and not searched twice, which results in searching a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) [DAG](index.php?title=DAG&action=edit&redlink=1 "DAG (page does not exist)").



* [Search Space](Search_Space "Search Space")
* [Search Tree](Search_Tree "Search Tree")
* [Root](Root "Root")
* [Node](Node "Node")
* [Conspiracy Numbers](Conspiracy_Numbers "Conspiracy Numbers")
* [Move List](Move_List "Move List")
* [Principal Variation](Principal_Variation "Principal Variation")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Repetitions](Repetitions "Repetitions")
* [Transposition](Transposition "Transposition")
* [Score](Score "Score")


## Search Algorithms


Most chess-programs use a variation of the [alpha-beta](Alpha-Beta "Alpha-Beta") algorithm to search the tree in a [depth-first](Depth-First "Depth-First") manner to attain an order of magnitude performance improvement over a pure [minimax](Minimax "Minimax") algorithm. Although [move ordering](Move_Ordering "Move Ordering") doesnt affect the performance of a pure mini-max search (as all branches and nodes are searched) — it becomes crucial for the performance of alpha beta search and enhancements such as [PVS](Principal_Variation_Search "Principal Variation Search"), [NegaScout](NegaScout "NegaScout") and [MTD(f)](MTD(f) "MTD(f)"). [Hans Berliner's](Hans_Berliner "Hans Berliner") chess-program [HiTech](HiTech "HiTech") and [Ulf Lorenz's](Ulf_Lorenz "Ulf Lorenz") program [P.ConNerS](P.ConNerS "P.ConNerS") used [best-first](Best-First "Best-First") approaches quite successfully.



### Depth-First Search


[Depth-First](Depth-First "Depth-First") search starts at the root and explores as far as possible along each branch before backtracking. Memory requirements are moderate, since only one path from the root to one leaf is kept in memory. The giga bytes of [RAM](Memory#RAM "Memory") in recent computers is utilized by a [transposition table](Transposition_Table "Transposition Table"). Minimax and Negamax are mentioned for educational reasons as the prototypes for the more advanced algorithms. They otherwise have no practical relevance in software, except traversing a minimax tree inside a [perft](Perft "Perft") framework for [testing](Engine_Testing "Engine Testing") the [move generator](Move_Generation "Move Generation"). Depth-first algorithms are generally embedded inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework for [time control](Time_Management "Time Management") and [move ordering](Move_Ordering "Move Ordering") issues.



* [Minimax](Minimax "Minimax")
* [Negamax](Negamax "Negamax")
* [Alpha-Beta](Alpha-Beta "Alpha-Beta")


### Alpha-Beta Enhancements


### Obligatory


* [Transposition Table](Transposition_Table "Transposition Table")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")


### Selectivity


* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Selectivity](Selectivity "Selectivity")
* [Mate Search](Mate_Search "Mate Search")


### Scout and Friends


* [Scout](Scout "Scout")
* [NegaScout](NegaScout "NegaScout")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")


### Alpha-Beta goes Best-First


* [NegaC\*](NegaC* "NegaC*")
* [MTD(f)](MTD(f) "MTD(f)")
* [Alpha-Beta Conspiracy Search](index.php?title=Alpha-Beta_Conspiracy_Search&action=edit&redlink=1 "Alpha-Beta Conspiracy Search (page does not exist)")


### Best-First Search


[Best-First](Best-First "Best-First") approaches build a search-tree by visiting the most promising nodes first.
They usually have huge memory requirements, since they keep an exponentially growing search space in memory.



* [B\*](B* "B*") as used by [Hans Berliner's](Hans_Berliner "Hans Berliner") chess-program [HiTech](HiTech "HiTech")
* [Best-First Minimax Search](Best-First_Minimax_Search "Best-First Minimax Search")
* [Conspiracy Number Search](Conspiracy_Number_Search "Conspiracy Number Search")
* [MCαβ](MC%CE%B1%CE%B2 "MCαβ")
* [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
* [SSS\* and Dual\*](SSS*_and_Dual* "SSS* and Dual*")
* [UCT](UCT "UCT")


## Opponent Model


* [Opponent Model Search](Opponent_Model_Search "Opponent Model Search")


## Parallel Search


* [Parallel Search](Parallel_Search "Parallel Search")
* [Parallel Controlled Conspiracy Number Search](Conspiracy_Number_Search#PCCNS "Conspiracy Number Search") as used by [Ulf Lorenz's](Ulf_Lorenz "Ulf Lorenz") program [P.ConNerS](P.ConNerS "P.ConNerS")


## Using Time


* [Pondering](Pondering "Pondering")
* [Time Management](Time_Management "Time Management")


## Related Issues


* [Depth](Depth "Depth")
* [Horizon Effect](Horizon_Effect "Horizon Effect")
* [Iterative Search](Iterative_Search "Iterative Search")
* [Move Ordering](Move_Ordering "Move Ordering")
* [Search Explosion](Search_Explosion "Search Explosion")
* [Search Instability](Search_Instability "Search Instability")
* [Search Pathology](Search_Pathology "Search Pathology")
* [Search Statistics](Search_Statistics "Search Statistics")
* [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Theorem-Proving and M & N procedure](James_R._Slagle#TheoremProving "James R. Slagle")


## See also


* [Backtracking](Backtracking "Backtracking")
* [History of Computer Chess](History "History")
* [Knowledge](Knowledge "Knowledge")


 [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
## Publications


### 1960 ...


* [Daniel Edwards](Daniel_Edwards "Daniel Edwards"), [Timothy Hart](Timothy_Hart "Timothy Hart") (**1961**). *The Alpha-Beta Heuristic*, AIM-030, reprint available from [DSpace](http://dspace.mit.edu/handle/1721.1/6098) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
* [Alexander Brudno](Alexander_Brudno "Alexander Brudno") (**1963**). *Bounds and valuations for shortening the search of estimates*. Problemy Kibernetiki (10) 141–150 and Problems of Cybernetics (10) 225–241
* [James R. Slagle](James_R._Slagle "James R. Slagle") (**1963**). *Game Trees, M & N Minimaxing, and the M & N alpha-beta procedure.* Artificial Intelligence Group Report 3, UCRL-4671, University of California
* [Jim Doran](Jim_Doran "Jim Doran"), [Donald Michie](Donald_Michie "Donald Michie") (**1966**). *[Experiments with the Graph Traverser Program](https://royalsocietypublishing.org/doi/10.1098/rspa.1966.0205)*. [Proceedings of the Royal Society](https://en.wikipedia.org/wiki/Proceedings_of_the_Royal_Society), Series A, Vol. 294, No. 1437, [pdf](https://stacks.stanford.edu/file/druid:yf330xx7624/yf330xx7624.pdf)
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [Philip Bursky](Philip_Bursky "Philip Bursky") (**1968**). *[Experiments With a Multipurpose, Theorem-Proving Heuristic Program](http://portal.acm.org/citation.cfm?id=321444)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 15, No. 1
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [John K. Dixon](John_K._Dixon "John K. Dixon") (**1969**). *[Experiments With Some Programs That Search Game Trees](http://portal.acm.org/citation.cfm?id=321510.321511)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 16, No. 2, [pdf](http://wiki.cs.pdx.edu/cs542-spring2011/nfp/abmin.pdf), [pdf](http://wiki.cs.pdx.edu/wurzburg2009/nfp/abmin.pdf)


### 1970 ...


* [James R. Slagle](James_R._Slagle "James R. Slagle"), [John K. Dixon](John_K._Dixon "John K. Dixon") (**1970**). *[Experiments with the M & N Tree-Searching Program](http://portal.acm.org/citation.cfm?id=362052.362054)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 13, No. 3, pp. 147-154.
* [James R. Slagle](James_R._Slagle "James R. Slagle"), [Richard C. T. Lee](Richard_C._T._Lee "Richard C. T. Lee") (**1971**). *[Application of game tree searching techniques to sequential pattern recognition](http://portal.acm.org/citation.cfm?id=362515.362562)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 14, No. 2
* [Larry Harris](Larry_Harris "Larry Harris") (**1973**). *The bandwidth heuristic search*. [3. IJCAI 1973](http://dblp.uni-trier.de/db/conf/ijcai/ijcai73.html), [pdf](http://www.ijcai.org/Past%20Proceedings/IJCAI-73/PDF/004.pdf)
* [Gerhard Wolf](Gerhard_Wolf "Gerhard Wolf") (**1973**). *[Implementation of a dynamic tree searching algorithm in a chess programme](http://dl.acm.org/citation.cfm?id=805704)*. [Proceedings of the ACM annual conference](http://dl.acm.org/citation.cfm?id=800192&picked=prox)
* [Larry Harris](Larry_Harris "Larry Harris") (**1974**). *Heuristic Search under Conditions of Error*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 5, No. 3, also published (**1977**) under the title: *The heuristic search: An alternative to the alpha-beta minimax procedure.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") (ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey"))
* [Larry Harris](Larry_Harris "Larry Harris") (**1975**) *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [IJCAI 1975](http://dblp.uni-trier.de/db/conf/ijcai/ijcai75.html), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1978**). *[Depth-m search in branch-and-bound algorithms](https://link.springer.com/article/10.1007/BF00991818)*. [International Journal of Parallel Programming](https://link.springer.com/journal/10766), Vol. 7, No. 4
* [Georgy Adelson-Velsky](Georgy_Adelson-Velsky "Georgy Adelson-Velsky"), [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Mikhail Donskoy](Mikhail_Donskoy "Mikhail Donskoy") (**1979**). *Algorithms of adaptive search*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html) (eds. [Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") and L.I. Mikulich), Ellis Horwood, Chichester.
* [George Stockman](George_Stockman "George Stockman") (**1979**). *A Minimax Algorithm Better than Alpha-Beta?* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 12, No. 2
* [John Gaschnig](John_Gaschnig "John Gaschnig") (**1979**). *[Performance Measurement and Analysis of Certain Search Algorithms](https://dl.acm.org/citation.cfm?id=909244)*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](http://reports-archive.adm.cs.cmu.edu/anon/scan/CMU-CS-79-124.pdf)


### 1980 ...


* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1981**). *Heuristic search theory: A survey of recent results*. [IJCAI-81](http://www.informatik.uni-trier.de/%7Eley/db/conf/ijcai/ijcai81.html), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-81-VOL%201/PDF/100.pdf)
* [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *[The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality](http://portal.acm.org/citation.cfm?id=358616&dl=ACM&coll=DL&CFID=27355608&CFTOKEN=40935826)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8
* [Murray Campbell](Murray_Campbell "Murray Campbell"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1983**). *A Comparison of Minimax Tree Search Algorithms*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 20, No. 4, [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/TR82-3.pdf)
* [Andrew L. Reibman](index.php?title=Andrew_L._Reibman&action=edit&redlink=1 "Andrew L. Reibman (page does not exist)"), [Bruce W. Ballard](index.php?title=Bruce_W._Ballard&action=edit&redlink=1 "Bruce W. Ballard (page does not exist)") (**1983**). *[Non-Minimax Search Strategies for Use against Fallible Opponents](http://www.aaai.org/Library/AAAI/1983/aaai83-084.php)*. Proceedings of [AAAI](AAAI "AAAI") 83
* [Nanda Srimani](index.php?title=Nanda_Srimani&action=edit&redlink=1 "Nanda Srimani (page does not exist)") (**1985**). *A New Algorithm (PS\*) for Searching Game Trees*. Master's thesis, [University of Alberta](University_of_Alberta "University of Alberta")
* [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki") (**1986**). *Generalization of Alpha-Beta and SSS\* Search Procedures.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 29
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Nanda Srimani](index.php?title=Nanda_Srimani&action=edit&redlink=1 "Nanda Srimani (page does not exist)") (**1986**). *Phased State Search*. [Fall Joint Computer Conference](http://www.informatik.uni-trier.de/~ley/db/conf/fjcc/fjcc86.html#MarslandS86), [pdf](http://webdocs.cs.ualberta.ca/~tony/OldPapers/fjcc.1986.pdf)
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek"), [Marcus Wagner](Marcus_Wagner "Marcus Wagner") (**1986**). *Selective Search versus Brute Force.* [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
* [Ronald L. Rivest](Ronald_L._Rivest "Ronald L. Rivest") (**1987**). *Game Tree Searching by Min/Max Approximation*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 34, No. 1, [pdf 1995](http://people.csail.mit.edu/rivest/Rivest-GameTreeSearchingByMinMaxApproximation.pdf)
* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1989**). *Control Strategies for Two-Player Games.* ACM Computing Surveys, Vol. 21, No. 2, [pdf](http://www.theinformationist.com/pdf/constrat.pdf/)
* [Stuart Russell](Stuart_Russell "Stuart Russell"), [Eric Wefald](Eric_Wefald "Eric Wefald") (**1989**). *[On optimal game-tree search using rational metareasoning](http://portal.acm.org/citation.cfm?id=1623807).* In Proceedings of the Eleventh International Joint Conference on Artificial Intelligence, Detroit, MI: Morgan Kaufmann, [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.79.9229&rep=rep1&type=pdf)
* [Liwu Li](Liwu_Li "Liwu Li") (**1989**). *[Probabilistic Analysis of Search](https://doi.org/10.7939/R3VX06F26)*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), advisor [Tony Marsland](Tony_Marsland "Tony Marsland")
* [Wolfgang Nagl](index.php?title=Wolfgang_Nagl&action=edit&redlink=1 "Wolfgang Nagl (page does not exist)") (**1989**). *Best-Move Proving: A Fast Game Tree Searching Program*. [Heuristic Programming in AI 1](1st_Computer_Olympiad#Workshop "1st Computer Olympiad")


### 1990 ...


* [Toshihide Ibaraki](Toshihide_Ibaraki "Toshihide Ibaraki"), [Naoki Katoh](index.php?title=Naoki_Katoh&action=edit&redlink=1 "Naoki Katoh (page does not exist)") (**1990**). *[Searching Minimax Game Trees Under Memory Space Constraint](https://link.springer.com/article/10.1007/BF01531075)*. [Annals of Mathematics and Artificial Intelligence](https://link.springer.com/journal/10472), Vol. 1, Nos. 1-4
* [Victor Allis](Victor_Allis "Victor Allis"), [Maarten van der Meulen](Maarten_van_der_Meulen "Maarten van der Meulen"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1991**). *Proof-Number Search.* Technical Reports in Computer Science, CS 91-01. Department of Computer Science, [University of Limburg](Maastricht_University "Maastricht University")
* [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Computer Chess and Search.* Encyclopedia of Artificial Intelligence (2nd ed.) (ed. S.C. Shapiro) John Wiley & Sons, Inc. [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf) [[4]](#cite_note-4) [[5]](#cite_note-5)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum") (**1992**). *On Optimal Game Tree Propagation for Imperfect Players*. [AAAI-92](AAAI "AAAI"), [pdf](http://www.aaai.org/Papers/AAAI/1992/AAAI92-078.pdf)
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich") (**1993**). *[A Bibliography on Minimax Trees](http://portal.acm.org/citation.cfm?id=165007)*. [ACM SIGACT News](ACM#SIG "ACM"), Vol. 24, No. 4
* [Deniz Yuret](Deniz_Yuret "Deniz Yuret") (**1994**). *[The Principle of Pressure in Chess](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=EJurXJ4AAAAJ&cstart=40&citation_for_view=EJurXJ4AAAAJ:TQgYirikUcIC)*. TAINN 1994
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Chris McConnell](Chris_McConnell "Chris McConnell") (**1995**). *B\* Probability Based Search.* [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University") Computer Science research report, Pittsburgh, PA, [postscript](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/ccm/www/papers/BStar.ps)
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich"), [Marc Gengler](index.php?title=Marc_Gengler&action=edit&redlink=1 "Marc Gengler (page does not exist)") (**1995**). *[A Survey on Minimax Trees and Associated Algorithms](http://link.springer.com/chapter/10.1007/978-1-4613-3557-3_2)*. *[Minimax and Its Applications](http://link.springer.com/book/10.1007/978-1-4613-3557-3)*. [Kluwer Academic Publishers](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1995**). *Best Play for Imperfect Players and Game Tree Search*. Part 1 - Theory
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1995**). *Best Play for Imperfect Players and Game Tree Search*. with pseudocode appendix by [Charles Garrett](index.php?title=Charles_Garrett&action=edit&redlink=1 "Charles Garrett (page does not exist)"), [ps](http://scorevoting.net/WarrenSmithPages/homepage/bpip1.ps)
* [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Charles Garrett](index.php?title=Charles_Garrett&action=edit&redlink=1 "Charles Garrett (page does not exist)"), [Rico Tudor](index.php?title=Rico_Tudor&action=edit&redlink=1 "Rico Tudor (page does not exist)") (**1995**). *Best Play for Imperfect Players and Game Tree Search*. Part 2 - Experiments, [ps](http://scorevoting.net/WarrenSmithPages/homepage/bpip2.ps)
* [Andrew N. Walker](Andy_Walker "Andy Walker") (**1996**). *Hybrid Heuristic Search*. [ICCA Journal, Vol. 19, No. 1](ICGA_Journal#19_1 "ICGA Journal")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1997**). *On the k-best Mode in Computer Chess: Measuring the Similarity of Move Proposals.* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Eric B. Baum](Eric_B._Baum "Eric B. Baum"), [Warren D. Smith](Warren_D._Smith "Warren D. Smith") (**1997**). *A Bayesian Approach to Relevance in Game Playing*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 97, [CiteSeerX](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.26.7961)
* [Donald E. Knuth](Donald_Knuth "Donald Knuth") (**1998**). *[The Art Of Computer Programming](http://www-cs-faculty.stanford.edu/%7Eknuth/taocp.html) Vol 3. Sorting and Searching, Second Edition*, Addison-Wesley
* [Wim Pijls](Wim_Pijls "Wim Pijls"), [Arie de Bruin](Arie_de_Bruin "Arie de Bruin") (**1998**). *[Game Tree Algorithms and Solution Trees](http://link.springer.com/chapter/10.1007/3-540-48957-6_12)*. [CG 1998](CG_1998 "CG 1998")


### 2000 ...


* [Paul E. Utgoff](Paul_E._Utgoff "Paul E. Utgoff"), [Richard P. Cochran](Richard_P._Cochran "Richard P. Cochran") (**2000**). *[A Least-Certainty Heuristic for Selective Search](http://link.springer.com/chapter/10.1007/3-540-45579-5_1)*. [CG 2000](CG_2000 "CG 2000"), [pdf](http://people.cs.umass.edu/~utgoff/papers/springer-lcf.pdf) » [LCF](Richard_P._Cochran#LCF "Richard P. Cochran")
* [Thomas Thomsen](index.php?title=Thomas_Thomsen&action=edit&redlink=1 "Thomas Thomsen (page does not exist)") (**2000**). *[Lambda-Search in Game Trees - with Application to Go](http://link.springer.com/chapter/10.1007/3-540-45579-5_2)*. [CG 2000](CG_2000 "CG 2000") also published in [ICGA Journal, Vol. 23, No. 4](ICGA_Journal#23_4 "ICGA Journal"), winning the 2001 [ICGA Journal Award](ICGA_Journal#JournalAward "ICGA Journal"), [preprint as pdf](http://www.t-t.dk/publications/lambda_icga.pdf) » [Lambda-Search](index.php?title=Lambda-Search&action=edit&redlink=1 "Lambda-Search (page does not exist)")
* [Todd W. Neller](Todd_W._Neller "Todd W. Neller") (**2000**). *Simulation-Based Search for Hybrid System Control and Analysis*. Ph.D. thesis, [Stanford University](Stanford_University "Stanford University"), advisor [Richard Fikes](Richard_Fikes "Richard Fikes"), [pdf](http://cs.gettysburg.edu/~tneller/papers/neller-dissertation.pdf)
* [Martin Müller](Martin_M%C3%BCller "Martin Müller") (**2001, 2002**). *Proof-Set Search*. Technical Report TR 01-09, [University of Alberta](University_of_Alberta "University of Alberta"), [CG 2002](CG_2002 "CG 2002"), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.20.9972) [[6]](#cite_note-6)
* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2002**). *Exploring the Computational Limits of Large Exhaustive Search Problems*. Ph.D thesis, [ETH Zurich](ETH_Zurich "ETH Zurich"), [pdf](http://e-collection.library.ethz.ch/eserv/eth:25905/eth-25905-02.pdf) » [Awari](Awari "Awari"), [Repetitions](Repetitions "Repetitions") [[7]](#cite_note-7)
* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)") (**2003**). *[Knowledge-Based Search in Competitive Domains](http://portal.acm.org/citation.cfm?id=776752.776792&coll=DL&dl=GUIDE&CFID=34101495&CFTOKEN=18614940)*. IEEE Transactions on Knowledge and Data Engineering, Vol. 15, No. 3
* [Arie de Bruin](Arie_de_Bruin "Arie de Bruin"), [Wim Pijls](Wim_Pijls "Wim Pijls") (**2003**). *[Trends in game tree search](https://repub.eur.nl/pub/459)*. [Erasmus University, Rotterdam](https://en.wikipedia.org/wiki/Erasmus_University_Rotterdam)
* [David Rasmussen](David_Rasmussen "David Rasmussen") (**2004**). *Parallel Chess Searching and Bitboards.* Masters thesis, [ps](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/3267/ps/imm3267.ps)
* [Yan Radovilsky](Yan_Radovilsky "Yan Radovilsky"), [Solomon Eyal Shimony](Solomon_Eyal_Shimony "Solomon Eyal Shimony") (**2004**). *Generalized Model for Rational Game Tree Search*. [SMC 2004](https://dblp.uni-trier.de/db/conf/smc/smc2004-2.html), [pdf](https://www.cs.bgu.ac.il/~yanr/Publications/smc04.pdf) [[8]](#cite_note-8)
* [Markian Hlynka](Markian_Hlynka "Markian Hlynka"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2004**). *Pre-Searching*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal")
* [Markian Hlynka](Markian_Hlynka "Markian Hlynka"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2005**). *[Automatic Generation of Search Engines](http://link.springer.com/chapter/10.1007/11922155_3)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11")
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2006**). *A new Implementation of Error Analysis in Game Trees*. [ICGA Journal, Vol. 29, No. 2](ICGA_Journal#29_2 "ICGA Journal")
* [Dmitry Batenkov](index.php?title=Dmitry_Batenkov&action=edit&redlink=1 "Dmitry Batenkov (page does not exist)") (**2006**). *Modern developments of Shannon’s Chess*. [pdf](http://www.wisdom.weizmann.ac.il/~dmitryb/writing/chess_report.pdf)
* [Pim Nijssen](index.php?title=Pim_Nijssen&action=edit&redlink=1 "Pim Nijssen (page does not exist)") (**2009**). *Using Intelligent Search Techniques to Play the Game Khet*. Master's Thesis, [Maastricht University](Maastricht_University "Maastricht University"), [pdf](http://www.personeel.unimaas.nl/pim.nijssen/pub/msc.pdf) [[9]](#cite_note-9)
* [Claude G. Diderich](Claude_G._Diderich "Claude G. Diderich"), [Marc Gengler](index.php?title=Marc_Gengler&action=edit&redlink=1 "Marc Gengler (page does not exist)") (**2009**). *[Minimax Game Tree Searching](http://link.springer.com/referenceworkentry/10.1007%2F978-0-387-74759-0_370)*. [Encyclopedia of Optimization](http://link.springer.com/book/10.1007/978-0-387-74759-0), [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
* [David Silver](David_Silver "David Silver") (**2009**). *Reinforcement Learning and Simulation-Based Search*. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Applications_files/thesis.pdf)


### 2010 ...


* [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto") (**2011**). *A Study on Game-Independent Heuristics in Game-Tree Search*. Ph.D. thesis, [JAIST](JAIST "JAIST")
* [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Meng-Tsung Tsai](index.php?title=Meng-Tsung_Tsai&action=edit&redlink=1 "Meng-Tsung Tsai (page does not exist)"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2011**). *Game Tree Search with Adaptive Resolution*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13"), [pdf](https://www.conftool.net/acg13/index.php/Chang-Game_Tree_Search_with_Adaptive_Resolution-145.pdf?page=downloadPaper&filename=Chang-Game_Tree_Search_with_Adaptive_Resolution-145.pdf&form_id=145&form_version=final)
* [Alexandru Godescu](index.php?title=Alexandru_Godescu&action=edit&redlink=1 "Alexandru Godescu (page does not exist)") (**2011**). *[Information and search in computer chess](http://arxiv.org/abs/1112.2149)*. [[10]](#cite_note-10)
* [Pim Nijssen](index.php?title=Pim_Nijssen&action=edit&redlink=1 "Pim Nijssen (page does not exist)"), [Mark Winands](Mark_Winands "Mark Winands") (**2012**). *An Overview of Search Techniques in Multi-Player Games*. [ECAI CGW 2012](index.php?title=ECAI_CGW_2012&action=edit&redlink=1 "ECAI CGW 2012 (page does not exist)")
* [Abdallah Saffidine](Abdallah_Saffidine "Abdallah Saffidine"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2012**). *A General Multi-Agent Modal Logic K Framework for Game Tree Search*. [ECAI CGW 2012](index.php?title=ECAI_CGW_2012&action=edit&redlink=1 "ECAI CGW 2012 (page does not exist)")
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Mark Winands](Mark_Winands "Mark Winands"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jahn-Takeshi Saito](Jahn-Takeshi_Saito "Jahn-Takeshi Saito") (**2012**). *Game-Tree Search using Proof Numbers: The First Twenty Years*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
* [Kuo-Yuan Kao](Kuo-Yuan_Kao "Kuo-Yuan Kao"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Yi-Chang Shan](Yi-Chang_Shan "Yi-Chang Shan"), [Shi-Jim Yen](Shi-Jim_Yen "Shi-Jim Yen") (**2012**). *Selection Search for Mean and Temperature of Multi-branch Combinatorial Games*. [ICGA Journal, Vol. 35, No. 3](ICGA_Journal#35_3 "ICGA Journal")
* [David Silver](David_Silver "David Silver"), [Richard Sutton](Richard_Sutton "Richard Sutton"), [Martin Mueller](Martin_M%C3%BCller "Martin Müller") (**2013**). *Temporal-Difference Search in Computer Go*. Proceedings of the [ICAPS-13 Workshop on Planning and Learning](http://icaps13.icaps-conference.org/technical-program/workshop-program/planning-and-learning/), [pdf](http://webdocs.cs.ualberta.ca/~sutton/papers/SSM-ICAPS-13.pdf)
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2014**). *[Interest Search - Another way to do Minimax](http://www.aifactory.co.uk/newsletter/2014_01_interest_minimax.htm)*. [AI Factory](AI_Factory "AI Factory"), Summer 2014
* [Tom Holden](index.php?title=Tom_Holden&action=edit&redlink=1 "Tom Holden (page does not exist)") (**2014**). *Notes on an alternative approach to move choice in games such as Chess*. [pdf](http://www.tholden.org/wp-content/uploads/2014/11/Notes-on-an-alternative-approach-to-move-choice-in-games-such-as-Chess.pdf) [[11]](#cite_note-11)
* [Christopher D. Rosin](Christopher_D._Rosin "Christopher D. Rosin") (**2014**). *Game playing*. [WIREs Cognitive Science](https://en.wikipedia.org/wiki/Wiley_Interdisciplinary_Reviews:_Cognitive_Science), Vol. 5, [pdf preprint](http://www.chrisrosin.com/Rosin-Game-Playing-submitted-ver.pdf)


### 2015 ...


* [Jakub Pawlewicz](Jakub_Pawlewicz "Jakub Pawlewicz"), [Ryan Hayward](Ryan_Hayward "Ryan Hayward") (**2015**). *Feature Strength and Parallelization of Sibling Conspiracy Number Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14")
* [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Critical Position Identiﬁcation in Games and Its Application to Speculative Play](https://www.researchgate.net/publication/281152992_Critical_Position_Identification_in_Games_and_Its_Application_to_Speculative_Play)*. [ICAART 2015](http://www.scitepress.org/DigitalLibrary/ProceedingsDetails.aspx?ID=+mGlly8Sp00=&t=1)
* [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [E. Mei Ang](index.php?title=E._Mei_Ang&action=edit&redlink=1 "E. Mei Ang (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Identifying Critical Positions Based on Conspiracy Numbers](http://link.springer.com/chapter/10.1007%2F978-3-319-27947-3_6)*. [Agents and Artificial Intelligence](http://link.springer.com/book/10.1007/978-3-319-27947-3), [ICAART 2015 - Revised Selected Papers](http://dblp.uni-trier.de/db/conf/icaart/icaart2015s.html#KhalidAYII15)
* [Ting-Han Wei](Ting-Han_Wei "Ting-Han Wei"), [Chao-Chin Liang](Chao-Chin_Liang "Chao-Chin Liang"), [I-Chen Wu](I-Chen_Wu "I-Chen Wu"), [Lung-Pin Chen](index.php?title=Lung-Pin_Chen&action=edit&redlink=1 "Lung-Pin Chen (page does not exist)") (**2015**). *Software Development Framework for Job-Level Algorithms*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
* [Tobias Joppen](Tobias_Joppen "Tobias Joppen"), [Miriam Moneke](index.php?title=Miriam_Moneke&action=edit&redlink=1 "Miriam Moneke (page does not exist)"), [Nils Schroder](index.php?title=Nils_Schroder&action=edit&redlink=1 "Nils Schroder (page does not exist)"), [Christian Wirth](index.php?title=Christian_Wirth&action=edit&redlink=1 "Christian Wirth (page does not exist)"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2017**). *[Informed Hybrid Game Tree Search for General Video Game Playing](http://ieeexplore.ieee.org/document/7970136/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. PP, No. 99
* [Michael Hartisch](index.php?title=Michael_Hartisch&action=edit&redlink=1 "Michael Hartisch (page does not exist)"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2019**). *A Novel Application for Game Tree Search - Exploiting Pruning Mechanisms for Quantified Integer Programs*. [Advances in Computer Games 16](Advances_in_Computer_Games_16 "Advances in Computer Games 16")


### 2020 ...


* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)"), [Tristan Cazenave](Tristan_Cazenave "Tristan Cazenave") (**2020**). *Minimax Strikes Back*. [arXiv:2012.10700](https://arxiv.org/abs/2012.10700) » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [Quentin Cohen-Solal](index.php?title=Quentin_Cohen-Solal&action=edit&redlink=1 "Quentin Cohen-Solal (page does not exist)") (**2021**). *Completeness of Unbounded Best-First Game Algorithms*. [arXiv:2109.09468](https://arxiv.org/abs/2109.09468)


## Forum Posts


### 1999


* [Some crazy ideas](https://www.stmintz.com/ccc/index.php?id=47379) by Gareth McCaughan, [CCC](CCC "CCC"), March 29, 1999


### 2000 ...


* [About search algorithms and heuristics](https://www.stmintz.com/ccc/index.php?id=112586) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), May 26, 2000
* [Search algorithms and effeciency](https://www.stmintz.com/ccc/index.php?id=172496) by Kim Roper Jensen, [CCC](CCC "CCC"), May 30, 2001
* [Search algorithms in chess programs](https://www.stmintz.com/ccc/index.php?id=201686) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), December 12, 2001
* [Search algorithms](https://www.stmintz.com/ccc/index.php?id=325977) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), November 06, 2003
* [Game tree search algorithms](https://www.stmintz.com/ccc/index.php?id=343686) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), January 20, 2004


### 2005 ...


* [Search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6665) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007 » [Fail-Soft](Fail-Soft "Fail-Soft"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Even more search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6666) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007 » [Root](Root "Root"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?t=402) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 05, 2007 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge"), [Evaluation](Evaluation "Evaluation")


 [Re: Search or Evaluation?](http://www.hiarcs.net/forums/viewtopic.php?p=2944) by [Mark Uniacke](Mark_Uniacke "Mark Uniacke"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 14, 2007
* [Efficient algorithm for k-best mode?](http://www.talkchess.com/forum/viewtopic.php?t=17921) by [Gijsbert Wiesenekker](Gijsbert_Wiesenekker "Gijsbert Wiesenekker"), [CCC](CCC "CCC"), November 17, 2007


### 2010 ...


* [Scaling at 2x nodes (or doubling time control).](http://www.talkchess.com/forum/viewtopic.php?t=48733) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 23, 2013 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Houdini](Houdini "Houdini")
* [Is search irrelevant when computing ahead of very big trees?](http://www.talkchess.com/forum/viewtopic.php?t=48743) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), July 24, 2013 » [Knowledge](Knowledge "Knowledge")
* [Improve the search or the evaluation?](http://www.talkchess.com/forum/viewtopic.php?t=49190) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), August 31, 2013 » [Evaluation](Evaluation "Evaluation"), [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
* [Slow Searchers?](http://www.talkchess.com/forum/viewtopic.php?t=49906) by Michael Neish, [CCC](CCC "CCC"), November 02, 2013
* [A new algorithm accounting for the uncertainty in eval funcs](http://www.talkchess.com/forum/viewtopic.php?t=54324) by [Tom Holden](index.php?title=Tom_Holden&action=edit&redlink=1 "Tom Holden (page does not exist)"), [CCC](CCC "CCC"), November 12, 2014


### 2015 ...


* [Search algorithm in it's simplest forum](http://www.talkchess.com/forum/viewtopic.php?t=55474) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 25, 2015 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Time assignment to children](http://www.talkchess.com/forum/viewtopic.php?t=57092) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 26, 2015
* [Some musings about search](http://www.talkchess.com/forum/viewtopic.php?t=57270) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 14, 2015 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [Search](http://www.talkchess.com/forum/viewtopic.php?t=60581) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), June 24, 2016
* [Searching using slow eval with tactical verification](http://www.talkchess.com/forum/viewtopic.php?t=61348) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 06, 2016
* [Root search](http://www.talkchess.com/forum/viewtopic.php?t=61358) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), September 08, 2016 » [Root](Root "Root")
* [Doubling of time control](http://www.talkchess.com/forum/viewtopic.php?t=61784) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 21, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Komodo](Komodo "Komodo")
* [search efficiency](http://www.talkchess.com/forum/viewtopic.php?t=64390) by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni"), [CCC](CCC "CCC"), June 23, 2017
* [comparing between search or evaluation](http://www.talkchess.com/forum/viewtopic.php?t=65403) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 09, 2017 » [Evaluation](Evaluation "Evaluation")


### 2020 ...


* [Tactical search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74170) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), June 13, 2020 » [Tactics](Tactics "Tactics")
* [Listening for GUI input when searching](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77189) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 27, 2021 » [GUI](GUI "GUI"), [Thread](Thread "Thread"), [UCI](UCI "UCI")
* [On reaching maximum ply](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77202) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), April 29, 2021 » [Maximum Search Depth](Depth#MaxPly "Depth"), [Ply](Ply "Ply")
* [Search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78505) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), October 26, 2021
* [Strategies to unit testing the search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79276) by Olexiy Svitashev, [CCC](CCC "CCC"), February 03, 2022 » [Engine Testing](Engine_Testing "Engine Testing")


## External Links


* [Search algorithm from Wikipedia](https://en.wikipedia.org/wiki/Search_algorithm)
* [Combinatorial search from Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_search)
* [Depth-first search from Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
* [Boost Graph Library: Depth-First Search](http://www.boost.org/doc/libs/1_42_0/libs/graph/doc/depth_first_search.html)
* [Best-first search from Wikipedia](https://en.wikipedia.org/wiki/Best-first_search)


 [A\* search algorithm from Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
* [Breadth-first search from Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
* [Dijkstra's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* [Lambda-search Java-code (version 2.0)](http://www.t-t.dk/go/cg2000/code20.html) by [Thomas Thomsen](index.php?title=Thomas_Thomsen&action=edit&redlink=1 "Thomas Thomsen (page does not exist)")
* [Chess Programming Part IV: Basic Search](http://www.gamedev.net/page/resources/_/technical/artificial-intelligence/chess-programming-part-iv-basic-search-r1171) by [François-Dominic Laramée](Fran%C3%A7ois-Dominic_Laram%C3%A9e "François-Dominic Laramée"), [gamedev.net](https://en.wikipedia.org/wiki/GameDev.net), Ausgust 2000
* [Chess Programming Part V: Advanced Search](http://www.gamedev.net/page/resources/_/technical/artificial-intelligence/chess-programming-part-v-advanced-search-r1197) by [François-Dominic Laramée](Fran%C3%A7ois-Dominic_Laram%C3%A9e "François-Dominic Laramée"), [gamedev.net](https://en.wikipedia.org/wiki/GameDev.net), September 2000
* [Engine - Hispanic Chess Engines | The search function](https://sites.google.com/site/hispanicchessengines/programs--interface---engines/engine) by [Pedro Castro](Pedro_Castro "Pedro Castro")
* [An Introduction to Game Tree Algorithms](http://hamedahmadi.com/gametree/) by [Hamed Ahmadi](Hamed_Ahmadi "Hamed Ahmadi")
* [Miroslav Vitouš](Category:Miroslav_Vitou%C5%A1 "Category:Miroslav Vitouš") - [Infinite Search](https://de.wikipedia.org/wiki/Infinite_Search) (1969), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Jack DeJohnette](Category:Jack_DeJohnette "Category:Jack DeJohnette"), [John McLaughlin](Category:John_McLaughlin "Category:John McLaughlin"), [Herbie Hancock](Category:Herbie_Hancock "Category:Herbie Hancock"), [Joe Henderson](Category:Joe_Henderson "Category:Joe Henderson")
 
## References


1. [↑](#cite_ref-1) [Schach Bilder Welten - Bernd Besser - Galerie](http://schachbilderwelten.tenners.de/html/galerie.html)
2. [↑](#cite_ref-2) [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf)
3. [↑](#cite_ref-3) [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1946**). *Het denken van den Schaker, een experimenteel-psychologische studie*. Ph.D. thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam); N.V. Noord-Hollandse Uitgevers Maatschappij, [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam). Translated with the help of [George Baylor](George_Baylor "George Baylor"), with additions (in **1965**) as *Thought and Choice in Chess*. Mouton Publishers, The Hague. ISBN 90-279-7914-6. ([amazon](http://www.amazon.com/gp/reader/9027979146/ref=sib_dp_pt#reader-link))
4. [↑](#cite_ref-4) [Excellent Computer-Chess Overview Paper Found!](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7df61a100528f201) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 6, 1997
5. [↑](#cite_ref-5) [Great article for people who wants to write a chess engine](https://www.stmintz.com/ccc/index.php?id=221364) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 03, 2002
6. [↑](#cite_ref-6) [Re: A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233322) by [Dan Andersson](index.php?title=Dan_Andersson&action=edit&redlink=1 "Dan Andersson (page does not exist)"), June 01, 2002
7. [↑](#cite_ref-7) [Re: Aquarium IDEA, repetitions, and minimax over cycles](http://www.open-chess.org/viewtopic.php?f=5&t=2093#p17469) by [syzygy](Ronald_de_Man "Ronald de Man"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2012
8. [↑](#cite_ref-8) [Re: Interesting ideas](http://www.talkchess.com/forum/viewtopic.php?t=57560&start=14) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), September 09, 2015
9. [↑](#cite_ref-9) [Khet (game) from Wikipedia](https://en.wikipedia.org/wiki/Khet_%28game%29)
10. [↑](#cite_ref-10) [Information and search in computer chess (Godescu)](http://www.open-chess.org/viewtopic.php?f=5&t=1736) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 12, 2011
11. [↑](#cite_ref-11) [A new algorithm accounting for the uncertainty in eval funcs](http://www.talkchess.com/forum/viewtopic.php?t=54324) by [Tom Holden](index.php?title=Tom_Holden&action=edit&redlink=1 "Tom Holden (page does not exist)"), [CCC](CCC "CCC"), November 12, 2014

**[Up one Level](Home "Home")**







 
