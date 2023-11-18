---
title: Perft Results
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Move Generation](Move_Generation "Move Generation") \* [Perft](Perft "Perft") \* Results**


This page contains detailed [perft](Perft "Perft") results for several positions that are useful for [debugging](Debugging "Debugging"), beginning with the start position. [Captures](Captures "Captures"), [checkmates](Checkmate "Checkmate"), and other information have been included along with the node counts ([leaf nodes](Leaf_Node "Leaf Node"), excluding internal or [interior nodes](Interior_Node "Interior Node")) or movepath enumerations. The move counters consider moves to the leaf positions only.



### Perft 10


* [Perft(10) 20 draft 9 Positions](Perft(10)_20_draft_9_Positions "Perft(10) 20 draft 9 Positions")
* [Perft(10) 400 draft 8 Positions](Perft(10)_400_draft_8_Positions "Perft(10) 400 draft 8 Positions")


### Perft 11


* [Perft(11) 20 draft 10 Positions](Perft(11)_20_draft_10_Positions "Perft(11) 20 draft 10 Positions")
* [Perft(11) 400 draft 9 Positions](Perft(11)_400_draft_9_Positions "Perft(11) 400 draft 9 Positions")


### Perft 12


* [Perft(12) 20 draft 11 Positions](Perft(12)_20_draft_11_Positions "Perft(12) 20 draft 11 Positions")
* [Perft(12) 400 draft 10 Positions](Perft(12)_400_draft_10_Positions "Perft(12) 400 draft 10 Positions")


### Perft 13


* [Perft(13) 20 draft 12 Positions](Perft(13)_20_draft_12_Positions "Perft(13) 20 draft 12 Positions")
* [Perft(13) 400 draft 11 Positions](Perft(13)_400_draft_11_Positions "Perft(13) 400 draft 11 Positions")


### Summary


