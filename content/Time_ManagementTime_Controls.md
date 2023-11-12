---
title: Time ManagementTime Controls
---
**[Home](Home "Home") \* [Search](Search "Search") \* Time Management**



 [](File:Roland_Barcsik_Timeout.jpg) [Roland La Tuffo Barcsik](Arts#LaTuffo "Arts") - Time out <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Time management** refers to algorithms and heuristics to allocate time for searching a move under [time control](https://en.wikipedia.org/wiki/Time_control) requirements in a [game of chess](Chess_Game "Chess Game"). The player [to move](Side_to_move "Side to move") consumes his time, and if he exceeds his time limit, the [game](Chess_Game "Chess Game") is lost on demand of the opponent player, or in automatic computer chess play by an arbiter instance.


[Iterative deepening](Iterative_Deepening "Iterative Deepening") in conjunction with its predictable [effective branching factor](Branching_Factor#EffectiveBranchingFactor "Branching Factor") allows a flexible time management either to terminate the current [iteration](Iteration "Iteration") and to fall back on [best move](Best_Move "Best Move") and [PV](Principal_Variation "Principal Variation") of the previous iteration, or to decide about termination prior to start a new iteration or to search a next root-move. 



### Sudden Death


Sudden death refers to a requirement that all the remaining moves, rather than a fixed number of moves, need to be played within the remaining time. Typically programs estimate the game will last further 25..40 moves, and divide the remaining time by this number.



### Regular Time Controls


Regular time controls define a number of moves to be made in a fixed amount of time. We don't have to make estimations for how long the game will last. However, some time should be saved in order to have a buffer in case later moves warrant longer thinking times.



### Time Control with Increment


To avoid time trouble where often blunders decide the game, chess champions, most notable [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) and [David Bronstein](David_Bronstein "David Bronstein"), proposed a delay or increment of time for each move made. It requires a special delay clock, which became handy with the [development of digital chess clocks](https://en.wikipedia.org/wiki/Game_clock#Early_development_of_digital_game_clocks) in the 70s and 80s <a id="cite-note-2" href="#cite-ref-2">[2]</a> .


Time trouble is also an issue in computer chess, either due to operators in over the board chess, boosted by deviation of internal and external clock, or in transmitting move transfer latencies in automatic play, where it is quite common nowadays to play with increment per move.




### Fischer Time


In 1988 [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) proposed an unconditional increment per move, no matter whether the delay was exhausted or not. With Fischer time one may therefor increase the remaining time if one moves faster than the delay <a id="cite-note-3" href="#cite-ref-3">[3]</a> .



### Bronstein Time


[Bronstein's](David_Bronstein "David Bronstein") time works similar, but never increases the remaining time. It was for instance used during the late [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments").



## Enhancements


Human chess players often wonder about the inflexible time management of various programs. A basic time management scheme might be enhanced in several ways, considering dynamic, statistical as well as static features of the search, the [best move](Best_Move "Best Move") and its [PV](Principal_Variation "Principal Variation").



### Considerations


* How often did the [best move](Best_Move "Best Move") change during the (last N) previous iterations?
* The score function over iterations and best moves, increase or decrease and/or oscillation, score amplitude, etc.
* The ratio of the size of the subtree under the best move versus the size of the whole [search tree](Search_Tree "Search Tree")
* Only one obvious way to recapture in an otherwise quiet position


### Premature Termination


* Only one legal move
* Prior a start of a new iteration, the relation of elapsed and allocated time (f.i. > 50%) <a id="cite-note-4" href="#cite-ref-4">[4]</a>


### Extra Time


* Fail low situations, a severe drop of the score may cause programs to allocate "panic time" to hopefully solve the critical situation
* During the first moves out of the [opening book](Opening_Book "Opening Book") programs often allocate more time


 For instance, [Robert Hyatt](Robert_Hyatt "Robert Hyatt") gave following formula from [Cray Blitz](Cray_Blitz "Cray Blitz") in *Using Time Wisely* <a id="cite-note-5" href="#cite-ref-5">[5]</a> 

```C++

   nMoves =  min( numberOfMovesOutOfBook, 10 );
   factor = 2 -  nMoves / 10 
   target = timeLeft / numberOfMovesUntilNextTimeControl
   time   = factor * target

```

 inspired by following graph of human timing from several grandmaster tournament games
 [](File:GrandmasterThinkingTime.jpg) 
* New and therefor likely not singular best moves, but statically "suspect", like weakening the [pawn structure](Pawn_Structure "Pawn Structure") or a [sacrifice](Sacrifice "Sacrifice") favors to allocate extra time and to start a further iteration, even if the score is fine.


## Losing on Time


* [Tech 2 versus Ribbit](ACM_1974#time "ACM 1974") at [ACM 1974](ACM_1974 "ACM 1974")
* [Duchess vs. T. Belle](ACM_1974#lone "ACM 1974") at [ACM 1974](ACM_1974 "ACM 1974")
* [Chess Tiger X - Pharaon 2.65](Massy_2002#timetrouble "Massy 2002") at [Massy 2002](Massy_2002 "Massy 2002")


## See also


* [CPW-Engine\_chronos](CPW-Engine_chronos "CPW-Engine chronos")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Playing Strength](Playing_Strength "Playing Strength")
* [Pondering](Pondering "Pondering")
* [Search Explosion](Search_Explosion "Search Explosion")
* [Search Statistics](Search_Statistics "Search Statistics")


## Publications


* [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1984**). *Using Time Wisely*. [ICCA Journal, Vol. 7, No. 1](ICGA_Journal#7_1 "ICGA Journal")
* [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [Albert Gower](Albert_Gower "Albert Gower"), [Harry Nelson](Harry_Nelson "Harry Nelson") (**1985**). *Using Time Wisely, revisited (extended abstract).* Proceedings of the 1985 ACM annual conference on The range of computing: mid-80's perspective, p. 271, Denver, Colorado. ISBN 0-89791-170-9.
* [Shaul Markovitch](Shaul_Markovitch "Shaul Markovitch"), [Yaron Sella](index.php?title=Yaron_Sella&action=edit&redlink=1 "Yaron Sella (page does not exist)") (**1993**). *[Learning of Resource Allocation Strategies for Game Playing](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8640.1996.tb00254.x)*. [IJCAI 1993](Conferences#IJCAI1993 "Conferences"), [pdf](https://www.ijcai.org/Proceedings/93-2/Papers/020.pdf)
* [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1994**). *On Timing, Permanent Brain and Human Intervention.* [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1994**). *A la Recherche du Temps Perdu: 'That was easy'* . [ICCA Journal, Vol. 17, No. 1](ICGA_Journal#17_1 "ICGA Journal")
* [Levente Kocsis](Levente_Kocsis "Levente Kocsis"), [Jos Uiterwijk](Jos_Uiterwijk "Jos Uiterwijk"), [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik") (**2000**). *[Learning Time Allocation using Neural Networks](http://link.springer.com/chapter/10.1007/3-540-45579-5_11)*. [CG 2000](CG_2000 "CG 2000"), [postscript](http://zaphod.aml.sztaki.hu/papers/kocsis-CG00.ps)
* [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković"), [Rade Šolak](index.php?title=Rade_%C5%A0olak&action=edit&redlink=1 "Rade Šolak (page does not exist)") (**2009**). *[Time Management Procedure in Computer Chess](http://facta.junis.ni.ac.rs/acar/acar200901/acar2009-07.html)*. [Facta Universitatis, Automatic Control and Robotics, Vol. 8, No. 1](http://facta.junis.ni.ac.rs/acar/acar200901/acar200901toc.html)
* [Rade Šolak](index.php?title=Rade_%C5%A0olak&action=edit&redlink=1 "Rade Šolak (page does not exist)"), [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2009**). *Time Management during a Chess Game*. [ICGA Journal, Vol. 32 No. 4](ICGA_Journal#32_4 "ICGA Journal")
* [Shih-Chieh Huang](Shih-Chieh_Huang "Shih-Chieh Huang"), [Rémi Coulom](R%C3%A9mi_Coulom "Rémi Coulom"), [Shun-Shii Lin](Shun-Shii_Lin "Shun-Shii Lin") (**2011**). *Time Management for Monte-Carlo Tree Search Applied to the Game of Go*. TAAI 2010, [pdf](http://remi.coulom.free.fr/Publications/TimeManagement.pdf)
* [Hendrik Baier](Hendrik_Baier "Hendrik Baier"), [Mark Winands](Mark_Winands "Mark Winands") (**2011**). *[Time Management for Monte-Carlo Tree Search in Go](http://link.springer.com/chapter/10.1007/978-3-642-31866-5_4)*. [Advances in Computer Games 13](Advances_in_Computer_Games_13 "Advances in Computer Games 13")
* [Hendrik Baier](Hendrik_Baier "Hendrik Baier"), [Mark Winands](Mark_Winands "Mark Winands") (**2016**). *Time Management for Monte Carlo Tree Search*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 8, No. 3, [draft as pdf](https://dke.maastrichtuniversity.nl/m.winands/documents/time_management_for_monte_carlo_tree_search.pdf)


## Forum Posts


### 1993 ...


* [Open Letter To Chess Computer Programmers](http://groups.google.com/group/rec.games.chess/browse_frm/thread/c7bf58b3c59273e2/f388d174febe18d2) by Kevin Gowen, [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), December 26, 1993
* [Computer chess strategy](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/5ecf6f473db3eeb6) by Al, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 22, 1997
* [Time usage](https://www.stmintz.com/ccc/index.php?id=12827) by John Bartkiw, [CCC](CCC "CCC"), December 08, 1997
* [How to program search timeout ?](https://www.stmintz.com/ccc/index.php?id=14872) by [Rudolf Posch](Rudolf_Posch "Rudolf Posch"), [CCC](CCC "CCC"), February 04, 1998
* [How much time per move?](https://www.stmintz.com/ccc/index.php?id=15406) by [Andrew Williams](Andrew_Williams "Andrew Williams"), [CCC](CCC "CCC"), March 02, 1998
* [Time control legend](https://www.stmintz.com/ccc/index.php?id=18553) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), May 13, 1998


### 2000 ...


* [Question: Fail low at root and time management](https://www.stmintz.com/ccc/index.php?id=95710) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), February 08, 2000 » [Fail-Low](Fail-Low "Fail-Low"), [Root](Root "Root")
* [new idea on managing time using depth reduction at root](https://www.stmintz.com/ccc/index.php?id=282702) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), February 08, 2003
* [finding when a move is obvious](https://www.stmintz.com/ccc/index.php?id=359869) by [Eric Oldre](Eric_Oldre "Eric Oldre"), [CCC](CCC "CCC"), April 13, 2004
* [question about fixing the time management of movei](https://www.stmintz.com/ccc/index.php?id=378905) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 25, 2004


### 2005 ...


* [Where to put timeout() code in search?](http://www.talkchess.com/forum/viewtopic.php?p=131908) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), July 18, 2007
* [obvious/easy move](http://www.talkchess.com/forum/viewtopic.php?t=20125) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), March 12, 2008
* [Crafty (and others?) time management question](http://www.talkchess.com/forum/viewtopic.php?t=27446) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), April 14, 2009
* [Time managment on ponder hit](http://www.talkchess.com/forum/viewtopic.php?t=28438) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), June 16, 2009 » [Pondering](Pondering "Pondering")
* [Info from timeout search](http://www.talkchess.com/forum/viewtopic.php?t=30326) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), October 26, 2009


### 2010 ...


* [As though they were pondering](http://www.talkchess.com/forum/viewtopic.php?t=35554) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), July 23, 2010 » [Pondering](Pondering "Pondering")
* [Move on Hash Hit](http://www.open-chess.org/viewtopic.php?f=5&t=588) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 18, 2010 » [Pondering](Pondering "Pondering")
* [New Time Controls for WB](http://www.talkchess.com/forum/viewtopic.php?t=35931) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), August 30, 2010 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [WinBoard](WinBoard "WinBoard"), [ChessGUI](ChessGUI "ChessGUI")
* [Repeating moves to add time](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=38608) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 31, 2011


**2012**



* [Sudden death time controls](http://www.talkchess.com/forum/viewtopic.php?t=43636) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), May 10, 2012
* [Winboard protocol and fractional increments](http://www.talkchess.com/forum/viewtopic.php?t=45325) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), September 25, 2012 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [WinBoard](WinBoard "WinBoard")
* [Adjustable search pruning depending on time control](http://www.talkchess.com/forum/viewtopic.php?t=46503) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), December 20, 2012 » [Pruning](Pruning "Pruning"), [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")


**2013**



* ["panic time" and "easy moves"](http://www.talkchess.com/forum/viewtopic.php?t=47242) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 16, 2013
* [Yet another time allocation heuristic](http://www.talkchess.com/forum/viewtopic.php?t=47251) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 17, 2013
* [easy-hard moves (again)](http://www.talkchess.com/forum/viewtopic.php?t=47442) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), March 08, 2013
* [Easy easy move](http://www.talkchess.com/forum/viewtopic.php?t=48824) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), August 02, 2013
* [out-of-time: what to do?](http://www.talkchess.com/forum/viewtopic.php?t=48903) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), August 09, 2013
* [Losing on time](http://www.talkchess.com/forum/viewtopic.php?t=50705) by [Gregory Strong](Gregory_Strong "Gregory Strong"), [CCC](CCC "CCC"), December 31, 2013


**2014**



* [Time control comparison between engines](http://www.talkchess.com/forum/viewtopic.php?t=50718) by [Ed Schroder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 01, 2014
* [fixed time control management](http://www.talkchess.com/forum/viewtopic.php?t=51135) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 01, 2014
* [Question about Time Management](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=53060) by ambrooks1, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 06, 2014
* [Move time and compiler optimization](http://www.talkchess.com/forum/viewtopic.php?t=51720) by [Edmund Moshammer](Edmund_Moshammer "Edmund Moshammer"), [CCC](CCC "CCC"), March 23, 2014
* [Playing strength development - increasing time control](http://www.talkchess.com/forum/viewtopic.php?t=52021) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), April 17, 2014
* [Time based contempt](http://www.talkchess.com/forum/viewtopic.php?t=52069) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), April 20, 2014 » [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Time Management](http://www.talkchess.com/forum/viewtopic.php?t=52464) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), May 29, 2014


### 2015 ...


* [Elo gain and optimal time management](http://www.talkchess.com/forum/viewtopic.php?t=54939) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 11, 2015
* [What's the fastest time control you can effectively test at?](http://www.talkchess.com/forum/viewtopic.php?t=56534) by Jordan Bray, [CCC](CCC "CCC"), May 30, 2015


**2016**



* [Time management trick](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=60869) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 19, 2016
* [Photographing Chess Clock](http://www.talkchess.com/forum/viewtopic.php?t=61672) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 10, 2016
* [Doubling of time control](http://www.talkchess.com/forum/viewtopic.php?t=61784) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 21, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Komodo](Komodo "Komodo")
* [New idea for "easy move detection"](http://www.talkchess.com/forum/viewtopic.php?t=61976) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), November 05, 2016 » [CT800](CT800 "CT800")
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Stockfish](Stockfish "Stockfish")
* [On time management](http://www.talkchess.com/forum/viewtopic.php?t=62586) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), December 24, 2016


**2017**



* [Time managment ?](http://www.talkchess.com/forum/viewtopic.php?t=63362) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), March 07, 2017
* [Time management ideas](http://www.open-chess.org/viewtopic.php?f=5&t=3098) by lucasart, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 03, 2017
* [Invariance with time control of rating schemes](http://www.talkchess.com/forum/viewtopic.php?t=64683) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 22, 2017 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Time Managment translating to SMP](http://www.talkchess.com/forum/viewtopic.php?t=66099) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 23, 2017 » [Parallel Search](Parallel_Search "Parallel Search")


**2018 ...**



* [Time control envelope in top engines could be improved?](http://www.talkchess.com/forum/viewtopic.php?t=66821) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 13, 2018 » [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength")
* [easy move?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68692) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 19, 2018


 [Re: easy move?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68692&start=8) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 19, 2018
* [UCI pondering and time management](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72686) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 30, 2019 » [UCI](UCI "UCI"), [Pondering](Pondering "Pondering")


### 2020 ...


* [CECP "time" and "otim"](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75944) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), November 30, 2020 » [CECP](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")


## External Links


* [Time Allocation](http://web.archive.org/web/20070607151549/www.brucemo.com/compchess/programming/time.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070607231311/www.brucemo.com/compchess/programming/index.htm)
* [Time control from Wikipedia](https://en.wikipedia.org/wiki/Time_control)
* [Time management from Wikipedia](https://en.wikipedia.org/wiki/Time_management)
* [Timing with a Neural Networks](http://web.archive.org/web/20050328050743/http://www.playwitharena.com:80/) by [Volker Annuss](Volker_Annuss "Volker Annuss"), [Arena](Arena "Arena") News-Ticker, Page 6, 86, FQ, March 23, 2005 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Time Management During a Chess Game](http://web.archive.org/web/20100615030345/http://www.chesscafe.com/text/time.txt) by [Dan Heisman](Dan_Heisman "Dan Heisman") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Time of check to time of use from Wikipedia](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use)
* [Buddy Rich](https://en.wikipedia.org/wiki/Buddy_Rich) - [Time Check](https://en.wikipedia.org/wiki/Don_Menza#Educator_and_composer), at The Top of the [Plaza](https://en.wikipedia.org/wiki/Midtown_Plaza_%28Rochester%29) in [Rochester, NY](https://en.wikipedia.org/wiki/Rochester,_New_York), February 6, 1973, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
* [Hiromi’s Sonicbloom](https://en.wikipedia.org/wiki/Hiromi_Uehara#Hiromi.27s_Sonicbloom) - [Time Difference](https://en.wikipedia.org/wiki/Time_Control), 2007, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Hiromi Uehara](Category:Hiromi_Uehara "Category:Hiromi Uehara"), [Martin Valihora](https://en.wikipedia.org/wiki/Martin_Valihora), [Tony Grey](https://en.wikipedia.org/wiki/Tony_Grey), [David Fiuczynski](Category:David_Fiuczynski "Category:David Fiuczynski")
 
* [Hiromi Uehara](Category:Hiromi_Uehara "Category:Hiromi Uehara"), [David Fiuczynski](Category:David_Fiuczynski "Category:David Fiuczynski"), [Tony Grey](https://en.wikipedia.org/wiki/Tony_Grey), [Jordan Perlson](http://www.linkedin.com/pub/jordan-perlson/18/562/b1b) - [Time Out](https://en.wikipedia.org/wiki/Time_Control), [XI Festival de Jazz de San Javier](http://es.wikipedia.org/wiki/Festival_Internacional_de_Jazz_de_San_Javier), 2008, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Streatham & Brixton Chess Blog: Chess in Art Postscript: Chess-in-Artists do for Christmas](http://streathambrixtonchess.blogspot.de/2009/11/chess-in-art-postscript-chess-in_22.html) The site *Roland La Tuffo Barczik Hungarian artist, La Tuffo's Artwork, Barcsik's Chess Art* no longer available
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [History of the clocks](http://digitalgametechnology.com/site/index.php/History/clock-history.html) from [DGT - Digital Game Technology](http://digitalgametechnology.com/site/)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Digital chess clock - Google Patent Search](http://www.google.com/patents?vid=4884255)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [question about fixing the time management of movei](https://www.stmintz.com/ccc/index.php?id=378905) by [Uri Blass](Uri_Blass "Uri Blass") from [CCC](CCC "CCC"), July 25, 2004
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1984**). *Using Time Wisely*. [ICCA Journal, Vol. 7, No. 1](ICGA_Journal#7_1 "ICGA Journal")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Normalized Elo](http://hardy.uhasselt.be/Toga/normalized_elo.pdf) (pdf) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh")

**[Up one Level](Search "Search")**







 
