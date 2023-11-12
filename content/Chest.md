---
title: Chest
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Chest**

\[ Marriage Chest Repair <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Chest**, (CHEST, CHEss problem analyST)

a [program for solving](Category:Problem "Category:Problem") orthodox [chess problems](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies"),
such as [checkmate](Checkmate "Checkmate"), [stalemate](Stalemate "Stalemate"), [helpmate](https://en.wikipedia.org/wiki/Helpmate), helpstalemate,
[selfmate](https://en.wikipedia.org/wiki/Selfmate) and selfstalemate in N
<a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Chest was developed since 1987, written in [ANSI C](C "C") by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [Holger Pause](index.php?title=Holger_Pause&action=edit&redlink=1 "Holger Pause (page does not exist)") and [Thomas Rakovsky](index.php?title=Thomas_Rakovsky&action=edit&redlink=1 "Thomas Rakovsky (page does not exist)"),
while Heiner Marxen already started with a [mate-in-two](https://en.wikipedia.org/wiki/Chess_problem#Types_of_problem) solver written in [Fortran II](Fortran "Fortran") in 1973
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Chest does not play chess, but proves shortest solutions or its absence. It was first released in December 1999 as [open source](Category:Open_Source "Category:Open Source")
<a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Description

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

## [Search](Search "Search")

The main tree [search](Search "Search") function, utilizing a [transposition table](Transposition_Table "Transposition Table"), is [recursive](Recursion "Recursion"), i.e. for a job of [depth](Depth "Depth") N this function does call itself several times with depth N-1,
and always performs "[iterative deepening](Iterative_Deepening "Iterative Deepening")", i.e. a job or subjob with a depth of 3 is first computed with a depth of 1, and if that fails, with a depth of 2 and if this also fails, with a depth of 3.

## [Board Representation](Board_Representation "Board Representation")

Chest uses a one-dimensional, [incremental updated](Incremental_Updates "Incremental Updates") 16x24 [mailbox](Mailbox "Mailbox") [board representation](Board_Representation "Board Representation") to not only apply [vector attacks](Vector_Attacks "Vector Attacks") but also to allow any legal displacement vector between two non-border squares to be added to any legal square without probing memory outside the 16x24 array.
Per [square](Squares "Squares"), Chest keeps distinct [piece type](Pieces#PieceTypeCoding "Pieces") and piece color, and further [piece-sets](Piece-Sets "Piece-Sets") of direct and indirect [attacking/defending pieces](Attack_and_Defend_Maps "Attack and Defend Maps"). The redundancy pays off, since the attack info greatly speeds up the [generation](Move_Generation "Move Generation") of [legal moves](Legal_Move "Legal Move").

## ChestUCI

**ChestUCI** by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)") <a id="cite-note-6" href="#cite-ref-6">[6]</a>,
is an [UCI](UCI "UCI") adapter written in [Delphi](Delphi "Delphi") for a slightly modified Chest 3.19 (closed source), to run it from any UCI capable [GUI](GUI "GUI") .

## See also

- [Checkmate](Checkmate "Checkmate")
- [Chess Problems, Compositions and Studies](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies")
- [CHREST](CHREST "CHREST")
- [Corresponding Squares](Corresponding_Squares "Corresponding Squares")
- [Mate-in-two](Mate-in-two "Mate-in-two")
- [Mate Search](Mate_Search "Mate Search")
- [Mater](Mater "Mater")
- [Proof-Number Search](Proof-Number_Search "Proof-Number Search")
- [Stalemate](Stalemate "Stalemate")

## Forum Posts

## 1999

- [CHEST 3.19 is available](https://www.stmintz.com/ccc/index.php?id=83247) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), December 18, 1999
- [Chest 3.19 is incredible!](https://www.stmintz.com/ccc/index.php?id=83526) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 20, 1999
- [1924 NY Chess Championship -- chest analyzed mates so far](https://www.stmintz.com/ccc/index.php?id=84584) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), December 27, 1999

## 2000 ...

- [Problem with CHEST](https://www.stmintz.com/ccc/index.php?id=85814) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 04, 2000
- [Who can help me with Chest (mate solver)](https://www.stmintz.com/ccc/index.php?id=125870) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), August 23, 2000
- [Re: Chest (German)](https://www.stmintz.com/ccc/index.php?id=173136) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), June 03, 2001
- [The program chest?](https://www.stmintz.com/ccc/index.php?id=192768) by Kees van Iersel, [CCC](CCC "CCC"), October 10, 2001
- [Nalimov's EGTBs (long post with code)](https://www.stmintz.com/ccc/index.php?id=192968) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), October 13, 2001 » [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
- [CHEST bugfix available](https://www.stmintz.com/ccc/index.php?id=228143) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), May 05, 2002
- [A new(?) technique to recognize draws](https://www.stmintz.com/ccc/index.php?id=233270) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), June 01, 2002 » [Corresponding Squares](Corresponding_Squares "Corresponding Squares"), [Repetitions](Repetitions "Repetitions")
- [´ChestUCI Ver.1.0´ - a new UCI-engine for the problem solver ´Chest´](https://www.stmintz.com/ccc/index.php?id=247557) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), August 24, 2002
- [About CHEST](https://www.stmintz.com/ccc/index.php?id=252628) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 18, 2002
- [CHEST vs. ALYBADIX](https://www.stmintz.com/ccc/index.php?id=261116) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), October 23, 2002 » [Alybadix](Alybadix "Alybadix")
- [Small Bug in Chest UCI](https://www.stmintz.com/ccc/index.php?id=366805) by Michael Drexel, [CCC](CCC "CCC"), May 23, 2004

## 2005 ...

- [ChestUCI 4.4 Update](https://www.stmintz.com/ccc/index.php?id=486713) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), February 14, 2006
- [Stunning Chest!](http://www.talkchess.com/forum/viewtopic.php?t=16205) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 02, 2007
- [ChestUCI 4.6](http://www.talkchess.com/forum/viewtopic.php?t=18500) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), December 22, 2007
- [ChestUCI v5.0 released](http://www.talkchess.com/forum/viewtopic.php?t=20008) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), March 05, 2008

## 2010 ...

- [ChestUCI Source Code](http://www.talkchess.com/forum/viewtopic.php?t=37092) by Louis Zulli, [CCC](CCC "CCC"), December 15, 2010
- [ChestUCI 5.2 update](http://www.talkchess.com/forum/viewtopic.php?t=38339) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), March 08, 2011
- [Re: Perft(3) from 1978, with a twist!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=41373&start=5) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), December 09, 2011 » [Perft](Perft "Perft")
- [Wanted: A successor to Chest](http://www.talkchess.com/forum/viewtopic.php?t=44185) by [Marek Soszynski](index.php?title=Marek_Soszynski&action=edit&redlink=1 "Marek Soszynski (page does not exist)"), [CCC](CCC "CCC"), June 25, 2012
- [CHEST anniversary!](http://www.talkchess.com/forum/viewtopic.php?t=54690) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), December 18, 2014

## 2015 ...

- [Add Chest to the elite software chess engines (good or bad?)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=54888&) by Jonathan Lee, [CCC](CCC "CCC"), January 07, 2015
- [Faster Forced Mate](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=64417&p=720744) by MikeGL, [CCC](CCC "CCC"), June 26, 2017
- [A mate suite to test multi-pv and new engines](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68146) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 06, 2018
- [Chest for Linux](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71806) by Canoike, [CCC](CCC "CCC"), September 12, 2019

## 2020 ...

- [To Franz Huber, Bug in ChestUCI5.2 ?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74427) by Paloma, [CCC](CCC "CCC"), July 09, 2020 » [Bláthy](Gustav#Longest_Problem "Gustav")

## External Links

## Chess Program

- [Chest: A Program for Solving Orthodox Chess Problems](http://turbotm.de/~heiner/Chess/chest.html) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen")

[Readme Long](http://turbotm.de/~heiner/Chess/README_LONG)

- [Program Projects](https://fhub.jimdofree.com/) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)")

## Misc

- [chest - Wiktionary](https://en.wiktionary.org/wiki/chest)
- [Chest (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Chest_(disambiguation)>)
- [Chest (furniture) from Wikipedia](<https://en.wikipedia.org/wiki/Chest_(furniture)>)
- [Chest of drawers from Wikipedia](https://en.wikipedia.org/wiki/Chest_of_drawers)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Re-glueing loose element of solid nut [marriage chest](https://en.wikipedia.org/wiki/Cassone) (prob. Italy, 19th century), Image by [Etan J. Tal](https://commons.wikimedia.org/wiki/User:Etan_J._Tal), July 19, 2011, [Category:Chests](https://commons.wikimedia.org/wiki/Category:Chests), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Chest - Readme Long](http://turbotm.de/~heiner/Chess/README_LONG)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: Perft(3) from 1978, with a twist!](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=41373&start=5) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), December 09, 2011
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [CHEST 3.19 is available](https://www.stmintz.com/ccc/index.php?id=83247) by [Heiner Marxen](Heiner_Marxen "Heiner Marxen"), [CCC](CCC "CCC"), December 18, 1999
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> Description based on [Readme Long](http://turbotm.de/~heiner/Chess/README_LONG)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: ChestUCI Source Code](http://www.talkchess.com/forum/viewtopic.php?t=37092&start=1) by [Franz Huber](index.php?title=Franz_Huber&action=edit&redlink=1 "Franz Huber (page does not exist)"), [CCC](CCC "CCC"), December 15, 2010

**[Up one level](Engines "Engines")**

