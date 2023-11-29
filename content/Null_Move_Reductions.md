---
title: Null Move Reductions
---

**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Reductions](Reductions "Reductions") \* Null Move Reductions**

**Null Move Reductions**,  
not to confused with the widespread [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), work similar to [Feldmann's](Rainer_Feldmann "Rainer Feldmann") [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions"), but use a [Null Move](Null_Move "Null Move") Search rather than static [evaluation](Evaluation "Evaluation") and reduces by a amount of **four** plies rather than one. [Eli David](Eli_David "Eli David") and [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") introduced so called **Extended Null-Move Reductions** <a id="cite-note-1" href="#cite-ref-1">[1]</a> with an adaptive [R](Depth_Reduction_R "Depth Reduction R") based on [depth](Depth "Depth").

## How it works

If a null move [fail-high](Fail-High "Fail-High") occurs - opposed to Null Move Pruning - the search is reduced by **four** plies, rather than pruned. Thus, **Null Move Reductions** are therefor less vulnerable to [Zugzwang](Zugzwang "Zugzwang") and might even applied in (late) endings.

```C++    if ( nullMoveAllowed && ...) {
        R = depth > 6 ? 4 : 3;
        makeNullMove()
        score = -zwSearch(1-beta, depth-R-1) // -AlphaBeta (0-beta, 1-beta, depth-R-1)
        unmakeNullMove();
        if (score >= beta ) {
        depth -= 4; // reduce search
        if ( depth <= 0 )
        return Evaluate(); // Quiescence
        }
    }
// continue search
```

_For zwSearch, see [Zero Window Search](Principal_Variation_Search#ZWS "Principal Variation Search") inside the [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")._

## See also

- [Double Null Move](Double_Null_Move "Double Null Move")
- [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions")
- [Null Move Observation](Null_Move_Observation "Null Move Observation")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Standing Pat](Quiescence_Search#StandPat "Quiescence Search") in [Quiescence Search](Quiescence_Search "Quiescence Search")

## Publications

- [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). _[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)_. [CG 2008](CG_2008 "CG 2008"), [pdf](http://www.oedavid.com/pubs/nmr.pdf)

## Forum Posts

- [Extended Null-Move Reductions](http://www.talkchess.com/forum/viewtopic.php?p=367283) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), August 20, 2010
- [Null move alterative in endgames](http://www.talkchess.com/forum/viewtopic.php?t=41104) by [Aleks Peshkov](Aleks_Peshkov "Aleks Peshkov"), [CCC](CCC "CCC"), November 16, 2011
- [thoughts on null-move reduction](http://www.talkchess.com/forum/viewtopic.php?t=56672) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), June 14, 2015 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")

## References

1.  <a id="cite-ref-1" href="#cite-note-1">↑</a> [Omid David](Eli_David "Eli David"), [Nathan S. Netanyahu](Nathan_S._Netanyahu "Nathan S. Netanyahu") (**2008**). _[Extended Null-Move Reductions](http://link.springer.com/chapter/10.1007/978-3-540-87608-3_19)_. [CG 2008](CG_2008 "CG 2008")

**[Up one level](Reductions "Reductions")**
