---
title: Atlas ESP
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Atlas**

\[ Sculpture of [Atlas](https://en.wikipedia.org/wiki/Atlas_%28mythology%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Atlas**,

an [UCI](UCI "UCI") compliant chess engine by [Andrés Manzanares Campillo](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo") written in [C++](Cpp "Cpp") - executables running under [Linux](Linux "Linux") and [Windows](Windows "Windows").
The development of Atlas started in 2004, initially [representing the board](Board_Representation "Board Representation") as [0x88](0x88 "0x88") [vector attacks](Vector_Attacks "Vector Attacks") [mailbox](Mailbox "Mailbox") along with [piece-lists](Piece-Lists "Piece-Lists"),
supporting [WinBoard](WinBoard "WinBoard"), and written in [C](C "C"). Atlas **2.90** was a complete rewrite released in June 2011, a [bitboard](Bitboards "Bitboards") approach only supporting UCI <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Features

<a id="cite-note-3" href="#cite-ref-3">[3]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows") (unsymmetrical)
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with [R==3](Depth_Reduction_R "Depth Reduction R") and [Verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
- [Futility Pruning](Futility_Pruning "Futility Pruning")
- [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Check Extensions](Check_Extensions "Check Extensions")
- [Singular Extensions](Singular_Extensions "Singular Extensions") (3.90)
- [Transposition Table](Transposition_Table "Transposition Table")
- [History Heuristic](History_Heuristic "History Heuristic")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Material Hash Table](Material_Hash_Table "Material Hash Table")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility") (non-linear)
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [King Safety](King_Safety "King Safety")

## Namesake

- [Atlas](Atlas "Atlas") by [Alex Bell](Alex_Bell "Alex Bell")

## Forum Posts

## 2005 ...

- [Atlas 2 Winboard Engine crashes in Arena GUI](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2330) by Marc Darius, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 20, 2005
- [Atlas 2.20 hash usage](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5473) by [Graham Banks](Graham_Banks "Graham Banks"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 27, 2006
- [Confused with Atlas 2.20- Help Appreciated](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=6103) by [George Speight](index.php?title=George_Speight&action=edit&redlink=1 "George Speight (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 12, 2007

## 2010 ...

- [Atlas 3.60 Release](http://www.talkchess.com/forum/viewtopic.php?t=50131) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), November 18, 2013
- [Atlas 3.70em Release](http://www.talkchess.com/forum/viewtopic.php?t=53021) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), July 20, 2014

## 2015 ...

- [Atlas 3.80 release](http://www.talkchess.com/forum/viewtopic.php?t=55234) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), February 06, 2015
- [Atlas 3.90 release](http://www.talkchess.com/forum/viewtopic.php?t=66387) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), January 22, 2018
- [Atlas 3.91 (bugfix version)](http://www.talkchess.com/forum/viewtopic.php?t=66416) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), January 26, 2018

## 2020 ...

- [Atlas website (update bookmarks)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75361) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), October 10, 2020

## External Links

## Chess Engine

- [Atlas - Home](https://sites.google.com/view/atlaschess/)
- [Atlas](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Atlas&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [Atlas (computer) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28computer%29)
- [Atlas (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28disambiguation%29)
- [Atlas from Wikipedia](https://en.wikipedia.org/wiki/Atlas)
- [Atlas Mountains from Wikipedia](https://en.wikipedia.org/wiki/Atlas_Mountains)
- [Atlas (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28mythology%29)
- [Farnese Atlas from Wikipedia](https://en.wikipedia.org/wiki/Farnese_Atlas)
- [Atlas (rocket family) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28rocket_family%29)
- [Atlas (star) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28star%29)
- [Atlas (moon) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28moon%29)
- [Colossochelys atlas from Wikipedia](https://en.wikipedia.org/wiki/Colossochelys_atlas)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Sculpture of [Atlas](https://en.wikipedia.org/wiki/Atlas_%28mythology%29), Praza do Toural, [Santiago de Compostela](https://en.wikipedia.org/wiki/Santiago_de_Compostela), Photo by [Luis Miguel Bugallo Sánchez](https://commons.wikimedia.org/wiki/User:Lmbuga), October 18, 2005, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Atlas (mythology) from Wikipedia](https://en.wikipedia.org/wiki/Atlas_%28mythology%29)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Progreso - Atlas](https://sites.google.com/view/atlaschess/home/progreso)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> Features of Atlas 3.80 based on [Atlas - Home](https://sites.google.com/view/atlaschess/) and [Atlas 3.80 release](http://www.talkchess.com/forum/viewtopic.php?t=55234) by [Andrés Manzanares](Andr%C3%A9s_Manzanares_Campillo "Andrés Manzanares Campillo"), [CCC](CCC "CCC"), February 06, 2015
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Atlas - Home - Agradecimientos](https://sites.google.com/view/atlaschess/home)

**[Up one Level](Engines "Engines")**

