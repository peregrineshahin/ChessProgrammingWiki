---
title: Chess Engine Communication Protocol
---
**[Home](Home "Home") * [Protocols](Protocols "Protocols") * Chess Engine Communication Protocol**

**Chess Engine Communication Protocol** (CECP),\
also dubbed the **XBoard** or **WinBoard** protocol after the eponymous [XBoard](XBoard "XBoard") or [WinBoard](WinBoard "WinBoard") [graphical user interfaces](GUI "GUI") (GUI), is an open [communication protocol](https://en.wikipedia.org/wiki/Communication_protocol) for chess engines to play [games](Chess_Game "Chess Game") automatically, that is to communicate with other chess playing entities.

## GUI

A [GUI](GUI "GUI") supporting the protocol is known as [XBoard](XBoard "XBoard") or [WinBoard](WinBoard "WinBoard"), being for [Unix](Unix "Unix") (Posix) or [Windows](Windows "Windows") operating systems, respectively. Many other GUIs support the protocol, which is based on text commands, while requiring the engine to keep the state of the game internally. While the [Universal Chess Interface](UCI "UCI") is somewhat more popular today, the Chess Engine Communication Protocol protocol is preferred by some because it allows greater flexibility for the engine (for instance, in [pondering](Pondering "Pondering")).

## How it began

[Tim Mann](Tim_Mann "Tim Mann") in an Interview by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), April 2000 <a id="cite-note-1" href="#cite-ref-1">[1]</a>:

```C++
Originally, xboard and WinBoard were simply graphical user interfaces for [GNU Chess](GNU_Chess "GNU Chess"), then for GNU Chess and [Internet chess servers](Chess_Server "Chess Server"). Because the [GUI](GUI "GUI") and the chess engine are separate programs, several people thought of the idea of connecting their own chess programs in place of GNU Chess, and they began to email me asking how to do it. I think the first person to ask was [Shay Bushinsky](Shay_Bushinsky "Shay Bushinsky"), in November 1994. Over the years I received so many requests for this information that I was more or less forced into documenting and extending the ad-hoc engine protocol to support them. The document that exists now (chess-engines.html) evolved directly from the original email reply I sent to Shay. Unfortunately, because the protocol was never really designed, but just grew out of documenting the existing communication with GNU Chess, there are still several bugs and deficiencies in it today. It would be nice to make some major revisions, but then of course it would (at best) take a long time for the existing engines to convert over to the new protocol, so both would have to be supported, probably forever. 

```

## UML State diagram

