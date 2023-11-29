---
title: EPD
---
(Redirected from [EPD](index.php?title=EPD&redirect=no "EPD"))


**[Home](Home "Home") * [Chess](Chess "Chess") * [Position](Chess_Position "Chess Position") * Extended Position Description**

**Extended Position Description** (**EPD**)

describes a chess position similar to the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN). Unlike FEN, **EPD** is designed to be expandable by the addition of new operations. **EPD** was developed by [John Stanback](John_Stanback "John Stanback") and [Steven Edwards](Steven_Edwards "Steven Edwards"). Its first implementation is in Stanback's chessplaying program [Zarkov](Zarkov "Zarkov"). Steven Edwards specified the **EPD** standard for computer chess applications as part of the [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") <a id="cite-note-1" href="#cite-ref-1">[1]</a>.

## EPD Syntax

One EPD string or record consists of one text line of variable length composed of four fields separated by a space character followed by zero or more operations. The four data fields, which describe the position, are common with the [FEN-Specification](Forsyth-Edwards_Notation#FEN_Syntax "Forsyth-Edwards Notation"), while the [halfmove clock](Halfmove_Clock "Halfmove Clock") and [full move counter](Forsyth-Edwards_Notation#Fullmovecounter "Forsyth-Edwards Notation"), obligatory in Forsyth-Edwards Notation are replaced by optional **hmvc** and **fmvn** operations, and 0, 1 are their default values <a id="cite-note-2" href="#cite-ref-2">[2]</a>.

*[Terminal and none terminal symbols](https://en.wikipedia.org/wiki/Terminal_and_nonterminal_symbols) of a variant of [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) below are embedded in ' ' resp. \< >.*

```C++
<EPD> ::=  <Piece Placement>
       ' ' <Side to move>
       ' ' <Castling ability>
       ' ' <En passant target square>
      {' ' <operation>}

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

Side to move is one lowercase letter for either White ('w') or Black ('b').

```C++
<Side to move> ::= {'w' | 'b'}

```

## Castling ability

If neither side can castle, the symbol '-' is used, otherwise each of four individual [castling rights](Castling_Rights "Castling Rights") for king and queen castling for both sides are indicated by a sequence of one to four letters.

```C++
<Castling ability> ::= '-' | ['K'] ['Q'] ['k'] ['q'] (1..4)

```

## En passant target square

The [en passant](En_passant "En passant") target square is specified after a double push of a pawn, no matter whether an en passant capture is really possible or not. Other moves than double pawn pushes imply the symbol '-' for this FEN field.

```C++
<En passant target square> ::= '-' | <epsquare>
<epsquare>   ::= <fileLetter> <eprank>
<fileLetter> ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h'
<eprank>     ::= '3' | '6'

```

## Operations

```C++
<operation> ::= <opcode> {' '<operand>} ';'
<opcode>    ::= <letter> {<letter> | <digit> | '_'} (up to 14)
<operand>   ::= <stringOperand>
              | <sanMove>
              | <unsignedOperand>
              | <integerOperand>
              | <floatOperand>

<stringOperand>  ::= '"' {<char>} '"'

<sanMove>        ::= <PieceCode> [<Disambiguation>] <targetSquare> [<promotion>] ['+'|'#']
                   | <castles>
<castles>        ::= 'O-O' | 'O-O-O' (upper case O, not zero)
<PieceCode>      ::= '' | 'N' | 'B' | 'R' | 'Q' | 'K'
<Disambiguation> ::= <fileLetter> | <digit18>
<targetSquare>   ::= <fileLetter> <digit18>
<fileLetter> ::= 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h'
<promotion>      ::=  '=' <PiecePromotion>
<PiecePromotion> ::= 'N' | 'B' | 'R' | 'Q'

<unsignedOperand>::= <digit19> { <digit> } | '0'
<integerOperand> ::= ['-' | '+'] <unsignedIntegerOperand>
<floatOperand>   ::= <integerOperand> '.' <digit> {<digit>}
<digit18> ::= '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8'
<digit19> ::= '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
<digit>   ::= '0' | <digit19>

```

## Opcode mnemonics

- **acd** analysis count [depth](Depth "Depth") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- **acn** analysis count [nodes](Node "Node")
- **acs** analysis count seconds
- **am** avoid move(s)
- **bm** best move(s)
- **c0** comment (primary, also **c1** though **c9**)
- **ce** [centipawn](Centipawns "Centipawns") evaluation
- **dm** direct mate fullmove count
- **draw_accept** accept a draw offer
- **draw_claim** claim a draw
- **draw_offer** offer a draw
- **draw_reject** reject a draw offer
- **eco** [Encyclopedia of Chess Openings](ECO "ECO") opening code
- **fmvn** fullmove number
- **hmvc** [halfmove clock](Halfmove_Clock "Halfmove Clock")
- **id** position identification
- **nic** [New In Chess](NIC-Key "NIC-Key") opening code
- **noop** no operation
- **pm** predicted move
- **pv** predicted variation
- **rc** repetition count
- **resign** game resignation
- **sm** supplied move
- **tcgs** telecommunication game selector
- **tcri** telecommunication receiver identification
- **tcsi** telecommunication sender identification
- **v0** variation name (primary, also **v1** though **v9**)

## Examples

The start position:

```C++
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - hmvc 0; fmvn 1;

```

Other EPD strings from some tests:

```C++
r1bqk2r/p1pp1ppp/2p2n2/8/1b2P3/2N5/PPP2PPP/R1BQKB1R w KQkq - bm Bd3; id "Crafty Test Pos.28"; c0 "DB/GK Philadelphia 1996, Game 5, move 7W (Bd3)";
8/3r4/pr1Pk1p1/8/7P/6P1/3R3K/5R2 w - - bm Re2+; id "arasan21.16"; c0 "Aldiga (Brainfish 091016)-Knight-king (Komodo 10 64-bit), playchess.com 2016";
3r1rk1/1p3pnp/p3pBp1/1qPpP3/1P1P2R1/P2Q3R/6PP/6K1 w - - bm Rxh7;c0 "Mate in 7 moves";id "BT2630-14";

```

## See also

- [Chess Artist](Ferdinand_Mosca#ChessArtist "Ferdinand Mosca") by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca")
- [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN)
- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") (PGN)

## Forum Posts

- [Help on PGN/ EPD-Format and its implementation wanted](https://groups.google.com/d/msg/rec.games.chess.computer/0-xpXHbfzh4/GoKIkW0SKoUJ) by [Rudolf Posch](Rudolf_Posch "Rudolf Posch"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), November 05, 1996 » [PGN](Portable_Game_Notation "Portable Game Notation")
- [EPD examples: Bratko-Kopec test suite](https://www.stmintz.com/ccc/index.php?id=20631) by [Steven J. Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), June 15, 1998 » [Bratko-Kopec Test](Bratko-Kopec_Test "Bratko-Kopec Test")
- [EPD format](https://www.stmintz.com/ccc/index.php?id=137052) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), November 07, 2000
- [Question about EPD](https://www.stmintz.com/ccc/index.php?id=155201) by [Aaron Tay](Aaron_Tay "Aaron Tay"), [CCC](CCC "CCC"), February 20, 2001
- [XBoard and epd tournament](http://www.talkchess.com/forum/viewtopic.php?t=32254) by [Vlad Stamate](Vlad_Stamate "Vlad Stamate"), [CCC](CCC "CCC"), January 31, 2010 » [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol"), [Engine Testing](Engine_Testing "Engine Testing")
- [What's wrong with this EPD?](http://www.talkchess.com/forum/viewtopic.php?t=38488) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), March 20, 2011
- [epd multipv](http://www.talkchess.com/forum/viewtopic.php?t=57108) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 28, 2015 » [Principal Variation](Principal_Variation "Principal Variation")
- [Test epd for Linux ?](http://www.talkchess.com/forum/viewtopic.php?t=59633) by Jean Arthuin, [CCC](CCC "CCC"), March 25, 2016 » [Linux](Linux "Linux"), [STS](Strategic_Test_Suite "Strategic Test Suite"), [XBoard](XBoard "XBoard")
- [FEN - Flipper for Windows](http://www.talkchess.com/forum/viewtopic.php?t=64003) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), May 17, 2017 » [Color Flipping](Color_Flipping "Color Flipping"), [FEN](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- [how to create a labeled epd from pgn?](http://www.talkchess.com/forum/viewtopic.php?t=65881) by [Erin Dame](Erin_Dame "Erin Dame"), [CCC](CCC "CCC"), December 02, 2017 » [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method"), [PGN](Portable_Game_Notation "Portable Game Notation")
- [Fun challenge for best cool code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70048) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), February 28, 2019

[Re: Fun challenge for best cool code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70048&start=3) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 28, 2019

- [Scid vs. PC - EPD Export feature](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71135) by [Steven Atkinson](Steven_Atkinson "Steven Atkinson"), [CCC](CCC "CCC"), June 29, 2019 » [Scid vs. PC](Scid_vs._PC "Scid vs. PC")

## External Links

- [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) 16.2: EPD by [Steven Edwards](Steven_Edwards "Steven Edwards")
- [EPD to HTML/ASCII Diagram Converter](http://www.marochess.de/php3/epd2html.html) by [Manfred Rosenboom](http://www.marochess.de/biograph.html) <a id="cite-note-4" href="#cite-ref-4">[4]</a>
- [40H Chess Tools and Utilities](http://40h.000webhostapp.com/) by [Norm Pollock](index.php?title=Norman_Pollock&action=edit&redlink=1 "Norman Pollock (page does not exist)") » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation") <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> <a id="cite-note-7" href="#cite-ref-7">[7]</a>
- [Chess-Tools/epd2uci.py at master · Mk-Chan/Chess-Tools · GitHub](https://github.com/Mk-Chan/Chess-Tools/blob/master/epd2uci.py) by [Manik Charan](Manik_Charan "Manik Charan") » [Python](Python "Python"), [python-chess](Python-chess "Python-chess")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [Standard: Portable Game Notation Specification and Implementation Guide](http://www.thechessdrum.net/PGN_Reference.txt) 16.2: EPD by [Steven Edwards](Steven_Edwards "Steven Edwards")
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Re: Fun challenge for best cool code](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=70048&start=5) by [Harm Geert Muller](Harm_Geert_Muller "Harm Geert Muller"), [CCC](CCC "CCC"), February 28, 2019
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [EPD format](https://www.stmintz.com/ccc/index.php?id=137052) by [Stefan Meyer-Kahlen](Stefan_Meyer-Kahlen "Stefan Meyer-Kahlen"), [CCC](CCC "CCC"), November 07, 2000
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [EPD2diag](http://www.rebel.nl/epd2diag.htm) hosted by [Ed Schröder](Ed_Schroder "Ed Schroder")
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [An important message to users of 40H utility tools](http://www.talkchess.com/forum/viewtopic.php?t=58581) by [Norm Pollock](index.php?title=Norman_Pollock&action=edit&redlink=1 "Norman Pollock (page does not exist)"), [CCC](CCC "CCC"), December 13, 2015
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Re: 40H chess downloads has moved](http://www.talkchess.com/forum/viewtopic.php?t=59376&start=1) by [Norm Pollock](index.php?title=Norman_Pollock&action=edit&redlink=1 "Norman Pollock (page does not exist)"), [CCC](CCC "CCC"), March 12, 2016
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [Moved "40H" tools/utilities to a new URL](http://www.talkchess.com/forum/viewtopic.php?t=62554) by[Norm Pollock](index.php?title=Norman_Pollock&action=edit&redlink=1 "Norman Pollock (page does not exist)"), [CCC](CCC "CCC"), December 21, 2016

**[Up one Level](Chess_Position "Chess Position")**

