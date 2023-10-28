---
title: Pawn Endgame
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* [Game Phases](Game_Phases "Game Phases") \* [Endgame](Endgame "Endgame") \* Pawn Endgame**



 [](http://www.elke-rehder.de/Chess_Paintings.htm) Pawns threaten the King <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
The **Pawn Endgame** is an endgame actually without any [pieces](Pieces "Pieces") but only [pawns](Pawn "Pawn") and [kings](King "King"). Pawn endings somehow remind on a completely different game domain, requiring special evaluation routines, as well as conditions inside the [search](Search "Search"), i. e. switching of [null move pruning](Null_Move_Pruning "Null Move Pruning"). Specially in "closed" or blocked pawn endgames with [rammed](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)") and [backward pawns](Backward_Pawn "Backward Pawn") with only very few reasonable moves due to extremely low [mobility](Mobility "Mobility"), [zugzwang](Zugzwang "Zugzwang"), [stalemate](Stalemate "Stalemate"), [triangulation](Triangulation "Triangulation"), [tempo](Tempo "Tempo") issues, the concepts of [opposition](Opposition "Opposition") or more general [corresponding squares](Corresponding_Squares "Corresponding Squares"), and [king path puzzles](King_Pattern#FloodFillAlgorithms "King Pattern") start to dominate. Otherwise, in open pawn endings, naturally with a bigger [branching factor](Branching_Factor "Branching Factor") than the closed, all kinds of [passed pawn](Passed_Pawn "Passed Pawn") issues are taken into account.


Using the [transposition table](Transposition_Table "Transposition Table") is essential in pawn endings, as demonstrated in positions like the [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position") (Fine 70) or the [Réti Endgame Study](R%C3%A9ti_Endgame_Study "Réti Endgame Study") with astonishing [search depths](Depth "Depth"). Certainly, many programs [extend](Capture_Extensions "Capture Extensions") a lot, if the last piece was captured with the transition into an "unclear" pawn endgame. [Ed Schröder](Ed_Schroder "Ed Schroder") for instance, extends by three [plies](Ply "Ply") in [Rebel](Rebel "Rebel") considering [bounds](Bound "Bound") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . 



### Contents


* [1 Considerations](#considerations)
* [2 Pawn Endgame Programs](#pawn-endgame-programs)
* [3 Pawn Endgame Positions](#pawn-endgame-positions)
* [4 See also](#see-also)
* [5 Publications](#publications)
	+ [5.1 Chess](#chess)
	+ [5.2 Computer Chess](#computer-chess)
	+ [5.3 1977 ...](#1977-...)
	+ [5.4 1980 ...](#1980-...)
	+ [5.5 1990 ...](#1990-...)
	+ [5.6 2000 ...](#2000-...)
	+ [5.7 2010 ...](#2010-...)
* [6 Forum Posts](#forum-posts)
	+ [6.1 1997 ...](#1997-...)
	+ [6.2 2000 ...](#2000-...-2)
	+ [6.3 2010 ...](#2010-...-2)
* [7 External Links](#external-links)
* [8 References](#references)






* [Backward Pawn](Backward_Pawn "Backward Pawn")
* [Blockage Detection](Blockage_Detection "Blockage Detection")
* [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [Capture Extensions](Capture_Extensions "Capture Extensions")
* [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
* [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
* [Hidden Passed Pawn](Hidden_Passed_Pawn "Hidden Passed Pawn")
* [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism")
* [KPK](KPK "KPK") database/rules
* [Opposition](Opposition "Opposition")
* [Outside Passed Pawn](Outside_Passed_Pawn "Outside Passed Pawn")
* [Pawns Breakthrough](Pawns_Breakthrough "Pawns Breakthrough")
* [Pawn Race](Pawn_Race "Pawn Race")
* [Passed Pawn](Passed_Pawn "Passed Pawn")
* [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
* [Protected Passed Pawn](Protected_Passed_Pawn "Protected Passed Pawn")
* [Rule of the Square](Rule_of_the_Square "Rule of the Square")
* [Stalemate](Stalemate "Stalemate")
* [Tempo](Tempo "Tempo")
* [Triangulation](Triangulation "Triangulation")
* [Zugzwang](Zugzwang "Zugzwang")


## Pawn Endgame Programs


* [Chunker](Chunker "Chunker")
* [Endspiel‎](Endspiel "Endspiel")
* [PawnKing](PawnKing "PawnKing")
* [Peasant](Peasant "Peasant")


## Pawn Endgame Positions


* [Lasker-Reichhelm Position](Lasker-Reichhelm_Position "Lasker-Reichhelm Position") (Fine 70)
* [Réti Endgame Study](R%C3%A9ti_Endgame_Study "Réti Endgame Study")


## See also


* [King and Pawns](King_Pattern#KingAndPawns "King Pattern") from [King Pattern](King_Pattern "King Pattern") in [Bitboards](Bitboards "Bitboards")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
* [Pawn Pattern and Properties](Pawn_Pattern_and_Properties "Pawn Pattern and Properties") in [Bitboards](Bitboards "Bitboards")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Queen versus Pawn](Queen_versus_Pawn "Queen versus Pawn")
* [Transposition Table](Transposition_Table "Transposition Table")


## Publications


### Chess


* [Vitali Halberstadt](https://en.wikipedia.org/wiki/Vitaly_Halberstadt) and [Marcel Duchamp](Category:Marcel_Duchamp "Category:Marcel Duchamp") (**1932**). *L'opposition et les cases conjuguées sont réconciliées*. » [Corresponding Squares](Corresponding_Squares "Corresponding Squares")


 Paris-Brussels 1932, German Edition 2001 *[Opposition und Schwesterfelder](http://www.buecher-nach-isbn.info/3-608/3608500359-Opposition-und-Schwesterfelder-Marcel-Duchamp-Vitali-Halberstadt-3-608-50035-9.html)*, ISBN 3-932170-35-0
* [Reuben Fine](https://en.wikipedia.org/wiki/Reuben_Fine) (**1941**). *[Basic Chess Endings](https://en.wikipedia.org/wiki/Basic_Chess_Endings)*, Chapter 2, King and Pawn Endings
* [Yuri Averbakh](https://en.wikipedia.org/wiki/Yuri_Averbakh), [Ilia Maizelis](http://de.wikipedia.org/wiki/Ilja_Lwowitsch_Maiselis) (**1987**). *Comprehensive Chess Endings Vol 4: Pawn Endings, Cadogan Books 1987*.
* [Karsten Müller](Karsten_M%C3%BCller "Karsten Müller"), [Frank Lamprecht](https://en.wikipedia.org/wiki/Frank_Lamprecht) (**2000**). *Secrets of Pawn Endings*. [Everyman Chess](https://en.wikipedia.org/wiki/Everyman_Chess), (**2007**). [re-issue](http://dev.jeremysilman.com/shop/pc/Secrets-of-Pawn-Endings-p3748.htm) by [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications)
* [Eric Schiller](Eric_Schiller "Eric Schiller") (**2006**). *Of Kings and Pawns - Chess Strategy in the Endgame*, Universal Publishers, ISBN-13: 978-1581129090, [amazon](http://www.amazon.com/Kings-Pawns-Chess-Strategy-Endgame/dp/1581129092), sample chapter as [pdf](http://www.ericschiller.com/pdf/Of%20Kings%20and%20Pawns%20Excerpts.pdf)


### Computer Chess


### 1977 ...


* [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *PEASANT: An endgame program for kings and pawns*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") » [Peasant](Peasant "Peasant")
* [Crispin Perdue](index.php?title=Crispin_Perdue&action=edit&redlink=1 "Crispin Perdue (page does not exist)"), [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *[EG: a case study in problem solving with king and pawn endings](http://dl.acm.org/citation.cfm?id=1624529)*. [5. IJCAI 1977](http://www.sigmod.org/dblp/db/conf/ijcai/ijcai77.html)
* [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1978**). *[Co-ordinate Squares: A Solution to Many Chess Pawn Endgames](http://dl.acm.org/citation.cfm?id=67030)*. B.Sc. thesis, [Massachusetts Institute of Technology](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology"), reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1979**). *Co-ordinate Squares: A Solution to Many Chess Pawn Endgames*. (abbreviated version of B.Sc. thesis), [IJCAI-79](Conferences#IJCAI1979 "Conferences"), Tokyo, Japan
* [Peter W. Frey](Peter_W._Frey "Peter W. Frey"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1979**). *[Creating a Chess-Player, Part 4: Thoughts on Strategy](https://archive.org/stream/byte-magazine-1979-01/1979_01_BYTE_04-01_Life_Algorithms#page/n127/mode/2up)*. In [Blaise W. Liffick](http://cs.millersville.edu/~liffick/) (ed.), [The Byte Book of Pascal](http://books.google.com/books/about/The_BYTE_book_of_Pascal.html?id=ofpfQgAACAAJ), pp. 143-155. Byte Publications, also [BYTE, Vol. 4, No. 1](Byte_Magazine#BYTE401 "Byte Magazine") » [Corresponding Squares](Corresponding_Squares "Corresponding Squares")


### 1980 ...


* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Ein Modell für Schachbauernendspiele mit menschlichen Problemlösungstechniken*. PhD-Thesis, Department of Computer Science, [University of Vienna](https://en.wikipedia.org/wiki/University_of_Vienna), Supervisors: [Prof. Dr. Curt Christian](http://www.logic.univie.ac.at/) (University of Vienna) and [Prof. Dr. Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") ([Vienna University of Technology](Vienna_University_of_Technology "Vienna University of Technology")).
* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1982**). *Construction of Planned Move Trees for Chess Pawn Endings*. Sigart Newsletter 80, pp. 163-168.
* [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1983**). *Knowledge-Based Move Selection and Evaluation to Guide the Search in Chess Pawn Endings*. [ICCA Journal, Vol. 6, No. 3](ICGA_Journal#6_3 "ICGA Journal")
* [Murray Campbell](Murray_Campbell "Murray Campbell"), [Hans Berliner](Hans_Berliner "Hans Berliner") (**1983**). *A Chess Program That Chunks*. AAAI 1983 49-53, [pdf](http://www.aaai.org/Papers/AAAI/1983/AAAI83-012.pdf) » [Chunker](Chunker "Chunker")
* [Hans Berliner](Hans_Berliner "Hans Berliner"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1984**). *[Using Chunking to Solve Chess Pawn Endgames](http://www.sciencedirect.com/science/article/pii/0004370284900067)*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 23, No. 1, pp. 97-120. ISSN 0004-3702
* [Andrew N. Walker](Andy_Walker "Andy Walker") (**1989**). *Interactive Solution of King and Pawn Endings*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")


### 1990 ...


* [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1995**). *Combining Knowledge and Search to Yield Infallible Endgame Programs A study of passed Pawns in the KPKP endgame.* [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Wilhelm Barth](Wilhelm_Barth "Wilhelm Barth") (**1995**). *The KPKP Endgame: An Amplification*. [ICCA Journal, Vol. 18, No. 4](ICGA_Journal#18_4 "ICGA Journal")


### 2000 ...


* [Omid David](Eli_David "Eli David"), [Ariel Felner](Ariel_Felner "Ariel Felner"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2004**). *Blockage Detection in Pawn Endgames*. [ICGA Journal, Vol. 27, No. 3](ICGA_Journal#27_3 "ICGA Journal")
* [Zvi Retchkiman Königsberg](Zvi_Retchkiman_K%C3%B6nigsberg "Zvi Retchkiman Königsberg") (**2007**). *A Combinatorial Game Mathematical Strategy Planning Procedure for a Class of Chess Endgames*. [International Mathematical Forum, Vol. 2, No. 68](http://www.m-hikari.com/imf-password2007/65-68-2007/index.html)


### 2010 ...


* [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**2014**). *Computer Chess Endgame Play with Pawns: Then and Now*. [ICGA Journal, Vol. 37, No. 4](ICGA_Journal#37_4 "ICGA Journal") » [Peasant](Peasant "Peasant"), [Crafty](Crafty "Crafty")


## Forum Posts


### 1997 ...


* [Deep analyses of pawn endgames](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/49490ca6fbd06b94) by [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 10, 1997


### 2000 ...


* [Pawn endings [blocked pawns](https://www.stmintz.com/ccc/index.php?id=92283)] by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), January 26, 2000
* [Pawn endgame test suite](https://www.stmintz.com/ccc/index.php?id=131885) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), October 07, 2000 » [Test-Positions](Test-Positions "Test-Positions")
* [king and pawns ending](https://www.stmintz.com/ccc/index.php?id=247236) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), August 23, 2002
* [Is this rule safe (how has K&Ps vs K&Ps databases? ...)](http://www.talkchess.com/forum/viewtopic.php?t=14578) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 20, 2007 » [KPK](KPK "KPK"), [Now](Now "Now")
* [king pawn endgames](http://www.talkchess.com/forum/viewtopic.php?t=19304) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), January 30, 2008


### 2010 ...


* [Pawns ending](http://www.talkchess.com/forum/viewtopic.php?t=37023) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), December 10, 2010
* [Code of Chiron for Detection of Pawn Blockages](http://www.talkchess.com/forum/viewtopic.php?t=40748) by [Ubaldo Andrea Farina](Ubaldo_Andrea_Farina "Ubaldo Andrea Farina"), [CCC](CCC "CCC"), October 13, 2011
* [pawn endgame](http://www.talkchess.com/forum/viewtopic.php?t=46183) by [Marek Kwiatkowski](index.php?title=Marek_Kwiatkowski&action=edit&redlink=1 "Marek Kwiatkowski (page does not exist)"), [CCC](CCC "CCC"), November 28, 2012


## External Links


* [King and pawn endings from Wikipedia](https://en.wikipedia.org/wiki/Chess_endgame#King_and_pawn_endings)
* [Chess Training: Endgame Lab - King and Pawn Endings](http://chess-training.blogspot.com/2006/11/endgame-lab-king-and-pawn-endings_24.html)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess Paintings](http://www.elke-rehder.de/Chess_Paintings.htm) by [Elke Rehder](Arts#Rehder "Arts")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Quote by [Ed Schröder](Ed_Schroder "Ed Schroder") from his [Programmer Corner](Rebel#ProgrammerCorner "Rebel"): The Search is extended with 3 plies when the search transits to a pawn-ending. An extra window check of 3 pawns is done on I\_SCORE before the extension is rewarded
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Steven Edwards](Steven_Edwards "Steven Edwards") (**1995**). *Comments on Barth’s Article “Combining Knowledge and Search to Yield Infallible Endgame Programs.”* [ICCA Journal, Vol. 18, No. 4](ICGA_Journal#18_4 "ICGA Journal")

**[Up one Level](Endgame "Endgame")**







 
