---
title: ShashChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* [Stockfish](Stockfish "Stockfish") \* ShashChess**


**ShashChess**,  

a [Stockfish](Stockfish "Stockfish") [derivative](Category:Derivative "Category:Derivative") by [Andrea Manzo](Andrea_Manzo "Andrea Manzo") with the aim to apply the proposals of [Alexander Shashin](index.php?title=Alexander_Shashin&action=edit&redlink=1 "Alexander Shashin (page does not exist)") as exposed in his book *Best Play: A New Method for Discovering the Strongest Move* <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
<a id="cite-note-3" href="#cite-ref-3">[3]</a>.
First released in July 2018 <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
subsequent ShashChess versions feature [skill levels](Playing_Strength "Playing Strength") and handicap modes, [NNUE](NNUE "NNUE"), [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search") with one or multiple [threads](Thread "Thread") in conjunction with [alpha-beta](Alpha-Beta "Alpha-Beta"),
and various [learning](Learning "Learning") techniques utilizing a [persistent hash table](Persistent_Hash_Table "Persistent Hash Table") <a id="cite-note-5" href="#cite-ref-5">[5]</a>
<a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### Contents


* [1 Personalities](#personalities)
* [2 Q-Learning](#q-learning)
* [3 Forum Posts](#forum-posts)
	+ [3.1 2018 ...](#2018-...)
	+ [3.2 2020 ...](#2020-...)
* [4 External Links](#external-links)
* [5 References](#references)






Based on static [evaluation](Evaluation "Evaluation") [score](Score "Score") ranges derivered from [pawn](Pawn "Pawn") endgame [point value](Point_Value "Point Value") (PawnValueEg = 208), ShashChess classifies the position with five personalities of three former [World Chess Champions](https://en.wikipedia.org/wiki/World_Chess_Championship),
[Tigran Petrosian](https://en.wikipedia.org/wiki/Tigran_Petrosian) for negative scores,
[José Raúl Capablanca](https://en.wikipedia.org/wiki/Jos%C3%A9_Ra%C3%BAl_Capablanca) for balanced scores,
and [Mikhail Tal](https://en.wikipedia.org/wiki/Mikhail_Tal) for positive scores <a id="cite-note-7" href="#cite-ref-7">[7]</a>:




```C++

if      (eval < -74) personality =  Petosian;
else if (eval < -31) personality =  Petosian | Capablanca;
else if (eval <  31) personality =             Capablanca;
else if (eval <  74) personality =             Capablanca | Tal;
else                 personality =                          Tal; 

```

These personalities are considered in various [search selectivity](Selectivity "Selectivity") thresholds, along with multiple dynamic evaluation score adjustments. 



## Q-Learning


A [rote learning](https://en.wikipedia.org/wiki/Rote_learning) technique inspired from [Q-learning](Reinforcement_Learning#Q-Learning "Reinforcement Learning"), worked out and introduced by [Kelly Kinyama](index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)")
<a id="cite-note-8" href="#cite-ref-8">[8]</a>
<a id="cite-note-9" href="#cite-ref-9">[9]</a> 
and also employed in [BrainLearn](index.php?title=BrainLearn&action=edit&redlink=1 "BrainLearn (page does not exist)") 9.0 <a id="cite-note-10" href="#cite-ref-10">[10]</a>,
was applied in ShashChess since version 12.0 <a id="cite-note-11" href="#cite-ref-11">[11]</a>. 
After the end of a decisive selfplay game, the [list of moves](Move_List "Move List") (ml) and associated [scores](Score "Score") is merged into the learn table from end to start, 
the score of timestep t adjusted as weighted average with the future reward of timestep t+1, using a [learning rate](https://en.wikipedia.org/wiki/Q-learning#Learning_Rate) α of 0.5 and a [discount factor](https://en.wikipedia.org/wiki/Q-learning#Discount_factor) γ of 0.99 <a id="cite-note-12" href="#cite-ref-12">[12]</a>:




```C++

  for (t = ml.size() - 2; t >= 0; t--) {
    ml[t].score = (1-α)*ml[t].score + α*γ*ml[t+1].score;
    insertIntoOrUpdateLearningTable( ml[t] );
  }

```

During repeated selfplay games, subsequently playing along the learned best line so far, decreasing score adjustments will stimulate exploration of alternative siblings, while increasing score adjustments correspondents to exploitation of the best move.



## Forum Posts


### 2018 ...


* [ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), July 28, 2018


 [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=103) (11.0) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), March 06, 2020
 [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=105) (12.0) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), June 28, 2020
 [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=209) (15.0) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), October 03, 2020
 [Re: ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093&start=272) (17.1) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), June 01, 2021
* [Build ShashChess for Android](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68120&p=769919) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), August 01, 2018


### 2020 ...


* [ShashChess 12.0](https://groups.google.com/g/fishcooking/c/GLag32ARtKo/m/3Zoaq3-rAwAJ) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020
* [A new reinforcement learning implementation of Q learning algorithm for alphabeta engines to automatically tune the evaluation of chess positions](https://groups.google.com/g/fishcooking/c/6IzmiSCB8lg/m/sFeSq9ykAQAJ) by [Kelly Kinyama](index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 29, 2020
* [ShashChess NNUE 1.0](https://groups.google.com/d/msg/fishcooking/yWtpz_FY5_Y/RMTG56fkAAAJ) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020
* [Shashchess which executable to use](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76394) by Andrew Bernasrd, [CCC](CCC "CCC"), January 23, 2021
* [New BrainLearn and ShashChess](https://groups.google.com/g/fishcooking/c/Iy1AlEZJWc8) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 19, 2021


## External Links


* [GitHub - amchess/ShashChess: A try to implement Alexander Shashin's theory on a Stockfish's derived chess engine](https://github.com/amchess/ShashChess)
* [ShashChess 11.0 64-bit](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=ShashChess%2011.0%2064-bit) in [CCRL 40/15](CCRL "CCRL")
* [ShashChess 15.0 64-bit](https://ccrl.chessdom.com/ccrl/4040/cgi/engine_details.cgi?print=Details&each_game=1&eng=ShashChess%2015.0%2064-bit) in [CCRL 40/15](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Welcome to BS Chess](http://www.bs-chess.com/latin/lectures/2011/shashin4.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Alexander Shashin](index.php?title=Alexander_Shashin&action=edit&redlink=1 "Alexander Shashin (page does not exist)") (**2013**). *Best Play: A New Method for Discovering the Strongest Move*. [Mongoose Press](https://mongoosepress.com/), [Amazon](https://www.amazon.com/Best-Play-Discovering-Strongest-2013-01-01/dp/B01A0CKJQM)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Review: Best Play | ChessVibes](https://web.archive.org/web/20130909054429/http://www.chessvibes.com/review-best-play) by [Arne Moll](https://ratings.fide.com/profile/1005820), September 05, 2013 ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [ShashChess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68093) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [CCC](CCC "CCC"), July 28, 2018
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ShashChess/README.md at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/README.md)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Komodo MCTS](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=70948&start=17) by [Mark Lefler](Mark_Lefler "Mark Lefler"), [CCC](CCC "CCC"), June 12, 2019 » [Komodo MCTS](Komodo#MCTS "Komodo")
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [ShashChess/search.cpp at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/src/All/search.cpp#L446)
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Re: Self-Learning stockfish upgraded](https://groups.google.com/g/fishcooking/c/fhX7dFAsyew/m/NSd0-OJjBwAJ) by [Kelly Kinyama](index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 28, 2019
9. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [A new reinforcement learning implementation of Q learning algorithm for alphabeta engines to automatically tune the evaluation of chess positions](https://groups.google.com/g/fishcooking/c/6IzmiSCB8lg/m/sFeSq9ykAQAJ) by [Kelly Kinyama](index.php?title=Kelly_Kinyama&action=edit&redlink=1 "Kelly Kinyama (page does not exist)"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 29, 2020
10. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [Release BrainLearn 9.0 · amchess/BrainLearn · GitHub](https://github.com/amchess/BrainLearn/releases/tag/9.0)
11. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [ShashChess 12.0](https://groups.google.com/g/fishcooking/c/GLag32ARtKo/m/3Zoaq3-rAwAJ) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), June 28, 2020
12. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [ShashChess/search.cpp at master · amchess/ShashChess · GitHub](https://github.com/amchess/ShashChess/blob/master/src/All/search.cpp#L2625)

**[Up one Level](Stockfish "Stockfish")**







 
