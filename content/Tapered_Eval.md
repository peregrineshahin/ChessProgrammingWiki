---
title: Tapered Eval
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Tapered Eval**



[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Ad Parnassum, 1932 <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
**Tapered Eval**,  

a technique used in evaluation to make a smooth transition between the [phases of the game](Game_Phases "Game Phases") using a fine grained numerical game phase value considering type of captured pieces so far. The technique requires aggregating two distinct [scores](Score "Score") for the position, with weights corresponding to the [opening](Opening "Opening") and [endgame](Endgame "Endgame"). The current game phase is then used to [interpolate](https://en.wikipedia.org/wiki/Interpolation) between these values. The idea behind Tapered Eval is to remove [evaluation discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity"). 



### Contents


* [1 History](#history)
* [2 Implementation example](#implementation-example)
* [3 See also](#see-also)
* [4 Selected Publications](#selected-publications)
* [5 Forum Posts](#forum-posts)
	+ [5.1 2005 ...](#2005-...)
	+ [5.2 2010 ...](#2010-...)
	+ [5.3 2015 ...](#2015-...)
	+ [5.4 2020 ...](#2020-...)
* [6 External Links](#external-links)
* [7 References](#references)






Though Tapered Eval has been used for many years (for example [The King](The_King "The King"), as [described](The_King#Description "The King") in 1991 <a id="cite-note-3" href="#cite-ref-3">[3]</a> and [Phalanx](Phalanx "Phalanx")), and was already mentioned by [Hans Berliner](Hans_Berliner "Hans Berliner") in 1979 <a id="cite-note-4" href="#cite-ref-4">[4]</a>, the technique gained massive popularity only during the past few years, with the release of [Fruit](Fruit "Fruit") and the growing awareness among programmers of the sensitivity of the evaluation function to discontinuity. <a id="cite-note-5" href="#cite-ref-5">[5]</a>. [Zurichess](Zurichess "Zurichess") by [Alexandru Moșoi](Alexandru_Mosoi "Alexandru Mosoi") uses the [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) library for [automated tuning](Automated_Tuning "Automated Tuning") - in a two layers [neural network](Neural_Networks "Neural Networks"), the second layer is for phasing endgame and middlegame scores <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



## Implementation example


Tapered Eval is done as follows in [Fruit](Fruit "Fruit") (similar implementations can be found in engines like [Crafty](Crafty "Crafty") and [Stockfish](Stockfish "Stockfish") etc.). The scaling looks like this:




```

eval = ((opening * (256 - phase)) + (endgame * phase)) / 256

```

Where *opening* is the evaluation of the position with middle game in mind (e.g. keep kings protected behind their pawn covers) and *endgame* is the evaluation with endgame in mind (e.g. activate the kings). Both these evaluations are done in parallel when evaluating a position.


The *phase* is evaluated like this (code specifics left out):




```

PawnPhase = 0
KnightPhase = 1
BishopPhase = 1
RookPhase = 2
QueenPhase = 4
TotalPhase = PawnPhase*16 + KnightPhase*4 + BishopPhase*4 + RookPhase*4 + QueenPhase*2

phase = TotalPhase

phase -= wp * PawnPhase // Where wp is the number of white pawns currently on the board
phase -= wn * Knight    // White knights
...
phase -= br * RookPhase
phase -= bq * QueenPhase

phase = (phase * 256 + (TotalPhase / 2)) / TotalPhase

```

## See also


* [Evaluation Discontinuity](Evaluation_Discontinuity "Evaluation Discontinuity")
* [Evaluation Philosophy](Evaluation_Philosophy "Evaluation Philosophy")
* [Game Phases](Game_Phases "Game Phases")
* [Neural Networks](Neural_Networks "Neural Networks")
* [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")
* [Stockfish Evaluation Guide](Stockfish#EvaluationGuide "Stockfish")


## Selected Publications


* [Hans Berliner](Hans_Berliner "Hans Berliner") (**1979**). *[On the Construction of Evaluation Functions for Large Domains](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/)*. [III. Smoothness](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/#sec-3), [IJCAI 1979](Conferences#IJCAI1979 "Conferences"), Tokyo, Vol. 1


## Forum Posts


### 2005 ...


* [designing neural networks](http://www.talkchess.com/forum/viewtopic.php?t=16162) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), August 31, 2007
* [Re: Lemming Poll](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=220004&t=23894) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), September 22, 2008 » [Crafty](Crafty "Crafty"), [LearningLemming](LearningLemming "LearningLemming")
* [Superlinear interpolator: a nice novelity ?](http://www.talkchess.com/forum/viewtopic.php?t=23860) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 20, 2008 » [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [Re: talk about IPP's evaluation](http://www.talkchess.com/forum/viewtopic.php?p=301746#301746) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), November 07, 2009 » [Ippolit](Ippolit "Ippolit"), [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")


### 2010 ...


* [My experience with Linux/GCC](http://www.talkchess.com/forum/viewtopic.php?t=38523) by [Richard Vida](Richard_Vida "Richard Vida"), [CCC](CCC "CCC"), March 23, 2011 » [C](C "C"), [Linux](Linux "Linux"), [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [two values in one integer](http://www.talkchess.com/forum/viewtopic.php?t=42054) by [Pierre Bokma](index.php?title=Pierre_Bokma&action=edit&redlink=1 "Pierre Bokma (page does not exist)"), [CCC](CCC "CCC"), January 18, 2012
* [Tapered evaluation](http://www.talkchess.com/forum/viewtopic.php?t=51656) by [Marco Pampaloni](Marco_Pampaloni "Marco Pampaloni"), [CCC](CCC "CCC"), March 18, 2014
* [advanced tapered evalutation](http://www.talkchess.com/forum/viewtopic.php?t=53220) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), August 08, 2014 » [SSE](SSE "SSE")


### 2015 ...


* [Why do some programs evaluate MidGame and EndGame together?](http://www.talkchess.com/forum/viewtopic.php?t=55519) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), March 01, 2015
* [Tapered Eval](http://www.talkchess.com/forum/viewtopic.php?t=57181) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), August 05, 2015
* [is phase a good indicator of game progress?](http://www.talkchess.com/forum/viewtopic.php?t=60565) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), June 23, 2016 » [Game Phases](Game_Phases "Game Phases")
* [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=4) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016 » [Deep Learning](Deep_Learning "Deep Learning"), [Zurichess](Zurichess "Zurichess")
* [Tapered Evaluation Questions](http://www.talkchess.com/forum/viewtopic.php?t=61571) by Jayakiran Akurathi, [CCC](CCC "CCC"), October 01, 2016
* [couple of questions about stockfish code ?](http://www.talkchess.com/forum/viewtopic.php?t=61850) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 26, 2016 » [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques"), [Stockfish](Stockfish "Stockfish")
* [Define end game](http://www.talkchess.com/forum/viewtopic.php?t=62153) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), November 16, 2016 » [Endgame](Endgame "Endgame")
* [Early / middle / end game transitions?](http://www.open-chess.org/viewtopic.php?f=5&t=3088) by notachessplayer, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2017
* [Four game phases](https://groups.google.com/d/msg/fishcooking/8h-TH6YckMI/uFUb6H6eDAAJ) by [Stefan Geschwentner](Stefan_Geschwentner "Stefan Geschwentner"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 20, 2017 » [Stockfish](Stockfish "Stockfish")
* [Tapered Eval between 4 phases](http://www.talkchess.com/forum/viewtopic.php?t=65466) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 16, 2017


 [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum/viewtopic.php?t=65466&start=4) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), October 16, 2017 » [Winter](Winter "Winter")
 [Re: Tapered Eval between 4 phases](http://www.talkchess.com/forum3/viewtopic.php?t=65466&start=7) by [Youri Matiounine](Youri_Matiounine "Youri Matiounine"), [CCC](CCC "CCC"), October 16, 2017 » [AVX2](AVX2 "AVX2")
* [Re: New uci engine: Rofchade](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68311&start=19) by [Ronald Friederich](Ronald_Friederich "Ronald Friederich"), [CCC](CCC "CCC"), August 28, 2018 » [RofChade](RofChade "RofChade"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Four-way evaluation trick?](https://groups.google.com/d/msg/fishcooking/6grLq5OEr9g/ERbVn0uDBQAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 07, 2018 » [Stockfish](Stockfish "Stockfish")
* [mg vs eg eval](https://groups.google.com/d/msg/fishcooking/znU1a7aZ2XI/yJDFtOQnAwAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 06, 2019 » [Middlegame](Middlegame "Middlegame"), [Endgame](Endgame "Endgame"), [Stockfish](Stockfish "Stockfish")


### 2020 ...


* [Tapered Evaluation and MSE (Texel Tuning)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76265) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 10, 2021 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")
* [Evaluation tapering methods](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77474) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), June 12, 2021
* [Game Phase and tapered PSQT evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77546) by Jon12345, [CCC](CCC "CCC"), June 23, 2021 » [PeSTO's Evaluation Function](PeSTO%27s_Evaluation_Function "PeSTO's Evaluation Function")


## External Links


* [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/) » [Stockfish Evaluation Guide](Stockfish#EvaluationGuide "Stockfish")
* [Tapered Eval](http://mediocrechess.blogspot.com/2011/10/guide-tapered-eval.html) from [Mediocre Chess](http://mediocrechess.varten.org/index.html) by [Jonatan Pettersson](Jonatan_Pettersson "Jonatan Pettersson")
* [Taper from Wikipedia](https://en.wikipedia.org/wiki/Taper)
* [Cone (geometry) from Wikipedia](https://en.wikipedia.org/wiki/Cone_%28geometry%29)
* [Interpolation from Wikipedia](https://en.wikipedia.org/wiki/Interpolation)
* [Fuzzy logic from Wikipedia](https://en.wikipedia.org/wiki/Fuzzy_logic)
* [T-norm fuzzy logics from Wikipedia](https://en.wikipedia.org/wiki/T-norm_fuzzy_logics)
* [Linear taper potentiometer from Wikipedia](https://en.wikipedia.org/wiki/Potentiometer#Linear_taper_potentiometer)
* [Sigmoid function from Wikipedia](https://en.wikipedia.org/wiki/Sigmoid_function)
* [Association P.C.](Category:Association_P.C. "Category:Association P.C.") - Frau Theunissen´s Kegel, [Erna Morena](http://www.discogs.com/Association-PC-Erna-Morena/master/248647) (1973), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 [Pierre Courbois](Category:Pierre_Courbois "Category:Pierre Courbois"), [Jasper van 't Hof](Category:Jasper_van_%27t_Hof "Category:Jasper van 't Hof"), [Toto Blanke](Category:Toto_Blanke "Category:Toto Blanke"), [Sigi Busch](https://de.wikipedia.org/wiki/Sigi_Busch), and [Heiner Wiberny](https://de.wikipedia.org/wiki/Heiner_Wiberny)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - [Ad Parnassum](https://en.wikipedia.org/wiki/File:Polyphony2.JPG), 1932, oil colors, stamped lines, dots stamped in white color and later repainted, on casein paint on canvas on stretcher frame, [Museum of Fine Arts Berne](https://en.wikipedia.org/wiki/Museum_of_Fine_Arts_Berne), [Paul Klee from Wikipedia](https://en.wikipedia.org/wiki/Paul_Klee)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Gradus ad Parnassum - Wikipedia](https://en.wikipedia.org/wiki/Gradus_ad_Parnassum)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Don Beal](Don_Beal "Don Beal") (**1991**). *Report on the [11th World Microcomputer Chess Championship](WMCCC_1991 "WMCCC 1991")*. [ICCA Journal, Vol. 14, No. 2](ICGA_Journal#14_2 "ICGA Journal")
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Hans Berliner](Hans_Berliner "Hans Berliner") (**1979**). *[On the Construction of Evaluation Functions for Large Domains](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/)*. [III. Smoothness](http://www.bkgm.com/articles/Berliner/EvaluationFunctionsLargeDomains/#sec-3), [IJCAI 1979](Conferences#IJCAI1979 "Conferences"), Tokyo, Vol. 1
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: Secrets of Rybka and Fruit from my point of view](https://www.stmintz.com/ccc/index.php?id=470681) by [Stuart Cracraft](Stuart_Cracraft "Stuart Cracraft"), [CCC](CCC "CCC"), December 15, 2005
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Re: Deep Learning Chess Engine ?](http://www.talkchess.com/forum/viewtopic.php?t=60883&start=1) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), July 21, 2016

**[Up one level](Evaluation "Evaluation")**







 
