---
title: Bismark
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Bismark**

\[ [Between Berlin and Rome](https://en.wikipedia.org/wiki/Kulturkampf) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Bismark**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Evgeny Shtranvasser](Evgeny_Shtranvasser "Evgeny Shtranvasser"), written in [C++](Cpp "Cpp"), recent version hosted by [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket) <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Bismark's board is represented as two-dimensional [8x8](8x8_Board "8x8 Board") [array](Array "Array") of [squares](Squares "Squares") and a [vector of pieces](Piece-Lists "Piece-Lists").
The engine applies [negamax](Negamax "Negamax") [alpha-beta](Alpha-Beta "Alpha-Beta") [PVS](Principal_Variation_Search "Principal Variation Search") with [null move pruning](Null_Move_Pruning "Null Move Pruning"), [transposition table](Transposition_Table "Transposition Table") and a pure capture [quiescence search](Quiescence_Search "Quiescence Search") within the [iterative deepening](Iterative_Deepening "Iterative Deepening") loop. Beside [material](Material "Material") as dominating term, Bismark's [evaluation](Evaluation "Evaluation") aggregates values of [middlegame](Middlegame "Middlegame") and [endgame](Endgame "Endgame") [piece-square tables](Piece-Square_Tables "Piece-Square Tables") along with [king tropism](King_Safety#KingTropism "King Safety"), finally [tapered](Tapered_Eval "Tapered Eval") by current [game phase](Game_Phases "Game Phases") using [float arithmetic](Float "Float"). Further, Bismark considers various [pawn structure](Pawn_Structure "Pawn Structure") terms, with appropriate bonuses for [passers](Passed_Pawn "Passed Pawn") and [candidates](Candidate_Passed_Pawn "Candidate Passed Pawn") and penalties for [doubled pawns](Doubled_Pawn "Doubled Pawn") and [islands](Pawn_Islands "Pawn Islands"), as well as beneficial piece positions such as [knight outposts](Outposts "Outposts"), [rook on open or semi-open file](Rook_on_Open_File "Rook on Open File") and [bishop pair](Bishop_Pair "Bishop Pair") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Forum Posts](#forum-posts)
- [2 External Links](#external-links)
  - [2.1 Chess Engine](#chess-engine)
  - [2.2 Misc](#misc)
- [3 References](#references)

## Forum Posts

- [Bismark and Powder](http://www.talkchess.com/forum/viewtopic.php?t=44760) by Geert Maeckelbergh, [CCC](CCC "CCC"), August 10, 2012

## External Links

## Chess Engine

- [jackalsh / Bismark — Bitbucket](https://bitbucket.org/jackalsh/bismark)
- [SDChess - Downloads](http://www.sdchess.ru/download_engines.htm)
- [Bismark 1.4](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Bismark%201.4) in [CCRL Blitz](CCRL "CCRL")
- [Chesstroid: New Android UCI engine: Bismark 1.3.JA](http://chesstroid.blogspot.com/2015/01/new-android-uci-engine-bismark-13ja.html) by [Gurcan Uckardes](index.php?title=Gurcan_Uckardes&action=edit&redlink=1 "Gurcan Uckardes (page does not exist)"), January 13, 2015

## Misc

- [Bismarck from Wikipedia](https://en.wikipedia.org/wiki/Bismarck)
- [Bismarck (board game) from Wikipedia](https://en.wikipedia.org/wiki/Bismarck_%28board_game%29)
- [Bismarck Archipelago from Wikipedia](https://en.wikipedia.org/wiki/Bismarck_Archipelago)
- [Bismarck, North Dakota from Wikipedia](https://en.wikipedia.org/wiki/Bismarck,_North_Dakota)
- [House of Bismarck from Wikipedia](https://en.wikipedia.org/wiki/House_of_Bismarck)
- [Mona von Bismarck from Wikipedia](https://en.wikipedia.org/wiki/Mona_von_Bismarck)
- [Otto von Bismarck from Wikipedia](https://en.wikipedia.org/wiki/Otto_von_Bismarck)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Caricature "Between Berlin and Rome" by [Wilhelm Scholz](https://de.wikipedia.org/wiki/Wilhelm_Scholz_%28Karikaturist%29), [Kladderadatsch](https://en.wikipedia.org/wiki/Kladderadatsch), May 16, 1875. The caption reads: ([Pope](https://en.wikipedia.org/wiki/Pope_Pius_IX):) "The last move was certainly very unpleasant for me; but that doesn't yet mean the game is lost. I have one more very fine move up my sleeve!" ([Bismarck](https://en.wikipedia.org/wiki/Otto_von_Bismarck):) "It will also be the last, and then you are mated in a few moves - at least for Germany." Note the caricaturist's error in orienting the chessboard by placing white squares on players' left. [Kulturkampf from Wikipedia](https://en.wikipedia.org/wiki/Kulturkampf), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [jackalsh / Bismark — Bitbucket](https://bitbucket.org/jackalsh/bismark/src/master/)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Description based on the sources of Bismark 1.3

**[Up one Level](Engines "Engines")**

