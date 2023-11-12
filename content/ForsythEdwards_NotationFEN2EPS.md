---
title: ForsythEdwards NotationFEN2EPS
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Forsyth-Edwards Notation**

**Forsyth-Edwards Notation** (**FEN**) describes a [Chess Position](Chess_Position "Chess Position"). It is an one-line [ASCII](https://en.wikipedia.org/wiki/ASCII)-string. **FEN** is based on a system created by Scotsman [David Forsyth](David_Forsyth "David Forsyth") in the 19th century. [Steven Edwards](Steven_Edwards "Steven Edwards") specified the **FEN standard** for computer chess applications as part of the [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") <a id="cite-note-1" href="#cite-ref-1">[1]</a> .

## Contents

- [1 FEN Syntax](#fen-syntax)
  - [1.1 Piece Placement](#piece-placement)
  - [1.2 Side to move](#side-to-move)
  - [1.3 Castling ability](#castling-ability)
  - [1.4 En passant target square](#en-passant-target-square)
  - [1.5 Halfmove Clock](#halfmove-clock)
  - [1.6 Fullmove counter](#fullmove-counter)
- [2 Samples](#samples)
- [3 Chess960](#chess960)
  - [3.1 Shredder-FEN](#shredder-fen)
  - [3.2 X-FEN](#x-fen)
- [4 See also](#see-also)
- [5 Forum Posts](#forum-posts)
  - [5.1 1993 ...](#1993-...)
  - [5.2 2000 ...](#2000-...)
  - [5.3 2005 ...](#2005-...)
  - [5.4 2010 ...](#2010-...)
  - [5.5 2015 ...](#2015-...)
  - [5.6 2020 ...](#2020-...)
- [6 External Links](#external-links)
- [7 References](#references)

## FEN Syntax

One FEN string or record consists of **six** fields separated by a space character. The first four fields of the FEN specification are the same as the first four fields of the [EPD](Extended_Position_Description "Extended Position Description") specification.

*[Terminal and nonterminal symbols](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols) of a variant of [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) below are embedded in ' ' resp. \< >.*

```C++

<FEN> ::=  <Piece Placement>
       ' ' <Side to move>
       ' ' <Castling ability>
       ' ' <En passant target square>
       ' ' <Halfmove clock>
       ' ' <Fullmove counter>

```

## Piece Placement

The Piece Placement is determined rank by rank in [big-endian](Big-endian "Big-endian") order, that is starting at the 8th rank down to the first rank. Each rank is separated by the terminal symbol '/' (slash). One rank, scans piece placement in [little-endian](Little-endian "Little-endian") file-order from the A to H.

A decimal digit counts consecutive empty squares, the pieces are identified by a single letter from standard English names for chess pieces as used in the [Algebraic Chess Notation](Algebraic_Chess_Notation "Algebraic Chess Notation"). Uppercase letters are for white pieces, lowercase letters for black pieces.

```C++

<Piece Placement> ::= <rank8>'/'<rank7>'/'<rank6>'/'<rank5>'/'<rank4>'/'<rank3>'/'<rank2>'/'<rank1>
<ranki>       ::= [<digit17>]<piece> {[<digit17>]<piece>} [<digit17>] | '8'
<piece>       ::= <white Piece> | <black Piece>
<digit17>     ::= '1' | '2' | '3' | '4' | '5' | '6' | '7'
<white Piece> ::= 'P' | 'N' | 'B' | 'R' | 'Q' | 'K'
<black Piece> ::= 'p' | 'n' | 'b' | 'r' | 'q' | 'k'

```

## Side to move

[Side to move](Side_to_move "Side to move") is one lowercase letter for either White ('w') or Black ('b').

```C++

<Side to move> ::= {'w' | 'b'}

```

## Castling ability

If neither side can castle, the symbol '-' is used, otherwise each of four individual [castling rights](Castling_Rights "Castling Rights") for king and queen castling for both sides are indicated by a sequence of one to four letters.

```C++

<Castling ability> ::= '-' | ['K'] ['Q'] ['k'] ['q'] (1..4)

```

## En passant target square

The [en passant](En_passant "En passant") target square is specified after a double push of a pawn, no matter whether an en passant capture is really possible or not <a id="cite-note-2" href="#cite-ref-2">[2]</a> <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a> . Other moves than double pawn pushes imply the symbol '-' for this FEN field.

```C++

<En passant target square> ::= '-' | <epsquare>
<epsquare>   ::= <fileLetter> <eprank>
<fileLetter> ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h'
<eprank>     ::= '3' | '6'

```

## Halfmove Clock

The [halfmove clock](Halfmove_Clock "Halfmove Clock") specifies a decimal number of half moves with respect to the [50 move draw rule](Fifty-move_Rule "Fifty-move Rule"). It is reset to zero after a capture or a pawn move and incremented otherwise.

```C++

<Halfmove Clock> ::= <digit> {<digit>}
<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

```

## Fullmove counter

The number of the full moves in a game. It starts at 1, and is incremented after each Black's move.

```C++

<Fullmove counter> ::= <digit19> {<digit>}
<digit19> ::= '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
<digit>   ::= '0' | <digit19>

```

## Samples

FEN strings of Starting Position and after 1.e4 c5 2.Nf3:

|  |
| --- |
|                                                                 ♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟                                ♙♙♙♙♙♙♙♙♖♘♗♕♔♗♘♖ |

```C++
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

```

|  |
| --- |
|                                                                 ♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟                    ♙           ♙♙♙♙ ♙♙♙♖♘♗♕♔♗♘♖ |

1.e4

```C++
rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1

```

|  |
| --- |
|                                                                 ♜♞♝♛♚♝♞♜♟♟ ♟♟♟♟♟          ♟         ♙           ♙♙♙♙ ♙♙♙♖♘♗♕♔♗♘♖ |

1.e4 c5

```C++
rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2

```

|  |
| --- |
|                                                                 ♜♞♝♛♚♝♞♜♟♟ ♟♟♟♟♟          ♟         ♙        ♘  ♙♙♙♙ ♙♙♙♖♘♗♕♔♗ ♖ |

1.e4 c5 2.Nf3

```C++
rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2 

```

## Chess960

## Shredder-FEN

**Shredder-FEN** or **SMK-FEN** is an extension of FEN covering [Chess960](Chess960 "Chess960"), introduced by [Shredder](Shredder "Shredder") author [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen") (SMK) in 2005.
Shredder-FEN uses different [castling right](Castling_Rights "Castling Rights") characters, that is instead of **KQkq**, upper case and lower case [file characters](Files "Files") of the affected rooks for white and black castling rights, and became a [de facto standard](https://en.wikipedia.org/wiki/De_facto_standard) supported by most [GUIs](GUI "GUI") and [protocols](Protocols "Protocols").

## X-FEN

The earlier [X-FEN](https://en.wikipedia.org/wiki/X-FEN) extension was introduced by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl") in 2003, and covers not only [Chess960](Chess960 "Chess960") but also 10x8 variants. Its author dogmatically claimed upward compatibility with standard chess <a id="cite-note-5" href="#cite-ref-5">[5]</a>, still using the **KQkq** [castling right](Castling_Rights "Castling Rights") characters for all Chess960 positions. Further, X-FEN introduced a changed [en passant](En_passant "En passant") target square semantic, which is only specified after a double pawn push was made beside an opponent pawn that might capture en passant if legal, that is not leaving its king in check.

## See also

- [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD)
- [Forsyth-Edwards Expanded Notation](index.php?title=Forsyth-Edwards_Expanded_Notation&action=edit&redlink=1 "Forsyth-Edwards Expanded Notation (page does not exist)") (FEEN)
- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") (PGN)
- [BMI2 FEN Compression](BMI2#FEN_Compression "BMI2")

## Forum Posts

## 1993 ...

- [Revised PGN standard available](https://groups.google.com/d/msg/rec.games.chess/MkLV6dIwGU4/GfbtTyR6o6sJ) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), December 20, 1993 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")
- [Full definition for FEN](https://www.stmintz.com/ccc/index.php?id=53266) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), May 27, 1999

## 2000 ...

- [File name extensions](https://www.stmintz.com/ccc/index.php?id=138460) by [Leen Ammeraal](Leen_Ammeraal "Leen Ammeraal"), [CCC](CCC "CCC"), November 14, 2000
- [Ten years later: revising EPD/FEN/PGN](https://www.stmintz.com/ccc/index.php?id=314898) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 09, 2003
- [Making positions in eps](https://www.stmintz.com/ccc/index.php?id=323898) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), October 27, 2003 » [Fen2eps](Forsyth-Edwards_Notation#FEN2EPS "Forsyth-Edwards Notation")

## 2005 ...

- [Why to use compatible X-FEN (in Chess960)](https://www.stmintz.com/ccc/index.php?id=437213) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), July 17, 2005
- [Chess960: X-FEN rules international](https://www.stmintz.com/ccc/index.php?id=439792) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), August 03, 2005
- [contradicting FEN and SMK-FEN](https://www.stmintz.com/ccc/index.php?id=439995) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), August 04, 2005
- [Chess960: Arena castle vs X-FEN castle](https://www.stmintz.com/ccc/index.php?id=459898) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 05, 2005
- [fen to fen functions](http://www.talkchess.com/forum/viewtopic.php?t=13923) by [Uri Blass](Uri_Blass "Uri Blass"), [CCC](CCC "CCC"), May 21, 2007

## 2010 ...

- [where FEN is not consistent](http://www.talkchess.com/forum/viewtopic.php?t=31521) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), January 06, 2010
- [FEN string](http://www.talkchess.com/forum/viewtopic.php?t=37879) by colin, [CCC](CCC "CCC"), January 30, 2011
- [No more pseudolegal en passant target foolishness](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=396838&t=37879) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 27, 2011
- [What's wrong with this EPD?](http://www.talkchess.com/forum/viewtopic.php?t=38488) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 20, 2011
- [Question about Shredder FEN and X-FEN](http://www.talkchess.com/forum/viewtopic.php?t=43417) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), April 22, 2012
- [Re: Causes for inconsistent benchmark signatures](http://www.talkchess.com/forum/viewtopic.php?t=47622&start=6) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 27, 2013 » [En passant](En_passant "En passant")
- [The maximum character length of a FEN string](http://www.talkchess.com/forum/viewtopic.php?t=49083) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), August 24, 2013
- [Is 79 maximal?](http://www.talkchess.com/forum/viewtopic.php?t=53120) by [Louis Zulli](Louis_Zulli "Louis Zulli"), [CCC](CCC "CCC"), July 29, 2014
- [PGN to FEN (with Evaluation)?](http://www.talkchess.com/forum/viewtopic.php?t=54779) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 28, 2014 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"), [Python](Python "Python")

## 2015 ...

- [Binary FEN](http://www.talkchess.com/forum/viewtopic.php?t=57065) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 24, 2015
- [Any tool to convert FEN strings to diagrams?](http://www.talkchess.com/forum/viewtopic.php?t=59255) by Ted Wong, [CCC](CCC "CCC"), February 15, 2016
- [FEN - Flipper for Windows](http://www.talkchess.com/forum/viewtopic.php?t=64003) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), May 17, 2017 » [Color Flipping](Color_Flipping "Color Flipping"), [EPD](Extended_Position_Description "Extended Position Description")
- [50 move counter in FEN and GUIs](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=72308) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), November 12, 2019

## 2020 ...

- [FEN and 3rd repetition rule. No information?](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73552) by [Luis Babboni](index.php?title=Luis_Babboni&action=edit&redlink=1 "Luis Babboni (page does not exist)"), [CCC](CCC "CCC"), April 03, 2020 » [Repetitions](Repetitions "Repetitions")
- [FEN compression](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76892) by lucasart, [CCC](CCC "CCC"), March 17, 2021 » [FEN Compression](BMI2#FEN_Compression "BMI2"), [NNUE Training](NNUE#Training "NNUE")
- [Required fields in Forsyth-Edwards Notation (FEN)](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=79627) by [Niels Abildskov](Niels_Abildskov "Niels Abildskov"), [CCC](CCC "CCC"), April 02, 2022

## External Links

- [Forsyth-Edwards Notation from Wikipedia](https://en.wikipedia.org/wiki/Forsyth-Edwards_Notation)
- [Chess Programming - Chess Board Implementation : A FEN parser](http://www.fam-petzke.de/cp_fen_en.shtml) by [Thomas Petzke](Thomas_Petzke "Thomas Petzke")
- [FEN Database](http://mathieupage.com/?p=65) by [Mathieu Pagé](Mathieu_Pag%C3%A9 "Mathieu Pagé")
- [Gilith - Chess Diagram Maker](http://www.gilith.com/chess/diagrams/) by [Joe Leslie-Hurd](Joe_Leslie-Hurd "Joe Leslie-Hurd")

[fen2img Chess Diagram Maker](http://www.gilith.com/software/fen2img/) by [Joe Leslie-Hurd](Joe_Leslie-Hurd "Joe Leslie-Hurd")

- [Chess Diagram Generator](http://webchess.freehostia.com/diag/index.php)
- [GitHub - bagaturchess/ChessBoardScanner: Java based Chess Board Scanner, which converts 2D chess board image into a machine readable format a.k.a. Forsyth–Edwards Notation (FEN)](https://github.com/bagaturchess/ChessBoardScanner) by [Krasimir Topchiyski](Krasimir_Topchiyski "Krasimir Topchiyski")
- [Chessforeva: 3D chess diagram from FEN](http://chessforeva.blogspot.de/2009/10/3d-chess-diagram-from-fen.html) » [3D Graphics Board](3D_Graphics_Board "3D Graphics Board")
- [Fen2eps](http://fen2eps.sourceforge.net/) by [Dirk Baechle](index.php?title=Dirk_Baechle&action=edit&redlink=1 "Dirk Baechle (page does not exist)") <a id="cite-note-6" href="#cite-ref-6">[6]</a>

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) 16.1: FEN by [Steven Edwards](Steven_Edwards "Steven Edwards")
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Re: Arasan test suite update](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=219015&t=23806) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), September 19, 2008
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [where FEN is not consistent](http://www.talkchess.com/forum/viewtopic.php?t=31521) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), January 06, 2010
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [No more pseudolegal en passant target foolishness](http://www.talkchess.com/forum/viewtopic.php?topic_view=threads&p=396838&t=37879) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), February 27, 2011
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Why to use compatible X-FEN (in Chess960)](https://www.stmintz.com/ccc/index.php?id=437213) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), July 17, 2005
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [Encapsulated PostScript from Wikipedia](https://en.wikipedia.org/wiki/Encapsulated_PostScript)

**[Up one Level](Chess_Position "Chess Position")**

