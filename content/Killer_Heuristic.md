---
title: Killer Heuristic
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Killer Heuristic**



[ Jack the Ripper <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Killer Heuristic**,  

a dynamic, path-dependent move ordering technique. It considers moves that caused a [beta-cutoff](Beta-Cutoff "Beta-Cutoff") in a [sibling node](Sibling_Node "Sibling Node") as [killer moves](Killer_Move "Killer Move") and orders them high on the [list](Move_List#SearchLists "Move List"). When a [node](Node "Node") [fails high](Fail-High "Fail-High"), a [quiet move](Quiet_Moves "Quiet Moves") that caused a cutoff is stored in a table indexed by [ply](Ply "Ply"), typically containing two or three moves per ply. The replacement scheme ought to ensure that all the available slots contain **different** moves. 



## How does it work?


Killer moves work on the supposition that most of the moves do not change the situation on the board too much. For example if a program decides that expelling a black bishop from b4 by a move a2-a3 is good, then it is likely to work whatever Black played on the previous move: ...Bd7, ...Be6, ...h6 etc. After the first fail-high caused by a2-a3 this move is remembered as a killer move. So when Black backtracks ...Bd7 and tries ...Be6, move a2-a3, normally having rather low priority, waits to be tried as one of the first in a new, but not-too-different position. Of course, most of the cutoffs come from the first killer slot. But occasionally opponent does something important, like attacking a queen. Program reacts, and has a good luck to fail high again, getting a new killer move... useful only as an evasion. That's where the second slot comes in handy. It prevents a program from forgetting the right plan because of occasional noise caused by switching to more urgent moves.



## See also


* [Butterfly Heuristic](Butterfly_Heuristic "Butterfly Heuristic")
* [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Fixafan](Fixafan "Fixafan")
* [History Heuristic](History_Heuristic "History Heuristic")
* [Killer Move](Killer_Move "Killer Move")
* [Last Best Reply](Last_Best_Reply "Last Best Reply")
* [Mate Killers](Mate_Killers "Mate Killers")
* [Refutation Table](Refutation_Table "Refutation Table")
* [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")
* [Vice Video](Vice#KillHist "Vice")


## Publications


* [Barbara J. Huberman](Barbara_Liskov "Barbara Liskov") (**1968**). *A Program to Play Chess End Games*. Technical Report no. CS-106, Ph.D. thesis. [Stanford University](Stanford_University "Stanford University"), Computer Science Department <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [James Gillogly](James_Gillogly "James Gillogly") (**1971**). *[The Technology Chess Program](http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=html&identifier=AD0736043)*. [Carnegie Mellon University](Carnegie_Mellon_University "Carnegie Mellon University"), CS-71-109, [pdf](http://repository.cmu.edu/cgi/viewcontent.cgi?article=2974&context=compsci)
* [Selim Akl](Selim_Akl "Selim Akl"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1977**). *The Principal Continuation and the Killer Heuristic*. 1977 ACM Annual Conference Proceedings, pp. 466-473. ACM, Seattle, WA.
* [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jan Derksen](Jan_Derksen "Jan Derksen"), [John Huisman](John_Huisman "John Huisman") (**1982**). *[De Killer-Heuristiek](https://pure.uvt.nl/portal/en/publications/de-killerheuristiek%28945033e5-8d1f-4339-bb92-e67c79cb33d5%29.html)*. [Computerschaak](Computerschaak "Computerschaak"), Vol. 2, No. 3 (Dutch)
* [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal"), pp. 8, The killer heuristic
* [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University"), advisor [Monroe Newborn](Monroe_Newborn "Monroe Newborn") » [Fixafan](Fixafan "Fixafan")
* [Junichi Hashimoto](Junichi_Hashimoto "Junichi Hashimoto"), [Tsuyoshi Hashimoto](Tsuyoshi_Hashimoto "Tsuyoshi Hashimoto"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2007**). *[Context Killer Heuristic and Its Application to Computer Shogi](https://www.researchgate.net/publication/258121764_Context_Killer_Heuristic_and_Its_Application_to_Computer_Shogi)*. [CGW 2007](CGW_2007 "CGW 2007")


## Forum Posts


### 1995 ...


* [Killer moves](http://groups.google.com/group/gnu.chess/browse_frm/thread/fb62cff6dea1bf09) by [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian"), [gnu.chess](GNU_Chess#NewsGroup "GNU Chess"), March 21, 1995
* [Unusual killer heuristic behavior](https://groups.google.com/d/msg/rec.games.chess.computer/jlFU_HW-qSY/z7R0NOjZYOIJ) by [Matt Craighead](Matt_Craighead "Matt Craighead"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 10, 1995 » [Morgoth](Morgoth "Morgoth")
* [Killer and history](https://www.stmintz.com/ccc/index.php?id=21072) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](CCC "CCC"), June 22, 1998
* [Killer Move Heuristic Questions](https://www.stmintz.com/ccc/index.php?id=54116) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), June 03, 1999


### 2000 ...


* [What is the Success Rate of Killer/History Moves?](https://www.stmintz.com/ccc/index.php?id=113078) by [Roberto Waldteufel](Roberto_Waldteufel "Roberto Waldteufel"), [CCC](CCC "CCC"), May 31, 2000
* [About history heuristics, killers and my futil. pruning code](https://www.stmintz.com/ccc/index.php?id=143331) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), December 06, 2000 » [History Heuristic](History_Heuristic "History Heuristic")
* [MTD(f) and killer heuristics](https://www.stmintz.com/ccc/index.php?id=179391) by Marcus Heidkamp, [CCC](CCC "CCC"), July 12, 2001 » [MTD(f)](MTD(f) "MTD(f)")
* [killers and history](https://www.stmintz.com/ccc/index.php?id=278991) by [Nathan Thom](Nathan_Thom "Nathan Thom"), [CCC](CCC "CCC"), January 22, 2003 » [History Heuristic](History_Heuristic "History Heuristic")
* [Killer Moves](https://www.stmintz.com/ccc/index.php?id=306149) by Rick Bischoff, [CCC](CCC "CCC"), July 12, 2003
* [killer moves?](https://www.stmintz.com/ccc/index.php?id=325602) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 04, 2003
* [Two questions: Bratko Kopec and variations on the killer heuristic](https://www.stmintz.com/ccc/index.php?id=357334) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 31, 2004 » [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")
* [Killer modifications reduced tree size by 8% (with identical results)](https://www.stmintz.com/ccc/index.php?id=357640) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), March 31, 2004
* [The Null Move Killer](https://www.stmintz.com/ccc/index.php?id=389695) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), September 29, 2004


### 2005 ...


* [Killer Moves](http://www.talkchess.com/forum/viewtopic.php?t=20068) by colin, [CCC](CCC "CCC"), March 09, 2008
* [killer moves and history heuristic table](http://www.talkchess.com/forum/viewtopic.php?t=24920) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), November 17, 2008 » [History Heuristic](History_Heuristic "History Heuristic")
* [Killer Curiosity](http://www.talkchess.com/forum/viewtopic.php?t=27315) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 04, 2009
* [Killer moves (ply or depth?)](http://www.talkchess.com/forum/viewtopic.php?t=29077) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), July 22, 2009


### 2010 ...


* [Killer moves with null move pruning](http://www.talkchess.com/forum/viewtopic.php?t=35045) by Ricardo Barreira, [CCC](CCC "CCC"), June 19, 2010
* [Killer moves?](http://www.talkchess.com/forum/viewtopic.php?t=40423) by Mike Robinson, [CCC](CCC "CCC"), September 16, 2011
* [Killer and History: Increased Node Count](http://www.talkchess.com/forum/viewtopic.php?t=46886) by [Cheney Nattress](index.php?title=Cheney_Nattress&action=edit&redlink=1 "Cheney Nattress (page does not exist)"), [CCC](CCC "CCC"), January 15, 2013
* [Killer and move encoding](http://www.talkchess.com/forum/viewtopic.php?t=53289) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 14, 2014 » [Encoding Moves](Encoding_Moves "Encoding Moves")
* [Effectiveness of killer moves](http://www.talkchess.com/forum/viewtopic.php?t=53317) by [Alex Ferguson](index.php?title=Alex_Ferguson&action=edit&redlink=1 "Alex Ferguson (page does not exist)"), [CCC](CCC "CCC"), August 17, 2014


### 2015 ...


* [killer trees](http://www.talkchess.com/forum/viewtopic.php?t=55438) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 23, 2015
* [Killer moves based on distance to common ancestor](http://www.talkchess.com/forum/viewtopic.php?t=56540) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), May 30, 2015


**2016**



* [Killer Table between searches?](http://www.talkchess.com/forum/viewtopic.php?t=61076) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), August 08, 2016
* [New killer idea](http://www.talkchess.com/forum/viewtopic.php?t=61260) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), August 28, 2016
* [Killer heuristic](http://www.talkchess.com/forum/viewtopic.php?t=61399) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 11, 2016


**2017**



* [Mate Killer Move](http://www.open-chess.org/viewtopic.php?f=5&t=3077) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 02, 2017 » [Mate Killers](Mate_Killers "Mate Killers")
* [TTMove legality checking ? & Killers Move Format?](http://www.talkchess.com/forum/viewtopic.php?t=63090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 08, 2017 » [Hash Move](Hash_Move "Hash Move"), [Killer Move](Killer_Move "Killer Move")
* [Early killer](http://www.talkchess.com/forum/viewtopic.php?t=63756) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 16, 2017
* [Deep killers](http://www.talkchess.com/forum/viewtopic.php?t=64925) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 18, 2017
* [LMR and killer](http://www.talkchess.com/forum/viewtopic.php?t=65169) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 14, 2017 » [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")


**2018 ...**



* [Saving killer moves...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67224) by [Vince Sempronio](index.php?title=Vince_Sempronio&action=edit&redlink=1 "Vince Sempronio (page does not exist)"), [CCC](CCC "CCC"), April 25, 2018
* [Killers and forward pruning test searches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69744) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), January 27, 2019


### 2020 ...


* [How much ELO should I expect to gain from killer moves?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77734) by Christian Dean, [CCC](CCC "CCC"), July 16, 2021 » [Playing Strength](Playing_Strength "Playing Strength")


## External Links


* [Killer heuristic from Wikipedia](https://en.wikipedia.org/wiki/Killer_heuristic)
* [Killer from Wikipedia](https://en.wikipedia.org/wiki/Killer)
* [Foolkiller from Wikipedia](https://en.wikipedia.org/wiki/Foolkiller)
* [Brian Auger](Category:Brian_Auger "Category:Brian Auger") and the [Trinity](https://en.wikipedia.org/wiki/Brian_Auger_and_the_Trinity) - [Fool Killer](https://www.youtube.com/watch?v=QD7buurf5FM) ([Mose Allison](https://en.wikipedia.org/wiki/Mose_Allison) <a id="cite-note-3" href="#cite-ref-3">[3]</a>), 1965, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Talking Heads](https://en.wikipedia.org/wiki/Talking_Heads) - [Psycho Killer](https://en.wikipedia.org/wiki/Psycho_Killer), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


 1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> One of a series of images from the [Illustrated London News](https://en.wikipedia.org/wiki/The_Illustrated_London_News) for October 13, 1888 carrying the overall caption, "With the Vigilance Committee in the East End". This specific image is entitled "A Suspicious Character", [Jack the Ripper from Wikipedia](https://en.wikipedia.org/wiki/Jack_the_Ripper), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**1992**). *The Countermove Heuristic*. [ICCA Journal, Vol. 15, No. 1](ICGA_Journal#15_1 "ICGA Journal"), pp. 8, The killer heuristic
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Brian Auger-und-The-Trinity-und-Julie-Driscoll The-Mod-years](http://www.green-brain-krautrock.de/BRIAN-AUGER-und-THE-TRINITY-und-JULIE-DRISCOLL-The-Mod-years-CD-MadeInGermany_17962.html)

**[Up one Level](Move_Ordering "Move Ordering")**







 
