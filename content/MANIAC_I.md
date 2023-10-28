---
title: MANIAC I
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MANIAC I**


**MANIAC I**,  

the chess program on a [MANIAC I](https://en.wikipedia.org/wiki/MANIAC_I) (Mathematical Analyzer, Numerical Integrator, and Computer or Mathematical Analyzer, Numerator, Integrator, and Computer), the machine designed and build by a team around [John von Neumann](John_von_Neumann "John von Neumann") and [Nicholas Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis) at the [Los Alamos Scientific Laboratory](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"). The MANIAC I chess program was written in [1956](Timeline#1956 "Timeline") by a group of H-bomb researchers, [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam"), [Paul Stein](Paul_Stein "Paul Stein"), [Mark Wells](Mark_Wells "Mark Wells"), [James Kister](James_Kister "James Kister"), [William Walden](William_Walden "William Walden") and [John Pasta](John_Pasta "John Pasta"). Due to lack of computing power, only a chess variant with a reduced 6 x 6 board was implemented, without bishops, [double-step](Pawn_Push#DoublePush "Pawn Push") for pawns and [castling](Castling "Castling") , later called [Los Alamos Chess](index.php?title=Los_Alamos_Chess&action=edit&redlink=1 "Los Alamos Chess (page does not exist)").



### Contents


* [1 Photos](#photos)
* [2 Description](#description)
* [3 Quotes](#quotes)
	+ [3.1 Fred Guterl](#fred-guterl)
	+ [3.2 Roger Snodgrass](#roger-snodgrass)
* [4 Selected Games](#selected-games)
* [5 See also](#see-also)
* [6 Selected Publications](#selected-publications)
* [7 External Links](#external-links)
	+ [7.1 Chess Program](#chess-program)
	+ [7.2 Computer](#computer)
	+ [7.3 Misc](#misc)
* [8 References](#references)






 [](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f64c5ba) 
[Los Alamos](Los_Alamos_National_Laboratory "Los Alamos National Laboratory") scientists [Paul Stein](Paul_Stein "Paul Stein") (left) and [Nick Metropolis](https://en.wikipedia.org/wiki/Nicholas_Metropolis) playing chess with the MANIAC computer <a id="cite-note-1" href="#cite-ref-1">[1]</a>



## Description


**MANIAC I** performed a [brute-force](Brute-Force "Brute-Force") [Shannon Type A strategy](Type_A_Strategy "Type A Strategy"), pure [minimax](Minimax "Minimax"). During game play with 11,000 ops./sec, it searched 4 [plies](Ply "Ply") deep in about 12 minutes to find its best move. The program was written in 600 words of machine code. Its [evaluation](Evaluation "Evaluation") took [material](Material "Material") and [mobility](Mobility "Mobility") under account, both [incrementally updated](Incremental_Updates "Incremental Updates") during [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.



## Quotes


Quote from *Chronology of Computing* compiled by [David Singmaster](Mathematician#DSingmaster "Mathematician") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```
A group at Los Alamos, based on Kister, Stein, Ulam, Walden and Wells, follows up a brief Russian reference to a chess program for [BESM](https://en.wikipedia.org/wiki/BESM) <a id="cite-note-4" href="#cite-ref-4">[4]</a>. The Los Alamos group writes a program for the MANIAC I to play a reduced game of chess – using a 6 x 6 board without bishops. 

```

### Fred Guterl


Quote by Fred Guterl from *Silicon gambit* <a id="cite-note-5" href="#cite-ref-5">[5]</a> :




```
The government laboratory in Los Alamos, New Mexico, got hold of one of the first computers, MANIAC I, so that Ulam and the other H-bomb researchers wouldn't have to stay up nights solving their voluminous equations with pencil and paper. Ulam, who described himself modestly as a "fair" chess player, couldn't resist putting the machine to work on a project of somewhat less import to coldwar strategy. Together with physicist [Paul Stein](Paul_Stein "Paul Stein"), he wrote one of the first chess-playing programs. 

```

### Roger Snodgrass


Roger Snodgrass in *LANL: The Rest of the Story* on MANIAC and [Mark Wells](Mark_Wells "Mark Wells") <a id="cite-note-6" href="#cite-ref-6">[6]</a>




```
Among the interesting tidbits in Wells article are stories about a chess-playing program on MANIAC. MANIAC’s limited memory restricted a play to board that was six squares by six squares and no bishops...

```


```
“Even then,” he wrote, “moves averaged about 10 minutes for a two-move, look-ahead strategy.” “That quickly became three moves, four moves, five moves ahead,” Wells said Tuesday, adding the current capability was at least 12 moves ahead. 

```


```
His essay also includes an anecdote about a moment when the computer seemed to have a mind of its own. When Princeton physicist [Martin Kruskal](Mathematician#MartinKruskal "Mathematician") checkmated the MANIAC on the 38th move of a game, the machine responded with an illegal move. “We were dumbfounded for a while, until we traced the trouble and realized that the program had never been taught to resign,” Wells wrote. Facing no moves, the machine was stuck in a loop and the loop changed the program.

```


```
“You might call that a learning program,” he recalled. 

```

## Selected Games


MANIAC I played a game against a young lady who had learnt the game a week earlier. It was the first time a human had lost to a computer in a game of intellectual skill <a id="cite-note-7" href="#cite-ref-7">[7]</a>:




```

[Event "6x6 Los Alamos Chess"]
[Site "Los Alamos"]
[Date "1956.??.??"]
[Round "?"]
[White "MANIAC I"]
[Black "Human"]
[Result "1-0"]

1.d3 b4 2.Nf3 d4 3.b3 e4 4.Ne1 a4 5.bxa4 Nxa4 6.Kd2 Nc3 7.Nxc3 bxc3+ 8.Kd1 f4 
9.a3 Rb6 10.a4 Ra6 11.a5 Kd5 12.Qa3 Qb5 13.Qa2+ Ke5 14.Rb1 Rxa5 15.Rxb5 Rxa2 
16.Rb1 Ra5 17.f3 Ra4 18.fxe4 c4 19.Nf3+ Kd6 20.e5+ Kd5 21.exf6Q Nc5 22.Qf6xd4+ 
Kc6 23.Nf3-e5 1-0

```

## See also


* [History of Computer Chess](History "History")
* [Los Alamos Chess](index.php?title=Los_Alamos_Chess&action=edit&redlink=1 "Los Alamos Chess (page does not exist)")
* [Nils Barricelli](Nils_Barricelli "Nils Barricelli") - [The Birth of the Computer](Nils_Barricelli#Video "Nils Barricelli")


## Selected Publications


* [Paul Stein](Paul_Stein "Paul Stein"), [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam") (**1957**). *Experiments in chess on electronic computing machines*. Chess Review, 13 January 1957.
* [James Kister](James_Kister "James Kister"), [Paul Stein](Paul_Stein "Paul Stein"), [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam"), [William Walden](William_Walden "William Walden"), [Mark Wells](Mark_Wells "Mark Wells") (**1957**). *[Experiments in Chess](http://dl.acm.org/citation.cfm?id=320868.320877&coll=DL&dl=GUIDE&CFID=628969023&CFTOKEN=30690604)*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 4, No. 2
* [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1958**). *Chess Playing Programs and the Problem of Complexity*. IBM Journal of Research and Development, Vol. 4, No. 2, pp. 320-335. Reprinted (1963) in [Computers and Thought](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=6685) (eds. [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") and [Julian Feldman](Mathematician#JulianFeldman "Mathematician")), pp. 39-70. McGraw-Hill, [pdf](http://aitopics.org/sites/default/files/classic/Feigenbaum_Feldman/C&T-Newll-Shaw-Simon.pdf)
* [Paul Stein](Paul_Stein "Paul Stein") (**1986**). *[Experiments in Chess on Electronic Computing Machines: Some Early Efforts](http://link.springer.com/chapter/10.1007%2F978-1-4615-9819-0_7)*. in [Stanislaw Ulam](Stanislaw_Ulam "Stanislaw Ulam") (**1986**). *[Science, Computers, and People - From the Tree of Mathematics](http://link.springer.com/book/10.1007/978-1-4615-9819-0)*. [Birkhäuser](https://en.wikipedia.org/wiki/Birkh%C3%A4user)
* [Herbert L. Anderson](https://en.wikipedia.org/wiki/Herbert_L._Anderson) (**1986**). *Metropolis, Monte Carlo, and the MANIAC*. [Los Alamos Science](http://la-science.lanl.gov/), [pdf](http://www.fas.org/sgp/othergov/doe/lanl/pubs/00326886.pdf)


## External Links


### Chess Program


* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Silicon gambit](http://discovermagazine.com/1996/jun/silicongambit791) by [Fred Guterl](https://www.linkedin.com/pub/fred-guterl/2/28/417), [Discover](https://en.wikipedia.org/wiki/Discover_%28magazine%29), June 01, 1996
* [LANL: The Rest of the Story](http://lanl-the-rest-of-the-story.blogspot.de/2008/07/lanl-unable-to-release-history-report.html) by [Roger Snodgrass](https://www.linkedin.com/pub/roger-snodgrass/0/1a2/196), Los Alamos Monitor Editor, July 16, 2008
* [MANIAC I - Mensch, Los Alamos, 1956 - Wikipedia.de](http://de.wikipedia.org/wiki/Schachengine#John_von_Neumann) (German)


### Computer


* [MANIAC I from Wikipedia](https://en.wikipedia.org/wiki/MANIAC_I)
* [BRL Report 1961 - MANIAC I](http://www.ed-thelen.org/comp-hist/BRL61-m.html#MANIAC-I) <a id="cite-note-9" href="#cite-ref-9">[9]</a>


### Misc


* [maniac - Wiktionary](http://en.wiktionary.org/wiki/maniac)
* [mania - Wiktionary](http://en.wiktionary.org/wiki/mania)
* [Mania from Wikipedia](https://en.wikipedia.org/wiki/Mania)
* [Volker Kriegel](Category:Volker_Kriegel "Category:Volker Kriegel") & [Mild Maniac Orchestra](https://en.wikipedia.org/wiki/Mild_Maniac_Orchestra) - Bahia Next Year, [NDR Hamburg](https://en.wikipedia.org/wiki/Norddeutscher_Rundfunk) 1976, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Wolfgang Schlüter](http://de.wikipedia.org/wiki/Wolfgang_Schl%C3%BCter_%28Musiker%29), Volker Kriegel, [Curt Cress](Category:Curt_Cress "Category:Curt Cress"), [Hans Peter Ströer](http://de.wikipedia.org/wiki/Hans_Peter_Str%C3%B6er), [Nippy Noya](Category:Nippy_Noya "Category:Nippy Noya"), [Alan Skidmore](Category:Alan_Skidmore "Category:Alan Skidmore"), [Rainer Brüninghaus](https://en.wikipedia.org/wiki/Rainer_Br%C3%BCninghaus)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Los Alamos scientisits Paul Stern (left) and Nick Metropolis playing chess with the MANIAC computer](http://www.computerhistory.org/chess/full_record.php?iid=stl-431614f64c5ba), 1956, Courtesy of [Los Alamos National Laboratory](Los_Alamos_National_Laboratory "Los Alamos National Laboratory"), hosted by [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1958**). *Chess Playing Programs and the Problem of Complexity*. IBM Journal of Research and Development, Vol. 4, No. 2, pp. 320-335. Reprinted (1963) in [Computers and Thought](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=6685) (eds. [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") and [Julian Feldman](Mathematician#JulianFeldman "Mathematician")), pp. 39-70. McGraw-Hill, [pdf](http://aitopics.org/sites/default/files/classic/Feigenbaum_Feldman/C&T-Newll-Shaw-Simon.pdf), pp. 45 Table I Comparison of Current Chess Programs
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chronology of Computing](http://www.fbi.fh-darmstadt.de/fileadmin/vmi/chronologie/index.htm) compiled by [David Singmaster](Mathematician#DSingmaster "Mathematician")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> "There are two other explorations between 1951 and 1956 of which we are aware - a hand simulation by [F. Mosteller](Mathematician#Mosteller "Mathematician") and a Russian program for [BESM](https://en.wikipedia.org/wiki/BESM). Unfortunately, not enough information is available on either to talk about them, so we must leave a gap in the history between 1951 and 1956" - footnote 1 in [Allen Newell](Allen_Newell "Allen Newell"), [Cliff Shaw](Cliff_Shaw "Cliff Shaw"), [Herbert Simon](Herbert_Simon "Herbert Simon") (**1958**). *Chess Playing Programs and the Problem of Complexity*. IBM Journal of Research and Development, Vol. 4, No. 2, Reprinted (1963) in [Computers and Thought](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=6685) (eds. [Edward Feigenbaum](Edward_Feigenbaum "Edward Feigenbaum") and [Julian Feldman](Mathematician#JulianFeldman "Mathematician")), pp. 47. McGraw-Hill, [pdf](http://aitopics.org/sites/default/files/classic/Feigenbaum_Feldman/C&T-Newll-Shaw-Simon.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Silicon gambit](http://discovermagazine.com/1996/jun/silicongambit791) by [Fred Guterl](https://www.linkedin.com/pub/fred-guterl/2/28/417), [Discover](https://en.wikipedia.org/wiki/Discover_%28magazine%29), June 01, 1996
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [LANL: The Rest of the Story](http://lanl-the-rest-of-the-story.blogspot.de/2008/07/lanl-unable-to-release-history-report.html) by [Roger Snodgrass](https://www.linkedin.com/pub/roger-snodgrass/0/1a2/196), Los Alamos Monitor Editor, July 16, 2008
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [From the Z1 to the Singularity – Zuse's 100th birthday](http://en.chessbase.com/post/from-the-z1-to-the-singularity-zuse-s-100th-birthday/9) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [ChessBase News](ChessBase "ChessBase"), June 22, 2010
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> from [Martin H. Weik](http://www.martinhweik.com/) (**1961**). *[A Third Survey of Domestic Electronic Digital Computing Systems](http://www.ed-thelen.org/comp-hist/BRL61.html#TOC)*. Report No. 1115

**[Up one level](Engines "Engines")**







 
