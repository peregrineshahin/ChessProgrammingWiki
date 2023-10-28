---
title: Requiem
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Requiem**



 [](https://www.dorisneidl.net/illustration?lightbox=image_18ck) Requiem for Ernst Jandl <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Requiem**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard") protocol 2 compliant chess engine by [Severi Salminen](Severi_Salminen "Severi Salminen"), written in [C](C "C") with some [x86](X86 "X86") [assembly](Assembly "Assembly") routines, first released in December 2001 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
As [bitboard](Bitboards "Bitboards") engine, it uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to calculate [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), and otherwise applies [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [null move pruning](Null_Move_Pruning "Null Move Pruning"), [mate threat extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [futility pruning](Futility_Pruning "Futility Pruning"), and [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework without [aspiration windows](Aspiration_Windows "Aspiration Windows") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Requem has a simple [evaluation function](Evaluation "Evaluation") supported by a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), and has some sense of [pawn islands](Pawn_Islands "Pawn Islands"). It is not aware of [repetitions](Repetitions "Repetitions") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, 
and lacks a main [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. 



### Contents


* [1 Forum Posts](#forum-posts)
* [2 External Links](#external-links)
	+ [2.1 Chess Engine](#chess-engine)
	+ [2.2 Misc](#misc)
* [3 References](#references)






* [Requiem (a WinBoard compatible engine) RELEASED!](https://www.stmintz.com/ccc/index.php?id=201192) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 09, 2001
* [Requiem (a WinBoard compatible engine) RELEASED!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35261) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 09, 2001
* [To Severi Salminen about Requiem](https://www.stmintz.com/ccc/index.php?id=207641) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), January 16, 2002
* [Requiem v0.52 released](https://www.stmintz.com/ccc/index.php?id=212309) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), February 07, 2002
* [Requiem v0.53 released](https://www.stmintz.com/ccc/index.php?id=254431) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), September 26, 2002


## External Links


### Chess Engine


* [Homepage of Severi Salminen - Requiem](http://www.saunalahti.fi/~sevesalm/Requiem.php)
* [Index of /chess/engines/Norbert's collection/Requiem (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert's%20collection/Requiem%20(Compilation)/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Requiem 0.53](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Requiem+0.53) in [CCRL Blitz](CCRL "CCRL")
* [Requiem 0.53](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?match_length=20&each_game=1&print=Details&each_game=1&eng=Requiem%200.53#Requiem_0_53) in [KCEC](KCEC "KCEC")


### Misc


* [Requiem from Wikipedia](https://en.wikipedia.org/wiki/Requiem)
* [Music for the Requiem Mass - Wikipedia](https://en.wikipedia.org/wiki/Music_for_the_Requiem_Mass)
* [Requiem (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Requiem_%28disambiguation%29)
* [Requiem shark from Wikipedia](https://en.wikipedia.org/wiki/Requiem_shark)
* [Achim Zepezauer](Category:Achim_Zepezauer "Category:Achim Zepezauer") - Requiem, [Tallinn](https://en.wikipedia.org/wiki/Tallinn), [Estonia](https://en.wikipedia.org/wiki/Estonia), February 2016, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Doris Neidl](Category:Doris_Neidl "Category:Doris Neidl"), 2002, [Collage](https://www.dorisneidl.net/illustration?lightbox=image_18ck) to [Frederike Mayroecker's](https://en.wikipedia.org/wiki/Friederike_Mayr%C3%B6cker) book *[Requiem for Ernst Jandl](https://www.amazon.com/Requiem-Ernst-Jandl-German-List/dp/0857424750)*, [Ernst Jandl from Wikipedia](https://en.wikipedia.org/wiki/Ernst_Jandl) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Requiem (a WinBoard compatible engine) RELEASED!](https://www.stmintz.com/ccc/index.php?id=201192) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 09, 2001
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Requiem v0.52 released](https://www.stmintz.com/ccc/index.php?id=212309) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), February 07, 2002
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [To Severi Salminen about Requiem](https://www.stmintz.com/ccc/index.php?id=207641) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), January 16, 2002
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Homepage of Severi Salminen - Requiem](http://www.saunalahti.fi/~sevesalm/Requiem.php)

**[Up one level](Engines "Engines")**







 
