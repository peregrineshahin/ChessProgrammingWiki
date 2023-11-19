---
title: Internal Iterative Reductions
---

**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Reductions](Reductions "Reductions") \* Internal Iterative Reductions**

it is an idea first introduced by [Ed Schroder](Ed_Schroder "Ed Schroder") into his engine [Rebel](Rebel "Rebel") in 2020. It is used as a replacement or in conjunction with [Internal Iterative Deepening](Internal_Iterative_Deepening), although the name is a bit of a misnomer.

[Internal Iterative Deepening](Internal_Iterative_Deepening) (IID) and [Internal Iterative Reductions](Internal_Iterative_Reductions) (IIR) are both meant to handle nodes where no [hash move](Hash_Move "Hash Move") is found. IID would attempt to fix this by running an internal, reduced depth search. However, IIR instead opts to simply reduce the depth of the entire node, in the hope that the node must not be very important as there was no hash move present. In early implementations, IIR was used on all types of nodes (in the case of [Rebel](Rebel "Rebel")) and only on [PV-nodes](Node_Types#pv-node "Node Types") (in the case of [Stockfish](Stockfish "Stockfish")). However, in 2021, genius [Michael Chaly](Michael_Chaly "Michael Chaly") revolutionized IIR forever by also having depth decrements on expected [cut-nodes](Node_Types#cut-nodes "Node Types"), which was introduced into [Stockfish](Stockfish "Stockfish"), and later adapted by [Ethereal](Ethereal). There is also an idea of reducing depth by more if the node has been searched before at a depth greater than or equal to current depth, but yet no [hash move](Hash_Move "Hash Move") is found.

## Conditions


Where to use IIR is also an important question. Limiting the depth is an obvious condition (only use IIR if depth > 5, say). Most only use IIR in [PV-Nodes](Node_Types#pv-node "Node Types") and expected [cut-nodes](Node_Types#cut-nodes "Node Types"), but some implementations use IIR on [all-nodes](Node_Types#all-nodes "Node Types") as well.

## See also


* [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
* [Razoring](Razoring "Razoring")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Delta Pruning](Delta_Pruning "Delta Pruning")

## Forum Posts
### 2020...
* [An alternative to IID](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=74769) by [Ed Schroder](Ed_Schroder "Ed Schroder")