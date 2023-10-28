---
title: Turochamp
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Turochamp**


**Turochamp**,  

a chess program by [Alan Turing](Alan_Turing "Alan Turing") and [David Champernowne](David_Champernowne "David Champernowne") developed in [1948](Timeline#1948 "Timeline") as chess playing algorithm, implemented as "paper machine". Since there was no machine yet that could execute the instructions, Turing acted as a human CPU requiring more than half an hour per move. One game from 1952 is recorded, which Turochamp lost to one of Turing's colleagues <a id="cite-note-1" href="#cite-ref-1">[1]</a>, [Alick Glennie](https://en.wikipedia.org/wiki/Alick_Glennie). It won an earlier game versus Champernowne's wife, a beginner at chess <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 


Turochamp incorporated important methods of [evaluation](Evaluation "Evaluation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and also the concepts of [selectivity](Selectivity "Selectivity") and [dead position](Quiescence_Search "Quiescence Search"), despite it is unclear how this was "implemented" in the game playing experiments. Champernowne [later said](David_Champernowne#Turochamp "David Champernowne") 'they were a bit slapdash about all this and must have made a number of slips since the arithmetic was extremely tedious with pencil and paper' <a id="cite-note-4" href="#cite-ref-4">[4]</a>. In a [CCC](CCC "CCC") forum post, [Frederic Friedel](Frederic_Friedel "Frederic Friedel") mentioned a [search](Search "Search") [depth](Depth "Depth") of up to three [plies](Ply "Ply") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Contents


* [1 Chess](#chess)
* [2 The Essential Turing](#the-essential-turing)
* [3 Evaluation Features](#evaluation-features)
* [4 Programming trials](#programming-trials)
* [5 Turochamp vs. Glennie](#turochamp-vs.-glennie)
* [6 Publications](#publications)
* [7 Forum Posts](#forum-posts)
* [8 External Links](#external-links)
* [9 References](#references)






In his 1953 paper 'Chess' in [Bowden's](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) *Faster Than Thought* <a id="cite-note-6" href="#cite-ref-6">[6]</a>, Turing defines [evaluation features](Evaluation "Evaluation"), and elaborates on [minimax strategy](Minimax "Minimax"), [variable look-ahead](Selectivity "Selectivity"), [quiescence](Quiescence_Search "Quiescence Search") and even [learning](Learning "Learning") as an early example of a [genetic algorithm](Genetic_Programming "Genetic Programming"). He does not explicitly mention the name Turochamp, but the 'Machine', and its game versus a human. [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) in *The Essential Turing*, 2004 <a id="cite-note-7" href="#cite-ref-7">[7]</a> on Turing's paper:




```
Turing says that the system of rules set out in 'Chess' is based on an '[introspective](https://en.wikipedia.org/wiki/Introspection) analysis' of his own [thought process](https://en.wikipedia.org/wiki/Thought) when playing (but with 'considerable simplifications'). His system anticipates much that has become standard in chess programming: the use of heuristics to guide the [search](Search "Search") through the [tree](Search_Tree "Search Tree") of possible [moves](Moves "Moves") and counter-moves; the use of [evaluation](Evaluation "Evaluation") rules which assign [numerical values](Score "Score"), indicative of strength or weakness, to [board configurations](Chess_Position "Chess Position"); the minimax strategy; and variable look-ahead whereby, instead of the consequences of every possible move being followed equally far, the 'more profitable moves are considered in greater detail than the less'. Turing also realized the necessity of using 'an entirely different system for the [end-game](Endgame "Endgame")'.

```


```
The [learning](Learning "Learning") procedure that Turing proposed in 'Chess' involves the machine trying out variations in its method of play - e.g. varying the numerical values that are assigned to the various pieces. The machine adopts any variation that leads to more satisfactory results. This procedure is an early example of a [genetic algorithm](Genetic_Programming "Genetic Programming"). 

```

## The Essential Turing


[Champernowne's](David_Champernowne "David Champernowne") quote on Turochamp from *The Essential Turing* <a id="cite-note-8" href="#cite-ref-8">[8]</a>:




```
 Most of our attention went to deciding which moves were to be followed up. My memory about this is infuriatingly weak, Captures had to be followed up at least to the point where no further captures was immediately possible. Check and forcing moves had to be followed further. We were particularly keen on the idea that whereas certain moves would be scorned as pointless and pursued no further others would be followed quite a long way down certain paths. In the actual experiment I suspect we were a bit slapdash about all this and must have made a number of slips since the arithmetic was extremely tedious with pencil and paper. Out general conclusion was that a computer should be fairly easy to programme to play a game of chess against a beginner and stand a fair chance of winning or least reaching a winning position.  

```





## Evaluation Features


<a id="cite-note-9" href="#cite-ref-9">[9]</a>



* [Point Values](Point_Value "Point Value") for [Material](Material "Material"): [Pawn](Pawn "Pawn")=1, [Knight](Knight "Knight")=3, [Bishop](Bishop "Bishop")=3.5, [Rook](Rook "Rook")=5, [Queen](Queen "Queen")=10
* [Mobility](Mobility "Mobility"): For the pieces other than Kings and pawns, add the square roots of the number of moves that the piece can make, counting a capture as two moves.
* [Piece safety](Connectivity "Connectivity"): If a Rook, Bishop, or Knight is defended once, add 1 point; add 1.5 points if it is defended twice.
* King mobility: Use the same method as above, but don’t count castling.
* [King safety](King_Safety "King Safety") : Deduct x points for a vulnerable King, with x being the number of moves that a Queen could move if it were on the same square as the one occupied by the King.
* [Castling](Castling "Castling"): When evaluating a move, add 1 point if castling is still possible after the move is made. Add another point if castling is immediately possible or if the castling move has just been performed.
* Pawn credit: Score 0.2 points for each square advanced, plus 0.3 points for each pawn defended by one or more non-pawns.
* [Checks](Check "Check") and mate threats: Score 1 point for the threat of mate and a half-point for a check.


## Programming trials


At the [University of Manchester](University_of_Manchester "University of Manchester"), Turing began programming Turochamp, as well as [Michie's](Donald_Michie "Donald Michie") and [Wylie's](Shaun_Wylie "Shaun Wylie") program [Machiavelli](Machiavelli "Machiavelli"), to run on a [Ferranti Mark 1](Ferranti_Mark_1 "Ferranti Mark 1") computer, but could not complete them <a id="cite-note-10" href="#cite-ref-10">[10]</a>. In 2004 [ChessBase](ChessBase "ChessBase") published a engine based on Turing's ideas, developed by [Mathias Feist](Mathias_Feist "Mathias Feist") with the help of [Ken Thompson](Ken_Thompson "Ken Thompson") <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>.




## Turochamp vs. Glennie


The mentioned game of Turochamp versus [Alick Glennie](https://en.wikipedia.org/wiki/Alick_Glennie), who wrote the [Autocode](https://en.wikipedia.org/wiki/Autocode) compiler for the [Manchester-Mark I](https://en.wikipedia.org/wiki/Manchester_Mark_1) computers. The game took several weeks <a id="cite-note-14" href="#cite-ref-14">[14]</a>.




```

[Event "Paper machine - Human"]
[Site "Manchester, UK"]
[Date "1952"]
[Round "?"]
[White "Turochamp"]
[Black "Alick Glennie"]
[Result "0-1"]

1.e4 e5 2.Nc3 Nf6 3.d4 Bb4 4.Nf3 d6 5.Bd2 Nc6 6.d5 Nd4 7.h4 Bg4 8.a4 Nxf3+ 9.gxf3 Bh5
10.Bb5+ c6 11.dxc6 0-0 12.cxb7 Rb8 13.Ba6 Qa5 14.Qe2 Nd7 15.Rg1 Nc5 16.Rg5 Bg6 17.Bb5 
Nxb7 18.0-0-0 Nc5 19.Bc6 Rfc8 20.Bd5 Bxc3 21.Bxc3 Qxa4 22.Kd2 Ne6 23.Rg4 Nd4 24.Qd3 Nb5 
25.Bb3 Qa6 26.Bc4 Bh5 27.Rg3 Qa4 28.Bxb5 Qxb5 29.Qxd6 Rd8 0-1

```

## Publications


* [Alan Turing](Alan_Turing "Alan Turing") (**1953**). *Chess*. part of the collection *Digital Computers Applied to Games*, in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), [Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719), a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in *The Essential Turing*, [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
* [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1)
* [Guy McCrossan Haworth](Guy_Haworth "Guy Haworth") (**2013**). *Turing, Kasparov and the Future*. [ICGA Journal, Vol. 36, No. 1](ICGA_Journal#36_1 "ICGA Journal")
* [David Levy](David_Levy "David Levy") (**2013**). *Alan Turing on Computer Chess*. in [S. Barry Cooper](Mathematician#SBCooper "Mathematician"), [Jan van Leeuwen](Mathematician#JvLeeuwen "Mathematician") (**2013**). *[Alan Turing: His Work and Impact](https://www.elsevier.com/books/alan-turing-his-work-and-impact/cooper/978-0-12-386980-7)*. [Elsevier Science](https://en.wikipedia.org/wiki/Elsevier), pp. 644-650
* [Garry Kasparov](Garry_Kasparov "Garry Kasparov"), [Frederic Friedel](Frederic_Friedel "Frederic Friedel") (**2018**). *Reconstructing Turing’s “paper machine”*. [ICGA Journal, Vol. 40, No. 2](ICGA_Journal#40_2 "ICGA Journal")


## Forum Posts


* [How did Alan Turing's program work?](https://www.stmintz.com/ccc/index.php?id=106953) by Pete Galati, [CCC](CCC "CCC"), April 20, 2000
* [New Chessbase Engine called "Turing"](https://www.stmintz.com/ccc/index.php?id=326962) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer"), [CCC](CCC "CCC"), November 12, 2003 <a id="cite-note-15" href="#cite-ref-15">[15]</a>
* [Alan Turing's 1950 Chess Computer Program](http://www.hiarcs.net/forums/viewtopic.php?t=8578) by fourthirty, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), September 05, 2017


## External Links


* [Turochamp from Wikipedia](https://en.wikipedia.org/wiki/Turochamp)
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-16" href="#cite-ref-16">[16]</a>
* [Computer und Schach: "Die goldene Gans, die niemals schnattert"](http://www.spiegel.de/netzwelt/gadgets/computer-und-schach-die-goldene-gans-die-niemals-schnattert-a-273665.html) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [Spiegel Online](https://en.wikipedia.org/wiki/Spiegel_Online), November 12, 2003 (German) <a id="cite-note-17" href="#cite-ref-17">[17]</a>
* [Alan Turing](http://www.chessbase.de/nachrichten.asp?newsid=3245) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [ChessBase Nachrichten](ChessBase "ChessBase"), June 07, 2004 (German)
* [Anmerkungen zur Programmierung der Turing-Engine](http://www.chessbase.de/spotlight/spotlight2.asp?id=15) by [Mathias Feist](Mathias_Feist "Mathias Feist"), [ChessBase Spotlights](ChessBase "ChessBase") (German, with original article 'Chess' by Alan Turing) (no longer available)
* [An “easy” engine for the Fritz/Rybka interface](http://uscfsales.wordpress.com/2011/07/01/an-%E2%80%9Ceasy%E2%80%9D-engine-for-the-fritzrybka-interface/) by [Steve Lopez](index.php?title=Steve_Lopez&action=edit&redlink=1 "Steve Lopez (page does not exist)"), [USCFSales](http://uscfsales.wordpress.com/), July 01, 2011
* [The Alan Turing Centenary Conference Manchester UK](http://www.turing100.manchester.ac.uk/), June 22-25, 2012, hosted by the [University in Manchester](University_of_Manchester "University of Manchester")
* [Kasparov on Alan Turing and his 'Paper Machine'](http://en.chessbase.com/post/kasparov-on-alan-turing-and-his-paper-machine-), [ChessBase News](ChessBase "ChessBase"), June 23, 2012
* [Alan Turing's 60-year-old chess program takes on Garry Kasparov | The Verge](http://www.theverge.com/2012/6/26/3119022/alan-turing-60-year-old-chess-program-garry-kasparov), by [Bryan Bishop](https://en.wikipedia.org/wiki/Bryan_Bishop), June 26, 2012
* [Kasparov versus Turing](http://www.cs.manchester.ac.uk/aboutus/news/2012/25-6-12_kasparov/), June 25, 2012, [Garry Kasparov](Garry_Kasparov "Garry Kasparov") and [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-18" href="#cite-ref-18">[18]</a>


 
* [In 1950, Alan Turing Created a Chess Computer Program That Prefigured A.I.](http://www.history.com/news/in-1950-alan-turing-created-a-chess-computer-program-that-prefigured-a-i) by [Martin Stezano](http://www.history.com/news/author/martinstezano), [History in the Headlines](http://www.history.com/), August 29, 2017 <a id="cite-note-19" href="#cite-ref-19">[19]</a>
* [The History of Computer Chess - Part 2 - Turochamp](https://www.chess.com/blog/Ginger_GM/the-history-of-computer-chess-part-2-turochamp) by [Simon Williams](https://en.wikipedia.org/wiki/Simon_Williams_(chess_player)), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), July 15, 2019


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [A short history of computer chess](http://www.chessbase.com/columns/column.asp?pid=102) from [ChessBase](ChessBase "ChessBase")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Chapter 16, Introduction on 'Chess', in [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1), [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [David Champernowne (1912-2000)](http://ilk.uvt.nl/icga/journal/contents/content23-4.htm#DAVID%20CHAMPERNOWNE), [ICGA Journal, Vol. 23, No. 4](ICGA_Journal#23_4 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1), [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: How did Alan Turing's program work?](https://www.stmintz.com/ccc/index.php?id=107112) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [CCC](CCC "CCC"), April 22, 2000
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Alan Turing](Alan_Turing "Alan Turing") (**1953**). ***Chess***. part of the collection *Digital Computers Applied to Games*. in [Bertram Vivian Bowden](https://en.wikipedia.org/wiki/B._V._Bowden,_Baron_Bowden) (editor), *[Faster Than Thought](http://www.computinghistory.org.uk/cgi-bin/sitewise.pl?act=det&p=10719)*, a symposium on digital computing machines, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), reprinted 2004 in Chapter 16 of [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1), [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1), [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> Chapter 16, Introduction on 'Chess', in [Alan Turing](Alan_Turing "Alan Turing"), [Jack Copeland](https://en.wikipedia.org/wiki/Jack_Copeland) (editor) (**2004**). *The Essential Turing, Seminal Writings in Computing, Logic, Philosophy, Artificial Intelligence, and Artificial Life plus The Secrets of Enigma*. [Oxford University Press](https://en.wikipedia.org/wiki/Oxford_University_Press), [amazon](http://www.amazon.com/Essential-Turing-Philosophy-Artificial-Intelligence/dp/0198250800/ref=sr_1_1?s=books&ie=UTF8&qid=1324659595&sr=1-1), [google books](http://books.google.com/books?id=RSkxnKlv1D4C&lpg=PP882&ots=VOWmiIm_lD&dq=Turochamp%2C%20chess&pg=PP881#v=onepage&q&f=true)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [An “easy” engine for the Fritz/Rybka interface](http://uscfsales.wordpress.com/2011/07/01/an-%E2%80%9Ceasy%E2%80%9D-engine-for-the-fritzrybka-interface/) by [Steve Lopez](index.php?title=Steve_Lopez&action=edit&redlink=1 "Steve Lopez (page does not exist)"), [USCFSales](http://uscfsales.wordpress.com/), July 01, 2011
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Chronology of Computing](http://www.fbi.fh-darmstadt.de/fileadmin/vmi/chronologie/index.htm) compiled by [David Singmaster](Mathematician#DSingmaster "Mathematician")
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Computer und Schach: "Die goldene Gans, die niemals schnattert"](http://www.spiegel.de/netzwelt/gadgets/computer-und-schach-die-goldene-gans-die-niemals-schnattert-a-273665.html) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [Spiegel Online](https://en.wikipedia.org/wiki/Spiegel_Online), November 12, 2003 (German)
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Alan Turing](http://www.chessbase.de/nachrichten.asp?newsid=3245) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [ChessBase Nachrichten](ChessBase "ChessBase"), June 07, 2004 (German)
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [An “easy” engine for the Fritz/Rybka interface](http://uscfsales.wordpress.com/2011/07/01/an-%E2%80%9Ceasy%E2%80%9D-engine-for-the-fritzrybka-interface/) by [Steve Lopez](index.php?title=Steve_Lopez&action=edit&redlink=1 "Steve Lopez (page does not exist)"), [USCFSales](http://uscfsales.wordpress.com/), July 01, 2011
14. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Alan Turing vs Alick Glennie (1952)](http://www.chessgames.com/perl/chessgame?gid=1356927) from [chessgames.com](http://www.chessgames.com/index.html)
15. <a id="cite-ref-15" href="#cite-note-15">[15]</a>  [Computer und Schach: "Die goldene Gans, die niemals schnattert"](http://www.spiegel.de/netzwelt/gadgets/computer-und-schach-die-goldene-gans-die-niemals-schnattert-a-273665.html) by [André Schulz](https://en.chessbase.com/author/andre-schulz), [Spiegel Online](https://en.wikipedia.org/wiki/Spiegel_Online), November 12, 2003 (German)
16. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015
17. <a id="cite-ref-17" href="#cite-note-17">[17]</a> [New Chessbase Engine called "Turing"](https://www.stmintz.com/ccc/index.php?id=326962) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer"), [CCC](CCC "CCC"), November 12, 2003
18. <a id="cite-ref-18" href="#cite-note-18">[18]</a> [Turochamp (Computer) vs Garry Kasparov (2012)](http://www.chessgames.com/perl/chessgame?gid=1670503) from [chessgames.com](http://www.chessgames.com/index.html)
19. <a id="cite-ref-19" href="#cite-note-19">[19]</a> [Alan Turing's 1950 Chess Computer Program](http://www.hiarcs.net/forums/viewtopic.php?t=8578) by fourthirty, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), September 05, 2017

**[Up one Level](Engines "Engines")**







 
