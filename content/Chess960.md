---
title: Chess960
---
**[Home](Home "Home") * [Games](Games "Games") * Chess960**

**Chess960**, (or Fischer Random Chess)

a chess variant invented by former [World Chess Champion](https://en.wikipedia.org/wiki/World_Chess_Champion) [Bobby Fischer](https://en.wikipedia.org/wiki/Bobby_Fischer), introduced on June 19, 1996 in [Buenos Aires](https://en.wikipedia.org/wiki/Buenos_Aires), [Argentina](https://en.wikipedia.org/wiki/Argentina) <a id="cite-note-1" href="#cite-ref-1">[1]</a> . Randomizing the pieces on its back rank has been known as *Shuffle Chess*, but Chess960 introduces rules so that [castling](Castling "Castling") options are retained in all starting positions, one player's bishops must start on opposite-color squares, and the king must start on a square between the rooks, resulting in 960 unique positions, while the classical [initial position](Initial_Position "Initial Position") is one of them. Chess960 practically handicaps the application of [opening theory](http://en.wikibooks.org/wiki/Chess_Opening_Theory) in classical chess with the [memorization](Opening_Book "Opening Book") of opening moves, both for human as well for chess programs.

## Castling moves with chess GUIs

For chess, players make a castling move by moving their Kings to two cells, left or right. However, for Chess960 sometimes they can’t move their King to two cells since the target cell may be still occupied by a piece and/or the distance between the King and the target cell may vary from 1 to 6 (not only 2 cells). Many chess GUIs solved that difficulty/ambiguity by changing the way to make castling move: move the King to capture its own Rooks.

## Programming

Chess960 is almost identical to chess, except for initial positions and the castling rule. A chess software can easily support Chess960 with only a few changes.

## Initial positions

A typical chess engine can support any given position thus it can parse correctly any initial position. It needs to parse input, setup, and process correctly the castling statuses.

For other software such as chess GUIs which need to generate all initial positions, they can simply store all initial FENs or use some algorithms to generate them when needed.

## Notations

Chess960 can use all chess notations with some caring about ambiguities:

- Some chess GUIs send castling moves as O-O, O-O-O (e.g., [Arena](Arena "Arena")) when some other ones send as own-Rook captures (e.g., [Shredder GUI](Shredder#GUI "Shredder"), [WinBoard](WinBoard "WinBoard"), [Banksia GUI](Banksia_GUI "Banksia GUI")) such as d1e1.
- Variant name (in PGN file): some programs use the name “Fischerandom” but others may use “Chess960”
- UCI engines: some engines tell chess GUIs that they support Chess960 via the option UCI_variant, others via UCI_Chess960

## See also

- [Chess960 Engines](Category:Chess960 "Category:Chess960")
- [Chess960 Perft Results](Chess960_Perft_Results "Chess960 Perft Results")
- [Livingston Chess960 Computer World Championship](Livingston_Chess960_Computer_World_Championship "Livingston Chess960 Computer World Championship")
- [Shredder-FEN](Forsyth-Edwards_Notation#Shredder-FEN "Forsyth-Edwards Notation")
- [X-FEN](Forsyth-Edwards_Notation#X-FEN "Forsyth-Edwards Notation")

## Publications

- [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl") (**2004**). *[Fischer-Random-Schach: (FRC/Chess 960)](http://books.google.com/books/about/Fischer_Random_Schach.html?id=DEatvtAx9RQC&redir_esc=y)*. Books on Demand, ISBN: 3833413220, 9783833413223 (German)
- [Matthew Sadler](Matthew_Sadler "Matthew Sadler") (**2021**). *Chess960 Superhumans*! [ICGA Journal, Vol. 43, No. 1](ICGA_Journal#43_1 "ICGA Journal"), [online](https://matthewsadler.me.uk/engine-chess/chess960-superhumans/)

## Forum Posts

## 2005 ...

- [Why to use compatible X-FEN (in Chess960)](https://www.stmintz.com/ccc/index.php?id=437213) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), July 17, 2005
- [Chess960 Nullmove castling](https://www.stmintz.com/ccc/index.php?id=439445) by [Gian-Carlo Pascutto](Gian-Carlo_Pascutto "Gian-Carlo Pascutto"), [CCC](CCC "CCC"), August 01, 2005
- [Chess960: X-FEN rules international](https://www.stmintz.com/ccc/index.php?id=439792) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), August 03, 2005
- [contradicting FEN and SMK-FEN](https://www.stmintz.com/ccc/index.php?id=439995) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), August 04, 2005
- [Chess960: Arena castle vs X-FEN castle](https://www.stmintz.com/ccc/index.php?id=459898) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 05, 2005
- [Chess960 in Fritz9GUI and Winboard_frc](https://www.stmintz.com/ccc/index.php?id=464214) by [Matthias Gemuh](Matthias_Gemuh "Matthias Gemuh"), [CCC](CCC "CCC"), November 24, 2005
- [supporting FRC questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=5579) by [Uri Blass](Uri_Blass "Uri Blass"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), September 13, 2006
- [0x88 FRC castle questions](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=50635) by [Daniel Uranga](Daniel_Uranga "Daniel Uranga"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 12, 2009 » [0x88](0x88 "0x88")

## 2010 ...

- [FRC / Chess960 Engine with "Divided" Command](http://www.talkchess.com/forum/viewtopic.php?t=54528) by [Steve Maughan](Steve_Maughan "Steve Maughan"), [CCC](CCC "CCC"), December 02, 2014 » [Perft](Perft "Perft")

## 2015 ...

- [Some Chess960/FRC positions to be confirmed](http://www.talkchess.com/forum/viewtopic.php?t=55274) by [Reinhard Scharnagl](Reinhard_Scharnagl "Reinhard Scharnagl"), [CCC](CCC "CCC"), February 09, 2015 » [Perft Results](Perft_Results "Perft Results")
- [FRC / Chess960 -- Some Lessons I Learned](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=71070) by [Andrew Grant](Andrew_Grant "Andrew Grant"), [CCC](CCC "CCC"), June 22, 2019
- [Strictly for Chess960 Enthusiasts ...](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71091) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), June 25, 2019
- [Chess960 Generator and Lookup Tool](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71349) by [Michael B](Michael_Byrne "Michael Byrne"), [CCC](CCC "CCC"), July 25, 2019
- [Polyglot FRC/960 Opening Book](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=72432) by [Dennis Sceviour](Dennis_Sceviour "Dennis Sceviour"), [CCC](CCC "CCC"), November 27, 2019 » [Opening Book](Opening_Book "Opening Book"), [PolyGlot](PolyGlot "PolyGlot")

## 2020 ...

- [PST for FRC](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=73865) by [Vivien Clauzon](Vivien_Clauzon "Vivien Clauzon"), [CCC](CCC "CCC"), May 07, 2020 » [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [FRC in CECP](http://www.talkchess.com/forum3/viewtopic.php?f=7&t=76106) by lucasart, [CCC](CCC "CCC"), December 20, 2020 » [CECP](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol")
- [Implementing FRC?](https://www.talkchess.com/forum3/viewtopic.php?f=7&t=78276) by [Martin Bryant](Martin_Bryant "Martin Bryant"), [CCC](CCC "CCC"), September 28, 2021

## External Links

- [Chess960 from Wikipedia](https://en.wikipedia.org/wiki/Chess960)
- [Chess960 starting position from Wikipedia](https://en.wikipedia.org/wiki/Chess960_starting_position)
- [Chess960 numbering scheme from Wikipedia](https://en.wikipedia.org/wiki/Chess960_numbering_scheme)
- [GitHub - MichaelB7/Chess960-Lookup: Generate or lookup Chess960 positions sequentially or randomly](https://github.com/MichaelB7/Chess960-Lookup) by [Michael Byrne](Michael_Byrne "Michael Byrne")
- [Fischer Random Chess](http://www.chessvariants.org/diffsetup.dir/fischer.html)
- [The birth of Fischer Random Chess](http://www.chessvariants.org/diffsetup.dir/fischerh.html) by [Eric van Reem](Eric_van_Reem "Eric van Reem")
- [Fischer Random Chess (Chess960)](http://www.dwheeler.com/essays/Fischer_Random_Chess.html) by [David A. Wheeler](https://en.wikipedia.org/wiki/David_A._Wheeler)
- [CCRL 40/4 FRC - Index](http://www.computerchess.org.uk/ccrl/404FRC/) » [CCRL](CCRL "CCRL")

## References

1. <a id="cite-ref-1" href="#cite-note-1">↑</a> [The birth of Fischer Random Chess](http://www.chessvariants.org/diffsetup.dir/fischerh.html) by [Eric van Reem](Eric_van_Reem "Eric van Reem")

**[Up one Level](Games "Games")**

