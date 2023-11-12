---
title: Depth Reduction R
---
**[Home](Home "Home") * [Search](Search "Search") * Depth Reduction R**

**R** is a common name for a constant or variable signifying [depth](Depth "Depth") reduction used in the [Null Move Pruning](Null_Move_Pruning "Null Move Pruning") <a id="cite-note-1" href="#cite-ref-1">[1]</a>, [Null Move Reductions](Null_Move_Reductions "Null Move Reductions") and independently in [Multi-Cut](Multi-Cut "Multi-Cut") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. In many null move implementations it is either 2 or 3, the exact formula being depth - R - 1.

## Variable Reduction

When **R** becomes a variable, then we say that a program uses [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), first described by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, using R=3 when normal search depth exceeds 6 plies and R=2 otherwise, while more recently most engines account increased search depth with greater reductions <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Forum Posts

## 1997 ...

- [Null move depth reductions](https://groups.google.com/d/msg/rec.games.chess.computer/JJTEBafyuYM/hRTys0ZxcUIJ) by [Tom King](Tom_King "Tom King"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 02, 1997
- [Null move reductions](https://www.stmintz.com/ccc/index.php?id=28772) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), October 04, 1998

## 2000 ...

- [Null move R=2 vs Null move R=2/3](https://www.stmintz.com/ccc/index.php?id=183089) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 09, 2001
- [Null-Move: Difference between R = 2 and R = 3 in action](https://www.stmintz.com/ccc/index.php?id=239907) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), July 11, 2002
- [Smooth scaling -- an explanation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=313492&t=31361) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 30, 2009

## 2010 ...

- [Figuring out the R factor](http://www.talkchess.com/forum/viewtopic.php?t=31436) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), January 03, 2010
- [How much to reduce ?](http://www.talkchess.com/forum/viewtopic.php?t=49558) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), October 03, 2013 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Reductions](http://www.talkchess.com/forum/viewtopic.php?t=60240) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 22, 2016 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
- [Calculating R value for Null Move](http://www.talkchess.com/forum/viewtopic.php?t=60561) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 23, 2016
- [Rethinking r in null move](http://www.talkchess.com/forum/viewtopic.php?t=64927) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 18, 2017
- [Update on null move and LMR](http://www.talkchess.com/forum/viewtopic.php?t=65351) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), October 01, 2017 » [RomiChess](RomiChess "RomiChess")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"). (**1993**). *Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs.* [ICCA Journal, Vol. 16, No. 3](ICGA_Journal#16_3 "ICGA Journal")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"). (**1999**). *Adaptive null-move pruning*. [ICCA Journal, Vol. 22, No 3](ICGA_Journal#22_3 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Rethinking r in null move](http://www.talkchess.com/forum/viewtopic.php?t=64927) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), August 18, 2017

**[Up one Level](Search "Search")**

