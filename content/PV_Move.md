---
title: PV Move
---

**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* PV-Move**

A **PV-Move** is part of the [principal variation](Principal_Variation "Principal Variation") and therefor a [best move](Best_Move "Best Move") found in the previous [iteration](Iteration "Iteration") of an [Iterative deepening](Iterative_Deepening "Iterative Deepening") framework. It is either a [hash move](Hash_Move "Hash Move") of a stored [PV-node](Node_Types#PV "Node Types") inside the [transposition table](Transposition_Table "Transposition Table"), or - if a [triangular PV-Table](Triangular_PV-Table "Triangular PV-Table") is applied, a move from that [array](Array "Array").

While starting a new iteration, the most important [move ordering](Move_Ordering "Move Ordering") technique is to try PV-Moves first at [leftmost PV-nodes](Leftmost_Node "Leftmost Node").

## See also

- [Hash Move](Hash_Move "Hash Move")
- [Killer Move](Killer_Move "Killer Move")
- [Mate Killers](Mate_Killers "Mate Killers")
- [Move Ordering](Move_Ordering "Move Ordering")
- [PV Extensions](PV_Extensions "PV Extensions")
- [Threat Move](Threat_Move "Threat Move") from [null move](Null_Move_Pruning "Null Move Pruning") refutations

## Forum Posts

- [Best move from previous iteration first: still needed with TT?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76888) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021 » [Hash Move](Hash_Move "Hash Move")
- [PV-move ordering necessary if you have TT-move ordering?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77593) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), July 01, 2021

**[Up one Level](Moves "Moves")**

Retrieved from "[https://www.chessprogramming.org/index.php?title=PV-Move&oldid=25456](https://www.chessprogramming.org/index.php?title=PV-Move&oldid=25456)"
