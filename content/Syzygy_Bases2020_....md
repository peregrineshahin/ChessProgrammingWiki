---
title: Syzygy Bases2020 ...
---
**[Home](Home "Home") \* [Knowledge](Knowledge "Knowledge") \* [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases") \* Syzygy Bases**



[ Syzygy - Three Planets Dance Over [La Silla](https://en.wikipedia.org/wiki/La_Silla_Observatory) [[1]](#cite_note-1)
**Syzygy Bases**, [[2]](#cite_note-2)  

a compact six piece endgame database developed by [Ronald de Man](Ronald_de_Man "Ronald de Man"), published on April 01, 2013. Since August 2018, **seven piece** Syzygy Bases are available after an effort by [Bojun Guo](Bojun_Guo "Bojun Guo") started in March 2018 [[3]](#cite_note-3). The generator is released under the [GNU General Public License Version 2](Free_Software_Foundation#GPL "Free Software Foundation"), the [thread safe](Thread "Thread") probing code is released without restrictions [[4]](#cite_note-4) .



### File Types


Syzygy Bases consist of two sets of files, **WDL** files (extension .rtbw) storing win/draw/loss information considering the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule") for access during [search](Search "Search"), and **DTZ** files (extension .rtbz) with [distance-to-zero](Endgame_Tablebases#DTZ50 "Endgame Tablebases") information for access at the [root](Root "Root"). WDL has full data for two sides but DTZ50 omitted data of one side to save space. Each endgame has a pair of those types.



### File Sizes




|  Men
 |  WDL
 |  DTZ
 |  Total
 |
| --- | --- | --- | --- |
|  3-5
 |  378.1 [MiB](https://en.wikipedia.org/wiki/Mebibyte) |  561.9 MiB
 |  939.0 MiB
 |
|  6
 |  67.8 [GiB](https://en.wikipedia.org/wiki/Gibibyte) |  81.4 GiB
 |  149.2 GiB
 |
|  7
 |  8.5 [TiB](https://en.wikipedia.org/wiki/Tebibyte) |  8.3 TiB
 |  16.7 TiB
 |


### Comparision


Syzygy EGTB is significantly smaller than any existent [DTM](Endgame_Tablebases#DTM "Endgame Tablebases") EGTB. It is 7 times as small as Gaviota for 5 men, 8 times as small as Nalimov for 6 men, 8 times as small as Lomonosov for 7 men. However, when all DTM EGTBs have full data of two sides, Syzygy EGTB omits data of one side for DTZ data to save space. [Ronald de Man](Ronald_de_Man "Ronald de Man") estimated if keep them all, the Syzygy's 6 men size may increase 158 GB, become 307 GB in total, double on size, be 4 times as small as Nalimov 6 men.



## Generation


### Up to 6-man


On the first release (Apr 01, 2013) the generator was ready to generate all endgames up to 6 men. It is multithreading and processes completely in RAM. To generate all 6 men, it requires a system with at least 32 GB of RAM and may run in 5 days (the period was measured with a computer 6-core i3930K @ 4.2Ghz, 64 GB).



### 7-man


Ronald de Man wasn't initially interested in the creation of 7-men Syzygy Based [[5]](#cite_note-5) since the generation would require about 1 TB of RAM, too expensive at that time. Generation time would be about 64 x per table, which means around 175 x time total [[6]](#cite_note-6).His original generator could not create them. But in 2018, he supported [Bojun Guo](Bojun_Guo "Bojun Guo") in his 5-month attempt to generated them [[7]](#cite_note-7). His hardware was estimated at over US$ 90K. In August of 2018 their creation was completed [[8]](#cite_note-8)[[9]](#cite_note-9).



### 8-man


After the completion of 7-man, many people start being curious about the feasibleness of building 8-man. Ronald de Man made an estimation that task requires computers with 64 TB RAM and 2000 TB hard disks[[10]](#cite_note-10) (costed about $640K and $40K respectively in 2020 [[11]](#cite_note-11)).



### Checksums


Syzygy endgame files may contain 128-bit checksum keys at the end of those files. It also has its own code for checksums (based on Google's cityhash library).



## Search


### During the Search


During the [search](Search "Search"), with the WDL tables stored on [SSD](https://en.wikipedia.org/wiki/Solid-state_drive) [[12]](#cite_note-12) , it is possible to probe the tables at all [depths](Depth "Depth") without much slowdown. They have been tested in Ronald de Man's engine [Sjaak](Sjaak "Sjaak") (playing on [FICS](index.php?title=FICS&action=edit&redlink=1 "FICS (page does not exist)") as TrojanKnight(C)) a couple of months quite successfully, don't probing in [quiescence search](Quiescence_Search "Quiescence Search").



### At the Root


At the [root](Root "Root"), since pure DTZ50-optimal play (i.e. minimaxing the number of moves to the next [capture](Captures "Captures") or [pawn move](Pawn_Push "Pawn Push") by either side) can be very unnatural, it might be desirable to let the engine search on the winning moves until it becomes clear that insufficient progress is being made and only then switch to DTZ-optimal play (e.g. by detecting [repetitions](Repetitions "Repetitions") and monitoring the [halfmove clock](Halfmove_Clock "Halfmove Clock")) [[13]](#cite_note-13).



## Pros & Cons


### Pros


* Small sizes. It is about 8 times as small as the second-best EGTBs. Having small sizes is the main success key of Syzygy Bases since it is much easier to create, store, provide, download than other EGTBs
* Free and more popular (than other EGTBs) to find on the Internet
* Support [DTZ50](Endgame_Tablebases#DTZ50 "Endgame Tablebases") metric. That metric can help engines to have better results than [DTM](Endgame_Tablebases#DTM "Endgame Tablebases") which is supported widely by other EGTBs


### Cons


* Hard to integrate with chess engines. [Ronald de Man](Ronald_de_Man "Ronald de Man") has not provided probing code as an independent library but as a part of [Stockfish](Stockfish "Stockfish") chess engines. The probe code has integrated too deeply with that chess engine code and it requires a lot of effort to de-integrate, modify and integrate with other chess projects
* Hard to understand and contribute to the project. ETGB itself is a hard topic. Syzygy EGTB has also integrated with many advanced techniques/tricks. It is written in old-style C language. All make it become very hard to understand and/or modify to improve or for other purposes
* [DTZ50](Endgame_Tablebases#DTZ50 "Endgame Tablebases") metric may lead the engines to win in much longer and ugly ways, compared with [DTM](Endgame_Tablebases#DTM "Endgame Tablebases") one


## Data publish


[Ronald de Man](Ronald_de_Man "Ronald de Man") has provided only open source code for generators/probers but not endgame files themselves. Using his tools some people have generated endgames and published them via DVD or online.



### DVD


As of February 2015, all 3-5 and most important 6-men Syzygy Bases are commercially available on 4 [DVDs](https://en.wikipedia.org/wiki/DVD) by [ChessBase](ChessBase "ChessBase") as *Endgame Turbo 4* for their products [Deep Fritz 14](Fritz "Fritz"), [Komodo Chess 8](Komodo#8 "Komodo"), [Houdini 4](Houdini "Houdini") or [ChessBase 12/13](ChessBase_(Database) "ChessBase (Database)") [[14]](#cite_note-14) [[15]](#cite_note-15). 



### Free Download


There are some free FTP servers for downloading such as [Bojun Guo](Bojun_Guo "Bojun Guo") and [Lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)") servers.



### 3-6 men


The sizes of those men are small enough to download and store on modern computers. Users should download them in full sets (3, 4, 5, 6 men).



### 7 men


All 7 men files' size is over 16.7 TiB, over storages of typical modern computers. They also require a long time to download too. Thus some users choose to download one or a few endgames only, based on their statistics of use in endgames. Bellow is the top 20 of those endgames by their order. The first one, KRPPvKRP, has a significantly higher frequency of use than the others and should be always downloaded:





|  Rank
 |  Name
 |  Rank
 |  Name
 |  Rank
 |  Name
 |  Rank
 |  Name
 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  1
 |  KRPPvKRP
 |  6
 |  KNPPvKNP
 |  11
 |  KBPPvKNP
 |  16
 |  KRBPPvKR
 |
|  2
 |  KBPPvKBP
 |  7
 |  KNPPvKBP
 |  12
 |  KRPPvKRB
 |  17
 |  KBPPvKPP
 |
|  3
 |  KPPPvKPP
 |  8
 |  KRBPvKRP
 |  13
 |  KRPPvKPP
 |  18
 |  KRPPPvKP
 |
|  4
 |  KRPPPvKR
 |  9
 |  KQPPvKPP
 |  14
 |  KBPPvKRP
 |  19
 |  KRBPvKRB
 |
|  5
 |  KQPPvKQP
 |  10
 |  KQPPPvKP
 |  15
 |  KRNPvKRP
 |  20
 |  KRPPvKRN
 |


## Probe Code and Tools


### Stockfish


[Ronald de Man](Ronald_de_Man "Ronald de Man") did not provide the probe code as an independent library. Instead, he published it firstly as an already integrated code for [Stockfish](Stockfish "Stockfish") chess engines. It is c++ code and it has been rewritten, updated several times by [Stockfish](Stockfish "Stockfish") team.



### Fathom


**Fathom** is a stand-alone Syzygy based probing tool and [API](https://en.wikipedia.org/wiki/Application_programming_interface) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), introduced in November 2015 along with his [Gull 3](Gull "Gull") release [[16]](#cite_note-16) . Unlike the original tbprobe code, Fathom does not necessarily require the callee to provide [move generation](Move_Generation "Move Generation") functionality. The new modifications and extensions to Ronald de Man's original code which can be "redistributed and/or modified without restrictions", are released under the permissive [MIT License](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology"). The API consists of three functions [[17]](#cite_note-17) :



* tb\_init initializes the tablebase
* tb\_probe\_wdl probes the Win-Draw-Loss (WDL) table for a given position
* tb\_probe\_root probes the Distance-To-Zero (DTZ) table for the given position.


[Jon Dart](Jon_Dart "Jon Dart") has a fork of Fathom with some bug fixes and enhancements [[18]](#cite_note-18), also supporting 7-man [[19]](#cite_note-19).



### Pyrrhic


**Pyrrhic** is a cleaned up Fathom by [Andrew Grant](Andrew_Grant "Andrew Grant"), introduced in August 2020 [[20]](#cite_note-20) [[21]](#cite_note-21).



## Elo gain


[Fishtest](Stockfish#Fishtest "Stockfish") team revealed a test with [Stockfish](Stockfish "Stockfish") (SF10dev) at 10+0.1, with all Syzygy WDL files on RAM, testing using none(0), 4, 5, and 6 man TB in a round-robin tournament[[22]](#cite_note-22).





|  Rank
 |  Name
 |  Elo
 |  +/-
 |  Games
 |  Score
 |  Draws
 |
| --- | --- | --- | --- | --- | --- | --- |
|  1
 |  syzygy6
 |  13
 |  2
 |  82591
 |  51.8%
 |  59.5%
 |
|  2
 |  syzygy5
 |  2
 |  2
 |  82590
 |  50.3%
 |  59.4%
 |
|  3
 |  syzygy4
 |  -7
 |  2
 |  82591
 |  49.0%
 |  59.3%
 |
|  4
 |  syzygy0
 |  -7
 |  2
 |  82592
 |  48.9%
 |  59.4%
 |


## Quotes


by [Ronald de Man](Ronald_de_Man "Ronald de Man") in a reply to [Guy Haworth](Guy_Haworth "Guy Haworth"), April 06, 2013 [[23]](#cite_note-23) :




```C++
I create both WDL and DTZ in one go, so I don't use WDL in the creation of DTZ. The algorithm used is the [grandfather algorithm](Retrograde_Analysis#Algorithm "Retrograde Analysis") with 2 plies per iteration (I think [HGM](Harm_Geert_Muller "Harm Geert Muller") calls this leapfrogging, but I might be wrong). I tried the outcounting method, but it didn't seem to be competitive (and it makes things more complicated). [[24]](#cite_note-24) [[25]](#cite_note-25)
A pure WDL/DTZ pair is not of much use for creating WDL50+/DTZ50+. I create tables in RAM that have all the information necessary for WDL50+ and DTZ50+, then permute them to different indexing schemes and compress. I do test runs on subsets of the data to find good permutations. (The idea to try permutations is from [Jesper Torp Kristensen's](Jesper_Torp_Kristensen "Jesper Torp Kristensen") master thesis.) [[26]](#cite_note-26) [[27]](#cite_note-27) 

```

[Ronald de Man](Ronald_de_Man "Ronald de Man") in a reply to [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), April 15, 2020 [[28]](#cite_note-28) :




```C++
Syzygy WDL is double sided, DTZ is single sided.
So to know whether a 7-piece position is winning, losing or drawn (or cursed), the engine needs to do only a single probe of a 7-piece WDL table. (It may in addition have to do some probes of 6-piece WDL tables if any direct captures are available.)
If the engine needs to know the DTZ value (which is only necessary when a TB root position has been reached), the probing code may have to do a 1-ply search to get to the "right" side of the DTZ table.
For 6-piece TBs, DTZ is 81.9GB when storing only the smaller side of each table. Storing both sides might require perhaps 240GB.

```

[Morgan Houppin](Morgan_Houppin "Morgan Houppin") explained why his chess engine [Stash](Stash "Stash") doesn't have Syzygy probe code, March 25, 2021 [[29]](#cite_note-29) :




```C++
Syzygy probing is a hell of a mess, and I don't want to plug two thousand lines of foreign code that I don't understand, nor do I have the motivation to fully understand how Syzygy files are stored, and then write the additional two thousand lines of code to read them for a mere 5 Elo gain at TCEC.

```

## Endgame News


In his 2014 *Chess Endgame News* in [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal") [[30]](#cite_note-30) , [Guy Haworth](Guy_Haworth "Guy Haworth") classified Syzygy Bases as **new** data in **three** ways:



1. 5-valued scale for evaluating positions in the context of the [FIDE](FIDE "FIDE") [50-move rule](Fifty-move_Rule "Fifty-move Rule") (50mr) which constrains the length of phases of play
	1. +2 ≡ unconditional win for the side to move
	2. +1 ≡ ‘win’ which can be frustrated by best play and a 50mr draw-claim
	3. \_0 ≡ unconditional draw
	4. -1 ≡ ‘loss’ saved by a 50mr draw-claim
	5. -2 ≡ unconditional loss
2. depths for ‘50mr draw’ positions with value ±1
3. depths in symmetric, information-preserving ply ‘p’


and further gives some news about early software bugs and glitches concerning [ChessBase](ChessBase "ChessBase") products, and the importance of [MD5](https://en.wikipedia.org/wiki/MD5) to check the EGT integrity.



## See also


* [Bitbases](Endgame_Bitbases "Endgame Bitbases")
* [Edwards' Tablebases](Edwards%27_Tablebases "Edwards' Tablebases")
* [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases")
* [Lomonosov Tablebases](Lomonosov_Tablebases "Lomonosov Tablebases")
* [Nalimov Tablebases](Nalimov_Tablebases "Nalimov Tablebases")
* [python-chess](Python-chess "Python-chess")
* [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [Thompson's Databases](Thompson%27s_Databases "Thompson's Databases")


## Publications


* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2014**). *Chess Endgame News*. [ICGA Journal, Vol. 37, No. 1](ICGA_Journal#37_1 "ICGA Journal")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2014**). *Chess Endgame News*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2014**). *Chess Endgame News*. [ICGA Journal, Vol. 37, No. 3](ICGA_Journal#37_3 "ICGA Journal") » [Fritz 14](Fritz "Fritz")
* [Guy Haworth](Guy_Haworth "Guy Haworth") (**2018**). *Chess Endgame News: 7-man ‘Syzygy’ DTZ50 EGTs*. [ICGA Journal, Vol. 40, No. 4](ICGA_Journal#40_4 "ICGA Journal")


## Forum Posts


### 2013 ...


* [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), April 01, 2013 [[31]](#cite_note-31)
* [New 6-piece tablebase generator](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=6971) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), April 01, 2013
* [Re: PEXT Bitboards](http://www.talkchess.com/forum/viewtopic.php?t=48220&start=1) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), June 07, 2013 » [BMI2 - PDEP](BMI2#PDEP "BMI2"), [BMI2 - PEXT](BMI2#PEXT "BMI2")
* [Syzygy EGTB's via Torrent Thread](http://www.talkchess.com/forum/viewtopic.php?t=49303) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), September 11, 2013
* [Syzygy tablebases, work in Stockfish?](http://www.talkchess.com/forum/viewtopic.php?t=49439) by [Jose Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), September 23, 2013 » [Stockfish](Stockfish "Stockfish")
* [Building Syzygy bases](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=27789) by higgs, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 12, 2013
* [tablebase caching / mmap() / page cache](http://www.talkchess.com/forum/viewtopic.php?t=49702) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), October 13, 2013 » [Memory](Memory "Memory")
* [Syzygy endgame tables: Generation and first impressions](http://www.talkchess.com/forum/viewtopic.php?t=49724) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), October 15, 2013
* [deMan TB Path and Cache](http://www.talkchess.com/forum/viewtopic.php?t=49770) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), October 19, 2013
* [syzygy TB (3-4-5 men only) download link ?](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=27833)  by MarshallArts, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), October 21, 2013
* [rkiss and other dependencies in syzygy](http://www.talkchess.com/forum/viewtopic.php?t=49807) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), October 23, 2013
* [Syzygy / egbb discussion](http://www.talkchess.com/forum/viewtopic.php?t=49819) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 23, 2013 » [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [Manual: How to use Syzygy (or any other) 6-men without SSD](http://www.talkchess.com/forum/viewtopic.php?t=50093) by [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"), [CCC](CCC "CCC"), November 16, 2013
* [potential deadlock in syzygy reference implementation](http://www.talkchess.com/forum/viewtopic.php?t=50192) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), November 23, 2013
* [Re: A note for C programmers](http://www.talkchess.com/forum/viewtopic.php?t=50186&start=68) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), November 27, 2013
* [Stockfish Syzygy: how to interpret mates?](http://www.talkchess.com/forum/viewtopic.php?t=50296) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 01, 2013 » [Stockfish](Stockfish "Stockfish"), [Mate Scores](Score#MateScores "Score")
* [Problem with 6-piece syzygy-bases using wine](http://www.talkchess.com/forum/viewtopic.php?t=50337) by [Bernhard Bauer](index.php?title=Bernhard_Bauer&action=edit&redlink=1 "Bernhard Bauer (page does not exist)"), [CCC](CCC "CCC"), December 05, 2013 [[32]](#cite_note-32)
* [ChessGUI 0.245f is available](http://www.talkchess.com/forum/viewtopic.php?t=50492) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), December 14, 2013 » [ChessGUI](ChessGUI "ChessGUI")
* [Syzygybases suitable for win32-systems?](http://www.talkchess.com/forum/viewtopic.php?t=50523) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), December 17, 2013
* [Syzygy Tablebases list of importance](http://www.open-chess.org/viewtopic.php?f=3&t=2545) by chri$, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 21, 2013
* [Syzygy options](http://www.talkchess.com/forum/viewtopic.php?t=50655) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), December 27, 2013


**2014**



* [Ideal Syzygy Probe Depth ? (using SSD)](http://www.talkchess.com/forum/viewtopic.php?t=50896) by Anil V Dharan, [CCC](CCC "CCC"), January 14, 2014
* [SYZYGY Base question](http://www.talkchess.com/forum/viewtopic.php?t=50967) by [Ingo Bauer](Ingo_Bauer "Ingo Bauer"), [CCC](CCC "CCC"), January 19, 2014
* [problem with syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=51134) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), February 01, 2014
* [Performance of Syzygy and Scorpio](http://www.talkchess.com/forum/viewtopic.php?t=51159) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), February 04, 2014 » [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [A question about syzygy](http://www.talkchess.com/forum/viewtopic.php?t=51421) by Enrico Tognoni, [CCC](CCC "CCC"), February 26, 2014
* [A question about syzygy 6 men and partial use](http://www.talkchess.com/forum/viewtopic.php?t=51426) by Enrico Tognoni, [CCC](CCC "CCC"), February 26, 2014
* [Syzygy on RAM Drive](http://www.talkchess.com/forum/viewtopic.php?t=52411) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 23, 2014 » [Stockfish](Stockfish "Stockfish"), [Komodo 7](Komodo#7 "Komodo"), [Houdini 4](Houdini "Houdini")
* [Re: Syzygy tb generator for windows](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=7396#p83338) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2014
* [Question about syzygy bases](http://www.talkchess.com/forum/viewtopic.php?t=52522) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), June 02, 2014
* [Re: 7-piece syzygy](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=7618#p83771) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), July 03, 2014
* [Question on Stockfish and SyzygyCache UCI option](http://www.talkchess.com/forum/viewtopic.php?t=54572) by Erfuk Neuni, [CCC](CCC "CCC"), December 07, 2014
* [USB 3 Storage for Syzygy WDL files](http://www.talkchess.com/forum/viewtopic.php?t=54636) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), December 13, 2014 » [USB 3.0](Memory#USB3 "Memory")


### 2015 ...


* [Komodo 8 - 5-men Syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=54928) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 10, 2015 » [Komodo 8](Komodo#8 "Komodo")
* [Problem with SF6 and Syzygy TB](http://www.talkchess.com/forum/viewtopic.php?t=55846) by Forrest Hoch, [CCC](CCC "CCC"), April 01, 2015 » [Stockfish](Stockfish "Stockfish")
* [SD Syzygy](http://www.talkchess.com/forum/viewtopic.php?t=56124) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), April 26, 2015
* [5 men Syzygy on USB 3.0 Flash Drive](http://www.talkchess.com/forum/viewtopic.php?t=56289) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 09, 2015
* [Re: how to probe egtb from console?](http://www.talkchess.com/forum/viewtopic.php?t=56363&start=3) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), May 15, 2015 » [python-chess](Python-chess "Python-chess")
* [Gull 3 Linux+Syzygy and Fathom released](http://www.talkchess.com/forum/viewtopic.php?t=58299) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), November 20, 2015 » [Gull](Gull "Gull"), [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
* [Syzygy probing code: DTZ in some cursed endgames off by one?](http://www.talkchess.com/forum/viewtopic.php?t=58488) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), December 06, 2015


**2016**



* [Re: Squash anyone?](http://www.talkchess.com/forum/viewtopic.php?t=59175&start=4) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), February 07, 2016 [[33]](#cite_note-33)
* [My troubles with MultiPV and Syzygy in Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=59273) by [Árpád Rusz](%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [CCC](CCC "CCC"), February 16, 2016
* [Stockfish 7 and partial 6 piece syzygy problem?](http://www.talkchess.com/forum/viewtopic.php?t=59407) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 01, 2016 » [Stockfish](Stockfish "Stockfish")


 [Re: Stockfish 7 and partial 6 piece syzygy problem?](http://www.talkchess.com/forum/viewtopic.php?t=59407&start=12) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 01, 2016
* [Arasan Syzygy support (working with Windows, too)](http://www.talkchess.com/forum/viewtopic.php?t=59463) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 10, 2016 » [Arasan](Arasan "Arasan")
* [Question to syzygy author](http://www.talkchess.com/forum/viewtopic.php?t=59947) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 24, 2016
* [syzygy question](http://www.talkchess.com/forum/viewtopic.php?t=60054) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), May 04, 2016
* [question about syzygy probing](http://www.talkchess.com/forum/viewtopic.php?t=60232) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), May 21, 2016
* [Natural TB](http://www.talkchess.com/forum/viewtopic.php?t=60312) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 29, 2016 » [Stockfish](Stockfish "Stockfish")
* [syzygy questions](http://www.talkchess.com/forum/viewtopic.php?t=60722) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), July 06, 2016
* [How texel probes endgame tablebases](http://www.talkchess.com/forum/viewtopic.php?t=60833) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), July 16, 2016 » [Gaviota Tablebases](Gaviota_Tablebases "Gaviota Tablebases"), [Texel](Texel "Texel")
* [Syzygy and draw by repetition](http://www.talkchess.com/forum/viewtopic.php?t=60906) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 22, 2016 » [Draw](Draw "Draw"), [Repetitions](Repetitions "Repetitions")
* [Syzygy question](http://www.talkchess.com/forum/viewtopic.php?t=61324) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), September 03, 2016
* [Suicide chess tablebases (stalemated player wins)](http://www.talkchess.com/forum/viewtopic.php?t=61832) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [CCC](CCC "CCC"), October 25, 2016 » [Losing Chess](Losing_Chess "Losing Chess")
* [Syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=62340) by Andy Leese, [CCC](CCC "CCC"), December 01, 2016
* [Help for Syzygy probe?](http://www.talkchess.com/forum/viewtopic.php?t=62378) by [Ted Wong](index.php?title=Ted_Wong&action=edit&redlink=1 "Ted Wong (page does not exist)"), [CCC](CCC "CCC"), December 04, 2016 » [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")


**2017**



* [6-men Syzygy from HDD and USB 3.0](http://www.talkchess.com/forum/viewtopic.php?t=63652) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 04, 2017 » [Komodo](Komodo "Komodo"), [Playing Strength](Playing_Strength "Playing Strength"), [USB 3.0](Memory#USB3 "Memory")
* [Fathom memory usage](http://www.talkchess.com/forum/viewtopic.php?t=64377) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 22, 2017» [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
* [RuyDos with support for syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=64383) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), June 23, 2017 » [RuyDos](RuyDos "RuyDos")
* [Natural TB (take 2)](http://www.talkchess.com/forum/viewtopic.php?t=60312&start=240) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 22, 2017 » [Stockfish](Stockfish "Stockfish")
* [Probing tablebases through USB 3.0](http://www.talkchess.com/forum/viewtopic.php?t=65284) by [Jon Fredrik Åsvang](index.php?title=Jon_Fredrik_%C3%85svang&action=edit&redlink=1 "Jon Fredrik Åsvang (page does not exist)"), [CCC](CCC "CCC"), September 25, 2017 » [USB 3.0](Memory#USB3 "Memory")
* [understanding DTZ](http://www.talkchess.com/forum/viewtopic.php?t=65390) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), October 06, 2017 » [DTZ](Endgame_Tablebases#DTZ "Endgame Tablebases"), [Fathom](#Fathom)
* [Is there now coming changes to syzygy databases?](http://www.talkchess.com/forum/viewtopic.php?t=65713) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 13, 2017 » [DTM](Endgame_Tablebases#DTM "Endgame Tablebases"), [CFish](CFish "CFish")
* [How to Download Syzygy Endgame Tablebase Files](http://www.talkchess.com/forum/viewtopic.php?t=66096) by Daniel Johnson, [CCC](CCC "CCC"), December 23, 2017


**2018**



* [The history of Syzygy tablebases](http://www.talkchess.com/forum/viewtopic.php?t=66754) by Isaac Haïk Dunn, [CCC](CCC "CCC"), March 06, 2018
* [7-men Syzygy attempt](http://www.talkchess.com/forum/viewtopic.php?t=66797) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), March 10, 2018


 [Re: 7-men Syzygy attempt](http://talkchess.com/forum3/viewtopic.php?f=7&t=66797&start=472) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), August 19, 2018
* [Syzygy implementations of top engines](http://www.talkchess.com/forum/viewtopic.php?t=66830) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 14, 2018
* [Probing the Syzygy tablebase - beginners question](http://www.talkchess.com/forum/viewtopic.php?t=67122) by [Andreas Matthies](Andreas_Matthies "Andreas Matthies"), [CCC](CCC "CCC"), April 16, 2018
* [DTM50](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67536) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), May 22, 2018
* [Re-Pair compression questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68236) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), August 17, 2018
* [BIG NEWS! The 7 man syzygy tablebase files are complete](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68265) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), August 20, 2018
* [Technical reason why probing N-men syzygy will also probe N-1 men?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68755) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), October 28, 2018
* [7 Man Syzygy and SSD](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69309) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), December 18, 2018


**2019**



* [Testing the implementation of Syzygy](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70074) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), March 02, 2019
* [7-man Syzygy support in Fathom](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70568) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 23, 2019 » [Fathom](#Fathom)
* [Simplest use of syzygy table](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71397) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), July 28, 2019
* [SYZYGY question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71512) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 11, 2019 » [Crafty](Crafty "Crafty"), [En passant](En_passant "En passant")
* [Syzygy 7-piece - several questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71604) by [Andreas Matthies](Andreas_Matthies "Andreas Matthies"), [CCC](CCC "CCC"), August 19, 2019
* [Syzygy 7 man advice please](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71625) by Barry Clements, [CCC](CCC "CCC"), August 21, 2019
* [Syzygy DTZ data explaination?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71896) by [Nguyen Pham](Pham_Hong_Nguyen "Pham Hong Nguyen"), [CCC](CCC "CCC"), September 23, 2019


### 2020 ...


* [Almost perfect DTM tablebase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73598) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), April 08, 2020
* [What is the best way to obtain the 7-piece tablebases?](http://talkchess.com/forum3/viewtopic.php?f=2&t=74185) by [Mark Thellen](index.php?title=Mark_Thellen&action=edit&redlink=1 "Mark Thellen (page does not exist)"), [CCC](CCC "CCC"), June 15, 2020
* [Pyrrhic, Fathom for Humanoids](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74809) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 16, 2020 » [Pyrrhic](#Pyrrhic)
* [EGTB compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75396) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 14, 2020 [[34]](#cite_note-34) [[35]](#cite_note-35)
* [Syzygy bases ... question to "Syzygy Probe Depth"](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75487) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), October 21, 2020
* [Fathom and 7-men](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75906) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), November 24, 2020 » [Fathom](#Fathom)
* [Problem with Syzygy tablebase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75973) by [Elias Nilsson](index.php?title=Elias_Nilsson&action=edit&redlink=1 "Elias Nilsson (page does not exist)"), [CCC](CCC "CCC"), December 03, 2020
* [Can EGTB storage requirements be reduced using this scheme?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76010) by mmt, [CCC](CCC "CCC"), December 07, 2020


**2021**



* [Syzygy Tablebase Names: A very stupid exercise](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77267) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), May 08, 2021
* [syzygy implementation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77358) by [Desperado](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), May 23, 2021
* [When will 8 piece tablebase be ready?](http://talkchess.com/forum3/viewtopic.php?f=2&t=77400) by [Agustin Jorge Pichardo](index.php?title=Agustin_Jorge_Pichardo&action=edit&redlink=1 "Agustin Jorge Pichardo (page does not exist)"), [CCC](CCC "CCC"), May 29, 2021
* [Syzygy bases from memory](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77499) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 16, 2021 » [KPK](KPK "KPK")
* [Syzygy benefit for current SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78080) by [Jouni](index.php?title=Jouni&action=edit&redlink=1 "Jouni (page does not exist)"), [CCC](CCC "CCC"), September 02, 2021


**2022**



* [Definite occurance ranking of 7-Man EGTB](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=79938) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), May 24, 2022
* [Fathom, munmap issue](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=80522) by [Pawel Osikowski](index.php?title=Pawel_Osikowski&action=edit&redlink=1 "Pawel Osikowski (page does not exist)"), [CCC](CCC "CCC"), August 19, 2022
* [Are tablebases useless for Stockfish15?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=80608) by [Jouni](index.php?title=Jouni&action=edit&redlink=1 "Jouni (page does not exist)"), [CCC](CCC "CCC"), September 02, 2022
* [endgame table generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=80696) by [Dave Gomboc](Dave_Gomboc "Dave Gomboc"), [CCC](CCC "CCC"), September 17, 2022


**2023**



* [very strange behavior with syzygy tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=82115) by [Carbec](index.php?title=Carbec&action=edit&redlink=1 "Carbec (page does not exist)"), [CCC](CCC "CCC"), June 02, 2023
* [EGTB encoding](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=82613) by [Edmund](index.php?title=Edmund&action=edit&redlink=1 "Edmund (page does not exist)"), [CCC](CCC "CCC"), September 18, 2023


## External Links


### Tablebase


* [syzygy1/tb · GitHub](https://github.com/syzygy1/tb) by [Ronald de Man](Ronald_de_Man "Ronald de Man")
* [jromang · GitHub](https://github.com/jromang?tab=repositories) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang") has a fork from syzygy1/tb
* [python-chess/syzygy.py at master · niklasf/python-chess · GitHub](https://github.com/niklasf/python-chess/blob/master/chess/syzygy.py) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [Python](Python "Python") implementation of probing code » [python-chess](Python-chess "Python-chess")
* [niklasf/syzygy-tables.info · GitHub](https://github.com/niklasf/syzygy-tables.info) by [Niklas Fiekas](Niklas_Fiekas "Niklas Fiekas"), [GUI](GUI "GUI") and public API for Syzygy probing
* [OICS Chess and EGTB Tracker Statistics](http://oics.olympuschess.com/tracker/index.php) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)") [[36]](#cite_note-36)
* [Endgame Tablebases Online](http://kirill-kryukov.com/chess/tablebases-online/) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Index of /tablebases/syzygy (3,4,5)](http://chess.cygnitec.com/tablebases/syzygy/) by [kingliveson](Franklin_Titus "Franklin Titus")
* [tablebase.sesse.net](http://tablebase.sesse.net/) by [Sesse](Steinar_H._Gunderson "Steinar H. Gunderson")


### Fathom


* [GitHub - basil00/Fathom: Syzygy TB probe tool](https://github.com/basil00/Fathom) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli")
* [jdart1/Fathom · GitHub](https://github.com/jdart1/Fathom) by [Jon Dart](Jon_Dart "Jon Dart") (with some bug fixes and enhancements)
* [GitHub - ljgw/syzygy-bridge: Java bridge to use the Syzygy Tablebases via JNI](https://github.com/ljgw/syzygy-bridge) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen") » [FrankWalter](FrankWalter "FrankWalter")


### Pyrrhic


* [GitHub - AndyGrant/Pyrrhic: Fathom, for Humanoids](https://github.com/AndyGrant/Pyrrhic/) by [Andrew Grant](Andrew_Grant "Andrew Grant")


### Online Lookup


* [Chess Cloud Database Query Interface](https://www.chessdb.cn/queryc_en/) by [noobpwnftw](Bojun_Guo "Bojun Guo") [[37]](#cite_note-37)
* [Syzygy endgame tablebases Web Interface](https://syzygy-tables.info/)


### ChessBase


* [Syzygy Tablebases: newest, fastest, smallest](http://en.chessbase.com/post/syzygy-tablebases-newest-fastest-smallest) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 08, 2015
* [Syzygy tablebases: maximizing performance](http://en.chessbase.com/post/syzygy-tablebases-maximizing-performance) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 10, 2015
* [Endgame Turbo 4](http://shop.chessbase.com/en/products/endspiel_turbo_4) by [ChessBase](ChessBase "ChessBase")


### Misc


* [syzygy - Wiktionary](http://en.wiktionary.org/wiki/syzygy)
* [Syzygy (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy)
* [Syzygy (astronomy) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy_%28astronomy%29)
* [Syzygy (mathematics) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy_%28mathematics%29)
* [Caledonian Antisyzygy from Wikipedia](https://en.wikipedia.org/wiki/Caledonian_Antisyzygy)
* [Michael Brecker Band](Category:Michael_Brecker "Category:Michael Brecker") - [Syzygy](https://en.wikipedia.org/wiki/Michael_Brecker_(album)), [BJD 1987](https://www.bjd.sk/archiv-1979-2001#1987), [Bratislava](https://en.wikipedia.org/wiki/Bratislava), [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos


 [Michael Brecker](Category:Michael_Brecker "Category:Michael Brecker"), [Mike Stern](Category:Mike_Stern "Category:Mike Stern"), [Jeff Andrews](https://de-de.facebook.com/JeffAndrewsBassPage/), [Adam Nussbaum](Category:Adam_Nussbaum "Category:Adam Nussbaum"), [Joey Calderazzo](https://en.wikipedia.org/wiki/Joey_Calderazzo)
 
 
## References


 1. [↑](#cite_ref-1) It’s a real treat for photographers and astronomers alike: our skies are currently witnessing a phenomenon known as a syzygy — when three [celestial bodies](https://en.wikipedia.org/wiki/Astronomical_object) (or more) nearly align themselves in the sky. When celestial bodies have similar ecliptic [longitude](https://en.wikipedia.org/wiki/Longitude), this event is also known as a triple near-[conjunction](https://en.wikipedia.org/wiki/Conjunction_%28astronomy%29). Of course, this is just a trick of perspective, but this doesn't make it any less spectacular. In this case, these bodies are three [planets](https://en.wikipedia.org/wiki/Planet), and the only thing needed to enjoy the show is a clear view of the sky at sunset. Luckily, this is what happened for [ESO](https://en.wikipedia.org/wiki/European_Southern_Observatory) [photo ambassador](http://www.eso.org/public/outreach/partnerships/photo-ambassadors/) [Yuri Beletsky](http://www.eso.org/public/images/yuribeletsky/), who had the chance to spot this spectacular view from ESO's [La Silla Observatory](https://en.wikipedia.org/wiki/La_Silla_Observatory) in northern [Chile](https://en.wikipedia.org/wiki/Chile) on Sunday May 26 , 2013. Above the round domes of the [telescopes](https://en.wikipedia.org/wiki/Telescope), three of the planets in our [Solar System](https://en.wikipedia.org/wiki/Solar_System) — [Jupiter](https://en.wikipedia.org/wiki/Jupiter) (top), [Venus](https://en.wikipedia.org/wiki/Venus) (lower left), and [Mercury](https://en.wikipedia.org/wiki/Mercury_%28planet%29) (lower right) — were revealed aftersunset, engaged in their cosmic dance. An alignment like this happens only once every several years. The last one took place in May 2011, and the next one will not be until October 2015. This celestial triangle was at its best over the last week of May, but you may still be able to catch a glimpse of the three planets as they form ever-changing arrangements during their journey across the sky - source [Three Planets Dance Over La Silla | ESO](http://www.eso.org/public/images/potw1322a/), [Syzygy (astronomy) from Wikipedia](https://en.wikipedia.org/wiki/Syzygy_%28astronomy%29) 
2. [↑](#cite_ref-2) [Re: New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681&start=45) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), April 10, 2013
3. [↑](#cite_ref-3) [Re: 7-men Syzygy attempt](http://talkchess.com/forum3/viewtopic.php?f=7&t=66797&start=472) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), August 19, 2018
4. [↑](#cite_ref-4) [New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), April 01, 2013
5. [↑](#cite_ref-5) [Re: 7-piece syzygy](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=7618#p83771) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), July 03, 2014
6. [↑](#cite_ref-6) [Re: Syzygy tb generator for windows](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=7396#p83338) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), June 01, 2014
7. [↑](#cite_ref-7) [7-men Syzygy attempt](http://www.talkchess.com/forum/viewtopic.php?t=66797) by [Bojun Guo](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), March 10, 2018
8. [↑](#cite_ref-8) [Powered by Ronald de Man's Syzygy endgame tablebases, 7-piece tables generated by Bojun Guo and a public API hosted by lichess.org](https://syzygy-tables.info/), August 19, 2018
9. [↑](#cite_ref-9) [Index of /tables/standard/7/ on lichess](http://tablebase.lichess.ovh/tables/standard/7/), August 19, 2018
10. [↑](#cite_ref-10) [Re: What is the best way to obtain the 7-piece tablebases?](http://talkchess.com/forum3/viewtopic.php?f=2&t=74185&sid=016570559fa97e785404dd65020c0ad6&start=20#p848245) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), June 22, 2020
11. [↑](#cite_ref-11) [Re: What is the best way to obtain the 7-piece tablebases?](http://talkchess.com/forum3/viewtopic.php?t=74185&start=30#p848394) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), June 23, 2020
12. [↑](#cite_ref-12) [Re: SSD and the use of Tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47931&start=2) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), May 08, 2013
13. [↑](#cite_ref-13) [Re: New 6-piece tablebases](http://www.talkchess.com/forum/viewtopic.php?t=47681&start=8) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), April 05, 2013
14. [↑](#cite_ref-14) [Endgame Turbo 4](http://shop.chessbase.com/en/products/endspiel_turbo_4) by [ChessBase](ChessBase "ChessBase")
15. [↑](#cite_ref-15) [Syzygy Tablebases: newest, fastest, smallest](http://en.chessbase.com/post/syzygy-tablebases-newest-fastest-smallest) by [Albert Silver](Albert_Silver "Albert Silver"), [ChessBase News](ChessBase "ChessBase"), February 08, 2015
16. [↑](#cite_ref-16) [Gull 3 Linux+Syzygy and Fathom released](http://www.talkchess.com/forum/viewtopic.php?t=58299) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli"), [CCC](CCC "CCC"), November 20, 2015
17. [↑](#cite_ref-17) [GitHub - basil00/Fathom: Syzygy TB probe tool](https://github.com/basil00/Fathom) by [Basil Falcinelli](Basil_Falcinelli "Basil Falcinelli")
18. [↑](#cite_ref-18) [jdart1/Fathom · GitHub](https://github.com/jdart1/Fathom) by [Jon Dart](Jon_Dart "Jon Dart")
19. [↑](#cite_ref-19) [7-man Syzygy support in Fathom](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70568) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 23, 2019
20. [↑](#cite_ref-20) [Pyrrhic, Fathom for Humanoids](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74809) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 16, 2020
21. [↑](#cite_ref-21) [GitHub - AndyGrant/Pyrrhic: Fathom, for Humanoids](https://github.com/AndyGrant/Pyrrhic/)
22. [↑](#cite_ref-22) <https://github.com/glinscott/fishtest/wiki/UsefulData> Collection of useful data concerning SF
23. [↑](#cite_ref-23) [Re: New 6-piece tablebase generator](http://kirill-kryukov.com/chess/discussion-board/viewtopic.php?f=6&t=6971&start=6) by [syzygy](Ronald_de_Man "Ronald de Man"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), April 06, 2013
24. [↑](#cite_ref-24) [Retrograde tablebase methods](http://www.open-chess.org/viewtopic.php?f=5&t=779) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 26, 2010
25. [↑](#cite_ref-25) [Leapfrog: Retrograde Analysis](http://home.hccnet.nl/h.g.muller/EGT7/retro.html) from [Leapfrog tablebase generator](http://home.hccnet.nl/h.g.muller/EGT7/7-men.html) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller")
26. [↑](#cite_ref-26) [Jesper Torp Kristensen](Jesper_Torp_Kristensen "Jesper Torp Kristensen") (**2005**). *[Generation and compression of endgame tables in chess with fast random access using OBDDs](https://issuu.com/jespertk/docs/master_thesis)*. Master thesis, supervisor [Peter Bro Miltersen](Mathematician#Miltersen "Mathematician"), [Aarhus University](https://en.wikipedia.org/wiki/Aarhus_University)
27. [↑](#cite_ref-27) [OBDD - Ordered Binary Decision Diagram from Wikipedia](https://en.wikipedia.org/wiki/Binary_decision_diagram)
28. [↑](#cite_ref-28) [Re: Almost perfect DTM tablebase](http://talkchess.com/forum3/viewtopic.php?f=7&t=73598) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), April 15, 2020
29. [↑](#cite_ref-29) [Re: Stash has lost 2 game because of NO EGTB](http://talkchess.com/forum3/viewtopic.php?f=2&t=76927#p888045) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), March 25, 2021
30. [↑](#cite_ref-30) [Guy Haworth](Guy_Haworth "Guy Haworth") (**2014**). *Chess Endgame News*. [ICGA Journal, Vol. 37, No. 2](ICGA_Journal#37_2 "ICGA Journal")
31. [↑](#cite_ref-31) [Found an interesting research](https://plus.google.com/100454521496393505718/posts/5C252LggQQS) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), April, 12, 2013
32. [↑](#cite_ref-32) [Wine (software) from Wikipedia](https://en.wikipedia.org/wiki/Wine_%28software%29)
33. [↑](#cite_ref-33) [N. Jesper Larsson](https://scholar.google.de/citations?user=8pKMsLMAAAAJ&hl=en), [Alistair Moffat](http://findanexpert.unimelb.edu.au/display/person13222) (**1999**). *[Offline Dictionary-Based Compression](http://dl.acm.org/citation.cfm?id=789701)*. [DCC'99](http://www.cs.brandeis.edu//~dcc/Programs/Program1999.pdf), [pdf](http://www.larsson.dogma.net/dcc99.pdf)
34. [↑](#cite_ref-34) [LZ4 (compression algorithm) from Wikipedia](https://en.wikipedia.org/wiki/LZ4_(compression_algorithm))
35. [↑](#cite_ref-35) [Zstandard from Wikipedia](https://en.wikipedia.org/wiki/Zstandard)
36. [↑](#cite_ref-36) [BitTorrent from Wikipedia](https://en.wikipedia.org/wiki/BitTorrent)
37. [↑](#cite_ref-37) [ChessDBCN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71764) by [noobpwnftw](Bojun_Guo "Bojun Guo"), [CCC](CCC "CCC"), September 09, 2019

**[Up one level](Endgame_Tablebases "Endgame Tablebases")**







 
