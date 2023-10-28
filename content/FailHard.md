---
title: FailHard
---
**[Home](Home "Home") * [Search](Search "Search") * [Alpha-Beta](Alpha-Beta "Alpha-Beta") * Fail-Hard**

**Fail-Hard** is a term related to an [Alpha-Beta](Alpha-Beta "Alpha-Beta") like [search](Search "Search"), to make [Alpha](Alpha "Alpha") and [Beta](Beta "Beta") **hard** [bounds](Bound "Bound") of the returned value of the search. Even [terminal nodes](Terminal_Node "Terminal Node") which indicate draw or mate scores are supposed to be adjusted on the hard alpha-beta bounds.

## Contents

- [1 Fail-Hard Condition](#fail-hard-condition)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
  - [3.1 2000 ...](#2000-...)
  - [3.2 2005 ...](#2005-...)
  - [3.3 2010 ...](#2010-...)
  - [3.4 2020 ...](#2020-...)
- [4 External Links](#external-links)

## Fail-Hard Condition

```
[Alpha](Alpha "Alpha") <= [Score](Score "Score") <= [Beta](Beta "Beta")

```

## See also

- [Fail-Soft](Fail-Soft "Fail-Soft")
- [Fail-High](Fail-High "Fail-High")
- [Fail-Low](Fail-Low "Fail-Low")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")

## Forum Posts

## 2000 ...

- [Fail-soft or Fail-hard ?](https://www.stmintz.com/ccc/index.php?id=136488) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), November 04, 2000 » [Fail-Soft](Fail-Soft "Fail-Soft")
- [Fail-hard, fail-soft question](https://www.stmintz.com/ccc/index.php?id=363710) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), May 06, 2004

## 2005 ...

- [fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=24954) by [cyberfish](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), November 19, 2008
- [Return eval or upper bound?](http://www.talkchess.com/forum/viewtopic.php?t=30333) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), October 26, 2009

## 2010 ...

- [First post (and FailHigh question!)](http://www.talkchess.com/forum/viewtopic.php?t=48274) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), June 14, 2013 » [Fail-High](Fail-High "Fail-High"), [Fail-Soft](Fail-Soft "Fail-Soft")
- [Fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=51284) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2014 » [Fail-Soft](Fail-Soft "Fail-Soft"), [Fail-Low](Fail-Low "Fail-Low"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")

## 2020 ...

- [Fail hard/soft](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79223) by Philippe Chevalier, [CCC](CCC "CCC"), January 28, 2022

## External Links

- [Alpha–beta pruning from Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode)
- [Lecture notes for February 2, 1999 Variants of Alpha-Beta Search](https://www.ics.uci.edu/~eppstein/180a/990202b.html) by [David Eppstein](David_Eppstein "David Eppstein")

**[Up one Level](Alpha-Beta "Alpha-Beta")**

