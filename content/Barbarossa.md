---
title: Barbarossa
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Barbarossa**

\[ Barbarossa <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Barbarossa**,

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), first released in Fall 2013 as successor of [Abulafia](Abulafia "Abulafia")
<a id="cite-note-2" href="#cite-ref-2">[2]</a> , both written in [Haskell](index.php?title=Haskell&action=edit&redlink=1 "Haskell (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
<a id="cite-note-4" href="#cite-ref-4">[4]</a>.
It uses [bitboards](Bitboards "Bitboards") to [represent the board](Board_Representation "Board Representation"),
and [magic bitboards](Magic_Bitboards "Magic Bitboards") <a id="cite-note-5" href="#cite-ref-5">[5]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks").
Barbarossa applies an [alpha-beta](Alpha-Beta "Alpha-Beta") search <a id="cite-note-6" href="#cite-ref-6">[6]</a> utilizing a [transposition table](Transposition_Table "Transposition Table") indexed by [Zobrist keys](Zobrist_Hashing "Zobrist Hashing"), and uses the [functional programming](https://en.wikipedia.org/wiki/Functional_programming) concept of [monad transformers](https://en.wikipedia.org/wiki/Monad_%28functional_programming%29) <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a> in [continuation passing style](https://en.wikipedia.org/wiki/Continuation-passing_style) to control the [search](Search "Search").
Some [evaluation](Evaluation "Evaluation") parameters were [tuned](Automated_Tuning "Automated Tuning") by [Rémi Coulom's](R%C3%A9mi_Coulom "Rémi Coulom") [CLOP](CLOP "CLOP"), and more recently by [MMTO](Minimax_Tree_Optimization "Minimax Tree Optimization") as introduced by [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki") and [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") in the domain of [Shogi](Shogi "Shogi") <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a>. Discrete [SPSA](SPSA "SPSA") (DSPSA), introduced by [Qi Wang](index.php?title=Qi_Wang&action=edit&redlink=1 "Qi Wang (page does not exist)") <a id="cite-note-11" href="#cite-ref-11">[11]</a> was applied in pawn evaluation tuning <a id="cite-note-12" href="#cite-ref-12">[12]</a> .

## See also

- [Abulafia](Abulafia "Abulafia")

## Forum Posts

## 2012 ...

- [Abulafia, chess, Haskell and some (new?) ideas](http://www.talkchess.com/forum/viewtopic.php?t=43384) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
- [Barbarossa 0.1.0](http://www.talkchess.com/forum/viewtopic.php?t=50213) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), November 24, 2013
- [New release of Barbarossa](http://www.talkchess.com/forum/viewtopic.php?t=55423) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), February 22, 2015
- [Barbarossa 0.3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=57859) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), October 06, 2015
- [Barbarossa-0.4.0 release](http://www.talkchess.com/forum/viewtopic.php?t=62547) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), December 20, 2016
- [Barbarossa 0.5.0 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69923) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), February 16, 2019

## 2020 ...

- [Barbarossa: new release 0.6.0](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77216) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), May 01, 2021

## External Links

## Chess Engine

- [nionita/Barbarossa · GitHub](https://github.com/nionita/Barbarossa)
- [Barbarossa](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Barbarossa&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Barbarossa - Wiktionary](https://en.wiktionary.org/wiki/Barbarossa)
- [Redbeard from Wikipedia](https://en.wikipedia.org/wiki/Redbeard)
- [Barbarossa from Wikipedia](https://en.wikipedia.org/wiki/Barbarossa)
- [Frederick Barbarossa from Wikipedia](https://en.wikipedia.org/wiki/Frederick_I,_Holy_Roman_Emperor)
- [King in the mountain from Wikipedia](https://en.wikipedia.org/wiki/King_in_the_mountain)
- [Barbarossa city from Wikipedia](https://en.wikipedia.org/wiki/Barbarossa_city)
- [Barbarossa Monument from Wikipedia](https://en.wikipedia.org/wiki/Kyffh%C3%A4user_Monument)
- [Oruç Reis from Wikipedia](https://en.wikipedia.org/wiki/Oru%C3%A7_Reis)
- [Hayreddin Barbarossa from Wikipedia](https://en.wikipedia.org/wiki/Hayreddin_Barbarossa)
- [Operation Barbarossa from Wikipedia](https://en.wikipedia.org/wiki/Operation_Barbarossa)
- [The Man from Barbarossa - Wikipedia](https://en.wikipedia.org/wiki/The_Man_from_Barbarossa)
- [Barbarossa (board game) from Wikipedia](https://en.wikipedia.org/wiki/Barbarossa_%28board_game%29) by [Klaus Teuber](https://en.wikipedia.org/wiki/Klaus_Teuber)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Bust of [Friedrich I., "Barbarossa"](https://en.wikipedia.org/wiki/Frederick_I,_Holy_Roman_Emperor), [gilded](https://en.wikipedia.org/wiki/Gilding) [bronze](https://en.wikipedia.org/wiki/Bronze), ca. 1160, given to his godfather Count [Otto of Cappenberg](https://de.wikipedia.org/wiki/Otto_von_Cappenberg) in 1171. It was used as a reliquary in [Cappenberg Abbey](https://en.wikipedia.org/wiki/Cappenberg_Castle), [St. Johannes Evangelist Church](http://de.wikipedia.org/wiki/St._Johannes_Evangelist_%28Cappenberg%29), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Barbarossa 0.1.0](http://www.talkchess.com/forum/viewtopic.php?t=50213) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), November 24, 2013
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Abulafia, chess, Haskell and some (new?) ideas](http://www.talkchess.com/forum/viewtopic.php?t=43384) by [Nicu Ionita](Nicu_Ionita "Nicu Ionita"), [CCC](CCC "CCC"), April 20, 2012
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Haskell (programming language) from Wikipedia](https://en.wikipedia.org/wiki/Haskell_%28programming_language%29)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Barbarossa/Magics.hs at master · nionita/Barbarossa · GitHub](https://github.com/nionita/Barbarossa/blob/master/Moves/Magics.hs)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Barbarossa/Albeta.hs at master · nionita/Barbarossa · GitHub](https://github.com/nionita/Barbarossa/blob/master/Search/Albeta.hs)
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Haskell/Monad transformers - Wikibooks](http://en.wikibooks.org/wiki/Haskell/Monad_transformers)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Haskell/Understanding monads - Wikibooks](http://en.wikibooks.org/wiki/Haskell/Understanding_monads)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2014**). *[Large-Scale Optimization for Evaluation Functions with Minimax Search](https://www.jair.org/papers/paper4217.html)*. [JAIR Vol. 49](https://www.jair.org/vol/vol49.html), [pdf](https://www.jair.org/media/4217/live-4217-7792-jair.pdf)
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [MMTO for evaluation learning](http://www.talkchess.com/forum/viewtopic.php?t=55084) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 25, 2015
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Qi Wang](index.php?title=Qi_Wang&action=edit&redlink=1 "Qi Wang (page does not exist)") (**2013**). *[Optimization with Discrete Simultaneous Perturbation Stochastic Approximation Using Noisy Loss Function Measurements](https://jscholarship.library.jhu.edu/handle/1774.2/36955)*. Ph.D. thesis, [Johns Hopkins University](https://en.wikipedia.org/wiki/Johns_Hopkins_University), advisor [James C. Spall](James_C._Spall "James C. Spall")
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [DSPSA eval weights for pawns · nionita/Barbarossa@b9ba4de · GitHub](https://github.com/nionita/Barbarossa/commit/b9ba4de3e3e324e2461a373c00b51f7651a514d9)

**[Up one level](Engines "Engines")**

