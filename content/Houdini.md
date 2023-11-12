---
title: Houdini
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Houdini**

\[ [Houdini](https://en.wikipedia.org/wiki/Harry_Houdini) in "[The Grim Game](https://en.wikipedia.org/wiki/The_Grim_Game)" [[1]](#cite_note-1)
**Houdini**,

a chess engine by [Robert Houdart](Robert_Houdart "Robert Houdart"), which appeared in 2010 as closed source engine, free for non-commercial use. In January 2011, Houdini **1.5** was leading [Ingo Bauer's](Ingo_Bauer "Ingo Bauer") [IPON](IPON "IPON") [rating list](Engine_Rating_Lists "Engine Rating Lists") [[2]](#cite_note-2). Houdini **2**, released in September 2011, is commercial and bundled with a number of [ChessOK](ChessOK "ChessOK") products, such as [Aquarium](Aquarium "Aquarium"), [Chess Assistant](Chess_Assistant "Chess Assistant") [[3]](#cite_note-3), and since December 2011, [Chess King](index.php?title=Chess_King&action=edit&redlink=1 "Chess King (page does not exist)") [[4]](#cite_note-4). Houdini 1.5a remains available as a free download [[5]](#cite_note-5). Houdini **3**, released in October 2012, has further improved by more than 50 Elo points [[6]](#cite_note-6). According to its author, Houdini 3 applies a accelerated [principal variation search](Principal_Variation_Search "Principal Variation Search"), also dubbed "Smart" [Fail-High](Fail-High "Fail-High"). If a different move becomes [best](Best_Move "Best Move") at very high [search depths](Depth "Depth") at the [root](Root "Root"), re-searches to determine its [exact score](Exact_Score "Exact Score") and the new [principal variation](Principal_Variation "Principal Variation") are done faster due to a reduced search depth, presumably in conjunction with [extensions](Extensions "Extensions") along the PV [[7]](#cite_note-7). Since November 2012, Houdini 3 is available as [ChessBase](ChessBase "ChessBase") engine [[8]](#cite_note-8) . Houdini **4**, released in November 2013, was about 50 Elo stronger than its predecessor, and features 6-men [Syzygy bases](Syzygy_Bases "Syzygy Bases").

## Houdini 5

Released about three years after the previous version, in November 2016, **Houdini 5** is vastly improved being about 200 Elo stronger than Houdini 4. It has a completely rewritten [evaluation](Evaluation "Evaluation") with more aggressive [king safety](King_Safety "King Safety") and sophisticated [piece mobility](Mobility "Mobility"), features a more [selective](Selectivity "Selectivity") [search](Search "Search"), exploring critical variations significantly deeper, and for hardware with multiple processors, [Lazy SMP](Lazy_SMP "Lazy SMP"). Houdini **5 Pro** supports up to 128 [threads](Thread "Thread"), up to 128 GiB of [hash memory](Shared_Hash_Table "Shared Hash Table"), [large memory pages](Memory#HugePages "Memory"), [NUMA-architecture](NUMA "NUMA"), and [Nalimov tablebases](Nalimov_Tablebases "Nalimov Tablebases") to find the shortest path to [mate](Checkmate "Checkmate").

A development version of Houdini 5 qualified for [TCEC Season 9 Superfinal](TCEC_Season_9#Superfinal "TCEC Season 9"), and even won the [TCEC Season 9 Rapid tournament](TCEC_Season_9#Rapid "TCEC Season 9"). The final release version of Houdini 5 is about 30 Elo stronger than the engine that played in the TCEC tournament so far. But that was apparently not enough for [Stockfish 8](Stockfish "Stockfish") in long time control matches - Houdini 5 lost the 100 game [Superfinal](TCEC_Season_9#Superfinal "TCEC Season 9") with 45½ - 54½.

## Houdini 6

Released in September 2017, Houdini **6** again improved in [search](Search "Search") and [evaluation](Evaluation "Evaluation") to add another 50-60 Elo in [strength](Playing_Strength "Playing Strength"), which roughly corresponds to doubling the computational power of the computer [[9]](#cite_note-9). **Houdini 6.03** won the [TCEC Season 10 Superfinal](TCEC_Season_10#Superfinal "TCEC Season 10") versus [Komodo 1970.00](Komodo "Komodo"), a successor of Komodo 11, with **53 - 47** (+15=76-9) [[10]](#cite_note-10) [[11]](#cite_note-11).

## Houdini's Origin

Robert Houdart claims his engine is original [[12]](#cite_note-12), and admits taking ideas from the open source programs [Ippolit](Ippolit "Ippolit")/[Robbolito](RobboLito "RobboLito"), [Stockfish](Stockfish "Stockfish") and [Crafty](Crafty "Crafty") [[13]](#cite_note-13) . Other programmers and forum members raised suspicions that Robert took ideas from the controversial Ippolit/Robbolito source code too literally as initial base of his program [[14]](#cite_note-14) [[15]](#cite_note-15) [[16]](#cite_note-16) [[17]](#cite_note-17).

## Sources of Inspiration

Robert Houdart on the origins of Houdini in [CCC](CCC "CCC"), June 08, 2010 [[18]](#cite_note-18)

```C++
From the start I have very clearly acknowledged the different sources of inspiration for Houdini ([Ippo/Robbo](Ippolit "Ippolit"), [Stockfish](Stockfish "Stockfish") and [Crafty](Crafty "Crafty")) and have shown every respect for the hard work of others, be it on my web site, in the readme file, or in this forum ...

```

```C++
Houdini and the Ippo family have lots of high-level similarities, but zillions of low-level subtle differences.

Claims have been made that I "just changed a couple of resource strings", "made a cheap compile" or "grabbed some free code", but, in truth, none of you have any clue about the effort that was invested in Houdini.

```

```C++
It is funny that I would not be called a "real" chess engine author, when I am both a professional software developer and a reasonably strong chess player (peak 2280 rating), who has been writing chess engines for over 25 years now in a variety of programming languages.

```

```C++
It is sad that on the one hand you request that everybody demonstrates respect for the hard work of others, but on the other hand you seem to be unable to extend the same courtesy (or even the benefit of the doubt) to Houdini. 

```

## Material Table

The idea to index the [material table](Material_Tables "Material Tables") in the same manner as [Robbolito](RobboLito "RobboLito"), with combined counters of queens, rooks, light and dark bishops, knights and pawns, and to calculate piece counters from that table-index by a sequence of mod/div operations by {2,2,3,3,2,2,2,2,3,3,9,9} might be considered obvious after studying the mentioned source code, and if applying that scheme, there is hardly anything to avoid a sequence of almost identical [x86](X86 "X86") machine code with same constants for [reciprocal multiplication](General_Setwise_Operations#ReciprocalMultiplication "General Setwise Operations") [[19]](#cite_note-19).

## Strelka 5

Robert Houdart on [Strelka 5](Strelka "Strelka"), December 04, 2011 [[20]](#cite_note-20)

```C++
Strelka 5 is Houdini 1.5 [RE](https://en.wikipedia.org/wiki/Reverse_engineering), not Houdini 2. I share your fears, any #1 engine will be RE'd in a matter of months. For Houdini 1.5 it's taken about 6 months. 

```

Reply by [Richard Vida](Richard_Vida "Richard Vida") [[21]](#cite_note-21)

```C++
You mean 6 months until [Strelka](Strelka "Strelka") has been released to public. You do not know how much time did [Yuri Osipov](Jury_Osipov "Jury Osipov") spent on RE, neither when he did start his RE project. For me it took barely one week. As [Milos S.](Milos_Stanisavljevic "Milos Stanisavljevic") pointed out [[22]](#cite_note-22) , you made RE very very easy because of starting your project from [Robbolito](RobboLito "RobboLito") codebase... Personally I see no problem with that (other than you not telling the truth). 

```

## Stockfish

In March 2020, an anonymous poster who came into possession of Houdini 6's source code, apparently due to access to a [subversion](https://en.wikipedia.org/wiki/Apache_Subversion) server owned by Robert Houdart, claimed Houdini 5 and 6 were [Stockfish](Stockfish "Stockfish") derivatives [[23]](#cite_note-23) [[24]](#cite_note-24). In summer 2021, the Stockfish team filed a [lawsuit](https://en.wikipedia.org/wiki/Lawsuit) against [ChessBase](ChessBase "ChessBase") to enforce the consequences of the license termination concerning [Fat Fritz 2](Fat_Fritz#Fat_Fritz_2 "Fat Fritz") and the allegedly Stockfish derivative Houdini 6 sold by ChessBase [[25]](#cite_note-25) [[26]](#cite_note-26) [[27]](#cite_note-27).

## Release Dates

- Houdini 1.0 : May 15, 2010
- Houdini 1.5 : December 15, 2010
- Houdini 2.0 : September 01, 2011
- Houdini 3 : October 15, 2012
- Houdini 4 : November 25, 2013
- Houdini 5: November 09, 2016
- Houdini 6: September 17, 2017

## Publications

## Chess Engine

- [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2012**). *Determining the Strength of Chess Players based on actual Play*. [ICGA Journal, Vol. 35, No. 1](ICGA_Journal#35_1 "ICGA Journal") » [Playing Strength](Playing_Strength "Playing Strength")
- [Arno Nickel](Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) [[28]](#cite_note-28)
- [Matej Guid](Matej_Guid "Matej Guid"), [Ivan Bratko](Ivan_Bratko "Ivan Bratko") (**2012**). *Detecting Fortresses in Chess*. [Elektrotehniški vestnik](http://ev.fe.uni-lj.si/), Vol. 79, Nos. 1-2, [pdf](https://ailab.si/matej/doc/Detecting_Fortresses_in_Chess.pdf) » [Fortress](Fortress "Fortress"), [Rybka](Rybka "Rybka"), Houdini
- [Diogo R. Ferreira](Diogo_R._Ferreira "Diogo R. Ferreira") (**2013**). *The Impact of the Search Depth on Chess Playing Strength*. [ICGA Journal, Vol. 36, No. 2](ICGA_Journal#36_2 "ICGA Journal") » [Depth](Depth "Depth"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength") [[29]](#cite_note-29)

## Harry Houdini

- [Harry Houdini](https://en.wikipedia.org/wiki/Harry_Houdini), et al. (**1906, 2012**). *[The Right Way to Do Wrong: An Exposé of Successful Criminals](https://books.google.com/books?id=j5_XHZImTqcC&printsec=frontcover)*. [CreateSpace](http://de.wikipedia.org/wiki/CreateSpace.com), [amazon.com](http://www.amazon.com/The-Right-Way-Wrong-Successful/dp/1481157647)

[Harry Houdini](https://en.wikipedia.org/wiki/Harry_Houdini) (**2007**). *[The Right Way to Do Wrong](https://archive.org/details/right_way_to_do_wrong_lah_librivox)*. [Librivox audio recording](https://en.wikipedia.org/wiki/LibriVox) from the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive)

- [Harry Houdini](https://en.wikipedia.org/wiki/Harry_Houdini), [Harry Houdini Collection](http://www.loc.gov/rr/rarebook/coll/122.html) (**1908**). *[The unmasking of Robert-Houdin](https://archive.org/details/unmaskingrobert00houdgoog)*. New York : Publishers Printing Co. [[30]](#cite_note-30)
- [Walter Brown Gibson](https://en.wikipedia.org/wiki/Walter_B._Gibson), [Morris N. Young](http://archives.library.illinois.edu/archon/?p=creators/creator&id=2380) (**1953**). *[Houdini on Magic](https://books.google.com/books?id=WqAlWYtemkIC)*. [Dover Publications](https://en.wikipedia.org/wiki/Dover_Publications)

## Postings

## 2010 ...

- [Re: Costeff Study 1979](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=348905&t=34326) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), May 16, 2010
- [Introducing Houdini, a new, strong UCI chess engine](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=34333) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), May 16, 2010
- [Houdini - a cheap compile of Ippo/Robo](http://www.talkchess.com/forum/viewtopic.php?t=34578) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC - Computer Chess Club: Engine Origins](CCC "CCC"), May 29, 2010 (requires login)
- [Re: question on draw evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=354023&t=34673) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), June 07, 2010 » [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
- [Houdini 1.03 is available](http://www.talkchess.com/forum/viewtopic.php?t=35453) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), July 15, 2010
- [Re: Mate in 17 revisited](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=361912&t=35338) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), July 16, 2010 » [Zugzwang](Zugzwang "Zugzwang")
- [Houdini 1.03a bug-fix is available](http://www.talkchess.com/forum/viewtopic.php?t=35469) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), July 17, 2010
- [Houdini 1.03a tests](http://www.talkchess.com/forum/viewtopic.php?t=35497) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), July 18, 2010
- [Why Is Houdini Not Entered In The WCCC??](http://www.open-chess.org/viewtopic.php?f=3&t=534) by Sean Evans, [Open Chess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 03, 2010
- [Re: Plain and fancy magic on modern hardware](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=368026&t=35858) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), August 26, 2010 » [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Gaviota EGTB in Houdini 1.5 + contacting Eugene Nalimov](http://www.talkchess.com/forum/viewtopic.php?t=36886) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 01, 2010
- [Houdini 1.5 is released](http://www.talkchess.com/forum/viewtopic.php?t=37091) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 15, 2010
- [Houdini 1.5 with Large Page support and 8-cores for w32](http://www.talkchess.com/forum/viewtopic.php?t=37175) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 19, 2010
- [Houdini 1.5: one mystery/question](http://www.talkchess.com/forum/viewtopic.php?t=37206) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 21, 2010
- [Houdini and Chessbase GUI engine matches](http://www.talkchess.com/forum/viewtopic.php?t=37311) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 27, 2010

**2011**

- [Houdini Engine Origins](http://open-chess.org/viewtopic.php?f=7&t=992) by [Jeremy Bernstein](Jeremy_Bernstein "Jeremy Bernstein"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 18, 2011
- [a Telltale position](http://www.talkchess.com/forum/viewtopic.php?t=38052) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), 12 February, 2011
- [Re: Why are the Ippo derivative stronger than Stockfish?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=396662&t=38198) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), 25 February, 2011
- [Re: Hash usage percent display (in Arena)](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=400730&t=38535) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), March 24, 2011
- [Re: Houdini, Fire, IvanHoe, (and Rybka?) are 'clones'...?](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=406820&t=38932) by [Jury Osipov](Jury_Osipov "Jury Osipov"), [CCC](CCC "CCC"), May 12, 2011
- [Some news about Houdini 2.0](http://www.talkchess.com/forum/viewtopic.php?t=39812) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), July 22, 2011
- [Houdini 2 is released](http://www.talkchess.com/forum/viewtopic.php?t=40245) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), September 02, 2011
- [Houdini 2 Aquarium released](http://www.talkchess.com/forum/viewtopic.php?t=40673) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), October 09, 2011
- [Computer Chess Biggest Liar](http://www.open-chess.org/viewtopic.php?f=3&t=1647) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), October 09, 2011
- [how far is too far: houdini for sell?](http://www.talkchess.com/forum/viewtopic.php?t=40709) by Joseph, [CCC](CCC "CCC"), October 11, 2011
- [Houdini with 1:1 Robbolito-code?](http://www.talkchess.com/forum/viewtopic.php?t=40728) by [Dr. Alexander Schmidt](index.php?title=Dr._Alexander_Schmidt&action=edit&redlink=1 "Dr. Alexander Schmidt (page does not exist)"), [CCC](CCC "CCC"), October 12, 2011

[Re: Houdini with 1:1 Robbolito-code?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=428534&t=40728) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), October 12, 2011

- [Strelka 5 by Yuriy Osipov](http://www.talkchess.com/forum/viewtopic.php?t=40777) by Slavik Pavloff, [CCC](CCC "CCC"), October 15, 2011 » [Strelka](Strelka "Strelka")
- [New:Houdini 2 Chess Benchmarks are Acceptable!](http://www.talkchess.com/forum/viewtopic.php?t=41221) by [Sedat Canbaz](index.php?title=Sedat_Canbaz&action=edit&redlink=1 "Sedat Canbaz (page does not exist)"), [CCC](CCC "CCC"), November 26, 2011
- [Re: Any plans for Houdini 3?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=436153&t=41313) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 03, 2011
- [Re: Komodo 4 on long time control](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=436498&t=41272) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), December 04, 2011 » [Komodo](Komodo "Komodo"), [Strelka](Strelka "Strelka")
- [Houdini 2.0c - Mate in 1 bug](http://www.talkchess.com/forum/viewtopic.php?t=41375) by [Árpád Rusz](%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [CCC](CCC "CCC"), December 08, 2011

**2012**

- [Re: Interesting poll](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=427014#pid427014) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 15, 2012
- [Houdini 3 reducing the depth feature](http://www.talkchess.com/forum/viewtopic.php?t=45624) by Maurizio Maglio, [CCC](CCC "CCC"), October 17, 2012
- [Houdini 3 does not behave the same in 64-bit and 32-bit](http://www.talkchess.com/forum/viewtopic.php?t=45697) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), October 23, 2012
- [houdini3 search and mate scores](http://www.talkchess.com/forum/viewtopic.php?t=45768) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 29, 2012 » [Mate Scores](Score#MateScores "Score")
- [Houdini 3 update does behave the same in 64-bit and 32-bit](http://www.talkchess.com/forum/viewtopic.php?t=45816) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), November 01, 2012
- [What is stronger than Houdini 3 for what?](http://www.talkchess.com/forum/viewtopic.php?t=45948) by S.Taylor, [CCC](CCC "CCC"), November 11, 2012
- [Houdini 3 tests (8cpu)](http://www.talkchess.com/forum/viewtopic.php?t=45961) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), November 12, 2012
- [The scaling of Houdini 3 and Komodo 5](http://www.talkchess.com/forum/viewtopic.php?t=46019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 16, 2012 » [Komodo](Komodo "Komodo")
- [Houdini 3-Houdini 3: Nutzen der Bedenkzeitverlängerung](http://forum.computerschach.de/cgi-bin/mwf/topic_show.pl?tid=5184) by Patrick Götz, [CSS-Forum](Computer_Chess_Forums "Computer Chess Forums"), December 07, 2012 (German) » [Diminishing Returns](Depth#DiminishingReturns "Depth")
- [Houdini 3 the same in 64-bit and 32-bit: well, not quite?](http://www.talkchess.com/forum/viewtopic.php?t=46182) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), November 28, 2012

**2013**

- [10 Lessons to be Learned from todays Top Engines](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=26392) by Josef, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2013 » [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
- [eval scale in Houdini](http://www.talkchess.com/forum/viewtopic.php?t=46879) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), January 14, 2013 » [Evaluation](Evaluation "Evaluation")
- [Scaling at 2x nodes (or doubling time control)](http://www.talkchess.com/forum/viewtopic.php?t=48733) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 23, 2013 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), Houdini
- [Houdini 4 has been released](http://www.talkchess.com/forum/viewtopic.php?t=50224) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), November 25, 2013
- [Houdini, much weaker engines, and Arpad Elo](http://www.talkchess.com/forum/viewtopic.php?t=50266) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 29, 2013 » [Match Statistics](Match_Statistics "Match Statistics"), [Pawn Advantage, Win Percentage, and ELO](index.php?title=Pawn_Advantage,_Win_Percentage,_and_ELO&action=edit&redlink=1 "Pawn Advantage, Win Percentage, and ELO (page does not exist)") [[31]](#cite_note-31)
- [IPON results for Houdini 4](http://www.talkchess.com/forum/viewtopic.php?t=50304) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 02, 2013 » [IPON](IPON "IPON")
- [Be careful where you buy Houdini 4, or you could get burned](http://www.talkchess.com/forum/viewtopic.php?t=50340) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), December 05, 2013

**2014**

- [Houdini 3/4?](http://www.talkchess.com/forum/viewtopic.php?t=51107) by Jason Coombs, [CCC](CCC "CCC"), January 30, 2014
- [Threads factor: Komodo, Houdini, Stockfish and Zappa](http://www.talkchess.com/forum/viewtopic.php?p=570955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 17, 2014 » [Thread](Thread "Thread"), [Komodo](Komodo "Komodo"), Houdini, [Stockfish](Stockfish "Stockfish"), [Zappa](Zappa "Zappa")

## 2015 ...

- [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting")

**2016**

- [Houdini 5 in TCEC](http://www.talkchess.com/forum/viewtopic.php?t=59849) by John Wentworth, [CCC](CCC "CCC"), April 13, 2016 » [TCEC Season 9](TCEC_Season_9 "TCEC Season 9") [[32]](#cite_note-32)
- [Houdini 5 dev in TCEC](http://www.talkchess.com/forum/viewtopic.php?t=61357) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 08, 2016 » [TCEC Season 9](TCEC_Season_9 "TCEC Season 9")
- [New Houdini](http://www.talkchess.com/forum/viewtopic.php?t=61611) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 05, 2016
- [Houdini 5 has been released](http://www.talkchess.com/forum/viewtopic.php?t=62035) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), November 09, 2016
- [chessbase houdini is out but...](http://www.talkchess.com/forum/viewtopic.php?t=62366) by Stavros Atmatzidis, [CCC](CCC "CCC"), December 03, 2016

**2017**

- [Houdini 6 has been released](http://www.talkchess.com/forum/viewtopic.php?t=65211) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), September 18, 2017
- [Scaling from FGRL results with top 3 engines](http://www.talkchess.com/forum/viewtopic.php?t=65288) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 26, 2017 » [FGRL](FGRL "FGRL"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish")
- [Re: Houdini 6.02](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65360&start=3) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), October 02, 2017
- [Houdini 6.03 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65782) by Christian Goralski, [CCC](CCC "CCC"), November 20, 2017
- [Whatever happened to Houdini for Android?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65783) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), November 21, 2017

**2018**

- [Houdini 6 - Initial position until depth 50](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67097) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), April 13, 2018 » [Initial Position](Initial_Position "Initial Position")

## 2020 ...

- [Houdini is a Stockfish Derivative (and started life as a Robbolito derivative)](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=73433) by cucumber, [CCC](CCC "CCC") (Engine Origins requires registration), March 22, 2020
- [Houdini is a clone of Stockfish 8](https://groups.google.com/d/msg/fishcooking/DygaIdBvJm0/cjtMosvdBQAJ) by c9publice...@gmail.com, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2020
- [An Old Engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73630) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), April 11, 2020
- [Re: Is cloning a hobby?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75040&start=44) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 17, 2020
- [Our lawsuit against ChessBase](https://stockfishchess.org/blog/2021/our-lawsuit-against-chessbase/), [The Stockfish Team](Stockfish "Stockfish"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2021 » [ChessBase](ChessBase "ChessBase"), [Fat Fritz 2](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
- [Re: Stockfish: Our lawsuit against ChessBase](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77762&start=239) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 24, 2021

## External Links

## Chess Engine

- [Houdini Chess Engine](http://www.cruxis.com/chess/houdini.htm)
- [Houdini Chess Engine](https://web.archive.org/web/20100519120411/http://www.cruxis.com/chess/houdini.htm) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), May 19, 2010)
- [Houdini (chess) from Wikipedia](https://en.wikipedia.org/wiki/Houdini_%28chess%29)

### Purchase

- [Houdini 6 Pro](https://shop.chessbase.com/en/products/houdini_6_pro_multiprocessor_version) [ChessBase Shop](ChessBase "ChessBase"), September 17, 2017
- [Houdini 5 Pro](https://shop.chessbase.com/en/products/houdini_5_pro_multiprocessor_version) [ChessBase Shop](ChessBase "ChessBase"), December 02, 2016
- [Houdini 6 and Aquarium 2018](https://shop.chessok.com/index.php?Home=index&cPath=7_56), [ChessOK](ChessOK "ChessOK") » [Aquarium](Aquarium "Aquarium")

### Interviews

- [Interview of Robert Houdart, the Creator of the Strongest Chess Engine in the world: Houdini](http://chess-king.com/images/kingintromaterials/HoudartInterview/InterviewHoudiniA.pdf) (pdf), [chess-king.com](http://chess-king.com/)
- [Houdini 3 – the world's strongest chess engine in the Fritz interface - Interview with Robert Houdart, author of Houdini](https://en.chessbase.com/post/houdini-3-the-world-s-strongest-che-engine-in-the-fritz-interface), [ChessBase News](ChessBase "ChessBase"), October 29, 2012
- [Robert Houdart on Houdini 5 dev in TCEC](http://www.chessdom.com/robert-houdart-on-houdini-5-dev-in-tcec/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), August 25, 2016 » [TCEC Season 9](TCEC_Season_9 "TCEC Season 9")
- [Interview with Robert Houdart, Mark Lefler and GM Larry Kaufman](http://www.chessdom.com/interview-with-robert-houdart-mark-lefler-and-gm-larry-kaufman/) by [Nelson Hernandez](Nelson_Hernandez "Nelson Hernandez"), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), November 23, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")
- [Interview with Robert Houdart, author of the champion engine Houdini](http://www.chessdom.com/interview-with-robert-houdart-author-of-the-champion-engine-houdini/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), December 08, 2017

### Reports

- [New: Houdini 6 | ChessBase](https://en.chessbase.com/post/neu-houdini-6), [ChessBase News](ChessBase "ChessBase"), October 18, 2017
- [Houdini 3: the new king of the block (part one)](https://en.chessbase.com/post/houdini-3-the-new-king-of-the-block-part-one-) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), November 13, 2012
- [Houdini 3: Analyzing in the cloud (part two)](https://en.chessbase.com/post/houdini-3-analyzing-in-the-cloud-part-two-) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), November 17, 2012
- [Houdini 4: the 800-pound gorilla](https://en.chessbase.com/post/houdini-4-the-800-pound-gorilla-2), [ChessBase News](ChessBase "ChessBase"), December 07, 2013
- [One chess champion per laptop](https://thetech.com/2014/01/15/chess-v133-n62) by [Roberto Perez-Franco](http://www.mit.edu/~roberto/), [MIT's](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") [The Tech](https://en.wikipedia.org/wiki/The_Tech_%28newspaper%29), January 15, 2014 » [TCEC Season 5](TCEC_Season_5 "TCEC Season 5")
- [Houdini 5 to participate in TCEC Season 9](http://www.chessdom.com/houdini-5-to-participate-in-tcec-season-9/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), April 13, 2016 » [TCEC Season 9](TCEC_Season_9 "TCEC Season 9")
- [Houdini 5's Tactical Mode: Releasing the Kraken](https://en.chessbase.com/post/houdini5tacticalmode) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), December 08, 2016
- [Fair play in engine chess](https://en.chessbase.com/post/fair-play-in-engine-match), [ChessBase News](ChessBase "ChessBase"), December 30, 2016 » [Houdini 5](Houdini#5 "Houdini"), [Komodo 10](Komodo#10 "Komodo")
- [TCEC: Superfinal Houdini vs Komodo](https://en.chessbase.com/post/tcec-superfinal-houdini-vs-komodo) by [Stephan Oliver Platz](index.php?title=Stephan_Oliver_Platz&action=edit&redlink=1 "Stephan Oliver Platz (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), November 23, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")
- [Houdini is TCEC Season 10 champion!](http://www.chessdom.com/houdini-is-tcec-season-10-champion/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), December 07, 2017
- [Houdini wins TCEC Superfinal](https://en.chessbase.com/post/houdini-wins-the-tcec-superfinal) by [Stephan Oliver Platz](index.php?title=Stephan_Oliver_Platz&action=edit&redlink=1 "Stephan Oliver Platz (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), December 13, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")
- [10 years Houdini](https://en.chessbase.com/post/10-years-houdini) by [Stephan Oliver Platz](index.php?title=Stephan_Oliver_Platz&action=edit&redlink=1 "Stephan Oliver Platz (page does not exist)"), [ChessBase News](ChessBase "ChessBase"), June 30, 2020

### Rating Lists

- [Houdini](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Houdini&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")
- [Houdini 6 64-bit 4CPU](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Houdini%206%2064-bit%204CPU#Houdini_6_64-bit_4CPU) in [CCRL 40/40](CCRL "CCRL")

## Harry Houdini

- [Harry Houdini from Wikipedia](https://en.wikipedia.org/wiki/Harry_Houdini)
- [Harry Houdini - The Life of Harry Houdini](https://www.thegreatharryhoudini.com/)
- [Harry Houdini Collection](http://www.loc.gov/rr/rarebook/coll/122.html)
- [Harry Houdini Biography - Facts, Birthday, Life Story - Biography.com](https://www.biography.com/people/harry-houdini-40056)

## References

1. [↑](#cite_ref-1) [The Grim Game](https://en.wikipedia.org/wiki/The_Grim_Game) a 1919 [silent film](https://en.wikipedia.org/wiki/Silent_film) starring [Harry Houdini](https://en.wikipedia.org/wiki/Harry_Houdini)
1. [↑](#cite_ref-2) [IPON-Rating-List Archive 2009/2010/2011](http://www.inwoba.de/News2009_2011.7z) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer")
1. [↑](#cite_ref-3) [Houdini 2 Aquarium products family has been released!](http://chessok.com/?p=25808), [ChessOK](ChessOK "ChessOK"), October 07, 2011
1. [↑](#cite_ref-4) [Chess King Released](http://chessok.com/?p=26441), [ChessOK](ChessOK "ChessOK"), December 14, 2011
1. [↑](#cite_ref-5) [Re: Houdini 2 is released](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=421920&t=40245) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), September 02, 2011
1. [↑](#cite_ref-6) [IPON-Rating-List, 2012.10.17](http://www.inwoba.de/index.html) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer")
1. [↑](#cite_ref-7) [Re: Houdini 3 reducing the depth feature](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=488422&t=45624) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), October 19, 2012
1. [↑](#cite_ref-8) [Houdini 3 Standard multiprocessor version](http://chessbase-shop.com/en/products/houdini_3_standard_multiprocessor_version), [ChessBase Shop](ChessBase "ChessBase")
1. [↑](#cite_ref-9) [Houdini Chess Engine](http://www.cruxis.com/chess/houdini.htm)
1. [↑](#cite_ref-10) [Houdini is TCEC Season 10 champion!](http://www.chessdom.com/houdini-is-tcec-season-10-champion/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), December 07, 2017
1. [↑](#cite_ref-11) [Interview with Robert Houdart, author of the champion engine Houdini](http://www.chessdom.com/interview-with-robert-houdart-author-of-the-champion-engine-houdini/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), December 08, 2017
1. [↑](#cite_ref-12) [Re: Why Is Houdini Not Entered In The WCCC??](http://www.open-chess.org/viewtopic.php?f=3&t=534&start=20#p4798) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [Open Chess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 04, 2010
1. [↑](#cite_ref-13) [Houdini Chess Engine - Acknowledgements](http://www.cruxis.com/chess/houdini.htm)
1. [↑](#cite_ref-14) [Re: Why Is Houdini Not Entered In The WCCC??](http://www.open-chess.org/viewtopic.php?f=3&t=534&start=40#p5084) by [kingliveson](Franklin_Titus "Franklin Titus"), [Open Chess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 09, 2010
1. [↑](#cite_ref-15) [Re: Why Is Houdini Not Entered In The WCCC??](http://www.open-chess.org/viewtopic.php?f=3&t=534&start=40#p5089) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [Open Chess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 10, 2010
1. [↑](#cite_ref-16) [Re: Computer Chess Biggest Liar](http://www.open-chess.org/viewtopic.php?f=3&t=1647&start=10#p14724) by [kingliveson](Franklin_Titus "Franklin Titus"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), October 11, 2011
1. [↑](#cite_ref-17) [Re: Interesting poll](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?pid=427014#pid427014) by [Rebel](Ed_Schroder "Ed Schroder"), [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), July 15, 2012
1. [↑](#cite_ref-18) [Re: Purpose of Chess Engine Origins forum is...?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=354245&t=34770) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC") (Computer Chess Club: Engine Origins, requires registration), June 08, 2010 in a reply to [Jeremy Bernstein](Jeremy_Bernstein "Jeremy Bernstein")
1. [↑](#cite_ref-19) [Houdini - a cheap compile of Ippo/Robo](http://www.talkchess.com/forum/viewtopic.php?t=34578) by [Lance Perkins](Lance_Perkins "Lance Perkins"), [CCC - Computer Chess Club: Engine Origins](CCC "CCC"), May 29, 2010 (requires login)
1. [↑](#cite_ref-20) [Re: Komodo 4 on long time control](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=436467&t=41272) by [Robert Houdart](Robert_Houdart "Robert Houdart"), [CCC](CCC "CCC"), December 04, 2011
1. [↑](#cite_ref-21) [Re: Komodo 4 on long time control](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=436498&t=41272) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), December 04, 2011
1. [↑](#cite_ref-22) [Re: Lazy eval - test results](http://talkchess.com/forum/viewtopic.php?topic_view=threads&p=435775&t=41236) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), December 01, 2011
1. [↑](#cite_ref-23) [Houdini is a Stockfish Derivative (and started life as a Robbolito derivative)](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=73433) by cucumber, [CCC](CCC "CCC") (Engine Origins requires registration), March 22, 2020
1. [↑](#cite_ref-24) [Houdini is a clone of Stockfish 8](https://groups.google.com/d/msg/fishcooking/DygaIdBvJm0/cjtMosvdBQAJ) by c9publice...@gmail.com, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), March 26, 2020
1. [↑](#cite_ref-25) [Our lawsuit against ChessBase](https://stockfishchess.org/blog/2021/our-lawsuit-against-chessbase/), [The Stockfish team](Stockfish "Stockfish"), [Stockfish Blog](Computer_Chess_Forums "Computer Chess Forums"), July 20, 2021
1. [↑](#cite_ref-26) [Re: Stockfish: Our lawsuit against ChessBase](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77762&start=239) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), July 24, 2021
1. [↑](#cite_ref-27) [GitHub - crossopterygian/Houdini_6: uci chess engine](https://github.com/crossopterygian/Houdini_6)
1. [↑](#cite_ref-28) Part 1 covers Houdini, [Rybka](Rybka "Rybka"), [Komodo](Komodo "Komodo"), [Stockfish](Stockfish "Stockfish"), [Critter](Critter "Critter"), [Naum](Naum "Naum"), [Chiron](Chiron "Chiron") and [Spike](Spike "Spike")
1. [↑](#cite_ref-29) [Ply versus ELO](https://www.hiarcs.net/forums/viewtopic.php?t=10004) by Greg, [HIARCS Forum](Computer_Chess_Forums "Computer Chess Forums"), May 30, 2020 » [Diogo R. Ferreira - Impact of the Search Depth ...](Diogo_R._Ferreira#Impact "Diogo R. Ferreira")
1. [↑](#cite_ref-30) [Jean Eugène Robert-Houdin - Wikipedia](https://en.wikipedia.org/wiki/Jean_Eug%C3%A8ne_Robert-Houdin)
1. [↑](#cite_ref-31) [Arpad Elo - Wikipedia](https://en.wikipedia.org/wiki/Arpad_Elo)
1. [↑](#cite_ref-32) [Houdini 5 to participate in TCEC Season 9](http://www.chessdom.com/houdini-5-to-participate-in-tcec-season-9/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), April 13, 2016

**[Up one level](Engines "Engines")**

