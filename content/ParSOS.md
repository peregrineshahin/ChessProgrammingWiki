---
title: ParSOS
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* ParSOS**


**ParSOS**, (Parallel SOS)  

the [parallel](Parallel_Search "Parallel Search") version of [Rudolf Huber's](Rudolf_Huber "Rudolf Huber") [MTD(f)](MTD(f) "MTD(f)") searcher [SOS](SOS "SOS"), written in [C](C "C"). ParSOS played the [WMCCC 2001](WMCCC_2001 "WMCCC 2001"), [WCCC 2002](WCCC_2002 "WCCC 2002"), [WCCC 2003](WCCC_2003 "WCCC 2003"), [WCCC 2004](WCCC_2004 "WCCC 2004") and the [WCCC 2006](WCCC_2006 "WCCC 2006") [World Microcomputer Chess](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship") and [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship"), the [Chess960CWC 2005](Chess960CWC_2005 "Chess960CWC 2005") and [Chess960CWC 2006](Chess960CWC_2006 "Chess960CWC 2006") [Livingston Chess960 Computer World Championships](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), and the [IPCCC 2004](IPCCC_2004 "IPCCC 2004") and [IPCCC 2007](IPCCC_2007 "IPCCC 2007"). According to a [CCC](CCC "CCC") discussion with [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner") <a id="cite-note-1" href="#cite-ref-1">[1]</a> and [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen") <a id="cite-note-2" href="#cite-ref-2">[2]</a> involved, ParSOS uses a kind of [ABDADA](ABDADA "ABDADA") to parallelize MTD(f), utilizing a [Shared Hash Table](Shared_Hash_Table "Shared Hash Table").



### Contents


* [1 Photos & Games](#photos-.26-games)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
* [4 References](#references)






 [](File:RudolfHuberSteffenJacob.jpg) 
[WCCC 2003](WCCC_2003 "WCCC 2003"), [Rudolf Huber](Rudolf_Huber "Rudolf Huber") and [Steffen A. Jakob](Steffen_A._Jakob "Steffen A. Jakob") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, round 4, ParSOS - [Hossa](Hossa "Hossa") <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "WCCC 2003"]
[Site "Graz"]
[Date "2003.11.24"]
[Round "4"]
[White "ParSOS"]
[Black "Hossa"]
[Result "1-0"]

1.c4 e5 2.g3 Nf6 3.Bg2 d5 4.cxd5 Nxd5 5.Nf3 Nc6 6.O-O Nb6 7.Nc3 Be7 8.d3 O-O 
9.Be3 Be6 10.Rc1 Nd5 11.d4 exd4 12.Bxd4 Nxc3 13.Bxc3 Bxa2 14.Qa4 Be6 15.Rfd1 
Qc8 16.Nd2 Rd8 17.Nc4 Bd7 18.Ne3 Bg5 19.f4 Be7 20.Kh1 Bc5 21.Nd5 Bd6 22.Qc2 
Bf5 23.e4 Bg4 24.Rd2 Be6 25.e5 Bc5 26.Be4 Bxd5 27.Rxd5 Rxd5 28.Bxd5 Qd7 29.Rd1 
Rd8 30.Qe4 Kh8 31.f5 Qe7 32.Rf1 Nb4 33.f6 gxf6 34.Bb3 c6 35.Rf5 Nd5 36.Rh5 f5 
37.Qxf5 f6 38.exf6 1-0

```

## Forum Posts


* [Parallel algorithms in chess programming](https://www.stmintz.com/ccc/index.php?id=163888) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), April 16, 2001 » [ABDADA](ABDADA "ABDADA"), [Parallel Search](Parallel_Search "Parallel Search")
* [CI 89 and Combinations from Graz 2003 - Parsos/DJ & List/Shredder](https://www.stmintz.com/ccc/index.php?id=364169) by [Mike Byrne](Michael_Byrne "Michael Byrne"), May 08, 2004


## External Links


* [SOS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=21) includes ParSOS
* [The chess games of ParSOS](http://www.chessgames.com/player/parsos_%28computer%29.html) from [chessgames.com](http://www.chessgames.com/index.html)
* [Interview with SOS programmer Rudolf Huber in German language!](https://web.archive.org/web/20120106031235/http://www.playwitharena.com/?Newsticker:Archive_9) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](Arena "Arena") - Archive 9, 132, May 10, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Parallel algorithms in chess programming](https://www.stmintz.com/ccc/index.php?id=163888) by [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner"), [CCC](CCC "CCC"), April 16, 2001
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Parallel algorithms in chess programming](https://www.stmintz.com/ccc/index.php?id=163895) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), April 16, 2001
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Brutus auf WM-Kurs?](http://www.chessbase.de/nachrichten.asp?newsid=2635) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), Images by [Matthias Wüllenweber](Matthias_W%C3%BCllenweber "Matthias Wüllenweber"), [ChessBase News](ChessBase "ChessBase"), November 24, 2003 (German)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [WCCC (4) ParSOS vs Hossa (1-0) PGN](https://www.stmintz.com/ccc/index.php?id=330155) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), November 24, 2003

**[Up one level](Engines "Engines")**







 
