---
title: Jabba
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Jabba**



[ [Jabba the Hutt](https://en.wikipedia.org/wiki/Jabba_the_Hutt) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Jabba**, (JabbaChess, Jabba Chess)  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Richard Allbert](Richard_Allbert "Richard Allbert"), written in [C++](Cpp "Cpp"), able to run under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS"). 
Jabba's development started around 2009 as successor of Richard's former engine [Lime](Lime "Lime"). 
In 2012, Jabba was ported to [C#](C_sharp "C sharp") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 
Jabba 1.0 is able to play [Knightmate Chess](Knightmate_Chess "Knightmate Chess"). 



### Contents


* [1 Description](#description)
* [2 Tournament Play](#tournament-play)
* [3 Selected Games](#selected-games)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2009](#2009)
	+ [5.2 2010 ...](#2010-...)
* [6 External Links](#external-links)
	+ [6.1 Chess Engine](#chess-engine)
	+ [6.2 Misc](#misc)
* [7 References](#references)






Jabba uses a hybrid board representation of a [0x88](0x88 "0x88") mailbox and [bitboards](Bitboards "Bitboards") for pawns <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 
It applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework along with [null move pruning](Null_Move_Pruning "Null Move Pruning"). 
It [extends](Extensions "Extensions") [checks](Check_Extensions "Check Extensions"), [pawn moves to the 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), and transitions to [pawn endings](Pawn_Endgame "Pawn Endgame"). Jabba's [evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") and considers [material imbalances](Material "Material") based on material analyses using statistics, [mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure"), [king safety](King_Safety "King Safety") and various [piece terms](Evaluation_of_Pieces "Evaluation of Pieces").



## Tournament Play


Jabba played the [CPT 2010](CPT_2010 "CPT 2010") and [CPT 2011](CPT_2011 "CPT 2011") Chess Programmers Tournaments over the board, further the [WCRCC 2010](WCRCC_2010 "WCRCC 2010") and [WCRCC 2012](WCRCC_2012 "WCRCC 2012") ACCA World Computer Rapid Chess Championships, and the [CCT12](CCT12 "CCT12"), [CCT13](CCT13 "CCT13"), [CCT14](CCT14 "CCT14") and [CCT15](CCT15 "CCT15") Computer Chess Tournaments.



## Selected Games


[WCRCC 2012](WCRCC_2012 "WCRCC 2012"), round 8, [Parrot](Parrot "Parrot") - Jabba, which ends in a [Stalemate](Stalemate "Stalemate") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "WCRCC 2012"]
[Site "Internet Chess Club"]
[Date "2012.07.14"]
[Round "8"]
[White "Parrot"]
[Black "Jabba"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 
9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.d4 Bd6 13.Re2 Qc7 14.h3 Bf5 15.a4 
Rae8 16.axb5 axb5 17.Na3 Nf6 18.Be3 Ne4 19.Nc2 Rd8 20.Ne1 Rfe8 21.Nf3 Nf6 
22.Bc2 Bxc2 23.Qxc2 Nd5 24.b3 g6 25.Bg5 Rxe2 26.Qxe2 f6 27.Bd2 Qf7 28.c4 
bxc4 29.bxc4 Re8 30.Qd3 Ne7 31.Ra6 Qe6 32.h4 Qc8 33.c5 Bb8 34.g3 Nd5 35.Ra1 
Bc7 36.Kg2 Re6 37.Ra6 Qb7 38.Qa3 Qb5 39.Ra8+ Kg7 40.h5 gxh5 41.Qa7 Re7 
42.Qa1 Qd3 43.Qc1 Re2 44.Ra3 Qg6 45.Nh4 Qg4 46.Bh6+ Kg8 47.Qa1 Qe4+ 48.Rf3 
Qe8 49.Kf1 Rc2 50.Nf5 Qe2+ 51.Kg2 Ra2 52.Qh1 Qe8 53.Ne3 Qf7 54.Nxd5 Qxd5 
55.Qe1 Kf7 56.Qe3 Ra1 57.Bg5 Bd8 58.Qc3 Ra2 59.Qc1 Kg8 60.Bf4 Qxd4 61.Qe1 
Kf7 62.Qb1 Qd5 63.Qxh7+ Ke8 64.Qg6+ Kd7 65.Bd6 Ra4 66.Qc2 Re4 67.Qb1 h4 
68.Qb7+ Ke8 69.Qg7 hxg3 70.Kxg3 Re1 71.Qh8+ Kd7 72.Qh3+ Ke8 73.Re3+ Rxe3+ 
74.fxe3 f5 75.Qh8+ Kd7 76.Qg7+ Ke8 77.Qh7 Qe4 78.Qg8+ Kd7 79.Qf7+ Kc8 
80.Bf4 Bh4+ 81.Kxh4 Qe7+ 82.Qxe7 {Black stalemated} 1/2-1/2

```

## See also


* [Lime](Lime "Lime")
* [Knightmate Chess](Knightmate_Chess "Knightmate Chess")


## Forum Posts


### 2009


* [New Winboard & UCI Engine, Jabba 1.0](http://www.talkchess.com/forum/viewtopic.php?t=31341) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), December 29, 2009
* [Jabba 1.0 Released](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50681&p=192408) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2009


### 2010 ...


* [Jabba 1.1 For the Mac (!)](http://www.talkchess.com/forum/viewtopic.php?t=31804) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), January 18, 2010
* [Move ordering help](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=32611) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), February 14, 2010 » [Move Ordering](Move_Ordering "Move Ordering")
* [Jabba 1.0 Linux](http://www.talkchess.com/forum/viewtopic.php?t=32808) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), February 21, 2010
* [Jabba chess](http://www.talkchess.com/forum/viewtopic.php?t=42771) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), March 06, 2012
* [Jabba13032012](http://www.talkchess.com/forum/viewtopic.php?t=42857) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), March 13, 2012
* [Jabba's games ACCA](http://www.talkchess.com/forum/viewtopic.php?t=44430) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), July 14, 2012


## External Links


### Chess Engine


* [Jabba, the Winboard & UCI chess engine](http://jabbachess.blogspot.com/)
* [Jabba - UCI and Winboard Chess Engine](https://web.archive.org/web/20140519133907/http://www.rja-software.com/Jabba.php) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Index of /chess/engines/Jim Ablett/JABBA](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/JABBA/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
* [Jabba 1.0 32-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Jabba%201.0%2032-bit#Jabba_1_0_32-bit) in [CCRL 40/40](CCRL "CCRL")
* [Jabba 13032012](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Jabba%2013032012#Jabba_13032012) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Jabba (Disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Jabba)
* [Jabba the Hutt from Wikipedia](https://en.wikipedia.org/wiki/Jabba_the_Hutt)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Jabba the Hutt by [Toby Philpott](https://en.wikipedia.org/wiki/Toby_Philpott), crop from [Toby Philpott, Jabba the Hutt puppeteer, and John Coppinger, Jabba sculptor](https://commons.wikimedia.org/wiki/File:Philpott_coppinger.jpg), 2007, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [C# Performance](http://www.talkchess.com/forum/viewtopic.php?t=42186) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), January 27, 2012
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jabba13032012](http://www.talkchess.com/forum/viewtopic.php?t=42857) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), March 13, 2012
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [New Winboard & UCI Engine, Jabba 1.0](http://www.talkchess.com/forum/viewtopic.php?t=31341) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), December 29, 2009
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Jabba's games ACCA](http://www.talkchess.com/forum/viewtopic.php?t=44430&start=7) by [Richard Allbert](Richard_Allbert "Richard Allbert"), [CCC](CCC "CCC"), July 15, 2012

**[Up one level](Engines "Engines")**







 
