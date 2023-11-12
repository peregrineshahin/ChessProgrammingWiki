---
title: Reductions
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* Reductions**


**Reductions** (as opposed to [pruning](Pruning "Pruning")),  

a class of search heuristics that decrease the [depth](Depth "Depth") to which a certain branch of the [tree](Search_Tree "Search Tree") is searched, also interpreted as negative [extension](Extensions "Extensions").



## Near the Tips


* [Razoring](Razoring "Razoring")


## Pruning after a reduced Search


Some dynamic pruning techniques base their [pruning](Pruning "Pruning") decision on a reduced search by [factor R](Depth_Reduction_R "Depth Reduction R"), also applied recursively:



* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Multi-Cut](Multi-Cut "Multi-Cut")


A none recursive pruning based on reduction at some fixed depth is applied by:



* [ProbCut](ProbCut "ProbCut")


## See also


* [Pruning](Pruning "Pruning")
* [Extensions](Extensions "Extensions")


## Forum Posts


### 1998 ...


* [A new selective heuristic?](https://www.stmintz.com/ccc/index.php?id=21017) by [Frank Schneider](Frank_Schneider "Frank Schneider"), [CCC](CCC "CCC"), June 21, 1998


### 2000 ...


* [Evaluation-based Reductions and/or Extensions](https://www.stmintz.com/ccc/index.php?id=338851) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), December 28, 2003 » [Extensions](Extensions "Extensions")
* [extensions + reductions + pruning = confusion](https://www.stmintz.com/ccc/index.php?id=356488) by [Johan de Koning](Johan_de_Koning "Johan de Koning"), [CCC](CCC "CCC"), March 24, 2004 (was [Shredder 8 secret: search depth?](https://www.stmintz.com/ccc/index.php?id=356109))


### 2005 ...


* [Reductions and null move refutations](http://www.open-aurec.com/wbforum/viewtopic.php?t=2300) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2005  » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Has anyone tested Gambit Fruit with Rebel Reductions on?](https://www.stmintz.com/ccc/index.php?id=461958) by [Ryan B.](Ryan_Benitez "Ryan Benitez"), [CCC](CCC "CCC"), November 15, 2005 » [Rebel](Rebel "Rebel"), [Gambit Fruit](Gambit_Fruit "Gambit Fruit") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
* [Reducing King Moves?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6066) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2007
* [Toga/Glaurung/Strelka Prunings/Reductions](http://www.talkchess.com/forum/viewtopic.php?t=19316) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), January 31, 2008 » [Toga](Toga "Toga"), [Glaurung](Glaurung "Glaurung"), [Strelka](Strelka "Strelka"), [Pruning](Pruning "Pruning")


### 2010 ...


* [Reducing/Pruning Bad Captures (SEE < 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 19, 2011 » [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Reductions from internal iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=44844) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), August 20, 2012 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Houdini 3 reducing the depth feature](http://www.talkchess.com/forum/viewtopic.php?t=45624) by Maurizio Maglio, [CCC](CCC "CCC"), October 17, 2012 » [Houdini](Houdini "Houdini")
* [Pruning in PV nodes](http://www.talkchess.com/forum/viewtopic.php?t=50907) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), January 14, 2014 » [Root](Root "Root"), [Node Types](Node_Types "Node Types")
* [variable reductions](http://www.talkchess.com/forum/viewtopic.php?t=52727) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), June 22, 2014


### 2015 ...


* [Ratio reduction](http://www.talkchess.com/forum/viewtopic.php?t=57697) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 20, 2015 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions"), [Symbolic](Symbolic "Symbolic")
* [Reduction Research Question](http://www.talkchess.com/forum/viewtopic.php?t=57747) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), September 25, 2015
* [Reductions](http://www.talkchess.com/forum/viewtopic.php?t=60240) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 22, 2016
* [EMR & EMP](http://www.talkchess.com/forum/viewtopic.php?t=60868) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 19, 2016
* [Floating Move Reduction](http://www.talkchess.com/forum/viewtopic.php?t=61425) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), September 14, 2016
* [EMR based on Null Move threat](http://www.talkchess.com/forum/viewtopic.php?t=65586) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 30, 2017


### 2020 ...


* [Pruning / reduction depending on king safety](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72981) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 02, 2020 » [King Safety](King_Safety "King Safety")
* [An alternative to IID](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74769) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 13, 2020 » [IID](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Futility reductions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77644) by [Jost Triller](Jost_Triller "Jost Triller"), [CCC](CCC "CCC"), July 05, 2021 » [Futility Pruning](Futility_Pruning "Futility Pruning")


## External Links


* [Reduction from Wikipedia](https://en.wikipedia.org/wiki/Reduction)
* [Programmer Corner - How Rebel Plays Chess - Reductions](https://web.archive.org/web/20120527155902/http://www.top-5000.nl/authors/rebel/chess840.htm#REDUCTIONS) by [Ed Schröder](Ed_Schroder "Ed Schroder") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)), [pdf reprint](http://members.home.nl/matador/Inside%20Rebel.pdf)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Programmer Corner - How Rebel Plays Chess - Reductions](http://www.top-5000.nl/authors/rebel/chess840.htm#REDUCTIONS) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [pdf reprint](http://members.home.nl/matador/Inside%20Rebel.pdf)

**[Up one level](Selectivity "Selectivity")**







 
