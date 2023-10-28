---
title: Beta
---
**[Home](Home "Home") * [Search](Search "Search") * [Score](Score "Score") * Beta**

**Beta** (β) is the [upper bound](Upper_Bound "Upper Bound") of a [score](Score "Score") for the [node](Node "Node"). If the node value exceeds or equals beta, it means that the opponent will avoid this node, since his guaranteed score ([Alpha](Alpha "Alpha") of the parent node) is already greater. Thus, Beta is the best-score the opponent (min-player) could archive so far - in a [Negamax](Negamax "Negamax") framework from max-players point of view, where beta is the negated value of [alpha](Alpha "Alpha") from the parent node. If a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") occurs on the [upper bound](Upper_Bound "Upper Bound") of a [Cut-Node](Node_Types#CUT "Node Types") given by Beta, the value returned is a [lower bound](Lower_Bound "Lower Bound").

## See also

- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Alpha](Alpha "Alpha")
- [Bound](Bound "Bound")
- [Lower Bound](Lower_Bound "Lower Bound")
- [Upper Bound](Upper_Bound "Upper Bound")
- [Exact Score](Exact_Score "Exact Score")

## External Links

- [Beta from Wikipedia](https://en.wikipedia.org/wiki/Beta)
- [Beta (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Beta_%28disambiguation%29)
- [Beta release - Software release life cycle from Wikipedia](https://en.wikipedia.org/wiki/Software_release_life_cycle#Beta)

**[Up one Level](Score "Score")**

