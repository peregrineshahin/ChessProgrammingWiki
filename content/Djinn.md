---
title: Djinn
---
**[Home](Home "Home") * [Engines](Engines "Engines") * Djinn**

\[ King of the djinns, Al-Malik al-Aswad <a id="cite-note-1" href="#cite-ref-1">[1]</a>
**Djinn**,

a [Chess Engine Communication Protocol](Chess_Engine_Communication_Protocol "Chess Engine Communication Protocol") compliant chess engine by [Tom Likens](Tom_Likens "Tom Likens"), written in [C++](Cpp "Cpp") with some [inline assembly](Assembly#InlineAssembly "Assembly"), first released in December 2003 <a id="cite-note-2" href="#cite-ref-2">[2]</a>.
Djinn utilizes [bitboards](Bitboards "Bitboards") to represent its [chess board](Chessboard "Chessboard") and [pieces](Pieces "Pieces").
As relatively slow searcher, Djinn spends most of its time in the [evaluation](Evaluation "Evaluation"). Executables are available to run under [Windows](Windows "Windows") and [Linux](Linux "Linux"), [Đorđe Vidanović](%C4%90or%C4%91e_Vidanovi%C4%87 "Đorđe Vidanović") has provided Djinn's [Opening Book](Opening_Book "Opening Book").
Over the years Djinn played four [CCT Tournaments](CCT_Tournaments "CCT Tournaments"), [CCT6](CCT6 "CCT6"), [CCT8](CCT8 "CCT8"), [CCT15](CCT15 "CCT15") and [CCT16](CCT16 "CCT16").

## Techniques and Algorithms

Djinn uses most of the following techniques and [algorithms](Algorithms "Algorithms") in one form or another <a id="cite-note-3" href="#cite-ref-3">[3]</a>:

- [Time Management](Time_Management "Time Management")
- [Minimax](Minimax "Minimax") [Search](Search "Search")
  - [Negamax](Negamax "Negamax") Searching
- [Alpha-beta](Alpha-Beta "Alpha-Beta")
  - [Negascout](NegaScout "NegaScout")
  - [PVS](Principal_Variation_Search "Principal Variation Search")
- [Iterative Deepening](Iterative_Deepening "Iterative Deepening")
  - [Aspiration Search](Aspiration_Windows "Aspiration Windows")
- [Null Move Pruning](Null_Move_Pruning "Null Move Pruning")
  - [Zugzwang](Zugzwang "Zugzwang")
  - [Verified Null-move Search](Null_Move_Pruning#ZugzwangVerification "Null Move Pruning")
  - [Adaptive Null-move Search](Null_Move_Pruning#AdaptiveNullMovePruning "Null Move Pruning")
- [Quiescence Search](Quiescence_Search "Quiescence Search")
  - [Checks](Quiescence_Search#Checks "Quiescence Search") in [Quiescence Search](Quiescence_Search "Quiescence Search")
- [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Collecting](Principal_Variation#CollectionDuringSearch "Principal Variation") the [Principal Variation](Principal_Variation "Principal Variation")
- [Extensions](Extensions "Extensions")
  - [Check Extensions](Check_Extensions "Check Extensions")
  - [Mate Threat Extensions](Mate_Threat_Extensions "Mate Threat Extensions")
  - [Passed Pawn Extensions](Passed_Pawn_Extensions "Passed Pawn Extensions")
  - [Recapture Extensions](Recapture_Extensions "Recapture Extensions")
  - [Singular Extensions](Singular_Extensions "Singular Extensions")
- [Reductions](Reductions "Reductions")/[Pruning](Pruning "Pruning")
- [Repetition Check](Repetitions "Repetitions")
- [Bitboards](Bitboards "Bitboards")
  - [FirstOne](BitScan "BitScan")
  - [Population (or Bit) Counting](Population_Count "Population Count")
  - [Inline Assembly](Assembly#InlineAssembly "Assembly")
- [Rotated Bitboards](Rotated_Bitboards "Rotated Bitboards")
- [Magic Bitboards](Magic_Bitboards "Magic Bitboards")
- [Move Generation](Move_Generation "Move Generation")
  - [MVV/LVA](MVV-LVA "MVV-LVA")
  - [Static-Exchange Evaluation (SEE)](Static_Exchange_Evaluation "Static Exchange Evaluation")
  - [Perft](Perft "Perft")
  - [In-Check Evasion](Check "Check")
- [Move ordering](Move_Ordering "Move Ordering")
  - [Ordering moves at the root](Move_Ordering#Root "Move Ordering")
  - [Hash move](Hash_Move "Hash Move")
  - [Killer moves](Killer_Move "Killer Move")
  - [Killer mate moves](Mate_Killers "Mate Killers")
  - [History Heuristic](History_Heuristic "History Heuristic")
- [Evaluation](Evaluation "Evaluation")
  - [Piece-Square Tables](Piece-Square_Tables "Piece-Square Tables")
  - [Opening](Opening "Opening")
    - [Development](Development "Development")
    - [Castling](Castling "Castling")
    - [Control of the Center](Center_Control "Center Control")
  - [Middlegame](Middlegame "Middlegame")
    - [Two-Bishops Bonus](Bishop_Pair "Bishop Pair")
    - [Rooks on the 7th Rank](Rook_on_Seventh "Rook on Seventh")
  - [Endgame](Endgame "Endgame")
    - [Opposite-colored bishops](Bishops_of_Opposite_Colors "Bishops of Opposite Colors")
    - [Passed Pawn](Passed_Pawn "Passed Pawn")
    - [Rule-of-the-Square](Rule_of_the_Square "Rule of the Square")
    - [Bahr's Rule](index.php?title=Bahr%27s_Rule&action=edit&redlink=1 "Bahr's Rule (page does not exist)")
  - [King Safety](King_Safety "King Safety")
    - [Defects](King_Safety#PawnShield "King Safety")
    - [Enemy Piece Tropism](King_Safety#KingTropism "King Safety")
    - [Delayed Castling](Castling "Castling")
    - [Control of the Squares Around the King](King_Safety#SquareControl "King Safety")
  - [Interior-Node Recognizers](Interior_Node_Recognizer "Interior Node Recognizer")
  - [Bitbases](Endgame_Bitbases "Endgame Bitbases")
- [Hash Tables](Transposition_Table "Transposition Table")
  - [Zobrist Keys](Zobrist_Hashing "Zobrist Hashing")
  - Adjusting [Mate Scores](Score#MateScores "Score") and [Bounds](Bound "Bound")
  - [Pawn Hash Tables](Pawn_Hash_Table "Pawn Hash Table")
  - [Evaluation Hash Table](Evaluation_Hash_Table "Evaluation Hash Table")
- [Internal Iterative Deepening](Internal_Iterative_Deepening "Internal Iterative Deepening")
- [Opening Book](Opening_Book "Opening Book")
- [Learning](Learning "Learning")
  - [Opening Book Modification](Book_Learning "Book Learning")
  - [Position Learning](Persistent_Hash_Table "Persistent Hash Table")
- [Endgame Tablebases](Endgame_Tablebases "Endgame Tablebases")
  - [Nalimov format](Nalimov_Tablebases "Nalimov Tablebases")
- [XBoard](XBoard "XBoard")/[WinBoard](WinBoard "WinBoard")

## Selected Games

[CCT6](CCT6 "CCT6"), round 7, [Hossa](Hossa "Hossa") - Djinn <a id="cite-note-4" href="#cite-ref-4">[4]</a>

```

[Event "CCT6"]
[Site "Internet Chess Club"]
[Date "2004.02.01"]
[Round "7"]
[White "Hossa"]
[Black "Djinn"]
[Result "0-1"]

1.e3 e5 2.d4 exd4 3.exd4 d5 4.Nf3 c6 5.Bd3 Qe7+ 6.Be3 Qb4+ 7.Nfd2 Nf6 8.O-O Be7 
9.c3 Qd6 10.Re1 Ng4 11.Nf3 Nxe3 12.Rxe3 O-O 13.Nbd2 g6 14.c4 Be6 15.c5 Qc7 16.Ne5 
Nd7 17.Nxd7 Qxd7 18.Qc2 b6 19.b4 bxc5 20.bxc5 Bg5 21.Ree1 Bf4 22.Rab1 Rfe8 23.Nf3 
Bg4 24.Ne5 Bxe5 25.dxe5 Rab8 26.Rxb8 Rxb8 27.a3 Bf5 28.f4 Rb5 29.Rc1 Bxd3 30.Qxd3 
h5 31.Qd2 Qf5 32.a4 Rb1 33.a5 Rxc1+ 34.Qxc1 Qe4 35.g3 Qb4 36.a6 Kf8 37.Kf2 Qd4+ 
38.Kg2 Qe4+ 39.Kf2 Qd3 40.e6 Qd4+ 41.Kg2 Qb4 42.exf7 Kxf7 43.Kf2 Qa5 44.Qc2 Qxa6 
45.f5 Qa1 46.fxg6+ Kg7 47.Qe2 Qd4+ 48.Kf1 Qc4 49.Qxc4 dxc4 50.Ke2 Kxg6 51.h3 Kf5 
52.Ke3 Ke5 53.Kd2 Kd4 54.Kc1 c3 55.Kc2 Kc4 56.Kd1 Kd3 57.Ke1 c2 58.Kf2 c1=Q 59.g4
Qf4+ 60.Kg2 Ke3 61.g5 Qxg5+ 62.Kf1 Qg3 63.h4 Qf2# 0-1

```

## See also

- [Genie](Genie "Genie")
- [Ifrit](Ifrit "Ifrit")

## Forum Posts

## 2003 ...

- [Djinn 0.815 Available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45757) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2003
- [Question for Tom Likens](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=46383) by [Matt McKnight](Matt_McKnight "Matt McKnight"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), February 07, 2004 » [Extended Futility Pruning](Futility_Pruning#Extendedfutilitypruning "Futility Pruning")
- [Re: Can any program find this thematic move? (Djinn 0.781)](https://www.stmintz.com/ccc/index.php?id=364245) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), May 08, 2004

## 2010 ...

- [Djinn 0.967 is now available for download](http://www.talkchess.com/forum/viewtopic.php?t=45572) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), October 15, 2012
- [Djinn 0.969 Released (64-bit + 32-bit)](http://www.talkchess.com/forum/viewtopic.php?t=45662) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), October 20, 2012
- [New Djinn 0.971 (time management fix)](http://www.talkchess.com/forum/viewtopic.php?t=45928) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), November 10, 2012
- [Djinn 0.979 Available (Win x64, 32 and Linux x64)](http://www.talkchess.com/forum/viewtopic.php?t=47046) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), January 30, 2013
- [Djinn 1.006](http://www.talkchess.com/forum/viewtopic.php?t=50618) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), December 24, 2013
- [Djinn 1.021](http://www.talkchess.com/forum/viewtopic.php?t=51972) by [Tom Likens](Tom_Likens "Tom Likens"), [CCC](CCC "CCC"), April 12, 2014

## External Links

## Chess Engine

- [Djinn](https://web.archive.org/web/20180112023028/http://webpages.charter.net/tlikens/index.html) by [Tom Likens](Tom_Likens "Tom Likens") ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))

[Djinn User Guide](https://web.archive.org/web/20161231040908/http://webpages.charter.net/tlikens/docs/Users_guide.html)

- [Djinn 0.925x](http://kirill-kryukov.com/chess/kcec/cgi/engine_details.cgi?print=Details&each_game=1&eng=Djinn%200.925x) in [KCEC](KCEC "KCEC")
- [Djinn](http://www.computerchess.org.uk/ccrl/404/cgi/compare_engines.cgi?family=Djinn&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/4](CCRL "CCRL")
- [Djinn](http://www.computerchess.org.uk/ccrl/4040/cgi/compare_engines.cgi?family=Djinn&print=Rating+list&print=Results+table&print=LOS+table&print=Ponder+hit+table&print=Eval+difference+table&print=Comopp+gamenum+table&print=Overlap+table&print=Score+with+common+opponents) in [CCRL 40/40](CCRL "CCRL")

## Misc

- [Djinn from Wikipedia](https://en.wikipedia.org/wiki/Jinn)
- [Djinn (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Djinn_%28disambiguation%29)
- [Jinn (disambiguation) from Wikipedia](https://en.wikipedia.org/wiki/Jinn_%28disambiguation%29)
- [Queenadreena](Category:Queenadreena "Category:Queenadreena") - Life (Support), [Djin](<https://en.wikipedia.org/wiki/Djin_(album)>) (2008), [YouTube](https://en.wikipedia.org/wiki/YouTube) Video

## References

1. <a id="cite-ref-1" href="#cite-note-1">[1]</a> The black king of the djinns, Al-Malik al-Aswad, from the late 14th century [Book of Wonders](https://en.wikipedia.org/wiki/Book_of_Wonders), [Bodleian Libraries](https://en.wikipedia.org/wiki/Bodleian_Libraries) Shelfmark; MS. Bodl. Or. 133. Fol. 30b, [Wikimedia Commons](https://en.wikipedia.org/wiki/Wikimedia_Commons)
1. <a id="cite-ref-2" href="#cite-note-2">[2]</a> [Djinn 0.815 Available](http://www.open-aurec.com/wbforum/viewtopic.php?f=18&t=45757) by [Tom Likens](Tom_Likens "Tom Likens"), [Winboard Forum](Computer_Chess_Forums "Computer Chess Forums"), December 25, 2003
1. <a id="cite-ref-3" href="#cite-note-3">[3]</a> [Computer Chess Programming Topics](https://web.archive.org/web/20180220175920/http://webpages.charter.net/tlikens/tech.html) ([Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine))
1. <a id="cite-ref-4" href="#cite-note-4">[4]</a> [CCT6 - PGN download](http://www.vrichey.de/cct6/) hosted by [Volker Richey](index.php?title=Volker_Richey&action=edit&redlink=1 "Volker Richey (page does not exist)")

**[Up one level](Engines "Engines")**

