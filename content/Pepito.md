---
title: Pepito
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Pepito**


**Pepito**,  

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") and [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") written by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho") in [C](C "C"), first released in September 2000 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. The recent version comes with an own [GUI](GUI "GUI") written in [C++](Cpp "Cpp") using [wxWidgets](https://en.wikipedia.org/wiki/WxWidgets) and can create [opening book databases](Opening_Book "Opening Book") from a pile of thousands of chess games, applying advanced data structures such as [B-trees](https://en.wikipedia.org/wiki/B-tree) and [skip lists](https://en.wikipedia.org/wiki/Skip_list) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. As [bitboard](Bitboards "Bitboards") engine, Pepito applies [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") with 1/2 MiB lookup tables, indexed by the full [8-bit line occupancy](Occupancy_of_any_Line "Occupancy of any Line"), to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Pepito played the [CCT4](CCT4 "CCT4"), [CCT5](CCT5 "CCT5") and [CCT6](CCT6 "CCT6") tournaments.



## Features


* [NegaScout](NegaScout "NegaScout") search algorithm
* [Extensions](Extensions "Extensions") to avoid [horizon effect](Horizon_Effect "Horizon Effect") (i.e. [check](Check_Extensions "Check Extensions"), [recapture](Recapture_Extensions "Recapture Extensions"), [pawn push](Passed_Pawn_Extensions "Passed Pawn Extensions"), ...)
* [Transposition tables](Transposition_Table "Transposition Table"), [pawn hash tables](Pawn_Hash_Table "Pawn Hash Table") and [evaluation cache](Evaluation_Hash_Table "Evaluation Hash Table")
* [AEL-pruning](AEL-Pruning "AEL-Pruning") à la [Heinz](Ernst_A._Heinz "Ernst A. Heinz")
* [Static exchange evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation"), used for [move ordering](Move_Ordering "Move Ordering") and also to cull losing [captures](Captures "Captures") in the [quiescence search](Quiescence_Search "Quiescence Search")
* [Lazy evaluation](Lazy_Evaluation "Lazy Evaluation")
* [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
* [Pondering](Pondering "Pondering")
* [Book learning](Book_Learning "Book Learning")


## Acknowledgments


Pepito wouldn't have come to life without the help from these guys, acknowledged by Carlos del Cacho in thanx.txt, shipped with the source files <a id="cite-note-4" href="#cite-ref-4">[4]</a>:



* [Bob Hyatt](Robert_Hyatt "Robert Hyatt") ([Crafty](Crafty "Crafty"))
* [Dušan Dobeš](Du%C5%A1an_Dobe%C5%A1 "Dušan Dobeš") ([Phalanx](Phalanx "Phalanx"))
* [Daniel Homan](Daniel_Homan "Daniel Homan") ([EXchess](EXchess "EXchess"))
* [Adrien Regimbald](Adrien_Regimbald "Adrien Regimbald") ([Faile](Faile "Faile"))
* [Jon Dart](Jon_Dart "Jon Dart") ([Arasan](Arasan "Arasan"))
* [Andrew Tridgell](Andrew_Tridgell "Andrew Tridgell") & [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter") ([KnightCap](KnightCap "KnightCap"))
* [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft") & [Chua Kong Sian](Chua_Kong_Sian "Chua Kong Sian") ([GNU Chess 5](GNU_Chess "GNU Chess"))
* [John Stanback](John_Stanback "John Stanback") ([GNU Chess 4](GNU_Chess "GNU Chess"))


... further ...



* [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov") for his [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")


... and 



* [Jonathan Schaeffer](Jonathan_Schaeffer "Jonathan Schaeffer")
* [Alexander Reinefeld](Alexander_Reinefeld "Alexander Reinefeld")
* [Ernst A. Heinz](Ernst_A._Heinz "Ernst A. Heinz")
* [Aske Plaat](Aske_Plaat "Aske Plaat")


for their papers, and 



* [Bruce Moreland](Bruce_Moreland "Bruce Moreland")
* [Dieter Bürßner](Dieter_B%C3%BCr%C3%9Fner "Dieter Bürßner")
* [Brian Richardson](Brian_Richardson "Brian Richardson")
* [Tony Werten](Tony_van_Roon-Werten "Tony van Roon-Werten")


and many others at [CCC](CCC "CCC") for their help...



## Selected Games


[CCT4](CCT4 "CCT4"), round 2, Pepito - [Yace](Yace "Yace") <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```

[Event "CCT4"]
[Site "Internet Chess Club"]
[Date "2002.01.19"]
[Round "2"]
[White "Pepito"]
[Black "Yace"]
[Result "1/2-1/2"]

1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3 e6 7.f3 b5 8.g4 h6 
9.Qd2 Nbd7 10.O-O-O Bb7 11.h4 b4 12.Na4 Qa5 13.b3 Nc5 14.a3 Rc8 15.Qxb4 
Qc7 16.Nxc5 dxc5 17.Qa4+ Nd7 18.Ne2 c4 19.b4 Bc6 20.Qxa6 Ra8 21.Qxc4 Rxa3 
22.Bf4 Qb7 23.c3 Bb5 24.Qd4 Ra2 25.Kb1 Rxe2 26.Rh3 e5 27.Bxe5 Bc5 28.Qd5 
Bc6 29.Qc4 Bb5 30.Qd5 Bc6 31.Qc4 Bb5 32.Qd5 1/2-1/2

```

## Clones


The program [Siboney](index.php?title=Siboney&action=edit&redlink=1 "Siboney (page does not exist)") by [Francisco Rivera](index.php?title=Francisco_Rivera&action=edit&redlink=1 "Francisco Rivera (page does not exist)") published in 2002 was based on Pepito with a changed [evaluation](Evaluation "Evaluation") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>. In 2003, [Deep<9>](Deep9 "Deep9") by pretended author [Denis Grafen](Denis_Grafen "Denis Grafen") was proven a blatant [clone](Category:Clone "Category:Clone") of Pepito <a id="cite-note-9" href="#cite-ref-9">[9]</a> <a id="cite-note-10" href="#cite-ref-10">[10]</a> <a id="cite-note-11" href="#cite-ref-11">[11]</a>.



## Forum Posts


### 2000


* [New winboard engine released!](https://www.stmintz.com/ccc/index.php?id=129855) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [CCC](CCC "CCC"), September 18, 2000
* [Pepito 1.01 uploaded! Bugfix + adjustable hash size](https://www.stmintz.com/ccc/index.php?id=130012) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [CCC](CCC "CCC"), September 20, 2000
* [About Pepito and Amyan](https://www.stmintz.com/ccc/index.php?id=130421) by [José Carlos](Jos%C3%A9_Carlos_Mart%C3%ADnez_Gal%C3%A1n "José Carlos Martínez Galán"), [CCC](CCC "CCC"), September 24, 2000 » [Amyan](Amyan "Amyan")
* [Pepito 1.03 available (Move now support & José C. bug fixed)](https://www.stmintz.com/ccc/index.php?id=130515) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [CCC](CCC "CCC"), September 25, 2000
* [Pepito v1.10 available w source](https://www.stmintz.com/ccc/index.php?id=146024) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [CCC](CCC "CCC"), December 22, 2000


### 2001


* [Pepito 1.40 MMX LCT2 test](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=34671&p=131024) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 02, 2001 » [LCT II](LCT_II "LCT II")
* [Pepito 1.42 MMX build](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=34689&p=131081) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 04, 2001


### 2002


* [The New Pepito...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37894&p=144268) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 24, 2002
* [new Pepito version available for download](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38337&p=146188) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 27, 2002
* [Config.dat for Pepito](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38372&p=146353) by [Carlos Pesce](Carlos_Pesce "Carlos Pesce"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 30, 2002
* [New format of Config.dat for Pepito (built from the readme!)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38378&p=146377) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 30, 2002
* [Pepito 1.55 ( Read for fixes)](https://www.stmintz.com/ccc/index.php?id=243447) by Nolan Denson, [CCC](CCC "CCC"), July 31, 2002
* [Siboney = a Pepito clone ??](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38504&p=146960) by [Brice Boissel](index.php?title=Brice_Boissel&action=edit&redlink=1 "Brice Boissel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 06, 2002 <a id="cite-note-12" href="#cite-ref-12">[12]</a>
* [Pepito 1.54 and learning](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39894&p=152458) by [Igor Korshunov](Igor_Korshunov "Igor Korshunov"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 12, 2002


### 2003


* [Deep<9> Is a Clone based of Pepito? Really?](https://www.stmintz.com/ccc/index.php?id=289182) by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)"), [CCC](CCC "CCC"), March 13, 2003
* [Deep9, Pepito and Leo's Qualify](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41725&p=159242) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 13, 2003


### 2004 ...


* [Pepito @ CCT6 After thoughts](https://www.stmintz.com/ccc/index.php?id=346386) by Nolan Denson, [CCC](CCC "CCC"), February 01, 2004
* [Pepito problem](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46805&p=177043) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 10, 2004
* [Pepito 1.59 Windows 64-bit build available](http://www.talkchess.com/forum/viewtopic.php?t=18466&) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 20, 2007


## External Links


### Chess Engine


* [Pepito Chess engine on Behance](https://www.behance.net/gallery/870970/Pepito-Chess-engine)
* [Pepito... that other xboard chess engine](http://www.quarkchess.de/pepito/) hosted by [Thomas Mayer](Thomas_Mayer "Thomas Mayer")
* [Index of /chess/engines/Norbert's collection/Pepito (Compilation)](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Pepito%20%28Compilation%29/) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Pepito](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Pepito&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [Pepito (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Pepito)
* [Pepito (sandwich) from Wikipedia](https://en.wikipedia.org/wiki/Pepito_(sandwich))
* [Pepe (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Pepe)
* [Pepito (comics) from Wikipedia](https://en.wikipedia.org/wiki/Pepito_%28comics%29)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [New winboard engine released!](https://www.stmintz.com/ccc/index.php?id=129855) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [CCC](CCC "CCC"), September 18, 2000
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Pepito Chess engine on Behance](https://www.behance.net/gallery/870970/Pepito-Chess-engine)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Pepito Chess engine on Behance](http://www.behance.net/gallery/Pepito-Chess-engine/870970)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [thanx.txt](http://kirr.homeunix.org/chess/engines/Norbert%27s%20collection/Pepito%20%28Compilation%29/v1.59/Windows/thanx.txt)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [CCT4 - PGN-Download](http://www.vrichey.de/cct4/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Siboney is at the moment not available!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37440&p=142378) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 24, 2002
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [What is the state of Siboney now?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37909&p=144333) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 26, 2002
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Siboney = a Pepito clone ??](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38504&p=146960) by [Brice Boissel](index.php?title=Brice_Boissel&action=edit&redlink=1 "Brice Boissel (page does not exist)"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 06, 2002
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: A Deep question](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=41578&p=158612) by [Carlos del Cacho](Carlos_del_Cacho "Carlos del Cacho"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 05, 2003
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [The truth about Deep <9>](https://www.stmintz.com/ccc/index.php?id=289305) by [Thomas Mayer](Thomas_Mayer "Thomas Mayer"), [CCC](CCC "CCC"), March 14, 2003
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Information](https://www.stmintz.com/ccc/index.php?id=289424) by [Denis Grafen](Denis_Grafen "Denis Grafen"), [CCC](CCC "CCC"), March 15, 2003
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [What is the state of Siboney now?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=37909&p=144333) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 26, 2002

**[Up one Level](Engines "Engines")**







 
