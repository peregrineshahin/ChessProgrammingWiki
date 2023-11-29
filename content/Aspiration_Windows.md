---
title: Aspiration Windows
---
**[Home](Home "Home") * [Search](Search "Search") * [Alpha-Beta](Alpha-Beta "Alpha-Beta") * Aspiration Windows**

[](File:TheNon-EuclideanWindow.JPG) The Non-Euclidean Window <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Aspiration windows** are a way to reduce the [search space](Search_Space "Search Space") in an alpha-beta search. The technique is to use a guess of the expected value (usually from the last iteration in [iterative deepening](Iterative_Deepening "Iterative Deepening")), and use a [window](Window "Window") around this as the alpha-beta [bounds](Bound "Bound"). Because the window is narrower, more beta cutoffs are achieved, and the search takes a shorter time. The drawback is that if the true score is outside this window, then a costly re-search must be made. Typical window sizes are 1/2 to 1/4 of a pawn on either side of the guess.

## Gradual Widening

Some programs, such as [Crafty](Crafty "Crafty"), also use a gradual widening on re-searches. For instance, if the window is, in pawns:

```C++[g - 1/4, g + 1/4]

```

and the search fails high, the next search would be

```C++[g - 1/4, g + 1]

```

It's important to note that the bound that didn't fail is unchanged. In a basic alpha-beta without [search instability](Search_Instability "Search Instability"), one could have done the next search on

```C++[g + 1/4, g + 1]

```

instead. However, a fully fledged search is typically full of [search instability](Search_Instability "Search Instability"), and it will often happen that the above re-search will fail low! This is why it is best to only widen the bound that fails, and leave the other bound unchanged.

Modern engines, like [RobboLito](RobboLito "RobboLito") or [Stockfish](Stockfish "Stockfish"), start with a rather small aspiration window, and increase the bound that fails in an exponential fashion.

## PVS and Aspiration

Using aspiration windows together with the [principal variation search](Principal_Variation_Search "Principal Variation Search") (PVS) causes some additional complications.

