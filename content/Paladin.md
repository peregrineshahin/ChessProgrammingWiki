---
title: Paladin
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Paladin**



[ Charlemagne and his Paladin <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Paladin**,  

an experimental [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), written in [C++](Cpp "Cpp"). 
Paladin is intended as testbed for various [bitboard](Bitboards "Bitboards") techniques concerning [space-time tradeoff](Space-Time_Tradeoff "Space-Time Tradeoff"), more or less suited for various architectures, such as [GPU](GPU "GPU") friendly [Kogge-Stone algorithms](Kogge-Stone_Algorithm "Kogge-Stone Algorithm") versus [fancy](Magic_Bitboards#Fancy "Magic Bitboards") or even [plain magic bitboards](Magic_Bitboards#Plain "Magic Bitboards") to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). Paladin features a set of [compile time](https://en.wikipedia.org/wiki/Compile_time) switches to control the [search](Search "Search"), to use intrinsics for [population count](Population_Count "Population Count") and [bitscan](BitScan "BitScan"), and as mentioned, to determine computation versus lookup techniques <a id="cite-note-2" href="#cite-ref-2">[2]</a>. While not officially released nor announced, the testing community exploited the publicly available sources from [GitHub](https://en.wikipedia.org/wiki/GitHub) providing its author with a [fait accompli](https://en.wiktionary.org/wiki/fait_accompli) <a id="cite-note-3" href="#cite-ref-3">[3]</a>.



### Board Representation


Paladin's [board is represented](Board_Representation "Board Representation") by a dense hexa bitboard suited for a [copy-make approach](Copy-Make "Copy-Make"), that is six [bitboards](Bitboards "Bitboards") for white pieces, pawns, knights, diagonal and orthogonal sliding pieces, and kings. The base ranks of the pawn bitboard are even used to encode game state data such as [castling rights](Castling_Rights "Castling Rights"), [en passant](En_passant "En passant") target square and [halfmove clock](Halfmove_Clock "Halfmove Clock") <a id="cite-note-4" href="#cite-ref-4">[4]</a>.



### Search


The [search](Search "Search") is basic [alpha-beta](Alpha-Beta "Alpha-Beta") with [transposition table](Transposition_Table "Transposition Table") inside an [iterative deepening](Iterative_Deepening "Iterative Deepening") loop without [aspiration](Aspiration_Windows "Aspiration Windows") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a>, enhanced by [adaptive null move pruning](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning"), [LMR](Late_Move_Reductions "Late Move Reductions") and a few [extensions](Extensions "Extensions"). [Move ordering](Move_Ordering "Move Ordering") is due to [hash move](Hash_Move "Hash Move") and [IID](Internal_Iterative_Deepening "Internal Iterative Deepening"), [MVV/LVA](MVV-LVA "MVV-LVA") and [SEE](Static_Exchange_Evaluation "Static Exchange Evaluation") for [captures](Captures "Captures"), and [killer heuristic](Killer_Heuristic "Killer Heuristic") and [history heuristic](History_Heuristic "History Heuristic") otherwise.



### Evaluation


Paladin's rudimentary [evaluation](Evaluation "Evaluation") is based on the [simplified evaluation function](Simplified_Evaluation_Function "Simplified Evaluation Function") by [Tomasz Michniewski](Tomasz_Michniewski "Tomasz Michniewski") with [point values](Point_Value "Point Value") partly taken from [Larry Kaufman's](Larry_Kaufman "Larry Kaufman") material imbalance article <a id="cite-note-7" href="#cite-ref-7">[7]</a> <a id="cite-note-8" href="#cite-ref-8">[8]</a>.



## Forum Posts


* [New engine?](http://www.talkchess.com/forum/viewtopic.php?t=60328) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 31, 2016


 [Re: New engine?](http://www.talkchess.com/forum/viewtopic.php?t=60328&start=10) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), July 11, 2016
## External Links


### Chess Engine


* [GitHub - ankan-ban/chess\_cpu: Ankan's new chess engine](https://github.com/ankan-ban/chess_cpu)
* [Paladin 0.1 64-bit](http://www.computerchess.org.uk/ccrl/404/cgi/engine_details.cgi?print=Details&eng=Paladin%200.1%2064-bit#Paladin_0_1_64-bit) in [CCRL 40/4](CCRL "CCRL")


### Misc


* [paladin - Wiktionary](https://en.wiktionary.org/wiki/paladin)
* [Paladin from Wikipedia](https://en.wikipedia.org/wiki/Paladin)
* [Paladin (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Paladin_(disambiguation))


 [Paladin (comics) from Wikipedia](https://en.wikipedia.org/wiki/Paladin_(comics))
 [Paladin (character class) from Wikipedia](https://en.wikipedia.org/wiki/Paladin_(character_class))
* [Paladin](http://www.progarchives.com/artist.asp?id=1292) - The Fakir I (1971), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Roland](https://en.wikipedia.org/wiki/Roland) receives the sword [Durendal](https://en.wikipedia.org/wiki/Durendal) from [Holy Roman Emperor](https://en.wikipedia.org/wiki/Holy_Roman_Emperor) [Charlemagne](https://en.wikipedia.org/wiki/Charlemagne). From a manuscript of a [chanson de geste](https://en.wikipedia.org/wiki/Chanson_de_geste). [Paladin from Wikipedia](https://en.wikipedia.org/wiki/Paladin), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [chess\_cpu/switches.h at master · ankan-ban/chess\_cpu · GitHub](https://github.com/ankan-ban/chess_cpu/blob/master/switches.h)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Re: New engine?](http://www.talkchess.com/forum/viewtopic.php?t=60328&start=10) by [Ankan Banerjee](Ankan_Banerjee "Ankan Banerjee"), [CCC](CCC "CCC"), July 11, 2016
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [chess\_cpu/chess.h at master · ankan-ban/chess\_cpu · GitHub](https://github.com/ankan-ban/chess_cpu/blob/master/chess.h)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [chess\_cpu/main.cpp at master · ankan-ban/chess\_cpu · GitHub](https://github.com/ankan-ban/chess_cpu/blob/master/main.cpp)
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [chess\_cpu/search.cpp at master · ankan-ban/chess\_cpu · GitHub](https://github.com/ankan-ban/chess_cpu/blob/master/search.cpp)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [The Evaluation of Material Imbalances](http://www.danheisman.com/evaluation-of-material-imbalances.html) by [Larry Kaufman](Larry_Kaufman "Larry Kaufman")
8. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [chess\_cpu/eval.cpp at master · ankan-ban/chess\_cpu · GitHub](https://github.com/ankan-ban/chess_cpu/blob/master/eval.cpp)

**[Up one Level](Engines "Engines")**







 
