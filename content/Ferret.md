---
title: Ferret
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Ferret**

\[ [Ferret](https://en.wikipedia.org/wiki/Ferret) [dentition](https://en.wikipedia.org/wiki/Dentition) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ferret** ,

a chess engine by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"). Ferret won the Amateur World Microcomputer Chess Champion Title in [Paderborn 1995](WMCCC_1995 "WMCCC 1995") and was two times winner of the World Microcomputer Speed-Chess Champion, in [Jakarta 1996](WMCCC_1996 "WMCCC 1996") and [Paris 1997](WMCCC_1997 "WMCCC 1997"). Ferret became runner up at the [14th World Microcomputer Chess Championship](WMCCC_1996 "WMCCC 1996"), Jakarta 1996 without losing a game. At the [9th World Computer Chess Championship](WCCC_1999 "WCCC 1999"), Paderborn 1999, Ferret was unlucky in not winning a dramatical playoff against [Shredder](Shredder "Shredder").

## Photos & Games

[](File:FerretShredder1999.JPG)
[WCCC 1999](WCCC_1999 "WCCC 1999"), Round 6: Ferret - [Shredder](Shredder "Shredder"), [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") and [Bruce Moreland](Bruce_Moreland "Bruce Moreland") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>

```

[Event "WCCC 1999"]
[Site "Paderborn, Germany"]
[Date "1999.06.18"]
[Round "6"]
[White "Ferret"]
[Black "Shredder"]
[Result "1/2-1/2"]

1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 exd4 7.O-O Nge7 8. cxd4 d5 
9.exd5 Nxd5 10.Ba3 Be6 11.Bb5 Bb4 12.Bxc6+ bxc6 13.Bxb4 Nxb4 14.Qa4 Qd6 15.Nc3 
Nd3 16.d5 Nc5 17.Qxc6+ Qxc6 18.dxc6 Ke7 19.Rfe1 Nd3 20.Re3 Nb4 21.Nd4 Rhd8 22.Rd1 
Kf6 23.a3 Nd5 24.Ne4+ Ke7 25.Ree1 Bg4 26.f3 Bc8 27.Nc5+ Kf6 28.Nb5 Be6 29.Na6 Rac8 
30.Nbxc7 h5 31.h3 h4 32.a4 Nxc7 33.Rxd8 Rxd8 34.Nxc7 Rc8 35.Nxe6 fxe6 36.Rc1 e5 
37.Kf2 Ke6 38.g3 hxg3+ 39.Kxg3 Kd6 40.Rd1+ Ke6 41.Rd7 Rxc6 42.Rxg7 Rc3 43.Rg4 Kf5 
44.h4 Rc1 45.h5 Rc6 46.Rg7 Ra6 47.Rg4 Rc6 48.Rg7 Ra6 49.Rg8 Rb6 50.Kh4 Rb4+ 51.Kg3
Rb6 52.Kh4 Rb4+ 53.Rg4 Rb2 54.Kg3 Rb6 55.a5 Rd6 56.Rg7 Ra6 57.Rg8 Rd6 58.Kh4 Rd4+ 
59.Kg3 Rd6 60.Rb8 Kg5 61.Re8 Rd5 62.a6 Ra5 63.Re7 e4 64.Rxa7 Ra3 65.Kf2 Rxf3+ 
66.Ke2 Kxh5 67.Ra8 Rf7 68.Ke3 Re7 69.Rb8 Kg6 70.Rb6+ Kf5 1/2-1/2

```

## Board Representation

Quote by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") <a id="cite-note-4" href="#cite-ref-4">[4]</a>:

```C++
Ferret's [board representation](Board_Representation "Board Representation") is an [array](Array "Array") of 64 squares. Each element is pretty big. [Move generation](Move_Generation "Move Generation") is accomplished by use of a [move table](Table-driven_Move_Generation#Ferret "Table-driven Move Generation"), much expanded from [the system](Table-driven_Move_Generation#GNUChess "Table-driven Move Generation") used in [GNU Chess](GNU_Chess "GNU Chess").

```

## Descriptions

## By Bruce Moreland

Description of Ferret from Bruce Moreland's site <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

```C++
Ferret is a "normal" chess program. By that I mean that it uses alpha-beta full-width search, a quiescent search, a transposition hash table, an evaluation function that is called at the tips, and so forth. It uses [null-move forward pruning](Null_Move_Pruning "Null Move Pruning"), and for that I am indebted to [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), who did not invent this technique, but he made it accessible to the amateur community via an [ICCA](ICCA "ICCA") Journal article (Vol. 16 #3, September 1993). 

```

```C++
The program uses numerous common [extensions](Extensions "Extensions") such as [check extension](Check_Extensions "Check Extensions"), [recapture extension](Recapture_Extensions "Recapture Extensions"), and [single-response](One_Reply_Extensions "One Reply Extensions") to check. It also uses a sort of [singular-extension](Singular_Extensions "Singular Extensions") that is loosely based upon the extension of this name that appears in [Deep Thought](Deep_Thought "Deep Thought") and presumably [Deep Blue](Deep_Blue "Deep Blue"). The [evaluation function](Evaluation_Function "Evaluation Function") is designed to catch common features without being slow, but it's slow enough that the program isn't particularly fast.

```

```C++
The program uses [endgame databases](Endgame_Tablebases "Endgame Tablebases") of my own design and construction, but which aren't any better than the [Nalimov](Eugene_Nalimov "Eugene Nalimov"), [Edwards](Steven_Edwards "Steven Edwards"), or [Thompson](Ken_Thompson "Ken Thompson") endgame databases. I wrote my own because I didn't want to take advantage of code written by others, since I felt that the program would be less mine if I did so. The program has a series of special case low-material evaluation functions that it uses when endgame databases are not present, and in some cases when they are. The program is written 100% in [C](C "C"), and is portable to any platform that runs any Windows-based operating system, including multiprocessor machines. 

```

## 1995

Description given in **1995** from the [ICCA](ICCA "ICCA") site <a id="cite-note-6" href="#cite-ref-6">[6]</a> :

```C++
Ferret is a "normal" [brute-force](Brute-Force "Brute-Force") program that runs under [Windows NT](Windows "Windows"). Techniques and tools used by the program include [alpha-beta pruning](Alpha-Beta "Alpha-Beta"), selective [search extensions](Extensions "Extensions"), [quiescence search](Quiescence_Search "Quiescence Search") limited by a [static exchange evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation"), [null-move forward pruning](Null_Move_Pruning "Null Move Pruning"), a 50,000-positions [opening book](Opening_Book "Opening Book"), several [hash tables](Hash_Table "Hash Table") and a few simple endgame databases. The program consists of about 20,000 lines of [C](C "C") code and has been compiled using [Microsoft](Microsoft "Microsoft") [Visual C++](https://en.wikipedia.org/wiki/Visual_C%2B%2B) 2.0. Ferret searches approximately 18,000-32,000 [nodes per second](Nodes_per_Second "Nodes per Second") on a [Pentium](https://en.wikipedia.org/wiki/Pentium) 66. It was written during off-hours over a period of about 4 years, for fun. Ferret finished fifth in [Don Beal's](Don_Beal "Don Beal") [uniform platform tournament](UPCCC_1994 "UPCCC 1994") last September. It has also played several hundred games of blitz chess on the [Internet Chess Server](Chess_Server "Chess Server"), where it has been shown to be competitive among strong human players and various commercial programs. Ferret is copyrighted but its author is not particularly secretive about the program as he feels indebted to the many people who have answered his own questions. 

```

## 1997

Description given in **1997** from the [ICCA](ICCA "ICCA") site:

```C++
Ferret is a normal chess program. It uses [null-move forward pruning](Null_Move_Pruning "Null Move Pruning") and other standard techniques. It is a leaf-node evaluator, and searches 80- 350K [nps](Nodes_per_Second "Nodes per Second") (120K typical middlegame) on a [Pentium Pro](https://en.wikipedia.org/wiki/Pentium_Pro) 200 mhz machine. 

```

## GNU Chess?

The quote of [Monty Newborn](Monroe_Newborn "Monroe Newborn") in *Beyond Deep Blue* <a id="cite-note-7" href="#cite-ref-7">[7]</a>, pg. 29 <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```C++
Ferret was a derivative of Moreland’s open source engine GNU Chess. 

```

is not correct, neither was [GNU Chess](GNU_Chess "GNU Chess") a program by Bruce Moreland, nor was Ferret a derivative of GNU Chess <a id="cite-note-9" href="#cite-ref-9">[9]</a>:

```C++
The program is 100% original, although at the time I started I had access to the Gnuchess source code. That code was kind of messy and it was its messy state that inspired me to think that I could do better. 

```

## See also

- [Gerbil](Gerbil "Gerbil")
- [Table-driven Move Generation](Table-driven_Move_Generation#Ferret "Table-driven Move Generation") in Ferret
- [Table-driven Move Generation](Table-driven_Move_Generation#GNUChess "Table-driven Move Generation") in [GNU Chess](GNU_Chess "GNU Chess")

## Forum Posts

- [Repetition detection w/hash tables](http://groups.google.com/group/rec.games.chess/browse_frm/thread/8cc6428ab611f70e) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rec.games.chess](Computer_Chess_Forums "Computer Chess Forums"), August 14, 1993 » [Repetitions](Repetitions "Repetitions"), [Transposition Table](Transposition_Table "Transposition Table")
- [Re: Quiescence search problems (solved)](http://groups.google.com/group/rec.games.chess.computer/msg/ea740f0cc65c5f59?hl=en) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 06, 1996 » [Quiescence Search](Quiescence_Search "Quiescence Search"), [Move Ordering](Move_Ordering "Move Ordering")
- [Ferret info](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/bd0eed64397a131b) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), September 26, 1997
- [Re: Ferret/Gerbil question](https://www.stmintz.com/ccc/index.php?id=189800) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), September 21, 2001 » [Gerbil](Gerbil "Gerbil")
- [Ferret 1.00 v258 - program from 1995](http://www.talkchess.com/forum/viewtopic.php?t=49533) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), October 01, 2013

## External Links

## Chess Engine

- [Ferret](http://web.archive.org/web/20070607231238/www.brucemo.com/compchess/ferret/index.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland") archived by the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)
- [Ferret's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=35)
- [The chess games of Ferret (Computer)](http://chessgames.com/player/ferret) from [chessgames.com](http://www.chessgames.com/)

## Misc

- [Ferret (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ferret_%28disambiguation%29)
- [Ferret search library from Wikipedia](https://en.wikipedia.org/wiki/Ferret_search_library), a [Ruby](index.php?title=Ruby&action=edit&redlink=1 "Ruby (page does not exist)") search library
- [Ferret Data Visualization and Analysis from Wikipedia](https://en.wikipedia.org/wiki/Ferret_Data_Visualization_and_Analysis)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> A picture of a ferret's teeth, very white and in good condition, [Ferret from Wikipedia](https://en.wikipedia.org/wiki/Ferret)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> Image captured from [Paderborn 1999 1.mp4](http://www.top-5000.nl/Paderborn_1999_1.mp4) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Paderborn 1999 - Chess - Round 6 - Game 3 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=8&round=6&id=3)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: Ferret/Gerbil question](https://www.stmintz.com/ccc/index.php?id=189800) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), September 21, 2001
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Ferret's Description](http://web.archive.org/web/20070825223426/www.brucemo.com/compchess/ferret/desc.htm) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland")
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Ferret's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=35)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Monty Newborn](Monroe_Newborn "Monroe Newborn") (**2011**). *[Beyond Deep Blue: Chess in the Stratosphere](http://www.springer.com/computer/general+issues/book/978-0-85729-340-4)*. [Springer](https://en.wikipedia.org/wiki/Springer_Science%2BBusiness_Media), ISBN-13: 978-0857293404, [amazon](http://www.amazon.com/Beyond-Deep-Blue-Chess-Stratosphere/dp/0857293400)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Download Sample pages 2 (pdf, 3.2 MB)](http://www.springer.com/cda/content/document/cda_downloaddocument/9780857293404-c2.pdf?SGWID=0-0-45-1117438-p174097071)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [The chess games of Ferret (Computer)](http://chessgames.com/player/ferret) from [chessgames.com](http://www.chessgames.com/)

**[Up one Level](Engines "Engines")**

