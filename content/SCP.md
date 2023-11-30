---
title: SCP
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* SCP**


**SCP**, (Stanback Chess Program, also mentioned as JSCP)  

an [open source chess program](Category:Open_Source "Category:Open Source") by [John Stanback](John_Stanback "John Stanback"), written in [C](C "C") and published in May 1987 at [comp.sources.games](Computer_Chess_Forums "Computer Chess Forums") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. SCP later evolved to [GNU Chess 2-4](GNU_Chess "GNU Chess"), and was also ported to the [Amiga](Amiga "Amiga") as *Chess* and *Chess 2.0*, the latter with a mouse-driven [GUI](GUI "GUI") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. A [WinBoard](WinBoard "WinBoard") compatible version of SCP was most recently updated by [Jim Ablett](Jim_Ablett "Jim Ablett") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Search


SCP [represents the board](Board_Representation "Board Representation") as 12x12 [mailbox](Mailbox "Mailbox") [array](Array "Array") with [piece lists](Piece-Lists "Piece-Lists"), and uses full-width [alpha-beta](Alpha-Beta "Alpha-Beta") with [extensions](Extensions "Extensions") on [checks](Check "Check"), [check evasions](Check_Extensions "Check Extensions"), [promotions](Promotions "Promotions"), [threats](Mate_Threat_Extensions "Mate Threat Extensions") and threats to multiple pieces. Capture sequences are handled by a [separate search routine](Quiescence_Search "Quiescence Search"). 




### Repetitions


SCP seems to originate the [repetition](Repetitions "Repetitions") counting algorithm, also found in some [GNU Chess](GNU_Chess "GNU Chess") versions, [TSCP](TSCP "TSCP") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, and [Belzebub](Belzebub "Belzebub"). It may detect false repetitions in case of exchanging two unequal pieces <a id="cite-note-6" href="#cite-ref-6">[6]</a>.




```C++

  for (i = GameCnt; i > Game50; i--)  {
    m = GameList[i]; f = m>>8; t = m & 0xFF;
    if (t != 255 && f != 255) {
      b[f]++; b[t]--;
      if (b[f] == 0) c--; else c++;
      if (b[t] == 0) c--; else c++;
      if (c == 0) r++;
    }
  }

```

### Evaluation


SCP's [evaluation](Evaluation "Evaluation") considers [material](Material "Material"), [piece-square tables](Piece-Square_Tables "Piece-Square Tables") for knights, bishops and [passed pawns](Passed_Pawn "Passed Pawn"), [piece mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure"), [rook on (half) open files](Rook_on_Open_File "Rook on Open File"), and some [king safety](King_Safety "King Safety") issues and positive [king centre proximity](King_Centralization "King Centralization") in the endgame.



## Publications


* [Gerald Tesauro](Gerald_Tesauro "Gerald Tesauro") (**2001**). *[Comparison Training of Chess Evaluation Functions](http://dl.acm.org/citation.cfm?id=644397)*. In [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [Miroslav Kubat](Miroslav_Kubat "Miroslav Kubat") (eds.) (**2001**). *[Machines that learn to play games](index.php?title=Thttps://www.novapublishers.com/catalog/product_info.php%3Fproducts_id%3D720&action=edit&redlink=1 "Thttps://www.novapublishers.com/catalog/product info.php?products id=720 (page does not exist)")*, 117–130, [Nova Science Publishers](https://en.wikipedia.org/wiki/Nova_Science_Publishers) » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Deep Blue](Deep_Blue "Deep Blue")


## See also


* [GNU Chess](GNU_Chess "GNU Chess")
* [TSCP](TSCP "TSCP")
* [Zarkov](Zarkov "Zarkov")


## Forum Posts


* [v01i023: chess - C source for chess](https://groups.google.com/d/msg/comp.sources.games/zs_1mrpdseE/YL2yGrzoXrEJ) by [John Stanback](John_Stanback "John Stanback"), [comp.sources.games](Computer_Chess_Forums "Computer Chess Forums"), May 21, 1987
* [SCP: ANSI C chess program package available via ftp](https://groups.google.com/d/msg/rec.games.chess/HG6FoUy9K18/YqrV-dNZhoUJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), December 26, 1993
* [SCP source now at my site](https://www.stmintz.com/ccc/index.php?id=74307) by [Pete Galati](index.php?title=Pete_Galati&action=edit&redlink=1 "Pete Galati (page does not exist)"), [CCC](CCC "CCC"), October 19, 1999
* [Winboard compatible version of SCP?](https://www.stmintz.com/ccc/index.php?id=85776) by Scott Ludwig, [CCC](CCC "CCC"), January 03, 2000
* [An Oldie, but a Goodie: Port of ancient SCP program plays itself...](https://www.stmintz.com/ccc/index.php?id=169105) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 10, 2001
* [SCP 1.0d update](http://www.talkchess.com/forum/viewtopic.php?t=14436) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), June 11, 2007
* [SCP/Gnuchess 2.02 JA by John Stanback - Update](http://www.talkchess.com/forum/viewtopic.php?t=29106) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), July 25, 2009


## External Links


* [John Stanback's Home Page](http://john.stanback.net/)
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [SCP](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/SCP/) maintained and updated by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Chess for Amiga (1987)](http://www.mobygames.com/game/chess_______), [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
* [Chess 2.0 for Amiga (1989)](http://www.mobygames.com/game/amiga/chess-20), [MobyGames](https://en.wikipedia.org/wiki/MobyGames)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [v01i023: chess - C source for chess](https://groups.google.com/d/msg/comp.sources.games/zs_1mrpdseE/YL2yGrzoXrEJ) by [John Stanback](John_Stanback "John Stanback"), [comp.sources.games](Computer_Chess_Forums "Computer Chess Forums"), May 21, 1987
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Chess 2.0 for Amiga (1989)](http://www.mobygames.com/game/amiga/chess-20), [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [SCP/Gnuchess 2.02 JA by John Stanback - Update](http://www.talkchess.com/forum/viewtopic.php?t=29106) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), July 25, 2009
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [SCP](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/SCP/) maintained and updated by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Detecting three-fold repetition?](https://www.stmintz.com/ccc/index.php?id=119911) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), July 17, 2000
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: Move Tables - explain as if I'm five](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=490672&t=45846) by [Karlo Bala Jr.](Karlo_Balla "Karlo Balla"), [CCC](CCC "CCC"), November 05, 2012
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one level](Engines "Engines")**







 
