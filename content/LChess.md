---
title: LChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* LChess**


**LChess** (L-Chess, Schaakmeester),   

a chess program by [Lex Loep](Lex_Loep "Lex Loep"), which played the [WCCC 1995](WCCC_1995 "WCCC 1995"), the [UPCCC 1994](UPCCC_1994 "UPCCC 1994"), as well as various [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship") and [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments"). LChess was market as *Schaakmeester* in the [Netherlands](https://en.wikipedia.org/wiki/Netherlands), running under [DOS](MS-DOS "MS-DOS") with an own [GUI](GUI "GUI"), and was later ported to natively run under [Windows NT](Windows "Windows") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. In the late 90s, LChess aka *Schaakmeester* for Windows evolved to [ChessPartner](ChessPartner "ChessPartner") <a id="cite-note-2" href="#cite-ref-2">[2]</a> with GUI and an protocol adapter compliant to the [Chess Engine Communication](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") protocols, to support other [WinBoard](Category:WinBoard "Category:WinBoard") and [UCI engines](Category:UCI "Category:UCI") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, market by [Lokasoft](Lokasoft "Lokasoft") and as *Chess Champ* by [Phoenix Games](https://en.wikipedia.org/wiki/Tuna_Technologies) <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### Contents


* [1 Description](#description)
* [2 Selected Games](#selected-games)
* [3 See also](#see-also)
* [4 Forum Posts](#forum-posts)
* [5 External Links](#external-links)
* [6 References](#references)






given in 1995 from the [ICGA](ICGA "ICGA") page <a id="cite-note-5" href="#cite-ref-5">[5]</a>:




```C++
The first version of LChess was written in 1987. In 1988 it participated for the first time in the Dutch Computer Chess Championship, ending 13th in a field of 16; the best result was in 1990 when it ended on a shared 3rd place. Lex Loep has steadily worked on the chess engine and the version which is playing in the WCCC has been ported to Windows NT. Techniques used by the chess engine include [alpha-beta](Alpha-Beta "Alpha-Beta") search, [iterative deepening](Iterative_Deepening "Iterative Deepening"), [PVS](Principal_Variation_Search "Principal Variation Search"), [null moves](Null_Move "Null Move") for [pruning](Null_Move_Pruning "Null Move Pruning") and [thread detection](Null_Move_Pruning#ThreatDetection "Null Move Pruning"), [history tables](History_Heuristic "History Heuristic"), [killer heuristics](Killer_Heuristic "Killer Heuristic"), [transposition tables](Transposition_Table "Transposition Table") and [refutation tables](Refutation_Table "Refutation Table"). Tactically the program plays very well, and is particularly good in finding mate threads. Positionally there is still a lot of work to do. On the Reinfeld test set it scores more than 80% with 1 minute CPU time on a [Pentium 90](X86 "X86"). Search speed is 30,000 - 50,000 [nodes/second](Nodes_per_Second "Nodes per Second"). [Ger Neef](index.php?title=Ger_Neef&action=edit&redlink=1 "Ger Neef (page does not exist)") wrote the user interface. 

```

## Selected Games


[DOCCC 1997](DOCCC_1997 "DOCCC 1997"), round 2, LChess - [Dappet](Dappet "Dappet")




```

[Event "DOCCC 1997"]
[Site "Alphen a/d Rijn NED"]
[Date "1997.11.22"]
[Round "02"]
[White "LChess 4.0"]
[Black "Dappet"]
[Result "1-0"]

1.d3 g6 2.Nf3 Nf6 3.c3 Bg7 4.e4 d5 5.e5 Nfd7 6.d4 f6 7.exf6 exf6 
8.Qe2+ Kf7 9.Qd1 Ke8 10.Bd3 Kf7 11.O-O c5 12.dxc5 Nxc5 13.Bc2 Be6 
14.Nd4 Qd6 15.b4 Ncd7 16.Na3 Na6 17.Nab5 Qb6 18.Bb3 Rae8 19.Nxe6 
Qxb5 20.a4 Qc6 21.Nd8+ Rxd8 22.Bxd5+ 1-0

```

## See also


* [ChessPartner](ChessPartner "ChessPartner")


## Forum Posts


* [How strong is LCHESS 5.3.0.2](http://www.talkchess.com/forum/viewtopic.php?t=22448) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), July 19, 2008


## External Links


* [LChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=193)
* [History of ChessPartner](http://www.lokasoft.nl/history.htm)
* [Download Chess Programs](http://www.top-5000.nl/cp.htm) by [Ed Schröder](Ed_Schroder "Ed Schroder")
* [Chess Champ for Windows (2003) - MobyGames](http://www.mobygames.com/game/windows/chess-champ)


 [Chess Champ Screenshots for Windows - MobyGames](http://www.mobygames.com/game/windows/chess-champ/screenshots/gameShotId,485483/)
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [History of ChessPartner](http://www.lokasoft.nl/history.htm)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [ChessPartner 4.0 available](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ccff9c16b2022c6a) by [Lex Loep](Lex_Loep "Lex Loep"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 9, 1998
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [ChessPartner 6.0](http://www.lokasoft.nl/chesspartner.aspx)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Chess Champ for Windows (2003) - MobyGames](http://www.mobygames.com/game/windows/chess-champ)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [LChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=193)

**[Up one level](Engines "Engines")**







 
