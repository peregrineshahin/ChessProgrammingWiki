---
title: Cinnamon
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Cinnamon**

\[ Cinnamon <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Cinnamon**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), written in [C++11](Cpp "Cpp"), published under [GPL Version 3](Free_Software_Foundation#GPL "Free Software Foundation").
Cinnamon was first released in February 2013 <a id="cite-note-2" href="#cite-ref-2">[2]</a> under that name, while former versions of the engine were called [Butterfly](index.php?title=Butterfly&action=edit&redlink=1 "Butterfly (page does not exist)").
It targets multiple hardware platforms and [operating systems](https://en.wikipedia.org/wiki/Operating_system) such as [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Android](Android "Android"),
also available for the [Raspberry Pi](Raspberry_Pi "Raspberry Pi"), and further provides a [JavaScript](JavaScript "JavaScript") library to play with [chessboard.js](index.php?title=Chessboard.js&action=edit&redlink=1 "Chessboard.js (page does not exist)") or any js [GUI](GUI "GUI").

## Sliding Piece Attacks

Cinnamon **1.2** applied a kind of [classical approach](Classical_Approach "Classical Approach") to generate ray-wise [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"), [captures](Captures "Captures") and [quiet moves](Quiet_Moves "Quiet Moves").
Cinnamon **2.0** already used line-wise [occupancy lookups](Sliding_Piece_Attacks#By_Occupancy_Lookup "Sliding Piece Attacks").
Four pre-calculated attack arrays containing attack bitboards on [ranks](Ranks "Ranks"), [files](Files "Files"), [diagonals](Diagonals "Diagonals") and [anti-diagonals](Anti-Diagonals "Anti-Diagonals")
were indexed by the square of the sliding piece, and the associated [occupancy](Occupancy "Occupancy") index of that line, determining the blockers affecting the attack set.
Rather than to get the occupancy index from [incremental updated](Incremental_Updates "Incremental Updates") [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") for each of the four line kinds,
Cinnamon extracts line occupancies into a dense index range using [multiplication](Occupancy_of_any_Line#Using_Multiplication "Occupancy of any Line") and shift right,
as mentioned in [diagonals to rank](Flipping_Mirroring_and_Rotating#DiagonalstoRanks "Flipping Mirroring and Rotating") or [flip about the diagonal](Flipping_Mirroring_and_Rotating#FlipAbouttheDiagonal "Flipping Mirroring and Rotating").
The resulting 8-bit occupancy requires 512 KiB for all lookup tables, so considering the [inner six bits](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") would quarter the table sizes.
In Cinnamon **2.3** the occupancy index may be computed by the [PEXT](BMI2#PEXT "BMI2") instruction, if the executable is compiled with [BMI2](BMI2 "BMI2") enabled.

## Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") by line-wise [Occupancy Lookup](Sliding_Piece_Attacks#By_Occupancy_Lookup "Sliding Piece Attacks")

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Razoring](Razoring "Razoring")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")

## Evaluation

- [Material](Material "Material")
- [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [King Safety](King_Safety "King Safety")

## Misc

- [PolyGlot](PolyGlot "PolyGlot") [Opening Book](Opening_Book "Opening Book")
- [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")
- [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
- [Perft](Perft "Perft")
- [Pondering](Pondering "Pondering")
- [Chess960](Chess960 "Chess960")

## See also

- [Butterfly](index.php?title=Butterfly&action=edit&redlink=1 "Butterfly (page does not exist)")

## Forum Posts

- [OSX compiler wanted](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52869&p=199463) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 06, 2013
- [Cinnamon 1.1 for Mac OS X 32-bit](http://www.talkchess.com/forum/viewtopic.php?t=48582) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), July 07, 2013
- [Cinnamon 2.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=59877) by supersharp77, [CCC](CCC "CCC"), April 17, 2016
- [Cinnamon 2.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75445) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 19, 2020

## External Links

## Chess Engine

- [GitHub - gekomad/Cinnamon: C++ UCI chess engine](https://github.com/gekomad/cinnamon)
- [Cinnamon](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Cinnamon&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [Cinnamon from Wikipedia](https://en.wikipedia.org/wiki/Cinnamon)
- [Cinnamomum from Wikipedia](https://en.wikipedia.org/wiki/Cinnamomum)

[Cinnamomum burmannii from Wikipedia](https://en.wikipedia.org/wiki/Cinnamomum_burmannii)
[Cinnamomum cassia from Wikipedia](https://en.wikipedia.org/wiki/Cinnamomum_cassia)
[Cinnamomum verum from Wikipedia](https://en.wikipedia.org/wiki/Cinnamomum_verum)

- [Cinnamon (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Cinnamon_%28disambiguation%29)
- [cinnamon - Wiktionary](https://en.wiktionary.org/wiki/cinnamon)
- [Cinnamon (software) from Wikipedia](https://en.wikipedia.org/wiki/Cinnamon_%28software%29)
- [Bill Anschell](https://en.wikipedia.org/wiki/Bill_Anschell), [Jose Martinez](http://www.seattledrumschool.com/portfolio-view/jose-martinez/), [Chris Symer](http://originarts.com/artists/artist.php?Artist_ID=228) - [La Flor de la Canela](https://en.wikipedia.org/wiki/La_Flor_de_la_Canela) by [Chabuca Granda](https://en.wikipedia.org/wiki/Chabuca_Granda), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Cinnamon: sticks ([ceylon cinnamon](https://en.wikipedia.org/wiki/Cinnamomum_verum) from [Sri Lanka](https://en.wikipedia.org/wiki/Sri_Lanka)), powder, and flowers. Created from 31 images stacked with [CombineZP](https://en.wikipedia.org/wiki/CombineZ), by [Simon A. Eugster](https://commons.wikimedia.org/wiki/User:LivingShadow), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Cinnamomum from Wikipedia](https://en.wikipedia.org/wiki/Cinnamomum)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Cinnamon](http://www.g-sei.org/cinnamon/) « [G 6](G_6 "G 6")
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [GitHub - gekomad/Cinnamon: C++ UCI chess engine](https://github.com/gekomad/Cinnamon)

**[Up one Level](Engines "Engines")**

