---
title: Branching Factor
---
**[Home](Home "Home") * [Search](Search "Search") * [Tree](Search_Tree "Search Tree") * Branching Factor**

\[ A [red-black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) with branching factor 2 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
In [computing](https://en.wikipedia.org/wiki/Computing), [tree data structures](<https://en.wikipedia.org/wiki/Tree_(data_structure)>), and [game theory](https://en.wikipedia.org/wiki/Game_theory), the **Branching Factor** is the number of children at each [node](Node "Node"), the [outdegree](https://en.wikipedia.org/wiki/Directed_graph#Indegree_and_outdegree). If this value is not uniform, an **average branching factor** can be calculated <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Contents

- [1 Average Branching Factor](#average-branching-factor)
- [2 Effective Branching Factor](#effective-branching-factor)
- [3 Mean Branching Factor](#mean-branching-factor)
- [4 Publications](#publications)
- [5 Forum Posts](#forum-posts)
  - [5.1 1997 ...](#1997-...)
  - [5.2 2000 ...](#2000-...)
  - [5.3 2005 ...](#2005-...)
  - [5.4 2010 ...](#2010-...)
  - [5.5 2015 ...](#2015-...)
  - [5.6 2020 ...](#2020-...)
- [6 External Links](#external-links)
- [7 References](#references)

## Average Branching Factor

In [chess](Chess "Chess"), in average there are about 35-38 [moves](Moves "Moves") per [position](Chess_Position "Chess Position"). One additional cycle of growth expands each [leaf](Leaf_Node "Leaf Node") so far accordantly. This is called the average branching factor of the [game tree](https://en.wikipedia.org/wiki/Game_tree).

## Effective Branching Factor

The effective branching factor (EBF), related to [iterative deepening](Iterative_Deepening "Iterative Deepening") of [depth-first search](Depth-First "Depth-First"), is conventionally defined as average ratio of [nodes](Node "Node") (or time used) revisited of the current [iteration](Iteration "Iteration") N versus the previous iteration N-1 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

- In pure [Minimax](Minimax "Minimax"), the effective branching factor is equal to the average branching factor
- In [Alpha-Beta](Alpha-Beta "Alpha-Beta"), assuming good [move ordering](Move_Ordering "Move Ordering"), the branching factor is reduced to about square root of the average branching factor <a id="cite-note-4" href="#cite-ref-4">[4]</a><a id="cite-note-5" href="#cite-ref-5">[5]</a>
- Alpha-beta enhancements, [transposition tables](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [late move reductions](Late_Move_Reductions "Late Move Reductions") further reduce the EBF below three, strong programs even near or below two <a id="cite-note-6" href="#cite-ref-6">[6]</a>

```
EBF(N-1) ::= nodes(N-1) / nodes(N-2)
EBF(N)   ::= nodes(N)   / nodes(N-1)

```

Due to the [odd-even effect](Odd-Even_Effect "Odd-Even Effect") of [Alpha-Beta](Alpha-Beta "Alpha-Beta") as described by [Michael Levin's Theorem](Michael_Levin#Theorem "Michael Levin"), this is lower if 'N' is even, and higher if 'N' is odd. Due to [extensions](Extensions "Extensions"), [reductions](Reductions "Reductions") and various [pruning techniques](Pruning "Pruning"), this odd-even effect is diminishing accordantly. One may also use the square root of the ratio of two odd or even iterations.

```
EBF ::= √(nodes(N) / nodes(N-2));

```

However, with all kind of extensions, reductions, and forward pruning applied to the tree, it is not at all clear that the average branch is searched precisely one ply deeper at iteration N+1 than at iteration N, which makes such an effective branching factor quite useless to compare between programs <a id="cite-note-7" href="#cite-ref-7">[7]</a>, despite some programs even perform ID depth increments of [fractions](Depth#FractionalPlies "Depth") of one ply.

## Mean Branching Factor

[Steven Edwards](Steven_Edwards "Steven Edwards") made following reasonable proposal of a Mean Branching Factor <a id="cite-note-8" href="#cite-ref-8">[8]</a>:

```
MBF ::= count of all nodes / count of non terminal nodes

```

## Publications

- [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") (**1978**). *On the branching factor of the alpha-beta pruning algorithm*. [Artificial Intelligence](Artificial_Intelligence#Journals "Artificial Intelligence") 10
- [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *[The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality](http://portal.acm.org/citation.cfm?id=358616&dl=ACM&coll=DL&CFID=27355608&CFTOKEN=40935826)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8
- [Stefan Edelkamp](index.php?title=Stefan_Edelkamp&action=edit&redlink=1 "Stefan Edelkamp (page does not exist)"), [Richard Korf](Richard_Korf "Richard Korf") (**1998**). *The Branching Factor of Regular Search Spaces*. [AAAI-98](Conferences#AAAI-98 "Conferences"), [pdf](https://pdfs.semanticscholar.org/1a71/184c9432957427399435b8cde7e2d1977955.pdf)

## Forum Posts

## 1997 ...

- [branching factor question](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/21c702f358784af) by vince, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 04, 1997
- [Please, say in few words what can reduce the "branching factor"](https://www.stmintz.com/ccc/index.php?id=69483) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 19, 1999

## 2000 ...

- [Branching factor, make me confuse more that ever](https://www.stmintz.com/ccc/index.php?id=104182) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 01, 2000
- [Definition of branching factor?](https://www.stmintz.com/ccc/index.php?id=152665) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 30, 2001
- [Branching Factor = q/p ?](https://www.stmintz.com/ccc/index.php?id=198563) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 23, 2001
- [Measured min-max branching factor](https://www.stmintz.com/ccc/index.php?id=259843) by [James Swafford](James_Swafford "James Swafford"), [CCC](CCC "CCC"), October 17, 2002
- [What's best low BF or good WAC result?](https://www.stmintz.com/ccc/index.php?id=289795) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 18, 2003
- [PVS and MTD(f) branching factor](https://www.stmintz.com/ccc/index.php?id=301402) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), June 17, 2003 » [PVS](Principal_Variation_Search "Principal Variation Search"), [MTD(f)](</MTD(f)> "MTD(f)")
- [Improvements in BF makes my MoveGen suck =(](https://www.stmintz.com/ccc/index.php?id=303316) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), June 26, 2003 » [Move Generation](Move_Generation "Move Generation")
- [To Ed: Branching factor formula in Rebel 12](https://www.stmintz.com/ccc/index.php?id=311344) by [Federico Corigliano](Federico_Andr%C3%A9s_Corigliano "Federico Andrés Corigliano"), [CCC](CCC "CCC"), August 15, 2003 » [Rebel](Rebel "Rebel")
- [Question about evaluation and branch factor](https://www.stmintz.com/ccc/index.php?id=328924) by [Marcus Prewarski](Marcus_Prewarski "Marcus Prewarski"), [CCC](CCC "CCC"), November 20, 2003 » [Evaluation](Evaluation "Evaluation")

## 2005 ...

- [iterative deepening and branching factor](http://www.talkchess.com/forum/viewtopic.php?t=14963) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 09, 2007 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Calculation of branching factor](http://www.talkchess.com/forum/viewtopic.php?t=20301) by PK-4, [CCC](CCC "CCC"), March 23, 2008
- [Reducing branching factor](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=24535) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), October 26, 2008

## 2010 ...

- [effective branching factor of chess programs](http://www.talkchess.com/forum/viewtopic.php?t=37205) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), December 21, 2010
- [EBF question](http://www.talkchess.com/forum/viewtopic.php?t=37910) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), February 01, 2011
- [EBF definition problem in chess wiki](http://www.talkchess.com/forum/viewtopic.php?t=39073) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 13, 2011
- [Node counts at a given depth/iteration in search](http://www.open-chess.org/viewtopic.php?f=5&t=1403) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 23, 2011
- [Bigger steps when branching factor \< 2?](http://www.talkchess.com/forum/viewtopic.php?t=41001) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), November 05, 2011 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Branching Factor of top engines](http://www.talkchess.com/forum/viewtopic.php?t=48281) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 15, 2013 » [Houdini 3](Houdini "Houdini"), [Stockfish 3](Stockfish "Stockfish"), [Komodo 5 CCT](Komodo "Komodo"), [Shredder 6](Shredder "Shredder")
- [Some fun with Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=53807) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 23, 2014 » [Komodo 8](Komodo#8 "Komodo")

## 2015 ...

- [High branching factor when mate score is found](http://www.talkchess.com/forum/viewtopic.php?t=63467) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), March 16, 2017

## 2020 ...

- [EBF](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73655) by lauriet, [CCC](CCC "CCC"), April 15, 2020
- [Effective branching factor question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76529) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), February 08, 2021

## External Links

- [Branching factor from Wikipedia](https://en.wikipedia.org/wiki/Branching_factor)
- [Combinatorial explosion from Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_explosion)
- [Branching Factor](http://www.fastgm.de/branching-factor.html) from [FGRL](FGRL "FGRL") by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller")
- [Led Zeppelin](Category:Led_Zeppelin "Category:Led Zeppelin") - [How Many More Times](https://en.wikipedia.org/wiki/How_Many_More_Times) (Danish TV 1969) , [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Example of red-black tree by [Cburnett](https://en.wikipedia.org/wiki/User:Cburnett), December 30, 2006, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Branching factor from Wikipedia](https://en.wikipedia.org/wiki/Branching_factor)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [EBF definition problem in chess wiki](http://www.talkchess.com/forum/viewtopic.php?t=39073) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 13, 2011
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Gérard M. Baudet](G%C3%A9rard_M._Baudet "Gérard M. Baudet") (**1978**). *On the branching factor of the alpha-beta pruning algorithm*. [Artificial Intelligence](Artificial_Intelligence#Journals "Artificial Intelligence") 10
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Judea Pearl](Judea_Pearl "Judea Pearl") (**1982**). *[The Solution for the Branching Factor of the Alpha-Beta Pruning Algorithm and its Optimality](http://portal.acm.org/citation.cfm?id=358616&dl=ACM&coll=DL&CFID=27355608&CFTOKEN=40935826)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 25, No. 8
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Branching Factor of top engines](http://www.talkchess.com/forum/viewtopic.php?t=48281) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), June 15, 2013 » [Houdini 3](Houdini "Houdini"), [Stockfish 3](Stockfish "Stockfish"), [Komodo 5 CCT](Komodo "Komodo"), [Shredder 6](Shredder "Shredder")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Calculation of branching factor](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=181822&t=20301) by [Tord Romstad](Tord_Romstad "Tord Romstad"), March 28, 2008
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Calculation of branching factor](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=181617&t=20301) by [Steven Edwards](Steven_Edwards "Steven Edwards"), March 27, 2008

**[Up one Level](Search_Tree "Search Tree")**

