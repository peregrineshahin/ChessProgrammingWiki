---
title: Pawn Pattern and Properties
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* Pawn Pattern and Properties**



 [](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbc) [Samuel Bak](Category:Samuel_Bak "Category:Samuel Bak") - Hero <a id="cite-note-1" href="#cite-ref-1">[1]</a> 
There are two approaches to determine [pawn](Pawn "Pawn") attack-sets, pawn move target squares or pawn-structure properties - using a single pawn or set-wise with multiple pawns. Since we have up to eight pawns per side, the set-wise approach has some merits. Disadvantage of set-wise operations is, we likely need different code for white and black pawns, while pre-calculated lookups by color and square allows to write more general code. 



## Properties


Properties about the [pawn structure](Pawn_Structure "Pawn Structure") are likely subject of [evaluation](Evaluation "Evaluation").



### Pawns in touch


* [Pawn Rams](Pawn_Rams_(Bitboards) "Pawn Rams (Bitboards)")
* [Pawn Levers](Pawn_Levers_(Bitboards) "Pawn Levers (Bitboards)")
* [Defended Pawns](Defended_Pawns_(Bitboards) "Defended Pawns (Bitboards)")
* [Duo Trio Quart](Duo_Trio_Quart_(Bitboards) "Duo Trio Quart (Bitboards)")


### Fills and Spans


* [Pawn Fills](Pawn_Fills "Pawn Fills") are about Front-, Rear- and Filefills
* [Pawns and Files](Pawns_and_Files_(Bitboards) "Pawns and Files (Bitboards)") about closed, open and halfopen files
* [Pawn Spans](Pawn_Spans "Pawn Spans") are about Front-, Rear- and Interspans - Stop and Telestop
* [Attack Spans](Attack_Spans "Attack Spans")


### Based on Spans


* [Double and Triple](Double_and_Triple_(Bitboards) "Double and Triple (Bitboards)")
* [Pawn Islands](Pawn_Islands_(Bitboards) "Pawn Islands (Bitboards)")
* [Dispersion and Distortion](Dispersion_and_Distortion "Dispersion and Distortion")
* [Isolated Pawns](Isolated_Pawns_(Bitboards) "Isolated Pawns (Bitboards)")
* [Unfree Pawns](Unfree_Pawns_(Bitboards) "Unfree Pawns (Bitboards)")
* [Open Pawns](Open_Pawns_(Bitboards) "Open Pawns (Bitboards)")
* [Passed Pawns](Passed_Pawns_(Bitboards) "Passed Pawns (Bitboards)")
* [Candidates](Candidates_(Bitboards) "Candidates (Bitboards)")
* [Backward Pawns](Backward_Pawns_(Bitboards) "Backward Pawns (Bitboards)")


## See also


* [Pawn Center](Pawn_Center "Pawn Center")
* [Pawn Structure](Pawn_Structure "Pawn Structure")
* [PawnKing](PawnKing "PawnKing")


## Publications


* [Hans Kmoch](Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959
* [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov") (**2017**). *Pawns*. [amazon](https://www.amazon.com/Pawns-Lyudmil-Tsvetkov-ebook/dp/B074S2MYQV)


## Forum Posts


* [how to detect information about pawn structure based on bitboard](https://www.stmintz.com/ccc/index.php?id=271055) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), December 17, 2002
* [Pawn Pattern Matching](http://www.talkchess.com/forum/viewtopic.php?t=20729) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), [CCC](CCC "CCC"), April 18, 2008
* [Pawn move generation in bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72461) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), November 29, 2019


 [Re: Pawn move generation in bitboards](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72461&start=3) by [Álvaro Begué](%C3%81lvaro_Begu%C3%A9 "Álvaro Begué"), [CCC](CCC "CCC"), December 05, 2019 » [C++](Cpp "Cpp")
## External Links


* [Pawn Power in Chess by Hans Kmoch - Glossary of Terms - Chess Forums](https://www.chess.com/forum/view/chess-equipment/pawn-power-in-chess-by-hans-kmoch-glossary-of-terms) - [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)") <a id="cite-note-2" href="#cite-ref-2">[2]</a>
* [Pawn structure](https://en.wikipedia.org/wiki/Pawn_structure) pattern of common [chess openings](https://en.wikipedia.org/wiki/Chess_opening)
* [The Game of Chess: Pawns and Their Related Terms](http://www.justchess.biz/chesspawns.htm) from [Just Chess .biz](http://www.justchess.biz/)


## References


1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess in the Art of Samuel Bak](http://chgs.elevator.umn.edu/asset/viewAsset/57f3b6787d58ae5f74bf8ba9#57f3b6d77d58ae5574bf8bbc), [Center for Holocaust & Genocide Studies](http://www.chgs.umn.edu/), [University of Minnesota](University_of_Minnesota "University of Minnesota")
2. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Hans Kmoch](Hans_Kmoch "Hans Kmoch") (**1959, 1990**). *Pawn Power in Chess*. New York: Dover, 1990. Previous ed.: New York: McKay, 1959. ISBN 0-486-26486-6

**[Up one Level](Bitboards "Bitboards")**







 
