---
title: Algebraic Chess NotationFAN
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Game](Chess_Game "Chess Game") * [Notation](Game_Notation "Game Notation") * Algebraic Chess Notation**

**Algebraic Chess Notation** is a chess notation to record and represent [moves](Moves "Moves") of a [human readable](https://en.wikipedia.org/wiki/Human-readable_medium) [game notation](Game_Notation "Game Notation"). It is based on a system developed by [Philipp Stamma](https://en.wikipedia.org/wiki/Philipp_Stamma) to notate the [target square](Target_Square "Target Square") by [algebraic coordinates](Squares#Algebraic "Squares"), and various forms to represent the [origin square](Origin_Square "Origin Square") of the move, either by language dependent [piece initials](https://en.wikipedia.org/wiki/Algebraic_chess_notation#Naming_the_pieces_in_various_languages) and/or [file](Files "Files"), [rank-](Ranks "Ranks") or [square](Squares "Squares") notation of the from- or origin square. [Promotions](Promotions "Promotions") must be disambiguated by including the promoted piece type, and [castling](Castling "Castling") usually has their own symbol strings ('O-O', 'O-O-O'). Some format variations also specify a [captured](Captures "Captures") piece, if any, for the purpose to make the notation reversible, and to go backward as easy as forward while re-playing a game.

## Sequence of Moves

Chess programs need to convert the [list](Move_List "Move List") of [encoded moves](Encoding_Moves "Encoding Moves") into a sequence of printable strings, or to render them inside a [notation window](GUI#NotationWindow "GUI"). The move number of the game, starting by '1.' from the [initial position](Initial_Position "Initial Position"), is prefix of the white halfmove, followed by a the black reply, often in a second column of a grid view. If a move notation starts with Black, also after embedded comments or annotations, a trailing [ellipsis](https://en.wikipedia.org/wiki/Ellipsis) is used instead of a single dot.

```C++

<move> ::= <move number><move descriptor>
<move number> ::= <digit>[<digit>...]{'.' | '...'}

```

Modern chess programs, and their [graphical user interface](GUI "GUI") often support various modes to represent all kinds of game and move notations. Regarding [input of moves](Entering_Moves "Entering Moves") from a [user interface](User_Interface "User Interface"), or reading moves from text files, programs needs to parse strings accordantly.

## Pure coordinate notation

Considering the common From-To [move encoding](Encoding_Moves "Encoding Moves") inside a chess program, pure coordinate notation is a straight-forward chess notation to use only algebraic From- and To-coordinates. This notation omits any machine redundant piece letters for the moving and/or capturing pieces, and only has to specify the promoted piece as trailing [letter](https://en.wikipedia.org/wiki/Algebraic_chess_notation#Naming_the_pieces_in_various_languages) in case of [promotions](Promotions "Promotions").

```C++

<move descriptor> ::= <from square><to square>[<promoted to>]
<square>        ::= <file letter><rank number>
<file letter>   ::= 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'
<rank number>   ::= '1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'
<promoted to>   ::= 'q'|'r'|'b'|'n'

```

Pure algebraic coordinate notation was often used in early microcomputer chess programs, sometimes even with capital file letters. Some programs used a hyphen or 'x' delimiter between the coordinate substrings to distinguish [quiet moves](Quiet_Moves "Quiet Moves") from [captures](Captures "Captures") in move outputs. While not common in human chess notation, pure coordinate notation has the advantage to avoid any ambiguity and is further easy convertible from a move list without the need of retrieving information from internal [board representations](Board_Representation "Board Representation"), (i.e. which [pieces](Pieces "Pieces") occupy which squares). Even [castling](Castling "Castling") was often written as E1G1 or E1C1 instead of 'O-O' or 'O-O-O'.

## XBoard

Per default, the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") requires pure algebraic coordinate notation without from-to delimiters as input and output move format <a id="cite-note-1" href="#cite-ref-1">[1]</a> .

## UCI

The [UCI](UCI "UCI") communication protocol requires *pure algebraic coordinate notation* without from-to delimiters as well. Inside its specification the UCI move format is called "long algebraic notation" <a id="cite-note-2" href="#cite-ref-2">[2]</a> , which might be considered slightly incorrect concerning leading piece character and dash or hyphen between from- and to coordinates, see LAN definition below.

## Output Samples

|  |  |  |
| --- | --- | --- |
| [8080Chess.JPG](File:8080Chess.JPG) |  | [C64 kempelen emulator scr2.gif](http://www.spacious-mind.com/html/c64_emu_-_kempelen.html) |
| [8080 Chess](8080_Chess "8080 Chess") Display <a id="cite-note-3" href="#cite-ref-3">[3]</a> |  | [Kempelen](Kempelen "Kempelen") [move list](Move_List "Move List") <a id="cite-note-4" href="#cite-ref-4">[4]</a> |

## ICCF numeric notation

The language independent [ICCF numeric notation](https://en.wikipedia.org/wiki/ICCF_numeric_notation) as used in [Correspondence chess](https://en.wikipedia.org/wiki/Correspondence_chess) is a numerical pure coordinate notation, giving coordinates by two digits (File '1'-'8) rather than letters ('a'-'h') for the file. In case of promotions a fifth trailing digit is used: '1' for queen, '2' for rook, '3' for bishop and '4' for knight.

## Smith Notation

The Smith notation designed by [Warren D. Smith](Warren_D._Smith "Warren D. Smith") <a id="cite-note-5" href="#cite-ref-5">[5]</a>, as used in the [Internet Chess Club](index.php?title=Internet_Chess_Club&action=edit&redlink=1 "Internet Chess Club (page does not exist)") chess server, encodes moves with from-square, to-square, and to make it reversible, so it is as easy to go backwards in a game as forwards, what piece was captured, if any ('E' for [En passant](En_passant "En passant"), the redundant 'c' and 'C' indicate king- or queen side [castling](Castling "Castling")):

```C++

<Smith move descriptor> ::= <from square><to square>[<capture indicator>][<promoted to>]
<capture indicator> ::=  'p' | 'n' | 'b' | 'r' | 'q' | 'k' | 'E' | 'c' | 'C'

```

## Long Algebraic Notation (LAN)

Beside the already sufficient and unambiguous pure origin- and target-coordinates, LAN uses a leading redundant, national dependent uppercase [piece letter](https://en.wikipedia.org/wiki/Algebraic_chess_notation#Naming_the_pieces_in_various_languages) or figurine piece symbol of the moving piece usually other than a [pawn](Pawn "Pawn"), to represent the move, which makes it more [human readable](https://en.wikipedia.org/wiki/Human-readable_medium) and compatible with SAN and [desciptive notation](https://en.wikipedia.org/wiki/Descriptive_chess_notation). However, for chess programs using pure from-to move encoding, converting the move list to LAN already requires a board representation in sync with the leading moves already played, to lookup the piece on the board.

```C++

<LAN move descriptor piece moves> ::= <Piece symbol><from square>['-'|'x']<to square>
<LAN move descriptor pawn moves>  ::= <from square>['-'|'x']<to square>[<promoted to>]
<Piece symbol> ::= 'N' | 'B' | 'R' | 'Q' | 'K'

```

*English symbols [Knight](Knight "Knight"), [Bishop](Bishop "Bishop"), [Rook](Rook "Rook"), [Queen](Queen "Queen") and [King](King "King")*.

|  |
| --- |
| [ChessForAndroidv1.png](@http://www.aartbik.com/MISC/android.html "@http://www.aartbik.com/MISC/android.html") |
| [Aart Bik's](Aart_Bik "Aart Bik") [Chess for Android](Chess_for_Android "Chess for Android"), G1 version with LAN representation <a id="cite-note-6" href="#cite-ref-6">[6]</a> |

## Standard Algebraic Notation (SAN)

Standard algebraic notation (SAN) is the official notation of the [FIDE](FIDE "FIDE") which must be used in all recognized international competition involving human players <a id="cite-note-7" href="#cite-ref-7">[7]</a> . Concerning computer chess, SAN is a representation standard for chess moves inside the [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") standard using the [ASCII](https://en.wikipedia.org/wiki/ASCII) [Latin alphabet](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) <a id="cite-note-8" href="#cite-ref-8">[8]</a>, and should be supported as default notation by all modern chess programs and their user interfaces <a id="cite-note-9" href="#cite-ref-9">[9]</a>.

|  |
| --- |
| [ChessForAndroid a chess.png](@http://www.aartbik.com/MISC/android.html "@http://www.aartbik.com/MISC/android.html") |
| [Aart Bik's](Aart_Bik "Aart Bik") [Chess for Android](Chess_for_Android "Chess for Android"), latest version in SAN mode <a id="cite-note-10" href="#cite-ref-10">[10]</a> |

While otherwise similar to LAN, SAN suppresses redundant information concerning the from-square, while keeping the descriptive letter or symbol of pieces other than a pawn. SAN further suppresses the from-to hyphen, and in some variations also the capture indicator 'x' (or ':').

```C++

<SAN move descriptor piece moves>   ::= <Piece symbol>[<from file>|<from rank>|<from square>]['x']<to square>
<SAN move descriptor pawn captures> ::= <from file>[<from rank>] 'x' <to square>[<promoted to>]
<SAN move descriptor pawn push>     ::= <to square>[<promoted to>]

```

## Ambiguities

If the piece is sufficient to unambiguously determine the origin square, the whole from square is omitted. Otherwise, if two (or more) pieces of the same kind can move to the same square, the piece's initial is followed by (in descending order of preference)

1. file of departure if different
1. rank of departure if the files are the same but the ranks differ
1. the complete origin square coordinate otherwise

## Captures

[Captures](Captures "Captures") are denoted by the lower case letter "x" immediately prior to the destination square. Pawn captures with the omitted piece symbol, include the file letter of the originating square of the capturing pawn prior to the "x" character, even if not required for unambiguousness. Some SAN variations in printed media even omit the target rank if unambiguous, like dxe, which might not be accepted as input format.

## En passant

The PGN-Standard does not require [En passant](En_passant "En passant") captures have any special notation, and is written as if the captured pawn were on the capturing pawn's destination square.[FIDE](FIDE "FIDE") states the redundant move suffix "e.p." optional (after 1 July 2014) <a id="cite-note-11" href="#cite-ref-11">[11]</a>.

In the case of an ‘en passant’ capture, ‘e.p.’ may be appended to the notation.

## Pawn promotion

A [pawn promotion](Promotions "Promotions") requires the information about the chosen piece, appended as trailing Piece letter behind the target square. The SAN PGN-Standard requires an equal sign ('=') immediately following the destination square.

## Castling

[Castling](Castling "Castling") is indicated by the special notations, "O-O" for kingside castling and "O-O-O" for queenside castling. While the FIDE handbook <a id="cite-note-12" href="#cite-ref-12">[12]</a> uses the digit zero, the SAN PGN-Standard requires the capital letter 'O' for its export format.

## Converting Moves

Due to the most compact representation, considering ambiguities concerning the origin square, converting moves with pure from- and to-squares to SAN requires not only an underlying board representation to determine piece initials, but also [legal move generation](Move_Generation#Legal "Move Generation") for a subset of moves to the destination square. [Pseudo legal](Pseudo-Legal_Move "Pseudo-Legal Move"), but [illegal moves](Legal_Move "Legal Move") for instance with a [Pinned piece](Pin "Pin") must not be considered in ambiguous issues in an export format.

## XBoard 2

With the [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") version 2, one can use the feature command to select SAN as move format for both input and output <a id="cite-note-13" href="#cite-ref-13">[13]</a> .

## Figurine Algebraic Notation (FAN)

Figurine notation uses miniature piece icons instead of single letter piece abbreviations. This enables the moves to be read independent of the language. The [Unicode](https://en.wikipedia.org/wiki/Unicode) [Miscellaneous Symbols](https://en.wikipedia.org/wiki/Miscellaneous_Symbols_Unicode_block) set includes all of the [symbols](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) necessary for FAN if appropriate [fonts](https://en.wikipedia.org/wiki/Font) were installed on the computer <a id="cite-note-14" href="#cite-ref-14">[14]</a> . [Chess GUIs](GUI "GUI") may alternatively use [Scalable Vector Graphics](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) or other scalable 2D [Vector Graphics](https://en.wikipedia.org/wiki/Vector_graphics) to render the symbols inside their views.

## Vector Graphics

|  |
| --- |
| [IsiChessFigurine.JPG](File:IsiChessFigurine.JPG) |
| [IsiChess](IsiChess "IsiChess"), notation window with figurine LAN, using 2D [Vector Graphics](https://en.wikipedia.org/wiki/Vector_graphics), see [sample code](2D_Graphics_Board#Drawing "2D Graphics Board") |

## LaTeX

|  |
| --- |
| [LaTeXChessNotation.JPG](File:LaTeXChessNotation.JPG) |
|  FAN in [LaTeX](https://en.wikipedia.org/wiki/LaTeX) <a id="cite-note-15" href="#cite-ref-15">[15]</a> |

## Reading Chess

In an attempt of [Computer vision](https://en.wikipedia.org/wiki/Computer_vision), [Henry S. Baird](Mathematician#HSBaird "Mathematician") and [Ken Thompson](Ken_Thompson "Ken Thompson") used [optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) along with various heuristics and applying the rules of chess, to "read" the figurine notation from Informant's [Encyclopaedia of Chess Openings](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings) with high accuracy and a success rate of 99.995% on approximately one million characters (2850 games, 945 pages) <a id="cite-note-16" href="#cite-ref-16">[16]</a> .

## See also

- [CPW-Engine_algebraic](CPW-Engine_algebraic "CPW-Engine algebraic")
- [Encoding Moves](Encoding_Moves "Encoding Moves")
- [Entering Moves](Entering_Moves "Entering Moves")
- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") (PGN)

## Publications

- [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
- [Michel Goossens](http://goossens.web.cern.ch/goossens/), [Frank Mittelbach](http://www.informit.com/authors/bio.aspx?a=A2624A62-C2B4-40F9-B8ED-E99563F89A27), [Sebastian Rahtz](http://users.ox.ac.uk/%7Erahtz/), [Denis Roegel](http://www.loria.fr/%7Eroegel/), [Herbert Voß](http://www.uit.co.uk/Authors/HerbVoss) (**2007**). *[The LATEXGraphics Companion](http://xml.web.cern.ch/XML/lgc2/)*. Second Edition, Addison-Wesley, ISBN-13: 978-0-321-50892-8, [sample pdf](http://ptgmedia.pearsoncmg.com/images/9780321508928/samplepages/0321508920_Sample.pdf), 10.1 Chess, 10.2 Xiangqi—Chinese Chess <a id="cite-note-17" href="#cite-ref-17">[17]</a>

## Forum Posts

## 2000 ...

- [correct SAN notation ?](https://www.stmintz.com/ccc/index.php?id=271760) by [Andreas Herrmann](Andreas_Herrmann "Andreas Herrmann"), [CCC](CCC "CCC"), December 19, 2002
- [Crafty (under winboard) question](https://www.stmintz.com/ccc/index.php?id=337347) by [Andrei Fortuna](Andrei_Fortuna "Andrei Fortuna"), [CCC](CCC "CCC"), December 21, 2003 » [WinBoard](WinBoard "WinBoard")

## 2010 ...

- [SAN Move Disambiguation -- looking for test positition](http://www.talkchess.com/forum/viewtopic.php?t=33764) by humble programmer, [CCC](CCC "CCC"), April 12, 2010 » [PGN](Portable_Game_Notation "Portable Game Notation")
- [Unicode values for chessmen](http://www.talkchess.com/forum/viewtopic.php?t=38318) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 07, 2011
- [Determining From squares](http://www.talkchess.com/forum/viewtopic.php?t=41322) by David Whitten, [CCC](CCC "CCC"), December 04, 2011
- [What world have I been in - castling notation?](http://www.talkchess.com/forum/viewtopic.php?t=53686) by Lonnie Cook, [CCC](CCC "CCC"), September 13, 2014
- [SAN test position](http://www.talkchess.com/forum/viewtopic.php?t=61393) by [Matthew Lai](Matthew_Lai "Matthew Lai"), [CCC](CCC "CCC"), September 11, 2016 » [SAN](Algebraic_Chess_Notation#SAN "Algebraic Chess Notation")
- [WAC using coordinate notation?](http://www.talkchess.com/forum/viewtopic.php?t=65193) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), September 17, 2017 » [Pure coordinate notation](Algebraic_Chess_Notation#PureCoordinateNotation "Algebraic Chess Notation"), [Win at Chess](Win_at_Chess "Win at Chess")

## 2020 ...

- [Optimised Algebraic Notation](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78770) by Dmitry Shechtman, [CCC](CCC "CCC"), November 29, 2021

## External Links

- [Algebraic chess notation from Wikipedia](https://en.wikipedia.org/wiki/Algebraic_chess_notation)
- [Desciptive notation from Wikipedia](https://en.wikipedia.org/wiki/Descriptive_chess_notation)
- [Punctuation (chess) from Wikipedia](https://en.wikipedia.org/wiki/Punctuation_%28chess%29)
- [Chess symbols in Unicode from Wikipedia](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode)
- [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](Steven_Edwards "Steven Edwards") - 8.2.3: Movetext SAN (Standard Algebraic Notation)
- [SAN Kit: Implemented Standards for Chess Move Notation](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/games/chess/san/) by [Steven Edwards](Steven_Edwards "Steven Edwards")
- [FIDE handbook, Laws of Chess - Appendix C. Algebraic notation](http://www.fide.com/component/handbook/?id=171&view=article)
- [Smith notation](https://web.archive.org/web/20160117212352/https://www.chessclub.com/chessviewer/smith.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Chess Engine Communication Protocol: 8. Commands from xboard to the engine](http://home.hccnet.nl/h.g.muller/engine-intf.html#8)
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [The UCI Specification](http://www.shredderchess.com/chess-info/features/uci-universal-chess-interface.html)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> *Processor Technology 8080 CHESS User's Manual*. [pdf](http://www.sol20.org/manuals/chess.pdf), [pdf](http://www.imsai.net/support/processor_tech/chess.pdf)
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Kempelen Chess from Sierra Online](http://www.spacious-mind.com/html/c64_emu_-_kempelen.html) from [The Spacious Mind](The_Spacious_Mind "The Spacious Mind")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Smith notation](https://web.archive.org/web/20160117212352/https://www.chessclub.com/chessviewer/smith.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Aart's Android Page](http://www.aartbik.com/MISC/android.html)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [FIDE handbook, Laws of Chess - Appendix C. Algebraic notation](http://www.fide.com/component/handbook/?id=171&view=article)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) by [Steven Edwards](Steven_Edwards "Steven Edwards") - 8.2.3: Movetext SAN (Standard Algebraic Notation)
1. <a id="cite-ref-9" href="#cite-note-9">↑</a> [SAN Kit: Implemented Standards for Chess Move Notation](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/games/chess/san/) by [Steven Edwards](Steven_Edwards "Steven Edwards")
1. <a id="cite-ref-10" href="#cite-note-10">↑</a> [Aart's Android Page](http://www.aartbik.com/MISC/android.html)
1. <a id="cite-ref-11" href="#cite-note-11">↑</a> [FIDE handbook, Laws of Chess - Appendix C. Algebraic notation, C-9](http://www.fide.com/component/handbook/?id=171&view=article)
1. <a id="cite-ref-12" href="#cite-note-12">↑</a> [FIDE handbook, Laws of Chess - Appendix C. Algebraic notation - C.13 Abbreviations](http://www.fide.com/component/handbook/?id=171&view=article)
1. <a id="cite-ref-13" href="#cite-note-13">↑</a> [Chess Engine Communication Protocol: 9. Commands from the engine to xboard](http://home.hccnet.nl/h.g.muller/engine-intf.html#9)
1. <a id="cite-ref-14" href="#cite-note-14">↑</a> [Unicode values for chessmen](http://www.talkchess.com/forum/viewtopic.php?t=38318) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 07, 2011
1. <a id="cite-ref-15" href="#cite-note-15">↑</a> [Michel Goossens](http://goossens.web.cern.ch/goossens/), [Frank Mittelbach](http://www.informit.com/authors/bio.aspx?a=A2624A62-C2B4-40F9-B8ED-E99563F89A27), [Sebastian Rahtz](http://users.ox.ac.uk/%7Erahtz/), [Denis Roegel](http://www.loria.fr/%7Eroegel/), [Herbert Voß](http://www.uit.co.uk/Authors/HerbVoss) (**2007**). *[The LATEXGraphics Companion](http://xml.web.cern.ch/XML/lgc2/)*. Second Edition, Addison-Wesley, ISBN-13: 978-0-321-50892-8, [sample pdf](http://ptgmedia.pearsoncmg.com/images/9780321508928/samplepages/0321508920_Sample.pdf), 10.1 Chess, 10.2 Xiangqi—Chinese Chess
1. <a id="cite-ref-16" href="#cite-note-16">↑</a> [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
1. <a id="cite-ref-17" href="#cite-note-17">↑</a> [LaTeX from Wikipedia](https://en.wikipedia.org/wiki/LaTeX)

**[Up one Level](Game_Notation "Game Notation")**

