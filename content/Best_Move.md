---
title: Best Move
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Moves](Moves "Moves") * Best Move**

*The **Best Move** is a [Search](Search "Search") related issue.*

The **Best Move** in the context of [search algorithms](Search "Search") like [Alpha-Beta](Alpha-Beta "Alpha-Beta") or [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), is found at the [root](Root "Root") or any other confirmed [PV-node](Node_Types#PV "Node Types"). It is that move which gained the maximum score, which is [exact](Exact_Score "Exact Score") since it exceeds [alpha](Alpha "Alpha") but is still below [beta](Beta "Beta") and therefor not good enough to refute opponent's previous move, which may become his best move and part of the [principal variation](Principal_Variation "Principal Variation") as well.

## Contents

- [1 Best so far](#best-so-far)
- [2 TT-Entry](#tt-entry)
- [3 PV-Table](#pv-table)
- [4 Cut-Node](#cut-node)
- [5 All-Node](#all-node)
- [6 See also](#see-also)
- [7 Forum Posts](#forum-posts)

## Best so far

If an alpha increase occurs, the recently searched move is the best so far and needs to be stored on an explicit or implicit [stack](Stack "Stack"), which also might be the [triangular PV-Table](Triangular_PV-Table "Triangular PV-Table") if available.

## TT-Entry

After all remaining moves were searched at a PV-node, the best move found is stored inside the [transposition table](Transposition_Table "Transposition Table") together with its associated values and flags.

## PV-Table

If using a [triangular PV-table](Triangular_PV-Table "Triangular PV-Table") to [collect the principal variation](Principal_Variation#CollectionDuringSearch "Principal Variation"), one has to store the best move (so far) anyway - immediately after an alpha increase occurs, to append the PV of ply + 1, which would otherwise void while searching further.

## Cut-Node

At [Cut-nodes](Node_Types#CUT "Node Types"), if a move [fails high](Fail-High "Fail-High"), it is not necessarily the best move, but a [refutation move](Refutation_Move "Refutation Move"), good enough to refute opponents previous move. Since it is the best move found so far, in the context of transposition table, it is often flippant mentioned as best move as well.

## All-Node

At [All-nodes](Node_Types#ALL "Node Types") there is no best move found at all, despite all childs were considered if not pruned. While there is a maximum score in the arithmetical sense, all scores below or equal to [alpha](Alpha "Alpha") are [upper bounds](Upper_Bound "Upper Bound") and not comparable to determine a best move.

## See also

- [Hash Move](Hash_Move "Hash Move")
- [Killer Move](Killer_Move "Killer Move")
- [PV-Move](PV-Move "PV-Move")
- [Threat Move](Threat_Move "Threat Move") from [null move](Null_Move_Pruning "Null Move Pruning") refutations
- [Triangular PV-Table](Triangular_PV-Table "Triangular PV-Table")

## Forum Posts

- [Best move statistics](http://www.talkchess.com/forum/viewtopic.php?t=61401) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 12, 2016 » [Search Statistics](Search_Statistics "Search Statistics")
- [Update Best Score and Best Move](http://www.talkchess.com/forum/viewtopic.php?t=63948) by Tamás Kuzmics, [CCC](CCC "CCC"), May 10, 2017

**[Up one Level](Moves "Moves")**

