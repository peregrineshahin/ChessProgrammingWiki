---
title: PuppetMaster
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* PuppetMaster**


**PuppetMaster**,  

an experimental chess playing entity by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden") which implements a multiple-brain concept using an [UDOO](UDOO "UDOO") computer running Folkert's engine [DeepBrutePos](DeepBrutePos "DeepBrutePos") in a so called "puppet master" mode, requesting best moves from external [UCI](UCI "UCI") or [XBoard](XBoard "XBoard") engines each running on one of seven [Raspberry Pi](Raspberry_Pi "Raspberry Pi") nodes connected via [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) [sockets](https://en.wikipedia.org/wiki/Network_socket) <a id="cite-note-1" href="#cite-ref-1">[1]</a> . The most chosen move is played, while DeepBrutePos keeps track how often a move of each engine was selected. In case of a tie, moves of engines with higher selection rate are preferred <a id="cite-note-2" href="#cite-ref-2">[2]</a> .



### Contents


* [1 Photos](#photos)
* [2 Tournament Play](#tournament-play)
* [3 Photos & Games](#photos-.26-games)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
	+ [6.1 Chess Entity](#chess-entity)
	+ [6.2 Misc](#misc)
* [7 References](#references)






 [](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/639-pt46-round-1) 
PuppetMaster in action at [PT 46](PT_46 "PT 46") <a id="cite-note-3" href="#cite-ref-3">[3]</a>



## Tournament Play


PuppetMaster had its official tournament debut at the [CSVN 1st Open Internet Tournament](index.php?title=1st_CSVN_OIT&action=edit&redlink=1 "1st CSVN OIT (page does not exist)") in May 2014, and further played the [PT 46](PT_46 "PT 46") over the board a week later, becoming 5th of 8 with a 50% score. At PT 46 the seven PI engines were <a id="cite-note-4" href="#cite-ref-4">[4]</a>:



1. [BikJump](BikJump "BikJump")
2. [GNU Chess](GNU_Chess "GNU Chess")
3. [Fruit](Fruit "Fruit")
4. [Toga II](Toga "Toga")
5. [Stockfish](Stockfish "Stockfish")
6. [MinkoChess](MinkoChess "MinkoChess")
7. [Arasan](Arasan "Arasan") <a id="cite-note-5" href="#cite-ref-5">[5]</a> .


## Photos & Games


 [](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/643-pt46-round-4) 
[CSVN](CSVN "CSVN") [PT 46](PT_46 "PT 46"), round 4, [The King](The_King "The King") - PuppetMaster <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [Johan de Koning](Johan_de_Koning "Johan de Koning") and  

[Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden") - [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") and [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") in the background <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "CSVN PT 46"]
[Site "Leiden"]
[Date "2014.05.18"]
[Round "4"]
[White "The King"]
[Black "DBP/PuppetMaster"]
[Result "0-1"]

1.e4 d5 2.exd5 Nf6 3.d4 Nxd5 4.Nf3 e6 5.c4 Bb4+ 6.Bd2 Bxd2+ 7.Qxd2 Nf6 8.Nc3 Nc6
9.Rd1 h6 10.Be2 O-O 11.O-O b6 12.Ne5 Bb7 13.Qf4 Nxe5 14.dxe5 Nd7 15.Rd3 Qe7
16.Rfd1 Nc5 17.Rg3 Kh8 18.b4 Nd7 19.Rgd3 Qxb4 20.Rxd7 Qxc3 21.Rxc7 Qc2 22.Rd2
Qc1+ 23.Bf1 Be4 24.Qe3 Kg8 25.a3 Bg6 26.c5 bxc5 27.Rxc5 Qa1 28.Rd6 Rfc8 29.Rxc8+
Rxc8 30.Qxa7 Rc1 31.Qa6 Qxe5 32.Rd2 Kh7 33.h3 Qe1 34.Rd8 Be4 35.Rd4 f5 36.Rd8
Bd5 37.Rxd5 exd5 38.a4 Qd2 39.a5 Rc2 40.f3 Qf2+ 41.Kh2 Qxf3 42.Qd3 Rxg2+ 43.Kh1
Qxd3 44.Bxd3 Ra2 45.Bxf5+ g6 46.Bd3 Rxa5 0-1

```

## See also


* [Clever & Smart](Clever_%26_Smart "Clever & Smart")
* [DeepBrutePos](DeepBrutePos "DeepBrutePos")
* [Raspberry Pi](Raspberry_Pi "Raspberry Pi")
* [UDOO](UDOO "UDOO")


## Forum Posts


* [raspberry pi cluster versus fairymax](http://www.talkchess.com/forum/viewtopic.php?t=49892) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 31, 2013
* [Re: CSVN 1st Open Internet Tournament: Results and games](http://www.talkchess.com/forum/viewtopic.php?t=52280&start=11) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 12, 2014
* [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=39) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014
* [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=41) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014


## External Links


### Chess Entity


* [DeepBrutePOS - An experimental chess program](https://vanheusden.com/DeepBrutePos/)


### Misc


* [Puppet Master (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Puppet_Master)
* [Puppet Master (comics) from Wikipedia](https://en.wikipedia.org/wiki/Puppet_Master_%28comics%29)
* [The Puppet Masters - Wikipedia](https://en.wikipedia.org/wiki/The_Puppet_Masters) - a 1951 [science fiction novel](https://en.wikipedia.org/wiki/Science_fiction_novel) by [Robert A. Heinlein](Category:Robert_Heinlein "Category:Robert Heinlein")
* [Puppet Master (film) - Wikipedia](https://en.wikipedia.org/wiki/Puppet_Master_%28film%29)
* [Metallica](Category:Metallica "Category:Metallica") - [Master of Puppets](https://en.wikipedia.org/wiki/Master_of_Puppets_%28song%29), [Johan Cruijff Arena](https://en.wikipedia.org/wiki/Johan_Cruyff_Arena), [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam), June 11, 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [raspberry pi cluster versus fairymax](http://www.talkchess.com/forum/viewtopic.php?t=49892) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 31, 2013
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=41) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Photo by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos"), [PT46: Round 1](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/639-pt46-round-1)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: CSVN Programmers' Tournaments May 2014](http://www.talkchess.com/forum/viewtopic.php?t=51761&start=39) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 20, 2014
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Cruel fate that [Arasan](Arasan "Arasan"), which became runner-up at [PT 46](PT_46 "PT 46") behind the [The Baron](The_Baron "The Baron"), lost from PuppetMaster due to an operator glitch unexperienced with [Arena](Arena "Arena"), [Re: The Baron is the winner](http://www.talkchess.com/forum/viewtopic.php?t=52344&start=12) by [Richard Pijl](Richard_Pijl "Richard Pijl"), [CCC](CCC "CCC"), May 18, 2014
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [CSVN PT 46 PGN download](http://marcelk.net/2014-05-18/PT46.pgn.bz2)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Photo by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos"), [PT46: Round 4](http://www.computerschaak.nl/nieuws-mainmenu-28/51-toernooien/643-pt46-round-4)

**[Up one Level](Engines "Engines")**







 
