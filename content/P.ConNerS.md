---
title: P.ConNerS
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* P.ConNerS**


**P.ConNerS**,  

a parallel chess program by [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"). P.ConNerS used the unique approach of [Parallel Controlled Conspiracy Number Search](Conspiracy_Number_Search#PCCNS "Conspiracy Number Search"), developed by Ulf Lorenz and [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") <a id="cite-note-1" href="#cite-ref-1">[1]</a> within the research group of [Burkhard Monien](Burkhard_Monien "Burkhard Monien") from the [Paderborn University](Paderborn_University "Paderborn University").
[Heiner Matthias](Heiner_Matthias "Heiner Matthias") was responsible for the [book moves](Opening_Book "Opening Book").



### ICGA


from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-2" href="#cite-ref-2">[2]</a>:




```C++
P.ConNerS stands for 'Parallel Controlled Conspiracy Number Search. It has been written by Ulf Lorenz, who is a member of Prof. Dr. Burkhard Monien's research group at the University of Paderborn. U. Lorenz mainly works on the research fields of domain independent selective search in game trees, and on the field of efficient parallel algorithms for optimization problems. P.ConNerS uses a variant of the so called 'Controlled Conspiracy Number Search' algorithm. As a result it examines highly selective and irregular game trees. Evaluations are done by the help of [depth](Depth "Depth") 2 [alphabeta searches](Alpha-Beta "Alpha-Beta"). When it runs on a parallel machine with 60 Pentium 300 MHz processors, P.ConNerS reaches a rate of about 1.2 million [nodes per second](Nodes_per_Second "Nodes per Second"). 

```

### P.ConNerS


