---
title: Mate Threat Extensions
---

**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Extensions](Extensions "Extensions") \* Mate Threat Extensions**

**Mate Threat Extensions** are extensions caused by a mate threat of the opponent [detected](Null_Move_Pruning#ThreatDetection "Null Move Pruning") after making a [null move](Null_Move "Null Move") in a [fail-soft](Fail-Soft "Fail-Soft") framework, or alternatively with a low shifted, or full window. Some programs detect [mate in one threats](Mate_at_a_Glance "Mate at a Glance") statically, i.e. as part or byproduct of [king safety](King_Safety "King Safety") in [evaluation](Evaluation "Evaluation"), to extend near or at the [horizon](Horizon_Node "Horizon Node").

## Threat Extensions

Mate threat extensions are special cases of the more general _Threat extensions_ not only restricted to [mate scores](Score#MateScores "Score") but losing some [material](Material "Material"). According to [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), the [Deep Thought](Deep_Thought "Deep Thought") team already used fail-low null move scores to detect threats before 1990 <a id="cite-note-1" href="#cite-ref-3">[1]</a>, descibed by [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") in his thesis <a id="cite-note-2" href="#cite-ref-2">[2]</a> and [ICCA Journal](ICGA_Journal "ICGA Journal") paper <a id="cite-note-3" href="#cite-ref-3">[3]</a>, where he mentioned fall 1986 implementation in [ChipTest](ChipTest "ChipTest").

### Deep-Search Extensions

The term _Deep-search extension_ was coined by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") in his _Null Move and Deep Search_ paper <a id="cite-note-4" href="#cite-ref-4">[4]</a>. As pointed out by Ernst A. Heinz, Donninger's idea was to extend the search by one ply if a null move near the horizon does not fail high and the null move score plus a constant margin is below [alpha](Alpha "Alpha"), while the [static evaluation](Evaluation "Evaluation") indicates a fail high. He further states <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

Donninger's idea is to extend the search one ply if a null move near the horizon (e.g. at depths <= 3) does not fail high and the null move score plus a constant margin (e.g. minor piece value) is <= alpha while the static evaluation at the node is >= [beta](Beta "Beta") (i.e. fails high). In order to get meaningful results for the null move score, you need to do it with a full alpha-beta window instead of a zero window (this is a known error in Donninger's original article). 

### DarkThought

Citing _How DarkThought Plays Chess_ <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

In order to avoid possibly [explosive growth](Search_Explosion "Search Explosion") of the [search tree](Search_Tree "Search Tree") as caused by excessive deep search extensions in the case of repeated mutual mating threats, [DarkThought](DarkThought "DarkThought") restricts them to null moves at depth = 2 in the first "2 \* iteration-number" plies on all paths. 

## See also

*   [Botvinnik-Markoff Extension](Botvinnik-Markoff_Extension "Botvinnik-Markoff Extension")
*   [Mate Killers](Mate_Killers "Mate Killers")
*   [Threat Detection](Null_Move_Pruning#ThreatDetection "Null Move Pruning")

## Publications

*   [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1990**). _A Statistical Study of Selective Min-Max Search in Computer Chess_. Doctoral Thesis. UMI Order Number: AAI9111467, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
*   [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). _Extension Heuristics_. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 14, No. 2, pp. 47-65
*   [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). _Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs._ [ICCA Journal](ICGA_Journal "ICGA Journal"), [Vol. 16, No. 3](http://people.csail.mit.edu/heinz/iccaj_db/node4.html), pp. 137-143
*   [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). _[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html)._ [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 20, No. 3, pp. 166-176 » [Extension Heuristics](http://people.csail.mit.edu/heinz/dt/node11.html)

## Forum Posts

*   [Deep Search Extension](https://www.stmintz.com/ccc/index.php?id=14259) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), January 18, 1998
*   [Null move mate extension](https://www.stmintz.com/ccc/index.php?id=57953) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), June 25, 1999
*   [The "same threat extension" as effective way to resolve horizon problem](https://www.stmintz.com/ccc/index.php?id=318833) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), October 01, 2003
*   [mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=389013) by Rick Bischoff, [CCC](CCC "CCC"), September 25, 2004

[Re: mate threat extension/null move](https://www.stmintz.com/ccc/index.php?id=390268) by [Don Beal](Don_Beal "Don Beal"), [CCC](CCC "CCC"), October 04, 2004 » [WAC](Win_at_Chess "Win at Chess") booster

*   [null move threat extension](http://www.talkchess.com/forum/viewtopic.php?t=24543) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), October 23, 2008

## External Links

*   [Extension Heuristics](http://people.csail.mit.edu/heinz/dt/node11.html) from [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). _[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html)._ [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 20, No. 3, pp. 166-176
*   [Programming Details - Slow Chess | Extensions Used, Detailed Description](http://www.3dkingdoms.com/chess/implementation.htm) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer") » [Slow Chess](Slow_Chess "Slow Chess")

## References

1.  <a id="cite-ref-1" href="#cite-note-1">↑</a> [Re: Deep Search Extension](https://www.stmintz.com/ccc/index.php?id=14327) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), January 19, 1998
2.  <a id="cite-ref-2" href="#cite-note-2">↑</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1990**). _A Statistical Study of Selective Min-Max Search in Computer Chess_. Doctoral Thesis. UMI Order Number: AAI9111467, [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University")
3.  <a id="cite-ref-3" href="#cite-note-3">↑</a> [Thomas Anantharaman](Thomas_Anantharaman "Thomas Anantharaman") (**1991**). _Extension Heuristics_. [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 14, No. 2, pp. 47-65
4.  <a id="cite-ref-4" href="#cite-note-4">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1993**). _Null Move and Deep Search: Selective-Search Heuristics for Obtuse Chess Programs._ [ICCA Journal](ICGA_Journal "ICGA Journal"), [Vol. 16, No. 3](http://people.csail.mit.edu/heinz/iccaj_db/node4.html), pp. 137-143
5.  <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Deep Search Extension](https://www.stmintz.com/ccc/index.php?id=14492) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), January 22, 1998
6.  <a id="cite-ref-6" href="#cite-note-6">↑</a> _[Extension Heuristics](http://people.csail.mit.edu/heinz/dt/node11.html)_ from [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). _[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html)._ [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 20, No. 3, pp. 166-176

**[Up one Level](Extensions "Extensions")**