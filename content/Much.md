---
title: Much
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Much**


**Much**, (MUCH)  

the [Maastricht University](Maastricht_University "Maastricht University") Chess Program by primary authors [Roger Hünen](Roger_H%C3%BCnen "Roger Hünen"), [Harry Nefkens](Harry_Nefkens "Harry Nefkens"), [Tom Pronk](Tom_Pronk "Tom Pronk") and [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, represented and operated at the [WCCC 1989](WCCC_1989 "WCCC 1989") by [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") and [Harm Bakker](index.php?title=Harm_Bakker&action=edit&redlink=1 "Harm Bakker (page does not exist)"). 
Much was written in [C](C "C"), and run on a [Sun-4](Sun#4 "Sun") [workstation](https://en.wikipedia.org/wiki/Workstation).



## Description


based on [WCCC 1989](WCCC_1989 "WCCC 1989") booklet <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++
Much consists of several programs. The [user-interface](User_Interface "User Interface") program accepts a move from the operator and subsequently generates [evaluation tables](Piece-Square_Tables "Piece-Square Tables") for the [search program](Search "Search").  The user-interface program also handles [time control](Time_Management "Time Management"), the [opening library](Opening_Book "Opening Book"), and the [endgame library](Endgame_Tablebases "Endgame Tablebases"). The [search program](Search "Search") receives the [board position](Chess_Position "Chess Position") and [evaluation tables](Piece-Square_Tables "Piece-Square Tables") from the user-interface program. The evaluation tables are tuned with the opening played. Before each move they are [incrementally updated](Incremental_Updates "Incremental Updates") according to the board position (strategical evaluation of squares), but also bonus points are provided to undeveloped pieces, the [pair of Bishops](Bishop_Pair "Bishop Pair") in open positions ([middlegame](Middlegame "Middlegame")/[endgame](Endgame "Endgame")), the Color of the Pawns and Bishop on the board (endgame). Moreover, several [plans](Planning "Planning") are encouraged. The configuration belonging to the execution of a plan is supplied with bonus points such that every piece and pawn involved tries to reach the plan-ideal square. The plan as a whole, once started to be carried out, increases the bonus points for every piece/pawn to be played at each move. Much then searches until it is interrupted by the user-interface program. The search program, based on the [alpha-beta](Alpha-Beta "Alpha-Beta") algorithm and its refinements, uses [PVS-search](Principal_Variation_Search "Principal Variation Search"), [killer](Killer_Heuristic "Killer Heuristic") and [transposition tables](Transposition_Table "Transposition Table"). [Move generation](Move_Generation "Move Generation") is done incrementally. Much uses specialized sub-programs to handle the KBBK, [KBNK](KBNK_Endgame "KBNK Endgame"), KBPK and KNPK endgames. These programs use a goal-directed search.

```

## See also


* [Dutch](Dutch "Dutch")


## External Links


* [Much's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=355)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Much's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=355)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Kings Move - Welcome to the 1989 AGT World Computer Chess Championship.](https://www.computerhistory.org/chess/doc-434fea055cbb3/) Edmonton, Alberta, Canada, Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), hosted by[The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")

**[Up one level](Engines "Engines")**







 
