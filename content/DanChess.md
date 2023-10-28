---
title: DanChess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * DanChess**

**DanChess**,

a chess engine by [Daniel Shawul](Daniel_Shawul "Daniel Shawul") written in [C++](Cpp "Cpp"), compliant to the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). DanChess uses a hybrid [mailbox](Mailbox "Mailbox") and [bitboards](Bitboards "Bitboards") board representation <a id="cite-note-1" href="#cite-ref-1">[1]</a> , utilizes [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps"), and is able to probe [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases"). DanChess had its tournament debut in 2005, playing a strong [CCT7](CCT7 "CCT7") <a id="cite-note-2" href="#cite-ref-2">[2]</a> , but was soon superseeded by its successor [Scorpio](Scorpio "Scorpio") <a id="cite-note-3" href="#cite-ref-3">[3]</a>.

## Contents

- [1 Controversy](#controversy)
- [2 Forum Posts](#forum-posts)
- [3 External Links](#external-links)
- [4 References](#references)

## Controversy

During [forum](Computer_Chess_Forums "Computer Chess Forums") discussions about early DanChess versions and the definition of [clones](Category:Clone "Category:Clone") <a id="cite-note-4" href="#cite-ref-4">[4]</a>, [Robert Hyatt](Robert_Hyatt "Robert Hyatt") pointed out DanChess had various pre-initialized tables as used in [Crafty](Crafty "Crafty") and a quite similar [SEE swap](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm") implementation <a id="cite-note-5" href="#cite-ref-5">[5]</a>, the latter also mentioned as extremely similar by [Dann Corbit](Dann_Corbit "Dann Corbit"), who as a kind of ombudsman inspected DanChess' source code concluding it "clean" otherwise, and disagreed with Hyatt about both the spirit and the extent of whether or not DanChess is a Crafty clone <a id="cite-note-6" href="#cite-ref-6">[6]</a>. However, all controversial tracks were later removed in subsequent versions, version 1.04 was published as open source <a id="cite-note-7" href="#cite-ref-7">[7]</a>.

## Forum Posts

- [WBEC-Ridderkerk new results + first chess engine from Ethiop](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=43920) by [Leo Dijksman](Leo_Dijksman "Leo Dijksman"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), August 29, 2003
- [New version of DanChess 1.02 8x faster](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45264) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 23, 2003
- [crafty clone?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45342) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 28, 2003
- [Danchess taken out suspected clone of ...](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46251) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 28, 2004
- [definition of clones: Danchess and Crafty](https://www.stmintz.com/ccc/index.php?id=349222) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 15, 2004
- [Robert Hyatt about Danchess and Crafty (in CCC)](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46486&start=20) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2004
- [Re: WBEC Ridderkerk new results](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46486&p=176048#p176025) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2004
- [DanChess accusation solved!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46332) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 24, 2004
- [DanChess with source code](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46673) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2004
- [DanChess 1.05 released!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=47804) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 07, 2004
- [DanChess 1.06](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=48175) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 13, 2004
- [DanChess SMP beta available](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=1113) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 24, 2004
- [About DanChess in cct7](https://www.stmintz.com/ccc/index.php?id=410092) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 07, 2005

## External Links

- [BayesianElo Ratinglist Edition 15 of WBEC Ridderkerk - DanChess](http://wbec-ridderkerk.nl/html/BayesianElo_ed15.htm)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Dan chess accusation solved!](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46332) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 24, 2004
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [About DanChess in cct7](https://www.stmintz.com/ccc/index.php?id=410092) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), February 07, 2005
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Gauntlet Scorpio v1.1 - games - replaced DanChess](https://www.stmintz.com/ccc/index.php?id=429465) by [Karl-Heinz Söntges](index.php?title=Karl-Heinz_S%C3%B6ntges&action=edit&redlink=1 "Karl-Heinz Söntges (page does not exist)"), [CCC](CCC "CCC"), June 02, 2005
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [crafty clone?](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45342) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), November 28, 2003
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: definition of clones: Danchess an Crafty](https://www.stmintz.com/ccc/index.php?id=349253) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), February 15, 2004
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: WBEC Ridderkerk new results](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46486&p=176048#p176025) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 15, 2004
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [DanChess with source code](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46673) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 01, 2004

**[Up one level](Engines "Engines")**

