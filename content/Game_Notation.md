---
title: Game Notation
---
**[Home](Home "Home") * [Chess](Chess "Chess") * [Game](Chess_Game "Chess Game") * Notation**

**Game Notation** refers to the recording of [moves](Moves "Moves") of the chess game including players or programs names, date, name of event and site - in human competitive chess each side is required to fill and sign a [score sheet](https://en.wikipedia.org/wiki/Scoresheet_%28chess%29#Score_sheet). In official computer chess over the board [tournaments](Tournaments_and_Matches "Tournaments and Matches"), it was required for human operators as well, but was practically relaxed since programs keep their internal [move list](Move_List "Move List") persistent and were able to restart for instance after a power failure <a id="cite-note-1" href="#cite-ref-1">[1]</a>. In Chess [GUIs](GUI "GUI"), the game notation is presented inside a [notation window](GUI#NotationWindow "GUI"), which may allow certain interactions, like scrolling the list, or replaying the game.

## Chess Notation

While the move numeration is quite obvious, starting with move number one, there are various [Chess notations](https://en.wikipedia.org/wiki/Chess_notation) with different move [syntax](https://en.wikipedia.org/wiki/Syntax) defined. Most common in printed and electronic chess media, also in chess programs and [databases](Databases "Databases"), is the [Algebraic Chess Notation](Algebraic_Chess_Notation "Algebraic Chess Notation"), especially its short form called [SAN](Algebraic_Chess_Notation#SAN "Algebraic Chess Notation"). [Descriptive chess notation](https://en.wikipedia.org/wiki/Descriptive_chess_notation) was used in English and Spanish-language literature until the late 20th century, but is today somehow obsolete.

Algebraic [figurine notation](Algebraic_Chess_Notation#FAN "Algebraic Chess Notation") (FAN) uses graphical [piece](Pieces "Pieces") symbols rather than national language dependent letters for pieces, early promoted by [Chess Informant](https://en.wikipedia.org/wiki/Chess_Informant). In an attempt of [Computer vision](https://en.wikipedia.org/wiki/Computer_vision), [Henry S. Baird](Mathematician#HSBaird "Mathematician") and [Ken Thompson](Ken_Thompson "Ken Thompson") used [optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) along with various heuristics and applying the rules of chess, to "read" the games of Informant's [Encyclopaedia of Chess Openings](https://en.wikipedia.org/wiki/Encyclopaedia_of_Chess_Openings) with high accuracy and a success rate of 99.995% on approximately one million characters (2850 games, 945 pages) <a id="cite-note-2" href="#cite-ref-2">[2]</a>. FAN is supported by various [chess GUIs](GUI "GUI"), corresponding [chess symbols](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) are available in [Unicode](https://en.wikipedia.org/wiki/Unicode) <a id="cite-note-3" href="#cite-ref-3">[3]</a> <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

## Sample Score sheet

## Image

Game Notation of [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) - [Miguel Najdorf](https://en.wikipedia.org/wiki/Miguel_Najdorf) in [Descriptive chess notation](https://en.wikipedia.org/wiki/Descriptive_chess_notation):

|  |
| --- |
| [Fischer Score Card.jpg](https://de.wikipedia.org/wiki/Schachnotation) |
| [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer) - [Miguel Najdorf](https://en.wikipedia.org/wiki/Miguel_Najdorf), [19th Chess Olympiad](https://en.wikipedia.org/wiki/19th_Chess_Olympiad), 1970, [Siegen](https://en.wikipedia.org/wiki/Siegen), [West Germany](https://en.wikipedia.org/wiki/West_Germany) <a id="cite-note-5" href="#cite-ref-5">[5]</a> <a id="cite-note-6" href="#cite-ref-6">[6]</a> |

## PGN

The above Game Notation in [SAN](Algebraic_Chess_Notation#SAN "Algebraic Chess Notation") as [Portable Game Notation](Portable_Game_Notation "Portable Game Notation"):

```
[Event "19th Chess Olympiad"]
[Site "Siegen, Germany"]
[Date "1970.??.??"]
[Round "3"]
[Result "1-0"]
[White "Robert James Fischer"]
[Black "Miguel Najdorf"]

1. e4 c5 2. Nf3 e6 3. d4 cxd4 4. Nxd4 a6 5. Bd3 Nf6 6. O-O d6
7. c4 Bd7 8. Nc3 Nc6 9. Be3 Be7 10. h3 Ne5 11. Be2 Rc8 12. Qb3
Qc7 13. Rac1 O-O 14. f4 Nc6 15. Nf3 Qb8 16. Qd1 Be8 17. Qd2
Na5 18. b3 b6 19. Bd3 Nc6 20. Qf2 b5 21. Rfd1 Nb4 22. Bf1 bxc4
23. bxc4 a5 24. Nd4 Qa8 25. Qf3 Na6 26. Ndb5 Nc5 27. e5 dxe5
28. Qxa8 Rxa8 29. fxe5 Nfe4 30. Nd6 Bc6 31. Ncxe4 Nxe4 32. c5
Ng3 33. Bc4 h5 34. Bf2 h4 35. Bxg3 hxg3 36. Bb5 Bxb5 37. Nxb5
f6 38. Rd7 Bd8 39. Rc3 fxe5 40. Rxg3 Rf7 41. Rxf7 Kxf7 42. c6
Bb6+ 43. Kf1 Kf8 44. c7 Rc8 45. a4 e4 46. Ke2 e5 47. Rg6 Bd4
48. h4 Bb2 1-0

```

## Notations

- [Algebraic Chess Notation](Algebraic_Chess_Notation "Algebraic Chess Notation")
- [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")

## See also

- [Encoding Moves](Encoding_Moves "Encoding Moves")
- [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation")
- [Chess Databases](Databases "Databases")
- [Graphical User Interface](GUI "GUI")
- [Move List](Move_List "Move List")

## Publications

- [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
- [Christian Wirth](index.php?title=Christian_Wirth&action=edit&redlink=1 "Christian Wirth (page does not exist)"), [Johannes Fürnkranz](Johannes_F%C3%BCrnkranz "Johannes Fürnkranz") (**2015**). *[On Learning From Game Annotations](http://ieeexplore.ieee.org/document/6861960/)*. [IEEE Transactions on Computational Intelligence and AI in Games](IEEE#TOCIAIGAMES "IEEE"), Vol. 7, No. 3

## Forum Posts

- [Chess Artist](http://www.talkchess.com/forum/viewtopic.php?t=61723) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), October 15, 2016 » [Chess Artist](Ferdinand_Mosca#ChessArtist "Ferdinand Mosca")
- [PGN score annotation tags wv and bv](http://www.talkchess.com/forum/viewtopic.php?t=66297) by [Dann Corbit](Dann_Corbit "Dann Corbit"), [CCC](CCC "CCC"), January 10, 2018 » [Portable Game Notation](Portable_Game_Notation "Portable Game Notation")
- [JGN: A PGN Replacement](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78626) by [Dominik Klein](Dominik_Klein "Dominik Klein"), [CCC](CCC "CCC"), November 09, 2021 <a id="cite-note-7" href="#cite-ref-7">[7]</a>

## External Links

- [Score sheet - Glossary of chess from Wikipedia](https://en.wikipedia.org/wiki/Scoresheet_%28chess%29#Score_sheet)
- [Chess notation from Wikipedia](https://en.wikipedia.org/wiki/Chess_notation)
- [Algebraic chess notation from Wikipedia](https://en.wikipedia.org/wiki/Algebraic_chess_notation)
- [Descriptive chess notation from Wikipedia](https://en.wikipedia.org/wiki/Descriptive_chess_notation)
- [ICCF numeric notation from Wikipedia](https://en.wikipedia.org/wiki/ICCF_numeric_notation)
- [Smith notation](https://web.archive.org/web/20160117212352/https://www.chessclub.com/chessviewer/smith.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)) by [Warren D. Smith](Warren_D._Smith "Warren D. Smith")
- [Chess symbols in Unicode from Wikipedia](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode)
- [Punctuation (chess) from Wikipedia](https://en.wikipedia.org/wiki/Punctuation_%28chess%29)
- [GitHub - fsmosca/chess-artist: A python script that can annotate chess games in pgn file ...](https://github.com/fsmosca/chess-artist) <a id="cite-note-8" href="#cite-ref-8">[8]</a> » [Chess Artist](Ferdinand_Mosca#ChessArtist "Ferdinand Mosca")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> really?
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Henry S. Baird](Mathematician#HSBaird "Mathematician"), [Ken Thompson](Ken_Thompson "Ken Thompson") (**1990**). *[Reading Chess](http://doc.cat-v.org/bell_labs/reading_chess/)*. [IEEE Transactions on Pattern Analysis and Machine Intelligence](IEEE#TPAMI "IEEE"), Vol. 12, No. 6, [pdf](http://doc.cat-v.org/bell_labs/reading_chess/reading_chess.pdf)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Unicode values for chessmen](http://www.talkchess.com/forum/viewtopic.php?t=38318) by [Steven Edwards](Steven_Edwards "Steven Edwards"), [CCC](CCC "CCC"), March 07, 2011
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Miscellaneous Symbols – Test for Unicode support in Web browsers](http://www.alanwood.net/unicode/miscellaneous_symbols.html)
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [JPEG BOBBY](http://www.echecs-photos.be/BobbyFischer-photos/index10.html)
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [Robert James Fischer vs Miguel Najdorf (1970)](http://www.chessgames.com/perl/chessgame?gid=1044320) from [chessgames.com](http://www.chessgames.com/index.html)
1. <a id="cite-ref-7" href="#cite-note-7">↑</a> [JSON from Wikipedia](https://en.wikipedia.org/wiki/JSON)
1. <a id="cite-ref-8" href="#cite-note-8">↑</a> [Chess Artist](http://www.talkchess.com/forum/viewtopic.php?t=61723) by [Ferdinand Mosca](Ferdinand_Mosca "Ferdinand Mosca"), [CCC](CCC "CCC"), October 15, 2016

**[Up one Level](Chess_Game "Chess Game")**

