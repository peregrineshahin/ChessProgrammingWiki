---
title: Ktulu
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Ktulu**



[ Artist depiction of Ktulu <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ktulu**,  

a commercial [UCI](UCI "UCI") and [WinBoard](WinBoard "WinBoard") compatible chess engine by [Rahman Paidar](Rahman_Paidar "Rahman Paidar") distributed by [Lokasoft](Lokasoft "Lokasoft"), but as of July 2020 no longer available <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Ktulu has a sophisticated [evaluation](Evaluation "Evaluation") - [King safety](King_Safety "King Safety") and [passed pawn](Passed_Pawn "Passed Pawn") evaluation, 
completely rewritten in version 6.2, are responsible for its dangerous attacking style with strong [tactical](Tactics "Tactics") and positional play. 
Further, some unsafe [pruning](Pruning "Pruning") algorithms were replaced with more sound methods 
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.
The first version of Ktulu was written in early 2002 in [Turbo Pascal](Pascal#TurboPascal "Pascal") under [MS-DOS](MS-DOS "MS-DOS"). The development of the [Windows](Windows "Windows") version started in summer 2002 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Photos & Games](#photos-.26-games)
	+ [2.1 Ktulu - Hermann](#ktulu---hermann)
	+ [2.2 Ktulu - Deep Sjeng](#ktulu---deep-sjeng)
* [3 Publications](#publications)
* [4 Forum Posts](#forum-posts)
	+ [4.1 2003](#2003)
	+ [4.2 2004](#2004)
	+ [4.3 2005 ...](#2005-...)
	+ [4.4 2010 ...](#2010-...)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Ktulu/Cthulhu](#ktulu.2fcthulhu)
		- [5.2.1 Cthulhu Mythos](#cthulhu-mythos)
		- [5.2.2 Call of Cthulhu](#call-of-cthulhu)
* [6 References](#references)






Ktulu played four [CSVN](CSVN "CSVN") tournaments over the board, the [Leiden](https://en.wikipedia.org/wiki/Leiden) [DOCCC 2005](DOCCC_2005 "DOCCC 2005"), [DOCCC 2008](DOCCC_2008 "DOCCC 2008"), [ICT 2009](ICT_2009 "ICT 2009") and [DOCCC 2009](DOCCC_2009 "DOCCC 2009"), operated by [Hans Secelle](Hans_Secelle "Hans Secelle").
Ktulu furher participated at the [CCT10](CCT10 "CCT10"), [CCT11](CCT11 "CCT11") and [CCT12](CCT12 "CCT12") online tournaments, and the [WCRCC 2007](WCRCC_2007 "WCRCC 2007") - the first [ACCA World Computer Rapid Chess Championship](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship").



## Photos & Games


### Ktulu - Hermann


 [](File:KtuluHermannICT2009.jpg) 
[ICT 2009](ICT_2009 "ICT 2009"), [Volker Annuss](Volker_Annuss "Volker Annuss") and [Hans Secelle](Hans_Secelle "Hans Secelle"), Ktulu - [Hermann](Hermann "Hermann")




```

[Event "ICT 2009"]
[Site "Leiden, NED"]
[Date "2009.06.05"]
[Round "4"]
[White "Ktulu 9"]
[Black "Hermann 2.4.24"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Qb6 8.Qd2 Qxb2 9.Rb1 Qa3 
10.e5 dxe5 11.fxe5 Nfd7 12.Be2 Qa5 13.Nb3 Qc7 14.O-O Nxe5 15.Bh5 Nbc6 16.Ne4 Ba3 17.Qe3 
Be7 18.Qg3 g6 19.Nf6+ Bxf6 20.Bxf6 Rg8 21.Be2 Qb8 22.Qh4 Nd7 23.Bc3 h5 24.Rbd1 Qa7+ 
25.Rf2 Qe3 26.Rd3 Qh6 27.Nd2 f5 28.Nc4 Rg7 29.Nd6+ Kf8 30.Bf3 Re7 31.Bxc6 bxc6 32.Rfd2 
c5 33.Nxc8 Rxc8 34.Rxd7 Qe3+ 35.Kf1 g5 36.Qxh5 Qf4+ 37.Ke2 Qe4+ 38.Kd1 Qg4+ 39.Qxg4 fxg4 
40.Bf6 Rxd7 41.Rxd7 Rb8 42.Rd8+ Rxd8+ 43.Bxd8 Kf7 44.Bxg5 Kg6 45.Be7 Kf5 46.Bxc5 Ke4 
47.h4 gxh3 48.gxh3 Kf5 49.h4 e5 50.Bb6 Ke6 51.h5 Kf6 52.h6 1-0

```

### Ktulu - Deep Sjeng


 [](File:KtuluSjeng2009.jpg) 
[DOCCC 2009](DOCCC_2009 "DOCCC 2009"), Ktulu - [Deep Sjeng](Deep_Sjeng "Deep Sjeng"), [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") and [Hans Secelle](Hans_Secelle "Hans Secelle") with [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")




```

[Event "DOCCC 2009"]
[Site "Leiden NED"]
[Date "2009.10.18"]
[Round "8"]
[White "Ktulu"]
[Black "Deep Sjeng"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 Nbd7 7.Bc4 e6 8.O-O Ne5 9.Be2 Be7 
10.f4 Ng6 11.f5 Ne5 12.fxe6 fxe6 13.Bh5+ g6 14.Be2 O-O 15.Qd2 Bd7 16.Kh1 Nf7 17.Be3 b5 
18.a3 Qc7 19.Rf2 Rac8 20.Raf1 Qd8 21.Qd3 Ne5 22.Qd1 Re8 23.Bh6 Rxc3 24.bxc3 Nxe4 25.R2f4 
Nf6 26.R4f2 d5 27.Nb3 Nf7 28.Bc1 Nd6 29.R2f3 Nfe4 30.Bf4 Qc8 31.Be5 Ng5 32.Qc1 Nf5 33.g4 
Nh6 34.R3f2 Nhf7 35.R2xf7 Nxf7 36.Rxf7 Kxf7 37.Qh6 Rf8 38.Qxh7+ Ke8 39.Qxg6+ Kd8 40.Nd4 
Re8 41.Bd3 Bf8 42.Qh7 Be7 43.Qh6 Qc5 44.Nxe6+ Bxe6 45.Qxe6 Bh4 46.Qf5 Qf8 47.Qxf8 Rxf8 
48.Kg2 Be7 49.Kg3 Kd7 50.Bf4 Bxa3 51.h4 Bb2 52.g5 Bxc3 53.h5 Kc6 54.h6 a5 55.g6 a4 56.g7 
Rg8 57.Bh7 Bxg7 58.Bxg8 Bc3 59.Bf7 a3 60.Be8+ Kc5 61.Be3+ Kd6 62.Bxb5 a2 0-1

```

## Publications


* [Klaus Wlotzka](index.php?title=Klaus_Wlotzka&action=edit&redlink=1 "Klaus Wlotzka (page does not exist)") (**2006**). *Ktulu 8 - Interview mit Rahman Paidar*. [CSS Online](Computerschach_und_Spiele "Computerschach und Spiele"), [pdf](https://computerschach.de/Files/2006/CSS-Rangliste%20-%20Der%20Weltmeister%20im%20Blickpunkt.pdf) (German)


## Forum Posts


### 2003


* [Ktulu Chess by Rahman Paidar](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42073) by [Tim Mann](Tim_Mann "Tim Mann"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 05, 2003
* [Ktulu and pondering](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42177) by [George Lyapko](George_Lyapko "George Lyapko"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 11, 2003 » [Pondering](Pondering "Pondering")
* [Ktulu 3.4 has been released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42258) by [Jan Kiwitter](index.php?title=Jan_Kiwitter&action=edit&redlink=1 "Jan Kiwitter (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 16, 2003
* [KTULU: A new strong WB-Engine (soon) - text german, sorry - ?](https://www.stmintz.com/ccc/index.php?id=317576) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), September 24, 2003
* [Ktulu 4.1 and 4.2](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45801) by [Rahman Paidar](Rahman_Paidar "Rahman Paidar"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 29, 2003


### 2004


* [Ktulu goes commercial](https://www.stmintz.com/ccc/index.php?id=357995) by Christian Koch, [CCC](CCC "CCC"), April 02, 2004
* [Ktulu 5.0 by Rahman Paidar commercial available around April 22th, 2004!](https://www.stmintz.com/ccc/index.php?id=360209) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), April 15, 2004
* [Ktulu 5.0 by Rahman Paidar (Iran) available in Gladiator-Shop tomorrow!](https://www.stmintz.com/ccc/index.php?id=362816) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 01, 2004
* [Ktulu 5.0 and Patriot 1.2.2 released ...](https://www.stmintz.com/ccc/index.php?id=362930) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 02, 2004
* [Ktulu 5.1 by Rahman Paidar released ...](https://www.stmintz.com/ccc/index.php?id=368299) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), May 31, 2004


### 2005 ...


* [Ktulu mirage vanishing and precociously marketed shams always coming...](https://www.stmintz.com/ccc/index.php?id=421521) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), April 18, 2005
* [Will Ktulu 7.0 run under Fritz?](https://www.stmintz.com/ccc/index.php?id=423481) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), April 29, 2005
* [Ktulu 7.0 and Lokasoft](https://www.stmintz.com/ccc/index.php?id=446111) by Thomas Logan, [CCC](CCC "CCC"), August 29, 2005
* [Ktulu 7.1 / 7.5](https://www.stmintz.com/ccc/index.php?id=459479) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), November 03, 2005
* [Dutch Open CC 8th round Zappa-Ktulu 1-0](https://www.stmintz.com/ccc/index.php?id=461463) by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), [CCC](CCC "CCC"), November 13, 2005 » [DOCCC 2005](DOCCC_2005 "DOCCC 2005")
* [Re: Rybka test position (Ktulu 7.5)](https://www.stmintz.com/ccc/index.php?id=469226) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), December 12, 2005 » [Rybka](Rybka "Rybka")
* [Ktulu 7.5 Test (40'/40) After 1010 games / 5moves match vs Fritz 9](https://www.stmintz.com/ccc/index.php?id=492059) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), March 08, 2006
* [Any news of Ktulu?](http://www.talkchess.com/forum/viewtopic.php?t=18025) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), November 25, 2007
* [Hiarcs-Ktulu, Leiden 2009](http://www.talkchess.com/forum/viewtopic.php?t=28307) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 08, 2009
* [Tactical Factor in Ktulu 9](http://www.talkchess.com/forum/viewtopic.php?t=31143) by Tom Giampietro, [CCC](CCC "CCC"), December 19, 2009


### 2010 ...


* [Concerning Ktulu 9 (CCT 12)](http://www.talkchess.com/forum/viewtopic.php?t=32214) by David Shanholtzer, [CCC](CCC "CCC"), January 30, 2010
* [Patt-Bug, Junior 11.1a show mate and Ktulu 9.03 made patt!](http://www.talkchess.com/forum/viewtopic.php?t=33435) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), March 23, 2010 » [Stalemate](Stalemate "Stalemate")
* [Ktulu's endgame play](http://www.talkchess.com/forum/viewtopic.php?t=35452) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), July 15, 2010


## External Links


### Chess Engine


* [Ktulu](https://www.lokasoft.nl/ktulu.aspx) from [Lokasoft](Lokasoft "Lokasoft") (as of July 2020, no longer available)
* [Rahman Paidar - Ktulu 8](https://www.schachversand.de/software/schachprogramm/ktulu-8-upgrade.html) - [Schachversand Niggemann](Schachversand_Niggemann "Schachversand Niggemann")
* [Ktulu 6.2 will be released soon](https://web.archive.org/web/20110611144445/http://www.playwitharena.com/?Newsticker:Archive_6), Interview with [Rahman Paidar](Rahman_Paidar "Rahman Paidar") by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena News-Ticker](Arena "Arena") 80, March 15, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Ktulu 7.0 by Rahman Paidar](https://web.archive.org/web/20110611144744/http://www.playwitharena.com/?Newsticker:Archive_7), [Arena News-Ticker](Arena "Arena") 105-107, April 15, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Ktulu's book learning by Rahman Paidar](https://web.archive.org/web/20110611144520/http://www.playwitharena.com/?Newsticker:Archive_9), [Arena News-Ticker](Arena "Arena") 133, May 10, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [SWCR: Ktulu 9.03 Ergebnisse ...](https://www.schach-welt.de/schach/computerschach/news-ticker/archiv-seite-10), [Frank's Chess Page](Frank_Quisinsky "Frank Quisinsky"), News-Ticker 096, March 24, 2010, hosted by [Schachwelt](https://www.schach-welt.de/) (German)
* [Ktulu](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Ktulu&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")
* [Ktulu 4.2](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Ktulu%204.2) in [KCEC](KCEC "KCEC")
* [The chess games of Ktulu](https://www.chessgames.com/perl/chessplayer?pid=109973) from [chessgames.com](https://www.chessgames.com/index.html)
* [Ktulu chess games - 365Chess.com](https://www.365chess.com/players/KTULU)


### Ktulu/Cthulhu


* [Ktulu - Wiktionary](https://en.wiktionary.org/wiki/Ktulu)
* [Cthulhu - Wiktionary](https://en.wiktionary.org/wiki/Cthulhu)
* [Cthulhu from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu)
* [Cthulhu (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_%28disambiguation%29)


### Cthulhu Mythos


* [Cthulhu Mythos from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_Mythos)
* [Cthulhu Mythos in popular culture from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_Mythos_in_popular_culture)
* [Cthulhu Mythos anthology from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_Mythos_anthology)
* [Cthulhu Mythos arcane literature from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_Mythos_arcane_literature)
* [Cthulhu Mythos deities from Wikipedia](https://en.wikipedia.org/wiki/Cthulhu_Mythos_deities)
* [The Shadow Over Innsmouth - Cthulhu Mythos from Wikipedia](https://en.wikipedia.org/wiki/The_Shadow_Over_Innsmouth#Cthulhu_Mythos)
* [CthulhuTech from Wikipedia](https://en.wikipedia.org/wiki/CthulhuTech)


### Call of Cthulhu


* [Call of Cthulhu (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Call_of_Cthulhu)
* [The Call of Cthulhu from Wikipedia](https://en.wikipedia.org/wiki/The_Call_of_Cthulhu)
* [Call of Cthulhu: The Card Game from Wikipedia](https://en.wikipedia.org/wiki/Call_of_Cthulhu:_The_Card_Game)
* [Call of Cthulhu (role-playing game) from Wikipedia](https://en.wikipedia.org/wiki/Call_of_Cthulhu_%28role-playing_game%29)


 [Delta Green from Wikipedia](https://en.wikipedia.org/wiki/Delta_Green)
* [Metallica](Category:Metallica "Category:Metallica") - [The Call of Ktulu](https://en.wikipedia.org/wiki/Ride_the_Lightning#The_Call_of_Ktulu), February 9, 2017, [Copenhagen](https://en.wikipedia.org/wiki/Copenhagen), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> An artist's [visual representation](https://commons.wikimedia.org/wiki/File:Cthulhu_and_R%27lyeh.jpg) of the Elder God [Cthulhu](https://en.wikipedia.org/wiki/Cthulhu), by [BenduKiwi](https://commons.wikimedia.org/wiki/User:BenduKiwi), July 30, 2006, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ktulu](https://www.lokasoft.nl/ktulu.aspx) from [Lokasoft](Lokasoft "Lokasoft") (as of July 2020, no longer available)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ktulu 6.2 will be released soon](https://web.archive.org/web/20110611144445/http://www.playwitharena.com/?Newsticker:Archive_6), Interview with [Rahman Paidar](Rahman_Paidar "Rahman Paidar") by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena News-Ticker](Arena "Arena") 80, March 15, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Klaus Wlotzka](index.php?title=Klaus_Wlotzka&action=edit&redlink=1 "Klaus Wlotzka (page does not exist)") (**2006**). *Ktulu 8 - Interview mit Rahman Paidar*. [CSS Online](Computerschach_und_Spiele "Computerschach und Spiele"), [pdf](https://computerschach.de/Files/2006/CSS-Rangliste%20-%20Der%20Weltmeister%20im%20Blickpunkt.pdf) (German)

**[Up one level](Engines "Engines")**







 
