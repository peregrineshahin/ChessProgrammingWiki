---
title: Checkmate
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Checkmate**

[](File:Foolsmate.jpg) [Shannon Larratt](index.php?title=Category:Shannon_Larratt&action=edit&redlink=1 "Category:Shannon Larratt (page does not exist)") - Fool's mate (2007) [[1]](#cite_note-1) [[2]](#cite_note-2) [[3]](#cite_note-3)
**Checkmate** (often shortened to **mate**) occurs if a [king](King "King") is under immediate attack by one (or two) opponent pieces (in [check](Check "Check")) and has no way to remove it from attack on the next move. Checkmate is the object of the game of chess, it ends with the mate giving player as the winner, and the mated player the loser.

## Contents

- [1 Mate Score](#Mate_Score)
  - [1.1 At the Root](#At_the_Root)
  - [1.2 Down the Tree](#Down_the_Tree)
- [2 Detecting Mate](#Detecting_Mate)
- [3 See also](#See_also)
- [4 Publications](#Publications)
  - [4.1 1952](#1952)
  - [4.2 1965 ...](#1965_...)
  - [4.3 1980 ...](#1980_...)
  - [4.4 1990 ...](#1990_...)
  - [4.5 2000 ...](#2000_...)
  - [4.6 2010 ...](#2010_...)
- [5 Forum Posts](#Forum_Posts)
  - [5.1 1997 ...](#1997_...)
  - [5.2 2000 ...](#2000_..._2)
  - [5.3 2005 ...](#2005_...)
  - [5.4 2010 ...](#2010_..._2)
  - [5.5 2015 ...](#2015_...)
  - [5.6 2020 ...](#2020_...)
  - [5.7 Leonid's Positions](#Leonid.27s_Positions)
- [6 External Links](#External_Links)
- [7 References](#References)

## Mate Score

## At the Root

At the [root](Root "Root") the [score](Score "Score") of a mated player is the worst score one can get, that is a negative score with the greatest absolute value of the score range. It is quite common and sufficient to use something like this in [C](C "C"), [C++](Cpp "Cpp"):

```

##include <limits.h>
/* (-32768/2 = -16384) */
##define VALUE_MATED (SHRT_MIN/2)

```

Inside a 16-bit [short](Word "Word") integer range, assuming [centipawn](Centipawns "Centipawns") evaluation, it translates to roughly being 16 queens down. Note that using [SHRT_MIN](Word#Ranges "Word") instead of SHRT_MIN/2 as mate value has issues in greater/less comparisons of additive expressions, where summands around SHRT_MIN or [SHRT_MAX](Word#Ranges "Word") may under- or overflow, which has somehow relaxed with the advent of the usual 32-bit sign-extension.

## Down the Tree

Inside a [negamax](Negamax "Negamax") based [search](Search "Search"), most [[4]](#cite_note-4) programs assign *VALUE_MATED + [ply](Ply "Ply") distance to the root* as worst case score if entering a [node](Node "Node"), which if propagated as mate score along the [Principal Variation](Principal_Variation "Principal Variation") to the root, translates in mate in odd plies (positive values), or getting mated in even plies. However, those scores need ply-adjustment if stored as [exact score](Exact_Score "Exact Score") inside the [transposition table](Transposition_Table "Transposition Table"), and re-adjustment if retrieving from TT. An alternative approach, not only related to mate scores was proposed by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), *The Delay Penalty* as implemented in [Micro-Max](Micro-Max "Micro-Max") [[5]](#cite_note-5) [[6]](#cite_note-6) [[7]](#cite_note-7) [[8]](#cite_note-8).

## Detecting Mate

Some programs rely on [pseudo-legal move generation](Move_Generation "Move Generation"), and find Checkmate if all those moves are in fact illegal after [making](Make_Move "Make Move") and finding the "refutation" of capturing the king. At the latest, if no legal move was found, programs need the information whether the king is in check to decide about checkmate or [stalemate](Stalemate "Stalemate") score. Despite, most programs (should be) are aware of check in advance, and use special [move generator(s)](Move_Generation "Move Generation") if in check or even in [double check](Double_Check "Double Check"):

1. [Double check](Double_Check "Double Check")
   1. Only King moves or captures
1. [Single check](Check "Check")
   1. Capture the checking piece
   1. King moves or captures
   1. In case of distant checks, interposing a piece between the threatening sliding piece and the king

## See also

- [Check](Check "Check")
- [Chess Problems, Compositions and Studies](Chess_Problems,_Compositions_and_Studies "Chess Problems, Compositions and Studies")
- [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
- [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
- [Mate-in-two](Mate-in-two "Mate-in-two")
- [Mate Search](Mate_Search "Mate Search")
- [Stalemate](Stalemate "Stalemate")

## Publications

## 1952

- [Dietrich Prinz](Dietrich_Prinz "Dietrich Prinz") (**1952**). *Robot Chess*. Research, Vol. 6, reprinted 1988 in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium") » [Mate-in-two](Mate-in-two "Mate-in-two")

## 1965 ...

- [George W. Baylor](George_Baylor "George Baylor") (**1965**). *[Report on a Mating Combinations Program](http://www.dtic.mil/docs/citations/AD0619018)*. SDC Paper, No. SP-2150, System Development Corporation, Santa Monica, Calif. » [Mater](Mater "Mater")
- [George W. Baylor](George_Baylor "George Baylor"), [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1966**). *[A chess mating combinations program](http://dl.acm.org/citation.cfm?id=1464182.1464233&coll=GUIDE&dl=GUIDE)*. [AFIPS](https://en.wikipedia.org/wiki/American_Federation_of_Information_Processing_Societies) [Joint Computer Conferences](https://en.wikipedia.org/wiki/Joint_Computer_Conference), reprinted in [Herbert A. Simon](Herbert_Simon "Herbert Simon") (**1979**). *[Models of Thought](http://yalepress.yale.edu/yupbooks/book.asp?isbn=9780300024326)*. [Yale University Press](https://en.wikipedia.org/wiki/Yale_University_Press), pp. 181-200, in [David Levy](David_Levy "David Levy") (ed.) (**1988**). *[Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")*.
- [George W. Baylor](George_Baylor "George Baylor") (**1966**). *A Computer Model of Checkmating Behaviour in Chess*. in [Adriaan de Groot](Adriaan_de_Groot "Adriaan de Groot"), [Walter R. Reitman](Walter_R._Reitman "Walter R. Reitman") (eds.) (**1966**). *Heuristic Processes in Thinking*. International Congress of Psychology, [Nauka](https://en.wikipedia.org/wiki/Nauka_%28publisher%29), [Moscow](https://en.wikipedia.org/wiki/Moscow)
- [Vladimir E. Alekseev](index.php?title=Vladimir_E._Alekseev&action=edit&redlink=1 "Vladimir E. Alekseev (page does not exist)") (**1969**). *[Compilation of Chess Problems on a Computer](http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=html&identifier=AD0689470)*. Technical translation FSTC-HT-23-124-69, US Army, NTIS AD 689470 ([Problemy Kibernetiki](http://www.worldcat.org/title/problemy-kibernetiki/oclc/1762911), 19, 1967)

## 1980 ...

- [John Birmingham](John_Birmingham "John Birmingham"), [Peter Kent](Peter_Kent "Peter Kent") (**1980**). *Mate at a Glance.* [Advances in Computer Chess 2](Advances_in_Computer_Chess_2 "Advances in Computer Chess 2"), reprinted in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
- [Max Bramer](Max_Bramer "Max Bramer") (**1982**). *Finding Checkmates*. [Computer & Video Games](https://en.wikipedia.org/wiki/Computer_and_Video_Games), [Spring 1982](http://www.chesscomputeruk.com/html/publication_archive_1982.html), [pdf](http://www.chesscomputeruk.com/Computer___Video_Games_Spring_1982.pdf) hosted by [Mike Watters](Mike_Watters "Mike Watters") » [Mater](Mater "Mater")
- [Don Beal](Don_Beal "Don Beal") (**1984**). *Mating Sequences in the Quiescence Search*. [ICCA Journal, Vol. 7, No. 3](ICGA_Journal#7_3 "ICGA Journal")

## 1990 ...

- [Thomas Mally](Thomas_Mally "Thomas Mally") (**1993**). *Matt in Wieviel?* [PC Schach](PC_Schach "PC Schach") 3/93 (German)

## 2000 ...

- [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2004**). *Realization of the Chess Mate Solver Application*. [Yugoslav Journal of Operations Research, Volume 14, Number 2](http://www.doiserbia.nb.rs/issue.aspx?issueid=138), [pdf](http://www.doiserbia.nbs.bg.ac.yu/img/doi/0354-0243/2004/0354-02430402273V.pdf)
- [Fridel Fainshtein](Fridel_Fainshtein "Fridel Fainshtein") (**2006**). *An Orthodox k-Move Problem-Composer for Chess Directmates*. M.Sc. thesis, [Bar-Ilan University](Bar-Ilan_University "Bar-Ilan University"), [pdf](http://www.problemschach.de/KMOVEComposer.pdf)
- [Fridel Fainshtein](Fridel_Fainshtein "Fridel Fainshtein"), [Yaakov HaCohen-Kerner](Yaakov_HaCohen-Kerner "Yaakov HaCohen-Kerner") (**2006**). *A Chess Composer of Two-Move Mate Problems*. [ICGA Journal, Vol. 29, No. 1](ICGA_Journal#29_1 "ICGA Journal"), [pdf](http://homedir.jct.ac.il/%7Ekerner/pdf_docs/ICGA_computer_composer.pdf)
- [Ami Hauptman](index.php?title=Ami_Hauptman&action=edit&redlink=1 "Ami Hauptman (page does not exist)"), [Moshe Sipper](index.php?title=Moshe_Sipper&action=edit&redlink=1 "Moshe Sipper (page does not exist)") (**2007**). *Evolution of an Efficient Search Algorithm for the Mate-In-N Problem in Chess*. [EuroGP 2007](http://www.informatik.uni-trier.de/~%20LEY/db/conf/eurogp/eurogp2007.html), [pdf](http://www.cs.bgu.ac.il/~sipper/papabs/gpsearch.pdf)

## 2010 ...

- [Azlan Iqbal](Azlan_Iqbal "Azlan Iqbal") (**2010**). *Aesthetics in Mate-In-3 Combinations*. Part I Combinatorics and Weights, [ICGA Journal, Vol. 33, No. 3](ICGA_Journal#33_3 "ICGA Journal")
- [Azlan Iqbal](Azlan_Iqbal "Azlan Iqbal") (**2010**). *Aesthetics in Mate-In-3 Combinations*. Part II Normality, [ICGA Journal, Vol. 33, No. 4](ICGA_Journal#33_4 "ICGA Journal")
- [Taichi Ishitobi](index.php?title=Taichi_Ishitobi&action=edit&redlink=1 "Taichi Ishitobi (page does not exist)"), [Alessandro Cincotti](index.php?title=Alessandro_Cincotti&action=edit&redlink=1 "Alessandro Cincotti (page does not exist)"), [Hiroyuki Iida](Hiroyuki_Iida "Hiroyuki Iida") (**2013**). *[Shape-Keeping Technique and Its Application to Checkmate Problem Composition](https://dspace.jaist.ac.jp/dspace/handle/10119/11606?locale=en)*. [2013 AIIDE Workshop](http://tr.aiide.org/)

## Forum Posts

## 1997 ...

- [Mate in 4 explanation](https://www.stmintz.com/ccc/index.php?id=10434) by Howard Exner, [CCC](CCC "CCC"), October 07, 1997
- [Mate in 30 testposition for Rebel 9!](https://www.stmintz.com/ccc/index.php?id=12186) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 20, 1997 » [Rebel](Rebel "Rebel")
- [Mate in 18 moves?](https://www.stmintz.com/ccc/index.php?id=13836) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 09, 1998
- [Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=58) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 05, 1998

[Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21814) by [David Eppstein](David_Eppstein "David Eppstein"), [CCC](CCC "CCC"), July 06, 1998
[Re: Using too-shallow mate scores from the hash table](https://www.stmintz.com/ccc/index.php?id=21838) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 07, 1998

- [Solve for Mate](https://www.stmintz.com/ccc/index.php?id=22049) by Trefor Deane, [CCC](CCC "CCC"), July 11, 1998
- [Mate the Royal Couple](https://www.stmintz.com/ccc/index.php?id=32930) by Hans Havermann, [CCC](CCC "CCC"), November 14, 1998
- [Estimated # of checkmate positions?](https://www.stmintz.com/ccc/index.php?id=59646) by Jeff Anderson, [CCC](CCC "CCC"), July 07, 1999
- [Mate solvers...](https://www.stmintz.com/ccc/index.php?id=67784) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), September 07, 1999
- [Interesting mate test for hashing](https://www.stmintz.com/ccc/index.php?id=68037) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 10, 1999 » [Transposition Table](Transposition_Table "Transposition Table")

## [Is "Interesting mate test..." the longest ever thread....](https://www.stmintz.com/ccc/index.php?id=68340) by Tina Long, [CCC](CCC "CCC"), September 11, 1999 2000 ...

- [Mate in 1 - but Fritz 6 needs 1 hour!!!](https://www.stmintz.com/ccc/index.php?id=123825) by Christoph Fieberg, [CCC](CCC "CCC"), August 10, 2000
- [What's the fastest mate-finder?](https://www.stmintz.com/ccc/index.php?id=126780) by [Michel Langeveld](Michel_Langeveld "Michel Langeveld"), [CCC](CCC "CCC"), August 27, 2000
- [Questions about Mate Searching](https://www.stmintz.com/ccc/index.php?id=130376) by [William Bryant](William_Bryant "William Bryant"), [CCC](CCC "CCC"), September 23, 2000 » [Mate Search](Mate_Search "Mate Search")
- [Mate in 7 moves - diagram](https://www.stmintz.com/ccc/index.php?id=130700) by [Eduard Nemeth](index.php?title=Eduard_Nemeth&action=edit&redlink=1 "Eduard Nemeth (page does not exist)"), [CCC](CCC "CCC"), September 27, 2000 » [Zugzwang](Zugzwang "Zugzwang")
- [Static Mate Detection](https://www.stmintz.com/ccc/index.php?id=209201) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), January 22, 2002 » [Mate at a Glance](Mate_at_a_Glance "Mate at a Glance")
- [First mate in 2, then mate in 3](https://www.stmintz.com/ccc/index.php?id=287666) by [Albert Bertilsson](Albert_Bertilsson "Albert Bertilsson"), [CCC](CCC "CCC"), March 03, 2003
- [Easy mate](https://www.stmintz.com/ccc/index.php?id=315666) by [Frank Phillips](Frank_Phillips "Frank Phillips"), [CCC](CCC "CCC"), September 13, 2003 [[9]](#cite_note-9)

## 2005 ...

- [Shortest ever mate?](https://www.stmintz.com/ccc/index.php?id=458757) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), October 30, 2005
- [The Code for the Rybka-Mate-Bug](https://www.stmintz.com/ccc/index.php?id=469728) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 13, 2005 » [Rybka](Rybka "Rybka")
- [Unusual Mate in 3](https://www.stmintz.com/ccc/index.php?id=490808) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), March 02, 2006
- [Delayed-loss-bonus discussion goes here](http://www.talkchess.com/forum/viewtopic.php?t=16751) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 28, 2007
- [mate detetion issue](http://www.talkchess.com/forum/viewtopic.php?t=24560) by [Mike Adams](index.php?title=Mike_Adams&action=edit&redlink=1 "Mike Adams (page does not exist)"), [CCC](CCC "CCC"), October 24, 2008 » [Connect Four](Connect_Four "Connect Four"), [Fail-Soft](Fail-Soft "Fail-Soft")
- [How to check for checkmate/stalemate programmatically?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=8533) by Valentin, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), November 22, 2008 » [Stalemate](Stalemate "Stalemate")
- [Draw by repetition when mate is possible](http://www.talkchess.com/forum/viewtopic.php?t=25705) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé"), [CCC](CCC "CCC"), December 30, 2008 » [Repetitions](Repetitions "Repetitions")

## 2010 ...

- [Puzzle with mate scores in TT](http://www.talkchess.com/forum/viewtopic.php?t=37016) by [Robert Purves](index.php?title=Robert_Purves&action=edit&redlink=1 "Robert Purves (page does not exist)"), [CCC](CCC "CCC"), December 10, 2010 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [Yet Another Mate Solving Test](http://www.talkchess.com/forum/viewtopic.php?t=37616) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 14, 2011
- [Mate score in TT](http://www.talkchess.com/forum/viewtopic.php?t=41640) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), December 28, 2011 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [Checkmate In Zero](http://www.talkchess.com/forum/viewtopic.php?t=46737) by [Christopher Conkie](index.php?title=Christopher_Conkie&action=edit&redlink=1 "Christopher Conkie (page does not exist)"), [CCC](CCC "CCC"), January 02, 2013
- [Quiescence Search and Checkmates](http://www.open-chess.org/viewtopic.php?f=5&t=2212) by [CDaley11](Christian_Daley "Christian Daley"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), January 11, 2013  » [Quiescence Search](Quiescence_Search "Quiescence Search")
- [To be, or not to be checkmated](http://www.talkchess.com/forum/viewtopic.php?t=52036) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 18, 2014
- [Mate score from the transposition table](http://www.talkchess.com/forum/viewtopic.php?t=54141) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), October 25, 2014 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")

## 2015 ...

- [Remember Leonid Liberman (author of LLCHESS)?](http://www.talkchess.com/forum/viewtopic.php?t=56455) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 23, 2015 » [Leonid's Positions](Checkmate#Leonid "Checkmate")
- [TT Mate scores](http://www.open-chess.org/viewtopic.php?f=5&t=2951) by rgoomes, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 10, 2016 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [Funny mate in 6](http://www.talkchess.com/forum/viewtopic.php?t=59276) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 17, 2016
- [Mate scores from IID](http://www.talkchess.com/forum/viewtopic.php?t=61134) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), August 16, 2016 » [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Why do engines lack mate solving?](http://www.talkchess.com/forum/viewtopic.php?t=61731) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), October 15, 2016 » [Mate Search](Mate_Search "Mate Search")
- [Mate Score](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=64428) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), June 27, 2017
- [Mate scores in TT (a new?... approach)](http://www.talkchess.com/forum/viewtopic.php?t=67049) by Vince Sempronio, [CCC](CCC "CCC"), April 09, 2018
- [Yet another Mate scores in TT thread](http://www.talkchess.com/forum/viewtopic.php?t=67078) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), April 12, 2018 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [mate test positions](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68100) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 29, 2018 » [Test-Positions](Test-Positions "Test-Positions")
- [A mate suite to test multi-pv and new engines](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68146) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), August 06, 2018
- [Trying to find a weird mate in 1...](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71337) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), July 22, 2019 » [Fieberg's mate-in-1](#FiebergMateInOne)

## 2020 ...

- [Correct way to store and extract mate scores](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74411) by Ian Mitchell, [CCC](CCC "CCC"), July 08, 2020 » [Score](Score "Score"), [Transposition Table](Transposition_Table "Transposition Table")
- [mate suite for chess engines](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77834) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), July 30, 2021

## Leonid's Positions

[Positions](Template:Leonid%27s_Positions "Template:Leonid's Positions") by [Leonid Liberman](Leonid_Liberman "Leonid Liberman")

- [Mate in ...?](https://www.stmintz.com/ccc/index.php?id=96675) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 12, 2000
- [Two mate positions to solve](https://www.stmintz.com/ccc/index.php?id=127930) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 02, 2000
- [Two mate position to solve](https://www.stmintz.com/ccc/index.php?id=128470) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 06, 2000
- [What shortest mate that you can find for this position?](https://www.stmintz.com/ccc/index.php?id=150512) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 17, 2001
- [If you like to find a mate...](https://www.stmintz.com/ccc/index.php?id=150751) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 18, 2001
- [If you want solve one mate...](https://www.stmintz.com/ccc/index.php?id=151169) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 21, 2001
- [One easy mate to solve...](https://www.stmintz.com/ccc/index.php?id=151382) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 22, 2001
- [One average mate position...](https://www.stmintz.com/ccc/index.php?id=151486) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 23, 2001
- [If you like to solve easy forced mate...](https://www.stmintz.com/ccc/index.php?id=151715) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 24, 2001
- [If you like to solve average mate position...](https://www.stmintz.com/ccc/index.php?id=151908) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 25, 2001
- [If you like to solve real mate...](https://www.stmintz.com/ccc/index.php?id=152200) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 27, 2001
- [If you like to solve mate from real game...](https://www.stmintz.com/ccc/index.php?id=152371) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 28, 2001
- [If you like forced mate...](https://www.stmintz.com/ccc/index.php?id=152603) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 30, 2001
- [Forced mate position to solve...](https://www.stmintz.com/ccc/index.php?id=152791) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), January 31, 2001
- [If you like to solve a mate...](https://www.stmintz.com/ccc/index.php?id=152923) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 01, 2001
- [Forced mate so solve...](https://www.stmintz.com/ccc/index.php?id=153440) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 05, 2001
- [If you like to solve easy mate...](https://www.stmintz.com/ccc/index.php?id=153845) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 08, 2001
- [If you like to solve a mate...](https://www.stmintz.com/ccc/index.php?id=153950) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 09, 2001
- [If you like to crush easy mate...](https://www.stmintz.com/ccc/index.php?id=154066) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 10, 2001
- [If you like to solve mate for light position...](https://www.stmintz.com/ccc/index.php?id=154172) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 11, 2001
- [If you like to solve mate...](https://www.stmintz.com/ccc/index.php?id=154554) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 14, 2001
- [If you like solving forced mate...](https://www.stmintz.com/ccc/index.php?id=154658) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 15, 2001
- [If you like to solve one easy mate...](https://www.stmintz.com/ccc/index.php?id=154766) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), February 16, 2001
- [Easy mate to solve...](https://www.stmintz.com/ccc/index.php?id=157090) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), March 04, 2001
- [If you like to sove a mate...](https://www.stmintz.com/ccc/index.php?id=157810) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), March 10, 2001
- [If you are ready to solve one mate...](https://www.stmintz.com/ccc/index.php?id=162940) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 11, 2001
- [If you like easy mate...](https://www.stmintz.com/ccc/index.php?id=163025) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 12, 2001
- [If you want to solve one mate...](https://www.stmintz.com/ccc/index.php?id=163310) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 14, 2001
- [If you enjoy like me solving mates...](https://www.stmintz.com/ccc/index.php?id=163779) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 16, 2001
- [Mate that every program will solve...](https://www.stmintz.com/ccc/index.php?id=164046) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 17, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=165276) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 22, 2001
- [Mate to solve...](https://www.stmintz.com/ccc/index.php?id=165567) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 23, 2001
- [Mate that every program will find](https://www.stmintz.com/ccc/index.php?id=166139) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 26, 2001
- [Mate to solve for champions...](https://www.stmintz.com/ccc/index.php?id=166656) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), April 29, 2001
- [One mate to solve for fittest programs](https://www.stmintz.com/ccc/index.php?id=167905) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 04, 2001
- [Very easy mate to solve](https://www.stmintz.com/ccc/index.php?id=168165) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 05, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=168263) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 06, 2001
- [Mate to solve in two flavous](https://www.stmintz.com/ccc/index.php?id=168487) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 07, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=168574) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 08, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=169798) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 15, 2001
- [One very easy mate to solve](https://www.stmintz.com/ccc/index.php?id=170990) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 21, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=172464) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), May 30, 2001
- [One mate to solve...](https://www.stmintz.com/ccc/index.php?id=173071) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 02, 2001
- [Mate to solve for good program](https://www.stmintz.com/ccc/index.php?id=174004) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 07, 2001
- [One mate to solve for Champion!](https://www.stmintz.com/ccc/index.php?id=175401) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), June 16, 2001
- [One mate to solve](https://www.stmintz.com/ccc/index.php?id=180081) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), July 17, 2001
- [One mate to sove for Champions!](https://www.stmintz.com/ccc/index.php?id=186841) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 02, 2001
- [One mate to solve for Champions!](https://www.stmintz.com/ccc/index.php?id=191366) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 02, 2001
- [A mate for Leonid](https://www.stmintz.com/ccc/index.php?id=192655) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), October 10, 2001
- [Try this mate](https://www.stmintz.com/ccc/index.php?id=193165) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 16, 2001
- [Try solve this mate](https://www.stmintz.com/ccc/index.php?id=193660) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 21, 2001
- [Try this moderate mate](https://www.stmintz.com/ccc/index.php?id=194491) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 27, 2001
- [One easy mate](https://www.stmintz.com/ccc/index.php?id=195515) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 04, 2001
- [Very easy mate to solve](https://www.stmintz.com/ccc/index.php?id=203145) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), December 22, 2001
- [Find a mate](https://www.stmintz.com/ccc/index.php?id=243935) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), August 03, 2002
- [One mate in 10 to solve](https://www.stmintz.com/ccc/index.php?id=245026) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), August 10, 2002
- [One mate in 11](https://www.stmintz.com/ccc/index.php?id=250639) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 07, 2002
- [Try to solve mate](https://www.stmintz.com/ccc/index.php?id=252069) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 14, 2002
- [Mate slightly harder](https://www.stmintz.com/ccc/index.php?id=312759) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), August 25, 2003
- [Mate that should be easy](https://www.stmintz.com/ccc/index.php?id=322476) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 19, 2003
- [Heavy mate position but easy to solve](https://www.stmintz.com/ccc/index.php?id=322581) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), October 20, 2003
- [Mate to torture](https://www.stmintz.com/ccc/index.php?id=325217) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 02, 2003
- [Try very easy mate](https://www.stmintz.com/ccc/index.php?id=325687) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 04, 2003
- [Try to solve very populated mate](https://www.stmintz.com/ccc/index.php?id=325879) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 05, 2003
- [Very easy mate](https://www.stmintz.com/ccc/index.php?id=326086) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), November 06, 2003

## External Links

- [Checkmate from Wikipedia](https://en.wikipedia.org/wiki/Checkmate)
- [Checkmate pattern from Wikipedia](https://en.wikipedia.org/wiki/Checkmate_pattern)
- [Checkmate/Stalemate Scoring](http://web.archive.org/web/20070707035457/www.brucemo.com/compchess/programming/matescore.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)
- [Handling Mate Scores](http://web.archive.org/web/20070707041901/www.brucemo.com/compchess/programming/matehash.htm) from [Bruce Moreland's](Bruce_Moreland "Bruce Moreland") [Programming Topics](http://web.archive.org/web/20070811182741/www.seanet.com/%7Ebrucemo/topics/topics.htm)

## References

1. [↑](#cite_ref-1) [Shannon Larratt](index.php?title=Category:Shannon_Larratt&action=edit&redlink=1 "Category:Shannon Larratt (page does not exist)") - [Fool's mate](https://en.wikipedia.org/wiki/Fool's_mate) (2007) from Tableaux ayant pour sujet les échecs (dead link)
1. [↑](#cite_ref-2) [In Loving Memory of Shannon Larratt 1:24](https://youtu.be/CILh2HaDS4Y?t=1m24s), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video
1. [↑](#cite_ref-3) [Shannon Larratt is Zentastic › Blog archives](http://www.zentastic.com/blog/2007/02/page/6/), February 09, 2007
1. [↑](#cite_ref-4) [The Code for the Rybka-Mate-Bug](https://www.stmintz.com/ccc/index.php?id=469728) by [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger"), [CCC](CCC "CCC"), December 13, 2005
1. [↑](#cite_ref-5) [Evaluation: Aging - The Delay Penalty](http://home.hccnet.nl/h.g.muller/delay.html) from [Micro-Max](Micro-Max "Micro-Max") by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
1. [↑](#cite_ref-6) [Re: Transposition Tables](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=147295&t=15129) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 26, 2007
1. [↑](#cite_ref-7) [Delayed-loss-bonus discussion goes here](http://www.talkchess.com/forum/viewtopic.php?t=16751) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), September 28, 2007
1. [↑](#cite_ref-8) [Seeing a promotion, but not playing it...](http://www.talkchess.com/forum/viewtopic.php?t=31981) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 24, 2010
1. [↑](#cite_ref-9) [Frank Phillips' KNNKP position revisited ...](https://www.stmintz.com/ccc/index.php?id=316547) by [Guy Haworth](Guy_Haworth "Guy Haworth"), [CCC](CCC "CCC"), September 18, 2003 » [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")

**[Up one Level](Chess "Chess")**

