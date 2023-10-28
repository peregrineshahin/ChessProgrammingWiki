---
title: Null Window
---
**[Home](Home "Home") \* [Dictionary](Dictionary "Dictionary") \* Null Window**


A **Null Window**, also called **Zero Window**, **Scout Window** or **Narrow Window**, is a way to reduce the [search space](Search_Space "Search Space") in [alpha-beta](Alpha-Beta "Alpha-Beta") like [search](Search "Search") algorithms, to perform a boolean test, whether a [move](Moves "Moves") produces a worse or better score than a passed value. Null window searches are the base of [Scout](Scout "Scout"), [NegaScout](NegaScout "NegaScout") or [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), and [MTD(f)](MTD(f) "MTD(f)"). 



### Contents


* [1 History](#history)
* [2 Applications](#applications)
* [3 See Also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






Null windows were first described by [Judea Pearl](Judea_Pearl "Judea Pearl"), when introducing his [Scout](Scout "Scout") algorithm in April 1980 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Independently, null window searches were further elaborated by [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") in the [SIGART](ACM#SIG "ACM") Bulletin, Issue 72, July 1980 <a id="cite-note-2" href="#cite-ref-2">[2]</a>, who was already trying to get this published starting in August 1979. Fishburn was somewhat disappointed in the speedup (or lack thereof) that he measured on [checkers](Checkers "Checkers") lookahead trees. However when he went to work at [Bell Labs](Bell_Laboratories "Bell Laboratories") in 1981, [Ken Thompson](Ken_Thompson "Ken Thompson") told him that he had read the SIGART paper, and had sped up [Belle](Belle "Belle") by 1.5x with null windows <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



## Applications


Null window searches are performed in



* [MTD(f)](MTD(f) "MTD(f)")
* [Multi-Cut](Multi-Cut "Multi-Cut") to prove no singularity
* [NegaC\*](NegaC* "NegaC*")
* [NegaScout](NegaScout "NegaScout")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") to prove a null move [fails high](Fail-High "Fail-High")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [ProbCut](ProbCut "ProbCut") for the reduced search
* [Scout](Scout "Scout")
* [SSS\* and Dual\* as MT](SSS*_and_Dual*#SSStarandDualStarAsMT "SSS* and Dual*")


A null window search can never return an [exact score](Exact_Score "Exact Score") with [alpha](Alpha "Alpha") < score < [beta](Beta "Beta") and therefor a [principal variation](Principal_Variation "Principal Variation"), but either an [upper bound](Upper_Bound "Upper Bound") with score < beta (score <= alpha) or a [lower bound](Lower_Bound "Lower Bound") with score >= beta (score > alpha). 


With integers a null-window is defined as alpha == beta - 1.



## See Also


* [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Window](Window "Window")


## Forum Posts


* [Zero-width Window Null Move Search](https://www.stmintz.com/ccc/index.php?id=20596) by [Dezhi Zhao](index.php?title=Dezhi_Zhao&action=edit&redlink=1 "Dezhi Zhao (page does not exist)"), [CCC](CCC "CCC"), June 15, 1998
* [when to try zero window search](http://www.talkchess.com/forum/viewtopic.php?t=24883) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), November 14, 2008
* [Zero window TT entry](http://www.talkchess.com/forum/viewtopic.php?t=33084) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), March 05, 2010 » [Transposition Table](Transposition_Table "Transposition Table")


## External Links


* [Negascout from Wikipedia](https://en.wikipedia.org/wiki/Negascout)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Judea Pearl](Judea_Pearl "Judea Pearl") (**1980**). *Scout: A Simple Game-Searching Algorithm with Proven Optimal Properties*. Proceedings of the First Annual National Conference on Artificial Intelligence. Stanford. [pdf](http://ftp.cs.ucla.edu/pub/stat_ser/scout.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1980**). *An optimization of alpha-beta search*, SIGART Bulletin, Issue 72
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn"), personal communication

**[Up one level](Dictionary "Dictionary")**







 
