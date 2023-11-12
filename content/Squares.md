---
title: Squares
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* Squares**



[ [Piet Mondrian](Category:Piet_Mondrian "Category:Piet Mondrian") - Tableau I <a id="cite-note-1" href="#cite-ref-1">[1]</a>
A **Square** in chess is one of 64 elements of a [chessboard](Chessboard "Chessboard"), which might be empty or [occupied](Occupancy "Occupancy") by a chess [man](Pieces "Pieces"). **Square centric** [representations](Board_Representation "Board Representation"), like [mailbox](Mailbox "Mailbox") or [0x88](0x88 "0x88") board [arrays](Array "Array"), contain [piece codes](Pieces#PieceCoding "Pieces"), the information, what piece, if any, resides on a particular square. The **piece centric** [bitboard](Bitboards "Bitboards"), as array of 64 bits, represent a boolean property of each square by a single bit. 


Depending on the underlying data structure of the [board representation](Board_Representation "Board Representation"), each square has an [address](https://en.wikipedia.org/wiki/Memory_address) inside the [board](Chessboard "Chessboard"). Square centric representations keep arrays of squares, containing the information which piece (if any) resides on each square. That is why these representation is often called [mailbox](Mailbox "Mailbox") approach, since each square has a associated mailbox which is either empty or contains a chess piece. To find the address of a certain square index in the a1..h8 aka 0..63 range sometimes requires additional computation or lookup, for instance to map coordinates for [0x88](0x88 "0x88") boards or surrounded mailbox boards.


In [bitboards](Bitboards "Bitboards") the address of a square correspondents to a bit-index, containing a boolean property of that square (bit set), or not (bit clear). The [square mapping](Square_Mapping_Considerations "Square Mapping Considerations") determines how bit-indices associate the squares on the [board](Chessboard "Chessboard"). 



## Algebraic Square Notation


In [algebraic chess notation](Algebraic_Chess_Notation "Algebraic Chess Notation") a [target square](Target_Square "Target Square") of a [move](Moves "Moves") is specified by two characters for its [cartesian coordinate](https://en.wikipedia.org/wiki/Cartesian_coordinates), per convention a letter for the [file](Files "Files") ('a'-'h'), followed by a digit for the [rank](Ranks "Ranks") number ('1'-'8').



## Square Definition


A typical [little-endian](Little-endian "Little-endian") rank-file mapping enumeration in [C++](Cpp "Cpp"):




```C++

enum enumSquare {
  a1, b1, c1, d1, e1, f1, g1, h1,
  a2, b2, c2, d2, e2, f2, g2, h2,
  a3, b3, c3, d3, e3, f3, g3, h3,
  a4, b4, c4, d4, e4, f4, g4, h4,
  a5, b5, c5, d5, e5, f5, g5, h5,
  a6, b6, c6, d6, e6, f6, g6, h6,
  a7, b7, c7, d7, e7, f7, g7, h7,
  a8, b8, c8, d8, e8, f8, g8, h8
};

```

## Square Properties


* [Center Distance](Center_Distance "Center Distance")
* [Center Manhattan-Distance](Center_Manhattan-Distance "Center Manhattan-Distance")
* [Color of a Square](Color_of_a_Square "Color of a Square")
* [Occupancy](Occupancy "Occupancy")
* [Square Attacked By](Square_Attacked_By "Square Attacked By")
* [Square Control](Square_Control "Square Control")


## Multiple Squares


### Lines


* [Ranks](Ranks "Ranks")
* [Files](Files "Files")
* [Diagonals](Diagonals "Diagonals")
* [Anti-Diagonals](Anti-Diagonals "Anti-Diagonals")
* [Rays](Rays "Rays") as subset of Lines
* [Line-masks](On_an_empty_Board#LineAttacks "On an empty Board") from [Bitboards](Bitboards "Bitboards")


### Two squares


Often, but not always related to a [move](Moves "Moves")



* [Origin Square](Origin_Square "Origin Square")
* [Target Square](Target_Square "Target Square")
* [Distance](Distance "Distance")
* [Manhattan-Distance](Manhattan-Distance "Manhattan-Distance")
* [Knight-Distance](Knight-Distance "Knight-Distance")
* [Direction](Direction "Direction")
* [0x88 Square Relations](0x88#SquareRelations "0x88")
* [In Between](Square_Attacked_By#InBetween "Square Attacked By")
* [Intersection Squares](Intersection_Squares "Intersection Squares")
* [Butterfly Boards](Butterfly_Boards "Butterfly Boards")
* [Two Squares on a File](Files#TwoSquares "Files")
* [Two Squares on a Rank](Ranks#TwoSquares "Ranks")
* [Two Squares on a Diagonal](Diagonals#TwoSquares "Diagonals")
* [Two Squares on a Anti-Diagonal](Anti-Diagonals#TwoSquares "Anti-Diagonals")


### Areas


* [Center](Center "Center")
* [Wings](index.php?title=Wings&action=edit&redlink=1 "Wings (page does not exist)")


### The whole Board


Lists, Arrays and Sets of Squares



* [Chessboard](Chessboard "Chessboard")
* [Board Representation](Board_Representation "Board Representation")
	+ [Mailbox](Mailbox "Mailbox")
	+ [Vector Attacks](Vector_Attacks "Vector Attacks")
	+ [Bitboards](Bitboards "Bitboards")
		- [Flipping Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating")
		- [Square Mapping Considerations](Square_Mapping_Considerations "Square Mapping Considerations")
		- [Setwise Rule of the Square](King_Pattern#SetwiseRuleoftheSquare "King Pattern")
	+ [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards")


## Pawn Squares


* [En passant](En_passant "En passant")
	+ [En passant target square](Forsyth-Edwards_Notation#Enpassanttargetsquare "Forsyth-Edwards Notation") inside the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
* [Promotion Square](Promotion_Square "Promotion Square")
* [Stop Square](Stop_Square "Stop Square")
* [Stop and Telestop](Pawn_Spans#StopandDistantStop "Pawn Spans")


## See also


* [Corresponding Squares](Corresponding_Squares "Corresponding Squares")


## External Links


* [Square from Wikipedia](https://en.wikipedia.org/wiki/Square)
* [Magic square from Wikipedia](https://en.wikipedia.org/wiki/Magic_square)
* [The Euler's 8x8 magic square](http://www.chess.com/article/view/the-eulers-8x8-magic-square), [Chess.com](index.php?title=Chess.com&action=edit&redlink=1 "Chess.com (page does not exist)")


## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Piet Mondrian](Category:Piet_Mondrian "Category:Piet Mondrian") - [Tableau I](https://commons.wikimedia.org/wiki/File:Tableau_I,_by_Piet_Mondriaan.jpg), 1921, [Gemeentemuseum Den Haag](https://en.wikipedia.org/wiki/Gemeentemuseum_Den_Haag)

**[Up one Level](Chess "Chess")**







 
