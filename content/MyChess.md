---
title: MyChess
---
**[Home](Home "Home") \* [Engines](Engines "Engines") \* MyChess**



 [](http://www.spacious-mind.com/html/commodore_c64_mychess_ii.html) MyChess II <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
**MyChess**,  

[David Kittinger's](David_Kittinger "David Kittinger") first chess program, developed in 1979 initially for the 8-Bit [Z80](Z80 "Z80") CPU written in [assembly](Assembly "Assembly") language to run under [CP/M](https://en.wikipedia.org/wiki/CP/M). It had its quite successful debut at the [ACM 1979](ACM_1979 "ACM 1979") and the [PCW-MCC 1979](PCW-MCC_1979 "PCW-MCC 1979") some days later, and further played the [MCC 1980](MCC_1980 "MCC 1980") and the [WCCC 1980](WCCC_1980 "WCCC 1980") supported by book-author [John Urwin](John_Urwin "John Urwin"), and the [ACM 1980](ACM_1980 "ACM 1980") and [ACM 1981](ACM_1981 "ACM 1981"). 


In 1981 Kittinger was hired by [Peter Auge](Peter_Auge "Peter Auge"), and MyChess was ported to [Novag's](Novag "Novag") [dedicated chess computers](Dedicated_Chess_Computers "Dedicated Chess Computers") <a id="cite-note-2" href="#cite-ref-2">[2]</a>, a tiny [Fairchild F8](Fairchild_F8 "Fairchild F8") based program for [Novag Micro Chess](Novag_Micro_Chess "Novag Micro Chess"), a smaller [6502](6502 "6502") based program for the [Super Sensor IV](index.php?title=Super_Sensor_IV&action=edit&redlink=1 "Super Sensor IV (page does not exist)"), and the [Z80](Z80 "Z80") program for [Savant](Savant "Savant") and the [Robot Adversary](Robot_Adversary "Robot Adversary"). 



### Contents


* [1 Description](#description)
	+ [1.1 Anatomy](#anatomy)
	+ [1.2 Move Generation](#move-generation)
* [2 Further Developments](#further-developments)
* [3 See also](#see-also)
* [4 Publications](#publications)
* [5 Forum Posts](#forum-posts)
* [6 External Links](#external-links)
* [7 References](#references)






### Anatomy


from *History and Anatomy of MYCHESS* by [David Kittinger](David_Kittinger "David Kittinger") <a id="cite-note-3" href="#cite-ref-3">[3]</a>:




```
MYCHESS uses an [iterative](Iterative_Deepening "Iterative Deepening") [Type A search](Type_A_Strategy "Type A Strategy"),  with [alpha-beta pruning](Alpha-Beta "Alpha-Beta") as well as the [killer](Killer_Heuristic "Killer Heuristic") and [capture heuristics](MVV-LVA "MVV-LVA"). It will predict its opponents best move, and start, [analyzing replies](Pondering "Pondering") while the opponent is still thinking. One [extra ply](Extensions "Extensions") is examined before backing up from a [best variation](Principal_Variation "Principal Variation") if the [side to move](Side_to_move "Side to move") can have anything captured. 

```


```
The desirability of a possible position is "[scored](Evaluation "Evaluation") " on the basis of [material](Material "Material") strength, using a ["swap off" evaluator](Static_Exchange_Evaluation "Static Exchange Evaluation") to resolve situations where something is under attack. If a decision can not be made using this score, then a secondary positional score is generated, which takes into account such features as [pawn structure](Pawn_Structure "Pawn Structure"), [piece placement](Piece-Square_Tables "Piece-Square Tables"), and [mobility](Mobility "Mobility"). When a possible position is found which is better than the current best variation, it is saved in the [ply table](Triangular_PV-Table "Triangular PV-Table") ; otherwise it is discarded. 

```

### Move Generation


MyChess focused on speed and had completely independent [move generation](Move_Generation "Move Generation") for white and black. As mentioned by its author, one of the funny things about MyChess is that it originally had two 16 byte [arrays](Array "Array") as [piece-list](Piece-Lists "Piece-Lists"), but fixed by the index, so that it could only [promote](Promotions "Promotions") a pawn to a captured piece <a id="cite-note-4" href="#cite-ref-4">[4]</a>. Continuation from *History and Anatomy of MYCHESS*: 


Moves are generated serially and only as necessary, to save time. The possible moves from a position are examined in the following [order](Move_Ordering "Move Ordering"):



1. [Best variation](PV-Move "PV-Move") from previous iteration
2. Winning or even [captures](Captures "Captures")
3. [Castle moves](Castling "Castling")
4. [En passant](En_passant "En passant") captures
5. [Killer moves](Killer_Move "Killer Move")
6. Two best regular moves from ply one
7. Losing capture moves ([sacrifices](Sacrifice "Sacrifice"))
8. Other moves


Pawn [promotions](Promotions "Promotions") are handled by the capture routines or regular pawn move routine, depending on whether the capture is made while promoting. Regular moves are generated piece by piece, starting with the king's rook pawn and ending with the king. 



## Further Developments


MyChess was further ported to the [6502](6502 "6502") and compatible CPUs to run on a [Commodore 64](Commodore_64 "Commodore 64") and [Commodore 128](Commodore_128 "Commodore 128") and market as *MyChess II* by [Beyond Software](https://en.wikipedia.org/wiki/Beyond_Software)<a id="cite-note-5" href="#cite-ref-5">[5]</a> , and also to the 16-Bit [8086](8086 "8086"), released by [Software Toolworks](index.php?title=Software_Toolworks&action=edit&redlink=1 "Software Toolworks (page does not exist)") in 1984 for the [IBM PC](IBM_PC "IBM PC") and [MS-DOS](MS-DOS "MS-DOS") operating system <a id="cite-note-6" href="#cite-ref-6">[6]</a>, forerunner of [Chessmaster 2000](Chessmaster#MyChess "Chessmaster"). The 6502 version was apparently also the base for [Novag's](Novag "Novag") [Constellation](Constellation "Constellation") and [Super Constellation](Super_Constellation "Super Constellation"). 



## See also


* [Chessmaster 2000](Chessmaster#MyChess "Chessmaster")
* [Constellation](Constellation "Constellation")
* [Super Constellation](Super_Constellation "Super Constellation")
* [WChess](WChess "WChess")


## Publications


* [John Urwin](John_Urwin "John Urwin") (**1979**). *Two New Programs Are Tested*. [Personal Computing, Vol. 3, No. 12](Personal_Computing#3_12 "Personal Computing"), pp. 71 » [Video Chess](Video_Chess "Video Chess")
* Editor (**1980**). *MyChess goes to college*. [Personal Computing, Vol. 4, No. 6](Personal_Computing#4_6 "Personal Computing"), pp. 91
* Editor (**1980**). *MyChess Shines*. [Personal Computing, Vol. 4, No. 11](Personal_Computing#4_11 "Personal Computing"), pp. 85
* [Harry Shershow](Harry_Shershow "Harry Shershow") (**1981**). *The MyChess-CSC Confrontation at San Jose*. [Personal Computing, Vol. 5, No. 1](Personal_Computing#5_1 "Personal Computing"), pp. 79 » [MCC 1980](MCC_1980 "MCC 1980")
* [John F. White](John_F._White "John F. White") (**1982**). *[Review-Chess Computers](http://yourcomputeronline.wordpress.com/2011/01/31/review-chess-computers/)*. [Your Computer](Your_Computer "Your Computer"), [March 1982](http://yourcomputeronline.wordpress.com/2011/01/30/march-1982-contents-and-editorial/)
* [Dave Kittinger](David_Kittinger "David Kittinger") (**1984**). *MyChess - Chess Playing Program*. [The Software Toolworks](index.php?title=Software_Toolworks&action=edit&redlink=1 "Software Toolworks (page does not exist)"), [pdf](http://heathkit.garlanger.com/library/TheSoftwareToolworks/software/manuals/210_Mychess.pdf) hosted by [garlanger.com](http://garlanger.com/Welcome.html)


## Forum Posts


* [Best way to run Mychess at the original speed (emulation)](http://www.talkchess.com/forum/viewtopic.php?t=14022) by Jonathan P., [CCC](CCC "CCC"), May 25, 2007
* [Hello all](http://www.talkchess.com/forum/viewtopic.php?t=43447) by [Dave Kittinger](David_Kittinger "David Kittinger"), [CCC](CCC "CCC"), April 25, 2012


## External Links


* [MyChess' ICGA Tournaments](https://www.game-ai-forum.org/icga-tournaments/program.php?id=424)
* [Download Chess Programs](http://www.top-5000.nl/cp.htm) hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
* [Classic Computer Chess - ... The programs of yesteryear](http://web.archive.org/web/20071221115817/http://classicchess.googlepages.com/Chess.htm) by [Carey](Carey_Bloodworth "Carey Bloodworth"), hosted by the [Internet Archive](https://en.wikipedia.org/wiki/Internet_Archive) <a id="cite-note-7" href="#cite-ref-7">[7]</a>
* [MYCHESS for DOS (1984)](http://www.mobygames.com/game/mychess) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
* [Mychess](http://www.hotud.org/component/content/article/37-strategy/21965) from [Home of the Underdogs](http://www.hotud.org/index.php?option=com_content&view=frontpage&Itemid=1)
* [Commodore 64/128 Old Computer Chess Game Collection - Mychess II](http://www.spacious-mind.com/html/commodore_c64_mychess_ii.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [Commodore 64 Emulator - Computer Chess Game Collection - Mychess II](http://www.spacious-mind.com/html/c64_emu_-_mychess_ii.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
* [The Software Toolworks - MyChess](http://heathkit.garlanger.com/library/TheSoftwareToolworks/software/mychess.shtml) by [garlanger.com](http://garlanger.com/Welcome.html)


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Commodore 64/128 Old Computer Chess Game Collection - Mychess II](http://www.spacious-mind.com/html/commodore_c64_mychess_ii.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Scisys and Novag : The Early Years](http://www.chesscomputeruk.com/html/scisys_and_novag___the_early_y.html) from [Chess Computer UK](http://www.chesscomputeruk.com/index.html) by [Mike Watters](Mike_Watters "Mike Watters")
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Dave Kittinger](David_Kittinger "David Kittinger") (**1984**). *MyChess - Chess Playing Program*. [The Software Toolworks](index.php?title=Software_Toolworks&action=edit&redlink=1 "Software Toolworks (page does not exist)"), [pdf](http://heathkit.garlanger.com/library/TheSoftwareToolworks/software/manuals/210_Mychess.pdf) hosted by [garlanger.com](http://garlanger.com/Welcome.html)
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [David Kittinger - Interview](http://kittinger.yolasite.com/) by [Bryan Whitby](index.php?title=Bryan_Whitby&action=edit&redlink=1 "Bryan Whitby (page does not exist)")
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Commodore 64/128 Old Computer Chess Game Collection - Mychess II](http://www.spacious-mind.com/html/commodore_c64_mychess_ii.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
6. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [MYCHESS for DOS (1984)](http://www.mobygames.com/game/mychess) from [MobyGames](https://en.wikipedia.org/wiki/MobyGames)
7. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Old programs CHAOS and USC](http://www.talkchess.com/forum/viewtopic.php?t=56938&start=2) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), July 11, 2015

**[Up one level](Engines "Engines")**







 
