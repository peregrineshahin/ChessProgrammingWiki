---
title: Legal Move
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* [Moves](Moves "Moves") \* Legal Move**



 [](https://fineartamerica.com/featured/the-king-can-never-be-captured-marina-kalinovsky.html) [Marina Kalinovsky](Category:Marina_Kalinovsky "Category:Marina Kalinovsky") - The King can never be Captured <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
A **Legal Move** is a [pseudo-legal move](Pseudo-Legal_Move "Pseudo-Legal Move") which does not leave its own [king](King "King") in [check](Check "Check"). If not in check, most programs delay the legality test to the child node, after [incremental updates](Incremental_Updates "Incremental Updates") [attack and defend maps](Attack_and_Defend_Maps "Attack and Defend Maps") or an explicit [square attacked test](Square_Attacked_By "Square Attacked By") direct after [make move](Make_Move "Make Move"). Earlier programs were even more "lazy", to determine illegal moves after an illegal king capture, while many programs consider [absolutely pinned](Pin#AbsolutePin "Pin") pieces in [move generation](Move_Generation "Move Generation") and also for [evaluation](Evaluation "Evaluation") purpose, or even perform a strictly legal generation to demand searching legal positions. If in check, most programs apply a special move generator to omit the majority of illegal moves. 




### Not in Check


* The moving piece is not [absolutely pinned](Pin#AbsolutePin "Pin") on its [move direction](Direction "Direction")
* [En passant](En_passant "En passant") requires special horizontal pin test of both involved pawns, which disappear from the same [rank](Ranks "Ranks")
* While [castling](Castling "Castling"), [rook](Rook "Rook") is not pinned horizontally in [Chess960](Chess960 "Chess960")


### King in Check


### [Double Check](Double_Check "Double Check")


* Only king moves to non attacked squares, sliding check x-rays the king


### [Single Check](Check "Check")


* Capture of checking piece. The capturing piece is not [absolutely pinned](Pin#AbsolutePin "Pin")
* King moves to non attacked squares, sliding check x-rays the king
* Interposing moves in case of distant sliding check. The moving piece is not absolutely pinned.


## See also


* [DirGolem](DirGolem "DirGolem")
* [Hash Move](Hash_Move "Hash Move")
* [Killer Move](Killer_Move "Killer Move")
* [Mate Killers](Mate_Killers "Mate Killers")
* [Move Generation](Move_Generation "Move Generation")
* [Pseudo-Legal Move](Pseudo-Legal_Move "Pseudo-Legal Move")
* [Pseudo Legality Test](Square_Attacked_By#LegalityTest "Square Attacked By") with [Bitboards](Bitboards "Bitboards")


## Forum Posts


* [Question about testing legality of moves](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=53063) by ambrooks1, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 07, 2014
* [En-passant legality test](http://www.open-chess.org/viewtopic.php?f=5&t=2697) by tetra, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 07, 2014 » [En passant](En_passant "En passant")
* [TTMove legality checking ? & Killers Move Format?](http://www.talkchess.com/forum/viewtopic.php?t=63090) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), February 08, 2017 » [Hash Move](Hash_Move "Hash Move"), [Killer Move](Killer_Move "Killer Move")
* [I just discovered a design flaw in my engine](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73479) by [Michael Sherwin](Michael_Sherwin "Michael Sherwin"), [CCC](CCC "CCC"), March 27, 2020
* [Efficiently Generated Legal moves question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77671) by Pedro Duran, [CCC](CCC "CCC"), July 08, 2021 » [Move Generation](Move_Generation "Move Generation")


## External Links


* [Generating Legal Chess Moves Efficiently](https://peterellisjones.com/posts/generating-legal-chess-moves-efficiently/) by [Peter Ellis Jones](index.php?title=Peter_Ellis_Jones&action=edit&redlink=1 "Peter Ellis Jones (page does not exist)"), February 09, 2017


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [The King can never be Captured by Marina Kalinovsky, Artwork for Sale - Brooklyn, NY - United States](https://fineartamerica.com/featured/the-king-can-never-be-captured-marina-kalinovsky.html)

**[Up one Level](Moves "Moves")**







 
