---
title: PieceSquare TablesPreprocessing
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Piece-Square Tables**



 [](http://www.artnet.com/magazineus/reviews/davis/davis11-1-05_detail.asp?picnum=2) [John Cage](Category:John_Cage "Category:John Cage"), Chess Pieces, ca. 1944 <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Piece-Square Tables**,  

a simple way to assign values to specific [pieces](Pieces "Pieces") on specific [squares](Squares "Squares"). A table is created for each piece of each [color](Color "Color"), and values assigned to each square. This scheme is fast, since the evaluation term from the piece square tables can be [incrementally updated](Incremental_Updates "Incremental Updates") as [moves](Moves "Moves") are [made](Make_Move "Make Move") and [unmade](Unmake_Move "Unmake Move") in the [search tree](Search_Tree "Search Tree"). Because of that speed, piece-square tables are of great help when conducting [lazy evaluation](Lazy_Evaluation "Lazy Evaluation").


The same technique can be used for a more subtle evaluation terms, instead of one fixed value for, say, an [isolated pawn](Isolated_Pawn "Isolated Pawn"). It is also possible to use piece-square tables for [move ordering](Move_Ordering "Move Ordering"), though [history heuristic](History_Heuristic "History Heuristic") tends to perform better. Some programs, like [Rebel](Rebel "Rebel"), use the combination of the two <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 






## Pre-processing


Older programs, running on slow hardware and reaching low depths, used an [oracle approach](Oracle "Oracle") to speed up their evaluation by initializing the piece-square tables at the [beginning of each search](Root "Root"), taking into account complex characteristics of position, influence of [pawn structure](Pawn_Structure "Pawn Structure"), distance to the enemy king etc <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Pre-processing, also dubbed **Pre Scan Heuristics** as applied in [Kittinger](David_Kittinger "David Kittinger") programs <a id="cite-note-4" href="#cite-ref-4">[4]</a>, most notably the [Super Constellation](Super_Constellation "Super Constellation") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, were used by [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [Richard Lang](Richard_Lang "Richard Lang") <a id="cite-note-7" href="#cite-ref-7">[7]</a>, [Don Dailey](Don_Dailey "Don Dailey"), who even developed a little language so that [Larry Kaufman](Larry_Kaufman "Larry Kaufman") could express evaluation concepts in a more natural way <a id="cite-note-8" href="#cite-ref-8">[8]</a>, [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") with [Nimzo 3](Nimzo "Nimzo"), and [Frans Morsch](Frans_Morsch "Frans Morsch") and [Mathias Feist](Mathias_Feist "Mathias Feist") with [Fritz 3](Fritz "Fritz"), to name a few, the latter even with user modifiable rules or tables. However, the idea already originated from the program [Tech](Tech "Tech") by [James Gillogly](James_Gillogly "James Gillogly") in the late 1960's <a id="cite-note-9" href="#cite-ref-9">[9]</a>.


With today's search depth this approach seems to be impractical, since the difference between the root and leaf position may be very big. There also might be a problem with re-using hash scores from the previous entries. About the only recent chess program that sticks with pre-processing for good or bad is [RomiChess](RomiChess "RomiChess") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>.



## Examples


Material and piece-square tables alone are enough for a program to play a semi-decent game of chess. Indeed, [Tomasz Michniewski](Tomasz_Michniewski "Tomasz Michniewski") advocated a method of testing requiring all the tested programs to have identical, simplistic evaluation function, so that only search and efficiency issues would influence the result. One such tournament has been carried out in Poland. [Ronald Friederich](Ronald_Friederich "Ronald Friederich") improved this approach using a [Tapered Eval](Tapered_Eval "Tapered Eval") and [Texel's tuning method](Texel%27s_Tuning_Method "Texel's Tuning Method") as applied in [RofChade](RofChade "RofChade") and [PeSTO](PeSTO "PeSTO").



* [Simplified Evaluation Function](Simplified_Evaluation_Function "Simplified Evaluation Function")
* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")


## See also


* [Center Distance](Center_Distance "Center Distance")
* [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
* [Evaluation in Rookie 2.0](Rookie#Evaluation "Rookie")
* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
* [Game Phases](Game_Phases "Game Phases")
* [Material](Material "Material")
* [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")
* [Oracle](Oracle "Oracle")
* [Space](Space "Space")
* [Tapered Eval](Tapered_Eval "Tapered Eval")


## Publications


* [Jack Good](Jack_Good "Jack Good") (**1968**). *A Five-Year Plan for Automatic Chess - Appendix F. The Value of the Pieces and Squares*. [Machine Intelligence Vol. 2](http://www.doc.ic.ac.uk/~shm/MI/mi2.html)
* [Don Beal](Don_Beal "Don Beal"), [Martin C. Smith](Martin_C._Smith "Martin C. Smith") (**1999**). *Learning Piece-Square Values using Temporal Differences.* [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
* [Jun Nagashima](Jun_Nagashima "Jun Nagashima"), [Masahumi Taketoshi](Masahumi_Taketoshi "Masahumi Taketoshi"), [Yoichiro Kajihara](Yoichiro_Kajihara "Yoichiro Kajihara"), [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2002**). *[An Efficient Use of Piece-Square Tables in Computer Shogi](http://ci.nii.ac.jp/naid/110006381103)*.
* [Sacha Droste](Sacha_Droste "Sacha Droste"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2008**). *Learning of Piece Values for Chess Variants.* Technical Report TUD–KE–2008-07, Knowledge Engineering Group, [TU Darmstadt](Darmstadt_University_of_Technology "Darmstadt University of Technology"), [pdf](http://www.ke.tu-darmstadt.de/publications/reports/tud-ke-2008-07.pdf)


## Forum Posts


### 1996 ...


* [Re:Rebel Transposition Table discussion](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/4e27d53cd9b6cc5e) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 18, 1996, *about clearing [TT](Transposition_Table "Transposition Table") if using a preprocessor*.
* [The Diep Home page (more correction needed)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d962cff95d967c3) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 21, 1997
* [Question about prescan and evaluating in Crafty](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d67609b6c2e3063d) by Willem Broekema, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 07, 1998
* [What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18179) by Howard Exner, [CCC](CCC "CCC"), May 07, 1998
* [Preprocessing vs leaf evaluating - any preprocessors left?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ce25565232355c61) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 05, 1998


### 2000 ...


* [Preprocessor blues?](https://www.stmintz.com/ccc/index.php?id=95525) by [Ernst Walet](index.php?title=Ernst_Walet&action=edit&redlink=1 "Ernst Walet (page does not exist)"), [CCC](CCC "CCC"), February 07, 2000
* [Re: What is Prescan Heuristics ??](https://www.stmintz.com/ccc/index.php?id=132894) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), October 13, 2000
* [Program settings (Re: Programmers Should Take A Cue From Chessmaster)](https://www.stmintz.com/ccc/index.php?id=304684) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), July 04, 2003 » [Sharper](Sharper "Sharper")
* [Pieze/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=21281) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), May 21, 2008
* [Determining values for piece-square tables.](http://www.talkchess.com/forum/viewtopic.php?t=29825) by [Mike Leany](Mike_Leany "Mike Leany"), [CCC](CCC "CCC"), September 21, 2009


### 2010 ...


* [dynamically modified evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=37191) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), December 20, 2010


**2011**



* [Move ordering by PST](http://www.talkchess.com/forum/viewtopic.php?t=38766) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), April 16, 2011 » [History Heuristic](History_Heuristic "History Heuristic"), [Move Ordering](Move_Ordering "Move Ordering"), [Onno](Onno "Onno")
* [Questions for BB about Rybka PST = Fruit PST](http://www.open-chess.org/viewtopic.php?f=5&t=1535) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 4, 2011 » [Rybka Controversy](Rybka_Controversy "Rybka Controversy")
* [PST Calculation](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22572) by [michiguel](Miguel_A._Ballicora "Miguel A. Ballicora"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 5, 2011
* [Fruit and Crafty Bishop PSTs](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22635) by [michiguel](Miguel_A._Ballicora "Miguel A. Ballicora"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 12, 2011 <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [A small detail about additive constants to PSTs](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22642) by [Trotsky](Chris_Whittington "Chris Whittington"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 13, 2011
* [Fruit 1.0 PST](http://www.open-chess.org/viewtopic.php?f=5&t=1552) by BB+ ([Mark Watkins](Mark_Watkins "Mark Watkins")), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 13, 2011
* [About PSQ tables](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22662) by [Richard Vida](Richard_Vida "Richard Vida"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 15, 2011
* [Take the Fruit Bishop tables...](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=22669) by [michiguel](Miguel_A._Ballicora "Miguel A. Ballicora"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), August 16, 2011
* [PST of Fruit 2.1 and Rybka 1.0 Beta](http://www.open-chess.org/viewtopic.php?f=5&t=1570) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 22, 2011


**2012**



* [Incremental or non-incremental PST evaluation calcs](http://www.talkchess.com/forum/viewtopic.php?t=42167) by [Mark Pearce](index.php?title=Mark_Pearce&action=edit&redlink=1 "Mark Pearce (page does not exist)"), [CCC](CCC "CCC"), January 26, 2012 » [Incremental Updates](Incremental_Updates "Incremental Updates")
* [Re: Some thoughts on QS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=475603&t=44507) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 25, 2012 » [Quiescence Search](Quiescence_Search "Quiescence Search")


**2013**



* [On history and piece square tables](http://www.talkchess.com/forum/viewtopic.php?t=48102) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), May 24, 2013 » [History Heuristic](History_Heuristic "History Heuristic")
* [PSQ tables depending on king sides, pawn patterns etc.](http://www.talkchess.com/forum/viewtopic.php?t=50294) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), December 01, 2013


**2014**



* [Piece/square table challenge](http://www.talkchess.com/forum/viewtopic.php?t=50840) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), January 09, 2014
* [SEE logic](http://www.talkchess.com/forum/viewtopic.php?t=51518) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), March 08, 2014 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [multi-dimensional piece/square tables](http://www.talkchess.com/forum/viewtopic.php?t=52861) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), July 04, 2014


 [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=7) by Tony P., [CCC](CCC "CCC"), January 28, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning")
### 2015 ...


* [about pst](http://www.talkchess.com/forum/viewtopic.php?t=57384) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), August 26, 2015
* [high values of pst](http://www.talkchess.com/forum/viewtopic.php?t=57575) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), September 09, 2015
* [pieces psqt](http://www.talkchess.com/forum/viewtopic.php?t=58231) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), November 11, 2015


**2016**



* [Sanity check on piece-value tables](http://www.talkchess.com/forum/viewtopic.php?t=61631) by [Stuart Riffle](Stuart_Riffle "Stuart Riffle"), [CCC](CCC "CCC"), October 06, 2016
* [Simple method for simple mates for programs without TBs](http://www.talkchess.com/forum/viewtopic.php?t=62257) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), November 25, 2016 » [KBNK Endgame](KBNK_Endgame "KBNK Endgame"), [Mop-up Evaluation](Mop-up_Evaluation "Mop-up Evaluation")


**2017**



* [Approximating Stockfish's Evaluation by PSQTs](http://www.talkchess.com/forum/viewtopic.php?t=64972) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 23, 2017 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Stockfish](Stockfish "Stockfish")


**2018**



* [Learning piece-square table](http://www.talkchess.com/forum/viewtopic.php?t=66588) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 13, 2018 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* ['ab-initio' piece values](http://www.talkchess.com/forum/viewtopic.php?t=66966) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 30, 2018 » [Point Value](Point_Value "Point Value")
* [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 28, 2018 » [RofChade](RofChade "RofChade"), [Tapered Eval](Tapered_Eval "Tapered Eval")


### 2020 ...


* [PST for FRC](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73865) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 07, 2020 » [Chess960](Chess960 "Chess960")
* [Using piece-square table score for move ordering](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74752) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), August 11, 2020 » [Move Ordering](Move_Ordering "Move Ordering")
* [Engine choosing between sets of piece/square tables](https://prodeo.actieforum.com/t120-engine-choosing-between-sets-of-piece-square-tables) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2020


**2021**



* [Piece square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76256) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), January 08, 2021
* [little fun with TSCP](https://prodeo.actieforum.com/t252-little-fun-with-tscp) by [nescitus](Pawel_Koziol "Pawel Koziol"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), February 12, 2021 » [TSCP](TSCP "TSCP"), [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
* [The PSTs of Carnivor](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76831) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 10, 2021
* [PST-only Evaluation for MinimalChess 0.4](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77089) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), April 15, 2021 » [MinimalChess](MinimalChess "MinimalChess")
* [Evaluating piece value](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77379) by Jon Lawrance, [CCC](CCC "CCC"), May 25, 2021 » [Point Value](Point_Value "Point Value")
* [Game Phase and tapered PSQT evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77546) by Jon12345, [CCC](CCC "CCC"), June 23, 2021 » [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
* [multi-PST for middle-game depend from kings positions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77667) by [Eugene Kotlov](index.php?title=Eugene_Kotlov&action=edit&redlink=1 "Eugene Kotlov (page does not exist)"), [CCC](CCC "CCC"), July 08, 2021
* [Just an untested idea](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77715) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 12, 2021 » [Automated Tuning](Automated_Tuning "Automated Tuning")


**2022**



* [Stuck trying to come up with my own PST values](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79401) by Kurt Peters, [CCC](CCC "CCC"), February 22, 2022
* [Re: Devlog of Leorik - A.k.a. how to tune high-quality PSTs from scratch (material values) in 20 seconds](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=127) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), March 28, 2022 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Leorik](Leorik "Leorik")


## External Links


* [Evaluation: Piece-Square Tables](http://home.hccnet.nl/h.g.muller/pcsqr.html) from [Micro-Max](Micro-Max "Micro-Max") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
* Cage. Music, art, chess - Film by Brian Brandt with [Margaret Leng Tan](https://en.wikipedia.org/wiki/Margaret_Leng_Tan) and [Larry List](https://www.linkedin.com/in/larry-list-937b888), [Noguchi Museum](https://en.wikipedia.org/wiki/Noguchi_Museum) <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a> <a id="cite-note-16" href="#cite-ref-16">[16]</a>, 2006, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [John Cage - Chess Pieces, Ca. 1944](http://www.artnet.com/magazineus/reviews/davis/davis11-1-05_detail.asp?picnum=2), Courtesy [The John Cage Trust](http://johncagetrust.blogspot.com/) from [artnet Magazine - We Are Duchampians](http://www.artnet.com/magazineus/reviews/davis/davis11-1-05.asp) by Ben Davis
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ed Schröder](Ed_Schroder "Ed Schroder") *How REBEL Plays Chess* as [pdf](http://members.home.nl/matador/Inside%20Rebel.pdf), see page 1,2 [Move Ordering](Move_Ordering "Move Ordering")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18181) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 07, 1998
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [PSH](http://www.schach-computer.info/wiki/index.php/PSH) from [Schachcomputer.info Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Novag Super Constellation](http://www.schach-computer.info/wiki/index.php/Novag_Super_Constellation) from [Schachcomputer.info - Wiki](http://www.schach-computer.info/wiki/index.php/Hauptseite_En) (German)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> "[This approach](Oracle#Donninger "Oracle") seems to have been invented by [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen") for his program [CXG Advanced Star Chess](CXG_Star_Chess#Advanced "CXG Star Chess")" from [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Some thoughts on QS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=475574&t=44507) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 25, 2012
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Some thoughts on QS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=475603&t=44507) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 25, 2012
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [David Kittinger](David_Kittinger "David Kittinger") and [Scott McDonald](Scott_McDonald "Scott McDonald") (**1984**). *Report from the U.S. Open*. [Computer Chess Digest Annual 1984](Computer_Chess_Reports "Computer Chess Reports") pp. 15-33
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18203) by [Ulrich Türke](Ulrich_T%C3%BCrke "Ulrich Türke"), [CCC](CCC "CCC"), May 08, 1998
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Re: What is "pre-processing"](https://www.stmintz.com/ccc/index.php?id=18213) by [Amir Ban](Amir_Ban "Amir Ban"), [CCC](CCC "CCC"), May 08, 1998
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Crafty accused of copying Fruit PST](http://www.talkchess.com/forum/viewtopic.php?t=40047) by William O, [CCC](CCC "CCC"), August 13, 2011
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Crafty \*NOT\* accused of copying Fruit PST](http://www.talkchess.com/forum/viewtopic.php?t=40085) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), August 17, 2011
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [The Imagery of Chess Revisited](https://shop.noguchi.org/imofchre.html)
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Discovering The Imagery of Chess featuring Larry List](https://www.youtube.com/watch?v=vegmCb9j4kE), 2017, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [The Imagery of Chess -Surrealism and Chess](http://www.edochess.ca/batgirl/Imagery_of_Chess3.html)

**[Up one level](Evaluation "Evaluation")**







 
