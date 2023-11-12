---
title: Horizon Effect
---
**[Home](Home "Home") * [Search](Search "Search") * Horizon Effect**

\[ [Water Horizon](https://en.wikipedia.org/wiki/Horizon) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
The **Horizon Effect** is caused by the [depth](Depth "Depth") limitation of the [search algorithm](Search "Search"), and became manifest when some negative event is inevitable but postponable. Because only a partial game tree has been analyzed, it will appear to the system that the event can be avoided when in fact this is not the case. Beside obligatory [quiescence search](Quiescence_Search "Quiescence Search"), [extensions](Extensions "Extensions"), specially [check extensions](Check_Extensions "Check Extensions") are designed to reduce horizon effects.

## Quotes

## By Tony Marsland

Quote by [Tony Marsland](Tony_Marsland "Tony Marsland") from *Computer Chess and Search.* <a id="cite-note-2" href="#cite-ref-2">[2]</a> :

```C++
**2. 6. Horizon Effect**
An unresolved defect of chess programs is the insertion of delaying moves that cause any inevitable loss of material to occur beyond the program’s horizon (maximum search depth), so that the loss is hidden ([Berliner](Hans_Berliner "Hans Berliner"), 1973 <a id="cite-note-3" href="#cite-ref-3">[3]</a>). The ‘horizon effect’ is said to occur when the delaying moves unnecessarily weaken the position or give up additional material to postpone the eventual loss. The effect is less apparent in programs with more knowledgeable quiescence searches ([Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), 1982 <a id="cite-note-4" href="#cite-ref-4">[4]</a>), but all programs exhibit this phenomenon. There are many illustrations of the difficulty; the example in Figure 4, which is based on a study by Kaindl, is clear. Here a program with a simple quiescence search involving only captures would assume that any blocking move saves the queen. Even an 8-ply search (..., Pb2; Bxb2, Pc3; Bxc3, Pd4; Bxd4, Pe5; Bxe5) might not show the inevitable, ‘believing’ that the queen has been saved at the expense of four pawns! 

```

```C++
Thus programs with a poor or inadequate quiescence search suffer more from the horizon effect.
The best way to provide automatic extension of non-quiescent positions is still an open question, despite proposals such as bandwidth heuristic search ([Larry Harris](Larry_Harris "Larry Harris"), 1973 <a id="cite-note-5" href="#cite-ref-5">[5]</a> ). 

```

|  |
| --- |
|                                                                                      ♜ ♚    ♕♟♛     ♟    ♟ ♟  ♙   ♟  ♙   ♟  ♙      ♙    ♗♔       |

```C++
5r1k/4Qpq1/4p3/1p1p2P1/2p2P2/1p2P3/3P4/BK6 b - -

```

## By Amir Ban

[Amir Ban](Amir_Ban "Amir Ban") in a reply to [Robert Hyatt](Robert_Hyatt "Robert Hyatt") on Horizon Effect 1998 <a id="cite-note-6" href="#cite-ref-6">[6]</a> :

```C++
>not much you can do... horizon effect happens anytime you stop the search
>in a non-quiet position... everybody sees it... just get faster.. :)

```

```C++
I don't agree with this statement. The exposure to horizon effects is what usually limits a program's strength, more than the depth it can reach. The fact that it cannot be totally overcome is irrelevant to the fact that limiting its damage is a first priority. Just getting generally deeper is a poor way to do that, and not very effective either. 

```

## By Robert Hyatt

[Robert Hyatt](Robert_Hyatt "Robert Hyatt") states on Horizon Effect in 2006 <a id="cite-note-7" href="#cite-ref-7">[7]</a> :

```C++
The "horizon effect" is something caused by a fixed search horizon that the search can't penetrate. If the search can therefore force something out beyond the horizon, in effect "delaying the problem for a while" that delaying can appear to be a "permanent solution" to the problem, since if the problem is pushed beyond the horizon, so far as the search is concerned, the problem no longer exists.

```

```C++
Search extensions are one way to mitigate this, but it is impossible to eliminate. 

```

## By Gerald Tripard

[Gerald Tripard](Gerald_Tripard "Gerald Tripard") in a 2010 letter <a id="cite-note-8" href="#cite-ref-8">[8]</a> on his time at [ETH Zurich](ETH_Zurich "ETH Zurich"), his chess program [Charly](Charly "Charly"), and the match versus [Mac Hack VI](Mac_Hack "Mac Hack") in 1968 <a id="cite-note-9" href="#cite-ref-9">[9]</a>:

```C++
One of the more interesting problems of [artificial intelligence](Artificial_Intelligence "Artificial Intelligence") that I learned about in working on the chess program was called, "The Horizon Effect". If a problem could be pushed "beyond the preprogrammed" [tree search](Search "Search") [limit](Depth "Depth"), the program would make the "bad" choice of sacrificing material to avoid losing, say, a queen "within" the horizon in the situation where the queen was going to be lost eventually anyway. I see this as not just a problem of "artificial" intelligence but human thinking in general, especially of politicians. You can find wonderful examples of this in today's headlines. For example politicians "buy" the favor of a certain class of workers by offering them fabulous retirement benefits. That effectively pushes an "accounting negative balance" beyond the horizon of the politician's career. The politician gets the immediate benefit of support from the affected workers but society will eventually have to pay the bill after the politician is gone. 

```

## Crossovers

[Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer") in an additional note on [Gerald Tripard's](Gerald_Tripard "Gerald Tripard") letter <a id="cite-note-10" href="#cite-ref-10">[10]</a>:

```C++
[Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt") also noted the "Horizon Effect", of course, although I don't know if he called it by that name. One way that [Mac Hack VI](Mac_Hack "Mac Hack") attempted to combat it was via a mechanism that I believe was called "[crossovers](Quiescence_Search "Quiescence Search")". If at the conclusion of the program's [lookahead](Search "Search") (typically six [plies](Ply "Ply") deep) there were still pieces under attack, the program extended the lookahead, for those positions only, to an even greater depth. This introduced some other problems, such as comparing board [evaluations](Evaluation "Evaluation") of different [depths](Depth "Depth"). However, this seemed better than working with a board evaluation based on a position that was still in a state of flux. 

```

## Ostrich Effect

by [Gary J. Boos](Gary_Boos "Gary Boos") on [Mr. Turk](Mr._Turk "Mr. Turk") from [Ben Mittman's](Ben_Mittman "Ben Mittman") 1971 Panel <a id="cite-note-11" href="#cite-ref-11">[11]</a> <a id="cite-note-12" href="#cite-ref-12">[12]</a>:

```C++
[Mundstock](James_Mundstock "James Mundstock") noticed an article by [Slagle](James_R._Slagle "James R. Slagle") and [Bursky](Philip_Bursky "Philip Bursky") in the [Journal of the ACM](ACM#Journal "ACM")  <a id="cite-note-13" href="#cite-ref-13">[13]</a>, that pointed toward an algorithm that seemed better than [alpha-beta](Alpha-Beta "Alpha-Beta") pruning. Based upon this article, and guided by Mundstock, I wrote a lookahead routine whose main theme is that the best line is analyzed until it is shown that it is no longer the best line.

```

```C++
This process eliminates many common problems that accompany a fixed depth search, one of which is the **Ostrich Effect** which existed in even [Northwestern University's](Northwestern_University "Northwestern University")  [Chess 3.0](Chess_(Program) "Chess (Program)"). Tests showed that in a small set of positions, *Mr. Turk* could find the main variation on the first try. We believe that the basic theme of our lookahead routine is better than alpha-beta pruning. ... 

```

## See also

- [Caesar's Horizon](Caesar#HorizonEffect "Caesar")
- [Check](Check "Check")
- [Check Extensions](Check_Extensions "Check Extensions")
- [Extensions](Extensions "Extensions")
- [Horizon Node](Horizon_Node "Horizon Node")
- [Quiescent Node](Quiescent_Node "Quiescent Node")
- [Quiescence Search](Quiescence_Search "Quiescence Search")

## Publications

- [Richard Greenblatt](Richard_Greenblatt "Richard Greenblatt"), [Donald Eastlake](Donald_Eastlake "Donald Eastlake"), [Stephen D. Crocker](Stephen_D._Crocker "Stephen D. Crocker") (**1967**). *The Greenblatt Chess Program*. Proceedings of the AfiPs Fall Joint Computer Conference, Vol. 31, reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-4.Greenblatt_Chess_Program/The_Greenblatt_Chess_Program.Greenblatt_Eastlake_Crocker.1967.Fall_Joint_Computer_Conference.062303060.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum") or as [pdf or ps](http://dspace.mit.edu/handle/1721.1/6176) from [DSpace](http://libraries.mit.edu/dspace-mit/) at [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology")
- [Hans Berliner](Hans_Berliner "Hans Berliner") (**1973**). *Some Necessary Conditions for a Master Chess Program.* [3. IJCAI 1973](http://dblp.uni-trier.de/db/conf/ijcai/ijcai73.html)
- [Larry Harris](Larry_Harris "Larry Harris") (**1975**) *The Heuristic Search And The Game Of Chess - A Study Of Quiescence, Sacrifices, And Plan Oriented Play*. [4. IJCAI 1975](http://dblp.uni-trier.de/db/conf/ijcai/ijcai75.html), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") by [David Levy](David_Levy "David Levy") (Editor) B.T. Batsford, London 1988, ISBN 0-7134-4914-4, Pages 136 - 142.
- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *Dynamic Control of the [Quiescence Search](Quiescence_Search "Quiescence Search") in Computer Chess*. Cybernetics and Systems Research (ed. R. Trappl), pp. 973-977. North-Holland, Amsterdam.
- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *[Quiescence Search](Quiescence_Search "Quiescence Search") in Computer Chess.* SIGART Newsletter, 80, pp. 124-131. Reprinted (1983) in Computer-Game-Playing: Theory and Practice, pp. 39-52. Ellis Horwood Ltd., Chichester.
- [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Computer Chess and Search.* Encyclopedia of Artificial Intelligence (2nd ed.) (ed. S.C. Shapiro) pp. 224-241. John Wiley & Sons, Inc., New York, NY. ISBN 0-471-50305-3. [pdf](http://www.cs.ualberta.ca/%7Etony/RecentPapers/report.mac.pdf)
- [David Levy](David_Levy "David Levy") (**2015**). *The "Horizon Effect" in Politics*. [ICGA Journal, Vol. 38, No. 2](ICGA_Journal#38_2 "ICGA Journal")

## Horizon Effect Elsewhere

- [Guangjie Li](http://www.sigmod.org/dblp/db/indices/a-tree/l/Li:Guangjie.html) (**2009**). *The Horizon Effect of Stock Return Predictability and Model Uncertainty on Portfolio Choice*: UK Evidence, as [pdf](http://www.cardiff.ac.uk/carbs/econ/workingpapers/papers/E2009_4.pdf)

## Forum Posts

## 1995 ....

- [Horizon Effects in modern chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/0yNRLqY8frA/J8vpLc3dFeIJ) by Steve McCracken, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 05, 1995
- [Re: Horizon Effects in modern chess programs?](https://groups.google.com/d/msg/rec.games.chess.computer/0yNRLqY8frA/fkAuIzzhJ-UJ) by [Brian Sheppard](Brian_Sheppard "Brian Sheppard"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 10, 1995
- [What to do with Horizon effect?](https://www.stmintz.com/ccc/index.php?id=31199) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), October 31, 1998

## 2000 ...

- [real job of the qSearch? find quiet vs stop horizon effect](https://www.stmintz.com/ccc/index.php?id=313206) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), August 28, 2003
- [What is horizon effect?](https://www.stmintz.com/ccc/index.php?id=483299) by Masros Tukiran, [CCC](CCC "CCC"), January 29, 2006
- [Good Example of Horizon effect in Eval](http://www.talkchess.com/forum/viewtopic.php?t=19374) by [Ross Boyd](Ross_Boyd "Ross Boyd"), [CCC](CCC "CCC"), February 02, 2008
- [Horizon Effect](http://www.talkchess.com/forum/viewtopic.php?t=20070) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), March 09, 2008 <a id="cite-note-14" href="#cite-ref-14">[14]</a>

## 2010 ...

- [Horizon detection](http://www.talkchess.com/forum/viewtopic.php?t=55782) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 25, 2015
- [Ostrich tactics and pointless checks](http://www.talkchess.com/forum/viewtopic.php?t=56517) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), May 29, 2015 » [Check](Check "Check")
- ['Analogy grafting' and the horizon effect](http://www.talkchess.com/forum/viewtopic.php?t=56746) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 22, 2015
- [Horizon effect](http://www.talkchess.com/forum/viewtopic.php?t=63846) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 27, 2017
- [Horizon effect](http://www.talkchess.com/forum/viewtopic.php?t=65087) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 05, 2017
- [Horizon effect and extensions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67823) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 25, 2018 » [Extensions](Extensions "Extensions")

## 2020 ...

- [Taboo moves](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73853) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 06, 2020
- [Reducing the horizon effect](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75065) by [Mike Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), September 10, 2020

## External Links

- [Horizon effect from Wikipedia](https://en.wikipedia.org/wiki/Horizon_effect)
- [Horizon from Wikipedia](https://en.wikipedia.org/wiki/Horizon)
- [Which nodes to search? Full-width vs. selective search](http://www.ics.uci.edu/%7Eeppstein/180a/990204.html), Lecture notes for February 4, 1999 by [David Eppstein](David_Eppstein "David Eppstein")
- [Mezzoforte](Category:Mezzoforte "Category:Mezzoforte") - Beyond The Horizon, Live In Reykjavik, March 27, 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Sunset](https://en.wikipedia.org/wiki/Sunset) (created with [Terragen](https://en.wikipedia.org/wiki/Terragen) on the PC, by [Dellex](https://commons.wikimedia.org/wiki/User:Dellex), July 22, 2008)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Tony Marsland](Tony_Marsland "Tony Marsland") (**1992**). *Computer Chess and Search.* Encyclopedia of Artificial Intelligence (2nd ed.) (ed. S.C. Shapiro) pp. 224-241. John Wiley & Sons, Inc., New York, NY. ISBN 0-471-50305-3. [pdf](http://www.cs.ualberta.ca/%7Etony/RecentPapers/report.mac.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1973**). *Some Necessary Conditions for a Master Chess Program.* [3. IJCAI 1973](http://dblp.uni-trier.de/db/conf/ijcai/ijcai73.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl") (**1982**). *[Quiescence Search](Quiescence_Search "Quiescence Search") in Computer Chess.* SIGART Newsletter, 80, pp. 124-131. Reprinted (1983) in Computer-Game-Playing: Theory and Practice, pp. 39-52. Ellis Horwood Ltd., Chichester.
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Larry Harris](Larry_Harris "Larry Harris") (**1973**). *The bandwidth heuristic search*. [3. IJCAI 1973](http://dblp.uni-trier.de/db/conf/ijcai/ijcai73.html), [pdf](http://dli.iiit.ac.in/ijcai/IJCAI-73/PDF/004.pdf)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: What to do with Horizon effect?](https://www.stmintz.com/ccc/index.php?id=31258) by [Amir Ban](Amir_Ban "Amir Ban"), [CCC](CCC "CCC"), November 01, 1998
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: What is horizon effect?](https://www.stmintz.com/ccc/index.php?id=483474) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 30, 2006
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [July 1, 2010 letter from Dr. Gerald Tripard](http://ljkrakauer.com/LJK/60s/tripardltr.htm), hosted by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Computer chess via ham radio](http://ljkrakauer.com/LJK/60s/hamchess.htm) by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [July 1, 2010 letter from Dr. Gerald Tripard](http://ljkrakauer.com/LJK/60s/tripardltr.htm), hosted by [Lawrence J. Krakauer](Lawrence_J._Krakauer "Lawrence J. Krakauer")
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Ben Mittman](Ben_Mittman "Ben Mittman") (**1971**). *[Computer Chess Programs (Panel)](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d1ee8)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-3.computer_chess_panel.mittman/3-1%20and%203-3.computer_chess_panel.mittman_etc.1971.ACM.062303021.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Ostrich effect from Wikipedia](https://en.wikipedia.org/wiki/Ostrich_effect)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [James R. Slagle](James_R._Slagle "James R. Slagle"), [Philip Bursky](Philip_Bursky "Philip Bursky") (**1968**). *Experiments With a Multipurpose, Theorem-Proving Heuristic Program*. [Journal of the ACM](ACM#Journal "ACM"), Vol. 15, No. 1
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [Next (2007 film) from Wikipedia](https://en.wikipedia.org/wiki/Next_%282007_film%29)

**[Up one level](Search "Search")**

