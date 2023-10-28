---
title: Endgame
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * [Game Phases](Game_Phases "Game Phases") * Endgame**

[](https://www.dorotheatanning.org/life-and-work/view/229/) [Dorothea Tanning](Category:Dorothea_Tanning "Category:Dorothea Tanning") - End Game, 1944 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
In the **Endgame** chess programs usually have quite a lot of difficulties. Even the most simple endgames often just lead to a mate after 10 to 15 plys or more, which is far beyond the horizon for engines without the specific endgame knowledge. There are some concepts that a chess programmer should implement to overcome the most basic problems. Usually chess engines activate this special Endgame knowledge as soon as the material on board reaches a certain lower-bound.

## Contents

- [1 Transposition Tables](#transposition-tables)
- [2 Evaluation](#evaluation)
- [3 Special Knowledge](#special-knowledge)
  - [3.1 King and Pawns](#king-and-pawns)
  - [3.2 Pieces](#pieces)
  - [3.3 Endgame Tablebases](#endgame-tablebases)
- [4 See also](#see-also)
- [5 Publications](#publications)
  - [5.1 1960 ...](#1960-...)
  - [5.2 1970 ...](#1970-...)
  - [5.3 1980 ...](#1980-...)
  - [5.4 1990 ...](#1990-...)
  - [5.5 1995 ...](#1995-...)
  - [5.6 2000 ...](#2000-...)
  - [5.7 2005 ...](#2005-...)
  - [5.8 2010 ...](#2010-...)
  - [5.9 2015 ...](#2015-...)
  - [5.10 2020 ...](#2020-...)
- [6 Forum Posts](#forum-posts)
  - [6.1 2000 ...](#2000-...-2)
  - [6.2 2010 ...](#2010-...-2)
  - [6.3 2020 ...](#2020-...-2)
- [7 External Links](#external-links)
- [8 References](#references)

## Transposition Tables

Nowhere else are the [Transposition Hash Tables](Transposition_Table "Transposition Table") more efficient than in Endgames. They are invaluable.

## Evaluation

When doing a positional evaluation, in the endgame, the chess engines should change some parameters. So for example in the [middlegame](Middlegame "Middlegame"), if the opponent's [king](King "King") is trapped in the center, it should be evaluated much better for the program than the opponent's king, safely standing at the border. In the **endgame** however, its the other way round. A king on the edge or even in the corner has not so many squares to escape to and is more beneficial for the other player. Furthermore, if you only have one [bishop](Bishop "Bishop"), it might be good to evaluate the opponent's king being forced to go to the corner with the [color](Color "Color") of the bishop a higher bonus, than for the other corner. In addition Pawn promotion is a very important aim in most endgames. The chess engines should consider that by evaluating the strength of [passed pawns](Passed_Pawn "Passed Pawn").

## Special Knowledge

Some endgames are extensively covered by theory, and for that reason one can supply a vast number of heuristics for playing them. Typical examples include:

- [Blockage Detection](Blockage_Detection "Blockage Detection")
- [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")

## King and Pawns

- [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
- [King Centralization](King_Centralization "King Centralization")
- [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism")
- [KPK](KPK "KPK")
- [Pawn Endgame](Pawn_Endgame "Pawn Endgame")
- [Rule of the Square](Rule_of_the_Square "Rule of the Square")

## Pieces

- [Bishops of Opposite Colors](Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
- [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")
- [Bishop versus Knight](Bishop_versus_Knight "Bishop versus Knight")
- [KBNK Endgame](KBNK_Endgame "KBNK Endgame")
- [KRK](KRK "KRK")
- [Rook Endgame](Rook_Endgame "Rook Endgame")
- [Queen Endgame](index.php?title=Queen_Endgame&action=edit&redlink=1 "Queen Endgame (page does not exist)")
- [Queen versus Pawn](Queen_versus_Pawn "Queen versus Pawn")

## Endgame Tablebases

*see main article [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases").*

Currently many engines support the usage of [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases"), precalculated databases that hold for every possible position in a certain endgame, whether it is drawn or how many moves are left for a side to win/lose assuming perfect play. With the help of those, chess engines can simply lookup, if it is advisable to do a certain exchange or not, as well as how to finish some of the more tricky endgames. The advantage of Endgame Tablebases is the ability to determine the definite outcome of a certain position, but on the other side, Tablebases are very space consuming and the disk-access tends to be slow.

## See also

- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
- [Opening](Opening "Opening")
- [Middlegame](Middlegame "Middlegame")
- [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")

## Publications

## 1960 ...

- [Barbara J. Huberman](Barbara_Liskov "Barbara Liskov") (**1968**). *A Program to Play Chess End Games*. Technical Report no. CS-106, Ph.D. thesis. [Stanford University](Stanford_University "Stanford University"), Computer Science Department

## 1970 ...

- [Coen Zuidema](index.php?title=Coen_Zuidema&action=edit&redlink=1 "Coen Zuidema (page does not exist)") (**1974**). *Chess: How to Program the Exceptions?* Technical Report IW21/74, Department of Informatics, [Mathematical Center Amdsterdam](https://en.wikipedia.org/wiki/Centrum_Wiskunde_%26_Informatica). [pdf](http://oai.cwi.nl/oai/asset/9480/9480A.pdf)
- [Pericles Negri](index.php?title=Pericles_Negri&action=edit&redlink=1 "Pericles Negri (page does not exist)") (**1977**). *Inductive Learning in a Hierarchical Model for Representing Knowledge in Chess End Games*. [pdf](http://www.mli.gmu.edu/papers/69-78/77-2.pdf)
- [Ryszard Michalski](Ryszard_Michalski "Ryszard Michalski"), [Pericles Negri](index.php?title=Pericles_Negri&action=edit&redlink=1 "Pericles Negri (page does not exist)") (**1977**). *An experiment on inductive learning in chess endgames*. [Machine Intelligence 8](http://www.doc.ic.ac.uk/~shm/MI/mi8.html), [pdf](http://www.mli.gmu.edu/papers/69-78/77-1.pdf)
- [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1978**). *[Co-ordinate Squares: A Solution to Many Chess Pawn Endgames](http://dl.acm.org/citation.cfm?id=67030)*. B.Sc. thesis, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") » [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
- [Ivan Bratko](Ivan_Bratko "Ivan Bratko"), [Tim Niblett](Tim_Niblett "Tim Niblett") (**1979**). *Conjectures and Refutations in a Framework for Chess Endgames*. in Expert Systems in the Micro-Electronic Age ([Donald Michie](Donald_Michie "Donald Michie"), ed.), Edinburgh: Edinburgh University Press, 1979.

## 1980 ...

- [Danny Kopec](Danny_Kopec "Danny Kopec"), [Tim Niblett](Tim_Niblett "Tim Niblett") (**1980**). *How Hard is the Play of the King-Rook-King-Knight Ending?* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2")
- [John F. White](John_F._White "John F. White") (**1981**). *[Chess-End-Game](http://yourcomputeronline.wordpress.com/2010/12/27/chess-end-game/)*. [Your Computer](Your_Computer "Your Computer"), [December 1981](http://yourcomputeronline.wordpress.com/2010/12/10/december-1981-%E2%80%93-contents-and-editorial/)
- [Alen Shapiro](Alen_Shapiro "Alen Shapiro"), [Tim Niblett](Tim_Niblett "Tim Niblett") (**1982**). *Automatic Induction of Classification Rules for Chess End game.* [Advances in Computer Chess 3](Advances_in_Computer_Chess_3 "Advances in Computer Chess 3")
- [Ross Quinlan](Ross_Quinlan "Ross Quinlan") (**1982**). *[Semi-Autonomous Acquisition of Pattern-Based Knowledge](https://www.researchgate.net/publication/292173657_SEMI-AUTONOMOUS_ACQUISITION_OF_PATTERN-BASED_KNOWLEDGE)*. [Introductory Readings in Expert Systems](https://archive.org/details/introductoryread0000mich)
- [Ross Quinlan](Ross_Quinlan "Ross Quinlan") (**1983**). *[Learning Efficient Classification Procedures and Their Application to Chess End Games](https://link.springer.com/chapter/10.1007/978-3-662-12405-5_15)*. in [Machine Learning: An Artificial Intelligence Approach](https://link.springer.com/book/10.1007%2F978-3-662-12405-5)
- [Denis Verhoef](index.php?title=Denis_Verhoef&action=edit&redlink=1 "Denis Verhoef (page does not exist)"), [Jacco H. Wesselius](index.php?title=Jacco_H._Wesselius&action=edit&redlink=1 "Jacco H. Wesselius (page does not exist)") (**1987**). *Two-ply KRKN: Safely overtaking Quinlan*. [ICCA Journal, Vol. 10, No. 4](ICGA_Journal#10_4 "ICGA Journal")
- [Lars Rasmussen](Lars_Rasmussen "Lars Rasmussen") (**1987**). *Correcting grandmasters' Analyses in Elementary Endgames*. [ICCA Journal, Vol. 10, No. 4](ICGA_Journal#10_4 "ICGA Journal")

## 1990 ...

- [Lars Rasmussen](Lars_Rasmussen "Lars Rasmussen") (**1992**). *Queen versus Rook and Pawn*. [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal")
- [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth"), [Stephan Barth](index.php?title=Stephan_Barth&action=edit&redlink=1 "Stephan Barth (page does not exist)") (**1992**). *Validating a Range of Endgame Programs*. [ICCA Journal, Vol. 15, No. 3](ICGA_Journal#15_3 "ICGA Journal")
- [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1994**). *How Hard is the Correct Coding of an Easy Endgame?* [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [zipped ps](http://www.recherche.enac.fr/%7Eweill/publications/acc7.ps.gz)

## 1995 ...

- [Lewis Stiller](Lewis_Stiller "Lewis Stiller") (**1996**). *Multilinear Algebra and Chess Endgames*. [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski"), [pdf](http://www.msri.org/publications/books/Book29/files/stiller.pdf)
- [Roberto Cifuentes](https://en.wikipedia.org/wiki/Roberto_Cifuentes), [Maarten De Zeeuw](http://www.newinchess.com/De_Zeeuw__Maarten-ip-185.html), [Jan van Reek](Jan_van_Reek "Jan van Reek") (**1997**). *Secrets of Chess Endings*. [ICCA Journal, Vol. 20, No. 4](ICGA_Journal#20_4 "ICGA Journal")
- [Kevin Coplan](Kevin_Coplan "Kevin Coplan") (**1998**). *Synthesis of Chess and Chess-like Endgames by Recursive Optimisation*. [ICCA Journal, Vol. 21, No. 3](ICGA_Journal#21_3 "ICGA Journal")
- [Noam D. Elkies](Noam_Elkies "Noam Elkies") (**1999**). *On numbers and endgames: Combinatorial game theory in chess endgames*. [pdf](http://arxiv.org/PS_cache/math/pdf/9905/9905198v1.pdf), differs only in trivial stylistic details from the (**1996**) version published in [Games of No Chance](http://library.msri.org/books/Book29/index.html) edited by [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski")
- [Philip G. K. Reiser](index.php?title=Philip_G._K._Reiser&action=edit&redlink=1 "Philip G. K. Reiser (page does not exist)"), [Patricia J. Riddle](index.php?title=Patricia_J._Riddle&action=edit&redlink=1 "Patricia J. Riddle (page does not exist)") (**1999**). *[Evolving Logic Programs to Classify Chess-Endgame Positions](http://link.springer.com/chapter/10.1007%2F3-540-48873-1_19)*. [Simulated Evolution and Learning](http://link.springer.com/book/10.1007%2F3-540-48873-1), [Canberra](https://en.wikipedia.org/wiki/Canberra), Australia. [Lecture Notes in Artificial Intelligence](http://www.springer.com/series/1244), No. 1585, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [pdf](http://stancomb.co.uk/Papers/seal98.pdf) » [Learning](Learning "Learning")

## 2000 ...

- [Matthias Lüscher](Matthias_L%C3%BCscher "Matthias Lüscher") (**2000**). *Automatic Generation of an Evaluation Function for Chess Endgames*. [ETH Zurich](ETH_Zurich "ETH Zurich") Supervisors: [Thomas Lincke](Thomas_Lincke "Thomas Lincke") and [Christoph Wirth](Christoph_Wirth "Christoph Wirth"), [pdf](http://www.datacomm.ch/m.luescher/evaluation_function_en.pdf) » [Neural Networks](Neural_Networks "Neural Networks")
- [Kevin Coplan](Kevin_Coplan "Kevin Coplan") (**2001**). *[Synthesis of Chess and Chess-like Endgames: A Proof of Correctness](http://ilk.uvt.nl/icga/journal/contents/content24-1.htm#SYNTHESIS%20OF%20CHESS)*. [ICCA Journal, Vol. 24, No. 1](ICGA_Journal#24_1 "ICGA Journal")
- [Kevin Coplan](Kevin_Coplan "Kevin Coplan") (**2001**). *Synthesis of Chess-like Endgames: Towards a Proof of Correctness*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Fabian Mäser](Fabian_M%C3%A4ser "Fabian Mäser") (**2002**). *Global Threats in Combinatorial Games: A Computation Model with Applications to Chess Endgames*. in [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski") (ed) (**2002**). *[More Games of No Chance](http://library.msri.org/books/Book42/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press), [pdf](http://library.msri.org/books/Book42/files/maeser.pdf)

## 2005 ...

- [Ami Hauptman](index.php?title=Ami_Hauptman&action=edit&redlink=1 "Ami Hauptman (page does not exist)"), [Moshe Sipper](index.php?title=Moshe_Sipper&action=edit&redlink=1 "Moshe Sipper (page does not exist)") (**2005**). *GP-EndChess: Using Genetic Programming to Evolve Chess Endgame Players*. [EuroGP 2005](http://www.informatik.uni-trier.de/~ley/db/conf/eurogp/eurogp2005.html#HauptmanS05), [pdf](http://www.cs.bgu.ac.il/~sipper/papabs/eurogpchess-final.pdf)
- [Omid David](Eli_David "Eli David"), [Ariel Felner](Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2006**). *Blockage Detection in Pawn Endgames*. [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 3846, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)
- [Ami Hauptman](index.php?title=Ami_Hauptman&action=edit&redlink=1 "Ami Hauptman (page does not exist)"), [Moshe Sipper](index.php?title=Moshe_Sipper&action=edit&redlink=1 "Moshe Sipper (page does not exist)") (**2007**). *Emergence of Complex Strategies in the Evolution of Chess Endgame Players*. [Advances in Complex Systems 10](http://www.informatik.uni-trier.de/~ley/db/journals/advcs/advcs10.html#HauptmanS07)
- [John Nunn](John_Nunn "John Nunn") (**2009**). *[Understanding Chess Endgames](http://www.newinchess.com/Understanding_Chess_Endgames-p-1843.html)*. [Gambit](https://en.wikipedia.org/wiki/Gambit_Publications) <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## 2010 ...

- [John Nunn](John_Nunn "John Nunn") (**2010**). *[Nunn's Chess Endings, volume 1](http://www.newinchess.com/Nunn_s_Chess_Endings__Volume_1-p-5025.html)*. [Gambit](https://en.wikipedia.org/wiki/Gambit_Publications) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [John Nunn](John_Nunn "John Nunn") (**2010**). *[Nunn's Chess Endings, volume 2](http://www.newinchess.com/Nunn_s_Chess_Endings__Volume_2-p-5053.html)*. [Gambit](https://en.wikipedia.org/wiki/Gambit_Publications)
- [John Nunn](John_Nunn "John Nunn") (**2013**). *Discoveries in R+2P vs. R+P Endings*. [ICGA Journal, Vol. 36, No. 3](ICGA_Journal#36_3 "ICGA Journal") » [Lomonosov Tablebases](Lomonosov_Tablebases "Lomonosov Tablebases")
- [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2013**). *Rook vs. Bishop*. [ICGA Journal, Vol. 36, No. 4](ICGA_Journal#36_4 "ICGA Journal")
- [Matej Guid](Matej_Guid "Matej Guid"), [Martin Možina](Martin_Mo%C5%BEina "Martin Možina"), [Ciril Bohak](index.php?title=Ciril_Bohak&action=edit&redlink=1 "Ciril Bohak (page does not exist)"), [Aleksander Sadikov](Aleksander_Sadikov "Aleksander Sadikov"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2013**). *Building an Intelligent Tutoring System for Chess Endgames*. [CSEDU 2013](http://dblp.uni-trier.de/db/conf/csedu/csedu2013.html#GuidMBSB13)
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2014**). *[Chess Endgame Records (dataset)](http://centaur.reading.ac.uk/34268/)*.

## 2015 ...

- [Michael Hartisch](index.php?title=Michael_Hartisch&action=edit&redlink=1 "Michael Hartisch (page does not exist)"), [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer") (**2015**). *Optimal Robot Play in Certain Chess Endgame Situations*. [ICGA Journal, Vol. 38, No. 3](ICGA_Journal#38_3 "ICGA Journal")
- [Efstratios Grivas](index.php?title=Efstratios_Grivas&action=edit&redlink=1 "Efstratios Grivas (page does not exist)") (**2017**). *The Modern Endgame Manual*. [ICGA Journal, Vol. 39, No. 2](ICGA_Journal#39_2 "ICGA Journal")
- [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller") (**2017**). *Tablebases, Fermat, Knights and Knightmares*. [ICGA Journal, Vol. 39, No. 2](ICGA_Journal#39_2 "ICGA Journal")
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2017**). *Understanding Rook Endgames*. [ICGA Journal, Vol. 39, No. 2](ICGA_Journal#39_2 "ICGA Journal")
- [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2018**). *Chess Endgame News: The World Chess Championship, 2018*. [ICGA Journal, Vol. 40, No. 4](ICGA_Journal#40_4 "ICGA Journal") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Guy Haworth](Guy_Haworth "Guy Haworth") (**2019**). *FinalGen revisited: new discoveries*. [ICGA Journal, Vol. 41, No. 1](ICGA_Journal#41_1 "ICGA Journal") » [FinalGen](FinalGen "FinalGen")
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2019**). *Chess endgame news: Understanding minor piece endgames* . [ICGA Journal, Vol. 41, No. 2](ICGA_Journal#41_2 "ICGA Journal")
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2019**). *Chess endgame news: an endgame challenge for neural nets*. [ICGA Journal, Vol. 41, No. 3](ICGA_Journal#41_3 "ICGA Journal") » [Neural Networks](Neural_Networks "Neural Networks")

## 2020 ...

- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2020**). *CEN: Understanding Rook vs Minor Piece Endgames*. [ICGA Journal, Vol. 42, No. 1](ICGA_Journal#42_1 "ICGA Journal")
- [Mark Dvoretsky](https://en.wikipedia.org/wiki/Mark_Dvoretsky) (**2020**). *[Dvoretsky's Endgame Manual 5th Edition](https://www.newinchess.com/dvoretsky-s-endgame-manual-6270)*. revised by [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Russell Enterprises](https://en.wikipedia.org/wiki/Hanon_Russell)
- [Guy Haworth](Guy_Haworth "Guy Haworth") (**2021**). *Dvoretsky’s Endgame Manual, Edition 5: The bible evolves*. [ICGA Journal, Vol. 43, No. 1](ICGA_Journal#43_1 "ICGA Journal")
- [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [Christian R. Shelton](index.php?title=Christian_R._Shelton&action=edit&redlink=1 "Christian R. Shelton (page does not exist)") (**2021**). *Chess endgame compression via logic minimization*. [Advances in Computer Games 17](Advances_in_Computer_Games_17 "Advances in Computer Games 17")

## Forum Posts

## 2000 ...

- [Endgame evaluation](https://www.stmintz.com/ccc/index.php?id=198870) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), November 25, 2001
- [Piece Values in the Endgame](https://www.stmintz.com/ccc/index.php?id=348493) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), February 11, 2004 » [Point Value](Point_Value "Point Value")
- [transition to endgame](https://www.stmintz.com/ccc/index.php?id=358108) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), April 02, 2004
- [Improving the endgame of my engine](https://www.stmintz.com/ccc/index.php?id=359113) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), April 08, 2004 » [Sharper](Sharper "Sharper")
- [Definition of "endgame"?](http://www.talkchess.com/forum/viewtopic.php?t=19296) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 30, 2008

## 2010 ...

- [End-game evaluation](http://www.talkchess.com/forum/viewtopic.php?t=40629) by [H.G.Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 04, 2011
- [Start EndGame - A matter of fine tuning ???](http://www.talkchess.com/forum/viewtopic.php?t=47173) by [Lourenço Araujo de Oliveira Junior](Louren%C3%A7o_Araujo_de_Oliveira_Junior "Lourenço Araujo de Oliveira Junior"), [CCC](CCC "CCC"), February 09, 2013
- [End Game Heuristics](http://www.talkchess.com/forum/viewtopic.php?t=51672) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), March 20, 2014
- [Define end game](http://www.talkchess.com/forum/viewtopic.php?t=62153) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), November 16, 2016 » [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Testing endgame strength](http://www.talkchess.com/forum/viewtopic.php?t=64356) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 21, 2017 » [Engine Testing](Engine_Testing "Engine Testing"), [RuyDos](RuyDos "RuyDos")
- [mg vs eg eval](https://groups.google.com/d/msg/fishcooking/znU1a7aZ2XI/yJDFtOQnAwAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 06, 2019 » [Middlegame](Middlegame "Middlegame"), [Stockfish](Stockfish "Stockfish")

## 2020 ...

- [Endgame woes](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73012) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), February 07, 2020 » [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [Allowing null move pruning in the endgame](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73713) by Steven Griffin, [CCC](CCC "CCC"), April 20, 2020 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Endgame recognition](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76521) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 07, 2021

## External Links

- [Chess endgame from Wikipedia](https://en.wikipedia.org/wiki/Chess_endgame)
- [Pawnless chess endgame from Wikipedia](https://en.wikipedia.org/wiki/Pawnless_chess_endgame)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Dorothea Tanning](Category:Dorothea_Tanning "Category:Dorothea Tanning") - End Game, 1944, from [artnet Magazine - We Are Duchampians by Ben Davis](http://www.artnet.com/magazineus/reviews/davis/davis11-1-05.asp), [Endgame | Dorothea Tanning](https://www.dorotheatanning.org/life-and-work/view/229/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Nunn on Understanding Chess Endgames](http://www.chessbase.com/post/nunn-on-understanding-che-endgames), [ChessBase News](ChessBase "ChessBase"), September 13, 2009
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Nunn’s Chess Endings Volume One](http://www.chessbase.com/post/nunn-s-che-endings-volume-one), [ChessBase News](ChessBase "ChessBase"), May 28, 2010
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [World Chess Championship 2018 from Wikipedia](https://en.wikipedia.org/wiki/World_Chess_Championship_2018)

**[Up one level](Game_Phases "Game Phases")**

