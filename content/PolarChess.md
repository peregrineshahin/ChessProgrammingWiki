---
title: PolarChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* PolarChess**



 [](http://www.flickr.com/photos/29528454@N04/5428134932) The case of the bi-polar chess queen <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**PolarChess**,  

a [WinBoard](WinBoard "WinBoard") compliant chess engine, written at [70° 4′ 24″ N](http://toolserver.org/~geohack/geohack.php?pagename=Vads%C3%B8&params=70_04_24_N_029_44_59_E_region:NO_type:city), 3° 30′ 40″ north the [Arctic Circle](https://en.wikipedia.org/wiki/Arctic_Circle) in [Vadsø](https://en.wikipedia.org/wiki/Vads%C3%B8) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Finnmark](https://en.wikipedia.org/wiki/Finnmark) [country](https://en.wikipedia.org/wiki/Counties_of_Norway), [Norway](https://en.wikipedia.org/wiki/Norway) by [Odd Gunnar Malin](Odd_Gunnar_Malin "Odd Gunnar Malin") in [C++](Cpp "Cpp"), first released in November 2001. PolarChess, version 1.2 as [open source](Category:Open_Source "Category:Open Source"), includes the PolarEngine package with [search](Search "Search") and [evaluation](Evaluation "Evaluation") decoupled from the [board representation](Board_Representation "Board Representation"). It has a [0x88](0x88 "0x88") board, and applies [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Checks](Check_Extensions "Check Extensions"), [pawn moves to the 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), and [mate threatening moves](Mate_Threat_Extensions "Mate Threat Extensions") are [extended](Extensions "Extensions"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic") help to [order moves](Move_Ordering "Move Ordering"). [Evaluation](Evaluation "Evaluation") counts [material](Material "Material") aware of the [bishop pair](Bishop_Pair "Bishop Pair") and trade bonuses for pieces if ahead and pawns if behind, and positionally considers [pawn structure](Pawn_Structure "Pawn Structure") utilizing a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), [passed pawns](Passed_Pawn "Passed Pawn"), [mobility](Mobility "Mobility"), [rook on open file](Rook_on_Open_File "Rook on Open File"), [bad bishop](Bad_Bishop "Bad Bishop"), and [pawn shield](King_Safety#PawnShield "King Safety") for [king safety](King_Safety "King Safety") to name the most important terms.


PolarChess played the [CCT4](CCT4 "CCT4") and [CCT5](CCT5 "CCT5") tournaments. 



### Contents


* [1 Selected Games](#selected-games)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc)
* [5 References](#references)






[CCT4](CCT4 "CCT4"), round 4, PolarChess - [Warlord](Warlord "Warlord") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.20"]
[Round "4"]
[White "PolarChess"]
[Black "Warlord Beta V1"]
[Result "1-0"]

1.e4 Nf6 2.e5 Ne4 3.d3 Nc5 4.d4 Ne6 5.d5 Nc5 6.Qd4 e6 7.d6 cxd6 8.exd6 Qb6 
9.Qc3 a5 10.Bf4 f6 11.Na3 e5 12.Nb5 Bxd6 13.Nxd6+ Qxd6 14.Be3 b6 15.Rd1 Qc6 
16.Bxc5 bxc5 17.Be2 Bb7 18.Bf3 e4 19.Be2 d5 20.Nh3 Qb6 21.Nf4 d4 22.Qh3 Nd7 
23.Ng6 Rg8 24.Qxh7 Qe6 25.b3 Nf8 26.Bb5+ Kf7 27.Qh5 Nxg6 28.Bc4 Qxc4 29.bxc4 
Rac8 30.Rb1 Ba8 31.Rb6 Rh8 32.Qf5 Rhe8 33.O-O Ne5 34.Ra6 Kg8 35.Rxa5 e3 
36.fxe3 dxe3 37.Re1 Rcd8 38.Qh5 g6 39.Qh4 Rd2 40.Rxe3 Red8 41.Rxc5 Rxg2+ 
42.Kf1 Rd1+ 43.Re1 Rxe1+ 44.Qxe1 Rxh2 45.Qb4 Rh1+ 46.Kf2 Rh2+ 47.Kg3 Rg2+ 
48.Kh3 Kf7 49.Qa3 Be4 50.Rxe5 fxe5 51.Qe3 Bb7 52.Qxe5 Rxc2 53.Qc7+ Kf6 54.Qxb7 
Rc3+ 55.Kg2 Rc2+ 56.Kf3 Rc3+ 57.Ke4 Rxc4+ 58.Kd3 Rh4 59.Qc6+ Kg7 60.Qc7+ Kh6 
61.Qe5 Rh3+ 62.Ke4 Rh4+ 63.Kf3 Ra4 64.Qh8+ Kg5 65.Qd8+ Kh6 66.Qf8+ Kh5 67.Qf7 
Ra3+ 68.Kf2 Ra4 69.Qd5+ Kh4 70.Qh1+ Kg4 71.Qd1+ 1-0

```

## See also


* [Amundsen](Amundsen "Amundsen")
* [Siberian Chess](Siberian_Chess "Siberian Chess")


## Forum Posts


* [PolarChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35161) by [Odd Gunnar Malin](Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 26, 2001
* [PolarChess](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35265) by [Odd Gunnar Malin](Odd_Gunnar_Malin "Odd Gunnar Malin"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 19, 2001


## External Links


### Chess Engine


* [Chess and Data](http://web.archive.org/web/20100922051419/http://home.online.no/~malin/sjakk/) - [WaybackMachine](https://en.wikipedia.org/wiki/Wayback_Machine)
* [PolarChess 1.3](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details+%28text%29&eng=PolarChess%201.3) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Polar (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Polar)


 [Pole and polar from Wikipedia](https://en.wikipedia.org/wiki/Pole_and_polar)
 [Polar coordinate system from Wikipedia](https://en.wikipedia.org/wiki/Polar_coordinate_system)
 [Polar set from Wikipedia](https://en.wikipedia.org/wiki/Polar_set)
 [Polar question from Wikipedia](https://en.wikipedia.org/wiki/Yes%E2%80%93no_question)
* [Polar circle from Wikipedia](https://en.wikipedia.org/wiki/Polar_circle)
* [Polaris](https://en.wikipedia.org/wiki/Polaris)
* [Polar Star (novel) from Wikipedia](https://en.wikipedia.org/wiki/Polar_Star_%28novel%29)
* Anne Paceo's Circles - Toundra, [Marseille](https://en.wikipedia.org/wiki/Marseille) [Jazz des Cinq Continents](http://www.telerama.fr/festivals-ete/2015/a-marseille-melody-gardot-en-diva-passionnee,129640.php), July 21, 2015 , [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Anne Paceo](https://fr.wikipedia.org/wiki/Anne_Paceo), [Leïla Martial](Category:Le%C3%AFla_Martial "Category:Leïla Martial"), [Christophe Panzani](https://fr.wikipedia.org/wiki/Christophe_Panzani), [Tony Paeleman](Category:Tony_Paeleman "Category:Tony Paeleman")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [THE CASE OF THE BI-POLAR CHESS QUEEN: A Short Story | Flickr - Fotosharing!](http://www.flickr.com/photos/29528454@N04/5428134932) by [Robert Huffstutter](http://www.flickr.com/photos/huffstutterrobertl/)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Vadsø, Norway - Sunrise, sunset, dawn and dusk times for the whole year - Gaisma](http://www.gaisma.com/en/location/vadso.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [CCT4 - PGN-Download](http://www.vrichey.de/cct4/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [PolarChess just beat Warlord](https://www.stmintz.com/ccc/index.php?id=208631) by [William H. Rogers](William_H._Rogers "William H. Rogers"), [CCC](CCC "CCC"), January 20, 2002

**[Up one Level](Engines "Engines")**







 
