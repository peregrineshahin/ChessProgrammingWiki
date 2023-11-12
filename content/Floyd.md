---
title: Floyd
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Floyd**

\[.jpg) Hurricane Floyd <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Floyd**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") for study purposes and prototyping of new ideas by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), written in [C](C "C"), and first released in October 2015 <a id="cite-note-2" href="#cite-ref-2">[2]</a> with a permissive license <a id="cite-note-3" href="#cite-ref-3">[3]</a> . Floyd can be build to run under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [Mac OS](Mac_OS "Mac OS"). Floyd had its over the board tournament debut at the [IGT 2016](IGT_2016 "IGT 2016") with a 50% score.

## Contents

- [1 Description](#description)
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

## Description

## Board Representation

Floyd uses an [8x8 Board](8x8_Board "8x8 Board"), agnostic to [square indexing](Square_Mapping_Considerations "Square Mapping Considerations"), in the sense that it can be adapted to any of the eight possible board geometries with just a local change <a id="cite-note-4" href="#cite-ref-4">[4]</a> . It uses an [attack table](Attack_and_Defend_Maps "Attack and Defend Maps"), for each side an array of 64 [bytes](Byte "Byte"), with following one- or two-bit attack counters per square ...

```C++

+-----+-----+-----+-----+-----+-----+-----+-----+
|   Pawns   |   Minors  |   Rooks   |Queen|King |
+-----+-----+-----+-----+-----+-----+-----+-----+
     7..6        5..4        3..2      1     0

```

... as used in [move generation](Move_Generation "Move Generation"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") and [evaluation](Evaluation "Evaluation").

## Search

The [search](Search "Search") is a classical [PVS](Principal_Variation_Search "Principal Variation Search") [iterative deepening](Iterative_Deepening "Iterative Deepening") approach with [Zobrist key](Zobrist_Hashing "Zobrist Hashing") [transposition table](Transposition_Table "Transposition Table"), [quiescence search](Quiescence_Search "Quiescence Search"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [mate distance pruning](Mate_Distance_Pruning "Mate Distance Pruning"). [Move ordering](Move_Ordering "Move Ordering") considers [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") and a simple [killer heuristic](Killer_Heuristic "Killer Heuristic").

## Evaluation

Floyd's [evaluation](Evaluation "Evaluation") employs a vector of feature and weight pairs to calculate a [score](Score "Score") as [weighted sum](https://en.wikipedia.org/wiki/Weighted_sum_model). In conjunction with a draw model <a id="cite-note-5" href="#cite-ref-5">[5]</a> using [sigmoid functions](https://en.wikipedia.org/wiki/Sigmoid_function), the score is mapped to [winning probabilities](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), suited for [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") tuning.

```C++

def evaluate(board, wiloVector, drawVector):
        wiloScore = ...snip... // a weighted sum of board features
        drawScore = ...snip... // another weighted sum of board features

        return sigmoid(drawScore) * 0.5
             + sigmoid(wiloScore)
             - sigmoid(wiloScore) * sigmoid(drawScore)

```

## Misc

Floyd provides a [Python](Python "Python") [API](https://en.wikipedia.org/wiki/Application_programming_interface) for search and evaluation functions <a id="cite-note-6" href="#cite-ref-6">[6]</a> , i.e. for [automated tuning](Automated_Tuning "Automated Tuning") <a id="cite-note-7" href="#cite-ref-7">[7]</a> . It generates a compact [KPK](KPK "KPK") [tablebase](Endgame_Tablebases "Endgame Tablebases") to deal with [perfect knowledge](Knowledge#PerfectKnowledge "Knowledge"), also available as stand alone project <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a> .

## See also

- [Mathematician - Robert W. Floyd (1936 - 2001)](Mathematician#RWFloyd "Mathematician")
- [MSCP](MSCP "MSCP")
- [Rookie](Rookie "Rookie")

## Forum Posts

- [Floyd 0.5 released](http://www.talkchess.com/forum/viewtopic.php?t=57913) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), October 11, 2015
- [Floyd 0.6 released](http://www.talkchess.com/forum/viewtopic.php?t=57973) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), October 17, 2015
- [Floyd 0.7 released](http://www.talkchess.com/forum/viewtopic.php?t=58259) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), November 15, 2015
- [Floyd 0.8 released](http://www.talkchess.com/forum/viewtopic.php?t=59695) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), March 31, 2016
- [Floyd 0.9 released](http://www.open-chess.org/viewtopic.php?f=3&t=3005) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 20, 2016

## External Links

## Chess Engine

- [kervinck/floyd · GitHub](https://github.com/kervinck/floyd)
- [Download page - Floyd chess engine - /etc/marcelk](https://marcelk.net/floyd/)
- [Floyd 0.6 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&each_game=1&eng=Floyd%200.7%2064-bit#Floyd_0_7_64-bit) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Floyd from Wikipedia](https://en.wikipedia.org/wiki/Floyd)
- [Hurricane Floyd from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Floyd)
- [Robert W. Floyd from Wikipedia](https://en.wikipedia.org/wiki/Robert_W._Floyd)
- [Floyd's cycle-finding algorithm from Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)
- [Floyd–Hoare logic from Wikipedia](https://en.wikipedia.org/wiki/Hoare_logic)
- [Floyd–Steinberg dithering from Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering)
- [Floyd–Warshall algorithm from Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [Pink Floyd](Category:Pink_Floyd "Category:Pink Floyd") - [High Hopes](https://en.wikipedia.org/wiki/High_Hopes_%28Pink_Floyd_song%29), [The Division Bell](https://en.wikipedia.org/wiki/The_Division_Bell), 1994, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Hurricane Floyd near peak intensity on September 14, 1999 at 2030 UTC. This image was produced from data from [NOAA-14](https://en.wikipedia.org/wiki/Television_Infrared_Observation_Satellite#Advanced_TIROS-N), provided by [NOAA](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Hurricane Floyd from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Floyd)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Floyd 0.5 released](http://www.talkchess.com/forum/viewtopic.php?t=57913) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), October 11, 2015
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [floyd/LICENSE at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/LICENSE)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [floyd/geometry.h at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Source/geometry.h)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [floyd/drawModel.txt at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Docs/drawModel.txt)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [floyd/README.md at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/README.md)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [floyd/tune.py at master · kervinck/floyd · GitHub](https://github.com/kervinck/floyd/blob/master/Tools/tune.py)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Yet another KPK endgame table generator: pfkpk](http://www.talkchess.com/forum/viewtopic.php?t=57517) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), September 05, 2015
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [kervinck/pfkpk · GitHub](https://github.com/kervinck/pfkpk)

**[Up one Level](Engines "Engines")**

