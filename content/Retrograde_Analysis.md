---
title: Retrograde Analysis
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* Retrograde Analysis**



 [](http://www.flickr.com/photos/smurpiknik/5149247538/in/photostream) Retrograde analysis [[1]](#cite_note-1) 
**Retrograde Analysis**,  

a method in [game theory](https://en.wikipedia.org/wiki/Game_theory) to solve [game positions](Chess_Position "Chess Position") for [optimal play](https://en.wikipedia.org/wiki/Best_response) by [backward induction](https://en.wikipedia.org/wiki/Backward_induction) from known outcomes. A sub-genre of solving certain [chess problems](https://en.wikipedia.org/wiki/Chess_problem) uses retrograde analysis to determine which [moves](Moves "Moves") were played to reach a position, and for the [proof game](https://en.wikipedia.org/wiki/Proof_game) whether a position is legal in the sense that it could be reached by a series of [legal moves](Legal_Move "Legal Move") from the [initial position](Initial_Position "Initial Position"). 




### Contents


* [1 History](#History)
* [2 Algorithm](#Algorithm)
* [3 See also](#See_also)
* [4 Selected Publications](#Selected_Publications)
	+ [4.1 1910 ...](#1910_...)
	+ [4.2 1920 ...](#1920_...)
	+ [4.3 1940 ...](#1940_...)
	+ [4.4 1960 ...](#1960_...)
	+ [4.5 1970 ...](#1970_...)
	+ [4.6 1980 ...](#1980_...)
	+ [4.7 1990 ...](#1990_...)
	+ [4.8 2000 ...](#2000_...)
	+ [4.9 2005 ...](#2005_...)
	+ [4.10 2010 ...](#2010_...)
	+ [4.11 2015 ...](#2015_...)
	+ [4.12 2020 ...](#2020_...)
* [5 Forum Posts](#Forum_Posts)
	+ [5.1 1995 ...](#1995_...)
	+ [5.2 2000 ...](#2000_..._2)
	+ [5.3 2005 ...](#2005_..._2)
	+ [5.4 2010 ...](#2010_..._2)
	+ [5.5 2015 ...](#2015_..._2)
	+ [5.6 2020 ...](#2020_..._2)
* [6 External Links](#External_Links)
	+ [6.1 Retrograde Analysis](#Retrograde_Analysis)
	+ [6.2 GitHub](#GitHub)
	+ [6.3 Programs](#Programs)
	+ [6.4 Induction](#Induction)
	+ [6.5 Retrograde](#Retrograde)
	+ [6.6 Analysis](#Analysis)
* [7 References](#References)






History based on [Lewis Stiller](Lewis_Stiller "Lewis Stiller"), *Multilinear Algebra and Chess Endgames* [[2]](#cite_note-2)




```
The mathematical justification for the retrograde analysis algorithm was already implicit in the 1912 paper of [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") [[3]](#cite_note-3). Additional theoretical work was done by [John von Neumann](John_von_Neumann "John von Neumann") and [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) [[4]](#cite_note-4). 

The contemporary [dynamic programming](Dynamic_Programming "Dynamic Programming") methodology, which defines the field of retrograde endgame analysis, was discovered by [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") in 1965 [[5]](#cite_note-5). Bellman had considered game theory from a classical perspective as well [[6]](#cite_note-6) [[7]](#cite_note-7), but his work came to fruition in his 1965 paper, where he observed that the entire [state-space](https://en.wikipedia.org/wiki/State_space_%28dynamical_system%29) could be stored and that dynamic programming techniques could then be used to compute whether either side could win any position. 

```


```
Bellman also sketched how a combination of [forward search](Search "Search"), dynamic programming, and [heuristic evaluation](Evaluation "Evaluation") could be used to solve much larger state spaces than could be tackled by either technique alone. He predicted that [Checkers](Checkers "Checkers") could be solved by his techniques, and the utility of his algorithms for solving very large state spaces has been validated by [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") et al. in the domain of Checkers [[8]](#cite_note-8), [Ralph Gasser](Ralph_Gasser "Ralph Gasser") in the domain of [Nine Men’s Morris](Nine_Men%E2%80%99s_Morris "Nine Men’s Morris") [[9]](#cite_note-9), and [John Romein](John_Romein "John Romein") with [Henri Bal](Henri_Bal "Henri Bal") in the domain of [Awari](Awari "Awari") [[10]](#cite_note-10). The first retrograde analysis implementation was due to [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein"), whose important 1970 dissertation described the solution of several pawnless 4-piece endgames [[11]](#cite_note-11).

```





## Algorithm


Retrograde analysis is the basic [algorithm](Algorithms "Algorithms") to construct [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"). A [bijective function](https://en.wikipedia.org/wiki/Bijection) is used to map [chess positions](Chess_Position "Chess Position") to [Gödel numbers](https://en.wikipedia.org/wiki/G%C3%B6del_numbering) which index a database of bitmaps during construction and retrieval, in its simplest form based on a multi-dimensional [array](Array "Array") index. Following description is based on [Ken Thompson's](Ken_Thompson "Ken Thompson") paper *Retrograde Analysis of Certain Endgames* with [depth to mate (DTM)](Endgame_Tablebases#DTM "Endgame Tablebases") metric [[12]](#cite_note-12), and assumes White the winning side. Files of sets of chess positions, where a one-bit is associated with the Gödel number of a position, are successively manipulated during the [iterative](Iteration "Iteration") generation process:



* Bi set of the latest newly found Black-to-move and lose in i moves positions
* Wi set of the latest newly found White-to-move and win in i moves positions
* B set of all currently known Black-to-move and lose positions, union of all Bi so far
* W set of all currently known White-to-move and win positions, union of all Wi so far
* Ji is temporary superset of Bi not necessarily lose positions


The algorithm starts in enumerating all Black-to-move [checkmate](Checkmate "Checkmate") positions B0 with the material configuration under consideration, an [un-move generator](Move_Generation#Reverse "Move Generation") is used to to build predecessor or parent positions. The un-move generation is similar to [move generation](Move_Generation "Move Generation"), with the difference that it is illegal to start in [check](Check "Check"), but legal to un-move into check, and illegal to capture, but legal to un-capture by leaving an opponent piece behind.


**for** (i=0; Bi; i++)



1. Every parent of a Bi position is a White-to-move won position - newly-won positions Wi+1 are parents of a Bi not (yet) in W
2. Wi+1 becomes subset of W
3. Every parent of a Wi+1 position is a Black-to-move and lose position if Black wanted to mate himself, stored in Ji+1
4. Only if all successors (by generating and making legal moves [[13]](#cite_note-13)) of a Ji+1 position are member of W, the Ji+1 position becomes member of Bi+1 and B


The algorithm terminates, if no more newly predecessor positions were found, that is either Wi+1 or Bi+1 stay empty. Each one-bit in W or B correspondents to a White-to-move and won or Black-to-move and lose position. Remaining zero bits indicate either a [draw](Draw "Draw"), White-to-move and lose, Black-to-move and won, or illegal positions.



## See also


* [Chess Position](Chess_Position "Chess Position")
* [Chess Problems, Compositions and Studies](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies")
* [Chess Problem Solving Engines](Category:Problem "Category:Problem")
* [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
* [Dynamic Programming](Dynamic_Programming "Dynamic Programming")
* [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases")
* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
* [Oracle](Oracle "Oracle")
* [Transposition | Retrograde Analysis](Transposition#RetrogradeAnalysis "Transposition")


## Selected Publications


### 1910 ...


* [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") (**1913**). *Über eine Anwendung der Mengenlehre auf die Theorie des Schachspiels* Proc. Fifth Congress Mathematicians, (Cambridge 1912), Cambridge Univ. Press 1913, 501–504. Translation: *On an Application of Set Theory to the Theory of the Game of Chess*.


### 1920 ...


* [Dénes Kőnig](Mathematician#DenesKoenig "Mathematician") (**1927**). *[Über eine Schlussweise aus dem Endlichen ins Unendliche](http://acta.fyx.hu/acta/showCustomerArticle.action?id=5131&dataObjectType=article&returnAction=showCustomerVolume&sessionDataSetId=2b29ea26fa2c9ba)*. [Acta Scientiarum Mathematicarum](http://acta.fyx.hu/acta/home.action?noDataSet=true) ([University of Szeged](https://en.wikipedia.org/wiki/University_of_Szeged))


### 1940 ...


* [John von Neumann](John_von_Neumann "John von Neumann"), [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) (**1944**). *Theory of Games and Economic Behavior*. Princeton University Press, Princeton, NJ


### 1960 ...


* [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1965**). *[On the Application of Dynamic Programming to the Determination of Optimal Play in Chess and Checkers](http://www.rand.org/pubs/papers/P3013/).* [PNAS](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America)
* [Vladimir E. Alekseev](index.php?title=Vladimir_E._Alekseev&action=edit&redlink=1 "Vladimir E. Alekseev (page does not exist)") (**1969**). *[Compilation of Chess Problems on a Computer](http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=html&identifier=AD0689470)*. Technical translation FSTC-HT-23-124-69, US Army, NTIS AD 689470 ([Problemy Kibernetiki](http://www.worldcat.org/title/problemy-kibernetiki/oclc/1762911), 19, 1967)


### 1970 ...


* [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein") (**1970**). *Untersuchungen über kombinatorische Spiele.* Ph.D. Thesis, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)
* [Edward Komissarchik](Edward_Komissarchik "Edward Komissarchik"), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1974**). *Ob Analize Ferzevogo Endshpilya pri Pomoshchi EVM.* (Analysis of a queen endgame using an IBM computer) Problemy Kybernetiki, Vol. 29, pp. 211-220. English translation by [Christian Posthoff](Christian_Posthoff "Christian Posthoff"), revised in [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal") (**1986**)
* [A. G. Alexandrov](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=55935), [A. M. Baraev](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=96113), [Ya. Yu. Gol'fand](http://www.mathnet.ru/php/person.phtml?option_lang=eng&personid=96114), [Edward Komissarchik](Edward_Komissarchik "Edward Komissarchik"), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1977**). *[Computer analysis of rook end game](http://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=at&paperid=7425&option_lang=eng)*. [Avtomatika i Telemekhanika](https://en.wikipedia.org/wiki/Automation_and_Remote_Control), No. 8, 113–117
* [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein"), [Ludwig Zagler](Ludwig_Zagler "Ludwig Zagler") (**1977**). *[Analyzing games by Boolean matrix iteration](http://www.sciencedirect.com/science/article/pii/0012365X77900334)*. [Discrete Mathematics](https://en.wikipedia.org/wiki/Discrete_Mathematics_%28journal%29), Vol. 19, No. 2
* [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein"), [Ludwig Zagler](Ludwig_Zagler "Ludwig Zagler") (**1978**). *Ergebnisse einer vollstandigen Analyse von Schachendspielen: König und Turm gegen König, König und Turm gegen König und Läufer.* Report, Institut für Informatik, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)
* [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1978**). *[Programming endgames with few pieces](https://zbmath.org/?q=an:03637634)*. [Soviet Physics. Doklady](https://en.wikipedia.org/wiki/Doklady_Physics), No. 23
* [Vladimir Arlazarov](Vladimir_Arlazarov "Vladimir Arlazarov"), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1979**). *Computer Analysis of a Rook End-Game*. [Machine Intelligence 9](http://www.doc.ic.ac.uk/~shm/MI/mi9.html) (eds. [Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie") and L.I. Mikulich), pp. 361-371. Ellis Horwood, Chichester. Reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Raymond Smullyan](Raymond_Smullyan "Raymond Smullyan") (**1979**). *[The Chess Mysteries of Sherlock Holmes](http://www.amazon.com/Chess-Mysteries-Sherlock-Holmes/dp/0394737571)*. [Alfred A. Knopf](https://en.wikipedia.org/wiki/Alfred_A._Knopf), New York [[14]](#cite_note-14)


### 1980 ...


* [Raymond Smullyan](Raymond_Smullyan "Raymond Smullyan") (**1981**). *[The Chess Mysteries of the Arabian Knights](http://www.chesslund.com/detail.asp?id=2206&n=Smullyan-The-Chess-Mysteries-of-the-Arabian-Knights)* . [Alfred A. Knopf](https://en.wikipedia.org/wiki/Alfred_A._Knopf), New York [[15]](#cite_note-15)
* [Max Bramer](Max_Bramer "Max Bramer"), [B. E. P. Alden](http://www.informatik.uni-trier.de/~ley/pers/hy/a/Alden:B=_E=_P=.html) (**1982**). *A Program for Solving Retrograde Analysis Chess Problems.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3") [[16]](#cite_note-16)
* [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Retrograde Analysis of Certain Endgames*. [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal"), [pdf](http://pdos.csail.mit.edu/~rsc/thompson86endgame.pdf)
* [Edward Komissarchik](Edward_Komissarchik "Edward Komissarchik"), [Aaron L. Futer](Aaron_L._Futer "Aaron L. Futer") (**1986**). *Computer Analysis of a Queen Endgame*. [ICCA Journal, Vol. 9, No. 4](ICGA_Journal#9_4 "ICGA Journal")
* [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1988**). *Massively Parallel Retrograde Endgame Analysis*. BUCS Tech. Report #88-014, Boston University, Computer Science Department.
* [B. E. P. Alden](http://www.informatik.uni-trier.de/~ley/pers/hy/a/Alden:B=_E=_P=.html), [Max Bramer](Max_Bramer "Max Bramer") (**1988**). *An Expert System for Solving Retrograde-Analysis Chess Problems.* [International Journal of Man-Machine Studies, Vol. 29, No. 2](http://www.interaction-design.org/references/periodicals/international_journal_of_man-machine_studies_volume_29.html)
* [Michael Schlosser](Michael_Schlosser "Michael Schlosser") (**1988**). *Computers and Chess-Problem Composition.* [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal")
* [David Forthoffer](David_Forthoffer "David Forthoffer"), [Lars Rasmussen](Lars_Rasmussen "Lars Rasmussen"), [Sito Dekker](Sito_Dekker "Sito Dekker") (**1989**). *A Correction to some KRKB-Database Results*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**1989**). *Retrograde Analysis and two Computerizable Definitions of the Quality of Chess Games.* [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal")


### 1990 ...


* [László Lindner](L%C3%A1szl%C3%B3_Lindner "László Lindner"), [Michael Schlosser](Michael_Schlosser "Michael Schlosser") (**1991**). *New Ideas in Problem Solving and Composing Programs*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
* [Michael Schlosser](Michael_Schlosser "Michael Schlosser") (**1991**). *Can a Computer Compose Chess Problems?* [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6")
* [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1991**). *Some Results from a Massively Parallel Retrograde Analysis.* [ICCA Journal, Vol. 14, No. 3](ICGA_Journal#14_3 "ICGA Journal")
* [Ralph Gasser](Ralph_Gasser "Ralph Gasser") (**1991**). *Applying Retrograde Analysis to Nine Men’s Morris.* [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
* [Robert Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Paul Lu](Paul_Lu "Paul Lu") (**1993**). *Solving Large Retrograde Analysis Problems Using a Network of Workstations*. Technical Report, TR93-13, [ps](ftp://ftp.cs.ualberta.ca/pub/TechReports/1993/TR93-13/)
* [Robert Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Paul Lu](Paul_Lu "Paul Lu") (**1994**). *Solving Large Retrograde Analysis Problems Using a Network of Workstations*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Henri Bal](Henri_Bal "Henri Bal"), [Victor Allis](Victor_Allis "Victor Allis") (**1995**). *Parallel Retrograde Analysis on a Distributed System*. Supercomputing ’95, San Diego, CA.
* [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1996**). *Multilinear Algebra and Chess Endgames*. [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski"), [pdf](http://www.msri.org/publications/books/Book29/files/stiller.pdf)
* [Dietmar Lippold](index.php?title=Dietmar_Lippold&action=edit&redlink=1 "Dietmar Lippold (page does not exist)") (**1996**). *Legality of Positions of Simple Chess Endgames*. [zipped pdf](http://digilander.libero.it/gargamellachess/papers/legality%20of%20positions.zip) [[17]](#cite_note-17)
* [Dietmar Lippold](index.php?title=Dietmar_Lippold&action=edit&redlink=1 "Dietmar Lippold (page does not exist)") (**1997**). *The Legitimacy of Positions in Endgame Databases*. [ICCA Journal, Vol. 20, No. 1](ICGA_Journal#20_1 "ICGA Journal")
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Jin Yoshimura](Jin_Yoshimura "Jin Yoshimura"), [Kazuro Morita](index.php?title=Kazuro_Morita&action=edit&redlink=1 "Kazuro Morita (page does not exist)"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1998**). *[Retrograde Analysis of the KGK Endgame in Shogi: Its Implications for Ancient Heian Shogi](http://www.springerlink.com/content/pg7at646416va0re/)*. [CG 1998](CG_1998 "CG 1998")
* [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [Jürg Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt") (**1999**). *Exhaustive and Heuristic Retrograde Analysis of the KPPKP Endgame.* [ICCA Journal, Vol. 22, No. 2](ICGA_Journal#22_2 "ICGA Journal")


### 2000 ...


* [Roel van der Goot](index.php?title=Roel_van_der_Goot&action=edit&redlink=1 "Roel van der Goot (page does not exist)") (**2000**). *[Awari Retrograde Analysis](http://link.springer.com/chapter/10.1007/3-540-45579-5_6)*. [CG 2000](CG_2000 "CG 2000")
* [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2000**). *[Construction of Chinese Chess Endgame Databases by Retrograde Analysis](http://link.springer.com/chapter/10.1007/3-540-45579-5_7)*. [CG 2000](CG_2000 "CG 2000")
* [Bruno Bouzy](Bruno_Bouzy "Bruno Bouzy") (**2001**). *Go Patterns Generated by Retrograde Analysis*. [6th Computer Olympiad Workshop](6th_Computer_Olympiad#Workshop "6th Computer Olympiad"), [pdf](http://www.mi.parisdescartes.fr/~bouzy/publications/RAGO.pdf)
* [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**2001**). *Retrograde Analysis: Software Architecture*. [ICGA Journal, Vol. 24, No. 2](ICGA_Journal#24_2 "ICGA Journal")
* [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2001**). *[Fast, Memory-efficient Retrograde Algorithms](http://ilk.uvt.nl/icga/journal/contents/content24-3.htm#FAST)*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal") [[18]](#cite_note-18) [[19]](#cite_note-19)
* [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2001**). *Parallel Retrograde Analysis on Different Architectures*. IEEE 10th Conference in High Performance Distributed Computing pp. 356-362, August 2001
* [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu"), [Shun-Chin Hsu](Shun-Chin_Hsu "Shun-Chin Hsu") (**2001**). *Construction of Chinese Chess Endgame Databases by Retrograde Analysis*. Lecture Notes in Computer Science 2063: [CG 2000](CG_2000 "CG 2000")
* [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2002**). *A memory efficient retrograde algorithm and its application to solve Chinese Chess endgames.* [More Games of No Chance](http://library.msri.org/books/Book42/) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski")
* [Thomas Lincke](Thomas_Lincke "Thomas Lincke") (**2002**). *Exploring the Computational Limits of Large Exhaustive Search Problems*. Ph.D thesis, [ETH Zurich](ETH_Zurich "ETH Zurich"), [pdf](http://e-collection.library.ethz.ch/eserv/eth:25905/eth-25905-02.pdf)
* [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal") (**2003**). *Solving the Game of Awari using Parallel Retrograde Analysis*. IEEE Computer, Vol. 36, No. 10, pp. 26–33
* [Ping-hsun Wu](index.php?title=Ping-hsun_Wu&action=edit&redlink=1 "Ping-hsun Wu (page does not exist)"), [Ping-Yi Liu](index.php?title=Ping-Yi_Liu&action=edit&redlink=1 "Ping-Yi Liu (page does not exist)"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2004**). *[An External-Memory Retrograde Analysis Algorithm](http://link.springer.com/chapter/10.1007/11674399_10)*. [CG 2004](CG_2004 "CG 2004")


### 2005 ...


* [Jesper Torp Kristensen](Jesper_Torp_Kristensen "Jesper Torp Kristensen") (**2005**). *[Generation and compression of endgame tables in chess with fast random access using OBDDs](https://issuu.com/jespertk/docs/master_thesis)*. Master thesis, supervisor [Peter Bro Miltersen](Mathematician#Miltersen "Mathematician"), [Aarhus University](https://en.wikipedia.org/wiki/Aarhus_University)
* [James Glenn](James_Glenn "James Glenn"), [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal") (**2006**). *[A Retrograde Approximation Algorithm for One-Player Can’t Stop](https://link.springer.com/chapter/10.1007/978-3-540-75538-8_13)*. [CG 2006](CG_2006 "CG 2006")
* [James Glenn](James_Glenn "James Glenn"), [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal") (**2007**). *A Retrograde Approximation Algorithm for Two-Player Can't Stop*. [CGW 2007](CGW_2007 "CGW 2007"), [pdf](http://www.cs.loyola.edu/~jglenn/Papers/cantstop2.pdf)
* [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [James Glenn](James_Glenn "James Glenn"), [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal") (**2008**). *Retrograde approximation algorithms for Jeopardy stochastic games*. [ICGA Journal, Vol. 31, No. 2](ICGA_Journal#31_2 "ICGA Journal")
* [James Glenn](James_Glenn "James Glenn"), [Haw-ren Fang](Haw-ren_Fang "Haw-ren Fang"), [Clyde Kruskal](Clyde_Kruskal "Clyde Kruskal") (**2008**). *[A Retrograde Approximation Algorithm for Multi-player Can’t Stop](https://link.springer.com/chapter/10.1007/978-3-540-87608-3_23)*. [CG 2008](CG_2008 "CG 2008")
* [Noam D. Elkies](Noam_Elkies "Noam Elkies"), [Richard P. Stanley](Mathematician#RPStanley "Mathematician") (**2008**). *Chess and Mathematics*. excerpt, 6 Retrograde Analysis, [pdf](http://www-math.mit.edu/%7Erstan/chess/spg.pdf)
* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)") (**2008**). *Developing Heuristics for Solving Retrograde Chess Problems*. [Seminar on Formal Methods and Applications](http://seminar.foi.hr/), [Varaždin](https://en.wikipedia.org/wiki/Vara%C5%BEdin), [Croatia](https://en.wikipedia.org/wiki/Croatia)
* [Dan Heisman](Dan_Heisman "Dan Heisman") (**2009**). *Steinitz, Zermelo, and Elkies*. [pdf](http://www.chesscafe.com/text/skittles358.pdf) from [ChessCafe.com](https://en.wikipedia.org/wiki/ChessCafe.com), on [Wilhelm Steinitz](https://en.wikipedia.org/wiki/Wilhelm_Steinitz), [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") and [Noam Elkies](Noam_Elkies "Noam Elkies")


### 2010 ...


* [Victor Zakharov](Victor_Zakharov "Victor Zakharov"), [Vladimir Makhnychev](Vladimir_Makhnychev "Vladimir Makhnychev") (**2010**). *A Retroanalysis Algorithm for Supercomputer Systems on the Example of Playing Chess*. Software Systems and Tools, Vol. 11 (Russian)
* [Ping-hsun Wu](index.php?title=Ping-hsun_Wu&action=edit&redlink=1 "Ping-hsun Wu (page does not exist)"), [Ping-yi Liu](index.php?title=Ping-yi_Liu&action=edit&redlink=1 "Ping-yi Liu (page does not exist)"), [Tsan-sheng Hsu](Tsan-sheng_Hsu "Tsan-sheng Hsu") (**2010**). *An External-memory Retrograde Analysis Algorithm*. slides as [pdf](http://www.iis.sinica.edu.tw/~tshsu/tcg2010/slides/slide12.pdf)
* [Paolo Ciancarini](Paolo_Ciancarini "Paolo Ciancarini"), [Gian Piero Favini](index.php?title=Gian_Piero_Favini&action=edit&redlink=1 "Gian Piero Favini (page does not exist)") (**2010**). *Retrograde analysis of Kriegspiel endgames*. IEEE Conf. on Computational Intelligence and Games, Copenhagen.
* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)"), [Mirko Čubrilo](index.php?title=Mirko_%C4%8Cubrilo&action=edit&redlink=1 "Mirko Čubrilo (page does not exist)") (**2010**). *[What Were the Last Moves?](http://bib.irb.hr/prikazi-rad?&rad=445958)* International Review on Computers and Software
* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)"), [Mirko Čubrilo](index.php?title=Mirko_%C4%8Cubrilo&action=edit&redlink=1 "Mirko Čubrilo (page does not exist)") (**2010**). *Solving Shortest Proof Games by Generating Trajectories using Coq Proof Management System*. Proceedings of 21st Central European Conference on Information and Intelligent Systems, [Varaždin](https://en.wikipedia.org/wiki/Vara%C5%BEdin), [Croatia](https://en.wikipedia.org/wiki/Croatia) [[20]](#cite_note-20)
* [Marko Maliković](index.php?title=Marko_Malikovi%C4%87&action=edit&redlink=1 "Marko Maliković (page does not exist)") (**2011**). *Automated Reasoning about Retrograde Chess Problems using Coq*. [Fourth Workshop on Formal and Automated Theorem Proving and Applications](http://argo.matf.bg.ac.rs/events/2011/fatpa2011/fatpa2011.html), [Belgrade](https://en.wikipedia.org/wiki/Belgrade), [Serbia](https://en.wikipedia.org/wiki/Serbia), [slides as pdf](http://argo.matf.bg.ac.rs/events/2011/fatpa2011/slides/MarkoMalikovic.pdf)
* [Jan van Rijn](Jan_van_Rijn "Jan van Rijn"), [Jonathan K. Vis](index.php?title=Jonathan_K._Vis&action=edit&redlink=1 "Jonathan K. Vis (page does not exist)") (**2013**). *Complexity and Retrograde Analysis of the Game Dou Shou Qi*. [BNAIC 2013](http://bnaic2013.tudelft.nl/) [[21]](#cite_note-21)
* [Jan van Rijn](Jan_van_Rijn "Jan van Rijn"), [Jonathan K. Vis](index.php?title=Jonathan_K._Vis&action=edit&redlink=1 "Jonathan K. Vis (page does not exist)") (**2014**). *Endgame Analysis of Dou Shou Qi*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal"), [pdf](http://www.liacs.nl/~jvrijn/pdf/pub/icga2014a.pdf)


### 2015 ...


* [Michael Hartisch](index.php?title=Michael_Hartisch&action=edit&redlink=1 "Michael Hartisch (page does not exist)") (**2015**). *Impact of Rounding during Retrograde Analysis for a Game with Chance Nodes: Karl’s Race as a Test Case*. [ICGA Journal, Vol. 38, No. 2](ICGA_Journal#38_2 "ICGA Journal") » [Games](Games "Games"), [EinStein würfelt nicht!](EinStein_w%C3%BCrfelt_nicht! "EinStein würfelt nicht!") [[22]](#cite_note-22)
* [Michael Hartisch](index.php?title=Michael_Hartisch&action=edit&redlink=1 "Michael Hartisch (page does not exist)"), [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2015**). *Optimal Robot Play in Certain Chess Endgame Situations*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")


### 2020 ...


* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2020**). *CEN: Thomas Ströhlein’s Endgame Tables, a 50th Anniversary*. [ICGA Journal, Vol. 42, Nos. 2-3](ICGA_Journal#42_23 "ICGA Journal")


## Forum Posts


### 1995 ...


* [retrograde analysis](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/b42e13fffe70a74e) by Stefan Schroedl, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 15, 1995


### 2000 ...


* [reverse engineering](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c2509d7520be9ba7) by NoKetch, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 16, 2000
* [EGTB: Better algorithm](https://www.stmintz.com/ccc/index.php?id=162252) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [CCC](CCC "CCC"), April 07, 2001 [[23]](#cite_note-23)
* [Re: How endgame tablebases work](http://groups.google.com/group/rec.games.chess.computer/msg/392bcd5797808c0e) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 19, 2001
* [Generating egtbs ICGAJ](https://www.stmintz.com/ccc/index.php?id=200335) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), December 04, 2001 [[24]](#cite_note-24) [[25]](#cite_note-25)


 [Wu/Beal predates Koistinen](https://www.stmintz.com/ccc/index.php?id=200376) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), December 04, 2001
* [Question about retrograde analysis algorithm for endgame databases](http://groups.google.com/group/rec.games.abstract/browse_frm/thread/48cca090ce094620) by mathpolymath, [rec.games.abstract](Computer_Chess_Forums "Computer Chess Forums"), April 24, 2002 [[26]](#cite_note-26)


### 2005 ...


* [Wu / Beal retrograde analisys algorithm](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6302&p=29956) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 10, 2007
* [Could this program be written?](http://www.talkchess.com/forum/viewtopic.php?t=23214) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2008
* [Retrograde analysis](http://www.talkchess.com/forum/viewtopic.php?t=24713) by Geolm, [CCC](CCC "CCC"), November 04, 2008


### 2010 ...


* [Retrograde tablebase methods](http://www.open-chess.org/viewtopic.php?f=5&t=779) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 26, 2010
* [Reverse move generation](http://www.talkchess.com/forum/viewtopic.php?t=54796) by Kostas Oreopoulos, [CCC](CCC "CCC"), December 30, 2014 » [Un-Move Generation](Move_Generation#Reverse "Move Generation")


 [Re: Reverse move generation](http://www.talkchess.com/forum/viewtopic.php?t=54796&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 30, 2014
### 2015 ...


* [Position Legally Reachable?](http://www.talkchess.com/forum/viewtopic.php?t=63515) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), March 21, 2017


### 2020 ...


* [Retrograde analysis - TBs move sequences to checkmate](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73332) by Hedinn Steingrimsson, [CCC](CCC "CCC"), March 12, 2020
* [On the number of chess positions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685) by [John Tromp](John_Tromp "John Tromp"), [CCC](CCC "CCC"), July 09, 2021


 [Re: On the number of chess positions](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685&start=34) by [John Tromp](John_Tromp "John Tromp"), [CCC](CCC "CCC"), April 02, 2022
 [Re: On the number of chess positions](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685&start=42) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 03, 2022 » [Chess Position](Chess_Position "Chess Position")
* [Fast reverse move generation](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78913) by koedem, [CCC](CCC "CCC"), December 18, 2021 » [Un-Move Generation](Move_Generation#Reverse "Move Generation")


## External Links


### Retrograde Analysis


* [Retrograde analysis from Wikipedia](https://en.wikipedia.org/wiki/Retrograde_analysis)
* [Leapfrog: Retrograde Analysis](https://home.hccnet.nl/h.g.muller/EGT7/retro.html) from [Leapfrog tablebase generator](http://home.hccnet.nl/h.g.muller/EGT7/7-men.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
* [Computing endgames with few men](https://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen") [[27]](#cite_note-27) [[28]](#cite_note-28) [[29]](#cite_note-29)
* [The Retrograde Analysis Corner](http://www.janko.at/Retros/index.htm)
* [Jewish Chess History: Prime Ministers and Retrograde Analysis](http://jewishchesshistory.blogspot.de/2008/01/prime-ministers-and-retrograde-analysis.html)
* [Non-Chess Retrograde Analysis](http://joekisenwether.wordpress.com/non-chess-retrograde-analysis/) « [Joe Kisenwether's Blog](http://joekisenwether.wordpress.com/)
* [Build Your Own Chess Endgame Monster - Level Up Coding](https://levelup.gitconnected.com/build-your-own-chess-endgame-monster-a3fb23bb3ec1) by [Don Cross](Don_Cross "Don Cross"), February 17, 2020


### GitHub


* [GitHub - tromp/ChessPositionRanking: Software suite for ranking chess positions and accurately estimating the number of legal chess positions](https://github.com/tromp/ChessPositionRanking) by [John Tromp](John_Tromp "John Tromp")


### Programs


* [Euclide 1.11 - Home](http://lestourtereaux.free.fr/euclide/) by [Étienne Dupuis](index.php?title=%C3%89tienne_Dupuis&action=edit&redlink=1 "Étienne Dupuis (page does not exist)") » [Euclide](index.php?title=Euclide&action=edit&redlink=1 "Euclide (page does not exist)")
* [Freezerchess.com - Endgame Analysis beyond Databases](https://www.freezerchess.com/) by [Eiko Bleicher](Eiko_Bleicher "Eiko Bleicher") » [Freezer](Freezer "Freezer")
* [Natch - Checking proof games](http://natch.free.fr/Natch.html) by [Pascal Wassong](index.php?title=Pascal_Wassong&action=edit&redlink=1 "Pascal Wassong (page does not exist)") » [Natch](index.php?title=Natch&action=edit&redlink=1 "Natch (page does not exist)")
* [Retractor](http://xenon.stanford.edu/~hwatheod/Retractor/) a program for Retrograde Analysis chess problems by [Chad Whipkey](index.php?title=Chad_Whipkey&action=edit&redlink=1 "Chad Whipkey (page does not exist)") and [Theodore Hwa](index.php?title=Theodore_Hwa&action=edit&redlink=1 "Theodore Hwa (page does not exist)") » [Retractor](index.php?title=Retractor&action=edit&redlink=1 "Retractor (page does not exist)")


### Induction


* [Inductive reasoning from Wikipedia](https://en.wikipedia.org/wiki/Inductive_reasoning)
* [Backward induction from Wikipedia](https://en.wikipedia.org/wiki/Backward_induction)
* [Backward chaining from Wikipedia](https://en.wikipedia.org/wiki/Backward_chaining)


### Retrograde


* [Retrograde (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Retrograde)
* [Retrograde motion from Wikipedia](https://en.wikipedia.org/wiki/Retrograde_motion)


 [Apparent retrograde motion from Wikipedia](https://en.wikipedia.org/wiki/Apparent_retrograde_motion)
* [Retrograde (music) from Wikipedia](https://en.wikipedia.org/wiki/Retrograde_%28music%29)
* [Darryl Reeves](https://www.allaboutjazz.com/musicians/darryl-reeves) - The Mercury Sessions - Retrograde, July 22, 2011 - Churchill Grounds - [Atlanta, GA](https://en.wikipedia.org/wiki/Atlanta), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 Darryl Reeves, Kenny Banks, Joel Powell, Kenton "Boom" Bostick
 
### Analysis


* [Analysis from Wikipedia](https://en.wikipedia.org/wiki/Analysis)
* [Analysis (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Analysis_%28disambiguation%29)


## References


1. [↑](#cite_ref-1) [Ретроградный анализ. / Retrograde analysis](http://www.flickr.com/photos/smurpiknik/5149247538/in/photostream), [Flickr: Fotostream by Segaboy](http://www.flickr.com/photos/smurpiknik/with/5149247538/#photo_5149247538)
2. [↑](#cite_ref-2) [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1996**). *Multilinear Algebra and Chess Endgames*. [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski"), [pdf](http://www.msri.org/publications/books/Book29/files/stiller.pdf)
3. [↑](#cite_ref-3) [Ernst Zermelo](Ernst_Zermelo "Ernst Zermelo") (**1913**). *Über eine Anwendung der Mengenlehre auf die Theorie des Schachspiels* Proc. Fifth Congress Mathematicians, (Cambridge 1912), Cambridge Univ. Press 1913, 501–504. Translation: *On an Application of Set Theory to the Theory of the Game of Chess*
4. [↑](#cite_ref-4) [John von Neumann](John_von_Neumann "John von Neumann") and [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern) (**1944**). *Theory of Games and Economic Behavior*. Princeton University Press, Princeton, NJ
5. [↑](#cite_ref-5) [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1965**). *[On the Application of Dynamic Programming to the Determination of Optimal Play in Chess and Checkers](http://www.rand.org/pubs/papers/P3013/).* [PNAS](https://en.wikipedia.org/wiki/Proceedings_of_the_National_Academy_of_Sciences_of_the_United_States_of_America)
6. [↑](#cite_ref-6) [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1954**). *On a new Iterative Algorithm for Finding the Solutions of Games and Linear Programming Problems*. Technical Report P-473, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), [Santa Monica, CA](https://en.wikipedia.org/wiki/Santa_Monica,_California)
7. [↑](#cite_ref-7) [Richard E. Bellman](Richard_E._Bellman "Richard E. Bellman") (**1957**). *The Theory of Games*. Technical Report P-1062, [RAND Corporation](https://en.wikipedia.org/wiki/RAND_Corporation), [Santa Monica, CA](https://en.wikipedia.org/wiki/Santa_Monica,_California)
8. [↑](#cite_ref-8) [Robert Lake](index.php?title=Rob_Lake&action=edit&redlink=1 "Rob Lake (page does not exist)"), [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer"), [Paul Lu](Paul_Lu "Paul Lu") (**1994**). *Solving Large Retrograde Analysis Problems Using a Network of Workstations*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
9. [↑](#cite_ref-9) [Ralph Gasser](Ralph_Gasser "Ralph Gasser") (**1991**). *Applying Retrograde Analysis to Nine Men’s Morris.* [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
10. [↑](#cite_ref-10) [John Romein](John_Romein "John Romein"), [Henri Bal](Henri_Bal "Henri Bal") (**2003**). *Solving the Game of Awari using Parallel Retrograde Analysis*. IEEE Computer, Vol. 36, No. 10
11. [↑](#cite_ref-11) [Thomas Ströhlein](Thomas_Str%C3%B6hlein "Thomas Ströhlein") (**1970**). *Untersuchungen über kombinatorische Spiele.* Ph.D. Thesis, [Technical University of Munich](Technical_University_of_Munich "Technical University of Munich") (German)
12. [↑](#cite_ref-12) [Ken Thompson](Ken_Thompson "Ken Thompson") (**1986**). *Retrograde Analysis of Certain Endgames*. [ICCA Journal, Vol. 9, No. 3](ICGA_Journal#9_3 "ICGA Journal")
13. [↑](#cite_ref-13) dubbed "grandfather" method, [Retrograde tablebase methods](http://www.open-chess.org/viewtopic.php?f=5&t=779) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 26, 2010
14. [↑](#cite_ref-14) [Smullyan Problem in Sherlock Holmes book](https://groups.google.com/d/msg/rec.games.chess.computer/MyFmpXxqccg/Z6WgNuoF-hcJ) by Christopher Heckman, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 18, 2013
15. [↑](#cite_ref-15) [Retrospektive (Retroanalyse)](http://de.wikipedia.org/wiki/Schachkomposition#Retrospektive_.28Retroanalyse.29) from German Wikipedia, [Raymond Smullyan](Mathematician#Smullyan "Mathematician"), [Manchester Guardian](https://en.wikipedia.org/wiki/The_Guardian), 1957
16. [↑](#cite_ref-16) [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**1981**). *Progress in Computer Chess.* [AISB Quarterly](http://www.aisb.org.uk/aisbq/qarchive.shtml), reprinted in [ICCA Newsletter, Vol. 4. No. 3](ICGA_Journal#4_3 "ICGA Journal"), [pdf](http://arno.uvt.nl/show.cgi?fid=106747)
17. [↑](#cite_ref-17) referred in [Jesper Torp Kristensen](Jesper_Torp_Kristensen "Jesper Torp Kristensen") (**2005**). *[Generation and compression of endgame tables in chess with fast random access using OBDDs](https://issuu.com/jespertk/docs/master_thesis)*. Master thesis, supervisor [Peter Bro Miltersen](Mathematician#Miltersen "Mathematician"), [Aarhus University](https://en.wikipedia.org/wiki/Aarhus_University)
18. [↑](#cite_ref-18) [Generating egtbs ICGAJ](https://www.stmintz.com/ccc/index.php?id=200335) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), December 04, 2001, with reference to [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen")
19. [↑](#cite_ref-19) [Wu / Beal retrograde analisys algorithm](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6302&p=29956) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 10, 2007
20. [↑](#cite_ref-20) [Coq from Wikipedia](https://en.wikipedia.org/wiki/Coq)
21. [↑](#cite_ref-21) [Jungle (board game) from Wikipedia](https://en.wikipedia.org/wiki/Jungle_%28board_game%29)
22. [↑](#cite_ref-22) [Karl's Race](http://www.althofer.de/karls-race.html) A Game on [Karl Scherer's](index.php?title=Karl_Scherer&action=edit&redlink=1 "Karl Scherer (page does not exist)") Alternating Tiling by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), 2006
23. [↑](#cite_ref-23) [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen")
24. [↑](#cite_ref-24) [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2001**). *Fast, Memory-efficient Retrograde Algorithms*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal")
25. [↑](#cite_ref-25) [Computing endgames with few men](http://www.abc.se/~m10051/eg.txt) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen")
26. [↑](#cite_ref-26) [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2001**). *Fast, Memory-efficient Retrograde Algorithms*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal")
27. [↑](#cite_ref-27)  [EGTB: Better algorithm](https://www.stmintz.com/ccc/index.php?id=162252) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [CCC](CCC "CCC"), April 07, 2001
28. [↑](#cite_ref-28) [Generating egtbs ICGAJ](https://www.stmintz.com/ccc/index.php?id=200335) by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), December 04, 2001
29. [↑](#cite_ref-29) [Ren Wu](Ren_Wu "Ren Wu"), [Don Beal](Don_Beal "Don Beal") (**2001**). *Fast, Memory-efficient Retrograde Algorithms*. [ICGA Journal, Vol. 24, No. 3](ICGA_Journal#24_3 "ICGA Journal")

**[Up one Level](Knowledge "Knowledge")**







 
