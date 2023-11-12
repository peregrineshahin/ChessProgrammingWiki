---
title: Natwarlal
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Natwarlal**



 [](File:Natwarlal.jpg) Natwarlal <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Natwarlal**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), written in [C++](Cpp "Cpp") and released under the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"). Natwarlal played the [CCT9](CCT9 "CCT9") with respectable 4/7. 
The name of the engine was inspired by [Mithilesh Kumar Srivastava](https://en.wikipedia.org/wiki/Natwarlal), better known as Natwarlal, a [Indian](https://en.wikipedia.org/wiki/India) [con man](https://en.wikipedia.org/wiki/Confidence_trick) <a id="cite-note-2" href="#cite-ref-2">[2]</a> known for having repeatedly "sold" the [Taj Mahal](https://en.wikipedia.org/wiki/Taj_Mahal), the [Red Fort](https://en.wikipedia.org/wiki/Red_Fort), and the [Rashtrapati Bhavan](https://en.wikipedia.org/wiki/Rashtrapati_Bhavan) and also the [Parliament House of India](https://en.wikipedia.org/wiki/Sansad_Bhavan) along with its 545 sitting members. He was a living-legend in his lifetime and a legend even after his death <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Features


<a id="cite-note-6" href="#cite-ref-6">[6]</a>



### [Board Representation](Board_Representation "Board Representation")


* [0x88](0x88 "0x88")
* [Piece-Lists](Piece-Lists "Piece-Lists")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [NegaScout](NegaScout "NegaScout")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Mate Killers](Mate_Killers "Mate Killers")
* [Selectivity](Selectivity "Selectivity")
	+ [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions")
	+ [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
	+ [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
	+ [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Rook on 7th Rank](Rook_on_Seventh "Rook on Seventh")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Castling Rights](Castling_Rights "Castling Rights")
	+ [Pawn Shield](King_Safety#PawnShield "King Safety")
	+ [King Piece Tropism](King_Safety#KingTropism "King Safety")
	+ [King](King "King") close to [open](Open_File "Open File") or [half-open files](Half-open_File "Half-open File")


### Misc


* [Opening Book](Opening_Book "Opening Book")
* [Perft](Perft "Perft")
* [Pondering](Pondering "Pondering")


## Selected Games


[CCT9](CCT9 "CCT9"), Natwarlal - [Berta](Berta "Berta")




```

[Event "CCT9"]
[Site "Internet Chess Club"]
[Date "2007.02.18"]
[Round "?"]
[White "Natwarlal"]
[Black "Berta"]
[Result "1-0"]
 
1.e4 e6 2.Nf3 d5 3.Nc3 Nf6 4.exd5 exd5 5.d4 c6 6.Bd3 Be7 7.O-O O-O 8.Re1 Bg4 
9.h3 Bh5 10.Bf4 Bd6 11.Be5 Bb4 12.Bf5 Nfd7 13.Bf4 Bxc3 14.bxc3 Nb6 15.Rb1 N8d7 
16.Qd3 Nf6 17.Bg5 h6 18.Bh4 g6 19.Ne5 Qd6 20.a4 Rae8 21.Qg3 Re7 22.Re3 Rd8 
23.Rb4 Kf8 24.a5 gxf5 25.axb6 a5 26.Ra4 Ne4 27.Qf4 Ng5 28.Bxg5 hxg5 29.Qxg5 f6 
30.Qxh5 fxe5 31.Rg3 Rf7 32.Rg6 Qxg6 33.Qxg6 exd4 34.cxd4 Ra8 35.f4 Rg7 36.Qxf5 
Kg8 37.Qe6 Kh7 38.f5 Rf8 39.Rxa5 Rfg8 40.g4 Rf8 41.f6 Rgf7 42.g5 Kg6 43.Ra3 c5 
44.Rf3 Kh7 45.g6 Kh8 46.gxf7 Ra8 47.Qxd5 Ra1 48.Kf2 Rf1 49.Kxf1 cxd4 50.Qh5#

```

## Forum Posts


### 2004


* [New chess engine](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46915) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 16, 2004
* [Natwarlal V0.03](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47710) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 29, 2004
* [Just released Natwarlal v0.04](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48063) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 01, 2004
* [Natwarlal v0.05](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48169) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2004
* [With big hash Natwarlal v0.06 searches pretty fast...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=49036) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2004
* [Natwarlal V0.07](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=49082) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 26, 2004
* [Natwarlal V0.08](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=229) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 10, 2004
* [Natwarlal v0.09](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=443) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 31, 2004


### 2005


* [Natwarlal 0.06....a tactical monster!](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1552) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 04, 2005
* [Natwarlal v0.10](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1811) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 28, 2005
* [Natwarlal v0.11](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1884) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 06, 2005
* [Natwarlal Remarks](https://www.stmintz.com/ccc/index.php?id=416869) by Marc D, [CCC](CCC "CCC"), March 15, 2005
* [Re: New Engine classifications](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2178&p=10172#p10172) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2005
* [Re: copying evaluation of other programs](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2456&p=11816#p11736) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 12, 2005
* [Re: copying evaluation of other programs](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2456&p=11816#p11816) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 13, 2005
* [Re: how much open source code did you read and understand?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2877&p=14199#p14199) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 30, 2005
* [Re: Piece-list representation](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3110&p=15091#p15091) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2005


## External Links


### Chess Engine


* [Pallav's Domain - Natwarlal](http://www.oocities.org/pallavnawani/chess-natwarlal.html)
* [Index of /chess/engines/Jim Ablett/NATWARLAL](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/NATWARLAL/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
* [Natwarlal 0.14](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Natwarlal%200.14#Natwarlal_0_14) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [Natwarlal from Wikipedia](https://en.wikipedia.org/wiki/Natwarlal)
* [Mr. Natwarlal from Wikipedia](https://en.wikipedia.org/wiki/Mr._Natwarlal)
* [Raja Natwarlal from Wikipedia](https://en.wikipedia.org/wiki/Raja_Natwarlal)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [India's Biggest Conman Natwarlal | Biography Of Natwarlal](https://www.scoopwhoop.com/Natwarlal-Indias-Greatest-Conman-Who-Sold-Taj-Mahal/) by [Shabdita Pareek](https://www.scoopwhoop.com/author/shabdita-pareek/?ref=page_article), [ScoopWhoop](https://en.wikipedia.org/wiki/ScoopWhoop)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: New Engine classifications](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2178&p=10172#p10172) by [Pallav Nawani](Pallav_Nawani "Pallav Nawani"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2005
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Natwarlal from Wikipedia](https://en.wikipedia.org/wiki/Natwarlal)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> readme.txt
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Initial version of Natwarlal was greatly influenced by [MSCP](MSCP "MSCP")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Pallav's Domain - Natwarlal](http://www.oocities.org/pallavnawani/chess-natwarlal.html) and source files

**[Up one Level](Engines "Engines")**







 
