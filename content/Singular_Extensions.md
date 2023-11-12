---
title: Singular Extensions
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Extensions](Extensions "Extensions") \* Singular Extensions**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d67d58ae5574bf8baa) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Uplifting <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Singular Extensions** (SE),  

are domain-independent extensions introduced in 1988 by [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), and [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, as implemented in [ChipTest](ChipTest "ChipTest") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and [Deep Thought](Deep_Thought "Deep Thought"). The idea is to extend the search at expected [PV-](Node_Types#PV "Node Types") and [Cut-Nodes](Node_Types#CUT "Node Types"), if one move seems to be a lot better than all of the alternatives. The problem is that one does not know in advance, and therefore has to perform a reduced search with a [null window](Null_Window "Null Window") lowered by some significant margin. Only if all alternatives fail below that window, a singular move is detected, and that move is re-searched with an extended [depth](Depth "Depth"). While it sounds expensive, the initial publication in 1988 reported encouraging results in tactical positions. In 1991, Anantharaman re-considered SE in comparison and interaction with other extensions, and mentioned implementation issues related to the [transposition table](Transposition_Table "Transposition Table") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a>. A somehow "reversed" idea compared to SE is [Björnsson's](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") [Multi-Cut](Multi-Cut "Multi-Cut") <a id="cite-note-6" href="#cite-ref-6">[6]</a> , to prune if in a reduced search multiple moves may [fail high](Fail-High "Fail-High"). 



## Singularity and Pathology


[Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") in *Extension Heuristics* <a id="cite-note-8" href="#cite-ref-8">[8]</a> :




```C++
In his Ph.D. thesis, [Schrüfer](G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") proves <a id="cite-note-9" href="#cite-ref-9">[9]</a> that singularity is related to [pathology](Search_Pathology "Search Pathology") in game trees: intuitively, if there are too many singular moves in a game tree, [brute-force](Brute-Force "Brute-Force") [minimax search](Minimax "Minimax") becomes pathological, beyond a certain [depth](Depth "Depth") deep searches are worse than shallow searches. More specifically for brute-force minimax search, where the [leaf evaluation](Evaluation "Evaluation") values are just [-1,1] (lose or win), then one necessary condition for the absence of pathology is that the fraction of nodes other than [PV-nodes](Node_Types#PV "Node Types") whose value is dependent on a single successor (singular) must be less than 1/B, where B is the [branching factor](Branching_Factor "Branching Factor") (36 for typical middle games). This result can be extended to the case when more than one value is assigned to [leaf nodes](Leaf_Node "Leaf Node"), though the resultant statement is more complicated. Intuitively, brute-force minimax search becomes pathological because it devotes too little effort to critical lines. The singular extension heuristic can be seen as a solution to this problem. 

```





## Restricted SE


A somehow relaxed version of SE was implemented in [Stockfish 1.6](Stockfish "Stockfish") in 2009, restricted to moves found in the [TT](Transposition_Table "Transposition Table") with a [lower bound flag](Lower_Bound "Lower Bound") set. According to [Larry Kaufman](Larry_Kaufman "Larry Kaufman") the idea may have its origin from [Rybka 3](Rybka "Rybka") via the disputed open source program [Ippolit](Ippolit "Ippolit") or its successors <a id="cite-note-10" href="#cite-ref-10">[10]</a> :




```C++
 At least one idea discussed on other forums that was attributed to Rybka 3 via the clone is already implemented in Stockfish 1.6, and was apparently the main reason for its large jump in strength over 1.5. So at least this idea will surely be in all top programs soon. Some developers will study the clone code themselves, while others may only use ideas they read about that came from the clone, but sooner or later other programs will show large gains from this information. At the very least, once an idea is implemented in a legitimate open-source program like Stockfish, it becomes accepted as something every programmer may use.

```


```C++
I don't think this is the place to publicize ideas from Rybka that were supposed to be secret, but the Stockfish 1.6 notes make it obvious that the big change in this version was a new way of doing "singular extension", improved from the way it was done in Deep Thought/Deep Blue.

```


```C++
Clearly the reverse engineering of Rybka is indeed "the highest form of flattery"; as to why the author(s) of the clone don't openly admit it I can't say. But the specific idea I'm talking about here is attributed to the clone (and hence by implication to Rykba) in the forum where it was discussed, so I don't think Stockfish or any other program which uses this idea is denying its origin. Once a good idea becomes common knowledge, regardless of its origin, programmers must use it (if it helps) to remain competitive. 

```

## See also


* [Check Extensions](Check_Extensions "Check Extensions")
* [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
* [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
* [Multi-Cut](Multi-Cut "Multi-Cut")


## Publications


<a id="cite-note-11" href="#cite-ref-11">[11]</a>



* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1988**). *Singular extensions: Adding Selectivity to Brute-Force Searching*. [AAAI](AAAI "AAAI") Spring Symposium, Computer Game Playing, also in [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), and (**1990**) in [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1990**). *Singular Extensions: Adding Selectivity to Brute-Force Searching*. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Confidently Selecting a Search Heuristic.* [ICCA Journal, Vol. 14, No. 1](ICGA_Journal#14_1 "ICGA Journal")
* [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
* [Tony Marsland](Tony_Marsland "Tony Marsland"), [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson") (**2001**). *Variable Depth Search.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), pp. 9-24. [pdf](http://www.ru.is/faculty/yngvi/pdf/MarslandB01.pdf)


## Forum Posts


### 1990 ...


* [Feng's (Deep Thought) article in Scientific American (long)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b3b584ef5a572d79#) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 19, 1990 <a id="cite-note-13" href="#cite-ref-13">[13]</a>


### 1995 ...


* [Re: Deep Thought](https://groups.google.com/d/msg/rec.games.chess/GV1_Q8voXJg/ZienH23_l2kJ) by [Paul Hsieh](Paul_Hsieh "Paul Hsieh"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), April 26, 1995
* [Want pseudo code of chess programming algorithm](http://groups.google.com/group/rec.games.chess.misc/browse_frm/thread/17daf11c5654b174) by Chavalit Likitvivatanavong, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 7, 1996
* [Deep Blue and Bob Hyatt...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/7043cdb46dd2ef5b#)by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 9, 1996
* [Singular Extensions...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/9356c55de4664308#) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 11, 1996
* [Singular extensions](https://www.stmintz.com/ccc/index.php?id=13783) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), January 08, 1998
* [Singular extensions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e661555d60ae82e6#) by KK, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 12, 1998
* [questions about singular extensions](https://www.stmintz.com/ccc/index.php?id=24282) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 09, 1998
* [DB and Singular Extensions](https://www.stmintz.com/ccc/index.php?id=33662) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [CCC](CCC "CCC"), November 22, 1998
* [Bob's secret SE experiment](https://www.stmintz.com/ccc/index.php?id=41906) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), February 02, 1999
* [Singular Extensions, Nullmove deepsearch](https://www.stmintz.com/ccc/index.php?id=43328) by [Frank Schneider](Frank_Schneider "Frank Schneider"), [CCC](CCC "CCC"), February 16, 1999 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")


### 2000 ...


* [Checks in qsearch/singular extensions](https://www.stmintz.com/ccc/index.php?id=88189) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), January 12, 2000
* [singular extension](https://www.stmintz.com/ccc/index.php?id=125295) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), August 20, 2000
* [singular extensions?](https://www.stmintz.com/ccc/index.php?id=130980) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), September 29, 2000
* [Limited singular extensions. Anybody tried?](https://www.stmintz.com/ccc/index.php?id=170356) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), May 18, 2001
* [Re: Nice tactical shot](https://www.stmintz.com/ccc/index.php?id=209565) by [Steve Timson](index.php?title=Steve_Timson&action=edit&redlink=1 "Steve Timson (page does not exist)"), [CCC](CCC "CCC"), January 24, 2002
* [Q: Singular extensions](https://www.stmintz.com/ccc/index.php?id=340288) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), January 05, 2004
* [singular extension](https://www.stmintz.com/ccc/index.php?id=387763) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 15, 2004
* [Which programs have Singular Extensions?](https://www.stmintz.com/ccc/index.php?id=393739) by Joshua Lee, [CCC](CCC "CCC"), October 28, 2004


### 2005 ...


* [New Algorithm for "el cheapo Singular Extensions" :)](https://www.stmintz.com/ccc/index.php?id=407576), [Dr. Axel Steinhage](http://www.future-shape.com/steinhage.html), [CCC](CCC "CCC"), January 26, 2005
* [Re: Singular extensions and null move](https://www.stmintz.com/ccc/index.php?id=428759) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), May 29, 2005 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Singular Extensions revisited](http://www.talkchess.com/forum/viewtopic.php?t=30211) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), October 19, 2009


### 2010 ...


* [iid and singular extensions](http://www.talkchess.com/forum/viewtopic.php?t=35302) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), July 05, 2010 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Stockfish Singular Extension, does it make sense?](http://www.talkchess.com/forum/viewtopic.php?t=35419) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), July 08, 2010
* [Singular Extensions](http://www.talkchess.com/forum/viewtopic.php?t=35603) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 28, 2010
* [Mult-cut, SE and ETC](http://www.talkchess.com/forum/viewtopic.php?t=35697) by Ricardo Gibert, [CCC](CCC "CCC"), August 05, 2010 » [Multi-Cut](Multi-Cut "Multi-Cut"), [Enhanced Transposition Cutoff](Enhanced_Transposition_Cutoff "Enhanced Transposition Cutoff")
* [next singular extension test](http://www.talkchess.com/forum/viewtopic.php?t=35698) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 05, 2010
* [Singular extension tests](http://www.talkchess.com/forum/viewtopic.php?t=35898) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 26, 2010
* [The "Secret" TT-move Singular Extension](http://www.talkchess.com/forum/viewtopic.php?t=38104) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), February 17, 2011
* [Singular Margin based on depth?](http://www.talkchess.com/forum/viewtopic.php?t=42419) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), February 11, 2012
* [Singular extension](https://groups.google.com/d/msg/fishcooking/IVuUkcSjdP8/bE6FPKJq2_oJ) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 01, 2013 » [Stockfish](Stockfish "Stockfish")
* [Singular extension: exclusion key](https://groups.google.com/d/msg/fishcooking/kpkfDzNfvhY/WGlKWPu-faQJ) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 24, 2013
* [Paper "Singular Extensions" by Anantharaman, Campbell, and Hsu (1988)](http://www.talkchess.com/forum/viewtopic.php?t=53713) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), September 15, 2014
* [search extensions](http://www.talkchess.com/forum/viewtopic.php?t=54281) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 08, 2014


### 2015 ...


* [Singular extensions](http://www.talkchess.com/forum/viewtopic.php?t=55734) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), March 21, 2015
* [Singular extension](http://www.talkchess.com/forum/viewtopic.php?t=57004) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 17, 2015
* [Singular extension](http://www.talkchess.com/forum/viewtopic.php?t=60435) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), June 11, 2016 » [Andscacs](Andscacs "Andscacs")
* [Singular extension improvement idea](http://www.talkchess.com/forum/viewtopic.php?t=66270) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), January 08, 2018
* [singular extension](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68290) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 24, 2018
* [some questions about singular search in Stockfish](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72231) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 01, 2019 » [Stockfish](Stockfish "Stockfish")
* [ELO value of TTSE?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72673) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), December 29, 2019 » [TTSE](#restrictedse)


## External Links


* [Singular extension](http://web.archive.org/web/20040420020213/brucemo.com/compchess/programming/extensions.htm#singular) from [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland")
* [Chess Programming Part V: Advanced Search](http://www.gamedev.net/page/resources/_/technical/artificial-intelligence/chess-programming-part-v-advanced-search-r1197) from [Chess Programming](Fran%C3%A7ois-Dominic_Laram%C3%A9e#Chess_Programming "François-Dominic Laramée") by [François-Dominic Laramée](Fran%C3%A7ois-Dominic_Laram%C3%A9e "François-Dominic Laramée"), [gamedev.net](http://www.gamedev.net/)
* [Travis Reuter Quintet](http://travisreuter.com/) - [Singular Arrays](http://www.allaboutjazz.com/rotational-templates-travis-reuter-new-focus-recordings-review-by-glenn-astarita.php), [Rotational Templates](http://www.newfocusrecordings.com/catalogue/travis-reuter-rotational-templates/) (2012), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Travis Reuter](http://travisreuter.com/), [Jeremy Viner](http://jeremyviner.com/), [Bobby Avey](http://bobbyavey.com/), [Chris Tordini](https://de.wikipedia.org/wiki/Chris_Tordini), [Jason Nazary](http://www.discogs.com/artist/1206973-Jason-Nazary)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Uplifting, Oil on Canvas, 24 x 36", [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d67d58ae5574bf8baa), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**1988**). *Singular extensions: Adding Selectivity to Brute-Force Searching*. [AAAI](AAAI "AAAI") Spring Symposium, Computer Game Playing, also in [ICCA Journal, Vol. 11, No. 4](ICGA_Journal#11_4 "ICGA Journal"), and (**1990**) in [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence_%28journal%29), Vol. 43, No. 1
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Feng's (Deep Thought) article in Scientific American (long)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/b3b584ef5a572d79#) by [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 19, 1990
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Confidently Selecting a Search Heuristic.* [ICCA Journal, Vol. 14, No. 1](ICGA_Journal#14_1 "ICGA Journal")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Yngvi Björnsson](Yngvi_Bj%C3%B6rnsson "Yngvi Björnsson"), [Tony Marsland](Tony_Marsland "Tony Marsland") (**2001**). *Multi-cut Alpha-Beta Pruning in Game Tree Search.* Theoretical Computer Science, Vol. 252, pp. 177-196. [pdf](http://www.ru.is/faculty/yngvi/pdf/BjornssonM01a.pdf)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu") (**2002**). *[Behind Deep Blue](http://press.princeton.edu/titles/7342.html): Building the Computer that Defeated the World Chess Champion*, Princeton University Press, ISBN 0-691-09065-3, pp. 54-55
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). *Extension Heuristics*. [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Günther Schrüfer](G%C3%BCnther_Schr%C3%BCfer "Günther Schrüfer") (**1988**). *Minimax-Suchen : Kosten, Qualität und Algorithmen*. Braunschweig : TU, 1988. (German)
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [A question to Larry Kaufman](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=14574), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30/31, 2009
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [ICGA Reference Database](ICGA_Journal#RefDB "ICGA Journal")
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Paper "Singular Extensions" by Anantharaman, Campbell, and Hsu (1988)](http://www.talkchess.com/forum/viewtopic.php?t=53713) by [Roland Stuckardt](Roland_Stuckardt "Roland Stuckardt"), [CCC](CCC "CCC"), September 15, 2014
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Feng-hsiung Hsu](Feng-hsiung_Hsu "Feng-hsiung Hsu"), [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman"), [Murray Campbell](Murray_Campbell "Murray Campbell"), [Andreas Nowatzyk](Andreas_Nowatzyk "Andreas Nowatzyk") (**1990**). *A Grandmaster Chess Machine*. [Scientific American](Scientific_American "Scientific American"), Vol. 263, No. 4, [Online Reprint](http://www.disi.unige.it/person/DelzannoG/AI2/hsu.html)

**[Up one Level](Extensions "Extensions")**







 
