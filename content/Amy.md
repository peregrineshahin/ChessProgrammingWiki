---
title: Amy
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Amy**

\[ The [Seal](https://en.wikipedia.org/wiki/Seal_%28emblem%29) of [Amy](https://en.wikipedia.org/wiki/Amy_%28demon%29) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Amy**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [XBoard](XBoard "XBoard") compliant [open source chess program](Category:Open_Source "Category:Open Source") under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation") by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), written in [C](C "C"). Its development started in 1993 on the [Amiga](Amiga "Amiga") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, and continued on [Unix](Unix "Unix") platforms, in particular [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD) <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Amy 0,6 was ported to [Windows](Windows "Windows") for [WinBoard](WinBoard "WinBoard") by [Dann Corbit](Dann_Corbit "Dann Corbit") in early 2000 <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Amy played the [WMCCC 1995](WMCCC_1995 "WMCCC 1995") in [Paderborn](https://en.wikipedia.org/wiki/Paderborn) and multiple [International Paderborn Computer Chess Championships](IPCCC "IPCCC").

## Contents

- [1 Features](#features)
  - [1.1 Board Representation](#board-representation)
  - [1.2 Search](#search)
  - [1.3 Evaluation](#evaluation)
  - [1.4 Misc](#misc)
- [2 See also](#see-also)
- [3 Forum Posts](#forum-posts)
  - [3.1 2000](#2000)
  - [3.2 2002 ...](#2002-...)
  - [3.3 2010 ...](#2010-...)
- [4 External Links](#external-links)
  - [4.1 Chess Engine](#chess-engine)
  - [4.2 Misc](#misc-2)
  - [4.3 Demonology](#demonology)
- [5 References](#references)

## Features

## [Board Representation](Board_Representation "Board Representation")

- [Bitboards](Bitboards "Bitboards")
- [Incremental Updated](Incremental_Updates "Incremental Updates") [Attack Tables](Attack_and_Defend_Maps "Attack and Defend Maps") à la [Chess 4.x](</Chess_(Program)#Chess_4.0_-_4.9> "Chess (Program)") (atkTo[64], atkFr[64]) <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Search](Search "Search")

- [ABDADA](ABDADA "ABDADA")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [NegaScout](NegaScout "NegaScout")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [SEE - Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
- [SEX Algorithm](SEX_Algorithm "SEX Algorithm")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Futility Pruning](Futility_Pruning "Futility Pruning")
  - [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
  - [Razoring](Razoring "Razoring")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
  - [One Reply Extensions](One_Reply_Extensions "One Reply Extensions")
  - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Zugzwang Extensions](Mate_Threat_Extensions#Deep-Search_Extensions "Mate Threat Extensions")
- [Interior Node Recognizer](Interior_Node_Recognizer "Interior Node Recognizer")
- [Quiescence Search](Quiescence_Search "Quiescence Search")

## [Evaluation](Evaluation "Evaluation")

- [Millipawn](Millipawns "Millipawns") Resolution
- [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Material](Material "Material")
- [Bishop Pair](Bishop_Pair "Bishop Pair")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Development](Development "Development")
- [Mobility](Mobility "Mobility")
  - [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
  - [Rook on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
  - [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
  - [Rook Battery](Battery "Battery")
- [Knight Outpost](Outposts "Outposts")
- [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
  - [Backward Pawn](Backward_Pawn "Backward Pawn")
  - [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
  - [Straggler](</Backward_Pawns_(Bitboards)#Straggler> "Backward Pawns (Bitboards)")
  - [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
  - [Pawn Duo](</Duo_Trio_Quart_(Bitboards)> "Duo Trio Quart (Bitboards)")
  - [Pawn Majority](Pawn_Majority "Pawn Majority")
  - [Passed Pawn](Passed_Pawn "Passed Pawn")
    - [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
    - [Blockade of Stop](Blockade_of_Stop "Blockade of Stop")
    - [Control of Stop and Telestop](Control_of_Stop_and_Telestop "Control of Stop and Telestop")
    - [Tarrasch Rule](Tarrasch_Rule "Tarrasch Rule")
    - [Outside Passed Pawn](Outside_Passed_Pawn "Outside Passed Pawn")
    - [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
- [King Safety](King_Safety "King Safety")
  - [Pawn Shield](King_Safety#PawnShield "King Safety")
  - [Fianchetto](Fianchetto "Fianchetto")
  - [Pawn Storm](King_Safety#PawnStorm "King Safety")
  - [King Tropism](King_Safety#KingTropism "King Safety")

## Misc

- [Opening Book](Opening_Book "Opening Book")
- [Book Learning](Book_Learning "Book Learning")

## See also

- [Amyan](Amyan "Amyan")

## Forum Posts

## 2000

- [Amy-0.6 released](https://www.stmintz.com/ccc/index.php?id=94606) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [CCC](CCC "CCC"), February 04, 2000
- [Something interesting about Amy](https://www.stmintz.com/ccc/index.php?id=94791) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), February 05, 2000
- [Amy 0,6 für Winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30827) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 05, 2000
- [New version of Amy should now multithread properly](https://www.stmintz.com/ccc/index.php?id=95905) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), February 08, 2000
- [Re: Amy and Isi at Paderborn? =(](https://www.stmintz.com/ccc/index.php?id=97165) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [CCC](CCC "CCC"), February 14, 2000
- [Amy-0.7 released](https://www.stmintz.com/ccc/index.php?id=102850) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [CCC](CCC "CCC"), March 22, 2000
- [New Amy Update (0.7)](https://www.stmintz.com/ccc/index.php?id=103124) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 23, 2000
- [Amy play very strong in my FQ-2 tournament !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31344) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 20, 2000

[Re: Amy play very strong in my FQ-2 tournament !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31344#p118550) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2000

- [Amy Source Code Is Outstanding Re: Quality source code](https://www.stmintz.com/ccc/index.php?id=140286) by [Brian Richardson](Brian_Richardson "Brian Richardson"), [CCC](CCC "CCC"), November 21, 2000
- [Usage of egtb.cpp in GPL software (Amy, ExChess, ...)](https://www.stmintz.com/ccc/index.php?id=142991) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), December 05, 2000 » [EXchess](EXchess "EXchess")

## [Re: Usage of egtb.cpp in GPL software (Amy, ExChess, ...)](https://www.stmintz.com/ccc/index.php?id=143013) by [Eugene Nalimov](Eugene_Nalimov "Eugene Nalimov"), [CCC](CCC "CCC"), December 05, 2000 » [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases") 2002 ...

- [Amy question...](https://www.stmintz.com/ccc/index.php?id=225207) by Jonas Cohonas, [CCC](CCC "CCC"), April 21, 2002
- [Great news from Thorsten Greiner: New Amy v0.8!!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38285) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 24, 2002
- [Amy 0.8](https://www.stmintz.com/ccc/index.php?id=242914) by Jonas Cohonas, [CCC](CCC "CCC"), July 28, 2002
- [Amy 0.8.1](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38354) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 29, 2002
- [Amy 0.8.4](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43119) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 23, 2003
- [for Dann Corbit about Amy 0.87](https://www.stmintz.com/ccc/index.php?id=450670) by Wilhelm Hudetz, [CCC](CCC "CCC"), September 20, 2005
- [Amy 0.8 mp x64 Windows build available](http://www.talkchess.com/forum/viewtopic.php?t=18663) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), December 31, 2007

## 2010 ...

- [Comet B15, Amy 0.6 Green Light Chess 2.07a available ...](http://www.talkchess.com/forum/viewtopic.php?t=32361) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), February 04, 2010 » [Comet](Comet "Comet"), [Green Light Chess](Green_Light_Chess "Green Light Chess")

## External Links

## Chess Engine

- [Amy's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=201)
- [tgreiner.net - Thorsten's Nifty Geeklog Site](http://web.archive.org/web/20050206093204/www.tgreiner.net/) hosted by [archive.org](https://en.wikipedia.org/wiki/Internet_Archive)

[Download Amy 0.8.7](http://web.archive.org/web/20050307080145/http://www.tgreiner.net/article.php?story=2004050623271311)

- [Amy](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/AMY/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Amy 0.87b](http://computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=Amy%200.87b#Amy_0_87b) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Amy (given name) from Wikipedia](https://en.wikipedia.org/wiki/Amy)
- [Amy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Amy_%28disambiguation%29)

## Demonology

- [Amy (demon) from Wikipedia](https://en.wikipedia.org/wiki/Amy_%28demon%29)
- [Pseudomonarchia Daemonum from Wikipedia](https://en.wikipedia.org/wiki/Pseudomonarchia_Daemonum)
- [List of demons in the Ars Goetia from Wikipedia](https://en.wikipedia.org/wiki/List_of_demons_in_the_Ars_Goetia)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> *The Fifty-eighth Spirit is Amy, or Avnas. He is a Great President, and appeareth at first in the form of a Flaming Fire; bur after a while he putteth on the Shape of a Man. His Office is to make one Wonderful Knowing in Astrology and all the Liberal Sciences. He giveth Good Familiars and can bewray Treasure that is kept by Spirits. He governeth 36 Legions of Spirits, and his Seal is this, etc.* in [Aleister Crowley](https://en.wikipedia.org/wiki/Aleister_Crowley) (**1904**). *[The Book of the Goetia of Solomon the King](https://archive.org/details/ac_goetia/page/n3)*. pp. 30, [Amy seal](https://commons.wikimedia.org/wiki/File:58-Amy_seal.png) from [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Amy play very strong in my FQ-2 tournament !](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=31344#p118550) by [Thorsten Greiner](Thorsten_Greiner "Thorsten Greiner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 25, 2000
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Index of /pub/FreeBSD-Archive/old-releases/pc98/5.3-RELEASE/packages/games/](http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/old-releases/pc98/5.3-RELEASE/packages/games/)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Amy 0,6 für Winboard](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=30827) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 05, 2000
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *Chess 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (1988) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")

**[Up one level](Engines "Engines")**

