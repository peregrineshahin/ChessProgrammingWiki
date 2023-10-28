---
title: Alarm
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Alarm**

\[ Flashing alarm icon <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Alarm**, (Deamon)

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Benny Antonsson](Benny_Antonsson "Benny Antonsson") and [Erik Robertsson](Erik_Robertsson "Erik Robertsson"), written in [C++](Cpp "Cpp"). Alarm, the Diabolic Chess Engine <a id="cite-note-2" href="#cite-ref-2">[2]</a>, was first released in July 2003 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and was first mentioned in 2001 formerly called **Deamon** <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Alarm played four [CCT Tournaments](CCT_Tournaments "CCT Tournaments") from 2003 to 2006, the [CCT5](CCT5 "CCT5"), [CCT6](CCT6 "CCT6"), [CCT7](CCT7 "CCT7") and the [CCT8](CCT8 "CCT8").

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc-2)
- [5 References](#references)

## Features

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Board Representation](Board_Representation "Board Representation")

- [8x8 Board](8x8_Board "8x8 Board")
- [Bitboards](Bitboards "Bitboards")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [NegaScout](NegaScout "NegaScout")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
  - [Check Extensions](Check_Extensions "Check Extensions")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Weak Pawns](Weak_Pawns "Weak Pawns")
    - [Backward Pawn](Backward_Pawn "Backward Pawn")
    - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
    - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
  - [Pawn Center](Pawn_Center "Pawn Center")
- [King Safety](King_Safety "King Safety")
- [Outposts](Outposts "Outposts")
- [Bishop Fianchetto](Fianchetto "Fianchetto")
- [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
- [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
- [Connectivity](Connectivity "Connectivity")
- and more ...

## Misc

- [Opening Book](Opening_Book "Opening Book") from [PGN](Portable_Game_Notation "Portable Game Notation")-file

## See also

- [Embracer](Embracer "Embracer")
- [StAndersen](StAndersen "StAndersen")

## Forum Posts

- [Loggo for Deamon](https://www.stmintz.com/ccc/index.php?id=199383) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), November 28, 2001
- [St.Andersen vs. Deamon 0.87A](https://www.stmintz.com/ccc/index.php?id=199856) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), November 30, 2001  » [StAndersen](StAndersen "StAndersen")
- [Another Nordic seems to grow (especially to Odd Gunnar)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=35199) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 01, 2001
- [Swedish programs](https://www.stmintz.com/ccc/index.php?id=200414) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), December 04, 2001
- [Winboard engine Alarm is released](https://www.stmintz.com/ccc/index.php?id=306680) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), July 16, 2003
- [Winboard engine Alarm is released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43375) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 16, 2003
- [Updated engine: Alarm 0.92.4](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43686) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 05, 2003
- [Testposition of Matador-Alarm CCT6](https://www.stmintz.com/ccc/index.php?id=346731) by [Stefan Knappe](Stefan_Knappe "Stefan Knappe"), [CCC](CCC "CCC"), February 03, 2004 » [CCT6](CCT6 "CCT6")
- [New version of Alarm](https://www.stmintz.com/ccc/index.php?id=364794) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), May 12, 2004

## External Links

## Chess Engine

- [Alarm - WinBoard Engine](http://web.archive.org/web/20020623093524/http://www.codenet.se:80/Alarm/) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))

[Alarm - Technical](http://web.archive.org/web/20020618151719fw_/http://www.codenet.se:80/alarm/technical.htm) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
[Alarm/Deamon - Revision log](http://web.archive.org/web/20020623034338fw_/http://www.codenet.se:80/alarm/revision.txt) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))

- [Computer-Chess Wiki - Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list)
- [Alarm 0.93.1](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Alarm%200.93.1) in [CCRL 40/2](CCRL "CCRL")
- [Alarm 0.93.1](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Alarm%200.93.1) in [KCEC](KCEC "KCEC")

## Misc

- [alarm - Wiktionary](https://en.wiktionary.org/wiki/alarm)
- [Alarm - Wiktionary](https://en.wiktionary.org/wiki/Alarm)
- [alarm - Wiktionary](https://sv.wiktionary.org/wiki/alarm) (Swedish)
- [Alarm - Wiktionary](https://sv.wiktionary.org/wiki/Alarm) (Swedish)
- [Daemon (computing) from Wikipedia](<https://en.wikipedia.org/wiki/Daemon_(computing)>)
- [Alarm (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Alarm_%28disambiguation%29)
- [Alarm Pressure](http://alarmpressure.com/) - Шелдон Купер, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Flashing alarm icon](https://commons.wikimedia.org/wiki/File:Alarm.gif), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Alarm - WinBoard Engine](http://web.archive.org/web/20020623093524/http://www.codenet.se:80/Alarm/) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Winboard engine Alarm is released](https://www.stmintz.com/ccc/index.php?id=306680) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), July 16, 2003
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Swedish programs](https://www.stmintz.com/ccc/index.php?id=200414) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), December 04, 2001
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Features based on [Alarm - Technical](http://web.archive.org/web/20020618151719fw_/http://www.codenet.se:80/alarm/technical.htm) and [Alarm/Deamon - Revision log](http://web.archive.org/web/20020623034338fw_/http://www.codenet.se:80/alarm/revision.txt) ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))

**[Up one Level](Engines "Engines")**

