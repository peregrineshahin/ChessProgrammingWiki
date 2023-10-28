---
title: AICE
---
**[Home](Home "Home") * [Engines](Engines "Engines") * AICE**

[](http://users.sch.gr/amilikas/?page_id=16) AICE Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**AICE**,

a free [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant chess engine by [Anastasios Milikas](Anastasios_Milikas "Anastasios Milikas"), written in [C++](Cpp "Cpp") using the [Standard Template Library](Cpp#Libraries "Cpp"), with [Windows](Windows "Windows") and [Linux](Linux "Linux") binaries available <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
AICE is an [Arena](Arena "Arena") partner engine and able to play [Chess960](Chess960 "Chess960"). AICE participated at the two open [Livingston Chess960 Computer World Championships](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), the [Chess960CWC 2005](Chess960CWC_2005 "Chess960CWC 2005") and the [Chess960CWC 2006](Chess960CWC_2006 "Chess960CWC 2006").

## Contents

- [1 Etymology](#etymology)
- [2 Features](#features)
- [3 Forum Posts](#forum-posts)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc)
- [5 References](#references)

## Etymology

AICE stands for ***A**rtificially **I**ntelligent **C**hess **E**ngine*, as explained by Anastasios, who also remarked "This is probably not a good name, since the engine is not intelligent! But I am working on it…” <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Anastasios initial intention with AICE was to use [neural networks](Neural_Networks "Neural Networks") and [genetic algorithms](Genetic_Programming#GeneticAlgorithm "Genetic Programming") in order to [optimize its evaluation weights](Automated_Tuning "Automated Tuning"), but he found that this was not productive and suitable for a chess [evaluation function](Evaluation_Function "Evaluation Function"). They might be useful in [time management](Time_Management "Time Management"), or controlling extensions or reductions <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Features

AICE is a [bitboard](Bitboards "Bitboards") based [PV searcher](Principal_Variation_Search "Principal Variation Search") with [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") in none [PV-Nodes](Node_Types#PV "Node Types"), using [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [history-](History_Heuristic "History Heuristic") and [killer heuristic](Killer_Heuristic "Killer Heuristic") to improve [move ordering](Move_Ordering "Move Ordering"), and [fractional extensions](Extensions#FractionalExtensions "Extensions") and non recursive [reductions](Reductions "Reductions") based on [evaluation](Evaluation "Evaluation") and history. In version 0.73, [fail-high reductions](Fail-High_Reductions "Fail-High Reductions") were implemented in addition to null move pruning, but removed in in 0.97. Beside the [transposition table](Transposition_Table "Transposition Table") and a smaller [hash table](Hash_Table "Hash Table") for the [quiescence search](Quiescence_Search "Quiescence Search"), AICE maintains a [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") to cache once calculated [pawn structure](Pawn_Structure "Pawn Structure") related data.

## Forum Posts

- [AICE 0.85](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1093) by [milix](Anastasios_Milikas "Anastasios Milikas"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 21, 2004
- [AICE 0.86](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1191) by [milix](Anastasios_Milikas "Anastasios Milikas"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2004
- [Cycle VI-2005 6. Bundesliga result and games - AICE !](https://www.stmintz.com/ccc/index.php?id=438205) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), July 24, 2005
- [Aice 0.96 Linux: confused by a draw offer](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5351) by [Volker Pittlik](index.php?title=Volker_Pittlik&action=edit&redlink=1 "Volker Pittlik (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 10, 2006
- [AICE 0.99.2](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=5455) by [milix](Anastasios_Milikas "Anastasios Milikas"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 25, 2006

## External Links

## Chess Engine

- [milix AICE chess engine for both UCI and Winboard](http://users.sch.gr/amilikas/?page_id=16)
- [Aice 0.99.2](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Aice%200.99.2#Aice_0_99_2) in [CCRL 40/40](CCRL "CCRL")
- [AICE 0.99.2](http://kirr.homeunix.org/chess/kcec/cgi/engine_details.cgi?print=Details&match_length=20&eng=AICE+0.99.2) in [KCEC](KCEC "KCEC")

## Misc

- [aice - Wiktionary](https://en.wiktionary.org/wiki/aice)
- [AICE (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/AICE)
- [Advanced International Certificate of Education (AICE) from Wikipedia](https://en.wikipedia.org/wiki/Advanced_International_Certificate_of_Education)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [milix AICE chess engine for both UCI and Winboard](http://users.sch.gr/amilikas/?page_id=16)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [milix AICE chess engine for both UCI and Winboard](http://users.sch.gr/amilikas/?page_id=16)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Portrait of Anastasios Mikilas, author of the Chess960 engine AICE](http://www.chesstigers.de/ccm9_index_news.php?id=310&rubrik=6&lang=1&kat=6) by [Mark Vogelgesang](http://www.chesstigers.de/index_news.php?id=594&rubrik=), July 21, 2005
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Interview with the programmer of AICE](http://www.playwitharena.com/?Newsticker:Archive_8) by [Alexander Schmidt](index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)") and [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Arena Chess GUI 3.0](Arena "Arena") - Archive 8, 118, April 27, 2005

**[Up one Level](Engines "Engines")**

