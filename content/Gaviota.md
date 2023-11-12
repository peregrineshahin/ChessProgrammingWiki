---
title: Gaviota
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gaviota**

\[ Gaviota austral <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Gaviota**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compatible chess engine written by [FM](https://en.wikipedia.org/wiki/FIDE_titles#FIDE_Master_.28FM.29) [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") in the [C](C "C") programming language. When It was released in 2001, it was the first Argentinian engine available. Gaviota supports its [own endgame tablebases](Gaviota_Tablebases "Gaviota Tablebases"), [book](Opening_Book "Opening Book"), and can use several processors ([SMP](SMP "SMP")). It has the ability to [learn](Book_Learning "Book Learning") by remembering book lines and positions that were not good. Gaviota avoids them in following games. There are versions for [Linux](Linux "Linux"), [Android](Android "Android"), [Windows](Windows "Windows"), and [Mac OS](Mac_OS "Mac OS") (0.86) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The Gaviota team is completed by tester [Adam Hair](Adam_Hair "Adam Hair") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 Etymology](#etymology)
- [3 Tournament Play](#tournament-play)
- [4 Selected Games](#selected-games)
- [5 Forum Posts](#forum-posts)
  - [5.1 2000 ...](#2000-...)
  - [5.2 2005 ...](#2005-...)
  - [5.3 2010 ...](#2010-...)
- [6 External Links](#external-links)
  - [6.1 Chess Engine](#chess-engine)
  - [6.2 Misc](#misc-2)
- [7 References](#references)

## Features

based on Gaviota's change log until **v1.0** <a id="cite-note-5" href="#cite-ref-5">[5]</a> and [Forum Posts](Computer_Chess_Forums "Computer Chess Forums")

## Board Representation

- [Bitboards](Bitboards "Bitboards")
- [BitScan with De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Fill Algorithm](Dumb7Fill "Dumb7Fill") for [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## Search

- [Parallel Search](Parallel_Search "Parallel Search")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Fractional Plies](Depth#FractionalPlies "Depth")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table") (4 [Buckets](Transposition_Table#Bucket "Transposition Table"))
- [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [History Heuristic](History_Heuristic "History Heuristic")
- [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
- [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Futility Pruning](Futility_Pruning "Futility Pruning")
- [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
- [Razoring](Razoring "Razoring")
- [Leaf Forward Pruning](History_Leaf_Pruning "History Leaf Pruning")

## Evaluation

- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [King Safety](King_Safety "King Safety")
- [Outposts](Outposts "Outposts")
- [Mobility](Mobility "Mobility")

[Pawn Mobility](Mobility "Mobility")
[Trapped Rook](Trapped_Pieces "Trapped Pieces")

- [Automated Tuning](Automated_Tuning "Automated Tuning")

## Misc

- [Book Learning](Book_Learning "Book Learning")
- [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")

## Etymology

[Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") on the name of his program <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```C++
Gaviota means "[seagull](https://en.wikipedia.org/wiki/Seagull)", from the story of [Jonathan Livingston Seagull](https://en.wikipedia.org/wiki/Jonathan_Livingston_Seagull). The spirit of the engine reflects the free spirit of the fictional bird, of flying for fun and excitement, not for food. In Spanish, the book was translated to [Juan Salvador Gaviota](http://es.wikipedia.org/wiki/Juan_Salvador_Gaviota). In addition, my wife's nickname is Gaby, so it has double meaning. 

```

## Tournament Play

Gaviota played various [ACCA Americas' Computer Chess Championships](ACCA_Americas%27_Computer_Chess_Championship "ACCA Americas' Computer Chess Championship"), [CCT Tournaments](CCT_Tournaments "CCT Tournaments") and [ACCA World Computer Rapid Chess Championships](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship"), further the [IGWT 2013](IGWT_2013 "IGWT 2013") and multiple [TCEC](TCEC "TCEC") seasons.

## Selected Games

[WCRCC 2013](WCRCC_2013 "WCRCC 2013"), [EXchess](EXchess "EXchess") - Gaviota <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```

[Event "WCRCC 2013"]
[Site "Internet Chess Club"]
[Date "2013.07.20"]
[Round "-"]
[White "EXchess"]
[Black "Gaviota"]
[Result "0-1"]

1.d4 d5 2.Nf3 Nf6 3.g3 c6 4.c4 Bf5 5.Nbd2 e6 6.Bg2 Be7 7.O-O O-O 8.b3 h5 
9.Ng5 Nbd7 10.e4 dxe4 11.Ndxe4 Nxe4 12.Nxe4 Nf6 13.Nxf6+ Bxf6 14.Be3 h4 
15.g4 Bh7 16.Qd2 Qd7 17.g5 Be7 18.Qe2 Qd8 19.f4 Bf5 20.d5 exd5 21.cxd5 h3 
22.Bf3 c5 23.Qb5 Bd6 24.Rae1 Qc7 25.Qc4 Qa5 26.a4 a6 27.Rec1 Rac8 28.Qc3 
Qc7 29.Qd2 Rfe8 30.Be2 Qe7 31.Kf2 Bc7 32.Bc4 Ba5 33.Qe2 Qd7 34.Qf3 Bb4 
35.d6 b5 36.Bd5 c4 37.Kg3 cxb3 38.Rxc8 Rxc8 39.axb5 Rc2 40.Rg1 axb5 
41.Bxb3 Be1+ 42.Rxe1 Rg2+ 43.Qxg2 hxg2 44.Bf2 Qxd6 45.Kxg2 Qxf4 46.Re8+ 
Kh7 47.g6+ Kxg6 48.Re3 b4 49.Kg1 Be6 50.Bc2+ Kh6 51.Kg2 Qg4+ 52.Bg3 Bd5+ 
53.Kf2 f5 54.Ke1 b3 55.Bxb3 Qb4+ 56.Kf2 Bxb3 57.Be5 f4 58.Rh3+ Kg6 59.Rxb3 
Qxb3 60.Bxf4 Kf5 61.Bc1 Ke4 62.Bg5 Qf3+ 63.Kg1 Qe2 64.Be3 Kxe3 65.h3 Kf3 
66.h4 Qg2# 0-1

```

## Forum Posts

## 2000 ...

- [Hash table efficiency](https://www.stmintz.com/ccc/index.php?id=143022) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 05, 2000 » [Transposition Table](Transposition_Table "Transposition Table"), [Search Statistics](Search_Statistics "Search Statistics")
- [New Winboard Engine](https://www.stmintz.com/ccc/index.php?id=151026) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 20, 2001
- [Gaviota should work everywhere now](https://www.stmintz.com/ccc/index.php?id=151842) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 24, 2001
- [Gaviota - FM Miguel A. Ballicora - live at ICC in 1 hour](https://www.stmintz.com/ccc/index.php?id=219390) by [Peter Berger](Peter_Berger "Peter Berger"), [CCC](CCC "CCC"), March 24, 2002
- [Great article for people who wants to write a chess engine](https://www.stmintz.com/ccc/index.php?id=221364) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 03, 2002 <a id="cite-note-10" href="#cite-ref-10">[10]</a>
- [Gaviota 0.33 released (for Linux fans too)](https://www.stmintz.com/ccc/index.php?id=287694) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), March 03, 2003
- [Engine Gaviota + WB2UCI in Fritz7 don,t Work pondering](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43805) by Luis Andraschnik, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 15, 2003 » [Wb2UCI](Wb2UCI "Wb2UCI")

## 2005 ...

- [Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 01, 2009

[Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009 » [Automated Tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

- [A New Gaviota Release](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50508) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2009
- [Yet another bitboard attack generator](http://www.talkchess.com/forum/viewtopic.php?t=30356) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), October 28, 2009
- [Gaviota EGTBs, interface proposal for programmers](http://www.talkchess.com/forum/viewtopic.php?t=31065) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), December 13, 2009

## 2010 ...

- [Test tournament starts: Gaviota, Daydreamer, Greko, Atak](http://www.talkchess.com/forum/viewtopic.php?t=31606) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), January 10, 2010 » Gaviota, [Daydreamer](Daydreamer "Daydreamer"), [GreKo](GreKo "GreKo"), [Atak](Atak "Atak")
- [Gaviota tablebases, Probing Code Release (Finally)](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50784) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2010 » [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")
- [Gaviota and SMP](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50989) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2010
- [WCRCC 2010 - Gaviota games](http://www.talkchess.com/forum/viewtopic.php?t=35478) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), July 17, 2010 » [WCRCC 2010](WCRCC_2010 "WCRCC 2010")
- [Gaviota tablebases, probing code v4 (UPDATE)](http://www.talkchess.com/forum/viewtopic.php?t=38372) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), March 11, 2011
- [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410892&t=39407) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), June 20, 2011
- [New Gaviota 0.86 (Linux, Android, Windows, and now Mac!)](http://www.talkchess.com/forum/viewtopic.php?t=46977) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 23, 2013
- [Insane move](http://www.talkchess.com/forum/viewtopic.php?t=48702) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), July 20, 2013 » [WCRCC 2013](WCRCC_2013 "WCRCC 2013")
- [Gaviota v1.0 (Release)](http://www.talkchess.com/forum/viewtopic.php?t=51530) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), March 08, 2014
- [Gaviota 1.0 for Mac OS X (Release)](http://www.talkchess.com/forum/viewtopic.php?t=51869) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 05, 2014

## External Links

## Chess Engine

- [Gaviota Home](http://sites.google.com/site/gaviotachessengine/)
- [Endgame Tablebases - gaviota chess engine](http://sites.google.com/site/gaviotachessengine/Home/endgame-tablebases-1)

[Compression Schemes for Gaviota Tablebases](http://sites.google.com/site/gaviotachessengine/schemes)

- [Gaviota Chess Program](https://www.msu.edu/~ballicor/gav/) (old site)
- [Interview](http://www.playwitharena.com/?Interviews:Interview_with_Miguel_Ballicora%26nbsp%3B) with [Miguel Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") by [Michael Diosi](index.php?title=Michael_Diosi&action=edit&redlink=1 "Michael Diosi (page does not exist)"), [Free chess graphical user interface (GUI) Arena for chess engines](http://www.playwitharena.com/), December 2010
- [Interview with Miguel Ballicora | Chessdom](http://www.chessdom.com/interview-with-miguel-ballicora/), February 23, 2013 <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>
- [Gaviota](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Gaviota&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [The chess games of Gaviota](http://www.chessgames.com/perl/chessplayer?pid=125281) from [chessgames.com](http://www.chessgames.com/index.html)

## Misc

- [Gaviota from Wikipedia](https://en.wikipedia.org/wiki/Gaviota)
- [Gaviota (desambiguación) - Wikipedia.es](http://es.wikipedia.org/wiki/Gaviota_%28desambiguaci%C3%B3n%29) (Spanish)

[Laridae - Wikipedia.es](http://es.wikipedia.org/wiki/Laridae) (Spanish) [Gull](https://en.wikipedia.org/wiki/Gull)
[Gaviota (galardón) - Wikipedia.es](http://es.wikipedia.org/wiki/Gaviota_%28galard%C3%B3n%29) (Spanish) award of the [Viña del Mar International Song Festival](https://en.wikipedia.org/wiki/Vi%C3%B1a_del_Mar_International_Song_Festival)

- [Gaviota, California from Wikipedia](https://en.wikipedia.org/wiki/Gaviota,_California)
- [Gaviota State Park from Wikipedia](https://en.wikipedia.org/wiki/Gaviota_State_Park)
- [Gaviota Peak from Wikipedia](https://en.wikipedia.org/wiki/Gaviota_Peak)
- [Gaviota Tunnel from Wikipedia](https://en.wikipedia.org/wiki/Gaviota_Tunnel)
- [Isla de las Gaviotas, Montevideo - Wikipedia](https://en.wikipedia.org/wiki/Isla_de_las_Gaviotas,_Montevideo)
- [Isla de las Gaviotas (Argentina) - Wikipedia.es](http://es.wikipedia.org/wiki/Isla_de_las_Gaviotas_%28Argentina%29) (Spanish)
- [Clare Fischer](https://en.wikipedia.org/wiki/Clare_Fischer) - [Gaviota](http://www.wikifonia.org/node/12237), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Laridae from Wikipedia.es](http://es.wikipedia.org/wiki/Laridae)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Gull from Wikipedia](https://en.wikipedia.org/wiki/Gull)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New Gaviota 0.86 (Linux, Android, Windows, and now Mac!)](http://www.talkchess.com/forum/viewtopic.php?t=46977) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), January 23, 2013
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Gaviota v1.0 (engine) - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/releases/gaviotav10)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Change Log - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/change-log)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Acknowledgments - gaviota chess engine](https://sites.google.com/site/gaviotachessengine/Home/acknowledgments)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Yet another bitboard attack generator](http://www.talkchess.com/forum/viewtopic.php?t=30356) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), October 28, 2009
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410892&t=39407) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), June 20, 2011
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Insane move](http://www.talkchess.com/forum/viewtopic.php?t=48702) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), July 20, 2013
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Computer Chess and Search.* Encyclopedia of Artificial Intelligence (2nd ed.) (ed. S.C. Shapiro) pp. 224-241. John Wiley & Sons, Inc., New York, NY. ISBN 0-471-50305-3. [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/encyc.mac-1991.pdf)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [TCEC computer chess LIVE!](http://www.chessdom.com/tcec-computer-chess-live/)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [TCEC - Thoresen Chess Engines Competition | Facebook](https://www.facebook.com/tcec.chess)

**[Up one Level](Engines "Engines")**

