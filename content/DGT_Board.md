---
title: DGT Board
---
**[Home](Home "Home") * [User Interface](User_Interface "User Interface") * [Sensory Board](Sensory_Board "Sensory Board") * DGT Board**

**DGT Board**,

a sensory board developed and market by [Digital Game Technology](index.php?title=DGT&action=edit&redlink=1 "DGT (page does not exist)"). The board in conjunction with a [digital chess clock](https://en.wikipedia.org/wiki/Game_clock#Early_development_of_digital_game_clocks) is connected to a host computer and its [chess gui](GUI "GUI") or control program via [USB](https://en.wikipedia.org/wiki/USB), [serial interface](https://en.wikipedia.org/wiki/Serial_communication), or [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth), and acts as a [real-time](https://en.wikipedia.org/wiki/Real_time_%28media%29) [move input device](Entering_Moves "Entering Moves") during [game play](Chess_Game "Chess Game"), to monitor or [broadcast](https://en.wikipedia.org/wiki/Live_broadcast) the game, or to give [chess engines](Engines "Engines") a whiff of [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers").

## Contents

- [1 Piece Recognition](#piece-recognition)
  - [1.1 Sensor Technology](#sensor-technology)
  - [1.2 Inside the Board](#inside-the-board)
  - [1.3 Scanning the Board](#scanning-the-board)
- [2 Applications](#applications)
  - [2.1 Chess GUIs](#chess-guis)
  - [2.2 Gavon](#gavon)
  - [2.3 PicoChess](#picochess)
  - [2.4 Revelation II](#revelation-ii)
  - [2.5 DGT LiveChess Software](#dgt-livechess-software)
  - [2.6 DGT Pi](#dgt-pi)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
  - [4.1 1998 ...](#1998-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2005 ...](#2005-...)
  - [4.4 2010 ...](#2010-...)
  - [4.5 2015 ...](#2015-...)
  - [4.6 2020 ...](#2020-...)
- [5 External Links](#external-links)
- [6 References](#references)

## Piece Recognition

## Sensor Technology

The patent-registered DGT sensor technology <a id="cite-note-1" href="#cite-ref-1">[1]</a> [recognizes pieces](Piece_Recognition "Piece Recognition") containing piece-type and piece-color specific passive [LC circuits](https://en.wikipedia.org/wiki/LC_circuit) with a [resonance frequency](https://en.wikipedia.org/wiki/Resonance) of 90 to 350 KHz, the [coil](https://en.wikipedia.org/wiki/Coil) on [ferrite core](https://en.wikipedia.org/wiki/Ferrite_core). [Squares](Squares "Squares") and their respective pieces (if any) are scanned by 2 x 8 [silver-ink](https://en.wikipedia.org/wiki/Conductive_ink) printed trace loops on a [polyester](https://en.wikipedia.org/wiki/Polyester) film placed under the board, [file](Files "Files") and [rank](Ranks "Ranks") sequentially selected by [analogue switch](https://en.wikipedia.org/wiki/Analogue_switch) [multiplexers](https://en.wikipedia.org/wiki/Multiplexer), [feeding back](https://en.wikipedia.org/wiki/Feedback) the output signal of an [amplifier](https://en.wikipedia.org/wiki/Amplifier) via the selected [inductive coupled](https://en.wikipedia.org/wiki/Inductive_coupling) LC circuit to its input, forcing [oscillation](https://en.wikipedia.org/wiki/Oscillation) in piece specific [resonance](https://en.wikipedia.org/wiki/Resonance). Measuring the signal frequency or its [period](https://en.wikipedia.org/wiki/Period) via a digital [input port](https://en.wikipedia.org/wiki/Input_port) by the controller [firmware](https://en.wikipedia.org/wiki/Firmware) to convert it into appropriate piece codes takes about 3 ms per square <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

## Inside the Board

[](http://en.chessbase.com/post/dgt-presents-new-clocks-technology-and-vladimir-kramnik)
Inside the DGT Board <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Scanning the Board

```

void scanBoard(char *board) {
   for (int rank = 0; rank < 8; rank++) {
      switchRankMultiplexer( rank );
      for (int file = 0; file < 8; file++) {
         connectFileMultiplexer( file );
         int f = measureFrequency(); /* e.g. in a 0 .. 35 range ~ 3 ms */
         *board++ = pieceTable[f]; /* includes empty (0) */
      }
   }
}

```

## Applications

## Chess GUIs

The DGT Board can be used with most [GUI's](GUI "GUI") <a id="cite-note-4" href="#cite-ref-4">[4]</a> , such as [Fritz GUI](Fritz#FritzGUI "Fritz") by [ChessBase](ChessBase "ChessBase"), [Chess Assistant](Chess_Assistant "Chess Assistant") and [Aquarium](Aquarium "Aquarium") by [ChessOK](ChessOK "ChessOK"), [Shredder GUI](Shredder "Shredder"), [Arena](Arena "Arena"), [PocketGrandmaster](PocketGrandmaster "PocketGrandmaster"), [WinBoard](WinBoard "WinBoard") <a id="cite-note-5" href="#cite-ref-5">[5]</a> and [XBoard](XBoard "XBoard"). The open source **dgtdrv** library by [Pierre Boulenguez](index.php?title=Pierre_Boulenguez&action=edit&redlink=1 "Pierre Boulenguez (page does not exist)") under [GPL](Free_Software_Foundation#GPL "Free Software Foundation") Version 2 or later, can be used to adapt almost every GUI to interact with the DGT board <a id="cite-note-6" href="#cite-ref-6">[6]</a>. Since v5.7 (2018), [Chess for Android](Chess_for_Android "Chess for Android") can connect to a DGT chessboard over [bluetooth](https://en.wikipedia.org/wiki/Bluetooth) or [USB](https://en.wikipedia.org/wiki/USB) (including older DGT models that use the [RS-232](https://en.wikipedia.org/wiki/RS-232) connector) on devices with [Android 6.0](Android "Android") and up (or even earlier for USB) <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> .

Chess for Android and DGT Board Connection, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## Gavon

[Josu Bergara Ede's](index.php?title=Josu_Bergara_Ede&action=edit&redlink=1 "Josu Bergara Ede (page does not exist)") dedicated [User Interface](User_Interface "User Interface") for various [open source chess engines](Category:Open_Source "Category:Open Source"), dubbed [Gavon](Gavon "Gavon"), based on the [Raspberry Pi](Raspberry_Pi "Raspberry Pi") is able to interface with the DGT USB or Bluetooth Board.

Gavon Bluetooth DGT Board Connection, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## PicoChess

[Jean-François Romang's](Jean-Francois_Romang "Jean-Francois Romang") [PicoChess](PicoChess "PicoChess") is a [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers") based on [Stockfish](Stockfish "Stockfish") on [Raspberry Pi](Raspberry_Pi "Raspberry Pi") and the DGT Board <a id="cite-note-9" href="#cite-ref-9">[9]</a> . The display of the digital chess clock acts as output device of a [command line interface](CLI "CLI").

[PicoChess](PicoChess "PicoChess") on a DGT eboard by [Jonas Žnidaršič](https://en.wikipedia.org/wiki/Jonas_%C5%BDnidar%C5%A1i%C4%8D), [BCE](http://bestchessmenever.com/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video <a id="cite-note-10" href="#cite-ref-10">[10]</a>

## Revelation II

DGT technology <a id="cite-note-11" href="#cite-ref-11">[11]</a> is involved in the [Revelation II](Revelation_II "Revelation II") [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers"), developed by [Ruud Martin's](Ruud_Martin "Ruud Martin") company [Phoenix Chess Systems](index.php?title=Phoenix_Chess_Systems&action=edit&redlink=1 "Phoenix Chess Systems (page does not exist)") in cooperation with DGT <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>.

Revelation II Test by [Jonas Žnidaršič](https://en.wikipedia.org/wiki/Jonas_%C5%BDnidar%C5%A1i%C4%8D), [BCE](http://bestchessmenever.com/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## DGT LiveChess Software

DGT LiveChess Software allows [live broadcast](https://en.wikipedia.org/wiki/Live_broadcast) of [chess games](Chess_Game "Chess Game") via the [internet](https://en.wikipedia.org/wiki/Internet) <a id="cite-note-14" href="#cite-ref-14">[14]</a> , as used for instance in recent [ICGA](ICGA "ICGA") and [CSVN](CSVN "CSVN") [computer chess tournaments](Tournaments_and_Matches "Tournaments and Matches") served by DGT employee, CSVN chairman and tournament director [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos"). Participants are advised to don't use the board for analyzing purposes, as it was quite usual in over the board computer chess with ordinary chessboards.

[](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/616-photo-s-pt45-gt27-day-1)
DGT Board in action for live broadcast at [PT 45](PT_45 "PT 45"), round 4, [Kallisto](Kallisto "Kallisto") - [The King](The_King "The King")\
[Bart Weststrate](Bart_Weststrate "Bart Weststrate") and [Johan de Koning](Johan_de_Koning "Johan de Koning"), [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") and [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") <a id="cite-note-15" href="#cite-ref-15">[15]</a>

## DGT Pi

[DGT Pi](DGT_Pi "DGT Pi") is a [dedicated chess computer](Dedicated_Chess_Computers "Dedicated Chess Computers") expansion hardware for the DGT Board integrated into a DGT3000 digital chess clock, released in October 2016 <a id="cite-note-16" href="#cite-ref-16">[16]</a>. DGT Pi consists of a [Raspberry Pi 3](Raspberry_Pi#3 "Raspberry Pi") with built-in [Bluetooth](https://en.wikipedia.org/wiki/Bluetooth) and [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi) functionality, and multiple chess engines included.

## See also

- [Chess for Android - Video](Chess_for_Android#Video "Chess for Android")
- [DGT Pi](DGT_Pi "DGT Pi")
- [Square Off](index.php?title=Square_Off&action=edit&redlink=1 "Square Off (page does not exist)")
- [TASC SmartBoard](TASC_SmartBoard "TASC SmartBoard")

## Forum Posts

## 1998 ...

- [To Bob H.: A Puzzlement about the DGT Board?](https://www.stmintz.com/ccc/index.php?id=30845) by [Steven Schwartz](Steven_Schwartz "Steven Schwartz"), [CCC](CCC "CCC"), October 28, 1998
- [DGT sensory board update](https://www.stmintz.com/ccc/index.php?id=33976) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 25, 1998
- [DGT vs Novag Universal](https://www.stmintz.com/ccc/index.php?id=40092) by Michael Ginat, [CCC](CCC "CCC"), January 19, 1999 » [Novag Universal Electronic Chess Board](Novag_Universal_Electronic_Chess_Board "Novag Universal Electronic Chess Board")

## 2000 ...

- [Does someone (Amir?) know the software used in Dortmund with DGT board?](https://www.stmintz.com/ccc/index.php?id=118813) by [Sylvain Renard](Sylvain_Renard "Sylvain Renard"), [CCC](CCC "CCC"), July 12, 2000
- [A question to other users - DGT board](https://www.stmintz.com/ccc/index.php?id=162914) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), April 11, 2001
- [Your thoughts on the DGT electronic chessboard](https://www.stmintz.com/ccc/index.php?id=201323) by Gerald Grimsley, [CCC](CCC "CCC"), December 10, 2001
- [How electronic chessboards works](http://groups.google.com/group/rec.games.chess.misc/msg/8734d1b2fffd6af0) by [Ben Bulsink DGT Project](http://digitalgametechnology.com/site/History/about-dgt.html), [rec.games.chess.misc](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2004
- [Crafty, Winboard, DGT and Move Annoucement](https://www.stmintz.com/ccc/index.php?id=361540) by [Mike Byrne](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), April 24, 2004

## 2005 ...

- [CEBoard now supports DGT Board](https://www.stmintz.com/ccc/index.php?id=464917) by [Alain Zanchetta](index.php?title=Alain_Zanchetta&action=edit&redlink=1 "Alain Zanchetta (page does not exist)"), [CCC](CCC "CCC"), November 27, 2005 » [CEBoard](index.php?title=CEBoard&action=edit&redlink=1 "CEBoard (page does not exist)")
- [DGT Board with Robot Arm](https://www.stmintz.com/ccc/index.php?id=481317) by Alfredo Delacruz, [CCC](CCC "CCC"), January 21, 2006
- [On the DGT piece recognition chessboard](http://www.talkchess.com/forum/viewtopic.php?t=25310) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 07, 2008

## 2010 ...

- [DGT Winboard interface](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=52438) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 19, 2012
- [DGT e-Board](http://www.talkchess.com/forum/viewtopic.php?t=48231) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 09, 2013
- [DGT and Android (or iPhone)](http://www.talkchess.com/forum/viewtopic.php?t=49660) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), October 10, 2013
- [Thoughts on the DGT chessboard](http://www.hiarcs.net/forums/viewtopic.php?t=6280) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 10, 2013
- [DGT board arrives -- serious disappointment](http://hiarcs.net/forums/viewtopic.php?t=6433&sid=748bb4336e8c6e0aecb1458ccf6de67e) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), November 16, 2013
- [DGT board and piece set arrive -- all issues resolved](http://hiarcs.net/forums/viewtopic.php?t=6456&sid=748bb4336e8c6e0aecb1458ccf6de67e) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2013
- [How to make a DGT Board ?](http://www.talkchess.com/forum/viewtopic.php?t=50344) by Sean Evans, [CCC](CCC "CCC"), December 05, 2013
- [That other DGT e-board](http://hiarcs.net/forums/viewtopic.php?t=6472&sid=748bb4336e8c6e0aecb1458ccf6de67e) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2013
- [DGT board C++ interface project](http://hiarcs.net/forums/viewtopic.php?t=6455) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2013

## [Re: Where is the USB port entry usder OS/X?](http://hiarcs.net/forums/viewtopic.php?t=6455&start=19) by [Shivkumar Shivaji](index.php?title=Shivkumar_Shivaji&action=edit&redlink=1 "Shivkumar Shivaji (page does not exist)"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 15, 2013 2015 ...

- [DGT will do dedicated units this year](http://www.hiarcs.net/forums/viewtopic.php?t=7587) by [Fernando](Fernando_Villegas "Fernando Villegas"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), January 01, 2016
- [DGT e-board / Mac,PC,Pico / full coverage / worthy & use](http://www.hiarcs.net/forums/viewtopic.php?t=7904) by SFK3, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2016
- [DGT sensory boards, any experience?](http://www.talkchess.com/forum/viewtopic.php?t=64164) by Gerald Grimsley, [CCC](CCC "CCC"), June 03, 2017
- [DGT Smart Board](http://www.hiarcs.net/forums/viewtopic.php?t=8639) by Schachspieler, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), October 26, 2017
- [Questions about the DGT Chessboard](http://www.talkchess.com/forum/viewtopic.php?t=66001) by Tracy S Miller, [CCC](CCC "CCC"), December 13, 2017
- [DGT board question](http://talkchess.com/forum3/viewtopic.php?f=2&t=68125) by Ponti, [CCC](CCC "CCC"), August 02, 2018
- [Chess for Android and Electronic ChessBoards](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69257) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), December 14, 2018 » [Chess for Android](Chess_for_Android "Chess for Android")

## 2020 ...

- [New DGT driver and updated eBoard drivers (Windows/Linux)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77783) by [Graham O'Neill](index.php?title=Graham_O%27Neill&action=edit&redlink=1 "Graham O'Neill (page does not exist)"), [CCC](CCC "CCC"), July 23, 2021

## External Links

- [DGT - Chess e-Boards](http://www.dgtshop.nl/index.php/44/e-boards)
- [DGT presents: new clocks, technology – and Vladimir Kramnik](http://www.chessbase.com/newsdetail.asp?newsid=4372), [ChessBase News](ChessBase "ChessBase"), January 10, 2008
- [Patent US6168158 - Device for detecting playing pieces on a board - Google Patents](http://www.google.com/patents/US6168158)
- [The DGT Chessboard](http://playwitharena.com/?Features:The_DGT_Chessboard) from [Arena Chess GUI](Arena "Arena")
- [Aart Bik's Website - Connecting Chess for Android with a DGT Chessboard](http://www.aartbik.com/android_dgt.php) » [Chess for Android](Chess_for_Android "Chess for Android")
- [DGT-board](http://www.pocketgrandmaster.com/english/help.html#DGT) from [PocketGrandmaster](PocketGrandmaster "PocketGrandmaster")
- [dgtdrv: An input engine for the DGT Digital Chess Board](http://dgtdrv.sourceforge.net/)
- [Mychess - Fidelity Electronics: DGT Projets](http://tradechess.blogspot.de/p/dgt-projets.html) (Spanish)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Patent US6168158 - Device for detecting playing pieces on a board - Google Patents](http://www.google.com/patents/US6168158)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [How electronic chessboards works](http://groups.google.com/group/rec.games.chess.misc/msg/8734d1b2fffd6af0) by [Ben Bulsink DGT Project](http://digitalgametechnology.com/site/History/about-dgt.html), [rec.games.chess.misc](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2004
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [DGT presents: new clocks, technology – and Vladimir Kramnik](http://www.chessbase.com/newsdetail.asp?newsid=4372), [ChessBase News](ChessBase "ChessBase"), January 10, 2008
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Which programs support the DGT e-Board?](http://digitalgametechnology.com/site/index.php/dgtsupport/frequently-asked-questions/287-boards-with-3rd-party-software/131-which-programs-support-the-dgt-e-board)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [DGT Winboard interface](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=52438) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 19, 2012
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [dgtdrv: An input engine for the DGT Digital Chess Board](http://dgtdrv.sourceforge.net/)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Aart Bik's Website - Connecting Chess for Android with a DGT Chessboard](http://www.aartbik.com/android_dgt.php)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Chess for Android and Electronic ChessBoards](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69257) by [Aart Bik](Aart_Bik "Aart Bik"), [CCC](CCC "CCC"), December 14, 2018
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [PicoChess](http://www.picochess.org/) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Video: DGT board and modern pieces](http://www.talkchess.com/forum/viewtopic.php?t=49199) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 01, 2013
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [DGT presents: new clocks, technology – and Vladimir Kramnik](http://www.chessbase.com/newsdetail.asp?newsid=4372), [ChessBase News](ChessBase "ChessBase"), January 10, 2008
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Revelation II](http://www.revelationii.com/index.php?option=com_content&view=article&id=130:revelation-ii&catid=92&Itemid=584) from [DGT](index.php?title=DGT&action=edit&redlink=1 "DGT (page does not exist)")
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [DGT starts delivery in december](http://www.chesscomputer.eu/index.php?option=com_content&view=article&id=166%3Adgt-starts-delivery-in-december&catid=1%3Alatest&Itemid=68&lang=en), [Phoenix Chess Systems](index.php?title=Phoenix_Chess_Systems&action=edit&redlink=1 "Phoenix Chess Systems (page does not exist)"), December 01, 2013
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [CSVN Live](http://www.csvn.nl/live-tournament-cloud)
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [Photo's PT45/GT27 day 1](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/616-photo-s-pt45-gt27-day-1)
1. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [DGT Pi - Chess Computer for DGT e-Boards - Digital Game Technology](http://www.digitalgametechnology.com/index.php/products/revelation-ii/533-dgt-pi-chess-computer-for-dgt-e-boards)

**[Up one level](Sensory_Board "Sensory Board")**

