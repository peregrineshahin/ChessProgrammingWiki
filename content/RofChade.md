---
title: RofChade
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RofChade**


**RofChade**, (rofChade)  

an [UCI](UCI "UCI") compliant chess engine by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), written in [C++](Cpp "Cpp"). While its over the board tournament debut already occured at the [PT 53](PT_53 "PT 53") in Spring 2018, RofChade was first released in August 2018.
However, the program's name was already established after the author made first attempts in chess programming in the 90s, combining his initials and [rochade](https://nl.wikipedia.org/wiki/Rochade), the Dutch term for [castling](Castling "Castling") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Despite initially using a [tapered eval](Tapered_Eval "Tapered Eval") of [middlegame](Middlegame "Middlegame") and [endgame](Endgame "Endgame") [material](Material "Material") and asymmetrical [piece-square tables](Piece-Square_Tables "Piece-Square Tables") only, 
albeit [Texel tuned](Texel%27s_Tuning_Method "Texel's Tuning Method") and along with a sophisticated [parallel search](Parallel_Search "Parallel Search"), RofChade **1.0** nevertheless already played in the 2700+ Elo range <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
RofChade 2.0 in December 2018, came with an improved [evaluation](Evaluation "Evaluation") considering [pawn structure](Pawn_Structure "Pawn Structure") and [king safety](King_Safety "King Safety").



### Contents


* [1 Tournament Play](#tournament-play)
* [2 Photos & Games](#photos-.26-games)
* [3 Features](#features)
	+ [3.1 Board Representation](#board-representation)
	+ [3.2 Search](#search)
	+ [3.3 Evaluation](#evaluation)
* [4 See also](#see-also)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2018 ...](#2018-...)
	+ [5.2 2020 ...](#2020-...)
* [6 External Links](#external-links)
* [7 References](#references)






RofChade had its over the board tournament debut at the [PT 53](PT_53 "PT 53") [CSVN Programmers Tournament](CSVN_Programmers_Tournament "CSVN Programmers Tournament"), and further played the [PT 54](PT_54 "PT 54"), the [PT 55](PT_55 "PT 55") (2nd behind [Komodo](Komodo "Komodo")), and won the [PT 56](PT_56 "PT 56"). Online, at the [WCRCC 2018](WCRCC_2018 "WCRCC 2018"), RofChade won versus [Chiron](Chiron "Chiron") and Komodo in the regular rounds, and all three programs finished with 8½/11 so that a playoff was neccessary to decide about the winner, where finally the commercial program succeeded with RofChade strong third. Since February 2019 at [TCEC Season 14](TCEC_Season_14 "TCEC Season 14"), RofChade successfully plays at [TCEC](TCEC "TCEC"), promoting to the [First Division](TCEC_Season_16#First "TCEC Season 16"). 



## Photos & Games


 [](https://www.csvn.nl/index.php/nieuws/51-toernooien/819-pt54-round-7) 
[PT 54](PT_54 "PT 54") round 7, [Jonny](Jonny "Jonny") vs. RofChade operated by their authors [Johannes Zwanzger](Johannes_Zwanzger "Johannes Zwanzger") and [Ronald Friederich](Ronald_Friederich "Ronald Friederich") <a id="cite-note-3" href="#cite-ref-3">[3]</a>




```

[Event "CSVN PT 54"]
[Site "Leiden"]
[Date "2018.12.02"]
[Round "7"]
[White "Jonny"]
[Black "Rofchade"]
[Result "1/2-1/2"]
[ECO "E00"]
[EventDate "2018.12.02"]

1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.g3 Bb4+ 5.Bd2 Be7 6.Bg2 Nbd7 7.O-O O-O 8.Qb3 c6
9.Bf4 a5 10.Rd1 Nh5 11.Bd2 Nhf6 12.Nc3 a4 13.Nxa4 dxc4 14.Qc2 b5 15.Nc3 Qb6
16.a4 b4 17.Ne4 Nxe4 18.Qxe4 Ra5 19.Be3 Qa6 20.Rdc1 Rxa4 21.Rxa4 Qxa4 22.Nd2
Ba6 23.Qxc6 Bb5 24.Qc7 Qa6 25.Bb7 Qb6 26.Bf4 Qa7 27.Nxc4 Bd8 28.Qc8 Bf6
29.Qc7 Bd8 30.Qc8 Bf6 31.Qc7 Bd8 1/2-1/2

```

## Features


<a id="cite-note-4" href="#cite-ref-4">[4]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Staged Move Generation](Move_Generation#Staged "Move Generation")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Captures](Captures "Captures")
		- [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
		- [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [Relative History Heuristic](Relative_History_Heuristic "Relative History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Razoring](Razoring "Razoring")
	+ [Check Extensions](Check_Extensions "Check Extensions") if [SEE >= 0](Static_Exchange_Evaluation "Static Exchange Evaluation")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [King Safety](King_Safety "King Safety")


## See also


* [PeSTO](PeSTO "PeSTO")
* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")


## Forum Posts


### 2018 ...


* [New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 27, 2018


 [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 28, 2018 » [Tapered Eval](Tapered_Eval "Tapered Eval"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [rofChade 2.0 released, first version with regular eval](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69330) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), December 20, 2018
* [New release: rofChade 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70593) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), April 26, 2019
* [New release: rofChade 2.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71745) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), September 06, 2019


### 2020 ...


* [New release: rofChade 2.3](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73719) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), April 21, 2020
* [Re: A Crossroad in Computer Chess; Or Desperate Flailing for Relevance](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75247&start=15) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), September 29, 2020 » [NNUE](NNUE "NNUE")


## External Links


* [RofChade – a UCI Chess Engine](http://rofchade.nl/)
* [RofChade](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=RofChade&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Thanks – RofChade](http://rofchade.nl/?page_id=106)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [RofChade 1.0 64-bit](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=RofChade%201.0%2064-bit#RofChade_1_0_64-bit) in [CCRL 40/40](CCRL "CCRL")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [PT54 Round 7](https://www.csvn.nl/index.php/nieuws/51-toernooien/819-pt54-round-7), Photo by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> based on [Technical – RofChade](http://rofchade.nl/?page_id=116), December 2018
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 28, 2018

**[Up one Level](Engines "Engines")**







 
