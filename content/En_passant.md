---
title: En passant
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Moves](Moves "Moves") * En passant**

**En passant** (from French: "in passing") <a id="cite-note-1" href="#cite-ref-1">[1]</a> is a special [pawn](Pawn "Pawn") [capture move](Captures "Captures"), which is only possible immediately after an opposing pawn tried passing an advanced pawn on the fifth [rank](Ranks "Ranks") (or fourth for black pawns) by a [double pawn push](Pawn_Push#DoublePush "Pawn Push"). This double pushed pawn can then be captured the same way, as it would only performed a single push - but only as an immediate reply.

This chess rule makes chess programming a bit harder. First, the target square of the en passant capture is not identical with origin of the captured pawn, opposed to all other captures. Second, the double pawn push, which triggered the immediate possibility of an en passant capture, must be part of the [chess position](Chess_Position "Chess Position"). The information required is whether there was a previous pawn push, and if so, at least the [file number](Files "Files") of that pawn, considered as [en passant target square](Forsyth-Edwards_Notation#Enpassanttargetsquare "Forsyth-Edwards Notation") inside the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN), albeit with the redundant rank (3 or 6) as well.

## Legality Test

To prove an en passant capture is actually possible, at least the [en passant target square](Forsyth-Edwards_Notation#Enpassanttargetsquare "Forsyth-Edwards Notation") should be under attack of an opponent pawn for [pseudo legality](Pseudo-Legal_Move "Pseudo-Legal Move"). Further, for [strict legality](Legal_Move "Legal Move"), the ep capturing pawn should not be [absolutely pinned](Pin#AbsolutePin "Pin"), which additionally requires a horizontal pin test of both involved pawns, which disappear from the same rank.

|  |
| --- |
|                                                                                                      ♝♝                ♖ ♟♙  ♚     ♙   ♙       ♔        |

```C++
8/6bb/8/8/R1pP2k1/4P3/P7/K7 b - d3 after d2-d4

```

The legality test should be best applied in [making](Make_Move "Make Move") of the [double pawn push](Pawn_Push#DoublePush "Pawn Push"), also considering [updating](Incremental_Updates "Incremental Updates") [Zobist keys](Zobrist_Hashing "Zobrist Hashing") to avoid dissimilarity of otherwise [repeated](Repetitions "Repetitions") [positions](Chess_Position "Chess Position") if the first occurrence happened after a double pawn push with no en passant capture actually possible <a id="cite-note-2" href="#cite-ref-2">[2]</a> .

## En passant bugs

The implementation of the en passant rule often caused subtle [bugs](Engine_Testing#bugs "Engine Testing"). Almost every chess programmer had various issues with it <a id="cite-note-3" href="#cite-ref-3">[3]</a> , most notable [Louis Kessler](Louis_Kessler "Louis Kessler") with his [Program Brute Force](</Brute_Force_(Program)> "Brute Force (Program)"). [Gerd Isenberg](Gerd_Isenberg "Gerd Isenberg") had a special en passant experience with [IsiChess](IsiChess "IsiChess") at [Aegon 1994](Aegon_1994 "Aegon 1994") in the game versus Henk Arnoldus. IsiChess pushed its white pawn from b2 to b4 "between" the two advanced pawns a4 and c4 from Henk, allowing two possible en passant options. Unfortunately IsiChess only generated one - the "wrong" one (an assembly bug due to jc instead if jnz or that like, otherwise it would not have played it), and was immediately lost after Henk played the "right" one <a id="cite-note-4" href="#cite-ref-4">[4]</a> <a id="cite-note-5" href="#cite-ref-5">[5]</a> :

```

[Event "9th AEGON man-comp"]
[Site "The Hague NED"]
[Date "1994.05.02"]
[Round "4"]
[White "IsiChess"]
[Black "Henk Arnoldus"]
[Result "0-1"]

1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 b6 6.Ngf3 Ba6 7.O-O Bxd3
8.cxd3 Be7 9.Nb3 O-O 10.Bd2 Na6 11.Qe2 Qc8 12.Rac1 Qb7 13.Rc2 c5
14.Rfc1 Rfc8 15.dxc5 bxc5 16.Qe3 Nb4 17.Bxb4 Qxb4 18.Nbd2 a5 19.a3 Qb7
20.Kh1 Ra6 21.d4 c4 22.Qc3 a4 23.b4 axb3 24.Nxb3 Rxa3 25.Nfd2 Rb8
26.Rb1 cxb3 27.Rcb2 Bb4 28.Qc1 Bxd2 29.Rxd2 Ra2 30.Rdb2 Rxb2
31.Qxb2 Qb4 32.f4 g6 33.h3 Qc4 34.Rc1 Qd3 35.f5 Qxf5 0-1

```

|  |
| --- |
|                                                                         ♜   ♚  ♛ ♞♝♟♟♟♜   ♟      ♟♙   ♟♙♟♙    ♙ ♕  ♘    ♖♘ ♙♙♙  ♖    ♔ |

```C++
2r3k1/1q1nbppp/r3p3/3pP3/pPpP4/P1Q2N2/2RN1PPP/2R4K b - b3 0 23

```

## See also

- [Algebraic Chess Notation - En passant](Algebraic_Chess_Notation#Enpassant "Algebraic Chess Notation")
- [Captures](Captures "Captures")
- [Castling](Castling "Castling")
- [FEN - En passant target square](Forsyth-Edwards_Notation#Enpassanttargetsquare "Forsyth-Edwards Notation")

## Forum Posts

## 1999

- [Hash Tables - Should one store EP, Castling rights etc?](https://www.stmintz.com/ccc/index.php?id=41612) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), January 30, 1999 » [Castling Rights](Castling_Rights "Castling Rights"), [Transposition Table](Transposition_Table "Transposition Table")
- [en-passant move generation](https://www.stmintz.com/ccc/index.php?id=42421) by Larry Griffiths, [CCC](CCC "CCC"), February 06, 1999
- [Unique nodes, en passant and perfect hashing](https://www.stmintz.com/ccc/index.php?id=79362) by Andreas Stabel, [CCC](CCC "CCC"), November 25, 1999

## 2000 ...

- [Does your program understand castling/en passant rights on 3x repetition](https://www.stmintz.com/ccc/index.php?id=99216) by Richard A. Fowell, [CCC](CCC "CCC"), February 27, 2000 » [Castling Rights](Castling_Rights "Castling Rights"), [Repetitions](Repetitions "Repetitions")
- [annoying en passant x-ray](https://www.stmintz.com/ccc/index.php?id=332375) by [Georg von Zimmermann](Georg_von_Zimmermann "Georg von Zimmermann"), [CCC](CCC "CCC"), November 30, 2003

## 2005 ...

- [Programmer bug hunt challenge](http://www.talkchess.com/forum/viewtopic.php?t=13557) by [Ed Schröder](Ed_Schroder "Ed Schroder"), [CCC](CCC "CCC"), May 04, 2007 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")

## 2010 ...

- [en passant and hash key calculation](http://www.talkchess.com/forum/viewtopic.php?t=33397) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), March 21, 2010
- [Komodo 3 and a minor bug](http://www.talkchess.com/forum/viewtopic.php?t=40248) by [Jouni Uski](Jouni_Uski "Jouni Uski"), [CCC](CCC "CCC"), September 02, 2011
- [Re: Causes for inconsistent benchmark signatures](http://www.talkchess.com/forum/viewtopic.php?t=47622&start=6) by [Evert Glebbeek](Evert_Glebbeek "Evert Glebbeek"), [CCC](CCC "CCC"), March 27, 2013 » [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- [polyglot en passant square](http://www.talkchess.com/forum/viewtopic.php?t=49316) by [Marco Belli](Marco_Belli "Marco Belli"), [CCC](CCC "CCC"), September 12, 2013 » [PolyGlot](PolyGlot "PolyGlot")
- [ep and castle rights hashing](http://www.talkchess.com/forum/viewtopic.php?t=49362) by [Natale Galioto](index.php?title=Natale_Galioto&action=edit&redlink=1 "Natale Galioto (page does not exist)"), [CCC](CCC "CCC"), September 15, 2013 » [Castling Rights](Castling_Rights "Castling Rights"), [Repetitions](Repetitions "Repetitions"), [Transposition Table](Transposition_Table "Transposition Table")
- [Abundance of castling vs en passant rights](http://www.talkchess.com/forum/viewtopic.php?t=51988) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), [CCC](CCC "CCC"), April 14, 2014 » [Castling](Castling "Castling")
- [En-passant legality test](http://www.open-chess.org/viewtopic.php?f=5&t=2697) by tetra, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), August 07, 2014 » [Legal Move](Legal_Move "Legal Move")

## 2015 ...

- [En passant bonus](http://www.talkchess.com/forum/viewtopic.php?t=55290) by [Lyudmil Tsvetkov](Lyudmil_Tsvetkov "Lyudmil Tsvetkov"), [CCC](CCC "CCC"), February 10, 2015 » [Pawn Structure](Pawn_Structure "Pawn Structure")
- [Dynamic EP flag](http://www.open-chess.org/viewtopic.php?f=5&t=2885) by thevinenator, [OpenChess Forum](Computer_Chess_Forums "Computer Chess Forums"), October 02, 2015
- [Triple Repitition: Is this considered a repitition or not?](http://www.talkchess.com/forum/viewtopic.php?t=60075) by Jayakiran Akurathi, [CCC](CCC "CCC"), May 07, 2016 » [Repetitions](Repetitions "Repetitions")
- [Enpass + Castling for Zorbist hashes](http://www.talkchess.com/forum/viewtopic.php?t=62733) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), January 06, 2017 » [Castling Rights](Castling_Rights "Castling Rights"), [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing")
- [Stockfish Chess 8 - en passant rule](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=65218) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), September 19, 2017
- [3-fold repetition and cutechess-cli](http://www.talkchess.com/forum/viewtopic.php?t=66323) by Lars Mathiesen, [CCC](CCC "CCC"), January 14, 2018 » [Repetitions](Repetitions "Repetitions")
- [SYZYGY question](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71512) by [Robert Hyatt](Robert_Hyatt "Robert Hyatt"), [CCC](CCC "CCC"), August 11, 2019 » [Crafty](Crafty "Crafty"), [Syzygy Bases](Syzygy_Bases "Syzygy Bases")

## 2020 ...

- [Being silly with perft and legal move generation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77350) by [Jakob Progsch](index.php?title=Jakob_Progsch&action=edit&redlink=1 "Jakob Progsch (page does not exist)"), [CCC](CCC "CCC"), May 19, 2021 » [Perft](Perft "Perft"), [Legal Move Generation](Move_Generation#Legal "Move Generation")

## External Links

- [En passant from Wikipedia](https://en.wikipedia.org/wiki/En_passant)
- [Boylston Chess Club Weblog: En passant](http://boylston-chess-club.blogspot.com/2008/08/en-passant.html)
- [En Passant - The Bimonthly Journal of the Pittsburgh Chess Club](http://www.cs.cmu.edu/%7Ebwl/EnPassant.htm) by [Bruce W. Leverett](Bruce_W._Leverett "Bruce W. Leverett")

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Earliest Occurrences of Chess Terms](http://www.chesshistory.com/winter/extra/earliest.html) by [Edward Winter](https://en.wikipedia.org/wiki/Edward_Winter_%28chess_historian%29)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [en passant and hash key calculation](http://www.talkchess.com/forum/viewtopic.php?t=33397) by [Fred Hamilton](index.php?title=Fred_Hamilton&action=edit&redlink=1 "Fred Hamilton (page does not exist)"), [CCC](CCC "CCC"), March 21, 2010
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chrilly Donninger](Chrilly_Donninger "Chrilly Donninger") (**1999**). *Computer machen keine Fehler*. [CSS](Computerschach_und_Spiele "Computerschach und Spiele") 2/99, [pdf](http://www.mustrum.de/chrilly/keine_fehler.pdf) (German)
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [CSVN Downloads Games Aegon Tournaments](http://www.csvn.nl/index.php?option=com_docman&task=cat_view&gid=40&Itemid=26&lang=en)
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Aegon 1994 Round 4 (REPOST)](http://groups.google.com/group/rec.games.chess/browse_frm/thread/8dbd04e027108e0c) by [Dap Hartmann](Dap_Hartmann "Dap Hartmann"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), May 09, 1994

**[Up one Level](Moves "Moves")**

