---
title: Naum
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Naum**



[ [Icon](https://en.wikipedia.org/wiki/Icon) of [Saint Naum](https://en.wikipedia.org/wiki/Saint_Naum) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Naum**,  

a former commercial chess engine written by [Alexander Naumov](Alexander_Naumov "Alexander Naumov") in [C++](Cpp "Cpp"). In about 2003, Naum was first developed for [Palm](index.php?title=Palm&action=edit&redlink=1 "Palm (page does not exist)") handheld computers, and ported to [x86](X86 "X86") [PCs](IBM_PC "IBM PC"), where Naum soon evolved to a top commercial chess engine. Naum **4.2** was released in March 2010, and did support both, the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") with executables shipped for single-and multiple-processor systems running under [Windows](Windows "Windows") and [Linux](Linux "Linux"). Naum was part of the *Chess Coach* program supporting the proprietary [BlitzIn](index.php?title=BlitzIn&action=edit&redlink=1 "BlitzIn (page does not exist)"), [Dasher](index.php?title=Dasher&action=edit&redlink=1 "Dasher (page does not exist)") and [ChessBase](ChessBase_(Database) "ChessBase (Database)") [GUIs](GUI "GUI"). As of 2012, the commercial career of Naum as stand alone program ended so far, and in September 2014, Alexander Naumov asked [Graham Banks](Graham_Banks "Graham Banks") to provide a download link for a free Naum **4.6** <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### Contents


* [1 Selectivity Issues](#selectivity-issues)
* [2 Tournament Play](#tournament-play)
* [3 Photos & Games](#photos-.26-games)
	+ [3.1 CCT9](#cct9)
	+ [3.2 Chess960CWC 2008](#chess960cwc-2008)
		- [3.2.1 Round 5](#round-5)
		- [3.2.2 Take me to the Hospital](#take-me-to-the-hospital)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2004](#2004)
	+ [5.2 2005 ...](#2005-...)
	+ [5.3 2010 ...](#2010-...)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc)
* [7 References](#references)






In [forum](Computer_Chess_Forums "Computer Chess Forums") discussions on [evaluation](Evaluation "Evaluation") at [interior nodes](Interior_Node "Interior Node"), Alex mentioned eval >= [beta](Beta "Beta") did not work in early Naum as [null move pruning](Null_Move_Pruning "Null Move Pruning") precondition <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and further that [history pruning](Late_Move_Reductions "Late Move Reductions") gave Naum about 40-50 ELO <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Tournament Play


Naum played the [Chess960CWC 2006](Chess960CWC_2006 "Chess960CWC 2006") and [Chess960CWC 2008](Chess960CWC_2008 "Chess960CWC 2008") <a id="cite-note-5" href="#cite-ref-5">[5]</a><a id="cite-note-6" href="#cite-ref-6">[6]</a> over the board, and online the [CCT9](CCT9 "CCT9"), the [CCT10](CCT10 "CCT10") (shared winner with [Rybka](Rybka "Rybka")), and the [ACCA 2008](ACCA_2008 "ACCA 2008"). Naum 4.2 to 4.6 (Stage 3, 4) played the [TCEC Season 5](TCEC_Season_5 "TCEC Season 5"), and 4.6 further [TCEC Season 6](TCEC_Season_6 "TCEC Season 6"), where it won stage 1b.



## Photos & Games


### CCT9


[CCT9](CCT9 "CCT9"), [Crafty](Crafty "Crafty") - Naum <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "CCT9"]
[Site "Internet Chess Club"]
[Date "2007.02.17"]
[Round "-"]
[White "Crafty"]
[Black "Naum"]
[Result "0-1"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d3 a6 6.O-O d6 7.Bb3 Ba7 
8.Nbd2 O-O 9.h3 Be6 10.Re1 Bxb3 11.Qxb3 Rb8 12.Nf1 h6 13.Be3 Bxe3 
14.Nxe3 Re8 15.Nd5 Nxd5 16.exd5 Ne7 17.d4 Ng6 18.dxe5 dxe5 19.Re4 
Kh7 20.c4 f5 21.Ree1 c5 22.Re2 e4 23.Ne1 b5 24.Rd1 Qd6 25.Qc3 Ne5 
26.cxb5 axb5 27.f3 Ng6 28.fxe4 Nf4 29.Rc2 c4 30.g3 Nh5 31.Qf3 Nxg3
32.exf5 Rf8 33.Rg2 Nxf5 34.Nc2 Rbe8 35.Qg4 g6 36.Rf1 h5 37.Qg5 Re5 
38.Qf4 Qc5+ 39.Kh2 Rxd5 40.Re1 Rd3 41.Qe5 Qc8 42.Qe6 Qb8+ 43.Qe5 Qd8 
44.Re4 Rd5 45.Qe6 Qc7+ 46.Kg1 Rd6 47.Qe5 Rf7 48.Qe8 Rdd7 49.a4 Qb6+ 
50.Kh2 Rfe7 51.Rxe7+ Rxe7 52.Qxb5 Qd6+ 53.Kh1 Nh4 54.Qxc4 Qd1+ 0-1

```

### Chess960CWC 2008


### Round 5


[Chess960CWC 2008](Chess960CWC_2008 "Chess960CWC 2008"), Round 5, Naum 3.1 - [Rybka 3](Rybka "Rybka") <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```

[Event "Chess960CWC 2008"]
[Site "Mainz GER"]
[Date "2008.07.30"]
[Round "5"]
[White "Naum 3.1"]
[Black "Rybka 3"]
[Result "1/2-1/2"]
[Variant "chess 960"]
[SetUp "1"]
[FEN "rnnqbbkr/pppppppp/8/8/8/8/PPPPPPPP/RNNQBBKR w HAha - 0 1"]

{SP 445} 1.e4 e6 2.Nc3 d5 3.exd5 exd5 4.d4 Nb6 5.Be2 Bd6 6.a4 a5 7.Nb3
c6 8.f3 f6 9.Bd3 Bf7 10.Bg3 Bxg3 11.hxg3 Nc4 12.Bxc4 dxc4 13.Nc5 b6 14.
N5e4 O-O 15.g4 Na6 16.Qd2 Nb4 17.O-O-O Re8 18.Kb1 Qc7 19.f4 Qd7 20.Rh4
Rad8 21.Rdh1 Qxd4 22.Rxh7 Kf8 23.Rh8+ Bg8 24.Qe2 Nd5 25.Qf3 Qe3 26.f5 Kf7
27.R8h5 Nxc3+ 28.Nxc3 Qxf3 29.gxf3 Re3 30.R5h3 Ke7 31.Kc1 Bd5 32.f4 Bxh1
33.Rxe3+ Kd6 34.g5 Rf8 35.Rh3 Bd5 36.Rh7 fxg5 37.fxg5 Rxf5 38.Nxd5 cxd5
39.Rxg7 d4 40.Rg8 Rf1+ 41.Kd2 Rf2+ 42.Kc1 Rg2 43.g6 c3 44.Kb1 Kc5 45.
Rc8+ Kb4 46.Rd8 cxb2 47.Kxb2 Kc4 48.Rc8+ Kd5 49.Rd8+ Kc5 50.Rc8+ Kd6 51.
Rd8+ Ke5 52.Re8+ Kd6 1/2-1/2

```





### Take me to the Hospital


[Chess960CWC 2008](Chess960CWC_2008 "Chess960CWC 2008"), Round 6, [Rybka 3](Rybka "Rybka") - Naum 3.1 <a id="cite-note-9" href="#cite-ref-9">[9]</a>



 [](http://www.chesstigers.de/ccm9_index_news.php?id=1435&rubrik=6&lang=0&kat=6) 
[Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [Elke Van Vlierberghe](Elke_Van_Vlierberghe "Elke Van Vlierberghe"), [Alex Naumov](Alexander_Naumov "Alexander Naumov"), ., [Hartmut Metz](http://www.scr-kuppenheim.de/meko/index.html), [Lars Bremer](Lars_Bremer "Lars Bremer"), .., [Hans-Walter Schmitt](index.php?title=Hans-Walter_Schmitt&action=edit&redlink=1 "Hans-Walter Schmitt (page does not exist)"), [Vasik Rajlich](Vasik_Rajlich "Vasik Rajlich") <a id="cite-note-10" href="#cite-ref-10">[10]</a>




```

[Event "Chess960CWC 2008"]
[Site "Mainz"]
[Date "2008.07.30"]
[Round "6"]
[White "Rybka 3 "]
[Black "Naum 3.1"]
[Result "0-1"]
[Variant "chess 960"]
[SetUp "1"]
[FEN "nnbbqrkr/pppppppp/8/8/8/8/PPPPPPPP/NNBBQRKR w HFhf - 0 1"]

{SP 037} 1.Nb3 d6 2.e4 Nb6 3.f4 h5 4.h3 e5 5.fxe5 dxe5 6.d3 Be7 7.Nc3
Nc6 8.Be3 Qd8 9.Qd2 Nd4 10.Ne2 c5 11.c3 Ne6 12.c4 Qd6 13.Nc3 Bd7 14.Na5
Qc7 15.Kh2 Nd4 16.Rhg1 g6 17.Nb3 Kg7 18.Kh1 h4 19.Re1 f5 20.Bf2 f4 21.
Nxd4 cxd4 22.Nd5 Nxd5 23.exd5 Bf5 24.Bf3 a5 25.Qe2 Bd6 26.Bg4 b6 27.Rc1
Qd7 28.Bxf5 gxf5 29.Rge1 Rfg8 30.Rb1 Ra8 31.Qc2 Ra6 32.Re2 Ra7 33.Rbe1
Qc7 34.Qa4 Kg6 35.Kg1 Kg5 36.Rf1 Rb7 37.Qc2 b5 38.b3 a4 39.Qc1 bxc4 40.
bxc4 a3 41.Rc2 Bc5 42.Qa1 Qb8 43.Qd1 Rhh7 44.Re2 Rb2 45.Rfe1 Re7 46.Rf1
Reb7 47.Rc2 Rb1 48.Rc1 R1b4 49.Qe1 Qh8 50.Ra1 Rb2 51.Qa5 Bb4 52.Qa6 Rg7
53.Kh1 Rg8 54.Qa4 Bc3 55.Rac1 Qg7 56.Qd1 Rxa2 57.Qf3 Rb2 58.Rg1 a2 59.c5
Bd2 60.Ra1 Be3 61.Bxe3 dxe3 62.d6 Qf7 63.c6 Qe6 64.d7 Rf2 65.Rac1 Qd6 66.
Qd1 a1=Q 67.Rxa1 Qxc6 68.Ra7 Kh6 69.d8=Q Rxd8 70.Qa1 Qf6 71.Qa3 Re8 72.
Qc5 Rg8 73.Rc7 Rg6 74.Rc8 Rb2 75.Rf8 Rc2 76.Qa3 Qd6 77.Rh8+ Kg5 78.Qa8
Rc6 79.Qa7 Rc7 80.Qa1 Qf6 81.Re8 Re7 82.Rd8 Ra7 83.Qxa7 Qxd8 84.Qf7 Qf6
85.Qe8 Qd6 86.Rf1 Rg7 87.Qh8 Rd7 88.Re1 Qf6 89.Qg8+ Qg7 90.Qb3 Rd8 91.
Qa3 Qf8 92.Qb3 Qd6 93.Qb7 Qd7 94.Qb4 Qc7 95.Qa3 Rc8 96.Qa2 Qc3 97.Rg1 Qc6
98.Qa7 Qc7 99.Qa6 Qd7 100.Qa1 Qd4 101.Qa2 Rd8 102.Qe6 Qd6 103.Qc4 Qxd3
104.Qc7 Kf6 105.Ra1 Rd7 106.Qc8 e2 107.Qf8+ Kg5 108.Qg8+ Kh5 109.Qh8+ Kg6
110.Qe8+ Kg7 111.Rg1 Kf6 112.Qh8+ Ke6 113.Qh5 Qd1 114.Qe8+ Kd6 115.Qb8+
Kd5 116.Qb4 Ke6 117.Qa5 Qd2 118.Qa1 Kf6 119.Qa6+ Rd6 120.Qc8 e1=Q 121.
Qf8+ Ke6 122.Qe8+ Kd5 123.Rxe1 Qxe1+ 124.Kh2 f3 125.gxf3 Qg3+ 126.Kh1
Qxf3+ 127.Kh2 Qe2+ 128.Kg1 Qd1+ 129.Kh2 Ke4 130.Qg8 0-1

```


```C++
"Take me to the hospital, that was crazy like that", said an exhausted [Alexander Naumov](Alexander_Naumov "Alexander Naumov") right after [his opponent](Vasik_Rajlich "Vasik Rajlich") resigned. The game was already a few minutes over when he was still shaking like a leaf and his hands were freezing ... 

```

## Publications


* [Arno Nickel](Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) <a id="cite-note-11" href="#cite-ref-11">[11]</a>


## Forum Posts


### 2004


* [Nobady will forget that we have soon a new Gandalf version, but Naum ...](https://www.stmintz.com/ccc/index.php?id=394848) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), November 07, 2004
* [Naum is a copy of ... SENSATION !!](https://www.stmintz.com/ccc/index.php?id=394866) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), November 07, 2004


### 2005 ...


* [Re: Do you evaluate internal nodes?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4155#p21405) by [Naum](Alexander_Naumov "Alexander Naumov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 18, 2006
* [Re: Irrefutable laws of chess programming !](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4197#p21614) by [Naum](Alexander_Naumov "Alexander Naumov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 22, 2006
* [Naum 1.8 for Palm (light version)](https://www.stmintz.com/ccc/index.php?id=442233) by [Alex Naumov](Alexander_Naumov "Alexander Naumov"), [CCC](CCC "CCC"), October 29, 2007
* [Naum EGTB bug](http://www.talkchess.com/forum/viewtopic.php?t=15447) by [Alex Naumov](Alexander_Naumov "Alexander Naumov"), [CCC](CCC "CCC"), July 30, 2007
* [New books for Naum available](http://www.talkchess.com/forum/viewtopic.php?t=17458) by [Alex Naumov](Alexander_Naumov "Alexander Naumov"), [CCC](CCC "CCC"), October 29, 2007
* [Future of Naum](http://www.talkchess.com/forum/viewtopic.php?t=28043&) by [Alexander Naumov](Alexander_Naumov "Alexander Naumov"), [CCC](CCC "CCC"), May 21, 2009


### 2010 ...


* [Naum 4.2 !](http://www.talkchess.com/forum/viewtopic.php?t=33253) by Vael Jean-Paul, [CCC](CCC "CCC"), March 14, 2010
* [NAUM 4.2](http://www.talkchess.com/forum/viewtopic.php?t=33366) by George Bodkin, [CCC](CCC "CCC"), March 20, 2010
* [Naum 4.2 FRC](http://www.talkchess.com/forum/viewtopic.php?t=33429) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), March 23, 2010
* [Wrong draw claim by Naum 4.2 ?](http://www.talkchess.com/forum/viewtopic.php?t=37592) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), January 12, 2011 » [Draw](Draw "Draw"), [Insufficient Material](Material#InsufficientMaterial "Material")
* [Bad news Naum chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=44701) by [Jose Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), August 06, 2012
* [Naum 4.5?](http://www.talkchess.com/forum/viewtopic.php?t=49627) by Tony Mokonen, [CCC](CCC "CCC"), October 07, 2013
* [Naum 4.6 (64-bit only) free to you all!](http://www.talkchess.com/forum/viewtopic.php?t=53858) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), September 28, 2014
* [Naum 4.6 - DrawContemptScore & MaterialImportance](http://www.talkchess.com/forum/viewtopic.php?t=53863) by Lonnie Cook, [CCC](CCC "CCC"), September 28, 2014


## External Links


### Chess Engine


* [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
* [Naum - Frequently Asked Questions](https://web.archive.org/web/20120529171234/http://naumchess.brinkster.net/faq.html) hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive): [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [Naum (chess) from Wikipedia](https://en.wikipedia.org/wiki/Naum_%28chess%29)
* [The chess games of Naum](http://www.chessgames.com/perl/chessplayer?pid=111056) from [chessgames.com](http://www.chessgames.com/index.html)
* [Naum](http://computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Naum&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) from [CCRL 40/40](CCRL "CCRL")


### Misc


* [Saint Naum from Wikipedia](https://en.wikipedia.org/wiki/Saint_Naum)
* [Airto Moreira](Category:Airto_Moreira "Category:Airto Moreira") - [Return to Forever](Category:Return_to_Forever "Category:Return to Forever"), [Free](https://en.wikipedia.org/wiki/Free_%28Airto_album%29) (1972), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Chick Corea](Category:Chick_Corea "Category:Chick Corea"), [Flora Purim](Category:Flora_Purim "Category:Flora Purim"), [Airto Moreira](Category:Airto_Moreira "Category:Airto Moreira"), [Joe Farrell](Category:Joe_Farrell "Category:Joe Farrell"), [Hubert Laws](https://en.wikipedia.org/wiki/Hubert_Laws), [Stanley Clarke](Category:Stanley_Clarke "Category:Stanley Clarke"), [Keith Jarrett](Category:Keith_Jarrett "Category:Keith Jarrett"), [George Benson](Category:George_Benson "Category:George Benson"), et al.
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Saint Naum from Wikipedia](https://en.wikipedia.org/wiki/Saint_Naum)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Naum 4.6 (64-bit only) free to you all!](http://www.talkchess.com/forum/viewtopic.php?t=53858) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), September 28, 2014
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Do you evaluate internal nodes?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4155#p21405) by [Naum](Alexander_Naumov "Alexander Naumov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 18, 2006
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: Irrefutable laws of chess programming !](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4197#p21614) by [Naum](Alexander_Naumov "Alexander Naumov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 22, 2006
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Chess Classic Mainz Category 29: The strongest chess tournament…ever! Livingston Chess960 computer chess world championship](http://www.chesstigers.de/ccm9_index_news.php?id=1406&rubrik=6&lang=1&kat=6) from [chesstigers](http://www.chesstigers.de/ccm9.php?lang=1)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [LatestChess - News - Chess960 computer chess world championship: The strongest chess tournament ever](http://latestchess.com/showNews.php?id=165) July 23, 2008 from [LatestChess - The Complete Chess Portal](http://www.latestchess.com/)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [The chess games of Naum](http://www.chessgames.com/perl/chessplayer?pid=111056) from [chessgames.com](http://www.chessgames.com/index.html)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Mainz Chess Classic 2008: die vierte Livingston Chess960 Computer World Championship](http://www.chesstigers.de/ccm9_index_news.php?id=1435&rubrik=6&lang=0&kat=6) by [Eric van Reem](Eric_van_Reem "Eric van Reem"), June 31, 2008 (German) from [chesstigers.de](http://www.chesstigers.de/ccm9.php?lang=0)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Rybka und Naum führen beim stärksten Turnier aller Zeiten](http://www.chessbase.de/nachrichten.asp?newsid=7990) by [Eric van Reem](Eric_van_Reem "Eric van Reem"), July 31, 2008, [ChessBase News](ChessBase "ChessBase") (German)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> Photos by [Eric van Reem](Eric_van_Reem "Eric van Reem") (glued by the editor), [Mainz Chess Classic 2008: die vierte Livingston Chess960 Computer World Championship](http://www.chesstigers.de/ccm9_index_news.php?id=1435&rubrik=6&lang=0&kat=6) by [Eric van Reem](Eric_van_Reem "Eric van Reem"), July 31, 2008, [chesstigers.de](http://www.chesstigers.de/ccm9.php?lang=0) (German)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> Part 1 covers [Houdini](Houdini "Houdini"), [Rybka](Rybka "Rybka"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish"), [Critter](Critter "Critter"), Naum, [Chiron](Chiron "Chiron") and [Spike](Spike "Spike")
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: Naum 4.6 - DrawContemptScore & MaterialImportance](http://www.talkchess.com/forum/viewtopic.php?t=53863&start=1) by James I, [CCC](CCC "CCC"), September 29, 2014

**[Up one Level](Engines "Engines")**







 
