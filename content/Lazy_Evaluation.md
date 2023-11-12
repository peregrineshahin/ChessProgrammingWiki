---
title: Lazy Evaluation
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Lazy Evaluation**



[ [Heinrich Kley](Category:Heinrich_Kley "Category:Heinrich Kley") - Das Kränzchen <a id="cite-note-1" href="#cite-ref-1">[1]</a>
  

In the chess programming sense of the phrase <a id="cite-note-2" href="#cite-ref-2">[2]</a>, **Lazy Evaluation** means dividing all the tasks performed by [evaluation function](Evaluation_Function "Evaluation Function") in (usually two) stages. If after performing all the tasks for a given stage score exceeds [beta](Beta "Beta") by a certain margin or if it falls below [alpha](Alpha "Alpha") by the same margin, the score is returned and no more evaluation is conducted. The first stage usually consists of the evaluation terms that are relatively cheap, possibly [incrementally updated](Incremental_Updates "Incremental Updates"), like [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables"). Lazy evaluation may be viewed as taking the [alpha-beta](Alpha-Beta "Alpha-Beta") principle one step further. If some parts of the evaluation function are omitted due to this heuristics, it means that one side is already winning "the evaluation game" by the margin unacceptable to the opponent, and therefore a cutoff occurs. 



## Forum Posts


### 1995 ...


* [approximate eval function](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/12607986c47b8ef6) by [Joël Rivat](Jo%C3%ABl_Rivat "Joël Rivat"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 20, 1995


### 2000 ...


* [Caution K v KBN and lazy eval or futility](https://www.stmintz.com/ccc/index.php?id=110681) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), May 14, 2000 » [KBNK Endgame](KBNK_Endgame "KBNK Endgame"), [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Chess Programming: "lazy eval"](https://www.stmintz.com/ccc/index.php?id=192813) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), October 11, 2001


### 2010 ...


* [doing lazy exit in eval or better not ?](http://www.talkchess.com/forum/viewtopic.php?t=37223) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), December 22, 2010
* [lazy eval discussion](http://www.talkchess.com/forum/viewtopic.php?t=38499) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 21, 2011
* [Lazy eval](http://www.talkchess.com/forum/viewtopic.php?t=41236) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 27, 2011
* [Razoring / Lazy eval question](http://www.talkchess.com/forum/viewtopic.php?t=46130) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), November 24, 2012 » [Razoring](Razoring "Razoring")
* [Re: lazy eval](http://www.talkchess.com/forum/viewtopic.php?t=52676&start=28) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), June 19, 2014
* [Lazy evaluation](http://www.talkchess.com/forum/viewtopic.php?t=53199) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 07, 2014
* [Implications of Lazy eval on Don Beal effect in Fail Soft](http://www.talkchess.com/forum/viewtopic.php?t=54387) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), November 19, 2014 » [Fail-Soft](Fail-Soft "Fail-Soft")


### 2015 ...


* [Is expensive eval required for QS?](http://www.talkchess.com/forum/viewtopic.php?t=64674) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2017 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [adaptive lazy eval](http://www.talkchess.com/forum/viewtopic.php?t=65047) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), August 31, 2017


## External Links


* [Not being lazy anymore](http://macechess.blogspot.de/2014/06/not-being-lazy-anymore.html)  by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), June 28, 2014 » [iCE](ICE "ICE")
* [Lazy evaluation from Wikipedia](https://en.wikipedia.org/wiki/Lazy_evaluation) as general programming term
* [Deep Purple](Category:Deep_Purple "Category:Deep Purple") - [Lazy](https://en.wikipedia.org/wiki/Lazy_%28Deep_Purple_song%29) ([Sydney 1984](https://www.setlist.fm/setlist/deep-purple/1984/sydney-entertainment-centre-sydney-australia-4bde3f66.html)), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Heinrich Kley](Category:Heinrich_Kley "Category:Heinrich Kley") - Das Kränzchen. Federzeichnung (aus: Skizzenbuch I, 1909)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> In general computer programming, [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation) refers a technique of delaying a computation until the result is required.

**[Up one Level](Evaluation "Evaluation")**







 
