---
title: B
---
**[Home](Home "Home") * [Search](Search "Search") * B**\*

\[ Moonlit Beauties <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**B**\*,

a [best-first](Best-First "Best-First") search algorithm that finds the least-cost path from the [root node](Root "Root") to any goal node out of one or more possible goals. B\* was first published by [Hans Berliner](Hans_Berliner "Hans Berliner") in [1977](Timeline#1977 "Timeline") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, it is related to the [A\* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm).

## Underlying Idea

*There are things that must be found and things that must be known*

The value of a [position](Chess_Position "Chess Position"), as calculated by the [evaluation function](Evaluation "Evaluation"), can’t be trusted unless it is confirmed by some kind of search. That is the “[Raison d’être](https://en.wikipedia.org/wiki/Raison_d%27%C3%AAtre)” of the [quiescence search](Quiescence_Search "Quiescence Search"). If one replaces the quiescence by a full search with depth one, one gets a better value of this position. The deeper the search, the more reliable the evaluation. The reversal of this argument is to search further as long one can’t trust the backed up evaluation. This is the underlying idea of B\*.

## Multiple Values

The first approach of this idea is to use three values to describe a position. First the classical static evaluation, and an upper and lower value of what can be achieved, a pessimistic and an optimistic value of the position. The closer these values converge the static evaluation, the better. But they are dependent - the pessimistic value for one player is the optimistic value of the opponent player.

Once separated the "risk factor" from the static evaluation, one can use the evaluation to drive the search. This first trial of B\* was not successful. The "risk factor" was not well measured by a static function. The step was to go for a specific search for more reliable values.

## Threats

One further idea is to consider threats to drive the search! Resulting from careful thought, one can measure an upper bound of a deep search by a [null move](Null_Move "Null Move") search. You play, your opponent pass and you play again, and now do a normal search ([alpha-beta](Alpha-Beta "Alpha-Beta") or [PVS](Principal_Variation_Search "Principal Variation Search")). This is the threat detection used by [Andrew James Palay](Andrew_James_Palay "Andrew James Palay") on PB\* <a id="cite-note-3" href="#cite-ref-3">[3]</a> . The two values to drive the search are:

1. the evaluation issued from a standard search
1. and an optimistic value from a null move search

## Probability based Search

The next major step in the development of PB\* is not to use the raw optimistic value to drive the search, but a probability to get a target value. If you select the target value, as the value that will force a change in the best move at root, the probability to get the target value fit the probability that this move will be better than the one selected at root.

Once you evaluate a leaf node you propagate the value and the probability to the root node. As the search evolves, the target value change and the probability also evolve. When there is no hope to get the target, one can terminate the search. Now we can define two logical modes to select a move: The move with best real value and the move with best probability to get the target value (optimism). These two modes must be used alternatively by the two players; otherwise you just get no sense. (You reply to a sac with another sac and then another sac...).

## Two Step Search

As we must take this alternate choice into account for both players, we are forced to implement a two phases search. In the first stage we put to use the optimism for the player (Select phase). In the second stage, the opponent exert his optimism (verify phase). In the select phase, the player tries to raise the value for moves not in the [principal variation](Principal_Variation "Principal Variation") (PV). In the verify phase, the opponent tries to pull down the value of the principal variation (below the second best).

## Comparison: B\* versus PVS

In the [principal variation search](Principal_Variation_Search "Principal Variation Search") (PVS) we can also consider two steps. In the first, you try to exact the value of your principal variation doing a search with an open window. In the second step you just try to demonstrate that nothing is better doing a search with a [closed window](Null_Window "Null Window"). In B\* these steps are somehow inverted. The first select-phase tries to demonstrate there is nothing better than the [PV](Principal_Variation "Principal Variation"). The second verify-phase tries to exact the principal variation.

## Rethinking PB\*

With a lot of abstraction we can think that B\* is a search algorithm where some part of the tree search is saved in memory and another part is volatile and done on the fly. Tree values are propagated the “normal” way, which is following [minimax](Minimax "Minimax"). The [selectivity](Selectivity "Selectivity") is done on the [tree](Search_Tree "Search Tree") in memory.

PB\* is a minimax on top of standard [alpha-beta](Alpha-Beta "Alpha-Beta") or [PVS](Principal_Variation_Search "Principal Variation Search"). The rest of the algorithm is just the selectivity added to minimax to choose the node that deserve deeper search. If we disregard the selectivity and explore the tree on a systematic approach we get a brute force algorithm.

## Quality of Evaluation

As PB is an algorithm driven by values, the question that emerges is how good this PB\*'s evaluation should be? The two values that are used in PB\* meet different tasks. The real value determine which move is considered better.

The optimistic value defines the probability that this move is better, and drives the search. The better the optimistic value, the more selective is the search. PB\* is based largely in the fact that we can assess, with some reliability, the maximum/minimum value that the position can reach. The criterion of goodness of the optimistic value is the percentage of evaluation (real value) that are inside the optimistic pessimist range. As the evaluation is done by a PVS search,the deeper the PVS search the more readily we meet the criterion with closer values and better selectivity is achieved. A balance between the cost of each expands (depth of PVS evaluation) and the number of expansions needed (selectivity) must be adjusted. If we add a bonus in proportion to the risk taken on each hand (just to fit the criterion), we improve in tactical test set. But this reduce selectivity of the search as we encourage the search of sacs.

Somehow we split the dynamic factors of the position and the more long term (trustable) of the evaluation. The dynamics factors can be explored with a deeper PVS search or with some bonus/penalty on the optimistic evaluation for some tactical weakness (Berliner). The bonus approach get good performance on tactical set, but the deep search get better general result. End game positions require more in-depth search. A minimal number of expands is also required, this is why a fixed nodes approach for each PVS probe search get better overall performance.

## Performance Considerations

Suppose there is a PB\* program of a similar performance to PVS. For PB\* the total number of PVS probe search is:

```C++
R * Moves * Expands * PVS(ProbeDepth)

```

with

```C++
Moves = average moves in the position.
R = ratio (average probes per moves from 1 to 2 ) ~1.5
Expands = number of expands

```

For a standard PVS:

```C++
(BranchFactor ^ PlyEquiv) * PVS(ProbeDepth)

```

The comparison becomes:

```C++
R * Moves * Expands <=> BranchFactor ^ PlyEquiv

```

A large [branching factor](Branching_Factor "Branching Factor") favours PB\*. PB\* is weaker in endgame position (low branching factor). PVS improves with BF and PB\* reducing the number of expands needed (selectivity). Berliner reported that PB\* (with 225 node expansions on average) get a similar performance than [alpha-beta](Alpha-Beta "Alpha-Beta") with a branching factor of 4.5

## Implementations

B\* and later PB\* was implemented in [HiTech](HiTech "HiTech"). B\*HiTech played the [ACM 1993](ACM_1993 "ACM 1993"). [C](C "C") source code for first own experiments with B\* Probability Search was posted by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas") in [CCC](CCC "CCC") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, further implemented in his experimental [open source engine](Category:Open_Source "Category:Open Source") [Rocinante](Rocinante "Rocinante") written in [C++](Cpp "Cpp") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## See also

- [Category:B\*](Category:B* "Category:B*")
- [Best-First](Best-First "Best-First")
- [Centaur](Centaur "Centaur")
- [HiTech](HiTech "HiTech")
- [Rocinante](Rocinante "Rocinante")
- [Search Pathology](Search_Pathology "Search Pathology")
- [SSS\* and Dual\*](SSS*_and_Dual* "SSS* and Dual*")

## Publications

- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *The B\* Tree Search Procedure: Best-first Search Combined with Branch and Bound*. Computer Science Department. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
- [Hans Berliner](Hans_Berliner "Hans Berliner"), [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Jacques Pitrat](Jacques_Pitrat "Jacques Pitrat"), [Arthur Samuel](Arthur_Samuel "Arthur Samuel"), [David Slate](David_Slate "David Slate") (**1977**). *Panel on Computer Game Playing*. 975-982 [5. IJCAI 1977](http://www.sigmod.org/dblp/db/conf/ijcai/ijcai77.html#BerlinerGPSS77), [pdf](http://ijcai.org/Past%20Proceedings/IJCAI-77-VOL2/PDF/087.pdf)
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1979**). *The B\*-Tree Search Algorithm - A Best-First Proof Procedure.* [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 12, No. 1, pp. 23-40. ISSN 0004-3702.
- [Andrew James Palay](Andrew_James_Palay "Andrew James Palay") (**1982**). *The B\* Tree Search Algorithm - New Results*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 19, No. 2
- [Andrew James Palay](Andrew_James_Palay "Andrew James Palay") (**1983**). *Searching with Probabilities*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
- [Hans Berliner](Hans_Berliner "Hans Berliner"), [Chris McConnell](Chris_McConnell "Chris McConnell") (**1995**). *B\* Probability Based Search.* [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), research report, [pdf](https://pdfs.semanticscholar.org/95c8/569d34c3b7bc94f98b159825bd66a8b5e75d.pdf)
- [Heinz Herbeck](Heinz_Herbeck "Heinz Herbeck") (**1995**). *Solving Chess Endgames using the B\* Algorithm and the Rule Method*. Abstract, CSGP Workshop, [Chinese University Hongkong](https://en.wikipedia.org/wiki/Chinese_University_of_Hong_Kong), May 1995.
- [Hans Berliner](Hans_Berliner "Hans Berliner"), [Chris McConnell](Chris_McConnell "Chris McConnell") (**1996**). *B\* probability based search*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 86, No. 1

## Forum Posts

- [The B\* Algorithm](https://groups.google.com/d/msg/rec.games.chess/BYatWIYBrss/qd9FWZLpHTkJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), June 06, 1995
- [B\* Probability Search (long)](http://www.talkchess.com/forum/viewtopic.php?t=24717) by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas"), [CCC](CCC "CCC"), November 04, 2008
- [B\* in QS](http://www.talkchess.com/forum/viewtopic.php?t=35995) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 07, 2010
- [MCTS without random playout?](http://www.talkchess.com/forum/viewtopic.php?t=41730) by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas"), [CCC](CCC "CCC"), January 01, 2012 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")

## External Links

- [B\* from Wikipedia](https://en.wikipedia.org/wiki/B*)
- [A\* search algorithm from Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Dijkstra's algorithm from Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [John Coltrane Quartet](Category:John_Coltrane "Category:John Coltrane") - [My Favorite Things](https://en.wikipedia.org/wiki/My_Favorite_Things_%28song%29#John_Coltrane), Belgium, 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

[McCoy Tyner](Category:McCoy_Tyner "Category:McCoy Tyner"), [Elvin Jones](Category:Elvin_Jones "Category:Elvin Jones"), [Jimmy Garrison](https://en.wikipedia.org/wiki/Jimmy_Garrison), [John Coltrane](Category:John_Coltrane "Category:John Coltrane")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Moonlit Beauties](http://commons.wikimedia.org/wiki/File:Moonlit_Beauties_by_Luis_Ricardo_Falero.jpg) by [Luis Ricardo Falero](Category:Luis_Ricardo_Falero "Category:Luis Ricardo Falero"), [Oil on canvas](https://en.wikipedia.org/wiki/Oil_painting), 19th century, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1977**). *The B\* Tree Search Procedure: Best-first Search Combined with Branch and Bound*. Computer Science Department. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Andrew James Palay](Andrew_James_Palay "Andrew James Palay") (**1983**). *Searching with Probabilities*. Ph.D. thesis, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [B\* Probability Search (long)](http://www.talkchess.com/forum/viewtopic.php?t=24717) by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas"), [CCC](CCC "CCC"), November 04, 2008
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [engine Rocinante is available](http://www.talkchess.com/forum/viewtopic.php?t=29360) by [Antonio Torrecillas](Antonio_Torrecillas "Antonio Torrecillas"), [CCC](CCC "CCC"), August 12, 2009

**[Up one level](Search "Search")**

