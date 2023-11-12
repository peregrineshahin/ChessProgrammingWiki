---
title: IsiChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* IsiChess**



 [](2D_Graphics_Board#Drawing "2D Graphics Board#Drawing") [IsiChess' Knight](2D_Graphics_Board#Drawing "2D Graphics Board") 
**IsiChess**,  

a commercial [DOS](MS-DOS "MS-DOS") chess program by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), distributed exclusively by [Martin Stamer's](Martin_Stamer "Martin Stamer") EuroChess Zentrale from 1994 until 1997. 
It had an own [GUI](GUI "GUI"), and was able to play simultaneously with up to ten board windows. While the GUI was written with [Borland](https://en.wikipedia.org/wiki/Borland) [C++](Cpp "Cpp"), the engine was written in [80386](X86 "X86") 32-bit [assembly](Assembly "Assembly"), applying a kind of [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking) using a [coroutine](https://en.wikipedia.org/wiki/Coroutine). 
In a special mode, IsiChess switched to the so called [unreal mode](https://en.wikipedia.org/wiki/Unreal_mode) to allocate more physical [memory](Memory "Memory") for [transposition tables](Transposition_Table "Transposition Table"), the DOS operating system was aware of.
The private [Windows](Windows "Windows") version, developed since 2000, was a complete rewrite influenced by [Robert Hyatt's](Robert_Hyatt "Robert Hyatt") [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards") paper <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
In the following years IsiChess evolved to a pure [fill based](Fill_Algorithms "Fill Algorithms") approach, motivated by the ideas of [Steffan Westcott](Steffan_Westcott "Steffan Westcott"). The [multi-treaded](Thread "Thread") [search](Search "Search") used a [shared](Shared_Hash_Table "Shared Hash Table") [transposition table](Transposition_Table "Transposition Table").



### MS-DOS


### Multiple Boards


 [](File:IsiChessDos.jpg) 
Commercial [MS-DOS](MS-DOS "MS-DOS") IsiChess [GUI](GUI "GUI") <a id="cite-note-2" href="#cite-ref-2">[2]</a>



### Book Editor


 [](File:IsiChessBook.jpg) 
IsiChess [Opening Book](Opening_Book "Opening Book") Editor, with variants [transposing](Transposition "Transposition") to the current position,  
 
listbox of possible lines and [ECO](ECO "ECO") code, where the current move follows up by a tree control



### Windows


 [](File:IsiChess_MMX.jpg) 
Private IsiChess MMX Windows GUI



## Descriptions


from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-3" href="#cite-ref-3">[3]</a>:



### 1999



```C++
In 1991 I started to write my first [C++](Cpp "Cpp") Project, a Class-Lib for a [DOS](MS-DOS "MS-DOS")-Window-Manager-Interface. Inspired from [David Levy's](David_Levy "David Levy") [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") (specially the article about [Chess 4.5](Chess_(Program) "Chess (Program)")), I started to write a chess-algorithm in bottom-up manner (beginning with data structures like [piece-sets](Piece-Sets "Piece-Sets") and [bitboards](Bitboards "Bitboards") and fast [assembler](Assembly "Assembly") routines to modify them). Two [incremental updated](Incremental_Updates "Incremental Updates") redundant sets PIECESET _ControlledBy[64] for each square and BITBOARD _ControllTo[32] for each piece are used for move generation and evaluation purposes. The Search is a standard [alpha-beta](Alpha-Beta "Alpha-Beta") [Null-window search](Principal_Variation_Search "Principal Variation Search") with [Iterative Deepening](Iterative_Deepening "Iterative Deepening") and several threat extensions and [Null move](Null_Move_Pruning "Null Move Pruning"). Standard Heuristics like [Killer](Killer_Heuristic "Killer Heuristic") and [History](History_Heuristic "History Heuristic") are used. The Leaf-[Evaluation](Evaluation "Evaluation") performs several tasks like extension-detection ([King danger](King_Safety "King Safety"), [passed pawns](Passed_Pawn "Passed Pawn") ) and several [Mate in one detections](Mate_at_a_Glance "Mate at a Glance"). With my own C++ Class-library an implementation of a [graphical user interface](GUI "GUI") for the chess program was an quite easy task - IsiChess was born. Special Feature is the ability to play simultaneously with up to ten chessboards in separate windows. 


```

### 2007



```C++
[Bitboard](Bitboards "Bitboards") engine based on MMX-flood-fills. Conventional [alpha-beta](Alpha-Beta "Alpha-Beta") searcher ([PVS](Principal_Variation_Search "Principal Variation Search")), [adaptive nullmove](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning") with [zugzwang verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"), sophisticated [extension](Extensions "Extensions") and [reduction](Reductions "Reductions") code as well as [evaluation](Evaluation "Evaluation"), [static mate detection](Mate_at_a_Glance "Mate at a Glance"). Own [GUI](GUI "GUI"). Own [opening book](Opening_Book "Opening Book") format (ASCII readable) - all lines manually edited over the years. 

```

## Tournaments


From 1994 until its last occurrence in 1997 Dos-IsiChess participated four times at the [Aegon Man-Machine Tournaments](Aegon_Tournaments "Aegon Tournaments") in [The Hague](https://en.wikipedia.org/wiki/The_Hague), [The Netherlands](https://en.wikipedia.org/wiki/Netherlands). 
Gerd Isenberg had the pleasure to operate IsiChess to play the IGMs [John Nunn](John_Nunn "John Nunn"), [Larry Christiansen](https://en.wikipedia.org/wiki/Larry_Christiansen), [Lembit Oll](https://en.wikipedia.org/wiki/Lembit_Oll), [Hans Ree](https://en.wikipedia.org/wiki/Hans_Ree) and [Friso Nijboer](http://nl.wikipedia.org/wiki/Friso_Nijboer). 
IsiChess, until 1999 the [DOS](MS-DOS "MS-DOS")-Program, participated at various [World-](World_Computer_Chess_Championship "World Computer Chess Championship") and [World Microcomputer Chess Championships](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), best result was 7th from 18 in 2002 and 6 out of 11 in 2004.





|  Event
 |  Site
 |  Standing
 |  Points
 |
| --- | --- | --- | --- |
| [WMCCC 1995](WMCCC_1995 "WMCCC 1995") | [Paderborn](https://en.wikipedia.org/wiki/Paderborn) |  17 / 34
 |  5½ / 11
 |
| [WMCCC 1996](WMCCC_1996 "WMCCC 1996") | [Jakarta](https://en.wikipedia.org/wiki/Jakarta) |  16 / 27
 |  5½ / 11
 |
| [WMCCC 1997](WMCCC_1997 "WMCCC 1997") | [Paris](https://en.wikipedia.org/wiki/Paris) |  20 / 34
 |  5½ / 11
 |
| [WCCC 1999](WCCC_1999 "WCCC 1999") | [Paderborn](https://en.wikipedia.org/wiki/Paderborn) |  19 / 30
 |  3 / 7
 |
| [WMCCC 2001](WMCCC_2001 "WMCCC 2001") | [Maastricht](https://en.wikipedia.org/wiki/Maastricht) |  14 / 18
 |  3½ / 9
 |
| [WCCC 2002](WCCC_2002 "WCCC 2002") | [Maastricht](https://en.wikipedia.org/wiki/Maastricht) |  7 / 18
 |  4½ / 9
 |
| [WCCC 2004](WCCC_2004 "WCCC 2004") | [Ramat-Gan](https://en.wikipedia.org/wiki/Ramat_Gan) |  9 / 14
 |  6 / 11
 |
| [WCCC 2005](WCCC_2005 "WCCC 2005") | [Reykjavík](https://en.wikipedia.org/wiki/Reykjav%C3%ADk) |  10 / 12
 |  2½ / 11
 |
| [WCCC 2006](WCCC_2006 "WCCC 2006") | [Turin](https://en.wikipedia.org/wiki/Turin) |  10 / 18
 |  5½ / 11
 |
| [WCCC 2007](WCCC_2007 "WCCC 2007") | [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam) |  10 / 12
 |  3½ / 11
 |


Since 1994 IsiChess played the [International Paderborn Computer Chess Championships](IPCCC "IPCCC"), since 2001 the [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and the [International CSVN Tournament](International_CSVN_Tournament "International CSVN Tournament"). 



## Photos & Games


### WCCC 2004


 [](File:IsiFritz2004.JPG) 
[WCCC 2004](WCCC_2004 "WCCC 2004"): [Frans Morsch](Frans_Morsch "Frans Morsch"), [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), IsiChess - [Fritz](Fritz "Fritz")




```

[Event "WCCC 2004"]
[Site "Ramat-Gan, Israel"]
[Date "2004.07.05"]
[Round "2"]
[White "IsiChess"]
[Black "Fritz"]
[Result "1/2-1/2"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 O-O 5.a3 Bxc3+ 6.Qxc3 b6 7.Nf3 Bb7 8.e3 d6 9.b4 Nbd7 10.Bb2 Ne4 
11.Qc2 f5 12.Bd3 a5 13.O-O Ng5 14.Ne1 Qe8 15.f3 Qg6 16.Be2 e5 17.c5 dxc5 18.bxc5 e4 19.cxb6 Nxb6 
20.Qxc7 Bd5 21.Bc1 f4 22.exf4 Nh3+ 23.Kh1 Rae8 24.Qc3 exf3 25.Bxf3 Bc4 26.Bd5+ Bxd5 27.Qxh3 Rf6 
28.Be3 Nc4 29.Bg1 Nd2 30.Rf2 Ne4 31.Rf3 Qf7 32.Qg4 Rg6 33.Qh5 Nf6 34.Qf5 Rxg2 35.Kxg2 Re2+ 36.Kf1 
Bxf3 37.Rc1 Bg4 38.Rc8+ Re8 39.Rxe8+ Qxe8 40.Qe5 Qa8 41.f5 a4 42.Qe6+ Kh8 43.Be3 Qh1+ 44.Bg1 Bh3+ 
45.Kf2 Qa8 46.Kg3 Nh5+ 47.Kf2 Qf8 48.Qc6 Bxf5 49.Ke2 Nf6 50.Qxa4 h6 51.Qb3 Qc8 52.Bf2 Be6 53.Qb2 
Qc4+ 54.Kd2 Bf5 55.Bg3 Ne4+ 56.Ke3 Nc3 57.Qd2 Qb3 58.Kf3 Ne4+ 59.Qe3 Ng5+ 60.Kf2 Nh3+ 61.Kf3 Bg4+ 
62.Ke4 Qf7 63.Kd3 Ng5  64.Kc3 Qa2 65.Kb4 Qb2+ 66.Ka5 Bd7 67.Qd3 Ne4 68.Be5 Nd2 69.a4 Qa2 70.Kb6 
Qe6+ 71.Ka7 Nc4 72.Qb3 Bc8 73.Qb5 Qf7+ 74.Kb8 Bd7 75.Qc5 Bxa4 76.Nd3 Kh7 77.Qc7 Bd7 78.Nc5 Qf8+ 
79.Ka7 Bh3 80.Ne4 Be6 81.Ka6 Ne3 82.Nd6 Qa8+ 83.Kb5 Qg2 84.Qb7 Bd5 85.Qd7 Qg6 86.Ka5 h5 87.h4 Bg8 
88.Qb7 Qg1 89.Qe4+ Kh8 90.Kb6 Nd5+ 91.Kb7 Qc1 92.Bxg7+ Kxg7 93.Qe5+ Kh7 94.Qxh5+ Qh6 95.Qf5+ Kh8 
96.Qe5+ Kh7 97.Qf5+ Kg7 98.Ne8+ Kh8 99.Qe5+ Kh7 100.Qe4+ Kh8 101.Qe5+ Kh7 102.Qf5+ Kh8 103.Qe5+ 
1/2-1/2

```

### WCCC 2005


 [](File:PeterGerdWCCC2005.jpg) 
[WCCC 2005](WCCC_2005 "WCCC 2005"): [Peter Berger](Peter_Berger "Peter Berger"), [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [Crafty](Crafty "Crafty") - IsiChess




```

[Event "WCCC 2005"]
[Site "Reykjavík, Iceland"]
[Date "2005.08.21"]
[Round "11"]
[White "Crafty"]
[Black "IsiChess"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.Bb5+ Nc6 4.O-O Bd7 5.Re1 Nf6 6.c3 a6 7.Bf1 Bg4 8.d3 e5 9.h3 Bxf3 10.Qxf3 Be7 
11.g3 O-O 12.a4 Qd7 13.Na3 b5 14.Be3 Rfb8 15.Bg2 Na5 16.axb5 Nb3 17.Rab1 axb5 18.Qd1 Qe6 19.f4 
Na5 20.d4 cxd4 21.cxd4 b4 22.d5 Qd7 23.Nc2 b3 24.Na1 Qa4 25.fxe5 dxe5 26.Qd3 Nc4 27.Kh2 Nxe3 
28.Qxe3 Qa2 29.Qf2 Bd8 30.Qf5 Bc7 31.Kh1 h6 32.Rf1 Ra7 33.Qf3 Bd6 34.Qe2 Bc5 35.h4 Ne8 36.g4 Nd6 
37.g5 hxg5 38.hxg5 g6 39.Kh2 Ra4 40.Rbc1 Bd4 41.Rc6 Qxb2 42.Qxb2 Bxb2 43.Nxb3 Nxe4 44.Bxe4 Rxe4 
45.Nc5 Re3 46.d6 Bd4 47.Rf2 Rc3 48.d7 Rxc5 49.Rxc5 Bxc5 50.Rc2 Rd8 51.Rxc5 Rxd7 52.Rxe5 Rd3 
53.Kg2 f5 54.gxf6 Kf7 55.Re7+ Kxf6 56.Re8 1/2-1/2

```

### WCCC 2006


 [](File:ErosGerd2006.jpg) 
[WCCC 2006](WCCC_2006 "WCCC 2006"): [Eros Riccio](Eros_Riccio "Eros Riccio"), [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [Diep](Diep "Diep") - IsiChess <a id="cite-note-4" href="#cite-ref-4">[4]</a>




```

[Event "WCCC 2006"]
[Site "Turin, Italy"]
[Date "2006.05.26"]
[Round "3"]
[White "Diep"]
[Black "IsiChess"]
[Result "1-0"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e6 7.f3 Be7 8.Qd2 O-O 9.O-O-O Nc6 10.g4 Rb8 
11.h4 Nxd4 12.Bxd4 b5 13.Kb1 Nd7 14.h5 h6 15.g5 Bxg5 16.f4 Bf6 17.Bxf6 Nxf6 18.e5 Ne8 19.Rg1 Qb6 
20.Bd3 Kh8 21.Ne4 Rg8 22.Nxd6 Nxd6 23.exd6 Qxd6 24.Qe3 Qc7 25.Qe4 f5 26.Qe3 Bd7 27.Rg6 Be8 28.Rxe6 
Bxh5 29.Rh1 Rge8 30.Bxf5 Rbd8 31.Bd3 Rxe6 32.Qxe6 Qxf4 33.Qxa6 Qd2 34.Qe6 Re8 35.Rf1 Qb4 36.a3 Rxe6 
37.axb4 g5 38.Bxb5 Bg6 39.Bd7 Re2 40.Rc1 h5 41.b5 Rd2 42.Bc6 Kg7 43.b6 Rd8 44.b7 g4 45.Rf1 Kh6 
46.Rf6 Kg7 47.Rd6 Rb8 48.Rd5 Be8 49.Rg5+ Kf7 50.Bxe8+ Rxe8 51.Kc1 Rb8 52.Rxh5 Kf6 53.Rb5 g3 54.Rb3 
g2 55.Rg3 Rxb7 56.Rxg2 Ke5 1-0

```

## See also


* [2D Graphics Board](2D_Graphics_Board#IsiChess "2D Graphics Board")
* [2D Vector Graphics](2D_Graphics_Board#Drawing "2D Graphics Board")
* [Figurine Algebraic Notation - Vector Graphics](Algebraic_Chess_Notation#Vector_Graphics "Algebraic Chess Notation")
* [HansDamf](index.php?title=HansDamf&action=edit&redlink=1 "HansDamf (page does not exist)")


## Forum Posts


### 1999


* [WCCC 99 Zugzwang - Isichess "1/2 - 1/2" Round 1](https://www.stmintz.com/ccc/index.php?id=55668) by Jose Hernandez, [CCC](CCC "CCC"), June 14, 1999


### 2000 ...


* [Static Mate Detection](https://www.stmintz.com/ccc/index.php?id=209201) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 22, 2002 » [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
* [Crafty-IsiChess,CCT4,r11 ==> A move to avoid?](https://www.stmintz.com/ccc/index.php?id=210702) by [José Antônio Fabiano Mendes](Jos%C3%A9_Ant%C3%B4nio_Fabiano_Mendes "José Antônio Fabiano Mendes"), [CCC](CCC "CCC"), January 29, 2002
* [Congratulations to IsiChess](https://www.stmintz.com/ccc/index.php?id=264834) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), November 13, 2002
* [Rebel - IsiChess: Some notes](https://www.stmintz.com/ccc/index.php?id=322544) by [Jeroen Noomen](Jeroen_Noomen "Jeroen Noomen"), [CCC](CCC "CCC"), October 20, 2003
* [CSNV Leiden : Hydra vs IsiChess (1) draw (commented game)](https://www.stmintz.com/ccc/index.php?id=361328) by [Kurt Utzinger](Kurt_Utzinger "Kurt Utzinger"), [CCC](CCC "CCC"), April 23, 2004
* [IsiChess-Fritz unbalanced](https://www.stmintz.com/ccc/index.php?id=374114) by [Ingo Althöfer](Ingo_Alth%C3%B6fer "Ingo Althöfer"), [CCC](CCC "CCC"), July 05, 2004 » [WCCC 2004](WCCC_2004 "WCCC 2004")
* [Isichess-Junior (+diagram)](https://www.stmintz.com/ccc/index.php?id=375077)] by [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten"), [CCC](CCC "CCC"), July 09, 2004
* [WCCC04 acknowledgements](https://www.stmintz.com/ccc/index.php?id=377326) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), July 16, 2004 » [WCCC 2004](WCCC_2004 "WCCC 2004")


### 2005 ...


* [TCB-IsiChess 1-0](https://www.stmintz.com/ccc/index.php?id=441905) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 14, 2005 » [WCCC 2005](WCCC_2005 "WCCC 2005")
* [Fruit-IsiChess](https://www.stmintz.com/ccc/index.php?id=442290) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), August 15, 2005
* [Zappa-Isichess](https://www.stmintz.com/ccc/index.php?id=443322) by [Anthony Cozzie](Anthony_Cozzie "Anthony Cozzie"), [CCC](CCC "CCC"), August 19, 2005
* [IsiChess - Deep Junior](https://www.stmintz.com/ccc/index.php?id=443519) by [Andreas Guettinger](Andreas_Guettinger "Andreas Guettinger"), [CCC](CCC "CCC"), August 20, 2005
* [Test position: Crafty-IsiChess](https://www.stmintz.com/ccc/index.php?id=443909) by Janos Keinrath, [CCC](CCC "CCC"), August 21, 2005


### 2010 ...


* [Re: Your first chess program](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=43381&start=5) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), April 20, 2012
* [Re: Mate at a glance](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=56457&start=1) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), May 23, 2015


## External Links


### Chess Program


* [IsiChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=17)
* [IsiChess' chess games](https://www.chessgames.com/perl/ezsearch.pl?search=IsiChess+%28Computer%29) from [chessgames.com](http://www.chessgames.com/index.html)
* [Aegon Man-Machine Tournaments](http://old.csvn.nl/aegonhist.html)


### Misc


* [Jerry Bergonzi](Category:Jerry_Bergonzi "Category:Jerry Bergonzi") - Simultaneous Looks, [Tenorist](https://www.discogs.com/de/Jerry-Bergonzi-Tenorist/release/5936774) (2007), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [John Abercrombie](Category:John_Abercrombie "Category:John Abercrombie"), [Dave Santoro](https://www.discogs.com/de/artist/2226028-Dave-Santoro), [Adam Nussbaum](Category:Adam_Nussbaum "Category:Adam Nussbaum")
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Robert Hyatt](Robert_Hyatt "Robert Hyatt") (**1999**). *Rotated Bitmaps, a New Twist on an Old Idea*. [ICCA Journal, Vol. 22, No. 4](ICGA_Journal#22_4 "ICGA Journal")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> Image photographed from an advertisement
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [IsiChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=17)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> Photo by [Alessandro Scotti](Alessandro_Scotti "Alessandro Scotti")

**[Up one level](Engines "Engines")**







 
