---
title: Chess.jl
---
**[Home](Home "Home") * [Software](Software "Software") * [Utilities](Utilities "Utilities") * Chess.jl**

**Chess.jl**,

a chess programming library by [Tord Romstad](Tord_Romstad "Tord Romstad"), written in the [Julia](index.php?title=Julia&action=edit&redlink=1 "Julia (page does not exist)") programming language <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
Chess.jl has functions to create and manipulate [chess games](Chess_Game "Chess Game"), [chess positions](Chess_Position "Chess Position") and [sets of squares](Bitboards "Bitboards")
on the [board](Chessboard "Chessboard") (aka [Bitboards](Bitboards "Bitboards") <a id="cite-note-2" href="#cite-ref-2">[2]</a>).
It can read and write [chess games](Chess_Game "Chess Game") in [PGN format](Portable_Game_Notation "Portable Game Notation") (including support for comments and variations),
create [opening books](Opening_Book "Opening Book"), and interact with [UCI chess engines](Category:UCI "Category:UCI") <a id="cite-note-3" href="#cite-ref-3">[3]</a>,
for instance to play engine versus engine matches for [tuning](Automated_Tuning "Automated Tuning") and [NNUE](NNUE "NNUE") training purposes.

## Types

Chess.jl features following data types and [APIs](https://en.wikipedia.org/wiki/API). Scalar data types like [Squares](Squares "Squares") and [Pieces](Pieces "Pieces") with discrete enumerated value range are internally wrapper around integer.

- [Squares](Squares "Squares")
  - [SquareFile](Files "Files")
  - [SquareRank](Ranks "Ranks")
- [SquareSet](Bitboards "Bitboards")
- [Pieces](Pieces "Pieces")
  - [Piece Type](Pieces#PieceTypeCoding "Pieces")
  - [Piece Color](Color "Color")
- [Board](Chess_Position "Chess Position")
- [Moves](Moves "Moves")
  - [UndoInfo](Make_Move "Make Move")
  - [MoveList](Move_List "Move List")
- [Chess Game](Chess_Game "Chess Game")
  - [PGN format](Portable_Game_Notation "Portable Game Notation")
- [Opening Book](Opening_Book "Opening Book")
- [UCI](UCI "UCI") [Chess Engine](Category:UCI "Category:UCI")

## SquareSet

The SquareSet aka Bitboard API <a id="cite-note-4" href="#cite-ref-4">[4]</a>
provide [setwise operations](General_Setwise_Operations "General Setwise Operations") including [shifts](General_Setwise_Operations#ShiftingBitboards "General Setwise Operations"), and piece-wise attack getter -
for [sliding pieces](Sliding_Piece_Attacks "Sliding Piece Attacks") from a given square and [occupancy](Occupancy "Occupancy").
There are also [functions](BitScan "BitScan") to [transform](Bitboard_Serialization "Bitboard Serialization") a SquareSet into a vector of squares.

## Board

Using a chess board object through a [Pluto](<https://en.wikipedia.org/wiki/Julia_(programming_language)#Interaction>) <a id="cite-note-5" href="#cite-ref-5">[5]</a> or [Jupyter notebook](https://en.wikipedia.org/wiki/Project_Jupyter#Jupyter_Notebook),
features a graphical board, along with a board representation link in [lichess](index.php?title=Lichess&action=edit&redlink=1 "Lichess (page does not exist)").

## See also

- [python-chess](Python-chess "Python-chess")

## Forum Posts

- [Re: Is cloning a hobby?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75040&start=74) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), September 21, 2020
- [Chess.jl – new version](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77210) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), April 30, 2021

## External Links

- [Home · Chess.jl](https://romstad.github.io/Chess.jl/dev/)
- [GitHub - romstad/Chess.jl: Julia chess programming library](https://github.com/romstad/Chess.jl)
- [🎈 chess-jl-tutorial.jl — Pluto.jl](https://romstad.github.io/Chess.jl/tutorial/)

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Julia (programming language) from Wikipedia](<https://en.wikipedia.org/wiki/Julia_(programming_language)>)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Is cloning a hobby?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=75040&start=74) by [Tord Romstad](Tord_Romstad "Tord Romstad"), [CCC](CCC "CCC"), September 21, 2020
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Home · Chess.jl](https://romstad.github.io/Chess.jl/dev/#Introduction-1)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [API Reference · Chess.jl](https://romstad.github.io/Chess.jl/dev/api/#Square-Sets-1)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [GitHub - fonsp/Pluto.jl: 🎈 Simple reactive notebooks for Julia](https://github.com/fonsp/Pluto.jl)

**[Up one Level](Utilities "Utilities")**

