---
title: Internal Iterative Reductions
---

used in [nodes](Node "Node") of the [search tree](Search_Tree "Search Tree") in a [iterative deepening](Iterative_Deepening "Iterative Deepening") [depth-first](Depth-First "Depth-First") [alpha-beta](Alpha-Beta "Alpha-Beta") framework, where a node has no [best move](Best_Move "Best Move") available from a previous search [PV](Principal_Variation "Principal Variation") or from the [transposition table](Transposition_Table "Transposition Table"). IIR reduces the search depth for such nodes as they are less promising, while having a worse move ordering. However, if a [hash move](Hash_Move "Hash Move") is found and the node is visited a second time, it is worth to search it the full depth. In the early implementations, IIR was only used on [PV-nodes](Node_Types#PV "Node Types"), or on every node without a [hash move](Hash_Move "Hash Move"). IIR was introduced by [Ed Schroder](Ed_Schroder "Ed Schroder") in 2020 into his engine [Rebel](Rebel "Rebel") and further improved by [Michael Chaly](Michael_Chaly "Michael Chaly") in 2021 into [Stockfish](Stockfish "Stockfish") by also having depth decrements on expected [cut-nodes](Node_Types#CUT "Node Types").

## Conditions


Where to use IIR is also an important question. Limiting the depth is an obvious condition (only use IIR if depth > 5, say). Most only use IIR in [PV-Nodes](Node_Types#PV "Node Types") and expected [cut-nodes](Node_Types#CUT "Node Types"), but some implementations use IIR on [all-nodes](Node_Types#ALL "Node Types") as well.

## See also


* [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* [Razoring](Razoring "Razoring")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Delta Pruning](Delta_Pruning "Delta Pruning")

## Forum Posts


### 2020...
* [An alternative to IID](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=74769) by [Ed Schroder](Ed_Schroder "Ed Schroder")