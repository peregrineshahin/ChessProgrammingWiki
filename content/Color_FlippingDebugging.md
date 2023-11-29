---
title: Color FlippingDebugging
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Color Flipping**

**Color Flipping** a chess position refers to the [vertical flipping](Vertical_Flipping "Vertical Flipping") or mirroring of all [pieces](Pieces "Pieces") along the horizontal axis between the 4th and 5th [rank](Ranks "Ranks") also swapping the [color](Color "Color") of the flipped pieces from White to Black and vice versa, the [side to move](Side_to_move "Side to move"), the [castling rights](Castling_Rights "Castling Rights") and the rank of a possible [en passant](En_passant "En passant") target square from six to three or vice versa accordantly. The resulting position is mirror equivalent, pawn and pieces have the same [span length](Pawn_Spans "Pawn Spans") or home rank relation. A white pawn on the light square c2 becomes a black pawn on the dark square c7. Color flipping a vertical symmetrical or mirror position (same castling rights, no en passant possible) results in the same position as if the side to move performed a [null move](Null_Move "Null Move"):

## Sample

* Giuoco Piano

<img src="https://lichess1.org/export/fen.gif?fen=r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -" style="
    width: 300px;
">

```
r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq -
```
<img src="https://lichess1.org/export/fen.gif?fen=r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -" style="
    width: 300px;
">

```
r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R w KQkq -
```

* Giuoco Piano Symmetrical

<img src="https://lichess1.org/export/fen.gif?fen=rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR b KQkq -" style="
    width: 300px;
">

<img src="https://lichess1.org/export/fen.gif?fen=r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -" style="
    width: 300px;
">

```
rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR b KQkq -
```

```
r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq -
```

## Book Transpositions

During the [opening](Opening "Opening"), in some lines, White may intentionally lose a [tempo](Tempo "Tempo"), to [transpose](Transposition "Transposition") into a color flipped position of an opening White likes to play the "Black" side, which might be considered in chess programs [book](Opening_Book "Opening Book") access code, see for instance [WMCCC 1988, Pandix-Y!88](WMCCC_1988#Pandix-Y.21 "WMCCC 1988").

## Flipping an 8x8 Board

An [8x8 Board](8x8_Board "8x8 Board") with a [rank-file mapping](Squares "Squares"), needs to perform an [exclusive or](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") with 56 (A8 in [LERF](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations")) to vertically flip square coordinates. Assuming piece color is least significant bit and empty square is zero, a pure 8x8 Board may be color flipped that way in [C](C "C"):

```C++
int board[64], sq, s, f;

for (sq = 0; sq < 32; ++sq) {
    s = board[sq];
    f = board[sq^56];
    board[sq] = f ^ (f != 0);
    board[sq^56] = s ^ (s != 0);
}

```

## Looking for Bugs

A side to move relative, bug free static [evaluation](Evaluation "Evaluation") should have the same [score](Score "Score") for both positions. [Search](Search "Search") is a different issue, since [move ordering](Move_Ordering "Move Ordering") might be slightly different for instance in bitboard programs due to different order in [bitboard serialization](Bitboard_Serialization "Bitboard Serialization") if one doesn't use a [symmetrical bitscan](Bitboard_Serialization#BlackorWhite "Bitboard Serialization") by side to move. Similar to the [butterfly effect](https://en.wikipedia.org/wiki/Butterfly_effect) in [chaos theory](https://en.wikipedia.org/wiki/Chaos_theory) a minor initial difference might amplify to enormous effects during the search. However, if the search behavior of a [tactical](Tactics "Tactics") [test position](Test_Positions "Test-Positions") of a most deterministic chess engine (e.g. no [parallel search](Parallel_Search "Parallel Search")), varies by magnitudes in solution [depth](Depth "Depth") and time between original and color flipped position, one may take a closer look performing some [logging](Logging "Logging") and/or [debugging](Debugging "Debugging").

## Monochrome

An idea to unify and simplify [move generation](Move_Generation "Move Generation") and to get rid of order dependencies, is to perform a color flip of the position and its internal [board representation](Board_Representation "Board Representation") directly after [making a move](Make_Move "Make Move"), to make the engine white to move only, that is only generating white moves, or similar, to keep a normal and flipped board to [update them incrementally](Incremental_Updates "Incremental Updates").

## MicroChess

