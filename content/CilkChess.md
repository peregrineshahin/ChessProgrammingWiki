---
title: CilkChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * CilkChess**

**CilkChess**,

a massive [parallel](Parallel_Search "Parallel Search") chess program written in the [C](C "C") or [C++](Cpp "Cpp") multithreaded programming extension [Cilk](Cilk "Cilk"). CilkChess was developed by various authors from [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") and elsewhere headed by [Charles Leiserson](Charles_Leiserson "Charles Leiserson") and programming lead by [Don Dailey](Don_Dailey "Don Dailey") <a id="cite-note-1" href="#cite-ref-1">[1]</a><a id="cite-note-2" href="#cite-ref-2">[2]</a>.

## Photos & Games

[](File:HiarcsCilk1999.JPG)
[WCCC 1999](WCCC_1999 "WCCC 1999"), round 7, [HIARCS](HIARCS "HIARCS") - CilkChess, [Erdogan Günes](Erdogan_G%C3%BCnes "Erdogan Günes"), [Charles Leiserson](Charles_Leiserson "Charles Leiserson") (back of head), and [Don Dailey](Don_Dailey "Don Dailey") <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "WCCC 1999"]
[Site "Paderborn, Germany"]
[Date "1999.06.19"]
[Round "7"]
[White "Hiarcs"]
[Black "CilkChess"]
[Result "0-1"]

1.d4 e6 2.c4 c5 3.Nf3 Nf6 4.e3 cxd4 5.exd4 d5 6.Nc3 Nc6 7.Bg5 Be7 8.c5 O-O 
9.Bb5 Bd7 10.O-O b6 11.Na4 bxc5 12.Bxf6 Bxf6 13.Nxc5 Re8 14.Rc1 Rc8 15.Ba6 
Rb8 16.b3 Qa5 17.a4 Rb4 18.Nd3 Rb6 19.Bb5 Rxb5 20.axb5 Nxd4 21.Nxd4 Bxd4 
22.Qc2 Bxb5 23.Rfd1 Qb6 24.Nc5 Be5 25.Qd2 Qb8 26.g3 Bf6 27.Rc2 Qa8 28.f3 a5 
29.Rdc1 Be7 30.Qd4 Bg5 31.f4 Bf6 32.Qd2 d4 33.Nd3 Be7 34.Rd1 Qf3 35.Ne5 Qe4 
36.Ra2 d3 37.Qg2 Qd4+ 38.Kh1 Bb4 39.Qb7 Qc5 40.Qe4 d2 41.Kg2 Qb6 42.Rc2 Rd8 
43.g4 f6 44.Nc6 Qb7 45.Qxe6+ Kf8 46.Kf2 Re8 47.Qd5 Bxc6 48.Rxc6 Qa7+ 0-1

```

## CilkChess Team

- [Reid Barton](Reid_Barton "Reid Barton")
- [Don Beal](Don_Beal "Don Beal") (engine programmer)
- [Don Dailey](Don_Dailey "Don Dailey") (lead programmer)
- [Matteo Frigo](Matteo_Frigo "Matteo Frigo")
- [Chris Joerg](Chris_Joerg "Chris Joerg")
- [Charles Leiserson](Charles_Leiserson "Charles Leiserson") (project leader)
- [Phil Lisiecki](Phil_Lisiecki "Phil Lisiecki")
- [Aske Plaat](Aske_Plaat "Aske Plaat")
- [Ryan Porter](Ryan_Porter "Ryan Porter")
- [Harald Prokop](Harald_Prokop "Harald Prokop")
- [David Venturini](index.php?title=David_Venturini&action=edit&redlink=1 "David Venturini (page does not exist)")

## Quotes

from Awards for Cilk Technology & Research <a id="cite-note-5" href="#cite-ref-5">[5]</a>:

- 1996 First Place in the [1996 Dutch Open Computer Chess Championship](DOCCC_1996 "DOCCC 1996") for CilkChess
- 1997 Second Place in the [1997 Dutch Open Computer Chess Championship](DOCCC_1997 "DOCCC 1997") for CilkChess

## Description

from the [WCCC 1999](WCCC_1999 "WCCC 1999") ICGA Tournament site <a id="cite-note-6" href="#cite-ref-6">[6]</a>:

```C++Cilkchess is a parallel program which will be running on a 256-processor SGI Origin 2000 at NASA Ames for the WCCC. Cilkchess won First Prize in the 1996 Dutch Open and took Second in both 1997 and 1998. Our earlier program, [\*Socrates](Star_Socrates "Star Socrates"), took Second in the [1995 WCCC](WCCC_1995 "WCCC 1995"), tying the winner [Fritz](Fritz "Fritz") in the main part of the tournament, but losing in the playoff.

