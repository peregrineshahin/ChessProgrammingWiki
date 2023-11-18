---
title: Late Move Reductions
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Selectivity](Selectivity "Selectivity") \* [Reductions](Reductions "Reductions") \* Late Move Reductions**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc8) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Other Rules <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Late Move Reductions (LMR)**,  

or its version known as **History Pruning** and **History Reductions** <a id="cite-note-2" href="#cite-ref-2">[2]</a> , save search by reducing [moves](Moves "Moves") that are [ordered](Move_Ordering "Move Ordering") closer to the end of likely [fail-low nodes](Node_Types#All-Nodes "Node Types"). Typically, most schemes search the first few moves (say 3-4) at full [depth](Depth "Depth"), then if no move [fails high](Fail-High "Fail-High"), many of the remaining moves are reduced in search [depth](Depth "Depth"). The technique has been used for many years in various forms, but it became very popular in 2005 after [Fruit](Fruit "Fruit") and [Glaurung](Glaurung "Glaurung") <a id="cite-note-3" href="#cite-ref-3">[3]</a> used open source implementations based on the [History Heuristic](History_Heuristic "History Heuristic"). LMR can often reduce the [effective branching factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor") to less than 2, depending on the reduction conditions. 



## Less Common Conditions


Less common conditions on moves not to reduce:



* [Passed Pawn](Passed_Pawn "Passed Pawn") Moves
* [Killer Moves](Killer_Heuristic "Killer Heuristic")
* Moves threatening the King area
* [Tactically](Tactics "Tactics") threatening moves
* Moves with good past [relative history](Relative_History_Heuristic "Relative History Heuristic") <a id="cite-note-4" href="#cite-ref-4">[4]</a>
* Any [Pawn Moves](Pawn_Push "Pawn Push")
* Reductions of "good" [captures](Captures "Captures") ([SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0)
* Moves of a [threatened piece](Null_Move_Pruning#ThreatDetection "Null Move Pruning") to safety (often detected via a [Null Move search](Null_Move_Pruning "Null Move Pruning"))


## Reduction Depth


Classical implementation reduces by one [ply](Ply "Ply") only. Yet modern programs, most notably [Stockfish](Stockfish "Stockfish"), allow reductions of more than one ply and increase them for later moves. Base reduction depth changes according to [depth](Depth "Depth") and move number, with further adjustments being made depending on certain conditions. Here are some sample base formulas can be viewed:


* [Weiss](Weiss "Weiss") reduces by `0.20 + ln(depth) * ln(move number) / 3.35` for captures and promotions and `1.35 + ln(depth) * ln(move number) / 2.75` for quiet moves.
* [Ethereal](Ethereal "Ethereal") reduces by `0.7844 + ln(depth) * ln(moves played) / 2.4696` for quiet moves and `3` (or `2` if the move gave check) for captures and promotions

### LMR adjustments


After determining a base value, several adjustments can be made to the reduction depending on certain conditions.

Some common conditions to reduce less:

* Move gives check
* Move is a [killer move](Killer_Heuristic "Killer Heuristic") or a [countermove](Countermove_Heuristic "Countermove Heuristic")
* We are on a [PV-node](Node_Types#PV-Node "Node Types")
* Move has a good [history](History_Heuristic "History Heuristic") score
* Move has a good [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") score

Some common conditions to reduce more:
* We are on an expected [cut-node](Node_Types#Cut-Nodes "Node Types")
* Move has a bad [history](History_Heuristic "History Heuristic") score
* Our score is not improving (ie our current evaluation is less than or equal to the evaluation from two [plies](Ply "Ply") ago)

## Re-searches

Classical implementation assumes a re-search at full depth if the reduced depth search returns a score above alpha. However, modern implementations have a triple-search system for [PV-nodes](Node_Types#PV-Node "Node Types") and a double search system for non PV-nodes.



## Test Results

Some test results related to LMR can be found on



* [Late Move Reduction Test Results](Late_Move_Reduction_Test_Results "Late Move Reduction Test Results")


## See also


* [Parallelism and Selectivity in Game Tree Search | Video](Tord_Romstad#Video "Tord Romstad"), Talk by [Tord Romstad](Tord_Romstad "Tord Romstad")
* [Bobby's Strategic Quiescence Search](Bobby#StrategicQuiescenceSearch "Bobby")
* [History Heuristic](History_Heuristic "History Heuristic")
* [History Leaf Pruning](History_Leaf_Pruning "History Leaf Pruning")
* [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Late Move Pruning)
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")
* [SEX Algorithm](SEX_Algorithm "SEX Algorithm")


## Publications


* [David Levy](David_Levy "David Levy"), [David Broughton](David_Broughton "David Broughton"), [Mark Taylor](Mark_Taylor "Mark Taylor") (**1989**). *The SEX Algorithm in Computer Chess*. [ICCA Journal, Vol. 12, No. 1](ICGA_Journal#12_1 "ICGA Journal")
* [Kunihito Hoki](Kunihito_Hoki "Kunihito Hoki"), [Masakazu Muramatsu](Masakazu_Muramatsu "Masakazu Muramatsu") (**2012**). *[Efficiency of three Forward-Pruning Techniques in Shogi: Futility Pruning, Null-move Pruning, and Late Move Reduction (LMR)](https://www.semanticscholar.org/paper/Efficiency-of-three-forward-pruning-techniques-in-Hoki-Muramatsu/206099961f401c8693e071c2b739f164ae5ffa6c)*. [Entertainment Computing](https://www.journals.elsevier.com/entertainment-computing), Vol. 3, No. 3
* [Daniel S. Abdi](Daniel_Shawul "Daniel Shawul") (**2013**). *Analysis of pruned minimax trees*. [pdf](https://dl.dropboxusercontent.com/u/55295461/analysis/pruning.pdf) » [Alpha-Beta](Alpha-Beta "Alpha-Beta"), [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")


## Forum Posts

### 2004


* [Forward pruning and some related techniques](https://www.stmintz.com/ccc/index.php?id=352384) by [Sergei Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), March 02, 2004


### 2005 ...


* [Reductions and null move refutations](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2300&p=10549) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 18, 2005 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [What is History Pruning?](https://www.stmintz.com/ccc/index.php?id=434809) by [David Dahlem](index.php?title=David_Dahlem&action=edit&redlink=1 "David Dahlem (page does not exist)"), [CCC](CCC "CCC"), July 03, 2005
* [History based pruning question](https://www.stmintz.com/ccc/index.php?id=445457) by [Alvaro Jose Povoa Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), August 26, 2005
* [About history pruning...](https://www.stmintz.com/ccc/index.php?id=457846) by Svein Bjørnar Myrvang, [CCC](CCC "CCC"), October 26, 2005
* [What is "history pruning"?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=3795) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 07, 2005


**2006**



* [History pruning](https://www.stmintz.com/ccc/index.php?id=489978) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), February 27, 2006
* [late move reductions](https://www.stmintz.com/ccc/index.php?id=490705) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 01, 2006


 [Re: late move reductions](https://www.stmintz.com/ccc/index.php?id=490712) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), March 01, 2006 » [Kiwi](Kiwi "Kiwi")
 [PHR (Peak History Reduction) idea](https://www.stmintz.com/ccc/index.php?id=490779) by [Daniel Mehrmann](Daniel_Mehrmann "Daniel Mehrmann"), [CCC](CCC "CCC"), March 01, 2006 » [Home](Home "Home"), [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")
* [history pruning/ late move pruning](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4435&p=23839) by [Tom King](Tom_King "Tom King"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006
* [LMR question](http://www.open-aurec.com/wbforum/viewtopic.php?t=5194) by [Uri Blass](Uri_Blass "Uri Blass"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2006


**2007**



* [LMR in micro-Max](http://www.talkchess.com/forum/viewtopic.php?t=12936) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 07, 2007 » [Micro-Max](Micro-Max "Micro-Max")
* [Fruit and History Reductions](http://www.talkchess.com/forum/viewtopic.php?t=15219) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 19, 2007 » [Fruit](Fruit "Fruit")
* [LMR other conditions](http://www.talkchess.com/forum/viewtopic.php?t=15304) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), July 23, 2007
* [Improving history tables](http://www.talkchess.com/forum/viewtopic.php?t=15337) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 25, 2007
* [LMR: history or not?](http://www.talkchess.com/forum/viewtopic.php?t=18345) by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti"), [CCC](CCC "CCC"), December 13, 2007 » [Hamsters](Hamsters "Hamsters")


**2008**



* [Extreme late move reductions?](http://www.talkchess.com/forum/viewtopic.php?p=178438) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 05, 2008
* [LMR?](http://www.talkchess.com/forum/viewtopic.php?t=20636) by [Martin Giepmans](Martin_Giepmans "Martin Giepmans"), [CCC](CCC "CCC"), April 12, 2008  » [Anatoli](Anatoli "Anatoli")
* [Adaptative LMR and TT](http://www.talkchess.com/forum/viewtopic.php?t=25599) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), December 23, 2008


**2009**



* [About LMR & History reductions](http://www.talkchess.com/forum/viewtopic.php?t=26703) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), February 24, 2009
* [LMR](http://www.talkchess.com/forum/viewtopic.php?t=26877) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 05, 2009
* [LMR and 'tactically connected' moves](http://www.talkchess.com/forum/viewtopic.php?t=26944) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 10, 2009
* [LMR revisited](http://www.talkchess.com/forum/viewtopic.php?t=27277) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), April 01, 2009
* [LMR and null move selectivity](http://www.talkchess.com/forum/viewtopic.php?t=27530) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), April 20, 2009
* [LMR](http://www.talkchess.com/forum/viewtopic.php?t=29944) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), September 30, 2009
* [May I Ask What You Think Of This?](http://www.talkchess.com/forum/viewtopic.php?t=30245) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](CCC "CCC"), October 20, 2009
* [Did people try replacing LMR by pruning](http://www.talkchess.com/forum/viewtopic.php?t=31369) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), December 31, 2009


### 2010 ...


* [The problem with LMR in suprtactical positions](http://www.talkchess.com/forum/viewtopic.php?t=31494) by [Oliver Brausch](Oliver_Brausch "Oliver Brausch"), [CCC](CCC "CCC"), January 05, 2010
* [Researching if LMR-affected search improves Alpha?](http://www.talkchess.com/forum/viewtopic.php?t=31933) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), January 22, 2010
* [Problems with LMR in late endgames](http://talkchess.com/forum/viewtopic.php?t=32984) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), March 01, 2010
* [LMR algorithm](http://www.talkchess.com/forum/viewtopic.php?t=33265) by kenny stanley, [CCC](CCC "CCC"), March 15, 2010
* [LMR Conditions](http://www.talkchess.com/forum/viewtopic.php?t=33434) by kenny stanley, [CCC](CCC "CCC"), March 23, 2010
* [LMR at root of search tree - worthwhile?](http://www.talkchess.com/forum/viewtopic.php?t=34437) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), May 21, 2010
* [EPR, even better than LMR!](http://www.talkchess.com/forum/viewtopic.php?t=34557) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), May 27, 2010
* [Re: "Automated Discovery of Search Extensions"](http://www.open-chess.org/viewtopic.php?f=5&t=248#p2538) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 26, 2010
* [lmr at PV nodes?](http://www.talkchess.com/forum/viewtopic.php?t=35558) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), July 23, 2010
* [move count based pruning](http://www.talkchess.com/forum/viewtopic.php?t=35955) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), September 02, 2010
* [LMR differences in long vs short games](http://www.talkchess.com/forum/viewtopic.php?t=36633) by [Jacob Børs Lind](index.php?title=Jacob_B%C3%B8rs_Lind&action=edit&redlink=1 "Jacob Børs Lind (page does not exist)"), [CCC](CCC "CCC"), November 08, 2010
* [fulitiy + lmr; funny results](http://www.talkchess.com/forum/viewtopic.php?t=37337) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), December 28, 2010


**2011**



* [lmr in PV](http://www.talkchess.com/forum/viewtopic.php?t=37424) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 03, 2011


**2012**



* [Should reduction depend on depth?](http://www.talkchess.com/forum/viewtopic.php?t=41995) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 14, 2012 » [Komodo](Komodo "Komodo")
* [Possible LMR improvement using AB\_FOOL](http://www.talkchess.com/forum/viewtopic.php?t=43434) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), April 24, 2012
* [LMR Research](http://www.talkchess.com/forum/viewtopic.php?t=44272) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), July 02, 2012
* [Adjustable search pruning depending on time control](http://www.talkchess.com/forum/viewtopic.php?t=46503) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), December 20, 2012 » [Time Management](Time_Management "Time Management")


**2013**



* [ROC analysis of Late Move Reductions](http://www.talkchess.com/forum/viewtopic.php?t=47577) by Gerard van Ewijk, [CCC](CCC "CCC"), March 22, 2013 <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [Is LMR Sound](http://www.talkchess.com/forum/viewtopic.php?t=48144) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), May 29, 2013
* [Is LMR safe within NULL move reduction](http://www.talkchess.com/forum/viewtopic.php?t=48154) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), May 30, 2013
* [LMR at CUT nodes can be arbitrarily bad!](http://www.talkchess.com/forum/viewtopic.php?t=48356) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), June 20, 2013 » [Node Types](Node_Types "Node Types"), [Python](Python "Python")
* [How much to reduce ?](http://www.talkchess.com/forum/viewtopic.php?t=49558) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), October 03, 2013 » [R](Depth_Reduction_R "Depth Reduction R")


**2014**



* [Null move and LMR](http://www.talkchess.com/forum/viewtopic.php?t=51578) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), March 12, 2014 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [LMR & TT interaction](http://www.talkchess.com/forum/viewtopic.php?t=52169) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), April 29, 2014 » [Transposition Table](Transposition_Table "Transposition Table")
* [A question about Stockfish and LMR or other pruning...](http://www.talkchess.com/forum/viewtopic.php?t=54392) by Forrest Hoch, [CCC](CCC "CCC"), November 20, 2014


### 2015 ...


* [About LMR , again :-)](http://www.talkchess.com/forum/viewtopic.php?t=55526) by [Daniel Anulliero](Daniel_Anulliero "Daniel Anulliero"), [CCC](CCC "CCC"), March 01, 2015
* [LMR tuning](http://www.talkchess.com/forum/viewtopic.php?t=56312) by [Shawn Chidester](Shawn_Chidester "Shawn Chidester"), [CCC](CCC "CCC"), May 11, 2015
* [Interpretation of LMR](http://www.talkchess.com/forum/viewtopic.php?t=56524) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), May 29, 2015
* [What's Your Engine's Maximum LMR Reduction?](http://www.talkchess.com/forum/viewtopic.php?t=56631) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), June 08, 2015
* [New "smoothing" issue](http://www.talkchess.com/forum/viewtopic.php?t=57035) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 20, 2015
* [On LMR, and statically predicting moves](http://www.talkchess.com/forum/viewtopic.php?t=57381) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), August 25, 2015
* [LMR by another name](http://www.talkchess.com/forum/viewtopic.php?t=57486) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 02, 2015 » [Spector](Spector "Spector")
* [Ratio reduction](http://www.talkchess.com/forum/viewtopic.php?t=57697) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 20, 2015 » [Symbolic](Symbolic "Symbolic")


**2016**



* [late move reduction](http://www.talkchess.com/forum/viewtopic.php?t=58996) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), January 21, 2016
* [Extensions in the days of LMR?](http://www.talkchess.com/forum/viewtopic.php?t=59598) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 22, 2016 » [Extensions](Extensions "Extensions")
* [LMR problems](http://www.talkchess.com/forum/viewtopic.php?t=60194) by [Alvaro Cardoso](Alvaro_Cardoso "Alvaro Cardoso"), [CCC](CCC "CCC"), May 16, 2016
* [Reductions](http://www.talkchess.com/forum/viewtopic.php?t=60240) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), May 22, 2016 » [R](Depth_Reduction_R "Depth Reduction R")
* [Disappointing LMR Results](http://www.talkchess.com/forum/viewtopic.php?t=61031) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), August 04, 2016
* [Null Move in LMR](http://www.talkchess.com/forum/viewtopic.php?t=61086) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), August 10, 2016 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")


**2017**



* [LMR and PVS](http://www.open-chess.org/viewtopic.php?f=5&t=3084) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2017 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Late move reductions ?](http://www.talkchess.com/forum/viewtopic.php?t=63521) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 22, 2017
* [Check extension vs LMR](http://www.talkchess.com/forum/viewtopic.php?t=63649) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 04, 2017 » [Check Extensions](Check_Extensions "Check Extensions")
* [LMR - or starters - Advance and Expert](http://www.talkchess.com/forum/viewtopic.php?t=63870) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 01, 2017
* [LMR and killer](http://www.talkchess.com/forum/viewtopic.php?t=65169) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 14, 2017 » [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
* [LMR prescription](http://www.talkchess.com/forum/viewtopic.php?t=65273) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), September 24, 2017


**2019**



* [Depth reduced but ELO increased](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=70217) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), March 16, 2019 » [Playing Strength](Playing_Strength "Playing Strength")


### 2020 ...


* [Elo expected from LMR](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78397) by Christian Dean, [CCC](CCC "CCC"), October 11, 2021 » [Playing Strength](Playing_Strength "Playing Strength")
* [Troubles with LMR](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79616) by Kurt Peters, [CCC](CCC "CCC"), March 31, 2022


## External Links


* [Late Move Reductions from Wikipedia](https://en.wikipedia.org/wiki/Late_Move_Reductions)
* [An Introduction to Late Move Reductions](https://web.archive.org/web/20150212051846/http://www.glaurungchess.com/lmr.html) by [Tord Romstad](Tord_Romstad "Tord Romstad") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Mediocre Chess: [Guide] Late move reduction (LMR)](http://mediocrechess.blogspot.de/2007/03/other-late-move-reduction-lmr.html) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson"), March 26, 2007 » [Mediocre](Mediocre "Mediocre")
* [History Reductions in Pro Deo](http://members.home.nl/matador/hr.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder") » [ProDeo](ProDeo "ProDeo")
* [LMR advanced](http://rebel13.nl/rebel13/blog/lmr%20advanced.html) from [Rebel 13](http://rebel13.nl/index.html) by [Ed Schroder](Ed_Schroder "Ed Schroder") <a id="cite-note-6" href="#cite-ref-6">[6]</a> » [Rebel](Rebel "Rebel")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bc8), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [History Reductions in Pro Deo](http://members.home.nl/matador/hr.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [An Introduction to Late Move Reductions](https://web.archive.org/web/20150212051846/http://www.glaurungchess.com/lmr.html) by [Tord Romstad](Tord_Romstad "Tord Romstad") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a>  [Mark Winands](Mark_Winands "Mark Winands"), [Erik van der Werf](Erik_van_der_Werf "Erik van der Werf"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk") (**2004**). *[The Relative History Heuristic](http://link.springer.com/chapter/10.1007/11674399_18)*. [CG 2004](CG_2004 "CG 2004"), [pdf](http://erikvanderwerf.tengen.nl/pubdown/relhis.pdf)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Receiver operating characteristic (ROC) from Wikipedia](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [LMR - or starters - Advance and Expert](http://www.talkchess.com/forum/viewtopic.php?t=63870) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 01, 2017

**[Up one level](Reductions "Reductions")**







 