[Jennings'](Peter_Jennings "Peter Jennings") [approach](6502#MicroChess "6502") with [MicroChess](MicroChess "MicroChess") was similar <a id="cite-note-1" href="#cite-ref-1">[1]</a>, but instead of vertical flipping (xor 56) he reversed or rotated the board by 180 degrees (xor 63), like players changing places and looking the board alternately from White's or Black's point of view, with some considerations of the additional horizontal mirroring, concerning [castling](Castling "Castling") and [en passant](En_passant "En passant").

## Quad-Bitboards

[Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") proposed a make move - color flipping approach using [Quad-Bitboards](Quad-Bitboards "Quad-Bitboards") <a id="cite-note-2" href="#cite-ref-2">[2]</a> . The black [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") were the byte-swapped white Zobrist keys from the vertically flipped squares (xor 56). In symmetrical positions this gains some additional hits while probing the [transposition table](Transposition_Table "Transposition Table"). But symmetrical mirror positions, or symmetrical subsets have the property, their [xored](General_Setwise_Operations#ExclusiveOr "General Setwise Operations") hashkey has only 32 distinct bits since hashkey equals [flipVertical](Flipping_Mirroring_and_Rotating#FlipVertically "Flipping Mirroring and Rotating")(hashkey), for instance:

```C++
  01020304|50607080  // white pieces
^ 80706050|04030201  // black pieces of a mirror position
= 81726354|54637281

```

## Six-Two Bitboards

The common [six piece kind and two color bitboard](Bitboard_Board-Definition#SixTwo "Bitboard Board-Definition") board representation takes eight byte swaps to color flip the whole board.

## Keeping two Boards

Rather than flipping the board after each make, [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl") proposed monochrome move generation by keeping a normal and a color flipped board, both [incremental updated](Incremental_Updates "Incremental Updates") <a id="cite-note-3" href="#cite-ref-3">[3]</a> . He further suggested asymmetrical [piece coding](Pieces#PieceCoding "Pieces") with less piece codes (only one or two) for the pieces of the side not to move. His approach has also the advantage to keep independent Zobrist keys for all squares and pieces.

## See also

- [Color](Color "Color")
- [Diagonal Mirroring](Diagonal_Mirroring "Diagonal Mirroring")
- [Flipping, Mirroring and Rotating](Flipping_Mirroring_and_Rotating "Flipping Mirroring and Rotating") of [Bitboards](Bitboards "Bitboards")
- [Horizontal Mirroring](Horizontal_Mirroring "Horizontal Mirroring")
- [Side to move](Side_to_move "Side to move")
- [Vertical Flipping](Vertical_Flipping "Vertical Flipping")

## Publications

- [Fernand Gobet](Fernand_Gobet "Fernand Gobet") (**1993**). *[A Computer Model of Chess Memory](http://people.brunel.ac.uk/%7Ehsstffg/papers/ModelChessMem/Chess%20Memory.html).* Proceedings of the 15th Annual Meeting of the Cognitive Science Society, pp. 463-468.

## Forum Posts

- [Conversion to dual positions for EPD testsuites?](https://www.stmintz.com/ccc/index.php?id=199005) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), November 26, 2001
- [fen to fen functions](http://www.talkchess.com/forum/viewtopic.php?t=13923) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 21, 2007
- [Comparison data of Crafty vs Rybka that I promised 2 days ago](http://www.talkchess.com/forum/viewtopic.php?t=14168) by Les, [CCC](CCC "CCC"), June 01, 2007
- [color-flipped perft](http://www.talkchess.com/forum/viewtopic.php?t=17589) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), November 04, 2007
- [Board without color flags](http://www.talkchess.com/forum/viewtopic.php?t=30423) by [Fritz Reul](Fritz_Reul "Fritz Reul"), [CCC](CCC "CCC"), October 31, 2009
- [Position flipping](http://www.talkchess.com/forum/viewtopic.php?t=48843) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 05, 2013
- [Black/White symmetry in move generation](http://www.talkchess.com/forum/viewtopic.php?t=54465) by Jeffery A Esposito, [CCC](CCC "CCC"), November 25, 2014 » [Move Generation](Move_Generation "Move Generation")
- [Symmetric move generation using bitboards](http://www.talkchess.com/forum/viewtopic.php?t=54704) by [Lasse Hansen](Lasse_Hansen "Lasse Hansen"), [CCC](CCC "CCC"), December 20, 2014
- [reversed-color transpositions](http://www.talkchess.com/forum/viewtopic.php?p=663148) by [John Fishburn](John_Philip_Fishburn "John Philip Fishburn"), [CCC](CCC "CCC"), March 11, 2016
- [FEN - Flipper for Windows](http://www.talkchess.com/forum/viewtopic.php?t=64003) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), May 17, 2017 » [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation"), [EPD](Extended_Position_Description "Extended Position Description")

## External Links

- [A "Mirror" Chess Problem](http://www.jimloy.com/chess/mirror1.htm) from [Jim Loy's Chess Pages](http://www.jimloy.com/chess/chess.htm)
- [Playing Chess Against Its Mirror Image](http://www.chessvariants.org/other.dir/mirror.html)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Peter Jennings](Peter_Jennings "Peter Jennings") (**1976**). *[MicroChess, a Chess playing program for the 6502 Microcomputer](http://www.computerhistory.org/chess/full_record.php?iid=doc-431614f6d8478)*. [pdf](http://archive.computerhistory.org/projects/chess/related_materials/text/4-1.MicroChess_%20Manual_for_6502.Micro-Ware/MicroChessManual.PETER_JENNINGS.062303071.sm.pdf), Courtesy of [Peter Jennings](Peter_Jennings "Peter Jennings"), [The Computer History Museum](The_Computer_History_Museum "The Computer History Museum")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [color-flipped perft](http://www.talkchess.com/forum/viewtopic.php?t=17589) by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg"), November 04, 2007
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Computerschach mit monochromen Methoden ?](http://www.open-chess.org/viewtopic.php?f=39&t=1039) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [OpenChess - Deutsches Forum](Computer_Chess_Forums "Computer Chess Forums"), January 27, 2011 (German)

**[Up one Level](Chess_Position "Chess Position")**

