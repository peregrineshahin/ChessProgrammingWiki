---
title: L27Excentrique
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* L'Excentrique**



[ Cam disc with tappet <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**L'Excentrique**,  

a chess program by [Claude Jarry](Claude_Jarry "Claude Jarry") running on [Amdahl](Amdahl_470 "Amdahl 470") mainframe computers <a id="cite-note-2" href="#cite-ref-2">[2]</a>. It incorporated [iterative deepening](Iterative_Deepening "Iterative Deepening") with two [ply](Ply "Ply") increments, to overcome possible inconsistencies introduced by the alternation of attacking and defensive continuations returned by successive [even-odd ply](Odd-Even_Effect "Odd-Even Effect") searches <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Further, the program used pure [Minimax](Minimax "Minimax") for the first few iterations in order to find and save the strongest continuation for each first level move. On deeper levels, L'Excentrique employs [alpha-beta](Alpha-Beta "Alpha-Beta"). Jarry argued that finding the strongest continuation for each first ply move on the initial few iterations results in faster searches on later iterations <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Photos](#photos)
* [3 Games](#games)
* [4 Fast Searcher](#fast-searcher)
* [5 External Links](#external-links)
* [6 References](#references)






L'Excentrique participated at the [ACM 1976](ACM_1976 "ACM 1976"), [ACM 1979](ACM_1979 "ACM 1979") and [ACM 1981](ACM_1981 "ACM 1981"), and the [3rd WCCC 1980](WCCC_1980 "WCCC 1980") in [Linz](http://en.wikipedia.org/wiki/Linz), where it upset reigning champion [Chess 4.9](Chess_(Program) "Chess (Program)") in round one, becoming strong fourth only losing from [Belle](Belle "Belle") <a id="cite-note-5" href="#cite-ref-5">[5]</a> . 



## Photos


 [](https://www.computerhistory.org/chess/stl-430b9bbe22237/) 
[Claude Jarry](Claude_Jarry "Claude Jarry") with L'Excentrique, [ACM 1979](ACM_1979 "ACM 1979") <a id="cite-note-6" href="#cite-ref-6">[6]</a>



## Games


[WCCC 1980](WCCC_1980 "WCCC 1980") Round 1 <a id="cite-note-7" href="#cite-ref-7">[7]</a>




```

[Event "3rd World Computer Chess Championship"]
[Site "Linz, Austria"]
[Date "1980.09.25"]
[Round "1"]
[White "L'Excentrique"]
[Black "Chess 4.9"]
[Result "1-0"]

1.e4 e5 2.Nf3 Nf6 3.d4 Nxe4 4.Bd3 d5 5.Nxe5 Bd6 6.c4 Bxe5 7.dxe5 Nc6 8.Bc2 Nxe5
9.Qxd5 Qxd5 10.cxd5 Bf5 11.O-O c6 12.f4 Ng4 13.h3 Ngf6 14.g4 Nd2 15.Re1+ Kf8
16.Bd1 Bxb1 17.Bxd2 Bd3 18.Re3 Bc4 19.Bb4+ Kg8 20.d6 Nd5 21.Re4 Bd3 22.Rd4 Nxb4
23.Rxb4 b6 24.Rd4 Bb5 25.a4 c5 26.Rd2 Bc6 27.a5 Rd8 28.a6 h5 29.gxh5 Rh6 30.Bg4
Rhxd6 31.Rxd6 Rxd6 32.Kf2 Rd2+ 33.Ke3 Rxb2 34.Rd1 Rb3+ 35.Kf2 Be4 36.Rd8+ Kh7
37.Rf8 f6 38.Rf7 Ra3 39.Rxa7 f5 40.Be2 Rxh3 41.Rd7 Rh2+ 42.Ke3 Rh1 43.Rd8 Rh3+
44.Kd2 Rb3 45.Bc4 Rb4 46.Bf7 Rd4+ 47.Rxd4 cxd4 48.a7 Kh6 49.Bg6 Bg2 50.Kd3 b5
51.Bxf5 g5 52.Be4 Bf1+ 53.Kxd4 Kxh5 54.f5 g4 55.a8=Q Kh4 56.Ke3 Kh3 57.Kf2 1-0

```

[WCCC 1980](WCCC_1980 "WCCC 1980") Round 3 <a id="cite-note-8" href="#cite-ref-8">[8]</a>




```

[Event "3rd World Computer Chess Championship"]
[Site "Linz, Austria"]
[Date "1980.09.27"]
[Round "3"]
[White "Belle"]
[Black "l'Excentrique"]
[Result "1-0"]

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Bc4 Ndf6 6.Ng5 e6 7.Ne2 h6 8.Nf3 Bd6
9.O-O b5 10.Bd3 Ne7 11.a4 bxa4 12.Rxa4 O-O 13.Be3 Ng4 14.Bf4 Bxf4 15.Nxf4 Qd6
16.Nh5 g6 17.Ng3 f5 18.Qa1 a6 19.Re1 Nf6 20.Bxa6 Bxa6 21.Rxa6 Rxa6 22.Qxa6 f4
23.Ne4 Nxe4 24.Rxe4 g5 25.c4 Rb8 26.c5 Qd5 27.Re2 g4 28.Qa7 Re8 29.Re5 Qd8
30.Ne1 Nf5 31.Qa6 Nxd4 32.Qd3 Kg7 33.Qe4 Rf8 34.Kh1 Rf5 35.Nd3 Kf6 36.Nxf4 g3
37.f3 gxh2 38.Rxe6+ Nxe6 39.Qxe6+ Kg7 40.Qxf5 Kg8 41.Qg6+ Kh8 42.Qf7 Qg5
43.Ng6+ Qxg6 44.Qxg6 h5 45.f4 h4 46.f5 h3 47.f6 hxg2+ 48.Qxg2 1-0

```

## Fast Searcher


According to [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), L'Excentrique was a fast and [tactical](Tactics "Tactics") strong searcher <a id="cite-note-9" href="#cite-ref-9">[9]</a> :




```C++
I remember [Ken](Ken_Thompson "Ken Thompson") once saying "If you can just hold on and not get caught by its tactics, it will eventually 'fold' and make a horrible positional mistake and crumble away." 

```

## External Links


* [l'Excentrique's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=423)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Excentrique (mécanique)](https://fr.wikipedia.org/wiki/Excentrique_%28m%C3%A9canique%29)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Ben Mittman](Ben_Mittman "Ben Mittman"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1980**). *[Computer chess at ACM 79: the tournament and the man vs. man and machine match](http://dl.acm.org/citation.cfm?id=358817&dl=ACM&coll=DL&CFID=78577980&CFTOKEN=10389697)*. [Communications of the ACM](ACM#Communications "ACM"), Vol. 23, Issue 1, [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79/3-1%20and%203-2%20and%203-3.Computer_chess_at_ACM_79.062303018.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Eric Thé](Eric_Th%C3%A9 "Eric Thé") (**1992**). *[An analysis of move ordering on the efficiency of alpha-beta search](http://digitool.library.mcgill.ca/R/?func=dbin-jump-full&object_id=56753&local_base=GEN01-MCG02)*. Master's thesis, [McGill University](McGill_University "McGill University"), advisor [Monroe Newborn](Monroe_Newborn "Monroe Newborn")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [David Levy](David_Levy "David Levy"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1982, 1983**). *[All About Chess and Computers](https://link.springer.com/book/10.1007/978-3-642-85538-2)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), [Postscript: 1978 – 80 and BELLE The World Champion](https://rd.springer.com/chapter/10.1007/978-3-642-85538-2_14)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [David Levy](David_Levy "David Levy"), [Ben Mittman](Ben_Mittman "Ben Mittman"), [Monroe Newborn](Monroe_Newborn "Monroe Newborn") (**1980**). *3rd World Computer Chess Championship*. [ICCA Newsletter](ICGA_Journal "ICGA Journal"), Vol. 3, No. 3, reprinted in [The Fourth World Computer Chess Championship](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6c8af8) (labeled 22nd ACM), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/3-1%20and%203-2%20and%203-3%20and%204-3.1983_WCCC/1983-%20WCCC.062303061.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum"), [pdf](http://www.sci.brooklyn.cuny.edu/%7Ekopec/Publications/Publications/O_36_C.pdf) from [Danny Kopec](Danny_Kopec "Danny Kopec")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Photo](https://www.computerhistory.org/chess/stl-430b9bbe22237/) gifts by [Monroe Newborn](Monroe_Newborn "Monroe Newborn"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Linz 1980 - Chess - Round 1 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=68&round=1&id=1)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Linz 1980 - Chess - Round 3 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=68&round=3&id=3)
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Who is the better chess program author?](http://www.stmintz.com/ccc/index.php?id=201762) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), December 13, 2001

**[Up one level](Engines "Engines")**







 