[](http://walkofmind.com/programming/chess/xboard.htm)
WinBoard/XBoard protocol [UML state diagram](https://en.wikipedia.org/wiki/UML_state_machine) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Version 2

[Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") established a protocol Version 2 in September, 2009 <a id="cite-note-4" href="#cite-ref-4">[4]</a>, also covering [Chess Variants](Games "Games") and different board sizes.

## Pros and Cons

Those pros and cons compared with [UCI](UCI "UCI")

## Pros

- All commands are short
- Has redundant commands for almost all chess tasks from old-time to now
- Designed to work without the need of having an extra thread for processing those commands
- Allows users to play directly with chess engines without using chess GUIs
- Allows chess engines act a bit independently such as they can auto-start pondering after a move

## Cons

- Has a long and complicated list of commands
- Use many assumptions about data without keywords requirements. For example, the string "a2a3" is considered as a move, "9 156 1084 48000 Nf3 Nc6 Nc3 Nf6" is considered as a computing output when the first number is the ply, the second number is a score in centipawn unit...
- Since allowing chess engines acting more independently chess GUIs may get loss to control engines
- Some popular chess GUIs don't support
- The majority of new chess engines don't support

## Engines

- [WinBoard Engines](Category:WinBoard "Category:WinBoard")
- [XBoard Engines](Category:XBoard "Category:XBoard")

## GUIs

## Native

- [WinBoard](WinBoard "WinBoard")
- [XBoard](XBoard "XBoard")

## Compatible

- [Arena](Arena "Arena")
- [ChessGUI](ChessGUI "ChessGUI")
- [ChessPartner](ChessPartner "ChessPartner")
- [ChessX](ChessX "ChessX")
- [Cute Chess](Cute_Chess "Cute Chess")
- [EBoard](index.php?title=EBoard&action=edit&redlink=1 "EBoard (page does not exist)")
- [jose](index.php?title=Jose&action=edit&redlink=1 "Jose (page does not exist)")
- [PyChess](PyChess "PyChess")
- [SCID](SCID "SCID")
- [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
- [Scidb](Scidb "Scidb")
- [Banksia](Banksia "Banksia")
- [Banksia GUI](Banksia_GUI "Banksia GUI")

## Utilities

- [InBetween](InBetween "InBetween")
- [PolyGlot](PolyGlot "PolyGlot")
- [Wb2UCI](Wb2UCI "Wb2UCI")
- [UCI2WB](UCI2WB "UCI2WB")

## See also

- [CPW-Engine_com](CPW-Engine_com "CPW-Engine com")
- [Engine Testing](Engine_Testing "Engine Testing")
- [GNU Chess](GNU_Chess "GNU Chess")
- [icsdrone](index.php?title=Icsdrone&action=edit&redlink=1 "Icsdrone (page does not exist)")
- [Pondering](Pondering "Pondering")
- [UCI](UCI "UCI")
- [Vice XBoard/WiBoard-Videos](Vice#CECP "Vice")

## Forum Posts

## 1990 ...

- [xboard datapoint](http://groups.google.com/group/gnu.chess/browse_frm/thread/40206c9937414b0d) by Paul Vaughan, [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), January 29, 1991
- [xboard v1.2](http://groups.google.com/group/gnu.chess/browse_frm/thread/28d5826a078d091d) by Chris Sears, [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), June 14, 1991
- [reading in a position and playing in xboard](http://groups.google.com/group/gnu.chess/browse_frm/thread/4dc93bfa82e41a08) by [Lewis Stiller](Lewis_Stiller "Lewis Stiller"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), February 20, 1992
- [Re: Accessing remote computers with WinBoard](http://groups.google.com/group/gnu.chess/browse_frm/thread/a7d8892d10f66aff) by [Tim Mann](Tim_Mann "Tim Mann"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), November 7, 1993

## 1995 ...

- [XBoard and WinBoard 3.4, patchlevel 1](http://groups.google.com/group/rec.games.board/browse_frm/thread/63700b0fcfa8b39e) by [Tim Mann](Tim_Mann "Tim Mann"), [rec.games.board](Computer_Chess_Forums "Computer Chess Forums"), December 13 1995
- [XBoard and WinBoard, version 3.6.0](https://groups.google.com/d/msg/rec.games.chess.misc/M-NkXvEu1DM/XeESczC85o0J) by [Tim Mann](Tim_Mann "Tim Mann"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), May 09, 1997
- [new autoplayer interface standard](https://www.stmintz.com/ccc/index.php?id=26696) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 15, 1998
- [xboard/winboard interface documentation](https://groups.google.com/d/msg/rec.games.chess.computer/su1X8FrRMPA/dMUBRY-RT4AJ) by [Jan Eric Larsson](Jan_Eric_Larsson "Jan Eric Larsson"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 27, 1998
- [WinBoard and pondering under W98](https://www.stmintz.com/ccc/index.php?id=62577) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), July 28, 1999 » [Pondering](Pondering "Pondering"), [WinBoard](WinBoard "WinBoard")

## 2000 ...

- [Winboard for Dummies](https://groups.google.com/d/msg/rec.games.chess.computer/r5-Kdb4p4bE/tKCt-SwZKlgJ) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 30, 2001
- [xboard and WinBoard 4.2.4 released](http://groups.google.com/group/gnu.chess/browse_frm/thread/3fffd13e5ba818aa) by [Tim Mann](Tim_Mann "Tim Mann"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), December 10, 2001
- [what is the importance of the ping command?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39184) by [Uri Blass](Uri_Blass "Uri Blass"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2002
- [Kiwi for Win98 and input-reading stuff](https://www.stmintz.com/ccc/index.php?id=389667) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), September 29, 2004 » [Kiwi](Kiwi "Kiwi"), [Windows](Windows "Windows"), [C++](Cpp "Cpp"), [Thread](Thread "Thread")

## 2005 ...

- [Safe I/O (repeated)](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1622) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2005
- [A question about kibitz](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1693&p=7809) by [Niyaz Khasanov](index.php?title=Niyaz_Khasanov&action=edit&redlink=1 "Niyaz Khasanov (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 18, 2005
- [Re: gnuchess/xboard protocol](http://lists.gnu.org/archive/html/info-gnu-chess/2006-05/msg00004.html) by [Hans Eric Sandström](index.php?title=Hans_Eric_Sandstr%C3%B6m&action=edit&redlink=1 "Hans Eric Sandström (page does not exist)"), [gnu.org](GNU_Chess#NewsGroup "GNU Chess"), May 19, 2006
- [Authors of WinBoard SMP engines, take note!](http://www.talkchess.com/forum/viewtopic.php?t=24327) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 11, 2008 » [Parallel Search](Parallel_Search "Parallel Search"), [SMP](SMP "SMP")
- [UCI protocol in winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=19&t=50429) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2009 » [UCI](UCI "UCI"), [WinBoard](WinBoard "WinBoard")
- [Adapter for non-standard chess engine to Winboard](http://www.talkchess.com/forum/viewtopic.php?t=30088) by [Carey](Carey_Bloodworth "Carey Bloodworth"), [CCC](CCC "CCC"), October 10, 2009

## 2010 ...

- [XBoard and epd tournament](http://www.talkchess.com/forum/viewtopic.php?t=32254) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), January 31, 2010 » [Engine Testing](Engine_Testing "Engine Testing")
- [Aquarium (other GUIs too?) and WB support => I am shocked](http://www.talkchess.com/forum/viewtopic.php?t=32952) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), February 27, 2010

**2011**

- [WinBoard protocol driver](http://www.open-aurec.com/wbforum/viewtopic.php?f=24&t=51739) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum - Chess Programming Lessons](Computer_Chess_Forums "Computer Chess Forums"), April 30, 2011
- [Starting to use the Winboard Protocol](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52093) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 11, 2011

**2012**

- [XBoard / WinBoard 4.6.0 released](http://www.talkchess.com/forum/viewtopic.php?t=42834) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 11, 2012
- [Winboard protocol and fractional increments](http://www.talkchess.com/forum/viewtopic.php?t=45325) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 25, 2012 » [Time Management](Time_Management "Time Management")

**2013**

- [A few questions about CECP](http://www.talkchess.com/forum/viewtopic.php?t=46780) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), January 05, 2013
- [WB protocol: describing how a piece moves](http://www.talkchess.com/forum/viewtopic.php?t=49683) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 12, 2013

**2014**

- [WB protocol extension: thinking output](http://www.talkchess.com/forum/viewtopic.php?t=50903) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 14, 2014
- [Handling xboard new game race condition in protover 1 engine](http://www.talkchess.com/forum/viewtopic.php?t=53265) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 12, 2014
- [for Chess-variant authors](http://www.talkchess.com/forum/viewtopic.php?t=53734) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 17, 2014
- [XBoard and chess variants](http://www.talkchess.com/forum/viewtopic.php?t=54124) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 28, 2014
- [UCCI2WB](http://www.talkchess.com/forum/viewtopic.php?t=54162) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 27, 2014
- [WB protocol specs](http://www.talkchess.com/forum/viewtopic.php?t=54629) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 12, 2014

## 2015 ...

- [xboard softquit](http://www.talkchess.com/forum/viewtopic.php?t=57082) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 26, 2015
- [Winboard 2 state diagram](http://www.open-chess.org/viewtopic.php?f=5&t=2871&p=22300) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 26, 2015
- [XBoard for Mac: Zippy problems](http://www.talkchess.com/forum/viewtopic.php?t=57430) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 29, 2015 » [Mac OS](Mac_OS "Mac OS")
- [Suggestions for XBoard documentation](http://www.talkchess.com/forum/viewtopic.php?t=57446) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 30, 2015
- [CECP ('WB protocol') specs](http://www.talkchess.com/forum/viewtopic.php?t=58714) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 28, 2015

**2016**

- [Release of XBoard 4.9.0 soon](http://www.talkchess.com/forum/viewtopic.php?t=59784) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 07, 2016
- [Chess on Android](http://www.talkchess.com/forum/viewtopic.php?t=59905) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), April 19, 2016 » [Chess for Android](Chess_for_Android "Chess for Android"), [DanaSah](DanaSah "DanaSah")
- [CECP: Chess variants with dice](http://www.talkchess.com/forum/viewtopic.php?t=60239) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 22, 2016
- [ChessGUI Timer Problem](http://www.talkchess.com/forum/viewtopic.php?t=61823) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), October 24, 2016 » [ChessGUI](ChessGUI "ChessGUI")

**2017**

- [Winboard variants online](http://www.talkchess.com/forum/viewtopic.php?t=63525) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), March 22, 2017 » [Chess Variants](Chess#Variants "Chess")
- [Winboard questions](http://www.talkchess.com/forum/viewtopic.php?t=64411) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 26, 2017
- [Winboard: Resigning?](http://www.talkchess.com/forum/viewtopic.php?t=64432) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), June 27, 2017
- [Loading opening book and tablebases (xboard vs uci)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=65454) by [Pedro Castro](Pedro_Castro "Pedro Castro"), [CCC](CCC "CCC"), October 15, 2017 » [UCI](UCI "UCI")

**2018 ...**

- [UCI vs Winboard question](http://www.talkchess.com/forum/viewtopic.php?t=66745) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 05, 2018 » [UCI](UCI "UCI")
- [Winboard state machine diagram](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70502) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), April 15, 2019
- [Xboard, CECP, how to handle long inits](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71186) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 04, 2019
- [Re: PGN standard, its improvement and standardization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72019&start=36) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), October 14, 2019 » from [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") to [Protocols](Protocols "Protocols")

## 2020 ...

- [UCI to CECP](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73592) by Fulvio, [CCC](CCC "CCC"), April 07, 2020 » [UCI](UCI "UCI")
- [Rolling dice](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74028) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 27, 2020 » [EinStein würfelt nicht!](EinStein_w%C3%BCrfelt_nicht! "EinStein würfelt nicht!")
- [Questions about CECP post-nopost (UCI info)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75239) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), September 28, 2020
- [CECP "time" and "otim"](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75944) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), November 30, 2020 » [Time Management](Time_Management "Time Management")
- [FRC in CECP](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76106) by lucasart, [CCC](CCC "CCC"), December 20, 2020 » [Chess960](Chess960 "Chess960")

## External Links

- [Chess Engine Communication Protocol - GNU Project - Free Software Foundation](https://www.gnu.org/software/xboard/engine-intf.html)
- [Chess Engine Communication Protocol from Wikipedia](https://en.wikipedia.org/wiki/Chess_Engine_Communication_Protocol)
- [Chess-Engine Communication Protocol](http://hgm.nubati.net/CECP.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
- [Chess Engine Communication Protocol](http://home.hccnet.nl/h.g.muller/engine-intf.html) by [Tim Mann](Tim_Mann "Tim Mann") & [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
- [Chess Engine Communication Protocol - New Specs](http://hgm.nubati.net/newspecs.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [XBoard News](http://hgm.nubati.net/news.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")

[What is new in XBoard/WinBoard 4.9.0?](http://hgm.nubati.net/XB-4.9.0/) by [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")

- [Tim Mann's Chess Pages, XBoard and WinBoard](http://timmann.server269.com/xboard.html)

[rshd-readme.txt](http://www.tim-mann.org/winboard/rshd-readme.txt) by [Dan Newman](Dan_Newman "Dan Newman") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>

- [bug-xboard mail archive](http://www.mail-archive.com/bug-xboard@gnu.org/maillist.html)
- [Tinkering with Winboard...](http://walkofmind.com/programming/chess/winboard_x.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")

[Winboard/XBoard UML state diagram](http://walkofmind.com/programming/chess/xboard.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")

- [FAQ on Winboard and Chess Engines](http://www.horizonchess.com/FAQ/Winboard/index.html) by [Aaron Tay](Aaron_Tay "Aaron Tay")
- [Lyapko George's WinBoard related page](http://www.oocities.org/siliconvalley/lab/6606/winboard.htm) (outdated) by [George Lyapko](George_Lyapko "George Lyapko") <a id="cite-note-9" href="#cite-ref-9">[9]</a>
- [Winboard and Chess Engines FAQ](http://computer-chess.org/doku.php?id=winboard:faq:index) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [WinBoard development and bugfixing Forum](http://www.open-aurec.com/wbforum/viewforum.php?f=19)
- [Arena, Interviews mit Prof. Dr. Robert Hyatt, Tim Mann und Martin Blume](http://web.archive.org/web/20020925204655fw_/http://www.playwitharena.com/directory/interviews/interviews.htm) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") for [ChessBits](ChessBits "ChessBits"), No. 18, May 2002 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)) » [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Tim Mann](Tim_Mann "Tim Mann"), [Martin Blume](Martin_Blume "Martin Blume") <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [XBoard Project History](http://tim-mann.org/history.html)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Winboard/XBoard UML state diagram](http://walkofmind.com/programming/chess/xboard.htm) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Winboard state machine diagram](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70502) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), April 15, 2019
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Engine Communication Protocol](http://home.hccnet.nl/h.g.muller/engine-intf.html) by [Tim Mann](Tim_Mann "Tim Mann") & [H.G. Muller](Harm_Geert_Muller "Harm Geert Muller")
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [CECP ('WB protocol') specs](http://www.talkchess.com/forum/viewtopic.php?t=58714) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 28, 2015
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [WB protocol specs](http://www.talkchess.com/forum/viewtopic.php?t=54629) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 12, 2014
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Remote Shell from Wikipedia](https://en.wikipedia.org/wiki/Remote_Shell)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Windows Implementation of RSHD](http://rshd.sourceforge.net/)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Tool to recreate PGN from winboard.debug?](http://www.talkchess.com/forum/viewtopic.php?t=46721) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 01, 2013
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [3 interviews about engine protocols with T. Mann, R. Hyatt and M. Blume](https://www.stmintz.com/ccc/index.php?id=245615) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), August 15, 2002

**[Up one Level](Protocols "Protocols")**

