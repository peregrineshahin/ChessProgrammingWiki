---
title: Search Instability
---
**[Home](Home "Home") \* [Search](Search "Search") \* Instability**



[ [Rayleigh–Taylor instability](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Taylor_instability) in the [Crab Nebula](https://en.wikipedia.org/wiki/Crab_Nebula) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Search Instability**,  

a search phenomenon in [alpha-beta](Alpha-Beta "Alpha-Beta") and enhancements, where re-searches, most often with different [windows](Window "Window") leave contradicting results, for instance with [aspiration windows](Aspiration_Windows "Aspiration Windows") at the [root](Root "Root"), an unexpected [fail-low](Fail-Low "Fail-Low") after a [fail-high](Fail-High "Fail-High") or vice versa. Beside other things, it may caused by [graph history interaction](Graph_History_Interaction "Graph History Interaction") or [path-dependency](Path-Dependency "Path-Dependency") in conjunction with the [transposition table](Transposition_Table "Transposition Table"), as well as alpha-beta window dependencies of [pruning](Pruning "Pruning") decisions, like [null move pruning](Null_Move_Pruning "Null Move Pruning"), [futility pruning](Futility_Pruning "Futility Pruning"), and [history heuristic](History_Heuristic "History Heuristic") to decide about [LMR](Late_Move_Reductions "Late Move Reductions"). 



### Contents


* [1 Pragmatism](#pragmatism)
* [2 Quotes](#quotes)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
	+ [4.1 1994 ...](#1994-...)
	+ [4.2 2000 ...](#2000-...)
	+ [4.3 2010 ...](#2010-...)
* [5 External Links](#external-links)
* [6 References](#references)






Some programmers abandon aspiration windows <a id="cite-note-2" href="#cite-ref-2">[2]</a> , while others don't immediately return from a [PV-nodes](Node_Types#PV "Node Types") in case of sufficient [exact](Exact_Score "Exact Score") hits from transposition table <a id="cite-note-3" href="#cite-ref-3">[3]</a>. 



## Quotes


In his *Programming Topics*, [Bruce Moreland](Bruce_Moreland "Bruce Moreland") elaborates on Search Instability <a id="cite-note-4" href="#cite-ref-4">[4]</a> :




```C++
Search instability is something that happens when you try to write a program that is strong, as opposed to one that is perfect. There are many causes of instability, and I will discuss how various search enhancements can lead to instability, when I discuss those enhancements. A few other search techniques must take into account the possibility of instability.

```


```C++
An unstable search is one that returns results that don't make any sense. You have an alpha-beta window of (5, 25) and fail high. So you re-search with (24, INFINITY) and fail low. This shouldn't happen, because the fail-high indicated very clearly that the score should be 25 or better. How can you fail low?

```


```C++
Fact is, a lot of the things that make a chess program fast or strong do sleazy things that result in searches returning slightly different values when called with different windows, and if you aren't expecting the values you get, you can crash or have a bug that might make your program play a dumb move.

```


```C++
Some chess programmers can't handle the idea of search instability, and they are willing to let very good search techniques go in order to avoid it, or in order to think that they are avoiding it.

```


```C++
I wish it was possible to get rid of it completely, but as long as certain very basic techniques are used, it will be a problem. I think that the solution is to defend against crashes and bad behavior, then try to put it out of your mind. 

```

## See also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Astronomy](Category:Astronomy "Category:Astronomy")
* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")
* [Path-Dependency](Path-Dependency "Path-Dependency")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Window](Window "Window")


## Forum Posts


### 1994 ...


* [Alpha-beta inconsistencies](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b5f847cde3d26fd6) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), February 19, 1994
* [Search inconsistency](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2f916d80413c656f) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 17, 1998
* [Question: Fail High then Low at Root](https://www.stmintz.com/ccc/index.php?id=84651) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), December 28, 1999 » [Fail-High](Fail-High "Fail-High"), [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")


### 2000 ...


* [Fail highs..which subsequently fail low](https://www.stmintz.com/ccc/index.php?id=126878) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 27, 2000 » [Fail-High](Fail-High "Fail-High"), [Fail-Low](Fail-Low "Fail-Low")
* [Search Inconsistencies](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5072) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 23, 2006


### 2010 ...


* [Fail-High / Fail-Low in mate situations...](http://www.talkchess.com/forum/viewtopic.php?t=49081) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), August 24, 2013
* [Fail low after fail high](http://www.talkchess.com/forum/viewtopic.php?t=55889) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), April 04, 2015 » [Fail-Low](Fail-Low "Fail-Low"), [Fail-High](Fail-High "Fail-High")
* [Ordering of Root moves and search instability !](http://www.talkchess.com/forum/viewtopic.php?t=58055) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Move Ordering](Move_Ordering "Move Ordering")
* [Shifting alpha/beta on hash hit](http://www.talkchess.com/forum/viewtopic.php?t=59856) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), April 14, 2016 » [Transposition Table](Transposition_Table "Transposition Table")


## External Links


* [Search Instability](http://web.archive.org/web/20070704214238/www.seanet.com/%7Ebrucemo/topics/instability.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
* [Aspiration Windows](http://web.archive.org/web/20070705134903/www.seanet.com/%7Ebrucemo/topics/aspiration.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
* [Instability from Wikipedia](https://en.wikipedia.org/wiki/Instability)


## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [This](https://en.wikipedia.org/wiki/File:Crab_Nebula.jpg) is a [mosaic image](https://en.wikipedia.org/wiki/Photographic_mosaic), one of the largest ever taken by [NASA](https://en.wikipedia.org/wiki/NASA)/[ESA's](https://en.wikipedia.org/wiki/European_Space_Agency) [Hubble Space Telescope](https://en.wikipedia.org/wiki/Hubble_Space_Telescope) of the [Crab Nebula](https://en.wikipedia.org/wiki/Crab_Nebula), a six-light-year-wide expanding remnant of a star's [supernova explosion](https://en.wikipedia.org/wiki/Supernova). Japanese and Chinese astronomers recorded this violent event nearly 1,000 years ago in 1054, as did, almost certainly, Native Americans. [Rayleigh–Taylor instability from Wikipedia](https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Taylor_instability), [HubbleSite - NewsCenter - A Giant Hubble Mosaic of the Crab Nebula (12/01/2005) - Release Images](http://hubblesite.org/newscenter/archive/releases/2005/37/image/a/), December 01, 2005 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: PVS](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=254862) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [CCC](CCC "CCC"), March 12, 2009
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Transposition table pruning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=305236&t=30788) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), November 25, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Search Instability](http://web.archive.org/web/20070704214238/www.seanet.com/%7Ebrucemo/topics/instability.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)

**[Up one Level](Search "Search")**







 
