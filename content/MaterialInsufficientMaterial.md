---
title: MaterialInsufficientMaterial
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Material**



 [](http://www.elke-rehder.de/Chess_Woodcuts.htm) [The Royal Game](https://en.wikipedia.org/wiki/The_Royal_Game) IV <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Material**,  

a term determined by the sum of [piece values](Point_Value "Point Value") of each side. The material value is the most influential part of the evaluation. Usually it is the sum of a constant value for each piece present, measured in units of a fraction of a pawn, for instance the common [centipawn scale](Centipawns "Centipawns"), which allows positional features of the position, worth less than a single pawn, to be evaluated without requiring fractions but a [fixed point score](Score#FixedPoint "Score"). 



### Contents


* [1 Basic Piece Values](#basic-piece-values)
* [2 Other Material Considerations](#other-material-considerations)
* [3 Insufficient Material](#insufficient-material)
* [4 Material Balance](#material-balance)
* [5 Hashing and Tables](#hashing-and-tables)
* [6 See also](#see-also)
* [7 Related Publications](#related-publications)
* [8 Forum Posts](#forum-posts)
	+ [8.1 2000 ...](#2000-...)
	+ [8.2 2005 ...](#2005-...)
	+ [8.3 2010 ...](#2010-...)
	+ [8.4 2015 ...](#2015-...)
	+ [8.5 2020 ...](#2020-...)
* [9 External Links](#external-links)
* [10 References](#references)






Piece relative values concerning their relative strength in potential exchanges based on human experience and [learning](Learning "Learning")



* [Point Value](Point_Value "Point Value")
* [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")


## Other Material Considerations


In chess, it is known that certain material features provide an advantage, such as the [bishop pair](Bishop_Pair "Bishop Pair") (which might be worth as much as half a pawn). A program might increase the values of rooks when there are less pawns on the board or prefer knights when there are many pawns. [Larry Kaufman](Larry_Kaufman "Larry Kaufman") performed statistical tests on a variety of different material configurations to approximate their values <a id="cite-note-2" href="#cite-ref-2">[2]</a> .


Other factors that affect material evaluation might be:



* Bonus for the [bishop pair](Bishop_Pair "Bishop Pair") (bishops complement each other, controlling squares of different [color](Color "Color"))
* Penalty for the rook pair (Larry Kaufman called it "principle of redundancy")
* Penalty for the knight pair (as two knights are less successful against the rook than any other pair of minor pieces)
* decreasing the value of the rook pawns and increasing the value of the central pawns (though this can be done in the [piece-square tables](Piece-Square_Tables "Piece-Square Tables") as well)
* Trade down bonus that encourages the winning side to trade pieces but no pawns <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* Penalty for having no pawns, as it makes it more difficult to win the endgame
* Bad trade penalty as proposed by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), that is penalizing the material imbalances that are disadvantageous like having three pawns for a piece or a rook for two minors.
* Elephantiasis effect as suggested by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") (meaning that stronger pieces lose part of their value in presence of weaker pieces)






## Insufficient Material


Using values like these blindly can lead to bad play. Most programs uses special code or tables to detect drawn or likely drawn material combinations. For example, KB vs K is a draw, as is KN vs K and KNN vs K. There is also a class of almost-certain draws, not mentioned in the [FIDE rules](index.php?title=FIDE_rules&action=edit&redlink=1 "FIDE rules (page does not exist)") because of the possibility of a checkmate (KN vs KN <a id="cite-note-4" href="#cite-ref-4">[4]</a> , KB vs KN, KNN vs KB, KBN vs KB, KBN vs KR etc.) A general rule that, although not perfect, catches many likely draws is that if one side has no pawns left, it needs the equivalent of +4 pawns more material to win. For example, KRN vsv KR is usually a draw, where KRR vs KBN is usually a win for the rook side. For more details see [draw evaluation](Draw_Evaluation "Draw Evaluation") and [interior node recognizer](Interior_Node_Recognizer "Interior Node Recognizer").




## Material Balance


The Material Balance is finally returned as the almost most dominating evaluation term, usually in [Negamax](Negamax "Negamax") from [side to move's](Side_to_move "Side to move") point of view, and in its pure form simply the difference of both sides material, MD:




```

md := material[side_2_move] - material[side_2_move ^ 1];

```

As mentioned, other material considerations, concerning [insufficient material](Material#InsufficientMaterial "Material") and material imbalances (e.g. rook versus two minor pieces, queen versus two rooks or three pieces, three pawns versus piece) should be taken into account - for instance to encourage exchanging pieces but no pawns if ahead, see the [hashing approach](Material_Hash_Table#ApproachOfChess "Material Hash Table") of [Chess 4.5](Chess_(Program) "Chess (Program)").



## Hashing and Tables


To save speed in the material evaluation, programs using rules often [hash](Hash_Table "Hash Table") the material evaluation scores. With [precomputed arrays of material values](Material_Tables "Material Tables"), this is not needed.



* [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Material Tables](Material_Tables "Material Tables")


## See also


* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Fixed Point Score](Score#FixedPoint "Score")
* [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
* [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
* [Material in Chess 4.5](Material_Hash_Table#ApproachOfChess "Material Hash Table")
* [Material in SOMA](SOMA#Material "SOMA")
* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")


## Related Publications


* [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Alan Turing](Alan_Turing "Alan Turing") (**1953**). ***Chess***. part of the collection *Digital Computers Applied to Games*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in *The Essential Turing*, [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
* [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
* [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine") (ed. [Peter W. Frey](Peter_W._Frey "Peter W. Frey")), pp. 82-118. Springer-Verlag, New York, N.Y. 2nd ed. 1983. ISBN 0-387-90815-3. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
* [Gennady Timoshchenko](index.php?title=Gennady_Timoshchenko&action=edit&redlink=1 "Gennady Timoshchenko (page does not exist)") (**1993**). *Bishop or Knight*? [ICCA Journal, Vol. 16, No. 4](ICGA_Journal#16_4 "ICGA Journal")
* [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1994**). *The Relative Value of the Pieces*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 4, No. 2, pp. 33
* [Mark Sturman](Mark_Sturman "Mark Sturman") (**1995**). *Beware The Bishop Pair*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, No. 2, pp.58 <a id="cite-note-5" href="#cite-ref-5">[5]</a> » [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Mark Sturman](Mark_Sturman "Mark Sturman") (**1996**). *Beware the Bishop Pair*. [ICCA Journal, Vol. 19, No. 2](ICGA_Journal#19_2 "ICGA Journal")
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1999**). *[The Evaluation of Material Imbalances](https://www.chess.com/article/view/the-evaluation-of-material-imbalances-by-im-larry-kaufman)*. (first published in [Chess Life](https://en.wikipedia.org/wiki/Chess_Life) March 1999, online version edited by [Dan Heisman](Dan_Heisman "Dan Heisman"))
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning of Piece Values for Chess Variants.* Technical Report TUD–KE–2008-07, Knowledge Engineering Group, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ke.tu-darmstadt.de/publications/reports/tud-ke-2008-07.pdf)
* [Christian Hesse](Christian_Hesse "Christian Hesse") (**2011**). *[The Joys of Chess - Heroes, Battles & Brilliancies](http://www.newinchess.com/The_Joys_of_Chess-p-953.html)*. ISBN: 978-90-5691-355-7, [New In Chess](https://en.wikipedia.org/wiki/New_In_Chess) <a id="cite-note-6" href="#cite-ref-6">[6]</a>


## Forum Posts


### 2000 ...


* [Queen vs two rooks](https://www.stmintz.com/ccc/index.php?id=222033) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), April 07, 2002
* [Exceptions to (1,3,3,5,9)](https://www.stmintz.com/ccc/index.php?id=286659) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 24, 2003
* [Bad trade](https://www.stmintz.com/ccc/index.php?id=345860) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), January 30, 2004


### 2005 ...


* [Quark 2.35 draw claim bug](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2112) by [Igor Korshunov](Igor_Korshunov "Igor Korshunov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2005 » [Quark](Quark "Quark"), [Draw](Draw "Draw")
* [Material imbalance evaluation](http://www.talkchess.com/forum/viewtopic.php?t=13166) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), April 16, 2007
* [Evaluation of material imbalance (a Rybka secret?)](http://www.talkchess.com/forum/viewtopic.php?t=18240) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), December 06, 2007
* [Relative Piece Values](http://www.talkchess.com/forum/viewtopic.php?t=27387) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), April 09, 2009 » [Point Value](Point_Value "Point Value")
* [Testing of Kaufman Material Values](http://www.talkchess.com/forum/viewtopic.php?t=27616) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), April 25, 2009
* [Rook Pair Penalty, Knight Pair Penalty, Having a Pawn Bonus](http://www.talkchess.com/forum/viewtopic.php?t=27842) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), May 11, 2009


### 2010 ...


* [Efficiently index material signatures and lookup](http://www.talkchess.com/forum/viewtopic.php?t=33035) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), March 03, 2010
* [Stockfish - material balance/imbalance evaluation](http://www.talkchess.com/forum/viewtopic.php?t=34159) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), May 05, 2010 » [Stockfish](Stockfish "Stockfish")


**2011**



* [Wrong draw claim by Naum 4.2 ?](http://www.talkchess.com/forum/viewtopic.php?t=37592) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 12, 2011 » [Draw](Draw "Draw")
* [Material imbalance/bad trade and borrowing code](http://www.talkchess.com/forum/viewtopic.php?t=37831) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), January 27, 2011


**2012**



* [Stockfish Code ( Piece Value's)](http://www.talkchess.com/forum/viewtopic.php?t=41916) by Nolan Denson, [CCC](CCC "CCC"), January 10, 2012 » [Stockfish](Stockfish "Stockfish")
* [Lone minor piece penalty - What did Larry mean?](http://www.talkchess.com/forum/viewtopic.php?t=41905) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), January 10, 2012
* [Why Knight and (lone) Bishop are so nearly equal in value](http://www.talkchess.com/forum/viewtopic.php?t=45321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 25, 2012


**2013**



* [An experiment with material imbalances and game-phase](http://www.talkchess.com/forum/viewtopic.php?t=47713) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), April 06, 2013 » [Material Tables](Material_Tables "Material Tables")
* [A balanced approach to imbalances](http://www.talkchess.com/forum/viewtopic.php?t=49808) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), October 23, 2013
* [handling draw by insufficient material](http://www.talkchess.com/forum/viewtopic.php?t=50150) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), November 19, 2013 » [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
* [Lonely queen](http://www.talkchess.com/forum/viewtopic.php?t=50504) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), December 15, 2013
* [Queen vs 3 minors](http://macechess.blogspot.de/2013/12/queen-vs-3-minors.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), December 18, 2013
* [Accessing Material Imbalance Information?](http://www.talkchess.com/forum/viewtopic.php?t=50550) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 19, 2013 » [Material Tables](Material_Tables "Material Tables")
* [Queen vs 3 Minors part 2](http://macechess.blogspot.de/2013/12/queen-vs-3-minors-part-2.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), December 21, 2013
* [Trading penalty with imbalances](http://www.talkchess.com/forum/viewtopic.php?t=50601) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), December 22, 2013


**2014**



* [Scaling eval with material on the board](http://www.talkchess.com/forum/viewtopic.php?t=52757) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), June 25, 2014
* [Obligatory scaling](http://www.talkchess.com/forum/viewtopic.php?t=52775) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), June 27, 2014 » [Rook Endgame](Rook_Endgame "Rook Endgame")


### 2015 ...


* [Rook vs 2 minor pieces with pawns on the board](http://www.talkchess.com/forum/viewtopic.php?t=56142) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), April 27, 2015
* [Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), April 30, 2015 <a id="cite-note-7" href="#cite-ref-7">[7]</a> » [Point Value](Point_Value "Point Value"), [Automated Tuning](Automated_Tuning "Automated Tuning")


**2017**



* [Another way of evaluating material imbalances](http://www.talkchess.com/forum/viewtopic.php?t=62687) by [Volker Annuss](Volker_Annuss "Volker Annuss"), [CCC](CCC "CCC"), January 01, 2017 » [Arminius](Arminius "Arminius")
* [trading pieces and pawns based on material balance](http://www.talkchess.com/forum/viewtopic.php?t=64110) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 28, 2017
* [insufficient mating material](http://www.talkchess.com/forum/viewtopic.php?t=64115) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 29, 2017 » [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
* [list of material combinations requiring specialized eval ?](http://www.talkchess.com/forum/viewtopic.php?t=64576) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), July 11, 2017
* [Trading Pieces When Ahead In Material](http://www.talkchess.com/forum/viewtopic.php?t=65364) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), October 03, 2017
* [Magic end-game material hash?](http://www.talkchess.com/forum/viewtopic.php?t=65870) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 30, 2017


**2018**



* ['ab-initio' piece values](http://www.talkchess.com/forum/viewtopic.php?t=66966) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 30, 2018 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [The Xiphos Material Evaluator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68842) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 05, 2018 » [Xiphos](Xiphos "Xiphos")


### 2020 ...


* [Imbalance](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72967) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 01, 2020
* [Trading gradient: to trade or not to trade?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76629) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 18, 2021


## External Links


* [The Evaluation of Material Imbalances](https://www.chess.com/article/view/the-evaluation-of-material-imbalances-by-im-larry-kaufman) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman")
* [Statistics of material imbalances in chess games](http://walkofmind.com/programming/chess/mat_stats.html) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti") » [Match Statistics](Match_Statistics "Match Statistics")
* [Chess piece relative value from Wikipedia](https://en.wikipedia.org/wiki/Chess_piece_relative_value)
* [About the Values of Chess Pieces](http://www.chessvariants.com/d.betza/pieceval/index.html) by [Ralph Betza](index.php?title=Ralph_Betza&action=edit&redlink=1 "Ralph Betza (page does not exist)")
* [The joys of chess – and the value of the pieces](http://www.chessbase.com/newsdetail.asp?newsid=7775), [ChessBase News](ChessBase "ChessBase"), December 21, 2011 <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Royal Game, Woodcuts Art](http://www.elke-rehder.de/Chess_Woodcuts.htm) by [Elke Rehder](Arts#Rehder "Arts"), [Stefan Zweig](https://en.wikipedia.org/wiki/Stefan_Zweig) [The Royal Game](https://en.wikipedia.org/wiki/The_Royal_Game) IV
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Evaluation of material imbalance (a Rybka secret?)](http://www.talkchess.com/forum/viewtopic.php?t=18240) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti") from [CCC](CCC "CCC"), December 06, 2007
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [trading pieces and pawns based on material balance](http://www.talkchess.com/forum/viewtopic.php?t=64110) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 28, 2017
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Quark 2.35 draw claim bug](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2112) by [Igor Korshunov](Igor_Korshunov "Igor Korshunov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 28, 2005 » [Quark](Quark "Quark"), [Draw](Draw "Draw")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Looking for Mark Sturman](https://groups.google.com/d/msg/rec.games.chess/xFCRAQIqvjw/OVFg2ezWYTYJ) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), July 02, 1995
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [The joys of chess – and the value of the pieces](http://www.chessbase.com/newsdetail.asp?newsid=7775), [ChessBase News](ChessBase "ChessBase"), December 21, 2011
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Определяем веса шахматных фигур регрессионным анализом / Хабрахабр](http://habrahabr.ru/post/254753/) by [WinPooh](Vladimir_Medvedev "Vladimir Medvedev"), April 27, 2015 (Russian)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Christian Hesse](Christian_Hesse "Christian Hesse") (**2011**). *[The Joys of Chess - Heroes, Battles & Brilliancies](http://www.newinchess.com/The_Joys_of_Chess-p-953.html)*. ISBN: 978-90-5691-355-7, [New In Chess](https://en.wikipedia.org/wiki/New_In_Chess)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Interesting article about the value of the pieces](http://www.talkchess.com/forum/viewtopic.php?t=41556) by Aloisio Ponti, [CCC](CCC "CCC"), December 22, 2011

**[Up one level](Evaluation "Evaluation")**







 
