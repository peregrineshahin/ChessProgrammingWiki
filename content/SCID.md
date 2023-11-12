---
title: SCID
---
**[Home](Home "Home") \* [User Interface](User_Interface "User Interface") \* [GUI](GUI "GUI") \* SCID**  

**[Home](Home "Home") \* [Software](Software "Software") \* [Databases](Databases "Databases") \* SCID**



[ SCID User Interface <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SCID**, (Scid, Shane's Chess Information Database)  

a [cross platform](https://en.wikipedia.org/wiki/Cross-platform) [open source](https://en.wikipedia.org/wiki/Open-source_software) chess database under the [GNU Lesser General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), to view, edit, and manage collections of chess games, 
initially developed by [Shane Hudson](Shane_Hudson "Shane Hudson"), who worked from 1999 to 2003 on it, the back end written in [C++](Cpp "Cpp"), the [GUI](GUI "GUI") in [Tcl/Tk](index.php?title=Tcl-Tk&action=edit&redlink=1 "Tcl-Tk (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. [Pascal Georges](Pascal_Georges "Pascal Georges") worked on SCID from December 2006 until January 2010 and added [UCI](UCI "UCI"), [FICS](index.php?title=Free_Internet_Chess_Server&action=edit&redlink=1 "Free Internet Chess Server (page does not exist)") and [Novag Citrine](Novag_Citrine "Novag Citrine") support, and ported SCID to the [Pocket PC](index.php?title=Pocket_PC&action=edit&redlink=1 "Pocket PC (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Further contributors were [Marc Lacrosse](index.php?title=Marc_Lacrosse&action=edit&redlink=1 "Marc Lacrosse (page does not exist)"), [Michal Rudolf](Michal_Rudolf "Michal Rudolf"), [Hans Ericson](index.php?title=Hans_Ericson&action=edit&redlink=1 "Hans Ericson (page does not exist)") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [Franz Nagl](index.php?title=Franz_Nagl&action=edit&redlink=1 "Franz Nagl (page does not exist)"), [Alexander Wagner](index.php?title=Alexander_Wagner&action=edit&redlink=1 "Alexander Wagner (page does not exist)") and [Uwe Klimmek](index.php?title=Uwe_Klimmek&action=edit&redlink=1 "Uwe Klimmek (page does not exist)"), et al.. 
SCID can read [PGN](Portable_Game_Notation "Portable Game Notation") and [EPD](Extended_Position_Description "Extended Position Description") files (and export to PGN, [LaTeX](https://en.wikipedia.org/wiki/LaTeX) and [HTML](https://en.wikipedia.org/wiki/HTML)) and uses its own database format for fast database search and queries by [position](Chess_Position "Chess Position"), material, pattern, players, and opening, etc., and can use [XBoard](XBoard "XBoard") and [UCI](UCI "UCI") compliant chess engines to analyze [games](Chess_Game "Chess Game"), and further supports mining of 5-man [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. The SCID library was used by [Gady Costeff](Gady_Costeff "Gady Costeff") and [Lewis Stiller](Lewis_Stiller "Lewis Stiller") to implement the [Chess Query Language](Chess_Query_Language "Chess Query Language") <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



## Database Format


SCID Databases consist of three kind of files, index files (.si4), name files (.sn4) and game files (.sg4), the latter containing the [moves](Moves "Moves"), variations and annotations of each [game](Chess_Game "Chess Game"). The compact [move encoding](Encoding_Moves "Encoding Moves") requires an [incremental updated](Incremental_Updates "Incremental Updates") [board representation](Board_Representation "Board Representation") aka [piece list](Piece-Lists "Piece-Lists"), and therefore takes only one [byte](Byte "Byte") for most moves (except diagonal queen moves), using a [nibble](Nibble "Nibble") as piece list index, determining [from square](Origin_Square "Origin Square") and piece to move, and the second nibble as [enumeration index](Influence_Quantity_of_Pieces "Influence Quantity of Pieces") of possible [target squares](Target_Square "Target Square") <a id="cite-note-7" href="#cite-ref-7">[7]</a>.



## SCID Forks


* [ChessDB](index.php?title=ChessDB&action=edit&redlink=1 "ChessDB (page does not exist)")
* [Scid on the Go](index.php?title=Scid_on_the_Go&action=edit&redlink=1 "Scid on the Go (page does not exist)")
* [Scid vs. PC](Scid_vs._PC "Scid vs. PC")
* [Scidb](Scidb "Scidb")


## See Also


* [Chess Assistant](Chess_Assistant "Chess Assistant")
* [Chess Query Language](Chess_Query_Language "Chess Query Language")
* [ChessBase (Database)](ChessBase_(Database) "ChessBase (Database)")
* [ChessX](ChessX "ChessX")
* [jose](index.php?title=Jose&action=edit&redlink=1 "Jose (page does not exist)")
* [Scidlet](index.php?title=Scidlet&action=edit&redlink=1 "Scidlet (page does not exist)")
* [Tarrasch](Tarrasch "Tarrasch")


## Forum Posts


### 1999


* [Scid: Linux Chess Data Base](https://www.stmintz.com/ccc/index.php?id=67829) by Peter Herttrich, [CCC](CCC "CCC"), September 08, 1999


### 2000 ...


* [A word in praise of Scid v1.0](https://www.stmintz.com/ccc/index.php?id=87763) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), January 11, 2000
* [Scid 2.0 Chess Data Base](https://www.stmintz.com/ccc/index.php?id=137466) by Peter Herttrich, [CCC](CCC "CCC"), November 09, 2000
* [Scid 2.1 (free chess database) now available](https://www.stmintz.com/ccc/index.php?id=140108) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), November 20, 2000
* [Scid 2.2 (free chess database app) available](https://www.stmintz.com/ccc/index.php?id=149981) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), January 14, 2001
* [Scid 2.4 now available](https://www.stmintz.com/ccc/index.php?id=168380) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), May 06, 2001
* [Scid 2.5 is now available](https://www.stmintz.com/ccc/index.php?id=176199) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), June 20, 2001
* [Sjeng & Scid](https://www.stmintz.com/ccc/index.php?id=186344) by [Stefan Knappe](Stefan_Knappe "Stefan Knappe"), [CCC](CCC "CCC"), August 30, 2001 » [Sjeng](Sjeng "Sjeng")
* [Scid 2.7 released](https://www.stmintz.com/ccc/index.php?id=193239) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), October 16, 2001
* [Scid 3.2 released](https://www.stmintz.com/ccc/index.php?id=215369) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), February 24, 2002
* [Paderborn 2002 Complete Opening Report with Scid 3.2](https://www.stmintz.com/ccc/index.php?id=216160) by [Arturo Ochoa](Arturo_Ochoa "Arturo Ochoa"), [CCC](CCC "CCC"), March 02, 2002 » [IPCCC 2002](IPCCC_2002 "IPCCC 2002")
* [Scid 3.3](https://www.stmintz.com/ccc/index.php?id=233844) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), June 04, 2002
* [SCID and chess variants](https://www.stmintz.com/ccc/index.php?id=241970) by Andrzej Nagorko, [CCC](CCC "CCC"), July 22, 2002
* [Installing Scid for Linux](https://www.stmintz.com/ccc/index.php?id=249085) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), September 01, 2002
* [is Scid used for running engine-engine matches?](https://www.stmintz.com/ccc/index.php?id=317654) by [Swaminathan Natarajan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), September 25, 2003
* [The new version 3.5 of SCID free chess database is out!](https://www.stmintz.com/ccc/index.php?id=336798) by Andy Prap, [CCC](CCC "CCC"), December 18, 2003
* [scid vs chessbase](https://groups.google.com/d/msg/rec.games.chess.computer/UJMm-K6cMXg/YSuwJGUFxmcJ) by [David Kirkby](index.php?title=David_Kirkby&action=edit&redlink=1 "David Kirkby (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 01, 2004 » [ChessBase (Database)](ChessBase_(Database) "ChessBase (Database)")
* [Scid 3.6 is now available](https://www.stmintz.com/ccc/index.php?id=351518) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), February 26, 2004
* [Scid 3.6.1 is released](https://www.stmintz.com/ccc/index.php?id=352457) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), March 02, 2004
* [One week without Windows ! Help with Scid install !](https://www.stmintz.com/ccc/index.php?id=357006) by Aloisio Ponti Lopes, [CCC](CCC "CCC"), March 28, 2004
* [What \_really\_ happened to Scid and Shane Hudson?](https://www.stmintz.com/ccc/index.php?id=369043) by George Sobala, [CCC](CCC "CCC"), June 05, 2004


### 2005 ...


* [Features added to Scid](https://groups.google.com/d/msg/rec.games.chess.computer/SnJ7z4skk90/GzKPI5sdIdgJ) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 02, 2007
* [Scid development activity?](https://groups.google.com/d/msg/rec.games.chess.computer/dMK7HBLbbIQ/RCbe-On3q8kJ) by stu..., [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 02, 2007
* [Scid 3.6.4 released (chess database)](https://groups.google.com/d/msg/rec.games.chess.computer/ZYpY2aF7mq8/d_eR1762lroJ) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 24, 2007
* [Scid 3.6.6 released (chess database)](http://www.avlerchess.com/chess-computer/Scid_366_released_chess_database_179456.html) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [Avler Chess](http://www.avlerchess.com/), March 07, 2007
* [Scid 3.6.11 released](http://www.talkchess.com/forum/viewtopic.php?t=13095) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), April 13, 2007
* [Scid 3.6.13 released](http://www.talkchess.com/forum/viewtopic.php?t=13412) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), April 26, 2007
* [Scid 3.6.14 released](http://www.talkchess.com/forum/viewtopic.php?t=13638) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), May 08, 2007
* [Scid for Pocket PC - First Beta released](http://www.talkchess.com/forum/viewtopic.php?t=14604) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), June 21, 2007
* [Why Scid should stay alive [Re: Statistical significance of score differences - new release ofChessDB]](https://groups.google.com/d/msg/rec.games.chess.computer/I-J53bggxm8/YJGioTFWSHUJ) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 22, 2007
* [FAKE Scid released (chess database software)](https://groups.google.com/d/msg/rec.games.chess.computer/aaziPZO-1mo/Jwr-RN2HOBsJ) by Guy Macon, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 09, 2007
* [Release of Scid 3.6.24 and Scid Pocket 1.1](http://www.talkchess.com/forum/viewtopic.php?t=21905) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), June 22, 2008
* [Scid 3.6.25 released](http://www.talkchess.com/forum/viewtopic.php?t=23438) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), September 01, 2008
* [Scid 3.7 released](http://www.talkchess.com/forum/viewtopic.php?t=26809) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), March 01, 2009
* [Scid 4.0 beta (chess database and training software)](http://www.talkchess.com/forum/viewtopic.php?t=29119) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), July 27, 2009
* [Scid 4.0 (chess database and training software)](http://www.talkchess.com/forum/viewtopic.php?t=29621) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), September 02, 2009
* [Scid Pocket v4 released](http://www.talkchess.com/forum/viewtopic.php?t=31230) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), December 24, 2009


### 2010 ...


* [Scid 4.1 released](http://www.talkchess.com/forum/viewtopic.php?t=31429) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), January 02, 2010
* [Scid 4.2 released](http://www.talkchess.com/forum/viewtopic.php?t=31847) by [Pascal Georges](Pascal_Georges "Pascal Georges"), [CCC](CCC "CCC"), January 19, 2010
* [Scid forks](http://www.talkchess.com/forum/viewtopic.php?t=38398) by Ivan Toporov, [CCC](CCC "CCC"), Mar 13, 2011
* [Scid 4.4 released](http://www.talkchess.com/forum/viewtopic.php?t=47641) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), March 29, 2013
* [Scid 4.5.1 development version released](http://www.talkchess.com/forum/viewtopic.php?t=47970) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), May 12, 2013
* [Scid vs PC 4.8 or Scid 4.4?](http://www.talkchess.com/forum/viewtopic.php?t=48813) by Gerald Grimsley, [CCC](CCC "CCC"), August 01, 2013
* [Scid.eco](https://www.mail-archive.com/scid-users@lists.sourceforge.net/msg06639.html) by [Gregor Cramer](index.php?title=Gregor_Cramer&action=edit&redlink=1 "Gregor Cramer (page does not exist)"), [scid-users](https://www.mail-archive.com/scid-users@lists.sourceforge.net/), April 19, 2014 » [ECO](ECO "ECO"), [Scidb](Scidb "Scidb")


### 2015 ...


* [SCID Chess](http://www.talkchess.com/forum/viewtopic.php?t=55055) by AA Ross, January 23, 2015
* [Scid (si4) File Format](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=55597) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), March 08, 2015
* [A new version of Scid is available [4.6.4](http://www.talkchess.com/forum/viewtopic.php?t=61013)] by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), August 02, 2016
* [About SCID](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=62236) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), November 23, 2016  » [Windows 32](Windows "Windows")
* [scid - pgn database size limitation?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66676) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), February 23, 2018
* [[SCID Database] Updated FIDE spelling files - February 2018+](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=66706) by styx, [CCC](CCC "CCC"), February 27, 2018
* [SCID 4.7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69771) by Fulvio, [CCC](CCC "CCC"), January 30, 2019


## External Links


* [Scid - Chess Database Software](http://scid.sourceforge.net/)
* [Scid: Code Documentation](http://scid.sourceforge.net/doxygen/html/index.html) by [Doxygen](https://en.wikipedia.org/wiki/Doxygen)
* [Scid | SourceForge.net](https://sourceforge.net/projects/scid/)
* [Shane's Chess Information Database from Wikipedia](https://en.wikipedia.org/wiki/Shane%27s_Chess_Information_Database)
* [scid-users mail archive](https://www.mail-archive.com/scid-users@lists.sourceforge.net/)
* [GitHub - asdfjkl/si4spec: Scid4 File Format Specification](https://github.com/asdfjkl/si4spec) by [Dominik Klein](Dominik_Klein "Dominik Klein")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Main window of Scid. The version is 4.6.2 and is running in [Windows 7](Windows "Windows"), Image by Nicoguaro, [Shane's Chess Information Database from Wikipedia](https://en.wikipedia.org/wiki/Shane%27s_Chess_Information_Database)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Scid / Wiki / ShaneHudson](https://sourceforge.net/p/scid/wiki/ShaneHudson/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Scid / Wiki / ScidAuthors](http://sourceforge.net/p/scid/wiki/ScidAuthors/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Scid / Wiki / ScidContributors](http://sourceforge.net/p/scid/wiki/ScidContributors/) by [Shane Hudson](Shane_Hudson "Shane Hudson"), April 2007
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Scid 2.1 (free chess database) now available](https://www.stmintz.com/ccc/index.php?id=140108) by [Shane Hudson](Shane_Hudson "Shane Hudson"), [CCC](CCC "CCC"), November 20, 2000
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Gady Costeff](Gady_Costeff "Gady Costeff") (**2004**). *The Chess Query Language: CQL*. [ICGA Journal, Vol. 27, No. 4](ICGA_Journal#27_4 "ICGA Journal"), [pdf](http://gadycosteff.com/chess_query_language.pdf)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [si4 database format](http://scidvspc.sourceforge.net/doc/Formats.htm)

**[Up one Level](Databases "Databases")**







 
