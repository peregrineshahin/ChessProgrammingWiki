---
title: Killer Move
---

**[Home](Main_Page "Main Page") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Killer Move**

The **Killer Move** is a [quiet move](Quiet_Moves "Quiet Moves") which caused a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") in a sibling [Cut-node](Node_Types#CUT "Node Types"), or any other earlier branch in the [tree](Search_Tree "Search Tree") with the same [ply](Ply "Ply") distance to the [root](Root "Root"). The [rule of thumb](https://en.wikipedia.org/wiki/Rule_of_thumb) is to try that move early direct after a possibly available [hash move](Hash_Move "Hash Move") from the [transposition table](Transposition_Table "Transposition Table") and considering apparently winning [captures](Captures "Captures"). This simple but efficient [move ordering](Move_Ordering "Move Ordering") heuristic is called the [Killer Heuristic](Killer_Heuristic "Killer Heuristic"). Similar to moves from the [transposition table](Transposition_Table "Transposition Table") , killers may actually save the [generation](Move_Generation "Move Generation") of quiet moves at all if it [fails high](Fail-High "Fail-High"), but require a [legality test](Legal_Move "Legal Move").

## See also

- [Hash Move](Hash_Move "Hash Move")
- [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
- [Mate Killers](Mate_Killers "Mate Killers")
- [Move Ordering](Move_Ordering "Move Ordering")
- [Pseudo-Legal Move](Pseudo-Legal_Move "Pseudo-Legal Move")
- [PV-Move](PV-Move "PV-Move")
- [Refutation Move](Refutation_Move "Refutation Move")
- [Threat Move](Threat_Move "Threat Move") from [null move](Null_Move_Pruning "Null Move Pruning") refutations

## Forum Posts

- [Killer moves](http://groups.google.com/group/gnu.chess/browse_frm/thread/fb62cff6dea1bf09) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 21, 1995
- [killer moves?](https://www.stmintz.com/ccc/index.php?id=325602) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 04, 2003
- [Killer moves?](http://www.talkchess.com/forum/viewtopic.php?t=40423) by Mike Robinson, [CCC](CCC "CCC"), September 16, 2011
- [Killer and move encoding](http://www.talkchess.com/forum/viewtopic.php?t=53289) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 14, 2014 » [Encoding Moves](Encoding_Moves "Encoding Moves")
- [Effectiveness of killer moves](http://www.talkchess.com/forum/viewtopic.php?t=53317) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), August 17, 2014
- [TTMove legality checking ? & Killers Move Format?](http://www.talkchess.com/forum/viewtopic.php?t=63090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 08, 2017 » [Hash Move](Hash_Move "Hash Move")
- [How much ELO should I expect to gain from killer moves?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77734) by Christian Dean, [CCC](CCC "CCC"), July 16, 2021 » [Playing Strength](Playing_Strength "Playing Strength")

**[Up one Level](Moves "Moves")**
