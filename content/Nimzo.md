---
title: Nimzo
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nimzo**



[ Aron Nimzowitsch <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Nimzo**,  

a chess program by primary developer [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), subsequently supported by members of the [First Vienna Computer Chess Club](index.php?title=First_Vienna_Computer_Chess_Club&action=edit&redlink=1 "First Vienna Computer Chess Club (page does not exist)") (Nimzo Werkstatt) concerning [testing](Engine_Testing "Engine Testing"), [chess knowledge](Knowledge "Knowledge"), [opening book](Opening_Book "Opening Book") and hardware. The program was first dubbed *Nimzo-Guernica* in remembrance to [Aron Nimzowitsch](https://en.wikipedia.org/wiki/Aron_Nimzowitsch) and as manifest of Chrilly's [Anti-war](https://en.wikipedia.org/wiki/Anti-war) engagement <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It had its tournament debut at the [3rd Computer Olympiad 1991](3rd_Computer_Olympiad#Chess "3rd Computer Olympiad") and further played the [DOCCC 1991](DOCCC_1991 "DOCCC 1991") and [IPCCC 1991](IPCCC_1991 "IPCCC 1991"). At the [WMCCC 1993](WMCCC_1993 "WMCCC 1993"), Nimzo-Guernica aka Nimzo-2 upset [Mephisto Gideon](Gideon "Gideon") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and later winner [HIARCS](HIARCS "HIARCS") to lead the pack after five rounds, and finished strong fourth despite 1.5 points out of the last four rounds. 



## Photos & Games


 [](http://www.thorstenczub.de/aegon.html) 
[David Bronstein](David_Bronstein "David Bronstein") playing Nimzo by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Johan de Koning](Johan_de_Koning "Johan de Koning") kibitzing, [Aegon 1997](Aegon_1997 "Aegon 1997") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "AEGON 1997"]
[Site "The Hague NED"]
[Date "1997.04.17"]
[Round "02"]
[White "David Bronstein"]
[Black "NIMZO"]
[Result "0-1"]

1.e4 c5 2.Nf3 d6 3.c3 Nf6 4.Bd3 Bg4 5.h3 Bxf3 6.Qxf3 Nc6 7.O-O g6 8.Bb5 Bg7 9.e5 dxe5 
10.Bxc6+ bxc6 11.Qxc6+ Nd7 12.d3 O-O 13.Nd2 Rc8 14.Qa6 Qb6 15.Qa4 Rfd8 16.Nb3 Nf6 
17.Qc4 Ne8 18.Bg5 Nd6 19.Qa4 Bf6 20.Be3 Nf5 21.Qc4 Nxe3 22.fxe3 a5 23.Rad1 a4 24.Nd2 
Qxb2 25.Ne4 Qe2 26.Rfe1 Qh5 27.Rd2 Bg5 28.Rf2 e6 29.Rf3 Qh6 30.Kh1 Be7 31.Ref1 Qg7 
32.g4 a3 33.g5 Rd5 34.h4 Rcd8 35.Nf2 h5 36.e4 R5d7 37.Qa6 Qf8 38.Nd1 Qe8 39.Kg2 Bf8
40.R1f2 Rd6 41.Qc4 R6d7 42.Rd2 Rb7 43.Kf1 Rdb8 44.Ke2 Ra7 45.d4 Ra4 46.Qd3 cxd4 
47.c4 Qc6 48.Rc2 Rbb4 49.c5 Ra5 50.Nf2 Rxc5 51.Rxc5 Rb2+ 52.Kf1 Qxc5 53.Qa6 Rxa2 
54.Qa7 f6 55.gxf6 Rb2 56.Qa8 Qc1+ 57.Kg2 a2 58.Qe8 a1=Q 59.Qxg6+ Kh8 60.Qxh5+ Qh6 
61.Qf7 Qd1 62.Rg3 Rxf2+ 63.Kxf2 Qhd2# 
0-1

```

[View this game on Lichess.org](https://lichess.org/t9MXstG9)



## Nimzo-3


Guernica and Nimzo-2 were leaf evaluators to spent 60 to 70 percent of its time in [evaluation](Evaluation "Evaluation"). The main design criterion for Nimzo-3 was combining the positional play of Nimzo-2 with the [tactical](Tactics "Tactics") strength of a program like [Fritz](Fritz "Fritz"). Nimzo-3 therefor became a [Genius](Chess_Genius "Chess Genius")/Fritz like program with a complex root evaluation <a id="cite-note-6" href="#cite-ref-6">[6]</a>, called [Oracle](Oracle "Oracle") as proposed by [Hans Berliner](Hans_Berliner "Hans Berliner") <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>, and which seems to have been first used by [Kaare Danielsen](Kaare_Danielsen "Kaare Danielsen"). The oracle approach with very simple, mainly first-order evaluation terms at the leaves, made Nimzo-3 to spent about only 10 to 20 percent on leaf evaluation, yielding in an increased node rate of 400%. 



## CHE


The [CHE](index.php?title=CHE&action=edit&redlink=1 "CHE (page does not exist)") and CHE++ declarative language for expressing chess knowledge using a [GUI](GUI "GUI") was used to incorporate [planning](Planning "Planning") features within the [oracle](Oracle "Oracle") used <a id="cite-note-9" href="#cite-ref-9">[9]</a>. 



## Commerce


During the [WMCCC 1996](WMCCC_1996 "WMCCC 1996"), Nimzo was still amateur, but soon went commercial as [MS-DOS](MS-DOS "MS-DOS") program Nimzo 3.5 and the [Windows](Windows "Windows") program Nimzo 2000 distributed by [Weiner's](Ossi_Weiner "Ossi Weiner") [Millennium 2000 GmbH](Millennium_2000_GmbH "Millennium 2000 GmbH"), later released as [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant engine WBNimzo. Nimzo98, Nimzo99 were native [ChessBase](ChessBase "ChessBase") engines, followed by Nimzo 7.32 and Nimzo 8 and its derivation [Schweinehund](Schweinehund "Schweinehund") <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>. 



## Description


given in 1999 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-12" href="#cite-ref-12">[12]</a>:




```C++Nimzo is one of the leading professional chess programs. It combines sound positional play with extremely strong tactics. Nimzo-Paderborn is a considerable improved version of the currently commercially available programs Nimzo98, Nimzo99 and Nimzo2000.

```


```C++Nimzo-Paderborn [learns](Learning "Learning") automatically from human grandmaster games. It is also equipped with an own Chess-Advice-Language (Che++) which allows strong human players to formulate chess-knowledge. The program can also access in its search [endgame databases](Endgame_Tablebases "Endgame Tablebases"). It therefore searches regularly from the middlegame into won endgames. 

```





## Forward Pruning in Nimzo 2.2.1


Following [forward pruning](Pruning "Pruning") code appears in Nimzo's 2.2.1 search routine <a id="cite-note-13" href="#cite-ref-13">[13]</a> applied at [frontier nodes](Frontier_Nodes "Frontier Nodes"), notably the aggressive [Lang](Richard_Lang "Richard Lang") mode at pre-pre-frontier nodes or below. The source was published along with a foreword by Donninger in 2002 <a id="cite-note-14" href="#cite-ref-14">[14]</a> :




```C++
  if((depth <= 1) && (!extflg) && (score > beta) && (GPtr->hung.w <= KNIGHTHUNG)) {
    return score;
  }

  if(LangModus) {
    if((depth <= 3) && (!extflg) && (score > beta) && (GPtr->hung.w == 0)) {
      return score;
    }
  }

```

## See also


* [Brutus](Brutus "Brutus")
* [Greif](Greif "Greif")
* [Hydra](Hydra "Hydra")
* [Hydra 97](Hydra_97 "Hydra 97")
* [Nimzo's winning white-black bug](WMCCC_1993#NimzoBug "WMCCC 1993"), [WMCCC 1993](WMCCC_1993 "WMCCC 1993")
* [Schweinehund](Schweinehund "Schweinehund")


## Publications


* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1992**). *The Relation of Mobility, Strategy and the Mean Dead Rabbit in Chess*. Heuristic Programming in Artificial Intelligence 3: the third computer olympiad (eds. [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and [Victor Allis](Victor_Allis "Victor Allis")), pp. 102-111. Ellis Horwood Ltd., Chichester, UK. ISBN 0-13-388265-9
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs*. [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
* [Thomas Mally](Thomas_Mally "Thomas Mally") (**1993**). *PC Power in Braille - Nimzo Guernica: Ein PC-Schachprogramm für Blinde*. [PC Schach](PC_Schach "PC Schach") 3/93 (German) <a id="cite-note-15" href="#cite-ref-15">[15]</a>
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")


## Forum Posts


### 1996 ...


* [NIMZO 3 ist out now!](https://groups.google.com/d/msg/rec.games.chess.computer/fON9kA5LPYo/Jpfn6nqs3yYJ) by [Tom Kerrigan](Tom_Kerrigan "Tom Kerrigan"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 15, 1996


 [Re: NIMZO 3 ist out now!](https://groups.google.com/d/msg/rec.games.chess.computer/fON9kA5LPYo/_utfvtP6RzsJ) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), July 19, 1996
* [Re: Nimzo3 - playing strength?](https://groups.google.com/d/msg/rec.games.chess.computer/lZshGHUeuxY/Kfef3R7vIkQJ) by [Helmut Weigel](Helmut_Weigel "Helmut Weigel"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 04, 1996
* [NIMZO 3 !](https://groups.google.com/d/msg/rec.games.chess.computer/o57y2Ldf-ks/rlfhb1TeyYMJ) by Komputer Korner, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 01, 1996
* [Re: computer chess "oracle" ideas...](https://groups.google.com/g/rec.games.chess.computer/c/me7GkjsEgds/m/E2WkkperxfkJ) by [Andreas Mader](Andreas_Mader "Andreas Mader"), reply to [Ronald de Man](Ronald_de_Man "Ronald de Man"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1997
* [Re: Mobility in eval](https://www.stmintz.com/ccc/index.php?id=12445) by [Andreas Mader](Andreas_Mader "Andreas Mader"), [CCC](CCC "CCC"), November 26, 1997
* [Re: Any word on future Nimzo plans](https://groups.google.com/g/rec.games.chess.computer/c/HMerbVnDF-Q/m/S-zPAuB5kioJ) by [Andreas Mader](Andreas_Mader "Andreas Mader"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 22, 1998


### 2000 ...


* [Nimzo 8 and piece values](https://www.stmintz.com/ccc/index.php?id=148289) by Matthew Barnett, [CCC](CCC "CCC"), January 05, 2001
* [Nimzo Engines of Millenium Chess System](http://www.talkchess.com/forum/viewtopic.php?t=60404) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 08, 2016


## External Links


### Chess Engine


* [Nimzo's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=93)
* [Willkommen auf der NIMZO Homepage!](https://web.archive.org/web/19991001153019/http://mitglied.tripod.de/Nimzo_Werkstatt/index.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), October 01, 1999)


### Misc


* [Aron Nimzowitsch from Wikipedia](https://en.wikipedia.org/wiki/Aron_Nimzowitsch)
* [Guernica (town) from Wikipedia](https://en.wikipedia.org/wiki/Guernica_%28town%29)
* [Bombing of Guernica from Wikipedia](https://en.wikipedia.org/wiki/Bombing_of_Guernica)
* [Guernica (painting) from Wikipedia](https://en.wikipedia.org/wiki/Guernica_%28painting%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Aron Nimzowitsch from Wikipedia](https://en.wikipedia.org/wiki/Aron_Nimzowitsch)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Bombing of Guernica from Wikipedia](https://en.wikipedia.org/wiki/Bombing_of_Guernica)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> With the help of a sign bug in [passed pawn](Passed_Pawn "Passed Pawn") evaluation, see [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1999**). *Computer machen keine Fehler*. [CSS](Computerschach_und_Spiele "Computerschach und Spiele") 2/99, [pdf](http://www.mustrum.de/chrilly/keine_fehler.pdf) (German)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Photo](https://commons.wikimedia.org/wiki/File:Guernica_reproduction_on_tiled_wall,_Guernica,_Spain_(PPL3-Altered)_julesvernex2.jpg) by [Jules Verne Times Two](https://commons.wikimedia.org/wiki/User:Julesvernex2), September 08, 2018, [Guernica](https://en.wikipedia.org/wiki/Guernica), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [David Bronstein](David_Bronstein "David Bronstein") vs. Nimzo, Photo by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") from [Aegon 1996-97](http://www.thorstenczub.de/aegon.html)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1996**). *CHE: A Graphical Language for Expressing Chess Knowledge*. [ICCA Journal, Vol. 19, No. 4](ICGA_Journal#19_4 "ICGA Journal")
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1987**). *Some Innovations Introduced by Hitech*. [ICCA Journal, Vol. 10, No. 3](ICGA_Journal#10_3 "ICGA Journal")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1989**). *Some Innovations Introduced by Hitech*. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5")
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [CHE docs in English / Nimzo 3 version](https://www.stmintz.com/ccc/index.php?id=198528) by [Mike S.](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), November 22, 2001
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Versions of Nimzo](https://www.stmintz.com/ccc/index.php?id=144598) by Shep, [CCC](CCC "CCC"), December 12, 2000
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Re: Nimzo 4](https://www.stmintz.com/ccc/index.php?id=265975) by [Manfred Meiler](index.php?title=Manfred_Meiler&action=edit&redlink=1 "Manfred Meiler (page does not exist)"), [CCC](CCC "CCC"), November 19, 2002
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Nimzo's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=93)
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> Nimzo: sr.c: search-tree handling (dead acor link) hosted by Roger Thormann
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> home.arcor.de/roger.thormann/yacdb.com/nimzo/vorwort.html Vorwort von Chrilly Donninger (German) hosted by Roger Thormann
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Braille from Wikipedia](https://en.wikipedia.org/wiki/Braille)

**[Up one Level](Engines "Engines")**







 
