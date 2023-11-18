---
title: RamJet
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* RamJet**



[ Bussard Ramjet <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**RamJet**,  

an [UCI](UCI "UCI") compliant chess engine by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), first released in January 2014. So far, RamJet played the [IGT 2014](IGT_2014 "IGT 2014"), the [IGT 2015](IGT_2015 "IGT 2015"), the [IGT 2016](IGT_2016 "IGT 2016") and the [IGT 2017](IGT_2017 "IGT 2017") over the board. 
IGT 2017 participant RamJet **0.14** was released afterwards as [open source engine](Category:Open_Source "Category:Open Source") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### RamJet 0.11


RamJet **0.11** rolled back to a pure [piece-square tables](Piece-Square_Tables "Piece-Square Tables") [evaluation](Evaluation "Evaluation"), had an improved [search](Search "Search"), configurable options, and supports [Chess960](Chess960 "Chess960") <a id="cite-note-4" href="#cite-ref-4">[4]</a>. 



### RamJet 0.14


The open source RamJet **0.14** distributes its [piece or empty square codes](Pieces#PieceCoding "Pieces") as vertical [nibbles](Nibble "Nibble") of a [quad-bitboard](Quad-Bitboards "Quad-Bitboards") board representation, and applies [Kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks").
The [evaluation function](Evaluation_Function "Evaluation Function") is implemented as a [neural network](Neural_Networks "Neural Networks") with one hidden layer of three neurons. Beside aggregation of [piece-square](Piece-Square_Tables "Piece-Square Tables") scores and a [games phase value](Game_Phases "Game Phases"), the latter passed to a [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) [tapering](Tapered_Eval "Tapered Eval") king scores, two further sigmoid units consider [tactical](Tactics "Tactics") features of attacks and [checks](Check "Check").



## See also


* [Pawn Ram](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")
* [ProChess](ProChess_IT "ProChess IT")
* [RAM](Memory#RAM "Memory") (Random Access Memory)


## Forum Posts


* [New engine RamJet 0.12](http://www.talkchess.com/forum/viewtopic.php?t=57996) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), October 19, 2015
* [New release: RamJet 0.14](http://www.talkchess.com/forum/viewtopic.php?t=65312) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), September 27, 2017


## External Links


### Chess Engine


* [RamJet](http://www.g-sei.org/ramjet/) « [G 6](G_6 "G 6")
* [RamJet](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=RamJet&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [Ramjet from Wikipedia](https://en.wikipedia.org/wiki/Ramjet)
* [Ramjet (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ramjet_%28disambiguation%29)
* [Ramjet (Image Comics) from Wikipedia](https://en.wikipedia.org/wiki/Ramjet_%28Image_Comics%29)
* [Ramjet (Transformers) from Wikipedia](https://en.wikipedia.org/wiki/Ramjet_(Transformers))
* [Ram (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Ram)
* [Jet engine from Wikipedia](https://en.wikipedia.org/wiki/Jet_engine)


## References


 1. <a id="cite-ref-1" href="#cite-note-1">↑</a> The [Bussard Ramjet](https://en.wikipedia.org/wiki/Bussard_ramjet) engine concept uses [interstellar](https://en.wikipedia.org/wiki/Interstellar) [hydrogen](https://en.wikipedia.org/wiki/Hydrogen) scooped up from its environment as the spacecraft passes by to provide [propellant](https://en.wikipedia.org/wiki/Propellant) mass. The hydrogen is then ionized and collected by an electromagentic field. In this image, an onboard [laser](https://en.wikipedia.org/wiki/Laser) is used to heat the plasma, and the laser or electron beam is used to trigger fusion pulses thereby creating propulsion. [NASA](https://en.wikipedia.org/wiki/NASA) image, April 2004, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons) 
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [New release: RamJet 0.14](http://www.talkchess.com/forum/viewtopic.php?t=65312) by [Edoardo Manino](Edoardo_Manino "Edoardo Manino"), [CCC](CCC "CCC"), September 27, 2017
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [RamJet](http://www.g-sei.org/ramjet/) « [G 6](G_6 "G 6")
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [RamJet\_011.zip\RamJet\_011\readme.txt](http://www.g-sei.org/wp-content/uploads/2014/07/RamJet_011.zip)

**[Up one level](Engines "Engines")**







 
