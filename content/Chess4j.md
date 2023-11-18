---
title: Chess4j
---
**[Home](Home "Home") * [Engines](Engines "Engines") * chess4j**

**chess4j**,

an [open source chess engine](Category:Open_Source "Category:Open Source") by [James Swafford](James_Swafford "James Swafford") using [Java](Java "Java") based technologies
and the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), released under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"),
and first published in September 2012 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
The engine was hosted on [SourceForge](https://en.wikipedia.org/wiki/SourceForge), and meant to be a test bed for various interests, including experimenting with different [JVM based languages](https://en.wikipedia.org/wiki/List_of_JVM_languages), [parallel](Parallel_Search "Parallel Search") and [distributed](https://en.wikipedia.org/wiki/Distributed_computing) programming techniques, and [machine learning](Learning "Learning").
Since version 3.2 released in March 2017, chess4j became a [bitboard](Bitboards "Bitboards") engine, using [magic bitboards](Magic_Bitboards "Magic Bitboards") to [generate moves](Move_Generation "Move Generation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, now hosted on [GitHub](https://en.wikipedia.org/wiki/GitHub).

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
- [Selectivity](Selectivity "Selectivity")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") with [Null Move Pruning#ZugzwangVerification Zugzwang Detection](Null_Move_Pruning#ZugzwangVerification_Zugzwang_Detection "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Rook on Open File](Rook_on_Open_File "Rook on Open File")
- [Rook/Queen on Seventh](Rook_on_Seventh "Rook on Seventh")
- [King Safety](King_Safety "King Safety")
  - [Pawn Shelter](King_Safety#PawnShield "King Safety")
  - [Knight/King Tropism](King_Safety#KingTropism "King Safety")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")

## See also

- [Prophet](Prophet "Prophet")

## Forum Posts

## 2012 ...

- [Mr.James Swafford and Chess4J project](http://www.talkchess.com/forum/viewtopic.php?t=45090) by Ruxy Sylwyka, [CCC](CCC "CCC"), September 11, 2012
- [Chess4J 2.0 is out !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=52597) by Ruxy Sylwyka, [CCC](CCC "CCC"), June 10, 2014

## 2015 ...

- [chess4j 3.0 is released](http://www.talkchess.com/forum/viewtopic.php?t=58934) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), January 16, 2016
- [chess4j 3.1 released](http://www.talkchess.com/forum/viewtopic.php?t=63157) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), February 12, 2017
- [chess4j 3.2 is released (and it's magic)](http://www.talkchess.com/forum/viewtopic.php?t=63412) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), March 11, 2017
- [hashing in chess4j](http://www.talkchess.com/forum/viewtopic.php?t=66183) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), December 30, 2017 » [Transposition Table](Transposition_Table "Transposition Table")
- [chess4j 3.4](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68089) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), July 27, 2018
- [chess4j 3.5](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69303) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), December 18, 2018

## 2020 ...

- [Prophet 4.0 and chess4j 4.0 are released](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78314) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), October 02, 2021

## External Links

- [GitHub - jswaff/chess4j: a Java based chess engine](https://github.com/jswaff/chess4j) <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [chess4j | James Swafford Blog](http://www.jamesswafford.com/chess4j/)
- [Chess4j](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Chess4j&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [chess4j 1.0 is released!](http://www.jamesswafford.com/2012/09/15/chess4j-1-0-is-released/) by [James Swafford](James_Swafford "James Swafford"), September 15, 2012
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [chess4j 3.2 is released (and it's magic)](http://www.talkchess.com/forum/viewtopic.php?t=63412) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), March 11, 2017
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: chess4j 3.2 is released (and it's magic)](http://www.talkchess.com/forum/viewtopic.php?t=63412&start=4) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), November 16, 2017

**[Up one level](Engines "Engines")**

