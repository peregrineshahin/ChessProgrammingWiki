---
title: Beaches
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Beaches**

\[.jpg) Chess at the Beach <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Beaches**, (BeachesChess)

a [WinBoard](WinBoard "WinBoard") compliant chess engine by [Robert Pope](Robert_Pope "Robert Pope"), written in [C++](Cpp "Cpp"), first mentioned and hosted by [Benny Antonsson](Benny_Antonsson "Benny Antonsson") in 2002 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
The later published source code with version history from 2006 until 2010 <a id="cite-note-3" href="#cite-ref-3">[3]</a> refers a [bitboard](Bitboards "Bitboards") engine - despite processing many of them per node, using 8-bit occupied state [rotated bitboard](Rotated_Bitboards "Rotated Bitboards") lookups for sliding pieces - the control structure of the [legal move generator](Move_Generation#Legal "Move Generation") and [evaluation](Evaluation "Evaluation") reminds more on a [mailbox](Mailbox "Mailbox") approach without [piece list](Piece-Lists "Piece-Lists").
Search is plain [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning") and [fractional ply decrements](Depth#FractionalPlies "Depth") with an conventional evaluation, taking [material](Material "Material") and [piece-square tables](Piece-Square_Tables "Piece-Square Tables") along with some [pawn structure](Pawn_Structure "Pawn Structure") and [king safety](King_Safety "King Safety") terms into account, as well the [population](Population_Count "Population Count") of ored aggregated attacks per side.

## See also

- [Abbess](Abbess "Abbess")

## Forum Posts

## 2002 ...

- [New WinBoard compatible engine - Beaches 0.96 by Robert Pope](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38196) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 16, 2002
- [New WinBoard compatible engine - Beaches 0.96 by Robert Pope](https://www.stmintz.com/ccc/index.php?id=240784) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [CCC](CCC "CCC"), July 16, 2002
- [New version of Beaches](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38849) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 04, 2002
- [BeaChes 1.2](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=39377) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 03, 2002
- [Beaches 1.5 download](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=40890) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), January 22, 2003

## 2005 ...

- [Beaches playing random moves](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=2476) by [Olivier Deville](Olivier_Deville "Olivier Deville"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), May 05, 2005
- [make/unmake](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4641) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), April 08, 2006 » [Unmake Move](Unmake_Move "Unmake Move")
- [WAC 109](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49273) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), June 17, 2008 » [Win at Chess](Win_at_Chess "Win at Chess")
- [0x88 engines](http://www.talkchess.com/forum/viewtopic.php?t=27680) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), May 01, 2009

## 2010 ...

- [Missing checkmates](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=51278) by [Robert Pope](Robert_Pope "Robert Pope"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 28, 2010
- [Beaches 1.20](http://www.talkchess.com/forum/viewtopic.php?t=57713) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), September 21, 2015

## External Links

## Chess Engine

- [BeachesChess](https://sites.google.com/site/beacheschess/)
- [Beaches](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/BEACHES/) compiled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [Beaches 2.32](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Beaches%202.32) in [CCRL 40/4](CCRL "CCRL")

## Misc

- [Beach from Wikipedia](https://en.wikipedia.org/wiki/Beach)
- [Beach (disambiguation) from Wikipedia](<https://en.wikipedia.org/wiki/Beach_(disambiguation)>)
- [beach - Wiktionary](https://en.wiktionary.org/wiki/beach)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Anything goes in [Santa Monica](https://en.wikipedia.org/wiki/Santa_Monica,_California) - strenuous upper arm workouts, playing on swings, or brain workouts in the form of chess matches, source: [Muscle Beach and Chess Beach, Santa Monica](https://www.flickr.com/photos/skinnylawyer/5847210301/), [Image](<https://commons.wikimedia.org/wiki/File:Muscle_Beach_and_Chess_Beach,_Santa_Monica_(5847210301).jpg>) by [InSapphoWeTrust](https://www.flickr.com/people/56619626@N05?rb=1), June 18, 2011, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/deed.en), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New WinBoard compatible engine - Beaches 0.96 by Robert Pope](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=38196) by [Benny Antonsson](Benny_Antonsson "Benny Antonsson"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 16, 2002
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [BeachesChess](https://sites.google.com/site/beacheschess/), Here is the source code of a slightly later version of Beaches (2.32)

**[Up one Level](Engines "Engines")**

