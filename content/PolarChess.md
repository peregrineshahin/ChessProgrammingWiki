---
title: PolarChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* PolarChess**



 [](http://www.flickr.com/photos/29528454@N04/5428134932) The case of the bi-polar chess queen <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**PolarChess**,  

a [WinBoard](WinBoard "WinBoard") compliant chess engine, written at [70° 4′ 24″ N](http://toolserver.org/~geohack/geohack.php?pagename=Vads%C3%B8&params=70_04_24_N_029_44_59_E_region:NO_type:city), 3° 30′ 40″ north the [Arctic Circle](https://en.wikipedia.org/wiki/Arctic_Circle) in [Vadsø](https://en.wikipedia.org/wiki/Vads%C3%B8) <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [Finnmark](https://en.wikipedia.org/wiki/Finnmark) [country](https://en.wikipedia.org/wiki/Counties_of_Norway), [Norway](https://en.wikipedia.org/wiki/Norway) by [Odd Gunnar Malin](Odd_Gunnar_Malin "Odd Gunnar Malin") in [C++](Cpp "Cpp"), first released in November 2001. PolarChess, version 1.2 as [open source](Category:Open_Source "Category:Open Source"), includes the PolarEngine package with [search](Search "Search") and [evaluation](Evaluation "Evaluation") decoupled from the [board representation](Board_Representation "Board Representation"). It has a [0x88](0x88 "0x88") board, and applies [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") and [null move pruning](Null_Move_Pruning "Null Move Pruning") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows"). [Checks](Check_Extensions "Check Extensions"), [pawn moves to the 7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), and [mate threatening moves](Mate_Threat_Extensions "Mate Threat Extensions") are [extended](Extensions "Extensions"), [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic") help to [order moves](Move_Ordering "Move Ordering"). [Evaluation](Evaluation "Evaluation") counts [material](Material "Material") aware of the [bishop pair](Bishop_Pair "Bishop Pair") and trade bonuses for pieces if ahead and pawns if behind, and positionally considers [pawn structure](Pawn_Structure "Pawn Structure") utilizing a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), [passed pawns](Passed_Pawn "Passed Pawn"), [mobility](Mobility "Mobility"), [rook on open file](Rook_on_Open_File "Rook on Open File"), [bad bishop](Bad_Bishop "Bad Bishop"), and [pawn shield](King_Safety#PawnShield "King Safety") for [king safety](King_Safety "King Safety") to name the most important terms.


PolarChess played the [CCT4](CCT4 "CCT4") and [CCT5](CCT5 "CCT5") tournaments. 



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







 
