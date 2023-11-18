---
title: FailHigh Reductions
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * [Reductions](Reductions "Reductions") * Fail-High Reductions**

**Fail-high reductions** (FHR),

as proposed and examined by [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, and implemented in the program [Zugzwang](</Zugzwang_(Program)> "Zugzwang (Program)"), are based on the [Null Move Observation](Null_Move_Observation "Null Move Observation") (NMO) - similar to the [Null Move Heuristic](Null_Move_Pruning "Null Move Pruning") (NMH). The idea is to search to shallower [depth](Depth "Depth") at [positions](Chess_Position "Chess Position") that are seemingly quiet and where the side to move has established a substantial advantage, according to a static [evaluation](Evaluation "Evaluation"). Apart from the [evaluation function](Evaluation_Function "Evaluation Function"), the heuristic requires an additional function that returns a value indicating threats against the side to move and therefor the quietness of a position.

## Implementation

FHR is applied at expected [Fail-high or Cut-Nodes](Node_Types#cut-nodes "Node Types") [recursively](Recursion "Recursion") inside a [NegaScout](NegaScout "NegaScout")-framework. Feldmann's implementation did no re-search with the original depth, if the shallow search didn't confirm the fail high. While NMH relies on a dynamic search, but cuts the whole subtree - FHR uses a static threat detection. FHR is not as vulnerable as NMH in situations, where the NMO fails - namely in [zugzwang](Zugzwang "Zugzwang").

```C++

eval, threat := evaluate(...);
if ( eval - threat >= beta && alpha == beta - 1) 
  reduce depth by one

```

## See also

- [Double Null Move](Double_Null_Move "Double Null Move")
- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Multi-Cut](Multi-Cut "Multi-Cut")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
- [Null Move Reductions](Null_Move_Reductions "Null Move Reductions")
- [ProbCut](ProbCut "ProbCut")
- [Zugzwang](Zugzwang "Zugzwang")
- [Zugzwang (Program)](</Zugzwang_(Program)> "Zugzwang (Program)")

## Publications

- [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1997**). *Fail-High Reductions.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), available as [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=4399933A9FAE32A9C855DED714120C66?doi=10.1.1.51.4897&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.4897)
- [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1998**). *[Selective Game Tree Search on a Cray T3E](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/ABSTRACTS/FM_T3E.html)*. [ps](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/FM_T3E.ps.Z)
- [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2000**). *Selective Depth-First Search Methods*. Games in AI Research (eds. [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") and [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida")), pp. 31-45. [Universiteit Maastricht](Maastricht_University "Maastricht University"), Maastricht, The Netherlands. ISBN 90-621-6416-1. [pdf preprint](http://www.cs.ualberta.ca/%7Etony/RecentPapers/nec97w.pdf)

## Forum Posts

- [Fail High reductions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/548e7af6ccc53474) by [Jon Dart](Jon_Dart "Jon Dart"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 7, 1996
- [Fail high reductions](https://www.stmintz.com/ccc/index.php?id=304136) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), July 01, 2003
- [Fail High Reductions - question about researches](https://www.stmintz.com/ccc/index.php?id=395592) by [milix](Anastasios_Milikas "Anastasios Milikas"), [CCC](CCC "CCC"), November 11, 2004

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1997**). *Fail-High Reductions.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), available as [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=4399933A9FAE32A9C855DED714120C66?doi=10.1.1.51.4897&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.4897)

**[Up one level](Reductions "Reductions")**

