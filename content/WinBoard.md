---
title: WinBoard
---
**[Home](Home "Home") \* [User Interface](User_Interface "User Interface") \* [GUI](GUI "GUI") \* WinBoard**


**WinBoard** is a [graphical user interface](GUI "GUI") for the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") under the [Windows](Windows "Windows") operating system, also called the WinBoard protocol, initially designed and developed by [Tim Mann](Tim_Mann "Tim Mann") based on [XBoard](XBoard "XBoard"). In 2009, [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") became the main developer and proposed a protocol definition <a id="cite-note-1" href="#cite-ref-1">[1]</a>, also covering [Chess Variants](Games "Games") with different board sizes.



### Contents


* [1 Screenshot](#screenshot)
* [2 Quotes](#quotes)
* [3 Chess protocols](#chess-protocols)
* [4 Pros and Cons](#pros-and-cons)
* [5 See also](#see-also)
* [6 Forum Posts](#forum-posts)
	+ [6.1 1990 ...](#1990-...)
	+ [6.2 1995 ...](#1995-...)
	+ [6.3 2000 ...](#2000-...)
	+ [6.4 2005 ...](#2005-...)
	+ [6.5 2010 ...](#2010-...)
	+ [6.6 2015 ...](#2015-...)
* [7 External Links](#external-links)
	+ [7.1 Free Software Foundation](#free-software-foundation)
	+ [7.2 Tim Mann & H.G. Muller](#tim-mann-.26-h.g.-muller)
	+ [7.3 WiBoard Misc](#wiboard-misc)
* [8 References](#references)






[](File:Xboard-4.4.0-petite.png)
WinBoard 4.4.0 running [GNU Chess](GNU_Chess "GNU Chess")]


  




## Quotes


Tim Mann's quote from an Interview by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), April 2000 <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++
Originally, xboard and WinBoard were simply graphical user interfaces for [GNU Chess](GNU_Chess "GNU Chess"), then for GNU Chess and [Internet chess servers](Chess_Server "Chess Server"). Because the [GUI](GUI "GUI") and the chess engine are separate programs, several people thought of the idea of connecting their own chess programs in place of GNU Chess, and they began to email me asking how to do it. I think the first person to ask was [Shay Bushinsky](Shay_Bushinsky "Shay Bushinsky"), in November 1994. Over the years I received so many requests for this information that I was more or less forced into documenting and extending the ad-hoc engine protocol to support them. The document that exists now (chess-engines.html) evolved directly from the original email reply I sent to Shay. Unfortunately, because the protocol was never really designed, but just grew out of documenting the existing communication with GNU Chess, there are still several bugs and deficiencies in it today. It would be nice to make some major revisions, but then of course it would (at best) take a long time for the existing engines to convert over to the new protocol, so both would have to be supported, probably forever. 

```

## Chess protocols


Winboard supports only [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). However, UCI's chess engines can run with Winboard via some adapters such as [PolyGlot](PolyGlot "PolyGlot"), [UCI2WB](UCI2WB "UCI2WB") ones.



## Pros and Cons


Winboard was the first-ever and unique for a while chess [graphical user interface](GUI "GUI") with good and very fast graphics, various functions, almost enough for general users. However, some users criticize it since it does not support directly UCI's chess engines as well as it has old-style, complicated and hard to use interface. Not supporting directly UCI engines is a huge disadvantage since almost all new and/or strong chess engines nowadays are UCI ones. It is also the main reason why recently there are so few computer chess tournaments using Winboard as a [Tournament Manager](Tournament_Manager "Tournament Manager") even it has enough functions to do that task.



## See also


* [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [CPW-Engine\_com](CPW-Engine_com "CPW-Engine com")
* [PolyGlot](PolyGlot "PolyGlot")
* [Tournament Manager](Tournament_Manager "Tournament Manager")
* [UCI](UCI "UCI")
* [WinBoard Engines](Category:WinBoard "Category:WinBoard")
* [XBoard](XBoard "XBoard")


## Forum Posts


### 1990 ...


* [Re: Accessing remote computers with WinBoard](http://groups.google.com/group/gnu.chess/browse_frm/thread/a7d8892d10f66aff) by [Tim Mann](Tim_Mann "Tim Mann"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), November 7, 1993


### 1995 ...


* [XBoard and WinBoard 3.4, patchlevel 1](http://groups.google.com/group/rec.games.board/browse_frm/thread/63700b0fcfa8b39e) by [Tim Mann](Tim_Mann "Tim Mann"), [rec.games.board](Computer_Chess_Forums "Computer Chess Forums"), December 13 1995
* [Problems with Winboard - fix??](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/d5a2c1b4cd56e830) by [Valavan Manohararajah](Valavan_Manohararajah "Valavan Manohararajah"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 6 1996
* [XBoard and WinBoard, version 3.6.0](https://groups.google.com/d/msg/rec.games.chess.misc/M-NkXvEu1DM/XeESczC85o0J) by [Tim Mann](Tim_Mann "Tim Mann"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), May 09, 1997
* [xboard/WinBoard 4.0.0 available](https://groups.google.com/d/msg/rec.games.chess.misc/mavUOiKKADQ/a-jCSNDL9fUJ) by [Tim Mann](Tim_Mann "Tim Mann"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 21, 1998
* [WinBoard and pondering under W98](https://www.stmintz.com/ccc/index.php?id=62577) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), July 28, 1999 » [Pondering](Pondering "Pondering")


### 2000 ...


* [Winboard for Dummies](https://groups.google.com/d/msg/rec.games.chess.computer/r5-Kdb4p4bE/tKCt-SwZKlgJ) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 30, 2001
* [xboard and WinBoard 4.2.4 released](http://groups.google.com/group/gnu.chess/browse_frm/thread/3fffd13e5ba818aa) by [Tim Mann](Tim_Mann "Tim Mann"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), December 10, 2001
* [Winboard.debug](https://www.stmintz.com/ccc/index.php?id=269311) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 07, 2002 » [Debugging](Debugging "Debugging")
* [New Winboard version 4.3.0 released](https://www.stmintz.com/ccc/index.php?id=281836) by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann"), [CCC](CCC "CCC"), February 05, 2003
* [Daniel's Winboard: kibitzing?](https://www.stmintz.com/ccc/index.php?id=282009) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), February 05, 2003
* [Kiwi for Win98 and input-reading stuff](https://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [Windows](Windows "Windows"), [C++](Cpp "Cpp"), [Thread](Thread "Thread")


### 2005 ...


* [Safe I/O (repeated)](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1622) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2005
* [A question about kibitz](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1693&p=7809) by [Niyaz Khasanov](index.php?title=Niyaz_Khasanov&action=edit&redlink=1 "Niyaz Khasanov (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 18, 2005
* [CPU usage at 505 in Winboard Engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5220) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 19, 2006
* [WinBoard 4.3 Downloads](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=49439&sid=27d04ba4c820ef569d3e6b217f547705) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 23, 2008
* [A Basic Guide for setting up Winboard a UCI Chess Engine](http://www.open-aurec.com/wbforum/viewtopic.php?t=49603) by Charles Browne, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), 01 Nov 2008
* [It's a plague of Winboard engines](http://www.open-aurec.com/wbforum/viewtopic.php?t=50346) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 20, 2009 » [Time Management](Time_Management "Time Management")
* [UCI protocol in winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=50429) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2009 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [UCI](UCI "UCI")
* [Adapter for non-standard chess engine to Winboard](http://www.talkchess.com/forum/viewtopic.php?t=30088) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), October 10, 2009
* [winboard engine config popup](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50583) by [Will Singleton](Will_Singleton "Will Singleton"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 19, 2009


### 2010 ...


* [WinBoard & Chessclub.com](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=50745) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 25, 2010
* [Aquarium (other GUIs too?) and WB support => I am shocked](http://www.talkchess.com/forum/viewtopic.php?t=32952) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), February 27, 2010
* [Multiple WinBoard installations](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=51142) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 17, 2010


**2011**



* [WinBoard, exotic version](http://www.talkchess.com/forum/viewtopic.php?start=0&t=37634) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 15, 2011
* [WinBoard 4.5 downloads](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=51528) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 06, 2011
* [WinBoard protocol driver](http://www.open-aurec.com/wbforum/viewtopic.php?f=24&t=51739) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum - Chess Programming Lessons](Computer_Chess_Forums "Computer Chess Forums"), April 30, 2011
* [ics command](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=51787) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 18, 2011
* [WinBoard 4.5.3 released](http://www.talkchess.com/forum/viewtopic.php?t=40613) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 02, 2011


**2012**



* [Winboard questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=52172&p=197618) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 26, 2012
* [Winboard bloated?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=24377) by tomgdrums, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), February 20, 2012
* [XBoard / WinBoard 4.6.0 released](http://www.talkchess.com/forum/viewtopic.php?t=42834) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 11, 2012
* [Winboard and braille display](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=52471&p=198303) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2012 <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Winboard/Java help](http://www.talkchess.com/forum/viewtopic.php?t=43411) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), April 22, 2012 » [Java](Java "Java")
* [For HGM: Engine priority under Winboard/Polyglot](http://www.talkchess.com/forum/viewtopic.php?t=44466) by [Joost Buijs](Joost_Buijs "Joost Buijs"), [CCC](CCC "CCC"), July 16, 2012
* [Winboard protocol and fractional increments](http://www.talkchess.com/forum/viewtopic.php?t=45325) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 25, 2012 » [Time Management](Time_Management "Time Management")


**2013**



* [Tool to recreate PGN from winboard.debug?](http://www.talkchess.com/forum/viewtopic.php?t=46721) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 01, 2013 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* [WinBoard 4.7.0 released (with CCT support!)](http://www.talkchess.com/forum/viewtopic.php?t=47292) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 21, 2013 » [CCT15](CCT15 "CCT15")
* [WinBoard 4.7.2 released](http://www.talkchess.com/forum/viewtopic.php?t=49164) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 29, 2013


**2014**



* [Any WinBoard bugs I missed?](http://www.talkchess.com/forum/viewtopic.php?t=53668) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 11, 2014
* [for Chess-variant authors](http://www.talkchess.com/forum/viewtopic.php?t=53734) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 17, 2014
* [WinBoard 4.8.0 pre-release](http://www.talkchess.com/forum/viewtopic.php?t=53785) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 22, 2014
* [WinBoard/XBoard 4.8.0 released](http://www.talkchess.com/forum/viewtopic.php?t=54084) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 18, 2014
* [UCCI2WB](http://www.talkchess.com/forum/viewtopic.php?t=54162) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 27, 2014


### 2015 ...


* [Setting up engines](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=53526) by Dan-the-K, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 08,2015
* [Winboard 4.8.0b and Amazon chess variant](http://www.talkchess.com/forum/viewtopic.php?t=58482) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), December 05, 2015


**2016**



* [Engines with interfaces for slightly nerdish people](http://www.talkchess.com/forum/viewtopic.php?t=59367) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), February 26, 2016
* [Einstein wuerfelt nicht](http://www.talkchess.com/forum/viewtopic.php?t=60688) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 03, 2016 » [EinStein würfelt nicht!](EinStein_w%C3%BCrfelt_nicht! "EinStein würfelt nicht!")
* [Weird Windows / WinBoard behavior](http://www.talkchess.com/forum/viewtopic.php?t=61435) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 15, 2016 » [Process](Process "Process"), [Windows](Windows "Windows")
* [Winboard book settings](http://www.talkchess.com/forum/viewtopic.php?t=61780) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), October 20, 2016 » [Opening Book](Opening_Book "Opening Book")
* [MinGW AlphaBlend](http://www.talkchess.com/forum/viewtopic.php?t=62315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), November 29, 2016 » [2D Graphics Board](2D_Graphics_Board "2D Graphics Board"), [Windows](Windows "Windows") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Polyglot pickBest](http://www.talkchess.com/forum/viewtopic.php?t=62642) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), December 29, 2016 » [PolyGlot](PolyGlot "PolyGlot")


**2017**



* [Novag UCB drivers (Winboard and UCI)](http://www.talkchess.com/forum/viewtopic.php?t=63256) by [Graham O'Neill](index.php?title=Graham_O%27Neill&action=edit&redlink=1 "Graham O'Neill (page does not exist)"), [CCC](CCC "CCC"), February 24, 2017 » [Novag Universal Electronic Chess Board](Novag_Universal_Electronic_Chess_Board "Novag Universal Electronic Chess Board")
* [Winboard variants online](http://www.talkchess.com/forum/viewtopic.php?t=63525) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), March 22, 2017 » [Chess Variants](Chess#Variants "Chess")
* [Winboard questions](http://www.talkchess.com/forum/viewtopic.php?t=64411) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 26, 2017
* [Winboard: Resigning?](http://www.talkchess.com/forum/viewtopic.php?t=64432) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), June 27, 2017


**2018**



* [about using winboard](http://www.talkchess.com/forum/viewtopic.php?t=66686) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 25, 2018
* [UCI vs Winboard question](http://www.talkchess.com/forum/viewtopic.php?t=66745) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 05, 2018 » [UCI](UCI "UCI")


**2020...**



* [Re: What GUI you use and why?](http://www.talkchess.com/forum/viewtopic.php?t=80192) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 1, 2020
* [How to pass UCI parameters to Xboard?](http://www.talkchess.com/forum/viewtopic.php?t=80342) by [Gautam Buddha](index.php?title=Gautam_Buddha&action=edit&redlink=1 "Gautam Buddha (page does not exist)"), [CCC](CCC "CCC"), July 21, 2020


## External Links


### [Free Software Foundation](Free_Software_Foundation "Free Software Foundation")


* [XBoard - GNU Project](https://www.gnu.org/software/xboard/) also includes **WinBoard**
	+ [What is new in WinBoard / XBoard 4.6.0?](https://www.gnu.org/software/xboard/whats_new/4.6.0/index.html)
		- [XBoard tourney-manager function](https://www.gnu.org/software/xboard/whats_new/4.6.0/TM.html) » [Tournament Manager](Tournament_Manager "Tournament Manager")
	+ [What is new in WinBoard / XBoard 4.7.0?](https://www.gnu.org/software/xboard/whats_new/4.7.0/index.html)
	+ [What is new in WinBoard / XBoard 4.8.0?](https://www.gnu.org/software/xboard/whats_new/4.8.0/index.html)
	+ [What is new in WinBoard / XBoard 4.9.0?](https://www.gnu.org/software/xboard/whats_new/4.9.0/index.html)


### [Tim Mann](Tim_Mann "Tim Mann") & [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")


* [Chess Engine Communication Protocol](http://home.hccnet.nl/h.g.muller/engine-intf.html) by [Tim Mann](Tim_Mann "Tim Mann") & [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")
* [hgm.nubati.net Git - xboard.git/summary](http://hgm.nubati.net/cgi-bin/gitweb.cgi?p=xboard.git;a=summary)
* [What is new in XBoard/WinBoard 4.9.0?](http://hgm.nubati.net/XB-4.9.0/) by [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")
* [Tim Mann's Chess Pages, XBoard and WinBoard](http://timmann.server269.com/xboard.html)


### WiBoard Misc


* [XBoard from Wikipedia](https://en.wikipedia.org/wiki/XBoard)
* [Tinkering with Winboard...](http://walkofmind.com/programming/chess/winboard_x.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")
	+ [Winboard/XBoard UML state diagram](http://walkofmind.com/programming/chess/xboard.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")
* [Lyapko George's WinBoard related page](http://www.oocities.org/siliconvalley/lab/6606/winboard.htm) (outdated) by [George Lyapko](George_Lyapko "George Lyapko") <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [FAQ on Winboard and Chess Engines](http://www.horizonchess.com/FAQ/Winboard/index.html) by [Aaron Tay](Aaron_Tay "Aaron Tay"), hosted by [Ron Murawski](Ron_Murawski "Ron Murawski")
* [What can Winboard do?](http://horizonchess.com/FAQ/Winboard/confusion.html) by [Aaron Tay](Aaron_Tay "Aaron Tay"), March 01, 2002, hosted by [Ron Murawski](Ron_Murawski "Ron Murawski")
* [Winboard and Chess Engines FAQ](http://computer-chess.org/doku.php?id=winboard:faq:index) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [Winboard](http://computer-chess.org/doku.php?id=computer_chess:winboard) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [Winboard Forum](http://www.open-aurec.com/wbforum/index.php)
* [WinBoard development and bugfixing Forum](http://www.open-aurec.com/wbforum/viewforum.php?f=19)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess Engine Communication Protocol](http://home.hccnet.nl/h.g.muller/engine-intf.html) by [Tim Mann](Tim_Mann "Tim Mann") & [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [XBoard Project History](http://tim-mann.org/history.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Refreshable braille display from Wikipedia](https://en.wikipedia.org/wiki/Refreshable_braille_display)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Lyapko George's WinBoard related page](http://www.oocities.org/siliconvalley/lab/6606/winboard.htm) (outdated) by [George Lyapko](George_Lyapko "George Lyapko")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Alpha compositing from Wikipedia](https://en.wikipedia.org/wiki/Alpha_compositing)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [MinGW from Wikipedia](https://en.wikipedia.org/wiki/MinGW)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Tool to recreate PGN from winboard.debug?](http://www.talkchess.com/forum/viewtopic.php?t=46721) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 01, 2013 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")

**[Up one Level](GUI "GUI")**







 
