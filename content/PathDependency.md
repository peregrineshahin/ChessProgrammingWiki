---
title: PathDependency
---
**[Home](Home "Home") \* [Search](Search "Search") \* Path-Dependency**


**Path-Dependency** describes a situation when the same [position](Chess_Position "Chess Position") gets a different value depending on a sequence of [moves](Moves "Moves") by which it has been reached. Whilst a few programs do this by design <a id="cite-note-1" href="#cite-ref-1">[1]</a>, within the standard [alpha-beta](Alpha-Beta "Alpha-Beta") framework path-dependency is considered undesirable, if impossible to avoid. 



### Contents


* [1 Typical Cases](#typical-cases)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
	+ [3.1 2000 ...](#2000-...)
	+ [3.2 2005 ...](#2005-...)
	+ [3.3 2010 ...](#2010-...)
* [4 External Links](#external-links)
* [5 References](#references)






* The position can be treated differently if there is a chance of [repetition](Repetitions "Repetitions") or hitting into a [fifty-move rule](Fifty-move_Rule "Fifty-move Rule").
* Different [move ordering](Move_Ordering "Move Ordering") can cause different result (different moves causing a cutoff), when it comes from the [hash table](Transposition_Table "Transposition Table") <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* Hf a program uses [search extensions](Extensions "Extensions"), search depth may be different (i.e. 1. d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3 vs 1.d4 Nf6 2.c4 e6 3.Nf3 Bb4+ 4.Nc3, where only the latter triggers a [check extension](Check_Extensions "Check Extensions"))
* History-dependent heuristics, like some versions of [LMR](index.php?title=Late_move_reductions&action=edit&redlink=1 "Late move reductions (page does not exist)") may prune different sub-trees.


## See also


* [Graph History Interaction](Graph_History_Interaction "Graph History Interaction") (GHI)
* [Transposition](Transposition "Transposition")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Repetitions](Repetitions "Repetitions")
* [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")


## Forum Posts


### 2000 ...


* ["Don't trust draw score" <=Is it true?](https://www.stmintz.com/ccc/index.php?id=182927) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), August 08, 2001 » [Repetitions](Repetitions "Repetitions"), [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")


### 2005 ...


* [path dependent evaluation](http://www.open-aurec.com/wbforum/viewtopic.php?t=2320) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 20, 2005
* [Re: And a still unsolved test position](https://www.stmintz.com/ccc/index.php?id=430487) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), June 09, 2005 » [Movei](Movei "Movei")
* [Semi-Path Dependent Hashing: a semi-useless idea](http://talkchess.com/forum/viewtopic.php?t=21343) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [CCC](CCC "CCC"), May 24, 2008 » [Transposition Table](Transposition_Table "Transposition Table")


### 2010 ...


* [Repetitions/50 moves and TT](http://www.talkchess.com/forum/viewtopic.php?t=40388) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 13, 2011
* [Texel recipe to fix TT draws scores](http://www.talkchess.com/forum/viewtopic.php?t=44167) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), June 23, 2012 » [Texel](Texel "Texel")


## External Links


* [Path dependence from Wikipedia](https://en.wikipedia.org/wiki/Path_dependence)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: Methods to stably evaluate nodes?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=115849&t=13559) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 05, 2007
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tony Warnock](Tony_Warnock "Tony Warnock"), [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1988**). *Search Tables in Computer Chess*. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 11, No. 1, pp. 10-13.

**[Up one Level](Search "Search")**







 
