---
title: Workshop Chess and Mathematics
---
**[Home](Home "Home") \* [Conferences](Conferences "Conferences") \* Workshop Chess and Mathematics**


  




[![Logo TU Dresden.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Logo_TU_Dresden.svg/255px-Logo_TU_Dresden.svg.png)](http://en.wikipedia.org/wiki/Dresden_University_of_Technology)
 Fakultät Mathematik und Naturwissenschaften Institut für Numerische Mathematik
 **Workshop Chess and Mathematics** <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
 [Dresden](https://en.wikipedia.org/wiki/Dresden), November 21st and 22nd, 2008
### Contents


* [1 Chess Olympiad 2008](#chess-olympiad-2008)
* [2 Programme Committee](#programme-committee)
* [3 Public Lecture](#public-lecture)
	+ [3.1 Schach und Mathematik](#schach-und-mathematik)
		- [3.1.1 German Abtract](#german-abtract)
		- [3.1.2 English Abtract](#english-abtract)
* [4 Invited and Contributed Lectures](#invited-and-contributed-lectures)
	+ [4.1 Multi-Cut](#multi-cut)
	+ [4.2 General Game Playing](#general-game-playing)
	+ [4.3 Optimal Line-Ups](#optimal-line-ups)
	+ [4.4 Combinatorics](#combinatorics)
	+ [4.5 Spielstärkeprognosen](#spielst.c3.a4rkeprognosen)
	+ [4.6 Solving Chess](#solving-chess)
	+ [4.7 Information of Chess Positions](#information-of-chess-positions)
	+ [4.8 Bitoptimiertes Speichern](#bitoptimiertes-speichern)
	+ [4.9 Endgame Databases](#endgame-databases)
	+ [4.10 Sliding Pieces Attacks](#sliding-pieces-attacks)
	+ [4.11 Valuation Equilibrium](#valuation-equilibrium)
	+ [4.12 Problem Chess and Mathematics](#problem-chess-and-mathematics)
	+ [4.13 Databases for Chess Problems](#databases-for-chess-problems)
	+ [4.14 Die Schachwelt im Internet](#die-schachwelt-im-internet)
* [5 References](#references)






The Workshop Chess and Mathematics was side event of the [Chess Olympiad, Dresden 2008](https://en.wikipedia.org/wiki/38th_Chess_Olympiad), the Public Lecture took place at the [Congress Center](http://www.dresden-congresscenter.de/eng/eng_1.htm), the Invited and Contributed Lectures on Saturday at the [TU Dresden](https://en.wikipedia.org/wiki/Dresden_University_of_Technology).



## Programme Committee


* [Prof. J. Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt") (Zürich)
* [Dr. U. Lorenz](Ulf_Lorenz "Ulf Lorenz") (Darmstadt)
* [Jun.-Prof. T. Linß](Torsten_Lin%C3%9F "Torsten Linß") (Dresden)
* [Prof. Hans-G. Roos](Mathematician#HGRoos "Mathematician") (Dresden)


## Public Lecture


### Schach und Mathematik


[Christian Hesse](Christian_Hesse "Christian Hesse"), Stuttgart <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>  

**SCHACH UND MATHEMATIK**  

Fr., 16:00, Congress Center (German)  




### German Abtract


Schach und Mathematik gehören zum geistigen Weltkulturerbe. Aufgrund ihrer inneren Logik bestehen viele Parallelen zwischen ihnen. Beide sind ein Resonanzboden für Kreativität, Leidenschaft, Ästhetik und Harmonie. Der Vortrag ist populäarwissenschaftlich angelegt und zeigt einige Highlights der Anwendung mathematischer Ideen auf Probleme des Schachs. Allgemeinverständlichkeit wird angestrebt.



### English Abtract


Chess and mathematics belong to the mental world cultural heritage. Due to their internal logic many parallels between them exist. Both are a resonance ground for creativity, passion, aesthetics and harmony. The popular science lecture shows some highlights of the application of mathematical ideas to problems of chess. Generally comprehensibleness is aimed at.



## Invited and Contributed Lectures


### Multi-Cut


[Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), Reykjavik  

**[MULTI-CUT](Multi-Cut "Multi-Cut"): A SPECULATIVE PRUNING MECHANISM FOR CHESSPLAYING PROGRAMS** <a id="cite-note-5" href="#cite-ref-5">[5]</a>  

Sa., 09:00, TU Dresden, WIL C207  



The [alpha-beta](Alpha-Beta "Alpha-Beta") algorithm is the most popular method for searching game-trees in adversary board games such as chess. It is much more efficient than a plain brute-force minimax search because it allows a large portion of the game-tree to be pruned, while still backing up the correct game-tree value. However, the number of nodes visited by the algorithm still increases exponentially with increasing search depth. This obviously limits the scope of the search, since game-playing programs must meet external time constraints: often having only a few minutes to make a decision. To somewhat alleviate this problem so-called speculative-pruning methods are used to cut off less interesting lines of play prematurely, while allowing interesting lines to be explored more deeply.


Here we discuss one such speculative-pruning method called [multi-cut](Multi-Cut "Multi-Cut"), which makes pruning decisions based not only on the risk of pruning off relevant lines of play, but also on the likelihood of such an erroneous pruning decision affecting the move decision at the [root](Root "Root") of the [search tree](Search_Tree "Search Tree"). The method has been successfully employed by several of the world’s strongest commercial chess program for a number of years.



### General Game Playing


[Michael Thielscher](Michael_Thielscher "Michael Thielscher"), Dresden  

**ARTIFICIAL INTELLIGENCE AND GENERAL GAME PLAYING** <a id="cite-note-6" href="#cite-ref-6">[6]</a>  

Sa., 09:45, TU Dresden, WIL C207  



Chess computers play at the same level as the best human players these days, but their general intelligence is severely limited. Most chess programs cannot even play slight variations of the game–like Bughouse Chess–let alone completely different games such as Tic-Tac-Toe, which every child easily learns to play well.


A general game player is a computer that understands a description of the rules of arbitrary games and learns to play these games well without human intervention. In this talk we introduce General Game Playing from the perspective of Artificial Intelligence research and provide some insight into our system [FLUXPLAYER](http://www.general-game-playing.de/research.html), which has been crowned the world champion at the Second General Game Playing Competition in 2006 in Boston.



### Optimal Line-Ups


[Stefan Schwarz](index.php?title=Stefan_Schwarz&action=edit&redlink=1 "Stefan Schwarz (page does not exist)"), Jena  

**OPTIMAL LINE-UPS IN TEAM COMPETITIONS WITH (NON-)LINEAR OBJECTIVE FUNCTIONS**  

Sa., 10:50, TU Dresden, WIL C207  



We consider a team competition (as in chess) where every member of team




```
A = {a1, . . . , an}

```

plays against exactly one member of team




```
B = {b1, . . . , bn},

```

where ai > 0 and bi > 0 denote the playing strength of the i-th player of team A and B, respectively. We assume that a player with strength bj playing against a player with strength ai gets in average



[](File:WSCMFormula1.jpg)
points. Further we assume that the sequence of team A is fixed whereas team B can order its players in an arbitrary permutation ¶. If the aim of team B is to maximize the expected sum of points



[](File:WSCMFormula2.jpg)
we get the well known assignment problem with a linear objective function. But in many applications team B do not want to maximize the expected number of points, but e. g. the probability of having more points than A. This results in an assignment problem with a non-linear objective function. We show for a broad class of such non-linear assignment problems that the set of potentially optimal permutations is exactly the same as in the linear case. That means for every permutation ¶ which is an unique optimal solution of a non-linear assignment problem, there is already a linear assignment problem such that ¶ is the unique optimum.



### Combinatorics


[Bernd Steinbach](Bernd_Steinbach "Bernd Steinbach"), Freiberg (with [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), St. Augustine)  

**COMBINATORICS ON THE CHESS BOARD – SOLUTIONS USING LOGIC EQUATIONS**  

Sa., 11:25, TU Dresden, WIL C207  



The [satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) (SAT) for Logic Equations has been well explored <a id="cite-note-7" href="#cite-ref-7">[7]</a>, many algorithms are available, mostly search-oriented. Based on a new data structure (ternary vectors) <a id="cite-note-8" href="#cite-ref-8">[8]</a>, very efficient parallel algorithms for its solution have been designed and implemented.
It will be shown that many combinatorial problems can be transformed into satisfiability problems and solved using these developed algorithms. The approach is constructive and very general, no research procedures are involved, results are always complete. It can be concluded that the solution algorithms for SAT can be used (in the sense of [NP-completeness](https://en.wikipedia.org/wiki/NP-complete)) for many other combinatorial problems in a very general way. Among the problems that have been solved are questions of the type



* How many queens (rooks, bishops, knights, fairy chess pieces, ?) can be placed on the chess board without threatening each other?
* Are there [Hamiltonian cycles](https://en.wikipedia.org/wiki/Hamiltonian_path) or paths on the chess board, and how many of them, again for different pieces?
* The n+k-problem: Is it possible to place n+k queens on a board of size n × n if k pawns are placed on the board.
* All these problems can also be considered not only on an 8 × 8 chess board, but also on boards of size n ×m, n,m > 0.


### Spielstärkeprognosen


[Robert Offinger](http://www.math.uni-magdeburg.de/%7Erooff/Mathematik.html), Magdeburg  

**SPIELSTÄRKEPROGNOSEN AUFGRUND DER BISHERIGEN ENTWICKLUNG DER ELO-ZAHL**
MIT HILFE VON STATISTISCHEN METHODEN
Sa., 11:35, TU Dresden, WIL C207  



Primäres Ziel unserer Untersuchung, die vom Deutschen Schachbund angeregt wurde, ist es, das Entwicklungspotential eines jungen, bis ca. 25 Jahre alten Spielers einzuschätzen und statistische Hilfsmittel bei der Aufstellung der Kader zur Verfügung zu stellen.


Zu Beginn unseres Vortrages werfen wir einen kurzen Blick auf bisherige rudimentäre Ansätze, die in diese Richtung unternommen wurden. Wir betrachten anschließend verschiedene neue Modelle für den Verlauf der mittleren Spielstärke gemessen in Ratingpunkten. Mit Hilfe dieser Modelle versuchen wir sowohl die mittlere Spielstärke eines Spielers in einem zukünftigen Zeitraum allein aufgrund der bisher erreichten Elo-Zahlen zu schätzen, als auch die konkrete Elo-Zahl zu einem Zeitpunkt mitsamt einem Unsicherheitsbereich vorherzusagen. Nachdem wir die Güte der Modelle für den angestrebten Personenkreis beurteilt haben, diskutieren wir abschließend, ob unser Modell auch für Clubspieler brauchbare Ergebnisse liefert und wo noch Schwachstellen und Verbesserungsmöglichkeiten der statistischen Modelle liegen.




### Solving Chess


[Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), Tilburg  

**CONDITIONS AND PREDICTIONS FOR SOLVING THE GAME OF CHESS**  

Sa., 13:30, TU Dresden, WIL C207 <a id="cite-note-9" href="#cite-ref-9">[9]</a>  



Chess is an attractive pastime and scientifically interesting by its complexity, its tactics, and its strategies. After fifty years of computer-chess research we have reached the situation (already since 1997) that computer programs outperform the best human beings. The next prevailing question therefore is: can a computer program solve the game of chess? The number of different reachable positions is 10^46 ([Chinchalkar](Shirish_Chinchalkar "Shirish Chinchalkar"), 1996).


However arranging the list of positions in such a way that they can be visited or cut off by a clever computer program requires



* (1) a new intelligent approach,
* (2) a considerable speed-up of computer power, and
* (3) a considerable enlargement of storage capabilities.


Stimulating developments in this respect are



* (a) Solving Checkers by [Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") et al. (2007), and
* (b) defeating [Kim Myungwan](http://senseis.xmp.net/?KimMyungwan) on [Go](Go "Go") (in a 9-stone handicap match, 2008).


New techniques potentially usable in chess are:



* (i) [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"),
* (ii) [UCT](UCT "UCT") (Upper Confidence bounds applied to Trees),
* (iii) Supercomputers, such as IBMp6 (with 3328 processors), and
* (iv) Grid Technology.


Conditions on and predictions for these techniques will be discussed in the lecture as well as their impact. An optimistic date for solving chess is 2035 and a pessimistic one (assuming that we can solve the game) is 2065. The solving time in 2035 (optimistic prediction) will be between 37 days and 4 months.



* [Chinchalkar, S.](Shirish_Chinchalkar "Shirish Chinchalkar") (**1996**). *An Upper Bound for the Number of Reachable Positions.* [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 19, No. 3, pp. 181-183.
* [Schaeffer, J.](Jonathan_Schaeffer "Jonathan Schaeffer") et al. (**2007**). *Checkers is Solved*. Science, Vol. 317, No. 5844, pp. 1518-1522.






### Information of Chess Positions


[J. Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt"), Zürich  

**THE INFORMATION CONTENT OF CHESS POSITIONS AND ITS IMPLICATIONS**  

Sa., 14:15, TU Dresden, WIL C207  



Experiments in [cognitive](Cognition "Cognition") [psychology](index.php?title=Psychology&action=edit&redlink=1 "Psychology (page does not exist)") involving the visual processing of chess positions ([A. de Groot](Adriaan_de_Groot "Adriaan de Groot"), [H.A. Simon](Herbert_Simon "Herbert Simon"), et al.) have revealed stark contrasts as well as similarities between chess masters and novices. In essence, and not surprisingly, experts perform much better than novices when facing realistic chess positions, but not on board positions where pieces are placed at random. The superior performance on realistic positions is explained by the expert’s ability to encode the position into perceptual [chunks](Chunking "Chunking"), each consisting of a familiar subconfiguration of pieces”. This encoding fails for random positions, where the expert’s chess specific knowledge does not help. This insight raises the question of investigating the fuzzy but intuitively meaningful concept “realistic chess position”. We describe a technique based on guessing an unknown position by asking questions. Experiments indicate that on average, 70 to 80 bits of information suffice to identify a randomly chosen realistic position. It follows that realistic positions are a tiny fraction of all legal positions.



### Bitoptimiertes Speichern


Eduard Humburg, Wolfratshausen  

**BITOPTIMIERTES SPEICHERN EINER SCHACHSTELLUNG**  

Sa., 14:35, TU Dresden, WIL C207 (German)  



Es wird eine Notation vorgeschlagen, die es ermöglicht, jede mögliche Schachstellung in optimierter Form binär zu codieren. Ein Programm, das sowohl die Codierung (Stellung wird eingegeben und daraus der Code erzeugt) als auch die Decodierung (aus einem codierten Datensatz wird die Stellung wieder erzeugt) wurde entwickelt.
Dabei werden außer der Darstellung der Figuren auch die Zusatzinformationen für Zugrecht, en-passant, Rochaderechte, 50-Züge-Regel und Gesamtzugzahl berücksichtigt. Ebenso sind auch alle Umwandlungen erfasst. Als interessantes Resultat ergibt sich eine obere Schranke für die Anzahl aller möglichen Stellungen.



### Endgame Databases


[Eiko Bleicher](Eiko_Bleicher "Eiko Bleicher"), Berlin  

**ENDGAME DATABASES FOR THE GAME OF CHESS**  

Sa., 15:15, TU Dresden, WIL C207  



Chess endgame analysis has been a topic of interest for many decades. [Databases](Endgame_Tablebases "Endgame Tablebases") started on paper and evolved with the available hardware. Space and time have always defined bounds to the complexity of the endgames examined. The best-known products of the recent years are [Ken Thompson's databases](Thompson%27s_Databases "Thompson's Databases"), the [Nalimov tablebases](Nalimov_Tablebases "Nalimov Tablebases") and the [ShredderBases](index.php?title=ShredderBases&action=edit&redlink=1 "ShredderBases (page does not exist)"). Whereas those database solve endgames in their entirety, the program [Freezer](Freezer "Freezer") makes analysis of more advanced endgames accessible by relying on imperfect information in the database generation process. This presentation will give an outline of the database build process in general and in Freezer.



### Sliding Pieces Attacks


[Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), Hattingen  

**[EFFICIENT GENERATION OF MOVES AND CONTROLS FOR SLIDING PIECES](Efficient_Generation_of_Sliding_Piece_Attacks "Efficient Generation of Sliding Piece Attacks")**  

Sa., 16:00, TU Dresden, WIL C207  



Attack-Sets as Base for [Bitboard](Bitboards "Bitboards") [Move-generation](Move_Generation "Move Generation"): Opposed to “None-sliding” pieces, [Knight](Knight "Knight"), [King](King "King") and [Pawn](Pawn "Pawn"), whose attacks are determined by its origin square only, [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") like [Rook](Rook "Rook")-, [Bishop](Bishop "Bishop")- and [Queen](Queen "Queen")-attacks are dependend on other pieces as well, which may block the attacking ray in one particular ray-direction. In [Quiescence Search](Quiescence_Search "Quiescence Search") the performance of generating (winning) capture moves is crucial. Opposed to classical [square-centric](Mailbox "Mailbox") [board-representations](Board_Representation "Board Representation") , which require loops over squares, bitboards permit more efficient algorithms in generating sliding attacks.



### Valuation Equilibrium


[Christian Seel](http://de.wikipedia.org/wiki/Christian_Seel), Bonn  

**VALUATION EQUILIBRIUM**  

Sa., 16:20, TU Dresden, WIL C207  



We study a boundedly rational approach to extensive form games by valuations (Jehiel 2007). Differing from standard microeconomics, players are unable to foresee the whole game tree, but group “similar” actions together (for example the same move in similar positions of a chess game) and attach a valuation to each of these groups. Our aim is to analyze how the partitioning into groups emerges and which equilibria satisfy a certain robustness criterion.



### Problem Chess and Mathematics


[Hans-Peter Rehm](http://de.wikipedia.org/wiki/Hans-Peter_Rehm), Karlsruhe  

**PROBLEM CHESS AND MATHEMATICS**  

Sa., 17:00, TU Dresden, WIL C207  



The role of symmetries of different kinds of the Chess Space and the set of thematical moves for the aesthetical value of chess compositions.



* Symmetry and asymmetry in position and thematical contents.
* Themes concerning the action of the symmetrical group on the set of played moves in a composition.


Generalized Chess in chess problem composition.



* Other chess spaces (e.g. the three dimensional STEREO CHESS)
* Other kinds of pieces and rules.


### Databases for Chess Problems


[Torsten Linß](Torsten_Lin%C3%9F "Torsten Linß"), Limerick  

**DATABASES FOR THE COMPOSITION OF CHESS PROBLEMS**  

Sa., 17:45, TU Dresden, WIL C207  



Databases (or endgame table bases) have been used in the analysis of the game of chess. Some of these EGTB by Herik, Thompson and Nalimov are available online and are used in some chess engines. In chess composition they have been used since the early 1970s (Mertens, with some earlier examples from the 1940s and 1950s by Halumbirek who used paper as main memory and his brain as processor).


The focus in chess composition is quite different from over-the-board competetive chess: it is the artistic value of the compositions (chess problems and studies) one is interested in. Apparently, databases can be used to verify the soundness of a composition, i.e. that there is only the solution intended by the authors, but they can also be searched for interesting problems. The latter often means to find the needle in a stack of hey of some millions of formally sound chess problems - with no clear/programmable definition at hand what constitutes an interesting problem.


In the talk the author will elaborate on these issues and present some (very) preliminary results.



### Die Schachwelt im Internet


Rolf Beran, Altlandsberg  

**DIE SCHACHWELT IM INTERNET**  

Sa., 18:05, TU Dresden, WIL C207 (German)  



Das Internet als Quelle für:



* Spieleplattformen (zum online-Schachspielen)
* Partiedatenbanken (zur gegnerspezifischen Vorbereitung, zur Auswahl von Theorievarianten, zur Analyse von Beispielpartien)
* Turnier- und Ergebnisdatenbanken (für statistische und historische Informationen)
* Einkauf (zur Beschaffung aktueller und antiquarischer Literatur, Spielmaterial)
* Schach-Linksammlungen (zur Orientierung und Suche nach weiterführenden Informationen)
* Personenbezogene Seiten (für biografische Informationen)
* Thematische Seiten (zur Vertiefung spezieller Eröffnungen)
* Aktuelle Berichterstattung und live-Übertragungen
* Audiovisuelle Medien (Schachvideos bei youtube, Kurzanleitung zur Herstellung eigener Schachvideos zu Lehrzwecken)
* Hintergrundwissen/Sonstiges (z.B. was sind pgn-Dateien?, wie wird die Elo-Zahl berechnet?)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [CHESS AND MATHEMATICS - Workshop Dresden, 21st - 23rd November 2008](http://www.math.tu-dresden.de/num/chess2008/index-en.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Workshop Chess and Mathematics](http://www.math.tu-dresden.de/num/chess2008/abstracts.pdf) (pdf) agenda and abstracts
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Prof. Dr. Christian Hesse](http://www.isa.uni-stuttgart.de/AbMathStat/Hesse/) from [Universität Stuttgart](http://www.uni-stuttgart.de/index.en.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Schach: Flow und mathematisches Modell, Interview mit Professor Christian Hesse](http://www.chessbase.de/nachrichten.asp?newsid=8375), [ChessBase News](ChessBase "ChessBase"), November 15, 2008 (German)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252, pp. 177-196. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [AAAI'08 Tutorial General Game Playing, Michael Thielscher, Dresden](http://cgi.cse.unsw.edu.au/~mit/Slides/AAAI08-Tutorial.pdf) (pdf)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Bernd Steinbach](Bernd_Steinbach "Bernd Steinbach"), [Christian Posthoff](Christian_Posthoff "Christian Posthoff") (**2007**). *Set-Based SAT-Solving*. [pdf](https://pdfs.semanticscholar.org/9a62/c2f75d619ea8b6fc07e55881f2724f5a33ac.pdf)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Bernd Steinbach](Bernd_Steinbach "Bernd Steinbach"), [Christina Dorotska](http://www.informatik.tu-freiberg.de/~dorotska/) (**2000**). *[Orthogonal Block Building Using Ordered Lists of Ternary Vectors](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.32.6551)*. [Freiberg University of Mining and Technology](https://en.wikipedia.org/wiki/Freiberg_University_of_Mining_and_Technology), [pdf](http://www.informatik.tu-freiberg.de/prof2/publikationen/BP2000_OBB.pdf)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Jaap van den Herik « Glarean Magazin | Ist im Jahr 2035 Schluss mit Schach?](http://glareanverlag.wordpress.com/tag/jaap-van-den-herik/) by [Eric van Reem](Eric_van_Reem "Eric van Reem"), January 2009 (German)

**[Up one Level](Conferences "Conferences")**







 
