---
title: Mobility
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Mobility**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bcb) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak"), Quite Clear <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**Mobility**,  

a measure of the number of choices ([legal moves](Legal_Move "Legal Move")) a player has in a given position. It is often used as a term in the [evaluation function](Evaluation_Function "Evaluation Function") of chess programs. It is based on the idea that the more choices you have at your disposal, the stronger your position. A study by [Eliot Slater](Eliot_Slater "Eliot Slater") of 350 tournament games in which the material balance was still even after the 20th move showed a definite correlation between a player's mobility and the number of games won <a id="cite-note-3" href="#cite-ref-3">[3]</a> . 



### Contents


* [1 Calculating Mobility](#calculating-mobility)
	+ [1.1 Safe Mobility](#safe-mobility)
	+ [1.2 Papa's Entropy](#papa.27s-entropy)
* [2 The Value of Reaching a Square](#the-value-of-reaching-a-square)
* [3 Mobility with Bitboards](#mobility-with-bitboards)
* [4 Progressive Mobility](#progressive-mobility)
* [5 Quotes](#quotes)
	+ [5.1 Alan Turing](#alan-turing)
	+ [5.2 Eliot Slater](#eliot-slater)
* [6 See also](#see-also)
* [7 Publications](#publications)
	+ [7.1 1949 ...](#1949-...)
	+ [7.2 1980 ...](#1980-...)
	+ [7.3 1990 ...](#1990-...)
	+ [7.4 2000 ...](#2000-...)
* [8 Forum Posts](#forum-posts)
	+ [8.1 1993 ...](#1993-...)
	+ [8.2 1995 ...](#1995-...)
	+ [8.3 2000 ...](#2000-...-2)
	+ [8.4 2005 ...](#2005-...)
	+ [8.5 2010 ...](#2010-...)
	+ [8.6 2015 ...](#2015-...)
	+ [8.7 2020 ...](#2020-...)
* [9 External Links](#external-links)
* [10 References](#references)






In computer programs, mobility is sometimes calculated differently than simply by summing up the number of [legal](Legal_Move "Legal Move") or [pseudo-legal moves](Pseudo-Legal_Move "Pseudo-Legal Move"). Often, it is done piece-by-piece, and the mobility bonus per possible move is not always the same for each type of piece (e.g., in the opening, the mobility of the [bishops](Bishop "Bishop") and [knights](Knight "Knight") is more important than that of the [rooks](Rook "Rook")). Sometimes forward mobility is scored higher than backward mobility, sometimes (in case of rooks) vertical mobility gets priority over horizontal mobility. Also, if a piece can move to the square of another friendly piece, sometimes that move is also counted - although it would not be a legal move, it is protecting the friendly piece, and therefore still serves a useful role.



### Safe Mobility


A couple of programs evaluates so-called **safe mobility** - counting only squares where a piece can move without being [En prise](En_prise "En prise"). This might be quite expensive, unless a program already keeps [incrementally updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"). In some cases, most notably in case of a knight, a middle-of-the-ground approach, not counting [squares controlled](Square_Control "Square Control") by enemy pawns, seems best.




### Papa's Entropy


Notes by [Tony Marsland](Tony_Marsland "Tony Marsland") on *[The World Computer-Chess Championship](WCCC_1974 "WCCC 1974")* by [Hayes](Jean_Hayes_Michie "Jean Hayes Michie") and [Levy](David_Levy "David Levy") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> :




```
[Freedom](Freedom "Freedom") and [Papa](Papa "Papa") both use mobility as their primary term in their [evaluation functions](Evaluation_Function "Evaluation Function"). As with [Wita](Awit "Awit"), both use the ratio of computer's moves / opponent moves. Papa and Wita also multiply by the ratio of the [squares controlled](Square_Control "Square Control") and Papa goes one step further and takes the [logarithm](https://en.wikipedia.org/wiki/Logarithm) of this product to form the "[entropy](Papa#Entropy "Papa")" of the position. The true merit of this entropy over the product ratio was not made clear, but it does ensure that in extreme situations the evaluation remains more closely bounded. 

```





## The Value of Reaching a Square


[Dan Heisman](Dan_Heisman "Dan Heisman") <a id="cite-note-7" href="#cite-ref-7">[7]</a> represents an attempt at mathematical abstraction applied to chess, introducing seven concepts as fundamental in analyzing a chess position: mobility, flexibility, vulnerability, [center control](Center_Control "Center Control"), piece coordination, time and speed. Heisman applies two [dichotomies](https://en.wikipedia.org/wiki/Dichotomy): *actual* versus *potential* and *local* versus *global*:





|  |  local
 |  global
 |
| --- | --- | --- |
|  actual
 |  Single movesfrom this position
 |  All reachable squaresfrom this position
 |
|  potential
 |  Single moveson an empty board
 |  All reachable squareson an empty board
 |


[Distance](Distance "Distance") as generalization of mobility and unification of Heisman's notions was introduced by [Robert Levinson](Robert_Levinson "Robert Levinson") and [Richard Snyder](Richard_Snyder "Richard Snyder") in the famous 1993 [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal") <a id="cite-note-8" href="#cite-ref-8">[8]</a> . Abstract and excerpt:




```
This article suggests a new approach to computer chess. A graph-theoretic representation of chess knowledge, uniformly based on a single mathematical abstraction, DISTANCE, is described. Most of the traditional forms of [chess knowledge](Knowledge "Knowledge"), it is shown, can be formalized in this new representation. In addition to comparing this approach to others, the article gives some experimental results and suggests how the new representation may be unified with existing approaches.

```


```
The DISTANCE idea is based on exploring a [piece's](Pieces "Pieces") mobility graph to determine what is close to and what is close to it. From a DISTANCE standpoint, [moves](Moves "Moves") on the [chess-board](Chessboard "Chessboard") are only considered good if they result in improved movement graphs for the mover's pieces and/or inferior ones for the opponent's pieces. Often, a good chess-player will move a piece, not to improve the attacking chances of that piece but rather the attacking chances of the piece behind it. 

```





## Mobility with Bitboards


For programs using [Bitboards](Bitboards "Bitboards"), piece mobility can be calculated very quickly either by [Population Count](Population_Count "Population Count") or a [SIMD-wise](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") kind of [weighted population count](SSE2#SSE2dotproduct "SSE2"). Similar to [Attacks by Occupancy Lookup](Sliding_Piece_Attacks#AttacksbyOccupancyLookup "Sliding Piece Attacks") to determine attack sets of sliding pieces, one may use pre-calculated population count or even center-weighted population count as a rough estimate on piece mobility. However it does not consider subsets of let say safe target squares. Most strong chess programs use a mobility calculation as part of the positional evaluation in some way. This approach is taken to the extremes in case of [OliThink](OliThink "OliThink") - a chess engine whose evaluation consists entirely of [material](Material "Material") balance and mobility.




## Progressive Mobility


[Fill approaches](Fill_Algorithms "Fill Algorithms"), like [Dumb7Fill](Dumb7Fill "Dumb7Fill") or [Kogge-Stone algorithm](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") are great to determine target sets one may reach in two or more moves, which population or weighted population might be considered as progressive mobility in some kind of positions <a id="cite-note-9" href="#cite-ref-9">[9]</a> . Another application in late [endings](Endgame "Endgame") is to determine whether a piece may [control a decisive stop or telestop](Control_of_Stop_and_Telestop "Control of Stop and Telestop") of a [passed pawn](Passed_Pawn "Passed Pawn") in time. [Path finding](All_Shortest_Paths "All Shortest Paths") algorithms for various pieces may be applied to find so called [Trajectories](Trajectory "Trajectory") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a> .



## Quotes


### Alan Turing


Quote by [Alan Turing](Alan_Turing "Alan Turing") on [Slater's](Eliot_Slater "Eliot Slater") 1950 paper *Statistics for the Chess Computer and the Factor of Mobility* <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>:




```
I wish to make two points concerning Dr. Slater's paper. I was greatly interested by the statistics provided, but fear that some people might draw invalid conclusions from them. It might for instance be thought that a good way of playing is to maximize one's mobility at one's next move, or perhaps to minimize that of one's opponent at his next move but one. It is evidently not feasible to foresee mobilities many moves ahead. Although the immediate mobility is a useful measure of the relative advantage of the players in normal play it by no means follows that it is wise to direct one's play to maximizing such a measure. To do so would be like taking a statistical analysis of the laundry of men in various positions and deciding, from the data collected, that an infallible method of getting ahead in life was to send a large number of shirts to the wash each week. 

```

### Eliot Slater


[Eliot Slater](Eliot_Slater "Eliot Slater") in reply <a id="cite-note-14" href="#cite-ref-14">[14]</a> :




```
Dr. Turing's argument by analogy what a naive laundry worker might conclude about ways of becoming rich really amounts to the suggestion that strategic advantage is the cause rather than the product of an advantage in mobility. I do not think that this can be accepted. An advantage in mobility usually appears in a game a number of moves before strategic advantage is detectable in other ways; it seems to be an essential aspect of what chess-players understand by "development"; and it supplies the decisive criterion of winning or losing. 

```

## See also


* [Blockade](Blockade "Blockade")
* [Center Control](Center_Control "Center Control")
* [Connectivity](Connectivity "Connectivity")
* [CPW-Engine\_eval](CPW-Engine_eval "CPW-Engine eval")
* [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
* [Pin](Pin "Pin")
* [Population Count](Population_Count "Population Count") of [Bitboards](Bitboards "Bitboards")


 [Mobility in Chess 4.6](CDC_Cyber#Mobility "CDC Cyber")
* [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Space](Space "Space")
* [Square Control](Square_Control "Square Control")
* [Strategy](Strategy "Strategy")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")


## Publications


### 1949 ...


* [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
* [Eliot Slater](Eliot_Slater "Eliot Slater") (**1950**). *[Statistics for the Chess Computer and the Factor of Mobility](http://www.eliotslater.org/index.php/chess/147-statistics-for-the-chess-computer-and-the-factor-of-mobility)*. Proceedings of the Symposium on Information Theory, London. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), pp. 113-117. Including the [transcript of a discussion](http://www.eliotslater.org/index.php/chess/159-discussion-on-the-above-paper-alan-turing-et-al-1950) with [Alan Turing](Alan_Turing "Alan Turing") and [Jack Good](Jack_Good "Jack Good")
* [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot") (**1965, 1978**). *Thought and Choice in Chess*. Mouton & Co Publishers, The Hague, The Netherlands. [amazon](http://www.amazon.com/gp/reader/9027979146/ref=sib_dp_pt#reader-link), [google](http://books.google.com/books?vid=ISBN9789053569986) <a id="cite-note-15" href="#cite-ref-15">[15]</a>


### 1980 ...


* [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of De Groot and Slater*. [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal")
* [Jan Eric Larsson](Jan_Eric_Larsson "Jan Eric Larsson") (**1987**). *Challenging that Mobility is Fundamental*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")


### 1990 ...


* [Dan Heisman](Dan_Heisman "Dan Heisman") (**1990, 1999, 2010, 2015**).*[The Positional Elements of Chess](http://www.danheisman.com/elements-of-positional-evaluation.html)*. Russell Enterprises
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1992**). *The Relation of Mobility, Strategy and the Mean Dead Rabbit in Chess*. [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
* [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *Distance: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
* [Jonathan Allen](index.php?title=Jonathan_Allen&action=edit&redlink=1 "Jonathan Allen (page does not exist)"), [Edward Hamilton](index.php?title=Edward_Hamilton&action=edit&redlink=1 "Edward Hamilton (page does not exist)"), [Robert Levinson](Robert_Levinson "Robert Levinson") (**1997**). *New Advances in Adaptive Pattern-Oriented Chess*. [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")


### 2000 ...


* [Mark Levene](Mark_Levene "Mark Levene"), [Trevor Fenner](Trevor_Fenner "Trevor Fenner") (**2001**). *The Effect of Mobility on Minimaxing of Game Trees with Random Leaf Values*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_(journal)), Vol. 130, No. 1, Review in [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#24_4 "ICGA Journal"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.21.6342&rep=rep1&type=pdf)
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**2006**). *Plättchen zählen*. [pdf](https://brigitte-godot.com/wp-content/uploads/2018/03/PlaettchenZaehlen.pdf) (German) » [Square Control](Square_Control "Square Control")
* [John L. Jerz](John_L._Jerz "John L. Jerz") (**2008, 2013**). *[A Proposed Heuristic for a Computer Chess Program](http://www.johnljerz.com/superduper/tlxdownloadsiteMAIN/id80.html)*.


## Forum Posts


### 1993 ...


* [deriving piece values from mobility](https://groups.google.com/d/msg/rec.games.chess/au2AlGf7T30/jgAq306Bix4J) by [Barney Pell](Barney_Pell "Barney Pell"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), August 09, 1993
* [Mobility Measure: Proposed Algorithm](https://groups.google.com/d/msg/rec.games.chess/6vwtkcF6sRU/4M3oOiDNYwgJ) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), September 23, 1993


### 1995 ...


* [Playing for position (mobility)](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/aeb03d37e406bf27) by S.Read, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 29, 1995


 [Re: Playing for position (mobility)](http://groups.google.com/group/rec.games.chess.computer/msg/6d07c745072dc611) by [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 02, 1995 » Mobility in [Zugzwang](Zugzwang_(Program) "Zugzwang (Program)")
* [Re: Incoporating chess knowledge in chess programs](https://groups.google.com/d/msg/rec.games.chess.computer/47bgYzU2kyQ/-dkD4FhigHYJ) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 28, 1996 » [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Mobility in evaluation functions- how much is it worth?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a589e61aa33f271) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 07, 1997
* [Mobility in eval](https://www.stmintz.com/ccc/index.php?id=12388) by [Willie Wood](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), November 24, 1997


### 2000 ...


* [Mobility in chess engines](https://groups.google.com/d/msg/rec.games.chess.computer/yZP38jTDewQ/WTcajkky4kgJ) by [Jean-François Gazet](index.php?title=Jean-Fran%C3%A7ois_Gazet&action=edit&redlink=1 "Jean-François Gazet (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 11, 2003
* [piece mobility?](https://www.stmintz.com/ccc/index.php?id=340896) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 08, 2004
* [An idea: Offensive and defensive mobility](https://www.stmintz.com/ccc/index.php?id=347567) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), February 06, 2004


### 2005 ...


* [Mobility](https://www.stmintz.com/ccc/index.php?id=404397) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), January 06, 2005
* [Mobility in Chess Evaluation Function at terminal-nodes](https://www.stmintz.com/ccc/index.php?id=474550) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), December 28, 2005
* [Re: CCC Retirement](https://www.stmintz.com/ccc/index.php?id=480043), [Robert Hyatt](Robert_Hyatt "Robert Hyatt") on Mobility, [CCC](CCC "CCC"), January 16, 2006
* [Magic and precomputation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6823) by [Onno Garms](Onno_Garms "Onno Garms"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), September 23, 2007
* [The limits of "Just-mobility-evaluation"](http://www.talkchess.com/forum/viewtopic.php?t=19273) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 29, 2008
* [Random number mobility scores](https://groups.google.com/d/msg/rec.games.chess.computer/Ab9uA1-8Hlw/UjT_JXTiHuIJ) by Guest, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2008 » [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [future mobility evaluation term](http://www.talkchess.com/forum/viewtopic.php?p=234786) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), December 01, 2008


### 2010 ...


* [mobility evaluation of stockfish](http://www.talkchess.com/forum/viewtopic.php?t=36307) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 09, 2010
* [Attack and mobility evaluation in chess variants](http://www.talkchess.com/forum/viewtopic.php?t=38084) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), February 15, 2011
* [Mobility eval](http://www.talkchess.com/forum/viewtopic.php?t=43527) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 01, 2012
* [static mobility(Q&D)](http://www.talkchess.com/forum/viewtopic.php?t=47497) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 13, 2013
* [Safe spatial mobility](http://www.talkchess.com/forum/viewtopic.php?t=48841) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), August 04, 2013
* [Re: Engine results: a surprise!](http://talkchess.com/forum/viewtopic.php?start=20&t=49687&topic_view=threads) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 18, 2013


### 2015 ...


* [mobility score](http://www.talkchess.com/forum/viewtopic.php?t=56360) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), May 15, 2015
* [Bishop Mobility ?](http://www.talkchess.com/forum/viewtopic.php?t=61284) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), August 31, 2016
* [Mobility Evaluation ?](http://www.talkchess.com/forum/viewtopic.php?t=61693) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 12, 2016
* [Safe mobility?](http://www.talkchess.com/forum/viewtopic.php?t=64645) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July, 18, 2017


### 2020 ...


* [Excluding squares from mobility](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75223) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 27, 2020


## External Links


* [Mobility from Wikipedia](https://en.wikipedia.org/wiki/Mobility)
* [Chess Strategy/Mobility - Wikibooks](https://en.wikibooks.org/wiki/Chess_Strategy/Mobility)
* [bitboard mobility](http://radagast.se/othello/bitmob.c) Copyright (c) 2003, [Gunnar Andersson](Gunnar_Andersson "Gunnar Andersson") » [Othello](Othello "Othello")
* [MadChess 3.0 Beta 5c5d4fc (Piece Mobility)](https://www.madchess.net/2020/02/01/madchess-3-0-beta-5c5d4fc-piece-mobility/) by [Erik Madsen](Erik_Madsen "Erik Madsen"), February 1, 2020 » [MadChess](MadChess "MadChess")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bcb), [Center for Holocaust & Genocide Studies](http://chgs.elevator.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> The mountain in the background looks like [Torghatten](https://en.wikipedia.org/wiki/Torghatten) near [Brønnøysund](https://en.wikipedia.org/wiki/Br%C3%B8nn%C3%B8ysund)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Eliot Slater](Eliot_Slater "Eliot Slater") (**1950**). *[Statistics for the Chess Computer and the Factor of Mobility](http://www.eliotslater.org/index.php/chess/147-statistics-for-the-chess-computer-and-the-factor-of-mobility)*. Proceedings of the Symposium on Information Theory, London. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), pp. 113-117. Including the [transcript of a discussion](http://www.eliotslater.org/index.php/chess/159-discussion-on-the-above-paper-alan-turing-et-al-1950) with [Alan Turing](Alan_Turing "Alan Turing") and [Jack Good](Jack_Good "Jack Good")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Jean E. Hayes](Jean_Hayes_Michie "Jean Hayes Michie"), [David Levy](David_Levy "David Levy") (**1976**). *[The world computer chess championship, Stockholm 1974](http://www.getcited.org/pub/101724802)*. University Press (Edinburgh) ISBN 0852242859
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [wita-awit#19-box2.pdf](http://webdocs.cs.ualberta.ca/~tony/Public/Awit-Wita-ComputerChess/Wita-base/WitaNotes/wita-awit%2319-box2.pdf) from [Wita Notes](http://webdocs.cs.ualberta.ca/~tony/Public/Awit-Wita-ComputerChess/Wita-base/WitaNotes/) by [Tony Marsland](Tony_Marsland "Tony Marsland")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Entropy in thermodynamics and information theory from Wikipedia](https://en.wikipedia.org/wiki/Entropy_in_thermodynamics_and_information_theory)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Dan Heisman](Dan_Heisman "Dan Heisman") (**1990, 1999, 2010**). *[Elements of Positional Evaluation](http://www.danheisman.com/elements-of-positional-evaluation.html)*. Russell Enterprises
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Robert Levinson](Robert_Levinson "Robert Levinson"), [Richard Snyder](Richard_Snyder "Richard Snyder") (**1993**). *DISTANCE: Toward the Unification of Chess Knowledge*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [John L. Jerz](John_L._Jerz "John L. Jerz") (**2008, 2013**). *[A Proposed Heuristic for a Computer Chess Program](http://www.johnljerz.com/superduper/tlxdownloadsiteMAIN/id80.html)*.
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Boris Stilman](Boris_Stilman "Boris Stilman") (**1994**). *A Linguistic Geometry of the Chess Model*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7"), [pdf draft](http://www.stilman-strategies.com/bstilman/boris_papers/Jour94_CHESS7.pdf)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Boris Stilman](Boris_Stilman "Boris Stilman") (**2000**). *Linguistic Geometry - From Search to Construction (Operations Research/Computer Science Interfaces Series)*. [amazon.com](http://www.amazon.com/Linguistic-Geometry-Construction-Operations-Interfaces/dp/0792377389/ref=sr_1_1?ie=UTF8&s=books&qid=1257674191&sr=1-1)
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Eliot Slater](Eliot_Slater "Eliot Slater") (**1950**). *[Statistics for the Chess Computer and the Factor of Mobility](http://www.eliotslater.org/index.php/chess/147-statistics-for-the-chess-computer-and-the-factor-of-mobility)*. Proceedings of the Symposium on Information Theory, London. Reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), pp. 113-117. Including the [transcript of a discussion](http://www.eliotslater.org/index.php/chess/159-discussion-on-the-above-paper-alan-turing-et-al-1950) with [Alan Turing](Alan_Turing "Alan Turing") and [Jack Good](Jack_Good "Jack Good")
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Conference on Information theory, 26-29 September 1950](http://www.turing.org.uk/sources/info50index.html)
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), pp. 115-117. Discussion on Dr. E. Slater's paper
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a> Quotes by [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot"): "... one of the important characteristics of a chess position is the number of possibilities available, i.e., the player's freedom of choice", as mentioned in [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**1987**). *How to Extract Relevant Knowledge from Grandmaster Games. Part 2: the Notion of Mobility, and the Work of De Groot and Slater*. [ICCA Journal, Vol. 10, No. 2](ICGA_Journal#10_2 "ICGA Journal"): "De Groot did not consider in-check positions, so imposing *De Groot Mobility* as a distinct norm"

**[Up one level](Evaluation "Evaluation")**







 
