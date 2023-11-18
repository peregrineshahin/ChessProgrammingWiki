---
title: Patzer
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Patzer**


**Patzer**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compatible chess engine by [Roland Pfister](Roland_Pfister "Roland Pfister"), later versions were [UCI](UCI "UCI") compliant, featuring a [parallel search](Parallel_Search "Parallel Search") and own [endgame bitbases](Endgame_Bitbases "Endgame Bitbases"), and were able to play [Chess960](Chess960 "Chess960") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Patzer is famous for solving the [Behting Study](Behting_Study "Behting Study") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> and a special [draw heuristic](Draw "Draw") for checking sequences. Patzer was available as [Young Talent](ChessBase#YoungTalents "ChessBase") by [ChessBase](ChessBase "ChessBase") running under the [Fritz6 GUI](Fritz#FritzGUI "Fritz") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



## Descriptions


<a id="cite-note-5" href="#cite-ref-5">[5]</a>



### 1997



```C++
Patzer uses state of the art methods as [minimal window](Null_Window "Null Window"), [hash tables](Hash_Table "Hash Table"), [history table](History_Heuristic "History Heuristic"), [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation") with [bitboards](Bitboards "Bitboards"), various [extensions](Extensions "Extensions"), [recursive nullmove](Null_Move_Pruning "Null Move Pruning") . It has small databases for [KPK](KPK "KPK") and [KPKP](index.php?title=KPKP&action=edit&redlink=1 "KPKP (page does not exist)") with blocked pawns to decide if it is a win or not. Additionally it can use [Thompson's](Ken_Thompson "Ken Thompson") Endgame CDs at [ply](Ply "Ply") 0.

```


```C++
At the moment I am working on including [endgame table base](Endgame_Tablebases "Endgame Tablebases") support. Patzer has a text interface a well as [GUIs](GUI "GUI") for [DOS](MS-DOS "MS-DOS"), [Windows](Windows "Windows"), OS/2 and [X11](index.php?title=X11&action=edit&redlink=1 "X11 (page does not exist)"). It can read/write [PGN](Portable_Game_Notation "Portable Game Notation") and [EPD](Extended_Position_Description "Extended Position Description") files. It has an Interface for [Autoplayer232](Auto232 "Auto232") and for [XBoard](XBoard "XBoard")/[WinBoard](WinBoard "WinBoard"). It has knowledge of the ["wrong" bishop](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn") in endgames. A [Hypertext](https://en.wikipedia.org/wiki/Hypertext) User Online Manual is available in German for [DOS](MS-DOS "MS-DOS"), [Windows](Windows "Windows"), OS/2 and [Unix](Unix "Unix"). 

```

### 1999



```C++
Patzer uses the standard [alpha-beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search") search, enhanced by [hashtables](Hash_Table "Hash Table") (4 retries replacement scheme), [recursive nullmove](Null_Move_Pruning "Null Move Pruning") ([R](Depth_Reduction_R "Depth Reduction R")=2) with verification if only one piece present, special [pruning](Pruning "Pruning") heuristic for [ALL-nodes](Node_Types#All-Nodes "Node Types"), various [extensions](Extensions "Extensions"). It also uses a special [material hash table](Material_Hash_Table "Material Hash Table") to adjust the [material](Material "Material") balance values for certain [endgames](Endgame "Endgame") where the "usual" values do not apply. It values [king safety](King_Safety "King Safety") and [passed pawns](Passed_Pawn "Passed Pawn") rather high (too high?). It is a [incremental](Incremental_Updates "Incremental Updates") [bitboard](Bitboards "Bitboards") program with [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") that are also used during [move generation](Move_Generation "Move Generation") and [sorting](Move_Ordering "Move Ordering"). 

```

## Photos


 [](http://www.quarkchess.de/csvn2001/body_index.html) 
Patzer team [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky") and [Roland Pfister](Roland_Pfister "Roland Pfister") at [ICT 2001](ICT_2001 "ICT 2001") <a id="cite-note-6" href="#cite-ref-6">[6]</a>



## See also


* [Woodpusher](Woodpusher "Woodpusher")


## Namesake


* [Patzer](index.php?title=Patzer_(K)&action=edit&redlink=1 "Patzer (K) (page does not exist)") by [Werner Koch](Werner_Koch "Werner Koch") and [Thomas Schäfer](index.php?title=Thomas_Sch%C3%A4fer&action=edit&redlink=1 "Thomas Schäfer (page does not exist)")


## Forum Posts


### 1998 ...


* [Yes, Patzer really seem to be quite something...](https://www.stmintz.com/ccc/index.php?id=20150) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), June 07, 1998
* [Diepeveen Attack !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30531&p=115980) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 11, 1999


### 2000 ...


* [Patzer](https://www.stmintz.com/ccc/index.php?id=165577) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer"), [CCC](CCC "CCC"), April 23, 2001
* [Re: 1 Hour CCR Test by IM Larry Kaufmann / Patzer 3.51](https://www.stmintz.com/ccc/index.php?id=169171) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), May 11, 2001 » [CCR One Hour Test](CCR_One_Hour_Test "CCR One Hour Test")
* [Goliath Light, Gromit, Patzer, SOS, etc. commercially sold](https://www.stmintz.com/ccc/index.php?id=186009) by [Theo van der Storm](Theo_van_der_Storm "Theo van der Storm"), [CCC](CCC "CCC"), August 28, 2001
* [Is there a Tournament book for Patzer?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35220&p=133316) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 05, 2001
* [Re: Position solved](https://www.stmintz.com/ccc/index.php?id=259020) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), October 14, 2002 » [Behting Study](Behting_Study "Behting Study")
* [Patzer 3.61 UCI vs 3.11 CB = 23 - 15](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=42137&p=160957) by Brice Boissel, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2003
* [Patzer\_299zt](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=44653&p=170186) by Telmo Escobar, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 18, 2003
* [Any programs besides Yace and Patzer that can use bitbase files](https://www.stmintz.com/ccc/index.php?id=370997) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 17, 2004 » [Endgame Bitbases](Endgame_Bitbases "Endgame Bitbases"), [Yace](Yace "Yace")


### 2010 ...


* [STS [1-10] Patzer 3.80](http://www.talkchess.com/forum/viewtopic.php?t=35320) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), July 06, 2010 » [Strategic Test Suite](Strategic_Test_Suite "Strategic Test Suite")


### 2020 ...


* [Patzer 3.80](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74394) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), July 06, 2020


## External Links


### Chess Engine


* [Patzer's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=19)
* [Patzer 3.80](http://web.archive.org/web/20090430124900/http://www.superchessengine.com/patzer.htm), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
* [Meet the Authors - PATZER, Roland Pfister](http://www.rebel.nl/authors.htm) hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
* [Patzer 3.80](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&eng=Patzer%203.80) in [CCRL 40/40](CCRL "CCRL")
* [Young Talents, Teil 2](http://scleinzell.schachvereine.de/p_spielprogramme/youngtal_b.shtml) by [Peter Schreiner](Peter_Schreiner "Peter Schreiner"), Mai 2000, hosted by [Schachclub Leinzell](http://scleinzell.schachvereine.de/home/news.shtml) (German)


### Misc


* [Patzer - Wiktionary](https://en.wiktionary.org/wiki/Patzer)


 [patzer - Wiktionary](https://en.wiktionary.org/wiki/patzer)
* [Glossary of chess - P, Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_chess#P)
* [Patzer Opening - Chess Opening Database](http://www.chessvideos.tv/chess-opening-database/search/Patzer-Opening)
* [Bobby Fischer - Wikiquote - Patzer sees a check, gives a check](https://en.wikiquote.org/wiki/Bobby_Fischer) <a id="cite-note-7" href="#cite-ref-7">[7]</a>


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Patzer 3.80](http://web.archive.org/web/20090430124900/http://www.superchessengine.com/patzer.htm), [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Meet the Authors - PATZER, Roland Pfister](http://www.rebel.nl/authors.htm) hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Position solved](https://www.stmintz.com/ccc/index.php?id=259020) by [Roland Pfister](Roland_Pfister "Roland Pfister"), [CCC](CCC "CCC"), October 14, 2002
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Support - ChessBase, May 28th, 2000](http://www.chessbase.com/support/support.asp?pid=100) (dead link)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Patzer's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=19)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [1st International CSVN-Tournament 2001](http://www.quarkchess.de/csvn2001/body_index.html) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [ICT 2001](ICT_2001 "ICT 2001")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) (**1969**). *[My 60 Memorable Games](https://en.wikipedia.org/wiki/My_60_Memorable_Games)*. [Simon & Schuster](https://en.wikipedia.org/wiki/Simon_%26_Schuster)

**[Up one Level](Engines "Engines")**







 
