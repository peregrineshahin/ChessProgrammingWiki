---
title: Nalimov Tablebases
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") \* Nalimov Tablebases**



[ Huffman tree <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Nalimov Tablebases**,  

are **3**-to-**6**-man endgame tablebases developed by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), providing [depth to mate](Endgame_Tablebases#DTM "Endgame Tablebases") information. First published for up to **5**-man in late 1998, **6**-man files were released subsequently over the years and **6**-man chess was finally solved in 2005 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Nalimov Tablebases apply a more efficient indexing scheme than previous tablebases, and were further [compressed](https://en.wikipedia.org/wiki/Data_compression) into 8 KiB blocks exploiting [common subsequences](https://en.wikipedia.org/wiki/Subsequence#Common_subsequence) and [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) as contributed by [Andrew Kadatch](Andrew_Kadatch "Andrew Kadatch"), doing less [file I/O](https://en.wikipedia.org/wiki/Input/output) which gets replaced by fast on-the-fly decompression <a id="cite-note-3" href="#cite-ref-3">[3]</a>. This allows fast probing not only at the [root](Root "Root"), but during the [search](Search "Search") inside the [tree](Search_Tree "Search Tree") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, further utilized by an own [LRU cache](https://en.wikipedia.org/wiki/Cache_algorithms#LRU) despite keeping TB files in the [page cache](https://en.wikipedia.org/wiki/Page_cache) by the [operating system](https://en.wikipedia.org/wiki/Operating_system). For endgames with pawns of both sides, the TBs consider [en passant](En_passant "En passant") with disjoint index ranges <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Contents


* [1 File Sizes](#file-sizes)
* [2 Savings](#savings)
* [3 License](#license)
* [4 See also](#see-also)
* [5 Publications](#publications)
* [6 Forum Posts](#forum-posts)
	+ [6.1 1998 ...](#1998-...)
	+ [6.2 2000 ...](#2000-...)
	+ [6.3 2005 ...](#2005-...)
	+ [6.4 2010 ...](#2010-...)
	+ [6.5 2015 ...](#2015-...)
	+ [6.6 2020 ...](#2020-...)
* [7 External Links](#external-links)
	+ [7.1 General](#general)
	+ [7.2 Online Lookup](#online-lookup)
	+ [7.3 Download](#download)
* [8 References](#references)






5-man Nalimov Tablebases are about two times smaller than [Edwards' Tablebases](Edwards%27_Tablebases "Edwards' Tablebases") when uncompressed, and about eight times smaller than Edwards' when compressed <a id="cite-note-6" href="#cite-ref-6">[6]</a>.





|  Men
 |  Sum of File sizes
 |
| --- | --- |
|  3
 |  62
 |  KiB
 |
|  4
 |  30
 |  MiB
 |
|  5
 |  7.1
 |  GiB
 |
|  6
 |  1.2
 |  TiB
 |


## Savings


In [CCC](CCC "CCC"), [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") gave a brief summary, how to realize the space savings <a id="cite-note-7" href="#cite-ref-7">[7]</a> :





|  |
| --- |
| 1. For pawnless ending, one can restrict one piece to a1-d1-d4 triangle (that was done in [SJE's](Steven_Edwards "Steven Edwards") generator). But if that piece happens to be on a1-d4 diagonal, one can restrict other piece to 'large' a1-h1-h8 triangle (exploit one more symmetry).
2. When one places a second piece on the board, one square is occupied already, so there are only 63 possible squares, for third - only 62, etc.
3. If there are two identical pieces (e.g. as in knnkp), one can order their locations - e.g. force second piece to occupy square with smaller number. Then one has not N\*(N-1) total combinations, but N\*(N-1)/2
4. Pawns occupy ranks 2-7. Even if one wants to handle en passant, there are better ways to do that than to reserve entire rank (or two) for possible en passant target
5. Kings never can be near each other, so there are only 3612 ways to place 2 kings on the empty board (not using symmetries), versus 4096 when using SJE's format
6. One cannot capture enemy's king, so, if one knows where it's located, there are some forbidden squares for the pieces of the side-to-move.
 |


## License


In the late 90s Nalimov Tablebases became defacto standard and were used in many [commercial](Category:Commercial "Category:Commercial"), [private](Category:Private "Category:Private") and free chess engines and [GUI's](GUI "GUI"). A reference implementation by Eugene Nalimov and [Robert Hyatt](Robert_Hyatt "Robert Hyatt") was realized in [Crafty](Crafty "Crafty"), with Tablebases and probing code previously available from Bob Hyatt's site <a id="cite-note-8" href="#cite-ref-8">[8]</a>. Probing could easily incorporated into own chess engines, however the license policy requires explicit permission by Eugene Nalimov <a id="cite-note-9" href="#cite-ref-9">[9]</a>. 



## See also


* [Bitbases](Endgame_Bitbases "Endgame Bitbases")
* [Edwards' Tablebases](Edwards%27_Tablebases "Edwards' Tablebases")
* [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")
* [Lomonosov Tablebases](Lomonosov_Tablebases "Lomonosov Tablebases")
* [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Thompson's Databases](Thompson%27s_Databases "Thompson's Databases")


## Publications


* [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [Guy Haworth](Guy_Haworth "Guy Haworth"), [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2000**). *[Space-Efficient Indexing of Chess Endgame Tables](http://centaur.reading.ac.uk/4562/)*. [ICGA Journal, Vol. 23, No. 3](ICGA_Journal#23_3 "ICGA Journal"), [postscript](http://supertech.lcs.mit.edu/%7Eheinz/ps/NHH_ICGA.ps.gz)
* [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [Guy Haworth](Guy_Haworth "Guy Haworth"), [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *[Space-efficient Indexing of Endgame Tables for Chess](http://centaur.reading.ac.uk/4563/)*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
* [Guy Haworth](Guy_Haworth "Guy Haworth"), [Peter Karrer](Peter_Karrer "Peter Karrer"), [John Tamplin](John_Tamplin "John Tamplin"), [Christoph Wirth](Christoph_Wirth "Christoph Wirth") (**2001**). *[3-5-man chess: Maximals and mzugs](http://centaur.reading.ac.uk/4581/)*. [ICGA Journal, Vol. 24, No. 4](ICGA_Journal#24_4 "ICGA Journal")
* [Eugène Nalimov](Eugene_Nalimov "Eugene Nalimov") (**2002**). *Chess Endgame Tablebases*. [Invited Lecture](Eugene_Nalimov#Lecture "Eugene Nalimov"), [7th Computer Olympiad Workshop](7th_Computer_Olympiad#Workshop "7th Computer Olympiad")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2005**). *[6-Man Chess Solved](http://centaur.reading.ac.uk/4522/)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")


## Forum Posts


### 1998 ...


* [Tablebases](https://www.stmintz.com/ccc/index.php?id=25540) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 28, 1998
* [Program for new TB by Dr. Eugene Nalimov ?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/13dce097a251e2a4#) by [Michael Diosi](index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 6, 1998
* [Nalimov's TBs: one question](https://www.stmintz.com/ccc/index.php?id=33325) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 18, 1998


 [Re: Nalimov's TBs: one question](https://www.stmintz.com/ccc/index.php?id=33351) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), November 18, 1998
* [Q: Nalimov EGTB?](https://www.stmintz.com/ccc/index.php?id=63581) by [Dennis Breuker](Dennis_Breuker "Dennis Breuker"), [CCC](CCC "CCC"), August 05, 1999


 [Re: Q: Nalimov EGTB?](https://www.stmintz.com/ccc/index.php?id=63619) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 05, 1999
* [Nalimov TB caching ?](https://www.stmintz.com/ccc/index.php?id=63720) by [Ulrich Türke](Ulrich_T%C3%BCrke "Ulrich Türke") from [CCC](CCC "CCC"), August 06, 1999
* [EGTBs](https://www.stmintz.com/ccc/index.php?id=67203) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), September 03, 1999
* [difference betrween nalimov and thompson EGTB](https://www.stmintz.com/ccc/index.php?id=81835) by [Rajen Gupta](index.php?title=Rajen_Gupta&action=edit&redlink=1 "Rajen Gupta (page does not exist)"), [CCC](CCC "CCC"), December 10, 1999


 [Re: difference betrween nalimov and thompson EGTB](https://www.stmintz.com/ccc/index.php?id=81932) by [Frederic Friedel](Frederic_Friedel "Frederic Friedel"), [CCC](CCC "CCC"), December 11, 1999
### 2000 ...


* [Nalimov-EGTBs in ANSI-C?](https://www.stmintz.com/ccc/index.php?id=90672) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), January 21, 2000
* [Usage of egtb.cpp in GPL software (Amy, ExChess, ...)](https://www.stmintz.com/ccc/index.php?id=142991) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 05, 2000 » [Amy](Amy "Amy"), [EXchess](EXchess "EXchess")


 [Re: Usage of egtb.cpp in GPL software (Amy, ExChess, ...)](https://www.stmintz.com/ccc/index.php?id=143013) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), December 05, 2000
* [Nalimov endgames](https://www.stmintz.com/ccc/index.php?id=155187) by [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill"), [CCC](CCC "CCC"), February 20, 2001
* [Nalimov's EGTBs (long post with code)](https://www.stmintz.com/ccc/index.php?id=192968) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), October 13, 2001
* [Nalimov TB question](https://www.stmintz.com/ccc/index.php?id=196952) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), November 11, 2001
* [Questions about the new Nalimov tablebase files...](https://www.stmintz.com/ccc/index.php?id=270531) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 12, 2002
* [Compressed Nalimov EGTBs](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/dc2f8a69e0deaded#) by Leonardo Ljubicic, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2003
* [Bug/glitch in Nalimov Code (and in Wilhelm)?](https://www.stmintz.com/ccc/index.php?id=364329) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), May 09, 2004
* [To Eugene Nalimov: Copyright of Tablebase files](https://www.stmintz.com/ccc/index.php?id=369041) by [Karl-Heinz Milaster](Karl-Heinz_Milaster "Karl-Heinz Milaster"), [CCC](CCC "CCC"), June 05, 2004
* [Are nalimov EGTB's a copyright from chessbase?](https://www.stmintz.com/ccc/index.php?id=369294) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), June 07, 2004
* [Enpassant in Nalimov](https://www.stmintz.com/ccc/index.php?id=393219) by Henry Hongdoyo, [CCC](CCC "CCC"), October 25, 2004


### 2005 ...


* [Subject: Problem (small bug?) with Nalimov TBs](https://www.stmintz.com/ccc/index.php?id=407134) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), January 23, 2005
* [To sumarize this](https://www.stmintz.com/ccc/index.php?id=442822) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [CCC](CCC "CCC"), August 17, 2005
* [For Eugene Nalimov: EGTB Request](https://www.stmintz.com/ccc/index.php?id=470947) by [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [CCC](CCC "CCC"), December 16, 2005
* [smp and nalimov egtb, how to make it work?](https://www.stmintz.com/ccc/index.php?id=488972) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), February 23, 2006
* [Chessbase releases 9 dvds on Nalimov 6-piece database 43 gb](https://www.stmintz.com/ccc/index.php?id=489022) by Daneil Johnson, [CCC](CCC "CCC"), February 23, 2006
* [Nalimov access](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=19) with [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 9, 2007
* [Nalimov Tablebases](http://www.talkchess.com/forum/viewtopic.php?t=14841) by Terry Giles, [CCC](CCC "CCC"), July 02, 2007
* [Nalimov EGTB](http://www.talkchess.com/forum/viewtopic.php?t=24476) by cyberfish, [CCC](CCC "CCC"), October 19, 2008
* [6-men (64 bit) Nalimov EGTB generator](http://www.talkchess.com/forum/viewtopic.php?t=29745) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), September 13, 2009
* [Nalimov EGTB probes skeleton code](http://www.talkchess.com/forum/viewtopic.php?t=31112) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), December 17, 2009


### 2010 ...


* [Nalimov and memory for indexes (are you aware?)](http://www.talkchess.com/forum/viewtopic.php?t=32987) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), March 01, 2010
* [Question for Nalimov experts](http://www.talkchess.com/forum/viewtopic.php?t=33726) by [Mincho Georgiev](Mincho_Georgiev "Mincho Georgiev"), [CCC](CCC "CCC"), April 10, 2010
* [Gaviota EGTB in Houdini 1.5 + contacting Eugene Nalimov](http://www.talkchess.com/forum/viewtopic.php?t=36886) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 01, 2010
* [Nalimov 6 men ...](http://www.talkchess.com/forum/viewtopic.php?t=46857) by [Michael Diosi](index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [CCC](CCC "CCC"), January 12, 2013
* [Nalimov](http://www.talkchess.com/forum/viewtopic.php?t=48084) by [Sune Larsson](index.php?title=Sune_Larsson&action=edit&redlink=1 "Sune Larsson (page does not exist)"), [CCC](CCC "CCC"), May 22, 2013


### 2015 ...


* [Nalimov EGTB problem related to DTM?](http://www.talkchess.com/forum/viewtopic.php?t=59237) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), February 14, 2016 » [DTM](Endgame_Tablebases#DTM "Endgame Tablebases")


 [Re: Nalimov EGTB problem related to DTM?](http://www.talkchess.com/forum/viewtopic.php?t=59237&start=7) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), February 14, 2016
* [Nalimov egtb probing code](http://www.talkchess.com/forum/viewtopic.php?t=60195) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), May 16, 2016


### 2020 ...


* [Nalimov errors](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77091) by Jonathan Colledge, [CCC](CCC "CCC"), April 15, 2021


## External Links


### General


* [Tablebases](https://web.archive.org/web/20141116144151/http://www.ajedrez-de-estilo.com.ar/int/Products/engines/tb/) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Nalimov Tablebases](https://web.archive.org/web/20131015101139/http://www.playwitharena.com/?User_Files%2C_Engines:Axon%2C_EloStat%2C_Nalimov:Nalimov_Tablebases) from [Arena Chess GUI](Arena "Arena") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Eugene Nalimov: Winner of the ChessBase Award and Guest of Honor in Maastricht](http://archive.today/HFYs) by [Eric van Reem](Eric_van_Reem "Eric van Reem"), [ChessBase](ChessBase "ChessBase") events, July 9, 2002 (archived)
* [Theoretical statistics for chess endgames with up to five pieces](https://ulthiel.com/math/other/endgames/) by [Ulrich Thiel](Mathematician#UlrichThiel "Mathematician")
* [Engines and endgame tablebases](http://en.chessbase.com/post/engines-and-endgame-tablebases) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 12, 2013


### Online Lookup


* [Endgame Nalimov Tablebases Online](http://chessok.com/?page_id=361) - [ChessOK](ChessOK "ChessOK")
* [Nalimov EGTB](http://www.gmchess.com/endgames/) from [GMchess.com](http://www.gmchess.com/index.html)
* [Nalimov Tablebase server (DTM)](http://www.lokasoft.nl/tbweb.htm) by [Lokasoft](Lokasoft "Lokasoft")
* [Web Query for Nalimov Endgame Tablebases](http://www.k4it.de/index.php?lang=en&topic=egtb) from [Knowledge4IT](http://www.k4it.de/index.php?topic=impressum&lang=en) by [Eiko Bleicher](Eiko_Bleicher "Eiko Bleicher")


### Download


* [Endgame Tablebases Online - 6-men endgame analysis free for everyone](http://kirill-kryukov.com/chess/tablebases-online/) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov") (3,4,5,6 pieces - via [emule](https://en.wikipedia.org/wiki/EMule))
* [tablebase.sesse.net](http://tablebase.sesse.net/) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Huffman tree generated from the exact frequencies of the text "this is an example of a huffman tree". The frequencies and codes of each character are below. Encoding the sentence with this code requires 135 bits, as opposed to 288 bits if 36 characters of 8 bits were used, [Huffman coding from Wikipedia](https://en.wikipedia.org/wiki/Huffman_coding)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Guy Haworth](Guy_Haworth "Guy Haworth") (**2005**). *[6-Man Chess Solved](http://centaur.reading.ac.uk/4522/)*. [ICGA Journal, Vol. 28, No. 3](ICGA_Journal#28_3 "ICGA Journal")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Compressed Nalimov EGTBs](https://groups.google.com/d/msg/rec.games.chess.computer/3C-KaeDere0/Bru6UFlOO4QJ) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 18, 2003
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Q: Nalimov EGTB?](https://www.stmintz.com/ccc/index.php?id=63619) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 05, 1999
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [Guy Haworth](Guy_Haworth "Guy Haworth"), [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *[Space-efficient Indexing of Endgame Tables for Chess](http://centaur.reading.ac.uk/4563/)*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), chapter 3. Nalimov’s Index Scheme
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Q: Nalimov EGTB?](https://www.stmintz.com/ccc/index.php?id=63619) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), August 05, 1999
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Nalimov's TBs: one question](https://www.stmintz.com/ccc/index.php?id=33351) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), November 18, 1998
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Index of /hyatt/crafty/TB](https://web.archive.org/web/20131102025806/http://www.cis.uab.edu/hyatt/crafty/TB/) hosted by [Robert Hyatt](Robert_Hyatt "Robert Hyatt") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [To sumarize this](https://www.stmintz.com/ccc/index.php?id=442822) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [CCC](CCC "CCC"), August 17, 2005

**[Up one level](Endgame_Tablebases "Endgame Tablebases")**







 
