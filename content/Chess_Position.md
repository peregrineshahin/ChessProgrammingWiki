---
title: Chess Position
---
**[Home](Home "Home") * [Chess](Chess "Chess") * Position**

[](http://www.slu.edu/sluma-home/past-exhibitions/2009/duchamp) [Marcel Duchamp](Category:Marcel_Duchamp "Category:Marcel Duchamp") <a id="cite-note-1" href="#cite-ref-1">[1]</a> <a id="cite-note-2" href="#cite-ref-2">[2]</a>
The **Chess Position** describes how [pieces](Pieces "Pieces") are placed on the [chessboard](Chessboard "Chessboard"), as printed as chess diagram, image or photograph from a [game of chess](Chess_Game "Chess Game"). In 1996 [Shirish Chinchalkar](Shirish_Chinchalkar "Shirish Chinchalkar") determined 1046 as upper bound for the number of reachable chess positions <a id="cite-note-3" href="#cite-ref-3">[3]</a>. The [maximum number of moves](Encoding_Moves#MoveIndex "Encoding Moves") per chess position seems 218 <a id="cite-note-4" href="#cite-ref-4">[4]</a>.

Of course, the information of any arbitrary chess position which occurs inside the game of chess, might be determined from a certain initial starting position and a [sequence of moves](Move_List "Move List") (half-moves), which leads to this position. Anyway, an efficient data structure for a chess position, which is [incrementally updated](Incremental_Updates "Incremental Updates") during game play and [search](Search "Search") is essential for a chess playing program.

## Specifying a Chess Position

Except the determination of three fold [repetitions](Repetitions "Repetitions"), which requires the whole move record, at least from the last [irreversible move](Irreversible_Moves "Irreversible Moves") (half-move) played, the chess position should keep track of various informations related to the position also for efficiency reasons. Another issue is to make chess positions persistent with a maximum of information required, but without the whole game history, as specified by the [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") or [Extended Position Description](Extended_Position_Description "Extended Position Description").

Beside piece placement, as considered by the [board representation](Board_Representation "Board Representation"), the [side to move](Side_to_move "Side to move") is essential, which might take only one [bit](Bit "Bit") inside an appropriate data structure for a chess position. Additionally, the [Castling](Castling "Castling") ability for both sides, as reflected by the [castling rights](Castling_Rights "Castling Rights") and a possible [en passant](En_passant "En passant") target square (or [file](Files "Files")) is needed to further completely specify the position, as well as the [halfmove clock](Halfmove_Clock "Halfmove Clock") to cover the [fifty-move rule](Fifty-move_Rule "Fifty-move Rule").

## Summary

A chess positions consists of

- [Piece](Pieces "Pieces") placement on the [Chessboard](Chessboard "Chessboard") as considered by the [Board Representation](Board_Representation "Board Representation")
- [Side to move](Side_to_move "Side to move")
- [Castling Rights](Castling_Rights "Castling Rights")
- [En passant](En_passant "En passant") target square
- [Halfmove Clock](Halfmove_Clock "Halfmove Clock")

## Positions inside the Search

In the context of Search, a position is the [node](Node "Node") inside a [search tree](Search_Tree "Search Tree"). To completely determine the position with respect to [repetitions](Repetitions "Repetitions"), one additionally needs a [move list](Move_List "Move List") or any other appropriate data structure, to keep up to 100 reversible half-moves, likely associated with [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") of the intermediate positions.

- [Incremental Updates](Incremental_Updates "Incremental Updates")
- [Copy-Make](Copy-Make "Copy-Make")

## Positions

- [Initial Position](Initial_Position "Initial Position")
- [Test-Positions](Test-Positions "Test-Positions")

## Notations

- [Extended Position Description](Extended_Position_Description "Extended Position Description") (EPD)
- [Forsyth-Edwards Notation](Forsyth-Edwards_Notation "Forsyth-Edwards Notation") (FEN)
- [Forsyth-Edwards Expanded Notation](index.php?title=Forsyth-Edwards_Expanded_Notation&action=edit&redlink=1 "Forsyth-Edwards Expanded Notation (page does not exist)") (FEEN)

## Flipping and Mirroring

- [Color Flipping](Color_Flipping "Color Flipping")
- [Diagonal Mirroring](Diagonal_Mirroring "Diagonal Mirroring")
- [Horizontal Mirroring](Horizontal_Mirroring "Horizontal Mirroring")
- [Vertical Flipping](Vertical_Flipping "Vertical Flipping")

## See Also

- [Board Representation](Board_Representation "Board Representation")
- [Chess Game](Chess_Game "Chess Game")
- [Chess Maxima](Chess#Maxima "Chess")
- [Chessboard](Chessboard "Chessboard")
- [Graphics Programming](Graphics_Programming "Graphics Programming")
- [Moves](Moves "Moves")
- [Node](Node "Node")
- [Pieces](Pieces "Pieces")

[Piece Recognition](Piece_Recognition "Piece Recognition")

- [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis")
- [Transposition](Transposition "Transposition")
- [User Interface](User_Interface "User Interface")

## Publications

- [Jürg Nievergelt](J%C3%BCrg_Nievergelt "Jürg Nievergelt") (**1977**). *Information content of chess positions.* ACM SIGART Newsletter 62, pp. 13-14. Reprinted as: *Information content of chess positions: Implications for game-specific knowledge of chess players*, pp. 283-289. [Machine Intelligence 12](http://www.doc.ic.ac.uk/~shm/MI/mi12.html) (eds. [Jean Hayes Michie](Jean_Hayes_Michie "Jean Hayes Michie"), [Donald Michie](Donald_Michie "Donald Michie"), [E. Tyugu](http://www.cs.ioc.ee/~tyugu/)). Clarendon Press, Oxford, 1991. ISBN 0-19-853823-5.
- [Bernhard Balkenhol](Bernhard_Balkenhol "Bernhard Balkenhol") (**1994**). *Data Compression in Encoding Chess Positions.* [ICCA Journal, Vol. 17, No. 3](ICGA_Journal#17_3 "ICGA Journal"), [zipped ps](http://www.balkenhol.net/papers/icca94.ps.gz)
- [Shirish Chinchalkar](Shirish_Chinchalkar "Shirish Chinchalkar") (**1996**). *An Upper Bound for the Number of Reachable Positions*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal")
- [Alex de Voogt](Alex_de_Voogt "Alex de Voogt") (**2002**). *[Reproducing board game positions: Western Chess and African Bao](http://psycnet.apa.org/index.cfm?fa=buy.optionToBuy&id=2003-03501-005)*. [Swiss Journal of Psychology](http://www.verlag-hanshuber.com/zeitschriften/journal.php?abbrev=sjp&show=editorial), Vol 61, No. 4
- [Manuel Cristóbal López-Michelone](Manuel_Crist%C3%B3bal_L%C3%B3pez-Michelone "Manuel Cristóbal López-Michelone"), [Jorge Luis Ortega-Arjona](Jorge_Luis_Ortega-Arjona "Jorge Luis Ortega-Arjona") (**2020**). *A description language for chess*. [ICGA Journal, Vol. 42, No. 1](ICGA_Journal#42_1 "ICGA Journal")

## Forum Posts

## 1980 ...

- [sri-unix.426: compact representation of a position](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.05_sri-unix.426_net.chess.txt) by [Bill Vaughan](index.php?title=Bill_Vaughan&action=edit&redlink=1 "Bill Vaughan (page does not exist)"), [net.chess](http://quux.org:70/Archives/usenet-a-news/NET.chess) January 5, 1982
- [Re: sri-unix.426: compact representation of a position](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.05_duke.1553_net.chess.txt) by [Tom Truscott](Tom_Truscott "Tom Truscott"), [net.chess](http://quux.org:70/Archives/usenet-a-news/NET.chess), January 5, 1982
- [Re: sri-unix.444: compact representation of chess positions](http://quux.org:70/Archives/usenet-a-news/NET.chess/82.01.07_duke.1593_net.chess.txt) by [Tom Truscott](Tom_Truscott "Tom Truscott"), [net.chess](http://quux.org:70/Archives/usenet-a-news/NET.chess), January 7, 1982 » [Zobrist Hashing](Zobrist_Hashing "Zobrist Hashing") <a id="cite-note-5" href="#cite-ref-5">[5]</a>

## 1990 ...

- [entropy of chess positions](https://groups.google.com/d/msg/rec.games.chess/pyM6LfZPbvY/DO2V0y4BezIJ) by [John Tromp](John_Tromp "John Tromp"), [rgc](Computer_Chess_Forums "Computer Chess Forums"), April 15, 1991
- [estimated number of chesspositions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/c15c92ded7ed6400/) by [Vincent Diepeveen](Vincent_Diepeveen "Vincent Diepeveen"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), October 27, 1995
- [number of moves in position](https://www.stmintz.com/ccc/index.php?id=69647) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 19, 1999

## [Re: number of moves in position](https://www.stmintz.com/ccc/index.php?id=69704) by [Leonid](Leonid_Liberman "Leonid Liberman"), [CCC](CCC "CCC"), September 21, 1999 2000 ...

- [Min # of bits needed to store a chess position](https://www.stmintz.com/ccc/index.php?id=106847) by [James Robertson](James_Robertson "James Robertson"), [CCC](CCC "CCC"), April 20, 2000
- [Minimum bits to encode a chess position](http://mathforum.org/kb/message.jspa?messageID=364071) by Ken Payson, [The Math Forum @ Drexel University](http://mathforum.org/), February 8, 2002
- [Making positions in eps](https://www.stmintz.com/ccc/index.php?id=323898) by [Renze Steenhuisen](Jan_Renze_Steenhuisen "Jan Renze Steenhuisen"), [CCC](CCC "CCC"), October 27, 2003 » [Fen2eps](Forsyth-Edwards_Notation#FEN2EPS "Forsyth-Edwards Notation")

## 2010 ...

- [allowing invalid positions](http://www.talkchess.com/forum/viewtopic.php?t=48952) by Eric Langedijk, [CCC](CCC "CCC"), August 13, 2013
- [Counting endgame positions](http://www.talkchess.com/forum/viewtopic.php?t=50832) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov"), [CCC](CCC "CCC"), January 08, 2014 <a id="cite-note-6" href="#cite-ref-6">[6]</a>
- [Total possible chess positions?](http://www.talkchess.com/forum/viewtopic.php?t=51744) by [Matthew R. Brades](Matthew_R._Brades "Matthew R. Brades"), [CCC](CCC "CCC"), March 26, 2014  » [Chess Maxima](Chess#Maxima "Chess")
- [Position validity](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=52214) by [Russell Reagan](Russell_Reagan "Russell Reagan"), [CCC](CCC "CCC"), May 04, 2014

## 2015 ...

- [Binary FEN](http://www.talkchess.com/forum/viewtopic.php?t=57065) by [J. Wesley Cleveland](index.php?title=J._Wesley_Cleveland&action=edit&redlink=1 "J. Wesley Cleveland (page does not exist)"), [CCC](CCC "CCC"), July 24, 2015
- [Max moves in a position](http://www.talkchess.com/forum/viewtopic.php?t=61792) by [Laurie Tunnicliffe](Laurie_Tunnicliffe "Laurie Tunnicliffe"), [CCC](CCC "CCC"), October 22, 2016 » [Chess Maxima](Chess#Maxima "Chess"), [Move List](Move_List "Move List")

## 2020 ...

- [Canonical Position Representation](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73614) by Dmitry Shechtman, [CCC](CCC "CCC"), April 10, 2020
- [On the number of chess positions](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685) by [John Tromp](John_Tromp "John Tromp"), [CCC](CCC "CCC"), July 09, 2021

## [Re: On the number of chess positions](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685&start=34) by [John Tromp](John_Tromp "John Tromp"), [CCC](CCC "CCC"), April 02, 2022 [Re: On the number of chess positions](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=77685&start=42) by [Peter Österlund](Peter_%C3%96sterlund "Peter Österlund"), [CCC](CCC "CCC"), April 03, 2022 » [Retrograde Analysis](Retrograde_Analysis "Retrograde Analysis") External Links

- [GitHub - tromp/ChessPositionRanking: Software suite for ranking chess positions and accurately estimating the number of legal chess positions](https://github.com/tromp/ChessPositionRanking)
- [Puzzle: Encoding a chess board state throughout a game](https://stackoverflow.com/questions/1831386/programmer-puzzle-encoding-a-chess-board-state-throughout-a-game) from [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow)
- [Chess Position Trainer](https://www.chesspositiontrainer.com/index.php/en/) by Stefan Renzewitz and Gregory Prentice
- [NULP in chess endgames](https://kirill-kryukov.com/chess/nulp/) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> Photo by [Arnold T. Rosenberg](https://en.wikipedia.org/wiki/Arnold_T._Rosenberg), [Marcel Duchamp](Category:Marcel_Duchamp "Category:Marcel Duchamp") playing chess on a sheet of Glass, 1958, see [Francis M. Naumann](https://en.wikipedia.org/wiki/Francis_Naumann), [Bradley Bailey](https://www.slu.edu/arts-and-sciences/fine-and-performing-arts/faculty/bailey-bradley.php) (**2009**). *[Marcel Duchamp: The Art of Chess](http://www.francisnaumann.com/Chess%20Book/)*
1. <a id="cite-ref-2" href="#cite-note-2">↑</a> [Marcel Duchamp: Chess Master](http://www.slu.edu/sluma-home/past-exhibitions/2009/duchamp) [Saint Louis University Museum of Art](https://www.slu.edu/sluma-home) [Saint Louis University : SLU](https://en.wikipedia.org/wiki/Saint_Louis_University)
1. <a id="cite-ref-3" href="#cite-note-3">↑</a> [Shirish Chinchalkar](Shirish_Chinchalkar "Shirish Chinchalkar") (**1996**). *An Upper Bound for the Number of Reachable Positions*. [ICCA Journal, Vol. 19, No. 3](ICGA_Journal#19_3 "ICGA Journal")
1. <a id="cite-ref-4" href="#cite-note-4">↑</a> [Subject: Maximum Number of Legal Moves](https://www.stmintz.com/ccc/index.php?id=424966) by [Andrew Shapira](Andrew_Shapira "Andrew Shapira"), [CCC](CCC "CCC"), May 08, 2005
1. <a id="cite-ref-5" href="#cite-note-5">↑</a> [Re: Hashing function for board positions](http://groups.google.com/group/rec.games.chess.computer/browse_frm/thread/a0a82ffbb59b7ced) post 4 by [Jim Gillogly](James_Gillogly "James Gillogly"), [rgcc](Computer_Chess_Forums "Computer Chess Forums"), May 12, 1997
1. <a id="cite-ref-6" href="#cite-note-6">↑</a> [NULP in chess endgames](http://kirill-kryukov.com/chess/nulp/) by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")

**[Up one Level](Chess "Chess")**

