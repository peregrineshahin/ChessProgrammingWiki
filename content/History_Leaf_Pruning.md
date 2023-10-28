---
title: History Leaf Pruning
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * [Pruning](Pruning "Pruning") * History Leaf Pruning**

**History leaf pruning**,

a pruning technique based on [history counters](History_Heuristic "History Heuristic"). The idea is to prune moves that are \<= 0 [depth](Depth "Depth") after [reductions](Reductions "Reductions") and are below a given history threshold. History Leaf Pruning showed up as an option in [Fruit 05/11/03](Fruit "Fruit") by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey").

## Sample Code

```

if (node_type != NodePV) {
    if (!in_check && played_nb >= 5 && !extended) {
        value = sort->value; // history score
        if (value < HistoryThreshold) {
            new_depth -= 1;
            if (value < LeafThreshold) continue; // History Leaf pruning
            reduced = true;
        }
    }
}

```

## See also

- [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
- [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
- [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic")
- [Futility Pruning](Futility_Pruning "Futility Pruning")
- [History Heuristic](History_Heuristic "History Heuristic")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Reductions](Reductions "Reductions")
- [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")

## Forum Posts

- [Re: Possible search improvment](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=274486&t=28459) by [Ryan Benitez](Ryan_Benitez "Ryan Benitez"), [CCC](CCC "CCC"), June 17, 2009 » [ProbCut](ProbCut "ProbCut")
- [Can someone explain this?](http://www.talkchess.com/forum/viewtopic.php?t=30036) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), October 07, 2009 » [Toga](Toga "Toga")

**[Up one Level](Pruning "Pruning")**

