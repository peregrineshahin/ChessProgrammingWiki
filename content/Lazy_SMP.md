---
title: Lazy SMP
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Parallel Search](Parallel_Search "Parallel Search") \* Lazy SMP**



[_(6076989366).jpg) Sloths traversing a tree <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Lazy SMP**,  

based on the [shared hash table](Shared_Hash_Table "Shared Hash Table") approach of a parallel search to profit from probing hash entries written by other instances of the search, as already used by [Vincent David's](Vincent_David "Vincent David") αβ\* <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Multiple [processes](Process "Process") or [threads](Thread "Thread") search the same [root position](Root "Root"), but are launched with different [depths](Depth "Depth"), and/or varying [move ordering](Move_Ordering "Move Ordering") at the root node, to statistically improve the gains from the effect of nondeterminism, otherwise depending on random timing fluctuations <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The term **Lazy SMP** was coined by [Julien Marcel](Julien_Marcel "Julien Marcel") end of 2012 <a id="cite-note-4" href="#cite-ref-4">[4]</a> with further elaborations by [Daniel Homan](Daniel_Homan "Daniel Homan") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>, [Martin Sedlak](Martin_Sedlak "Martin Sedlak") and others. Today, many chess programs use this easy to implement parallel search approach, which [scales](https://en.wikipedia.org/wiki/Scalability) surprisingly well up to 8 cores and beyond <a id="cite-note-7" href="#cite-ref-7">[7]</a>, not only in [nodes per second](Nodes_per_Second "Nodes per Second") (as expected), but in [playing strength](Playing_Strength "Playing Strength"), while it seems worse than [YBW](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") in [speedup](https://en.wikipedia.org/wiki/Speedup) concerning time to [depth](Depth "Depth") <a id="cite-note-8" href="#cite-ref-8">[8]</a>. Notably [Stockfish 7](Stockfish "Stockfish"), released in January 2016, switched from YBW to lazy SMP <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>. 



### Contents


* [1 Cheng's Pseudo Code](#cheng.27s-pseudo-code)
* [2 See also](#see-also)
* [3 Selected Publications](#selected-publications)
* [4 Forum Posts](#forum-posts)
	+ [4.1 2010 ...](#2010-...)
	+ [4.2 2015](#2015)
	+ [4.3 2016](#2016)
	+ [4.4 2017](#2017)
	+ [4.5 2018](#2018)
	+ [4.6 2019](#2019)
	+ [4.7 2020](#2020)
	+ [4.8 2021 ...](#2021-...)
* [5 External Links](#external-links)
* [6 References](#references)






Pseudo Code of Lazy SMP in [Cheng](Cheng "Cheng") as given by its author [Martin Sedlak](Martin_Sedlak "Martin Sedlak") <a id="cite-note-12" href="#cite-ref-12">[12]</a>:




```

IterativeDeepening:
  synchronize smp threads (copy age, board, history, repetition list, multipv => helpers)
  depth 1 with full width window on 1 thread
  loop (depth=2 .. max)
    AspirationLoop:
      (as usual)
      start helper threads( depth, alpha, beta )
      root( depth, alpha, beta)
      stop helper threads
      (rest as usual)
    end aspiration loop
  end depth loop 

starting helper threads:
  clear smp abort flag
  for each helper thread:
    copy rootmoves and minimum qs depth => helper
    signal helper to start root search at current depth (add 1 for each even helper 
     assuming 0-based indexing)  with aspiration alpha, beta bounds and wait until 
     helper starts searching 

aborting helper threads:
  set abort flag for each helper and wait for each to stop searching 

```

## See also


* [ABDADA](ABDADA "ABDADA")
* [Dynamic Tree Splitting](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [Lazy SMP](EXchess#LazySMP "EXchess") in [EXchess](EXchess "EXchess")
* [Lazy Evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
* [SMP](SMP "SMP")
* [NUMA](NUMA "NUMA")
* [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")


## Selected Publications


* [Vincent David](Vincent_David "Vincent David") (**1993**). *[Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax](http://cat.inist.fr/?aModele=afficheN&cpsidt=161774)* = Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax, Ph.D. Thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse), [France](https://en.wikipedia.org/wiki/France)


 **Abstract**: *The method of parallelization is based on a suppression of control between the search processes, in favor of a speculative parallelism and full sharing of information achieved through a physically distributed but virtually shared memory. The contribution of our approach for real-time distributed systems and fault-tolerant is evaluated through experimental results*.
* [Emil Fredrik Østensen](index.php?title=Emil_Fredrik_%C3%98stensen&action=edit&redlink=1 "Emil Fredrik Østensen (page does not exist)") (**2016**). *A Complete Chess Engine Parallelized Using Lazy SMP*. M.Sc. thesis, [University of Oslo](https://en.wikipedia.org/wiki/University_of_Oslo), [pdf](https://www.duo.uio.no/bitstream/handle/10852/53769/master.pdf?sequence=1) » [Kholin](Kholin "Kholin")


## Forum Posts


### 2010 ...


* [SMP speed up](http://www.talkchess.com/forum/viewtopic.php?t=36082) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), September 14, 2010
* [Lazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=46597) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), December 27, 2012
* [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
* [Lazy SMP, part 3](http://www.talkchess.com/forum/viewtopic.php?t=47455) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), March 09, 2013
* [Shared hash table smp result](http://www.talkchess.com/forum/viewtopic.php?t=47568) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), March 21, 2013
* [ABDADA speedup results](http://www.talkchess.com/forum/viewtopic.php?t=47887) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), May 01, 2013 » [ABDADA](ABDADA "ABDADA")
* [Measure of SMP scalability](http://www.talkchess.com/forum/viewtopic.php?t=48524) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 03, 2013
* [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013 » [Lazy SMP](EXchess#LazySMP "EXchess") in [EXchess](EXchess "EXchess")
* [cheng4 0.35](http://www.talkchess.com/forum/viewtopic.php?t=49443) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), September 24, 2013 » [Cheng](Cheng "Cheng")
* [SMP and pondering](http://www.talkchess.com/forum/viewtopic.php?t=51198) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), February 08, 2014 » [Myrddin](Myrddin "Myrddin"), [Pondering](Pondering "Pondering")
* [Nirvanachess 2.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=54671) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), December 17, 2014 » [Nirvanachess](Nirvanachess "Nirvanachess")


### 2015


* [SMP: on same branch instead splitting?](http://www.talkchess.com/forum/viewtopic.php?t=55047) by Frank Ludwig, [CCC](CCC "CCC"), January 23, 2015
* [Myrddin 0.87 release](http://www.talkchess.com/forum/viewtopic.php?t=55093) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), January 25, 2015 » [Myrddin](Myrddin "Myrddin")
* [A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), February 01, 2015


 [Re: A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170&start=3) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 01, 2015
 [Re: A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170&start=11) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 01, 2015
* [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015 » [Cheng](Cheng "Cheng")
* [Lazy SMP scaling Cheng0.38](https://groups.google.com/d/msg/fishcooking/VL4pEYZXuuM/wJSehP7SQlYJ) by Bertil, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 24, 2015
* [Trying to improve lazy smp](http://www.talkchess.com/forum/viewtopic.php?t=55970) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), April 11, 2015 » [Andscacs](Andscacs "Andscacs")
* [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015 » Lazy SMP, [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=57572) by Lucas Braesch, [CCC](CCC "CCC"), September 09, 2015
* [Lazy SMP](https://groups.google.com/d/msg/fishcooking/GVdyWSWEpQY/bZbeaJAbBgAJ) by [Mikael](Mikael_B%C3%A4ckman "Mikael Bäckman"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 26, 2015 » [Stockfish](Stockfish "Stockfish")
* [Komodo, Lazy SMP, and the like :-)](https://groups.google.com/d/msg/fishcooking/vGgxv_W_LOI/SAQOxpFsBwAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 30, 2015 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Lazy SMP Better than YBWC?](http://www.talkchess.com/forum/viewtopic.php?t=58031) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), October 23, 2015 » [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [New Stockfish with Lazy\_SMP, but what about the TC bug ?](http://www.talkchess.com/forum/viewtopic.php?t=58056) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Stockfish](Stockfish "Stockfish"), [TCEC Season 8](TCEC_Season_8 "TCEC Season 8")
* [Helper Thread Depths in the Lazy SMP algorithm](https://groups.google.com/d/msg/fishcooking/Sq8HJ7Xq0Ww/rKbWeHASBQAJ) by Rohan Ryan, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 14, 2015 » [Stockfish](Stockfish "Stockfish")
* [lazy smp questions](http://www.talkchess.com/forum/viewtopic.php?t=58645) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), December 21, 2015


### 2016


* [Lazy SMP - how it works](http://www.talkchess.com/forum/viewtopic.php?t=59389) by [Kalyankumar Ramaseshan](index.php?title=Kalyankumar_Ramaseshan&action=edit&redlink=1 "Kalyankumar Ramaseshan (page does not exist)"), [CCC](CCC "CCC"), February 29, 2016
* [Pedone 1.4](http://www.talkchess.com/forum/viewtopic.php?t=59732) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), April 03, 2016 » [Pedone](Pedone "Pedone")
* [stockfish threading model](http://www.talkchess.com/forum/viewtopic.php?t=60155) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), May 13, 2016


 [Re: stockfish threading model](http://www.talkchess.com/forum/viewtopic.php?t=60155&start=1) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 13, 2016
* [parallel search speed measurement](http://www.talkchess.com/forum/viewtopic.php?t=60271) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 24, 2016


 [Re: parallel search speed measurement](http://www.talkchess.com/forum/viewtopic.php?t=60271&start=9) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 26, 2016
* [Crazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=60537) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 19, 2016


 [Re: Crazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=60537&start=2) by [Stan Arts](Stan_Arts "Stan Arts"), [CCC](CCC "CCC"), June 20, 2016 
* [lazy smp using ms vs2015 c++11 std::async](http://www.talkchess.com/forum/viewtopic.php?t=60979) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), July 29, 2016 » [Thread](Thread "Thread") <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [Time to depth concerns](http://www.talkchess.com/forum/viewtopic.php?t=61131) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), August 15, 2016
* [Some hyperthreading results](http://www.talkchess.com/forum/viewtopic.php?t=61408) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 12, 2016 » [Thread](Thread "Thread"), [YBW](Young_Brothers_Wait_Concept "Young Brothers Wait Concept")
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")


### 2017


* [How to find SMP bugs ?](http://www.talkchess.com/forum/viewtopic.php?t=63454) by Lucas Braesch, [CCC](CCC "CCC"), March 15, 2017
* [Ideas to improve SMP scaling](http://www.open-chess.org/viewtopic.php?f=5&t=3097) by lucasart, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 03, 2017
* [Some data about LazySMP](https://groups.google.com/d/msg/fishcooking/Cbm5y4dpeEE/wYmQokNfAAAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2017 » [Stockfish](Stockfish "Stockfish")
* [Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum/viewtopic.php?t=63903) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 05, 2017 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
* [Symmetric multiprocessing (SMP) scaling - K10.4 Contempt=0](http://www.talkchess.com/forum/viewtopic.php?t=63955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 11, 2017 » [SMP](SMP "SMP"), [Komodo](Komodo "Komodo"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Symmetric multiprocessing (SMP) scaling - SF8 Contempt=10](http://www.talkchess.com/forum/viewtopic.php?t=63967) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 13, 2017 » [SMP](SMP "SMP"), [Stockfish](Stockfish "Stockfish"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Lazy SMP and "lazy cluster" experiments](http://www.talkchess.com/forum/viewtopic.php?t=64824) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017


 [Lazy SMP and lazy cluster algorithm](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=1) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017
 [SMP NPS measurements](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=2) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Nodes per Second](Nodes_per_Second "Nodes per Second")
 [ELO measurements](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=3) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017 » [Playing Strength](Playing_Strength "Playing Strength")
 [Possible improvements](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=4) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 06, 2017
 [Approximate ABDADA](http://www.talkchess.com/forum/viewtopic.php?t=64824&start=43) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), August 23, 2017 » [ABDADA](ABDADA "ABDADA")
* [lazysmp (again)](http://www.talkchess.com/forum/viewtopic.php?t=64850) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), August 09, 2017
* [Lazy SMP >4 Thread Slowdown](http://www.talkchess.com/forum/viewtopic.php?t=65844) by [Can Cetin](index.php?title=Can_Cetin&action=edit&redlink=1 "Can Cetin (page does not exist)"), [CCC](CCC "CCC"), November 29, 2017 » [Thread](Thread "Thread")


 [Re: Lazy SMP >4 Thread Slowdown](http://www.talkchess.com/forum/viewtopic.php?t=65844&start=4) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), November 29, 2017
* [Parallel search/LazySMP question](http://www.talkchess.com/forum/viewtopic.php?t=66044) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 17, 2017


### 2018


* [Lazy SMP and 44 cores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68154) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), August 07, 2018


 [Re: Lazy SMP and 44 cores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68154&start=7) by [John Stanback](John_Stanback "John Stanback"), [CCC](CCC "CCC"), August 08, 2018 » [Wasp](Wasp "Wasp")
* [Lazy SMP ideas](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68278) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 22, 2018


 [Lazy SMP ideas](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68278&start=2) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), August 23, 2018
 [Re: Lazy SMP ideas](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68278&start=16) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 03, 2018 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
### 2019


* [Simplest way to implement quick and dirty lazy smp](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69481) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 04, 2019
* [What's the best Lazy SMP logic?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69507) by Daniel Bennett, [CCC](CCC "CCC"), January 06, 2019 » [Stockfish](Stockfish "Stockfish")
* [strategies for finding slowdows in lazy smp](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70919) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), June 04, 2019 » [Nodes per Second](Nodes_per_Second "Nodes per Second"), [Thread](Thread "Thread")
* [RMO - Randomized Move Order - yet another Lazy SMP derivate](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72684) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), December 30, 2019


### 2020


* [lazy smp behaviour of stockfish](https://groups.google.com/d/msg/fishcooking/9X3lDH83tlk/DtRtuFMOCAAJ) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 05, 2020 » [Stockfish](Stockfish "Stockfish")
* [Laziest Lazy SMP](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74793) by Ian Mitchell, [CCC](CCC "CCC"), August 15, 2020
* [SMP, first shot at implementation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75088) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 12, 2020 » [Thread](Thread "Thread")
* [Very Lazy SMP and worker threads](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75151) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 18, 2020
* [Dispelling the Myth of NNUE with LazySMP: An Analysis](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76190) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 30, 2020 » [NNUE](NNUE "NNUE")


### 2021 ...


* [Stockfish search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79588) by Werewolf, [CCC](CCC "CCC"), March 26, 2022 » [Stockfish](Stockfish "Stockfish")


## External Links


* [lazy - Wiktionary](https://en.wiktionary.org/wiki/lazy)
* [Lazy from Wikipedia](https://en.wikipedia.org/wiki/Lazy)
* [Laziness from Wikipedia](https://en.wikipedia.org/wiki/Laziness)
* [Sloth (deadly sin) from Wikipedia](https://en.wikipedia.org/wiki/Sloth_(deadly_sin))
* [Symmetric multiprocessing (SMP) from Wikipedia](https://en.wikipedia.org/wiki/Symmetric_multiprocessing)
* [Lazy evaluation from Wikipedia](https://en.wikipedia.org/wiki/Lazy_evaluation)
* [Small Faces](Category:Small_Faces "Category:Small Faces") - [Lazy Sunday](https://en.wikipedia.org/wiki/Lazy_Sunday_(Small_Faces_song)), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Three-toed sloth](https://en.wikipedia.org/wiki/Three-toed_sloth), [Image](https://commons.wikimedia.org/wiki/File:Our_living_world_(Full_Page_Illustration)_(6076989366).jpg?uselang=en) by [Friedrich Specht](https://en.wikipedia.org/wiki/Friedrich_Specht) in [Joseph Bassett Holder](https://en.wikipedia.org/wiki/Joseph_Bassett_Holder), [John George Wood](https://en.wikipedia.org/wiki/John_George_Wood) (**1885**). *[Our living world; an artistic edition of the Rev. J. G. Wood's Natural history of animate creation](http://www.biodiversitylibrary.org/bibliography/49480#/summary)*. New York : Selmar Hess, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Vincent David](Vincent_David "Vincent David") (**1993**). *[Algorithmique parallèle sur les arbres de décision et raisonnement en temps contraint. Etude et application au Minimax](http://cat.inist.fr/?aModele=afficheN&cpsidt=161774)* = Parallel algorithm for heuristic tree searching and real-time reasoning. Study and application to the Minimax, Ph.D. Thesis, [École nationale supérieure de l'aéronautique et de l'espace](https://en.wikipedia.org/wiki/%C3%89cole_nationale_sup%C3%A9rieure_de_l%27a%C3%A9ronautique_et_de_l%27espace), [Toulouse](https://en.wikipedia.org/wiki/Toulouse), [France](https://en.wikipedia.org/wiki/France)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Lazy SMP - how it works](http://www.talkchess.com/forum/viewtopic.php?t=59389&start=5) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 19, 2016
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Lazy SMP](http://www.talkchess.com/forum/viewtopic.php?t=46597) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), December 27, 2012
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Lazy SMP, part 2](http://www.talkchess.com/forum/viewtopic.php?t=46858) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), January 12, 2013
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Lazy SMP and Work Sharing](http://www.talkchess.com/forum/viewtopic.php?t=48536) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), July 03, 2013
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: A new chess engine : m8 (comming not so soon)](http://www.talkchess.com/forum/viewtopic.php?t=55170&start=11) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 01, 2015
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Time to depth concerns](http://www.talkchess.com/forum/viewtopic.php?t=61131) by [Carl Bicknell](index.php?title=Carl_Bicknell&action=edit&redlink=1 "Carl Bicknell (page does not exist)"), [CCC](CCC "CCC"), August 15, 2016
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58779) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), January 02, 2016
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Threads test incl. Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58887) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 11, 2016
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Stockfish 7 progress](http://www.talkchess.com/forum/viewtopic.php?t=58935) by Carl Lumma, [CCC](CCC "CCC"), January 16, 2016
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Lazy SMP in Cheng](http://www.talkchess.com/forum/viewtopic.php?t=55188) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), February 02, 2015 » [Cheng](Cheng "Cheng")
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [std::async - cppreference.com](http://en.cppreference.com/w/cpp/thread/async)

**[Up one level](Parallel_Search "Parallel Search")**







 
