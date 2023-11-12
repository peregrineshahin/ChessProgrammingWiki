---
title: FailLow
---
**[Home](Home "Home") * [Search](Search "Search") * [Alpha-Beta](Alpha-Beta "Alpha-Beta") * Fail-Low**

\[ Going down? <a id="cite-note-1" href="#cite-ref-1">[1]</a>
There are two related semantics, if talking of a **Fail-Low** - inside the [search tree](Search_Tree "Search Tree") or if using [aspiration windows](Aspiration_Windows "Aspiration Windows") at the [root](Root "Root").

## Contents

- [1 Inside the Tree](#inside-the-tree)
- [2 Root with Aspiration](#root-with-aspiration)
- [3 See also](#see-also)
- [4 Forum Posts](#forum-posts)
  - [4.1 1995 ...](#1995-...)
  - [4.2 2000 ...](#2000-...)
  - [4.3 2005 ...](#2005-...)
  - [4.4 2010 ...](#2010-...)
  - [4.5 2015 ...](#2015-...)
  - [4.6 2020 ...](#2020-...)
- [5 External Links](#external-links)
- [6 References](#references)

## Inside the Tree

A **Fail-low** appears at so called [All-Nodes](Node_Types#ALL "Node Types") inside the [alpha-beta algorithm](Alpha-Beta "Alpha-Beta"), also called Fail-Low nodes. The score returned is a [upper bound](Upper_Bound "Upper Bound") on the [exact score](Exact_Score "Exact Score") of the [node](Node "Node").

Quote by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") <a id="cite-note-2" href="#cite-ref-2">[2]</a>:

```C++
A fail-low indicates that this position was not good enough for us.  We will not reach this position, because we have some other means of reaching a position that is better.  We will not make the move that allowed the opponent to put us in this position. 

```

## Root with Aspiration

Another meaning of a **Fail-Low**, is associated with [aspiration windows](Aspiration_Windows "Aspiration Windows") at the [root](Root "Root"), where one needs to re-search with wider windows to get the true score rather than an [upper bound](Upper_Bound "Upper Bound").

Bruce again:

```C++
You can also talk about failing high and failing low from the root position, if you use an aspiration window. 

```

## See also

- [Fail-High](Fail-High "Fail-High")
- [Upper Bound](Upper_Bound "Upper Bound")
- [Lower Bound](Lower_Bound "Lower Bound")
- [Exact Score](Exact_Score "Exact Score")
- [Move Ordering](Move_Ordering "Move Ordering")
- [Null Window](Null_Window "Null Window")

## Forum Posts

## 1995 ...

- [Failing low at the root](https://www.stmintz.com/ccc/index.php?id=23672) by [Guido Schimmels](Guido_Schimmels "Guido Schimmels"), [CCC](CCC "CCC"), August 03, 1998
- [Question: Fail High then Low at Root](https://www.stmintz.com/ccc/index.php?id=84651) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), December 28, 1999 » [Fail-High](Fail-High "Fail-High"), [Root](Root "Root"), [Search Instability](Search_Instability "Search Instability")

## 2000 ...

- [Question: Fail low at root and time management](https://www.stmintz.com/ccc/index.php?id=95710) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), February 08, 2000 » [Root](Root "Root"), [Time Management](Time_Management "Time Management")
- [Fail-Low ?](https://www.stmintz.com/ccc/index.php?id=104748) by [Nobuhiro Yoshimura](index.php?title=Nobuhiro_Yoshimura&action=edit&redlink=1 "Nobuhiro Yoshimura (page does not exist)"), [CCC](CCC "CCC"), April 05, 2000
- [Researching after a fail-low](https://www.stmintz.com/ccc/index.php?id=124884) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), August 17, 2000
- [Fail highs..which subsequently fail low](https://www.stmintz.com/ccc/index.php?id=126878) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 27, 2000 » [Fail-High](Fail-High "Fail-High"), [Search Instability](Search_Instability "Search Instability")
- [Researching after a deep fail low](https://www.stmintz.com/ccc/index.php?id=190179) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), September 24, 2001
- [MTD, IID, fail-low, root-research](https://www.stmintz.com/ccc/index.php?id=311269) by Juergen Wolf, [CCC](CCC "CCC"), August 14, 2003 » [MTD(f)](</MTD(f)> "MTD(f)"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Root](Root "Root")
- [Search behavior in a case of root fail high/low](https://www.stmintz.com/ccc/index.php?id=353798) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 10, 2004 » [Fail-High](Fail-High "Fail-High"), [MTD(f)](</MTD(f)> "MTD(f)")

## 2005 ...

- [Fail-low pruning](https://www.stmintz.com/ccc/index.php?id=480380) by Tommi Rimpiläinen, [CCC](CCC "CCC"), January 17, 2006

## 2010 ...

- [Fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=51284) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2014 » [Fail-Soft](Fail-Soft "Fail-Soft"), [Fail-Hard](Fail-Hard "Fail-Hard"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Solving a fail low situation at the root](http://www.talkchess.com/forum/viewtopic.php?t=54241) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), November 03, 2014 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [What does "fail low at the root" mean?](http://www.open-chess.org/viewtopic.php?f=5&t=2754) by watersky33, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 24, 2014

## 2015 ...

- [Fail low after fail high](http://www.talkchess.com/forum/viewtopic.php?t=55889) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), April 04, 2015 » [Fail-High](Fail-High "Fail-High"), [Search Instability](Search_Instability "Search Instability")
- [Restarting iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=58542) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 09, 2015 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [(I)ID and PV dropout](http://www.talkchess.com/forum/viewtopic.php?t=64321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2017 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")

## 2020 ...

- [The devilish fail low](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73566) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 05, 2020

## External Links

- [Programming - Glossary - Fail Low, Fail High](http://web.archive.org/web/20040512194831/brucemo.com/compchess/programming/glossary.htm#fail-high) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics Site](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)

- [The Beatles](Category:The_Beatles "Category:The Beatles") - [I'm Down](https://en.wikipedia.org/wiki/I%27m_Down) (1966), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

- [Stevie Ray Vaughan](Category:Stevie_Ray_Vaughan "Category:Stevie Ray Vaughan") with [Jeff Beck](Category:Jeff_Beck "Category:Jeff Beck") and [Terry Bozzio](Category:Terry_Bozzio "Category:Terry Bozzio") - [I'm Going Down](http://www.guitarworld.com/stevie-ray-vaughan-and-jeff-beck-perform-going-down-1989-video) (1989), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Going down?](https://commons.wikimedia.org/wiki/File:Going_down_%3F.jpg) [Camden Fort Meagher](https://en.wikipedia.org/wiki/Camden_Fort_Meagher) by Twhelton, February 9, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Programming - Glossary - Fail Low, Fail High](http://web.archive.org/web/20040512194831/brucemo.com/compchess/programming/glossary.htm#fail-high) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics Site](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)

**[Up one Level](Alpha-Beta "Alpha-Beta")**

