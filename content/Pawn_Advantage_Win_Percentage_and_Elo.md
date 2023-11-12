---
title: Pawn Advantage Win Percentage and Elo
---
**[Home](Home "Home") \* [Evaluation](Evaluation "Evaluation") \* Pawn Advantage, Win Percentage and Elo**


An examination by [Sune Fischer](Sune_Fischer "Sune Fischer") and [Pradu Kannan](Pradu_Kannan "Pradu Kannan") in December 2007 on the approximate relations between **Win Percentage**, **Pawn Advantage**, and [Elo rating](https://en.wikipedia.org/wiki/Elo_rating_system) advantage for computer chess resulted in following findings. 



## Data Acquisition


Data was taken from a collection of 405,460 computer games in [PGN format](Portable_Game_Notation "Portable Game Notation"). Whenever exactly 5 plys in a game had gone by without captures, the game result was accumulated twice in a table indexed by the material configuration. The data was accumulated twice because it was assumed that material values were equal for both colors. So if there was data for a KPK material configuration, the data was also tallied for the KKP. Only data pertaining to the material configuration was taken. This was considered reasonable because the material configuration is the most important quantity that affects the result of a game.



## Data Reduction and Modeling


For each material configuration, a pawn value was computed using conventional pawn-normalized material ratios that are close to those used in strong chess programs (P=1, N=4, B=4.1, R=6, Q=12). The relationship between Win Percentage and Pawn Advantage was assumed to follow a [logistic model](https://en.wikipedia.org/wiki/Logistic_regression) <a id="cite-note-1" href="#cite-ref-1">[1]</a> with its [sigmoid curve](https://en.wikipedia.org/wiki/Sigmoid_function), namely,



 [](File:PawnWinELOFormula4.jpg) 
where K is an unknown non-zero constant. When applying the condition that the win probability is 0.5 if there is no pawn advantage, the solution to the above seperable differential equation becomes



 [](File:PawnWinELOFormula5.jpg) 
For K=4, the proposed logistic model and the data is plotted here for comparison:



 [](File:Wp2pa.PNG) 
## See also


* [Bishop versus Knight - Winning Percentages](Bishop_versus_Knight#WinningPercantages "Bishop versus Knight")
* [Match Statistics](Match_Statistics "Match Statistics")
* [Material](Material "Material")
* [Playing Strength](Playing_Strength "Playing Strength")


## Publications


* [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Kazunori Yamaguchi](Kazunori_Yamaguchi "Kazunori Yamaguchi"), [Satoru Kawai](Satoru_Kawai "Satoru Kawai") (**2007**). *Visualization and Adjustment of Evaluation Functions Based on Evaluation Values and Win Probability*. [AAAI 2007](http://www.informatik.uni-trier.de/~ley/db/conf/aaai/aaai2007.html), [pdf](https://www.aaai.org/Papers/AAAI/2007/AAAI07-136.pdf)
* [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Jason Zhou](index.php?title=Jason_Zhou&action=edit&redlink=1 "Jason Zhou (page does not exist)") (**2014**). *Human and Computer Preferences at Chess*. [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/RBZ14aaai.pdf)
* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Measuring Level-K Reasoning, Satisficing, and Human Error in Game-Play Data*. [IEEE](IEEE "IEEE") [ICMLA 2015](http://www.icmla-conference.org/icmla15/), [pdf preprint](http://www.cse.buffalo.edu/~regan/papers/pdf/BiRe15_ICMLA2015.pdf)
* [Shogo Takeuchi](Shogo_Takeuchi "Shogo Takeuchi"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko") (**2015**). *[Estimating Ratings of Computer Players by the Evaluation Scores and Principal Variations in Shogi](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7336038)*. [ACIT-CSI](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=7335993)


## Postings


### 1999


* [Elo performance?](https://www.stmintz.com/ccc/index.php?id=52542) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), May 22, 1999 » [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength")


### 2000 ...


* [likelihood instead of pawnunits? + chess knowledge](https://www.stmintz.com/ccc/index.php?id=261636) by [Ingo Lindam](index.php?title=Ingo_Lindam&action=edit&redlink=1 "Ingo Lindam (page does not exist)"), [CCC](CCC "CCC"), October 25, 2002
* [Winning percentage and centipawns](http://www.talkchess.com/forum/viewtopic.php?t=30695) by [Luca Hemmerich](Luca_Hemmerich "Luca Hemmerich"), [CCC](CCC "CCC"), November 18, 2009


### 2010 ...


* [Pawn Advantage, Win Percentage, and Elo](http://www.talkchess.com/forum/viewtopic.php?t=43323) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), April 15, 2012
* [normal vs logistic curve for Elo model](http://www.talkchess.com/forum/viewtopic.php?t=44670) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), August 02, 2012
* [Houdini, much weaker engines, and Arpad Elo](http://www.talkchess.com/forum/viewtopic.php?t=50266) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 29, 2013 » [Houdini](Houdini "Houdini"), [Match Statistics](Match_Statistics "Match Statistics") <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [Pawn Advantage in iCE](http://macechess.blogspot.de/2014/03/pawn-advantage-in-ice.html) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke"), [mACE Chess](http://macechess.blogspot.de/), March 16, 2014 » [iCE](ICE "ICE")
* [Using the Stockfish position evaluation score to predict victory probability](https://chesscomputer.tumblr.com/post/98632536555/using-the-stockfish-position-evaluation-score-to/embed) by unavoidablegrain, [Tumblr](https://en.wikipedia.org/wiki/Tumblr), September 28, 2014 » [Stockfish](Stockfish "Stockfish")


### 2015 ...


* [Depth of Satisficing](https://rjlipton.wordpress.com/2015/10/06/depth-of-satisficing/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), October 06, 2015  » [Depth](Depth "Depth"), [Match Statistics](Match_Statistics "Match Statistics"), Pawn Advantage, Win Percentage, and Elo, [Stockfish](Stockfish "Stockfish"), [Komodo](Komodo "Komodo") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [Magnus and the Turkey Grinder](https://rjlipton.wordpress.com/2016/12/08/magnus-and-the-turkey-grinder/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), December 08, 2016 » [Match Statistics](Match_Statistics "Match Statistics") <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>
* [Statistical interpretation of search and eval scores](http://www.talkchess.com/forum/viewtopic.php?t=65764) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), November 18, 2017 » [Match Statistics](Match_Statistics "Match Statistics"), [Score](Score "Score")
* [Why Lc0 eval (in cp) is asymmetric against AB engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=68072) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), July 25, 2018 » [Asymmetric Evaluation](Asymmetric_Evaluation "Asymmetric Evaluation"), [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [UCI Win/Draw/Loss reporting](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72140) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), October 22, 2019


### 2020 ...


* [Win-Draw-Loss evaluation](https://lczero.org/blog/2020/04/wdl-head/) by [crem](Alexander_Lyashuk "Alexander Lyashuk"), [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), April 20, 2020 » [TCEC Season 17 Superfinal](TCEC_Season_17#Superfinal "TCEC Season 17")
* [Stockfish has included WDL stats in engine output](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74339) by Deberger, [CCC](CCC "CCC"), July 02, 2020 » [Stockfish](Stockfish "Stockfish")


## External Links


* [Elo rating system from Wikipedia](https://en.wikipedia.org/wiki/Elo_rating_system)
* [Elo Win Probability Calculator](http://wismuth.com/elo/calculator.html) by [François Labelle](Mathematician#FLabelle "Mathematician")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [logistic model from Wolfram MathWorld](http://mathworld.wolfram.com/LogisticEquation.html)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Arpad Elo - Wikipedia](https://en.wikipedia.org/wiki/Arpad_Elo)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Regan's latest: Depth of Satisficing](http://www.talkchess.com/forum/viewtopic.php?t=57890) by [Carl Lumma](index.php?title=Carl_Lumma&action=edit&redlink=1 "Carl Lumma (page does not exist)"), [CCC](CCC "CCC"), October 09, 2015
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [When Data Serves Turkey](https://rjlipton.wordpress.com/2016/11/30/when-data-serves-turkey/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), November 30, 2016
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [World Chess Championship 2016 from Wikipedia](https://en.wikipedia.org/wiki/World_Chess_Championship_2016)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Regan's conundrum](http://www.talkchess.com/forum/viewtopic.php?t=62435) by [Carl Lumma](index.php?title=Carl_Lumma&action=edit&redlink=1 "Carl Lumma (page does not exist)"), [CCC](CCC "CCC"), December 09, 2016

**[Up one Level](Evaluation "Evaluation")**







 
