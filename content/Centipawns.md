---
title: Centipawns
---
**[Home](Home "Home") * [Search](Search "Search") * [Score](Score "Score") * Centipawns**

\[ Centipede <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Centipawns**, (Centi-pawns)

a score unit which corresponds approximately to **one hundredth** of a [pawn unit](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"). [Fixed point](https://en.wikipedia.org/wiki/Fixed-point_arithmetic) representation with centipawn fractions allows a smooth relation of all [piece values](Point_Value "Point Value") with a reasonable granularity to distinguish positional scores. 16 or even 15 bits are sufficient to store signed centipawn ranges in [hash tables](Hash_Table "Hash Table"), while sign extension to the common 32-bit integer range is convenient to avoid overflows in scaling terms like in the [tapered eval](Tapered_Eval "Tapered Eval"), even with an internal finer granularity used inside the evaluation <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

## Quotes

## Robert Hyatt

[Robert Hyatt](Robert_Hyatt "Robert Hyatt") on score grain in [Crafty](Crafty "Crafty") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

```C++Having done all three, my take on the issue is this:

```

1. `**Decipawns** (0.1) is too coarse. Not every positional consideration is worth 0.1 pawns, so you either have to round the score up to 0.1, or else throw it out since it would be zero.`
1. `**Millipawns** (0.001) is too fine. I do not believe that my evaluation has any .001 accuracy ideas in it. As you spread the evaluation scores out, your tree search becomes less efficient (for example, compare a program with no positional scoring to one with, with respect to tree size).`
1. `**Centipawns** (0.01) is reasonable. One could make the argument that maybe .05 is better (1/20th of a pawn). Or some other number. But my intuition after trying all three during the development of Crafty is that the right value lies in the interval {0.01, 0.1}. Whether it is on one end or the other, or somewhere in the middle, is a point for conjecture. It is too hard to test the idea, although I suppose I could just do a normal eval and then at the end, reduce it to the accuracy needed. But it is not easy to test for smaller than .01 increments since no increments in crafty would be smaller than .01...`

## Aske Plaat

[Aske Plaat's](Aske_Plaat "Aske Plaat") implementation tip on [MTD(f)](</MTD(f)> "MTD(f)") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++The coarser the grain of eval, the less passes [MTD(f)](MTD(f) "MTD(f)") has to make to converge to the minimax value. Some programs have a fine grained evaluation function, where positional knowledge can be worth as little as one hundredth of a pawn. Big score swings can become inefficient for these programs. It may help to dynamically increase the step size: instead of using the previous bound, one can, for example, add an extra few points in the search direction (for failing high, or searching upward, adding the bonus, and for failing low, or searching downward, subtracting the bonus) every two passes or so. ([Don Dailey](Don_Dailey "Don Dailey") found that a scheme like this works well in a version of [Cilkchess](Cilkchess "Cilkchess").) At the end, if you overshoot the minimax value, you have to make a small search in the opposite direction, using the previous search bound without an extra bonus, to make the final convergence. Also, it can be quite instructive to experiment with different evaluation function grain sizes. Sometimes coarse grain functions work better than fine grain, both for [NegaScout](NegaScout "NegaScout") and MTD(f). 

```

## See also

- [Millipawns](Millipawns "Millipawns")
- [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
- [Point Value](Point_Value "Point Value")

## Forum Posts

## 2000 ...

- [Performance of MTD(f) versus eval granularity?](https://www.stmintz.com/ccc/index.php?id=195217) by Werner Mühlpfordt, [CCC](CCC "CCC"), November 01, 2001 » [MTD(f)](</MTD(f)> "MTD(f)")
- [Centipawns and Millipawns](http://www.talkchess.com/forum/viewtopic.php?t=29694) by Ricardo Gibert, [CCC](CCC "CCC"), September 08, 2009
- [Winning percentage and centipawns](http://www.talkchess.com/forum/viewtopic.php?t=30695) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), November 18, 2009

## 2010 ...

- [xboard protocol and centipawn](http://www.talkchess.com/forum/viewtopic.php?t=36389) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), October 17, 2010
- [Evaluations in centipawns and symbols](http://www.talkchess.com/forum/viewtopic.php?t=45692) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), October 23, 2012
- [Is centipawn the right unit for measuring the score?](http://www.talkchess.com/forum/viewtopic.php?t=61071) by Karol Majewski, [CCC](CCC "CCC"), August 09, 2016

## 2020 ...

- [Centipawns vs Millipawns with NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75501) by Madeleine Birchfield, [CCC](CCC "CCC"), October 23, 2020 » [NNUE](NNUE "NNUE")

## External Links

- [Centipawn - WikiChess](http://chess.wikia.com/wiki/Centipawn)
- [centi- - Wiktionary](http://en.wiktionary.org/wiki/centi-)
- [Centi- from Wikipedia](https://en.wikipedia.org/wiki/Centi-)
- [Fixed-point arithmetic from Wikipedia](https://en.wikipedia.org/wiki/Fixed-point_arithmetic)
- [Granularity from Wikipedia](https://en.wikipedia.org/wiki/Granularity)
- [Resolution from Wikipedia](https://en.wikipedia.org/wiki/Resolution)
- [Rounding from Wikipedia](https://en.wikipedia.org/wiki/Rounding)
- [Centipede](https://en.wikipedia.org/wiki/Centipede_%28band%29) - [Septober Energy](https://en.wikipedia.org/wiki/Septober_Energy), 1971 (edited), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

feat. [Keith Tippett](Category:Keith_Tippett "Category:Keith Tippett"), [Ian Carr](Category:Ian_Carr "Category:Ian Carr"), [Karl Jenkins](Category:Karl_Jenkins "Category:Karl Jenkins"), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Jeff Clyne](Category:Jeff_Clyne "Category:Jeff Clyne"), [Roy Babbington](Category:Roy_Babbington "Category:Roy Babbington"), ...

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Centipede in peat [marshlands](https://en.wikipedia.org/wiki/Wetland) of [Kawai Nui](https://en.wikipedia.org/wiki/Kawai_Nui_Marsh), [O'ahu](https://en.wikipedia.org/wiki/Oahu), [Hawai'i](https://en.wikipedia.org/wiki/Hawaii) photographed by [Eric Guinther](https://en.wikipedia.org/wiki/User:Marshman), [Centipede from Wikipedia](https://en.wikipedia.org/wiki/Centipede)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Centipawns and Millipawns](http://www.talkchess.com/forum/viewtopic.php?t=29694&start=10) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), September 08, 2009
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Centipawns and Millipawns](http://www.talkchess.com/forum/viewtopic.php?t=29694&start=14) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 09, 2009
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [MTD(f) - A Minimax Algorithm faster than NegaScout](http://people.csail.mit.edu/plaat/mtdf.html) by [Aske Plaat](Aske_Plaat "Aske Plaat"), December 3, 1997

**[Up one level](Score "Score")**

