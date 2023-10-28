---
title: Fire
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Fire**

\[ Fire <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Fire**, (Firebird, Fire xTreme)

an [UCI](UCI "UCI") compliant chess engine by [Norman Schmidt](Norman_Schmidt "Norman Schmidt") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, until version 3.0 derived from [IvanHoe](IvanHoe "IvanHoe") and the [Ippolit](Ippolit "Ippolit") series of programs with some help of [Milos Stanisavljevic](Milos_Stanisavljevic "Milos Stanisavljevic"). Initially called Firebird, and later renamed to Fire due to a trademark naming conflict <a id="cite-note-3" href="#cite-ref-3">[3]</a>, it was released as open source, Fire licensed under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation"). The sources were later closed with [Windows](Windows "Windows") executables available for download for recent [Intel](Intel "Intel") processors <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Fire features [magic bitboards](Magic_Bitboards "Magic Bitboards"), it can be configured with more than 70 UCI options, and applies a [SMP parallel search](Parallel_Search "Parallel Search"). Since April 2021 with Fire **8.1**, the program is [open source](Category:Open_Source "Category:Open Source") again <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 Fire 4](#fire-4)
- [2 Fire 5, Fire 6.1](#fire-5.2c-fire-6.1)
- [3 Fire 7.1](#fire-7.1)
- [4 Fire 8](#fire-8)
- [5 See also](#see-also)
- [6 Forum Posts](#forum-posts)
  - [6.1 2010 ...](#2010-...)
  - [6.2 2015 ...](#2015-...)
  - [6.3 2020 ...](#2020-...)
- [7 External Links](#external-links)
  - [7.1 Chess Engine](#chess-engine)
  - [7.2 Misc](#misc)
- [8 References](#references)

## Fire 4

Fire **4**, released in December 2014, was a compete re-write and does not use any source code from or related to [Ippolit](Ippolit "Ippolit"). It supports [Syzygy Bases](Syzygy_Bases "Syzygy Bases"), and includes a revamped memory management which uses [OpenMP](https://en.wikipedia.org/wiki/OpenMP) [#pragmas](https://en.wikipedia.org/wiki/C_preprocessor#Compiler-specific_preprocessor_features) to utilize [thread local storage](https://en.wikipedia.org/wiki/Thread-local_storage) <a id="cite-note-6" href="#cite-ref-6">[6]</a> and minimize the amount of 'shared' resources among [threads](Thread "Thread") for its [SMP implementation](Parallel_Search "Parallel Search"). [Testing](Engine_Testing "Engine Testing") was done via massive parallel, automated 24/7 ultra-fast chess engine matches using [Cutechess-cli](Cutechess-cli "Cutechess-cli") and [LittleBlitzer](LittleBlitzer "LittleBlitzer"). Code changes were tested to a very high level of confidence using [LOS](Match_Statistics#Likelihood_of_superiority "Match Statistics") and [SPRT](Match_Statistics#SPRT "Match Statistics") (min. 40,000 games) against a pool of top engines. Development and testing included approx. 200,000 - 240,000 ultra-fast games per day <a id="cite-note-7" href="#cite-ref-7">[7]</a>. According to a [CCC](CCC "CCC") posting by anonymous poster cucumber in September 2020, but in contradiction to Norman Schmidt's later statement <a id="cite-note-8" href="#cite-ref-8">[8]</a>, Fire 4 was later released as open source engine [Seagull](Gull#SeaGull "Gull") based on [Gull](Gull "Gull"), hiding its Fire 4 origin <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

## Fire 5, Fire 6.1

Fire **5**, released in November 2016, improved with new [evaluation](Evaluation "Evaluation") terms, and [SPSA](SPSA "SPSA") tuned evaluation and [search](Search "Search") parameters, and supports [Chess960](Chess960 "Chess960"). Fire **6.1**, released in September 2017, added approximately 30-40 Elo in [playing strength](Playing_Strength "Playing Strength") <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## Fire 7.1

Fire **7.1** from May 27, 2018 <a id="cite-note-11" href="#cite-ref-11">[11]</a>, was announced as the **last** public release of Fire <a id="cite-note-12" href="#cite-ref-12">[12]</a>. Its private successor, Fire **8_beta** won the [League 1](TCEC_Season_19#First "TCEC Season 19") of [TCEC Season 19](TCEC_Season_19 "TCEC Season 19") in summer 2020, and qualified for the top eight in the [Premier Division](TCEC_Season_19#Premier "TCEC Season 19").
On September 18, 2020, [Ethereal](Ethereal "Ethereal") author [Andrew Grant](Andrew_Grant "Andrew Grant") published a *Fire 7.1* [GPLv3](Free_Software_Foundation#GPL "Free Software Foundation") Source Request in [CCC](CCC "CCC"), since he believes that some or all of Fire is likely to fall under the GPLv3, as it is inherited from [Stockfish's](Stockfish "Stockfish") GPLv3 license <a id="cite-note-13" href="#cite-ref-13">[13]</a>.

## Fire 8

Fire **8** with smaller and highly tuned evaluation was released on Februray 23, 2021 <a id="cite-note-14" href="#cite-ref-14">[14]</a>.
The further optimized Fire **8.1** was released on April 16, 2021 as [open source](Category:Open_Source "Category:Open Source"), licensed under the [GNU GPL](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-15" href="#cite-ref-15">[15]</a>. **Fire_8.N**, released on May 22, 2021, features [NNUE](NNUE "NNUE") by utilizing a modified version of [Daniel Shawul's](Daniel_Shawul "Daniel Shawul") [ScorpioNNUE](Scorpio#ScorpioNNUE "Scorpio") probing code along with a [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") net created by [Sergio Vieri](Sergio_Vieri "Sergio Vieri") <a id="cite-note-16" href="#cite-ref-16">[16]</a>.

## See also

- [FireFly](FireFly "FireFly")
- [Firenzina](Firenzina "Firenzina")
- [IvanHoe](IvanHoe "IvanHoe")
- [Phoenix](Phoenix "Phoenix")

## Forum Posts

## 2010 ...

- [Firebird 1.0....](http://www.talkchess.com/forum/viewtopic.php?t=31664) by [Dr.Wael Deeb](index.php?title=Dr.Wael_Deeb&action=edit&redlink=1 "Dr.Wael Deeb (page does not exist)"), [CCC](CCC "CCC"), January 12, 2010
- [GGT + Firebird wins Amar Gambit + related chess notes +](http://www.talkchess.com/forum/viewtopic.php?t=32218) by [Rainer Neuhäusler](index.php?title=Rainer_Neuh%C3%A4usler&action=edit&redlink=1 "Rainer Neuhäusler (page does not exist)"), [CCC](CCC "CCC"), January 30, 2010
- [Firebird wins Ware Gambit](http://www.talkchess.com/forum/viewtopic.php?t=32301) by [Rainer Neuhäusler](index.php?title=Rainer_Neuh%C3%A4usler&action=edit&redlink=1 "Rainer Neuhäusler (page does not exist)"), [CCC](CCC "CCC"), February 02, 2010
- [I should mention that I also made a few small fixes to fire](http://www.talkchess.com/forum/viewtopic.php?t=38348) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), March 09, 2011
- [Houdini, Fire, IvanHoe, (and Rybka?) are 'clones'...?](http://www.talkchess.com/forum/viewtopic.php?t=38932) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), April 30, 2011
- [Fire 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=50463) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), December 13, 2013

## 2015 ...

- [Fire 4 for linux](http://www.talkchess.com/forum/viewtopic.php?t=56855) by Lucas Braesch, [CCC](CCC "CCC"), July 03, 2015
- [Fire 5](http://www.talkchess.com/forum/viewtopic.php?t=60329) by [Rainer Neuhäusler](index.php?title=Rainer_Neuh%C3%A4usler&action=edit&redlink=1 "Rainer Neuhäusler (page does not exist)"), [CCC](CCC "CCC"), May 31, 2016
- [Fire 5 is out!](http://www.talkchess.com/forum/viewtopic.php?t=62127) by [Dmitri Gusev](Dmitri_Gusev "Dmitri Gusev"), [CCC](CCC "CCC"), November 14, 2016
- [Fire 6 is available!](http://www.talkchess.com/forum/viewtopic.php?t=65253) by Anton Ross, [CCC](CCC "CCC"), September 22, 2017

[Re: Fire 6 is available!](http://www.talkchess.com/forum/viewtopic.php?t=65253&start=18) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), September 23, 2017

- [Fire 7](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67513) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), May 21, 2018
- [Fire 7.1](http://www.talkchess.com/forum3/viewtopic.php?t=67579) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), May 27, 2018

## 2020 ...

- [Fire question!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75046) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), [CCC](CCC "CCC"), September 08, 2020
- [Fire 7.1 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75150) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 18, 2020 » [Stockfish](Stockfish "Stockfish")

[Re: Fire 7.1 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75150&start=170) by cucumber, [CCC](CCC "CCC"), September 23, 2020 » [Seagull](Gull#SeaGull "Gull")

- [Fire 8 released](https://prodeo.actieforum.com/t287-fire-8-released) by matejst, [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), February 25, 2021
- [Fire 8 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=76719) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), February 26, 2021 (Engine Origins)

[Re: Fire 8 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=76719&start=3) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), February 26, 2021

- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=243) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), April 19, 2021
- [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=358) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), May 22, 2021
- [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [NNUE](NNUE "NNUE")

## [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=58) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), June 17, 2021 External Links

## Chess Engine

- [Fire Chess Engine](https://chesslogik.wixsite.com/fire)
- [ABOUT | fire](https://chesslogik.wixsite.com/fire/about)
- [GitHub - FireFather/fire: a very strong, state-of-the-art, highly optimized, open-source freeware UCI chess engine...](https://github.com/FireFather/fire)
- [Fire – the chess engine releases a new version](http://www.chessdom.com/fire-the-chess-engine-releases-a-new-version/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), October 02, 2017 » [TCEC Season 10](TCEC_Season_10 "TCEC Season 10")
- [Fire](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Fire&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Fire from Wikipedia](https://en.wikipedia.org/wiki/Fire)
- [Portal:Fire from Wikipedia](https://en.wikipedia.org/wiki/Portal:Fire)
- [Fire (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Fire_%28disambiguation%29)
- [Fire (classical element) from Wikipedia](https://en.wikipedia.org/wiki/Fire_%28classical_element%29)
- [Fire ecology from Wikipedia](https://en.wikipedia.org/wiki/Fire_ecology)
- [Firefighting from Wikipedia](https://en.wikipedia.org/wiki/Firefighting)
- [Fire protection from Wikipedia](https://en.wikipedia.org/wiki/Fire_protection)
- [List of fires from Wikipedia](https://en.wikipedia.org/wiki/List_of_fires)
- [Arson from Wikipedia](https://en.wikipedia.org/wiki/Arson)
- [Conflagration from Wikipedia](https://en.wikipedia.org/wiki/Conflagration)
- [Pyromania from Wikipedia](https://en.wikipedia.org/wiki/Pyromania)
- [Quest for Fire (film) from Wikipedia](https://en.wikipedia.org/wiki/Quest_for_Fire_%28film%29)
- [Firebird from Wikipedia](https://en.wikipedia.org/wiki/Firebird)
- [Firebird (database server) from Wikipedia](https://en.wikipedia.org/wiki/Firebird_%28database_server%29)
- [The Foundation for Individual Rights in Education - FIRE](http://thefire.org/)
- [The Rolling Stones](Category:The_Rolling_Stones "Category:The Rolling Stones") - [Play with Fire](<https://en.wikipedia.org/wiki/Play_with_Fire_(The_Rolling_Stones_song)>) (1965), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Photo of a fire](https://en.wikipedia.org/wiki/File:Fire.JPG) taken with a 1/4000th of a second [exposure](https://en.wikipedia.org/wiki/Exposure_%28photography%29) by Awesomoman, 2009, [Fire from Wikipedia](https://en.wikipedia.org/wiki/Fire)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Fire 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=50463&start=5) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 13, 2013
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chess Engine List](http://computer-chess.org/doku.php?id=computer_chess:wiki:lists:chess_engine_list) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Fire 3.0 released](http://www.talkchess.com/forum/viewtopic.php?t=50463) by Stefan Pohl, [CCC](CCC "CCC"), December 13, 2013
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GitHub - FireFather/fire: a very strong, state-of-the-art, highly optimized, open-source freeware UCI chess engine...](https://github.com/FireFather/fire)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Use Thread-local Storage to Reduce Synchronization | Intel® Developer Zone](https://software.intel.com/en-us/articles/use-thread-local-storage-to-reduce-synchronization), November 2, 2011
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> Information provided by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), July 2015
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Fire 8 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=10&t=76719&start=3) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), February 26, 2021 (Engine Origins)
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [Re: Fire 7.1 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75150&start=170) by cucumber, [CCC](CCC "CCC"), September 23, 2020
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Fire – the chess engine releases a new version](http://www.chessdom.com/fire-the-chess-engine-releases-a-new-version/), [Chessdom](index.php?title=Chessdom&action=edit&redlink=1 "Chessdom (page does not exist)"), October 02, 2017
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [Fire 7.1](http://www.talkchess.com/forum3/viewtopic.php?t=67579) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), May 27, 2018
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [ABOUT | fire](https://web.archive.org/web/20200913090350/https://chesslogik.wixsite.com/fire/about) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), September 13, 2020)
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [Fire 7.1 GPLv3 Source Request](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75150) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 18, 2020
1. <a id="cite-ref-14" href="#cite-note-14">[14]</a> [History | fire](https://chesslogik.wixsite.com/fire/history)
1. <a id="cite-ref-15" href="#cite-note-15">[15]</a> [GitHub - FireFather/fire: a very strong, state-of-the-art, highly optimized, open-source freeware UCI chess engine...](https://github.com/FireFather/fire)
1. <a id="cite-ref-16" href="#cite-note-16">[16]</a> [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=358) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), May 22, 2021

**[Up one Level](Engines "Engines")**

