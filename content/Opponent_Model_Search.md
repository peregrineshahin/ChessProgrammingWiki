---
title: Opponent Model Search
---
**[Home](Home "Home") \* [Search](Search "Search") \* Opponent Model Search**



[ Nosce hostem - know the enemy [[1]](#cite_note-1)
**Opponent Model Search** incorporates asymmetric search and [asymmetric evaluation](Asymmetric_Evaluation "Asymmetric Evaluation") techniques considering the peculiarities of an opponent, which requires explicit [knowledge](Knowledge "Knowledge") or assumption, and includes a model on how the opponent evaluates positions. Naive approaches in computer chess tournaments are [opening book](Opening_Book "Opening Book") preparation and [contempt](Contempt_Factor "Contempt Factor"). Some chess programs, notably [Psion](Psion "Psion") [[2]](#cite_note-2) , its successor [Chess Genius](Chess_Genius "Chess Genius") [[3]](#cite_note-3) , and [KnightCap](KnightCap "KnightCap") [[4]](#cite_note-4) , apply asymmetric evaluation and search, for instance to [extend](Extensions "Extensions") when the own side is in trouble but not the opponent. Other programs, like [Crafty](Crafty "Crafty"), can be adapted asymmetric for playing human chess players, specially [anti-computerchess](index.php?title=Anti-Computerchess&action=edit&redlink=1 "Anti-Computerchess (page does not exist)") specialists, for instance to reduce the program's tendency to trade material and to avoid blocked positions with a high [rammed pawn](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") versus [lever](Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)") ratio. [Ed Schröder](Ed_Schroder "Ed Schroder") proposed to reward own [hanging pieces](Hanging_Piece "Hanging Piece") to encourage complicated, [tactical](Tactics "Tactics") play versus humans, and to keep opponents under time pressure in playing immediate [ponder hits](Pondering "Pondering") [[5]](#cite_note-5) . Programs may [tune](Automated_Tuning "Automated Tuning") and [learn](Learning "Learning") feature vectors and their respective weights to maximize result scores against certain opponents as well. 




## Cross-Disciplinary Aspects


In his essay *"Too clever is dumb"* – *Kleine Philosophie des Schwindelns,* [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt") (2017) investigates speculative play from a cross-disciplinary perspective of chess, game theory, strategic decision making, philosophy, and literature, elucidating that always choosing the objectively best move (in chess as well as in everyday’s social interactions) might yield suboptimal outcomes, and that „knowing your enemy“ – as the prerequisite for successful (algorithmic as well as human) **swindles** – has in fact been long known to be the appropriate guiding principle in diverse scenarios of imperfect knowledge, dating back to the Chinese General and philosopher [Sun Tsu](https://en.wikipedia.org/wiki/Sun_Tzu) around 500 BCE.



## Further Research


Opponent Model search was further investigated by various game researchers, such as [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch"), [Xinbo Gao](Xinbo_Gao "Xinbo Gao"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg"), [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Pieter Spronck](Pieter_Spronck "Pieter Spronck") and [Sander Bakkes](index.php?title=Sander_Bakkes&action=edit&redlink=1 "Sander Bakkes (page does not exist)").


Carmel and Markovitch introduced **M**\* [[8]](#cite_note-8), a generalization of [minimax](Minimax "Minimax") that uses an arbitrary opponent model to simulate the opponent’s search, and further proved a sufficient condition for pruning and present the **αβ**\* algorithm which returns the M\* value of a tree while searching only necessary branches [[9]](#cite_note-9) . Gao et al. researched on a generalization of opponent model search, called **(D, d)-OM** search, where **D** stands for the [depth](Depth "Depth") of [search](Search "Search") by the player and **d** for the opponent’s depth of search [[10]](#cite_note-10) . The **Probabilistic** Opponent-Model Search (**PrOM**) for several game domains was developed by Donkers, Uiterwijk and Van den Herik, published in 2000 [[11]](#cite_note-11) . It uses an extended model that includes uncertainty of the opponent.



## See also


* [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation")
* [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Knowledge](Knowledge "Knowledge")
* [Learning](Learning "Learning")
* [Planning](Planning "Planning")


## Publications


### BCE ...


* [Sun Tsu](https://en.wikipedia.org/wiki/Sun_Tzu) (**around 500 BCE**). *[The Art of War.](https://en.wikipedia.org/wiki/The_Art_of_War)* CreateSpace Independent Publishing Platform, 2012.


### 1500 ...


* [Niccolò Machiavelli](https://en.wikipedia.org/wiki/Niccol%C3%B2_Machiavelli) (**1532**). *[Il Principe](https://en.wikipedia.org/wiki/The_Prince)*. [Antonio Blado d'Asola](https://it.wikipedia.org/wiki/Antonio_Blado)


### 1980 ...


* [Andrew L. Reibman](index.php?title=Andrew_L._Reibman&action=edit&redlink=1 "Andrew L. Reibman (page does not exist)"), [Bruce W. Ballard](index.php?title=Bruce_W._Ballard&action=edit&redlink=1 "Bruce W. Ballard (page does not exist)") (**1983**). *[Non-Minimax Search Strategies for Use against Fallible Opponents](http://www.aaai.org/Library/AAAI/1983/aaai83-084.php)*. Proceedings of [AAAI](AAAI "AAAI") 83
* [Ed Felten](Ed_Felten "Ed Felten") (**1989**). *Playing Against an Imperfect Opponent*. [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")
* [Peter Jansen](Peter_Jansen "Peter Jansen") (**1989**). *Problematic Positions and Speculative Play.* [Workshop on New Directions in Game-Tree Search](WCCC_1989#Workshop "WCCC 1989")


### 1990 ...


* [Peter Jansen](Peter_Jansen "Peter Jansen") (**1990**). *Problematic Positions and Speculative Play.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
* [Peter Jansen](Peter_Jansen "Peter Jansen") (**1992**). *Using Knowledge about the Opponent in Game-Tree Search*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA259234&Location=U2&doc=GetTRDoc.pdf)
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1992**). *On Asymmetries in Chess Programs.* [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal")
* [Peter Jansen](Peter_Jansen "Peter Jansen") (**1992**). *KQKR: Awareness of a Fallible Opponent*. [ICCA Journal, Vol. 15, No. 3](ICGA_Journal#15_3 "ICGA Journal")
* [Peter Jansen](Peter_Jansen "Peter Jansen") (**1993**). *KQKR: Speculatively Thwarting a Human Opponent.* [ICCA Journal, Vol. 16, No. 1](ICGA_Journal#16_1 "ICGA Journal")
* [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1993**). *[Learning Models of Opponent's Strategy in Game Playing](https://aaai.org/Library/Symposia/Fall/1993/fs93-02-019.php)*. [AAAI 1993](Conferences#AAAI-93 "Conferences"), FS-93-02, [pdf](https://www.aaai.org/Papers/Symposia/Fall/1993/FS-93-02/FS93-02-019.pdf)
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1993**). *Opponent-Model Search*. Technical Reports in Computer Science, CS 93-03. Department of Computer Science, [University of Limburg](Maastricht_University "Maastricht University"). ISSN 0922-8721.
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1993**). *Potential Applications of Opponent-Model Search. Part 1: The Domain of Applicability.* [ICCA Journal, Vol. 16, No. 4](ICGA_Journal#16_4 "ICGA Journal")
* [Luis Antunes](index.php?title=Luis_Antunes&action=edit&redlink=1 "Luis Antunes (page does not exist)"), [Luis Moniz](index.php?title=Luis_Moniz&action=edit&redlink=1 "Luis Moniz (page does not exist)"), [Carlos Azevedo](index.php?title=Carlos_Azevedo&action=edit&redlink=1 "Carlos Azevedo (page does not exist)") (**1993**). *[Rb+: the Dynamic Estimation of the Opponent's Strength](https://www.semanticscholar.org/paper/Rb-the-Dynamic-Estimation-of-the-Opponent-s-Antunes-Moniz/4844e9d1694f61d4052a87de94c4aeb2510c2404)*. [INESC-ID](https://en.wikipedia.org/wiki/INESC-ID), [Lisbon](https://en.wikipedia.org/wiki/Lisbon), [Portugal](https://en.wikipedia.org/wiki/Portugal) » [RB](Opponent_Model_Search#RB "Opponent Model Search")
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1994**). *Potential Applications of Opponent-Model Search. Part 2. Risks and strategies*. [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Bob Herschberg](Bob_Herschberg "Bob Herschberg") (**1994**). *Thoughts on the Application of Opponent-Model Search*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1994**). *Speculative Play in Computer Chess*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1994**). *[The M\* Algorithm: Incorporating Opponent Models into Adversary Search](https://www.semanticscholar.org/paper/The-M*-Algorithm%3A-Incorporating-Opponent-Models-Carmel-Markovitch/bd788272c81951dc44fa7944e0f72451ced14129)*. CIS Report #9402, [pdf](http://www.cs.technion.ac.il/~shaulm/papers/pdf/Carmel-Markovitch-CIS9402.pdf) [[12]](#cite_note-12)


### 1995 ...


* [Steven Walczak](index.php?title=Steven_Walczak&action=edit&redlink=1 "Steven Walczak (page does not exist)") (**1996**). *[Improving Opening Book Performance Through Modeling of Chess Opponents](http://portal.acm.org/citation.cfm?id=228334&dl=ACM&coll=DL&CFID=34101495&CFTOKEN=18614940)*. [ACM](ACM "ACM") Conference on Computer Science 1996
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1996**). *A Game-Tree Model Including an Opponent Model.* NAIC'96)
* [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1996**). *Incorporating Opponent Models into Adversary Search*. [AAAI 1996](Conferences#AAAI-96 "Conferences"), [pdf](http://www.cs.technion.ac.il/~shaulm/papers/pdf/Carmel-Markovitch-aaai1996.pdf)
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Yoshiyuki Kotani](Yoshiyuki_Kotani "Yoshiyuki Kotani"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1997**). *Gains and Risks of OM Search*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
* [Xinbo Gao](Xinbo_Gao "Xinbo Gao"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1998**). *[A Speculative Strategy](http://link.springer.com/chapter/10.1007/3-540-48957-6_5)*. [CG 1998](CG_1998 "CG 1998")


### 2000 ...


* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2000**). *Investigating Probabilistic Opponent-Model Search*. JCIS 2000, [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cbnaic00.pdf) (extended abstract)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Probabilistic Opponent-Model Search.* Information Science, Vol. 135, Nos. 3-4
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *Admissibility in Opponent Model Search*. BNAIC 2001
* [Xinbo Gao](Xinbo_Gao "Xinbo Gao"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2001**). *[Strategies anticipating a difference in search depth using opponent-model search](http://www.sciencedirect.com/science/article/pii/S0304397500000773)*. [Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol. 252, Nos. 1–2
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2002**). *Learning Opponent-Type Probabilities for PrOM Search*. Proceedings of the 14th Dutch-Belgian Artificial Intelligence Conference (BNAIC 2002 )(eds. H. Blockeel and M. Denecker), pp. 91-98. Leuven, Belgium.
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2003**). *Admissibility in Opponent-Model Search*. IS Journal, in press.
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2003**). *Opponent Models in Bao: Conditions of a Successfull Application*, [Advances in Computer Games 10](Advances_in_Computer_Games_10 "Advances in Computer Games 10"), [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cacg10.pdf)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers") (**2003**). *Nosce Hostem - Searching with Opponent Models*. Ph.D. thesis [Universiteit Maastricht](Maastricht_University "Maastricht University"), [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cnoscehostem.pdf)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers") (**2004**) *Opponent Models and Knowledge Symmetry in Game Tree Search*. Proceedings of the First Knowledge and Games Workshop. University of Liverpool, [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Ckag2004.pdf)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2004**). *[Opponent Models in Games](http://www.ercim.eu/publication/Ercim_News/enw57/donkers.html)*. Ercim News – Special: Game Technology, Nr. 57, April 2004, pp. 42-43. [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cercim.pdf)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), (**2004**). *Probabilistic Opponent-Model Search in Bao*. International Conference on Entertainment Computing - ICEC 2004. LNCS 3166, Springer, Berlin. pp. 409-419. [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cicec2004.pdf)


### 2005 ...


* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2005**). *Selecting Evaluation Functions in Opponent-Model Search*.[Theoretical Computer Science](https://en.wikipedia.org/wiki/Theoretical_Computer_Science_%28journal%29), Vol 349, No. 2
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Pieter Spronck](Pieter_Spronck "Pieter Spronck") (**2005**). *Opponent Modelling and Commercial Games*. (Keynote paper). [CIG’05](https://www.scimagojr.com/journalsearch.php?q=20000195030&tip=sid&clean=0)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2005**). *[Similarity Pruning in PrOM Search](http://link.springer.com/chapter/10.1007/11922155_5)*. [Advances in Computer Games 11](Advances_in_Computer_Games_11 "Advances in Computer Games 11")
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers") (**2005**). *[Opponent Models and Knowledge Symmetry in Game-Tree Search](https://www.semanticscholar.org/paper/Opponent-Models-and-Knowledge-Symmetry-in-Game-Tree-Donkers/6e37e557098873608df5847d324179cb0e199595)*. IKAT [Universiteit Maastricht](Maastricht_University "Maastricht University")
* [Austin Parker](Austin_Parker "Austin Parker"), [Dana S. Nau](Dana_S._Nau "Dana S. Nau"), [V.S. Subrahmanian](index.php?title=V.S._Subrahmanian&action=edit&redlink=1 "V.S. Subrahmanian (page does not exist)") (**2006**). *Overconfidence or Paranoia? Search in Imperfect-Information Games*. [AAAI 2006](Conferences#AAAI-2006 "Conferences"), [pdf](https://www.aaai.org/Papers/AAAI/2006/AAAI06-164.pdf)
* [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Pieter Spronck](Pieter_Spronck "Pieter Spronck") (**2006**). *Preferenced-Based Player Modelling*. In AI Game Programming Wisdom 3
* [Alan J. Lockett](Alan_J._Lockett "Alan J. Lockett"), [Charles L. Chen](index.php?title=Charles_L._Chen&action=edit&redlink=1 "Charles L. Chen (page does not exist)"), [Risto Miikkulainen](Risto_Miikkulainen "Risto Miikkulainen") (**2007**). *[Evolving Explicit Opponent Models for Game Play](http://nn.cs.utexas.edu/?lockett:gecco07)*. [GECCO 2007](https://dblp.uni-trier.de/db/conf/gecco/gecco2007c.html)
* [Sander Bakkes](index.php?title=Sander_Bakkes&action=edit&redlink=1 "Sander Bakkes (page does not exist)"), [Pieter Spronck](Pieter_Spronck "Pieter Spronck"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2009**). *Opponent Modelling for Case-based Adaptive Game AI*. [Entertainment Computing](http://www.journals.elsevier.com/entertainment-computing/), Vol. 1, Nr. 1, pp. 27-37, [pdf](http://ticc.uvt.nl/~pspronck/pubs/bakkes_journalOM.pdf)


### 2015 ...


* [Mohd Nor Akmal Khalid](index.php?title=Mohd_Nor_Akmal_Khalid&action=edit&redlink=1 "Mohd Nor Akmal Khalid (page does not exist)"), [Umi Kalsom Yusof](index.php?title=Umi_Kalsom_Yusof&action=edit&redlink=1 "Umi Kalsom Yusof (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)") (**2015**). *[Critical Position Identiﬁcation in Games and Its Application to Speculative Play](https://www.researchgate.net/publication/281152992_Critical_Position_Identification_in_Games_and_Its_Application_to_Speculative_Play)*. [ICAART 2015](http://www.scitepress.org/DigitalLibrary/ProceedingsDetails.aspx?ID=+mGlly8Sp00=&t=1)
* [Naoki Mizukami](Naoki_Mizukami "Naoki Mizukami"), [Yoshimasa Tsuruoka](Yoshimasa_Tsuruoka "Yoshimasa Tsuruoka") (**2015**). *Building a Computer Mahjong Player Based on Monte Carlo Simulation and Opponent Models*. [IEEE CIG 2015](IEEE#TOCIAIGAMES "IEEE"), [pdf](http://www.logos.ic.i.u-tokyo.ac.jp/~mizukami/paper/cig_2015.pdf)
* [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt") (**2017**). *"Too clever is dumb" - Kleine Philosophie des Schwindelns.* In: [Glarean Magazin, June 6th, 2017.](https://glarean-magazin.ch/2017/06/06/schach-essay-to-clever-is-dumb-philosophie-des-schwindelns-roland-stuckardt/) [(PDF)](http://www.stuckardt.de/rsdokumente/glarean-magazin.ch-Schach-Essay%20von%20R%20Stuckardt%20Too%20clever%20is%20dumb.pdf)


### 2020 ...


* [Hung-Jui Chang](Hung-Jui_Chang "Hung-Jui Chang"), [Cheng Yueh](index.php?title=Cheng_Yueh&action=edit&redlink=1 "Cheng Yueh (page does not exist)"), [Gang-Yu Fan](index.php?title=Gang-Yu_Fan&action=edit&redlink=1 "Gang-Yu Fan (page does not exist)"), [Ting-Yu Lin](index.php?title=Ting-Yu_Lin&action=edit&redlink=1 "Ting-Yu Lin (page does not exist)"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2021**). *Opponent Model Selection Using Deep Learning*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")


## Forum Posts


* [asymmetry](https://groups.google.com/group/rec.games.chess.computer/msg/f9bfe5d4457a19ad) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 12, 1997 » [KnightCap](KnightCap "KnightCap"), [Parity Pruning](Parity_Pruning "Parity Pruning")
* [Collector's Corner..Knowing your opponent..](https://www.stmintz.com/ccc/index.php?id=404966) by [Steve Blincoe](Steve_Blincoe "Steve Blincoe"), [CCC](CCC "CCC"), January 10, 2005
* [Opponent-modeling in computer chess](https://www.stmintz.com/ccc/index.php?id=436702) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), July 14, 2005
* [Knowing your opponents](http://www.talkchess.com/forum/viewtopic.php?t=31117) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), December 17, 2009
* [Different eval for white/black](http://www.talkchess.com/forum/viewtopic.php?t=54865) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), January 05, 2015 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation")


## External Links


* [Opponent Models in Games](http://www.ercim.eu/publication/Ercim_News/enw57/donkers.html) by [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers") and [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik")
* [Know Your Enemy (Disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Know_Your_Enemy)
* [Ignorant Hussy: Know your enemy](http://ignoranthussy.blogspot.de/2006/08/know-your-enemy.html)
* [Rage Against the Machine](https://en.wikipedia.org/wiki/Rage_Against_the_Machine) - [Know Your Enemy](https://en.wikipedia.org/wiki/Know_Your_Enemy_%28Rage_Against_the_Machine_song%29) [[13]](#cite_note-13) [[14]](#cite_note-14) [[15]](#cite_note-15) , [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) Nosce hostem, 532nd [Military Intelligence Battalion](https://en.wikipedia.org/wiki/Military_Intelligence_Corps_(United_States_Army)) [Distinctive Unit Insignia](https://en.wikipedia.org/wiki/Distinctive_unit_insignia), [United States Army](https://en.wikipedia.org/wiki/United_States_Army), [Distinctive unit insignia from Wikipedia](https://en.wikipedia.org/wiki/Distinctive_unit_insignia)
2. [↑](#cite_ref-2) [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") (**1987**). *The 7th World Microcomputer Chess Championship, Rome, Italy, September 14-20, 1987*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal") » [WMCCC 1987](WMCCC_1987 "WMCCC 1987")
3. [↑](#cite_ref-3) [Genius' asymmetric-search by example: TRY yourself](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b456400a43207b02) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 30, 1997
4. [↑](#cite_ref-4) [asymmetry](https://groups.google.com/group/rec.games.chess.computer/msg/f9bfe5d4457a19ad) by [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 12, 1997
5. [↑](#cite_ref-5) [Re: Anti Coward Mode](http://www.open-chess.org/viewtopic.php?f=5&t=2546&start=1) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 22, 2013
6. [↑](#cite_ref-6) [Peter Jansen](Peter_Jansen "Peter Jansen") (**1990**). *Problematic Positions and Speculative Play.* [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition")
7. [↑](#cite_ref-7) [Peter Jansen](Peter_Jansen "Peter Jansen") (**1992**). *Using Knowledge about the Opponent in Game-Tree Search*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), [pdf](http://www.dtic.mil/cgi-bin/GetTRDoc?AD=ADA259234&Location=U2&doc=GetTRDoc.pdf)
8. [↑](#cite_ref-8) [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1994**). *[The M\* Algorithm: Incorporating Opponent Models into Adversary Search](https://www.semanticscholar.org/paper/The-M*-Algorithm%3A-Incorporating-Opponent-Models-Carmel-Markovitch/bd788272c81951dc44fa7944e0f72451ced14129)*. CIS Report #9402, [pdf](http://www.cs.technion.ac.il/~shaulm/papers/pdf/Carmel-Markovitch-CIS9402.pdf)
9. [↑](#cite_ref-9) [David Carmel](Mathematician#DCarmel "Mathematician"), [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch") (**1996**). *Incorporating Opponent Models into Adversary Search*. [AAAI 1996](Conferences#AAAI-96 "Conferences"), [pdf](http://www.cs.technion.ac.il/~shaulm/papers/pdf/Carmel-Markovitch-aaai1996.pdf)
10. [↑](#cite_ref-10) [Xinbo Gao](Xinbo_Gao "Xinbo Gao"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1998**). *[A Speculative Strategy](http://link.springer.com/chapter/10.1007/3-540-48957-6_5)*. [CG 1998](CG_1998 "CG 1998")
11. [↑](#cite_ref-11) [Jeroen Donkers](Jeroen_Donkers "Jeroen Donkers"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2000**). *Investigating Probabilistic Opponent-Model Search*. JCIS 2000, [pdf](http://www.fdg.unimaas.nl/educ/donkers/pubs/..%5Cpdf%5Cbnaic00.pdf) (extended abstract)
12. [↑](#cite_ref-12) [Re: Different eval for white/black](http://www.talkchess.com/forum/viewtopic.php?t=54865&start=27) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), January 08, 2015
13. [↑](#cite_ref-13) [1999 Seattle WTO protests from Wikipedia](https://en.wikipedia.org/wiki/1999_Seattle_WTO_protests)
14. [↑](#cite_ref-14) [Noam Chomsky](Mathematician#Chomsky "Mathematician")
15. [↑](#cite_ref-15) [Manufacturing Consent: The Political Economy of the Mass Media - Wikipedia](https://en.wikipedia.org/wiki/Manufacturing_Consent:_The_Political_Economy_of_the_Mass_Media)

**[Up one level](Search "Search")**







 
