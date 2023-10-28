---
title: Sloppy
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Sloppy**



 [](https://en.wikipedia.org/wiki/Sloppy_identity) Sloppy Reading Tree <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**Sloppy**,  

an [open source chess engine](Category:Open_Source "Category:Open Source") by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), written in [C](C "C") to build executables to run under [Windows](Windows "Windows"), [Linux](Linux "Linux") and [OS X](Mac_OS "Mac OS"), compliant with the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"). Sloppy is released under the [GPLv3](Free_Software_Foundation#GPL "Free Software Foundation") license, and was first published in October, 2007 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 
Sloppy is full of [low-level trickery](Bit-Twiddling "Bit-Twiddling") with [bitwise operators](General_Setwise_Operations "General Setwise Operations"), efficient [data structures](Data "Data") and [algorithms](Algorithms "Algorithms"). Starting with [rotated bitboards](Rotated_Bitboards "Rotated Bitboards") <a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
it uses [magic bitboards](Magic_Bitboards "Magic Bitboards") based on [Pradu Kannan's](Pradu_Kannan "Pradu Kannan") implementation <a id="cite-note-4" href="#cite-ref-4">[4]</a> to determine [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks"). 
Sloppy **0.2.0**, released in February 2008, supports [Daniel Shawul's](Daniel_Shawul "Daniel Shawul") [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.



### Contents


* [1 Features](#features)
	+ [1.1 Board Representation](#board-representation)
	+ [1.2 Search](#search)
	+ [1.3 Evaluation](#evaluation)
	+ [1.4 Misc](#misc)
* [2 See also](#see-also)
* [3 Forum Posts](#forum-posts)
* [4 External Links](#external-links)
	+ [4.1 Chess Engine](#chess-engine)
	+ [4.2 Misc](#misc-2)
* [5 References](#references)






<a id="cite-note-6" href="#cite-ref-6">[6]</a>



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [Legal Move Generation](Move_Generation#Legal "Move Generation")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [PVS](Principal_Variation_Search "Principal Variation Search") / [Alpha-Beta](Alpha-Beta "Alpha-Beta")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Quiescence Search](Quiescence_Search "Quiescence Search")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
	+ [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [PV-Move](PV-Move "PV-Move")
	+ [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
* [Tempo](Tempo "Tempo")
* [Evaluation Patterns](Evaluation_Patterns "Evaluation Patterns")
	+ [Outposts](Outposts "Outposts")
	+ [Rook on Open and Semi-open File](Rook_on_Open_File "Rook on Open File")
	+ [Rook on Seventh Rank](Rook_on_Seventh "Rook on Seventh")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
	+ [Candidate Passed Pawn](Candidate_Passed_Pawn "Candidate Passed Pawn")
* [King Pawn Tropism](King_Pawn_Tropism "King Pawn Tropism")
* [King Safety](King_Safety "King Safety")
	+ [Castling Rights](Castling_Rights "Castling Rights")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
	+ [Pawn Storm](King_Safety#PawnStorm "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [King Queen Tropism](King_Safety#KingTropism "King Safety")


### Misc


* [Opening Book](Opening_Book "Opening Book")
	+ [Book Learning](Book_Learning "Book Learning")
	+ [AVL tree](Georgy_Adelson-Velsky "Georgy Adelson-Velsky")
* [Perft](Perft "Perft")
* [Scorpio Bitbases](Scorpio_Bitbases "Scorpio Bitbases")


## See also


* [Cute Chess](Cute_Chess "Cute Chess")
* [Cutechess-cli](Cutechess-cli "Cutechess-cli")


## Forum Posts


* [Sloppy 0.1.1 released](http://www.talkchess.com/forum/viewtopic.php?t=17305) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), October 23, 2007
* [Some sloppy results](http://www.talkchess.com/forum/viewtopic.php?t=17577) by Tony Thomas, [CCC](CCC "CCC"), November 04, 2007
* [Sloppy 0.2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=19432) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), February 06, 2008
* [Results of Crafty 22.0, Sloppy 0.2.0 and Atlanchess 4.1](http://www.talkchess.com/forum/viewtopic.php?t=19807) by Tony Thomas, [CCC](CCC "CCC"), February 24, 2008 » [Crafty](Crafty "Crafty"), [AtlanChess](AtlanChess "AtlanChess")
* [Sloppy experiment, results after 1 cycle](http://www.talkchess.com/forum/viewtopic.php?t=19934) by Tony Thomas, [CCC](CCC "CCC"), March 01, 2008


## External Links


### Chess Engine


* [Sloppy : Home](http://ilaripih.mbnet.fi/sloppy/index.html)
* [GitHub - cutechess/sloppy: Chess engine using the XBoard chess protocol](https://github.com/cutechess/sloppy)
* [Index of /chess/engines/Jim Ablett/SLOPPY](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/SLOPPY/) compliled by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Sloppy](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Sloppy&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")


### Misc


* [sloppy - Wiktionary](https://en.wiktionary.org/wiki/sloppy)
* [Sloppy from Wikipedia](https://en.wikipedia.org/wiki/Sloppy)
* [Sloppy identity from Wikipedia](https://en.wikipedia.org/wiki/Sloppy_identity)
* [Sloppy Meateaters](https://en.wikipedia.org/wiki/Sloppy_Meateaters) - [Play The Game](https://www.discogs.com/composition/35c9667f-d8cb-4713-86dc-e00ae513ae1d-Play-The-Game), [Forbidden Meat](https://www.discogs.com/release/6142474) (2001), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> Image made by Dcstrosh to show the sloppy reading of a sentence, [Sloppy identity from Wikipedia](https://en.wikipedia.org/wiki/Sloppy_identity), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Sloppy : Home](http://ilaripih.mbnet.fi/sloppy/index.html)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [sloppy/CHANGES at master · cutechess/sloppy · GitHub](https://github.com/cutechess/sloppy/blob/master/CHANGES)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [sloppy/magicmoves.c at master · cutechess/sloppy · GitHub](https://github.com/cutechess/sloppy/blob/master/src/magicmoves.c)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Sloppy 0.2.0 released](http://www.talkchess.com/forum/viewtopic.php?t=19432) by [Ilari Pihlajisto](Ilari_Pihlajisto "Ilari Pihlajisto"), [CCC](CCC "CCC"), February 06, 2008
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> Features based on [sloppy/src at master · cutechess/sloppy · GitHub](https://github.com/cutechess/sloppy/tree/master/src)

**[Up one level](Engines "Engines")**







 
