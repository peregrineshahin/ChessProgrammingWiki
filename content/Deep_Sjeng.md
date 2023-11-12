---
title: Deep Sjeng
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Deep Sjeng**

**Deep Sjeng**,

a private, and former commercial chess engine by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), which emerged in 2002 from the 12.7 closed source branch of the chess variant and chess playing [open source engine](Category:Open_Source "Category:Open Source") [Sjeng](Sjeng "Sjeng") <a id="cite-note-1" href="#cite-ref-1">[1]</a> . Opposed to other commercial engines with the surename "deep" to indicate the version is able to play on multiple processors and sold for almost the double price than their "none deep" counterparts, Deep Sjeng, albeit able to play on multiple cores as well, is the native engine name for single as well as multiple processors.
Deep Sjeng was market since 2003 by [Lex Loep's](Lex_Loep "Lex Loep") company [Lokasoft](Lokasoft "Lokasoft") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . It came with the [ChessPartner](ChessPartner "ChessPartner") [graphical interface](GUI "GUI") and supports [UCI](UCI "UCI") and the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Version 2.X with the [Mayura Chess Board](index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)") <a id="cite-note-3" href="#cite-ref-3">[3]</a> and its third incarnation Deep Sjeng 3.x were distributed via Gian-Carlo's own site, but Deep Sjeng is no longer for sale <a id="cite-note-4" href="#cite-ref-4">[4]</a> .

## Contents

- [1 Tournaments](#tournaments)
- [2 Screenshot](#screenshot)
- [3 Parallel Search](#parallel-search)
- [4 Automated Learning](#automated-learning)
- [5 Forum Posts](#forum-posts)
- [6 External Links](#external-links)
- [7 References](#references)

## Tournaments

Deep Sjeng played many [computer chess tournaments](Tournaments_and_Matches "Tournaments and Matches"). It participated (so far) at six [World Computer Chess Championships](World_Computer_Chess_Championship "World Computer Chess Championship") <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

|  Edition
|  Tournament
|  Ranking
|  Participants
|  Score
|  Games
|
| --- | --- | --- | --- | --- | --- |
|  11th
| [WCCC 2003](WCCC_2003 "WCCC 2003") | [Graz](https://en.wikipedia.org/wiki/Graz) |  11
|  16
|  4.5
|  11
|
|  12th
| [WCCC 2004](WCCC_2004 "WCCC 2004") | [Ramat Gan](https://en.wikipedia.org/wiki/Ramat_Gan) |  10
|  14
|  5.5
|  11
|
|  13th
| [WCCC 2005](WCCC_2005 "WCCC 2005") | [Reykjavík](https://en.wikipedia.org/wiki/Reykjav%C3%ADk) |  3
|  12
|  7.5
|  11
|
|  15th
| [WCCC 2007](WCCC_2007 "WCCC 2007") | [Amsterdam](https://en.wikipedia.org/wiki/Amsterdam) |  6
|  11
|  6
|  11
|
|  16th
| [WCCC 2008](WCCC_2008 "WCCC 2008") <a id="cite-note-6" href="#cite-ref-6">[6]</a> | [Beijing](https://en.wikipedia.org/wiki/Beijing) |  8
|  10
|  3.5
|  9
|
|  17th
| [WCCC 2009](WCCC_2009 "WCCC 2009") <a id="cite-note-7" href="#cite-ref-7">[7]</a> | [Pamplona](https://en.wikipedia.org/wiki/Pamplona) |  1
|  9
|  6.5
|  9
|

Deep Sjeng further played various [Dutch Open Computer Chess Championships](Dutch_Open_Computer_Chess_Championship "Dutch Open Computer Chess Championship"), [International CSVN Tournaments](International_CSVN_Tournament "International CSVN Tournament"), [Livingston Chess960 Computer World Championships](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship"), dominated [The Chess Programmers Tournament](The_Chess_Programmers_Tournament "The Chess Programmers Tournament") with three wins so far from four editions, and won the Italian [IOCSC 2010](IOCSC_2010 "IOCSC 2010"). Online Deep Sjeng played multiple [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), where Deep Sjeng won the [CCT12](CCT12 "CCT12") in 2010 and [CCT13](CCT13 "CCT13") in 2011. Since 2008, Deep Sjeng participated the [ACCA World Computer Rapid Chess Championship](ACCA_World_Computer_Rapid_Chess_Championship "ACCA World Computer Rapid Chess Championship") always with top rankings, winning the [WCRCC 2012](WCRCC_2012 "WCRCC 2012").

## Screenshot

[](https://sjeng.org/deepsjeng2.html)
Deep Sjeng 2.5 with [Mayura Chess Board](index.php?title=Mayura_Chess_Board&action=edit&redlink=1 "Mayura Chess Board (page does not exist)") <a id="cite-note-8" href="#cite-ref-8">[8]</a>

## Parallel Search

[Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto") in a reply to [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann") on Deep Sjeng's [parallel search](Parallel_Search "Parallel Search") <a id="cite-note-9" href="#cite-ref-9">[9]</a> :

How is Deep Sjeng going? What did you use to understand the parallel algorithms you are using (which ones) ?

```C++
I started out with [ABDADA](ABDADA "ABDADA") (described in ICCA journal article and used in [Amy](Amy "Amy")), which got me a speedup of +- 1.2. I went on to try [PVS](Parallel_Search#PrincipalVariationSplitting "Parallel Search") ([Crafty 15.0](Crafty "Crafty") and described in several articles about parallel search) which got me a speedup of 1.2-1.3.

```

```C++
1.3 wasn't enough, so I 'bit the bullent' and started looking at [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting") ([Cray Blitz](Cray_Blitz "Cray Blitz")). Unfortunately, DTS is both hideously complicated and requires a [nonrecursive search](Iterative_Search "Iterative Search") and a [p2p design](https://en.wikipedia.org/wiki/Point-to-point_%28network_topology%29#Point-to-point). I spent some time working on a variant of DTS that can work with a [recursive](Recursion "Recursion") search function and a [master-slave design](https://en.wikipedia.org/wiki/Master/slave_%28technology%29) and that is what I am using now. It still needs a lot of test work, but current results indicate a speedup of about 1.6. 

```

## Automated Learning

In 2007, Gian-Carlo's experimental program [Stoofvlees](Stoofvlees "Stoofvlees") aka Deep Sjeng 2.7 <a id="cite-note-10" href="#cite-ref-10">[10]</a> with a set of feature recognizers coupled to a [neural network](Neural_Networks "Neural Networks") <a id="cite-note-11" href="#cite-ref-11">[11]</a>, had its [evaluation function](Evaluation_Function "Evaluation Function") entirely [automatically](Automated_Tuning "Automated Tuning") [learned](Learning "Learning") from "watching" Grandmaster games. The results were incorporated into Deep Sjeng 3.0 <a id="cite-note-12" href="#cite-ref-12">[12]</a>. The engine has noticeably improved in strength, particularly in the areas where it was less optimal before.

## Forum Posts

- [Deep Sjeng testers wanted](https://www.stmintz.com/ccc/index.php?id=248485) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 28, 2002
- [Deep Sjeng 1.0 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/261bfb217175033a) by [Lex](Lex_Loep "Lex Loep"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 3, 2003
- [Deep Sjeng Opteron Performance Results](https://www.stmintz.com/ccc/index.php?id=310212) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 06, 2003
- [Positions from the WCCC2005: Deep Sjeng - Zappa](https://www.stmintz.com/ccc/index.php?id=445348) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 26, 2005
- [Deep Sjeng 2.5 has arrived!](http://www.talkchess.com/forum/viewtopic.php?t=13368) by [Eelco de Groot](index.php?title=Eelco_de_Groot&action=edit&redlink=1 "Eelco de Groot (page does not exist)"), April 24, 2007
- [Deep Sjeng 2.7 released](http://www.talkchess.com/forum/viewtopic.php?t=16244) by Jens, [CCC](CCC "CCC"), September 03, 2007
- [Incredibly crazy game from Leiden: Deep Sjeng - The King](http://www.talkchess.com/forum/viewtopic.php?t=30193) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 18, 2009
- [Deep Sjeng @ 29th Dutch Open](http://www.talkchess.com/forum/viewtopic.php?t=30221) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 19, 2009
- [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316769&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 08, 2010
- [Deep Sjeng 50-move rule bug](http://www.talkchess.com/forum/viewtopic.php?t=33259) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), March 14, 2010
- [Deep Sjeng @ ICT 2010](http://www.talkchess.com/forum/viewtopic.php?t=34671) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), June 02, 2010

## External Links

- [Sjeng - chess, audio and misc. software - Deep Sjeng 3.x](https://sjeng.org/deepsjeng3.html)
- [Sjeng's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=72) (mostly Deep Sjeng)
- [Sjeng (Chess) from Wikipedia](https://en.wikipedia.org/wiki/Sjeng_%28Chess%29)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Sjeng 12.7 and 11.2 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/66707061247326df) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), January 2, 2002
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Deep Sjeng 1.0 released](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/261bfb217175033a) by [Lex](Lex_Loep "Lex Loep"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), March 3, 2003
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [SJENG.ORG - Deep Sjeng 2.x](http://sjeng.org/deepsjeng2.html)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [SJENG.ORG - Deep Sjeng 3.x](http://sjeng.org/deepsjeng3.html)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Sjeng's ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=72) (mostly Deep Sjeng)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> Deep Sjeng played the [WCCC 2008](WCCC_2008 "WCCC 2008") under the name Sjeng, not to confused with the "old" Sjeng
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> After the [disqualification](World_Computer_Chess_Championship#RybkaDisqualification "World Computer Chess Championship") of [Rybka](Rybka "Rybka") in June 2011, shared Champion with [Shredder](Shredder "Shredder") and [Junior](Junior "Junior")
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Deep Sjeng 2.x - Screenshots](https://sjeng.org/deepsjeng2.html)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Deep Sjeng testers wanted](https://www.stmintz.com/ccc/index.php?id=248594) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 29, 2002
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Deep Sjeng 2.7 released](http://www.talkchess.com/forum/viewtopic.php?t=16244) by Jens, [CCC](CCC "CCC"), September 03, 2007
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316511&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 07, 2010
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [Re: Chess program with Artificial Neural Networks (ANN)?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=316769&t=31545) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 08, 2010

**[Up one Level](Engines "Engines")**

