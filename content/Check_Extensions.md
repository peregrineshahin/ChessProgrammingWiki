---
title: Check Extensions
---
**[Home](Home "Home") * [Search](Search "Search") * [Selectivity](Selectivity "Selectivity") * [Extensions](Extensions "Extensions") * Check Extensions**

**Check Extensions** have two distinct forms: one of them extends when giving [check](Check "Check"), the other - when *evading* it. In each case, typical [depth](Depth "Depth") to extend is **one** ply. The reason behind check extension is that we are in a forcing sequence, so that it is desirable to know its outcome with more certainty, and the number of replies to check is limited, so we do not have to be afraid of a [search explosion](Search_Explosion "Search Explosion"). Also, not extending checks may easily lead to the [horizon effect](Horizon_Effect "Horizon Effect"), delaying the threat so far that the program cannot see it. However, some programmers don't extend checks (and captures) with negative [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") or even [reduce](Reductions "Reductions") them. [Robert Hyatt](Robert_Hyatt "Robert Hyatt") claimed a significant gain in [Crafty](Crafty "Crafty") by doing so <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

If a program does not consider checks in the [quiescence search](Quiescence_Search "Quiescence Search"), then we should take care that it does not enter it while in check. This is also a form of check extension <a id="cite-note-3" href="#cite-ref-3">[3]</a>. In its most straightforward form, check extension is implemented in [TSCP](TSCP "TSCP").

## See also

- [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
- [Singular Extensions](Singular_Extensions "Singular Extensions")

## Forum Posts

## 2000 ...

- [Check Extension](https://www.stmintz.com/ccc/index.php?id=274620) by [Martin Bauer](Martin_Bauer "Martin Bauer"), [CCC](CCC "CCC"), January 03, 2003
- [What's best low BF or good WAC result?](https://www.stmintz.com/ccc/index.php?id=289795) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 18, 2003 » [Win at Chess](Win_at_Chess "Win at Chess")
- [Buggy check extensions, back to square one =(.](https://www.stmintz.com/ccc/index.php?id=290060) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 20, 2003
- [check extention explosion](https://www.stmintz.com/ccc/index.php?id=358170) by Aivaras Juzvikas, [CCC](CCC "CCC"), April 03, 2004 » [Search Explosion](Search_Explosion "Search Explosion")
- [Checks in QSearch](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=702&p=2642) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), November 23, 2004 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")

## 2005 ...

- [hashing, check extensions and depth](http://www.talkchess.com/forum/viewtopic.php?t=14075) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), May 27, 2007
- [Revisiting Check Extensions](http://www.talkchess.com/forum/viewtopic.php?t=14333) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 07, 2007
- [checks in q-search](http://www.talkchess.com/forum/viewtopic.php?t=23447) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 02, 2008
- [check extension](http://www.talkchess.com/forum/viewtopic.php?t=22840) by [Andrew Short](index.php?title=Andrew_Short&action=edit&redlink=1 "Andrew Short (page does not exist)"), [CCC](CCC "CCC"), August 07, 2008
- [check extensions](http://www.talkchess.com/forum/viewtopic.php?t=24614) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), October 28, 2008
- [Check extension](http://www.talkchess.com/forum/viewtopic.php?t=27384) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 09, 2009

## 2010 ...

- [Problem with exploding tree because of extensions](http://www.talkchess.com/forum/viewtopic.php?t=31505) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 05, 2010
- [Problems when implementing checks in qsearch](http://talkchess.com/forum/viewtopic.php?t=32345) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), February 03, 2010 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [Spite checks](http://www.talkchess.com/forum/viewtopic.php?t=52309) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 13, 2014
- [Pointless delays](http://www.talkchess.com/forum/viewtopic.php?t=53078) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), July 25, 2014

## 2015 ...

- [Check-extension in QS](http://www.talkchess.com/forum/viewtopic.php?t=55874) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 03, 2015 » [Checks in Quiescence Search](Quiescence_Search#Checks "Quiescence Search")
- [Is a Check Extension Really a Win?](http://www.talkchess.com/forum/viewtopic.php?t=56361) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), May 15, 2015
- [Spite checks, again](http://www.talkchess.com/forum/viewtopic.php?t=61803) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 23, 2016
- [Starting with check extensions](http://www.talkchess.com/forum/viewtopic.php?t=63303) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), February 28, 2017
- [Check Extensions](http://www.talkchess.com/forum/viewtopic.php?t=63319) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), March 02, 2017
- [Check extension vs LMR](http://www.talkchess.com/forum/viewtopic.php?t=63649) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 04, 2017 » [LMR](Late_Move_Reductions "Late Move Reductions")
- [Depth extensions and effect on transposition queries](http://www.talkchess.com/forum/viewtopic.php?t=67131) by [Kenneth Jones](index.php?title=Kenneth_Jones&action=edit&redlink=1 "Kenneth Jones (page does not exist)"), [CCC](CCC "CCC"), April 16, 2018 » [Transposition Table](Transposition_Table "Transposition Table")
- [check extension](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69131) by lucasart, [CCC](CCC "CCC"), December 03, 2018

## External Links

- [Check extension](http://web.archive.org/web/20070607151732/www.brucemo.com/compchess/programming/extensions.htm#check) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Re: move count based pruning](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=368875&t=35955) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 04, 2010
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [search extensions](http://www.talkchess.com/forum/viewtopic.php?t=54281) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), November 08, 2014
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [checks in q-search](http://www.talkchess.com/forum/viewtopic.php?t=23447) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 02, 2008

**[Up one Level](Extensions "Extensions")**

