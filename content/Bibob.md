---
title: Bibob
---
**[Home](Home "Home") * [Programming](Programming "Programming") * [Debugging](Debugging "Debugging") * Bibob**

**Bibob**,

a [Windows](Windows "Windows") [bitboard](Bitboards "Bitboards") [MDI](https://en.wikipedia.org/wiki/Multiple_document_interface) observer, editor and calculator by [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") - so far in [Little-Endian Rank-File Mapping](Square_Mapping_Considerations#LittleEndianRankFileMapping "Square Mapping Considerations"), since version 2.2 all eight orthogonal mappings. This application is a little overdressed and was intended as play ground for some [MFC](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library) [GUI](GUI "GUI") features such as [toolbars](https://en.wikipedia.org/wiki/Toolbar) with various controls like a [Combo box](https://en.wikipedia.org/wiki/Combo_box). For debugging under Windows, to inspect bitboards, one may [copy](https://en.wikipedia.org/wiki/Cut,_copy,_and_paste) the content of 64-bit variables from a Debugger to the [clipboard](https://en.wikipedia.org/wiki/Clipboard_%28computing%29) to paste it into a Bibob document window. Bibob accepts pasting [decimal](https://en.wikipedia.org/wiki/Decimal) or [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) strings as well as [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation").

## Screenshot

## [](File:Bibob.JPG) Features

Bibob is a Multiple Document Bitboard Viewer/Editor. It displays 64-bit Numbers in a Bitboard-Representation. Document-Windows act as Operands, a set of Unary as well as Binary Operations perform on Bitboards. A Second Operand Dropdown-Combobox features some common Constants, as well as Bitboards of other Document-
Windows - so that binary arithmetical and bitwise logical Operations may be performed between several Windows. Double click on a square toggles its state.

## Update 2.2

April 15, 2013

- Five new unary operators
- Persistent [Square Mapping Mode](Square_Mapping_Considerations "Square Mapping Considerations")

## Square Mapping Modes

|  LERF
|  LERBEF
|
| --- | --- |
| [Lerf.JPG](File:Lerf.JPG) | [Lerbef.JPG](File:Lerbef.JPG) |
|  |
| BERLEF
| BERF
|
| [Berlef.JPG](File:Berlef.JPG) | [Berf.JPG](File:Berf.JPG) |
|  |
|  LEFR
|  LEFBER
|
| [Lefr.JPG](File:Lefr.JPG) | [Leber.JPG](File:Leber.JPG) |
|  |
|  BEFLER
|  BEFR
|
| [Befler.JPG](File:Befler.JPG) | [Befr.JPG](File:Befr.JPG) |

## Executable and Sources

[7z compressed](https://en.wikipedia.org/wiki/7z), Win32 executable, plus [C++](Cpp "Cpp") source code for the ancient [Visual C++ 6.0](https://en.wikipedia.org/wiki/Visual_C%2B%2B#32-bit_versions) compiler using [MFC](https://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library):

[File:Bibob.zip](File:Bibob.zip "File:Bibob.zip")

## External Links

- [Bitboard Calculator](http://cinnamonchess.altervista.org/bitboard_calculator/Calc.html) by [Giuseppe Cannella](Giuseppe_Cannella "Giuseppe Cannella")
- [Free Chess Bitboard Viewer - Computer Chess Programming](http://www.chessprogramming.net/computerchess/free-chess-bitboard-viewer/) by [Steve Maughan](Steve_Maughan "Steve Maughan")
- [New free tool : Bitboards Helper](http://www.chess2u.com/t2159-new-free-tool-bitboards-helper) by [Julien Marcel](Julien_Marcel "Julien Marcel")

**[Up one Level](Debugging "Debugging")**

