---
title: Texel27s Tuning Method
---
**[Home](Home "Home") \* [Automated Tuning](Automated_Tuning "Automated Tuning") \* Texel's Tuning Method**



[ Texel and Gaviotas stay tuned on [Ynys Echni](https://en.wikipedia.org/wiki/Flat_Holm) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Texel's Tuning Method**,  

by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund") as applied to [Texel 1.03](Texel#1.03 "Texel") and following versions <a id="cite-note-2" href="#cite-ref-2">[2]</a> is a concrete instance of a [logistic regression](Automated_Tuning#LogisticRegression "Automated Tuning") <a id="cite-note-3" href="#cite-ref-3">[3]</a> . This page is a slightly edited reprint of a reply to [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué") <a id="cite-note-4" href="#cite-ref-4">[4]</a> and subsequent postings in a [CCC](CCC "CCC") discussion about [automated tuning](Automated_Tuning "Automated Tuning") initiated by [Tom Likens](Tom_Likens "Tom Likens") in January 2014 <a id="cite-note-5" href="#cite-ref-5">[5]</a> . As mentioned in a further reply <a id="cite-note-6" href="#cite-ref-6">[6]</a> , a similar technique was already proposed by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora") in 2009, as applied to [Gaviota](Gaviota "Gaviota") <a id="cite-note-7" href="#cite-ref-7">[7]</a> . 



## Advantages


One big advantage of this method is that it can simultaneously optimize several hundreds of evaluation function parameters in a reasonable amount of time. The first step that collects a set of games does not take any extra time, because those games have already been played when previous changes to the engine were tested. The step that converts from [PGN](Portable_Game_Notation "Portable Game Notation") to FEN only takes a few minutes. The time consuming step is to compute the local minimum. In my engine M is currently around 400 and computing the gradient takes around 25 minutes on a 16-core Dell T620 computer <a id="cite-note-16" href="#cite-ref-16">[16]</a> . A local minimum can usually be computed within 6 hours, faster if only small changes to the parameter values are needed.


While 6 hours may seem like a lot, consider how long it would take [CLOP](CLOP "CLOP") to simultaneously optimize 400 parameters (assuming you have enough memory to actually do that). I have not worked out the math but I guess it would take at least ten years to get reliable results.


Another advantage is that no external source of [knowledge](Knowledge "Knowledge") is needed. You don't need to find a large set of games played by engines or humans that are stronger than the engine you want to improve. While this may not be a practical advantage for the current [strength](Playing_Strength "Playing Strength") of my engine, I still find this property theoretically pleasing, somewhat similar to the concept of self [calibration](https://en.wikipedia.org/wiki/Calibration) <a id="cite-note-17" href="#cite-ref-17">[17]</a> .


A third advantage is that the need for different evaluation terms to be "[orthogonal](https://en.wikipedia.org/wiki/Orthogonality#Statistics.2C_econometrics.2C_and_economics)" disappears, since the optimization will automatically deal with dependencies between evaluation terms.


A fourth advantage, compared to the method used by [Amir Ban](Amir_Ban "Amir Ban") to tune the [Junior](Junior "Junior") evaluation function <a id="cite-note-18" href="#cite-ref-18">[18]</a> , is that my method does not need the implementation of a "drawishness" function in the chess engine.



## Concerns


My biggest concern about this method is what is called [Correlation does not imply causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation) in statistics. I don't have a specific example for chess, but the Wikipedia example about ice cream sales and drowning accidents is quite illuminating. It is a known fact that when ice cream sales increase, so does drowning accidents, but that does not imply that stopping ice cream sales would reduce the number of [drowning](https://en.wikipedia.org/wiki/Drowning) accidents. It is conceivable that the chess engine would learn to appreciate positional features that are correlated to increased winning chances, even though actively striving to reach such positions does not increase winning chances. Anyway the method does work in my engine, possibly because of the counter argument that "Correlation is not causation but it sure is a hint".


Another concern is that the chess engine will not be able to learn things that it does not understand at all. For example, assume the chess engine did not know how to win [KBNK endings](KBNK_Endgame "KBNK Endgame"), so all games leading to this endgame would end in a draw. Because of this E would tend to be smaller if the evaluation functions scored all KBNK endings as draws, so there is a risk the evaluation actually gets worse after optimization.


On the other hand, the algorithm can be expected to improve the engine's knowledge about things that it partially already knows, or knowledge about things that are good even if you don't know it. For example, assume the engine does not know that the bishop pair deserves a bonus. However, if the engine has general knowledge about mobility it is likely that it will win more than it loses anyway when it has the bishop pair advantage. Therefore the engine will be able to learn that the bishop pair deserves a bonus. If the algorithm is then repeated with a new set of games, the engine might learn that the bishop pair is even better when it knows that it should not unnecessarily trade a bishop.


It may also be argued that since more than one position is picked from each game (in fact about 140 positions per game on average), the result is invalid because there is a dependence between terms in the summation that defines E, but least squares theory in general assumes that different data points are independent. The way I see it, E has contributions from 64000 independent events and the fact that there are 140 times more terms in the summation is similar to what would happen if you solved a weighted least squares problem where the weights are determined by how often a particular type of position is present in typical games.


While it would probably be better (or at least equally good) to take one position each from 8.8 million different games, obtaining that many games would require more computation time than I am willing to spend. I believe 64000 independent events is more than enough to estimate 400 parameters anyway.



## Results


When I started using this method, I calculated that K=1.13 best matched the then current evaluation function in my engine. I have not changed the value of K since then and do not intend to change it in the future either, since it is just an arbitrary scaling constant.


Since 2014-01-01 when the first evaluation change based on this algorithm was included in my engine, the Elo improvements caused by evaluation weight tuning (measured using 32000 games at 1+0.08) have been:




```C++
24.6 + 4.0 + 5.8 + 2.8 + 12.8 + 39.4 + 10.2 = 99.6 Elo

```

The 24.6 improvement was when I made most of the evaluation parameters accessible to the optimization algorithm. The next three improvements came when I in three stages exposed more evaluation parameters to the algorithm. The 12.8 improvement came when I re-created the set of test positions based on the most recently played games.


The 39.4 improvement came when I changed the criteria for which positions to include in the test set. Initially I removed also all positions where the q-search score deviated too much from the search score in the actual game (which conveniently is saved by [cutechess-cli](Cutechess-cli "Cutechess-cli") in PGN comments). I believed that including those positions would just raise the "noise level" of the data and cause a worse solution to be found. Apparently this is not the case. I now believe that even though including these positions causes noise, the q-search function has to deal with them all the time in real games, so trying to learn how those positions should be evaluated on average is still beneficial.


The 10.2 improvement came when I added separate queen piece square tables for middle game and end game. Previously texel only had one queen PST, which had horizontal, vertical and diagonal symmetry.


The last improvement was made after the texel 1.03 release. The others are included in the 1.03 release and I believe they are responsible for most of the [strength](Playing_Strength "Playing Strength") increase in texel 1.03.


I don't know if the large strength increase was made possible because the method is good or because the texel evaluation function was particularly bad before I started using this algorithm. Anyway I don't expect to be able to get equally big improvements in the future as I got in texel 1.03, but I hope the algorithm will nevertheless help finding a fair amount of smaller evaluation improvements.



## Future improvements


Currently local search is used to find a local optimum. I believe it would be faster to initially use a few Gauss-Newton iterations and then switch to local search when the remaining corrections are small.


A number of evaluation parameters have values that appear quite unintuitive. For example, the value of a white queen on b7/g7 (and a black queen on b2/g2 because of symmetry) in the middle game has a value of -128[cp](Centipawns "Centipawns"). I have not investigated the cause yet, but I believe the explanation is that almost always when a white/black queen is on b7/b2 in the early middle game, it is because it has just eaten the "[poisoned pawn](https://en.wikipedia.org/wiki/Poisoned_Pawn_Variation)", and the opponent is about to win back a pawn by playing Rb1 and Rxb7. If placing the queen on b7/g7/b2/g2 for other reasons is much less common, the optimization algorithm will assign a large penalty for a queen on these squares. While this improves the evaluation function in the average case, it will also cause large evaluation errors for the uncommon cases that do not fall under the "poisoned pawn" category. Implementing a more specific rule about poisoned pawns could be profitable.


Other examples of odd parameter values include a white king on b8 which in the middle game gives white a 200cp bonus, a white knight on a8 in the middle game which gives white a 223cp penalty, the pawn race bonus which is only 157cp even though it is supposed to trigger only when one side can promote a queen and the opponent can not.


Investigating the cause for these and other odd looking parameter values may suggest further improvements to the evaluation function.


Another interesting approach is to apply data mining techniques on the residuals to try to discover missing knowledge in the evaluation function. I don't know how successful this approach will be. It may be more profitable to test different variants of already known chess evaluation principles instead.



## Pseudo Code


of a local optimization routine <a id="cite-note-19" href="#cite-ref-19">[19]</a>




```C++
vector<int> localOptimize(const vector<int>& initialGuess) {
   const int nParams = initialGuess.size();
   double bestE = E(initialGuess);
   vector<int> bestParValues = initialGuess;
   bool improved = true;
   while ( improved ) {
      improved = false;
      for (int pi = 0; pi < nParams; pi++) {
         vector<int> newParValues = bestParValues;
         newParValues[pi] += 1;
         double newE = E(newParValues);
         if (newE < bestE) {
            bestE = newE;
            bestParValues = newParValues;
            improved = true;
         } else {
            newParValues[pi] -= 2;
            newE = E(newParValues);
            if (newE < bestE) {
               bestE = newE;
               bestParValues = newParValues;
               improved = true;
            }
         }
      }
   }
   return bestParValues;
}

```

## See also


* [Arasan's Tuning](Arasan#Tuning "Arasan")
* [Eval Tuning in Deep Thought](Eval_Tuning_in_Deep_Thought "Eval Tuning in Deep Thought")
* [GLEM](Michael_Buro#GLEM "Michael Buro") by [Michael Buro](Michael_Buro "Michael Buro")
* [Gosu](Gosu "Gosu")
* [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")
* [RuyTune](RuyTune "RuyTune")
* [Texel's Tuning Video | Wukong JS](Wukong_JS#TexelTuningVideo "Wukong JS") by [Maksim Korzh](Maksim_Korzh "Maksim Korzh")
* [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")


## Forum Posts


### 2009


* [Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009 » [Gaviota](Gaviota "Gaviota")


### 2014


* [How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), January 07, 2014


 [Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=10) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 08, 2014
* [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=26) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014


 [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=27) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 31, 2014 » [Cross-entropy from Wikipedia](https://en.wikipedia.org/wiki/Cross_entropy) 
 [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=40) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 05, 2014
 [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum3/viewtopic.php?t=50823&start=70) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), Mar 04, 2014 » [Regularization from Wikipedia](https://en.wikipedia.org/wiki/Regularization_(mathematics)) 
* [Texel tuning method](https://groups.google.com/forum/#!topic/fishcooking/QJPG9MS8tCA) by vdb..., [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 31, 2014 » [Stockfish](Stockfish "Stockfish")
* [Tune cut margins with Texel/gaviota tuning method](http://www.talkchess.com/forum/viewtopic.php?t=53657) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 11, 2014
* [A little improvement to the Texel's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=54021) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), October 11, 2014


### 2015 ...


* [Optimization algorithm for the Texel/Gaviota tuning method](http://www.talkchess.com/forum/viewtopic.php?t=55265) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), February 09, 2015
* [Experiments with eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=55621) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 10, 2015 » [Arasan](Arasan "Arasan")
* [txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 18, 2015 <a id="cite-note-20" href="#cite-ref-20">[20]</a>


 [Re: txt: automated chess engine tuning](http://www.talkchess.com/forum/viewtopic.php?t=55696&start=108) by [Sergei S. Markoff](Sergei_Markoff "Sergei Markoff"), [CCC](CCC "CCC"), February 15, 2016 » [SmarThink](SmarThink "SmarThink")
* [Re: Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168&start=30) by [Marcel van Kervinck](Marcel_van_Kervinck "Marcel van Kervinck"), [CCC](CCC "CCC"), May 03, 2015 » [Point Value by Regression Analysis](Point_Value_by_Regression_Analysis "Point Value by Regression Analysis")


 [Re: Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168&start=36) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), May 04, 2015 » [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning")
* [test positions for texel tuning](http://www.talkchess.com/forum/viewtopic.php?t=57700) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), September 20, 2015
* [Why computing K that minimizes the sigmoid func. value?...](http://www.talkchess.com/forum/viewtopic.php?t=58298) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), November 19, 2015


 [Re: Why computing K that minimizes the sigmoid func. value?](http://www.talkchess.com/forum/viewtopic.php?t=58298&start=43) by [Thomas Kolarik](Thomas_Kolarik "Thomas Kolarik"), [CCC](CCC "CCC"), November 27, 2015 » [Nirvanachess](Nirvanachess "Nirvanachess")
 [Re: Why computing K that minimizes the sigmoid func. value?](http://www.talkchess.com/forum/viewtopic.php?t=58298&start=46) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), November 29, 2015
 [Re: Why computing K that minimizes the sigmoid func. value?](http://www.talkchess.com/forum/viewtopic.php?t=58298&start=52) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), December 07, 2015 » [Andscacs](Andscacs "Andscacs")
**2016**



* [Tuning](http://www.open-chess.org/viewtopic.php?f=5&t=2987) by ppyvabw, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), June 11, 2016
* [GreKo 2015 ML: tuning evaluation (article in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=60902) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [CCC](CCC "CCC"), July 22, 2016 » [GreKo](GreKo "GreKo")
* [training data to use with Texel Tuning method](http://www.talkchess.com/forum/viewtopic.php?t=61427) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), September 14, 2016
* [Python script for TTM](http://www.talkchess.com/forum/viewtopic.php?t=61856) by Lucas Braesch, [CCC](CCC "CCC"), October 28, 2016 » [Python](Python "Python")
* [A database for learning evaluation functions](http://www.talkchess.com/forum/viewtopic.php?t=61861) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), October 28, 2016 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Evaluation](Evaluation "Evaluation"), [Learning](Learning "Learning")
* [Texel tuning - some issues](http://www.talkchess.com/forum/viewtopic.php?t=62440) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), December 10, 2016


**2017**



* [improved evaluation function](http://www.talkchess.com/forum/viewtopic.php?t=63408) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi"), [CCC](CCC "CCC"), March 11, 2017 » [Zurichess](Zurichess "Zurichess")
* [Texel tuning method with a small number of positions](http://www.talkchess.com/forum/viewtopic.php?t=63542) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), March 23, 2017
* [Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), June 05, 2017


 [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=35) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), June 07, 2017
 [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=42) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), July 20, 2017 » [Python](Python "Python")
 [Re: Texel tuning method question](http://www.talkchess.com/forum/viewtopic.php?t=64189&start=46) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), July 23, 2017
* [Impressive Texel-tuning results](http://www.talkchess.com/forum/viewtopic.php?t=64310) by [Sander Maassen vd Brink](index.php?title=Sander_Maassen_vd_Brink&action=edit&redlink=1 "Sander Maassen vd Brink (page does not exist)"), [CCC](CCC "CCC"), June 16, 2017 » [chess22k](Chess22k "Chess22k")
* [Cooking Cheese with Texel's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=64313) by [Patrice Duhamel](Patrice_Duhamel "Patrice Duhamel"), [CCC](CCC "CCC"), June 16, 2017 » [Cheese](Cheese "Cheese")
* [cursed parameters in Texel tuning](http://www.talkchess.com/forum/viewtopic.php?t=64338) by [Pawel Koziol](Pawel_Koziol "Pawel Koziol"), [CCC](CCC "CCC"), June 18, 2017
* [Troubles with Texel Tuning](http://www.talkchess.com/forum/viewtopic.php?t=65290) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 26, 2017
* [Texel Tuning - Success!](http://www.talkchess.com/forum/viewtopic.php?t=65538) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 24, 2017
* [tuning for the uninformed](http://www.talkchess.com/forum/viewtopic.php?t=65799) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), November 23, 2017
* [how to create a labeled epd from pgn?](http://www.talkchess.com/forum/viewtopic.php?t=65881) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), December 02, 2017 » [EPD](Extended_Position_Description "Extended Position Description"), [PGN](Portable_Game_Notation "Portable Game Notation")


**2018**



* [texel tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67614) by [Folkert van Heusden](Folkert_van_Heusden "Folkert van Heusden"), [CCC](CCC "CCC"), June 01, 2018
* [Texel Tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=67893) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), July 03, 2018
* [Texel tuning speed](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=68326) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 29, 2018
* [Texel tuning for piece values](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69194) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), December 08, 2018


### 2020 ...


* [Tool and data for Texel Tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74221) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), June 18, 2020
* [Question on Texel's Tuning Method](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74416) by Josh Odom, [CCC](CCC "CCC"), July 08, 2020 <a id="cite-note-21" href="#cite-ref-21">[21]</a>
* [Evaluation & Tuning in Chess Engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74877) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), August 24, 2020 » [Ethereal](Ethereal "Ethereal")


**2021**



* [Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 05, 2021


 [Re: Help with Texel's tuning](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76238&start=15) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), January 07, 2021 » [Wukong JS](Wukong_JS "Wukong JS")
* [Tapered Evaluation and MSE (Texel Tuning)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76265) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 10, 2021 » [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Training data](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76288) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), January 12, 2021
* [Texel tuning variant](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76380) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), January 21, 2021
* [Reinforcement learning project](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76465) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), January 31, 2021 » [Reinforcement Learning](Reinforcement_Learning "Reinforcement Learning")
* [A hybrid of SPSA and local optimization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77420) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), June 01, 2021 » [SPSA](SPSA "SPSA")


**2022**



* [Re: Devlog of Leorik - A.k.a. how to tune high-quality PSTs from scratch (material values) in 20 seconds](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79049&start=127) by [Thomas Jahn](Thomas_Jahn "Thomas Jahn"), [CCC](CCC "CCC"), March 28, 2022 » [Automated Tuning](Automated_Tuning "Automated Tuning"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [Leorik](Leorik "Leorik")


## External Links


* [Logistic regression from Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
* [The texel way of tuning](http://macechess.blogspot.de/2014/03/the-texel-way-of-tuning_10.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), March 10, 2014 » [iCE](ICE "ICE")
* [Some more tuning results](http://macechess.blogspot.de/2014/03/some-more-tuning-results.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), March 22, 2014
* [NEWUOA from Wikipedia](https://en.wikipedia.org/wiki/NEWUOA) <a id="cite-note-22" href="#cite-ref-22">[22]</a>
* [zurichess/txt — Bitbucket](https://bitbucket.org/zurichess/txt) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi")
* [Самообучение шахматной программы / Хабрахабр](https://habrahabr.ru/post/305604/) by [Vladimir Medvedev](Vladimir_Medvedev "Vladimir Medvedev"), [Habrahabr](https://en.wikipedia.org/wiki/Habrahabr), July 21, 2016 (Russian) [translated](https://translate.google.com/translate?sl=ru&tl=en&js=y&prev=_t&hl=de&ie=UTF-8&u=https%3A%2F%2Fhabrahabr.ru%2Fpost%2F305604%2F&edit-text=) by [Google Translate](https://en.wikipedia.org/wiki/Google_Translate) » [GreKo](GreKo "GreKo")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Texel sheep](https://en.wikipedia.org/wiki/Texel_%28sheep%29) and [gulls](https://en.wikipedia.org/wiki/Gull), [Flat Holm Island](https://en.wikipedia.org/wiki/Flat_Holm), [Wales](https://en.wikipedia.org/wiki/Wales), Photo by [Sam Whitfield](http://www.flickr.com/people/8007352@N06), March 20, 2010, [Category:Texel (sheep) - Wikimedia Commons](http://commons.wikimedia.org/wiki/Category:Texel_%28sheep%29)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=555522&t=50823) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), January 31, 2014 » [Automated Tuning](Automated_Tuning "Automated Tuning")
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: Piece weights with regression analysis (in Russian)](http://www.talkchess.com/forum/viewtopic.php?t=56168&start=36) by [Fabien Letouzey](Fabien_Letouzey "Fabien Letouzey"), [CCC](CCC "CCC"), May 04, 2015
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Re: How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=10) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), January 08, 2014
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [How Do You Automatically Tune Your Evaluation Tables](http://www.talkchess.com/forum/viewtopic.php?t=50823) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), January 07, 2014
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=28) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), January 31, 2014
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Re: Insanity... or Tal style?](http://www.talkchess.com/forum/viewtopic.php?t=27266&postdays=0&postorder=asc&topic_view=&start=11) by [Miguel A. Ballicora](Miguel_A._Ballicora "Miguel A. Ballicora"), [CCC](CCC "CCC"), April 02, 2009
8. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Partition of sums of squares - Wikipedia](https://en.wikipedia.org/wiki/Partition_of_sums_of_squares)
9. <a id="cite-ref-9" href="#cite-note-9">↑</a> [Re: Why computing K that minimizes the sigmoid func. value?](http://www.talkchess.com/forum/viewtopic.php?t=58298&start=46) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), November 29, 2015
10. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Sigmoid function from Wikipedia](https://en.wikipedia.org/wiki/Sigmoid_function)
11. <a id="cite-ref-11" href="#cite-note-11">↑</a> [Logistic function from Wikipedia](https://en.wikipedia.org/wiki/Logistic_function)
12. <a id="cite-ref-12" href="#cite-note-12">↑</a> see also winning probability W in [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
13. <a id="cite-ref-13" href="#cite-note-13">↑</a> [log-linear 1 / (1 + 10^(-s/4)) , s=-10 to 10](http://wolfr.am/1al3d5B) plot by [Wolfram Alpha](https://en.wikipedia.org/wiki/Wolfram_Alpha)
14. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Re: Experiments with eval tuning](http://www.talkchess.com/forum/viewtopic.php?t=55621&start=4) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), March 10, 2015
15. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Why computing K that minimizes the sigmoid func. value?...](http://www.talkchess.com/forum/viewtopic.php?t=58298) by [Michael Hoffmann](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), November 19, 2015
16. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Dell PowerEdge T620 review | ZDNet](http://www.zdnet.com/dell-poweredge-t620-review-7000003879/)
17. <a id="cite-ref-17" href="#cite-note-17">↑</a> [What is Self-Calibration?](http://www.selfcalibration.com/)
18. <a id="cite-ref-18" href="#cite-note-18">↑</a> [Amir Ban](Amir_Ban "Amir Ban") (**2012**). *[Automatic Learning of Evaluation, with Applications to Computer Chess](http://www.ratio.huji.ac.il/node/2362)*. Discussion Paper 613, [The Hebrew University of Jerusalem](https://en.wikipedia.org/wiki/Hebrew_University_of_Jerusalem) - Center for the Study of Rationality, [Givat Ram](https://en.wikipedia.org/wiki/Givat_Ram)
19. <a id="cite-ref-19" href="#cite-note-19">↑</a> [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=40) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), February 05, 2014
20. <a id="cite-ref-20" href="#cite-note-20">↑</a> [brtzsnr / txt — Bitbucket](https://bitbucket.org/brtzsnr/txt) by [Alexandru Mosoi](Alexandru_Mosoi "Alexandru Mosoi")
21. <a id="cite-ref-21" href="#cite-note-21">↑</a> [Central limit theorem from Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)
22. <a id="cite-ref-22" href="#cite-note-22">↑</a> [Re: The texel evaluation function optimization algorithm](http://www.talkchess.com/forum/viewtopic.php?t=50823&start=94) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 12, 2014

**[Up one Level](Automated_Tuning "Automated Tuning")**







 
