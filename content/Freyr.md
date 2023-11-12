---
title: Freyr
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Freyr**

\[ [Freyr](https://en.wikipedia.org/wiki/Freyr) and [Gullinbursti](https://en.wikipedia.org/wiki/Gullinbursti) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Freyr**,

a [WinBoard](WinBoard "WinBoard") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), written in [C++](Cpp "Cpp"), intended as a test ground for various chess algorithms, first released in February 2000.

## Description

Freyr is a [bitboard](Bitboards "Bitboards") engine and uses [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). The search is [PVS](Principal_Variation_Search "Principal Variation Search") <a id="cite-note-2" href="#cite-ref-2">[2]</a> with [null move pruning](Null_Move_Pruning "Null Move Pruning") inside an [aspiration window](Aspiration_Windows "Aspiration Windows") [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [transposition table](Transposition_Table "Transposition Table"), using several [move ordering](Move_Ordering "Move Ordering") heuristics, such as [killer](Killer_Heuristic "Killer Heuristic"), [history](History_Heuristic "History Heuristic") and [countermove](Countermove_Heuristic "Countermove Heuristic"), as well as [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") to order [captures](Captures "Captures"). [Lazy evaluation](Lazy_Evaluation "Lazy Evaluation") considers [incremental updated](Incremental_Updates "Incremental Updates") [material-](Material "Material") and [piece-square table](Piece-Square_Tables "Piece-Square Tables") scores and [cached](Pawn_Hash_Table "Pawn Hash Table") [pawn structure](Pawn_Structure "Pawn Structure") stuff. [Evaluation](Evaluation "Evaluation") further includes [king safety](King_Safety "King Safety") and [passed pawns](Passed_Pawn "Passed Pawn") as most dominant terms <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [Thor's Hammer](Thor%27s_Hammer "Thor's Hammer")

## Forum Posts

- [New Winboard Program](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30905) by [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2000
- [A New Release of my Amateur Chess Engine Freyr](https://www.stmintz.com/ccc/index.php?id=98762) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), February 22, 2000
- [Freyr 0.960 released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30992) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 29, 2000
- [A Question on simple Alpha-Beta versus PVS/Negascout](https://www.stmintz.com/ccc/index.php?id=102792) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), March 21, 2000 » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [NegaScout](NegaScout "NegaScout")
- [Freyr 0.987 Released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31398) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 30, 2000
- [Freyr 1.015 Released](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31531) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 29, 2000
- [Freyr 1.024 sees the daylight](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31554) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 02, 2000
- [Freyr 1.067](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=32400) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 15, 2000

## External Links

## Chess Engine

- [Freyr - A Chess Playing Program](https://web.archive.org/web/20180713142619/http://www.planet-source-code.com/vb/scripts/ShowCode.asp?txtCodeId=3333&lngWId=3) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Index of /chess/engines/Jim Ablett/FREYR](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/FREYR/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Freyr 1.068 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&print=Details&each_game=1&eng=Freyr%201.068%2064-bit) in [CCRL Blitz](CCRL "CCRL")

## Misc

- [Freyr from Wikipedia](https://en.wikipedia.org/wiki/Freyr)
- [Sword of Freyr from Wikipedia](https://en.wikipedia.org/wiki/Sword_of_Freyr)
- [Yngvi-Freyr from Wikipedia](https://en.wikipedia.org/wiki/Yngvi)
- [Frey (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Frey_%28disambiguation%29)
- [Freyja from Wikipedia](https://en.wikipedia.org/wiki/Freyja)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> *Freyr* by [Johannes Gehrts](https://en.wikipedia.org/wiki/Johannes_Gehrts). The god [Freyr](https://en.wikipedia.org/wiki/Freyr) stands with his sword and the boar [Gullinbursti](https://en.wikipedia.org/wiki/Gullinbursti). Source: [Felix Dahn](https://en.wikipedia.org/wiki/Felix_Dahn), [Therese Dahn](https://de.wikipedia.org/wiki/Therese_Dahn) (**1901**). *[Walhall: Germanische Götter- und Heldensagen. Für Alt und Jung am deutschen Herd](https://archive.org/details/walhallgermanisc1888dahn/page/n5)*. [Breitkopf & Härtel](https://en.wikipedia.org/wiki/Breitkopf_%26_H%C3%A4rtel), [Sword of Freyr from Wikipedia](https://en.wikipedia.org/wiki/Sword_of_Freyr)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [A Question on simple Alpha-Beta versus PVS/Negascout](https://www.stmintz.com/ccc/index.php?id=102792) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), March 21, 2000
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Planet Source Code™ | Freyr - A Chess Playing Program](http://www.planet-source-code.com/vb/scripts/ShowCode.asp?txtCodeId=3333&lngWId=3) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna")

**[Up one level](Engines "Engines")**

