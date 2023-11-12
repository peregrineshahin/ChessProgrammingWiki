---
title: MVVLVA
---
**[Home](Home "Home") \* [Search](Search "Search") \* [Move Ordering](Move_Ordering "Move Ordering") \* MVV-LVA**


**MVV-LVA** (**M**ost **V**aluable **V**ictim - **L**east **V**aluable **A**ggressor),  

is a simple heuristic to [generate](Move_Generation "Move Generation") or sort [capture moves](Captures "Captures") in a reasonable order. Inside a so called find-victim cycle, one first look up the potential victim of all [attacked](Attacks "Attacks") opponent pieces, in the order of the most valuable first, thus [queen](Queen "Queen"), [rook](Rook "Rook"), [bishop](Bishop "Bishop"), [knight](Knight "Knight") and [pawn](Pawn "Pawn"). After the most valuable victim is found, the find-aggressor cycle loops over the potential aggressors that may capture the victim in inverse order, from pawn, knight, bishop, rook, queen to [king](King "King"). The heuristic is easy to implement and covers a lot of simple cases, such as PxR before BxP. It is used in various move generators build in hardware, such a [Belle](Belle#Hardware "Belle") and more recently in [FPGA](FPGA "FPGA") approaches such as [Brutus](Brutus "Brutus") and [MBChess](MBChess "MBChess") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. However the heuristic may fail, if victims attacked by more valuable attackers are defended, in such cases most programs rely on [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), set-wise [pawn attacks](Pawn_Attacks_(Bitboards)#PawnAttacks "Pawn Attacks (Bitboards)") (defends) on the fly to perform a [static exchange evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation").



## Forum Posts


### 1995 ...


* [mvv/lva vs SEE capture ordering test results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/1fa5e36362f5dde4) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 10, 1995
* [MVV/LVA vs SEE move ordering - more test results](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/645f44f84102e450) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 25, 1995


 [Re: MVV/LVA vs SEE move ordering - more test results](http://groups.google.com/group/rec.games.chess.computer/msg/1951744da404fc33) by [Brian Sheppard](Brian_Sheppard "Brian Sheppard"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 27, 1995
* [MVV/LVA and SEE - what do they mean?](https://groups.google.com/d/msg/rec.games.chess.computer/5byhl_6Jmc8/D1QAR146VLIJ) by [Peter Kappler](Peter_Kappler "Peter Kappler"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), August 28, 1995
* [MVA/LVA sorting order](https://www.stmintz.com/ccc/index.php?id=45655) by [Jan Willem de Kort](index.php?title=Jan_Willem_de_Kort&action=edit&redlink=1 "Jan Willem de Kort (page does not exist)"), [CCC](CCC "CCC"), March 12, 1999


### 2000 ...


* [Fast BB move generation](https://www.stmintz.com/ccc/index.php?id=109588) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), May 08, 2000
* [MVV/LVA or SEE - liability?](https://www.stmintz.com/ccc/index.php?id=141813) by [Severi Salminen](Severi_Salminen "Severi Salminen"), [CCC](CCC "CCC"), November 29, 2000 » [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [MVVLVA sorting does not help for move ordering](https://www.stmintz.com/ccc/index.php?id=253151) by [Scott Farrell](Scott_Farrell "Scott Farrell"), [CCC](CCC "CCC"), September 21, 2002


### 2005 ...


* [Sorting captures](http://www.talkchess.com/forum/viewtopic.php?t=22755) by [Pablo Vazquez](Pablo_Vazquez "Pablo Vazquez"), [CCC](CCC "CCC"), August 02, 2008
* [Effect of MVV/LVA](http://www.talkchess.com/forum/viewtopic.php?t=23727) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), Sepember 14, 2008
* [MVV/LVA. Or should it be LVV/MVA?](http://www.talkchess.com/forum/viewtopic.php?t=27254) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), March 31, 2009


### 2010 ...


* [LVA MVV with relative Pin](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=395213) by [Clemens Pruell](index.php?title=Clemens_Pruell&action=edit&redlink=1 "Clemens Pruell (page does not exist)"), [CCC](CCC "CCC"), February 16, 2011 » [Pin](Pin "Pin")
* [MVV/LVA sorting](http://www.talkchess.com/forum/viewtopic.php?t=48202) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 05, 2013


### 2015 ...


* [DarkThought sorts MVV/LVA without looking at any moves?](http://www.talkchess.com/forum/viewtopic.php?t=56114) by Rob Williamson, [CCC](CCC "CCC"), April 25, 2015 » [DarkThought](DarkThought "DarkThought")
* [MVV/LVA](http://www.talkchess.com/forum/viewtopic.php?t=57813) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 02, 2015
* [Sorting Captures](http://www.talkchess.com/forum/viewtopic.php?t=61021) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), August 03, 2016
* [A smarter MVV/LVA](http://www.open-chess.org/viewtopic.php?f=5&t=3058) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 28, 2016
* [MVV LVA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67873) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 01, 2018
* [is LVA as in MVV-LVA useless ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70918) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 04, 2019
* [correct way to score promotions using MVV-LVA](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70936) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), June 06, 2019 » [Promotions](Promotions "Promotions")


## External links


* [MVV/LVA](http://web.archive.org/web/20040427014440/brucemo.com/compchess/programming/quiescent.htm#MVVLVA) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20040403211728/brucemo.com/compchess/programming/index.htm)
* [Micro-Max 4: Quiescence Search](http://home.hccnet.nl/h.g.muller/mvv.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
* [The Dorf](Category:The_Dorf "Category:The Dorf") feat. [FM Einheit](https://en.wikipedia.org/wiki/F.M._Einheit) und [Caspar Brötzmann](https://en.wikipedia.org/wiki/Caspar_Br%C3%B6tzmann) - [Massaker](https://en.wikipedia.org/wiki/Home_(Caspar_Br%C3%B6tzmann_Massaker_album)), [Grammatikoff](http://www.grammatikoff.de/), [Duisburg](https://en.wikipedia.org/wiki/Duisburg), May 17, 2014, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Marc Boulé](Marc_Boul%C3%A9 "Marc Boulé") (**2002**). *An FPGA Move Generator for the Game of Chess*. Masters thesis, [McGill University](McGill_University "McGill University"), (Supervisor: [Zeljko Zilic](Zeljko_Zilic "Zeljko Zilic"), Co-Supervisor: [Monty Newborn](Monroe_Newborn "Monroe Newborn")), [pdf](http://www.iml.ece.mcgill.ca/%7Emboule/files/mbthesis02.pdf)

**[Up one level](Move_Ordering "Move Ordering")**







 
