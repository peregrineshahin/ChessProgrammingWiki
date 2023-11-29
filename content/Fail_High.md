---
title: Fail-High
---

**[Home](Home "Home") _ [Search](Search "Search") _ [Alpha-Beta](Alpha-Beta "Alpha-Beta") \* Fail-High**

\[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Red Balloon, 1922 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
There are two related semantics, if talking of a **Fail-High** - inside the [search tree](Search_Tree "Search Tree") or if using [aspiration windows](Aspiration_Windows "Aspiration Windows") at the [root](Root "Root").

## Inside the Tree

A **Fail-High** is associated with a [Beta-Cutoff](Beta-Cutoff "Beta-Cutoff") in the [alpha-beta algorithm](Alpha-Beta "Alpha-Beta"), which appears at so called [Cut-Nodes](Node_Types#cut-nodes "Node Types"), also called Fail-High nodes. The score returned is a [lower bound](Lower_Bound "Lower Bound") on the [exact score](Exact_Score "Exact Score") of the [node](Node "Node").

Quote by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```C++
A fail-high indicates that the search found something that was "too good".  What this means is that the opponent has some way, already found by the search, of avoiding this position, so you have to assume that they'll do this. If they can avoid this position, there is no longer any need to search successors, since this position won't happen.

```

## Root with Aspiration

Another meaning of a **Fail-High**, is associated with [Aspiration Windows](Aspiration_Windows "Aspiration Windows") at the [Root](Root "Root"), where one needs to re-search with wider windows to get the true score rather than a [lower bound](Lower_Bound "Lower Bound").

Quote by Bruce again:

```C++
You can also talk about failing high and failing low from the root position, if you use an aspiration window.

```

## See also

- [Fail-Hard](Fail-Hard "Fail-Hard")
- [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions")
- [Fail-Low](Fail-Low "Fail-Low")
- [Fail-Soft](Fail-Soft "Fail-Soft")
- [Upper Bound](Upper_Bound "Upper Bound")
- [Lower Bound](Lower_Bound "Lower Bound")
- [Exact Score](Exact_Score "Exact Score")
- [Move Ordering](Move_Ordering "Move Ordering")
- [Null Window](Null_Window "Null Window")

## Forum Posts

## 1995 ...

- [Question: Fail High then Low at Root](https://www.stmintz.com/ccc/index.php?id=84651) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), December 28, 1999 » [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root"), [Search Instability](Search_Instability "Search Instability")

## 2000 ...

- ["Percentage of fail-highs" question](https://www.stmintz.com/ccc/index.php?id=85729) by [Daniel Clausen](index.php?title=Daniel_Clausen&action=edit&redlink=1 "Daniel Clausen (page does not exist)"), [CCC](CCC "CCC"), January 03, 2000
- [Fail highs..which subsequently fail low](https://www.stmintz.com/ccc/index.php?id=126878) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 27, 2000 » [Fail-Low](Fail-Low "Fail-Low"), [Search Instability](Search_Instability "Search Instability")
- [Q: Fail High percentage](https://www.stmintz.com/ccc/index.php?id=143776) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), December 08, 2000
- [What means lazy/plain alpha bounding?](https://www.stmintz.com/ccc/index.php?id=153648) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), February 06, 2001 » [Root](Root "Root")
- [About False Fail Highs, professionals, and MTD searches](https://www.stmintz.com/ccc/index.php?id=223036) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), April 12, 2002 » [MTD(f)](</MTD(f)> "MTD(f)")
- [what does "fail high" mean?](https://www.stmintz.com/ccc/index.php?id=268076) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), November 29, 2002
- [what does "fail high" mean? In the context of iterative deepening](https://www.stmintz.com/ccc/index.php?id=268121) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), November 30, 2002 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Hash and first Fail High](https://www.stmintz.com/ccc/index.php?id=311272) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), August 14, 2003
- [Search behavior in a case of root fail high/low](https://www.stmintz.com/ccc/index.php?id=353798) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 10, 2004 » [Fail-Low](Fail-Low "Fail-Low"), [MTD(f)](</MTD(f)> "MTD(f)")
- [Fail-high on first move stat (86%)](https://www.stmintz.com/ccc/index.php?id=379624) by Michael Henderson, [CCC](CCC "CCC"), July 29, 2004 » [Move Ordering](Move_Ordering "Move Ordering")

## 2005 ...

- [Return eval or upper bound?](http://www.talkchess.com/forum/viewtopic.php?t=30333) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), October 26, 2009

## 2010 ...

- [Fail High nodes](http://www.open-chess.org/viewtopic.php?f=5&t=2220) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2013
- [First post (and FailHigh question!)](http://www.talkchess.com/forum/viewtopic.php?t=48274) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), June 14, 2013 » [Fail-Hard](Fail-Hard "Fail-Hard"), [Fail-Soft](Fail-Soft "Fail-Soft")
- [Why lower bound in fail-high?](http://www.open-chess.org/viewtopic.php?f=5&t=2726) by grandsmaster, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), September 20, 2014

## 2015 ...

- [Fail low after fail high](http://www.talkchess.com/forum/viewtopic.php?t=55889) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), April 04, 2015 » [Fail-Low](Fail-Low "Fail-Low"), [Search Instability](Search_Instability "Search Instability")
- [cut nodes](http://www.talkchess.com/forum/viewtopic.php?t=65477) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 18, 2017  » [Cut-Nodes](Node_Types#cut-nodes "Node Types")
- [On failing high and finding mates](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69927) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), February 16, 2019

## 2020 ...

- [Searching fail highs shallower..](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73250) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 02, 2020

## External Links

- [Programming - Glossary - Fail Low, Fail High](http://web.archive.org/web/20040512194831/brucemo.com/compchess/programming/glossary.htm#fail-high) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics Site](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Red Balloon, 1922, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Solomon R. Guggenheim Museum](https://en.wikipedia.org/wiki/Solomon_R._Guggenheim_Museum)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Programming - Glossary - Fail Low, Fail High](http://web.archive.org/web/20040512194831/brucemo.com/compchess/programming/glossary.htm#fail-high) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics Site](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)

**[Up one Level](Alpha-Beta "Alpha-Beta")**
