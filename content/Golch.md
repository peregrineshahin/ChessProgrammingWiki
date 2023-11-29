---
title: Golch
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Golch**

\[ Perceptron <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Golch**,

an experimental chess engine by [Artem Pyatakov](Artem_Petakov "Artem Petakov"). Initially written in early 2001 <a id="cite-note-2" href="#cite-ref-2">[2]</a> during his [freshman](https://en.wikipedia.org/wiki/Freshman) year at [Princeton University](https://en.wikipedia.org/wiki/Princeton_University), it was a conventional chess program written in [C](C "C"), using a [0x88](0x88 "0x88") [board representation](Board_Representation "Board Representation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, [alpha-beta](Alpha-Beta "Alpha-Beta"), [iterative deepening](Iterative_Deepening "Iterative Deepening"), [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [killer-](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic"), along with all the domain dependent tricks in [move ordering](Move_Ordering "Move Ordering") (i.e searching [captures](Captures "Captures") first), [selectivity](Selectivity "Selectivity") and [evaluation](Evaluation "Evaluation"). In 2001, Golch was active at [ICC](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") <a id="cite-note-5" href="#cite-ref-5">[5]</a>. The program was later used as test-bed for Pyatakov's [senior thesis](https://en.wikipedia.org/wiki/Thesis#United_States) *Improving Computer Chess through Machine Learning* <a id="cite-note-6" href="#cite-ref-6">[6]</a> under advisor [Robert Schapire](Robert_Schapire "Robert Schapire") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. The aim was to narrow the claimed gap between [artificial intelligence](Artificial_Intelligence "Artificial Intelligence") methods and computer chess methods and tricks, manifested as human-generated, domain dependent ideas that happened to work without a good theoretical justification and cannot be easily generalized to other games <a id="cite-note-8" href="#cite-ref-8">[8]</a>.

## Perceptron

The [online-learning](Learning "Learning") approach to replace classical evaluation by a [single layer perceptron](Neural_Networks#Perceptron "Neural Networks"), combining a [feature vector](https://en.wikipedia.org/wiki/Feature_vector), [representing the board](Board_Representation "Board Representation"), with a set of adjustable weights, trained by [supervised move adaption](Automated_Tuning#SupervisedLearning "Automated Tuning") with some [test-positions](Test_Positions "Test-Positions") such as the [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test") produced slightly disappointing results. The feature-vector used had 64 binary elements of an [occupied bitboard](Occupancy "Occupancy"), and a 16x16 [attack map](Attack_and_Defend_Maps "Attack and Defend Maps") <a id="cite-note-9" href="#cite-ref-9">[9]</a>, which hopefully distinguished attacked but sufficiently defended pieces or pawns from pieces or pawns [en prise](En_prise "En prise").

## History Heuristic

More promising results was due to an advanced implementaion of [history heuristic](History_Heuristic "History Heuristic"), where a table was not only indexed by its \[from\]\[to\] coordinates of a move, but a much larger table with additional context of the moving piece along with a bitmask of pieces attacking the from square, which was reported to work about 3% better than the pure history heuristic in terms of node counts on the [Bratko-Kopec problems](Bratko-Kopec_Test "Bratko-Kopec Test") <a id="cite-note-10" href="#cite-ref-10">[10]</a>:

```C++
history[piece][from][to][attack_bit_vector] += (1 << depth);

```

## See also

- [Chess Engines with Neural Networks](Neural_Networks#engines "Neural Networks")
- [Learning Chess Programs](Learning#Programs "Learning")
- [NeuroChess](NeuroChess "NeuroChess")
- [SAL](SAL "SAL")

## Publications

- [Artem Pyatakov](Artem_Petakov "Artem Petakov") (**2004**). *Improving Computer Chess through Machine Learning*. Senior thesis, [Princeton University](https://en.wikipedia.org/wiki/Princeton_University), advisor [Robert Schapire](Robert_Schapire "Robert Schapire") <a id="cite-note-11" href="#cite-ref-11">[11]</a>

## Forum Posts

- [Fastest Conversion from 0x88 board to 8x8 board representation](https://www.stmintz.com/ccc/index.php?id=178465) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 06, 2001 » [0x88](0x88 "0x88")
- [Question about Gerbil](https://www.stmintz.com/ccc/index.php?id=179247) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 11, 2001
- [Bitfields and Crafty](https://www.stmintz.com/ccc/index.php?id=179328) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 11, 2001
- [Artificial Intelligence in Computer Chess](https://www.stmintz.com/ccc/index.php?id=357095) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004 » [Artificial Intelligence](Artificial_Intelligence "Artificial Intelligence")
- [Re: Artificial Intelligence in Computer Chess - \*DETAILS\* as promised](https://www.stmintz.com/ccc/index.php?id=357112) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004 » [History Heuristic](History_Heuristic "History Heuristic")
- [Killer modifications reduced tree size by 8% (with identical results)](https://www.stmintz.com/ccc/index.php?id=357640) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 31, 2004 » [Killer Heuristic](Killer_Heuristic "Killer Heuristic")

## External Links

- [Finger golch](http://www6.chessclub.com/finger/golch) at [Internet Chess Club](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The appropriate weights are applied to the inputs, and the resulting weighted sum passed to a function that produces the output y, image created by [mat_the_w](https://en.wikipedia.org/wiki/User:Mat_the_w), based on [raster image](https://en.wikipedia.org/wiki/Raster_graphics) [Perceptron.gif](http://commons.wikimedia.org/wiki/File:Perceptron.gif) by '[Paskari](https://en.wikipedia.org/wiki/User:Paskari)', using [Inkscape](https://en.wikipedia.org/wiki/Inkscape) 0.46 for [OSX](Mac_OS "Mac OS"), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Perceptron from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Question about Gerbil](https://www.stmintz.com/ccc/index.php?id=179247) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 11, 2001
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Fastest Conversion from 0x88 board to 8x8 board representation](https://www.stmintz.com/ccc/index.php?id=178465) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 06, 2001
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Question about Gerbil](https://www.stmintz.com/ccc/index.php?id=179247) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), July 11, 2001
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Finger golch](http://www6.chessclub.com/finger/golch) at [Internet Chess Club](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Artificial Intelligence in Computer Chess](https://www.stmintz.com/ccc/index.php?id=357095) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Princeton - Independent Project Presentation Schedule](http://www.cs.princeton.edu/~rywang/03fIND/iw_sched.html)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Artificial Intelligence in Computer Chess](https://www.stmintz.com/ccc/index.php?id=357095) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Artificial Intelligence in Computer Chess - \*DETAILS\* as promised](https://www.stmintz.com/ccc/index.php?id=357112) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Artificial Intelligence in Computer Chess - \*DETAILS\* as promised](https://www.stmintz.com/ccc/index.php?id=357112) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Artificial Intelligence in Computer Chess](https://www.stmintz.com/ccc/index.php?id=357095) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 28, 2004

**[Up one level](Engines "Engines")**

