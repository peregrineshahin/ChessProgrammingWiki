---
title: Titboards
---
**[Home](Home "Home") \* [Board Representation](Board_Representation "Board Representation") \* [Bitboards](Bitboards "Bitboards") \* [Sliding Piece Attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") \* Titboards**


**Titboards**,  

a bitboard-based [move generation](Move_Generation "Move Generation") technique invented by [Zach Wegner](Zach_Wegner "Zach Wegner") <a id="cite-note-1" href="#cite-ref-1">[1]</a>. Titboards are based on an extension of bitboards to ternary boards, hence the name ("bit" means binary digit, "tit" mean [ternary digit](https://en.wikipedia.org/wiki/Ternary_numeral_system)). Titboards are only used for move generation, not for any other purposes that typical bitboard attack-getters will be used for.


The idea of titboards is to eliminate [bitscans](BitScan "BitScan"). Typical bitboard move generation techniques generate a bitboard, intersect it with the set of allowable [squares](Squares "Squares") (empty or enemy-occupied), and then [serialize](Bitboard_Serialization "Bitboard Serialization") that into a list of moves. Titboards take a bitboard occupancy for each side for just one rank, file, or diagonal, and convert them to ternary representations and add them together. This index can determine which squares can actually be moved to, instead of just attacked. It is used in a lookup table of 3^7=2187 entries per [direction](Direction "Direction") per square.


Titboards are not typically used (there is no known engine that implements them). The reasons behind this are that they use a large amount of memory (more than [Magic Bitboards](Magic_Bitboards "Magic Bitboards")), and they must keep another attack generation method beside them due to their inflexibility. However, they are very fast, possibly the fastest bitboard-based move generator.






* [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006 » [Move Generation](Move_Generation "Move Generation")


 [Re: Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 01, 2006 <a id="cite-note-2" href="#cite-ref-2">[2]</a>
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&p=27838) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=8) by Tony P., [CCC](CCC "CCC"), January 28, 2020 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")

**[Up one level](Sliding_Piece_Attacks "Sliding Piece Attacks")**







 
