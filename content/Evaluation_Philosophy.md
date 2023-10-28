---
title: Evaluation Philosophy
---
**[Home](Home "Home") * [Evaluation](Evaluation "Evaluation") * Philosophy**

This page discusses some general **philosophy** behind the [evaluation](Evaluation "Evaluation") function. Instead of discussing the specific aspects of implementation, we discuss general design decisions of the overall evaluation.

## Contents

- [1 General](#general)
  - [1.1 Knowledge versus Speed](#knowledge-versus-speed)
  - [1.2 Light versus Heavy](#light-versus-heavy)
- [2 The Art of Evaluation](#the-art-of-evaluation)
  - [2.1 Orthogonality](#orthogonality)
  - [2.2 Continuity](#continuity)
  - [2.3 Sense of Progress](#sense-of-progress)
  - [2.4 Good Worst Case Behavior](#good-worst-case-behavior)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
- [5 External Links](#external-links)
- [6 References](#references)

## General

## Knowledge versus Speed

The evaluation is typically a collection of "[rules of thumb](https://en.wikipedia.org/wiki/Rule_of_thumb)" collected from hundreds of years of human [experience](https://en.wikipedia.org/wiki/Experience). It would be practically impossible to program all of the rules that humans have come up with over the years. Even if you could code for all of them, it would be inadvisable because of performance reasons. There must be a trade-off between [knowledge](Knowledge "Knowledge") versus speed. The more time you spend evaluating a position, the less time you have to search, and therefore, the less deep your program can see.

## Light versus Heavy

Some programs are designed with a very light evaluation function containing only the most basic features, letting the search make up the rest. Others prefer a heavy evaluation with as much knowledge as possible.

Most programs have an evaluation somewhere in the middle, with the trend in recent years being towards simpler, lighter evaluation functions, the idea being that these evaluations are the most bug-free and maintainable, which is far more important in practice than having many obscure pieces of knowledge. A big influence in this direction was the advent of [Fruit](Fruit "Fruit"), which has a very minimal evaluation function, yet it is a very solid, strong engine.

## The Art of Evaluation

[Tord Romstad](Tord_Romstad "Tord Romstad") writes about his evaluation philosophy <a id="cite-note-1" href="#cite-ref-1">[1]</a>: "You need patience, restraint, thorough testing, and a sound basic philosophy to succeed. The following are, in my opinion, the most important properties of a good evaluation function".

## Orthogonality

When it is possible, it is better to avoid having two different evaluation components which to some extent quantify the same extent of the position. When adding a new evaluation component which has a non-zero "orthogonal projection" (in a methaphorical sense, of course) on a previously existing component, try to adjust the two components in such a way that the projection is minimized, or to generalize and combine the two components into one.

## Continuity

If two positions X and Y which are "close to each other" in the sense that it is possible to get from position X to position Y by a short sequence of good moves, the two positions should ideally have similar evaluations. As a [corollary](https://en.wikipedia.org/wiki/Corollary), when one adds a big bonus or penalty for some particular pattern, one should also consider introducing a smaller bonus or penalty for getting close to this pattern. For instance, when adding a big bonus for a knight on an outpost square, it might be a good idea to add a smaller bonus for a knight attacking an outpost square.

## Sense of Progress

It is much more important that the evaluation function is able to accurately judge which of two very similar positions is better, than that it is able to judge which of two totally different positions is better. The evaluation function doesn't need to be able to answer questions like whether a certain classical King's Indian middle game is better than an endgame arising from a Richter-Rauzer Sicilian. What it needs is to be able to decide is things like whether one side should try to exchange a bishop for a knight, or whether it is better to castle kingside or queenside.

## Good Worst Case Behavior

It is better to be wrong by 10 centipawns all the time than to be completely correct 99.9% of the time and wrong by 300 centipawns 0.1% of the time.

## See also

- [Evaluation Discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity")
- [Knowledge](Knowledge "Knowledge")
- [Oracle](Oracle "Oracle")
- [Tapered Eval](Tapered_Eval "Tapered Eval")

## Forum Posts

- [The Art of Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=135133&t=15504) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 2, 2007

## External Links

- [Philosophy from Wikipedia](https://en.wikipedia.org/wiki/Philosophy)
- [Orthogonality from Wikipedia](https://en.wikipedia.org/wiki/Orthogonality)
- [Continuity from Wikipedia](https://en.wikipedia.org/wiki/Continuity)
- [Best, worst and average case from Wikipedia](https://en.wikipedia.org/wiki/Best,_worst_and_average_case)
- [Rule of thumb from Wikipedia](https://en.wikipedia.org/wiki/Rule_of_thumb)
- [John Scofield](Category:John_Scofield "Category:John Scofield") - Rule of thumb, album [Still Warm](https://en.wikipedia.org/wiki/Still_Warm) (1986), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Art of Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=135133&t=15504) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 2, 2007

**[Up One Level](Evaluation "Evaluation")**

