---
title: Daydreamer
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Daydreamer**

\[ A daydreaming gentleman <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Daydreamer**, (DayDreamer)

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Aaron Becker](Aaron_Becker "Aaron Becker"), written in [C](C "C"), and the **2.0** pre-release in [Rust](Rust "Rust") <a id="cite-note-2" href="#cite-ref-2">[2]</a>,
also able to play [Chess960](Chess960 "Chess960"). Developed since early 2009, the program was named Daydreamer after a bug in an early version caused it to occasionally follow up very strong play with bizarre blunders, as though it had lost its focus on the game and its mind was wandering aimlessly.
First released in August 2009 <a id="cite-note-3" href="#cite-ref-3">[3]</a>, it initially used [Tomasz Michniewski's](Tomasz_Michniewski "Tomasz Michniewski") [simplified evaluation function](Simplified_Evaluation_Function "Simplified Evaluation Function"), while subsequent versions were rapidly improving since mid 2010. DayDreamer played the [CCT12](CCT12 "CCT12") and [ACCA 2010](ACCA_2010 "ACCA 2010") online tournaments.

## Description

## Board Representation

Daydreamer prior to **2.0** pre-release used [piece-lists](Piece-Lists "Piece-Lists") and a [16x16 vector attacks](Vector_Attacks "Vector Attacks") board around a [0x88](0x88 "0x88") board inside its middle 16x8 slots <a id="cite-note-4" href="#cite-ref-4">[4]</a>. [Move generation](Move_Generation "Move Generation") of pieces is unrolled over [directions](Direction "Direction"), [capture](Captures "Captures") generation of [sliding pieces](Sliding_Pieces "Sliding Pieces") for [quiescence](Quiescence_Search "Quiescence Search") uses the leading efficient [blocker loop](Vector_Attacks#blockerloop "Vector Attacks"), i.e. for one vertical direction <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

```C++

  for (to=from+16; pos->board[to]==EMPTY; to+=16) {}
  if (can_capture(piece, pos->board[to])) {
    moves = add_move(pos, create_move(from, to, piece,
                     pos->board[to]), moves);
  }

```

Daydreamer 2.0 is a not finished rewrite in [Rust](Rust "Rust") <a id="cite-note-6" href="#cite-ref-6">[6]</a>, with the significant change to [bitboards](Bitboards "Bitboards") and the introduction of \[\[Move Generation#Staged|staged move generation\].

## Search

The [search](Search "Search") is [PVS](Principal_Variation_Search "Principal Variation Search") [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [null move pruning](Null_Move_Pruning "Null Move Pruning") combined with [mate threat extensions](Mate_Threat_Extensions "Mate Threat Extensions"), [razoring](Razoring "Razoring"), [futility pruning](Futility_Pruning "Futility Pruning") and [late move reductions](Late_Move_Reductions "Late Move Reductions") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") framework with [aspiration windows](Aspiration_Windows "Aspiration Windows") and [floating point](Float "Float") [fractional ply depth](Depth#FractionalPlies "Depth"),
the latter credited to [Ivan Bonkin](Ivan_Bonkin "Ivan Bonkin") and his [Bison](Bison "Bison") program <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Opening Book

Daydreamer supports [PolyGlot](PolyGlot "PolyGlot") and [ctg](CTG "CTG") [opening books](Opening_Book "Opening Book") <a id="cite-note-8" href="#cite-ref-8">[8]</a>, the [huffman codes](https://en.wikipedia.org/wiki/Huffman_coding) and ctg move decoding based on [Stephan Vermeire's](Stephan_Vermeire "Stephan Vermeire") ctg code for [Brutus](Brutus_NL "Brutus NL") <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

## Endgame Tablebases

Daydreamer is able to probe [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases") as well as [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases") <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## Evaluation

Daydreamer's [evaluation](Evaluation "Evaluation") might be [lazy](Lazy_Evaluation "Lazy Evaluation") with respect to [bounds](Bound "Bound") and margins based on [cached](Material_Hash_Table "Material Hash Table") [material](Material "Material"), considering imbalances, and [piece-square table](Piece-Square_Tables "Piece-Square Tables") [scores](Score "Score") only. Otherwise, supported by a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table"), it takes [pawn structure](Pawn_Structure "Pawn Structure"), [mobility](Mobility "Mobility"), [king safety](King_Safety "King Safety") and various other terms into account, speculatively aggregating [middle-](Middlegame "Middlegame") and [endgame](Endgame "Endgame") scores, which were finally [tapered](Tapered_Eval "Tapered Eval") by a range of 24 [game phases](Game_Phases "Game Phases").

## Selected Games

[ACCA 2010](ACCA_2010 "ACCA 2010"), round 6, DayDreamer - [Gaviota](Gaviota "Gaviota") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

```

[Event "ACCA 2010"]
[Site "FICS, San Jose, California USA"]
[Date "2010.11.07"]
[Round "6"]
[White "DayDreamer"]
[Black "Gaviota"]
[Result "1-0"]

1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3+ 6.bxc3 Ne7 7.Qg4 O-O 8.Bd3 Nbc6 
9.Nf3 f5 10.exf6 Rxf6 11.Qh5 h6 12.O-O c4 13.Be2 Qa5 14.Bd2 Bd7 15.Ne5 Be8 
16.Qh4 Nxe5 17.dxe5 Nf5 18.Qh3 Rf8 19.a4 Bxa4 20.g4 Nd4 21.Bd1 b5 22.Kh1 Rf7 
23.g5 Nf5 24.gxh6 Qc7 25.Bh5 Re7 26.Bg6 Bxc2 27.Rg1 Qxe5 28.Bh7+ Kf8 29.Rae1 
Be4+ 30.f3 Ke8 31.fxe4 dxe4 32.hxg7 Kd7 33.g8=Q Rxg8 34.Rxg8 Kc7 35.Ra1 Kb7 
36.Bxf5 Qxf5 37.Qh8 a5 38.Rg5 Qf3+ 39.Kg1 e5 40.Qd8 Qf6 41.Qxa5 Qb6+ 42.Qxb6+ 
Kxb6 43.Be3+ Kc6 44.Ra6+ Kd7 45.Bc5 e3 46.Bxe7 1-0

```

## See also

- [Dreamer](Dreamer "Dreamer")

## Forum Posts

## 2009

- [Announcing Daydreamer 1.0](http://www.talkchess.com/forum/viewtopic.php?t=29417) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), August 16, 2009
- [Daydreamer 1.01 : 2037](http://www.talkchess.com/forum/viewtopic.php?t=29519) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), August 24, 2009
- [Announcing Daydreamer 1.5](http://www.talkchess.com/forum/viewtopic.php?t=29651) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), September 04, 2009
- [Daydreamer 1.51 : 2272](http://www.talkchess.com/forum/viewtopic.php?t=30605) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), November 14, 2009
- [Announcing Daydreamer 1.6](http://www.talkchess.com/forum/viewtopic.php?t=31200) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), December 22, 2009

## 2010 ...

- [Daydreamer 1.61: 2361](http://www.talkchess.com/forum/viewtopic.php?t=31421) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), January 02, 2010
- [Test tournament starts: Gaviota, Daydreamer, Greko, Atak](http://www.talkchess.com/forum/viewtopic.php?t=31606) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), January 10, 2010 » [Gaviota](Gaviota "Gaviota"), Daydreamer, [GreKo](GreKo "GreKo"), [Atak](Atak "Atak")
- [Daydreamer 1.7](http://www.talkchess.com/forum/viewtopic.php?t=33361) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), March 19, 2010
- [Daydreamer 1.7 : 2519](http://www.talkchess.com/forum/viewtopic.php?t=33417) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), March 22, 2010
- [Daydreamer 1.75](http://www.talkchess.com/forum/viewtopic.php?t=33590) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), April 02, 2010
- [Daydreamer 1.75 : 2569](http://www.talkchess.com/forum/viewtopic.php?t=33622) by [Patrick Buchmann](Patrick_Buchmann "Patrick Buchmann"), [CCC](CCC "CCC"), April 05, 2010
- [Compiling Daydreamer in Visual Studio](http://www.talkchess.com/forum/viewtopic.php?t=34094) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), May 01, 2010
- [Developments of the last two years](http://www.talkchess.com/forum/viewtopic.php?t=47384) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), March 02, 2013
- [Re: copy/make vs make/unmake](http://www.talkchess.com/forum/viewtopic.php?t=50805&start=3) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), January 07, 2014 » [Copy-Make](Copy-Make "Copy-Make"), [Make Move](Make_Move "Make Move"), [Unmake Move](Unmake_Move "Unmake Move")

## 2015 ...

- [Daydreamer 2.0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68647) by CMCanavessi, [CCC](CCC "CCC"), October 14, 2018

## [Re: Daydreamer 2.0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68647&start=2) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 14, 2018 External Links

## Chess Engine

- [GitHub - AaronBecker/daydreamer](https://github.com/AaronBecker/daydreamer)

[Downloads · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/downloads)

- [Index of /chess/engines/Jim Ablett/DAYDREAMER](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/DAYDREAMER/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

[Index of /chess/engines/Jim Ablett/+++ LINUX ENGINES ++/32 BIT/daydreamer](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/+++%20LINUX%20ENGINES%20++/32%20BIT/daydreamer/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

- [Daydreamer 1.75 64-bit](http://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Daydreamer+1.75+64-bit) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Daydreamer (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Daydreamer)
- [Daydream from Wikipedia](https://en.wikipedia.org/wiki/Daydream)
- [Broken Brass Ensemble](Category:Broken_Brass_Ensemble "Category:Broken Brass Ensemble") - Daydream, October 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [A daydreaming gentleman](https://commons.wikimedia.org/wiki/File:Daydreaming_Gentleman.jpg); from an original 1912 postcard published in Germany, [Daydream from Wikipedia](https://en.wikipedia.org/wiki/Daydream), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [daydreamer/README.md at release · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/blob/release/README.md)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Announcing Daydreamer 1.0](http://www.talkchess.com/forum/viewtopic.php?t=29417) by [Aaron Becker](Aaron_Becker "Aaron Becker"), [CCC](CCC "CCC"), August 16, 2009
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [daydreamer/position.h at release · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/blob/release/position.h)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [daydreamer/move_generation.c at release · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/blob/release/move_generation.c)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Daydreamer 2.0?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68647&start=2) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), October 14, 2018
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Bison by Иван Бонькин (Ivan Bonkin), Russia!](http://www.sdchess.ru/Bison.html) from [sdchess.ru](http://www.sdchess.ru/) - searcher.h
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [GitHub - AaronBecker/daydreamer: A chess engine, focused on search, written in C - Changes from 1.6 to 1.7](https://github.com/AaronBecker/daydreamer#changes-from-16-to-17)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [daydreamer/book_ctg.c at release · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/blob/release/book_ctg.c)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [daydreamer/scorpio_bb.c at release · AaronBecker/daydreamer · GitHub](https://github.com/AaronBecker/daydreamer/blob/release/scorpio_bb.c)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [The 2010 Fifth Annual ACCA Americas' Computer Chess Championships -- Results](http://compchess.org/ACCAChampionships/ACCA2010Championships/2010ACCCResults.html)

**[Up one level](Engines "Engines")**

