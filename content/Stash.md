---
title: Stash
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Stash**



[ The [Omphalos stone](https://en.wikipedia.org/wiki/Omphalos_of_Delphi) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Stash**, (Stash-bot)  

an [UCI](UCI "UCI") compliant [open source chess engine](Category:Open_Source "Category:Open Source") by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), written in [C](C "C"), licensed under the [GPL v3](Free_Software_Foundation#GPL "Free Software Foundation") and first released on [GitLab](https://en.wikipedia.org/wiki/GitLab) in February 2020 <a id="cite-note-2" href="#cite-ref-2">[2]</a>. 



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
* [PEXT Bitboards](BMI2#PEXTBitboards "BMI2")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
	+ [Shared Hash Table](Shared_Hash_Table "Shared Hash Table")
	+ [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [Hash Move](Hash_Move "Hash Move")
	+ [Promotions](Promotions "Promotions")
	+ [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")
	+ [MVV/LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
* [Selectivity](Selectivity "Selectivity")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Razoring](Razoring#dropping-into-q-search "Razoring")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Delta Pruning](Delta_Pruning "Delta Pruning")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Zugzwang Verification](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
	+ [ProbCut](ProbCut "ProbCut")
	+ [Singular Extensions](Singular_Extensions "Singular Extensions")
	+ [Check Extensions](Check_Extensions "Check Extensions")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Mate Distance Pruning](Mate_Distance_Pruning "Mate Distance Pruning")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")


### [Evaluation](Evaluation "Evaluation")


* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
	+ [Bishop Pair](Bishop_Pair "Bishop Pair")
	+ [Draw Evaluation](Draw_Evaluation "Draw Evaluation")
* [Mobility](Mobility "Mobility")
	+ [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Castling Rights](Castling_Rights "Castling Rights")


## Forum Posts


* [New engine: Stash](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73092) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), February 14, 2020
* [Re: Linux friendly engines at all levels](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69693&start=27) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), October 11, 2020
* [INTERESTING Engines with Unique Styles (Unlike SF)](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75371) by [Brendan J. Norman](index.php?title=Brendan_J._Norman&action=edit&redlink=1 "Brendan J. Norman (page does not exist)"), [CCC](CCC "CCC"), October 11, 2020
* [Re: Stash has lost 2 game because of NO EGTB](http://talkchess.com/forum3/viewtopic.php?f=2&t=76927#p888045) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), March 25, 2021
* [Re: New engine releases & news 2021](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76209&start=299) (Stash 30.0, [Bagatur](Bagatur "Bagatur") 2.2b) by [Günther Simon](G%C3%BCnther_Simon "Günther Simon"), [CCC](CCC "CCC"), May 01, 2021
* [Re: New engine: Stash](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73092&start=120) (Stash 31.0) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), June 28, 2021


## External Links


### Chess Engine


* [Morgan Houppin / stash-bot · GitLab](https://gitlab.com/mhouppin/stash-bot)
* [GitHub - mhouppin/stash-bot: Mirror of my Gitlab chess engine project](https://github.com/mhouppin/stash-bot)
* [Stash in CCRL Blitz](http://ccrl.chessdom.com/ccrl/404/cgi/compare_engines.cgi?family=Stash&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)


### Misc


* [stash - Wiktionary](https://en.wiktionary.org/wiki/stash)
* [Stash from Wikipedia](https://en.wikipedia.org/wiki/Stash)
* [Phish](Category:Phish "Category:Phish") - [Stash](https://en.wikipedia.org/wiki/Stash_(Phish_album)), [Merriweather Post Pavilion](https://en.wikipedia.org/wiki/Merriweather_Post_Pavilion) in [Columbia, MD](https://en.wikipedia.org/wiki/Columbia,_Maryland), July 14, 2013, [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The [omphalos stone](https://en.wikipedia.org/wiki/Omphalos_of_Delphi) displayed outside at [Delphi](https://en.wikipedia.org/wiki/Delphi), [Greece](https://en.wikipedia.org/wiki/Greece), lower piece is a stash, [Image](https://commons.wikimedia.org/wiki/File:Outside_Omphalos_at_Delphi.jpg) by [Patar knight](https://commons.wikimedia.org/wiki/User:Patar_knight), March 21, 2009, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [New engine: Stash](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73092) by [Morgan Houppin](Morgan_Houppin "Morgan Houppin"), [CCC](CCC "CCC"), February 14, 2020
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> Features based on [Releases · Morgan Houppin / stash-bot · GitLab v22.0](https://gitlab.com/mhouppin/stash-bot/-/releases#v22.0)

**[Up one level](Engines "Engines")**







 