from the P.ConNerS site, after winning the 10th Grandmaster Tournament in [Lippstadt](https://en.wikipedia.org/wiki/Lippstadt), July 2000 <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```C++
P.ConNerS stands for 'Parallel Controlled Conspiracy Number Search'. Thus, the tournament victory is highly interesting from a research perspective, as well: P.ConNerS uses a non-conventional, non-alphabeta search algorithm. The search algorithm tries not only to maximize the search depth, but also tries to guarantee that even when one leaf-value changes, the result stays the same. A conspiracy 2 search may be interpreted as a special, global arrangement of a lot of so called [singular extensions](Singular_Extensions "Singular Extensions"). As a result, it domain-independently searches highly selective and irregular game trees. The program is written in [C](C "C").

```


```C++
P.ConNerS runs in [parallel](Parallel_Search "Parallel Search") and gets its [playing strength](Playing_Strength "Playing Strength") out of a workstation cluster, which consists of 160 [Pentium II](X86 "X86"), 450 Mhz processors. Those are connected with a new European interconnection network, the so called SCI network. On that machine P.ConNerS examines between 3.5 and 5.0 Mnds/sec. On the 160 processors it achieves a speedup of about 50. 

```

## Achievements


* Winner [IPCCC 1999](IPCCC_1999 "IPCCC 1999").
* Winner of the 10th Grandmaster Tournament in [Lippstadt](https://en.wikipedia.org/wiki/Lippstadt), Germany <a id="cite-note-4" href="#cite-ref-4">[4]</a>.


## Selected Games


10th Grandmaster Tournament, [Lippstadt](https://en.wikipedia.org/wiki/Lippstadt), P.ConNerS - [Maia Chiburdanidze](https://en.wikipedia.org/wiki/Maia_Chiburdanidze) <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "Lippstadt 10th"]
[Site "Lippstadt"]
[Date "2000.07.06"]
[Round "2"]
[White "P.ConNers"]
[Black "Maia Chiburdanidze"]
[Result "1-0"]

1.c4 e5 2.Nc3 Bb4 3.Nd5 Be7 4.d4 d6 5.e4 Nc6 6.dxe5 dxe5 7.Nf3 Bg4 8.Be2 Nf6 
9.O-O O-O 10.Nxe5 Nxe5 11.Nxf6+ Bxf6 12.Bxg4 Qxd1 13.Bxd1 Nxc4 14.Be2 Na3 
15.Bf4 Bxb2 16.Rad1 c6 17.Rd2 Bc3 18.Rd7 Rfe8 19.Bc1 Nb5 20.Bc4 Rxe4 21.Bxf7+ 
Kh8 22.Rfd1 Bf6 23.Rxb7 Nd6 24.Rd7 Nxf7 25.Rxf7 Ra4 26.a3 c5 27.Rdd7 Kg8 28.Kf1 
a6 29.Bg5 Ba1 30.Be3 Rc8 31.Bc1 Rc4 32.Be3 Rc2 33.Rf5 c4 34.Ra5 Rc6 35.Ra7 Rd6 
36.g3 Rd1+ 37.Kg2 Bf6 38.R5xa6 c3 39.a4 Re2 40.Rc6 h5 41.a5 Ra2 42.a6 Rda1 
43.Ra8+ Kh7 44.a7 Kg6 45.Kf3 Ra4 46.h3 Kh7 47.g4 hxg4+ 48.hxg4 Bd4 49.Bxd4 Rxd4
50.g5 Rda4 51.Rh8+ 1-0

```

## See also


* [Arachne](Arachne "Arachne")
* [Ulysses](Ulysses "Ulysses")


## Publications


* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2000**). *P.ConNerS wins the 10th Grandmaster Tournament in Lippstadt (Germany)*. [ICGA Journal, Vol. 23, No. 3](ICGA_Journal#23_3 "ICGA Journal")
* [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz") (**2002**). *[Parallel Controlled Conspiracy Number Search](https://link.springer.com/chapter/10.1007/3-540-45706-2_57)*. [Euro-Par 2002](https://dblp1.uni-trier.de/db/conf/europar/europar2002.html), [LNCS](https://en.wikipedia.org/wiki/Lecture_Notes_in_Computer_Science) 2400, [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media)


## Forum Posts


### 1998 ...


* [Is there really any good alternative to alfa-beta search?](https://www.stmintz.com/ccc/index.php?id=20233) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), June 09, 1998
* [WCCC 99 LambChop - P. ConNerS "1 - 0" Round 1](https://www.stmintz.com/ccc/index.php?id=55675) by Jose Hernandez, [CCC](CCC "CCC"), June 14, 1999 » [LambChop](LambChop "LambChop"), [WCCC 1999](WCCC_1999 "WCCC 1999")
* [What went wrong with P.Conners and Zugzwang in WCCC?](https://www.stmintz.com/ccc/index.php?id=58557) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), June 29, 1999 » [WCCC 1999](WCCC_1999 "WCCC 1999")


### 2000 ...


* [P.Conners is leading with 4 out of 5](https://www.stmintz.com/ccc/index.php?id=118581) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 10, 2000
* [About PConners](https://www.stmintz.com/ccc/index.php?id=121556) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), July 25, 2000
* [Test Position, Rook and Pawn Ending, Yace- P.ConNerS (0-1)](https://www.stmintz.com/ccc/index.php?id=155540) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), February 22, 2001


## External Links


* [P.ConNerS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=95)
* [The chess games of ConNers](http://www.chessgames.com/perl/chessplayer?pid=112697) from [chessgames.com](http://www.chessgames.com/index.html)
* [The chess program P.ConNerS](https://www.wiwi.uni-siegen.de/technologiemanagement/hp/lorenz/pconners.html?lang=en)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Ulf Lorenz](Ulf_Lorenz "Ulf Lorenz"), [Valentin Rottmann](Valentin_Rottmann "Valentin Rottmann") (**1996**). *Parallel Controlled Conspiracy-Number Search.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [P.ConNerS' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=95)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [The chess program P.ConNerS](https://www.wiwi.uni-siegen.de/technologiemanagement/hp/lorenz/pconners.html?lang=en)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Computer P.ConNers gewinnt 10. Lippstädter GM Turnier](http://www.hsk1830.de/pages/berichte/lippstadt/lippstadt00.htm)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ConNers (Computer) vs Maia Chiburdanidze (2000)](http://www.chessgames.com/perl/chessgame?gid=1285976) from [chessgames.com](http://www.chessgames.com/index.html)

**[Up one Level](Engines "Engines")**







 
