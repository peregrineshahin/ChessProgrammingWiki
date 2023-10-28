---
title: Nightmare GER
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nightmare GER**



[ [Henry Fuseli](Category:Henry_Fuseli "Category:Henry Fuseli") - The Nightmare<a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Nightmare**,  

a chess program by [Reinhold Gellner](Reinhold_Gellner "Reinhold Gellner") and [Gaby von Rekowski](Gaby_von_Rekowski "Gaby von Rekowski"), playing various tournaments in the late 80s and 90s, most notably the [WMCCC 1989](WMCCC_1989 "WMCCC 1989"), [ACM 1990](ACM_1990 "ACM 1990"), [WMCCC 1990](WMCCC_1990 "WMCCC 1990"), [2nd Computer Olympiad 1990](2nd_Computer_Olympiad#Chess "2nd Computer Olympiad"), [WMCCC 1991](WMCCC_1991 "WMCCC 1991"), [WCCC 1992](WCCC_1992 "WCCC 1992"), [WMCCC 1993](WMCCC_1993 "WMCCC 1993"), [WCCC 1995](WCCC_1995 "WCCC 1995"), [WMCCC 1995](WMCCC_1995 "WMCCC 1995"), [WMCCC 1996](WMCCC_1996 "WMCCC 1996"), [WMCCC 1997](WMCCC_1997 "WMCCC 1997"), [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments") and the early [IPCCCs](IPCCC "IPCCC"). 



### Contents


* [1 Description](#description)
* [2 Selected Games](#selected-games)
	+ [2.1 WMCCC 1990](#wmccc-1990)
	+ [2.2 WMCCC 1996](#wmccc-1996)
* [3 Namesake](#namesake)
* [4 Publications](#publications)
* [5 External Links](#external-links)
	+ [5.1 Chess Engine](#chess-engine)
	+ [5.2 Misc](#misc)
* [6 References](#references)






given in 1995 <a id="cite-note-2" href="#cite-ref-2">[2]</a> :




```
Completely written in [C](C "C"), work on Nightmare started in 1989 as a non-commercial project. It is a [brute force](Brute-Force "Brute-Force") program searching up to 7-ply in the middle-game with a selective search depth of up to 40 ply. Modified [null-move searches](Null_Move_Pruning "Null Move Pruning"), modified [singular extensions](Singular_Extensions "Singular Extensions"), [part-ply extensions](Extensions#FractionalExtensions "Extensions") and a new idea of hashing related meaningful subtrees are special features of Nightmare.

```


```
The program also uses well known techniques like [killer-moves](Killer_Heuristic "Killer Heuristic"), [history heuristic](History_Heuristic "History Heuristic"), [principal variation search](Principal_Variation_Search "Principal Variation Search") and [hash tables](Transposition_Table "Transposition Table") of 64,000 entries per side. The tournament [opening book](Opening_Book "Opening Book") consists of about 40,000 moves. Endgame databases are NOT used. Last year, Nightmare was transferred to 32-bit under extended [DOS](MS-DOS "MS-DOS") and it can now search 12,000 moves per second. The program's rating is about 2000ELO (German) on a [486-50](X86 "X86"). 

```

## Selected Games


### WMCCC 1990


[WMCCC 1990](WMCCC_1990 "WMCCC 1990"), round 3, [BB](BB "BB") - Nightmare <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "WMCCC 1990"]
[Site "Lyon, France"]
[Date "1990.01.01"]
[Round "3"]
[White "BB"]
[Black "Nightmare (D)"]
[Result "0-1"]

1.d4 Nf6 2.e3 d5 3.f3 Nbd7 4.Bd3 e5 5.Bf5 c5 6.Nc3 cxd4 7.exd4 exd4 8.Qxd4 Nc5 9.Qe5+ Qe7 10.Qxe7+
Bxe7 11.Bxc8 Rxc8 12.Be3 O-O 13.O-O-O Rfd8 14.Bg5 d4 15.Nb5 Ne6 16.Bd2 a6 17.Na3 d3 18.c3 Bxa3 
19.bxa3 Nd5 20.Kb2 b5 21.Re1 Nb6 22.Kb1 Nc4 23.Kc1 Nxa3 24.Re4 Nc5 25.Rb4 a5 26.Rb2 b4 27.Bg5 
bxc3 28.Bxd8 cxb2+ 29.Kxb2 Rxd8 30.Nh3 Nc4+ 31.Kc3 Na3 32.Rd1 Nc2 33.Kd2 Rd4 34.Rb1 Rb4 35.Rxb4 
Nxb4 36.Nf2 a4 37.a3 Nc2 38.Nxd3 Nxd3 39.Kxc2 Ne1+ 40.Kd2 Nxg2 41.Ke2 Kf8 42.Kf2 Nf4 43.Ke3 Ne6 
44.Kd3 Ke7 45.h4 Kd6 46.Kc4 Ke5 47.h5 Kf4 48.h6 gxh6 49.Kb4 Kxf3 50.Kxa4 Ke4 51.Kb4 h5 52.a4 h4 
53.a5 Nc7 54.Kc5 h3 55.Kd6 Na8 56.Kc6 h2 0-1 

```

### WMCCC 1996


[WMCCC 1996](WMCCC_1996 "WMCCC 1996"), round 3, [Patzer](Patzer "Patzer") - Nightmare <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "WMCCC 1996"]
[Site "Jakarta, ID"]
[Date "1996.10.09"]
[Round "3"]
[White "Patzer"]
[Black "Nightmare (D)"]
[Result "0-1"]

1.e4 e5 2.Nc3 Nf6 3.g3 Bc5 4.Bg2 O-O 5.Nf3 d5 6.exd5 e4 7.Ng1 Re8 8.Nge2 Na6 9.a3 Bf5 10.d4 exd3 
11.cxd3 Bd6 12.O-O Nc5 13.d4 Nd3 14.Qb3 a6 15.Qxb7 a5 16.Qc6 Rb8 17.Ra2 Ng4 18.f3 Nxc1 19.Rxc1 Ne3 
20.Qa6 Rb6 21.Qxa5 Bd3 22.Ne4 Bxe2 23.Qd2 Bc4 24.Raa1 Rb3 25.Rc3 Nxg2 26.Rxc4 Ne3 27.Rc3 Rxc3
28.Nxc3 Nc4 29.Qc2 Qg5 30.Qf2 Qe3 31.Qxe3 Rxe3 32.Nb5 h6 33.Nxc7 Bxc7 34.Rc1 Nxb2 35.Rxc7 Rd3 
36.Rc2 Nd1 37.Rc4 Ne3 38.Rc8+ Kh7 39.Rc7 Nxd5 40.Rxf7 Rxa3 41.Rf5 Ne7 42.Rf7 Nc6 43.d5 Ne5 44.Re7 
Ng6 45.Rd7 Rxf3 46.Rd8 Rd3 47.Kf2 Ne7 48.d6 Nc6 49.Rd7 Ne5 50.Ke2 Rd4 51.Re7 Nc4 52.d7 Nb6 53.Re8 
Nxd7 54.Rd8 Kg6 55.h3 Rd5 56.Kf2 Nf6 57.Rxd5 Nxd5 58.Kf3 Kf5 59.g4+ Ke5 60.Kg3 Nf4 61.Kh2 Ke4 
62.Kg3 g5 63.h4 Ke3 64.hxg5 hxg5 65.Kh2 Kf3 66.Kg1 Nh3+ 67.Kf1 Nf2 68.Ke1 Nxg4 0-1 

```

## Namesake


* [Nightmare](Nightmare_NL "Nightmare NL") by [Joost Buijs](Joost_Buijs "Joost Buijs")


## Publications


* [Raymond Smullyan](Raymond_Smullyan "Raymond Smullyan") (**1982**). *[An Epistemological Nightmare](http://www.mit.edu/people/dpolicar/writing/prose/text/epistemologicalNightmare.html)*. [MIT](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") <a id="cite-note-5" href="#cite-ref-5">[5]</a>


## External Links


### Chess Engine


* [Nightmare's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=18)


### Misc


* [Nightmare from Wikipedia](https://en.wikipedia.org/wiki/Nightmare)
* [Nightmare (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Nightmare_%28disambiguation%29)
* [Knightmare (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Knightmare_%28disambiguation%29)
* [Artie Shaw](Category:Artie_Shaw "Category:Artie Shaw") - [Nightmare](https://www.jazziz.com/short-history-nightmare-artie-shaw-1936/), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Henry Fuseli](Category:Henry_Fuseli "Category:Henry Fuseli") - The Nightmare, 1781, [Detroit Institute of Arts](https://en.wikipedia.org/wiki/Detroit_Institute_of_Arts), [The Nightmare from Wikipedia](https://en.wikipedia.org/wiki/The_Nightmare)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Nightmare's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=18)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Lyon 1990 - Chess - Round 3 - Game 6 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=60&round=3&id=6)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Jakarta 1996 - Chess - Round 3 - Game 2 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=55&round=3&id=2)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Epistemology from Wikipedia](https://en.wikipedia.org/wiki/Epistemology)

**[Up one level](Engines "Engines")**







 
