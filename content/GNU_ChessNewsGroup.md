---
title: GNU ChessNewsGroup
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GNU Chess**

\[ A Bold GNU Head <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**GNU Chess**,

the [open source chess engine](Category:Open_Source "Category:Open Source") of the [Free Software Foundation](Free_Software_Foundation "Free Software Foundation"). GNU Chess was initially written by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft") in the mid 80s, joined by [John Stanback](John_Stanback "John Stanback") who contributed his [own code](SCP "SCP") to GNU Chess 2 and 3 which was laboriously and meticulously well-written <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Dozens of developers have enhanced GNU Chess over the times. Version 5 was a complete rewrite by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), incorporating his chess program [Cobalt](Cobalt "Cobalt") and Cracraft's [Gazebo](Gazebo "Gazebo") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") is the primary author of GNU Chess 6, based on [Fruit 2.1](Fruit "Fruit") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Fidelity Match

In 1990, GNU Chess 1.55 with [Hans Eric Sandström's](index.php?title=Hans_Eric_Sandstr%C3%B6m&action=edit&redlink=1 "Hans Eric Sandström (page does not exist)") fast [move generator](Table-driven_Move_Generation#GNUChess "Table-driven Move Generation") defeats [Fidelity](Fidelity "Fidelity") in a 10 game match <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++
A 10 game match was conducted between GNU Chess 1.55 running on a [Sun](index.php?title=Sun_Microsystems&action=edit&redlink=1 "Sun Microsystems (page does not exist)") [SPARCstation-1](SPARCstation "SPARCstation") and the strong commercial chess machine Fidelity Mach 3. Fidelity Mach 3 is officially rated USCF 2265 (2200 is master). Most observers acknowledge it is a true master. The match result was 7-3 in GNU's favor. After various corrections, we arrive at a putative rating of around 2330 (strong master) for GNU Chess 1.55 on this machine. This result was most unexpected since prior versions of GNU Chess had scored no more than 3 points out of 10 against the Mach 3. The big leap appears to come from: (1) the inclusion of Hans Eric Sandstrom's fast move generator and (2) the Sparcstation-1, which is (apparently) particularly suited to speedy chess processing. Minor modifications to the book, draw factor, and thinking on opponent's time have also helped. Please remember this rating is based on a short match result. Certain moves GNU Chess plays are clearly non-master in quality. Computer masters generally achieve their strength through accuracy of [tactics](Tactics "Tactics"), not subtle positional moves. 

```

## Authors

## Primary

- [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), Versions 1, 2, 5
- [John Stanback](John_Stanback "John Stanback"), Versions 2, 3, 4
- [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), Version 5
- [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), Version 6

## Contributors

- [Jim Aspnes](index.php?title=Jim_Aspnes&action=edit&redlink=1 "Jim Aspnes (page does not exist)") » [ACM 1987](ACM_1987 "ACM 1987")
- [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos")
- [Lukas Geyer](index.php?title=Lukas_Geyer&action=edit&redlink=1 "Lukas Geyer (page does not exist)")
- [Hans Eric Sandström](index.php?title=Hans_Eric_Sandstr%C3%B6m&action=edit&redlink=1 "Hans Eric Sandström (page does not exist)")
- [Jay Scott](Jay_Scott "Jay Scott") » [ACM 1987](ACM_1987 "ACM 1987")
- [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
- [Simon Waters](index.php?title=Simon_Waters&action=edit&redlink=1 "Simon Waters (page does not exist)")

## See also

- [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [Cobalt](Cobalt "Cobalt")
- [Free Software Foundation](Free_Software_Foundation "Free Software Foundation")
- [Gazebo](Gazebo "Gazebo")
- [GNOME Chess](index.php?title=GNOME_Chess&action=edit&redlink=1 "GNOME Chess (page does not exist)")
- [NeuroChess](NeuroChess "NeuroChess")
- [SCP](SCP "SCP")
- [Table-driven Move Generation](Table-driven_Move_Generation "Table-driven Move Generation")
- [WinBoard](WinBoard "WinBoard")
- [XBoard](XBoard "XBoard")

## Publications

- T.M. Balajee, Adithya Udupa, Anil Kumar, D. Namratha (**2009**). *[Aggrandizement of Board Games’ Performance on Multi-core Systems: Taking GNU-Chess as a prototype](http://software.intel.com/en-us/articles/aggrandizement-of-board-games-performance-on-multi-core-systems-taking-gnu-chess-as-a-prototype/)*. [BMS College of Engineering](https://en.wikipedia.org/wiki/B.M.S._College_of_Engineering), Faculty mentor: Professor [Ashok Kumar](http://de.slideshare.net/ashokkumars75), [Intel® Developer Zone](http://software.intel.com/en-us) » [Parallel Search](Parallel_Search "Parallel Search")
- [Tomohiko Mitsuta](index.php?title=Tomohiko_Mitsuta&action=edit&redlink=1 "Tomohiko Mitsuta (page does not exist)"), [Lothar M. Schmitt](index.php?title=Lothar_M._Schmitt&action=edit&redlink=1 "Lothar M. Schmitt (page does not exist)") (**2010**). *[Optimizing the Performance of GNU-chess with a Genetic Algorithm](http://dl.acm.org/citation.cfm?id=1994517)*. [HC 2010](http://www.informatik.uni-trier.de/~ley/db/conf/hcce/hc2010.html#MitsutaS10), [pdf](http://www.wlu.ca/science/physcomp/kotsireas/468/RAP_DStu.pdf) » [Genetic Algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming")

## Forum Posts

## 1989

- [Changes to gnuchess1.52](http://groups.google.com/group/gnu.chess/browse_frm/thread/b6421a28fcffea8b) by [Tom Vijlbrief](Tom_Vijlbrief "Tom Vijlbrief"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), December 8, 1989

## 1990 ...

- [GNU Chess 1.55 ready](http://groups.google.com/group/gnu.chess/browse_frm/thread/6328395dfadd7b08) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 2, 1990
- [GNU Chess 1.55 vs. Fidelity Mach 3](http://groups.google.com/group/gnu.chess/msg/583f6ed4f648bf90) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 3, 1990
- [gnuchess.book in Lisp](http://groups.google.com/group/gnu.chess/browse_frm/thread/329b9401059f679b) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 23, 1990
- [Re: IBM PC front end for GNU chess](http://groups.google.com/group/gnu.chess/browse_frm/thread/f2cc2aff75c006bc) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), December 17, 1990
- [Help needed -- can't compile xchess](http://groups.google.com/group/gnu.chess/browse_frm/thread/42211ed6f4cc7dce) by [Heinz Herbeck](Heinz_Herbeck "Heinz Herbeck"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 17, 1992
- [Post information from Gnuchess 4.0](http://groups.google.com/group/gnu.chess/browse_frm/thread/d5a26047ebfac90d) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 12, 1992
- [GNU Chess wins London computer chess tourney](http://groups.google.com/group/gnu.chess/browse_frm/thread/09394d3e9b22b252) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), August 17, 1992 » [UPCCC 1992](UPCCC_1992 "UPCCC 1992")
- [Gnuchess 4.0 for DOS](http://groups.google.com/group/gnu.chess/browse_frm/thread/b338264d5235cdd0) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 29, 1993
- [Re: Gnu Chess for the Mac](http://groups.google.com/group/gnu.chess/browse_frm/thread/185bde65b524170d) by [Urban Koistinen](Urban_Koistinen "Urban Koistinen"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), April 16, 1993 » [Macintosh](Macintosh "Macintosh")
- [QMW computer chess](http://groups.google.com/group/rec.games.chess/browse_frm/thread/51267e26536fa912) by [Don Beal](Don_Beal "Don Beal"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 19, 1993 » [UPCCC 1993](UPCCC_1993 "UPCCC 1993")
- [gnu.chess FAQ](http://groups.google.com/group/rec.games.chess/browse_frm/thread/8362d0a032ca3eee) by [Tim Mann](Tim_Mann "Tim Mann"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 4, 1994
- [Fix for ScoreKBNK routine](http://groups.google.com/group/gnu.chess/browse_frm/thread/4a125563ff526c1a) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), February 11, 1994
- [KILLT & HISTORY](http://groups.google.com/group/gnu.chess/browse_frm/thread/316f8ea222d08d03) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), February 19, 1994
- [Search extensions on recaptures](http://groups.google.com/group/gnu.chess/browse_frm/thread/e1098742caf7570d) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 22, 1994
- [Bug fixes for PawnValue()](http://groups.google.com/group/gnu.chess/browse_frm/thread/41a90f3084b72a9e) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 24, 1994
- [Speed up Gnuchess](http://groups.google.com/group/gnu.chess/browse_frm/thread/f47ff393e50f1bce) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), April 18, 1994
- [Speed up UpdatePieceList](http://groups.google.com/group/gnu.chess/browse_frm/thread/a6b1257a1c386acf) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), April 18, 1994
- [Alpha-beta inconsistencies](http://groups.google.com/group/gnu.chess/browse_frm/thread/92b320ddac0f18b3) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), May 20, 1994
- [Bug in ttable.c wrt storing of mate scores](http://groups.google.com/group/gnu.chess/browse_frm/thread/95885a1683123c48) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), May 20, 1994
- [Patches for eval.c](http://groups.google.com/group/gnu.chess/browse_frm/thread/429405cb09558795) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), May 28, 1994
- [Pawn ram code in gnuchess](http://groups.google.com/group/gnu.chess/browse_frm/thread/37bbd87f491aa673) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 18, 1994

## 1995 ...

- [Killer moves](http://groups.google.com/group/gnu.chess/browse_frm/thread/fb62cff6dea1bf09) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 21, 1995
- [Re: request ...](https://groups.google.com/d/msg/gnu.chess/KChQhVPAACA/ApFk4OeWlcYJ) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 16, 1995
- [Re: The KISS Chess Program Project - Overview - ABSEARCH.TXT (0/1)](https://groups.google.com/d/msg/rec.games.chess.computer/Co_7iTrx7rM/5znIOUfvGy4J) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 12, 1997
- [GNU move generation](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7292bfb78152b40b) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 18, 1998 » [Move Generation](Move_Generation "Move Generation")
- [Sever Clutter with Clones of GnuChess/Crafty](https://www.stmintz.com/ccc/index.php?id=41100) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 27, 1999
- [GNU Chess 5](http://groups.google.com/group/gnu.chess/browse_frm/thread/506a4b7acc294d25) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), October 10, 1999

## 2000 ...

- [GNUChess 5.0.. or later... if there is later...](https://www.stmintz.com/ccc/index.php?id=147909) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), January 03, 2001
- [The marvelous showing of GnuChess at CCT3](https://www.stmintz.com/ccc/index.php?id=172108) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 28, 2001 » [CCT3](CCT3 "CCT3")
- [Wb2UCI and Problems with ExChess4.03a and GnuChess4.0.8](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43496) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 24, 2003 » [Wb2UCI](Wb2UCI "Wb2UCI"), [InBetween](InBetween "InBetween")
- [First draw against GnuChess](https://www.stmintz.com/ccc/index.php?id=330725) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), November 26, 2003
- [Who started GNUChess?](https://www.stmintz.com/ccc/index.php?id=356855) by Jamie Stegner, [CCC](CCC "CCC"), March 26, 2004
- [Controversy about who's 1st author of Gnuchess..........John? or Stuart?](https://www.stmintz.com/ccc/index.php?id=357129) by Jamie Stegner, [CCC](CCC "CCC"), March 29, 2004

## 2005 ...

- [Re: gnuchess/xboard protocol](http://lists.gnu.org/archive/html/info-gnu-chess/2006-05/msg00004.html) by [Hans Eric Sandström](index.php?title=Hans_Eric_Sandstr%C3%B6m&action=edit&redlink=1 "Hans Eric Sandström (page does not exist)"), [gnu.org](GNU_Chess#NewsGroup "GNU Chess"), May 19, 2006
- [GNU 5.07](http://www.talkchess.com/forum/viewtopic.php?t=15179) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), July 17, 2007
- [Did someone mention the GNUChess move Generator?](http://www.talkchess.com/forum/viewtopic.php?t=17820) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), November 12, 2007 » [Move Generation](Move_Generation "Move Generation")
- [PSP GNU CHESS: Chess game for PSP v1.0.3](http://zx81.zx81.free.fr/serendipity/index.php?/categories/60-Chess-Game) by zx-81 in Chess-Game, November 17, 2007

## 2010 ...

- [GNUChess for Android](http://www.talkchess.com/forum/viewtopic.php?t=37269) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), December 24, 2010

**2011**

- [GNU Chess v6 pretest](http://lists.gnu.org/archive/html/info-gnu/2011-01/msg00011.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), January 23, 2011
- [GNU Chess 6 (= Fruit)](http://www.talkchess.com/forum/viewtopic.php?t=37789) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 25, 2011 » [Fruit](Fruit "Fruit")
- [GNU Chess 5.08 released](http://lists.gnu.org/archive/html/info-gnu/2011-02/msg00001.html) by [Simon Waters](index.php?title=Simon_Waters&action=edit&redlink=1 "Simon Waters (page does not exist)"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), January 30, 2011
- [GNU Chess 6 released](http://lists.gnu.org/archive/html/info-gnu/2011-04/msg00015.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), April 27, 2011
- [GNU Chess release 6.0.1](http://lists.gnu.org/archive/html/info-gnu/2011-09/msg00009.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), September 08, 2011
- [gnuchess 5.07.173b](http://www.talkchess.com/forum/viewtopic.php?t=40465) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), September 19, 2011

**2012**

- [GNU Chess release 6.0.2](http://lists.gnu.org/archive/html/info-gnu/2012-03/msg00003.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), March 04, 2012
- [GnuChess 5.07.174.1b](http://www.talkchess.com/forum/viewtopic.php?t=45665) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), October 20, 2012

**2013**

- [GNU Chess release 6.0.3](http://lists.gnu.org/archive/html/info-gnu/2013-03/msg00004.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), March 11, 2013
- [GNU Chess 5.50](http://www.talkchess.com/forum/viewtopic.php?t=47793) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), April 16, 2013
- [GNU Chess release 6.1.0](http://lists.gnu.org/archive/html/info-gnu/2013-11/msg00009.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), November 10, 2013
- [GNU Chess 6.1.1](http://lists.gnu.org/archive/html/info-gnu/2013-11/msg00012.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), November 23, 2013

**2014**

- [GNU Chess 6.1.2](http://lists.gnu.org/archive/html/info-gnu/2014-07/msg00016.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), July 30, 2014
- [GNU Chess 5.60](http://www.talkchess.com/forum/viewtopic.php?t=54418) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), November 22, 2014

## 2015 ...

- [GNU Chess release 6.2.1](http://lists.gnu.org/archive/html/info-gnu/2015-01/msg00002.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), January 04, 2015
- [Building GNU Chess 5.07](http://www.talkchess.com/forum/viewtopic.php?t=57806) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 01, 2015
- [GNU Chess 6.2.2](http://lists.gnu.org/archive/html/info-gnu/2015-10/msg00005.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), October 17, 2015
- [Short questions (1): GNUChess 5.6 or 6.22 ... differents?](http://www.talkchess.com/forum/viewtopic.php?t=58030) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 23, 2015

**2016**

- [SourceForge . GNUChess 6.2.2 for Windows](http://www.talkchess.com/forum/viewtopic.php?t=58995) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), January 21, 2016
- [GNU Chess 6.2.3](https://groups.google.com/g/gnu.chess/c/xccjfQHCQsU/m/PaSmtv-jBQAJ) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [gnu.chess](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2016
- [GNU Chess 6.2.3 Release](http://www.talkchess.com/forum/viewtopic.php?t=61618) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), October 06, 2016
- [GNU Chess 6.2.4](http://lists.gnu.org/archive/html/info-gnu/2016-10/msg00013.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), October 29, 2016

**2017 ...**

- [GNU Chess 6.2.5](http://lists.gnu.org/archive/html/info-gnu/2017-07/msg00012.html) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [info-gnu Archives](http://lists.gnu.org/archive/html/info-gnu/), July 25, 2017
- [GNU Chess 6.2.5 release](http://www.talkchess.com/forum/viewtopic.php?t=64842) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 08, 2017
- [Is gnu chess what I am looking for ?](https://groups.google.com/g/gnu.chess/c/JMzNBz14R7k/m/oo5OhmDWAgAJ) by David Wilson, [gnu.chess](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2019

## 2020 ...

- [GNU Chess 6.2.6 released](https://groups.google.com/g/gnu.chess/c/557bKpH7phQ/m/kCUTrjrmAAAJ) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [gnu.chess](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2020
- [GNU Chess 6.2.7 released](https://groups.google.com/g/gnu.chess/c/6oyaGYHT6rk/m/AipnWBmHAwAJ) by [Antonio Ceballos](Antonio_Ceballos "Antonio Ceballos"), [gnu.chess](Computer_Chess_Forums "Computer Chess Forums"), May 31, 2020

## External Links

## Chess Engine

- [GNU Chess - Free Software Foundation](http://www.gnu.org/software/chess/chess.html)
- [GNU Chess](http://www.tim-mann.org/gnuchess.html) on [Tim Mann's](Tim_Mann "Tim Mann") Chess Pages
- [GNU Chess from Wikipedia](https://en.wikipedia.org/wiki/GNU_Chess)
- [GNU Chess](http://www.mobygames.com/game/gnu-chess), [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
- [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [rec.games.chess.computer GNU Chess and XBoard: Frequently Asked Questions](http://groups.google.de/group/rec.games.chess.computer/browse_frm/thread/ede2b5c699e38334)
- [GitHub - heisencoder/gnuchess: Git fork of GNU Chess 5](https://github.com/heisencoder/gnuchess)
- [Index of /Toga/gnuchess-release](http://hardy.uhasselt.be/Toga/gnuchess-release/) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")
- [Index of /GnuCheese](http://hardy.uhasselt.be/GnuCheese/) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")

## Rating

- [GNU Chess 5.50 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=GNU%20Chess%205.50%2064-bit) in [CCRL 40/40](CCRL "CCRL")
- [GNU Chess 5.50 64-bit](http://www.computerchess.org.uk/ccrl/404FRC/cgi/engine_details.cgi?print=Details&eng=GNU%20Chess%205.50%2064-bit#GNU_Chess_5_50_64-bit) in [CCRL 40/4 FRC](CCRL "CCRL")

## News Group

- [gnu.chess](http://groups.google.com/group/gnu.chess/topics) (early years have less spam)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [GNU Project - Free Software Foundation - A Bold GNU Head](https://www.gnu.org/graphics/heckert_gnu.html) by [Aurelio A. Heckert](http://wiki.colivre.net/Aurium/)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: request ...](https://groups.google.com/d/msg/gnu.chess/KChQhVPAACA/ApFk4OeWlcYJ) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 16, 1995
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [gnuchess/common.h at master · heisencoder/gnuchess · GitHub](https://github.com/heisencoder/gnuchess/blob/master/src/common.h)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [GNU Chess - Free Software Foundation](http://www.gnu.org/software/chess/chess.html)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GNU's Bulletin, vol. 1 no. 8 - GNU Project - Free Software Foundation (FSF) | GNUs Flashes](http://www.gnu.org/bulletins/bull8.html#SEC7)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [GNU Chess 1.55 vs. Fidelity Mach 3](http://groups.google.com/group/gnu.chess/msg/583f6ed4f648bf90) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 3, 1990
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one Level](Engines "Engines")**

