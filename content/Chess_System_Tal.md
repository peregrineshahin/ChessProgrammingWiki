---
title: Chess System Tal
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chess System Tal**

**Chess System Tal** (Complete Chess System 2 - TAL, CSTal, AI Factory Chess Tal),

a commercial chess program developed by [Chris Whittington](Chris_Whittington "Chris Whittington") in the mid 90s as successor of the [Complete Chess System](Complete_Chess_System "Complete Chess System"), marketed through his company [Oxford Softworks](Oxford_Softworks "Oxford Softworks"). The first version was a [MS-DOS](MS-DOS "MS-DOS") program, **Chess System Tal II**, released in 1999 ran under [Windows](Windows "Windows"). Chess System Tal is famous for its entertaining, strong human playing style with focus on [King attacks](King_Safety "King Safety") and speculative [sacrifices](Sacrifice "Sacrifice"), resembling that of the former World Champion [Mikhail Tal](https://en.wikipedia.org/wiki/Mikhail_Tal). Chess System Tal II was further marketed by [Ubisoft](index.php?title=Ubisoft&action=edit&redlink=1 "Ubisoft (page does not exist)") <a id="cite-note-1" href="#cite-ref-1">[1]</a> and continued by [Jeff Rollason's](Jeff_Rollason "Jeff Rollason") [AI Factory](AI_Factory "AI Factory") <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a>, who now own the rights on the CSTal sources <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Contents

- [1 Chess System Tal with NNUE](#chess-system-tal-with-nnue)
- [2 Tournament Play](#tournament-play)
- [3 Photos](#photos)
- [4 Selected Games](#selected-games)
- [5 Description](#description)
- [6 See also](#see-also)
  - [6.1 Engines](#engines)
  - [6.2 People](#people)
- [7 Forum Posts](#forum-posts)
  - [7.1 1996 ...](#1996-...)
  - [7.2 2000 ...](#2000-...)
  - [7.3 2005 ...](#2005-...)
  - [7.4 2010 ...](#2010-...)
  - [7.5 2020 ...](#2020-...)
- [8 External Links](#external-links)
- [9 References](#references)

## Chess System Tal with NNUE

[Chess System Tal 2.00](https://github.com/ChrisWhittington/Chess-System-Tal-NNUE-2), released in June 2023 as [UCI](UCI "UCI") compliant public available and private source engine is developed by [Chris Whittington](Chris_Whittington "Chris Whittington") and [Ed Schroder](Ed_Schroder "Ed Schroder") and was specifically designed to play in style of the legendary Tal. It comes in two flavors, one for Elo (strength) and the other for Tal-like play (EAS).

## Tournament Play

CSTal played two [World Microcomputer Chess Championships](World_Microcomputer_Chess_Championship "World Microcomputer Chess Championship"), the [WMCCC 1995](WMCCC_1995 "WMCCC 1995"), the [WMCCC 1997](WMCCC_1997 "WMCCC 1997"), and three [Aegon Tournaments](Aegon_Tournaments "Aegon Tournaments"), [Aegon 1995](Aegon_1995 "Aegon 1995"), [Aegon 1996](Aegon_1996 "Aegon 1996") and [Aegon 1997](Aegon_1997 "Aegon 1997") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Photos

[](http://www.thorstenczub.de/aegon.html)
Chess System Tal at [Aegon 1996](Aegon_1996 "Aegon 1996") operated by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## Selected Games

[WMCCC 1995](WMCCC_1995 "WMCCC 1995"), round 4, [Chess Genius](Chess_Genius "Chess Genius") - Chess System Tal <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```

[Event "WMCCC 1995"]
[Site "Paderborn, Germany"]
[Date "1995.10.11"]
[Round "4"]
[White "Chess Genius"]
[Black "Chess System Tal"]
[Result "0-1"]

1.c4 e5 2.Nc3 Nf6 3.Nf3 Nc6 4.g3 d5 5.cxd5 Nxd5 6.Bg2 Nb6 7.O-O Be7 8.a3 O-O 
9.b4 Re8 10.Rb1 Bf8 11.d3 a5 12.b5 Nd4 13.Nd2 Rb8 14.e3 Ne6 15.Nf3 Ng5 16.Nxg5 
Qxg5 17.Ne4 Qd8 18.Qc2 Bg4 19.f4 exf4 20.Rxf4 Be6 21.Rf2 f5 22.Nc3 Bf7 23.Ne2 
Qd7 24.Qc3 Nd5 25.Bxd5 Qxd5 26.Nd4 Re5 27.Qxc7 Ra8 28.Qc3 Rae8 29.Nf3 Rxe3 
30.Bxe3 Rxe3 31.Nd4 g6 32.Re2 Bc5 33.Rxe3 Bxd4 34.Qc8+ Kg7 35.Re1 f4 36.gxf4 
Qf3 37.Qc7 Bxe3+ 38.Rxe3 Qxe3+ 39.Kg2 Qe2+ 40.Kg1 Qxd3 41.Qxb7 Qxa3 42.b6 Qc5+ 
43.Kf1 a4 44.Qc7 Qxc7 45.bxc7 Be6 46.h4 a3 0-1 

```

## Description

given in 1997 from the [ICGA](ICGA "ICGA") tournament site <a id="cite-note-9" href="#cite-ref-9">[9]</a> :

```C++
CSTal is designed to play in the romantic and dangerous style of Michael Tal, famous for his daring and aggressive style of play.

```

```C++
Programmer Chris Whittington has developed a radically different approach to chess programming, concentrating on speculative chess knowledge within the [evaluation function](Evaluation_Function "Evaluation Function"); and the use of [forward pruning](Pruning "Pruning") techniques which rely on this evaluation function knowledge.

```

```C++
One effect of using a high knowledge-based approach is that CSTal operates at a [nodes per second](Nodes_per_Second "Nodes per Second") rate much less than programs with simple evaluation functions. The risks and benefits of this strategy are obvious; on the one side CSTal is able to steer games towards tactical king-attack complexities, and to execute stunning sacrifices. On the other side the disparity in effective search depth means that state of the art search programs will have the advantage if the position does not contain factors where CSTal's knowledge is able to give it the edge.

```

```C++
CSTal's computer-computer games are often very exciting and double-edged, with the result in doubt until the end. It is capable of causing serious upsets to top programs, but also of being seriously upset itself.

```

```C++
In a materialistic world, in the materialistic world of computer chess, Chess System Tal offers the alternative pathway of idealism. 

```

## See also

## Engines

- [Chess Player 2150](Chess_Player_2150 "Chess Player 2150")
- [Chess Simulator](Chess_Simulator "Chess Simulator")
- [Complete Chess System](Complete_Chess_System "Complete Chess System")

## People

- [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
- [Jeff Rollason](Jeff_Rollason "Jeff Rollason")
- [Chris Whittington](Chris_Whittington "Chris Whittington")
- [Ed Schroder](Ed_Schroder "Ed Schroder")

## Forum Posts

## 1996 ...

- [Chess System Tal beta testers](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e32a20ebb61e20f9) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 22, 1996
- [ICCA Press Release: 14th WMCCC Jakarta](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/e1052ee6e0c1716c) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), September 15, 1996
- [Whats happening with Chess System Tal?](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/ea500961cdc4cf14) by Torstein Hall, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), December 3, 1996
- [Chess System Tal](https://www.stmintz.com/ccc/index.php?id=10025) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), September 22, 1997
- [CS Tal reply](https://www.stmintz.com/ccc/index.php?id=12508) by [Detlef Pordzik](Detlef_Pordzik "Detlef Pordzik"), [CCC](CCC "CCC"), November 29, 1997

[Re: CS Tal reply](https://www.stmintz.com/ccc/index.php?id=12565) by [Christophe Théron](Christophe_Th%C3%A9ron "Christophe Théron"), [CCC](CCC "CCC"), December 02, 1997

- [Chess System Tal on ICC](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2351569ef701d0fb) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 12, 1998
- [Chess System Tal II for Windows](https://www.stmintz.com/ccc/index.php?id=47726) by Didzis Cirulis, [CCC](CCC "CCC"), April 01, 1999
- [Chess System Tal upgrade 2.01](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/349f33a61897f59c) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), April 23, 1999
- [CSTal 2.50 Developer's Version](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8b379902631fd4f1) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), June 4, 1999
- [Chess System Tal](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/9eb9daca8c6b7546) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 23, 1999

## 2000 ...

- [Where does one buy Chess System Tal?](https://www.stmintz.com/ccc/index.php?id=89555) by James A. Tackett, [CCC](CCC "CCC"), January 18, 2000
- [complete rewrite of Chess System Tal](https://www.stmintz.com/ccc/index.php?id=219232) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), March 23, 2002
- [What's the strength of chess system tal II?](https://www.stmintz.com/ccc/index.php?id=242458) by Yang Sheng, [CCC](CCC "CCC"), July 25, 2002
- [Want to order System TAL II ....still available?](https://www.stmintz.com/ccc/index.php?id=272182) by Art Basham, [CCC](CCC "CCC"), December 21, 2002
- [Some Analysis by Chess System Tal 2 of Game 5 Kasparov-DJ](https://www.stmintz.com/ccc/index.php?id=282219) by Ludicrous, [CCC](CCC "CCC"), February 06, 2003 » [Kasparov versus Deep Junior 2003](Kasparov_versus_Deep_Junior_2003 "Kasparov versus Deep Junior 2003")
- [CSTAL 2 in another interface?](https://www.stmintz.com/ccc/index.php?id=354828) by Randy Adams, [CCC](CCC "CCC"), March 16, 2004

## 2005 ...

- [For those interested in: A) Chess Tal B) New engines](https://www.stmintz.com/ccc/index.php?id=429003) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), [CCC](CCC "CCC"), May 30, 2005
- [Chris Whittington's Chess System Tal!](http://www.talkchess.com/forum/viewtopic.php?t=21299) by [Swaminathan](Swaminathan_Natarajan "Swaminathan Natarajan"), [CCC](CCC "CCC"), May 22, 2008

## 2010 ...

- [Rating list with Virtual Chess 2 and/or Chess System Tal ?](http://www.talkchess.com/forum/viewtopic.php?t=42174) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), January 26, 2012 » [Virtual Chess](Virtual_Chess "Virtual Chess")
- [what is known about CSTal's inner workings?](http://www.talkchess.com/forum/viewtopic.php?t=53174) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), August 04, 2014
- [Re: La Máquina Preservadora. Programas de Ajedrez](http://www.foro.meca-web.es/viewtopic.php?f=9&t=72&start=50#p9325) by duct, [Meca Foro](Computer_Chess_Forums "Computer Chess Forums"), May 20, 2016 (Spanish)
- ["reincarnations" of Chess System Tal 2](http://www.hiarcs.net/forums/viewtopic.php?t=8184) by jarek, [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), December 26, 2016

## 2020 ...

- [Chess System Tal 2 released](https://prodeo.actieforum.com/t1264-chess-system-tal-2-released) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [ProDeo Forum](index.php?title=ProDeo_Forum&action=edit&redlink=1 "ProDeo Forum (page does not exist)"), June 29, 2023
- [Chess System Tal 2 NNUE has been released](https://talkchess.com/forum3/viewtopic.php?f=2&t=82249&) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](CCC "CCC"), June 29, 2023

## External Links

- [Chris Whittington on GitHub](https://github.com/ChrisWhittington/)
- [Chess System Tal's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=31)
- [AI Factory Chess Tal](http://www.aifactory.co.uk/AIF_Games_Chess_Tal.htm)
- [Chess System Tal for DOS (1997)](http://www.mobygames.com/game/chess-system-tal) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
- [Chess System Tal II for Windows (1999)](http://www.mobygames.com/game/chess-system-tal-ii) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
- [Chris Wittington - Chess System Tal: 25,31 Euro - Schachprogramm](http://www.schachversand.de/d/detail/software/58.html) from [Schachversand Niggemann](Schachversand_Niggemann "Schachversand Niggemann") (German)
- [Chris Wittington - Chess System Tal II: 50,11 Euro - Schachprogramm](http://www.schachversand.de/d/detail/software/201.html) from [Schachversand Niggemann](Schachversand_Niggemann "Schachversand Niggemann") (German)
- [Complete Chess System 2 - TAL](http://www.thorstenczub.de/complcss2.html) hosted by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
- [Was macht eigentlich: Chris Whittington ?](http://www.thorstenczub.de/cwnow.html) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") (German)
- [i hate materialists](http://www.thorstenczub.de/ihatematerialists.html) by [Chris Whittington](Chris_Whittington "Chris Whittington"), hosted by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
- [Chess System Tal - A Promise Finally Accomplished?](http://www.thorstenczub.de/cst_f_v.html) by [Fernando Villegas](Fernando_Villegas "Fernando Villegas"), hosted by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
- [Tal lebt!](http://www.thorstenczub.de/tal_lebt_inscw.html) by [Karsten Bauermeister](Karsten_Bauermeister "Karsten Bauermeister"), hosted by [Thorsten Czub](Thorsten_Czub "Thorsten Czub") (German)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Chess System Tal 2 (PC) bei spieletipps](http://www.spieletipps.de/pc/chess-system-tal-2/) (German)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [AI Factory Chess Tal](http://www.aifactory.co.uk/AIF_Games_Chess_Tal.htm)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [AI Factory World Championships and Competitions - Chess](http://www.aifactory.co.uk/AIF_Competitions.htm#chess)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: For those interested in: A) Chess Tal B) New engines](https://www.stmintz.com/ccc/index.php?id=429044) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub"), [CCC](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2005
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [AEGON Tournaments Computer Results Summary Latest 3 Tournaments](http://www.csvn.nl/index.php?option=com_content&task=view&id=124&Itemid=50), [CSVN](CSVN "CSVN") site
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Aegon 1996-97](http://www.thorstenczub.de/aegon.html) by [Thorsten Czub](Thorsten_Czub "Thorsten Czub")
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Amazon.com: Attack with Mikhail Tal (9781857440430): Mikhail Tal, Iakov Damsky, Ken Neat](http://www.amazon.com/Attack-Mikhail-Tal/dp/1857440439)
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Paderborn 1995 - Chess - Round 4 - Game 4 (ICGA Tournaments)](https://www.game-ai-forum.org/icga-tournaments/round.php?tournament=56&round=4&id=4)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Chess System Tal's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=31)

**[Up one Level](Engines "Engines")**

