---
title: Mantissa
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* Mantissa**



 [](File:Mantissa_logo_minimal.png) Mantissa's Logo <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a> 
**Mantissa**,  

an [UCI](UCI "UCI") compatible [open source chess engine](Category:Open_Source "Category:Open Source") by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), written in [Rust](Rust "Rust"), 
licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation"), first released in September 2021 <a id="cite-note-3" href="#cite-ref-3">[3]</a>.
Supported by [Zahak](Zahak "Zahak") author [Amanj Sherwany](Amanj_Sherwany "Amanj Sherwany"), Mantissa **v3.0.0**, released in December 2021, came with an [NNUE](NNUE "NNUE") implementation of a 769 -> 128 -> 1 net topology.
In Mantissa **v3.3.0**, released in January 2022, the net topology was changed due to an inspiration from reading [Koivisto's](Koivisto "Koivisto") source code, considering board symmetry. 
Now instead of a 769th feature for [side to move](Side_to_move "Side to move"), the new net uses 2 sets of 128 neurons in the hidden layer with mirrored weights to reflect the game from the point of views of both sides. 



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards")
* [Magic Bitboards](Magic_Bitboards "Magic Bitboards")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
* [Lazy SMP](Lazy_SMP "Lazy SMP")
* [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Selectivity](Selectivity "Selectivity")
	+ [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
	+ [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
	+ [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
	+ [Futility Pruning](Futility_Pruning "Futility Pruning")
	+ [Reverse Futility Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning")
	+ [Singular Extensions](Singular_Extensions "Singular Extensions")
	+ [Multi-Cut](Multi-Cut "Multi-Cut")
	+ [Quiescence Search](Quiescence_Search "Quiescence Search")
	+ [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
* [Move Ordering](Move_Ordering "Move Ordering")
	+ [MVV-LVA](MVV-LVA "MVV-LVA")
	+ [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
	+ [History Heuristic](History_Heuristic "History Heuristic")
	+ [Countermove Heuristic](Countermove_Heuristic "Countermove Heuristic")


### [Evaluation](Evaluation "Evaluation")


* [NNUE](NNUE "NNUE") (v3.0.0)
* [Tapered Evaluation](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
* [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
* [Rook on (Semi) Open File](Rook_on_Open_File "Rook on Open File")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Advanced Connected Pawns](Connected_Pawns "Connected Pawns")
	+ [Passed Pawns](Passed_Pawn "Passed Pawn")
* [King Safety](King_Safety "King Safety")


## Forum Posts


* [New Engine: Mantissa](https://kirill-kryukov.com/chess/discussion-board/viewtopic.php?t=13339) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), September 19, 2021
* [Mantissa 3.0.0](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78855) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCC](CCC "CCC"), December 10, 2021
* [Re: New engine releases & news H1 2022](https://www.talkchess.com/forum3/viewtopic.php?f=2&t=78884&start=18) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCC](CCC "CCC"), January 11, 2022


## External Links


### Chess Engine


* [GitHub - jtheardw/mantissa: Chess Engine](https://github.com/jtheardw/mantissa)
* [Mantissa](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=Mantissa&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) at [CCRL 40/15](CCRL "CCRL")


### Misc


* [Mantissa from Wikipedia](https://en.wikipedia.org/wiki/Mantissa)
* [Common logarithm from Wikipedia](https://en.wikipedia.org/wiki/Common_logarithm#)
* [Significand from Wikipedia](https://en.wikipedia.org/wiki/Significand)
* [Mantissa](https://en.wikipedia.org/wiki/Mantissa_(band)) - Land of The Living (1992), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [mantissa/mantissa\_logo\_minimal.png at master · jtheardw/mantissa · GitHub](https://github.com/jtheardw/mantissa/blob/master/logos/mantissa_logo_minimal.png)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [NaN from Wikipedia](https://en.wikipedia.org/wiki/NaN)
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [New Engine: Mantissa](https://kirill-kryukov.com/chess/discussion-board/viewtopic.php?t=13339) by [Jeremy Wright](index.php?title=Jeremy_Wright&action=edit&redlink=1 "Jeremy Wright (page does not exist)"), [CCRL Discussion Board](Computer_Chess_Forums "Computer Chess Forums"), September 19, 2021
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [mantissa/README.md at master · jtheardw/mantissa · GitHub](https://github.com/jtheardw/mantissa/blob/master/README.md)

**[Up one level](Engines "Engines")**







 
