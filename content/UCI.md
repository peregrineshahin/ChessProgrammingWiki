---
title: UCI
---
**[Home](Home "Home") \* [Protocols](Protocols "Protocols") \* UCI**


**UCI**, (Universal Chess Interface)  

an open [communication protocol](https://en.wikipedia.org/wiki/Communication_protocol) for chess engines to play [games](Games "Games") automatically, that is to communicate with other programs including [Graphical User Interfaces](GUI "GUI"). UCI was designed and developed by [Rudolf Huber](Rudolf_Huber "Rudolf Huber") and [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") [[1]](#cite_note-1), and released in November 2000 [[2]](#cite_note-2) . It has, by-in-large, replaced the older [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") ([WinBoard](WinBoard "WinBoard")/[XBoard](XBoard "XBoard")).



### Contents


* [1 Design Philosophy](#Design_Philosophy)
* [2 Critique](#Critique)
	+ [2.1 Contra](#Contra)
	+ [2.2 Pro](#Pro)
* [3 Engines](#Engines)
* [4 GUIs](#GUIs)
* [5 CLIs](#CLIs)
* [6 Utilities](#Utilities)
* [7 See also](#See_also)
* [8 Forum Posts](#Forum_Posts)
	+ [8.1 2000 ...](#2000_...)
	+ [8.2 2005 ...](#2005_...)
	+ [8.3 2010 ...](#2010_...)
	+ [8.4 2015 ...](#2015_...)
	+ [8.5 2020 ...](#2020_...)
* [9 External Links](#External_Links)
	+ [9.1 Interviews](#Interviews)
	+ [9.2 Implementations](#Implementations)
	+ [9.3 JavaScript](#JavaScript)
* [10 Video Tutorials](#Video_Tutorials)
* [11 References](#References)






The UCI capable [GUI](GUI "GUI") is not only View and Controller of a chess [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), but also keeps the Model with its internal [game states](Chess_Game "Chess Game"). It is also an "arbiter" instance to decide about the outcome of the game, for instance in declaring a game to be drawn after a [threefold repetition](Repetitions "Repetitions") has occurred. The UCI GUI may choose and play moves from an [opening book](Opening_Book "Opening Book") and [endgame tablebase](Endgame_Tablebases "Endgame Tablebases").



## Critique


While the UCI design makes it simple for engine programmers to integrate a "stateless" chess engine, it was also disputed by various chess programmers, since it subsumes engine control parameters and delegates possibly game decisive stuff to the GUI.



### Contra


* GUIs may send very long commands (for chess positions) to chess engines
* It is hard for chess engines to process input/output without an extra thread for that duty
* Missing some useful commands/info: inform chess engines the results, no information about after movestogo GUIs will reset clock or not


Excerpt concerning UCI from a [Robert Hyatt](Robert_Hyatt "Robert Hyatt") interview by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") in 2002 [[3]](#cite_note-3) :




```C++
I simply don't like UCI. It subsumes **all** engine control parameters. It tells the engine when to [ponder](Pondering "Pondering"), when to [search](Search "Search"), when to stop, etc. That is contrary to my design and I have no interest in hacking [Crafty](Crafty "Crafty") to support something that is so different from the [WinBoard/XBoard](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") protocol that has been around for a **long** time and which works **perfectly**.

```


```C++
It removes several critical engine-decisions that are best made by the engine, not the GUI.

```

[Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") wrote on a [Talkchess](Talkchess "Talkchess") thread [[4]](#cite_note-4)




```C++
IMO statelessness w.r.t. the game state (including clocks) in UCI was a very bad idea. It is not only that it makes the communication unnecessarily verbose, but w.r.t. clocks there is a real problem: in classical TC the timing info accompanying the 'go' command does not specify how much time will be added after the 'movestogo' have been played. With movestogo=1 and wtime/btime=59000 you could be in a 40moves/hour game, at the brink of receiving another hour for the next 40 moves, in which case it would be wise to completely spend the remaining 59 sec on the upcoming move, as this is already below average. But you could also be in a 40moves/min game, where you got out of book after 39 moves, and receive only 1 new minute for the next 40. Wasting the 59 sec on a single move now effectively reduces your time for the second session by a factor 2, which would be very sub-optimal. The time management in this case should act like you have 1:59 for 41 moves (but be aware of a 'cold-turkey deadline' for the upcoming move). There is no way a UCI engine could know this.

```

### Pro


* Statelessness. That reduces unsynchronised problems between chess GUIs and engines
* Chess systems (chess GUIs and chess engines) may work more stably
* Remove the need of having extra configuration/init files for engines
* Easier for chess engine developers to support: easy to parse, create commands, almost no ambiguous, straight/simple code since it is almost not required automatic algorithms
* Easier for debugging: easy to start a match from the middle of a game (using various opening types); easy to pick up a position from long logs (for debugging purposes)
* Almost all new and/or strong chess engines support UCI
* Almost all chess GUIs support


[Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey") emphasize the ease of implementation in a [Quisinsky](Frank_Quisinsky "Frank Quisinsky") interview, April 05, 2005 [[5]](#cite_note-5) :




```C++
The choice of UCI is based on software-design principles that are not easy to explain. It's a programmer's thing really, I don't expect engine users to understand. Let me give you a clue though: think about young WinBoard engines that you have tried; how many handled pondering ... without bugs??? Another clue might be that surely, [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") knows a lot about good programming, right? So trust him if not me, UCI is good for programmers because it leads to fewer bugs in the code ... 


```

Fabien wrote a protocol translation program, [PolyGlot](PolyGlot "PolyGlot") to allow use of the new protocol on [Linux](Linux "Linux"), though this is now supported natively by the powerful [Scid vs. PC](Scid_vs._PC "Scid vs. PC") toolkit. Scid vs. PC itself includes Polyglot code to enable support for Polyglot opening books.


[Marco Costalba](Marco_Costalba "Marco Costalba") replied [Robert Hyatt](Robert_Hyatt "Robert Hyatt") on a [Talkchess](Talkchess "Talkchess") thread [[6]](#cite_note-6)




```C++
The protocol is brilliant (and you can clearly realize it was designed by a very good programmer) because allows the code needed to handle it to be:
- Straightforward
- Simple (meaning with the minimal number of 'if' branches and logic)
- General (meaning the same algorithm can handle all the different cases in an uniform fashion).
The aim of the UCI protocol is to make the code simple, that's why I think it was made for programmers by a (great) programmer.

```

[Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen") replied [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") on a [Talkchess](Talkchess "Talkchess") thread [[7]](#cite_note-7)




```C++
UCI's statelessness is surely not a bad idea. Your example did not prove that (it is a bad idea) but just point out a flawed detail on UCI design.
A stateless protocol means a chess GUI must provide enough information each time an engine starts thinking. In your example, it cannot send enough information about the timer since the protocol does not mention it. It is not a big deal since programmers can solve that issue easily by adding some assumes. Of course, it is better one day we can fix those flawed details in the protocol (version 2?).

```


```C++
I have written engines with both protocols (UCI, WB) and now support them all in my own chess GUI. Thus I have my own ideas about the strong points of each. Both are so good and can do so well their jobs. The stateless idea is the central point of UCI, which makes it a bit more suitable for modern computers and programming - that is why recently it becomes very popular.

```

## Engines


* [UCI Engines](Category:UCI "Category:UCI")
* [Linux UCI Engines](Category:Linux "Category:Linux")






## [GUIs](GUI "GUI")


* [Aquarium](Aquarium "Aquarium")
* [Arena](Arena "Arena")
* [Banksia](Banksia "Banksia")
* [Banksia GUI](Banksia_GUI "Banksia GUI")
* [Chess Assistant](Chess_Assistant "Chess Assistant")
* [ChessBase (Database)](ChessBase_(Database) "ChessBase (Database)")
* [Chess for Android](Chess_for_Android "Chess for Android")
* [ChessPartner](ChessPartner "ChessPartner")
* [Chess Wizard](index.php?title=Chess_Wizard_(GUI)&action=edit&redlink=1 "Chess Wizard (GUI) (page does not exist)")
* [Cute Chess](Cute_Chess "Cute Chess")
* [Fritz GUI](Fritz#FritzGUI "Fritz")
* [HIARCS Chess Explorer](HIARCS_Chess_Explorer "HIARCS Chess Explorer")
* [Jerry](Jerry "Jerry")
* [jose](index.php?title=Jose&action=edit&redlink=1 "Jose (page does not exist)")
* [Kvetka](Kvetka "Kvetka")
* [LittleBlitzer](LittleBlitzer "LittleBlitzer")
* [Lucas Chess](Lucas_Chess "Lucas Chess")
* [PyChess](PyChess "PyChess")
* [SCID](SCID "SCID")
* [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
* [Scidb](Scidb "Scidb")
* [Shredder GUI](Shredder#GUI "Shredder")
* [Tarrasch](Tarrasch "Tarrasch")


## [CLIs](CLI "CLI")


* [Cutechess-cli](Cutechess-cli "Cutechess-cli")
* [c-chess-cli](C-chess-cli "C-chess-cli")


## Utilities


* [InBetween](InBetween "InBetween")
* [JSUCI](index.php?title=JSUCI&action=edit&redlink=1 "JSUCI (page does not exist)")
* [PolyGlot](PolyGlot "PolyGlot")
* [Wb2UCI](Wb2UCI "Wb2UCI")
* [UCI2WB](UCI2WB "UCI2WB")


## See also


* [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [CPW-Engine\_com](CPW-Engine_com "CPW-Engine com")
* [Engine Testing](Engine_Testing "Engine Testing")
* [USI](USI "USI") - Universal Shogi Interface
* [Vice UCI-Videos](Vice#UCI "Vice")
* [WinBoard](WinBoard "WinBoard")
* [XBoard](XBoard "XBoard")


## Forum Posts


### 2000 ...


* [UCI (=universal chess interface)](https://www.stmintz.com/ccc/index.php?id=141612) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), November 28, 2000
* [UCI Issues](https://www.stmintz.com/ccc/index.php?id=155894) by [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [CCC](CCC "CCC"), February 25, 2001
* [UCI - a good idea?](https://www.stmintz.com/ccc/index.php?id=202057) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 15, 2001
* [Delphi and the UCI Protokoll](https://www.stmintz.com/ccc/index.php?id=224455) by [Martin Bauer](Martin_Bauer "Martin Bauer"), [CCC](CCC "CCC"), April 18, 2002 » [Delphi](Delphi "Delphi")
* [One more time Delphi and UCI](https://www.stmintz.com/ccc/index.php?id=225107) by [Martin Bauer](Martin_Bauer "Martin Bauer"), [CCC](CCC "CCC"), April 21, 2002
* [UCI versus Winboard](https://www.stmintz.com/ccc/index.php?id=246554) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), August 21, 2002
* [UCI - Worth Implementing?](https://www.stmintz.com/ccc/index.php?id=269320) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), December 07, 2002
* [UCI-protocoll and engines. score cp (x)](https://www.stmintz.com/ccc/index.php?id=291359) by Juergen Wolf, [CCC](CCC "CCC"), April 01, 2003
* [Extension of the UCI protocol](https://www.stmintz.com/ccc/index.php?id=360181) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), April 15, 2004


### 2005 ...


* [How to implement the UCI command "currline"](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2374) by [Josué Forte](Josu%C3%A9_Forte "Josué Forte"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 24, 2005
* [UCI protocol question](https://www.stmintz.com/ccc/index.php?id=453616) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), October 04, 2005
* [UCI protocol and SMP](http://www.talkchess.com/forum/viewtopic.php?t=24866) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), November 13, 2008 » [Parallel Search](Parallel_Search "Parallel Search"), [SMP](SMP "SMP")
* [Appeal to SMP-engines programmers using UCI](http://www.talkchess.com/forum/viewtopic.php?t=25908) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 09, 2009
* [UCI protocol in winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=50429) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2009 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [WinBoard](WinBoard "WinBoard")


### 2010 ...


* [Handling UCI protocol and Stockfish / Glaurung behavior](http://www.talkchess.com/forum/viewtopic.php?t=31608) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), January 10, 2010 » [Stockfish](Stockfish "Stockfish"), [Glaurung](Glaurung "Glaurung")
* [UCI extensions for kibitzing](http://www.talkchess.com/forum/viewtopic.php?t=33088) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), March 05, 2010
* [UCI issues](http://www.talkchess.com/forum/viewtopic.php?t=34481) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), May 24, 2010
* [UCI-compatible interface for 10x8 chess?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=37126) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), December 17, 2010
* [some UCI protocol issues/questions](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=381800) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 17, 2010


**2011**



* [SMP for Android UCI engines](http://www.talkchess.com/forum/viewtopic.php?t=38753) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), April 14, 2011 » [Android](Android "Android"), [SMP](SMP "SMP")
* [UCI multipv question](http://www.talkchess.com/forum/viewtopic.php?t=39340) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), June 11, 2011 » [Multi-PV](Principal_Variation#MultiPV "Principal Variation")
* [UCI nullmove](http://www.talkchess.com/forum/viewtopic.php?t=39950) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 03, 2011
* [UCI Engine Tuning](http://www.talkchess.com/forum/viewtopic.php?t=40117) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), August 20, 2011


**2012**



* [About UCI multipv](http://www.talkchess.com/forum/viewtopic.php?t=42037) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), January 17, 2012 » [Multi-PV](Principal_Variation#MultiPV "Principal Variation")
* [good macintosh guy for UCI engine development](http://www.talkchess.com/forum/viewtopic.php?t=42154) by [Sam Hamilton](Sam_Hamilton "Sam Hamilton"), [CCC](CCC "CCC"), January 25, 2012 » [GUI](GUI "GUI"), [Macintosh](Macintosh "Macintosh"), [Mac OS](Mac_OS "Mac OS")
* [Remote UCI engines and port forwarding](https://open-chess.org/viewtopic.php?f=7&t=2053) by itias, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 01, 2012
* [Ponder and UCI](http://www.open-chess.org/viewtopic.php?f=5&t=2146) by geko, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 19, 2012 » [Pondering](Pondering "Pondering")
* [Problem with UCI engines hash in Arena](http://www.talkchess.com/forum/viewtopic.php?t=46586) by Carl Langan, [CCC](CCC "CCC"), December 26, 2012 » [Arena](Arena "Arena")


**2013**



* [UCI Programming](http://www.open-chess.org/viewtopic.php?f=5&t=2221) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 15, 2013
* [UCI protocol not working](http://www.open-chess.org/viewtopic.php?f=5&t=2245) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 27, 2013
* [UCI Interfacing question](http://www.open-chess.org/viewtopic.php?f=5&t=2357) by epideath, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 05, 2013
* [UCI protocol issue](http://www.talkchess.com/forum/viewtopic.php?t=48768) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 27, 2013 » [Repetitions](Repetitions "Repetitions")
* [uci ponder protocol](http://www.talkchess.com/forum/viewtopic.php?t=48996) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), August 17, 2013 » [Pondering](Pondering "Pondering")
* [UCI variants support](http://www.talkchess.com/forum/viewtopic.php?t=50498) by [Balint Pfliegel](Balint_Pfliegel "Balint Pfliegel"), [CCC](CCC "CCC"), December 15, 2013


**2014**



* [JSUCI 1.0 - connect javascript chess engines to UCI](http://www.talkchess.com/forum/viewtopic.php?t=51763) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), March 28, 2014 » [JavaScript](JavaScript "JavaScript") [[8]](#cite_note-8)
* [MadChess UCI\_LimitStrength Algorithm](http://www.talkchess.com/forum/viewtopic.php?t=51973) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), April 12, 2014 » [MadChess](MadChess "MadChess"), [Playing Strength](Playing_Strength "Playing Strength")
* [UCI, ownbooks, and a potential problem](http://www.talkchess.com/forum/viewtopic.php?t=52661) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), June 16, 2014 » [Opening Book](Opening_Book "Opening Book")
* [UCI exclude move](http://www.talkchess.com/forum/viewtopic.php?t=53123) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), July 30, 2014
* [UCI Protocol](http://www.talkchess.com/forum/viewtopic.php?t=53504) by jay dee, [CCC](CCC "CCC"), August 31, 2014
* [PV after stop/readyok](http://www.talkchess.com/forum/viewtopic.php?t=54093) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), October 20, 2014
* [UCCI2WB](http://www.talkchess.com/forum/viewtopic.php?t=54162) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 27, 2014 » [Chinese Chess](Chinese_Chess "Chinese Chess") [[9]](#cite_note-9)
* [UCI protocol for chess variants](http://www.talkchess.com/forum/viewtopic.php?t=54167) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 28, 2014
* [How does input console for UCI work ?](http://www.talkchess.com/forum/viewtopic.php?t=54703) by [Piotr Lopusiewicz](index.php?title=Piotr_Lopusiewicz&action=edit&redlink=1 "Piotr Lopusiewicz (page does not exist)"), [CCC](CCC "CCC"), December 20, 2014


### 2015 ...


* [UCI request answers all time..... how to do it?](http://www.talkchess.com/forum/viewtopic.php?t=55662) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), March 14, 2015
* [UCI way to communications. Wich kind of inputs?](http://www.talkchess.com/forum/viewtopic.php?t=55666) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), March 15, 2015
* [UCI extension: nodestime](http://www.talkchess.com/forum/viewtopic.php?t=55742) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), March 22, 2015
* [UCI extension: nps NODE\_RATE](http://www.talkchess.com/forum/viewtopic.php?t=55745) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), March 23, 2015
* [ponder engine-gui interaction](http://www.talkchess.com/forum/viewtopic.php?t=56776) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), June 25, 2015 » [Pondering](Pondering "Pondering")
* [Crafty UCI version](http://www.talkchess.com/forum/viewtopic.php?t=56935) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), July 10, 2015 » [Crafty](Crafty "Crafty")
* [UCI OwnBook shim?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=58176) by [Ian Osgood](Ian_Osgood "Ian Osgood"), [CCC](CCC "CCC"), November 07, 2015 » [PolyGlot](PolyGlot "PolyGlot")
* [Ugly UCI](http://www.talkchess.com/forum/viewtopic.php?t=58392) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), November 27, 2015


 [Re: Ugly UCI](http://www.talkchess.com/forum/viewtopic.php?t=58392&start=9) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), November 27, 2015
**2016**



* [stateless UCI](http://www.talkchess.com/forum/viewtopic.php?t=59235) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), February 13, 2016 » [Pondering](Pondering "Pondering")
* [Question to UCI engine authors](http://www.talkchess.com/forum/viewtopic.php?t=62342) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 01, 2016


**2017**



* [UCI protocol: letting the engine know the game result](http://www.talkchess.com/forum/viewtopic.php?t=62869) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), January 19, 2017
* [UCI: Console Play Mode?](http://www.talkchess.com/forum/viewtopic.php?t=63228) by Matthew Hull, [CCC](CCC "CCC"), February 20, 2017
* [Novag UCB drivers (Winboard and UCI)](http://www.talkchess.com/forum/viewtopic.php?t=63256) by [Graham O'Neill](index.php?title=Graham_O%27Neill&action=edit&redlink=1 "Graham O'Neill (page does not exist)"), [CCC](CCC "CCC"), February 24, 2017 » [Novag Universal Electronic Chess Board](Novag_Universal_Electronic_Chess_Board "Novag Universal Electronic Chess Board")
* [Reporting a draw in UCI](http://www.talkchess.com/forum/viewtopic.php?t=63906) by Vince Sempronio, [CCC](CCC "CCC"), May 05, 2017 » [Draw](Draw "Draw")
* [UCI, What command should the engine expect while it's searching](http://www.talkchess.com/forum/viewtopic.php?t=64227) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 09, 2017
* [UCI on another thread, programming help !](http://www.talkchess.com/forum/viewtopic.php?t=64262) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 11, 2017
* [UCI error codes?](http://www.talkchess.com/forum/viewtopic.php?t=64679) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), July 21, 2017
* [Regarding UCI Pondering](http://www.talkchess.com/forum/viewtopic.php?t=65324) by [Manik Charan](Manik_Charan "Manik Charan"), [CCC](CCC "CCC"), September 28, 2017 » [Pondering](Pondering "Pondering")
* [Loading opening book and tablebases (xboard vs uci)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65454) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), October 15, 2017 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [UCI pondering or infinite search](http://www.talkchess.com/forum/viewtopic.php?t=65679) by Lucas Braesch, [CCC](CCC "CCC"), November 10, 2017 » [Pondering](Pondering "Pondering")
* [Regarding options ponder flag](http://www.talkchess.com/forum/viewtopic.php?t=65913) by [Jürgen Précour](index.php?title=J%C3%BCrgen_Pr%C3%A9cour&action=edit&redlink=1 "Jürgen Précour (page does not exist)"), [CCC](CCC "CCC"), December 06, 2017 » [Pondering](Pondering "Pondering")


**2018**



* [UCI vs Winboard question](http://www.talkchess.com/forum/viewtopic.php?t=66745) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 05, 2018 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [WinBoard](WinBoard "WinBoard")
* [UCI Pondering workaround](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67971) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 13, 2018 » [Pondering](Pondering "Pondering")
* [ExaChess interface UCI to program](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68703) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), October 20, 2018
* [UCI pondering done right](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69279) by lucasart, [CCC](CCC "CCC"), December 16, 2018 » [Pondering](Pondering "Pondering")


**2019**



* [UCI question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69746) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 28, 2019
* [Ambiguous: UCI and option Clear Hash](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71050) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), June 20, 2019
* [Sending pure comments using UCI protocol](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71617) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 21, 2019
* [Re: PGN standard, its improvement and standardization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72019&start=36) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), October 14, 2019 » from [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") to [Protocols](Protocols "Protocols")
* [UCI Win/Draw/Loss reporting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72140) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 22, 2019 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [UCI pondering and time management](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72686) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 30, 2019 » [Pondering](Pondering "Pondering"), [Time Management](Time_Management "Time Management")


### 2020 ...


* [UCI to CECP](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73592) by Fulvio, [CCC](CCC "CCC"), April 07, 2020 » [CECP](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
* [UCI Options, clarifation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73617) by Alan Cooper, [CCC](CCC "CCC"), April 10, 2020
* [Remote UCI](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75218) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), September 26, 2020
* [UCI wrapper?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75783) by Kurt Lanc, [CCC](CCC "CCC"), November 13, 2020
* [UCI Gui to remote Linux Engine](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75992) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), December 05, 2020 » [GUI](GUI "GUI"), [Linux](Linux "Linux")


**2021**



* [Uci "go" command without other parameters](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76344) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), January 17, 2021
* [Missing input in ponder](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77088) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), April 15, 2021 » [Pondering](Pondering "Pondering")
* [Listening for GUI input when searching](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77189) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 27, 2021 » [GUI](GUI "GUI"), [Search](Search "Search"), [Thread](Thread "Thread")
* [Reporting errors in UCI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77432) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), June 03, 2021
* [uci question, receive stop before pondering starts](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77650) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 06, 2021
* [UCI's readyok: A mistake or a misunderstanding](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77835) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 31, 2021
* [Ignoring threads option, is it valid?](http://talkchess.com/forum3/viewtopic.php?f=7&t=77842) by [CM Canavessi](index.php?title=CM_Canavessi&action=edit&redlink=1 "CM Canavessi (page does not exist)"), [CCC](CCC "CCC"), August 01, 2021
* [Latest UCI spec?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77904) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), August 08, 2021


## External Links


* [The UCI Specification](https://www.shredderchess.com/chess-features/uci-universal-chess-interface.html) from [Shredder Chess](Shredder "Shredder")
* [UCI protocol](http://wbec-ridderkerk.nl/html/UCIProtocol.html) hosted by [WBEC Ridderkerk](WBEC "WBEC")
* [Universal Chess Interface From Wikipedia](https://en.wikipedia.org/wiki/Universal_Chess_Interface)


### Interviews


* [Arena, Interviews mit Prof. Dr. Robert Hyatt, Tim Mann und Martin Blume](http://web.archive.org/web/20020925204655fw_/http://www.playwitharena.com/directory/interviews/interviews.htm) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") for [ChessBits](ChessBits "ChessBits"), No. 18, May 2002 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)) » [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann"), [Martin Blume](Martin_Blume "Martin Blume") [[10]](#cite_note-10)
* [Interview with SOS programmer Rudolf Huber in German language!](https://web.archive.org/web/20120106031235/http://www.playwitharena.com/?Newsticker:Archive_9) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](Arena "Arena") - Archive 9, 132, May 10, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))


### Implementations


* [UCI Engine Support for Android](http://www.aartbik.com/MISC/uchess.html) by [Aart Bik](Aart_Bik "Aart Bik")
* [Back to the 80's with UCI](http://www.top-5000.nl/mephisto.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder") » [Mephisto](Mephisto "Mephisto")
* [Senjo C++ UCI Adapter](https://github.com/zd3nik/SenjoUCIAdapter) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester") » [Clubfoot](Clubfoot "Clubfoot"), [C++](Cpp "Cpp")
* [GitHub - freeeve/uci: a UCI (Universal Chess Interface) API for golang](https://github.com/freeeve/uci) by [Eve Freeman](index.php?title=Eve_Freeman&action=edit&redlink=1 "Eve Freeman (page does not exist)") » [Go (Programming Language)](Go_(Programming_Language) "Go (Programming Language)")
* [nionita/chessNet · GitHub](https://github.com/nionita/chessNet) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita") » [Haskell](index.php?title=Haskell&action=edit&redlink=1 "Haskell (page does not exist)")


### [JavaScript](JavaScript "JavaScript")


* [Javascript Universal Chess Interface | Free software downloads at SourceForge.net](http://sourceforge.net/projects/jsuci/) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer")
* [GitHub - ebemunk/node-uci: UCI Protocol for node.js - talk to chess engines painlessly](https://github.com/ebemunk/node-uci) by [Buğra Fırat](index.php?title=Bu%C4%9Fra_F%C4%B1rat&action=edit&redlink=1 "Buğra Fırat (page does not exist)") [[11]](#cite_note-11)


 [node-uci Documentation](https://ebemunk.com/node-uci/)
* [GitHub - imor/uci: A thin wrapper on a uci chess engine](https://github.com/imor/uci)


## Video Tutorials


* An overview of the UCI protocol from a programmer's perspective by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* Implementing the UCI protocol in your engine (pseudo code) by [Jonathan Warkentin](Jonathan_Warkentin "Jonathan Warkentin"), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. [↑](#cite_ref-1) [Interview with SOS programmer Rudolf Huber in German language!](https://web.archive.org/web/20120106031235/http://www.playwitharena.com/?Newsticker:Archive_9) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](Arena "Arena") - Archive 9, 132, May 10, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
2. [↑](#cite_ref-2) [Universal Chess Interface From Wikipedia](https://en.wikipedia.org/wiki/Universal_Chess_Interface)
3. [↑](#cite_ref-3) [Arena, Interviews mit Prof. Dr. Robert Hyatt, Tim Mann und Martin Blume](http://web.archive.org/web/20020925204655fw_/http://www.playwitharena.com/directory/interviews/interviews.htm) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") for [ChessBits](ChessBits "ChessBits"), No. 18, May 2002 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
4. [↑](#cite_ref-4) [Re: PGN standard, its improvement and standardization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72019&start=36) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), October 14, 2019 » from [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") to [Protocols](Protocols "Protocols")
5. [↑](#cite_ref-5) [The alternative to Crafty, Interview with Fabien Letouzey](http://www.playwitharena.com/?Newsticker:Archive_7) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](Arena "Arena") - Archive , Page 7, 96, April 05, 2005
6. [↑](#cite_ref-6) [Re: Ugly UCI](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=58392&hilit=winboard&start=20#p650169) by [Kempelen](Kempelen "Kempelen"), [CCC](CCC "CCC"), November 29, 2015 » [Protocols](Protocols "Protocols")
7. [↑](#cite_ref-7) [Re: PGN standard, its improvement and standardization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72019&start=36) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), October 14, 2019 » from [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") to [Protocols](Protocols "Protocols")
8. [↑](#cite_ref-8) [Javascript Universal Chess Interface | Free software downloads at SourceForge.net](http://sourceforge.net/projects/jsuci/) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer")
9. [↑](#cite_ref-9) [中国象棋电脑应用规范(五)：中国象棋通用引擎协议](http://www.xqbase.com/protocol/cchess_ucci.htm) Universal Chinese Chess Protocol (UCCI)
10. [↑](#cite_ref-10) [3 interviews about engine protocols with T. Mann, R. Hyatt and M. Blume](https://www.stmintz.com/ccc/index.php?id=245615) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), August 15, 2002
11. [↑](#cite_ref-11) [Node.js from Wikipedia](https://en.wikipedia.org/wiki/Node.js)

**[Up one Level](Protocols "Protocols")**







 