```

```C++CilkChess is programmed in the [Cilk](Cilk "Cilk") multithreaded programming language <a id="cite-note-7" href="#cite-ref-7">[7]</a>, which allows highly irregular programs, such as chess, to be written with ease for parallel computers. The program uses a parallel variant of the [MTD(f)](MTD(f) "MTD(f)") search algorithm that incorporates [null-move forward pruning](Null_Move_Pruning "Null Move Pruning"), but few [extensions](Extensions "Extensions"). The [evaluation function](Evaluation_Function "Evaluation Function") has been tuned from thousands of self-play games using a [temporal-coherence learning](Temporal_Difference_Learning "Temporal Difference Learning") algorithm. The [transposition table](Transposition_Table "Transposition Table") is stored in 32 gigabytes of shared memory. In the late middle game, Cilkchess typically looks more than 15 [ply](Ply "Ply") (half-moves) ahead and performs 5-11 million [make-moves](Make_Move "Make Move") per second. 

```

## See also

- [Occam](Occam "Occam")

## Publications

- [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**2001**). *Using Cilk to Write Multiprocessor Chess Programs*. [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf)

## Forum Posts

- [CilkChess question for Don](https://www.stmintz.com/ccc/index.php?id=41708) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), January 31, 1999 » [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
- [Re: CilkChess](https://www.stmintz.com/ccc/index.php?id=43395) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), February 14, 1999 » [MTD(f)](</MTD(f)> "MTD(f)")
- [MTD is a big win](https://www.stmintz.com/ccc/index.php?id=61058) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 19, 1999

## External Links

- [The CilkChess Parallel Chess Program](http://supertech.csail.mit.edu/chess/)
- [The CilkChess Parallel Chess Program - in the 1998 Dutch Open Computer Chess Championship](http://people.csail.mit.edu/dutch98/)
- [CilkChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=56)
- [CilkChess from Wikipedia](https://en.wikipedia.org/wiki/CilkChess)
- [Cilk from Wikipedia](https://en.wikipedia.org/wiki/Cilk)
- [The Cilk Project](http://supertech.csail.mit.edu/cilk)
- [Intel Cilk Plus from Wikipedia](https://en.wikipedia.org/wiki/Intel_Cilk_Plus) » [Intel](Intel "Intel")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Cilkchess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=56)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The Cilkchess Parallel Chess Program](http://supertech.csail.mit.edu/chess/)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> Image captured from [Paderborn 1999 1.mp4](http://www.top-5000.nl/Paderborn_1999_1.mp4) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Paderborn 1999 - Chess - Round 7 - Game 12 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=8&round=7&id=12)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Awards for Cilk Technology & Research](http://www.cilk.com/company/awards/)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [CilkChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=56)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Don Dailey](Don_Dailey "Don Dailey"), [Charles E. Leiserson](Charles_Leiserson "Charles Leiserson") (**2001**). *Using Cilk to Write Multiprocessor Chess Programs*, [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9"), [pdf](http://supertech.csail.mit.edu/papers/icca99.pdf)

**[Up one Level](Engines "Engines")**

