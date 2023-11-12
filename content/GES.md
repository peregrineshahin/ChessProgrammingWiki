---
title: GES
---
**[Home](Home "Home") * [Engines](Engines "Engines") * GES**

**GES**,

[David B. Weller's](David_B._Weller "David B. Weller") first chess engine, written in [C](C "C") and compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") aka [WinBoard](WinBoard "WinBoard"),
first released in July 2004 <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
GES applies [PVS](Principal_Variation_Search "Principal Variation Search") with [aspiration](Aspiration_Windows "Aspiration Windows"), a [main transposition table](Transposition_Table "Transposition Table") and [pawn hash table](Pawn_Hash_Table "Pawn Hash Table") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, [verified null move pruning](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning"),
and a rudimentary [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation"). GES' [extension](Extensions "Extensions") policy was to add one [ply](Ply "Ply") if any of the conditions met, which were [checks](Check_Extensions "Check Extensions"), [pawns to 2nd/7th rank](Passed_Pawn_Extensions "Passed Pawn Extensions"), [mate threats](Mate_Threat_Extensions "Mate Threat Extensions"), [single replies](One_Reply_Extensions "One Reply Extensions"), and [recaptures](Recapture_Extensions "Recapture Extensions"), and later tried aggregated but [fractional extensions](Extensions#FractionalExtensions "Extensions") without obvious progress <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## See also

- [Xpdnt](Xpdnt "Xpdnt")

## Forum Posts

## 2004

- [new win32 winboard engine](https://www.stmintz.com/ccc/index.php?id=374619) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), July 07, 2004
- [GES is working!](https://www.stmintz.com/ccc/index.php?id=379254) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), July 27, 2004
- [GES 108](https://www.stmintz.com/ccc/index.php?id=382689) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), August 17, 2004
- [GES 110 available](https://www.stmintz.com/ccc/index.php?id=382846) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), August 18, 2004
- [GES 111](https://www.stmintz.com/ccc/index.php?id=382993) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), August 19, 2004
- [GES 117 available n/t](https://www.stmintz.com/ccc/index.php?id=385958) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), September 04, 2004
- [GES_126 available](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=363&p=1337) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 24, 2004
- [GES_132](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1112&p=5033) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 23, 2004
- [GES_133](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1140&p=5139) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 26, 2004

## 2005

- [Under the wire! GES_134](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1253&p=5736) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 06, 2005
- [About GES..](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1333&p=6242) by [Carlos Pesce](Carlos_Pesce "Carlos Pesce"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 14, 2005
- [GES Lives!](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1713&p=7904) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2005
- [Testers needed](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1746&p=8154) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 22, 2005
- [Limiting extensions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1754&p=8190) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 23, 2005
- [GES_136 available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2040&p=9533) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 21, 2005

## External Links

- [Index of /chess/engines/Jim Ablett/GES](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/GES/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Engine Download List](http://www.computer-chess.org/doku.php?id=computer_chess:wiki:download:engine_download_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [new win32 winboard engine](https://www.stmintz.com/ccc/index.php?id=374619) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), July 07, 2004
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [GES 111](https://www.stmintz.com/ccc/index.php?id=382993) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), August 19, 2004
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Limiting extensions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=1754&p=8190) by [David B. Weller](David_B._Weller "David B. Weller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 23, 2005

**[Up one Level](Engines "Engines")**

