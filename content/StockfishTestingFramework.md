---
title: StockfishTestingFramework
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Stockfish**



 [](File:Stockfish-logo.png) Stockfish logo [[1]](#cite_note-1) 
 [](https://stockfishchess.org/) Stockfish 12 logo [[2]](#cite_note-2) 
**Stockfish**,  

an [UCI](UCI "UCI") compatible [open source](Category:Open_Source "Category:Open Source") chess engine developed by [Tord Romstad](Tord_Romstad "Tord Romstad"), [Marco Costalba](Marco_Costalba "Marco Costalba"), [Joona Kiiski](Joona_Kiiski "Joona Kiiski") and [Gary Linscott](Gary_Linscott "Gary Linscott") [[3]](#cite_note-3), licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"). Marco forked the project from version 2.1 of Tord's engine [Glaurung](Glaurung "Glaurung"), first announced by Marco in November 8, 2008 [[4]](#cite_note-4), and in early 2009 Joona's [Smaug](Smaug "Smaug"), a further Glaurung 2.2 derivative, was incorporated [[5]](#cite_note-5) . Starting out among the top twenty engines, Stockfish has quickly climbed in [strength](Playing_Strength "Playing Strength") to become the world strongest chess entity as of 2018 - at least concerning the [AlphaZero](AlphaZero "AlphaZero") hype [[6]](#cite_note-6), public available chess entity. The name "Stockfish" reflects the ancestry of the engine. Tord is Norwegian and Marco Italian, and there is a long history of [stockfish](https://en.wikipedia.org/wiki/Stockfish) trade from Norway to Italy (to Marco's home town of [Vicenza](https://en.wikipedia.org/wiki/Vicenza), in fact). Stockfish also referred another famous "little fish", the then strongest chess engine [Rybka](Rybka "Rybka"). In 2011, Marco Costalba and Joona Kiiski stepped down as Stockfish maintainers [[7]](#cite_note-7). From that, the project is being developed and maintained by the [Stockfish community](Category:Stockfish_Contributor "Category:Stockfish Contributor"). 


A synergy effect with the [Shogi](Shogi "Shogi") community led to the promising branch of [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE"), courtesy of [Nodchip](Hisayori_Noda "Hisayori Noda"), who introduced [NNUE](NNUE "NNUE") to Stockfish in 2019 [[8]](#cite_note-8). On September 02, 2020, **Stockfish 12** was released with a huge jump in [playing strength](Playing_Strength "Playing Strength") due to NNUE and further [tuning](Automated_Tuning "Automated Tuning") of the engine [[9]](#cite_note-9). The release of **Stockfish 13** on February 19, 2021, has been triggered by the start of sales of the [Fat Fritz 2](Fat_Fritz#Fat_Fritz_2 "Fat Fritz") engine by [ChessBase](ChessBase "ChessBase"), based on a recent development version of Stockfish with minor modifications [[10]](#cite_note-10). **Stockfish 14**, released on July 02, 2021, further improved due to efforts by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk") and [Gary Linscott](Gary_Linscott "Gary Linscott") in designing a new [NNUE architecture](Stockfish_NNUE#HalfKA "Stockfish NNUE") in conjunction with a [GPU](GPU "GPU") accelerated trainer written in [PyTorch](https://en.wikipedia.org/wiki/PyTorch). Further, the collaboration with the [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") team payed off, in providing billions of positions to train the new NNUE [[11]](#cite_note-11).


**Stockfish 16**, released June 30, 2023, removes the classical [evaluation](Evaluation "Evaluation") from the engine and focuses on [NNUE](NNUE "NNUE") neural networks.[[12]](#cite_note-12)



## Platforms


Since Stockfish is written in [C++](Cpp "Cpp"), it may be compiled and build for various processors and operating systems such as [Android](Android "Android"), [iOS](index.php?title=IOS&action=edit&redlink=1 "IOS (page does not exist)"), [Linux](Linux "Linux"), [macOS](Mac_OS "Mac OS"), and [Windows](Windows "Windows"). Stockfish for [macOS](Mac_OS "Mac OS") was built by [Daylen Yang](Daylen_Yang "Daylen Yang"), who is also responsible for the Stockfish website. Stockfish for [iOS](index.php?title=IOS&action=edit&redlink=1 "IOS (page does not exist)") was built by Tord Romstad [[13]](#cite_note-13).




## Fishtest


The Stockfish Testing Framework dubbed **Fishtest** [[14]](#cite_note-14) is a [web application](https://en.wikipedia.org/wiki/Web_application) written by [Gary Linscott](Gary_Linscott "Gary Linscott") [[15]](#cite_note-15) [[16]](#cite_note-16), based on a [SETI@home](https://en.wikipedia.org/wiki/SETI@home) kind of [volunteer computing](https://en.wikipedia.org/wiki/Volunteer_computing).
Fishtest is mainly written in [Python](Python "Python") under the *Pyramid Application Development Framework* [[17]](#cite_note-17), and distributes games across different machines to reduce the test latency and increment throughput. Started in early 2013 with Stockfish 3.0, Fishtest has hundreds of contributors, as of June 2018, 1130 testers and 162 developers [[18]](#cite_note-18) active in testing ideas and tweaks [[19]](#cite_note-19), to make Stockfish the strongest chess entity of the world [[20]](#cite_note-20).




## Evaluation Guide


Since April 2017 the interactive **Stockfish Evaluation Guide** is available to explore Stockfish's [evaluation](Evaluation "Evaluation") with a [JavaScript](JavaScript "JavaScript") implementation running in a [browser](https://en.wikipedia.org/wiki/Web_browser) [[21]](#cite_note-21) . One may enter a [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") string of a [position](Chess_Position "Chess Position"), to get the resulting [score](Score "Score") of the main evaluation term considering the [game phases](Game_Phases "Game Phases") within its [tapered evaluation](Tapered_Eval "Tapered Eval"), and may navigate through the tree of subterms and features with its particular characteristics for the given position [[22]](#cite_note-22), also supporting [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") nets [[23]](#cite_note-23).



## Tournament Play


Stockfish is top contender of the prestigious [Top Chess Engines Competition (TCEC)](TCEC "TCEC"), reaching the superfinals since [season 4](TCEC_Season_4 "TCEC Season 4"), and established its world number one status in winning TCECs, leaving its commercial rivals [Komodo](Komodo "Komodo") and [Houdini](Houdini "Houdini") behind.
Since [season 14](TCEC_Season_14#Superfinal "TCEC Season 14") in early 2019, Stockfish competes with the [deep learning](Deep_Learning "Deep Learning") [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero") engines, whose [playing strength](Playing_Strength "Playing Strength") triggered a motivation boost in the developing community to further improve Stockfish.




## GM+Rybka vs. Stockfish


On July 19, 2014, Stockfish 5 played a four game match versus [Daniel Naroditsky](https://en.wikipedia.org/wiki/Daniel_Naroditsky) plus [Rybka 3](Rybka "Rybka") (2008), 45 minutes plus 30-second increment. Stockfish won 3½ - ½ [[24]](#cite_note-24) [[25]](#cite_note-25) . A few weeks later the experiment continued with [Hikaru Nakamura](https://en.wikipedia.org/wiki/Hikaru_Nakamura) in [Burlingame, California](https://en.wikipedia.org/wiki/Burlingame,_California) [[26]](#cite_note-26) . Supported two games by Rybka 3, Nakamura lost ½ - 1½, two games with pawn odds (Stockfish both Black without h- and b-pawn) ended ½ - 1½ in favour to Stockfish 5 as well. It played the latest development build compiled for [OS X](Mac_OS "Mac OS") running on a 3 GHz 8-Core [Mac Pro](Macintosh "Macintosh") [[27]](#cite_note-27) .



## Selected Features


[[28]](#cite_note-28)



### [Board Representation](Board_Representation "Board Representation")


* [8x8 Board](8x8_Board "8x8 Board")
* [Bitboards](Bitboards "Bitboards") with [Little-Endian Rank-File Mapping (LERF)](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


 [BMI2 - PEXT Bitboards](BMI2#PEXTBitboards "BMI2") (not recommend for [AMD](AMD "AMD") [Ryzen](https://en.wikipedia.org/wiki/Ryzen) [[29]](#cite_note-29) prior to [Zen 3](https://en.wikipedia.org/wiki/Zen_3))
* [Piece-Lists](Piece-Lists "Piece-Lists") until Stockfish 12 [[30]](#cite_note-30) [[31]](#cite_note-31) [[32]](#cite_note-32)


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Parallel Search](Parallel_Search "Parallel Search") using [Threads](Thread "Thread")
	+ [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept") prior to Stockfish 7
	+ [Lazy SMP](Lazy_SMP "Lazy SMP") since Stockfish 7, January 2016
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ 10 [Bytes](Byte "Byte") per [Entry](Transposition_Table#Entry "Transposition Table"), 3 Entries per [Cluster](Transposition_Table#Bucket "Transposition Table")
	+ [Depth-preferred Replacement Strategy](Transposition_Table#ReplacementStrategies "Transposition Table")
	+ No [PV-Node](Node_Types#PV "Node Types") probing
	+ [Prefetch](Memory#Cache "Memory")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
	+ [Counter Moves History](History_Heuristic#CMHist "History Heuristic") since Stockfish 7, January 2016 [[33]](#cite_note-33)
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Selectivity](Selectivity "Selectivity")
	+ [Extensions](Extensions "Extensions")
		- [Check Extensions](Check_Extensions "Check Extensions") if [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") >= 0
		- [Restricted Singular Extensions](Singular_Extensions#RestrictedSE "Singular Extensions")
	+ [Pruning](Pruning "Pruning")
		- [Futility Pruning](Futility_Pruning "Futility Pruning")
		- [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
		- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
			* [Dynamic Depth Reduction](Depth_Reduction_R "Depth Reduction R") based on [depth](Depth "Depth") and [value](Score "Score")
			* [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
			* [Verification search](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning") at high depths
		- [ProbCut](ProbCut "ProbCut")
		- [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Reductions](Reductions "Reductions")
		- [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
		- [Razoring](Razoring "Razoring")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE")
	+ [HalfKP](Stockfish_NNUE#HalfKP "Stockfish NNUE") (Stockfish 12)
	+ [HalfKAv2](Stockfish_NNUE#HalfKA "Stockfish NNUE") (Stockfish 14)


 *See also* [Evaluation Philosophy](Evaluation_Philosophy "Evaluation Philosophy") [[34]](#cite_note-34) [[35]](#cite_note-35)
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Score Grain](Score#Grain "Score"): ~1/256 of a [pawn unit](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Material](Material "Material")
	+ [Point Values](Point_Value "Point Value")
		- [Midgame](Middlegame "Middlegame"): 198, 817, 836, 1270, 2521
		- [Endgame](Endgame "Endgame"): 258, 846, 857, 1278, 2558
	+ [Bishop Pair](Bishop_Pair "Bishop Pair")
	+ [Imbalance Tables](Material_Tables "Material Tables")
	+ [Material Hash Table](Material_Hash_Table "Material Hash Table")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Space](Space "Space")
* [Mobility](Mobility "Mobility")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Outposts](Outposts "Outposts")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Phalanx](Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)")
	+ [Connected Pawns](Connected_Pawns "Connected Pawns")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")
	+ [Square Control](King_Safety#SquareControl "King Safety")
* [Evaluation Patterns](Evaluation_Patterns "Evaluation Patterns")


### Misc


* [Chess960](Chess960 "Chess960")
* [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")


 [SPSA](SPSA "SPSA")
* [Syzygy Bases](Syzygy_Bases "Syzygy Bases")


## Release Dates


### 2008


* Stockfish 1.0 - November 02, 2008
* Stockfish 1.01 - November 03, 2008
* Stockfish 1.1 - December 06, 2008
* Stockfish 1.1a - December 08, 2008
* Stockfish 1.2 - December 29, 2008


### 2009


* Stockfish 1.3 - May 02, 2009
* Stockfish 1.3.1 - May 03, 2009
* Stockfish 1.4 - July 05, 2009
* Stockfish 1.5 - October 04, 2009
* Stockfish 1.5.1 - October 11, 2009
* Stockfish 1.6 - December 25, 2009
* Stockfish 1.6.1 - December 25, 2009
* Stockfish 1.6.2 - December 31, 2009


### 2010 ...


* Stockfish 1.6.3 - February 02, 2010
* Stockfish 1.7 - April 08, 2010
* Stockfish 1.7.1 - April 10, 2010
* Stockfish 1.8 - July 02, 2010
* Stockfish 1.9 - October 02, 2010
* Stockfish 1.9.1 - October 05, 2010


**2011**



* Stockfish 2.0 - January 01, 2011
* Stockfish 2.0.1 - January 04, 2011
* Stockfish 2.1 - May 04, 2011
* Stockfish 2.1.1 - May 08, 2011
* Stockfish 2.2 - December 29, 2011


**2012**



* Stockfish 2.2.1 - January 06, 2012
* Stockfish 2.2.2 - January 14, 2012
* Stockfish 2.3 - September 15, 2012
* Stockfish 2.3.1 - September 22, 2012


**2013**



* Stockfish 3 - April 30, 2013
* Stockfish 4 - August 20, 2013
* Stockfish DD - November 29, 2013
* Stockfish 5 - May 31, 2014


### 2015 ...


* Stockfish 6 - January 27, 2015
* Stockfish 7 - January 02, 2016
* Stockfish 8 - November 01, 2016
* Stockfish 9 - February 01, 2018
* Stockfish 10 - November 29, 2018


### 2020 ...


* Stockfish 11 - January 18, 2020
* [Stockfish 12](Stockfish_NNUE "Stockfish NNUE") - September 02, 2020
* Stockfish 13 - February 19, 2021
* Stockfish 14 - July 02, 2021
* Stockfish 15 - April 18, 2022
* Stockfish 15.1 - December 04, 2022
* Stockfish 16 - June 30, 2023






## Ports


* [asmFish](AsmFish "AsmFish")
* [CFish](CFish "CFish")
* [DroidFish](DroidFish "DroidFish")
* [Fat Titz](Fat_Titz "Fat Titz")
* [Portfish](Portfish "Portfish")
* [Rustfish](Rustfish "Rustfish")
* [Stockfish-js](Stockfish-js "Stockfish-js") [[36]](#cite_note-36)






## Derivatives


* [Brainfish](Brainfish "Brainfish")
* [Crystal](Crystal "Crystal")
* [DON](DON "DON")
* [Eman](Eman "Eman")
* [Fat Fritz 2.0](Fat_Fritz#Fat_Fritz_2 "Fat Fritz")
* [Houdini](Houdini "Houdini")
* [McBrain](index.php?title=McBrain&action=edit&redlink=1 "McBrain (page does not exist)")
* [ShashChess](ShashChess "ShashChess")
* [Sting](index.php?title=Sting&action=edit&redlink=1 "Sting (page does not exist)")
* [SugaR](SugaR "SugaR")


## Authors


### Founders of the Stockfish project and Fishtest infrastructure


* [Marco Costalba](Marco_Costalba "Marco Costalba")
* [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
* [Gary Linscott](Gary_Linscott "Gary Linscott")
* [Tord Romstad](Tord_Romstad "Tord Romstad")


### Authors and inventors of NNUE, training, NNUE port


* [Yu Nasu](Yu_Nasu "Yu Nasu")
* [Motohiro Isozaki](Motohiro_Isozaki "Motohiro Isozaki")
* [Hisayori Noda](Hisayori_Noda "Hisayori Noda")


### All other authors of the code


There are 196 authors, counted to version 15.1.



* [Contributors](Category:Stockfish_Contributor "Category:Stockfish Contributor")


## Elo Progress


of Stockfish in first 10 years [[37]](#cite_note-37)



 [](File:SfElo.png) 
## See also


* [Evaluation Philosophy](Evaluation_Philosophy "Evaluation Philosophy")
* [Glaurung](Glaurung "Glaurung")
* [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")
* [Raspberry Turk](Raspberry_Turk "Raspberry Turk")
* [NNUE](NNUE "NNUE")
* [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
	+ [HalfKP](Stockfish_NNUE#HalfKP "Stockfish NNUE") (Stockfish 12)
	+ [HalfKAv2](Stockfish_NNUE#HalfKA "Stockfish NNUE") (Stockfish 14)


## Publications


* [Arno Nickel](Arno_Nickel "Arno Nickel") (**2012**). *[Die schöne neue Welt der Schachengines](http://www.edition-marco-shop.de/epages/64079634.sf/de_DE/?ObjectPath=/Shops/64079634/Categories/Schachgeschehen/Computerschach)*. [SCHACH](http://www.zeitschriftschach.de/) 2,3,5,6 2012, [pdf](http://www.edition-marco-shop.de/WebRoot/Store14/Shops/64079634/5177/F0A3/C389/D0DD/3A71/C0A8/2935/25F6/Die_schoene_neue_Welt_der_Schachengines.pdf) (German) [[38]](#cite_note-38)
* [Oleg Arenz](index.php?title=Oleg_Arenz&action=edit&redlink=1 "Oleg Arenz (page does not exist)") (**2012**). *Monte Carlo Chess*. B.Sc. thesis, [Darmstadt University of Technology](Darmstadt_University_of_Technology "Darmstadt University of Technology"), advisor [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz"), [pdf](http://www.ke.tu-darmstadt.de/lehre/arbeiten/bachelor/2012/Arenz_Oleg.pdf) » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Quantifying Depth and Complexity of Thinking and Knowledge*. [ICAART 2015](http://www.icaart.org/EuropeanProjectSpace.aspx?y=2015), [pdf](http://www.cse.buffalo.edu/~regan/papers/pdf/BiReICAART15CR.pdf)
* [Tamal T. Biswas](Tamal_T._Biswas "Tamal T. Biswas"), [Kenneth W. Regan](Kenneth_W._Regan "Kenneth W. Regan") (**2015**). *Measuring Level-K Reasoning, Satisficing, and Human Error in Game-Play Data*. [IEEE](IEEE "IEEE") [ICMLA 2015](http://www.icmla-conference.org/icmla15/), [pdf preprint](http://www.cse.buffalo.edu/~regan/papers/pdf/BiRe15_ICMLA2015.pdf)
* [Shu Yokoyama](Shu_Yokoyama "Shu Yokoyama"), [Tomoyuki Kaneko](Tomoyuki_Kaneko "Tomoyuki Kaneko"), [Tetsuro Tanaka](Tetsuro_Tanaka "Tetsuro Tanaka") (**2015**). *Parameter-Free Tree Style Pipeline in Asynchronous Parallel Game-Tree Search*. [Advances in Computer Games 14](Advances_in_Computer_Games_14 "Advances in Computer Games 14") , [pdf](http://www.graco.c.u-tokyo.ac.jp/~kaneko/papers/acg2015-yokoyama.pdf) » [P-GPP](Shu_Yokoyama#PGPP "Shu Yokoyama")
* [Jean-Marc Alliot](Jean-Marc_Alliot "Jean-Marc Alliot") (**2017**). *Who is the Master*? [ICGA Journal, Vol. 39, No. 1](ICGA_Journal#39_1 "ICGA Journal"), [draft as pdf](http://www.alliot.fr/CHESS/draft-icga-39-1.pdf) [[39]](#cite_note-39)
* [Bill Jordan](Bill_Jordan "Bill Jordan") (**2020**). *Calculation versus Intuition: Stockfish versus Leela*. [amazon](https://www.amazon.com/Calculation-versus-Intuition-Stockfish-Leela-ebook/dp/B08LYBQDMB/) » [TCEC](TCEC "TCEC"), [Leela Chess Zero](Leela_Chess_Zero "Leela Chess Zero")


## Forum Posts


### 2008 ...


* [Stockfish 1.0](http://www.talkchess.com/forum/viewtopic.php?t=24675) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 02, 2008
* [Please drop Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=24771) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 07, 2008


**2009**



* [Re: Stockfish - Glaurung](http://wbec-ridderkerk.forumotion.com/wbec-ridderkerk-news-info-f1/stockfish-glaurung-t402.htm) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [WBEC-Ridderkerk forum](http://wbec-ridderkerk.forumotion.com/forum.htm), September 05, 2009
* [Stockfish 1.5.1](http://www.talkchess.com/forum/viewtopic.php?t=30051) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 08, 2009


### 2010 ...


* [Stockfish 1.7](http://www.talkchess.com/forum/viewtopic.php?t=33677) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), April 08, 2010
* [Stockfish-1.7.0 Hyper-threading Detection](http://www.talkchess.com/forum/viewtopic.php?t=33705) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), April 09, 2010 » [Thread](Thread "Thread")
* [stockfish fail high fail low](http://www.talkchess.com/forum/viewtopic.php?t=33779) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 13, 2010
* [MTD experiment with stockfish 1.7.1](http://www.talkchess.com/forum/viewtopic.php?t=33813) by [Vratko Polák](index.php?title=Vratko_Pol%C3%A1k&action=edit&redlink=1 "Vratko Polák (page does not exist)"), [CCC](CCC "CCC"), April 15, 2010
* [about stockfish and logic](http://www.talkchess.com/forum/viewtopic.php?t=33842) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), April 17, 2010
* [Stockfish - material balance/imbalance evaluation](http://www.talkchess.com/forum/viewtopic.php?t=34159) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), May 05, 2010
* [Qsearch of Stockfish 1.7.1](http://www.talkchess.com/forum/viewtopic.php?t=34286) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), May 13, 2010
* [Stockfish do\_move + undo\_move](http://www.talkchess.com/forum/viewtopic.php?t=34670) by [Matthew Purland](index.php?title=Matthew_Purland&action=edit&redlink=1 "Matthew Purland (page does not exist)"), [CCC](CCC "CCC"), June 02, 2010
* [static null move pruning is stockfish](http://www.talkchess.com/forum/viewtopic.php?t=34909) by [Tom King](Tom_King "Tom King"), [CCC](CCC "CCC"), June 13, 2010
* [Stockfish - single evasion extensions](http://www.talkchess.com/forum/viewtopic.php?t=35186) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), June 27, 2010
* [Stockfish 1.8 JA available](http://www.talkchess.com/forum/viewtopic.php?t=35246) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), July 02, 2010
* [stockfish 1.8 - Eval hash gone?](http://www.talkchess.com/forum/viewtopic.php?t=35284) by [Edward Yu](index.php?title=Edward_Yu&action=edit&redlink=1 "Edward Yu (page does not exist)"), [CCC](CCC "CCC"), July 04, 2010
* [Stockfish Singular Extension, does it make sense?](http://www.talkchess.com/forum/viewtopic.php?t=35419) by [Volker Böhm](Volker_B%C3%B6hm "Volker Böhm"), [CCC](CCC "CCC"), July 08, 2010
* [Stockfish 1.8 tweaks](http://www.talkchess.com/forum/viewtopic.php?t=35355) by [Vratko Polák](index.php?title=Vratko_Pol%C3%A1k&action=edit&redlink=1 "Vratko Polák (page does not exist)"), [CCC](CCC "CCC"), July 09, 2010
* [Stockfish question](http://www.open-chess.org/viewtopic.php?f=3&t=423) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 10, 2010
* [Taken from CCC (Stockfish & mainlines)](http://www.open-chess.org/viewtopic.php?f=5&t=434) by [Rebel](Ed_Schroder "Ed Schroder"), [OpenChess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), July 12, 2010
* [backward pawns in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=35459) by [Marek Kwiatkowski](index.php?title=Marek_Kwiatkowski&action=edit&redlink=1 "Marek Kwiatkowski (page does not exist)"), [CCC](CCC "CCC"), July 16, 2010
* [Questions for the Stockfish team](http://www.talkchess.com/forum/viewtopic.php?t=35455) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), July 16, 2010
* [Stockfish 1.8 - eval cache](http://www.talkchess.com/forum/viewtopic.php?t=35496) by [Ralph Stoesser](index.php?title=Ralph_Stoesser&action=edit&redlink=1 "Ralph Stoesser (page does not exist)"), [CCC](CCC "CCC"), July 18, 2010 » [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
* [Stockfish null move pre-condition](http://www.talkchess.com/forum/viewtopic.php?t=35543) by [Rein Halbersma](Rein_Halbersma "Rein Halbersma"), [CCC](CCC "CCC"), July 22, 2010 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Stockfish for 39 dollars](http://www.talkchess.com/forum/viewtopic.php?t=35901) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), August 26, 2010
* [Stockfish 1.9 JA update available](http://www.talkchess.com/forum/viewtopic.php?t=36239) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), October 02, 2010
* [mobility evaluation of stockfish](http://www.talkchess.com/forum/viewtopic.php?t=36307) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), October 09, 2010


**2011**



* [Stockfish 2.0 Available](http://www.talkchess.com/forum/viewtopic.php?t=37399) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), January 01, 2011
* [Stockfish 2.0.0 tests](http://www.talkchess.com/forum/viewtopic.php?t=37450) by [Harun Taner](Harun_Taner "Harun Taner"), [CCC](CCC "CCC"), January 04, 2011
* [Stockfish "Use Sleeping Threads" Test](http://www.talkchess.com/forum/viewtopic.php?t=37468) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), January 05, 2011
* [StockFish engine](http://www.talkchess.com/forum/viewtopic.php?t=37573) by [Andriy Dzyben](index.php?title=Andriy_Dzyben&action=edit&redlink=1 "Andriy Dzyben (page does not exist)"), [CCC](CCC "CCC"), January 11, 2011
* [Designing an analysis friendly Stockfish?](http://www.open-chess.org/viewtopic.php?f=5&t=1042) by Uly, [Open Chess Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), January 28, 2011
* [Why are the Ippo derivative stronger than Stockfish?](http://www.talkchess.com/forum/viewtopic.php?t=38198) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), 24 February, 2011
* [Transposition Table updates in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=38740) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), April 12, 2011 » [Transposition Table](Transposition_Table "Transposition Table")
* [Stockfish random generator (rkiss.h)](http://www.talkchess.com/forum/viewtopic.php?t=38760) by [Martin Sedlak](Martin_Sedlak "Martin Sedlak"), [CCC](CCC "CCC"), Apr 15, 2011 » [Bob Jenkins](Bob_Jenkins "Bob Jenkins")
* [futility pruning in stockfish](http://www.talkchess.com/forum/viewtopic.php?t=39169) by [Engin Üstün](Engin_%C3%9Cst%C3%BCn "Engin Üstün"), [CCC](CCC "CCC"), May 25, 2011 » [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Stockfish clones in the AppStore: it's becoming a plague...](http://www.talkchess.com/forum/viewtopic.php?t=39214) by [Julien Marcel](Julien_Marcel "Julien Marcel"), [CCC](CCC "CCC"), May 28, 2011 » [Clones](Category:Clone "Category:Clone")
* [Root node search in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=39346) by [Onno Garms](Onno_Garms "Onno Garms"), [CCC](CCC "CCC"), June 12, 2011 » [Move Ordering](Move_Ordering "Move Ordering"), [Root](Root "Root")
* [Grandmaster prefers Stockfish evals](http://www.talkchess.com/forum/viewtopic.php?t=40562) by [Albert Silver](Albert_Silver "Albert Silver"), [CCC](CCC "CCC"), September 29, 2011
* [Stockfish on github](http://www.talkchess.com/forum/viewtopic.php?t=40610) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 02, 2011
* [Stockfish's tuning method](http://www.talkchess.com/forum/viewtopic.php?t=40662) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), October 07, 2011 » [Stockfish's Tuning Method](Stockfish%27s_Tuning_Method "Stockfish's Tuning Method")


**2012**



* [StockFish LS with LimitStrength feature](http://www.talkchess.com/forum/viewtopic.php?t=41732) by [Alexander Schmidt](index.php?title=Alexander_Schmidt&action=edit&redlink=1 "Alexander Schmidt (page does not exist)"), [CCC](CCC "CCC"), January 01, 2012
* [Stockfish Code ( Piece Value's)](http://www.talkchess.com/forum/viewtopic.php?t=41916) by Nolan Denson, [CCC](CCC "CCC"), January 10, 2012 » [Point Value](Point_Value "Point Value")
* [Stockfish hash implementation](http://www.talkchess.com/forum/viewtopic.php?t=41917) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), January 10, 2012 » [Transposition Table](Transposition_Table "Transposition Table")
* [Stockfish 2.2.2 JA update available](http://www.talkchess.com/forum/viewtopic.php?t=41999) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), January 14, 2012
* [CLOP on Stockfish](http://www.talkchess.com/forum/viewtopic.php?p=454327) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), March 10, 2012 » [CLOP](CLOP "CLOP")
* [optimal aspiration window for stockfish question](http://www.talkchess.com/forum/viewtopic.php?t=42841) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), March 12, 2012 » [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Raspberry Pi / Stockfish dedicated chess computer/board](http://www.talkchess.com/forum/viewtopic.php?t=44901) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), August 26, 2012 » [Raspberry Pi](Raspberry_Pi "Raspberry Pi"), [Dedicated Chess Computers](Dedicated_Chess_Computers "Dedicated Chess Computers")
* [Stockfish 2.3 update available](http://www.talkchess.com/forum/viewtopic.php?t=45163) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), September 15, 2012


**2013**



* [10 Lessons to be Learned from todays Top Engines](http://rybkaforum.net/cgi-bin/rybkaforum/topic_show.pl?tid=26392) by Josef, [Rybka Forum](Computer_Chess_Forums "Computer Chess Forums"), January 03, 2013 » [Houdini](Houdini "Houdini"), [Komodo](Komodo "Komodo")
* [Stockfish 3 Official JA Windows/Linux builds available](http://www.talkchess.com/forum/viewtopic.php?t=47881) by [Jim Ablett](Jim_Ablett "Jim Ablett"), [CCC](CCC "CCC"), April 30, 2013
* [Fishtest Distributed Testing Framework](http://www.talkchess.com/forum/viewtopic.php?t=47885) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 01, 2013 » [Fishtest](Stockfish#Fishtest "Stockfish")
* [Re: History pruning / move ordering question](http://www.talkchess.com/forum/viewtopic.php?t=47953&start=10) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), May 12, 2013 » [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
* [Stockfish 3 PA\_GTB](http://open-chess.org/viewtopic.php?f=7&t=2322) by [Jeremy Bernstein](Jeremy_Bernstein "Jeremy Bernstein"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), May 15, 2013
* [Probcut](http://www.talkchess.com/forum/viewtopic.php?p=518426) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), May 24, 2013 » [ProbCut](ProbCut "ProbCut")
* [Stockfish bug](http://www.talkchess.com/forum/viewtopic.php?t=48149) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), May 30, 2013 » [Repetitions](Repetitions "Repetitions")
* [The Ultimate Stockfish!](http://www.talkchess.com/forum/viewtopic.php?t=48602) by [Mike Scheidl](index.php?title=Michael_Scheidl&action=edit&redlink=1 "Michael Scheidl (page does not exist)"), [CCC](CCC "CCC"), July 09, 2013
* [use sleeping threads](http://www.talkchess.com/forum/viewtopic.php?t=48612) by [Don Dailey](Don_Dailey "Don Dailey"), [CCC](CCC "CCC"), July 10, 2013 » [Parallel Search](Parallel_Search "Parallel Search"), [Thread](Thread "Thread")
* [Stockfish 4](http://www.talkchess.com/forum/viewtopic.php?t=49035) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 20, 2013
* [18 days from SF4 release and about ~30+ ELO gain!](http://www.talkchess.com/forum/viewtopic.php?t=49283) by Alexandre Meirelles Souza, [CCC](CCC "CCC"), September 08, 2013
* [How much of Stockfish code is still from Tord Romstad?](http://www.talkchess.com/forum/viewtopic.php?t=49375) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 16, 2013
* [Syzygy tablebases, work in Stockfish?](http://www.talkchess.com/forum/viewtopic.php?t=49439) by [Jose Mº Velasco](Jose_Maria_Velasco "Jose Maria Velasco"), [CCC](CCC "CCC"), September 23, 2013 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Stockfish search](http://www.talkchess.com/forum/viewtopic.php?t=49854) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), October 28, 2013 » [Principal Variation](Principal_Variation "Principal Variation")
* [Some food for thought](http://hiarcs.net/forums/viewtopic.php?t=6425) by [Spacious Mind](The_Spacious_Mind "The Spacious Mind"), [Hiarcs Forum](Computer_Chess_Forums "Computer Chess Forums"), November 11, 2013 » Stockfish vs. [Tasc CM32 512K](ChessMachine "ChessMachine") [The King 2.2](The_King "The King")
* [Stockfish scaling](http://www.talkchess.com/forum/viewtopic.php?t=50083) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), November 15, 2013
* [Stockfish depth vs. others; challenge](http://www.talkchess.com/forum/viewtopic.php?t=50220) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), November 24, 2013 » [Depth](Depth "Depth")
* [Stockfish DD: a new official release](http://www.talkchess.com/forum/viewtopic.php?t=50275) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 29, 2013 » [TCEC Season 5](TCEC_Season_5 "TCEC Season 5"), dedicated to [Don Dailey](Don_Dailey "Don Dailey")
* [Stockfish Syzygy: how to interpret mates?](http://www.talkchess.com/forum/viewtopic.php?t=50296) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 01, 2013 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases"), [Mate Scores](Score#MateScores "Score")
* [Is SF DD greater efficiency would be null move pruning?](http://www.talkchess.com/forum/viewtopic.php?t=50587) by Jonathan Lee, [CCC](CCC "CCC"), December 22, 2013 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")


**2014**



* [Help me to test an idea for Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=50742) by Robert Tournevisse, [CCC](CCC "CCC"), January 03, 2014 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables"), [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Stockfish seems definitely the strongest engine](http://www.talkchess.com/forum/viewtopic.php?t=50989) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), January 21, 2014
* [Stockfish Mac app](http://www.talkchess.com/forum/viewtopic.php?t=50992) by [Daylen Yang](Daylen_Yang "Daylen Yang"), [CCC](CCC "CCC"), January 22, 2014 » [Macintosh](Macintosh "Macintosh")
* [Stockfish goes EGBB](http://www.talkchess.com/forum/viewtopic.php?t=51096) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [CCC](CCC "CCC"), January 29, 2014 » [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")
* [fixing the null move search "bug"](http://www.talkchess.com/forum/viewtopic.php?t=51129) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), February 01, 2014 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Disabling Null Move Pruning in Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=51291) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 15, 2014 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Threads-Test](http://www.talkchess.com/forum/viewtopic.php?t=51655) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), March 18, 2014 » [Thread](Thread "Thread"), [Parallel Search](Parallel_Search "Parallel Search")
* [Stockfish haswell optimized build](http://www.talkchess.com/forum/viewtopic.php?t=51879) by [Jean-Francois Romang](Jean-Francois_Romang "Jean-Francois Romang"), [CCC](CCC "CCC"), April 06, 2014 » [BMI2](BMI2 "BMI2")
* [Huge simplification](http://www.talkchess.com/forum/viewtopic.php?t=52117&start=1) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), April 25, 2014 » [Pawn Chain](Pawn_Chain "Pawn Chain")
* [Stockfish zero evals](http://www.talkchess.com/forum/viewtopic.php?t=52204) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), May 02, 2014
* [Threads-Test - SF, Zappa, Komodo - 1 vs. 2, 4, 8, 16 Threads](http://www.talkchess.com/forum/viewtopic.php?t=52219) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 04, 2014 » [Thread](Thread "Thread"), Stockfish, [Zappa](Zappa "Zappa"), [Komodo](Komodo "Komodo")
* [investigating why stockfish is strong idea](http://www.talkchess.com/forum/viewtopic.php?t=52231) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 05, 2014
* [Threads factor: Komodo, Houdini, Stockfish and Zappa](http://www.talkchess.com/forum/viewtopic.php?p=570955) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 17, 2014 » [Komodo](Komodo "Komodo"), [Houdini](Houdini "Houdini"), Stockfish, [Zappa](Zappa "Zappa")
* [Goodbye CLOP, hello SPSA](https://groups.google.com/d/msg/fishcooking/WNrxeXAJ6VI/ZkCnRv4I_qEJ) by [Gary Linscott](Gary_Linscott "Gary Linscott"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), May 17, 2014 » [CLOP](CLOP "CLOP"), [SPSA](SPSA "SPSA")
* [Stockfish 5](http://www.talkchess.com/forum/viewtopic.php?t=52487) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 31, 2014
* [Stockfish Status Report](http://www.talkchess.com/forum/viewtopic.php?t=52781) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), June 27, 2014
* [GM and Rybka vs. Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=53228) by Robert Maddox, [CCC](CCC "CCC"), August 09, 2014 » [GM+Rybka vs. Stockfish](Stockfish#Matches "Stockfish")
* [Nakamura vs Stockfish, public match 8/23](http://www.talkchess.com/forum/viewtopic.php?t=53315) by Jesse L, [CCC](CCC "CCC"), August 17, 2014
* [Using the Transposition Table for long searches](https://groups.google.com/d/msg/fishcooking/6nNXAQQAXOE/FXs2chqDargJ) by Theodr Elwurtz, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2014 » [Transposition Table](Transposition_Table "Transposition Table")
* [Rule of the square](https://groups.google.com/d/msg/fishcooking/T7OFWxD4LK8/pzurkRQNLjwJ) by [Mikael](Mikael_B%C3%A4ckman "Mikael Bäckman"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 24, 2014 » [Rule of the Square](Rule_of_the_Square "Rule of the Square")
* [Using the Stockfish position evaluation score to predict victory probability](https://chesscomputer.tumblr.com/post/98632536555/using-the-stockfish-position-evaluation-score-to/embed) by unavoidablegrain, [Tumblr](https://en.wikipedia.org/wiki/Tumblr), September 28, 2014 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [Threads test incl. Stockfish 5 and Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=53995) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 09, 2014
* [Threads test - Stockfish 5 against Komodo 8](http://www.talkchess.com/forum/viewtopic.php?t=54009) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), October 10, 2014 » [Thread](Thread "Thread"), [Parallel Search](Parallel_Search "Parallel Search"), Stockfish, [Komodo](Komodo "Komodo")
* [Stockfish and accurate PV](http://www.talkchess.com/forum/viewtopic.php?t=54750) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), December 25, 2014 » [Principal Variation](Principal_Variation "Principal Variation")
* [Stockfish 32-bit and hardware instructions on MSVC++](http://www.talkchess.com/forum/viewtopic.php?t=54798) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), December 30, 2014 » [BitScan](BitScan "BitScan"), [Population Count](Population_Count "Population Count")


### 2015 ...


* [Stockfish in Lozza UIs](http://www.talkchess.com/forum/viewtopic.php?t=54891) by [Colin Jenkins](Colin_Jenkins "Colin Jenkins"), [CCC](CCC "CCC"), January 07, 2015 » [Lozza](Lozza "Lozza"), [Stockfish-js](Stockfish-js "Stockfish-js") [[40]](#cite_note-40)
* [SF6 has been released](http://www.talkchess.com/forum/viewtopic.php?t=55122) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), January 27, 2015
* [Stockfish 6 is impressive in Behting study](http://www.talkchess.com/forum/viewtopic.php?t=55167) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 31, 2015 » [Behting Study](Behting_Study "Behting Study")
* [Stockfish with 16 threads - big news?](http://www.talkchess.com/forum/viewtopic.php?t=55352) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 15, 2015 » [Thread](Thread "Thread")


 [Explanation for non-expert?](http://www.talkchess.com/forum/viewtopic.php?t=55368) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 16, 2015 » [Parallel Search](Parallel_Search "Parallel Search")
* [Stockfish still scales poorly?](http://www.talkchess.com/forum/viewtopic.php?t=55402) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 20, 2015
* [Measuring SF idle time](http://www.talkchess.com/forum/viewtopic.php?t=55409) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 21, 2015
* [Better NPS scaling for Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=55494) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), February 27, 2015
* [Stockfish Questions](http://www.talkchess.com/forum/viewtopic.php?t=55510) by [Syed Fahad](Syed_Fahad "Syed Fahad"), [CCC](CCC "CCC"), February 28, 2015
* [Best Stockfish NPS scaling yet](http://www.talkchess.com/forum/viewtopic.php?t=55536) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), March 02, 2015
* [Stockfish contempt factor](http://www.talkchess.com/forum/viewtopic.php?t=55623) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), March 10, 2015 » [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Improving SF passer code](http://www.talkchess.com/forum/viewtopic.php?t=55792) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), March 26, 2015 » [Connected Passed Pawns](Connected_Passed_Pawns "Connected Passed Pawns")
* [Problem with SF6 and Syzygy TB](http://www.talkchess.com/forum/viewtopic.php?t=55846) by Forrest Hoch, [CCC](CCC "CCC"), April 01, 2015 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Empirical results with Lazy SMP, YBWC, DTS](http://www.talkchess.com/forum/viewtopic.php?t=56019) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), April 16, 2015 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [YBWC](Young_Brothers_Wait_Concept "Young Brothers Wait Concept"), [DTS](Dynamic_Tree_Splitting "Dynamic Tree Splitting")
* [The effective speedup from 1 to 8 cpus for SF and Komodo](http://www.talkchess.com/forum/viewtopic.php?t=56543) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), May 31, 2015 » [Parallel Search](Parallel_Search "Parallel Search"), [Komodo](Komodo "Komodo")
* [New Stockfish with Lazy\_SMP, but what about the TC bug ?](http://www.talkchess.com/forum/viewtopic.php?t=58056) by [Ernest Bonnem](index.php?title=Ernest_Bonnem&action=edit&redlink=1 "Ernest Bonnem (page does not exist)"), [CCC](CCC "CCC"), October 26, 2015 » [Parallel Search](Parallel_Search "Parallel Search"), [TCEC Season 8](TCEC_Season_8 "TCEC Season 8")
* [Binary for TCEC superfinal](https://goo.gl/QLcPAF) by Kiran Panditrao, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 30, 2015 » [TCEC Season 8](TCEC_Season_8 "TCEC Season 8")
* [SF binaries for TCEC superfinal](http://www.talkchess.com/forum/viewtopic.php?t=58103) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 31, 2015
* [Stockfish dev 091115 for ANDROID](http://www.talkchess.com/forum/viewtopic.php?t=58210) by Nathanael Russell, [CCC](CCC "CCC"), November 09, 2015 » [Android](Android "Android")
* [Stockfish now benefits from hyperthreading](http://www.talkchess.com/forum/viewtopic.php?t=58236) by [Dmitri Gusev](Dmitri_Gusev "Dmitri Gusev"), [CCC](CCC "CCC"), November 12, 2015 » [Thread](Thread "Thread")
* [Stockfish 7 beta 1](http://www.talkchess.com/forum/viewtopic.php?t=58703) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), December 27, 2015
* [Another GHI example in SF (maybe)](http://www.open-chess.org/viewtopic.php?f=5&t=2942) by [BB+](Mark_Watkins "Mark Watkins"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), December 30, 2015 » [Graph History Interaction](Graph_History_Interaction "Graph History Interaction")


**2016**



* [Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58779) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), January 02, 2016
* [Threads test incl. Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58887) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 11, 2016 » [Thread](Thread "Thread"), [Parallel Search](Parallel_Search "Parallel Search")
* [Stockfish 7 progress](http://www.talkchess.com/forum/viewtopic.php?t=58935) by Carl Lumma, [CCC](CCC "CCC"), January 16, 2016
* [Oddity around depths 7-8 with Stockfish 6 & 7](http://www.talkchess.com/forum/viewtopic.php?t=58990) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [CCC](CCC "CCC"), January 21, 2016
* [Stockfish 7 and partial 6 piece syzygy problem?](http://www.talkchess.com/forum/viewtopic.php?t=59407) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 01, 2016


 [Re: Stockfish 7 and partial 6 piece syzygy problem?](http://www.talkchess.com/forum/viewtopic.php?t=59407&start=12) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 01, 2016
* [Computer Chess Progress: Stockfish 7 vs Ruffian 1.0.5](http://www.talkchess.com/forum/viewtopic.php?t=59543) by [Martin Fierz](Martin_Fierz "Martin Fierz"), [CCC](CCC "CCC"), March 17, 2016 » [Ruffian](Ruffian "Ruffian")
* [Natural TB](http://www.talkchess.com/forum/viewtopic.php?t=60312) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 29, 2016 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Stockfish eval output](http://www.talkchess.com/forum/viewtopic.php?t=61250) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), August 27, 2016 » [Wrong Color Bishop and Rook Pawn](Wrong_Color_Bishop_and_Rook_Pawn "Wrong Color Bishop and Rook Pawn")
* [Re: Beginner's guide to graphical profiling](http://www.talkchess.com/forum/viewtopic.php?t=61373&start=2) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), September 10, 2016 » [Profiling](index.php?title=Profiling&action=edit&redlink=1 "Profiling (page does not exist)")
* [ELO inflation ha ha ha](http://www.talkchess.com/forum/viewtopic.php?t=61444) by [Henk van den Belt](index.php?title=Henk_van_den_Belt&action=edit&redlink=1 "Henk van den Belt (page does not exist)"), [CCC](CCC "CCC"), September 16, 2016 » [Delphil](Delphil "Delphil"), [Match Statistics](Match_Statistics "Match Statistics"), [Playing Strength](Playing_Strength "Playing Strength"), [TCEC Season 9](TCEC_Season_9 "TCEC Season 9") [[41]](#cite_note-41)
* [pin-aware see](https://groups.google.com/d/msg/fishcooking/S_4E_Xs5HaE/mS3VTnuEFgAJ) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 14, 2016 » [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm"), [Pin](Pin "Pin")
* [Illegal moves in SEE](https://groups.google.com/d/msg/fishcooking/9mcmjnyqbAQ/S6mDA0QsAAAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2016 » [SEE - The Swap Algorithm](SEE_-_The_Swap_Algorithm "SEE - The Swap Algorithm")
* [Stockfish underpromotes much more often than Komodo](http://www.talkchess.com/forum/viewtopic.php?t=61601) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), October 05, 2016 » [Komodo](Komodo "Komodo"), [Match Statistics](Match_Statistics "Match Statistics"), [Promotions](Promotions "Promotions")
* [couple of questions about stockfish code ?](http://www.talkchess.com/forum/viewtopic.php?t=61850) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), October 26, 2016 » [SIMD and SWAR Techniques](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques"), [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Stockfish 8](https://groups.google.com/d/msg/fishcooking/LCoojE9O5jU/h6xgvg2EBgAJ) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 01, 2016
* [Stockfish 8 official](http://www.talkchess.com/forum/viewtopic.php?t=61924) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 01, 2016
* [NUMA test compilation](https://groups.google.com/d/msg/fishcooking/7hHC075ZnnM/IaITCiLaBwAJ) by Joachim Müller, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 05, 2016 » [NUMA](NUMA "NUMA")
* [Stockfish 8 - Double time control vs. 2 threads](http://www.talkchess.com/forum/viewtopic.php?t=62146) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), November 15, 2016 » [Doubling TC](Match_Statistics#DoublingTC "Match Statistics"), [Diminishing Returns](Depth#DiminishingReturns "Depth"), [Playing Strength](Playing_Strength "Playing Strength"), [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Stockfish benchmark data](http://www.open-chess.org/viewtopic.php?f=3&t=3044) by [Adam Hair](Adam_Hair "Adam Hair"), [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), November 27, 2016
* [The new chess rules (5-fold repetition and 75-move draw)](https://groups.google.com/d/msg/fishcooking/M2bkzC3MuFQ/N3pHK4DcAgAJ) by [Lyudmil Antonov](Lyudmil_Antonov "Lyudmil Antonov"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2016 » [Repetitions](Repetitions "Repetitions"), [Fifty-move Rule](Fifty-move_Rule "Fifty-move Rule")
* [Scoutfish: powerful chess query tool](http://www.talkchess.com/forum/viewtopic.php?t=62452) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), December 11, 2016 » [Databases](Databases "Databases"), [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"), [Scoutfish](index.php?title=Scoutfish&action=edit&redlink=1 "Scoutfish (page does not exist)")


**2017**



* [SF Progression since Fishtest inception](http://www.talkchess.com/forum/viewtopic.php?t=62822) by [Adam Hair](Adam_Hair "Adam Hair"), [CCC](CCC "CCC"), January 14, 2017 » [Fishtest](Stockfish#Fishtest "Stockfish")
* [Re: Chessprogams with the most chessknowing](http://www.talkchess.com/forum/viewtopic.php?t=54697&start=50) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), February 19, 2017 » [Search versus Evaluation](Knowledge#SearchVersusEvaluation "Knowledge")
* [Stockfish bench in i486 & Pentium 75mhz !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=63857) by hammerklavier, [CCC](CCC "CCC"), April 29, 2017


 [Re: Stockfish bench ...](#i486Re)
* [Symmetric multiprocessing (SMP) scaling - SF8 and K10.4](http://www.talkchess.com/forum/viewtopic.php?t=63903) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 05, 2017 » [Lazy SMP](Lazy_SMP "Lazy SMP"), [Komodo](Komodo "Komodo")
* [Symmetric multiprocessing (SMP) scaling - SF8 Contempt=10](http://www.talkchess.com/forum/viewtopic.php?t=63967) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), May 13, 2017 » [SMP](SMP "SMP"), [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Stockfish version with hash saving capability](http://www.talkchess.com/forum/viewtopic.php?t=64720) by [Daniel José Queraltó](Daniel_Jos%C3%A9_Queralt%C3%B3 "Daniel José Queraltó"), [CCC](CCC "CCC"), July 25, 2017 » [Persistent Hash Table](Persistent_Hash_Table "Persistent Hash Table")
* [Natural TB (take 2)](http://www.talkchess.com/forum/viewtopic.php?t=60312&start=240) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), August 22, 2017 » [Syzygy Bases](Syzygy_Bases "Syzygy Bases")
* [Approximating Stockfish's Evaluation by PSQTs](http://www.talkchess.com/forum/viewtopic.php?t=64972) by [Thomas Dybdahl Ahle](Thomas_Dybdahl_Ahle "Thomas Dybdahl Ahle"), [CCC](CCC "CCC"), August 23, 2017 » [Regression](Automated_Tuning#Regression "Automated Tuning"), [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Stockfish no progress in 2month and half , why ?](http://www.talkchess.com/forum/viewtopic.php?t=65017) by Jean Baptiste, [CCC](CCC "CCC"), August 28, 2017
* [Stockfish testing at STC and LTC: one question](http://www.talkchess.com/forum/viewtopic.php?t=65216) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 19, 2017
* [Scaling from FGRL results with top 3 engines](http://www.talkchess.com/forum/viewtopic.php?t=65288) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), September 26, 2017 » [FGRL](FGRL "FGRL"), [Houdini](Houdini "Houdini"), [Komodo](Komodo "Komodo")
* [AlphaZero vs Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=65919) by Bigler, [CCC](CCC "CCC"), December 06, 2017 » [AlphaZero vs. Stockfish](AlphaZero#StockfishMatch "AlphaZero")
* [A branch to test the Monte Carlo algorithm in Stockfish](https://groups.google.com/forum/#!topic/fishcooking/AE4EgWQ20dY) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 06, 2017 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search"), [AlphaZero](AlphaZero "AlphaZero")
* [Reactions about AlphaZero from top GMs...](http://www.talkchess.com/forum/viewtopic.php?t=65934) by [Norman Schmidt](Norman_Schmidt "Norman Schmidt"), [CCC](CCC "CCC"), December 08, 2017 » [AlphaZero: Reactions From Top GMs, Stockfish Author](AlphaZero#Reactions "AlphaZero"), [Tord Romstad](Tord_Romstad "Tord Romstad")
* [MCTS wrapper for StockFish](https://groups.google.com/d/msg/fishcooking/rMCfc8zMerc/F01WuNtDCgAJ) by [Jonathan Baxter](Jonathan_Baxter "Jonathan Baxter"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), December 19, 2017 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")


**2018**



* [Stockfish 8 - Initial position until depth 59](http://www.talkchess.com/forum/viewtopic.php?t=66340) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), January 16, 2018 » [Initial Position](Initial_Position "Initial Position")
* [New Stockfish contempt](http://www.talkchess.com/forum/viewtopic.php?t=66444) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), January 29, 2018 » [Contempt Factor](Contempt_Factor "Contempt Factor")
* [Contributors in the last two years](https://groups.google.com/d/msg/fishcooking/_FW_RIowarw/y1e-qMEXAgAJ) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), Jnauary 30, 2018
* [Stockfish 9](http://www.talkchess.com/forum/viewtopic.php?t=66470) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), February 01, 2018
* [Elo measurement of contempt in SF in self-play](http://www.talkchess.com/forum/viewtopic.php?t=66793) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), March 10, 2018 » [Contempt](Contempt_Factor "Contempt Factor"), [Playing Strength](Playing_Strength "Playing Strength")
* [Stockfish 180113 - Initial position until depth 65](http://www.talkchess.com/forum/viewtopic.php?t=66935) by [Andreas Strangmüller](Andreas_Strangm%C3%BCller "Andreas Strangmüller"), [CCC](CCC "CCC"), March 27, 2018 » [Initial Position](Initial_Position "Initial Position")
* [Stockfish and serious hardware: 384 threads](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67932) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), July 08, 2018 » [Thread](Thread "Thread")
* [Stockfish 10 - Call for Binaries](https://groups.google.com/d/msg/fishcooking/kJ6vNKyp6h8/zwRnc-i7CwAJ) by [Daylen Yang](Daylen_Yang "Daylen Yang"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), November 29, 2018
* [Re: piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364&start=12) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 26, 2018 » [Piece-Lists](Piece-Lists "Piece-Lists"), [asmFish](AsmFish "AsmFish")


**2019**



* [Re: What's the best Lazy SMP logic?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69507&start=1) by [Sven Schüle](Sven_Sch%C3%BCle "Sven Schüle"), [CCC](CCC "CCC"), January 06, 2019 » [Lazy SMP](Lazy_SMP "Lazy SMP") in Stockfish
* [Training the trainer: how is it done for Stockfish?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70069) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), March 01, 2019 » [Monte-Carlo Tree Search](Monte-Carlo_Tree_Search "Monte-Carlo Tree Search")
* [Some NUMA data for Stockfish-dev and Cfish-dev](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71027) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), June 17, 2019 » [NUMA](NUMA "NUMA"), [CFish](CFish "CFish")
* [Why does stockfish randomise draw evaluations?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71707) by [Vincent Tang](Vincent_Tang "Vincent Tang"), [CCC](CCC "CCC"), September 01, 2019 » [Draw](Draw "Draw"), [Draw Evaluation](Draw_Evaluation "Draw Evaluation"), [Draw Score](Score#DrawScore "Score"), [Search with Random Leaf Values](Search_with_Random_Leaf_Values "Search with Random Leaf Values")
* [Help needed testing vectorized Stockfish pawns.cpp...](https://groups.google.com/d/msg/fishcooking/xGM9K7wd5rM/pmx2MVX-BwAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 23, 2019
* [mg vs eg eval](https://groups.google.com/d/msg/fishcooking/znU1a7aZ2XI/yJDFtOQnAwAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 06, 2019 » [Middlegame](Middlegame "Middlegame"), [Endgame](Endgame "Endgame"), [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Stockfish contempt testing](https://groups.google.com/d/msg/fishcooking/liMe2Ho53j8/GP9l07hSBAAJ) by Leonardo Ljubičić, [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 29, 2019 » [Contempt](Contempt_Factor "Contempt Factor")
* [some questions about singular search in Stockfish](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72231) by [Jon Dart](Jon_Dart "Jon Dart"), [CCC](CCC "CCC"), November 01, 2019 » [Singular Extensions](Singular_Extensions "Singular Extensions")
* ["stat score bonus" in stockfish](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72232) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), November 01, 2019
* [Stockfish 10 was released 29.11.2018](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72480) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), December 01, 2019


### 2020 ...


* [lazy smp behaviour of stockfish](https://groups.google.com/d/msg/fishcooking/9X3lDH83tlk/DtRtuFMOCAAJ) by [Daniel Shawul](Daniel_Shawul "Daniel Shawul"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 05, 2020 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [The Stockfish of shogi](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72754) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman"), [CCC](CCC "CCC"), January 07, 2020 » [NNUE](NNUE "NNUE"), [Shogi](Shogi "Shogi")
* [Stockfish 11](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72837) by [Stephane Nicolet](Stephane_Nicolet "Stephane Nicolet"), [CCC](CCC "CCC"), January 18, 2020
* [Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962) by Deberger, [CCC](CCC "CCC"), February 01, 2020


 [Re: Stockfish Reverts 5 Recent Patches](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72962&start=6) by [Michel Van den Bergh](Michel_Van_den_Bergh "Michel Van den Bergh"), [CCC](CCC "CCC"), February 02, 2020 » [SPRT](Match_Statistics#SPRT "Match Statistics")
* [Stockfish and latest +6 ELO patch!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73273) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 05, 2020 » [Distance](Distance "Distance"), [Space-Time Tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff") [[42]](#cite_note-42)
* [Null move](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73753) by [Robert Pope](Robert_Pope "Robert Pope"), [CCC](CCC "CCC"), April 24, 2020 » [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Stockfish\_dev is probably stronger than Sargon 1978 v1.00](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74037) by [Kai Laskos](Kai_Laskos "Kai Laskos"), [CCC](CCC "CCC"), May 29, 2020 » [Sargon](Sargon "Sargon")
* [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020 » [NNUE](NNUE "NNUE"), [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Stockfish has included WDL stats in engine output](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=74339) by Deberger, [CCC](CCC "CCC"), July 02, 2020 » [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo")
* [stockfishNNUE vs others (TCEC 18 bonus)](https://groups.google.com/d/msg/fishcooking/EBKQSrb9I08/5xasTnnSCAAJ) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2020
* [Can the sardine! NNUE clobbers SF](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74484) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), July 16, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [The most stupid idea by the Stockfish Team](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74933) by Damir, [CCC](CCC "CCC"), August 30, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Stockfish 12](https://groups.google.com/d/msg/fishcooking/TJHsiI61yQ4/liQoZ-AzAgAJ) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), September 02, 2020
* [Stockfish 12 is released today!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74974) by Nay Lin Tun, [CCC](CCC "CCC"), September 02, 2020
* [Stockfish 12 has arrived!](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74978) by daniel71, [CCC](CCC "CCC"), September 02, 2020
* [SF NNUE/Classical](https://groups.google.com/d/msg/fishcooking/yjh1YOxy7nw/rJA6u1ODAAAJ) by [Fauzi](Fauzi_Akram_Dabat "Fauzi Akram Dabat"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), October 05, 2020 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Re: Stockfish bench in i486 & Pentium 75mhz !](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=63857&start=14) by [Vincent Lejeune](index.php?title=Vincent_Lejeune&action=edit&redlink=1 "Vincent Lejeune (page does not exist)"), [CCC](CCC "CCC"), October 11, 2020 » [Stockfish bench ...](#i486)
* [Re: Raspberry Pi 4 compiled chess engines](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75841&start=8) by [Rasmus Althoff](Rasmus_Althoff "Rasmus Althoff"), [CCC](CCC "CCC"), November 16, 2020 » [Raspberry Pi](Raspberry_Pi "Raspberry Pi")


**2021**



* [Shouldn't positional attributes drive SF's NNUE input features (rather than king position)?](https://groups.google.com/g/fishcooking/c/cad1MGSdpU4/m/Ury4iBqSBgAJ) by [Nick Pelling](Nick_Pelling "Nick Pelling"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), January 10, 2021 » [Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE")
* [Stockfish 13](https://groups.google.com/g/fishcooking/c/AzYDbbv-Coo) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), [FishCooking](Computer_Chess_Forums "Computer Chess Forums"), February 19, 2021
* [Stockfish 13 merged on github](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76639) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), February 19, 2021
* [Setting up Stockfish on a server](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76977) by Jon12345, [CCC](CCC "CCC"), March 29, 2021 » [Chess Server](Chess_Server "Chess Server")
* [Joking FTW, Seriously](https://lczero.org/blog/2021/04/joking-ftw-seriously/) by borg, [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), April 25, 2021
* [Stockfish with new NNUE architecture and bigger net released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77344) by [Stefan Pohl](index.php?title=Stefan_Pohl&action=edit&redlink=1 "Stefan Pohl (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 [[43]](#cite_note-43) [[44]](#cite_note-44)
* [The importance of open data](https://lczero.org/blog/2021/06/the-importance-of-open-data/) by borg , [LCZero blog](Leela_Chess_Zero "Leela Chess Zero"), June 15, 2021
* [will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503) by Wilson, [CCC](CCC "CCC"), June 17, 2021 » [TCEC Season 21](TCEC_Season_21 "TCEC Season 21")


 [Re: will Tcec allow Stockfish with a Leela net to play?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77503&start=55) by [Connor McMonigle](Connor_McMonigle "Connor McMonigle"), [CCC](CCC "CCC"), June 17, 2021
* [Stockfish 14 release round the corner](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77599) by Prasanna Bandihole, [CCC](CCC "CCC"), July 02, 2021
* [Before things become more messy than they already are](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77602) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), July 02, 2021
* [Stockfish 14 has been released](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77605) by Madeleine Birchfield, [CCC](CCC "CCC"), July 02, 2021
* [Stockfish: Our lawsuit against ChessBase](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=77762) by Kurt Lanc, [CCC](CCC "CCC"), July 20, 2021
* [The Great Stockfish NPS Debate](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=78030) by Dietrich Kappe, [CCC](CCC "CCC"), August 27, 2021


**2022**



* [Stockfish search](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79588) by Werewolf, [CCC](CCC "CCC"), March 26, 2022 » [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Stockfish 15 is ready](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79713) by Mehmet Karaman, [CCC](CCC "CCC"), April 19, 2022
* [Stockfish 15's Immortal Game?](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=79793) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), May 01, 2022
* [Are tablebases useless for Stockfish15?](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=80608) by [Jouni](index.php?title=Jouni&action=edit&redlink=1 "Jouni (page does not exist)"), [CCC](CCC "CCC"), September 02, 2022
* [Stockfish 15.1 is ready](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=81105) by [Mehmet Karaman](index.php?title=Mehmet_Karaman&action=edit&redlink=1 "Mehmet Karaman (page does not exist)"), [CCC](CCC "CCC"), December 05, 2022
* [SF branching factor](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=81108) by [Jouni](index.php?title=Jouni&action=edit&redlink=1 "Jouni (page does not exist)"), [CCC](CCC "CCC"), December 05, 2022


## Blog Posts


* [Stockfish Blog](https://blog.stockfishchess.org/)


### 2014


* [One chess champion per laptop](http://tech.mit.edu/V133/N62/chess.html) by [Roberto Perez-Franco](http://www.mit.edu/~roberto/), [MIT's](Massachusetts_Institute_of_Technology "Massachusetts Institute of Technology") [The Tech](https://en.wikipedia.org/wiki/The_Tech_%28newspaper%29), January 15, 2014 » [TCEC Season 5](TCEC_Season_5 "TCEC Season 5")


### 2015 ...


* [And then there were two](http://en.chessbase.com/post/john-hartmann-and-then-there-were-two) by [John Hartmann](http://en.chessbase.com/author/john-hartmann), [ChessBase News](ChessBase "ChessBase"), June 09, 2015 » [Komodo](Komodo "Komodo"), Stockfish
* [Depth of Satisficing](https://rjlipton.wordpress.com/2015/10/06/depth-of-satisficing/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), October 06, 2015 » [Depth](Depth "Depth"), [Match Statistics](Match_Statistics "Match Statistics"), [Pawn Advantage, Win Percentage, and Elo](Pawn_Advantage,_Win_Percentage,_and_Elo "Pawn Advantage, Win Percentage, and Elo"), Stockfish, [Komodo](Komodo "Komodo") [[45]](#cite_note-45)
* [A Chess Firewall at Zero?](https://rjlipton.wordpress.com/2016/01/21/a-chess-firewall-at-zero/) by [Ken Regan](Kenneth_W._Regan "Kenneth W. Regan"), [Gödel's Lost Letter and P=NP](https://rjlipton.wordpress.com/), January 21, 2016
* [Stockfish 8](https://stockfishchess.org/blog/2016/stockfish-8/), November 01, 2016
* [Stockfish 9](https://stockfishchess.org/blog/2018/stockfish-9/), February 09, 2018
* [Stockfish 10](https://stockfishchess.org/blog/2018/stockfish-10/), December 01, 2018


### 2020 ...


* [Stockfish 11](https://stockfishchess.org/blog/2020/stockfish-11/), The Stockfish Team, January 15, 2020
* [Introducing NNUE Evaluation](https://stockfishchess.org/blog/2020/introducing-nnue-evaluation/), August 07, 2020
* [Stockfish 12](https://stockfishchess.org/blog/2020/stockfish-12/), The Stockfish Team, September 02, 2020
* [Stockfish 13](https://stockfishchess.org/blog/2021/stockfish-13/), The Stockfish Team, February 19, 2021
* [Stockfish 14](https://stockfishchess.org/blog/2021/stockfish-14/), The Stockfish Team, July 02, 2021
* [Our lawsuit against ChessBase](https://stockfishchess.org/blog/2021/our-lawsuit-against-chessbase/), The Stockfish Team, July 20, 2021 » [ChessBase](ChessBase "ChessBase"), [Fat Fritz 2](Fat_Fritz#Fat_Fritz_2 "Fat Fritz"), [Houdini 6](Houdini#Stockfish "Houdini")
* [Stockfish 14.1](https://stockfishchess.org/blog/2021/stockfish-14-1/), The Stockfish Team, October 28, 2021


## External Links


### Chess Engine


* [Stockfish - Open Source Chess Engine](https://stockfishchess.org/)
* [official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish)
* [GitHub - nodchip/Stockfish: UCI chess engine](https://github.com/nodchip/Stockfish) ([Stockfish NNUE](Stockfish_NNUE "Stockfish NNUE") by [Nodchip](Hisayori_Noda "Hisayori Noda"))
* [zamar · GitHub](https://github.com/zamar) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski")
* [NCM Stockfish Dev Builds](https://nextchessmove.com/dev-builds)
* [Stockfish Development Versions](https://abrok.eu/stockfish/) hosted by [Roman Korba](Roman_Korba "Roman Korba")
* [Stockfish (chess) from Wikipedia](https://en.wikipedia.org/wiki/Stockfish_%28chess%29)


### Issues


* [Issues · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues)
* [NNUE merge · Issue #2823 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/2823) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), July 25, 2020 [[46]](#cite_note-46)
* [NNUE ideas and discussion (post-merge) Issue #2915 official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/2915) by [Joost VandeVondele](Joost_VandeVondele "Joost VandeVondele"), August 06, 2020
* [NNUE eval rotate vs mirror · Issue #3021 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/issues/3021) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), August 18, 2020


### Pull Requests


* [Pull requests · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pulls)
* [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474) by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk")


### Testing


* [Get Involved - Stockfish - Powerful Open Source Chess Engine](https://stockfishchess.org/get-involved/)
* [Stockfish Testing Framework](https://tests.stockfishchess.org/tests) » [Fishtest](Stockfish#Fishtest "Stockfish")
* [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/) » [Stockfish Evaluation Guide](Stockfish#EvaluationGuide "Stockfish")


 [Stockfish Evaluation Guide - NNUE](https://hxim.github.io/Stockfish-Evaluation-Guide/?p=nnue)
* [GitHub - glinscott/fishtest: Stockfish testing](https://github.com/glinscott/fishtest)


 [Creating my first test · glinscott/fishtest Wiki · GitHub](https://github.com/glinscott/fishtest/wiki/Creating-my-first-test)
 [Fishtest mathematics · glinscott/fishtest Wiki · GitHub](https://github.com/glinscott/fishtest/wiki/Fishtest-mathematics)
* [SPSA Tuner for Stockfish Chess Engine](https://github.com/zamar/spsa) » [SPSA](SPSA "SPSA")
* [FishCooking - Google Groups](https://groups.google.com/forum/#!forum/fishcooking) a discussion group for developers and testers of Stockfish chess engine
* [Adam's Computer Chess Pages: Stockfish Progression](http://adamsccpages.blogspot.com/p/sf-framework-history.html) by [Adam Hair](Adam_Hair "Adam Hair") » [Fishtest](Stockfish#Fishtest "Stockfish")


### Rating Lists


* [Stockfish](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Stockfish&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) from [CCRL 40/15](CCRL "CCRL")
* [Stockfish](http://computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Stockfish&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL Blitz](CCRL "CCRL")


### Matches


* [Can a GM and Rybka beat Stockfish?](http://www.chess.com/article/view/how-rybka-and-i-tried-to-beat-the-strongest-chess-computer-in-the-world) by GM [Daniel Naroditsky](https://en.wikipedia.org/wiki/Daniel_Naroditsky), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 08, 2014 » [GM+Rybka vs. Stockfish](Stockfish#Matches "Stockfish")
* [Stockfish Outlasts "Rybkamura"](http://www.chess.com/news/stockfish-outlasts-nakamura-3634) by [FM Mike Klein](http://www.chess.com/article/view/chesscom-player-profiles-fm-mikeklein), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 24, 2014
* [AlphaZero: Reactions From Top GMs, Stockfish Author](https://www.chess.com/news/view/alphazero-reactions-from-top-gms-stockfish-author) by [Peter Doggers](Peter_Doggers "Peter Doggers"), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), December 08, 2017 » [AlphaZero vs. Stockfish](AlphaZero#StockfishMatch "AlphaZero")


### Interviews


* [Computerschach, Interview with Tord Romstad (Norway), Joona Kiiski (Finland) and Marco Costalba (Italy)](http://www.schach-welt.de/schach/computerschach/interviews/romstad-kiiski-costalba-eng) by [Frank Quisinsky](Frank_Quisinsky "Frank Quisinsky"), March 29, 2010
* [Stockfish 4 to play in the new season of TCEC | Chessdom - Short interview with the Stockfish team](http://www.chessdom.com/stockfish-4-to-play-in-the-new-season-of-tcec/), August 22, 2013 » [TCEC](TCEC "TCEC"), [TCEC Season 5](TCEC_Season_5 "TCEC Season 5")


### Videos


* [How do modern chess engines work? | Video](Daylen_Yang#Video "Daylen Yang"), Talk by [Daylen Yang](Daylen_Yang "Daylen Yang"), [TNG | Big Techday 8](http://www.tngtech.com/tng-ueber-uns/bigtechday/big-techday-8.html), June 12, 2015
* [Parallelism and Selectivity in Game Tree Search | Video](Tord_Romstad#Video "Tord Romstad"), Talk by [Tord Romstad](Tord_Romstad "Tord Romstad"), [TNG | Big Techday 8](http://www.tngtech.com/tng-ueber-uns/bigtechday/big-techday-8.html), June 12, 2015
* [How Modern Chess Programs Work | Video](Tord_Romstad#Video "Tord Romstad") by [Tord Romstad](Tord_Romstad "Tord Romstad"), [flatMap(Oslo)](http://2017.flatmap.no/talks/romstad/), May 02, 2017


### Misc


* [Stockfish from Wikipedia](https://en.wikipedia.org/wiki/Stockfish)
* [Lofoten Stockfish Museum from Wikipedia](https://en.wikipedia.org/wiki/Lofoten_Stockfish_Museum)
* [Postcards from the Lofoten Islands](https://ruthhorowitz.wordpress.com/2012/05/29/postcards-from-the-lofoten-islands/) from [Giving Up The Ghost](https://ruthhorowitz.wordpress.com/), May 29, 2012 » Stockfish and [Gulls](Gull "Gull")


## References


1. [↑](#cite_ref-1) The Stockfish icon was designed by [Klein Maetschke](http://iamkle.in/), [About - Stockfish](https://stockfishchess.org/about/)
2. [↑](#cite_ref-2) [Stockfish - Open Source Chess Engine](https://stockfishchess.org/), The Stockfish 12 icon was designed by [Klein Maetschke](http://iamkle.in/), [About - Stockfish](https://stockfishchess.org/about/)
3. [↑](#cite_ref-3) [Stockfish 7](http://www.talkchess.com/forum/viewtopic.php?t=58779) by [Joona Kiiski](Joona_Kiiski "Joona Kiiski"), [CCC](CCC "CCC"), January 02, 2016
4. [↑](#cite_ref-4) [Stockfish 1.0](http://www.talkchess.com/forum/viewtopic.php?t=24675) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), November 02, 2008
5. [↑](#cite_ref-5) [Re: Smaug: a new chess engine based on glaurung](http://www.talkchess.com/forum/viewtopic.php?t=26971&start=1) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), March 12, 2009
6. [↑](#cite_ref-6) [David Silver](David_Silver "David Silver"), [Thomas Hubert](Thomas_Hubert "Thomas Hubert"), [Julian Schrittwieser](Julian_Schrittwieser "Julian Schrittwieser"), [Ioannis Antonoglou](Ioannis_Antonoglou "Ioannis Antonoglou"), [Matthew Lai](Matthew_Lai "Matthew Lai"), [Arthur Guez](Arthur_Guez "Arthur Guez"), [Marc Lanctot](Marc_Lanctot "Marc Lanctot"), [Laurent Sifre](Laurent_Sifre "Laurent Sifre"), [Dharshan Kumaran](Dharshan_Kumaran "Dharshan Kumaran"), [Thore Graepel](Thore_Graepel "Thore Graepel"), [Timothy Lillicrap](Timothy_Lillicrap "Timothy Lillicrap"), [Karen Simonyan](Karen_Simonyan "Karen Simonyan"), [Demis Hassabis](Demis_Hassabis "Demis Hassabis") (**2017**). *Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm*. [arXiv:1712.01815](https://arxiv.org/abs/1712.01815)
7. [↑](#cite_ref-7) [Stockfish on github](http://www.talkchess.com/forum/viewtopic.php?t=40610) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), October 02, 2011
8. [↑](#cite_ref-8) [Stockfish NN release (NNUE)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74059) by [Henk Drost](index.php?title=Henk_Drost&action=edit&redlink=1 "Henk Drost (page does not exist)"), [CCC](CCC "CCC"), May 31, 2020
9. [↑](#cite_ref-9) [Stockfish 12](https://stockfishchess.org/blog/2020/stockfish-12/), The Stockfish Team, [Stockfish Blog](https://blog.stockfishchess.org/), September 02, 2020
10. [↑](#cite_ref-10) [Stockfish 13](https://stockfishchess.org/blog/2021/stockfish-13/), The Stockfish Team, February 19, 2021
11. [↑](#cite_ref-11) [Stockfish 14](https://stockfishchess.org/blog/2021/stockfish-14/), The Stockfish Team, July 02, 2021
12. [↑](#cite_ref-12) [GitHub - Stockfish commit, Remove classical evaluation](https://github.com/official-stockfish/Stockfish/commit/af110e02ec96cdb46cf84c68252a1da15a902395)
13. [↑](#cite_ref-13) [About - Stockfish](https://stockfishchess.org/about/)
14. [↑](#cite_ref-14) [glinscott/fishtest · GitHub](https://github.com/glinscott/fishtest)
15. [↑](#cite_ref-15) [Get Involved - Stockfish - Powerful Open Source Chess Engine](http://stockfishchess.org/get-involved/)
16. [↑](#cite_ref-16) [Fishtest Distributed Testing Framework](http://www.talkchess.com/forum/viewtopic.php?t=47885) by [Marco Costalba](Marco_Costalba "Marco Costalba"), [CCC](CCC "CCC"), May 01, 2013
17. [↑](#cite_ref-17) [The Pyramid Web Framework — The Pyramid Web Framework v1.5](http://docs.pylonsproject.org/projects/pyramid/en/latest/)
18. [↑](#cite_ref-18) [Stockfish Testing Framework - Users](http://tests.stockfishchess.org/users)
19. [↑](#cite_ref-19) [Stockfish Testing Framework](http://tests.stockfishchess.org/tests)
20. [↑](#cite_ref-20) [Adam's Computer Chess Pages: Stockfish Progression](http://adamsccpages.blogspot.com/p/sf-framework-history.html) by [Adam Hair](Adam_Hair "Adam Hair")
21. [↑](#cite_ref-21) [Re: How far away are we from deep learning Stockfish, Komodo](http://www.talkchess.com/forum/viewtopic.php?t=64025&start=27) by [Gary](Gary_Linscott "Gary Linscott"), [CCC](CCC "CCC"), May 21, 2017
22. [↑](#cite_ref-22) [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/)
23. [↑](#cite_ref-23) [Stockfish Evaluation Guide - NNUE](https://hxim.github.io/Stockfish-Evaluation-Guide/?p=nnue)
24. [↑](#cite_ref-24) [Can a GM and Rybka beat Stockfish?](http://www.chess.com/article/view/how-rybka-and-i-tried-to-beat-the-strongest-chess-computer-in-the-world) by GM [Daniel Naroditsky](https://en.wikipedia.org/wiki/Daniel_Naroditsky), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 08, 2014
25. [↑](#cite_ref-25) [GM and Rybka vs. Stockfish](http://www.talkchess.com/forum/viewtopic.php?t=53228) by Robert Maddox, [CCC](CCC "CCC"), August 09, 2014
26. [↑](#cite_ref-26) [Nakamura vs Stockfish, public match 8/23](http://www.talkchess.com/forum/viewtopic.php?t=53315) by Jesse L, [CCC](CCC "CCC"), August 17, 2014
27. [↑](#cite_ref-27) [Stockfish Outlasts "Rybkamura"](http://www.chess.com/news/stockfish-outlasts-nakamura-3634) by [FM Mike Klein](http://www.chess.com/article/view/chesscom-player-profiles-fm-mikeklein), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)"), August 24, 2014
28. [↑](#cite_ref-28) if not mentioned otherwise, based on the sources of Stockfish 6
29. [↑](#cite_ref-29) [Ryzen and BMI2: Strange behavior and high latencies](https://www.reddit.com/r/Amd/comments/60i6er/ryzen_and_bmi2_strange_behavior_and_high_latencies/) by DonnieTinyHands, [Reddit](https://en.wikipedia.org/wiki/Reddit), March 20, 2017
30. [↑](#cite_ref-30) [Stockfish/position.h at sf\_12 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/blob/sf_12/src/position.h#L193)
31. [↑](#cite_ref-31) [Remove piece lists by syzygy1 · Pull Request #3247 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3247)
32. [↑](#cite_ref-32) [Re: piece lists advantage with bit-boards?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69364&start=12) by [Ronald de Man](Ronald_de_Man "Ronald de Man"), [CCC](CCC "CCC"), December 26, 2018
33. [↑](#cite_ref-33) [Re: Stockfish 7 progress](http://www.talkchess.com/forum/viewtopic.php?t=58935&start=2) by Lucas Braesch, [CCC](CCC "CCC"), January 17, 2016
34. [↑](#cite_ref-34) [The Art of Evaluation](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=135133&t=15504) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), August 2, 2007
35. [↑](#cite_ref-35) [Stockfish Evaluation Guide](https://hxim.github.io/Stockfish-Evaluation-Guide/)
36. [↑](#cite_ref-36) [exoticorn/stockfish-js · GitHub](https://github.com/exoticorn/stockfish-js)
37. [↑](#cite_ref-37) [Cscuile's Sheets](https://docs.google.com/spreadsheets/d/1ZAIuHR6n-5JTxKQc0XUSx1jyUrgVEcj8DNLKA7-urBw/edit#gid=201239930)
38. [↑](#cite_ref-38) Part 1 covers [Houdini](Houdini "Houdini"), [Rybka](Rybka "Rybka"), [Komodo](Komodo "Komodo"), Stockfish, [Critter](Critter "Critter"), [Naum](Naum "Naum"), [Chiron](Chiron "Chiron") and [Spike](Spike "Spike")
39. [↑](#cite_ref-39) [Who is the Master?](http://www.alliot.fr/CHESS/ficga.html.en) from [Jean-Marc Alliot's](Jean-Marc_Alliot "Jean-Marc Alliot") [professional website](http://www.alliot.fr/fpro.html.en)
40. [↑](#cite_ref-40) [exoticorn/stockfish-js · GitHub](https://github.com/exoticorn/stockfish-js)
41. [↑](#cite_ref-41) [Delphil 3.3b2 (2334) - Stockfish 030916 (3228), TCEC Season 9 - Rapid, Round 11](http://tcec.chessdom.com/archive.php?se=9&rapid&ga=163), September 16, 2016
42. [↑](#cite_ref-42) [Use equations for PushAway and PushClose · official-stockfish/Stockfish@5a7b45e · GitHub](https://github.com/official-stockfish/Stockfish/commit/5a7b45eac9dedbf7ebc61d9deb4dd934058d1ca1#diff-4cd6bcdb505b124d7bdc612c4789dc26L57-R59)
43. [↑](#cite_ref-43) [Update default net to nn-8a08400ed089.nnue by Sopel97 · Pull Request #3474 · official-stockfish/Stockfish · GitHub](https://github.com/official-stockfish/Stockfish/pull/3474) by [Tomasz Sobczyk](Tomasz_Sobczyk "Tomasz Sobczyk")
44. [↑](#cite_ref-44) [Sopel97 (Tomasz Sobczyk) · GitHub](https://github.com/Sopel97)
45. [↑](#cite_ref-45) [Regan's latest: Depth of Satisficing](http://www.talkchess.com/forum/viewtopic.php?t=57890) by Carl Lumma, [CCC](CCC "CCC"), October 09, 2015
46. [↑](#cite_ref-46) [An info](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=74560) by Sylwy, [CCC](CCC "CCC"), July 25, 2020

**[Up one Level](Engines "Engines")**







 
