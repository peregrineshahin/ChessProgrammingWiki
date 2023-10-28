---
title: Auto232
---
**[Home](Home "Home") * [Protocols](Protocols "Protocols") * Auto232**

[](File:Sorcerersapprentice.JPG) Zauberlehrling <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Auto232**,

an autoplayer protocol based on the [serial communication](https://en.wikipedia.org/wiki/Serial_communication) [RS-232](https://en.wikipedia.org/wiki/RS-232) standard. It was initially developed by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") in the mid 90s to communicate with the [Chess 232 Board](Chess_232_Board "Chess 232 Board"). A [MS-DOS](MS-DOS "MS-DOS") [TSR](https://en.wikipedia.org/wiki/Terminate_and_stay_resident_program) driver, available for various [chess programs](MS-DOS#Engines "MS-DOS"), was able to "hook" into their printer output to parse their [moves](Moves "Moves") played, and to [redirect](<https://en.wikipedia.org/wiki/Redirection_(computing)>) input and commands into the [keyboard buffer](https://en.wikipedia.org/wiki/Keyboard_buffer) to start new games and [enter moves](Entering_Moves "Entering Moves").

With two [PCs](IBM_PC "IBM PC"), or two [COM ports](<https://en.wikipedia.org/wiki/COM_(hardware_interface)>) even with one computer <a id="cite-note-2" href="#cite-ref-2">[2]</a>, connected by a modified [null-modem](https://en.wikipedia.org/wiki/Null_modem) cable, it was now possible to play matches between two programs automaticly, a huge relief for testers and [engine rating list](Engine_Rating_Lists "Engine Rating Lists") organizations like [SSDF](SSDF "SSDF"). The Auto232 product with cable and software was purchased by [CSS-Shop](Dieter_Steinwender#CSS "Dieter Steinwender") and [Gambit-Soft](index.php?title=Gambit-Soft&action=edit&redlink=1 "Gambit-Soft (page does not exist)").

## Contents

- [1 Windows](#windows)
- [2 See also](#see-also)
- [3 Publications](#publications)
- [4 Forum Posts](#forum-posts)
  - [4.1 1997 ...](#1997-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2005 ...](#2005-...)
  - [4.4 2010 ...](#2010-...)
- [5 External Links](#external-links)
- [6 References](#references)

## Windows

A free [Windows](Windows "Windows") Auto232 driver written by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") <a id="cite-note-3" href="#cite-ref-3">[3]</a> allowed automatic play also between Windows programs. Auto232 was further incorporated inside various [GUIs](GUI "GUI") and engines, but implementations were at times buggy and the protocol not that reliable specially concerning game termination <a id="cite-note-4" href="#cite-ref-4">[4]</a>. With the advent and wider distribution of the standardized [computer chess protocols](Protocols "Protocols") such as the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") / [XBoard](XBoard "XBoard") and the [Universal Chess Interface](UCI "UCI"), Auto232 became obsolete and outdated.

## See also

- [Chess 232 Board](Chess_232_Board "Chess 232 Board")
- [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")

[WinBoard](WinBoard "WinBoard")
[XBoard](XBoard "XBoard")

- [UCI](UCI "UCI")

## Publications

- [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *Zauberlehrling - Das Auto232-Protokoll im Detail*. [CSS](Computerschach_und_Spiele "Computerschach und Spiele") 1/96, [pdf](http://www.mustrum.de/chrilly/auto232.pdf) (German) <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## Forum Posts

## 1997 ...

- [Technische Spezifikation des 232-Protokolls](https://groups.google.com/d/msg/rec.games.chess.computer/Y26C-mjUWqE/yojGpxsy4gkJ) (German) by [Harald Faber](index.php?title=Harald_Faber&action=edit&redlink=1 "Harald Faber (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 08, 1997
- [Windows driver for CHESS 232 board an Autoplayer 232](https://www.stmintz.com/ccc/index.php?id=11806) by [Bert Seifriz](index.php?title=Berthold_Seifriz&action=edit&redlink=1 "Berthold Seifriz (page does not exist)"), [CCC](CCC "CCC"), November 09, 1997

**1998**

- [AUTO232 question](https://www.stmintz.com/ccc/index.php?id=15383) by [Amir Ban](Amir_Ban "Amir Ban"), [CCC](CCC "CCC"), March 01, 1998
- [Smartboard, Auto232](https://www.stmintz.com/ccc/index.php?id=15053) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), February 14, 1998
- [Kill this auto232-players](https://www.stmintz.com/ccc/index.php?id=17744) by Peter Herttrich, [CCC](CCC "CCC"), April 29, 1998
- [Survey proposal: Importance of Auto232 compatibility](https://www.stmintz.com/ccc/index.php?id=26251) by [Moritz Berger](Moritz_Berger "Moritz Berger"), [CCC](CCC "CCC"), September 09, 1998
- [Autoplayer for Win32 (again)](https://www.stmintz.com/ccc/index.php?id=26448) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), September 12, 1998
- [Auto232](https://groups.google.com/d/msg/rec.games.chess.computer/_0QqhmplNvc/Hw235ChCMNEJ) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 12, 1998
- [Autoplayers and Bean-Counters](https://groups.google.com/d/msg/rec.games.chess.computer/Jt6Xt11aAV0/nKEElQKgdVkJ) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 18, 1998

**1999**

- [AUTO232 and memory protection](https://www.stmintz.com/ccc/index.php?id=42019) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 03, 1999
- [Re: Auto232 questions, here is the manual in English!](https://www.stmintz.com/ccc/index.php?id=48326) by [Harald Faber](index.php?title=Harald_Faber&action=edit&redlink=1 "Harald Faber (page does not exist)"), [CCC](CCC "CCC"), April 07, 1999
- [Re: What Is Auto232?](https://www.stmintz.com/ccc/index.php?id=49575) by [Harald Faber](index.php?title=Harald_Faber&action=edit&redlink=1 "Harald Faber (page does not exist)"), [CCC](CCC "CCC"), April 23, 1999
- [Re: my own auto232 player](https://www.stmintz.com/ccc/index.php?id=81208) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), December 07, 1999

## 2000 ...

- [Re: Auto232 with one machine?](https://www.stmintz.com/ccc/index.php?id=93127) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), January 29, 2000
- [end of auto232?](https://www.stmintz.com/ccc/index.php?id=99969) by [Harald Faber](index.php?title=Harald_Faber&action=edit&redlink=1 "Harald Faber (page does not exist)"), [CCC](CCC "CCC"), March 03, 2000
- [Definition of the Extended Autoplayer 232 Protocol](https://www.stmintz.com/ccc/index.php?id=111002) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), May 16, 2000
- [Auto232, and one computer](https://www.stmintz.com/ccc/index.php?id=125103) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), August 18, 2000
- [Auto232 - Anyone with a good source of info on how to use it?](https://www.stmintz.com/ccc/index.php?id=139298) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), November 17, 2000
- [Auto232 using a network](https://www.stmintz.com/ccc/index.php?id=180062) by Fabio Barrettone, [CCC](CCC "CCC"), July 17, 2001
- [how to run auto232 with 1 pc](https://www.stmintz.com/ccc/index.php?id=232525) by Mustafa, [CCC](CCC "CCC"), May 28, 2002
- [auto232](https://www.stmintz.com/ccc/index.php?id=261225) by Christophe Drieu, [CCC](CCC "CCC"), October 23, 2002
- [Auto232 1.0 revisited](https://www.stmintz.com/ccc/index.php?id=318146) by Michael P. Nance Sr., [CCC](CCC "CCC"), September 27, 2003
- [auto232 without null modem cable](https://www.stmintz.com/ccc/index.php?id=360549) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), April 18, 2004

## 2005 ...

- [Chess programs using Auto232](https://www.stmintz.com/ccc/index.php?id=448028) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [CCC](CCC "CCC"), September 06, 2005
- [Auto232 with only USB ports (solution?)](https://www.stmintz.com/ccc/index.php?id=476954) by James T. Walker, [CCC](CCC "CCC"), January 04, 2006
- [How do I connect using auto232 to ICC using Fritz GUI?](http://www.talkchess.com/forum/viewtopic.php?t=28407) by LJC, [CCC](CCC "CCC"), June 14, 2009

## 2010 ...

- [Eberhard Boerger's Auto232 adaptor/Remi Coulom's Auto232](http://www.talkchess.com/forum/viewtopic.php?t=51509) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)"), [CCC](CCC "CCC"), March 06, 2014
- [Auto232 Driver for DOS (and Windows?)](http://www.talkchess.com/forum/viewtopic.php?t=56944) by Theo Heinze, [CCC](CCC "CCC"), July 11, 2015

## External Links

- [Auto232 player - Auto232 and Winboard](http://horizonchess.com/FAQ/Winboard/auto232player.html) by [Aaron Tay](Aaron_Tay "Aaron Tay"), hosted by [Ron Murawski](Ron_Murawski "Ron Murawski")
- [Schachclub Leinzell - Autoplayer 232](http://scleinzell.schachvereine.de/p_basiswissen/autoplayer.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), May 2000 (German)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Zauberlehrling](<https://de.wikipedia.org/wiki/Zauberlehrling_(Oberhausen)>) ([The Sorcerer's Apprentice](https://en.wikipedia.org/wiki/The_Sorcerer%27s_Apprentice)) by [Inges Idee](https://en.wikipedia.org/wiki/Inges_Idee) - a 35 meter steel tower like a dancing electricity pylon, installed at [Emscherkunst](https://de.wikipedia.org/wiki/Emscherkunst) art exhibition 2013 near [Haus Ripshorst](https://de.wikipedia.org/wiki/Haus_Ripshorst), [Gasometer Oberhausen](https://en.wikipedia.org/wiki/Gasometer_Oberhausen) in the background, [Oberhausen](https://en.wikipedia.org/wiki/Oberhausen), Germany, [The Industrial Heritage Trail](Category:Industrial_Heritage_Trail "Category:Industrial Heritage Trail"), Image by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), October 11, 2015
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Auto232, and one computer](https://www.stmintz.com/ccc/index.php?id=125103) by [Peter Skinner](Peter_Skinner "Peter Skinner"), [CCC](CCC "CCC"), August 18, 2000
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Windows driver for CHESS 232 board an Autoplayer 232](https://www.stmintz.com/ccc/index.php?id=11806) by [Bert Seifriz](index.php?title=Berthold_Seifriz&action=edit&redlink=1 "Berthold Seifriz (page does not exist)"), [CCC](CCC "CCC"), November 09, 1997
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Auto232 - Anyone with a good source of info on how to use it?](https://www.stmintz.com/ccc/index.php?id=139460) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 17, 2000
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [The Sorcerer's Apprentice (Zauberlehrling) from Wikipedia](https://en.wikipedia.org/wiki/The_Sorcerer%27s_Apprentice)

**[Up one Level](Protocols "Protocols")**

