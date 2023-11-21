---
title: Hash Move
---

**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Hash Move**

The **Hash Move** is a move probed from the [transposition table](Transposition_Table "Transposition Table"), either a [best move](Best_Move "Best Move") of a stored [PV-node](Node_Types#pv-node "Node Types") - a [PV-move](PV-Move "PV-Move"), or a good enough [refutation move](Refutation_Move "Refutation Move") to cause a [cutoff](Beta-Cutoff "Beta-Cutoff"). This move should most importantly searched first <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>. One may save the [move generation](Move_Generation "Move Generation") at all, if the hash move actually [fails high](Fail-High "Fail-High"). To guard against rare [TT key collisions](Transposition_Table#KeyCollisions "Transposition Table"), one may apply a [legality test](Legal_Move "Legal Move") of the hash move <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [Best Move](Best_Move "Best Move")
- [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Killer Move](Killer_Move "Killer Move")
- [Mate Killers](Mate_Killers "Mate Killers")
- [Move Ordering](Move_Ordering "Move Ordering")
- [Null Move](Null_Move "Null Move")
- [Pseudo-Legal Move](Pseudo-Legal_Move "Pseudo-Legal Move")
- [PV-Move](PV-Move "PV-Move")
- [Refutation Move](Refutation_Move "Refutation Move")
- [Threat Move](Threat_Move "Threat Move") from [null move](Null_Move_Pruning "Null Move Pruning") refutations
- [Transposition Table](Transposition_Table "Transposition Table")

[Collisions](Transposition_Table#Collisions "Transposition Table")

## Forum Posts

- [TTMove legality checking ? & Killers Move Format?](http://www.talkchess.com/forum/viewtopic.php?t=63090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 08, 2017 » [Killer Move](Killer_Move "Killer Move")
- [tt move vs null move](http://www.talkchess.com/forum/viewtopic.php?t=64093) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 27, 2017 » [Null Move](Null_Move "Null Move"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Marginal hash move](http://www.talkchess.com/forum/viewtopic.php?t=65189) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 16, 2017
- [Hash move ordering vs. Hash cuts: savings in number of nodes visited](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76887) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021
- [Best move from previous iteration first: still needed with TT?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76888) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 16, 2021 » [PV-Move](PV-Move "PV-Move")
- [PV-move ordering necessary if you have TT-move ordering?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77593) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), July 01, 2021

## References

1.  <a id="cite-ref-1" href="#cite-note-1">↑</a> but usually after trying the [Null Move](Null_Move "Null Move") of the [Null Move Heuristic](Null_Move_Pruning "Null Move Pruning")
2.  <a id="cite-ref-2" href="#cite-note-2">↑</a> [tt move vs null move](http://www.talkchess.com/forum/viewtopic.php?t=64093) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), May 27, 2017
3.  <a id="cite-ref-3" href="#cite-note-3">↑</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie") (**2005**). _[The Effect of Hash Signature Collisions in a Chess Program](http://www.cis.uab.edu/hyatt/collisions.html)_. [ICGA Journal, Vol. 28., No. 3](ICGA_Journal "ICGA Journal")

**[Up one Level](Moves "Moves")**
