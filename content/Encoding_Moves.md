---
title: Encoding Moves
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Moves](Moves "Moves") * Encoding Moves**

\[ [Daoist](https://en.wikipedia.org/wiki/Taoism) [Bagua](https://en.wikipedia.org/wiki/Bagua) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Encoding Moves** inside a chess program refers to both [game records](Chess_Game#GameRecord "Chess Game") or [game notation](Game_Notation "Game Notation"), and [search](Search "Search") related [generation](Move_Generation "Move Generation"), [make](Make_Move "Make Move") and [unmake move](Unmake_Move "Unmake Move") to [incremental update](Incremental_Updates "Incremental Updates") the [board](Chessboard "Chessboard"). During generation, moves are stored inside [move lists](Move_List "Move List"), and [best moves](Best_Move "Best Move") or [refutation moves](Refutation_Move "Refutation Move") [failing high](Fail-High "Fail-High") inside the [search](Search "Search") are stored inside the [transposition table](Transposition_Table "Transposition Table"), [Killer slots](Killer_Heuristic "Killer Heuristic"), [PV-](Triangular_PV-Table "Triangular PV-Table") or [refutation table](Refutation_Table "Refutation Table"), and moves, or certain aspects of a move, such as [origin square](Origin_Square "Origin Square") and the [target square](Target_Square "Target Square") are used to index [butterfly boards](Butterfly_Boards "Butterfly Boards") for [history](History_Heuristic "History Heuristic")- or [countermove heuristic](Countermove_Heuristic "Countermove Heuristic").

## Space-Time Tradeoff

Move encoding in [game records](Chess_Game#GameRecord "Chess Game") and [game databases](Databases "Databases") is usually designed to minimize size, while in [search](Search "Search") efficiency in generating is the main concern, considering [board representation](Board_Representation "Board Representation") and other data structures like [attack and defend maps](Attack_and_Defend_Maps "Attack and Defend Maps"). In general, move encoding either comprehend full information, that is contains involved [pieces](Pieces "Pieces") and square coordinates, or more common, omits the redundant piece information and relies on a adequate board representation to lookup the pieces by square. In [Alpha-Beta](Alpha-Beta "Alpha-Beta") like search, an important consideration is lazy move generation, to delay acquisition of certain information until it is really needed, which might be never in case of [Cut-nodes](Node_Types#cut-nodes "Node Types").

## Information Required

## From-To Based

The information required to uniquely describe a move is the [initial square](Origin_Square "Origin Square"), also called from-, origin- or departure square, and the [target square](Target_Square "Target Square"), also called to- or destination square, and in case of [promotions](Promotions "Promotions") the promoted piece code. While this from-to information is also sufficient for [castling](Castling "Castling") in standard chess, due to the otherwise impossible double king step, it might not in [Chess960](Chess960 "Chess960"). Therefore and also for efficiency reasons, castles are tagged as "special" moves. Such a move encoding conveniently fits inside a 16-bit [word](Word "Word"), 6 bits for from-to square each to index a [butterfly board](Butterfly_Boards "Butterfly Boards"), still leaves a [nibble](Nibble "Nibble") for flags for move kind and promoted piece code, for instance this arbitrary flags:

|  code
|  promotion
|  capture
|  special 1
|  special 0
|  kind of move
|
| --- | --- | --- | --- | --- | --- |
|  0
|  0
|  0
|  0
|  0
| [quiet moves](Quiet_Moves "Quiet Moves") |
|  1
|  0
|  0
|  0
|  1
| [double pawn push](Pawn_Push#DoublePush "Pawn Push") |
|  2
|  0
|  0
|  1
|  0
| [king castle](Castling "Castling") |
|  3
|  0
|  0
|  1
|  1
| [queen castle](Castling "Castling") |
|  4
|  0
|  1
|  0
|  0
| [captures](Captures "Captures") |
|  5
|  0
|  1
|  0
|  1
| [ep-capture](En_passant "En passant") |
|  8
|  1
|  0
|  0
|  0
| [knight-promotion](Promotions "Promotions") |
|  9
|  1
|  0
|  0
|  1
| [bishop-promotion](Promotions "Promotions") |
|  10
|  1
|  0
|  1
|  0
| [rook-promotion](Promotions "Promotions") |
|  11
|  1
|  0
|  1
|  1
| [queen-promotion](Promotions "Promotions") |
|  12
|  1
|  1
|  0
|  0
|  knight-promo capture
|
|  13
|  1
|  1
|  0
|  1
|  bishop-promo capture
|
|  14
|  1
|  1
|  1
|  0
|  rook-promo capture
|
|  15
|  1
|  1
|  1
|  1
|  queen-promo capture
|

## Extended Move Structure

The information which piece performs the move and which piece is captured (if any) is implicit given by the from-to squares, with the requirement to lookup the current board before making the move, but in case of [captures](Captures "Captures") not after making or before unmaking the move. Some programs use a 32-bit [double word](Double_Word "Double Word") as extended move structure at generation time as well for making/unmaking moves, with the upper bits used for a move score scaled by various [move ordering](Move_Ordering "Move Ordering") techniques for instance dedicated [piece-square tables](Piece-Square_Tables "Piece-Square Tables") and/or [history heuristic](History_Heuristic "History Heuristic"), and perhaps two three bit codes for the moving and captured piece (if any) which also implies a kind of [MVV-LVA](MVV-LVA "MVV-LVA") coding. Also the extended move may apply composite indices for [incremental update](Incremental_Updates "Incremental Updates") of [Zobrist](Zobrist_Hashing "Zobrist Hashing")- or [BCH keys](BCH_Hashing "BCH Hashing").

Having the piece codes inside the move structure safes the board lookups during make, and makes storing captured pieces on a ply stack for unmake needless. Of course for space considerations to store moves inside [transposition table](Transposition_Table "Transposition Table"), [Killer slots](Killer_Heuristic "Killer Heuristic"), [PV-](Triangular_PV-Table "Triangular PV-Table") or [refutation table](Refutation_Table "Refutation Table"), the compact 16-bit move structure is still adequate for coordinate and move kind comparison with the lower 16 bits of the extended move structure.

## C++ Sample

Rather than using [bitfield](C#Bitfield "C") move structures or classes in [C](C "C") and [C++](Cpp "Cpp"), most programmers rely on scalar integers, such as *short* and *int* for 16- or 32-bit words, but implement the composition and extraction while writing and reading various structure elements by explicit shifts and masks, likely encapsulated thought an interface with most likely inlined functions (or macros) to hide the internal representation. Further extended move structures might either embed or inherit this most compact base structure or class, which might already rely the native 32-bit integer type to avoid [x86](X86 "X86") 16-bit optimization issues.

```C++

class CMove {
   CMove(unsigned int from, unsigned int to, unsigned int flags) {
      m_Move = ((flags & 0xf)<<12) | ((from & 0x3f)<<6) | (to & 0x3f);
   }
   void operator=(CMove a} {m_Move = a.m_Move;}

   unsigned int getTo() const {return m_Move & 0x3f;}
   unsigned int getFrom() const {return (m_Move >> 6) & 0x3f;}
   unsigned int getFlags() const {return (m_Move >> 12) & 0x0f;}

   void setTo(unsigned int to) {m_Move &= ~0x3f; m_Move |= to & 0x3f;}
   void setFrom(unsigned int from) {m_Move &= ~0xfc0; m_Move |= (from & 0x3f) << 6;}
   ...

   bool isCapture() const {return (m_Move & CAPTURE_FLAG) != 0;}
   ...

   unsigned int getButterflyIndex() const {return m_Move & 0x0fff;}
   bool operator==(CMove a) const {return (m_Move & 0xffff) == (a.m_Move & 0xffff);}
   bool operator!=(CMove a) const {return (m_Move & 0xffff) != (a.m_Move & 0xffff);}

   unsigned short asShort() const {return (unsigned short) m_Move;}

protected:
   unsigned int m_Move; // or short or template type
};

```

## Various Encodings and Decorations

## Algebraic Notation

Based on [Philipp Stamma's](https://en.wikipedia.org/wiki/Philipp_Stamma) short [algebraic chess notation](Algebraic_Chess_Notation "Algebraic Chess Notation"), a move can be described by the moving piece code and destination square. In case of disambiguating moves if two (or more) identical pieces can move to the same square, the file of departure, or if files are identical as well, the rank or both file and rank are given. A capture move, denoted by the symbol 'x' (takes) does not explicitly specify the captured piece and requires a look to the board as well.

Chess programs usually use algebraic notations concerning the [user interface](GUI "GUI") and [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") - for appropriate conversion they have to deal with disambiguating source squares, that is need to be aware of all other moves of this piece-kind to the destination square to determine whether the from square needs additional file and/or rank information despite the moving piece.

## Direction-Target

Another move encoding alternative motivated by [direction wise](Pieces_versus_Directions#DirectionWise "Pieces versus Directions") target square serialization in [bitboards](Bitboards "Bitboards") is not to use the from-square but target square and [direction](Direction "Direction"). While the information is non-ambiguous it needs some effort with ray-lookup and [bitscan](BitScan "BitScan") to determine the from-square.

## Check Flag

It might be interesting to determine whether a move gives [check](Check "Check") in advance during generation time, to possibly score them higher for move ordering, i. e. to don't [reduce](Late_Move_Reductions "Late Move Reductions") or even [extend](Check_Extensions "Check Extensions") them, and also to safe in check detection after make move. However, as mentioned, lazy move generation is required, to delay acquisition of information until it is really needed, which might be never in case of [Cut-nodes](Node_Types#cut-nodes "Node Types"). Additionally an early determined checking move, even if [failing high](Fail-High "Fail-High"), usually implies a huge sub-tree due to [check extensions](Check_Extensions "Check Extensions"), while an early non checking moves likely makes a cheaper [cutoff](Beta-Cutoff "Beta-Cutoff") for most futile Cut-nodes. Therefor, determining checking moves in advance is not that recommended for most board-representations.

## Move Index

If the [generated moves](Move_Generation "Move Generation") inside a [move list](Move_List "Move List") are [deterministic](https://en.wikipedia.org/wiki/Determinism), one may encode moves as relative list index. Since the maximum number of moves per positions seems 218 <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> , one [byte](Byte "Byte") is enough to index the move. This encoding was used in early game databases.

|  Two Positions with 218 Moves each
| [A. Dickins](http://commons.wikimedia.org/wiki/File:DickinsAnthony.jpg) (1968) <a id="cite-note-4" href="#cite-ref-4">[4]</a> |
| --- | --- |
|

|  |
| --- |
|                                                                              ♖      ♖   ♕     ♕    ♕     ♕     ♕    ♕♕    ♕  ♟♟ ♕    ♚♗♘♘ ♔♗  |

|

|  |
| --- |
|                                                                                  ♕     ♕    ♕     ♕     ♕    ♖♕    ♕     ♕     ♕    ♖♟ ♔ ♗♗♘♘♚ |

|
| R6R/3Q4/1Q4Q1/4Q3/2Q4Q/Q4Q2/pp1Q4/kBNN1KB1 w - - 0 1 | 3Q4/1Q4Q1/4Q3/2Q4R/Q4Q2/3Q4/1Q4Rp/1K1BBNNk w - - 0 1 |

This method can be refined if variable-length encoding is allowed. This is especially useful for long sequences of moves. If the number of legal moves from the position is equal to `n` then only `ceil(log2(n))` bits need to be used to encode the move (note: positions without a move available require special handling; position with one move available need 0 bits, so they may need some more information to encode whether a move was made or the game terminated prior to it, depending on use-case). Empirical data based on a sample of human games shows that each move when encoded with this scheme takes approximately 5.11 bits, that is about 63.8% of the original size (1 byte per move).

A simple variation of this is to use a list of pseudo-legal moves, which may speed up the encoding/decoding process at a cost of a slightly larger size. On the same dataset as above it amounts to approximately 5.41 bits per move, or about 67.7% of the original size. Other methods of indexing into the movelist (for example using 2 indirections - piece and square) and other criteria for the moves included in the movelist can be devised for different tradeoffs between speed and compression ratio.

## Move Enumeration

### Per Piece and Square

For the subset of common chess positions a faster encoding scheme is possible that doesn't require move generation of any kind. Let's enumerate the upper bound on the number of unique moves a piece of a given type can make from one [square](Squares "Squares") - for [sliding pieces](Sliding_Pieces "Sliding Pieces") assuming no obstacles:

|  Piece
|  # of Moves
|  Remarks
|
| --- | --- | --- |
| [Pawn](Pawn "Pawn") |  12
|  7th rank, 4 [promotions](Promotions "Promotions") * 3 [target squares](Target_Square "Target Square") |
| [Knight](Knight "Knight") |  8
|  from the 16 [extended center](Center#ExtendedCenter "Center") squares
|
| [Bishop](Bishop "Bishop") |  13
|  from the 4 [center](Center "Center") squares
|
| [Rook](Rook "Rook") |  14
|  from any square
|
| [Queen](Queen "Queen") |  27
|  from the 4 [center](Center "Center") squares
|
| [King](King "King") |  8
|  there are two additional [castling moves](Castling "Castling"),but they are only possible from the start positionwhere the king has 5 normal moves available
|

NOTE: We will always use this upper bound instead of the actual number of possible legal moves because this way we don't have to compute any attacks.

So for the standard chess piece set we have an upper bound of `12*8 + 8*2 + 13*2 + 14*2 + 27 + 8 == 201` possible moves before considering promotions. Each knight promotion reduces it by 12-8=4. Each bishop promotion increases it by 1; rook promotion by 2; queen promotion by 15. In the parametrized worst case (all pawns promoted to either rooks or queens) we have `n` queen and `8-n` rook promotions, so the upper bound is `f(n) = 8*2 + 13*2 + 14*(2+8-n) + 27*(1+n) + 8 == 217 + 13n`. `f(n=3)=256 <= 2^8`.

So for legal [Chess960](Chess960 "Chess960") positions with at most 3 queens on the board one can encode any legal move in just one byte. Note that whether the result can always fit in one byte is determined based solely one the position, so no additional information needs to be stored for disambiguation. This way it's easy to implement a fallback for the positions not supported by this encoding (this could be either to use 2 bytes for the move index or use legal move generation to ensure all values take one byte). One way to encode a position using this information is in the following way:

```C++

offset = 0
for each square in our_pieces_bb:
    if square == move.from:
        break
    
    offset += upper_bound(pos.piece_on(square).type)

move_index = offset + piece_move_index(moved_piece, move)
```

The `piece_move_index(moved_piece, move)` function can be implemented for example using lookup tables - the board state doesn't matter, only the move does.

Alternatively we can go through each piece type in some order (instead of going through individual squares), which allows faster computation of the offset if [popcount](Population_Count "Population Count") instruction is available:

```C++

offset = 0
for each piece_type lower than moved_piece.type:
    offset += 
        popcount(pos.pieces_bb(piece_type, side_to_move)) 
        * upper_bound(piece_type)

offset += 
    popcount(
        pos.pieces_bb(moved_piece.type, side_to_move) 
        & squares_before_bb(move.from)) 
    * upper_bound(piece_type)

move_index = offset + piece_move_index(moved_piece, move)

```

To decode the move we step through different offsets in the same way as we did when encoding, but now we have to look for the range of values that contains the encoded move index - once we find the range we can just decode the move index of that specific piece type (using an inverse of `piece_move_index`). While this method allows much faster encoding/decoding then the one involving a list of legal moves, it requires additional work if one needs to verify the correctness of the decoded moves (in the former one just needs to check if the index is within bounds).

This method is used in one of the move encodings available in the [BCGN](index.php?title=BCGN&action=edit&redlink=1 "BCGN (page does not exist)") chess game storage format <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

### Over All Pieces and Squares

Based on [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces") one may enumerate all moves, to specify a unique determined move number with respect to moving piece, from- and to squares, captured piece (if any) and promoted piece inside a 16-bit range.

**Pawn Moves**

|  Move Kind
|  Ranks
|  Files
|  Directions
|  TargetCombinations
|  Cardinality
|
| --- | --- | --- | --- | --- | --- |
|  Pushs
|  5
|  8
|  1
|  1
|  40
|
|  Promotions
|  1
|  8
|  1
|  4
|  32
|
|  Double Pushs
|  1
|  8
|  1
|  1
|  8
|
|  Total Pushs
|  6
|  8
|  1
| 1+2/3 | **80** |
|  Captures
|  5
|  7
|  2
|  5
|  350
|
|  Captures & Promotions
|  1
|  7
|  2
|  4\*4
| <a id="cite-note-6" href="#cite-ref-6">[6]</a> 224
|
|  En passant
|  1
|  7
|  2
|  1
|  14
|
|  Total Captures
|  6
|  7
|  2
|  | **588** |
|  Total Pawns
|  6
|  |  3
|  | **668** |

**Piece Moves**
Reversible and Captures, [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces") times six target combinations for empty and five possible capture targets.

|  Piece
|  Influence Quantity
|  Cardinality
|
| --- | --- | --- |
|  Knight
|  336
|  2016
|
|  King
|  420
|  2520
|
|  Bishop
|  560
|  3360
|
|  Rook
|  896
|  5376
|
|  Queen
|  1456
|  8736
|
|  Total
|  3668
| **22008** |

**All Moves**
Sheet of all moves, considering [Castling](Castling "Castling") (but no null move):

|  Piece
|  Move Kind
|  From-To
|  None
|  Captures
|  per Side
|  Total
|
| --- | --- | --- | --- | --- | --- | --- |
|  Pawn
|  Promotions
|  8
|  32
|  -
|  32
|  64
|
|  Captures & Promotions
|  14
|  -
|  224
|  224
|  448
|
|  Double Pushs
|  8
|  8
|  -
|  8
|  16
|
|  Pushs
|  40
|  40
|  -
|  40
|  80
|
|  Captures
|  70
|  -
|  350
|  350
|  700
|
|  En passant
|  14
|  -
|  14
|  14
|  28
|
| **Total** |  | **80** | **588** | **668** | **1336** |
|  King
|  Castles
|  2
|  2
|  -
|  2
|  4
|
|  |  420
|  420
|  2100
|  2520
|  5040
|
| **Total** |  | **422** | **2100** | **2522** | **5044** |
|  Knight
|  |  336
|  336
|  1680
|  2016
|  4032
|
|  Bishop
|  |  560
|  560
|  2800
|  3360
|  6720
|
|  Rook
|  |  896
|  896
|  4480
|  5376
|  10752
|
|  Queen
|  |  1456
|  1456
|  7280
|  8736
|  17472
|
|  | **Total** |  | **3248** | **16240** | **19488** | **38976** |
|  Total
|  |  | **3750** | **18928** | **22678** | **45356** |

## See also

- [Influence Quantity of Pieces](Influence_Quantity_of_Pieces "Influence Quantity of Pieces")
- [Move Generation](Move_Generation "Move Generation")
- [Move Ordering](Move_Ordering "Move Ordering")

## Forum Posts

## 1993 ...

- [recording chess games in very few bits per move](https://groups.google.com/d/msg/rec.games.chess/RspnvkCEY7s/W4kUZ0uH7jMJ) by Toby Robison, [rgc](Computer_Chess_Forums "Computer Chess Forums"), March 05, 1993
- [Chess move binary encoding](https://groups.google.com/d/msg/rec.games.chess/yL_tzhBpVsw/PBb6dSWl9FgJ) by [Jeff Mallett](Jeff_Mallett "Jeff Mallett") via [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), July 04, 1994

## 2000 ...

- [Subject: Maximum Number of Legal Moves](https://www.stmintz.com/ccc/index.php?id=424966) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), May 08, 2005
- [Two doubts](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=20092) by [Fermin Serrano](Fermin_Serrano "Fermin Serrano"), [CCC](CCC "CCC"), March 10, 2008

## 2010 ...

- [max amount of moves from a position?](http://www.talkchess.com/forum/viewtopic.php?t=39332) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 10, 2011 » [Chess Maxima](Chess#Maxima "Chess")
- [Contest: Find Position with the most moves](http://www.talkchess.com/forum/viewtopic.php?t=41388) by [Charles Roberson](Charles_Roberson "Charles Roberson"), [CCC](CCC "CCC"), December 09, 2011
- [Move encoding](http://www.talkchess.com/forum/viewtopic.php?t=52083) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), April 21, 2014
- [Killer and move encoding](http://www.talkchess.com/forum/viewtopic.php?t=53289) by [Fabio Gobbato](Fabio_Gobbato "Fabio Gobbato"), [CCC](CCC "CCC"), August 14, 2014 » [Killer Heuristic](Killer_Heuristic "Killer Heuristic")

## 2020 ...

- [Generating all the moves on a board](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73867) by [Marc-Philippe Huget](Marc-Philippe_Huget "Marc-Philippe Huget"), [CCC](CCC "CCC"), May 07, 2020
- [Move structure and hash tables](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78466) by gaard, [CCC](CCC "CCC"), October 20, 2021

## External Links

- [Move Representation - Computer Architecture and Languages Laboratory](http://labraj.uni-mb.si/en/Move_Representation), [University of Maribor](University_of_Maribor "University of Maribor")
- [Code from Wikipedia](https://en.wikipedia.org/wiki/Code)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Binary code from Wikipedia](https://en.wikipedia.org/wiki/Binary_code)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Subject: Maximum Number of Legal Moves](https://www.stmintz.com/ccc/index.php?id=424966) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), May 08, 2005
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [max amount of moves from a position?](http://www.talkchess.com/forum/viewtopic.php?t=39332) by [Srdja Matovic](Srdja_Matovic "Srdja Matovic"), [CCC](CCC "CCC"), June 10, 2011
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Re: max amount of moves from a position?](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=410026&t=39332) by [Árpád Rusz](%C3%81rp%C3%A1d_Rusz "Árpád Rusz"), [CCC](CCC "CCC"), June 11, 2011
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [A detailed walkthrough of an implementation of BCGN's move index based move encoding scheme · GitHub](https://github.com/Sopel97/chess_pos_db/blob/master/docs/bcgn/move_index.md)
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> PxP not possible during promotion, therefore only four capture targets

**[Up one Level](Moves "Moves")**

