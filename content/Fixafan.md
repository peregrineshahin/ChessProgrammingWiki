---
title: Fixafan
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Fixafan**

\[ Fan Moved by Mechanism <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Fixafan**, (Fix a Fan)

the thesis chess program by [Eric Thé](Eric_Th%C3%A9 "Eric Thé"), published in appendix D of his 1992 Master's thesis as subject of an analysis of [move ordering](Move_Ordering "Move Ordering") on the efficiency of [alpha-beta](Alpha-Beta "Alpha-Beta") search. Fixafan was written in [C](C "C") on a [Solbourne 5/600](https://en.wikipedia.org/wiki/Solbourne_Computer) dual [SPARC](SPARC "SPARC") processor machine running [Unix](Unix "Unix"). It used a two-dimensional [8x8 board](8x8_Board "8x8 Board") array, and, focusing on move ordering, a [material](Material "Material") only [evaluation](Evaluation "Evaluation"), and [iterative deepening](Iterative_Deepening "Iterative Deepening") with [aspiration windows](Aspiration_Windows "Aspiration Windows") of ± 2 pawns <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Move Ordering](#move-ordering)
- [2 Experiments](#experiments)
- [3 Results](#results)
- [4 Publications](#publications)
- [5 External Links](#external-links)
- [6 References](#references)

## Move Ordering

Eight [move ordering](Move_Ordering "Move Ordering") heuristics were implemented and examined, in isolation and combination - beside the chess dependent [MVV/LVA](MVV-LVA "MVV-LVA")  ordering of [captures](Captures "Captures"), seven variations of the [killer heuristic](Killer_Heuristic "Killer Heuristic"), aka [countermove heuristic](Countermove_Heuristic "Countermove Heuristic") or [history heuristic](History_Heuristic "History Heuristic"), including the [best move](Best_Move "Best Move") probed from the [transposition table](Transposition_Table "Transposition Table") (BEST_TT). Opposed to static move ordering applied during [generation](Move_Generation "Move Generation") time, dynamic move ordering heuristic reorders remaining moves after searching early ones, by looking whether new killers appeared two plies ahead, still to try inside the [movelist](Move_List "Move List"), now considering next.

## Experiments

The experiments were made using the 24 positions of the [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test") searching on the depth of 6 or 7 (midgame) and 9 (endgame) plies, comparing performance by measuring of [node](Node "Node") counts, CPU time, [average branching factor](Branching_Factor "Branching Factor") (ABF), and a "Killer average" (KA), which is the ratio of number of "kills" versus number of reordered nodes per level. A kill is when a [cutoff](Beta-Cutoff "Beta-Cutoff") occurs within the subset of moves reordered at a node. If a certain heuristic or combination of heuristics reordered N moves at the front of a node's movelist, and a cutoff occurs after searching one of the N moves, then a kill is registered. One should consider the fact that Fixafan evaluates only material balance at all [leaf nodes](Leaf_Node "Leaf Node"), and therefor the last level of all iterations is not expanded and searched thoroughly as with all previous levels. Instead, the highest capture is immediately taken as the best move and all other moves are ignored. The consequence of this shortcut is that the ABF for the last level of every iteration can never exceed 1.00.

## Results

BEST_TT was clearly the most effective heuristic reducing the tree size by 70% and search time by 75% on average compared to a null test (no ordering heuristic at all, quiet sliding moves generated before captures), followed by MVV/LVA captures, which also raises the efficiency when combined with any of the other heuristics not dependent on the properties of chess. The history heuristic consumed just 4.5% less execution time than the null test. Although HH had a high Killer average, most of the cutoffs seemed to happen too late to be effective. Small improvements in BEST_TT + Captures were noticed when complemented with countermove and the level dependent killer heuristic. Using two killer slots was slightly advantageous, while dynamic re-ordering reduced the tree size with disappointing time results.

## Publications

- [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University"), advisor [Monroe Newborn](Monroe_Newborn "Monroe Newborn")

## External Links

- [Fix from Wikipedia](https://en.wikipedia.org/wiki/Fix)
- [fix - Wiktionary](https://en.wiktionary.org/wiki/fix)
- [Fan from Wikipedia](https://en.wikipedia.org/wiki/Fan)
- [Fan-out from Wikipedia](https://en.wikipedia.org/wiki/Fan-out)
- [fan - Wiktionary](https://en.wiktionary.org/wiki/fan)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Patent drawing](https://commons.wikimedia.org/wiki/File:Patent,_Mechanical_Fan,_1830.png) of Fan Moved by Mechanism by [James Barron](http://ead.lib.virginia.edu/vivaxtf/view?docId=wm/viw00021.xml), November 27, 1830. The original drawing for this patent was destroyed by a fire in the Patent Office in 1836. The coverage date is the original patent date. This drawing is a restoration created in 1837 or shortly thereafter, [Mechanical fan from Wikipedia](https://en.wikipedia.org/wiki/Mechanical_fan), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University"), advisor [Monroe Newborn](Monroe_Newborn "Monroe Newborn")

**[Up one Level](Engines "Engines")**

