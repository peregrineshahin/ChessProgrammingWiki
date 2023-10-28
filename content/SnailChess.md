---
title: SnailChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SnailChess**



[ Helix pomatia <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**SnailChess**,  

an experimental [WinBoard](WinBoard "WinBoard") compliant chess engine by [Rasjid Chan](Rasjid_Chan "Rasjid Chan") with the fame of a slow searcher, written in [C](C "C"), first released in November 1999. SnailChess started as plain [alpha-beta](Alpha-Beta "Alpha-Beta") searcher, SnailChess **1.07** used [NegaScout](NegaScout "NegaScout") with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, an intermediate **SnailSCP** was a partial clone of [TSCP](TSCP "TSCP") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
The last public SnailChess **4.013** was released in June 2002. Then SnailChess became a testbed for various [board representations](Board_Representation "Board Representation") and [move generation](Move_Generation "Move Generation") techniques, using [incremental updated](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") and various [bitboard](Bitboards "Bitboards") methods such as [rotated](Rotated_Bitboards "Rotated Bitboards") and [magic bitboards](Magic_Bitboards "Magic Bitboards"), and applied an [iterative search](Iterative_Search "Iterative Search") with a [stack](Stack "Stack") of structs <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### Contents


* [1 Forum Posts](#forum-posts)
	+ [1.1 1999](#1999)
	+ [1.2 2000 ...](#2000-...)
	+ [1.3 2005 ...](#2005-...)
* [2 External Links](#external-links)
	+ [2.1 Chess Engine](#chess-engine)
	+ [2.2 Misc](#misc)
* [3 References](#references)






### 1999


* [New kid on the block : Snailchess](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30497) by K1, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 04, 1999
* [SOS 031199, Ant 4.16 und SnailChess 1.01](https://www.stmintz.com/ccc/index.php?id=79029) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), November 22, 1999


### 2000 ...


* [SnailChess-new release](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31555) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 03, 2000
* [SnailChess ver 1.07](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=32444) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2000
* [SnailChess Copper, a new re-write](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=33767) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 12, 2001
* [SnailChess Copper ver 2.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=33788) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 18, 2001
* [SnailChess Ver 3.01 is now at homepage](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35095) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 19, 2001
* [SnailChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35649) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 08, 2002
* [SnailChess Copper Revived- Ver 4.0](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37851) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 21, 2002


### 2005 ...


* [Does simple futility prune work](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2101&p=9758) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 27, 2005
* [Re: NPS](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3370&p=17074) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 01, 2005
* [Help! SnailChess Debug problem](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4038&p=20576) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 28, 2005
* [Re: Fastest Magic Move Bitboard Generator ready to use](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5452&p=27108) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 28, 2006
* [Re: Help Finding X](http://www.talkchess.com/forum/viewtopic.php?t=14366&start=9) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), June 09, 2007  » [KPK](KPK "KPK")


## External Links


### Chess Engine


* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [SnailChess 4.013](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=SnailChess%204.013) in [CCRL 40/4](CCRL "CCRL")
* [SnailChess 4.013](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=SnailChess%204.013) in [KCEC](KCEC "KCEC")


### Misc


* [Snail from Wikipedia](https://en.wikipedia.org/wiki/Snail)
* [Snail (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Snail_%28disambiguation%29)
* [Helix (gastropod) from Wikipedia](https://en.wikipedia.org/wiki/Helix_%28gastropod%29)
* [Snail slime from Wikipedia](https://en.wikipedia.org/wiki/Snail_slime)
* [A snail can slide over a razor blade without being hurt. | Wikistupidia](http://www.wikistupidia.com/2010/10/08/a-snail-can-slide-over-a-razor-blade-without-being-hurt/) <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [SKNAIL](http://sknail.com/) - The Other Side, produced by [Bastien Bron](https://ch.linkedin.com/pub/bastien-bron/70/b6/128), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Picture](http://commons.wikimedia.org/wiki/File:Grapevinesnail_01.jpg) of [Helix pomatia](https://en.wikipedia.org/wiki/Helix_pomatia) by [Jürgen Schoner](https://de.wikipedia.org/wiki/Benutzer:Heliodor), May 23, 2005, [Snail from Wikipedia](https://en.wikipedia.org/wiki/Snail)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [SnailChess ver 1.07](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=32444) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 28, 2000
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [SnailChess-new release](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31555) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 03, 2000
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [Re: Fastest Magic Move Bitboard Generator ready to use](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5452&p=27108) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 28, 2006
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Warum können Schnecken über Rasierklingen kriechen, ohne sich zu verletzen?](http://www.wdr.de/tv/kopfball/sendungsbeitraege/2009/1025/schleimspur.jsp), [Kopfball](http://de.wikipedia.org/wiki/Kopfball_%28Show%29) [DasErste](https://en.wikipedia.org/wiki/Das_Erste) (German)

**[Up one level](Engines "Engines")**







 
