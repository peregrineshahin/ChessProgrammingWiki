---
title: Ifrit
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Ifrit**



[ An Ifrit named Arghan Div <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Ifrit**, (Ифрит)  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Andrey Brenkman](index.php?title=Andrey_Brenkman&action=edit&redlink=1 "Andrey Brenkman (page does not exist)"), written in [C++](Cpp "Cpp"), distributed under the [GNU General Public License](Free_Software_Foundation#GPL "Free Software Foundation"), with executables built to run under [Windows](Windows "Windows"), [Linux](Linux "Linux"), [Mac OS](Mac_OS "Mac OS") and [Android](Android "Android"), 64, and 32 bit. 
The development started in 2006, as suggested by the copyright notice inside the source files, the most recent version m1.8 published on [Bitbucket](https://en.wikipedia.org/wiki/Bitbucket) on June 14, 2012. Ifrit used several [board representations](Board_Representation "Board Representation") and implementations in four series, namely [0x88](0x88 "0x88") in series "c" , [Bitboards](Bitboards "Bitboards") in "b", object oriented Bitboards in series "j", and finally, [Magic Bitboards](Magic_Bitboards "Magic Bitboards") in series "m". The [search](Search "Search") does not perform [Negamax](Negamax "Negamax"), but indirect [recursion](Recursion "Recursion") with White as max-player and Black as min-player. Some routines, such as [bitscan](BitScan "BitScan"), are instantiated in multiple source files, bitboard constants are defined as decimals rather than more intuitive [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) for board pattern. 



### [Move Generation](Move_Generation "Move Generation")


* [Plain Magic Bitboards](Magic_Bitboards#Plain "Magic Bitboards")
* [BitScan Forward by De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
* [BitScan Reverse by Double Conversion](BitScan#DoubleConversionBSR "BitScan")
* [SWAR-Popcount](Population_Count#SWARPopcount "Population Count")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
* [Selectivity](Selectivity "Selectivity")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Razoring](Razoring "Razoring")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")


### [Evaluation](Evaluation "Evaluation")


* [Material](Material "Material")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
* [King Safety](King_Safety "King Safety")
	+ [Pawn Shield](King_Safety#PawnShield "King Safety")
	+ [Square Control](King_Safety#SquareControl "King Safety")


## See also


* [Djinn](Djinn "Djinn")
* [Genie](Genie "Genie")


## Forum Posts


* [Ifrid??](http://www.talkchess.com/forum/viewtopic.php?t=18427) by Tony Thomas, [CCC](CCC "CCC"), December 17, 2007
* [Ifrit](http://www.talkchess.com/forum/viewtopic.php?t=18525) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), December 24, 2007
* [Ifrit Updated](http://www.talkchess.com/forum/viewtopic.php?t=32163) by [Swaminathan Natarajan](Swaminathan_Natarajan "Swaminathan Natarajan"), January 29, 2010
* [[STS 1-10] Ifrit 3.6](http://www.talkchess.com/forum/viewtopic.php?t=35800) by [Swaminathan Natarajan](Swaminathan_Natarajan "Swaminathan Natarajan"), August 14, 2010


## External Links


### Chess Engine


* [Шахматная программа Ифрит (Ifrit chess engine)](http://alphagameset.xyz/ifrit/ifrit_chess_engine.html)
* [abrenkman / Ifrit\_chess\_engine / source / — Bitbucket](https://bitbucket.org/abrenkman/ifrit_chess_engine/src/default/)
* [Index of /chess/engines/Jim Ablett/IFRIT](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/IFRIT/) by [Jim Ablett](Jim_Ablett "Jim Ablett") hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
* [Mac Chess Engines Repository](http://julien.marcel.free.fr/macchess/Chess_on_Mac/Engines.html) hosted by [Julien Marcel](Julien_Marcel "Julien Marcel")
* [Ifrit](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Ifrit&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/40](CCRL "CCRL")


### Misc


* [Ifrit from Wikipedia](https://en.wikipedia.org/wiki/Ifrit)


 [Ифрит — Википедия](https://ru.wikipedia.org/wiki/%D0%98%D1%84%D1%80%D0%B8%D1%82)
* [Melechesh](https://en.wikipedia.org/wiki/Melechesh) - A Summoning of Ifrit and Genii, [Djinn](https://en.wikipedia.org/wiki/Djinn_(album)) (2001), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> "An Ifrit named Arghan [Div](https://en.wikipedia.org/wiki/Daeva) brings the chest of armor to [Hamza](https://en.wikipedia.org/wiki/Hamzanama)", unknown artist, between 1562 and 1577, [Brooklyn Museum](https://en.wikipedia.org/wiki/Brooklyn_Museum), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Ifrit from Wikipedia](https://en.wikipedia.org/wiki/Ifrit)
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> Based on Ifrit\_m1\_9\_Beta\_24\_June\_2012, [abrenkman / Ifrit\_chess\_engine / source / — Bitbucket](https://bitbucket.org/abrenkman/ifrit_chess_engine/src/default/)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Bitscan forward by De Bruijn Multiplication](BitScan#DeBruijnMultiplation "BitScan") with De Bruijn constant from CPW, 0x03F79D71B4CB0A89, used as decimal magic 285870213051386505, implementation (decimal conversion?) credited to [Jim Ablett](Jim_Ablett "Jim Ablett"), routine by [Charles Leiserson](Charles_Leiserson "Charles Leiserson"), [Harald Prokop](Harald_Prokop "Harald Prokop") and [Keith H. Randall](Keith_H._Randall "Keith H. Randall"), end of [abrenkman / Ifrit\_chess\_engine / source / move\_generation.cpp — Bitbucket](https://bitbucket.org/abrenkman/ifrit_chess_engine/src/159ff9cab144e4fb6d63f208550566b3d2ed4f81/move_generation.cpp?fileviewer=file-view-default), also instantiated elsewhere

**[Up one Level](Engines "Engines")**







 
