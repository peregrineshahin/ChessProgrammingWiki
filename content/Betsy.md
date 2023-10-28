---
title: Betsy
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Betsy**

\[ Hurricane Betsy <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Betsy**,

a [WinBoard](WinBoard "WinBoard") compatible chess engine by [Landon Rabern](Landon_Rabern "Landon Rabern"), written in [C](C "C") with a little [Assembly](Assembly "Assembly"), released in September 2000 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Originally written in [Pascal](Pascal "Pascal") with its own [text interface](CLI "CLI") it was rewritten in C using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards"). Betsy applies [PVS](Principal_Variation_Search "Principal Variation Search") with [null move pruning](Null_Move_Pruning "Null Move Pruning"), and various standard and some aggressive non-standard [extensions](Extensions "Extensions") and [reductions](Reductions "Reductions").
According to a former [Arena](Arena "Arena") site, Betsy was the first published chess engine able to play [Chess960](Chess960 "Chess960") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, and was therefore Arena partner engine.

## Contents

- [1 Neural Networks](#neural-networks)
- [2 C# Port](#c.23-port)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Neural Networks

Quote by [Landon Rabern](Landon_Rabern "Landon Rabern") <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```
As a child, I was obsessed with machine intelligence. I coded a strong chess AI (codenamed Betsy) and experimented with using [neural networks](Neural_Networks "Neural Networks") in Betsy, both for the [static evaluation](Evaluation "Evaluation") at [leaf nodes](Leaf_Node "Leaf Node") and within the [tree](Search_Tree "Search Tree") for [pruning](Pruning "Pruning"). The networks learned from self-play to get about as good as my hand-tuned functions (discounting the slowdown incurred by [sigmoid evaluation](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")). I concluded that to do better, I would need to use raw game state data instead of the set of features I preselected as network inputs; unfortunately, this was 2000 and I did not have nearly enough processing power to do so.

```

## C# Port

As of 2014, Landon Rabern started to port Betsy to [C#](C_sharp "C sharp"), available as [open source engine](Category:Open_Source "Category:Open Source") under the [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") at [GitHub](https://en.wikipedia.org/wiki/GitHub).
All the major components of a chess engine are there, just not a tuned [evaluation](Evaluation "Evaluation") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.
The board class embeds an [8x8 board](8x8_Board "8x8 Board") and the [Bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition"), and implements [rotated bitboards](Rotated_Bitboards "Rotated Bitboards").
The [search](Search "Search") is implemented using a derivation chain of classes, the abstract base *Brain*, *TranspositionTableBrain* ([Transposition Table](Transposition_Table "Transposition Table"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")), and the concrete *BasicAlphaBetaBrain* ([Alpha-Beta](Alpha-Beta "Alpha-Beta")), *NullMoveBrain* ([Null Move Pruning](Null_Move_Pruning "Null Move Pruning")) and *MTDfBrain* ([MTD(f)](</MTD(f)> "MTD(f)")) classes.

## Forum Posts

- [Re: C or C++ for Chess Programming?](https://www.stmintz.com/ccc/index.php?id=125117) by [Landon Rabern](Landon_Rabern "Landon Rabern"), [CCC](CCC "CCC"), August 18, 2000
- [Betsy 5.0 is now winboard compatable](https://www.stmintz.com/ccc/index.php?id=128512) by [Landon Rabern](Landon_Rabern "Landon Rabern"), [CCC](CCC "CCC"), September 06, 2000
- [Betsy 5.26](https://www.stmintz.com/ccc/index.php?id=178491) by [Landon Rabern](Landon_Rabern "Landon Rabern"), [CCC](CCC "CCC"), July 06, 2001
- [Re: FRC_TheBaron_101 Vs Fritz8 (Castling vs Not Castling rules)](https://www.stmintz.com/ccc/index.php?id=302797) by [Landon Rabern](Landon_Rabern "Landon Rabern"), [CCC](CCC "CCC"), June 24, 2003
- [Betsy in Arena](https://www.stmintz.com/ccc/index.php?id=315727) by Mark Loftus, [CCC](CCC "CCC"), September 13, 2003
- [Betsy 6.5.1 by Landon Rabern](http://www.talkchess.com/forum/viewtopic.php?t=23156) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), August 21, 2008

## External Links

## Chess Engine

- [Index of /chess/engines/Norbert's Collection/Betsy](http://kirr.homeunix.org/chess/engines/Norbert%27s%20Collection/Betsy%20%5B-xboard%2032%5D%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Betsy](https://web.archive.org/web/20131109133342/http://wbec-ridderkerk.nl/html/details1/Betsy.html) from [WBEC Ridderkerk](WBEC "WBEC") ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
- [Betsy 6.51 Nobook](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Betsy%206.51%20Nobook) in [CCRL 40/2](CCRL "CCRL")
- [landon rabern - about](https://landon.github.io/#about)
- [Betsy Fischer](http://www.computerchess.org.uk/ccrl/404FRC/cgi/engine_details.cgi?print=Details&eng=Betsy%20Fischer#Betsy_Fischer) in [CCRL 40/4 FRC](CCRL "CCRL")
- [GitHub - landon/Chess: Beginnings of a port of Betsy to C#](https://github.com/landon/Chess)

## Misc

- [Betsy from Wikipedia](https://en.wikipedia.org/wiki/Betsy)
- [Betsy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Betsy_%28disambiguation%29)
- [Betsy (dog) from Wikipedia](https://en.wikipedia.org/wiki/Betsy_%28dog%29)
- [Hurricane Betsy from Wikipedia](https://en.wikipedia.org/wiki/Hurricane_Betsy)
- [Tropical Storm Betsy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Tropical_Storm_Betsy_%28disambiguation%29)
- [Bitch](<https://en.wikipedia.org/wiki/Bitch_(band)>) - [You Want It You Got It (Betsy Album)](<https://en.wikipedia.org/wiki/Betsy_(Bitch_album)>) (1988), [YouTube](http://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Hurricane Betsy](https://en.wikipedia.org/wiki/Hurricane_Betsy) in the [Gulf of Mexico](https://en.wikipedia.org/wiki/Gulf_of_Mexico) in September of 1965 as taken by the [TIROS-8](https://en.wikipedia.org/wiki/Television_Infrared_Observation_Satellite) weather satellite. Source: [NOAA](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration) [Photo Library](http://www.photolib.noaa.gov/), September 4, 1965
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Betsy](https://web.archive.org/web/20131109133342/http://wbec-ridderkerk.nl/html/details1/Betsy.html) from [WBEC Ridderkerk](WBEC "WBEC") ([Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive))
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Der Chess960-Express ist nicht mehr aufzuhalten](https://chess-tigers.de/index_news.php?id=308&rubrik=4&PHPSESSID=d71dfe17e7e8aae16adce6f8fb284410), [Chess Tigers Training Center](https://chess-tigers.de/cttc_main.php?rubrik=7), July 20, 2005 (German)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [landon rabern - about](https://landon.github.io/#about) (2019)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GitHub - landon/Chess: Beginnings of a port of Betsy to C#](https://github.com/landon/Chess)

**[Up one Level](Engines "Engines")**

