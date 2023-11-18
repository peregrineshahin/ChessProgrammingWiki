---
title: RattateChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RattateChess**



[ Nosferatu Fountain <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**RattateChess**, (RattateChess Nosferatu)  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Maurizio Monge](Maurizio_Monge "Maurizio Monge"), written in [C++](Cpp "Cpp"), released under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation"), first announced in November 2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
RattateChess played a strong [CIPS 2007](CIPS_2007 "CIPS 2007"), becoming fourth with 4/6. RattateChess **Nosferatu** played the [I.G.W.T. 2013](IGWT_2013 "IGWT 2013"), where it lost from [Gaviota](Gaviota "Gaviota") in the round of sixteen.
RattateChess is announced to be superseded by its successor under development, [RattatAjedrez](index.php?title=RattatAjedrez&action=edit&redlink=1 "RattatAjedrez (page does not exist)"), written in much cleaner code, with focus on [automatic tuning](Automated_Tuning "Automated Tuning") of [evaluation](Evaluation "Evaluation") features and [search](Search "Search") parameters <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Search


Using a [0x88](0x88 "0x88") board representation, RattateChess performs [NegaScout](NegaScout "NegaScout") [alpha-beta](Alpha-Beta "Alpha-Beta") with [null move pruning](Null_Move_Pruning "Null Move Pruning") and [threat extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [transposition table](Transposition_Table "Transposition Table") and [IID](Internal_Iterative_Deepening "Internal Iterative Deepening") inside a [fractional ply](Depth#FractionalPlies "Depth") [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with 1/100 ply resolution. 
Beside [quiescence search](Quiescence_Search "Quiescence Search"), further [selectivity](Selectivity "Selectivity") is realized by [history reductions](Late_Move_Reductions "Late Move Reductions"), [futility pruning](Futility_Pruning "Futility Pruning"), [recapture extensions](Recapture_Extensions "Recapture Extensions"), and [single-reply extension](One_Reply_Extensions "One Reply Extensions").



### Evaluation


The [evaluation](Evaluation "Evaluation") considers [material](Material "Material") through [piece-square tables](Piece-Square_Tables "Piece-Square Tables") for knights and bishops, [bishop pair](Bishop_Pair "Bishop Pair"), [pawn structure](Pawn_Structure "Pawn Structure") addressing [backward](Backward_Pawn "Backward Pawn"), [isolated](Isolated_Pawn "Isolated Pawn"), [doubled](Doubled_Pawn "Doubled Pawn") and [passed pawns](Passed_Pawn "Passed Pawn"), [development](Development "Development"), [square control](Square_Control "Square Control") and [center control](Center_Control "Center Control"), [rook on (semi) open files](Rook_on_Open_File "Rook on Open File") and [seventh rank](Rook_on_Seventh "Rook on Seventh"), and [king safety](King_Safety "King Safety") through (half) open neighbored files, and [king piece](King_Safety#KingTropism "King Safety") and piece attack tropism.



## See also


* [RattatAjedrez](index.php?title=RattatAjedrez&action=edit&redlink=1 "RattatAjedrez (page does not exist)")


## Forum Posts


* [New Chess Engine ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39916&p=152540) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 13, 2002
* [Rattatechess 0.666 alpha windows build](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=3646&p=18472) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 09, 2005
* [Rattatechess new version and website](http://www.talkchess.com/forum/viewtopic.php?t=32879) by [Alex Brunetti](Alex_Brunetti "Alex Brunetti"), [CCC](CCC "CCC"), February 24, 2010


## External Links


### Chess Engine


* [Public Git Hosting - rattatechess.git/summary](https://repo.or.cz/w/rattatechess.git)
* [RattatAjedrez](https://sites.google.com/site/rattatajedrez/)
* [Index of /chess/engines/Jim Ablett/RATTATECHESS](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/RATTATECHESS/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/32 BIT/rattatechess-nosferatu](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/32%20BIT/rattatechess-nosferatu/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [RattateChess 1.0 Nosferatu](https://ccrl.chessdom.com/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=RattateChess%201.0%20Nosferatu) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Rat from Wikipedia](https://en.wikipedia.org/wiki/Rat)
* [Rattata - Wikipedia.it](http://it.wikipedia.org/wiki/Rattata)
* [Rattata - List of Pokémon - Wikipedia](https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon_%281%E2%80%9351%29#Rattata)


### Nosferatu


* [Nosferatu (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Nosferatu_%28disambiguation%29)
* [Nosferatu (word) from Wikipedia](https://en.wikipedia.org/wiki/Nosferatu_%28word%29)
* [John Zorn](Category:John_Zorn "Category:John Zorn") - Renfield, [Nosferatu](https://en.wikipedia.org/wiki/Nosferatu_(John_Zorn_album)) (2012), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Rob Burger](https://en.wikipedia.org/wiki/Rob_Burger), [Bill Laswell](https://en.wikipedia.org/wiki/Bill_Laswell), [Kevin Norton](https://en.wikipedia.org/wiki/Kevin_Norton)
 
* [Nosferatu](https://en.wikipedia.org/wiki/Nosferatu) A Symphony of Horror by [F. W. Murnau](https://en.wikipedia.org/wiki/F._W._Murnau) 1922, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 based on [Bram Stoker's](https://en.wikipedia.org/wiki/Bram_Stoker) novel [Dracula](https://en.wikipedia.org/wiki/Dracula). [Max Schreck](https://en.wikipedia.org/wiki/Max_Schreck) as [Count Orlok](https://en.wikipedia.org/wiki/Count_Orlok)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Image by Joergsam, September 2011, [Filmpark Babelsberg](https://en.wikipedia.org/wiki/Babelsberg_Studio), [Nosferatu – Eine Symphonie des Grauens - Wikipedia.de](https://de.wikipedia.org/wiki/Nosferatu_%E2%80%93_Eine_Symphonie_des_Grauens), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [New Chess Engine ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39916&p=152540) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 13, 2002
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [RattatAjedrez](https://sites.google.com/site/rattatajedrez/)

**[Up one level](Engines "Engines")**







 
