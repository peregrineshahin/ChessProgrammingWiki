---
title: Gochess
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Gochess**

**Gochess**,

a didactic [open source chess engine](Category:Open_Source "Category:Open Source") by [Franziskus Domig](index.php?title=Franziskus_Domig&action=edit&redlink=1 "Franziskus Domig (page does not exist)"), written in [Golang](</Go_(Programming_Language)> "Go (Programming Language)"), released under the [MIT license](Massachusetts_Institute_of_Technology#License "Massachusetts Institute of Technology") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.
It was inspired by [chess-at-nite](Chess-at-nite "Chess-at-nite") ([C/C++](Cpp "Cpp")) and uses most of its concepts <a id="cite-note-2" href="#cite-ref-2">[2]</a>

## Screenshot

[](https://github.com/fdomig/gochess/blob/master/gochess.png)
Gochess' [command line interface](CLI "CLI"): [ASCII-board](Graphics_Programming#ASCIIDiagrams "Graphics Programming") with [Unicode Pieces](Pieces#Unicode "Pieces") <a id="cite-note-3" href="#cite-ref-3">[3]</a>

## Unicode

<a id="cite-note-4" href="#cite-ref-4">[4]</a>

```C++
symbolsUnicode = []string {
  ".",
  "♙", "♘", "♗", "♖", "♕", "♔",
  "♟", "♞", "♝", "♜", "♛", "♚",
}

```

## Features

## [Board Representation](Board_Representation "Board Representation")

- [0x88 Board](0x88 "0x88")

## [Search](Search "Search")

<a id="cite-note-5" href="#cite-ref-5">[5]</a>

- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Check Extensions](Check_Extensions "Check Extensions")

## [Evaluation](Evaluation "Evaluation")

<a id="cite-note-6" href="#cite-ref-6">[6]</a>

- [Material Balance](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Doubled Pawn](Doubled_Pawn "Doubled Pawn")

## See also

- [chess-at-nite](Chess-at-nite "Chess-at-nite")

## External Links

## Chess Engine

- [GitHub - fdomig/gochess: A chess engine written in Go](https://github.com/fdomig/gochess)

## Namesakes

- [GitHub - jonpchin/gochess: Online real time chess web server using websockets](https://github.com/jonpchin/gochess)
- [GitHub - anastasop/gochess: A library for handling chess games. It will support PGN, FEN, UCI](https://github.com/anastasop/gochess)

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [gochess/LICENSE at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/LICENSE)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [gochess/README.md at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/README.md)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [gochess/gochess.png at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/gochess.png)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [ochess/piece.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/piece.go)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [gochess/search.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/search.go)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [gochess/eval.go at master · fdomig/gochess · GitHub](https://github.com/fdomig/gochess/blob/master/engine/eval.go)

**[Up one level](Engines "Engines")**

