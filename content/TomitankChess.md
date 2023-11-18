---
title: TomitankChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* tomitankChess**


**tomitankChess**,  

an [open source chess engine](Category:Open_Source "Category:Open Source") by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics") written in [JavaScript](JavaScript "JavaScript"), licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation").
tomitankChess was first released as version 1.4 in September 2017 <a id="cite-note-1" href="#cite-ref-1">[1]</a>. 
The js source code was initially [obfuscated](https://en.wikipedia.org/wiki/Obfuscation_(software))
<a id="cite-note-2" href="#cite-ref-2">[2]</a>
<a id="cite-note-3" href="#cite-ref-3">[3]</a>, 
but published as human readable source a few days later 
<a id="cite-note-4" href="#cite-ref-4">[4]</a>. 
tomitankChess uses the [Node.js](https://en.wikipedia.org/wiki/Node.js) JavaScript runtime <a id="cite-note-5" href="#cite-ref-5">[5]</a> to implement [UCI](UCI "UCI").
tomitankChess is available as [mobile app](https://en.wikipedia.org/wiki/Mobile_app) **Chess** or **Sakk** under [iOS](index.php?title=IOS&action=edit&redlink=1 "IOS (page does not exist)") and [Android](Android "Android"), the **Pro** versions at a not too cheap price <a id="cite-note-6" href="#cite-ref-6">[6]</a>.



### [Board Representation](Board_Representation "Board Representation")


* [Bitboards](Bitboards "Bitboards") (tomitankChess 2.0)
* [Blockers and Beyond](Blockers_and_Beyond "Blockers and Beyond")
* [Piece-Lists](Piece-Lists "Piece-Lists")


### [Search](Search "Search")


* [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
* [Fail-Soft](Fail-Soft "Fail-Soft") [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
* [Transposition Table](Transposition_Table "Transposition Table")
* [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
* [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
* [Late Move Pruning](Futility_Pruning#MoveCountBasedPruning "Futility Pruning")
* [Razoring](Razoring "Razoring")
* [Futility Pruning](Futility_Pruning "Futility Pruning")
* [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
* [Static Null Move Pruning](Reverse_Futility_Pruning "Reverse Futility Pruning") (Reverse Futility Pruning)
* [Quiescence Search](Quiescence_Search "Quiescence Search")


 [Delta Pruning](Delta_Pruning "Delta Pruning")
 [SEE Pruning](Static_Exchange_Evaluation "Static Exchange Evaluation")
### [Evaluation](Evaluation "Evaluation")


* [Neural Networks](Neural_Networks "Neural Networks") (5.0)
* [Tapered Eval](Tapered_Eval "Tapered Eval")
* [Material](Material "Material")
* [Bishop Pair](Bishop_Pair "Bishop Pair")
* [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
* [Mobility](Mobility "Mobility")
	+ [Trapped Pieces](Trapped_Pieces "Trapped Pieces")
	+ [Rooks on (Semi) Open Files](Rook_on_Open_File "Rook on Open File")
	+ [Rook on Seventh](Rook_on_Seventh "Rook on Seventh")
* [Outposts](Outposts "Outposts")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
	+ [Pawn Hash Table](Pawn_Hash_Table "Pawn Hash Table")
	+ [Backward Pawn](Backward_Pawn "Backward Pawn")
	+ [Connected Pawns](Connected_Pawns "Connected Pawns")
	+ [Doubled Pawn](Doubled_Pawn "Doubled Pawn")
	+ [Isolated Pawn](Isolated_Pawn "Isolated Pawn")
	+ [Passed Pawn](Passed_Pawn "Passed Pawn")
	+ [Unstoppable Passer](Unstoppable_Passer "Unstoppable Passer")
* [King Safety](King_Safety "King Safety")
	+ [Attacking King Zone](King_Safety#Attacking "King Safety")
	+ [Pawn Shelter](King_Safety#PawnShield "King Safety")
* [Tempo](Tempo "Tempo")
* [Automated Tuning](Automated_Tuning "Automated Tuning") by [Logistic Regression](Automated_Tuning#LogisticRegression "Automated Tuning")


## Forum Posts


### 2017 ...


* [JavaScript Pawn Bitboard (with 32 bit integers)](http://www.talkchess.com/forum/viewtopic.php?t=65198) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 17, 2017
* [tomitankChess - New JavaScript engine](http://www.talkchess.com/forum/viewtopic.php?t=65200) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 17, 2017
* [Strongest JavaScript Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=65344) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 30, 2017
* [tomitankChess v.1.5](http://www.talkchess.com/forum/viewtopic.php?t=65899) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), December 03, 2017
* [tomitankChess 2.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=67954) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), July 11, 2018
* [tomitankChess 2.1](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69059) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), November 26, 2018
* [tomitankChess 3.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69596) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), January 14, 2019


### 2020 ...


* [tomitankChess 4.0](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72894) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), January 24, 2020
* [Mobile application](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73377) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), March 15, 2020
* [tomitankChess 4.2](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=75188) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 23, 2020
* [tomitankChess 5.0 with NN](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=76359) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), January 18, 2021


## External Links


* [GitHub - tomitank/tomitankChess: Hungarian JavaScript Chess Engine](https://github.com/tomitank/tomitankChess)
* [Chess - Apps on Google Play](https://play.google.com/store/apps/details?id=sakk.tanky.hu&hl=en)
* [Chess Pro - Apps on Google Play](https://play.google.com/store/apps/details?id=sakk.tanky.hu.premium)
* [Sakk on the App Store](https://apps.apple.com/us/app/sakk/id1150654415)
* [Sakk Pro on the App Store](https://apps.apple.com/us/app/sakk-pro/id1152837781)
* [tomitankChess](http://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=tomitankChess&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/15](CCRL "CCRL")


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [tomitankChess - New JavaScript engine](http://www.talkchess.com/forum/viewtopic.php?t=65200) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 17, 2017
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Javascript-Obfuscator.aspx](http://www.javascriptobfuscator.com/Javascript-Obfuscator.aspx)
3. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Re: tomitankChess - New JavaScript engine](http://www.talkchess.com/forum/viewtopic.php?t=65200&start=14) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 21, 2017
4. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Strongest JavaScript Chess Engine](http://www.talkchess.com/forum/viewtopic.php?t=65344) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), September 30, 2017
5. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Node.js](https://nodejs.org/en/)
6. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Mobile application](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=73377) by [Tamás Kuzmics](Tam%C3%A1s_Kuzmics "Tamás Kuzmics"), [CCC](CCC "CCC"), March 15, 2020
7. <a id="cite-ref-7" href="#cite-note-7">↑</a> Features based on [tomitankChess/README.md at master · tomitank/tomitankChess · GitHub](https://github.com/tomitank/tomitankChess/blob/master/README.md) and tomitankChess 4.2

**[Up one Level](Engines "Engines")**







 
