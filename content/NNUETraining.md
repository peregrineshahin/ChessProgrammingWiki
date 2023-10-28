---
title: NNUETraining
---
**[Home](Home "Home") \* [Learning](Learning "Learning") \* [Neural Networks](Neural_Networks "Neural Networks") \* NNUE**



[ [Toriyama Sekien](Category:Toriyama_Sekien "Category:Toriyama Sekien") - Nue (鵺) [[1]](#cite_note-1) [[2]](#cite_note-2)
**NNUE**, (ƎUИИ Efficiently Updatable Neural Networks)  
 
a Neural Network architecture intended to replace the [evaluation](Evaluation "Evaluation") of [Shogi](Shogi "Shogi"), [chess](Chess "Chess") and other board game playing [alpha-beta](Alpha-Beta "Alpha-Beta") searchers running on a CPU. Inspired by [Kunihito Hoki's](Kunihito_Hoki "Kunihito Hoki") approach of [piece-square tables](Piece-Square_Tables "Piece-Square Tables") indexed by king location, and further two-piece locations and side to move as applied in his Shogi engine [Bonanza](Bonanza "Bonanza") [[3]](#cite_note-3), **NNUE** was introduced in 2018 by [Yu Nasu](Yu_Nasu "Yu Nasu") [[4]](#cite_note-4), and was used in Shogi adaptations of [Stockfish](Stockfish "Stockfish") such as [YaneuraOu](YaneuraOu "YaneuraOu") [[5]](#cite_note-5),
and [Kristallweizen](Kristallweizen "Kristallweizen") [[6]](#cite_note-6), apparently with [AlphaZero](AlphaZero "AlphaZero") strength [[7]](#cite_note-7). 



### Contents


* [1 Stockfish NNUE](#Stockfish_NNUE)
* [2 NNUE Engines](#NNUE_Engines)
* [3 NN Structure](#NN_Structure)
* [4 See also](#See_also)
* [5 Publications](#Publications)
* [6 Forum Posts](#Forum_Posts)
	+ [6.1 2020](#2020)
		- [6.1.1 January ...](#January_...)
		- [6.1.2 July](#July)
		- [6.1.3 August](#August)
		- [6.1.4 September](#September)
		- [6.1.5 October](#October)
		- [6.1.6 November](#November)
		- [6.1.7 December](#December)
	+ [6.2 2021](#2021)
		- [6.2.1 January](#January)
		- [6.2.2 February](#February)
		- [6.2.3 March](#March)
		- [6.2.4 April](#April)
		- [6.2.5 May](#May)
		- [6.2.6 June](#June)
		- [6.2.7 July](#July_2)
		- [6.2.8 August ...](#August_...)
	+ [6.3 2022 ...](#2022_...)
* [7 External Links](#External_Links)
	+ [7.1 NNUE](#NNUE)
	+ [7.2 NNUE libraries](#NNUE_libraries)
	+ [7.3 Source Code](#Source_Code)
	+ [7.4 Misc](#Misc)
* [8 References](#References)






As reported by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)") [[8]](#cite_note-8), 
[Nodchip](Hisayori_Noda "Hisayori Noda") incorporated NNUE into the chess playing [Stockfish](Stockfish "Stockfish") 10 as a proof of concept.
[Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") was born, and in summer 2020 the computer chess community bursts out enthusiastically due to its rapidly raising [playing strength](Playing_Strength "Playing Strength") with different networks trained using a mixture of [supervised](Supervised_Learning "Supervised Learning") and [reinforcement learning](Reinforcement_Learning "Reinforcement Learning") methods -
despite the approximately halved search speed, becoming stronger than its original [[9]](#cite_note-9), finally responsible for the huge [strength](Playing_Strength "Playing Strength") improvement of **Stockfish 12**.



## NNUE Engines


*see [Category:NNUE](Category:NNUE "Category:NNUE")*


Being tempted by the success of [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") and attracted by how easy the method and small the code is, many engine developers have started testing and applying NNUE. For quick trials and evaluating before going into serious development, some of them borrowed and/or rewrote NNUE code and use networks from Stockfish NNUE. Most of them reported positive results, such as [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)") with [Orion](Orion "Orion") [[10]](#cite_note-10), [Ehsan Rashid](index.php?title=Ehsan_Rashid&action=edit&redlink=1 "Ehsan Rashid (page does not exist)") with [DON](DON "DON") [[11]](#cite_note-11), various [Stockfish derivatives](Stockfish#Derivatives "Stockfish") by [Michael Byrne](Michael_Byrne "Michael Byrne") [[12]](#cite_note-12), and [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna") with [Igel](Igel "Igel") [[13]](#cite_note-13) using the *Night Nurse* NNUE net by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe") [[14]](#cite_note-14). [Daniel Shawul](Daniel_Shawul "Daniel Shawul") added NNUE support à la [CFish](CFish "CFish") into his [egbbdll](Scorpio#Bitbases "Scorpio") probing library of [Scorpio](Scorpio "Scorpio") [[15]](#cite_note-15) [[16]](#cite_note-16), making it even easier to use NNUE. The promising engines [Halogen](Halogen "Halogen") 7 and 8 by [Kieren Pearson](Kieren_Pearson "Kieren Pearson"), and [Seer](Seer "Seer") by [Connor McMonigle](Connor_McMonigle "Connor McMonigle") came with their own, distinct NNUE implementations, and on November 10, 2020, the commercial [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess") aka [Komodo](Komodo "Komodo") NNUE appeared [[17]](#cite_note-17), trying to close the gap to Stockfish NNUE. The commercial [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz"), based on a slightly modified Stockfish 12 using a customized, double sized network, was released by [ChessBase](ChessBase "ChessBase") in February 2021.



## NN Structure


The neural network of Stockfish NNUE consists of four layers, W1 through W4. The input layer W1 is heavily overparametrized, feeding in the [board representation](Board_Representation "Board Representation") for various king configurations.
The efficiency of the net is due to [incremental update](Incremental_Updates "Incremental Updates") of W1 in [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move"),
where only a fraction of its neurons need to be recalculated. The remaining three layers with 32x2x256, 32x32 and 32x1 weights are computational less expensive, best calculated using appropriate [SIMD instructions](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") like [AVX2](AVX2 "AVX2") on [x86-64](X86-64 "X86-64"), or if available, [AVX-512](AVX-512 "AVX-512").



 [](File:NNUE.jpg) 
NNUE structure with [incremental update](Incremental_Updates "Incremental Updates") [[18]](#cite_note-18)



## See also


* [Cerebrum](index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
* [SANE](David_E._Moriarty#SANE "David E. Moriarty")
* [Stockfish HalfKAv2](Stockfish_NNUE#HalfKA "Stockfish NNUE")


## Publications


* [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf), [pdf](https://www.apply.computer-shogi.org/wcsc28/appeal/the_end_of_genesis_T.N.K.evolution_turbo_type_D/nnue.pdf) (Japanese with English abstract) [GitHub - asdfjkl/nnue translation](https://github.com/asdfjkl/nnue) [[19]](#cite_note-19)
* [Dominik Klein](Dominik_Klein "Dominik Klein") (**2021**). *[Neural Networks For Chess](https://github.com/asdfjkl/neural_network_chess)*. [Release Version 1.1 · GitHub](https://github.com/asdfjkl/neural_network_chess/releases/tag/v1.1) [[20]](#cite_note-20)


## Forum Posts


### 2020


### January ...


* [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020 » [Stockfish](Stockfish "Stockfish"), [Shogi](Shogi "Shogi")


 [Re: The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754&start=18) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), January 18, 2020
* [Stockfish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74058) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020 » [Stockfish](Stockfish "Stockfish")
* [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
* [NNUE shared library and tools](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74148) by [Adam Treat](Adam_Treat "Adam Treat"), [CCC](CCC "CCC"), June 10, 2020


### July


* [Lizard-NNUE Experiment NOT bad with NNUE Net Evaluation...](http://talkchess.com/forum3/viewtopic.php?t=74480) by Nancy M Pichardo, [CCC](CCC "CCC"), July 15, 2020
* [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 16, 2020
* [NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), July 21, 2020


 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=1) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 23, 2020
 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=5) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), July 24, 2020
 [Re: NNUE accessible explanation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74531&start=8) by [Jonathan Rosenthal](Jonathan_Rosenthal "Jonathan Rosenthal"), [CCC](CCC "CCC"), August 03, 2020
* [BrainLearn NNUE 1.0](https://groups.google.com/d/msg/fishcooking/Wpk-9COzk64/ez643VTkAAAJ) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020 » [BrainLearn](index.php?title=BrainLearn&action=edit&redlink=1 "BrainLearn (page does not exist)")
* [ShashChess NNUE 1.0](https://groups.google.com/d/msg/fishcooking/yWtpz_FY5_Y/RMTG56fkAAAJ) by [Andrea Manzo](Andrea_Manzo "Andrea Manzo"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 25, 2020 » [ShashChess](ShashChess "ShashChess")
* [LC0 vs. NNUE - some tech details...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74607) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 29, 2020 » [Lc0](Leela_Chess_Zero#Lc0 "Leela Chess Zero")
* [What does NNUE actually mean](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74611) by Paloma, [CCC](CCC "CCC"), July 29, 2020


### August


* [What happens with my hyperthreading?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74705) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), August 06, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Re: Minic version 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73521&start=59) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), August 08, 2020 » [Minic](Minic "Minic")
* [Neural Networks weights type](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74777) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 13, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Re: Introducing Igel chess engine - Igel and NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=17) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), August 19, 2020 » [Igel](Igel "Igel")
* [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](CCC "CCC"), August 19, 2020 » [Orion](Orion "Orion")
* [Night Nurse 0.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), August 19, 2020 » [A0lite](A0lite "A0lite"), [Igel](Igel "Igel")
* [NNUE](http://laatste.info/bb3/viewtopic.php?f=53&t=8298) by [Bert Tuyt](index.php?title=Bert_Tuyt&action=edit&redlink=1 "Bert Tuyt (page does not exist)"), [World Draughts Forum](http://laatste.info/bb3/viewforum.php?f=53), August 19, 2020 » [Draughts](Draughts "Draughts")


### September


* [Train a neural network evaluation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74955) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 01, 2020 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [RubiChess NNUE player implemented](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75016) by [Andreas Matthies](Andreas_Matthies "Andreas Matthies"), [CCC](CCC "CCC"), September 06, 2020 » [RubiChess](RubiChess "RubiChess")
* [Toga III 0.4 NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75027) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), September 07, 2020 » [Toga](Toga "Toga")
* [Neural network quantization](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75042) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), September 08, 2020 » [Neural Networks](Neural_Networks "Neural Networks")
* [AVX-512 and NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75049) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), September 08, 2020 » [AVX-512](AVX-512 "AVX-512")
* [First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), September 23, 2020 » [Neural Networks](Neural_Networks "Neural Networks")


 [Re: First success with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75190&start=21) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), November 11, 2020 » [Checkers](Checkers "Checkers")
* [Nemorino 6 (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75241) by [Florentino](index.php?title=Christian_G%C3%BCnther&action=edit&redlink=1 "Christian Günther (page does not exist)"), [CCC](CCC "CCC"), September 28, 2020 » [Nemorino](Nemorino "Nemorino")
* [A Crossroad in Computer Chess; Or Desperate Flailing for Relevance](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75247) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 29, 2020
* [NNUE variation](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75248) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), September 29, 2020


### October


* [BONA\_PIECE\_ZERO](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75296) by [elcabesa](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), October 04, 2020
* [Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=91) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020 » [Ethereal](Ethereal "Ethereal")
* [Request for someone to train an NNUE for Ethereal](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75345) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 09, 2020
* [Ethereal Tuning - Data Dump](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75350) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 10, 2020
* [Dangerous turn](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75358) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), October 10, 2020
* [Black crushing white, weird ?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75393) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), October 14, 2020 » [MinicNNUE](Minic#MinicNNUE "Minic")
* [Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 15, 2020 » [CFish](CFish "CFish")


 [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 15, 2020 » [Scorpio](Scorpio "Scorpio")
* [How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020


 [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 17, 2020
* [Embedding Stockfish NNUE to ANY CHESS ENGINE: YouTube series](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75418) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 17, 2020 » [BBC](BBC "BBC")
* [Seer](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75433) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), October 18, 2020 » [Seer](Seer "Seer")
* [BBC 1.3 + Stockfish NNUE released!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75482) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), October 21, 2020 » [BBC](BBC "BBC")
* [Mayhem NNUE - New NN engine](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75500) by [JohnWoe](Toni_Helminen "Toni Helminen"), [CCC](CCC "CCC"), October 22, 2020 » [Mayhem](Mayhem "Mayhem")
* [Centipawns vs Millipawns with NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75501) by Madeleine Birchfield, [CCC](CCC "CCC"), October 23, 2020 » [Centipawns](Centipawns "Centipawns"), [Millipawns](Millipawns "Millipawns")
* [NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), October 23, 2020 » [Stockfish NNUE - NNUE Structure](Stockfish_NNUE#NNUE_Structure "Stockfish NNUE")


 [July 01, 2021 continuation](#KingPlacementsCont)
### November


* [Komodo 14.1 Release and Dragon Announcement](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75651) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 02, 2020 » [Komodo](Komodo "Komodo")
* [NNUE outer product vs tensor product](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75653) by Madeleine Birchfield, [CCC](CCC "CCC"), November 02, 2020 [[21]](#cite_note-21) [[22]](#cite_note-22)
* [Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), November 08, 2020 [[23]](#cite_note-23)
* [TucaNNo: neural network research](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75725) by [Alcides Schulz](Alcides_Schulz "Alcides Schulz"), [CCC](CCC "CCC"), November 08, 2020
* [Dragon by Komodo Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75748) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 10, 2020 » [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess")
* [Tensorflow NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75751) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), November 10, 2020 [[24]](#cite_note-24)
* [Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890) by Madeleine Birchfield, [CCC](CCC "CCC"), November 11, 2020


 [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=6) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020
 [Re: Speculations about NNUE development (was New engine releases 2020)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75890&start=9) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), November 12, 2020 » [Dragon by Komodo Chess](Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Seer](Seer "Seer"), [Halogen](Halogen "Halogen")
* [Re: Final Release of Ethereal, V12.75](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75335&start=134) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 12, 2020
* [Maybe not the best diversity of strongest chess engines under development](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75797) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), November 14, 2020 » [Engine Similarity](Engine_Similarity "Engine Similarity")
* [CPU Vector Unit, the new jam for NNs...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75862) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), November 18, 2020 » [SIMD](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques")
* [You've trained a brilliant NN(UE) King-Piece Network. Now what?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75870) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), November 19, 2020
* [Pawn King Neural Network](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75925) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), November 26, 2020


### December


* [Orion 0.8 + The Cerebrum release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75953) by [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](CCC "CCC"), December 01, 2020 » [Orion](Orion "Orion"), [Cerebrum](index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
* [The NNUE split programmers are in](https://prodeo.actieforum.com/t104-the-nnue-split-programmers-are-in) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [ProDeo Forum](Computer_Chess_Forums "Computer Chess Forums"), December 02, 2020
* [Introducing the "Cerebrum" library (NNUE-like trainer and inference code)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76006) by [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](CCC "CCC"), December 07, 2020
* [Dispelling the Myth of NNUE with LazySMP: An Analysis](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76190) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), December 30, 2020 » [Lazy SMP](Lazy_SMP "Lazy SMP")


### 2021


### January


* [Translation of Yu Nasu's NNUE paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76250) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), January 07, 2021
* [Re: Pytorch NNUE training](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75724&start=60) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), January 09, 2021
* [More experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76263) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), January 09, 2021 » [Slow Chess](Slow_Chess "Slow Chess")
* [Shouldn't positional attributes drive SF's NNUE input features (rather than king position)?](https://groups.google.com/g/fishcooking/c/cad1MGSdpU4/m/Ury4iBqSBgAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2021 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [HalfKP Structure in NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76285) by Roger Stephenson, [CCC](CCC "CCC"), January 12, 2021
* [Andscacs nnue 0.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76346) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), January 17, 2021 » [Andscacs](Andscacs "Andscacs")
* [It's NNUE era (sharing my thoughts)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76353) by Basti Dangca, [CCC](CCC "CCC"), January 18, 2021
* [NNUE and game phase](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76356) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), January 18, 2021 » [Game Phases](Game_Phases "Game Phases")
* [correspondence chess in the age of NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76382) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 21, 2021
* [One for Andrew Grant et al. - NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76386) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), January 21, 2021
* [256 in NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76437) by Ted Wong, [CCC](CCC "CCC"), January 28, 2021
* [So what do we miss in the traditional evaluation?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76446) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), January 29, 2021 » [Evaluation](Evaluation "Evaluation")
* [Latest Night Nurse released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76447) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), January 29, 2021
* [None-GPL NNUE probing code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76456) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 31, 2021


### February


* [Fat Fritz 2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76537) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), February 09, 2021 » [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
* [How much work is it to train an NNUE?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76552) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), February 11, 2021
* [HCE and NNUE and vectorisation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76556) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), February 11, 2021 » [Minic](Minic "Minic")
* [nnue reading code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76570) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), February 13, 2021
* [New net: The White Rose](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76648) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), February 20, 2021
* [Are neural nets (the weights file) copyrightable?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76664) by [Adam Treat](Adam_Treat "Adam Treat"), [CCC](CCC "CCC"), February 21, 2021
* [My first NNUE nn-f0c1c3cbf2f1.nnue](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76731) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), February 27, 2021
* [How to make a double-sized net as good as SF NNUE in a few easy steps](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76742) by [Chris Whittington](Chris_Whittington "Chris Whittington"), [CCC](CCC "CCC"), February 28, 2021 » [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")


### March


* [A random walk down NNUE street …](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76790) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), March 06, 2021
* [NNUE Research Project](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76833) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), March 10, 2021 » [Engine Similarity](Engine_Similarity "Engine Similarity")
* [Simex including NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76840) by jjoshua2, [CCC](CCC "CCC"), March 11, 2021 » [Engine Similarity](Engine_Similarity "Engine Similarity")
* [NNUE ranking](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76844) by Jim Logan, [CCC](CCC "CCC"), March 12, 2021 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [FEN compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76892) by lucasart, [CCC](CCC "CCC"), March 17, 2021 » [FEN Compression](BMI2#FEN_Compression "BMI2"), [NNUE Training](#Training)
* [Mabigat - hyperparameter optimizer for NNUE net](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76917) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), March 22, 2021 » [Automated Tuning](Automated_Tuning "Automated Tuning")
* [nnue-trainer](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76964) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 27, 2021
* [Zeta with NNUE on GPU?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76986) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), March 31, 2021 » [Zeta](Zeta "Zeta"), [GPU](GPU "GPU")


### April


* [Rubichess NN questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77157) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), April 23, 2021 » [RubiChess](RubiChess "RubiChess")
* [Crafty NNUE Chess Engine?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77200) by supersharp77, [CCC](CCC "CCC"), April 29, 2021 » [Crafty](Crafty "Crafty"), [Vafra](index.php?title=Vafra&action=edit&redlink=1 "Vafra (page does not exist)") [[25]](#cite_note-25)


### May


* [Komodo Dragon 2 released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77244) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), May 04, 2021 » [Komodo Dragon](Dragon_by_Komodo_Chess "Dragon by Komodo Chess")
* [Stockfish with new NNUE architecture and bigger net released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77344) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 » [Stockfish](Stockfish "Stockfish"), [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") [[26]](#cite_note-26)
* [NNUE scoring (egbb lib)](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77348) by [Desperado](Michael_Hoffmann "Michael Hoffmann"), [CCC](CCC "CCC"), May 19, 2021 » [Scorpio NNUE](Scorpio#ScorpioNNUE "Scorpio")


### June


* [Re: Booot progress](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77243&start=20) by [Alex Morozov](Alex_Morozov "Alex Morozov"), [CCC](CCC "CCC"), June 01, 2021 » [Booot](Booot "Booot")
* [Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021 » [Ethereal 13.00 (NNUE)](Ethereal#Ethereal_13_.28NNUE.29 "Ethereal")


 [Re: Commercial Release of Ethereal 13.00 (NNUE) for AVX2 Systems](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77438&start=17) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 04, 2021 » [HalfKP](Stockfish_NNUE#NNUE_Structure "Stockfish NNUE")
* [Dark Horse Update](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77467) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), June 11, 2021
* [Some more experiments with neural nets](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77492) by [Jonathan Kreuzer](Jonathan_Kreuzer "Jonathan Kreuzer"), [CCC](CCC "CCC"), June 15, 2021 » [Slow Chess](Slow_Chess "Slow Chess")
* [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021 » [Stockfish](Stockfish "Stockfish"), [Komodo Dragon](Dragon_by_Komodo_Chess "Dragon by Komodo Chess"), [Ethereal](Ethereal "Ethereal"), [Seer](Seer "Seer")


 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=63) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), June 18, 2021 » [Scorpio](Scorpio "Scorpio")
 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=68) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), June 18, 2021 » [Minic](Minic "Minic")
* [I declare that HCE is dead...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77571) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 29, 2021 » [Ethereal](Ethereal "Ethereal"), [HCE](Evaluation "Evaluation")


### July


* [Re: NNUE Question - King Placements](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=39) by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk"), [CCC](CCC "CCC"), July 01, 2021 » [NNUE Question](#KingPlacements)


 [Re: NNUE Question - King Placements](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=75506&start=40) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), July 01, 2021 » [ScorpioNNUE](Scorpio#ScorpioNNUE "Scorpio")
* [Before things become more messy than they already are](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77602) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 02, 2021
* [NNUE training set generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77606) by [Edsel Apostol](Edsel_Apostol "Edsel Apostol"), [CCC](CCC "CCC"), July 03, 2021
* [Time to rethink what Albert Silver has done?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77612) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), July 03, 2021 » [Fat Fritz 2](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
* [Would the ICGA have accepted today's NNUE engines?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77639) by Madeleine Birchfield, [CCC](CCC "CCC"), July 05, 2021 » [ICGA](ICGA "ICGA")
* [Koivisto 5.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77664) by [Finn Eggers](Finn_Eggers "Finn Eggers"), [CCC](CCC "CCC"), July 07, 2021 » [Koivisto](Koivisto "Koivisto")
* [NNUE one year retrospective](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77681) by Madeleine Birchfield, [CCC](CCC "CCC"), July 09, 2021


### August ...


* [Basic NNUE questions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77869) by [Amanj Sherwany](Amanj_Sherwany "Amanj Sherwany"), [CCC](CCC "CCC"), August 04, 2021
* [Alternatives to King-Pawn, King-All NNUE encoding](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=78109) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), September 05, 2021
* [NNUE - Efficiently Updatable Network - understanding](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78394) by [Daniel Infuehr](index.php?title=Daniel_Infuehr&action=edit&redlink=1 "Daniel Infuehr (page does not exist)"), [CCC](CCC "CCC"), October 11, 2021
* [NNUE - only from own engine?](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78497) by [Rebel](Ed_Schroder "Ed Schroder"), October 25, 2021
* [Regarding AVX2](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78588) by [Rebel](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 03, 2021 » [AVX2](AVX2 "AVX2")
* [Mantissa 3.0.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78855) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCC](CCC "CCC"), December 10, 2021 » [Mantissa](Mantissa "Mantissa")
* [Are NNUE Nets Specific to Chess Engines or They Universal to All Engines?](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78979) by daniel71, [CCC](CCC "CCC"), December 26, 2021


### 2022 ...


* [Why NNUE trainer requires an online qsearch on each training position?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79020) by [Chao Ma](Chao_Ma "Chao Ma"), [CCC](CCC "CCC"), January 01, 2022
* [Rebel 14](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79107) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), January 12, 2022 » [Rebel 14](Rebel#14 "Rebel")
* [Koivisto 8.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79523) by [Finn Eggers](Finn_Eggers "Finn Eggers"), [CCC](CCC "CCC"), March 15, 2022 » [Koivisto](Koivisto "Koivisto")
* [NNUE + Pawn-King Network](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79742) by Alvin Peng, [CCC](CCC "CCC"), April 22, 2022


## External Links


### NNUE


* [Efficiently updatable neural network | Wikipedia](https://en.wikipedia.org/wiki/Efficiently_updatable_neural_network)
* [次世代の将棋思考エンジン、NNUE関数を学ぼう（その１．ネットワーク構造編） - コンピュータ将棋 Qhapaq](http://qhapaq.hatenablog.com/entry/2018/06/02/221612), June 02, 2018 (Japanese)


 Learn Next Generation Shogi Thinking Engine, NNUE Function (Part 1. Network Structure) - Computer Shogi
* [次世代の将棋思考エンジン、NNUE関数を学ぼう（その2．改造/学習編） - コンピュータ将棋 Qhapaq](http://qhapaq.hatenablog.com/entry/2018/07/08/193316), July 08, 2018 (Japanese)


 Let's Learn Next Generation Shogi Thinking Engine, NNUE Function (Part 2. Remodeling/Learning) - Computer Shogi
* [Stockfish NNUE – The Complete Guide](http://yaneuraou.yaneu.com/2020/06/19/stockfish-nnue-the-complete-guide/), June 19, 2020 (Japanese and English)
* [3 technologies in shogi AI that could be used for chess AI](http://yaneuraou.yaneu.com/2020/08/21/3-technologies-in-shogi-ai-that-could-be-used-for-chess-ai/) by [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki"), August 21, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Stockfish NNUE Wiki](https://www.qhapaq.org/shogi/shogiwiki/stockfish-nnue/)
* [nnue | Home of the Dutch Rebel](http://rebel13.nl/home/nnue.html) by [Ed Schröder](Ed_Schroder "Ed Schroder")
* [NNUE Guide (nnue-pytorch/nnue.md at master · glinscott/nnue-pytorch · GitHub)](https://github.com/glinscott/nnue-pytorch/blob/master/docs/nnue.md) hosted by [Gary Linscott](Gary_Linscott "Gary Linscott")


### NNUE libraries


Some developers disintegrate and rewrite the Stockfish NNUE code into independent libraries which can be much easier to embed into other chess engines.



* [GitHub - david-carteau/cerebrum: The Cerebrum library](https://github.com/david-carteau/cerebrum) by [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)") » [Cerebrum](index.php?title=Cerebrum&action=edit&redlink=1 "Cerebrum (page does not exist)")
* [GitHub - dshawul/nncpu-probe](https://github.com/dshawul/nncpu-probe) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul")
* [GitHub - jdart1/nnue: NNUE reading code for chess](https://github.com/jdart1/nnue) by [Jon Dart](Jon_Dart "Jon Dart")


### Source Code


* [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
* [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
* [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) ([Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") by [Nodchip](Hisayori_Noda "Hisayori Noda"))
* [A Leela NNUE? Night Nurse and Others · dkappe/leela-chess-weights Wiki · GitHub](https://github.com/dkappe/leela-chess-weights/wiki/A-Leela-NNUE%3F-Night-Nurse-and-Others) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe")
* [GitHub - DanielUranga/TensorFlowNNUE](https://github.com/DanielUranga/TensorFlowNNUE) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga")
* [GitHub - glinscott/nnue-pytorch: NNUE (Chess evaluation) trainer in Pytorch](https://github.com/glinscott/nnue-pytorch) by [Gary Linscott](Gary_Linscott "Gary Linscott")
* [GitHub - connormcmonigle/seer-nnue: UCI chess engine using neural networks for position evaluation](https://github.com/connormcmonigle/seer-nnue) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle") » [Seer](Seer "Seer")
* [GitHub - bmdanielsson/nnue-trainer: PyTorch trainer for NNUE style neural networks](https://github.com/bmdanielsson/nnue-trainer) by [Martin Danielsson](Martin_Danielsson "Martin Danielsson") » [Marvin](Marvin "Marvin") [[27]](#cite_note-27)
* [GitHub - fsmosca/Mabigat: NNUE parameter optimizer](https://github.com/fsmosca/Mabigat) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca") » [Automated Tuning](Automated_Tuning "Automated Tuning")


### Misc


* [Lower Numerical Precision Deep Learning Inference and Training](https://software.intel.com/content/www/us/en/develop/articles/lower-numerical-precision-deep-learning-inference-and-training.html) by [Andres Rodriguez](https://community.intel.com/t5/user/viewprofilepage/user-id/134067) et al., [Intel](Intel "Intel"), January 19, 2018 » [AVX-512](AVX-512 "AVX-512")
* [Nue from Wikipedia](https://en.wikipedia.org/wiki/Nue)
* [Hiromi](Category:Hiromi_Uehara "Category:Hiromi Uehara") - [Spectrum](https://en.wikipedia.org/wiki/Spectrum_(Hiromi_album)), 2019, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


  
## References


1. [↑](#cite_ref-1) [Nue](https://en.wikipedia.org/wiki/Nue) (鵺) from the [Konjaku Gazu Zoku Hyakki](https://en.wikipedia.org/wiki/Konjaku_Gazu_Zoku_Hyakki) (今昔画図続百鬼) by [Toriyama Sekien](Category:Toriyama_Sekien "Category:Toriyama Sekien"), circa 1779, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. [↑](#cite_ref-2) [Re: What does NNUE actually mean](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74611&start=2) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 29, 2020
3. [↑](#cite_ref-3) [機械学習エンジニアのための将棋AI開発入門その1 Introduction to Shogi AI development for machine learning engineers Part 1](http://yaneuraou.yaneu.com/2020/05/03/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E5%B0%86%E6%A3%8Bai%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80%E3%81%9D%E3%81%AE1/), May 03, 2020 (Japanese)
4. [↑](#cite_ref-4) [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf) (Japanese with English abstract)
5. [↑](#cite_ref-5) [GitHub - yaneurao/YaneuraOu: YaneuraOu is the World's Strongest Shogi engine(AI player), WCSC29 1st winner, educational and USI compliant engine](https://github.com/yaneurao/YaneuraOu)
6. [↑](#cite_ref-6) [GitHub - Tama4649/Kristallweizen: 第29回世界コンピュータ将棋選手権 準優勝のKristallweizenです。](https://github.com/Tama4649/Kristallweizen/)
7. [↑](#cite_ref-7) [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020
8. [↑](#cite_ref-8) [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
9. [↑](#cite_ref-9) [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 16, 2020
10. [↑](#cite_ref-10) [Orion 0.7 : NNUE experiment](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74828) by [David Carteau](index.php?title=David_Carteau&action=edit&redlink=1 "David Carteau (page does not exist)"), [CCC](CCC "CCC"), August 19, 2020
11. [↑](#cite_ref-11) [Re: New engine releases 2020...Don NNUE 2020?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=320#p856640) by supersharp77, [CCC](CCC "CCC"), August 19, 2020
12. [↑](#cite_ref-12) [... the last shall be first ...](http://talkchess.com/forum3/viewtopic.php?f=2&t=74825) by [MikeB](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), 19 Aug 2020
13. [↑](#cite_ref-13) [Introducing Igel chess engine](http://talkchess.com/forum3/viewtopic.php?f=2&t=67890&start=10#p856742) by [Volodymyr Shcherbyna](Volodymyr_Shcherbyna "Volodymyr Shcherbyna"), [CCC](CCC "CCC"), 20 Aug 2020
14. [↑](#cite_ref-14) [Night Nurse 0.2](http://talkchess.com/forum3/viewtopic.php?f=2&t=74837) by [Dietrich Kappe](Dietrich_Kappe "Dietrich Kappe"), [CCC](CCC "CCC"), August 19, 2020
15. [↑](#cite_ref-15) [Re: Hacking around CFish NNUE](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75400&start=22) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 15, 2020
16. [↑](#cite_ref-16) [Re: How to scale stockfish NNUE score?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75415&start=3) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), October 17, 2020
17. [↑](#cite_ref-17) [Dragon by Komodo Chess](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75748) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 10, 2020
18. [↑](#cite_ref-18) Image from [Yu Nasu](Yu_Nasu "Yu Nasu") (**2018**). *ƎUИИ Efficiently Updatable Neural-Network based Evaluation Functions for Computer Shogi*. Ziosoft Computer Shogi Club, [pdf](https://github.com/ynasu87/nnue/blob/master/docs/nnue.pdf) (Japanese with English abstract)
19. [↑](#cite_ref-19) [Translation of Yu Nasu's NNUE paper](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76250) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), January 07, 2021
20. [↑](#cite_ref-20) [Book about Neural Networks for Chess](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78283) by dkl, [CCC](CCC "CCC"), September 29, 2021
21. [↑](#cite_ref-21) [Outer product from Wikipedia](https://en.wikipedia.org/wiki/Outer_product)
22. [↑](#cite_ref-22) [Tensor product from Wikipedia](https://en.wikipedia.org/wiki/Tensor_product)
23. [↑](#cite_ref-23) [PyTorch from Wikipedia](https://en.wikipedia.org/wiki/PyTorch)
24. [↑](#cite_ref-24) [TensorFlow from Wikipedia](https://en.wikipedia.org/wiki/TensorFlow)
25. [↑](#cite_ref-25) [Vafra](http://www.jurjevic.org.uk/chess/vafra/index.html) by [Robert Jurjević](index.php?title=Robert_Jurjevi%C4%87&action=edit&redlink=1 "Robert Jurjević (page does not exist)")
26. [↑](#cite_ref-26) [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474) by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk")
27. [↑](#cite_ref-27) [nnue-trainer](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76964) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), March 27, 2021

**[Up one Level](Neural_Networks "Neural Networks")**







 
