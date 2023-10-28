---
title: Window
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Alpha-Beta](Alpha-Beta "Alpha-Beta") \* Window**



[ Arched Window of wall painting showing [Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Window** in the context of Alpha-Beta search (Alpha-Beta window) is the [open interval](https://en.wikipedia.org/wiki/Interval_%28mathematics%29#Terminology) between the [lower bound](Lower_Bound "Lower Bound") [Alpha](Alpha "Alpha") and the [upper bound](Upper_Bound "Upper Bound") [Beta](Beta "Beta"). 




```
**(α,β) = ]α,β[ = { x ∈ ℤ | α < x < β}**

```

Only values inside this interval, that is excluding Alpha and Beta, are [exact scores](Exact_Score "Exact Score"). Thus, with [integers](https://en.wikipedia.org/wiki/Integer) at least a window of (x-1, x+1) is necessary to reveal one exact score x. A [Null Window](Null_Window "Null Window") as used in the [Scout](Scout "Scout") part of [PVS](Principal_Variation_Search "Principal Variation Search") aka [NegaScout](NegaScout "NegaScout"), and [MTD(f)](MTD(f) "MTD(f)"), with integers (α, α+1) or (β-1, β), can therefor only provide a [bound](Bound "Bound"), either [failing-high](Fail-High "Fail-High") with a lower bound or [failing-low](Fail-Low "Fail-Low") with an upper bound. 



### Contents


* [1 Minimax Wall](#minimax-wall)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
* [5 References](#references)






[Robert Hyatt](Robert_Hyatt "Robert Hyatt") in a [CCC](CCC "CCC") reply to [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), January 1998 <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```
If the window is above the true value, so that you will [fail low](Fail-Low "Fail-Low"), you get maximal efficiency. Here's the way to follow why.  If every root move fails low, it can do so after searching only one move at ply 2, the one move necessary to 'refute' the root move.  So you get a truly small tree. If the window is below the true value, so you [fail high](Fail-High "Fail-High") on every move at the root, to fail high at the root means *every* move at ply=2 must fail low. The tree is roughly W times larger in this case.

```


```
[Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") noticed this and referred to this as the "minimax wall", that point where the window just drops down over the real score so that you don't get the quick fail lows.  I saw this when I played with [mtd(f)](MTD(f) "MTD(f)") a few months ago, as it was faster when the window was too high. Fast enough that it is best to keep it up there rather than dropping below the real value and having to fail upward... 

```

## See also


* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [MTD(f)](MTD(f) "MTD(f)")
* [Null Window](Null_Window "Null Window")
* [Odd-Even Effect](Odd-Even_Effect "Odd-Even Effect")
* [Scoring Root Moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man")


## Forum Posts


* [Alpha-Beta window in transposition tables?](https://groups.google.com/d/msg/rec.games.chess.computer/p8GbiiLjp0o/81vZ3czsthIJ) by Marty Bochane, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 25, 1996 » [Transposition Table](Transposition_Table "Transposition Table") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Negative alpha/beta windows: Are they useful?](http://www.talkchess.com/forum/viewtopic.php?t=55577) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), March 06, 2015


## External Links


* [Interval (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Interval_%28mathematics%29)
* [Window (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Window_%28disambiguation%29)
* [Window from Wikipedia](https://en.wikipedia.org/wiki/Window)
* [Launch window from Wikipedia](https://en.wikipedia.org/wiki/Launch_window)
* [Window (computing) from Wikipedia](https://en.wikipedia.org/wiki/Window_%28computing%29) » [GUI](GUI "GUI")
* [Register window from Wikipedia](https://en.wikipedia.org/wiki/Register_window)
* [Window function from Wikipedia](https://en.wikipedia.org/wiki/Window_function)
* [Window (short story) from Wikipedia](https://en.wikipedia.org/wiki/Window_%28short_story%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Arched Window of a [wall painting showing](https://commons.wikimedia.org/wiki/File:Fenster-Dal%C3%AD.JPG) [Salvador Dalí](Category:Salvador_Dal%C3%AD "Category:Salvador Dalí"), [Lima](https://en.wikipedia.org/wiki/Lima), [Peru](https://en.wikipedia.org/wiki/Peru), 2005 by Tabea Huth, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Re: New(?) search idea](https://www.stmintz.com/ccc/index.php?id=14539) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 22, 1998
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re. Fail low after fail high](http://www.talkchess.com/forum/viewtopic.php?t=55889&start=8) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), April 05, 2015 » [Fail-Low](Fail-Low "Fail-Low") , [Fail-High](Fail-High "Fail-High")

**[Up one level](Alpha-Beta "Alpha-Beta")**







 
