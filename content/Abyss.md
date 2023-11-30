---
title: Abyss
---

**[Home](Home "Home") _ [Engines](Engines "Engines") _ Abyss**

a [Chinese Chess](Chinese_Chess "Chinese Chess") program by [Chun Ye](Chun_Ye "Chun Ye") and [Tony Marsland](Tony_Marsland "Tony Marsland"), written in [C](C "C") under [Unix](Unix "Unix") aka [SunOS](https://en.wikipedia.org/wiki/SunOS). A [X Window](https://en.wikipedia.org/wiki/X_Window_System) [GUI](GUI "GUI") was written in [C++](Cpp "Cpp") by [Haiying Wang](index.php?title=Haiying_Wang&action=edit&redlink=1 "Haiying Wang (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. The program was subject of Chun Ye's 1992 master thesis at [University of Alberta](University_of_Alberta "University of Alberta") <a id="cite-note-3" href="#cite-ref-3">[3]</a> on the topic of [selectivity](Selectivity "Selectivity") and [extension heuristics](Extensions "Extensions") in the domain of Chinese Chess. Not only Ye's advisor, Tony Marsland, contributed to the development of the program, but also [Don Beal](Don_Beal "Don Beal") - at that time visiting professor at University of Alberta - in particular concerning [null move quiescence search](Null_Move_Pruning#NMQS "Null Move Pruning").

## Description

The framework of Abyss <a id="cite-note-4" href="#cite-ref-4">[4]</a> was based on the Western experimental Chess program [Parabelle](Parabelle "Parabelle") by [Fred Popowich](Fred_Popowich "Fred Popowich") and Tony Marsland <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## [Move Generation](Move_Generation "Move Generation")

Abyss' board is [represented](Chinese_Chess_Board_Representation "Chinese Chess Board Representation") as [Mailbox](Mailbox "Mailbox") - a one-dimensional [array](Array "Array") of 90 computer words, indexed by 0 .. 89. Pieces are encoded by ±1 for red and black pawns until ±7 for red and black kings, empty squares are represented by zero. To detect the edges of the board and [palace](Chinese_Chess#Palace "Chinese Chess") during move generation, board arrays of pre-computed 12-bit [direction](Direction "Direction") masks consisting of four groups for each orthogonal direction of 3 bits each are utilized. Only the empty intersection of the move direction with the mask of the [target square](Target_Square "Target Square") indicates target on board or inside palace, followed by piece specific tests to generate [pseudo legal moves](Pseudo-Legal_Move "Pseudo-Legal Move") or to continue a direction loop for rook or [cannon](Chinese_Chess#Cannon "Chinese Chess"). Detection of strictly [legal moves](Legal_Move "Legal Move"), i.e. it does not expose the own king in check, or does not oppose both kings on the same file with no pieces intervening, is delayed until the move is actually made for efficiency reasons - since not all generated pseudo legal moves are examined.

## [Search](Search "Search")

The search procedure of Abyss was subject of Chun Ye's thesis concerning [selectivity](Selectivity "Selectivity"), in particular [extensions](Extensions "Extensions") which are combined in various experiments, and further elaborated in two additional papers along with Tony Marsland <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Abyss already featured [recursive null move pruning](Null_Move_Pruning "Null Move Pruning") with [depth reduction](Depth_Reduction_R "Depth Reduction R") of 1 <a id="cite-note-8" href="#cite-ref-8">[8]</a>, and further [Don Beal's](Don_Beal "Don Beal") [null move quiescence search](Null_Move_Pruning#NMQS "Null Move Pruning") <a id="cite-note-9" href="#cite-ref-9">[9]</a>. A piece evading move extension was motivated by threat detection concerning the complicated [repetition](Repetitions "Repetitions") rules of Chinese Chess.

### Basics

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")

[Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")

- [Refutation Table](Refutation_Table "Refutation Table")

### [Move Ordering](Move_Ordering "Move Ordering")

- [Hash Move](Hash_Move "Hash Move")
- [Refutation Move](Refutation_Move "Refutation Move")
- [MVV/LVA](MVV-LVA "MVV-LVA")
- [History Heuristic](History_Heuristic "History Heuristic")

### [Selectivity](Selectivity "Selectivity")

- [Extensions](Extensions "Extensions")

[Check Evasion Extensions](Check_Extensions "Check Extensions")
[Recapture Extensions](Recapture_Extensions "Recapture Extensions")
[King Threats](Mate_Threat_Extensions "Mate Threat Extensions")
[One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
[Singular Extensions](Singular_Extensions "Singular Extensions")

- [Pruning](Pruning "Pruning")

## [Recursive Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with [R](Depth_Reduction_R "Depth Reduction R") = 1 [Don Beal's Null Move Quiescence Search](Null_Move_Pruning#NMQS "Null Move Pruning") [Futility Pruning](Futility_Pruning "Futility Pruning") [Quiescence Search](Quiescence_Search "Quiescence Search") [Evaluation](Evaluation "Evaluation")

- [Material Balance](Material "Material") with [Point Values](Point_Value "Point Value")
<table class="wikitable" style="text-align: center;">

<tbody><tr>
<th> Piece
</th>
<th> Opening
</th>
<th> Endgame
</th></tr>
<tr>
<td style="text-align: left;"> <a href="/Chinese_Chess#King" title="Chinese Chess">King</a>
</td>
<td colspan="2"> 7000
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Rook" title="Chinese Chess">Rook</a>
</td>
<td colspan="2"> 1800
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Cannon" title="Chinese Chess">Cannon</a>
</td>
<td style="text-align:right;"> 900
</td>
<td style="text-align:right;"> 800
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Horse" title="Chinese Chess">Horse</a>
</td>
<td style="text-align:right;"> 800
</td>
<td style="text-align:right;"> 900
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Elephant" title="Chinese Chess">Elephant</a>
</td>
<td colspan="2"> 300
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Advisor" title="Chinese Chess">Advisor</a>
</td>
<td colspan="2"> 300
</td></tr>
<tr>
<td style="text-align: left;">  <a href="/Chinese_Chess#Pawn" title="Chinese Chess">Pawn</a>
</td>
<td colspan="2"> 100
</td></tr></tbody></table>

- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Square Control](Square_Control "Square Control")
- [King Safety](King_Safety "King Safety")

## [Attacking King Zone](King_Safety#Attacking "King Safety") [Penalty for King](King_Safety#Patterns "King Safety") on [rank](Ranks "Ranks") or [file](Files "Files") of opponent's [Cannon](Chinese_Chess#Cannon "Chinese Chess") Misc

- [Opening Book](Opening_Book "Opening Book")

## See also

- [Parabelle](Parabelle "Parabelle")

## Publications

- [Chun Ye](Chun_Ye "Chun Ye") (**1992**). _Experiments in Selective Search Extensions_. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). _Experiments in Forward Pruning with Limited Extensions._ [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/Experiments-FP-YeMars-1992.pdf)
- [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). _Selective Extensions in Game-Tree Search._

## External Links

## Engine

- [Abyss' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=252)

## Misc

- [abyss - Wiktionary](https://en.wiktionary.org/wiki/abyss)
- [Abyss from Wikipedia](https://en.wikipedia.org/wiki/Abyss)
- [Abyssal zone from Wikipedia](https://en.wikipedia.org/wiki/Abyssal_zone)
- [Abyssal plain from Wikipedia](https://en.wikipedia.org/wiki/Abyssal_plain)
- [Abyss (comics) from Wikipedia](<https://en.wikipedia.org/wiki/Abyss_(comics)>)
- [Abyss (religion) from Wikipedia](<https://en.wikipedia.org/wiki/Abyss_(religion)>)
- [Abyss (roller coaster) from Wikipedia](<https://en.wikipedia.org/wiki/Abyss_(roller_coaster)>)
- [Abyss (Thelema) from Wikipedia](<https://en.wikipedia.org/wiki/Abyss_(Thelema)>)
- [Abyssinia from Wikipedia](https://en.wikipedia.org/wiki/Abyssinia)
- [In the Abyss - Wikipedia](https://en.wikipedia.org/wiki/In_the_Abyss)
- [Abyss Odyssey - Wikipedia](https://en.wikipedia.org/wiki/Abyss_Odyssey)
- [Tales of the Abyss - Wikipedia](https://en.wikipedia.org/wiki/Tales_of_the_Abyss)
- [Slayer](Category:Slayer "Category:Slayer") - [Seasons in the Abyss](https://en.wikipedia.org/wiki/Seasons_in_the_Abyss), [Wacken](https://en.wikipedia.org/wiki/Wacken_Open_Air) [2014](https://en.wikipedia.org/wiki/Wacken_Open_Air#2014), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Lysefjord](https://en.wikipedia.org/wiki/Lysefjord), [Norway](https://en.wikipedia.org/wiki/Norway)- a man standing on [Preikestolen](https://en.wikipedia.org/wiki/Preikestolen) at the edge of the Abyss, [Image](https://commons.wikimedia.org/wiki/File:Lysefjorden_-_Man_standing_on_Preikestolen.JPG) by [Mercy](https://commons.wikimedia.org/wiki/User:Mercy), August 2008, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Haiying Wang](index.php?title=Haiying_Wang&action=edit&redlink=1 "Haiying Wang (page does not exist)") (**1994**). _[An application-oriented user interface model and development system](https://era.library.ualberta.ca/files/2227mr67d)_. Ph.D. thesis, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/files/2227mr67d/NN11407.pdf), see 6.2 Chinese Chess Program pp. 101.
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Chun Ye](Chun_Ye "Chun Ye") (**1992**). _Experiments in Selective Search Extensions_. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> Description is based on [Chun Ye](Chun_Ye "Chun Ye") (**1992**). _Experiments in Selective Search Extensions_. M.Sc. thesis, Department of Computing Science, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://era.library.ualberta.ca/public/datastream/get/uuid:e4fbf48d-7603-490f-85cc-5497bbecf5a8/DS1)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Fred Popowich](Fred_Popowich "Fred Popowich"), [Tony Marsland](Tony_Marsland "Tony Marsland"). (**1983**) _Parabelle: Experience with a Parallel Chess Program._ Technical Report 83-7. Computing Science Department, [University of Alberta](University_of_Alberta "University of Alberta"), [pdf](https://webdocs.cs.ualberta.ca/~tony/TechnicalReports/TR83-7.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Chun Ye](Chun_Ye "Chun Ye"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). _Experiments in Forward Pruning with Limited Extensions._ [ICCA Journal, Vol. 15, No. 2](ICGA_Journal#15_2 "ICGA Journal"), [pdf](http://webdocs.cs.ualberta.ca/~tony/RecentPapers/Experiments-FP-YeMars-1992.pdf)
7. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Gordon Goetsch](Gordon_Goetsch "Gordon Goetsch"), [Murray Campbell](Murray_Campbell "Murray Campbell") (**1990**). _[Experiments with the Null-Move Heuristic](https://link.springer.com/chapter/10.1007/978-1-4613-9080-0_9)_. [Computers, Chess, and Cognition](Computers,_Chess,_and_Cognition "Computers, Chess, and Cognition"), pp. 159-168
8. _Experiments with the Null Move_. [Advances in Computer Chess 5](Advances_in_Computer_Chess_5 "Advances in Computer Chess 5"), A revised version is published (**1990**) under the title _A Generalized Quiescence Search Algorithm_. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1, pp. 85-98. ISSN 0004-3702.
9. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Abyss' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=252)

**[Up one Level](Chinese_Chess "Chinese Chess")**
