---
title: FailSoft
---
**[Home](Home "Home") * [Search](Search "Search") * [Alpha-Beta](Alpha-Beta "Alpha-Beta") * Fail-Soft**

\[ Window of Perception <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Fail-Soft** is a term related to an [Alpha-Beta](Alpha-Beta "Alpha-Beta") like [search](Search "Search"). Returned scores might be outside the [bounds](Bound "Bound"):

- an [upper bound](Upper_Bound "Upper Bound") less than [alpha](Alpha "Alpha") at [All-Nodes](Node_Types#All-Nodes "Node Types")
- a [lower bound](Lower_Bound "Lower Bound") greater than [beta](Beta "Beta") at [Cut-Nodes](Node_Types#Cut-Nodes "Node Types")

## History

In his 1983 paper *Another optimization of alpha-beta search* <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") introduced Fail-Soft [Alpha-Beta](Alpha-Beta "Alpha-Beta") as an improvement of [Fail-Hard](Fail-Hard "Fail-Hard") without any extra work <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Fail-Soft has the reputation for searching less [nodes](Node "Node") than Fail-Hard, but might also require some care regarding to [search instability](Search_Instability "Search Instability") issues in conjunction with [transposition tables](Transposition_Table "Transposition Table") and various [pruning](Pruning "Pruning")-, [reduction](Reductions "Reductions")- and [extension](Extensions "Extensions") techniques.

## Mate Scores

In [Chrilly Donninger's](Chrilly_Donninger "Chrilly Donninger") initial [null move pruning](Null_Move_Pruning "Null Move Pruning") implementation there was a [deep search extension](Null_Move_Pruning#ThreatDetection "Null Move Pruning") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, if the null move was refuted by a mate attack, thus relying on Fail-Soft of a [null window](Null_Window "Null Window") search, where many "random" moves may refute the null-move with or without [score](Score "Score") in the mate range.

## See also

- [Fail-Hard](Fail-Hard "Fail-Hard")
- [Fail-High](Fail-High "Fail-High")
- [Fail-Low](Fail-Low "Fail-Low")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [NegaScout](NegaScout "NegaScout")
- [NegaC\*](NegaC* "NegaC*")
- [MTD(f)](</MTD(f)> "MTD(f)")

## Publications

- [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *[Another optimization of alpha-beta search](http://portal.acm.org/citation.cfm?id=1056623.1056628&coll=DL&dl=GUIDE&CFID=26266656&CFTOKEN=86225814)*. [SIGART Bulletin](ACM#SIG "ACM"), Issue 84, [pdf](https://drive.google.com/file/d/0B2pvWWlf39g-cjJpZkc1cDhfbkk/view)

## Forum Posts

## 1995 ...

- [bounds in alpha-beta](https://groups.google.com/d/msg/rec.games.chess.computer/xkepvuKHYUc/vI9AK1G2KkwJ) by [Walter Ravenek](Walter_Ravenek "Walter Ravenek"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 05, 1996 » [Arthur](Arthur "Arthur"), [Crafty](Crafty "Crafty")
- [New improvement to alpha/beta + TT?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a895e1a5524f8158) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 13, 1997
- [Fail-soft with PVS?](https://www.stmintz.com/ccc/index.php?id=45482) by [Will Singleton](Will_Singleton "Will Singleton"), [CCC](CCC "CCC"), March 09, 1999 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [What is the advantage of fail-soft?](https://www.stmintz.com/ccc/index.php?id=65947) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), August 25, 1999

## 2000 ...

- [Fail-soft or Fail-hard ?](https://www.stmintz.com/ccc/index.php?id=136488) by [Teerapong Tovirat](Teerapong_Tovirat "Teerapong Tovirat"), [CCC](CCC "CCC"), November 04, 2000 » [Fail-Hard](Fail-Hard "Fail-Hard")
- [Alpha beta fail soft, pruning & hash bounds?](https://www.stmintz.com/ccc/index.php?id=144854) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 14, 2000 » [Pruning](Pruning "Pruning"), [Bound](Bound "Bound")
- [Fail Soft Alpha Beta & Transpositions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/287d76556a5a298c) by Orhan Öztürk, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 3, 2003
- [(Fail soft) alpha beta](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/91dbbc00fc666c86) by Delphi, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 4, 2003
- [Fail soft alpha-beta](https://www.stmintz.com/ccc/index.php?id=314585) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), September 08, 2003
- [Is this a correct fail-soft?](https://www.stmintz.com/ccc/index.php?id=316955) by [Mikael Bäckman](Mikael_B%C3%A4ckman "Mikael Bäckman"), [CCC](CCC "CCC"), September 21, 2003
- [fail soft question?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45430) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 03, 2003
- [My fail soft reduces quality of collected PV. Help needed](https://www.stmintz.com/ccc/index.php?id=360837) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), April 20, 2004
- [Fail-hard, fail-soft question](https://www.stmintz.com/ccc/index.php?id=363710) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), May 06, 2004

## 2005 ...

- [Fail Soft question](https://www.stmintz.com/ccc/index.php?id=487414) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), February 17, 2006
- [Search questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6665) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 17, 2007 » [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning"), [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Returning score](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=21627) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), June 05, 2008
- [mate detetion issue](http://www.talkchess.com/forum/viewtopic.php?t=24560) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), October 24, 2008 » [Checkmate](Checkmate "Checkmate"), [Connect Four](Connect_Four "Connect Four")
- [fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=24954) by [cyberfish](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), November 19, 2008
- [Return eval or upper bound?](http://www.talkchess.com/forum/viewtopic.php?t=30333) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), October 26, 2009

## 2010 ...

- [First post (and FailHigh question!)](http://www.talkchess.com/forum/viewtopic.php?t=48274) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), June 14, 2013 » [Fail-High](Fail-High "Fail-High"), [Fail-Hard](Fail-Hard "Fail-Hard")
- [Fail soft vs fail hard](http://www.talkchess.com/forum/viewtopic.php?t=51284) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2014 » [Fail-Hard](Fail-Hard "Fail-Hard"), [Fail-Low](Fail-Low "Fail-Low"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Implications of Lazy eval on Don Beal effect in Fail Soft](http://www.talkchess.com/forum/viewtopic.php?t=54387) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), November 19, 2014 » [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
- [Multi-cut and fail-soft](http://www.talkchess.com/forum/viewtopic.php?t=60650) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 30, 2016 » [Multi-Cut](Multi-Cut "Multi-Cut")
- [Fail Soft best practices](http://www.open-chess.org/viewtopic.php?f=5&t=3180) by kickstone, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), July 30, 2018

## 2020 ...

- [Fail hard/soft](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79223) by Philippe Chevalier, [CCC](CCC "CCC"), January 28, 2022

## External Links

- [Alpha–beta pruning from Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode)
- [Lecture notes for February 2, 1999 Variants of Alpha-Beta Search](https://www.ics.uci.edu/~eppstein/180a/990202b.html) by [David Eppstein](David_Eppstein "David Eppstein")
- [fail-soft - Wiktionary](https://en.wiktionary.org/wiki/fail-soft)
- [Fail soft from Wikipedia](https://en.wikipedia.org/wiki/Fail_soft)
- [Soft Machine](Category:Soft_Machine "Category:Soft Machine") - [Hazard Profile](<https://en.wikipedia.org/wiki/Bundles_(album)>), 1975, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

Lineup: [Mike Ratledge](https://en.wikipedia.org/wiki/Mike_Ratledge), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Karl Jenkins](Category:Karl_Jenkins "Category:Karl Jenkins"), [Roy Babbington](Category:Roy_Babbington "Category:Roy Babbington"), [Allan Holdsworth](Category:Allan_Holdsworth "Category:Allan Holdsworth")

- [Ian Carr's](Category:Ian_Carr "Category:Ian Carr") [Nucleus](Category:Nucleus "Category:Nucleus") - Song For The Bearded Lady (1970), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

Lineup: [Ian Carr](Category:Ian_Carr "Category:Ian Carr"), [Brian Smith](https://en.wikipedia.org/wiki/Brian_Smith_%28musician%29), [Karl Jenkins](Category:Karl_Jenkins "Category:Karl Jenkins"), [John Marshall](Category:John_Marshall "Category:John Marshall"), [Chris Spedding](https://en.wikipedia.org/wiki/Chris_Spedding), [Jeff Clyne](Category:Jeff_Clyne "Category:Jeff Clyne")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Window of Perception (Jump Start Century 21 and move on)](https://commons.wikimedia.org/wiki/File:Modern_Tropical_Art-Window_of_Perception.jpg) by Dominic01, May 19, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [John Philip Fishburn](John_Philip_Fishburn "John Philip Fishburn") (**1983**). *[Another optimization of alpha-beta search](http://portal.acm.org/citation.cfm?id=1056623.1056628&coll=DL&dl=GUIDE&CFID=26266656&CFTOKEN=86225814)*. [SIGART Bulletin](ACM#SIG "ACM"), Issue 84, [pdf](https://drive.google.com/file/d/0B2pvWWlf39g-cjJpZkc1cDhfbkk/view)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Jean-Christophe Weill](Jean-Christophe_Weill "Jean-Christophe Weill") (**1991**). *Experiments With the NegaC\* Search - An Alternative for Othello Endgame Search.* [Heuristic Programming in AI 2](2nd_Computer_Olympiad#Workshop "2nd Computer Olympiad")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")

**[Up one Level](Alpha-Beta "Alpha-Beta")**

