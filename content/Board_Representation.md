---
title: Board Representation
---
**[Home](Home "Home") * Board Representation**

\[ [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Überschach, 1937 <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A chess program needs an internal **board representation** to maintain [chess positions](Chess_Position "Chess Position") for its [search](Search "Search"), [evaluation](Evaluation "Evaluation") and [game-play](Chess_Game "Chess Game"). Beside modelizing the [chessboard](Chessboard "Chessboard") with its [piece](Pieces "Pieces")-placement, some additional information is required to fully specify a chess position, such as [side to move](Side_to_move "Side to move"), [castling rights](Castling_Rights "Castling Rights"), possible [en passant](En_passant "En passant") target square and the number of [reversible moves](Reversible_Moves "Reversible Moves") to keep track on the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule").

To begin with, we further elaborate on the pure data structures to represent the board and its piece-placement. There are piece centric and square centric representations as well as hybrid solutions.

## Piece Centric

A **piece centric** representation keeps [lists](Linked_List "Linked List"), [arrays](Array "Array") or sets of all [pieces](Pieces "Pieces") still on the board - with the associated information which [square](Squares "Squares") they occupy. A popular piece centric representative is the set-wise [bitboard-approach](Bitboards "Bitboards"). One 64-bit word for each piece type, where one-bits associate their [occupancy](Occupancy "Occupancy").

- [Piece-Lists](Piece-Lists "Piece-Lists")
- [Piece-Sets](Piece-Sets "Piece-Sets")
- [Bitboards](Bitboards "Bitboards")

## Square Centric

The **square centric** representation implements the inverse association - is a [square](Squares "Squares") empty or is it [occupied](Occupancy "Occupancy") by a particular [piece](Pieces "Pieces")? The most popular square centric representations, [mailbox](Mailbox "Mailbox") or it's [0x88](0x88 "0x88")-enhancements - are basically [arrays](Array "Array") of direct [piece-codes](Pieces#PieceCoding "Pieces") including the empty square and probably out of board codes. Hybrid solutions may further refer piece-list entries.

- [Mailbox](Mailbox "Mailbox")
  - [8x8 Board](8x8_Board "8x8 Board")
  - [10x12 Board](10x12_Board "10x12 Board")
  - [Vector Attacks](Vector_Attacks "Vector Attacks")

## [0x88](0x88 "0x88") Hybrid Solutions

While different algorithms and tasks inside a chess program might prefer one of these associations, it is quite common to use redundant board representations with elements of both. Bitboard approaches often keep a 8x8 board to determine a piece by square, while square centric board array approaches typically keep [piece-lists](Piece-Lists "Piece-Lists") and/or [piece-sets](Piece-Sets "Piece-Sets") to avoid scanning the board for [move generation](Move_Generation "Move Generation") purposes.

## Move Generation

With a board representation, one big consideration is the generation of [moves](Moves "Moves"). This is essential to the [game playing](Chess_Game "Chess Game") aspect of a chess program, and it must be completely correct. Writing a good move generator is often the first basic step of creating a chess program.

- [Move Generation](Move_Generation "Move Generation")
- [Perft](Perft "Perft")

## Make and Unmake

- [Incremental Updates](Incremental_Updates "Incremental Updates")
- [Copy-Make](Copy-Make "Copy-Make")
- [Make Move](Make_Move "Make Move")
- [Unmake Move](Unmake_Move "Unmake Move")
- [Bitboard Update By Move](General_Setwise_Operations#UpdateByMove "General Setwise Operations")

## See Also

- [Array of Nibbles](Nibble#ArrayOfNibbles "Nibble")
- [Attack and Defend Maps](Attack_and_Defend_Maps "Attack and Defend Maps")
- [Chess Position](Chess_Position "Chess Position")
  - [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD)
  - [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN)
- [Chinese Chess Board Representation](Chinese_Chess_Board_Representation "Chinese Chess Board Representation")
- [Graphics Programming](Graphics_Programming "Graphics Programming")
- [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")

## Publications

- [Claude Shannon](Claude_Shannon "Claude Shannon") (**1949**). *[Programming a Computer for Playing Chess](http://www.pi.infn.it/%7Ecarosi/chess/shannon.txt)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon/2-0%20and%202-1.Programming_a_computer_for_playing_chess.shannon.062303002.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](http://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
- [Dan Spracklen](Dan_Spracklen "Dan Spracklen"), [Kathe Spracklen](Kathe_Spracklen "Kathe Spracklen") (**1978**). *First Steps in Computer Chess Programming*. [BYTE, Vol. 3, No. 10](Byte_Magazine#BYTE310 "Byte Magazine"), [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-4.First_Steps.Byte_Magazine/First_Steps_in_Computer_Chess_Programing.Spracklen-Dan_Kathe.Byte_Magazine.Oct-1978.062303035.sm.pdf) from [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
- [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2008**). *The Compact Chessboard Representation*. [ICGA Journal, Vol. 31, No. 3](ICGA_Journal#31_3 "ICGA Journal") » [Array of Nibbles](Nibble#ArrayOfNibbles "Nibble")
- [Vladan Vučković](Vladan_Vu%C4%8Dkovi%C4%87 "Vladan Vučković") (**2012**). *An Alternative Efficient Chessboard Representation based on 4-Bit Piece Coding*. [Yugoslav Journal of Operations Research, Vol. 22, No. 1](http://www.doiserbia.nb.rs/issue.aspx?issueid=1761), [pdf](http://www.doiserbia.nb.rs/img/doi/0354-0243/2012/0354-02431200011V.pdf)

## Forum Posts

## 1999

- [Datastructures in computer chess](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/2ffae88f631ac20d) by Gustav Grundin, [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 11, 1999
- [How do you represent chess boards in your chess programms](http://www.stmintz.com/ccc/index.php?id=69942) by Brian Nielsen, [CCC](CCC "CCC"), September 22, 1999
- [Re: How do you represent chess boards in your chess programms](http://www.stmintz.com/ccc/index.php?id=71016) by [Sven Reichard](Sven_Reichard "Sven Reichard"), [CCC](CCC "CCC"), September 29, 1999

## 2000 ...

- [Differences between 0x88 ,10x12 and Bitboards!?](http://www.stmintz.com/ccc/index.php?id=265915) by Axel Grüttner, [CCC](CCC "CCC"), November 19, 2002
- [Fruit's Board Representation?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=2407&p=11195) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [Winboard Programming Forum](Computer_Chess_Forums "Computer Chess Forums"), April 27, 2005
- [Board representation : 0x88 or 10x12 ?](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=4442) by Philippe, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 02, 2006
- [Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623) by [Zach Wegner](Zach_Wegner "Zach Wegner"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 22, 2006 » [Titboards](Titboards "Titboards")

[Re: Yet another new bitboard move generation method](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5623&start=6) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), October 01, 2006 <a id="cite-note-2" href="#cite-ref-2">[2]</a>

- [Board Types in '08](http://www.talkchess.com/forum/viewtopic.php?t=22023) by [Joshua Shriver](index.php?title=Joshua_Shriver&action=edit&redlink=1 "Joshua Shriver (page does not exist)"), [CCC](CCC "CCC"), June 28, 2008

## 2010 ...

- [I'm Puzzled - Storing Piece Info & Magic Move Gen...](http://www.talkchess.com/forum/viewtopic.php?t=47615) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), March 27, 2013
- [Table-less bitboards (bitrays?)](http://www.talkchess.com/forum/viewtopic.php?t=48324) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), June 18, 2013
- [Best Board Representation for 32bit CPUs](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=52878) by net, [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), July 14, 2013
- [Some questions from a beginner](http://talkchess.com/forum/viewtopic.php?t=59691) by Tim Hagen, [CCC](CCC "CCC"), March 30, 2016
- [best board representation for variants (javascript) ?](http://www.talkchess.com/forum/viewtopic.php?t=65962) by [Mahmoud Uthman](index.php?title=Mahmoud_Uthman&action=edit&redlink=1 "Mahmoud Uthman (page does not exist)"), [CCC](CCC "CCC"), December 10, 2017 » [JavaScript](JavaScript "JavaScript"), [Chess Variants](Games#ChessVariants "Games")
- [CCR board representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=69046) by [Maksim Korzh](Maksim_Korzh "Maksim Korzh"), [CCC](CCC "CCC"), November 25, 2018 » [Array of Nibbles](Nibble#ArrayOfNibbles "Nibble")

## External Links

- [Board representation (chess) from Wikipedia](http://en.wikipedia.org/wiki/Board_representation_%28chess%29)
- [Chapter 3: Board Games - 3.1 CHESS](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/p003.htm) from [Alex Bell](Alex_Bell "Alex Bell") (**1972**). *[Games Playing with Computers](http://www.chilton-computing.org.uk/acl/literature/books/gamesplaying/overview.htm)*. [Allen & Unwin](http://en.wikipedia.org/wiki/Allen_%26_Unwin), ISBN-13: 978-0080212227
- [Chess board representations](http://www.craftychess.com/hyatt/boardrep.html) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt")
- [Board representations | Lecture notes](http://www.ics.uci.edu/~eppstein/180a/970408.html) by [David Eppstein](David_Eppstein "David Eppstein"), April 8, 1997
- [Chess Programming - The Chess Board](http://www.fam-petzke.de/cp_board_en.shtml) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke")
- [Representation of Chess Game - Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/Representation_of_Chess_Game), [University of Maribor](University_of_Maribor "University of Maribor")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Paul Klee](Category:Paul_Klee "Category:Paul Klee") - Ueberschach, 1937, [[1]](https://commons.wikimedia.org/wiki/File:Paul_Klee_Ueberschach.jpg) [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons), [Kunsthaus Zürich](https://en.wikipedia.org/wiki/Kunsthaus_Z%C3%BCrich)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: multi-dimensional piece/square tables](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52861&start=8) by Tony P., [CCC](CCC "CCC"), January 28, 2020

**[Up one Level](Home "Home")**

