---
title: Googleplex Starthinker
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Googleplex Starthinker**

[](File:Googleplex_Starthinker.png) Googleplex Starthinker <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Googleplex Starthinker**,

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Jost Triller](Jost_Triller "Jost Triller"),
written in [C++](Cpp "Cpp"), first released in December 2018 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Googleplex Starthinker is a [bitboard](Bitboards "Bitboards") engine and generates [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") [Kindergarten](Kindergarten_Bitboards "Kindergarten Bitboards") like,
by looking up four pre-calculated line attack arrays, 32-Kbyte each, indexed by square and [inner six bit](First_Rank_Attacks#TheOuterSquares "First Rank Attacks") [line occupancy](Occupancy_of_any_Line "Occupancy of any Line") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Etymology](#etymology)
- [2 Features](#features)
  - [2.1 Board Representation](#board-representation)
  - [2.2 Search](#search)
  - [2.3 Evaluation](#evaluation)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
  - [5.1 Chess Engine](#chess-engine)
  - [5.2 Misc](#misc)
- [6 References](#references)

## Etymology

In the scripts for [Fit the Fourth](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy_Primary_and_Secondary_Phases#Fit_the_Fourth) of the [The Hitchhiker's Guide to the Galaxy radio series](<https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy_(radio_series)>),
the first programmer asks [Deep Thought](https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Deep_Thought) if it is not "a greater analyst than the **Googleplex Starthinker** in the Seventh Galaxy of Light and Ingenuity which can calculate the trajectory of every single dust particle throughout a five-week [Aldebaran](https://en.wikipedia.org/wiki/Aldebaran) sand blizzard?",
which the great computer dismisses because he has already "contemplated the very vectors of the atoms in the [Big Bang](https://en.wikipedia.org/wiki/Big_Bang) itself" <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>.

## Features

<a id="cite-note-7" href="#cite-ref-7">[7]</a>

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Kindergarten Bitboards](Kindergarten_Bitboards "Kindergarten Bitboards")
- [Staged Move Generation](Move_Generation#Staged "Move Generation")

## [Search](Search "Search")

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta") [Negamax](Negamax "Negamax")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Hash Move](Hash_Move "Hash Move")
  - [MVV-LVA](MVV-LVA "MVV-LVA")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Delta Pruning](Delta_Pruning "Delta Pruning")

## [Evaluation](Evaluation "Evaluation")

- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Outposts](Outposts "Outposts")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
- [King Safety](King_Safety "King Safety")

## See also

- [Deep Thought](Deep_Thought "Deep Thought")
- [Hactar](Hactar "Hactar")
- [Nalwald](Nalwald "Nalwald")
- [squared-chess](Squared-chess "Squared-chess")

## Forum Posts

- ["Googleplex Starthinker" chess engine](http://talkchess.com/forum3/viewtopic.php?f=2&t=69117) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), December 02, 2018
- [GooglePlex Starthinker](http://talkchess.com/forum3/viewtopic.php?f=2&t=71579) by Damir, [CCC](CCC "CCC"), August 17, 2019

## External Links

## Chess Engine

- [Tsoj Tsoj / Googleplex_Starthinker · GitLab](https://gitlab.com/tsoj/Googleplex_Starthinker)
- [Googleplex Starthinker](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Googleplex&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")

## Misc

- [List of The Hitchhiker's Guide to the Galaxy characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Googleplex_Starthinker)
- [Googleplex Starthinker | Hitchhikers | Fandom](https://hitchhikers.fandom.com/wiki/Googleplex_Starthinker)
- [Googleplex Starthinker](http://starthinker.fr/)
- [Googolplex from Wikipedia](https://en.wikipedia.org/wiki/Googolplex)
- [Return to Forever](Category:Return_to_Forever "Category:Return to Forever") - [Hymn of the Seventh Galaxy](https://en.wikipedia.org/wiki/Hymn_of_the_Seventh_Galaxy), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), 2008, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[Chick Corea](Category:Chick_Corea "Category:Chick Corea"), [Al Di Meola](Category:Al_Di_Meola "Category:Al Di Meola"), [Stanley Clarke](Category:Stanley_Clarke "Category:Stanley Clarke"), [Lenny White](Category:Lenny_White "Category:Lenny White")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Googleplex Starthinker logo based on [Googleplex_Starthinker.png · master · Tsoj Tsoj / Googleplex_Starthinker · GitLab](https://gitlab.com/tsoj/Googleplex_Starthinker/-/blob/master/Googleplex_Starthinker.png)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> ["Googleplex Starthinker" chess engine](http://talkchess.com/forum3/viewtopic.php?f=2&t=69117) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), December 02, 2018
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [src/bitboard.hpp · master · Tsoj Tsoj / Googleplex_Starthinker · GitLab](https://gitlab.com/tsoj/Googleplex_Starthinker/-/blob/master/src/bitboard.hpp#L106)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [List of The Hitchhiker's Guide to the Galaxy characters - Wikipedia](https://en.wikipedia.org/wiki/List_of_The_Hitchhiker%27s_Guide_to_the_Galaxy_characters#Googleplex_Starthinker)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Douglas Adams](Category:Douglas_Adams "Category:Douglas Adams") (**1985**). *[The Hitch-Hiker's Guide to the Galaxy: The Original Radio Scripts](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy:_The_Original_Radio_Scripts)*. Pan Books
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Googleplex Starthinker](http://starthinker.fr/)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [README.md · master · Tsoj Tsoj / Googleplex_Starthinker · GitLab](https://gitlab.com/tsoj/Googleplex_Starthinker/-/blob/master/README.md)

**[Up one Level](Engines "Engines")**

