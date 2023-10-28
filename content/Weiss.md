---
title: Weiss
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Weiss**



[ [Weiss](https://en.wikipedia.org/wiki/Weiss_(crater)) and its satellite craters <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Weiss**,   

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), 
written in [C](C "C"), first released in November 2019 under the [GPL 3](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Weiss was initially based on [Vice](Vice "Vice") and is inspired by [Ethereal](Ethereal "Ethereal"), [Stockfish](Stockfish "Stockfish") and [Demolito](Demolito "Demolito").
It is part of the [OpenBench](OpenBench "OpenBench") testing framework <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Weiss had its tournament debut at [TCEC Season 18](TCEC_Season_18 "TCEC Season 18") in May 2020.



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 Forum Posts](#forum-posts)
* [3 External Links](#external-links)
	+ [3.1 Chess Engine](#chess-engine)
	+ [3.2 Misc](#misc-2)
* [4 References](#references)






### [Board Representation](Board_Representation "Board Representation")


* [Dense Bitboard Board-Definition](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition")
* [8x8 Board](8x8_Board "8x8 Board")
* [Fancy Magic Bitboards](Magic_Bitboards#Fancy "Magic Bitboards")
* [PEXT Bitboards](BMI2#PEXTBitboards "BMI2")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Razoring](Razoring "Razoring")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Rook on (Half) Open File](Rook_on_Open_File "Rook on Open File")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
* [King Safety - Virtual Mobility](King_Safety#VMOB "King Safety")
* [Tempo](Tempo "Tempo")
* [Automated Tuning](Automated_Tuning "Automated Tuning")


### Misc


* [Syzygy Bases](Syzygy_Bases "Syzygy Bases") using [Fathom](Syzygy_Bases#Fathom "Syzygy Bases")
* [Perft](Perft "Perft")


## Forum Posts


* [Engine release: weiss](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72369) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), November 19, 2019
* [Re: New engine releases 2019](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=422) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), December 06, 2019
* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=10) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), January 07, 2020
* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=71) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), February 14, 2020
* [Re: New engine releases 2020](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72613&start=170) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), April 25, 2020
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=458) (Weiss 1.4) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), July 02, 2021


## External Links


### Chess Engine


* [GitHub - GitHub - TerjeKir/weiss: Weiss - a UCI chess engine](https://github.com/TerjeKir/weiss)
* [Weiss](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Weiss&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


### Misc


* [weiss - Wiktionary](https://en.wiktionary.org/wiki/weiss)
* [Weiss - Wiktionary](https://en.wiktionary.org/wiki/Weiss)
* [weiß - Wiktionary](https://en.wiktionary.org/wiki/wei%C3%9F)
* [white - Wiktionary](https://en.wiktionary.org/wiki/white)
* [Weiss from Wikipedia](https://en.wikipedia.org/wiki/Weiss)
* [Weiss (crater) from Wikipedia](https://en.wikipedia.org/wiki/Weiss_(crater))
* [Weiß – Wikipedia.de](https://de.wikipedia.org/wiki/Wei%C3%9F) (German)
* [White from Wikipedia](https://en.wikipedia.org/wiki/White)
* [Hvit – Wikipedia.no](https://no.wikipedia.org/wiki/Hvit) (Bokmål)
* [Kvit – Wikipedia.nn](https://nn.wikipedia.org/wiki/Kvit) (Nynorsk)
* [Häns'che Weiss Quintett](https://www.discogs.com/artist/1419247-H%C3%A4nsche-Weiss-Quintett), Dutch TV, 1977, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 Lineup: [Häns'che Weiss](https://en.wikipedia.org/wiki/H%C3%A4ns%27che_Weiss), [Lulu Reinhardt](https://en.wikipedia.org/wiki/Lulu_Reinhardt), [Ziroli Winterstein](https://de.wikipedia.org/wiki/Ziroli_Winterstein), [Titi Winterstein](https://de.wikipedia.org/wiki/Titi_Winterstein), [Hojok Merstein](https://www.discogs.com/artist/1419244-Hojok-Merstein)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Weiss](https://en.wikipedia.org/wiki/Weiss_(crater)) (named after Austrian astronomer [Edmund Weiss](https://en.wikipedia.org/wiki/Edmund_Weiss)) and its satellite [craters](https://en.wikipedia.org/wiki/Impact_crater) on the [moon](https://en.wikipedia.org/wiki/Moon), [Image](https://commons.wikimedia.org/wiki/File:Weiss_satellite_craters_map.jpg) by [Андрей Щербаков](https://commons.wikimedia.org/wiki/User:%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9_%D0%A9%D0%B5%D1%80%D0%B1%D0%B0%D0%BA%D0%BE%D0%B2), October 30, 2013, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Engine release: weiss](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72369) by [Terje Kirstihagen](index.php?title=Terje_Kirstihagen&action=edit&redlink=1 "Terje Kirstihagen (page does not exist)"), [CCC](CCC "CCC"), November 19, 2019
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [weiss/README.md at master · TerjeKir/weiss · GitHub](https://github.com/TerjeKir/weiss/blob/master/README.md)

**[Up one Level](Engines "Engines")**







 
