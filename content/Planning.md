---
title: Planning
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* Planning**



[ Plan is law, fulfillment is duty, over-fulfillment is honor! <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Planning**,  

the process of applying knowledge, [thinking](https://en.wikipedia.org/wiki/Thought) and [prediction](https://en.wikipedia.org/wiki/Prediction) to create and maintain a [plan](https://en.wikipedia.org/wiki/Plan), a [temporal](https://en.wikipedia.org/wiki/Temporal_logic) set of intended actions to achieve a certain goal, in chess, to finally win the game. 



## Long-range Planning


Long-range planning by human chess players is usually made on the basis of [reasoning](https://en.wikipedia.org/wiki/Reason), [experience](https://en.wikipedia.org/wiki/Experience), and [intuition](https://en.wikipedia.org/wiki/Intuition_%28psychology%29), as investigated by [De Groot](Adriaan_de_Groot "Adriaan de Groot") in 1946 <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Search and Evaluation


Conventional [depth-first](Depth-First "Depth-First") [alpha-beta searchers](Alpha-Beta "Alpha-Beta") have no real sense of planning other than [minimaxing](Minimax "Minimax") their [score](Score "Score") inside their [search horizons](Horizon_Effect "Horizon Effect"). Inside chess programs, planning is often implicit due to [look ahead](Search "Search") and certain [evaluation](Evaluation "Evaluation") features and their associated weights. For instance, a bonus for a [Rook on an open file](Rook_on_Open_File "Rook on Open File"), and another bonus to [occupy the 7th rank](Rook_on_Seventh "Rook on Seventh") is a typical example to mimic some kind of strategic planning. However, long-range planning and seeking for goals requires [pattern recognition](Pattern_Recognition "Pattern Recognition") and associated advices if they match.



## Oracle Approaches


[Oracle](Oracle "Oracle") approaches such as [pre-processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables") and initializing [piece-square tables](Piece-Square_Tables "Piece-Square Tables") based on features and pattern of the [root](Root "Root") may realize plans like [minority attack](Minority_Attack "Minority Attack") and along with [pawn structure](Pawn_Structure "Pawn Structure") and king placement, plans to attack the king. However, with todays typical [search depths](Depth "Depth") one has to consider [path-dependencies](Path-Dependency "Path-Dependency"), [transposition table](Transposition_Table "Transposition Table") anomalies and resulting [search instabilities](Search_Instability "Search Instability"). Instead, oracle approaches at or near the root, may be used to initialize dedicated piece-square tables for the sole purpose to control [selectivity](Selectivity "Selectivity") further down the tree, for instance to [extend](Extensions "Extensions") moves according to a certain plan. 



## Chess Quotes


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



* [Frank Marshall](https://en.wikipedia.org/wiki/Frank_Marshall_%28chess_player%29): A bad plan is better than none at all.
* [Emanuel Lasker](Mathematician#EmanuelLasker "Mathematician"): To find the right plan is just as hard as looking for its sound justification.
* [Eugene Znosko-Borovsky](https://en.wikipedia.org/wiki/Eugene_Znosko-Borovsky): It is not a move, even the best move that you must seek, but a realizable plan.
* [Alexander Kotov](https://en.wikipedia.org/wiki/Alexander_Kotov): It is better to follow out a plan consistently even if it isn't the best one than to play without a plan at all. The worst thing is to wander about aimlessly.


## Chess Programs


* [N.N.](N.N. "N.N.")
* [Paradise](Paradise "Paradise")
* [Planner](Planner "Planner")
* [Symbolic](Symbolic "Symbolic")


## See also


* [CHE](index.php?title=CHE&action=edit&redlink=1 "CHE (page does not exist)")
* [Chunking](Chunking "Chunking")
* [Cognition](Cognition "Cognition")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Learning](Learning "Learning")
* [Opponent Model Search](Opponent_Model_Search "Opponent Model Search")
* [Oracle](Oracle "Oracle")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Pattern Recognition](Pattern_Recognition "Pattern Recognition")
* [Pre-Processing](Piece-Square_Tables#Preprocessing "Piece-Square Tables")
* [Psychology](index.php?title=Psychology&action=edit&redlink=1 "Psychology (page does not exist)")
* [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [Strategy](Strategy "Strategy")
* [Tactics](Tactics "Tactics")
* [Time Management](Time_Management "Time Management")


## Publications


### 1946 ...


* [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1946**). *Het denken van den Schaker, een experimenteel-psychologische studie.* Ph.D. thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam), advisor [Géza Révész](Mathematician#Revesz "Mathematician"); N.V. Noord-Hollandse Uitgevers Maatschappij, [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam). Translated with the help of [George Baylor](George_Baylor "George Baylor"), with additions, (in **1965**) as *Thought and Choice in Chess*. Mouton Publishers, The Hague. ISBN 90-279-7914-6.


### 1950 ...


* [Max Euwe](Max_Euwe "Max Euwe") (**1953**). *Judgment and Planning in Chess*. McKay Company, New York, N.Y. <a id="cite-note-6" href="#cite-ref-6">[6]</a>


### 1960 ...


* [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1965, 1978**). *Thought and Choice in Chess*. Mouton & Co Publishers, The Hague, The Netherlands. ISBN 90-279-7914-6
* [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html) pp. 110-115, [pdf](http://doczine.com/bigdata/2/1366100941_3145d71044/mi2-ch7-good.pdf) from [doczine](http://doczine.com/)


### 1970 ...


* [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik") (**1970**). *Computers, Chess and Long-Range Planning*. Springer-Verlag, New York.
* [Walter R. Reitman](Walter_R._Reitman "Walter R. Reitman"), [James Kerwin](index.php?title=James_Kerwin&action=edit&redlink=1 "James Kerwin (page does not exist)"), [Robert Nado](index.php?title=Robert_Nado&action=edit&redlink=1 "Robert Nado (page does not exist)"), [Judith S. Reitman](index.php?title=Judith_Spencer_Olson&action=edit&redlink=1 "Judith Spencer Olson (page does not exist)"), [Bruce Wilcox](index.php?title=Bruce_Wilcox&action=edit&redlink=1 "Bruce Wilcox (page does not exist)") (**1974**). *[Goals and Plans in a Program for Playing Go](http://dl.acm.org/citation.cfm?id=810391)*. Proceedings of the 29th [ACM](ACM "ACM") Conference
* [Larry R. Harris](Larry_Harris "Larry Harris") (**1975**) *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [4. IJCAI 1975](http://dblp.uni-trier.de/db/conf/ijcai/ijcai75.html), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat") (**1977**). *A Chess Combination Program Which Uses Plans.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol 8, No. 3
* [Russell M. Church](index.php?title=Russell_M._Church&action=edit&redlink=1 "Russell M. Church (page does not exist)"), [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1977**). *Plans, Goals, and Search Strategies for the Selection of a Move in Chess*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")
* [David Wilkins](David_Wilkins "David Wilkins") (**1979**). *Using Patterns and Plans to Solve Problems and Control Search*. Ph.D. thesis, Computer Science Dept, [Stanford University](Stanford_University "Stanford University"), Stanford, California, AI Lab Memo AIM-329
* [David Wilkins](David_Wilkins "David Wilkins") (**1979**). *Using plans in chess*. In Proceedings of the 1979 International Joint Conference on Artificial Intelligence, (Tokyo, Japan), pp. 960-967.
* [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat") (**1979**). *A Program which Uses Plans for Finding Combinations in Chess*. [ICCA Newsletter, Vol. 2 No. 2](ICGA_Journal#2_2 "ICGA Journal")


### 1980 ...


* [David Wilkins](David_Wilkins "David Wilkins") (**1980**). *Using patterns and plans in chess*. Artificial Intelligence, Vol. 14, pp. 165-203. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat") (**1980**). *The Behaviour of a Chess Combination Program using Plans.* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1980**). *Long-Range Planning in Computer Chess*. Master's thesis, Department of Computer Science, [University of Waterloo](University_of_Waterloo "University of Waterloo")
* [Sarah E. Goldin](index.php?title=Sarah_E._Goldin&action=edit&redlink=1 "Sarah E. Goldin (page does not exist)"), [Barbara Hayes-Roth](http://www.ksl.stanford.edu/people/bhr/) (**1980**). *[Individual Differences in Planning Processes](http://www.rand.org/pubs/notes/N1488.html)*. [RAND](https://en.wikipedia.org/wiki/RAND_Corporation) note N-1488
* [Jaime Carbonell](Jaime_Carbonell "Jaime Carbonell") (**1981**). *Counterplanning: A Strategy-Based Model of Adversary Planning in Real-World Situations*. Artificial Intelligence, Vol. 16
* [Kai von Luck](Kai_von_Luck "Kai von Luck"), [Bernd Owsnicki](Bernd_Owsnicki-Klewe "Bernd Owsnicki-Klewe") (**1982**). *N.N.: A View of Planning in Chess*. in [Wahlster](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/w/Wahlster:Wolfgang.html), [GWAI-82](http://www.informatik.uni-trier.de/%7Eley/db/conf/ki/gwai1982.html)
* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Construction of Planned Move Trees for Chess Pawn Endings*. Sigart Newsletter 80, pp. 163-168.
* [E. D. Cherevik](Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Y. M. Shvyrkov](http://www.amazon.de/s/ref=dp_byline_sr_book_2?ie=UTF8&field-author=Y.M.+Shvyrkov&search-alias=books-de-intl-us&text=Y.M.+Shvyrkov) (**1982**). *[An ABC of Planning : Fundamentals of the Theory and Methodology of Economic Planning](https://catalog.lib.uchicago.edu/vufind/Record/517650)*. [Progress Moscow](https://en.wikipedia.org/wiki/Progress_Publishers)
* [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *Positional Long-Range Planning in Computer Chess.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3"), also published as [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1983**). *Positional Long-Range Planning in Computer Chess.* [Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology"), Austria.
* [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**1984**). *Advice and Planning in Chess Endgames.* Artificial and Human Thinking (eds. S. Amarel, A. Elithorn and R. Banerji). North-Holland.


### 1985 ...


* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1985**). *Goals, Plans, and Mechanisms: Non-symbolically in an Evaluation Surface.* Presentation at Evolution, Games, and Learning, Center for Nonlinear Studies, [Los Alamos National Laboratory](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), May 21.
* [Richard Korf](Richard_Korf "Richard Korf") (**1987**). *Planning as Search: A Quantitative Approach.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 33, pp. 65-88.
* [David Wilkins](David_Wilkins "David Wilkins") (**1988**). *Practical Planning: Extending the Classical AI Planning Paradigm*. (Morgan Kaufmann Series in Representation and Reasoning), [amazon](http://www.amazon.com/ref=gno_logo)
* [Bruce Abramson](Bruce_Abramson "Bruce Abramson") (**1989**). *Control Strategies for Two-Player Games.* [ACM Computing Surveys](ACM#Surveys "ACM"), Vol. 21, No. 2
* [Reiner Seidel](Reiner_Seidel "Reiner Seidel") (**1989**). *A Model of Chess Knowledge - Planning Structures and Constituent Analysis*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")


### 1990 ...


* [David Wilkins](David_Wilkins "David Wilkins") (**1991**). *Working notes on paradise chess patterns*. Technical Note 509, AI Center, SRI International, 333 Ravenswood Ave., Menlo Park, CA 94025
* [Jens Christensen](Jens_Christensen "Jens Christensen"), [Adam Grove](http://www.informatik.uni-trier.de/%7Eley/db/indices/a-tree/g/Grove:Adam_J=.html) (**1991**). *A Formal Model Classical Planning*. [IJCAI-91](http://dblp.uni-trier.de/db/conf/ijcai/ijcai91.html#ChristensenG91), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-91-VOL1/PDF/039.pdf)
* [Jens Christensen](Jens_Christensen "Jens Christensen") (**1991**). *[Automatic Abstraction in Planning](http://naca.larc.nasa.gov/search.jsp?R=19970034976&qs=N%3D4294129240%2B4294374694)*. Ph.D. thesis, [Stanford University](Stanford_University "Stanford University")
* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)") (**1992**). *Pattern-Based Tactical Planning*. [IJPRAI](http://www.informatik.uni-trier.de/~ley/db/journals/ijprai/ijprai6.html#Walczak92), Vol. 6, No. 5
* [Stephen J.J. Smith](Stephen_J.J._Smith "Stephen J.J. Smith"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Thomas A. Throop](Thomas_A._Throop "Thomas A. Throop") (**1992**). *[A hierarchical approach to strategic planning with non-cooperating agents under conditions of uncertainty](http://dl.acm.org/citation.cfm?id=139657)*. Proceedings of the First International Conference on AI Planning Systems
* [Stephen J.J. Smith](Stephen_J.J._Smith "Stephen J.J. Smith"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau") (**1993**). *[Strategic planning for imperfect-information games](http://dl.acm.org/citation.cfm?id=171355&coll=DL&dl=GUIDE&CFID=403943247&CFTOKEN=26458653)*. Technical Report, [University of Maryland, College Park](https://en.wikipedia.org/wiki/University_of_Maryland,_College_Park)
* [Mikhail Botvinnik](Mikhail_Botvinnik "Mikhail Botvinnik"), [Evgeniĭ Dmitrievich Cherevik](Evgeni%C4%AD_Dmitrievich_Cherevik "Evgeniĭ Dmitrievich Cherevik"), [Vasily Vladimirov](Vasily_Vladimirov "Vasily Vladimirov"), [Vitaly Vygodsky](Vitaly_Vygodsky "Vitaly Vygodsky") (**1994**). *[Solving Shannon's Problem: Ways and Means](https://getinfo.de/app/Solving-Shannon-s-Problem-Ways-and-Means/id/BLCP%3ACN011979464)*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7") » [CC Sapiens](CC_Sapiens "CC Sapiens")
* [Andreas L. Opdahl](Andreas_L._Opdahl "Andreas L. Opdahl"), [Bjornar Tessem](index.php?title=Bjornar_Tessem&action=edit&redlink=1 "Bjornar Tessem (page does not exist)") (**1994**). *Long-Term Planning in Computer Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")


### 1995 ...


* [Stephen J.J. Smith](Stephen_J.J._Smith "Stephen J.J. Smith"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Thomas A. Throop](Thomas_A._Throop "Thomas A. Throop") (**1996**). *Total-Order Multi-Agent Task-Network Planning for Contract Bridge*. [AAAI 1996](AAAI "AAAI")
* [Henry Kautz](https://en.wikipedia.org/wiki/Henry_Kautz), [Bart Selman](Bart_Selman "Bart Selman") (**1996**). *Pushing the Envelope: Planning, Propositional Logic, and Stochastic Search*. [AAAI 1996](AAAI "AAAI"), [pdf](http://www.cs.cornell.edu/selman/papers/pdf/plan.pdf)
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
* [Jussi Tella](http://fi.wikipedia.org/wiki/Jussi_Tella) (**1997**). *[Planning in Games](http://www.cs.hut.fi/~sto/planning-seminaari/tella/planning-in-games.htm)*. Seminar on Knowledge Engineering, Fall 1997, [Helsinki University of Technology](https://en.wikipedia.org/wiki/Helsinki_University_of_Technology)
* [Jan van Reek](Jan_van_Reek "Jan van Reek") (**1997**). *Strategy in Chess*. Schachfirma Fruth, Unterhaching, ISBN 3-9804896-9-8
* [Jan van Reek](Jan_van_Reek "Jan van Reek"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1998**). *Planning a Strategy in Chess*. [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
* [Stephen J.J. Smith](Stephen_J.J._Smith "Stephen J.J. Smith"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [Thomas A. Throop](Thomas_A._Throop "Thomas A. Throop") (**1998**). *Computer Bridge: A Big Win for AI Planning*. AI Magazine, Vol. 19, No. 2
* [Ian Frank](Ian_Frank "Ian Frank") (**1998**). *[Search and Planning Under Incomplete Information: A Study Using Bridge Card Play](http://www.goodreads.com/book/show/7998822-search-and-planning-under-incomplete-information)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), Ph.D. thesis, [University of Edinburgh](University_of_Edinburgh "University of Edinburgh")


### 2000 ...


* [Mark Brockington](Mark_Brockington "Mark Brockington") (**2000**). *Computer Chess Meets Planning*. [ICGA Journal, Vol. 23, No. 2](ICGA_Journal#23_2 "ICGA Journal")
* [Alex B. Meijer](index.php?title=Alex_B._Meijer&action=edit&redlink=1 "Alex B. Meijer (page does not exist)"), [Henk Koppelaar](Henk_Koppelaar "Henk Koppelaar") (**2001**). *[Pursuing abstract goals in the game of Go](http://www.kbs.twi.tudelft.nl/Publications/Conference/2001/2001-MeijerKoppelaar-BNAIC01.html)*. [BNAIC 2001](http://hcs.science.uva.nl/bnaic01/)
* [Adi Botea](Adi_Botea "Adi Botea") (**2002**). *Using Abstraction for Heuristic Search and Planning*. Research Summary. In Proceedings of the 5th International Symposium on Abstraction, Reformulation, and Approximation SARA-02, volume 2371 of Lecture Notes in Artificial Intelligence, 326-327, Kananaskis, AB, Canada.
* [Ari Shapiro](index.php?title=Ari_Shapiro&action=edit&redlink=1 "Ari Shapiro (page does not exist)"), [Gil Fuchs](index.php?title=Gil_Fuchs&action=edit&redlink=1 "Gil Fuchs (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**2002**). *[Learning a Game Strategy Using Pattern-Weights and Self-play](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_4)*. [CG 2002](CG_2002 "CG 2002")
* [Adi Botea](Adi_Botea "Adi Botea"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2002**). *[Using Abstraction for Planning in Sokoban](http://link.springer.com/chapter/10.1007/978-3-540-40031-8_24)*. [CG 2002](CG_2002 "CG 2002")
* [Joelle Pineau](Joelle_Pineau "Joelle Pineau") (**2004**). *Tractable Planning Under Uncertainty: Exploiting Structure*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](http://www.cs.mcgill.ca/~jpineau/files/jpineau-thesis.pdf)
* [Malik Ghallab](https://scholar.google.com/citations?user=A4v885AAAAAJ&hl=en), [Dana Nau](Dana_S._Nau "Dana S. Nau"), [Paolo Traverso](https://scholar.google.it/citations?user=ho38I-wAAAAJ&hl=en) (**2004**). *[Automated Planning: Theory and Practice](http://projects.laas.fr/planning/aptp/index.html)*. [Morgan Kaufmann Publishers](https://en.wikipedia.org/wiki/Morgan_Kaufmann_Publishers)
* [Yan Radovilsky](Yan_Radovilsky "Yan Radovilsky"), [Solomon Eyal Shimony](Solomon_Eyal_Shimony "Solomon Eyal Shimony") (**2004**). *Generalized Model for Rational Game Tree Search*. [SMC 2004](https://dblp.uni-trier.de/db/conf/smc/smc2004-2.html), [pdf](https://www.cs.bgu.ac.il/~yanr/Publications/smc04.pdf) <a id="cite-note-7" href="#cite-ref-7">[7]</a>


### 2005 ...


* [Adi Botea](Adi_Botea "Adi Botea"), [Markus Enzenberger](Markus_Enzenberger "Markus Enzenberger"), [Martin Müller](Martin_M%C3%BCller "Martin Müller"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**2005**). *Macro-FF: Improving AI Planning with Automatically Learned Macro-Operators*. Journal of Artificial Intelligence Research 24 (2005) 581-621, [pdf](http://www.jair.org/media/1696/live-1696-2537-jair.pdf)
* [René Alquézar](http://www.lsi.upc.edu/~alquezar/), A. Gonzalez Camargo, [Alejandro González Romero](Alejandro_Gonz%C3%A1lez_Romero "Alejandro González Romero") (**2006**). *[Evolving Plans for the KRKa2 Chess Ending](http://portal.acm.org/citation.cfm?id=1166904)*. Artificial Intelligence and Applications 2006
* [Adi Botea](Adi_Botea "Adi Botea") (**2006**). *Improving AI Planning and Search with Automatic Abstraction*. PhD Thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](http://abotea.rsise.anu.edu.au/data/thesis.pdf)
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Csaba Szepesvári](Csaba_Szepesv%C3%A1ri "Csaba Szepesvári") (**2006**). *[Bandit based Monte-Carlo Planning](http://www.computer-go.info/resources/bandit.html)* ECML-06, LNCS/LNAI 4212, pp. 282-293. introducing [UCT](UCT "UCT"), [pdf](http://www.sztaki.hu/%7Eszcsaba/papers/ecml06.pdf)
* [Frantisek Sailer](index.php?title=Frantisek_Sailer&action=edit&redlink=1 "Frantisek Sailer (page does not exist)"), [Michael Buro](Michael_Buro "Michael Buro"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot") (**2007**). *Adversarial planning through strategy simulation*. [Computational Intelligence and Games](IEEE#CIG "IEEE"), [pdf](https://skatgame.net/mburo/ps/rtsmc.pdf)
* [Zvi Retchkiman Königsberg](Zvi_Retchkiman_K%C3%B6nigsberg "Zvi Retchkiman Königsberg") (**2007**). *A Combinatorial Game Mathematical Strategy Planning Procedure for a Class of Chess Endgames*. [International Mathematical Forum, Vol. 2, No. 68](http://www.m-hikari.com/imf-password2007/65-68-2007/index.html)
* [Sylvain Gelly](Sylvain_Gelly "Sylvain Gelly"), [Jean-Baptiste Hoock](Jean-Baptiste_Hoock "Jean-Baptiste Hoock"), [Arpad Rimmel](index.php?title=Arpad_Rimmel&action=edit&redlink=1 "Arpad Rimmel (page does not exist)"), [Olivier Teytaud](Olivier_Teytaud "Olivier Teytaud"), [Yann Kalemkarian](http://fr.linkedin.com/pub/yann-kalemkarian/7/7aa/716) (**2008**). *The Parallelization of Monte-Carlo Planning - Parallelization of MC-Planning*. ICINCO-ICSO 2008: 244-249, [pdf](http://hal.archives-ouvertes.fr/docs/00/28/78/67/PDF/icin08.pdf), [slides as pdf](http://www.lri.fr/~teytaud/UCTpara.pdf)
* [Akihiro Kishimoto](Akihiro_Kishimoto "Akihiro Kishimoto"), [Alex Fukunaga](index.php?title=Alex_Fukunaga&action=edit&redlink=1 "Alex Fukunaga (page does not exist)"), [Adi Botea](Adi_Botea "Adi Botea") (**2009**). *Scalable, Parallel Best-First Search for Optimal Sequential Planning*. In Proceedings of the [19th International Conference on Automated Planning and Scheduling](http://icaps09.uom.gr/) (ICAPS-2009) (Best Paper Award), pages 201-208, [pdf](http://abotea.rsise.anu.edu.au/data/kishimoto-etal-icaps09.pdf)
* [Gerhard Trippen](index.php?title=Gerhard_Trippen&action=edit&redlink=1 "Gerhard Trippen (page does not exist)") (**2009**). *Plans, Patterns and Move Categories Guiding a Highly Selective Search*. [Advances in Computer Games 12](Advances_in_Computer_Games_12 "Advances in Computer Games 12"), [pdf](http://arimaa.com/arimaa/papers/0905Trippen/Contribution118.pdf)


### 2010 ...


* [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Ashish Sabharwal](Ashish_Sabharwal "Ashish Sabharwal"), [Bart Selman](Bart_Selman "Bart Selman") (**2010**). *[On Adversarial Search Spaces and Sampling-Based Planning](http://www.aaai.org/ocs/index.php/ICAPS/ICAPS10/paper/view/1458)*. [ICAPS 2010](http://www.aaai.org/Press/Proceedings/icaps10.php)
* [Raghuram Ramanujan](Raghuram_Ramanujan "Raghuram Ramanujan"), [Bart Selman](Bart_Selman "Bart Selman") (**2011**). *[Trade-Offs in Sampling-Based Adversarial Planning](http://aaai.org/ocs/index.php/ICAPS/ICAPS11/paper/view/2708)*. [ICAPS 2011](http://www.aaai.org/Press/Proceedings/icaps11.php), [best paper](http://videolectures.net/raghuram_ramanujan/), [VideoLecture](http://videolectures.net/icaps2011_ramanujan_sampling/) » [UCT](UCT "UCT")
* [Ari Weinstein](Ari_Weinstein "Ari Weinstein"), [Michael L. Littman](Michael_L._Littman "Michael L. Littman") (**2013**). *Open-Loop Planning in Large-Scale Stochastic Domains*. [AAAI-2013](Conferences#AAAI-2013 "Conferences")
* [Ari Weinstein](Ari_Weinstein "Ari Weinstein") (**2013**). *Local Planning For Continuous Markov Decision Processes*. Ph.D. thesis, [Rutgers University](https://en.wikipedia.org/wiki/Rutgers_University), advisor [Michael L. Littman](Michael_L._Littman "Michael L. Littman"), [pdf](http://cs.brown.edu/~mlittman/theses/weinstein.pdf)
* [Arthur Guez](Arthur_Guez "Arthur Guez"), [David Silver](David_Silver "David Silver"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2014**). *Better Optimism By Bayes: Adaptive Planning with Rich Models*. [arXiv:1402.1958v1](https://arxiv.org/abs/1402.1958)
* [Arthur Guez](Arthur_Guez "Arthur Guez"), [Nicolas Heess](index.php?title=Nicolas_Heess&action=edit&redlink=1 "Nicolas Heess (page does not exist)"), [David Silver](David_Silver "David Silver"), [Peter Dayan](Peter_Dayan "Peter Dayan") (**2014**). *Bayes-Adaptive Simulation-based Search with Value Function Approximation*. [NIPS 2014](https://papers.nips.cc/book/advances-in-neural-information-processing-systems-27-2014), [pdf](https://papers.nips.cc/paper/5501-bayes-adaptive-simulation-based-search-with-value-function-approximation.pdf)


### 2015 ...


* [Arthur Guez](Arthur_Guez "Arthur Guez") (**2015**). *Sample-based Search Methods for Bayes-Adaptive Planning*. Ph.D. Thesis, Gatsby Computational Neuroscience Unit, [University College London](https://en.wikipedia.org/wiki/University_College_London), [pdf](http://www.gatsby.ucl.ac.uk/~aguez/files/guez_phdthesis2015.pdf)
* [Malik Ghallab](https://scholar.google.com/citations?user=A4v885AAAAAJ&hl=en), [Dana Nau](Dana_S._Nau "Dana S. Nau"), [Paolo Traverso](https://scholar.google.it/citations?user=ho38I-wAAAAJ&hl=en) (**2016**). *[Automated Planning and Acting](https://www.cambridge.org/core/books/automated-planning-and-acting/E6DE5715A2190651352DFB0869916BC3#)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press)
* [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Simon Schmitt](index.php?title=Simon_Schmitt&action=edit&redlink=1 "Simon Schmitt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2019**). *Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model*. [arXiv:1911.08265](https://arxiv.org/abs/1911.08265) <a id="cite-note-8" href="#cite-ref-8">[8]</a>


### 2020 ...


* [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Simon Schmitt](index.php?title=Simon_Schmitt&action=edit&redlink=1 "Simon Schmitt (page does not exist)"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Edward Lockhart](Edward_Lockhart "Edward Lockhart"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [David Silver](David_Silver "David Silver") (**2020**). *[Mastering Atari, Go, chess and shogi by planning with a learned model](https://www.nature.com/articles/s41586-020-03051-4)*. [Nature](https://en.wikipedia.org/wiki/Nature_%28journal%29), Vol. 588 <a id="cite-note-9" href="#cite-ref-9">[9]</a>


## Forum Posts


* [Plans in chess programs?](https://www.stmintz.com/ccc/index.php?id=56104) by Rodney Topor, [CCC](CCC "CCC"), June 16, 1999
* [Implementing Planning in an Engine](https://www.stmintz.com/ccc/index.php?id=347144) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), February 04, 2004
* [Possible definition of planning](https://www.stmintz.com/ccc/index.php?id=348682) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), February 12, 2004
* [When will the chess programmers write an engine that plans ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73418) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), March 20, 2020


## External Links


* [Planning from Wikipedia](https://en.wikipedia.org/wiki/Planning)
* [Plan (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Plan_%28disambiguation%29)
* [State space planning from Wikipedia](https://en.wikipedia.org/wiki/State_space_planning)
* [Strategic planning from Wikipedia](https://en.wikipedia.org/wiki/Strategic_planning)
* [Plan from Wikipedia](https://en.wikipedia.org/wiki/Plan)
* [Automated planning and scheduling from Wikipedia](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling)
* [Hierarchical task network (HTN) from Wikipedia](https://en.wikipedia.org/wiki/Hierarchical_task_network)
* [Planning fallacy from Wikipedia](https://en.wikipedia.org/wiki/Planning_fallacy)
* [Forecasting from Wikipedia](https://en.wikipedia.org/wiki/Forecasting)
* [Prediction from Wikipedia](https://en.wikipedia.org/wiki/Prediction)
* [Planning in Chess](https://www.chess.com/article/view/planning-in-chess) by [Natalia Pogonina](https://en.wikipedia.org/wiki/Natalia_Pogonina), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), June 21, 2010
* [Bigbonobo Combo](http://opsound.org/artist/bigbonobotheinternationalbigbono/) - Whitecube plan, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Лозунг «План — закон, выполнение — долг, перевыполнение — честь!» в здании Ольховско-Батьковского торфяного предприятия в Кубринске, Переславский район - «Plan is law, fulfillment is duty, over-fulfillment is honor!» Building Olkhovskaya Batkovsky - peat enterprise [Kubrinsk](http://www.stad.com/index.php?city_id=540014), [Pereslavskiy district](https://en.wikipedia.org/wiki/Pereslavsky_District), Photo by Н. Частов (N. Part), November 1997, [Five-Year Plans for the National Economy of the Soviet Union - Wikipedia](https://en.wikipedia.org/wiki/Five-Year_Plans_for_the_National_Economy_of_the_Soviet_Union)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Jan van Reek](Jan_van_Reek "Jan van Reek") (**1997**). *Strategy in Chess*. Schachfirma Fruth, Unterhaching, ISBN 3-9804896-9-8
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Jan van Reek](Jan_van_Reek "Jan van Reek"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1998**). *Planning a Strategy in Chess*. [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1946**). *Het denken van den Schaker, een experimenteel-psychologische studie.* Ph.D. thesis, [University of Amsterdam](https://en.wikipedia.org/wiki/University_of_Amsterdam); N.V. Noord-Hollandse Uitgevers Maatschappij, [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam). Translated with the help of [George Baylor](George_Baylor "George Baylor"), with additions, (in **1965**) as *Thought and Choice in Chess*. Mouton Publishers, The Hague. ISBN 90-279-7914-6
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Chess Quotes - Strategy](http://www.chessquotes.com/topic-strategy)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Judgment and Planning in Chess](http://www.chessgames.com/perl/chesscollection?cid=1006215), games from [Dr. Max Euwe's](Max_Euwe "Max Euwe") book *Judgment and Planning in Chess*. [chessgames.com](http://www.chessgames.com/index.html)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Interesting ideas](http://www.talkchess.com/forum/viewtopic.php?t=57560&start=14) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), September 09, 2015
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [New DeepMind paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72381) by GregNeto, [CCC](CCC "CCC"), November 21, 2019
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [MuZero: Mastering Go, chess, shogi and Atari without rules](https://deepmind.com/blog/article/muzero-mastering-go-chess-shogi-and-atari-without-rules?fbclid=IwAR3mSwrn1YXDKr9uuGm2GlFKh76wBilex7f8QvBiQecwiVmAvD6Bkyjx-rE)

**[Up one Level](Knowledge "Knowledge")**







 
