---
title: Conqueror
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Conqueror**

\[\_film_poster.jpg) [The Conqueror](<https://en.wikipedia.org/wiki/The_Conqueror_(1956_film)>) <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Conqueror,**

an [UCI](UCI "UCI") compatible chess program by [Aditya Pande](Aditya_Pande "Aditya Pande"). It is written in [C++](Cpp "Cpp"), released as [open source software](Category:Open_Source "Category:Open Source") under [GPLv3 license](Free_Software_Foundation#GPL "Free Software Foundation").
It's development started in June 2014 and is being improved for better performance and a more intricate evaluation scheme.
The engine supports UCI GUIs like [Arena](Arena "Arena"), [ChessGUI](ChessGUI "ChessGUI"), etc. and the support has been extended to latest [WinBoard GUI](WinBoard "WinBoard") but requires some configuration.

## Features

<a id="cite-note-2" href="#cite-ref-2">[2]</a>

- [Hybrid Board Representation](Board_Representation "Board Representation")
  - [Bitboard Board-Definition](Bitboard_Board-Definition "Bitboard Board-Definition")
  - [Piece-Lists](Piece-Lists "Piece-Lists")
- [Legal Move Generation](Move_Generation#Legal "Move Generation")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Alpha-Beta](Alpha-Beta "Alpha-Beta")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
- [MVV/LVA](MVV-LVA "MVV-LVA")
- [Tapered Evaluation](Tapered_Eval "Tapered Eval")

## Selected Games

The following game versus [Pulsar](Pulsar "Pulsar") represents the current strength of the engine (about 2100):

```

[Event "Test Game"]
[Site "INTEL-CORE-DUO-"]
[Date "2014.07.08"]
[Round "2"]
[White "Conqueror"]
[Black "pulsar2009-9b"]
[Result "1/2-1/2"]

1.Nc3 Nf6 2.e4 d6 3.d4 g6 4.Nf3 Bg7 5.Bc4 O-O 6.O-O Nxe4 7.Nxe4 d5 8.Qe2 dxe4 9.Qxe4 Nc6 10.c3 Na5 
11.Bb5 Bf5 12.Qe2 a6 13.Bd3 Bxd3 14.Qxd3 e5 15.Re1 Re8 16.Bg5 Qd5 17.Qe4 Qxe4 18.Rxe4 h6 19.Bd2 exd4 
20.Rxe8+ Rxe8 21.cxd4 Nc6 22.Be3 Nb4 23.a3 Nd5 24.Rc1 h5 25.Bd2 Re4 26.Rc5 c6 27.Rc4 Ne7 28.Bc3 Nf5 
29.h3 Nd6 30.Rb4 Bf6 31.Rb3 Re2 32.a4 h4 33.Ne5 Bg5 34.Rb6 Rc2 35.Nd3 Re2 36.Rb3 Bf6 37.d5 Bxc3 
38.dxc6 Bxb2 39.cxb7 Nxb7 40.Rxb7 Bd4 41.Rb4 Ba7 42.Rb7 Bd4 43.Rb4 Ba7 44.Rb7 Bd4
1/2-1/2

```

## See also

- [Chessmaster 11 Conqueror](Chessmaster#CM11Settings "Chessmaster") <a id="cite-note-3" href="#cite-ref-3">[3]</a>
- [Ivan II The Conqueror](Ivan_II_The_Conqueror "Ivan II The Conqueror")

## Forum Posts

- [Conqueror CE (UCI) by Aditya Pande](http://www.talkchess.com/forum/viewtopic.php?t=52773) by [Norbert Raimund Leisner](Norbert_Raimund_Leisner "Norbert Raimund Leisner"), [CCC](CCC "CCC"), June 27, 2014
- [Improve my chess engine (mainly nps and branching factor)](http://www.talkchess.com/forum/viewtopic.php?t=52847) by [Aditya Pande](Aditya_Pande "Aditya Pande"), [CCC](CCC "CCC"), July 03, 2014

## External Links

## Chess Engine

- [GitHub - pandeaditya/Conqueror](https://github.com/pandeaditya/Conqueror)
- [Conqueror Chess Engine download | SourceForge.net](https://sourceforge.net/projects/conqueror-chess-engine/)

## Misc

- [conqueror - Wiktionary](http://en.wiktionary.org/wiki/conqueror)
- [Conqueror (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Conqueror)
- [List of people known as the Conqueror from Wikipedia](https://en.wikipedia.org/wiki/List_of_people_known_as_the_Conqueror)
- [John Lumpkin](https://remo.com/team/member/john-lumpkin/bio/) - The Conqueror, album [The Devotion](https://www.johnlumpkinmusic.com/) (2015), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [The Conqueror](<https://en.wikipedia.org/wiki/The_Conqueror_(1956_film)>) theatrical release poster, [John Wayne](https://en.wikipedia.org/wiki/John_Wayne) was posthumously named a "winner" of a [Golden Turkey Award](https://en.wikipedia.org/wiki/The_Golden_Turkey_Awards) for his performance in the film, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Conqueror/README.md at master · pandeaditya/Conqueror · GitHub](https://github.com/pandeaditya/Conqueror/blob/master/README.md)
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Chessmaster 11 Settings](Chessmaster#CM11Settings "Chessmaster") by [Graham Banks](Graham_Banks "Graham Banks")

**[Up one level](Engines "Engines")**

