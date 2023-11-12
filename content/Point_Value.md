---
title: Point Value
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Pieces](Pieces "Pieces") \* Point Value**



[ [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky"), Points <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Point Value**,  

a piece relative value concerning its relative strength in potential exchanges based on human experience and [learning](Learning "Learning"). Common rule of thumb are the {1, 3, 3, 5, 9} point values for [pawn](Pawn "Pawn") (1), [knight](Knight "Knight"), [bishop](Bishop "Bishop"), [rook](Rook "Rook") and [queen](Queen "Queen"), also proposed by [Claude Shannon](Claude_Shannon "Claude Shannon") in his 1949 paper *Programming a Computer for Playing Chess* <a id="cite-note-2" href="#cite-ref-2">[2]</a> . In the [evaluation](Evaluation "Evaluation") of a chess program, the balance of [material](Material "Material"), the aggregated point values for both sides, is usually the most influential term. 




## Basic values


Measured in units of a fraction of a pawn, for instance the common [centipawn scale](Centipawns "Centipawns"), allows positional features of the position, worth less than a single pawn, to be evaluated without requiring fractions but a [fixed point score](Score#FixedPoint "Score"). Sample point values from various sources over the time, most were used in concrete chess programs.





|  Source
 |  Year
 |  Pawn
 |  Knight
 |  Bishop
 |  Rook
 |  Queen
 |
| --- | --- | --- | --- | --- | --- | --- |
| [H. S. M. Coxeter](Mathematician#Coxeter "Mathematician") <a id="cite-note-7" href="#cite-ref-7">[7]</a> |  1940
 |  |  300
 |  350
 |  550
 |  1000
 |
| [Max Euwe](Max_Euwe "Max Euwe") and Hans Kramer <a id="cite-note-8" href="#cite-ref-8">[8]</a> |  1944
 |  100
 |  350
 |  350
 |  550
 |  1000
 |
| [Claude Shannon](Claude_Shannon "Claude Shannon") <a id="cite-note-9" href="#cite-ref-9">[9]</a> |  1949
 |  100
 |  300
 |  300
 |  500
 |  900
 |
| [Alan Turing](Alan_Turing "Alan Turing") <a id="cite-note-10" href="#cite-ref-10">[10]</a> |  1953
 |  100
 |  300
 |  350
 |  500
 |  1000
 |
| [Mac Hack](Mac_Hack "Mac Hack") <a id="cite-note-11" href="#cite-ref-11">[11]</a> |  1967
 |  100
 |  325
 |  350
 |  500
 |  975
 |
| [Chess 4.5](Chess_(Program) "Chess (Program)") <a id="cite-note-12" href="#cite-ref-12">[12]</a> |  1977
 |  100
 |  325
 |  350
 |  500
 |  900
 |
| [Tomasz Michniewski](Tomasz_Michniewski "Tomasz Michniewski") <a id="cite-note-13" href="#cite-ref-13">[13]</a> |  1995
 |  100
 |  320
 |  330
 |  500
 |  900
 |
| [Hans Berliner](Hans_Berliner "Hans Berliner") <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a> |  1999
 |  100
 |  320
 |  333
 |  510
 |  880
 |
| [Larry Kaufman](Larry_Kaufman "Larry Kaufman") <a id="cite-note-16" href="#cite-ref-16">[16]</a> |  1999
 |  100
 |  325
 |  325
 |  500
 |  975
 |
| [Fruit](Fruit "Fruit") and others <a id="cite-note-17" href="#cite-ref-17">[17]</a> |  2005
 |  100
 |  400
 |  400
 |  600
 |  1200
 |
| [Larry Kaufman](Larry_Kaufman "Larry Kaufman") <a id="cite-note-18" href="#cite-ref-18">[18]</a> |  2012
 |  100
 |  350
 |  350
 |  525
 |  1000
 |


The king value is often assigned a large constant such as 10000 centipaws, which is important to avoid king captures in certain implementations of [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation").




## Reciprocal piece values


Concerning a piece [controlling](Square_Control "Square Control") a [square](Squares "Squares"), its value of attack might be considered as [inverse proportional](https://en.wikipedia.org/wiki/Proportionality_%28mathematics%29#Inverse_proportionality) to its point value, which is an issue in aggregating of [mobility](Mobility "Mobility") or square control terms of different pieces.



## Samples


* [Material in SOMA](SOMA#Material "SOMA")
* [Piece Coding in Gambiet](Gambiet#PieceCoding "Gambiet")
* [Point Values in Komodo](Komodo#PointValues "Komodo")
* [Point Values in LL Chess](LL_Chess#PointValues "LL Chess")
* [Point Values in MicroChess](MicroChess#PointValues "MicroChess")
* [Point Values in Turochamp](Turochamp#EvaluationFeatures "Turochamp")


## See also


* [Experiments with Chess](Jens_Christensen#Experiments "Jens Christensen") by [Jens Christensen](Jens_Christensen "Jens Christensen") and [Richard Korf](Richard_Korf "Richard Korf")
* [Fixed Point Score](Score#FixedPoint "Score")
* [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis") by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev")
* [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function") by [Tomasz Michniewski](Tomasz_Michniewski "Tomasz Michniewski")


## Publications


* H. M. Taylor (**1876**). *[On the Relative Values of the Pieces in Chess](http://www.tandfonline.com/doi/abs/10.1080/14786447608639029#.UfEUGXePZlR)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Series 5, Vol. 1, pp. 221-229
* [Max Euwe](Max_Euwe "Max Euwe"), Hans Kramer (**1944, 1977**). *Het middenspel, deel 1-4*. Spectrum, Utrecht
* [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. Philosophical Magazine, Ser. 7, Vol. 41, No. 314 - March 1950, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Alan Turing](Alan_Turing "Alan Turing") (**1953**). ***Chess***. part of the collection *Digital Computers Applied to Games*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in *The Essential Turing*, [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
* [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
* [Jens Christensen](Jens_Christensen "Jens Christensen"), [Richard Korf](Richard_Korf "Richard Korf") (**1986**). *A Unified Theory of Heuristic Evaluation functions and Its Applications to Learning.* Proceedings of the [AAAI-86](http://www.aaai.org/Conferences/AAAI/aaai86.php), pp. 148-152, [pdf](http://www.aaai.org/Papers/AAAI/1986/AAAI86-023.pdf)
* [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1994**). *The Relative Value of the Pieces*. [Computer Chess Reports](Computer_Chess_Reports "Computer Chess Reports"), Vol. 5, No. 2, pp. 33
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1997**). *Learning Piece Values Using Temporal Differences*. [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1999**). *The System: A World Champion's Approach to Chess*. [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications), ISBN 1-901983-10-2
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning of Piece Values for Chess Variants.* Technical Report TUD–KE–2008-07, Knowledge Engineering Group, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ke.tu-darmstadt.de/publications/reports/tud-ke-2008-07.pdf)
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning the Piece Values for three Chess Variants*. [ICGA Journal, Vol. 31, No. 4](ICGA_Journal#31_4 "ICGA Journal")
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2011**). *[The Global Landscape of Objective Functions for the Optimization of Shogi Piece Values with a Game-Tree Search](http://link.springer.com/chapter/10.1007%2F978-3-642-31866-5_16)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13") » [Shogi](Shogi "Shogi")


## Forum Posts


### 1993 ...


* [deriving piece values from mobility](https://groups.google.com/d/msg/rec.games.chess/au2AlGf7T30/jgAq306Bix4J) by [Barney Pell](Barney_Pell "Barney Pell"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), August 09, 1993
* [Value of the pieces](https://groups.google.com/d/msg/rec.games.chess/efBhsZU3J1g/fC7rxV5yuycJ) by Joost de Heer, [rgc](Computer_Chess_Forums "Computer Chess Forums"), February 01, 1995 » [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
* [Chess in BASIC?](https://www.stmintz.com/ccc/index.php?id=25568) by [William H. Rogers](William_H._Rogers "William H. Rogers"), [CCC](CCC "CCC"), August 28, 1998 » [Basic](Basic "Basic")


### 2000 ...


* [A Piece Value Question](https://groups.google.com/d/msg/rec.games.chess.computer/DV6qvJnygxo/jJ0BS7AFYz4J) by laocmo, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 12, 2000
* [piece values](https://www.stmintz.com/ccc/index.php?id=339346) by Toni, [CCC](CCC "CCC"), December 30, 2003
* [Piece Values in the Endgame](https://www.stmintz.com/ccc/index.php?id=348493) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), February 11, 2004 » [Endgame](Endgame "Endgame")


### 2005 ...


* [Re: 2005 National Computer Chess Championships](http://www.chesschat.org//showpost.php?p=63437&postcount=10) by [Shaun Press](Shaun_Press "Shaun Press"), [Chess Chat](http://www.chesschat.org/archive/index.php/), July 17, 2005 » [NC3 2005](NC3_2005 "NC3 2005")
* [Relative Piece Values](http://www.talkchess.com/forum/viewtopic.php?t=27387) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), April 09, 2009


### 2010 ...


* [Stockfish Code ( Piece Value's)](http://www.talkchess.com/forum/viewtopic.php?t=41916) by Nolan Denson, [CCC](CCC "CCC"), January 10, 2012
* [Why Knight and (lone) Bishop are so nearly equal in value](http://www.talkchess.com/forum/viewtopic.php?t=45321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 25, 2012
* [What is the correct value of the pieces?](http://www.talkchess.com/forum/viewtopic.php?t=45512) by [Roberto Munter](Roberto_Munter "Roberto Munter"), [CCC](CCC "CCC"), October 10, 2012
* [The value of a pawn](http://www.talkchess.com/forum/viewtopic.php?t=47632) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 28, 2013


### 2015 ...


* [Piece Value - Human vs. Computer](http://www.talkchess.com/forum/viewtopic.php?t=56063) by Sean Evans, [CCC](CCC "CCC"), April 19, 2015
* [Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), April 30, 2015 » [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")
* [Pawn value estimation](http://www.talkchess.com/forum/viewtopic.php?t=56232) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 04, 2015


 [Re: Pawn value estimation](http://www.talkchess.com/forum/viewtopic.php?t=56232&start=24) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), May 09, 2015
* [Larry Kaufman, Math and "The Development of Chess Style](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=56427) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), May 19, 2015
* [Xiangqi piece value model](http://www.talkchess.com/forum/viewtopic.php?t=60303) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), May 29, 2016 » [Xiangqi](Chinese_Chess "Chinese Chess")
* [Approximating Stockfish's Evaluation by PSQTs](http://www.talkchess.com/forum/viewtopic.php?t=64972) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 23, 2017 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [Stockfish](Stockfish "Stockfish")
* ['ab-initio' piece values](http://www.talkchess.com/forum/viewtopic.php?t=66966) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 30, 2018 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [The Xiphos Material Evaluator](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68842) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 05, 2018 » [Schooner](Schooner "Schooner"), [Xiphos](Xiphos "Xiphos")


### 2020 ...


* [Estimating piece strength](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73765) by grandmastermac, [CCC](CCC "CCC"), April 26, 2020
* [How to calculate piece weights with logistic regression?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75267) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 01, 2020 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")
* [Evaluating piece value](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77379) by Jon Lawrance, [CCC](CCC "CCC"), May 25, 2021


## External Links


* [Chess piece relative value from Wikipedia](https://en.wikipedia.org/wiki/Chess_piece_relative_value)
* [Centipawn - WikiChess](http://chess.wikia.com/wiki/Centipawn)
* [About the Values of Chess Pieces](http://www.chessvariants.com/d.betza/pieceval/index.html) by [Ralph Betza](index.php?title=Ralph_Betza&action=edit&redlink=1 "Ralph Betza (page does not exist)")
* [The joys of chess – and the value of the pieces](http://en.chessbase.com/post/the-joys-of-che-and-the-value-of-the-pieces), [ChessBase News](ChessBase "ChessBase"), December 21, 2011 <a id="cite-note-19" href="#cite-ref-19">[19]</a> <a id="cite-note-20" href="#cite-ref-20">[20]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky"), [Points](https://en.wikipedia.org/wiki/File:Wassily_Kandinsky,_1920_-_Points.jpg), 1920, [Ohara Museum of Art](https://en.wikipedia.org/wiki/Ohara_Museum_of_Art), [Google Art Project](http://www.google.com/culturalinstitute/entity/%2Fm%2F0856z?projectId=art-project), [Wassily Kandinsky from Wikipedia](https://en.wikipedia.org/wiki/Wassily_Kandinsky)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. Philosophical Magazine, Ser. 7, Vol. 41, No. 314 - March 1950
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> H. M. Taylor (**1876**). *[On the Relative Values of the Pieces in Chess](http://www.tandfonline.com/doi/abs/10.1080/14786447608639029#.UfEUGXePZlR)*. [Philosophical Magazine](https://en.wikipedia.org/wiki/Philosophical_Magazine), Series 5, Vol. 1, pp. 221-229
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [H. S. M. Coxeter](Mathematician#Coxeter "Mathematician") (**1940**). *Mathematical Recreations and Essays*. from the [original](http://www.gutenberg.org/ebooks/26839) by [W. W. Rouse Ball](Mathematician#WWRouseBall "Mathematician"), [Macmillan](https://en.wikipedia.org/wiki/Macmillan_Publishers)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Influence Quantity of Pieces - Fibonacci Spiral](Influence_Quantity_of_Pieces#FibonacciSpiral "Influence Quantity of Pieces")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> see [Theoretical Attempt](Point_Value#TheoreticalAttempt "Point Value") {12, 14, 22, 40} \* 25 = {300, 350, 550, 1000}
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Max Euwe](Max_Euwe "Max Euwe"), Hans Kramer (**1944, 1977**). *Het middenspel, deel 1-4*. Spectrum, Utrecht
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. Philosophical Magazine, Ser. 7, Vol. 41, No. 314 - March 1950
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Alan Turing](Alan_Turing "Alan Turing") (**1953**). ***Chess***. part of the collection *Digital Computers Applied to Games*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in *The Essential Turing*, [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1999**). *The System: A World Champion's Approach to Chess*. [Gambit Publications](https://en.wikipedia.org/wiki/Gambit_Publications), ISBN 1-901983-10-2
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Chess piece value, the Hans Berliner's system from Wikipedia](https://en.wikipedia.org/wiki/Chess_piece_point_value#Hans_Berliner.27s_system)
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Larry Kaufman](Larry_Kaufman "Larry Kaufman") (**1999**). *[The Evaluation of Material Imbalances](https://www.chess.com/article/view/the-evaluation-of-material-imbalances-by-im-larry-kaufman)*. (first published in [Chess Life](https://en.wikipedia.org/wiki/Chess_Life) March 1999, on-line version edited by [Dan Heisman](Dan_Heisman "Dan Heisman"))
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [Re: 2005 National Computer Chess Championships](http://www.chesschat.org//showpost.php?p=63437&postcount=10) by [Shaun Press](Shaun_Press "Shaun Press"), [Chess Chat](http://www.chesschat.org/archive/index.php/), July 17, 2005 » [NC3 2005](NC3_2005 "NC3 2005")
18. <a id="cite-ref-18" href="#cite-note-18">[18]</a> [Re: What is the correct value of the pieces?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=487051&t=45512) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), October 10, 2012
19. <a id="cite-ref-19" href="#cite-note-19">[19]</a> [Christian Hesse](Christian_Hesse "Christian Hesse") (**2011**). *[The Joys of Chess - Heroes, Battles & Brilliancies](http://www.newinchess.com/The_Joys_of_Chess-p-953.html)*. ISBN: 978-90-5691-355-7, [New In Chess](https://en.wikipedia.org/wiki/New_In_Chess)
20. <a id="cite-ref-20" href="#cite-note-20">[20]</a> [Interesting article about the value of the pieces](http://www.talkchess.com/forum/viewtopic.php?t=41556) by Aloisio Ponti, [CCC](CCC "CCC"), December 22, 2011

**[Up one Level](Pieces "Pieces")**







 