- [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")

## See also

- [Null Window](Null_Window "Null Window")
- [Scoring Root Moves](Ronald_de_Man#ScoringRootMoves "Ronald de Man")
- [Search Instability](Search_Instability "Search Instability")
- [Window](Window "Window")

## Publications

- [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Reza Shams](index.php?title=Reza_Shams&action=edit&redlink=1 "Reza Shams (page does not exist)"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1991**). *[Minimax Search Algorithms with and without Aspiration Windows](http://portal.acm.org/citation.cfm?id=123034).* [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 13, No. 12
- [Reza Shams](index.php?title=Reza_Shams&action=edit&redlink=1 "Reza Shams (page does not exist)"), [Hermann Kaindl](Hermann_Kaindl "Hermann Kaindl"), [Helmut Horacek](Helmut_Horacek "Helmut Horacek") (**1991**). *Using Aspiration Windows for Minimax Algorithms*. [IJCAI 1991](Conferences#IJCAI1991 "Conferences"), [pdf](http://ijcai.org/Proceedings/91-1/Papers/031.pdf)

## Forum Posts

## 1995 ...

- [Question about aspiration window](https://www.stmintz.com/ccc/index.php?id=24677) by [Werner Inmann](Werner_Inmann "Werner Inmann"), [CCC](CCC "CCC"), August 14, 1998
- [aspiration windows](https://www.stmintz.com/ccc/index.php?id=34177) by [James Long](James_Swafford "James Swafford"), [CCC](CCC "CCC"), November 27, 1998
- [Aspiration Rules...](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/8ad0cbc2b137dbf3) by Chris Pile, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), February 5, 1999
- [Aspiration search](https://www.stmintz.com/ccc/index.php?id=49314) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), April 20, 1999
- [Aspiration search](https://www.stmintz.com/ccc/index.php?id=64553) by [Scott Gasch](Scott_Gasch "Scott Gasch"), [CCC](CCC "CCC"), August 13, 1999

## 2000 ...

- [Aspiration window](https://www.stmintz.com/ccc/index.php?id=208714) by [Bas Hamstra](Bas_Hamstra "Bas Hamstra"), [CCC](CCC "CCC"), January 20, 2002
- [Exact value of second best move in AlphaBeta with aspiration Window](https://www.stmintz.com/ccc/index.php?id=243640) by [Martin Bauer](Martin_Bauer "Martin Bauer"), [CCC](CCC "CCC"), August 01, 2002
- [Aspiration search, PVS](https://www.stmintz.com/ccc/index.php?id=273558) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), December 28, 2002
- [Unstable aspiration search](https://www.stmintz.com/ccc/index.php?id=283426) by [Sune Fischer](Sune_Fischer "Sune Fischer"), [CCC](CCC "CCC"), February 10, 2003
- [Question about aspiration search](https://www.stmintz.com/ccc/index.php?id=356170) by [Jaime Benito de Valle Ruiz](Jaime_Benito_de_Valle_Ruiz "Jaime Benito de Valle Ruiz"), [CCC](CCC "CCC"), March 23, 2004
- [What is a common Aspiration window?](https://www.stmintz.com/ccc/index.php?id=356826) by [Joachim Rang](index.php?title=Joachim_Rang&action=edit&redlink=1 "Joachim Rang (page does not exist)"), [CCC](CCC "CCC"), March 26, 2004
- [aspiration search question](https://www.stmintz.com/ccc/index.php?id=364869) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), May 13, 2004
- [Q. Aspiration, PVS, Fail-Soft](https://www.stmintz.com/ccc/index.php?id=373537) by [David B. Weller](David_B._Weller "David B. Weller"), [CCC](CCC "CCC"), July 02, 2004
- [PVS and aspiration windows](https://www.stmintz.com/ccc/index.php?id=381004) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 06, 2004

## 2005 ...

- [Aspiration Window sizes](https://www.stmintz.com/ccc/index.php?id=416677) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), March 14, 2005
- [Bounds for aspiration window re-search](http://www.talkchess.com/forum/viewtopic.php?t=27040) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), March 17, 2009
- [A way to improve PVS](http://www.talkchess.com/forum/viewtopic.php?t=29681) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), September 07, 2009

## 2010 ...

- [Apiration window](http://www.talkchess.com/forum/viewtopic.php?t=33500) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), March 27, 2010
- [A few general questions...](http://www.talkchess.com/forum/viewtopic.php?t=42224) by [Bill Henry](index.php?title=Bill_Henry&action=edit&redlink=1 "Bill Henry (page does not exist)"), [CCC](CCC "CCC"), January 29, 2012 » [Root](Root "Root"), [Exact Score](Exact_Score "Exact Score")
- [optimal aspiration window for stockfish question](http://www.talkchess.com/forum/viewtopic.php?t=42841) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), March 12, 2012 » [Stockfish](Stockfish "Stockfish")
- [Aspiration Windows: Rubbish!](http://www.talkchess.com/forum/viewtopic.php?t=44464) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), July 16, 2012
- [Aspiration window - effect? Issue with hashtables?!](http://www.talkchess.com/forum/viewtopic.php?t=46624) by [Jens Bæk Nielsen](Jens_B%C3%A6k_Nielsen "Jens Bæk Nielsen"), [CCC](CCC "CCC"), December 28, 2012
- [Aspiration Windows](http://www.talkchess.com/forum/viewtopic.php?t=46837) by [Jerry Donald](index.php?title=Jerry_Donald&action=edit&redlink=1 "Jerry Donald (page does not exist)"), [CCC](CCC "CCC"), January 11, 2013
- [Aspiration windows](http://www.talkchess.com/forum/viewtopic.php?t=47996) by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni"), [CCC](CCC "CCC"), May 14, 2013
- [Your experience with PVS + Aspiration window](http://www.talkchess.com/forum/viewtopic.php?t=53972) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), October 07, 2014 » [Principal Variation Search](Principal_Variation_Search "Principal Variation Search"), [PVS and Aspiration](PVS_and_Aspiration "PVS and Aspiration")
- [Solving a fail low situation at the root](http://www.talkchess.com/forum/viewtopic.php?t=54241) by [Alberto Sanjuan](Alberto_Sanjuan "Alberto Sanjuan"), [CCC](CCC "CCC"), November 03, 2014 » [Fail-Low](Fail-Low "Fail-Low")

## 2015 ...

- [Parallel aspiration windows](http://www.talkchess.com/forum/viewtopic.php?t=57113) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella"), [CCC](CCC "CCC"), July 29, 2015
- [Restarting iterative deepening](http://www.talkchess.com/forum/viewtopic.php?t=58542) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 09, 2015 » [Fail-Low](Fail-Low "Fail-Low"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Dynamic aspiration window](http://www.talkchess.com/forum/viewtopic.php?t=60285) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), May 26, 2016
- [Aspiration Windows on the root search -- Determining margin](http://www.talkchess.com/forum/viewtopic.php?t=60402) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 08, 2016
- [Iterative Deepening Question](http://www.talkchess.com/forum/viewtopic.php?t=60916) by [David Cimbalista](index.php?title=David_Cimbalista&action=edit&redlink=1 "David Cimbalista (page does not exist)"), [CCC](CCC "CCC"), July 23, 2016 » [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration window with TT question](http://www.open-chess.org/viewtopic.php?f=5&t=2995) by [sandermvdb](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 01, 2016 » [Transposition Table](Transposition_Table "Transposition Table")

**2017 ...**

- [Conceptual question on aspiration windows](http://www.talkchess.com/forum/viewtopic.php?t=63706) by Jacob Wilkins, [CCC](CCC "CCC"), April 09, 2017
- [(I)ID and PV dropout](http://www.talkchess.com/forum/viewtopic.php?t=64321) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 17, 2017 » [Fail-Low](Fail-Low "Fail-Low"), [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening"), [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Aspiration window problem](http://www.talkchess.com/forum/viewtopic.php?t=65589) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), October 30, 2017
- [Re: Lazy SMP ideas](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68278&start=16) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), October 03, 2018 » [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Impact of Aspiration on tree size](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69627) by Frank Kopp, [CCC](CCC "CCC"), January 16, 2019

## 2020 ...

- [Are Aspiration Windows Worthless?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76115) by [Erik Madsen](Erik_Madsen "Erik Madsen"), [CCC](CCC "CCC"), December 20, 2020 » [MadChess](MadChess "MadChess")
- [Number of aspiration "windows" before full-width search?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78625) by [John Merlino](John_Merlino "John Merlino"), [CCC](CCC "CCC"), November 09, 2021
- [Aspiration Window Instability?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78910) by Gianni Casati, [CCC](CCC "CCC"), December 17, 2021

## External Links

- [Aspiration Windows](http://web.archive.org/web/20070705134903/www.seanet.com/%7Ebrucemo/topics/aspiration.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](Bruce_Moreland#Topics "Bruce Moreland")
- [Lecture notes for February 2, 1999 Variants of Alpha-Beta Search](https://www.ics.uci.edu/~eppstein/180a/990202b.html) by [David Eppstein](David_Eppstein "David Eppstein")
- [Aspiration from Wikipedia](https://en.wikipedia.org/wiki/Aspiration)
- [aspiration - Wiktionary](https://en.wiktionary.org/wiki/aspiration)
- [aspire - Wiktionary](https://en.wiktionary.org/wiki/aspire)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Gerhard Hoehme](Category:Gerhard_Hoehme "Category:Gerhard Hoehme") - The Non-Euclidean Window (1964), mixed technique / wood on canvas, [Art Museum](Category:Art_Museum_Bochum "Category:Art Museum Bochum"), [Bochum](https://en.wikipedia.org/wiki/Bochum), [North Rhine-Westphalia](https://en.wikipedia.org/wiki/North_Rhine-Westphalia), [Germany](https://en.wikipedia.org/wiki/Germany), Photo by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), October 30, 2016

**[Up one level](Alpha-Beta "Alpha-Beta")**

