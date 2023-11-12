---
title: Static Exchange Evaluation
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* Static Exchange Evaluation**



[_MET_DP855300.jpg) [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - Small Worlds IX <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Static Exchange Evaluation (SEE)** examines the consequence of a series of exchanges on a single [square](Squares "Squares") after a given [move](Moves "Moves"), and calculates the likely evaluation change ([material](Material "Material")) to be lost or gained, [Donald Michie](Donald_Michie "Donald Michie") coined the term [swap-off value](SOMA#SwapOff "SOMA"). A positive static exchange indicates a "winning" move. For example, PxQ will always be a win, since the Pawn side can choose to stop the exchange after its Pawn is recaptured, and still be ahead. Some programs optimize the SEE function to only return a losing or equal/winning flag, since they only use SEE to determine if a move is worth searching and do not need the actual value. SEE is useful in [move ordering](Move_Ordering "Move Ordering"), [futility pruning](Futility_Pruning "Futility Pruning") and especially in [quiescence search](Quiescence_Search "Quiescence Search") in conjunction with [delta pruning](Delta_Pruning "Delta Pruning"), as well to [reduce](Reductions "Reductions") "bad" [captures](Captures "Captures") and [checks](Check "Check") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . 



## Seeing a Capture


To statically evaluate a [capture](Captures "Captures"), that particular capture should be forced, because it might not be the lowest attacker that makes the capture, and must not allow the option of standing pat <a id="cite-note-5" href="#cite-ref-5">[5]</a> .




```C++

int seeCapture(int from, int to, int side)
{
   value = 0;
   piece = board[from];

   make_capture(piece, to);
   value = piece_just_captured() - see(to, other(side));
   undo_capture(piece, to);
   return value;
}

```

## SOMA


Instead of using a [quiescence search](Quiescence_Search "Quiescence Search"), some (early) chess programs aimed to determine the material balance of a position by a static analysis of **all** possible capture-move sequences. These routines are often referred to as [SOMA](SOMA#SOMAALGO "SOMA") (**S**wapping **O**ff **M**aterial **A**nalyzer) <a id="cite-note-6" href="#cite-ref-6">[6]</a> based on the [swap-off algorithm](SOMA#SwapOff "SOMA") used in the one-ply analyzing "paper machine" [SOMA](SOMA "SOMA") by [evolutionary biologist](https://en.wikipedia.org/wiki/Evolutionary_biologist) [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), the **S**mith **O**ne-**M**ove **A**nalyzer designed in the early 60s <a id="cite-note-7" href="#cite-ref-7">[7]</a> .



## See also


* [Negamax](Negamax "Negamax")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Delta Pruning](Delta_Pruning "Delta Pruning")
* [Guard Heuristic](Guard_Heuristic "Guard Heuristic")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [MVV-LVA](MVV-LVA "MVV-LVA")
* [Ed's Lookup](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps") from [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
* [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") with [Bitboards](Bitboards "Bitboards")
* [SOMA](SOMA "SOMA")


 [Swap-off algorithm](SOMA#Swapoff "SOMA")
* [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")


## Publications


* [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), [Donald Michie](Donald_Michie "Donald Michie") (**1961**). *Machines that play games*. [New Scientist](https://en.wikipedia.org/wiki/New_Scientist), 12, 367-9. [google books](http://books.google.com/books?id=lo7r0zX_T0sC&lpg=PA369&dq=Machines%20that%20play%20games.%201961%2C%20New%20Scientist%2C%2012&pg=PA367#v=onepage&q&f=false) » [SOMA](SOMA "SOMA")
* [Donald Michie](Donald_Michie "Donald Michie") (**1966**). *Game Playing and Game Learning Automata.* Advances in Programming and Non-Numerical Computation, [Leslie Fox](https://en.wikipedia.org/wiki/Leslie_Fox) (ed.), pp. 183-200. Oxford, Pergamon. » Includes Appendix: *Rules of SOMAC* by [John Maynard Smith](John_Maynard_Smith "John Maynard Smith") <a id="cite-note-8" href="#cite-ref-8">[8]</a>
* [Donald Michie](Donald_Michie "Donald Michie") (**1974**). *On Machine Intelligence*. Edinburgh: University Press, ISBN 10: 085224262X, ISBN 13: 9780852242629, [abebooks.com](http://www.abebooks.com/servlet/SearchResults?isbn=085224262X), [alibris.com](http://www.alibris.com/search/books/qwork/4836304/used/On%20machine%20intelligence), [biblio.com](http://www.biblio.com/isbn/9780852242629.html)
* [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *[An Exchange Evaluator for Computer Chess](https://archive.org/stream/byte-magazine-1978-11/1978_11_BYTE_03-11_The_Sky_is_the_Limit#page/n17/mode/2up)*. [BYTE, Vol. 3, No. 11](Byte_Magazine#BYTE311 "Byte Magazine") <a id="cite-note-9" href="#cite-ref-9">[9]</a>
* [David Levy](David_Levy "David Levy") (**1979**). *Chess Programming - Before You Begin*. [Personal Computer World](Personal_Computer_World "Personal Computer World"), May 1979
* [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2000**). *SUPER-SOMA - Solving Tactical Exchanges in Shogi without Tree Searching*. Lecture Notes In Computer Science; Vol. 2063, [CG 2000](CG_2000 "CG 2000"), [Word preprint](http://www.aifactory.co.uk/downloads/SUPER-SOMA.doc)<a id="cite-note-10" href="#cite-ref-10">[10]</a>
* [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2002**). *Computer Shogi*. Artificial Intelligence, Vol. 134, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.130.2727)
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. Thesis, Chapter 4, Static Exchange Evaluation, [pdf](http://www.personeel.unimaas.nl/uiterwijk/Theses/PhD/Reul_thesis.pdf)
* [Fritz Reul](Fritz_Reul "Fritz Reul") (**2010**). *Static Exchange Evaluation with αβ-Approach*. [ICGA Journal, Vol. 33, No. 1](ICGA_Journal#33_1 "ICGA Journal")


## Forum Posts


### 1990 ...


* [efficient algorithm for safety of pieces](http://groups.google.com/group/rec.games.chess/browse_frm/thread/638ca70e88930bb4) by [Deniz Yuret](Deniz_Yuret "Deniz Yuret"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 18, 1993
* [Computer Chess: swap down evaluators vs capture search](http://groups.google.com/group/rec.games.chess/browse_frm/thread/dd1c55ecc9f48717) by [Jon Dart](Jon_Dart "Jon Dart"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), October 24, 1994


### 1995 ...


* [mvv/lva vs SEE capture ordering test results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1fa5e36362f5dde4) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 10, 1995
* [MVV/LVA vs SEE move ordering - more test results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/645f44f84102e450) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 25, 1995


 [Re: MVV/LVA vs SEE move ordering - more test results](http://groups.google.com/group/rec.games.chess.computer/msg/1951744da404fc33) by [Brian Sheppard](Brian_Sheppard "Brian Sheppard"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 27, 1995
* [MVV/LVA and SEE - what do they mean?](https://groups.google.com/d/msg/rec.games.chess.computer/5byhl_6Jmc8/D1QAR146VLIJ) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 28, 1995 » [MVV/LVA](MVV-LVA "MVV-LVA")
* [Quiescence vs swapoff](https://www.stmintz.com/ccc/index.php?id=17016) by [Peter Fendrich](Peter_Fendrich "Peter Fendrich"), [CCC](CCC "CCC"), April 15, 1998
* [Question about static exchange evaluation](https://www.stmintz.com/ccc/index.php?id=32703) by Larry Coon, [CCC](CCC "CCC"), November 12, 1998
* [Help with Static Exchange Evaluator](https://www.stmintz.com/ccc/index.php?id=60880) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), July 18, 1999
* [SEE for forward pruning in Q. Search](https://www.stmintz.com/ccc/index.php?id=63511) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 04, 1999 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [SEE for forward pruning in the Q. search - I'm confused!](https://www.stmintz.com/ccc/index.php?id=64357) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), August 11, 1999


### 2000 ...


* [Re: Explain SEE (static exchange evaluator)?](https://www.stmintz.com/ccc/index.php?id=134986) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), October 25, 2000
* [Qsearch problems...(about sorting and SEE)](https://www.stmintz.com/ccc/index.php?id=141230) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 26, 2000 » [Quiescence Search](Quiescence_Search "Quiescence Search")
* [MVV/LVA or SEE - liability?](https://www.stmintz.com/ccc/index.php?id=141813) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 29, 2000 » [MVV-LVA](MVV-LVA "MVV-LVA")


**2001**



* [About SEE](https://www.stmintz.com/ccc/index.php?id=147977) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 04, 2001
* [Should an engine using SEE beat another not using it?](https://www.stmintz.com/ccc/index.php?id=152256) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), January 27, 2001
* [SEE and possible EXChess bug](https://www.stmintz.com/ccc/index.php?id=161209) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), April 01, 2001 » [EXchess](EXchess "EXchess") <a id="cite-note-11" href="#cite-ref-11">[11]</a>
* [Static Exchange Eval (SEE)](https://www.stmintz.com/ccc/index.php?id=179023) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), July 10, 2001
* [Static Exchange Eval](https://www.stmintz.com/ccc/index.php?id=178979) by [Artem Pyatakov](Artem_Petakov "Artem Petakov"), [CCC](CCC "CCC"), August 02, 2001
* [I want to SEE](https://www.stmintz.com/ccc/index.php?id=202931) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), December 21, 2001


 [Re: I want to SEE](https://www.stmintz.com/ccc/index.php?id=202933) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), December 21, 2001
**2002**



* [Value of King in SEE](https://www.stmintz.com/ccc/index.php?id=206056) by [David Rasmussen](David_Rasmussen "David Rasmussen"), [CCC](CCC "CCC"), January 07, 2002
* [Static exchange evaluator and 0x88](https://www.stmintz.com/ccc/index.php?id=262577) by Pierre Bokma, [CCC](CCC "CCC"), October 30, 2002


**2003**



* [Static Exchange Evaluation (SEE) for pruning in quiescence (?)](https://www.stmintz.com/ccc/index.php?id=311899) by [Omid David](Eli_David "Eli David"), [CCC](CCC "CCC"), August 19, 2003
* [table-based SEE or "evaluation in rebel (hanging pieces)"](https://www.stmintz.com/ccc/index.php?id=330947) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), November 27, 2003 » [Hanging Piece](Hanging_Piece "Hanging Piece"), [Rebel](Rebel "Rebel")


**2004**



* [A SIMD idea, eg. Piece/Gain of a capture target](https://www.stmintz.com/ccc/index.php?id=343790) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 21, 2004
* [SEE and FH-%](https://www.stmintz.com/ccc/index.php?id=357382) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), March 30, 2004
* [SEE results](https://www.stmintz.com/ccc/index.php?id=381606) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), August 10, 2004
* [SEE and pin detection](https://www.stmintz.com/ccc/index.php?id=385126) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), August 30, 2004 » [Pin](Pin "Pin")
* [Pin aware SEE](https://www.stmintz.com/ccc/index.php?id=390108) by [Dan Honeycutt](Dan_Honeycutt "Dan Honeycutt"), [CCC](CCC "CCC"), October 03, 2004


### 2005 ...


* [Help on how to implement move ordering with a Static Exchange Evaluator](https://www.stmintz.com/ccc/index.php?id=410423) by Carlos Magno, [CCC](CCC "CCC"), February 09, 2005
* [Static Exchange Evaluation Methods](http://www.open-aurec.com/wbforum/viewtopic.php?t=1961) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 14, 2005


**2007**



* [SEE with magic bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?t=6104) by [Pradu Kannan](Pradu_Kannan "Pradu Kannan"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 24, 2007 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [SEE on non-capture moves in main search](http://www.talkchess.com/forum/viewtopic.php?t=12706) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 28, 2007 » [Move Ordering](Move_Ordering "Move Ordering")
* [How good is your SEE?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=6421) by [mjlef](Mark_Lefler "Mark Lefler"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 24, 2007
* [Re: Movei added to Crafty vs Rybka comparison data](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=123511&t=14168) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), June 06, 2007
* [SEE algorithm](http://www.talkchess.com/forum/viewtopic.php?t=18163) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), December 02, 2007


**2008**



* [SEE problem](http://www.talkchess.com/forum/viewtopic.php?t=20646) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 13, 2008
* [How is SEE used?](http://www.talkchess.com/forum/viewtopic.php?t=24357) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), October 13, 2008


**2009**



* [SEE Observation](http://www.talkchess.com/forum/viewtopic.php?t=29216) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), August 02, 2009 » [Tinker](Tinker "Tinker")
* [SEE algorithm on chessprogramming wiki](http://www.talkchess.com/forum/viewtopic.php?t=30905) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), December 02, 2009


### 2010 ...


* [SEE Improvement Idea](http://www.talkchess.com/forum/viewtopic.php?t=31464) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), January 04, 2010
* [GetSmallestAttacker() in 16x12 board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=31776) by metax, [CCC](CCC "CCC"), January 17, 2010 » [Piece-Lists](Piece-Lists "Piece-Lists")


**2011**



* [Using SEE to prune in main search](http://www.talkchess.com/forum/viewtopic.php?t=37514) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), January 08, 2011 » [Pruning](Pruning "Pruning"), [Reductions](Reductions "Reductions")
* [Simple question about SEE](http://www.talkchess.com/forum/viewtopic.php?t=37582) by [Andres Valverde](Andres_Valverde "Andres Valverde"), [CCC](CCC "CCC"), January 12, 2011
* [Implementing SEE](http://www.talkchess.com/forum/viewtopic.php?t=40046) by colin, [CCC](CCC "CCC"), Aug 12, 2011
* [SEE with alpha beta](http://www.talkchess.com/forum/viewtopic.php?t=40054) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), August 14, 2011 » [Onno](Onno "Onno")
* [Reducing/Pruning Bad Captures (SEE < 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 19, 2011 » [Reductions](Reductions "Reductions"), [Pruning](Pruning "Pruning")
* [question about SEE](http://www.talkchess.com/forum/viewtopic.php?t=40283) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), September 05, 2011


**2013**



* [SEE](http://www.talkchess.com/forum/viewtopic.php?t=47330) by [Rasjid Chan](Rasjid_Chan "Rasjid Chan"), [CCC](CCC "CCC"), February 25, 2013
* [Static Exchange Evaluation...](http://www.talkchess.com/forum/viewtopic.php?t=48609) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), July 10, 2013 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [SEE() is slow and SEE() is fast](http://www.talkchess.com/forum/viewtopic.php?t=48899) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 09, 2013


**2014**



* [SEE](http://www.talkchess.com/forum/viewtopic.php?t=51272) by [Richard Delorme](Richard_Delorme "Richard Delorme"), [CCC](CCC "CCC"), February 13, 2014
* [SEE logic](http://www.talkchess.com/forum/viewtopic.php?t=51518) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), March 08, 2014 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")


### 2015 ...


* [SEE Map](http://www.talkchess.com/forum/viewtopic.php?t=57045) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), July 20, 2015 <a id="cite-note-13" href="#cite-ref-13">[13]</a>
* [Magic SEE](http://www.talkchess.com/forum/viewtopic.php?t=57548) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 07, 2015
* [Problems with SEE](http://www.talkchess.com/forum/viewtopic.php?t=64166) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), June 03, 2017
* [Evasion (capture) moves ordering by See](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64827) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), August 06, 2017
* [see](http://www.talkchess.com/forum/viewtopic.php?t=65836) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), November 28, 2017
* [Poor man's SEE](http://www.talkchess.com/forum/viewtopic.php?t=65982) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 11, 2017
* [Fast SEE (Ed's lookup revisited)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69301) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 17, 2018 » [Ed's lookup](Attack_and_Defend_Maps#EDsLookup "Attack and Defend Maps")


### 2020 ...


* [SEE versus SEE\_GE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72862) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), January 21, 2020
* [SEE (Static Exchange Evaluation) pruning nodes](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76750) by [Marcel Vanthoor](Marcel_Vanthoor "Marcel Vanthoor"), [CCC](CCC "CCC"), March 01, 2021
* [Static exchange evaluation with promotion](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77787) by Guido Flohr, [CCC](CCC "CCC"), July 23, 2021
* [Static Exchange Evaluation without bitboards](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78477) by Jonathan McDermid, [CCC](CCC "CCC"), October 22, 2021
* [Move ordering using SEE](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79077) by Christian Dean, [CCC](CCC "CCC"), January 08, 2022
* [Request for thoughts: SEE "Test Set"](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79936) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), May 24, 2022


## External Links


* [SEE](https://web.archive.org/web/20071027170528/http://www.brucemo.com/compchess/programming/quiescent.htm#SEE) from [Bruce Moreland's Programming Topics](https://web.archive.org/web/20071026090003/http://www.brucemo.com/compchess/programming/index.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
* [Static exchange evaluation (SEE)](http://mediocrechess.blogspot.com/2007/03/guide-static-exchange-evaluation-see.html) from [Mediocre Chess](http://mediocrechess.varten.org/index.html) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson")
* [Static Exchange Evaluation in Chess](http://www.chessprogramming.net/computerchess/static-exchange-evaluation-in-chess/) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [Chess Programming Blog](http://www.chessprogramming.net/), July 9, 2013
* [Wolfgang Schmid](Category:Wolfgang_Schmid "Category:Wolfgang Schmid") - Ringading Dang, [Special Kick](https://play.google.com/store/music/album?id=B4j7q7gplpdq4ibqno2twclf7si&tid=song-Trie7zbkahun3mi7yaz4hynimze&hl=en) (2002), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Joo Kraus](Category:Joo_Kraus "Category:Joo Kraus"), [Libor Shima](https://de.wikipedia.org/wiki/Libor_%C5%A0%C3%ADma), [Peter Wölpl](https://de.wikipedia.org/wiki/Peter_W%C3%B6lpl), [Marco Minnemann](Category:Marco_Minnemann "Category:Marco Minnemann")
 
  




### Test suites


* [<https://github.com/jdart1/arasan-chess/blob/master/src/unit.cpp> unit.cpp by [Jon Dart](Jon_Dart "Jon Dart")
* [<https://github.com/lithander/Leorik/blob/master/Leorik.Test/see.epd> see.epd by [Thomas Jahn](Thomas_Jahn "Thomas Jahn")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Wassily Kandinsky](Category:Wassily_Kandinsky "Category:Wassily Kandinsky") - [Small Worlds IX](https://commons.wikimedia.org/wiki/File:Kleine_Welten_IX_(Small_Worlds_IX)_MET_DP855300.jpg?uselang=en), 1922, [Metropolitan Museum of Art](https://en.wikipedia.org/wiki/Metropolitan_Museum_of_Art)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Reducing/Pruning Bad Captures (SEE < 0)](http://www.talkchess.com/forum/viewtopic.php?t=40100) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), August 19, 2011
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [SEE algorithm on chessprogramming wiki](http://www.talkchess.com/forum/viewtopic.php?t=30905) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), December 02, 2009
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: SEE algorithm on chessprogramming wiki](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=310782&t=30905) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 20, 2009
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Simple question about SEE](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=387694&t=37582) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 12, 2011
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida"), [Makoto Sakuta](Makoto_Sakuta "Makoto Sakuta"), [Jeff Rollason](Jeff_Rollason "Jeff Rollason") (**2002**). *Computer Shogi*. Artificial Intelligence, Vol. 134, [Elsevier](https://en.wikipedia.org/wiki/Elsevier), [CiteSeerX](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.130.2727)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [John Maynard Smith](John_Maynard_Smith "John Maynard Smith"), [Donald Michie](Donald_Michie "Donald Michie") (**1961**). *Machines that play games*. [New Scientist](https://en.wikipedia.org/wiki/New_Scientist), 12, 367-9. [google books](http://books.google.com/books?id=lo7r0zX_T0sC&lpg=PA369&dq=Machines%20that%20play%20games.%201961%2C%20New%20Scientist%2C%2012&pg=PA367#v=onepage&q&f=false)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> see [Swap-off](Helmut_Richter#Swapoff "Helmut Richter") by [Helmut Richter](Helmut_Richter "Helmut Richter")
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Sargon Z80 assembly listing](http://www.andreadrian.de/schach/sargon.asm) by [Dan](Dan_Spracklen "Dan Spracklen") and [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen"), hosted by [Andre Adrian](Andre_Adrian "Andre Adrian"), see XCHNG
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Looking for Alternatives to Quiescence Search](http://www.aifactory.co.uk/newsletter/2006_03_quiescence_alts.htm) by [Jeff Rollason](Jeff_Rollason "Jeff Rollason"), [AI Factory](AI_Factory "AI Factory"), December 2006
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [EXchess v4.02 released](https://www.stmintz.com/ccc/index.php?id=162704) by [Daniel Homan](Daniel_Homan "Daniel Homan"), [CCC](CCC "CCC"), April 10, 2001
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Static Exchange Evaluation in Chess](http://www.chessprogramming.net/computerchess/static-exchange-evaluation-in-chess/) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [Chess Programming Blog](http://www.chessprogramming.net/), July 9, 2013
13. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Russell M. Church](index.php?title=Russell_M._Church&action=edit&redlink=1 "Russell M. Church (page does not exist)"), [Kenneth W. Church](Kenneth_W._Church "Kenneth W. Church") (**1977**). *Plans, Goals, and Search Strategies for the Selection of a Move in Chess*. [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine")

**[Up one level](Move_Ordering "Move Ordering")**







 
