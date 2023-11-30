---
title: RookieEvaluation
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Rookie**



 [](http://marcelk.net/rookie/nostalgia/v1/rookie1.png) Rookie 1.0 Screen <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Rookie**,  

a family of chess programs developed by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"). Rookie started its life in the early 90s, evolved from a mate-in-two problem solver, and was entirely written in [68000](68000 "68000") [assembly](Assembly "Assembly") <a id="cite-note-2" href="#cite-ref-2">[2]</a> to run on an [Amiga](Amiga "Amiga"), since Rookie 1.0 with an own [Graphical User Interface](GUI "GUI") written in [C](C "C") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Rookie **2.x** was pure C and active during the late 90s, while Rookie **3.x**, a complete rewrite from scratch <a id="cite-note-4" href="#cite-ref-4">[4]</a> , appeared in 2010 after Marcel took a long break from computer chess programming. 



### Search


Chapter 2 covers the [search](Search "Search") topics [PVS](Principal_Variation_Search "Principal Variation Search"), [iterative deepening](Iterative_Deepening "Iterative Deepening"), [quiescence search](Quiescence_Search "Quiescence Search"), [move ordering](Move_Ordering "Move Ordering"), [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"), [killer-](Killer_Heuristic "Killer Heuristic") and [counter moves](Countermove_Heuristic "Countermove Heuristic"), [history heuristic](History_Heuristic "History Heuristic"), [fractional extensions](Extensions#FractionalExtensions "Extensions"), [pruning](Pruning "Pruning"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [transposition table](Transposition_Table "Transposition Table"), and a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) like [hash table](Hash_Table "Hash Table") to detect [repetitions](Repetitions#RepetitionHashTable "Repetitions"), and much more interesting stuff.




### Evaluation


Chapter 3 of the thesis elaborates on [evaluation](Evaluation "Evaluation"), chapter 4 on the [opening book](Opening_Book "Opening Book") including [book learning](Book_Learning "Book Learning"). The instructive overview of Rookie's 2.0 evaluator demonstrates its components including various [hash-](Hash_Table "Hash Table"), [material-](Material_Tables "Material Tables") and dynamic [piece-square tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>:



### Triple Stage Evaluator


* Stage 1: [material](Material "Material") and [pawn](Pawn_Structure "Pawn Structure")-[king](King_Safety#PawnShield "King Safety") structure
* Stage 2: dynamic [piece-square tables](Piece-Square_Tables "Piece-Square Tables")
* Stage 3: [mobility](Mobility "Mobility") and [board control](Square_Control "Square Control")


 [](http://marcelk.net/thesis/talk-eval-rookie/sld013.htm) 
Rookie 2.0: Triple Stage Evaluator with conditional [lazy eval](Lazy_Evaluation "Lazy Evaluation") short cuts <a id="cite-note-8" href="#cite-ref-8">[8]</a>



### The Big Picture


 [](http://marcelk.net/thesis/talk-eval-rookie/sld017.htm) 
Overview of Rookie 2.0 Evaluator <a id="cite-note-9" href="#cite-ref-9">[9]</a>



## Rookie 3


After years "out of business", Marcel started Rookie **3.0**, a 100% rewrite from scratch, but still using [incremental](Incremental_Updates "Incremental Updates") [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") and dynamic [piece-square tables](Piece-Square_Tables "Piece-Square Tables") of Rookie 1, so he decided to stick with the name <a id="cite-note-10" href="#cite-ref-10">[10]</a> .



## Tournaments


Rookie **0.82** had its debut at the [DOCCC 1993](DOCCC_1993 "DOCCC 1993"), Rooie **2.0** further played the [DOCCC 1997](DOCCC_1997 "DOCCC 1997") and [DOCCC 1998](DOCCC_1998 "DOCCC 1998"), and Rookie **3.x** the [DOCCC 2010](DOCCC_2010 "DOCCC 2010"), [CPT 2011](CPT_2011 "CPT 2011"), [ICT 2011](ICT_2011 "ICT 2011"), [CCT13](CCT13 "CCT13"), the [Fifth Annual World Computer Rapid Chess Championships](WCRCC_2011 "WCRCC 2011") 2011, and the [19th World Computer Chess Championship](WCCC_2011 "WCCC 2011") in [Tilburg](Tilburg_University "Tilburg University") 2011. In June 2013, Rookie with [upcoming repetition detection](Repetitions "Repetitions") <a id="cite-note-11" href="#cite-ref-11">[11]</a> implemented, won the [ICT 2013](ICT_2013 "ICT 2013") <a id="cite-note-12" href="#cite-ref-12">[12]</a>.



### Photos


### Rookie of the Year Award


 [](http://www.csvn.nl/index.php?option=com_content&view=article&id=487%3A30th-odccc-final-results&catid=51%3Atoernooien&Itemid=28&lang=en) 
[DOCCC 2010](DOCCC_2010 "DOCCC 2010"): [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") receives the "Rookie of the Year Award" from [Cock de Gorter](Cock_de_Gorter "Cock de Gorter") <a id="cite-note-13" href="#cite-ref-13">[13]</a>



### ICT 2011


 [](http://www.csvn.nl/index.php?option=com_content&view=article&id=508%3Aict11-round-7&catid=51%3Atoernooien&Itemid=28&lang=en) 
[ICT 2011](ICT_2011 "ICT 2011"): [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") and [Gyula Horváth](Gyula_Horv%C3%A1th "Gyula Horváth"), Rookie - [Pandix](Pandix "Pandix") <a id="cite-note-14" href="#cite-ref-14">[14]</a>



### Selected Games


### DOCCC 1997


[DOCCC 1997](DOCCC_1997 "DOCCC 1997"), Round 10, [Diep](Diep "Diep") - Rookie 2.0 <a id="cite-note-15" href="#cite-ref-15">[15]</a>




```
[Event "DOCCC 1997"]
[Site "Alphen a/d Rijn NED"]
[Date "1997.11.30"]
[Round "10"]
[White "Diep"]
[Black "Rookie 2.0"]
[Result "0-1"]

1.d4 Nf6 2.c4 e6 3.g3 Bb4+ 4.Bd2 Be7 5.Bg2 d5 6.Nf3 O-O 7.O-O c6 8.Qc2 Nbd7 
9.Bf4 Nh5 10.Bc1 Nhf6 11.b3 b6 12.Rd1 Bb7 13.Nc3 Rc8 14.Bf4 b5 15.c5 b4 16.Nb1 
Ne4 17.Ne5 Nxe5 18.Bxe5 Nf6 19.Qd2 a5 20.a3 bxa3 21.Rxa3 Ra8 22.Rc1 Ng4 23.Bf4 
h6 24.f3 Nf6 25.Qc3 Nd7 26.Nd2 Re8 27.Bd6 Bxd6 28.cxd6 Qb8 29.Rxa5 Rxa5 30.Qxa5 
Qxd6 31.Qc3 e5 32.e3 g5 33.b4 Ra8 34.Nb3 Ra3 35.Bh3 exd4 36.exd4 Nb6 37.Qc5 Qf6 
38.Qxb6 Qe7 39.Nd2 Ra6 40.Qc5 Qe3+ 41.Kh1 Qxd2 42.Bg2 Kg7 43.f4 Ra2 44.Rg1 Rb2 
45.fxg5 Qxg5 46.Rf1 Qd2 47.Rg1 Qxb4 48.Qxb4 Rxb4 49.Rd1 Bc8 50.Kg1 Bf5 51.Rd2 
Rc4 52.Kf2 Rc3 53.Bf3 Be4 54.Be2 c5 55.dxc5 Rxc5 56.Bf3 f5 57.Bxe4 dxe4 58.Ke3 
Rc3+ 59.Kd4 Rf3 60.Rb2 Kf6 61.Ra2 Rd3+ 62.Kc4 Kg5 63.Ra6 h5 64.h4+ Kg4 65.Rg6+ 
Kh3 66.Rg5 Rf3 67.Rxh5 Kxg3 68.Rh8 e3 69.Kd3 Kf2 70.Re8 f4 71.Ke4 e2 72.Kf5 Re3 
73.Ra8 e1=Q 74.Ra6 Qe2 75.Rb6 Qh5+ 76.Kf6 Qh6+ 77.Kf7 Qxb6 78.h5 Qd6 79.Kg8 Re7 
80.Kh8 Qd8# 0-1

```

### WCCC 2011


[WCCC 2011](WCCC_2011 "WCCC 2011"), Round 1, Rookie 3.4 - [Shredder](Shredder "Shredder") <a id="cite-note-16" href="#cite-ref-16">[16]</a>




```
[Event "WCCC 2011"]
[Site "Tilburg NED"]
[Date "2011.11.23"]
[Round "1"]
[White "Rookie"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.e4 c5 2.Nc3 e6 3.Nf3 a6 4.d4 cxd4 5.Nxd4 Qc7 6.Qf3 Bd6 7.Be3 Nc6 8.O-O-O Be5 
9.Qe2 Nf6 10.g3 d6 11.f4 Bxd4 12.Bxd4 e5 13.fxe5 Nxd4 14.Rxd4 dxe5 15.Rc4 Qa5 
16.Qe3 Be6 17.Qc5 Qxc5 18.Rxc5 Nd7 19.Rc7 Rb8 20.Nd5 Rf8 21.Bg2 Kd8 22.Rc3 Bxd5 
23.exd5 f5 24.d6 g6 25.Rd1 e4 26.g4 Rc8 27.Rxc8 Kxc8 28.gxf5 gxf5 29.Rd5 Kd8 
30.c4 Nb6 31.Rd4 Re8 32.Kd2 h6 33.b4 Rg8 34.Bh3 Rg5 35.c5 Nd7 36.Rd5 f4 37.Rf5 
Rxf5 38.Bxf5 e3 39.Ke2 Ne5 40.a3 h5 41.Bh3 Nc6 42.Bf1 Ne5 43.h4 Kc8 44.a4 Nc6 
45.b5 axb5 46.axb5 Nd4 47.Kd3 Nxb5 48.Be2 Kd7 49.Bxh5 Nxd6 50.cxd6 Kxd6 51.Ke4
f3 52.Kxe3 f2 53.Kxf2 Kd5 1/2-1/2

```

## See also


* [Floyd](Floyd "Floyd")
* [MSCP](MSCP "MSCP")


## Publications


* [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf) <a id="cite-note-17" href="#cite-ref-17">[17]</a>
* [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *[A pattern-recognition strategy for chess position evaluation](http://marcelk.net/thesis/talk-eval-rookie/sld001.htm)*. Slides from *The design and implementation of the Rookie 2.0 Chess Playing Program*.
* [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2013**). *A fast software-based method for upcoming cycle detection in search trees*. [pdf preview](http://marcelk.net/2013-04-06/paper/upcoming-rep-v2.pdf) » [Repetitions](Repetitions "Repetitions") <a id="cite-note-18" href="#cite-ref-18">[18]</a>


## Forum Posts


* [Rookie program deserves a look](https://www.stmintz.com/ccc/index.php?id=29929) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), October 19, 1998
* [Rotor uses Rookie's attack table!](http://www.talkchess.com/forum/viewtopic.php?t=32925) by [Jan Brouwer](Jan_Brouwer "Jan Brouwer"), [CCC](CCC "CCC"), February 26, 2010 » [Rotor](Rotor "Rotor")
* [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410664&t=39407) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), June 18, 2011
* [2011 Fifth Annual ACCA WCRCC: Rookie games](http://www.talkchess.com/forum/viewtopic.php?t=39845) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), July 24, 2011
* [ICT13 programmer's report: Rookie v3.7](http://www.open-chess.org/viewtopic.php?f=3&t=2336) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 04, 2013 » [ICT 2013](ICT_2013 "ICT 2013")
* [test position: Rookie-Arasan](http://www.talkchess.com/forum/viewtopic.php?t=51071) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 27, 2014 » [Arasan](Arasan "Arasan"), [Zugzwang](Zugzwang "Zugzwang")
* [Some SMP measurements with Rookie v3](http://www.talkchess.com/forum/viewtopic.php?t=55224) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), February 05, 2015 » [Parallel Search](Parallel_Search "Parallel Search")


## External Links


### Chess Engine


* [Rookie's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=716)
* [Index of /rookie](http://marcelk.net/rookie/) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") [archive.org](https://web.archive.org/web/20201106235548/http://marcelk.net/rookie/)
* [The chess games of Rookie](http://www.chessgames.com/perl/chessplayer?pid=134353) from [chessgames.com](http://www.chessgames.com/index.html)


### Misc


* [Rookie from Wikipedia](https://en.wikipedia.org/wiki/Rookie)


 [Rookie of the Year (award) from Wikipedia](https://en.wikipedia.org/wiki/Rookie_of_the_Year_%28award%29)
* [rookie - Wiktionary](http://en.wiktionary.org/wiki/rookie)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Index of /rookie/nostalgia/v1](http://marcelk.net/rookie/nostalgia/v1/)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> Rookie 1.0 [68000](68000 "68000") [assembly](Assembly "Assembly") source, search.s from [Index of /rookie/nostalgia/v1](http://marcelk.net/rookie/nostalgia/v1/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> ['Rookie' timeline](http://marcelk.net/thesis/talk-eval-rookie/sld004.htm) from [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *[A pattern-recognition strategy for chess position evaluation](http://marcelk.net/thesis/talk-eval-rookie/sld001.htm)*. Slides from *The design and implementation of the Rookie 2.0 Chess Playing Program*.
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Rotor uses Rookie's attack table!](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=334259&t=32925) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), February 28, 2010
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *The design and implementation of the Rookie 2.0 Chess Playing Program*. Masters Thesis, [pdf](http://alexandria.tue.nl/extra2/afstversl/wsk-i/kervinck2002.pdf), Overview of Rookie 2.0 Eval, pp. 66
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> Images from [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck") (**2002**). *A pattern-recognition strategy for chess position evaluation*. Slides from *The design and implementation of the Rookie 2.0 Chess Playing Program*.
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Rookie 2.0: triple-stage evaluator](http://marcelk.net/thesis/talk-eval-rookie/sld013.htm)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [The big picture](http://marcelk.net/thesis/talk-eval-rookie/sld017.htm)
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Re: Programmers: what's the story behind the name of your engine](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410664&t=39407) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), June 18, 2011
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Upcoming repetition detection](http://www.open-chess.org/viewtopic.php?f=5&t=2300) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 06, 2013 » [Repetitions](Repetitions "Repetitions")
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> [ICT13 programmer's report: Rookie v3.7](http://www.open-chess.org/viewtopic.php?f=3&t=2336) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 04, 2013
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Programmersprize 2010](http://www.csvn.nl/index.php?option=com_content&view=article&id=468%3Arules-programmersprize&catid=51%3Atoernooien&Itemid=28&lang=en)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [ICT11 Round 7 - Photos](http://www.csvn.nl/index.php?option=com_content&view=article&id=508%3Aict11-round-7&catid=51%3Atoernooien&Itemid=28&lang=en)
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Downloads | Open Dutch Computer Chess Championships | Games](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=37&Itemid=26&lang=en&limitstart=15)
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Rookie (Computer) vs Shredder (Computer) (2011)](http://www.chessgames.com/perl/chessgame?gid=1649053) from [chessgames.com](http://www.chessgames.com/index.html)
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [Chess Programmers -- take note: M. N. J. van Kervinck's Master's Thesis](https://www.stmintz.com/ccc/index.php?id=246260) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), August 19, 2002
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Upcoming repetition detection](http://www.open-chess.org/viewtopic.php?f=5&t=2300) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), April 06, 2013

**[Up one Level](Engines "Engines")**







 
