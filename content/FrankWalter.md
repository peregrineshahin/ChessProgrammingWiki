---
title: FrankWalter
---
**[Home](Home "Home") * [Engines](Engines "Engines") * FrankWalter**

\[ Frank-Walter meets Condoleezza <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**FrankWalter**, (Frank Walter, Frank-Walter)

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), written in [Java](Java "Java"). The development started in 2009 with various trials to implement efficient [bitboard](Bitboards "Bitboards") techniques in Java <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
After continuing the development on his old engine <a id="cite-note-3" href="#cite-ref-3">[3]</a>, Laurens Winkelhagen re-published FrankWalter **2.2.0** in November 2018 <a id="cite-note-4" href="#cite-ref-4">[4]</a>,
short before it had its over the board debut at the [PT 54](PT_54 "PT 54") in [Leiden](https://en.wikipedia.org/wiki/Leiden).
Since **2.3.2** in February 2019, FrankWalter has become [open source](Category:Open_Source "Category:Open Source"), hosted on [GitHub](https://en.wikipedia.org/wiki/GitHub) and licensed under the [GPL v3.0](Free_Software_Foundation#GPL "Free Software Foundation") <a id="cite-note-5" href="#cite-ref-5">[5]</a>.

## Contents

- [1 Etymology](#etymology)
- [2 Features](#features)
  - [2.1 Board Representation](#board-representation)
  - [2.2 Search](#search)
  - [2.3 Evaluation](#evaluation)
  - [2.4 Misc](#misc)
- [3 Photos & Games](#photos-.26-games)
- [4 See also](#see-also)
- [5 Forum Posts](#forum-posts)
  - [5.1 2009](#2009)
  - [5.2 2018 ...](#2018-...)
- [6 External Links](#external-links)
  - [6.1 Chess Engine](#chess-engine)
  - [6.2 Misc](#misc-2)
- [7 References](#references)

## Etymology

[Frank-Walter Steinmeier](https://en.wikipedia.org/wiki/Frank-Walter_Steinmeier), in 2009 German [Minister for Foreign Affairs](<https://en.wikipedia.org/wiki/Minister_for_Foreign_Affairs_(Germany)>), since March 2017 [President of Germany](https://en.wikipedia.org/wiki/President_of_Germany),
and his apparently desired name change <a id="cite-note-6" href="#cite-ref-6">[6]</a> to Frank was the inspiration for the name of the chess engine <a id="cite-note-7" href="#cite-ref-7">[7]</a>. Frank-Walter Steinmeier in an 2011 interview <a id="cite-note-8" href="#cite-ref-8">[8]</a>

```
Mr. Steinmeier, can you actually play chess, like [Peer Steinbrück](https://en.wikipedia.org/wiki/Peer_Steinbr%C3%BCck) and [Helmut Schmidt](https://en.wikipedia.org/wiki/Helmut_Schmidt)?

```

```
Frank-Walter Steinmeier: Neither am I a good chess player nor am I currently writing a book.

```

## Features

## [Board Representation](Board_Representation "Board Representation")

FrankWalter [represents the board](Board_Representation "Board Representation") using a two-dimensional [array](Array "Array") of [piece bitboards](Bitboard_Board-Definition#CBoardDef "Bitboard Board-Definition"), indexed by [color](Color "Color") and [type](Pieces#PieceTypeCoding "Pieces"), and further has an [8x8 board](8x8_Board "8x8 Board") for a square-centric view.
These are all members of a board class along with the usual stuff specifying a [chess position](Chess_Position "Chess Position"), such as [side to move](Side_to_move "Side to move"), [castling rights](Castling_Rights "Castling Rights"), [en passant](En_passant "En passant") target, [halfmove clock](Halfmove_Clock "Halfmove Clock"), and an array of [Zobrist keys](Zobrist_Hashing "Zobrist Hashing") to detect [repetitions](Repetitions "Repetitions") along the actual game record and variation.
Despite [sliding piece attacks](Sliding_Piece_Attacks "Sliding Piece Attacks") are determined by a memory friendly approach of [Kindergarten bitboards](Kindergarten_Bitboards "Kindergarten Bitboards") for [files](Files "Files") and [Magic bitboards](Magic_Bitboards "Magic Bitboards") for [ranks](Ranks "Ranks") and [bishops](Bishop "Bishop"),
FrankWalter keeps [attack tables](Attack_and_Defend_Maps "Attack and Defend Maps") in [classical](Attack_and_Defend_Maps#Classical_Approach "Attack and Defend Maps") [Chess 4.5](</Chess_(Program)> "Chess (Program)") style <a id="cite-note-9" href="#cite-ref-9">[9]</a>, two bitboard arrays (ATKFR and ATKTO) indexed by square,
While along with keeping bitboards for [pinned pieces](Pin "Pin"), this seems an reasonable approach to implement [legal move generation](Move_Generation#Legal "Move Generation"), the culprit is the [incremental update](Incremental_Updates "Incremental Updates"),
in particular using a [copy-make stack](Copy-Make#Stack "Copy-Make") to copy the 1K attack table not only during [make](Make_Move "Make Move") but also back during [unmake](Unmake_Move "Unmake Move") <a id="cite-note-10" href="#cite-ref-10">[10]</a>.

## [Search](Search "Search")

- [Lazy SMP](Lazy_SMP "Lazy SMP")
- [Fractional Ply](Depth#FractionalPlies "Depth") [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
- [Principal Variation Search](Principal_Variation_Search "Principal Variation Search")
- [Aspiration Windows](Aspiration_Windows "Aspiration Windows")
- [Transposition Table](Transposition_Table "Transposition Table")
- [Selectivity](Selectivity "Selectivity")
  - [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Late Move Reductions](Late_Move_Reductions "Late Move Reductions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Move Ordering](Move_Ordering "Move Ordering")
  - [PV-Move](PV-Move "PV-Move")
  - [Killer Heuristic](Killer_Heuristic "Killer Heuristic")
  - [History Heuristic](History_Heuristic "History Heuristic")
  - [Static Exchange Evaluation](Static_Exchange_Evaluation "Static Exchange Evaluation")

## [Evaluation](Evaluation "Evaluation")

- [Material](Material "Material")
- [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
- [Mobility](Mobility "Mobility")
- [Pawn Structure](Pawn_Structure "Pawn Structure")
- [King Safety](King_Safety "King Safety")
- [Tapered Eval](Tapered_Eval "Tapered Eval")
- [Texel's Tuning Method](Texel%27s_Tuning_Method "Texel's Tuning Method")

## Misc

- [Syzygy Bases](Syzygy_Bases "Syzygy Bases") via [JNI](https://en.wikipedia.org/wiki/Java_Native_Interface) [Fathom](Syzygy_Bases#Fathom "Syzygy Bases") Bridge (JSyzygy) <a id="cite-note-11" href="#cite-ref-11">[11]</a>
- [Beowulf](Beowulf "Beowulf") [Opening Book](Opening_Book "Opening Book") Format

## Photos & Games

[](https://csvn.nl/index.php/nieuws/51-toernooien/830-55th-programmer-tournament-ranking)
[PT 55](PT_55 "PT 55"), Round 4, FrankWalter - [The King](The_King "The King"), [Johan de Koning](Johan_de_Koning "Johan de Koning") and [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen") <a id="cite-note-12" href="#cite-ref-12">[12]</a> <a id="cite-note-13" href="#cite-ref-13">[13]</a>

```

[Event "PT55"]
[Site "Amersfoort"]
[Date "2019.05.19"]
[Round "4"]
[White "FrankWalter"]
[Black "The King"]
[Result "1-0"]

1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3 c5 5.g3 Nc6 6.dxc5 Bxc5 7.Bg2 d5 8.cxd5 exd5 9.Bg5 O-O 10.Bxf6 Qxf6 
11.Qxd5 Bb4 12.O-O Be6 13.Qb5 Rab8 14.Rfc1 a6 15.Qg5 Be7 16.Qxf6 Bxf6 17.Ne1 Nb4 18.a3 Nc6 19.Rab1 Rfd8 
20.Rd1 a5 21.Rxd8+ Rxd8 22.Nd3 Bd4 23.Rd1 Bb3 24.Rc1 Bc4 25.Bxc6 bxc6 26.Na4 Bb5 27.Nac5 a4 28.Kg2 g5
29.Rc2 Bg7 30.Nb4 h6 31.Kf3 Rd4 32.h3 Kf8 33.b3 axb3 34.Nxb3 Rc4 35.Rxc4 Bxc4 36.Na5 Bb5 37.Nd3 Bd4 
38.Nb3 Bb6 39.Nbc5 Ke7 40.a4 Bc4 41.Nb7 f5 42.Ndc5 Ba7 43.a5 Bd5+ 44.Ke3 Bc4 45.Kd2 h5 46.h4 g4 47.e3 
Bd5 48.Kc3 Bg8 49.a6 Bd5 50.Kb4 Bf3 51.Na5 Bd5 52.Nc4 Be6 53.Nxe6 Kxe6 54.Nb2 Kd5 55.Nd3 Ke4 56.Nf4
Kf3 57.Nxh5 Kxf2 58.Ng7 f4 59.exf4 Kxg3 60.h5 Kxf4 61.h6 g3 62.Nh5+ Kg5 63.Nxg3 Kxh6 64.Nf5+ Kg5 65.Ne7 
Be3 66.Nxc6 Kf6 67.Kc4 Bb6 68.Kb5 Bf2 69.Nb4 Ke6 70.Kc6 Ba7 71.Nd5 Kf5 72.Kb7 Bd4 73.Nb6 1-0

```

## See also

- [JanWillem](JanWillem "JanWillem")

## Forum Posts

## 2009

- [Java & Magic Bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49948) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2009
- [Frank-Walter 1.0.5](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50010) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2009
- [New Frank-Walter version (1.0.8)](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50051) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 24, 2009

## 2018 ...

- [Revived Engine - Frank Walter 2.2.0 (Java - WB)](http://talkchess.com/forum3/viewtopic.php?t=68989) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), November 20, 2018
- [Frank Walter](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=69057) by [Gabor Szots](Gabor_Szots "Gabor Szots"), [CCC](CCC "CCC"), November 26, 2018
- [Re: New engine releases 2019](http://talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=9) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), February 12, 2019
- [Re: New engine releases 2019](http://talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=34) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), March 10, 2019
- [Re: New engine releases 2019](http://talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=96) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), April 09, 2019
- [Frank-Walter & Tablebases](http://www.talkchess.com/forum3/viewtopic.php?f=2&t=71937) by [Ted Summers](Ted_Summers "Ted Summers"), [CCC](CCC "CCC"), September 27, 2019

## External Links

## Chess Engine

- [GitHub - ljgw/frankwalter: a WB2 java chess engine](https://github.com/ljgw/frankwalter)
- [frank-walter](http://www.computer-chess.org/doku.php?id=computer_chess:engines:frank-walter:index) from [Ron Murawski's](Ron_Murawski "Ron Murawski") [Computer-Chess Wiki](http://computer-chess.org/doku.php?id=home)
- [Index of /chess/engines/Jim Ablett/FRANK-WALTER](http://kirr.homeunix.org/chess/engines/Jim%20Ablett/FRANK-WALTER/) by [Jim Ablett](Jim_Ablett "Jim Ablett"), hosted by [Kirill Kryukov](Kirill_Kryukov "Kirill Kryukov")
- [FrankWalter](https://ccrl.chessdom.com/ccrl/4040/cgi/compare_engines.cgi?family=FrankWalter&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents)  in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Frank (given name) from Wikipedia](<https://en.wikipedia.org/wiki/Frank_(given_name)>)
- [Walter (name) from Wikipedia](<https://en.wikipedia.org/wiki/Walter_(name)>)
- [Frank Walter from Wikipedia](https://en.wikipedia.org/wiki/Frank_Walter)
- [Frank Walter](http://www.frankwalter.org/) ([Antiguan](https://en.wikipedia.org/wiki/Antigua) Artist)
- [Frank-Walter Steinmeier from Wikipedia](https://en.wikipedia.org/wiki/Frank-Walter_Steinmeier)
- [Jazzfest Bonn](https://www.jazzfest-bonn.de/en/2019-2/videos-jazzfest-bonn-2019/): Frank-Walter Steinmeier ist größter Jazz-Fan, May 16, 2019, and [Mezzoforte](Category:Mezzoforte "Category:Mezzoforte") - Medley: A Blast From The Past, [YouTube](https://en.wikipedia.org/wiki/YouTube) Videos

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> [Secretary Rice](https://en.wikipedia.org/wiki/Condoleezza_Rice) greets Foreign Minister [Steinmeier](https://en.wikipedia.org/wiki/Frank-Walter_Steinmeier), [Washington DC](https://en.wikipedia.org/wiki/Washington,_D.C.), April 4, 2006, [Photo: Secretary Rice Greets Foreign Minister Steinmeier of Germany](https://2001-2009.state.gov/r/pa/ei/pix/2006/64144.htm), [United States Department of State](https://en.wikipedia.org/wiki/United_States_Department_of_State), [Frank-Walter Steinmeier – Wikipedia.de](https://de.wikipedia.org/wiki/Frank-Walter_Steinmeier) (German), [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Java & Magic Bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49948) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 03, 2009
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Frank-Walter 1.0.5](http://www.open-aurec.com/wbforum/viewtopic.php?f=2&t=50010) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), March 03, 2009
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [Revived Engine - Frank Walter 2.2.0 (Java - WB)](http://talkchess.com/forum3/viewtopic.php?t=68989) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), November 20, 2018
1. <a id="cite-ref-5" href="#cite-note-5">[5]</a> [Re: New engine releases 2019](http://talkchess.com/forum3/viewtopic.php?f=2&t=69754&start=9) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [CCC](CCC "CCC"), February 12, 2019
1. <a id="cite-ref-6" href="#cite-note-6">[6]</a> [To be perfectly Frank... minister shortens name](https://uk.reuters.com/article/oukoe-uk-germany-spd-steinmeier/to-be-perfectly-frank-minister-shortens-name-idUKTRE51E19520090217) by [Erik Kirschbaum](https://www1.wdr.de/daserste/presseclub/gaeste/gast-erik-kirschbaum-latimes-100.html), [Reuters](https://en.wikipedia.org/wiki/Reuters), February 17, 2009
1. <a id="cite-ref-7" href="#cite-note-7">[7]</a> [Re: Java & Magic Bitboards](http://www.open-aurec.com/wbforum/viewtopic.php?f=4&t=49948&p=189209#p189206) by [Laurens Winkelhagen](Laurens_Winkelhagen "Laurens Winkelhagen"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 17, 2009
1. <a id="cite-ref-8" href="#cite-note-8">[8]</a> [Spielen Sie eigentlich Schach, Herr Steinmeier?](https://www.welt.de/print/wams/politik/article13700701/Spielen-Sie-eigentlich-Schach-Herr-Steinmeier.html) by [Claus Christian Malzahn](https://de.wikipedia.org/wiki/Claus_Christian_Malzahn) and [Daniel Friedrich Sturm](https://de.wikipedia.org/wiki/Daniel_Friedrich_Sturm), [Welt am Sonntag](https://en.wikipedia.org/wiki/Welt_am_Sonntag) November 6, 2011
1. <a id="cite-ref-9" href="#cite-note-9">[9]</a> [David Slate](David_Slate "David Slate"), [Larry Atkin](Larry_Atkin "Larry Atkin") (**1977**). *CHESS 4.5 - The Northwestern University Chess Program.* [Chess Skill in Man and Machine](Chess_Skill_in_Man_and_Machine "Chess Skill in Man and Machine"), reprinted (**1988**) in [Computer Chess Compendium](Computer_Chess_Compendium "Computer Chess Compendium")
1. <a id="cite-ref-10" href="#cite-note-10">[10]</a> [frankwalter/Board.java at master · ljgw/frankwalter · GitHub](https://github.com/ljgw/frankwalter/blob/master/src/main/java/com/winkelhagen/chess/frankwalter/board/Board.java)
1. <a id="cite-ref-11" href="#cite-note-11">[11]</a> [GitHub - ljgw/syzygy-bridge: Java bridge to use the Syzygy Tablebases via JNI](https://github.com/ljgw/syzygy-bridge)
1. <a id="cite-ref-12" href="#cite-note-12">[12]</a> [55th Programmer Tournament Photos day 2](https://csvn.nl/index.php/nieuws/51-toernooien/830-55th-programmer-tournament-ranking) by [Jan Krabbenbos](Jan_Krabbenbos "Jan Krabbenbos")
1. <a id="cite-ref-13" href="#cite-note-13">[13]</a> [CSVN Programmer Tournament 55 pgn download](https://csvn.nl/index.php/download/partijen/csvn-programmer-tournaments/262-csvn-programmer-tournament-55)

**[Up one level](Engines "Engines")**

