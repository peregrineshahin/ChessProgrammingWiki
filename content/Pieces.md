---
title: Pieces
---
**[Home](Home "Home") \* [Chess](Chess "Chess") \* Pieces**



[ [Pawn](Pawn "Pawn"), [Rook](Rook "Rook"), [Knight](Knight "Knight"), [Bishop](Bishop "Bishop"). [Queen](Queen "Queen"), and [King](King "King") <a id="cite-note-1" href="#cite-ref-1">[1]</a>
This is about [Chess Pieces](https://en.wikipedia.org/wiki/Chess_piece) of Classical or Orthodox Chess. Other chess variants introduce [Fairy chess pieces](https://en.wikipedia.org/wiki/Fairy_chess_piece) with different movement.


In chess terminology the term Piece is a bit ambiguous and may have different meanings - the term **Chess Men** is therefor often appropriate, since pieces otherwise don't include [Pawns](Pawn "Pawn") and even the [King](King "King"), but consider [minor pieces](https://en.wikipedia.org/wiki/Minor_piece#Minor_piece), [Knight](Knight "Knight") and [Bishop](Bishop "Bishop"), and the [major pieces](https://en.wikipedia.org/wiki/Minor_piece#Major_piece) (also heavy pieces), [Rook](Rook "Rook") and [Queen](Queen "Queen"). Rook, Bishop and Queen are so called [sliding pieces](Sliding_Pieces "Sliding Pieces"), since they may "slide" in appropriate ray-directions as far they like - as long they are not hindered (blocked) by own or opponent pieces (which they may capture), with implications on [move generation](Move_Generation "Move Generation") issues. 




### Contents


* [1 Piece Coding](#piece-coding)
	+ [1.1 Piece-Type Coding](#piece-type-coding)
	+ [1.2 Piece Type and Color](#piece-type-and-color)
	+ [1.3 Disjoint Piece Flags](#disjoint-piece-flags)
	+ [1.4 Encapsulation](#encapsulation)
	+ [1.5 Samples](#samples)
* [2 Value of Pieces](#value-of-pieces)
* [3 Tactical Properties](#tactical-properties)
* [4 Printing and Drawing](#printing-and-drawing)
	+ [4.1 ASCII Art](#ascii-art)
	+ [4.2 Unicode](#unicode)
* [5 See also](#see-also)
* [6 Forum Posts](#forum-posts)
* [7 External Links](#external-links)
* [8 References](#references)






There are six types of pieces for each side, in total twelve different men. Since only one piece may occupy one [square](Squares "Squares") at a time, one usually expands the range of piece codes with the Nil-Piece aka empty square, often encoded as zero. Depending on the [board representation](Board_Representation "Board Representation"), some programmers introduce an artificial blocking piece, which surrounds the embedded [8x8 boards](8x8_Board "8x8 Board") inside a [10x12 board](10x12_Board "10x12 Board") for cheaper off the board tests in offset [move generation](Move_Generation "Move Generation").


For cheaper extraction, most programmers prefer distinct coding of piece-types and the color of piece. Quite common is to use three bits to encode the piece-type plus one bit or [Two's Complement](General_Setwise_Operations#TheTwosComplement "General Setwise Operations") (not recommend for languages with zero based array indices, like [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java")) for the color.


Other programs distinguish not only piece-type and color, but enumerate all 32 pieces from their [initial position](Initial_Position "Initial Position"), which label or code does not change during the course of a game (even after a possible [promotion](Promotions "Promotions") of a pawn) and might be one-to-one associated with the bit-position of a 32-bit [piece set](Piece-Sets "Piece-Sets"), and/or are used to index a [piece list](Piece-Lists "Piece-Lists") containing the current [square](Squares "Squares") the piece resides on. 


[Lachex](Lachex "Lachex") for instance used following enumeration scheme: the a1-rook was labeled with 1, b1-knight with 2, a2-pawn with 9, the a8-rook with 17 and the h7-pawn with 32. Beside a [bitboard board-definition](Bitboard_Board-Definition "Bitboard Board-Definition") using 12 piece [bitboards](Bitboards "Bitboards") and [occupancy](Occupancy "Occupancy") as union set, Lachex used a redundant [8x8 board array](8x8_Board "8x8 Board"), containing those 1..32 piece-codes, but zero for empty squares. Another piece-array contained the associated piece-types or zero if the piece is missing <a id="cite-note-2" href="#cite-ref-2">[2]</a>.




### Piece-Type Coding


Any enumeration of piece-type codes is fine. [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller") proposed distinct white and black pawn codes inside the otherwise colorless range of piece-types, to take the different move-directions of pawns into account. This way piece-type completely specifies the mechanical move abilities, and three bits are still appropriate for a dense range to index tables or lookup-arrays, e.g. for [Piece Values](Material "Material") and that like. Often the order of enumeration is conform with the value of the pieces, for instance a [C++](Cpp "Cpp") enumeration:




```C++

enum EPieceType
{
   ept_pnil   = 0, // empty
   ept_wpawn  = 1,
   ept_bpawn  = 2,
   ept_knight = 3,
   ept_bishop = 4,
   ept_rook   = 5,
   ept_queen  = 6,
   ept_king   = 7,
};

```

### Piece Type and Color


One approach is to use negative values for black and positive for white (or color don't care) pieces. But if we like to index (zero based) [arrays](Array "Array") in [C](C "C"), [C++](Cpp "Cpp") or [Java](Java "Java") by piece codes an offset has to be considered - also the Two's Complement needs abs-functions or additional indirection to extract the pure piece code, rather than to mask (and eventually shift) three bits. That is why most programmers rely on positive ranges only and concatenate the three piece-type bits with one color-bit, for instance the color at the [big end](Big-endian "Big-endian").




```C++

 PieceCode:4 = 8 * Color:1 + PieceType:3;

```

In C++ as enumeration:




```C++

enum EPieceCode
{
   epc_empty   = ept_pnil,
   epc_wpawn   = ept_wpawn,
   epc_woff    = ept_bpawn, // may be used as off the board blocker in mailbox
   epc_wknight = ept_knight,
   epc_wbishop = ept_bishop,
   epc_wrook   = ept_rook,
   epc_wqueen  = ept_queen,
   epc_wking   = ept_king,

   epc_blacky  = 8, // color code, may used as off the board blocker in mailbox
   epc_boff    = ept_wpawn  + epc_blacky, // may be used as off the board blocker in mailbox
   epc_bpawn   = ept_bpawn  + epc_blacky,
   epc_bknight = ept_knight + epc_blacky,
   epc_bbishop = ept_bishop + epc_blacky,
   epc_brook   = ept_rook   + epc_blacky,
   epc_bqueen  = ept_queen  + epc_blacky,
   epc_bking   = ept_king   + epc_blacky,
};

```

To concatenate piece type and color the other way around is also quite common, color at the [little end](Little-endian "Little-endian").




```C++

 PieceCode:4 = 2 * PieceType:3 + Color:1;

```





### Disjoint Piece Flags


An alternative coding approach for most efficient inner loops with cheap test-instructions in scanning [board arrays](Board_Representation "Board Representation") in conjunction with [move generation](Move_Generation "Move Generation"), specially [captures](Captures "Captures"), is to encode pieces by five and up to eight disjoint bits (one [byte](Byte "Byte")). Each white and black piece has a disjoint color bit set, and appropriate bits may indicate a sliding piece, orthogonal or diagonal stepping or sliding etc.. One may even use one disjoint bit out of six per piece, yielding in exactly two bits set per regular piece code, for instance <a id="cite-note-3" href="#cite-ref-3">[3]</a>:





|  Bit
 |  Binary
 |  Semantic
 |
| --- | --- | --- |
|  0
 | `0000 0001` |  White
 |
|  1
 | `0000 0010` |  Black
 |
|  combined (ored with)
 |
|  2
 | `0000 0100` | [Pawn](Pawn "Pawn") |
|  3
 | `0000 1000` | [Knight](Knight "Knight") |
|  4
 | `0001 0000` | [Bishop](Bishop "Bishop") |
|  5
 | `0010 0000` | [Rook](Rook "Rook") |
|  6
 | `0100 0000` | [Queen](Queen "Queen") |
|  7
 | `1000 0000` | [King](King "King") |


### Encapsulation


There are a lot of possibilities to encode pieces, however surrounding source code should not directly rely on the binary representation and range of that codes, e.g. the semantic of a certain bit. In general, it is recommend to hide implementation details, likely in [C++](Cpp "Cpp") inside a wrapper class with inlined getter and setter, or in [C](C "C") a set of [C-Macros](index.php?title=C-Macros&action=edit&redlink=1 "C-Macros (page does not exist)") and functions that "wrap" an scalar integer type. A distinct type, e.g. a type definition in C/C++ is recommend for better compile time checking, other programmer still prefer (unsigned) integer types for passing pieces (and moves, colors and square coordinates) around.


On the other hand, one should not exaggerate abstraction, to be aware of an wrapped integer type is fine, and that bytes are appropriate to store an array of piece codes, which may easily zero-extended to wider types if passed via registers. If you intend to implement stuff like [Zillions of Games](https://en.wikipedia.org/wiki/Zillions_of_Games) or different [Fairy Chess](https://en.wikipedia.org/wiki/Fairy_chess) variants, it might be a reasonable idea, to design derived piece classes with virtual functions and late binding during runtime.



### Samples


* [Piece Coding in Gambiet](Gambiet#PieceCoding "Gambiet")


## Value of Pieces


* [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
* [Point Value](Point_Value "Point Value")


*and under the [Evaluation](Evaluation "Evaluation") topic:*



* [Evaluation of Pieces](Evaluation_of_Pieces "Evaluation of Pieces")
* [Material](Material "Material")
* [Mobility](Mobility "Mobility")
* [Trapped Pieces](Trapped_Pieces "Trapped Pieces")


## Tactical Properties


* [En prise](En_prise "En prise")
* [Hanging Piece](Hanging_Piece "Hanging Piece")
* [Loose Piece](Loose_Piece "Loose Piece")
* [Overloading](Overloading "Overloading")






## Printing and Drawing


* [Drawing Piece Sample Code](2D_Graphics_Board#Drawing "2D Graphics Board")
* [Boris Diplomat Chess Piece Font](David_Lindsay#ChessFont "David Lindsay") by [David Lindsay](David_Lindsay "David Lindsay")






### ASCII Art


[ASCII art](https://en.wikipedia.org/wiki/ASCII_art) chess pieces, collected by Andreas Freise <a id="cite-note-4" href="#cite-ref-4">[4]</a>:




```C++

                                .      +
       []       ()    _,,       ()     ()
       )(       )(   "-=\~      )(     )(       ()
       )(       )(     )(       )(     )(       )(
ejm97 /__\     /__\   /__\     /__\   /__\     /__\

                                .      +
       []       ()    _,,       ()     ()
       )(       )(   "-X\~      )(     )(       ()
       )(       )(     )(       )(     )(       )(
ejm97 /XX\     /XX\   /XX\     /XX\   /XX\     /XX\

```

[ASCII art](https://en.wikipedia.org/wiki/ASCII_art) [Staunton chess set](https://en.wikipedia.org/wiki/Staunton_chess_set) by David Moeser <a id="cite-note-5" href="#cite-ref-5">[5]</a>




```C++

    .::.
    _::_
  _/____\_        ()
  \      /      <~--~>
   \____/        \__/         <>_
   (____)       (____)      (\)  )                        __/"""\
    |  |         |  |        \__/      WWWWWW            ]___ 0  }
    |__|         |  |       (____)      |  |       __        /   }
   /    \        |__|        |  |       |  |      (  )     /~    }
  (______)      /____\       |__|       |__|       ||      \____/
 (________)    (______)     /____\     /____\     /__\     /____\
 /________\   (________)   (______)   (______)   (____)   (______)
    King        Queen       Bishop      Rook      Pawn     kNight

```

### Unicode


[Chess symbols](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) in [Unicode](https://en.wikipedia.org/wiki/Unicode), see also the [Unicode Board](2D_Graphics_Board#Unicode "2D Graphics Board").





|  Name  |  Symbol  |  Code point  |  HTML (dec)  |  HTML (hex)
 |
| --- | --- | --- | --- | --- |
|  White King  | ♔ | U+2654  |  &#9812;  |  &#x2654;
 |
|  White Queen  | ♕ | U+2655  |  &#9813;  |  &#x2655;
 |
|  White Rook  | ♖ | U+2656  |  &#9814;  |  &#x2656;
 |
|  White Bishop  | ♗ | U+2657  |  &#9815;  |  &#x2657;
 |
|  White Knight  | ♘ | U+2658  |  &#9816;  |  &#x2658;
 |
|  White Pawn  | ♙ | U+2659  |  &#9817;  |  &#x2659;
 |
|  Black King  | ♚ | U+265A  |  &#9818;  |  &#x265A;
 |
|  Black Queen  | ♛ | U+265B  |  &#9819;  |  &#x265B;
 |
|  Black Rook  | ♜ | U+265C  |  &#9820;  |  &#x265C;
 |
|  Black Bishop  | ♝ | U+265D  |  &#9821;  |  &#x265D;
 |
|  Black Knight  | ♞ | U+265E  |  &#9822;  |  &#x265E;
 |
|  Black Pawn  | ♟︎ | U+265F  |  &#9823;  |  &#x265F;
 |


## See also


* [Piece Drop](index.php?title=Piece_Drop&action=edit&redlink=1 "Piece Drop (page does not exist)")
* [Piece-Lists](Piece-Lists "Piece-Lists")
* [Piece Recognition](Piece_Recognition "Piece Recognition")
* [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards") for dense "vertical" piece code nibbles


## Forum Posts


* [Chess piece abbreviations](https://www.stmintz.com/ccc/index.php?id=176601) by [Bruce Moreland](Bruce_Moreland "Bruce Moreland"), [CCC](CCC "CCC"), June 23, 2001


## External Links


* [Chess piece from Wikipedia](https://en.wikipedia.org/wiki/Chess_piece)
* [Lewis chessmen from Wikipedia](https://en.wikipedia.org/wiki/Lewis_chessmen)
* [Staunton chess set from Wikipedia](https://en.wikipedia.org/wiki/Staunton_chess_set)
* [The House of Staunton - Chess Sets and Chess Boards - Manufacturer of the World's Finest Chess Sets and Chess Boards](http://www.houseofstaunton.com/)
* [Standards of Chess Equipment and tournament venue for FIDE Tournaments](http://www.fide.com/fide/handbook?id=16&view=category)
* [Phil Collins Big Band](https://en.wikipedia.org/wiki/The_Phil_Collins_Big_Band) - [Pick up the pieces](https://en.wikipedia.org/wiki/Pick_Up_the_Pieces_(Average_White_Band_song)), [Montreux Jazz Festival](https://en.wikipedia.org/wiki/Montreux_Jazz_Festival), [1998](https://en.wikipedia.org/wiki/List_of_performers_at_the_Montreux_Jazz_Festival#1998), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video


 feat.: [Phil Collins](Category:Phil_Collins "Category:Phil Collins"), [Gerald Albrigth](https://en.wikipedia.org/wiki/Gerald_Albright), [Sadao Watanabe](https://en.wikipedia.org/wiki/Sadao_Watanabe_(musician)), [Klaus Doldinger](Category:Klaus_Doldinger "Category:Klaus Doldinger"), [Pee Wee Ellis](https://en.wikipedia.org/wiki/Alfred_%22Pee_Wee%22_Ellis), [George Duke](Category:George_Duke "Category:George Duke"), [James Carter](https://en.wikipedia.org/wiki/James_Carter_(musician)), arranged and conducted by [Arif Mardin](https://en.wikipedia.org/wiki/Arif_Mardin)
 
## References


1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> An example of early-style [Staunton Chess Set](https://en.wikipedia.org/wiki/Staunton_chess_set) - Photo used by permission of [Frank A. Camaratta, Jr.](http://www.uschess.org/cc/absolute/camarattabio.php); [The House of Staunton, Inc.](https://en.wikipedia.org/wiki/House_of_Staunton); [houseofstaunton.com](http://www.houseofstaunton.com/), [Chess piece from Wikipedia](https://en.wikipedia.org/wiki/Chess_piece), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
2. <a id="cite-ref-2" href="#cite-note-2">[2]</a>  [Burton Wendroff](Burton_Wendroff "Burton Wendroff") (**1985**). *Attack Detection and Move Generation on the [X-MP/48](http://www.cisl.ucar.edu/computers/gallery/cray/xmp.jsp).* [ICCA Journal](ICGA_Journal "ICGA Journal"), Vol. 8, No. 2
3. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Fritz Reul](Fritz_Reul "Fritz Reul") (**2009**). *New Architectures in Computer Chess*, Ph.D. Thesis, *Chapter 2 Non-Bitboard Architectures*
4. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [chess - Ascii Art Dictionary](http://www.ascii-art.de/ascii/c/chess.txt) by [Andreas Freise](http://www.sr.bham.ac.uk/~adf/)
5. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [ASCII Chess Pieces](http://www.chessvariants.com/d.pieces/ascii.html) by [David Moeser](http://www.chessvariants.com/books.html#lotus)

**[Up one Level](Chess "Chess")**







 
