---
title: BetaCutoff
---
**[Home](Home "Home") * [Search](Search "Search") * [Alpha-Beta](Alpha-Beta "Alpha-Beta") * Beta-Cutoff**

\[ Cut-off <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **beta-cutoff** occurs in the [alpha-beta algorithm](Alpha-Beta "Alpha-Beta"), if the [score](Score "Score") backed up by the search is greater than or equal to [beta](Beta "Beta") and [fails high](Fail-High "Fail-High"). No further [moves](Moves "Moves") need to be searched, since one [refutation](Refutation_Move "Refutation Move") is already sufficient to avoid the move that led to this [node](Node "Node") or [position](Chess_Position "Chess Position"). Nodes, where a beta-cutoff occurs are then [cut-nodes](Node_Types#cut-nodes "Node Types") where [move ordering](Move_Ordering "Move Ordering") was crucial to try the refutation move as early as possible - typically as first move in 90 to 95 per cent of all cases. In [max versus min alpha-beta](Alpha-Beta#MaxversusMin "Alpha-Beta") a beta-cutoff can only occur for the max-player, while the min-player cuts if below or equal alpha, called **alpha-cutoff**. Since the common [negamax](Negamax "Negamax") implementation makes both players maximizers, [negamax alpha-beta](Alpha-Beta#Negamax "Alpha-Beta") has beta-cutoffs exclusively for both players.

## Shallow or Deep

A **shallow** cutoff occurs if the [window](Window "Window") was narrowed at the parent node, that is, reduced current beta. A **deep** cutoff occurs if the [window](Window "Window") was narrowed closer to the [root](Root "Root") with an odd ply-distance of at least three to the current node. Deep cutoffs were sometimes omitted in early chess programs if not passing [alpha](Alpha "Alpha") through the [recursive](Recursion "Recursion") call <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

|  |  |  |
| --- | --- | --- |
| [Shallowcutoff.jpg](File:Shallowcutoff.jpg) |  | [Deepcutoff.jpg](File:Deepcutoff.jpg) |
|  Shallow Cutoff if α >= β
|  |  Deep Cutoff if α >= β <a id="cite-note-3" href="#cite-ref-3">[3]</a> |

## See also

- [Cut-Nodes](Node_Types#cut-nodes "Node Types")
- [Cutoff ratio in Sierżant](Sier%C5%BCant#Cutratio "Sierżant")
- [Fail-Hard](Fail-Hard "Fail-Hard")
- [Fail-High](Fail-High "Fail-High")
- [Fail-Low](Fail-Low "Fail-Low")
- [Fail-Soft](Fail-Soft "Fail-Soft")

## Forum Posts

- [Cutoffs in Quiescence Search](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64940) by jfern2011, [CCC](CCC "CCC"), August 20, 2017 » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [cut nodes](http://www.talkchess.com/forum/viewtopic.php?t=65477) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 18, 2017  » [Cut-Nodes](Node_Types#cut-nodes "Node Types")
- [Transposition table based cutoffs](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79647) by Michal Witanowski, [CCC](CCC "CCC"), April 05, 2022  » [Transposition Table](Transposition_Table "Transposition Table")

## External Links

- [cutoff - Wiktionary](https://en.wiktionary.org/wiki/cutoff)
- [cut off - Wiktionary](https://en.wiktionary.org/wiki/cut_off)
- [Cutoff from Wikipedia](https://en.wikipedia.org/wiki/Cutoff)
- [Cut-off from Wikipedia](https://en.wikipedia.org/wiki/Cut-off)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> A Biker's vintage cut-off adorned with club badges, Image by [Bullenwächter](https://commons.wikimedia.org/wiki/User:Bullenw%C3%A4chter), December 12, 2004, [Cut-off from Wikipedia](https://en.wikipedia.org/wiki/Cut-off), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: What the computer chess community needs to decide](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=394125&t=38007) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), February 11, 2011
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Modified images from [Matthew L. Ginsberg](Matthew_L._Ginsberg "Matthew L. Ginsberg"), [Alan Jaffray](index.php?title=Alan_Jaffray&action=edit&redlink=1 "Alan Jaffray (page does not exist)") (**2002**). *Alpha-Beta Pruning Under Partial Orders*. in [Richard J. Nowakowski](Richard_J._Nowakowski "Richard J. Nowakowski") (ed.) *[More Games of No Chance](http://library.msri.org/books/Book42/)*. [Cambridge University Press](https://en.wikipedia.org/wiki/Cambridge_University_Press), [pdf](http://library.msri.org/books/Book42/files/ginsberg.pdf)

**[Up one Level](Alpha-Beta "Alpha-Beta")**