* [Initial Position Summary](Initial_Position_Summary "Initial Position Summary")
* [Perft(15)](Perft#15 "Perft")






## Position 2


also known as **Kiwipete** by [Peter McKenzie](Peter_McKenzie "Peter McKenzie") <a id="cite-note-7" href="#cite-ref-7">[7]</a>. The number of double-checks in depth 5 is discussed in [Talkchess](CCC "CCC") <a id="cite-note-8" href="#cite-ref-8">[8]</a> and may be 2645 instead of 2637.





|  |
| --- |
|                                                                 ♜   ♚  ♜♟ ♟♟♛♟♝ ♝♞  ♟♞♟    ♙♘    ♟  ♙     ♘  ♕ ♟♙♙♙♗♗♙♙♙♖   ♔  ♖ |



```C++
r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 

```



|  Depth
 |  Nodes
 |  Captures
 |  E.p.
 |  Castles
 |  Promotions
 |  Checks
 |  Discovery Checks
 |  Double Checks
 |  Checkmates
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  1
 |  48
 |  8
 |  0
 |  2
 |  0
 |  0
 |  0
 |  0
 |  0
 |
|  2
 |  2039
 |  351
 |  1
 |  91
 |  0
 |  3
 |  0
 |  0
 |  0
 |
|  3
 |  97862
 |  17102
 |  45
 |  3162
 |  0
 |  993
 |  0
 |  0
 |  1
 |
|  4
 |  4085603
 |  757163
 |  1929
 |  128013
 |  15172
 |  25523
 |  42
 |  6
 |  43
 |
|  5
 |  193690690
 |  35043416
 |  73365
 |  4993637
 |  8392
 |  3309887
 |  19883
 |  2637
 |  30171
 |
|  6
 |  8031647685
 |  1558445089
 |  3577504
 |  184513607
 |  56627920
 |  92238050
 |  568417
 |  54948
 |  360003
 |






## Position 3




|  |
| --- |
|                                                                                                 ♟        ♟    ♔♙     ♜ ♖   ♟ ♚            ♙ ♙          |



```C++
8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 

```



|  Depth
 |  Nodes
 |  Captures
 |  E.p.
 |  Castles
 |  Promotions
 |  Checks
 |  Discovery Checks
 |  Double Checks
 |  Checkmates
 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  1
 |  14
 |  1
 |  0
 |  0
 |  0
 |  2
 |  0
 |  0
 |  0
 |
|  2
 |  191
 |  14
 |  0
 |  0
 |  0
 |  10
 |  0
 |  0
 |  0
 |
|  3
 |  2812
 |  209
 |  2
 |  0
 |  0
 |  267
 |  3
 |  0
 |  0
 |
|  4
 |  43238
 |  3348
 |  123
 |  0
 |  0
 |  1680
 |  106
 |  0
 |  17
 |
|  5
 | <a id="cite-note-9" href="#cite-ref-9">[9]</a> 674624
 |  52051
 |  1165
 |  0
 |  0
 |  52950
 |  1292
 |  3
 |  0
 |
|  6
 |  11030083
 |  940350
 |  33325
 |  0
 |  7552
 |  452473
 |  26067
 |  0
 |  2733
 |
|  7
 |  178633661
 |  14519036
 |  294874
 |  0
 |  140024
 |  12797406
 |  370630
 |  3612
 |  87
 |
|  8
 |  3009794393
 |  267586558
 |  8009239
 |  0
 |  6578076
 |  135626805
 |  7181487
 |  1630
 |  450410
 |






## Position 4




|  |
| --- |
|                                                                  ♜   ♚  ♜♙♟♟♟ ♟♟♟ ♝   ♞♝♘♞♙      ♗♗♙ ♙   ♛    ♘  ♙♟ ♙  ♙♙♖  ♕ ♖♔  |



```C++
r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1

```

Or mirrored (with the same perft results):




```C++
r2q1rk1/pP1p2pp/Q4n2/bbp1p3/Np6/1B3NBn/pPPP1PPP/R3K2R b KQ - 0 1 

```



|  Depth
 |  Nodes
 |  Captures
 |  E.p.
 |  Castles
 |  Promotions
 |  Checks
 |  Checkmates
 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  1
 |  6
 |  0
 |  0
 |  0
 |  0
 |  0
 |  0
 |
|  2
 |  264
 |  87
 |  0
 |  6
 |  48
 |  10
 |  0
 |
|  3
 |  9467
 |  1021
 |  4
 |  0
 |  120
 |  38
 |  22
 |
|  4
 |  422333
 |  131393
 |  0
 |  7795
 |  60032
 |  15492
 |  5
 |
|  5
 |  15833292
 |  2046173
 |  6512
 |  0
 |  329464
 |  200568
 |  50562
 |
|  6
 |  706045033
 |  210369132
 |  212
 |  10882006
 |  81102984
 |  26973664
 |  81076
 |






## Position 5


This position was discussed on [Talkchess](CCC "CCC") <a id="cite-note-10" href="#cite-ref-10">[10]</a> and caught bugs in engines several years old at depth 3 <a id="cite-note-11" href="#cite-ref-11">[11]</a> and was also reported wrong here <a id="cite-note-12" href="#cite-ref-12">[12]</a>, hopefully now corrected with the results given by [Steven Edwards](Steven_Edwards "Steven Edwards"), July 18, 2015 <a id="cite-note-13" href="#cite-ref-13">[13]</a>





|  |
| --- |
|                                                                     ♜♞♝♛ ♚ ♜♟♟ ♙♝♟♟♟  ♟               ♗             ♙♙♙ ♘♞♙♙♖♘♗♕♔  ♖ |



```C++
rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8  

```



|  Depth
 |  Nodes
 |
| --- | --- |
|  1
 |  44
 |
|  2
 |  1,486
 |
|  3
 |  62,379
 |
|  4
 |  2,103,487
 |
|  5
 |  89,941,194
 |






## Position 6


An alternative Perft given by [Steven Edwards](Steven_Edwards "Steven Edwards") <a id="cite-note-14" href="#cite-ref-14">[14]</a> <a id="cite-note-15" href="#cite-ref-15">[15]</a>

```C++
r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10 

```



|  Depth
 |  Nodes
 |
| --- | --- |
|  0
 |  1
 |
|  1
 |  46
 |
|  2
 |  2,079
 |
|  3
 |  89,890
 |
|  4
 |  3,894,594
 |
|  5
 |  164,075,551
 |
|  6
 |  6,923,051,137
 |
|  7
 |  287,188,994,746
 |
|  8
 |  11,923,589,843,526
 |
|  9
 |  490,154,852,788,714
 |


## See also


* [Chess960 Perft Results](Chess960_Perft_Results "Chess960 Perft Results")
* [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")


## Forum Posts


### 2000 ...


* [kiwipete perft position](https://www.stmintz.com/ccc/index.php?id=274926) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), January 04, 2003 » [Peter McKenzie](Peter_McKenzie "Peter McKenzie"), [Kiwipete](Perft_Results#kiwipete "Perft Results")
* [perft results (how accurate is accurate enough ?)](https://www.stmintz.com/ccc/index.php?id=388806) by [Roman Hartmann](Roman_Hartmann "Roman Hartmann"), [CCC](CCC "CCC"), September 23, 2004


### 2010 ...


* [REPORT: wrong perft result by qperft](http://www.talkchess.com/forum/viewtopic.php?t=42463) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), February 14, 2012 » [Position 5](Perft_Results#Position5 "Perft Results")
* [Perft and en\_passant](http://www.talkchess.com/forum/viewtopic.php?t=45099) by [Harald Lüßen](Harald_L%C3%BC%C3%9Fen "Harald Lüßen"), [CCC](CCC "CCC"), September 11, 2012 » [En passant](En_passant "En passant")
* [Perft(14) estimates thread](http://www.talkchess.com/forum/viewtopic.php?t=47335) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 26, 2013
* [Perft(15) estimates thread](http://www.talkchess.com/forum/viewtopic.php?t=47740) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 10, 2013
* [An altenative perft() initial FEN](http://www.talkchess.com/forum/viewtopic.php?t=48616) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 11, 2013
* [Impossible perft question](http://www.talkchess.com/forum/viewtopic.php?t=48811) by [Andy Duplain](index.php?title=Andy_Duplain&action=edit&redlink=1 "Andy Duplain (page does not exist)"), [CCC](CCC "CCC"), August 01, 2013 » [Position 3](Perft_Results#Position3 "Perft Results")
* [Wide open perft()](http://www.talkchess.com/forum/viewtopic.php?t=49000) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 18, 2013
* [Perft(14) revisited](http://www.talkchess.com/forum/viewtopic.php?t=53224) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 08, 2014
* [Perft(14) Weekly Status Report](http://www.talkchess.com/forum/viewtopic.php?t=53406) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2014
* [Perft(14) verification](http://www.talkchess.com/forum/viewtopic.php?t=54767) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 28, 2014


### 2015 ...


* [Perft(14) Weekly Status Reports for 2015](http://www.talkchess.com/forum/viewtopic.php?t=54853) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), January 04, 2015
* [Perft for various positions](http://www.talkchess.com/forum/viewtopic.php?t=54995) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), January 17, 2015
* [Some Chess960/FRC positions to be confirmed](http://www.talkchess.com/forum/viewtopic.php?t=55274) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), February 09, 2015 » [Chess960](Chess960 "Chess960")
* [kiwipete perft position](http://www.talkchess.com/forum/viewtopic.php?t=55787) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), March 26, 2015 » [Kiwipete](Perft_Results#kiwipete "Perft Results")
* [Perft(14) Weekly Status Reports for 2016](http://www.talkchess.com/forum/viewtopic.php?t=58726) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), December 29, 2015


**2016**



* [A perft(7) challenge position](http://www.talkchess.com/forum/viewtopic.php?t=59781) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 07, 2016
* [Another perft(7) challenge position](http://www.talkchess.com/forum/viewtopic.php?t=59818) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 13, 2016
* [Perft(7) challenge position #3](http://www.talkchess.com/forum/viewtopic.php?t=59915) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 20, 2016
* [Perft(7) challenge position #4](http://www.talkchess.com/forum/viewtopic.php?t=59957) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 25, 2016
* [Perft(7) challenge position #5](http://www.talkchess.com/forum/viewtopic.php?t=59961) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), April 25, 2016
* [Another perft(7) challenge](http://www.talkchess.com/forum/viewtopic.php?t=60102) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 08, 2016
* [Perft(7) challenge position #6](http://www.talkchess.com/forum/viewtopic.php?t=60114) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 10, 2016
* [Perft(7) 64 bit hash mismatch set 8](http://www.talkchess.com/forum/viewtopic.php?t=60242) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), May 22, 2016
* [Twenty-nine perft(7) mismatches from work unit 528](http://www.talkchess.com/forum/viewtopic.php?t=60942) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 25, 2016
* [yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 13, 2016


 [Re: yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119&start=30) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 09, 2016 
* [Two perft(7) mismatches from work unit 571](http://www.talkchess.com/forum/viewtopic.php?t=61329) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 04, 2016


**2017 ...**



* [perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017 » [Perft(15)](Perft#15 "Perft")


 [Re: perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=4) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017 
* [Contrived position for perft](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70543) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), April 21, 2019
* [You gotta love Perft... just not too much!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71379) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), July 27, 2019
* [Level 11 Perft statistics](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71841&p=812577) by [Andreas Øverland](index.php?title=Andreas_%C3%98verland&action=edit&redlink=1 "Andreas Øverland (page does not exist)"), [CCC](CCC "CCC"), September 17, 2019


### 2020 ...


* [Place to find correct perft result from a fen position](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75877) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), November 20, 2020
* [Chinese chess Xiangqi perft results](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76430) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 27, 2021 » [Chinese Chess Perft Results](Chinese_Chess_Perft_Results "Chinese Chess Perft Results")
* [Perft 7 -> 1.6 trillion moves](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77069) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), April 12, 2021
* [Being silly with perft and legal move generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77350) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 » [Legal Move Generation](Move_Generation#Legal "Move Generation"), [En passant](En_passant "En passant")


## External Links


* [A048987](https://oeis.org/A048987) from [On-Line Encyclopedia of Integer Sequences (OEIS)](https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences)
* [µ-Max Dowload Page - qperft](https://home.hccnet.nl/h.g.muller/dwnldpage.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
* [perft-random.epd](https://marcelk.net/rookie/nostalgia/v3/perft-random.epd) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck")
* [Crafty Command Documentation](https://craftychess.com/documentation/craftydoc.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), see [Crafty](Crafty "Crafty") perft
* [Sharper - Perft calculation](https://web.archive.org/web/20060430011809/http://www.albert.nu/programs/sharper/perft.htm) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Distributed Perft Project](https://web.archive.org/web/20130517080941/http://www.albert.nu/programs/dperft/default.asp) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [perft, divide, debugging a move generator](http://www.rocechess.ch/perft.html) from [ROCE](ROCE "ROCE") by [Roman Hartmann](Roman_Hartmann "Roman Hartmann")
* [Perft - sample test positions](https://sites.google.com/site/numptychess/perft) used by [Numpty chess](Numpty_chess "Numpty chess")
* [Perft](https://www.stmintz.com/ccc/index.php?terms=perft&search=1), search the [CCC Archives](Computer_Chess_Forums "Computer Chess Forums")
* [Statistics on chess games](https://wismuth.com/chess/statistics-games.html) by [François Labelle](Mathematician#FLabelle "Mathematician")
* [vajolet/perft.txt at master · elcabesa/vajolet · GitHub](https://github.com/elcabesa/vajolet/blob/master/tests/perft.txt) by [Marco Belli](Marco_Belli "Marco Belli")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Perft FEN data](http://www.talkchess.com/forum/viewtopic.php?t=46055) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), November 18, 2012
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119&start=30) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 09, 2016
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=4) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Perft(12) count confirmed](http://www.talkchess.com/forum/viewtopic.php?t=38862) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2011
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: yet another attempt on Perft(14)](http://www.talkchess.com/forum/viewtopic.php?t=61119&start=30) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), September 09, 2016
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: perft(15)](http://www.talkchess.com/forum/viewtopic.php?t=64983&start=4) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), August 25, 2017
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [kiwipete perft position](https://www.stmintz.com/ccc/index.php?id=274926) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), January 04, 2003
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Perft statistics - chessprogrammingwiki](http://talkchess.com/forum3/viewtopic.php?f=7&t=78402) by [Murat Yirci](index.php?title=Murat_Yirci&action=edit&redlink=1 "Murat Yirci (page does not exist)"), [CCC](CCC "CCC"), October 10, 2021
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Impossible perft question](http://www.talkchess.com/forum/viewtopic.php?t=48811) by [Andy Duplain](index.php?title=Andy_Duplain&action=edit&redlink=1 "Andy Duplain (page does not exist)"), [CCC](CCC "CCC"), August 01, 2013
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [REPORT: wrong perft result by qperft](http://www.talkchess.com/forum/viewtopic.php?t=42463) by [Jesús Muñoz](index.php?title=Jes%C3%BAs_Mu%C3%B1oz&action=edit&redlink=1 "Jesús Muñoz (page does not exist)"), [CCC](CCC "CCC"), February 14, 2012
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Re: REPORT: wrong perft result by qperft](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=450535&t=42463) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), February 14, 2012
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [Re: Correction of my error](http://www.talkchess.com/forum/viewtopic.php?t=42463&start=18) by [Eugene Kotlov](index.php?title=Eugene_Kotlov&action=edit&redlink=1 "Eugene Kotlov (page does not exist)"), [CCC](CCC "CCC"), July 17, 2015
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Re: Correction of my error](http://www.talkchess.com/forum/viewtopic.php?t=42463&start=21) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 18, 2015
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [An altenative perft() initial FEN](http://www.talkchess.com/forum/viewtopic.php?t=48616) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), July 11, 2013
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Some perft() results for that alternative test position](http://www.talkchess.com/forum/viewtopic.php?t=49118) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 26, 2013

**[Up one level](Perft "Perft")**







 
 



### Navigation menu




### Personal tools


* [Log in](index.php?title=Special:UserLogin&returnto=Perft+Results "You are encouraged to log in; however, it is not mandatory [o]")





### Namespaces


* [Page](Perft_Results "View the content page [c]")
* [Discussion](index.php?title=Talk:Perft_Results&action=edit&redlink=1 "Discussion about the content page [t]")




### 
Variants










### Views


* [Read](Perft_Results)
* [View source](index.php?title=Perft_Results&action=edit "This page is protected.
You can view its source [e]")
* [View history](index.php?title=Perft_Results&action=history "Past revisions of this page [h]")




### More








### 
Search




 







### Navigation



* [Home](Home "Visit the Home [z]")
* [Recent changes](Special:RecentChanges "A list of recent changes in the wiki [r]")
* [Random page](Special:Random "Load a random page [x]")
* [Help](https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents "The place to find out")





### Tools



* [What links here](Special:WhatLinksHere/Perft_Results "A list of all wiki pages that link here [j]")
* [Related changes](Special:RecentChangesLinked/Perft_Results "Recent changes in pages linked from this page [k]")
* [Special pages](Special:SpecialPages "A list of all special pages [q]")
* [Printable version](index.php?title=Perft_Results&printable=yes "Printable version of this page [p]")
* [Permanent link](index.php?title=Perft_Results&oldid=26511 "Permanent link to this revision of the page")
* [Page information](index.php?title=Perft_Results&action=info "More information about this page")







* This page was last edited on 29 August 2022, at 05:10.
* Content is available under [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](Chessprogramming:About "Chessprogramming:About") unless otherwise noted.


* [Privacy policy](Chessprogramming:Privacy_policy "Chessprogramming:Privacy policy")
* [About Chessprogramming wiki](Chessprogramming:About "Chessprogramming:About")
* [Disclaimers](Chessprogramming:General_disclaimer "Chessprogramming:General disclaimer")
* [Mobile view](https://www.chessprogramming.org/index.php?title=Perft_Results&mobileaction=toggle_view_mobile)


 * [](https://creativecommons.org/licenses/by-sa/3.0/) 
* [](/www.mediawiki.org/)






