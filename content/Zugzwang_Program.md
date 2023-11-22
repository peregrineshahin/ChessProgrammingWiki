---
title: Zugzwang Program
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Zugzwang**


**Zugzwang** was a massive parallel chess program by [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") and [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") from the [Paderborn University](Paderborn_University "Paderborn University"), Germany. It won the bronze medal at the [2nd Computer Chess Olympiad, London 1990](2nd_Computer_Olympiad#Chess "2nd Computer Olympiad"), and was runner up with three wins and two draws at the [WCCC 1992](WCCC_1992 "WCCC 1992"), and won three times the International Paderborn Computer Chess Championships [IPCCC](IPCCC "IPCCC"). The Zugzwang team was completed by chess player and [opening book author](Category:Opening_Book_Author "Category:Opening Book Author") [Heiner Matthias](Heiner_Matthias "Heiner Matthias"). Zugzwang was first based on [Transputer](Transputer "Transputer") technology with a grid of up to 1024 [Inmos](https://en.wikipedia.org/wiki/Inmos) T800 and later T805 processors. Software was developed in the [Occam](https://en.wikipedia.org/wiki/Occam_%28programming_language%29) programming language. Later it was also ported to the [C-programming language](C "C"), to run on other hardware architectures such as the [Cray T3E](Cray_T3E "Cray T3E") supercomputer in 1999. The [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") was elaborated exhaustingly by Feldmann et al. <a id="cite-note-1" href="#cite-ref-1">[1]</a><a id="cite-note-2" href="#cite-ref-2">[2]</a>. Zugzwang didn't use [Null Move Pruning](Null_Move_Pruning "Null Move Pruning"), but Feldmann's [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions") as well based on the [Null Move Observation](Null_Move_Observation "Null Move Observation") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Zugzwang's [evaluation](Evaluation "Evaluation") was [tuned](Automated_Tuning "Automated Tuning") by [simulated annealing](Simulated_Annealing "Simulated Annealing") as described in Mysliwietz' Ph.D. thesis <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



## Descriptions


given from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-5" href="#cite-ref-5">[5]</a>:



### 1995



```
Zugzwang made its first moves in 1989. It won the bronze medal in the 1990 Computer Olympiad, and won the Paderborn (human) Championships in 1991. In the last [Computer World Championships in Madrid 1992](WCCC_1992 "WCCC 1992"), Zugzwang, running on a system consisting of 1023 T800 transputers, finished second and was undefeated without playing the eventual Champion, [ChessMachine Schroeder](ChessMachine "ChessMachine"). In 1993 Zugzwang had its first victory over a grandmaster. In 1994 Zugzwang was completely rewritten from OCCAM to C (about 20,000 lines of code) and is now portable to a large spectrum of machines including [SPARC](SPARC "SPARC"), SGI, [DEC Alpha](DEC_Alpha "DEC Alpha"), [i860](I860 "I860"), [486](X86 "X86") and [PowerPC](PowerPC "PowerPC"). In this year's Championships, Zugzwang will run on a GC-Powerplus distributed system (based on the PowerPC) with at least 96 processors. The [opening book](Opening_Book "Opening Book") contains about 130,000 moves and 1MB [transposition tables](Transposition_Table "Transposition Table") are used per processor. Zugzwang uses [brute-force](Brute-Force "Brute-Force") [alpha-beta](Alpha-Beta "Alpha-Beta")  search with [history tables](History_Heuristic "History Heuristic") and [killer heuristics](Killer_Heuristic "Killer Heuristic"). The program searches about 3000 [nodes per second](Nodes_per_Second "Nodes per Second") per processor on a PowerPC. The search is performed by distributed processors using a distributed algorithm based on the [Young Brothers Wait Concept](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), which gives good results even if as many as 1000 processors are used. In this case the system calculates moves more than 400 times faster than a sequential system. 

```

### 1999



```
Zugzwang has been written by Rainer Feldmann and Peter Mysliwietz (until 1996). Rainer Feldmann is a member, Peter Mysliwietz a former member of the research group of [Prof. Dr. Burkhard Monien](Burkhard_Monien "Burkhard Monien") at the University of Paderborn. Zugzwang is a product of an ongoing research in the field of efficient parallel algorithms for optimization problems. In the course of this research we developed a parallel game tree search algorithm which runs efficiently even on massively parallel systems without any shared memory.

```


```
The program started as an OCCAM program for Transputers. In 1992 it played the [WCCC in Madrid](WCCC_1992 "WCCC 1992") running on a system with 1024 processors. From 1995 the program was rewritten to C. It now runs efficiently on various hardware platforms as e.g. PowerPC based parallel computers or the [Cray T3E](Cray_T3E "Cray T3E").

```


```
The opening book of Zugzwang is handwritten. No automatic opening book compilation is used. The search algorithm used is the [Fail-High Reductions](Fail_High_Reductions "Fail-High Reductions") algorithm. The program has access to the [endgame databases](Thompson%27s_Databases "Thompson's Databases") of [Ken Thompson](Ken_Thompson "Ken Thompson").

```


```
The most recent tournament played was the Lippstadt Grandmaster Tournament in August 1998, where the program finished second and played at a rate of about 2600 ELO points. The program ran on a Cray T3E with 512 processors (300 MHz) at the [John von Neumann Institute for Computing](https://en.wikipedia.org/wiki/Forschungszentrum_J%C3%BClich) <a id="cite-note-6" href="#cite-ref-6">[6]</a> in [Juelich](https://en.wikipedia.org/wiki/J%C3%BClich), Germany. 

```

## See also


* [Alpha I](Alpha_I "Alpha I")
* [Zugzwang](Zugzwang "Zugzwang")


## Publications


* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Oliver Vornberger](Oliver_Vornberger "Oliver Vornberger") (**1989**). *Distributed Game-Tree Search*. [ICCA Journal, Vol. 12, No. 2](ICGA_Journal#12_2 "ICGA Journal") <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1992**). *Experiments with a Fully Distributed Chess Program*. [Heuristic Programming in AI 3](3rd_Computer_Olympiad#Workshop "3rd Computer Olympiad")
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems*. Phd-Thesis, [pdf](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1994**). *Game-Tree Search on a Massively Parallel System*. [Advances in Computer Chess 7](Advances_in_Computer_Chess_7 "Advances in Computer Chess 7")
* [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
* [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1998**). *Selective Game Tree Search on a Cray T3E*. [ps](http://www2.cs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/FM_T3E.ps.Z) <a id="cite-note-8" href="#cite-ref-8">[8]</a>


## Forum Posts


* [Re: Playing for position (mobility)](http://groups.google.com/group/rec.games.chess.computer/msg/6d07c745072dc611) by [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 02, 1995 » [Mobility](Mobility "Mobility")
* [Zugzwang with GM-like perfomance in Lippstadt tournament](https://www.stmintz.com/ccc/index.php?id=25061) by [Dirk Frickenschmidt](Dirk_Frickenschmidt "Dirk Frickenschmidt"), [CCC](CCC "CCC"), August 19, 1998
* [What went wrong with P.Conners and Zugzwang in WCCC?](https://www.stmintz.com/ccc/index.php?id=58557) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), June 29, 1999 » [WCCC 1999](WCCC_1999 "WCCC 1999")


## External Links


* [Zugzwang's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=54)
* [Zugzwang's games at chessgames.com](http://www.chessgames.com/perl/ezsearch.pl?search=Zugzwang)
* [Parallele Suche in Spielbäumen](http://www.faui01.de/brettspiele/parallel.pdf) (pdf) by Stefan Büttcher (german)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann"), [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz"), [Burkhard Monien](Burkhard_Monien "Burkhard Monien") (**1991**). *A Fully Distributed Chess Program*. [Advances in Computer Chess 6](Advances_in_Computer_Chess_6 "Advances in Computer Chess 6"), [pdf](http://www.top-5000.nl/ps/A%20fully%20distribuited%20chess%20program.pdf)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1993**). *Game Tree Search on Massively Parallel Systems* Phd-Thesis, [pdf](http://wwwcs.uni-paderborn.de/fachbereich/AG/monien/PUBLICATIONS/POSTSCRIPTS/feldmann_phd.pdf)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Rainer Feldmann](Rainer_Feldmann "Rainer Feldmann") (**1997**). *Fail-High Reductions.* [Advances in Computer Chess 8](Advances_in_Computer_Chess_8 "Advances in Computer Chess 8"), [pdf](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=4399933A9FAE32A9C855DED714120C66?doi=10.1.1.51.4897&rep=rep1&type=pdf) from [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.4897)
4. <a id="cite-ref-4" href="#cite-note-4">↑</a>  [Peter Mysliwietz](Peter_Mysliwietz "Peter Mysliwietz") (**1994**). *Konstruktion und Optimierung von Bewertungsfunktionen beim Schach.* Ph.D. thesis (German)
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Zugzwang's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=54)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [John von Neumann Institute for Computing](http://fzj.helmholtz.de/nic/nic-e.html)
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer") (**1989**). *Comment on 'Distributed Game-Tree Search'* . [ICCA Journal, Vol. 12, No. 4](ICGA_Journal#12_4 "ICGA Journal")
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Forschungszentrum Jülich schickt Cray T-3 zur Schachweltmeisterschaft](https://www.computerwoche.de/a/forschungszentrum-juelich-schickt-cray-t-3-zur-schachweltmeisterschaft,508177), June 09, 1999, [Computerwoche](Computerworld#Woche "Computerworld") (German) » [WCCC 1999](WCCC_1999 "WCCC 1999")

**[Up one Level](Engines "Engines")**







 
