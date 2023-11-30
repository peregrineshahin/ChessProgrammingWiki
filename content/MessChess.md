---
title: MessChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MessChess**



 [](Hhttp://www.oocities.org/ebnsteve/muirwam.html "Hhttp://www.oocities.org/ebnsteve/muirwam.html") [What-a-Mess](https://en.wikipedia.org/wiki/What-a-Mess) <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**MessChess**, (Mess)  

an experimental private chess engine written by [Mridul Muralidharan](Mridul_Muralidharan "Mridul Muralidharan"), which could be build to run under [Linux](Linux "Linux"), [Solaris](Unix#Solaris "Unix") and [Windows](Windows "Windows"). 
MessChess played the [CCT5](CCT5 "CCT5") and [CCT6](CCT6 "CCT6") online tournaments, and the [WCRCC 2008](WCRCC_2008 "WCRCC 2008") ACCA World Computer Rapid Chess Championship. 



## Description


MessChess was used to to test ideas on chess game tree [search](Search "Search"), in particular the effect of heavy [move ordering](Move_Ordering "Move Ordering"), heavy [quiescence search](Quiescence_Search "Quiescence Search"), and various [extensions](Extensions "Extensions"). 
For instance many programs extend most of the useless checks, where MessChess tries to minimize most of these and the logic for this built into the move ordering code <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
MessChess applies [PVS](Principal_Variation_Search "Principal Variation Search") with [aspiration](Aspiration_Windows "Aspiration Windows"), [double null move](Double_Null_Move "Double Null Move") with [R](Depth_Reduction_R "Depth Reduction R") = 3, an extensive quiescence with "good" [captures](Captures "Captures"), "good" [checks](Check "Check"), as well as other tactical moves, and heavily utilizes [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") for [evaluation](Evaluation "Evaluation") and move ordering, storing and retrieving results inside the primary and separate qsearch [transposition tables](Transposition_Table "Transposition Table"), and a [pawn structure-](Pawn_Hash_Table "Pawn Hash Table") and [evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table"). 



## Selected Games


[WCRCC 2008](WCRCC_2008 "WCRCC 2008"), round 10, [Arasan](Arasan "Arasan") - MessChess <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```
[Event "WCRCC 2008"]
[Site "Internet Chess Club"]
[Date "2008.06.22"]
[Round "10"]
[White "Arasan"]
[Black "MessChess"]
[Result "0-1"]

1.d4 d5 2.c4 e6 3.Nf3 dxc4 4.e3 b5 5.a4 c6 6.axb5 cxb5 7.b3 Nc6 8.bxc4 bxc4 
9.Bxc4 Nf6 10.O-O Bd6 11.e4 Be7 12.d5 exd5 13.exd5 Nb4 14.Nc3 O-O 15.Re1 Bg4 
16.Bb3 Rc8 17.Bb2 Bc5 18.Ne4 Nxe4 19.Rxe4 Bh5 20.g4 Bg6 21.Rxb4 Bxb4 22.Qd4 
Qf6 23.Qxf6 gxf6 24.Rxa7 Rb8 25.Ra4 Rfc8 26.Ba2 Bc2 27.Ra6 Be4 28.Kg2 Bc5 
29.Bc1 Bb6 30.Be3 Rc3 31.Kg3 Bxe3 32.fxe3 Rxe3 33.Kf4 Rxf3+ 34.Kxe4 Rh3 
35.Bc4 Re8+ 36.Kd4 Kg7 37.Ra7 Rh4 38.h3 h5 39.d6 hxg4 40.hxg4 Rxg4+ 41.Kd3 
Rd8 42.d7 Rg5 43.Kd4 Kf8 44.Bb3 Ke7 45.Ba4 Rb8 46.Kc4 f5 47.Ra5 f6 48.Bc6 f4 
49.Ra6 Re5 50.Ra1 Rb6 51.d8=N Kxd8 52.Bf3 Ke7 53.Bg4 f5 54.Bf3 Re3 55.Kc5 Rbb3 
56.Bd5 Rbc3+ 57.Kb4 0-1

```

## See also


* [CHAOS](CHAOS "CHAOS")
* [MChess](MChess "MChess")
* [Witchess](Witchess "Witchess")


## Forum Posts


* [Re: In fact, Arasan and KingofKings are Indian !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43743#p167070) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 10, 2003
* [Re: New chess engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46915&p=177483&start=7#p177483) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 18, 2004 » [Natwarlal](Natwarlal "Natwarlal")


## External Links


### Chess Engine


* [MessChess](http://www.geocities.ws/mridulm80/messchess.htm)
* [Information about messchess(C)](http://www.chessclub.com/finger/messchess) from [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")


### Misc


* [mess - Wiktionary](https://en.wiktionary.org/wiki/mess)
* [Mess (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Mess_%28disambiguation%29)


 [Multi Emulator Super System](https://en.wikipedia.org/wiki/Multi_Emulator_Super_System)
* [What-a-Mess from Wikipedia](https://en.wikipedia.org/wiki/What-a-Mess)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Image from [The What-a-Mess Collection](http://www.oocities.org/ebnsteve/muirwam.html), The [WaM books](https://en.wikipedia.org/wiki/What-a-Mess#Books_list), written by [Frank Muir](https://en.wikipedia.org/wiki/Frank_Muir) and illustrated by [Joseph Wright](https://en.wikipedia.org/wiki/Joseph_Wright_(illustrator)), tell the tale of an [Afghan hound](https://en.wikipedia.org/wiki/Afghan_Hound) whose real name is Prince [Amir of Kinjan](https://en.wikipedia.org/wiki/What-a-Mess)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [MessChess](http://www.geocities.ws/mridulm80/messchess.htm)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [MessChess](http://www.geocities.ws/mridulm80/messchess.htm)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Arasan in ACCA Rapid tourney (day 2)](http://www.talkchess.com/forum/viewtopic.php?t=21913) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 22, 2008

**[Up one Level](Engines "Engines")**







 
