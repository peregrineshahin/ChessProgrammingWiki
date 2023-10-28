---
title: Nirvanachess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Nirvanachess**



[ Mahavira's Nirvana <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Nirvanachess**, (Nirvana)  

an [UCI](UCI "UCI") compliant chess engine by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), written in [C++](Cpp "Cpp"), first released in April 2013 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. Nirvanachess applies a [principal variation search](Principal_Variation_Search "Principal Variation Search") with a four bucket [transposition table](Transposition_Table "Transposition Table"), [null move pruning](Null_Move_Pruning "Null Move Pruning"), [late move reduction](Late_Move_Reductions "Late Move Reductions"), and [futility pruning](Futility_Pruning "Futility Pruning") and [razoring](Razoring "Razoring") with [CLOP](CLOP "CLOP") optimized margins inside an [iterative deepening framework](Iterative_Deepening "Iterative Deepening") with [aspiration windows](Aspiration_Windows "Aspiration Windows"), [move ordering](Move_Ordering "Move Ordering") improved by the [killer heuristics](Killer_Heuristic "Killer Heuristic"). Its [evaluation](Evaluation "Evaluation") uses [material](Material "Material") and [piece-squares tables](Piece-Square_Tables "Piece-Square Tables"), and further places emphasis on [mobility](Mobility "Mobility"), [pawn structure](Pawn_Structure "Pawn Structure") with focus on [passed pawns](Passed_Pawn "Passed Pawn") and [pawn chains](Pawn_Chain "Pawn Chain"), and [king safety](King_Safety "King Safety"), considing [pawn storms](King_Safety#PawnStorm "King Safety"), how many [squares around the king](King_Pattern#KingAttacks "King Pattern") are attacked by how many attackers, and the quality of the [pawn shelter](King_Safety#PawnShield "King Safety") <a id="cite-note-3" href="#cite-ref-3">[3]</a>. Nirvana **2.0**, released in December 2014, was a complete rewrite using [bitboards](Bitboards "Bitboards") instead of a [10x12 board](10x12_Board "10x12 Board") with an improved evaluation and a [parallel search](Parallel_Search "Parallel Search") using the [lazy SMP](Lazy_SMP "Lazy SMP") approach <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Nirvanachess **2.1** improved due to [singular extensions](Singular_Extensions#RestrictedSE "Singular Extensions"), [logistic regression tuning](Automated_Tuning#LogisticRegression "Automated Tuning") aka [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method") of evaluation weights, as well as [SPSA](SPSA "SPSA") tuning for pruning margins <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>. 



### Contents


* [1 Forum Posts](#forum-posts)
	+ [1.1 2013](#2013)
	+ [1.2 2014](#2014)
	+ [1.3 2015 ...](#2015-...)
	+ [1.4 2020 ...](#2020-...)
* [2 External Links](#external-links)
	+ [2.1 Chess Engine](#chess-engine)
	+ [2.2 Misc](#misc)
* [3 References](#references)






### 2013


* [Nirvanachess 1.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=47750) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), April 10, 2013
* [Nirvanachess 1.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=48186) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), June 03, 2013
* [Nirvanachess 1.2 Release](http://www.talkchess.com/forum/viewtopic.php?t=49053) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), August 22, 2013
* [Nirvanachess 1.3 Release](http://www.talkchess.com/forum/viewtopic.php?t=50039) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), November 12, 2013


### 2014


* [Nirvanachess 1.4 Release](http://www.talkchess.com/forum/viewtopic.php?t=50839) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), January 09, 2014
* [Nirvanachess 1.5 Release](http://www.talkchess.com/forum/viewtopic.php?t=51500) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), March 05, 2014
* [Hyper Bullet Rating List](http://www.talkchess.com/forum/viewtopic.php?p=560787) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), March 08, 2014
* [Nirvanachess 1.6 Release](http://www.talkchess.com/forum/viewtopic.php?t=52041) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), April 18, 2014
* [Nirvanachess 1.7 Release](http://www.talkchess.com/forum/viewtopic.php?t=52846) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), July 03, 2014
* [Nirvanachess 1.8 Release](http://www.talkchess.com/forum/viewtopic.php?t=53448) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), August 27, 2014
* [Transposition Table Oddity](http://www.talkchess.com/forum/viewtopic.php?p=590030) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), September 28, 2014
* [Nirvanachess 2.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=54671) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), December 17, 2014


### 2015 ...


* [Nirvanachess 2.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=56239) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), May 05, 2015
* [Nirvanachess 2.2 Release](http://www.talkchess.com/forum/viewtopic.php?t=57948) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), October 15, 2015
* [Nirvanachess 2.3 Release](http://www.talkchess.com/forum/viewtopic.php?t=61001) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), July 31, 2016
* [Nirvanachess 2.4 Release](http://nirvanachess.blogspot.com/2017/08/nirvanachess-24-release.html) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), Nirvanachess, August 11, 2017 <a id="cite-note-7" href="#cite-ref-7">[7]</a>


### 2020 ...


* [Nirvanachess 2.5 Release](http://nirvanachess.blogspot.com/2020/12/nirvanachess-25-release.html) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), Nirvanachess, December 06, 2020
* [Nirvanachess 2.5 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76012) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), December 07, 2020


## External Links


### Chess Engine


* [Nirvanachess](http://nirvanachess.blogspot.com/)
* [NirvanaChess 1.7 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=NirvanaChess%201.7%2064-bit#NirvanaChess_1_7_64-bit) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [nirvana - Wiktionary](https://en.wiktionary.org/wiki/nirvana)
* [Nirvana (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Nirvana_%28disambiguation%29)
* [Nirvana from Wikipedia](https://en.wikipedia.org/wiki/Nirvana)
* [Nirvana (Buddhism) from Wikipedia](https://en.wikipedia.org/wiki/Nirvana_%28Buddhism%29)
* [Nirvana](Category:Nirvana "Category:Nirvana") - [Smells Like Teen Spirit](https://en.wikipedia.org/wiki/Smells_Like_Teen_Spirit) (1991), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Mahavira's](https://en.wikipedia.org/wiki/Mahavira) [Nirvana](https://en.wikipedia.org/wiki/Nirvana) or [Moksha](https://en.wikipedia.org/wiki/Moksha). Note the crescent shaped [Siddhashila](https://en.wikipedia.org/wiki/Siddhashila) (a place where all [Siddhas](https://en.wikipedia.org/wiki/Siddha) reside after Nirvana). Folio 53r from [Kalpa Sūtra](https://en.wikipedia.org/wiki/Kalpa_S%C5%ABtra) series, loose leaf manuscript, [Patan, Gujarat](https://en.wikipedia.org/wiki/Patan,_Gujarat), ca. 1472, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Nirvanachess 1.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=47750) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), April 10, 2013
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Nirvanachess](http://nirvanachess.blogspot.com/)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Nirvanachess 2.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=54671) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), December 17, 2014
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Nirvanachess: Nirvanachess 2.1 Release](http://nirvanachess.blogspot.de/2015/05/nirvanachess-21-release.html), May 04, 2015
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Nirvanachess 2.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=56239) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), May 05, 2015
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Nirvanachess 2.4 has been released](http://www.talkchess.com/forum/viewtopic.php?t=64904) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), August 15, 2017

**[Up one level](Engines "Engines")**







 
