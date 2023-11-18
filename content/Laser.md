---
title: Laser
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Laser**



[ [Laser](https://en.wikipedia.org/wiki/Laser) Towards [Milky Way's](https://en.wikipedia.org/wiki/Milky_Way) Center <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Laser**,  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)") and [Michael An](index.php?title=Michael_An&action=edit&redlink=1 "Michael An (page does not exist)"), written in [C++11](Cpp "Cpp"), first released in summer 2015 under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"). Laser **1.0**, released in December 2015, already performes [lazy SMP](Lazy_SMP "Lazy SMP") <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")


### [Search](Search "Search")


* [Lazy SMP](Lazy_SMP "Lazy SMP") (rewritten with 1.6)
* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Fail-Hard](Fail-Hard "Fail-Hard") [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
	+ [Two Bucket System](Transposition_Table#Bucket "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Adaptive Null Move Pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions"), since 1.3 also at [PV nodes](Node_Types#PV-Node "Node Types")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Razoring](Razoring "Razoring")
	+ [Move Count Based Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning") (Late Move Pruning)
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Singular Extensions](Singular_Extensions "Singular Extensions")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Captures](Captures "Captures")
	+ [Queen Promotions](Promotions "Promotions")
	+ [Checks](Check "Check") on first three [plies](Ply "Ply")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Evaluation Cache](Evaluation_Hash_Table "Evaluation Hash Table")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [King Safety](King_Safety "King Safety")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Mobility](Mobility "Mobility")
* [SWAR](SIMD_and_SWAR_Techniques "SIMD and SWAR Techniques") [Tapered Eval](Tapered_Eval "Tapered Eval") à la [Stockfish](Stockfish "Stockfish")
* [Tuned](Automated_Tuning "Automated Tuning") with [reinforcement learning](Reinforcement_Learning "Reinforcement Learning"), [coordinate descent](https://en.wikipedia.org/wiki/Coordinate_descent), and a variation of [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")


### Misc


* [Syzygy TB support](Syzygy_Bases "Syzygy Bases") (1.3)


## Forum Posts


* [Laser 0.1 moves instantly every move for me](http://www.talkchess.com/forum/viewtopic.php?t=57690) by [Graham Banks](Graham_Banks "Graham Banks"), [CCC](CCC "CCC"), September 18, 2015
* [Laser 1.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=58680) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), December 24, 2015
* [Laser 1.1 Release](http://www.talkchess.com/forum/viewtopic.php?t=59898) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), April 18, 2016
* [Laser 1.2 Release](http://www.talkchess.com/forum/viewtopic.php?t=61451) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), September 17, 2016
* [Laser 1.3 Release](http://www.talkchess.com/forum/viewtopic.php?t=62771) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), January 08, 2017
* [Laser 1.4 Release](http://www.talkchess.com/forum/viewtopic.php?t=63956) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), May 11, 2017
* [Laser 1.5 Release](http://www.talkchess.com/forum/viewtopic.php?t=66153) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), December 27, 2017
* [Laser 1.6 Release](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67982) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), July 14, 2018


## External Links


### Chess Engine


* [jeffreyan11/uci-chess-engine · GitHub](https://github.com/jeffreyan11/uci-chess-engine)
* [Releases · jeffreyan11/uci-chess-engine · GitHub](https://github.com/jeffreyan11/uci-chess-engine/releases)
* [Laser 1.6 64-bit 4CPU](http://www.computerchess.org.uk/ccrl/4040/cgi/engine_details.cgi?match_length=30&each_game=1&print=Details&each_game=1&eng=Laser%201.6%2064-bit%204CPU#Laser_1_6_64-bit_4CPU) in [CCRL 40/40](CCRL "CCRL")


### Misc


* [Laser from Wikipedia](https://en.wikipedia.org/wiki/Laser)
* [Laser (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Laser_%28disambiguation%29)
* [Au5](https://en.wikipedia.org/wiki/Au5) & [Fractal](https://en.wikipedia.org/wiki/Fractal_(producer)) - [Laser Beam Show](https://en.wikipedia.org/wiki/Laser_lighting_display), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> In mid-August 2010 [ESO](https://en.wikipedia.org/wiki/European_Southern_Observatory) Photo Ambassador Yuri Beletsky snapped [this photo](https://commons.wikimedia.org/wiki/File:Laser_Towards_Milky_Ways_Centre.jpg) at ESO’s [Paranal Observatory](https://en.wikipedia.org/wiki/Paranal_Observatory), [Chile](https://en.wikipedia.org/wiki/Chile). A group of astronomers were observing the center of the [Milky Way](https://en.wikipedia.org/wiki/Milky_Way) using the [laser guide star](https://en.wikipedia.org/wiki/Laser_guide_star) facility at Yepun, one of the four Unit Telescopes of the [Very Large Telescope](https://en.wikipedia.org/wiki/Very_Large_Telescope). [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Laser 1.0 Release](http://www.talkchess.com/forum/viewtopic.php?t=58680) by [Jeffrey An](index.php?title=Jeffrey_An&action=edit&redlink=1 "Jeffrey An (page does not exist)"), [CCC](CCC "CCC"), December 24, 2015
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [uci-chess-engine/README.md at master · jeffreyan11/uci-chess-engine · GitHub](https://github.com/jeffreyan11/uci-chess-engine/blob/master/README.md)

**[Up One Level](Engines "Engines")**







 
