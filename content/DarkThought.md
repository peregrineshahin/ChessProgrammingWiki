---
title: DarkThought
---
**[Home](Home "Home") * [Engines](Engines "Engines") * DarkThought**

\[ [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Composition, 1911 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**DarkThought** (Dark Thought),

a chess program by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch") and [Markus Gille](Markus_Gille "Markus Gille") from the [University of Karlsruhe](https://en.wikipedia.org/wiki/Karlsruhe_Institute_of_Technology/). The development of DarkThought started in 1993, when Heinz and Gillgasch founded a computer-chess group to write a chess program using [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . In 1994, Markus Gille joined the team <a id="cite-note-3" href="#cite-ref-3">[3]</a> , and Peter Gillgasch left the DarkThought team in April 1996 <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Descriptions

from the [ICGA](ICGA "ICGA") page <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## 1995

```C++
Dark Thought is a [brute-force](Brute-Force "Brute-Force") program employing sophisticated [move ordering techniques](Move_Ordering "Move Ordering") and [search extensions](Extensions "Extensions") backed by a selective [quiescence search](Quiescence_Search "Quiescence Search"). On a [DEC 3000-600](DEC_Alpha#3000 "DEC Alpha") (175Mhz [Alpha 21064 CPU](DEC_Alpha "DEC Alpha"), 64MB [RAM](Memory#RAM "Memory")) Dark Thought visits up to 60,000 [nodes per second](Nodes_per_Second "Nodes per Second") and reaches a non-selective, brute-force search [depth](Depth "Depth") of at least 8 [plies](Ply "Ply") in 1 minute. Its [opening book](Opening_Book "Opening Book") contains 250,000 positions. On-line access to [Thompson's endgame databases](Thompson%27s_Databases "Thompson's Databases") is handled by a greatly enhanced version of the public domain software by Beuckens and Hoekstra. Peter Gillgasch, the main brain behind the chess engine, wrote a prototype version of Dark Thought in [Pascal](Pascal "Pascal") in 1992.

```

```C++
Today the program compiles and runs from the same [ANSI C](C "C") source files on a variety of platforms. Markus Gille and Ernst Heinz are responsible for fine-tuning the [evaluation](Evaluation "Evaluation") function and databases and Peter Gillagasch still maintains the chess engine. During the [World Championships](WCCC_1995 "WCCC 1995"), Darkthought will run on the most powerful DEC Alpha workstation available. 

```

## 1997

```C++
DarkThought is a [bitboard-based](Bitboards "Bitboards") chess program developed at the University of Karlsruhe that has successfully participated in all [world championships](World_Computer_Chess_Championship "World Computer Chess Championship") since 1995. On a 500MHz [DEC Alpha-21164a](DEC_Alpha#21164 "DEC Alpha") with 128MB RAM, DarkThought routinely reaches speeds of 200K nps in the middlegame while peaking at over 650K nps in the endgame.

```

```C++
DarkThought is a sophisticated [alpha-beta](Alpha-Beta "Alpha-Beta") searcher written in ANSI-C that uses [PVS/NegaScout](Principal_Variation_Search "Principal Variation Search") with state-of-the-art enhancements like [futility pruning](Futility_Pruning "Futility Pruning"), [internal iterative deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), dynamic move ordering ([killer](Killer_Heuristic "Killer Heuristic")+[history heuristic](History_Heuristic "History Heuristic")), [recursive](Recursion "Recursion") [null move pruning](Null_Move_Pruning "Null Move Pruning"), selective extensions, [interior-node recognizers](Interior_Node_Recognizer "Interior Node Recognizer"), and interior-node [endgame database](Endgame_Tablebases "Endgame Tablebases") access. 

```

## 1999

```C++
DarkThought is a full-blown 64-bit chess program based on the bitboard technology. It was developed at the Institute for Program Structures and Data Organization (University of Karlsruhe, Germany) and has successfully participated in all [ICCA](ICCA "ICCA") world championships since 1995. On a 767MHz KryoTech [Alpha-21164a](DEC_Alpha#21164 "DEC Alpha") with 256MB RAM, DarkThought easily reaches speeds of 350K nps in the middle game while peaking at over 1M nps in the endgame.

```

```C++
DarkThought is a sophisticated alpha-beta searcher written in ANSI-C that uses PVS/NegaScout with state-of-the-art enhancements like various [hash tables](Hash_Table "Hash Table"), [normal](Futility_Pruning "Futility Pruning") and [extended futility pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning"), internal iterative deepening, dynamic move ordering (history+killer heuristic), recursive null-move pruning, selective extensions, and interior-node recognizers (incl. access to endgame databases). 

```

## Photos & Games

## WCCC 1995

[](File:DarkThoughtTeam1995.jpg)
[WCCC 1995](WCCC_1995 "WCCC 1995") DarkThought team [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [Markus Gille](Markus_Gille "Markus Gille") and [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch") playing [Virtua Chess](Virtua_Chess "Virtua Chess") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

```

[Event "WCCC 1995"]
[Site "Shatin, Hong Kong - China"]
[Date "1995.05.27"]
[Round "3"]
[White "Dark Thought"]
[Black "Virtua Chess"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Bd3 Nc6 6.Ne2 d5 7.cxd5 exd5 8.a3 Bd6 9.Nb5 Be7
10.O-O Re8 11.f3 a6 12.Nbc3 Bd6 13.Bc2 Qe7 14.e4 dxe4 15.fxe4 Bg4 16.Be3 Rad8 17.Qe1
Bxe2 18.Qxe2 Nxd4 19.Bxd4 Bxh2+ 20.Kxh2 Rxd4 21.Kh1 Qd6 22.Rad1 c5 23.Qf3 Re5 24.Kg1
Qe6 25.Qg3 Qd6 26.Rf5 Rxd1+ 27.Nxd1 Qd4+ 28.Ne3 Re8 29.Rf2 Qe5 30.Qxe5 Rxe5 31.Nc4 Re6
32.e5 Nd7 33.Rd2 Nf8 34.Bf5 Re7 35.Rd8 h5 36.Bc8 g6 37.Nd6 Rxe5 38.Bxb7 Re2 39.Nc4 Kg7
40.Bxa6 Ne6 41.Rd2 Re4 42.Nd6 Re1+ 43.Kf2 Rc1 44.Bc4 Ng5 45.Bd5 Kf8 46.Kg3 f6 47.a4 Ke7
48.Nb7 Nf7 49.a5 Ne5 50.a6 c4 51.a7 Ra1 52.Nd6 Kxd6 53.a8=Q Rxa8 54.Bxa8+ Kc5 55.Rd5+
Kb4 56.Rd6 f5 57.Re6 Nd3 58.Rxg6 f4+ 59.Kh4 Nxb2 60.Rf6 Kc3 61.Rxf4 1-0

```

## Aegon 1997

[](http://www.thorstenczub.de/aegon.html)
[Aegon 1997](Aegon_1997 "Aegon 1997"), [Sofia Polgar](https://en.wikipedia.org/wiki/Sofia_Polgar) vs. DarkThought operated by [Markus Gille](Markus_Gille "Markus Gille"), [Yona Kosashvili](https://en.wikipedia.org/wiki/Yona_Kosashvili) and

[Karsten Bauermeister](Karsten_Bauermeister "Karsten Bauermeister") watching <a id="cite-note-8" href="#cite-ref-8">[8]</a> <a id="cite-note-9" href="#cite-ref-9">[9]</a>

```

[Event "12th AEGON Man-Mach"]
[Site "The Hague NED"]
[Date "1997.04.21"]
[Round "04"]
[White "Sofia Polgar"]
[Black "DarkThought"]
[Result "0-1"]

1.c4 c6 2.b3 Nf6 3.Bb2 e6 4.Nf3 d5 5.e3 Bb4 6.a3 Be7 7.Qc2 O-O 8.Nc3 Re8 9.d4 Nbd7
10.Be2 Nf8 11.O-O Ng6 12.Rfe1 Bd6 13.e4 dxe4 14.Nxe4 Nf4 15.Bf1 Nxe4 16.Qxe4 Bc7
17.Rad1 Bd7 18.g3 Nh5 19.Ne5 Nf6 20.Qc2 Re7 21.Bg2 Rc8 22.Ba1 Kh8 23.Qb2 Be8 24.f4
Ba5 25.Rf1 Qd6 26.Kh1 Bc7 27.g4 Rb8 28.g5 Nh5 29.Qe2 f6 30.b4 a5 31.Bc3 Qd8 32.gxf6
gxf6 33.d5 exd5 34.cxd5 Rg7 35.Ng4 axb4 36.axb4 Bd7 37.dxc6 bxc6 38.f5 Qf8 39.Bf3
c5 40.Qb2 Rb6 41.Rg1 cxb4 42.Bd4 Bc6 43.Bxc6 Rxc6 44.Qg2 Rc4 45.Qa2 b3 46.Qa1 Rc2
47.Rd3 Qe8 48.Qd1 Qe4+ 0-1

```

## See also

- [Demonology](Category:Demonology "Category:Demonology")
- [Thought](Category:Thought "Category:Thought")

## Publications

- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess](http://people.csail.mit.edu/heinz/dt/node2.html).* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1998**). *[DarkThought Goes Deep](http://people.csail.mit.edu/heinz/dt/node46.html).* [ICCA Journal, Vol. 21, No. 4](ICGA_Journal#21_4 "ICGA Journal")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1999**). *[Scalable Search in Computer Chess](http://people.csail.mit.edu/heinz/node1.html#scale-cchess)*. [Morgan Kaufmann](https://en.wikipedia.org/wiki/Morgan_Kaufmann), [Vieweg-Verlag](https://de.wikipedia.org/wiki/Vieweg_Verlag), [Springer Link](https://link.springer.com/book/10.1007/978-3-322-90178-1) <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>

[](https://link.springer.com/book/10.1007/978-3-322-90178-1)

- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Modeling the “Go Deep” Behaviour of CRAFTY and DARK THOUGHT.* [Advances in Computer Games 9](Advances_in_Computer_Games_9 "Advances in Computer Games 9")
- [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**2001**). *Selected Goodies of DarkThought*. Invited Lecture, [6th Computer Olympiad Workshop](6th_Computer_Olympiad#Workshop "6th Computer Olympiad"), [ppt](https://ilk.uvt.nl/icga/news/Olympiad/Olympiad/workshop/InvitedLecture-Heinz.ppt)

## Forum Posts

- [Drawn games (Was Re: Transposition table)](http://groups.google.com/group/rec.games.chess.computer/msg/b8bdef757df5d5c9) by [Peter Gillgasch](Peter_Gillgasch "Peter Gillgasch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 06, 1996
- [Uniform Platform Match "DarkThought" vs. "XXXX II"](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/41bd04ab11cc7c85) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 15, 1998
- [Uniform Platform Match "DarkThought" vs. "XXXX II"](https://www.stmintz.com/ccc/index.php?id=14123) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), January 15, 1998 » [XXXX](XXXX "XXXX")
- [Re: Darkthought](https://www.stmintz.com/ccc/index.php?id=58575) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), June 29, 1999 » [WCCC 1999](WCCC_1999 "WCCC 1999")
- [ANN: Updated WWW Pages of "DarkThought"](https://www.stmintz.com/ccc/index.php?id=83268) by [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz"), [CCC](CCC "CCC"), December 18, 1999
- [DarkThought: keeps all 3/4-piece endgame databases in RAM](https://www.stmintz.com/ccc/index.php?id=197637) by [Wylie Garvin](index.php?title=Wylie_Garvin&action=edit&redlink=1 "Wylie Garvin (page does not exist)"), [CCC](CCC "CCC"), November 16, 2001
- [DarkThought sorts MVV/LVA without looking at any moves?](http://www.talkchess.com/forum/viewtopic.php?t=56114) by Rob Williamson, [CCC](CCC "CCC"), April 25, 2015 » [MVV-LVA](MVV-LVA "MVV-LVA")

## External Links

## Chess Program

- [DarkThought's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=15)
- [WWW Pages of DarkThought](http://people.csail.mit.edu/heinz/dt/)

## Misc

- [Van der Graaf Generator](Category:Van_der_Graaf_Generator "Category:Van der Graaf Generator") - [Darkness](https://en.wikipedia.org/wiki/The_Least_We_Can_Do_Is_Wave_to_Each_Other) ([BBC Top Gear](<https://en.wikipedia.org/wiki/Top_Gear_(radio_show)>), 1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [«Композиция 5».jpg](https://commons.wikimedia.org/wiki/File:%C2%AB%D0%9A%D0%BE%D0%BC%D0%BF%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D1%8F_5%C2%BB.jpg)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Rotated Bitboards](http://people.csail.mit.edu/heinz/dt/node8.html) from [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz") (**1997**). *[How DarkThought Plays Chess.](http://people.csail.mit.edu/heinz/dt/node2.html)* [ICCA Journal, Vol. 20, No. 3](ICGA_Journal#20_3 "ICGA Journal")
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Ernst A. Heinz - Professional Experience](http://people.csail.mit.edu/heinz/node10.html)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [DarkThought - Acknowledgements](http://people.csail.mit.edu/heinz/dt/node1.html#acknlg)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Dark Thought's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=15)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> Image clipped from [ICCA Journal, Vol. 18, No. 3](ICGA_Journal#18_3 "ICGA Journal"), pp. 178, Photo courtesy by [Jaap van den Herik](Jaap_van_den_Herik "Jaap van den Herik")
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Shatin 1995 - Chess - Round 3 - Game 1 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=29&round=3&id=1)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Aegon 1996-97](http://www.thorstenczub.de/aegon.html) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [CSVN Downloads Games Aegon Tournaments](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=40&Itemid=26&lang=en)
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Dap Hartmann](Dap_Hartmann "Dap Hartmann") (**2000**). *[The Importance of being Scalable](http://ilk.uvt.nl/icga/journal/contents/content23-1.htm#THE%20IMPORTANCE%20OF%20BEING%20SCALABLE)*. [ICGA Journal, Vol. 23, No. 1](ICGA_Journal#23_1 "ICGA Journal"), Review
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**2000**). *Die Wissenschaft kehrt zurück - Computerschach-Forschung und das Buch von Ernst Heinz*. [CSS](Computerschach_und_Spiele "Computerschach und Spiele") 2/00, [pdf](http://www.mustrum.de/chrilly/heinz.pdf) (German)

**[Up one level](Engines "Engines")**

